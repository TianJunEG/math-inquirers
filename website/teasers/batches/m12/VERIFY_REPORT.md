# Teaser batch m12 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 31 | 31 | 1 | 21 | 3 | 31 |
| 2 | 31 | 31 | 1 | 26 | 3 | 31 |
| 3 | 31 | 27 | 3 | 23 | 3 | 31 |
| 4 | 31 | 30 | 2 | 26 | 2 | 31 |
| 5 | 31 | 30 | 2 | 26 | 2 | 31 |
| 6 | 31 | 30 | 2 | 25 | 2 | 31 |

Sources searched (whole working tree, tracked or not): 6760 files, 1363.2 MB, sha256 f23be12b38f2ffc78ecacad9.  Files per root: deck 158, diag 12, docs 423, extension 257, hp 41, k2 5, levels 23, mascot 4, ops 14, outputs 180, p1 1, p2 27, p3 27, p4 27, p5 28, p6 38, portal 45, practice 373, print 6, rebuild 87, releases 1, review 1, school 474, split 1801, taster 2, term 2532, tutor 130, website 42, worker 1.

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 0. REVIEW items: 84.


- REVIEW L1-lockerdigits [12-02]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-lockerdigits [12-02]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L1-circlekids [12-05]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-biscuithalves [12-06]: rule S: sentence "Aisha cuts a round biscuit in two equal pieces with one straight cut t" shares 5 content words with "A round pizza has 3 straight cuts, all through the middle." (k2/Math_Inquirers_K2_Starter_Pack.pdf)
- REVIEW L1-bookshelf [12-10]: story words 3 of 4 like "Q: The books in the library were placed on 30 shelves with an equal number of books on eac ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L1-purse [12-13]: rule S (window): 5 of 7 content words (box,cent,coin,money,twenty) in "Express the amount saved Jan to May as a fraction of pocket money rece ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L1-eggtrays [12-14]: story words 3 of 5 like "| Prelim | 2023 | TaoNan | P2-11 | 4 | Hawkers A and B buy same number of trays; big 30? a ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L1-stonehops [12-15]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-rulerbill [12-18]: rule B: 3 of the same numbers ['3', '4', '9'] as "Picture-dependent items re-solved from the picture, not the key: B1 L1 S1 (26),  ..." (term/l1/audit/AUDIT_BOOKS_1_4_ROUND2.md)
- REVIEW L1-sudoku3 [12-22]: rule S (window): 8 of 11 content words (bottom,column,fill,grid,middle,row,square,top) in "List the possibilities in order.", "steps": ["Both squares in the midd ..." (practice/holiday/p4/08/dist/data/p4l08.json)
- REVIEW L1-oddbig [12-23]: rule B: 3 of the same numbers ['12', '24', '8'] as "Why is the odd one so much bigger?', a: '24 (1, 2, 3, 4, 6, 8, 12, 24) and 105 ( ..." (p6/content/l2.js)
- REVIEW L1-traysame [12-25]: story words 5 of 7 like "Pupils colour their own copy. Colour key: 1260 = yellow, 1680 = red, 2520 = blue, 3360 = g ..." (school/p4/out/S1_key.html)
- REVIEW L1-marbleswap [12-26]: rule B: 3 of the same numbers ['11', '3', '4'] as "| 13 | 2 Missing Digit Mysteries | 3[ ]5 + 214 = 579; 6[ ]8 - 205 = 433; [ ] - 1 ..." (docs/terms/l2_preflight.md)
- REVIEW L1-chartwalk [12-28]: number 100 in the question is not a parameter (written in the wording; check)
- REVIEW L1-chartwalk [12-28]: rule S: sentence "He moves it down 3 rows, then right 2 squares, then up 1 row." shares 4 content words with "It moves down 1, then right 1." -> "A counter is on 26 on the 100 squa" (term/l1/WORDING_REVIEW_L04.md)
- REVIEW L1-twodice [12-31]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-lessonend [12-04]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L2-lessonend [12-04]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L2-lessonend [12-04]: number 20 in the question is not a parameter (written in the wording; check)
- REVIEW L2-lessonend [12-04]: rule B: 3 of the same numbers ['20', '50', '55'] as "min</text></svg>", "marking_mode": "auto", "frame": "Ends at Hours: {f1} Minutes ..." (practice/holiday/p3/09/dist/data/p3l09.json)
- REVIEW L2-windowsolids [12-09]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L2-windowsolids [12-09]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-11]: number 35 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-11]: number 39 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-11]: story words 4 of 6 like "What happens to the gap between them?", "steps": ["At the start Tank A has 60 litres more  ..." (practice/holiday/p4/09/dist/data/p4l09.json)
- REVIEW L2-tankwater [12-11]: rule S: sentence "A water tank holds 42 litres at the start of Monday." shares 4 content words with "**B3.1** [G] Two water tanks hold 90 litres altogether." (docs/books/word_problems_g1_g2_original_draft.md)
- REVIEW L2-seesaw [12-14]: story words 5 of 8 like "l2_scale level balance scales: scales [{left: [obj, ...], right: [obj, ...], label?}], obj ..." (extension/tools/figs_l2_u09.py)
- REVIEW L2-toyboxshape [12-16]: rule S (window): 8 of 11 content words (box,cone,cube,cylinder,face,flat,solid,sphere) in "Stacks of cubes (S05, S09, C03) are taught by one line ("count layer b ..." (extension/l2/AUDIT.md)
- REVIEW L2-walletmoney [12-17]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stickgame [12-19]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-gardenfence [12-25]: story words 3 of 4 like "Start with the shortest width, 1 m, and list in order.", "steps": ["Half of 18 m is 9 m, s ..." (practice/holiday/p3/07/dist/data/p3l07.json)
- REVIEW L2-gardenfence [12-25]: rule S3: the sentence "A garden is a rectangle 20 m long and 11 m wide." is like "ch=[('1.','A garden is 10 m long and 8 m wide." (rebuild/gen_p4l7.py)
- REVIEW L2-recyclegrid [12-28]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-recyclegrid [12-28]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-recyclegrid [12-28]: rule B: 3 of the same numbers ['3', '50', '58'] as "sol_fig=lambda f: combine([one_graph(FOUR, ['1', '2', '3', '4'], 50, 60, 1, 5, ' ..." (practice/holiday/p4/09/lesson.py)
- REVIEW L2-chocbar [12-31]: rule C: two four-word runs shared with "| C1 | Fill in the box: 1/2 = ?/10 | A chocolate bar has 10 equal pieces. ..." (docs/audit/gifted_fixes_p3.md): a chocolate bar has / chocolate bar has #
- REVIEW L2-chocbar [12-31]: rule S: sentence "A chocolate bar has 4 rows of 7 squares." shares 4 content words with "Count the squares in a bar of chocolate by rows." (outputs/print/term/Math_Inquirers_L1_T4_Book8_Lessons06-10_AnswerKey_TUTOR_PRINT.pdf)
- REVIEW L3-raffledays [12-02]: story words 3 of 5 like "| SA1 | 2021 | Raffles | B2-11 | 4 | graph | 3 | 1 | Buns sold Monday to Friday 500 total; ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L3-raffledays [12-02]: rule S: sentence "It sold 126 on Friday, 238 on Saturday, 184 on Sunday and 97 on Monday" shares 4 content words with ""text": "Friday 1, Saturday 2, Sunday 3, Monday 4." (term/l1/lessons/l27.json)
- REVIEW L3-buttonjar [12-03]: story words 4 of 5 like "Then 10 more red cubes are put in." Holiday `l3.js` line 144: "A jar has 12 red beads and  ..." (extension/l5/AUDIT_ROUND2.md)
- REVIEW L3-raffledigits [12-04]: story words 3 of 4 like "21:('Letters and Brackets',[('EXP','T','stamps at n cents paid with $5: change in terms of ..." (docs/books/private_p6_papers/build_plan_section.py)
- REVIEW L3-handshake8 [12-05]: story words 4 of 6 like "Keep going down the list.", "steps": ["Friend 1 shakes hands with the other {n} - 1 friend ..." (practice/holiday/p6/05/dist/data/p6l05.json)
- REVIEW L3-handshake8 [12-05]: rule S: sentence "Each pair of children shakes hands exactly once." shares 4 content words with "Every pair of friends shakes hands once." (practice/holiday/p6/05/dist/data/p6l05.json)
- REVIEW L3-lanes5 [12-07]: story words 3 of 4 like "How many seats were there in the school hall? - [EOY_2024_Raffles Q36, 2m, Seats rows/colu ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L3-moneybox [12-10]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-floortiles2 [12-13]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L3-floortiles2 [12-13]: rule S3: the sentence "A vegetable plot is a rectangle 13 m long and 7 m wide." is like "| A rectangle is 10 m long and 8 m wide." (docs/audit/gifted_fixes_p3.md)
- REVIEW L3-ropepieces [12-14]: rule S3: the sentence "A rope 33 metres long is cut into two pieces." is like "**15.3** A rope is cut into 2 pieces." (docs/sasmo/g2_original_problems_draft.md)
- REVIEW L3-stallminutes [12-15]: story words 3 of 5 like "### Lesson 6: Market Day **Total 103.3 (fast 93, slow 115).** Warm-up **OVER +4.0**: six i ..." (docs/audit/timing_p2.md)
- REVIEW L3-fishmass [12-16]: story words 3 of 4 like "Change it to cm.", "Add the lengths of the {k} pieces.", "Take that away from the ribbon:  ..." (practice/holiday/p3/09/dist/data/p3l09.json)
- REVIEW L3-clubs [12-19]: story words 3 of 4 like "f"From {cats[ri[0]]} to {cats[ri[1]]}, the number went up by how many?", f"How many pupils ..." (school/p4/gen/pages_d.py)
- REVIEW L3-fairtables [12-23]: rule C: two four-word runs shared with "Each table seats 4 people or 6 people. ..." (practice/holiday/p4/10/dist/data/p4l10.json): each table seats # / table seats # people
- REVIEW L3-cryptsum [12-24]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-smalldigitsum [12-28]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-01]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-01]: number 00 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-01]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-01]: number 00 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-01]: rule S3: the sentence "A hall clock gains 20 minutes in every real hour." is like ""text": "A clock gains 3 minutes every hour." (extension/data/l2_u09.json)
- REVIEW L4-liftfloors [12-04]: story words 5 of 8 like "Which number should go in the block "change floor by ( )"?", "svg": "<svg overflow="visibl ..." (practice/holiday/p6/03/dist/data/p6l03.json)
- REVIEW L4-digitfive [12-09]: rule B: 3 of the same numbers ['3', '4', '5'] as "Circle the quicker way: take away or count up." (blank had a hidden second quest ..." (term/l1/WORDING_REVIEW_L07.md)
- REVIEW L4-nametags [12-12]: rule C: two four-word runs shared with "G2 **CTX.** Cans are sold in packs of 6 for $5.40 and 8 for $6.80. ..." (docs/terms/l4_preflight.md): are sold in packs / sold in packs of
- REVIEW L4-pencilpacks [12-19]: rule C: two four-word runs shared with "I('pack', 5, 6, GF, 'Totals you cannot make', 'Make a table', ['Cookies are sold ..." (levels/gap_items.py): are sold in packs / sold in packs of
- REVIEW L4-sundaes [12-24]: rule B: 3 of the same numbers ['3', '4', '5'] as "**Gaps and posts on a line are set in every term.** "10 trees at equal distances ..." (docs/books/p3_school_paper_patterns.md)
- REVIEW L4-reachtotal [12-29]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-climbing [12-02]: number 358 in the question is not a parameter (written in the wording; check)
- REVIEW L5-dronepaths [12-03]: rule S: sentence "It makes five moves: 22 m north, 25 m east, 11 m south, 7 m west and 9" shares 4 content words with "(1) south-east (2) south-west (3) north-east (4) north-west ANSWER:" (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L5-redeye [12-08]: story words 3 of 4 like "| 31 | Factors, Multiples and Tests | Every number is a rectangle in waiting, and its digi ..." (docs/pedagogy/term_review.md)
- REVIEW L5-roundtable [12-15]: story words 5 of 7 like "- **Go further.** Six children sit round a table; clues give next to, opposite; place ever ..." (docs/terms/l1_term2_preflight.md)
- REVIEW L5-penboxes [12-17]: rule S: sentence "A box of red pens has 4 times as many pens as a box of blue pens." shares 4 content words with "**A5.1** [T] Box A holds 15 red pens and 21 blue pens." (docs/books/word_problems_g1_g2_original_draft.md)
- REVIEW L5-lostnumber [12-23]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-fourside [12-25]: rule B: 3 of the same numbers ['110', '360', '70'] as "The turtle walks along one side, then turns 70 degrees from straight on. The ins ..." (practice/holiday/p6/07/dist/data/p6l07.json)
- REVIEW L5-flourbags [12-28]: story words 4 of 5 like "(Give your answer in kilograms) ANSWER: 0.4 kg - [WA2_2025_HenryPark Q9, 3m, Mass decimals ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L5-ladybirdgrid [12-30]: rule S3: the sentence "The grid is 5 squares wide and 4 squares tall." is like "Old: A grid is 3 squares wide and 1 square tall." (docs/audit/gifted_fixes_p6.md)
- REVIEW L6-cyclistrun [12-06]: story words 3 of 3 like "Ravi leaves the same house at 9:30 a.m. and cycles along the same road, the same way, at 1 ..." (docs/sasmo/g5_original_problems_draft.md)
- REVIEW L6-jarcoins [12-07]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-jarcoins [12-07]: rule C: two four-word runs shared with "Day 1: 3 coins in the jar. Day 5: 17.', 'The number he adds goes up by 1 each da ..." (levels/gap_items.py): jar on day # / the jar on day
- REVIEW L6-recurrence [12-10]: rule B: 6 of the same numbers ['12', '13', '21', '3', '5', '8'] as "| Number sense: place value, odd/even, digit-card puzzles (split into tens and o ..." (docs/sasmo/g1_analysis.md)
- REVIEW L6-quizmean [12-16]: story words 3 of 5 like "| Prelim | 2024 | Nanyang | P1-8 | 1 | Table of pastries over 3 days; total of two days gi ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L6-tankfraction [12-17]: rule S: sentence "He uses 2/5 of the water in the tank to wash the car." shares 4 content words with "Mrs Tan uses 3 pails of water to wash her car." (docs/books/private_p2_papers/non_routine_questions.md)
- REVIEW L6-twoclasses [12-23]: rule B: 3 of the same numbers ['30', '50', '70'] as "The whole class has 40 pupils. The other cells are empty." style="width:100%;max ..." (practice/holiday/p5/07/dist/data/p5l07.json)
- REVIEW L6-decagon [12-25]: rule S (window): 5 of 6 content words (angle,big,inside,regular,side) in "New: The inside angles of a regular polygon add up to 1800°. A second  ..." (docs/audit/gifted_fixes_p6.md)
- REVIEW L6-gamepay [12-27]: number 8 in the question is not a parameter (written in the wording; check)
- REVIEW L6-gamepay [12-27]: number 12 in the question is not a parameter (written in the wording; check)
