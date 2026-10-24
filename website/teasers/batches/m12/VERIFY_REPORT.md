# Teaser batch m12 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 31 | 31 | 1 | 21 | 3 | 31 |
| 2 | 31 | 31 | 1 | 27 | 3 | 31 |
| 3 | 31 | 29 | 2 | 26 | 3 | 31 |
| 4 | 31 | 31 | 1 | 29 | 2 | 31 |
| 5 | 31 | 29 | 2 | 26 | 2 | 31 |
| 6 | 31 | 30 | 2 | 24 | 2 | 31 |

Sources searched (whole working tree, tracked or not): 6664 files, 1357.7 MB, sha256 4133d40de45df2e44201d848.  Files per root: deck 158, diag 12, docs 416, extension 257, hp 41, k2 5, levels 20, mascot 4, ops 14, outputs 180, p1 1, p2 27, p3 27, p4 27, p5 28, p6 38, portal 45, practice 289, print 6, rebuild 87, releases 1, review 1, school 474, split 1801, taster 2, term 2530, tutor 130, website 42, worker 1.

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 1. REVIEW items: 105.

- FAIL L1-twodice [12-05]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['3', '4', '5', '6', '7', '10'] with the shared story words: "Two dice: 36 equally likely outcomes blue die red die 1 1 2 2 3 3 4 4 5 5 6 6 2 3 4 5 6 7 3 4 5 6 7  ..." (split/p6l6/project/slides/p6l6-teachtwo.html) words blue,happen,red

- REVIEW L1-rulerbill [12-01]: rule B: 3 of the same numbers ['3', '4', '9'] as "Picture-dependent items re-solved from the picture, not the key: B1 L1 S1 (26),  ..." (term/l1/audit/AUDIT_BOOKS_1_4_ROUND2.md)
- REVIEW L1-twodice [12-05]: question has 54 words (limit 48)
- REVIEW L1-twodice [12-05]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-traysame [12-08]: story words 5 of 7 like "Pupils colour their own copy. Colour key: 1260 = yellow, 1680 = red, 2520 = blue, 3360 = g ..." (school/p4/out/S1_key.html)
- REVIEW L1-chartwalk [12-09]: number 100 in the question is not a parameter (written in the wording; check)
- REVIEW L1-toycars [12-10]: rule B: 3 of the same numbers ['3', '8', '9'] as "7 Student-led inquiry: 2 - Explore round 3 is a free build; the Investigation as ..." (term/l1/AUDIT_L32.md)
- REVIEW L1-fourodds [12-12]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 7 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: rule B: 4 of the same numbers ['3', '5', '7', '9'] as "Easy first step: use counters to try 3 + 5, 7 + 9 and 11 + 13.", "marking_mode": ..." (practice/holiday/p2/02/dist/data/p2l02.json)
- REVIEW L1-circlekids [12-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-circlekids [12-18]: story words 5 of 8 like "Posts and gaps: round a pond (L2-POST2) 8 lamps stand round a pond, the same distance apar ..." (outputs/skill_additions/Math_Inquirers_L2_Skill_Additions_Tutor_Sheet.pdf)
- REVIEW L1-eggtrays [12-22]: story words 3 of 5 like "| Prelim | 2023 | TaoNan | P2-11 | 4 | Hawkers A and B buy same number of trays; big 30? a ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L1-streetwalk [12-24]: rule B: 3 of the same numbers ['3', '5', '6'] as "The turtle walks along one side, then turns 70 degrees from straight on. The ins ..." (practice/holiday/p6/07/dist/data/p6l07.json)
- REVIEW L1-oddbig [12-27]: rule B: 3 of the same numbers ['12', '24', '8'] as "Why is the odd one so much bigger?', a: '24 (1, 2, 3, 4, 6, 8, 12, 24) and 105 ( ..." (p6/content/l2.js)
- REVIEW L1-robottrack [12-29]: number 8 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bookshelf [12-31]: story words 3 of 4 like "Q: The books in the library were placed on 30 shelves with an equal number of books on eac ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L2-sudoku4 [12-02]: question has 75 words (limit 55)
- REVIEW L2-chocbar [12-06]: rule C: two four-word runs shared with "| C1 | Fill in the box: 1/2 = ?/10 | A chocolate bar has 10 equal pieces. ..." (docs/audit/gifted_fixes_p3.md): a chocolate bar has / chocolate bar has #
- REVIEW L2-recyclegrid [12-07]: question has 57 words (limit 55)
- REVIEW L2-recyclegrid [12-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stripchain [12-08]: story words 5 of 8 like "- [SA2_2020_Nanyang P2-17, 5m, Black white squares pattern, diff 3, pic] Black 1,5,13...;  ..." (docs/books/private_p5_papers/non_routine_questions.md)
- REVIEW L2-hallfloor [12-10]: question has 56 words (limit 55)
- REVIEW L2-hallfloor [12-10]: longest sentence 28 words (limit 22)
- REVIEW L2-seesaw [12-11]: story words 5 of 8 like "l2_scale level balance scales: scales [{left: [obj, ...], right: [obj, ...], label?}], obj ..." (extension/tools/figs_l2_u09.py)
- REVIEW L2-busroutes [12-12]: longest sentence 26 words (limit 22)
- REVIEW L2-tinstack [12-14]: longest sentence 33 words (limit 22)
- REVIEW L2-stickgame [12-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-sevens [12-23]: rule B: 3 of the same numbers ['12', '4', '8'] as "He reads for half an hour. What time does he stop?", "hint": "The long hand goes ..." (term/l1/out/l23/practice/data/t3l23.json)
- REVIEW L2-tankwater [12-25]: number 35 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-25]: number 39 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-25]: story words 4 of 6 like "How many points did each team score? Tank A has 80 litres of water and loses 6 litres ever ..." (outputs/designed/Math_Inquirers_P4_Question_Bank.pdf)
- REVIEW L2-gardenfence [12-26]: story words 3 of 4 like "Start with the shortest width, 1 m, and list in order.", "steps": ["Half of 18 m is 9 m, s ..." (practice/holiday/p3/07/dist/data/p3l07.json)
- REVIEW L2-cakeshare [12-28]: rule B: 3 of the same numbers ['3', '4', '8'] as "What fraction of the cake do they eat altogether?", "hint": "The slices are all  ..." (practice/holiday/p2/07/dist/data/p2l07.json)
- REVIEW L2-sortrule2 [12-30]: rule B: 4 of the same numbers ['19', '21', '25', '52'] as "eq(T['S5']['val'], sorted([52, 25, 41, 14], key=tens_ones), 'S5') eq(T['S6']['va ..." (term/l1/verify/l03_checks.py)
- REVIEW L3-buttonjar [12-01]: story words 4 of 5 like "Then 10 more red cubes are put in." Holiday `l3.js` line 144: "A jar has 12 red beads and  ..." (extension/l5/AUDIT_ROUND2.md)
- REVIEW L3-floortiles2 [12-03]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L3-handshake8 [12-04]: story words 5 of 7 like "Friend 2 has already shaken hands with friend 1: how many new handshakes does friend 2 mak ..." (practice/holiday/p6/05/dist/data/p6l05.json)
- REVIEW L3-booksales [12-07]: longest sentence 31 words (limit 26)
- REVIEW L3-mapshort [12-08]: longest sentence 31 words (limit 26)
- REVIEW L3-moneybox [12-10]: longest sentence 28 words (limit 26)
- REVIEW L3-moneybox [12-10]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-moneybox [12-10]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cryptsum [12-11]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-ricejar [12-14]: story words 4 of 6 like "When it is half full, it weighs 0.85 kg. What is the mass of the empty jug, in kilograms?' ..." (practice/holiday/p4/05/lesson.py)
- REVIEW L3-smalldigitsum [12-15]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-watertank [12-19]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L3-watertank [12-19]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-watertank [12-19]: rule B: 3 of the same numbers ['12', '3', '9'] as "The 9 ℓ let out is 9000 cm³, so 18 000 cm³ is left.", "One cm of depth over the  ..." (practice/holiday/p5/05/dist/data/p5l05.json)
- REVIEW L3-fishmass [12-20]: story words 3 of 4 like "P = code_items_page(25, 8125, "Kilograms and Grams", 1, "Mass: reading scales in kilograms ..." (school/p2/gen/pages_w4.py)
- REVIEW L3-barpieces [12-23]: story words 4 of 6 like "| Challenge 1: A chocolate bar has 10 equal pieces. Ali eats 1/10 of it. ..." (docs/audit/gifted_p2.md)
- REVIEW L3-clubs [12-24]: story words 3 of 4 like "f"From {cats[ri[0]]} to {cats[ri[1]]}, the number went up by how many?", f"How many pupils ..." (school/p4/gen/pages_d.py)
- REVIEW L3-fruitsums [12-26]: story words 3 of 5 like "if d1 == d2: continue # the first two clues must add different amounts, or Apple and Banan ..." (school/p1/gen/pages_measure.py)
- REVIEW L3-raffledays [12-29]: rule C: two four-word runs shared with "Q: A total of 380 movie tickets were sold in two days. 90 fewer tickets were sol ..." (docs/books/private_p3_papers/non_routine_questions.md): many tickets were sold / tickets were sold on
- REVIEW L3-lanes5 [12-30]: story words 3 of 4 like "How many seats were there in the school hall? - [EOY_2024_Raffles Q36, 2m, Seats rows/colu ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L3-cardcorners [12-31]: rule B: 3 of the same numbers ['3', '4', '9'] as "How wide and how high is that rectangle?", "label": "4(a) box", "svg": "<svg vie ..." (practice/holiday/p4/07/dist/data/p4l07.json)
- REVIEW L4-gainingclock [12-01]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-01]: number 00 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-01]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-01]: number 00 in the question is not a parameter (written in the wording; check)
- REVIEW L4-threedigitsum [12-02]: rule B: 3 of the same numbers ['3', '5', '8'] as "(a) value of $2 vouchers (b) least cash | (a) $210 | | WA1 | 2025 | ACSJ | B2-18 ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L4-liftmin [12-04]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-liftmin [12-04]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L4-notebooks [12-08]: rule C: two four-word runs shared with "**A12.1** [T] 2 pens cost $8. How much do 5 pens cost? ..." (docs/books/word_problems_g1_g2_original_draft.md): # pens cost # / do # pens cost
- REVIEW L4-digitfive [12-09]: rule B: 3 of the same numbers ['3', '4', '5'] as "Fill in the blanks.", "Counting in 2s: 2, 4, 6, ____, ____, 12, ____, 16"], "q": ..." (practice/holiday/p1/01/dist/data/p1l01.json)
- REVIEW L4-nametags [12-12]: rule C: two four-word runs shared with "G2 **CTX.** Cans are sold in packs of 6 for $5.40 and 8 for $6.80. ..." (docs/terms/l4_preflight.md): are sold in packs / sold in packs of
- REVIEW L4-heightline [12-18]: question has 76 words (limit 75)
- REVIEW L4-addpattern [12-20]: rule B: 3 of the same numbers ['3', '4', '9'] as "Is she always right?"], "q": "Investigation 2. Mei says: "In a pattern that repe ..." (practice/holiday/p1/04/dist/data/p1l04.json)
- REVIEW L4-visitortable [12-21]: story words 3 of 4 like "ANSWER: 120 l - [EOY_2025_MahaBodhi P2-8, 3m, Line graph and money, diff 2, pic] Visitors  ..." (docs/books/private_p5_papers/non_routine_questions.md)
- REVIEW L4-sundaes [12-24]: rule B: 3 of the same numbers ['3', '4', '5'] as "**Gaps and posts on a line are set in every term.** "10 trees at equal distances ..." (docs/books/p3_school_paper_patterns.md)
- REVIEW L4-tilefigures [12-26]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-26]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-26]: rule B: 5 of the same numbers ['13', '15', '3', '5', '9'] as "35); growing-figure patterns and two-number operator rules are NOT IN (SASMO 19- ..." (docs/terms/l3_preflight.md)
- REVIEW L4-reachtotal [12-29]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-climbing [12-02]: number 358 in the question is not a parameter (written in the wording; check)
- REVIEW L5-redeye [12-08]: story words 3 of 4 like "| 31 | Factors, Multiples and Tests | Every number is a rectangle in waiting, and its digi ..." (docs/pedagogy/term_review.md)
- REVIEW L5-zoogates [12-12]: longest sentence 35 words (limit 34)
- REVIEW L5-zoogates [12-12]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-zoogates [12-12]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L5-zoogates [12-12]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-zoogates [12-12]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L5-zoogates [12-12]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L5-zoogates [12-12]: number 6 in the question is not a parameter (written in the wording; check)
- REVIEW L5-zoogates [12-12]: rule B: 4 of the same numbers ['3', '4', '5', '6'] as "P4-30 item 5 "Two 10 cm by 3 cm rectangles are joined along their long sides." ( ..." (docs/audit_final/p4_semester_booklets_audit.md)
- REVIEW L5-roundtable [12-15]: story words 5 of 7 like "- **Go further.** Six children sit round a table; clues give next to, opposite; place ever ..." (docs/terms/l1_term2_preflight.md)
- REVIEW L5-routeplan [12-20]: longest sentence 37 words (limit 34)
- REVIEW L5-lostnumber [12-23]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-fourside [12-25]: rule B: 3 of the same numbers ['110', '360', '70'] as "The turtle walks along one side, then turns 70 degrees from straight on. The ins ..." (practice/holiday/p6/07/dist/data/p6l07.json)
- REVIEW L5-flourbags [12-28]: story words 4 of 5 like "(Give your answer in kilograms) ANSWER: 0.4 kg - [WA2_2025_HenryPark Q9, 3m, Mass decimals ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L6-sixclubs [12-02]: rule C: two four-word runs shared with "Which pet is left for Ali?", "steps": ["Clue 1: Ali has no cat and no dog.", "Th ..." (practice/holiday/p1/08/dist/data/p1l08.json): a different pet cat / different pet cat dog
- REVIEW L6-cyclistrun [12-06]: story words 3 of 3 like "Ravi leaves the same house at 9:30 a.m. and cycles along the same road, the same way, at 1 ..." (docs/sasmo/g5_original_problems_draft.md)
- REVIEW L6-jarcoins [12-07]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-jarcoins [12-07]: rule C: two four-word runs shared with "Day 1: 3 coins in the jar. Day 5: 17.', 'The number he adds goes up by 1 each da ..." (levels/gap_items.py): jar on day # / the jar on day
- REVIEW L6-hiddenpair [12-09]: rule B: 3 of the same numbers ['4', '6', '7'] as "Fill in the blanks.", "Counting in 2s: 2, 4, 6, ____, ____, 12, ____, 16"], "q": ..." (practice/holiday/p1/01/dist/data/p1l01.json)
- REVIEW L6-recurrence [12-10]: rule B: 6 of the same numbers ['12', '13', '21', '3', '5', '8'] as "| Number sense: place value, odd/even, digit-card puzzles (split into tens and o ..." (docs/sasmo/g1_analysis.md)
- REVIEW L6-codingclub [12-14]: rule B: 3 of the same numbers ['28', '4', '40'] as "| T4 | Mean and outlier (31); fair or unfair, random trials (33); counting basic ..." (docs/terms/level_6_year_plan.md)
- REVIEW L6-bunboxes [12-15]: story words 5 of 7 like ""text": "A baker packs 43 buns into boxes of 6. She fills {b} boxes and has {b} buns left  ..." (extension/data/l3_u05.json)
- REVIEW L6-quizmean [12-16]: story words 3 of 5 like "| Prelim | 2024 | Nanyang | P1-8 | 1 | Table of pastries over 3 days; total of two days gi ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L6-cakeshare [12-17]: story words 3 of 4 like "Ali eats half of what is left. Draw the cake. What fraction of the WHOLE cake did Ali eat? ..." (outputs/designed/Math_Inquirers_P5_Question_Bank.pdf)
- REVIEW L6-twoclasses [12-23]: rule B: 3 of the same numbers ['30', '50', '70'] as "The whole class has 40 pupils. The other cells are empty." style="width:100%;max ..." (practice/holiday/p5/07/dist/data/p5l07.json)
- REVIEW L6-gaussjar [12-27]: number 10 in the question is not a parameter (written in the wording; check)
- REVIEW L6-gaussjar [12-27]: number 15 in the question is not a parameter (written in the wording; check)
- REVIEW L6-tankdepth [12-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-tankdepth [12-28]: number 1000 in the question is not a parameter (written in the wording; check)
