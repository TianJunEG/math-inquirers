-- AUDIT 06: server-side marking cannot be forged by client flags; answer keys never leak through reports; submission integrity. Local throwaway Postgres only.
\set ON_ERROR_STOP on
\i :HERE/audit_lib.sql
reset role;
\set A 'aaaaaaaa-0000-0000-0000-00000000000a'
\set T1 'cccccccc-0000-0000-0000-00000000000c'
\set ADM 'eeeeeeee-0000-0000-0000-00000000000e'
delete from public.practice_submissions; delete from public.child_sessions;
update public.parents set deleted_at = null where email = 'pa@audit.test';
delete from public.consents where false;
set role authenticated; select set_config('request.jwt.claim.sub',:'A',false);
select public.record_consents('{"online_practice":true,"contact":true,"terms":true}','t9','p9'); reset role;
insert into public.child_sessions (child_id, token_hash, expires_at) select id, encode(extensions.digest('MIA2TOKEN_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','sha256'),'hex'), now()+interval '4 hours' from public.children where display_name='Mia';
create temp table th as select encode(extensions.digest('MIA2TOKEN_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','sha256'),'hex') h;
create or replace function pg_temp.rec(sid uuid, unit text, rev int, rows jsonb) returns jsonb language sql as $$ select public.service_practice_record((select h from th), unit, 'v1', sid, rev, rows) $$;

-- a client cannot choose a mark that disagrees with the item's marking mode
select pg_temp.chk('mark "right" on a self-checked item is rejected', pg_temp.rec(gen_random_uuid(),'hol-l1l01',1,'[{"item_id":"q3","marking_mode":"self","mark":"right"}]')->>'error' = 'bad_rows', 'High');
select pg_temp.chk('marking_mode lie (auto row for a self item) is rejected', pg_temp.rec(gen_random_uuid(),'hol-l1l01',1,'[{"item_id":"q3","marking_mode":"auto","mark":"right"}]')->>'error' = 'bad_rows', 'High');
select pg_temp.chk('unknown item id rejected', pg_temp.rec(gen_random_uuid(),'hol-l1l01',1,'[{"item_id":"zzz","marking_mode":"auto","mark":"right"}]')->>'error' = 'bad_rows', 'High');
select pg_temp.chk('invalid mark word rejected', pg_temp.rec(gen_random_uuid(),'hol-l1l01',1,'[{"item_id":"q1","marking_mode":"auto","mark":"perfect"}]')->>'error' = 'bad_rows', 'Medium');
select pg_temp.chk('more than 400 rows rejected', pg_temp.rec(gen_random_uuid(),'hol-l1l01',1,(select jsonb_agg('{"item_id":"q1","marking_mode":"auto","mark":"right"}'::jsonb) from generate_series(1,401)))->>'error' = 'bad_rows', 'Low');
select pg_temp.chk('rows not an array rejected', pg_temp.rec(gen_random_uuid(),'hol-l1l01',1,'{"a":1}')->>'error' = 'bad_rows', 'Low');
select pg_temp.chk('rev 0 and rev 201 rejected', pg_temp.rec(gen_random_uuid(),'hol-l1l01',0,'[]')->>'error' = 'bad_rows' and pg_temp.rec(gen_random_uuid(),'hol-l1l01',201,'[]')->>'error' = 'bad_rows', 'Low');
-- a duplicate item id within one submission
select pg_temp.as_('service_role',null,$q$select public.service_practice_record(encode(extensions.digest('MIA2TOKEN_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','sha256'),'hex'),'hol-l1l01','v1',gen_random_uuid(),1,'[{"item_id":"q1","marking_mode":"auto","mark":"right"},{"item_id":"q1","marking_mode":"auto","mark":"wrong"}]')$q$) as r \gset
select pg_temp.chk('duplicate item ids in one submission are rejected cleanly (bad_rows), not an unhandled constraint error', :'r' like 'ok:%' and (select count(*) from public.practice_submissions)=0, 'Low', :'r');
delete from public.practice_submissions;
-- counts come from the rows only
select pg_temp.rec('00000000-0000-0000-0000-0000000000c1','hol-l1l01',1,'[{"item_id":"q1","marking_mode":"auto","mark":"wrong","answered":true,"answer_text":"7","slip_idx":0},{"item_id":"q2","marking_mode":"auto","mark":"skipped","answered":false},{"item_id":"q3","marking_mode":"self","mark":"self","answered":true,"self_result":"got"}]') as r \gset
select pg_temp.chk('counts are recomputed from the stored rows (auto 2, right 0, wrong 1, skipped 1, self 1, self_got 1)', (select n_auto=2 and n_right=0 and n_wrong=1 and n_skipped=1 and n_self=1 and n_self_got=1 from public.practice_submissions), 'High');
select pg_temp.rec('00000000-0000-0000-0000-0000000000c1','hol-l1l01',1,'[{"item_id":"q1","marking_mode":"auto","mark":"right","answered":true}]') as r \gset
select pg_temp.chk('replay of the same rev is a duplicate and changes nothing', (:'r'::jsonb)->>'duplicate' = 'true' and (select n_wrong from public.practice_submissions)=1, 'Medium');
select pg_temp.rec('00000000-0000-0000-0000-0000000000c1','hol-l1l01',0,'[]') as r \gset
select pg_temp.rec('00000000-0000-0000-0000-0000000000c1','hol-l1l01',2,'[{"item_id":"q1","marking_mode":"auto","mark":"right","answered":true,"answer_text":"9"}]') as r \gset
select pg_temp.rec('00000000-0000-0000-0000-0000000000c1','hol-l1l01',1,'[{"item_id":"q1","marking_mode":"auto","mark":"wrong","answered":true}]') as r2 \gset
select pg_temp.chk('higher rev replaces; a stale lower rev afterwards cannot overwrite', (select n_right=1 and n_wrong=0 and rev=2 from public.practice_submissions) and (:'r2'::jsonb)->>'stale' = 'true', 'Medium');
-- SID reuse across units
select pg_temp.rec('00000000-0000-0000-0000-0000000000c1','hol-l1l01',3,'[{"item_id":"q1","marking_mode":"auto","mark":"right","answered":true}]') as r \gset
delete from public.practice_submissions;
select pg_temp.rec('00000000-0000-0000-0000-0000000000c2','hol-l1l01',1,'[{"item_id":"q1","marking_mode":"auto","mark":"right","answered":true}]') as r \gset
insert into public.child_book_access (child_id, level, format, source) select id,1,'online','admin' from public.children where display_name='Mia';
select pg_temp.rec('00000000-0000-0000-0000-0000000000c2','ext-l1u01',2,'[{"item_id":"q1","marking_mode":"auto","mark":"wrong","answered":true}]') as r \gset
select pg_temp.chk('reusing one client_sid for a DIFFERENT unit is refused (submission.unit_key must match)', (select count(*) from public.practice_submissions s where s.unit_key='hol-l1l01' and exists (select 1 from public.practice_attempts a where a.submission_id=s.id and a.lesson_key='ext-l1u01')) = 0, 'Medium',
  'result of 2nd call: ' || (:'r')::text || '. service_practice_record looks the submission up by (child, client_sid) only; the second call replaces the rows with another unit''s rows while submissions.unit_key stays the first unit; reports then join the wrong tags. The Worker takes unit and sid both from the browser body');
delete from public.child_book_access where source='admin' and child_id=(select id from public.children where display_name='Mia');
delete from public.practice_submissions;

-- ===== the answer key never appears in any report output =====
select pg_temp.rec(gen_random_uuid(),'hol-l1l01',1,'[{"item_id":"q1","marking_mode":"auto","mark":"wrong","answered":true,"answer_text":"7","slip_idx":0},{"item_id":"q2","marking_mode":"auto","mark":"right","answered":true,"answer_text":"20"},{"item_id":"q3","marking_mode":"self","mark":"self","answered":true,"self_result":"not_yet"}]') as r \gset
create temp table leak(src text, body text);
insert into leak select 'child_detail(parent)', pg_temp.val('authenticated',:'A',$q$select coalesce(jsonb_agg(d)::text,'') from public.practice_child_detail((select mia from public.audit_ctx),'hol-l1l01') d$q$);
insert into leak select 'child_detail(tutor)', pg_temp.val('authenticated',:'T1',$q$select coalesce(jsonb_agg(d)::text,'') from public.practice_child_detail((select mia from public.audit_ctx),'hol-l1l01') d$q$);
insert into leak select 'tutor_group_practice', pg_temp.val('authenticated',:'T1',$q$select coalesce(jsonb_agg(d)::text,'') from public.tutor_group_practice('L1A') d$q$);
insert into leak select 'tutor_group_skill_report', pg_temp.val('authenticated',:'T1',$q$select coalesce(jsonb_agg(d)::text,'') from public.tutor_group_skill_report('L1A','hol-l1l01') d$q$);
insert into leak select 'tutor_group_slips', pg_temp.val('authenticated',:'T1',$q$select coalesce(jsonb_agg(d)::text,'') from public.tutor_group_slips('L1A','hol-l1l01') d$q$);
insert into leak select 'my_children_progress', pg_temp.val('authenticated',:'A',$q$select coalesce(jsonb_agg(d)::text,'') from public.my_children_progress() d$q$);
insert into leak select 'admin_practice_overview', pg_temp.val('authenticated',:'ADM',$q$select coalesce(jsonb_agg(d)::text,'') from public.admin_practice_overview() d$q$);
insert into leak select 'practice_attempts(parent)', pg_temp.val('authenticated',:'A',$q$select coalesce(jsonb_agg(d)::text,'') from public.practice_attempts d$q$);
insert into leak select 'practice_submissions(tutor)', pg_temp.val('authenticated',:'T1',$q$select coalesce(jsonb_agg(d)::text,'') from public.practice_submissions d$q$);
select pg_temp.chk('no report function returns the secret answer ("SECRET-ANSWER-9") or the key column', not exists (select 1 from leak where body like '%SECRET-ANSWER-9%' or body like '%answer_key%'), 'High', (select string_agg(src, ',') from leak where body like '%SECRET-ANSWER-9%'));
select pg_temp.chk('reports returned data (the leak test is not vacuous)', (select count(*) from leak where length(body) > 5) >= 7, 'Low', (select string_agg(src||':'||length(body), ',') from leak));
select pg_temp.chk('tutor report shows the slip text but NOT the right answer for a wrong item', (select body from leak where src='child_detail(tutor)') like '%Count the tens first%', 'Low');
select pg_temp.chk('parent report has no scores/percentages/ranks fields (my_children_progress)', (select body from leak where src='my_children_progress') !~* '(percent|score|rank|streak|n_right|n_wrong)', 'Medium',
  'my_children_progress itself returns no right/wrong; practice_child_detail returns per-item mark right/wrong to the parent, and the parent direct table read practice_attempts exposes correct=true/false per item');
select pg_temp.note('parent can read per-question right/wrong (practice_child_detail, practice_attempts.correct); the UI shows only "worth looking at together" text, but the API returns every mark and the wrong answer_text', 'Low', 'fine for the owner design ("reports"), only matters for the "no scores" wording promise to children, who cannot call these');

-- ===== the HTTP Worker contract: what the browser may learn after Submit (read from practice/submit/handler.js, not SQL) =====
select pg_temp.note('Worker reply returns marks (right/wrong/skipped) for every item after each Submit and up to 200 revisions of one sid are allowed: a child (or script) can discover the answer key by submit/adjust/resubmit', 'Low', 'inherent in instant marking; rate limit is 20 distinct submissions per hour per child, not per revision. Decide whether marks should be shown only after a final submit');
