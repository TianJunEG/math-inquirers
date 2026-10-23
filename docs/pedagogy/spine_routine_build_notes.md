# Spine routine: stage A build notes (Level 1 pilot), 23 Oct 2026

Implements stage A of `docs/pedagogy/spine_routine_spec.md`: the shared code and data, applied to Level 1 only (holiday lessons 1-10: decks `split/l1..l10`, workbook, tutor guide, print files). Nothing was republished to Artifact URLs. Term, school, extension, website and portal were not touched.

## What was built

- `levels/spine_icons/*.svg` (8 icons: pattern, list, draw, table, backwards, guess, simpler, actout): 64 by 64, one 3-unit stroke, stroke only (the "filled" dots are drawn with strokes only), `currentColor`, no grey, no text, no Mi. Viewed at 200, 46, 38 and 20 px and in the B&W print PDF at 10 mm: all legible.
- `levels/spine.json`: single data file (eight tools with band A/B/C definitions, band per level, look-back prompts and timers, guide script lines, card labels, and all 60 lesson rows parsed from the spec table: main tool, "also" tools, hint note). Counts match the spec (13 list, 12 draw, 7 pattern, 7 backwards, 6 choose, 5 actout, 5 table, 3 simpler, 2 guess).
- `levels/spine_icons.py` (inline SVG + data loader), `levels/spine_wb.js` (`card`, `lookback`), `levels/spine_guide.js` (`info`).
- `levels/spine_deco.py`: idempotent deck post-pass, wired into `levels/restyle.py` just before `mi_deco`. Title-slide "TODAY'S TOOL" chip (marked `data-spine`, removed and re-added each run), `<key>-tool` "Strategy of the day" slide after the title at Levels 1-3 (written whole, id added to `deck.json` only if absent, pill copied from the title so `tutor/build_data.py` maps it to Opening), talk badge at Levels 4-6 (coded, NOT yet tested on a real deck), `reflect` slide rebuilt whole (three prompts in band wording, tool ticks, still stuck/pass, timer label, new speaker note). Added speaker-note text starts with `SPINE:`. Existing Mi image on the reflect slide is kept and `mi_deco` still re-places it. `LEVELS_ON = {'1'}` unless env `SPINE_ALL=1`.
- Workbook: `hp/workbook_html.js` (`hdr` adds the card on each lesson's "Start here" page only; `refl` now returns the new Look back box). Guide: `hp/guide.js` (Opening SAY/DO, Talk ASK row, look-back script replaced, new "Toolbox and look-back" front-matter section).

## Results (Level 1)

- Decks: all 10 gain a tool slide (slide count +1), titles get the chip, reflect rebuilt. Two further `restyle.py` runs changed 0 files (checked over 4 runs). Mi is still only on title, break and the last slide (Lesson 10 keeps its existing `end` trophy). No overflow at 1920 by 1080 (30 slides measured). No new "camera" text. "Something I did well" is gone from decks and the workbook. Tutor data rebuilt (`tutor/build_data.py 1`): part minutes still sum to 90; `tool` maps to Opening, `reflect` to Look-back.
- Workbook: 58 source pages unchanged (64 print pages, 32 sheets, 6 blank, same cut-out pages, so `outputs/print/print_spec.json` is unchanged). B&W file rebuilt (`outputs/print/bw/`, git-ignored); `print/check_bw.py` ok: non-grey 0, light-tint cells 0.133 (below the fail level).
- Guide: 93 to 94 pages. Segment minutes unchanged (budget untouched).
- Viewed: decks l1, l2, l3, l4, l5, l6, l8, l9, l10 (title, tool, look-back; laptop-size renders), workbook pages (lesson 1, 2, 3, 6, 7, 10 first pages; lesson 1 and 6 look-back page), the B&W print pages, guide page for lesson 4.

## Assumed owner decisions (spec recommended options; the owner can change any)

- D1: the eight names and the A/B/C definitions exactly as in the spec (edit `levels/spine.json`).
- D2: main/also mapping as in the spec (L1.4, L5.9, L6.5 as the three "Try something simpler" lessons). The 17 extra "Try something simpler" hint lines are listed in `spine.json` (`hint`) but NOT added to the guide hint ladders in stage A.
- D3: retire "Something I did well / hardest part / next time"; keep the "Tool I used" row and "still stuck / pass" footer. (GAPS `hard` data is now unused by the workbook.)
- D4: no check-together slot added to Levels 1, 3, 4, 6.
- D5: Level 4 moves 1 minute from Looking back to Talk time (not done yet; Level 4 is not in stage A).
- D6: full "Strategy of the day" slide at Levels 1-3, badge only at Levels 4-6.
- D7: the A5 toolbox card is assumed to go in the Inquirer Kit. It has NOT been built. The Lesson 1 tool slide and guide say "Eight tools: see your Inquirer Kit card"; if the card is not made, set `kit_line` in `spine.json` to "" and rerun.

## Deviations from the spec and problems found

1. Card size: the 62 by 17 mm card cannot hold label, name, definition and "also" line at 9 pt or larger. Built 96 mm wide, about 19 mm high, beside the title (long titles drop from 38 to 29 px). Lesson 10 uses a full-width row of eight icons with "I chose" boxes.
2. Pages too full: first pages of lessons 3, 6 and 7 had no slack (the card pushed a question box to an extra page). Those three use the spec's fallback in compact form: a header-row chip (TOOL OF THE DAY, icon, name, tick box, no definition). Set `COMPACT` in `hp/workbook_html.js`. For Levels 2-6 expect the same on dense lessons; check page counts after the build.
3. Look back box: same width as the old box and shorter. Tool icons in it have no names (icon + tick only), to keep the height.
4. Opening is only 2 minutes in Lessons 2-10: the tool line is about 20 s. No stopwatch test was done.
5. Level 1 Lesson 1 title pill reads "2-4 MIN" (existing); the tool slide copies it.
6. The sandbox auto-checkpoint commit `d785506` already contains most of the deck and code changes; the remaining files were committed separately.
7. Not done: `levels/scheme.py` sentence, the parent-pack text, the weekly zip for other levels, the `hp/workbook.js` docx builder (not in the shipped pipeline), `outputs/workbook/*_Student_Workbook.docx`. The Level 1 weekly zip `outputs/designed/Math_Inquirers_Weekly_PDFs.zip` was rebuilt.

## Commands to apply to Levels 2-6 (N = 2..6)

1. Add `'N'` to `LEVELS_ON` in `levels/spine_deco.py` (or run with `SPINE_ALL=1`).
2. Decks: `python3 levels/restyle.py $(for i in 1 2 3 4 5 6 7 8 9 10; do echo split/pNl$i; done)` twice; the second run must report 0. Then `python3 tutor/build_data.py N`. Level 4: first edit `DUR` in `rebuild/p4_budget.py` (look-back 3.5 to 2.5, talk +1), rerun, then `rebuild/p4_fix.py`. Test the Levels 4-6 talk badge on a real deck before trusting it.
3. Workbook: copy the `hdr`, `LEVEL`, `COMPACT` and `refl` edits from `hp/workbook_html.js` into `pN/workbook_html.js` (spec section 4 gives the line numbers; set `LEVEL = N`; the new box replaces `reflect`, `lookBack` or `reflectBox`). Then `cd pN && node workbook_html.js && python3 wb_pdf.py`; compare page counts with `outputs/print/print_spec.json`; add lesson numbers to `COMPACT` for any lesson that gains a page.
4. Guide: copy the `SG`, Opening, Talk, look-back and front-matter edits from `hp/guide.js` into `pN/guide.js` (use `SG.info(N, l.n)`), then `node guide.js` and the `docx2pdf_designed.py` line in `levels/build_level.sh`, then `weekly_level.py` and `parent_pack_level.py`.
5. Print: `python3 -c "import sys; sys.path.insert(0,'print'); import make_print_pdfs as m; print(m.build(N))"` (or the whole script), update `outputs/print/print_spec.json` if counts change, then `python3 print/make_bw_print.py --only P<N>_Workbook` (this overwrites `bw_spec.json` with only the matched rows: back it up and merge) and `python3 print/check_bw.py outputs/print/bw/Math_Inquirers_P<N>_Workbook_PRINT.pdf`.
6. Republish decks only after the owner approves, one at a time (spec section 4).

## Files changed

New: `levels/spine.json`, `levels/spine_icons/*.svg`, `levels/spine_icons.py`, `levels/spine_wb.js`, `levels/spine_guide.js`, `levels/spine_deco.py`, this file.
Edited: `levels/restyle.py`, `hp/workbook_html.js`, `hp/guide.js`.
Regenerated: `split/l1..l10/project/*` (title, reflect, new tool, deck.json), `tutor/data/p1l*.json`, `hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf`, `hp/Math_Inquirers_P1_Tutor_Guide.{pdf,html}`, `hp/P1_Holiday_Program_Guide.docx`, their copies in `outputs/workbook` and `outputs/designed`, `outputs/designed/Math_Inquirers_Weekly_PDFs.zip`, `outputs/print/Math_Inquirers_P1_Workbook_PRINT.pdf`, `outputs/print/bw/Math_Inquirers_P1_Workbook_PRINT.pdf` (ignored by git).
