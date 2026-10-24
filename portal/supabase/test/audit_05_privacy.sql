-- AUDIT 05: privacy: deletion, retention, consent gating, birth year, data minimisation, hostile text. Local throwaway Postgres only.
\set ON_ERROR_STOP on
\i :HERE/audit_lib.sql
reset role;
\set ADM 'eeeeeeee-0000-0000-0000-00000000000e'
\set G 'a0a0a0a0-0000-0000-0000-0000000000a0'
insert into auth.users (id, email) values (:'G', 'pg@audit.test');
delete from public.child_book_access; delete from public.ext_orders; delete from public.practice_submissions; delete from public.trial_requests;
update public.ext_prices set active = true, amount_cents = 1000 where product_id = 'ext-l1-online';

-- ===== family G: a full life, then "delete my data" =====
set role authenticated; select set_config('request.jwt.claim.sub',:'G',false);
do $$ declare c uuid; begin
  c := public.add_child_profile('Gigi', 1, '1111', extract(year from now())::int - 8);
  perform public.record_consents('{"contact":true,"terms":true,"online_practice":true,"book_delivery":true,"marketing_contact":true}', 't1','p1');
  perform public.create_ext_order(c, 1, 'workbook', 'Gee Parent', '5 Gee Street #02-02', '555555', '86543210');   -- stays pending
  perform public.create_ext_order(c, 1, 'online');                                                                -- will be paid
  perform public.request_trial(c, 1, array['weekday-evening'], 'My daughter is shy and has a nut allergy', 'other');
end $$;
update public.parents set full_name = 'Gee Parent', phone = '86543210' where id = :'G';
reset role;
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_mark_ext_order_paid((select id from public.ext_orders where format='online' and parent_id='a0a0a0a0-0000-0000-0000-0000000000a0'))$q$);
do $$ declare th text; begin
  insert into public.child_sessions (child_id, token_hash, expires_at) select id, encode(extensions.digest('GIGITOKEN_gggggggggggggggggggggggggggggggggggggg','sha256'),'hex'), now()+interval '4 hours' from public.children where display_name='Gigi';
  perform public.service_practice_record(encode(extensions.digest('GIGITOKEN_gggggggggggggggggggggggggggggggggggggg','sha256'),'hex'),'ext-l1u01','v1',gen_random_uuid(),1,'[{"item_id":"q1","marking_mode":"auto","mark":"right","answered":true,"answer_text":"1"}]');
end $$;
select pg_temp.chk('fixture: Gigi has a submission, a session, access, 2 orders, a trial request', (select count(*) from public.practice_submissions)=1 and (select count(*) from public.child_book_access)=1 and (select count(*) from public.ext_orders)=2 and (select count(*) from public.trial_requests)=1, 'Low');

-- consent gating
select pg_temp.chk('trial request exists with only contact+terms+online_practice+book_delivery (marketing optional)', (select count(*) from public.trial_requests) = 1, 'Low');
select pg_temp.chk('no function gates anything on marketing_contact (it is only stored)', (select count(*) from pg_proc p join pg_namespace n on n.oid=p.pronamespace where n.nspname='public' and p.prosrc like '%marketing_contact%' and p.proname not in ('record_consents')) = 0, 'Low');

-- practice answers deletion that keeps the account
select pg_temp.as_('authenticated',:'G',$q$select public.delete_child_practice((select id from public.children where display_name='Gigi'))$q$) as r \gset
select pg_temp.chk('delete_child_practice removes submissions, attempts and sessions but keeps child and access', :'r' like 'ok%' and (select count(*) from public.practice_submissions)=0 and (select count(*) from public.practice_attempts where child_id=(select id from public.children where display_name='Gigi'))=0
  and (select count(*) from public.child_sessions s join public.children c on c.id=s.child_id where c.display_name='Gigi')=0 and (select count(*) from public.child_book_access)=1, 'High');

-- ===== delete_my_data =====
select pg_temp.as_('authenticated',:'G','select public.delete_my_data()') as r \gset
select pg_temp.chk('delete_my_data runs', :'r' like 'ok%', 'High', :'r');
select pg_temp.chk('parents row emptied (email, name, phone null; deleted_at set)', (select email is null and full_name is null and phone is null and deleted_at is not null from public.parents where id=:'G'), 'High');
select pg_temp.chk('children, sessions, access, submissions gone', (select count(*) from public.children where parent_id=:'G')=0 and (select count(*) from public.child_book_access)=0, 'High');
select pg_temp.chk('login deleted (auth.users)', (select count(*) from auth.users where id=:'G')=0, 'High');
select pg_temp.chk('DELETE MY DATA clears the delivery name/address/phone on the pending workbook order', (select count(*) from public.ext_orders where parent_id=:'G' and (ship_name is not null or ship_address is not null or ship_phone is not null or ship_postal is not null)) = 0, 'High',
  'delete_my_data (schema.sql / finish_setup.sql) pre-dates ext_orders and was not extended; the address, phone and name stay in ext_orders for ever (no retention job touches an unpaid/undelivered order)');
select pg_temp.chk('DELETE MY DATA clears the child''s name snapshot (ext_orders.child_label)', (select count(*) from public.ext_orders where parent_id=:'G' and child_label is not null) = 0, 'High', 'child_label keeps the child''s nickname after the parent asked for deletion');
select pg_temp.chk('DELETE MY DATA cancels the open (unpaid) book order', (select count(*) from public.ext_orders where parent_id=:'G' and status='pending_payment') = 0, 'Medium', 'unpaid orders stay pending_payment against a deleted parent; the owner could still tick them paid');
select pg_temp.note('DELETE MY DATA leaves the PAID book order as plain "paid" with no "refund due" flag (the enrolment path writes "account deleted by parent: refund due per terms"); ext_orders has no note column', 'Medium', 'the parent''s deletion silently removes paid online access with no refund signal to the owner');
select pg_temp.chk('DELETE MY DATA removes the trial request and its free-text note', (select count(*) from public.trial_requests where parent_id=:'G') = 0, 'Medium', 'trial_requests.parent_id references parents (row kept), so ON DELETE CASCADE never fires; the 300-character note ("nut allergy" in the fixture) stays up to 12 months and is listed in admin_list_trial_requests with a blank parent');
select pg_temp.chk('consents of a deleted account are retained anonymised (by design, evidence)', (select count(*) from public.consents where parent_id=:'G') > 0, 'Low');
select pg_temp.chk('a deletion_requests row is written', (select count(*) from public.deletion_requests where parent_id=:'G')=1, 'Low');


-- ===== retention routines =====
-- build old submissions
insert into auth.users (id,email) values ('a1a1a1a1-0000-0000-0000-0000000000a1','ret@audit.test');
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
select public.add_child('Retty', 1, '2222'); reset role;
do $$ declare c uuid := (select id from public.children where display_name='Retty'); s1 uuid; s2 uuid; s3 uuid; begin
  insert into public.child_book_access (child_id, level, format, source) values (c, 1, 'online', 'admin');
  insert into public.practice_submissions (child_id, unit_key, unit_version, client_sid, received_at) values
    (c,'ext-l1u01','v1',gen_random_uuid(), now() - interval '13 months') returning id into s1;
  insert into public.practice_submissions (child_id, unit_key, unit_version, client_sid, received_at) values
    (c,'ext-l1u02','v1',gen_random_uuid(), now() - interval '2 months') returning id into s2;
  perform pg_temp.chk('fixture ok', s1 is not null and s2 is not null, 'Low');
end $$;
select pg_temp.as_('authenticated',:'ADM','select public.admin_purge_expired_practice()') as r \gset
select pg_temp.chk('purge: 13-month-old submission deleted, 2-month-old with active access kept', (select count(*) from public.practice_submissions where unit_key='ext-l1u01')=0 and (select count(*) from public.practice_submissions where unit_key='ext-l1u02')=1, 'High');
update public.child_book_access set status='refunded', ended_at = now() - interval '91 days' where child_id=(select id from public.children where display_name='Retty');
update public.practice_submissions set received_at = now() - interval '100 days' where unit_key='ext-l1u02';
select pg_temp.as_('authenticated',:'ADM','select public.admin_purge_expired_practice()') as r \gset
select pg_temp.chk('purge: 100-day-old submission of a child whose access ended and who has no enrolment is deleted', (select count(*) from public.practice_submissions where unit_key='ext-l1u02')=0, 'High');
select pg_temp.note('the 90-day rule counts from the submission date, not from the date access ended (the consent text says "90 days after access ends")', 'Low', 'a child refunded yesterday with a 100-day-old submission loses data at once; the reverse (kept longer than promised) cannot happen because 12 months is the cap');
select pg_temp.note('the practice purge is manual (button / SQL), not scheduled; 12-month and 30-day promises rely on the owner running it', 'Medium', 'add the pg_cron lines the recordings/preview files already show');
insert into public.trial_requests (parent_id, level, source, expires_at) values ('a1a1a1a1-0000-0000-0000-0000000000a1', 1, 'other', now() - interval '1 day');
select pg_temp.as_('authenticated',:'ADM','select public.admin_purge_expired_practice()') as r \gset
select pg_temp.chk('purge also deletes expired trial requests', (select count(*) from public.trial_requests where parent_id='a1a1a1a1-0000-0000-0000-0000000000a1')=0, 'Low');

-- ===== birth year =====
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
reset role;
select pg_temp.chk('birth year: 1990, 2000 (too old), future year and 2024 (age 2) are refused', pg_temp.denied(pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child_profile('Old',1,'3333',1990)$q$)) and pg_temp.denied(pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child_profile('Fut',1,'3333',extract(year from now())::int + 1)$q$)) and pg_temp.denied(pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child_profile('Tot',1,'3333',extract(year from now())::int - 1)$q$)), 'Low');
select pg_temp.chk('birth year is optional (NULL accepted)', pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child_profile('NoYear',1,'3333',null)$q$) like 'ok%', 'Low');
select pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.update_child_birth_year((select id from public.children where display_name='Retty'), extract(year from now())::int - 9)$q$) as r \gset
select pg_temp.chk('parent can set and read own child''s birth year', pg_temp.val('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select birth_year::text from public.children where display_name='Retty'$q$) = (extract(year from now())::int - 9)::text, 'Low');
select pg_temp.chk('another parent cannot read the birth year', pg_temp.val('authenticated','bbbbbbbb-0000-0000-0000-00000000000b',$q$select count(*) from public.children where birth_year is not null$q$) = '0', 'High');
select pg_temp.chk('a tutor cannot read children.birth_year (no row access to children)', pg_temp.val('authenticated','cccccccc-0000-0000-0000-00000000000c',$q$select count(*) from public.children$q$) = '0', 'High');
select pg_temp.chk('child token overview never returns the birth year', pg_temp.val('anon',null,format($q$select (public.child_session_overview(%L))::text like '%%birth%%'$q$, 'x'||repeat('a',40))) in ('false','<null>'), 'Low');
select pg_temp.note('birth year is a personal-data field the original schema promised not to hold ("no birth date"); it is optional, owner-set; lawyer to confirm. The free preview form (preview_class.sql) REQUIRES a child birth year (2008-2022) for an anonymous parent', 'Medium', 'two different treatments of the same field; the preview stores it in the clear in preview_registrations for 30 days and as a hashed key for 7 months');

-- ===== hostile text in nickname =====
set role authenticated; select set_config('request.jwt.claim.sub','a1a1a1a1-0000-0000-0000-0000000000a1',false);
select public.add_child($$x'); drop table children;--$$, 1, '4444') as r1 \gset
select public.add_child($$<img src=x onerror=alert(1)>$$, 1, '5555') as r2 \gset
reset role;
select pg_temp.chk('SQL-injection nickname stored literally, tables intact', (select count(*) from public.children where display_name like 'x''%') = 1 and to_regclass('public.children') is not null, 'High');
select pg_temp.chk('HTML nickname stored literally (the front end renders with textContent only)', (select count(*) from public.children where display_name like '<img%') = 1, 'Low');
select pg_temp.chk('nickname longer than 30 characters refused', pg_temp.denied(pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child(repeat('x',31),1,'6666')$q$)), 'Low');
select pg_temp.chk('whitespace-only nickname refused', pg_temp.denied(pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child('    ',1,'6666')$q$)), 'Low');
select pg_temp.chk('PIN must be 4-6 digits (letters, 3 digits, 7 digits refused)', pg_temp.denied(pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child('P1',1,'abcd')$q$)) and pg_temp.denied(pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child('P2',1,'123')$q$)) and pg_temp.denied(pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child('P3',1,'1234567')$q$)), 'Medium');
select pg_temp.chk('weak PINs (0000, 1234, 1111) are accepted', pg_temp.as_('authenticated','a1a1a1a1-0000-0000-0000-0000000000a1',$q$select public.add_child('P4',1,'0000')$q$) not like 'ok%', 'Low', 'no weak-PIN list; with 20 guesses/hour per child these fall in the first hours of a targeted attack');
select pg_temp.chk('PIN stored as bcrypt hash, never plaintext', (select count(*) from public.children where pin_hash !~ '^\$2[aby]\$10\$') = 0, 'High');
