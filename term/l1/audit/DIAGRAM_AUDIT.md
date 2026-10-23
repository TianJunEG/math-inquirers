# Level 1 Term workbooks: diagram audit (L01-L40)

Audit date 23 Oct 2026, branch `claude/great-fermi-1hv4vc`. Read-only audit of the 40 Level 1 term lesson workbooks (ages 6-8), their home sheets and online practice. Every workbook page was rendered at 80 dpi and looked at (about 240 pages), then each question was classified. Question text was extracted from `term/l1/lessons/lNN.json` and cross-checked against the rendered pages.

**Build state.** All 40 `out/lNN/LNN_Workbook.pdf` files exist. L30, L36, L39 and L40 had source JSON newer than their PDF (Term 4 fix checkpoint at 10:07); other agents were running builds (`build.sh 35`, extension build), so no lesson was rebuilt. The last good PDFs were used. The faults below sit in figure specs and figure code that did not change in that checkpoint, but re-check L30 and L36-L40 after the next rebuild.

**Classes.** A = a diagram is needed (a 6-7 year old cannot picture it from words). B = a diagram would clearly help. C = fine as text, or a good diagram already exists. D = an existing diagram has a fault. Page and ids follow the workbook (S = Start here, T = Think harder, G = Go further, I = investigation). Priority High = a child could not start without it (or the figure actively misleads).

## 1. Headline findings

1. **Picture graphs use bare red dots, not picture symbols (L37, L38: 12 graphs, High).** The figure supports `icon_name`, but the lessons set `"icon": "counter"`. The tutor deck makes the same switch: the sort slide shows ball, car and bike icons, and the next slide turns them into red dots. This is the owner's "picture graphs use picture symbols" feedback, and the biggest single fix. Row labels are also 2 mm tall.
2. **Home practice has no diagrams at all.** 0 of 200 home questions carry a figure; `home_html` in `tools/b_print.py` has no figure slot. Clock questions (L21 H1-H4, L22 H1-H2) are described in words ("the long hand is on the 6, the short hand is half way between the 8 and the 9"). L04 H2 asks about a 100 square the child does not have in front of them.
3. **Online practice L01-L10 has no figures (about 135 items).** Only 100 of 512 online items carry a `fig`. L16, L30, L39 and L40 have none either. Runner v2 already accepts any registered figure with `{vars}`, so this is content work, not engine work.
4. **Term 1 stories and jump questions have almost no picture support.** L06 pages 3-4 have no number line although the lesson is "jump and hop"; L08 "Balance and Swap" has no balance picture and S2 asks the child to draw a plate that is not there; L10 story steps are text only.
5. **Triangle pattern never drawn (L28).** T1 and T2 ask about rows of triangles made with sticks; only squares are pictured (S1).
6. **L35 labels missing.** Questions say "Picture 1", "Picture A", "Shelf 1", "Tile 2" but the figures carry no such labels.
7. **Colour-only cue (black and white).** L04 G3: yellow (luminance 201) and mint (215) print as the same grey; the question depends on which pair is yellow. Other colour pairs checked were fine (red 112 vs yellow 201; shapes in L27/L35 differ by shape and hatch).
8. **Sizes.** Many small figures are below 5 mm: multi-clock rows (numerals about 2 mm), ten-frames, plates/jars of 3 mm food icons (L15), coins and notes in sets (L24), price tags in rows of five, dot grids (L33, 1 mm dots), top-view cubes (L34), 10-child lines (L11).
9. **Rulers.** Objects are labelled bars floating 13-26 mm above the scale with no drop line, and not pencils. Every workbook ruler starts at 0, so the owner point that a ruler need not start at 0 is only half met (L09 T2 shifts the object, not the scale).
10. **Bare dots.** L13 S1 dominoes, L15 T1, L16 T1, L17 T1, L36 S5, L40 S6 use plain black or red dots; the owner called these dull.

## 2. Counts per term

Workbook questions are the tier questions S, T, G and the investigation I (exit tickets E1-E3 and look-back not counted; they reuse the same figures and share the clock and size faults). A question with both a missing diagram and a fault is counted once, under the more serious class.

| Term | Lessons | Questions | A | B | C | D |
|---|---|---|---|---|---|---|
| 1 | L01-L10 | 148 | 5 | 61 | 72 | 10 |
| 2 | L11-L20 | 141 | 0 | 24 | 90 | 27 |
| 3 | L21-L30 | 135 | 2 | 32 | 81 | 20 |
| 4 | L31-L40 | 131 | 1 | 16 | 73 | 41 |
| All | L01-L40 | 555 | 8 | 133 | 316 | 98 |


**Home sheets (5 questions per lesson, 200 in all, all text only):**

| Term | Lessons | Questions | A | B | C | D (n/a, no figures) |
|---|---|---|---|---|---|---|
| 1 | L01-L10 | 50 | 1 | 21 | 28 | 0 |
| 2 | L11-L20 | 50 | 2 | 29 | 19 | 0 |
| 3 | L21-L30 | 50 | 13 | 13 | 24 | 0 |
| 4 | L31-L40 | 50 | 0 | 24 | 26 | 0 |
| All | L01-L40 | 200 | 16 | 87 | 97 | 0 |


The home A items are clock, 100-square and grid questions that cannot be pictured from words alone.

**Online practice (512 items, heuristic count of items with no figure):**

| Term | Lessons | Questions | A | B | C | D |
|---|---|---|---|---|---|---|
| 1 | L01-L10 | 137 | 8 | 33 | 96 | 0 |
| 2 | L11-L20 | 126 | 0 | 38 | 88 | 0 |
| 3 | L21-L30 | 117 | 5 | 20 | 92 | 0 |
| 4 | L31-L40 | 132 | 0 | 9 | 123 | 0 |
| All | L01-L40 | 512 | 13 | 100 | 399 | 0 |


Online A = clock hands or ruler marks described in words with no `fig` (L09, L21-L23). Online B = named-child story problems without a `fig`. 100 items have a `fig`. Figures that exist online share the workbook faults (L37, L38 use `icon: counter`).

## 3. Top 25 priority items

| # | Lesson | Page | Item | Class | What the diagram should show | Figure |
|---|---|---|---|---|---|---|
| 1 | L06 | 3 | T3 | A | two frogs from 12: 3 tens then 4 / 4 then 3 tens, two arcs each | number_line two routes (exists) |
| 2 | L06 | 4 | G1 | A | 7 to 97 with jump 10 or 20 arcs the child can mark | number_line 0-100 (exists) |
| 3 | L06 | 2 | S7 | B | printed 30-70 line with 36 marked; the box is empty and a 6 year old cannot draw an even line | number_line blank (exists) |
| 4 | L08 | 1 | S2 | A | two plates drawn: 6+2 buttons on the left, 7 on the right; child draws the rest. Now the box is blank and there are no plates at all | plates (exists, kit only) |
| 5 | L10 | 3 | T3 | A | Ben 12, Mei 5 more, Siti 3 fewer than Mei | bar_model 3 bars (exists) |
| 6 | L10 | 4 | G3 | A | Mei 25, Ali +10, Ben ? so total 70 | bar_model total 70 (exists) |
| 7 | L28 | 3 | T1 | A | row of 1, 2, 3 triangles from sticks. No triangle picture exists anywhere in the workbook | stick_pattern triangle (exists) |
| 8 | L28 | 3 | T2 | A | rows of triangles with 20 and 25 sticks | stick_pattern triangle (exists) |
| 9 | L36 | 3 | T2 | A | 4 tops by 2 shorts: icons, a grid of outfits to fill | combos (NEW) |
| 10 | L35 | 1 | S1 | D | 'Picture 1' and 'Picture 2' (and Tile 1, 2, 3) are named in the question but not labelled on the figure | panel (enhance) |
| 11 | L35 | 1 | S2 | D | 'Picture A, B, C, D' not labelled on the figure | panel (enhance) |
| 12 | L35 | 2 | S4 | D | 'Shelf 1 / Shelf 2' not labelled and no shelf | objects (enhance) |
| 13 | L35 | 2 | S5 | D | 'Picture 1/2' and 'Tile' numbers not on the figure | panel (enhance) |
| 14 | L37 | 1 | S3 | D | every graph row uses a plain red dot, not a picture symbol of cat, fish, bird; row labels 2 mm | picture_graph (content) |
| 15 | L37 | 2 | S5 | D | red dots for chess, ludo, cards | picture_graph (content) |
| 16 | L37 | 3 | T2 | D | red dots for shells, stones, feathers | picture_graph (content) |
| 17 | L37 | 4 | G1 | D | red dots for sweets | picture_graph (content) |
| 18 | L38 | 2 | S4 | D | fruit shown as red dots | picture_graph (content) |
| 19 | L38 | 3 | T1 | D | fish shown as red dots; blue and gold fish cannot be told apart | picture_graph (content) |
| 20 | L38 | 3 | T2 | D | shells shown as red dots with key 2 | picture_graph (content) |
| 21 | L37 | 2 | S4 | D | blank boxes and key are red dots, not fruit | picture_graph (content) |
| 22 | L37 | 3 | T3 | D | red dots for books | picture_graph (content) |
| 23 | L37 | 4 | G3 | D | red dots for flowers | picture_graph (content) |
| 24 | L38 | 4 | G1 | D | stickers as red dots | picture_graph (content) |
| 25 | L38 | 4 | G3 | D | books as red dots | picture_graph (content) |

Items 14 to 25 are the same fix repeated on 12 picture graphs: switch the icon, enlarge the row labels, add an object key.

## 4. Figure types: what exists and what is missing

**Exists** (`svg.py`, `figs2.py`, `figs3.py`): bundles, kit_blocks (tens bars), scatter, ten_frame (one and two colour), ten_to_bundle, number_line (jumps, marks, hide, labels, prefix, suffix), hundred (shade, mark, arrows, window), seq tiles with gaps, ruler (true scale, shifted objects, guide mark), plates, objects (32 + 23 icons), groups (plate, bag, box, jar, cup), array (pairs, ring, hide), line_up, round_table, bar_model (compare, part-whole, units, brace, gap, transfer arrow), table (icon cells), picture_equation, domino, clock (hide hands, sector, mirror, digital), money (coins and notes), price_tag, calendar, stick_pattern (triangle, square), shapes2d (halves, quarters, fold, compose), grid (dots, squares, route, poly, mirror), cube_stack (iso, top, views), fold_punch, panel (tiles with pattern, size, turn), network, picture_graph (icon, each, tally, key, orient).

**Missing or needing an upgrade:**

| Figure | Used for | Effort |
|---|---|---|
| `digit_cards` (large card tiles, 0 included) | L03 (11 items), L03 home, online | S |
| `balance` (two pans, level or tilted, objects or numbers) | L08 (6 items), home, online | M |
| `story_steps` (card pile, arrow with +/-, next pile) | L10 (7), L39 (2) | M |
| `combos` (tops by shorts grid) | L36 T2, H2 | S |
| `bead_string` (repeat pattern) | L28 S2 | S |
| `clock_pair` (start clock, arrow, end clock) | L23, L29 | S |
| Ruler upgrade: object icon (pencil, crayon, snail) touching the scale, drop lines, broken ruler start | L09 (5 D) | M |
| bar_model upgrade: thick gap bracket, hatched gap block, transfer arrow with number badge, shelf and pocket skins | L12, L25, L39 (9 D) | M |
| picture_graph content with real icons, larger row labels, B&W-safe key | L37, L38 (12 D) | S (content) + S (label size) |
| shapes2d food skins (pizza, sandwich) | L31 (B) | S |
| New icons: egg, seat, pocket, page, shirt, shorts | L07, L20, L28, L36 | S |
| line_up finish/podium variant | L11 G3 | S |
| clock mirror frame and reversed numerals | L21 G1-G2 | S |
| Size defaults: clock rows, plates and jars, coin sets, price-tag rows, dot grids, top views | about 45 D items | M |
| Panel figure labels (`Picture 1`, `Picture A`, `Shelf 1`, tile numbers) | L35 (9 D) | S |
| Home figure slot (`visual` on `home_practice`, rendered small) | all 40 home sheets | M |

## 5. Build plan

| Step | Work | Items fixed | Effort |
|---|---|---|---|
| 1 | Picture graphs: set `icon` per graph (cat, fish, bird, book, shell, fruit...), larger labels, test B&W | 12 D High, online L37-L38 | S, half a day |
| 2 | L35 labels in `panel`/`objects` | 4 D High, 5 more | S, half a day |
| 3 | L06 number lines (T3, G1, S7 plus T1, T2, T4, G2, G3, I1) | 2 A High, 1 B High | S, half a day (figure exists) |
| 4 | L28 triangle pictures, L36 T2 `combos` | 3 A High | S, half a day |
| 5 | `balance` (L08) and `story_steps` (L10, L39) | 2 A High, about 20 B | M, 1.5 days |
| 6 | bar_model gap bracket, transfer arrow | 9 D | M, 1 day |
| 7 | Ruler upgrade plus broken ruler (L09) | 5 D, 1 B | M, 1 day |
| 8 | Size pass: clocks, plates/jars, coin sets, tags, grids, top views; mirror clock frame | about 40 D | M, 1.5 days |
| 9 | `digit_cards` and L03 | 11 B | S, half a day |
| 10 | Add figures to B items using existing types (stories in L01, L02, L07, L12, L15, L17, L18, L20, L22-L26, L29, L30) | about 60 B | M, 2 days |
| 11 | Home sheet figure slot, then add figures to the 40 A and about 90 B home items | home | M, 2 days |
| 12 | Online practice: add `fig` to L01-L10 and the story items | about 100 items | M, 2 days |
| 13 | Rebuild and check all 40 lessons, validator, B&W print | all | S, 1 day |

Total about 15 working days; steps 1-4 (about 2 days) remove every High item except L08, L10, L37 home equivalents.

## 6. Item list (A, B and D)

Page numbers are the workbook page (1 to 4; investigation on 5). Figure shows whether the figure exists in `tools` or is new.


### L01 Bundles and Singles (Term 1 lesson 1)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S5 | B | Med | 47 loose sticks drawn in a tray so the child ties them into tens | scatter/bundles (exists) |
| 2 | S6 | B | Low | Kumar's 3 bundles and 4 singles, labelled | bundles (exists) |
| 3 | T1 | B | Med | 5 tied bundles plus 14 loose sticks | bundles (exists; ones up to 14) |
| 3 | T4 | B | Med | Mei 7 bundles 2 sticks beside Ali 6 bundles 12 sticks | bundles x2 (exists) |
| 4 | G1 | B | Med | Ben and Siti pictures with loose sticks | bundles x2 (exists) |
| 4 | G2 | B | Med | 4 full boxes of 10 pencils and 18 loose pencils, target 60 | groups box + objects (exists, compose) |

### L02 Number Words and the Number Line (Term 1 lesson 2)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S6 | B | Low | 0 to 100 line with blanks | number_line step 10 (exists) |
| 3 | T1 | B | Med | 40-50 and 80-90 lines with 47 and 89 marked | number_line highlight (exists) |
| 3 | T2 | B | Med | 27 to 36 with the two end numbers ringed | number_line (exists) |
| 4 | G1 | B | Med | equal jump arcs with empty boxes | number_line jumps+hide (exists) |
| 4 | G2 | B | Med | 28 and 52 with two frogs and meeting arcs | number_line + frog marker (marker icon new, small) |

### L03 Digit Cards (Term 1 lesson 3)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | B | Med | two big digit cards 3 and 5 the child can swap | digit_cards (NEW) |
| 1 | S3 | D | Med | Mei's picture squares about 3 mm; Ben's picture missing (words only); no names on the pictures | kit_blocks/bundles (exists) |
| 2 | S4 | B | Med | cards 6 and 2 | digit_cards (NEW) |
| 2 | S7 | B | Med | cards 2 and 8 | digit_cards (NEW) |
| 3 | T1 | B | Med | cards 3, 5, 8 | digit_cards (NEW) |
| 3 | T2 | B | Med | cards 0, 3, 7 (0 card shown) | digit_cards (NEW) |
| 3 | T3 | B | Med | cards 1, 3, 5, 7 | digit_cards (NEW) |
| 3 | T4 | B | Med | cards 2, 4, 6 | digit_cards (NEW) |
| 4 | G1 | B | Med | cards 2, 5, 6, 9 | digit_cards (NEW) |
| 4 | G2 | B | Med | cards 1, 2, 3, 4 | digit_cards (NEW) |
| 4 | G3 | B | Med | cards 1, 3, 4, 7 | digit_cards (NEW) |
| 5 | I1 | B | Low | the four card pairs | digit_cards (NEW) |

### L04 The 100 Square Explorer (Term 1 lesson 4)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Low | 100 square cells about 6 mm, numerals about 2 mm: too small to colour 10 cells with a crayon | hundred (exists, cell size) |
| 1 | S2 | D | Low | same as S1 | hundred (exists) |
| 3 | T1 | B | Med | 100 square with the counter on 27 and arrow down 3 rows | hundred mark (exists) |
| 3 | T2 | B | Med | counter on 14, down 2, right 3 | hundred mark+arrows (exists) |
| 3 | T3 | B | Low | 6,7,9,12,16 tiles with gap arcs | seq with gaps (exists) |
| 4 | G1 | B | Low | 2,6,_,14,22 tiles with arcs | seq (exists) |
| 4 | G3 | D | Med | yellow vs mint cells have almost the same grey (luminance 201 vs 215) so the yellow pair cannot be told in black and white; parts c and e squeezed into a narrow column. Add hatch or bold outline plus letters | hundred (exists) |

### L05 Make-a-Ten Adding (Term 1 lesson 5)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Low | frames about 25 mm wide, counters 3 mm, plus sign tiny | ten_frame (exists) |
| 2 | S4 | B | Low | show the 6 as a separate group beside the 28 | bundles + ten_frame (exists) |
| 5 | I1 | B | Med | two blank ten-frames to draw on instead of an empty box | ten_frame pair (exists) |

### L06 Tens Jump, Ones Hop (Term 1 lesson 6)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S3 | B | Low | jump arcs for 23+10 etc. | number_line jumps (exists) |
| 2 | S4 | B | Low | jump or hop line | number_line (exists) |
| 2 | S5 | B | Med | 68 pencils as 6 boxes of 10 and 8 loose, 3 boxes to give away | groups box + objects (exists) |
| 2 | S7 | B | High | printed 30-70 line with 36 marked; the box is empty and a 6 year old cannot draw an even line | number_line blank (exists) |
| 3 | T1 | B | Med | 23, +40, +5 route | number_line jumps (exists) |
| 3 | T2 | B | Med | 79 back 30 then 5 | number_line jumps (exists) |
| 3 | T3 | A | High | two frogs from 12: 3 tens then 4 / 4 then 3 tens, two arcs each | number_line two routes (exists) |
| 3 | T4 | B | Med | ? then three tens landing on 78 | number_line (exists) |
| 4 | G1 | A | High | 7 to 97 with jump 10 or 20 arcs the child can mark | number_line 0-100 (exists) |
| 4 | G2 | B | Med | same line, fewest jumps | number_line (exists) |
| 4 | G3 | B | Med | 25, +30, -10, +20, then hop to 69 | number_line jumps (exists) |
| 5 | I1 | B | Med | start 6 jumping tens | number_line 0-60 (exists) |

### L07 Take Away, Count Up (Term 1 lesson 7)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S7 | B | Med | bus of 64 seats, 21 filled | bar_model part-whole (exists) or array of seats (icon new) |
| 3 | T2 | B | Med | 77 to 83 count-up line | number_line (exists) |
| 3 | T3 | B | Med | 24 and 31 plus 10 each | bar_model compare (exists) |
| 3 | T4 | B | Med | 71 pages, 46 read, ? left | bar_model part-whole (exists) |
| 4 | G2 | B | Med | 100 eggs, 64 sold, as a 100 grid | hundred shade (exists) |

### L08 Balance and Swap (Term 1 lesson 8)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | B | Med | equations as two pans, 5+3 against 4+? | balance (NEW) |
| 1 | S2 | A | High | two plates drawn: 6+2 buttons on the left, 7 on the right; child draws the rest. Now the box is blank and there are no plates at all | plates (exists, kit only) |
| 1 | S3 | B | Low | 6+3 against 5+9 tilted | balance (NEW) |
| 2 | S4 | B | Low | 7+5 level pans | balance (NEW) |
| 2 | S6 | B | Med | Mei 9 red 6 blue; Ben 10 red ? | bar_model compare or plates (exists) |
| 4 | G3 | B | Med | page + pocket bars equal in total | bar_model part-whole x4 (exists) |
| 5 | I1 | B | Low | add 3 to one pan, take 3 from the other | balance (NEW) |

### L09 Draw and Measure (Term 1 lesson 9)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S4 | D | Med | Ali's and Mei's pencils are labelled bars floating 13 mm and 26 mm above the ruler with no drop line; not pencils | ruler + pencil icon (enhance) |
| 2 | S5 | B | Med | NO workbook ruler starts anywhere but 0 (owner: rulers need not start at 0). Add a broken ruler, 3 to 13 cm, with an object lined up on the 5 mark | ruler start not 0 (exists, start param unused) |
| 2 | S6 | D | Med | same floating bar; the end does not touch the scale | ruler (enhance) |
| 3 | T2 | D | Med | same; the shifted start (2 mark) needs a drop line at both ends | ruler (enhance) |
| 3 | T3 | D | Med | tips between marks (9.3 and 12.7) cannot be read against a bar 26 mm away; needs a pencil tip touching the scale and a drop line | ruler (enhance) |
| 4 | G1 | B | Med | 30 cm ribbon in 3 pieces | bar_model part-whole (exists) |
| 4 | G2 | D | Low | plain bar labelled snail's way | ruler + snail icon (enhance) |
| 5 | I1 | B | Low | three lines starting at marks 3, 5, 8 | ruler objects (exists) |

### L10 Story Steps: Read It Twice (Term 1 lesson 10)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | B | Med | 30 take away 20 then plus 6 as two arrows between card piles | story_steps (NEW) or number_line |
| 1 | S2 | B | Med | 42 +7 -10 | story_steps (NEW) |
| 1 | S3 | B | Low | 25 +10 -3 | story_steps (NEW) |
| 2 | S5 | B | Med | Ali 23, Ben 10 more | bar_model compare (exists) |
| 2 | S6 | B | Med | bus 30, off 10, on 4 | story_steps (NEW) |
| 3 | T1 | B | Med | Ravi 15, 3 more than Mei | bar_model compare (exists) |
| 3 | T2 | B | Med | Mei highlighted with 6 in front and 4 behind | line_up (exists) |
| 3 | T3 | A | High | Ben 12, Mei 5 more, Siti 3 fewer than Mei | bar_model 3 bars (exists) |
| 3 | T4 | B | Med | 12 -7 -8 (second step impossible) | story_steps (NEW) |
| 4 | G1 | B | Med | 60 -24 -15 +30 | story_steps (NEW) |
| 4 | G3 | A | High | Mei 25, Ali +10, Ben ? so total 70 | bar_model total 70 (exists) |

### L11 Who Is Where? (Term 2 lesson 1)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S3 | D | Med | 10 children about 4 mm wide: too small to touch and count | line_up (exists, cell shrinks) |
| 3 | T2 | D | Med | same, 10 children | line_up (exists) |
| 4 | G3 | B | Med | race with 1st 2nd 3rd 4th flags | line_up finish/podium (variant NEW) |

### L12 Bar Strips: More and Fewer (Term 2 lesson 2)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Med | difference bracket is a 0.5 mm red hairline with a 2 mm question mark; make it a thick bracket or hatched gap block | bar_model gap (enhance) |
| 2 | S6 | D | Med | same | bar_model gap (enhance) |
| 2 | S7 | B | Med | 40 and 24 beads with gap | bar_model compare (exists) |
| 3 | T2 | D | Med | transfer arrow a hairline | bar_model transfer (enhance) |
| 3 | T3 | D | Med | same | bar_model gap (enhance) |
| 4 | G1 | D | Med | top/bottom shelf are just bars; hairline arrow carries the 7 | bar_model transfer (enhance) |
| 4 | G3 | B | Med | 12 more then 4 moved | bar_model compare (exists) |

### L13 Doubles and Near Doubles (Term 2 lesson 3)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | B | Low | plain black dots: use friendly pips (colour, ladybird) | domino (exists) |
| 1 | S2 | D | Med | frame about 30 mm, counters 4 mm, plus sign tiny | ten_frame (exists) |
| 3 | T1 | D | Med | ringed counter hard to see at 4 mm | ten_frame ring (exists) |

### L14 Odd + Odd: Always, Sometimes, Never (Term 2 lesson 4)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 4 | G1 | B | Low | a printed paired-counters mat for the draw box | array pairs mat (exists) |
| 4 | G3 | B | Low | same | array pairs mat (exists) |

### L15 Equal Groups (Term 2 lesson 5)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Med | sweets about 3 mm: counting 3 to 4 per bag is hard | groups bag (exists) |
| 1 | S2 | D | Med | plates 16 mm wide with cookies 3 mm | groups plate (exists) |
| 1 | S3 | D | Med | jars with 2 sweets of 3 mm | groups jar (exists) |
| 2 | S4 | D | Med | child must draw 4 dots on a 14 mm plate | groups plate (exists) |
| 3 | T1 | D | Low | bare black dots: use friendly objects | array (exists) |
| 3 | T2 | D | Med | plates 16 mm | groups plate (exists) |
| 3 | T3 | B | Med | 3 plates of 4 apples | groups (exists) |
| 4 | G2 | B | Med | 6 jars of 5 marbles, target 40 | groups jar (exists) |

### L16 Skip-Count Tables (Term 2 lesson 6)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 3 | T1 | D | Low | bare navy dots: use friendly objects | array (exists) |

### L17 Sharing and Grouping (Term 2 lesson 7)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S3 | B | Med | 14 sweets and 2 friend plates | groups plate (exists) |
| 3 | T1 | D | Low | 19 bare red dots | objects (exists) |
| 3 | T2 | B | Med | 20 biscuits, 4 people | groups plate (exists) |
| 3 | T3 | B | Med | 18 sweets in bags of 6 | groups bag (exists) |
| 3 | T4 | B | Med | 17 stickers, bags of 5 | groups bag (exists) |
| 4 | G2 | B | Med | 4 pots, then 3 more each | groups pot (exists) |
| 4 | G3 | B | Med | 20 stickers, keeps 2, 3 friends | groups (exists) |

### L18 Times Stories (Term 2 lesson 8)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S2 | B | Med | 4 boxes of 3 pencils | groups box (exists) |
| 2 | S6 | B | Low | add the 2 lost marbles | bar_model (exists) |
| 3 | T1 | B | Med | 3 boxes of 6 + 5 loose | groups box + objects (exists) |
| 3 | T3 | B | Med | Mei 4, Ravi twice | bar_model (exists) |
| 4 | G1 | B | Med | 4 cards x3 stickers, 5 cards x2, 4 in hand | groups card (exists) |

### L19 Picture Equations (Term 2 lesson 9)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Low | an empty glass beside 3 counters: nothing is hidden; 11 in all not shown | objects cup (exists) |
| 2 | S7 | D | Low | bags drawn empty, no 13 total mark | objects bag (exists) |
| 3 | T1 | D | Low | symbols about 5 mm | picture_equation (size) |
| 3 | T2 | D | Low | same | picture_equation (size) |
| 3 | T3 | D | Low | same | picture_equation (size) |
| 4 | G1 | D | Low | same | picture_equation (size) |
| 4 | G2 | D | Low | same | picture_equation (size) |
| 4 | G3 | D | Low | same | picture_equation (size) |

### L20 Find One First (Term 2 lesson 10)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Med | 4 pens drawn but the $16 total is nowhere in the picture | objects + bracket (enhance) |
| 2 | S5 | D | Med | 5 pens drawn but $15 not shown, so the claim '$4 each' cannot be tested | objects + bracket (enhance) |
| 3 | T2 | B | Med | dozen buns in a 12-tray with $24 | array egg box (icon egg NEW) |
| 3 | T3 | B | Med | 6 cups = $24 | bar_model (exists) |
| 3 | T4 | B | Med | 4 pens $8 and a $10 note | bar_model (exists) |
| 4 | G1 | B | Med | hat and scarf tags | price_tag x2 (exists) |
| 4 | G2 | B | Med | 8 pens $24 | bar_model (exists) |

### L21 What Time Is It? (Term 3 lesson 1)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Med | four clocks 28 mm wide, numerals 2 mm | clock (size) |
| 1 | S3 | D | Med | three small clocks | clock (size) |
| 2 | S5 | D | Med | three small clocks | clock (size) |
| 3 | T1 | D | Med | two clocks, numerals 2 mm | clock (size) |
| 4 | G1 | D | Med | mirror clock has no numerals and is captioned 'mirror' under it: add a mirror frame, show reversed numerals, and the real clock beside it | clock mirror (enhance) |
| 4 | G2 | D | Med | same | clock mirror (enhance) |

### L22 Five Minutes at a Time (Term 3 lesson 2)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Med | three small clocks | clock (size) |
| 2 | S6 | D | Med | two small clocks | clock (size) |
| 4 | G1 | D | Med | time labels 2 mm tall | number_line (enhance) |
| 4 | G2 | B | Med | 2:45 to 3:20 chunk line | number_line time (exists) |
| 4 | G3 | B | Med | two reading spans | number_line time x2 (exists) |

### L23 Time Passes (Term 3 lesson 3)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S3 | B | Low | start clock to end clock | clock pair (NEW convenience) |
| 2 | S4 | D | Med | three small clocks | clock (size) |
| 2 | S5 | D | Med | two small clocks | clock (size) |
| 3 | T1 | B | Med | 5:30 plus 1 h / plus half hour | number_line time (exists) |
| 3 | T2 | B | Med | 4:15 and 9:45 each plus half hour | number_line time (exists) |
| 3 | T3 | B | Med | work back from 7:00 pm | number_line time (exists) |
| 4 | G3 | B | Med | both end 4:30 | number_line time (exists) |
| 5 | I1 | B | Med | 12:30 to 3:00 with job blocks | number_line time (exists) |

### L24 Dollars and Change (Term 3 lesson 4)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S5 | D | Med | the $2 note is 15 mm wide with 'PLAY MONEY' about 1 mm tall; hard to tell from the $1 coin | money (enhance) |
| 3 | T1 | B | Low | ruler $4, book $5, $10 note | price_tag (exists) |
| 3 | T3 | B | Med | pencil tag, $1 coin, 40c change | price_tag + money (exists) |
| 3 | T4 | D | Med | three coin sets 7 mm coins, 2 mm labels | money (size) |

### L25 Price Tags: Compare and Choose (Term 3 lesson 5)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S2 | D | Med | hairline gap bracket | bar_model gap (enhance) |
| 3 | T2 | D | Med | same | bar_model gap (enhance) |
| 3 | T3 | B | Med | robot $27, drum $18, $50 note | price_tag x2 + money (exists) |
| 3 | T4 | D | Med | five tags 14 mm wide, price 2 mm | price_tag (size) |
| 4 | G1 | D | Med | same | bar_model gap (enhance) |
| 4 | G2 | B | Med | puzzle, scooter, doll | bar_model 3 bars (exists) |

### L26 The School Shop (Term 3 lesson 6)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 3 | T1 | B | Med | pens $2 and books $7 tags | price_tag + table (exists) |
| 3 | T2 | B | Low | $2 and $5 notes | money notes (exists) |
| 3 | T3 | B | Med | book $9, hat $4, pen $2, $50 | price_tag x3 + money (exists) |
| 4 | G1 | B | Low | $10, $5, $2 notes | money (exists) |
| 4 | G3 | D | Low | five tags 14 mm | price_tag (size) |

### L27 Fill the Grid (Term 3 lesson 7)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S5 | B | Low | blank 3 by 3 | grid (exists) |
| 4 | G1 | D | Low | cell 8 mm with 2 mm letters | grid squares (size) |
| 4 | G2 | D | Low | a, b, c markers 2 mm grey | grid squares (size) |
| 4 | G3 | B | Low | blank 5 by 5 | grid (exists) |

### L28 Make a Table (Term 3 lesson 8)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S2 | B | Med | 3 red 2 blue bead pattern | bead_string (NEW) |
| 2 | S3 | B | Med | squares 4,5,6 drawn | stick_pattern square (exists) |
| 2 | S4 | B | Low | 5 pages a day | array book icons (exists) |
| 3 | T1 | A | High | row of 1, 2, 3 triangles from sticks. No triangle picture exists anywhere in the workbook | stick_pattern triangle (exists) |
| 3 | T2 | A | High | rows of triangles with 20 and 25 sticks | stick_pattern triangle (exists) |
| 3 | T3 | B | Med | squares 1 to 6 so the wrong count shows | stick_pattern (exists) |
| 4 | G1 | B | Med | triangle and square rows side by side | stick_pattern both (exists) |
| 4 | G2 | B | Med | 31 and 37 sticks | stick_pattern (exists) |
| 4 | G3 | B | Low | 10 pictures each | stick_pattern (exists) |
| 5 | I1 | B | Med | 14 strips | stick_strips + stick_pattern (exists) |

### L29 Spot the Mistake (Term 3 lesson 9)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 3 | T1 | B | Low | 74 -30 +1 | number_line (exists) |
| 3 | T3 | B | Med | Mei 28, Aisha 6 more | bar_model compare (exists) |

### L30 Calendar Detective (Term 3 lesson 10)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 3 | T1 | B | Low | today Thursday strip | calendar week strip (exists) |
| 3 | T2 | B | Low | day 1 Monday to day 10 | calendar (exists) |
| 4 | G3 | B | Med | 6th Monday, 3 weeks later | calendar (exists) |
| 5 | I1 | B | Med | 31 days starting Wednesday | calendar full month (exists) |

### L31 Half and Quarter (Term 4 lesson 1)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | B | Low | pizza/sandwich in place of plain shapes | shapes2d food skin (enhance) |
| 1 | S3 | B | Low | same | shapes2d food skin (enhance) |
| 4 | G1 | D | Low | letters A, B, C sit inside the cells being counted | grid squares (enhance) |
| 4 | G2 | B | Med | half circle and half-square triangle pictures | shapes2d (exists) |

### L32 Build the Figure (Term 4 lesson 2)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S3 | D | Low | the 'boat' is a bare trapezoid outline, no sail or mast | grid dots (enhance) |
| 2 | S5 | B | Low | two squares / two half circles joined | shapes2d (exists) |

### L33 Copy on the Grid (Term 4 lesson 3)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S3 | D | Low | dots 1.3 mm to draw a path | grid dots (size) |
| 2 | S4 | D | Med | labels A, B, C 2 mm and dots 1 mm | grid dots (size) |
| 2 | S5 | D | Low | same | grid dots (size) |
| 3 | T1 | D | Med | tiny S and E badges, dots 1 mm | grid route (size) |
| 3 | T2 | D | Med | same | grid route (size) |
| 3 | T3 | D | Med | picture of 2 sets is 25 mm wide, dots 1 mm | grid route (size) |
| 4 | G2 | D | Med | same | grid route (size) |
| 4 | G3 | D | Low | same | grid dots (size) |

### L34 Cubes and Views (Term 4 lesson 4)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S3 | D | Med | options A, B, C are 8 mm with 2 mm digits and no clear orientation arrow | cube_stack top view (size) |
| 2 | S4 | D | Med | orientation is a paragraph ('Top stack: back left...'); a 7 year old needs an arrow and corner labels on the picture | cube_stack (enhance) |
| 3 | T1 | D | Med | same paragraph | cube_stack (enhance) |
| 3 | T3 | D | Low | dots 1 mm | fold dots (size) |

### L35 Spot It (Term 4 lesson 5)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | High | 'Picture 1' and 'Picture 2' (and Tile 1, 2, 3) are named in the question but not labelled on the figure | panel (enhance) |
| 1 | S2 | D | High | 'Picture A, B, C, D' not labelled on the figure | panel (enhance) |
| 1 | S3 | D | Low | tile letters 2 mm | panel (size) |
| 2 | S4 | D | High | 'Shelf 1 / Shelf 2' not labelled and no shelf | objects (enhance) |
| 2 | S5 | D | High | 'Picture 1/2' and 'Tile' numbers not on the figure | panel (enhance) |
| 3 | T1 | D | Low | letters 2 mm | panel (size) |
| 3 | T3 | D | Med | tile numbers 1 mm tall | panel (size) |
| 4 | G1 | D | Low | shadow dots 1 mm | grid (size) |
| 4 | G2 | D | Low | letters 2 mm | panel (size) |

### L36 Count Everything (Term 4 lesson 6)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S5 | D | Low | bare navy dots | array (exists) |
| 2 | S6 | D | Low | yellow versus white only; add hatch | grid squares (enhance) |
| 3 | T2 | A | High | 4 tops by 2 shorts: icons, a grid of outfits to fill | combos (NEW) |
| 4 | G1 | B | Med | 5 and 6 children with lines | network all lines (exists) |
| 4 | G3 | B | Med | Home, Park, School with road counts | network labelled (exists) |

### L37 Make Your Own Graph (Term 4 lesson 7)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S3 | D | High | every graph row uses a plain red dot, not a picture symbol of cat, fish, bird; row labels 2 mm | picture_graph (content) |
| 2 | S4 | D | High | blank boxes and key are red dots, not fruit | picture_graph (content) |
| 2 | S5 | D | High | red dots for chess, ludo, cards | picture_graph (content) |
| 3 | T2 | D | High | red dots for shells, stones, feathers | picture_graph (content) |
| 3 | T3 | D | High | red dots for books | picture_graph (content) |
| 4 | G1 | D | High | red dots for sweets | picture_graph (content) |
| 4 | G2 | B | Med | 21 stickers, four children | bar_model (exists) |
| 4 | G3 | D | High | red dots for flowers | picture_graph (content) |

### L38 Graph Detectives (Term 4 lesson 8)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Low | book icons 3 mm | picture_graph (size) |
| 2 | S4 | D | High | fruit shown as red dots | picture_graph (content) |
| 3 | T1 | D | High | fish shown as red dots; blue and gold fish cannot be told apart | picture_graph (content) |
| 3 | T2 | D | High | shells shown as red dots with key 2 | picture_graph (content) |
| 4 | G1 | D | High | stickers as red dots | picture_graph (content) |
| 4 | G2 | B | Med | ducks, geese, hens boxes | picture_graph blank (exists) |
| 4 | G3 | D | High | books as red dots | picture_graph (content) |

### L39 The Problem-Solving Toolbox (Term 4 lesson 9)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 1 | S1 | D | Med | hairline bracket | bar_model gap (enhance) |
| 1 | S2 | B | Med | 30 -12 -9 | story_steps (NEW) |
| 2 | S4 | B | Med | ? -8 = 17 | story_steps backwards (NEW) |
| 2 | S6 | D | Low | stray bold caption 'PLAY MONEY' under the coins looks like a heading | money (enhance) |
| 3 | T1 | B | Med | 3 rulers $15 | bar_model (exists) |
| 3 | T2 | B | Med | $10 note, toy $6, change $1 | bar_model (exists) |
| 3 | T3 | B | Low | Siti 4th from front, 3rd from back | line_up (exists) |
| 3 | T4 | B | Med | 7 coins of 5c and 10c | money (exists) |

### L40 Inquirers' Showcase (Term 4 lesson 10)

| Page | Id | Class | Priority | What the diagram should show or what is wrong | Figure |
|---|---|---|---|---|---|
| 2 | S4 | B | Med | Siti 9, Ravi 4 more | bar_model compare (exists) |
| 2 | S5 | B | Low | 9 + 7 make-a-ten | ten_frame (exists) |
| 2 | S6 | D | Low | bare navy dots | array (exists) |

All other workbook questions are C (symbolic number work, drawing boxes where the child draws, or already supported by a good figure).

## 7. Home sheets and online practice: items

Home (A, High): L21 H1,H2,H3,H4; L22 H1,H2; L04 H2; L19 H4,H5; L27 H1,H2,H3,H4; L28 H3,H4; L24 H1.

Home (B): L01 H1,H4; L02 H1,H3; L03 H1,H3,H4; L04 H1; L06 H1,H3; L07 H1,H4; L08 H1,H2,H3; L09 H2,H4; L10 H1,H2,H3,H4; L11 H2,H3; L12 H1,H2,H3,H4,H5; L13 H2; L15 H1,H2,H5; L17 H1,H2,H3,H4,H5; L18 H1,H2,H3,H4,H5; L19 H1,H2,H3; L20 H1,H2,H3,H4,H5; L24 H2,H3; L25 H1,H2,H3,H4; L26 H1,H2,H3,H4; L28 H1,H2; L29 H5; L31 H1,H3,H4; L32 H1,H3,H4; L33 H1,H4; L34 H1,H4; L35 H1,H3; L36 H1,H2; L37 H1,H2,H4; L38 H1,H2,H3,H4; L39 H1,H2,H4.

Online: L01-L10 have no `fig` on any item; the same figures as the workbook (bundles, number_line, hundred, digit_cards, balance, ruler, bar_model) should be attached with `{vars}`. L21-L23 items that describe hands in words (`c3`, `c5` L21; `c2`, `c5` L22) need `clock` figures with `hide`. L09 items `c1`, `c5`, `t1`, `t3`, `g2` need the `ruler` figure. L37 and L38 `picture_graph` figs use `icon: counter`.

## 8. Tutor decks

Decks reuse the same figure code, so every D above also appears on slides (checked L37: the sort slide uses ball, car and bike icons and the graph slide switches to red dots). Wide figures scale up on slides, so the size faults matter less there; the label, icon and bracket faults do not.

