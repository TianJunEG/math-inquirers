# P4 fix pass: what changed

Brief: `docs/audit/fixpass_brief_p4.txt`, plus the P4 review's kit items and the safeguarding correction (no private one-to-one messages anywhere). Nothing was committed. Every changed answer is re-computed in `docs/audit/verify_fixpass_p4.py` (75 checks, all pass).

## Safeguarding correction (applied everywhere)
- No private chat or DM from tutor to child in the workbook, slides, notes, script or guide. The guide keeps "No private messages to children".
- Invitations go to the WHOLE group: "when you have finished Start here you can choose Think harder, Go further or the Investigation". Nobody is named or announced; pairs are not split unless both children agree; if a pair loses a member the other child joins another pair or the tutor at once.
- Sneak-peek answers: own paper, held to the camera at the same moment for everyone (or shown only to the tutor on camera). Never boards in front of the group, never private chat.
- "I am still stuck" gets a check-in in the open session (quick visit to the shared breakout room or a hand signal, parent nearby). The printed wording is "(my tutor will check in with me)" (the brief's "privately" was dropped).
- The reflection box may be looked at only if the child holds it to the camera. It is never collected or shown.

## Changes common to all ten lessons
1. Labels: Core = "Start here", Think Harder = "Think harder", Challenge = "Go further", open task = "Investigation". The printed fast-track criterion and every "strong thinkers / early finishers / genius / gifted" label are gone from workbook, slides and guide (guide disclaimer now says "builds problem-solving and thinking skills"). Page 1 carries "After question 3 you may choose: carry on, or try Think harder."
2. Warm-up check is now "Sneak-peek puzzles" (1 to 4 min): an access question (objects, drawing or counting) then a thinking question; slide and notes say these are ideas not yet learnt, guessing and "I do not know" are welcome, nobody is marked. L7 has a picture.
3. Reflection: "Looking back" box (Something I did well / The hardest part was / What helped me; ticks include "I asked for help", "I am still stuck (my tutor will check in with me)", "I pass today") on page 3 (the Investigation page every child reaches). 2 minutes, 88 to 90 (L10: 87 to 89, exit 85 to 87, certificates 89 to 90). No "you you" typos exist in P4; the real duplicate found was "IF STUCK  Stuck: ..." in the guide, fixed.
4. Talk time: volunteers first, passing always fine, no cold-calling, no tallies (slide rules, notes, guide).
5. Investigation printed as an option on page 3 with an "Easy first step" and the model answer kept (L9 replaced by "Sales have doubled!", honest scale).
6. Go further: one second what-if on every explore slide (L1 36 tiles, L2 closest to 70 000, L3 two pairs of brackets, L4 8-slice pizzas, L5 target 50, L6 3:30 is 75 degrees, L7 24 tiles, L8 longest row 3, L9 other scale, L10 impossible 65 legs). LOW support: solo page 2 has a printed cap ("Page 2 is on your own. Aim for Q... first...") and trimmed items.
7. Timeline now consistent in deck, notes, script, guide, workbook: opening 0-1, sneak peek 1-4, game 4-6, quick 6-8, explore 8-18, mini-lesson 18-30, break 30-34, page 1 34-50 (L6: teaching 34-36, page 36-50), check 50-53, teach 53-58, page 2 58-76, check 76-80, talk 80-85, exit 85-88, reflect 88-90. Minute labels added to every slide that lacked one (title 0-1; Go further / Think harder slides "Any time").

## Per lesson (level-specific defects)
- L1: Q6a step scaffold; Fizz-Buzz slip rule is "my go again" (no one out).
- L2: Q1 table cut to 47 285 and 63 950, "Try next" (9049, 80 503); Q2a "Start here" hint; Q4a hint; digit cards supplied.
- L3: Target Numbers has no race or points; quick questions 48 / 6, 9 x 6, 4 x 20 (originals as "Try next"); Q6 now 124 plates (31, 93, 62; old 1 236 version kept in the bank); teach-before-page-2 capped at two methods: machine (53-55) and bar model (55-58); number trick and chain slides are "OPTIONAL, only if time". The review said "bar model and bracket order", but there is no bracket slide in that block, so the machine slide stands in.
- L4: drawn bars for 4/9 v 5/8; Q4 asks for a reason in (c) only; Mei framed as a made-up character in the talk slide.
- L5: warm-up closes with "0.8 is the same as 0.80. 0.80 is bigger than 0.75."; Q3 keeps part (a) only, with a number line (the rest is in the bank); Q4 cut to 6 numbers (point after the first digit); Q6 bar scaffold. The review described a 12-number Q4 and 2.40 / 6; the current workbook differed, so the intent was applied.
- L6: protractor tip; mirrored self-view note; paper clock, protractor, ruler on the kit page.
- L7: Q2b moved to the bank; Q3 b and c merged; Q4a frame scaffold; "layers" replaced by "rows".
- L8, L9, L10: materials and online lines updated; L9 "Not sure? Try 2 per line"; L10 pairs choose 3 of the 4 puzzle cards.

## Kit (printed pages added to `p4/kit.js`, new `p4/kit_extra.js`)
Digit 0-9 x2, 4 decimal points, signs x2, 2 pairs of brackets; two blank graph grids with scale boxes; paper clock with hands, three pizza circles, and a "Bring from home" box (180 degree protractor, 30 cm ruler, pencils, scissors, tape). +3 pages.

## Page counts
| Item | Before | After |
|---|---|---|
| Student workbook | 57 | 64 (+3 kit pages, +4 spill pages) |
| Tutor guide | 79 | 83 |
| Weekly dose | 25 | 25 |
| Slides per lesson | 28 29 28 30 29 28 29 28 27 29 | unchanged |
Workbook pages per lesson: 5 before; after L1 6, L2 6, L3 5, L4 5, L5 5, L6 6, L7 5, L8 5, L9 5, L10 5. Rule met (at most +1); L1, L2 and L6 are +1 because one question block no longer fits on its page (Q6, Q3 and Q2 respectively).
Overflow check: all 285 slides measured, none below y 920 and none wider than the page.

## Diagnostic (`diag/content/p4.json` only)
Done in the JSON: warm-up reordered (9 x 7, 2/3 = ?/12, area, 5000 - 1346 last); Q1 defines "factor"; stretch reassurance prefixed to Brain stretcher 1 (a workaround, see build change 3); W4 key accepts 42 square cm, 42 sq cm or 42 cm2 and gives the mark if the unit is missing; Q4 key says mixed number preferred, 22/5 accepted; Q5 error now "3.22 or 5.92"; minutes 40; topics list states it samples number, fractions, decimals, area and perimeter only (angles, symmetry, nets, graphs not in it); new `placement` block with the exact wording for the build to read. All answers verified in Python.

Needed in `diag/build_diag.py` (not edited; shared by all levels):
1. Replace the hard-coded rows at lines 53-55 with `d["placement"]["rows"]` (fill `{AGE}`, `{LV}`, `{down}`); keep the "try up" sentence for 6 to 8.
2. Heading "Skills covered" (line 57) to `d["placement"]["skillsHeading"]`; the "Not yet?" box to `lowerMarkBox`; remove "Not yet" and "failure" anywhere.
3. Print `stretchNote` above "Brain stretchers" as its own line, then delete the prefix from stretch[0].q. (Needed because the workaround text also shows in the tutor key.)
4. Add a "This has not been taught yet" tick box beside every main question (`notTaughtTick`) and the rule `notTaughtRule` on the key page.
5. Put `keyNote` ("Please do not mark in front of your child.") at the top of the tutor key page, and print the tutor key as a separate page set from the parent result page.
6. Replace "About N minutes" on page 1 with `timeLine`; add the grey-zone chat line (`greyZone`) and swap rule (`swapRule`) to the result page.
7. Line 56 "Strong? ... will enjoy the challenge questions in class" should be reworded (it implies labelling); line 8 mixes age wording ("Open to a year either side") with the level age; use one wording.
8. Optional: a 4-question try-up set (`tryUp`) from next year; reconcile `docs/levels_and_placement.md` with the raw-mark bands.

## Not edited (shared files), for the coordinator
- `levels/mkextras.py`: LV[4]['kit'] needs three new entries: Digit/point/sign/bracket cards [2,3,5,10], Graph grids [9], Paper clock, pizza circles and what to bring [4,6].
- `levels/mkextras.py` marketing text still uses "Think Harder / Challenge for strong thinkers / Challenge Group for children who show the signs", and the Question Bank intro says "move up when they are ready" (generated PDFs in `outputs/designed/`). Same rule should apply there.
- L5 Fix E (splitting L5 into two lessons) is a longer-term note only.
