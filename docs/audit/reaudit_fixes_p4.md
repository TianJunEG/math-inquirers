# Level 4 fix pass after the re-audit (docs/audit/reaudit_p4.md)

Scope: content and wording defects that were low risk. Nothing committed. Shared files (diag/*, levels/*.py, levels/*.js, rebuild/slidekit.py, hp/*, website/*, docs/levels_and_placement.md) were not edited. Every new or changed numeric answer was checked in Python (exact arithmetic or brute force over all cases): L2 S7 (37 500 to 38 499), L2 S8 (94 875, the largest of 1470 candidates), L3 S5 (20 and the wrong 2900), L3 X2 (122, 178, gift 28; with $400: 172, 228, gift 28), L4 S7 (19 quarters, 14 left, 3 1/2), L8 X5 (only 6, 2, 4 has one face from each opposite pair with sum 12), L9 S2 (175, 275), L9 S3 (40, 55, 70, 55, 40), L9 S7 (15, 25, 25, 45), L10 S4 (unique over all 24 orders), L10 S5 (21), L10 S7 (27 x 29 only), L10 X7 (8 tables; 60 to 90 seats; every even total is reachable and 77 is odd).

## 1. Looking back: "what I would try next" restored

| Where | Old | New |
|---|---|---|
| Printed page 3 (p4/workbook_html.js `reflectBox`) | Something I did well / The hardest part was / What helped me (ticks) / still stuck / pass today | Same, plus a row "One thing I could try next": drawing it, a list or table, a smaller number, a partner, another question like this, other, and a tick "I pass on this one". Neutral, optional. Each tick option is kept with its box so it does not wrap apart. |
| Slide "Looking back" (rebuild/p4_fix.py `reflect_slide`) | One column of boxes | Two-by-two layout with the same new "One thing I could try next" box and one combined "still stuck / pass" line. Checked at 1920 by 1080. |
| Model sentence in every lesson (`gaps.reflect`, used by the tutor guide and the slide notes) | Three sentences | A fourth, lesson-specific: "One thing I could try next: ..." (10 lessons). |
| Tutor guide (p4/guide.js, two lines) | Listed three prompts | Lists four prompts and says "tick a choice, write your own, or pass". |

Duplicated stretch reassurance: the re-audit found it on the DIAGNOSTIC child sheet (Q11 prefix and the printed tip) and in the diagnostic tutor key. That is in diag/*, which I was told not to edit. See "For the lead". In the Level 4 workbook, slides and guide the reassurance appears once.

## 2. Start-here pages: a low-floor entry for all 18 flagged questions

A small yellow "Start here." tip (new file p4/tip.js, 13 px, kept inside the question box) or, in L4 Q6, a drawn strip. Answers and keys are unchanged. Page counts held by tightening sub-question spacing, shortening tips to one line and shrinking some figures (see section 6).

| Q | Entry added |
|---|---|
| L1 Q5 | Use 6 counters: 1 row of 6, 2 rows of 3 ... each different number of rows is a factor; then 9 counters. Tip on pairs for (b) |
| L1 Q6 | (b) Write the first six multiples of 3 and of 6 on two lines and compare |
| L2 Q2 | (b) 5345 is halfway between 5340 and 5350: does it round up or down? (a) already had one |
| L2 Q4 | (b) The digits are two 1s or one 2, the first digit is not 0; write 20 000 and 10 001 first |
| L3 Q1 | Draw the 5 packs of 14 stickers, then add the 36. Sub-lines tightened |
| L3 Q3 | Try brackets round 4 + 8, then 5 − 3, then 8 × 5 − 3 and write each answer |
| L4 Q4 | Fold a strip into quarters, then each quarter in half: 3 quarters = ___ eighths |
| L4 Q5 | Put 27 counters into 3 equal groups: how many in each group? |
| L4 Q6 | A printed strip of 12 numbered boxes to shade (1/3, then 3/4); the old "draw a strip" hint became "Start here: on the strip, shade ..." |
| L5 Q2 | Write each number with 3 decimal places (3.5 is 3.500) and compare tenths first |
| L5 Q3 | 7.45 is halfway between 7.4 and 7.5: which marks on the line round to 7.4? |
| L6 Q1 | Hold the corner of a sheet of paper on each angle: smaller or bigger than a right angle? Use that for the estimate. The protractor now comes after the estimate |
| L7 Q4 | Walk a finger along the edge of the staircase: how far across, how far down? |
| L7 Q6 | Draw the 8 by 6 photo and its 1 cm frame on squared paper and count the frame squares |
| L8 Q6 | Fold the page on the dashed line: where does each shaded square land? Is that square shaded? |
| L9 Q3 | Read each dot and write Ali's and Mei's money for weeks 1 to 6 in the blanks, then use them for (a) to (c) |
| L9 Q5 | Read the scale of each graph: where it starts and what each line is worth |
| L10 Q6 | A worked first try: Ben 6, father 44; in 5 years 11 and 49; 49 is not 3 times 11; try again |

## 3. Items outside their tier (10 bank items, 5 slide items, plus 3 bank Challenge items)

Bank Think harder (S = position in the bank; S1 to S4 are the printed page):

| Item | Old (problem) | New |
|---|---|---|
| L2 S7 | Smallest and largest difference of two rounded crowds (Challenge level) | A concert crowd was 38 000 to the nearest thousand: smallest and largest it could be (37 500, 38 499) |
| L2 S8 | Largest 5-digit odd number with different digits (place value only) | Same, but it must also round to 90 000 to the nearest ten thousand (94 875) |
| L3 S5 | 120 − 4 x (18 + 7): one step of the method | Ali got 2900. Which step was in the wrong order? What is the right answer (20)? |
| L4 S7 | Quarters in 4 3/4: one conversion | A 4 3/4 m ribbon cut into 1/4 m pieces, 5 used for a bow: how much is left as a mixed number (3 1/2 m) |
| L9 S2 (printed) | Scale of 20, 3 lines above 40 | Scale starts at 100, lines worth 25, Ali 3 lines up, Mei 7 lines up: how much more, and is Mei's number more than double (100 more; no) |
| L9 S3 (printed) | 300 kites in 4 days, find Day 3 | Graph starts at 40 on Monday, up 15 a day to Wednesday then down 15: Friday and the day matching Thursday (40; Tuesday) |
| L9 S7 | Biggest change between four days (repeats the exit ticket) | A scale starting at 0 with lines worth 5, points 3, 5, 5, 9 lines up: biggest rise and the week it stayed the same (week 4, up 20; week 3) |
| L10 S4 (printed) | Three ages in order | Four ages 8 to 11 with three clues, one answer (Ali 11, Ben 10, Siti 9, Mei 8) |
| L10 S5 | Queue, one front and one back position | Ali 8th from the front, Ben 6th from the back, 7 children between them (21) |
| L10 S7 | Three next-door numbers add to 117 | Two next-door odd numbers multiply to 783 (27 and 29) |

Bank Challenge:

| Item | Old | New |
|---|---|---|
| L3 X2 | $56 more, total $300: one-step bar model | Adds (b) how much Ali gives so they are equal ($28) and (c) what if the total were $400: does it change? (justify: half the gap) |
| L8 X5 | Side faces of a dice add to 14 (recall of 7 + 7) | Keeps the justification and adds: seen from a corner, three faces add to 12, which numbers? Only one answer (6, 2, 4) |
| L10 X7 | The taught "suppose" method in one step (same as Go further Q5) | Adds (b) fewest and most seats (60, 90) and (c) could there be 77 seats (no: every total is even). The slide copy was updated to match |

Also L4 S6 reworded: "How many pieces can she cut? (Count the quarters in each metre.)" (MOE note: division by a fraction is later).

Slide Think harder items: all five (L2 item 2, L3 item 1, L4 item 1, L9 items 1 and 2) were replaced by the item 4 fix below.

## 4. Slide Think harder = printed page; Go further notes

- New helper rebuild/p4bank.py reads the first four `qbank.stretch` items from p4/content/l*.js (exactly what p4/workbook_html.js prints) and the slide notes now carry those four answers. Each gen_p4l*.py uses it, so slide and page cannot drift apart again. The slide shows four cards in a 2 by 2 grid (it showed three single cards before).
- Slide titles now say "Think harder", "Go further", "Go further: see it", "Go further: walk-through" (they said Stretch and Challenge).
- Seven Go further notes (L1, L2, L3, L4, L7, L9, L10) said "These are Think Harder Q..."; they now say "These are Go further Q..." with the numbers checked against the printed page: L1 Q7 and Q6, L2 Q5 and Q7, L3 Q5 and Q6, L4 Q6 and Q7, L7 Q6 and Q7, L9 Q5 and Q6, L10 Q5 and Q6. The L5, L6 and L8 Challenge slides never claimed a number (they show bank items) and were left alone.

## 5. Lesson 6 protractor

The materials and online text already said "bring from home" and the kit page listed it, but the first question was still a protractor measurement. Now:
- p4/content/l6.js `materials`: a clear 180 degree protractor and 30 cm ruler for each child, not printed in the kit, bring from home, listed on the kit page, tutor keeps 2 or 3 spares. `online`: children check they have one before the lesson and tell the tutor if not.
- p4/kit_extra.js "Bring from home" box: line 1 says Lesson 6 starts with them; a new line says to tell the tutor before Lesson 6 (spares, or share with a partner). Box lines re-spaced.
- rebuild/gen_p4l6.py Materials note updated. L6 Q1 now begins with a paper-corner estimate (section 2), so a child without a protractor can still start.
- Not done: a cut-out protractor. It would need a new kit page (+1 workbook page) or a crowded page; say if you want it.

## 6. MOE wording (Level 4 text only)

L3 Think harder 7 now reads "Use each of 2, 3, 4 and 5 once in [box] + [box] x [box] - [box] ... (one number in each box, in any order)"; L3 Challenge 4 "The same number goes in all three boxes: [box] x [box] - [box] = 30"; L5 Think harder 1 "Find ALL the digits that can go in the box: 3.[box]5 < 3.42". Answers unchanged. The box is the Unicode square, which renders in the question bank PDF (checked).

Not changed, for the lead to decide: the 8-point compass and turns in Lesson 6 (objective, C3, C4, T1, T4, T5, T7, CH3, CH6, workbook Q4 and Q6); no pie charts in L8 or L9; L4 CH2, CH5, CH6, CH7 add unrelated fractions (1/3 and 1/4, 1/2 and 1/3) which MOE may place at P5 (a bar model solves each).

## 7. Final page counts (re-measured from the built PDFs)

| File | Before this pass (HEAD) | Now |
|---|---|---|
| Student workbook | 64 | 64 (lessons 1 to 10 take 6, 6, 5, 5, 5, 6, 5, 5, 5, 5 pages, the same split as before) |
| Tutor guide | 99 | 99 (a longer guide line spilled one page; shortened) |
| Weekly dose | 25 | 25 |
| Question bank / email pack / free taster / what learners get | 28 / 12 / 5 / 1 | 28 / 12 / 5 / 1 (self-check OK) |
| Decks | 285 slides (28, 28, 29, 30, 29, 28, 29, 28, 27, 29) | same |

To keep the workbook at 64 I tightened sub-question spacing (L3 Q1, L5 Q2), put the scaffold tips on one line, moved two tips out of the narrow side column (L7), removed one answer line and shrank the L8 Q6 grids a little, narrowed the two L9 line graphs from 600 to 500 px, and used one blank row instead of a table for L9 Q3. L1, L2 and L6 already ran to a third core page before this pass and still do.

## 8. What I could not fix, and why

- Duplicate stretch reassurance and the diagnostic items: in diag/* (not mine).
- "Challenge Group for children who show the signs" and "moves up when they are ready" in What Learners Get and the Question Bank intro: printed by levels/mkextras.py (shared). Rebuilt output still has them.
- A cut-out protractor (see section 5).
- Journey, pacing, compacting and depth-over-speed items: out of scope (timing audit running).
- The tutor guide cannot grow by a page; the extra Looking-back and spare-protractor lines were kept to one short phrase each.

## For the lead

1. levels/mkextras.py still prints "Challenge Group for children who show the signs" in What Learners Get and "Every child starts with Core, then moves up when they are ready" in the Question Bank intro.
2. The duplicated reassurance (Q11 prefix and printed tip, and the tutor key) is in diag/*.
3. levels/mklevel.py line for P4 says "Children need their own protractor for Lesson 6": consistent with the new text, no change needed.
4. Decisions pending: 8-point compass, pie charts, unlike-denominator fraction puzzles (section 6).
