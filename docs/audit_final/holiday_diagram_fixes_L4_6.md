# Holiday workbooks, Levels 4-6: diagram fixes (branch claude/great-fermi-1hv4vc)

Shared helper: `levels/figs_l4_6.js` (bar model with braces/overhangs/before-after rows, number line with marks, clock, rings for clock/week/star dots, sample-space grid, dot plot, vertical line, queue row). `FG.fit()` is applied to every `H.fig` in p4/p5/p6 `workbook_html.js`: it enlarges a figure until its smallest text prints at >= 9 pt on the A4 print (P5 is laid out 850 px wide and shrunk, the hidden 850 px spacer in `p5/wb_pdf.py` is untouched; P6 code-block figures keep their old size, floor 7.3 pt, to protect the page layout). New figures from the helper are always >= 9 pt. All shading uses hatch/dot patterns plus a label, so B&W works (`check_bw.py`: ok, non-grey 0.000).

## Page counts (source workbook PDF -> print PDF with blanks)
| Level | before | after | print pages before | after | note |
|---|---|---|---|---|---|
| P4 | 66 | 66 | 76 | 76 | unchanged |
| P5 | 57 | 57 | 62 | 62 | unchanged |
| P6 | 55 | 57 | 58 | 60 | L8 and L9 each gained one page (Start-here page 2 now starts later); print_spec.json and bw_spec.json updated for P4-P6 only; all counts even |

## Done, in audit priority order
Level 4: L3 No.6, L4 No.5, L5 No.5, L10 No.6 (bar models replacing blank boxes: question text now says "use the bar model", answers unchanged); L10 No.5 queue (Mei counted from front and back); L6 No.3 three clocks (4 o'clock, 7 o'clock, blank for part c; smaller angle hatched); L6 No.1 angles enlarged (arms about 45 mm); L6 Think harder clocks (10/2 o'clock, 7:15/7:50, blank clocks); L9 No.3/5 graphs redrawn with 9 pt+ scales and taller plots; L5 No.1 number lines (ends and middle labelled, bigger arrows); L4 No.4c bars enlarged; L8 nets enlarged 1.5x; Think harder/Go further bars: L3 (2 340 beads, Ravi/Siti, Mei's money), L4 (beads, jar, book), L5 ($9.20 shared, jugs).
Level 5: L10 No.2 and No.3 bar models; L2 No.5 skeleton bar; L3 A1, A4, B1 bars; L6 No.2 price tags and No.3 tank now full width and legible, No.4 printers bar; L7 No.3 (25% up, 20% down) bars; fit enlarges tags, time line, tables/houses, solids, quadrilaterals (capped at 150 px height on Think harder pages so pages do not spill).
Level 6: L8 No.1 12-hour clock ring and 7-day ring (placed beside the sub-questions), L8 C7 two blank clock rings; L7 corner figure enlarged, L7 C5 blank 9-dot and 20-dot circles; L9 No.1 and No.4 dot plots (the $69 outlier shown off the scale); L6 C6/C7 6x6 and 3x4 sample-space grids; L10 C6 8x8 grid; L3 No.1 number line (arrows with letters, larger labels) and blank jump line; L3 T2 vertical line (diver, sea level, gull).
Answer keys: no figure changes what is asked; every figure is a scaffold (no value or result printed). Re-solved: L3 Q6 (31, 93, 62), L4 Q5 (45, 18), L5 Q5 (Mei $5.30, Siti $4.10), L10 Q5 (18, 15th), Q6 (Ben 10), P5 L10 Q2 ($63), Q3 (Mei $60, Ravi $55), L2 Q5 ($120 ... unchanged). Weekly PDFs for P4-P6 rebuilt.

## Not done (and why)
- P4: L2 No.1 rounding line, L1 arrays, L7 C6/C7 and L10 No.2 picture row (B/Low); L4 T1/T3-type bars not on printed pages.
- P5: L10 T1/B1 age bars, L3 No.2 Before model and A2, L6 A1/A3/B1/B2, L9 tables and houses beyond the automatic enlargement, L8 quadrilateral hatch marks beyond enlargement (the A4 Think harder figure is capped for page fit, text about 7 pt).
- P6: L6 T2 grid (Think harder page full), L7 No.4 star figure on the page itself (page full; blank dot circles are on Go further instead), L7 T3/C6 polygon figures, L8 Caesar wheel, L5 No.5 route map (colour-only puddle), L4 machine flow, L3 C7 floor list, L9 mean "balance" bars.
- P6 code-block figures stay at about 7.4 pt (not changed, they are 10.5 px blocks).
- Weekly/tutor guides: only the weekly PDFs were rebuilt; Tutor Guide PDFs were not regenerated (guide text and keys unchanged).
