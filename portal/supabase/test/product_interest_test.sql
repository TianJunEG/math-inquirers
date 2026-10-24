-- Assertions for product_interest.sql (run after schema, policies, seed and rls_test, like interest_test.sql). Any failure raises and stops psql.
\set ON_ERROR_STOP on
create or replace function pg_temp.fails(sql text, expect text default null) returns boolean language plpgsql as $$
begin execute sql; return false;
exception when others then
  if expect is not null and sqlerrm not like '%'||expect||'%' then raise exception 'wrong error for [%]: got [%], wanted [%]', sql, sqlerrm, expect; end if;
  return true; end $$;
\i :HERE/../product_interest.sql
\i :HERE/../product_interest.sql
set role anon;
do $$ declare r jsonb; begin
  assert pg_temp.fails($q$select * from public.product_interest$q$, 'permission denied'), 'anon cannot select';
  assert pg_temp.fails($q$insert into public.product_interest (parent_first_name,contact_email,items,consent_version) values ('x','a@b.co','[{"product":"ext-l1","format":"soft","qty":1}]','v')$q$, 'permission denied'), 'anon cannot insert directly';
  assert pg_temp.fails($q$select * from public.admin_product_interest_tally()$q$, 'permission denied'), 'anon cannot call tally';
  r := public.submit_product_interest('Mei','9123 4567',null,'[{"product":"ext-l1","format":"soft","qty":1},{"product":"ext-l3","format":"physical","qty":2}]','hello',true,'privacy-test');
  assert r->>'status' = 'received', 'first insert';
  r := public.submit_product_interest('Mei','+65 9123 4567',null,'[{"product":"ext-l2","format":"soft","qty":1}]',null,true,'privacy-test');
  assert r->>'status' = 'already_received', 'same contact within a day (65 prefix normalised)';
  r := public.submit_product_interest('Sam',null,'Sam@Example.com','[{"product":"ext-l1","format":"soft","qty":5},{"product":"ext-l1","format":"soft","qty":1},{"product":"ext-l3","format":"physical","qty":1},{"product":"ext-l3","format":"physical","qty":4}]',null,true,'privacy-test');
  assert r->>'status' = 'received', 'email only, duplicate lines merged';
  r := public.submit_product_interest('Bot','81234567',null,'[{"product":"ext-l1","format":"soft","qty":1}]',null,true,'v','http://spam');
  assert r->>'status' = 'received', 'honeypot looks successful';
  assert pg_temp.fails($q$select public.submit_product_interest('A',null,null,'[{"product":"ext-l1","format":"soft","qty":1}]',null,true,'v')$q$, 'invalid_input'), 'no contact';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[{"product":"ext-l1","format":"soft","qty":1}]',null,false,'v')$q$, 'consent_required'), 'no consent';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[]',null,true,'v')$q$, 'invalid_input'), 'no items';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,null,null,true,'v')$q$, 'invalid_input'), 'null items';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'{"product":"ext-l1"}',null,true,'v')$q$, 'invalid_input'), 'items not an array';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[{"product":"EXT; drop","format":"soft","qty":1}]',null,true,'v')$q$, 'invalid_input'), 'bad product id';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[{"product":"ext-l1","format":"hardback","qty":1}]',null,true,'v')$q$, 'invalid_input'), 'bad format';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[{"product":"ext-l1","format":"physical","qty":11}]',null,true,'v')$q$, 'invalid_input'), 'qty too high';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[{"product":"ext-l1","format":"physical","qty":0}]',null,true,'v')$q$, 'invalid_input'), 'qty zero';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[{"product":"ext-l1","format":"physical","qty":"2"}]',null,true,'v')$q$, 'invalid_input'), 'qty not a number';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[{"product":"ext-l1","format":"soft","qty":1,"price":1}]',null,true,'v')$q$, null) = false, 'extra keys are ignored, never stored';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111112',null,(select jsonb_agg(jsonb_build_object('product','p'||i,'format','soft','qty',1)) from generate_series(1,13) i),null,true,'v')$q$, 'invalid_input'), 'too many items';
  assert pg_temp.fails($q$select public.submit_product_interest(repeat('a',41),'81111111',null,'[{"product":"ext-l1","format":"soft","qty":1}]',null,true,'v')$q$, 'invalid_input'), 'name too long';
  assert pg_temp.fails($q$select public.submit_product_interest('A','123',null,'[{"product":"ext-l1","format":"soft","qty":1}]',null,true,'v')$q$, 'invalid_input'), 'short phone';
  assert pg_temp.fails($q$select public.submit_product_interest('A',null,'not-an-email','[{"product":"ext-l1","format":"soft","qty":1}]',null,true,'v')$q$, 'invalid_input'), 'bad email';
  assert pg_temp.fails($q$select public.submit_product_interest('A','81111111',null,'[{"product":"ext-l1","format":"soft","qty":1}]',repeat('n',401),true,'v')$q$, 'invalid_input'), 'note too long';
end $$;
reset role;
do $$ begin
  assert (select count(*) from public.product_interest where parent_first_name in ('Mei','Sam')) = 2, 'Mei and Sam stored (dupe and honeypot not stored)';
  assert (select count(*) from public.product_interest) = 3, 'plus the one "A" row from the extra-keys check';
  assert (select contact_whatsapp from public.product_interest where parent_first_name='Mei') = '91234567';
  assert (select contact_email from public.product_interest where parent_first_name='Sam') = 'sam@example.com';
  assert (select expires_at - created_at from public.product_interest limit 1) between interval '364 days' and interval '367 days', '12 month default retention';
  assert (select items from public.product_interest where parent_first_name='A') = '[{"qty": 1, "format": "soft", "product": "ext-l1"}]'::jsonb, 'extra keys such as price are dropped';
  assert (select jsonb_array_length(items) from public.product_interest where parent_first_name='Sam') = 2, 'duplicate lines merged';
  assert (select (items->1->>'qty')::int from public.product_interest where parent_first_name='Sam') = 4, 'merged physical qty is the larger one';
end $$;
delete from public.product_interest where parent_first_name='A';
-- rate cap
insert into public.product_interest (parent_first_name,contact_email,items,consent_version)
  select 'f',i||'@x.co','[{"product":"ext-l1","format":"soft","qty":1}]','v' from generate_series(1,300) i;
set role anon;
do $$ begin assert pg_temp.fails($q$select public.submit_product_interest('A','81111112',null,'[{"product":"ext-l1","format":"soft","qty":1}]',null,true,'v')$q$, 'busy'), 'global hourly cap'; end $$;
reset role;
delete from public.product_interest where parent_first_name='f';
-- admin
set role authenticated; select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-000000000001',false);
do $$ begin
  assert pg_temp.fails($q$select * from public.admin_product_interest_tally()$q$, 'forbidden'), 'non-admin refused';
  assert pg_temp.fails($q$select * from public.product_interest$q$, 'permission denied'), 'authenticated cannot select';
  assert pg_temp.fails($q$select public.admin_purge_expired_product_interest()$q$, 'forbidden');
end $$;
select set_config('request.jwt.claim.sub','cccccccc-0000-0000-0000-000000000003',false);
do $$ declare id1 uuid; begin
  assert (select requests from public.admin_product_interest_tally() where product='*') = 2, 'total requests';
  assert (select requests from public.admin_product_interest_tally() where product='ext-l1' and format='soft') = 2;
  assert (select copies from public.admin_product_interest_tally() where product='ext-l3' and format='physical') = 6, 'copies: 2 + 4';
  assert (select count(*) from public.admin_list_product_interest()) = 2;
  select id into id1 from public.admin_list_product_interest() where parent_first_name='Mei';
  perform public.admin_set_product_interest_status(id1,'notified');
  assert (select status from public.admin_list_product_interest() where id=id1) = 'notified';
  assert pg_temp.fails(format($q$select public.admin_set_product_interest_status(%L,'bogus')$q$, id1), 'invalid_input');
  perform public.admin_delete_product_interest(id1);
  assert (select count(*) from public.admin_list_product_interest()) = 1;
end $$;
reset role;
update public.product_interest set expires_at = now() - interval '1 day';
set role authenticated; select set_config('request.jwt.claim.sub','cccccccc-0000-0000-0000-000000000003',false);
do $$ begin assert public.admin_purge_expired_product_interest() = 1, 'purge deletes expired'; end $$;
reset role;
select 'product interest tests passed' as result;
