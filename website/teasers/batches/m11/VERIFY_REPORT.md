# Teaser batch m11 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 30 | 29 | 2 | 21 | 3 | 30 |
| 2 | 30 | 29 | 2 | 19 | 3 | 30 |
| 3 | 30 | 30 | 1 | 25 | 2 | 30 |
| 4 | 30 | 28 | 2 | 24 | 2 | 30 |
| 5 | 30 | 30 | 1 | 22 | 3 | 30 |
| 6 | 30 | 25 | 3 | 21 | 3 | 30 |

Sources searched (whole working tree, tracked or not): 3818 files, 69.9 MB, sha256 07be370cdf611f6bf2274ee2.  Files per root: deck 158, diag 12, docs 413, extension 255, hp 35, k2 3, levels 20, mascot 4, ops 4, outputs 27, p1 1, p2 24, p3 24, p4 24, p5 25, p6 35, portal 44, practice 235, print 6, rebuild 87, releases 1, review 1, school 364, split 1801, taster 2, term 40, tutor 130, website 42, worker 1.

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 9. REVIEW items: 113.

- FAIL L2-lampring [11-05]: same story as a source: rule A (content words): same story skeleton, 6 of 8 story words (2 rare) with other numbers: "add(id='L2-POST2', level=2, lesson=10, slot='bank', skill='Posts and gaps: round a pond', tool='draw ..." (rebuild/skill_items_l1_3.py) words lamp,path,pond,post,round,stand
- FAIL L2-cardtriple2 [11-14]: same story as a source: same story (2 of 3 words) and the same numbers ['14', '38']: "The heaviest single kits are the fraction wall (12) and the digit cards (10). **The Level 4 home box ..." (docs/terms/l4_preflight.md) words card,set
- FAIL L2-dicetops [11-26]: same story as a source: same objects (3 of 5 story words) and 3 same numbers: "Every cube sits on the table or on another cube.",42,600)}</div>', 'Minutes 80 to 90. Answer: 7 (bot ..." (rebuild/gen_p2l8.py) words bottom,sit,top
- FAIL L3-mirrorclock [11-06]: same story as a source: rule C (four-word runs, numbers masked): 3 of 9 shared, e.g. "a wall clock in": "Solution: 1 + 2 + 3 + 4 = 10; two rows is double. **4.3** Mina looks at a wall clock in a mirror. ..." (docs/sasmo/g1_original_problems_draft.md) words clock,mirror,wall
- FAIL L3-clockturn [11-12]: same story as a source: rule C (four-word runs, numbers masked): 3 of 8 shared, e.g. "hand of a clock": "{ q: 'What is the smaller angle between the hands of a clock at 5 o\'clock? At 8 o\'clock?', a: '150 ..." (p5/content/l8.js) words clock,hand,through
- FAIL L4-calc [11-09]: same story as a source: same objects (3 of 5 story words) and 3 same numbers: "Is about 6 hours per new lesson realistic for your review capacity, or should Terms 3 and 4 be built ..." (docs/terms/level_4_year_plan.md) words follow,order,should
- FAIL L4-clockfive [11-29]: same story as a source: rule C (four-word runs, numbers masked): 4 of 9 shared, e.g. "and the minute hand": "A child may find a different rule; the answer to the question then has to be checked.) ## 9. Clock h ..." (docs/sasmo/g5_original_problems_draft.md) words clock,hand,hour
- FAIL L5-figures [11-01]: same story as a source: rule C (four-word runs, numbers masked): 3 of 9 shared, e.g. "# tiles and figure": ""problem": "Tiles make a plus sign. Figure 1 has 5 tiles and figure 2 has 9 tiles. Figure 3 has arms ..." (extension/data/l5_u09.json) words figure,tile
- FAIL L6-twored [11-25]: same story as a source: rule C (four-word runs, numbers masked): 5 of 13 shared, e.g. "# red # blue": ""q": "A bag has 4 red, 3 blue and 5 green marbles. One marble is picked without looking. ..." (diag/content/p6.json) words bag,blue,green,marble,red,without

- REVIEW L1-bikesigns [11-02]: story words 3 of 5 like "Waves (explained in section 13): A = can be written with the tools as they stand (kit only ..." (docs/terms/l3_preflight.md)
- REVIEW L1-drinksmachine [11-03]: story words 3 of 5 like "| | EX-BACK-2 | Think harder | 5 | Aisha bought 4 notebooks the same price. She paid with  ..." (docs/books/p2_non_routine_catalogue.md)
- REVIEW L1-seatrow [11-04]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-seatrow [11-04]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-seatrow [11-04]: story words 3 of 5 like "3.5 minutes: water and toilet FIRST (about one minute), then the game (about two minutes), ..." (split/p4l6/project/slides/p4l6-break.html)
- REVIEW L1-numpattern [11-06]: question has 54 words (limit 48)
- REVIEW L1-numpattern [11-06]: longest sentence 25 words (limit 20)
- REVIEW L1-bamboo [11-07]: story words 3 of 5 like "- **NY18T2 Q8** | 1 mk | length | LOG | d3 | pic Y - Q: Ali has a ribbon shorter than 30 c ..." (docs/books/private_p2_papers/non_routine_questions.md)
- REVIEW L1-campdays [11-08]: story words 3 of 5 like ""k": "READ", "text": "Your turn. A holiday lasts one week. How many days is that? ..." (term/l1/lessons/l27.json)
- REVIEW L1-siblingsages [11-10]: story words 3 of 5 like "inv={"title":"What stays the same?","intro":"Mei is 13 years old and her brother is 5.", " ..." (docs/audit/mkgifted_p3.py)
- REVIEW L1-mrtdays [11-11]: rule C: two four-word runs shared with "| L10 Q6 (if time) 3-digit odd riddle | none | hint lists the digit sets with no ..." (docs/audit/reaudit_fixes_p3.md): # tuesday # wednesday / monday # tuesday #
- REVIEW L1-queuebus [11-12]: story words 4 of 6 like "________')); W.push(H.sub('b', '20 people are in a queue. Ben is 6th from the front. What  ..." (p4/content/l10.js)
- REVIEW L1-secret63 [11-16]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-counterbox [11-17]: story words 4 of 4 like "How many blue counters must be added so that P(red) = 1/5?', check=lambda: next(x for x in ..." (practice/holiday/p6/06/lesson.py)
- REVIEW L1-busminute [11-18]: story words 4 of 6 like "(2) Say 1 to 12 round a ring (which comes after 12?) on the kit clock. (3) "Half" is two e ..." (docs/terms/l1_term3_term4_preflight.md)
- REVIEW L1-threefifty [11-19]: number 35 in the question is not a parameter (written in the wording; check)
- REVIEW L1-jarsweets [11-20]: story words 3 of 4 like "|---|---|---|---| | EX-EQ-1 | Think harder | A big jar holds twice as many sweets as a sma ..." (docs/books/p4_non_routine_catalogue.md)
- REVIEW L1-trackflags [11-21]: rule C: two four-word runs shared with "**GEO-015** | 2021 | Tao Nan | EY2 | Q6 | 3 marks | AREA | difficulty 3 | pictur ..." (docs/books/private_p3_papers/non_routine_questions.md): school field is # / the school field is
- REVIEW L1-twobags [11-25]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-twobags [11-25]: number 19 in the question is not a parameter (written in the wording; check)
- REVIEW L1-twobags [11-25]: number 19 in the question is not a parameter (written in the wording; check)
- REVIEW L1-twobags [11-25]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bigtwo [11-26]: rule B: 3 of the same numbers ['4', '6', '8'] as "warmQs: [['4 hundreds, 6 tens, 2 ones = ?', '462'], ['What is the 8 worth in 384 ..." (p2/content/l1.js)
- REVIEW L1-stripmarks [11-27]: story words 3 of 5 like "Pairs work with the materials: Paper number strip 0 to 50 (or floor tape), counters, two c ..." (deck/project/slides/l1-explore1.html)
- REVIEW L1-marblecontest [11-29]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L2-clubdays [11-02]: longest sentence 27 words (limit 22)
- REVIEW L2-signsscale [11-08]: story words 3 of 5 like "| L1.2 | Number bonds to 10 and 20, equal sign | SAME G1 (G1 equality) | SAME G1 (K bonds  ..." (docs/audit/intl_mapping_americas_oceania_india.md)
- REVIEW L2-jarcoins [11-09]: story words 3 of 5 like "Q: The graph shows the number of each type of bun sold by ABC Bakery. ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L2-cakeparts [11-11]: story words 4 of 6 like "Draw the cake. What fraction of the WHOLE cake did Ali eat?', a: '1/4 of the whole cake.'  ..." (p5/content/l2.js)
- REVIEW L2-cinemarow [11-12]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L2-cinemarow [11-12]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-fewestswaps [11-13]: rule B: 3 of the same numbers ['3', '4', '5'] as "put('p2l1-ws1',ws_preview('p2l1-ws1','36–50 MIN','Worksheet page 1: with your pa ..." (rebuild/gen_p2l1.py)
- REVIEW L2-ticketnotes [11-16]: story words 4 of 6 like "| | EX-BACK-2 | Think harder | 5 | Aisha bought 4 notebooks the same price. She paid with  ..." (docs/books/p2_non_routine_catalogue.md)
- REVIEW L2-plankcuts [11-17]: story words 3 of 5 like "How many pieces is that? Write it as 1/2 = ?/10. (Draw the bar and cut it in two halves if ..." (docs/audit/gifted_fixes_p3.md)
- REVIEW L2-ticketnumbers [11-28]: number 400 in the question is not a parameter (written in the wording; check)
- REVIEW L3-palin [11-01]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-palin [11-01]: number 232 in the question is not a parameter (written in the wording; check)
- REVIEW L3-palin [11-01]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-mirrorclock [11-06]: number 7 in the question is not a parameter (written in the wording; check)
- REVIEW L3-erasers [11-08]: story words 3 of 5 like "She fills 7 bags and has 4 left over. Dan packs the same cookies 5 to a bag. How many full ..." (docs/sasmo/g1_original_problems_draft.md)
- REVIEW L3-badmintonko [11-10]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-books [11-17]: story words 3 of 5 like "Parent result page text * Replace "Strong? Choose the level that fits the score, not the s ..." (docs/audit/journey_p5.md)
- REVIEW L3-cardsorder [11-18]: number 52 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cardsorder [11-18]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cardsorder [11-18]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cardsorder [11-18]: story words 3 of 4 like "Make the biggest 3-digit number you can. Move the cards around to try.','940','Biggest dig ..." (docs/audit/mkfixpass_p3_gifted.py)
- REVIEW L3-bookread [11-19]: story words 3 of 4 like "of a book on Saturday, 3/8? on Sunday and the remaining pages on Monday. ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L3-robot [11-20]: story words 6 of 9 like "["Start at START. Move up, down, left or right.", f"Step only on multiples of {m}.", "Do n ..." (school/p4/gen/pages_a.py)
- REVIEW L3-twentyfour [11-21]: number 0915 in the question is not a parameter (written in the wording; check)
- REVIEW L3-parrotsrabbits [11-22]: story words 4 of 6 like "Suggested home: Lesson 14 Take away, count up; Lesson 17. **A4.1** [S] A pet shop has 60 a ..." (docs/books/word_problems_g1_g2_original_draft.md)
- REVIEW L3-houses [11-24]: number 21 in the question is not a parameter (written in the wording; check)
- REVIEW L3-houses [11-24]: number 22 in the question is not a parameter (written in the wording; check)
- REVIEW L3-houses [11-24]: number 23 in the question is not a parameter (written in the wording; check)
- REVIEW L3-magic [11-25]: rule C: two four-word runs shared with "# ---------- 21 challenge ---------- ch=[('1.','Put −4, −3, −2, −1, 0, 1, 2, 3,  ..." (rebuild/gen_p6l3.py): every row every column / row every column and
- REVIEW L3-grid33 [11-26]: story words 3 of 3 like "Then fill column by column. A computer check found that this is the only grid that fits th ..." (docs/sasmo/g2_original_problems_draft.md)
- REVIEW L3-bakery [11-28]: rule C: two four-word runs shared with "Solution: 9 x 4 = 36 shells in the jars; 36 + 7 = 43. **B6.3** [T] Mrs Lim has 3 ..." (docs/books/word_problems_g1_g2_original_draft.md): buns on each tray / trays with # buns
- REVIEW L3-ladder [11-29]: story words 4 of 6 like "Plan a program that tests it 1000 times.', fig: FG.grid({ rows: [1, 2, 3, 4, 5, 6, 7, 8],  ..." (p6/content/l10.js)
- REVIEW L3-jugs [11-30]: longest sentence 30 words (limit 26)
- REVIEW L3-jugs [11-30]: rule C: two four-word runs shared with "2   You have a 3 ℓ jug and a 5 ℓ jug. You can fill a jug from the tap, empty a j ..." (p2/workbook_body.html): pour from one jug / tap empty a jug
- REVIEW L4-theatrerows [11-01]: number 18 in the question is not a parameter (written in the wording; check)
- REVIEW L4-theatrerows [11-01]: number 21 in the question is not a parameter (written in the wording; check)
- REVIEW L4-attendance [11-03]: story words 3 of 5 like "| L2 S7 | Smallest and largest difference of two rounded crowds (Challenge level) | A conc ..." (docs/audit/reaudit_fixes_p4.md)
- REVIEW L4-roundprices [11-07]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L4-rects33 [11-08]: story words 3 of 4 like "Then fill column by column. A computer check found that this is the only grid that fits th ..." (docs/sasmo/g2_original_problems_draft.md)
- REVIEW L4-flour [11-13]: rule B: 3 of the same numbers ['3', '4', '5'] as "| 33 (11 gaps x 3) | | Prelim | 2026 | ACSJ | P1-23 | 2 | Ratio recipe, most who ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L4-pencilshare [11-15]: story words 3 of 5 like "- [EOY_2025_NanHua Q14, 2m, Factors and multiples, diff 2] Mr Tan has some pencils. The nu ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L4-motherage [11-16]: story words 3 of 3 like "In how many years' time will their total age add up to 18? ANSWER: 4 - [SA1_2021_ACSJ Q44, ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L4-milkjugs [11-17]: story words 4 of 5 like "| EX-DIAG-3 | Go further | 8, 24 | A tank is filled with 4 jugs of water. A jug holds 3 bo ..." (docs/books/p2_non_routine_catalogue.md)
- REVIEW L4-eggtrays30 [11-18]: story words 3 of 5 like "The better buy also depends on how many you really need (if Mei needs only 3 pens, the 3-p ..." (rebuild/gen_p5l6.py)
- REVIEW L4-books [11-20]: story words 4 of 4 like "- **Start here (6).** Compare two price tags ("Circle the cheaper one"); "How much more do ..." (docs/terms/l1_term3_term4_preflight.md)
- REVIEW L4-smallest5 [11-23]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L5-town [11-02]: story words 3 of 4 like ""1": ["Reading, comparing and rounding numbers up to 10 million, and riddles about large n ..." (p5/parent_side.json)
- REVIEW L5-orangeprofit [11-06]: story words 3 of 5 like ""link_to_lesson": "Fibonacci wrote about prices, profit and changing money, just like the  ..." (docs/stories/p2.json)
- REVIEW L5-stairs60 [11-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-stairs60 [11-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-pct35 [11-09]: story words 3 of 4 like "f"There are {T6} pupils. {FR(e1)} of them walk to school. ..." (school/p4/gen/pages_b.py)
- REVIEW L5-bracketmult [11-10]: story words 3 of 5 like "### Term 1: Number, calculation and everyday tools (all new; follows the holiday course wi ..." (docs/terms/level_3_year_plan.md)
- REVIEW L5-fishtank [11-12]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-fishtank [11-12]: story words 5 of 8 like "Ask "Why not grams for the rice?" (the number would be very big; kilograms are the bigger  ..." (rebuild/gen_p2l9.py)
- REVIEW L5-palin5 [11-15]: number 48384 in the question is not a parameter (written in the wording; check)
- REVIEW L5-palin5 [11-15]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubes [11-16]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubes [11-16]: story words 3 of 4 like "Puzzle      Listen for       Puzzle 1 (access): A box is 4 cubes long, 3 cubes wide and 2  ..." (p5/Math_Inquirers_P5_Tutor_Guide.html)
- REVIEW L5-frogsteps [11-18]: story words 3 of 4 like "One step of the taught add-3 rule (same as worksheet Q4/Q5 and Stretch 3). | | Challenge 9 ..." (docs/audit/gifted_p2.md)
- REVIEW L5-fieldwidth [11-19]: story words 3 of 3 like "- [EOY_2025_NanHua Q15, 2m, Area (path), diff 2] A field was built on a rectangular plot o ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L5-ropes [11-21]: story words 4 of 6 like "It is cut into 3 pieces. The first and second pieces are each 66 cm long. What is the leng ..." (docs/books/private_p2_papers/non_routine_questions.md)
- REVIEW L5-ricecost [11-22]: story words 3 of 4 like "Solution: 3 hats cost 3 x 6 = $18, which is the price of 2 scarves; 18 / 2 = $9. **B9.3**  ..." (docs/books/word_problems_g1_g2_original_draft.md)
- REVIEW L5-queue5 [11-23]: story words 3 of 5 like "Draw a bar for each person. a) Ali is 4 years older than his sister. Their ages add up to  ..." (outputs/skill_additions/Math_Inquirers_L2_Skill_Additions_Tutor_Sheet.html)
- REVIEW L5-tank [11-24]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L5-tank [11-24]: number 1000 in the question is not a parameter (written in the wording; check)
- REVIEW L5-threesports [11-25]: rule C: two four-word runs shared with "## 10. Overlapping groups, combined percent and averages [draft, not yet in the  ..." (docs/sasmo/g5_original_problems_draft.md): # play football # / play football # play
- REVIEW L5-cubetower9 [11-27]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubetower9 [11-27]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubetower9 [11-27]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cubetower9 [11-27]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-bottleshare [11-28]: story words 3 of 5 like "`Ben ate 1/3 of a pizza ...` is workbook Think Harder Q2 and `4 litres of juice ... 6 bott ..." (docs/audit/audit_p5.md)
- REVIEW L5-cube4 [11-30]: number 64 in the question is not a parameter (written in the wording; check)
- REVIEW L5-cube4 [11-30]: story words 5 of 6 like "**4.1** A 5 by 5 by 2 block of cheese is made of 50 small cubes. Its whole outside, includ ..." (docs/sasmo/g6_original_problems_draft.md)
- REVIEW L6-hiddencubes [11-09]: number 216 in the question is not a parameter (written in the wording; check)
- REVIEW L6-lockcode [11-11]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L6-freezer [11-12]: number 14 in the question is not a parameter (written in the wording; check)
- REVIEW L6-sixfactors [11-15]: rule B: 3 of the same numbers ['3', '4', '6'] as "| 4 | Sharing 24 stickers (what if) | Whole-number unit fractions of 24: 1/2,1/3 ..." (docs/audit/close_gaps_p4.md)
- REVIEW L6-waterbarrel [11-17]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-primes100 [11-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-primes100 [11-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-phoneplan [11-21]: rule C: two four-word runs shared with "to 2.50 p.m.? $9.50 (4 h 35 min: first hour, then 3 h 35 min is 8 half hours or  ..." (p5/Math_Inquirers_P5_Tutor_Guide.html): # a month plus / a month plus #
- REVIEW L6-upthendown [11-24]: rule C: two four-word runs shared with "It goes down by 1. ..." (hp/Math_Inquirers_P1_Tutor_Guide.html): goes down by # / it goes down by
- REVIEW L6-redblue [11-26]: rule C: two four-word runs shared with "Explain. - **Challenge 1 → Challenge 7** (replaced). Old: A bag has red and blue ..." (docs/audit/gifted_fixes_p6.md): and blue counters in / blue counters in the
- REVIEW L6-program [11-28]: story words 3 of 4 like "Counting carefully [draft, not yet in the program] (suggested for L10, or beside L8) **5.1 ..." (docs/sasmo/g3_original_problems_draft.md)
- REVIEW L6-bin45 [11-29]: number 6 in the question is not a parameter (written in the wording; check)
- REVIEW L6-bin45 [11-29]: number 0 in the question is not a parameter (written in the wording; check)
- REVIEW L6-bin45 [11-29]: number 10 in the question is not a parameter (written in the wording; check)
- REVIEW L6-juicecups [11-30]: story words 4 of 5 like "(c) 4 pizzas are 32 slices, and 32 − 27 = 5.')) S.append(item(U+'-S11', 'start', 3, 'A jug ..." (extension/l4/src/u04.py)
