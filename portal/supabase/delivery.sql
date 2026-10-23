-- Math Inquirers: soft-copy delivery (expiring download links). REVIEW FIRST, do not run until the owner has read docs/shop/delivery_plan.md.
-- Run AFTER schema.sql and policies.sql (needs public.is_admin()). Idempotent: safe to re-run. Touches no existing table.
--
-- Design (details in docs/shop/delivery_plan.md):
--   * public.entitlements: one row per file a buyer may download. The download link token is NEVER stored; only its SHA-256 hash (token_hash).
--     The Worker derives the token as HMAC-SHA256(DELIVERY_TOKEN_SALT, link_nonce), so a database-only leak cannot rebuild any link.
--   * public.delivery_log: one row per download attempt (outcome + entitlement + salted-hash of the IP for rate limiting). No email, no name,
--     no raw IP. Purge rows older than 90 days (function below).
--   * RLS is ON for both tables with NO policy and NO grant: anon/authenticated cannot read or write them. Only service_role
--     (the Cloudflare Functions) and the admin_* SECURITY DEFINER functions (is_admin() checked inside) touch them.

create table if not exists public.entitlements (
  id                uuid primary key default gen_random_uuid(),
  order_id          text not null check (length(order_id) between 1 and 80),          -- shop order reference, or 'MANUAL-xxxx' for an admin link
  stripe_session_id text,                                                              -- cs_... (null for manual links)
  product_id        text not null check (length(product_id) between 1 and 80),
  format            text not null default 'pdf' check (format in ('pdf','zip','other')),
  buyer_email       text check (buyer_email is null or length(buyer_email) <= 254),   -- null for a link handed over on WhatsApp
  r2_key            text not null check (length(r2_key) between 1 and 300),          -- key inside the private R2 bucket
  filename          text not null check (length(filename) between 1 and 150),        -- name offered to the buyer in Content-Disposition
  file_version      text,
  file_sha256       text check (file_sha256 is null or file_sha256 ~ '^[0-9a-f]{64}$'),
  link_nonce        text not null check (length(link_nonce) between 20 and 100),     -- random; token = HMAC(DELIVERY_TOKEN_SALT, nonce)
  token_hash        text not null unique check (token_hash ~ '^[0-9a-f]{64}$'),      -- SHA-256 hex of the token
  expires_at        timestamptz not null,
  max_downloads     int not null default 5 check (max_downloads between 1 and 100),
  download_count    int not null default 0 check (download_count >= 0),
  last_download_at  timestamptz,
  revoked_at        timestamptz,
  revoked_reason    text,
  source            text not null default 'stripe' check (source in ('stripe','manual')),
  note              text check (note is null or length(note) <= 300),
  created_by        uuid,                                                              -- admin user id for manual links
  email_claimed_at  timestamptz,                                                       -- lease so two webhook retries do not both send the email
  emailed_at        timestamptz,
  created_at        timestamptz not null default now()
);
create unique index if not exists entitlements_session_product_uq on public.entitlements (stripe_session_id, product_id, format) where stripe_session_id is not null;
create index if not exists entitlements_order_idx   on public.entitlements (order_id);
create index if not exists entitlements_session_idx on public.entitlements (stripe_session_id) where stripe_session_id is not null;
create index if not exists entitlements_created_idx on public.entitlements (created_at desc);

create table if not exists public.delivery_log (
  id             bigint generated always as identity primary key,
  at             timestamptz not null default now(),
  entitlement_id uuid references public.entitlements(id) on delete set null,
  order_id       text,
  outcome        text not null,        -- ok, ok_range, not_found, expired, revoked, exhausted, rate_limited, range_denied, storage_missing, links_view
  ip_hash        text                  -- HMAC of the IP with DELIVERY_TOKEN_SALT, for rate limiting only; not reversible without the salt
);
create index if not exists delivery_log_ip_idx  on public.delivery_log (ip_hash, at desc) where ip_hash is not null;
create index if not exists delivery_log_at_idx  on public.delivery_log (at);

alter table public.entitlements enable row level security;   -- no policy, no grant: invisible to anon and logged-in users
alter table public.delivery_log enable row level security;
revoke all on public.entitlements from public, anon, authenticated;
revoke all on public.delivery_log from public, anon, authenticated;
revoke all on sequence public.delivery_log_id_seq from public, anon, authenticated;
grant select, insert, update on public.entitlements to service_role;
grant select, insert, delete on public.delivery_log to service_role;
grant usage on sequence public.delivery_log_id_seq to service_role;

-- ---------- service_role functions (called by the Cloudflare Functions) ----------

-- Idempotent grant: the same (Stripe session, product, format) returns the existing row (created=false), so a repeated webhook mints no second link.
create or replace function public.service_grant_entitlement(
  p_order_id text, p_session_id text, p_product_id text, p_format text, p_email text,
  p_r2_key text, p_filename text, p_version text, p_sha256 text,
  p_nonce text, p_token_hash text, p_expires_at timestamptz, p_max int,
  p_source text default 'stripe', p_note text default null, p_created_by uuid default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare r public.entitlements; made boolean := true;
begin
  insert into public.entitlements (order_id, stripe_session_id, product_id, format, buyer_email, r2_key, filename, file_version, file_sha256,
                                   link_nonce, token_hash, expires_at, max_downloads, source, note, created_by)
  values (p_order_id, p_session_id, p_product_id, coalesce(p_format,'pdf'), nullif(lower(trim(p_email)),''), p_r2_key, p_filename, p_version, p_sha256,
          p_nonce, p_token_hash, p_expires_at, coalesce(p_max,5), p_source, p_note, p_created_by)
  on conflict (stripe_session_id, product_id, format) where stripe_session_id is not null do nothing
  returning * into r;
  if r.id is null then
    made := false;
    select * into r from public.entitlements e where e.stripe_session_id = p_session_id and e.product_id = p_product_id and e.format = coalesce(p_format,'pdf');
  end if;
  return jsonb_build_object('created', made, 'id', r.id, 'order_id', r.order_id, 'product_id', r.product_id, 'format', r.format,
    'filename', r.filename, 'link_nonce', r.link_nonce, 'token_hash', r.token_hash, 'expires_at', r.expires_at, 'max_downloads', r.max_downloads,
    'buyer_email', r.buyer_email, 'emailed_at', r.emailed_at);
end $$;

-- Rows of one checkout session for the order success page and for the email. Returns nothing for an unknown session.
create or replace function public.service_order_entitlements(p_session_id text)
returns table (id uuid, order_id text, product_id text, format text, filename text, link_nonce text, expires_at timestamptz,
               max_downloads int, download_count int, revoked boolean, buyer_email text, emailed_at timestamptz)
language sql stable security definer set search_path = public as $$
  select e.id, e.order_id, e.product_id, e.format, e.filename, e.link_nonce, e.expires_at, e.max_downloads, e.download_count,
         (e.revoked_at is not null), e.buyer_email, e.emailed_at
  from public.entitlements e where e.stripe_session_id = p_session_id and p_session_id is not null order by e.created_at, e.product_id;
$$;

-- Atomic lease: returns true to exactly one caller per 10 minutes while the order's email is not yet sent.
create or replace function public.service_claim_email(p_session_id text) returns boolean
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  update public.entitlements set email_claimed_at = now()
   where stripe_session_id = p_session_id and emailed_at is null and buyer_email is not null
     and (email_claimed_at is null or email_claimed_at < now() - interval '10 minutes');
  get diagnostics n = row_count;
  return n > 0;
end $$;

create or replace function public.service_mark_emailed(p_session_id text) returns void
language sql security definer set search_path = public as $$
  update public.entitlements set emailed_at = now() where stripe_session_id = p_session_id and emailed_at is null;
$$;

-- One call per download request. Validates, rate-limits, logs, and (when p_count) consumes one download. Returns {status, ...}.
--   p_count = true  : a normal full request (or a range starting at byte 0): uses one of max_downloads.
--   p_count = false : a range that starts after byte 0 (resume of a download that already started): free, but only within 2 hours of a counted
--                     download, so ranges cannot be used to fetch the file without ever being counted.
create or replace function public.service_download_begin(p_token_hash text, p_ip_hash text, p_count boolean,
                                                         p_rate_max int default 30, p_rate_window_min int default 10)
returns jsonb language plpgsql security definer set search_path = public as $$
declare e public.entitlements; recent int; st text;
begin
  if p_ip_hash is not null then
    select count(*) into recent from public.delivery_log l where l.ip_hash = p_ip_hash and l.at > now() - make_interval(mins => p_rate_window_min);
    if recent >= p_rate_max then
      insert into public.delivery_log (outcome, ip_hash) values ('rate_limited', p_ip_hash);
      return jsonb_build_object('status', 'rate_limited');
    end if;
  end if;
  select * into e from public.entitlements where token_hash = p_token_hash for update;
  if not found then
    insert into public.delivery_log (outcome, ip_hash) values ('not_found', p_ip_hash);
    return jsonb_build_object('status', 'not_found');
  end if;
  if e.revoked_at is not null then st := 'revoked';
  elsif e.expires_at <= now() then st := 'expired';
  elsif p_count and e.download_count >= e.max_downloads then st := 'exhausted';
  elsif not p_count and (e.download_count = 0 or e.last_download_at is null or e.last_download_at < now() - interval '2 hours') then st := 'range_denied';
  end if;
  if st is not null then
    insert into public.delivery_log (entitlement_id, order_id, outcome, ip_hash) values (e.id, e.order_id, st, p_ip_hash);
    return jsonb_build_object('status', st);
  end if;
  if p_count then
    update public.entitlements set download_count = download_count + 1, last_download_at = now() where id = e.id;
    e.download_count := e.download_count + 1;
  end if;
  insert into public.delivery_log (entitlement_id, order_id, outcome, ip_hash) values (e.id, e.order_id, case when p_count then 'ok' else 'ok_range' end, p_ip_hash);
  return jsonb_build_object('status', 'ok', 'entitlement_id', e.id, 'r2_key', e.r2_key, 'filename', e.filename, 'sha256', e.file_sha256,
                            'order_id', e.order_id, 'remaining', e.max_downloads - e.download_count);
end $$;

-- Give the download back when the file could not be read from storage (our fault, not the buyer's).
create or replace function public.service_download_release(p_entitlement uuid) returns void
language plpgsql security definer set search_path = public as $$
begin
  update public.entitlements set download_count = greatest(download_count - 1, 0) where id = p_entitlement;
  insert into public.delivery_log (entitlement_id, order_id, outcome) select id, order_id, 'storage_missing' from public.entitlements where id = p_entitlement;
end $$;

-- Success-page lookups share the same rate limit table (outcome 'links_view').
create or replace function public.service_links_rate(p_ip_hash text, p_max int default 20, p_window_min int default 10) returns boolean
language plpgsql security definer set search_path = public as $$
declare recent int;
begin
  select count(*) into recent from public.delivery_log where ip_hash = p_ip_hash and outcome = 'links_view' and at > now() - make_interval(mins => p_window_min);
  if recent >= p_max then return false; end if;
  insert into public.delivery_log (outcome, ip_hash) values ('links_view', p_ip_hash);
  return true;
end $$;

create or replace function public.service_purge_delivery_log(p_days int default 90) returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  delete from public.delivery_log where at < now() - make_interval(days => p_days);
  get diagnostics n = row_count;
  return n;
end $$;

-- ---------- admin functions (logged-in admin only; is_admin() is checked inside) ----------

create or replace function public.admin_list_entitlements(p_limit int default 100)
returns table (id uuid, order_id text, product_id text, format text, filename text, buyer_email text, source text, note text,
               expires_at timestamptz, max_downloads int, download_count int, last_download_at timestamptz, revoked_at timestamptz,
               emailed_at timestamptz, created_at timestamptz)
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query select e.id, e.order_id, e.product_id, e.format, e.filename, e.buyer_email, e.source, e.note, e.expires_at, e.max_downloads,
                      e.download_count, e.last_download_at, e.revoked_at, e.emailed_at, e.created_at
               from public.entitlements e order by e.created_at desc limit least(greatest(p_limit,1), 500);
end $$;

create or replace function public.admin_revoke_entitlement(p_id uuid, p_reason text default null) returns boolean
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  update public.entitlements set revoked_at = now(), revoked_reason = left(p_reason, 200) where id = p_id and revoked_at is null;
  get diagnostics n = row_count;
  return n > 0;
end $$;

-- Resend: extends the expiry, optionally gives the downloads back, un-revokes nothing (a revoked link stays revoked: grant a new one).
-- Returns what the Function needs to rebuild the same link and email it.
create or replace function public.admin_prepare_resend(p_id uuid, p_extend_days int default 14, p_reset_count boolean default false)
returns table (id uuid, order_id text, product_id text, filename text, buyer_email text, link_nonce text, expires_at timestamptz, max_downloads int)
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
  with u as (
    update public.entitlements e set
        expires_at = greatest(e.expires_at, now() + make_interval(days => least(greatest(p_extend_days,1), 90))),
        download_count = case when p_reset_count then 0 else e.download_count end
      where e.id = p_id and e.revoked_at is null
      returning e.id, e.order_id, e.product_id, e.filename, e.buyer_email, e.link_nonce, e.expires_at, e.max_downloads)
  select u.id, u.order_id, u.product_id, u.filename, u.buyer_email, u.link_nonce, u.expires_at, u.max_downloads from u;
end $$;

-- Manual link (beta PDF fallback, WhatsApp delivery) without payment. The Function generates nonce + token_hash and passes them in.
create or replace function public.admin_create_manual_entitlement(
  p_label text, p_r2_key text, p_filename text, p_email text, p_nonce text, p_token_hash text, p_days int default 14, p_max int default 5, p_note text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare r public.entitlements;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  insert into public.entitlements (order_id, product_id, format, buyer_email, r2_key, filename, link_nonce, token_hash, expires_at, max_downloads, source, note, created_by)
  values ('MANUAL-' || upper(substr(replace(gen_random_uuid()::text,'-',''),1,8)), left(coalesce(nullif(p_label,''),'manual'),80), 'pdf', nullif(lower(trim(p_email)),''),
          p_r2_key, p_filename, p_nonce, p_token_hash, now() + make_interval(days => least(greatest(p_days,1),90)), least(greatest(p_max,1),100), 'manual', left(p_note,300), auth.uid())
  returning * into r;
  return jsonb_build_object('id', r.id, 'order_id', r.order_id, 'expires_at', r.expires_at, 'max_downloads', r.max_downloads, 'filename', r.filename);
end $$;

create or replace function public.admin_purge_delivery_log(p_days int default 90) returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  delete from public.delivery_log where at < now() - make_interval(days => greatest(p_days,1));
  get diagnostics n = row_count;
  return n;
end $$;

-- Retention (owner decision: purchase records kept 7 years; download log 90 days). Schedule with pg_cron if wanted:
--   select cron.schedule('purge-delivery-log', '20 3 * * *', $$delete from public.delivery_log where at < now() - interval '90 days'$$);
-- Expired entitlement rows stay (they are the purchase record); delete buyer_email after the retention period decided with the lawyer.

-- ---------- grants (everything revoked first, then granted narrowly) ----------
revoke all on function public.service_grant_entitlement(text,text,text,text,text,text,text,text,text,text,text,timestamptz,int,text,text,uuid) from public, anon, authenticated;
revoke all on function public.service_order_entitlements(text)               from public, anon, authenticated;
revoke all on function public.service_claim_email(text)                      from public, anon, authenticated;
revoke all on function public.service_mark_emailed(text)                     from public, anon, authenticated;
revoke all on function public.service_download_begin(text,text,boolean,int,int) from public, anon, authenticated;
revoke all on function public.service_download_release(uuid)                 from public, anon, authenticated;
revoke all on function public.service_links_rate(text,int,int)               from public, anon, authenticated;
revoke all on function public.service_purge_delivery_log(int)                from public, anon, authenticated;
revoke all on function public.admin_list_entitlements(int)                   from public, anon, authenticated;
revoke all on function public.admin_revoke_entitlement(uuid,text)            from public, anon, authenticated;
revoke all on function public.admin_prepare_resend(uuid,int,boolean)         from public, anon, authenticated;
revoke all on function public.admin_create_manual_entitlement(text,text,text,text,text,text,int,int,text) from public, anon, authenticated;
revoke all on function public.admin_purge_delivery_log(int)                  from public, anon, authenticated;

grant execute on function public.service_grant_entitlement(text,text,text,text,text,text,text,text,text,text,text,timestamptz,int,text,text,uuid) to service_role;
grant execute on function public.service_order_entitlements(text)            to service_role;
grant execute on function public.service_claim_email(text)                   to service_role;
grant execute on function public.service_mark_emailed(text)                  to service_role;
grant execute on function public.service_download_begin(text,text,boolean,int,int) to service_role;
grant execute on function public.service_download_release(uuid)              to service_role;
grant execute on function public.service_links_rate(text,int,int)            to service_role;
grant execute on function public.service_purge_delivery_log(int)             to service_role;
grant execute on function public.admin_list_entitlements(int)                to authenticated;   -- is_admin() checked inside
grant execute on function public.admin_revoke_entitlement(uuid,text)         to authenticated;
grant execute on function public.admin_prepare_resend(uuid,int,boolean)      to authenticated;
grant execute on function public.admin_create_manual_entitlement(text,text,text,text,text,text,int,int,text) to authenticated;
grant execute on function public.admin_purge_delivery_log(int)               to authenticated;
