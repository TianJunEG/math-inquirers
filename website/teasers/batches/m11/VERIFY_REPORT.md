# Teaser batch m11 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 30 | 27 | 2 | 23 | 3 | 30 |
| 2 | 30 | 30 | 1 | 23 | 3 | 30 |

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 0. REVIEW items: 6.


- REVIEW L1-samedigits [11-20]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-change [11-25]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-change [11-25]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L2-liftmax [11-22]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stickerbook [11-25]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stickerbook [11-25]: number 3 in the question is not a parameter (written in the wording; check)
