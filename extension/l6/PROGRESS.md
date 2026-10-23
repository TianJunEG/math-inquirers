# Level 6 Extension Workbook: progress note

Author pipeline: unit source `extension/l6/src/uNN.py` (Python, helpers in `src/lib.py`) -> `python3 extension/l6/src/uNN.py` writes `extension/data/l6_uNN.json` and
picks the Start here pages with `extension/l6/tools/measure.py` (measures every item in the real stylesheet and fits them to 3 pages of 87 to 98.5 percent).
Checks: `extension/verify/l6_uNN_checks.py` (+ `l6_lib.py`, a small interpreter that runs the printed code blocks). Figures: `extension/tools/figs_l6_core.py`, `figs_l6_geo.py` (types start with `l6_`).
Quick view: `python3 extension/tools/build.py --level 6 --units N --no-bw`.

Per-unit status (G = gates: answers checked, wording lint, dup gate, build, pages viewed)
| Unit | Title | Status |
|---|---|---|
| 1 | Code the pattern | done, gates pass, viewed |
| 2 | Prime hunters | done, gates pass, viewed |
| 3 | Below zero | done, gates pass, viewed |
| 4 | Algebra machines | done, gates pass, viewed |
| 5 | Every possible way | done, gates pass, viewed |
| 6 | Fair or unfair? | done, gates pass, viewed |
| 7 | Turtle geometry | done, gates pass, viewed |
| 8 | Secret codes | done, gates pass, viewed |
| 9 | Data detectives | done, gates pass, viewed |
| 10 | Showcase challenge | done, gates pass, viewed |

To resume: start the next unit in the table: write `src/uNN.py` (copy the shape of `src/u01.py`), run it (it prints the page fills), write `verify/l6_uNN_checks.py`, then
`python3 extension/verify/run_checks.py --level 6`, `wording_lint.py --level 6`, `dup_check.py --level 6`, build, view every page, commit only the Level 6 paths.
