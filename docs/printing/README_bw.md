# Black-and-white print pipeline (owner decision 23 Oct 2026)

Printed (posted) workbooks are black and white; soft copies stay colour.

## One command
```
python3 print/make_bw_print.py --rebuild --check     # rebuild colour print PDFs, convert all, check
python3 print/make_bw_print.py --check               # convert what is already in outputs/print and outputs/print/term
python3 print/make_term_books.py --level 1 --bw      # rebuild term books, then B&W + check
python3 print/make_bw_print.py --only L1_T2          # a subset (substring of the file name)
python3 print/check_bw.py                            # re-run only the checks on outputs/print/bw
```
About 4 s per page on 4 cores (roughly 10 minutes for everything). Needs PyMuPDF (`pip install pymupdf`), Pillow, numpy.

## Output
`outputs/print/bw/Math_Inquirers_P1..P6_Workbook_PRINT.pdf`, `outputs/print/bw/term/*_PRINT.pdf` (workbook, AnswerKey_TUTOR, HomePack for each book), `outputs/print/bw/bw_spec.json`. Each is a 1-bit 600 dpi CCITT G4 PDF with exactly the same page count, order, blank backs, kit-page positions and 12 mm gutter as its colour source. The colour print PDFs stay in `outputs/print/` (soft copies / reference).

## How colour is handled (no source change, soft copies untouched)
Each page is rendered at 600 dpi and mapped pixel by pixel: dark (luma < 0.42) becomes solid black; very light tints (luma > 0.90: grid paper, cream and pale boxes) become white; mid-tones become a pattern by hue family: red/pink = diagonal hatch (/), orange/gold/yellow = dots, green = diagonal hatch (\\), blue/teal = horizontal lines, purple = vertical lines, neutral grey = fine stipple; weight follows lightness (capped at 50% so text on a fill stays legible). So red and yellow counters, tier chips, graph keys and coloured shapes stay distinguishable on a photocopier, and "same colour" becomes "same pattern".

## Checks (`print/check_bw.py`)
Per file: share of non-grey pixels (must be 0; FAIL if > 0.05%), blank pages, and "light-tint cells" (8 px cells with 1 to 15% ink: areas that reproduce unreliably). Patterns count as ink, so tint cells only arise from isolated fine dots.

## Limits
Pale tints are deliberately dropped (the grid background disappears; ruled answer lines remain). Real "colour it red" tasks work with crayons. Text that is only a light colour on white is darkened only if luma < 0.42; very light coloured text (rare) is lost: audit list in the 23 Oct report. Rebuild after Term 2 fixes land with the first command above.
