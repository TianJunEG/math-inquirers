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

## Level 4 (holiday P4), 23 Oct 2026

Rolled out to Level 4 per the commands above. Nothing republished.

What changed
- `levels/spine_deco.py`: `'4'` added to `LEVELS_ON` (all six levels are now on).
- Budget (D5): `rebuild/p4_budget.py` `DUR`: `look` 3.5 to 2.5 and `talk` +1 in all 10 lessons; slide windows: `talk` ends 1 minute later, `exit` starts and ends 1 minute later, `reflect` starts at 87.5 (Lesson 10: talk 76-80.5, exit 80.5-85, reflect 85-87.5, end 87.5-90). `p4/budget.json` regenerated. `rebuild/p4_fix.py` `finish()` now rewrites the talk and exit pills and the "Minutes a to b." note from the budget (the gen_p4l* scripts still hold the old hard-coded pills, so this keeps them honest), adds a "TOOL MINUTE" speaker note to the talk slide and updates the Time plan sentence. The decks were rebuilt with `gen_p4l1..10.py` then `restyle.py` (regenerating from gen reproduced the old decks exactly apart from the deck.json timestamp, which was reverted).
- Decks: restyle run twice, the second changed 0 files (also 0 on a further run). Slide counts unchanged (27, 26, 25, 28, 28, 26, 25, 26, 26, 28). Title chip, talk badge, rebuilt `reflect` (Lesson 10 keeps `end` last). Mi still only on title, break and last slide. No overflow at 1920 by 1080 (measured: title, talk, exit, break, reflect, end for all 10), no duplicate `data-spine` elements, one pill per slide, no "Something I did well", no positive "hold to the camera" text.
- Talk badge (Levels 4-6, first real test): works. Bottom-left pill, 70 px, clear of the cards above (checked all 10 decks for overlap) and of the footer text. No fix needed.
- Tutor data: `tutor/build_data.py 4`: part minutes sum to 90 in all 10 lessons; Talk 4.5 (5 in L4, L7, L8), Looking back 2.5.
- Workbook `p4/workbook_html.js`: `hdr(..., first)`, `LEVEL = 4`, `COMPACT = {5, 8, 9, 10}`, `reflectBox` returns `SP.lookback(4)`. The full card pushed a question to an extra page in lessons 5, 8, 9 and 10 (66 became 70 pages); compact header chips for 5, 8, 9 and a new compact one-row Lesson 10 "choose" card (`levels/spine_wb.js`, `card(level, n, true)` for a choose row, sits beside the title) bring it back to 66 pages with identical per-lesson page counts. Note: another agent also added a compact-choose branch to `spine_wb.js` after mine; mine comes first so theirs is dead code and can be deleted.
- Guide `p4/guide.js`: `SG`, Opening SAY/DO, Talk tool question (band B wording), look-back script with the 90 second timer, minutes table text, "Toolbox and look-back" front-matter section. Guide 102 to 103 pages. Segment minutes come from `budget.json` (Looking back 2.5, Talk 4.5 or 5). Weekly zip rebuilt. Not run: `parent_pack_level.py`, `levels/scheme.py`.
- Print: `outputs/print/print_spec.json` unchanged for Level 4 (66 source pages, 76 print pages, 38 sheets, 10 blank, cut-outs 58-66: the cut-out pages remain single-sided with blank backs and no content page sits behind them). Colour print PDF rebuilt with `make_print_pdfs.build(4)` only.

Level 4 lesson issues for the owner (NOT changed): L4.9 (Data Detectives, tables and line graphs) duplicates the content of term lesson 4.1; L4.7 (Area Architects II) opens like L4.1 (as found in the pedagogy review; not re-checked here). Also: the Level 4 time plan sentence says Talk time has "one minute of pair talk"; the extra minute is spent on the tool question, which has not been stopwatch-timed.

## Levels 2-3 (rolled out 23 Oct 2026)

Done exactly as the commands above, no republish. `LEVELS_ON` now includes '2' and '3' (other levels add their own).

- Decks (`split/p2l1..10`, `split/p3l1..10`): `restyle.py` run twice, second run 0 files (re-checked after a later edit: 0). Each deck +1 slide (`<key>-tool` after title), title chip, rebuilt `reflect`. Mi only on title, break and last slide; no duplicate ids, pills or chips; no overflow at 1920 by 1080 (Level 3 reflect reports scrollHeight 1082 only because of the section's bottom padding; nothing is drawn past 1016 px); no "paper to the camera" text; "Something I did well" gone from decks, workbooks and guides. `tutor/build_data.py 2` and `3`: all 20 lessons still total 90 min; `tool` maps to Opening, `reflect` to Looking back.
- Deviation: Level 2 look-back timer is 90 s (spec timing table), not the band-A 120 s. Added `lookback.timer_by_level {"2": 90}` to `spine.json`, read by `spine_deco.py` and `spine_guide.js` (Level 1 unchanged, 0 files changed).
- Workbooks: `hdr` gets a `first` flag (Level 2: new last argument; Level 3: fourth argument), `LEVEL`, `COMPACT`, and the look-back box replaces `reflect` (p2) / `lookBack` (p3). `COMPACT`: Level 2 {4}, Level 3 {3, 5, 7, 10}. `levels/spine_wb.js` `card(level, n, true)` now also returns a one-line slim icon row for a "Choose" lesson (used by Level 3 Lesson 10, whose first page had no slack). Compact lessons also get a no-wrap lesson badge. Page counts: Level 3 unchanged (58 source pages). Level 2 went 66 to 62 source pages: no lesson gained a page, but Lessons 6-9 each lost one because their first pages reflow tighter than before (this reflow is deterministic and was checked by eye; the old PDF had wasted half pages). Print: Level 2 74 to 70 pages (37 to 35 sheets, 8 blank backs, cut-outs at 55-62), Level 3 64 (32 sheets) unchanged; `print_spec.json` and `docs/printing/quote_request.md` updated (Level 2 row).
- Guides: `SG` require, Opening SAY/DO, Talk ASK row, look-back SAY/DO, new "Toolbox and look-back" front-matter section in `p2/guide.js` and `p3/guide.js`. Level 2 look-back line adds "That is what we did in check together" (D4). Page counts unchanged (112, 104). Tutor guide PDFs, weekly zips and weekly-dose PDFs rebuilt.
- B&W: `make_bw_print.py --only P2_Workbook` / `P3_Workbook`; `check_bw.py` ok for both (non-grey 0; light-tint cells 0.140 and 0.147). `bw_spec.json` is merged by hand because `--only` overwrites it. Viewed: 12 decks (title, tool, look-back; Level 2 and 3 lessons 1, 3, 4, 6, 8, 10 at laptop size), workbook first pages (L2: 1, 4, 10; L3: 1, 3, 10), look-back pages, a guide page each, one B&W print page per level. Contact sheets: `docs/pedagogy/spine_samples/level2.png`, `level3.png`.
- Not done (as for Level 1): `levels/scheme.py` sentence, the A5 kit card, docx workbook builder.

## Levels 5-6 (holiday P5 and P6), 23 Oct 2026

Rolled out per the commands above. Nothing republished.

What `l6s` is: `split/l6s` is the 60-minute trial deck for LEVEL 1 lesson 6 (the "Lesson 6 Trial 60 min" pilot, `hp/Math_Inquirers_Lesson6_Trial_60min.docx`), not a Level 6 deck. `spine_deco.key_level` does not match its name, so restyle never touches it (it has no tool slide, chip or new look-back), and it stays out of the republish list as the spec says. Level 6 decks are `split/p6l1..p6l10`; `split/l6` is Level 1 lesson 6.

What changed
- `levels/spine_deco.py`: `'5'`, `'6'` added to `LEVELS_ON`. New small change for band C (Levels 5-6): the look-back slide uses 40 px prompts and 14 px row padding (46 and 24 for bands A and B, unchanged) and a shorter answer line. At 46 px the third prompt ran to three lines and the card overlapped the footer line on every Level 5-6 deck (measured at 1920 by 1080 with the real fonts: card bottom 1020 vs footer at 1000; now the card ends at about 880). This was the "audit found Mi touching the notice" slide: the old yellow notice box is gone, and Mi (right 1783 to 1876) is clear of the card (right edge 1730) on all 20 look-back slides.
- `levels/spine.json`: `lookback.timer_by_level["5"] = 90` (spec: Level 5 timer 90 s; Level 6 stays at the band C default 75 s).
- Decks: `restyle.py` on `split/p5l1..10` and `split/p6l1..10`, twice; the second run changed 0 files (checked again after the band C change). Slide counts unchanged (badge, not a new slide). Per deck: one title chip, one talk badge, rebuilt `reflect`. Level 6 Lesson 10 has no `talk` slide (it has `showcase`), so it gets the chip (all eight icons, "You choose") and the look-back but no badge; the guide asks the "Which tool did you choose, and why?" question in its look-back. Mi only on title, break and the last slide (`reflect`, or `end` in Lesson 10). No duplicate ids, one time pill per slide, no "hold paper to the camera". Rendered all title, talk (or showcase), reflect slides of both levels (60) at 1920 by 1080: no overflow, no text under Mi.
- Talk badge (Levels 4-6): works at Levels 5 and 6 (bottom-left pill, clear of the cards and the footer text).
- Tutor data (`tutor/build_data.py 5`, `6`): part minutes sum to 90 in all 20 lessons; `reflect` maps to the Exit/Looking back part, `talk` to Talk time.
- Workbooks: `p5/workbook_html.js` (`hdr(..., first)`, `LEVEL = 5`, `COMPACT = {}`, `reflect` = `SP.lookback(5)`), `p6/workbook_html.js` (same; `COMPACT = {1, 2, 3, 6, 7, 8, 9}`: the full card pushed the first page over in those lessons; the Start-here pointer line moves under the name line when the card sits beside the title). Page counts unchanged: 57 and 55 source pages, identical per lesson.
- IMPORTANT, Level 5 print scale: the old Level 5 reflection box had lines wider than the page, so Chrome printed the whole document shrunk to 794/850 and every page was laid out for that scale. The new look-back box fits the page, so without that shrink the first pages of every lesson overflowed (57 became 80 pages). `p5/wb_pdf.py` now adds a hidden 850 px spacer to keep exactly the same scale. Do not remove it.
- `levels/spine_wb.js`: the icon SVGs are collapsed to one line (`wb_pdf.py` in p2-p6 groups the body line by line; multi-line SVG inside a card broke the question boxes).
- Guides: `p5/guide.js` and `p6/guide.js`: `SG` require, Opening SAY/DO (Lesson 1 adds the kit line), Talk ASK row, look-back SAY/DO (Level 5 adds "That is what we did in check together", D4; Level 6 does not), band C "Toolbox and look-back" section (also the old "Something I did well" sentence in the Level 5 front matter). Guides 108 to 113 pages (Level 5) and 106 to 107 (Level 6). Segment minutes are unchanged (they come from `budget.json`). Weekly zips, weekly dose PDFs and parent packs rebuilt.
- Print: `make_print_pdfs.build(5)` and `build(6)`: identical to `print_spec.json` (62 and 58 print pages, 31 and 29 sheets, 5 and 3 blank, cut-outs from page 53 on), so the spec is unchanged. B&W: `make_bw_print.py --only P5_Workbook` and `P6_Workbook`, `check_bw.py` ok (Level 5: non-grey 0, light-tint cells 0.153). `bw_spec.json` restored after each run (the tool overwrites it).
- Viewed: decks p5l1-10 and p6l1-10 title, talk and look-back (contact sheets `docs/pedagogy/spine_samples/level5.png`, `level6.png`), workbook pages (first page of lessons 1, 3, 10; look-back page of lessons 1 and 10; both levels), guide pages (toolbox section, a lesson opening), one B&W print page per level.
- Not done: `levels/scheme.py` sentence, A5 kit card, docx workbook builder; the Level 5 `data.js` `scriptReflect` text (old "Something I did well" wording) is now unused by the guide.

## Tool re-mapping (audit item M1), 23 Oct 2026

Owner decision "fix the 5 tool mappings". Only `lessons.<key>.main` and `.also` in `levels/spine.json` were changed (single source); everything else was regenerated by the existing idempotent steps. Nothing was republished to Artifact URLs; the 60 deck URLs need the republish only for these five decks (`split/l4`, `split/l7`, `split/p3l9`, `split/p5l1`, `split/p6l9`) if the owner wants it, and the other agent's republish should be re-run for them.

| Lesson | Old tool | New tool (also) | Reason (from the lesson content) |
|---|---|---|---|
| L1.4 Pattern Inquiry | Try something simpler | Spot the pattern (also: Try something simpler) | Q1-Q6 are "find the 8th, 10th, 12th, 30th item of a repeating pattern"; only Q7 builds small cases. Swapped main and also. |
| L1.7 Shape Safari | Act it out | Make a table (also: List every way) | Nothing is acted out; Q2 is a sides-and-corners table, and shapes are counted one kind at a time in order. |
| L3.9 Measure and Money Masters | Draw it | Make a table (also: Draw it) | Unit-conversion trick table, the $20 shopping price table and bus/time tables are the main move; the time line is a secondary drawing, so Draw it stays as "also". |
| L5.1 Million Puzzles | List every way | Guess and check (also: List every way) | "Closest to a target, test both sides" and the digit riddle ("check every clue") are guess, test, adjust; listing all 7-digit numbers is only the Think harder items. |
| L6.9 Data Detectives | Draw it | Work backwards (also: Draw it) | Missing value from a mean (total first, then take away), "what must the 4th score be"; the balance/levelling picture is the secondary tool. |

The old `hint` text on L1.4 ("in content (build 1, 2, 3)") and L5.1 was left as it was (it is not used by any builder). The "Try something simpler" lessons are now only L5.9 and L6.5 as main (L1.4 keeps it as "also"); the tool counts in the spec table no longer match exactly (pattern 8, table 7, guess 3, simpler 2, actout 4, draw 10, list 12, backwards 8, choose 6).

Files changed
- Source: `levels/spine.json`.
- Decks: `split/l4`, `split/l7`, `split/p3l9`, `split/p5l1`, `split/p6l9` (title chip; tool slide at L1.4, L1.7, L3.9; talk badge at L5.1, L6.9). The `reflect` slides are unchanged (they carry no tool name). `restyle.py` run twice: 2 files per deck, then 0.
- Tutor data: `tutor/data/p1l4`, `p1l7`, `p3l9`, `p5l1`, `p6l9` (`.public.json` and `.notes.json`). Minutes still sum to 90 for all five.
- Workbooks (whole-level rebuild, only the five Start-here pages differ in content): `hp/` and `p3`, `p5`, `p6` `Student_Workbook_Designed.pdf` (+ `workbook_body.html` / `workbook_full.html` for p3, p5, p6) and `outputs/workbook/..._P1_...Designed.pdf`. Source page counts unchanged (58, 58, 57, 55, all per-lesson counts the same); the print files are unchanged in size (64, 64, 62, 58 pages, all even) so `print_spec.json` is unchanged.
- Guides: `hp/Math_Inquirers_P1_Tutor_Guide.{pdf,html}`, `hp/P1_Holiday_Program_Guide.docx`, `outputs/designed/Math_Inquirers_P1_Tutor_Guide.{pdf,docx}`, and the same three files in `p3`, `p5`, `p6`. Page counts unchanged (94, 104, 113, 107).
- Weekly zips: `outputs/designed/Math_Inquirers_Weekly_PDFs.zip`, `p3/p5/p6 ..._Weekly_PDFs.zip`.
- Print: colour `outputs/print/Math_Inquirers_P1/P3/P5/P6_Workbook_PRINT.pdf`; B&W files in `outputs/print/bw/` (git-ignored), `check_bw.py` result below.
- Not rebuilt: parent packs (they do not name the tool), `levels/scheme.py`, docx workbook builder.

Other medium audit items
- M2 fixed: `hp/guide.js` timing-table look-back sentence no longer lists "Something I did well", "The hardest part was ..." or "What helped me"; it now describes the three questions, the "Tool I used" row and the stuck/pass footer. Level 1 guide rebuilt (94 pages, 0 hits for the retired wording).
- M4: see the B&W line below.
