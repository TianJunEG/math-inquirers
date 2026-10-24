# Level 5 re-budget (every lesson fits 90 minutes live online)

Applies `docs/audit/timing_p5.md` (sections 6 to 8) to the ten Level 5 lessons, on top of the fix pass in `docs/audit/reaudit_fixes_p5.md` (29 to 31 slides, numbered Q1-Q6 / A1-A4 / B1-B3 / C, computed choice line, 30-second think time). Nothing committed. Not touched: `diag/*`, `levels/*`, `rebuild/slidekit.py`, `hp/*`, `website/*`, `tutor/*`, `docs/levels_and_placement.md`.

## Where the minutes live now

* `rebuild/p5_budget.py` is the one source: part budgets (audit section 7, every lesson sums to 90), the clock window of every slide, the cut slides, the optional slides. Run `python3 rebuild/p5_budget.py` to write `p5/budget.json` (it lists only the optional slides actually in each deck).
* `rebuild/p5_gaps.py` (called at the end of every `gen_p5lK.py`) rewrites every time pill, every leading "Minutes a to b" in the speaker notes and the title-slide "Time plan" from that table. The old literals left in the generators ('9-14 MIN' and so on) are overwritten there: change minutes in `p5_budget.py` only.
* `p5/data.js` builds the routine table from `p5/budget.json` (ranges over the ten lessons); `p5/guide.js` reads `p5/budget.json` for every `pushSeg()` time. The recording cues (the `REC` require of `../levels/reccues.js`, `rec()`, `pushSeg()`, "Watching the recording" header row, chapter table, "Recording the lesson" front section, policy sentences) were already in `p5/guide.js` and in the same form as `p4/guide.js`; nothing had to be added. `reccues.js` reads whole minutes only, so `pushSeg` passes it the rounded length (the printed seg time keeps the half minutes).
* The guide's workbook segment now runs from the start of page 1 to the end of the page-2 check (was labelled 37-72 but ran to 76) and each lesson has a final seg for the Buffer.

## Old to new budgets (minutes)

Old = the same for every lesson. The Buffer is the audit's leftover (1 to 5), the last part of the lesson, unscripted.

| Part | Old | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Opening (now inside the clock) | 0 | 2 | 2 | 2 | 2 | 3.5 | 2 | 2 | 2 | 2 | 2 |
| Sneak-peek | 3 | 4.5 | 4.5 | 4.5 | 4.5 | 4.5 | 4 | 4.5 | 4 | 4.5 | 4.5 |
| Warm-up | 6 | 6 | 6.5 | 6.5 | 6 | 6.5 | 6 | 5.5 | 6 | 5.5 | 6.5 |
| Explore | 12 | 14 | 14 | 13.5 | 13 | 13.5 | 14 | 12.5 | 12.5 | 13.5 | 14.5 |
| Mini-lesson | 12 | 11 | 11 | 12 | 11 | 12 | 12.5 | 11 | 12 | 11.5 | 10.5 |
| Brain break | 4 | 4.5 | 4 | 4 | 4.5 | 4.5 | 4 | 4.5 | 4.5 | 4 | 4 |
| Worksheet page 1 (pairs) | 12 | 14.5 | 15.5 | 14 | 12.5 | 15 | 14.5 | 14 | 13 | 14 | 13.5 |
| Check page 1 | 4 | 4 | 4 | 3.5 | 3.5 | 3.5 | 4 | 3.5 | 3.5 | 4 | 3 |
| Short teaching | 5 | 3 | 1.5 | 1.5 | 3 | 0 | 1.5 | 1.5 | 3 | 3.5 | 2 |
| Worksheet page 2 (alone) | 14 | 8 | 8 | 8 | 10 | 7 | 9 | 11.5 | 7.5 | 9 | 7.5 |
| Check page 2 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| Talk time | 6 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 |
| Exit ticket, reflection, close | 8 | 8 | 8 | 9.5 | 7 | 8.5 | 8.5 | 9 | 8.5 | 9 | 10.5 |
| Buffer | 0 | 2 | 2.5 | 3.5 | 4.5 | 4 | 1.5 | 2 | 5 | 1 | 3 |
| Total | 90 | 90 | 90 | 90 | 90 | 90 | 90 | 90 | 90 | 90 | 90 |

Exit/reflection/close is split 'exit ticket = the rest', reflection 2.5 (75 seconds of writing plus the slide), close 1 (stamp typed in the chat, goodbye); Lesson 10 close is 3.5 (certificates, 12 seconds each, last stamp typed).
Explore is split explore1 = budget minus 4, explore2 = 4 (two regroup questions plus the guesses). Pair work is stated as 6 minutes (6.5 in L4 and L8 where pairs stay in the main room, 5.5 in L9) in the explore notes and the guide: "Pencils down" is said at the start of explore2.

## What changed in every lesson

* Opening: inside the clock; one-paragraph hook, wave and chat greeting, one-sentence recording notice (guide DO line and title-slide note).
* Sneak-peek: one hold-up for both puzzles, no volunteer round, one-line intro "Guessing is welcome. Nobody is marked." (slide, notes, `data.js` script, guide bullet); each answer said with one short reason. L4 puzzle 1 is answered by drawing only (no cutting).
* Warm-up: four quick questions (the fifth was dropped from the slide, the notes and `deck.warmQs`; question 4 is the first rung of the cut-first ladder) and ONE game round (L1 and L9 no longer say "3 rounds" or "Rounds 2 and 3").
* Explore: two regroup questions (the third is in the notes as "not asked together" or moved to the Go further what-if); pair work capped; "Pencils down" minute printed. L1 10 million seconds and L9 the rule for 8 and 30 children went into the what-if; L6 the 430-page job went into the what-if; L2 "5 pizzas among 6" stays only as the Go further step; L9 table stops at 6 children; L10 each pair solves ONE puzzle card and teaches it, the second card is the what-if; L4 parents draw the 8 by 6 rectangle the day before (the workbook cut-out page itself was not changed).
* Mini-lesson: every Your-turn slide has items a and b only (a note says so); L5 `teachlist`, L9 `try3`, L10 `try2` removed.
* Worksheet: parts that moved to take-home carry a star and the words "take-home" in the workbook (source `p5/content/take.js`); page 1 shows the legend "star take-home parts are for home"; the Investigation page says the first step is take-home (or the start of the next lesson). The slides (`ws1`, `ws2`, check slides) list in-class and take-home items, and every check slide keeps all answers (the notes say one pair explains the heaviest question, the tutor clicks through the rest, take-home answers are there for the tutor). Keys, tier labels, pass option, private-paper rules unchanged.
* Choice line: `choiceQ(n)` in `p5/data.js` is now the last question to do in class on page 1 (a question starred take-home or done in the page 2 time is not counted): 3 in L1, L5, L6, L7; 2 in L2, L3, L4, L8, L9, L10 (L2 and L10 changed).
* Page 2 plan lines (`solo` in `gaps.js`, printed on page 2, slide and guide) name the in-class items only. New fields `p1` and `take` in `gaps.js` feed the guide (header rows "Take-home" and "Clock checkpoints") and the ws1 notes.
* Talk time: 30 seconds silent thinking, pairs 2 minutes, volunteers 1.5 minutes; the Investigation first step is take-home (script, slide card, notes, TIMELINE row). Second talk questions that pointed at take-home items (L1 Q6, L2 Q4) were re-pointed at in-class items.
* Exit: typed stamp (guide, reflect-slide notes); reflection about 75 seconds with a one-tick version when late; L10 certificates 12 seconds each.
* Optional slides (Think harder, Go further, extras, L7 `teachchange` and `teachdeal`): pill "Optional, if you finish early", no clock time, `OPTNOTE` in the notes; the explore-slide what-if card says "OPTIONAL, IF YOU FINISH EARLY".
* Guide: routine table with ranges, cut-first ladder (Investigation first step, quick question 4, Go further what-if, last in-class item of page 2, reflection to one tick), the buffer, per-lesson clock checkpoints, per-lesson seg times (fixes the 37-72 label).

## Per lesson: cut, moved to take-home, in class

| L | Slides cut | In class (page 1 / page 2) | Take-home (starred) |
|---|---|---|---|
| 1 | `trybrackets`, `teachfind` | Q2 a b, Q3 a-c / Q4 a-d, Q5 a b (+ `teachest`, `teachbrackets`) | Q1; Q5 c, Q6 |
| 2 | `teachpattern`, `teachboth` | Q1 a b, Q2 a b / Q5 a b, Q4 a (+ `teachback`) | Q3; Q4 b c, Q6 |
| 3 | `trydiff`, `teachone` | Q1 a-c, Q2 a b / Q4 (+ `teachdiff`) | Q3, Q5 (Q3 removed from the page-1 slides) |
| 4 | `teachsplit` | Q1, Q2 / Q5, Q4 (+ `teachtake`, `teachsame`) | Q3 |
| 5 | `teachlist`, `teachpaint`, `teachpour` | Q2 a b, Q3 a b / Q4 a-c (no teaching slide) | Q1, Q3 c; Q5, Q6 |
| 6 | `teachpark` | Q1 a b, Q2 a b, Q3 a / Q4 a b, Q6 a (+ `teachplans`) | Q3 b c; Q5, Q6 b c |
| 7 | `teachtable` | Q1 a b, Q3 a-c / Q2 a-d (printed on page 1, "Do this in the page 2 time"), Q4 a-c (+ `teachrem`) | Q4 d, Q5 |
| 8 | `teachcases` | Q1 a-d, Q2 a b / Q3 b, Q4 a b (+ `teachchain`, `teachcombo`) | Q2 c; Q3 c d, Q5 |
| 9 | `try3`, `teachmarks` | Q1 a b, Q2 a b / Q3, Q4 a (+ `teachgs`, `teachsup`) | Q1 c d, Q2 c; Q4 b, Q5 |
| 10 | `try2`, `teachliar`, `teachage` | Q1, Q2 / Q3 (printed on page 1, "Do this in the page 2 time"), Q4 a (+ `teachsq`) | Q4 b c, Q5, Q6 |

Other text cuts: L1 and L5 hook shortened to one paragraph; L6 brain break is one 60-second star-jump count; L10 warm-up relay is six cards (angles and patterns are in the quick questions).

## New totals (timing model re-run on the rebuilt decks)

`python3 docs/audit/rebudget_p5.py` (wrapper on `timing_p5.py`, fix scenario of the audit, same constants, judgement inputs unchanged because the in-class item sets are the audit's). Sum of the parts' needs with the two worksheet blocks counted at their budget; every part's need is within its budget (no part is 0.75 minute or more over; the largest is Exit in L10, 10.2 of 10.5).

| Lesson | Slides in deck | Estimated total (min) | Audit's old total | Budget sum | Slack the buffer covers | Buffer held |
|---|---|---|---|---|---|---|
| 1 | 28 | 85.4 | 110 | 90 | 4.6 | 2 |
| 2 | 27 | 85.0 | 107 | 90 | 5.0 | 2.5 |
| 3 | 27 | 83.4 | 109 | 90 | 6.6 | 3.5 |
| 4 | 30 | 82.0 | 102 | 90 | 8.0 | 4.5 |
| 5 | 27 | 82.9 | 111 | 90 | 7.1 | 4 |
| 6 | 29 | 86.3 | 106 | 90 | 3.7 | 1.5 |
| 7 | 29 | 85.1 | 100 | 90 | 4.9 | 2 |
| 8 | 29 | 82.2 | 102 | 90 | 7.8 | 5 |
| 9 | 28 | 86.4 | 113 | 90 | 3.6 | 1 |
| 10 | 28 | 83.9 | 115 | 90 | 6.1 | 3 |

The audit predicted exactly 90 with 1 to 5 minutes of buffer, because it rounds each part's need up to the half minute; the model's unrounded needs sum to 82.0-86.4, so the budgets are met everywhere with 3.6-8.0 minutes of slack, of which the named buffer (1-5) is the planned part. Estimates, not stopwatch times; the audit's plus or minus range still applies (the buffer covers ordinary slippage, the cut-first ladder the rest).

## Page counts (rebuilt)

Student workbook 57 (unchanged, 5 pages per lesson; per-page structure checked). Tutor guide 109 (was 102: routine ladder, per-lesson rows and the buffer seg). Weekly dose pack 26, question bank 28, weekly email pack 12, free taster 5, What Learners Get 1 (all unchanged). Decks: 28, 27, 27, 30, 27, 29, 29, 29, 28, 28 slides (was 30, 29, 29, 31, 30, 30, 30, 30, 30, 31). `rebuild/preview.py`: no slide overflows in any deck.

## Not applied, and why

* L4 "print the 8 by 6 rectangle on the grid cut-out page": the cut-out page is `p5/kit.js`, which would change the workbook pages; instead parents are asked to draw it the day before (materials text and explore note).
* L7 and L10: the audit moves Q2 (L7) and Q3 (L10) to page 2. Moving them physically would grow page 2 or renumber the keys, so they stay printed on page 1 with the marker "Do this in the page 2 time" and are checked on the page-2 check slide.
* Take-home items that lost their teaching slide (L5 Q5 and Q6, L1 Q6, L2 pattern and "largest and smallest" sums, L3 beads, L4 split, L6 car park, L7 table, L8 every-case, L9 marks, L10 liar and ages) have no slide any more, as the audit says; their Start-here lines in the workbook are the only support. The tutor should hand out the take-home answers with the next lesson's opener if parents ask.
* The 3-minute standing buffer is the audit's per-lesson leftover (1 to 5 minutes, average 2.9). L9 (1 minute) and L6 (1.5) are tight; the guide tells the tutor to use the typed stamp and the one-tick reflection first.
* The model assumes breakout rooms in the lessons that use them (L1, L2, L6, L9, L10); the audit's caveat that L3, L4, L5, L7, L8 add about 3 minutes if they also use breakouts for explore and page 1 still holds and is covered by the buffer plus the ladder.

## For the lead (shared files)

* `tutor/build_data.py` has `PARTS` for Level 4 only; Level 5 should read `p5/budget.json` (parts with title, start, end; optional slide ids). The Level 5 pill text for optional slides is now "Optional, if you finish early".
* `levels/reccues.js` `mins()` reads whole minutes only; with half-minute parts the cue is rounded by the guide (not a defect, but a half-minute-aware version would be cleaner).
* `levels/mkextras.py` lines 283 and 340 still print "fast finishers" and the Challenge Screening Set wording (already noted in `reaudit_fixes_p5.md`).
