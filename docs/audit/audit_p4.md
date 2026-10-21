# Audit: Math Inquirers P4 Holiday Program (suitability and difficulty)

Scope: `p4/content/l1.js` to `l10.js` (lesson, script, deck, qbank, workbook), `p4/data.js`, `p4/workbook_html.js`, the rendered `p4/Math_Inquirers_P4_Student_Workbook_Designed.pdf` (51 pages), and all 10 slide decks in `split/p4l1` to `split/p4l10` (25 to 27 slides each).
Audience: children aged 10 to 11 finishing Primary 4 (Singapore), 10 lessons x 90 min, online, groups of 8, inquiry-based, leading into P5.
Status: read-only audit. No content file was edited and nothing was committed.

Method
- Syllabus check against the MOE 2021 P4 mathematics content as published by schools (e.g. Tao Nan Primary "Curriculum Information 2024 P4 Mathematics": whole numbers to 100 000 with rounding to the nearest 10, 100, 1000; factors of numbers within 100, common factors, multiples of 1-digit numbers and common multiples of two 1-digit numbers; fractions (equivalent, mixed/improper, comparing, add/subtract, fraction of a set); decimals to 3 places; angles (name, measure, draw); area and perimeter of composite figures; nets; symmetry; tables and line graphs) plus `p4/SPEC.md`.
- Every numeric answer in every `key`, `qbank` (core, stretch, challenge), `deck` and slide note was recomputed. Uniqueness claims ("only one answer", "find ALL") were brute-forced in Python/node (signs and brackets puzzles, digit-sum and digit-card puzzles, rounding overlaps, logic grids, seating puzzle, heads-and-legs). The cube-net claims in Lesson 8 were checked with a small cube-folding simulation (which of the 6 shapes fold, opposite faces on both dice nets and the lettered net, 8 of the 12 pentominoes fold into an open box, 11 hexomino nets).
- Slide timelines, element counts, font sizes (no CSS font under 24 px, none over 200 elements, no notes over 4000 chars) and the PDF page flow were inspected.

Headline result: no wrong numeric answer was found anywhere in the 10 lessons (about 300 items rechecked). The real problems are pacing, pagination, a handful of items pitched above "Core", two ambiguous items, some answer leakage between slides and printed pages, and online practicalities.

---

## 1. Summary table

| Lesson | Verdict | One-line reason |
|---|---|---|
| 1 Factor Hunters | minor fix | Content and answers sound; Q2 orientation ambiguity, exit ticket and Think Harder Q1 reuse worked examples from the slides, Q5c is stretch-level in a 7-minute solo page. |
| 2 Big Number Puzzles | minor fix | Syllabus-aligned; Q2b and Q4a are Think-Harder difficulty inside the Core pages; 7 teaching slides in 10 minutes. |
| 3 Operation Detectives | minor fix | Good lesson; page 2 has four question types in a 7-minute slot, and Q5b ("explain why the trick works") is beyond most P4 children. |
| 4 Fraction Frontier | minor fix | Page 2 is overloaded (Q4 to Q7, five teaching slides in 6 minutes, one slide with 74 elements); Q6/Q7 are stretch-level. |
| 5 Decimal Detectives | minor fix | Strong lesson; Q7 and 2-decimal rounding in the Core bank are above Core; rounding to 2 d.p. is probably P5. |
| 6 Angle Turns | needs rework | Page 2 packs four sub-skills (10 sub-parts); Q5c diagram is unclear; one Think Harder item is ambiguous; clock-hand angles go beyond P4. |
| 7 Area Architects II | minor fix (layout, high priority) | Content is the best-fitting of the set, but the printed workbook runs to 4 pages instead of 2 (Q3 stranded alone, Q6 on page 4). |
| 8 Symmetry and Nets | minor fix (layout, high priority) | Content and answers verified; same pagination bug (4 pages, Q3 and Q6 stranded); Q4 key text wrong; last Think Harder item is too easy. |
| 9 Data Detectives | OK | Syllabus-aligned, answers all correct; one inconsistency between the workbook graph and the teaching slide (faint gridlines). |
| 10 Challenge Day | OK | Heuristics are the point; supposition and age problems are above P4 but are taught on the slides; Q4 logic grid is easy. |

---

## 2. Cross-cutting findings (affect every lesson)

### 2.1 The 90-minute plan does not fit the work set
Every deck uses the same clock (checked in all 10 `deck.json` orders):

| Block | Slide clock | Work asked | Realistic need |
|---|---|---|---|
| Warm-up + quick questions | 0 to 10 | 2 slides | 10 (fine) |
| Explore | 10 to 25 | 2 slides, 15 min | fine, but it eats the lesson |
| Teaching | 25 to 35 (L8 25 to 36) | 5 to 7 content slides, whiteboards up, reveals | 14 to 18 min |
| Worksheet page 1 | 40 to 52 (12 min) | 3 questions, 6 to 9 sub-parts, in pairs, in breakout rooms | 15 to 20 min |
| Page-2 pre-teach | 54 to 60 (6 min) | 3 to 5 new mini-lessons (L4: 5 slides; L3: 4; L6: 4) | 8 to 10 min |
| Worksheet page 2 | 60 to 67 (7 min) | 3 to 4 questions, 6 to 10 sub-parts, alone | 15 to 20 min |
| Check page 2 | 67 to 69 | | 3 to 4 min |
| Challenge slides | 65 to 80 | 3 slides (challenge, see it, walk-through) | 12 to 15 min |
| Talk time | 70 to 80 | | 10 min |
| Exit ticket | 80 to 90 | 1 slide | 5 min |

Problems: (a) page 2 gets 7 minutes for the individual work that has the most new skills; (b) "Challenge 65 to 80" and "Talk time 70 to 80" overlap, so the 3 challenge slides cannot both be done and discussed; (c) the two Think Harder pages (4 Stretch + 3 Challenge items per child) have no time slot at all; (d) page-1 "work in pairs" in breakout rooms costs 2 to 3 minutes each way online.

Proposed fix (apply to the shared slide generator `rebuild/gen_p4l*.py` clock labels and to the title-slide notes):

| Slot | Proposed |
|---|---|
| Warm-up (game) | 0 to 5 |
| Quick questions | 5 to 8 (5 questions, 35 s each) |
| Explore (merge explore1 and explore2) | 8 to 18 |
| Teaching (max 4 content slides incl. one "your turn") | 18 to 30 |
| Brain break | 30 to 34 |
| Worksheet page 1 | 34 to 50 |
| Check page 1 | 50 to 53 |
| Page-2 pre-teach (max 2 to 3 slides) | 53 to 58 |
| Worksheet page 2 | 58 to 76 |
| Check page 2 | 76 to 80 |
| Talk time | 80 to 85 |
| Exit ticket | 85 to 90 |
| Challenge slides and Think Harder | early finishers, then take-home (state this on the Think Harder page and in the title-slide notes) |

### 2.2 Think Harder pages
- Layout is fine: stretch page + challenge page, 2 pages per lesson, no spill to a 4th page in any lesson (the PDF confirms this).
- Difficulty gradient is weak: the first "Stretch" item is often Core level (L2, L3, L4, L5, L9; see issue 8). The three printed Challenge items are consistently genuine challenges, apart from L6 Q7 (ambiguous) and L8 Q7 (too easy).
- The challenge slides in L5, L6 and L8 show items that are not the three printed Challenge items, so the strongest printed items in those lessons have no "see it" or walk-through support. Acceptable if intended; otherwise point the slides at the printed Q5 to Q7.

### 2.3 Reading load and vocabulary (computed from the workbook text)
- Words per question stem: median about 45, longest single stem 41 words (L5 Q4); whole-lesson workbook text 190 (L8) to 320 (L5, L7) words. Short enough for 10-year-olds. Longest multi-part blocks: L3 Q3 (84 words, 4 sub-parts), L9 Q1 (79 words), L1 Q6 (72 words).
- Vocabulary introduced is handled (palindrome defined in the question; improper fraction and mixed number defined at the top of L4 page; vertex, ray, angle notation and clockwise explained in L6 slides). "Next-door numbers" is friendly but non-standard (say "consecutive numbers (next-door numbers)" once in L10 Q1a). "Breadth" and "tenths/hundredths/thousandths" are standard Singapore usage.
- No language above P4 reading level was found.

### 2.4 Online practicalities
- Heavy pre-lesson preparation falls on parents: 24 paper squares (L1), digit cards 0 to 9 (L2, L5), sign and bracket cards (L3), paper circles cut in quarters (L4), protractor and paper clock (L6), 12 tiles and a cutting strip (L7), 6 paper squares and tape (L8), printed graph grid (L9). Provide one "Materials to prepare" note per lesson sent 48 hours before (the workbook already ends with 4 kit pages from `p4/kit.js`: cut-outs, square grid, dot grid, cube net; say which one each lesson needs).
- Workbook must be printed (L6 Q1 is measured with a protractor; L7 Q3, L8 Q4 and Q6 need drawing). Tell parents to print at 100 percent, black and white is fine. Drawn arms in L6 Q1 are only about 2.7 to 3.1 cm; the slide already says "draw them longer with a ruler" (good); add the same sentence under the Q1 table.
- Clockwise and anticlockwise (L6): on a mirrored self-view the turn looks reversed. Add to the L6 warm-up notes: "Say 'turn to your right' for clockwise, and tell children to ignore their own picture."
- Breakout rooms: all "with your partner" page-1 work and L10's four-station explore need breakout rooms. Note a 2-minute transition in the plan, or run ws1 as whole-class screen-share if only 8 children.

---

## 3. Specific issues, ranked by severity

### High

**1. L7 and L8: printed workbook is 4 pages, not 2 (file: `p4/content/l7.js`, `l8.js` workbook figures; PDF pages 27 to 30 and 33 to 36).**
Evidence from the rendered PDF: page 27 = header, Q1, Q2 only; page 28 = Q3 alone on an otherwise empty page; page 29 = Q4 and Q5 with about 38 percent free; page 30 = Q6 alone. Same pattern in L8 (p33 Q1, Q2; p34 Q3 alone; p35 Q4, Q5; p36 Q6 alone). The slides tell children "Page 1: Q1 to Q3, Page 2: Q4 to Q6", so a child flips to the wrong page, 2 sheets are mostly blank, and the lesson prints 6 pages instead of 4. Cause: each question is a keep-together chain (stem + figure + sub-parts) and the figures are too tall.
Fix (then re-render and confirm 2 pages):
- L7: `q1Svg` cell size `c = 20` to `16` and viewBox height 190 to 160; Q2 table row height `h: 60` to `h: 44` (three rows); `blankGrid(24, 4, 22, ...)` to `blankGrid(24, 3, 22, ...)`; merge the two `H.ans` lines in Q1b into one; Q6 figure `c = 14` to `11` and drop the single `H.lines(1)` after Q6c (use a ruled blank at the end of the sub-part instead).
- L8: `q1Svg` `ph = 96` to `84`; `q2Svg` `c = 44` to `36`; `q6Grid` cell `c = 30` to `26` (and `q6Svg` height accordingly); keep the existing `{pb:true, before:0}` on Q4.
- If Q3 still will not fit on page 1 in either lesson, move Q3 to the top of page 2 and move that lesson's Q6 to Think Harder as a Stretch item (both lessons have a 6th question beyond the 5 that the page can hold).

**2. All lessons: the slide clock is unrealistic (see 2.1).**
Fix: replace the labels in every `gen_p4lN.py` with the proposed clock in 2.1; shrink the teaching block to 4 content slides (each "Your turn" slide is optional and can be dropped); state in the title-slide notes that Challenge slides and Think Harder are for early finishers and take-home.

**3. L6: page 2 is overloaded and Q5c is unclear (file `p4/content/l6.js`).**
Page 2 asks four different sub-skills (clock angles, compass turns, corners of squares, robot cards) with 10 sub-parts in a 7-minute slot, after 4 pre-teach slides in 6 minutes. Clock-hand angles (30 degrees per hour space, 6 degrees per minute, Q3d) go beyond P4 (they are P6 or competition material) though the slides do teach them.
- Fix A: take Q3d ("How many degrees does the minute hand turn from 3:10 to 3:35?" key 150) and Q6b ("Find ALL the pairs") off the Core page. Q3d is already covered by `qbank.stretch[2]` ("7:15 to 7:50"), so delete it; Q6b becomes a Stretch item. Page 2 is then Q3 (a to c), Q4 (a to d), Q5 and Q6a: 8 sub-parts instead of 10. Also update `lesson.key` Q3 and Q6 and the `p4l6-ws2`, `p4l6-ws2ans` slides.
- Fix B: in the render, the Q5 figure is only about 2.2 cm per drawing, label "a" and "58 degrees" collide, and in (c) the overlapping translucent squares hide where angle c is. Enlarge `corners()` (make each drawing about 25 percent larger, give the three drawings their own rows if needed) and add words to the stem: "In (c) two squares share the corner O. The angle where they overlap is 30 degrees. Angle c is the whole angle covered by the two squares together." Key unchanged (c = 150).
- Fix C: Think Harder challenge item 9 (`qbank.challenge[8]`) is ambiguous without a figure. Replace the text with: "Two squares share one corner O and overlap, like Q5(c). The angle covered by both squares together (from the outside side of one square to the outside side of the other) is 160 degrees. What is the angle where the squares overlap?" Answer unchanged: 20 degrees. Add a small figure to the Think Harder page or the challenge slides.

### Medium

**4. L1 Q2: orientation ambiguity (file `l1.js`, `workbook`, Q2).**
The explore activity (tiles) says "a 2 by 12 and a 12 by 2 count as the same", but Q2 expects 6 ways including both 2 rows of 20 and 20 rows of 2 (key and 7-column table). A child applying the lesson rule finds 3 ways and is marked wrong. The tutor note on the ws1 slide explains it, but the child sees nothing.
Replace the stem with: "A gardener plants 40 trees in equal rows. There are at least 2 rows, and at least 2 trees in each row. (2 rows of 20 trees and 20 rows of 2 trees are different ways to plant.)" Keep the key (6 ways).

**5. Answer leakage from slides into the printed pages and exit tickets.**
- L1 exit ticket asks for all the factors of 18, but slide `p4l1-teachodd` (54 to 56) already lists the factor pairs of 18 and states "6 factors", and quick question 5 (`warm2`) asks for 18 as a product. The first part of the exit ticket is therefore a copy exercise. Replace `lesson.exit` and the exit slide with: q "Write all the factors of 28. Then find the smallest number that is a multiple of both 6 and 9." a "1, 2, 4, 7, 14, 28. The smallest common multiple of 6 and 9 is 18."
- L1 Think Harder Stretch 1 (`qbank.stretch[0]`, "How many factors does 36 have?") is the worked example on slide `p4l1-we1`. Replace with: "How many factors does 72 have? List them in order." a "12 factors: 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72." (slide stretch uses 64, teachodd uses 100 and 81, so 72 is new.)
- L10 exit ticket ("10 heads, 26 legs, ducks and goats") is almost the same as slide `try2` a ("10 heads, 28 legs, ducks and cows"). Change the exit numbers to "12 heads and 34 legs" (answer 5 goats and 7 ducks: all ducks 24 legs, 10 short, each swap adds 2, so 5 swaps; check 7 x 2 + 5 x 4 = 34).

**6. Items at Think-Harder difficulty inside the Core worksheet pages.** "Core: doable by almost every child" is not true for:
- L2 Q2b (two rounding clues, find the overlap) and Q4a (rounding clue + digit clue + "tens digit double the ones digit" + "all digits different"). Simplify Q4a to: "I am a 5-digit number. Rounded to the nearest thousand, I am 48 000. My hundreds digit is 6. My ones digit is 1 and my tens digit is double my ones digit." Answer 47 621 (still unique; checked). Mark Q2b with a star ("star = stretch").
- L3 Q5b ("Explain why the number trick always gives 7. A bar model can help") needs algebraic reasoning. Replace with a scaffold: "Fill in: Multiplying by 5 and then dividing by 5 gives back my ______. The 35 divided by 5 adds ______. Taking away my number leaves ______." (answers: number, 7, 7.) Keep the open version as a Think Harder stretch.
- L4 Q6 (find ALL twelfths between 1/3 and 3/4, ends excluded) and Q7 (five-clue "Who am I?"): fine as page-2 "star" items, but with Q4 and Q5 on the same page the page has 8 sub-parts. Move Q7 to Think Harder Stretch and keep Q6.
- L5 Q7 (mystery decimal: 3 decimal places, rounds to 4.7, hundredths = tenths + 2, digits add to 25) is a 5-condition search. Keep but star it; the slide `teachclue` already models the method.
- L1 Q5c ("Find ALL the numbers from 1 to 60 with exactly 3 factors") needs the square-of-a-prime insight; Q5b leads to it, but give the hint in the stem: "Hint: look at your answer to (b)."

**7. L9 Q1: workbook graph vs teaching slide (file `l9.js`, `juiceSvg`).**
The slide teaches "each numbered line is worth 10, the faint lines are 5" (so 25 is on a faint line), but `juiceSvg` draws only lines every 10 (`step: 10, lab: 10`), so Monday-to-Sunday values 25, 55, 65, 75 have to be read halfway between lines with no guide, in a "Core" question. Fix: `step: 10` to `step: 5` (keep `lab: 10`), exactly like `moneySvg`.

**8. Think Harder gradient (file `qbank.stretch[0]` in each lesson).** The first printed "Stretch" item is Core-level in L2 ("smallest number that rounds to 80 000"), L3 ("120 − 4 × (18 + 7)", same type as the exit ticket), L4 ("how many quarters in 4 3/4", same as workbook Q1d), L5 ("write 5 decimals in order", same as workbook Q2a) and L9 ("biggest change between 4 days of museum visitors", same as the worked example). Swap each with a harder stretch item already in the bank (only indices 0 to 3 are printed): L2 swap `[0]` and `[4]` (the 55 555 riddle); L3 swap `[0]` and `[4]` (the 2 340 beads, 4 times as many bar model); L4 swap `[0]` and `[6]` (7/4 against 1 5/8 pizzas); L5 swap `[0]` and `[5]` (find ALL digits in the box 3.[ ]5 < 3.42); L9 swap `[0]` and `[6]` (the 4A/4B girls puzzle). Keep L1, L6, L7, L8, L10 as they are (apart from the L1 change in issue 5).
Also L8: the last printed Challenge item (`qbank.challenge[8]`, "Ali says the 4 side faces always add up to 14") is a yes-or-no explain item, easier than the stretch items. Swap `challenge[8]` with `challenge[4]` (shade 5 squares of a 3 by 3 grid to get 4 lines of symmetry) so the printed page ends on a genuine challenge; the slides already show that item.

**9. L5: rounding scope.** The syllabus source does not say which decimal places are rounded at P4; school schemes normally put the nearest whole number and 1 decimal place at P4 and 2 decimal places at P5. The lesson also asks 3 d.p. to 2 d.p. (challenge 1, 3-decimal mystery number) and Core item 4 ("Round 7.462 to 2 decimal places"). Replace Core item 4 with: q "Round 7.46 to 1 decimal place." a "7.5". Leave the 2 d.p. items in Stretch and Challenge, where they are a reasonable step beyond.

**10. L4 slide `p4l4-teachcompare` (54 to 56): 74 elements, three comparison tools in 2 minutes.** Split into two slides (tools 1 and 2; tool 3 and the "your turn"), or cut the third tool (same numerator) to Think Harder. Also `p4l4-teachfind` has 85 elements and combines two lessons (find ALL, and Who am I?): move "Who am I?" to the Think Harder page together with Q7 (issue 6).

### Low

**11. L8 Q4 key is wrong in its description (file `l8.js`, `lesson.key` Q4 and the tutor key).** It says "counting squares from the left edge of the grid"; the counting is from the dashed line. Replace with: "(a) Rocket: flip each corner across the dashed line, the same number of squares on the other side: shoulders 2 squares to the right of the line, fin tips 4 squares to the right at the bottom, bottom edge ends 1 square right of the line, notch on the line, then join. (b) Fish: flip each corner below the line, the same number of squares: tail tip 2 below, then 1 below, back 3 below, 2 below, nose on the line."

**12. L8 Q3, Q5: sub-labels.** Q3 shows only "(c)" in the text and Q5 prints "a ____ (b) ____ (c) ____ (d) ____" with only the first label styled as a sub-letter. Change Q5 line to `H.sub('', '(a) ________   (b) ________   (c) ________   (d) ________')` and Q3's "c" to "a" (and add "b" for the second net), or label (a)/(b) in the text.

**13. L1 Q1a wording.** "You may not need every row" but the grid is a single row of six boxes: change to "You may not need every box."

**14. L1 Q4 (buses every 10 and 15 minutes).** The syllabus says common multiples of two 1-digit numbers; 10 and 15 are 2-digit. Not wrong, a small step beyond, and the slide teaches the method. Recommendation: leave as is (changing the numbers would force a re-key of part b and the time-line drawing).

**15. L1 `qbank.challenge[5]`.** "Both of its factor pairs use odd numbers only" is redundant because every odd number has only odd factors. Replace with: "Find a number between 20 and 40 that has exactly 4 factors and is odd." Same answer list (21, 27, 33, 35, 39).

**16. L2 slide `p4l2-we1`** uses the "approximately equal" sign in "36 482 ≈ 36 000". The sign is in MOE P4 textbooks, but add "(≈ means 'is about')" to the slide notes in case children have not met it.

**17. Housekeeping.** Comments in `p4/data.js` ("p2/content/l1.js") and `p4/workbook_html.js` ("Run in p2/") still say p2. No effect on output.

**18. Syllabus coverage gaps (informational).** The 10 lessons do not touch pie charts (listed for P4), equivalent-fractions practice beyond the L4 warm-up, adding and subtracting fractions beyond the warm-up, multiplying 3-digit by 2-digit numbers, or nets on an isometric grid. Acceptable for an enrichment programme, but say so in the parent pitch.

---

## 4. Lesson-by-lesson judgement

(a) topic fit, (b) difficulty of Core / Think Harder / Challenge, (c) reading load, (d) wrong or ambiguous items, (e) 90-minute realism, (f) online confusion.

### L1 Factor Hunters
a. In syllabus: factors within 100, common factors (18 and 24, 12 and 18, 36 and 48), common multiples. Slightly beyond: Q4 uses 10 and 15 (2-digit), odd/even number of factors (enrichment, well taught).
b. Core Q1 to Q4 right; Q5c and Q6a are firm for a solo page. Think Harder: stretch gradient fine; challenge items (bells 4, 6, 10 = 60; remainder 1 = 61; 20 lockers) are genuine challenges, the locker puzzle needs the odd-factors idea from the slides (it is explained).
c. Light. d. No wrong answers. Ambiguity: Q2 orientation (issue 4). Leaks: issue 5. e. 7 teaching slides in 10 min (we1, we2, we3 plus 2 "your turn" slides); ws2 at 7 min is short for Q4 to Q6. f. Needs 24 paper squares ready.

### L2 Big Number Puzzles
a. In syllabus (5-digit numbers, rounding to 10/100/1000). Rounding backwards, overlaps of two rounding clues, palindromes, digit-sum counting: enrichment, appropriate to Think Harder, heavy for Core.
b. Q1, Q3, Q5, Q6 are Core. Q2b and Q4a are stretch (issue 6). Think Harder: well pitched.
c. Light. d. All answers verified (47 621 unique; 15 five-digit numbers with digit sum 3; 100 palindromes 4aba4 etc.). e. Six content slides in 10 min is too many (rounding to 1000/100, working backwards, two clues, estimate). f. Digit cards are used on camera; fine.

### L3 Operation Detectives
a. In syllabus (order of operations and brackets are P4 content in most schemes; bar models "times as many"). Number tricks and 4-4-4-4 are enrichment.
b. Core Q1 to Q4, Q6, Q7 fine; Q3d (two pairs of brackets) and Q5b are above Core (issue 6). Think Harder: challenge items (signs 1 to 6 sum 7, half-and-$6 money puzzle, backwards chain) are good.
c. Q3 is the longest block (84 words). d. All answers correct; "only one answer" claims for Q2 and Q3d verified unique. Q7b needs guess and check (taught). e. Page 2 has four unlike questions in 7 min; four pre-teach slides in 6 min. f. Sign and bracket cards on camera need prep.

### L4 Fraction Frontier
a. In syllabus (improper/mixed, fraction of a set, comparing). "Find the whole from a part" is at the top of the P4 range; "find all fractions between" is enrichment.
b. Core page 1 right. Page 2 Q4 to Q7 is a lot (issue 6, 10). Think Harder: item 1 is Core (issue 8); challenge items fine (4/16, half-is-3-more-than-third, Siti's book = 150).
c. Fraction layout renders well. d. All answers correct (verified Q4a to e, Q6 = 4 fractions, Q7 = 17/6 unique). e. Heaviest pre-teach block (5 slides in 6 min, two slides over 70 elements). f. Paper circles cut into quarters before the lesson.

### L5 Decimal Detectives
a. In syllabus (decimals to 3 places, ordering, comparing, money and mass). 2 d.p. and 3 d.p. rounding probably P5 (issue 9).
b. Q1 arrow B (6.85) sits between ticks: acceptable halfway reading. Q4 (12 numbers listed) is long but systematic. Q7 is stretch (issue 6). Think Harder fine.
c. Moderate (Q4 68 words). d. All answers correct (47 combos and unique 2.459, 4.687, 3.17 verified). e. Page 2 has four questions; fine after the clock change. f. Digit and decimal-point cards.

### L6 Angle Turns
a. Measuring angles, right angle and 90 degree corners, 8-point compass, angles in squares and rectangles are in scope. Clock-hand angles (30 and 6 degrees, hour hand drift at 3:30 and 9:30) and overlapping squares are beyond P4 but are Think Harder or taught.
b. Core Q1 and Q2 fine. Page 2 too heavy (issue 3). Think Harder: item 9 ambiguous (issue 3 fix C).
c. Moderate. d. All answers correct (compass turns, clock angles, fan 6 angles, robot pair puzzle 2 ways verified). e. Over-packed page 2. f. Protractor and print requirement; mirror image for clockwise (2.4).

### L7 Area Architects II
a. In syllabus (composite rectilinear figures, area and perimeter, squares and rectangles). Borders, plus-shape, paths crossing: enrichment.
b. Core Q1, Q2, Q4, Q5, Q6 right; Q3 (smallest and largest perimeter of a 6-tile shape) is a fine open-ended item. Think Harder good (paths, 9 by 4 into a square, 36-tile perimeters).
c. Q6 70 words but clear. d. All answers verified (area 48 and perimeter 32; staircase 34 and 42; frame 32; 9 by 4 cut to 6 by 6). e. Four printed pages (issue 1). f. Cutting paper strips on camera is fine.

### L8 Symmetry and Nets
a. In syllabus (nets of a cube, line symmetry, completing symmetric figures). Dice puzzles and pentomino open boxes are enrichment.
b. Core fine; Q4 (irregular rocket and fish) is the hardest Core item but the teaching slide models it. Last Think Harder item too easy (issue 8).
c. Light (190 words, the lightest lesson). d. Simulated every net: A, C, E fold; B, D, F do not; lettered net opposites A–E, B–D, C–F; both dice nets have a unique completion; 8 of 12 pentominoes fold into an open box; 11 nets of a cube. Key Q4 text wrong (issue 11). e. Four printed pages (issue 1). f. Paper squares and tape; mirror-hand break is good.

### L9 Data Detectives
a. In syllabus (tables, line graphs, reading scale and change). Misleading scales is an enrichment step.
b. Core Q1 to Q4 fine; Q5 (two shops, same-looking graphs) is the best item in the programme. Think Harder: tank graph and ages in teams are good.
c. Q1 stem 79 words, still fine. d. All answers correct; graph points match the keys. e. Fits (25 slides). f. Printed grid for the explore; graph slides are clear.
Fix: issue 7.

### L10 Challenge Day
a. Guess and check, working backwards, logic and queue puzzles are right for the age. Supposition (heads and legs) and age problems are P5 and P6 methods but are taught step by step in `we2`, `teachages`.
b. Core Q1 to Q6 fine; Q4 logic grid is easy by design (two clues). Think Harder: challenge (15 tables 76 seats; Mei's stickers 32; uncle 4 times as old = 5) good; the uncle item needs the "difference stays the same" idea, which is not taught (the slide teaches the total idea), so it is a true challenge.
c. Light. d. All answers verified (23 by 24, 2 pen-notebook ways, 18 chickens and goats 7 goats, unique seating puzzle). e. Four breakout cards in 15 min is tight; fine. f. Breakout rooms needed.

---

## 5. Items verified correct (so they need no action)
Lesson keys Q1 to Q7 in all 10 lessons; all 60 Core, 80 Stretch and 90 Challenge answers in `qbank`; slide "Your turn" answers; stretch slide answers; the three-step worked examples. Specific brute-force confirmations: L1 Q6a = 36 only; L2 Q4a = 47 621 only; five-digit digit-sum-3 count = 15; L3 Q2 each unique, Q3d two-pair solution unique, 1 to 6 with plus/minus summing to 7 = exactly 2 ways; L5 Q7 = 4.687 only, 2.459 only; L7 Q2 and Q3 perimeters; L8 nets and dice (see above); L9 Q2 table totals 252 and Q3 and Q5; L10 Q1 to Q6, challenge seating puzzle unique, digit-swap puzzle = 47 only.

## 6. Suggested order of work
1. Fix L7 and L8 pagination (issue 1) and re-render to 2 pages.
2. New slide clock and title-slide notes (issue 2).
3. L6 rework of page 2 plus Q5c figure and Think Harder item (issue 3).
4. L1 Q2 and the leaked items (issues 4, 5).
5. Core-versus-stretch re-labelling and the Think Harder swaps (issues 6, 8, 9).
6. Small content fixes (issues 7, 10 to 17).
