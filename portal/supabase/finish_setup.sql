-- NOTE (23 Oct 2026): this one-off snapshot still contains the retired HitPay service functions. After running it, run stripe_migration.sql.
-- finish_setup.sql: for the Supabase project already created by Claude (tables, gen_code, is_admin, _require_parent, add_child already exist).
-- Paste this whole file into the Supabase SQL Editor and click Run. It adds the remaining functions, row level security and the six beta groups.

-- ---- round-1 audit fixes (escalating PIN lockout, weak-PIN list, parent alert): columns and table first, then the functions ----
alter table public.children add column if not exists pin_lock_level smallint not null default 0;
create table if not exists public.pin_lock_events (
  id uuid primary key default gen_random_uuid(),
  child_id uuid not null references public.children(id) on delete cascade,
  locked_at timestamptz not null default now(), locked_until timestamptz not null, lock_level smallint not null, seen_at timestamptz);
create index if not exists pin_lock_events_child_idx on public.pin_lock_events (child_id, locked_at desc);
alter table public.pin_lock_events enable row level security;
revoke all on public.pin_lock_events from anon, authenticated;
-- PIN rules, checked when a PIN is SET (never on sign-in): 4 to 6 digits, and not one of the easy guesses an attacker (or a sibling) tries first:
-- all the same digit (0000, 1111), a run up or down (1234, 4321, 7890, 123456), a repeated pair or triple (1212, 123123), a few very common PINs (2580, 1004 ...)
-- and birth-year patterns (a 4-digit year 1940-2039, or year+month / month+year in 6 digits). The lockout in child_sign_in is the second line of defence.
create or replace function public._pin_check(p_pin text) returns void
language plpgsql immutable set search_path = public as $$
begin
  if p_pin is null or p_pin !~ '^[0-9]{4,6}$' then raise exception 'pin_format'; end if;
  if p_pin ~ '^(.)\1+$'
     or position(p_pin in '01234567890') > 0 or position(p_pin in '09876543210') > 0
     or p_pin ~ '^(..)\1+$' or p_pin ~ '^(...)\1$'
     or p_pin in ('2580','0852','1004','1010','1122','1313','2000','2001','6969','7410','8520','1230','3210','123321','112233','121314','654321')
     or p_pin ~ '^(19[4-9][0-9]|20[0-3][0-9])$'
     or p_pin ~ '^(19[4-9][0-9]|20[0-3][0-9])(0[1-9]|1[0-2])$' or p_pin ~ '^(0[1-9]|1[0-2])(19[4-9][0-9]|20[0-3][0-9])$'
  then raise exception 'pin_weak'; end if;
end $$;

create or replace function public.add_child(p_name text, p_level int, p_pin text) returns uuid
language plpgsql security definer set search_path = public, extensions as $$
declare uid uuid := public._require_parent(); cid uuid;
begin
  perform public._pin_check(p_pin);
  if (select count(*) from public.children where parent_id = uid) >= 6 then raise exception 'too_many_children'; end if;
  insert into public.children (parent_id, display_name, level, pin_hash)
  values (uid, btrim(p_name), p_level, crypt(p_pin, gen_salt('bf', 10)))
  returning id into cid;
  return cid;
end $$;

create or replace function public.update_child(p_child uuid, p_name text, p_level int, p_pin text default null) returns void
language plpgsql security definer set search_path = public, extensions as $$
declare uid uuid := public._require_parent(); c public.children;
begin
  select * into c from public.children where id = p_child and parent_id = uid for update;
  if not found then raise exception 'not_found'; end if;
  if p_level <> c.level and exists (select 1 from public.enrolments where child_id = p_child and status <> 'cancelled') then
    raise exception 'level_locked_by_enrolment';
  end if;
  if p_pin is not null and p_pin <> '' then
    perform public._pin_check(p_pin);
    update public.children set pin_hash = crypt(p_pin, gen_salt('bf', 10)), pin_failed = 0, pin_locked_until = null, pin_lock_level = 0 where id = p_child;
    update public.pin_lock_events set seen_at = coalesce(seen_at, now()) where child_id = p_child;   -- a new PIN answers the alert
  end if;
  update public.children set display_name = btrim(p_name), level = p_level, updated_at = now() where id = p_child;
end $$;

create or replace function public.delete_child(p_child uuid) returns void
language plpgsql security definer set search_path = public as $$
declare uid uuid := public._require_parent();
begin
  if not exists (select 1 from public.children where id = p_child and parent_id = uid) then raise exception 'not_found'; end if;
  if exists (select 1 from public.enrolments where child_id = p_child and status <> 'cancelled') then
    raise exception 'cancel_enrolment_first';
  end if;
  delete from public.children where id = p_child;   -- practice_attempts cascade; enrolments.child_id set null
end $$;

-- Child sign-in check (callable without a parent login). Returns a row on success, nothing on any failure
-- (unknown family/name, wrong PIN, locked): the caller cannot tell which. ESCALATING lockout: 5 wrong PINs lock the child for 15 minutes; each further
-- lock without a correct sign-in in between is longer (1 hour, 6 hours, then 24 hours), so guessing a PIN is limited to 20 tries a day at worst and a
-- guesser cannot keep a child out for ever without the parent being told: every lock writes a pin_lock_events row that the parent sees on the dashboard
-- (my_pin_alerts) and the parent can reset the PIN (update_child), which clears the lock. A correct sign-in clears the level; a level not
-- raised for 7 days falls back to the first step.
create or replace function public.child_sign_in(p_family_code text, p_name text, p_pin text)
returns table (child_id uuid, display_name text, level smallint)
language plpgsql security definer set search_path = public, extensions as $$
declare c public.children; lvl int; dur interval;
begin
  select ch.* into c from public.children ch join public.parents p on p.id = ch.parent_id
   where p.family_code = upper(btrim(p_family_code)) and p.deleted_at is null
     and lower(btrim(ch.display_name)) = lower(btrim(p_name)) for update of ch;
  if not found then
    perform crypt(coalesce(p_pin, ''), '$2a$10$abcdefghijklmnopqrstuuwQ6k3uJ4Z2n6mO7cT0xk4oJ0z9y3v6e'); -- even out timing
    return;
  end if;
  if c.pin_locked_until is not null and c.pin_locked_until > now() then return; end if;
  if p_pin is not null and c.pin_hash = crypt(p_pin, c.pin_hash) then
    update public.children set pin_failed = 0, pin_locked_until = null, pin_lock_level = 0 where id = c.id;
    return query select c.id, c.display_name, c.level;
  elsif c.pin_failed + 1 < 5 then
    update public.children set pin_failed = pin_failed + 1 where id = c.id;
    return;
  else
    lvl := case when c.pin_lock_level > 0 and c.pin_locked_until is not null and c.pin_locked_until < now() - interval '7 days' then 1
                else least(c.pin_lock_level + 1, 4) end;
    dur := case lvl when 1 then interval '15 minutes' when 2 then interval '1 hour' when 3 then interval '6 hours' else interval '24 hours' end;
    update public.children set pin_failed = 0, pin_lock_level = lvl, pin_locked_until = now() + dur where id = c.id;
    insert into public.pin_lock_events (child_id, locked_until, lock_level) values (c.id, now() + dur, lvl);
    return;
  end if;
end $$;

-- What the parent sees on the dashboard: locks of their children in the last 14 days that they have not yet dismissed.
create or replace function public.my_pin_alerts() returns table (child_id uuid, child_name text, locked_at timestamptz, locked_until timestamptz, lock_level smallint, still_locked boolean)
language sql stable security definer set search_path = public as $$
  select e.child_id, c.display_name, e.locked_at, e.locked_until, e.lock_level, e.locked_until > now()
    from public.pin_lock_events e join public.children c on c.id = e.child_id
   where c.parent_id = public._require_parent() and e.seen_at is null and e.locked_at > now() - interval '14 days'
   order by e.locked_at desc limit 20;
$$;
create or replace function public.dismiss_pin_alerts() returns void
language plpgsql security definer set search_path = public as $$
declare uid uuid := public._require_parent();
begin
  update public.pin_lock_events e set seen_at = now() from public.children c where c.id = e.child_id and c.parent_id = uid and e.seen_at is null;
end $$;

create or replace function public.group_fill() returns table (group_id text, seats int, taken int)
language sql stable security definer set search_path = public as $$
  select g.id, g.seats,
         (select count(*)::int from public.enrolments e where e.group_id = g.id and e.status <> 'cancelled')
    from public.groups g where g.active;
$$;

create or replace function public.record_consents(p_items jsonb, p_terms text, p_privacy text) returns void
language plpgsql security definer set search_path = public as $$
declare uid uuid := public._require_parent(); k text; v jsonb;
begin
  if jsonb_typeof(p_items) <> 'object' then raise exception 'bad_items'; end if;
  for k, v in select * from jsonb_each(p_items) loop
    if k not in ('contact','terms','recording','childs_work','feedback_quotes') then raise exception 'bad_consent_type'; end if;
    if jsonb_typeof(v) <> 'boolean' then raise exception 'bad_consent_value'; end if;
    insert into public.consents (parent_id, consent_type, granted, terms_version, privacy_version)
    values (uid, k, (v)::text::boolean, p_terms, p_privacy);
  end loop;
end $$;

create or replace function public.my_consents() returns table (consent_type text, granted boolean, terms_version text, privacy_version text, created_at timestamptz)
language sql stable security definer set search_path = public as $$
  select distinct on (c.consent_type) c.consent_type, c.granted, c.terms_version, c.privacy_version, c.created_at
    from public.consents c where c.parent_id = auth.uid() order by c.consent_type, c.seq desc;
$$;

create or replace function public.enrol_child(p_child uuid, p_group text) returns uuid
language plpgsql security definer set search_path = public, extensions as $$
declare uid uuid := public._require_parent(); ch public.children; g public.groups; eid uuid; ref text; tries int := 0; taken int; missing text;
begin
  select * into ch from public.children where id = p_child and parent_id = uid;
  if not found then raise exception 'not_found'; end if;
  select * into g from public.groups where id = p_group and active for update;   -- row lock serialises seat checks
  if not found then raise exception 'group_not_found'; end if;
  if g.level <> ch.level then raise exception 'level_mismatch'; end if;
  if exists (select 1 from public.enrolments where child_id = p_child and status <> 'cancelled') then raise exception 'already_enrolled'; end if;
  select string_agg(t, ',') into missing from unnest(array['contact','terms','recording','childs_work']) t
   where not coalesce((select c.granted from public.consents c where c.parent_id = uid and c.consent_type = t order by c.seq desc limit 1), false);
  if missing is not null then raise exception 'consents_missing:%', missing; end if;
  select count(*) into taken from public.enrolments where group_id = g.id and status <> 'cancelled';
  if taken >= g.seats then raise exception 'group_full'; end if;
  insert into public.enrolments (parent_id, child_id, child_label, group_id) values (uid, ch.id, ch.display_name, g.id) returning id into eid;
  loop
    ref := 'MI-' || public.gen_code(6);
    exit when not exists (select 1 from public.payments where reference = ref);
    tries := tries + 1; if tries > 20 then raise exception 'ref_alloc'; end if;
  end loop;
  insert into public.payments (enrolment_id, reference, amount_cents) values (eid, ref, g.fee_cents);
  return eid;
end $$;

create or replace function public.cancel_my_enrolment(p_enrolment uuid) returns void
language plpgsql security definer set search_path = public as $$
declare uid uuid := public._require_parent(); pay public.payments;
begin
  select p.* into pay from public.payments p join public.enrolments e on e.id = p.enrolment_id
    where e.id = p_enrolment and e.parent_id = uid and e.status = 'pending_payment';
  if not found or pay.status <> 'pending' then raise exception 'cannot_cancel_contact_us'; end if;
  update public.enrolments set status = 'cancelled', cancelled_at = now() where id = p_enrolment;
  update public.payments set status = 'cancelled', updated_at = now() where id = pay.id;
end $$;

create or replace function public.my_enrolments() returns table (
  enrolment_id uuid, child_id uuid, child_name text, group_id text, enrolment_status text,
  payment_id uuid, payment_method text, payment_status text, payment_reference text, amount_cents int, paid_at timestamptz, created_at timestamptz)
language sql stable security definer set search_path = public as $$
  select e.id, e.child_id, coalesce(c.display_name, e.child_label), e.group_id, e.status,
         p.id, p.method, p.status, p.reference, p.amount_cents, p.paid_at, e.created_at
    from public.enrolments e join public.payments p on p.enrolment_id = e.id left join public.children c on c.id = e.child_id
   where e.parent_id = auth.uid() order by e.created_at;
$$;

-- ---------- admin ----------
create or replace function public.admin_list_enrolments() returns table (
  enrolment_id uuid, created_at timestamptz, parent_email text, parent_name text, parent_phone text, child_name text, level smallint,
  group_id text, enrolment_status text, payment_id uuid, payment_method text, payment_status text, payment_reference text, amount_cents int, paid_at timestamptz)
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
  select e.id, e.created_at, pa.email, pa.full_name, pa.phone, coalesce(c.display_name, e.child_label), g.level, e.group_id, e.status,
         p.id, p.method, p.status, p.reference, p.amount_cents, p.paid_at
    from public.enrolments e join public.payments p on p.enrolment_id = e.id join public.parents pa on pa.id = e.parent_id
    join public.groups g on g.id = e.group_id left join public.children c on c.id = e.child_id
   order by e.created_at desc;
end $$;

create or replace function public.admin_mark_paid(p_payment uuid, p_note text default null) returns void
language plpgsql security definer set search_path = public as $$
declare pay public.payments;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  select * into pay from public.payments where id = p_payment for update;
  if not found then raise exception 'not_found'; end if;
  if pay.status = 'paid' then return; end if;                       -- idempotent
  if pay.status <> 'pending' then raise exception 'payment_not_pending'; end if;
  update public.payments set status = 'paid', paid_at = now(), marked_by = auth.uid(), note = left(p_note, 500), updated_at = now() where id = p_payment;
  update public.enrolments set status = 'confirmed' where id = pay.enrolment_id and status = 'pending_payment';
end $$;

create or replace function public.admin_cancel_enrolment(p_enrolment uuid, p_note text default null) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  update public.enrolments set status = 'cancelled', cancelled_at = now() where id = p_enrolment and status <> 'cancelled';
  -- a paid payment stays 'paid' (the money is still held); the note flags the refund. Set 'refunded' by hand once the PayNow refund is sent.
  update public.payments set status = case when status = 'paid' then 'paid' else 'cancelled' end,
         note = left(coalesce(p_note, '') || case when status = 'paid' then ' [cancelled: refund due]' else '' end, 500), updated_at = now()
   where enrolment_id = p_enrolment and status in ('pending','paid');
end $$;

-- ---------- service-role only (Cloudflare Functions) ----------
-- Look up a payable enrolment for a given parent (the function has verified the parent's JWT).
create or replace function public.service_begin_hitpay(p_enrolment uuid, p_parent uuid)
returns table (amount_cents int, reference text, payment_status text, enrolment_status text, parent_email text, parent_name text)
language sql stable security definer set search_path = public as $$
  select p.amount_cents, p.reference, p.status, e.status, pa.email, pa.full_name
    from public.enrolments e join public.payments p on p.enrolment_id = e.id join public.parents pa on pa.id = e.parent_id
   where e.id = p_enrolment and e.parent_id = p_parent;
$$;

create or replace function public.service_attach_hitpay(p_enrolment uuid, p_request_id text) returns void
language sql security definer set search_path = public as $$
  update public.payments set method = 'hitpay', hitpay_payment_request_id = p_request_id, updated_at = now()
   where enrolment_id = p_enrolment and status = 'pending';
$$;

-- Idempotent. Returns: paid | already_paid | paid_enrolment_cancelled | amount_mismatch | not_found
create or replace function public.service_mark_hitpay_paid(p_enrolment uuid, p_request_id text, p_payment_id text, p_amount_cents int)
returns text language plpgsql security definer set search_path = public as $$
declare pay public.payments; est text;
begin
  select p.* into pay from public.payments p where p.enrolment_id = p_enrolment for update;
  if not found then return 'not_found'; end if;
  if pay.status = 'paid' then return 'already_paid'; end if;
  if pay.amount_cents <> p_amount_cents then return 'amount_mismatch'; end if;
  update public.payments set status = 'paid', method = 'hitpay', paid_at = now(), hitpay_payment_request_id = coalesce(p_request_id, hitpay_payment_request_id),
         hitpay_payment_id = p_payment_id, updated_at = now() where id = pay.id;
  select status into est from public.enrolments where id = p_enrolment;
  if est = 'pending_payment' then
    update public.enrolments set status = 'confirmed' where id = p_enrolment;
    return 'paid';
  end if;
  return 'paid_enrolment_cancelled';   -- money arrived for a cancelled enrolment: owner must refund by hand
end $$;

-- ---------- PDPA: delete my data ----------
-- NOTE: practice_submissions.sql REPLACES this function with the full version (extension orders, trial requests, recording views, preview registrations).
-- Removes the children (and their practice data), cancels open enrolments, strips parent PII, deletes the login.
-- Payment and consent rows are kept (anonymised: they only point at the now-empty parents row) for the retention
-- period in privacy.html, then purged by the owner. Paid enrolments are cancelled but NOT refunded here: the owner refunds per the terms.
create or replace function public.delete_my_data() returns void
language plpgsql security definer set search_path = public as $$
declare uid uuid := public._require_parent();
begin
  update public.payments set status = case when status = 'paid' then 'paid' else 'cancelled' end,
         note = case when status = 'paid' then coalesce(note || ' | ', '') || 'account deleted by parent: refund due per terms' else note end, updated_at = now()
   where status in ('pending','paid') and enrolment_id in (select id from public.enrolments where parent_id = uid and status <> 'cancelled');
  update public.enrolments set status = 'cancelled', cancelled_at = now(), child_label = null where parent_id = uid;
  delete from public.children where parent_id = uid;
  update public.parents set email = null, full_name = null, phone = null, deleted_at = now() where id = uid;
  insert into public.deletion_requests (parent_id) values (uid);
  delete from auth.users where id = uid;
end $$;

-- ===== policies.sql =====
-- Math Inquirers portal: grants + row level security. Run AFTER schema.sql.
-- Supabase grants ALL on new public tables/functions to anon/authenticated by default, so everything is revoked first
-- and re-granted narrowly. Direct writes are NOT granted at all except parents.full_name/phone: every write goes
-- through a SECURITY DEFINER function in schema.sql (PIN hashing, capacity, consent and admin checks live there).

alter table public.parents           enable row level security;
alter table public.children          enable row level security;
alter table public.groups            enable row level security;
alter table public.enrolments        enable row level security;
alter table public.payments          enable row level security;
alter table public.consents          enable row level security;
alter table public.practice_attempts enable row level security;
alter table public.admins            enable row level security;   -- no policy, no grant: only is_admin() (definer) reads it
alter table public.deletion_requests enable row level security;   -- no policy, no grant

revoke all on all tables    in schema public from anon, authenticated;
revoke all on all sequences in schema public from anon, authenticated;
revoke all on all functions in schema public from public, anon, authenticated;

-- ---- table privileges (RLS then filters rows) ----
grant select on public.groups to anon, authenticated;
grant select (id, email, full_name, phone, family_code, created_at) on public.parents to authenticated;
grant update (full_name, phone) on public.parents to authenticated;
-- children: the PIN hash and lockout counters are never selectable by a client
grant select (id, parent_id, display_name, level, created_at, updated_at) on public.children to authenticated;
grant select on public.enrolments, public.payments, public.consents, public.practice_attempts to authenticated;

-- ---- policies ----
create policy groups_read on public.groups for select to anon, authenticated using (active);

create policy parents_own_select on public.parents for select to authenticated using (id = auth.uid() or public.is_admin());
create policy parents_own_update on public.parents for update to authenticated
  using (id = auth.uid() and deleted_at is null) with check (id = auth.uid() and deleted_at is null);

create policy children_own_select on public.children for select to authenticated using (parent_id = auth.uid() or public.is_admin());

create policy enrolments_own_select on public.enrolments for select to authenticated using (parent_id = auth.uid() or public.is_admin());

create policy payments_own_select on public.payments for select to authenticated using (
  public.is_admin() or exists (select 1 from public.enrolments e where e.id = payments.enrolment_id and e.parent_id = auth.uid()));

create policy consents_own_select on public.consents for select to authenticated using (parent_id = auth.uid() or public.is_admin());

create policy attempts_own_select on public.practice_attempts for select to authenticated using (
  public.is_admin() or exists (select 1 from public.children c where c.id = practice_attempts.child_id and c.parent_id = auth.uid()));

-- ---- function execute grants ----
grant execute on function public.is_admin()                                   to authenticated;   -- used inside policies
grant execute on function public.add_child(text, int, text)                   to authenticated;
grant execute on function public.update_child(uuid, text, int, text)          to authenticated;
grant execute on function public.delete_child(uuid)                           to authenticated;
grant execute on function public.record_consents(jsonb, text, text)           to authenticated;
grant execute on function public.my_consents()                                to authenticated;
grant execute on function public.enrol_child(uuid, text)                      to authenticated;
grant execute on function public.cancel_my_enrolment(uuid)                    to authenticated;
grant execute on function public.my_enrolments()                              to authenticated;
grant execute on function public.group_fill()                                 to authenticated;
grant execute on function public.delete_my_data()                             to authenticated;
grant execute on function public.admin_list_enrolments()                      to authenticated;   -- checks is_admin() inside
grant execute on function public.admin_mark_paid(uuid, text)                  to authenticated;
grant execute on function public.admin_cancel_enrolment(uuid, text)           to authenticated;
grant execute on function public.child_sign_in(text, text, text)              to anon, authenticated;
grant execute on function public.my_pin_alerts()                              to authenticated;
grant execute on function public.dismiss_pin_alerts()                         to authenticated;
grant execute on function public.service_begin_hitpay(uuid, uuid)             to service_role;
grant execute on function public.service_attach_hitpay(uuid, text)            to service_role;
grant execute on function public.service_mark_hitpay_paid(uuid, text, text, int) to service_role;
-- _require_parent(), gen_code(), forbid_mutation(), handle_new_user() are internal: not granted to any API role.
-- service_role bypasses RLS but its table privileges are untouched by the revokes above.

-- ===== seed_groups.sql =====
-- GENERATED by portal/tools/gen_groups_seed.py from website/data/beta_schedule.json. Do not edit by hand.
insert into public.groups (id, level, name, ages, seats, sessions, first_label, last_label, start_date, fee_cents) values
  ('L1A', 1, 'Level 1 · Group A', '6 to 8', 8, '[{"day": "Tue", "start": "09:00", "end": "10:30"}, {"day": "Fri", "start": "09:00", "end": "10:30"}]'::jsonb, 'Tue 24 Nov', 'Thu 24 Dec', '2026-11-24', 25000),
  ('L2A', 2, 'Level 2 · Group A', '7 to 9', 8, '[{"day": "Tue", "start": "10:45", "end": "12:15"}, {"day": "Fri", "start": "10:45", "end": "12:15"}]'::jsonb, 'Tue 24 Nov', 'Thu 24 Dec', '2026-11-24', 25000),
  ('L3A', 3, 'Level 3 · Group A', '8 to 10', 8, '[{"day": "Tue", "start": "13:15", "end": "14:45"}, {"day": "Fri", "start": "13:15", "end": "14:45"}]'::jsonb, 'Tue 24 Nov', 'Thu 24 Dec', '2026-11-24', 25000),
  ('L4A', 4, 'Level 4 · Group A', '9 to 11', 8, '[{"day": "Tue", "start": "15:00", "end": "16:30"}, {"day": "Fri", "start": "15:00", "end": "16:30"}]'::jsonb, 'Tue 24 Nov', 'Thu 24 Dec', '2026-11-24', 25000),
  ('L5A', 5, 'Level 5 · Group A', '10 to 12', 8, '[{"day": "Fri", "start": "16:45", "end": "18:15"}, {"day": "Sun", "start": "16:15", "end": "17:45"}]'::jsonb, 'Fri 27 Nov', 'Sun 27 Dec', '2026-11-27', 25000),
  ('L6A', 6, 'Level 6 · Group A', '11 to 13', 8, '[{"day": "Thu", "start": "18:15", "end": "19:45"}, {"day": "Sat", "start": "18:45", "end": "20:15"}]'::jsonb, 'Thu 26 Nov', 'Sat 26 Dec', '2026-11-26', 25000)
on conflict (id) do update set level = excluded.level, name = excluded.name, ages = excluded.ages, seats = excluded.seats,
  sessions = excluded.sessions, first_label = excluded.first_label, last_label = excluded.last_label,
  start_date = excluded.start_date, fee_cents = excluded.fee_cents;
