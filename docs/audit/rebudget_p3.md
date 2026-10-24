# Level 3 re-budget (P3): what was applied

Applies `docs/audit/timing_p3.md` to the ten Level 3 lessons so that a tutor running the slides live online fits 90 minutes. Nothing was committed. Source of the clock: `rebuild/p3_rebudget.py` writes `p3/budget.json` (parts and optional slides, for the tutor console timer) and the per-slide `plan` in `p3/gifted.json`; `rebuild/p3_gifted.py` (pills, speaker notes, title-slide time plan) and `p3/guide.js` (seg() headings, routine table, scripts) read them. Re-run the model with `python3 docs/audit/timing_p3_rebudget.py` (same constants as `timing_p3.py`, reads `p3/budget.json`).

## 1. Old to new budget (minutes; every lesson sums to 90; Talk time holds the named 3-minute float)

Old (every lesson): Opening 2, Sneak-peek + game + quick Qs 8, Explore 15, Mini-lesson 10, Brain break 5, Worksheet 30, Talk time 10, Exit + look back + close 10.

| Lesson | Opening | Sneak/game/Qs | Explore | Mini | Break | Worksheet | Talk | Exit/look back/close | New clock check |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 -> **1.5** | 8 -> **9.5** | 15 -> **13** | 10 -> **11** | 5 (same) | 30 -> **31** | 10 -> **8** | 10 -> **11** | 90 |
| 2 | 2 -> **1.5** | 8 -> **9.5** | 15 -> **14** | 10 -> **9** | 5 (same) | 30 -> **32** | 10 -> **8** | 10 -> **11** | 90 |
| 3 | 2 -> **1.5** | 8 -> **9.5** | 15 -> **14.5** | 10 -> **11** | 5 (same) | 30 -> **29** | 10 -> **8** | 10 -> **11.5** | 90 |
| 4 | 2 -> **1.5** | 8 -> **9.5** | 15 -> **14** | 10 -> **9.5** | 5 (same) | 30 -> **32** | 10 -> **7.5** | 10 -> **11** | 90 |
| 5 | 2 -> **1.5** | 8 -> **9.5** | 15 -> **14.5** | 10 -> **11** | 5 (same) | 30 -> **31** | 10 -> **7** | 10 -> **10.5** | 90 |
| 6 | 2 -> **1.5** | 8 -> **9.5** | 15 -> **14** | 10 -> **11** | 5 (same) | 30 (same) | 10 -> **8** | 10 -> **11** | 90 |
| 7 | 2 -> **1.5** | 8 -> **9.5** | 15 -> **13.5** | 10 -> **11.5** | 5 (same) | 30 -> **31** | 10 -> **7** | 10 -> **11** | 90 |
| 8 | 2 -> **1.5** | 8 -> **9** | 15 -> **13.5** | 10 -> **10.5** | 5 (same) | 30 -> **31** | 10 -> **8** | 10 -> **11.5** | 90 |
| 9 | 2 -> **1.5** | 8 -> **9** | 15 (same) | 10 -> **8.5** | 5 (same) | 30 -> **31** | 10 -> **8.5** | 10 -> **11.5** | 90 |
| 10 | 2 -> **1.5** | 8 -> **9** | 15 -> **16.5** | 10 -> **9.5** | 5 (same) | 30 -> **29.5** | 10 -> **6** | 10 -> **13** | 90 |

Part clocks (start-end) for every lesson are in `p3/budget.json`. Break is always 5 (2 movement, 2 water, 1 settle; toilet before the break). Optional pages (Think harder, Go further, see it, walk-through: `stretch`, `challenge`, `chdiag`, `chwalk`) carry the pill "Optional, if you finish early" and no clock time; the 3-minute choose window stays inside the worksheet part.

## 2. New estimated totals (model, central; low-high = optimistic and pessimistic sets)

| Lesson | Before (audit) | After fixes, audit prediction | **New, re-run on the rebuilt decks** | Low-high | Float vs 90 |
|---|---|---|---|---|---|
| 1 | 98.7 | 86.9 | **87.0** | 80.0-96.1 | 3.0 |
| 2 | 101.8 | 86.3 | **86.3** | 79.3-95.4 | 3.7 |
| 3 | 98.7 | 86.5 | **87.2** | 80.5-95.9 | 2.8 |
| 4 | 104.2 | 89.3 | **89.2** | 82.0-98.7 | 0.8 |
| 5 | 97.3 | 88.3 | **88.4** | 81.2-97.7 | 1.6 |
| 6 | 105.9 | 84.8 | **85.1** | 78.2-94.3 | 4.9 |
| 7 | 100.4 | 88.9 | **89.0** | 81.7-98.7 | 1.0 |
| 8 | 102.9 | 86.9 | **86.9** | 79.7-96.3 | 3.1 |
| 9 | 94.8 | 82.9 | **82.7** | 75.8-91.7 | 7.3 |
| 10 | 111.6 | 89.2 | **87.9** | 80.4-97.7 | 2.1 |

All ten lessons are now at or under 90 minutes in the central estimate (mean 87.0, the same as the audit's predicted mean of 87.0). L4 (0.8), L7 (1.0), L5 (1.6) and L10 (2.1) keep the least float and rely on the cut ladder (guide section "Keeping to 90 minutes"). The pessimistic set still exceeds 90 in every lesson (91.7 to 98.7), as the audit expected; glitches, repeats and late arrivals are not modelled.

Differences from the audit's prediction: L3 +0.7 (the merged last-digit slide keeps its worked example), L10 -1.3 (see section 5: try2 was also cut), all others within 0.3.

## 3. What was applied, level-wide

- Warm-up: both sneak-peek puzzles stay, with one "show me" for both (slide, notes, guide SAY/DO); game played as two rounds; three quick questions on the slide and in the guide table. The cut questions are on a starred "Take-home" box at the bottom of the Go further page of each lesson workbook (L1 Q4/Q5, L2 Q4/Q5, L4 Q4/Q5, L5 Q4/Q5, L6 Q4/Q5, L7 Q4, L8 Q4, L9 Q4/Q5, L10 Q4/Q5); answers are in the tutor guide (a "Take-home questions" table under the quick questions). L3's cut question moved to talk time instead.
- Rooms: pre-assigned breakout rooms with auto-move and auto-close wording (explore1 and ws1 notes, title notes, guide routine table, Setting up online, L4/L5/L6/L8/L10 online set-up text); "what is on your desk" checklist and L6 "cut the strips out before class" added to the guide's one-week-before text.
- Page 1 has its real time on its slide (12 to 15.5 minutes = 2-minute start + about 1.5 of room moves + pair work); ws1 notes spell this out.
- Both answer slides are 60-second self-checks (title "Page N: self-check", 1.5 minutes, "how do you know" on one question only; L6 page 2 and L7 page 1 get 2). Answers stay on the slides.
- Guide: seg() times per lesson from `p3/budget.json`; routine table rewritten (ranges); new section "Keeping to 90 minutes" (float, cut ladder, never-cut list); "At about minute 52" check-in replaced by a check-in during page 2 so it no longer overlaps a check slide; "Choice" paragraph, explore, worksheet, exit, look-back minutes all derive from the lesson clock; REC minutes are the whole-minute length of the part (reccues.js untouched; decimal ranges are rounded in guide.js before calling it). Brain break text: 2 + 2 + 1, toilet before.
- Talk time notes and guide carry the float sentence. Title-slide "Time plan" notes are generated per lesson.
- L2 teachmagic and L10 teachbetween: "before page 2 (Q3)" fixed (L2 teachmagic now runs before page 1; L10 teachbetween deleted).

## 4. Lesson by lesson: cuts and moves

| Lesson | Slides removed (deck order, guide and notes) | Changed or moved | Worksheet (stars / take-home) |
|---|---|---|---|
| 1 | tryclues, teachsum (content kept in the Go further notes) | warm1 two rounds; page 1 = 13 min | Q4/Q5 quick questions to the take-home box |
| 2 | try2 (mini), teachshape | teachmagic moved before page 1; explore 4th instruction moved to the Go further card; pair work about 6.5 min | Q2(c) starred take-home |
| 3 | we1 merged into try1 (one slide) | predict SAY about 35 words; warmIntro sentence dropped; explore: tutor does the 6s, pairs make only the 4s, 8s on the Go further card; 6 x 8 vs 7 x 7 to talk time; teachgrid kept (Q4 is if time; may start with Q5) | none (Q4/Q6 already if time) |
| 4 | tryunits | teachsame moved into talk time; 3-times towers become debrief question 1, "22 cubes" to talk time; Ravi's mistake to talk time; page 2 window 7.5 | Q5(b) and Q6 marked (if time); Q4/Q5 quick questions take-home |
| 5 | teachtable | self-checks, rooms | Q4/Q5 quick questions take-home; Q3(b), Q4(b) stay (if time) |
| 6 | tryadd, teachpairs, teachbetween (teachbetween content moved to the Think harder notes) | explore: parents pre-cut strips, pairs only mark 1/2, 1/4, 1/8 and compare with printed strips; page 2 = Q4 + Q5 | Q1(c) and Q6 starred take-home |
| 7 | teachadd (content in Go further notes), we2 merged into try2 | teach1 trimmed to the essentials; explore 3-row table (1x12, 2x6, 3x4); page 1 = 14 min | square-root quick question take-home |
| 8 | try1 (content in the Think harder notes) | right-angle checker folded in Explore, Q1 only sorts (ws1 says so); fold twice and hunt | Q3(b) starred take-home; Q4 four letters (E, H, T, L), Z and N starred take-home; Q6 marked (if time); ruler quick question take-home |
| 9 | teach24 (content in Go further notes) | explore: two constraints, "exactly $20" kept as an extension line; mini slides shortened to 2/2.5/2.5; spare float used for page 1 (15.5 min) and talk time 8.5 | Q4/Q5 quick questions take-home |
| 10 | teachtable, teachbetween (one recap slide: teachlist retitled "Recap: draw it, list it, make a table"); we1 merged into try1; try2 | stations 4 minutes each with a switch, debrief question 1 plus the two answers on the slide; certificates one 20-second sentence each, volunteers once, parent summary posted after the lesson; exit ticket 2 minutes of work | quick questions 4/5 take-home |

## 5. Not applied exactly as the audit proposed, and why

- L9 keeps three quick questions (audit said L9 could keep five): the brief says three everywhere; L9 now has 7.3 minutes of float.
- L3 "use the spare 1.5 min for a longer page 2": applied as a 5-minute page 2 window and a note that Q5 may be started first; the workbook order (if-time Q4 before compulsory Q5) is unchanged because every answer and key must stay as printed.
- L10: the audit's merge of "the shortest worked example" was implemented as we1 merged into try1, and the logic-grid try-it (try2) was also cut (its content is in the we2 notes; worksheet Q2 is the practice). Without the second cut the model gave 90.7 minutes.
- L4 Q6 and L8 Q6 are marked "(if time)", not starred, because the audit demotes them (they stay on the worksheet) rather than sending them home; L8 Q4 Z/N and L6 Q1(c)/Q6, L2 Q2(c), L8 Q3(b) are starred "take-home".
- Quick questions moved to take-home are placed on one starred box on the Go further page because the workbook has no separate take-home page (and may not grow). Page counts: workbook 58 (unchanged, re-measured), tutor guide 102 (was 93; the new routine text, Keeping to 90 minutes section and take-home answer tables), weekly dose 25.
- Pills with decimal minutes (for example 25.5-27 MIN) are accurate to the budget; see note 1 for the lead.
- L9 has two orphan slide files (`p3l9-try2`, `p3l9-teachlist`) that were never in the deck order; left as they were.

## 6. Shared-file issues for the lead (not edited)

1. `tutor/build_data.py` assigns a slide to a part with `re.match(r'\s*(\d+)', pill)`: for pills such as "25.5-27 MIN" it reads 25 and puts the slide in the previous part. Use `(\d+(?:\.\d+)?)` and compare floats. Its PARTS table is now replaced by `p3/budget.json` for Level 3 (title, start, end, plus `optional_slides`; optional pills read "Optional, if you finish early", which its OPTIONAL regex already matches).
2. `levels/reccues.js` parses minutes with `(\d+)\s*[-–]\s*(\d+)`; with decimal ranges it would read "1.5-11" as 5-11. `p3/guide.js` works round it by passing whole-minute ranges; other levels will need the same if they adopt half-minute parts.
3. `docs/levels_and_placement.md`, `levels/*`, `hp/*`, `diag/*`, `website/*`, `rebuild/slidekit.py` untouched. The timing model files `docs/audit/timing_p3.py` and `.md` are unchanged; the new model run is `docs/audit/timing_p3_rebudget.py`.
4. REC and recording policy: the REC cue lines now give the new whole-minute part lengths; the earlier audit note about the recording policy still stands.
