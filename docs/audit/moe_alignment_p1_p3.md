# MOE syllabus alignment audit: Math Inquirers Levels 1, 2 and 3 (P1 to P3)

Audit date: 22 Oct 2026. Read-only audit of lesson content; no lesson files were edited. Scope: Level 1 (hp/lessons.js, hp/qbank.json), Level 2 (p2/content/l1..l10.js), Level 3 (p3/content/l1..l10.js), the scheme-of-work PDFs, docs/levels_and_placement.md, docs/gifted_research.md section 3, and parent-facing labels in website/ and levels/.

Labels: **[OFFICIAL]** = read directly in the MOE PDF. **[SECONDARY]** = non-official. **[UNVERIFIED]** = could not confirm. Nothing below is from memory unless it says so.

## Verified against MOE syllabus (Oct 2025)

Re-checked on 22 Oct 2026 against the supplied PDF "Mathematics Syllabus Primary One to Six" (footer "Updated: Oct 2025", 50 pages). Full summary: `docs/moe/syllabus_by_level.md`; every change: `docs/moe/verification_report.md`. Result for Levels 1 to 3: every ON / ABOVE / NOT IN call below was confirmed (all P1 to P3 outcome numbers, p. 31 to 36, match), with two corrections:

1. **Three-denominator fraction sums** (P3 Level 3 lesson 6 Stretch s8, "1/2 + 1/4 + 1/8"). Was "ABOVE (P4)". The P4 outcome allows "not more than two different denominators" (P4 Fractions 3.1, p. 37) and no later year relaxes it, so this is beyond the primary syllabus (NOT IN), not just a P4 preview.
2. **"Diagonal"** (M10). Was "first referred to in P4 (Rectangle and Square 2.1)". P4 2.1 says "properties of rectangle and square, excluding diagonal properties" (p. 39): diagonals are explicitly left out of the primary syllabus, so the word is NOT IN at any year (rewording advice unchanged).

Also settled here: bar models are not named anywhere in the syllabus (no hit for "bar model" or "model drawing" in the full text); pentagon, hexagon and octagon are not named in any year; common multiples are P4 (p. 37); letters for unknowns are P6 (p. 43); odd and even are P2 (p. 33); remainders P3 (p. 35); seconds, start/finish/duration and the 24-hour clock P3 (p. 36). Items marked [UNVERIFIED] in sections 3 and 6 about school conventions (time layout, remainder layout, cents symbol, "breadth") stay unverified: the syllabus does not specify them.

---

## 1. Syllabus document used

| Item | Detail |
|---|---|
| Document | "MATHEMATICS SYLLABUS Primary One to Six, Implementation starting with 2021 Primary One Cohort" (the 2021 syllabus). The cover does not carry the title "Primary Mathematics Teaching and Learning Syllabus"; the MOE page calls it "2021 Mathematics Syllabus (Primary 1 to 6)". |
| Version/date | Footer on every page: "Updated: Oct 2025". PDF creation date 9 Oct 2025. Copyright 2025 Curriculum Planning and Development Division. 50 pages. |
| URL (downloaded and read in full, 22 Oct 2026) | https://www.moe.gov.sg/media/files/primary/92bff26d-b2b4-4535-b868-b8415c744b91.pdf |
| Listing page | https://www.moe.gov.sg/primary/curriculum/syllabus (Mathematics row reads "2021 Mathematics Syllabus (Primary 1 to 6) (788KB) (Updated October 2025)"). |
| Is it the latest? | It is the newest I could confirm, and it is what the MOE page linked on 22 Oct 2026. Earlier revisions exist: search results show a "Dec 2023" copy on school sites and an MOE file named "...updated-dec-2024.pdf" (that URL returned 404 for me, so I did not read it). I cannot rule out a revision published after the MOE page I fetched. |
| Rollout note in the PDF | The 2021 syllabus applies to P1 to P5 in 2025 and to P6 from 2026. So P1 to P3 are fully on the 2021 syllabus. |
| Not needed | The SEAB PSLE page (404 on fetch) is only relevant to P6. The P1 to P3 content comes entirely from the MOE PDF. |

Tool note: WebFetch returned empty pages for the PDF; I downloaded it with curl and read the text (pdftotext). Search-engine summaries were not used for any syllabus fact.

### What the syllabus says for P1 to P3 [OFFICIAL]

Content is organised in 3 strands: Number and Algebra, Measurement and Geometry, Statistics. Outcome numbers below are the PDF's own (for example P2 Fractions 1.3).

**Primary 1**
- Number and Algebra. Whole numbers: numbers up to 100 (counting, place value in tens and ones, reading and writing in numerals and words, comparing and ordering, patterns in number sequences, ordinals first to tenth with symbols 1st, 2nd, 3rd); addition and subtraction (use of + - =, relationship, adding more than two 1-digit numbers, within 100, algorithms, mental calculation within 20); multiplication and division (concepts, use of x, multiplying within 40, dividing within 20). Money: cents up to $1, dollars up to $100.
- Measurement and Geometry. Length in cm (use of "cm", ordering, measuring and drawing to the nearest cm). Time: tell time to 5 minutes, "am" and "pm", abbreviations "h" and "min", durations of one hour or half hour. 2D shapes: rectangle, square, triangle, circle, half circle, quarter circle; forming figures; identifying the shapes in a figure; copying figures on dot or square grid.
- Statistics. Picture graphs (reading and interpreting).

**Primary 2**
- Numbers up to 1000 (tens/hundreds counting, hundreds-tens-ones, odd and even, patterns); addition and subtraction algorithms up to 3 digits and mental calculation; multiplication tables of 2, 3, 4, 5, 10, use of the division sign, relationship of x and /; fractions as part of a whole (unit fractions, like fractions, denominators not exceeding 12, add and subtract like fractions within one whole); money in dollars and cents, decimal notation, converting between decimal notation and cents.
- Length in m, mass in kg/g, volume of liquid in litres, abbreviations m, g, kg, l; time to the minute, hours and minutes to minutes and back. Patterns with 2D shapes by size, shape, colour, orientation. 3D shapes: cube, cuboid, cone, cylinder, sphere. Picture graphs with scales.

**Primary 3**
- Numbers up to 10 000; addition and subtraction algorithms up to 4 digits; mental calculation of two 2-digit numbers; tables of 6, 7, 8, 9; division with remainder; multiplication and division algorithms (up to 3 digits by 1 digit); equivalent fractions, simplest form, comparing unlike fractions (denominators not exceeding 12), adding and subtracting two related fractions; adding and subtracting money in decimal notation.
- Length in km, volume in ml, compound units and conversion (km and m, m and cm, kg and g, l and ml); time in seconds, finding start/finish/duration, 24-hour clock; area and perimeter (concepts, cm2 and m2, perimeter of rectilinear figure/rectangle/square, area of rectangle/square); angles (right angle, greater/smaller than a right angle); perpendicular and parallel lines (identify and draw). Bar graphs, including different scales on the axis.

**Processes and conventions [OFFICIAL]**
- Section 2 names mathematical processes as abstracting, reasoning, representing and communicating, applying and modelling, plus metacognition and attitudes. Problem solving is described with Polya's four steps and "heuristics" in general terms. The PDF does **not** list specific heuristics and does **not** use the words "bar model" or "model drawing" (I searched the extracted text; the only "model" hits are "modelling"). Footnote: primary students are expected to formulate real-world problems mathematically and check reasonableness; formal modelling is a secondary-level topic.
- Notation/vocabulary stated inside outcomes: tens, ones, hundreds, thousands; "am"/"pm" (no full stops in the PDF); "h" and "min"; cm, m, km, g, kg, l, ml, cm2, m2; use of +, -, =, x, division sign; unit fractions, like fractions, equivalent fractions, simplest form, denominator and numerator; "decimal notation" for money; "division with remainder". Later years (not yet met): approximation sign, angle notation and degrees (P4), mixed numbers and factors/multiples (P4), percentage/rate (P5), ratio and letters for unknown numbers (P6 Algebra 1.1, 1.2).
- The PDF does not prescribe a time format (5:40 vs 5.40 vs 0540 h), a remainder format ("r 1"), or the symbol for cents. Those are **[UNVERIFIED]** conventions.

---

## 2. Lesson-by-lesson alignment

Key: **ON** = in the syllabus for that year. **BELOW** = syllabus covers it in an earlier year. **ABOVE (Pn)** = syllabus covers it in year n later. **NOT IN** = not named in the 2021 syllabus for any primary year (puzzle skill or enrichment topic). A lesson gets a verdict for its main topic; mixed lessons list the exceptions in the last column. "Core" means the six or so Core items, "Stretch" and "Challenge" are the Think Harder and Go Further items.

### Level 1 (Primary 1, ages 6-8)

Note on framing: the scheme PDF and tutor guide describe Level 1 as a holiday programme "for children finishing Primary 1", so items from the P1 syllabus are consolidation and anything from P2 onwards is a preview, not just enrichment.

| L | Topic | Main verdict and MOE outcome | Exceptions in Stretch/Challenge or other items |
|---|---|---|---|
| 1 | Number patterns (skip count 2s, 3s, 5s; add/take-away rule) | **ON.** P1 Whole Numbers 1.6 "patterns in number sequences"; also 3.3 "multiplying within 40" (skip counting is the groundwork). | Stretch "Frog A in 3s and Frog B in 4s, which numbers do both land on", "3s and 5s... more than 10 and less than 40", "Ali counts 2s... Mei 5s": common multiples, **ABOVE (P4** Factors and Multiples 2.5). Challenge "1,2,4,7,11,16... 8th number": growing-difference sequences, **NOT IN**. Challenge "how many different patterns... 5th number is 20": open enumeration, **NOT IN**. |
| 2 | Number bonds to 10 and 20, balancing "=" | **ON.** P1 Addition/Subtraction 2.1 to 2.3 (concepts, use of "+ - =", relationship), 2.7 mental calculation within 20. | Stretch "A + A + 4 = 20, the two As stand for the same number": letter for an unknown, **ABOVE (P6** Algebra 1.1). Magic triangle: **NOT IN**. Challenge "Ali 20 stickers, keeps 9, Ben gets 3 more than Mei": comparison/bar-model, **NOT IN** (uses P1 arithmetic). |
| 3 | Picture graphs and class vote | **ON** for 1 picture = 1 child. P1 Statistics 1.1 "reading and interpreting data from picture graphs". | Stretch "1 picture = 2 children", half picture; Challenge "1 picture = 3 children": picture graphs with scales, **ABOVE (P2** Statistics 1.1). "What a class vote can and cannot tell us" (sampling): **NOT IN**. |
| 4 | Repeating and growing patterns | **Mixed.** Number sequences ON (P1 1.6). Repeating shape/colour patterns and "what is the 10th/100th one": patterns with 2D shapes by shape/colour are **ABOVE (P2** Geometry 1.1). Growing stick patterns: **NOT IN** as a named topic. | Core items go to the 11th and 12th place; Stretch to 14th, 20th, 23rd, 25th, 100th; Challenge 33rd and 47th: ordinals beyond tenth (P1 stops at tenth, see section 3). "How many sticks left over / how many squares with 50 sticks": division with remainder, **ABOVE (P3** Multiplication and Division 3.3). "Odd places are circles" (exit ticket key): odd/even is **ABOVE (P2** Whole Numbers 1.6). Challenge "Dots 1, 3, 6, 10, 15": triangular numbers, **NOT IN**. |
| 5 | Working backwards ("I think of a number...") | **ON** at core level: P1 2.3 "relationship between addition and subtraction", numbers within 100. | Number-machine tables (IN/OUT), queue problems, 3 and 4 step stories: reasoning skill, **NOT IN** as named topics. Challenge "snail climbs 3 cm and slides 1 cm": **NOT IN**. Challenge "Ali and Ben 20 marbles, Ali has 4 more" and L10 "Ali, Ben, Mei 29 stickers": comparison problems, arithmetic ON, structure **NOT IN**. |
| 6 | Money (coin combinations) | **ON.** P1 Money 1.1 "counting amount of money in cents up to $1; in dollars up to $100". Notes up to $50 and $34 + change are within $100. | "How much change" (Core T "Ali buys ruler 35c... 50c coin", "$34 bag, $50 note") is subtraction in context; the syllabus lists counting amounts only for P1, so treat as an application of P1 subtraction, **ON by extension**. Amounts like 95c with fewest coins and "every set": systematic listing, **NOT IN**. 100c written as $1 is fine. |
| 7 | 2D shapes (sides, corners, counting shapes) | **ON** for triangle, square, rectangle, circle (P1 Geometry 1.1, 1.2, 1.3). | Pentagon, hexagon, octagon (Q2, exit ticket, Core Q3 hexagon): not in the P1 shape list and not named in any year of the PDF, **NOT IN**. Parallelogram accepted in Q5 key: **ABOVE (P5** Geometry 3.1). Word "diagonal" in the Explore, Think Harder and Challenge text: **NOT IN** (P4 Rectangle and Square 2.1 says "excluding diagonal properties", p. 39; corrected from ABOVE (P4)). Counting all squares/rectangles/triangles in grids and "4 squares joined" shape enumeration: **NOT IN**. Half circle and quarter circle (P1 list) are never taught in this lesson. |
| 8 | Logic and sorting | **NOT IN.** Venn diagram, logic grids and ordering from clues are not in the P1 to P3 syllabus. | Core "odd and even" sorting: **ABOVE (P2** 1.6). Counting in 2s, 3s, 4s, 5s overlap: see L1 (common multiples, **ABOVE P4**). Challenge "all orders of three people" (permutations) and "labels all wrong" box puzzle: **NOT IN**. |
| 9 | Length (cubes, clips, cm ruler) | **ON** for cm. P1 Length 1.1 to 1.4 (measure in cm, compare/order lengths, measure a line to the nearest cm). | Non-standard units (cubes, clips, spans, erasers) and converting between them (1 clip = 3 cubes): not listed in the 2021 P1 outcomes, **NOT IN** (supports the P1 concept; I did not find a P1 outcome that names non-standard units). "Cut a ribbon into equal pieces" ON (division within 20). Challenge "ribbon 30 cubes into three pieces, first 4 more than second": comparison problem, **NOT IN**. |
| 10 | Mixed puzzles | **Mixed**: draws on L1 to L9, so the same exceptions apply. | Challenge "secret number between 20 and 60 in 3s, 5s and one more than 4s": common multiples **ABOVE (P4)**. Challenge "triangles and squares sticks, same number of sticks": **NOT IN**. |

Level 1 summary: the Core items are almost all ON-level or consolidation of P1 skills. The recurring ABOVE items are common multiples (L1, L8, L10), picture-graph scales (L3), repeating shape patterns/odd-even/remainders (L4), and one use of a letter for an unknown (L2 Stretch).

### Level 2 (Primary 2, ages 7-9)

Note: SPEC.md says P2 children are "finishing Primary 2" (going into P3).

| L | Topic | Main verdict and MOE outcome | Exceptions |
|---|---|---|---|
| 1 | Numbers to 1000, digit cards | **ON.** P2 Whole Numbers 1.1 to 1.5 (place value hundreds-tens-ones, counting in tens/hundreds, comparing/ordering, patterns). | Stretch s3 "3 hundreds, 14 tens, 6 ones" (renaming): ON in spirit. Digit-sum puzzles, "how many 3-digit numbers...": **NOT IN**. Reading and writing numbers in words (1.3) is never taught. |
| 2 | Addition and subtraction within 1000, missing digits, magic squares | **ON.** P2 Addition/Subtraction 2.1 (algorithms up to 3 digits). | Core c1, c2, c3, c5 and Stretch s2, s3, s6 use a letter A (and B) for a missing digit or number: **ABOVE (P6** Algebra 1.1; see section 3). Challenge c2 "A + 150 = 550 - A" (unknown on both sides): **ABOVE (P6** Algebra 1.5 and beyond). Magic squares/triangles: **NOT IN**. |
| 3 | Multiplication and division (arrays, legs and wheels) | **ON.** P2 Multiplication/Division 3.1 to 3.4 (tables of 2, 3, 4, 5, 10). | "Share with leftovers" (Core c3-style, Stretch s3, s5, Challenge c6, c8): division with remainder is **ABOVE (P3** 3.3). Challenge c1, c3, c6, c8: groups-with-remainders and "number that leaves remainder 2 on 5 and 3 on 4" are common-multiple style, **ABOVE (P4)**. Legs-and-wheels two-unknown tables: **NOT IN**. |
| 4 | Patterns with multiplication | **ON.** P2 1.5 "patterns in number sequences"; P2 Geometry 1.1 (patterns with 2D shapes). | Stretch s5, Challenge c7, c9 "numbers both say": common multiples **ABOVE (P4** 2.5). Challenge c1 "every 3 seconds... 5 seconds": seconds are **ABOVE (P3** Time 2.1). Growing patterns with a rule (sticks, towers, tiles): **NOT IN** as a named topic. |
| 5 | Working backwards, number machines, bar models | **ON** for undoing + - x /: P2 3.3 "relationship between multiplication and division". | "Gave half of them" (Stretch s3, Challenge c7): fraction of a set is **ABOVE (P4** Fractions 2.1); P2 only has "fraction as part of a whole" (Fractions 1.1). Challenge c6 "add 10 gives same as multiply by 3" (equation with the unknown on both sides): **ABOVE (P6** Algebra 1.5). Before-and-after bar models, number machines: **NOT IN** as named items; [UNVERIFIED] whether MOE materials name bar models at P2, the syllabus PDF does not. |
| 6 | Money (dollars and cents) | **ON.** P2 Money 1.1 to 1.4 (dollars and cents, decimal notation $1.25, comparing, converting 275c to $2.75). Change by counting on is fine. | "Spent half of his money" (Stretch s1, s6, Challenge c7): fraction of a set/amount, **ABOVE (P4** 2.1), though the lesson uses a bar cut in half. Challenge "10 coins of 10c/20c, all totals": **NOT IN**. |
| 7 | Fractions (halves to twelfths) | **ON.** P2 Fractions 1.1 to 1.3 and 2.1 (part of a whole, unit and like fractions, denominators up to 12, add/subtract like fractions within one whole). | Challenge c9 "Siti eats 1/2, then Ravi eats 1/2 of what is left": fraction of a fraction, **ABOVE (P5** multiplying fractions). Equivalent fractions (1/4 = 2/8): **ABOVE (P3** Fractions 1.1); the tutor notes already say this is a P3 topic and use bars only. |
| 8 | 2D and 3D shapes, counting squares/cubes | **ON** for half circle, quarter circle (P1 list, reused), and 3D shapes cube/cone/cylinder (P2 Geometry 2.1). | Nets, deciding which fold to a cube (objective, s3, s4): **ABOVE (P4** Nets 4.3). The tutor notes in l8.js admit "Nets are not in the P1 to P3 syllabus". Counting cubes in stacks, hidden cubes, painted cube: building solids with unit cubes is **ABOVE (P5** Volume 2.1). Counting all squares/triangles/rectangles in figures: **NOT IN**. Sphere (P2 outcome) never appears. |
| 9 | Length, mass, volume, time | **ON.** P2 Measurement 1.1 to 1.3 (m, cm, g, kg, litres), time 2.1 to 2.3. | "Find start time given duration" (s5 "lesson ended 4:15 pm, lasted 45 minutes", Challenge c3): **ABOVE (P3** Time 2.2). Balance-scale and jug puzzles: **NOT IN**. Time "to 5 minutes" stated in the scheme understates P2 Time 2.1 "to the minute". |
| 10 | Mixed: picture graphs with scales, logic | **ON** for picture graphs with scales (P2 Statistics 1.1) and money/fractions items. | Logic grid, "lost key" picture graph: **NOT IN**. Half-of-something items: see L5. |

Level 2 summary: the main topic of every lesson except Lesson 8 (nets, cubes) is ON-level; the ABOVE items are remainders (L3), common multiples (L3, L4), fraction of a set (L5, L6, L10), letters for unknowns (L2), nets/volume (L8), and start-time-from-duration (L9).

### Level 3 (Primary 3, ages 8-10)

| L | Topic | Main verdict and MOE outcome | Exceptions |
|---|---|---|---|
| 1 | Numbers to 10 000 | **ON.** P3 Whole Numbers 1.1 to 1.5. | Digit-sum and palindrome puzzles, "digits needed to number pages": **NOT IN**. |
| 2 | Addition and subtraction to 4 digits, missing digits | **ON.** P3 2.1 (algorithms up to 4 digits). | Core c3, c4 and many Stretch/Challenge items use A, B, C for digits or numbers. Number pyramid s3 uses "A, B, C" for unknown numbers: **ABOVE (P6** Algebra 1.1). Letter-cryptarithms (AA + BB = CBC): **NOT IN** (digit puzzles). Magic square: **NOT IN**. |
| 3 | Tables of 6, 7, 8, 9 | **ON.** P3 Multiplication/Division 3.1, 3.2, 3.5. | Challenge c3, c6, c9, Stretch s4 "divided exactly by both 6 and 9", "6 and 9 and between 40 and 60": common multiples **ABOVE (P4** 2.5). Stretch s2, s6, Challenge c5, c8 "8 x 8 x 8", "7 multiplied 8 times", "6 x 7 x 8 x 9": repeated products and last-digit cycles, **NOT IN**. Challenge c2 uses 6 x 20: beyond tables to 10 (syllabus does not state a limit). |
| 4 | Bar models for word problems | **ON** at the operations level (P3 +, -, x, / and money). Bar models themselves are **NOT IN** the syllabus text. | Stretch s5 (age problem "when mother is 3 times as old"), s9, Challenge c1, c2 ("pencil box and 3 pens / 5 pens"), c3, c5, c8: multi-step, two-unknown or unchanged-difference problems. These are heavier than the P3 outcomes imply; [UNVERIFIED] which year MOE schools expect these, the syllabus is silent. |
| 5 | Division with remainders | **ON.** P3 Multiplication/Division 3.3 "division with remainder". | Core items use divisors 4 to 7 and dividends below 100, fine for 3.3/3.4. Challenge c1, c2, c4, c6, Stretch s2, s7 "remainder 2 on 3, 4, 5, 6": common multiples plus remainders, **ABOVE (P4)**. Challenge c9 (4 pens left over / 4 pens short): two-condition problem, **NOT IN**. The vertical algorithm (3.4) is not taught (see section 4). |
| 6 | Fractions (fraction wall) | **ON.** P3 Fractions 1.1 to 1.4, 2.1. | Stretch s8 "1/2 + 1/4 + 1/8" (three terms, three denominators): **NOT IN** (P4 Fractions 3.1 allows "not more than two different denominators", p. 37; corrected from ABOVE (P4), see the verification block). Challenge c1 to c3, c9 (find a fraction between two fractions; "make the top numbers the same"): reasoning beyond outcomes, **NOT IN**. |
| 7 | Area and perimeter | **ON** for rectangles/squares: P3 Area 1.1 to 1.4. | Finding a side from area or perimeter (Stretch s2, s6, Challenge c2, c4, exit ticket "perimeter 12 cm, length 4 cm, area?"): **ABOVE (P4** Area and Perimeter 1.1, 1.2). Composite figures with cut-outs (Challenge c5, c9, Stretch s4): **ABOVE (P4** 1.3). "Biggest area for a given perimeter" investigation: **NOT IN**. |
| 8 | Angles, perpendicular and parallel lines | **ON.** P3 Angles 1.1, 1.2; Perpendicular/Parallel 2.1, 2.2. No protractor, degrees, or angle letters used (good). | Counting angles at a point (n lines give n(n-1)/2 angles), counting right angles in staircases: **NOT IN**. Six-sided shape puzzles: **NOT IN**. |
| 9 | Compound units, money, time (12 and 24 hour) | **ON.** P3 Measurement 1.2, 1.3; Time 2.2, 2.3; Money 1.1. | Challenge c8 (3 pens and 2 files, file 60c more): two-unknown, **NOT IN**. Jug puzzle (300 ml and 500 ml): **NOT IN**. Seconds (P3 Time 2.1) never appear. |
| 10 | Mixed: bar graphs, logic | **ON** for bar graphs with scales (P3 Statistics 1.1, 1.2; Core c4, Stretch s5, Challenge c9). | Logic grid, handshake problem (triangular numbers), "squares in a 3 by 3 grid", truth-teller puzzle: **NOT IN**. |

Level 3 summary: topics of all ten lessons are ON-level except L4 (bar-model method, which the syllabus does not name) and the logic/enrichment parts of L8, L10. ABOVE items cluster in common multiples (L3, L5), letter notation (L2), P4 area/perimeter (L7), and a three-denominator fraction sum (L6).

---

## 3. Vocabulary, notation and method mismatches

Searched all lesson text (qbank, key, objective, workbook items, tutor notes) by keyword. No use found of: percentage, ratio, negative numbers, protractor/degrees, angle letters, long-division layout, "numerator"/"denominator", "quotient", "simplest form", "sphere", "dot grid". The items below are the real mismatches. "Suggested rewording" is for student-facing text.

| # | Where | Issue | Suggested rewording |
|---|---|---|---|
| M1 | **Letters for unknowns.** L1 Stretch "A + A + 4 = 20, and the two As stand for the same number". L2 Core c1 "3A5 + 214 = 579. What is the digit A?", c2, c3 "...= 300 + A", c5 "A - 150 = 600", Stretch s2, s3, s6, Challenge c2 "A + 150 = 550 - A", c5, c7, c9 "AB7 + 4CD". L3 pyramid s3 "A, B, C". Also L3 Core c3, c4 "4A27 + 1365". | MOE introduces a letter for an unknown number in P6 (Algebra 1.1); before that the unknown is a blank or box. | Use a box: "3[ ]5 + 214 = 579. What digit goes in the box?". For several unknowns use different shapes: "[ ] + [ ] + 4 = 20, the two boxes hold the same number". For P2 c2 write "A + 150 = 550 - A" as "[ ] + 150 = 550 - [ ] (the same number in both boxes)" and mark it as a Challenge puzzle, not school algebra. Keep letter codes only for the cryptarithms (P3 L2 s6, s8, c3, c4, c9) and say once: "Each letter is a digit. Same letter, same digit. This is a code puzzle, not algebra." |
| M2 | **Ordinals past tenth.** P1 L4 Core "11th, 12th, 15th"; Stretch "14th, 20th, 23rd, 25th, 100th"; Challenge "33rd, 47th". Also P1 L1 Stretch "8th number", "9th number" (these are within tenth, so fine). | P1 syllabus: ordinal numbers first to tenth with symbols 1st, 2nd, 3rd (1.7). | For beyond tenth write "place 14" or "the shape in place 14": "What shape is in place 14?" (keep "10th" and below as is). |
| M3 | **"Multiples" / common multiples.** L1 Stretch "Frog A in 3s, Frog B in 4s... which numbers do both land on", L8 Core "counting in 2s AND 5s", L10 Challenge secret number; P2 L4 Stretch s5, Challenge c7, c9; P3 L3 Challenge c3, c6, c9; P3 L5 Challenge c1, c2, c4, c6. | Common multiples and factors are P4 (Factors and Multiples 2.1 to 2.5). The wording used ("numbers both say") is fine; the formal word "multiple" is not used by students, only in the tutor skills line ("prediction by multiples", hp L4). | Keep "numbers in both counting patterns" for P1 and P2. For P3 use "divides exactly by both 6 and 9" or "is in both the 6 times table and the 9 times table", and avoid the word "multiple" in student pages. |
| M4 | **Remainders below P3.** P1 L4 "sticks left over" (Stretch "25 sticks... how many left over", "50 sticks"). P2 L3 "share with leftovers" (objective, Stretch s3, s5, Challenge c6, c8, tutor note "division with a remainder"). | P3 3.3 "division with remainder". P2 ÷ is only within the tables. | Keep "left over" in P1/P2 (everyday word), reserve "remainder" for P3. In P2 pages add a one-line teacher note: "left over = preview of a P3 idea". No student-text change needed beyond not using "remainder". |
| M5 | **Fraction of a set/amount in Level 2.** L5 Stretch s3 "She gave half of them to Mei", Challenge c7; L6 Stretch s1 "spent half of his money", s6, Challenge c7; L10 Stretch s3 "half of the people got off", s6. | P2 syllabus is "fraction as part of a whole" (1.1). "Fraction of a set" (e.g. half of 12 beads) is P4 Fractions 2.1. | Reword so the whole is one bar: "Siti's beads are one bar. She cuts the bar into 2 equal parts and gives one part to Mei." Or label "halving" and avoid the word "fraction". |
| M6 | **"Bottom number / top number".** P2 L7 (about 16 uses), P3 L6 (about 18 uses), scheme text. | The syllabus outcomes use "denominator" (P2 Fractions 1.3) and "numerator and denominator" (P3 1.4). Children will meet these terms in school. | First use: "the bottom number (the denominator)" and "the top number (the numerator)"; then either may be used. Add a glossary line in the P3 L6 student page. |
| M7 | **Seconds before P3.** P2 L4 Challenge c1 "Light A flashes every 3 seconds. Light B every 5 seconds... next 30 seconds". | Seconds are P3 Time 2.1. | "Light A flashes every 3 minutes. Light B flashes every 5 minutes... in the next 30 minutes" (the P1/P2 unit minutes) or make it "every 3 counts". |
| M8 | **"a.m." / "p.m." with stops.** P2 L9 and P3 L9 pages: "5:40 p.m.", "12:30 a.m."; website parent page "a.m. and p.m.". | The PDF writes 'am' and 'pm' (P1 Time 2.2). | Write "am" and "pm". The time layout (5:40 vs 5.40) and the 24-hour layout (09:30, 21:00 vs 0930 h) are **[UNVERIFIED]** because the syllabus PDF does not show a format; check a P3 school textbook or MOE exemplar before changing. |
| M9 | **"semicircle" at P2.** P2 L8 objective and Core ("Name semicircles and quarter circles"; 28 uses). | The P1 syllabus word is "half circle" (Geometry 1.1); "semicircle" first appears at P6 (area and perimeter). | "Half circle (also called a semicircle)" on first use. |
| M10 | **"diagonal".** P1 L7 text (Explore "fold along a diagonal", Challenge, Think Harder "both diagonals drawn (lines joining opposite corners)"). P2 L8 already says "from corner to corner". | "Diagonal" is not taught in primary: P4 Rectangle and Square 2.1 says "excluding diagonal properties" (p. 39). | "Fold the square from corner to corner" and "both lines from corner to corner". |
| M11 | **Shape names not in P1 list.** P1 L7 Q2, Core, exit ticket (pentagon, hexagon, octagon, "7 sides"), Q5 key (parallelogram). | P1 list: rectangle, square, triangle, circle, half circle, quarter circle. Pentagon/hexagon/octagon are not named in any primary year of the PDF [OFFICIAL]. | Keep them as vocabulary the tutor introduces ("a 6-sided shape is called a hexagon") and add a note in the tutor guide: "Not named in the P1 syllabus; enrichment vocabulary." |
| M12 | **Bar model, number machine, magic square, array, pattern core, ten-frame, number bond, IN/OUT.** Throughout. | None of these terms appear in the 2021 syllabus PDF [OFFICIAL]. "Bar model" and "number bond" are common Singapore school terms, but I could not confirm either from an MOE document: **[UNVERIFIED]** that MOE materials use them at P1 to P3. | No change; do not describe them as "MOE terminology". Describe them as "tools we use for thinking". |
| M13 | **Money layout.** P2 and P3 mix "65c" and "$3.65" in the same page; P1 uses c and $ only. | P2 Money 1.2 to 1.4: decimal notation and conversion. P1 Money 1.1: cents up to $1, dollars up to $100, no decimal notation. The c symbol is not shown in the PDF [UNVERIFIED]. | P2/P3: encourage answers in decimal notation ($0.65, $3.65) as well as cents, and teach the conversion explicitly (already in P2 L6 Core c1). P1: keep c and whole dollars, no decimals (already so). |
| M14 | **Remainder layout "29 / 4 = 7 r 1".** P3 L5 key. | Syllabus says "division with remainder" without a layout. School layout (R vs r vs words) is **[UNVERIFIED]**. | Student-facing answers: "7 remainder 1", with "r" only in the key. |
| M15 | **Breadth.** P3 L7 Stretch s6 "Find its length and breadth". | "Breadth" vs "width" convention not stated in the PDF [UNVERIFIED]. Core items elsewhere use "wide". | Use "length and width" to match the Core wording. |
| M16 | **Picture-graph scale and half pictures in Level 1.** L3 Stretch, Challenge. | P2 Statistics 1.1. | Add "(a P2 idea)" in the tutor guide; student text can stay. |
| M17 | **Scheme PDFs out of step with lesson files.** P1 scheme PDF lists exit tickets and an objective for L6 ("pay in dollars with notes up to $100"; "Make 40c using three coins") that differ from hp/lessons.js ("Paying in dollars is an extra on the Think harder page"; exit ticket 30c). P1 L7 exit ticket differs too. | The scheme PDF is generated by levels/scheme.py from hp/lessons.js, so the committed PDF looks stale. | Re-run `python3 levels/scheme.py p1` (and p2, p3) before sharing the PDFs. |

---

## 4. MOE learning outcomes that no lesson touches (coverage gaps)

"Touch" means a Core or lesson-level item practises the outcome. Partial = appears only in Stretch/Challenge or incidentally.

**Primary 1**
- Whole Numbers 1.2 place value (tens, ones), 1.3 reading and writing numbers in words, 1.4 comparing sets, 1.5 comparing and ordering numbers (partial in L9 and graph items), 1.7 ordinal symbols (1st to 10th, partial in L5).
- Addition/Subtraction 2.4 adding more than two 1-digit numbers (partial), 2.5 to 2.6 within 100 and algorithms, 2.7 mental calculation beyond within 20.
- Multiplication/Division 3.1 to 3.4 (concepts, sign x, within 40, dividing within 20): only skip counting in L1.
- Money: counting mixed notes and coins to $100 is only partly met (L6 notes in Think Harder).
- Measurement: 1.4 drawing a line segment to the nearest cm; all of Time (2.1 to 2.4: telling time, am/pm, h/min, durations). The P1 scheme PDF already tells parents time, multiplication and division and 2-digit addition and subtraction within 100 are not taught.
- Geometry: half circle and quarter circle (1.1, 1.2), copying figures on dot or square grid (1.4).
- Statistics: covered (picture graphs).

**Primary 2**
- Whole Numbers 1.3 reading and writing numbers in words; 1.6 odd and even numbers (only incidental); 2.2 mental calculation; 3.5 mental calculation with tables; 3.2 use of the division sign is used but not taught as a topic.
- Fractions: covered. Money: covered.
- Measurement: 2.1 telling time to the minute (the lessons stay on 5-minute and mostly quarter times), 2.3 converting hours and minutes to minutes only (partial in L9 durations).
- Geometry 1.1 patterns with 2D shapes changing in size, shape, colour or orientation (L4 repeating patterns are about position counting, not attributes); 3D shapes sphere, classifying and naming all five (L8 is mostly cube and nets).
- Statistics: picture graphs with scales appear in L10 only (about three items); no lesson is dedicated to reading and interpreting.

**Primary 3**
- Whole Numbers 1.1 counting in hundreds/thousands (partial), 1.3 reading and writing in words; 2.2 mental calculation of two 2-digit numbers; 3.4 multiplication and division algorithms (3 digits by 1 digit) (L3 and L5 use facts and counting, not the vertical algorithm); 3.5 mental calculation.
- Fractions 1.2 expressing a fraction in its simplest form ("simplest" appears nowhere), 1.4 given-denominator/numerator equivalent fractions (partial); Money: covered.
- Measurement 1.1 km (one item), 2.1 seconds (none); 1.2 area in m2 (partial); Statistics: bar graphs appear in L10 only (about three items) and different scales on an axis is touched once.
- Geometry: covered (L8). Area/perimeter: covered.

**Does it matter for an enrichment programme?** For learning value, mostly no: the programme's stated aim is depth, reasoning and puzzles, not coverage, and the schemes say so (P1 scheme says explicitly it is not the whole P1 syllabus). It matters for communication: the labels "covers P1/P2/P3 topics" imply coverage the lessons do not provide. Two gaps are worth parent disclosure at P2 and P3 because they are heavily examined skills in school: the written algorithms (P3 3.4, plus P1/P2 algorithms) and mental calculation. Suggested one-line disclosure for each scheme: "This programme does not teach written algorithms, mental calculation drills, telling time to the minute, or most of the data-handling outcomes in the school syllabus." Time (P1 and P2), mental calculation and written algorithms are the biggest absences.

---

## 5. Labelling and wording: honesty check and suggested safe wording

### What the repo already does well
- website/dist/index.html footer: "Not affiliated with MOE or the Gifted Education Programme."
- taster/gen.py: "does not promise exam results and is not affiliated with the Ministry of Education or the Gifted Education Programme."
- levels/mkextras.py: "It is enrichment. It does not replace school maths or follow a school syllabus, and it is not linked to MOE or the Gifted Education Programme."
- p2/guide.js, p3/guide.js footers: "not affiliated with, run by or endorsed by the Ministry of Education or any school."
- The P1 scheme includes an honest "Coverage" note. The parent FAQ cites an MOE-hosted source for the 2021 P1 facts (cm, time to 5 minutes, am/pm), and these match the official PDF I read.
- gifted_research.md section 3 wording ("inspired by research-based approaches used in gifted education", "extends thinking beyond the school syllabus") is in use on the website.

### Wording that overclaims or contradicts itself
1. **"Ages 6-8 (covers P1 topics)", "Ages 7-9 (covers P2 topics)", "Ages 8-10 (covers P3 topics)"** (website/dist/index.html level list and the Level dropdown; docs/levels_and_placement.md example). The lessons do not cover the year's topics: section 4 lists large gaps (all of Time at P1, algorithms at P3). "Covers" is a coverage claim.
2. **"non-routine puzzles tagged to the school syllabus"** and the table column "Title and syllabus topic" (levels/scheme.py, all six scheme PDFs). This reads as alignment, and it contradicts mkextras.py ("does not ... follow a school syllabus"). It is also only partly true: this audit found ABOVE or NOT IN items in every level, most in Stretch/Challenge, and some whole lessons (P1 L8 Logic, P3 L10 logic part) are not syllabus topics.
3. P2/SPEC.md and P3 SPEC say "tagged to the P2 syllabus". Internal, but the phrase propagates.

### Suggested safe wording (supported by this audit)
Supported by section 2: most Core items sit in that year's MOE syllabus, several lesson topics (logic, patterns, bar-model method, nets) are not syllabus topics, and Stretch/Challenge items often go beyond it. These wordings make no claim of alignment or coverage.

- Level list: "Ages 8-10 (topics that build on Primary 3 maths)". Or "Ages 8-10 (for children around Primary 3)".
- Scheme PDF "Approach": "Enrichment, not extra drill: non-routine puzzles on topics chosen to complement the school syllabus. Many puzzles go beyond it, and the programme does not cover the whole school syllabus." Column header: "Title and topic" (not "syllabus topic").
- Parent paragraph: "Each lesson uses ideas children meet in school at this level, then asks them to explain, test and extend them. It does not replace school maths and is not linked to MOE or the Gifted Education Programme."
- Keep: "Extends thinking beyond the school syllabus" (not "ahead of the syllabus").
- Do not write: "MOE-aligned", "follows the MOE syllabus", "covers the P3 syllabus", "GEP preparation", "GEP-style", "prepares for P3 GEP selection".
- Add to P2 and P3 schemes the same kind of Coverage note P1 has (see section 4).

---

## 6. What I could not verify

1. A syllabus version newer than "Updated Oct 2025". The MOE listing page I fetched on 22 Oct 2026 shows October 2025 as current; the "Dec 2024" MOE file URL returned 404, and no Dec 2023 or Dec 2024 copy was read.
2. Whether MOE materials outside the syllabus PDF (textbooks, school guides, the old "learning experiences") use the terms "bar model", "number bond", "model drawing", or specific heuristics at P1 to P3. The syllabus PDF does not name them. [UNVERIFIED]
3. School conventions that the PDF leaves open: time format (5:40 vs 5.40; 24-hour 0930 h vs 09:30), the remainder layout ("r 1"/"R 1"), the cents symbol, "length and breadth" vs "width", and whether schools say "semicircle" before P6. [UNVERIFIED]
4. The year MOE schools typically expect for multi-step comparison/unchanged-difference bar-model problems (P3 L4 Stretch/Challenge). The syllabus gives no year. [UNVERIFIED]
5. Whether MOE considers non-standard units (cubes, clips) part of P1 length. The 2021 PDF lists only cm for P1 Length; I did not check the earlier 2013 syllabus.
6. The website claim that MOE is "discontinuing the Gifted Education Programme in its current form and starting a refreshed approach from 2027" (press release 3 March 2026). I did not check this; it is out of scope but should be re-verified before publication, per gifted_research.md section 4, item 5.
7. I did not read every workbook illustration, slide, or tutor script line; item-level findings come from the qbank, key, objectives, and tutor notes in the content files, plus keyword searches. Pages the children see (rendered PDFs) were not inspected for stacked vs slash fractions or other typesetting.
8. I did not tally the number of ABOVE/NOT IN items per level; the lists above are my reading of the content files, and may miss some items.
