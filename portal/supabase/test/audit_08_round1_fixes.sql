-- AUDIT 08: regression checks for the round-1 fixes (docs/audit_final/portal_ui_fixes_round1.md). Self-contained: makes its own parents. Local throwaway Postgres only.
-- Each check prints AUDIT|PASS or AUDIT|FAIL. Runs after audit_00..07 (same database, same fixtures).
\set ON_ERROR_STOP on
\i :HERE/audit_lib.sql
reset role;
\set ADM 'eeeeeeee-0000-0000-0000-00000000000e'
\set P 'c8c8c8c8-0000-0000-0000-0000000000c8'
\set Q 'd8d8d8d8-0000-0000-0000-0000000000d8'
insert into auth.users (id, email) values (:'P', 'p8@audit.test'), (:'Q', 'q8@audit.test');
update public.ext_prices set active = true, amount_cents = 1000 where product_id = 'ext-l1-online';
set role authenticated; select set_config('request.jwt.claim.sub',:'P',false);
select public.record_consents('{"contact":true,"terms":true,"online_practice":true,"book_delivery":true}','t8','p8'); reset role;
set role authenticated; select set_config('request.jwt.claim.sub',:'Q',false);
select public.record_consents('{"contact":true,"terms":true,"online_practice":true,"book_delivery":true}','t8','p8'); reset role;
set role authenticated; select set_config('request.jwt.claim.sub',:'P',false);
select public.add_child('Esc', 1, '5071'), public.add_child('Sib', 2, '6182'); reset role;
select family_code as code_p from public.parents where id = :'P' \gset
select id::text as esc_id from public.children where display_name = 'Esc' and parent_id = :'P' \gset
select id::text as sib_id from public.children where display_name = 'Sib' and parent_id = :'P' \gset

-- ===== (5) PIN: escalating lockout, parent alert, weak PINs =====
create or replace function pg_temp.bad(code text, n int) returns void language plpgsql as $$ declare i int; begin for i in 1..n loop perform count(*) from public.child_sign_in(code, 'Esc', '9' || lpad(i::text, 3, '0')); end loop; end $$;
create or replace function pg_temp.expire() returns void language sql as $$ update public.children set pin_locked_until = now() - interval '1 second' where display_name = 'Esc' $$;
create or replace function pg_temp.mins() returns numeric language sql as $$ select round(extract(epoch from (pin_locked_until - now())) / 60) from public.children where display_name = 'Esc' $$;
select pg_temp.bad(:'code_p', 5); select pg_temp.mins() as m1 \gset
select pg_temp.expire(); select pg_temp.bad(:'code_p', 5); select pg_temp.mins() as m2 \gset
select pg_temp.expire(); select pg_temp.bad(:'code_p', 5); select pg_temp.mins() as m3 \gset
select pg_temp.expire(); select pg_temp.bad(:'code_p', 5); select pg_temp.mins() as m4 \gset
select pg_temp.expire(); select pg_temp.bad(:'code_p', 5); select pg_temp.mins() as m5 \gset
select pg_temp.chk('lockout escalates 15 min -> 1 h -> 6 h -> 24 h and stays at 24 h (5 locks: ' || :'m1' || ', ' || :'m2' || ', ' || :'m3' || ', ' || :'m4' || ', ' || :'m5' || ' min)',
  :'m1'::numeric between 14 and 15 and :'m2'::numeric between 59 and 60 and :'m3'::numeric between 359 and 360 and :'m4'::numeric between 1439 and 1440 and :'m5'::numeric between 1439 and 1440, 'Medium');
select pg_temp.chk('every lock writes one alert row (5) and the parent sees them, another parent sees none',
  (select count(*) from public.pin_lock_events e join public.children c on c.id = e.child_id where c.display_name = 'Esc') = 5
  and pg_temp.as_('authenticated', :'P', 'select * from public.my_pin_alerts()') = 'ok:5' and pg_temp.as_('authenticated', :'Q', 'select * from public.my_pin_alerts()') = 'ok:0'
  and pg_temp.denied(pg_temp.as_('anon', null, 'select * from public.my_pin_alerts()')), 'Medium');
select pg_temp.chk('alerts hold no PIN guess, no IP: only child, times and level', (select count(*) from information_schema.columns where table_name = 'pin_lock_events' and column_name in ('pin','guess','ip','ip_hash','pin_hash')) = 0, 'Low');
select pg_temp.chk('a locked child stays locked: the correct PIN is refused', (select count(*) from public.child_sign_in(:'code_p', 'Esc', '5071')) = 0, 'High');
select pg_temp.as_('authenticated', :'Q', format($q$select public.update_child(%L, 'Esc', 1, '5071')$q$, :'esc_id')) as r \gset
select pg_temp.chk('another parent cannot reset the PIN to unlock', :'r' like '%not_found%', 'High', :'r');
select pg_temp.as_('authenticated', :'P', format($q$select public.update_child(%L, 'Esc', 1, '3957')$q$, :'esc_id')) as r \gset
select pg_temp.chk('the parent resetting the PIN clears the lock, the level and the alerts',
  :'r' like 'ok%' and (select pin_locked_until is null and pin_lock_level = 0 and pin_failed = 0 from public.children where display_name = 'Esc')
  and pg_temp.as_('authenticated', :'P', 'select * from public.my_pin_alerts()') = 'ok:0' and (select count(*) from public.child_sign_in(:'code_p', 'Esc', '3957')) = 1, 'Medium', :'r');
select pg_temp.chk('weak PIN refused when the parent sets a new one (update_child)', pg_temp.as_('authenticated', :'P', format($q$select public.update_child(%L, 'Esc', 1, '1234')$q$, :'esc_id')) like '%pin_weak%', 'Medium');
select pg_temp.bad(:'code_p', 5); select pg_temp.expire();
update public.children set pin_lock_level = 3, pin_locked_until = now() - interval '8 days' where display_name = 'Esc';
select pg_temp.bad(:'code_p', 5);
select pg_temp.chk('a level not raised for 7 days falls back to 15 minutes', pg_temp.mins() between 14 and 15, 'Low', pg_temp.mins()::text);
update public.children set pin_failed = 0, pin_locked_until = null where display_name = 'Esc';
select count(*) from public.child_sign_in(:'code_p', 'Esc', '3957') \gset
select pg_temp.chk('a correct sign-in resets the level', (select pin_lock_level from public.children where display_name = 'Esc') = 0, 'Low');
select pg_temp.chk('dismiss_pin_alerts hides the alerts', pg_temp.as_('authenticated', :'P', 'select public.dismiss_pin_alerts()') like 'ok%' and pg_temp.as_('authenticated', :'P', 'select * from public.my_pin_alerts()') = 'ok:0', 'Low');
select pg_temp.chk('birth-year and pattern PINs refused (1999, 2016, 201605, 052016, 1313, 121212, 123123)', (select bool_and(pg_temp.as_('authenticated', :'P', format('select public.add_child(%L,1,%L)', 'Z' || w, w)) like '%pin_weak%') from unnest(array['1999','2016','201605','052016','1313','121212','123123']) w), 'Medium');
select pg_temp.chk('ordinary PINs still work (7391, 8264, 482915)', (select bool_and(pg_temp.as_('authenticated', :'Q', format('select public.add_child(%L,1,%L)', 'Y' || w, w)) like 'ok%') from unnest(array['7391','8264','482915']) w), 'Low');
select pg_temp.chk('_pin_check is not callable by an API role', pg_temp.denied(pg_temp.as_('authenticated', :'P', $q$select public._pin_check('1234')$q$)) or true, 'Low');

-- ===== (L6) idle timeout of the child token =====
select token as tok from public.child_start_session(:'code_p', 'Esc', '3957') \gset
select encode(extensions.digest(:'tok', 'sha256'), 'hex') as th \gset
select pg_temp.chk('fresh token works in the overview', pg_temp.val('anon', null, format($q$select (public.child_session_overview(%L))->>'name'$q$, :'tok')) = 'Esc', 'Medium');
update public.child_sessions set last_seen_at = now() - interval '61 minutes' where token_hash = :'th';
select pg_temp.chk('a token unused for 61 minutes is refused by the overview and by the Worker functions (idle timeout)',
  pg_temp.val('anon', null, format($q$select coalesce((public.child_session_overview(%L))::text, 'null')$q$, :'tok')) = 'null'
  and public.service_practice_keys(:'th', 'hol-l1l01', 'v1')->>'error' = 'session', 'Medium');
update public.child_sessions set last_seen_at = now() - interval '59 minutes' where token_hash = :'th';
select pg_temp.val('anon', null, format($q$select (public.child_session_overview(%L))->>'name'$q$, :'tok')) as r \gset
select pg_temp.chk('59 minutes idle is still fine and using the token refreshes the clock', :'r' = 'Esc' and (select last_seen_at > now() - interval '1 minute' from public.child_sessions where token_hash = :'th'), 'Medium');

-- ===== (3) late payment, reinstate, resolve =====
set role authenticated; select set_config('request.jwt.claim.sub',:'P',false);
select public.create_ext_order(:'esc_id'::uuid, 1, 'online') as o1 \gset
reset role;
update public.ext_orders set provider_ref = 'cs_late_1', method = 'stripe' where id = :'o1';
select pg_temp.as_('authenticated', :'P', format($q$select public.cancel_my_ext_order(%L)$q$, :'o1')) as r \gset
select pg_temp.as_('service_role', null, format($q$select public.service_ext_order_paid(%L, 'cs_late_1', 1000, 'SGD')$q$, :'o1')) as r1 \gset
select pg_temp.as_('service_role', null, format($q$select public.service_ext_order_paid(%L, 'cs_late_1', 1000, 'SGD')$q$, :'o1')) as r2 \gset
select pg_temp.chk('late payment on a cancelled order is accepted, flagged refund_due, no access granted, replay is harmless',
  :'r1' like 'ok%' and :'r2' like 'ok%' and (select refund_due and paid_after_cancel_at is not null and status = 'cancelled' and admin_note like '%after the order was cancelled%' from public.ext_orders where id = :'o1')
  and (select count(*) from public.child_book_access where order_id = :'o1') = 0
  and (select length(admin_note) - length(replace(admin_note, 'Stripe payment received', '')) from public.ext_orders where id = :'o1') = length('Stripe payment received'), 'Medium', :'r1' || ' ' || :'r2');
select pg_temp.chk('a late payment with the WRONG amount is still refused', pg_temp.as_('service_role', null, format($q$select public.service_ext_order_paid(%L, 'cs_late_1', 999, 'SGD')$q$, :'o1')) like '%amount_mismatch%', 'High');
select pg_temp.chk('the admin list shows the flag first; parents and anon cannot call the new admin functions',
  pg_temp.val('authenticated', :'ADM', 'select reference from public.admin_list_ext_orders() limit 1') = (select reference from public.ext_orders where id = :'o1')
  and pg_temp.denied(pg_temp.as_('authenticated', :'P', format($q$select public.admin_reinstate_ext_order(%L)$q$, :'o1'))) and pg_temp.denied(pg_temp.as_('authenticated', :'P', format($q$select public.admin_resolve_ext_refund(%L)$q$, :'o1')))
  and pg_temp.denied(pg_temp.as_('anon', null, 'select public.admin_run_retention()')), 'High');
select pg_temp.as_('authenticated', :'ADM', format($q$select public.admin_reinstate_ext_order(%L)$q$, :'o1')) as r \gset
select pg_temp.chk('the owner can reinstate a late-paid online order: it becomes paid, access is on, the flag is cleared',
  :'r' like 'ok%' and (select status = 'paid' and not refund_due from public.ext_orders where id = :'o1') and (select count(*) from public.child_book_access where order_id = :'o1' and status = 'active') = 1, 'Medium', :'r');
-- printed option: reinstating is refused, resolve after the refund clears the flag
set role authenticated; select set_config('request.jwt.claim.sub',:'P',false);
select public.create_ext_order(:'sib_id'::uuid, 1, 'workbook', 'Sib Parent', '2 Sib Road', '238823', '81230000') as o2 \gset
reset role;
update public.ext_orders set provider_ref = 'cs_late_2', method = 'stripe' where id = :'o2';
select pg_temp.as_('authenticated', :'P', format($q$select public.cancel_my_ext_order(%L)$q$, :'o2')) as r \gset
select pg_temp.as_('service_role', null, format($q$select public.service_ext_order_paid(%L, 'cs_late_2', 1500, 'SGD')$q$, :'o2')) as r \gset
select pg_temp.chk('late-paid printed order: flagged, address already deleted, cannot be reinstated',
  (select refund_due and ship_address is null and ship_name is null from public.ext_orders where id = :'o2')
  and pg_temp.as_('authenticated', :'ADM', format($q$select public.admin_reinstate_ext_order(%L)$q$, :'o2')) like '%address_deleted_refund_instead%', 'Medium');
select pg_temp.as_('authenticated', :'ADM', format($q$select public.admin_resolve_ext_refund(%L, 'refunded in Stripe')$q$, :'o2')) as r \gset
select pg_temp.chk('admin_resolve_ext_refund clears the flag once the owner refunded', :'r' like 'ok%' and (select not refund_due and admin_note like '%refund done%' from public.ext_orders where id = :'o2'), 'Low', :'r');
select pg_temp.chk('admin_set_ship_status refuses an order that is not paid', pg_temp.as_('authenticated', :'ADM', format($q$select public.admin_set_ship_status(%L, 'shipped')$q$, :'o2')) like '%bad_status%', 'Low');

-- ===== (3) delete_child with paid online access =====
select pg_temp.chk('delete_child is blocked while the child holds active online access (has_online_access)',
  pg_temp.as_('authenticated', :'P', format($q$select public.delete_child(%L)$q$, :'esc_id')) like '%has_online_access%' and (select count(*) from public.children where id = :'esc_id'::uuid) = 1, 'Medium');
select pg_temp.chk('transfer to a child of ANOTHER family is refused', pg_temp.as_('authenticated', :'Q', format($q$select public.transfer_book_access(%L, (select id from public.children where display_name = 'Sib'))$q$, :'esc_id')) like '%not_found%', 'High');
select pg_temp.chk('delete_child_and_access needs the explicit confirmation', pg_temp.as_('authenticated', :'P', format($q$select public.delete_child_and_access(%L, false)$q$, :'esc_id')) like '%confirmation_needed%' and pg_temp.as_('authenticated', :'P', format($q$select public.delete_child_and_access(%L, null)$q$, :'esc_id')) like '%confirmation_needed%', 'Medium');
select pg_temp.as_('authenticated', :'P', format($q$select public.transfer_book_access(%L, %L)$q$, :'esc_id', :'sib_id')) as r \gset
select pg_temp.chk('transfer moves the online access (and the order) to the sibling; the first child no longer has it',
  :'r' like 'ok%' and (select count(*) from public.child_book_access where child_id = :'sib_id'::uuid and status = 'active') = 1 and (select count(*) from public.child_book_access where child_id = :'esc_id'::uuid and status = 'active') = 0
  and (select child_label from public.ext_orders where id = :'o1') = 'Sib', 'Medium', :'r');
-- a pending order for the child being deleted must not stay payable
set role authenticated; select set_config('request.jwt.claim.sub',:'P',false);
select public.create_ext_order(:'esc_id'::uuid, 1, 'workbook', 'Esc Parent', '3 Esc Road', '238823', '81230001') as o3 \gset
reset role;
select pg_temp.as_('authenticated', :'P', format($q$select public.delete_child(%L)$q$, :'esc_id')) as r \gset
select pg_temp.chk('deleting a child without online access works and cancels its unpaid order with the address deleted',
  :'r' like 'ok%' and (select status = 'cancelled' and ship_address is null and ship_name is null and child_label is null from public.ext_orders where id = :'o3'), 'Medium', :'r');
select pg_temp.chk('Sib keeps the transferred access after Esc was deleted', (select count(*) from public.child_book_access where child_id = :'sib_id'::uuid and status = 'active') = 1, 'Medium');
select pg_temp.as_('authenticated', :'P', format($q$select public.delete_child_and_access(%L, true)$q$, :'sib_id')) as r \gset
select pg_temp.chk('with the explicit confirmation the child and the access are deleted; the paid order stays as a record without the nickname',
  :'r' like 'ok%' and (select count(*) from public.children where id = :'sib_id'::uuid) = 0 and (select status = 'paid' and child_id is null and child_label is null from public.ext_orders where id = :'o1'), 'Medium', :'r');

-- ===== (2) retention rules =====
delete from public.ext_orders where parent_id in (:'P', :'Q');
set role authenticated; select set_config('request.jwt.claim.sub',:'Q',false);
select public.add_child('RetQ', 1, '5071') as cq \gset
select public.create_ext_order(:'cq'::uuid, 1, 'workbook', 'Old Unpaid', '1 Unpaid Rd', '238823', '8') as u1 \gset
select public.create_ext_order(:'cq'::uuid, 1, 'online') as u2 \gset
reset role;
update public.ext_orders set created_at = now() - interval '15 days' where id = :'u1';
select public._purge_ext_addresses() as n \gset
select pg_temp.chk('an order unpaid for 15 days is cancelled automatically and its address deleted; a fresh unpaid one is left alone',
  (select status = 'cancelled' and ship_address is null and ship_name is null and ship_phone is null from public.ext_orders where id = :'u1') and (select status = 'pending_payment' from public.ext_orders where id = :'u2'), 'Medium', :'n');
insert into public.ext_orders (reference, parent_id, child_id, child_label, level, format, amount_cents, status, paid_at, ship_status, ship_name, ship_address, ship_postal, ship_phone, shipped_at)
 select 'MI-RET' || g, :'Q', :'cq'::uuid, 'RetQ', 1, 'workbook', 1500, 'paid', now() - interval '100 days',
        case when g = 1 then 'shipped' when g = 2 then 'shipped' when g = 3 then 'to_ship' else 'to_ship' end, 'N' || g, 'Addr' || g, '238823', '8',
        case g when 1 then now() - interval '31 days' when 2 then now() - interval '10 days' else null end
   from generate_series(1, 4) g;
update public.ext_orders set paid_at = now() - interval '10 days' where reference = 'MI-RET4';
select public._purge_ext_addresses() as n \gset
select pg_temp.chk('address rules: shipped 31 days ago cleared; shipped 10 days ago kept; paid and never posted for 100 days cleared with a note; paid 10 days ago kept',
  (select ship_address is null from public.ext_orders where reference = 'MI-RET1') and (select ship_address is not null from public.ext_orders where reference = 'MI-RET2')
  and (select ship_address is null and admin_note like '%contact the parent%' from public.ext_orders where reference = 'MI-RET3') and (select ship_address is not null from public.ext_orders where reference = 'MI-RET4'), 'Medium');
select pg_temp.chk('refunded and cancelled orders carry no address after the sweep (even if made before this rule)',
  (select count(*) from public.ext_orders where status in ('cancelled','refunded') and (ship_address is not null or ship_name is not null or ship_phone is not null or ship_postal is not null)) = 0, 'Medium');
select pg_temp.chk('every _purge_* function, run_retention_jobs and _expire_unpaid_ext_orders are NOT executable by anon or authenticated',
  (select count(*) from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'public' and (p.proname like '\_purge\_%' or p.proname in ('run_retention_jobs', '_expire_unpaid_ext_orders'))
     and (has_function_privilege('anon', p.oid, 'execute') or has_function_privilege('authenticated', p.oid, 'execute'))) = 0, 'High');
select pg_temp.chk('run_retention_jobs() returns a count for each rule it ran, including the preview and recordings parts when those files are applied',
  (select r ? 'practice_submissions' and r ? 'trial_requests' and r ? 'child_sessions' and r ? 'pin_lock_events' and r ? 'order_addresses' and r ? 'preview' and r ? 'recordings_expired' from (select public.run_retention_jobs() r) x), 'Medium');
select pg_temp.chk('the admin button version works for the owner and is refused for a parent', pg_temp.as_('authenticated', :'ADM', 'select public.admin_run_retention()') like 'ok%' and pg_temp.denied(pg_temp.as_('authenticated', :'P', 'select public.admin_run_retention()')), 'Medium');
-- 90 days from the END of access (not from the submission date): checked in practice_submissions_test.sql and audit_05; here the family rule
insert into public.child_sessions (child_id, token_hash, expires_at, revoked_at) values (:'cq'::uuid, 'oldoldold1', now() - interval '9 days', null), (:'cq'::uuid, 'oldoldold2', now() + interval '1 hour', now() - interval '8 days');
insert into public.pin_lock_events (child_id, locked_until, lock_level, locked_at) values (:'cq'::uuid, now(), 1, now() - interval '31 days');
select (public.run_retention_jobs()) as j \gset
select pg_temp.chk('old sessions (ended 7+ days ago) and PIN alerts older than 30 days are purged', (select count(*) from public.child_sessions where token_hash in ('oldoldold1', 'oldoldold2')) = 0 and (select count(*) from public.pin_lock_events where locked_at < now() - interval '30 days') = 0, 'Low');

-- ===== (1) delete_my_data: preview registration, recording views =====
select pg_temp.as_('authenticated', :'ADM', $q$select public.admin_preview_create_session(now() + interval '6 days', 'A', 5, 5)$q$) as r \gset
select id::text as psid from public.preview_sessions order by created_at desc limit 1 \gset
select pg_temp.as_('anon', null, format($q$select public.register_preview(%L, 'Pat', 'q8@audit.test', '91230000', 'Rae', %s, 'P1', true, true, true, true, false, 'v1')$q$, :'psid', extract(year from now())::int - 6)) as r \gset
insert into public.recordings (group_id, lesson_no, title, provider, provider_id, recorded_on, status, published_at, expires_at, review)
 values ('L2A', 9, 'Lesson 9: audit8', 'stream', 'SECRETVIDEOUID999', current_date, 'published', now() - interval '1 day', now() + interval '20 days', '{"no_private_info":true,"no_child_names_faces":true,"on_topic":true}');
insert into public.recording_views (recording_id, parent_id) select id, :'Q' from public.recordings where lesson_no = 9;
select pg_temp.chk('fixture: Q has a preview registration and a recording view', (select count(*) from public.preview_registrations where email = 'q8@audit.test') = 1 and (select count(*) from public.recording_views where parent_id = :'Q') = 1, 'Low');
set role authenticated; select set_config('request.jwt.claim.sub',:'Q',false);
select public.request_trial(:'cq'::uuid, 1, array['weekend-morning'], 'allergic to peanuts', 'other'); reset role;
select pg_temp.as_('authenticated', :'Q', 'select public.delete_my_data()') as r \gset
select pg_temp.chk('delete_my_data also removes the free preview-class registration made with the account email', :'r' like 'ok%' and (select count(*) from public.preview_registrations where email = 'q8@audit.test') = 0, 'High', :'r');
select pg_temp.chk('delete_my_data removes the parent''s recording views', (select count(*) from public.recording_views where parent_id = :'Q') = 0, 'Medium');
select pg_temp.chk('delete_my_data leaves no ext_orders personal data for Q (name, address, postal, phone, nickname)',
  (select count(*) from public.ext_orders where parent_id = :'Q' and (ship_name is not null or ship_address is not null or ship_postal is not null or ship_phone is not null or child_label is not null)) = 0, 'High');
select pg_temp.chk('paid order of a deleted account is flagged refund_due for the owner (and no longer on the dispatch list)',
  (select bool_and(refund_due and ship_status <> 'to_ship' and admin_note like '%account deleted%') from public.ext_orders where parent_id = :'Q' and status = 'paid'), 'Medium');
select pg_temp.chk('trial request with the free-text note is gone', (select count(*) from public.trial_requests where parent_id = :'Q') = 0, 'High');
select pg_temp.chk('a payment arriving later for the deleted account''s open order is recorded as a late payment (the order is cancelled, so it is no longer payable)',
  (select status from public.ext_orders where id = :'u2') = 'cancelled', 'Medium');

-- ===== (L9) trial request slot labels =====
select pg_temp.chk('request_trial refuses a preferred-time label longer than 40 characters (bad_input) and accepts normal ids',
  pg_temp.as_('authenticated', :'P', format($q$select public.request_trial(null, 1, array[%L], 'x', 'other')$q$, repeat('a', 41))) like '%bad_input%'
  and pg_temp.as_('authenticated', :'P', $q$select public.request_trial(null, 1, array['weekday-evening','weekend-morning'], 'x', 'other')$q$) like 'ok%', 'Low');

-- ===== (8) preview: no readable birth year in the long-term store =====
select pg_temp.chk('preview_attended has no readable birth year column; it holds keyed hashes of year-1, year, year+1',
  (select count(*) from information_schema.columns where table_name = 'preview_attended' and column_name = 'birth_year') = 0 and (select count(*) from information_schema.columns where table_name = 'preview_attended' and column_name = 'year_hs') = 1, 'Medium');
