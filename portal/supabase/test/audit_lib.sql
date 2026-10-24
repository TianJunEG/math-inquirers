-- shared helpers, \i'd by each audit file. pg_temp functions live for one psql session.
create or replace function pg_temp.chk(name text, ok boolean, sev text default 'Medium', note text default '') returns void language plpgsql as $$
begin raise notice 'AUDIT|%|%|%', case when ok then 'PASS' else 'FAIL' end, sev, name || case when note = '' then '' else ' -- ' || note end; end $$;
-- run one statement as a role + jwt subject; returns 'ok:<rows>' or 'err:<sqlstate>:<message>'
create or replace function pg_temp.as_(r text, uid text, q text) returns text language plpgsql as $$
declare n bigint; res text;
begin
  execute format('set local role %I', r);
  perform set_config('request.jwt.claim.sub', coalesce(uid,''), true);
  begin execute q; get diagnostics n = row_count; res := 'ok:' || n;
  exception when others then res := 'err:' || sqlstate || ':' || left(sqlerrm, 200); end;
  reset role;
  return res;
end $$;
-- same, but returns the first column of the first row as text
create or replace function pg_temp.val(r text, uid text, q text) returns text language plpgsql as $$
declare v text; res text;
begin
  execute format('set local role %I', r);
  perform set_config('request.jwt.claim.sub', coalesce(uid,''), true);
  begin execute q into v; res := coalesce(v, '<null>');
  exception when others then res := 'err:' || sqlstate || ':' || left(sqlerrm, 200); end;
  reset role;
  return res;
end $$;
create or replace function pg_temp.denied(res text) returns boolean language sql immutable as $$ select res like 'err:%' $$;
create or replace function pg_temp.zero(res text) returns boolean language sql immutable as $$ select res = 'ok:0' or res like 'err:%' $$;

create or replace function pg_temp.note(name text, sev text default 'Low', detail text default '') returns void language plpgsql as $$
begin raise notice 'AUDIT|NOTE|%|%', sev, name || case when detail = '' then '' else ' -- ' || detail end; end $$;
