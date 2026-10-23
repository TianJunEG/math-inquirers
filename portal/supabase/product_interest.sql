-- Math Inquirers: shop "Tell me when it's ready" (product interest). Run AFTER schema.sql and policies.sql.
-- Safe to re-run (idempotent). If you ever re-run policies.sql (it revokes every function grant), re-run this file after it.
-- NOT applied to the live database by the author: REVIEW FIRST, then paste into the Supabase SQL editor.
-- Same design as interest_requests.sql ("Request another time"); that file is the pattern this one copies.
--
-- Design
--   * Parents are anonymous visitors on the public site (/shop/). They have NO table privileges at all: anon cannot select,
--     insert, update or delete. The only way in is the SECURITY DEFINER function submit_product_interest(), which validates every
--     field, applies the one-per-contact-per-day limit and a global hourly cap, and stores the row. It is NOT an order and takes
--     no payment: it only records who wants to hear when which product is ready.
--   * No personal data in logs: every error message is a fixed word (never an input value) and the function never uses
--     RAISE NOTICE / WARNING with values.
--   * Only admins (rows in public.admins, checked by is_admin()) can read the tally or the list, change status, or delete.
--   * Data minimised: parent FIRST name only (never a child's name or age), at least one of a WhatsApp number or an email,
--     and the items asked for as [{product, format, qty}] (no prices are ever stored or accepted).
--   * Product ids are free text here on purpose (pattern ^[a-z0-9-]{1,24}$): the catalogue lives in website/data/products.json,
--     so adding a product needs no database change. Format is 'soft' (PDF download) or 'physical' (printed, posted in Singapore).
--   * Retention (DEFAULT, for the owner and a lawyer to confirm): 12 months from the request, then deleted by
--     admin_purge_expired_product_interest(). Change the interval in the expires_at default below AND in website/privacy.html
--     and the consent wording in website/shop_build.py if you decide differently.

create extension if not exists pgcrypto with schema extensions;

create table if not exists public.product_interest (
  id               uuid primary key default gen_random_uuid(),
  created_at       timestamptz not null default now(),
  expires_at       timestamptz not null default (now() + interval '12 months'),   -- DEFAULT retention: 12 months
  parent_first_name text       not null check (char_length(btrim(parent_first_name)) between 1 and 40),
  contact_whatsapp text        check (contact_whatsapp is null or contact_whatsapp ~ '^[0-9]{8,15}$'),
  contact_email    text        check (contact_email is null or (char_length(contact_email) <= 120 and contact_email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$')),
  items            jsonb       not null check (jsonb_typeof(items) = 'array' and jsonb_array_length(items) between 1 and 12),   -- [{"product":"ext-l1","format":"soft","qty":1}]
  note             text        check (note is null or char_length(note) <= 400),
  consent_at       timestamptz not null default now(),
  consent_version  text        not null check (char_length(consent_version) between 1 and 40),
  status           text        not null default 'new' check (status in ('new','notified','closed')),   -- notified = we told them the product is ready
  check (contact_whatsapp is not null or contact_email is not null)
);
create index if not exists product_interest_created_idx on public.product_interest (created_at desc);
create index if not exists product_interest_expires_idx on public.product_interest (expires_at);
create index if not exists product_interest_wa_idx      on public.product_interest (contact_whatsapp, created_at) where contact_whatsapp is not null;
create index if not exists product_interest_email_idx   on public.product_interest (contact_email, created_at) where contact_email is not null;

alter table public.product_interest enable row level security;   -- deliberately NO policy: nobody reads through the API directly
revoke all on public.product_interest from anon, authenticated;

-- ---------- parent-facing: the only write path ----------
-- p_items: json array of {"product": text, "format": "soft"|"physical", "qty": 1..10}. Returns {"ok":true,"status":"received"} or
-- {"ok":true,"status":"already_received"} (same contact within 24 hours). Raises one of: invalid_input, consent_required, busy.
-- Never echoes input.
create or replace function public.submit_product_interest(
  p_first_name text, p_whatsapp text, p_email text, p_items jsonb, p_note text,
  p_consent boolean, p_consent_version text, p_hp text default null
) returns jsonb
language plpgsql volatile security definer set search_path = public as $$
declare
  v_wa    text;
  v_em    text;
  v_name  text  := btrim(regexp_replace(coalesce(p_first_name, ''), '[[:cntrl:]]', ' ', 'g'));
  v_note  text  := nullif(btrim(regexp_replace(coalesce(p_note, ''), '[[:cntrl:]]', ' ', 'g')), '');
  v_ver   text  := btrim(coalesce(p_consent_version, ''));
  v_items jsonb;
  e       jsonb;
begin
  -- honeypot: a bot filled the hidden field. Pretend success, store nothing.
  if p_hp is not null and btrim(p_hp) <> '' then return jsonb_build_object('ok', true, 'status', 'received'); end if;

  if p_consent is distinct from true then raise exception 'consent_required' using errcode = '22023'; end if;
  if char_length(v_name) not between 1 and 40 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if v_note is not null and char_length(v_note) > 400 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if char_length(v_ver) not between 1 and 40 then raise exception 'invalid_input' using errcode = '22023'; end if;

  -- items: 1 to 12 objects, each with a plain product id, a known format and a small quantity
  if p_items is null or jsonb_typeof(p_items) <> 'array' or jsonb_array_length(p_items) not between 1 and 12 then
    raise exception 'invalid_input' using errcode = '22023';
  end if;
  for e in select * from jsonb_array_elements(p_items) loop
    if jsonb_typeof(e) <> 'object'
       or jsonb_typeof(e->'product') is distinct from 'string' or (e->>'product') !~ '^[a-z0-9-]{1,24}$'
       or jsonb_typeof(e->'format')  is distinct from 'string' or (e->>'format') not in ('soft','physical')
       or jsonb_typeof(e->'qty')     is distinct from 'number' or (e->>'qty') !~ '^[0-9]{1,2}$' or (e->>'qty')::int not between 1 and 10 then
      raise exception 'invalid_input' using errcode = '22023';
    end if;
  end loop;
  -- normalise: one line per (product, format); a soft copy is always quantity 1; stored keys are exactly product, format, qty
  select jsonb_agg(jsonb_build_object('product', product, 'format', format, 'qty', qty) order by product, format)
    into v_items
    from (select e2->>'product' as product, e2->>'format' as format,
                 case when e2->>'format' = 'soft' then 1 else max((e2->>'qty')::int) end as qty
            from jsonb_array_elements(p_items) e2
           group by e2->>'product', e2->>'format') n;

  -- contact: normalise. WhatsApp keeps digits only; a Singapore number written with 65 in front is stored as the 8 digits.
  v_wa := nullif(regexp_replace(coalesce(p_whatsapp, ''), '[^0-9]', '', 'g'), '');
  if v_wa is not null and char_length(v_wa) = 10 and left(v_wa, 2) = '65' then v_wa := substr(v_wa, 3); end if;
  if v_wa is not null and v_wa !~ '^[0-9]{8,15}$' then raise exception 'invalid_input' using errcode = '22023'; end if;
  v_em := nullif(lower(btrim(coalesce(p_email, ''))), '');
  if v_em is not null and (char_length(v_em) > 120 or v_em !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$') then raise exception 'invalid_input' using errcode = '22023'; end if;
  if v_wa is null and v_em is null then raise exception 'invalid_input' using errcode = '22023'; end if;

  -- global cap (abuse brake): at most 300 requests an hour across the whole shop
  if (select count(*) from public.product_interest where created_at > now() - interval '1 hour') >= 300 then
    raise exception 'busy' using errcode = '53400';
  end if;
  -- one request per contact per day
  if exists (select 1 from public.product_interest r
              where r.created_at > now() - interval '24 hours'
                and ((v_wa is not null and r.contact_whatsapp = v_wa) or (v_em is not null and r.contact_email = v_em))) then
    return jsonb_build_object('ok', true, 'status', 'already_received');
  end if;

  insert into public.product_interest (parent_first_name, contact_whatsapp, contact_email, items, note, consent_version)
  values (v_name, v_wa, v_em, v_items, v_note, v_ver);
  return jsonb_build_object('ok', true, 'status', 'received');
end $$;

-- ---------- admin only ----------
-- Tally: one row per (product, format): how many requests asked for it (requests) and how many copies (copies: physical quantities, soft = 1 each).
-- product '*' / format '*' gives the number of requests in total.
create or replace function public.admin_product_interest_tally() returns table (product text, format text, requests bigint, copies bigint)
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
  select '*'::text, '*'::text, count(*), count(*) from public.product_interest r
  union all
  select i->>'product', i->>'format', count(*), coalesce(sum((i->>'qty')::int), 0)::bigint
    from public.product_interest r, jsonb_array_elements(r.items) i group by 1, 2
  order by 1, 2;
end $$;

create or replace function public.admin_list_product_interest() returns table (
  id uuid, created_at timestamptz, expires_at timestamptz, parent_first_name text, contact_whatsapp text, contact_email text,
  items jsonb, note text, status text)
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
  select r.id, r.created_at, r.expires_at, r.parent_first_name, r.contact_whatsapp, r.contact_email, r.items, r.note, r.status
    from public.product_interest r order by r.created_at desc limit 1000;
end $$;

create or replace function public.admin_set_product_interest_status(p_id uuid, p_status text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  if p_status not in ('new','notified','closed') then raise exception 'invalid_input' using errcode = '22023'; end if;
  update public.product_interest set status = p_status where id = p_id;
end $$;

-- Deletion on request (PDPA) or when a parent asks to be removed.
create or replace function public.admin_delete_product_interest(p_id uuid) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  delete from public.product_interest where id = p_id;
end $$;

-- Retention: deletes requests past expires_at (default 12 months). Run it from the admin page or the SQL editor now and then,
-- or schedule it (Supabase: Database > Extensions > pg_cron), for example:
--   select cron.schedule('purge-product-interest', '20 3 * * *', $$delete from public.product_interest where expires_at < now()$$);
create or replace function public.admin_purge_expired_product_interest() returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  delete from public.product_interest where expires_at < now();
  get diagnostics n = row_count;
  return n;
end $$;

-- ---------- grants (everything revoked first, then granted narrowly) ----------
revoke all on function public.submit_product_interest(text, text, text, jsonb, text, boolean, text, text) from public, anon, authenticated;
revoke all on function public.admin_product_interest_tally()                  from public, anon, authenticated;
revoke all on function public.admin_list_product_interest()                   from public, anon, authenticated;
revoke all on function public.admin_set_product_interest_status(uuid, text)   from public, anon, authenticated;
revoke all on function public.admin_delete_product_interest(uuid)             from public, anon, authenticated;
revoke all on function public.admin_purge_expired_product_interest()          from public, anon, authenticated;

grant execute on function public.submit_product_interest(text, text, text, jsonb, text, boolean, text, text) to anon, authenticated;
grant execute on function public.admin_product_interest_tally()                to authenticated;   -- is_admin() checked inside
grant execute on function public.admin_list_product_interest()                 to authenticated;
grant execute on function public.admin_set_product_interest_status(uuid, text) to authenticated;
grant execute on function public.admin_delete_product_interest(uuid)           to authenticated;
grant execute on function public.admin_purge_expired_product_interest()        to authenticated;

-- Quick tally for the SQL editor (no admin login needed there):
--   select i->>'product' as product, i->>'format' as format, count(*) as requests, sum((i->>'qty')::int) as copies
--     from public.product_interest, jsonb_array_elements(items) i group by 1, 2 order by 1, 2;
