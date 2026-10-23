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

## Final state (23 Oct 2026, after audit rounds 1 to 3)
Round 1: clone items re-framed, give-aways removed, Learn gaps filled. Round 2: unit 3 Learn step corrected, two stale Why overrides rewritten, clone items replaced in units 3, 9 and 10, code legend extended, unit 2 tests for 4 and 9, unit 7 angle sum, unit 10 G1 prints `answer`.
Round 3 (last pass): legend now also explains the green flag, > and <, and a clearer if/else line; pointers to it on p. 6 (unit 1 Learn) and p. 7 (first code item). Lows: unit 3 example arc no longer crosses a label, the unit 10 S2 Why no longer names 111, "no smaller number" Whys reworded, unit 9 T3 and G3 hints softened, "stickers" removed from unit 9 S8, unit 1 C1 changed to difference 6, unit 10 S12 is now a coin-jar story.
Full build 100 pages in both editions, answers from page 80, legend on page 27. 528 answers independently checked.
Open: a Welcome-page pointer to the legend needs a `welcome_notes` entry in levels.json (not edited by the author); the six "missing mean" items were not varied; owner review, child trial of pace, tutor's real Scratch run, printer proof.
