# Level 3 pre-flight (lessons 1 to 40, ages 8 to 10, Primary 3)

Status: planning only, written 23 Oct 2026. No lesson, tool, template or output file was edited, and no shared file was touched. Level 1 (`term/l1/`: lessons 1 to 30 built, 31 to 40 in progress) is the model; no Level 3 lesson is written. This document tells the people who will write the 40 Level 3 term lessons what each lesson is, what the templates must learn first, what went wrong at Level 1 and must not be repeated, which decisions the owner must make, and in which order to build. Every default is marked **[Default]**.

Sources read in full: `docs/terms/owner_decisions.md` (all entries), `docs/terms/l1_term2_preflight.md`, `docs/terms/l1_term3_term4_preflight.md`, `docs/terms/level_3_year_plan.md` (all of it, including its non-routine section and matrix), `docs/books/p3_school_paper_patterns.md`, `docs/books/p3_non_routine_catalogue.md`, `docs/moe/syllabus_by_level.md` (P1 to P6 and the year index), `docs/sasmo/g3_analysis.md` and `g3_original_problems_draft.md`, `term/l1/AUTHORING.md`, `WORDING_GUIDE.md`, `audit/TERM_WIDE_AUDIT.md`, `audit/CUTOUT_AUDIT.md`, `audit/FINAL_AUDIT_T1.md`, `audit/FINAL_AUDIT_T2.md`, the holiday Level 3 content `p3/content/l1.js` to `l10.js` (every question bank), `docs/printing/README_bw.md`, and the Level 1 tool inventory (`term/l1/tools/figs2.py`, `figs3.py`, `svg.py` signatures, `b_quest.py` bans, the Level 1 Lesson 30 data file for the Quest and `beyond` fields). The word-problem analyses (`word_problems_g1_g2_*`) cover Grades 1 and 2 only and were not used.

Numbers quoted as "verified" were recomputed by brute force in `verify_l3_preflight.py` (appendix): **178 checks, all passed**. Lesson authors must still write their own `verify/lNN_checks.py`; nothing here replaces it. Check ids (`V7.5` and so on) point to the appendix.

## 0. Headline findings

1. **The Level 3 year plan's "Non-routine assignments" section is Level 5 text.** `docs/terms/level_3_year_plan.md` lines 274 to 395 (commit 853d14b) list lessons called "Shifting Places", "Factor Finders", "Tank Tales", "Percent Sense", cite `p5_non_routine_catalogue.md`, "2279 questions in 166 Primary 5 papers", GST at 9 percent, ratio and average previews, and a table of 40 lessons that do not exist at Level 3 (the Level 3 titles are Number Lines to 10 000, Write It Down, Check It, and so on). The Primary 3 files `p3_non_routine_catalogue.md` and `p3_school_paper_patterns.md` are correct and were committed beside it. **Do not use the plan's section.** Section 4 of this document rebuilds the per-lesson assignments from the P3 catalogue (1098 questions, 16 types) and gives the matrix. The plan section should be replaced by it (an edit to a shared file, left to the owner; question D1).
2. **"No holiday reuse" is true by title and false by item.** The holiday course is the same strands (H1 Number Sleuths to H10 Puzzle Day), and its question banks already hold the plan's contest items: handshakes among 6 children and squares in a 3 by 3 grid (H10), numbering pages 1 to 120 (H1; the plan's lesson 34 says pages 1 to 130), the day of the week 100 days later and the 50th shape in a cycle (H5; lesson 32), ages in n years and the pencil-box-and-pens pair (H4; lessons 24, 25), pouring 300 ml and 500 ml cups to get 100 ml (H9; lesson 28), 24-hour clock durations and a station clock 10 minutes fast (H9; lessons 9, 35), area and perimeter in full (H7; lessons 13, 14), perpendicular and parallel lines (H8; lessons 15, 23). Section 3 is a lesson-by-lesson register of the closest holiday items, what each term lesson is barred from reusing, and what is new. Owner decision D2.
3. **Four plan items are near-copies of SASMO problems** and are replaced here: "matchstick digits with exactly 17 sticks" (lesson 37; SASMO 2020 Q23), "the 31st number using only odd digits" (lesson 34; Q10), counting multiples between a start and 100 with a 6s table (lesson 32; Q5) and a Y of circles with equal line sums (lesson 26; Q24). Same ideas, new contexts and numbers (V26.1, V34.1, V37.1).
4. **The Quest lessons are also content lessons.** Lessons 10, 20, 30, 40 carry a 20-minute Mi's Challenge Quest after the break. Level 3's lesson 10 (Price per Piece) and lessons 20, 30, 40 (Class Shop, Playground Plan, Mathematicians' Fair) have only about 19 minutes of Explore and Mini-lesson each. Lesson 10 introduces an idea (unit price) and must be light; lessons 20, 30, 40 are reviews and projects and cost nothing in new content. The plan's old "last 25 minutes" check (plan lines 107, 166, 234) is superseded.
5. **Level 1's tools cover about half of Level 3's figures.** Checked in `figs2.py`, `figs3.py` and `svg.py`: `number_line`, `bar_model`, `table`, `clock`, `money`, `price_tag`, `calendar`, `stick_pattern`, `grid`, `cube_stack`, `fold_punch`, `panel`, `network`, `picture_graph`, `objects`, `array`, `groups`, `seq`, `hundred` and `ruler` exist and serve nine lessons outright (section 5.1) and part of many others. Eighteen items do not exist and block the rest (section 5): vertical column layouts for add, subtract, multiply and short division, place-value counters, an area model, fractions on a strip and line, scale dials and jugs, a balance, a true bar graph, composite grid figures, equal-gap posts, line and angle figures, mirror images, magic-circle figures. Estimated 85 hours of figure work, 20 of kit builders, 19 of runner work and 26 of term tools, 150 in all (about 133 with deferrals; section 5.6).
6. **Printed workbooks are black and white; the books print every page at 94.3 percent.** Level 3 depends on colour more than Level 1 does (picture patterns, graphs, shaded fractions, mirror images, balance objects). Every figure must carry its meaning in shape, label or fill pattern; colour is decoration for the soft copy. Anything measured against a real ruler or set square (lessons 11, 13, 15) must not rely on printed scale: the Level 1 audit found a "real size" claim false in the book (CUTOUT_AUDIT F4, FINAL_AUDIT_T1 finding 10).
7. **Seven lessons have no (or only partial) school-paper evidence** (patterns section 6, item 11): 19 Cube Stacks and Views, 21 Fold, Flip, Mirror, 22 Picture Patterns (the grid half; growing pictures are set), 23 Turns and Corners, 26 Magic Totals, 34 Counting Digits and Pages, 36 Target Practice. They stay as the plan says, labelled beyond school; lesson 23 is the weakest (the plan's own "no degrees" rule leaves little to measure) and has an owner-swap option (D4). Lessons 21, 31 and 36 are P4 or P5 topics (symmetry, factors, brackets): their Start here must stay pre-formal.
8. **Level 1's recurring defects are known and must be designed out from lesson 1:** kit pieces that do not match the tasks, false "next lesson" materials lines, workbook numbers repeated from class, answers on the slide while the question is asked, paper hold-ups to the camera, family pages that print the global lesson number, a validator that fails on our own catalogue text. Sections 6, 7 and 10 turn each into a rule with a check.
9. **Cutting load is about 270 pieces a year** (T1 45, T2 55, T3 71, T4 about 100; section 6). The Level 1 audit objected to 203 in one term. Term 4's load can drop to about 84 by making the lesson 36 operator tiles optional.
10. **The 2019 P3 papers were read from the owner's 100 dpi OCR and about 16 of 39 scans were not read**; no picture was seen in any paper. Wording for pictures, clock hands, graph layouts and coin images is inferred. Every item whose form rests on a figure is marked "wording unverified" until the owner supplies the picture (question D19).
11. **Estimate:** about 340 agent-hours for the 40 lessons (write, wording review, independent audit, fix pass, term-wide audits) and 133 to 150 hours of template engineering, so roughly 475 to 490 hours; at the Level 1 pace (eight to ten writers, three engineers) about 8 to 10 working days from Sprint A to an audited Term 4 (section 13). Hours are estimates from Level 1 documents, not measurements.

## 0.1 Assumptions made (change them if wrong)

- **Format.** 40 lessons of 90 minutes (owner decision of 23 Oct, "then work with 90mins"), groups of up to 8, online. Files are `term/l3/lessons/l01.json` to `l40.json`; `level` 3, `term` 1 to 4, `lesson` 1 to 40, `lesson_in_term` 1 to 10, `id` `l3-t1-01` ... `l3-t4-40`, practice keys `l3t1l01` ... `l3t4l40` (the level prefix is new because the shared runner already holds `t1l01` for Level 1). Family pages print "Level 3 Term 2 Lesson 4", never "Lesson 14 of 10". The leak check allows "Lesson 1" only where `lesson_in_term` is 1.
- **The 11-part skeleton as built at Level 1:** Opening 2, Remember 6, Sneak-peek 4, Explore 16, Mini-lesson 10, Break 4, Workbook 28, Talk 6, Exit 6, Look-back 3, Flex 5 (Opening may be 4 with Explore 14). Quest lessons (10, 20, 30, 40): Opening 2, Remember 6, Sneak-peek 4, Explore 10, Mini-lesson 9, Break 4, **Quest 20 at minutes 35 to 55**, Workbook 25, Talk 4, Look-back 2, Flex 4 = 90; the exit ticket is not live.
- **Tiers.** Start here 6 questions (workbook pages 1 and 2, at most 20 modelled minutes for a middle child), Think harder 4 (page 3), Go further exactly 3 (page 4), one Investigation (page 5) with an easy first step, kit page 6. Start here is a Primary 3 skill with scaffolding; Think harder carries the taught idea in a new setting **and every contest-style item**; Go further is extension. No non-routine item at Start here (owner rule of 23 Oct). Labels are neutral and never shown as ranks.
- **Named beyond-syllabus item in every lesson** (owner rule, 23 Oct): one named puzzle at Think harder or Go further, never Start here, original, with a tutor-only `beyond` field `{name, where, text, parent}` and a one-line level note (for example "Primary 4 idea"). It takes one of the Think harder or Go further slots; it is not an extra question.
- **Mi's Challenge Quest** in lessons 10, 20, 30, 40 (owner decisions of 22 Oct): a game, no scores, marks, ranking or visible timer, no word "test" or "exam" on any child or parent page (`BAN_FAMILY` in `b_quest.py`), private paper, the tutor keeps private notes for one line per parent, photos returned by the parent to the business WhatsApp (+65 9880 5962, never on slides). Eight gates and one optional cave (section 8).
- **Books.** Printed black-and-white 5-lesson books issued on payment: Book k holds lessons 5k-4 to 5k (eight books). The Quest Log (3 pages) sits in Books 2, 4, 6, 8. Kit pages are on a front page with a blank back; soft copies stay colour. [Default] both books of a term are issued with the first payment (D11 at Level 1).
- **Wording** follows `WORDING_GUIDE.md` with the Primary 3 changes in section 1.1: options numbered (1) to (4), an "Ans:" frame with the unit after the line, 24-hour times as 14 30, money as $3.20 and 1850¢, "true, false or not possible to tell" tick tables, no hint naming the tool at Think harder unless the type is new, no marks printed on child pages.
- **Cast.** Mei, Ali, Ben, Siti, Ravi, Kumar, Aisha, Wei, Jenny, Lily, Jamie, Ray, Amelia, Jason, plus Zoe, Kai, Maya, Talib, Yongli, Dev, Cara. Wrong working is attributed to "a child" or "a child in another class", never to a cast name (Level 1 audit).
- **Calculators.** None in any lesson; Mi never shows one (the P3 papers allowed one once, Raffles 2024 WA1).
- **Scissors.** [Default] a grown-up, or the child with a grown-up, cuts the kit before the lesson; nobody cuts during a lesson (Level 1 rule, relaxed only for older children; D5).
- **Ruler, set square, string.** [Default] a 30 cm ruler is listed from lesson 11 on (every Primary 3 child has one); the book supplies a cut-out right-angle checker (lesson 15) so a set square is not required; measuring tasks are written so that scale of the printed page does not matter (section 11, risk 5).

## 1. Lesson specs

### 1.0 Field order, holiday codes and the named beyond item

Every spec uses this order: big idea, strand and page references with the **holiday boundary**, objective, prerequisites, Remember warm-up (three items, re-taught with objects or pictures), Start here / Think harder / Go further outline with question counts, the **Beyond (named)** puzzle, non-routine work (type, tier, check id), number ranges, home materials, kit with piece counts, figures, misconceptions, template needs (codes from sections 5 and 6). "Beyond P3" labels follow `docs/moe/syllabus_by_level.md` (page numbers are PDF pages).

Holiday codes used throughout: H1 Number Sleuths, H2 Cryptarithm Crackers, H3 Times Table Treasure, H4 Model Makers, H5 Remainder Riddles, H6 Fraction Walls, H7 Area Architects, H8 Angle and Line Detectives, H9 Measure and Money Masters, H10 Puzzle Day. Holiday graduates start Term 1 (owner decision 4), so a graduate must not meet an item from `p3/content/lN.js` again; the Remember warm-up may revisit a holiday topic once (owner rule: spiral in warm-ups only).

Check ids `Vn.k` are in the appendix. Examples are original: the numbers differ from the catalogue examples and from the drafts. The owner's private file of school questions (`docs/books/private_p3_papers/`) was not copied from.

### 1.1 Level 3 wording deltas from the Level 1 guide (from `p3_school_paper_patterns.md` section 7)

Rules 1 to 25 of `WORDING_GUIDE.md` still apply; the Primary 1 rule 25 (tests numbers to 40, "say why" is enrichment) is replaced by: the papers test numbers to 9999, two- and three-step stories, "true, false or not possible to tell" and a few reasons; explain-why prompts stay out of Start here and the exit ticket. Changes: (a) children read their own questions: the tutor reads a stem aloud only for Think harder items, not for every Start here item; (b) section instructions in paper style ("Show your working clearly." "Write your answers in the units stated."); (c) options (1) to (4) with a bracket at the right, never A to D; (d) "Ans:" with the unit after the line, and a "Working" box on two-step items; (e) fixed words: "Find the sum of", "Find the difference between", "Find the product of", "What is the quotient and remainder when", "Arrange the numbers in order. Begin with the smallest.", "more than", "fewer than", "times as many", "How many more", "altogether"; (f) time written 3:15 pm (accept 3.15 p.m.) and 24-hour 14 30 (accept 1430); (g) money $3.20 and 1850¢, "gave the cashier", "How much change did he receive?"; (h) units km, m, cm, kg, g, L or l, ml; (i) the tick table: "Each statement below is either true, false or not possible to tell. Put a tick in the correct column."; (j) "All diagrams are not drawn to scale." on figure pages (this is also the honest answer to the 94.3 percent print scale); (k) no stem names its tool at Start here; a Think harder stem may say "Draw a model" for a type new to that term (the papers almost never do).

### 1.2 Term 1: Number, calculation and everyday tools (lessons 1 to 10)

Can a new child join cold? Yes: the warm-up covers Primary 2 recall (place value to 1000, tables 2, 3, 4, 5 and 10, two-digit add and subtract, halves and quarters, time to the minute). Holiday graduates meet the holiday topics only in the first six minutes (digit-clue place value 1, missing digits 2, tables 6 to 9 3, remainders 5, bar models 4, fraction walls 6, area 7, angles 8, units 9, logic 10). Entry check: see D15. Chains: 1 feeds 2 and 34; 2, 3 and 4 feed 6, 10 and 32; 8 and 10 are a pair; 7 feeds 27. **Safest to skip or make up (recording, or holiday class): lesson 5**; hardest to miss: 2, 3, 4, 6. Lesson 10 hosts the Quest and cannot be skipped lightly (the make-up route is the Quest at the make-up slot).

#### Lesson 1. Number Lines to 10 000

- **Big idea.** Every number has a place on a line, and the line shows what is near it.
- **Strand.** MOE P3 Whole Numbers: numbers to 10 000, count in hundreds and thousands, place value, compare, patterns (1.1, p. 35). Contest tag: bounds and midpoints. **Holiday boundary (H1):** H1 built numbers from digit cards, listed numbers in order and solved digit-clue riddles. Lesson 1 sets none of: greatest or smallest number from cards, "I am a 4-digit number" digit-sum riddles, counting a digit from 1 to 100. Digit cards return in lesson 34.
- **Objective.** Read and place numbers on marked and unmarked lines to 10 000; count on and back in 10s, 100s and 1000s; compare and order with a line; move between numerals and words. Think harder: the number halfway between two numbers; a riddle on a line. Go further: alternating steps; counting numbers between bounds.
- **Prerequisites.** Primary 2: place value to 1000, counting in tens and hundreds.
- **Remember (6 min).** (1) Count on in 100s from 2300 to 2800 along a printed line, one clap per step. (2) Read 706 and 760 in words and say which is greater (P2 recall). (3) Spiral from H1: the value of the 7 in 4721 on a Th H T O chart.
- **Start here (6).** (1) Read the number an arrow points to on a line marked every 100 (3000 to 4000). (2) Mark 3450 on a line marked every 100: it sits halfway between two marks. (3) Count on 4 steps of 100 from 4250 and back 3 steps of 1000 from 7300. (4) "1000 more than 5003", "3 tens more than 3090" (the paper forms). (5) Put four numbers in order on a line (new numbers, for example 6035, 6305, 6053, 6350). (6) "Write six thousand and forty in numerals" and the reverse.
- **Think harder (4).** (1) Read an arrow on an unmarked line with equal intervals not starting at 0 (marks 3600 and 3800, the arrow after three equal gaps). (2) The number halfway between two numbers: 1250 and 2750, then 3490 and 3610 (V1.1). (3) A riddle: "I am between 6400 and 6700. My tens and ones digits are both 0. My hundreds digit is even. What number am I?" (6600, the only one, V1.4). (4) True, false or not possible to tell about points on a line (for example "Point A is halfway between 2000 and 3000, so A is 2500"; V1.6).
- **Go further (3).** G1 **Beyond (named): "Halfway House".** A number halfway between two numbers that are not on the marked ticks, and why the answer is "add both and halve". Level note: midpoints and rounding to the nearest hundred are Primary 4 (1.5, p. 37); the lesson says "halfway" and never "round". G2 Alternating steps: 3200, 4200, 4000, 5000, ... (add 1000, take away 200, repeat): the 9th number is 6400 (V1.3). G3 How many numbers between 3900 and 4100 end in 5? (20, V1.2).
- **Non-routine.** LOG T (riddle, V1.4), EXP T (true, false or not possible to tell), PAT G (V1.3). The catalogue's LIST T for lesson 1 (digit cards, EX-LIST-1) is moved to lesson 34 because it is H1's core.
- **Numbers.** 0 to 10 000; steps 10, 20, 50, 100, 200, 500, 1000; "1000 less than" and "3 tens more than" forms (V1.5).
- **Home materials.** Pencil, 30 cm ruler (optional), a strip of paper.
- **Kit (KT1 `line_kit`, one page, 14 pieces to cut).** 2 line strips (18 cm, 10 equal intervals, tick marks only) and 12 number cards (28 x 19 mm, with 6 and 9 underlined where they occur). Contract: Explore places 8 cards on 1 strip; the Mini-lesson uses 2 strips (a marked and an unmarked one); supplied 12 and 2, maximum used 8 and 2. Alternative with no printer: draw a line on a long strip of paper and write the numbers on scraps.
- **Figures.** `number_line` (exists; needs a pointer at a position between ticks, ticks with no labels and an axis break for a non-zero start, X5), place-value chart (X2).
- **Misconceptions.** Reading a mark by counting marks instead of by the interval size; taking the middle of 2640 and 2680 as 2500; "four hundred and five" written 4005 or 405 either way; "between" including the ends; assuming a drawn line is evenly spaced when its marks are not.
- **Needs.** X5, X2, KT1, RN1 (number and word answers).

#### Lesson 2. Write It Down, Check It

- **Big idea.** A written method is a tidy record of what the numbers did, and a second look finds the slip.
- **Strand.** MOE P3 Whole Numbers: add and subtract with algorithms to 4 digits (p. 35). Contest tag: undo and error analysis. **Holiday boundary (H2):** H2 was missing-digit sums, letter puzzles, pyramids and magic squares. Barred here: letter puzzles (AB + B = BA), pyramids, magic squares, "7A03 - B46C". The missing-digit work is kept to one Think harder item and one Go further item with boxes (not letters).
- **Objective.** Add and subtract numbers to 4 digits, regroup across zeros, estimate to check, and explain a mistake. Think harder: spot a wrong worked answer; find the unknown in "a number plus 2583 is 6479". Go further: which mistake gives a stated wrong answer.
- **Prerequisites.** Place value to 10 000 (lesson 1 as a warm-up, not a requirement).
- **Remember (6 min).** (1) Regroup 1 thousand as 10 hundreds with place-value counters drawn on the chart. (2) Two-digit add and subtract with a carry (Primary 2). (3) Spiral from H2: check a subtraction by adding.
- **Start here (6).** (1) 4682 + 2739 in a column, with an estimate (about 4700 + 2700 = 7400, answer 7421, V2.1). (2) 9000 - 5826 with the zeros regrouped (3174). (3) A two-step story with a column for each step. (4) The same sum done twice, the second time by adding back. (5) "A number plus 2583 is 6479" (3896, V2.2). (6) A story with a decision: which two of four prices make a total.
- **Think harder (4).** (1) A child works 5000 - 2467 and gets 2533; find the step where a different child went wrong to get 3467 (V2.3). (2) A column with a wrong carry: circle the digit that is wrong. (3) A subtraction with two missing digits in different numbers: 4 [] 76 - 28 [] 4 = 1792 (the digits are 6 and 8, unique, V2.4); one item only. (4) True, false or not possible to tell: "estimating can show that 7421 is too big for 4700 + 2700" and similar.
- **Go further (3).** G1 **Beyond (named): "Wrong on Purpose".** Find the mistake rule that gives a given wrong answer: take the smaller digit from the larger in every column gives 3467 for 5000 - 2467 (V2.3). Level note: error analysis is a process skill (pp. 13 to 14), not an outcome. G2 Write a subtraction with a missing digit and a partner's rewrite as an addition. G3 Two stories where the same two numbers need different operations.
- **Non-routine.** BACK T (V2.2), EXP T (mistake), LOG G (missing digits, one item).
- **Numbers.** Sums to 9999, differences from 9000, 8000 and 5000; no letters.
- **Home materials.** Pencil, squared paper (the book has column paper).
- **Kit.** No cut kit. A printed place-value mat and column paper (not cut).
- **Figures.** `column` add and subtract with carry and borrow marks, boxes and a circled digit (X1), place-value counters (X2).
- **Misconceptions.** Subtracting the smaller digit from the larger in each column; forgetting that regrouping across a 0 borrows twice; carrying into the wrong column; an estimate that rounds both numbers down; writing the answer's digits in the wrong columns.
- **Needs.** X1, X2, RN1.

#### Lesson 3. Multiply by Splitting

- **Big idea.** A hard product is two easy ones added.
- **Strand.** MOE P3 tables of 6 to 9 and multiply 2- and 3-digit numbers by 1 digit (3.4, p. 35). **Holiday boundary (H3):** H3 was the 6, 7, 8, 9 tables (patterns, last digits, 9 x 7 as 10 x 7 - 7, the digit-sum of the 9s) and the 6s and 9s counted to 200. The term lesson treats the tables as known (warm-up) and starts at the area model for two- and three-digit numbers. Barred: last-digit patterns, digit sums of the 9s table, "numbers divisible by both 6 and 9 up to 200", 7 x 9 style comparisons.
- **Objective.** Split a number into tens and ones (and hundreds), multiply the parts and add (area model), connect it to the column method, multiply 3-digit numbers by 1 digit. Think harder: a two-step story; a table of equal groups. Go further: digits that must fit a product.
- **Prerequisites.** Tables to 9 x 9; place value to 1000.
- **Remember (6 min).** (1) Six facts from the 6, 7, 8, 9 tables by splitting (7 x 6 = 5 x 6 + 2 x 6). (2) "7 hundreds x 3". (3) Spiral from H3: 9 x 7 = 70 - 7.
- **Start here (6).** (1) 36 x 4 by an area model: 30 x 4 + 6 x 4 = 144 (V3.4). (2) "Ravi has 7 stickers; Ali has 3 times as many": 21 (the Start here exposure to times as many; V3.4). (3) "Has the same value as 4 groups of 7" (28, V3.5). (4) 14 x 6 and 23 x 5 in a column. (5) "7 hundreds x 3". (6) A story: 8 boxes of 24 pencils.
- **Think harder (4).** (1) 327 x 6 as 1800 + 120 + 42 = 1962 and in a column (V3.1). (2) A two-step story: 9 boxes of 120 pens, 285 sold, the rest packed equally into 5 packs: 159 in each (V3.2). (3) A table: a tricycle has 3 wheels, make a table for 1 to 5 tricycles and find how many have 45 wheels (15, V3.5). (4) True or false: 6 x 48 = 6 x 50 - 6 x 2 (true, V3.5). Also "times as many with a difference": 6 cards and 5 times as many, how many more (24, V3.4).
- **Go further (3).** G1 **Beyond (named): "Product Detective".** Digits missing in a multiplication: 3 [] 7 x 6 = 1 [] 02 (the digits are 1 and 9, unique, V3.3). Level note: reasoning from the last digit upward is contest-style; the multiplication is Primary 3. G2 Which tables can 6 x 48 be split into, and how many ways. G3 Pose a story for 4 x 125.
- **Non-routine.** MULTI T (V3.2), TAB T, EXP T, CMP T (times as many with a difference).
- **Numbers.** 2-digit x 1-digit; 3-digit x 1-digit with products to 6000; hundreds times a digit.
- **Home materials.** Pencil, squared paper.
- **Kit.** None cut (area-model grid is a printed page).
- **Figures.** `area_model` (X3), `column` multiply (X1), `table` (exists).
- **Misconceptions.** Forgetting a partial product; place value in a partial product (20 x 6 as 12); "times as many" read as "more".
- **Needs.** X3, X1.

#### Lesson 4. Divide It Up

- **Big idea.** Dividing is sharing out the biggest pieces first, and the remainder decides what to do next.
- **Strand.** MOE P3 division with remainder, algorithm up to 3 digits by 1 digit (3.3, 3.4, p. 35). **Holiday boundary (H5):** H5 was remainders in stories, riddles and two-divisor remainder riddles (a number from 20 to 30 with remainder 3 when divided by 4 and 5 when divided by 6). The term lesson is the short division algorithm with 3-digit dividends, rounding up and the quotient-and-remainder check. Barred: remainder riddles with two divisors, "biggest 2-digit number leaving remainder 8", the 50th shape in a cycle, and H5's own stories (35 counters among 4, 58 sweets into bags of 7, 45 stickers among 6, a ribbon of 50 cm in pieces of 6 cm). Round-up ('how many buses') is a stock school item (about 35 in the papers) and H5 set it once with 100 people in boats of 9, so it returns here with 3-digit numbers and a different frame.
- **Objective.** Divide 2- and 3-digit numbers by 1 digit with a remainder; check by multiplying back and adding the remainder; decide whether a remainder means one more box. Think harder: least number of boxes; true, false or not possible to tell. Go further: smallest and biggest numbers with a given remainder.
- **Prerequisites.** Tables to 9; lesson 3 (multiplication).
- **Remember (6 min).** (1) Share 12 tens among 3 with counters. (2) 9 x 6 + 4 = 58 and back to 58 divided by 9. (3) Spiral from H5: put 25 counters into groups of 4.
- **Start here (6).** (1) 84 / 4 and 156 / 3 by sharing tens and ones (21 and 52, V4.6). (2) 487 / 6 as a short division, 81 remainder 1 (V4.1). (3) Check 487 by 81 x 6 + 1. (4) A story with a remainder ("62 pencils into boxes of 8"; not H5's 58 into 7). (5) 803 / 4 = 200 remainder 3 (V4.6). (6) A story where the remainder is ignored.
- **Think harder (4).** (1) Least number of boxes: 253 pupils, 8 to a bus (32 buses, V4.2). (2) True, false or not possible to tell: "Ali has 54 stickers: he can put them in bags of 6 with none left (true), of 4 (false), of 9 (true)" (V4.3). (3) A number divided by 7 gives 12 remainder 5: what number? (89, V4.4). (4) A story with a hidden extra step (the sharer).
- **Go further (3).** G1 **Beyond (named): "Smallest and Biggest".** The smallest and the biggest 3-digit number that leaves remainder 5 when divided by 9 (104 and 995, V4.5). Level note: bounds on a remainder condition are contest-style (the remainder is Primary 3). G2 A story where the answer is "one fewer than the number of boxes". G3 Pose a story with quotient 12 and remainder 5.
- **Non-routine.** GC T (V4.2), EXP T (V4.3), BACK T (V4.4), LOG G (V4.5).
- **Numbers.** Dividends to 999 (stories to 1250); divisors 2 to 9.
- **Home materials.** Pencil; 30 small things for the Explore.
- **Kit.** None cut.
- **Figures.** `column` short division (X1), place-value counters (X2).
- **Misconceptions.** Remainder larger than the divisor; dropping a zero in the quotient (803 / 4 giving 20); rounding down when boxes are needed; writing the remainder as a decimal.
- **Needs.** X1, X2, X18 (tick table), RN2 (quotient-and-remainder frame).

#### Lesson 5. Mental Maths Moves

- **Big idea.** Numbers can be bent to make easy sums, and a long list can be paired.
- **Strand.** MOE P3 mental calculation of two 2-digit numbers (p. 35); pairing and the total of a stepping list are NOT IN (contest tag: SASMO 19-1, 20-1, 20-16). **Holiday boundary (H2):** H2 stretch had one compensation item (add 1099, not 1999); this lesson makes it the core.
- **Objective.** Make tens and hundreds, compensate (38 + 25 = 40 + 23), pair numbers in a long sum, and add a stepping list by pairing first and last. Think harder: pairs to 1000; a balanced equation. Go further: count the terms first.
- **Prerequisites.** Two-digit addition.
- **Remember (6 min).** (1) Pairs to 100. (2) 38 + 25 by 40 + 23. (3) Spiral from H2: 1999 + 4 by 2000 + 3.
- **Start here (6).** (1) Pairs to 100 (64 and 36, V5.7). (2) 38 + 25 and 47 + 36 by compensating. (3) 76 + 28 + 24 + 12 + 88 + 72 by finding pairs to 100 (300, V5.1). (4) 98 + 47. (5) Subtract by compensating: 83 - 29. (6) Which route is quickest, circle it.
- **Think harder (4).** (1) Pairs to 1000 in a list of five (275 + 725 and 640 + 360, V5.5). (2) Fill the box: 300 + [] = 48 x 9 (132, V5.3). (3) 250 + 138 = 238 + [] without adding both sides (150, V5.4). (4) The total of 11, 14, 17, ..., 41: 11 numbers, 286 (V5.2).
- **Go further (3).** G1 **Beyond (named): "Pair It Up".** Add 105, 112, 119, ..., 175: first count the terms (11), then pair first and last (1540, V5.6). Level note: summing a stepping list is NOT IN; no formula is named. G2 A list whose first number is not the smallest. G3 A short explanation of why pairing works.
- **Non-routine.** LIST T (V5.5), EQ T (V5.4), PAT G (V5.2, V5.6).
- **Numbers.** Sums to 1000 in pairs; lists of at most 12 terms.
- **Home materials.** Pencil.
- **Kit (KT2 `pair_cards`, 12 cards to cut).** 12 number cards that form six pairs summing to 100 (for example 24 and 76, 35 and 65, 18 and 82, 47 and 53, 29 and 71, 13 and 87). Contract: the Explore sorts all 12; supplied 12, maximum used 12.
- **Figures.** `seq` and `number_line` jumps (exist).
- **Misconceptions.** Compensating in the wrong direction; pairing numbers that do not sum to a round number; counting the terms of a list wrongly by one; thinking 1 + 2 + ... works without pairing.
- **Needs.** KT2.

#### Lesson 6. The Hidden Question

- **Big idea.** A two-step story hides a question you must answer first.
- **Strand.** MOE P3 word problems with the four operations and money, two steps (p. 35); drawing strips is a method, not named by MOE (p. 13). Contest tag: comparison and sum-and-difference. **Holiday boundary (H4):** H4 drew bar models for part-whole, comparison, times-as-many and before-and-after. Here the focus is finding the hidden step and the reversal trap; strips are drawn but not taught. Barred: ages-in-years, a ribbon cut in three, pencil box and pens pair, give-to-make-equal.
- **Objective.** Find and answer the hidden question in a two-step story; read "more than" and "fewer than" in the right direction; find two numbers from their sum and difference; undo a story. Think harder: reversal, sum and difference, undo. Go further: when a story cannot work.
- **Prerequisites.** Lessons 2 to 4 (operations); warm-up covers strips.
- **Remember (6 min).** (1) Draw two strips for "Ali has 8 and Mei has 3". (2) One step of a story: find the total. (3) Spiral from H4: draw one strip for "3 times as many".
- **Start here (6).** (1) "3 books at $4 each, a ruler for $2; Mei pays $20; change?" (14 spent, change 6; Q1.2). (2) A story with a hidden sum then a take-away. (3) A story with "times as many" (one unit, one story). (4) A story with a strip drawn for the child. (5) A story with money to $200. (6) Mark the hidden question in two given stories.
- **Think harder (4).** (1) The reversal trap: Siti has 1246 stickers, 358 more than Ravi; Ravi has? (888, V6.6). (2) Sum and difference: 515 beads altogether, Mei has 49 more than Ali; Ali has 233 and Mei 282 (V6.2). (3) Undo: Kai gave 120 to Maya, got 275 from Talib and now has 1308; at first 1153 (V6.1). (4) A cake costs 4 times as much as a pie and $27 more: pie $9, cake $36 (V6.3). Also a three-box story: 6 boxes of 250 pens, 475 sold, the rest in 5 packs, 205 in each (V6.4).
- **Go further (3).** G1 **Beyond (named): "Story That Cannot Work".** Two numbers with sum 91 and difference 14: no whole-number answer, because a sum and a difference have the same odd-or-even-ness (V6.5). Level note: parity reasoning is contest-style. G2 Three-step undo story. G3 Write a story whose hidden question is "how many in all".
- **Non-routine.** CMP T (reversal, sum and difference), MULTI T (V6.4), BACK T (V6.1), LOG G (V6.5). The Start here "times as many" exposure is also in lesson 3.
- **Numbers.** 3- and 4-digit numbers to 5000; money to $200; multipliers 2 to 7.
- **Home materials.** Pencil, strips of paper.
- **Kit.** None cut.
- **Figures.** `bar_model` compare and part-whole (exists; X14 for a ghost segment and four bars).
- **Misconceptions.** Adding when the sentence says "more than ... than Ravi" and Ravi is unknown; sharing the total without removing the difference first; giving the answer to the first step as the final answer.
- **Needs.** X14.

#### Lesson 7. Fractions on the Number Line

- **Big idea.** Every fraction has a place on the line, and many names.
- **Strand.** MOE P3 Fractions: equivalent fractions, simplest form, compare and order unlike fractions with denominators to 12, add and subtract two related fractions within one whole (1.1 to 2.1, p. 35). A sum of three fractions with three different denominators is beyond even Primary 4 (at most two denominators, p. 37). **Holiday boundary (H6):** H6 was the fraction wall: equivalents, comparing, adding related fractions, fractions between. Here the picture is the number line, the new skills are simplest form and "more parts to shade". Barred: ordering 2/3, 5/6, 7/12; 1/2 + 1/4 + 1/8; "halfway between 1/4 and 1/2"; the 5/6 jug.
- **Objective.** Place fractions on a 0 to 1 line, find equivalent fractions and the simplest form, compare and order, add and subtract related fractions, say how many more parts to shade. Think harder: simplest form by dividing; order three fractions; true, false or not possible to tell. Go further: fractions between.
- **Prerequisites.** Primary 2 fractions (halves, quarters, like fractions).
- **Remember (6 min).** (1) Shade 3 of 8 parts. (2) 1/2 = 2/4 on a strip. (3) Spiral from H6: 1/2 + 1/4.
- **Start here (6).** (1) Mark halves, quarters and eighths on a strip. (2) Place 3/4 and 5/8 on a 0 to 1 line. (3) "How many more parts must be shaded to show 5/8?" (3 more, V7.7). (4) 6/8 in simplest form (3/4, V7.1). (5) Compare 3/4 and 5/8 on the line. (6) 1/4 + 3/8 = 5/8 (V7.3).
- **Think harder (4).** (1) Simplest form of 10/12 (5/6, V7.1). (2) Order 5/8, 2/3, 3/4 (V7.2). (3) True, false or not possible to tell: 4/8 and 3/6 are the same point on the line (true, V7.8). (4) 3/4 = []/12 (9, V7.4); also 5/6 - 1/2 = 1/3 (V7.3).
- **Go further (3).** G1 **Beyond (named): "Between Neighbours".** Fractions between 1/3 and 1/2: only 5/12 has denominator 12; with denominator 24 there are three (V7.5). Level note: fractions between fractions is NOT IN. G2 Three fractions with three different denominators that make 1 whole: 1/2 + 1/3 + 1/6 (V7.6; beyond the Primary 4 limit of two denominators, so a contest item). G3 Write a fraction between 2/5 and 1/2 and prove it.
- **Non-routine.** EQ T (missing numerator), EXP T (V7.1), LOG G (V7.5).
- **Numbers.** Denominators 2, 3, 4, 5, 6, 8, 10, 12 (7 and 9 rare); sums within 1.
- **Home materials.** Pencil, a strip of paper to fold.
- **Kit (KT3 `fraction_strips`, 7 strips to cut).** Whole, halves, thirds, quarters, sixths, eighths, twelfths (20 cm, patterned not coloured). Contract: tasks use at most 4 strips at once; supplied 7. Reused in lesson 27.
- **Figures.** `fraction` strip, wall and line (X4); `number_line` with fraction labels through X5.
- **Misconceptions.** A larger denominator means a larger fraction; adding tops and bottoms; "more parts to shade" read as the target; not simplest because only divided once.
- **Needs.** X4, X5, KT3, RN4 (fraction answers).

#### Lesson 8. Dollars and Cents

- **Big idea.** Cents are hundredths of a dollar, and offers need a plan.
- **Strand.** MOE P3 add and subtract money in decimal notation (p. 35); P2 conversion between decimal notation and cents (p. 33). Contest tag: exact total from two prices (SASMO 19-22). **Holiday boundary (H9):** H9 had change from $10 and a menu with a $20 budget, 20¢ and 50¢ coins. Barred: ($3.80 + $1.45 from $10), "9 coins worth $3", the party planner. Here: offers, "which two items", exact total with a count limit.
- **Objective.** Add and subtract amounts to $100, give change, convert $ and ¢, use "3 for $8" offers, find which two items give an exact total. Think harder: offers; exact total with a limit on the count. Go further: all the ways to pay.
- **Prerequisites.** P2 money.
- **Remember (6 min).** (1) $3.20 = 320¢. (2) 7 + 8 + 5 in dollars and cents. (3) Spiral from H9: change from $10 for $6.50.
- **Start here (6).** (1) $4.50 + $2.85 (V8.1). (2) $20 - $13.65 (V8.1). (3) Express 1850¢ in dollars. (4) A bill of three items and the change from $50. (5) Compare two prices: how much more. (6) Coins and notes that make $7.35.
- **Think harder (4).** (1) Pens 1 for $3 or 4 for $10: exactly 11 pens at least cost, $29 (V8.2). (2) Menu roti $2.40, laksa $5.90, tea $1.80, cake $3.70, juice $2.60: exactly $8.30 on two different items (roti and laksa, V8.3). (3) Books $7 and pens $4: exactly $59 with fewer than 12 items (5 books and 6 pens, V8.4). (4) Change from $50 for two items.
- **Go further (3).** G1 **Beyond (named): "Exactly the Total".** Pay exactly $26 with $2 and $5 notes: all the ways, three of them (V8.5). Level note: listing all ways is contest-style. G2 A budget with three rules. G3 Write an offer and a question for a partner.
- **Non-routine.** CTX T (V8.2), LIST T (V8.3), GC T (V8.4), WAYS G (V8.5).
- **Numbers.** Decimal notation to $200; offers of 3 to 7 items; menus of 4 to 5 items.
- **Home materials.** Pencil.
- **Kit (KT4 `menu_cards`, 8 cards to cut).** 8 price cards with an item picture and a price. Contract: tasks use at most 5 at once; supplied 8. Reused in lessons 10 and 20 (as price tags).
- **Figures.** `price_tag`, `money` (exist), `column` for money (X1).
- **Misconceptions.** Aligning dollars and cents wrongly (5.9 as 5.09); treating 1850¢ as $1.85; choosing the cheaper lot without checking the count.
- **Needs.** KT4, X1, RN5 (money forms).

#### Lesson 9. Time Detectives

- **Big idea.** Time is a number line that loops.
- **Strand.** MOE P3 time: seconds, start, finish and duration, 24-hour clock (2.1 to 2.3, p. 36). Contest tag: calendar and day-of-week cycles (SASMO 19-10, 19-13, 20-4, 20-7). **Holiday boundary (H9):** H9 had 12- and 24-hour conversion, a 10-minute-fast station clock, an overnight train, school timetable. Barred: station clock 10 minutes fast, 22:40 to 01:15, 09:30 to 21:00, "bus every 25 minutes". Here: seconds, calendar cycles, and fast and slow watches in both directions.
- **Objective.** Convert minutes and seconds, find duration, start and finish across noon, use the 24-hour clock, and move through calendar days. Think harder: find the start; set a slow or fast watch right. Go further: a watch seen in two journeys.
- **Prerequisites.** Primary 2 time to the minute.
- **Remember (6 min).** (1) 60 seconds in a minute, 3 min 15 s in seconds. (2) 14 30 is 2:30 pm. (3) Spiral from H9: 24-hour conversion.
- **Start here (6).** (1) 3 min 15 s = 195 s (V9.1). (2) 7:45 am to 9:20 am is 1 h 35 min (V9.2). (3) Write 2:30 pm as 14 30 (V9.8). (4) A film starts at 4:15 pm and lasts 1 h 50 min. (5) 30 April is a Wednesday; what day is 7 May (V9.7)? (6) Draw a timeline for a journey.
- **Think harder (4).** (1) A film ends at 5:10 pm and lasts 2 h 25 min: it started at 2:45 pm (V9.3). (2) A watch 12 minutes slow shows 8:35: the real time is 8:47 (V9.4). (3) Today is Tuesday; the day 45 days later is Friday (V9.6). (4) A timeline question with a draw-a-timeline instruction.
- **Go further (3).** G1 **Beyond (named): "Wrong Watch".** A watch 25 minutes fast shows 2:45 pm at the start and 4:20 pm at the end of a game; the real times are 2:20 pm and 3:55 pm (V9.5). Level note: setting a fast or slow clock right is P3 time reasoning; the double reading is contest-style. G2 Two watches, one fast and one slow. G3 A journey in three legs.
- **Non-routine.** CTX T (V9.4), BACK T (V9.3), BACK G (V9.5), CMP G (two watches).
- **Numbers.** Times to the minute; durations to 6 h 45 min; 24-hour times 00 00 to 23 59.
- **Home materials.** A real or toy clock if there is one; a calendar page.
- **Kit (KT5 `clock_kit`, exists; 4 hands to cut).** 2 clock faces (not cut), 2 hour hands, 2 minute hands. Contract: tasks use 2 faces and 2 hand pairs (the two-watch item). Keep the clock for lessons 23 and 35.
- **Figures.** `clock` (exists; X13 for a 24-hour readout), time line (`number_line` labels), `calendar` (exists).
- **Misconceptions.** 1:60; crossing noon and writing 12 + 12; setting a slow watch the wrong way; counting the start day.
- **Needs.** KT5, X13.

#### Lesson 10. Price per Piece, and Mi's Challenge Quest

- **Big idea.** If you know the price of several, you can find the price of one.
- **Strand.** MOE P3 division word problems with money; the price of one in whole numbers only, no ratio notation (the P3 SPEC avoids ratio, plan line 62). Contest tag: shared payment (SASMO 20-12). Division of money by a whole number with a decimal answer is P4, so every price here divides exactly. **Holiday boundary (H9, H4):** H9 and H4 had simultaneous prices (pencil box and pens). Barred: "a pencil box and 3 pens cost $25 ... and 5 pens cost $35". The Quest runs in this lesson, so Explore (10) and Mini-lesson (9) are the whole new idea.
- **Objective.** Find the price of one from a pack; share a bill when two friends bought different numbers; read offers with free items. Think harder: simultaneous prices; free items. Go further: price per item with free items.
- **Prerequisites.** Lesson 4 (division), lesson 8 (money).
- **Remember (6 min).** (1) 6 pencils cost 120¢: 20¢ each. (2) 4 x $7. (3) Spiral from H4: draw one strip for "4 equal parts".
- **Start here (6).** (1) 4 pens cost $12; one pen costs $3. (2) 6 pencils cost 120¢; one costs 20¢. (3) "$3 each: 7 pens cost?" (4) Which is the better buy, 3 for $8 or 5 for $12: 5 for $12, because one pen costs $2.40 against about $2.67 (V10.8). (5) A bill shared. (6) 8 stickers for $24: one costs $3. (Prices of one: V10.7.)
- **Think harder (4).** (1) Kai bought 4 mugs and Maya 7 mugs; together they paid $77: $7 each, Kai $28, Maya $49 (V10.1). (2) 3 cakes and 1 tart cost $17; 1 cake and 1 tart cost $9: a cake $4, a tart $5 (V10.2). (3) For every 4 books a bookmark is free: 28 books give 7 bookmarks (V10.3); for every 5 pens bought 3 are free, so to end with 64 pens in all you buy 40 (V10.4). (4) Find the paid-and-change price of one item (BACK).
- **Go further (3).** G1 **Beyond (named): "Free Pen Price".** Buy 3 get 1 free for $24: the price of each of the 4 pens is $6 (V10.5). Level note: unit price with free items is contest-style. G2 Cave-style: pens 1 for $3, 2 for $5, 5 for $11, exactly 9 pens at least cost $21 (V10.6; this is also the optional cave item for the Quest). G3 A rate table with a free item.
- **Non-routine.** CMP T (V10.2), CTX T (V10.3, V10.4), TAB T (rate table), BACK T, CTX G (V10.5, V10.6).
- **Numbers.** Whole-dollar and whole-cent unit prices; packs of 3 to 8; totals to $100.
- **Home materials.** Pencil; the price cards from lesson 8.
- **Kit.** No new kit (reuse `menu_cards`, lesson 8). The Quest Log is a separate 3-page file in the book (Book 2).
- **Figures.** `bar_model` units with a total (exists; X14), `price_tag` (exists), `table` (exists).
- **Misconceptions.** Dividing the smaller by the larger; subtracting the free items from the count; counting the free ones as paid; assuming the cheapest per piece uses all items.
- **Needs.** X14, TL3 (Quest builder).
- **Quest (lesson 10).** Gates in section 8.

### 1.3 Term 2: Measurement, shape, data and patterns (lessons 11 to 20)

Can a new child join cold? Yes: the warm-up covers written add and subtract with regrouping, a short-division or multiplication fact, a two-step story and one fraction fact from Term 1. Each lesson needs only Primary 2 measures and number work. Holiday graduates meet area and perimeter by tiling (H7), angles (H8), compound units (H9), bar-graph reading (H10) and column logic (H2) only in the first six minutes. School mid-year assessments often fall late in this term [UNVERIFIED for any single school]. **Safest to skip or make up: lesson 14**; chains: 11, 12 are independent; 13 feeds 14 and 30; 16 feeds 20. Lesson 20 hosts the Quest.

#### Lesson 11. Length and Distance

- **Big idea.** A kilometre is a thousand metres you can feel, and equal gaps hide an off-by-one count.
- **Strand.** MOE P3 length in km, m, cm; compound units and conversions (p. 36). Contest tag: gaps and posts (SASMO 20-14; about 71 school items in the P3 papers, every term). **Holiday boundary (H9):** H9 was conversion in compound units (2 m 45 cm to cm), a 1 km 250 m walk to school and back, and a 5 m ribbon cut into two pieces 80 cm apart. Barred: those three items and the 25-minute bus timetable. New: benchmarks, a ruler that does not start at 0, route maps, posts and gaps (the line version moved here from the plan's lesson 33, which keeps the ring).
- **Objective.** Estimate with benchmarks, convert km, m and cm, read a ruler picture that starts away from 0, compare routes, count posts and gaps on a straight line. Think harder: posts and gaps; a circuit. Go further: a three-day distance in two units; gaps in time.
- **Prerequisites.** Primary 2 length.
- **Remember (6 min).** (1) 1 m = 100 cm, 1 km = 1000 m. (2) Read a pencil's length from a ruler picture that starts at 0. (3) Spiral from H9: 2 m 45 cm in centimetres.
- **Start here (6).** (1) 2 km 350 m in metres (2350, V11.8). (2) Choose the best estimate for a classroom's length (8 m, 8 km, 8 cm). (3) Read the length of a pencil on a ruler picture whose left end is at 3 cm. (4) Route A is 4 km 80 m and route B 3 km 960 m: which is shorter, and by how much (120 m, V11.5). (5) 1 km 450 m + 2 km 650 m = 4 km 100 m (V11.9). (6) A story with a length in m and cm.
- **Think harder (4).** (1) Posts stand 6 m apart on a straight line from 0 m to 54 m: how many posts (10, V11.1)? (2) The 1st to the 5th lamp post is 24 m: how far from the 1st to the 21st (120 m, V11.2)? (3) A park path is a rectangle 350 m by 150 m; Ben jogs round it 3 times: 3000 m, that is 3 km (V11.4). (4) True, false or not possible to tell about route lengths on a map with legs in metres.
- **Go further (3).** G1 **Beyond (named): "Count the Gaps".** A fence has a post every 3 m and 25 posts in a line: 72 m (V11.6); a clock strikes 4 times in 9 seconds: 7 strikes take 18 seconds (V11.7). Level note: gaps and posts is not in the syllabus. G2 A hiker walks 3 km 250 m on day 1, 650 m more on day 2, and 1 km 400 m less on day 3 than on day 2: 9 km 650 m in all (V11.3). G3 The shortest route on a map with five legs.
- **Non-routine.** DIAG T (V11.1, V11.2), GEO T (V11.4), CMP T (V11.5), MULTI G (V11.3), DIAG G (V11.7).
- **Numbers.** km and m to 10 km; cm to 100; posts 5 to 25; gaps 3 to 20 m.
- **Home materials.** 30 cm ruler, a 1 m piece of string, a tape if there is one.
- **Kit.** None cut; a printed posts mat (not cut).
- **Figures.** `posts` and `route map` (X9), `ruler` (exists; non-zero start through `objects.from`), `number_line` (exists).
- **Misconceptions.** Posts equal gaps; reading an object's length from the wrong end of the ruler; 1 km 40 m written 1400 m; a ring and a line treated alike.
- **Needs.** X9, X5, RN1.

#### Lesson 12. Mass and Volume

- **Big idea.** Heavy and full are measured with the same kind of scale, and a balance can be solved by drawing it.
- **Strand.** MOE P3 mass in kg and g, volume in l and ml, compound units add and subtract (p. 36). Contest tag: balance with identical objects, a tank weighed twice (SASMO 19-9, 20-13). **Holiday boundary (H9):** H9 had 3060 g in kg and g, a pail of 4 l 500 ml, a 2 l bottle poured into 300 ml cups, a box of 4 books at 1 kg 50 g, a bottle half poured out (1 kg 200 g to 750 g), cartons of milk. Barred: all of these, above all the "bottle half poured out" (it is SASMO 20-13's move). New: dials and jugs read from a picture, balances with identical objects, two weighings.
- **Objective.** Read a dial and a jug, convert and add and subtract compound units, solve a balance picture, use two weighings. Think harder: a balance; a tank. Go further: weighing twice.
- **Prerequisites.** None.
- **Remember (6 min).** (1) 1 kg = 1000 g, 1 l = 1000 ml. (2) Read a jug marked every 100 ml. (3) Spiral from H9: 4 l 500 ml in millilitres.
- **Start here (6).** (1) 3095 g in kg and g (3 kg 95 g, V12.1). (2) Read a kitchen dial (0 to 5 kg, a mark every 100 g). (3) Read a jug (0 to 1000 ml). (4) 4 kg 750 g + 1 kg 380 g = 6 kg 130 g (V12.2). (5) A bottle holds 1 l 250 ml and 380 ml is drunk. (6) Which is heavier and by how much.
- **Think harder (4).** (1) 4 identical parcels balance 3 of them and a 900 g weight: a parcel is 900 g (V12.3); 5 bags balance 2 bags and 3 kg: a bag is 1 kg (V12.4). (2) A tank is filled with 5 jugs, a jug holds 4 cups, a cup 150 ml: 3 l (V12.5). (3) A plate of 450 g and 3 identical cups weigh 1 kg 200 g: a cup is 250 g (V12.6). (4) "Heavier by" with a multiple (one object is 3 times as heavy and 1 kg more).
- **Go further (3).** G1 **Beyond (named): "Weighing Twice".** A tank with 3 l of water weighs 5 kg 200 g and with 5 l weighs 7 kg 200 g; each litre of water has mass 1 kg (given in the question); the empty tank is 2 kg 200 g (V12.7). Level note: two weighings and subtract is a contest move; the units are Primary 3. G2 A two-step jug and cup story. G3 Pose a balance puzzle.
- **Non-routine.** DIAG T (V12.3, V12.4), MULTI T (V12.5), BACK T (V12.6), CMP T, DIAG G (V12.7).
- **Numbers.** kg and g to 9 kg; l and ml to 6 l.
- **Home materials.** Kitchen scale if there is one, cups, a jug, a 1 l bottle.
- **Kit.** None cut.
- **Figures.** `dial`, `jug`, `balance` (X6), `column` with unit headers (X1), `table` (exists).
- **Misconceptions.** 1 l = 100 ml; adding kg and g as one number; the heavier side of a balance read as the larger number; mixed units in the answer.
- **Needs.** X6, X1, RN1.

#### Lesson 13. Fences and Floors

- **Big idea.** Area counts squares, perimeter walks the edge, and they change independently.
- **Strand.** MOE P3 area in cm2 and m2 (no conversion), perimeter of a rectilinear figure, rectangle and square, area of a rectangle and square (p. 36); composite area is P4 (p. 39). Contest tag: perimeter grows by 2x when a side grows by x (SASMO 20-17); the P3 papers add figures of identical rectangles and a wire bent into a rectangle then a square (GEO, 42 items). **Holiday boundary (H7): this is the largest overlap in the year.** H7 was the whole strand in challenge form: 12 squares into every rectangle, all rectangles of area 24 or perimeter 24 in a table, an L-shape with a corner cut out, a square cut in two, an 8 by 2 rectangle and a square of the same perimeter, gardens 9 m by 5 m and 7 m by 7 m, 2 cm tiles on a mat, 5 squares of 2 cm for the biggest perimeter. Barred: all of these. New: units and everyday scale, three shapes of one perimeter, figures of identical parts, a wire bent twice, one side stretched.
- **Objective.** Find area and perimeter with units; perimeter of a rectilinear figure from labelled sides; figures of identical parts; compare. Think harder: same perimeter different area; identical parts. Go further: a wire bent twice; stretching one side.
- **Prerequisites.** Lesson 3 (multiplication).
- **Remember (6 min).** (1) Rows times columns. (2) The perimeter of a 7 by 3 rectangle. (3) Spiral from H7: area by counting squares.
- **Start here (6).** (1) Count the squares and the edges of a shaded figure on a grid. (2) Area of a 9 cm by 4 cm rectangle (36 cm2, Q2.1). (3) Perimeter of a rectilinear figure with labelled sides. (4) A square of side 8 m: area and perimeter. (5) A floor 6 m by 5 m: area in m2. (6) Which two figures have the same perimeter (a picture of three).
- **Think harder (4).** (1) A square has a perimeter of 36 cm: its area is 81 cm2 (V13.1). (2) Three rectangles of perimeter 24 cm: 10 by 2, 8 by 4 and 6 by 6 have areas 20, 32 and 36 cm2 (V13.2). (3) Five identical squares in a row have a perimeter of 36 cm: each side is 3 cm and the figure's area is 45 cm2 (V13.4). (4) True, false or not possible to tell about two figures (same perimeter? same area?).
- **Go further (3).** G1 **Beyond (named): "Stretch One Side".** A rectangle 12 cm by 7 cm is made 5 cm longer: its perimeter grows by 10 cm, whatever the breadth (V13.5). Level note: contest move (SASMO 20-17); the arithmetic is Primary 3. G2 A wire 56 cm long is bent into a rectangle 18 cm long and then into a square: the square's area is 196 cm2 (V13.3). G3 A fence with a gap for a gate.
- **Non-routine.** GEO T (V13.1, V13.2, V13.4), EXP T, GEO G (V13.3, V13.5).
- **Numbers.** Sides to 50 cm, perimeters to 108 m; 2 to 5 identical parts.
- **Home materials.** Ruler, string (about 60 cm), squared paper.
- **Kit (KT6 `square_tiles`, 24 tiles to cut).** 24 square tiles of 2 cm. Contract: the Explore makes rectangles of 24 tiles (maximum used 24); perimeter play uses 16 or fewer; supplied 24. Keep for lessons 17 and 31.
- **Figures.** `grid` squares (exists) with edge labels and identical-part figures (X8), `area_model` (X3).
- **Misconceptions.** Perimeter and area confused; adding only two sides; counting a corner square twice; cm and cm2 mixed.
- **Needs.** X8, X3, KT6.

#### Lesson 14. Cut, Slide, Count

- **Big idea.** Moving a piece does not change its area.
- **Strand.** MOE P3 area of a rectangle (p. 36); composite figures are P4 (1.3, p. 39) and half squares joined into whole squares are contest-style (SASMO 20-21). The P3 papers do set figures of identical rectangles and the area of one tile (patterns section 3.9), so Start here stays with those and with counting; splitting a figure into rectangles with labelled sides is a Think harder idea labelled Primary 4 on purpose. **Holiday boundary (H7):** H7 had a 10 m by 8 m rectangle with a corner cut out, a square cut into four squares in a row, 7 by 5 with four corners removed. Barred: any rectangle with a corner removed.
- **Objective.** Count area on a grid with half squares, cut and slide to a rectangle, find the area of one tile, split an L-shape. Think harder: half squares; splitting. Go further: cost with two materials.
- **Prerequisites.** Lesson 13.
- **Remember (6 min).** (1) 9 x 6. (2) Count the squares in a shaded L. (3) Spiral from H7: the perimeter of a rectangle.
- **Start here (6).** (1) Count the whole squares in a grid figure. (2) A figure of 4 identical rectangles, each 6 cm by 2 cm, in a row: its area. (3) Cut the piece and slide it to make a rectangle: the area is unchanged. (4) A figure of 6 identical squares has area 54 cm2: the area of one tile is 9 cm2 (V14.4). (5) How many more squares to cover a 5 by 4 rectangle. (6) Match the figure to the rectangle it can be cut and slid into.
- **Think harder (4).** (1) A shaded region has 8 whole squares and 6 half squares: its area is 11 squares (V14.1). (2) An L-shape made of a 7 cm by 3 cm and a 4 cm by 5 cm rectangle: 41 cm2 (V14.3). (3) True, false or not possible to tell: two figures have the same area. (4) Which rectangle has the same area as the cut-and-slide figure.
- **Go further (3).** G1 **Beyond (named): "Half-Square Puzzle".** A shaded region on a grid made of whole squares and halves, with the halves not pairing in the obvious way (V14.1). Level note: joining halves is Primary 3 reasoning; splitting into rectangles is Primary 4. G2 Cost a floor: 12 m2 at $4 a square metre and 18 m2 at $6: $156 (V14.2). G3 Which pieces make this figure.
- **Non-routine.** GEO T (V14.1, V14.3), EXP T, LIST G, MULTI G (V14.2).
- **Numbers.** Sides to 12; squares to 36; costs to $200.
- **Home materials.** Squared paper; a grown-up cuts.
- **Kit (KT7 `cut_slide`, 8 pieces to cut).** 4 half-square triangles, 2 rectangles, 2 L-pieces. Contract: the Explore uses all 8; supplied 8.
- **Figures.** `grid` with half-square shading and labelled edges (X8), `area_model` (X3).
- **Misconceptions.** A half square counted as a whole or as zero; a border square counted twice; thinking a slide changes the area; cost found by one total area times one price.
- **Needs.** X8, X3, KT7.

#### Lesson 15. Lines and Corners

- **Big idea.** A right angle is a ruler for every other angle, and parallel lines never meet.
- **Strand.** MOE P3 angles (right angle, greater or smaller) and perpendicular and parallel lines, identify and draw (p. 36). Contest tag: letters with both kinds of line (papers). **Holiday boundary (H8):** H8 had the folded-paper checker, right angles in a rectangle, clock-hand angles at o'clock, the hash sign, letters E and H, four lines from a point (6 angles), a staircase of squares, a noughts-and-crosses grid, "Mei says perpendicular means up and across". Barred: all of these. New: drawing with the cut-out checker or a set square, naming lines in a lettered figure, arrowheads, sorting angles, a street map.
- **Objective.** Name and draw perpendicular and parallel lines, mark right angles in a figure, sort angles as greater or smaller than a right angle. Think harder: letters with both; listing pairs. Go further: counting right angles at crossings.
- **Prerequisites.** None.
- **Remember (6 min).** (1) A right angle is a square corner. (2) Two edges of a ruler are parallel. (3) Spiral from H8: fold paper twice for a checker.
- **Start here (6).** (1) Mark the right angles in a figure of 6 lettered points. (2) Name a pair of parallel lines (arrowheads). (3) Name a line perpendicular to AB. (4) Draw a line parallel to AB through a point on a grid. (5) Draw a line perpendicular to AB with the checker. (6) How many angles are smaller than a right angle in a figure with 3 to 8 marked angles.
- **Think harder (4).** (1) Which of the letters H, A, M, L, E, T (drawn in block capitals on a grid) have both a pair of parallel and a pair of perpendicular lines. (2) List every pair of perpendicular lines in a lettered figure. (3) A street plan: which street is parallel to the school road. (4) True, false or not possible to tell about two lines in a picture.
- **Go further (3).** G1 **Beyond (named): "Crossroads Count".** Three parallel streets crossed by four parallel streets make 12 crossings and 48 right angles (V15.1): crossings times 4. Level note: counting is Primary 3; the product rule is contest-style. G2 True or false with a counterexample: "any two lines that cross make four right angles". G3 Draw a figure with exactly 3 right angles.
- **Non-routine.** LOG T (letters), LIST T, EXP G.
- **Numbers.** 3 to 8 marked angles per figure; figures with 6 to 9 lettered points.
- **Home materials.** Ruler; a set square if there is one.
- **Kit (KT8 `angle_kit`, 4 pieces to cut).** 2 right-angle checkers (card corners with a quarter-circle mark) and 2 straight-edge strips. Contract: tasks use at most 2 checkers; supplied 2 and 2.
- **Figures.** `lines_fig` (X10), `grid` (exists).
- **Misconceptions.** Perpendicular means vertical and horizontal; parallel lines are the same length; measuring an angle from the wrong corner; arrowheads read as part of the line.
- **Needs.** X10, KT8.

#### Lesson 16. Bar Graphs that Tell Stories

- **Big idea.** A graph's scale decides what you notice.
- **Strand.** MOE P3 bar graphs, including different scales on the axis (p. 36); picture graphs with a scale are P2 (p. 34). Contest tag: picture graph with a key (SASMO 19-18), reading a bar graph (20-19). **Holiday boundary (H10):** H10 had a bar graph with lines at 0, 10, ..., 50 and a half-way bar, a stamps graph (Ali 35, Ben 20, Mei 15 more) and a paper-collection graph with a 10 kg clue. Barred: those. New: the scale torn off, a missing bar from clues, double bars, a picture key of 5, 6 or 10, a misleading scale, true, false or not possible to tell.
- **Objective.** Read and draw bar graphs with scales 1, 2, 5, 10, 20, 50; read a picture graph with a key; find a missing bar; judge statements. Think harder: statements; the best scale. Go further: the missing scale and bar.
- **Prerequisites.** None.
- **Remember (6 min).** (1) Read a bar against a scale of 5. (2) Count in 5s and 20s. (3) Spiral from H10: a bar halfway between two lines.
- **Start here (6).** (1) Read a bar graph with a scale of 5 (3A 35, 3B 50, 3C 20, 3D 45). (2) How many more did 3B collect than 3C. (3) How many altogether (150, V16.3). (4) Complete a table from a picture graph with a key of 6. (5) Draw the missing bar of 20. (6) Which class collected the least.
- **Think harder (4).** (1) Each statement is true, false or not possible to tell: "3A collected 15 more than 3C" (true), "3C and 3D together collected more than 3B" (true), "3D collected twice as much as 3C" (false), and one that the graph cannot show (V16.3). (2) Re-read the same data on a graph with a different scale. (3) A double bar graph (boys and girls). (4) Which scale is better for these numbers.
- **Go further (3).** G1 **Beyond (named): "The Missing Scale".** The scale is torn off; bars of 2, 3 and 5 spaces are 150 in all, so one space is 15 and the bars are 30, 45 and 75 (V16.2). Level note: a graph with the scale removed is a school item; finding a unit from a total is contest-style. G2 Four bars total 150: A is 40, B is twice A, D is 15 fewer than A: C is 5 (V16.1). G3 Write a question the graph cannot answer.
- **Non-routine.** EXP T (V16.3), CMP T, EQ T (make two bars equal), CHAL G (V16.1, V16.2).
- **Numbers.** Scales 1, 2, 5, 10, 20, 50; 4 to 6 bars; totals to 450; picture key 5, 6, 10.
- **Home materials.** Squared paper, pencils.
- **Kit.** None cut; a printed graph mat.
- **Figures.** `bar_graph` (X7), `picture_graph` (exists), `table` with a tick column (X18).
- **Misconceptions.** Reading the number of squares instead of the scale; counting the bar top; assuming the tallest bar is the most whatever the scale; starting a bar at the wrong line.
- **Needs.** X7, X18.

#### Lesson 17. Patterns That Grow

- **Big idea.** Look at the gaps, then the gaps of the gaps.
- **Strand.** MOE P3 number patterns (1.1, p. 35); growing-figure patterns and two-number operator rules are NOT IN (SASMO 19-17, 20-8). **Holiday boundary (H10, H1):** H10 had 5, 9, 13, 17 (the 10th number), triangles in a row with sticks (12 triangles) and growing squares; H1 had 1, 3, 7, 15, 31 and +7 from 1000. Barred: sticks for triangles in a row, growing squares from sticks, the doubling-plus-one sequence, +7 from 1000. New: chairs round tables, alternating steps, growing gaps, operator rules, two patterns that share a number.
- **Objective.** Extend and describe patterns, use a table for the nth figure, find the figure for a total. Think harder: growing gaps, an operator rule, alternating steps. Go further: two patterns that meet.
- **Prerequisites.** None.
- **Remember (6 min).** (1) Extend +3. (2) A table of position and total. (3) Spiral from H1: counting in 6s.
- **Start here (6).** (1) Extend a +3 and a -5 pattern. (2) Tables pushed together in a row: 1 table seats 6, 2 seat 10, 3 seat 14 (V17.6). (3) Seats at 10 tables: 42 (V17.1). (4) Fill a table of tables and seats. (5) The rule in words. (6) A pattern on a number line.
- **Think harder (4).** (1) How many tables seat 90 (22, V17.1)? (2) Gaps that grow by 2: 3, 5, 9, 15, 23, 33 (V17.2). (3) A sign works on two numbers: 5 and 2 give 13, 4 and 4 give 8, 7 and 1 give 20, 6 and 3 give 15; what do 9 and 5 give (22; the rule is "3 times the first, take away the second", the only rule of that kind, V17.3)? (4) Alternating steps: 1200, 1500, 1450, 1750, ...: the 9th is 2200 (V17.4).
- **Go further (3).** G1 **Beyond (named): "Where Two Patterns Meet".** 5, 9, 13, ... and 3, 8, 13, ...: the numbers in both are 13, 33, 53 (V17.5). Level note: common terms of two patterns are common multiples (Primary 4, p. 37). G2 A harder sign from three examples. G3 Invent a growing pattern and predict the 50th figure.
- **Non-routine.** PAT T (V17.1, V17.2, V17.4), LOG T (V17.3), PAT G (V17.5).
- **Numbers.** Figures to the 10th or 20th; steps 2 to 1000.
- **Home materials.** The square tiles from lesson 13 as tables, pencil.
- **Kit.** No new kit (reuse `square_tiles`; contract: tasks use at most 16 tiles).
- **Figures.** `table`, `seq` (exist), `objects` rows (exist).
- **Misconceptions.** The figure number times the first difference as the rule; off by one for the first figure; a rule guessed from two terms.
- **Needs.** None beyond the existing tools.

#### Lesson 18. Balance and Swap

- **Big idea.** Equal means the same on both sides, so symbols can be swapped.
- **Strand.** Picture equations and balances are NOT IN (letters for unknowns are P6, p. 43, so symbols only); chained comparisons (SASMO 19-9, 19-15, 19-20, 20-22). **Holiday boundary (H4):** H4 had a pencil box and pens at $25 and $35, 2 jugs and 3 cups (a jug holds 3 times as much as a cup), bags of sugar and flour. Barred: those. New: "2 of A balance 3 of B" chains, a box used twice, baskets that differ by one item.
- **Objective.** Swap a symbol, order objects from comparisons, solve a box used twice, subtract one picture equation from another. Think harder: order; baskets. Go further: the gap after a gift.
- **Prerequisites.** None.
- **Remember (6 min).** (1) 3 + [] = 10. (2) One balance: 2 cubes balance 1 block. (3) Spiral from H4: before and after.
- **Start here (6).** (1) A balance with identical objects: 1 box balances 3 cubes. (2) Swap one symbol in a picture equation. (3) Find the value of a box in one line. (4) Two scales, one question. (5) Fill a missing number on a balance. (6) Which side is heavier.
- **Think harder (4).** (1) 2 apples balance 3 pears and 4 pears balance 3 plums: an apple is 9, a pear 6 and a plum 8 (units); heaviest to lightest is apple, plum, pear (V18.1). (2) A box used twice: 5 boxes and 1 box make 3 x 14 + 6: the box is 8 (V18.2). (3) Basket A has 3 mangoes and 2 limes for $19; basket B has 3 mangoes and 1 lime for $14: a lime is $5 and a mango $3 (V18.3). (4) A box on both sides of an equals sign.
- **Go further (3).** G1 **Beyond (named): "Heaviest to Lightest".** Four objects ordered from three balance pictures, then the second heaviest named. Level note: chained comparisons are contest-style. G2 Ria has 180 more stamps than Sam and gives him 45: she now has 90 more (V18.4). G3 Pose a two-basket puzzle.
- **Non-routine.** DIAG T (V18.1), CMP T (V18.3), EQ G (V18.4).
- **Numbers.** Masses to 20 units; totals to $100.
- **Home materials.** None special.
- **Kit (KT9 `balance_cards`, 9 cards to cut).** 3 apples, 3 pears, 3 plums (told apart by outline pattern, not colour). Contract: the Explore uses 9 on a printed balance mat; supplied 9.
- **Figures.** `balance` (X6), `picture_equation` (exists).
- **Misconceptions.** The heavier side has more objects; swapping unlike objects; reading "2 of A = 3 of B" as A = 3 B.
- **Needs.** X6, KT9.

#### Lesson 19. Cube Stacks and Views

- **Big idea.** A solid can be read from above and from the front.
- **Strand.** P2 3D shapes (cube, cuboid, p. 34) as spiral; stacks, top and front views are NOT IN; a pyramid is beyond the P2 list; nets are Primary 4 (p. 39). No school-paper evidence (patterns section 5); contest SASMO 19-4, 20-6, 20-15. **Holiday boundary:** none (H7 and H8 are flat); the largest SASMO gap is new here. This is the plan's added lesson.
- **Objective.** Count cubes in a stack from a drawing, read a height grid, draw top and front views, find the fewest and most cubes for given views. Think harder: views; hidden cubes. Go further: fewest and most.
- **Prerequisites.** Lesson 3 (multiplication).
- **Remember (6 min).** (1) Count the cubes in a 2 by 3 by 2 block. (2) Rows and columns. (3) Spiral from lesson 13: area as squares.
- **Start here (6).** (1) Build a stack of 5 cubes from a picture. (2) A height grid, rows (front first) 2 1 3 / 0 2 1 / 1 1 2: 13 cubes (V19.1). (3) From above you see 8 squares (V19.1). (4) From the front you see columns 2, 2 and 3: 7 squares (V19.1). (5) Match a stack to its top view. (6) How many cubes cannot be seen.
- **Think harder (4).** (1) Draw the top view as numbers. (2) Pick the right top view by checking one feature at a time. (3) A square-based pyramid has 5 faces, four triangles and one square (beyond P2). (4) Which view cannot belong to the stack.
- **Go further (3).** G1 **Beyond (named): "Fewest and Most".** The front view shows columns of height 3, 1 and 2 on a base 3 wide and 2 deep with every square used: at least 9 and at most 12 cubes (V19.2). Level note: not in the syllabus; Primary 5 papers ask "greatest number of cubes to add". G2 Match a net to a solid (Primary 4 preview). G3 Describe a stack by its views only.
- **Non-routine.** LOG T (views), DIAG T (draw a top view), LIST G (V19.2).
- **Numbers.** Base at most 3 by 3; heights at most 3; at most 14 cubes.
- **Home materials.** 12 to 14 blocks of one size (building bricks, dice, sugar cubes). Fallback: drawn stacks and counters on a printed base mat. The 13-cube grid is drawn only.
- **Kit.** None cut; a printed 3 by 3 base mat. Contract for the family's blocks: supplied 14, maximum used by a real-block task 12.
- **Figures.** `cube_stack` (exists: iso, top, views); a pyramid (X15, optional). No hand-drawn figure is needed (D18).
- **Misconceptions.** Forgetting hidden cubes; counting faces; the front view as the sum of all heights.
- **Needs.** RN7 (picture options).

#### Lesson 20. The Class Shop, and Mi's Challenge Quest

- **Big idea.** A realistic problem needs several skills at once.
- **Strand.** Project and review of lessons 8, 10 to 16: money, graphs, measures. **Holiday boundary (H9):** the party planner (a $20 budget for 8 friends from a menu card). Barred: that menu, budget and rule. New: a class shop with a price list, offers, a sales bar graph and a mass item.
- **Objective.** Plan a stall for a budget, read a sales bar graph, justify the best plan. Think harder: a plan within a budget; least cost with offers. Go further: prove no cheaper plan exists.
- **Prerequisites.** None (a review).
- **Remember (6 min).** (1) Read a bar to a scale. (2) The price of one from a pack. (3) The area of a rectangle.
- **Start here (6, 25-minute workbook).** Price-list reading, totals and change, three bar-graph readings, a mass in kg and g.
- **Think harder (4).** A plan with an offer; least cost for the class; how many of each within a budget; a table of sales.
- **Go further (3).** G1 **Beyond (named): "Best Plan Proof".** List every plan that meets the rules and show none costs less. Level note: exhaustive checking is contest-style. G2 A backwards sales story. G3 Pose a shop rule.
- **Non-routine.** CMP T, MULTI T, GC T, BACK G, WAYS G.
- **Home materials.** Pencil; the price cards.
- **Kit (KT10 `price_tags`, exists; 10 tags to cut).** 10 stall tags (item picture and price). Contract: tasks use at most 8 at once; supplied 10.
- **Quest (lesson 20).** Gates in section 8.
- **Needs.** KT10, X7, TL3.

### 1.4 Term 3: Space, modelling and reasoning (lessons 21 to 30)

Can a new child join cold? Yes: the warm-up covers area and perimeter of a rectangle, reading a bar graph, a strip for a two-step story and one unit conversion; lesson 24 re-teaches the strip in its first 3 minutes. Holiday graduates revisit strips (H4, for 24 and 25), fraction walls (H6, 27), compound units (H9, 28), logic from clues (H10, 29), perimeter and area (H7, 30) in the first six minutes only. Term 3 usually has no school exam peak [UNVERIFIED]. **Safest to skip or make up: lesson 23** (the weakest lesson; nothing later depends on it). Chains: 24 and 25 are a pair; 21 and 22 share a figure family; 30 reviews 13, 14, 16, 24.

#### Lesson 21. Fold, Flip, Mirror

- **Big idea.** Some changes keep the shape and some do not.
- **Strand.** Symmetry and reflection are Primary 4 (p. 39); paper folding and cutting are NOT IN; choosing a mirror image by checking one feature at a time is a contest move (SASMO 19-7). No school-paper evidence (patterns section 5). **Holiday boundary:** none (H8 is angles); new. Start here stays pre-formal: fold to check, the word "symmetry" is introduced as a name for what the fold shows.
- **Objective.** Fold and cut, predict the unfolded shape, check a mirror image feature by feature. Think harder: unfolded cut-outs; mirror images; fold twice. Go further: fold three times.
- **Prerequisites.** None.
- **Remember (6 min).** (1) Halve a paper square by folding. (2) Say which side is left and right in a picture. (3) Spiral from lesson 15: a right angle is a square corner.
- **Start here (6).** (1) Fold a paper in half: draw the fold line. (2) Complete the other half of a shape on a grid across a dashed line. (3) Which letters look the same in a mirror (A, H, M against F, R). (4) Cut a notch from a folded paper: draw the cut-out. (5) Is this line a fold that matches the halves (circle Yes or No). (6) Count the matching parts in a flag.
- **Think harder (4).** (1) Predict the unfolded cut-out from a folded one with one notch. (2) Choose the mirror image of a picture from four, checking one feature at a time (left and right swap, up and down do not). (3) A square folded in half twice and punched once has 4 holes (V21.1). (4) True, false or not possible to tell about mirror images.
- **Go further (3).** G1 **Beyond (named): "Fold Three Times".** A square folded in half three times and punched once has 8 holes (V21.1); a paper strip folded in half three times and cut once straight across (not on a fold) falls into 9 pieces (V21.2). Level note: not in the syllabus. G2 Design a pattern with a given symmetry. G3 Pose a fold-and-cut puzzle with its answer.
- **Non-routine.** LOG T (mirror), EXP T, PAT G (V21.1, V21.2).
- **Numbers.** Folds up to 3; grids at most 8 by 8.
- **Home materials.** Scrap paper; a grown-up cuts any kit paper first.
- **Kit (KT11 `fold_squares`, exists as `fold_shapes`; 8 pieces to cut).** 6 paper squares (12 cm) and 2 strips. Contract: tasks use at most 4 squares and 1 strip; supplied 6 and 2. Nobody uses scissors during the lesson (a cut is drawn).
- **Figures.** Mirror-image options and fold-cut-unfold states up to three folds (X11), `panel` with a flip option (X17), `fold_punch` (exists, two folds).
- **Misconceptions.** A mirror image is a turned picture; a hole on the fold line; folding order mixed; up and down also swapped.
- **Needs.** X11, X17, RN7, KT11.

#### Lesson 22. Picture Patterns

- **Big idea.** Every feature of a picture runs its own cycle.
- **Strand.** Picture patterns where each feature has its own cycle and a missing picture in a 3 by 3 grid by combine-and-remove are NOT IN (SASMO 19-2, 19-11, 20-3); growing pictures are At school level (patterns section 3.12). **Holiday boundary (H5):** H5 asked for the 50th shape in a circle, triangle, square pattern. Barred: that item. New: features in separate cycles, a bead cycle of 6, a combine-and-remove grid. **Black and white:** features are shape, number of dots, size, turn and fill pattern; colour never carries a feature.
- **Objective.** Name each feature's cycle, find the nth picture, complete a grid by its rule, count in a growing picture pattern. Think harder: a bead cycle; a grid rule. Go further: invent a grid.
- **Prerequisites.** None.
- **Remember (6 min).** (1) Continue circle, triangle, square, circle. (2) The 10th of a 3-picture cycle. (3) Spiral from H5: the remainder tells where you land.
- **Start here (6).** (1) Continue a repeating strip of pictures. (2) The next two pictures. (3) Name each feature's own cycle (shape, turn, number of dots). (4) A growing dot pattern: Figure 4. (5) Complete a table of figure and dots. (6) The 10th picture of a strip with a cycle of 3.
- **Think harder (4).** (1) Beads repeat in a cycle of 6 (circle, square, triangle, triangle, square, circle): the 100th bead is a triangle and the first 100 beads hold 34 triangles (V22.1). (2) A 3 by 3 grid whose third picture in each row is the first and second combined with the parts they share removed: find the missing picture (V22.2). (3) Dot-circle counts by position. (4) Which of four pictures breaks the pattern.
- **Go further (3).** G1 **Beyond (named): "Hidden Rule Grid".** Invent a 3 by 3 grid with a hidden rule and test it on a partner; the author checks by brute force that the rule is the only one that fits. Level note: picture-pattern puzzles are NOT IN. G2 The 12th figure of a growing picture. G3 Pose a bead-cycle question.
- **Non-routine.** PAT T (V22.1), LOG T (V22.2), CHAL G.
- **Numbers.** Cycles of 2 to 6; positions to 100.
- **Home materials.** Pencil.
- **Kit (KT12 `picture_tiles`, 15 tiles to cut).** 15 square tiles told apart by shape, number, size, turn and fill pattern. Contract: a 3 by 3 grid uses 9; supplied 15 (9 plus 6 spare); maximum used 9.
- **Figures.** `panel` (exists: shape, number, size, turn, pattern, hide), flip option (X17), `stick_pattern` and `objects` (exist).
- **Misconceptions.** Treating the features as one pattern; counting the cycle wrongly; an off-by-one in the nth picture.
- **Needs.** X17, KT12.

#### Lesson 23. Turns and Corners

- **Big idea.** Angles measure turning.
- **Strand.** MOE P3 angles: right angle, greater or smaller (p. 36); quarter, half and three-quarter turns, no degrees (degrees are Primary 4, p. 39). **No school-paper evidence for clock-hand angles (patterns section 5); this is the weakest lesson and has a swap option (D4).** **Holiday boundary (H8):** H8 asked, at o'clock times, whether the angle between the hands is smaller or bigger than a right angle (3 o'clock, 2 o'clock, each time from 1 to 11, 4 against 8 o'clock). Barred: every o'clock-angle item. New: turns of a person or robot, the minute hand's turn, quarter-hour times.
- **Objective.** Describe turns as a quarter, half or three-quarter turn, follow a sequence of turns, compare the angle between clock hands at quarter-hour times with a right angle. Think harder: a turn sequence; quarter-hour angles. Go further: the net result of many turns.
- **Prerequisites.** Lesson 15 helps (a right angle).
- **Remember (6 min).** (1) A quarter turn makes a right angle. (2) The minute hand at 12 and at 3. (3) Spiral from lesson 15: use the checker.
- **Start here (6).** (1) Act out a quarter turn to the right, facing the door. (2) A half turn. (3) Which turn takes the arrow from A to B (circle). (4) The minute hand moves from 12 to 3: what part of a turn. (5) From 12 to 6, and from 12 to 9. (6) How many quarter turns make a full turn.
- **Think harder (4).** (1) Facing the door: a quarter turn right, a half turn, a quarter turn left and three quarter turns right leave you a quarter turn to the right of the start (V23.1). (2) Between 12:00 and 5:45 at quarter-hour steps there are 24 times; the hands make an angle greater than a right angle at 11 of them, found by testing each clock with the checker (V23.2). (3) The hour hand moves how much of a turn in 3 hours. (4) True, false or not possible to tell about turns.
- **Go further (3).** G1 **Beyond (named): "Turning Robot".** A robot follows twelve turn commands; its final direction depends only on the net number of quarter turns, counted in fours (V23.1). Level note: net turns counted in fours is contest-style; angles in degrees are Primary 4. G2 Which of 3:00, 4:15, 6:30 and 9:00 show a right angle between the hands (3:00 and 9:00, V23.3). G3 Pose a turn puzzle.
- **Non-routine.** LOG T (V23.1), LIST T (V23.2), CTX G (directions without a compass).
- **Numbers.** Turns in quarters; clock times in 15-minute steps.
- **Home materials.** A real or toy clock; a toy for the robot.
- **Kit (KT13 `turn_kit`, 2 pieces to cut).** A direction disc and an arrow (the lesson also reuses the clock from lesson 9, KT5). Contract: tasks use 1 disc and 1 arrow; supplied 1 and 1.
- **Figures.** `clock` with sector (exists), arrows and turn diagrams (X10).
- **Misconceptions.** The hour hand sits on the number at half past; left and right swap when the robot faces the child; a half turn counted as one quarter.
- **Needs.** X10, KT5, KT13.

#### Lesson 24. Model Makers: Times As Many

- **Big idea.** A group can be "3 units".
- **Strand.** MOE P3 multiplication and division word problems (p. 35); drawing units is a method the syllabus does not name (pp. 13 to 14). The P3 papers set "times as many" in about 178 items from Weighted Assessment 1, so this lesson is late for school and the Start here exposure is already in lessons 3 and 6. **Holiday boundary (H4): the second largest overlap.** H4 had 4 times as many cards, 5 times as much (pen and bag), 96 cards with Ali 3 times Ben, ages in n years (Mei 8, mother 36; Ravi 7 and his sister 3, sum 30), a gift so two amounts are equal, 3 times as many marbles with a 20-marble gift, 120 stickers at 3 times, boys and girls, 2 jugs and 3 cups. Barred: all of these. **The plan's Go further "ages in 3 years" is H4's and is replaced.** New: three-unit chains, 4-bar models with a brace, "times as many" with a given difference, prices.
- **Objective.** Draw units for "times as many", solve with a total or a difference given, solve a chain of three. Think harder: with a difference; with a total. Go further: a chain.
- **Prerequisites.** Lesson 6 helps.
- **Remember (6 min).** (1) Draw a strip of 3 equal parts. (2) 4 x 24. (3) Spiral from H4: a part-whole strip.
- **Start here (6).** (1) Ravi has 7 stickers; Ali has 3 times as many (21, V3.4). (2) One unit known, two steps. (3) Three groups of 12. (4) A strip for "5 times as much as $3". (5) The pen costs $3 and the bag 5 times as much: how much more is the bag. (6) Shade the units.
- **Think harder (4).** (1) Dev has 5 times as many cards as Eli, 96 more: 4 units are 96, a unit is 24, together 144 (V24.1). (2) Mia and Noor have 72 beads; Mia has 3 times as many as Noor: 54 and 18, a difference of 36 (V24.4). (3) A pen costs $1.60, a ruler 3 times as much, a bag $2.40 more than the ruler: $7.20 (V24.5). (4) A four-bar model with a brace.
- **Go further (3).** G1 **Beyond (named): "Three in a Chain".** Tom, Sue and Rina have 117 stickers: Sue has 4 times as many as Tom and Rina twice as many as Sue; 13 units, a unit is 9: 9, 36 and 72 (V24.2). Level note: unit chains are Primary 4 to 5 model work; the arithmetic is Primary 3. G2 Two comparisons in one story. G3 Pose a times-as-many story and check it.
- **Non-routine.** CMP T (V24.1, V24.4), DIAG T, MULTI T (V24.5), CMP G (V24.2).
- **Numbers.** Multipliers 2 to 7; totals to 5000; money to $1000.
- **Home materials.** Strips of paper.
- **Kit (KT14 `unit_strips`, exists; 4 strips to cut).** 4 strips of 10 cells. Contract: the largest task uses 13 cells (1 + 4 + 8); supplied 40.
- **Figures.** `bar_model` with up to four bars and a brace (X14).
- **Misconceptions.** "3 times as many" read as 3 more; the unit confused with the total; the difference treated as the total.
- **Needs.** X14, KT14.

#### Lesson 25. Before and After

- **Big idea.** When something is added or removed, the model changes in a visible way.
- **Strand.** Before-and-after and unchanged-difference models, working backwards (methods the syllabus does not name; the arithmetic is Primary 3 to 4, pp. 35, 37). The P3 papers set BACK (126) and give-and-receive (EQ, 89) items in four terms. **Holiday boundary (H4):** H4 had Siti 54 more than Mei giving some to be equal, equal gifts so one has twice as much, weeks to catch up, 3 times as many then a gift. Barred: those. New: the gap shrinks by twice a gift, the sum stays, paid and change.
- **Objective.** Draw before-and-after strips, see that a gift changes the gap by twice the gift, work backwards from change. Think harder: gifts; paid and change; unchanged sum. Go further: when two people end equal.
- **Prerequisites.** Lesson 6 helps.
- **Remember (6 min).** (1) 150 take away 40. (2) Draw two strips with a gap. (3) Spiral from H4: give and get.
- **Start here (6).** (1) After giving 35 he has 90; how many at first. (2) After getting 50 and giving 20 she has 130. (3) Draw the after strip. (4) Both children get $5: does the difference change (circle Yes or No). (5) Undo two steps in order. (6) A story with a total that stays the same.
- **Think harder (4).** (1) Ali has 150 more cards than Ben and gives Ben 40: he now has 70 more (V25.1). (2) Ben pays $100 for 4 caps and a $14.80 bag and gets $13.20 change: a cap costs $18 (V25.2). (3) Ali and Ben have 90 stickers; Ali has 40 more; after Ali gives Ben some, Ali has 20 more; he gave 10 (V25.3). (4) A three-step story to undo.
- **Go further (3).** G1 **Beyond (named): "Gap After the Gift".** With a gap of 150, Ali must give 75 for them to be equal: the gap falls by 2 for each 1 given (V25.4). Level note: contest move. G2 A two-change story with a check. G3 Pose a story where a gift of 8 leaves a gap of 14.
- **Non-routine.** BACK T (V25.2), EQ T (V25.1, V25.3), EQ G (V25.4).
- **Numbers.** Amounts to 2500; gifts 14 to 900; money to $100.
- **Home materials.** None special.
- **Kit.** None cut.
- **Figures.** `bar_model` before and after with a transfer arrow (exists) and a removed segment (X14).
- **Misconceptions.** The gap shrinks by the gift, not twice it; undoing in the original order; ignoring the unchanged sum.
- **Needs.** X14.

#### Lesson 26. Magic Totals

- **Big idea.** When a number belongs to several lines, it counts several times.
- **Strand.** Magic squares, shape sums and bounds are NOT IN (SASMO 19-24, 20-24); one equal-sum grid appears in the P3 papers. **Holiday boundary (H2):** H2 had a magic square from 1000 to 1800 and number pyramids. Barred: those two. New: shapes where a cell lies on several lines (a plus, a triangle of circles), possible and impossible totals.
- **Objective.** Complete a line to a given total, explain a magic total from the sum of all the numbers, count the shared cell extra, find possible and impossible totals. Think harder: the plus shape; the 3 by 3 square. Go further: which totals cannot be made.
- **Prerequisites.** None.
- **Remember (6 min).** (1) Split 15 into three numbers. (2) 1 + 2 + ... + 9 = 45. (3) Spiral from H2: complete a magic square.
- **Start here (6).** (1) Complete a 3 by 3 magic square (total 15) with four numbers given. (2) Check one row. (3) Which number is missing from a line. (4) The three rows use all of 1 to 9, which add to 45: why each row is 15 (V26.4). (5) Complete a line to a given total. (6) A square that is not magic: circle the bad line.
- **Think harder (4).** (1) Put 2, 4, 6, 8 and 10 in a plus of five circles so both lines of three have the same total: the middle must be 2, 6 or 10 and the totals are 16, 18 and 20 (V26.2). (2) Why the middle number is counted twice. (3) The 3 by 3 magic square from 1 to 9: there are 8 arrangements and 5 is always in the middle (V26.3). (4) Can the total be 14.
- **Go further (3).** G1 **Beyond (named): "Which Totals Are Impossible".** Put 1 to 9 once each in nine circles, three corners and six on the sides, four to a side, so that all three sides have the same total: the totals 17, 19, 20, 21 and 23 can be made, 18 and 22 cannot (V26.1). Level note: shape sums are NOT IN. G2 Design a magic figure. G3 Explain why the total must be a multiple of 3 plus the corner sum.
- **Non-routine.** LOG T (V26.2), LOG G (V26.1), CHAL G.
- **Numbers.** Numbers 1 to 10; totals to 30.
- **Home materials.** Pencil.
- **Kit (KT15 `number_tokens`, 18 tokens to cut).** Two sets of 1 to 9 (15 mm squares, 6 and 9 underlined). Contract: the Explore uses one set at a time, two pairs share a second; supplied 18, maximum used 18. The figure mats are printed and not cut.
- **Figures.** `circle_fig` (X12), `table` (exists).
- **Misconceptions.** Ignoring the shared cell; equal sums on some lines only; trial and error without a bound.
- **Needs.** X12, KT15.

#### Lesson 27. Fractions Everywhere

- **Big idea.** Fractions belong to measures, not only pictures.
- **Strand.** MOE P3 fractions (p. 35) in length, volume, time and money (whole units only); a fraction of a set is Primary 4 (p. 37). **Holiday boundary (H6):** H6 had a book read in 1/4 and 1/2, a jug 5/6 full with 1/2 poured out, and five pieces to fill a whole. Barred: those. New: unit fractions of a metre, kilogram, litre, hour and dollar as conversions, a missing fraction in a story.
- **Objective.** Convert a fraction of a unit (3/4 m = 75 cm), add related fractions of a litre, find the missing fraction. Think harder: related sums in a litre; time. Go further: a fraction of a set.
- **Prerequisites.** Lesson 7 helps.
- **Remember (6 min).** (1) Half a metre in cm. (2) A quarter of an hour in minutes. (3) Spiral from lesson 7: simplest form.
- **Start here (6).** (1) 3/4 m in cm (75). (2) 2/5 km in m (400). (3) 5/8 kg in g (625). (4) 3/10 l in ml (300). (5) 3/4 hour in minutes (45). (6) 1/5 of $1 in cents (20). (All V27.1.)
- **Think harder (4).** (1) A jug holds 3/4 l and 1/2 l is poured out: 1/4 l is left (V27.3). (2) A cake: 1/3 and 1/4 are eaten: 5/12 is left (V27.2). (3) Half an hour and 1/4 hour together. (4) Cut a 1 m ribbon into 5/8 and the rest.
- **Go further (3).** G1 **Beyond (named): "Half of a Dozen".** A fraction of a set: 3/4 of 24 sweets is 18 (V27.2). Level note: a fraction of a set is Primary 4 (p. 37). G2 The missing fraction in a story. G3 Pose a story with a fraction of a measure.
- **Non-routine.** CTX T (V27.1), MULTI T, CMP G, EQ G.
- **Numbers.** Denominators 2, 3, 4, 5, 8, 10, 12 of whole units.
- **Home materials.** A measuring jug.
- **Kit.** No new kit (reuse the fraction strips of lesson 7).
- **Figures.** `fraction` strip and line (X4), `jug` (X6).
- **Misconceptions.** 3/4 m as 34 cm; 1/4 hour as 25 minutes; adding denominators.
- **Needs.** X4, X6.

#### Lesson 28. Jugs, Scales and Balances

- **Big idea.** Unequal containers can still measure.
- **Strand.** MOE P3 volume (p. 36); pouring puzzles are NOT IN. **Holiday boundary (H9):** H9 had "get exactly 100 ml with a 300 ml and a 500 ml cup" (the same puzzle as 3 l and 5 l to 1 l) and the half-poured bottle. Barred: that pair and the plan's "3 l and 5 l jugs to measure 1 l". New: other jug pairs and counting the moves.
- **Objective.** Fill, empty and pour to measure an amount and count the moves; use a balance with a weight. Think harder: a pair that works in two moves. Go further: a pair that needs six.
- **Prerequisites.** Lesson 12 helps.
- **Remember (6 min).** (1) 1 l = 1000 ml. (2) A jug half full. (3) Spiral from H9: ml and l.
- **Start here (6).** Real-container tasks (a cup and a jug): (1) fill the cup and pour into the jug. (2) How much is left in the jug. (3) Three cups fill the jug. (4) Read the level in a drawn jug. (5) Pour into a drawn second jug. (6) Which jug is fuller.
- **Think harder (4).** (1) Jugs of 5 l and 8 l: measure exactly 3 l in 2 moves (fill the 8, pour into the 5; V28.1). (2) A tank poured out in steps, undo them. (3) Draw the state of both jugs after each move. (4) A balance with a 500 g weight.
- **Go further (3).** G1 **Beyond (named): "Fewest Moves".** Jugs of 4 l and 7 l: measure 6 l in 6 moves; 5 l takes 8 moves (V28.1). Level note: pouring puzzles are contest-style. G2 Which amounts can the 4 l and 7 l jugs measure. G3 Pose a jug puzzle.
- **Non-routine.** BACK T, DIAG T, GC G (V28.1), DIAG G.
- **Numbers.** Jugs of 3 to 9 l; amounts to 9 l.
- **Home materials.** Two cups or bottles of different size, a bowl and rice or water.
- **Kit.** None cut; a printed pour mat.
- **Figures.** `jug` (X6).
- **Misconceptions.** Pouring more than fits; fills and empties not counted as moves; forgetting that a pour stops when one jug is full or empty.
- **Needs.** X6.

#### Lesson 29. Who Sat Where?

- **Big idea.** Clues eliminate; they never guess.
- **Strand.** Logic grids, ordering chains and four-person puzzles are NOT IN; true, false or not possible to tell is common in the P3 papers (34 items, from 2020). **Holiday boundary (H10):** H10 had three people and three pets, Ali not first with Ben just behind Siti, the kueh with one liar, four readers with 8, 11, 13 and 15 books, and "make up a puzzle with 3 people and 3 things". Barred: those. New: four people in a row, negative clues, a check that the answer is unique.
- **Objective.** Solve a four-person seating puzzle with positive and negative clues, test that the answer is the only one, judge statements. Think harder: seating; statements. Go further: uniqueness.
- **Prerequisites.** None.
- **Remember (6 min).** (1) Order three children by two clues. (2) An end seat. (3) Spiral from H10: ticks and crosses.
- **Start here (6).** Three children in a row with objects (three clues), then four children with two clues given and two to use, a tick-and-cross grid, "who is at the end".
- **Think harder (4).** (1) Four children in a row. Ben sits at one end. Ali sits next to Ben. Ali does not sit next to Cara. Ali sits somewhere to the left of Ben: the row is Cara, Dev, Ali, Ben (V29.1). (2) Ali has 20 more stickers than Ben and Ben has 15 more than Cara; true, false or not possible to tell: Ali has 35 more than Cara (true); Ali has more than 50 (not possible to tell: with Cara on 1, Ali has 36; with Cara on 100, 135; V29.3). (3) A grid with ticks and crosses. (4) Which clue was not needed.
- **Go further (3).** G1 **Beyond (named): "Is It the Only Answer?".** Leave out each of the four clues in turn: the answer stops being unique every time (V29.2). Level note: uniqueness is contest-style. G2 Write a four-person puzzle with exactly one answer. G3 One clue is false: find which.
- **Non-routine.** LOG T (V29.1), EXP T (V29.3), LOG G (V29.2), EXP G.
- **Numbers.** Four people, four seats; differences to 100.
- **Home materials.** Pencil.
- **Kit (KT16 `clue_cards`, 8 cards to cut).** 8 clue cards and 4 name cards. Contract: the Explore uses 6 clue cards; supplied 8. Printed 4 by 4 mats (not cut).
- **Figures.** `table` with tick columns (X18).
- **Misconceptions.** Stopping at the first fit; "next to" read as "right of"; "left of" read as "next to"; guessing.
- **Needs.** X18, KT16.

#### Lesson 30. The Playground Plan, and Mi's Challenge Quest

- **Big idea.** Constraints make design a puzzle.
- **Strand.** Project and review of lessons 13, 14, 16, 24: area, perimeter, money, measurement. **Holiday boundary (H7):** none new; barred: H7's gardens and rectangle lists.
- **Objective.** Plan a playground within a perimeter and a cost; find the plan with the biggest area and prove it. Think harder: stay within perimeter and cost. Go further: prove the best.
- **Prerequisites.** None (a review).
- **Remember (6 min).** (1) Perimeter and area of a rectangle. (2) Cost of a fence. (3) Read a bar.
- **Start here (6, 25-minute workbook).** Fit shapes on a grid, perimeter of a plan, area, cost of a fence, a bar reading.
- **Think harder (4).** A plan within a perimeter and a cost; a fence with a gate gap; a table of plans; compare two plans.
- **Go further (3).** G1 **Beyond (named): "Biggest Playground".** With 24 m of fence and whole-metre sides, list all six rectangles and see that 6 m by 6 m, 36 m2, is the biggest (V30.1). Level note: exhaustive checking is contest-style. G2 A cost problem with two materials. G3 Pose a rule for a new playground.
- **Non-routine.** GEO T, MULTI T, CMP T, CHAL G (V30.1).
- **Home materials.** Squared paper.
- **Kit (KT17 `plan_pieces`, 12 pieces to cut).** 12 rectangles to place on a printed squared page. Contract: tasks use at most 10; supplied 12.
- **Quest (lesson 30).** Gates in section 8.
- **Needs.** X8, KT17, TL3.

### 1.5 Term 4: Structure, counting and showcase (lessons 31 to 40)

Can a new child join cold? Yes: the warm-up covers a table fact with a remainder (share 17 sweets among 5), counting by gaps, reading a clock, one fold or mirror and one "times as many" strip; lesson 32 re-teaches share-and-remainder in its first 5 minutes. Holiday graduates revisit remainders (H5, 32), column logic (H2, 38), logic-grid habits (H10, 38 and 39) and fraction-wall equivalences (H6, 36) in the first six minutes only. End-of-year school exams often fall in this term [UNVERIFIED for the actual year]; Term 4 is often shorter than 10 weeks [UNVERIFIED], and if it is, lesson 39 is the one to drop. **Safest to skip or make up: lesson 36** (brackets are Primary 5; no school evidence; nothing later depends on it). Lesson 40 is the public showcase and the year Quest and should not be missed.

#### Lesson 31. Factors, Multiples and Tests

- **Big idea.** Every number is a rectangle in waiting, and its digits can tell you about the 3s.
- **Strand.** Factors and multiples are Primary 4 (p. 37); the digit-sum test for 3 and "2 and 3 means 6" are NOT IN (SASMO 19-8, 19-14, 20-9); the P3 papers set a "divisible by 9" riddle now and then (Some). **Holiday boundary (H3, H5):** H3 had the digit sums of the 9s table, "divisible by 7 and digits add to 10", numbers 1 to 200 divisible by both 6 and 9, sweets shared among 6, 9 and 4, "divisible by 7 and 9, digits add to 9"; H5 had common remainders. Barred: all of these. New: factor pairs from arrays, the test for 3, "2 and 3 means 6", digits that fit a gap, numbers with exactly 3 or 4 factors. Start here stays pre-formal: arrays and "can it be shared equally".
- **Objective.** Find all the factors of a number by arranging tiles in rectangles, test divisibility by 3 with the digit sum, use "2 and 3 means 6". Think harder: all the factors; the test; digits in a gap. Go further: numbers with exactly 3 factors.
- **Prerequisites.** Lesson 4 (remainder zero).
- **Remember (6 min).** (1) 4 x 6 as a rectangle of tiles. (2) 54 in bags of 6, none left. (3) Spiral from lesson 4: a remainder of 0 means it divides exactly.
- **Start here (6).** (1) Arrange 12 tiles in rectangles: 1 by 12, 2 by 6, 3 by 4 (V31.4). (2) Which numbers can be shared equally among 4. (3) Is 36 in the 4s table. (4) List the multiples of 6 up to 60. (5) Is 48 in the 6s table. (6) Draw all the rectangles for 16 tiles.
- **Think harder (4).** (1) The factors of 36: there are 9 (V31.3). (2) Three-digit even numbers in the 3s table whose hundreds digit is twice the tens digit: 210, 216, 420, 426, 630, 636, 840, 846 (V31.1). (3) A 4-digit number 6 [] 3 [] with both blanks the same digit and in the 3s table: 6030, 6333, 6636, 6939, by the digit-sum test (V31.2). (4) True, false or not possible to tell: a number in the 6s table is also in the 2s and 3s tables.
- **Go further (3).** G1 **Beyond (named): "Three Factors Only".** The numbers under 50 with exactly three factors are 4, 9, 25 and 49; the first six numbers with exactly four factors are 6, 8, 10, 14, 15 and 21 (V31.3). Level note: factors are Primary 4. G2 Which digits fit a gap so that the number is in the 6s table. G3 Pose a riddle with two conditions.
- **Non-routine.** LOG T (V31.1, V31.2), EXP T, PAT G (V31.3).
- **Numbers.** Factors of numbers to 60; digit sums to 36; 4-digit numbers.
- **Home materials.** The 24 square tiles of lesson 13 (keep), pencil.
- **Kit.** No new kit (reuse `square_tiles`; contract: tasks use at most 24 tiles, larger numbers are drawn).
- **Figures.** `array`, `table` (exist).
- **Misconceptions.** Leaving out 1 and the number itself; factor and multiple swapped; "digit sum divisible by 3" applied to the digits one by one.
- **Needs.** None beyond the existing tools.

#### Lesson 32. Cycles and Remainders

- **Big idea.** A cycle repeats, so the remainder tells where you land.
- **Strand.** MOE P3 division with remainder revisited (p. 35); counting multiples in a range and "4s or 6s" overlap are contest moves (SASMO 19-14, 20-5); least boxes is a stock P3 item (about 35). **Holiday boundary (H5):** H5 had the 50th shape of a circle, triangle, square cycle, the day of the week 100 days from Monday, 100 people crossing a river 9 at a time, and several remainder riddles. Barred: those. New: counting multiples in a range, the overlap of the 4s and 6s, a weekday after 95 days from a Thursday, last digits of repeated products, most you can buy and fewest boxes with larger numbers.
- **Objective.** Use the remainder to find the nth item in a cycle, count multiples in a range by dividing, count a union once, find the last digit of a repeated product. Think harder: cycles; ranges; unions. Go further: last digits; round up and round down.
- **Prerequisites.** Lesson 4.
- **Remember (6 min).** (1) 17 sweets among 5 children, 3 each and 2 left. (2) Continue a repeating pattern. (3) Spiral from lesson 4: the remainder is smaller than the divisor.
- **Start here (6).** (1) Continue a pattern of 4 pictures. (2) The 9th picture. (3) The day 10 days after a Monday. (4) Full boxes of 8 from 60 eggs. (5) 29 divided by 7. (6) List the multiples of 6 up to 60.
- **Think harder (4).** (1) Today is Thursday: 95 days later it is a Monday (V32.3). (2) How many multiples of 7 are there from 40 to 150: 150 divided by 7 is 21, take away the 5 below 40: 16 (V32.2). (3) How many numbers from 1 to 120 are in the 4s or the 6s table: 40, counting the common ones once (V32.1). (4) The last digit of 3 multiplied by itself over and over: eight 3s end in 1 (V32.6).
- **Go further (3).** G1 **Beyond (named): "Last Digit Loop".** The last digit of twenty 3s multiplied together is 1, and of twenty-five 7s is 7 (V32.4). Level note: contest-style cycles. G2 Round up and round down: 1250 sweets in boxes of 8 need 157 boxes; $100 buys 14 books at $7 (V32.5). G3 Pose a remainder story.
- **Non-routine.** LOG T (V32.3), PAT T (V32.6), GC G (V32.5).
- **Numbers.** Cycles of 2 to 8; ranges to 150; dividends to 1250; divisors 2 to 9.
- **Home materials.** A calendar page.
- **Kit (KT18 `pattern_cards`, 12 cards to cut).** 12 pattern cards (circle, square, triangle, four of each, told apart by fill pattern). Contract: tasks lay out at most 12; supplied 12.
- **Figures.** `seq`, `calendar`, `objects` (exist).
- **Misconceptions.** Remainder 0 means the last item of the cycle, not the first; off by one at the ends of a range; the start counted twice.
- **Needs.** KT18.

#### Lesson 33. Counting Carefully

- **Big idea.** A list that is organised cannot miss one.
- **Strand.** Combinations, tree diagrams, banned pairs, posts on a ring and rectangles by size are NOT IN (SASMO 19-6, 19-16, 20-14, 20-18); combinations are set as whole tasks from 2025 (Tao Nan WA2, three tasks) and by Nanyang from 2021. **Holiday boundary (H10):** H10 had 6 children shaking hands, squares of any size in a 3 by 3 grid and the 3rd from the front and 5th from the back of a queue. Barred: handshakes (**the plan's "handshakes if time" is H10's and is dropped**), squares of any size in a 3 by 3 grid, queue counting. The line version of posts and gaps moved to lesson 11; this lesson keeps the ring.
- **Objective.** List outfits and teams, use a banned pair, count trees round a plot, count rectangles by size. Think harder: outfits; teams; a banned pair. Go further: a ring; rectangles.
- **Prerequisites.** Lesson 11 (posts), lesson 3 (multiplication).
- **Remember (6 min).** (1) List 2 hats with 3 scarves. (2) Posts and gaps on a line. (3) Spiral from H10: list in order.
- **Start here (6).** (1) Outfits from 2 hats and 3 scarves (6, V33.5). (2) Multiply two stages. (3) A menu of 2 mains and 3 drinks. (4) List the pairs of 3 children. (5) Finish a tree diagram. (6) Complete a table of outfits.
- **Think harder (4).** (1) 3 hats and 4 scarves make 12 outfits (V33.1). (2) Five children pick a team of 2: 10 teams, listed; 3 from 5 is also 10 (V33.1). (3) 5 shirts and 4 pairs of shorts, one pair never worn together: 19 outfits (V33.2). (4) Rectangles of any size in a 2 by 3 grid: 18 (V33.3).
- **Go further (3).** G1 **Beyond (named): "Count the Rectangles".** A 3 by 3 grid holds 36 rectangles and a 2 by 4 grid holds 30 (V33.3): choose two of the vertical lines and two of the horizontal lines. Level note: contest-style. G2 Trees round a square plot, 7 on each side with one at every corner, number 24; a ring track of 72 m with a lamp every 6 m has 12 lamps (V33.4). G3 Pose a counting question.
- **Non-routine.** WAYS T (V33.1, V33.2), LIST T, DIAG G (V33.4).
- **Numbers.** 3 to 5 choices per stage; selections of 2 or 3; grids to 3 by 4.
- **Home materials.** Pencil.
- **Kit (KT19 `outfit_cards`, 16 cards to cut).** 3 hats, 4 scarves, 5 shirts, 4 pairs of shorts. Contract: the Explore uses hats and scarves (7), the banned-pair task uses shirts and shorts (9); supplied 16.
- **Figures.** `table`, `grid` (exist), ring posts (X9), tree diagram (X16, optional).
- **Misconceptions.** Counting A with B and B with A as two teams; forgetting the banned pair; four corners counted twice (28 trees instead of 24).
- **Needs.** X9, KT19.

#### Lesson 34. Counting Digits and Pages

- **Big idea.** Count by place, not by number.
- **Strand.** Digit-restricted counting and digit appearances over a range are NOT IN (SASMO 19-23, 20-10). **Holiday boundary (H1): H1 held the plan's items.** H1 had how many times the digit 5 is written from 1 to 100, the digits needed to number pages 1 to 120, digit-card numbers (greatest even, smallest odd, the cards 1, 1, 0, 0), 3-digit numbers from 2, 4, 6, 8 and palindromes between 3000 and 4000. Barred: all of these; **"pages 1 to 130" in the plan (282 digits, V34.4) is H1's page item with a new number and is dropped, and so is the catalogue's digit-card build (EX-LIST-1)**. New: numbers using only even digits and the nth of them, a digit counted over 1 to 150, pages recovered from the digits used.
- **Objective.** List numbers whose digits all come from a set, in order, and find the nth; count how often a digit is written over a range; recover the number of pages from the digits used. Think harder: the nth number; a digit over a range. Go further: pages from digits.
- **Prerequisites.** Lesson 1 (place value).
- **Remember (6 min).** (1) Place value of 4-digit numbers. (2) List in order. (3) Spiral from H1: count the 1s written in 1 to 20.
- **Start here (6).** (1) List the 2-digit numbers that use only 1, 2 and 3. (2) How many 2-digit numbers use only odd digits. (3) The 5th positive number that uses only even digits (20, since 2, 4, 6 and 8 come first and zero cannot lead; V34.6). (4) The digits needed for pages 1 to 12 (15, V34.7). (5) A table of how many 1-digit, 2-digit and 3-digit numbers there are and their digits. (6) The digits used to write all the numbers from 1 to 20 (31, V34.7).
- **Think harder (4).** (1) The 40th positive number that uses only even digits is 260 (V34.1). (2) The digit 3 is written 35 times from 1 to 150 (V34.3). (3) List the 2-digit numbers with only even digits in order (20 of them, V34.8). (4) Pages 1 to 25 need 41 digits (V34.7).
- **Go further (3).** G1 **Beyond (named): "Pages from Digits".** A book's page numbers use 192 digits in all: it has 100 pages (V34.2). Level note: contest-style. G2 The sum of all the digits written on pages 1 to 30 is 168 (V34.5). G3 Pose a digit-counting question.
- **Non-routine.** LOG T (V34.1), LIST T, CHAL G (V34.2).
- **Numbers.** Numbers to 3 digits; ranges to 150; digit counts to 300.
- **Home materials.** Pencil.
- **Kit (KT20 `digit_cards`, 20 cards to cut).** Two sets of 0 to 9 (6 and 9 underlined). Contract: tasks use one set at once; supplied 20. Reused in lessons 36 and 38.
- **Figures.** `table`; `column` for digit sums (X1).
- **Misconceptions.** A leading zero; 100 counted as two digits; the digit 3 counted once in 33.
- **Needs.** KT20, X1.

#### Lesson 35. Timetable Puzzles

- **Big idea.** Try both orders, then compare.
- **Strand.** Timetables, durations, scheduling with fixed show times, a sequence with a 7-day cycle (SASMO 19-10, 19-13, 20-7); time itself is P3 (p. 36). **Holiday boundary (H9):** H9 had a school timetable (five 35-minute lessons and a 20-minute recess), a bus every 25 minutes, a station clock 10 minutes fast, an overnight train and a shop open 09:30 to 21:00. Barred: those. New: two films at fixed times in both orders, a falling daily reading pattern, a three-leg journey with a delay.
- **Objective.** Read a timetable, find durations, schedule two shows with a gap, try both orders. Think harder: both orders; days left. Go further: a three-leg journey with a delay.
- **Prerequisites.** Lesson 9.
- **Remember (6 min).** (1) The time from 9:15 to 10:40. (2) A 24-hour time to 12-hour. (3) Spiral from lesson 9: a slow watch.
- **Start here (6).** (1) Read a bus timetable. (2) The next bus after 8:20. (3) The length of a bus ride. (4) The arrival time. (5) Which show ends first. (6) A timetable with a break: the duration.
- **Think harder (4).** (1) Film P starts at 10:00 am or 12:30 pm and lasts 2 h 10 min; film Q starts at 11:00 am or 1:45 pm and lasts 1 h 50 min; Ali sees both with at least 15 minutes between: only P then Q works, finishing at 3:35 pm (V35.1). (2) Days left to finish a book when the pages read each day fall by 2. (3) A timetable with a break: the duration. (4) The start from the end across noon.
- **Go further (3).** G1 **Beyond (named): "Both Orders".** Three errands with fixed opening times: decide which orders are possible and compare finish times. Level note: scheduling is contest-style. G2 A three-leg journey with a delay and every order checked. G3 Pose a timetable puzzle.
- **Non-routine.** BACK T, MULTI T, TAB T (V35.1), CMP G, CTX G.
- **Numbers.** Times to the minute; durations to 6 h 45 min.
- **Home materials.** The clock from lesson 9 (keep).
- **Kit (KT21 `show_cards`, 6 cards to cut).** 4 show cards and 2 film cards. Contract: tasks use all 6; supplied 6. Reuses the clock (KT5).
- **Figures.** `table` timetable style (X13), `clock` (exists), a time line (`number_line` labels).
- **Misconceptions.** The gap added to the wrong film; 1:45 pm read as 2:45; assuming one order only.
- **Needs.** X13, KT21, KT5.

#### Lesson 36. Target Practice

- **Big idea.** Operations are tools; brackets say which goes first.
- **Strand.** Mixed operations with brackets are Primary 5 (p. 41), a two-year preview that overlaps Level 4 and Level 5 lesson 1; no school-paper evidence. **Holiday boundary:** none (H2 used digit cards for sums only). Start here is pre-formal: "do the bracket first" with + and - only, never the order of operations without brackets.
- **Objective.** Reach a target number from four cards with + - x and ÷, brackets showing the order. Think harder: x and brackets; a bracket that changes the answer. Go further: every number from 1 to 10.
- **Prerequisites.** None.
- **Remember (6 min).** (1) A subtraction chain from left to right. (2) 4 x 6 and 24 / 4. (3) Spiral from lesson 2: check by the opposite.
- **Start here (6).** (1) Reach 12 from 2, 3 and 7 with + and -. (2) Work (8 - 5) + 4. (3) Fill the missing sign. (4) Work (6 + 4) - 3. (5) Reach 10 from three numbers. (6) Where does the bracket go to make 9.
- **Think harder (4).** (1) Reach 24 from the cards 2, 3, 5 and 8 using each once, with brackets (it can be done, V36.1). (2) Put the brackets in 12 - 4 x 2 so that it equals 16 ((12 - 4) x 2 does; 12 - (4 x 2) is 4; V36.2). (3) True or false: (8 - 3) x 2 = 8 - (3 x 2). (4) Reach 17.
- **Go further (3).** G1 **Beyond (named): "Make Every Number".** With the cards 2, 3, 5 and 8, each number from 1 to 10 can be made, and 24 too (V36.1). Level note: brackets are Primary 5 (p. 41). G2 Pick any four cards from 1 to 9 and find which of the targets 1 to 10 you can make. G3 Pose a target puzzle for a partner.
- **Non-routine.** GC T, EQ T, LOG G (V36.1).
- **Numbers.** Cards 1 to 9; four cards; targets to 30.
- **Home materials.** The digit cards of lesson 34 (keep).
- **Kit (KT22 `operator_tiles`, 16 tiles to cut, optional).** 3 each of + - x and ÷ (12) and 2 pairs of brackets (4). Contract: an expression uses 4 cards, 3 signs and 2 bracket pairs; supplied 12 and 4. If the owner prefers to cut the load, children write the signs in boxes (D10).
- **Figures.** `table` and boxes (exist).
- **Misconceptions.** Working left to right and ignoring the brackets; using a card twice; a division that does not come out whole.
- **Needs.** KT22 (optional), KT20.

#### Lesson 37. Most for the Least

- **Big idea.** With a fixed supply, more pieces beat bigger pieces.
- **Strand.** Guess, check and improve; most or fewest pieces for a fixed amount; fewest notes and coins; offers (about 45 P3 items). NOT IN as puzzles. **Holiday boundary (H9):** H9 had Ben's nine 20¢ and 50¢ coins worth $3. Barred: that. **The plan's "matchstick digits with exactly 17 sticks" is SASMO 2020 Q23's structure and is replaced** with digit stickers priced in ink units. New: priced digits, fewest notes and coins, animals' legs, offers under a budget.
- **Objective.** Find the most digits for a fixed supply, then the biggest number; the fewest notes and coins for an amount; two kinds of animal from heads and legs; the most items under a budget with offers. Think harder: all four. Go further: a second limit.
- **Prerequisites.** Lesson 8.
- **Remember (6 min).** (1) Make $13 from notes. (2) 18 animals with 4 legs each. (3) Spiral from lesson 8: an offer.
- **Start here (6).** (1) Make $37 with the fewest notes and coins. (2) Make 85¢. (3) Is 3 for $8 or 1 for $3 the cheaper way to buy 3. (4) 5 packets at $7. (5) Can $50 buy 7 books at $7. (6) The change from $100.
- **Think harder (4).** (1) Digit stickers cost 2 ink units for a 1, 3 for a 7, 4 for a 4 and 5 for any other digit; exactly 19 units buys at most 9 digits, and the biggest number is 711111111 (V37.1). (2) The fewest notes and coins for $186 is 7 (V37.2). (3) A zoo has ostriches (2 legs) and zebras (4 legs): 18 animals have 52 legs, so 8 zebras (V37.3). (4) $60 and the offers 1 for $3, 3 for $8, 7 for $17: the most items is 24 (V37.4).
- **Go further (3).** G1 **Beyond (named): "Most for the Least".** The sticker puzzle with a second limit: exactly 19 units and no 7: 8 digits, the biggest number 91111111 (V37.5). Level note: optimising under a fixed supply is contest-style. G2 The fewest notes and coins for $137 is 6 (V37.2). G3 Pose a stickers puzzle.
- **Non-routine.** GC T (V37.3), CTX T (V37.4), WAYS G.
- **Numbers.** Amounts to $200; 15 to 50 items; offers of 1 to 7.
- **Home materials.** Pencil.
- **Kit (KT23 `play_notes`, 15 pieces to cut).** $100 x 1, $50 x 2, $10 x 4, $5 x 2, $2 x 3 and $1 coin x 3, marked PLAY MONEY and told apart by size and label, not colour. Contract: the $186 task uses 7 pieces ($100, $50, three $10, $5, $1); supplied 15. Singapore has no $20 note. Whether play money may carry a stylised note design is an open legal question (D1 at Level 1, D13 here).
- **Figures.** `money` (exists; needs a $100 note), `table`.
- **Misconceptions.** Choosing the biggest digit instead of the most digits; counting the same animal twice; forgetting the change.
- **Needs.** KT23.

#### Lesson 38. Contest Lab

- **Big idea.** A calm method beats rushing.
- **Strand.** Mixed original problems in contest style: eliminate, estimate, check; possible or impossible from smallest and biggest totals; one short letter puzzle (SASMO 19-3, 19-24, 20-24, 19-25, 20-25). No exam skills are taught: no timed paper and no option elimination (g3 analysis section 7). **Holiday boundary (H2):** H2 had AB + B = BA, AA + BB = CBC, AA + BB + CC = ABC, ABC - CB = CAB and ABC + ACB = CBA. Barred: all letter-sum puzzles of that kind. New: a multiplication letter puzzle.
- **Objective.** Apply the routine (read, underline what is asked, estimate, solve, check) to a plain problem; decide whether a total is possible from the smallest and biggest; solve a short letter puzzle. Think harder: bounds; parity; a letter puzzle. Go further: two moves.
- **Prerequisites.** Lessons 2 and 6 help.
- **Remember (6 min).** (1) The routine in five words. (2) 2 + 3 + 4 as the smallest total of three different cards. (3) Spiral from lesson 2: check by adding back.
- **Start here (6).** The routine on a plain problem: (1) read and underline what is asked. (2) Estimate. (3) Solve a two-step story. (4) Check by another way. (5) Write the answer with its unit. (6) Tick the routine.
- **Think harder (4).** (1) Three different cards from 2 to 9: the total is at least 9 and at most 24, so 25 is impossible and 20 is possible (V38.1). (2) Five different odd numbers from 1 to 19: the total is odd and between 25 and 75, so 50 is impossible (V38.2). (3) AB x 7 = CAC with different letters for different digits: A = 4, B = 9, C = 3, since 49 x 7 = 343 (V38.3). (4) Find the error in a worked solution.
- **Go further (3).** G1 **Beyond (named): "Possible or Impossible".** A puzzle with three conditions decided from the smallest, the biggest and odd or even, before any listing. Level note: contest-style. G2 A two-move problem: bounds, then a list. G3 Design an impossible puzzle and prove it cannot be solved.
- **Non-routine.** LOG T (V38.1, V38.2), EXP T, MULTI T, CHAL G, CMP G.
- **Numbers.** Cards 1 to 9; totals to 100.
- **Home materials.** The digit cards of lesson 34.
- **Kit.** None new.
- **Figures.** `column` (X1), `circle_fig` (X12).
- **Misconceptions.** Listing before looking at the bounds; a letter standing for two digits; "none of the above" habits from five-option papers.
- **Needs.** X1, X12.

#### Lesson 39. Problem-Solving Studio

- **Big idea.** Choose the move before you pick up the pencil.
- **Strand.** Synthesis of the year's named moves (draw it, list it, table, pattern, work backwards, cases, count systematically); the P3 papers added error-analysis and posing items in 2024 (Rulang: explain the mistake, "what is the question if the answer is 139", "what if there are 8 shelves"). **Holiday boundary:** none.
- **Objective.** Match a plain problem to a move and solve it, choose a move when it is not named and say what was rejected, find the error in a worked solution, write a question for a given answer. Think harder: choose; error; question from the answer. Go further: what-if.
- **Prerequisites.** Lessons 6, 17, 25, 33 help.
- **Remember (6 min).** (1) Name three moves. (2) Draw a strip for "5 times as many". (3) Spiral from lesson 33: list the outfits.
- **Start here (6).** The move is named every time: (1) strip. (2) Table. (3) Work backwards. (4) List. (5) Pattern. (6) Draw it.
- **Think harder (4).** (1) Choose the move for a problem of a contest kind. (2) A bag costs $46.80, $12.30 less than a coat; a child says the coat costs $34.50: the mistake is taking away instead of adding, the coat costs $59.10 (V39.1). (3) Mei has 36 red, 24 blue and 15 green beads: write a question whose answer is 51 (red and green together; no other pair or difference gives 51, V39.2). (4) Say which move you rejected and why.
- **Go further (3).** G1 **Beyond (named): "Change One Number".** There are 6 boxes with 24 apples in each (144). What if there are 8 boxes (192)? What if each box has 20 apples (120)? Which change gives more (V39.1). Level note: posing and what-if are process skills (pp. 13 to 14). G2 Change one number in a problem so a different move is needed. G3 Pose a problem for the Fair.
- **Non-routine.** POSE T, EXP T (V39.1), POSE G (V39.1).
- **Numbers.** Within 1000; money to $200.
- **Home materials.** The tool cards.
- **Kit (KT24 `tool_cards`, exists; 15 cards to cut).** 7 tool cards and 8 problem cards. Contract: the Explore sorts 8 problems under 7 tools (two problems share a tool); supplied 15.
- **Figures.** `bar_model`, `table`, `number_line` (exist); tool icons (exist in `figs3`).
- **Misconceptions.** Choosing the tool by a keyword ("more" so add); using a tool for show; giving up after the first try.
- **Needs.** KT24.

#### Lesson 40. Mathematicians' Fair, and Mi's Challenge Quest

- **Big idea.** Posing a good problem is harder than solving one.
- **Strand.** Problem posing and presenting; spiral review of all four terms; processes (pp. 13 to 14). The Quest of the year. **Holiday boundary:** none.
- **Objective.** Choose a favourite idea of the year and teach it to the group in about a minute (a pass is always allowed); write a puzzle with a unique answer; swap and solve. Go further: a puzzle with a proof.
- **Prerequisites.** None: a look-back. A child who joins here does the Quest and the Fair on the ideas they know.
- **Remember (6 min).** Three "I remember" picks led by the tutor (a pattern, a way to add, a shape or a story); volunteers only.
- **Start here (5, light workbook of 25 minutes).** Show a favourite page and say one thing with a sentence frame; sort four year-cards into "I know it well" and "I am learning it". Not marked.
- **Think harder (3).** Write a problem with its solution for a new Level 3 child; swap with a partner and solve.
- **Go further (3).** G1 **Beyond (named): "Puzzle With a Proof".** Write a puzzle with a rule and show that the answer must be right (draw it, list every case, or check a second way); checklist: one answer, checked twice, not copied. G2 A family of problems from one rule (change one number). G3 Find what is wrong with a friend's puzzle.
- **Non-routine.** POSE T, POSE G, CHAL G, WAYS G.
- **Safeguarding.** Showing work is voluntary; no "best", no ranking, no votes; puzzles stay inside the group unless a grown-up agrees; presentations are recorded under the usual statement.
- **Home materials.** A favourite page from the year, plain paper, the Quest Log closed in its envelope, a quest partner.
- **Kit.** None.
- **Misconceptions.** A puzzle with two answers; the writer cannot solve it; a copied puzzle; a harder puzzle is not a better one.
- **Quest (lesson 40).** Minutes 35 to 55 after the break; the Fair follows in the Workbook and Talk parts; the exit ticket is not live. Gates in section 8.
- **Needs.** TL3, parent report line.

## 2. Terms at a glance

Waves (explained in section 13): A = can be written with the tools as they stand (kit only); B = needs the column and place-value figures (X1, X2, X3, X5); C = needs the measure, graph, post and timetable figures (X6, X7, X9, X13); D = needs the area and angle figures (X8, X10); E = needs fractions, models, balance, mirror and magic figures (X4, X11, X12, X14, X17, X18); Q = a Quest lesson, built last in its term. Codes X, KT, RN, TL are defined in section 5.

### Term 1

| # | Title | Wave | Blocking template items | Beyond (named) | Safe to skip? |
|---|---|---|---|---|---|
| 1 | Number Lines to 10 000 | B | X5, X2, KT1 | Halfway House | No, 2 and 34 use it |
| 2 | Write It Down, Check It | B | X1, X2 | Wrong on Purpose | No, 3 to 6 and 10 use it |
| 3 | Multiply by Splitting | B | X3, X1 | Product Detective | No, 4 and 6 use it |
| 4 | Divide It Up | B | X1, X2, X18, RN2 | Smallest and Biggest | No, 6, 10 and 32 use it |
| 5 | Mental Maths Moves | A | KT2 | Pair It Up | Safest in Term 1 |
| 6 | The Hidden Question | A | none (X14 optional) | Story That Cannot Work | No, 10 builds on it |
| 7 | Fractions on the Number Line | E | X4, X5, KT3, RN4 | Between Neighbours | No, 27 builds on it |
| 8 | Dollars and Cents | B | X1, KT4, RN5 | Exactly the Total | No, 10 builds on it |
| 9 | Time Detectives | C | X13, KT5 (exists) | Wrong Watch | No, 35 builds on it |
| 10 | Price per Piece (and the Quest) | Q | TL3 (Quest); X14 optional | Free Pen Price | No (holds the Quest) |

### Term 2

| # | Title | Wave | Blocking template items | Beyond (named) | Safe to skip? |
|---|---|---|---|---|---|
| 11 | Length and Distance | C | X9, X5, RN1 | Count the Gaps | Fairly safe |
| 12 | Mass and Volume | C | X6, X1, RN1 | Weighing Twice | Fairly safe |
| 13 | Fences and Floors | D | X8, X3, KT6 | Stretch One Side | No, 14 and 30 build on it |
| 14 | Cut, Slide, Count | D | X8, X3, KT7 | Half-Square Puzzle | Safest in Term 2 |
| 15 | Lines and Corners | D | X10, KT8 | Crossroads Count | Fairly safe |
| 16 | Bar Graphs that Tell Stories | C | X7, X18 | The Missing Scale | Fairly safe |
| 17 | Patterns That Grow | A | none | Where Two Patterns Meet | Fairly safe |
| 18 | Balance and Swap | E | X6, KT9 | Heaviest to Lightest | Fairly safe |
| 19 | Cube Stacks and Views | A | none (cube_stack exists) | Fewest and Most | Fairly safe |
| 20 | The Class Shop (and the Quest) | Q | TL3, X7, KT10 | Best Plan Proof | No (holds the Quest) |

### Term 3

| # | Title | Wave | Blocking template items | Beyond (named) | Safe to skip? |
|---|---|---|---|---|---|
| 21 | Fold, Flip, Mirror | E | X11, X17, RN7, KT11 | Fold Three Times | Fairly safe |
| 22 | Picture Patterns | E | X17, KT12 | Hidden Rule Grid | Fairly safe |
| 23 | Turns and Corners | D | X10, KT13 | Turning Robot | Safest in Term 3 |
| 24 | Model Makers: Times As Many | E | X14, KT14 | Three in a Chain | No, 25 builds on it |
| 25 | Before and After | E | X14 | Gap After the Gift | Fairly safe |
| 26 | Magic Totals | E | X12, KT15 | Which Totals Are Impossible | Fairly safe |
| 27 | Fractions Everywhere | E | X4, X6 | Half of a Dozen | Fairly safe |
| 28 | Jugs, Scales and Balances | E | X6 | Fewest Moves | Fairly safe |
| 29 | Who Sat Where? | E | X18, KT16 | Is It the Only Answer? | Fairly safe |
| 30 | The Playground Plan (and the Quest) | Q | TL3, X8, KT17 | Biggest Playground | No (holds the Quest) |

### Term 4

| # | Title | Wave | Blocking template items | Beyond (named) | Safe to skip? |
|---|---|---|---|---|---|
| 31 | Factors, Multiples and Tests | A | none | Three Factors Only | Fairly safe |
| 32 | Cycles and Remainders | A | KT18 | Last Digit Loop | Fairly safe |
| 33 | Counting Carefully | C | X9, KT19 | Count the Rectangles | Fairly safe |
| 34 | Counting Digits and Pages | B | X1, KT20 | Pages from Digits | Fairly safe |
| 35 | Timetable Puzzles | C | X13, KT21 | Both Orders | Fairly safe |
| 36 | Target Practice | A | KT22 (optional) | Make Every Number | Safest in Term 4 |
| 37 | Most for the Least | A | KT23 | Most for the Least | Fairly safe |
| 38 | Contest Lab | B | X1, X12 | Possible or Impossible | Fairly safe |
| 39 | Problem-Solving Studio | A | KT24 (exists) | Change One Number | Fairly safe |
| 40 | Mathematicians' Fair (and the Quest) | Q | TL3 | Puzzle With a Proof | No (holds the Quest) |

## 3. Holiday no-repeat register

The rule (owner, 22 Oct): all four terms are new content and holiday lessons are not reused; spiral review of a holiday topic is allowed in the first six-minute warm-up only. A holiday graduate starts Term 1 and must never meet a holiday item again. Overlap: Heavy = the term lesson is the same strand and the same kinds of item as a holiday lesson, so only the barred list and a new angle keep it new; Medium = shared strand with a different focus; Light = one item; None = no holiday counterpart. **Eleven lessons are Heavy: 2, 3, 4, 6, 7, 9, 12, 13, 14, 15, 23, 24, 25, 28, 29, 31, 32, 33, 34, 35** (twenty). The lesson authors must check every item against `p3/content/lN.js` before the wording review (a script that finds a 7-word overlap with those files is part of TL2).

| L | Closest holiday lesson and items | Overlap | Barred in the term lesson | What is new |
|---|---|---|---|---|
| 1 | H1 Number Sleuths (digit cards, listing, clue riddles, digit counts) | Medium | Greatest or smallest number from cards, digit-sum riddles, digits 1 to 100 | Number lines, midpoint, alternating steps, bounds |
| 2 | H2 Cryptarithm Crackers (missing digits, letters, pyramids) | Heavy | Letter sums, pyramids, magic squares, '7A03 - B46C' | The algorithm itself, zeros, estimates, error analysis; one boxed missing-digit item only |
| 3 | H3 Times Table Treasure (tables 6 to 9, last digits, 9s digit sums) | Heavy | Last-digit patterns, digit sums of 9s, 1 to 200 divisible by both 6 and 9 | Area model, 3-digit by 1-digit, times as many (Start here) |
| 4 | H5 Remainder Riddles (remainders in stories, two-divisor riddles) | Heavy | Riddles with two divisors, biggest 2-digit with remainder 8, 100 people in boats of 9 | Short division of 3-digit numbers, round up, true/false/NPT, bounds |
| 5 | H2 stretch (compensation, one item) | Light | 1099 for 1999 item | Pairing, stepping lists |
| 6 | H4 Model Makers (bar models, two-step) | Heavy | Ages in n years, pencil box and pens $25/$35, give-to-equal, ribbon in three | Hidden question, reversal trap, sum and difference, impossible stories |
| 7 | H6 Fraction Walls (wall, equivalents, compare, add) | Heavy | Order 2/3, 5/6, 7/12; 1/2+1/4+1/8; halfway between 1/4 and 1/2; the 5/6 jug | Number line, simplest form, parts to shade, fractions between 1/3 and 1/2 |
| 8 | H9 Measure and Money Masters (decimal money, change, coins) | Medium | $3.80 + $1.45 from $10; 9 coins worth $3; party planner | Offers, which two items, exact total with a count limit, all ways |
| 9 | H9 (24-hour, durations, station clock 10 min fast, night train) | Heavy | Station clock fast; 22:40 to 01:15; 09:30 to 21:00; bus every 25 min | Seconds, calendar cycles, slow and fast watches both ways |
| 10 | H4/H9 (simultaneous prices, unit prices) | Medium | Pencil box and 3 or 5 pens | Shared payment, free items, price per piece |
| 11 | H9 (compound lengths, 1 km 250 m walk, ribbon 80 cm longer) | Medium | Those three items | Benchmarks, ruler not at 0, posts and gaps, routes |
| 12 | H9 (3060 g, 4 l 500 ml, half-poured bottle, box of 4 books) | Heavy | Half-poured bottle (it is SASMO 20-13's move), box of books, 300 ml cups | Dials, jugs, balance with identical objects, two weighings |
| 13 | H7 Area Architects (the whole strand) | Heavy | 12 squares into every rectangle, area/perimeter 24 tables, corner cut-outs, 8 by 2 and a square, gardens, 2 cm tiles, 5 squares of 2 cm | Units, three shapes of one perimeter, identical parts, wire bent twice, stretched side |
| 14 | H7 (L-shape with a corner out, square cut in four) | Heavy | Any rectangle with a corner removed | Cut and slide, half squares, area of one tile, cost |
| 15 | H8 Angle and Line Detectives (checker, hash sign, letters, staircase) | Heavy | Clock angles at o'clock, 4 lines from a point, staircase, noughts-and-crosses grid | Drawing with the checker, lettered figures, arrowheads, street map, crossroads |
| 16 | H10 (bar graph reading, stamps graph, paper collection) | Medium | Stamps 35/20/15 more; 3P1 10 kg more than 3P2 | Scale removed, missing bar, double bars, key of 5 or 6, misleading scale |
| 17 | H10/H1 (5, 9, 13, 17; triangles in a row; 1, 3, 7, 15, 31; +7 from 1000) | Medium | Sticks for triangles, growing squares, doubling-plus-one, +7 | Seats round tables, growing gaps, operator rules, alternating, two patterns that meet |
| 18 | H4 (pencil box and pens, jugs and cups, sugar and flour) | Medium | Those three | Chained balances, a box used twice, baskets that differ by one item |
| 19 | none (H7/H8 are flat) | None | - | New topic |
| 20 | H9 party planner ($20, 8 friends, menu card) | Medium | That menu, budget and rules | A class shop with offers, a sales graph, a mass item |
| 21 | none | None | - | New topic |
| 22 | H5 (the 50th shape of a 3-cycle) | Light | The 50th of circle, triangle, square | Feature cycles, a 6-bead cycle, combine-and-remove grid |
| 23 | H8 (clock angles at o'clock: 3, 2, each from 1 to 11, 4 against 8) | Heavy | Every o'clock angle item | Turn sequences, the minute hand's turn, quarter-hour times |
| 24 | H4 (the second largest overlap: times-as-many, ages, equal after a gift) | Heavy | Ages in n years, 96 cards at 3 times, 3 times with a 20-marble gift, 120 stickers, boys and girls, jugs and cups | Unit chains, 4-bar models, prices, difference or total given. Plan's 'ages in 3 years' dropped |
| 25 | H4 (give-to-equal, equal gifts, weeks to catch up) | Heavy | Those items | Gap shrinks by twice a gift, unchanged sum, paid and change |
| 26 | H2 (magic square 1000 to 1800, pyramids) | Medium | Those two | Plus and triangle shapes, shared cells, impossible totals |
| 27 | H6 (book 1/4 and 1/2, jug 5/6, five pieces to a whole) | Medium | Those three | Fractions of measures, missing fraction, fraction of a set (P4 preview) |
| 28 | H9 (300 ml and 500 ml cups to get 100 ml) | Heavy | That pair and 3 l and 5 l to 1 l | Other jug pairs, counting moves (5 and 8; 4 and 7) |
| 29 | H10 (3 people 3 pets, Ali not first, kueh liar, 4 readers) | Heavy | Those four | 4 in a row, negative clues, uniqueness, T/F/NPT on differences |
| 30 | H7 (gardens, rectangle lists) | Medium | Those lists | Playground plan with cost and proof |
| 31 | H3/H5 (9s digit sums, divisible by 6 and 9 to 200, common remainders) | Heavy | Those items | Factor pairs from arrays, test for 3, '2 and 3 means 6', exactly 3 or 4 factors |
| 32 | H5 (50th shape, 100 days weekday, 100 people in boats) | Heavy | Those items | Multiples in a range, 4s or 6s, 95 days from Thursday, last digits |
| 33 | H10 (6 handshakes, squares in 3 by 3, queue counting) | Heavy | Handshakes, squares of any size in 3 by 3, queue counting | Outfits, teams, banned pair, ring, rectangles. Plan's handshakes dropped |
| 34 | H1 (digit 5 from 1 to 100, pages 1 to 120, digit cards, palindromes) | Heavy | Those items; the plan's pages 1 to 130; digit-card builds | Even-digit nth number, digit 3 over 1 to 150, pages from digits |
| 35 | H9 (school timetable, bus every 25 min, station clock, night train) | Heavy | Those items | Two shows in both orders, falling pattern, 3-leg journey |
| 36 | none (H2 used cards for sums) | None | - | Brackets (P5 preview) |
| 37 | H9 (9 coins worth $3) | Light | That item; the plan's matchstick digits with 17 sticks (SASMO 20-23) | Priced digit stickers, fewest notes, heads and legs, offers |
| 38 | H2 (AB+B=BA, AA+BB=CBC, AA+BB+CC=ABC, ABC-CB=CAB, ABC+ACB=CBA) | Medium | All those letter sums | A multiplication letter puzzle, bounds, parity |
| 39 | none | None | - | Choosing a move, error analysis, posing |
| 40 | none | None | - | Showcase |

Count: Heavy 20, Medium 12, Light 3, None 5.

## 4. Non-routine assignments (rebuilt from the Primary 3 catalogue)

**Why this section exists.** The owner decided on 23 Oct that every term plan names, for each lesson, the non-routine question types it carries, the tier (Think harder or Go further, never Start here) and original example items, with the spiral shown as a type-by-lesson matrix. The Level 3 plan's section of that name (lines 274 to 395 of `level_3_year_plan.md`) was written from the Primary 5 catalogue by mistake (headline finding 1) and cannot be used. This section replaces it. Source: `docs/books/p3_non_routine_catalogue.md` (1098 non-routine questions from 197 tests, 28 school labels, 2019 to 2025, 16 types; its per-type 'Where it belongs for us' lists) and `docs/books/p3_school_paper_patterns.md`. Examples are original and script-verified (appendix); no school text is copied.

How to read it. Types: CMP comparison (difference, sum, times as many, simultaneous prices); MULTI multi-step; BACK work backwards; EQ make equal or transfer; LOG number clues, ordering, missing digits; CTX unfamiliar context (offers, hidden fact, slow and fast watches); DIAG draw a model or diagram; GC guess and check, least or most; LIST systematic list; GEO area and perimeter reasoning; PAT pattern; EXP explain, true or false, not possible to tell; CHAL build a graph or answer from clues; WAYS how many ways; TAB table; POSE pose a question, what if, find the mistake. T = Think harder, G = Go further. Every entry is status N (planned; no Level 3 term lesson is written). The lesson's named Beyond puzzle (section 1) sits beside these types and takes one of the Think harder or Go further slots. Papers do not name the heuristic in the stem: a Think harder item may name the tool for a type new to that term, Go further drops it. 366 of the 1098 school items need the picture, so every picture-dependent item needs a drawn figure on the page (section 5).

### 4.1 Lesson by lesson

| # | Lesson | Non-routine types (tier): what (check) |
|---|---|---|
| 1 | Number Lines to 10 000 | LOG T: riddle on a line between 6400 and 6700 (V1.4); EXP T: true, false or not possible to tell about points on a line; PAT G: alternating steps (V1.3) |
| 2 | Write It Down, Check It | BACK T: a number plus 2583 is 6479 (V2.2); EXP T: find the slip in a worked column (V2.3); LOG G: two missing digits in a subtraction, one item (V2.4) |
| 3 | Multiply by Splitting | MULTI T: boxes, sales and packs (V3.2); EXP T: 6 x 48 = 6 x 50 - 6 x 2; TAB T: tricycle wheels; CMP T: times as many with a difference |
| 4 | Divide It Up | GC T: least number of buses, round up (V4.2); EXP T: true, false or not possible to tell about bags of 54 (V4.3); BACK T: dividend from quotient and remainder (V4.4); LOG G: smallest and biggest with remainder 5 (V4.5) |
| 5 | Mental Maths Moves | LIST T: pairs that make 1000 in a list (V5.5); EQ T: a balanced equation without adding both sides (V5.4); PAT G: total of a stepping list by pairing (V5.2, V5.6) |
| 6 | The Hidden Question | CMP T: reversal trap and sum and difference (V6.2); MULTI T: boxes, sale, packs (V6.4); BACK T: undo a story (V6.1); LOG G: a story that cannot work (V6.5) |
| 7 | Fractions on the Number Line | EQ T: missing numerator and parts to shade (V7.4); EXP T: same point on the line (V7.1); LOG G: fractions between two fractions (V7.5) |
| 8 | Dollars and Cents | CTX T: offers, exactly 11 pens (V8.2); LIST T: which two items make exactly $8.30 (V8.3); GC T: exactly $59 with a count limit (V8.4); WAYS G: all ways to pay $26 (V8.5) |
| 9 | Time Detectives | CTX T: slow watch (V9.4); BACK T: start from end and duration (V9.3); BACK G: fast watch read twice (V9.5); CMP G: two watches |
| 10 | Price per Piece (and the Quest) | CMP T: simultaneous prices (V10.2); CTX T: free items (V10.3, V10.4); TAB T: rate table; BACK T: price of one from paid and change; CTX G: free pen price (V10.5, V10.6) |
| 11 | Length and Distance | DIAG T: posts and gaps (V11.1, V11.2); GEO T: circuit (V11.4); CMP T: routes (V11.5); MULTI G: three-day distance (V11.3); DIAG G: gaps in time (V11.7) |
| 12 | Mass and Volume | DIAG T: balance with identical objects (V12.3, V12.4); MULTI T: tank of jugs (V12.5); BACK T: cup from plate and cups (V12.6); CMP T: heavier by a multiple; DIAG G: weighed twice (V12.7) |
| 13 | Fences and Floors | GEO T: perimeter to area, same perimeter (V13.1, V13.2, V13.4); EXP T: statements about two figures; GEO G: wire bent twice, stretched side (V13.3, V13.5) |
| 14 | Cut, Slide, Count | GEO T: half squares and an L-shape (V14.1, V14.3); EXP T: same area?; LIST G: which pieces make the figure; MULTI G: floor cost (V14.2) |
| 15 | Lines and Corners | LOG T: letters with both kinds of line; LIST T: list the perpendicular pairs; EXP G: a counterexample about crossing lines (Beyond item: V15.1) |
| 16 | Bar Graphs that Tell Stories | EXP T: true, false or not possible to tell from a graph (V16.3); CMP T: differences; EQ T: make two bars equal; CHAL G: missing bar, missing scale (V16.1, V16.2) |
| 17 | Patterns That Grow | PAT T: seats, growing gaps, alternating steps (V17.1, V17.2, V17.4); LOG T: two-number sign from four examples (V17.3); PAT G: two patterns that meet (V17.5) |
| 18 | Balance and Swap | DIAG T: chained balances (V18.1); CMP T: baskets that differ by one item (V18.3); EQ T: a box used twice (V18.2); EQ G: gap after a gift (V18.4) |
| 19 | Cube Stacks and Views | LOG T: match the views; DIAG T: draw the top view; LIST G: fewest and most cubes (V19.2) |
| 20 | The Class Shop (and the Quest) | CMP T: compare two plans; MULTI T: a budget; GC T: guess and check a purchase; BACK G: a backwards sales story; WAYS G: every plan listed |
| 21 | Fold, Flip, Mirror | LOG T: mirror image feature by feature; EXP T: statements about mirror images; PAT G: fold counts and pieces (V21.1, V21.2) |
| 22 | Picture Patterns | PAT T: bead cycle (V22.1); LOG T: combine-and-remove grid (V22.2); CHAL G: invent a grid |
| 23 | Turns and Corners | LOG T: sequence of turns (V23.1); LIST T: quarter-hour clock angles (V23.2); CTX G: directions without a compass |
| 24 | Model Makers: Times As Many | CMP T: times as many with a difference or total (V24.1, V24.4); DIAG T: four-bar model; MULTI T: prices with times as much (V24.5); CMP G: three in a chain (V24.2) |
| 25 | Before and After | BACK T: paid and change (V25.2); EQ T: gap shrinks by twice a gift, unchanged sum (V25.1, V25.3); EQ G: gap to equal (V25.4) |
| 26 | Magic Totals | LOG T: plus shape (V26.2), the 3 by 3 square (V26.3); LOG G: impossible totals (V26.1); CHAL G: design a magic figure |
| 27 | Fractions Everywhere | CTX T: fractions of measures (V27.1); MULTI T: fractions left; CMP G: related sums; EQ G: the missing fraction (V27.2) |
| 28 | Jugs, Scales and Balances | BACK T: pour out in steps; DIAG T: draw both jugs; GC G: fewest moves (V28.1); DIAG G: which amounts are possible |
| 29 | Who Sat Where? | LOG T: four in a row (V29.1); EXP T: true, false or not possible to tell (V29.3); LOG G: is the answer unique (V29.2); EXP G: one clue is false |
| 30 | The Playground Plan (and the Quest) | GEO T: fence and area; MULTI T: cost; CMP T: compare two plans; CHAL G: biggest playground (V30.1) |
| 31 | Factors, Multiples and Tests | LOG T: digit riddles with the 3s test (V31.1, V31.2); EXP T: statements about the 6s table; PAT G: exactly three or four factors (V31.3) |
| 32 | Cycles and Remainders | LOG T: weekday after 95 days, multiples in a range, 4s or 6s (V32.3, V32.2, V32.1); PAT T: last digit cycle (V32.6); GC G: round up and round down (V32.5) |
| 33 | Counting Carefully | WAYS T: outfits, teams, a banned pair (V33.1, V33.2); LIST T: list the teams; DIAG G: ring of trees and lamps (V33.4) |
| 34 | Counting Digits and Pages | LOG T: nth number with only even digits (V34.1); LIST T: list numbers by digit rule; CHAL G: pages from digits (V34.2) |
| 35 | Timetable Puzzles | BACK T: start from end across noon; MULTI T: timetable steps; TAB T: both orders (V35.1); CMP G: two journeys; CTX G: three legs with a delay |
| 36 | Target Practice | GC T: reach a target; EQ T: brackets that keep both sides equal; LOG G: every number 1 to 10 (V36.1) |
| 37 | Most for the Least | GC T: heads and legs (V37.3); CTX T: sticker ink, offers under a budget (V37.1, V37.4); WAYS G: a second limit (V37.5) |
| 38 | Contest Lab | LOG T: possible or impossible (V38.1, V38.2); EXP T: find the error; MULTI T: a two-step problem; CHAL G: an impossible puzzle designed; CMP G: two moves |
| 39 | Problem-Solving Studio | POSE T: a question for a given answer (V39.2); EXP T: find the mistake (V39.1); POSE G: change one number (V39.1) |
| 40 | Mathematicians' Fair (and the Quest) | POSE T: write a problem with its solution; POSE G: a puzzle with a rule; CHAL G: a proof; WAYS G: a family of problems |

### 4.2 Matrix: type by lesson (the spiral across the year)

`T` = Think harder only, `G` = Go further only, `B` = both; `.` = not planned. Lessons 1 to 40 in four groups of ten (one group per term). No type sits at Start here.

```
Lesson   1234567890 1234567890 1234567890 1234567890
Term     1111111111 2222222222 3333333333 4444444444
EQ       ....T.T... .....T.G.. ....B.G... .....T....
GEO      .......... T.BT...... .........T ..........
LOG      TG.G.GG... ....T.T.T. TTT..B..B. TT.T.G.T..
CTX      .......TTB .......... ..G...T... ....G.T...
LIST     ....T..T.. ...GT...G. ..T....... ..TT......
MULTI    ..T..T.... GT.G.....T ...T..T..T ....T..T..
BACK     .T.T.T..BT .T.......G ....T..T.. ....T.....
CHAL     .......... .....G.... .G...G...G ...G...G.G
EXP      TTTT..T... ..TTGT.... T.......B. T......TT.
TAB      ..T......T .......... .......... ....T.....
GC       ...T...T.. .........T .......G.. .G...TT...
PAT      G...G..... ......B... GT........ GT........
DIAG     .......... BB.....TT. ...T...B.. ..G.......
CMP      ..T..T..GT TT...T.T.T ...B..G..T ....G..G..
WAYS     .......G.. .........G .......... ..T...G..G
POSE     .......... .......... .......... ........BB
```

Lessons per type (of 40): EQ 7; GEO 4; LOG 18; CTX 7; LIST 8; MULTI 11; BACK 10; CHAL 7; EXP 14; TAB 3; GC 7; PAT 7; DIAG 7; CMP 14; WAYS 5; POSE 2.

**Departures from the catalogue's own lesson lists** (and why): (a) LIST Think harder at lesson 1 (digit cards, EX-LIST-1) is dropped because it is holiday lesson H1's core; digit-card listing lives at lesson 34 only as a sorted list under a digit rule, never as 'smallest or greatest from cards'. (b) EQ Go further at lesson 24 (a gift so two amounts are equal) is dropped because H4 sets it; lessons 25 and 27 keep the EQ Go further. (c) CMP Go further at lesson 5 has no natural home and is dropped. (d) Added: LOG at 6, 17, 38; LIST at 33; MULTI at 14; EXP at 1 and 13; GC at 8; PAT at 5; CMP at 3. The catalogue's per-type verdicts (CMP 14 lessons, MULTI 10, BACK 10, EQ 8, LOG 15, CTX 7, DIAG 7, GC 6, LIST 8, GEO 4, PAT 6, EXP 12, CHAL 7, WAYS 5, TAB 3, POSE 2) are met or exceeded except EQ (7 against 8, because lesson 24's EQ is H4's); POSE (2) and TAB (3) equal them and match the thin paper counts (2 and 5 items).

### 4.3 Paper-based changes this plan adopts (from `p3_school_paper_patterns.md` section 6)

1. Times as many at Start here in lessons 3 and 6, with the Think harder 'with a difference' (lessons 3, 6, 24). 2. Round-up 'least number of boxes' at Think harder in lessons 4 and 32, true or false for 'none left' in lesson 4. 3. Offers, 'which two items', the one-extra-item bill: lessons 8, 10, 18, 37. 4. Fast and slow watches and a drawn timeline: lessons 9 and 35. 5. Posts and gaps on a line in lesson 11; the ring in 33. 6. 'Same perimeter, different area', 'wire bent into', 'made up of identical rectangles', 'area of one tile': lessons 13 and 14. 7. Bar graph with the scale removed, a missing bar, a picture key of 5 or 6: lesson 16. 8. True, false or not possible to tell in lessons 4, 14, 16 and 29 (and 1, 7, 13, 21, 31, 38, 39). 9. A list-all-the-ways routine in a Term 2 warm-up (section 9). 10. Posing and error analysis (lessons 2, 38, 39, 40). 11. Lessons 19, 21, 22, 23, 26, 34 and 36 keep their contest-style content and are labelled beyond school (no paper evidence).

## 5. New template capabilities Level 3 needs beyond `term/l1/tools`

Codes: **X** figure, **KT** kit page, **RN** online runner, **TL** term-level tool. Hours are template-engineer estimates from the Level 1 documents, not measurements. Rule from Level 1: only the template owner edits `svg.py`, `figs2.py`, `figs3.py`, `validate.py`, `b_*.py`; lesson agents write only `lNN.json`, `verify/lNN_checks.py`, `AUDIT_LNN.md` and `out/lNN/`. New figures go in a new file `figs4.py` appended to the `figs2.render` dispatch (so lesson and engineering work do not collide); the one shared-file edit (X5, a few lines in `svg.number_line`) is the template owner's.

### 5.1 What already exists and is reused as it stands (checked in the working tree on 23 Oct 2026)

Figures: `bundles`, `scatter`, `ten_frame`, `number_line` (`marks`, `hide`, `jumps`, `highlight`, `labels`, `prefix`, `suffix`; integer ticks only), `hundred`, `seq`, `ruler` (cm, objects with a shifted start), `plates`, `objects` (about 55 icons), `groups`, `array`, `line_up`, `round_table`, `bar_model` (compare, part-whole, units, transfer; lengths to scale, brace, gap), `table` (text, boxes, circles, tick boxes, icons), `picture_equation` (six symbols), `domino`, `clock` (hour hand at h + m/60, `sector`, `mirror`, `digital`, `ampm`), `money`, `price_tag`, `calendar`, `stick_pattern`, `shapes2d`, `grid` (dots or squares, `poly`, `route`, `counts`, `mirror` line, `mark`), `cube_stack` (iso, top, views), `fold_punch` (paper, folded, unfolded; one or two folds), `panel` (tiles with shape, number, size, colour, pattern, turn; `hide`), `network`, `picture_graph` (`each`, key, tally). Kits: `base_ten`, `ten_frame`, `plates`, `hundred`, `number_strip`, `cards` (text labels, optional round), `shapes`, `number_line`, `groups_mat`, `unit_strips`, `array_mat`, `people`, `clock_kit`, `play_money`, `price_tags`, `grid_tiles`, `mistake_cards`, `fold_shapes`, `shape_pieces`, `pair_cards`, `grid_mat`, `graph_mat`, `tool_cards`, `event_cards`, `stick_strips`, `calendar_cards`. Question forms: `visuals`, `tf`, `mcq`, `steps`, `draw`, `choices`; tokens `___`, `[]`, `[2]`, `()`, `[ ]`, `{eq}`. Runner v2: `fig`, `fields`, `ordered`, templated choice, `multiples`/`common`/`divisors`, formatters `{n|ord}`, `{n|word}`, `{n|usd}`, `{n|c}`, `{m|mm}`. Lesson fields: `beyond`, `materials.kit_contract`, `home_practice[].rewind_of`, `challenge_quest.scope`; the hand-off check warns when `next_materials` omits the next kit; `b_quest.py` builds the Quest Log, tutor notes and parent note from a `challenge_quest` block and fails on the banned family words.

Lessons that can be written with the tools as they stand (kit work only): 5, 6, 17, 19, 31, 32, 36, 37, 39 (wave A), and the non-Quest parts of 10 and 40.

### 5.2 New figures

| Code | Item | Lessons | Spec in one line | Hours |
|---|---|---|---|---|
| X1 | `column` | 2, 3, 4, 8, 12, 34, 38 | Vertical add, subtract, multiply and short division: digit cells in aligned columns, optional Th H T O or unit headers (kg and g, l and ml, km and m, h and min, $ and decimal point), carry and borrow marks, struck digits, `[]` boxes or letters, one circled digit for error analysis, at most 5 rows; the key shows the filled version. The highest-value figure. | 10 |
| X2 | `pv_counters` | 1, 2, 4 | Place-value chart with discs that differ by column through pattern (dot, ring, double ring, square) so a black-and-white print still reads; exchange arrows; `[]` boxes. | 5 |
| X3 | `area_model` | 3, 13, 14, 30 | A rectangle split into labelled parts with side lengths and partial products in cells (`[]` allowed). | 3 |
| X4 | `fraction` | 7, 27 | Strip (n equal parts, k shaded, patterned), wall (stacked strips) and a 0 to 1 or 0 to 2 line with denominators to 12 and a pointer. A thin wrapper over `number_line` and X5. | 6 |
| X5 | `number_line` extension | 1, 7, 9, 11, 35 | Pointer at any position between ticks, ticks with no labels, an axis break for a non-zero start, 24-hour and dollar labels, a midpoint mark. The only shared-file edit. | 3 |
| X6 | `dial`, `jug`, `balance` | 12, 18, 27, 28 | A kitchen dial with a pointer (0 to 5 kg and 0 to 1000 g), a beaker with a level and ticks (0 to 1000 ml and 0 to 2 l, unmarked option), a pan balance with identical objects and weights and a tilt; objects differ by outline pattern. | 8 |
| X7 | `bar_graph` | 16, 20, 30 and the Quests | Vertical or horizontal bars, scales 1 to 50, double bars with a legend, a hidden bar, a hidden scale, a title, gridlines; `picture_graph` keys of 5, 6, 10 checked. | 7 |
| X8 | `grid` extension | 13, 14, 20, 30 | Edge-length labels, rectilinear polygons from vertices, figures of identical rectangles, half-square diagonal shading, count labels. | 6 |
| X9 | `posts`, `route` | 11, 33 | Equal-gap posts on a line or a ring with labelled distances and `[]` boxes; a route map with legs in metres. | 4 |
| X10 | `lines_fig` | 15, 23 | Labelled points and segments, parallel arrowheads, right-angle marks, block letters on a grid, street and floor plans, turn arrows and arcs. | 6 |
| X11 | `mirror`, `fold` | 21 | A figure with four options flipped, turned or shifted across a dashed line; fold-cut-unfold stages up to three folds; strip folds. | 6 |
| X12 | `circle_fig` | 26, 38 | Plus, triangle (three per side or four per side) and square of circles with values and `[]` boxes. | 3 |
| X13 | `timetable` and 24-hour | 9, 35 | A `table` preset for timetables, a `clock` digital readout in 24-hour form (14 30), span bars on a time line. | 3 |
| X14 | `bar_model` extension | 6, 10, 24, 25, 39 | Up to four bars and twelve cells, a removed (hatched) segment, a before-and-after pair, a nested brace. | 5 |
| X15 | `solid` (optional) | 19 | Square pyramid and cuboid with named faces; nets stay a labelled Primary 4 preview. | 4 |
| X16 | tree diagram (optional) | 33 | Two-stage tree; the `table` already lists outfits. | 2 |
| X17 | `panel` flip and patterns | 21, 22 | `flip` and `rotate` options and a set of fill patterns so that no feature is colour. | 2 |
| X18 | `table` extension | 4, 16, 29 | Tick columns for the true, false or not possible to tell format, a hidden header, merged cells. | 2 |
| | **Total** | | 79 required plus 6 optional | **85** |

### 5.3 Kit builders (section 6 lists the pieces)

New builders: `line_kit` (KT1), `fraction_strips` (KT3), `cut_slide` (KT7), `angle_kit` (KT8), `picture_tiles` (KT12), `turn_kit` (KT13), `plan_pieces` (KT17), `outfit_cards` (KT19), `operator_tiles` (KT22, optional), `pattern_cards` (KT18), `show_cards` (KT21), a $100 note and coin variant of `play_money` (KT23), a menu variant of `price_tags` (KT4). Existing builders reused: `cards` (KT2 pair, KT15 tokens, KT16 clues, KT20 digits, KT9 balance cards), `unit_strips` (KT14), `clock_kit` (KT5), `fold_shapes` (KT11), `shapes` (KT6 tiles), `price_tags` (KT10), `tool_cards` (KT24). Printed mats that are not cut: place-value mat, column paper, grid pages, posts mat, graph mat, balance mat, base mat, magic-figure mats, 4 by 4 mats, pour mat. About **20 hours** for the builders and a check that each page's contract (`kit_contract`) matches the tasks.

### 5.4 Online runner (shared `practice/public/practice.js`; versioned so Levels 1 and 2 keep working)

| Code | Item | Lessons | Hours |
|---|---|---|---|
| RN1 | Compound-unit answers (km and m, kg and g, l and ml, h and min, $ and cents) with equivalent forms accepted (3095 g = 3 kg 95 g) and 'give your answer in the units stated' | 2, 8, 9, 11, 12, 27, 35 | 3 |
| RN2 | Quotient-and-remainder frame with a remainder-less-than-divisor guard | 4, 32 | 1 |
| RN3 | True, false or not possible to tell as an ordered tick table | 4, 14, 16, 29 | 2 |
| RN4 | Fraction answers (top and bottom boxes), a 'simplest form' check, equivalents not accepted when simplest is asked | 7, 27 | 3 |
| RN5 | Money normalisation ($3.2 equals $3.20), cents and dollars conversion, the cent sign | 8, 10, 25, 37 | 2 |
| RN6 | Time answers in 12-hour with am or pm and 24-hour 'hour space minutes' (1430 accepted) | 9, 35 | 2 |
| RN7 | Options that are pictures (mirror images, views, nets) with labels (1) to (4) | 19, 21 | 3 |
| RN8 | New figures usable in `fig` with variables and the 80-variant cap kept | all with figures | 3 |
| | **Total** | | **19** |

### 5.5 Term-level tools

| Code | Item | Hours |
|---|---|---|
| TL1 | `level` parameter: `term/l3/` paths, identity `l3-tN-NN`, practice keys `l3tNlNN`, footers 'Math Inquirers Level 3 Term N', term taglines (T1 'Notice it', T2 'Test it', T3 'Explain why', T4 'Choose and create' as at Level 1), the leak check keyed on `lesson_in_term` and 'the first lesson of Term 4' | 6 |
| TL2 | Copy-check reference list: **exclude our own catalogues** (`docs/books/p*_non_routine_catalogue.md`), whose examples the lessons legitimately mirror (this blocked Level 1 L3, L10, L11, L17 rebuilds); add the gitignored `private_p3_papers/non_routine_questions.md` (school text) and the holiday files `p3/content/l1.js` to `l10.js` so a repeated holiday item fails the build | 1 |
| TL3 | Quest builder for Level 3 (figures in gates, banned words kept, year version for lesson 40) | 2 |
| TL4 | `print/make_term_books.py --level 3` (eight books, page counts, the B&W conversion and check); real-size pages are not shrunk or carry no real-size claim | 3 |
| TL5 | Hand-off checker upgraded from a warning to a failure for Level 3, and a standard 'tear out the kit page' sentence | 1 |
| TL6 | Wording linter for Level 3 conventions: the cent sign, 14 30 time form, 'Ans:' frames, options (1) to (4), no 'work out', no 'bigger' for numbers | 2 |
| TL7 | Entry check for joiners: a five-minute, eight-question check of Primary 2 skills with a catch-up page per result (D15) | 4 |
| TL8 | Level 3 author brief (a copy of the Level 1 briefs plus this document, the figure names, the holiday register and the failure checklist) | 3 |
| TL9 | Validator keys: reading-load limits for age 8 to 10 (child text up to 50 words), `limits`, Quest rules | 1 |
| TL10 | Rewind sets and the home-sheet rewind slot | 3 |
| | **Total** | **26** |

### 5.6 Totals and what can wait

Figures 85 + kit builders 20 + runner 19 + term tools 26 = **150 hours** if everything is built. Deferrable without blocking a lesson (about 17 hours): X15 (4), X16 (2), KT22 (1, children write the signs), RN8 (3, use static figures in practice), TL7 (4, the entry check can follow the first trial), TL10 (3). That leaves about **133 hours**. Not needed at Level 3: speed, ratio, decimals beyond money, percentages, coordinates, letters for unknowns.

## 6. Kit contracts: supplied pieces against the most a task may use

The Level 1 cut-out audit found two Reworks (L12 strips, L19 shape cards) because piece counts were never checked against tasks, and 203 pieces in one term. Each row is the contract the lesson author signs: `supplied` is what the page prints; `max used` is the most any task uses; the lesson's `materials.kit_contract` (a field that exists in the Level 1 schema) and its verify script assert supplied >= max used. A grown-up (or the child with a grown-up) cuts before the lesson; nobody cuts during a lesson. Every kit page carries the standard note: print on its own sheet (the book puts it on a front page with a blank back), keep the pieces in an envelope with the child's name, tear out along the dashed line. All kits are black and white: pieces differ by shape, size, label or fill pattern, never colour alone; digits that can be turned (6, 9) are underlined; cut lines at least 6 mm apart; counters and tiles are squares with rounded corners; a 'no printer' fallback is written on every kit page.

| L | Kit | Supplied | Max used by a task | Cut | Notes |
|---|---|---|---|---|---|
| 1 | KT1 line_kit: 2 line strips, 12 number cards | 12 cards, 2 strips | 8 cards, 2 strips | 14 | Alternative: draw a line on a paper strip, write numbers on scraps |
| 2 | none cut | - | - | 0 | Place-value mat and column paper printed, not cut |
| 3 | none cut | - | - | 0 | Area-model grid printed, not cut |
| 4 | none cut | - | - | 0 | None; about 30 small things from home |
| 5 | KT2 pair_cards: 12 cards (six pairs to 100) | 12 | 12 | 12 |  |
| 6 | none cut | - | - | 0 | None |
| 7 | KT3 fraction_strips: whole, halves, thirds, quarters, sixths, eighths, twelfths | 7 strips | 4 at once | 7 | Keep for lesson 27; patterned, not coloured |
| 8 | KT4 menu_cards: 8 price cards | 8 | 5 at once | 8 | Reused in lessons 10 and 20 |
| 9 | KT5 clock_kit: 2 faces (not cut), 2 hour hands, 2 minute hands | 2 faces, 2 + 2 hands | 2 faces, 2 + 2 hands | 4 | Keep for lessons 23 and 35; loose hands, no pin |
| 10 | none cut | - | - | 0 | None; reuses the lesson 8 menu cards; Quest Log in the book |
| 11 | none cut | - | - | 0 | Posts mat printed, not cut |
| 12 | none cut | - | - | 0 | None; cups and a jug |
| 13 | KT6 square_tiles: 24 tiles of 2 cm | 24 | 24 | 24 | Keep for lessons 17 and 31 |
| 14 | KT7 cut_slide: 4 half-square triangles, 2 rectangles, 2 L-pieces | 8 | 8 | 8 |  |
| 15 | KT8 angle_kit: 2 right-angle checkers, 2 straight-edge strips | 2 + 2 | 2 + 1 | 4 | A set square is optional |
| 16 | none cut | - | - | 0 | Graph mat printed, not cut |
| 17 | none cut | - | - | 0 | None; reuses the 24 square tiles of lesson 13 (at most 16 used) |
| 18 | KT9 balance_cards: 3 apples, 3 pears, 3 plums | 9 | 9 | 9 | Told apart by outline pattern, not colour |
| 19 | none cut | - | - | 0 | 3 by 3 base mat printed, not cut; 12 to 14 blocks from home (max used by a real-block task 12) |
| 20 | KT10 price_tags: 10 stall tags (item picture, price) | 10 | 8 at once | 10 | Reuse the lesson 8 cards if kept |
| 21 | KT11 fold_squares: 6 paper squares (12 cm), 2 strips | 6 + 2 | 4 + 1 | 8 | Nobody uses scissors in the lesson; a cut is drawn |
| 22 | KT12 picture_tiles: 15 tiles | 15 | 9 | 15 | Features: shape, number, size, turn, fill pattern; never colour |
| 23 | KT13 turn_kit: 1 direction disc, 1 arrow | 1 + 1 | 1 + 1 | 2 | Plus the clock (KT5) |
| 24 | KT14 unit_strips: 4 strips of 10 cells | 40 cells | 13 cells | 4 | Exists as `unit_strips` |
| 25 | none cut | - | - | 0 | None |
| 26 | KT15 number_tokens: two sets of 1 to 9 | 18 | 18 | 18 | 6 and 9 underlined; mats not cut |
| 27 | none cut | - | - | 0 | None; reuses the fraction strips of lesson 7 |
| 28 | none cut | - | - | 0 | Pour mat printed, not cut; two cups and rice or water |
| 29 | KT16 clue_cards: 8 clue cards, 4 name cards | 12 | 10 | 12 | 4 by 4 mats not cut |
| 30 | KT17 plan_pieces: 12 rectangles | 12 | 10 | 12 | Quest Log separate |
| 31 | none cut | - | - | 0 | None; reuses the 24 square tiles (max 24) |
| 32 | KT18 pattern_cards: 12 cards (circle, square, triangle x 4) | 12 | 12 | 12 |  |
| 33 | KT19 outfit_cards: 3 hats, 4 scarves, 5 shirts, 4 pairs of shorts | 16 | 9 at once | 16 |  |
| 34 | KT20 digit_cards: two sets of 0 to 9 | 20 | 10 | 20 | Keep for lessons 36 and 38; 6 and 9 underlined |
| 35 | KT21 show_cards: 4 show cards, 2 film cards | 6 | 6 | 6 | Plus the clock (KT5) |
| 36 | KT22 operator_tiles: 3 each of + - x and division (12), 2 bracket pairs (4) | 16 | 15 | 16 | Optional: write the signs in boxes instead |
| 37 | KT23 play_notes: $100 x 1, $50 x 2, $10 x 4, $5 x 2, $2 x 3, $1 coin x 3 | 15 | 7 | 15 | PLAY MONEY; stylised; no $20 note; legal check (D13) |
| 38 | none cut | - | - | 0 | None; reuses the digit cards |
| 39 | KT24 tool_cards: 7 tool cards, 8 problem cards | 15 | 15 | 15 | Exists as `tool_cards` |
| 40 | none cut | - | - | 0 | None |

Cut per term: Term 1 45, Term 2 55, Term 3 71, Term 4 100 (84 without the lesson 36 tiles); year 271. Per book (5 lessons): Book 1 26; Book 2 19; Book 3 36; Book 4 19; Book 5 29; Book 6 42; Book 7 54; Book 8 46.

Book page counts (estimate from the Level 1 pattern, 5 pages per lesson plus kit pages, a Quest Log of 3 pages in Books 2, 4, 6, 8, a cover and contents, and a blank pad so each lesson starts on a right-hand page): about 36 to 40 pages per book. `term_books_spec.json` gives the true counts after a build.

## 7. Hand-off chain: what the family must have ready (truth between all 40 lessons)

The Level 1 rule: `parent.next_materials` of lesson n lists everything lesson n+1 needs that a family has to prepare: the book (issued on payment), any kit page to cut, anything kept from earlier, anything to find at home. The tutor's spoken goodbye, the `s-end` slide and `tutor_prep` carry the same words. Under the print-on-payment decision the wording is 'your next workbook is in your book: tear out the kit page along the dashed line, then a grown-up cuts out the pieces' (Level 1 audit F6). The row for lesson n to n+1 is what lesson n+1 needs, copied from the kit contracts, so the two tables cannot disagree. A validator check (TL5) fails a build when a lesson's `next_materials` omits the next lesson's cut-out kit.

| From to | Cut / prepare (a grown-up cuts a week before) | Keep from before | Find at home | Check and hazard |
|---|---|---|---|---|
| before 1 | 12 number cards and 2 line strips (KT1) (Book 1) | - | pencil; 30 cm ruler optional | Term 1 start: Book 1 is posted to the family before the lesson |
| 1 to 2 | nothing (place-value mat and column paper are printed in the book) | - | pencil |  |
| 2 to 3 | nothing (grid page in the book) | - | pencil |  |
| 3 to 4 | nothing | - | about 30 small things (buttons, beans) |  |
| 4 to 5 | 12 pair cards (KT2) | - | pencil |  |
| 5 to 6 | nothing | - | strips of paper | Book 2 starts here: it is issued with the first payment (D11); if it is late this hand-off fails |
| 6 to 7 | 7 fraction strips (KT3) | - | a paper strip to fold |  |
| 7 to 8 | 8 menu cards (KT4) | - | pencil |  |
| 8 to 9 | the clock hands (KT5) | - | a calendar page; a real clock if there is one | The clock hands are the clock of lessons 23 and 35 too: keep them all year |
| 9 to 10 | nothing to cut | the menu cards (lesson 8) | the Quest Log closed in its envelope (it is in Book 2); a quest partner |  |
| 10 to 11 | nothing (posts mat in the book) | - | 30 cm ruler, 1 m of string | Term break; Book 3 starts; the tutor gives the Term 2 start date |
| 11 to 12 | nothing | - | cups, a jug, a 1 l bottle; a kitchen scale if there is one |  |
| 12 to 13 | 24 square tiles (KT6) | - | ruler, string about 60 cm, squared paper | The tiles are used again in lessons 17 and 31: keep them all year |
| 13 to 14 | 8 cut-and-slide pieces (KT7) | - | squared paper |  |
| 14 to 15 | 2 checkers and 2 strips (KT8) | - | ruler; a set square if there is one |  |
| 15 to 16 | nothing | - | squared paper, pencils | Book 4 starts here |
| 16 to 17 | nothing | the 24 square tiles (lesson 13) | pencil |  |
| 17 to 18 | 9 balance cards (KT9) | - | pencil |  |
| 18 to 19 | nothing (base mat in the book) | - | 12 to 14 same-size blocks (building bricks, dice, sugar cubes) | No blocks at home: the fallback is drawn stacks and counters |
| 19 to 20 | 10 stall tags (KT10) | the menu cards | the Quest Log closed; a quest partner |  |
| 20 to 21 | 6 paper squares and 2 strips (KT11) | - | scrap paper | Term break; Book 5 starts (Term 3); nobody cuts in the lesson |
| 21 to 22 | 15 picture tiles (KT12) | - | pencil |  |
| 22 to 23 | direction disc and arrow (KT13) | the clock (lesson 9) | a toy for the robot |  |
| 23 to 24 | 4 unit strips (KT14) | - | strips of paper |  |
| 24 to 25 | nothing | - | pencil |  |
| 25 to 26 | 18 number tokens (KT15) | - | pencil | Book 6 starts; its Quest Log stays closed in the envelope |
| 26 to 27 | nothing | the fraction strips (lesson 7) | a measuring jug |  |
| 27 to 28 | nothing (pour mat in the book) | - | two cups or bottles of different size, a bowl, rice or water |  |
| 28 to 29 | 8 clue cards and 4 name cards (KT16) | - | pencil |  |
| 29 to 30 | 12 plan pieces (KT17) | - | squared paper; the Quest Log closed; a quest partner |  |
| 30 to 31 | nothing | the 24 square tiles | pencil | Term break; Book 7 starts; the tutor gives the Term 4 start date |
| 31 to 32 | 12 pattern cards (KT18) | - | a calendar page |  |
| 32 to 33 | 16 outfit cards (KT19) | - | pencil |  |
| 33 to 34 | 20 digit cards (KT20) | - | pencil |  |
| 34 to 35 | 6 show cards (KT21) | the clock (lesson 9) | - |  |
| 35 to 36 | 16 operator tiles (KT22, optional) | the digit cards (lesson 34) | - | Book 8 starts here; its Quest Log stays closed |
| 36 to 37 | 15 play notes and coins (KT23) | - | pencil | The heaviest cut of Term 4 (15 pieces) |
| 37 to 38 | nothing | the digit cards | pencil |  |
| 38 to 39 | 15 tool and problem cards (KT24) | - | pencil |  |
| 39 to 40 | nothing | - | a favourite page from the year; plain paper; the Quest Log closed; a quest partner |  |
| 40 to next | the tutor sends the next level's placement note; no materials list is printed here | - | - | Not a lesson-file concern |

## 8. Mi's Challenge Quest in lessons 10, 20, 30 and 40

The Level 1 Quest (lesson 20) is the model: 20 minutes at minutes 35 to 55 straight after the break; eight short gates and one optional secret cave; a quest partner (answers are written on private paper, each child writes their own); no score, mark, ranking or visible timer; no word 'test' or 'exam' on any child or parent page (`BAN_FAMILY` in `b_quest.py`); the tutor keeps private notes only, used for one line to each grown-up and for advice on next term's group; the recording is paused for the Quest and a make-up child does the Quest before watching the recording; photos of the Quest Log are returned by the parent to the business WhatsApp (+65 9880 5962, never on a slide). Explore 10 and Mini-lesson 9; the Start here workbook is 25 minutes; pages 3 to 5 are for home; the exit ticket is not live. Three files per Quest: `LNN_Quest_Log.pdf` (3 pages, in Books 2, 4, 6, 8), `LNN_Quest_Tutor_Notes.pdf` (key book), `LNN_Quest_Parent_Note.pdf` (home pack). The Quest Log may carry figures (a clock, a bar graph) because the Level 1 generator now accepts any registered figure (the Level 1 note to check this with a clock gate stands, TL3). Rules for authors: every gate is Start here level for its own lesson and 'pass' is always allowed; the Quest is never the part that shrinks in a slow class (skip order: Flex, then the optional Go further slide, then Talk); the cave is the only place for a puzzle the children have not met; one item per part; Level 3 children read the Quest Log themselves but the tutor reads each gate once aloud.

Lessons share a gate where the plan says two lessons are neighbours, so every lesson of the term is visited by exactly one gate. All answers below were recomputed (check ids in the last column).

### 8.1 Term 1 (lesson 10)

| Gate | Lessons | Item (Start here level) | Figure | Check |
|---|---|---|---|---|
| 1 | 1 | The arrow on a line marked every 100 from 4000 to 5000 is at the third mark: 4300. 1000 more than 6205: 7205 | `number_line` | Q1.1 |
| 2 | 2, 5 | 4382 + 2519 = 6901. 64 + 29 + 36: find the pair that makes 100, total 129 | `column` | Q1.1 |
| 3 | 3, 4 | 34 x 6 = 204. 85 shared among 4: 21 each and 1 left over | `column` | Q1.1 |
| 4 | 6 | Mei buys 3 books at $4 each and a ruler for $2 and pays $20: she spends $14, change $6 | none | Q1.2 |
| 5 | 7 | 3/6 in simplest form is 1/2. Which is greater, 3/4 or 5/8: 3/4 | `fraction` | Q1.2 |
| 6 | 8 | $2.50 + $3.45 = $5.95. The change from $10 is $4.05 | `price_tag` | Q1.3 |
| 7 | 9 | A film starts at 2:40 pm and lasts 1 h 35 min: it ends at 4:15 pm. 3:20 pm in 24-hour form is 15 20 | `clock` | Q1.3 |
| 8 | 10 | 5 pens cost $15: one pen costs $3, so 8 pens cost $24 | `bar_model` | Q1.3 |
| Cave | beyond | Pens cost 1 for $3, 2 for $5 or 5 for $11. Exactly 9 pens at the least cost: $21 | `table` | V10.6 |

### 8.2 Term 2 (lesson 20)

| Gate | Lessons | Item (Start here level) | Figure | Check |
|---|---|---|---|---|
| 1 | 11 | Seven posts stand in a line 5 m apart: the first to the last is 30 m | `posts` | Q2.1 |
| 2 | 12 | 3 kg 250 g + 1 kg 900 g = 5 kg 150 g | `dial` | Q2.1 |
| 3 | 13, 14 | A rectangle 9 cm by 4 cm: perimeter 26 cm, area 36 cm2 | `grid` | Q2.1 |
| 4 | 15 | Name a pair of parallel lines in a lettered figure; name a line perpendicular to AB | `lines_fig` | none (a picture answer) |
| 5 | 16 | Two bars on a scale of 5 show 35 and 20: the difference is 15 | `bar_graph` | Q2.1 |
| 6 | 17, 18 | The 10th number of 5, 9, 13, 17 is 41. 4 oranges balance 3 oranges and a 150 g weight: an orange is 150 g | `seq`, `balance` | Q2.1 |
| 7 | 19 | A stack of cubes with heights 2, 1, 3 in a row has 6 cubes | `cube_stack` | none (counting) |
| 8 | 20 | 3 pens at $4 and 2 rulers at $3, paid with $20: the bill is $18, change $2 | `price_tag` | Q2.2 |
| Cave | beyond | A square garden has 10 m on each side and a post every 2 m round it: 20 posts | `posts` | Q2.1 |

### 8.3 Term 3 (lesson 30)

| Gate | Lessons | Item (Start here level) | Figure | Check |
|---|---|---|---|---|
| 1 | 21, 22 | A square folded in half twice and punched once: 4 holes. The next picture in a repeating strip | `fold_punch`, `panel` | Q3.1 |
| 2 | 23 | Facing the door you make a quarter turn right and then a half turn: you face the left wall (three quarter turns) | `lines_fig` | Q3.2 |
| 3 | 24 | Amy has 24 stickers and Ben has 3 times as many: together 96 | `bar_model` | Q3.1 |
| 4 | 25 | After giving away 40, Ali has 85 left: at first 125 | `bar_model` | Q3.1 |
| 5 | 26 | A magic square with total 15 has a row 8, [], 6: the missing number is 1 | `table` | Q3.1 |
| 6 | 27, 28 | 3/4 m is 75 cm. With jugs of 5 l and 8 l, fill the 8 l jug and pour into the 5 l jug to measure 3 l | `jug` | Q3.1 |
| 7 | 29 | Three children in a row: Ali sits at one end, Ben does not sit next to Ali, Cara sits somewhere to the left of Ali: Ben, Cara, Ali | `table` | Q3.4 |
| 8 | 30 | A playground 12 m by 8 m has a perimeter of 40 m; fencing at $5 a metre costs $200 | `grid` | Q3.1 |
| Cave | beyond | Put 1, 3, 5, 7 and 9 in a plus of five circles so both lines of three have the same total: the middle can be 1, 5 or 9 (totals 13, 15, 17) | `circle_fig` | Q3.5 |

### 8.4 Term 4 (lesson 40)

| Gate | Lessons | Item (Start here level) | Figure | Check |
|---|---|---|---|---|
| 1 | 31 | Is 4725 in the 3s table? The digits add to 18, so yes | none | Q4.1 |
| 2 | 32 | Today is Thursday: 20 days later it is Wednesday | `calendar` | Q4.1 |
| 3 | 33 | 3 hats and 4 scarves make 12 outfits | `table` | Q4.1 |
| 4 | 34 | Pages 1 to 25 need 41 digits | none | Q4.1 |
| 5 | 35 | Buses leave every 15 minutes from 7:40 am: the 4th bus leaves at 8:25 am | `table` | Q4.1 |
| 6 | 36 | Work (8 - 5) x 4 = 12 | none | Q4.1 |
| 7 | 37 | The fewest notes and coins for $62 is 3 ($50, $10, $2) | `money` | Q4.1 |
| 8 | 38, 39 | Jo has 3 times as many stickers as Kit and together they have 36: choose a move (a strip) and find Jo's 27 | `bar_model` | Q4.1 |
| Cave | beyond | A shop gives 1 free sticker for every 4 bought; Zoe wants 30 stickers: she must buy 24 | `table` | Q4.2 |

Lesson 40's own showcase is the closing part of the Quest lesson; it has no gate. A child who joins at lesson 30 or 40 has not met the earlier gates: every gate states its own idea in one line, and the cave may be skipped.

## 9. Spiral review across the year

The Level 1 term-wide audit found no spiral review (warm-ups re-teach only what the lesson needs; home and online practice are current-lesson only), and Level 1 Terms 3 and 4 fixed it with layers that add no minutes to the 90. Level 3 builds them in from lesson 1.

1. **Home sheet slot 5 is 'Mi's rewind'.** One item from lesson n - 10 (for n of 11 or more), with its answer on the separate answer sheet; lessons 1 to 10 rewind a holiday topic (the warm-up list in section 1.2). Items are copied from the earlier lesson's home or online bank by id, not rewritten (needs the `rewind_of` tag and the rewind set tool, TL10).
2. **Online practice ends with two rewind items** from lesson n - 5 (n of 6 or more) and, from lesson 21, a second pair from lesson n - 20, so every Term 1 and Term 2 idea is visited again at three distances in the year.
3. **The Quest cave** is an unseen puzzle joining two moves; one Remember item per lesson may be a spiral item.
4. **Warm-up bank for Terms 2 to 4** (plan line 58 and patterns section 6.9): a recurring five-minute spatial routine (draw a cube stack, name the feature that differs, pick a mirror image) from lesson 11 on, so the eye is trained before lessons 19 to 22; and a two-minute list-all-the-ways routine (hats and scarves, a team of 2 from 5) in Term 2 warm-ups, so lesson 33 is not a first meeting. Neither costs a lesson.

| Lesson | Home rewind | Online rewind | Lesson | Home rewind | Online rewind |
|---|---|---|---|---|---|
| 1 | holiday topic | - | 21 | 11 Length and Distance | 16 Bar Graphs that Tell Stories; 1 Number Lines to 10 000 |
| 2 | holiday topic | - | 22 | 12 Mass and Volume | 17 Patterns That Grow; 2 Write It Down, Check It |
| 3 | holiday topic | - | 23 | 13 Fences and Floors | 18 Balance and Swap; 3 Multiply by Splitting |
| 4 | holiday topic | - | 24 | 14 Cut, Slide, Count | 19 Cube Stacks and Views; 4 Divide It Up |
| 5 | holiday topic | - | 25 | 15 Lines and Corners | 20 The Class Shop; 5 Mental Maths Moves |
| 6 | holiday topic | 1 Number Lines to 10 000 | 26 | 16 Bar Graphs that Tell Stories | 21 Fold, Flip, Mirror; 6 The Hidden Question |
| 7 | holiday topic | 2 Write It Down, Check It | 27 | 17 Patterns That Grow | 22 Picture Patterns; 7 Fractions on the Number Line |
| 8 | holiday topic | 3 Multiply by Splitting | 28 | 18 Balance and Swap | 23 Turns and Corners; 8 Dollars and Cents |
| 9 | holiday topic | 4 Divide It Up | 29 | 19 Cube Stacks and Views | 24 Model Makers: Times As Many; 9 Time Detectives |
| 10 | holiday topic | 5 Mental Maths Moves | 30 | 20 The Class Shop | 25 Before and After; 10 Price per Piece |
| 11 | 1 Number Lines to 10 000 | 6 The Hidden Question | 31 | 21 Fold, Flip, Mirror | 26 Magic Totals; 11 Length and Distance |
| 12 | 2 Write It Down, Check It | 7 Fractions on the Number Line | 32 | 22 Picture Patterns | 27 Fractions Everywhere; 12 Mass and Volume |
| 13 | 3 Multiply by Splitting | 8 Dollars and Cents | 33 | 23 Turns and Corners | 28 Jugs, Scales and Balances; 13 Fences and Floors |
| 14 | 4 Divide It Up | 9 Time Detectives | 34 | 24 Model Makers: Times As Many | 29 Who Sat Where?; 14 Cut, Slide, Count |
| 15 | 5 Mental Maths Moves | 10 Price per Piece | 35 | 25 Before and After | 30 The Playground Plan; 15 Lines and Corners |
| 16 | 6 The Hidden Question | 11 Length and Distance | 36 | 26 Magic Totals | 31 Factors, Multiples and Tests; 16 Bar Graphs that Tell Stories |
| 17 | 7 Fractions on the Number Line | 12 Mass and Volume | 37 | 27 Fractions Everywhere | 32 Cycles and Remainders; 17 Patterns That Grow |
| 18 | 8 Dollars and Cents | 13 Fences and Floors | 38 | 28 Jugs, Scales and Balances | 33 Counting Carefully; 18 Balance and Swap |
| 19 | 9 Time Detectives | 14 Cut, Slide, Count | 39 | 29 Who Sat Where? | 34 Counting Digits and Pages; 19 Cube Stacks and Views |
| 20 | 10 Price per Piece | 15 Lines and Corners | 40 | 30 The Playground Plan | 35 Timetable Puzzles; 20 The Class Shop |

**Spiral threads across the year** (each strand returns at least twice in a new setting; fractions return in warm-ups and lesson 39).

| Thread | Term 1 | Term 2 | Term 3 | Term 4 |
|---|---|---|---|---|
| Number lines and bounds | 1 | 16 (graph scales) | 26 (impossible totals) | 38 (possible or impossible) |
| Column work and checking | 2, 3, 4 | 12 (unit columns) | 25 (undo) | 34 (digit sums), 39 (error analysis) |
| Money | 8, 10 | 20 (shop) | 30 (cost) | 37 (fewest notes) |
| Time | 9 | 11 (gaps in time) | 23 (turns, clock) | 35 (timetables) |
| Fractions | 7 | warm-ups | 27 | warm-ups, 39 |
| Models and finding one | 6, 10 | 18 | 24, 25 | 39 |
| Listing every case | 5, 8 | 15, 19 | 26, 29 | 31, 33, 34, 37 |
| Area and perimeter | - | 13, 14 | 30 | - |
| Patterns and rules | 1, 5 | 17 | 22 | 32 |

## 10. Known failure patterns from Level 1: the author checklist

Read from `TERM_WIDE_AUDIT`, `CUTOUT_AUDIT`, `FINAL_AUDIT_T1`, `FINAL_AUDIT_T2` and the two Level 1 pre-flights. Each line is something the Level 1 fix passes repaired more than once; the Level 3 authors should not write it in the first place, and each has a check.

| # | Level 1 failure (source) | Level 3 rule | Check |
|---|---|---|---|
| 1 | Kit counts do not match tasks (L12 strips, L19 shape cards, L20 tokens, L13 counters; CUTOUT F1, F2) | Every kit lesson fills `materials.kit_contract`; supplied >= max used; section 6 | `verify/lNN_checks.py` asserts it; validator fails otherwise |
| 2 | False 'next lesson' materials lines (7 of 9 in Term 1; L7 to L8, L9 to L10, L10 to L11) | `next_materials` is copied from section 7 and says 'tear out the kit page'; the spoken goodbye and `s-end` slide use the same words | TL5 fails a build on a mismatch |
| 3 | Workbook numbers repeat class numbers (WB1 in L15 to L20, L8 T1) | No Start here or Think harder number is used in Explore, Mini-lesson, Sneak-peek or the Quest | verify script scans the slide data |
| 4 | Answers on the slide while the question is asked (G1, every Term 2 deck audit) | `reveal` blocks and answer slides; Explore pictures never carry the count | deck check |
| 5 | Family pages use the global lesson number ('Lesson 14', 'Lesson 1 of 10'); mixed numbering in books (cover 'Lesson 11', pages 'Lesson 1') | 'Level 3 Term 2 Lesson 4' on every family page; books print 'Term 2 Lesson 4 (lesson 14 of 40)' | leak check keyed on `lesson_in_term`; 'the first lesson of Term 4' |
| 6 | Start here too long for the 28 workbook minutes (15.5 to 19 modelled against 28; slow class 3 to 4 minutes over) | Six Start here items, at most 20 modelled minutes; page 1 about 8 minutes, page 2 about 9, choice 3; 'Think harder and Go further are for home' on the page | validator timing |
| 7 | Keys accept one order or form (3 x 4 against 4 x 3) | Accept equivalent forms: 3 x 4 and 4 x 3; $3.2 and $3.20; 3 kg 95 g and 3095 g; 14 30 and 1430; ways in any order; teams in any order | RN1, RN5, RN6 |
| 8 | Recording and camera scripts differ across lessons; first names on the recording; 'cameras on' beside 'may switch off' | Copy the final Level 1 wording (L6 to L10 after the 23 Oct fix) into every Opening: notice first, then start the recording; 'the tutor, the shared screen and any unmuted voice are recorded; children may mute and keep cameras off'; no first names on the recording; no paper hold-ups | identical-text check across lessons |
| 9 | 'I am still stuck' had no route | Tick on the look-back, the parent photographs the page to the business WhatsApp after class; the number is never on a slide | validator privacy check |
| 10 | Parent page: boilerplate term line, no weekly workload, no 'do not teach' line, no practice link | A lesson-specific term line; 'Home Practice (15 minutes) if you like; pages 3 to 5 and online practice are optional'; a words list; a when-stuck line; the beyond-Primary-3 sentence from `beyond.parent` | parent-page check |
| 11 | Runner variants: '1 hours', '1 stickers', double full stops, raw placeholders | Plural guards; every variant verified three ways (oracle, runner, validator) | validator |
| 12 | Investigation page overflow | A drawing box, four ruled lines, an easy first step | real-PDF page check |
| 13 | Small pictures on the workbook (tables, number lines, strips; L14 chart cells 6 mm) | Give `size` and column width for each new figure in the first build; chart cells at least 12 mm | page view |
| 14 | Wrong working attached to cast names | 'A child' or 'a child in another class' | text scan |
| 15 | Children cutting in the lesson | A grown-up cuts beforehand; nobody cuts in a lesson | guide and materials text |
| 16 | A contest label on a child page; the word 'Challenge' used for tiers | `contest_where` names tiers in tutor text only; 'Challenge' only in 'Mi's Challenge Quest' | validator banned words |
| 17 | Colour or glyph reliance (red and yellow counters, stars as marks, symbols that read the same in grey) | Black and white by shape, label and fill pattern; `print/check_bw.py` on every book | B&W check |
| 18 | Slow-class overrun; Quest squeezed | No part OVER in the slow-class model; in lessons 10, 20, 30, 40 the Quest is never the part that shrinks | timing model |
| 19 | Mi's calculator image; stale builds (L3, L10, L11, L17 kept the old Mi because the validator blocked a rebuild) | The no-calculator image everywhere; rebuild every lesson after a template change; rebuild the books after | build log check |
| 20 | Real-size ruler claims false in the books (94.3 percent scale) | No 'real size' claim; 'All diagrams are not drawn to scale'; tasks that measure use the child's own ruler on real objects | text scan |
| 21 | The copy check failed on our own catalogue text (L3, L10, L11, L17) | TL2 excludes our own catalogues and adds the school text and the holiday files | validator |
| 22 | Recording notice said after the recording started (L13 to L20) | Notice first | script check |
| 23 | Quest tutor notes printed wrong part answers (L20 gate 6: 20 and 17 against 15 and 11) | Part answers generated from the values and compared by the verify script | verify script |
| 24 | The error-spotter was always the same name | Spread across the cast; 'a child' for wrong working | text scan |
| 25 | Investigation tables and drawing boxes missing (Term 1 audits L1, L2, L8, L10) | `table` figure and `visuals` on page 5 where the task needs them | page view |

## 11. Risks

1. **Holiday overlap (twenty Heavy lessons).** The register in section 3 is built from the question stems of the holiday banks; a repeated item is the most likely audit finding. Mitigation: authors read the holiday file for their lesson first; TL2 fails the build on a 7-word overlap; the independent audit checks the register.
2. **Plan contamination.** Anyone who builds lesson assignments from the plan's non-routine section will write Level 5 content (shifting places, GST, ratio). Use section 4.
3. **Picture dependence.** 366 of 1098 school items need the picture, and 18 figure types do not exist. If figure work slips, the first items to drop are the optional ones (X15 pyramid, X16 tree), then the picture options of lessons 19 and 21, never a Start here item. Lessons 1, 7, 9, 11 to 16 and 21 to 23 cannot start before their figures.
4. **Black and white and the 94.3 percent print scale.** Colour is decoration only; no lesson task may depend on a printed length. Lessons 11, 13 and 15 name the child's own ruler or checker; the set square is optional.
5. **Reading load.** Primary 3 stems are one to three sentences; Level 3 children read themselves, but a Think harder item with a new word needs the tutor to read it. New vocabulary per lesson goes in the parent word list (for example 'quotient', 'perpendicular', 'simplest form', 'perimeter').
6. **Tier honesty.** Likeliest slips: a P4 factors item at lesson 31 Start here; the word 'symmetry' defined at lesson 21 Start here; unbracketed order of operations at lesson 36 Start here (P5); a composite-area split at lesson 14 Start here; a fraction of a set at lesson 27 Start here; a letter puzzle at lesson 2 Start here. An independent reader checks every Start here item against `syllabus_by_level.md`.
7. **Joining cold.** Term 1 Start here uses Primary 2 skills only; later terms re-teach one earlier idea in under five minutes (strips in 24, remainders in 32, posts in 33, area in 14). A mid-year joiner who never met H2 meets cryptarithms only in lessons 2 (one item) and 38 (one item).
8. **SASMO near-copy and the 'no SASMO preparation' claim.** Four plan items replaced (finding 3). No contest text; the 7-word check against the SASMO analysis stays. Child and parent pages never say SASMO, MOE-aligned or GEP.
9. **Lessons with no school evidence.** Six (19, 21, 22, 26, 34, 36) plus 23. Seven of forty lessons (17.5 percent) teach contest ideas the school papers do not set. They are labelled beyond school and each has a named swap candidate (D4).
10. **Quest lessons are tight.** Explore 10 and Mini-lesson 9 minutes. Lesson 10 introduces unit price; if the first trial shows 19 minutes is too short, move the unit-price Start here to lesson 8's Think harder and make lesson 10 a Term 1 review (D16).
11. **Timing.** The Level 1 audits found the workbook 3 to 4 minutes over in a slow class in every lesson and the 5-minute buffer consumed. Level 3 children write more per question and the plan keeps six Start here questions. Measure in the trial; if confirmed, cut one warm-up group per lesson.
12. **Cutting load.** 271 pieces a year (section 6); Term 4 about 100. Options: operator tiles optional, play notes cut from 15 to 10, tiles reused (already planned).
13. **Play money.** The same open legal question as Level 1 (D1 there): stylised, marked PLAY MONEY, no $20 note, a $100 note added. Check before anything realistic is printed.
14. **Wording evidence.** 2019 papers read from 100 dpi OCR, about 16 of 39 2019 scans unread, no picture seen. Items whose form rests on a picture (clock, graph, balance, coin, views) are 'wording unverified' until the owner supplies pictures or sample papers.
15. **Books.** Eight books of about 36 to 40 pages; a book boundary falls at lessons 5, 15, 25, 35 mid-term; if a book is late the hand-off fails (D11). The Quest Log must stay closed in its envelope.
16. **Slots.** The 90-minute lessons need slots re-derived from the 2027 grid (owner entry of 23 Oct); Level 3 children (ages 8 to 10) may attend after school or at weekends; hand-off dates depend on it.
17. **Website, privacy and terms** still describe the holiday beta; the Level 1 findings F10 and F11 apply unchanged to Level 3 (no Level 3 term page, the photo return flow unnamed in the privacy notice). Not a lesson-file concern.
18. **Parallel agents on shared files.** Same rule as Level 1: only the template owner edits shared tools; lesson agents write only their own files and commit with explicit `git add`, never `git add -A`.
19. **Authoring documents are Level 1 specific** (`AUTHORING.md` lists Lessons 2 to 10, `LESSON_BRIEF.txt` names Lesson 1 as the pilot): TL8.
20. **Hours are estimates**, taken from Level 1 documents; Level 3 lessons carry more verification and more figures.

## 12. Decisions the owner must make (defaults I chose are marked [Default])

None is irreversible; changing a default after the build costs time, as noted.

- **D1. The plan's non-routine section.** It is Level 5 text. [Default] Use section 4 of this document as the Level 3 source; replace lines 274 to 395 of `level_3_year_plan.md` with it (an edit I did not make because I was told to touch only my file). Cost of waiting: authors may pick up the wrong list.
- **D2. Holiday overlap policy.** Twenty lessons share a strand and kinds of item with a holiday lesson (section 3). [Default] Keep the plan's lesson list (the strands are the school strands), forbid item reuse by the register and TL2, and say in the tutor guide that holiday graduates will recognise the topic but not the questions. [Alternative] Swap the two largest overlaps (13 and 14 with H7; 24 and 25 with H4) for other Primary 3 topics; a swap costs about a day of re-planning each.
- **D3. Replacements of plan items that repeat the holiday or SASMO.** Dropped or replaced: handshakes (33), pages 1 to 130 (34), ages in 3 years (24), 3 l and 5 l jugs to 1 l (28), the 100 days weekday and the 50th shape (32), matchstick digits with 17 sticks (37), the 31st odd-digit number (34), multiples between a start and 100 with a 6s table (32), a Y of circles (26). [Default] All replaced as in section 1.
- **D4. Weak or no-evidence lessons.** 19, 21, 22, 26, 34, 36 keep their place as beyond school; lesson 23 has the weakest content. [Default] Keep all, mark 23 and 36 'safest to skip', and if lesson 23 fails the tutor trial replace it with 'Rounding and Estimating' (Primary 4 preview, p. 37) or 'Tables and Line Graphs' (Primary 4 preview).
- **D5. Cutting.** [Default] A grown-up, or the child with a grown-up, cuts before the lesson; scissors never in a lesson.
- **D6. Ruler, set square, string.** [Default] A 30 cm ruler from lesson 11, string from 13, a set square optional (a cut-out right-angle checker is supplied); no printed ruler (the Level 1 owner choice) and no real-size claim in the books.
- **D7. Marks on child pages.** [Default] None. The papers print marks; our pages use an 'Ans:' frame and a Working box, and the Quest has no score.
- **D8. Time and money forms.** [Default] 3:15 pm with a colon (accept 3.15 p.m.); 24-hour 14 30 (accept 1430); $3.20 and 1850¢ with the cent sign; money decimals only as add and subtract (multiply and divide of decimals is Primary 4).
- **D9. File layout and tools.** [Default] `term/l3/` holds the data; the Level 1 tools are imported through a `level` parameter (TL1) and new figures live in `figs4.py`. Moving the tools to a shared folder is cleaner but disturbs the agents still building Level 1; do it after Level 1 Term 4 is audited.
- **D10. Lesson 36 operator tiles.** [Default] Optional; children write the signs in boxes if the cutting load has to fall.
- **D11. Books and payment.** [Default] Both books of a term are issued with the first payment; a mid-term joiner receives the full book and the books to come; hand-off lines say 'your book'.
- **D12. When to build.** [Default] Build Term 1 now (wave A first), start the template work for Terms 2 to 4 in parallel, write Terms 3 and 4 only after the first tutor trial of Term 1 reports timing, then run one 40-lesson consistency sweep.
- **D13. Play money legal check.** [Default] Stylised notes marked PLAY MONEY; I have not checked Singapore's rules on reproducing notes and coins.
- **D14. Tutor reading aloud.** [Default] The tutor reads every Think harder stem and every Quest gate once aloud; Start here items are read by the children.
- **D15. Entry check for joiners.** [Default] A five-minute eight-question check of Primary 2 skills at sign-up, with a catch-up page per result (TL7); build it after the first trial.
- **D16. Lesson 10 as a content lesson.** [Default] Keep Price per Piece with the Quest; fallback in risk 10.
- **D17. Photo return of the Quest Log.** [Default] The parent sends the Quest Log to the business WhatsApp (+65 9880 5962); tutors never use personal phones; the number is not on slides.
- **D18. Hand-drawn figures (KIV for the old lessons 22 and 23, now 19, 21, 22).** [Default] No hand drawing: `cube_stack`, `panel`, the mirror figure (X11) and `fold_punch` generate every figure; the pyramid (X15) is optional and may be dropped.
- **D19. Wording evidence.** [Default] Items resting on a picture are marked 'wording unverified'. Please supply (or point me to) one Primary 3 paper or quiz on each of time (clock hands), money (notes and coins), bar graphs, balance pictures and cube views.
- **D20. Calculators.** [Default] None, and Mi never shows one.
- **D21. Weekly workload statement.** [Default] 'Home Practice (about 15 minutes) if you like; pages 3 to 5 and online practice are optional.' Reports use one descriptive line from the tutor's private notes, not a strand profile; the plan's four report lines (section 5 of the plan) become the sentence stems.
- **D22. Quest content reach.** [Default] Each Quest visits every lesson of its term through eight gates (section 8) and holds an unseen cave puzzle.
- **D23. Beyond field.** The beyond-syllabus rule is recorded (owner decisions, 23 Oct). [Default] The tutor-only `beyond` metadata field is required in all 40 lessons from the start (no retrofit needed at Level 3); the child-facing name is a puzzle title and never carries the word 'challenge'.
- **D24. Level code in the runner keys.** [Default] `l3t1l01` ... `l3t4l40`.

## 13. Build order, effort and cost

### 13.1 Dependencies in the content

Lesson 1 feeds 2 and 34; 2, 3, 4 feed 6, 10 and 32; 8 and 10 are a pair; 9 feeds 35 (and 23); 11 feeds 33; 12 feeds 27 and 28; 13 feeds 14 and 30; 7 feeds 27; 16 feeds 20; 24 and 25 are a pair (strips); 21 and 22 share X11 and X17; 31, 32 and 34 are independent; lessons 10, 20, 30, 40 need every earlier lesson of their term to have passed its fix pass (answers fixed) before the Quest is written. The plan says a lesson does not assume the previous one except through Remember, so these are build-order and wording-consistency dependencies, not content ones. Lesson 39 uses words from 6, 17, 25, 33 and must match their fixed wording ('strip', 'table', 'list', 'work backwards').

### 13.2 Waves and sprints

**Sprint A (day 0, one engineer, about half a day):** TL1 (level parameter), TL2 (copy-check list), TL8 (author brief), X5, X2, the add-and-subtract half of X1, KT1; then write **Lesson 1** (pilot of Level 3 conventions: identity, footers, the Opening script, the hand-off wording). **In parallel, wave A** (existing tools and kit work only): lessons 17, 19, 31, 39 (no kit or figure work) and 5, 6, 32, 36, 37 (a kit each).
**Sprint B (two engineers):** the rest of X1 (multiply, short division, unit headers), X3, X14, X4, X18, RN1 to RN6, KT2, KT3, KT4. **Wave B:** lessons 2, 3, 4, 8, 34, 38; lessons 7, 24 and 25 are wave E by their figures, but X4 and X14 are built in Sprint B, so they follow it.
**Sprint C:** X6, X7, X9, X13, X8, X10, RN3, RN7 and the kits KT5 to KT8, KT19 to KT21. **Waves C and D:** lessons 9, 11, 12, 16, 33, 35, 13, 14, 15, 23.
**Sprint E:** X11, X12, X17 (and X15, X16 if not deferred), KT9, KT11 to KT17. **Wave E:** lessons 18, 21, 22, 24, 25, 26, 27, 28, 29.
**Wave Q:** lessons 10, 20, 30, 40 last in their term, after TL3 and the Quest Logs; the term books (TL4) after each term's fix pass.
**Audit and fix per term**, then the three term-wide second-round audits (guide and deck; home, parent and practice; term-wide), as at Level 1. After Term 4: one 40-lesson consistency sweep (rewind items TL10, hand-offs against section 7, beyond table, books, B&W check), and the cold-join trial (lessons 1 and 11 with one child who has only done the holiday course).
Which lessons can be written first with the existing tools: 17, 19, 31, 39 (nothing to build), then 5, 6, 32, 36, 37 (a kit). Lessons 7, 12, 13 to 16, 21 to 23 cannot start until their figures exist.

### 13.3 Effort (agent-hours, not measured)

Per lesson, written as total hours = write and build + wording review + audit + fix pass, the Level 1 split (about 4.5, 0.7, 1.0, 1.3). Level 1 evidence: lesson totals 6.0 to 9.0, Quest lessons 12.5 to 13.5; Term 2 took about 6.5 hours wall clock from pre-flight to the end of the first fix pass with parallel agents.

| Term | Lesson totals | Sum |
|---|---|---|
| 1 | 1: 7.5, 2: 7.5, 3: 7.5, 4: 7.5, 5: 6.0, 6: 6.5, 7: 8.0, 8: 7.0, 9: 7.0, 10: 12.5 | 77.0 |
| 2 | 11: 7.0, 12: 7.5, 13: 7.5, 14: 7.0, 15: 7.0, 16: 7.0, 17: 6.0, 18: 7.0, 19: 6.5, 20: 13.0 | 75.5 |
| 3 | 21: 8.0, 22: 7.0, 23: 6.5, 24: 7.0, 25: 6.5, 26: 7.0, 27: 6.5, 28: 6.5, 29: 7.0, 30: 13.0 | 75.0 |
| 4 | 31: 6.0, 32: 6.5, 33: 7.0, 34: 6.5, 35: 7.0, 36: 6.0, 37: 7.0, 38: 6.5, 39: 6.5, 40: 12.5 | 71.5 |
| All | 40 lessons | **299.0** |

Plus four term-wide second-round audits (about 8 hours each, 32) and one 40-lesson consistency sweep (about 10): **about 340 agent-hours** for the lessons. Template engineering (section 5): **150 hours if everything is built, about 133 with the deferrals**. Together about 475 to 490 hours.

Elapsed time, at the Level 1 pace (eight to ten writing agents and three engineers working as in 13.2): Term 1 about 1.5 working days including the figure foundations, Term 2 about 1.5, Term 3 about 2, Term 4 about 2, plus audits and fixes, so **about 8 to 10 working days** from Sprint A to an audited Term 4; if the template work is done serially before any lesson starts, add about 2 days. Not in these numbers: a tutor trial per term, the cold-join trial, the legal check (D13), the owner's paper search (D19), and the owner and tutor review time (allow another 20 to 25 hours across the year).

## 14. What was not checked

- No lesson, tool or output was run or built; the figure inventory was read from the working tree, which holds uncommitted edits to `figs2.py`, `figs3.py` and `svg.py` by other agents, so section 5.1 reflects the tree on 23 Oct, not a commit. Hours are estimates.
- The holiday register compares question stems (first 100 characters of each of 23 or 24 questions per lesson) and the objective, skills and Explore lines; it did not read the holiday decks, scripts or workbooks, so an overlap that exists only there would be missed (TL2 reads the files).
- MOE placements come from `docs/moe/syllabus_by_level.md`; I did not find 'mm' in the Primary 3 length outcomes, so millimetres are not used.
- No Primary 3 picture was seen in any paper; no clock, graph, balance, coin or cube picture could be compared with a school style. The 2019 papers rest on OCR; about 16 of 39 2019 scans were never read.
- Singapore's rules on reproducing banknotes and coins were not checked.
- The Level 2, 4, 5 and 6 plans were not read for overlap; the Level 3 plan says lesson 36 (brackets) overlaps Level 4 lesson 1.2 and Level 5 lesson 1, and lesson 31 (factors) is Primary 4 content.
- Trivial Start here arithmetic written without a check id is for the author's own verify script; every id quoted in the lesson specs, the Quest tables and section 4 has a check in the appendix (178 checks).
- The 2027 term slot grid for 90-minute lessons is not re-derived here (owner entry of 23 Oct, still open).

## Appendix: the check script

`verify_l3_preflight.py`, run with `python3 -I verify_l3_preflight.py`. On 23 Oct 2026 it printed `verify_l3_preflight: 178 checks, 178 passed`. Checks are brute force: all digit pairs, all permutations, breadth-first search of jug states, all note counts, all clue sets, exhaustive fold simulations; they use no formula from the lessons.

```python
#!/usr/bin/env python3
"""Brute-force checks for every number quoted in docs/terms/l3_preflight.md (run: python3 -I verify_l3_preflight.py)."""
import itertools, math, datetime
from fractions import Fraction as F
from functools import lru_cache
from collections import deque

R = []
def ck(i, got, exp):
    ok = got == exp
    R.append((i, ok))
    if not ok: print("FAIL", i, "got", got, "expected", exp)

# ---------------- Term 1
ck("V1.1", ((1250 + 2750) // 2, (3490 + 3610) // 2), (2000, 3550))
ck("V1.2", len([n for n in range(3901, 4100) if n % 10 == 5]), 20)
s = [3200]
for k in range(8): s.append(s[-1] + (1000 if k % 2 == 0 else -200))
ck("V1.3", s[8], 6400)
ck("V1.4", [n for n in range(6401, 6700) if n % 100 == 0 and (n // 100) % 10 % 2 == 0], [6600])
ck("V1.5", (5003 - 1000, 3090 + 30), (4003, 3120))
ck("V1.6", (2000 + 3000) // 2, 2500)

def sfl(a, b):
    x, y = str(a).zfill(4), str(b).zfill(4)
    return int(''.join(str(abs(int(p) - int(q))) for p, q in zip(x, y)))
ck("V2.1", (4682 + 2739, 4700 + 2700, 9000 - 5826), (7421, 7400, 3174))
ck("V2.2", 6479 - 2583, 3896)
ck("V2.3", (5000 - 2467, sfl(5000, 2467)), (2533, 3467))
ck("V2.4", [(a, b) for a in range(10) for b in range(10) if int(f"4{a}76") - int(f"28{b}4") == 1792], [(6, 8)])

ck("V3.1", (327 * 6, 300 * 6 + 20 * 6 + 7 * 6), (1962, 1962))
ck("V3.2", (9 * 120 - 285) / 5, 159.0)
ck("V3.3", [(a, b) for a in range(10) for b in range(10) if int(f"3{a}7") * 6 == int(f"1{b}02")], [(1, 9)])
ck("V3.4", (7 * 3, 6 * 5 - 6, 36 * 4, 30 * 4 + 6 * 4), (21, 24, 144, 144))
ck("V3.5", (4 * 7, 45 // 3, 6 * 48 == 6 * 50 - 6 * 2), (28, 15, True))

ck("V4.1", divmod(487, 6), (81, 1))
ck("V4.2", (divmod(253, 8), -(-253 // 8)), ((31, 5), 32))
ck("V4.3", (54 % 6, 54 % 4, 54 % 9), (0, 2, 0))
ck("V4.4", 12 * 7 + 5, 89)
c9 = [n for n in range(100, 1000) if n % 9 == 5]
ck("V4.5", (min(c9), max(c9)), (104, 995))
ck("V4.6", (divmod(84, 4), divmod(156, 3), divmod(803, 4)), ((21, 0), (52, 0), (200, 3)))

ck("V5.1", (76 + 24, 28 + 72, 12 + 88, 76 + 28 + 24 + 12 + 88 + 72), (100, 100, 100, 300))
ck("V5.7", 64 + 36, 100)
l = list(range(11, 42, 3)); ck("V5.2", (len(l), sum(l)), (11, 286))
ck("V5.3", 48 * 9 - 300, 132)
ck("V5.4", 250 + 138 - 238, 150)
ck("V5.5", [(a, b) for a, b in itertools.combinations([275, 640, 725, 360, 590], 2) if a + b == 1000], [(275, 725), (640, 360)])
l = list(range(105, 176, 7)); ck("V5.6", (len(l), sum(l)), (11, 1540))

ck("V6.1", 1308 - 275 + 120, 1153)
ck("V6.2", ((515 - 49) // 2, (515 - 49) // 2 + 49, (515 - 49) % 2), (233, 282, 0))
ck("V6.3", (27 // 3, 27 // 3 * 4), (9, 36))
ck("V6.4", (6 * 250 - 475) / 5, 205.0)
ck("V6.5", (91 - 14) % 2, 1)
ck("V6.6", 1246 - 358, 888)

ck("V7.1", (F(6, 8), F(10, 12), F(8, 12)), (F(3, 4), F(5, 6), F(2, 3)))
ck("V7.2", sorted([F(5, 8), F(2, 3), F(3, 4)]), [F(5, 8), F(2, 3), F(3, 4)])
ck("V7.3", (F(1, 4) + F(3, 8), F(5, 6) - F(1, 2)), (F(5, 8), F(1, 3)))
ck("V7.4", F(3, 4) * 12, 9)
ck("V7.5", ([n for n in range(1, 12) if F(1, 3) < F(n, 12) < F(1, 2)], [n for n in range(1, 24) if F(1, 3) < F(n, 24) < F(1, 2)]), ([5], [9, 10, 11]))
ck("V7.6", F(1, 2) + F(1, 3) + F(1, 6), 1)
ck("V7.7", 5 - 2, 3)
ck("V7.8", F(4, 8) == F(3, 6), True)

ck("V8.1", (round(4.50 + 2.85, 2), round(20 - 13.65, 2)), (7.35, 6.35))
ck("V8.2", min((3 * c + 10 * b, b, c) for b in range(4) for c in range(12) if 4 * b + c == 11), (29, 2, 3))
menu = {'roti': 240, 'laksa': 590, 'tea': 180, 'cake': 370, 'juice': 260}
ck("V8.3", [(a, b) for a, b in itertools.combinations(menu, 2) if menu[a] + menu[b] == 830], [('roti', 'laksa')])
ck("V8.4", [(a, b) for a in range(16) for b in range(10) if 4 * a + 7 * b == 59 and a + b < 12], [(6, 5)])
ck("V8.5", [(x, y) for x in range(6) for y in range(14) if 5 * x + 2 * y == 26], [(0, 13), (2, 8), (4, 3)])

ck("V9.1", 3 * 60 + 15, 195)
ck("V9.2", (9 * 60 + 20) - (7 * 60 + 45), 95)
ck("V9.3", (17 * 60 + 10) - (2 * 60 + 25), 14 * 60 + 45)
ck("V9.4", (8 * 60 + 35) + 12, 8 * 60 + 47)
ck("V9.5", ((2 * 60 + 45) - 25, (4 * 60 + 20) - 25), (2 * 60 + 20, 3 * 60 + 55))
D = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
ck("V9.6", D[(D.index('Tue') + 45) % 7], 'Fri')
ck("V9.7", (datetime.date(2027, 4, 30) + datetime.timedelta(7)).day, 7)
ck("V9.8", (2 + 12, 30), (14, 30))

ck("V10.1", (77 // 11, 4 * 7, 7 * 7), (7, 28, 49))
ck("V10.2", [(c, t) for c in range(1, 10) for t in range(1, 10) if 3 * c + t == 17 and c + t == 9], [(4, 5)])
ck("V10.3", 28 // 4, 7)
ck("V10.4", (5 + 3, 64 // 8, 64 // 8 * 5), (8, 8, 40))
ck("V10.5", 24 // 4, 6)
@lru_cache(None)
def cost(n):
    if n == 0: return 0
    return min(p + cost(n - k) for k, p in ((1, 3), (2, 5), (5, 11)) if n >= k)
ck("V10.6", cost(9), 21)
ck("V10.7", (12 // 4, 120 // 6, 24 // 8), (3, 20, 3))
ck("V10.8", (F(12, 5) < F(8, 3), float(F(12, 5)), round(float(F(8, 3)), 2)), (True, 2.4, 2.67))

# ---------------- Term 2
ck("V11.1", 54 // 6 + 1, 10)
ck("V11.2", (24 // 4, (21 - 1) * 6), (6, 120))
ck("V11.3", (3250 + (3250 + 650) + (3250 + 650 - 1400)), 9650)
ck("V11.4", 2 * (350 + 150) * 3, 3000)
ck("V11.5", 4080 - 3960, 120)
ck("V11.6", (25 - 1) * 3, 72)
ck("V11.7", (7 - 1) * (9 // (4 - 1)), 18)
ck("V11.8", 2 * 1000 + 350, 2350)
ck("V11.9", 1450 + 2650, 4100)

ck("V12.1", 3095 - 3000, 95)
ck("V12.2", 4750 + 1380, 6130)
ck("V12.3", 900, 900)
ck("V12.4", 3000 // (5 - 2), 1000)
ck("V12.5", 5 * 4 * 150, 3000)
ck("V12.6", (1200 - 450) // 3, 250)
ck("V12.7", (7200 - 5200, 5200 - 3000), (2000, 2200))

ck("V13.1", (36 // 4) ** 2, 81)
ck("V13.2", [(2 * (a + b), a * b) for a, b in ((10, 2), (8, 4), (6, 6))], [(24, 20), (24, 32), (24, 36)])
ck("V13.3", (56 // 2 - 18, (56 // 4) ** 2), (10, 196))
ck("V13.4", (5 * 2 + 2, 36 // 12, 5 * (36 // 12) ** 2), (12, 3, 45))
ck("V13.5", 2 * (12 + 5 + 7) - 2 * (12 + 7), 10)

ck("V14.1", 8 + 6 // 2, 11)
ck("V14.2", 12 * 4 + 18 * 6, 156)
ck("V14.3", 7 * 3 + 4 * 5, 41)
ck("V14.4", 54 // 6, 9)

ck("V15.1", 3 * 4 * 4, 48)

A = 40; B = 2 * A; Dd = A - 15; C = 150 - A - B - Dd
ck("V16.1", (C, A + B + C + Dd), (5, 150))
ck("V16.2", [150 // 10 * k for k in (2, 3, 5)], [30, 45, 75])
d = {'3A': 35, '3B': 50, '3C': 20, '3D': 45}
ck("V16.3", (sum(d.values()), d['3A'] - d['3C'], d['3C'] + d['3D'] > d['3B'], d['3D'] == 2 * d['3C']), (150, 15, True, False))

ck("V17.1", (4 * 10 + 2, (90 - 2) // 4), (42, 22))
g = [3]
for k in range(1, 6): g.append(g[-1] + 2 * k)
ck("V17.2", g, [3, 5, 9, 15, 23, 33])
rules = [(p, q) for p in range(-9, 10) for q in range(-9, 10) if all(p * a + q * b == r for a, b, r in [(5, 2, 13), (4, 4, 8), (7, 1, 20), (6, 3, 15)])]
ck("V17.3", (rules, 3 * 9 - 5), ([(3, -1)], 22))
s = [1200]
for k in range(8): s.append(s[-1] + (300 if k % 2 == 0 else -50))
ck("V17.4", s[8], 2200)
ck("V17.5", sorted(set(range(5, 400, 4)) & set(range(3, 400, 5)))[:3], [13, 33, 53])
ck("V17.6", (4 * 1 + 2, 4 * 2 + 2, 4 * 3 + 2), (6, 10, 14))

a_, p_, m_ = 9, 6, 8
ck("V18.1", (2 * a_ == 3 * p_, 4 * p_ == 3 * m_, max([('apple', a_), ('plum', m_), ('pear', p_)], key=lambda x: x[1])[0]), (True, True, 'apple'))
ck("V18.2", [x for x in range(30) if 5 * x + x == 3 * 14 + 6], [8])
ck("V18.3", [(m, li) for m in range(1, 10) for li in range(1, 10) if 3 * m + 2 * li == 19 and 3 * m + li == 14], [(3, 5)])
ck("V18.4", 180 - 2 * 45, 90)

H = [[2, 1, 3], [0, 2, 1], [1, 1, 2]]
ck("V19.1", (sum(map(sum, H)), sum(1 for r in H for x in r if x > 0), sum(max(H[r][c] for r in range(3)) for c in range(3))), (13, 8, 7))
fv = [3, 1, 2]; mn = 10**9; mx = 0
for h in itertools.product(range(1, 4), repeat=6):
    cols = [(h[0], h[1]), (h[2], h[3]), (h[4], h[5])]
    if all(max(c) == fv[i] for i, c in enumerate(cols)):
        mn = min(mn, sum(h)); mx = max(mx, sum(h))
ck("V19.2", (mn, mx), (9, 12))

# ---------------- Term 3
def pieces(n, c):
    w = 2 ** -n
    return len([k * w + (c if k % 2 == 0 else w - c) for k in range(2 ** n)]) + 1
ck("V21.1", (2 ** 2, 2 ** 3), (4, 8))
ck("V21.2", pieces(3, 0.03), 9)
cyc = "CSTTSC"; beads = [cyc[i % 6] for i in range(100)]
ck("V22.1", (beads[99], beads.count('T')), ('T', 34))
ck("V22.2", all(r[0] ^ r[1] == r[2] for r in [({'c', 's'}, {'s', 't'}, {'c', 't'}), ({'c'}, {'s'}, {'c', 's'})]), True)
dd = 0
for t, q in [('R', 1), ('R', 2), ('L', 1), ('R', 3)]: dd = (dd + (q if t == 'R' else -q)) % 4
ck("V23.1", dd, 1)
cnt = 0
for h in range(6):
    for m in (0, 15, 30, 45):
        hh = (h % 12) * 30 + m * 0.5; mm = m * 6; a = abs(hh - mm); a = min(a, 360 - a)
        if a > 90: cnt += 1
ck("V23.2", cnt, 11)
def hand_angle(h, m):
    hh = (h % 12) * 30 + m * 0.5; mm = m * 6; a = abs(hh - mm); return min(a, 360 - a)
ck("V23.3", [t for t in ((3, 0), (4, 15), (6, 30), (9, 0)) if hand_angle(*t) == 90], [(3, 0), (9, 0)])
ck("V24.1", (96 // 4, 6 * (96 // 4)), (24, 144))
ck("V24.2", (117 // 13, 117 // 13 * 4, 117 // 13 * 8), (9, 36, 72))
ck("V24.4", (72 // 4, 72 // 4 * 3, 72 // 4 * 3 - 72 // 4), (18, 54, 36))
ck("V24.5", round(1.60 * 3 + 2.40, 2), 7.20)
ck("V25.1", 150 - 2 * 40, 70)
ck("V25.2", (100 - 13.20 - 14.80) / 4, 18.0)
ck("V25.3", ((90 + 40) // 2, (90 - 40) // 2, (90 + 20) // 2, (90 + 40) // 2 - (90 + 20) // 2), (65, 25, 55, 10))
ck("V25.4", 150 // 2, 75)
sols = {}
for perm in itertools.permutations(range(1, 10)):
    c = perm[:3]; mid = perm[3:]
    s1 = c[0] + mid[0] + mid[1] + c[1]; s2 = c[1] + mid[2] + mid[3] + c[2]; s3 = c[2] + mid[4] + mid[5] + c[0]
    if s1 == s2 == s3: sols[s1] = sols.get(s1, 0) + 1
ck("V26.1", sorted(sols), [17, 19, 20, 21, 23])
tot = {}
for m in (2, 4, 6, 8, 10):
    rest = [x for x in (2, 4, 6, 8, 10) if x != m]
    for a, b, c, d2 in itertools.permutations(rest):
        if a + b == c + d2: tot[m] = a + b + m
ck("V26.2", tot, {2: 16, 6: 18, 10: 20})
ms = [p for p in itertools.permutations(range(1, 10)) if all(sum(p[3*i:3*i+3]) == 15 for i in range(3)) and all(sum(p[i::3]) == 15 for i in range(3)) and p[0]+p[4]+p[8] == 15 and p[2]+p[4]+p[6] == 15]
ck("V26.3", (len(ms), set(p[4] for p in ms)), (8, {5}))
ck("V26.4", (sum(range(1, 10)), sum(range(1, 10)) // 3), (45, 15))
ck("V27.1", (F(3, 4) * 100, F(2, 5) * 1000, F(5, 8) * 1000, F(3, 10) * 1000, F(3, 4) * 60, F(1, 5) * 100), (75, 400, 625, 300, 45, 20))
ck("V27.2", (1 - F(1, 3) - F(1, 4), F(3, 4) * 24), (F(5, 12), 18))
ck("V27.3", F(3, 4) - F(1, 2), F(1, 4))
def bfs(a, b, target):
    start = (0, 0); dq = deque([(start, 0)]); seen = {start}
    while dq:
        (x, y), dist = dq.popleft()
        if x == target or y == target: return dist
        nxt = [(a, y), (x, b), (0, y), (x, 0)]
        t = min(x, b - y); nxt.append((x - t, y + t)); t = min(y, a - x); nxt.append((x + t, y - t))
        for st in nxt:
            if st not in seen: seen.add(st); dq.append((st, dist + 1))
ck("V28.1", (bfs(5, 8, 3), bfs(4, 7, 6), bfs(4, 7, 5), bfs(3, 5, 1)), (2, 6, 8, 4))
names = ['Ali', 'Ben', 'Cara', 'Dev']
cl = [lambda s: s['Ben'] in (1, 4), lambda s: abs(s['Ali'] - s['Ben']) == 1, lambda s: abs(s['Ali'] - s['Cara']) != 1, lambda s: s['Ali'] < s['Ben']]
def solve(cs): return [dict(zip(names, p)) for p in itertools.permutations(range(1, 5)) if all(c(dict(zip(names, p))) for c in cs)]
ck("V29.1", solve(cl), [{'Ali': 3, 'Ben': 4, 'Cara': 1, 'Dev': 2}])
ck("V29.2", [len(solve([c for j, c in enumerate(cl) if j != i])) > 1 for i in range(4)], [True] * 4)
ck("V29.3", [(c, c + 15 + 20) for c in (1, 100)], [(1, 36), (100, 135)])
rl = [(a, b) for a in range(1, 12) for b in range(a, 12) if 2 * (a + b) == 24]
ck("V30.1", (len(rl), max((a * b, a, b) for a, b in rl)), (6, (36, 6, 6)))

# ---------------- Term 4
ck("V31.1", [n for n in range(100, 1000) if n % 2 == 0 and n % 3 == 0 and n // 100 == 2 * ((n // 10) % 10)], [210, 216, 420, 426, 630, 636, 840, 846])
ck("V31.2", [n for n in (int(f"6{x}3{x}") for x in range(10)) if n % 3 == 0], [6030, 6333, 6636, 6939])
def nf(n): return len([k for k in range(1, n + 1) if n % k == 0])
ck("V31.3", (nf(36), [n for n in range(2, 50) if nf(n) == 3], [n for n in range(2, 60) if nf(n) == 4][:6]), (9, [4, 9, 25, 49], [6, 8, 10, 14, 15, 21]))
ck("V31.4", [(a, 12 // a) for a in range(1, 4) if 12 % a == 0], [(1, 12), (2, 6), (3, 4)])
ck("V32.1", len([n for n in range(1, 121) if n % 4 == 0 or n % 6 == 0]), 40)
ck("V32.2", 150 // 7 - 39 // 7, 16)
ck("V32.3", D[(D.index('Thu') + 95) % 7], 'Mon')
ck("V32.4", (pow(3, 20, 10), pow(7, 25, 10)), (1, 7))
ck("V32.5", (divmod(1250, 8), 100 // 7), ((156, 2), 14))
ck("V32.6", pow(3, 8, 10), 1)
ck("V33.1", (3 * 4, len(list(itertools.combinations(range(5), 2))), len(list(itertools.combinations(range(5), 3)))), (12, 10, 10))
ck("V33.2", 5 * 4 - 1, 19)
def rects(r, c): return (r * (r + 1) // 2) * (c * (c + 1) // 2)
cnt = sum(1 for r1 in range(3) for r2 in range(r1, 3) for c1 in range(3) for c2 in range(c1, 3))
ck("V33.3", (cnt, rects(3, 3), rects(2, 4), rects(2, 3)), (36, 36, 30, 18))
ck("V33.4", (4 * (7 - 1), 72 // 6), (24, 12))
ck("V33.5", 2 * 3, 6)
def nth_even(k):
    c = 0; n = 0
    while c < k:
        n += 1
        if all(ch in '02468' for ch in str(n)): c += 1
    return n
ck("V34.1", nth_even(40), 260)
def digits_to(p): return sum(len(str(i)) for i in range(1, p + 1))
ck("V34.2", [p for p in range(1, 500) if digits_to(p) == 192], [100])
ck("V34.3", sum(str(i).count('3') for i in range(1, 151)), 35)
ck("V34.4", digits_to(130), 282)
ck("V34.5", sum(int(ch) for i in range(1, 31) for ch in str(i)), 168)
ck("V34.6", nth_even(5), 20)
ck("V34.7", (digits_to(12), digits_to(20), digits_to(25)), (15, 31, 41))
ck("V34.8", len([n for n in range(10, 100) if all(c in "02468" for c in str(n))]), 20)
def tm(h, m): return h * 60 + m
P = ([tm(10, 0), tm(12, 30)], 130); Q = ([tm(11, 0), tm(13, 45)], 110)
res = []
for first, second, tag in ((P, Q, 'PQ'), (Q, P, 'QP')):
    for s1 in first[0]:
        e1 = s1 + first[1]
        for s2 in second[0]:
            if s2 >= e1 + 15: res.append((s2 + second[1], tag))
ck("V35.1", sorted(res), [(tm(15, 35), 'PQ')])
def reach(cards):
    out = set()
    def rec(nums):
        if len(nums) == 1: out.add(nums[0]); return
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                rest = [nums[k] for k in range(len(nums)) if k not in (i, j)]
                a, b = nums[i], nums[j]
                for v in {a + b, a - b, a * b}: rec(rest + [v])
    rec([F(c) for c in cards]); return out
r = reach((2, 3, 5, 8))
ck("V36.1", ([t for t in range(1, 11) if F(t) in r], F(24) in r), (list(range(1, 11)), True))
cost2 = {d: 5 for d in range(10)}; cost2[1] = 2; cost2[7] = 3; cost2[4] = 4
@lru_cache(None)
def maxd(t):
    if t == 0: return 0
    return max([1 + maxd(t - v) for d, v in cost2.items() if v <= t] + [-10**9])
def best(total, banned=()):
    global cost2
    keep = dict(cost2)
    cost2 = {d: v for d, v in keep.items() if d not in banned}
    maxd.cache_clear()
    try:
        return _best(total)
    finally:
        cost2 = keep; maxd.cache_clear()
def _best(total):
    nd = maxd(total); t = total; out = []
    for pos in range(nd):
        for d in sorted(cost2, reverse=True):
            if pos == 0 and d == 0: continue
            if cost2[d] <= t and maxd(t - cost2[d]) == nd - pos - 1:
                out.append(d); t -= cost2[d]; break
    return nd, int(''.join(map(str, out)))
ck("V36.2", ((12 - 4) * 2, 12 - (4 * 2)), (16, 4))
ck("V37.1", best(19), (9, 711111111))
ck("V37.5", best(19, (7,)), (8, 91111111))
@lru_cache(None)
def fewest(a):
    if a == 0: return 0
    return min(1 + fewest(a - d) for d in (100, 50, 10, 5, 2, 1) if d <= a)
ck("V37.2", (fewest(186), fewest(73), fewest(137)), (7, 5, 6))
ck("V37.3", (52 - 2 * 18) // 2, 8)
@lru_cache(None)
def most(b):
    return max([k + most(b - p) for k, p in ((1, 3), (3, 8), (7, 17)) if p <= b] + [0])
ck("V37.4", most(60), 24)
sums = [sum(c) for c in itertools.combinations(range(2, 10), 3)]
ck("V38.1", (min(sums), max(sums), 25 in sums, 20 in sums), (9, 24, False, True))
odd = list(range(1, 20, 2)); tt = set(sum(c) for c in itertools.combinations(odd, 5))
ck("V38.2", (min(tt), max(tt), 50 in tt, all(t % 2 for t in tt)), (25, 75, False, True))
ck("V38.3", [(A, B, C) for A, B, C in itertools.permutations(range(10), 3) if A > 0 and C > 0 and (10 * A + B) * 7 == 100 * C + 10 * A + C], [(4, 9, 3)])
ck("V39.1", (round(46.80 + 12.30, 2), 8 * 24, 6 * 20, 6 * 24), (59.10, 192, 120, 144))
bd = {'red': 36, 'blue': 24, 'green': 15}
vals = {}
for (a, x), (b, y) in itertools.combinations(bd.items(), 2):
    vals[('sum', a, b)] = x + y; vals[('diff', a, b)] = abs(x - y)
ck("V39.2", [k for k, v in vals.items() if v == 51], [('sum', 'red', 'green')])

# ---------------- Quest gate items
ck("Q1.1", (1000 + 6205, 4382 + 2519, 64 + 29 + 36, 34 * 6, divmod(85, 4)), (7205, 6901, 129, 204, (21, 1)))
ck("Q1.2", (3 * 4 + 2, 20 - 14, F(3, 6), F(3, 4) > F(5, 8)), (14, 6, F(1, 2), True))
ck("Q1.3", (round(2.50 + 3.45, 2), round(10 - 5.95, 2), 2 * 60 + 40 + 95 == 4 * 60 + 15, 15 // 5, 8 * 3), (5.95, 4.05, True, 3, 24))
ck("Q2.1", ((7 - 1) * 5, 3250 + 1900, 2 * (9 + 4), 9 * 4, 35 - 20, 4 * 10 + 1, 4 * 10 // 2), (30, 5150, 26, 36, 15, 41, 20))
ck("Q3.1", (2 ** 2, 24 * 4, 85 + 40, 15 - 8 - 6, 2 * (12 + 8), 2 * (12 + 8) * 5), (4, 96, 125, 1, 40, 200))
ck("Q4.1", (4 + 7 + 2 + 5, 4725 % 3, D[(D.index('Thu') + 20) % 7], 3 * 4, 9 + 16 * 2, tm(7, 40) + 45 == tm(8, 25), (8 - 5) * 4, fewest(62), 36 // 4 * 3), (18, 0, 'Wed', 12, 41, True, 12, 3, 27))

ck("Q2.2", (3 * 4 + 2 * 3, 20 - 18), (18, 2))
ck("Q3.2", (1 + 2) % 4, 3)
g3 = [p for p in itertools.permutations(range(1, 4)) if p[0] in (1, 3) and abs(p[0] - p[1]) != 1 and p[2] < p[0]]
ck("Q3.4", g3, [(3, 1, 2)])
cv = {}
for m in (1, 3, 5, 7, 9):
    rest = [x for x in (1, 3, 5, 7, 9) if x != m]
    for a, b, c, d2 in itertools.permutations(rest):
        if a + b == c + d2: cv[m] = a + b + m
ck("Q3.5", cv, {1: 13, 5: 15, 9: 17})
ck("Q4.2", 30 // 5 * 4, 24)
print("verify_l3_preflight: %d checks, %d passed" % (len(R), sum(1 for r in R if r[1])))
```
