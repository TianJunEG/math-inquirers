# Teaser batch m11 verification report

Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.

| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |
|---|---|---|---|---|---|---|
| 1 | 30 | 27 | 2 | 23 | 3 | 30 |

Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, external private source files, and the seven fixed website puzzles.

FAIL count: 7. REVIEW items: 4.

- FAIL L1-stickerswap [11-13]: shares a 7-word run with external: "same number of stickers how many stickers"
- FAIL L1-stickerswap [11-13]: shares a 7-word run with the extension workbooks: "number of stickers how many stickers does"
- FAIL L1-reading [11-16]: shares a 7-word run with term: "an hour how many minutes is that"
- FAIL L1-backplace [11-19]: shares a 7-word run with term: "3rd from the front what place is"
- FAIL L1-cards307 [11-21]: shares a 7-word run with external: "3 digit number what is the smallest"
- FAIL L1-tencoins [11-27]: doubled word "sets sets" in why
- FAIL L1-stargraph [11-29]: forbidden word in q: picture

- REVIEW L1-toast [11-14]: number 1 in the question is not a parameter (written in the wording; check)
- REVIEW L1-samedigits [11-20]: number 2 in the question is not a parameter (written in the wording; check)
- REVIEW L1-change [11-25]: number 3 in the question is not a parameter (written in the wording; check)
- REVIEW L1-change [11-25]: number 2 in the question is not a parameter (written in the wording; check)
