# Audit: Math Inquirers P1 holiday program (ages 7-8, finishing Primary 1)

Scope: suitability and difficulty of 10 lessons x 90 min, online, groups of 8.
Files read: `hp/lessons.js`, `hp/qbank.json` (+ `hp/qbank.py` generator), `hp/workbook.js` (and the images it uses), `hp/scripts.js`, all 10 decks in `split/l1..l10/project/slides` (every slide, including speaker notes). `rebuild/gen_l1..10.py` generate those slides; the issues below are fixed in the generator for each lesson (the slide HTML is generated output).
No content files were edited.

Syllabus reference (MOE Primary 1, 2021 syllabus as summarised in school P1 handbooks):
- Whole numbers to 100, ordinal numbers, number sequences/patterns.
- Add/subtract within 100 (mental within 20); multiplication within 40; division within 20.
- Money: cents up to $1, dollars up to $100.
- Length: cm only (measure, compare, order, to nearest cm).
- Time: to 5 minutes.
- 2D shapes: rectangle, square, triangle, circle, half and quarter circle; form figures and identify basic shapes in a figure.
- Picture graphs: reading and interpreting.
- Sources: https://shuqunpri.moe.edu.sg/files/P1_Math_Handbook_2025.pdf and https://www.admiraltypri.moe.edu.sg/files/Level%20Matters/Content/MATH_CONTENT__P1_to_P3_.pdf

How the workbook is built (matters for the findings): main worksheet = Q1..Qn; "THINK HARDER" = first 4 items of `qbank[n].stretch`; "Challenge" = last 3 items of `qbank[n].challenge`, numbered Q5-Q7 (`extra()` in `hp/workbook.js`). `qbank.core` is not printed in the workbook (question bank / tutor use only).

## Method for answers

Every numeric answer in `lessons.js` keys, every `qbank.json` item (about 190 items) and every slide answer was recomputed by hand and with Python brute force (coin combinations, orderings, sequences, grid counts, logic puzzles). Result: **no wrong numeric answer was found.** All issues below are about difficulty, ambiguity, alignment, timing and wording.

## 1. Summary table

| Lesson | Verdict | One-line reason |
|---|---|---|
| L1 Count with the Frog | minor fix | Sound and age-right. Challenge items are CRT-style (two offset sequences); one ambiguous Challenge item; odd/even used without being taught until a late slide. |
| L2 Number Bond Inquiry | minor fix | Strong lesson. Worksheet page 2 has only 6 minutes for 3 hard items (two magic triangles, sum-and-difference). |
| L3 Let's Plan the Fruit Party | minor fix | Good. Keys of 2/3/4 and building graphs are beyond P1 (reading only); Challenge Q8 needs 40 divided by 4 and "twice as many" (P3 language). |
| L4 Pattern Inquiry | OK | Well paced, answers right, core idea scaffolded. Only wording nits and a safety note (matchsticks). |
| L5 Mystery Number | minor fix | Good. Challenge age puzzle is P4 level; Think Harder is four copies of one type; page 2 is tight. |
| L6 Coin Combos | needs rework | 7 minutes for 5 hard worksheet questions; three Think Harder items repeat in-class examples; several main items are Challenge level but unlabelled. |
| L7 Shape Safari | needs rework | Overloaded; 10 minutes of mini-lesson (counting squares/rectangles/tetromino shapes) is never practised on the worksheet; Think Harder is easier than the main worksheet; shape names beyond syllabus. |
| L8 Logic Lab | minor fix | Content right and well taught. Reading load highest of the course; stale tutor note; odd/even and Venn terms need a one-line reminder. |
| L9 Measure It! | minor fix (one big gap) | cm ruler is taught and is the exit ticket, but no workbook or question-bank item practises it (the one skill P1 actually assesses). Think Harder repeats the main worksheet. |
| L10 Challenge Day | needs rework | Explore asks for 4 stations x 8 min = 32 min in a 15-minute slot, and the four puzzle cards do not exist as files. Page 2 has 8 minutes for 5 items including inventing a puzzle. |

## 2. Programme-wide findings

- **P-1 Schedule double-booking (all lessons except L5).** Every `l*-challenge` and `l*-chdiag` slide is labelled "65-80 MIN", but Talk time is 70-80 and check-together runs to 68-70. The Stretch slide has no time. The workbook then prints 4 Think Harder + 3 Challenge items. In practice that is 0-5 minutes of extra-item time for a child who finishes page 2 at about 66.
- **P-2 One break in 90 online minutes.** Only a 5-minute break at 35-40. For 7-8 year olds on a screen, minutes 40-90 are 50 minutes of continuous seated work with no movement break.
- **P-3 Writing/reading load.** Many items end in "How do you know?" with 2-3 writing lines. Seven-year-olds write slowly (and have to hold paper up to a camera). Reading is heaviest in L5 Q4, L8 Q1c, L9 Q5, L6 Q3-Q7, L10 Q3-Q8.
- **P-4 Numbering clash.** Think Harder is Q1-Q4 and Challenge is Q5-Q7, so "Q5" means two things in lessons with 5+ main questions (L5, L6, L7, L8, L9, L10). Tutors saying "do Q5" is ambiguous.
- **P-5 Slide Stretch/Challenge differ from workbook items.** Slides show 3 Stretch items that are not in the workbook; answers are only in speaker notes. Children and tutor are looking at different "stretch".
- **P-6 Coverage note.** The program never touches time, multiplication/division, or 2-digit addition/subtraction within 100. That is fine for enrichment but parents may expect it ("finishing P1"); say so on the sign-up page.

## 3. Issues, ranked by severity

### HIGH

**1. L10 explore: impossible timing and missing materials.**
Files: `hp/lessons.js` (L10 `explore`, `materials`), `rebuild/gen_l10.py` (`l10-explore1`), `deck/gen.js` line 72, `hp/scripts.js` L10 `think`.
Problem: "Four stations, eight minutes at each" = 32 min, but the slot is 10-25 (15 min). Online, "one puzzle per breakout pair" contradicts rotation. The "puzzle cards for 4 stations" are listed under materials but no file contains them (only 3 sample puzzles in the tutor script).
Fix: replace the explore text with: "Four puzzle cards (coins, patterns, logic, measuring). Pairs get ONE card for 10 minutes, then swap cards with another pair for a second 4-minute round. Online: one card per breakout room; each pair reports in 30 seconds." Produce the 4 cards. Suggested card puzzles, all verified: Coins "Make 45c with exactly 3 coins from 5c, 10c, 20c, 50c" (20+20+5). Patterns "5, 8, 11, 14 ... what is the 10th number?" (32). Logic "Mei is taller than Ben, Ben taller than Sam, Ali shorter than Sam. Order them" (Mei, Ben, Sam, Ali). Measuring "A pencil is 6 cubes. A pen is 4 cubes longer. Put them end to end: how many cubes?" (16). Change `lessons.js` L10 `materials` accordingly.

**2. L9: cm ruler taught and assessed, but never practised.**
Files: `hp/workbook.js` (L9 section), `hp/qbank.json` L9, `hp/lessons.js` L9 `mini`, `exit`; slides `l9-teachcm`, `l9-we2`, `l9-try2`, exit ticket.
Problem: Objective, mini-lesson, three slides and the exit ticket cover centimetres (P1 syllabus: "cm only"), but workbook Q1-Q6 and all 18 qbank items use cubes/clips/erasers only. Online lessons also do not list a ruler under `online`.
Fix: (a) Replace workbook L9 Q6 ("Challenge! Find something at home that is exactly 10 cubes long") with a cm question, exact text: "Q6. Use your ruler. (a) A pencil lies from the 0 cm mark to the 12 cm mark. How long is it? ____ cm  (b) A crayon lies from the 3 cm mark to the 8 cm mark. How long is it? ____ cm  (c) Measure your own pencil with your ruler. ____ cm. Is it longer or shorter than 10 cm?" Answers: 12 cm, 5 cm, open. (b) Add to `qbank.json` L9 core: "A ribbon lies from the 2 cm mark to the 7 cm mark on a ruler. How long is it?" -> "5 cm (count the spaces: 7 - 2)". (c) `lessons.js` L9 `online`: add "Each child needs a cm ruler (or print the ruler strip)."

**3. L6: worksheet page 2 is not completable in the time; difficulty not differentiated.**
Files: `hp/workbook.js` L6 Q3-Q7; slides `l6-ws2` (60-67 MIN), `l6-teach*`.
Problem: Q3 (two parts), Q4 (all 4-coin sets worth 70c, 2 solutions among 24 combinations), Q5, Q6 (two unknowns, 90c with 6 coins), Q7 (three parts, dollars) in 7 minutes, after 6 min of teaching, with play money cut-outs. Q4 and Q6 are Challenge-level but unlabelled; there are three such items before "Think Harder".
Fix: Keep Q3, Q5, Q7 as the main page. Move Q4 and Q6 to Think Harder (replacing stretch[1] and stretch[2], see Issue 4). Extend `l6-ws2` to 60-68 and drop `l6-teachexact` or `l6-teachswap` from the pre-teaching, or move one of them to the Challenge slides.

**4. L6: Think Harder repeats work already done in class.**
File: `hp/workbook.js` `extra(6)` uses `qbank[6].stretch[0..3]`.
Problem: stretch[0] "ways to make 25c" is the worked example on `l6-we1`; stretch[1] "ways to make 30c" is main worksheet Q2; stretch[2] "20c with 10c and 5c" is `l6-try1` b. Only stretch[3] ($34 change from $50) is new.
Fix: reorder `qbank.json` L6 stretch so the first four are: (1) "A bag costs $34. Ali pays with a $50 note. How much change does he get?" (existing), (2) "Make 70c using exactly 4 coins from 5c, 10c, 20c and 50c. Find every set." (50+10+5+5; 20+20+20+10; currently main Q4), (3) "Sam has only 10c and 20c coins. He pays exactly 90c using 6 coins. How many of each?" (3 and 3; currently main Q6), (4) "What is the fewest number of coins to make 45c from 5c, 10c, 20c and 50c?" (3: 20+20+5).

**5. L7: mini-lesson content is not on the worksheet; overloaded lesson.**
Files: `hp/lessons.js` L7 `mini`; `rebuild/gen_l7.py`; slides `l7-teach1`, `l7-we1`, `l7-try1`, `l7-we2`, `l7-try2`, `l7-we3` (25-35 min) vs workbook Q1-Q5.
Problem: Slides 25-35 teach counting squares in grids, rectangles in strips and 3-square shapes. The worksheet (Q1-Q5) only asks: shapes in a house, sides/corners table, "Who am I?", triangles in 3 pictures, two triangles joined. The grid/strip skills first reappear in the exit ticket (a 4 x 2 grid) and in Challenge. The lesson also has 9 separate teaching episodes plus a 3-question stretch slide. This is too much for 90 minutes with 7-year-olds.
Fix: Keep squares-in-a-grid (`l7-teach1`, `l7-we1`, `l7-try1`) as the key idea since it is the "count by size" idea behind Q4. Cut `l7-we2`/`l7-try2` (rectangles in strips) and `l7-we3` (3-square shapes) and move them to the Challenge/stretch tier. Add one worksheet item to practise the kept idea, exact text: "Q6. How many squares can you find in this picture? Count the small ones first, then the bigger one. (A 2 x 2 grid.) ____ squares" (answer 5).

**6. L7: Think Harder is easier than the main worksheet.**
File: `hp/workbook.js` `extra(7)` uses `qbank[7].stretch[0..3]`.
Problem: stretch[0] "4 sides, all the same length" repeats Q3a; stretch[3] "7 corners, how many sides" repeats Q2b; stretch[1] and [2] are simple multiplication-by-counting (3 triangles = 9 sides; 5 squares = 20 corners).
Fix: reorder `qbank.json` L7 stretch so the first four are: "Fold a square along a diagonal and cut. Which shapes do you get?" (existing stretch[4]); "Two same-size triangles can make a square. Can they also make a bigger triangle? Draw how." (existing [5]); the slide items "How many squares are in a grid 3 squares long and 2 squares high?" (8) and "Join 4 same-size squares, whole sides touching. How many different shapes? (Turns and flips are the same.)" (5). Add both slide items to `qbank.json` (they currently exist only in speaker notes).

**7. L7: shape names and terms beyond the P1 syllabus; mixed message on "rectangle".**
Files: `hp/workbook.js` L7 Q2 (pentagon, hexagon, octagon), Q3c; `qbank.json` L7 core 3-5, stretch 7, challenge 6; slide notes `l7-explore2`, `l7-ws2ans`.
Problem: P1 lists rectangle, square, triangle, circle, half and quarter circle. Pentagon, hexagon, octagon and parallelogram/rhombus are later. Core items 3-5 ("How many sides and corners does a pentagon/hexagon/octagon have?") are vocabulary recall, not reasoning, so they are not Core for a child who missed the Q2 table. Separately, `l7-we2` says "a square counts as a rectangle" while the worksheet and key idea say a square goes only in the Square column.
Fix: (a) Rephrase core 3-5 to give the picture or name in the question: "Here is a hexagon (a shape with 6 straight sides). How many corners does it have?" (6). (b) Replace stretch 7 (ambiguous, see Issue 11) with "Draw a shape with 4 straight sides that is NOT a square. Is it a rectangle?" (open). (c) In `l7-we2` change the spoken line to "In this puzzle only, count squares as rectangles too" (already hinted at; make it a printed line on the slide) and on `l7-key` add "On the house picture, a square goes in the Square column only."

**8. L2/L5/L6/L9/L10: worksheet page 2 windows are 6-8 minutes for 3-5 multi-part items.**
Files: `l2-ws2` (60-66), `l5-ws2` (61-68), `l6-ws2` (60-67), `l9-ws2` (59-67), `l10-ws2` (58-66).
Problem: L2 page 2 = Q4 (5 parts), Q5 (two magic triangles), Q6 (+Challenge) in 6 min. L10 page 2 = 5 questions including "make your own puzzle" in 8 min. A 7-year-old doing written explanations online needs about 2.5-3 min per multi-part item.
Fix: Give each page-2 window 10 minutes by trimming the pre-teaching slides on page 2 (L2: merge `l2-teachtri` and `l2-teachtwo` into one 2-minute slide; L10: move Q9 "make a puzzle" to the Talk time slot) and set the Stretch slide to 66-70 only for those who have finished. Move check-together (66-70) to 68-72 and shorten Talk time to 72-80.

**9. P-1 Talk time vs Challenge schedule (programme-wide).**
Files: all `rebuild/gen_l*.py` (`l*-challenge`, `l*-chdiag`).
Fix: relabel Challenge slides "Optional: if you finish early" with no clock time, or "70-80" only on Talk time. Add one line to the routine slide: "Think Harder and Challenge are for early finishers or home."

### MEDIUM

**10. L3: scale keys, tally and building graphs are beyond P1 (reading only); Challenge Q8 uses division and "twice".**
Files: `qbank.json` L3 stretch 1-5, challenge 6-8; `hp/workbook.js` L3 Part B; slides `l3-teach2`, `l3-try2`, `l3-teach3`.
Problem: P1 picture graphs are read, not built, with one picture = one child. Keys of 2, 3, 4 are P2. Challenge Q8 ("1 picture = 4 children. 40 children... how many pictures in all?") needs 40 / 4; division within 20 is P1. "Orange got twice as many as banana" (Q7) is P2-P3 language.
Fix: Keep the key-of-2 work (it is well taught on slides and labelled Think Harder). Replace Challenge 8 with: "1 picture = 2 children. 20 children voted for three fruits. A has 3 pictures. B has 2 more pictures than A. How many children chose C?" Answer: 4 children (2 pictures). 20 / 2 = 10 pictures; counting in 2s to 20 is within reach. Replace "twice as many" in Q7 with "Orange got 6 more votes than banana. Apple got 6 votes. 24 voted. How many votes did banana and orange get?" Answer: banana 6, orange 12.

**11. L7 ambiguous items.**
Files: `qbank.json` L7 stretch 1 and 7; `hp/workbook.js` L7 Q3a, L10 Q5a.
Problem: "4 sides, all the same length" also describes a rhombus. "Which shape has the same number of sides as a rectangle but is not a rectangle" also fits trapezium, kite, rhombus, parallelogram; the key accepts only two.
Fix: Stretch 1 and Q3a: change to "I have 4 sides, all the same length, and 4 square corners. What shape am I?" (square). L10 Q5a: same wording. Stretch 7: see Issue 7(b).

**12. L9 Core 4 answer is arguable.**
File: `qbank.json` L9 core[3]: "Which is longer: 8 cubes or 8 paper clips? Why can we not tell?" -> "We cannot tell. The units are different sizes."
Problem: A child can reasonably say "clips are longer" (true in real life); the answer is wrong for them.
Fix: replace with "A rope is 8 cubes long. A string is 8 paper clips long. Do we know which is longer? Why not?" -> "No. A cube and a paper clip are different lengths, so 8 of each are not the same."

**13. L9 Think Harder duplicates the main worksheet and the Talk slide.**
File: `qbank.json` L9 stretch[2] ("Ali's desk is 6 spans... Mei's 9 spans...") repeats workbook Q3 and `l9-talk`. stretch[0],[1] repeat `l9-tryconv`.
Fix: make the first four stretch items: stretch[3] caterpillar (15 cubes), [4] string/rope (23), plus two new: "A ribbon lies from the 3 cm mark to the 11 cm mark. How long is it?" (8 cm), and "A pencil is 3 erasers long. A ruler is 2 pencils long. A desk is 4 rulers long. How many erasers long is the desk?" (24; currently only a slide item).

**14. L9 Challenge Q6 uses "ruler" for a 12-cube object.**
File: `qbank.json` L9 challenge[5]: "A ruler is 12 cubes long..." Lesson now teaches a cm ruler.
Fix: "A stick is 12 cubes long. Ali measures a desk by laying the stick end to end 4 times and then 5 more cubes. How long is the desk in cubes?" (53).

**15. L9 Q2 table "Difference" column is unexplained on the worksheet.**
File: `hp/workbook.js` L9 Q2 (column header "Difference").
Fix: header "Difference (guess and measure)". Add to the instruction: "Write how far off your guess was."

**16. L5 Challenge: age puzzle and Think Harder repetition.**
Files: `qbank.json` L5 challenge[7] ("Ali is 5 years older than Ben. In 3 years' time their ages will add up to 25"); workbook `extra(5)`.
Problem: Age-and-sum problems are P4 model-method; "in 3 years' time" adds a time step. Think Harder 1-4 are four "add then take away" items, the same type as Q1c and slide `l5-try2`, so they do not stretch.
Fix: replace challenge[7] with "Ali and Ben have 20 marbles together. Ali has 4 more than Ben. How many does each have?" (Ben 8, Ali 12; the L5 slide stretch 1). Replace stretch[0] and stretch[1] with the existing stretch[5] (Ben marbles, 14) and "Ben had some stickers. He gave away 6, got 4, then gave away 3. Now he has 10. How many at first?" (15).

**17. L1 Challenge ambiguity and difficulty.**
File: `qbank.json` L1 challenge[5]: "A pattern adds the same number each time. Its 5th number is 20 and it starts at a whole number more than 0. How many different patterns..."
Problem: "adds the same number" does not exclude adding 0 (start 20, add 0), and add 5 gives start 0 which is excluded only by the start clause.
Fix: "...It adds a number bigger than 0 each time, its 5th number is 20, and it starts at a whole number bigger than 0." Answer stays 4. Also Challenge 9 (workbook Q7) needs two long lists (17 and 13 numbers) offset from 0; fine for strong thinkers but keep the walk-through slide visible (`l1-chwalk` already lists both).

**18. L6 Challenge 4 is ambiguous.**
File: `qbank.json` L6 challenge[3]: "Which amounts from 5c to 50c cannot be made using only 20c and 10c coins?"
Fix: "Which amounts in 5c steps (5c, 10c, 15c ... 50c) cannot be made using only 20c and 10c coins?" Answer unchanged: 5c, 15c, 25c, 35c, 45c.

**19. L8 reading load and unexplained terms.**
Files: `hp/workbook.js` L8 Q1c, Q5; slides `l8-we2`, `l8-ws1`.
Problem: Q1c is 4 sentences. "Odd numbers" labels the Venn loop but odd/even is only explained on a late L1 slide (`l1-teachtable`) and is not in P1. "Venn diagram" and "logic grid" are adult terms.
Fix: Q1c: split into three lines with the same words. On `l8-we2` or `l8-ws1`, add a printed reminder: "Odd numbers end in 1, 3, 5, 7, 9. Even numbers end in 0, 2, 4, 6, 8." Call it "two-loop picture" in the child-facing slide text (keep "Venn diagram" in tutor notes).

**20. L8 Q4: "behind" ambiguity is handled only by a tutor note.**
Files: `hp/workbook.js` L8 Q4 ("Ben is behind Ali. Sam is behind Ben.") and slide `l8-ws2` note: "'behind' means somewhere behind, not always right behind."
Problem: The worksheet does not say so; in this puzzle the answer is unique either way, but children over-think it.
Fix: change the Q4 text to "Mei is first. Ali is in front of Ben. Ben is in front of Sam. Where does each child stand?" (Mei, Ali, Ben, Sam).

**21. L7 exit ticket is a transfer problem, not a check of the core idea.**
File: `lessons.js` L7 `exit`; slide `l7-exit`: "How many squares in a grid 4 long and 2 high?" (11).
Problem: The 4 x 2 grid was never taught; half the group will write 8 (small squares only).
Fix: use the grid that was taught: "How many squares are in a 3 x 3 grid?" (14), or a 3 x 2 grid for a mild transfer (6 small + 2 of size 2 x 2 = 8). Keep 4 x 2 (answer 11) as the extension.

### LOW

**22. `qbank.json` L7 core[4]: "does a octagon have?" -> "does an octagon have?"** Cause: template in `hp/qbank.py` line 193 (`'... does a %s have?'`). Fix: use "an" for octagon (e.g. `('an' if n[0] in 'aeiou' else 'a')`).

**23. L7 circle "0 sides".** Workbook Q2 gives the circle 0 sides and `lessons.js` lists "Saying a circle has 1 side" as a mistake. Some school textbooks describe a circle as having 1 curved side. Rename the column "Straight sides" (circle: 0) so the answer is true under either convention.

**24. L8 `l8-ws2` note is stale.** It says the worksheet does not say "each child has a different pet"; the workbook Q3 does ("each have a different pet"). Remove the note's parenthesis.

**25. L9 workbook Q6** ("exactly 10 cubes long") is replaced in Issue 2. If kept, change to "about 10 cubes long" (exact matches are unrealistic).

**26. Safety: matchsticks.** L4 `materials`: "21 matchsticks or straws per pair"; `online`: "straws, toothpicks or pencils at home". Real matches and toothpicks should not be handled by 7-year-olds unsupervised. Change to "21 straws, lolly sticks or paper strips per pair (never real matches)". L8 buttons: add "Small objects: only with a grown-up nearby".

**27. P-2 break.** Add a 60-90 second "stand up and stretch" at about minute 65 (a line on the `l*-ws2ans` slide) so there is movement before Talk time.

**28. P-4 numbering.** In `extra()` of `hp/workbook.js`, number Think Harder `T1..T4` and Challenge `C1..C3`, and update `l*` slide references ("Finished early? Stretch and Challenge come next").

**29. P-5 slide vs workbook stretch.** Make the slide Stretch (`l*-stretch`) use the same four items as the workbook Think Harder (or print answers for the slide items in `lessons.js` `key`). Currently answers for the slide-only items exist only in speaker notes.

## 4. Per-lesson detail (a)-(f)

Legend: (a) syllabus fit, (b) difficulty of Core / Think Harder / Challenge, (c) reading load, (d) answers/ambiguity, (e) 90-minute timing, (f) online suitability.

**L1 Count with the Frog.** (a) Number patterns and skip counting are in the P1 sequence content; common multiples of two counts is just beyond. (b) Core: 6 add/subtract rules, easy. Think Harder: gaps, 8th-number, "does 30 belong", "which number does not belong": a real step up. Challenge: growing gaps (2,4,7,11,16), two offset sequences: strong. (c) Light. (d) All correct; Issue 17. (e) Page 1 13 min, page 2 8 min: fine. (f) Number strip printed; fine.

**L2 Number Bond Inquiry.** (a) Bonds to 20 are P1 core; "=" as balance is P1; magic triangles and sum-and-difference are beyond but taught with cubes. (b) Core: bonds, trivial. Think Harder: balance equations, fine. Challenge: magic triangle for 11, 20 - 9 shared 3 more: strong. (c) Light. (d) Correct; all magic-triangle solutions are unique (checked). (e) Issue 8. (f) Needs a printed triangle (provided).

**L3 Fruit Party.** (a) Reading picture graphs is P1; building graphs, keys above 1 and tally are P2. (b) Core: read, compare, total: right. Think Harder: key of 2: right with the slide teaching. Challenge: Issue 10. (c) Q6/Q7 need sentences. (d) Correct. (e) Page 2 (58-66) = Q6, Q7, group vote with tally, Q8, Q9: tight. (f) Group vote in chat works.

**L4 Pattern Inquiry.** (a) Shape/number repeating patterns appear informally in P1; growing matchstick patterns and the core-length trick are beyond (P3). (b) Core: positions up to the 15th with cores of 2-4: reachable by drawing. Think Harder and Challenge appropriately graded. (c) Light. (d) All correct (checked cores, 25 sticks = 12 triangles exactly, 50 sticks = 16 squares + 1). (e) Fine. (f) Issue 26.

**L5 Mystery Number.** (a) Inverse of +/- within 20 and 100 is P1; two-step undo is stretch. (b) Core easy; Think Harder repetitive; Challenge Issue 16. (c) Q4 wording is long. (d) Correct (snail: day 4, checked). (e) Page 2 7 min. (f) Fine.

**L6 Coin Combos.** (a) Coins and notes are P1; systematic listing is enrichment. (b) Core is doable; main worksheet and Think Harder are Issues 3 and 4. (c) Heavy: 5 questions with long stems. (d) All correct (brute-forced: 4, 6, 9 ways; 2 sets of 4 coins for 70c; 15 amounts); Issue 18. (e) Issue 3. (f) Play money must be cut out (pairs need about 24 coins).

**L7 Shape Safari.** (a) Issues 5 and 7. (b) Core is vocabulary; Think Harder inverted (Issue 6); Challenge (15 triangles, 9 squares) is P3-level but fine for strong thinkers and well walked-through. (c) Light. (d) All correct (house = 8, Q4 = 3, 2, 8, grids 5, 14, 11, 20); Issue 11, 22, 23. (e) Overloaded. (f) Needs scissors; shape hunt at home is fine.

**L8 Logic Lab.** (a) Logic puzzles, Venn diagrams, odd/even are enrichment. (b) Core: orderings, easy. Think Harder fine. Challenge (apples/oranges box, 20-number Venn) is strong. (c) Highest of the course; Issue 19. (d) Correct (orderings and riddles brute-forced; all unique). (e) Pages fit. (f) Items from home: ok.

**L9 Measure It!** (a) Issue 2. Unit-conversion questions (clips to erasers) are P2-P3 but well taught. (b) Core easy; Think Harder (Issue 13); Challenge ok. (c) Q5 is 3 sentences. (d) Correct; Issues 12, 14, 15. (e) Fine. (f) Needs a ruler; cube strip is printed.

**L10 Challenge Day.** (a) Revision of L1-L9; fine. (b) Core/Think Harder/Challenge consistent with earlier lessons. (c) Fine. (d) Correct (checked pattern 10th = 32, 70c four coins = 2 ways, stickers 8/12/9). (e) Issues 1 and 8. (f) Breakout rooms with no cards: Issue 1.
