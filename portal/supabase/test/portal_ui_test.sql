-- Assertions for portal_ui.sql (DRAFT) and the two fixes made to create_ext_order() in practice_submissions.sql. Run by run_sql_test.sh after practice_submissions_test.sql
-- (same throwaway local PostgreSQL, same Supabase stand-in). Test prices below are TEST VALUES ONLY, not real prices.
\set ON_ERROR_STOP on
\i :HERE/../portal_ui.sql
\i :HERE/../portal_ui.sql
create or replace function pg_temp.fails(sql text, expect text default null) returns boolean language plpgsql as $$
begin execute sql; return false;
exception when others then
  if expect is not null and sqlerrm not like '%'||expect||'%' then raise exception 'wrong error for [%]: got [%], wanted [%]', sql, sqlerrm, expect; end if;
  return true; end $$;

reset role;
insert into auth.users (id, email) values
 ('11110000-0000-0000-0000-00000000aa01','uia@example.com'), ('11110000-0000-0000-0000-00000000bb02','uib@example.com');
-- units: holiday L2 (enrolled), extension L2 x2 published, extension L3 NOT published, extension L3 published
insert into public.practice_units (unit_key, unit_version, product, level, title, unit_no, access, published) values
 ('ui-hol-l2-01','v1','holiday',2,'Holiday L2 lesson 1',1,'enrolled',true),
 ('ui-ext-l2u01','v1','extension',2,'Ext L2 unit 1',1,'purchased',true), ('ui-ext-l2u02','v1','extension',2,'Ext L2 unit 2',2,'purchased',true),
 ('ui-ext-l3u01','v1','extension',3,'Ext L3 unit 1',1,'purchased',false), ('ui-ext-l3u02','v1','extension',3,'Ext L3 unit 2',2,'purchased',true),
 ('ui-ext-l2u01','v2','extension',2,'Ext L2 unit 1 (newer)',1,'purchased',true);
update public.practice_units set created_at = now() + interval '1 hour' where unit_key = 'ui-ext-l2u01' and unit_version = 'v2';   -- newer version
insert into public.practice_item_tags (unit_key, unit_version, item_id, position, marking_mode, strand, skill, slips) values
 ('ui-hol-l2-01','v1','q1',1,'auto','Whole Numbers','Place value','[{"a":[7],"say":"Gave the digit, not the value."}]'),
 ('ui-hol-l2-01','v1','q2',2,'auto','Whole Numbers','Place value','[]'),
 ('ui-hol-l2-01','v1','q3',3,'auto','Whole Numbers','Skip counting','[]'),
 ('ui-hol-l2-01','v1','q4',4,'self','Measurement and Geometry','Draw it','[]');
insert into public.ext_prices (product_id, amount_cents) values ('ext-l2-online', 100), ('ext-l2-both', 200), ('ext-l2-workbook', 100), ('ext-l3-online', 100)
  on conflict (product_id) do update set amount_cents = excluded.amount_cents, active = true;
insert into public.ext_prices (product_id, amount_cents, active) values ('ext-l4-online', 100, false) on conflict (product_id) do update set active = false;

-- ===== 1. prices: anyone may read the ACTIVE list; the table itself stays closed =====
set role anon; select set_config('request.jwt.claim.sub','',false);
do $$ begin
  assert (select count(*) from public.list_ext_prices() where product_id = 'ext-l2-online') = 1, 'active price listed';
  assert (select count(*) from public.list_ext_prices() where product_id = 'ext-l4-online') = 0, 'inactive price not listed';
  assert (select count(*) from public.list_ext_prices() where product_id = 'ext-l5-online') = 0, 'unset price: no row = price coming soon';
  assert pg_temp.fails('select * from public.ext_prices', 'permission denied'), 'table closed';
  assert pg_temp.fails($q$select public.add_child_profile('x', 1, '7391', 2020)$q$), 'anon can not add a child';
end $$;
reset role;

-- ===== 2. parent A: two children, birth year optional and checked =====
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
do $$ declare yr int := extract(year from now())::int; k uuid; l uuid; begin
  assert pg_temp.fails(format('select public.add_child_profile(%L, 2, %L, %s)', 'Old', '7391', yr - 40), 'bad_birth_year'), 'too old';
  assert pg_temp.fails(format('select public.add_child_profile(%L, 2, %L, %s)', 'Baby', '7391', yr), 'bad_birth_year'), 'too young';
  assert pg_temp.fails(format('select public.add_child_profile(%L, 2, %L)', 'Short', '12'), 'pin_format'), 'PIN rules of add_child still apply';
  k := public.add_child_profile('Kai', 2, '7391', yr - 8);
  l := public.add_child_profile('Lia', 2, '7142');
  assert (select birth_year from public.children where id = k) = yr - 8, 'birth year saved, readable by the parent';
  assert (select birth_year from public.children where id = l) is null, 'birth year is optional';
  perform public.update_child_birth_year(l, yr - 6);
  assert (select birth_year from public.children where id = l) = yr - 6;
  assert pg_temp.fails(format('select public.update_child_birth_year(%L, %s)', l, yr - 30), 'bad_birth_year');
  assert pg_temp.fails(format('select public.update_child_birth_year(%L, %s)', gen_random_uuid(), yr - 6), 'not_found');
  assert pg_temp.fails('select pin_hash from public.children', 'permission denied'), 'PIN hash still unreadable';
  perform public.record_consents('{"contact":true,"terms":true,"online_practice":true,"book_delivery":true}', 'tui', 'pui');
end $$;
reset role;

-- ===== 3. parent B: enrolled in L2A (live group family), one child =====
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000bb02',false);
do $$ declare m uuid; begin
  m := public.add_child_profile('Max', 2, '1873', null);
  perform public.record_consents('{"contact":true,"terms":true,"recording":true,"childs_work":true,"online_practice":true}', 'tui', 'pui');
  perform public.enrol_child(m, 'L2A');
end $$;
reset role;
create temp table uids as select
  (select id from public.children where display_name = 'Kai' and parent_id = '11110000-0000-0000-0000-00000000aa01') as kai,
  (select id from public.children where display_name = 'Lia' and parent_id = '11110000-0000-0000-0000-00000000aa01') as lia,
  (select id from public.children where display_name = 'Max' and parent_id = '11110000-0000-0000-0000-00000000bb02') as max,
  (select family_code from public.parents where id = '11110000-0000-0000-0000-00000000aa01') as ca,
  (select family_code from public.parents where id = '11110000-0000-0000-0000-00000000bb02') as cb;
grant all on uids to anon, authenticated, service_role;
do $$ begin assert (select count(*) from public.enrolments where child_id = (select max from uids) and status = 'pending_payment') = 1, 'Max reserved a place'; end $$;

-- before payment: Max has NOTHING (a reserved place is not an enrolment)
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000bb02',false);
do $$ begin
  assert (select count(*) from public.my_children_access()) = 0, 'no entitlement before the place is confirmed';
  assert (select count(*) from public.my_children_units()) = 0;
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
select public.admin_mark_paid((select id from public.payments where enrolment_id = (select id from public.enrolments where child_id = (select max from uids))));
reset role;

-- ===== 4. buying: pending order, guards, cancel, then pay =====
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
do $$ declare o uuid; o2 uuid; k uuid := (select kai from uids); begin
  o := public.create_ext_order(k, 2, 'online');
  assert pg_temp.fails(format('select public.create_ext_order(%L, 2, %L)', k, 'online'), 'already_pending'), 'one unpaid online order per child and level';
  assert pg_temp.fails(format('select public.create_ext_order(%L, 2, %L, %L, %L, %L)', k, 'both', 'A Parent', '1 Test Road', '123456'), 'already_pending'), 'an unpaid both blocks online for the same child and level';
  perform public.cancel_my_ext_order(o);
  assert (select status from public.ext_orders where id = o) = 'cancelled';
  assert pg_temp.fails(format('select public.cancel_my_ext_order(%L)', o), 'cannot_cancel_order'), 'only an unpaid order can be cancelled';
  -- a workbook order keeps its address until cancelled; cancel clears it
  o2 := public.create_ext_order(k, 2, 'workbook', 'A Parent', '5 Test Lane #02-03', '234567', '81234567');
  assert (select ship_status from public.ext_orders where id = o2) = 'to_ship';
  perform public.cancel_my_ext_order(o2);
  assert (select ship_address is null and ship_postal is null and ship_cleared_at is not null from public.ext_orders where id = o2), 'cancel clears the address';
  perform public.create_ext_order(k, 2, 'online');
end $$;
reset role;
-- consent fix: "both" also needs online_practice (a parent with delivery consent but no online_practice consent can not buy "both")
insert into auth.users (id, email) values ('11110000-0000-0000-0000-00000000cc03','uic@example.com');
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000cc03',false);
do $$ declare c uuid; begin
  c := public.add_child_profile('Cy', 3, '7391');
  perform public.record_consents('{"contact":true,"terms":true,"book_delivery":true}', 'tui', 'pui');
  assert pg_temp.fails(format('select public.create_ext_order(%L, 3, %L, %L, %L, %L)', c, 'both', 'C', '1 Road', '123456'), 'consents_missing:online_practice'), 'both needs online_practice';
  perform public.create_ext_order(c, 3, 'workbook', 'C', '1 Road', '123456', null);   -- ext-l3-workbook has no price yet
exception when others then
  if sqlerrm not like '%price_not_set%' then raise; end if;
end $$;
reset role;

-- parent B can not cancel parent A's order; the owner can mark it paid
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000bb02',false);
do $$ begin assert pg_temp.fails(format('select public.cancel_my_ext_order(%L)', (select id from public.ext_orders where child_id = (select kai from uids) and status = 'pending_payment')), 'cannot_cancel_order'); end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
do $$ begin assert pg_temp.fails($q$select public.admin_mark_ext_order_paid(id) from public.ext_orders$q$, 'forbidden'), 'a parent can not mark paid'; end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
select public.admin_mark_ext_order_paid((select id from public.ext_orders where child_id = (select kai from uids) and status = 'pending_payment'));
reset role;

-- ===== 5. what each child may open: the purchase is for Kai only =====
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
do $$ begin
  assert (select count(*) from public.my_children_access() where child_id = (select kai from uids) and kind = 'book' and level = 2 and format = 'online') = 1, 'Kai has L2 online';
  assert (select count(*) from public.my_children_access() where child_id = (select lia from uids)) = 0, 'sibling Lia has no access';
  assert (select count(*) from public.my_children_access() where child_id = (select max from uids)) = 0, 'other families never appear';
  assert (select count(*) from public.my_children_units() where child_id = (select kai from uids)) = 2, 'Kai: the two published L2 units (newest version of each unit once)';
  assert (select count(*) from public.my_children_units() where child_id = (select kai from uids) and unit_key = 'ui-ext-l2u01' and unit_version = 'v2') = 1, 'newest version';
  assert (select count(*) from public.my_children_units() where child_id = (select lia from uids)) = 0, 'Lia sees no unit';
  assert (select count(*) from public.my_children_units() where unit_key like 'ui-ext-l3%' or unit_key like 'ui-hol%') = 0, 'no L3 and no holiday unit for this family';
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000bb02',false);
do $$ begin
  assert (select count(*) from public.my_children_access() where kind = 'enrolled' and level = 2) = 1, 'enrolled L2 once confirmed';
  assert (select count(*) from public.my_children_units() where unit_key = 'ui-hol-l2-01') = 1, 'the holiday unit is open to the enrolled family';
  assert (select count(*) from public.my_children_units() where unit_key like 'ui-ext%') = 0, 'an enrolment does not unlock extension books';
end $$;
reset role;

-- child sign-in (needs online_practice: both families have it) and the child's own practice list
create temp table utok (who text, token text);
grant all on utok to anon, authenticated, service_role;
set role anon; select set_config('request.jwt.claim.sub','',false);
do $$ begin
  insert into utok select 'kai', token from public.child_start_session((select ca from uids), 'Kai', '7391');
  insert into utok select 'lia', token from public.child_start_session((select ca from uids), 'Lia', '7142');
  insert into utok select 'max', token from public.child_start_session((select cb from uids), 'Max', '1873');
  assert (select count(*) from utok) = 3, 'three sessions';
end $$;
do $$ declare k jsonb; l jsonb; m jsonb; begin
  k := public.child_session_overview((select token from utok where who = 'kai'));
  l := public.child_session_overview((select token from utok where who = 'lia'));
  m := public.child_session_overview((select token from utok where who = 'max'));
  assert k->>'name' = 'Kai' and (k->>'can_submit')::boolean, 'Kai overview';
  assert jsonb_array_length(k->'units') = 2 and (k->'units'->0->>'unit_key') = 'ui-ext-l2u01' and (k->'units'->1->>'unit_key') = 'ui-ext-l2u02', 'Kai: his two units, in order';
  assert jsonb_array_length(k->'access') = 1 and k->'access'->0->>'format' = 'online';
  assert jsonb_array_length(l->'units') = 0 and jsonb_array_length(l->'access') = 0, 'Lia (sibling) sees nothing';
  assert jsonb_array_length(m->'units') = 1 and m->'units'->0->>'unit_key' = 'ui-hol-l2-01' and m->'access'->0->>'kind' = 'enrolled', 'Max: holiday unit only';
  assert position('answer' in k::text) = 0 and position('token' in k::text) = 0 and position('hash' in k::text) = 0, 'nothing secret in the overview';
  assert public.child_session_overview('nonsense') is null and public.child_session_overview(null) is null and public.child_session_overview(repeat('a', 43)) is null, 'bad tokens give nothing';
  assert pg_temp.fails('select * from public.child_sessions', 'permission denied'), 'sessions table closed';
  assert pg_temp.fails('select * from public._entitlements(gen_random_uuid())', 'permission denied'), 'internal helper not callable';
end $$;
reset role;
-- an expired or revoked session gives nothing; withdrawing online_practice makes can_submit false
update public.child_sessions set expires_at = now() - interval '1 minute' where child_id = (select lia from uids);
set role anon;
do $$ begin assert public.child_session_overview((select token from utok where who = 'lia')) is null, 'expired token'; end $$;
select public.child_end_session((select token from utok where who = 'max'));
do $$ begin assert public.child_session_overview((select token from utok where who = 'max')) is null, 'signed-out token'; end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
select public.record_consents('{"online_practice":false}', 'tui', 'pui');
reset role;
set role anon;
do $$ begin assert (public.child_session_overview((select token from utok where who = 'kai'))->>'can_submit')::boolean = false, 'consent withdrawn'; end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
select public.record_consents('{"online_practice":true}', 'tui', 'pui');
reset role;

-- ===== 6. parent progress summary: counts of what was done, own children only =====
insert into public.practice_submissions (child_id, unit_key, unit_version, client_sid, rev, received_at, n_auto, n_right, n_wrong, n_skipped, n_self, n_self_got, n_open)
 values ((select kai from uids), 'ui-ext-l2u01', 'v1', gen_random_uuid(), 1, now() - interval '2 days', 6, 3, 2, 1, 1, 0, 1),
        ((select kai from uids), 'ui-ext-l2u01', 'v1', gen_random_uuid(), 1, now() - interval '1 day', 6, 5, 0, 1, 1, 1, 1);
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
do $$ declare r record; begin
  assert (select count(*) from public.my_children_progress()) = 1, 'one row per child and unit';
  select * into r from public.my_children_progress();
  assert r.child_id = (select kai from uids) and r.tries = 2 and r.n_auto = 6 and r.n_skipped = 1 and r.n_self_got = 1 and r.title = 'Ext L2 unit 1', 'newest attempt counts and the count of tries';
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000bb02',false);
do $$ begin assert (select count(*) from public.my_children_progress()) = 0, 'family B sees none of family A''s progress'; end $$;
reset role;

-- ===== 7. owner helpers: only the owner; prices; children and access lists =====
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
do $$ begin
  assert pg_temp.fails('select * from public.admin_list_children()', 'forbidden');
  assert pg_temp.fails('select * from public.admin_list_book_access()', 'forbidden');
  assert pg_temp.fails('select * from public.admin_list_ext_prices()', 'forbidden');
  assert pg_temp.fails($q$select public.admin_set_ext_price('ext-l6-online', 100, true)$q$, 'forbidden');
  assert pg_temp.fails($q$select public.admin_cancel_ext_order(gen_random_uuid())$q$, 'forbidden');
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ declare a uuid; begin
  assert (select count(*) from public.admin_list_children() where display_name in ('Kai','Lia','Max') and parent_email like 'ui%') = 3, 'owner sees the children with the parent email';
  assert (select count(*) from public.admin_list_book_access() where child_name = 'Kai' and format = 'online' and status = 'active' and source = 'paynow_manual') = 1, 'access row from the paid order';
  perform public.admin_set_ext_price('ext-l6-online', 100, true);
  assert (select amount_cents from public.admin_list_ext_prices() where product_id = 'ext-l6-online') = 100;
  perform public.admin_set_ext_price('ext-l6-online', 150, false);
  assert (select active from public.admin_list_ext_prices() where product_id = 'ext-l6-online') = false and (select amount_cents from public.admin_list_ext_prices() where product_id = 'ext-l6-online') = 150, 'upsert';
  assert pg_temp.fails($q$select public.admin_set_ext_price('not-a-product', 100, true)$q$), 'product id pattern enforced';
  assert pg_temp.fails($q$select public.admin_set_ext_price('ext-l6-both', 0, true)$q$), 'zero price rejected';
  -- grant to Lia (admin gift) and revoke again
  a := public.admin_grant_book_access((select lia from uids), 2, 'online', 'gift test');
  assert (select count(*) from public.admin_list_book_access() where child_name = 'Lia' and status = 'active' and source = 'admin') = 1;
  perform public.admin_revoke_book_access(a);
  assert (select status from public.admin_list_book_access() where access_id = a) = 'revoked';
end $$;
reset role;
set role anon;
do $$ begin assert jsonb_array_length(public.child_session_overview((select token from utok where who = 'kai'))->'units') = 2, 'Kai still has access after Lia''s gift was revoked'; end $$;
reset role;
-- an unpaid order the owner cancels
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
do $$ declare o uuid; begin o := public.create_ext_order((select lia from uids), 2, 'workbook', 'A Parent', '9 Test Rd', '345678', '81234567'); end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ declare o uuid := (select id from public.ext_orders where child_id = (select lia from uids) and status = 'pending_payment'); begin
  perform public.admin_cancel_ext_order(o);
  assert (select status from public.ext_orders where id = o) = 'cancelled' and (select ship_address from public.ext_orders where id = o) is null;
  assert pg_temp.fails(format('select public.admin_cancel_ext_order(%L)', o), 'cannot_cancel_order');
end $$;
reset role;

-- ===== 8. tutor group report (L2A: Max) =====
insert into public.practice_submissions (id, child_id, unit_key, unit_version, client_sid, rev, received_at, n_auto, n_right, n_wrong, n_skipped, n_self, n_self_got, n_open)
 values ('77770000-0000-0000-0000-000000000001', (select max from uids), 'ui-hol-l2-01', 'v1', gen_random_uuid(), 1, now(), 3, 1, 1, 1, 1, 1, 0),
        ('77770000-0000-0000-0000-000000000002', (select max from uids), 'ui-hol-l2-01', 'v1', gen_random_uuid(), 1, now() - interval '3 days', 3, 0, 3, 0, 1, 0, 0);
insert into public.practice_attempts (child_id, lesson_key, item_key, submission_id, unit_version, marking_mode, mark, slip_idx, self_result) values
 ((select max from uids), 'ui-hol-l2-01', 'q1', '77770000-0000-0000-0000-000000000001', 'v1', 'auto', 'wrong', 0, null),
 ((select max from uids), 'ui-hol-l2-01', 'q2', '77770000-0000-0000-0000-000000000001', 'v1', 'auto', 'right', null, null),
 ((select max from uids), 'ui-hol-l2-01', 'q3', '77770000-0000-0000-0000-000000000001', 'v1', 'auto', 'skipped', null, null),
 ((select max from uids), 'ui-hol-l2-01', 'q4', '77770000-0000-0000-0000-000000000001', 'v1', 'self', 'self', null, 'got'),
 ((select max from uids), 'ui-hol-l2-01', 'q1', '77770000-0000-0000-0000-000000000002', 'v1', 'auto', 'wrong', 0, null),
 ((select max from uids), 'ui-hol-l2-01', 'q2', '77770000-0000-0000-0000-000000000002', 'v1', 'auto', 'wrong', null, null);
set role authenticated; select set_config('request.jwt.claim.sub','d4d4d4d4-0000-0000-0000-0000000000d4',false);   -- tutor of L2A
do $$ begin
  assert (select count(*) from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01')) = 3, 'two skills plus the paper row, newest submission only';
  assert (select n_right from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01') where skill = 'Place value') = 1 and
         (select n_wrong from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01') where skill = 'Place value') = 1, 'newest submission counted, not the older one';
  assert (select n_skipped from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01') where skill = 'Skip counting') = 1;
  assert (select n_self_got from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01') where skill is null) = 1, 'checked on paper kept apart';
  assert (select display_name from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01') limit 1) = 'Max';
  assert (select count(*) from public.tutor_group_slips('L2A', 'ui-hol-l2-01')) = 1 and
         (select say from public.tutor_group_slips('L2A', 'ui-hol-l2-01')) = 'Gave the digit, not the value.' and
         (select n_children from public.tutor_group_slips('L2A', 'ui-hol-l2-01')) = 1 and (select n_sent from public.tutor_group_slips('L2A', 'ui-hol-l2-01')) = 1;
  assert pg_temp.fails($q$select * from public.tutor_group_skill_report('L1A', 'ui-hol-l2-01')$q$, 'forbidden'), 'not their group';
  assert pg_temp.fails($q$select * from public.tutor_group_slips('L1A', 'ui-hol-l2-01')$q$, 'forbidden');
  assert not exists (select 1 from public.tutor_group_slips('L2A', 'ui-hol-l2-01') where say ~* 'answer_key|key'), 'no key text';
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','c3c3c3c3-0000-0000-0000-0000000000c3',false);   -- tutor of L1A only
do $$ begin
  assert pg_temp.fails($q$select * from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01')$q$, 'forbidden'), 'another group''s tutor';
  assert (select count(*) from public.tutor_group_skill_report('L1A', 'ui-hol-l2-01')) = 0;
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ begin assert (select count(*) from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01')) = 3, 'owner reads any group'; end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','11110000-0000-0000-0000-00000000aa01',false);
do $$ begin assert pg_temp.fails($q$select * from public.tutor_group_skill_report('L2A', 'ui-hol-l2-01')$q$, 'forbidden'), 'a parent is not a tutor'; end $$;
reset role;

-- ===== 9. the new functions are not callable by the wrong roles =====
set role anon; select set_config('request.jwt.claim.sub','',false);
do $$ begin
  assert pg_temp.fails('select * from public.my_children_access()', 'permission denied');
  assert pg_temp.fails('select * from public.my_children_progress()', 'permission denied');
  assert pg_temp.fails('select * from public.admin_list_children()', 'permission denied');
  assert pg_temp.fails('select * from public.tutor_group_slips(''L2A'',''x'')', 'permission denied');
  assert pg_temp.fails($q$select public.cancel_my_ext_order(gen_random_uuid())$q$, 'permission denied');
end $$;
reset role;

select 'portal_ui_test: all assertions passed' as result;
