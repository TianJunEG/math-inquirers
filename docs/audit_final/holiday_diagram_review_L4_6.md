# Holiday workbooks, Levels 4-6: independent diagram review (23 Oct 2026)

Reviewer: independent (not the builder). Branch `claude/great-fermi-1hv4vc`, audit only: no workbook, figure or key was edited. Print order Fri 6 Nov 2026, so every item below is fixable before Mon 2 Nov.

Page numbers are PRINT PDF page numbers (`outputs/print/Math_Inquirers_P{4,5,6}_Workbook_PRINT.pdf`, and the same page in `outputs/print/bw/`). Source-workbook page = print page for the content pages of all three levels (the blanks and cut-outs come after).

## Verdicts

| Level | Verdict | Why |
|---|---|---|
| P4 (76 pp) | READY for print | No High findings. Two Medium items worth a quick fix (M7 jar bar gives away the key step, M8 red text hatched in B&W). |
| P5 (62 pp) | NOT READY until H1 and H2 are fixed | H1 (Go further tank figure has colliding and clipped labels) and H2 (L1 No.6 number line shades the answer). Both are one-line figure edits in `p5/content/l5.js` and `p5/content/l1.js`. After that, ready. |
| P6 (62 pp) | READY for print | No High findings. One Medium (M6, the "P" label on the route grid) worth a quick fix. |

## Method

- Rendered every content page of P4, P5 and P6, colour print file and B&W print file, with `pdftoppm` (90 dpi contact sheets, 200 to 400 dpi crops for every changed figure). Compared several changed pages against the pre-change PDFs (commit `a161c6c`).
- Extracted every text span with PyMuPDF and listed everything under 9 pt.
- Re-solved every question that has a changed figure by hand and compared with the printed answer key in the tutor guide (`pdftotext` of the three Tutor Guide PDFs).
- Re-derived figure geometry for the nets (P4 L8), the clocks, the angle figures, the number lines, the dot plots, the route grid and the bar-model proportions.
- Checked page counts and `print_spec.json` / `bw_spec.json`, and that the hidden 850 px spacer is still in `p5/wb_pdf.py` (line 23: yes, intact).
- Limits: I looked at every page, but the "unchanged" pages only got a visual pass and a check of figure against question, not a full re-solve.

## Page counts and layout (check 6)

| Level | source pages | print pages | print_spec | bw_spec | even? | blank pages (verso) |
|---|---|---|---|---|---|---|
| P4 | 66 | 76 | 76 | 76 | yes | 58, 60, ..., 76 |
| P5 | 57 | 62 | 62 | 62 | yes | 54, 56, ..., 62 |
| P6 | 58 | 62 | 62 | 62 | yes | 56, 58, 60, 62 |

All consistent. `p5/wb_pdf.py` hidden 850 px spacer is present. No page overflow or lost content found. The only clipping is H1 below. P6 L7 p35 (No.5 and the Python box alone) and P6 L8 p39/p40, L9 p46 are mostly blank pages; this is acceptable but see L1 (guide wording).

## Answer-key re-solve (check 3)

All printed keys match the figures as drawn. Re-solved by hand: P4 L1 Q2 (4 x 10 array, 6 ways), Q3 (6 packs of 3 red and 4 blue), L2 Q1 (47 285 -> 47 290, 47 300, 47 000), L3 Q6 (124 plates: 93 and 31, 62 more), T1 (468), L4 Q5 (45 and 18), L5 Q1 (A 6.3, B 6.85, C 4.53, D 4.58, E 0.247 read off the three lines at the drawn tick positions), Q5 ($5.30 and $4.10), Q6 (0.4 kg and 2.05 kg), L6 Q1 (40, 115, 75, 150 drawn to size), Q3 (120, 150; the hatched wedges show the smaller angle), Q5 (b = 27 from 15, 27, 48), T3 (210), L8 Q2 (A-E, B-D, C-F: confirmed by rolling the net), Q3 dice nets (3,5,4,2 / 6 and 5,4 / 1,2 / 3,6), L9 Q3 (Ali 10 to 60, Mei 30 to 55, equal at $50 in Week 5, $15 in Week 8), Q5 (60 and 12), L10 Q4 (Ali nasi lemak, Ben laksa, Mei prata, Siti chicken rice), Q5 (18 people, 15th from the back), Q6 (Ben 10); P5 L2 Q3 ($60 left of $240 etc.), L2 Q5 ($120), L3 Q2 (84; Siti 48, Mei 36), A1 ($120), A4 ($80), B1 ($60), L4 Q1 to Q4 (24, 84, 36, 13 and 15; 30 and 30; 35 and 21; 96, 16, 16, 24, 40), L5 Q3 to Q6 (27 l, 33 l, 12 cm, 14.4 l, 12 cm), L6 Q4 (18 and 20 min), Q5 ($4.80: six half-hour lots), L7 No.3 ($100 then $80), L8 Q1 to Q4 (112, 68, 112, 65; 108, 72, 108; 116, 32; 70, 100; 62, 56, 118, 24), L10 Q2 ($63), Q3 (Mei $60, Ravi $55), A1 ($60); P6 L3 Q1 (A -8, B -3, C 4), Q3 (15, 9, -13), L4 Q1 to Q3, L5 Q5 (20 routes; 8 avoiding P: 12 pass through P), L6 Q1 (3/8, 6/8), Q4 table (0:6, 1:10, 2:8, 3:6, 4:4, 5:2), L7 Q3, Q4 rows, L8 Q1 (3 o'clock, 5 o'clock, 7 o'clock, Monday, Thursday), L9 Q1 (total 30, mean 6), Q4 ($22, $15, $12, 6 pupils), L10 Q1 (6, 11, 16 sticks; 76 from the code).

No key is wrong. No figure contradicts a key.

## Findings

Severity: High = wrong, misleading, gives away the answer, or unreadable. Medium = should fix if there is time. Low = cosmetic or note.

### High

**H1. P5 L5 Go further B3 (tank with the 10 x 10 x 15 block), print p27 (also bw p27).**
The figure is broken after the enlargement:
- The label "block 10 × 10 × 15" is clipped at the right edge of the SVG and prints as "block 10 × 10 × 1" (pdftotext confirms the text is cut).
- The block's own "15 cm" label overprints the water-depth arrow label "10".
- The block's "10 cm" label at the base is overprinted by the tank's "30 cm" label ("30 cm" and "10 cm" collide into one smudge).
- Cause (`p5/content/l5.js`, B3 block, lines 216 to 220): the text at x = 285, size 15 starts too far right for a viewBox of 400; the box labels are placed on top of each other.
- Fix: move the block caption to x about 235 or shorten it to "block 10 x 10 x 15" at size 14 and anchor it above the block; drop the block's duplicate "10 cm" label (the question already gives 10 x 10 x 15); move the water label "10 cm" to the left of the arrow; put "30 cm" under the tank, clear of the block. Re-render the page and check the B&W page.

**H2. P5 L1 Start here No.6 number line, print p4 (also bw p4).**
The figure is titled "Which numbers round to 2 500 000?" and draws a shaded band from 2 499 500 to 2 500 500. That is the answer to No.6(a) (circle each one that rounds to 2 500 000) and (b) (smallest and greatest). It is also wrong at the right edge: 2 500 500 rounds to 2 501 000, and the key says the greatest is 2 500 499. (Pre-existing figure, but it is in the print file and the answer is on the page.)
- Fix (`p5/content/l1.js`, lines 28 and 32): delete the dashed `rect` and the title text, keep the five ticks and labels. No change to the key.

### Medium

**M1. P5 L2 No.1(b) (print p8): figure shows the comparison.** Two bars on the same whole, with each child's share shaded (A shows 2 of 3, B shows 3 of 5), so the longer shaded bar answers "which group gets more". The hint already asks for shortfalls. Fix: draw the two wholes unshaded with the 3-part and 5-part cuts only, or shade nothing. The labels "Group A / Group B" (7.3 pt) and "one child's share is shaded" (6.8 pt) are also under 9 pt: enlarge to 9 pt.

**M2. P5 L2 No.3 (print p8): text 7.7 to 8.2 pt.** "Ben" (7.7), "240 stickers" (8.2), "the remainder: draw the rest!" (7.7). Builder's note says all fitted figures are at least 9 pt; this one is not. Enlarge the figure about 20 percent (there is white space beside it).

**M3. P5 L5 No.3 tank (print p23): labels 7.4 pt** ("50 cm", "40 cm", "30 cm", "18 cm"). These are the numbers the child needs for the Start here box. Enlarge or increase label size to at least 9 pt.

**M4. P5 L8 Think harder A4 (print p41).** Square with equilateral triangle: figure is about 14 to 18 mm wide, the two "?" labels are 7.4 pt and the 15 degree angle is a sliver. The builder lists this as a known exception, but there is room: the A4 box has about 100 px of empty height under the figure. Allow the cap to rise to about 230 px so the "?" labels reach 9 pt. Needs a re-render of the Think harder page; check it still fits on one page (it has about 60 mm free at the bottom of p41).

**M5. B&W: red labels become hatched ghost text.** In the B&W files every red label turns into a fine hatch. Angle values are data the child needs. Worst cases (9 to 11 pt): P5 L8 p38 (72, 64, 68, 95, 130, 70, 110, 80, "?"), p39 (62, 38, 56), p41 (56, "3 x B", "?"), p42 (40); P6 L7 p33 ("turn 70°"); P6 L9 p46 ("$69 →"); P4 L5 p26 ("$1.20 more"), p32 and p35 ("45°"), p38 ("? cm" twice), p54 ("Mei is 12th from the back"). At 300 dpi they are readable but weak. Fix: set these labels to the navy (#1B2A49) or black in the figure code, or make the B&W converter map red text to black. The P5 L8 angle values are the priority. (The builder noted orange text and yellow headers as left alone; red data labels are a different case.)

**M6. P6 L5 No.5 route grid (print p24).** The boxed "P" sits on the street between circle (0,1) and the hatched circle and touches the left circle, so P can be read as labelling the left circle. The question says "the hatched circle marked P". Fix: place the P box directly above-left of the hatched circle clear of the street, or put the P inside the hatch (white box in the centre). Also "B" touches the top-right circle edge (Low). Hatching is clear in B&W (dots with a heavy rim), so no colour cue is used.

**M7. P4 L4 Go further No.5 (print p24, jar bar).** The bar is pre-cut into 6 equal parts: Mei's brace covers 3, Ali's covers 2, and the last cell is labelled "5 left". That gives away the key step (1/2 + 1/3 leaves 1/6, and 1/6 = 5). It is the Go further challenge, so it should not be this scaffolded. Fix: draw the bar as one undivided bar with only "Mei takes 1/2", "Ali takes 1/3" and "5 left" braces, or an unmarked bar with the "5 left" brace. (Think harder No.2 on p23 is an 8-part bar with 3 shaded; that is a normal scaffold, fine.)

**M8. P4 L10 No.5 queue (print p54).** The figure is right (7th from the front, 12th from the back) but "Mei is 12th from the back" is red, about 10 pt, and prints as hatched ghost text in the B&W file. Fix: print it in navy/black. It repeats the question text, so it could also be dropped.

**M9. P5 L6 No.4 printers bar (print p29).** Not to scale and ambiguous: "P alone, 5 min" is drawn as 25 percent of the 900-page bar, but it is 150 of 900 (16.7 percent); and the "? minutes" brace sits under "P and Q together" only, while the question asks for the time for the whole job from the start (key 20 min). Fix: either extend the brace over the whole bar and label it "? minutes in all", or draw the P-alone segment at one sixth.

### Low

- L1 P4 L1 No.4 timeline (p4): the labels are the union of both bus timetables (6:10, 6:15, 6:20, 6:30, 6:40, 6:45, 6:50, 7:00), so the blanks can be copied. Pre-existing. Optional: label only the ticks, not the times.
- L2 P4 L2 No.2 (p9): the 62 000 to 64 000 line labels 62 500 and 63 500, which are the smallest and the "largest + 1" for part (a). Pre-existing, partly a scaffold. Optional.
- L3 P5 L6 No.5 timeline (p29): the line draws exactly six half-hour boxes, so the count is visible. Child still has to compute the price. Note only.
- L4 P4 L6 clocks (p32 No.3, p36 Think harder No.2 and 3): the minute hand covers the "12", and in the 7:50 clock it covers the "10". Hands and times are right (4 o'clock 120, 7 o'clock 150, 10 and 2 o'clock, 7:15 and 7:50 all match). Cosmetic: draw the numerals under the hands or shorten the minute hand.
- L5 P4 pages 4, 9, 30, 32, 35 (print and B&W): a thin sliver (the top edge of the next question tab) shows at the bottom left above the footer. Pre-existing and trivial, but visible on A4. If an easy fix exists, clip the overflow; otherwise ignore.
- L6 P6 L4 Go further No.6 (p22): the "+12" boxes are wider than one part (80 vs 54 px), although with n = 12 the +12 equals exactly one part. Add "Not to scale" (the alt text says it; the page does not). Do not draw it to scale; that gives the answer.
- L7 P6 L9 No.1 and No.4 (p45, p46): "books read" and "dollars a week" are 8.7 pt; other axis text is at least 9 pt. Trivial.
- L8 P5 L4 No.1 (p18): the six side labels are 8.8 pt (just under 9).
- L9 P6 L7 to L9 page splits vs guide wording (check 7): the Tutor Guide says "pairs work on page 1, alone on page 2" (and lesson ws1/ws2 lines: L7 "Page 2: Q3, Q4, Q5", L8 "Page 1: Q1, Q2", L9 "Page 1: Q1 to Q4"). After the new page breaks, P6 L7 Q5 is on a third sheet (p35), L8 Q2 is on the second sheet (p40) and L9 Q4 is on the second sheet (p46). Nothing is wrong on the page (the "After question n you may choose" boxes are still correct), but a tutor reading the guide will find Q2/Q4/Q5 one sheet later than stated. Either add "(next page)" to those `ws1`/`ws2` lines in `p6/content/l7.js`, `l8.js`, `l9.js` and rebuild the guide, or leave it.
- L10 P6 L5 No.5 B label touches the corner circle (see M6).

## Per-question table for the questions the builder lists as changed

OK = figure matches the text (counts, labels, units, order), does not give the answer, key re-solved and correct, legible in colour and B&W. Otherwise the finding is in brackets.

**P4**
| Q | Print p | Result |
|---|---|---|
| L1 Q2 array (4 rows of 10) | 3 | OK |
| L1 Q3 "Most packs" wording | 3 | OK; key "6 packs, 3 red and 4 blue" fits "Most packs"; no guide or deck text quotes the old wording |
| L1 Q4 timeline (not changed) | 4 | OK (Low L1) |
| L2 Q1 47 000 to 48 000 line | 9 | OK; ticks every 100, 47 500 labelled; 47 285 sits at the 2.85th tick, closer to 47 000 |
| L3 Q6 bar (Laksa 1, chicken rice 3, 124 plates) | 16 | OK |
| L3 Think harder No.1 bar (2 340 beads) and challenge bars | 18, 19 | OK |
| L4 Q5 jar bar | 21 | OK |
| L4 Think harder No.2, Go further No.5 and No.7 bars | 23, 24 | OK (M7 for No.5 giving away the step) |
| L5 Q1 three number lines | 25 | OK; read positions give 6.3, 6.85, 4.53, 4.58, 0.247; middle labels only |
| L5 Q5 bar, Q6 scale and bar | 26 | OK |
| L5 Go further bars (Ali/Ben/Siti, jugs) | 29 | OK |
| L6 Q1 four angles | 30 | OK; arms about 45 mm, angles measure 40, 115, 75, 150 |
| L6 Q3 clocks | 32 | OK (Low L4) |
| L6 Think harder clocks, compass | 35, 36 | OK (Low L4) |
| L7 Q1 corner | 38 | OK; lengths 7, 9, 4, 4 and the two "?" sides are to scale on the grid (B&W "? cm" weak, M5) |
| L8 nets (Q1 to Q3) | 43 | OK; enlarged, all legible; opposite faces confirmed |
| L9 Q3 and Q5 graphs | 49 | OK; scales at least 9 pt, y labels every 20 and 4; dots on the right values |
| L10 Q5 queue | 54 | OK figure; M8 (B&W text) |
| L10 Q6 bar | 54 | OK; the "? years" brace correctly shows 60 unknown |

**P5**
| Q | Print p | Result |
|---|---|---|
| L2 Q5 skeleton bar (2 fifths, then half the rest, $36) | 9 | OK, drawn to scale (book and $36 each 1.5 fifths) |
| L3 Q1 and Q2 bars (Before skeleton, After bars) | 13 | OK; After bars 3 : 4 match "3/4 as many" |
| L3 A1, A4, B1 bars | 16, 17 | OK, drawn to scale |
| L4 triangles Q1 to Q4 | 18, 19 | OK; labels 8.8 to 9 pt (Low L8) |
| L5 No.3, No.4, No.5 and No.6 solids and tanks | 23, 24 | No.3 tank labels 7.4 pt (M3); No.4, No.5, No.6 OK |
| L5 Go further B3 tank | 27 | H1 |
| L6 No.2 tags, No.3 tank, No.4 printers | 28, 29 | No.2, No.3 OK; No.4 M9 |
| L7 No.3 bars (25 percent up, 20 percent down) | 33 | OK, drawn to scale |
| L8 Q1 to Q4, A1, A3, A4, B1, B2 | 38 to 42 | OK geometry; A4 tiny (M4); B&W red labels (M5) |
| L10 No.2, No.3 bar models, A1 bar | 48, 49, 51 | OK, drawn to scale |

**P6**
| Q | Print p | Result |
|---|---|---|
| L3 No.1 number line | 13 | OK; A, B, C at -8, -3, 4 |
| L3 No.3 sea picture | 13 | OK; seagull 9, diver -6, crab -15 at scale |
| L3 blank jump line (No.4) | 14 | OK |
| L3 Think harder No.2 vertical line | 16 | OK; seagull 9, sea level 0, diver -14 drawn at scale; no result printed |
| L4 No.2 machines, T3 machines, Go further ages | 18, 21, 22 | OK (Low L6) |
| L5 No.5 route grid | 24 | OK; 20 and 8 re-solved; puddle P hatched, text says "hatched circle" (consistent); M6 for the label |
| L6 Think harder No.2, Go further No.6, No.7 grids | 31, 32 | OK; 6 x 6, 6 x 6, 3 x 4 grids blank, labels correct |
| L7 No.1 corner/ring figure, No.4 stars, Go further No.5 dots | 33, 34, 38 | OK; 5-point star correctly drawn (0-2-4-1-3), 9 and 20 dots evenly spaced, labels right |
| L8 No.1 12-hour ring and 7-day ring | 39 | OK; ring order correct, Saturday marked |
| L8 Go further No.7 two blank rings | 44 | OK |
| L9 No.1 and No.4 dot plots | 45, 46 | OK; all five and all seven values at the right positions; $69 off scale with arrow |
| L10 No.1 hexagon chain, Go further No.6 8 x 8 grid | 51, 55 | OK |
| P6 code blocks | various | about 7.0 to 8.1 pt as the builder said; legible in print; judged acceptable |

## Notes on the builder's own list (check 7)

- "P6 L5 No.5 now says 'hatched circle'": consistent with the figure and the key. The deck slide (`split/p6l5/.../p6l5-ws2.html`) says "put 0 at the puddle", which is still correct; no guide text mentions colour.
- "P4 L1 Q3 wording shortened to 'Most packs'": consistent with the key; the old wording "Greatest number of packs" survives only in the question bank (a different question about pencils and erasers), which is fine.
- No other workbook/guide/deck inconsistencies found for changed questions, apart from the page-split wording in Low L9.

## Suggested fix order (all small)

1. H1 (`p5/content/l5.js` B3 labels), H2 (`p5/content/l1.js` remove band and title). Rebuild P5 workbook, weekly PDFs, print and B&W files.
2. M5 (red labels to navy, P5 L8 angle values first).
3. M7, M8 (P4), M6 (P6).
4. M1 to M4, M9, then Low items if time allows.
After any edit, re-run the page-count check (P5 must stay 62, P4 76, P6 62) and `check_bw.py`.
