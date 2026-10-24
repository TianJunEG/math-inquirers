# Teaser batch m12 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 31 | 29 | 2 | 25 | 3 | 31 |

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 15. REVIEW items: 6.

- FAIL L1-fruitclass [12-06]: doubled word "children children" in why
- FAIL L1-bondten [12-10]: shares a 7-word run with holiday: "3 7 and 7 3 count as"
- FAIL L1-bundles [12-15]: shares a 7-word run with term: "14 loose sticks how many sticks does"
- FAIL L1-threeodds [12-19]: hint gives the answer away
- FAIL L1-squares22 [12-22]: shares a 7-word run with holiday: "can you find count the small ones"
- FAIL L1-squares22 [12-22]: shares a 7-word run with external: "any size can you find count the"
- FAIL L1-squares22 [12-22]: shares a 7-word run with term: "count the small ones and the big"
- FAIL L1-fewestcoins [12-27]: doubled word "coins coins" in why
- FAIL L1-fewestcoins [12-27]: shares a 7-word run with holiday: "coins what is the smallest number of"
- FAIL L1-fewestcoins [12-27]: shares a 7-word run with external: "10 cent 20 cent and 50 cent"
- FAIL L1-bluebeads [12-28]: shares a 7-word run with holiday: "blue blue how many blue beads are"
- FAIL L1-ruler [12-29]: shares a 7-word run with holiday: "does not start at 0 count the"
- FAIL L1-orangebags [12-30]: shares a 7-word run with term: "in each bag how many bags does"
- FAIL L1-orangebags [12-30]: shares a 7-word run with the extension workbooks: "in each bag how many bags does"
- FAIL L1-pets [12-31]: shares a 7-word run with holiday: "does not have the cat who has"

- REVIEW L1-bondten [12-10]: number 0 in the question is not a parameter (written in the wording; check)
- REVIEW L1-threeodds [12-19]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-threeodds [12-19]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L1-threeodds [12-19]: number 7 in the question is not a parameter (written in the wording; check)
- REVIEW L1-digitvalue [12-26]: longest sentence 21 words (limit 20)
- REVIEW L1-ruler [12-29]: longest sentence 22 words (limit 20)
