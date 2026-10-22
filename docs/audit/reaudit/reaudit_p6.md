# Math Inquirers P6: RE-AUDIT after the fix passes
Date 2026-10-22. Read-only. Repo untouched. Same method and scales as the three baselines (audit_p6, gifted_p6, journey_p6 Part 1). Files were not mid-edit when read.
Independent checks: `scratchpad/recheck.py` (263 answer checks across all 10 lessons: 261 pass; the 2 "fails" are bugs in my own checks, a k=1 star filter and a Fraction-vs-float compare; the content is right) and `scratchpad/stage.py` (L7 stage fit). I found NO wrong answer in any lesson (Core, Think Harder, Challenge, sneak peeks, Investigation, Go further, exit slips, Scratch traces). Limit: still a paper review. No child used it, and the Scratch editor was not run (no .sb3 files exist in the repo).

## 1. Content audit (baseline audit_p6.md)

### 1.1 Verdicts per lesson
| Lesson | Before | After | Move | Why |
|---|---|---|---|---|
| 1 Code the Pattern | minor fix | OK | improved | Q5 now `say ... for 1 seconds`, so the child can see the 20 terms. Sneak peeks (9 sticks, $43) are correct. Note: the Think Harder SLIDE and the printed page differ (see N1). |
| 2 Prime Hunters | minor fix | minor fix | same (better) | Q6 say-loop fixed. ws2 still carries Q3-Q6 (about 35 answers) in a short slot, and lesson 2 still stacks if + mod + counter + if/else. |
| 3 Below Zero | OK | OK | same | Challenge 9 vs "0 = ground floor" now consistent (my check: 4 to B3 is 6 moves). New nit N2: TH repeats Core. |
| 4 Algebra Machines | minor fix | OK | improved | "Sensing is purple" gone; Q1 tables are all step 1. |
| 5 Every Possible Way | minor fix | OK | improved | "when start clicked" gone from every file (grep: 0 hits). Hat is "when green flag clicked". |
| 6 Fair or Unfair? | minor fix | OK | improved | Same hat fix. Probability is still beyond Sec 1: an enrichment topic and the lesson says so. |
| 7 Turtle Geometry | needs rework | minor fix | improved | Four set-up blocks, `turn ↻`, stage size and move sizes are now stated (deck7 slide notes). Remaining: N3 below. |
| 8 Secret Codes | needs rework | minor fix | improved | The whole machine is specified and spaces are protected by an if/else on `item # of`. The "alphabet" starter `.sb3` is still not in the repo. |
| 9 Data Detectives | minor fix | minor fix | same | "Holiday Program" footer gone. Core is still PSLE revision (mean, total = mean x n); the new maths is median and mode only. |
| 10 Showcase Challenge | needs rework | minor fix | improved | Showcase is now two rounds of 4 at 2:30 + 20 s switch (62-85, 23 min, fits). Four starters (A-D) are still not in the repo. |

Counts. Before: OK 1, minor fix 6, needs rework 3. After: OK 5 (L1, L3, L4, L5, L6), minor fix 5 (L2, L7, L8, L9, L10), needs rework 0.

### 1.2 Baseline findings, status (24 items; numbering follows my reading of the baseline's issue list)
| # | Baseline finding | Status |
|---|---|---|
| 1 | "when start clicked" hat (L5, L6) | FIXED |
| 2 | L1 Q5 and L2 Q6 plain `say` in a loop | FIXED |
| 3 | L7 programs off stage / set-up missing | PARTLY (see N3) |
| 4 | L7 "turn right" label | FIXED (`turn ↻`, "clockwise arrow") |
| 5 | L8 cipher machine under-specified, spaces mis-coded | FIXED on paper; not testable |
| 6 | Block colours wrong (Sensing purple, list colours) | PARTLY: slides say "find blocks by category name"; purple claim gone |
| 7 | "Send four starter blocks in chat" impossible | FIXED (tutor shares file/screen) |
| 8 | L10 plan-build-present in about 13 min | PARTLY: build window is now 32-62 (30 min), which fits |
| 9 | L10 showcase 8 x 3:20 in 24 min | FIXED (two rounds of 4, 23 min) |
| 10 | Starter `.sb3` files missing (L5, L8, L10, L7 start file) | NOT FIXED: the notes say "no .sb3 exists in this repository, build it beforehand". Honest, but still a tutor chore |
| 11 | L2 ws2 about 35 answers in 6 min | NOT FIXED (partly eased by moving items to TH) |
| 12 | L5 ws2 about 25 answers in 7 min | PARTLY |
| 13 | L6 Q4 table + Q5 in 8 min | PARTLY |
| 14 | L3 Challenge 9 changes the floor convention | FIXED |
| 15 | No primer for children new to Scratch | NOT FIXED |
| 16 | L7 TH items abstract/ambiguous (8, 9) | FIXED (square + octagon + octagon; hexagon vs 120) |
| 17 | L5 teachcode note wording | FIXED ("23 and 24 which are not real outfits") |
| 18 | L4 Q1(c) steps IN by 2 | FIXED |
| 19 | L9 maths too familiar | NOT FIXED (inherent; Go further and Investigation help) |
| 20 | Footers "P6 Holiday Program" | FIXED |
| 21 | Brain breaks unchanged | NOT FIXED (cosmetic) |
| 22 | "Dice" wording | NOT FIXED (cosmetic) |
| 23 | L8 Python corner (optional) | SAME (acceptable, optional) |
| 24 | Fence-post / answer keys | no error found |
Counts: FIXED 13, PARTLY 4, NOT FIXED 5, SAME/no error 2.

### 1.3 New problems introduced or still open (exact place and fix)
- **N1 "you you" typo, NOT FIXED although fixpass_p6.md says it is.** Present once in every `p6lN-reflect` slide note (deck1..deck10) and 10 times in the Tutor Guide. Source `p6/guide.js` about line 162: `say "you you counted the jumps..."`. Fix: delete the extra "you" before `reflectEx` (or drop the "you" from `reflectEx`).
- **N1b Think Harder slide differs from the printed Think Harder page.** `data.js`: `th = stretch.slice(0, 4 - moved.length).concat(moved)`; the page shows those, but the slide shows the older stretch list. L1: page has "Find the 100th term of 12, 19, 26, 33" and the moved item; the slide shows "The 5th term is 23..." and "1st term 4, 10th term 40". A tutor reading answers off the slide will not match the child's page. Fix: build the slide from the same `th` array, and check the same for L2-L10.
- **N2 L3 Think Harder repeats Core** (same -7 + 12 / 5 - 13 skills, new numbers only). Fix: replace two TH items with a "two-move" or "unknown start" item (a - b = 7 pairs, as the Investigation does).
- **N3 L7 workbook page 1 Q1** says "move 80, but 30 for 24 sides and 10 for 36", and the table has a 15-sided row (turn 24). My simulation from (-50, 100) heading 90: 15-gon with move 80 reaches y = -281 and x = -201 to 181, so it runs off the stage (the stage floor is -180). The deck notes say 12-15 sides use move 50 (that fits: y min -138) but the page does not. Everything else I simulated fits: octagon/9-gon/10-gon at 80, 24-gon at 30, 36-gon at 10, stars {5/2} 150, {8/3} 200, {9/2} 150, {9/4} 120, {20/3} 100, {10/3} 150, rosette from (0, 0). Fix: change the Q1 sentence to "move 80 up to 10 sides, 50 for 12 to 15 sides, 30 for 24, 10 for 36".
- **N4 Parent-facing text still says "Challenge for strong thinkers"** (`Weekly_Dose_of_Thinking_Math`, `What_Learners_Get`). It contradicts the neutral page names and "never say advanced" rule. Fix: "Challenge: for anyone who wants more".
- **N5 Reflection timing is inconsistent**: the notes put "Looking back" at 88-90 in L10 but "while you collect exit tickets" elsewhere. Fix: one fixed 2 min slot after the exit slip in every lesson.
- Safeguarding rule holds: sneak-peek and Finish-page notes say "Never private chat", answers shown to camera at the same moment, nobody singled out. I found no remaining instruction to message a child privately (grep of fast-track / private in all outputs).

## 2. Gifted-style rubric (baseline gifted_p6.md, 12 criteria, 0/1/2)
Scoring rule I used: start from the baseline "before" score, add the tier-compliance gains the baseline itself projected (criteria 1, 6, 9; I checked them as delivered), add +1 on criterion 10 (the Looking back box asks for the strategy used, what was hard, what next; L10 already had it), and keep criterion 11 at 1: a self-chosen page is flexibility, but there is still no skip-ahead route for a child who has mastered the material, so it is not compacting. Criterion 7 stays at the shared-routine score. -1 on criterion 6 for L1 because the slide and page ladders disagree (N1b); not verified for the other lessons, so the same -1 may apply there.

| Lesson | Before | Baseline's projected "after" | Re-audit now | Change vs before | Band now |
|---|---|---|---|---|---|
| 1 Code the Pattern | 18 | 20 | 20 | +2 | 20-24 |
| 2 Prime Hunters | 15 | 17 | 18 | +3 | 12-19 |
| 3 Below Zero | 13 | 16 | 17 | +4 | 12-19 |
| 4 Algebra Machines | 19 | 19 | 20 | +1 | 20-24 |
| 5 Every Possible Way | 18 | 18 | 19 | +1 | 12-19 (top) |
| 6 Fair or Unfair? | 16 | 18 | 19 | +3 | 12-19 (top) |
| 7 Turtle Geometry | 16 | 18 | 19 | +3 | 12-19 (top) |
| 8 Secret Codes | 15 | 17 | 18 | +3 | 12-19 |
| 9 Data Detectives | 18 | 20 | 20 | +2 | 20-24 |
| 10 Showcase Challenge | 20 | 20 | 20 | 0 | 20-24 |
| **Mean** | **16.8** | **18.3** | **19.0** | **+2.2** | |

Tier compliance: the printed Core, Think Harder and Challenge items follow the tier principle (Core needs no taught method). I found no Core item that needs the lesson's new method. Remaining ceilings: (a) no compacting route (criterion 11 is 1 everywhere); (b) criterion 12 stays 1 in L2, L3, L4, L6, L7 (Sec 1 content taught early, as the SPEC states); (c) L9 Core is revision. Direction: no lesson dropped; four lessons now reach the 20-24 band (L1, L4, L9, L10), none is under 12.

## 3. Student journey (baseline journey_p6.md Part 1)
Scale: P D F C M S, 1-5, D scored 5 = just right. Cells are my judgement from the slides, scripts and workbook. Changes are small because the worksheet load, the 10 minute teaching blocks and the set-up in L7 are unchanged.
Reasons for movement: sneak-peek puzzles replace the public pre-test (C up for LOW, S up in L1/L2/L10); Puzzle 1 is an access puzzle everyone can start (P/D); Investigation and Go further are now visible to the whole group on the Finish page and announced to everyone (M up for HIGH); L10 showcase no longer overruns or leaves HIGH waiting 20 min; FASTPTR chip is neutral (no "did not qualify" text).

### 3.1 Heatmap (lesson mean, before -> after, delta)
| Lesson | LOW | MID | HIGH |
|---|---|---|---|
| 1 Code the Pattern | 2.67 -> 3.17 (+0.50) | 3.67 -> 3.83 (+0.17) | 3.83 -> 4.00 (+0.17) |
| 2 Prime Hunters | 2.50 -> 3.00 (+0.50) | 3.50 -> 3.67 (+0.17) | 4.00 -> 4.17 (+0.17) |
| 3 Below Zero | 3.33 -> 3.50 (+0.17) | 4.17 -> 4.17 (0) | 3.83 -> 3.83 (0) |
| 4 Algebra Machines | 2.50 -> 2.83 (+0.33) | 3.67 -> 3.83 (+0.17) | 4.00 -> 4.17 (+0.17) |
| 5 Every Possible Way | 3.00 -> 3.17 (+0.17) | 4.00 -> 4.00 (0) | 4.17 -> 4.33 (+0.17) |
| 6 Fair or Unfair? | 3.00 -> 3.17 (+0.17) | 4.33 -> 4.33 (0) | 4.33 -> 4.50 (+0.17) |
| 7 Turtle Geometry | 2.17 -> 2.33 (+0.17) | 3.50 -> 3.67 (+0.17) | 4.33 -> 4.33 (0) |
| 8 Secret Codes | 3.00 -> 3.17 (+0.17) | 4.17 -> 4.17 (0) | 4.50 -> 4.50 (0) |
| 9 Data Detectives | 3.33 -> 3.50 (+0.17) | 4.17 -> 4.17 (0) | 3.33 -> 3.50 (+0.17) |
| 10 Showcase Challenge | 2.33 -> 2.67 (+0.33) | 3.50 -> 3.67 (+0.17) | 4.17 -> 4.33 (+0.17) |
| **Level mean** | **2.78 -> 3.05 (+0.27)** | **3.87 -> 3.95 (+0.08)** | **4.05 -> 4.17 (+0.12)** |
No cell dropped. Improved 22 of 30 cells, same 8. LOW is still the weak persona: L7 (2.33), L10 (2.67), L2 (3.00) and L4 (2.83) are below 3.

### 3.2 Per-cell scores (P D F C M S; was in brackets)
| L | LOW | MID | HIGH |
|---|---|---|---|
| 1 | 3 3 3 4 3 3 (3 2 3 3 3 2) | 4 4 4 4 4 3 (4 4 4 3 4 3) | 5 3 4 4 5 3 (5 3 4 4 4 3) |
| 2 | 3 2 3 4 3 3 (3 2 3 2 3 2) | 4 3 4 4 4 3 (4 3 4 3 4 3) | 5 3 4 4 5 4 (5 3 4 4 4 4) |
| 3 | 4 3 4 4 3 3 (4 3 4 3 3 3) | 5 4 4 4 4 4 (same) | 5 3 4 4 4 3 (same) |
| 4 | 3 3 3 3 3 2 (3 2 3 2 3 2) | 4 3 4 4 4 4 (4 3 4 3 4 4) | 5 3 4 4 5 4 (5 3 4 4 4 4) |
| 5 | 3 2 4 4 3 3 (3 2 4 3 3 3) | 4 3 5 4 4 4 (same) | 5 3 5 4 5 4 (5 3 5 4 4 4) |
| 6 | 4 2 4 3 3 3 (4 2 4 2 3 3) | 5 4 5 4 4 4 (same) | 5 4 5 4 5 4 (5 3 5 4 5 4) |
| 7 | 2 1 3 3 3 2 (2 1 3 2 3 2) | 3 3 4 4 4 4 (3 3 4 3 4 4) | 4 4 5 4 5 4 (same) |
| 8 | 4 2 4 3 3 3 (4 2 4 2 3 3) | 4 3 5 4 5 4 (same) | 5 4 5 4 5 4 (same) |
| 9 | 4 4 3 4 3 3 (4 4 3 3 3 3) | 5 4 4 4 4 4 (same) | 5 2 3 4 4 3 (5 2 3 4 3 3) |
| 10 | 3 2 3 3 3 2 (3 2 3 2 3 1) | 4 3 4 3 4 4 (4 3 4 3 4 3) | 5 3 5 4 5 4 (5 3 5 4 5 3) |

### 3.3 Remaining and new journey problems, with a fix
1. **L7 LOW (2.33, the worst cell).** Set-up is still about 10 minutes (`setup` slide, deck7 minute 10 to 21), and wb page 1 still opens with a 6-row table using "turn", "inside angle" and "total turning" before they are used. Fix: split the table, give rows 1-2 as examples, move the ws2 9-row trace to the Think Harder page for anyone who wants it, and ship the prebuilt Turtle start file.
2. **L7 wb Q1 15-gon off the stage (N3).** A LOW child who tests the 15-sided row at move 80 sees a kinked, clipped drawing and concludes the maths is wrong. Fix as in N3.
3. **L9 HIGH (3.50)** still meets revision for the first 35 minutes (`warm2`, `we1`, `we2`, ws1 Q1-Q3). Fix: open with the "misleading mean" puzzle ($22 mean vs $15 median) as the sneak-peek puzzle 2, and let the group choose Go further from minute 10.
4. **L1-L10 HIGH wait in teaching blocks (25-35).** The Think Harder invitation is now open, but the teach block is the same length. Fix: invite the whole group to "Start here, then choose" at minute 12 instead of 40.
5. **L2 / L4 / L10 LOW, slot overload.** L2 ws2 (about 35 answers), L4 ws2, and L10 relay (5-8, "name someone else" cold-call pattern if the tutor uses it) remain. Fix: halve the number of printed parts on ws2 pages, and make the relay volunteers-only.
6. **"you you" (N1)**: a tutor reading the reflection line aloud says "you you", which looks careless in the one routine meant to feel kind.
7. **Slide vs page mismatch (N1b)**: HIGH children pick Think Harder from the slide and find different questions on paper; LOW children who glance at the slide see items not in their workbook.
8. **No Scratch primer / no .sb3 files**: the L5, L8, L10 starters and the L7 start file depend on the tutor building them. A child who has not used Scratch before still meets nested operators, lists and Pen in a single lesson.

## 4. Ten-line summary
1. Audit-1 verdicts before: OK 1, minor fix 6, needs rework 3.
2. Audit-1 verdicts after: OK 5, minor fix 5, needs rework 0 (24 baseline findings: 13 fixed, 4 partly, 5 not fixed, 2 same).
3. No wrong answer found (263 Python checks; the 2 failures were bugs in my checks). One real L7 stage error remains: wb p1 Q1 15-gon at move 80 runs off stage (needs move 50).
4. Gifted mean before 16.8 (baseline projected 18.3), re-audit now 19.0; 4 lessons now in the 20-24 band, none under 12; no lesson dropped.
5. Journey LOW mean 2.78 -> 3.05 (+0.27).
6. Journey MIDDLE mean 3.87 -> 3.95 (+0.08).
7. Journey HIGH mean 4.05 -> 4.17 (+0.12); 22 of 30 cells up, 8 same, 0 down.
8. Not fixed despite the fix report: "you you" typo in every reflect note and the Tutor Guide (`p6/guide.js` about line 162).
9. New: the Think Harder slide differs from the printed page (L1 confirmed; check all lessons); L3 TH repeats Core; parent docs still say "strong thinkers".
10. Open: no .sb3 starters, L7 LOW (2.33) and L10 LOW (2.67) still weakest, L9 HIGH still revision-heavy.
