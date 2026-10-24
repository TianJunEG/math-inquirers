-- Local test for recordings.sql (NOT wired into run_sql_test.sh; run by hand after schema, policies, seed, recordings).
insert into auth.users (id, email) values
  ('aaaaaaaa-0000-0000-0000-0000000000a1','fam.a@example.com'),   -- paid, confirmed, L1A
  ('bbbbbbbb-0000-0000-0000-0000000000b2','fam.b@example.com'),   -- confirmed in L2A only
  ('cccccccc-0000-0000-0000-0000000000c3','fam.c@example.com'),   -- reservation never paid (cancelled) L1A
  ('dddddddd-0000-0000-0000-0000000000d4','fam.d@example.com'),   -- paid then withdrew (cancelled after paid) L1A
  ('eeeeeeee-0000-0000-0000-0000000000e5','owner@example.com');
insert into public.admins (user_id) values ('eeeeeeee-0000-0000-0000-0000000000e5');
insert into public.children (id, parent_id, display_name, level, pin_hash) values
  ('a1a1a1a1-0000-0000-0000-000000000001','aaaaaaaa-0000-0000-0000-0000000000a1','Ann',1,'x'),
  ('b2b2b2b2-0000-0000-0000-000000000002','bbbbbbbb-0000-0000-0000-0000000000b2','Ben',2,'x'),
  ('c3c3c3c3-0000-0000-0000-000000000003','cccccccc-0000-0000-0000-0000000000c3','Cy',1,'x'),
  ('d4d4d4d4-0000-0000-0000-000000000004','dddddddd-0000-0000-0000-0000000000d4','Di',1,'x');
insert into public.enrolments (id, parent_id, child_id, child_label, group_id, status) values
  ('11111111-0000-0000-0000-000000000001','aaaaaaaa-0000-0000-0000-0000000000a1','a1a1a1a1-0000-0000-0000-000000000001','Ann','L1A','confirmed'),
  ('22222222-0000-0000-0000-000000000002','bbbbbbbb-0000-0000-0000-0000000000b2','b2b2b2b2-0000-0000-0000-000000000002','Ben','L2A','confirmed'),
  ('33333333-0000-0000-0000-000000000003','cccccccc-0000-0000-0000-0000000000c3','c3c3c3c3-0000-0000-0000-000000000003','Cy','L1A','cancelled'),
  ('44444444-0000-0000-0000-000000000004','dddddddd-0000-0000-0000-0000000000d4','d4d4d4d4-0000-0000-0000-000000000004','Di','L1A','cancelled');
insert into public.payments (enrolment_id, reference, status, amount_cents, paid_at) values
  ('11111111-0000-0000-0000-000000000001','MI-T00001','paid',25000,now()),
  ('22222222-0000-0000-0000-000000000002','MI-T00002','paid',25000,now()),
  ('33333333-0000-0000-0000-000000000003','MI-T00003','cancelled',25000,null),
  ('44444444-0000-0000-0000-000000000004','MI-T00004','paid',25000,now());
insert into public.consents (parent_id, consent_type, granted, terms_version, privacy_version)
  select p, 'recording', true, 't', 'p' from unnest(array['aaaaaaaa-0000-0000-0000-0000000000a1','bbbbbbbb-0000-0000-0000-0000000000b2','cccccccc-0000-0000-0000-0000000000c3','dddddddd-0000-0000-0000-0000000000d4']::uuid[]) p;

set role authenticated; select set_config('request.jwt.claim.sub','eeeeeeee-0000-0000-0000-0000000000e5',false);
do $$ declare r uuid; n int; begin
  r := public.admin_save_recording('L1A', 3::smallint, 'Lesson 3: Number bonds', 'stream', 'abcdef1234567890', current_date, now() + interval '30 days', 70::smallint);
  begin perform public.admin_publish_recording(r, '{"no_private_info":true}'); raise exception 'should fail'; exception when others then if sqlerrm <> 'review_incomplete' then raise; end if; end;
  perform public.admin_publish_recording(r, '{"no_private_info":true,"no_child_names_faces":true,"on_topic":true}');
  perform set_config('t.rec', r::text, false);
end $$;

select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-0000000000a1',false);
do $$ declare n int; begin
  select count(*) into n from public.my_recordings(); if n <> 1 then raise exception 'A should see 1, got %', n; end if;
  select count(*) into n from public.recording_playback(current_setting('t.rec')::uuid, 'a1a1a1a1-0000-0000-0000-000000000001'); if n <> 1 then raise exception 'A playback'; end if;
  begin perform 1 from public.recordings; raise exception 'direct select must be denied'; exception when insufficient_privilege then null; end;
end $$;
select set_config('request.jwt.claim.sub','bbbbbbbb-0000-0000-0000-0000000000b2',false);
do $$ declare n int; begin
  select count(*) into n from public.my_recordings(); if n <> 0 then raise exception 'B (other group) must see 0'; end if;
  select count(*) into n from public.recording_playback(current_setting('t.rec')::uuid); if n <> 0 then raise exception 'B playback must be refused'; end if;
end $$;
select set_config('request.jwt.claim.sub','cccccccc-0000-0000-0000-0000000000c3',false);
do $$ declare n int; begin select count(*) into n from public.my_recordings(); if n <> 0 then raise exception 'unpaid must see 0'; end if; end $$;
select set_config('request.jwt.claim.sub','dddddddd-0000-0000-0000-0000000000d4',false);
do $$ declare n int; begin select count(*) into n from public.my_recordings(); if n <> 1 then raise exception 'paid-then-withdrew keeps access'; end if; end $$;
select set_config('request.jwt.claim.sub','',false); set role anon;
do $$ begin begin perform * from public.my_recordings(); raise exception 'anon must be denied'; exception when insufficient_privilege then null; end; end $$;

-- consent withdrawn stops access; withdraw stops access; deletion flow
reset role;
insert into public.consents (parent_id, consent_type, granted, terms_version, privacy_version) values ('aaaaaaaa-0000-0000-0000-0000000000a1','recording',false,'t','p');
set role authenticated; select set_config('request.jwt.claim.sub','aaaaaaaa-0000-0000-0000-0000000000a1',false);
do $$ declare n int; begin select count(*) into n from public.my_recordings(); if n <> 0 then raise exception 'withdrawn consent must stop access'; end if; end $$;
select set_config('request.jwt.claim.sub','eeeeeeee-0000-0000-0000-0000000000e5',false);
do $$ declare n int; begin
  perform public.admin_withdraw_recording(current_setting('t.rec')::uuid, 'test');
  select count(*) into n from public.admin_recordings_due_for_deletion(); if n <> 1 then raise exception 'due list'; end if;
  perform public.admin_confirm_recording_deleted(current_setting('t.rec')::uuid);
  select count(*) into n from public.admin_recordings_due_for_deletion(); if n <> 0 then raise exception 'due list after delete'; end if;
end $$;
select 'RECORDINGS TEST OK' as result;
