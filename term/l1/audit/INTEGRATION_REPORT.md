# Level 1 term books: integration report (x10, spine, look-back, Toolbox Card)

23 Oct 2026 (night), branch `claude/great-fermi-1hv4vc`. Nothing pushed. Inputs: `X10_QUEST_HANDOFF.md`, `X10_TERM2_HANDOFF.md`, `X10_TERM34_HANDOFF.md`, `SPINE_TERM_DESIGN.md`, owner decisions of 23 Oct 2026 (night): LOOKBACK-RETIRE, ACCEPT-NOTE, CARD-BOOK1.

## What changed
1. **Stale references fixed** (lesson JSON, text only):
   - l08: Picture Equations is Term 2 Lesson 3 (was 9).
   - l12, l18: strips lessons now "Term 2 Lessons 8, 9 and 10" / "Lessons 9 and 10"; make-up pointer "before Term 2 Lesson 9".
   - l23, l24 (4 places), l25: $1 tokens come from Term 2 Lesson 9 (Find One First).
   - Rewind home items: l39 H5 (cup item) now tagged Term 2 Lesson 3 and is a verbatim copy of l13 H2; l40 H5 (5 pens $10) tagged Term 2 Lesson 9, copy of l19 H1; l33 H5 was the retired Doubles item, now a copy of l13 H2 (tag unchanged, Term 2 Lesson 3); l37 online items r1, r2 were Fill the Grid items, now copies of Calendar Detective c2, c5 (tag Term 3 Lesson 7). Verify scripts l24, l33, l37, l39, l40 updated (l24 reads the token page from l19).
   - Lesson numbers that were absolute numbers written as "Term N Lesson M" were turned into term-local numbers: l25 (Term 2 Lesson 2), l26 (5, 7), l27 (6, 1), l28 (3, 4, 6), l33 (Term 2 Lesson 1), l40 (6).
   - Lesson 7: the word "tool" (for take away / count up) is now "way" everywhere. Lesson 33 "the grid page is our tool" now "helper".
2. **spine_term.json** rows 10, 13, 19, 20, 27, 29, 30, 39, 40 now match the new lessons: 13 Picture Equations (Work backwards, also Act it out, role I), 19 Find One First (Draw it, also Make a table), 20 Choose Your Tool (choose), 27 Calendar Detective (Spot the pattern, also Act it out), 29 Spot the Mistake (Work backwards), 30 Tool Detectives (choose), 39 (choose, eight card names), 40 (choose). `tools_met` per term equals `b_quest.TERM_TOOLS` (4, 6, 7, 8 tools; Term 4 order differs only on the page).
3. **apply_spine_term.py --apply** run (46 files: 40 lessons, b_print, b_guide, b_deck, validate, schema, AUTHORING). Lessons 3, 6, 9 (and 10, where the tool is the lesson) got a written note instead of a spoken tool line (ACCEPT-NOTE). The old did-well / hardest / next look-back is gone (common look-back replaces it).
4. **validate.py**: template-leak check no longer flags a lesson title that is also a tool name ("Make a Table", lesson 28 vs the tool Make a table); this had produced 8 false FAILs in lessons 21 to 26 and 29.
5. **Books** rebuilt (colour and B&W). `print/make_term_books.py`: Book 1 contents page lists the Toolbox Card (row "Card ... in the pack" and a note) and the spec row gets `ships_with` (CARD-BOOK1). The card is a loose A5 card, not a bound page, so page counts do not change.
6. Docs: `docs/printing/quote_request.md` (counts, Book 4 Quest Log 4 pages, Toolbox Card paragraph), `docs/terms/level_1_year_plan.md` (applied banner and slot map).

## Validation
All 40 lessons: `build.sh NN` validate 0 FAIL (22 to 23 passes, 0 to 8 timing warnings, all "slow class over its part, buffer absorbs it"). Slow-class totals 76:36 to 90:00 of 90:00 (lesson 10 is 89:59 to 90:00, exactly full; lessons 3, 6, 9 are 89:50 to 89:56). Independent `verify/lNN_checks.py`: all 40 pass. Workbook pages as designed: 5 pages for 9, 23, 26, 38, 40; 7 for 2, 3, 13, 15, 24, 32; 8 for 31; 6 for the rest (13 is 7 because it holds two kit pages, 19 is 6 with the tokens page).

## Final page counts (colour; B&W identical, 1-bit 600 dpi)
| Book | Workbook (sheets, blank pages) | Key (tutor) | Home pack |
|---|---|---|---|
| 1 (T1 L1-5) | 46 (23, 12) | 22 | 12 |
| 2 (T1 L6-10) | 44 (22, 9) | 32 | 14 |
| 3 (T2 L1-5) | 46 (23, 12) | 22 | 12 |
| 4 (T2 L6-10) | 46 (23, 10) | 30 | 14 |
| 5 (T3 L1-5) | 42 (21, 10) | 22 | 12 |
| 6 (T3 L6-10) | 44 (22, 9) | 32 | 14 |
| 7 (T4 L1-5) | 48 (24, 13) | 22 | 12 |
| 8 (T4 L6-10) | 42 (21, 8) | 32 | 14 |

Before: workbooks 46/44/44/48/42/44/48/42, keys 22/30/22/28/22/30/22/30. Changes: Book 3 +2 (ten-frame and shape kit pages in lesson 13), Book 4 -2 (loses shape kit, gains tool-card kit, Quest Log 3 to 4 pages), Books 2 and 6 and 8 keys +2 (Quest Tutor Notes 9, 9 and 10 pages), Book 4 key +2. Quest Logs are 4 pages in Books 2, 4, 6, 8. Kit pages all sit on front pages with blank backs (checked by pixel test). Book 1 kit pages 9, 17, 19, 27, 29, 37, 45; Book 3: 9, 17, 25, 27 (ten-frame, shapes), 35, 43, 45; Book 4: 9, 17, 25, 33 (Find One First tokens), 41 (tool cards); Book 6: 15, 23, 31, 39 (calendar cards at lesson 7, tool cards at lesson 30 within the lesson); Book 8: 9, 17, 31 (toolbox cards at lesson 9).
`outputs/print/term/term_books_spec.json` now holds all 24 rows (the tracked file held only Books 5 to 8). `outputs/print/bw/bw_spec.json` holds the 24 term rows (the tracked one held Books 5 and 6 only; holiday rows are written by the holiday job).

## Warnings left (not fixed)
- Deck layout warnings (build.sh exit code 1, outputs built): lesson 9 slide s-m4, lessons 21, 25 slide s-ws2, lessons 23, 26 slide s-ws1. Present before this work (confirmed by building HEAD in a scratch worktree for 9 and 21).
- Timing warnings: slow-class overrun of single parts in many lessons (buffer absorbs); lesson 10 totals exactly 90:00 slow class. First trial lesson should time the Quest.
- Lesson 3, 6, 9, 10: written note only, no spoken tool line.
- Choose lessons (10, 20, 30, 40) show the tool chip as icons with tick boxes but without names on the workbook page; the names are on the Toolbox Card and in the Quest tool row.
- Term 4 look-back and Quest pills carry eight icons at about 7 mm; B&W legibility spot-checked at 300 dpi crops (Book 2 four icons, Book 8 eight icons): all icons readable; the dotted circle of Spot the pattern and the small dots of List every way are the weakest, still distinguishable.

## Items for an independent audit
1. Read the chip and look-back on page 1 and last page of lessons 7, 13, 19, 20, 27, 29, 30, 39, 40 (new rows) in colour and B&W.
2. Confirm spine choices for 13 (Work backwards, Act it out), 19 (Draw it, Make a table), 27 (Spot the pattern, Act it out) with the owner; 13's old guess-and-check feel is not allowed in Term 2 (not yet met).
3. Check the three rewrites of rewind items (l33 H5, l37 r1 and r2) and that home answers match.
4. Check the term-local conversions of "Term N Lesson M" pointers in l25 to l28, l33, l40 against the real slot map.
5. Lesson 33 and 14, 18 still use the word "tool" for other meanings (MOE "testing tool", "choosing a tool" in the Term 2 parent line): decide whether acceptable.
6. Quest tutor notes 9 to 10 pages with loose page breaks; key book layout.
7. Toolbox Card is loose and not in any PDF book: confirm the printer pack includes `outputs/kit/Math_Inquirers_Toolbox_Card_A_6-8_PRINT_BW.pdf` with Book 1 (one per child).
8. `term/l1/audit/retired_L13_doubles` and old audits for 13, 19, 20 still carry "re-audit pending" banners: workbook, home and wording audits for 13, 19, 20, 27, 30 are not re-run.
9. Dated tables in `docs/terms/level_1_year_plan.md`, `l1_term2_preflight.md`, `l1_term3_term4_preflight.md` and `term_review.md` still list old slots (banner added only to the year plan).

## B&W
`print/make_bw_print.py --only L1_T` then `check_bw.py`: all 24 term PDFs ok, max non-grey 0.00000, every embedded image 1-bit, page counts equal the colour books. (The converter's worker pool stalled twice in this sandbox; the run was resumed with `--resume` and Book 8 converted separately; `bw_spec.json` was then rebuilt from the 24 files, so `pale_tint_dropped_max` is null for rows converted in an earlier partial run.)
