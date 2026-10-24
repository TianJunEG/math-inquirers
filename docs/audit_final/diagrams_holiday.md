# Holiday workbooks: diagram audit (Levels 1-6)

Read-only audit, 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`.
Scope: the six holiday student workbooks, colour print PDFs `outputs/print/Math_Inquirers_P{1..6}_Workbook_PRINT.pdf` (64 / 70 / 64 / 76 / 62 / 58 pages). Strategy card and look-back (spine) work excluded.

Page numbers below are PRINT PDF page numbers. Question ids are "No.n" (Start here pages), "T" / "A" / "think-harder" and "C" / "B" / "go-further" pages keep the numbering shown in the workbook.

## Method and honesty note

- Every Start-here, Think-harder and Go-further page was rendered at 70 dpi (4-up contact sheets) and looked at. Text was extracted with `pdftotext -layout` and read for every question.
- Investigation pages and look-back boxes were read but not graded (they are open prompts with no figure need beyond what is on the page).
- Counts are tallies of numbered questions (a question with parts a-e counts once; class priority is D, then A, then B, then C). They are accurate to about +/-4 per level. The item lists below are exact, the totals are my tally.
- I did not open the .docx/.js source for every question. Where I say a figure is "missing" I checked the rendered page.

## Summary per level

| Level (age) | Questions | A needed | B would help | C fine as text | D fault in an existing figure |
|---|---|---|---|---|---|
| P1 (6-7) | 138 | 24 | 28 | 80 | 6 |
| P2 (7-9) | 126 | 26 | 30 | 65 | 5 |
| P3 (8-10) | 140 | 34 | 28 | 72 | 6 |
| P4 (9-11) | 130 | 26 | 28 | 69 | 7 |
| P5 (10-12) | 125 | 24 | 26 | 68 | 7 |
| P6 (11-13) | 129 | 22 | 26 | 76 | 5 |
| Total | 788 | 156 | 166 | 430 | 36 |

Pattern across levels:
- P1 and P2 have good figures where a figure was chosen (house, ribbons, ruler, number machine strips, bar models, fraction bars, balances, jugs). They fail where the owner's feedback already points: patterns, sharing, boxes of stickers, coins (no coin pictures anywhere in the question pages), picture graph made of bare dots.
- P3 is the weakest on bar models: Lesson 4 is called MODEL MAKERS but Q4-Q6 and all Think-harder questions say "Draw your model here" with only blank space, and Lesson 9 (time, money, length) has no time line, clock, ruler or coin at all.
- P4 and P5 are the best-drawn levels (number lines, bar models, compass, nets, graphs, tank figures). Their faults are size and legibility (figures 2-4 cm wide) and word problems that say "Draw a bar model" on a blank box.
- P6 shows code blocks as figures (good) but has few maths diagrams for clock arithmetic, stars, dot plots, probability spaces.

## Figures that exist and are good (keep, reuse as the house style)

P1 L5 No.1 and No.3 (number-machine strip, marble bars), P1 L9 No.1, No.3, No.6 (ribbons, spans, ruler 0-12 with crayon starting at 3), P2 L2 No.4-5 (magic square, triangles), P2 L5 No.3-4 (bars), P2 L7 No.2-6 (fraction bars), P2 L9 No.1 (balances), P3 L3 No.3 (array split), P3 L4 No.1-3 (bar models), P3 L6 wall, P4 L4/L5 (quarter line, hundredth line, cans on scale), P4 L6 compass, P4 L8 nets, P5 L3 No.1-2 (partial bars), P5 L5 tank, P6 L3 No.3 (sea level).

---

## A and D items by level

Priority: High = a child could not start without it (or the figure is missing or wrong); Med = the child can start but will be slow or wrong; Low = nice.

### Level 1 (P1, ages 6-7)

| # | Lesson, page | Q | Class | What the diagram should show | Figure type | Pri |
|---|---|---|---|---|---|---|
| 1 | L4, p18 | No.4 (a-d) | A, MISSING | Text says "The pattern keeps going in the same way" but NO pattern is printed on the page. Print a row of places 1-9 (e.g. cat, dog, dog / cat, dog, dog ...) with numbers under, and empty boxes to 12 and a cut-off. | picture row | High |
| 2 | L1, p4 | No.5 | A (owner feedback) | 4-5 sticker boxes in a row: Box 1 with 2 star stickers, Box 2 with 5, then "+3" arrows; boxes 3-4 empty to draw into; keep the table as the record. Use stickers (stars, hearts), not dots. | picture row + table | High |
| 3 | L1, p3 | No.3 | A and D | Number line 0-20 is 8-9 mm tall with 5 pt numbers. Redraw large, with a friendly frog on 0 and hop arcs of 4 above the line; second row of arcs of 5 for part a. | number line with arcs | High |
| 4 | L4, p18 | No.2, No.3 | A | Row of circle / square / triangle (and red / red / blue counters drawn as filled shapes so it works in B&W) with place numbers 1-10 and the "core" bracketed after the first run. | picture row | High |
| 5 | L4, p19 | No.5, No.6 | A | Cat, dog, dog picture row (animal faces); A B C D A B C letter tiles. Places numbered. | picture row | High |
| 6 | L6, p28 | No.1 | A | Coin pictures with cents printed on each (20c, 10c, 5c) as the column headers of the table; row cells show the coins as they are written. Do not rely on the cut-out page only. | coins | High |
| 7 | L6, p28 | No.2, No.3 | A | 20c / 10c / 5c / 50c coins drawn in a tray; for 85c show a blank "purse" strip with 85c on top for the child to place coins. | coins | High |
| 8 | L6, p29 | No.4, No.5, No.6 | A | Ali's coins drawn (20c, 10c, 5c); Mei's two 20c and one 5c; Ben's 35c question with two empty coin circles. | coins | High |
| 9 | L10, p48 | No.4 | A | One 20c, two 10c, two 5c coin pictures with cents printed. | coins | High |
| 10 | L9, p44 | No.4 | A | Clip strip: desk = 5 clips; erasers: 1 clip = 2 erasers, drawn as paired strips (clips above, erasers below). Pencil = 12 erasers. | strip | High |
| 11 | L9, p44 | No.5 | A | Mei's pencil 8 cubes as a cube strip; Ali's 3 longer; Ben's 2 shorter, drawn end to end on the same baseline. | strip / bar | High |
| 12 | L5, p24 | No.4a, 4b | A | A queue of 20 faces (or a row of 20 circles) with Mei's marked at 7th; for b, a row of 5 empty circles with Ali in the 3rd place from each end. | picture row | Med |
| 13 | L8, p38 | No.1a-c | A | Three children of different heights side by side (a); cat / dog / hen sized figures (b); four ribbons of different lengths (c) as the child sorts, with empty slots. | picture row / strips | Med |
| 14 | L2, p9 | No.6 | A | Two bars (10 in total, one 2 more) as a strip of 10 squares split in a bar model. | bar model / strip | Med |
| 15 | L3, p13 and L10, p48 No.3 | picture graphs | D | Rows use plain coloured dots, not picture symbols; the key is a black dot; fruit names in the row labels, but identity is carried by colour only (fails B&W). Draw the actual fruit (apple, banana, orange, grape, watermelon) and pets (dog, cat, fish, bird) as the symbol; key shows "1 symbol = 1 child". | picture graph | High |
| 16 | L3, p16 | T1-T4 | A | 1 picture = 2 children: show the three coloured/patterned rows (red 3, blue 5, green 4), a half picture for T4, and a blank row with a key for T3. No figure is printed at all. | picture graph | High |
| 17 | L3, p16-17 | T4, C2 | A | Half picture and key drawn; C2 rows for A/B/C partly drawn. | picture graph | Med |
| 18 | L6, p31 | T5 | A | $1, $2, $5, $10, $50 notes drawn with values; toy $17, bicycle $65, helmet $8 on price tags. | notes and coins | Med |
| 19 | L4, p21-22 | T1, T3, T4, C1, C2 | A | Bead rows (red blue blue / red red blue ...) with place numbers; squares-and-sticks row (4, 7, 10) for T4 and dot rows (1, 3, 6, 10, 15) for C2. | picture row | Med |
| 20 | L5, p26-27 | T1, T2, C2 | A | T1 / T2 as number-machine strips like No.1; C2 snail on a 9 cm wall as a stepped ladder with day / night arrows. | machine strip, route | Med |
| 21 | L10, p52 | C2 | A | Ali / Ben / Mei sticker bars (Ben = Ali + 4, Mei = Ben - 3, total 29). | bar model | Low |
| 22 | L7, p33-34 | No.1, No.4 | D | House picture is 45 mm wide, shape icons in No.2 are 8 mm; triangles in No.4 (A and B) are drawn with no unit squares. Make 1.5x larger, add count dots. | shapes | Med |
| 23 | L9, p44 | No.6 | D | Ruler 0-12 is 5 pt numbers; pencil on 0, crayon from 3: labelled correctly, but ticks are 1.5 mm. Enlarge, add 1/2-cm ticks only if needed. Keep the "not starting at 0" crayon. | ruler | Low |
| 24 | L1, p3 | No.1-No.2 | B, plus the row | See B list. | | |
| 25 | L8, p38 | No.2 | D | Venn loops have heads "Numbers less than 6" and "Odd numbers" but the question text never says what the loops are. Put the loop labels into the question text and give number cards 1-10 to place. | Venn | Low |

P1 B list (diagram clearly helps): L1 No.1, No.2 (skip counting on a strip of 20 with jump arcs); L2 No.1, No.2 (ten frame or two-colour counters for bonds of 10); L2 No.3 (bond of 10 ladder to 20); L2 No.4 (balance scale for "="); L2 No.5 (magic triangle exists, add a counters tray); L2 No.T2 (two pockets); L4 No.7 and No.8 (sticks pictures only reach 3 triangles; extend to 4-5, and for No.8 a bundle of 15 sticks); L4 T3 and T4 (squares of sticks); L5 T1, T2 (before/after strips); L6 T1-T4 (coin trays); L7 T1, T2, T3 (draw-on-grid scaffold); L8 T1 (race order lanes), T2 (three toys); L9 C1, C2 (train and ribbon bars); L10 No.2 (two bars), C2.

### Level 2 (P2, ages 7-9)

| # | Lesson, page | Q | Class | What the diagram should show | Figure type | Pri |
|---|---|---|---|---|---|---|
| 1 | L3, p16 | No.4 | A | Four friends (faces) with 23 counters, dealt one at a time; blank plates for the child; 3 left over region. The Tip says "draw 4 friends" so draw them. | sharing picture | High |
| 2 | L3, p16 | No.5 | B/A | Six vans of 5 seats as a row of seat boxes; 28 children as dots. | picture row | Med |
| 3 | L3, p16 | No.6 | B | Chairs in rows grid (2 rows of 10 to 10 rows of 2). | array | Med |
| 4 | L3, p15 | No.3 | B | Pen with 7 animals: hens (2 legs) swapped for goats (4 legs) as picture row under the table. | picture row | Med |
| 5 | L2, p11 | No.6 | A | "Draw a model: two bars, the long bar is 200 longer": give two bars with the 200 overhang marked and 700 total brace. | bar model | High |
| 6 | L5, p28 | T2 (Ben $15 book, dad gives as much as left) | A | Bars: start, after the book, after the gift ($42); "?" on each. | bar model | High |
| 7 | L5, p28 | T4, T3 | A | T4: three bars (Ali, Ben +5, Siti +8; total 40). T3: Siti's beads halved and +12 bar. | bar model | Med |
| 8 | L6, p30 | No.1 | A | Price table: show each item as a price tag with a small picture (curry puff, notebook, umbrella, bicycle); "notes and coins I use" cells show note/coin outlines to place or draw into; coins printed with cents ($1.65 as $1 + 50c + 10c + 5c). | coins and notes | High |
| 9 | L6, p30 | No.2 | A | $5 / $2 notes and $1 coins drawn, with stack of $8 target. | notes and coins | Med |
| 10 | L6, p31 | No.3 | A | Change: number line or counting-up strip from 65c to $1; and from $26 to $50. | number line / coins | High |
| 11 | L6, p31 | No.5 | A | Bar: 45c + 30c + 25c left. | bar model | Med |
| 12 | L6, p31 | No.6 | B | 20c stickers and 50c erasers as coin / tag pictures. | coins | Med |
| 13 | L6, p33-34 | T1, T3, C1 (halves of money) | A | Money bar cut in half (T1), coin sets (T3), double-halving bar (C1). | bar model | Med |
| 14 | L7, p35 | No.3 (compare fractions) | A | Pairs of equal-length bars: 1/3 v 1/8, 5/9 v 7/9; "smallest first" four bars. The text says "draw bars" but none are printed. | bar models | High |
| 15 | L7, p38 | T2, T3 | A | Two bars 3/8 v 3/5; bar of 8 with 3 + 2 shaded and wrong 5/16 attempt. | bar models | Med |
| 16 | L7, p39 | C5, C6 | A | 12-piece strip; 10-piece strip for three children. | strip | Low |
| 17 | L4, p21 | No.4 | B | Show 6 flowers as a picture row; 5 petals each in two flowers; only one flower drawn now. | picture row | Med |
| 18 | L4, p23-24 | T4 (houses), C6 (towers), C7 (frogs) | A | Houses of sticks 1, 2, 3 (same style as P5 L9); towers 2, 5, 8 cubes; two frogs on a number line 0-30 with arcs (jump 4 from 0, jump 3 from 2). | picture row, line | Med |
| 19 | L1, p3 | No.1 and T3 | B / A | Base-ten blocks: flats, rods, units, 15 tens (T3: 46 ten-blocks; 3 hundred-blocks and 15 ten-blocks). | place value blocks | Med |
| 20 | L9, p48-49 | T1, T3, C6 | A | Balance pictures with apples, lemons, pomelo, cubes, 300 g weight, as in No.1. | balance | Med |
| 21 | L9, p48-49 | T2, C7 | A | Time lines: 10:45 to 12:10; three lessons 35 min and 10 min breaks from 8:15. | time line | Med |
| 22 | L8, p43-44 | T1, C5, C7 | A | Cube stack layers drawn (T1: 4x3, 3x2, 1), pyramid layers 1,4,9,16 (C5), 3x3x3 painted cube (C7). | cube stack | Med |
| 23 | L10, p53-54 | T1, C5 | A | Picture graph with symbols and key (5 children per picture), mango row missing; football 6, swimming 4, lost key. | picture graph | Med |
| 24 | L9, p46 | No.5 | D | Clocks A and B are ~14 mm across; numerals 3 pt; the red minute hand is the same weight as the hour hand ("short thick = hour" is legible but the face is too small to read to the minute). Enlarge to 35 mm. | clock | High |
| 25 | L9, p45 | No.1 | D | Scales and fruit are ~25 mm wide; apple, lemon, melon hard to tell apart in B&W. Add labels under fruit. | balance | Med |
| 26 | L10, p51 | No.6 | D | Tower 1-3 pictures are 6 mm wide and stacks of 4, 8, 12 cubes cannot be counted. Redraw at 3x size. | cube stack | Med |
| 27 | L8, p41 and p43 | No.4, T3 nets | D | Nets A-D and E-F are 18 mm; squares cannot be folded in the head. Print 2x size. | net | Med |
| 28 | L3, p18 | T1 | D | Bicycle and tricycle drawn, tricycle shows 2 back wheels in perspective (reads as 3 wheels but cramped). Fine but small. | picture | Low |

P2 B list: L1 No.1 (blocks), No.5 (jump arcs on the 1000 chart); L2 No.1-No.2 (column sums are fine as is); L2 T1 (triangle drawn); L3 No.1 array is drawn (fine); L5 No.1, No.2 (machine strips exist; tables fine); L6 No.4 price tags exist; L6 C5, C6 (coin tray); L7 No.1 shapes exist; L8 No.2 exists; L9 No.4 ribbon exists and is in proportion (blue 46 : red 64 checked); L9 C5-C6 balances.

### Level 3 (P3, ages 8-10)

| # | Lesson, page | Q | Class | What the diagram should show | Figure type | Pri |
|---|---|---|---|---|---|---|
| 1 | L4, p19 | No.4 (Ali 24 more than Ben, total 150) | A | Two bars with the 24 difference marked, total brace 150, "?" on each. Currently a blank "Draw your model here". | bar model | High |
| 2 | L4, p19 | No.5 (Mei 85, Siti 47, equal) | A | Two bars with the gap and halfway mark (the difference is split in two). | bar model | High |
| 3 | L4, p19 | No.6 (Ali $45, Ben $18, plus $10 each) | A | Before and after bars with +$10 on both and the gap unchanged. | bar model | High |
| 4 | L4, p20-21 | T1, T2, T3, T4, C6, C7 | A | T1 3 times as many (96 total); T2 Siti 54 more, equal share; T3 Box A, B, C with +50 steps (600); T4 rice 3 kg heavier (9 kg); C7 ribbon pieces 475 cm. | bar models | High |
| 5 | L9, p43 | No.1f, T3, T4 | A | 3 m ribbon with four 65 cm pieces (bar with remainder); 1 kg 50 g box with 4 books and a 250 g box. | bar model | Med |
| 6 | L9, p44 | No.5 | A | Time lines: 3:45 pm to 5:10 pm jumping to 4:00, 5:00; 4:35 pm + 50 min; film 1 h 50 min ending 9:15 pm. The question says "draw a time line" but gives none. | time line | High |
| 7 | L9, p44 | No.6 | A | Bus time line 06:40 + 25 min steps, with Ravi's 08:15 marked; school at +35 min. | time line | High |
| 8 | L9, p44 | No.4 | A | 24-hour clock: two 12-hour face clocks beside a 24-hour dial or a 0-24 strip. | clock / strip | Med |
| 9 | L9, p45 | T2, T4, C5, C6 | A | T2 shop hours on a time line; T4 bus timetable; C5 bottle bar (full / half); C6 pens and files bars. | time line, bar model | Med |
| 10 | L9, p43 | No.1, No.2, No.3 | A / B | Number lines: m and cm (3 m 6 cm); weights as four labelled bags on a kg scale; price tags with pictures ($7.85 book, $4.60 pen set ...) with coins. | line, tags | Med |
| 11 | L6, p29 | No.5 (fence 1/6 + 2/3) | A | Bar of 6 equal parts shaded 1 and 4; "Draw a bar" given. | bar model | High |
| 12 | L6, p29 | No.2, No.4 | B | Paired bars for the comparison and addition (wall at the back is the only help). | bar models | Med |
| 13 | L6, p30-31 | T2, T3, T4, C6 | A | Bars for 3/5 v 7/10; book read 1/4 then 1/2; ordering three fractions; five 1/2, 1/4, 1/8 pieces filling a whole. | bar models | Med |
| 14 | L5, p23-25 | No.2, No.3, T1, T4 | B | Counters grouped in nines (minibuses), bags of 8 (draw them is already said), boat loads. | picture groups | Med |
| 15 | L10, p49 | No.3 | A | Queue rows: Ben 3rd from front, 5th from back (7 in queue); Ali 2nd, Siti last, 3 between. | picture row | High |
| 16 | L10, p48 | No.1 | D | Bar graph: Teh bar is pale blue / white (fails B&W and on the print copy it is almost invisible), y-axis numbers 5 pt, bars carry no value labels, the missing Lime juice slot has no outline. Use patterns, bigger axis, dotted outline for the missing bar. | bar graph | High |
| 17 | L10, p51 | C7 | A | Bar graph of paper collected by 4 classes. | bar graph | Low |
| 18 | L7, p33 | No.1 | D | Figures A-D are 25 mm wide, grid squares 3 mm; the child must count squares and perimeter from this. Enlarge 2x, label A-D inside. | grid shapes | Med |
| 19 | L7, p33-35 | No.2, No.3, T1-T4, C6, C7 | A | Garden rectangles (18 m fence) as outlines on a grid; a square and 7x3 rectangle; rectangle 12 cm and perimeter 30; 6 cm square cut in two; corner-cut rectangle. | rectangles, grid | Med |
| 20 | L8, p38 | No.1, No.2, No.3 | D | Angles a-f are 10-12 mm with tiny arcs; the right-angle checker comparison cannot be done at this size. Lines from O in No.3 are 15 mm. Enlarge to 30 mm arms. | angles | Med |
| 21 | L8, p40 | T3 | A | Clock faces at 1-11 o'clock for sorting into angle groups. | clock | Med |
| 22 | L1, p4 | No.4 | B | Base-ten blocks: thousand cube / hundred flat / ten rod / one unit for 4 thousands, 15 hundreds. | blocks | Med |
| 23 | L5, p23 | No.1 | OK | Plates and counters already drawn; keep. | | |
| 24 | L10, p50 | T1 | B | Three coins 10c, 20c, 50c drawn with cents. | coins | Low |

### Level 4 (P4, ages 9-11)

| # | Lesson, page | Q | Class | What the diagram should show | Figure type | Pri |
|---|---|---|---|---|---|---|
| 1 | L3, p16 | No.6 (3 times as many chicken rice, 124 plates) | A | Bar model skeleton: laksa 1 unit, chicken rice 3 units, total 124 with brace. The text says "Draw a bar model" on a blank. | bar model | High |
| 2 | L4, p21 | No.5 (3/5 red, 27 red) | A | Bar of 5 parts, 3 shaded = 27, "?" total. | bar model | High |
| 3 | L5, p26 | No.5 ($9.40, Mei $1.20 more) | A | Two bars with the $1.20 overhang, total brace $9.40. | bar model | High |
| 4 | L10, p54 | No.6 (Ben and father 50 years, in 5 years 3 times) | A | Age bars now and in 5 years (before and after). | bar model | High |
| 5 | L10, p54 | No.5 (queue 7th from front, 12th from back) | A | Row of circles with Mei's circle in both counts, overlapping region. | picture row | Med |
| 6 | L6, p32 | No.3 (clock angles) | A | Two clock faces (4 o'clock, 7 o'clock) with 12 spaces marked and an arc; "find both times for 30 degrees" with a blank clock. | clock | High |
| 7 | L6, p35-36 | T2, T3, C5 | A | Clocks for 10, 2 o'clock; 7:15 to 7:50 minute-hand sweep; clock for the puzzle. | clock | Med |
| 8 | L6, p30 | No.1 | D | Angles a-d are about 25 mm with arms 12 mm; the text itself says "the arms are short: draw them longer with a ruler" so the angle cannot be measured. Print with arms 40 mm and a vertex dot, or provide the protractor cut-out. | angle + protractor | High |
| 9 | L3, p16 | No.5, T1, T4, C6 | A / B | Number-trick bar; T1 2340 beads (4 times); T4 trick as a bar; C6 half book / lunch / gift as a bar. | bar model | Med |
| 10 | L4, p23-24 | T5, T7, C5-C7 | A | Jar and pages bars (1/2 and 1/3 of sweets; 2/5 then half). | bar model | Med |
| 11 | L5, p29 | C6, C7 | A | $9.20 shared with +$0.50 and +$1.30 bars; jug full and half full on a scale. | bar, scale | Med |
| 12 | L9, p49 | No.3 (Ali and Mei money box graph) | D | Graph 55 mm wide, y-axis 4 pt, six weeks crowded, Ali circles/green line and Mei squares/red dashed line (shape plus colour: fine for B&W). Increase to 80 mm and add the point values to the grid. | line graph | Med |
| 13 | L9, p49 | No.5 (two shop graphs) | D | Both graphs are 40 mm wide with tick labels 4 pt; the point of the question is reading the scale, so make the scales legible (the whole point of the task). | line graphs | High |
| 14 | L5, p25 | No.1 | D | Number lines (a)(b)(c) are 60 mm wide, ticks unlabelled, numbers 5 pt. Label every 5th tick or give the step in the question. | number line | Med |
| 15 | L4, p21 | No.4c | D | 9 parts v 8 parts bars have labels 4 pt. Enlarge, mark 4/9 and 5/8 inside. | bar model | Low |
| 16 | L8, p43 | No.1, No.2 | D | Nets are 20-25 mm; E and F are 2-3 mm squares in print, hard to fold. Enlarge 1.7x. | nets | Med |
| 17 | L10, p53 | No.2 | B | Heads (18) and legs (50) farm as picture row with chickens and goats. | picture row | Low |
| 18 | L1, p3-5 | No.2, No.3 | B | Trees in rows (4 rows of 10) and bead packs as arrays. | array | Low |
| 19 | L2, p9 | No.1 | B | Number line 47 285 marked between 47 000 and 48 000 for rounding. | number line | Med |
| 20 | L7, p42; L9, p51-52 | C6, C7, T/C | A | Garden path crossing figure; tanks A and B (two lines crossing). | figure, graph | Low |

### Level 5 (P5, ages 10-12)

| # | Lesson, page | Q | Class | What the diagram should show | Figure type | Pri |
|---|---|---|---|---|---|---|
| 1 | L10, p48 | No.2 (Ali 1/3 book, $12 lunch, half gift, $15 left) | A | Bar: whole, 1/3 spent, $12, half of rest, $15 left; "?" whole. | bar model | High |
| 2 | L10, p48 | No.3 (Mei and Ravi $115, Ravi $10 more than 3/4 of Mei) | A | Mei 4 units, Ravi 3 units + $10 overhang, brace $115. | bar model | High |
| 3 | L10, p49 | No.6 and T1, B1 | A | Age bars now and later; Siti 2/5 then 1/3. | bar model | Med |
| 4 | L2, p9 | No.5 (Ravi 2/5 game, 1/2 of rest book, $36 left) | A | Skeleton printed as empty rectangle; give 5-part bar with the 2 shaded. | bar model | High |
| 5 | L3, p13 | No.2 | A | "Draw the Before model": supply Siti 3 : Mei 4 After bars and the +12 / -12 arrows. | bar model | Med |
| 6 | L3, p16-17 | A1, A2, A4, B1, B2, B3 | A | Fraction-remainder bars; red-bead fraction before and after (3/7 to 3/5); equal remainder. | bar models | Med |
| 7 | L6, p29 | No.4 (printers P 30, Q 20, 900 pages) | A | Two bars filling to 900 with P's 5-minute head start. | bar / strip | Med |
| 8 | L6, p31-32 | A1, A3, B1, B2 | A | Taps and a tank bar; car park half-hour time line; cats-fish table; candles side by side (heights vs hours). | bar, time line | Med |
| 9 | L6, p28 | No.2 | D | Three shop tags are 20 mm wide with 3 pt text ("Pack of 6 cans $4.20"); unreadable on print. Enlarge to 40 mm. | price tags | High |
| 10 | L6, p28 | No.3 | D | Tank with taps A and B and crack: text 3 pt, arrows tiny. | tank figure | High |
| 11 | L6, p29 | No.5 | D | Car park sign and half-hour line are legible, but tick labels (9.40, 10.40, 11.10 ...) are 4 pt. | time line | Med |
| 12 | L9, p43 | No.1, No.2 | D | Tables and houses figures are 15-20 mm per step with labels 3 pt "1 table" "2 tables". Enlarge. | picture row | Med |
| 13 | L5, p24 | No.4, No.6 | D | Tank-with-cubes figure is 40 mm; dimensions 3 pt; the 5 cubes picture is 12 mm. Container A and tank B (No.6) are 25 mm. | solid figures | Med |
| 14 | L7, p33 | No.2 | D | Price tags A and B text is 4 pt. | tags | Low |
| 15 | L7, p33 | No.3 (25% up then 20% down) | A | Bar $80 with +25% extension, then 20% cut; shows why 84 is wrong. | bar model | Med |
| 16 | L7, p34 | No.5 | B | Class of 40 pupils as a 10-block bar for girls / boys with glasses shaded. | table + bar | Low |
| 17 | L8, p38-39 | No.2, No.3, No.4 | D | Quadrilateral diagrams are 20-25 mm; the tick marks for equal sides (hatch) are only 1 mm. Enlarge 1.5x. | angle figures | Med |
| 18 | L4, p18-19 | No.1 | OK | "Drawings are to scale": checked heights; (b) height 12 is dashed with a square mark. Keep. | | |
| 19 | L1, p3-6 | | C | Digit-card questions: text is fine. | | |
| 20 | L9, p44-45 | No.3, No.4, No.5 | B | Ticket-price table of guesses (table exists); 30 coins; quiz scores as a number line stepping by 7. | table / line | Low |

### Level 6 (P6, ages 11-13)

| # | Lesson, page | Q | Class | What the diagram should show | Figure type | Pri |
|---|---|---|---|---|---|---|
| 1 | L8, p38 | No.1 (clock and calendar puzzles) | A | A 12-hour clock face with hour marks to place arrows on (8 + 7, 11 + 30) and a 7-day circle (Saturday + 100, - 30). | clock, day circle | High |
| 2 | L8, p42 | C7 (jumps of 5 and 4 on a clock) | A | 12-point circle with arrows. | modular circle | Med |
| 3 | L8, p38-39 | No.2, No.3, No.4 | A | The letter numbers (A = 0 to Z = 25) are in a table; add a Caesar wheel (two rings) or a strip with a sliding second strip: shift 7 on PIZZA. | alphabet strip / wheel | Med |
| 4 | L7, p34 | No.4, T4, C5 (stars) | A | Star polygons {5/2}, {9/4} drawn with the turn and point angle marked; two blank dot circles for {9/4} and the 20-point star. | star polygon | High |
| 5 | L7, p33 | Intro and No.2 | D | The "turn / inside angle" diagram is 30 mm wide with 4 pt text; the nonagon prediction box is 25 mm. Enlarge; give a 9-dot circle to draw on. | turtle figure | Med |
| 6 | L7, p36-37 | T3 (4-sided shape, turns 70, 100, 90), C6 (shapes round a point) | A | Quadrilateral path with exterior turns marked; squares, hexagon and 12-gon meeting at a point. | polygon | Med |
| 7 | L6, p29 | No.4 | A (exists) | Difference grid is printed and partly filled. OK. | | |
| 8 | L6, p31-32 | T2, T6, T7 (two dice sums, Mei v Ali dice, spinners) | A | 6x6 sample-space grid for T2 and T6; 3x4 grid for T7. | grid | High |
| 9 | L6, p28 | No.3 | B | Bag with 4 red and 6 blue counters. | picture | Low |
| 10 | L5, p24 | No.5 (routes) | D | The puddle P is a pale blue circle (colour-only cue), and the grid is 38 mm with 3 mm circles. Mark P with a cross or hatch, enlarge to 55 mm. | route map | Med |
| 11 | L5, p23-24 | No.1, No.2, No.4, T3, C6 | B | Tree diagram for T-shirts, shorts, caps; handshake dots (7 friends joined) for No.4; 6 x 6 matches grid for T3; domino table for C6. | tree, dots, grid | Med |
| 12 | L9, p43 | No.1, No.4 | A | Dot plot or bar of 4, 7, 2, 8, 9 with a mean line and the +/- distances marked; pocket money 7 pupils with $69 outlier as a dot plot, showing mean v median. | dot plot | High |
| 13 | L9, p43-44 | No.3, No.6 | B | Dot plots before and after each change; temperatures as a bar chart with the mean line. | graph | Med |
| 14 | L9, p46-47 | T1, T2, C7 | B | Mean "balance" bars (4 children 150 cm to 152 cm). | bar model | Low |
| 15 | L3, p13 | No.1 | D | Number line -10 to 10 is 70 mm wide, numbers 4 pt, A / B / C points are small circles in near-identical blue / white (colour cue). Enlarge and mark with letters above. | number line | Med |
| 16 | L3, p16-17 | T2 (diver -14 m, gull 9 m), C7 (levels B3 to 4 without a 0) | A | Vertical scale with the two heights; a building floor list L4, L3, L2, L1, B1, B2, B3. | vertical number line | Med |
| 17 | L3, p13 | No.2 | B | Temperature as a small line graph or thermometer strip. | graph | Low |
| 18 | L4, p21-22 | T3, C5-C7 | A | Machine flow diagrams (A: x2 then +10, B: +5 then x2), age bars for C6. | machine / bar | Med |
| 19 | L10, p52 | C6 | A | 8 x 8 spin-sum grid. | grid | Med |
| 20 | L2, p8-9 | No.2 (factor trees) | OK | Empty trees are printed and the right size. Keep. | | |

---

## Top 20 priority items overall

1. P1 L4 No.4 p18: the pattern is missing from the page (child cannot start).
2. P1 L1 No.5 p4: boxes of stickers as pictures (owner feedback, High).
3. P1 L6 No.1-No.6 p28-29 and L10 No.4 p48: coin pictures with cents (no coin appears in the questions at present).
4. P1 L3 p13 and L10 No.3 p48: picture graphs made of bare dots, replace with fruit and pet symbols.
5. P1 L3 T1-T4 p16: picture graph with 1 symbol = 2 children not printed.
6. P1 L4 No.2, 3, 5, 6 p18-19: shape, colour and animal pattern rows.
7. P1 L9 No.4, No.5 p44: clip / eraser and cube pencil strips.
8. P1 L1 No.3 p3: enlarge number line and add frog hop arcs.
9. P2 L3 No.4 p16: sharing 23 stickers among 4 friends.
10. P2 L2 No.6 p11 and L5 T2, T4 p28: bar models.
11. P2 L6 No.1-No.3 p30-31: notes and coins, change line.
12. P2 L7 No.3 p35: pairs of fraction bars.
13. P2 L9 No.5 p46: clocks far too small.
14. P3 L4 No.4-No.6 p19 and T1-T4 p20, C7 p21: bar models (the lesson is called Model Makers).
15. P3 L9 No.5, No.6 p44, T2, T4 p45: time lines and bus timetable.
16. P3 L6 No.5 p29, T2-T4 p30: fraction bars.
17. P3 L10 No.1 p48: bar graph fix (pale bar, 5 pt axis); L10 No.3 p49 queue.
18. P4 L3 No.6 p16, L4 No.5 p21, L5 No.5 p26, L10 No.6 p54: bar models on blank boxes.
19. P4 L6 No.3 p32 (clock angles) and L6 No.1 p30 (angles too small to measure).
20. P5 L10 No.2, No.3 p48, L2 No.5 p9, and the P5 L6 No.2-No.3 p28 tags and tank (illegible).

Next after these: P6 L8 No.1 p38 (clock and week circles), P6 L7 No.4 p34 (star polygons), P6 L9 No.1, No.4 p43 (dot plots), P6 L6 T2, T6, T7 p31-32 (sample-space grids), P4 L9 No.5 p49 (graph scales).

## Figure types the generators lack

Where figures live: P1 is built by `p1/build.js` (docx library) with PNG images from `hp/` (`dots_*.png`, `coins.png`, `cubestrip.png`, `house.png`, `venn.png` ...). P2-P6 use one hand-written inline SVG function per figure inside `p{n}/content/l{k}.js`, wrapped with `H.fig(...)` (131 uses); `hp/kit.js`, `p2/kit.js`, `p4/kit_extra.js` only draw the cut-out kit (coins, notes, fraction strips, clock, nets, graph grids). There is NO shared figure library: the same bar, number line and array code is retyped per lesson, with different sizes, line weights and font sizes, which is why legibility varies (3 pt to 9 pt text) and why the same missing item recurs.

Missing as a reusable function:
1. Picture-symbol pictograph (symbol image, key, half symbol) and a dot-plot. P1 graphs use plain dots.
2. Coin and note renderer that prints the value with the cent sign (the kit has coins in `hp/kit.js` but the lessons cannot place them in a question or in a table cell).
3. Clock face with hands at given h:m (only the kit clock in `p2/kit.js` and the 24 h dial are not parameterised), a time line with jumps, and a calendar / modular circle.
4. Number line with arcs / jumps and labelled ticks (every lesson hand-codes it, tick labels are often under 5 pt).
5. Bar model generator: units, brace, "?" , comparison overhang, before-and-after pairs, fractions of a bar (exists only as one-off drawings in P2 L5, P3 L4, P4 L4, P5 L3 - the blank "Draw your model here" boxes are the gap).
6. Picture row for patterns and queues (shapes, animals, counters, stickers with place numbers), array and sharing plates (P2 and P3 have one-offs), ten frame, part-whole bond, base-ten blocks.
7. Strip / ruler (start not at 0; the P1 L9 ruler is hard-coded 0-12), cube stack (isometric) from a layer list, balance scale.
8. Coordinate grid is not needed by the current content (none found).
9. Sample-space grid and tree diagram (P6), star polygon / turtle path, alphabet wheel.
10. A true B&W safe palette: shading uses yellow v pale blue in many figures; use hatch patterns (print B&W copy in `outputs/print/bw/` exists, but the figures themselves rely on colour).

## Build plan and effort

Effort in person-days (one developer, includes regenerating the six PDFs and checking the B&W copy). Order is by value per day.

| Step | Work | Effort | Fixes |
|---|---|---|---|
| 0 | Fix P1 L4 No.4 missing pattern (stop-ship) and P1 L1 No.5 stickers; both are one figure each | 0.5 day | items 1, 2 |
| 1 | `hp/figlib.js` shared SVG library: `pictureRow`, `coins` / `notes` (cents), `numberLine` (arcs, labels min 7 pt), `barModel`, `strip`, `clock`, `timeLine` with one style sheet (stroke widths, font 8 pt min, hatch palette for B&W) | 3 days | foundation |
| 2 | P1: coins in L6 and L10, picture graph symbols (L3, L10), pattern rows, strips, queue, frog line; PNG assets for fruit and pets | 2 days | P1 A and D |
| 3 | P2: sharing, bar scaffolds, money, fraction pairs, clocks, balances, time lines, picture graph | 2.5 days | P2 |
| 4 | P3: bar-model scaffolds for L4 (all 12), fraction bars L6, time lines and clocks L9, graph L10, enlarge L7 and L8 figures | 3 days | P3 |
| 5 | P4: bar-model scaffolds, clock-angle faces, enlarge angles, nets and graph scales | 2 days | P4 |
| 6 | P5: bar models for L2, L3, L10; enlarge tags, tank, tables; scale diagrams | 2 days | P5 |
| 7 | P6: clock and day circle, star polygons, sample-space grids, dot plots, vertical number line | 2.5 days | P6 |
| 8 | B-list pass (166 items, ~half are quick reuse of the library: ten frames, balances, arrays, ruler) | 3 days | B items |
| 9 | Re-render all six print and B&W PDFs, check page counts do not change (several A fixes add 20-40 mm of height per question; P1 L4 and P3 L4 will need a page break) | 1 day | QA |

Total about 21-22 days for everything; A and D only (steps 0-7 and 9) about 16 days; the top-20 list on its own about 6 days (steps 0, 1 and the High items of 2-6).

Rule for new figures (from the owner's feedback): use friendly objects (stickers, fruit, animals), proper diagrams (bar models with units and "?"), picture symbols in graphs, coin pictures with cents, clocks and rulers large enough to read (min 35 mm clock, ticks 1.5 mm and 7 pt labels), rulers that do not always start at 0, shading that survives B&W (hatching plus label, never colour alone).
