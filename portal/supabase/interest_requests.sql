-- Math Inquirers: "Request another time" (timing interest) requests. Run AFTER schema.sql and policies.sql.
-- Safe to re-run (idempotent). If you ever re-run policies.sql (it revokes every function grant), re-run this file after it.
-- NOT applied to the live database by the author: review first, then paste into the Supabase SQL editor.
--
-- Design
--   * Parents are anonymous visitors on the public site. They have NO table privileges at all: anon cannot select,
--     insert, update or delete. The only way in is the SECURITY DEFINER function submit_interest_request(), which
--     validates every field, applies the one-per-contact-per-day limit and a global hourly cap, and stores the row.
--   * No personal data in logs: every error message is a fixed word (never an input value) and the function never
--     uses RAISE NOTICE / WARNING with values.
--   * Only admins (rows in public.admins, checked by is_admin()) can read the tally, list or delete requests.
--   * Data minimised: parent FIRST name only, child age BAND (never the child's name or birth date), and at least one of
--     a WhatsApp number or an email.
--   * Retention (DEFAULT, for the owner and a lawyer to confirm): 12 months from the request, then deleted by
--     admin_purge_expired_interest_requests(). Change the interval in the expires_at default below AND in
--     website/privacy.html if you decide differently.

create extension if not exists pgcrypto with schema extensions;

create table if not exists public.interest_requests (
  id               uuid primary key default gen_random_uuid(),
  created_at       timestamptz not null default now(),
  expires_at       timestamptz not null default (now() + interval '12 months'),   -- DEFAULT retention: 12 months
  level            smallint    not null check (level between 1 and 6),
  age_band         text        not null check (age_band in ('under-6','6-7','8-9','10-11','12-13','14-plus')),
  slots            text[]      not null default '{}' check (cardinality(slots) <= 12),
  windows          text[]      not null default '{}' check (cardinality(windows) <= 8),
  other_time       text        check (other_time is null or char_length(other_time) <= 200),
  parent_first_name text       not null check (char_length(btrim(parent_first_name)) between 1 and 40),
  contact_whatsapp text        check (contact_whatsapp is null or contact_whatsapp ~ '^[0-9]{8,15}$'),
  contact_email    text        check (contact_email is null or (char_length(contact_email) <= 120 and contact_email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$')),
  note             text        check (note is null or char_length(note) <= 400),
  consent_at       timestamptz not null default now(),
  consent_version  text        not null check (char_length(consent_version) between 1 and 40),
  status           text        not null default 'new' check (status in ('new','contacted','closed')),
  check (contact_whatsapp is not null or contact_email is not null),
  check (cardinality(slots) > 0 or cardinality(windows) > 0 or other_time is not null)
);
create index if not exists interest_requests_created_idx  on public.interest_requests (created_at desc);
create index if not exists interest_requests_expires_idx  on public.interest_requests (expires_at);
create index if not exists interest_requests_wa_idx       on public.interest_requests (contact_whatsapp, created_at) where contact_whatsapp is not null;
create index if not exists interest_requests_email_idx    on public.interest_requests (contact_email, created_at) where contact_email is not null;

alter table public.interest_requests enable row level security;   -- deliberately NO policy: nobody reads through the API directly
revoke all on public.interest_requests from anon, authenticated;

-- ---------- parent-facing: the only write path ----------
-- Returns {"ok":true,"status":"received"} or {"ok":true,"status":"already_received"} (same contact within 24 hours).
-- Raises one of: invalid_input, consent_required, busy. Never echoes input.
create or replace function public.submit_interest_request(
  p_level int, p_age_band text, p_slots text[], p_windows text[], p_other_time text,
  p_first_name text, p_whatsapp text, p_email text, p_note text,
  p_consent boolean, p_consent_version text, p_hp text default null
) returns jsonb
language plpgsql volatile security definer set search_path = public as $$
declare
  v_wa    text;
  v_em    text;
  v_name  text := btrim(regexp_replace(coalesce(p_first_name, ''), '[[:cntrl:]]', ' ', 'g'));
  v_other text := nullif(btrim(regexp_replace(coalesce(p_other_time, ''), '[[:cntrl:]]', ' ', 'g')), '');
  v_note  text := nullif(btrim(regexp_replace(coalesce(p_note, ''), '[[:cntrl:]]', ' ', 'g')), '');
  v_slots text[] := coalesce(p_slots, '{}');
  v_wins  text[] := coalesce(p_windows, '{}');
  v_ver   text := btrim(coalesce(p_consent_version, ''));
  s text;
begin
  -- honeypot: a bot filled the hidden field. Pretend success, store nothing.
  if p_hp is not null and btrim(p_hp) <> '' then return jsonb_build_object('ok', true, 'status', 'received'); end if;

  if p_consent is distinct from true then raise exception 'consent_required' using errcode = '22023'; end if;
  if p_level is null or p_level not between 1 and 6 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if p_age_band is null or p_age_band not in ('under-6','6-7','8-9','10-11','12-13','14-plus') then raise exception 'invalid_input' using errcode = '22023'; end if;
  if char_length(v_name) not between 1 and 40 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if v_other is not null and char_length(v_other) > 200 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if v_note  is not null and char_length(v_note)  > 400 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if char_length(v_ver) not between 1 and 40 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if cardinality(v_slots) > 12 or cardinality(v_wins) > 8 then raise exception 'invalid_input' using errcode = '22023'; end if;
  foreach s in array v_slots loop
    if s is null or s !~ '^[A-Za-z0-9-]{1,16}$' then raise exception 'invalid_input' using errcode = '22023'; end if;
  end loop;
  foreach s in array v_wins loop
    if s is null or s !~ '^[a-z-]{1,16}$' then raise exception 'invalid_input' using errcode = '22023'; end if;
  end loop;
  if cardinality(v_slots) = 0 and cardinality(v_wins) = 0 and v_other is null then raise exception 'invalid_input' using errcode = '22023'; end if;

  -- contact: normalise. WhatsApp keeps digits only; a Singapore number written with 65 in front is stored as the 8 digits.
  v_wa := nullif(regexp_replace(coalesce(p_whatsapp, ''), '[^0-9]', '', 'g'), '');
  if v_wa is not null and char_length(v_wa) = 10 and left(v_wa, 2) = '65' then v_wa := substr(v_wa, 3); end if;
  if v_wa is not null and v_wa !~ '^[0-9]{8,15}$' then raise exception 'invalid_input' using errcode = '22023'; end if;
  v_em := nullif(lower(btrim(coalesce(p_email, ''))), '');
  if v_em is not null and (char_length(v_em) > 120 or v_em !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$') then raise exception 'invalid_input' using errcode = '22023'; end if;
  if v_wa is null and v_em is null then raise exception 'invalid_input' using errcode = '22023'; end if;

  -- global cap (abuse brake): at most 300 requests an hour across the whole site
  if (select count(*) from public.interest_requests where created_at > now() - interval '1 hour') >= 300 then
    raise exception 'busy' using errcode = '53400';
  end if;
  -- one request per contact per day
  if exists (select 1 from public.interest_requests r
              where r.created_at > now() - interval '24 hours'
                and ((v_wa is not null and r.contact_whatsapp = v_wa) or (v_em is not null and r.contact_email = v_em))) then
    return jsonb_build_object('ok', true, 'status', 'already_received');
  end if;

  insert into public.interest_requests (level, age_band, slots, windows, other_time, parent_first_name, contact_whatsapp, contact_email, note, consent_version)
  values (p_level, p_age_band, (select coalesce(array_agg(distinct x), '{}') from unnest(v_slots) x),
          (select coalesce(array_agg(distinct x), '{}') from unnest(v_wins) x), v_other, v_name, v_wa, v_em, v_note, v_ver);
  return jsonb_build_object('ok', true, 'status', 'received');
end $$;

-- ---------- admin only ----------
-- Tally: one row per (level, kind, key). kind = 'slot' (a placeholder slot id), 'window' (a day/time chip) or 'other' (free text given).
-- Each request counts once per distinct key. key = '*' with kind 'total' gives the number of requests for that level.
create or replace function public.admin_interest_tally() returns table (level smallint, kind text, key text, n bigint)
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
  select r.level, 'total'::text, '*'::text, count(*) from public.interest_requests r group by r.level
  union all
  select r.level, 'slot'::text, s, count(*) from public.interest_requests r, unnest(r.slots) s group by r.level, s
  union all
  select r.level, 'window'::text, w, count(*) from public.interest_requests r, unnest(r.windows) w group by r.level, w
  union all
  select r.level, 'other'::text, 'free-text'::text, count(*) from public.interest_requests r where r.other_time is not null group by r.level
  order by 1, 2, 3;
end $$;

create or replace function public.admin_list_interest_requests() returns table (
  id uuid, created_at timestamptz, expires_at timestamptz, level smallint, age_band text, slots text[], windows text[], other_time text,
  parent_first_name text, contact_whatsapp text, contact_email text, note text, status text)
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
  select r.id, r.created_at, r.expires_at, r.level, r.age_band, r.slots, r.windows, r.other_time, r.parent_first_name,
         r.contact_whatsapp, r.contact_email, r.note, r.status
    from public.interest_requests r order by r.created_at desc limit 1000;
end $$;

create or replace function public.admin_set_interest_status(p_id uuid, p_status text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  if p_status not in ('new','contacted','closed') then raise exception 'invalid_input' using errcode = '22023'; end if;
  update public.interest_requests set status = p_status where id = p_id;
end $$;

-- Deletion on request (PDPA) or when a parent asks to be removed.
create or replace function public.admin_delete_interest_request(p_id uuid) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  delete from public.interest_requests where id = p_id;
end $$;

-- Retention: deletes requests past expires_at (default 12 months). Run it from the admin page or the SQL editor now and then,
-- or schedule it (Supabase: Database > Extensions > pg_cron), for example:
--   select cron.schedule('purge-interest-requests', '15 3 * * *', $$delete from public.interest_requests where expires_at < now()$$);
create or replace function public.admin_purge_expired_interest_requests() returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  delete from public.interest_requests where expires_at < now();
  get diagnostics n = row_count;
  return n;
end $$;

-- ---------- grants (everything revoked first, then granted narrowly) ----------
revoke all on function public.submit_interest_request(int, text, text[], text[], text, text, text, text, text, boolean, text, text) from public, anon, authenticated;
revoke all on function public.admin_interest_tally()                     from public, anon, authenticated;
revoke all on function public.admin_list_interest_requests()             from public, anon, authenticated;
revoke all on function public.admin_set_interest_status(uuid, text)      from public, anon, authenticated;
revoke all on function public.admin_delete_interest_request(uuid)        from public, anon, authenticated;
revoke all on function public.admin_purge_expired_interest_requests()    from public, anon, authenticated;

grant execute on function public.submit_interest_request(int, text, text[], text[], text, text, text, text, text, boolean, text, text) to anon, authenticated;
grant execute on function public.admin_interest_tally()                  to authenticated;   -- is_admin() checked inside
grant execute on function public.admin_list_interest_requests()          to authenticated;
grant execute on function public.admin_set_interest_status(uuid, text)   to authenticated;
grant execute on function public.admin_delete_interest_request(uuid)     to authenticated;
grant execute on function public.admin_purge_expired_interest_requests() to authenticated;

-- Quick tally for the SQL editor (no admin login needed there):
--   select level, s as slot, count(*) from public.interest_requests, unnest(slots) s group by 1, 2 order by 1, 3 desc;
