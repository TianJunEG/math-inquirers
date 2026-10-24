-- AUDIT 01: who can execute / read what (catalog-level), SECURITY DEFINER hygiene, answer-key exposure. Local throwaway Postgres only.
\set ON_ERROR_STOP on
\i :HERE/audit_lib.sql
reset role;

-- 1. every function in public that PUBLIC/anon can execute must be on the reviewed allow-list
create temp table anon_ok(name text);
insert into anon_ok values ('child_sign_in'),('child_start_session'),('child_end_session'),('child_session_overview'),('list_ext_prices'),
  ('register_preview'),('cancel_preview'),('preview_open_sessions'),('submit_interest_request'),('submit_product_interest');
do $$ declare r record; bad text := ''; begin
  for r in select p.proname, p.oid from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'public' and p.prokind = 'f' loop
    if (has_function_privilege('anon', r.oid, 'EXECUTE') or has_function_privilege('public', r.oid, 'EXECUTE')) and r.proname not in (select name from anon_ok) then bad := bad || r.proname || ' '; end if;
  end loop;
  perform pg_temp.chk('anon/PUBLIC can execute only the reviewed allow-list of functions', bad = '', 'High', 'unexpected: ' || bad);
end $$;

-- 2. service_* and internal helpers: not executable by anon/authenticated
do $$ declare r record; bad text := ''; begin
  for r in select p.proname, p.oid from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'public' and p.prokind = 'f'
            and (p.proname like 'service\_%' or p.proname like '\_%') loop
    if has_function_privilege('authenticated', r.oid, 'EXECUTE') or has_function_privilege('anon', r.oid, 'EXECUTE') then bad := bad || r.proname || ' '; end if;
  end loop;
  perform pg_temp.chk('service_* and _internal functions are not executable by anon/authenticated', bad = '', 'High', 'exposed: ' || bad);
end $$;

-- 3. every SECURITY DEFINER function pins search_path
do $$ declare r record; bad text := ''; begin
  for r in select p.proname, p.proconfig from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'public' and p.prosecdef loop
    if r.proconfig is null or not exists (select 1 from unnest(r.proconfig) c where c like 'search_path=%') then bad := bad || r.proname || ' '; end if;
  end loop;
  perform pg_temp.chk('every SECURITY DEFINER function sets search_path', bad = '', 'High', 'missing: ' || bad);
end $$;
-- 3b. informational: pg_temp is not listed last (temp-table shadowing). Exploitable only with a raw SQL connection; PostgREST cannot create temp tables.
do $$ declare n int; begin
  select count(*) into n from pg_proc p join pg_namespace ns on ns.oid = p.pronamespace where ns.nspname = 'public' and p.prosecdef
     and not exists (select 1 from unnest(p.proconfig) c where c like '%pg_temp%');
  perform pg_temp.chk('SECURITY DEFINER search_path ends with pg_temp (hardening; informational)', n = 0, 'Low', n || ' functions lack an explicit pg_temp at the end');
end $$;

-- 4. table privileges: the secret tables are not readable by any API role
do $$ declare t text; bad text := ''; begin
  foreach t in array array['practice_item_keys','practice_item_tags','practice_units','child_sessions','admins','tutors','deletion_requests','ext_prices','preview_config',
                           'preview_registrations','preview_attended','preview_attempts','preview_sessions','recordings','recording_views'] loop
    if has_table_privilege('anon', 'public.'||t, 'SELECT') or has_table_privilege('authenticated', 'public.'||t, 'SELECT') then bad := bad || t || ' '; end if;
  end loop;
  perform pg_temp.chk('secret/internal tables are not selectable by anon or authenticated', bad = '', 'High', 'readable: ' || bad);
end $$;
do $$ declare t text; bad text := ''; begin
  for t in select c.relname from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'public' and c.relkind = 'r' loop
    if t <> 'audit_ctx' and has_table_privilege('anon', 'public.'||t, 'INSERT,UPDATE,DELETE') then bad := bad || t || '(anon) '; end if;
    if t <> 'audit_ctx' and (has_table_privilege('authenticated', 'public.'||t, 'INSERT') or has_table_privilege('authenticated', 'public.'||t, 'DELETE')) then bad := bad || t || '(auth ins/del) '; end if;
  end loop;
  perform pg_temp.chk('no API role can INSERT/DELETE any table directly', bad = '', 'High', bad);
end $$;
do $$ declare t text; bad text := ''; begin
  for t in select c.relname from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'public' and c.relkind = 'r' loop
    if has_table_privilege('authenticated', 'public.'||t, 'UPDATE') and t not in ('parents','audit_ctx') then bad := bad || t || ' '; end if;
  end loop;
  perform pg_temp.chk('only parents is UPDATE-able by authenticated', bad = '', 'High', bad);
end $$;
do $$ declare t text; bad text := ''; begin
  for t in select c.relname from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'public' and c.relkind = 'r' and not c.relrowsecurity loop
    bad := bad || t || ' ';
  end loop;
  perform pg_temp.chk('RLS enabled on every public table', bad = '' or bad = 'audit_ctx ', 'High', 'no RLS: ' || bad);
end $$;
-- column grants on children: pin_hash / pin_failed / pin_locked_until never selectable
select pg_temp.chk('children.pin_hash/pin_failed/pin_locked_until not selectable by authenticated',
  not has_column_privilege('authenticated','public.children','pin_hash','SELECT') and not has_column_privilege('authenticated','public.children','pin_failed','SELECT')
  and not has_column_privilege('authenticated','public.children','pin_locked_until','SELECT'), 'High');
select pg_temp.chk('parents.update limited to full_name, phone (not id, email, family_code, deleted_at)',
  has_column_privilege('authenticated','public.parents','full_name','UPDATE') and not has_column_privilege('authenticated','public.parents','family_code','UPDATE')
  and not has_column_privilege('authenticated','public.parents','deleted_at','UPDATE') and not has_column_privilege('authenticated','public.parents','id','UPDATE')
  and not has_column_privilege('authenticated','public.parents','email','UPDATE'), 'High');

-- 5. the answer key cannot be read by any API role by any route (table, tags, function result)
select pg_temp.chk('anon cannot SELECT practice_item_keys', pg_temp.denied(pg_temp.as_('anon', null, 'select * from public.practice_item_keys')), 'High');
select pg_temp.chk('parent cannot SELECT practice_item_keys', pg_temp.denied(pg_temp.as_('authenticated', 'aaaaaaaa-0000-0000-0000-00000000000a', 'select * from public.practice_item_keys')), 'High');
select pg_temp.chk('tutor cannot SELECT practice_item_keys', pg_temp.denied(pg_temp.as_('authenticated', 'cccccccc-0000-0000-0000-00000000000c', 'select * from public.practice_item_keys')), 'High');
select pg_temp.chk('admin (as authenticated) cannot SELECT practice_item_keys directly', pg_temp.denied(pg_temp.as_('authenticated', 'eeeeeeee-0000-0000-0000-00000000000e', 'select * from public.practice_item_keys')), 'Low');
select pg_temp.chk('authenticated cannot call service_practice_keys', pg_temp.denied(pg_temp.as_('authenticated', 'aaaaaaaa-0000-0000-0000-00000000000a', $q$select public.service_practice_keys('x','hol-l1l01','v1')$q$)), 'High');
select pg_temp.chk('anon cannot call service_practice_keys', pg_temp.denied(pg_temp.as_('anon', null, $q$select public.service_practice_keys('x','hol-l1l01','v1')$q$)), 'High');
select pg_temp.chk('authenticated cannot call service_practice_record', pg_temp.denied(pg_temp.as_('authenticated', 'aaaaaaaa-0000-0000-0000-00000000000a', $q$select public.service_practice_record('x','hol-l1l01','v1',gen_random_uuid(),1,'[]')$q$)), 'High');
