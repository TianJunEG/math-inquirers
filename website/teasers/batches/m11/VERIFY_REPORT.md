# Teaser batch m11 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 30 | 27 | 2 | 23 | 3 | 30 |
| 2 | 30 | 30 | 1 | 23 | 3 | 30 |
| 3 | 30 | 30 | 1 | 24 | 2 | 30 |
| 4 | 30 | 28 | 2 | 25 | 2 | 30 |

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 9. REVIEW items: 19.

- FAIL L4-gate [11-01]: shares a 7-word run with external: "a 2 m gap for a gate"
- FAIL L4-motherage [11-05]: shares a 7-word run with the extension workbooks: "mother is 3 times as old as"
- FAIL L4-fourclaims [11-06]: shares a 7-word run with the extension workbooks: "child is not telling the truth who"
- FAIL L4-books [11-08]: sub-structure money.change is not allowed at level 4 (levels [1, 2, 3])
- FAIL L4-symmetry [11-21]: shares a 7-word run with holiday: "a rectangle that is not a square"
- FAIL L4-symmetry [11-21]: shares a 7-word run with the extension workbooks: "a rectangle that is not a square"
- FAIL L4-grass [11-22]: shares a 7-word run with the extension workbooks: "12 m long and 8 m wide"
- FAIL L4-rects33 [11-23]: not an instance of sub-structure counting_grid.rectangles_in_grid (parameter what='rects' not in ['rectangles'])
- FAIL L4-smallest5 [11-26]: shares a 7-word run with external: "digits add up to 20 what number"

- REVIEW L1-samedigits [11-20]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-change [11-25]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-change [11-25]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L2-liftmax [11-22]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stickerbook [11-25]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L2-stickerbook [11-25]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-houses [11-08]: number 21 in the question is not a parameter (written in the wording; check)
- REVIEW L3-houses [11-08]: number 22 in the question is not a parameter (written in the wording; check)
- REVIEW L3-houses [11-08]: number 23 in the question is not a parameter (written in the wording; check)
- REVIEW L3-round350 [11-11]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L3-palin [11-17]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-palin [11-17]: number 232 in the question is not a parameter (written in the wording; check)
- REVIEW L3-palin [11-17]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-fewestdollar [11-24]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L4-towerblocks [11-15]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L4-towerblocks [11-15]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L4-towerblocks [11-15]: number 6 in the question is not a parameter (written in the wording; check)
- REVIEW L4-towerblocks [11-15]: number 9 in the question is not a parameter (written in the wording; check)
- REVIEW L4-smallest5 [11-26]: number 5 in the question is not a parameter (written in the wording; check)
