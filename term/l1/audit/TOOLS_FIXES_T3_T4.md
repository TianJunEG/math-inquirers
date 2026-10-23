# Shared-tool fixes for the Term 3 and Term 4 audits

Scope: `term/l1/tools/*` and `term/l1/runner/practice.js` (the online runner). `print/` and `school/` untouched. No lesson JSON edited, no book rebuilt.
Sources: `FINAL_FIXES_T3.md`, `FIXES_T3_L21` to `L30`, `AUDIT_T4_L31_35.md`, `AUDIT_T4_L36_40.md`.
Check: `validate.py NN --no-built` gives 0 FAIL for lessons 1 to 40. Two lesson verify scripts that pinned old drawing details were adjusted (see "Verify scripts").
Looked at after a rebuild: L11, L21, L24, L31, L34, L36 (workbook, kit pages, deck and practice where relevant).

Status: FIXED / PARTLY / NOT FIXED (with the reason).

## 1. Guide
| Defect | Status |
|---|---|
| "papers to the camera 30 s" in the timing line (`b_guide.py`) | FIXED. The line now reads "... 20 s answers. Nobody holds paper up to the camera." Generated only in one place; every guide needs a rebuild to show it. |

## 2. Kit shapes
| Defect | Status |
|---|---|
| `fold_shapes` ignored `d_mm` (pieces 28 mm) | FIXED. `d_mm` is honoured (spec key `d_mm`, default 88 mm = "about 9 cm"; 95 also works: the kit then prints 108 % wide and is centred, because two 95 mm shapes need 196 mm). Circles and squares are really that size. |
| Long rectangles printed as 4 columns | FIXED. Each is `d_mm` by `d_mm / 2` and a 4 by 2 grid (3 + 1 grey lines, 1.8 px, readable in black and white). |
| 10 pieces do not fit one page at 9 cm | FIXED by paging: the kit now runs over 3 printed pages (circles, squares, rectangles). `b_print.kit_pages` prints one page per kit page with "(page n of 3)" in the title; `common.kit_pages_total` and the validator count them. Lesson text that says "page 6" for the kit still resolves; the lesson owner must say "pages 6 to 8" where it matters (book plan: L31 has 8 workbook pages). |
| `fold_punch` ignored size | FIXED. Drawing size is `draw` (default 150); `size` stays a page percentage. |
| Kit pieces and mats at the size the lessons say | FIXED for: clock faces 80 mm, hour hands 24 mm, minute hands 36 mm; coins 20 to 26 mm, notes about 50 by 25 mm (3 per row, 13 notes fit one page); tiles 22 mm, mats 24 mm cells; price tags 54 by 44 mm; event cards 38 by 36 mm, mat boxes 85 by 100 mm; strips 60 by 8 mm; mistake cards 85 by 16 mm; fold shapes as above. Every figs3 kit now prints at a stated page width, so 1 mm is exact (`kit_pct`, `kit_unit`). |
| `cards` kit (L34 four squares, 3 mm gaps, no centre mark) | NOT FIXED. It is the generic Term 1 and 2 `cards_kit` in `svg.py`, shared with 20 lessons; changing it changes built Term 1 and 2 kits. Use `fold_shapes` (squares only) in a later lesson edit, or ask for a centre-mark option. |

## 3. Kit pages
| Defect | Status |
|---|---|
| Clock kit too small, hands longer than face radius, no centre dot, cut lines 2.5 mm apart, "a hour", clipped line, heading | FIXED. 80 mm faces (numerals, ticks), hands with a dot at the pivot end, 6 mm gaps, "an hour" gone (new wording: "Lay an hour hand and a minute hand ..."), no clipped text, heading "Cut out 2 clock faces and 6 hands: 8 pieces in all." |
| Event-card mat too small, headings cut, "a.m." with full stops, gaps 3.4 mm | FIXED. Boxes 85 by 100 mm, headings "am (night and morning)" and "pm (afternoon and evening)" in full, cards 38 by 36 mm with 6 mm gaps, label wraps to two lines (no `[:12]`). |
| 4 by 4 mat clipped (grid tiles) | FIXED. Mats 3 by 3 and 4 by 4 side by side, 24 mm cells, both fully on the page. |
| Tile cut lines too close | FIXED. 22 mm tiles, 6 mm gaps, centred. |
| Price tags: small, 6 mm gaps, centring | FIXED. 54 by 44 mm, 6 mm gaps, grid centred, 4 rows. |
| Play money: small pieces, narrow gaps | FIXED. See sizes above; 6 mm gaps. Coin page is now about 60 % full (was 35 %). |
| Stick strips 6 mm, gaps 3.7 mm | FIXED. 8 mm strips, 6 mm gaps. |
| Mistake cards gaps 3.3 to 4.3 mm, pale mat labels | FIXED. 6 mm gaps, mat labels in navy. |
| Calendar day cards, shape pieces, pair cards, tool cards: gaps | FIXED. All 6 mm. Tool card label "Work backwards" now shrinks to fit. |
| `shapes2d` size is both drawing size and page percentage | FIXED. New `draw` key is the drawing size; `size` is only the page percentage. For old lessons that gave a number of 60 or more in `size` and no `draw`, the drawing size is unchanged (no layout shift). |
| Grid page: three route grids in one unlabelled row (L33) | FIXED. Each grid has a frame and a number ("Grid 1", "Copy grid 1"). |
| Graph mat: stray tally-like bars under the mat (L37) | FIXED (bars removed). The mat is still 5 columns by 8 rows: its orientation (M4) is a lesson-data decision, NOT FIXED here. |
| "We use them again" printed for every kit | FIXED. Printed only for kits a later lesson reuses (clock kit, play money, price tags: `figs3.KIT_REUSED`, or a kit key `reused: true/false`). For Term 3 and 4 lessons every other kit, including the `cards` kit, now omits it. Term 1 and 2 kits keep the old sentence. |
| Kit-note sentence in Term 1 and 2 | Unchanged on purpose. |

## 4. Figures
| Defect | Status |
|---|---|
| Clock: minute hand covers its numeral | FIXED. With numerals the minute hand stops just inside the numeral ring (54 units, numerals at 71), hour hand 36; numerals are drawn after the hands with a white halo; ticks shortened. Without numerals (`labels: none`) the long hands are kept. |
| Money: one coin scale, show cents | FIXED. Every money picture has the same 620-unit canvas and one coin size table (so a coin is the same size in every picture), rows wrap, coins print "5¢" ... "50¢". `size` s, m, l still shrink it. Existing pictures with `size` now print larger than before; lesson owners may want fewer coins per row. |
| Table icons about 9 mm | FIXED. Rows that hold pictures are 112 units tall and icons up to 96 units, about 14 mm on a 137 mm table when the column allows. Lessons using icon tables: 20, 37, 39 (check page fill after rebuild). |
| Picture graph pictures larger | FIXED. Pictures are `cell * 0.9`, the cell is chosen to keep the figure about 640 units wide (up to 76), label column fitted to the longest label. Lessons 37, 38, 40. |
| Network letters bigger | FIXED. Node radius 24 with letters of about 27 units when labels are present. |
| Stick pictures merge into single lines | FIXED. Each stick is pulled in at both ends and has a joint dot, so collinear sticks are visibly separate; default side 80 (taller picture). Lessons 28, 30. |
| Panel cannot draw a dark shadow | FIXED. Tile key `shadow: true` draws a solid dark silhouette. |
| `pair_cards` icons only or text only | FIXED. A face may be mixed: `"icon:apple+3"`, `["icon:apple","3"]` or `{"icon":..,"text":..}`. |
| Network, cube, fold figures cannot take A/B/C letters | FIXED. `tag: "A"` on `cube_stack`, `fold_punch`, `panel`, `shapes2d`, `network` draws a round letter badge. (`network` already accepted node `labels`; they are now larger.) |
| `ball` icon looks like a globe | FIXED. Now a yellow-green tennis ball with two white seams (no blue, no meridians). Lessons that use it: 15, 22, 24, 34, 37. |
| Cube stacks tiny (L34 audit) | PARTLY. The drawing is now cropped to the stack (low stacks are drawn about 1.5 to 2 times larger). The printed size is still the lesson's `size`/CSS class: raising `size` is a lesson edit. S3 convention (which cell is front) is lesson content. |

## 5. Layout, deck, runner
| Defect | Status |
|---|---|
| Time answer boxes too small | FIXED. `digital: "[]"` is a 124 by 48 unit box: about 24 by 9 mm at the usual 46 mm clock, 6 mm or more tall down to size 50 %. |
| Exit ticket needs its own half page | FIXED as an opt-in. `workbook.exit_page: true` puts the Investigation on page 5 and the exit ticket and look-back on page 6 (kit pages then start at 7); the validator accepts the new page numbers. NOT applied to existing lessons: it changes page numbers in lesson text and book layouts, so it is a lesson-by-lesson choice (needed for L21 and L22 first). |
| Deck footers collide with cards | FIXED. Footer 22 px at 22 px from the bottom edge (it was 28 px at 44 px, inside the 1035 px content limit). Every deck needs a rebuild to show it. |
| Runner: "4-5-6" read as 4, minus 5, minus 6 | FIXED. A hyphen or dash between digits is a separator. |
| Runner: shown answer "The answer is The film ends at 4 : 00.." | FIXED. Fields items now say "It says: The film ends at 4:00." |
| Runner: slips for fields items | FIXED in the runner (`slips` of a templated fields item are filled and matched against the boxes in order). Needs the lesson data to supply `slips` in the template. |
| Runner: non-digit text in set and fields | FIXED. Same digit message as number items. |
| Runner: minute above 59 | FIXED for boxes whose id is m, mm, min, mins or minutes. |
| Runner: "Term 3" in the sub line | FIXED when the data has `term` (it does). |
| Runner: Enter in every box, narrow phone wrap, picture for calendar items, `set` list item for exact-amount questions | NOT FIXED. Larger runner and data design change; listed for the next runner pass. |
| L36 "sneak peek" | Not affected by any tool change; it is lesson data (M2). |

## Not in the request, also done
- `b_quest.py`: "Lessons 29 to 29" now reads "Lesson 29"; "Print at 100% (actual size)" removed from the Quest Log footer.

## Not fixed (outside the shared tools or too wide)
- `lessons/l20.json` hand-off, Quest gates, lesson wording, home-practice pictures (the home sheet has no picture slot), look-back box wrap in `b_print.py`, rewind label "Term 1 Lesson N" on child sheets, answer-key header "Term 3", `qs` slide thumbnails (table and clock thumbnails on slides). All are `b_print.py` or `b_deck.py` template changes that move every built lesson; they stay on the list.
- `cards` kit (see 2).

## Verify scripts adjusted (not lesson JSON)
- `verify/l31_checks.py`: the kit check expects 8 faint lines (rectangles are a 4 by 2 grid), not 6.
- `verify/l28_checks.py` still passes unchanged (sticks keep stroke width 7).

## Lessons that need a rebuild
- All 40 (guide timing line, deck footer, runner copy): `bash term/l1/build.sh NN`.
- Visible figure or kit change, check page fill after rebuild: 21 (clock, time box), 22 (clock, time box, event cards, ball), 23, 29, 30, 33 (clock), 24, 25, 26, 30, 39 (money, price tags), 20, 37, 39 (table icons: 20 is Term 2), 37, 38, 40 (picture graph), 32, 36, 40 (network), 28, 30 (sticks), 31, 32, 34, 40 (shapes2d or fold), 34, 40 (cube, fold), 27, 30, 32, 35, 40 (panel), 15, 22, 24, 34, 37 (ball icon), 31 (3 kit pages), 27, 29, 33, 35, 37, 39 (kit layout).
- Rebuilt and looked at here: 11, 21, 24, 31, 34, 36. The rebuilt files in `term/l1/out` are working copies and are not committed.
