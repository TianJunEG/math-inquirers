# Independent audit: Level 4 Extension Workbook (self-study, with answers, ages 9-11)

Audited 23 Oct 2026, desk review by a model in a fresh session (no child tested). Report only: nothing in the book, data or tools was edited. Files: `outputs/extension/L4/*Soft_Copy_Colour.pdf` and `*Print_BW.pdf` (102 pages each; the `*_vector.pdf` was used for text only), `extension/data/l4_u01..u10.json`, `extension/l4/README.md`, `PROGRESS.md`, `TOOL_REQUESTS.md`. Method modelled on `extension/l1/AUDIT.md` and `AUDIT_2.md`; spec `docs/extension_books/plan.md`; wording `term/l1/WORDING_GUIDE.md`.

## Method and coverage (honest)
- **Items.** All 219 items plus 10 "Your turn" items (229 items, 422 separate answers) solved by me, not only the 60 percent asked. Text items were solved from the printed question (read from the data file, which the PDF prints one-to-one; checked on the rendered pages) and compared with every printed answer and "Why". Figure items (number lines, bar models, protractor, fan of rays, nets, graphs, tables, shapes, symmetry grids) were checked against the rendered figure, not the figure spec. A Python brute force of my own re-checked 30 risky items: factor counts (least number with 10 factors = 48), 4-and-7 boxes (17), stepwise rounding (1445), numbers 1-1000 with a 7 (271), numbers rounding both ways (100), nearest to 40 000 (38 641), digit-distinct bounds (74 986 / 65 012), signs and brackets uniqueness, missing digits (3, 3), unit-fraction sums, closest to 20 (19.64), area = perimeter rectangles (4x4, 3x6 only), fence with a wall (98), 3x3 symmetric patterns (10), the seating puzzle (unique), digit-sum 5 up to 200 (11), pens and notebooks (3 ways), the temperature puzzle, clock angles 100-160 (4, 5, 7, 8 o'clock), bus times. Also ran `verify/run_checks.py --level 4` (422 answers, 0 mismatches), `verify/wording_lint.py --level 4` (0 errors, 4 harmless warnings) and `verify/dup_check.py --level 4` with the private sources present (see Section D).
- **Result: 0 wrong answers, 0 unsolvable items, 0 wrong "Why" lines.** Four items have a second defensible reading (Section A). Maths quality is clearly better than the Level 1 pilot.
- **Pages.** Print edition, every page 1-82, 87-88, 91-92, 95-96, 101-102 viewed as images at 90 dpi (two-up); zoom at 170-300 dpi of pp. 41, 42, 44, 64 and the certificate. Answer pages 83-86, 89-90, 93-94, 97-100 read as text only (they are generated from the same data). Colour edition: pp. 1, 28, 42, 56, 64, 65 viewed; the rest by text and by comparison with print. Font sizes of every span measured with PyMuPDF (colour PDF).
- Print PDF: `pdfimages` shows 102 images, gray, 1 bit, CCITT, 4958x7016 (600 ppi): correct 1-bit print format. No colour dependence found: graph lines differ by solid/dashed and circle/square, shading is hatching, Mi is halftone.

## Verdict
**Ready to sell after fixes.** The maths, the keys, the tier structure, the licence page and the 1-bit print file are in good shape. Five High items must be fixed first (Welcome page equipment text, repeated holiday items, two answer give-aways, the Unit 6 protractor figures, narrow answer boxes for 5-digit answers). They are small, but the repeated items need new items and a re-run of the answer checks. A child trial for pace and reading load is still needed (not replaceable by this review).

## Findings

### High

**H1. Welcome page (p3, both editions) has a stale line and misses the equipment the book needs.**
- Print p3 "For the grown-up" ends: "The rulers in Unit 9 are printed at real size." Level 4 has no rulers; this is a Level 1 leftover (Level 1 Unit 9 is Length). The soft copy says "Print at 100 percent so the rulers are true size" (also wrong: there are protractors, and only the real-size Unit 6 angles matter).
- Nothing on p3 or the pace plan (p5) says a **180 degree protractor, a ruler and a pencil** are needed; the only mention is one sentence on the Unit 6 Learn it page (p41), in week 6. Unit 6 Start here 1 (p42) cannot be done without them. Fix: p3 "You will need: pencil, rubber, ruler, a 180 degree protractor (Unit 6)"; delete the Unit 9 sentence (Level 4: "Print at 100 percent so the angles on page 42 are the right size").
- The label "Beyond Level 4: ..." (9 items) is never explained on the Welcome page; add one line ("Beyond Level 4 means ahead of the school year; it is fine to skip").

**H2. Repeats of holiday items (same story and same structure, only the numbers changed). The spec says new contexts, never a repeat.** Compared 242 items with `p4/content/l1..l10.js` by sentence similarity and read the top 30. The REVIEW list of `dup_check.py` (Section D) shows only skeletons; these are the ones a child who attended will recognise:
| Item (page) | Holiday source | What is shared |
|---|---|---|
| U9 Learn it Try (p62) "stall sold 35 cups Mon, 60 cups Tue, by how many did sales go up" | l9.js "stall sold 45 bowls of laksa Mon and 60 Tue, by how many bowls did sales go up" | whole item |
| U9 T3 (p66) "Tank A 100 L loses 4 an hour, Tank B 15 L gains 13, lines cross" | l9.js "Tank A 80 L loses 6, Tank B 20 gains 9, the two lines cross" | story, question, method |
| U10 T1 (p73) "hawker centre, 14 tables, 4 or 6 seats, 68 people; (a) tables that seat 6 (b) fewest and most" | l10.js "hawker centre 15 tables, 4 or 6, 76 seats; (a) tables seating 6 (b) fewest and most" | whole item minus (c) |
| U10 T2 (p73) "five children in a row of 5 seats, numbered 1 to 5 from the left; end seat; not next to" | l10.js "Ali, Ben, Mei and Siti in a row of 4 seats, numbered 1 to 4 from the left; Mei at one end; Ali not next to Ben" | story, clue types |
| U10 T3 (p73) grandfather 7 times, in 12 years 3 times | l10.js uncle 4 times, in 10 years twice | structure, question |
| U10 S8 and C3 (p72, p75) "9th from the front and 5th from the back" | l10.js "Mei 7th from the front, 12th from the back"; "20 people, Ben 6th from the front" (U10 S8(b) is the same two-part shape) | structure |
| U10 S9 (p72) ages total 44, in 6 years 3 times | l10.js "Ben and his father 50, in 5 years 3 times" | structure |
| U8 T1 (p59) cube numbered 1-6, "Face 1 touches ..., Face 2 touches ..." | l8.js same wording | structure, wording |
| U8 G2 (p60) "shade exactly 5 squares of a 5 by 5 grid, 4 lines of symmetry" | l8.js same with a 3 by 3 grid | wording |
| U1 S8 (p8) "Bus A every 8 min, Bus B every 12 min, both leave 9:00" | l1.js "Bus A 6 min, Bus B 8 min, both leave 7:00 am, next together after 24 minutes" | story, and the answer (24 min) |
| U9 S7 (p65) "scale starts at 50, each line 20, Ali 4 lines, Mei 9 lines" | l9.js "scale starts at 100, each line 25, Ali 3 lines, Mei 7 lines" | wording |
| U2 S10 (p16) 5-digit riddle, rounds to 52 000, hundreds 7, tens 5, ones 2 | l2.js 5-digit riddle, rounds to 48 000, hundreds 6, ones 1 | structure |
Fix: change story and structure of at least U9 Try, U9 T3, U10 T1, U10 T2, U10 T3, U8 T1 (new item type, same skill), U1 S8, U9 S7; accept the rest as "same type". Then rerun `l4_uNN_checks.py`, `dup_check.py`, the build. Also U8 Check yourself Q1 (p61) is the same net as Start here Q1 option C (see M5).

**H3. Two Go further items give the answer on the page.**
- **U1 Go further 1 (p11)**: "What is the least number that has exactly 10 factors?" prints the writing line label **"Factors of 48:"** and the upside-down hint "Count factors of numbers that are 24, 30, 36, 40 and 48." The answer, 48, is in both. Fix: label "My factor lists:" and a hint such as "Count the factors of some numbers between 20 and 60".
- **U3 Go further 3 (p25)**: "3 [] 4 x 7 = 2 [] 3 8"; the hint "Multiply 334-style numbers by 7" states the first missing digit (3) and the number 334. Fix: "Start with the ones: 4 x 7."
- (Also see M4 for the U3 T3 hint, which is garbled.)

**H4. Unit 6 protractor figures are hard to read in the 1-bit print file (the central skill of the unit).** Zoomed at 170 dpi:
- **p42 Start here 2 ("Read the angle from the protractor")**: the two scale rows (outer and inner) collide: "130" is struck through by the arm, "50" overlaps "60", "70 80 90100 110" run together, "180-0" is crossed by the baseline at both ends. Number labels measure 9.6 pt. A child cannot tell which of 50 or 52 is meant. There is also **no arc marking which angle is meant**: the baseline runs through both sides, so 52 and 128 are both "the angle" (the Why concedes "the other scale says 128"; part (b) cannot settle it). Fix: draw only the baseline arm that carries the 0, mark the angle with an arc, thin the labels (every 10 on the outer ring, every 10 on the inner ring, offset), or show only 0-90-180 numbers plus ticks.
- **p41 Learn it protractor** has the same crowding ("120/60", "150/30", "90/90", "180 0" at both ends touching) and does not show the arm at the 0 that the text tells the child to use.
- **p44 Start here 7 (corner angles)**: the label backgrounds cut the rays and the vertical arm (the "37°" box breaks the vertical line; in (b) the two rays are broken into stubs and "28°" and "19°" sit side by side on top of them). Readable with effort, but looks broken. Fix: place labels beside the arcs, not on the rays.
- p42 Start here 3 fan of rays: arc labels "25° 35° 40°" are about 8 pt and crowd the vertex.

**H5. Answer boxes are about 15 mm wide, too narrow for 5-digit answers.** The README says "5-digit answers fit the boxes" (16 x 10 mm). Measured on p16 and p17: boxes are 15-16 mm; a 9-11 year old's five digits plus a gap need about 22-25 mm. Affected: U2 S5, S10, S11 (three boxes), S12, T1, T2, T3, G1, C3, C4 and U2 S1 (cells are wide, fine); U3 S1(a), C1 ("23 640"); U1 none. Fix: wider boxes for answers of 5 or more characters (the table cells in U2 S1 are the right size).

### Medium

**M1. Unit 9 Start here 8(c) (p65) has two defensible answers.** "At what time was it 29 °C? [ ] am": it is 29 °C at 9 am (rising) and again at 2 pm (falling: 35, 32, 29). The "am" after the box steers to the key but a careful child who finds 2 pm is told they are wrong. Fix: "At what time before noon was it 29 °C?"

**M2. Unit 4 Think harder 2 (p31) "a toy took 1/3 of it".** "It" can be her money (key 90) or what was left after the book (then 60). The hint says "same whole", the key assumes it. Fix: "1/3 of her money".

**M3. Unit 3 Think harder 3 hint (p24) is wrong.** "After the gift, Mei has 36 + 36 more than 1 unit." After the gift they are equal; the true statement is "Before the gift Mei has 36 + 36 more than Lily". Fix the hint.

**M4. Other hints state the whole method, not a nudge** (Level 1 audit M6): U4 T2 ("Use 15 units"), U4 G3 (the whole first step), U9 T2 ("Day 1 is 1 unit. Day 2 is 2 units. Day 3 is 2 units and 15 more" is the complete bar model), U10 G2 ("Make groups of 3 twenty-cent coins and 1 fifty-cent coin" is the solution), U10 G1, U1 T1 ("List the multiples of 24"), U8 G2 ("The middle square is always shaded"). Hints are the correct size (11 pt, one line, upside down) but the first hint should only start the child. Fix: replace with a question ("What do 3 twenty-cent coins and 1 fifty-cent coin cost together?" is also too much: use "Try a small case first").

**M5. Untaught prerequisites on Learn it pages** (worked example present on every Learn it page: 2 worked examples, a how-to box, a facts box and a Try: good).
- **U4 (p27):** equivalent fractions (S9, S7, S8 ordering needs a common denominator), whole-from-a-part (S6, C4) and mixed numbers on a number line (S5) are used but not shown; Learn it covers only improper/mixed and fraction-of-a-set. Add a line "Equivalent: multiply or divide the top and bottom by the same number" and a bar showing "3/7 = 36, whole = ?".
- **U8 (p55):** how to decide that a net does not fold (S1 needs "4 squares round a corner", "5 in a row"), counting lines of symmetry, and surface area (S8 "area of the card" for a 4 x 3 x 2 box) are not taught. S8 is surface area of a cuboid: beyond Primary 4 and unlabelled in Start here. Make it a cube-only item or move it to Think harder with "Beyond Level 4".
- **U10 (p69):** the logic grid (S7) and age puzzles (S9, T3) have no worked example; only "Draw a queue or a bar model".
- **U6 (p41):** the notation "angle AOC" (S3) and "angle BOD" is not introduced.
- **U8 Check yourself 1 (p61)** is the same net as Start here 1 option C (2-2-2 staircase). A child who did S1 recognises it. Change the net.

**M6. Pace plan is optimistic for sessions 1 and 3 (p5).** Session 1 = Learn it (dense page: two worked examples, how-to, facts, Try) plus Start here 1 in 20-25 minutes, e.g. Unit 6 (read the Learn it, then measure three angles with a protractor and make arms longer with a ruler, read a protractor, three fan angles) or Unit 3 (page of four 4-digit calculations). Session 3 = Think harder (3 multi-step items with working lines and a hint) plus Check yourself (4 items, score, look back) in the same time, for 9-11. Go further as a weekend page is a good fix (carried over from Level 1). Suggest "25 to 30 minutes", or move "Check yourself" to the weekend page with Go further. Needs the child trial.

**M7. Figure and text size in the print edition.**
- Learn-it figure text below 10 pt: U1 p6 table 9.3 pt, U3 p20 machine labels 9.3-9.9 pt, U6 p41 protractor 9.6, U7 p48 table 9.6, U9 p62 table 9.1, U10 p69 tables 9.1 (README claims `figs.MIN_PT` 10 pt: not true for these). U5 Learn it number lines (p34) have 8-9 pt labels and very small ticks.
- U9 Start here 4 (p64): the Ali and Mei lines overlap from Week 6 to Week 8; at Week 8 the 90 circle sits behind the 85 square, which part (d) ("Ali first has more than Mei in Week [ ]") needs; in 1-bit this is a coin toss for a child. Offset the markers or add data labels at Weeks 6-8, or ask (d) from the table of values.
- U9 Start here 6 (p65): Bakery Q's axis labels 52...40 (about 8 pt, one every 2 units) are crowded with the zigzag mark.
- U9 Check yourself 1 (p68): graph plot is 62 x 25 mm with labels about 8 pt; reading 65 (halfway between 60 and 70) means a 1.5 mm judgement. Enlarge.
- U7 Think harder 1 (p52) and Check yourself 1 (p54): the shapes are 13-30 mm and the labels small (about 8 pt: "9 cm", "3 cm"): enlarge a little.

**M8. "Beyond Level 4" label.** Nine items carry it, all in Think harder or Go further (U1 G2, U2 G2, U3 T1 and G1, U4 G2, U6 T1, U8 G1, U9 G3, U10 G4): **no beyond item in Start here, and the label reads "Beyond Level 4" everywhere, no "Level 1" leak** (confirmed in both PDFs). It is printed as a bold first line of the stem, so it looks like a title and not a label; Level 1 uses a badge. The tool fix in `TOOL_REQUESTS.md` would make Level 4 consistent. Syllabus check of beyond items against `docs/syllabus_map/tier_rows.json`: order of operations (Primary 5) labelled, average (P5) labelled, angles on a line and at a point (P5) labelled, painted cubes, number cycles, unit fractions, three common multiples labelled. Items beyond Primary 4 that are **not** labelled: U8 S8 (surface area of a cuboid, see M5), U9 T3 and U3 G2 are fine; U4 C3 "5/8 or 7/12" and U4 G4(c) need 24ths and 20ths (the project notes treat fractions with unrelated denominators as Primary 4, so no change, but C3 is a hard Check yourself item).

**M9. Items per unit (units 6-9).** Counts (items, with the Try): U1 24, U2 24, U3 22, U4 24, U5 23, U6 21, U7 20, U8 20, U9 18, U10 23. Separate answers 33-50 per unit, 422 in all. Units 6 to 9 have 8-10 Start here items instead of 13-14. **Acceptable**: the items are multi-part and figure-heavy and the answer count (35-46) is close to the others; the pages are full. U9 (8 Start here items) is the thinnest; if page budget allows add one Start here item in U9 and U7.

**M10. Tier honesty.**
- Start here holds a few Think-harder types: U1 S13 (odd count of factors, new idea after only a "good to know"), U2 S11(c) greatest odd number, U4 S12 (fraction of the rest), U10 S2 (list all ways), U10 S9 (ages), U9 S8(c) (see M1). Reasonable for Level 4.
- Some Think harder or Go further items are no harder than Start here: U1 T1 and T3 (LCM and a digit riddle), U6 T1 (beyond-labelled angle sums, one step), U9 T1 (same skill as S5), U3 T2 (same as S11), U2 G3 (woven pattern), U3 G2 (fill a table), U5 G4 (add 0.05). Swap one in each unit if possible.
- Check yourself repeats earlier items closely: U7 C3 = S6 type, U5 C4 = T1 type, U10 C3 = S8 type (acceptable: a quick check).

### Low
1. **Contents (p4)** prints each unit title twice ("Factor Hunters" and "Factor hunters · follows ..." in lower case). Print the unit title once.
2. **Print edition Welcome and licence are edition-specific** ("This printed book is licensed to the buyer" is right), but the soft copy's Welcome tells a reader to print at 100 percent while the pace plan has no "Real size" note on the pages that matter (p42).
3. **Answer layout.** Check yourself questions put a second answer box on the next line (U2 C2, C4; U10 S11 third box; U10 T1(b)); the box is easy to miss. Keep boxes on the same line.
4. **U1 G4 (p11)** "Length [ ] Width [ ]": give 12 and 7 or 7 and 12? Say "The length is the greater side" (as U7 S3 does).
5. **U6 S8(b) and T3(b)** "In all it turned [ ]°": the total turning is 270 and 495, but the net turn is 0 and 135 (the robot ends where it began in S8). Say "The turns add up to [ ]°".
6. **U9 S7(c)** states a child's wrong reasoning in the stem (WORDING_GUIDE rule 19). **U3 S1 and U5 S11** "Work these out" (rule 14: "Find the value of"). U2 S4 and others "Write the numbers in order. Begin with the greatest" (rule 13: "Arrange"). U1 G3, U4 G1 start with "Think about ..." with no command.
7. U7 T1 figure (a 13 x 13 mm dashed square) is a small object.
8. **U9 G1** has no figures for Graph X and Y (text only): add two small graphs, or keep it as an arithmetic item.
9. **Certificate (p77)** Mi's trophy plaque carries pseudo-text (garbled letters in the Mi image). Check the asset and replace the plaque with a blank or "Well done".
10. **Licence page.** Present and correct: Preciouslyours Pte Ltd, UEN 201507566K, trading as Math Inquirers; email pypteltd@gmail.com; registered office 66 Tannery Ln, Singapore 347805; business WhatsApp +65 9880 5962; "DRAFT licence text, for owner and lawyer approval. Not final." in both editions (a printed DRAFT line must be removed before sale). The UEN is not found in `docs/terms/`; owner to confirm.
11. **Cover** Mi is about 15 percent of the page, no speech, no numbers: fine. **Page 78** is blank and answers begin on p79, a right-hand page: correct for a bound book.
12. **Grammar and unit wording:** "tiles along the edge are dark" (U7 S9, G4) draws nothing; a small drawing would help. U7 S1(a) wraps "a = [] cm b = []" over two lines.
13. **Colour edition** was not read page by page; spot checks show the same layout, with figures differing only in fill.

## D. Originality and compliance
- **No price anywhere** (grep of the colour text and the vector print file). **No SASMO, MOE, GEP, PSLE, olympiad, gifted or syllabus text** ("not an official school or examination book" only). **No tutor or class dependence** ("class" occurs only in story items: classes borrowing books, a class with 32 children; "teacher" in U1 S3 story; "You do not need to have joined it" is the Welcome line).
- "Holiday Program" is defined on p3 ("our school-holiday course") and each unit header says which lesson it follows.
- **`extension/verify/dup_check.py --level 4` re-run with the private sources present:** corpus holiday 11 files, 49 181 7-grams; external 48 files, 519 102 7-grams; 239 question texts; **no shared 7-word run with the holiday bank or the private sources ("OK")**. The REVIEW list (54 entries) was read: all are stock command skeletons ("all the factors of # in order", "the common factors of # and #", "use the digit cards # # #", "round # # to # decimal place", "an area of # cm² its length", "# cm long and # cm wide", "angle between the clock hands at #", "multiply to make # what are they", "#th from the front and #th from the back", "buys some # pens and some #", "# seats numbered # to # from"). Most are acceptable. Those that signal a real repeat of a holiday item are in H2 (U10 S1, S2, S8, T2, C3, C4; U8 S7, S8, G2; U9 S3, S7, T3; U1 S8; U2 S10). U10 S1 and C4 are the same item type as the holiday's "next-door numbers" and are fine as "new numbers", but they sit with U10 S8 and C3 in the clone list because the whole unit mirrors holiday Lesson 10 item by item. No item copied from private papers was found; the contest-style items (Frobenius coin problem U1 G3, painted cubes U8 G1, number cycles U10 G4) are standard puzzles, written freshly.
- Spot comparison against `p4/content` (20 items, by sentence similarity of the whole stem): the top matches were U3 C4 "I think of a number" (type only), U10 C4 "next-door numbers" (type only), U2 C4 / S12 "find the rule" (type only), U9 Try, U9 S7, U9 T3, U10 L1/T1/T2/T3/S8/S9, U8 T1/G2, U1 S8, U1 G1 "least number with exactly 6 factors" (here 10: same type, fine). Details in H2.
- Cast (Ali, Mei, Siti, Ben, Kumar, Aisha, Ravi, Wei, Lily, plus Mr Tan, Mrs Lee): consistent with the guide.

## E. Syllabus level and consistency with the holiday program
- The 10 units follow the 10 holiday lessons in order, with the same question types (factor pairs; rounding; four operations with bar models; mixed numbers and fractions of a set; decimals; angles; area and perimeter; nets and symmetry; line graphs; puzzle heuristics). Items beyond Primary 4 sit in Think harder or Go further with the label (Section M8), with one exception in Start here: U8 S8.
- Start here is school-range, Think harder is Section C part (a) style with a hint, Go further is longer or harder. Reading load is acceptable for 9-11 (max sentence 20 words).

## Checks that passed
102 pages in both files, even count; contents page numbers (6, 13, 20, 27, 34, 41, 48, 55, 62, 69) and answer page numbers (80, 82, 84, 86, 89, 91, 93, 95, 97, 99) all correct; pace plan page numbers correct; every unit has Learn it with two worked examples, a how-to box, a facts box, a Try with its answer at the back; every item has an answer and a "Why" (answer type 11.6 pt, much better than Level 1); 4-item Check yourself with score rule and Look back in every unit; hints printed upside down at 11 pt, one line; no overflow or clipping found on any viewed page; B&W conversion loses nothing (hatching, dash and marker differences hold); no colour-only meaning; writing space is generous (working lines, bar-model boxes, "List:" lines); cover, certificate and progress pages fine; DRAFT licence marking present.

## Ranked top 10
1. Welcome page: stale "rulers in Unit 9" line and no protractor/ruler list (H1).
2. Repeats of holiday items, 8 to 12 items (H2).
3. Two answer give-aways in Go further: U1 G1 "Factors of 48:", U3 G3 "334-style" (H3).
4. Unit 6 protractor and corner figures: label collisions, no marked angle (H4).
5. Answer boxes too narrow for 5-digit answers (H5).
6. U9 S8(c) two answers (9 am and 2 pm); U4 T2 "of it"; U3 T3 hint wrong (M1-M3).
7. Untaught prerequisites: U4 equivalent fractions, U8 nets and surface area, U10 logic grid and ages (M5).
8. Hints that state the method (M4).
9. Figure text and size: Learn-it figures under 10 pt, U9 graphs, U9 S4 markers overlap (M7).
10. Pace plan sessions 1 and 3 (M6) and the "Beyond Level 4" label style (M8).

## What a child trial still has to answer
Reading load of the Learn it pages; whether Unit 6 is too hard without help; whether 20-25 minutes works for session 1 and 3; whether the protractor and ruler are to hand; whether the 5-digit boxes are used or ignored.
