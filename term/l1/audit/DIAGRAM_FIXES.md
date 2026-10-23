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
