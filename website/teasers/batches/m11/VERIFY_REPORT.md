# Teaser batch m11 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 30 | 29 | 2 | 21 | 3 | 30 |
| 2 | 30 | 29 | 2 | 20 | 3 | 30 |
| 3 | 30 | 30 | 1 | 26 | 2 | 30 |
| 4 | 30 | 28 | 2 | 24 | 2 | 30 |
| 5 | 30 | 30 | 1 | 21 | 3 | 30 |
| 6 | 30 | 25 | 3 | 21 | 3 | 30 |

Sources searched (whole working tree, tracked or not): 6604 files, 1353.9 MB, sha256 f5d485ff197171466d84f60e.  Files per root: deck 158, diag 12, docs 416, extension 257, hp 41, k2 5, levels 20, mascot 4, ops 14, outputs 174, p1 1, p2 27, p3 27, p4 27, p5 28, p6 38, portal 45, practice 235, print 6, rebuild 87, releases 1, review 1, school 474, split 1801, taster 2, term 2530, tutor 130, website 42, worker 1.

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 23. REVIEW items: 105.

- FAIL L1-marblegame [11-26]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['3', '4', '5', '24'] with the shared story words: "steps=['Each player wins on 3 differences, but the differences are not equally likely: 0 has 6 outco ..." (practice/holiday/p6/06/lesson.py) words game,win
- FAIL L2-lunchsets [11-03]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['3', '4', '24'] with the shared story words: "(Check: 4 × 3 × 5 = 60.)'], src=['A set lunch is 1 main, 1 drink and 1 dessert.']), dict(id='T2a', t ..." (practice/holiday/p6/05/lesson.py) words drink,lunch,main,set
- FAIL L2-machine3 [11-22]: sub-structure backwards.undo_steps is not allowed at level 2 (levels [3, 4, 5])
- FAIL L2-fivecoins [11-24]: sub-structure coins.amounts_made is not allowed at level 2 (levels [])
- FAIL L3-palin [11-01]: sub-structure digit_puzzles.palindromes is not allowed at level 3 (levels [])
- FAIL L3-mrtsteps [11-07]: sub-structure counting_ways.stairs_steps is not allowed at level 3 (levels [])
- FAIL L3-magic [11-25]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['3', '4', '5', '6', '7', '8', '9'] with the shared story words: "* Drawn diagrams on the sneak-peek (check) slides, which the re-audit says were missing in L1, L3, L ..." (docs/audit/reaudit_fixes_p5.md) words already,diagonal,empty,grid
- FAIL L3-grid33 [11-26]: sub-structure counting_grid.squares_in_grid is not allowed at level 3 (levels [])
- FAIL L3-grid33 [11-26]: retired frame count_in_grid: count every square or rectangle in a grid (tutor notes, split l7 / p2l8, extension L3 workbook)
- FAIL L3-ladder [11-29]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['4', '5', '10', '22'] with the shared story words: "4, 7, 10, 13, 16, 19, 22: 7 squares.') put('p2l4-teachgrow',sec('p2l4-teachgrow','54–55 MIN',body,'T ..." (rebuild/gen_p2l4.py) words lolly,stick
- FAIL L4-roundprices [11-07]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['50', '100', '400', '500'] with the shared story words: ""explanation": "36 482 is between 36 000 and 37 000, and it is before the halfway mark 36 500, so it ..." (extension/data/l4_u02.json) words halfway,nearest,round
- FAIL L4-rects33 [11-08]: sub-structure counting_grid.rectangles_in_grid is not allowed at level 4 (levels [])
- FAIL L4-rects33 [11-08]: retired frame count_in_grid: count every square or rectangle in a grid (tutor notes, split l7 / p2l8, extension L3 workbook)
- FAIL L4-calc [11-09]: sub-structure order_ops.evaluate is not allowed at level 4 (levels [5, 6])
- FAIL L5-palin5 [11-15]: sub-structure digit_puzzles.palindromes is not allowed at level 5 (levels [])
- FAIL L5-frogsteps [11-18]: sub-structure counting_ways.stairs_steps is not allowed at level 5 (levels [])
- FAIL L5-threeclubs [11-25]: sub-structure sorting.three_sets is not allowed at level 5 (levels [])
- FAIL L5-cubetower9 [11-27]: sub-structure stacks.layers_of_cubes is not allowed at level 5 (levels [])
- FAIL L5-cube4 [11-30]: sub-structure cubes.painted is not allowed at level 5 (levels [])
- FAIL L5-cube4 [11-30]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['4', '24', '64'] with the shared story words: "D(id='5t2', tier='core', no='5 table: 2 faces', label='5 2-face', type='fields', skill='painted cube ..." (practice/holiday/p5/05/lesson.py) words outside,paint
- FAIL L6-tiles13 [11-06]: sub-structure counting_ways.stairs_steps is not allowed at level 6 (levels [])
- FAIL L6-hiddencubes [11-09]: sub-structure cubes.painted is not allowed at level 6 (levels [])
- FAIL L6-juicecups [11-30]: same story as a source: same objects (3 of 4 story words) and 3 same numbers: "| 11 | H5 stretch 4, challenge 1, 8 | Medium | painting the whole outside of a 3 x 4 x 5 cuboid, 96  ..." (docs/terms/l5_preflight.md) words litre,paint,pour

- REVIEW L1-racerun [11-02]: story words 3 of 5 like "| Schema valid (JSON Schema + key checks) | PASS | all top-level keys, schema 2020-12, ide ..." (term/l1/AUDIT_L11.md)
- REVIEW L1-secret63 [11-04]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-noodleset [11-05]: story words 4 of 6 like "She ordered 1 side dish, 1 main dish and 1 drink for lunch. What did she eat? [menu: Frenc ..." (docs/books/private_p2_papers/non_routine_questions.md)
- REVIEW L1-siblingsages [11-06]: rule B: 3 of the same numbers ['30', '5', '9'] as "In how many years will their ages add up to 30? Type the number of years.", "mar ..." (practice/holiday/p3/04/dist/data/p3l04.json)
- REVIEW L1-numpattern [11-07]: rule B: 4 of the same numbers ['11', '4', '6', '9'] as "What time does she sit down?", "hint": "Go back half an hour from 7 o'clock.", " ..." (term/l1/out/l23/practice/data/t3l23.json)
- REVIEW L1-tilewall [11-10]: longest sentence 23 words (limit 20)
- REVIEW L1-threefifty [11-14]: number 35 in the question is not a parameter (written in the wording; check)
- REVIEW L1-stripmarks [11-17]: story words 3 of 5 like "**DIAG-019** | 2020 | Catholic High | SA2 | Q38 | 3 marks | LEN | difficulty 3 | picture y ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L1-busminute [11-18]: rule B: 3 of the same numbers ['20', '35', '4'] as "| 14 | 5 Machines; 6 Market Day; 7 Fair Shares | Before-and-after bars; three ch ..." (docs/terms/l2_preflight.md)
- REVIEW L1-marblecontest [11-19]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-counterbox [11-21]: story words 3 of 4 like "- Why non-routine: 6 apples and 4 pears shared equally into 2 baskets ..." (docs/books/private_p1_papers/non_routine_questions.md)
- REVIEW L1-seatrow [11-23]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-seatrow [11-23]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-seatrow [11-23]: rule B: 3 of the same numbers ['3', '4', '5'] as "- [WA_2020_TA1_StNicholas Q15, 2m, Cinema seats rows behind in front, diff 3] 5  ..." (docs/books/private_p5_papers/non_routine_questions.md)
- REVIEW L1-woodpecker [11-24]: rule B: 3 of the same numbers ['4', '7', '9'] as "| L5 No.5 route grid | 24 | OK; 20 and 8 re-solved; puddle P hatched, text says  ..." (docs/audit_final/holiday_diagram_review_L4_6.md)
- REVIEW L1-marblegame [11-26]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-marblegame [11-26]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-marblegame [11-26]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-twobags [11-27]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-twobags [11-27]: number 19 in the question is not a parameter (written in the wording; check)
- REVIEW L1-twobags [11-27]: number 19 in the question is not a parameter (written in the wording; check)
- REVIEW L1-twobags [11-27]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-openingtimes [11-28]: rule B: 3 of the same numbers ['11', '4', '6'] as "| 4 | Pattern Machines | Far places in a repeating pattern come from the groups  ..." (docs/pedagogy/holiday_review.md)
- REVIEW L1-drinksmachine [11-29]: story words 3 of 5 like "**LIST-051** | 2025 | Raffles Girls | EOY | Q8 | 2 marks | MONEY | difficulty 3 | picture  ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L2-clubdays [11-02]: longest sentence 27 words (limit 22)
- REVIEW L2-tilebed [11-07]: story words 3 of 4 like "Solution: the left die's far face is 1, so its touching face is 6; the next die's touching ..." (docs/sasmo/g5_original_problems_draft.md)
- REVIEW L2-signsscale [11-08]: rule B: 3 of the same numbers ['20', '4', '9'] as "| 17 to 18 | Ruler; the graph grids are in the book | - | | | 18 to 19 | Up to 1 ..." (docs/terms/l5_preflight.md)
- REVIEW L2-cakeparts [11-11]: rule C: two four-word runs shared with "How many glasses can be filled? M 2 S 1 18 Z 1 2 2 8 9 of the garden is split in ..." (school/p6/out/S1_pupil.html): of the whole garden / the whole garden is
- REVIEW L2-cinemarow [11-12]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L2-cinemarow [11-12]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-fewestswaps [11-13]: story words 3 of 5 like "| 35 Timetable Puzzles (new, from old 20) | Try both orders, timetable plus 7-day cycle (T ..." (docs/terms/level_3_year_plan.md)
- REVIEW L2-cardtriple2 [11-14]: rule B: 3 of the same numbers ['14', '31', '38'] as "Lessons 20 to 40 are being rebuilt anyway (and the strategy card and common look ..." (docs/pedagogy/lesson_x10_consolidation_plan.md)
- REVIEW L2-ticketnotes [11-16]: rule B: 3 of the same numbers ['3', '30', '5'] as "The maths is right everywhere: counting mixed coins and notes, swapping a coin f ..." (term/l1/audit/WORKBOOK_AUDIT_L24.md)
- REVIEW L2-ticketnumbers [11-28]: number 400 in the question is not a parameter (written in the wording; check)
- REVIEW L2-ticketnumbers [11-28]: story words 3 of 5 like "21:('Letters and Brackets',[('EXP','T','stamps at n cents paid with $5: change in terms of ..." (docs/books/private_p6_papers/build_plan_section.py)
- REVIEW L3-palin [11-01]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-palin [11-01]: number 232 in the question is not a parameter (written in the wording; check)
- REVIEW L3-palin [11-01]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-badmintonko [11-10]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-books [11-17]: rule B: 3 of the same numbers ['20', '24', '31'] as "Singapore public holidays (Google "Holidays in Singapore" calendar, 1 Nov-31 Dec ..." (docs/audit_final/schedule_and_calendar.md)
- REVIEW L3-cardsorder [11-18]: number 52 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cardsorder [11-18]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cardsorder [11-18]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cardsorder [11-18]: rule B: 3 of the same numbers ['35', '5', '7'] as "Which answer is the biggest, and which is the smallest?", "try_it_answer": "7 x  ..." (docs/stories/final_p2.json)
- REVIEW L3-twentyfour [11-21]: number 0915 in the question is not a parameter (written in the wording; check)
- REVIEW L3-twentyfour [11-21]: rule B: 3 of the same numbers ['24', '35', '8'] as "- L8: Q2 hint (a dent corner is bigger than a right angle) and shape A done for  ..." (docs/audit/fixpass_p3.md)
- REVIEW L3-parrotsrabbits [11-22]: story words 4 of 6 like "**A4.1** [S] A pet shop has 60 animals. 24 are fish, 17 are birds and the rest are rabbits ..." (docs/books/word_problems_g1_g2_original_draft.md)
- REVIEW L3-houses [11-24]: number 21 in the question is not a parameter (written in the wording; check)
- REVIEW L3-houses [11-24]: number 22 in the question is not a parameter (written in the wording; check)
- REVIEW L3-houses [11-24]: number 23 in the question is not a parameter (written in the wording; check)
- REVIEW L4-theatrerows [11-01]: number 18 in the question is not a parameter (written in the wording; check)
- REVIEW L4-theatrerows [11-01]: number 21 in the question is not a parameter (written in the wording; check)
- REVIEW L4-attendance [11-03]: story words 3 of 5 like "{ q: 'The crowd at a concert was 38 000 when rounded to the nearest thousand. ..." (p4/content/l2.js)
- REVIEW L4-ferry [11-05]: rule B: 3 of the same numbers ['13', '7', '9'] as "Notes on the tag: 1.3, 1.7 (reading and writing numbers in numerals and in words ..." (school/p1/out/P1_S1_Answer_Key.pdf)
- REVIEW L4-roundprices [11-07]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L4-calc [11-09]: story words 4 of 6 like "Counting the boxes shows a line that takes a shortcut. S1-05 (P5-05) Colour the Rocket 1 s ..." (school/p5/out/P5_S1_Answer_Key.pdf)
- REVIEW L4-flour [11-13]: rule B: 3 of the same numbers ['3', '4', '5'] as "| 33 (11 gaps x 3) | | Prelim | 2026 | ACSJ | P1-23 | 2 | Ratio recipe, most who ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L4-pencilshare [11-15]: rule B: 3 of the same numbers ['12', '5', '8'] as "Answer: 4, 3, 4 8 sweets among 2 friends is 4 each. 12 sweets among 4 friends is ..." (outputs/print/term/Math_Inquirers_L1_T2_Book4_Lessons06-10_AnswerKey_TUTOR_PRINT.pdf)
- REVIEW L4-milkjugs [11-17]: story words 3 of 5 like "- **P5-08 item 5** "7 litres of juice are poured equally into 8 jugs. How much juice is in ..." (docs/audit_final/p5_semester_booklets_audit.md)
- REVIEW L4-eggtrays30 [11-18]: story words 3 of 5 like "- **P5-27** (bus, tailor, pens, farmer, cleaner, Ali): the frame "N things in a minutes, h ..." (docs/audit_final/p5_semester_booklets_audit_round2.md)
- REVIEW L4-sunflower [11-19]: rule B: 3 of the same numbers ['15', '4', '7'] as "| L9 S2 (printed) | Scale of 20, 3 lines above 40 | Scale starts at 100, lines w ..." (docs/audit/reaudit_fixes_p4.md)
- REVIEW L4-piechart [11-21]: story words 5 of 7 like "| Prelim | 2026 | Raffles | P2-2 | 2 | Pie chart: true, false or not possible to tell | 3  ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L4-smallest5 [11-23]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L5-town [11-02]: story words 3 of 4 like "- [EOY_2021_AiTong P1-10, 1m, Road map facing south-east, diff 3, pic] Car along Road S he ..." (docs/books/private_p5_papers/non_routine_questions.md)
- REVIEW L5-stairs60 [11-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-stairs60 [11-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-bracketmult [11-10]: story words 4 of 6 like "Counting the boxes shows a line that takes a shortcut. S1-05 (P5-05) Colour the Rocket 1 s ..." (school/p5/out/P5_S1_Answer_Key.pdf)
- REVIEW L5-moneyleft [11-11]: rule B: 3 of the same numbers ['3', '50', '8'] as "**Same type, new numbers (round 1 accepted; listed so the owner can decide):** U ..." (extension/l2/AUDIT_ROUND2.md)
- REVIEW L5-fishtank [11-12]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-fishtank [11-12]: story words 5 of 8 like "(2) Using the height of the tank instead of the depth of the water, or giving the new leve ..." (tutor/data/p5l5.notes.json)
- REVIEW L5-palin5 [11-15]: number 48384 in the question is not a parameter (written in the wording; check)
- REVIEW L5-palin5 [11-15]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubes [11-16]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubes [11-16]: story words 3 of 4 like "s+=f'<text x="{P(2,0,0)[0]:.0f}" y="{P(2,0,0)[1]+22:.0f}" font-size="22" font-weight="700" ..." (rebuild/p5_gaps.py)
- REVIEW L5-savingsinterest [11-17]: story words 5 of 7 like "(6) A story with a bank. - **Think harder (4).** (1) $2 000 at 3% a year for 4 years earns ..." (docs/terms/l5_preflight.md)
- REVIEW L5-fieldwidth [11-19]: story words 3 of 3 like "- [EOY_2025_NanHua Q15, 2m, Area (path), diff 2] A field was built on a rectangular plot o ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L5-ropes [11-21]: story words 4 of 6 like "What number am I? - [WA2_2025_Nanyang Q8, 2m, Rope fractions chain, diff 3] Jim had 3 piec ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L5-ricecost [11-22]: rule C: two four-word runs shared with "Go further: Three Painters. - **Prerequisites.** Primary 4 multiplication and di ..." (docs/terms/l5_preflight.md): kg of rice cost / of rice cost #
- REVIEW L5-queue5 [11-23]: story words 3 of 5 like "| Level 2 (ages 7-9) is the next most complete. Older levels read and write more on paper  ..." (docs/product/face_to_face_pilot_plan.md)
- REVIEW L5-tank [11-24]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-tank [11-24]: number 1000 in the question is not a parameter (written in the wording; check)
- REVIEW L5-tank [11-24]: story words 7 of 11 like ""Six tank stories that need litres changed to cm³ or back: the depth of water, the litres  ..." (school/p6/gen/pages_d.py)
- REVIEW L5-threeclubs [11-25]: rule B: 3 of the same numbers ['22', '3', '60'] as "Private sources (`docs/books/private_*`, `docs/sasmo/private_*`): 20 files, 22 2 ..." (docs/audit_final/p3_semester_booklets_audit.md)
- REVIEW L5-cubetower9 [11-27]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubetower9 [11-27]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubetower9 [11-27]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubetower9 [11-27]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubetower9 [11-27]: rule C: two four-word runs shared with "The bottom layer is 3 rows of 3. The next layer is 2 rows of 2. The top layer is ..." (outputs/skill_additions/Math_Inquirers_L2_Skill_Additions_Tutor_Sheet.html): the top layer is / top layer is #
- REVIEW L5-bottleshare [11-28]: story words 4 of 5 like "Stand tall if it holds more than 1 ℓ. Crouch if it holds less.','Five minutes. Call: a tea ..." (rebuild/gen_p5l5.py)
- REVIEW L5-cornerscard [11-29]: rule B: 5 of the same numbers ['15', '4', '5', '6', '8'] as "| Where | Old | New | Tier change | | Bank Core C1 to C6 | formula items (12 and ..." (docs/audit/gifted_fixes_p5.md)
- REVIEW L5-cube4 [11-30]: number 64 in the question is not a parameter (written in the wording; check)
- REVIEW L6-hiddencubes [11-09]: number 216 in the question is not a parameter (written in the wording; check)
- REVIEW L6-lockcode [11-11]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L6-freezer [11-12]: number 14 in the question is not a parameter (written in the wording; check)
- REVIEW L6-diagonals [11-13]: story words 3 of 4 like "cxo = sum(a for a, b in op[:8]) / 8; cyo = sum(b for a, b in op[:8]) / 8 labs = ''.join(T( ..." (rebuild/gen_p6l7.py)
- REVIEW L6-sixfactors [11-15]: rule B: 3 of the same numbers ['3', '4', '6'] as "In units of 10°, you need three whole numbers that add up to 9.", "steps": ["In  ..." (practice/holiday/p4/06/dist/data/p4l06.json)
- REVIEW L6-waterbarrel [11-17]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-primes100 [11-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-primes100 [11-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-reverse [11-20]: rule C: two four-word runs shared with "(if time) Letter puzzle: AB + AB + AB = CAB. Each letter stands for a digit. ..." (outputs/print/Math_Inquirers_P3_Workbook_PRINT.pdf): each letter stands for / letter stands for a
- REVIEW L6-phoneplan [11-21]: rule C: two four-word runs shared with "Phone plan A costs $15 a month plus 10¢ a minute. ..." (outputs/designed/Math_Inquirers_P5_Question_Bank.pdf): # a month plus / a month plus #
- REVIEW L6-redblue [11-26]: rule C: two four-word runs shared with "['A bag has red and blue counters in the ratio 3 : 5. ..." (levels/gap_items.py): and blue counters in / blue counters in the
- REVIEW L6-bin45 [11-29]: number 6 in the question is not a parameter (written in the wording; check)
- REVIEW L6-bin45 [11-29]: number 0 in the question is not a parameter (written in the wording; check)
- REVIEW L6-bin45 [11-29]: number 10 in the question is not a parameter (written in the wording; check)
