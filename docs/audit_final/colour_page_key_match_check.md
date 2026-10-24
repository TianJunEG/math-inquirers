# Colour-by-code pages, Primary 1 to 5: does the Answer Key match the pupil page?

Checked 23 Oct 2026, on the committed PDFs (commit `9768175`) and again on the latest PDFs in the working tree at 21:50 (commit `50cfabb`, P4 and P5 PDFs rebuilt at 21:47 and 21:48); a third run after all builds had finished gave the same result. Nothing was edited except this file.

## Result

**No mismatch found in any of the 14 colour-by-code pages of P1 to P5.** On every page the questions printed on the pupil page are the questions printed in the key, the key's colouring and tally are the right ones for the pupil page, and the Complete Pack pupil page is identical to the Puzzles pupil page. The bug P6 found (key shows different questions from the pupil page) is **not present in the P1 to P5 PDFs**. It is, however, **latent in all five vendored copies** (see "Root cause" below): the pipelines are correct only because nothing builds a sheet outside the `BOX_SIDE` wrapper today, and none of P1 to P5 has the validate check that P6 added.

| Level | Page | Picture and topic | Pupil vs key (questions, labels, pictures) | Hand colouring vs key colouring and tally | Complete Pack pupil page = Puzzles pupil page |
|---|---|---|---|---|---|
| P1 | P1-01 (S1-02) | Rocket, tens and ones | match | match, 15 parts, tally 3/4/2/4/2 | identical |
| P1 | P1-12 (S1-04) | House, corners | match | match, 14 parts, tally 3/4/3/3/4, small marks agree | identical |
| P1 | P1-14 (S2-03) | Ice cream, counting in 2s/5s | match | match, 13 parts, tally 2/3/3/3/2 | identical |
| P2 | P2-38 (S1-02) | Rocket, numbers to 1000 | match | match, 15 parts, tally 3/2/4/4/2 | identical |
| P2 | P2-39 (S1-17) | House, tables of 2 to 10 | match | match, 17 parts, tally 4/3/4/3/3 | identical |
| P2 | P2-40 (S2-20) | Butterfly, money | match | match, 14 parts, tally 2/4/2/2/4 | identical |
| P3 | P3-14 (S1-14) | Fish, tables of 6 to 9 | match | match, 17 parts, tally 4/4/4/2/2 | identical |
| P3 | P3-39 (S2-19) | House, changing units | match | match, 17 parts, tally 2/3/4/4/4 | identical |
| P3 | P3-40 (S2-20) | Butterfly, money | match | match, 14 parts, tally 2/4/4/2/2 | identical |
| P4 | P4-05 (S1-05) | Bus, numbers to 100 000 | match | match, 16 parts, tally 4/3/3/3/3 | identical |
| P4 | P4-11 (S1-11) | Lorry, larger multiplication | match | match, 15 parts, tally 3/4/3/2/3 | identical |
| P4 | P4-40 (S2-20) | Ferry, decimals | match | match, 12 parts, tally 4/2/2/2/2 | identical |
| P5 | P5-05 (S1-05) | Rocket, order of operations | match | match, 15 parts, tally 2/4/3/3/3 | identical |
| P5 | P5-22 (S2-02) | Butterfly, percentage | match | match, 14 parts, tally 2/2/2/4/4 | identical |

Tally order is yellow/red/blue/green/orange. The page numbers P1-01, 12, 14; P2-38, 39, 40; P3-14, 39, 40; P4-05, 11, 40; P5-05, 22 are the ones listed in each `school/pN/README.md` and `gen/pages_cbc.py` (14 pages in all; P1 has 3, P2 3, P3 3, P4 3, P5 2).

## What was compared, and how

For each page I took the pupil page from `P?_S?_Puzzles.pdf` and `P?_S?_Complete_Pack.pdf`, and the full-page "Answers:" entry (the last page of the key, with the solved picture) from `P?_S?_Answer_Key.pdf`.

1. **Text.** `pdftotext -layout` of the pupil page, the Complete Pack page and the key page. Every line of the pupil picture (every question, clue and label, excluding the instruction lines and the colour-key row) was found in the key page text; the only lines not found were instruction sentences, which the key does not repeat.
2. **Independent regeneration.** I imported each level's `gen/pages_cbc.py`, built the sheet (two different `PYTHONHASHSEED` values, output identical, so the builds are deterministic) and compared every region's question lines and solution lines with the tokens of the pupil PDF page and the key PDF page. Nothing was missing on either page, except glyph-spacing artefacts (the thin space in "25 356" and the fraction glyphs in P4-40 that pdftotext splits). So the PDFs contain exactly the questions and solutions of the code.
3. **Pictures.** I rendered the pupil page and the key page of each of the 14 pages (110 dpi) and compared them side by side, label by label and part by part: same picture, same parts in the same places, same small marks (triangle, square, star, plus, dot, moon).
4. **Hand colouring.** I worked every question on the pupil page myself, looked the answer up in the key row printed on the pupil page, and coloured the part (on paper, by colour name). I then compared with the colour printed in brackets in the key and counted the parts of each colour. In all 14 pages my colouring equals the key's colouring, my counts equal the key's tally, and my counts equal the "You should have: ..." sentence on the pupil page. On the pages with "parts in the same place on the left and on the right have the same colour" or "parts with the same small mark have the same colour" I checked the pairs; all agree (for example P1-12: both roof triangles red, both star parts green, three plus parts blue; P2-40: all seven left/right pairs equal).
5. **Complete Pack vs Puzzles.** Word-for-word text equality of the pupil page and a pixel difference at 70 dpi; no difference on any of the 14 pages, in either run.
6. **Latest PDFs.** Re-run at 21:50 on the working-tree PDFs (P4 and P5 rebuilt at 21:47 and 21:48). Key pages are pixel-identical to the committed ones on all 14 pages. Pupil pages changed only on P4-11, P4-40, P5-05 and P5-22, and only in the instruction sentences (P4: the "A number half way rounds up." line removed on the Lorry page; P5: instruction wording changed to "Colour the part, or write its letter (Y, R, B, G or O) if you have no crayon."); the questions are unchanged and still match the key and the code. Re-run the script below once the P3 to P6 builders have finished.

Small observations, not mismatches:
- On "Greatest/Smallest of three numbers" parts (P2-38, P2-40) the key prints the colour but does not underline the answer (the other parts underline it). The teacher has to pick the greatest or smallest from the three numbers. Low severity.
- P2-40 and P4-05 use colour keys of mixed units (35¢ in the key, $0.35 in a question). That is deliberate (conversion is the exercise) and the key agrees.

## Root cause analysis (P6 bug, and whether P1 to P5 share it)

There is no live mismatch in P1 to P5, so there is no root cause of a mismatch to report. The mechanism that produced the P6 bug exists in every level, though.

**The mechanism.** The answer-box size is a module global in the vendored library: `school/pN/cbc_vendor/layout.py:15` (`BOX_SIDE = 6.0`; P4 also `BOX_W` at line 15). `layout.fit()` and `layout.render()` read it (lines 48, 55, 121), and `sheet.make_sheet()` (`cbc_vendor/sheet.py`, `def make_sheet`) uses `fit()` to choose which question variant fits each region, consuming the random generator as it goes. A different `BOX_SIDE` therefore gives different questions, not just different box sizes. I confirmed this on P5-05: building the sheet with the default 6.0 instead of 9.0 changes 13 of the 15 questions.

Each level's `gen/pages_cbc.py` sets the size only for the duration of one call:
- P1: `page12()` sets `L.BOX_SIDE = 8.0` at `school/p1/gen/pages_cbc.py:141-144` (P1-01 and P1-14 use the library default 6.0).
- P2: `cbc_page()` sets 9.0, `school/p2/gen/pages_cbc.py:82-86`.
- P3: 12.0, `school/p3/gen/pages_cbc.py:82-86`.
- P4: 12.3 and `L.BOX_W = 17.5`, `school/p4/gen/pages_cbc.py:82-87`.
- P5: 9.0, `school/p5/gen/pages_cbc.py:82-86`.
- (P6: 11.0, `school/p6/gen/pages_cbc.py:83-87`.)

Inside that wrapper the code does `S.make_sheet(...)` (line 89/90, P1 line 83), builds the pupil SVG, `teacher_svg(sh)` (line 106 or 112/113) and the verification model from the same `sh`. So in P1 to P5 the key's label SVG (`P["teacher_svg"]`, printed by `render.py` at lines 361 to 367) is built in the same call, with the same box size, from the same sheet object as the pupil page. That is why they match.

**Where it breaks.** Any code that calls `make_sheet`, `L.fit` or `L.render` for one of these specs outside the wrapper (a second build of the key, a validator, a preview, a rebuild of just the key page) gets the library default (6.0, or P4's `BOX_W=None`) and silently different questions. P6 had exactly this, and its fix is visible in the vendored copy: `school/p6/cbc_vendor/layout.py:15` now has `BOX_SIDE = 11.0` as the default, so any build outside the wrapper agrees with the wrapper. P1 to P5 still have the default 6.0 at `cbc_vendor/layout.py:15` (P4 line 16) while their pages use 8 to 12.3.

**Shared by the other levels?** Yes, all of P1 to P5 share the mechanism (the global at `cbc_vendor/layout.py:15`, the try/finally wrapper in `gen/pages_cbc.py`, the `make_sheet` use of `fit`). `school/colour_by_code/layout.py:15` has the same global at 6.0 but nothing in that library sets another value. None of P1 to P5 triggers it today: `make_sheet` is called only from `gen/pages_cbc.py` (grep over `school/p[1-5]` of `make_sheet`, `import layout`, `import sheet` finds only that file), and `render.py` and `validate.py` use the strings and `P["sheet"]` already built. None of `school/p1` to `school/p5/validate.py` has the colour-page consistency check that `school/p6/validate.py:331-336` has ("every question printed on a colour page is printed in the key too"), so a future regression would not be caught in P1 to P5.

## Recommended fixes (not applied)

1. **Add the P6 check to P1 to P5 `validate.py`**: copy the block at `school/p6/validate.py:331-336` (questions from `data-t` on `out/S?_pupil.html` must appear in `out/S?_key.html`). Better, also compare `P["sheet"]` item lines with the PDF text, as I did, because the check on the HTML only sees strings.
2. **Remove the global-state hazard.** Either set the page's box size as the library default in each level's `cbc_vendor/layout.py:15` (P6's fix: P1 8.0/6.0, P2 9.0, P3 12.0, P4 12.3 plus `BOX_W = 17.5`, P5 9.0), or pass the size into `make_sheet`/`L.fit`/`L.render` explicitly. Setting the default is the smallest change and keeps today's PDFs byte-for-byte unchanged (P1 needs care: P1-01 and P1-14 use 6.0, P1-12 uses 8.0 and the thick-line variant at `cbc_vendor/layout.py:122`, so keep a per-page override there).
3. **Do not rebuild only the key page** for a colour page; always rebuild the whole booklet so pupil and key come from the same sheet object.
4. Optional: underline the answer on "Greatest/Smallest" parts in the key (P2-38, P2-40) so the teacher sees which number is meant.

## Re-running the comparison

The scripts are in the scratchpad (`.../scratchpad/w/final.py`, `chk2.py`, `dump.py`, `cmp.py`); they need only `pdftotext`, `pdftoppm`, Python with PIL, and each level's `gen/pages_cbc.py`. Run `python3 final.py <school dir> <out dir>` for text/tally/pixel checks and `python3 chk2.py <school dir>` after `dump.py N` for the regeneration check.
