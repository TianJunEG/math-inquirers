# Teaser batch m01 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 31 | 30 | 2 | 21 | 3 | 31 |
| 2 | 31 | 31 | 1 | 26 | 2 | 31 |

Sources searched (whole working tree, tracked or not): 6760 files, 1363.2 MB, sha256 f23be12b38f2ffc78ecacad9.  Files per root: deck 158, diag 12, docs 423, extension 257, hp 41, k2 5, levels 23, mascot 4, ops 14, outputs 180, p1 1, p2 27, p3 27, p4 27, p5 28, p6 38, portal 45, practice 373, print 6, rebuild 87, releases 1, review 1, school 474, split 1801, taster 2, term 2532, tutor 130, website 42, worker 1.

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 0. REVIEW items: 31.


- REVIEW L1-tagtiles [01-01]: rule B: 3 of the same numbers ['6', '7', '9'] as "| Challenge (bank X1-X9) | 9 | **X3** "Ravi: 24 m of fence, largest area": list  ..." (docs/audit/gifted_p4.md)
- REVIEW L1-noodlepot [01-03]: rule B: 3 of the same numbers ['35', '5', '6'] as "First clock: the long hand is on the 1: 5 minutes past 1, written 1:05. Second c ..." (term/l1/lessons/l22.json)
- REVIEW L1-prizecorner [01-04]: story words 3 of 5 like "The slide plants the misconception "the hour changes at half past" (the hour hand is half  ..." (term/l1/audit/GUIDE_DECK_AUDIT_L23.md)
- REVIEW L1-starchart [01-08]: story words 3 of 5 like "Teacher-note edits: the figures are sketches except P5-28; excluded topics "are not used i ..." (docs/audit_final/p5_semester_booklets_audit_round2.md)
- REVIEW L1-bikelock [01-10]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bikelock [01-10]: story words 3 of 5 like "body = h2('Worked example: a bike lock') + card(p('A lock has 3 dials. Each dial shows 1,  ..." (rebuild/gen_p6l5.py)
- REVIEW L1-busdepart [01-12]: story words 3 of 5 like "- [EOY_2024_NanChiau Q34, 2m, Timetable, diff 2] Bus schedule table: leaves Singapore 06 5 ..." (docs/books/private_p4_papers/non_routine_questions.md)
- REVIEW L1-pagefives [01-14]: number 52 in the question is not a parameter (written in the wording; check)
- REVIEW L1-pagefives [01-14]: rule B: 3 of the same numbers ['15', '5', '52'] as "A brace under the bar asks for the minutes in all." style="width:100%;max-width: ..." (practice/holiday/p5/06/dist/data/p5l06.json)
- REVIEW L1-lighthouse [01-18]: rule B: 3 of the same numbers ['12', '3', '8'] as "12 factors: 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72. Workbook Think harder 2: On ..." (p4/Math_Inquirers_P4_Tutor_Guide.html)
- REVIEW L1-floormat [01-19]: rule S: sentence "Lena covers a floor mat with 7 rows of 9 square tiles." shares 4 content words with "A square floor is covered with square tiles." (outputs/extension/L4/Math_Inquirers_L4_Extension_Workbook_Print_BW_vector.pdf)
- REVIEW L1-busseats [01-22]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-busseats [01-22]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-cousinstay [01-23]: story words 4 of 6 like "About 15 minutes, a few days after the lesson. Use your day cards and the month page, or a ..." (outputs/print/term/Math_Inquirers_L1_T3_Book6_Lessons06-10_HomePack_PRINT.pdf)
- REVIEW L1-capcollect [01-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-capcollect [01-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-capcollect [01-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-capcollect [01-28]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-robotturns [01-29]: story words 3 of 5 like "- **Non-routine.** LOG T (V23.1), LIST T (V23.2), CTX G (directions without a compass). -  ..." (docs/terms/l3_preflight.md)
- REVIEW L1-coveredbit [01-31]: story words 3 of 3 like "f = F('s-rem3'); eq((f['jumps'][0][0], f['jumps'][0][1], f['jumps'][0][2]), (7, 12, '+5'), ..." (term/l1/verify/l39_checks.py)
- REVIEW L2-padlockcode [01-01]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L2-hallchairs [01-04]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-hallchairs [01-04]: rule S: sentence "Chairs in a school hall are put out in rows of 12." shares 4 content words with "Q: In a school hall, chairs were arranged in 9 equal rows." (docs/books/private_p3_papers/non_routine_questions.md)
- REVIEW L2-pencilsodd [01-08]: rule S (window): 5 of 7 content words (colour,even,hold,odd,pencil) in "- **Odd/even and division honesty.** Not applicable here; "every secon ..." (term/l1/audit/GUIDE_DECK_AUDIT_L16.md)
- REVIEW L2-boardroutes [01-09]: rule S: sentence "It can move one square right or one square down at a time." shares 4 content words with "It moves down 1, then right 1." -> "A counter is on 26 on the 100 squa" (term/l1/WORDING_REVIEW_L04.md)
- REVIEW L2-penspacks [01-15]: rule B: 3 of the same numbers ['4', '5', '7'] as "Then count the pieces.', figure=tags([('Marker pen', '$2.85'), ('Kite', '$7.40') ..." (extension/l2/author/u06.py)
- REVIEW L2-bookswaps [01-18]: rule B: 3 of the same numbers ['12', '3', '6'] as "Type a fraction.", "label": "T3 (left)", "svg": "<svg overflow="visible" aria-la ..." (practice/holiday/p3/06/dist/data/p3l06.json)
- REVIEW L2-netballleague [01-20]: rule C: two four-word runs shared with "(Each pair of teams plays twice: 15 pairs × 2 = 30.)"], "slips": [], "tags": {"s ..." (practice/holiday/p6/05/dist/data/p6l05.json): plays every other team / team plays every other
- REVIEW L2-roomstickers [01-21]: rule B: 3 of the same numbers ['3', '6', '8'] as "| 1 | Shifting Places | LIST (T, N): digit cards: smallest or greatest even numb ..." (docs/terms/level_5_year_plan.md)
- REVIEW L2-topupvouchers [01-22]: rule B: 3 of the same numbers ['3', '4', '7'] as "The answer is 5, 10." (the answer is also shown as "5, 10", not "5/10"). Either  ..." (practice/holiday/AUDIT_WEEK5_L1_3.md)
- REVIEW L2-bunboxes6 [01-27]: rule B: 3 of the same numbers ['14', '5', '6'] as "?" (no neighbours of the answer), figure beside the text; intro clear of the "No ..." (term/l1/audit/AUDIT_FINAL_ROUND4.md)
