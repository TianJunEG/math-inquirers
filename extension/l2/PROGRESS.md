# Level 2 extension workbook: progress

Author scripts: extension/l2/author/uNN.py (build data/l2_uNN.json with lib.py). Checks: extension/verify/l2_uNN_checks.py. Figures: extension/tools/figs_l2_*.py (type names start with l2_).

| Unit | Title | Status |
|---|---|---|
| 1 | Digit detectives | done (checks, dup, lint, pages viewed) |
| 2 | Missing digit mysteries | done |
| 3 | Legs, wheels and arrays | done |
| 4 | Pattern machines | done |
| 5 | Mystery number machines | done |
| 6-10 | | remaining |

Resume: write unit N with extension/l2/author/uNN.py, checks, build with `python3 extension/tools/build.py --level 2 --units N --no-bw --out <scratch>`.
Issues: none yet.

Note: lib.build sorts start items by page so printed numbers = answer numbers = ids. Scratch builds go to scratchpad/l2w (the scratchpad is shared with other agents; keep to that folder).
