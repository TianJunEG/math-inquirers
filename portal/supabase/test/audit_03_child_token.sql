-- AUDIT 03: child sessions (tokens), PIN brute force, replay, expiry, injection in text inputs. Local throwaway Postgres only.
\set ON_ERROR_STOP on
\i :HERE/audit_lib.sql
reset role;
select set_config('audit.code_a', (select code_a from public.audit_ctx), false), set_config('audit.code_b', (select code_b from public.audit_ctx), false);

-- ===== sign-in basics =====
create temp table tok(who text primary key, token text, child uuid);
grant all on tok to anon, authenticated;
set role anon; select set_config('request.jwt.claim.sub','',false);
insert into tok select 'mia', token, child_id from public.child_start_session(current_setting('audit.code_a'), 'Mia', '1234');
reset role;
select pg_temp.chk('Mia can start a session with correct code/name/PIN', (select count(*) from tok where who='mia') = 1, 'High');
select pg_temp.chk('token is stored only as a SHA-256 hash (no plaintext token in child_sessions)', not exists (select 1 from public.child_sessions s, tok t where s.token_hash = t.token), 'High');
select pg_temp.chk('token is long and URL-safe (43 chars, 256 bits)', (select length(token) from tok where who='mia') >= 43 and (select token from tok where who='mia') ~ '^[A-Za-z0-9_-]+$', 'Medium');
select pg_temp.chk('overview with a random/garbage token returns null', pg_temp.val('anon',null,$q$select public.child_session_overview(repeat('a',43))$q$) = '<null>', 'High');
select pg_temp.chk('overview with a malformed token returns null (no SQL error)', pg_temp.val('anon',null,$q$select public.child_session_overview($$x'; drop table public.children;--$$)$q$) = '<null>', 'High');
select pg_temp.chk('overview with Mia''s token returns Mia only', pg_temp.val('anon',null,format($q$select public.child_session_overview(%L)->>'name'$q$, (select token from tok where who='mia'))) = 'Mia', 'High');
select pg_temp.chk('overview does not contain pin, parent id/email, family code, birth year, answer keys',
  pg_temp.val('anon',null,format($q$select (public.child_session_overview(%L))::text ~* '(pin|parent|email|family|birth|answer_key|SECRET)'$q$, (select token from tok where who='mia'))) = 'false', 'High');
select pg_temp.chk('Mia''s overview lists her entitled unit (holiday L1) and not B''s or other levels', pg_temp.val('anon',null,format($q$select string_agg(u->>'unit_key', ',' order by u->>'unit_key') from jsonb_array_elements(public.child_session_overview(%L)->'units') u$q$, (select token from tok where who='mia'))) = 'hol-l1l01', 'Medium');
-- sibling Kai (same parent, not himself enrolled, no book): D2-ENROLLED opens holiday/term for ANY child of an enrolled family. Informational check of the actual rule.
select pg_temp.note('sibling Kai (not enrolled himself) gets the holiday unit through Mia''s enrolment: ' || (select count(*) from public._child_units((select kai from public.audit_ctx)))::text || ' unit(s)', 'Low', 'D2 rule is family-level for enrolled; owner should confirm this is intended');
select pg_temp.chk('Kai gets NO extension unit from a purchase for another child', (select count(*) from public._child_units((select kai from public.audit_ctx)) where product='extension') = 0, 'High');
select pg_temp.chk('Ben (family B, online book L1) gets ext L1 units but not the holiday unit and not L2', (select string_agg(unit_key, ',' order by unit_key) from public._child_units((select ben from public.audit_ctx))) = 'ext-l1u01,ext-l1u02', 'High');
select pg_temp.chk('unpublished and open sample units never offered', not exists (select 1 from public._child_units((select ben from public.audit_ctx)) where unit_key in ('ext-l1u03','smp-l1u01')), 'Medium');

-- ===== token lifecycle =====
create temp table h2(h text); insert into h2 select encode(extensions.digest((select token from tok where who='mia'),'sha256'),'hex');
select pg_temp.chk('service keys accept a live token', (public.service_practice_keys((select h from h2),'hol-l1l01','v1')->>'ok') = 'true', 'High');
-- expiry
update public.child_sessions set expires_at = now() - interval '1 second' where token_hash = (select h from h2);
select pg_temp.chk('expired token: overview null', pg_temp.val('anon',null,format($q$select public.child_session_overview(%L)$q$, (select token from tok where who='mia'))) = '<null>', 'High');
select pg_temp.chk('expired token: service keys refuse (session)', public.service_practice_keys((select h from h2),'hol-l1l01','v1')->>'error' = 'session', 'High');
select pg_temp.chk('expired token: service record refuses (session)', public.service_practice_record((select h from h2),'hol-l1l01','v1',gen_random_uuid(),1,'[]')->>'error' = 'session', 'High');
update public.child_sessions set expires_at = now() + interval '4 hours' where token_hash = (select h from h2);
-- revoke via end session
select pg_temp.as_('anon',null,format($q$select public.child_end_session(%L)$q$, (select token from tok where who='mia'))) as r \gset
select pg_temp.chk('child_end_session by token revokes it', :'r' = 'ok:1' and public.service_practice_keys((select h from h2),'hol-l1l01','v1')->>'error' = 'session', 'High');
-- replay a revoked token
select pg_temp.chk('replay of a revoked token fails (overview null)', pg_temp.val('anon',null,format($q$select public.child_session_overview(%L)$q$, (select token from tok where who='mia'))) = '<null>', 'High');
-- anyone holding the token can end it (bearer): informational
-- token tied to a deleted/deactivated parent
update public.child_sessions set revoked_at = null where token_hash = (select h from h2);
update public.parents set deleted_at = now() where email = 'pa@audit.test';
select pg_temp.chk('token of a deleted-parent family stops working', public.service_practice_keys((select h from h2),'hol-l1l01','v1')->>'error' = 'session', 'High');
update public.parents set deleted_at = null where email = 'pa@audit.test';
-- consent withdrawal stops sessions and submissions at once
set role authenticated; select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-00000000000a',false);
select public.record_consents('{"online_practice":false}','t2','p2');
reset role;
select pg_temp.chk('withdrawing online_practice: existing token cannot fetch keys (consent)', public.service_practice_keys((select h from h2),'hol-l1l01','v1')->>'error' = 'consent', 'High');
select pg_temp.chk('withdrawing online_practice: no new child session', (select count(*) from (select * from public.child_start_session(current_setting('audit.code_a'),'Mia','1234')) s) = 0, 'High');
select pg_temp.chk('withdrawing online_practice: overview says can_submit=false (and still lists units)', pg_temp.val('anon',null,format($q$select public.child_session_overview(%L)->>'can_submit'$q$, (select token from tok where who='mia'))) = 'false', 'Low');
set role authenticated; select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-00000000000a',false);
select public.record_consents('{"online_practice":true}','t3','p3');
reset role;
-- token cross-use: Mia's token must not reach Ben's units
select pg_temp.chk('Mia''s token cannot fetch keys for an extension unit she has not bought (entitlement)', public.service_practice_keys((select h from h2),'ext-l1u01','v1')->>'error' = 'entitlement', 'High');
select pg_temp.chk('Mia''s token cannot record to an unentitled unit', public.service_practice_record((select h from h2),'ext-l2u01','v1',gen_random_uuid(),1,'[{"item_id":"q1","marking_mode":"auto","mark":"right"}]')->>'error' = 'entitlement', 'High');
select pg_temp.chk('open sample unit: keys refuse (stores nothing)', public.service_practice_keys((select h from h2),'smp-l1u01','v1')->>'error' = 'unit', 'Medium');
select pg_temp.chk('unpublished unit: keys refuse', public.service_practice_keys((select h from h2),'ext-l1u03','v1')->>'error' = 'unit', 'Medium');
select pg_temp.chk('unknown unit: keys refuse', public.service_practice_keys((select h from h2),'nope','v1')->>'error' = 'unit', 'Low');

-- ===== PIN brute force / lockout =====
create or replace function pg_temp.try_pin(code text, nm text, pin text) returns int language sql as $$ select count(*)::int from public.child_start_session(code, nm, pin) $$;
do $$ declare i int; ok int := 0; code text := current_setting('audit.code_a'); begin
  for i in 1..5 loop perform pg_temp.try_pin(code, 'Kai', '000' || i); end loop;
  perform pg_temp.chk('5 wrong PINs lock the child (pin_locked_until set)', (select pin_locked_until > now() from public.children where display_name = 'Kai'), 'High');
  perform pg_temp.chk('while locked even the correct PIN is refused', pg_temp.try_pin(code, 'Kai', '2468') = 0, 'High');
  perform pg_temp.chk('locked: case/space variations of the name do not bypass the lock', pg_temp.try_pin(code, '  kAI ', '2468') = 0 and pg_temp.try_pin(lower(code), 'KAI', '2468') = 0, 'High');
  update public.children set pin_locked_until = now() - interval '1 second' where display_name = 'Kai';
  perform pg_temp.chk('after the lock expires the correct PIN works', pg_temp.try_pin(code, 'Kai', '2468') = 1, 'Medium');
  -- does the lockout escalate? lock a second time right after the first lock expired and compare the lock length
  update public.children set pin_failed = 0, pin_locked_until = null where display_name = 'Kai';
  for i in 1..5 loop perform pg_temp.try_pin(code, 'Kai', '999' || i); end loop;
  update public.children set pin_locked_until = now() - interval '1 second' where display_name = 'Kai';
  for i in 1..5 loop perform pg_temp.try_pin(code, 'Kai', '888' || i); end loop;
  perform pg_temp.chk('PIN lockout escalates after repeated lock cycles (stays 15 min flat otherwise: 20 guesses/hour/child for ever)',
     (select pin_locked_until > now() + interval '16 minutes' from public.children where display_name='Kai'), 'Medium',
     'a 4-digit PIN falls in at most ~500 hours of patient guessing; a griefer who knows family code + name can keep a child locked out. Suggest escalating lock (15 min, 1 h, 24 h) and an email to the parent');
  update public.children set pin_failed = 0, pin_locked_until = null where display_name = 'Kai';
end $$;
select pg_temp.chk('unknown family code and unknown name give the same empty result as a wrong PIN', pg_temp.try_pin('ZZZZZZ','Mia','1234') = 0 and pg_temp.try_pin(current_setting('audit.code_a'),'Nobody','1234') = 0, 'Medium');
select pg_temp.chk('a PIN from the OTHER family does not work (Ben''s PIN on Mia)', pg_temp.try_pin(current_setting('audit.code_a'),'Mia','4321') = 0, 'High');
select pg_temp.chk('child_start_session does not allow a name in family A to sign in with B''s code', pg_temp.try_pin(current_setting('audit.code_b'),'Mia','1234') = 0, 'High');
select pg_temp.chk('child_sign_in: PIN with SQL metacharacters is just a wrong PIN', pg_temp.try_pin(current_setting('audit.code_a'),'Mia', $$1234' or '1'='1$$) = 0 and pg_temp.try_pin(current_setting('audit.code_a'), $$Mia' or '1'='1$$, '1234') = 0, 'High');
select pg_temp.chk('wildcards in the name do not match (LIKE injection)', pg_temp.try_pin(current_setting('audit.code_a'),'%','1234') = 0 and pg_temp.try_pin(current_setting('audit.code_a'),'M_a','1234') = 0, 'High');
select pg_temp.chk('NULL arguments do not sign anyone in', pg_temp.try_pin(null,null,null) = 0 and pg_temp.try_pin(current_setting('audit.code_a'),'Mia',null) = 0, 'High');
-- family code enumeration: how guessable?
select pg_temp.note('family code space: 6 chars from a 31-letter alphabet (~887M); no per-IP throttle exists in SQL', 'Low', 'rely on Supabase API rate limits / Cloudflare; the code alone gives nothing without name + PIN');

-- ===== session count limit =====
do $$ declare i int; begin
  for i in 1..8 loop perform pg_temp.try_pin(current_setting('audit.code_a'),'Mia','1234'); end loop;
  perform pg_temp.chk('at most 5 live sessions per child', (select count(*) from public.child_sessions s join public.children c on c.id=s.child_id where c.display_name='Mia' and s.revoked_at is null and s.expires_at > now()) <= 5, 'Low');
end $$;

-- ===== rate limit on submissions (20 per child per hour) =====
do $$ declare i int; th text := (select encode(extensions.digest(token,'sha256'),'hex') from (select token from public.child_start_session(current_setting('audit.code_a'),'Mia','1234') limit 1) t); r jsonb; begin
  delete from public.practice_submissions where child_id = (select mia from public.audit_ctx);
  for i in 1..20 loop
    perform public.service_practice_record(th,'hol-l1l01','v1',gen_random_uuid(),1,'[{"item_id":"q1","marking_mode":"auto","mark":"right","answered":true,"answer_text":"9"}]');
  end loop;
  r := public.service_practice_keys(th,'hol-l1l01','v1');
  perform pg_temp.chk('21st request in an hour is rate limited', r->>'error' = 'rate', 'Medium');
  perform pg_temp.note('rate limit also blocks REVISIONS of an existing submission (child stuck after 20 units/hour)', 'Low', 'keys step refuses any call at 20 submissions, even rev 2 of an existing sid; acceptable for children, noted');
  perform pg_temp.note('service_practice_record has no rate limit of its own (relies on the Worker calling keys first)', 'Low', 'only service_role can call it, so not client-exploitable');
  delete from public.practice_submissions where child_id = (select mia from public.audit_ctx);
end $$;
