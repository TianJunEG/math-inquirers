# 2027 Term 1: Jasmine's availability and usable slots (draft, to confirm)

**UPDATE 23 Oct 2026: term lessons are 90 minutes (owner decision). Sections 2-6 below are SUPERSEDED 75-minute history, kept only for the record: their slot ids (T27-FRI-1630, T27-SAT-1800, T27-SUN-1630 etc.) are NOT on the site or the form. The CURRENT slots are in section 7 and match `website/data/interest_slots.json`. Section 1 (the grid) is still valid except the Sunday correction below.**

**CORRECTION 23 Oct 2026 (owner_decisions.md): Sunday church plus lunch is blocked from 10:30am to about 2:00pm, so the Sunday 12:30-2:00pm row below is no longer "unknown": it is blocked. MOE 2027 Term 1 (4 Jan-12 Mar, March holidays 13-21 Mar) comes from secondary sources only: verify on moe.gov.sg before fixing dates.**

Written 23 Oct 2026 from Jasmine's weekly availability grid (yellow = free, red = blocked, white = taken) and her 2027 term-time slot grid (`docs/terms/owner_decisions.md`, entry "2027 term-time slot grid"). Everything marked "assumed" is for her to confirm. Singapore time. One tutor, all lessons online.

## 1. The transcribed grid
| Day | Day job (Outram Sec) | Taken (private tutoring or other) | Blocked (red) | Free (yellow) |
|---|---|---|---|---|
| Mon | 7:45am-2:30pm | 3:00-4:30pm, 5:30-7:30pm, 8:00-10:00pm | | none stated |
| Tue | 7:45am-2:30pm | 4:15-6:30pm, 7:00-8:30pm | | afternoon until 4:15pm |
| Wed | 7:45am-2:30pm | 3:00-5:00pm, 5:30-7:00pm, 8:00-9:30pm | | none stated |
| Thu | 7:45am-2:30pm | 3:30-5:30pm | | from 5:30pm onwards |
| Fri | none | 6:00-7:30pm, 8:00-9:30pm | | all day until 6:00pm (the 7:30-8:00pm gap is not usable) |
| Sat | none | 8:30-10:00am, 10:30am-12:30pm | 2:00-5:00pm (Chinese orchestra) | from 5:00pm |
| Sun | none | 9:00-10:30am, 2:00-3:30pm | about 10:30am-12:30pm (church) | from 3:30pm |

CONFIRMED by the owner (23 Oct 2026): Sat 12:30-2:00pm is her lunch time, so it is not free (treated as blocked; no class there). Assumed (please confirm): Sun 12:30-2:00pm is unspecified, so treated as unknown / not free. Sun church is taken as 10:30am-12:30pm ("about"). Mon and Wed show no free time. A "free" window is only free if nothing is taken inside it.

## 2. Rules used  [SUPERSEDED 75-minute content, do not use; see section 7]
- 75-minute slots from the owner's 2027 term-time grid. Weekday: 3:00-4:15, 4:30-5:45, 6:00-7:15, 7:45-9:00pm. Weekend: 9:00-10:15, 10:30-11:45am, 12:00-1:15, 1:30-2:45, 3:00-4:15, 4:30-5:45, 6:00-7:15, 7:45-9:00pm.
- At least 15 minutes between consecutive classes, including her private lessons (both before and after the slot).
- No class past 9:00pm.
- School-age children are at school on weekdays, so weekday daytime is not usable even though Friday morning is free. Weekday slots start at 3:00pm or later.
- A slot is usable only if it sits wholly inside a free window and keeps the 15-minute buffer before the next taken commitment. Computed by script (all 4 weekday x 5 days and 8 weekend x 2 days slots checked).

## 3. Usable slots (9)  [SUPERSEDED 75-minute content, do not use; see section 7]
| Slot | Time | Buffer to next commitment | Suggested levels | Notes |
|---|---|---|---|---|
| T27-FRI-1500 | Fri 3:00-4:15pm | 105 min (6:00pm lesson) | 1, 2 | weekday after school; young children |
| T27-FRI-1630 | Fri 4:30-5:45pm | 15 min (6:00pm lesson) | 2, 3, 4 | tight but meets the rule |
| T27-THU-1800 | Thu 6:00-7:15pm | none after (7:45pm slot free) | 4, 5, 6 | 30 min after the 3:30-5:30 lesson |
| T27-THU-1945 | Thu 7:45-9:00pm | none | 6 (5 if needed) | late school night; older children only |
| T27-SAT-1800 | Sat 6:00-7:15pm | none | 3, 4, 5 | free from 5:00pm |
| T27-SAT-1945 | Sat 7:45-9:00pm | none | 5, 6 | late; older children |
| T27-SUN-1630 | Sun 4:30-5:45pm | none | 1, 2, 3 | free from 3:30pm; best for young children |
| T27-SUN-1800 | Sun 6:00-7:15pm | none | 3, 4, 5 | |
| T27-SUN-1945 | Sun 7:45-9:00pm | none | 5, 6 | FLAG: Sunday night before school; not suggested for young children (Levels 1-3) |

Levels and ages: 1 = 6-8, 2 = 7-9, 3 = 8-10, 4 = 9-11, 5 = 10-12, 6 = 11-13. Younger levels sit earlier in the day, older levels later.

### Flagged, not counted as usable
- Tue 3:00-4:15pm: zero buffer before the 4:15pm private lesson (breaks the 15-minute rule). Usable only if she accepts 0 minutes, or if the 4:15 lesson moves later.
- All 7:45pm slots (Thu, Sat, Sun): ends at 9:00pm exactly, late for school-age children; kept for Levels 5-6 only.
- Excluded because of overlap: every Mon and Wed slot; Tue after 4:15pm; Thu 3:00 and 4:30pm; Fri 6:00pm and 7:45pm; Sat before 5:00pm (taken, Sat lunch 12:30-2:00pm, or orchestra), Sat 4:30pm (orchestra until 5:00pm); Sun before 3:30pm (taken, church, or unknown) and Sun 3:00pm (taken until 3:30pm).

## 4. DEFAULT draft assignment (default chosen, for Jasmine to change)  [SUPERSEDED 75-minute content, do not use; see section 7]
Term lessons are one lesson a week (10 per term), so one weekly slot per level.

| Level | Default weekly slot |
|---|---|
| 1 (6-8) | Fri 3:00-4:15pm |
| 2 (7-9) | Sun 4:30-5:45pm |
| 3 (8-10) | Fri 4:30-5:45pm |
| 4 (9-11) | Sun 6:00-7:15pm |
| 5 (10-12) | Thu 6:00-7:15pm |
| 6 (11-13) | Sat 7:45-9:00pm |

Spare slots for second groups: Sat 6:00-7:15pm (Levels 3-5), Thu 7:45-9:00pm (Levels 5-6), Sun 7:45-9:00pm (Levels 5-6, flagged). There is no spare early slot for a second Level 1-2 group: Fri 4:30-5:45pm (Levels 2-3) is Level 3's default and could be shared if needed.

## 5. Open questions  [SUPERSEDED 75-minute content, do not use; see section 7]
1. 75-minute slots vs 90-minute lessons: pending the owner's decision (shorten term lessons to 75 minutes, or use 90-minute lessons in modified slots).
2. 2027 Term 1 start date and the school term calendar (so first lesson and 10 weeks can be placed; also public holidays).
3. Confirm the assumptions in section 1: the unspecified Sun 12:30-2:00pm gap (treated not free; Sat 12:30-2:00pm is confirmed as lunch), church end time, and whether Mon and Wed truly have no free time.
4. Accept the 15-minute rule at Fri 4:30pm (ends 5:45, lesson at 6:00pm) and the late 7:45pm slots for older children?
5. Is a zero-buffer Tue 3:00pm worth considering, or can the 4:15 private lesson move?
6. Do the default assignments suit her, especially Level 6 on Sat 7:45pm?

## 6. Website  [SUPERSEDED 75-minute content, do not use; see section 7]
The usable slots are placeholders in `website/data/interest_slots.json` (ids `T27-...`), labelled "2027 term time" and "Not open yet", under each suggested level. No 2027 dates or prices are shown. The 2026 holiday placeholders are unchanged.

## 7. CURRENT: 90-minute re-derivation (supersedes sections 2-6)
Rules: 90-minute lesson; at least 15 minutes to any other class or her private lesson/commitment (before and after); finish by 9:00pm; weekday start 3:00pm or later, weekend 9:00am or later; taken/blocked times as in section 1 (Sat 2:00-5:00pm orchestra, Sat 12:30-2:00pm lunch, Sun 10:30am-2:00pm church/lunch blocked). Computed by script on a 15-minute grid (every start time checked), then a maximal non-overlapping set per day with 15-minute breaks, earliest first. Anchors 3:00 / 4:45 / 6:30pm do not give the maximum on any day, so the pattern is packed instead.

| Day | Free window after buffers | Slots (8 total) |
|---|---|---|
| Mon, Tue, Wed | no 90-minute window | none (Tue 3:00-4:30pm overlaps the 4:15pm lesson) |
| Thu | 5:45-9:00pm | 5:45-7:15pm, 7:30-9:00pm |
| Fri | 3:00-5:45pm | 3:00-4:30pm (4:15-5:45pm is the only other start; one lesson fits) |
| Sat | 5:15-9:00pm | 5:15-6:45pm, 7:00-8:30pm |
| Sun | 3:45-9:00pm | 3:45-5:15pm, 5:30-7:00pm, 7:15-8:45pm |

Site ids and suggested levels (younger earlier): T27-FRI-1500 (L1-2), T27-SUN-1545 (L1-3), T27-THU-1745 (L3-5), T27-SAT-1715 (L3-5), T27-SUN-1730 (L3-5), T27-THU-1930 (L5-6), T27-SAT-1900 (L5-6), T27-SUN-1915 (L5-6).

Flags:
- Zero-buffer slots: none in the set. Sat 5:00-6:30pm would touch the orchestra (not used; Sat starts 5:15pm).
- Ending after 8:30pm: Thu 7:30-9:00pm (ends 9:00pm) and Sun 7:15-8:45pm (Sunday night before school): Levels 5-6 only, not for younger levels. Sat 7:00-8:30pm ends exactly 8:30pm: Level 5-6 only.
- Only one early weekday slot (Fri 3:00pm) now exists for Levels 1-2; the 75-minute set had two. Sun 3:45pm is the other early slot.
- Slot count: 8 (was 9). Each level page lists at most 9 placeholders (Level 5), under the form's 12-selection cap; total site placeholders 14 (6 holiday + 8 term), but a parent only sees their own level's.

DEFAULT draft assignment (for Jasmine to change), one weekly slot per level:
| Level | Slot |
|---|---|
| 1 (6-8) | Fri 3:00-4:30pm |
| 2 (7-9) | Sun 3:45-5:15pm |
| 3 (8-10) | Sun 5:30-7:00pm |
| 4 (9-11) | Thu 5:45-7:15pm |
| 5 (10-12) | Sat 5:15-6:45pm |
| 6 (11-13) | Sat 7:00-8:30pm |
Spares: Thu 7:30-9:00pm and Sun 7:15-8:45pm (Levels 5-6), nothing early for a second Level 1-2 group.

Open questions 1 (slot length) is closed: 90 minutes. Questions 2-4 and 6 still apply.

## 8. UPDATE 23 Oct 2026 (owner answers 16 and 17)
- The Thu 7:30-9:00pm (`T27-THU-1930`) and Sun 7:15-8:45pm (`T27-SUN-1915`) options are offered to LEVELS 5 AND 6 ONLY. This was already the case in `website/data/interest_slots.json` and is now locked by `website/tests/slots_data_test.py`. No SQL source holds slot ids or levels, so nothing in `portal/supabase/*.sql` changed.
- Sunday 2:00pm is NOT available (owner). Sunday stays blocked until about 11:15am (church), with lunch 12:30-2:00pm on Sat and Sun. The 2027 Sunday slots above start at 3:45pm and are unaffected.
- The 2026 reserve R4 (Sun 2:00pm) is withdrawn; PROPOSED replacement R4B (Sat 9:00-10:30am + Sun 6:00-7:30pm, Levels 5-6) is in `docs/schedule/beta_schedule.md`.
