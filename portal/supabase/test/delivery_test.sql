-- Local Postgres test for delivery.sql (run by run_delivery_test.sh after stub_supabase.sql, schema.sql, policies.sql). Assertions raise on failure.
\set ON_ERROR_STOP on
create or replace function pg_temp.expect(c boolean, msg text) returns void language plpgsql as $$ begin if not c then raise exception 'FAILED: %', msg; end if; end $$;
create or replace function pg_temp.fails(q text) returns boolean language plpgsql as $$ begin execute q; return false; exception when others then return true; end $$;

do $t$
declare g jsonb; g2 jsonb; r jsonb; n int; h text := repeat('a',64); h2 text := repeat('b',64); adm uuid := gen_random_uuid(); u uuid := gen_random_uuid();
begin
  -- grant + idempotency
  g  := public.service_grant_entitlement('MI-T1','cs_test_x','ext-l1','pdf','Buyer@X.com','files/ext-l1/v1/b.pdf','b.pdf','v1',null,repeat('n',43),h,now()+interval '14 days',5);
  g2 := public.service_grant_entitlement('MI-T1','cs_test_x','ext-l1','pdf','buyer@x.com','files/ext-l1/v1/b.pdf','b.pdf','v1',null,repeat('m',43),h2,now()+interval '14 days',5);
  perform pg_temp.expect((g->>'created')::boolean and not (g2->>'created')::boolean, 'second grant is not created');
  perform pg_temp.expect(g2->>'link_nonce' = repeat('n',43), 'repeat returns the original nonce');
  select count(*) into n from public.entitlements; perform pg_temp.expect(n = 1, 'one row');
  perform pg_temp.expect((select buyer_email from public.entitlements) = 'buyer@x.com', 'email lowercased');
  -- email lease
  perform pg_temp.expect(public.service_claim_email('cs_test_x'), 'first claim wins');
  perform pg_temp.expect(not public.service_claim_email('cs_test_x'), 'second claim loses');
  perform public.service_mark_emailed('cs_test_x');
  perform pg_temp.expect(not public.service_claim_email('cs_test_x'), 'no claim after emailed');
  -- download
  r := public.service_download_begin(h, 'ip1', true); perform pg_temp.expect(r->>'status' = 'ok' and (r->>'remaining')::int = 4, 'ok, 4 left');
  r := public.service_download_begin(h, 'ip1', false); perform pg_temp.expect(r->>'status' = 'ok', 'range after counted download is free');
  perform pg_temp.expect((select download_count from public.entitlements) = 1, 'range not counted');
  r := public.service_download_begin(repeat('c',64), 'ip1', true); perform pg_temp.expect(r->>'status' = 'not_found', 'unknown hash');
  update public.entitlements set download_count = 5; r := public.service_download_begin(h, 'ip2', true); perform pg_temp.expect(r->>'status' = 'exhausted', 'exhausted');
  update public.entitlements set download_count = 1, expires_at = now() - interval '1 second'; r := public.service_download_begin(h, 'ip2', true); perform pg_temp.expect(r->>'status' = 'expired', 'expired');
  update public.entitlements set expires_at = now() + interval '1 day', revoked_at = now(); r := public.service_download_begin(h, 'ip2', true); perform pg_temp.expect(r->>'status' = 'revoked', 'revoked');
  update public.entitlements set revoked_at = null, download_count = 0, last_download_at = null; r := public.service_download_begin(h, 'ip3', false); perform pg_temp.expect(r->>'status' = 'range_denied', 'range before any download');
  r := public.service_download_begin(h, 'ip3', true); perform public.service_download_release((r->>'entitlement_id')::uuid);
  perform pg_temp.expect((select download_count from public.entitlements) = 0, 'release gives it back');
  -- rate limit: 3 per window
  for i in 1..3 loop perform public.service_download_begin(repeat('d',64), 'ipR', true, 3, 10); end loop;
  r := public.service_download_begin(h, 'ipR', true, 3, 10); perform pg_temp.expect(r->>'status' = 'rate_limited', 'rate limited');
  perform pg_temp.expect(public.service_links_rate('ipL', 2, 10) and public.service_links_rate('ipL', 2, 10) and not public.service_links_rate('ipL', 2, 10), 'links rate');
  -- log keeps no email / raw ip
  perform pg_temp.expect(not exists (select 1 from public.delivery_log where ip_hash like '%@%'), 'no email in log');
  -- purge
  update public.delivery_log set at = now() - interval '100 days' where ip_hash = 'ip1';
  perform pg_temp.expect(public.service_purge_delivery_log(90) >= 1, 'purge removes old rows');
  -- admin functions: forbidden for non-admins, work for admin
  insert into auth.users (id, email) values (adm, 'a@x.com'), (u, 'u@x.com'); insert into public.admins (user_id) values (adm);
  perform set_config('request.jwt.claim.sub', u::text, true);
  perform pg_temp.expect(pg_temp.fails('select * from public.admin_list_entitlements()'), 'non-admin list refused');
  perform pg_temp.expect(pg_temp.fails($q$select public.admin_revoke_entitlement(gen_random_uuid())$q$), 'non-admin revoke refused');
  perform pg_temp.expect(pg_temp.fails($q$select public.admin_create_manual_entitlement('x','files/a/v1/a.pdf','a.pdf',null,repeat('z',43),repeat('e',64))$q$), 'non-admin create refused');
  perform set_config('request.jwt.claim.sub', adm::text, true);
  perform pg_temp.expect((select count(*) from public.admin_list_entitlements()) = 1, 'admin lists');
  r := public.admin_create_manual_entitlement('beta-workbook-l1','files/b/v1/b.pdf','b.pdf',null,repeat('z',43),repeat('e',64),14,5,'WhatsApp');
  perform pg_temp.expect(r->>'order_id' like 'MANUAL-%', 'manual order id');
  perform pg_temp.expect((select count(*) from public.admin_prepare_resend((r->>'id')::uuid, 30, true)) = 1, 'resend prepared');
  perform pg_temp.expect(public.admin_revoke_entitlement((r->>'id')::uuid, 'test'), 'revoked');
  perform pg_temp.expect((select count(*) from public.admin_prepare_resend((r->>'id')::uuid)) = 0, 'revoked cannot be resent');
  perform pg_temp.expect(public.admin_purge_delivery_log(90) >= 0, 'admin purge');
end $t$;

-- RLS: a logged-in user and anon cannot see or touch the tables, or call service functions
set role authenticated;
do $t$ begin
  perform pg_temp.expect(pg_temp.fails('select * from public.entitlements'), 'authenticated cannot select entitlements');
  perform pg_temp.expect(pg_temp.fails('select * from public.delivery_log'), 'authenticated cannot select log');
  perform pg_temp.expect(pg_temp.fails($q$select public.service_download_begin('x','y',true)$q$), 'authenticated cannot call service functions');
end $t$;
set role anon;
do $t$ begin
  perform pg_temp.expect(pg_temp.fails('select * from public.entitlements'), 'anon cannot select entitlements');
  perform pg_temp.expect(pg_temp.fails('select * from public.admin_list_entitlements()'), 'anon cannot call admin functions');
end $t$;
reset role;
\echo delivery_test.sql: all assertions passed
