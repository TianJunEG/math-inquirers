-- Assertions for interest_requests.sql (run after schema, policies, seed). Any failure raises and stops psql.
\set ON_ERROR_STOP on
create or replace function pg_temp.fails(sql text, expect text default null) returns boolean language plpgsql as $$
begin execute sql; return false;
exception when others then
  if expect is not null and sqlerrm not like '%'||expect||'%' then raise exception 'wrong error for [%]: got [%], wanted [%]', sql, sqlerrm, expect; end if;
  return true; end $$;
\i :HERE/../interest_requests.sql
\i :HERE/../interest_requests.sql
set role anon;
do $$ declare r jsonb; begin
  assert pg_temp.fails($q$select * from public.interest_requests$q$, 'permission denied'), 'anon cannot select';
  assert pg_temp.fails($q$insert into public.interest_requests (level,age_band,parent_first_name,contact_email,consent_version,other_time) values (1,'6-7','x','a@b.co','v','t')$q$, 'permission denied'), 'anon cannot insert directly';
  assert pg_temp.fails($q$select * from public.admin_interest_tally()$q$, 'permission denied'), 'anon cannot call tally';
  r := public.submit_interest_request(1,'6-7',array['R1','MON-PM'],array['sat'],null,'Mei','9123 4567',null,'hello',true,'privacy-test');
  assert r->>'status' = 'received', 'first insert';
  r := public.submit_interest_request(2,'8-9',array['R1'],'{}',null,'Mei','+65 9123 4567',null,null,true,'privacy-test');
  assert r->>'status' = 'already_received', 'same contact within a day (65 prefix normalised)';
  r := public.submit_interest_request(2,'8-9','{}','{}','Tue 4pm','Sam',null,'Sam@Example.com',null,true,'privacy-test');
  assert r->>'status' = 'received', 'email only';
  r := public.submit_interest_request(2,'8-9',array['R1'],'{}',null,'Bot','81234567',null,null,true,'v','http://spam');
  assert r->>'status' = 'received', 'honeypot looks successful';
  assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9',array['R1'],'{}',null,'A',null,null,null,true,'v')$q$, 'invalid_input'), 'no contact';
  assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9',array['R1'],'{}',null,'A','81111111',null,null,false,'v')$q$, 'consent_required'), 'no consent';
  assert pg_temp.fails($q$select public.submit_interest_request(7,'8-9',array['R1'],'{}',null,'A','81111111',null,null,true,'v')$q$, 'invalid_input'), 'bad level';
  assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9','{}','{}',null,'A','81111111',null,null,true,'v')$q$, 'invalid_input'), 'no time at all';
  assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9',array['R1; drop'],'{}',null,'A','81111111',null,null,true,'v')$q$, 'invalid_input'), 'bad slot id';
  assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9',array['R1'],'{}',null,repeat('a',41),'81111111',null,null,true,'v')$q$, 'invalid_input'), 'name too long';
  assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9',array['R1'],'{}',null,'A','123',null,null,true,'v')$q$, 'invalid_input'), 'short phone';
  assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9',array['R1'],'{}',null,'A',null,'not-an-email',null,true,'v')$q$, 'invalid_input'), 'bad email';
  assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9',array['R1'],'{}',null,'A','81111111',null,repeat('n',401),true,'v')$q$, 'invalid_input'), 'note too long';
end $$;
reset role;
do $$ begin
  assert (select count(*) from public.interest_requests) = 2, 'two rows stored (dupe and honeypot not stored)';
  assert (select contact_whatsapp from public.interest_requests where parent_first_name='Mei') = '91234567';
  assert (select contact_email from public.interest_requests where parent_first_name='Sam') = 'sam@example.com';
  assert (select expires_at - created_at from public.interest_requests limit 1) between interval '364 days' and interval '367 days', '12 month default retention';
end $$;
-- rate cap
insert into public.interest_requests (level,age_band,other_time,parent_first_name,contact_email,consent_version)
  select 1,'6-7','x','f',i||'@x.co','v' from generate_series(1,300) i;
set role anon;
do $$ begin assert pg_temp.fails($q$select public.submit_interest_request(2,'8-9',array['R1'],'{}',null,'A','81111112',null,null,true,'v')$q$, 'busy'), 'global hourly cap'; end $$;
reset role;
delete from public.interest_requests where parent_first_name='f';
-- admin
set role authenticated; select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-000000000001',false);
do $$ begin
  assert pg_temp.fails($q$select * from public.admin_interest_tally()$q$, 'forbidden'), 'non-admin refused';
  assert pg_temp.fails($q$select * from public.interest_requests$q$, 'permission denied'), 'authenticated cannot select';
  assert pg_temp.fails($q$select public.admin_purge_expired_interest_requests()$q$, 'forbidden');
end $$;
select set_config('request.jwt.claim.sub','cccccccc-0000-0000-0000-000000000003',false);
do $$ declare id1 uuid; begin
  assert (select n from public.admin_interest_tally() where level=1 and kind='slot' and key='R1') = 1;
  assert (select n from public.admin_interest_tally() where level=1 and kind='total') = 1;
  assert (select n from public.admin_interest_tally() where level=2 and kind='other') = 1;
  assert (select count(*) from public.admin_list_interest_requests()) = 2;
  select id into id1 from public.admin_list_interest_requests() where parent_first_name='Mei';
  perform public.admin_set_interest_status(id1,'contacted');
  assert (select status from public.admin_list_interest_requests() where id=id1) = 'contacted';
  assert pg_temp.fails(format($q$select public.admin_set_interest_status(%L,'bogus')$q$, id1), 'invalid_input');
  perform public.admin_delete_interest_request(id1);
  assert (select count(*) from public.admin_list_interest_requests()) = 1;
end $$;
reset role;
update public.interest_requests set expires_at = now() - interval '1 day';
set role authenticated; select set_config('request.jwt.claim.sub','cccccccc-0000-0000-0000-000000000003',false);
do $$ begin assert public.admin_purge_expired_interest_requests() = 1, 'purge deletes expired'; end $$;
reset role;
select 'interest tests passed' as result;
