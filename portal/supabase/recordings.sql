-- Math Inquirers: recorded live lessons for ENROLLED families (Google Meet -> tutor review -> published copy).
-- DRAFT. NOT APPLIED to any database by the author. Review first (owner + lawyer: see docs/recordings_design.md), then try on a scratch
-- Supabase project, never first on the live one. Run AFTER schema.sql and policies.sql. Safe to re-run (idempotent).
-- If you ever re-run policies.sql (it revokes every function grant), re-run this file after it.
--
-- Design in one paragraph
--   * One row per published lesson recording: recordings(group_id, lesson_no, title, provider, provider_id, status, published_at, expires_at).
--     'provider_id' (the Cloudflare Stream video uid, or a Drive file id) is the secret that finds the file. Clients can NOT select it
--     (column grants below). They list recordings through my_recordings() and ask to play one through recording_playback().
--   * Who may watch: the logged-in PARENT (auth.uid()) of a child whose enrolment is in the recording's group and is 'confirmed', or was
--     cancelled AFTER a paid payment (terms: "can still watch the recordings of lessons already held"), AND whose current 'recording' consent is
--     granted. An unpaid, expired or never-paid reservation has no access. Admin sees everything. Tutor access: add is_tutor_of_group() later.
--   * Playback is a two-step: (1) the browser calls the Cloudflare Pages Function /api/recording-token with the parent's Supabase JWT;
--     (2) the function calls recording_playback() AS THAT PARENT (JWT forwarded, so RLS/auth.uid() apply), and only if a row comes back signs a
--     short-lived Cloudflare Stream token (under 1 hour) for that video uid. The signing key lives only in Cloudflare secrets.
--   * Every successful playback request writes one recording_views row (who, which recording, when) so the owner can show make-up use and
--     investigate a leak. Views are deleted with the recording.
--   * Nothing here sends anything, calls Google or Cloudflare, or deletes a file: the database only says what should exist and what is due for
--     deletion. The owner/script deletes the provider file, then confirms it with admin_confirm_recording_deleted().

create extension if not exists pgcrypto with schema extensions;

-- same definition as practice_submissions.sql (create or replace is safe if both files are applied)
create or replace function public._has_consent(p_parent uuid, p_type text) returns boolean
language sql stable security definer set search_path = public, pg_temp as $$
  select coalesce((select c.granted from public.consents c where c.parent_id = p_parent and c.consent_type = p_type order by c.seq desc limit 1), false);
$$;

-- ---------- 1. recordings ----------
create table if not exists public.recordings (
  id             uuid primary key default gen_random_uuid(),
  group_id       text not null references public.groups(id),
  lesson_no      smallint not null check (lesson_no between 1 and 10),
  title          text not null check (char_length(btrim(title)) between 1 and 120),   -- e.g. 'Lesson 3: Number bonds' (no child names, ever)
  provider       text not null check (provider in ('stream','drive','r2')),
  provider_id    text check (provider_id is null or char_length(provider_id) between 8 and 200),   -- null once the provider file is deleted
  duration_min   smallint check (duration_min is null or duration_min between 1 and 240),
  recorded_on    date not null,
  status         text not null default 'draft' check (status in ('draft','in_review','published','withdrawn','expired')),
  published_at   timestamptz,
  expires_at     timestamptz not null,       -- default rule: last lesson of the group + 30 days (privacy.html retention table)
  review         jsonb not null default '{}'::jsonb,  -- tutor checklist: {"no_private_info":true,"no_child_names_faces":true,"on_topic":true,"trimmed":true,"reviewer":"..."}
  reviewed_by    uuid,                        -- admin user id who published it
  provider_deleted_at timestamptz,            -- set when the file at the provider was deleted
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now(),
  check (status <> 'published' or (published_at is not null and provider_id is not null)),
  check (status <> 'published' or (review ? 'no_private_info' and review ? 'no_child_names_faces' and review ? 'on_topic'))
);
-- one live copy per group lesson; a withdrawn/expired row may be followed by a replacement upload
create unique index if not exists recordings_one_live on public.recordings (group_id, lesson_no) where status in ('draft','in_review','published');
create index if not exists recordings_group_idx on public.recordings (group_id, lesson_no);
create index if not exists recordings_due_idx on public.recordings (expires_at) where status in ('published','withdrawn');

create table if not exists public.recording_views (
  id           bigint generated always as identity primary key,
  recording_id uuid not null references public.recordings(id) on delete cascade,
  parent_id    uuid not null,                 -- no FK: kept only as long as the recording; deleted with it
  child_id     uuid,
  viewed_at    timestamptz not null default now()
);
create index if not exists recording_views_rec_idx on public.recording_views (recording_id, viewed_at desc);

-- ---------- 2. access rule (one place) ----------
-- true when p_parent has a child with a confirmed enrolment (or a cancelled one that was PAID) in p_group, and the 'recording' consent is on.
create or replace function public._can_watch_group(p_parent uuid, p_group text, p_child uuid default null) returns boolean
language sql stable security definer set search_path = public, pg_temp as $$
  select public._has_consent(p_parent, 'recording')
     and exists (
       select 1 from public.enrolments e
        where e.parent_id = p_parent and e.group_id = p_group
          and (p_child is null or e.child_id = p_child)
          and (e.status = 'confirmed'
               or (e.status = 'cancelled' and exists (select 1 from public.payments pay where pay.enrolment_id = e.id and pay.status = 'paid'))));
$$;

-- ---------- 3. parent / family reads ----------
-- Lists published, unexpired recordings for the caller's groups. NO provider_id. One row per (child, recording) so the page can show
-- "Watch recording" under the right child.
create or replace function public.my_recordings()
returns table (recording_id uuid, child_id uuid, child_name text, group_id text, lesson_no smallint, title text, duration_min smallint,
               recorded_on date, published_at timestamptz, expires_at timestamptz)
language sql stable security definer set search_path = public, pg_temp as $$
  select r.id, e.child_id, coalesce(c.display_name, e.child_label), r.group_id, r.lesson_no, r.title, r.duration_min, r.recorded_on, r.published_at, r.expires_at
    from public.recordings r
    join public.enrolments e on e.group_id = r.group_id and e.parent_id = auth.uid()
    left join public.children c on c.id = e.child_id
   where auth.uid() is not null
     and r.status = 'published' and r.published_at <= now() and r.expires_at > now()
     and public._can_watch_group(auth.uid(), r.group_id, e.child_id)
   order by r.group_id, r.lesson_no desc;
$$;

-- Called by the Pages Function with the PARENT's JWT. Returns provider + provider_id only when the rule passes; logs the view.
-- No row = the function must answer 404 (never say whether the recording exists).
create or replace function public.recording_playback(p_recording uuid, p_child uuid default null)
returns table (provider text, provider_id text, title text, expires_at timestamptz)
language plpgsql security definer set search_path = public, pg_temp as $$
#variable_conflict use_column
declare r public.recordings; uid uuid := auth.uid();
begin
  if uid is null then return; end if;
  select * into r from public.recordings where id = p_recording and status = 'published' and published_at <= now() and expires_at > now() and provider_id is not null;
  if not found then return; end if;
  if not public._can_watch_group(uid, r.group_id, p_child) then return; end if;
  insert into public.recording_views (recording_id, parent_id, child_id) values (r.id, uid, p_child);
  return query select r.provider, r.provider_id, r.title, r.expires_at;
end $$;

-- ---------- 4. admin (owner) ----------
create or replace function public.admin_list_recordings()
returns table (id uuid, group_id text, lesson_no smallint, title text, provider text, provider_id text, status text, recorded_on date,
               published_at timestamptz, expires_at timestamptz, views bigint, review jsonb, provider_deleted_at timestamptz)
language plpgsql stable security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  return query select r.id, r.group_id, r.lesson_no, r.title, r.provider, r.provider_id, r.status, r.recorded_on, r.published_at, r.expires_at,
                      (select count(*) from public.recording_views v where v.recording_id = r.id), r.review, r.provider_deleted_at
                 from public.recordings r order by r.group_id, r.lesson_no, r.created_at;
end $$;

-- Create or update the DRAFT for a group lesson (after the owner has uploaded the trimmed file and has its provider id).
create or replace function public.admin_save_recording(p_group text, p_lesson smallint, p_title text, p_provider text, p_provider_id text,
                                                       p_recorded_on date, p_expires_at timestamptz, p_duration_min smallint default null)
returns uuid language plpgsql security definer set search_path = public, pg_temp as $$
declare rid uuid;
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  if p_expires_at <= now() then raise exception 'expiry_in_past'; end if;
  select id into rid from public.recordings where group_id = p_group and lesson_no = p_lesson and status in ('draft','in_review');
  if rid is null then
    insert into public.recordings (group_id, lesson_no, title, provider, provider_id, recorded_on, expires_at, duration_min)
    values (p_group, p_lesson, btrim(p_title), p_provider, p_provider_id, p_recorded_on, p_expires_at, p_duration_min) returning id into rid;
  else
    update public.recordings set title = btrim(p_title), provider = p_provider, provider_id = p_provider_id, recorded_on = p_recorded_on,
           expires_at = p_expires_at, duration_min = p_duration_min, updated_at = now() where id = rid;
  end if;
  return rid;
end $$;

-- Publish only with a completed review checklist (all three required keys true). p_review example:
--   {"no_private_info":true,"no_child_names_faces":true,"on_topic":true,"trimmed":true,"reviewer":"Jasmine"}
create or replace function public.admin_publish_recording(p_recording uuid, p_review jsonb)
returns void language plpgsql security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  if coalesce((p_review->>'no_private_info')::boolean, false) is not true
     or coalesce((p_review->>'no_child_names_faces')::boolean, false) is not true
     or coalesce((p_review->>'on_topic')::boolean, false) is not true then raise exception 'review_incomplete'; end if;
  update public.recordings set status = 'published', published_at = now(), review = p_review, reviewed_by = auth.uid(), updated_at = now()
   where id = p_recording and status in ('draft','in_review') and provider_id is not null;
  if not found then raise exception 'not_publishable'; end if;
end $$;

-- Pull a recording at once (something private was found, a parent withdrew consent, a mistake). Playback stops immediately; the provider file
-- is deleted by the owner and confirmed below.
create or replace function public.admin_withdraw_recording(p_recording uuid, p_reason text default null)
returns void language plpgsql security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  update public.recordings set status = 'withdrawn', updated_at = now(),
         review = review || jsonb_build_object('withdrawn_reason', left(coalesce(p_reason, ''), 200), 'withdrawn_at', now())
   where id = p_recording and status in ('draft','in_review','published');
  if not found then raise exception 'not_found'; end if;
end $$;

-- Retention sweep. Marks every published recording past expires_at as 'expired' (playback is already refused by expires_at; this makes the
-- state explicit) and RETURNS the provider files that must now be deleted (expired + withdrawn, not yet confirmed deleted).
create or replace function public.admin_recordings_due_for_deletion()
returns table (id uuid, group_id text, lesson_no smallint, provider text, provider_id text, status text, expires_at timestamptz)
language plpgsql security definer set search_path = public, pg_temp as $$
#variable_conflict use_column
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  update public.recordings set status = 'expired', updated_at = now() where status = 'published' and expires_at <= now();
  return query select r.id, r.group_id, r.lesson_no, r.provider, r.provider_id, r.status, r.expires_at
                 from public.recordings r where r.status in ('expired','withdrawn') and r.provider_id is not null order by r.expires_at;
end $$;

-- After the owner has deleted the file at Cloudflare/Drive: blank the provider id and delete the view log for that recording.
create or replace function public.admin_confirm_recording_deleted(p_recording uuid)
returns void language plpgsql security definer set search_path = public, pg_temp as $$
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  update public.recordings set provider_id = null, provider_deleted_at = now(), updated_at = now()
   where id = p_recording and status in ('expired','withdrawn');
  if not found then raise exception 'not_found'; end if;
  delete from public.recording_views where recording_id = p_recording;
end $$;

-- ---------- 5. RLS + grants ----------
alter table public.recordings      enable row level security;
alter table public.recording_views enable row level security;
revoke all on public.recordings, public.recording_views from anon, authenticated;
-- No client can read provider_id, review or reviewer: the whole table has no grant. Reads go through my_recordings()/recording_playback()
-- (security definer) and the admin functions. (RLS is on with no policy as a second lock.)
grant usage on sequence public.recording_views_id_seq to service_role;

revoke all on function public._can_watch_group(uuid, text, uuid), public._has_consent(uuid, text) from public, anon, authenticated;
revoke all on function public.my_recordings(), public.recording_playback(uuid, uuid), public.admin_list_recordings(),
  public.admin_save_recording(text, smallint, text, text, text, date, timestamptz, smallint), public.admin_publish_recording(uuid, jsonb),
  public.admin_withdraw_recording(uuid, text), public.admin_recordings_due_for_deletion(), public.admin_confirm_recording_deleted(uuid)
  from public, anon;
grant execute on function public.my_recordings()                         to authenticated;
grant execute on function public.recording_playback(uuid, uuid)          to authenticated;   -- called with the parent's JWT by the Pages Function
grant execute on function public.admin_list_recordings()                 to authenticated;   -- each admin_* checks is_admin() inside
grant execute on function public.admin_save_recording(text, smallint, text, text, text, date, timestamptz, smallint) to authenticated;
grant execute on function public.admin_publish_recording(uuid, jsonb)    to authenticated;
grant execute on function public.admin_withdraw_recording(uuid, text)    to authenticated;
grant execute on function public.admin_recordings_due_for_deletion()     to authenticated;
grant execute on function public.admin_confirm_recording_deleted(uuid)   to authenticated;

-- ---------- 6. optional daily sweep (pg_cron; enable the extension in Supabase first). Only flips status; deleting files stays a human step. ----------
-- select cron.schedule('recordings-expire', '15 19 * * *', $$ update public.recordings set status = 'expired', updated_at = now() where status = 'published' and expires_at <= now() $$);

-- ---------- 7. account deletion ----------
-- delete_my_data() (the full version in practice_submissions.sql) already deletes this parent's recording_views rows when this table exists (R1-H1).
