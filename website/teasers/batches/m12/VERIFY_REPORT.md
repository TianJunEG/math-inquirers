# Teaser batch m12 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 31 | 28 | 2 | 24 | 3 | 31 |
| 2 | 31 | 29 | 2 | 25 | 3 | 31 |
| 3 | 31 | 28 | 2 | 25 | 2 | 31 |
| 4 | 31 | 29 | 2 | 30 | 2 | 31 |

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 7. REVIEW items: 20.

- FAIL L4-chesssquares [12-01]: shares a 7-word run with external: "how many squares of any size can"
- FAIL L4-visitortable [12-02]: sub-structure graphs.table_total is not allowed at level 4 (levels [1, 2, 3])
- FAIL L4-outfitsthree [12-15]: shares a 7-word run with external: "how many different outfits can she make"
- FAIL L4-yearlater [12-16]: sub-structure calendar.weekday_after is not allowed at level 4 (levels [1, 2, 3])
- FAIL L4-stationery [12-20]: sub-structure place_value.regroup is not allowed at level 4 (levels [1, 2, 3])
- FAIL L4-palyears [12-29]: shares a 7-word run with holiday: "reads the same forwards and backwards like"
- FAIL L4-palyears [12-29]: shares a 7-word run with the extension workbooks: "number reads the same forwards and backwards"

- REVIEW L1-bondten [12-10]: number 0 in the question is not a parameter (written in the wording; check)
- REVIEW L1-bundles [12-15]: number 10 in the question is not a parameter (written in the wording; check)
- REVIEW L2-bigtens [12-07]: number 31 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cartons [12-04]: number 1000 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cartons [12-04]: number 100 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cartons [12-04]: number 10 in the question is not a parameter (written in the wording; check)
- REVIEW L3-smalldigitsum [12-08]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-watertank [12-16]: number 12 in the question is not a parameter (written in the wording; check)
- REVIEW L3-watertank [12-16]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L3-dotgaps [12-17]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L3-strawbridge [12-21]: number 5 in the question is not a parameter (written in the wording; check)
- REVIEW L3-cryptsum [12-22]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L4-unpainted [12-08]: number 64 in the question is not a parameter (written in the wording; check)
- REVIEW L4-liftmin [12-09]: number 4 in the question is not a parameter (written in the wording; check)
- REVIEW L4-shellpiles [12-14]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-18]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L4-tilefigures [12-18]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L4-stationery [12-20]: number 1000 in the question is not a parameter (written in the wording; check)
- REVIEW L4-stationery [12-20]: number 100 in the question is not a parameter (written in the wording; check)
- REVIEW L4-stationery [12-20]: number 10 in the question is not a parameter (written in the wording; check)
