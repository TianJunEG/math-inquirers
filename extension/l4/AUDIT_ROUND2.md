# Round 2 independent audit: Level 4 Extension Workbook (self-study, with answers, ages 9-11)

Audited 23 Oct 2026, desk review by a second model in a fresh session. Branch `claude/great-fermi-1hv4vc`. Report only: nothing in the book, data or tools was edited, nothing pushed. Files: `outputs/extension/L4/*Print_BW.pdf` (100 pp, 1-bit CCITT 600 ppi), `*Print_BW_vector.pdf` (text and figure coordinates), `*Soft_Copy_Colour.pdf` (100 pp), `build_report.json`. Round 1: `AUDIT.md`. Holiday source compared: `p4/content/l1.js` to `l10.js` (qbank and workbook strings).

## Method and honest coverage
- **Hand-solved from the PDF text, not from the verify scripts:** every one of the 229 items plus the 10 "Your turn" items, and every printed answer and Why, was solved by me and compared (all 10 units). I did not run `run_checks.py`, `dup_check.py` or `wording_lint.py`.
- **Figures read from the drawing, not the figure spec:** Unit 6 protractor and ray figures were read from the vector coordinates of the PDF at the printed scale (arm angles measured with `atan2` on the drawn lines) and checked against the 1-bit bitmap at 130 and 300 dpi. Number lines (U2 S5, U4 S5, U5 S1-S3), nets (U8), shaded grids (U8 S4, S6, S9), graphs (U9), shapes (U7) were read on the rendered page.
- **Pages viewed as images (print edition):** 3, 4, 8, 11, 15, 16, 17, 19, 21, 26, 27, 28, 29, 35, 41, 42, 43, 44, 49 to 54, 55 to 61, 63 to 68, 73, 77. Colour edition: 3 and 42 viewed; the rest of the colour text equals the print text word for word (checked page by page; the only differences are the intended p2 "printed book / soft copy" wording and the p3 print note).
- **Holiday comparison, by hand:** I extracted all holiday question text (about 650 lines) and read each Level 4 item against it by sentence frame, story and sub-questions. A 3-gram similarity script was used only to surface candidates; every claim below was confirmed by reading both texts.

## Verdict
**Not yet sell-ready. One High and one Medium remain, both small in effort but the High is a content decision.**
- All round-1 mechanical Highs are closed (Welcome page, protractor figures, wide boxes, the two give-aways, the 12 listed holiday repeats). Maths is sound: **0 wrong answers, 0 unsolvable items in the 239 solved**, and no figure disagrees with its key.
- **New High (missed in round 1): about 55 items are same-story clones of holiday items** (same characters or situation, same structure, often the same sub-questions, only numbers or the object changed). The Welcome page promises "new numbers and stories". See H1 below. Either rewrite those items with a new context, or have the owner accept "same type, new numbers" as the policy and change the Welcome sentence.
- **New Medium:** one Why line was inverted by the trimming (U2 G1(c)).
- Everything else is Low. A child trial for pace and reading load is still needed (a desk review cannot replace it).

## Round 1 High and Medium: closed or open

| Round 1 item | Status | Evidence |
|---|---|---|
| H1 Welcome stale "rulers in Unit 9" line | **Closed** | p3 print: no ruler sentence; print edition has no print note (empty by design). |
| H1 equipment line | **Closed** | p3 both editions: "You will need: a pencil, a rubber, a ruler and a protractor." |
| H1 "Beyond Level 4" explained | **Closed** | p3: "Beyond Level 4 is ahead of school. You may skip it." |
| H1 colour print note only in colour | **Closed** | Colour p3: "Print at 100 percent so the angles in Unit 6 are true size." Not in the print PDF. No "Unit 9", no "Level 1" anywhere. |
| H1 Welcome overflow | **Closed** | `build_report.json`: soft p3 excess -2.6 mm (fits), `problems: []`; colour p3 viewed, last box clear of the footer; print p3 viewed, no overflow. |
| H2 the 12 listed holiday repeats | **Closed as listed** (U9 Try, U9 T3, U9 S7, U10 T1, T2, T3, S8, C3, S9, U8 T1, G2, U1 S8). Hand-read: new contexts. **But** U1 S8 now reuses the numbers of another holiday item (see H1 table) and the wider clone problem is open (H1 below). |
| H3 U1 G1 "Factors of 48:" | **Closed** | p11 label "My factor lists:", hint "Count the factors of some numbers between 20 and 60." (a range, not the answer). |
| H3 U3 G3 "334-style" | **Closed** | p25 hint "Start with the ones: what is 4 × 7?" Solved: 334 × 7 = 2338, both digits 3. |
| H4 Unit 6 protractor, p41 | **Closed** | p41 arm 55.0 degrees (measured), key 55. Outer scale outside the rim, arc marked, labels every 30 with white outline, arm tip stops about 1.7 mm right of the "60" label (not struck). |
| H4 p42 Start here 2 | **Closed** | Arm measured at 128.0 degrees from the right baseline, so 52 from the left 0; arc drawn on the 52 side; outer and inner rings separate; key 52, "smaller". Legible at 300 dpi 1-bit. |
| H4 p42 Start here 1 arms | Arms measured 25, 65, 130 degrees (key 25, 65, 130, within 2 degrees). Arms 38 mm long, the item says to lengthen them. OK. |
| H4 p42 fan | Rays at 20, 45, 80, 120 degrees: 25, 35, 40; AOC 60, BOD 75, AOD 100, 6 angles. Matches the key. Arc labels now 10 pt or more. |
| H4 p44 corner angles | **Closed** | Labels sit beside the rays; a = 53 (ray measured 53), b = 43 (rays 62 and 43 measured). |
| H5 narrow boxes | **Closed** | Every 5-digit answer in the data uses `{bw}` (scan of all items, 22 items with 5-digit answers, all wide). Boxes measure about 25 mm on p16, p17, p19, p21, p26. |
| M1 U9 S8(c) | **Closed** | "At what time before noon was it 29 °C?" Solved: 9 am only. |
| M2 U4 T2 | **Closed** | "1/3 of her money": 90. |
| M3 U3 T3 hint | **Closed** | "Before the gift, how many more does Mei have than Lily?" |
| M4 hints | **Closed** | U4 T2, U4 G3, U9 T2, U10 G1, G2, U1 T1, U1 G1 are now nudges. |
| M5 untaught prerequisites | **Closed** | U4 box has equivalent fractions and whole from a part; U6 has angle AOC; U8 has "No fold: 4 squares at one corner, or 5 in a row"; U10 has the logic grid. U8 S8 replaced (dice net area 54); U8 C1 is now a different net (answer No, solved: both extras on the same side). |
| M6 pace | **Closed** | p3 and p5 say 25 to 30 minutes. |
| M7 figure text and graphs | **Mostly closed** | No figure text under 10 pt on pages 6-75 (only the 9 pt footer and the 9 pt badge). U9 S4 markers offset: week 7 shows circle and square both at 80, week 8 90 against 85: readable at 250 dpi 1-bit. U9 C1 graph still small (see L7). |
| M8 beyond label | **Closed** | p11, 18, 24, 25, 32, 45, 60, 67, 74: "★ Beyond Level 4: name" is a badge on the card rule, not a stem line. Only in Think harder or Go further. |
| Page numbers | **Closed** | Contents: units 6, 13, 20, 27, 34, 41, 48, 55, 62, 69; progress 76; certificate 77; answers 79. Checked against the pages: answer start pages 80, 82, 84, 86, 88, 91, 93, 95, 96, 98 match the contents. Pace plan page pairs match. p78 blank, p79 divider (odd page), 100 pages, even. |

## Findings

### High

**H1. About 55 items are same-story clones of holiday items.** The 7-word gate cannot see these. "Clone" here means the same characters or situation and the same question or sub-questions, with only numbers (or one object) changed. A child who attended the holiday course will recognise them, the spec says "new contexts, never a repeat", and the Welcome page says "with new numbers and stories". Round 1 found 12 such items and they were rewritten; this pass found many more, mostly in Units 3 to 10. Exact pairs (Level 4 item, holiday source, what is shared):

| Level 4 item (page) | Holiday source | Shared |
|---|---|---|
| U1 S8 (8) jogging every 10 and 15 days, how many times together | l1 "Bus 33 every 10 minutes and Bus 51 every 15 minutes ... how many times together" | same numbers, same two sub-questions, answer 30 again |
| U1 S7 (8) Ravi red and blue marbles in equal bags | l1 "Mei has 18 red beads and 24 blue beads ... identical packs" | same frame |
| U2 S9 (16) ferry 4018 people, 5 trips, estimate, exact, more or less | l2 "A bakery bakes 4982 buns every day for 6 days ... round, estimate, exact, more or less" | same three sub-questions |
| U2 S12 (16) three number rules | l2 find-the-rule set (+1000 pattern and a -1500 pattern) | same steps, new start values |
| U2 T1 (17) five cards, 5-digit number nearest to 40 000 | l2 "digit cards 1, 4, 6, 7, 9 ... closest to 70 000" | whole item |
| U2 G2 (18) numbers 1 to 1000 with a 7 | l10 "1 to 100 with the digit 7" | whole item scaled |
| U3 T2 (24) chain, 5th and 6th given, find the 1st | l3 same (5th 30, 6th 49) | whole item |
| U3 T3 (24) Mei 5 times Lily, gives 36, then equal | l3 "Ravi has 3 times as many as Siti, gives 20, now equal" | whole item |
| U3 S8 (22) number trick x3, +12, /3, minus start | l3 "x5, +35, /5, minus start, always 7" | same trick |
| U3 S12 (23) Kumar 3 times Aisha, 480 in all, how many more | l3 hawker "3 times as many ... 1236 altogether, how many more" | same frame |
| U3 G1 (25) signs in 9 ○ 4 ○ 6 = 30 and one pair of brackets in 7+3×8-4 | l3 "12 __ 4 __ 5 = 15" and "one pair of brackets in 3+5×6-2" | both parts |
| U4 S8 (29) order 3/4, 2/3, 5/12, 1/2 | l4 "order 2/3, 1/2, 5/6, 7/12" | same denominators, same task |
| U4 S10 (30) pizzas cut in 8, 27 slices eaten, mixed number | l4 "11 slices, pizza cut in 3, how many whole pizzas" | same |
| U4 S11 (30) rope 2 2/3 m cut into 1/3 m, 5 used, left | l4 "ribbon 4 3/4 m cut into 1/4 m, uses 5 pieces, left" | same, even "5 pieces" |
| U4 S13 (30) quarters in 5 wholes | l4 "How many eighths in 5 wholes?" | same question |
| U4 T1 (31) fraction, denominator 7, between 3 and 4, closer to 4, even top | l4 "denominator 6, between 2 and 3, odd numerator, closer to 3" | same riddle |
| U4 T2 (31) Mei, two fractions of her money, $24 left | l4 "Mei spent 1/3 on a book and 1/4 on a pen, $25 left" | same |
| U4 T3 (31) Siti reads 1/3 Monday, 3/4 of rest Tuesday, 20 left | l4 "Siti read 2/5 Monday, half of the rest Tuesday, 45 left" | same |
| U4 G1 (32) denominator 20 between 1/4 and 3/5 | l4 "denominator 10 between 1/5 and 1/2" | same |
| U5 S5 (36) order 5.205 5.25 5.052 5.5 5.025 | l5 "3.405, 3.45, 3.054, 3.5, 3.045" | same digit pattern |
| U5 S9 (37) Ravi and Kumar $12.60, Ravi $2.40 more | l5 "Mei and Siti $9.40, Mei $1.20 more" | same bar model |
| U5 S10 (37) box with 4 packs, box 0.5 kg, 4.1 kg, one pack, take one out | l5 "box with 6 cans, 2.85 total, 0.45 box, one can, take 2 out" | same steps |
| U5 T2 (38) cards 1, 4, 6, 9 and a point, closest to 20 | l5 "cards 2, 4, 7 and a point, closest to 50" | same |
| U5 T3 (38) mug $2.40 more than a cup, 3 mugs 2 cups $17.20 | l5 "pen $0.85 more than a pencil, 2 pens 1 pencil $4.70" | same |
| U5 G1 (39) bottle of juice 1.26 kg, 1/3 left 0.58 kg, empty bottle | l5 "jug full 1.45 kg, half full 0.85 kg, empty jug" | same |
| U5 G2 (39) 12 coins of 10¢ and 50¢ worth $3.60 | l5 "Ravi has 10 coins of 20¢ and 50¢, $3.80" | same |
| U5 C3 (40) Siti 4 notebooks, $10 | l5 "Siti buys 4 notebooks, pays $10, change $2.60" | same story reversed |
| U6 S3 (42) rays OA to OD, 25, 35, 40, how many angles | l6 "Four rays OA to OD ... 25° and 40°, how many angles" | same |
| U6 S4(a), (d) (43) Ali faces W turns 90 clockwise; Ravi turns anticlockwise to face S, at first | l6 "Ali faces W and turns 90° clockwise" ; "Ravi turns 90° anticlockwise and ends up facing NW, at first" | same |
| U6 G1 (46) six rays, 5 equal angles, outside 150, how many angles, right angles | l6 "Five rays, 4 equal angles, outside 120, how many, right angles" | same |
| U6 G2 (46) robot turns 135 again and again, after 50 turns | l6 "robot turns 45 again and again, after 30 turns" | same |
| U6 G3 (46) corner of 90 cut by 2 lines, 1:2:6 | l6 "corner of a square cut into 3 angles, 1:2:3" | same |
| U6 S9 (44) corner split, one angle 5 times the other | l6 "one angle 4 times as big, find both" | same |
| U6 C4 (47) minute hand 5:10 to 5:35 | l6 "minute hand from 7:15 to 7:50" | same |
| U7 S6 (50) photo 12 by 9, frame 2 cm, area of frame | l7 "photo 8 by 6, frame 1 cm, area of frame" | same |
| U7 T1 (52) square cut into 2 identical rectangles, perimeter 30, area | l7 same with perimeter 24 | only the number differs |
| U7 T2 (52) 28 m of fence, 4 sides, then one side a wall | l7 "Ravi has 24 m of fencing ... (a) largest area (b) one side a wall" | whole item |
| U7 T3 (52) garden 12 by 9, two paths 2 m wide, area not path | l7 "garden 10 by 8, two paths 1 m wide, area not path" | whole item |
| U7 G3 (53) two strips 10 by 2 make a plus | l7 "two 8 by 2 rectangles cross to make a plus, area and perimeter" | whole item |
| U8 S7 and C3 (58, 61) dice top 6 front 4 / top 2 front 3, bottom and back | l8 "top 3, front 5, bottom and back" | same |
| U8 T2 (59) corner faces add to 10 | l8 "Mei looks from a corner, 3 faces add to 12, which numbers" | same |
| U8 T3 (59) shade exactly 3 squares of a 3 by 3 grid, middle fold | l8 "shade exactly 2 squares of a 3 by 3 grid, up-down line through the middle" | same |
| U8 C2 (61) rectangle that is not a square, lines of symmetry | l8 "fold a rectangle that is not a square, how many ways" | same |
| U9 S3 (63) library books, 3 classes, Week 1 and 2, missing totals, "which class borrowed fewer in Week 2" | l9 "table of books three classes borrowed from the library, fill in missing, which borrowed more in Week 1 than Week 2" | same story and question |
| U9 S4 (64) Ali and Mei money boxes graph: Mei's money in Week 3, Ali adds each week, same in Week, Ali first has more | l9 same graph and the same four questions | all four sub-questions |
| U9 S5 (64) Siti reads more pages each day, fill the table, how many more, pages in 5 days | l9 same, word for word | whole item |
| U9 S6 (65) two bakeries, scales, January to April, who went up more | l9 "two shops' line graphs, scales, January to April" | same |
| U9 T1 (66) sales grow by the same each week, week 3 and 8, week 1, first over 100 | l9 "week 2 and 6, week 1, first over 100" | whole item |
| U9 G2 (67) stall plates in 5 days, each day beats the day before | l9 "stall 400 plates Monday to Friday, 10 more each day" | same |
| U9 C2 (68) 28 and 35 and a 3-day total 99, Wednesday | l9 "three days add to 90, Day 1 30, Day 2 25, Day 3" | same |
| U10 S2 (70) Mei buys $3 pens and $5 notebooks, exactly $41, how many ways | l10 "Mei buys $4 pens and $7 notebooks for exactly $50, find all ways" | same |
| U10 S3 (70) farm hens and cows, 17, 50 legs, with the same scaffold (suppose all, short, swap) | l10 "chickens and goats, 18 heads 50 legs, same scaffold" | same, same total legs |
| U10 S4 (71) bicycles and tricycles, 13, 33 wheels | l10 "20 bicycles and tricycles, 47 wheels" | same |
| U10 S5 (71) Mei half to Ali, buys 12, loses 7, 25 | l10 "Ravi gave half, won 9, lost 5, 30" | same |
| U10 S10 (72) Ravi, 9 coins of 20¢ and 50¢ | l5 and l10 coin items ("Ravi has 10 coins, 20¢ and 50¢") | same |
| U10 S12 (72) 2-digit, digits add to 12, swap is 18 more | l10 "digits add to 11, swap is 27 more" | same |
| U10 G3 (74) Ben 11th from left, Mei 8th from right, 5 between | l10 "Ali 8th from front, Ben 6th from back, 7 between" | same |

Weaker (same type with a changed story, acceptable as "same question type"): U1 S3, S10, S13, T1, T2, C4, G2 (three lighthouses 6, 8, 9; the holiday lighthouse item uses 6 and 9), U2 S7, S10, S11, T3, U3 S11, S5, C3, U4 S4, S12, C4, U5 G3, T1, U6 S1 (instruction wording), S6, S7, S8, T2, U7 S5, S7, S2, U8 S2, S5, S6, U9 S1, S7, S8, U10 S1, S6, S7, S8, C1.

Recommendation: rewrite the clone list (new story, new structure for the same skill, new numbers), then re-run `l4_uNN_checks.py`, the build, and re-solve the rewritten items. Cheaper alternative the owner may choose: accept "same type, new numbers" as policy and edit the Welcome sentence ("with new numbers and stories") to "with new numbers". The near word-for-word copies (U9 S4, S5, U7 T1, T3, U3 T2) should be rewritten whichever policy is chosen.

### Medium

**M1. U2 Go further 1(c) Why is wrong after trimming (answers page 83).** Key says "1445 becomes 1450, 1500, 2000, but in one go it is 1000. Any 4-digit number below 1445 does this." As written this says the opposite of the point: no 4-digit number below 1445 does this (1444 gives 1000 both ways). The round-1 text read "gives the same answer both ways". Fix: "No 4-digit number below 1445 does this." The answer 1445 itself is correct (checked: 1000 to 1444 all agree).

**M2. U10 S7 Why lost its reason (answers page 99).** "Mei does not have the rabbit, so Mei has the cat" no longer says why Mei is not the rabbit (the clue "does not hop"). Restore "A rabbit hops, so Mei does not have the rabbit."

### Low

1. **Contents (p4)** still prints each unit title twice, "Factor Hunters" then "Factor hunters · follows ...". (Tool issue, round 1 Low 1, not fixed.)
2. **Certificate (p77)** the trophy plaque in the Mi image still shows pseudo-text. Replace the plaque or the image.
3. **DRAFT licence line (p2, both editions)** "DRAFT licence text, for owner and lawyer approval. Not final." must come out before sale. Known, not a code fault.
4. **"−180" in the p42 protractor** the baseline stub before 180 reads like a minus sign. Remove the stub or leave a gap.
5. **U1 S8(b)** "How many more times do they jog together in the next 100 days?" Answer 3 (days 30, 60, 90). A child who has just used day 30 in (a) may say 2. Use "in all" instead of "more".
6. **U7 T1 hint** "Each rectangle has 3 sides that equal the side of the square" is loose: it has 2 whole sides and 2 half sides, worth 3 sides in all. Say "its sides add up to 3 sides of the square".
7. **U9 C1 (p68)** half-line reading (65) is a 1.8 mm judgement (plot 47 by 28 mm, lines every 3.5 mm). Better than round 1, still small. Enlarge by one page-line or ask for a value on a line.
8. **U10 T2 hint** "Write what you know in 3 groups": the clues give 2 groups (the chain Ali, Mei, Ben and the pair Siti, Kumar).
9. **Answer boxes that wrap to a second line** (the box is easy to miss): U2 C1 (1000 box), U1 S8(b) "times", U7 S1(a) "b =", U7 S6(a), U10 T2 fifth box. Round 1 Low 3, not fixed.
10. **U1 G1** "Show the factors you found" has one short writing line (about 100 mm) for several factor lists.
11. **U4 Learn it (p27)** "Whole from a part" and "Equivalent" lines sit in the box headed "Comparing". Give them their own heading or rename the box "Good to know".
12. **U6 p43 clocks** the minute hand covers the numeral 12. Readable, but draw the hands thinner over 12.
13. **U9 G1** still text only (no graphs X and Y). **U7 S9** tiles have no drawing. Round 1 Lows, not fixed.
14. **U8 T1 Why (a)** ("A face touches 4 faces, so a third red face would touch one of 2 opposite red faces") is correct but terse; "red faces that share no edge must be opposite, so at most 2" is clearer.

## Hand-solve results for new or changed items (all agree with the printed keys)
Solved from the printed question and figure: U1 S1-S13, T1-T3, G1-G4, C1-C4 (including S8 = 30 days and 3 times; T1 = 72; G1 = 48, 36 has 9 and 40 has 8; G2 = 72 s, 8 times; G3 = 17; G4 = 12 by 7). U2 all 13 Start here items, T1 38 641, T2 68 000 and 69 998, T3 74 986 and 65 012, G1 37 000 / 36 000 / 1445, G2 271, G3 8000 and 15, G4 No and 100, C1-C4. U3 all, including G1 (9 × 4 - 6; (7 + 3) × 8 - 4, both unique) and G3 (334 × 7 = 2338, both 3). U4 all (S5 arrows 2/3, 1 1/3, 8/3 read from the line). U5 all (arrows 5.3, 5.8, 0.43, 0.48, 3.427 read from the ticks; T2 19.64; G1 0.24). U6 all, with figures read from the drawing: 25, 65, 130; 52 smaller; 60, 75, 100 and 6; 53; 43. U7 all (S4 perimeters 10, 12, 12 from the tile drawings; C1 area 43 from the labelled L shape). U8 all (S1 A and C fold; S2 R, T, U checked by folding; S3 5, 4, 6; S4 24; S5 1, 2, 4, 0; S6 2; S9 20; T1 2 and 3; T2 1, 4, 5 and 2, 3, 6; T3 10; G1 8, 12, 6, 1; G2 17 and 16; G3 6 and 1; C1 No). U9 all (S3 table 47, 41, 74, 112, 117, 229 with 4B fewer; S4 60, 10, 7, 8; S6 48, 10, P; S7 60, 90, No; C1 65). U10 all (S2 3 ways, fewest pens 2; T2 Ali, Mei, Ben, Siti, Kumar is the only order; G3 12 or 24).

## What is in good shape
- Print file: 100 gray 1-bit CCITT images at 600 ppi, 100 pages, even. No colour dependence; graph series differ by solid line and circle against dashed line and square, shading is hatching.
- Welcome, contents, pace plan, answers divider (p79), progress, certificate: correct page numbers; build report has no problems.
- Wide boxes: every 5-digit answer has a wide box; narrow boxes remain only for answers of 4 characters or fewer.
- Figures: all Unit 6 figures are drawn to the angles printed in the key; Learn-it protractor and clock are clean.
- Every answer is stated first, then a Why, then the page of the question; shortened Why lines still explain, except M1 and M2 above.
- Licence: Preciouslyours Pte Ltd, UEN 201507566K, trading as Math Inquirers; no price, no examination or syllabus claims; no "Level 1" text.

## Remaining items before sale, in order
1. H1: rewrite the clone items (start with the verbatim ones: U9 S4, S5, S3, U7 T1, T2, T3, G3, S6, U3 T2, T3, U10 S2, S4, S5, S12) or decide the policy and edit the Welcome sentence.
2. M1: fix the U2 G1 Why. M2: restore the rabbit reason in U10 S7.
3. Remove the DRAFT line when the lawyer text is approved; fix the certificate plaque.
4. Low items as time allows (contents titles, wrapped boxes, "more times" wording).
5. Child trial: reading load of the Learn it pages, whether Unit 6 works without help, whether 25 to 30 minutes holds, whether the protractor and ruler are to hand.
