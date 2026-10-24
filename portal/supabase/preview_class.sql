-- Math Inquirers: FREE PREVIEW CLASS (weekly, open to everyone, one attendance per child per 6 months).
-- DRAFT. NOT APPLIED to any Supabase project. Run only after schema.sql and policies.sql (needs is_admin() and the pgcrypto extension).
-- Safe to re-run (idempotent). Design and honest limits: docs/preview_class_design.md. Lawyer question 13: docs/owner_kit/lawyer_email_draft.md.
-- Local test: bash portal/supabase/test/run_preview_test.sh   (throwaway local PostgreSQL 16 with the repo's Supabase stand-in; not run on real Supabase)
--
-- Design in five lines
--   * Registrants are anonymous parents on the public site. They have NO table privileges: the only ways in are the SECURITY DEFINER
--     functions register_preview() and cancel_preview(). Every error is a fixed word; no input value is ever echoed or logged.
--   * Two stores with two lifetimes. preview_registrations holds contact details (plain, needed to send the link and reminders) and is deleted 30 days
--     after the class (6 months if the parent ticked the optional marketing consent). preview_attended holds ONLY keyed hashes (HMAC-SHA256 with a secret
--     pepper that no API role can read) of the identifiers of children who actually attended, and is deleted 7 months after attendance
--     (6 months of exclusion + 1 month of grace for the weekly purge).
--   * "Attended" means the host admitted the child's join name (name + code from the registration) and the child stayed at least p_min_minutes.
--     A registration alone never counts. No-shows do not use up the free class; a third no-show in 6 months goes to a human.
--   * Eligibility is the same function for registration and for the admin "can this family come?" check. One generic answer for a block
--     ('not_available'), so a stranger cannot learn WHICH field matched. It is a policy aid, not proof (see design section 1: easy to get round).
--   * No marketing is sent from here. The optional marketing consent is stored with a version; sending is a separate manual step.

create extension if not exists pgcrypto with schema extensions;

-- ---------- pepper (secret key for the hashes). Nobody but the SECURITY DEFINER functions can read it. ----------
create table if not exists public.preview_config (key text primary key, value text not null);
revoke all on public.preview_config from anon, authenticated, public;
alter table public.preview_config enable row level security;   -- deliberately no policy
insert into public.preview_config (key, value) values ('pepper', encode(extensions.gen_random_bytes(32), 'hex')) on conflict (key) do nothing;
insert into public.preview_config (key, value) values ('exclusion_months', '6') on conflict (key) do nothing;
-- On real Supabase prefer Vault (supabase_vault) for the pepper; losing or rotating it only means "everyone is new again".

-- ---------- tables ----------
create table if not exists public.preview_sessions (
  id            uuid primary key default gen_random_uuid(),
  starts_at     timestamptz not null,
  band          text        not null check (band in ('A','B','C')),          -- A = Primary 1-2 (levels 1-2), B = Primary 3-4 (levels 3-4), C = Primary 5-6 (levels 5-6)
  capacity      int         not null default 40 check (capacity between 1 and 120),   -- confirmed registrations (more than the live cap: many do not show)
  live_cap      int         not null default 30 check (live_cap between 1 and 120),   -- people the tutor admits at once (children; one parent each is not counted)
  status        text        not null default 'open' check (status in ('open','closed','held','cancelled')),
  lesson_version text       not null default 'v1',                            -- which fixed deck (same content every week)
  warmup_ref    text,                                                          -- which daily teaser feeds this week's warm-up, e.g. 'L3 11-07'
  stats         jsonb,                                                         -- written when the session is closed: counts only
  created_at    timestamptz not null default now()
);
create index if not exists preview_sessions_start_idx on public.preview_sessions (starts_at);

create table if not exists public.preview_registrations (
  id             uuid primary key default gen_random_uuid(),
  session_id     uuid        not null references public.preview_sessions(id) on delete cascade,
  created_at     timestamptz not null default now(),
  status         text        not null default 'confirmed' check (status in ('confirmed','waitlisted','pending_review','cancelled','attended','no_show','declined')),
  review_reason  text        check (review_reason is null or review_reason in ('similar_child','repeat_no_show')),
  join_code      text        not null,
  parent_first_name text     not null check (char_length(btrim(parent_first_name)) between 1 and 40),
  email          text        not null check (char_length(email) <= 120 and email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  phone          text        check (phone is null or phone ~ '^[0-9]{8,15}$'),
  child_first_name text      not null check (char_length(btrim(child_first_name)) between 1 and 30),
  child_birth_year smallint  not null check (child_birth_year between 2008 and 2022),
  school_year    text        not null check (school_year in ('P1','P2','P3','P4','P5','P6')),
  email_h        text        not null,
  phone_h        text,
  child_h        text        not null,        -- first name + birth year
  name_h         text        not null,        -- first name only (for the "similar child" rule)
  parent_present boolean     not null check (parent_present),
  consent_contact   boolean  not null check (consent_contact),
  consent_terms     boolean  not null check (consent_terms),
  consent_exclusion boolean  not null check (consent_exclusion),
  consent_marketing boolean  not null default false,   -- optional, never pre-ticked
  consent_version   text     not null check (char_length(consent_version) between 1 and 40),
  consent_at        timestamptz not null default now(),
  attended_minutes  int,
  wants_trial       boolean  not null default false,
  followup_status   text     not null default 'none' check (followup_status in ('none','contacted','trial_booked','trial_attended','enrolled','declined')),
  reminded_24h      boolean  not null default false,
  reminded_1h       boolean  not null default false,
  expires_at        timestamptz not null            -- set by register_preview(): 30 days after the class, or 6 months if marketing consent
);
create unique index if not exists preview_reg_code_uq   on public.preview_registrations (session_id, join_code);
create unique index if not exists preview_reg_child_uq  on public.preview_registrations (session_id, email_h, child_h) where status <> 'cancelled';
create index if not exists preview_reg_email_h_idx      on public.preview_registrations (email_h, created_at);
create index if not exists preview_reg_phone_h_idx      on public.preview_registrations (phone_h) where phone_h is not null;
create index if not exists preview_reg_expires_idx      on public.preview_registrations (expires_at);

-- Hash-only attempt log for the rate limit (also counts blocked attempts, so nobody can probe "did this family attend?" by trying again and again). Kept 2 days.
create table if not exists public.preview_attempts (
  at      timestamptz not null default now(),
  email_h text not null
);
create index if not exists preview_attempts_idx on public.preview_attempts (email_h, at);
alter table public.preview_attempts enable row level security;
revoke all on public.preview_attempts from anon, authenticated, public;

create table if not exists public.preview_attended (
  id           uuid primary key default gen_random_uuid(),
  attended_at  timestamptz not null default now(),
  expires_at   timestamptz not null default (now() + interval '7 months'),
  email_h      text not null,
  phone_h      text,
  child_h      text not null,
  name_h       text not null,
  birth_year   smallint not null
);
create index if not exists preview_att_email_idx on public.preview_attended (email_h);
create index if not exists preview_att_phone_idx on public.preview_attended (phone_h) where phone_h is not null;
create index if not exists preview_att_child_idx on public.preview_attended (child_h);
create index if not exists preview_att_name_idx  on public.preview_attended (name_h);
create index if not exists preview_att_exp_idx   on public.preview_attended (expires_at);

alter table public.preview_sessions      enable row level security;   -- no policies: not readable through the API
alter table public.preview_registrations enable row level security;
alter table public.preview_attended      enable row level security;
revoke all on public.preview_sessions, public.preview_registrations, public.preview_attended from anon, authenticated, public;   -- (preview_attempts and preview_config are revoked where created)

-- ---------- normalisers and hashing (internal) ----------
create or replace function public._pv_norm_email(p text) returns text language sql immutable as $$
  -- lower-case; drop "+tag"; for gmail/googlemail also drop dots and map googlemail.com to gmail.com
  select case when d in ('gmail.com','googlemail.com') then replace(split_part(l, '+', 1), '.', '') || '@gmail.com'
              else split_part(l, '+', 1) || '@' || d end
  from (select split_part(lower(btrim(coalesce(p,''))), '@', 1) l, split_part(lower(btrim(coalesce(p,''))), '@', 2) d) x;
$$;
create or replace function public._pv_norm_phone(p text) returns text language sql immutable as $$
  select case when d ~ '^65[0-9]{8}$' then substr(d, 3) when d ~ '^[0-9]{8,15}$' then d else null end
  from (select regexp_replace(coalesce(p,''), '[^0-9]', '', 'g') d) x;
$$;
create or replace function public._pv_norm_name(p text) returns text language sql immutable as $$
  -- first word only, letters only, lower-case: "Mei Ling", "mei-ling!" and "MEI" all become "mei" (a nickname or a double name still matches)
  select regexp_replace(lower(split_part(btrim(regexp_replace(coalesce(p,''), '[^[:alpha:] ]', ' ', 'g')), ' ', 1)), '[^[:alpha:]]', '', 'g');
$$;
create or replace function public._pv_h(label text, val text) returns text
language sql stable security definer set search_path = public, extensions as $$
  select case when val is null or val = '' then null
         else encode(extensions.hmac(label || ':' || val, (select value from public.preview_config where key = 'pepper'), 'sha256'), 'hex') end;
$$;

-- ---------- eligibility (internal; also used by the admin check) ----------
-- Returns one of: 'ok' | 'blocked' | 'review_similar' | 'review_no_show'
-- blocked        : someone with the same child key (first name + birth year) AND the same parent email OR phone attended within the window.
-- review_similar : same first name, birth year within 1, and same email OR phone attended within the window (typo, age instead of year, ...). A person decides.
-- review_no_show : the same child key registered and never turned up twice or more in the window (a human checks that nothing is wrong).
-- ok             : everything else, including a sibling (same parent contact, different first name) and a stranger with the same name and year.
create or replace function public._pv_eligibility(p_email_h text, p_phone_h text, p_child_h text, p_name_h text, p_birth_year int) returns text
language plpgsql stable security definer set search_path = public as $$
declare win interval := ((select value from public.preview_config where key = 'exclusion_months') || ' months')::interval;
begin
  if exists (select 1 from public.preview_attended a
              where a.attended_at > now() - win and a.child_h = p_child_h
                and (a.email_h = p_email_h or (p_phone_h is not null and a.phone_h = p_phone_h))) then return 'blocked'; end if;
  if exists (select 1 from public.preview_attended a
              where a.attended_at > now() - win and a.name_h = p_name_h and abs(a.birth_year - p_birth_year) <= 1
                and (a.email_h = p_email_h or (p_phone_h is not null and a.phone_h = p_phone_h))) then return 'review_similar'; end if;
  if (select count(*) from public.preview_registrations r
       where r.status = 'no_show' and r.child_h = p_child_h and r.created_at > now() - win) >= 2 then return 'review_no_show'; end if;
  return 'ok';
end $$;

create or replace function public._pv_band_of(p_school_year text) returns text language sql immutable as $$
  select case p_school_year when 'P1' then 'A' when 'P2' then 'A' when 'P3' then 'B' when 'P4' then 'B' when 'P5' then 'C' when 'P6' then 'C' end;
$$;

-- ---------- parent-facing: register ----------
-- Returns {"ok":true,"status":S,"join_code":C?}  S in: registered | waitlisted | pending | not_available | wrong_band | already_registered | closed
-- Raises: invalid_input, consent_required, busy. Never echoes input.
create or replace function public.register_preview(
  p_session uuid, p_parent_first text, p_email text, p_phone text, p_child_first text, p_birth_year int, p_school_year text,
  p_parent_present boolean, p_consent_contact boolean, p_consent_terms boolean, p_consent_exclusion boolean, p_consent_marketing boolean,
  p_consent_version text, p_hp text default null
) returns jsonb
language plpgsql volatile security definer set search_path = public as $$
declare
  v_pname text := btrim(regexp_replace(coalesce(p_parent_first,''), '[[:cntrl:]]', ' ', 'g'));
  v_cname text := btrim(regexp_replace(coalesce(p_child_first,''),  '[[:cntrl:]]', ' ', 'g'));
  v_email text := lower(btrim(coalesce(p_email,'')));
  v_phone text := public._pv_norm_phone(p_phone);
  v_ver   text := btrim(coalesce(p_consent_version,''));
  s public.preview_sessions%rowtype;
  v_eh text; v_ph text; v_ch text; v_nh text; v_elig text; v_status text; v_reason text; v_code text; v_n int; v_try int := 0;
  v_alpha constant text := 'ACDEFGHJKLMNPQRTUVWXY34679';
begin
  if p_hp is not null and btrim(p_hp) <> '' then return jsonb_build_object('ok', true, 'status', 'registered'); end if;   -- honeypot: look successful, store nothing
  if p_consent_contact is distinct from true or p_consent_terms is distinct from true or p_consent_exclusion is distinct from true
     or p_parent_present is distinct from true then raise exception 'consent_required' using errcode = '22023'; end if;
  if char_length(v_pname) not between 1 and 40 or char_length(v_cname) not between 1 and 30 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if char_length(v_email) > 120 or v_email !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' then raise exception 'invalid_input' using errcode = '22023'; end if;
  if nullif(btrim(coalesce(p_phone,'')), '') is not null and v_phone is null then raise exception 'invalid_input' using errcode = '22023'; end if;
  if p_birth_year is null or p_birth_year not between 2008 and 2022 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if p_school_year is null or public._pv_band_of(p_school_year) is null then raise exception 'invalid_input' using errcode = '22023'; end if;
  if char_length(v_ver) not between 1 and 40 then raise exception 'invalid_input' using errcode = '22023'; end if;
  if public._pv_norm_name(v_cname) = '' then raise exception 'invalid_input' using errcode = '22023'; end if;

  select * into s from public.preview_sessions where id = p_session;
  if not found then raise exception 'invalid_input' using errcode = '22023'; end if;
  if s.status <> 'open' or s.starts_at < now() + interval '1 hour' then return jsonb_build_object('ok', true, 'status', 'closed'); end if;
  if public._pv_band_of(p_school_year) <> s.band then return jsonb_build_object('ok', true, 'status', 'wrong_band'); end if;

  -- abuse brakes: 300 registrations an hour site-wide; 8 attempts per parent email per day (blocked attempts count too)
  if (select count(*) from public.preview_registrations where created_at > now() - interval '1 hour') >= 300 then raise exception 'busy' using errcode = '53400'; end if;
  v_eh := public._pv_h('email', public._pv_norm_email(v_email));
  v_ph := public._pv_h('phone', v_phone);
  v_nh := public._pv_h('name', public._pv_norm_name(v_cname));
  v_ch := public._pv_h('child', public._pv_norm_name(v_cname) || ':' || p_birth_year::text);
  delete from public.preview_attempts where at < now() - interval '2 days';
  if (select count(*) from public.preview_attempts where email_h = v_eh and at > now() - interval '24 hours') >= 8 then raise exception 'busy' using errcode = '53400'; end if;
  insert into public.preview_attempts (email_h) values (v_eh);

  if exists (select 1 from public.preview_registrations where session_id = s.id and email_h = v_eh and child_h = v_ch and status <> 'cancelled') then
    return jsonb_build_object('ok', true, 'status', 'already_registered');
  end if;

  v_elig := public._pv_eligibility(v_eh, v_ph, v_ch, v_nh, p_birth_year);
  if v_elig = 'blocked' then return jsonb_build_object('ok', true, 'status', 'not_available'); end if;   -- same word whatever matched
  if v_elig = 'review_similar' then v_status := 'pending_review'; v_reason := 'similar_child';
  elsif v_elig = 'review_no_show' then v_status := 'pending_review'; v_reason := 'repeat_no_show';
  else
    select count(*) into v_n from public.preview_registrations where session_id = s.id and status in ('confirmed','pending_review');
    v_status := case when v_n >= s.capacity then 'waitlisted' else 'confirmed' end;
  end if;

  loop   -- short join code used as a name tag ("Mei 7K3Q"); unique per session
    v_code := (select string_agg(substr(v_alpha, 1 + floor(random() * length(v_alpha))::int, 1), '') from generate_series(1, 4));
    exit when not exists (select 1 from public.preview_registrations where session_id = s.id and join_code = v_code);
    v_try := v_try + 1; if v_try > 20 then raise exception 'busy' using errcode = '53400'; end if;
  end loop;

  insert into public.preview_registrations (session_id, status, review_reason, join_code, parent_first_name, email, phone, child_first_name, child_birth_year, school_year,
      email_h, phone_h, child_h, name_h, parent_present, consent_contact, consent_terms, consent_exclusion, consent_marketing, consent_version, expires_at)
  values (s.id, v_status, v_reason, v_code, v_pname, v_email, v_phone, v_cname, p_birth_year, p_school_year, v_eh, v_ph, v_ch, v_nh, true, true, true, true,
      coalesce(p_consent_marketing, false), v_ver,
      s.starts_at + case when coalesce(p_consent_marketing, false) then interval '6 months' else interval '30 days' end);
  return case v_status when 'confirmed'      then jsonb_build_object('ok', true, 'status', 'registered', 'join_code', v_code)
                       when 'waitlisted'     then jsonb_build_object('ok', true, 'status', 'waitlisted')
                       else                       jsonb_build_object('ok', true, 'status', 'pending') end;
end $$;

-- ---------- parent-facing: which sessions can I register for? (no counts; only open/full) ----------
create or replace function public.preview_open_sessions() returns table (id uuid, starts_at timestamptz, band text, is_full boolean)
language sql stable security definer set search_path = public as $$
  select s.id, s.starts_at, s.band,
         (select count(*) from public.preview_registrations r where r.session_id = s.id and r.status in ('confirmed','pending_review')) >= s.capacity
    from public.preview_sessions s where s.status = 'open' and s.starts_at > now() + interval '1 hour' and s.starts_at < now() + interval '45 days' order by s.starts_at;
$$;

-- A parent cancels with the join code AND the email used. Returns true if a registration was cancelled.
create or replace function public.cancel_preview(p_session uuid, p_join_code text, p_email text) returns boolean
language plpgsql volatile security definer set search_path = public as $$
declare n int;
begin
  update public.preview_registrations set status = 'cancelled'
   where session_id = p_session and join_code = upper(btrim(coalesce(p_join_code,''))) and email_h = public._pv_h('email', public._pv_norm_email(p_email))
     and status in ('confirmed','waitlisted','pending_review');
  get diagnostics n = row_count;
  return n > 0;
end $$;

-- ---------- admin ----------
create or replace function public._pv_admin() returns void language plpgsql stable security definer set search_path = public as $$
begin if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if; end $$;

create or replace function public.admin_preview_create_session(p_starts_at timestamptz, p_band text, p_capacity int default 40, p_live_cap int default 30,
  p_lesson_version text default 'v1', p_warmup_ref text default null) returns uuid
language plpgsql security definer set search_path = public as $$
declare i uuid;
begin
  perform public._pv_admin();
  insert into public.preview_sessions (starts_at, band, capacity, live_cap, lesson_version, warmup_ref) values (p_starts_at, p_band, p_capacity, p_live_cap, p_lesson_version, p_warmup_ref) returning id into i;
  return i;
end $$;

-- The check-in sheet and reminder list (contact details: admin only).
create or replace function public.admin_preview_list(p_session uuid) returns table (
  id uuid, status text, review_reason text, join_code text, parent_first_name text, email text, phone text, child_first_name text, child_birth_year smallint,
  school_year text, consent_marketing boolean, wants_trial boolean, followup_status text, reminded_24h boolean, reminded_1h boolean)
language plpgsql stable security definer set search_path = public as $$
begin
  perform public._pv_admin();
  return query select r.id, r.status, r.review_reason, r.join_code, r.parent_first_name, r.email, r.phone, r.child_first_name, r.child_birth_year, r.school_year,
                      r.consent_marketing, r.wants_trial, r.followup_status, r.reminded_24h, r.reminded_1h
                 from public.preview_registrations r where r.session_id = p_session order by r.created_at;
end $$;

-- A person decides a pending_review registration: 'confirm' or 'decline'.
create or replace function public.admin_preview_decide(p_id uuid, p_decision text) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public._pv_admin();
  if p_decision not in ('confirm','decline') then raise exception 'invalid_input' using errcode = '22023'; end if;
  update public.preview_registrations set status = case p_decision when 'confirm' then 'confirmed' else 'declined' end where id = p_id and status = 'pending_review';
end $$;

create or replace function public.admin_preview_promote_waitlist(p_session uuid, p_n int) returns int
language plpgsql security definer set search_path = public as $$
declare k int;
begin
  perform public._pv_admin();
  with c as (select id from public.preview_registrations where session_id = p_session and status = 'waitlisted' order by created_at limit greatest(p_n, 0))
  update public.preview_registrations r set status = 'confirmed' from c where r.id = c.id;
  get diagnostics k = row_count;
  return k;
end $$;

-- AFTER the class: the host/tutor passes the join codes of everyone who was admitted and stayed (from the check-in sheet, or the codes read
-- off a Meet attendance report if the edition provides one). Codes are minutes-paired: p_minutes[i] is how long code p_codes[i] was present.
-- Only a registration that is confirmed and present for at least p_min_minutes becomes 'attended' and writes the hash-only exclusion row.
create or replace function public.admin_preview_mark_attendance(p_session uuid, p_codes text[], p_minutes int[], p_min_minutes int default 15) returns int
language plpgsql security definer set search_path = public as $$
declare i int; r public.preview_registrations%rowtype; n int := 0; c text;
begin
  perform public._pv_admin();
  if p_codes is null or p_minutes is null or cardinality(p_codes) <> cardinality(p_minutes) then raise exception 'invalid_input' using errcode = '22023'; end if;
  for i in 1 .. cardinality(p_codes) loop
    c := upper(btrim(p_codes[i]));
    select * into r from public.preview_registrations where session_id = p_session and join_code = c and status in ('confirmed','attended');
    if not found then continue; end if;
    update public.preview_registrations set attended_minutes = greatest(coalesce(attended_minutes, 0), p_minutes[i]) where id = r.id;
    if p_minutes[i] >= p_min_minutes and r.status = 'confirmed' then
      update public.preview_registrations set status = 'attended' where id = r.id;
      insert into public.preview_attended (email_h, phone_h, child_h, name_h, birth_year) values (r.email_h, r.phone_h, r.child_h, r.name_h, r.child_birth_year);
      n := n + 1;
    end if;
  end loop;
  return n;
end $$;

-- Close the session: confirmed people who never came are 'no_show' (they may try again), counts are stored, the session is 'held'.
create or replace function public.admin_preview_close_session(p_session uuid) returns jsonb
language plpgsql security definer set search_path = public as $$
declare st jsonb;
begin
  perform public._pv_admin();
  update public.preview_registrations set status = 'no_show' where session_id = p_session and status = 'confirmed';
  select jsonb_build_object('registered', count(*) filter (where status <> 'cancelled'), 'attended', count(*) filter (where status = 'attended'),
                            'no_show', count(*) filter (where status = 'no_show'), 'waitlisted', count(*) filter (where status = 'waitlisted'),
                            'declined', count(*) filter (where status = 'declined'), 'cancelled', count(*) filter (where status = 'cancelled'))
    into st from public.preview_registrations where session_id = p_session;
  update public.preview_sessions set status = 'held', stats = st where id = p_session;
  return st;
end $$;

-- The parent asked for a trial/next step (button on the thank-you page or a reply): counts for the funnel, nothing is sent from here.
create or replace function public.admin_preview_set_followup(p_id uuid, p_status text, p_wants boolean default null) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public._pv_admin();
  if p_status not in ('none','contacted','trial_booked','trial_attended','enrolled','declined') then raise exception 'invalid_input' using errcode = '22023'; end if;
  update public.preview_registrations set followup_status = p_status, wants_trial = coalesce(p_wants, wants_trial) where id = p_id;
end $$;

-- "Can this family come?" for the owner answering a parent by WhatsApp. Same rule as the form. Returns ok | blocked | review_similar | review_no_show.
create or replace function public.admin_preview_check(p_email text, p_phone text, p_child_first text, p_birth_year int) returns text
language plpgsql stable security definer set search_path = public as $$
begin
  perform public._pv_admin();
  return public._pv_eligibility(public._pv_h('email', public._pv_norm_email(p_email)), public._pv_h('phone', public._pv_norm_phone(p_phone)),
    public._pv_h('child', public._pv_norm_name(p_child_first) || ':' || p_birth_year::text), public._pv_h('name', public._pv_norm_name(p_child_first)), p_birth_year);
end $$;

-- 6-month enforcement report (hash-only, no names): how many exclusion rows are live, and how many registrations were turned away in the last 30 days is NOT kept (nothing stored on a block).
create or replace function public.admin_preview_exclusion_count() returns bigint
language plpgsql stable security definer set search_path = public as $$
begin perform public._pv_admin(); return (select count(*) from public.preview_attended where attended_at > now() - interval '6 months'); end $$;

-- Funnel counts (no tracking, only rows that exist). One row per band: sessions held, registered, attended, asked for a trial, trial attended, enrolled.
-- Counts of people are taken from registrations still stored (30 days / 6 months); older sessions are covered by preview_sessions.stats.
create or replace function public.admin_preview_funnel() returns table (band text, sessions_held bigint, registered bigint, attended bigint, wants_trial bigint, trial_attended bigint, enrolled bigint)
language plpgsql stable security definer set search_path = public as $$
begin
  perform public._pv_admin();
  return query
  select s.band, count(distinct s.id) filter (where s.status = 'held'),
         count(r.id) filter (where r.status not in ('cancelled','declined')), count(r.id) filter (where r.status = 'attended'),
         count(r.id) filter (where r.wants_trial), count(r.id) filter (where r.followup_status in ('trial_attended','enrolled')), count(r.id) filter (where r.followup_status = 'enrolled')
    from public.preview_sessions s left join public.preview_registrations r on r.session_id = s.id group by s.band order by s.band;
end $$;

-- PDPA deletion on request: removes the family's registrations AND their exclusion rows (so they may attend again; that is the cost of deleting).
create or replace function public.admin_preview_delete_person(p_email text) returns int
language plpgsql security definer set search_path = public as $$
declare h text := public._pv_h('email', public._pv_norm_email(p_email)); n int; m int;
begin
  perform public._pv_admin();
  delete from public.preview_registrations where email_h = h; get diagnostics n = row_count;
  delete from public.preview_attended where email_h = h;       get diagnostics m = row_count;
  return n + m;
end $$;

-- Retention: contact details 30 days after the class (6 months with marketing consent); exclusion hashes 7 months after attendance.
-- Schedule with pg_cron, for example:  select cron.schedule('purge-preview', '30 3 * * *', $$select public.admin_purge_preview_internal()$$);
create or replace function public.admin_purge_preview_internal() returns int
language plpgsql security definer set search_path = public as $$
declare a int; b int;
begin
  delete from public.preview_registrations where expires_at < now(); get diagnostics a = row_count;
  delete from public.preview_attended where expires_at < now();      get diagnostics b = row_count;
  return a + b;
end $$;
create or replace function public.admin_purge_preview() returns int
language plpgsql security definer set search_path = public as $$
begin perform public._pv_admin(); return public.admin_purge_preview_internal(); end $$;

-- ---------- grants ----------
revoke all on function public._pv_norm_email(text), public._pv_norm_phone(text), public._pv_norm_name(text), public._pv_h(text, text),
  public._pv_eligibility(text, text, text, text, int), public._pv_band_of(text), public._pv_admin(), public.admin_purge_preview_internal() from public, anon, authenticated;
revoke all on function public.register_preview(uuid, text, text, text, text, int, text, boolean, boolean, boolean, boolean, boolean, text, text) from public, anon, authenticated;
revoke all on function public.cancel_preview(uuid, text, text), public.preview_open_sessions() from public, anon, authenticated;
revoke all on function public.admin_preview_create_session(timestamptz, text, int, int, text, text), public.admin_preview_list(uuid), public.admin_preview_decide(uuid, text),
  public.admin_preview_promote_waitlist(uuid, int), public.admin_preview_mark_attendance(uuid, text[], int[], int), public.admin_preview_close_session(uuid),
  public.admin_preview_set_followup(uuid, text, boolean), public.admin_preview_check(text, text, text, int), public.admin_preview_exclusion_count(),
  public.admin_preview_funnel(), public.admin_preview_delete_person(text), public.admin_purge_preview() from public, anon, authenticated;

grant execute on function public.register_preview(uuid, text, text, text, text, int, text, boolean, boolean, boolean, boolean, boolean, text, text) to anon, authenticated;
grant execute on function public.cancel_preview(uuid, text, text), public.preview_open_sessions() to anon, authenticated;
grant execute on function public.admin_preview_create_session(timestamptz, text, int, int, text, text), public.admin_preview_list(uuid), public.admin_preview_decide(uuid, text),
  public.admin_preview_promote_waitlist(uuid, int), public.admin_preview_mark_attendance(uuid, text[], int[], int), public.admin_preview_close_session(uuid),
  public.admin_preview_set_followup(uuid, text, boolean), public.admin_preview_check(text, text, text, int), public.admin_preview_exclusion_count(),
  public.admin_preview_funnel(), public.admin_preview_delete_person(text), public.admin_purge_preview() to authenticated;   -- is_admin() checked inside
-- Internal helpers are executed by SECURITY DEFINER callers running as the function owner, so they need no grant.
