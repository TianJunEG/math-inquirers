# Level 4 progress

Pipeline: unit sources are `extension/l4/src/uNN.py` (helpers in `lib.py`); `python3 extension/l4/src/uNN.py` writes `extension/data/l4_uNN.json`. Checks: `extension/verify/l4_uNN_checks.py`. Figures: `extension/tools/figs_l4_*.py`.

| Unit | Status |
|---|---|
| 1 Factor Hunters | written, checked, gates ok, viewed |
| 2 Big Number Puzzles | written, checked, gates ok, viewed |
| 3 Operation Detectives | written, checked, gates ok, viewed |
| 4 Fraction Frontier | written, checked, gates ok, viewed |
| 5 Decimal Detectives | written, checked, gates ok, viewed |
| 6 Angle Turns | written, checked, gates ok, viewed |
| 7 Area Architects II | written, checked, gates ok, viewed |
| 8 Symmetry and Nets | written, checked, gates ok, viewed |
| 9 Data Detectives | written, checked, gates ok, viewed |
| 10 Puzzle Day | written, checked, gates ok, viewed |

Status: all 10 units written, checked, viewed (colour edition, every unit page) and committed. Full build done: both PDFs are 102 pages (even); contents and answer page numbers are right (answers start on page 79 divider, unit 1 answers on page 80). Gates run for Level 4: run_checks (422 answers, 0 mismatches), dup_check (no shared 7-word run; REVIEW list read and accepted), wording_lint (0 errors), build (no overflow, every unit page at least 85 percent full), bw_check and print/check_bw on the Level 4 print PDF (0 colour pixels, 0 flat grey), fill_check OK. `verify_all.sh 4` calls `bw_check.py` without arguments, which scans every level's print PDF; the Level 4 gates were therefore run on the Level 4 file only.

Resume: nothing left to write. If a unit is edited, rerun `python3 extension/l4/src/uNN.py`, then the full build and the gates above. Open items for people: independent audit, child trial, owner review.
