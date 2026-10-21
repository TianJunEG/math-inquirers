# Audit: Math Inquirers P3 Holiday Program (suitability and difficulty)

Scope: `p3/content/l1.js` to `l10.js` (lesson, script, deck, qbank, workbook), `p3/data.js`, `p3/SPEC.md`, the 48-page workbook PDF (figures viewed for L2, L6, L7, L8, L10) and the slide text and speaker notes in `split/p3l1` to `split/p3l10`.
Audience: children aged 9 to 10, just finishing Primary 3 in Singapore, going into P4. Online, groups of 8, 10 lessons of 90 minutes.
Method: every numeric answer in the keys, qbanks, workbook figures and slide notes was recomputed (Python brute force for digit, cryptarithm, remainder, fraction, polyomino, money and timetable items; a regex pass over all slide text for "a op b = c"). Syllabus reference: MOE P3 content as set out in a school P3 Math Handbook 2025 (https://shuqunpri.moe.edu.sg/files/P3_Math_Handbook_2025.pdf) and the SPEC.

## 1. Headline findings

- **No wrong answers found.** All keys, qbank answers and slide-note answers recompute correctly. The earlier L3 flag ("4 rows of 5" vs "5 rows of 4") is NOT in the P3 files. It sits in `p2/content/l3.js` (P2 Lesson 3, Q6, 20 chairs; also `split/p2l3/...we1` and `ws2ans`). The P3 equivalent (L3 Q5, 36 chairs) already says "3 rows of 12 is different from 12 rows of 3" and its key is consistent (7 ways, 6 rows of 6 has no partner). So P3 is fine; the P2 wording still needs the same explicit sentence.
- **Syllabus fit is good.** Every lesson topic is in the P3 syllabus. The lessons are enrichment (puzzles, systematic lists, "explain why"), which is what the program promises. Fractions use denominators up to 12 and unlike fractions, which the P3 syllabus does include. Perimeter of rectilinear figures and the 24-hour clock are also P3.
- **Two lessons need rework.** L4 (Model Makers) has several P5-level before-and-after / "same difference" problems on the core worksheet and Challenge slides. L9 (Measure and Money Masters) is too long for the 30-minute worksheet slot (17 lettered parts, five topics) and has one story contradiction.
- **Main systemic risk is timing, not content.** The worksheet slot is 40 to 70 min and must hold 6 to 7 questions (10 to 18 lettered parts), 3 to 5 short teaching slides and 2 check-together slides. Realistic working time is about 15 to 18 minutes, so about 2.5 minutes a question. L1, L3, L5, L9 and L10 will overrun unless parts are marked "if time" or moved to home.
- **Online problems.** L10 station rotation (four station cards, a physical 1 m 20 cm string, 7-minute rotations in breakout rooms) is not workable as written. Several lessons assume a printed workbook and physical manipulatives (right-angle checker, paper strips, digit cards). "In pairs" worksheet work online means breakout rooms with no tutor visibility, and this is not stated.

## 2. Summary table

| Lesson | Verdict | One-line reason |
|---|---|---|
| L1 Number Sleuths | minor fix | Content correct and in syllabus; Q5(b) and Q6 are stretch-level on the core page, and two long systematic lists make the page tight. |
| L2 Cryptarithm Crackers | minor fix | Correct and in syllabus; Q6 (shape sum) needs a two-case ones-column argument that is too hard for a core "on your own" question; Q1(b) borrows across zeros. |
| L3 Times Table Treasure | minor fix | Correct, good pattern work; Q2(a) asks for 7 tables to be tested, and the Q5 table has 7 slots but 17 row-counts to try. Earlier flagged item already fixed in P3. |
| L4 Model Makers | needs rework | Q5/Q6 and the Challenge/Think Harder items (before-after, "twice as much", ages, "3 times as old") are P4 to P5 level, well beyond "just beyond" for a P3 core page. |
| L5 Remainder Riddles | OK | Squarely in syllabus, correct, graded well; only a wording fix (boat trips) and one P5-style Challenge (excess and shortage). |
| L6 Fraction Walls | OK | In syllabus (unlike fractions to 12), correct; one ambiguous Challenge item (digits 1, 2, 3, 6) and a stray "coin lesson" reference. |
| L7 Area Architects | minor fix | Correct; Q4 L-shape area is a P4 skill (acceptable stretch); Q2 table has 5 rows for 4 gardens; one ambiguous cut wording in qbank. |
| L8 Angle and Line Detectives | minor fix | Correct; Q5 diagonal perpendicular lines (slope swap) go beyond the P3 grid skill; Challenge c6/c8 rely on angle-sum / turning arguments P3 children cannot make. |
| L9 Measure and Money Masters | needs rework | Five topics, 7 questions, 17 parts, decimal money, in 30 minutes; Q7(c) contradicts Q7(a); Challenge c8 (fast clock) is ambiguous. |
| L10 Challenge Day | minor fix | Content correct and well chosen; station rotation and string station do not work online; logic clue 2 is ambiguously worded. |

## 3. Difficulty and suitability by lesson

"Core" = workbook pages 1 and 2 plus qbank `core`. "Think Harder" = `stretch[0..3]` and the last 3 challenge items, which print in the workbook. "Challenge" = the Challenge slide items and the rest of the qbank.

| Lesson | (a) Topic vs P3 syllabus | (b) Core | Think Harder | Challenge | (c) Reading load | (e) 90 min timing |
|---|---|---|---|---|---|---|
| L1 | Within (numbers to 10 000, patterns) | Q1 to Q4 fine; Q5(b), Q6 stretch | Fine | Fine (c2 pages, c6 sum-4 list are long) | Light (252 words, no hard vocabulary) | Tight: 6 Q, 18 parts, two lists of 9 and 10 |
| L2 | Within (4-digit add/sub); cryptarithms are enrichment | Q1(b) and Q2(c) hard for weaker children; Q6 too hard | Fine | c7 and c8 very hard but fenced as Challenge | Light | OK |
| L3 | Within (tables 6 to 9); factor pairs and common multiples preview P4 | Q1 to Q4 fine; Q2(a) heavy | Fine | Fine | Light | Tight: two 10-entry tables, a grid, a 17-row list |
| L4 | Models within syllabus; "same difference", "times as old", before-after are P4 to P5 | Q1 to Q3 fine; Q4 to Q6 hard | s3, c6, c7 too hard | Slide Q1 and c7 beyond | Light | 3 teach slides plus 6 models: tight |
| L5 | Within (division with remainder, 3-digit by 1-digit) | Well graded | Fine | c5 (LCM) and c8 (excess/shortage) are P5 to P6 style but tutor-led | Light | OK |
| L6 | Within (equivalent, compare, add/subtract related; denominators to 12) | Fine; 7 questions | Fine | Fine | Light | Tight but short parts |
| L7 | Within (area and perimeter of rectangles, squares, rectilinear) | Q4 (composite area) is P4 but taught | Fine | c7 hard | Light; "perimeter", "rectangular" are known words | OK |
| L8 | Within (right angles, parallel, perpendicular); counting angles C(n,2) is enrichment | Q5(b)(c) diagonal lines too hard | s1 moderate | c6, c8 beyond | Light | OK; online needs printed sheet |
| L9 | Within (all five topics are syllabus), money division beyond | 17 parts; Q7 contradiction | Fine | c8 ambiguous | Heaviest (369 words, decimals) | Over: will not finish |
| L10 | Within (bar graphs with scales, logic, patterns) | Fine | c6 (liar puzzle) hard but fenced | Fine | Light | Explore too long online |

Reading and vocabulary: no lesson has a reading problem. The longest words are "perpendicular", "perimeter", "interchange", "remainder", "afternoon" and all are taught or familiar. Average sentence length is short.

## 4. Specific issues, ranked by severity

Severity: **High** = children will fail, stall or be misled; **Medium** = a visible problem for a meaningful share of children or for the tutor; **Low** = polish.

### High

1. **L4 (Model Makers): difficulty spike on the core page and Challenge items.**
   Files: `p3/content/l4.js` workbook Q5 and Q6; `qbank.challenge` c0, c3, c7 (c0 is the Challenge slide Q1; c6, c7, c8 are the printed Challenge items); `qbank.stretch` s3, s5.
   Problem: Q6 ("Grandma gives each boy the same amount; now Ali has twice as much") is a P5 same-difference problem, set as the last "on your own" question on core page 2. Q5 (give half the difference) is P4. Challenge c0 (before-after with 4 times as many) and c7 (two different spends, then 5 times as much) are PSLE-style. s3 ("when her mother is 3 times as old") is a P5 age problem. A P3 child who is secure on Q1 to Q4 will still stall here, and the lesson spends only three short teach slides on it.
   Fix:
   - Replace workbook Q6 with a P4-level idea, keep the "same difference" insight but not the "twice as much" step. Exact text: "Q6. Ali has $45. Ben has $18. Grandma gives each boy $10. (a) How much more money does Ali have than Ben now? ____ (b) How much more did Ali have than Ben before Grandma gave the money? ____ (c) What do you notice? Why?" Key: "(a) $27 (Ali $55, Ben $28) (b) $27 (c) The difference stays the same, because both boys got the same amount." Move the original "twice as much" problem to `qbank.stretch` as s5.
   - Replace the Challenge slide Q1 (c0) with: "Ali and Ben have 120 stickers altogether. Ali has 3 times as many as Ben. Ali gives 20 stickers to Ben. How many stickers does each boy have now?" Answer: "Ben 30, Ali 90 at first (4 units = 120); after giving: Ali 70, Ben 50." Use `chdiag` and `chwalk` to draw "before" and "after" bars.
   - Replace Challenge c7 (printed, last 3 items) with: "A pen costs $3 more than a ruler. Mei buys 2 pens and 2 rulers for $18. How much does one pen cost?" Answer: "$6. 2 pens and 2 rulers is 2 pairs, so one pen and one ruler cost $9. The pen is $3 more, so take away $3: $6 is 2 equal parts, a ruler costs $3 and a pen costs $6." Check: 2 × 6 + 2 × 3 = 18.
   - Demote s3 (age) to the end of the qbank, not `stretch[0..3]`. It is currently s3, so it prints in the workbook; swap it with s4 (rice and flour).

2. **L9 (Measure and Money Masters): overload, will not finish in 30 minutes.**
   Files: `p3/content/l9.js` workbook Q1 to Q7 (17 lettered parts); `lesson.explore`.
   Problem: five topics (length, mass, volume, money, time) in one lesson. The worksheet has 7 questions, mostly multi-step, with decimal money in Q4 and a timetable in Q7, plus teach slides `teachbudget`, `teach24`, `teachlist` and two check slides in the same 30-minute slot. The explore (party budget with six decimal prices, in breakout rooms) already uses 15 minutes.
   Fix: cut to 5 questions. Delete Q3 (ribbon; covered by Q1(d) and `qbank.core` c2) and merge its idea into Q1. Keep Q7 as (a) and (b) only; make (c) a Think Harder item. Result: about 12 parts. Mark Q4(b) "if time".

3. **L9 Q7: story contradiction between (a) and (c).**
   File: `p3/content/l9.js` Q7. In (a) Ravi reaches the interchange at 08:15. In (c) the "latest bus he can take" to reach school by 08:30 is the 07:55 bus (key), which has already left.
   Fix: replace (c) with exact text: "(c) On another day, Ravi must reach school by 08:30. Which is the latest bus he can take? ________". Key unchanged (07:55 bus, arrives 08:30).

4. **L10 (Challenge Day): station rotation is not workable online.**
   Files: `p3/content/l10.js` `lesson.explore`, `lesson.materials`, `lesson.online`; slide `p3l10-explore1`.
   Problem: "pick 2 of 4 stations, about 7 minutes each" in breakout pairs needs four station cards on screen, moves between rooms, and a physical "1 m 20 cm string" that children will not have. Transitions will consume the 15 minutes.
   Fix: run two stations only, as whole-group-then-pairs. Replace the Measure station with: "A 120 cm ribbon is cut into 3 pieces. Each piece is 10 cm longer than the one before. Draw it and find each piece." (answer 30, 40, 50 cm, unchanged). Change `materials` to remove the string and `online` to: "Two stations, 7 minutes each. Pairs stay in one breakout room, and the tutor shares the next station card when the timer ends. No physical materials beyond paper."

5. **L10 Q2: clue 2 is ambiguous.**
   File: `p3/content/l10.js` Q2. "Mei and Ravi went to watch their friend sing in the choir concert" requires an inference ("their friend" is someone else, so neither is in the choir) that a 9-year-old may not make, or may read as "one of them is the friend".
   Fix: "(Clue 2) Mei and Ravi are not in the choir." Update the key text ("Clue 2: Mei and Ravi are not in the choir") and `deck.mini2` is unaffected. Answer unchanged (Ali football, Mei chess, Ravi swimming, Siti choir).

6. **L8 Q5(b) and (c): perpendicular lines on a slope go beyond the P3 grid skill.**
   File: `p3/content/l8.js` workbook Q5. The P3 syllabus has drawing perpendicular and parallel lines on a square grid, normally along grid lines. Q5(b) needs "swap the steps and turn" (1 right 1 up becomes 1 right 1 down); Q5(c) needs the 2:1 slope turned to 1:2. The slide `teachgrid` does teach this, so (b) is acceptable as a stretch; (c) is not for a core "on your own" question.
   Fix: keep (a) and (b). Label (c) "Think harder (if you have time)" and add the hint "Check with your right-angle checker; try 1 right and 2 down." Alternatively move (c) to `qbank.stretch`.

### Medium

7. **L8 Challenge c6 and c8 use arguments children cannot make.**
   File: `p3/content/l8.js` `qbank.challenge` c6, c8 and slide `p3l8-chwalk`. c6 ("4-sided shape with 3 right angles: what is the 4th angle?") needs the angle sum of a quadrilateral. c8 and the chwalk slide use a "walk round the shape, 4 same-way turns" argument that is Secondary-level reasoning.
   Fix: c6 text: "A 4-sided shape has 3 right angles. Draw it. Test the 4th angle with your checker. Can a 5-sided shape have exactly 3 right angles? Draw one." Answer: "The 4th angle is a right angle too (it is a rectangle). Yes: cut one corner off a rectangle with one slanted cut." For c8, keep the question but change the answer line to: "No. The most is 5, for example an L shape. Children try to draw 6 square corners and always find a dent. A proof is not expected." Remove the turning argument from the `chwalk` slide's second half and replace it with "Try it: draw 6 square corners on grid paper. What do you always get?".

8. **L2 Q6 (shape puzzle) is too hard for the last "on your own" core question; Q1(b) borrows across zeros.**
   File: `p3/content/l2.js` Q6, Q1.
   Problem: ★● + ★● + ★● = ▲★●. The ones column needs "● + ● + ● ends in ●", which fits both 0 and 5, and ruling out 5 needs a parity argument in the tens column. Most P3 children will guess.
   Fix: add a scaffold to (b): "(b) The ones column: ● + ● + ● ends in ●. Which digits can ● be? Try 0 and 5, then check the tens column." Alternatively move Q6 to `qbank.challenge` and use `stretch` s4 (◆● + ● = ●◆) as Q6. Q1(b) (7□03 − □46□ = 2538) is a syllabus skill but hard for weaker children: add the existing check-by-adding instruction to the printed prompt: "Hint: turn it round and add: 2538 + □46□ = 7□03."

9. **L1 Q5(b) and Q6 are stretch-level on the core page; page 1 and 2 are long.**
   File: `p3/content/l1.js` workbook Q5(b), Q6 (18 lettered parts, two systematic lists of 9 and 10 numbers).
   Fix: mark Q5(b) and Q6 with a ★ and tell tutors in `ws2` that they are "if time"; the 1, 3, 6 pattern in Q6(b) is the point. Exact `deck.ws2` replacement: "Page 2, on your own: Q4 place value puzzles; Q5(a) what number am I?; then Q5(b) and Q6 (digits that add up to 3) if you have time."

10. **L3 Q2(a): testing seven tables is too heavy; L3 Q5 table does not match the work.**
    File: `p3/content/l3.js` workbook Q2(a), Q5.
    Problem: "Find ALL the other tables from 2 to 9 that also use all ten last digits" means 70 products. Q5(a) has a 7-column table, but a child must try every number of rows from 2 to 18, and 10 of the 17 do not work.
    Fix: Q2(a): "Test the 3, 6 and 9 times tables. Which of them also use all ten last digits? ______" (answer 3 and 9; 6 gives only even digits). Q5(a): add "Not every number of rows works. Write down only the ways that work, and stop when you have all of them." Key unchanged.

11. **L9 explore rules do not match the key.**
    File: `p3/content/l9.js` `lesson.explore`, `deck.expAsk`. "Buy enough punch" is read as one 2 ℓ bottle, but all three exact-$20 solutions need 2 or 3 bottles (I confirmed there are exactly three: pizza + 2 punch + 2 balloons; wings + 2 punch + 3 balloons; cupcakes + 3 punch + 2 balloons).
    Fix: "Buy at least 2 ℓ of punch (any number of bottles) and at least one food. You may buy more than one of an item." Then the "3 ways" claim is exactly right.

12. **L9 Challenge c8 (fast clock) is ambiguous.**
    File: `p3/content/l9.js` `qbank.challenge` c8. "A train leaves when this clock shows 13:05" could mean the train leaves at the real 13:05.
    Fix: "The clock at the station is 10 minutes fast. The train leaves when this clock shows 13:05. The trip takes 1 h 40 min. What is the real (correct) time when the train arrives? Give it in 24-hour and 12-hour time." Answer unchanged (14:35, 2:35 p.m.).

13. **Worksheet slot is 30 minutes in every lesson; plan for about 2.5 minutes a question.**
    Files: title notes of every `p3lN-title.html`. Lessons with the heaviest pages: L9 (17 parts), L1 (18), L5 (14), L10 (13), L7 (12 and a 5-row table).
    Fix: add one line to every title-slide time plan: "If the class is behind, children finish the last question of each page at home; the check slides cover it." And mark one "if time" question per page in the workbook (suggested: L1 Q6, L3 Q6, L5 Q6, L7 Q6, L9 Q7, L10 Q6).

14. **Online logistics are not stated for pair work and paper tools.**
    Files: `lesson.online` fields (L4, L5, L6, L8). Pair worksheets mean breakout rooms the tutor cannot see; L8 Q1 and Q5 need a printed sheet and a folded right-angle checker (a screen figure does not work); L6 needs seven cut 24 cm strips (prep burden on parents; folding thirds is hard for a 9-year-old).
    Fix: in each `online` field add: "Print the workbook before the lesson. Pairs work in one breakout room for 10 minutes, then return for the check slide." For L6 add: "Send the printed fraction strip page instead of asking children to measure and cut strips."

15. **L5 stretch s3: "How many trips must the boat make?" is ambiguous.**
    File: `p3/content/l5.js` `qbank.stretch` s3. A careful child will count the return trips.
    Fix: "A boat can carry 9 people at a time. 100 people want to cross the river. How many boatloads are needed?" Answer: "12 boatloads (100 ÷ 9 = 11 r 1; the last person needs a boatload too)."

16. **L6 Challenge c2 has more than two answers if improper fractions are allowed.**
    File: `p3/content/l6.js` `qbank.challenge` c2. With the digits 1, 2, 3, 6 there are also 2/1 = 6/3 and 3/1 = 6/2.
    Fix: "Use the digits 1, 2, 3 and 6, once each, to make two equal fractions that are each less than 1: ?/? = ?/?. Find both ways." Answer unchanged (1/2 = 3/6 and 1/3 = 2/6).

### Low

17. **L7 Q2 table has 5 blank rows but there are only 4 gardens.** `p3/content/l7.js` Q2. A child may hunt for a fifth. Add under the table: "You may not need all the rows." (Do not give the count; it spoils the "list ALL" skill.)

18. **L7 qbank c2 wording ("across the 6 cm sides" / "along the 6 cm sides") is easy to misread.** Replace the question with: "A rectangle 6 cm by 4 cm is cut into two rectangles with one straight cut that is parallel to one side. Find the total perimeter of the two pieces. Is there more than one answer?" and the answer with: "Yes, two answers. A cut parallel to the 4 cm sides is 4 cm long: 20 + 4 + 4 = 28 cm. A cut parallel to the 6 cm sides is 6 cm long: 20 + 6 + 6 = 32 cm."

19. **L8 qbank s6 compares 4 o'clock and 8 o'clock; at 8 o'clock the angle between the hands can be read as 240°.** Replace with: "Is the smaller angle between the clock hands at 4 o'clock the same size as at 8 o'clock?" Answer: "Yes, in both the hands are 4 hour-marks apart the short way round."

20. **L8 Q1 angle f (70°) is too close to a right angle to judge by eye**, but children use a checker, so the task works. For safety change `ANG` entry f from size 70 to 60 in `l8.js` (and keep the key: f is smaller). L8 s3 ("The # sign is made of 4 lines"): add "2 upright lines and 2 lines across".

21. **L10 stretch s6 snail: the key says "end of each day: 5, 8, 11, 14 m"; those are the highest points each day, not the end-of-day positions** (3, 6, 9 m after sliding). Replace with "highest point each day: 5, 8, 11, 14 m".

22. **Stray cross-level reference.** `split/p3l6/project/slides/p3l6-chwalk.html` notes say "as in the coin lesson"; there is no coin lesson in P3. Change to "as in the list-in-order puzzles earlier in the program".

23. **`p3/data.js` first-line comment says "p2/content/l1.js ... l10.js"**; it reads P3 content. Cosmetic.

24. **L7 Q4 (L-shape area) is a P4 skill.** Accept as a taught stretch (the `teach` slides cover "push the steps out" and subtraction). Leave as is, but keep it as the last question on page 2 so weaker children can stop.

25. **P4 bridge.** The brief says "leading into P4". Only L3 (factor pairs, common multiples) and L7 (L-shapes) clearly preview P4. Optional: add one sentence to each lesson's closing slide naming the P4 topic it leads to (L1 5-digit numbers, L5 factors and multiples, L6 mixed numbers, L8 angles in degrees, L9 decimals). No content change needed.

## 5. What was checked and found correct (spot list)

- L1: all key answers and qbank items (digit-card greatest/smallest/odd/closest, 9 numbers from 2, 0, 5, 5, digit-sum 3 gives 10 numbers, digit-sum 4 gives 20, 252 page digits, 6842 unique, 9810/3012, 10th number 2341).
- L2: 168 digit-card sums, each with exactly one carry and digit sum 18; magic square (total 4500, unique); both pyramids; shape puzzles (★=5, ●=0, ▲=1; 89 + 9 = 98; 99 + 22 = 121; 736 − 63 = 673; 11 + 99 + 88 = 198; 459 + 495 = 954); minimum differences 47 (cards 1 to 6) and 247 (cards 1 to 8); Q1 figure boxes unique.
- L3: grid puzzle has one solution (rows 7, 9, 6; columns 8, 6, 9); factor pairs of 36 (7 ways); 24, 48, 72, 96; last-digit counts (4 in 6 × 1 to 6 × 20, 63 and 133 in the 7s); 126; last digit of 7 to the 8th is 1.
- L4: all model answers (Q1 to Q6, and the stretch and challenge items).
- L5: all remainder riddles (53; 11, 23, 35, 47; 63; 5 tables and 35 children; 62; 36 and 48; 73; 3 and 9; 301; 7 to 35; Wednesday; 7 pupils and 38 pens).
- L6: wall equivalents, comparisons, Q3 shaded fractions (viewed: A, B, D are 1/4; C is 2/6; E is 3/8), Q6 pairs, Q7 (7/12 and 8/12), 2 ways for 5 pieces (confirmed by brute force).
- L7: all areas and perimeters (figures viewed); polyomino perimeters (5 squares: 10 or 12 edges; 6 squares: 10 only for 2 × 3, up to 14; 7 squares: 12 to 16).
- L8: right-angle counts (plus 8, staircase 6, house 3, trapezoid 2, window 16, U shape 6, 36 and 24 in the grids); C(n,2) angle counts; letter pairs.
- L9: all conversions, budgets (best three items $19.35), clock arithmetic, timetable (06:40, 07:05, 07:30, 07:55, 08:20, 08:45), and the three exact-$20 party plans.
- L10: bar graph (Lime = 50), logic grid unique, queue counts, sticks (3n + 1), digit riddle (213, 321, 411), liar puzzle (Mei), 14 squares, 15 handshakes.
- Slide text: no wrong arithmetic found in any `we`, `try`, `teach`, `ws*ans`, `stretch`, `challenge` or `chwalk` slide.

Not checked: the rendered look of slide diagrams (`chdiag`, `expPic`), the tutor guide PDF, the weekly PDFs, and the visual layout of Think Harder pages beyond L2.
