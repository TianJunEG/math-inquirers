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

## Final state (23 Oct 2026)
All ten units written, checked (526 answers), linted, dup-gated and viewed. Full build: soft copy 100 pages, print 100 pages (even), answers from page 80, contents page numbers match.
Gates run on the final build: run_checks OK, dup_check OK, wording_lint OK, bw_check OK, print/check_bw OK, fill_check OK (no page under 85 percent, no overflow).
Open: the Welcome page still carries the Level 1 sentence about rulers and the shared renderer prints nothing level-aware; the coordinator is changing build.py/render.py to read per-level keys from levels.json. When that lands, set the Level 6 keys (no rulers; Beyond label) and rebuild; Level 6 items can then use the `beyond` key instead of the text label (see TOOL_REQUESTS.md).
