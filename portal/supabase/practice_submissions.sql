-- Math Inquirers: online practice submissions (child profile -> auto-marked answers -> tutor and parent reports).
-- DRAFT. NOT APPLIED to any database by the author. Review first (owner + lawyer: see docs/online_submission_design.md), then try on a scratch
-- Supabase project, never first on the live one. Run AFTER schema.sql and policies.sql. Safe to re-run (idempotent).
-- If you ever re-run policies.sql (it revokes every function grant), re-run this file after it.
--
-- Design in one paragraph
--   * Identity: the EXISTING child profile (public.children: display name + PIN, no child email) under the EXISTING parent account. The child signs in
--     with family code + name + PIN exactly as now (child_sign_in); child_start_session() wraps that check and mints a short-lived random token (stored
--     only as a SHA-256 hash). The token is a bearer for ONE child, 4 hours. No new password, no child email, no new account system.
--   * Consent: a NEW consent type 'online_practice' (the existing 'childs_work' text mentions practice answers but not sending marked answers to tutors
--     and reports). Sessions and submissions need it to be CURRENTLY granted; withdrawing it (a new consents row) stops new submissions at once.
--   * Writes: ONLY through service_practice_record(), executable by service_role alone (the Cloudflare Worker, which re-marks every answer from the
--     answer key before calling it). Parents, tutors, anon and the child token can not insert, update or delete anything directly.
--   * Answer key: public.practice_item_keys. RLS on, no policy, no grant to anon or authenticated. Only service_role (bypasses RLS) and the definer
--     functions below can read it. Reports never return it.
--   * Reads (RLS): parent -> own children's rows; tutor -> children with a confirmed enrolment in a group the tutor is assigned to; admin -> all.
--   * Reuse: public.practice_attempts (the placeholder table already in schema.sql) becomes the per-question row; children, parents, enrolments,
--     groups, consents, admins, delete_my_data()'s cascade (children ON DELETE CASCADE) are unchanged.

create extension if not exists pgcrypto with schema extensions;

-- ---------- 1. new consent type ----------
alter table public.consents drop constraint if exists consents_consent_type_check;
alter table public.consents add constraint consents_consent_type_check
  check (consent_type in ('contact','terms','recording','childs_work','feedback_quotes','online_practice'));

create or replace function public.record_consents(p_items jsonb, p_terms text, p_privacy text) returns void
language plpgsql security definer set search_path = public as $$
declare uid uuid := public._require_parent(); k text; v jsonb;
begin
  if jsonb_typeof(p_items) <> 'object' then raise exception 'bad_items'; end if;
  for k, v in select * from jsonb_each(p_items) loop
    if k not in ('contact','terms','recording','childs_work','feedback_quotes','online_practice') then raise exception 'bad_consent_type'; end if;
    if jsonb_typeof(v) <> 'boolean' then raise exception 'bad_consent_value'; end if;
    insert into public.consents (parent_id, consent_type, granted, terms_version, privacy_version)
    values (uid, k, (v)::text::boolean, p_terms, p_privacy);
  end loop;
end $$;

create or replace function public._has_consent(p_parent uuid, p_type text) returns boolean
language sql stable security definer set search_path = public as $$
  select coalesce((select c.granted from public.consents c where c.parent_id = p_parent and c.consent_type = p_type order by c.seq desc limit 1), false);
$$;

-- ---------- 2. child sessions (short-lived, hashed) ----------
create table if not exists public.child_sessions (
  id         uuid primary key default gen_random_uuid(),
  child_id   uuid not null references public.children(id) on delete cascade,
  token_hash text not null unique,
  created_at timestamptz not null default now(),
  expires_at timestamptz not null,
  revoked_at timestamptz
);
create index if not exists child_sessions_child_idx on public.child_sessions (child_id, expires_at desc);

-- Same check as child_sign_in (lockout after 5 wrong PINs, same silent failure), plus: the parent must have granted 'online_practice'.
-- Returns one row on success and nothing on any failure, so the caller cannot tell which part was wrong.
create or replace function public.child_start_session(p_family_code text, p_name text, p_pin text)
returns table (token text, child_id uuid, display_name text, level smallint, expires_at timestamptz)
language plpgsql security definer set search_path = public, extensions as $$
declare c record; pid uuid; tok text;
begin
  select * into c from public.child_sign_in(p_family_code, p_name, p_pin);
  if not found then return; end if;
  select ch.parent_id into pid from public.children ch where ch.id = c.child_id;
  if not public._has_consent(pid, 'online_practice') then return; end if;
  update public.child_sessions set revoked_at = now()
   where child_sessions.child_id = c.child_id and revoked_at is null
     and id not in (select id from public.child_sessions s where s.child_id = c.child_id and s.revoked_at is null order by s.created_at desc limit 4);   -- at most 5 live sessions per child
  tok := translate(encode(extensions.gen_random_bytes(32), 'base64'), '+/=', '-_');
  insert into public.child_sessions (child_id, token_hash, expires_at)
  values (c.child_id, encode(extensions.digest(tok, 'sha256'), 'hex'), now() + interval '4 hours');
  return query select tok, c.child_id, c.display_name, c.level, now() + interval '4 hours';
end $$;

create or replace function public.child_end_session(p_token text) returns void
language sql security definer set search_path = public, extensions as $$
  update public.child_sessions set revoked_at = now() where token_hash = encode(extensions.digest(p_token, 'sha256'), 'hex') and revoked_at is null;
$$;

-- ---------- 3. units, item tags (not secret) and answer keys (secret) ----------
create table if not exists public.practice_units (
  unit_key     text not null check (unit_key ~ '^[a-z0-9][a-z0-9-]{2,39}$'),
  unit_version text not null check (unit_version ~ '^[A-Za-z0-9._-]{1,30}$'),
  product      text not null check (product in ('holiday','term','extension')),
  level        smallint not null check (level between 1 and 6),
  title        text not null,
  content_hash text,                 -- hash of the built data file the keys were made from
  published    boolean not null default false,
  created_at   timestamptz not null default now(),
  primary key (unit_key, unit_version)
);

create table if not exists public.practice_item_tags (       -- what a report may show: tags and the listed wrong answers, never the right answer
  unit_key text not null, unit_version text not null, item_id text not null check (item_id ~ '^[A-Za-z0-9_.-]{1,40}$'),
  position     int  not null,
  tier         text,
  marking_mode text not null check (marking_mode in ('auto','self','none')),   -- auto: marked by code | self: child compares with the solution (incl. paper-only) | none: open, never marked
  paper_only   boolean not null default false,
  strand       text,                 -- MOE strand label (tutor-facing only), e.g. 'Whole Numbers'
  skill        text,                 -- short skill tag, e.g. 'Place value to 1000'
  topic        text,
  slips        jsonb not null default '[]',   -- [{"a":[7],"say":"7 is 3 + 4 ..."}]: listed wrong answers and the likely misconception, kindly worded
  primary key (unit_key, unit_version, item_id),
  foreign key (unit_key, unit_version) references public.practice_units on delete cascade
);

create table if not exists public.practice_item_keys (       -- SECRET: no policy, no grant
  unit_key text not null, unit_version text not null, item_id text not null,
  answer_type  text not null check (answer_type in ('number','fields','set','choice','fraction','decimal','text','selfcheck','open')),
  answer_key   jsonb,
  ordered      boolean not null default false,
  equivalent   boolean not null default false,
  primary key (unit_key, unit_version, item_id),
  foreign key (unit_key, unit_version, item_id) references public.practice_item_tags on delete cascade
);

-- ---------- 4. submissions (one per child, unit and attempt; the latest revision wins) and the per-question rows ----------
create table if not exists public.practice_submissions (
  id                uuid primary key default gen_random_uuid(),
  child_id          uuid not null references public.children(id) on delete cascade,
  unit_key          text not null, unit_version text not null,
  client_sid        uuid not null,                       -- made by the browser once per attempt; makes a retry idempotent
  rev               smallint not null default 1 check (rev between 1 and 50),
  first_received_at timestamptz not null default now(),
  received_at       timestamptz not null default now(),   -- server time of the latest revision. No client clock and no per-question timers are stored.
  n_auto smallint not null default 0, n_right smallint not null default 0, n_wrong smallint not null default 0, n_skipped smallint not null default 0,
  n_self smallint not null default 0, n_self_got smallint not null default 0, n_open smallint not null default 0,
  unique (child_id, client_sid),
  foreign key (unit_key, unit_version) references public.practice_units
);
create index if not exists practice_submissions_child_idx on public.practice_submissions (child_id, unit_key, received_at desc);
create index if not exists practice_submissions_received_idx on public.practice_submissions (received_at);

-- practice_attempts already exists (schema.sql): child_id, lesson_key, item_key, correct, hints_used, created_at. Extend it; do not add a second table.
alter table public.practice_attempts
  add column if not exists submission_id  uuid references public.practice_submissions(id) on delete cascade,
  add column if not exists unit_version   text,
  add column if not exists marking_mode   text check (marking_mode in ('auto','self','none')),
  add column if not exists mark           text check (mark in ('right','wrong','skipped','self','open')),
  add column if not exists answered       boolean,
  add column if not exists answer_text    text check (answer_text is null or char_length(answer_text) <= 200),   -- auto items only; never free text
  add column if not exists partial_found  smallint,
  add column if not exists partial_of     smallint,
  add column if not exists slip_idx       smallint,
  add column if not exists self_result    text check (self_result in ('got','not_yet','checked')),
  add column if not exists note           text;
create unique index if not exists practice_attempts_sub_item_uq on public.practice_attempts (submission_id, item_key) where submission_id is not null;

-- ---------- 5. tutors (assigned to groups; same Supabase Auth login as the admin page) ----------
create table if not exists public.tutors (
  user_id uuid primary key, note text, created_at timestamptz not null default now()
);
create table if not exists public.tutor_groups (
  user_id  uuid not null references public.tutors(user_id) on delete cascade,
  group_id text not null references public.groups(id) on delete cascade,
  primary key (user_id, group_id)
);

create or replace function public.is_tutor_of_child(p_child uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.tutor_groups tg join public.enrolments e on e.group_id = tg.group_id
                  where tg.user_id = auth.uid() and e.child_id = p_child and e.status = 'confirmed');
$$;
create or replace function public.is_tutor_of_group(p_group text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.tutor_groups tg where tg.user_id = auth.uid() and tg.group_id = p_group);
$$;

-- ---------- 6. grants and row level security ----------
alter table public.child_sessions       enable row level security;
alter table public.practice_units       enable row level security;
alter table public.practice_item_tags   enable row level security;
alter table public.practice_item_keys   enable row level security;
alter table public.practice_submissions enable row level security;
alter table public.tutors               enable row level security;
alter table public.tutor_groups         enable row level security;

revoke all on public.child_sessions, public.practice_units, public.practice_item_tags, public.practice_item_keys,
              public.practice_submissions, public.tutors, public.tutor_groups from anon, authenticated;
revoke insert, update, delete on public.practice_attempts from anon, authenticated;

grant select on public.practice_submissions to authenticated;                         -- RLS filters rows
grant select on public.tutor_groups to authenticated;
-- practice_attempts: select already granted in policies.sql; add the tutor policy next to the existing parent/admin one.

drop policy if exists practice_submissions_select on public.practice_submissions;
create policy practice_submissions_select on public.practice_submissions for select to authenticated using (
  public.is_admin() or public.is_tutor_of_child(child_id)
  or exists (select 1 from public.children c where c.id = practice_submissions.child_id and c.parent_id = auth.uid()));

drop policy if exists attempts_tutor_select on public.practice_attempts;
create policy attempts_tutor_select on public.practice_attempts for select to authenticated using (public.is_tutor_of_child(child_id));

drop policy if exists tutor_groups_own on public.tutor_groups;
create policy tutor_groups_own on public.tutor_groups for select to authenticated using (user_id = auth.uid() or public.is_admin());

-- ---------- 7. service functions (service_role only) ----------
create or replace function public._child_for_token(p_hash text) returns uuid
language sql stable security definer set search_path = public as $$
  select s.child_id from public.child_sessions s join public.children c on c.id = s.child_id join public.parents p on p.id = c.parent_id
   where s.token_hash = p_hash and s.revoked_at is null and s.expires_at > now() and p.deleted_at is null;
$$;

-- Step 1 for the Worker: who is this, may they submit, and the keys to mark with. Rate limits: 20 submissions per child per hour, 3000 per hour in all.
create or replace function public.service_practice_keys(p_token_hash text, p_unit text, p_version text) returns jsonb
language plpgsql security definer set search_path = public as $$
declare cid uuid := public._child_for_token(p_token_hash); pid uuid; keys jsonb;
begin
  if cid is null then return jsonb_build_object('ok', false, 'error', 'session'); end if;
  select parent_id into pid from public.children where id = cid;
  if not public._has_consent(pid, 'online_practice') then return jsonb_build_object('ok', false, 'error', 'consent'); end if;
  if not exists (select 1 from public.practice_units where unit_key = p_unit and unit_version = p_version and published) then
    return jsonb_build_object('ok', false, 'error', 'unit'); end if;
  if (select count(*) from public.practice_submissions where child_id = cid and received_at > now() - interval '1 hour') >= 20
     or (select count(*) from public.practice_submissions where received_at > now() - interval '1 hour') >= 3000 then
    return jsonb_build_object('ok', false, 'error', 'rate'); end if;
  select jsonb_agg(jsonb_build_object('id', t.item_id, 'marking_mode', t.marking_mode, 'paper_only', t.paper_only, 'type', k.answer_type,
           'key', k.answer_key, 'ordered', k.ordered, 'equivalent', k.equivalent, 'slips', t.slips) order by t.position)
    into keys from public.practice_item_tags t join public.practice_item_keys k using (unit_key, unit_version, item_id)
   where t.unit_key = p_unit and t.unit_version = p_version;
  return jsonb_build_object('ok', true, 'keys', coalesce(keys, '[]'::jsonb));
end $$;

-- Step 2: store the already re-marked rows. Idempotent on (child, client_sid): same rev = duplicate, lower rev = stale, higher rev replaces.
-- Counts are recomputed here from the rows; nothing the browser or the Worker computed is trusted for them.
create or replace function public.service_practice_record(p_token_hash text, p_unit text, p_version text, p_sid uuid, p_rev int, p_rows jsonb) returns jsonb
language plpgsql security definer set search_path = public as $$
declare cid uuid := public._child_for_token(p_token_hash); pid uuid; sub public.practice_submissions; r jsonb; n_bad int;
begin
  if cid is null then return jsonb_build_object('ok', false, 'error', 'session'); end if;
  select parent_id into pid from public.children where id = cid;
  if not public._has_consent(pid, 'online_practice') then return jsonb_build_object('ok', false, 'error', 'consent'); end if;
  if jsonb_typeof(p_rows) <> 'array' or jsonb_array_length(p_rows) > 400 or p_rev < 1 or p_rev > 50 then return jsonb_build_object('ok', false, 'error', 'bad_rows'); end if;
  select count(*) into n_bad from jsonb_array_elements(p_rows) x
   where not exists (select 1 from public.practice_item_tags t where t.unit_key = p_unit and t.unit_version = p_version and t.item_id = x->>'item_id'
                       and t.marking_mode = x->>'marking_mode')
      or (x->>'mark') not in ('right','wrong','skipped','self','open')
      or ((x->>'marking_mode') = 'auto' and (x->>'mark') in ('self','open'))
      or ((x->>'marking_mode') <> 'auto' and (x->>'mark') in ('right','wrong','skipped'));
  if n_bad > 0 then return jsonb_build_object('ok', false, 'error', 'bad_rows'); end if;
  select * into sub from public.practice_submissions where child_id = cid and client_sid = p_sid for update;
  if found then
    if p_rev = sub.rev then return jsonb_build_object('ok', true, 'duplicate', true, 'rev', sub.rev); end if;
    if p_rev < sub.rev then return jsonb_build_object('ok', true, 'stale', true, 'rev', sub.rev); end if;
    delete from public.practice_attempts where submission_id = sub.id;
  else
    insert into public.practice_submissions (child_id, unit_key, unit_version, client_sid, rev) values (cid, p_unit, p_version, p_sid, p_rev) returning * into sub;
  end if;
  for r in select * from jsonb_array_elements(p_rows) loop
    insert into public.practice_attempts (child_id, lesson_key, item_key, submission_id, unit_version, marking_mode, mark, correct, answered, answer_text,
                                          partial_found, partial_of, slip_idx, self_result, note)
    values (cid, p_unit, r->>'item_id', sub.id, p_version, r->>'marking_mode', r->>'mark',
            case r->>'mark' when 'right' then true when 'wrong' then false else null end,
            (r->>'answered')::boolean, left(r->>'answer_text', 200),
            nullif(r->>'partial_found','')::smallint, nullif(r->>'partial_of','')::smallint, nullif(r->>'slip_idx','')::smallint,
            nullif(r->>'self_result',''), left(r->>'note', 60));
  end loop;
  update public.practice_submissions s set rev = p_rev, received_at = now(),
    n_auto = (select count(*) from public.practice_attempts a where a.submission_id = s.id and a.marking_mode = 'auto'),
    n_right = (select count(*) from public.practice_attempts a where a.submission_id = s.id and a.mark = 'right'),
    n_wrong = (select count(*) from public.practice_attempts a where a.submission_id = s.id and a.mark = 'wrong'),
    n_skipped = (select count(*) from public.practice_attempts a where a.submission_id = s.id and a.mark = 'skipped'),
    n_self = (select count(*) from public.practice_attempts a where a.submission_id = s.id and a.mark = 'self'),
    n_self_got = (select count(*) from public.practice_attempts a where a.submission_id = s.id and a.self_result = 'got'),
    n_open = (select count(*) from public.practice_attempts a where a.submission_id = s.id and a.mark = 'open')
   where s.id = sub.id;
  return jsonb_build_object('ok', true, 'rev', p_rev);
end $$;

-- ---------- 8. report functions (RLS-equivalent checks inside; none returns an answer key) ----------
-- Group summary for a tutor (or the admin): one row per child and unit, latest revision. Children = confirmed enrolments in the group.
create or replace function public.tutor_group_practice(p_group text, p_unit text default null)
returns table (child_id uuid, display_name text, unit_key text, unit_version text, received_at timestamptz,
               n_auto smallint, n_right smallint, n_wrong smallint, n_skipped smallint, n_self smallint, n_self_got smallint, n_open smallint)
language plpgsql stable security definer set search_path = public as $$
begin
  if not (public.is_admin() or public.is_tutor_of_group(p_group)) then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
    select c.id, c.display_name, s.unit_key, s.unit_version, s.received_at, s.n_auto, s.n_right, s.n_wrong, s.n_skipped, s.n_self, s.n_self_got, s.n_open
      from public.enrolments e join public.children c on c.id = e.child_id
      join public.practice_submissions s on s.child_id = c.id
     where e.group_id = p_group and e.status = 'confirmed' and (p_unit is null or s.unit_key = p_unit)
     order by c.display_name, s.unit_key, s.received_at desc;
end $$;

-- Question-level report rows for ONE child (the parent, the child's tutor or the admin). Tags and the misconception text come from the tags table.
create or replace function public.practice_child_detail(p_child uuid, p_unit text)
returns table (item_id text, position int, tier text, strand text, skill text, topic text, marking_mode text, paper_only boolean, mark text,
               answer_text text, partial_found smallint, partial_of smallint, misconception text, self_result text, answered boolean, received_at timestamptz)
language plpgsql stable security definer set search_path = public as $$
begin
  if not (public.is_admin() or public.is_tutor_of_child(p_child)
          or exists (select 1 from public.children ch where ch.id = p_child and ch.parent_id = auth.uid())) then
    raise exception 'forbidden' using errcode = '42501'; end if;
  return query
    select a.item_key, t.position, t.tier, t.strand, t.skill, t.topic, a.marking_mode, t.paper_only, a.mark, a.answer_text, a.partial_found, a.partial_of,
           case when a.slip_idx is not null then t.slips -> a.slip_idx ->> 'say' end, a.self_result, a.answered, s.received_at
      from public.practice_submissions s join public.practice_attempts a on a.submission_id = s.id
      join public.practice_item_tags t on t.unit_key = s.unit_key and t.unit_version = s.unit_version and t.item_id = a.item_key
     where s.child_id = p_child and s.unit_key = p_unit
       and s.received_at = (select max(s2.received_at) from public.practice_submissions s2 where s2.child_id = p_child and s2.unit_key = p_unit)
     order by t.position;
end $$;

-- A parent can delete a child's practice answers without deleting the account (also what 'withdraw practice consent + delete' uses).
create or replace function public.delete_child_practice(p_child uuid) returns int
language plpgsql security definer set search_path = public as $$
declare uid uuid := public._require_parent(); n int;
begin
  if not exists (select 1 from public.children where id = p_child and parent_id = uid) then raise exception 'not_found'; end if;
  delete from public.practice_submissions where child_id = p_child;   -- practice_attempts rows go with them (ON DELETE CASCADE)
  get diagnostics n = row_count;
  delete from public.child_sessions where child_id = p_child;
  return n;
end $$;

-- Retention (suggested, for the owner and a lawyer to confirm): answers are deleted 12 months after the latest submission; the group-level
-- rule 'also 90 days after the program ends' is run by the owner per group with admin_purge_practice_for_group().
create or replace function public.admin_purge_expired_practice() returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  delete from public.practice_submissions where received_at < now() - interval '12 months';
  get diagnostics n = row_count;
  delete from public.child_sessions where expires_at < now() - interval '7 days';
  return n;
end $$;
create or replace function public.admin_purge_practice_for_group(p_group text, p_before timestamptz) returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  delete from public.practice_submissions s where s.received_at < p_before
    and s.child_id in (select e.child_id from public.enrolments e where e.group_id = p_group and e.child_id is not null);
  get diagnostics n = row_count;
  return n;
end $$;

-- ---------- 9. function grants (everything revoked first, then granted narrowly) ----------
revoke all on function public.child_start_session(text, text, text), public.child_end_session(text), public._has_consent(uuid, text),
  public.is_tutor_of_child(uuid), public.is_tutor_of_group(text), public._child_for_token(text),
  public.service_practice_keys(text, text, text), public.service_practice_record(text, text, text, uuid, int, jsonb),
  public.tutor_group_practice(text, text), public.practice_child_detail(uuid, text), public.delete_child_practice(uuid),
  public.admin_purge_expired_practice(), public.admin_purge_practice_for_group(text, timestamptz), public.record_consents(jsonb, text, text)
  from public, anon, authenticated;
grant execute on function public.record_consents(jsonb, text, text) to authenticated;
grant execute on function public.child_start_session(text, text, text) to anon, authenticated;
grant execute on function public.child_end_session(text) to anon, authenticated;
grant execute on function public.is_tutor_of_child(uuid), public.is_tutor_of_group(text) to authenticated;   -- used inside policies
grant execute on function public.tutor_group_practice(text, text), public.practice_child_detail(uuid, text), public.delete_child_practice(uuid),
  public.admin_purge_expired_practice(), public.admin_purge_practice_for_group(text, timestamptz) to authenticated;   -- each checks who the caller is inside
grant execute on function public.service_practice_keys(text, text, text), public.service_practice_record(text, text, text, uuid, int, jsonb) to service_role;
-- _has_consent(), _child_for_token() are internal: not granted to any API role.

-- Owner set-up by hand in the SQL editor (not a function: it is rare):
--   insert into public.tutors (user_id, note) select id, 'Tutor name' from auth.users where email = 'tutor@example.com';
--   insert into public.tutor_groups (user_id, group_id) select id, 'L1A' from auth.users where email = 'tutor@example.com';
