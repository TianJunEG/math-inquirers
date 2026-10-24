# Teaser batch m12 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 31 | 31 | 1 | 20 | 3 | 31 |
| 2 | 31 | 31 | 1 | 27 | 3 | 31 |
| 3 | 31 | 29 | 2 | 25 | 3 | 31 |
| 4 | 31 | 30 | 2 | 29 | 2 | 31 |
| 5 | 31 | 29 | 2 | 26 | 2 | 31 |
| 6 | 31 | 30 | 2 | 25 | 2 | 31 |

Sources searched (whole working tree, tracked or not): 6604 files, 1353.9 MB, sha256 e57711cddecc6031fa00b778.  Files per root: deck 158, diag 12, docs 416, extension 257, hp 41, k2 5, levels 20, mascot 4, ops 14, outputs 174, p1 1, p2 27, p3 27, p4 27, p5 28, p6 38, portal 45, practice 235, print 6, rebuild 87, releases 1, review 1, school 474, split 1801, taster 2, term 2530, tutor 130, website 42, worker 1.

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 24. REVIEW items: 98.

- FAIL L1-twodice [12-05]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['3', '4', '5', '6', '8'] with the shared story words: "1 6 yellow 3 8 red 5 8 blue 7 10 green 5 12 orange 3 8 + 2 8 = 5 8 (blue) 7 8 − 2 8 = 5 8 (blue) 3 1 ..." (school/colour_by_code/out/p2/html/CBC-P2-15_house_frac_teacher.html) words green,yellow
- FAIL L1-swimbike [12-11]: sub-structure sorting.overlap_both is not allowed at level 1 (levels [2, 3, 4, 5, 6])
- FAIL L2-cubestack [12-31]: sub-structure stacks.layers_of_cubes is not allowed at level 2 (levels [])
- FAIL L3-fourtiles [12-12]: sub-structure polyominoes.count_shapes is not allowed at level 3 (levels [])
- FAIL L3-fourtiles [12-12]: retired frame tetromino: how many different shapes from squares joined edge to edge (P4 question bank and workbook state the answer)
- FAIL L3-flagstrip [12-14]: sub-structure repeating_pattern.cycle is not allowed at level 3 (levels [1, 2, 4])
- FAIL L3-flagstrip [12-14]: rule L (listed sequence): "red, red, blue, green" with the number 30 in "Beads go red, red, blue, green, red, red, blue, green … Mei says the 30th bead is blue. ..." (outputs/designed/Math_Inquirers_P2_Question_Bank.pdf)
- FAIL L3-pencildrawing [12-16]: sub-structure networks.draw_without_lifting is not allowed at level 3 (levels [])
- FAIL L3-mealset [12-23]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['3', '4', '24'] with the shared story words: "(c) 4 choices, then 3, then 2: 4 {X} 3 {X} 2 = 24.', parts=[P('a', 'A menu has 3 starters, 5 mains a ..." (extension/l6/src/u10.py) words drink,main
- FAIL L3-cubetower [12-26]: sub-structure stacks.layers_of_cubes is not allowed at level 3 (levels [])
- FAIL L4-jellycube [12-03]: sub-structure cubes.painted is not allowed at level 4 (levels [])
- FAIL L4-concert [12-09]: same story as a source: rule B (numbers): 5 of the same numbers ['15', '24', '40', '45', '6'] (2 distinctive) and 4 shared story words: "ev = d['workbook']['kits'][0]['events'] # each event card carries a time; its am or pm comes from th ..." (term/l1/verify/l22_checks.py) words break,come,hour,school
- FAIL L4-floorstrip [12-14]: sub-structure counting_ways.stairs_steps is not allowed at level 4 (levels [])
- FAIL L4-palyears [12-15]: sub-structure digit_puzzles.palindromes is not allowed at level 4 (levels [])
- FAIL L4-fanten [12-25]: sub-structure counting_grid.triangles_in_fan is not allowed at level 4 (levels [])
- FAIL L4-fanten [12-25]: retired frame fan_triangles: triangles in a fan of lines from one corner (practice P5 and the P1 workbook Go further use it)
- FAIL L4-chesssquares [12-29]: sub-structure counting_grid.squares_in_grid is not allowed at level 4 (levels [])
- FAIL L4-chesssquares [12-29]: retired frame count_in_grid: count every square or rectangle in a grid (tutor notes, split l7 / p2l8, extension L3 workbook)
- FAIL L5-diagline [12-08]: sub-structure counting_grid.diagonal_squares is not allowed at level 5 (levels [])
- FAIL L5-rects43 [12-27]: sub-structure counting_grid.rectangles_in_grid is not allowed at level 5 (levels [])
- FAIL L5-rects43 [12-27]: retired frame count_in_grid: count every square or rectangle in a grid (tutor notes, split l7 / p2l8, extension L3 workbook)
- FAIL L6-tankdiff [12-12]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['3', '36', '54'] with the shared story words: "Work backwards from 16 litres: what was there an hour earlier?', steps=['Each hour 1/3 is let out, s ..." (practice/holiday/p5/02/lesson.py) words litre,tank,water
- FAIL L6-machine3 [12-14]: sub-structure backwards.undo_steps is not allowed at level 6 (levels [3, 4, 5])
- FAIL L6-cubeedges [12-26]: sub-structure networks.draw_without_lifting is not allowed at level 6 (levels [])

- REVIEW L1-rulerbill [12-01]: rule B: 3 of the same numbers ['3', '4', '9'] as "Picture-dependent items re-solved from the picture, not the key: B1 L1 S1 (26),  ..." (term/l1/audit/AUDIT_BOOKS_1_4_ROUND2.md)
- REVIEW L1-traysame [12-08]: story words 5 of 7 like "Pupils colour their own copy. Colour key: 1260 = yellow, 1680 = red, 2520 = blue, 3360 = g ..." (school/p4/out/S1_key.html)
- REVIEW L1-chartwalk [12-09]: number 100 in the question is not a parameter (written in the wording; check)
- REVIEW L1-toycars [12-10]: rule B: 3 of the same numbers ['3', '8', '9'] as "7 Student-led inquiry: 2 - Explore round 3 is a free build; the Investigation as ..." (term/l1/AUDIT_L32.md)
- REVIEW L1-fourodds [12-12]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 7 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: rule B: 4 of the same numbers ['3', '5', '7', '9'] as "Easy first step: use counters to try 3 + 5, 7 + 9 and 11 + 13.", "marking_mode": ..." (practice/holiday/p2/02/dist/data/p2l02.json)
- REVIEW L1-circlekids [12-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-circlekids [12-18]: story words 3 of 5 like ""text": "Opposite S: {b}", "explanation": "In the row of 3 squares P, Q, R, the 2 ends P a ..." (extension/data/l4_u08.json)
- REVIEW L1-eggtrays [12-22]: story words 3 of 5 like "| Prelim | 2023 | TaoNan | P2-11 | 4 | Hawkers A and B buy same number of trays; big 30? a ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L1-whichsun [12-23]: story words 3 of 5 like "| Row 1: star, sun, moon. ..." (docs/books/p1_non_routine_catalogue.md)
- REVIEW L1-streetwalk [12-24]: rule B: 3 of the same numbers ['3', '5', '6'] as "For each way, how many bicycles are there? Type them in order, starting with the ..." (practice/holiday/p2/03/dist/data/p2l03.json)
- REVIEW L1-oddbig [12-27]: rule B: 3 of the same numbers ['12', '24', '8'] as "Why is the odd one so much bigger?', a: '24 (1, 2, 3, 4, 6, 8, 12, 24) and 105 ( ..." (p6/content/l2.js)
- REVIEW L1-robottrack [12-29]: number 8 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bookshelf [12-31]: story words 3 of 4 like "Q: The books in the library were placed on 30 shelves with an equal number of books on eac ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L2-sudoku4 [12-02]: question has 56 words (limit 55)
- REVIEW L2-chocbar [12-06]: rule C: two four-word runs shared with "| C1 | Fill in the box: 1/2 = ?/10 | A chocolate bar has 10 equal pieces. ..." (docs/audit/gifted_fixes_p3.md): a chocolate bar has / chocolate bar has #
- REVIEW L2-recyclegrid [12-07]: question has 57 words (limit 55)
- REVIEW L2-recyclegrid [12-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stripchain [12-08]: story words 5 of 8 like "- [SA2_2020_Nanyang P2-17, 5m, Black white squares pattern, diff 3, pic] Black 1,5,13...;  ..." (docs/books/private_p5_papers/non_routine_questions.md)
- REVIEW L2-seesaw [12-11]: story words 5 of 8 like "l2_scale level balance scales: scales [{left: [obj, ...], right: [obj, ...], label?}], obj ..." (extension/tools/figs_l2_u09.py)
- REVIEW L2-busroutes [12-12]: longest sentence 26 words (limit 22)
- REVIEW L2-stadiumrows [12-14]: longest sentence 23 words (limit 22)
- REVIEW L2-stadiumrows [12-14]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stadiumrows [12-14]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stadiumrows [12-14]: rule B: 3 of the same numbers ['3', '4', '7'] as "(6) A story: a school prints 2 500 sheets a day; how many in 40 days (100 000, V ..." (docs/terms/l5_preflight.md)
- REVIEW L2-stickgame [12-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-25]: number 35 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-25]: number 39 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-25]: story words 4 of 6 like "How many points did each team score? Tank A has 80 litres of water and loses 6 litres ever ..." (outputs/designed/Math_Inquirers_P4_Question_Bank.pdf)
- REVIEW L2-gardenfence [12-26]: story words 3 of 4 like "# ---------- teach before page 2: border ---------- fr=grid(0,0,12,9,c)+RC(c,c,c,0,0,9,7,' ..." (rebuild/gen_p4l7.py)
- REVIEW L2-cakeshare [12-28]: rule B: 3 of the same numbers ['3', '4', '8'] as "| Workbook core page Q5: Cake in 8 slices: together, left, who eats more | compl ..." (docs/audit/gifted_p2.md)
- REVIEW L2-sortrule2 [12-30]: rule B: 4 of the same numbers ['19', '21', '25', '52'] as "eq(T['S5']['val'], sorted([52, 25, 41, 14], key=tens_ones), 'S5') eq(T['S6']['va ..." (term/l1/verify/l03_checks.py)
- REVIEW L2-cubestack [12-31]: longest sentence 26 words (limit 22)
- REVIEW L2-cubestack [12-31]: rule C: two four-word runs shared with "The next layer is 2 rows of 2. The top layer is 1 cube.', ..." (rebuild/skill_items_l1_3.py): the top layer is / top layer is #
- REVIEW L3-cardcorners [12-02]: rule B: 3 of the same numbers ['3', '4', '9'] as "The top bar is cut into 9 equal parts with 4 shaded. The bottom bar is cut into  ..." (practice/holiday/p4/04/dist/data/p4l04.json)
- REVIEW L3-handshake8 [12-03]: story words 5 of 7 like "Handshakes: 5 friends, every pair shakes once. A shakes 4 new hands, B 3 new, C 2, D 1, E  ..." (p6/Math_Inquirers_P6_Tutor_Guide.html)
- REVIEW L3-clubs [12-04]: rule B: 3 of the same numbers ['3', '38', '40'] as "| Nets at one line weight; new word | pyramid C, triangular prism A, 2x2 block s ..." (docs/audit_final/p4_semester_booklets_audit_round2.md)
- REVIEW L3-lanes5 [12-07]: story words 3 of 4 like "How many seats were there in the school hall? - [EOY_2024_Raffles Q36, 2m, Seats rows/colu ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L3-mapshort [12-09]: longest sentence 31 words (limit 26)
- REVIEW L3-floortiles2 [12-11]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L3-buttonjar [12-15]: story words 4 of 5 like "Then 10 more red cubes are put in." Holiday `l3.js` line 144: "A jar has 12 red beads and  ..." (extension/l5/AUDIT_ROUND2.md)
- REVIEW L3-smalldigitsum [12-17]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-fishmass [12-18]: story words 3 of 4 like "P = code_items_page(25, 8125, "Kilograms and Grams", 1, "Mass: reading scales in kilograms ..." (school/p2/gen/pages_w4.py)
- REVIEW L3-barpieces [12-19]: story words 4 of 6 like "| Challenge 1: A chocolate bar has 10 equal pieces. Ali eats 1/10 of it. ..." (docs/audit/gifted_p2.md)
- REVIEW L3-watertank [12-20]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L3-watertank [12-20]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-watertank [12-20]: rule B: 3 of the same numbers ['12', '3', '9'] as "The 9 ℓ let out is 9000 cm³, so 18 000 cm³ is left.", "One cm of depth over the  ..." (practice/holiday/p5/05/dist/data/p5l05.json)
- REVIEW L3-cryptsum [12-21]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-ricejar [12-25]: story words 4 of 6 like "When it is half full, it weighs 0.85 kg. What is the mass of the empty jug, in kilograms?' ..." (practice/holiday/p4/05/lesson.py)
- REVIEW L3-cubetower [12-26]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cubetower [12-26]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cubetower [12-26]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cubetower [12-26]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cubetower [12-26]: rule C: two four-word runs shared with "The bottom layer is 3 rows of 3. The next layer is 2 rows of 2. The top layer is ..." (outputs/skill_additions/Math_Inquirers_L2_Skill_Additions_Tutor_Sheet.html): the top layer is / top layer is #
- REVIEW L4-addpattern [12-01]: rule B: 3 of the same numbers ['3', '4', '7'] as "| 4 | 12th bead; sticks for 4 squares | Is it always true? place 30 matches plac ..." (docs/audit/close_gaps_p1.md)
- REVIEW L4-jellycube [12-03]: number 125 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-07]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-07]: rule B: 5 of the same numbers ['13', '15', '3', '5', '9'] as "35); growing-figure patterns and two-number operator rules are NOT IN (SASMO 19- ..." (docs/terms/l3_preflight.md)
- REVIEW L4-concert [12-09]: number 2105 in the question is not a parameter (written in the wording; check)
- REVIEW L4-digitfive [12-12]: rule B: 3 of the same numbers ['3', '4', '5'] as "Start here (6 questions, modelled at 17 minutes of the 30) is fill in a strip of ..." (term/l1/AUDIT_L18.md)
- REVIEW L4-gainingclock [12-13]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-13]: number 00 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-13]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-13]: number 00 in the question is not a parameter (written in the wording; check)
- REVIEW L4-palyears [12-15]: number 1331 in the question is not a parameter (written in the wording; check)
- REVIEW L4-palyears [12-15]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L4-notebooks [12-17]: rule C: two four-word runs shared with "**B7.1** [T] 4 notebooks cost $20. How much do 7 notebooks cost? ..." (docs/books/word_problems_g1_g2_original_draft.md): # notebooks cost # / do # notebooks cost
- REVIEW L4-liftmin [12-18]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-liftmin [12-18]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L4-sundaes [12-21]: rule B: 3 of the same numbers ['3', '4', '5'] as "**Gaps and posts on a line are set in every term.** "10 trees at equal distances ..." (docs/books/p3_school_paper_patterns.md)
- REVIEW L4-cubenet [12-26]: story words 5 of 8 like "today: 'Find out which shapes fold into a cube, find opposite faces on a dice net, and com ..." (p4/content/l8.js)
- REVIEW L4-nametags [12-27]: rule C: two four-word runs shared with "G2 **CTX.** Cans are sold in packs of 6 for $5.40 and 8 for $6.80. ..." (docs/terms/l4_preflight.md): are sold in packs / sold in packs of
- REVIEW L4-visitortable [12-30]: story words 3 of 4 like "ANSWER: 120 l - [EOY_2025_MahaBodhi P2-8, 3m, Line graph and money, diff 2, pic] Visitors  ..." (docs/books/private_p5_papers/non_routine_questions.md)
- REVIEW L5-lostnumber [12-03]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-diagline [12-08]: story words 6 of 10 like "return _svg('A rectangle 6 squares wide and 4 squares tall on squared paper with a diagona ..." (rebuild/p5_gaps.py)
- REVIEW L5-fourside [12-18]: rule B: 3 of the same numbers ['110', '360', '70'] as "body += ostep(128, 260, 2, 'The turn is the angle between straight on and the ne ..." (rebuild/gen_p6l7.py)
- REVIEW L5-redeye [12-20]: story words 3 of 4 like "| 31 | Factors, Multiples and Tests | Every number is a rectangle in waiting, and its digi ..." (docs/pedagogy/term_review.md)
- REVIEW L5-flourbags [12-26]: story words 4 of 5 like "(Give your answer in kilograms) ANSWER: 0.4 kg - [WA2_2025_HenryPark Q9, 3m, Mass decimals ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L5-climbing [12-28]: number 358 in the question is not a parameter (written in the wording; check)
- REVIEW L5-roundtable [12-31]: story words 5 of 7 like "- **Go further.** Six children sit round a table; clues give next to, opposite; place ever ..." (docs/terms/l1_term2_preflight.md)
- REVIEW L6-gaussjar [12-01]: number 10 in the question is not a parameter (written in the wording; check)
- REVIEW L6-gaussjar [12-01]: number 15 in the question is not a parameter (written in the wording; check)
- REVIEW L6-quizmean [12-03]: story words 3 of 5 like "| Prelim | 2024 | Nanyang | P1-8 | 1 | Table of pastries over 3 days; total of two days gi ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L6-codingclub [12-05]: rule B: 3 of the same numbers ['28', '4', '40'] as "| T4 | Mean and outlier (31); fair or unfair, random trials (33); counting basic ..." (docs/terms/level_6_year_plan.md)
- REVIEW L6-sevencards [12-08]: rule B: 4 of the same numbers ['12', '22', '24', '8'] as "| Bar model, difference, unit price | L4 strong: part-whole, comparison, times a ..." (docs/sasmo/g3_analysis.md)
- REVIEW L6-twoclasses [12-10]: rule B: 3 of the same numbers ['20', '30', '80'] as "Extra idea for anyone who wants it Make a list of 5 whole numbers with mean 10,  ..." (p6/Math_Inquirers_P6_Tutor_Guide.pdf)
- REVIEW L6-jarcoins [12-13]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-jarcoins [12-13]: rule C: two four-word runs shared with "Day 1: 3 coins in the jar. Day 5: 17.', 'The number he adds goes up by 1 each da ..." (levels/gap_items.py): jar on day # / the jar on day
- REVIEW L6-recurrence [12-16]: rule B: 6 of the same numbers ['12', '13', '21', '3', '5', '8'] as "| Number sense: place value, odd/even, digit-card puzzles (split into tens and o ..." (docs/sasmo/g1_analysis.md)
- REVIEW L6-sixclubs [12-17]: rule C: two four-word runs shared with ""q": "Ali, Mei, Siti and Ben each have a different pet: cat, dog, fish or rabbit ..." (diag/content/p2.json): a different pet cat / different pet cat dog
- REVIEW L6-cakeshare [12-18]: story words 3 of 4 like "Ali eats half of what is left. Draw the cake. What fraction of the WHOLE cake did Ali eat? ..." (outputs/designed/Math_Inquirers_P5_Question_Bank.pdf)
- REVIEW L6-cubeedges [12-26]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L6-cubeedges [12-26]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L6-cyclistrun [12-28]: story words 3 of 3 like "Ravi leaves the same house at 9:30 a.m. and cycles along the same road, the same way, at 1 ..." (docs/sasmo/g5_original_problems_draft.md)
