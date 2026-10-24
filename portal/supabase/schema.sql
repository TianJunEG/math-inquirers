-- Math Inquirers portal: schema (Supabase Postgres). Run FIRST in the Supabase SQL editor, then policies.sql, then seed_groups.sql.
-- Money is stored in cents (SGD). No plaintext PIN is ever stored: PINs are hashed server-side with bcrypt (pgcrypto crypt()).

create extension if not exists pgcrypto with schema extensions;

-- ---------- helpers ----------
create or replace function public.gen_code(n int) returns text
language plpgsql volatile set search_path = public, extensions as $$
declare alphabet constant text := 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; -- no 0/O/1/I/L
        out text := ''; i int;
begin
  for i in 1..n loop
    out := out || substr(alphabet, 1 + floor(random() * length(alphabet))::int, 1);
  end loop;
  return out;
end $$;

-- ---------- parents (one row per auth user; id = auth.users.id, deliberately NO foreign key so that
-- retained payment/consent records survive deletion of the login, see delete_my_data()) ----------
create table public.parents (
  id          uuid primary key,
  email       text,
  full_name   text check (full_name is null or char_length(full_name) <= 100),
  phone       text check (phone is null or char_length(phone) <= 30),
  family_code text not null unique,            -- the short code a child types with name + PIN
  created_at  timestamptz not null default now(),
  deleted_at  timestamptz
);

-- ---------- children (minimal: display name, level, PIN hash. No email, photo, school, birth date) ----------
create table public.children (
  id               uuid primary key default gen_random_uuid(),
  parent_id        uuid not null references public.parents(id) on delete cascade,
  display_name     text not null check (char_length(btrim(display_name)) between 1 and 30),
  level            smallint not null check (level between 1 and 6),
  pin_hash         text not null,
  pin_failed       smallint not null default 0,
  pin_locked_until timestamptz,
  pin_lock_level   smallint not null default 0,      -- escalating lockout: 0 none, 1 = 15 min, 2 = 1 hour, 3 = 6 hours, 4 = 24 hours (see child_sign_in)
  created_at       timestamptz not null default now(),
  updated_at       timestamptz not null default now()
);

-- One row each time a child's PIN is locked by wrong guesses, so the PARENT is told on the dashboard (my_pin_alerts). No PIN, no guess, no IP is stored.
create table public.pin_lock_events (
  id           uuid primary key default gen_random_uuid(),
  child_id     uuid not null references public.children(id) on delete cascade,
  locked_at    timestamptz not null default now(),
  locked_until timestamptz not null,
  lock_level   smallint not null,
  seen_at      timestamptz                              -- the parent pressed "Got it"
);
create index pin_lock_events_child_idx on public.pin_lock_events (child_id, locked_at desc);
create unique index children_parent_name_uq on public.children (parent_id, lower(btrim(display_name)));

-- ---------- groups (seeded from website/data/beta_schedule.json by portal/tools/gen_groups_seed.py) ----------
create table public.groups (
  id          text primary key,
  level       smallint not null check (level between 1 and 6),
  name        text not null,
  ages        text not null,
  seats       int  not null check (seats > 0),
  sessions    jsonb not null,           -- [{day,start,end}]
  first_label text,
  last_label  text,
  start_date  date,
  fee_cents   int  not null check (fee_cents > 0),
  active      boolean not null default true
);

-- ---------- enrolments ----------
create table public.enrolments (
  id           uuid primary key default gen_random_uuid(),
  parent_id    uuid not null references public.parents(id),
  child_id     uuid references public.children(id) on delete set null,
  child_label  text,                     -- display name snapshot, survives child deletion
  group_id     text not null references public.groups(id),
  status       text not null default 'pending_payment' check (status in ('pending_payment','confirmed','cancelled')),
  created_at   timestamptz not null default now(),
  cancelled_at timestamptz
);
create unique index enrolments_one_active_per_child on public.enrolments (child_id) where status <> 'cancelled' and child_id is not null;
create index enrolments_group_idx on public.enrolments (group_id) where status <> 'cancelled';
create index enrolments_parent_idx on public.enrolments (parent_id);

-- ---------- payments (one per enrolment in the beta) ----------
create table public.payments (
  id                        uuid primary key default gen_random_uuid(),
  enrolment_id              uuid not null unique references public.enrolments(id),
  method                    text not null default 'paynow_manual' check (method in ('paynow_manual','stripe','hitpay')),   -- provider; 'hitpay' kept for history only
  reference                 text not null unique,     -- PayNow reference code the parent types in the transfer
  status                    text not null default 'pending' check (status in ('pending','paid','failed','refunded','cancelled')),
  amount_cents              int  not null check (amount_cents > 0),
  currency                  text not null default 'SGD' check (currency = 'SGD'),
  paid_at                   timestamptz,
  marked_by                 uuid,                     -- admin who ticked a manual payment
  note                      text,
  provider_ref              text,                     -- Stripe Checkout Session id (cs_...)
  provider_payment_ref      text,                     -- Stripe PaymentIntent id (pi_...)
  provider_attempt          int  not null default 0,  -- bumped when a Checkout Session expires/fails; part of the Stripe idempotency key
  hitpay_payment_request_id text,                     -- retired (HitPay replaced by Stripe 22 Oct 2026), unused
  hitpay_payment_id         text,                     -- retired, unused
  created_at                timestamptz not null default now(),
  updated_at                timestamptz not null default now(),
  check (status <> 'paid' or paid_at is not null)
);

-- ---------- consents: append-only evidence. Latest row per (parent, consent_type) is the current state. ----------
create table public.consents (
  id            uuid primary key default gen_random_uuid(),
  seq           bigint generated always as identity,   -- ordering: several rows can share one transaction timestamp
  parent_id     uuid not null references public.parents(id),
  consent_type  text not null check (consent_type in ('contact','terms','recording','childs_work','feedback_quotes')),
  granted       boolean not null,
  terms_version   text not null check (char_length(terms_version) between 1 and 60),
  privacy_version text not null check (char_length(privacy_version) between 1 and 60),
  created_at    timestamptz not null default clock_timestamp()
);
create index consents_parent_idx on public.consents (parent_id, consent_type, seq desc);

create or replace function public.forbid_mutation() returns trigger language plpgsql as $$
begin raise exception 'consents is append-only'; end $$;
create trigger consents_append_only before update or delete on public.consents
  for each row execute function public.forbid_mutation();

-- ---------- placeholder for the practice area (written by a future server-side child session) ----------
create table public.practice_attempts (
  id          uuid primary key default gen_random_uuid(),
  child_id    uuid not null references public.children(id) on delete cascade,
  lesson_key  text not null,
  item_key    text not null,
  correct     boolean,
  hints_used  smallint not null default 0,
  created_at  timestamptz not null default now()
);
create index practice_attempts_child_idx on public.practice_attempts (child_id, created_at desc);

-- ---------- admin role: owner's auth user id goes here (insert by hand, see README) ----------
create table public.admins (
  user_id    uuid primary key,
  note       text,
  created_at timestamptz not null default now()
);

create table public.deletion_requests (
  id           uuid primary key default gen_random_uuid(),
  parent_id    uuid not null,
  requested_at timestamptz not null default now(),
  note         text
);

-- ---------- sign-up trigger: create the parents row ----------
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public, extensions as $$
declare code text; tries int := 0;
begin
  loop
    code := public.gen_code(6);
    exit when not exists (select 1 from public.parents where family_code = code);
    tries := tries + 1;
    if tries > 20 then raise exception 'could not allocate family code'; end if;
  end loop;
  insert into public.parents (id, email, full_name, family_code)
  values (new.id, new.email, left(nullif(btrim(new.raw_user_meta_data ->> 'full_name'), ''), 100), code);
  return new;
end $$;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- ======================================================================
-- Functions. All SECURITY DEFINER functions pin search_path and check auth.uid() themselves.
-- EXECUTE is granted explicitly in policies.sql (default PUBLIC execute is revoked there).
-- ======================================================================
create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.admins where user_id = auth.uid());
$$;

create or replace function public._require_parent() returns uuid
language plpgsql stable security definer set search_path = public as $$
declare uid uuid := auth.uid();
begin
  if uid is null then raise exception 'not_signed_in' using errcode = '28000'; end if;
  if not exists (select 1 from public.parents where id = uid and deleted_at is null) then
    raise exception 'no_parent_profile' using errcode = '28000';
  end if;
  return uid;
end $$;

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

-- Unpaid seat reservations expire. A pending_payment enrolment whose payment is still pending after p_days is cancelled (frees the seat).
-- Called (a) inside enrol_child for the group being booked, so no cron is needed, and (b) optionally by a scheduled job as
-- expire_unpaid_reservations(). Default 7 days: OWNER TO CONFIRM (docs/audit_final/open_owner_items.md). A payment that arrives afterwards
-- is recorded and reported as paid_enrolment_cancelled (late payment), never silently lost.
create or replace function public._expire_stale_reservations(p_group text default null, p_days int default 7) returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  with stale as (
    select e.id from public.enrolments e join public.payments p on p.enrolment_id = e.id
     where e.status = 'pending_payment' and p.status = 'pending'
       and e.created_at < now() - make_interval(days => greatest(p_days, 1))
       and (p_group is null or e.group_id = p_group)
     for update of e, p),
  ce as (update public.enrolments e set status = 'cancelled', cancelled_at = now() from stale s where e.id = s.id returning e.id)
  update public.payments p set status = 'cancelled', note = left(coalesce(p.note || ' ', '') || '[reservation expired, unpaid]', 500), updated_at = now()
    from ce where p.enrolment_id = ce.id;
  get diagnostics n = row_count;
  return n;
end $$;

create or replace function public.expire_unpaid_reservations(p_days int default 7) returns int
language sql security definer set search_path = public as $$ select public._expire_stale_reservations(null, p_days); $$;

create or replace function public.enrol_child(p_child uuid, p_group text) returns uuid
language plpgsql security definer set search_path = public, extensions as $$
declare uid uuid := public._require_parent(); ch public.children; g public.groups; eid uuid; ref text; tries int := 0; taken int; missing text;
begin
  select * into ch from public.children where id = p_child and parent_id = uid;
  if not found then raise exception 'not_found'; end if;
  select * into g from public.groups where id = p_group and active for update;   -- row lock serialises seat checks
  if not found then raise exception 'group_not_found'; end if;
  if g.level <> ch.level then raise exception 'level_mismatch'; end if;
  perform public._expire_stale_reservations(g.id);   -- free seats held by unpaid reservations older than 7 days
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
-- Look up a payable enrolment for a parent (the Cloudflare Function has already verified the parent's JWT).
-- Returns the payment id, the amount agreed at reservation (payments.amount_cents, copied from groups.fee_cents when the seat was reserved),
-- the group's current fee_cents (for logging; the function charges amount_cents), and the retry counter used in the Stripe idempotency key.
create or replace function public.service_begin_payment(p_enrolment uuid, p_parent uuid)
returns table (payment_id uuid, amount_cents int, currency text, group_fee_cents int, group_name text, reference text,
               payment_status text, enrolment_status text, parent_email text, parent_name text, attempt int)
language sql stable security definer set search_path = public as $$
  select p.id, p.amount_cents, p.currency, g.fee_cents, g.name, p.reference, p.status, e.status, pa.email, pa.full_name, p.provider_attempt
    from public.enrolments e
    join public.payments p on p.enrolment_id = e.id
    join public.parents pa on pa.id = e.parent_id
    join public.groups g on g.id = e.group_id
   where e.id = p_enrolment and e.parent_id = p_parent;
$$;

-- Remember which Checkout Session belongs to the payment. Only touches a payment that is still pending.
create or replace function public.service_attach_session(p_payment uuid, p_session_id text) returns void
language sql security definer set search_path = public as $$
  update public.payments set method = 'stripe', provider_ref = p_session_id, updated_at = now()
   where id = p_payment and status = 'pending';
$$;

-- Idempotent. Returns: paid | already_paid | duplicate_payment | not_payable:<status> | paid_enrolment_cancelled | amount_mismatch | currency_mismatch | not_found
--  * duplicate_payment: the payment is already paid by something else (manual PayNow ticked by the admin, or another PaymentIntent). Nothing is
--    changed; the webhook logs NEEDS OWNER ATTENTION so the owner refunds the second payment by hand. A repeat of the SAME PaymentIntent is already_paid.
--  * not_payable:refunded / not_payable:failed: a late event can never turn a refunded (or failed) payment back into paid. Nothing is changed.
--  * paid_enrolment_cancelled: money arrived after the enrolment was cancelled or the unpaid reservation expired (a LATE payment). The payment is
--    recorded as paid and the owner decides: re-open the seat if it is still free, or refund.
-- A mismatch changes nothing: the owner sees it in the Cloudflare log and handles it by hand.
create or replace function public.service_mark_paid(p_payment uuid, p_session_id text, p_payment_intent text, p_amount_cents int, p_currency text)
returns text language plpgsql security definer set search_path = public as $$
declare pay public.payments; est text;
begin
  select p.* into pay from public.payments p where p.id = p_payment for update;
  if not found then return 'not_found'; end if;
  if pay.status = 'paid' then
    if pay.method <> 'stripe' then return 'duplicate_payment'; end if;                                  -- paid by hand (PayNow), now Stripe too
    if p_payment_intent is not null and pay.provider_payment_ref is not null
       and pay.provider_payment_ref <> p_payment_intent then return 'duplicate_payment'; end if;        -- a second, different Stripe payment
    return 'already_paid';
  end if;
  if pay.status not in ('pending', 'cancelled') then return 'not_payable:' || pay.status; end if;       -- refunded / failed never flip back to paid
  if upper(coalesce(p_currency, '')) <> pay.currency then return 'currency_mismatch'; end if;
  if pay.amount_cents <> p_amount_cents then return 'amount_mismatch'; end if;
  update public.payments set status = 'paid', method = 'stripe', paid_at = now(),
         provider_ref = coalesce(p_session_id, provider_ref), provider_payment_ref = p_payment_intent, updated_at = now()
   where id = pay.id;
  select status into est from public.enrolments where id = pay.enrolment_id;
  if est = 'pending_payment' then
    update public.enrolments set status = 'confirmed' where id = pay.enrolment_id;
    return 'paid';
  end if;
  return 'paid_enrolment_cancelled';   -- money arrived for a cancelled/expired enrolment: owner must re-open the seat or refund by hand
end $$;

-- Checkout Session expired or an async (PayNow) payment failed: the payment stays 'pending' so the parent can try again,
-- but the session reference is cleared and the retry counter moves on so the next attempt gets a fresh idempotency key.
-- Returns: reset | ignored (not pending, or a different/newer session) | not_found
create or replace function public.service_mark_session_failed(p_payment uuid, p_session_id text) returns text
language plpgsql security definer set search_path = public as $$
declare pay public.payments;
begin
  select p.* into pay from public.payments p where p.id = p_payment for update;
  if not found then return 'not_found'; end if;
  if pay.status <> 'pending' or pay.provider_ref is distinct from p_session_id then return 'ignored'; end if;
  update public.payments set provider_ref = null, provider_attempt = provider_attempt + 1, updated_at = now() where id = pay.id;
  return 'reset';
end $$;

-- ---------- PDPA: delete my data ----------
-- NOTE: practice_submissions.sql REPLACES this function (create or replace) with the full version that also covers extension-book orders (delivery details,
-- child nickname), trial requests, recording views and free preview registrations. Always run it after this file.
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
