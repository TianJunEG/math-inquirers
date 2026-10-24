# Colour-by-code pages: box-size guard, Primary 1, 2 and 4 (Primary 3 skipped)

Done 23 Oct 2026, following `colour_page_key_match_check.md`. Code-hardening only: no colour page, key, complete pack or front matter changes.

## What changed

1. **Page box size is now the library default** (so `make_sheet`, `layout.fit` and `layout.render` pick the same questions and the same box whichever code path calls them):
   - `school/p2/cbc_vendor/layout.py:15`: `BOX_SIDE = 9.0` (was 6.0).
   - `school/p4/cbc_vendor/layout.py:15-16`: `BOX_W = 17.5`, `BOX_SIDE = 12.3` (were `None` and 6.0).
   - `school/p1/cbc_vendor/layout.py:15`: default stays 6.0 (P1-01 and P1-14 use 6.0); a comment names the one per-page override. P1-12 still sets 8.0 in `gen/pages_cbc.py` `page12()` (try/finally). **Residual P1 hazard:** a build of P1-12 outside `page12()` still uses 6.0. The new validate check below would catch it for what is printed.
   - The `old = L.BOX_SIDE ... finally` wrappers in each `gen/pages_cbc.py` were left in place (they now set the value that is already the default).
2. **`validate.py` of P1, P2 and P4 has the P6 check** (inserted before the browser layout block, the same place as P6): every `data-t` question string on the colour pages of `out/S?_pupil.html` must be in `out/S?_key.html`. In addition (the "ideally" part), every question line of each colour page's own sheet (`p["sheet"]`) must be printed in `P?_S?_Puzzles.pdf` and `P?_S?_Complete_Pack.pdf` (pupil page, blank box removed) and in `P?_S?_Answer_Key.pdf` (the answer stands where the box is, so the box is a wildcard of up to 14 characters). Text comes from `pdftotext -raw`, whitespace and thin spaces removed, restricted to the PDF pages that carry the page code. 11 new PASS lines per level (2 HTML + 3 pages x 3 PDFs).

## Before / after comparison

- Sheet level: `build.all`-independent dump of each level's 3 colour pages (body SVG hash, teacher SVG hash, every question line and answer, check text, key text) before and after: **identical** for P1, P2, P4 (9 pages). Building each page's spec with a bare `make_sheet` outside the wrapper equals the page build for P2 and P4 (P1-01, P1-14 too; P1-12 differs as expected, see above).
- PDF level: I rebuilt all eight PDFs per level (P1, P2, P4) once with the old layout files and once with the new ones, in the scratchpad (`build.py --outdir`), and compared `pdftotext -layout` and the md5 of every page at 70 dpi: **all 24 PDFs identical in text and pixels**, so the 9 colour pages (P1-01, 12, 14; P2-38, 39, 40; P4-05, 11, 40), their keys, the packs and the front matter are unchanged.
- Note: a fresh build in this container differs from the committed `out/*.pdf` (line wrapping and spacing in many pages, e.g. P1 "Kumar" line), with old and new code alike, so it is an environment effect (fonts/renderer), not this change. `school/pN/out` was not touched or rebuilt. The questions in the committed colour pages equal the code's (the sheet dump above was run on the committed code and the new code).
- `validate.py` run once per level on the fresh scratch builds (`--outdir`): P1 796 checks, 0 failed; P2 758, 0 failed; P4 746, 2 failed: `P4_S1/S2_FrontMatter.pdf: no flat grey tint areas`. That failure also exists with the old code (front matter is pixel-identical old vs new) and not in the committed `p4/out/validation_report.txt` (0 FAIL), so it comes from rendering in this container, not from this change. P4 validate was fast here, not 25 minutes.
- Not run: P3.

## Skipped: Primary 3

`git status` showed uncommitted edits by another builder in `school/p3` (`gen/art2.py`, `art3.py`, `css_p3.py`, `pages_s2b.py`, `pages_s2d.py`, `kit.py`, `render.py`, rebuilt `out/` PDFs), so I made no change in P3 (I reverted my own first insert into `p3/validate.py`). Left for P3: the same two changes, `school/p3/cbc_vendor/layout.py:15` `BOX_SIDE = 12.0`, and the validate block (copy it from `school/p4/validate.py`, search "the colour pages: the questions printed"; change `P4` to `P3` in the three PDF names).

## Left for P5 and P6

- P5: port the same validate block (replace `P4` by `P5` in the PDF names) and set `school/p5/cbc_vendor/layout.py:15` `BOX_SIDE = 9.0`. Not touched (other agents are working there).
- P6: has the HTML check and the default (11.0); it does not have the sheet-vs-PDF text check, which can be copied from P4 if wanted.
- `school/colour_by_code/layout.py` still defaults to 6.0 (nothing there sets another size).

## Primary 3 and Primary 6 (23 Oct 2026, follow-up)

Code hardening only. Changed: `school/p3/cbc_vendor/layout.py` (`BOX_SIDE = 12.0`, the value `gen/pages_cbc.py` `cbc_page()` sets; the try/finally wrapper is left in place), `school/p3/validate.py` (the P4 block ported, `P4_` changed to `P3_`: the HTML pupil-vs-key check plus the sheet-vs-PDF check), `school/p6/validate.py` (the sheet-vs-PDF check added after its existing HTML check; its 11.0 default is unchanged).

- Sheet level: for P3-14, 39, 40 and the P6 colour pages (S1-09, S2-12, S2-20) I dumped every question line and answer, key text, check text, body SVG hash, teacher SVG hash, thumbnail hash and instruction before and after: **identical** (both levels).
- PDF level: built all eight PDFs per level once with a copy of the old code and once with the new, in scratch dirs (`build.py --outdir`, with the `fonts` folder reachable so both builds use the real fonts), and compared `pdftotext -layout` and the md5 of every page at 70 dpi: **all 16 PDFs identical in text and pixels** (also S1_key.html and S2_pupil.html byte-identical). `school/p3/out`, `school/p6/out` and other levels were not touched.
- `validate.py` once per level on the scratch builds (`--outdir`), new code vs old code on the same old build:
  - P3: new 755 checks, 1 failed; old 744 checks, 1 failed (+11 new PASS lines: 2 HTML + 3 pages x 3 PDFs). The failure `S2 pupil page 08 layout (no overflow/clipping/margin breach): content leaves puzzle area` is the same with the OLD code (not a colour page; a rendering effect in this container).
  - P6: new 757 checks, 5 failed; old 748, 5 failed (+9 new PASS lines for the PDF check; the HTML check was already there). The 5 failures (S1/S2 "marked DRAFT ... 6 DRAFT stamps", S1/S2 front page 02 layout, S2 key page 01 layout) are all identical with the OLD code and none is on a colour page.
- Still open: P5 (done by its builder), `school/colour_by_code/layout.py` default 6.0.
