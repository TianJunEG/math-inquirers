# Audit: schedule and calendar (holiday beta timetable, 2027 Term 1 grid, calendar files)

Auditor: independent. Audited at commit 5bf9d9b (branch claude/great-fermi-1hv4vc). Audit only; no existing file edited. Date of audit: 23 Oct 2026.

## Verdict: Ready after minor fixes
0 High, 3 Medium, 5 Low. The dates, weekdays, breaks, lunch, end times and calendar clearances all recompute correctly. The problems are wording and stale or incomplete documentation, not wrong dates.

## What I did (evidence)
1. Recomputed all 60 lessons from `website/data/beta_schedule.json` with a script (weekday of every date, 90-minute length, 09:00 to 21:00 window, lunch 12:15-13:15, sessions on the same day at least 15 minutes apart, Sunday church block 10:30-14:00, Saturday lunch 12:30-14:00, no lesson on Fri 25 Dec, lesson count 10 per group). Result: 0 mismatches. Latest end time 20:15 (Level 6 Saturday). Smallest same-day gap 15 minutes (as required). Christmas week exceptions are right: Levels 1-4 lesson 10 on Thu 24 Dec at their usual time of day; Level 5 lesson 9 on Wed 23 Dec 16:45-18:15 and lesson 10 on Sun 27 Dec 16:15; Level 6 unaffected (Thu 24 Dec, Sat 26 Dec). Thu 24 Dec holds L1-L4 then L6 at 18:15 (105 minutes after L4); a fifth class there would indeed have touched L6, so the Level 5 Wednesday move is sound.
2. Owner's rules: Level 5 Sunday 16:15 (4:15pm) and Level 6 Saturday 18:45 (6:45pm) are in the JSON, the docs, `seed_groups.sql`, `update_groups_schedule.sql`, the embedded sign-up data and the live database.
3. Live Supabase `public.groups` (read-only query, project math-inquirers): six rows L1A-L6A; `sessions`, `first_label`, `last_label`, `start_date`, `seats` (8) and `fee_cents` (25000) all equal the JSON and both SQL files. No drift.
4. Google Calendar (read only), 23 Nov-28 Dec 2026. `list_calendars` returns only `jasmine@mncoholding.com` and "Holidays in Singapore"; the primary calendar is the same account (identical event list from both calls). Events: Wed 20:00-21:30 "P5M" (25 Nov, 2, 9, 16, 23 Dec); Sat 14:00-17:00 "Chinese orchestra practice" (28 Nov, 5, 12, 19, 26 Dec); Mon 10:30-12:30 "P5M" (7, 14, 21, 28 Dec). No other events. Every one of the 60 published sessions and all 8 reserved sessions is at least 45 minutes clear (tightest: Wed 23 Dec L5 ends 18:15, P5M 20:00 = 105 minutes; Sat L6 18:45 after orchestra 17:00 = 105 minutes; Monday afternoon placeholder from 13:15 after 12:30 = 45 minutes). Matches the claims in `beta_schedule.md`.
5. Singapore public holidays (Google "Holidays in Singapore" calendar, 1 Nov-31 Dec 2026): Deepavali Sun 8 Nov and Mon 9 Nov (before the beta), Christmas Eve 24 Dec (observance only, not a public holiday), Christmas Day Fri 25 Dec (public holiday; correctly skipped), New Year's Eve (observance). Nothing else falls in 23 Nov-27 Dec.
6. MOE dates (web search 23 Oct 2026; the MOE page itself could not be opened, so these come from search results that quote the MOE press release "School Terms and Holidays for 2026", 30 Jul 2025, https://www.moe.gov.sg/news/press-releases/20250730-school-terms-and-holidays-for-2026, and moe.gov.sg/calendar): 2026 Term 4 is 14 Sep-20 Nov; year-end holidays 21 Nov-31 Dec. So the whole beta (23 Nov-27 Dec) is in the holidays, and weekday daytime slots are valid for children. For 2027 (secondary sources only, e.g. practicle.sg): Term 1 4 Jan-12 Mar, March holidays 13-21 Mar, Term 2 starts 22 Mar. Not confirmed from MOE.
7. 2027 grid: re-ran my own 15-minute-step script on the transcription in `term_2027_t1_availability.md` section 1 (90-minute lesson, 15-minute buffer to every taken block, finish by 21:00, weekday start 15:00 or later, weekend 09:00 or later). Usable starts: Thu 17:45-19:30, Fri 15:00-16:15, Sat 17:15-19:30, Sun 15:45-19:30; none on Mon, Tue, Wed. Maximum packings: Thu 17:45 and 19:30, Fri 15:00, Sat 17:15 and 19:00, Sun 15:45, 17:30 and 19:15. This is exactly the doc's 8 slots and the 8 `T27-*` ids in `website/data/interest_slots.json` (times match the ids). Old 75-minute ids (T27-FRI-1630, -SAT-1800 etc.) appear only once each, in the superseded section of the doc, not on the site or the form.
8. Interest ids: the form DB function accepts `^[A-Za-z0-9-]{1,16}$` (longest id T27-FRI-1500 is 12 characters), slot cap 24 (the page shows at most 9 per level). Level pages in `website/dist` and the embedded data in `website/mi_signup.html` show the same ids, labels and times as `interest_slots.json`; level mapping equals the doc (L1-2: FRI-1500; L1-3: SUN-1545; L3-5: THU-1745, SAT-1715, SUN-1730; L5-6: THU-1930, SAT-1900, SUN-1915).
9. ICS or calendar invites: `ops/` does not exist and there is no `.ics` file in the repo at commit 5bf9d9b. Not audited (nothing to audit).

## Findings

### Medium
**M1. Sign-up page says "Lessons start Mon 23 Nov", but no group meets that day.**
Location: `website/lp_build.py:59`, `website/mi_signup.html:277`, built into `website/dist/index.html` (the Choose a group section). Evidence: first lessons are Tue 24 Nov (L1-L4), Thu 26 Nov (L6), Fri 27 Nov (L5); Mon 23 Nov has no session in the JSON. A parent may expect a lesson on Monday. Fix: "Lessons start in the week of Mon 23 Nov (first lessons Tue 24 to Fri 27 Nov, see each group)".

**M2. `term_2027_t1_availability.md` still carries superseded 75-minute content and stale open questions.**
Location: sections 2-6 (lines 14-70), section 5 question 1, and the "Open questions" line at the end. Evidence: a banner says sections 1-6 are superseded, but section 3 lists 9 slots with 75-minute ids (T27-FRI-1630, T27-SAT-1800 etc.), section 6 says "ids T27-..." generically, and section 1 still says "Sun 12:30-2:00pm unknown" although the owner decided (owner_decisions.md, 23 Oct) that Sunday 10:30am to about 2:00pm is blocked. The MOE 2027 Term 1 dates are now known (4 Jan-12 Mar per secondary sources) so question 2 is partly answerable. A reader or agent who skips the banner would use wrong slots. Fix: delete or move sections 2-6 to an "archive" file; update section 1 Sunday row to church/lunch blocked until 14:00; add the MOE 2027 term dates with a "verify on moe.gov.sg" note.

**M3. Reserved groups have no week-5 or per-lesson dates, and three of them collide with published groups in week 5.**
Location: `docs/schedule/beta_reserved.json`, `beta_schedule.md` (Christmas section, last sentence). Evidence: R1 Thu 09:00, R2 Thu 10:45, R3 Thu 13:15 are the same times as L1, L2, L3 on Thu 24 Dec (published exception). The doc admits "a released reserve needs its own week-5 times" but gives none, and the sign-up page / JSON has no lesson list for reserves. When a group fills, the owner would have to improvise under pressure. Fix: precompute R1-R4 lesson dates (including Wed 23 Dec free slots: Wed 09:00, 10:45, 13:15 are free that day, so R1-R3 week 5 could be Wed 23 Dec and Tue 22 Dec or similar) and store them in `beta_reserved.json`.

### Low
**L1. R4 starts at exactly the end of the owner's church and lunch block.** `beta_reserved.json` R4 Sun 14:00-15:30; `interest_slots.json` R4. The owner said Sunday is blocked "to about 2:00pm"; zero buffer. R4 is shown on the Level 5 and 6 pages as an interest option. Fix: Sun 14:15 or 14:30 (still 45 minutes or more before Level 5's 16:15 if wanted), or confirm with the owner.

**L2. Late-evening options on school nights are offered to Level 5 (ages 10-12).** `interest_slots.json` T27-THU-1930 (Thu 19:30-21:00, ends 21:00) and T27-SUN-1915 (Sun 19:15-20:45) have levels [5, 6]. The doc itself flags them "Levels 5-6 only" and Sunday night before school as not for young children; a 10-year-old is borderline. Not a rule break (nothing after 9:00pm), just a judgement call; consider Level 6 only for THU-1930.

**L3. Final week is uneven and falls on Christmas Eve.** Levels 1-4 have lesson 9 on Tue 22 Dec and lesson 10 on Thu 24 Dec (two days apart, Christmas Eve); Level 5 ends Sun 27 Dec. Parents may travel or have events. No rule broken; the cards show the exception. Consider telling parents at sign-up (already shown as "Week 5: Thu 24 Dec").

**L4. `beta_schedule.md` open point on school holidays is now answerable and a number is unclear.** "Assumed school holidays from mid-November ... Confirm" should read: MOE 2026 Term 4 ends 20 Nov, year-end holidays 21 Nov-31 Dec (source above). Also line "Mon 23 Nov onward gives 20 usable weekly sessions" is ambiguous (12 published + 8 reserved weekly sessions); say so.

**L5. The database holds no per-lesson dates or the Christmas exceptions** (only weekly pattern, `first_label`, `last_label`, `start_date`). Not wrong today (the website JSON is the source), but any later reminder, attendance or ICS feature built from the DB would put lessons on Fri 25 Dec. Fix: when building invites, generate from `beta_schedule.json` `lessons[]`, not the DB pattern.

## Not audited / limits
- The owner's original availability grid image (yellow/red/white): I could only check the transcription in the doc, not the picture, so a transcription error would not be caught. Sections of that table that feed 2027 (Fri free until 18:00, Thu from 17:30, Sat from 17:00, Sun from 15:30) are taken as given.
- Sunday church time is not on the calendar; I used the owner's stated time.
- Only the connected Google account was readable. Another calendar the owner may own (for example under pypteltd@gmail.com) was not available. Working-location, birthday and tentative-only events were not requested.
- The MOE primary pages could not be opened; dates come from search results that cite MOE and secondary sites. 2027 public holidays (Chinese New Year, Hari Raya Puasa, Good Friday) and their effect on 10 lessons per term in Term 1 were not checked.
- No ICS or `ops/` files exist; the sign-up form's browser behaviour (rendering in a real browser) was checked only in the built HTML, not clicked through. Seat counts and registrations in other tables were not checked.

## Ranked top 10
1. M1 "Lessons start Mon 23 Nov" is wrong for every group (misleading to parents).
2. M3 Reserved groups lack week-5 and lesson dates; R1-R3 collide with L1-L3 on Thu 24 Dec.
3. M2 Availability doc still holds superseded 75-minute sections and the Sunday "unknown" assumption.
4. L1 R4 Sunday 14:00 has no buffer after church and lunch.
5. L5 DB has no exception dates; invites must not be generated from it.
6. L4 Beta schedule open point (MOE confirmation) and "20 sessions" wording need updating.
7. L2 Level 5 offered Thu 19:30-21:00 and Sun 19:15-20:45 on school nights.
8. L3 Final week uneven, Christmas Eve lessons for five groups.
9. Not audited: owner's grid image and 2027 public holidays.
10. Not audited: no ICS or `ops/` exists yet; re-audit when built.
