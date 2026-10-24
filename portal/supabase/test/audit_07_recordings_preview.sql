-- AUDIT 07: recordings.sql and preview_class.sql (both DRAFT, not applied): anonymous abuse, enumeration, access by non-enrolled parents. Local throwaway Postgres only.
\set ON_ERROR_STOP on
\i :HERE/audit_lib.sql
reset role;
\set A 'aaaaaaaa-0000-0000-0000-00000000000a'
\set B 'bbbbbbbb-0000-0000-0000-00000000000b'
\set ADM 'eeeeeeee-0000-0000-0000-00000000000e'

-- ===== recordings =====
insert into public.recordings (group_id, lesson_no, title, provider, provider_id, recorded_on, status, published_at, expires_at, review)
 values ('L1A', 1, 'Lesson 1: audit', 'stream', 'SECRETVIDEOUID123', current_date, 'published', now() - interval '1 day', now() + interval '20 days', '{"no_private_info":true,"no_child_names_faces":true,"on_topic":true}');
set role authenticated; select set_config('request.jwt.claim.sub',:'A',false);
select public.record_consents('{"recording":true}','t5','p5'); reset role;
select id as rid from public.recordings limit 1 \gset
select mia::text as mia_id, ben::text as ben_id from public.audit_ctx \gset
select pg_temp.chk('recordings: provider_id is not selectable from the table by any parent', pg_temp.denied(pg_temp.as_('authenticated',:'A','select provider_id from public.recordings')), 'High');
select pg_temp.as_('authenticated',:'A','select * from public.my_recordings()') as r1 \gset
select pg_temp.as_('authenticated',:'B','select * from public.my_recordings()') as r2 \gset
select pg_temp.chk('enrolled parent A sees the recording in my_recordings; non-enrolled parent B sees none', :'r1' = 'ok:1' and :'r2' = 'ok:0', 'High', :'r1' || ' ' || :'r2');
select pg_temp.as_('authenticated',:'B',format($q$select * from public.recording_playback(%L, %L)$q$, :'rid', :'mia_id')) as r \gset
select pg_temp.chk('non-enrolled parent B cannot get playback (even naming the child of A)', :'r' = 'ok:0', 'High', :'r');
select pg_temp.chk('anon cannot call playback or list', pg_temp.denied(pg_temp.as_('anon',null,format($q$select * from public.recording_playback(%L)$q$, :'rid'))) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.my_recordings()')), 'High');
select pg_temp.as_('authenticated',:'A',format($q$select * from public.recording_playback(%L, %L)$q$, :'rid', :'mia_id')) as r \gset
select pg_temp.chk('enrolled parent A gets playback and a view row is logged', :'r' = 'ok:1' and (select count(*) from public.recording_views) = 1, 'Medium', :'r');
select pg_temp.as_('authenticated',:'A',format($q$select * from public.recording_playback(%L, %L)$q$, :'rid', :'ben_id')) as r \gset
select pg_temp.chk('A cannot ask playback "as" Ben (other family child)', :'r' = 'ok:0', 'High', :'r');
set role authenticated; select set_config('request.jwt.claim.sub',:'A',false);
select public.record_consents('{"recording":false}','t6','p6'); reset role;
select pg_temp.as_('authenticated',:'A',format($q$select * from public.recording_playback(%L)$q$, :'rid')) as r \gset
select pg_temp.chk('withdrawing the recording consent stops playback at once', :'r' = 'ok:0', 'High', :'r');
select pg_temp.as_('authenticated','cccccccc-0000-0000-0000-00000000000c',format($q$select * from public.recording_playback(%L)$q$, :'rid')) as r \gset
select pg_temp.chk('a tutor (not enrolled) has no playback (design says add later)', :'r' = 'ok:0', 'Low', :'r');
select pg_temp.note('R1: delete_my_data() now deletes the parent''s recording_views rows (checked in audit_08)', 'Low');
set role authenticated; select set_config('request.jwt.claim.sub',:'A',false);
select public.record_consents('{"recording":true}','t7','p7'); reset role;

-- ===== preview class (anonymous) =====
select pg_temp.as_('authenticated',:'ADM',$q$select public.admin_preview_create_session(now() + interval '5 days','A',2,2)$q$) as r \gset
select pg_temp.chk('admin can create a preview session', :'r' like 'ok%', 'Low', :'r');
select id as sid from public.preview_sessions limit 1 \gset
select pg_temp.chk('anon can list open sessions (no counts, only is_full)', pg_temp.as_('anon',null,'select * from public.preview_open_sessions()') = 'ok:1', 'Low');
select pg_temp.chk('anon cannot read preview_registrations / attended / config / sessions', pg_temp.denied(pg_temp.as_('anon',null,'select * from public.preview_registrations')) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.preview_attended')) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.preview_config')) and pg_temp.denied(pg_temp.as_('anon',null,'select * from public.preview_sessions')), 'High');
select pg_temp.chk('authenticated parent cannot read preview tables or the pepper', pg_temp.denied(pg_temp.as_('authenticated',:'A','select * from public.preview_config')) and pg_temp.denied(pg_temp.as_('authenticated',:'A','select * from public.preview_registrations')), 'High');
select pg_temp.chk('anon cannot call admin_preview_* or read the check-in sheet', pg_temp.denied(pg_temp.as_('anon',null,format($q$select * from public.admin_preview_list(%L)$q$, :'sid'))) and pg_temp.denied(pg_temp.as_('anon',null,$q$select public.admin_preview_check('a@b.co',null,'Amy',2018)$q$)) and pg_temp.denied(pg_temp.as_('anon',null,$q$select public.admin_purge_preview()$q$)), 'High');
select pg_temp.chk('a parent (non admin) cannot call admin_preview_*', pg_temp.denied(pg_temp.as_('authenticated',:'A',format($q$select * from public.admin_preview_list(%L)$q$, :'sid'))) and pg_temp.denied(pg_temp.as_('authenticated',:'A',$q$select public.admin_preview_delete_person('a@b.co')$q$)), 'High');
select pg_temp.as_('anon',null,format($q$select public.register_preview(%L,'Pam','pam@audit.test','91234567','Amy',%s,'P1',true,true,true,true,false,'v1')$q$, :'sid', extract(year from now())::int - 6)) as r \gset
select pg_temp.chk('anon registration works', :'r' like 'ok%', 'Low', :'r');
select pg_temp.chk('marketing consent is stored false unless explicitly true (never pre-ticked)', (select consent_marketing from public.preview_registrations limit 1) = false, 'High');
select pg_temp.chk('registration without exclusion/terms/contact/parent_present consent is refused', pg_temp.denied(pg_temp.as_('anon',null,format($q$select public.register_preview(%L,'Pam','pam2@audit.test',null,'Bo',%s,'P1',true,true,false,true,false,'v1')$q$, :'sid', extract(year from now())::int - 6))), 'High');
select pg_temp.chk('SQL injection / HTML in names and email is stored literally or refused, never executed', pg_temp.as_('anon',null,format($q$select public.register_preview(%L,$$<b>x</b>'); drop table public.parents;--$$,'inj@audit.test',null,$$Rob'); drop table public.children;--$$,%s,'P1',true,true,true,true,false,'v1')$q$, :'sid', extract(year from now())::int - 6)) is not null and to_regclass('public.parents') is not null and to_regclass('public.children') is not null, 'High');
select pg_temp.chk('error messages are fixed words (no input echo) for bad email', pg_temp.as_('anon',null,format($q$select public.register_preview(%L,'Pam','not-an-email<script>',null,'Cy',%s,'P1',true,true,true,true,false,'v1')$q$, :'sid', extract(year from now())::int - 6)) not like '%script%', 'Medium');
select pg_temp.chk('birth year outside 2008-2022 refused', pg_temp.denied(pg_temp.as_('anon',null,format($q$select public.register_preview(%L,'Pam','b@audit.test',null,'Dee',1999,'P1',true,true,true,true,false,'v1')$q$, :'sid'))), 'Low');
-- abuse brake: 8 attempts per email per day
do $$ declare i int; n int := 0; begin
  for i in 1..12 loop
    begin perform pg_temp.as_('anon',null,format($q$select public.register_preview(%L,'Pam','spam@audit.test',null,%L,%s,'P1',true,true,true,true,false,'v1')$q$, (select id from public.preview_sessions limit 1), 'Kid'||i, extract(year from now())::int - 6));
          if pg_temp.as_('anon',null,format($q$select public.register_preview(%L,'Pam','spam@audit.test',null,%L,%s,'P1',true,true,true,true,false,'v1')$q$, (select id from public.preview_sessions limit 1), 'Kid'||i||'z', extract(year from now())::int - 6)) like 'err:53400%' then n := n + 1; end if;
    exception when others then null; end;
  end loop;
  perform pg_temp.chk('per-email brake (8/day) trips on rapid registrations', n > 0, 'Medium', 'tripped ' || n || ' times');
end $$;
select pg_temp.note('abuse: anyone can fill a session''s capacity with made-up emails (300/hour site-wide brake only)', 'Low', 'capacity is 40 by default; an attacker with 40 throwaway emails can fill every session and starve real parents; no CAPTCHA. Honeypot only. Real risk is low for a free class but it is the funnel');
select pg_temp.chk('cancel_preview with wrong code returns false and leaks nothing', pg_temp.val('anon',null,format($q$select public.cancel_preview(%L,'ZZZZ','pam@audit.test')::text$q$, :'sid')) = 'false', 'Low');
select pg_temp.note('status "pending" vs "registered" tells the registrant whether a similar child attended in the last 6 months (small eligibility oracle)', 'Low', 'by design the answer to the registrant is "pending" only for review cases; the 8/day/email brake and hashed store limit probing');
