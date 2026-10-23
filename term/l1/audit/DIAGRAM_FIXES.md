# Level 1 diagram fixes: running log (branch claude/great-fermi-1hv4vc)

Source: audit/DIAGRAM_AUDIT.md. Owner approved ("DIAGRAMS: go"). Only term/l1 files touched. Every touched lesson was rebuilt (`build.sh NN`, validate 0 FAIL) and every changed workbook page viewed.

## Shared figure helpers (tools/figs4.py and small edits to svg.py, figs2.py, figs3.py, b_print.py)
- Icons batch 3 (picture symbols, no bare dots): cat, dog, pear, plum, fig, orange, pawn, die, card, hat, stone, feather, mint, toffee, gum, rose, daisy, tulip, bowl, stamp, duck, goose, hen, kite, kite_blue, egg, fish_red/blue/gold (stripes, spots, plain: differ in B&W), book_m/s/a/sc, crab, snail, crayon, shirt, shorts, seat, pocket, page. Shell icon redrawn as a scallop.
- picture_graph: icon per row, larger row labels and key text.
- jump_lines (number line rows with point tiles, route arcs and clear headroom for the child's own jumps).
- balance (two pans, level or tilted, number tiles, picture groups, dashed "draw here" place).
- shelf (pictures on a labelled board), combos (tops + shorts), panel `title` and larger tile labels.
- ruler: objects are pencils / snail / bars lying on the scale with dashed drop lines from both ends, and a broken (zig-zag) left end when the ruler does not start at 0 (true 1:1 scale kept for print).
- hundred: mint cells are hatched (yellow solid), so the two read differently in black and white.
- domino pips coloured with a highlight; groups (plates, bags, jars) draw bigger pictures and use less height; clock numerals larger.
- Home sheets: `home_html` accepts `visual` / `visuals` on a home question (small figure at the right of the question).
- Layout: `stack` option on a question (figures one under another), `gw` width class for groups, page-fit loop also uses measured page heights.

## Done (top-25 order)
1. L37 and L38 picture graphs (items 14-25, all 12 graphs; deck, exit and online graphs too): real picture symbols per row (cat, fish, bird, pawn, die, card, shell, stone, feather, mint, toffee, gum, rose, daisy, tulip, books with different covers, fish with stripes/spots/plain...). Deck sort slide icons (ball, car, bike) now carry through to the graph slide.
2. L04 G3 yellow vs mint: hatched.
3. L06 number lines: S7 (printed 30-70 line, 36 marked, "Show 2 jumps of ten on the number line, beginning at 36"), T3 (two frog lines with arcs), G1/G2 (0-100 with 7 and 97). T1, T2, T4, G3, I1 lines were left out: no room on the pages without making the figures unreadable (S3/S4 line figures not added, Low).
4. L08 balance: S1 (part a), S2 (two plates as a tilted balance, dashed place for the child's buttons; draw box removed), S6.
5. L28 triangle patterns: T1 and T2 (rows of triangles with a ghost next one).
6. L35 labels: S1, S2, S5 (Picture titles, tile numbers), S4 (Shelf 1 / Shelf 2 drawn as shelves).
7. L09 rulers (S4, S6, T2, T3, G2): pencils/snail on the scale with drop lines; G2 ruler starts at 2 with a broken end.
8. Small multi-clock rows: L21 (S1, S2, S3, T1, T2, T3, exit), L22, L23 clocks now 35-46 mm with larger numerals.
9. L15 plates, jars, bags bigger; L24 S5 note and coin stacked at full size, T4 coin sets stacked (readable, cents shown); L25, L26 price-tag rows larger.
10. L36 T2 outfits picture (tops + shorts).
11. L10 T3 and G3 bar models (no answer printed).
12. Bare dots replaced by friendly objects (wording changed from dots to the object): L13 S1 (coloured domino pips), L15 T1 stars, L16 T1 ladybirds, L17 T1 sweets (check script updated), L36 S5 flowers, L40 S6 apples.
13. Home figure slot built; pictures added to L21 H1-H4, L22 H1-H2, L04 H2.
14. Online practice: figures added (with {vars}) to L01 c1 t1, L04 c3 c4 t1, L06 (10 items), L07 c4, L08 c1 c2 c4, L09 c1 c2 t1, L10 c3 c5 t4.

## Not done, and why
- L10 story_steps (S1-S3, S6, T4, G1), L39 story_steps: new card-pile figure not built.
- L03 digit_cards (11 items): not built.
- L12, L25, L39 bar-model gap bracket/transfer arrow: another agent changed bar-model numbers (white pills) in the same files; not touched here.
- L21 G1/G2 mirror clock (frame and reversed numerals): left as it is. A reflected face would print the answer on the page (the real time is the mirror image).
- L22 G1 time line labels, L11 line_up 10-child size, L13 S2/T1 ten-frame size, L19 symbol size, L27 grids, L31-L34 size pass, L33 dot grids, L34 top views: not done.
- Home sheets: only the 7 clock/100-square items above; the other ~85 B home items still have no figure.
- Online practice: L02, L03, L05, L10 story items and L21-L23 clock items have no figure yet.
- L06 T1, T2, T4, G3, I1 and L24 S6 figures kept at the old size or omitted for page room.

## Wrap-up (stopped early on the coordinator's request)
- L13 items (S1 domino pips, S2/T1 ten-frame size) are moot: lesson 13 is being retired by the x.10 consolidation. Also L10, L19, L20, L27, L30, L39 and L40 are being rewritten: the L10 bar models (T3, G3), L10 online figures, L40 S6 apples and L06/L08-L10 changes may need re-doing on the new lessons.
- All touched lessons (01, 04, 06-10, 13, 15-17, 20-40) were rebuilt after the last tool change: validate 0 FAIL. L17 T1 (larger sweets) was rebuilt after the books ran.
- Books were rebuilt once (Books 1-8, 24 PDFs, page counts unchanged, B&W check 0 non-grey) from the lesson PDFs of that moment. The Book 4 workbook still holds the old L17 T1 sweets: rebuild books with print/make_term_books.py then print/make_bw_print.py --check. The tracked specs (term_books_spec.json, bw_spec.json) were restored with git checkout.
- Not started: everything in the "Not done" list above.


## Update 23 Oct 2026 (combined fix pass): status
Closed now: L39 bracket, L9 snail, L4 G3, L6 G1 labels, L35 fills and 5-sun card, exit and home clocks (L21, L22) and the enlargements listed in RETROFIT_REPORT.md section 9. NOT closed: L31 to L34 size pass (pages are full), L33 dot grids, L34 top views, L11 line-ups, L35 T3 tiles, L10 and L39 story-step piles, L3 digit cards, figure-less home sheets, online figures for L2, L3, L5, L10, L21 to L23. WAIT-DIAGRAMS stays open.


## Update 23 Oct 2026 (WAIT-DIAGRAMS closing pass): closed / not-closed table
Every "closed" row below was viewed in the final colour PDF of the book (print/term/*) and, for the figures that matter in black and white, in the 1-bit PDF (print/bw/term/*). validate.py: 0 FAIL on all 40 lessons. Books rebuilt colour and B&W: workbooks 46/44/46/46/42/44/48/42, keys 22/32/22/30/22/32/22/32, home packs 12/14/12/14/12/14/12/14 (all unchanged, all even); `check_bw.py`: all 24 B&W PDFs ok, non-grey 0.00000.

| Item | Status | What was done and where it was viewed |
|---|---|---|
| M5 question text 13.1 pt shrunk to 10.6 pt on 13 to 14 pages | CLOSED (text size) | Cause: `b_print.py` escalated every page over 96.5% full to the 15 px text size when any page of the lesson overflowed. Now a page is tightened only when it is really over full (measured over 99.5%, or the real PDF has an extra page), and the text-shrink step is the last of seven levels. New levels in between: tighter padding, then one writing line less in each multi-line answer (`lastln`), tighter header lines, then figures 90% and 80%. Before: about 50 workbook pages at 11.2 pt (15 px). Now 0 pages at 11.2 pt in all 40 lessons and all 8 books (measured with PyMuPDF on the lesson and book PDFs). Viewed: the pages the audit named (Book 2 pp 5, 19, 21, 35; Book 3 pp 3, 4, 22, 23, 37, 38, 39; Book 4 pp 13, 37, 39) and the Book 5-8 pages that were small. NO content was moved off any page. Cost: 43 pages now trim the last blank writing line of multi-line questions (levels 4 to 6, see list below); pages 5 (Investigation + exit + look-back) of L13, L18, L20, L24, L26, L28, L32, L33 keep the look-back box at 13 px as before (question text is full size). |
| L8 S1 balance and S2/S6 | CLOSED | Beam picture cropped (the empty strip above the beam is gone) and sized 78 / 84 / 100 percent. No extra page. Viewed in Book 2 p 19. |
| L36 T1 handshake network and T3 | CLOSED | T1 75 percent (was 44), T3 66 percent; S1, S6, G3, E1 and E2 sizes raised too. No extra page. Viewed in Book 8 pp 3 to 7. |
| L11 line-ups (10 children) | CLOSED | `px` (figure width) set to 523 px (about 138 mm) for the 10-child lines and 387 to 433 px for the 7- and 8-child lines; the empty ordinal strip under figures with no labels is cropped, so the children are bigger for the same height. Viewed in Book 3 pp 3 to 6. |
| L31 to L34 size pass | CLOSED | New figure size field `mm` (grid cell, panel cell, cube edge in millimetres on the page) in `b_print._vis_html`; L31 to L35 figures set from 8 to 14 mm. L32 T2 table and tiles, L33 and L34 pages re-laid out with a `vlayout` option (rows of figures such as 1 then 3). Viewed in Book 7 pp 3 to 44. |
| L33 dot grids | CLOSED | Dots 2.6 mm across (were about 1 mm); route arrows, S/E badges and ringed marks drawn larger (`figs3.grid`); cells 9 to 12 mm; the A, B, C options of S4 are corner badges (the letter no longer sits in a cell); verify script L33 updated. Viewed in Book 7 pp 25 to 31. |
| L34 top views | CLOSED | Top views drawn 8 to 12 mm per cell. New `compass` option: BACK / LEFT / FRONT / RIGHT printed round every top view and answer grid, and a small compass (arrows) beside every isometric stack (S3, S4, T1, G2, S6, G3, home H1). The paragraph "Top stack: back left ..." stays in the question text. Viewed in Book 7 pp 33 to 36 and the 1-bit crops. |
| L35 T3 tiles and other L35 panels | CLOSED | Tile cell 13 mm (was about 7 mm) for T3, S3, S6, T1, G2, E2; G1 shadows 8.5 mm with corner letters (verify script L35 updated). Viewed in Book 7 pp 41 to 44. |
| Story-step card piles (L10, L39) | CLOSED | New figure `story_steps` (`figs4.py`): card piles joined by arrows that carry only the story's words ("gives away 20", "gets 6 more"), never + or -, never the result; unknown piles are dashed "?" cards. L10 S1, S2, S3, S6, T4, G1; L39 S2 and S4; online L10 c2, c4, g1. Viewed in Book 2 pp 33 to 36, Book 8 pp 25 and 26 and the 1-bit crop. |
| Digit cards (L3) | CLOSED | New figure `digit_cards`: big cards, 0 included (`figs4.py`). L3 S1, S4, S7, T1, T2, T3, T4, G1, G2, G3, I1, E2; home H1 and H4; online c3, c4, c5, t1 to t4, g1, g3. Viewed in Book 1 pp 21 to 24 and online in a browser (L3 c3). |
| Figure-less home sheets | PARTLY CLOSED | The home figure slot is now a floating column at the right of the question (28 mm; `hw` sets the width; wide strips such as bar models, number lines, rulers and story steps use `below`). 58 new figures on home items in 38 lessons (65 home items in all now have a figure, was 7): bundles, ten-frame, number lines, balance, ruler, story steps, line-ups, bar models, picture equations, counters, plates and bags, price tags, coins, calendar, stick patterns, clock faces, grids, top view, tiles and picture graphs. No figure gives the answer (checked item by item; the L25 and L26 tag prices follow the kit prices, as the verify scripts require). About 135 home items have no figure: these are pure number or word items (for example 63 + 18, "Fill in the missing numbers", time of day words) where a picture would only repeat the numbers or would give the answer. This is my judgement, not the owner's; an independent re-check should look at that list. Viewed in Home Pack PDFs for lessons 1 to 40 on 16 sheets (colour) and 6 sheets in 1-bit. |
| Online practice figures | CLOSED for the listed lessons | Added L2 c1, c2, t1, t2 (number line with the answer box, jump line), L3 (digit cards), L5 c1 (ten-frames), L10 c2, c4, g1 (story steps), L21 c3, L22 c2, c5 (clock faces with hands that do not overlap). L2 c1/c2 lines are cut so the missing number is not framed by its neighbours. Viewed: rendered variants in a browser page and L3 in the running practice page. L21 c1 c2 t1 t2 t3 g1 and L23 already had clocks. Not done: L2 t3, g1 to g3, L5 other items, and the online items of L10 c1, c3 that already carry figures. |
| Quest log figures | CLOSED | L30 and L40 Quest gate figures enlarged without adding a page (L40 gate 3 cubes 18 to 40 percent, fold figures 18 to 30, gate 1 circle 22; L30 unchanged because 4 pages is the limit). Viewed in Book 8 pp 39 to 42. |

Other shared changes in this pass (all in `term/l1/tools`): `bar_model` difference brackets (L12, L18, L25, L29, L30, L39) now draw a hatched "missing" piece on the shorter bar with a thick bracket and a larger "?" (the old bracket was a 0.5 mm hairline); the L8 balance tiles are light yellow so they print as a light stipple instead of a dark one; number-line jump labels accept `|` for two lines (L23 G1 labels no longer overlap); `jio.py` (lesson JSON round trip without formatting noise).

Pages that now use the "trim the last blank writing line" level (4) or tighter (5, 6) after all other steps (every one is still at full text size; none was moved): L3 p3; L6 p3; L8 p1, p3; L10 p1 (6), p3 (6); L13 p4; L15 p1, p3; L17 p3; L20 p3; L21 p1, p5; L22 p3; L23 p1, p3, p4, p5; L25 p3; L26 p3; L29 p3; L30 p3; L31 p1; L33 p1 to p5; L34 p1 (5), p3 (5), p4, p5 (5); L35 p1, p3, p4, p5; L36 p3 (5), p5; L37 p1, p3; L38 p4; L39 p1; L40 p4. On levels 5 and 6 the figures on that page print at 90 or 80 percent of their size: L10 p1, p3; L33 p2, p4; L34 p1, p3, p5; L36 p3.

NOT closed in this pass: nothing from the Not-done list above is left open except (a) the L21 G1/G2 mirror clock (left on purpose, see above), (b) about 135 home items without a figure (judged not to need one), (c) the online items named above, (d) L12/L25/L39 bar-model "transfer arrow" is still the thin red arrow (the difference brackets were redone, the transfer arrow was not), and (e) the lessons that the x10 consolidation will rewrite (L10, L20, L30, L40 and the retired L13 and L30 content) will need their figures re-checked after that rewrite. WAIT-DIAGRAMS: the diagram work is done to this list; the independent re-check and the owner's RELEASE are still needed.
