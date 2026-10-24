-- Math Inquirers: SQL that the portal screens need on top of practice_submissions.sql (what the screens read; nothing here changes who may write what).
-- DRAFT. NOT APPLIED to any database by the author. Run AFTER schema.sql, policies.sql and practice_submissions.sql (in that order). Safe to re-run.
-- Review first, try on a scratch Supabase project, never first on the live one. See docs/portal_ui_status.md and portal/README.md ("Portal screens").
--
-- What is in here
--   1. children.birth_year (OPTIONAL, owner and lawyer to confirm: the original schema promised "no birth date"; a birth YEAR is the minimum that
--      lets us suggest a level) + add_child_profile() / update_child_birth_year().
--   2. list_ext_prices(): the price list the buy screen shows. ext_prices stays empty until the owner fills it: no row means "price coming soon".
--   3. What a child may open: _entitlements(), _child_units(), my_children_access(), my_children_units(), my_children_progress(), child_session_overview().
--      One place for the rule, the same rule as _can_access() in practice_submissions.sql.
--   4. cancel_my_ext_order() (a parent cancels an unpaid order, e.g. chose the wrong child) and the owner's admin_* helpers for the admin tabs.
--   5. Tutor group report helpers (by skill; most common misconceptions). Counts only, alphabetical, never ranked.
-- Nothing in here returns an answer key, a PIN hash, a token hash or another family's rows.

-- ---------- 1. optional birth year ----------
alter table public.children add column if not exists birth_year smallint check (birth_year is null or birth_year between 2000 and 2100);
grant select (birth_year) on public.children to authenticated;      -- the column-level select list in policies.sql does not include it

create or replace function public._valid_birth_year(p int) returns boolean
language sql stable set search_path = public, pg_temp as $$
  select p is null or (p between extract(year from now())::int - 18 and extract(year from now())::int - 3);
$$;

create or replace function public.add_child_profile(p_name text, p_level int, p_pin text, p_birth_year int default null) returns uuid
language plpgsql security definer set search_path = public, extensions, pg_temp as $$
declare cid uuid;
begin
  if not public._valid_birth_year(p_birth_year) then raise exception 'bad_birth_year'; end if;
  cid := public.add_child(p_name, p_level, p_pin);          -- checks the parent, the PIN format and the limit of 6 children
  update public.children set birth_year = p_birth_year where id = cid;
  return cid;
end $$;

create or replace function public.update_child_birth_year(p_child uuid, p_year int) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
declare uid uuid := public._require_parent();
begin
  if not public._valid_birth_year(p_year) then raise exception 'bad_birth_year'; end if;
  update public.children set birth_year = p_year, updated_at = now() where id = p_child and parent_id = uid;
  if not found then raise exception 'not_found'; end if;
end $$;

-- ---------- 2. prices the buy screen may show (active rows only; empty table = "price coming soon") ----------
create or replace function public.list_ext_prices() returns table (product_id text, amount_cents int)
language sql stable security definer set search_path = public, pg_temp as $$
  select p.product_id, p.amount_cents from public.ext_prices p where p.active order by p.product_id;
$$;

-- ---------- 3. what a child may open ----------
-- 'enrolled' rows: a confirmed enrolment (any child of the same parent) in a group of that level opens the holiday and term practice of that level.
-- 'book' rows: child_book_access for THIS child only (a sibling gets nothing from it). format 'workbook' means a posted book only: no online access.
create or replace function public._entitlements(p_child uuid) returns table (kind text, level smallint, format text, source text, access_id uuid, since timestamptz)
language sql stable security definer set search_path = public, pg_temp as $$
  select 'enrolled'::text, g.level, null::text, 'enrolment'::text, null::uuid, min(e.created_at)
    from public.enrolments e join public.groups g on g.id = e.group_id
    join public.children c2 on c2.id = e.child_id join public.children c on c.id = p_child
   where c2.parent_id = c.parent_id and e.status = 'confirmed' group by g.level
  union all
  select 'book'::text, a.level, a.format, a.source, a.id, a.created_at
    from public.child_book_access a where a.child_id = p_child and a.status = 'active';
$$;

-- Published units this child may open right now (the newest version of each unit). Same rule as _can_access(): not 'open' sample pages.
create or replace function public._child_units(p_child uuid) returns table (unit_key text, unit_version text, product text, level smallint, unit_no smallint, title text)
language sql stable security definer set search_path = public, pg_temp as $$
  select x.unit_key, x.unit_version, x.product, x.level, x.unit_no, x.title from (
    select distinct on (u.unit_key) u.unit_key, u.unit_version, u.product, u.level, u.unit_no, u.title
      from public.practice_units u where u.published and public._can_access(p_child, u.unit_key, u.unit_version)
     order by u.unit_key, u.created_at desc) x
  order by case x.product when 'holiday' then 1 when 'term' then 2 else 3 end, x.level, x.unit_no, x.unit_key;
$$;

create or replace function public.my_children_access() returns table (child_id uuid, kind text, level smallint, format text, source text, access_id uuid, since timestamptz)
language sql stable security definer set search_path = public, pg_temp as $$
  select c.id, x.kind, x.level, x.format, x.source, x.access_id, x.since
    from public.children c cross join lateral public._entitlements(c.id) x
   where c.parent_id = public._require_parent() order by c.created_at, x.kind, x.level;
$$;

create or replace function public.my_children_units() returns table (child_id uuid, unit_key text, unit_version text, product text, level smallint, unit_no smallint, title text)
language sql stable security definer set search_path = public, pg_temp as $$
  select c.id, u.unit_key, u.unit_version, u.product, u.level, u.unit_no, u.title
    from public.children c cross join lateral public._child_units(c.id) u
   where c.parent_id = public._require_parent() order by c.created_at;
$$;

-- Parent progress summary: one row per child and unit, the newest submission. Counts of what was done only: NO right/wrong counts, no score, no rank,
-- no time. (Question-level "worth looking at together" comes from practice_child_detail(), which the parent may already call for their own child.)
create or replace function public.my_children_progress() returns table (child_id uuid, unit_key text, title text, product text, level smallint, unit_no smallint,
  tries int, last_received_at timestamptz, n_auto smallint, n_skipped smallint, n_self smallint, n_self_got smallint, n_open smallint)
language sql stable security definer set search_path = public, pg_temp as $$
  select l.child_id, l.unit_key, u.title, u.product, u.level, u.unit_no, l.tries::int, l.received_at, l.n_auto, l.n_skipped, l.n_self, l.n_self_got, l.n_open
    from (select distinct on (s.child_id, s.unit_key) s.child_id, s.unit_key, s.unit_version, s.received_at, s.n_auto, s.n_skipped, s.n_self, s.n_self_got, s.n_open,
                 count(*) over (partition by s.child_id, s.unit_key) as tries
            from public.practice_submissions s join public.children c on c.id = s.child_id
           where c.parent_id = public._require_parent()
           order by s.child_id, s.unit_key, s.received_at desc) l
    join public.practice_units u on u.unit_key = l.unit_key and u.unit_version = l.unit_version
   order by l.received_at desc;
$$;

-- The child's own practice list, from the 4-hour token (and at most 60 minutes idle) that child_start_session() gave them. Returns null for an unknown, expired or revoked token
-- (the page then sends the child back to sign in). Only what THIS child may open; the answer keys are never involved.
create or replace function public.child_session_overview(p_token text) returns jsonb
language plpgsql security definer set search_path = public, extensions, pg_temp as $$
declare h text; cid uuid; c public.children; s public.child_sessions;
begin
  if p_token is null or p_token !~ '^[A-Za-z0-9_-]{32,128}$' then return null; end if;
  h := encode(extensions.digest(p_token, 'sha256'), 'hex');
  cid := public._child_for_token(h);
  if cid is null then return null; end if;
  perform public._touch_child_session(h);        -- R1-L6: using the list keeps the 60-minute idle clock alive; an unused session stops working
  select * into c from public.children where id = cid;
  select * into s from public.child_sessions where token_hash = h;
  return jsonb_build_object(
    'child_id', cid, 'name', c.display_name, 'level', c.level, 'expires_at', s.expires_at,
    'can_submit', public._practice_consents_ok(c.parent_id),
    'access', coalesce((select jsonb_agg(jsonb_build_object('kind', x.kind, 'level', x.level, 'format', x.format) order by x.kind, x.level)
                          from public._entitlements(cid) x where x.kind = 'enrolled' or x.format in ('online','both')), '[]'::jsonb),
    'units',  coalesce((select jsonb_agg(jsonb_build_object('unit_key', u.unit_key, 'product', u.product, 'level', u.level, 'unit_no', u.unit_no, 'title', u.title))
                          from public._child_units(cid) u), '[]'::jsonb));
end $$;

-- ---------- 4. parent cancels an unpaid order; owner helpers ----------
create or replace function public.cancel_my_ext_order(p_order uuid) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
declare uid uuid := public._require_parent();
begin
  update public.ext_orders set status = 'cancelled', ship_status = 'not_needed', ship_name = null, ship_address = null, ship_postal = null, ship_phone = null, ship_cleared_at = now()
   where id = p_order and parent_id = uid and status = 'pending_payment';
  if not found then raise exception 'cannot_cancel_order'; end if;
end $$;

create or replace function public.admin_cancel_ext_order(p_order uuid) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  update public.ext_orders set status = 'cancelled', ship_status = 'not_needed', ship_name = null, ship_address = null, ship_postal = null, ship_phone = null, ship_cleared_at = now()
   where id = p_order and status = 'pending_payment';
  if not found then raise exception 'cannot_cancel_order'; end if;
end $$;

create or replace function public.admin_list_children() returns table (child_id uuid, display_name text, level smallint, birth_year smallint, parent_email text, parent_name text)
language plpgsql stable security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query select c.id, c.display_name, c.level, c.birth_year, p.email, p.full_name
                 from public.children c join public.parents p on p.id = c.parent_id where p.deleted_at is null order by lower(p.email), c.created_at limit 1000;
end $$;

create or replace function public.admin_list_book_access() returns table (access_id uuid, child_id uuid, child_name text, parent_email text, level smallint, format text,
  source text, source_note text, status text, created_at timestamptz, ended_at timestamptz)
language plpgsql stable security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query select a.id, a.child_id, c.display_name, p.email, a.level, a.format, a.source, a.source_note, a.status, a.created_at, a.ended_at
                 from public.child_book_access a join public.children c on c.id = a.child_id join public.parents p on p.id = c.parent_id
                order by a.created_at desc limit 500;
end $$;

create or replace function public.admin_list_ext_prices() returns table (product_id text, amount_cents int, active boolean)
language plpgsql stable security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return query select p.product_id, p.amount_cents, p.active from public.ext_prices p order by p.product_id;
end $$;

-- The OWNER sets a price (cents, Singapore dollars). Nothing in the repo contains a price; an order cannot be made until this has been called.
create or replace function public.admin_set_ext_price(p_product text, p_cents int, p_active boolean default true) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  insert into public.ext_prices (product_id, amount_cents, active) values (p_product, p_cents, coalesce(p_active, true))
  on conflict (product_id) do update set amount_cents = excluded.amount_cents, active = excluded.active;
end $$;

-- ---------- 5. tutor group report helpers (the tutor of the group, or the owner) ----------
-- One row per child and skill, from the child's NEWEST submission of the unit, auto-marked items only. skill is null on the one extra row per child
-- that counts the checked-on-paper items (those are never mixed into the auto-marked counts).
create or replace function public.tutor_group_skill_report(p_group text, p_unit text)
returns table (child_id uuid, display_name text, skill text, n_right int, n_wrong int, n_skipped int, n_self_got int, n_self_notyet int, n_self_checked int)
language plpgsql stable security definer set search_path = public, pg_temp as $$
#variable_conflict use_column
begin
  if not (public.is_admin() or public.is_tutor_of_group(p_group)) then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
    with kids as (select distinct c.id as cid, c.display_name as cname from public.enrolments e join public.children c on c.id = e.child_id
                   where e.group_id = p_group and e.status = 'confirmed'),
         latest as (select distinct on (s.child_id) s.id as sid, s.child_id as cid from public.practice_submissions s join kids k on k.cid = s.child_id
                     where s.unit_key = p_unit order by s.child_id, s.received_at desc)
    select k.cid, k.cname, coalesce(t.skill, 'Other')::text,
           (count(*) filter (where a.mark = 'right'))::int, (count(*) filter (where a.mark = 'wrong'))::int, (count(*) filter (where a.mark = 'skipped'))::int, 0, 0, 0
      from latest l join kids k on k.cid = l.cid join public.practice_attempts a on a.submission_id = l.sid
      join public.practice_item_tags t on t.unit_key = p_unit and t.unit_version = a.unit_version and t.item_id = a.item_key
     where a.marking_mode = 'auto' group by k.cid, k.cname, coalesce(t.skill, 'Other')
    union all
    select k.cid, k.cname, null::text, 0, 0, 0,
           (count(*) filter (where a.self_result = 'got'))::int, (count(*) filter (where a.self_result = 'not_yet'))::int, (count(*) filter (where a.self_result = 'checked'))::int
      from latest l join kids k on k.cid = l.cid join public.practice_attempts a on a.submission_id = l.sid
     where a.marking_mode = 'self' group by k.cid, k.cname
    order by 2, 3;
end $$;

-- The most common listed wrong answers (with the kindly worded likely misconception) across the group's newest submissions, for planning the next lesson.
create or replace function public.tutor_group_slips(p_group text, p_unit text)
returns table (item_id text, item_pos int, skill text, say text, n_children int, n_sent int)
language plpgsql stable security definer set search_path = public, pg_temp as $$
#variable_conflict use_column
begin
  if not (public.is_admin() or public.is_tutor_of_group(p_group)) then raise exception 'forbidden' using errcode = '42501'; end if;
  return query
    with kids as (select distinct e.child_id as cid from public.enrolments e where e.group_id = p_group and e.status = 'confirmed' and e.child_id is not null),
         latest as (select distinct on (s.child_id) s.id as sid, s.child_id as cid from public.practice_submissions s join kids k on k.cid = s.child_id
                     where s.unit_key = p_unit order by s.child_id, s.received_at desc)
    select a.item_key, t.position, t.skill, (t.slips -> a.slip_idx::int ->> 'say')::text, (count(distinct l.cid))::int, (select count(*) from latest)::int
      from latest l join public.practice_attempts a on a.submission_id = l.sid
      join public.practice_item_tags t on t.unit_key = p_unit and t.unit_version = a.unit_version and t.item_id = a.item_key
     where a.mark = 'wrong' and a.slip_idx is not null and (t.slips -> a.slip_idx::int ->> 'say') is not null
     group by a.item_key, t.position, t.skill, (t.slips -> a.slip_idx::int ->> 'say')
     order by 5 desc, t.position;
end $$;

-- ---------- 6. grants (revoked first, then granted narrowly; same pattern as practice_submissions.sql) ----------
revoke all on function public._valid_birth_year(int), public.add_child_profile(text, int, text, int), public.update_child_birth_year(uuid, int), public.list_ext_prices(),
  public._entitlements(uuid), public._child_units(uuid), public.my_children_access(), public.my_children_units(), public.my_children_progress(),
  public.child_session_overview(text), public.cancel_my_ext_order(uuid), public.admin_cancel_ext_order(uuid), public.admin_list_children(),
  public.admin_list_book_access(), public.admin_list_ext_prices(), public.admin_set_ext_price(text, int, boolean),
  public.tutor_group_skill_report(text, text), public.tutor_group_slips(text, text)
  from public, anon, authenticated;
grant execute on function public.list_ext_prices() to anon, authenticated;
grant execute on function public.child_session_overview(text) to anon, authenticated;            -- the 4-hour child token is the credential
grant execute on function public.add_child_profile(text, int, text, int), public.update_child_birth_year(uuid, int),
  public.my_children_access(), public.my_children_units(), public.my_children_progress(), public.cancel_my_ext_order(uuid) to authenticated;   -- _require_parent() inside
grant execute on function public.admin_cancel_ext_order(uuid), public.admin_list_children(), public.admin_list_book_access(), public.admin_list_ext_prices(),
  public.admin_set_ext_price(text, int, boolean) to authenticated;                                -- is_admin() inside
grant execute on function public.tutor_group_skill_report(text, text), public.tutor_group_slips(text, text) to authenticated;   -- tutor of the group or admin, checked inside
-- _valid_birth_year(), _entitlements() and _child_units() are internal: not granted to any API role.
