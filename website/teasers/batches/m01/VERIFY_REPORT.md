# Teaser batch m01 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 31 | 30 | 2 | 21 | 3 | 31 |
| 2 | 31 | 31 | 1 | 26 | 2 | 31 |

Sources searched (whole working tree, tracked or not): 6759 files, 1363.2 MB, sha256 f4b95a8afe23b53915a07bdb.  Files per root: deck 158, diag 12, docs 422, extension 257, hp 41, k2 5, levels 23, mascot 4, ops 14, outputs 180, p1 1, p2 27, p3 27, p4 27, p5 28, p6 38, portal 45, practice 373, print 6, rebuild 87, releases 1, review 1, school 474, split 1801, taster 2, term 2532, tutor 130, website 42, worker 1.

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 15. REVIEW items: 46.

- FAIL L1-partyclinks [01-02]: shares a 7-word run with external: "once with every other child how many"
- FAIL L1-partyclinks [01-02]: shares a 7-word run with term: "once with every other child how many"
- FAIL L1-tartrows [01-08]: same story as a source: rule N (the question's numbers and the answer all in one source window): ['3', '5', '12'] with the shared story words: "| Prelim | 2023 | TaoNan | P2-11 | 4 | Hawkers A and B buy same number of trays; big 30? and small 1 ..." (docs/books/private_p6_papers/non_routine_questions.md) words egg,tray
- FAIL L1-applegraph [01-13]: forbidden word in q: picture
- FAIL L1-applegraph [01-13]: forbidden word in hint: picture
- FAIL L1-applegraph [01-13]: forbidden word in why: picture
- FAIL L1-photoline [01-24]: forbidden word in q: photo
- FAIL L1-hatscarf [01-30]: shares a 7-word run with external: "how many different outfits can she make"
- FAIL L1-hatscarf [01-30]: shares a 7-word run with term: "hat and one scarf how many different"
- FAIL L1-hatscarf [01-30]: same story as a source: rule A (content words): same story skeleton, 4 of 5 story words (2 rare) with other numbers: "How much do the rulers cost altogether?", "answer": "3*p", "hint": "Add {p} three times.", "steps":  ..." (term/l1/out/l36/practice/data/t4l36.json) words hat,outfit,scarf,scarve
- FAIL L2-smudgesum [01-16]: arithmetic in q is wrong: 6 + 428 = 744.
- FAIL L2-kitedrum [01-23]: forbidden word in q: picture
- FAIL L2-shoegraph [01-26]: forbidden word in q: picture
- FAIL L2-shoegraph [01-26]: forbidden word in hint: picture
- FAIL L2-shoegraph [01-26]: forbidden word in why: picture

- REVIEW L1-tagtiles [01-01]: rule B: 3 of the same numbers ['6', '7', '9'] as "| Challenge (bank X1-X9) | 9 | **X3** "Ravi: 24 m of fence, largest area": list  ..." (docs/audit/gifted_p4.md)
- REVIEW L1-grapeplates [01-07]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L1-grapeplates [01-07]: number 22 in the question is not a parameter (written in the wording; check)
- REVIEW L1-grapeplates [01-07]: number 22 in the question is not a parameter (written in the wording; check)
- REVIEW L1-grapeplates [01-07]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bikelock [01-10]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bikelock [01-10]: story words 3 of 4 like "body = h2('Worked example: a bike lock') + card(p('A lock has 3 dials. Each dial shows 1,  ..." (rebuild/gen_p6l5.py)
- REVIEW L1-busdepart [01-12]: story words 3 of 5 like "- [EOY_2024_NanChiau Q34, 2m, Timetable, diff 2] Bus schedule table: leaves Singapore 06 5 ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L1-applegraph [01-13]: rule C: two four-word runs shared with "| Core 2 (bank): In a picture graph, each ★ stands for 2 children. ..." (docs/audit/gifted_p2.md): a picture graph each / in a picture graph
- REVIEW L1-applegraph [01-13]: rule S3: the sentence "In a picture graph, each apple picture stands for 10 apples." is like "In a picture graph, each picture stands for 2 children." (outputs/designed/Math_Inquirers_P2_Question_Bank.pdf)
- REVIEW L1-pagefives [01-14]: number 52 in the question is not a parameter (written in the wording; check)
- REVIEW L1-pagefives [01-14]: rule B: 3 of the same numbers ['15', '5', '52'] as "A brace under the bar asks for the minutes in all." style="width:100%;max-width: ..." (practice/holiday/p5/06/dist/data/p5l06.json)
- REVIEW L1-busplates [01-15]: rule S: sentence "The table shows how many sticks each digit needs." shares 4 content words with ""q": "Explain: A table shows 1 triangle needs 3 sticks, 2 triangles ne" (term/l1/habit_items.json)
- REVIEW L1-flagcards [01-17]: longest sentence 21 words (limit 20)
- REVIEW L1-lighthouse [01-18]: rule B: 3 of the same numbers ['12', '3', '8'] as "12 factors: 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72. Workbook Think harder 2: On ..." (p4/Math_Inquirers_P4_Tutor_Guide.html)
- REVIEW L1-floormat [01-19]: rule S: sentence "Lena covers a floor mat with 7 rows of 9 square tiles." shares 4 content words with "A square floor is covered with square tiles." (outputs/extension/L4/Math_Inquirers_L4_Extension_Workbook_Print_BW_vector.pdf)
- REVIEW L1-busseats [01-22]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-busseats [01-22]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-cousinstay [01-23]: story words 4 of 6 like "About 15 minutes, a few days after the lesson. Use your day cards and the month page, or a ..." (outputs/print/term/Math_Inquirers_L1_T3_Book6_Lessons06-10_HomePack_PRINT.pdf)
- REVIEW L1-rafflepicks [01-26]: number 52 in the question is not a parameter (written in the wording; check)
- REVIEW L1-rafflepicks [01-26]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-rafflepicks [01-26]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-rafflepicks [01-26]: number 7 in the question is not a parameter (written in the wording; check)
- REVIEW L1-rafflepicks [01-26]: rule B: 3 of the same numbers ['3', '5', '7'] as "| Prelim | 2024 | Nanyang | P2-3 | 2 | Average of 7 numbers is 7; add one: avera ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L1-borrowedbooks [01-28]: longest sentence 25 words (limit 20)
- REVIEW L1-borrowedbooks [01-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-borrowedbooks [01-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-borrowedbooks [01-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-borrowedbooks [01-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-borrowedbooks [01-28]: story words 5 of 5 like "Week 3 total?"], "q": "2(b). In Week 3, each class borrowed 6 more books than in Week 2. H ..." (practice/holiday/p4/09/dist/data/p4l09.json)
- REVIEW L1-borrowedbooks [01-28]: rule S: sentence "A table shows how many library books four classes borrowed this week: " shares 6 content words with "The table shows how many books three classes borrowed from the library" (practice/holiday/p4/09/dist/data/p4l09.json)
- REVIEW L1-robotturns [01-29]: rule S: sentence "Which way does it face now: north, east, south or west?" shares 4 content words with "(1) south-east (2) south-west (3) north-east (4) north-west ANSWER:" (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L2-padlockcode [01-01]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-hallchairs [01-04]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-hallchairs [01-04]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L2-hallchairs [01-04]: story words 3 of 4 like "Q: In a school hall, chairs were arranged in 9 equal rows. ..." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L2-hallchairs [01-04]: rule S: sentence "A school hall has 12 chairs in every row." shares 4 content words with "Q: In a school hall, chairs were arranged in 9 equal rows." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L2-penspacks [01-15]: rule B: 3 of the same numbers ['4', '5', '7'] as "Then count the pieces.', figure=tags([('Marker pen', '$2.85'), ('Kite', '$7.40') ..." (extension/l2/author/u06.py)
- REVIEW L2-marathon [01-19]: rule B: 3 of the same numbers ['4', '7', '8'] as "| Every answer verified independently (verify/lNN_checks.py) | PASS | 214 checks ..." (term/l1/AUDIT_L39.md)
- REVIEW L2-netballleague [01-20]: story words 4 of 6 like "(Each pair of teams plays twice: 15 pairs × 2 = 30.)"], "slips": [], "tags": {"strand": "C ..." (practice/holiday/p6/05/dist/data/p6l05.json)
- REVIEW L2-roomstickers [01-21]: rule B: 3 of the same numbers ['3', '6', '8'] as "| 1 | Shifting Places | LIST (T, N): digit cards: smallest or greatest even numb ..." (docs/terms/level_5_year_plan.md)
- REVIEW L2-topupvouchers [01-22]: rule B: 3 of the same numbers ['4', '40', '7'] as "| 4 | 4 Pattern Machines | Beads red-red-blue-green; houses 5, 9, 13 sticks; 2,  ..." (docs/terms/l2_preflight.md)
- REVIEW L2-shoegraph [01-26]: rule B: 3 of the same numbers ['11', '25', '4'] as "| Prelim | 2021 | TaoNan | B2-14 | 5 | line graph | 3 | 1 | Residents in Town A  ..." (docs/books/private_p6_papers/non_routine_questions.md)
- REVIEW L2-bunboxes6 [01-27]: story words 3 of 3 like ""text": "A baker packs 43 buns into boxes of 6. ..." (extension/data/l3_u05.json)
- REVIEW L2-bunboxes6 [01-27]: rule S3: the sentence "A baker packs buns into boxes of 6." is like ""text": "A baker packs 43 buns into boxes of 6." (extension/data/l3_u05.json)
- REVIEW L2-festivalshows [01-29]: longest sentence 23 words (limit 22)
