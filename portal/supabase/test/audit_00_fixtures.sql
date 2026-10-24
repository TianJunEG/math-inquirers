-- AUDIT fixtures (round 1). Loaded first by audit_run.sh. Local throwaway Postgres only. All data is fake.
\set ON_ERROR_STOP on
reset role;
insert into auth.users (id, email) values
 ('aaaaaaaa-0000-0000-0000-00000000000a','pa@audit.test'), ('bbbbbbbb-0000-0000-0000-00000000000b','pb@audit.test'),
 ('cccccccc-0000-0000-0000-00000000000c','t1@audit.test'), ('dddddddd-0000-0000-0000-00000000000d','t2@audit.test'),
 ('eeeeeeee-0000-0000-0000-00000000000e','adm@audit.test'), ('ffffffff-0000-0000-0000-00000000000f','px@audit.test');
insert into public.admins (user_id) values ('eeeeeeee-0000-0000-0000-00000000000e');
insert into public.tutors (user_id, note) values ('cccccccc-0000-0000-0000-00000000000c','T1'), ('dddddddd-0000-0000-0000-00000000000d','T2');
insert into public.tutor_groups values ('cccccccc-0000-0000-0000-00000000000c','L1A'), ('dddddddd-0000-0000-0000-00000000000d','L2A');

insert into public.practice_units (unit_key, unit_version, product, level, title, unit_no, access, published) values
 ('hol-l1l01','v1','holiday',1,'Holiday L1 lesson 1',1,'enrolled',true), ('ext-l1u01','v1','extension',1,'Ext L1 U1',1,'purchased',true),
 ('ext-l1u02','v1','extension',1,'Ext L1 U2',2,'purchased',true), ('ext-l2u01','v1','extension',2,'Ext L2 U1',1,'purchased',true),
 ('smp-l1u01','v1','extension',1,'Sample',1,'open',true), ('ext-l1u03','v1','extension',1,'Unpublished',3,'purchased',false);
insert into public.practice_item_tags (unit_key, unit_version, item_id, position, marking_mode, strand, skill, slips) values
 ('hol-l1l01','v1','q1',1,'auto','Whole Numbers','Place value','[{"a":[7],"say":"7 is 3 + 4. Count the tens first."}]'),
 ('hol-l1l01','v1','q2',2,'auto','Whole Numbers','Skip counting','[]'), ('hol-l1l01','v1','q3',3,'self','Geometry','Draw a line','[]'),
 ('ext-l1u01','v1','q1',1,'auto','Whole Numbers','x','[]'), ('ext-l1u02','v1','q1',1,'auto','Whole Numbers','x','[]'),
 ('ext-l2u01','v1','q1',1,'auto','Whole Numbers','x','[]'), ('smp-l1u01','v1','q1',1,'auto','Whole Numbers','x','[]'), ('ext-l1u03','v1','q1',1,'auto','Whole Numbers','x','[]');
insert into public.practice_item_keys (unit_key, unit_version, item_id, answer_type, answer_key) values
 ('hol-l1l01','v1','q1','number','"SECRET-ANSWER-9"'), ('hol-l1l01','v1','q2','number','20'), ('hol-l1l01','v1','q3','selfcheck',null),
 ('ext-l1u01','v1','q1','number','1'), ('ext-l1u02','v1','q1','number','1'), ('ext-l2u01','v1','q1','number','1'), ('smp-l1u01','v1','q1','number','1'), ('ext-l1u03','v1','q1','number','1');
insert into public.ext_prices (product_id, amount_cents) values ('ext-l1-online', 1000), ('ext-l1-both', 2000), ('ext-l1-workbook', 1500), ('ext-l2-online', 1000);
-- TEST VALUES ONLY, not real prices.

set role authenticated; select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-00000000000a',false);
do $$ declare c uuid; k uuid; begin
  c := public.add_child('Mia', 1, '7391'); k := public.add_child('Kai', 1, '2468');
  perform public.record_consents('{"contact":true,"terms":true,"recording":true,"childs_work":true,"online_practice":true,"book_delivery":true}', 't1', 'p1');
  perform public.enrol_child(c, 'L1A');
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','bbbbbbbb-0000-0000-0000-00000000000b',false);
do $$ begin
  perform public.add_child('Ben', 1, '9152'); perform public.add_child('Zoe', 2, '1357');
  perform public.record_consents('{"contact":true,"terms":true,"online_practice":true,"book_delivery":true}', 't1', 'p1');
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','eeeeeeee-0000-0000-0000-00000000000e',false);
select public.admin_mark_paid((select p.id from public.payments p join public.enrolments e on e.id = p.enrolment_id where e.parent_id = 'aaaaaaaa-0000-0000-0000-00000000000a'));
reset role;

-- shared helpers are re-created per file (pg_temp is per session); keep this file to data only
create table public.audit_ctx as select
  (select family_code from public.parents where email='pa@audit.test') as code_a, (select family_code from public.parents where email='pb@audit.test') as code_b,
  (select id from public.children where display_name='Mia') as mia, (select id from public.children where display_name='Kai') as kai,
  (select id from public.children where display_name='Ben') as ben, (select id from public.children where display_name='Zoe') as zoe;
grant select on public.audit_ctx to anon, authenticated, service_role;   -- fake ids, lets the attack scripts name children while running as an API role
