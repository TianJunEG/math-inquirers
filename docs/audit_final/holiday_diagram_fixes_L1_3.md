# Holiday workbooks, Levels 1-3: diagram fixes (23 Oct 2026)

Scope: the Level 1 (P1, `hp/`), Level 2 (`p2/`) and Level 3 (`p3/`) holiday student workbooks, from the audit `docs/audit_final/diagrams_holiday.md`.
Branch `claude/great-fermi-1hv4vc`. Nothing pushed, no PRs, no decks republished.
Level 4-6 files, `levels/figs_l4_6.js` and the other agents' work were not touched.

## What was built

| File | Purpose |
|---|---|
| `hp/figs_l1_3.js` | ONE shared SVG helper for Levels 1-3: icons (star, heart, shapes, cat, dog, fish, bird, fruit, face, counters with a letter), `coinF` / `coinRow` (cents printed), `noteF`, `numberLineF` (hops, frog, labels 15 units = about 11 pt), `barModelF` (units, braces top / bottom / vertical, "?", hatch for the added part), `pictureRowF`, `pictographF` (symbol graph, key, half symbol), `clockF`, `timeLineF`, `rulerF` + `barsOnRulerF` (start not at 0), hatch / dot / cross / line patterns so every shading works in B&W. House style: 1 unit is about 0.26 mm, icons >= 30 units (8 mm), text >= 15 units, hatch plus a label, never colour alone. |
| `hp/figs_l1_3_l1.js` | Level 1 figures and the Think harder / Go further hook (`FX`, keyed `<lesson>.T<n>` / `.C<n>`). |
| `p2/figs_l2.js` | Level 2 figures (also `fracBars`, balances, towers, base-ten blocks). Keys `<lesson>.<q>`, `.t<n>`, `.c<n>`; injected after the question by wrapping `H.q` in `p2/workbook_html.js`. |
| `p3/figs_l3.js` | Level 3 figures; same key scheme plus `<lesson>.<q><part>` (injected after a part); `H.q` and `H.sub` are wrapped in `p3/workbook_html.js`. |
| `print/make_print_l1_3.py` | Rebuilds only the Level 1-3 print PDFs and B&W PDFs and updates only their rows in `print_spec.json` / `bw_spec.json`. |

Question wording was changed only where the figure needed it (listed below). Every answer and tutor key was re-checked against the drawn figure; none changed.

## Page counts

| Level | Workbook pages before | after | Print pages before | after | Sheets before | after |
|---|---|---|---|---|---|---|
| 1 | 58 | 60 | 64 | 66 | 32 | 33 |
| 2 | 62 | 66 | 70 | 74 | 35 | 37 |
| 3 | 58 | 62 | 64 | 68 | 32 | 34 |

`outputs/print/print_spec.json` was updated for these three levels (all counts are even; blank backs of the cut-out pages unchanged: 6 / 8 / 6).
The increases are real: the new figures are taller than the one-line answers they replace and the "Start here" pages were already full. Where a page break was forced (`pb`) I removed it only when that let the page count stay the same.

Pages added, by lesson (each is a whole page that was added by a figure):
- Level 1: L4 (+1: Start here page 2, pattern rows), L9 (+1: clip / cube strips).
- Level 2: L5 (+1: Think harder, bar models), L6 (+1: Start here, coins and change lines), L7 (+1: Start here, fraction bars), L9 (+1: Think harder, balances).
- Level 3: L4 (+1: Think harder, bar models), L8 (+1: angles drawn 1.5x), L9 (+1: time lines), L10 (+1: queue figures).
If the printer cost matters, the cheapest pages to give back are Level 3 L4 Think harder No.T4 and Level 2 L5 Think harder No.T4 (each sits alone on a page).

## Level 1 items (audit numbers)

| Audit item | Done | What changed |
|---|---|---|
| 1 L4 No.4 missing pattern | yes | Row of 12 places: circle, star, square repeated, places 1-8 drawn, 9-12 empty boxes. Text now reads "Look at this pattern. It keeps going in the same way. You may draw in the empty boxes." Key unchanged (10th circle, 12th and 30th square). |
| 2 L1 No.5 sticker boxes | yes | Four boxes, stars (not dots): box 1 two stars, box 2 five stars, "+3" arrows, boxes 3-4 empty; the table stays. |
| 3 L1 No.3 frog line | yes | Two number lines 0-20 (17-unit labels), frog on 0, first hop of 4 drawn as a model, second empty line for the 5s. Text: "Circle or colour ... The first hop is drawn for you." Cross marks go "on the second number line". |
| 4 L4 No.2, No.3 | yes | Pattern rows (shapes; counters with R / B letters so they work in B&W), boxes to the asked place. |
| 5 L4 No.5, No.6 | yes | Cat / dog / dog row; letter tiles A B C D A B C. Both with empty numbered boxes. |
| 6-9 coins L6 No.1-No.6, L10 No.4 | yes | Coin pictures with cents (5¢, 10¢, 20¢, 50¢): column headers of the L6 No.1 table, a 85¢ purse strip in No.3, two empty coins and "= 35¢ ?" in No.4, Ali's and Mei's coins in No.5-6, the five coins of L10 No.4. L6 No.2 uses the No.1 coins (no extra tray, no room). |
| 10-11 L9 No.4, No.5 | yes | Clip / eraser strips (1 clip over 2 erasers, desk of 5 clips, pencil of 12 erasers); Mei, Ali (+3 dashed), Ben (-2 dashed) cube strips on one baseline. |
| 12 L5 No.4a | yes | Queue of 20 children in two rows, Mei marked 7th. (4b left as "draw the children": a 5-circle row would give the answer.) |
| 15 picture graphs L3, L10 No.3 | yes | Real symbols: apple, banana, orange, grape, watermelon (1 symbol = 1 child); dog, cat, fish, bird (1 symbol = 1 pet); key shown, shapes differ so B&W works. |
| 16-17 L3 T1-T4 | yes | Star graph (Red 3, Blue 5, Green 4) with key "1 star = 2 children" and the half star, empty Pizza row, Apple row with 3 and a half stars. C2 not drawn. |
| 19 L4 T1, T3, T4, C2 | yes | Shape row to place 14 (T1), beads (T3), squares made of sticks 1-2-3 (T4), dot triangles 1, 3, 6, 10, 15 (C2). |
| 20 L5 T1, T2, C2 | yes | Number-machine strips (? - 5 + 3 = 12; ? - 6 + 4 - 3 = 10); snail wall 0-9 cm. |
| 14 L2 No.6 | yes | Two bars, the bigger has "2", brace "10 altogether". |
| 18 L6 T5 | partly | Row of $2, $5, $10, $50 notes and the $1 coin. Price tags were drawn but did not fit on the page: not printed. |
| 23 L9 No.6 ruler | yes | Redrawn bigger, pencil from 0, crayon from 3 (not all from 0). |
| 25 L8 No.2 Venn | yes (text) | Question now names the loops: "Numbers less than 6" and "Odd numbers" (key unchanged). |
| 22 L7 No.1, No.4 enlarge | NOT done | The L7 Start here page is full; enlarging the house and triangle pictures pushed the lesson to 7 pages. Left at the old size. |
| 13 L8 No.1, 21 L10 C2, 17 C2, B-list | NOT done | See "What remains". |

## Level 2 items

| Audit item | Done | What changed |
|---|---|---|
| 1 L3 No.4 sharing | yes | Pile of 23 star stickers, four friend faces with empty dashed plates, a "left over" box. |
| 5 L2 No.6 | yes | Short bar and long bar (+200 hatched), vertical brace "700 altogether". |
| 6-7 L5 T2, T3, T4 | yes | Ben's money (15 book, left, gift, 42 now); Siti's beads (half given away, +12, 30 now); three marble bars (+5, +8, 40). |
| 8-9 L6 No.1, No.2 | yes | Price table has a small picture in each Item cell (curry puff, notebook, umbrella, bicycle); a strip of the coins and notes above it; No.2 shows $5, $2, $1 with "pay exactly $8". |
| 10 L6 No.3 change | yes | Two empty counting-up lines: 65¢ to $1 and $26 to $50 (start and end marked, hops left to the child). |
| 11, 12 L6 No.5, No.6 | yes | Bar 45¢ + 30¢ + 25¢ left; sticker 20¢ and eraser 50¢ tags. |
| 14 L7 No.3 | yes | Pairs of equal-length bars: 1/3 v 1/8, 5/9 v 7/9, and the four "smallest first" bars. |
| 15 L7 T2, T3 | yes | 3/8 and 3/5 bars; a bar of 8 with 3 + 2 shaded. |
| 16 L7 C5, C6 | yes | Empty strips of 12 and of 10 parts. |
| 24 L9 No.5 clocks | yes | Clock faces about 37 mm across (radius 70 units), hour hand short and thick, minute hand long and thin; caption says "long thin hand", not "red". |
| 18 L4 C6, C7 | yes | Towers of 2, 5, 8 cubes; two frog lines 0-30 with the first jump drawn. (T4 houses not drawn: the stick house picture is ambiguous for 5 sticks.) |
| 20 L9 T1, T3, C6 | yes | New balance-scale drawings (apple, lemon, pomelo, cube, ball, weights). |
| 21 L9 T2, C7 | yes | Time line 10:45 am to 12:10 pm; start line for three lessons from 8:15. |
| 19 L1 T3 | yes | 46 ten-blocks against 3 hundred-blocks and 15 ten-blocks. |
| T1 L6 | yes | Ben's money bar cut in half. |
| 27 nets | yes | Nets A-F redrawn 36 units per square, two per row. |
| not done | | L3 No.3, No.5, No.6 (B/A Med), L4 No.4 flowers, L6 T3, C1, L8 cube stacks (T1, C5, C7), L9 No.1 labels under the fruit, L10 No.6 towers, L1 No.1 blocks. |

## Level 3 items

| Audit item | Done | What changed |
|---|---|---|
| 1-3 L4 No.4, 5, 6 | yes | Two bars with "24 more" and "150 altogether"; Mei 85 and Siti 47 with the gap and a dashed "same number here" line; before and after bars (+$10 on both). |
| 4 L4 T1-T4, C7 | yes | Ali 3 times Ben (96); Siti +54; boxes A, B, C with +50 steps (600); rice +3 kg (9 kg); ribbon of 3 pieces (475 cm). |
| 5 L9 No.1f, T3 | yes | 3 m ribbon with four 65 cm pieces and a dashed remainder; box (250 g) and four books (1 kg 50 g). |
| 6 L9 No.5 | yes | Three time lines (3:45 to 5:10 pm; 4:35 pm; film ending 9:15 pm) with the o'clock marks and empty hops. |
| 7 L9 No.6 | yes | Time line from 06:40 with a tick every 25 minutes and Ravi at 08:15. |
| 8 L9 No.4 | yes | 24-hour strip, am and pm halves, 00:00 to 24:00. |
| 9 L9 T2, C5, C6 | yes | Shop hours line; bottle full / half poured out (1 kg 200 g, 750 g); pens and files bars ($9.20, files +60¢). T4 bus line not drawn. |
| 11 L6 No.5, 13 T2, T3, T4, C6 | yes | Empty bars cut into equal parts (sixths; fifths and tenths; quarters; thirds, sixths and twelfths); whole bar of 8 with 1/2, 1/4, 1/8 pieces. The child shades them. |
| 15 L10 No.3 | yes | Ben's two counts share one circle; Ali, "3 people between", Siti. |
| 16 L10 No.1 bar graph | yes | Bars use four hatch patterns, value labels 45 / 30 / 55 / 20, axis numbers 18 units, the missing Lime juice bar is a dashed outline with "?". |
| 20 L8 No.1, No.3 angles | yes | Angles drawn with arms 1.5x longer in 2 rows of 3; the fan in No.3 is bigger. |
| 18 L7 No.1 | partly | Grid figures 560 -> 500 wide would not fit; kept at 500 (was 420). |
| not done | | L9 No.1-3 number lines and price tags (10), L6 No.2, No.4 paired bars (12), L5 (14), L10 C7 (17), L7 rectangles (19), L8 T3 clocks (21), L1 No.4 blocks (22), L10 T1 coins (24), L9 T4 bus line. |

## B&W

All Level 1-3 figures use outline plus pattern plus label. `print/make_print_l1_3.py --check` ran `print/check_bw.py` on the three B&W files; results are in the last section of this file.

## Rebuilt

Workbooks (designed PDFs) for Levels 1, 2, 3; weekly PDF zips for Levels 1-3 (`outputs/designed/Math_Inquirers_Weekly_PDFs.zip`, `p2/..._Weekly_PDFs.zip`, `p3/..._Weekly_PDFs.zip`); `outputs/workbook/Math_Inquirers_P1_Student_Workbook_Designed.pdf` (copy); print and B&W print PDFs for Levels 1-3; `print_spec.json` and `bw_spec.json` rows for Levels 1-3.
Not rebuilt (nothing in them changed): tutor guides, question banks, parent packs, decks. The Word (`.docx`) Level 1 student workbook is NOT updated (`hp/workbook.js` is a separate build); the PDF is the printed version.

## What remains and why

1. Level 1 L7 No.1 / No.4 shape pictures are still small (page is full).
2. The B-list items (ten frames, arrays, base-ten blocks, trays for L6 T1-T4, paired bars) were not started.
3. Level 3 L9 No.1-No.3 (number lines, tags) and L7 / L8 grid and clock items.
4. Level 2 L3 No.3, No.5, No.6 and L8 cube stacks.
5. Think harder pages that now spill by one question (Level 3 L4 T4, Level 2 L5 T4) could be tightened to save two pages if the cost matters.
6. Level 1 and Level 2 decks and the tutor guide slides still show the older small figures where a deck copies a workbook figure; decks were not touched.

## B&W check result

`print/check_bw.py` on the rebuilt B&W print PDFs (all three: OK):

| Level | B&W pages | blank | max non-grey share | max light-tint cells |
|---|---|---|---|---|
| 1 | 66 | 6 | 0.00000 | 0.123 |
| 2 | 74 | 8 | 0.00000 | 0.140 |
| 3 | 68 | 6 | 0.00000 | 0.153 |

I looked at B&W pages of each level (Level 1: picture graphs, pattern rows, coins; Level 3: bar models, time lines, drinks graph): the hatched parts, dotted parts and the letter-tiled counters stay readable. `bw_spec.json` rows for Levels 1-3 were updated (66 / 74 / 68 pages, 33 / 37 / 34 sheets).
