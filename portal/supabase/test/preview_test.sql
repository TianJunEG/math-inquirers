-- Assertions for preview_class.sql (run after schema, policies, preview_class). Any failure raises and stops psql.
\set ON_ERROR_STOP on
create or replace function pg_temp.fails(sql text, expect text default null) returns boolean language plpgsql as $$
begin execute sql; return false;
exception when others then
  if expect is not null and sqlerrm not like '%'||expect||'%' then raise exception 'wrong error for [%]: got [%], wanted [%]', sql, sqlerrm, expect; end if;
  return true; end $$;
-- all consents given; marketing optional
create or replace function pg_temp.reg(s uuid, email text, phone text, child text, yr int, sy text, mkt boolean default false) returns jsonb language sql as $$
  select public.register_preview(s, 'Parent', email, phone, child, yr, sy, true, true, true, true, mkt, 'preview-test-v1') $$;

insert into auth.users (id, email) values ('eeeeeeee-0000-0000-0000-0000000000e5','owner@example.com');
insert into public.admins (user_id) values ('eeeeeeee-0000-0000-0000-0000000000e5');
insert into public.preview_sessions (id, starts_at, band) values
  ('11111111-0000-0000-0000-00000000000b', now() + interval '3 days', 'B'),
  ('22222222-0000-0000-0000-00000000000b', now() + interval '10 days', 'B'),
  ('33333333-0000-0000-0000-00000000000b', now() + interval '17 days', 'B'),
  ('44444444-0000-0000-0000-00000000000b', now() + interval '24 days', 'B'),
  ('55555555-0000-0000-0000-00000000000b', now() + interval '30 minutes', 'B');
insert into public.preview_sessions (id, starts_at, band, capacity) values ('66666666-0000-0000-0000-00000000000b', now() + interval '31 days', 'B', 1);

-- ---------- anon: no table access, no admin ----------
set role anon;
do $$ begin
  assert pg_temp.fails($q$select * from public.preview_registrations$q$, 'permission denied'), 'anon cannot select registrations';
  assert pg_temp.fails($q$select * from public.preview_attended$q$, 'permission denied'), 'anon cannot select attended';
  assert pg_temp.fails($q$select * from public.preview_config$q$, 'permission denied'), 'anon cannot read the pepper';
  assert pg_temp.fails($q$select * from public.preview_sessions$q$, 'permission denied'), 'anon cannot select sessions';
  assert pg_temp.fails($q$select public.admin_preview_check('a@b.co','81234567','Mei',2016)$q$, 'permission denied'), 'anon cannot call admin check';
  assert pg_temp.fails($q$select public._pv_h('email','x')$q$, 'permission denied'), 'anon cannot call the hash helper';
  assert pg_temp.fails($q$select public._pv_eligibility('a','b','c','d',2016)$q$, 'permission denied'), 'anon cannot call eligibility directly';
end $$;

-- the public list shows open sessions more than 1 hour away, no counts
set role anon;
do $$ begin
  assert (select count(*) from public.preview_open_sessions()) = 5, 'five open sessions more than 1 hour away (the 30-minute one is hidden)';
  assert (select count(*) from public.preview_open_sessions() where is_full) = 0;
end $$;
reset role;

-- ---------- registration validation ----------
do $$ declare r jsonb; s uuid := '11111111-0000-0000-0000-00000000000b'; begin
  assert pg_temp.fails($q$select public.register_preview('11111111-0000-0000-0000-00000000000b','P','a@b.co',null,'Mei',2016,'P4',true,true,true,false,false,'v')$q$, 'consent_required'), 'exclusion record consent is required';
  assert pg_temp.fails($q$select public.register_preview('11111111-0000-0000-0000-00000000000b','P','a@b.co',null,'Mei',2016,'P4',false,true,true,true,false,'v')$q$, 'consent_required'), 'parent present is required';
  assert pg_temp.fails($q$select public.register_preview('11111111-0000-0000-0000-00000000000b','P','not-an-email',null,'Mei',2016,'P4',true,true,true,true,false,'v')$q$, 'invalid_input'), 'bad email';
  assert pg_temp.fails($q$select public.register_preview('11111111-0000-0000-0000-00000000000b','P','a@b.co','123','Mei',2016,'P4',true,true,true,true,false,'v')$q$, 'invalid_input'), 'bad phone';
  assert pg_temp.fails($q$select public.register_preview('11111111-0000-0000-0000-00000000000b','P','a@b.co',null,'Mei',1990,'P4',true,true,true,true,false,'v')$q$, 'invalid_input'), 'bad birth year';
  assert pg_temp.fails($q$select public.register_preview('11111111-0000-0000-0000-00000000000b','P','a@b.co',null,'Mei',2016,'P9',true,true,true,true,false,'v')$q$, 'invalid_input'), 'bad school year';
  assert pg_temp.fails($q$select public.register_preview('11111111-0000-0000-0000-00000000000b','P','a@b.co',null,'1234',2016,'P4',true,true,true,true,false,'v')$q$, 'invalid_input'), 'child name needs letters';
  r := public.register_preview(s,'Bot','b@b.co',null,'Bot',2016,'P4',true,true,true,true,false,'v','http://spam');
  assert r->>'status' = 'registered', 'honeypot looks successful';
  assert pg_temp.reg(s,'x@y.co',null,'Zed',2016,'P1')->>'status' = 'wrong_band', 'P1 child cannot take a band B session';
  assert pg_temp.reg('55555555-0000-0000-0000-00000000000b','x@y.co',null,'Zed',2016,'P4')->>'status' = 'closed', 'registration closes 1 hour before';
end $$;
reset role;
do $$ begin assert (select count(*) from public.preview_registrations) = 0, 'honeypot, wrong band and closed store nothing'; end $$;

-- ---------- class 1: Mei attends, Sam registers and does not come, Tom comes for 5 minutes ----------
set role anon;
do $$ declare r jsonb; s uuid := '11111111-0000-0000-0000-00000000000b'; begin
  r := pg_temp.reg(s,'Mei.Parent@Gmail.com','+65 9123 4567','Mei',2016,'P4');
  assert r->>'status' = 'registered' and length(r->>'join_code') = 4, 'Mei registered with a 4 character code';
  assert pg_temp.reg(s,'mei.parent@gmail.com','91234567','mei',2016,'P4')->>'status' = 'already_registered', 'same child twice in one session';
  assert pg_temp.reg(s,'sam@example.com',null,'Sam',2015,'P4')->>'status' = 'registered', 'Sam registered';
  assert pg_temp.reg(s,'tom@example.com','81112222','Tom',2016,'P3')->>'status' = 'registered', 'Tom registered';
end $$;
reset role;
select set_config('request.jwt.claim.sub','eeeeeeee-0000-0000-0000-0000000000e5',false);
set role authenticated;
do $$ declare s uuid := '11111111-0000-0000-0000-00000000000b'; mc text; tc text; n int; st jsonb; begin
  select join_code into mc from public.admin_preview_list(s) where child_first_name = 'Mei';
  select join_code into tc from public.admin_preview_list(s) where child_first_name = 'Tom';
  n := public.admin_preview_mark_attendance(s, array[mc, tc, 'ZZZZ'], array[50, 5, 60]);
  assert n = 1, 'only Mei counts: Tom stayed 5 minutes, ZZZZ is unknown';
  st := public.admin_preview_close_session(s);
  assert (st->>'attended')::int = 1 and (st->>'no_show')::int = 2 and (st->>'registered')::int = 3, 'stats written: 1 attended, 2 no-shows (Sam, Tom)';
  assert public.admin_preview_exclusion_count() = 1, 'one exclusion row';
end $$;
reset role;
do $$ begin
  assert (select count(*) from public.preview_attended where email_h like '%@%' or phone_h like '%9123%' or child_h ilike '%mei%') = 0, 'exclusion store holds no plain identifiers';
  assert (select length(email_h) from public.preview_attended) = 64, 'sha256 hex';
  assert (select count(*) from public.preview_registrations where status = 'no_show') = 2, 'registered-only people are no-shows, not attendees';
end $$;

-- ---------- class 2: the rule ----------
set role anon;
do $$ declare s uuid := '22222222-0000-0000-0000-00000000000b'; r jsonb; begin
  assert pg_temp.reg(s,'mei.parent@gmail.com','91234567','Mei',2016,'P4')->>'status' = 'not_available', 'same child, same email: blocked';
  assert pg_temp.reg(s,'meiparent+class@googlemail.com','98887777','MEI',2016,'P4')->>'status' = 'not_available', 'gmail dots, +tag and googlemail are normalised; case ignored';
  assert pg_temp.reg(s,'other.mum@example.com','6591234567','Mei Ling',2016,'P4')->>'status' = 'not_available', 'new email but same phone (+65 form) and first word of name: blocked';
  assert pg_temp.reg(s,'new.dad@example.com','90001111','Mei',2016,'P4')->>'status' = 'registered', 'LIMIT: new email AND new phone gets in (cannot be detected)';
  assert pg_temp.reg(s,'mei.parent@gmail.com','91234567','Mia',2018,'P2')->>'status' = 'wrong_band', 'sibling in another band is steered to that band';
  assert pg_temp.reg(s,'mei.parent@gmail.com','91234567','Mia',2014,'P3')->>'status' = 'registered', 'sibling with a different first name is a new child';
  r := pg_temp.reg(s,'mei.parent@gmail.com','91234567','Mei',2017,'P3');
  assert r->>'status' = 'pending' and not (r ? 'join_code'), 'same first name, birth year within 1, same email: a person decides';
  assert pg_temp.reg(s,'sam@example.com',null,'Sam',2015,'P4')->>'status' = 'registered', 'a no-show may try again';
  assert pg_temp.reg(s,'tom@example.com','81112222','Tom',2016,'P3')->>'status' = 'registered', 'a short stay does not use up the free class';
end $$;
reset role;
do $$ begin
  assert (select review_reason from public.preview_registrations where child_first_name = 'Mei' and child_birth_year = 2017) = 'similar_child';
  assert (select count(*) from public.preview_registrations where session_id = '22222222-0000-0000-0000-00000000000b') = 5, 'blocked attempts store nothing (5 rows: new dad Mei, Mia, Mei 2017, Sam, Tom)';
end $$;

-- admin check answers like the form; decide the review case; cancel; waitlist
select set_config('request.jwt.claim.sub','eeeeeeee-0000-0000-0000-0000000000e5',false);
set role authenticated;
do $$ declare id uuid; begin
  assert public.admin_preview_check('mei.parent@gmail.com','91234567','Mei',2016) = 'blocked';
  assert public.admin_preview_check('x@y.co','81230000','Mei',2016) = 'ok';
  assert public.admin_preview_check('mei.parent@gmail.com',null,'Mei',2017) = 'review_similar';
  select r.id into id from public.admin_preview_list('22222222-0000-0000-0000-00000000000b') r where r.status = 'pending_review';
  perform public.admin_preview_decide(id, 'decline');
end $$;
reset role;
do $$ begin assert (select status from public.preview_registrations where review_reason = 'similar_child') = 'declined', 'decline recorded'; end $$;

-- cancel with code + email only
do $$ declare c text; s uuid := '22222222-0000-0000-0000-00000000000b'; begin
  select join_code into c from public.preview_registrations where session_id = s and child_first_name = 'Mia';
  perform set_config('t.code', c, false);
end $$;
set role anon;
do $$ declare s uuid := '22222222-0000-0000-0000-00000000000b'; c text := current_setting('t.code'); begin
  assert not public.cancel_preview(s, c, 'wrong@example.com'), 'wrong email cannot cancel';
  assert not public.cancel_preview(s, 'ZZZZ', 'mei.parent@gmail.com'), 'wrong code cannot cancel';
  assert public.cancel_preview(s, lower(c), 'MEI.PARENT@gmail.com'), 'code + email cancels (case-insensitive)';
  assert pg_temp.reg(s,'mei.parent@gmail.com','91234567','Mia',2014,'P3')->>'status' = 'registered', 'can register again after cancelling';
end $$;
-- capacity 1 -> waitlist -> promote
do $$ declare s uuid := '66666666-0000-0000-0000-00000000000b'; begin
  assert pg_temp.reg(s,'a1@example.com',null,'Ann',2016,'P4')->>'status' = 'registered';
  assert pg_temp.reg(s,'b1@example.com',null,'Ben',2016,'P4')->>'status' = 'waitlisted', 'over capacity goes to the waitlist';
end $$;
reset role;
set role authenticated;
do $$ declare s uuid := '66666666-0000-0000-0000-00000000000b'; begin
  assert public.admin_preview_promote_waitlist(s, 1) = 1;
  assert (select count(*) from public.admin_preview_list(s) where status = 'confirmed') = 2, 'promoted';
end $$;
reset role;

-- ---------- repeat no-shows go to a person; window expiry; marketing retention ----------
-- Sam has 1 no-show (class 1). Close class 2 -> Sam second no-show -> third registration is reviewed.
select set_config('request.jwt.claim.sub','eeeeeeee-0000-0000-0000-0000000000e5',false);
set role authenticated;
do $$ begin perform public.admin_preview_close_session('22222222-0000-0000-0000-00000000000b'); end $$;
reset role;
set role anon;
do $$ declare s uuid := '33333333-0000-0000-0000-00000000000b'; begin
  assert pg_temp.reg(s,'sam@example.com',null,'Sam',2015,'P4')->>'status' = 'pending', 'third registration after two no-shows: a person checks';
  assert pg_temp.reg(s,'carl@example.com',null,'Carl',2015,'P4', true)->>'status' = 'registered';
end $$;
reset role;
do $$ begin
  assert (select review_reason from public.preview_registrations where child_first_name='Sam' and session_id='33333333-0000-0000-0000-00000000000b') = 'repeat_no_show';
  assert (select expires_at - s.starts_at from public.preview_registrations r join public.preview_sessions s on s.id = r.session_id where r.child_first_name='Carl') between interval '179 days' and interval '183 days', 'marketing consent keeps contact 6 months';
  assert (select expires_at - s.starts_at from public.preview_registrations r join public.preview_sessions s on s.id = r.session_id where r.child_first_name='Sam' and r.session_id='33333333-0000-0000-0000-00000000000b') = interval '30 days', 'otherwise 30 days';
end $$;
delete from public.preview_attempts;   -- (the daily attempt limit is tested below)
-- six months pass: Mei is new again (7 months: row not purged yet but outside the 6 month window)
update public.preview_attended set attended_at = now() - interval '6 months 1 day';
set role anon;
do $$ begin assert pg_temp.reg('44444444-0000-0000-0000-00000000000b','mei.parent@gmail.com','91234567','Mei',2016,'P4')->>'status' = 'registered', 'after 6 months the child is eligible again'; end $$;
reset role;
update public.preview_attended set attended_at = now() - interval '5 months 29 days';
set role anon;
do $$ begin assert pg_temp.reg('44444444-0000-0000-0000-00000000000b','mei.parent@gmail.com','91234567','Mei',2016,'P4')->>'status' = 'already_registered', 'same session already holds her'; end $$;
reset role;

-- attempt limit: 8 tries a day per parent email, blocked tries included
set role anon;
do $$ declare i int; begin
  for i in 1 .. 8 loop perform pg_temp.reg('44444444-0000-0000-0000-00000000000b','probe@example.com',null,'Pat'||chr(96+i),2016,'P4'); end loop;
  assert pg_temp.fails($q$select public.register_preview('44444444-0000-0000-0000-00000000000b','P','probe@example.com',null,'Pat',2016,'P4',true,true,true,true,false,'v')$q$, 'busy'), 'ninth attempt in a day is refused';
end $$;
reset role;
do $$ begin assert (select count(*) from public.preview_attempts where email_h like '%@%') = 0, 'attempt log is hash-only'; end $$;

-- ---------- retention and deletion ----------
update public.preview_attended set expires_at = now() - interval '1 day';
update public.preview_registrations set expires_at = now() - interval '1 day' where session_id = '11111111-0000-0000-0000-00000000000b';
select set_config('request.jwt.claim.sub','eeeeeeee-0000-0000-0000-0000000000e5',false);
set role authenticated;
do $$ declare n int; begin
  n := public.admin_purge_preview();
  assert n = 4, 'purged 3 first-class registrations and 1 exclusion row, got ' || n;
  assert public.admin_preview_exclusion_count() = 0;
  assert (select count(*) from public.admin_preview_funnel()) = 1, 'funnel has one row per band in use';
  assert public.admin_preview_delete_person('sam@example.com') >= 1, 'PDPA deletion by parent email';
end $$;
reset role;
do $$ begin assert (select count(*) from public.preview_registrations where child_first_name = 'Sam') = 0; end $$;
-- non-admin authenticated user is refused
insert into auth.users (id, email) values ('99999999-0000-0000-0000-000000000009','x@example.com');
select set_config('request.jwt.claim.sub','99999999-0000-0000-0000-000000000009',false);
set role authenticated;
do $$ begin
  assert pg_temp.fails($q$select * from public.admin_preview_list('11111111-0000-0000-0000-00000000000b')$q$, 'forbidden'), 'non-admin refused';
  assert pg_temp.fails($q$select public.admin_purge_preview()$q$, 'forbidden'), 'non-admin cannot purge';
end $$;
reset role;
\echo preview_test.sql OK
