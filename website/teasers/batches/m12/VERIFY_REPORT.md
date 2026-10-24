# Teaser batch m12 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 31 | 29 | 2 | 25 | 3 | 31 |

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 2. REVIEW items: 4.

- FAIL L1-threeodds [12-19]: shares a 7-word run with term: "5 7 is the total odd or"
- FAIL L1-orangebags [12-30]: shares a 7-word run with term: "every bag how many bags is that"

- REVIEW L1-bondten [12-10]: number 0 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bundles [12-15]: number 10 in the question is not a parameter (written in the wording; check)
- REVIEW L1-digitvalue [12-26]: longest sentence 21 words (limit 20)
- REVIEW L1-ruler [12-29]: longest sentence 22 words (limit 20)
