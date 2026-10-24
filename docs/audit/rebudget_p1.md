# Level 1 re-budget pass (applies docs/audit/timing_p1.md)

All ten lessons now have a 90-minute plan that sums to 90 with a 2-minute standing buffer (Lesson 10: none, shortened plan). Source of every clock time: `rebuild/p1budget.py` (writes `hp/budget.json` for the tutor console and `hp/budget_slides.json` for the guide). Estimates are the audit's model, re-run on the repository as it is now (`python3 -I docs/audit/timing_p1.py --rebudget`); they are not stopwatch timings.

## 1. Budgets, old to new (minutes: start-end)

Old plan for every lesson: Opening 0-2, Warm-up 2-7, Sneak-peek 7-10, Explore 10-25, Mini-lesson 25-35, Break 35-40, Worksheet 40-72, Talk 72-80, Exit 80-88, Look-back 88-90.

| Part | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Opening | 0-4 | 0-2 | 0-2 | 0-2 | 0-2 | 0-2 | 0-2 | 0-2 | 0-2 | 0-2 |
| Warm-up | 4-10 | 2-8 | 2-8 | 2-8 | 2-8 | 2-8 | 2-8 | 2-8 | 2-8 | 2-6 |
| Sneak-peek | 10-14 | 8-12 | 8-12 | 8-12 | 8-12 | 8-12 | 8-12 | 8-12 | 8-12 | 6-10 |
| Explore | 14-28 | 12-26 | 12-26 | 12-26 | 12-26 | 12-26 | 12-28 | 12-26 | 12-27 | 10-28 |
| Mini-lesson | 28-38 | 26-36 | 26-37 | 26-37 | 26-36 | 26-36 | 28-36 | 26-36 | 27-37 | 28-37 |
| Brain break | 38-42 | 36-40 | 37-41 | 37-41 | 36-40 | 36-40 | 36-40 | 36-40 | 37-41 | 37-41 |
| Worksheet | 42-72 | 40-72 | 41-72 | 41-72 | 40-72 | 40-72 | 40-72 | 40-72 | 41-72 | 41-71 |
| Talk time | 72-79 | 72-79 | 72-79 | 72-79 | 72-79 | 72-79 | 72-79 | 72-79 | 72-79 | 71-79 |
| Exit ticket | 79-85 | 79-85 | 79-85 | 79-85 | 79-85 | 79-85 | 79-85 | 79-85 | 79-85 | 79-87 |
| Look-back | 85-88 | 85-88 | 85-88 | 85-88 | 85-88 | 85-88 | 85-88 | 85-88 | 85-88 | 87-90 |
| Flex time (buffer) | 88-90 | 88-90 | 88-90 | 88-90 | 88-90 | 88-90 | 88-90 | 88-90 | 88-90 | none |

The buffer is placed where the audit places it (section 7: the last 2 minutes, after the look-back), not after the page-2 check; it is never taken from the exit ticket, look-back or stamp. Worksheet page splits (slide clocks): L1 42-52 / check 52-54 / teach 54-58 / 58-68 / 68-72; L2 40-50 / 50-52 / 52-54 / 54-66 / 66-72; L3 41-50 / 50-52 / 52-55 / 55-67 / 67-72; L4 41-53 / 53-55 / 55-67 / 67-72; L10 41-53 / 53-55 / 55-67 / 67-71; others unchanged (page 2 58-68, check 68-72). Explore is split 5 + rest (L7 6 + 10; L10 plan 1 + 6 + 11).

## 2. Applied

* **Universal.** Warm-up asks quick questions 1-3, 4-5 only if on time (marked "(if on time)" on the slide, guide, notes). Sneak-peek: one 25-word line and ONE camera moment after the second question. Break 4 minutes. Talk 7, exit 6, look-back 3 (workbook box and slide now say "Three minutes"), flex time. Clock checks, flex time and skip list printed in the guide (routine chapter) and in the Lesson 1 routine-slide notes; guide worksheet lines say "go straight to Talk time". All `Minutes a to b`, "At minute 40", the title-slide time plan, the routine table (slide and guide) follow the budget.
* **Optional slides** are labelled "Optional, if you finish early" with no clock (L10's three re-teach slides: "Optional, if you need a reminder"). They stay in deck order right after the page-2 check; `optional_slides` in `hp/budget.json` lets the console skip them.
* **L1:** cover slide dropped; routine slide 30 s, four phases; opening 4; parents cut and tape the strip (lessons.js, title/explore notes, guide set-up, email pack week 1).
* **L2:** `l2-try3` dropped; worksheet re-split (page 2 gets 12 minutes); magic triangle and hint kept.
* **L3:** `l3-try3` merged into `l3-teach3` as one "your turn" (a); (b), (c) moved to a star "Take-home" card on the Think harder slide; third think-aloud quote cut in scripts.js; `l3-ws1`/`ws1ans` now list Q1-Q4 and Q5 moved to page 2 slides (matches the printed pages).
* **L4:** four Core items from the Question Bank added (circle/square/triangle 10th; red red blue 8th on page 1; cat dog dog 12th; A B C D 11th on page 2). Questions renumbered Q1-Q8 (old Q2 = Q4, Q3 = Q7, Q4 = Q8); slides, key (`lessons.js`) and workbook updated; answers of old items unchanged.
* **L5:** Q5 marked with a star and "Take-home (if you have time, or at home)". `teachq1`/`teachq2`: the "your turn" already appears only once (teachq2), so no change.
* **L6:** two "your turn" slides added to the Mini-lesson (`l6-try2` core 1, 2, 3 and `l6-try3` core 5, 6); Q5 and Q6 (count the money, 35c and 45c) added at the end of page 2; key updated.
* **L7:** re-budget only (explore 16, mini 8); guide says skip the six optional slides.
* **L8:** `teachriddle` and `teachodd` show all steps at once, 30 s each, notes shortened; the non-idempotent "together together" repeat in `l8-warm1` fixed.
* **L9:** Q2 reuses the Explore numbers (workbook + slide), only "My choice" is new; parents cut the cube strip (lessons.js, notes, email pack week 5); `l9-tryconv` dropped; break "giant steps in place"; teaching slides now use 1 clip = 2 erasers like the printed Q4 (answers unchanged).
* **L10:** `l10-warm2`, `l10-try1`, `l10-try2` dropped; cards 6 min, swap, round 2 four minutes, ONE debrief question (slide reduced to it), 20 s pair reports, pairs read their own card; reminder slides optional; Q9 written on page 2 (slides, workbook wording), talk time = swap, solve, pair talk, volunteers; certificates said once then 10 s per child, `end` slide moved before the look-back (84-87); scripts trimmed (think-aloud 4 to 2, warm-up, predict, talk, close).
* Rebuilt: decks (gen_l1..l10 + restyle), workbook pdf/docx, guide docx/pdf, weekly PDFs, email pack, tracker, scheme (all copied to `outputs/`). Question bank and Weekly Dose unchanged (qbank.json not edited).

## 3. New estimated totals

| Lesson | Need (base) | Fast - slow | Audit predicted | Diff | Slack to 90 incl. buffer |
|---|---:|---|---:|---:|---:|
| 1 | 83.6 | 73.4 - 94.3 | 82.9 | +0.7 | 6.4 |
| 2 | 87.3 | 76.5 - 98.5 | 86.6 | +0.7 | 2.7 |
| 3 | 86.3 | 75.7 - 97.3 | 85.7 | +0.6 | 3.7 |
| 4 | 85.9 | 75.9 - 96.3 | 83.3 | +2.6 | 4.1 |
| 5 | 84.8 | 74.4 - 95.7 | 84.2 | +0.6 | 5.2 |
| 6 | 84.3 | 74.6 - 94.4 | 85.5 | -1.2 | 5.7 |
| 7 | 84.8 | 74.5 - 95.6 | 84.2 | +0.6 | 5.2 |
| 8 | 87.3 | 76.9 - 98.3 | 85.6 | +1.7 | 2.7 |
| 9 | 86.6 | 76.2 - 97.6 | 86.4 | +0.2 | 3.4 |
| 10 | 86.6 | 76.0 - 97.5 | 86.6 | 0.0 | 3.4 |

Differences from the audit come from the REC cues (not shortened, see 5), real slide sets, and item times in L4 (+0.7 item cost and four added items). Per-part tables: run `python3 -I docs/audit/timing_p1.py --rebudget`. All lessons now fit the base case (previously L9 +6, L10 +15 over; L4 -11, L6 -8 short). The slow case (about +11) still needs the skip list, as the audit said.

## 4. Page counts

Workbook 58 pages (unchanged; each lesson still 2 Start-here pages + look-back + Think harder + Go further; L4 page 1 = Q1-Q4, page 2 = Q5-Q8; L6 page 2 = Q3-Q6). Tutor guide 93 pages (was 90 in the committed PDF). Email pack 7, weekly PDFs rebuilt.

## 5. Not applied, and shared-file issues for the lead

* **U4, shorter REC cue lines** (~20 words): the cues live in `levels/reccues.js` (shared, not edited). The guide still says "under ten seconds" while the cues run 8-20 s; the model therefore keeps 2.2 min of REC. Applying U4 would save about 0.6 min a lesson.
* **`levels/scheme.py`** still prints the old routine ("warm-up (10 min), explore (15), mini-lesson (10), brain break (5) ..., exit ticket and journal stamp (10)"); it should say warm-up and sneak-peek 12 (2-12), explore 14, mini-lesson 10, break 4, worksheet 32, talk 7, exit 6, look-back 3, flex 2.
* Buffer placement: the brief said "usually after check-together page 2"; the audit puts it at 88-90, so that is what was applied.
* L5 `teachq1`/`teachq2`: nothing to cut (already one "your turn").
* L3 (b),(c) take-home appear on the Think harder slide and in notes, not as new printed workbook items (the audit puts them on the slide).
* Tight spots left as the audit predicted: L10 warm-up (-0.7) and exit (-0.2), L1 talk (-0.3); LOW children still finish about 2-6 of the required Start-here items, so "pass is fine" stays the rule.
