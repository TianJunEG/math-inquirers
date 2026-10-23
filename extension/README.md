# Extension workbooks: tooling

Self-study extension workbooks (one per level, with answers; physical and soft copy). Plan, spec, QA and estimates: `docs/extension_books/plan.md`.

```
extension/
  config/levels.json        page grid, type sizes, writing space, lint thresholds and the 10 unit titles per level
  data/lN_uXX.json          one unit: learn page, items (tier, text, figure, answer, explanation, hint)
  tools/figs.py             figure specs -> SVG (colour, or black and white with patterns); reuses term/l1/tools/svg.py
  tools/render.py           unit data -> page HTML
  tools/ext.css             stylesheet (palette from hp/wb_style.css; two themes: colour, bw)
  tools/build.py            builds the colour soft copy and the black-and-white print PDF
  verify/lN_uXX_checks.py   independent per-item answer checks (recompute, never copy)
  verify/run_checks.py      schema + answer runner (fails on any mismatch or missing check)
  verify/dup_check.py       7-word overlap against the holiday banks, private source texts, term lessons
  verify/wording_lint.py    reading load and wording rules from term/l1/WORDING_GUIDE.md
  verify/bw_check.py        colour and flat-grey measurement of the print PDF at 200 dpi
  verify/fill_check.py      page fill (85 percent) and overflow gate
  verify_all.sh [level]     all gates, then the PDFs are in outputs/extension/L<level>/
```

Build one level: `python3 extension/tools/build.py --level 1` (units found in `data/`, or `--units 1,2`).
Run every gate: `extension/verify_all.sh 1`.

Needs: python3 with playwright (chromium), pypdf, PyMuPDF (fitz), Pillow, numpy, scipy; fonts from `fonts/node_modules/@fontsource` (run `npm install` in `fonts/`).
`dup_check.py` reads the gitignored private source files (`docs/books/private_*`, `docs/sasmo/private_*`); on a checkout without them it prints a warning and the external check is NOT run.

Status: Level 1 units 1 and 2 are written (proof of the pipeline). Everything else is plan.
