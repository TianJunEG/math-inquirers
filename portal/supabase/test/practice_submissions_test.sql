-- Assertions for practice_submissions.sql (DRAFT). Run by run_sql_test.sh after schema, policies, seed and the other tests. Local throwaway Postgres only.
\set ON_ERROR_STOP on
\i :HERE/../practice_submissions.sql
create or replace function pg_temp.fails(sql text, expect text default null) returns boolean language plpgsql as $$
begin execute sql; return false;
exception when others then
  if expect is not null and sqlerrm not like '%'||expect||'%' then raise exception 'wrong error for [%]: got [%], wanted [%]', sql, sqlerrm, expect; end if;
  return true; end $$;
create or replace function pg_temp.h(t text) returns text language sql as $$ select encode(extensions.digest(t, 'sha256'), 'hex') $$;

reset role;
insert into auth.users (id, email) values
 ('a1a1a1a1-0000-0000-0000-0000000000a1','psa@example.com'), ('b2b2b2b2-0000-0000-0000-0000000000b2','psb@example.com'),
 ('c3c3c3c3-0000-0000-0000-0000000000c3','tutor1@example.com'), ('d4d4d4d4-0000-0000-0000-0000000000d4','tutor2@example.com'),
 ('e5e5e5e5-0000-0000-0000-0000000000e5','owner2@example.com');
insert into public.admins (user_id) values ('e5e5e5e5-0000-0000-0000-0000000000e5');
insert into public.tutors (user_id, note) values ('c3c3c3c3-0000-0000-0000-0000000000c3','T1'), ('d4d4d4d4-0000-0000-0000-0000000000d4','T2');
insert into public.tutor_groups values ('c3c3c3c3-0000-0000-0000-0000000000c3','L1A'), ('d4d4d4d4-0000-0000-0000-0000000000d4','L2A');
-- units, tags, keys (loaded by the owner/agent with service role, never by a client)
insert into public.practice_units (unit_key, unit_version, product, level, title, unit_no, access, published) values
 ('hol-l1l01','v1','holiday',1,'Holiday L1',1,'enrolled',true), ('ext-l1u01','v1','extension',1,'Ext L1 U1',1,'purchased',true),
 ('ext-l1u02','v1','extension',1,'Ext L1 U2',2,'purchased',true), ('smp-l1u01','v1','extension',1,'Sample',1,'open',true);
insert into public.practice_item_tags (unit_key, unit_version, item_id, position, marking_mode, strand, skill, slips) values
 ('hol-l1l01','v1','q1',1,'auto','Whole Numbers','Place value','[{"a":[7],"say":"7 is 3 + 4. Count the tens first."}]'),
 ('hol-l1l01','v1','q2',2,'auto','Whole Numbers','Skip counting','[]'), ('hol-l1l01','v1','q3',3,'self','Measurement and Geometry','Draw a line','[]'),
 ('hol-l1l01','v1','q4',4,'none','Whole Numbers','Make a riddle','[]'),
 ('ext-l1u01','v1','q1',1,'auto','Whole Numbers','x','[]'), ('ext-l1u02','v1','q1',1,'auto','Whole Numbers','x','[]'), ('smp-l1u01','v1','q1',1,'auto','Whole Numbers','x','[]');
insert into public.practice_item_keys (unit_key, unit_version, item_id, answer_type, answer_key) values
 ('hol-l1l01','v1','q1','number','9'), ('hol-l1l01','v1','q2','number','20'), ('hol-l1l01','v1','q3','selfcheck',null), ('hol-l1l01','v1','q4','open',null),
 ('ext-l1u01','v1','q1','number','1'), ('ext-l1u02','v1','q1','number','1'), ('smp-l1u01','v1','q1','number','1');

-- ===== parent A: child Mia, consents, enrolment =====
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
do $$ declare c uuid; e uuid; begin
  c := public.add_child('Mia', 1, '1234');
  perform public.record_consents('{"contact":true,"terms":true,"recording":true,"childs_work":true}', 't1', 'p1');
  e := public.enrol_child(c, 'L1A');
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
select public.admin_mark_paid((select id from public.payments where enrolment_id = (select id from public.enrolments where parent_id = 'a1a1a1a1-0000-0000-0000-0000000000a1')));
reset role;
-- ===== parent B: child Ben, no enrolment, no practice consent =====
set role authenticated; select set_config('request.jwt.claim.sub','b2b2b2b2-0000-0000-0000-0000000000b2',false);
do $$ begin perform public.add_child('Ben', 1, '4321'); perform public.record_consents('{"contact":true,"terms":true,"recording":true,"childs_work":true}', 't1', 'p1'); end $$;
reset role;

-- ===== sessions: need the online_practice consent; wrong PIN gives nothing; same silent failure =====
create temp table codes as select 'x'::text as a, (select family_code from public.parents where email = 'psa@example.com') as ca, (select family_code from public.parents where email = 'psb@example.com') as cb;
grant all on codes to anon, authenticated, service_role;
set role anon; select set_config('request.jwt.claim.sub','',false);
do $$ declare ca text := (select ca from codes); cb text := (select cb from codes); begin
  assert (select count(*) from public.child_start_session(ca, 'Mia', '1234')) = 0, 'no session before the online_practice consent';
  assert (select count(*) from public.child_start_session(cb, 'Ben', '4321')) = 0, 'B has no consent';
  assert (select count(*) from public.child_start_session(ca, 'Mia', '0000')) = 0, 'wrong PIN';
  assert pg_temp.fails('select * from public.child_sessions', 'permission denied'), 'anon can not read sessions';
  assert pg_temp.fails('select * from public.practice_item_keys', 'permission denied'), 'anon can not read keys';
  assert pg_temp.fails('select * from public.practice_attempts', 'permission denied');
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
select public.record_consents('{"online_practice":true}', 't2', 'p2');
reset role;
set role anon;
create temp table tok as select * from public.child_start_session((select ca from codes), 'Mia', '1234');
reset role;
grant all on tok to service_role;
do $$ begin assert (select count(*) from tok) = 1 and (select length(token) from tok) = 43, 'session minted'; assert (select count(*) from public.child_sessions) = 1; end $$;
do $$ begin assert (select token_hash from public.child_sessions) <> (select token from tok), 'only the hash is stored'; end $$;

-- ===== service functions: enrolment gate (holiday), entitlement gate (extension), open sample, consent =====
set role service_role;
do $$ declare th text := pg_temp.h((select token from tok)); r jsonb; begin
  r := public.service_practice_keys(th, 'hol-l1l01', 'v1');
  assert (r->>'ok')::boolean and jsonb_array_length(r->'keys') = 4, 'enrolled family gets the keys: ' || r::text;
  assert r->'keys'->0->>'key' = '9';
  assert public.service_practice_keys(pg_temp.h('nope'), 'hol-l1l01', 'v1')->>'error' = 'session';
  assert public.service_practice_keys(th, 'ext-l1u01', 'v1')->>'error' = 'entitlement', 'extension needs an entitlement';
  assert public.service_practice_keys(th, 'smp-l1u01', 'v1')->>'error' = 'unit', 'sample units are never submitted';
  assert public.service_practice_keys(th, 'zzz-l9u99', 'v1')->>'error' = 'unit';
end $$;
reset role;
-- Ben's family is not enrolled and has no consent even with a token: build one by hand to prove the gates in the service functions themselves
insert into public.child_sessions (child_id, token_hash, expires_at) select id, pg_temp.h('BEN-TOKEN'), now() + interval '1 hour' from public.children where parent_id = 'b2b2b2b2-0000-0000-0000-0000000000b2';
set role service_role;
do $$ begin
  assert public.service_practice_keys(pg_temp.h('BEN-TOKEN'), 'hol-l1l01', 'v1')->>'error' = 'consent';
end $$;
reset role;

-- ===== record: marks stored, idempotent, stale, replace; bad rows refused =====
set role service_role;
do $$ declare th text := pg_temp.h((select token from tok)); sid uuid := '99999999-9999-4999-8999-999999999999'; r jsonb;
 rows1 jsonb := '[{"item_id":"q1","marking_mode":"auto","mark":"wrong","answer_text":"7","answered":true,"slip_idx":0},
                  {"item_id":"q2","marking_mode":"auto","mark":"skipped","answered":false},
                  {"item_id":"q3","marking_mode":"self","mark":"self","answered":true,"self_result":"got"},
                  {"item_id":"q4","marking_mode":"none","mark":"open","answered":true}]'; begin
  r := public.service_practice_record(th, 'hol-l1l01', 'v1', sid, 1, rows1);
  assert (r->>'ok')::boolean and r->>'rev' = '1', r::text;
  assert (select n_auto = 2 and n_right = 0 and n_wrong = 1 and n_skipped = 1 and n_self = 1 and n_self_got = 1 and n_open = 1 from public.practice_submissions), 'counts recomputed by the database';
  assert (select count(*) from public.practice_attempts) = 4;
  assert (select correct from public.practice_attempts where item_key = 'q1') = false and (select correct from public.practice_attempts where item_key = 'q3') is null;
  assert (public.service_practice_record(th, 'hol-l1l01', 'v1', sid, 1, rows1)->>'duplicate')::boolean, 'same rev is a duplicate';
  assert (select count(*) from public.practice_submissions) = 1;
  r := public.service_practice_record(th, 'hol-l1l01', 'v1', sid, 3, replace(rows1::text, '"wrong"', '"right"')::jsonb);
  assert r->>'rev' = '3' and (select n_right from public.practice_submissions) = 1 and (select count(*) from public.practice_attempts) = 4, 'higher rev replaces';
  assert (public.service_practice_record(th, 'hol-l1l01', 'v1', sid, 2, rows1)->>'stale')::boolean, 'older rev ignored';
  assert (select rev from public.practice_submissions) = 3;
  assert public.service_practice_record(th, 'hol-l1l01', 'v1', gen_random_uuid(), 1, '[{"item_id":"q1","marking_mode":"auto","mark":"self"}]')->>'error' = 'bad_rows', 'auto item can not be self';
  assert public.service_practice_record(th, 'hol-l1l01', 'v1', gen_random_uuid(), 1, '[{"item_id":"q3","marking_mode":"self","mark":"right"}]')->>'error' = 'bad_rows', 'self item can not be right';
  assert public.service_practice_record(th, 'hol-l1l01', 'v1', gen_random_uuid(), 1, '[{"item_id":"zz","marking_mode":"auto","mark":"right"}]')->>'error' = 'bad_rows', 'unknown item';
  assert public.service_practice_record(th, 'ext-l1u01', 'v1', gen_random_uuid(), 1, '[]')->>'error' = 'entitlement';
end $$;
reset role;
do $$ begin assert (select count(*) from public.practice_submissions) = 1, 'rejected calls stored nothing'; end $$;

-- ===== RLS: parent, other parent, tutor of the group, tutor of another group, anon =====
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
do $$ declare c uuid := (select id from public.children where display_name = 'Mia'); begin
  assert (select count(*) from public.practice_submissions) = 1 and (select count(*) from public.practice_attempts) = 4, 'parent A sees own child rows';
  assert (select count(*) from public.practice_child_detail(c, 'hol-l1l01')) = 4;
  assert (select misconception from public.practice_child_detail(c, 'hol-l1l01') where item_id = 'q1') like '7 is 3 + 4%', 'misconception text comes from the tags table';
  assert pg_temp.fails($q$select * from public.practice_item_keys$q$, 'permission denied'), 'parent can not read keys';
  assert pg_temp.fails($q$insert into public.practice_attempts (child_id, lesson_key, item_key) select id, 'x', 'y' from public.children$q$, 'permission denied'), 'no direct insert';
  assert pg_temp.fails($q$update public.practice_attempts set mark = 'right'$q$, 'permission denied'), 'no direct update';
  assert pg_temp.fails($q$delete from public.practice_submissions$q$, 'permission denied');
  assert pg_temp.fails($q$select public.service_practice_keys('a','b','c')$q$, 'permission denied'), 'parent can not call service functions';
  assert pg_temp.fails($q$select * from public.tutor_group_practice('L1A')$q$, 'forbidden'), 'parent is not a tutor';
  assert pg_temp.fails($q$select public.admin_grant_book_access(gen_random_uuid(), 1, 'online', 'x')$q$, 'forbidden');
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','b2b2b2b2-0000-0000-0000-0000000000b2',false);
do $$ begin
  assert (select count(*) from public.practice_submissions) = 0 and (select count(*) from public.practice_attempts) = 0, 'parent B sees nothing of A';
end $$;
reset role;
create temp table ids as select id as mia from public.children where parent_id = 'a1a1a1a1-0000-0000-0000-0000000000a1';
grant all on ids to authenticated, service_role;
set role authenticated; select set_config('request.jwt.claim.sub','b2b2b2b2-0000-0000-0000-0000000000b2',false);
do $$ begin assert pg_temp.fails(format('select * from public.practice_child_detail(%L, %L)', (select mia from ids), 'hol-l1l01'), 'forbidden'), 'B can not read A child detail'; end $$;
reset role;
-- tutor of L1A: sees Mia (confirmed enrolment in that group), through RLS and the report functions; never the keys
set role authenticated; select set_config('request.jwt.claim.sub','c3c3c3c3-0000-0000-0000-0000000000c3',false);
do $$ begin
  assert (select count(*) from public.practice_submissions) = 1 and (select count(*) from public.practice_attempts) = 4, 'tutor sees the group child by RLS';
  assert (select count(*) from public.tutor_group_practice('L1A')) = 1 and (select display_name from public.tutor_group_practice('L1A')) = 'Mia';
  assert (select count(*) from public.practice_child_detail((select mia from ids), 'hol-l1l01')) = 4;
  assert (select strand from public.practice_child_detail((select mia from ids), 'hol-l1l01') where item_id = 'q3') = 'Measurement and Geometry';
  assert pg_temp.fails($q$select * from public.practice_item_keys$q$, 'permission denied'), 'tutor can not read keys';
  assert pg_temp.fails($q$select * from public.children$q$, 'permission denied');
  assert pg_temp.fails($q$select * from public.tutor_group_practice('L2A')$q$, 'forbidden'), 'not the tutor of group L2A';
end $$;
reset role;
-- tutor of another group: nothing
set role authenticated; select set_config('request.jwt.claim.sub','d4d4d4d4-0000-0000-0000-0000000000d4',false);
do $$ begin
  assert (select count(*) from public.practice_submissions) = 0 and (select count(*) from public.practice_attempts) = 0, 'other group tutor sees nothing';
  assert pg_temp.fails($q$select * from public.tutor_group_practice('L1A')$q$, 'forbidden');
  assert pg_temp.fails(format('select * from public.practice_child_detail(%L, %L)', (select mia from ids), 'hol-l1l01'), 'forbidden');
end $$;
reset role;
-- a cancelled or unpaid enrolment is not "in the group" for the tutor
update public.enrolments set status = 'pending_payment' where parent_id = 'a1a1a1a1-0000-0000-0000-0000000000a1';
set role authenticated; select set_config('request.jwt.claim.sub','c3c3c3c3-0000-0000-0000-0000000000c3',false);
do $$ begin assert (select count(*) from public.practice_submissions) = 0, 'tutor loses sight when the enrolment is not confirmed'; end $$;
reset role;
update public.enrolments set status = 'confirmed' where parent_id = 'a1a1a1a1-0000-0000-0000-0000000000a1';
-- admin sees all
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ begin assert (select count(*) from public.practice_submissions) = 1; assert (select count(*) from public.tutor_group_practice('L1A')) = 1; end $$;
-- ===== extension-only family (no enrolment, no group): parent B, children Ben and Bo. One purchase = one child. =====
set role authenticated; select set_config('request.jwt.claim.sub','b2b2b2b2-0000-0000-0000-0000000000b2',false);
do $$ begin
  perform public.add_child('Bo', 1, '5555');
  assert pg_temp.fails($q$select public.create_ext_order((select id from public.children where display_name = 'Ben' and parent_id = auth.uid()), 1, 'online')$q$, 'price_not_set'), 'no price, no order';
end $$;
reset role;
insert into public.ext_prices (product_id, amount_cents) values ('ext-l1-online', 100), ('ext-l1-both', 200), ('ext-l1-workbook', 100);   -- TEST VALUES ONLY, not real prices
set role authenticated; select set_config('request.jwt.claim.sub','b2b2b2b2-0000-0000-0000-0000000000b2',false);
do $$ declare ben uuid := (select id from public.children where display_name = 'Ben' and parent_id = auth.uid()); o uuid; begin
  assert pg_temp.fails(format('select public.create_ext_order(%L, 1, %L)', ben, 'online'), 'consents_missing'), 'online_practice consent needed to buy online';
  perform public.record_consents('{"contact":true,"terms":true,"online_practice":true}', 't2', 'p2');
  assert pg_temp.fails(format('select public.create_ext_order(%L, 1, %L)', gen_random_uuid(), 'online'), 'not_found'), 'only own child';
  assert pg_temp.fails(format('select public.create_ext_order(%L, 1, %L)', ben, 'both'), 'consents_missing'), 'delivery consent needed for a posted book';
  perform public.record_consents('{"book_delivery":true}', 't2', 'p2');
  assert pg_temp.fails(format('select public.create_ext_order(%L, 1, %L)', ben, 'both'), 'bad_address'), 'address needed';
  assert pg_temp.fails(format('select public.create_ext_order(%L, 1, %L, %L, %L, %L)', ben, 'both', 'B Parent', '1 Test Road', 'AB1234'), 'bad_address'), 'Singapore 6-digit postal code';
  o := public.create_ext_order(ben, 1, 'online');
  assert (select status from public.ext_orders where id = o) = 'pending_payment' and (select ship_status from public.ext_orders where id = o) = 'not_needed';
  assert (select product_id from public.ext_orders where id = o) = 'ext-l1-online';
  assert pg_temp.fails($q$update public.ext_orders set status = 'paid'$q$, 'permission denied'), 'parent can not mark paid';
  assert pg_temp.fails($q$insert into public.child_book_access (child_id, level, format, source) select id, 1, 'online', 'admin' from public.children$q$, 'permission denied'), 'parent can not grant access';
end $$;
reset role;
create temp table bids as select (select id from public.children where display_name = 'Ben' and parent_id = 'b2b2b2b2-0000-0000-0000-0000000000b2') as ben,
                                 (select id from public.children where display_name = 'Bo' and parent_id = 'b2b2b2b2-0000-0000-0000-0000000000b2') as bo,
                                 (select id from public.ext_orders where child_label = 'Ben') as ord;
grant all on bids to authenticated, service_role;
-- real session for Ben (needs contact + terms + online_practice: now granted); Bo has a session too
set role anon;
create temp table bentok as select * from public.child_start_session((select cb from codes), 'Ben', '4321');
create temp table botok as select * from public.child_start_session((select cb from codes), 'Bo', '5555');
reset role;
grant all on bentok, botok to service_role;
do $$ begin assert (select count(*) from bentok) = 1 and (select count(*) from botok) = 1, 'extension-only family: sessions without any enrolment or group'; end $$;
set role service_role;
do $$ declare hb text := pg_temp.h((select token from bentok)); ho text := pg_temp.h((select token from botok)); begin
  assert public.service_practice_keys(hb, 'ext-l1u01', 'v1')->>'error' = 'entitlement', 'not paid yet';
end $$;
reset role;
-- admin ticks the PayNow payment -> access for Ben only
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
select public.admin_mark_ext_order_paid((select ord from bids));
select public.admin_mark_ext_order_paid((select ord from bids));   -- idempotent
do $$ begin assert (select count(*) from public.child_book_access) = 1 and (select child_id from public.child_book_access) = (select ben from bids), 'one purchase = one access row for one child'; end $$;
reset role;
set role service_role;
do $$ declare hb text := pg_temp.h((select token from bentok)); ho text := pg_temp.h((select token from botok)); r jsonb; begin
  assert (public.service_practice_keys(hb, 'ext-l1u01', 'v1')->>'ok')::boolean, 'Ben: unit 1 of the book he has';
  assert (public.service_practice_keys(hb, 'ext-l1u02', 'v1')->>'ok')::boolean, 'Ben: the whole book (all 10 units), not one unit';
  assert public.service_practice_keys(ho, 'ext-l1u01', 'v1')->>'error' = 'entitlement', 'the purchase for Ben does NOT unlock his sibling Bo';
  assert public.service_practice_keys(hb, 'hol-l1l01', 'v1')->>'error' = 'entitlement', 'a book does not unlock the holiday/term lessons';
  r := public.service_practice_record(hb, 'ext-l1u01', 'v1', gen_random_uuid(), 1, '[{"item_id":"q1","marking_mode":"auto","mark":"right","answered":true,"answer_text":"1"}]');
  assert (r->>'ok')::boolean, r::text;
  assert public.service_practice_record(ho, 'ext-l1u01', 'v1', gen_random_uuid(), 1, '[]')->>'error' = 'entitlement', 'record is gated too';
  assert public.service_practice_record(hb, 'smp-l1u01', 'v1', gen_random_uuid(), 1, '[]')->>'error' = 'entitlement', 'open sample units are never stored';
end $$;
reset role;
-- reports without a group: parent B sees own child; tutor of L1A does not; admin overview shows has_group = false
set role authenticated; select set_config('request.jwt.claim.sub','b2b2b2b2-0000-0000-0000-0000000000b2',false);
do $$ begin
  assert (select count(*) from public.practice_submissions) = 1, 'parent sees own child submission';
  assert (select count(*) from public.practice_child_detail((select ben from bids), 'ext-l1u01')) = 1;
  assert (select count(*) from public.my_consents() where granted) >= 3;
  assert pg_temp.fails($q$select * from public.admin_practice_overview()$q$, 'forbidden');
  assert (select count(*) from public.ext_orders) = 1 and (select count(*) from public.child_book_access) = 1, 'parent sees own order and access';
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','c3c3c3c3-0000-0000-0000-0000000000c3',false);
do $$ begin assert (select count(*) from public.practice_submissions where child_id = (select ben from bids)) = 0, 'a tutor never sees a child with no group'; assert (select count(*) from public.ext_orders) = 0; end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ begin
  assert (select count(*) from public.admin_practice_overview() where display_name = 'Ben' and has_group = false) = 1, 'admin overview covers children without a group';
  assert (select count(*) from public.admin_list_ext_orders()) = 1;
end $$;
-- the funnel: trial request from the parent, counted by source, no tracking
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','b2b2b2b2-0000-0000-0000-0000000000b2',false);
do $$ declare t uuid; begin
  t := public.request_trial((select ben from bids), 1, array['weekend-morning'], 'hello', 'after_submit');
  assert pg_temp.fails($q$select public.request_trial(gen_random_uuid(), 1, '{}', null, 'book')$q$, 'not_found');
  assert pg_temp.fails($q$select public.request_trial(null, 1, '{}', null, 'bogus')$q$), 'unknown source refused';
  perform public.request_trial(null, 1, '{}', null, 'book'); perform public.request_trial(null, 1, '{}', null, 'book');
  assert pg_temp.fails($q$select public.request_trial(null, 1, '{}', null, 'book')$q$, 'too_many'), '3 requests a day at most';
  assert pg_temp.fails($q$select * from public.admin_list_trial_requests()$q$, 'forbidden');
  assert pg_temp.fails($q$select public.admin_funnel_counts()$q$, 'forbidden');
  assert (select count(*) from public.trial_requests) = 3, 'parent sees own requests';
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ declare f jsonb; begin
  perform public.admin_set_trial_status((select id from public.trial_requests where source = 'after_submit'), 'attended');
  f := public.admin_funnel_counts();
  assert (f->>'books_paid')::int = 1 and (f->>'children_started')::int = 1 and (f->>'trial_requests')::int = 3 and (f->>'trial_attended')::int = 1, f::text;
  assert (f->'trial_by_source'->>'book')::int = 2, f::text;
end $$;
reset role;
-- shipping: a workbook order needs the address; the address is cleared 30 days after delivery
set role authenticated; select set_config('request.jwt.claim.sub','b2b2b2b2-0000-0000-0000-0000000000b2',false);
create temp table wo as select public.create_ext_order((select bo from bids), 1, 'workbook', 'B Parent', '1 Test Road #01-01', '123456', '81234567') as id;
reset role;
grant all on wo to authenticated;
do $$ begin assert (select ship_status from public.ext_orders where id = (select id from wo)) = 'to_ship'; end $$;
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
select public.admin_mark_ext_order_paid((select id from wo));
select public.admin_set_ship_status((select id from wo), 'delivered');
do $$ begin assert public.admin_clear_delivered_addresses() = 0, 'not before 30 days'; end $$;
reset role;
update public.ext_orders set delivered_at = now() - interval '31 days' where id = (select id from wo);
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ begin assert public.admin_clear_delivered_addresses() = 1; assert (select ship_address from public.ext_orders where id = (select id from wo)) is null, 'address cleared'; end $$;
-- a workbook-only purchase gives NO online access
do $$ begin assert (select count(*) from public.child_book_access where format = 'workbook') = 1; end $$;
reset role;
set role service_role;
do $$ begin assert public.service_practice_keys(pg_temp.h((select token from botok)), 'ext-l1u01', 'v1')->>'error' = 'entitlement', 'workbook-only format does not open the online practice'; end $$;
reset role;
-- refund: access revoked at once, past answers stay until retention removes them
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
select public.admin_refund_ext_order((select ord from bids));
reset role;
set role service_role;
do $$ begin assert public.service_practice_keys(pg_temp.h((select token from bentok)), 'ext-l1u01', 'v1')->>'error' = 'entitlement', 'refund revokes online access'; end $$;
reset role;
do $$ begin assert (select status from public.child_book_access where order_id = (select ord from bids)) = 'refunded'; assert (select count(*) from public.practice_submissions where child_id = (select ben from bids)) = 1, 'answers stay after refund'; end $$;
update public.practice_submissions set received_at = now() - interval '100 days' where child_id = (select ben from bids);
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ declare pn int := public.admin_purge_expired_practice(); begin raise notice 'purged %', pn; assert pn = 1 and (select count(*) from public.practice_submissions where child_id = (select ben from bids)) = 0, '90 days after access ended: answers deleted'; end $$;
-- manual admin grant (free) for a child
select public.admin_grant_book_access((select bo from bids), 1, 'online', 'prize');
reset role;
set role service_role;
do $$ begin assert (public.service_practice_keys(pg_temp.h((select token from botok)), 'ext-l1u01', 'v1')->>'ok')::boolean, 'admin grant opens it'; end $$;
reset role;

-- ===== consent withdrawn: no more submissions at once =====
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
select public.record_consents('{"online_practice":false}', 't2', 'p2');
reset role;
set role service_role;
do $$ declare th text := pg_temp.h((select token from tok)); begin
  assert public.service_practice_keys(th, 'hol-l1l01', 'v1')->>'error' = 'consent';
  assert public.service_practice_record(th, 'hol-l1l01', 'v1', gen_random_uuid(), 1, '[]')->>'error' = 'consent';
end $$;
reset role;
-- parent deletes the practice answers of one child (account stays); the sessions go too
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
do $$ begin
  assert public.delete_child_practice((select mia from ids)) = 1;
  assert pg_temp.fails(format('select public.delete_child_practice(%L)', gen_random_uuid()), 'not_found');
end $$;
reset role;
do $$ begin assert (select count(*) from public.practice_attempts) = 0 and (select count(*) from public.child_sessions where child_id = (select mia from ids)) = 0, 'answers and sessions deleted'; end $$;
-- deleting the whole account removes everything through the existing cascade
insert into public.practice_submissions (child_id, unit_key, unit_version, client_sid) values ((select mia from ids), 'hol-l1l01', 'v1', gen_random_uuid());
update public.practice_submissions set received_at = now() - interval '13 months';
set role authenticated; select set_config('request.jwt.claim.sub','e5e5e5e5-0000-0000-0000-0000000000e5',false);
do $$ begin assert public.admin_purge_expired_practice() = 1, '12 month retention purge'; end $$;
reset role;
insert into public.practice_submissions (child_id, unit_key, unit_version, client_sid) values ((select mia from ids), 'hol-l1l01', 'v1', gen_random_uuid());
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
select public.delete_my_data();
reset role;
do $$ begin assert (select count(*) from public.practice_submissions) = 0 and (select count(*) from public.child_sessions where child_id = (select mia from ids)) = 0, 'delete_my_data removes the children, so their practice data and sessions go through the cascade (entitlements stay, like payment records: a purchase, no personal data)'; end $$;
select 'practice_submissions_test: all assertions passed' as result;
