-- Assertions for schema.sql + policies.sql. Run via run_sql_test.sh. Any failed assertion raises and stops psql (ON_ERROR_STOP).
\set ON_ERROR_STOP on
create or replace function pg_temp.fails(sql text, expect text default null) returns boolean language plpgsql as $$
begin execute sql; return false;
exception when others then
  if expect is not null and sqlerrm not like '%'||expect||'%' then raise exception 'wrong error for [%]: got [%], wanted [%]', sql, sqlerrm, expect; end if;
  return true; end $$;

insert into auth.users (id, email, raw_user_meta_data) values
 ('aaaaaaaa-0000-0000-0000-000000000001','pa@example.com','{"full_name":"Parent A"}'),
 ('bbbbbbbb-0000-0000-0000-000000000002','pb@example.com','{}'),
 ('cccccccc-0000-0000-0000-000000000003','owner@example.com','{}');
insert into public.admins (user_id) values ('cccccccc-0000-0000-0000-000000000003');
do $$ begin assert (select count(*) from public.parents) = 3, 'parents rows created by trigger'; end $$;
do $$ begin assert (select count(*) from public.groups) = 6, 'groups seeded'; end $$;

-- ===== parent A =====
set role authenticated; select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-000000000001',false);
do $$ declare c1 uuid; c2 uuid; e uuid; n int; begin
  assert (select count(*) from public.parents) = 1, 'A sees only own parent row';
  c1 := public.add_child('Mia', 1, '1234');
  c2 := public.add_child('Ben', 3, '4321');
  assert (select count(*) from public.children) = 2;
  assert pg_temp.fails($q$select pin_hash from public.children$q$, 'permission denied'), 'pin_hash not selectable';
  assert pg_temp.fails($q$select pin_failed from public.children$q$, 'permission denied');
  assert pg_temp.fails($q$select * from public.children$q$, 'permission denied'), 'select * denied (must list columns)';
  assert pg_temp.fails($q$insert into public.children (parent_id,display_name,level,pin_hash) values (auth.uid(),'X',1,'plain')$q$, 'permission denied'), 'no direct child insert';
  assert pg_temp.fails($q$update public.children set level=2$q$, 'permission denied');
  assert pg_temp.fails($q$select public.add_child('Z', 1, 'abcd')$q$, 'pin_format');
  assert pg_temp.fails($q$select public.add_child('Z', 1, '12')$q$, 'pin_format');
  assert pg_temp.fails($q$select public.add_child('mia', 1, '1111')$q$), 'duplicate name per family';
  -- enrolling needs consents first
  assert pg_temp.fails(format('select public.enrol_child(%L,%L)', c1, 'L1A'), 'consents_missing');
  perform public.record_consents('{"contact":true,"terms":true,"recording":true,"childs_work":true,"feedback_quotes":false}', 'terms-v1', 'privacy-v1');
  assert (select count(*) from public.my_consents()) = 5;
  assert (select granted from public.my_consents() where consent_type='feedback_quotes') = false;
  assert pg_temp.fails($q$select public.record_consents('{"bogus":true}', 'a', 'b')$q$, 'bad_consent_type');
  assert pg_temp.fails($q$update public.consents set granted=false$q$, 'permission denied');
  assert pg_temp.fails(format('select public.enrol_child(%L,%L)', c1, 'L2A'), 'level_mismatch');
  e := public.enrol_child(c1, 'L1A');
  assert pg_temp.fails(format('select public.enrol_child(%L,%L)', c1, 'L1A'), 'already_enrolled');
  assert (select payment_status from public.my_enrolments() where enrolment_id = e) = 'pending';
  assert (select payment_reference from public.my_enrolments() where enrolment_id = e) ~ '^MI-[A-Z2-9]{6}$';
  assert (select amount_cents from public.my_enrolments() where enrolment_id = e) = 25000;
  assert pg_temp.fails($q$update public.payments set status='paid'$q$, 'permission denied'), 'parent cannot mark paid';
  assert pg_temp.fails($q$select public.admin_mark_paid(gen_random_uuid())$q$, 'forbidden');
  assert pg_temp.fails($q$select * from public.admin_list_enrolments()$q$, 'forbidden');
  assert pg_temp.fails($q$select * from public.admins$q$, 'permission denied');
  assert pg_temp.fails(format('select public.update_child(%L,%L,%s)', c1, 'Mia', 2), 'level_locked_by_enrolment');
  assert pg_temp.fails(format('select public.delete_child(%L)', c1), 'cancel_enrolment_first');
  perform set_config('t.c1', c1::text, false); perform set_config('t.e1', e::text, false);
  -- withdraw a required consent -> cannot enrol the other child
  perform public.record_consents('{"recording":false}', 'terms-v1', 'privacy-v1');
  assert pg_temp.fails(format('select public.enrol_child(%L,%L)', c2, 'L3A'), 'consents_missing:recording');
  perform public.record_consents('{"recording":true}', 'terms-v1', 'privacy-v1');
  assert (select count(*) from public.consents) = 7, 'append only history kept';
  update public.parents set full_name = 'Parent A2';
  assert pg_temp.fails($q$update public.parents set family_code='AAAAAA'$q$, 'permission denied');
end $$;
reset role;

-- ===== parent B must not see A's anything =====
set role authenticated; select set_config('request.jwt.claim.sub','bbbbbbbb-0000-0000-0000-000000000002',false);
do $$ declare a_child uuid := current_setting('t.c1')::uuid; begin
  assert (select count(*) from public.parents) = 1;
  assert (select count(*) from public.children) = 0;
  assert (select count(*) from public.enrolments) = 0;
  assert (select count(*) from public.payments) = 0;
  assert (select count(*) from public.consents) = 0;
  assert (select count(*) from public.my_enrolments()) = 0;
  assert pg_temp.fails(format('select public.update_child(%L,%L,1)', a_child, 'Hacked'), 'not_found');
  assert pg_temp.fails(format('select public.delete_child(%L)', a_child), 'not_found');
  assert pg_temp.fails(format('select public.enrol_child(%L,%L)', a_child, 'L1A'), 'not_found');
  assert (select taken from public.group_fill() where group_id='L1A') = 1, 'fill visible to all, counts only';
  update public.parents set full_name='B';  -- only own row
  assert (select count(*) from public.parents where full_name='B') = 1;
end $$;
reset role;
do $$ begin assert (select full_name from public.parents where id='aaaaaaaa-0000-0000-0000-000000000001') = 'Parent A2'; end $$;

-- ===== anon =====
set role anon; select set_config('request.jwt.claim.sub','',false);
do $$ begin
  assert (select count(*) from public.groups) = 6, 'anon reads groups';
  assert pg_temp.fails($q$select * from public.parents$q$, 'permission denied');
  assert pg_temp.fails($q$select count(*) from public.payments$q$, 'permission denied');
  assert pg_temp.fails($q$select public.add_child('x',1,'1234')$q$, 'permission denied');
  assert pg_temp.fails($q$select * from public.my_enrolments()$q$, 'permission denied');
  assert pg_temp.fails($q$select * from public.group_fill()$q$, 'permission denied');
end $$;

-- ===== child sign-in (anon callable) =====
do $$ declare fc text; begin
  reset role; select family_code into fc from public.parents where id='aaaaaaaa-0000-0000-0000-000000000001'; perform set_config('t.fc', fc, false);
end $$;
set role anon;
do $$ declare fc text := current_setting('t.fc'); i int; begin
  assert (select count(*) from public.child_sign_in(fc, 'mia', '1234')) = 1, 'good pin, case-insensitive name';
  assert (select count(*) from public.child_sign_in(lower(fc), ' Mia ', '1234')) = 1;
  assert (select count(*) from public.child_sign_in(fc, 'Mia', '9999')) = 0;
  assert (select count(*) from public.child_sign_in('ZZZZZZ', 'Mia', '1234')) = 0;
  assert (select count(*) from public.child_sign_in(fc, 'Nobody', '1234')) = 0;
  for i in 1..5 loop perform * from public.child_sign_in(fc, 'Ben', '0000'); end loop;
  assert (select count(*) from public.child_sign_in(fc, 'Ben', '4321')) = 0, 'locked after 5 failures even with right PIN';
end $$;
reset role;
do $$ begin
  assert (select pin_hash from public.children where display_name='Mia') like '$2%', 'bcrypt hash stored';
  assert (select count(*) from public.children where pin_hash in ('1234','4321')) = 0, 'no plaintext pin';
  update public.children set pin_locked_until = now() - interval '1 minute' where display_name='Ben';
end $$;
set role anon;
do $$ begin assert (select count(*) from public.child_sign_in(current_setting('t.fc'), 'Ben', '4321')) = 1, 'lock expires'; end $$;
reset role;

-- ===== capacity =====
do $$ declare i int; pid uuid; cid uuid; begin
  for i in 1..7 loop   -- 1 seat already used by Mia; fill remaining 7
    insert into auth.users (id, email) values (gen_random_uuid(), 'f'||i||'@x.com') returning id into pid;
    perform set_config('request.jwt.claim.sub', pid::text, false);
    set local role authenticated;
    cid := public.add_child('K'||i, 1, '1234');
    perform public.record_consents('{"contact":true,"terms":true,"recording":true,"childs_work":true}', 'v', 'v');
    perform public.enrol_child(cid, 'L1A');
    reset role;
  end loop;
  assert (select count(*) from public.enrolments where group_id='L1A') = 8;
  insert into auth.users (id, email) values ('dddddddd-0000-0000-0000-000000000004', 'late@x.com');
  perform set_config('request.jwt.claim.sub', 'dddddddd-0000-0000-0000-000000000004', false);
  set local role authenticated;
  cid := public.add_child('Late', 1, '1234');
  perform public.record_consents('{"contact":true,"terms":true,"recording":true,"childs_work":true}', 'v', 'v');
  assert pg_temp.fails(format('select public.enrol_child(%L,%L)', cid, 'L1A'), 'group_full'), 'ninth is refused';
  reset role;
end $$;

-- ===== admin =====
set role authenticated; select set_config('request.jwt.claim.sub','cccccccc-0000-0000-0000-000000000003',false);
do $$ declare pid uuid; begin
  assert public.is_admin();
  assert (select count(*) from public.admin_list_enrolments()) = 8;
  select payment_id into pid from public.admin_list_enrolments() where child_name = 'Mia';
  perform public.admin_mark_paid(pid, 'PayNow 22 Oct');
  perform public.admin_mark_paid(pid, 'again');   -- idempotent
  assert (select payment_status from public.admin_list_enrolments() where child_name='Mia') = 'paid';
  assert (select enrolment_status from public.admin_list_enrolments() where child_name='Mia') = 'confirmed';
  assert (select marked_by from public.payments where id = pid) = 'cccccccc-0000-0000-0000-000000000003';
  assert (select count(*) from public.children) >= 9, 'admin can read children (no pin hash)';
  assert pg_temp.fails($q$select pin_hash from public.children$q$, 'permission denied');
end $$;
reset role;

-- ===== service role / Stripe =====
set role service_role;
do $$ declare e uuid; p uuid; begin
  select id into e from public.enrolments where child_label = 'K1';
  assert (select amount_cents from public.service_begin_payment(e, (select parent_id from public.enrolments where id=e))) = 25000;
  assert (select group_fee_cents from public.service_begin_payment(e, (select parent_id from public.enrolments where id=e))) = 25000;
  assert (select count(*) from public.service_begin_payment(e, 'aaaaaaaa-0000-0000-0000-000000000001')) = 0, 'wrong parent sees nothing';
  select payment_id into p from public.service_begin_payment(e, (select parent_id from public.enrolments where id=e));
  perform public.service_attach_session(p, 'cs_test_1');
  assert (select method from public.payments where id = p) = 'stripe' and (select provider_ref from public.payments where id = p) = 'cs_test_1';
  -- expired session: stays pending, reference cleared, attempt bumped; a stale/other session id is ignored
  assert public.service_mark_session_failed(p, 'cs_other') = 'ignored';
  assert public.service_mark_session_failed(p, 'cs_test_1') = 'reset';
  assert (select provider_attempt from public.payments where id = p) = 1 and (select status from public.payments where id = p) = 'pending';
  assert public.service_mark_session_failed(p, 'cs_test_1') = 'ignored', 'second expiry event is harmless';
  perform public.service_attach_session(p, 'cs_test_2');
  assert public.service_mark_paid(p, 'cs_test_2', 'pi_1', 100, 'sgd') = 'amount_mismatch';
  assert public.service_mark_paid(p, 'cs_test_2', 'pi_1', 25000, 'usd') = 'currency_mismatch';
  assert (select status from public.payments where id = p) = 'pending', 'mismatches change nothing';
  assert public.service_mark_paid(p, 'cs_test_2', 'pi_1', 25000, 'sgd') = 'paid';
  assert public.service_mark_paid(p, 'cs_test_2', 'pi_1', 25000, 'sgd') = 'already_paid';
  assert (select status from public.enrolments where id = e) = 'confirmed';
  assert (select provider_payment_ref from public.payments where id = p) = 'pi_1';
  assert public.service_mark_session_failed(p, 'cs_test_2') = 'ignored', 'paid payment is never reset';
  assert public.service_mark_paid(gen_random_uuid(), 'x', 'y', 25000, 'sgd') = 'not_found';
end $$;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','bbbbbbbb-0000-0000-0000-000000000002',false);
do $$ begin
  assert pg_temp.fails($q$select public.service_mark_paid(gen_random_uuid(),'x','y',1,'sgd')$q$, 'permission denied'), 'parents cannot call service fns';
  assert pg_temp.fails($q$select * from public.service_begin_payment(gen_random_uuid(), auth.uid())$q$, 'permission denied');
  assert pg_temp.fails($q$select public.service_attach_session(gen_random_uuid(),'x')$q$, 'permission denied');
  assert pg_temp.fails($q$select public.service_mark_session_failed(gen_random_uuid(),'x')$q$, 'permission denied');
end $$;
reset role;
set role anon;
do $$ begin
  assert pg_temp.fails($q$select public.service_mark_paid(gen_random_uuid(),'x','y',1,'sgd')$q$, 'permission denied'), 'anon cannot call service fns';
end $$;
reset role;

-- ===== cancel + delete my data =====
set role authenticated; select set_config('request.jwt.claim.sub','bbbbbbbb-0000-0000-0000-000000000002',false);
do $$ begin perform public.add_child('Zed', 2, '5555'); perform public.delete_my_data(); end $$;
reset role;
do $$ begin
  assert not exists (select 1 from auth.users where id='bbbbbbbb-0000-0000-0000-000000000002'), 'login deleted';
  assert (select email is null and full_name is null and deleted_at is not null from public.parents where id='bbbbbbbb-0000-0000-0000-000000000002'), 'pii stripped';
  assert not exists (select 1 from public.children where parent_id='bbbbbbbb-0000-0000-0000-000000000002');
  assert (select count(*) from public.deletion_requests) = 1;
end $$;
-- parent A: cancel unpaid enrolment of a K child is not A's; use A's Ben
set role authenticated; select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-000000000001',false);
do $$ declare ben uuid; e uuid; begin
  select id into ben from public.children where display_name='Ben';
  e := public.enrol_child(ben, 'L3A');
  perform public.cancel_my_enrolment(e);
  assert (select taken from public.group_fill() where group_id='L3A') = 0, 'cancel frees the seat';
  assert pg_temp.fails(format('select public.cancel_my_enrolment(%L)', current_setting('t.e1')::uuid), 'cannot_cancel_contact_us'), 'paid enrolment: contact us';
  perform public.delete_child(ben);
end $$;
reset role;
select 'ALL SQL TESTS PASSED' as result;
