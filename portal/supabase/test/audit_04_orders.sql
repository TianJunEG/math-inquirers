-- AUDIT 04: extension-book purchase flow: states, double orders, siblings, price handling, payment forgery, refunds, address handling. Local throwaway Postgres only.
\set ON_ERROR_STOP on
\i :HERE/audit_lib.sql
reset role;
\set A 'aaaaaaaa-0000-0000-0000-00000000000a'
\set B 'bbbbbbbb-0000-0000-0000-00000000000b'
\set X 'ffffffff-0000-0000-0000-00000000000f'
\set ADM 'eeeeeeee-0000-0000-0000-00000000000e'
-- clean slate for this file
delete from public.child_book_access; delete from public.ext_orders; delete from public.practice_submissions;
update public.ext_prices set active = true;

-- ===== creation guards =====
select pg_temp.chk('no price (L3) -> price_not_set, no order row', pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),3,'online')$q$) like '%price_not_set%' and (select count(*) from public.ext_orders)=0, 'High');
update public.ext_prices set active = false where product_id = 'ext-l1-online';
select pg_temp.chk('inactive price -> price_not_set', pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'online')$q$) like '%price_not_set%', 'High');
update public.ext_prices set active = true;
select pg_temp.chk('NULL level/format -> rejected, not silently accepted', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),null,'online')$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,null)$q$)), 'Medium');
select pg_temp.chk('bad format / level 0 / level 7 rejected', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'pdf')$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),0,'online')$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),7,'online')$q$)), 'Medium');
select pg_temp.chk('SQL injection in format/ship fields cannot execute (rejected or stored literally)',
  pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,$$online'; drop table public.ext_orders;--$$)$q$)) and to_regclass('public.ext_orders') is not null, 'High');
select pg_temp.chk('stranger X (no consents, no children) cannot order', pg_temp.denied(pg_temp.as_('authenticated',:'X',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'online')$q$)), 'High');

-- consents: B withdraws online_practice -> cannot order online or both, can order workbook if book_delivery
set role authenticated; select set_config('request.jwt.claim.sub',:'B',false);
select public.record_consents('{"online_practice":false}','t2','p2'); reset role;
select pg_temp.chk('online order needs online_practice consent', pg_temp.as_('authenticated',:'B',$q$select public.create_ext_order((select zoe from public.audit_ctx),2,'online')$q$) like '%consents_missing:online_practice%', 'High');
select pg_temp.chk('"both" order needs online_practice consent', pg_temp.denied(pg_temp.as_('authenticated',:'B',$q$select public.create_ext_order((select ben from public.audit_ctx),1,'both','B Parent','1 Road','123456','9')$q$)), 'High');
set role authenticated; select set_config('request.jwt.claim.sub',:'B',false);
select public.record_consents('{"online_practice":true,"book_delivery":false}','t3','p3'); reset role;
select pg_temp.chk('workbook order needs book_delivery consent', pg_temp.as_('authenticated',:'B',$q$select public.create_ext_order((select ben from public.audit_ctx),1,'workbook','B Parent','1 Road','123456','9')$q$) like '%consents_missing:book_delivery%', 'High');
set role authenticated; select set_config('request.jwt.claim.sub',:'B',false);
select public.record_consents('{"book_delivery":true}','t4','p4'); reset role;

-- ===== address handling =====
select pg_temp.chk('workbook order without address rejected (bad_address)', pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'workbook',null,null,null,null)$q$) like '%bad_address%', 'Medium');
select pg_temp.chk('workbook order with 5-digit and 7-digit postal rejected', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'workbook','N','Addr','12345','9')$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'workbook','N','Addr','1234567','9')$q$)), 'Medium');
select pg_temp.chk('workbook order with NULL postal code is rejected (SQL NULL logic in the bad_address guard)',
  pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'workbook','Name Here','1 Some Road',null,'9')$q$)), 'Medium', 'p_ship_postal !~ ... is NULL for NULL, and "false or false or NULL" does not raise');
delete from public.ext_orders where ship_postal is null and format = 'workbook';
select pg_temp.chk('postal code must be a real Singapore sector (first two digits 01-82)', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select kai from public.audit_ctx),1,'workbook','N','Addr','000000','9')$q$)), 'Low', 'only the 6-digit shape is checked; a stricter check is cheap');
delete from public.ext_orders where ship_postal = '000000';
-- online-only order must not keep an address even if a client sends one (data minimisation at API level)
select pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select kai from public.audit_ctx),1,'online','Sneaky Name','Sneaky Address','654321','98765432')$q$) as r \gset
select pg_temp.chk('online-only order with an address is REJECTED (bad_address) and nothing is stored (R1-M4)', :'r' like '%bad_address%' and (select count(*) from public.ext_orders where format='online' and (ship_name is not null or ship_address is not null or ship_phone is not null or ship_postal is not null)) = 0, 'Medium', :'r');
select pg_temp.chk('online-only order with only a phone number is also rejected', pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select kai from public.audit_ctx),1,'online',null,null,null,'98765432')$q$) like '%bad_address%', 'Low');
-- injection stored literally
select pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'workbook',$$<img src=x onerror=alert(1)>$$,$$'); drop table public.children;-- <script>$$,'123456','+65 9123 4567')$q$);
select pg_temp.chk('hostile text in address is stored literally; tables intact', (select ship_address from public.ext_orders where format='workbook' and child_label='Mia') like '%drop table%' and to_regclass('public.children') is not null, 'High');
select pg_temp.chk('over-long address (201 chars) is refused', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select kai from public.audit_ctx),1,'workbook','N',repeat('x',201),'123456','9')$q$)), 'Low');

-- ===== double orders / siblings =====
select pg_temp.chk('second unpaid workbook for same child+level -> already_pending', pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'workbook','N','Addr','123456','9')$q$) like '%already_pending%', 'Medium');
select pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'online')$q$);
select pg_temp.chk('online + workbook pending side by side for same child is allowed (different kinds)', (select count(*) from public.ext_orders where child_label='Mia' and status='pending_payment') = 2, 'Low');
select pg_temp.chk('"both" while an online order is pending -> already_pending', pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'both','N','Addr','123456','9')$q$) like '%already_pending%', 'Medium');
select pg_temp.chk('NOTHING is unlocked by a pending order (no access, no units)', (select count(*) from public.child_book_access) = 0 and (select count(*) from public._child_units((select mia from public.audit_ctx)) where product='extension') = 0, 'High');
do $$ declare i int; n int := 0; begin
  for i in 1..30 loop
    begin
      perform pg_temp.as_('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select public.create_ext_order((select kai from public.audit_ctx),2,'online')$q$);
      perform pg_temp.as_('authenticated','aaaaaaaa-0000-0000-0000-00000000000a',$q$select public.cancel_my_ext_order((select id from public.ext_orders where child_label='Kai' and level=2 and status='pending_payment'))$q$);
    exception when others then null; end;
  end loop;
  select count(*) into n from public.ext_orders where child_label='Kai' and level=2 and status='cancelled';
  perform pg_temp.chk('order create/cancel loop is rate limited (30 cycles attempted)', n < 30, 'Low', n || ' cancelled order rows created by one parent in one go; no per-parent rate limit (creates rows and reference codes without bound)');
  delete from public.ext_orders where child_label='Kai' and level=2;
end $$;

-- ===== forging payment =====
select pg_temp.chk('parent cannot mark own order paid (admin fn)', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.admin_mark_ext_order_paid((select id from public.ext_orders where child_label='Mia' and format='online'))$q$)), 'High');
select pg_temp.chk('parent cannot call service_ext_order_paid', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.service_ext_order_paid((select id from public.ext_orders where child_label='Mia' and format='online'),'cs_x',1000,'SGD')$q$)), 'High');
select pg_temp.chk('anon cannot call service_ext_order_paid', pg_temp.denied(pg_temp.as_('anon',null,$q$select public.service_ext_order_paid(gen_random_uuid(),'cs_x',1000,'SGD')$q$)), 'High');
select pg_temp.chk('parent cannot call _order_paid / _order_refunded', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public._order_paid((select id from public.ext_orders limit 1),'admin',null)$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public._order_refunded((select id from public.ext_orders limit 1))$q$)), 'High');
select pg_temp.chk('service: wrong amount is refused', pg_temp.as_('service_role',null,$q$select public.service_ext_order_paid((select id from public.ext_orders where child_label='Mia' and format='online'),'cs_x',1,'SGD')$q$) like '%amount_mismatch%', 'High');
select pg_temp.chk('service: wrong currency is refused', pg_temp.as_('service_role',null,$q$select public.service_ext_order_paid((select id from public.ext_orders where child_label='Mia' and format='online'),'cs_x',1000,'USD')$q$) like '%amount_mismatch%', 'High');
select pg_temp.chk('service: unknown order id is refused', pg_temp.denied(pg_temp.as_('service_role',null,$q$select public.service_ext_order_paid(gen_random_uuid(),'cs_x',1000,'SGD')$q$)), 'Medium');
select pg_temp.chk('refused payments grant nothing', (select count(*) from public.child_book_access) = 0, 'High');

-- ===== paid -> access (service path) =====
select pg_temp.as_('service_role',null,$q$select public.service_ext_order_paid((select id from public.ext_orders where child_label='Mia' and format='online'),'cs_test_1',1000,'sgd')$q$) as r \gset
select pg_temp.chk('service: right amount marks paid and grants access to THAT child only', :'r' like 'ok%'
  and (select count(*) from public.child_book_access a join public.children c on c.id=a.child_id where c.display_name='Mia' and a.status='active') = 1 and (select count(*) from public.child_book_access) = 1, 'High');
select pg_temp.as_('service_role',null,$q$select public.service_ext_order_paid((select id from public.ext_orders where child_label='Mia' and format='online'),'cs_test_1',1000,'SGD')$q$) as r \gset
select pg_temp.chk('webhook replay is idempotent (no double access)', :'r' like 'ok%' and (select count(*) from public.child_book_access) = 1, 'Medium');
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_mark_ext_order_paid((select id from public.ext_orders where child_label='Mia' and format='online'))$q$) as r \gset
select pg_temp.chk('admin tick after Stripe paid is a no-op (no double access)', :'r' like 'ok%' and (select count(*) from public.child_book_access) = 1, 'Medium');
select pg_temp.chk('Mia now has ext L1 units; Kai (sibling) does not', (select count(*) from public._child_units((select mia from public.audit_ctx)) where product='extension') = 2 and (select count(*) from public._child_units((select kai from public.audit_ctx)) where product='extension') = 0, 'High');
select pg_temp.chk('a second order for Kai (sibling) is allowed and independent', pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select kai from public.audit_ctx),1,'online')$q$) like 'ok%', 'Medium');
select pg_temp.chk('already_has_online blocks a second online/both order for Mia', pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'both','N','Addr','123456','9')$q$) like '%already_has_online%', 'Medium');
select pg_temp.chk('same Stripe session id cannot pay two different orders', pg_temp.denied(pg_temp.as_('service_role',null,$q$select public.service_ext_order_paid((select id from public.ext_orders where child_label='Kai' and format='online' and status='pending_payment'),'cs_test_1',1000,'SGD')$q$)), 'High');
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_set_ext_price('ext-l1-online', 5000)$q$) as r \gset
select pg_temp.chk('price later changed: order amount stays as at order time', :'r' like 'ok%' and (select amount_cents from public.ext_orders where child_label='Mia' and format='online') = 1000, 'Low');
select pg_temp.chk('admin_set_ext_price rejects 0 and negative', pg_temp.denied(pg_temp.as_('authenticated',:'ADM',$q$select public.admin_set_ext_price('ext-l1-online', 0)$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'ADM',$q$select public.admin_set_ext_price('ext-l1-online', -5)$q$)) and pg_temp.denied(pg_temp.as_('authenticated',:'ADM',$q$select public.admin_set_ext_price('ext-l9-pdf', 5)$q$)), 'Medium');
update public.ext_prices set amount_cents = 1000 where product_id = 'ext-l1-online';

-- ===== cancel races =====
select pg_temp.chk('parent cannot cancel a paid order', pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.cancel_my_ext_order((select id from public.ext_orders where child_label='Mia' and format='online'))$q$)), 'High');
select pg_temp.as_('authenticated',:'A',$q$select public.cancel_my_ext_order((select id from public.ext_orders where child_label='Mia' and format='workbook'))$q$) as r \gset
select pg_temp.chk('parent cancel of unpaid workbook clears the address', :'r' like 'ok%'
  and (select ship_address is null and ship_name is null and ship_postal is null and ship_phone is null and status='cancelled' from public.ext_orders where child_label='Mia' and format='workbook'), 'High');
-- Stripe session already open, parent cancels, customer then pays the open session
update public.ext_orders set provider_ref = 'cs_test_open', method = 'stripe' where child_label='Kai' and format='online' and status='pending_payment';
select pg_temp.as_('authenticated',:'A',$q$select public.cancel_my_ext_order((select id from public.ext_orders where child_label='Kai' and format='online' and status='pending_payment'))$q$);
select pg_temp.chk('PAYMENT AFTER CANCEL: a Stripe payment for a cancelled order is recorded for the owner (not an unrecorded error)',
  pg_temp.as_('service_role',null,$q$select public.service_ext_order_paid((select id from public.ext_orders where child_label='Kai' and status='cancelled' and format='online'),'cs_test_open',1000,'SGD')$q$) like 'ok%', 'Medium',
  'raises bad_status: the money is taken by Stripe, nothing is recorded or flagged in the database (the enrolment flow has paid_enrolment_cancelled for this). cancel_my_ext_order also does not check that a Checkout Session is open');
select pg_temp.chk('cancelled order stays unpaid and grants nothing', (select count(*) from public.child_book_access a join public.children c on c.id=a.child_id where c.display_name='Kai') = 0, 'High');

-- ===== refund =====
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_refund_ext_order((select id from public.ext_orders where child_label='Mia' and format='online'))$q$) as r \gset
select pg_temp.chk('admin refund revokes access and units', :'r' like 'ok%'
  and (select count(*) from public._child_units((select mia from public.audit_ctx)) where product='extension') = 0 and (select status from public.ext_orders where child_label='Mia' and format='online') = 'refunded', 'High');
select pg_temp.as_('service_role',null,$q$select public.service_ext_order_paid((select id from public.ext_orders where child_label='Mia' and format='online'),'cs_test_1',1000,'SGD')$q$) as r \gset
select pg_temp.chk('refunded order cannot be flipped back to paid by a late webhook', pg_temp.denied(:'r') and (select count(*) from public.child_book_access where status='active') = 0, 'High');
-- refunded workbook order keeps its address
select pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select mia from public.audit_ctx),1,'workbook','Refund Person','9 Refund Lane','111111','81234567')$q$);
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_mark_ext_order_paid((select id from public.ext_orders where ship_name='Refund Person'))$q$);
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_refund_ext_order((select id from public.ext_orders where ship_name='Refund Person'))$q$);
update public.ext_orders set created_at = now() - interval '200 days' where ship_name='Refund Person';
select pg_temp.as_('authenticated',:'ADM','select public.admin_clear_delivered_addresses()');
select pg_temp.chk('REFUNDED (never delivered) order: the delivery address is cleared by the retention routine', (select ship_address is null from public.ext_orders where reference = (select reference from public.ext_orders where child_label='Mia' and format='workbook' and status='refunded')), 'Medium',
  'only ship_status=delivered is ever cleared (30 days). Refunded, undelivered, lost or never-marked-delivered orders keep name, address and phone indefinitely, against the 30-day promise in the consent line');
select pg_temp.chk('admin_set_ship_status cannot mark a refunded/unpaid order as shipped', pg_temp.denied(pg_temp.as_('authenticated',:'ADM',$q$select public.admin_set_ship_status((select id from public.ext_orders where status='refunded' and format='workbook'),'shipped')$q$)) , 'Low', 'no status guard: an unpaid or refunded order can be marked posted');

-- delivered > 30 days is cleared; < 30 days is kept
select pg_temp.as_('authenticated',:'A',$q$select public.create_ext_order((select kai from public.audit_ctx),1,'workbook','Deliv One','1 Deliv Rd','222222','8')$q$);
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_mark_ext_order_paid((select id from public.ext_orders where ship_name='Deliv One'))$q$);
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_set_ship_status((select id from public.ext_orders where ship_name='Deliv One'),'delivered')$q$);
select pg_temp.as_('authenticated',:'ADM','select public.admin_clear_delivered_addresses()');
select pg_temp.chk('address kept inside 30 days after delivery', (select ship_address is not null from public.ext_orders where ship_name='Deliv One'), 'Low');
update public.ext_orders set delivered_at = now() - interval '31 days' where ship_name='Deliv One';
select pg_temp.as_('authenticated',:'ADM','select public.admin_clear_delivered_addresses()');
select pg_temp.chk('address (name, address, postal, phone) cleared 31 days after delivery', (select count(*) from public.ext_orders where status='paid' and ship_status='delivered' and (ship_address is not null or ship_name is not null or ship_phone is not null or ship_postal is not null)) = 0, 'High');
select pg_temp.note('R1: the address rule is now _purge_ext_addresses(), run daily by run_retention_jobs() (pg_cron lines in portal/README.md, not enabled by any file); see audit_08', 'Low');

-- ===== deleting a child who has a paid book =====
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_grant_book_access((select zoe from public.audit_ctx),2,'online','audit')$q$);
select pg_temp.as_('authenticated',:'B',$q$select public.delete_child((select zoe from public.audit_ctx))$q$);
select pg_temp.chk('deleting a child who holds paid/granted online access is blocked or warned by the database', (select count(*) from public.children where display_name='Zoe') = 1, 'Medium',
  'delete_child cascades child_book_access; a paid ext_order keeps child_id NULL. No guard like cancel_enrolment_first; the UI confirm text does not mention the purchase');
