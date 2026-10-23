-- Updates the EXISTING public.groups rows to the schedule with 15-minute breaks and a lunch hour.
-- Generated from website/data/beta_schedule.json (run portal/tools/gen_groups_seed.py for the full seed). Safe to re-run; seats taken and fees are not touched.
begin;
update public.groups set sessions = '[{"day": "Tue", "start": "09:00", "end": "10:30"}, {"day": "Fri", "start": "09:00", "end": "10:30"}]'::jsonb, first_label = 'Tue 24 Nov', last_label = 'Thu 24 Dec', start_date = '2026-11-24' where id = 'L1A';
update public.groups set sessions = '[{"day": "Tue", "start": "10:45", "end": "12:15"}, {"day": "Fri", "start": "10:45", "end": "12:15"}]'::jsonb, first_label = 'Tue 24 Nov', last_label = 'Thu 24 Dec', start_date = '2026-11-24' where id = 'L2A';
update public.groups set sessions = '[{"day": "Tue", "start": "13:15", "end": "14:45"}, {"day": "Fri", "start": "13:15", "end": "14:45"}]'::jsonb, first_label = 'Tue 24 Nov', last_label = 'Thu 24 Dec', start_date = '2026-11-24' where id = 'L3A';
update public.groups set sessions = '[{"day": "Tue", "start": "15:00", "end": "16:30"}, {"day": "Fri", "start": "15:00", "end": "16:30"}]'::jsonb, first_label = 'Tue 24 Nov', last_label = 'Thu 24 Dec', start_date = '2026-11-24' where id = 'L4A';
update public.groups set sessions = '[{"day": "Fri", "start": "16:45", "end": "18:15"}, {"day": "Sun", "start": "16:15", "end": "17:45"}]'::jsonb, first_label = 'Fri 27 Nov', last_label = 'Sun 27 Dec', start_date = '2026-11-27' where id = 'L5A';
update public.groups set sessions = '[{"day": "Thu", "start": "18:15", "end": "19:45"}, {"day": "Sat", "start": "18:45", "end": "20:15"}]'::jsonb, first_label = 'Thu 26 Nov', last_label = 'Sat 26 Dec', start_date = '2026-11-26' where id = 'L6A';
commit;
