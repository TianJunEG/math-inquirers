# Holiday workbooks, Levels 4-6: diagram fixes (branch claude/great-fermi-1hv4vc)

Shared helper: `levels/figs_l4_6.js` (bar model with braces/overhangs/before-after rows, number line with marks, clock, rings for clock/week/star dots, sample-space grid, dot plot, vertical line, queue row). `FG.fit()` is applied to every `H.fig` in p4/p5/p6 `workbook_html.js`: it enlarges a figure until its smallest text prints at >= 9 pt on the A4 print (P5 is laid out 850 px wide and shrunk, the hidden 850 px spacer in `p5/wb_pdf.py` is untouched; P6 code-block figures keep their old size, floor 7.3 pt, to protect the page layout). New figures from the helper are always >= 9 pt. All shading uses hatch/dot patterns plus a label, so B&W works (`check_bw.py`: ok, non-grey 0.000).

## Page counts (source workbook PDF -> print PDF with blanks)
| Level | before | after | print pages before | after | note |
|---|---|---|---|---|---|
| P4 | 66 | 66 | 76 | 76 | unchanged |
| P5 | 57 | 57 | 62 | 62 | unchanged |
| P6 | 55 | 58 | 58 | 62 | L8, L9 and L7 each gained one page (L7 No.5 and the Python box now sit on their own page after the star dots); print_spec.json and bw_spec.json updated for P4-P6 only; all counts even |

## Done, in audit priority order
Level 4: L3 No.6, L4 No.5, L5 No.5, L10 No.6 (bar models replacing blank boxes: question text now says "use the bar model", answers unchanged); L10 No.5 queue (Mei counted from front and back); L6 No.3 three clocks (4 o'clock, 7 o'clock, blank for part c; smaller angle hatched); L6 No.1 angles enlarged (arms about 45 mm); L6 Think harder clocks (10/2 o'clock, 7:15/7:50, blank clocks); L9 No.3/5 graphs redrawn with 9 pt+ scales and taller plots; L5 No.1 number lines (ends and middle labelled, bigger arrows); L4 No.4c bars enlarged; L8 nets enlarged 1.5x; Think harder/Go further bars: L3 (2 340 beads, Ravi/Siti, Mei's money), L4 (beads, jar, book), L5 ($9.20 shared, jugs).
Level 5: L10 No.2 and No.3 bar models; L2 No.5 skeleton bar; L3 A1, A4, B1 bars; L6 No.2 price tags and No.3 tank now full width and legible, No.4 printers bar; L7 No.3 (25% up, 20% down) bars; fit enlarges tags, time line, tables/houses, solids, quadrilaterals (capped at 150 px height on Think harder pages so pages do not spill).
Level 6: L8 No.1 12-hour clock ring and 7-day ring (placed beside the sub-questions), L8 C7 two blank clock rings; L7 corner figure enlarged, L7 C5 blank 9-dot and 20-dot circles; L9 No.1 and No.4 dot plots (the $69 outlier shown off the scale); L6 C6/C7 6x6 and 3x4 sample-space grids; L10 C6 8x8 grid; L3 No.1 number line (arrows with letters, larger labels) and blank jump line; L3 T2 vertical line (diver, sea level, gull).
Answer keys: no figure changes what is asked; every figure is a scaffold (no value or result printed). Re-solved: L3 Q6 (31, 93, 62), L4 Q5 (45, 18), L5 Q5 (Mei $5.30, Siti $4.10), L10 Q5 (18, 15th), Q6 (Ben 10), P5 L10 Q2 ($63), Q3 (Mei $60, Ravi $55), L2 Q5 ($120 ... unchanged). Weekly PDFs for P4-P6 rebuilt.

## Second pass (freeze 2 Nov)
- Tutor Guide PDFs for P4-P6 regenerated (guide text and keys are unchanged; they do not quote workbook page numbers) and weekly PDFs rebuilt again from the final workbooks.
- B&W print pages viewed for every changed page of P4, P5 and P6 (contact sheets at 55 dpi). Fixed: P4 L9 graph y-axis labels every 20 (were crowded), P5 L5 Go further tank (was 5.6 pt, now >= 9 pt), P6 L4 age-bar labels clipped, P6 L5 puddle label overlapping the grid. Pre-existing B&W artefacts left as they are (orange "take-home" text and yellow table headers turn into patterned strikes or dots in the converter, not part of this job).
- New: P6 L6 T2 6x6 grid (Think harder lines trimmed to make room); P6 L7 No.4 star figure (5-point star drawn, blank 9-dot circle) with No.5 and the Python box moved to their own page; P4 L2 No.1 47 000 to 48 000 line with ticks every 100 (child marks 47 285; closer to 47 000); P4 L1 Q2 array of the example (4 rows of 10); P5 L3 Q2 "Before" skeleton (two dashed bars, Siti gives 12, Mei gets 12) next to the After bars; P5 L10 A1 bar (2/5 spent, then 1/3 of the rest, $24 left); P6 L5 No.5 route grid enlarged, puddle P now a hatched circle with a boxed P label (no colour cue; the question says "hatched circle"); P6 L4 machine strips (Think harder T3) and age bars (Go further C6).
- Re-solved and unchanged: P4 L1 Q2 (40 trees: 4x10, 5x8, 8x5, 10x4 ... as before), L2 Q1 (47 285 -> 47 290, 47 300, 47 000), P5 L10 A1 ($60), P6 L4 C6 (Mei 12).
- Text wording changes (keys unchanged): P4 L1 Q3 "Most packs" for "Greatest number of packs"; P6 L5 No.5 "hatched circle".
- Figure text still under 9 pt: P5 L8 A4 (square with equilateral triangle, about 7.4 pt, capped at 175 px so the Think harder page keeps its 5-page layout); P6 code-block figures (about 7.4 pt, unchanged on purpose).

## Not done (and why)
- P4: L7 C6/C7 garden/tank figures, L10 No.2 heads and legs picture row (Low).
- P5: L3 A2 red/blue bead bars, L6 A1/A3/B1/B2, L10 No.6 age bars, B1 tank bar.
- P6: L7 T3 and C6 polygon figures, L8 Caesar wheel, L3 C7 floor list, L9 mean "balance" bars.
