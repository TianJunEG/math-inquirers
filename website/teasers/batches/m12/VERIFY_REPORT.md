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

Sources searched (whole working tree, tracked or not): 3818 files, 69.9 MB, sha256 07be370cdf611f6bf2274ee2.  Files per root: deck 158, diag 12, docs 413, extension 255, hp 35, k2 3, levels 20, mascot 4, ops 4, outputs 27, p1 1, p2 24, p3 24, p4 24, p5 25, p6 35, portal 44, practice 235, print 6, rebuild 87, releases 1, review 1, school 364, split 1801, taster 2, term 40, tutor 130, website 42, worker 1.

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 11. REVIEW items: 94.

- FAIL L1-rulerbill [12-01]: same story as a source: same objects (3 of 4 story words) and 3 same numbers: "Prices $1 to $19. - **Think harder (4).** Three prices: the difference between the dearest and the c ..." (docs/terms/l1_term3_term4_preflight.md) words book,change,ruler
- FAIL L1-twodice [12-05]: same story as a source: rule C (four-word runs, numbers masked): 4 of 7 shared, e.g. "a red die and": "(b) 26. Solution: every whole number from 5 to 30 can be made (move one die at a time), so 30 - 5 +  ..." (docs/sasmo/g4_original_problems_draft.md) words blue,die,red
- FAIL L1-chartwalk [12-09]: same story as a source: same objects (3 of 5 story words) and 3 same numbers: "- **Objective.** Shade the 2s, 5s and 10s on a hundred chart and say what you see; Think harder: a c ..." (docs/terms/l2_preflight.md) words chart,counter,move
- FAIL L2-beanleaves [12-05]: same story as a source: rule C (four-word runs, numbers masked): 3 of 9 shared, e.g. "a bean plant has": "Answer: 25; the gaps are 1, 2, 3, 4, 5, then 6. **3.2** A bean plant has 2 leaves on day 1 and 3 lea ..." (docs/sasmo/g1_original_problems_draft.md) words bean,leave,plant
- FAIL L3-beadbag [12-15]: same story as a source: rule C (four-word runs, numbers masked): 3 of 9 shared, e.g. "green beads are in": "65–80 MIN Challenge    1. Beads repeat in a pattern of 5: red, red, blue, blue, green. How many gree ..." (deck/project/slides/l4-challenge.html) words bead,blue,green,red
- FAIL L5-fourside [12-18]: same story as a source: rule C (four-word runs, numbers masked): 3 of 6 shared, e.g. "a four sided shape": "Pencils down: gather the pairs. Answers: 1) The three corners make a straight line, so the angles of ..." (rebuild/gen_p5l8.py) words shape,sid
- FAIL L5-flourbags [12-26]: same story as a source: rule A (content words): same story skeleton, 4 of 5 story words (3 rare) with other numbers: "What was the mass of the box when it was empty? (Give your answer in kilograms)  ANSWER: 0.4 kg - [W ..." (docs/books/private_p4_papers/non_routine_questions.md) words bag,flour,kilogram,weigh
- FAIL L6-bannerheight [12-02]: same story as a source: same wording with other numbers (9 of 19 word triples): "The square has sides of 6 cm. The triangle has a base of 9 cm. What is the height of the triangle? ..." (p5/Math_Inquirers_P5_Tutor_Guide.html) words base,height
- FAIL L6-quizmean [12-03]: same story as a source: same story (2 of 5 words) and the same numbers ['85', '90']: "The heatmap is a mean of the six scores. - Template (every lesson, slide labels sum to 89 min): chec ..." (docs/audit/journey_p4.md) words mean,score
- FAIL L6-codingclub [12-05]: same story as a source: same story (2 of 4 words) and the same numbers ['28', '40']: "(3) A library table: fiction 84 (boys) and 66 (girls), non-fiction 40 and 30: what percentage of the ..." (docs/terms/l5_preflight.md) words class,pupil
- FAIL L6-tilepattern6 [12-24]: same story as a source: rule C (four-word runs, numbers masked): 3 of 10 shared, e.g. "# tiles and figure": ""problem": "Tiles make a plus sign. Figure 1 has 5 tiles and figure 2 has 9 tiles. Figure 3 has arms ..." (extension/data/l5_u09.json) words figure,tile

- REVIEW L1-storypages [12-02]: story words 3 of 4 like "| VIOLATION | One-step riddle, same type as worksheet Q6a: no extension, and it needs only ..." (docs/audit/gifted_p2.md)
- REVIEW L1-traysame [12-08]: story words 5 of 7 like "## 5. Worst case, pigeonhole and unattainable totals [draft, not yet in the program] (sugg ..." (docs/sasmo/g6_original_problems_draft.md)
- REVIEW L1-chartwalk [12-09]: number 100 in the question is not a parameter (written in the wording; check)
- REVIEW L1-toycars [12-10]: story words 3 of 5 like "- Recurring structure: the pictured price list comes first ("items for sale in a toy shop" ..." (docs/books/p1_school_paper_patterns.md)
- REVIEW L1-fourodds [12-12]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 7 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L1-fourodds [12-12]: rule B: 4 of the same numbers ['3', '5', '7', '9'] as "Is Ali right? Easy first step: use counters to try 3 + 5, 7 + 9 and 11 + 13.", " ..." (practice/holiday/p2/02/dist/data/p2l02.json)
- REVIEW L1-circlekids [12-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-stickertable [12-19]: story words 3 of 5 like "A: 378 **CMP-174** | 2024 | Nanyang | EOY | Q27 | 4 marks | DIV | difficulty 3 | picture n ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L1-whichsun [12-23]: story words 3 of 5 like "How many triangles ca... | VIOLATION | Triangles with 25 sticks: Q4 with another number. | ..." (docs/audit/gifted_p1.md)
- REVIEW L1-oddbig [12-27]: rule B: 3 of the same numbers ['12', '24', '8'] as "Common factors: 12 apples and 18 oranges share the factors 1, 2, 3, 6, so 6 bags ..." (p4/content/l1.js)
- REVIEW L1-robottrack [12-29]: number 8 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bookshelf [12-31]: story words 3 of 4 like "Q: The books in the library were placed on 30 shelves with an equal number of books on eac ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L2-sudoku4 [12-02]: question has 56 words (limit 55)
- REVIEW L2-chocbar [12-06]: rule C: two four-word runs shared with "|---|---|---|---| | C1 | Fill in the box: 1/2 = ?/10 | A chocolate bar has 10 eq ..." (docs/audit/gifted_fixes_p3.md): a chocolate bar has / chocolate bar has #
- REVIEW L2-recyclegrid [12-07]: question has 57 words (limit 55)
- REVIEW L2-recyclegrid [12-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-busroutes [12-12]: longest sentence 26 words (limit 22)
- REVIEW L2-stadiumrows [12-14]: longest sentence 23 words (limit 22)
- REVIEW L2-stadiumrows [12-14]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stadiumrows [12-14]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L2-libraryhalves [12-16]: story words 3 of 3 like "(3) A library table: fiction 84 (boys) and 66 (girls), non-fiction 40 and 30: what percent ..." (docs/terms/l5_preflight.md)
- REVIEW L2-stickgame [12-18]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-bookcase [12-19]: story words 3 of 5 like "a) How many books did Jenny have altogether? Jenny packed all her books equally onto 8 she ..." (docs/books/private_p2_papers/non_routine_questions.md)
- REVIEW L2-foldcut [12-22]: story words 7 of 11 like "fold corner to corner  ✂    two triangles, same size Go further: your choice, any time  Wh ..." (split/l7/project/slides/l7-explore1.html)
- REVIEW L2-tankwater [12-25]: number 28 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-25]: number 41 in the question is not a parameter (written in the wording; check)
- REVIEW L2-tankwater [12-25]: story words 5 of 7 like "- **Go further (3).** G1 **Beyond (named): "Mirror Number".** Find a 4-digit number that b ..." (docs/terms/l4_preflight.md)
- REVIEW L2-gardenfence [12-26]: story words 3 of 4 like "Job 1: put a fence round a garden.'], predict: ['You have 12 squares. ..." (p3/content/l7.js)
- REVIEW L2-cakeshare [12-28]: rule B: 3 of the same numbers ['3', '4', '8'] as "| Workbook core page Q6: Pizza: 1/4 vs 3/8 with a bar hint | compliant |  | | Co ..." (docs/audit/gifted_p2.md)
- REVIEW L2-cubestack [12-31]: longest sentence 26 words (limit 22)
- REVIEW L2-cubestack [12-31]: story words 4 of 6 like "Answer: 36 tiles; Figure 10 (55 tiles). Solution: each new figure adds a new bottom row: 1 ..." (docs/sasmo/g2_original_problems_draft.md)
- REVIEW L3-handshake8 [12-03]: story words 4 of 6 like "Old: 4 friends meet. Every pair shakes hands once. How many handshakes? ..." (docs/audit/gifted_fixes_p6.md)
- REVIEW L3-bigsumcards [12-08]: rule B: 3 of the same numbers ['5', '7', '9'] as "Lesson 1: Million Puzzles SLIDE  Tool: Guess and check  Digit sums and the great ..." (outputs/skill_additions/Math_Inquirers_L5_Skill_Additions_Tutor_Sheet.html)
- REVIEW L3-mapshort [12-09]: longest sentence 31 words (limit 26)
- REVIEW L3-floortiles2 [12-11]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L3-fourtiles [12-12]: story words 4 of 6 like "What is the most squares in a row a net can have?', a: 'With 5 in a row, four squares wrap ..." (p4/content/l8.js)
- REVIEW L3-flagstrip [12-14]: story words 6 of 8 like "When do we first see a red star again? G3. &emsp;Beads repeat in a pattern of 5: red, red, ..." (hp/Math_Inquirers_P1_Question_Bank.html)
- REVIEW L3-smalldigitsum [12-17]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-fishmass [12-18]: story words 3 of 4 like "Ask "Why not grams for the rice?" (the number would be very big; kilograms are the bigger  ..." (rebuild/gen_p2l9.py)
- REVIEW L3-barpieces [12-19]: story words 4 of 6 like "|---|---|---|---| | C1 | Fill in the box: 1/2 = ?/10 | A chocolate bar has 10 equal pieces ..." (docs/audit/gifted_fixes_p3.md)
- REVIEW L3-watertank [12-20]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L3-watertank [12-20]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cryptsum [12-21]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-secondthursday [12-24]: story words 3 of 4 like "b) Wednesday. c) Thursday.", "say": "Write the dates in rows of 7 under the days of the we ..." (p2/qbank_skills.json)
- REVIEW L3-ricejar [12-25]: story words 4 of 6 like "'A jug full of water weighs 1.45 kg. When it is half full, it weighs 0.85 kg. What is the  ..." (practice/holiday/p4/05/lesson.py)
- REVIEW L3-cubetower [12-26]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cubetower [12-26]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cubetower [12-26]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cubetower [12-26]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L4-addpattern [12-01]: story words 3 of 3 like "- "[Name] tested a friend's claim ('is it always true that ...?') with an example, and fou ..." (docs/pedagogy/holiday_review.md)
- REVIEW L4-jellycube [12-03]: number 125 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-07]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-07]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-07]: rule B: 5 of the same numbers ['13', '15', '3', '5', '9'] as "3D: cube, cuboid, cone, cylinder, sphere, count flat faces, rolling, objects cla ..." (docs/books/private_p2_papers/pattern_notes.md)
- REVIEW L4-swaphundreds [12-08]: story words 3 of 4 like "The tutor calls 'swap the hundreds and the tens' or 'swap the tens and the ones'. Show you ..." (docs/audit/audit_p2.md)
- REVIEW L4-concert [12-09]: number 2105 in the question is not a parameter (written in the wording; check)
- REVIEW L4-digitfive [12-12]: rule B: 3 of the same numbers ['3', '4', '5'] as "Fill in the blanks.', { pb: true, before: 0, keepNext: true })); W.push(sub('a', ..." (hp/workbook.js)
- REVIEW L4-gainingclock [12-13]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-13]: number 00 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-13]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-gainingclock [12-13]: number 00 in the question is not a parameter (written in the wording; check)
- REVIEW L4-palyears [12-15]: number 1331 in the question is not a parameter (written in the wording; check)
- REVIEW L4-palyears [12-15]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L4-palyears [12-15]: story words 4 of 6 like "How much does the total change for each swap?”'], hints: ['Hint 1: “Make a table: figure n ..." (p5/content/l9.js)
- REVIEW L4-notebooks [12-17]: story words 3 of 4 like "- Recurring structure: the pictured price list comes first ("items for sale in a toy shop" ..." (docs/books/p1_school_paper_patterns.md)
- REVIEW L4-liftmin [12-18]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-liftmin [12-18]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L4-nametags [12-27]: rule C: two four-word runs shared with "Lesson 6: Rate Racers SLIDE  Tool: Make a table  Totals you cannot make  (L5-PAC ..." (outputs/skill_additions/Math_Inquirers_L5_Skill_Additions_Tutor_Sheet.html): are sold in packs / sold in packs of
- REVIEW L4-visitortable [12-30]: rule C: two four-word runs shared with "On Monday there were 1874 visitors. On Tuesday there were 650 more than on Monda ..." (p3/content/l2.js): how many visitors came / many visitors came on
- REVIEW L5-lostnumber [12-03]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L5-fourthwednesday [12-09]: story words 3 of 4 like ""first": "A month has 31 days. The 1st is a Wednesday. Write the dates of every Wednesday. ..." (term/l1/lessons/l27.json)
- REVIEW L5-stampgive [12-13]: story words 4 of 4 like "The final minute (89-90, slide "end") asks the tutor to hand out certificates and stamped  ..." (docs/audit/timing_p4.md)
- REVIEW L5-penboxes [12-15]: story words 4 of 4 like "Suggested home: Lesson 17 Think harder. **A5.1** [T] Box A holds 15 red pens and 21 blue p ..." (docs/books/word_problems_g1_g2_original_draft.md)
- REVIEW L5-cardsmax5 [12-22]: rule B: 4 of the same numbers ['3', '4', '6', '8'] as "warmQs: [['4 hundreds, 6 tens, 2 ones = ?', '462'], ['What is the 8 worth in 384 ..." (p2/content/l1.js)
- REVIEW L5-rects43 [12-27]: story words 3 of 5 like "Solution: the heights of PAB and PCD from P add up to the height of the parallelogram, so  ..." (docs/sasmo/g6_original_problems_draft.md)
- REVIEW L5-climbing [12-28]: number 358 in the question is not a parameter (written in the wording; check)
- REVIEW L5-sevendigit [12-30]: story words 3 of 3 like "| box only | 6/4/3+1; exit 3 | 34 / 30 | Chunk the Gap (duration by chunks) | none | | 23  ..." (docs/pedagogy/term_review.md)
- REVIEW L6-gaussjar [12-01]: number 10 in the question is not a parameter (written in the wording; check)
- REVIEW L6-gaussjar [12-01]: number 15 in the question is not a parameter (written in the wording; check)
- REVIEW L6-tankdiff [12-12]: story words 4 of 4 like "| EX-DIAG-3 | Go further | 8, 24 | A tank is filled with 4 jugs of water. A jug holds 3 bo ..." (docs/books/p2_non_routine_catalogue.md)
- REVIEW L6-jarcoins [12-13]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L6-jarcoins [12-13]: rule C: two four-word runs shared with "Day 3: 8. Day 4: 12. Day 5: 17.', 'The number he adds goes up by 1 each day.', ' ..." (levels/gap_items.py): jar on day # / the jar on day
- REVIEW L6-testpercent [12-15]: story words 3 of 4 like "A child who scores 0-3 is a child to whom the lessons will be new, which is exactly who th ..." (docs/audit/journey_p6.md)
- REVIEW L6-sixclubs [12-17]: rule C: two four-word runs shared with "Ali does not have the dog. Mei has neither the fish nor the dog. Ravi does not h ..." (docs/terms/l4_preflight.md): neither the fish nor / the fish nor the
- REVIEW L6-cakeshare [12-18]: story words 3 of 4 like "Ben eats 2 pieces. What fraction of the cake does he eat? | compliant |  | | Core 2 (bank) ..." (docs/audit/gifted_p2.md)
- REVIEW L6-foldsix [12-19]: rule C: two four-word runs shared with "], challenge: [ { q: 'A paper strip is folded in half, then in half again, then  ..." (p2/content/l7.js): paper strip is folded / strip is folded in
- REVIEW L6-decagon [12-21]: story words 3 of 4 like "- **Challenge 3 → Challenge 7** (replaced). Old: Each inside angle of a regular polygon is ..." (docs/audit/gifted_fixes_p6.md)
- REVIEW L6-tilepattern6 [12-24]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L6-cubeedges [12-26]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L6-cubeedges [12-26]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L6-cyclistrun [12-28]: story words 3 of 3 like "Ravi leaves the same house at 9:30 a.m. and cycles along the same road, the same way, at 1 ..." (docs/sasmo/g5_original_problems_draft.md)
