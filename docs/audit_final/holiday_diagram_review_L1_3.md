# Holiday workbooks, Levels 1-3: independent review of the new diagrams (23 Oct 2026)

Reviewer: independent (not the builder). Audit only: no workbook, figure, key or print file was changed.
Scope: `hp/`, `p2/`, `p3/` designed PDFs (61 / 66 / 62 pages), the colour print files and the B&W print files in `outputs/print/` and `outputs/print/bw/`, against `docs/audit_final/holiday_diagram_fixes_L1_3.md`.
Method: every page of all three workbooks rendered with pdftoppm and read (colour for layout, B&W print file for pattern and label reliance); suspect figures re-rendered at 200-300 dpi; text sizes measured with PyMuPDF (spans under 9 pt); every changed question re-solved by hand and the printed key (the `key` arrays in `hp/lessons.js`, `p2/content/l*.js`, `p3/content/l*.js`, also in the tutor guides) checked against what the figure shows; geometry of rulers, number lines, time lines, bar widths, clock hands and angles measured on the rendered page or in the source.

Page numbers below are workbook (source) page numbers. Source and print numbers are equal up to the first cut-out page, so they are also the print page numbers except in the cut-out section.

## Verdicts

| Level | Verdict | Why |
|---|---|---|
| 1 (hp) | NOT ready until 1 High is fixed (small fix) | Think harder T1 picture-graph key is cut off on p16 (colour and B&W). Everything else is Medium or Low. Every key re-solved: all correct for the figures. |
| 2 (p2) | NOT ready until 1 High is fixed (small fix) | L7 No.3 shows shaded bars that answer the question. Medium: clipped labels on the L9 balance and time-line figures, tiny weight labels, small L5 bar labels. Keys all correct. |
| 3 (p3) | NOT ready until 4 High items are fixed | L10 No.1 placeholder bar drawn at 60 (answer is 50), L9 No.5 time lines (misleading hop, start off the line), L10 No.5 captions 5.9 pt and clipped, L9 C5 label clipped. Keys all correct. |

No answer key is wrong for the figure it sits with. No ruler, coin value, clock hand, bar-to-scale or picture-graph count is wrong (details at the end). The High items are layout and design faults, all fixable in the figure files before Mon 2 Nov.

Page counts: print files 68 / 74 / 68 pages, all even, equal to `print_spec.json` (68 / 74 / 68, 34 / 37 / 34 sheets, blanks 7 / 8 / 6). Colour print files have exactly those blank pages (even pages before each cut-out section). Every cut-out page starts on an odd (front) print page. No unexpected blank page. B&W print files have the same page counts and no blank-page flag.

---

## HIGH

### H1. Level 1, Lesson 3, Think harder T1 and T4, p16: picture-graph key is clipped
- The key box reads "Key: [star] = 2 children   [half star] = 1 cl" and stops at the box edge: the half-star symbol is sliced and "child" is cut to "cl". Same in the colour and the B&W file.
- T4 depends on this half-star ("A half picture means 1 child. Apple has 3 pictures and a half").
- Change: widen the key box / viewBox in `hp/figs_l1_3_l1.js` (the `3.T1` pictograph key) so the half-star and the full text "= 1 child" fit. Re-check the T4 row (3 stars and a half star: the half star there is fine).

### H2. Level 3, Lesson 10, No.1 (drinks bar graph), p51: the missing Lime juice bar is drawn to 60, the answer is 50
- Dashed placeholder "?" box reaches the 60 gridline. Key: Lime juice = 200 − 150 = 50 ("the bar reaches the 50 line"). A child who copies the dashed box draws 60. Misleading and contradicts the key.
- Change: make the placeholder an empty outline only at the bottom (a short dashed baseline plus the "?" label above the axis), or draw it at a clearly meaningless height with no top edge (open dashed sides, no top), so the child must find the height.

### H3. Level 3, Lesson 10, No.5 (sticks in a row of squares), p52: captions unreadable and clipped
- Captions under the three square figures are 5.9 pt (5.6 pt after the 0.9429 print scale) and the first one is cut at the left ("iquare: 4 sticks" instead of "1 square: 4 sticks").
- Change: caption text at least 9 pt (the table below already gives 4, 7, 10), widen the viewBox so the first caption is not cut. The table row 4, 7, 10 already carries the data, so shorter captions ("1 square", "2 squares", "3 squares") are enough.

### H4. Level 3, Lesson 9, No.5 time lines, p46: second line misleading, third line too short for the answer
- (b) Piano lesson 4:35 pm + 50 min (answer 5:25 pm). The line has hops 4:35 to 5:00 ("? min") and 5:00 to 6:00 ("? min"). The second hop ends at the 6:00 tick, so a child who fills the hops writes 25 and 60 (85 minutes), which contradicts the 50-minute lesson. The 5:25 point is not on the line.
  Change: end the second hop at an unlabelled point (or at a blank "?" tick) at 25 minutes after 5:00, not at 6:00.
- (c) Film ends 9:15 pm and lasts 1 h 50 min (answer 7:25 pm). Line has ticks 8:00, 9:00, 9:15 and starts only about 12 minutes before 8:00. 7:25 falls off the left end of the line.
  Change: extend the line to the left (about 40 minutes before 8:00), or move 8:00 further right.
- (a) is correct and to scale (3:45, 4:00, 5:00, 5:10: 4.6 px per minute throughout).

### H5. Level 2, Lesson 7, No.3 (compare fractions), p38: shaded bars answer the question
- 3(a) "Which is bigger?" shows 1/3 against 1/8 and 5/9 against 7/9 as shaded bars of equal length; 3(b) "Smallest first" shows 1/5, 1/2, 1/10, 1/4 as shaded bars. A child reads the answers off the lengths. The question text says "Draw bars the same length if it helps": the figure removes the task. (Bars are correct: equal lengths, right shading.)
- Change: print the same equal-length bars with the parts marked but NOT shaded (child shades), as the builder did on L7 T2/T3 and No.4; or keep shaded only for one pair as a worked example.

---

## MEDIUM

### Level 1
- **M1-1. L8 No.2 (Venn), p40:** the overlap of the two loops is about 8 mm wide; the child must write "1, 3, 5" there (3 numbers). Enlarge the loops (or the overlap) so the middle fits 3 numbers. Loop titles are about 8 pt.
- **M1-2. L7 No.1 (house), p34:** the flag triangle (counted in the key: triangle 2 = roof + flag) and the sun circle are about 3-5 mm. Enlarge flag and sun, or add a visible flag. Also p34 is more than 40 percent empty (house page ends after the table). If the page can be filled (move No.2 up) a page is saved; otherwise accept.
- **M1-3. L5 No.4a (queue of 20), p25:** the "front" label collides with circle 1 and the numbers 1-20 under the circles let a child just count circles behind Mei (13). Acceptable for age 6-7 as the model; move "front" left of the row. Optional: remove the printed numbers 8-20 if you want the subtraction.
- **M1-4. L10 No.3 (pet graph), p51:** dog and bird icons touch or overlap (bird row in particular), which makes counting 5 birds harder in B&W. Reduce icon size by 10 percent or increase spacing. Counts are right (dog 4, cat 7, fish 3, bird 5).
- **M1-5. L7 No.1 / No.4:** house and triangles are 1.3 times bigger, not 1.5 times as in the original audit request (builder reports this). Acceptable.

### Level 2
- **M2-1. L9 balances (No.1, p48; T1 and T3, p51; C6, p53):** "Scale 1" / "Scale 2" captions are cut off at the bottom of the SVG (top half of the letters only), on all four balance figures. The pans of Scale 1's right side and Scale 2's left side touch each other, and on T1 the two top lemons sit on the beam. Enlarge the viewBox height by about 20 units and add 10 units between the two scales.
- **M2-2. L9 balances: weight labels "100g", "300g", "500g" are 7.1 pt (6.7 pt in print).** They are the data of T3 and C6 (also in the text, so the question stays solvable). Enlarge to at least 9 pt (make the weight icon bigger).
- **M2-3. L9 C7 time line (p53, Go further No.7):** the label "8:15 am" under the tick is cut off (only the tops of the digits show). Increase viewBox height.
- **M2-4. L9 T2 time line (p51):** "? min / ? h / ? min" labels sit directly under the question text line; fine but tight. Add 8-10 units of space above.
- **M2-5. L6 T1 (Ben's money), p35:** the row label is clipped at the left ("en's money"). Widen `labelW` or shorten to "Ben". The bar is to scale (kite half = $10 = $4 + $6) and so shows that the kite part equals the other two parts (it hands over the structure; acceptable for a Think harder).
- **M2-6. L5 No.3 and No.4 (bars), p26:** labels "At first", "Gave 24", "taken out", "left", "+ 15", "− 24" are 7.0-7.4 pt (6.6-7.0 pt printed). Raise to at least 9 pt (the bars have room: p26 is half empty).
- **M2-7. L3 No.3 (pen of 7 hens), p15:** the seven bird icons overlap and the caption is about 8 pt. Space the icons (spacing 38 units for 34-unit icons leaves no gap).
- **M2-8. L3 T1 (bicycle and tricycle), p18:** captions "bicycle: 2 wheels", "tricycle: 3 wheels" are 7.8 pt. Raise to 9 pt or more.
- **M2-9. L8 No.4b grid, p44:** the dashed grid is pale; in B&W print it is almost invisible. Use a darker grey (about 40 percent) for the grid lines.
- **M2-10. L7 No.3 (also see H5):** the page is not the issue, but the page break leaves p39 (No.5, No.6) and p40 (investigation) partly blank; fine.
- **M2-11. Tutor guide page references, L6 take-home line:** the guide says "Page 1: Q1 last row and Q2(b); Page 2: Q3(b) and Q4(b)". In the new layout Q1 is page 1, Q2 and Q3 are page 2 and Q4 is page 3. Update `p2/content/l6.js` takehome text (Q2(b) is now on page 2, Q4(b) on page 3), then rebuild the guide.

### Level 3
- **M3-1. L5 No.1 (47 counters), p24:** the bottom row of counters is sliced flat (the fourth counter in each column of 4 is cut in half) in colour and B&W. All 47 are still countable, but it looks like a rendering fault. Increase the SVG height by about 12 units.
- **M3-2. L9 C5 (bottle bar), p49:** the brace label "1 kg 200 g" is cut at the top (upper part of the letters missing) and touches the question text. Increase top margin.
- **M3-3. L9 T3 (box and four books), p48:** the bar is not to scale: the "250 g box" segment is 2.5 times as wide as one book (book = 200 g, so it should be 1.25 times). Redraw the box segment at 1.25 book widths, or add "not to scale". Every other L3 bar model checked is to scale.
- **M3-4. L9 No.4 (24-hour strip), p46:** the label "pm" sits on the dotted pattern and is hard to read in B&W. Put the label in a white box. Axis tick spacing is correct (12:00 exactly in the middle).
- **M3-5. L10 No.3 (queues), p52:** the figure nearly solves both parts: (a) shows Ben twice, 3 circles in front row and 5 in the back row, with a dashed line between the two Ben circles (the answer 7 is 3 + 5 − 1, visible by counting); (b) shows "1st, 2nd, 3 people between, last" (the answer 6 is a count). Also the dashed connector in (a) strikes through the label "3rd". Acceptable as a "Draw it!" model but consider removing the printed ordinals from part (b) to leave one step to the child; move the "3rd" label so the dashed line does not cross it.
- **M3-6. L8 No.2 shapes A-D, p39:** the four shapes are only 11-16 mm across and the letter labels 8.1 pt. The child must test every corner with a right-angle checker; enlarge by about 1.5 times (as done for No.1 and No.3). Geometry itself is exact (house roof angle is 90 degrees, A has 8 right angles, B has 6, C has 3, D has 2).
- **M3-7. L8 Investigation No.8 (staircases), p44:** captions "1 step / 2 steps / 3 steps" are 6.8 pt. Raise to 9 pt.
- **M3-8. L4 No.1 / No.2 bar labels, p18:** the bar labels "Mei", "345", "Ali", "128", "Ravi", "Siti", "248 beads" are 8.2-8.4 pt (7.7-7.9 pt printed). Raise to 9 pt or more.
- **M3-9. L4 No.5 (p19):** the "?" label of Siti's dashed part is crossed by the vertical dashed "same number" line. Move the "?" off the line.
- **M3-10. L7 No.6 grids (p35):** the two L-shape grids are about 3 mm per cell (22 mm wide figure), too small to draw and shade a square in. Not changed by the builder, but this question needs the figure; enlarge to at least 5 mm per cell.
- **M3-11. Pages almost empty (whole-page cost):** p21 (L4 T4 alone), p40 (L8 No.3 alone, 60 percent empty), p47 (L9 No.6, 60 percent empty), p53 (L10 No.6 alone). Level 2: p5 (No.6 alone), p11 (No.6 alone), p29 (L5 T4 alone), p34/p52. Builder already lists p21 (L3) and p29 (L2) as the two cheapest to give back. If printing cost matters, folding one question up on each saves a sheet per two pages; otherwise accept.

---

## LOW

- **L1-1.** L9 No.3 (desk and spans, p46): the two strips have different cell widths, so the figure itself shows the answer to "Whose span is longer?" (Ali's cells are bigger). The text already gives 6 and 8 spans, so the reasoning is still needed. Labels "Ali: 6 spans / Mei: 8 spans" are about 7 pt.
- **L1-2.** L9 No.6 (ruler, p47): "12" at the right end touches the ruler border. Scale spacing is uniform (40 px per cm), pencil 0 to 12, crayon 3 to 8 are drawn exactly right.
- **L1-3.** L3 picture graph (p13): banana icons are thin outlines and look faint in B&W. Counts are right (6, 5, 8, 3, 5).
- **L1-4.** Number lines 0-20 (L1 No.3, p3): numbers 10-20 are close together but legible (about 11 pt).
- **L3-1.** L1-3 print files are scaled to 0.9429: every size above is 5.7 percent smaller in print (a 9 pt label prints at 8.5 pt). Keep that in mind when setting the new minimum (use 10 pt on the page for labels that carry data).
- **Deck and tutor guide text:** nothing in the guides quotes the question wording for the changed items (guides carry the keys only, all verified unchanged). Decks still show the older, smaller figures where a deck copies a workbook figure (builder reports this); not a conflict, but the L1 and L2 decks should not be said to "match the workbook" for the changed pages.

---

## What I checked and found correct (re-solved by hand, figure against key)

Level 1 (key in `hp/lessons.js`):
- L1 No.3 frog lines: first hop 0 to 4 correct, second line empty, key "both land on 20" correct. No.5 stickers: box 1 two stars, box 2 five stars (2 + 3), table 2, 5, ... Box 10 = 29, key correct.
- L2 No.6: bars "smaller ?" and "bigger ? + 2", total 10: answer 4 and 6, key correct.
- L3 Part A graph (apple 6, banana 5, orange 8, grape 3, watermelon 5): Q1 orange, Q2 grape, Q3 5 more, Q4 banana and watermelon, Q5 27, all correct. T1 (blue 5 stars = 10), T3 (pizza 3 pictures), T4 (3 and a half = 7) correct against the key; only the key box is clipped (H1).
- L4 No.1 to No.6, T1 (14th = triangle), T2 (10), T3 (20th = blue), T4 (6 squares, 1 stick left), C2 (21, 28; 10th = 55): all rows match text and key. Counters carry R / B letters so B&W works.
- L5 No.3 grid (Ali 8 shaded, Mei 13, Ben 7), No.4a (queue of 20, Mei 7th, 13 behind), T1 (14), T2 (15), C2 (snail on day 4): correct.
- L6 coins: all values with cents correct (5¢, 10¢, 20¢, 50¢, $1 coin, $2, $5, $10, $50 notes); No.5 = 35¢, No.6 = 45¢, No.3 (4 coins: 50 + 20 + 10 + 5), No.4 (no, 35¢ needs 3 coins: 20 + 10 + 5), L10 No.4 (20 + 10 + 10 + 5 + 5 = 50¢, 35¢ = 20 + 10 + 5): correct.
- L7 No.1 (circle 1, triangle 2 including the flag, square 3, rectangle 2: 8 shapes), No.4 (A 3, B 2), No.6 (5): correct.
- L9 No.1 ribbons 7, 5, 9: C longest, B shortest, 2 more, 12 units, C minus 2 = A: correct. No.4 (10 erasers, 6 clips), No.5 (Ali 11, Ben 6, total 25), No.6 ruler: correct.
- L10 No.3 (7 cats, 5 birds, 19 pets, cat and fish = 10): correct.

Level 2 (key in `p2/content/l*.js`):
- L1 T3: 46 ten-blocks (23 + 23) against 3 hundred-blocks and 15 ten-blocks = 460 against 450 (Ali by 10): correct.
- L2 No.6: bars 700, +200: 250 and 450: correct. No.5 triangles: correct.
- L3 No.3 (7 hens, start of the table), No.4 (23 stars, 5 each, 3 left over), No.5 (28 children, 6 vans, 2 empty seats): figures match.
- L4 No.1-No.5, T1-T4, C6 (towers 2, 5, 8), C7 (frogs): pattern rows, groups of 5 and 4, tables and house sticks 5, 9, 13 all match.
- L5 T2 (36), T3 (36), T4 (Ali 9, Ben 14, Siti 17), No.3 (59), No.4: bars proportional and correct.
- L6 No.1 (prices), No.2, No.3 (counting-up lines: 65¢ to $1 = 35¢; $26 to $50 = $24), No.4 (tags $9 / $3 / $14 / $8), No.5 (25¢ + 30¢ + 45¢ = $1.00), No.6 (20¢ and 50¢ tags): correct.
- L7 No.3 and T2/T3 bars: equal lengths, right shading (but see H5). No.4 bars cut into 5, 8, 12, 6, 10: correct.
- L8 No.1-No.5: robot counts, 4 by 4 grid, stacks A 5, B 8, C 14, nets A (cube), B (not), C (cube), D (not), E / F: all match the key; Q4b shape is 5 squares (row of 4 and one above).
- L9 No.1 (melon 400 g, apple 200 g, lemon 50 g, 8 lemons), No.4 (ribbon), No.5 clocks (A 7:25 am: hour hand 222 degrees, minute hand on 5; B 4:50 pm: minute hand at 10, hour hand 145 degrees: both correct and to scale; swimming ends 5:25 pm; trip 45 min), T1, T3 (apple 100 g, pomelo 300 g), C6 (cube 100 g, ball 200 g), C7: correct.
- L10 No.1 picture graph (4, 6, 3 pictures of 5; Thursday 5 pictures = 25), No.5 bar of 10, No.6 towers: correct.

Level 3 (key in `p3/content/l*.js`):
- L4 No.1-No.6 (bars to scale: 486, 378, ? = 386; 345 / +128 / −79; 4 units of 62; 24 more and 150; 85 / 47 with the 66 line; $45 / $18 with +$10), T1 (Ben 24, Ali 72), T2, T3 (Box B 150, A 200, C 250), T4 (rice 6, flour 3), C7 (ribbon 90, 180, 205): all correct.
- L5 No.1 (47 counters: 11 columns of 4 and 1 of 3; 7 each, 5 left over): correct (but clipped, M3-1).
- L6 No.3 shapes A-E, No.5 (bar of 6), T2 (fifths and tenths equal length), T3, T4 (thirds, sixths, twelfths equal length), C6 (pieces to scale: 1/2, 1/4, 1/8): correct.
- L7 No.1 (A 8 cm2 / 12 cm, B 8 / 14, C 9 / 12, D 5 / 12) and No.4 (L shape 58 cm2, 34 cm), No.5 (staircase 10 cm2 / 16 cm): drawn exactly.
- L8 No.1 angles (measured from the rendered page: a 90, b 45, c 121, d 90, e 147, f 60 degrees; key smaller b, f, right a, d, bigger c, e), No.3 fan (6 lines = 15 angles), No.5 (AB 1 right 1 up, EF 2 right 1 up, G on the middle of EF), T3 eleven clocks (hands at 1:00 to 11:00 correct), No.8 staircases: correct.
- L9 No.1f (65 cm times 4 = 260, 40 cm left), No.3 (shopping list prices), No.4 (strip to scale), No.5(a) (1 h 25 min), No.6 (buses 06:40, 07:05, 07:30, 07:55, 08:20; ticks every 25 min, Ravi at 08:15 five minutes before 08:20: scale correct), T2 (09:30 to 21:00: 11 h 30 min; ticks to scale), T3 (book 200 g), C5 (bottle 300 g), C6 (pen $1.60, file $2.20): figures match.
- L10 No.1 (45, 30, 55, 20; Lime 50; Milo + Kopi = 100: values and four hatch patterns correct and readable in B&W apart from H2), No.2, No.3 (answers 7 and 6), No.4, No.5 (13, 16, 19; 25 sticks; 10 squares): match.

B&W check: every changed figure uses outline plus hatch, dot or letter plus a label; none relies on colour alone (R / B counters, dotted vs hatched bars, "kite (half)" labels). Fill greys are distinguishable. The only B&W weak points are M2-9 (pale grid), M3-4 ("pm" on dots) and L1-3 (faint bananas).

Layout check (colour and B&W): no content running off a page or into the footer; no collisions apart from those listed; no unwanted blank page; the cut-out sections start on front pages in all three print files.

## Fix list in priority order (all in the figure files, rebuilds of three workbooks and print files)

1. H1 L1 L3 T1 key box (`hp/figs_l1_3_l1.js`).
2. H2, H3, H4 and M3-1, M3-2 in `p3/figs_l3.js` (and `p3/content/l10.js` if the sticks caption lives there).
3. H5 in `p2/figs_l2.js` (L7 No.3).
4. M2-1, M2-3, M2-5 (viewBox and labelW) in `p2/figs_l2.js`; M2-2, M2-6, M2-8, M3-7, M3-8, M1-1 label sizes at least 9 pt.
5. M2-11 guide page references (L6 take-home), rebuild the Level 2 tutor guide only if you accept the guide change.
Then re-run `print/make_print_l1_3.py --check` and look again at p16 (L1), p38 and p48-p53 (L2), p24, p46, p49, p51, p52 (L3) in colour and B&W.
