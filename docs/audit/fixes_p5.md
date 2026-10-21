# Fixes applied to the P5 program (from docs/audit/audit_p5.md)

Date: 2026-10-22. Edited the SOURCE only (p5/content/l1.js to l10.js, p5/workbook_html.js, p5/guide.js, p5/SPEC.md, rebuild/gen_p5l1.py to gen_p5l10.py). The slide HTML in split/p5lN was regenerated, not hand-edited. Nothing was committed or published. No shared files (rebuild/slidekit.py, rebuild/p5l*_common.py, hp/*, levels/*) were changed.

## Re-verification of changed numbers (Python, exact Fractions / brute force)
All pass: L1 digits 1 to 1000 = 2893 (and 1 to 1 000 000 = 5 888 896 unchanged); L2 1/7-1/8=1/56, 1/8-1/9=1/72, 1/10-1/11=1/110, 1/56+1/72=2/63=1/7-1/9; 3/5 x 1/2 + 1/10 = 2/5; 9/20 between 2/5 and 1/2; 7/8 of 24 = 21, 5/6 of 30 = 25; L3 bead box unique (70 at first, 100 now; blue 4 units, whole box 10 units); L5 cube in tank 40x30x6 - 10x10x6 = 6600 cm3; L6 cheapest >= 20 cans $13.64 (22 cans $14.92, 24 cans $15.60), exactly 20 cans: $13.64, $14.24, $14.60, 1330/190 = 7; L7 25% and 20%, shops $45 and $42 (25% off), glasses 6 + 8 = 14 = 35%, 21/60 = 35%; L10 logic grid has exactly one solution once Mei and Siti are girls (7 solutions without that). No existing answer changed.

## Per issue

| # | Status | What was done |
|---|---|---|
| 1 | Applied | New plan in all ten gen_p5lN.py (badges and "Minutes a to b" in notes, title "Time plan"): warm-up 0-9, explore 9-21, teaching 21-33, break 33-37, page 1 37-49, check 49-51, teach before page 2 51-57, page 2 57-72 (15 min), check 72-76, talk 76-82, exit 82-90 (L10 exit 82-88, certificates 88-90). Stretch/challenge slides are badged "For early finishers" and the plan says they are for early finishers or home. Teaching-region slides were re-sliced per lesson with no overlaps. |
| 2 | Applied | L2 teachpattern replaced with the verified 1/7-1/8 example (steps, check line 16/504 = 2/63, note no longer shows the worksheet terms). |
| 3 | Applied | L5 and L6 workbook now 2 pages each (all 10 lessons = 4 pages; total 47 pages, was 49). L5: smaller figQ4/figQ5/figQ6 with larger in-figure labels (box() gained an optional label size and svg() an optional viewBox, inside l5.js only), compact Q4(a to c), paint table rows 70. L6: figure Q3 placed beside the sub-parts, smaller shop board, rate table rows 38, Q2(a) one line. |
| 4 | Applied | L7: Q5 (percentage change) and Q7 (deals) removed from page 2 and made Think Harder Q1 and Q2 (qbank.stretch[0], [1], with the line "percentage change = the change out of the amount you START with"). Page 2 is now Q4 (remainder) and Q5 (class table, was Q6). Objective, key and ws2 text flag "preview of P6". workbook_html.js: Stretch banner "Q1: preview of P6, percentage change", Challenge banner "for strong thinkers: P6 preview" (L7 only). Core qbank item "$20 to $25 percentage increase" replaced by a P5 item. teachchange and teachdeal slides moved after ws2ans and badged "Think Harder". The five reverse-percentage bank items (challenge 1, 2, 4, 7, 9) stay in the Challenge list under the P6-preview banner. Two stretch bank items were dropped to keep 8 (up 10% twice, tank 35% full). |
| 5 | Applied | L2: objective says "(as a preview of P6)", teach1 note says it is a P6 skill, workbook Q1c/Q1d swapped so the division part is the last part of Q1 marked "(stretch)", key and ws1ans updated, core[5] is now 3/5 x 1/2 + 1/10. SPEC.md corrected (fraction division and ratio statements). |
| 6 | Applied | L3 Q5 gets the scaffold sub-part (before: red 3 units, blue ? units; after: blue is 2 of every 5; whole box ? units), sub-parts renumbered a to d, key and ws2ans updated; ratio notation in the ws2ans note replaced with "3 parts out of 5". |
| 7 | Applied | L6 Q2(c) now "exactly 20 cans, find one way" (key lists $13.64, $14.24, $14.60). The "at least 20 cans" version with the 22/24-can explanation is in the challenge bank (replaced the Ken and Dan fence item). ws1ans slide note updated. |
| 8 | Applied | L6 teach1 step 3 "1330 cents / 190 cents = 7 kg" and note; think script updated. |
| 9 | Applied | L6 lesson.share, script.talk, talkAns and the talk slide now use "Is the biggest pack always the best buy?"; the two-tap puzzle moved to the challenge slide as item 3 (answer in its notes). |
| 10 | Applied | L8: printed Reasons strip A to F at the top of page 2; Q3 stem asks for a reason only for (b) and (d); (a) and (c) lines are answers only; slide preview and ws2 note updated. |
| 11 | Applied | L5 Q1(b) new wording; teachlist has its own 2-minute slot (30-32, key 32-33); challenge[2] (two tanks) replaced with the cube-in-tank item (6600 cm3), including the challenge, chdiag (new SVG) and chwalk slides. |
| 12 | Partly applied | Added the line "Draw a big, neat diagram first and label every length or angle you know." to the Think Harder header of every lesson (workbook_html.js). The eight figure-dependent items were NOT given printed figures: the figure code is private to each content file or to Python slide builders, so reusing it needs a shared refactor. |
| 13 | Applied | L10 Q2 clue 2 names the girls and boys; key text expanded; uniqueness verified. |
| 14 | Applied | L10 challenge note now says the chairs puzzle is Think Harder Q7 and the rambutan puzzle is bank only; materials say four puzzle cards on the slide or sent as images. |
| 15 | Applied | L1 Q2 stem "A 7-digit number cannot start with 0"; challenge 3 is now 1 to 1000 (2893) with the 1 000 000 version as "go further". Q2(b) was not moved (the audit says only if time is short; page 1 now has 12 min). |
| 16 | Applied | L2 stretch slide now: 5/6 vs 6/7, fraction between 2/5 and 1/2 over 20, 7/8 of 24 vs 5/6 of 30 (qbank stretch[6], [7] changed to match). |
| 17 | Applied | L2 ws2ans note and L9 chwalk note rewritten in words. The L9 chwalk child-facing line "figure n ... (2 x n - 1)" now uses figure 6. |
| 18 | Applied (printed word) | L10 "consecutive" glossed with "like 40 and 41". "palindrome" is bank-only and already defined in its question. |
| 19 | Applied | guide.js parent summary has the Lesson 5 (24 to 36 cubes or squared paper) and Lesson 9 (20 matchsticks) bullet and "print the workbook before the lesson"; L9 materials say about 20 per child. |
| 20 | Applied | Overlapping slide times removed as part of issue 1. |
| Lesson-level online notes (L3, L4 camera) | Applied | L3 and L4 lesson.online and explore1 notes: camera up, hold work to the camera, or use the interactive slide. |

Cross-cutting items A to E (tutor-guide rules for whiteboards, breakouts, second device, parent letter) were not applied beyond issue 19: they are guidance text in P5_Holiday_Program_Guide.docx and were not in the High/Medium list.

## Regenerated deck keys
All ten: p5l1, p5l2, p5l3, p5l4, p5l5, p5l6, p5l7, p5l8, p5l9, p5l10 (python3 rebuild/gen_p5lN.py, then python3 levels/restyle.py split/p5lN on each). Slide counts: 26, 25, 24, 25, 25, 25, 26, 26, 26, 27. Preview check: no overflow except p5l1-explore1 and p5l4-explore1 (1087 and 1081 px), which also overflow on the unmodified source after restyle (restyle decoration, not caused by these edits).

## Build
bash levels/build_level.sh 5 ran cleanly. Workbook page count: 47 (was 49); every lesson is 2 worksheet pages + 2 Think Harder pages. Tutor guide 68 pages, weekly dose 25 pages.
