# Diagram audit: Level 1 Extension Workbook and Primary 1 puzzle pack

Audit date 23 Oct 2026. Read-only desk audit. Branch `claude/great-fermi-1hv4vc`.

## Scope and method

| Item | File | Pages |
|---|---|---|
| (a) | `outputs/extension/L1/Math_Inquirers_L1_Extension_Workbook_Soft_Copy_Colour.pdf` | 98 |
| (b1) | `school/p1/out/P1_Complete_Pack.pdf` | 25 (5 front matter, 20 puzzles) |
| (b2) | `school/colour_by_code/out/p1/*_pupil.pdf` (15 sheets) | 15 |
| (b3) | `school/colour_by_code/out/p2/*_pupil.pdf` (15 sheets), sampled only | 15 |

- Every content page was rendered with `pdftoppm` (60 to 170 dpi) and looked at. Text was extracted per page with `pdftotext`.
- Extension pages 6 to 75 were viewed in full. Pages 76 to 98 (progress, certificate, answers) were checked as a contact sheet and the answer text was read. The answers are text only and carry no worked diagrams.
- Zooms were taken of Extension p30, p32 and P1 clocks p11 and p23, and P1 rulers p22. Ruler and clock figures were measured from pixel positions.
- Grades: **A** = a child aged 6 to 8 cannot picture it from words alone. **B** = a diagram would clearly help. **C** = fine as text, or the existing diagram is fine. **D** = an existing diagram has a fault.
- Priority: High means a child could not start without it, or the page is wrong or gives the answer away. Med and Low are lesser.
- Counts are per numbered question, so (a)/(b) parts are not counted separately. For the P1 pack and galleries, "items" are the numbered questions or the colour regions. The counts are good to about plus or minus 3.

## 0. Critical finding: the Extension PDF is stale against its own source

`extension/data/l1_u01.json` already contains the figures the owner asked for:

- **L1U01-S07** (Start here Q7, "30, 26, 22, 18, ..."): `chain`, nodes `[30,26,22,18,null]`, ops `["?","?","?","?"]`. This is the right design, because "?" on the arcs does not give away the rule.
- **L1U01-S08** (Start here Q8, Siti's stickers): `sticker_boxes`, counts `[3,6,9,null,null,null]`, with the code in `extension/tools/figs_l1_u01.py`.

**Neither figure appears in the audited PDF.** p8 Q7 and Q8 are still text and a blank "Write the numbers:" line. Q9 on the same page, which does have a figure, renders. The source and tools were committed at 10:12, and the PDF in `outputs/` was built before that. Rebuild both the colour and BW files and re-check p8 before anything else.

Other incidental issues:

- `pdftoppm` reports "Kid object (page 49/50/52/53/54/70) is wrong type" on the Soft Copy file. The page tree is damaged but poppler renders it. Run it through `qpdf` or rebuild.
- The same two figure fixes in the source (S07, S08) are the only data/PDF mismatch I found. Figure ids for units 2 to 10 match what is rendered.

## 1. Totals

### Extension Workbook, 237 numbered items

| Unit | Items | A | B | D | C (fine, incl. already-illustrated) |
|---|---|---|---|---|---|
| 1 Hops and rules | 25 | 4 | 10 | 3 | 8 |
| 2 Make 10 and 20 | 25 | 3 | 11 | 1 | 10 |
| 3 Picture graphs | 21 | 0 | 3 | 3 | 15 |
| 4 Patterns that go on | 24 | 3 | 8 | 3 | 10 |
| 5 Working backwards | 25 | 9 | 13 | 0 | 3 |
| 6 Money | 25 | 1 | 14 | 3 | 7 |
| 7 2D shapes | 20 | 0 | 6 | 2 | 12 |
| 8 Logic and sorting | 22 | 5 | 11 | 1 | 5 |
| 9 Length | 25 | 5 | 11 | 0 | 9 |
| 10 Puzzle day | 25 | 6 | 11 | 2 | 6 |
| **Total** | **237** | **36** | **98** | **18** | **85** |

- By page type, the A and B items fall most in Start here (about 60) and Check yourself (about 28). Check yourself questions are almost all bare text, and a child who gets one wrong has nothing to see.
- Units 3, 7 and 9 are the best illustrated. Units 5, 8 and 10 are the worst, with story problems and ordering and no picture.

### Primary 1 pack (20 puzzles, about 124 items) and galleries

| Set | Items | A | B | D | Notes |
|---|---|---|---|---|---|
| P1 puzzle pack | about 124 | 10 | about 55 | about 42 | D is mostly "too small, outline-only, or numerals misplaced" |
| P1 colour-by-code (15 sheets) | about 217 regions | about 20 | about 120 | about 45 | picture-graph, mini-clock, ruler and coin regions |
| P2 colour-by-code (sampled) | about 230 regions | not graded | not graded | not graded | same style, same issues (see section 4) |

## 2. Extension Workbook: items needing action

IDs are page number then question, for example `p8 Q7`. S = Start here, T = Think harder, G = Go further, C = Check yourself.

### Unit 1 Hops and rules (pp. 6 to 12)

| ID | Gr | Diagram needed | Type | Pri |
|---|---|---|---|---|
| p8 Q7 | A | Row of 5 boxes 30, 26, 22, 18, empty box, with curved arrows labelled "?" (not "-4"). Up/Down and "take away" choices need circles or boxes. **Source has it, PDF stale.** | chain / number strip | High |
| p8 Q8 | A | Row of 6 numbered boxes with stars (3, 6, 9) then three dashed empty boxes. **Source has it, PDF stale.** | picture row (`sticker_boxes`) | High |
| p9 Q12 | A | Jar with coins plus a Mon to Fri table: 5¢ coin stack, 10¢, 15¢, then blank Thu and Fri | picture table | High |
| p10 T3 | A | Five numbered position boxes (1st to 5th) with 2nd = 10 and 5th = 25 filled, arcs "?" between them | chain | Med |
| p8 Q9 | D | Blocks are small squares in oversized empty frames, not a staircase. Redraw Steps 1 to 3 as stacked steps (1, 3, 5) with a dashed Step 4 frame the same size as the others | cube stack / staircase | Med |
| p9 Q13 | D | The 0 to 31 strip has cells about 6 mm wide. Circling is hard. Use a larger two-row grid and mark the start (3) | number strip | Low |
| p11 G1 | D | Triangle numbers are bare yellow dots, which the owner called dull. Use stars or sticker pips and mark the new dots in a second colour | tri_dots | Low |
| p7 Q4, Q5 | B | Number strip with "?" arcs under 5, 9, 13, 17 and 21, 18, 15, 12. The tile version is used for Q1 to Q3 | chain | Low |
| p8 Q6 | B | Chain 7, 11, 15, 19 with "?" arcs before the three choices. Also add circles to the choices | chain | Med |
| p9 Q10 | B | Row of 6 tiles 9, 12, 15, 17, 21, 24 so the wrong one can be circled | tiles | Med |
| p10 T1 | B | Number line 0 to 45 for hops of 5 from 2 (child marks it) | number line | Med |
| p10 T2 | B | Two number rows (Ali 4s, Mei 10s) up to 50, matching numbers aligned | number strip | Med |
| p11 G2, G3 | B | G2: two rows to 40. G3: number line 2 to 20 for trying hop sizes | number line | Low |
| p12 C1, C2 | B | Tiles with arcs, as in Start here | chain | Low |

### Unit 2 Make 10 and 20 (pp. 13 to 19)

| ID | Gr | Diagram needed | Type | Pri |
|---|---|---|---|---|
| p15 Q8 | A | Bookshelf with 2 rows of 10 slots, 16 filled | ten frames / shelf | High |
| p18 G1 | A | Two stacks of stickers (16 and 8) with a dashed "equal" level line | bar model | High |
| p18 G2 | A | Two jars as bars (17 total), A longer than B by a marked 5 | bar model | High |
| p17 T1 | D | **Answer given away.** The table has exactly 6 rows and the answer is 6 ways. Draw 8 empty rows, or none. Add two bag pictures | table | High |
| p14 Q3 | B | Pocket and bag split of 10 marbles | part-whole / ten frame | Med |
| p15 Q6, Q7 | B | Number line to 20 and to 50 with the jump to the next ten | number line | Med |
| p16 Q9 | B | Balance scale: 6 + 5 against 7 + empty | balance | Med |
| p16 Q10 | B | Pairs to 9 as stacked two-colour bars, a staircase | bar strips | Low |
| p16 Q12, Q13 | B | Q12: 20 child icons (7 girls). Q13: line 8, 10, 20 | bar / number line | Med |
| p17 T2 | B | The star and dot glyphs in "★ + ★ + 5 = 17" become bags of marbles | picture equation | Med |
| p17 T3 | B | Number cards 1 to 6 to pick from | tiles | Low |
| p18 G4 | B | Five number cards and a pair-sum table | table | Low |
| p19 C4 | B | 20 flowers, 11 red, as a bar | bar model | Low |

### Unit 3 Picture graphs (pp. 20 to 26)

This is the best illustrated unit. Symbols have a key, rows are aligned and empty slots are provided.

| ID | Gr | Issue or diagram needed | Type | Pri |
|---|---|---|---|---|
| p20 Try | D | The graph (Ben/Kumar) runs into the page footer and page number. Shift it up or shrink the box | layout | Med |
| p20 Worked example | D | The book symbols are about 2.5 mm, and thin outlines blur. Enlarge the symbol and row height | picture graph | Low |
| p24 T1 | D | The half face is clipped and looks like a stray mark. Draw a clear half circle face with a legend the same size | picture graph | Med |
| p21 Q4 | B | Zoo 9, museum 6, beach 8, farm = rest, as tally or bar | tally / bar | Low |
| p25 G2 | B | Empty three-row graph for kites, balls, ropes | picture graph | Low |
| p25 G3 | B | Two graph strips side by side with keys 2 and 3 | picture graph | Low |

### Unit 4 Patterns that go on (pp. 27 to 33)

| ID | Gr | Diagram needed | Type | Pri |
|---|---|---|---|---|
| p32 G2 | D | **Figure wrong.** The text says Mei makes a row of 3 triangles sharing sides. The drawing shows 2 triangles. Redraw 3 sharing sides, label the straws | stick rows | High |
| p30 Q12 | D | **Answer given away.** The dashed Tower 4 outline is exactly 11 blocks high, so Q12(a) is read off the frame. Use a generic tall frame with no grid, or no frame | towers | High |
| p28 Q5 | A | Ten slots with clap, clap, stomp icons for the first 6, rest empty | picture row | High |
| p29 Q11 | A | Day 1 to 5 bead strings (3 beads then +2) | picture row / table | Med |
| p31 T3 | A | Day 1 to 3 sticker piles (5, 8, 11) and a table | picture table | Med |
| p27 Worked example 2 | D | The +5 arcs under the table are about 2 mm and cramped. Space the table out | table | Low |
| p28 Q4 | B | M, N, O, M, N, O, M as numbered letter tiles | shape row | Med |
| p29 Q8, Q9 | B | Q8: number strip 1 to 17 with 2, 5, 8 circled. Q9: show a pattern of 4 to 13 | number strip / shape row | Med |
| p32 G1 | B | Dots or bars for jumps 1, 2, 3, 4 | number line | Low |
| p33 C1 to C4 | B | Row of shapes for C1 and C2, 3 towers for C3, 3 triangles for C4 | shape row / towers / stick rows | Low |

### Unit 5 Working backwards (pp. 34 to 40)

Unit 5 has a good worked example (p34) and Q4, Q6 and Q7. Most story problems still have no picture.

| ID | Gr | Diagram needed | Type | Pri |
|---|---|---|---|---|
| p35 Q1 | A | Cup (hidden, "?") with an arrow +5, then 13 counters | chain with picture start | High |
| p35 Q3 | A | Plate with "?" biscuits, an arrow "eat 4", 9 left | chain with picture | High |
| p35 Q5 | A | Chain ? then -3 then +8 then 14 (pencils) | chain | High |
| p36 Q9 | A | Vertical strip of floors 1 to 14 with a lift icon at "?" and arrows -4 and +6 to floor 11 | lift / vertical number line | High |
| p37 Q10 | A | Queue row: 6 spaces for the first 6 children, Kumar marked 6th, 2 behind. The blank dashed "Draw the queue" box is only about 90 by 10 mm and has no places | queue | High |
| p37 Q11 | A | Row of 12 numbered places, 5th marked Aisha | queue | High |
| p38 T1 | A | Chain ? then -5 then +8 then -4 then 13 | chain | High |
| p38 T3 | A | Two stacks: Ali gives 4 to Mei and both end at 10 | bar model | Med |
| p39 G3 | A | A well drawn as 12 steps, with the frog marked at the bottom. Day and night arrows | staircase / vertical strip | High |
| p34 Try, p35 Q2 | B | Chain with "?" start | chain | Med |
| p36 Q8 | B | Chains with the blank first, middle or last | chain | Low |
| p37 Q12 | B | Two bars: more than and fewer than | bar model | Med |
| p37 Q13, Q14 | B | Chains for the forward check | chain | Low |
| p38 T2 | B | In/out machine with two steps, then one step | in_out | Med |
| p39 G1, G2 | B | Double as two equal bars; the order of steps on a number line | bar / number line | Low |
| p40 C1 to C4 | B | Chain, machine | chain / in_out | Low |

### Unit 6 Money (pp. 41 to 47)

Unit 6 coins show cents and tags are clear.

| ID | Gr | Diagram needed | Type | Pri |
|---|---|---|---|---|
| p46 G2 | A | A $50 note as one bar, split into hat $18, bag "?" and change $12 | bar model | High |
| p42 Q2 | D | Notes are plain small boxes labelled $10, $5, $2, same size and colour. Draw notes as rectangles with different sizes plus the numerals | notes | Med |
| p45 T3 | D | **Answer given away.** The table has exactly 3 rows and there are 3 ways | table | Med |
| p45 T1 | D | "Set 1, Set 2" gives away the number of sets (2). Provide 4 lines | table | Low |
| p41 Try | B | Row of the four coin pictures to pick from | coins | Med |
| p42 Q3, Q4, Q5 | B | Q3: coin pictures that exchange. Q4: coin tray. Q5: two coins beside 40¢ | coins | Med |
| p43 Q7, Q9 | B | Q7: 50¢ coin and the 30¢ tag. Q9: $8 and $13 on a number line | coins / number line | Med |
| p44 Q12, Q13 | B | Coin groups for the true or false list. Fewest coins for 40¢ and 90¢ | coins | Med |
| p45 T1, T2 | B | Coin tray; 7 coins of two kinds | coins | Med |
| p46 G1, G3 | B | Coins shared between two or four purses; a $38 notes tray | coins / notes | Low |
| p47 C2, C3 | B | Coin tray; 90¢ minus 65¢ | coins / bar | Low |

### Unit 7 2D shapes (pp. 48 to 54)

Good. Shapes are drawn and labelled, with a names box.

| ID | Gr | Issue or diagram needed | Type | Pri |
|---|---|---|---|---|
| p53 G1 | D | Shapes A, B, C are about 8 to 10 mm. A child must draw fold lines. Enlarge to about 30 mm | shapes | Low |
| p54 C3 | D | The triangle picture is about 12 mm wide. Enlarge | shapes | Low |
| p49 Q2 | B | A shapes-and-sides reference picture | shapes | Low |
| p50 Q4 | B | Riddle choices as small pictures, not only words | shapes | Med |
| p52 T3 | B | Shape cards with side counts | shapes | Low |
| p53 G2 | B | 12 square tiles as a movable grid | grid | Low |
| p54 C2, C4 | B | 3 squares; a triangle plus 3 more sides | shapes | Low |

### Unit 8 Clues and sorting (pp. 55 to 61)

Grids and loops are good. Ordering questions have no picture.

| ID | Gr | Diagram needed | Type | Pri |
|---|---|---|---|---|
| p56 Q1 | A | Three child faces on an age ladder, oldest top | ladder / order strip | High |
| p56 Q2 | A | Queue row with Ben at place 3, two empty neighbours | queue | High |
| p56 Q3 | A | Line of 4 places, Ali 1st and Ben last | queue | High |
| p56 Q4 | A | Three bars of different height for tall, shorter, shortest | height bars | High |
| p57 Q6 | A | Five stacks of sweets 5 to 9 with name tags to place | ladder / bars | High |
| p59 T1 | D | The logic grid header text is about 5 pt and cells about 7 mm. Enlarge to match Q9 | logic grid | Med |
| p56 Q5 | B | Two loops (odd and even) with a number tray | loops | Med |
| p57 Q8 | B | Two number strips 1 to 24 with 3s and 4s marked | number strip | Med |
| p58 Q10, Q11 | B | Number strip with multiples marked | number strip | Low |
| p59 T2 | B | Blank two-loop Venn for 1 to 20 | Venn | Med |
| p60 G1 | B | Speech bubbles for the three children (not plain boxes) | speech bubbles | Low |
| p60 G3 | B | Number strip being halved by each question | strip | Low |
| p61 C1 to C4 | B | Ordering ladders, number strip 1 to 10 | ladder / strip / Venn | Low |

### Unit 9 Length (pp. 62 to 68)

Rulers are accurate. I measured the ruler on p62, p64, p65 and p72 from pixels: 0 is at the start, the cm scale is consistent at about 9.9 mm per cm, and the dashed guide lines land on the right marks. No answers are given away.

| ID | Gr | Diagram needed | Type | Pri |
|---|---|---|---|---|
| p63 Q2 | A | Two bars: tape 13 cubes, strip 8 cubes, difference marked "?" | bar model | High |
| p63 Q4 | A | Rope bar of 15 with a cut-off piece of 6 and "?" left | bar model | High |
| p64 Q6 | A | Tape bar 8 and a strip 5 longer | bar model | High |
| p65 Q14 | A | A table bar made of 6 pencils and the same bar made of 9 rubbers | bar model | High |
| p66 T2 | A | Nested bars: clip is 2 cubes, pen is 5 clips, bag is 2 pens | bar model | High |
| p63 Q3 | B | Four strips of cubes to put in order | bars | Med |
| p64 Q10 | B | Ruler with a leaf shape from 9 to 15 | ruler | Med |
| p65 Q12 | B | Ruler with a straw starting at 4 | ruler | Med |
| p66 T1 | B | 24-cube ribbon bar split into 4 (the blank draw box is small) | bar | Med |
| p66 T3 | B | Ruler with pencil and crayon | ruler | Med |
| p67 G2, G3 | B | Rod and cube bars; 14-cube rope | bars | Low |
| p68 C1 to C4 | B | Ruler for C1, bars for C2, C3 and C4 | ruler / bars | Low |

### Unit 10 Puzzle day (pp. 69 to 75)

| ID | Gr | Diagram needed | Type | Pri |
|---|---|---|---|---|
| p71 Q8 | A | Four children on an age ladder (the blank draw box has no scaffold) | ladder | High |
| p72 Q12 | A | Chain: ? then -3 then +8 then 14 | chain | High |
| p72 Q13 | A | Two bars: ribbon 13 and string 5 shorter | bar model | High |
| p73 T2 | A | A square and two triangles with a sticker on every side | shapes with pips | Med |
| p73 T3 | A | Chain: ? then -4 then -3 then +2 then 11 | chain | High |
| p74 G1 | A | A strip folded once, twice, three times with parts counted | fold strip | Med |
| p69 Try | D | The Try box overlaps the page footer and page number. Same as p20 | layout | Med |
| p71 Q7 | D | The triangle, square, triangle are about 4 mm. Enlarge | shapes | Low |
| p70 Q4 | B | Balance for "both sides equal" | balance | Low |
| p71 Q5 | B | A 70¢ and 45¢ coin and a bar | coins / bar | Low |
| p72 Q10, Q11 | B | Coin tray; chain with ? | coins / chain | Low |
| p73 T1 | B | Coin piles per day | coin table | Low |
| p74 G2, G3 | B | Bar model for 24 stickers; three triangles and squares | bar / shapes | Low |
| p75 C1 to C4 | B | Chain; bar; coin and change; ladder | mixed | Low |

### Cross-cutting issues in the Extension Workbook

1. **Choices with no controls.** "Circle ..." options are bare words (p8 Q6, Q7a; p10 T1; p21 Q3; p29 Q9). Add outlined circles or tick boxes.
2. **Table rows or lines equal to the answer** (p17 T1, p45 T1 and T3). Add spare rows.
3. **Layout collisions with the footer** on p20 and p69.
4. **Check yourself questions have almost no pictures.** They are meant to be independent, but a child who gets one wrong has nothing to see. Add at least one figure per unit.
5. **Blank "Draw ..." boxes with no scaffold** (p37 Q10 and Q11, p66 T1, p71 Q8). Give a row of places or a ruler line.

## 3. Primary 1 puzzle pack (P1_Complete_Pack.pdf)

Owner rules: friendly objects, proper diagrams, picture symbols in graphs, coins show cents, clocks and rulers legible. Findings against each puzzle follow.

| Puzzle | Gr | Finding | Fix and type | Pri |
|---|---|---|---|---|
| P1-01 Colour the Rocket | B | 15 regions are text equations ("9 and _ make 10"). The rocket is the picture; the sums have none | ten frames in 6 bond regions | Med |
| P1-02 Mystery Numbers | B (5) | Clues like "I am less than 73 and more than 59" have no number line | 0 to 100 hundred chart or number line to shade | Med |
| P1-03 Fair Shares | D (6) | Balloons, fish, apples and stars are 3 to 4 mm outline icons. The "bags" are rounded boxes and the plates are ovals. Item 1: balloons and bags are separate, so the child has nothing to drop into. The ring on the first group in items 2, 4 and 6 shows the method | large coloured objects; real bags, plates and bowls with slots to fill | High |
| P1-04 Sticker Grid | B (5) | "Ali has fewer than Mei" has no picture | stacks of stickers on a ladder | Med |
| P1-05 Times Code | A (5), B (1) | **No figure at all.** "4 x 5", "4 x _ = 16", "_ x 5 = 25", "3 groups of 2", "2 groups of 5" are bare symbols. The page says "3 x 4 means 3 groups of 4" and shows no groups | arrays and equal-group pictures | High |
| P1-06 What Time Is It? | D (6) | Numerals are about 7 pt and unevenly placed, with ticks colliding with 11, 12 and 1 and numerals sitting off the circle. Hour hand and minute hand differ only by thickness | larger faces (about 35 mm), numerals on a true circle, a short thick hour hand with a different colour | High |
| P1-07 The Queue | A | Children are blank circle-and-box figures, with no front marker. The answer places are a plain stack | queue of characters with a "front" arrow and ordinal slots | High |
| P1-08 Make Twelve | B | Plain 4 by 4 equation grid. Fine for a route puzzle but dull | a path theme (stepping stones) | Low |
| P1-09 Magic Square | D, B | The two diagonal total boxes are small dashed squares with diagonal lines, unlabeled. The grid is plain | label "corner to corner" totals; number tiles | Low |
| P1-10 Take Away Code | B (4), A (2) | Q5 and Q6 ("17 - _ = 12", "19 - _ = 3") have no picture | number line with jumps back; a cross-out row | Med |
| P1-11 Big Number Sums | B (4), A (2) | "31 - 10", "84 - 3", "54 + 40" with no tens and ones. Q4 and Q5 missing-number | tens-and-ones sticks | Med |
| P1-12 Colour the House | D (page) | Shapes are about 5 mm and answer boxes are tiny. Legible but small | enlarge the shapes | Low |
| P1-13 Equal Groups | D (6) | Same as P1-03: 3 mm outline icons, and "bags" drawn as boxes. Item 6 is five boxes of tiny stars | bags and objects at 6 to 8 mm, filled colour | High |
| P1-14 Colour the Ice Cream | B (13) | Skip counting is plain text. There is no number line | hop arrows or a number strip in 4 of the regions | Low |
| P1-15 Coin Purses | C, D low | Good. Coins show their value and "cents", with different sizes and motifs. The "cents" text is about 4 pt | enlarge text | Low |
| P1-16 Shop Prices | B (6) | Pen, book, ball, kite and cup are words only. No pictures of the items | friendly item pictures beside the rows | Med |
| P1-17 How Long? | D low | The ruler is right (0 at the left, 1 mm ticks, true size). The numerals are about 6 pt, the mm ticks are dense, and the strips are bare hatched bars | thicker numerals; pencil and crayon shaped strips | Low |
| P1-18 Clock Time | D (5) | Same clock fault as P1-06. In Q2 the minute hand tip runs into the numeral 5, and in Q3 into 6 | same | High |
| P1-19 Shape Count | D (5) | Bare outline shapes on a blank panel. Half and quarter circles are drawn in four orientations with no friendly picture | build a robot, house or train from the shapes | Med |
| P1-20 Fruit Graph | C, D low | The graph is fine. The key symbol is a smiley for a child and each row has a tiny fruit icon. Rows have 9 slots, enough for 9. The fruit icons are about 4 mm | enlarge the fruit icons | Low |

Front matter (cover, licence, notes, contents): no diagrams needed.

## 4. Colour-by-code galleries

### Primary 1 (15 pupil sheets, about 217 regions)

- Almost every region is a text equation inside a shape outline. That suits the colouring task and the check strip.
- Pictures appear only for money, time, length, shapes, sharing and graphs, and these are all small.

| Sheet | Gr | Finding | Fix | Pri |
|---|---|---|---|---|
| CBC-13 icecream and rocket picture graphs | D (about 27 regions) | Every mini-graph uses the same small smiley (about 2 mm) for cars, pies, tarts, dolls, dogs, hats. The owner rule says picture graphs use picture symbols. The key "smiley = 1" is tiny | use the object itself (a car for Cars) as the symbol, 4 to 5 mm | High |
| CBC-08 butterfly time | D (about 6) | Mini clocks are about 8 mm with unreadable numerals. 7 of 14 regions are text only ("5 o'clock + 1 hour") | enlarge; add a clock to the text-only regions | High |
| CBC-07 sailboat money | D (about 4) | Mini coins are about 4 mm with 4.2 mm text | enlarge to 7 mm | Med |
| CBC-09 icecream length | D (about 4) | Mini rulers 0 to 5 are about 12 mm wide and numerals are unreadable | enlarge; 1 ruler per larger region | Med |
| CBC-14 sailboat ordinal | D (3) | Queue figures are about 3 mm. The rest are text ("Just after 5th") | larger queue figures | Med |
| CBC-11 car multiplication | A (about 8) | "5 groups of 4 is" and "3 bags, 5 in each" are text only | bag and array pictures | Med |
| CBC-12 castle sharing | A (about 12) | "Share 12 by 2. Each:" and similar are text only. Two regions have tiny star boxes | counters or objects shown | Med |
| CBC-01 to 06, 10 | B | Text-only equations, counting patterns, comparison | ten frame, number line | Low |

### Primary 2 (15 sheets, sampled)

Same style. Seen: CBC-P2-10 graphs use the same smiley for kites, buns, bags and pens, plus tally marks (symbols need to be the objects). CBC-P2-08 mini clocks are about 10 mm. CBC-P2-06 and P2-15 use shaded fraction bars at about 10 mm (acceptable but small). CBC-P2-11 3D shape icons are about 5 mm. These need the same treatment, but P2 is outside this audit and was not graded item by item.

## 5. Top 15 priorities

1. **Rebuild the Extension PDFs.** p8 Q7 (chain) and p8 Q8 (sticker boxes) are in the source but not in the PDF. This is the owner's "need diagram" request, and it is already fixed in the source.
2. **U4 p32 G2:** Mei's drawing shows 2 triangles but the text says 3. Redraw.
3. **U4 p30 Q12:** the dashed Tower 4 frame is 11 blocks high, which gives away Q12(a). Use an ungridded frame.
4. **U2 p17 T1:** the 6-row table gives away "6 ways". U6 p45 T3 (3-row table) and T1 (2 lines) do the same.
5. **U5 p35 Q1, Q3, Q5 and p38 T1:** story chains with a hidden start (cup, plate, pencils, stickers). Use the existing `chain` with a picture start.
6. **U5 p36 Q9 and p39 G3:** the lift (vertical floor strip) and the well (12 steps).
7. **U5 p37 Q10, Q11 and U8 p56 Q2, Q3:** queue rows with numbered places and a front marker. P1-07 needs the same figure.
8. **U8 p56 Q1, Q4 and p57 Q6:** ordering ladders (age, height, sweets).
9. **U9 p63 Q2, Q4, p64 Q6, p65 Q14, p66 T2:** bar models for "how many longer", cuts and nested units.
10. **U10 p72 Q12, Q13, p73 T3, p71 Q8:** chain and bar models, age ladder.
11. **U1 p9 Q12 and U4 p28 Q5, p29 Q11, p31 T3:** picture tables and rows for growing patterns.
12. **U2 p15 Q8, p18 G1, G2 and U6 p46 G2:** shelf frame, two-stack and bar model for the sharing and money comparisons.
13. **P1-05 Times Code:** no figure at all. Arrays and equal groups for 5 of 6 items.
14. **P1-06 and P1-18 clocks, and P1-03 and P1-13 icons:** enlarge and redraw. The clock numerals are unevenly placed and small.
15. **CBC-13 graphs (both sheets):** use the object as the picture symbol. The owner rule is explicit.

Also worth doing early and cheap: fix the footer collisions on p20 and p69, and add circles to all "Circle ..." options.

## 6. Figure types the generators lack

### Extension (`extension/tools/figs*.py`)

Present in L1: `tiles`, `numstrip`, `dot_boxes`, `tri_dots`, `bonds`, `ten_frame`, `sticker_boxes`, `picture_graph`, `shape_row`, `stick_rows`, `towers`, `tally`, `grow_table`, `chain`, `in_out`, `coins`, `tags`, `shapes`, `grids`, `draw`, `loops`, `logic_grid`, `latin`, `names_table`, `bars` (cube strips only), `ruler`, `fence`.

`number_line` exists in `figs.py` as a legacy wrapper but is used **0 times** in the L1 data. `ten_frame`, `numstrip` and `tally` are used once or twice.

Missing:

| Type | Needed for |
|---|---|
| `bar_model` (part-whole and comparison with labelled lengths and a "?" gap) | U2 G1, G2, C4; U5 T3; U6 G2; U9 Q2, Q4, Q6, Q14, T2; U10 Q13, G2 |
| `queue` / `ordinal_row` (child icons with place numbers and a front marker) | U5 Q10, Q11; U8 Q2, Q3; P1-07 |
| `ladder` / `height_bars` (ordered stacks for older/younger, taller/shorter) | U8 Q1, Q4, Q6; U10 Q8 |
| `picture_chain` (chain with an object as the start, such as a cup or plate) | U5 Q1, Q3, Q5, T1 |
| `vertical_strip` (lift, well, staircase) | U5 Q9, G3; U1 Q9 |
| `picture_row` / `picture_table` (object icons in numbered slots, by day) | U1 Q12; U4 Q5, Q11, T3 |
| `balance` | U2 Q9; U10 Q4 |
| `shelf` / `array` (rows of slots) | U2 Q8; P1-05, P1-10, P1-11 |
| `fold_strip` | U10 G1 |
| `note` (banknote picture) | U6 Q2, G3 |
| `speech_bubble` | U8 G1 |
| `hundred_chart` / `base_ten` | P1-02, P1-11 |

### P1 pack (`school/p1/gen/*.py`, `common.py`)

Present: `coins_svg`, `clock_svg`, `ruler_unit`, `groups_svg`, `share_svg`, `face_svg`, `fruit_icon`, `mini_route`, `mini_ticks`, `mini_magic`, `mini_graph`, `obj_g`, `container_g`, `shape_svg`. Gaps:

- `array` / `equal groups` is not used on P1-05 (`groups_svg` exists, but only P1-13 uses it).
- `ten_frame`, `number_line` and `base_ten` blocks are absent.
- `queue` of characters is absent. P1-07 draws bare circles.
- Object sizes are fixed at about 3 to 4 mm (`obj_g` default size 6.6 units). `container_g` draws boxes, not bags.
- `clock_svg` places numerals unevenly. Fix the numeral radius and size (`pages_measure.py` line 219).
- `mini_graph` uses one smiley for every row. It needs per-row object symbols.
- No friendly composite picture for shape counting (P1-19).

## 7. Build plan

1. **Rebuild** the Extension colour and BW PDFs from the current source. Re-check p8 Q7 and Q8. Fix the structural page-tree errors.
2. **Correctness fixes first** (small): U4 p32 G2 (3 triangles), U4 p30 Q12 (frame), the table rows on U2 p17 T1 and U6 p45 T1 and T3, the p20 and p69 footer collisions, the p24 T1 half face, option circles on every "Circle" item.
3. **Add three new figure types**, which cover over half the A items: `bar_model`, `queue` / `ordinal_row` / `ladder`, and `picture_chain` (extend `chain` to take an object icon). About 1 day each, with specs in the unit JSON and a test that no figure reveals an answer (row counts, frame heights).
4. **Fill the A items** in order: U5, U8, U9, U10, then U2, U4, U1, U6.
5. **Add `number_line` use**, `balance`, `picture_row`, `vertical_strip`, `note` and `shelf`. Then fill the B items. Do Check yourself B items last, one figure per unit.
6. **P1 pack:** add `array`/`ten_frame`/`number_line`/`base_ten`; put an array on P1-05, number lines on P1-02, P1-10 and P1-11, a queue on P1-07; enlarge icons (P1-03, P1-13, P1-19) and redraw clock numerals (P1-06, P1-18).
7. **Galleries:** switch `mini_graph` symbols to the object, enlarge mini clocks, coins and rulers on CBC-07, 08, 09 and 14, and add bag and array pictures on CBC-11 and 12. Apply the same to P2.
8. **Check:** rerun each unit's verify, render at 80 dpi, and re-measure rulers. Add a check that every item with an A grade has a figure.
