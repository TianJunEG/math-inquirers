-- AUDIT 02: cross-family isolation, tutor scope, privilege escalation, anon access. Local throwaway Postgres only.
\set ON_ERROR_STOP on
\i :HERE/audit_lib.sql
reset role;
\set A 'aaaaaaaa-0000-0000-0000-00000000000a'
\set B 'bbbbbbbb-0000-0000-0000-00000000000b'
\set T1 'cccccccc-0000-0000-0000-00000000000c'
\set T2 'dddddddd-0000-0000-0000-00000000000d'
\set ADM 'eeeeeeee-0000-0000-0000-00000000000e'
\set X 'ffffffff-0000-0000-0000-00000000000f'

-- seed: a submission each for Mia (A) and Ben (B), an order each, a trial request each (done as the service/definer paths, not by the attacker)
select set_config('audit.mia', (select mia::text from public.audit_ctx), false), set_config('audit.ben', (select ben::text from public.audit_ctx), false),
       set_config('audit.kai', (select kai::text from public.audit_ctx), false), set_config('audit.zoe', (select zoe::text from public.audit_ctx), false);
select 'x' from (select 1) z where false;
-- sessions + submissions
do $$ declare m uuid := current_setting('audit.mia')::uuid; b uuid := current_setting('audit.ben')::uuid; rows jsonb; begin
  perform 1;
  -- Mia: enrolled -> holiday unit; Ben: B has no group, give B an online book via admin so B can submit an extension unit
  insert into public.child_book_access (child_id, level, format, source, source_note) values (b, 1, 'online', 'admin', 'audit fixture');
  insert into public.child_sessions (child_id, token_hash, expires_at) values
    (m, encode(extensions.digest('MIATOKEN_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','sha256'),'hex'), now() + interval '4 hours'),
    (b, encode(extensions.digest('BENTOKEN_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb','sha256'),'hex'), now() + interval '4 hours');
  rows := '[{"item_id":"q1","marking_mode":"auto","mark":"wrong","answered":true,"answer_text":"7","slip_idx":0},{"item_id":"q2","marking_mode":"auto","mark":"right","answered":true,"answer_text":"20"},{"item_id":"q3","marking_mode":"self","mark":"self","answered":true,"self_result":"got"}]';
  perform public.service_practice_record(encode(extensions.digest('MIATOKEN_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','sha256'),'hex'),'hol-l1l01','v1',gen_random_uuid(),1,rows);
  perform public.service_practice_record(encode(extensions.digest('BENTOKEN_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb','sha256'),'hex'),'ext-l1u01','v1',gen_random_uuid(),1,'[{"item_id":"q1","marking_mode":"auto","mark":"right","answered":true,"answer_text":"1"}]');
end $$;
-- orders: A orders a workbook for Mia; B orders online for Ben (both pending)
set role authenticated; select set_config('request.jwt.claim.sub',:'A',false);
select public.create_ext_order((select mia from public.audit_ctx), 1, 'workbook', 'Pa Parent', '1 Audit Road #01-01', '123456', '91234567');
reset role;
set role authenticated; select set_config('request.jwt.claim.sub',:'B',false);
select public.create_ext_order((select zoe from public.audit_ctx), 2, 'online');
select public.request_trial((select zoe from public.audit_ctx), 2, array['weekday-evening'], 'B private note', 'other');
reset role;
set role authenticated; select set_config('request.jwt.claim.sub',:'A',false);
select public.request_trial(null, 1, array['weekend-morning'], 'A note', 'other');
reset role;

-- ===== A tries to read B (direct table reads under RLS) =====
do $$ declare bad text := ''; begin
  -- count rows A can see that belong to B, by joining on B's identity
  if (select pg_temp.val('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select count(*) from public.children where parent_id = 'bbbbbbbb-0000-0000-0000-00000000000b'$q$)) <> '0' then bad := bad || 'children '; end if;
  if (select pg_temp.val('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select count(*) from public.ext_orders where parent_id = 'bbbbbbbb-0000-0000-0000-00000000000b'$q$)) <> '0' then bad := bad || 'ext_orders '; end if;
  if (select pg_temp.val('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select count(*) from public.trial_requests where parent_id = 'bbbbbbbb-0000-0000-0000-00000000000b'$q$)) <> '0' then bad := bad || 'trial_requests '; end if;
  if (select pg_temp.val('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select count(*) from public.consents where parent_id = 'bbbbbbbb-0000-0000-0000-00000000000b'$q$)) <> '0' then bad := bad || 'consents '; end if;
  if (select pg_temp.val('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select count(*) from public.child_book_access a join public.children c on c.id=a.child_id where c.parent_id = 'bbbbbbbb-0000-0000-0000-00000000000b'$q$)) <> '0' then bad := bad || 'child_book_access '; end if;
  if (select pg_temp.val('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select count(*) from public.practice_submissions s join public.children c on c.id=s.child_id where c.parent_id = 'bbbbbbbb-0000-0000-0000-00000000000b'$q$)) <> '0' then bad := bad || 'practice_submissions '; end if;
  if (select pg_temp.val('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select count(*) from public.practice_attempts where child_id = (select ben from public.audit_ctx)$q$)) like 'err%' then null; end if;
  if (select pg_temp.val('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select count(*) from public.parents where id = 'bbbbbbbb-0000-0000-0000-00000000000b'$q$)) <> '0' then bad := bad || 'parents '; end if;
  perform pg_temp.chk('parent A cannot read parent B rows (children, orders, trials, consents, access, submissions, parents)', bad = '', 'High', bad);
end $$;
select pg_temp.chk('parent A sees own order and own order only', pg_temp.val('authenticated',:'A','select count(*) from public.ext_orders') = '1', 'High');
-- A calls functions with B's child ids
select pg_temp.chk('A: practice_child_detail(Ben) forbidden', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select * from public.practice_child_detail((select ben from public.audit_ctx),'ext-l1u01')$q$)), 'High');
select pg_temp.chk('A: delete_child_practice(Ben) not_found', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.delete_child_practice((select ben from public.audit_ctx))$q$)), 'High');
select pg_temp.chk('A: create_ext_order for Ben not_found', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select ben from public.audit_ctx),1,'online')$q$)), 'High');
select pg_temp.chk('A: update_child_birth_year(Ben) not_found', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.update_child_birth_year((select ben from public.audit_ctx),2018)$q$)), 'High');
select pg_temp.chk('A: update_child(Ben) not_found', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.update_child((select ben from public.audit_ctx),'Pwned',1,'8264')$q$)), 'High');
select pg_temp.chk('A: delete_child(Ben) not_found', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.delete_child((select ben from public.audit_ctx))$q$)), 'High');
select pg_temp.chk('A: enrol_child(Ben) not_found', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.enrol_child((select ben from public.audit_ctx),'L1A')$q$)), 'High');
select pg_temp.chk('A: request_trial(Ben) not_found', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.request_trial((select ben from public.audit_ctx),1,'{}','x','other')$q$)), 'High');
select id as b_order from public.ext_orders where parent_id='bbbbbbbb-0000-0000-0000-00000000000b' \gset
select id as b_trial from public.trial_requests where parent_id='bbbbbbbb-0000-0000-0000-00000000000b' \gset
select pg_temp.as_('authenticated',:'A',format($q$select public.cancel_my_ext_order(%L)$q$, :'b_order')) as r \gset
select pg_temp.chk('A: cancel B''s order is refused and B''s order stays pending', pg_temp.denied(:'r') and (select status from public.ext_orders where id=:'b_order') = 'pending_payment', 'High', :'r');
select pg_temp.as_('authenticated',:'A',format($q$select public.withdraw_trial_request(%L)$q$, :'b_trial')) as r \gset
select pg_temp.chk('A: withdraw B''s trial request has no effect', (select status from public.trial_requests where id=:'b_trial') = 'new', 'High', :'r');
select pg_temp.as_('authenticated',:'A',format($q$select * from public.practice_child_detail(%L,'ext-l1u01')$q$, (select ben from public.audit_ctx))) as r \gset
select pg_temp.chk('A: practice_child_detail(Ben) with the real unit is forbidden', pg_temp.denied(:'r') and :'r' like '%forbidden%', 'High', :'r');
select pg_temp.chk('A: my_children_progress shows only A''s children', pg_temp.val('authenticated',:'A',$q$select count(*) from public.my_children_progress() where child_id <> (select mia from public.audit_ctx)$q$) = '0', 'High');
select pg_temp.chk('A: my_children_access shows only A''s children', pg_temp.val('authenticated',:'A',$q$select count(*) from public.my_children_access() where child_id not in ((select mia from public.audit_ctx),(select kai from public.audit_ctx))$q$) = '0', 'High');
select pg_temp.chk('A: my_children_units shows only A''s children', pg_temp.val('authenticated',:'A',$q$select count(*) from public.my_children_units() where child_id not in ((select mia from public.audit_ctx),(select kai from public.audit_ctx))$q$) = '0', 'High');

-- ===== privilege escalation =====
select pg_temp.chk('parent cannot UPDATE parents.family_code', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$update public.parents set family_code='HACKED' where id='aaaaaaaa-0000-0000-0000-00000000000a'$q$)), 'High');
select pg_temp.chk('parent cannot UPDATE B''s parents row (RLS: 0 rows)', pg_temp.zero(pg_temp.as_('authenticated',:'A',$q$update public.parents set full_name='x' where id='bbbbbbbb-0000-0000-0000-00000000000b'$q$)), 'High');
select pg_temp.chk('parent cannot INSERT into admins', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$insert into public.admins(user_id) values ('aaaaaaaa-0000-0000-0000-00000000000a')$q$)), 'High');
select pg_temp.chk('parent cannot INSERT into tutor_groups / tutors', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$insert into public.tutor_groups values ('aaaaaaaa-0000-0000-0000-00000000000a','L1A')$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$insert into public.tutors(user_id) values ('aaaaaaaa-0000-0000-0000-00000000000a')$q$)), 'High');
select pg_temp.chk('parent cannot UPDATE ext_orders.status / amount', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$update public.ext_orders set status='paid'$q$)), 'High');
select pg_temp.chk('parent cannot INSERT child_book_access (self-grant)', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$insert into public.child_book_access(child_id,level,format,source) values ((select kai from public.audit_ctx),1,'online','admin')$q$)), 'High');
select pg_temp.chk('parent cannot INSERT enrolments / payments / consents directly', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$insert into public.consents(parent_id,consent_type,granted,terms_version,privacy_version) values ('aaaaaaaa-0000-0000-0000-00000000000a','terms',true,'x','y')$q$)), 'High');
select pg_temp.chk('parent cannot UPDATE children (pin_hash, birth_year, level) directly', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$update public.children set level=6 where parent_id='aaaaaaaa-0000-0000-0000-00000000000a'$q$)), 'High');
select pg_temp.chk('parent cannot UPDATE practice_attempts / submissions (forge marks)', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$update public.practice_attempts set correct=true$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$update public.practice_submissions set n_right=99$q$)), 'High');
select pg_temp.chk('parent cannot DELETE consents (append-only; no grant)', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$delete from public.consents$q$)), 'High');
select pg_temp.chk('parent cannot call admin_mark_ext_order_paid', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.admin_mark_ext_order_paid((select id from public.ext_orders limit 1))$q$)), 'High');
select pg_temp.chk('parent cannot call admin_grant_book_access', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.admin_grant_book_access((select kai from public.audit_ctx),1,'both','hax')$q$)), 'High');
select pg_temp.chk('parent cannot call admin_set_ext_price', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.admin_set_ext_price('ext-l1-online',1)$q$)), 'High');
select pg_temp.chk('parent cannot call admin_list_children / orders / trials / funnel / overview',
  pg_temp.denied(pg_temp.as_('authenticated',:'A','select * from public.admin_list_children()')) and pg_temp.denied(pg_temp.as_('authenticated',:'A','select * from public.admin_list_ext_orders()'))
  and pg_temp.denied(pg_temp.as_('authenticated',:'A','select * from public.admin_list_trial_requests()')) and pg_temp.denied(pg_temp.as_('authenticated',:'A','select public.admin_funnel_counts()'))
  and pg_temp.denied(pg_temp.as_('authenticated',:'A','select * from public.admin_practice_overview()')) and pg_temp.denied(pg_temp.as_('authenticated',:'A','select * from public.admin_list_book_access()')), 'High');
select pg_temp.chk('parent cannot call admin purge / clear functions', pg_temp.denied(pg_temp.as_('authenticated',:'A','select public.admin_purge_expired_practice()')) and pg_temp.denied(pg_temp.as_('authenticated',:'A','select public.admin_clear_delivered_addresses()')), 'High');
select pg_temp.chk('parent cannot call admin recordings / preview admin', pg_temp.denied(pg_temp.as_('authenticated',:'A','select * from public.admin_list_recordings()')) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select * from public.admin_preview_list(gen_random_uuid())$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.admin_preview_delete_person('a@b.co')$q$)), 'High');
select pg_temp.chk('parent cannot call tutor_group_practice / skill_report / slips for a group', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select * from public.tutor_group_practice('L1A')$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select * from public.tutor_group_skill_report('L1A','hol-l1l01')$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select * from public.tutor_group_slips('L1A','hol-l1l01')$q$)), 'High');
select pg_temp.chk('tutor cannot call admin_* functions', pg_temp.denied(pg_temp.as_('authenticated',:'T1','select * from public.admin_list_children()')) and pg_temp.denied(pg_temp.as_('authenticated',:'T1','select * from public.admin_list_ext_orders()')) and pg_temp.denied(pg_temp.as_('authenticated',:'T1','select public.admin_funnel_counts()')), 'High');
select pg_temp.chk('tutor is not an admin (is_admin false)', pg_temp.val('authenticated',:'T1','select public.is_admin()') = 'false', 'High');
select pg_temp.chk('tutor cannot read parents / children / ext_orders / payments tables', pg_temp.val('authenticated',:'T1','select (select count(*) from public.parents where id <> auth.uid())+(select count(*) from public.children)+(select count(*) from public.ext_orders)+(select count(*) from public.payments)+(select count(*) from public.trial_requests)+(select count(*) from public.consents)') = '0', 'High');

-- ===== tutor scope =====
select pg_temp.chk('tutor T1 (group L1A) sees Mia''s submissions', pg_temp.val('authenticated',:'T1',$q$select count(*) from public.practice_submissions where child_id=(select mia from public.audit_ctx)$q$) = '1', 'Medium');
select pg_temp.chk('tutor T1 cannot see Ben''s submissions (not in group)', pg_temp.val('authenticated',:'T1',$q$select count(*) from public.practice_submissions where child_id=(select ben from public.audit_ctx)$q$) = '0', 'High');
select pg_temp.chk('tutor T1 cannot read Ben''s attempts', pg_temp.val('authenticated',:'T1',$q$select count(*) from public.practice_attempts where child_id=(select ben from public.audit_ctx)$q$) = '0', 'High');
select pg_temp.chk('tutor T2 (group L2A) cannot see Mia''s submissions or attempts', pg_temp.val('authenticated',:'T2',$q$select (select count(*) from public.practice_submissions)+(select count(*) from public.practice_attempts)$q$) = '0', 'High');
select pg_temp.chk('tutor T2 cannot call tutor_group_practice for L1A', pg_temp.denied(pg_temp.as_('authenticated',:'T2',$q$select * from public.tutor_group_practice('L1A')$q$)), 'High');
select pg_temp.chk('tutor T2 cannot call tutor_group_skill_report/slips for L1A', pg_temp.denied(pg_temp.as_('authenticated',:'T2',$q$select * from public.tutor_group_skill_report('L1A','hol-l1l01')$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'T2',$q$select * from public.tutor_group_slips('L1A','hol-l1l01')$q$)), 'High');
select pg_temp.chk('tutor T2 cannot call practice_child_detail(Mia)', pg_temp.denied(pg_temp.as_('authenticated',:'T2',$q$select * from public.practice_child_detail((select mia from public.audit_ctx),'hol-l1l01')$q$)), 'High');
select pg_temp.chk('tutor T1 can call practice_child_detail(Mia) but not Kai-or-Ben outside the group', pg_temp.as_('authenticated',:'T1',$q$select * from public.practice_child_detail((select mia from public.audit_ctx),'hol-l1l01')$q$) = 'ok:3'
   and pg_temp.denied(pg_temp.as_('authenticated',:'T1',$q$select * from public.practice_child_detail((select ben from public.audit_ctx),'ext-l1u01')$q$)), 'High');
-- tutor loses access when the enrolment is cancelled
update public.enrolments set status = 'cancelled', cancelled_at = now() where parent_id = 'aaaaaaaa-0000-0000-0000-00000000000a';
select pg_temp.chk('tutor T1 loses sight of Mia once the enrolment is cancelled', pg_temp.val('authenticated',:'T1',$q$select count(*) from public.practice_submissions$q$) = '0', 'Medium');
update public.enrolments set status = 'confirmed', cancelled_at = null where parent_id = 'aaaaaaaa-0000-0000-0000-00000000000a';
-- tutor sees an extension-book submission by a child who is also in their group (scope question, informational)
-- admin sees all
select pg_temp.chk('admin sees all submissions and orders', pg_temp.val('authenticated',:'ADM','select count(*) from public.practice_submissions') = '2' and pg_temp.val('authenticated',:'ADM','select count(*) from public.ext_orders') = '2', 'Low');

-- ===== anon =====
select pg_temp.chk('anon cannot read any family table', pg_temp.denied(pg_temp.as_('anon',null,'select * from public.children')) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.parents')) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.ext_orders')) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.practice_submissions')) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.trial_requests')), 'High');
select pg_temp.chk('anon cannot call parent/admin/tutor functions', pg_temp.denied(pg_temp.as_('anon',null,$q$select public.add_child('x',1,'7391')$q$)) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.my_children_progress()')) and pg_temp.denied(pg_temp.as_('anon',null,'select public.delete_my_data()')) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.admin_list_children()')) and pg_temp.denied(pg_temp.as_('anon',null,$q$select * from public.tutor_group_practice('L1A')$q$)), 'High');
select pg_temp.chk('anon: list_ext_prices works and returns only product_id + amount (public prices)', pg_temp.as_('anon',null,'select * from public.list_ext_prices()') = 'ok:4', 'Low');
select pg_temp.chk('anon: group_fill is not callable', pg_temp.denied(pg_temp.as_('anon',null,'select * from public.group_fill()')), 'Low');
-- X: a parent with no children: no data from others
select pg_temp.chk('stranger parent X sees nothing of others', pg_temp.val('authenticated',:'X','select (select count(*) from public.children)+(select count(*) from public.ext_orders)+(select count(*) from public.practice_submissions)+(select count(*) from public.trial_requests)') = '0', 'High');
-- the auth.uid() NULL case: authenticated role with no subject
select pg_temp.chk('authenticated with no subject (no JWT sub) is rejected by parent functions', pg_temp.denied(pg_temp.as_('authenticated',null,$q$select public.add_child('x',1,'7391')$q$)), 'High');
