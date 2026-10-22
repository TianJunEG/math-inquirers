# International syllabus mapping: East Asia (Hong Kong, Mainland China, Japan, South Korea)

Math Inquirers Levels 1-6 (60 lessons) mapped against the primary mathematics curricula of Hong Kong, Mainland China, Japan and South Korea.
Prepared 2026-10-22. Read-only audit: no lesson content was edited. This file is internal research, not marketing copy.

## 0. How to read this document

**Source labels.** Every jurisdiction below states which document was actually opened. `[SECONDARY]` means a publisher, university or summary source rather than the ministry text. `[UNVERIFIED]` means I could not confirm it from a document I opened; nothing marked that way should be repeated outside this file. I did not rely on memory for any curriculum fact in the matrix. Where a fact in the vocabulary section comes from general knowledge of textbooks rather than a curriculum document I opened, it is marked.

**What was mapped.** The program's lesson topics and objectives: Level 1 from `hp/lessons.js`; Levels 2-6 from the `objective`, `title` and `topic` fields in `pN/content/l1..l10.js`. I did not re-audit worksheets or the question bank; a lesson's mapping is by its stated topic and objective, and a lesson with several strands is mapped by its main topic, with the secondary strands noted in the cell.

**Program ages.** Level 1 ages 6-8, Level 2 7-9, Level 3 8-10, Level 4 9-11, Level 5 10-12, Level 6 11-13 (`docs/levels_and_placement.md`). Each level is a three-year band that is named after the Singapore primary year with the same number (P1 = about age 6-7, P6 = about age 11-12).

**Comparison rule used in the matrix.** All four systems start formal schooling at roughly age 6 (typical entry age is general knowledge, not stated in the curriculum documents I opened [UNVERIFIED]), so I compare by year number: Level N is compared with the jurisdiction's grade N.

| Code | Meaning |
|---|---|
| SAME | the jurisdiction introduces the topic in grade N (or in the two-year band containing grade N) |
| EARLIER | introduced in a grade below N: the lesson is taught to an older child than the jurisdiction's first teaching |
| LATER | introduced in a grade above N (or in lower secondary): the lesson is enrichment ahead of that curriculum |
| NOT | no matching topic in that jurisdiction's primary documents I read |
| n/a | the lesson is a mixed review (Challenge Day or Showcase) and has no single topic |

Caveats on the codes:
1. **China and Korea set content by two-year band, not by single year.** The 2022 Chinese standard has three primary stages (grades 1-2, 3-4, 5-6) and the Korean 2022 curriculum has three grade bands (1-2, 3-4, 5-6). The year inside a band is chosen by textbooks, which I did not review. A cell reading "SAME G3-4" for a Level 3 or Level 4 lesson therefore means "within the band", and the true year could be one year either side. Hong Kong and Japan name single grades.
2. **The level is three years wide.** A one-grade difference (for example LATER P4 for a Level 3 lesson) still falls inside the level's age band. The code shows the offset against the Singapore-style year the level is named after, and families should read it as a hint, not a verdict.
3. **"Introduced" means the standard first lists the topic.** Mastery and depth are not compared, and this program teaches each topic as inquiry puzzles rather than as a procedure.
4. **Hong Kong uses "P1-P6", the others "G1-G6"** (G = their grade). JHS = Japanese lower secondary.

## 1. Summary matrix: 60 lessons by 4 jurisdictions

Tallies (primary code of each cell; the 5 mixed lessons per jurisdiction are excluded from the four codes):

| Jurisdiction | SAME | EARLIER | LATER | NOT | mixed (n/a) |
|---|---|---|---|---|---|
| Hong Kong | 30 | 6 | 11 | 8 | 5 |
| Mainland China | 42 | 5 | 6 | 2 | 5 |
| Japan | 35 | 5 | 10 | 5 | 5 |
| South Korea | 34 | 5 | 12 | 4 | 5 |

Reading the tallies: for all four systems the clear majority of the program's single-topic lessons are introduced in the same year or earlier in the jurisdiction's own curriculum. The "LATER" cells cluster in a few places: fractions at Level 2, area and perimeter at Level 3 (strongest in Korea), protractor and degree at Level 4 (Hong Kong teaches it in P6), symmetry and nets, line graphs, percentages and speed in Hong Kong (P6), and almost all of the Level 6 enrichment topics (negative numbers, counting, probability, algebra in Korea). Level 6 "NOT" cells are real gaps in the curricula, not in the program: clock arithmetic and nth-term sequences are in none of the four.

| # | Lesson (topic) | Hong Kong | Mainland China | Japan | South Korea |
|---|---|---|---|---|---|
| 1.1 | Count with the Frog: skip counting, rules | SAME P1 (skip-count 2/5/10; rule-finding not a unit) | SAME G1-2 (patterns) | SAME G1-2 (number sequence G1; groups G2; rules not named) | SAME G1-2 (patterns) |
| 1.2 | Number Bond Inquiry | SAME P1 (add/sub to 20) | SAME G1-2 (add/sub within 20) | SAME G1 (numbers as sum/difference; ten as a unit) | SAME G1-2 (compose/decompose) |
| 1.3 | Fruit Party: picture graphs | LATER P2 (pictograms) | SAME G1-2 (classification only; pictogram not named) | SAME G1 (pictures for quantities; tables/graphs G2) | SAME G1-2 (graphs with symbols) |
| 1.4 | Pattern Inquiry: repeating, growing | NOT (no pattern unit; algebra P5) | SAME G1-2 (pattern rules) | NOT as a topic (functions G4) | SAME G1-2 (repeat/increase rules) |
| 1.5 | Mystery Number: working backwards | LATER P5 (equations) | SAME G1-2 (inverse operations only) | LATER G3 (box-expressions; inverse relation G2) | SAME G1-2 (box in +/- sentences) |
| 1.6 | Coin Combos: money | SAME P1 (Money I) | SAME G1-2 (RMB, thematic activity) | NOT listed | NOT listed |
| 1.7 | Shape Safari: 2D shapes | SAME P1 | SAME G1-2 | SAME G1 (formal triangles/quadrilaterals G2) | SAME G1-2 |
| 1.8 | Logic Lab: sorting, Venn, logic | SAME P1 (enrichment topics only) | SAME G1-2 (classification; logic grids not named) | LATER G2 (classify into tables); Venn/grids not named | SAME G1-2 (classification) |
| 1.9 | Measure It!: length | SAME P1 | SAME G1-2 | LATER G2 (standard units cm/m; comparison G1) | SAME G1-2 |
| 1.10 | Challenge Day (mixed) | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped |
| 2.1 | Digit Detectives: numbers to 1000 | SAME P2 | SAME G1-2 (to 10 000) | SAME G2 (3-digit simple G1; 4-digit G2) | SAME G1-2 (to 4 digits) |
| 2.2 | Missing Digits: 3-digit add/sub | SAME P2 (with borrowing) | SAME G1-2 | SAME G2-3 (simple 3-digit G2) | LATER G3-4 (3-digit add/sub) |
| 2.3 | Legs, Wheels, Arrays: multiplication, division | SAME P2 | SAME G1-2 (table facts) | SAME G2 (x); division G3 | SAME G1-2 (x tables); division G3-4 |
| 2.4 | Pattern Machines: patterns with multiplication | SAME P2 (tables); growth rules not a unit | SAME G1-4 (pattern rules) | SAME G2 (table patterns); growth tables G4 | SAME G1-4 (patterns) |
| 2.5 | Mystery Number Machines: two-step backwards, bar models | LATER P5 (equations) | LATER G5-6 (equality property) | LATER G3 (box-expressions) | SAME G1-2 (box, +/- only) |
| 2.6 | Market Day: money | SAME P2 (Money II) | SAME G1-2 (RMB) | NOT listed | NOT listed |
| 2.7 | Fair Shares: fractions | LATER P3 (Fractions I) | LATER G3-4 | SAME G2 (1/2, 1/4); unit fractions, add/sub G3 | LATER G3-4 |
| 2.8 | Shape Builders: 2D/3D, cubes, nets | SAME P2 (3-D II); nets P5 | SAME G1-2 (solids, building); nets G5-6 | SAME G2 (boxes); nets G4 | SAME G1-2 (cube stacks); nets G5-6 |
| 2.9 | Measure Masters: m, cm, g, kg, litre, time | LATER P3 (g/kg, L); time, length P1-2 | SAME G1-2 (length, time); g/kg G3-4; L/mL G5-6 | SAME G2 (length, L/dL/mL, time); g/kg G3 | SAME G1-2 (length, time); L, g, kg G3-4 |
| 2.10 | Challenge Day (mixed) | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped |
| 3.1 | Number Sleuths: numbers to 10 000 | EARLIER P2 | EARLIER G1-2 | EARLIER G2 | EARLIER G1-2 |
| 3.2 | Cryptarithms: 4-digit add/sub | SAME P3 | SAME G3-4 | SAME G3 | SAME G3-4 |
| 3.3 | Times Table Treasure: 6-9 tables | EARLIER P2 (tables 0-10) | EARLIER G1-2 | EARLIER G2 (to 9x9) | EARLIER G1-2 |
| 3.4 | Model Makers: bar-model word problems | SAME P3-4 (4-operation problems; bar model not named) | SAME G3-4 (addition/multiplication models; bar model not named) | SAME G3-4 (diagrams generic; tape diagram not named) | SAME G3-4 (bar model not named) |
| 3.5 | Remainder Riddles: division with remainders | SAME P3 (concept P2) | SAME G3-4 (remainder not named in text read) | SAME G3 | SAME G3-4 |
| 3.6 | Fraction Walls: equivalent, compare, add/sub | SAME P3 (equivalent P3; reduce/expand P4) | SAME G3-4 (like denominators); equivalent G5-6 | SAME G3-4 (unit fractions G3; equal fractions G4) | SAME G3-4 (like denominators); equivalent G5-6 |
| 3.7 | Area Architects: area and perimeter | LATER P4 | SAME G3-4 | LATER G4 (area); perimeter not itemised | LATER G5-6 |
| 3.8 | Angle and Line Detectives: angles, perpendicular, parallel | SAME P2-3 (angles, perpendicular P2; parallel P3) | SAME G3-4 | SAME G3-4 (angles G3; parallel/perpendicular G4) | SAME G3-4 |
| 3.9 | Measure and Money: compound units, budgets, 24-hour time | SAME P3 (24-hour time P3) | SAME G3-4 (24-hour time, mass units; RMB earlier) | SAME G3 (km, g/kg, seconds); money/24-hour not listed | SAME G3-4 (units, durations); money not listed |
| 3.10 | Challenge Day: bar graphs, logic | SAME P3 (bar charts; scales P4) | SAME G3-4 (bar charts); logic grids not named | SAME G3 (bar graphs); logic grids not named | SAME G3-4 (bar graphs); logic grids not named |
| 4.1 | Factor Hunters: factors, multiples | SAME P4 | LATER G5-6 | LATER G5 | LATER G5-6 |
| 4.2 | Big Number Puzzles: 5-digit, rounding, estimation | EARLIER P3 (5-digit); rounding P5 | SAME G3-4 (large numbers, estimation); rounding not named | SAME G4 (rounding; oku and cho units) | LATER G5-6 (rounding); numbers >10 000 G3-4 |
| 4.3 | Operation Detectives: order of operations | EARLIER P3 (brackets, mixed operations) | SAME G3-4 (mixed, up to 3 steps) | SAME G4 | LATER G5-6 |
| 4.4 | Fraction Frontier: improper/mixed, fraction of a set | SAME P4 | LATER G5-6 (common denominators) | SAME G4 (terms); unlike denominators G5 | SAME G3-4 (improper/mixed); unlike denominators G5-6 |
| 4.5 | Decimal Detectives: decimals to 3 places | SAME P4 (to 4 d.p.) | SAME G3-4 (initial decimals) | SAME G4 (tenths G3) | SAME G3-4 (to 3 places) |
| 4.6 | Angle Turns: protractor, clock, compass | LATER P6 (degree unit) | SAME G3-4 (protractor) | SAME G4 | SAME G3-4 |
| 4.7 | Area Architects II: composite area, perimeter | SAME P4 (composites P5) | SAME G3-4 (rectangle/square) | SAME G4 (composites in activities) | LATER G5-6 |
| 4.8 | Symmetry and Nets | LATER P5-6 (nets P5, symmetry P6) | LATER G5-6 (nets, axes); intuitive G3-4 | LATER G6 (symmetry); nets G4 | LATER G5-6 (nets, symmetry); reflection G3-4 |
| 4.9 | Data Detectives: tables, line graphs | LATER P6 (broken-line graphs) | LATER G5-6 (line charts) | SAME G4 | SAME G3-4 |
| 4.10 | Challenge Day (mixed heuristics) | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped |
| 5.1 | Million Puzzles: numbers to 10 million | SAME P5 | EARLIER G3-4 (wan, yi units) | EARLIER G4 (oku, cho) | EARLIER G3-4 |
| 5.2 | Fraction Feats: fractions and division, 4 operations | SAME P5 | SAME G5-6 | SAME G5 (division as fraction); x and / by fractions G6 | SAME G5-6 |
| 5.3 | Before and After: fraction word problems | SAME P5 | SAME G5-6 | SAME G5-6 (add/sub G5; x, / G6) | SAME G5-6 |
| 5.4 | Triangle Areas | SAME P5 | SAME G5-6 | SAME G5 | SAME G5-6 |
| 5.5 | Volume Vault: cuboid volume | SAME P5 | SAME G5-6 | SAME G5 | SAME G5-6 |
| 5.6 | Rate Racers: unit rate, speed | LATER P6 (speed) | EARLIER G3-4 (price/speed relations); ratio G5-6 | SAME G5 (per-unit quantity, speed) | SAME G5-6 (ratio/rate; speed not listed) |
| 5.7 | Percentage Puzzles: discount, GST | LATER P6 | SAME G5-6 | SAME G5 | SAME G5-6 |
| 5.8 | Angle Chasers: triangle/quadrilateral angles | NOT (angle-sum facts not in primary list) | SAME G5-6 (triangle 180 degrees) | SAME G5 | EARLIER G3-4 |
| 5.9 | Pattern Generalisers: rules in words, 3n+1 | SAME P5 (letters for numbers) | SAME G5-6 (letters) | EARLIER G4 (varying quantities); letters G6 | SAME G5-6 (correspondence tables) |
| 5.10 | Challenge Day (mixed strategies) | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped |
| 6.1 | Code the Pattern: sequences, nth term | NOT (nth term); letters P5 | NOT (nth term); letters G5-6 | NOT (nth term); letters G6 | NOT (nth term); correspondence G5-6 |
| 6.2 | Prime Hunters: primes, factor trees | EARLIER P4 (primes); factor trees secondary | SAME G5-6 (primes; factor trees not named) | LATER JHS1 (primes since 2017); factors G5 | LATER middle school (factors G5-6) |
| 6.3 | Below Zero: negative numbers | NOT (secondary) | SAME G5-6 (introduced only, thematic) | LATER JHS1 | LATER middle school |
| 6.4 | Algebra Machines: expressions, equations | EARLIER P5 (algebra, equations) | SAME G5-6 (letters, equality property); equations secondary | SAME G6 (letters); equations JHS1 | LATER middle school (box/triangle only in primary) |
| 6.5 | Every Possible Way: counting | NOT | SAME G5-6 (listing outcomes only) | SAME G6 (possible cases) | LATER middle school |
| 6.6 | Fair or Unfair?: probability | NOT | SAME G5-6 (qualitative) | LATER (lower secondary; not in primary) | SAME G5-6 (numeric possibility, simple events) |
| 6.7 | Turtle Geometry: polygon angles, coding | NOT (polygon angle sums secondary) | SAME G5-6 (triangle sum only) | EARLIER G5 (regular polygons, programming example) | EARLIER G3-4 (angle sums, regular polygons) |
| 6.8 | Secret Codes: clock arithmetic, ciphers | NOT | NOT | NOT | NOT |
| 6.9 | Data Detectives: mean, median, mode | SAME P6 (average only) | EARLIER G3-4 (mean); median/mode not primary | SAME G6 (mean, median, mode; mean of measures G5) | SAME G5-6 (mean); median/mode middle school |
| 6.10 | Showcase Challenge (mixed + code) | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped | mixed review, not mapped |

Footnotes to the matrix:
- Lesson 6.8 (clock arithmetic and Caesar ciphers) is NOT in any of the four primary documents. Calendar and time-unit conversion is mapped separately (lessons 2.9 and 3.9), but modular arithmetic and ciphers are not.
- Lessons 1.8, 3.10: logic grids and Venn diagrams are not named as topics in any of the four documents. Hong Kong has sorting and Sudoku only as optional Enrichment Topics (P1, units 1E1 and 1E2). The classification (SAME) cells refer to the sorting half of the lesson only.
- Lesson 3.4: no document names the bar model. Hong Kong, Japan and Korea state four-operation word problems and generic diagrams; China's teaching hints mention an "addition model" and "multiplication model" (a different idea). Conventions are in each section.
- Lesson 6.7: Japan's 2017 commentary says the Grade 5 regular-polygon construction topic is the example where programming may be used. That is the only place any of the four documents ties programming to a topic I mapped. I could not confirm anything about Chinese, Korean or Hong Kong programming in primary maths [UNVERIFIED].
- Codes were assigned by me from the extracted topic lists below. Reasonable people could code a few boundary cells differently (for example 3.5 in China, where the remainder idea is not named in the text I read).


## 2. Hong Kong

### 2.1 Sources

| Item | Detail |
|---|---|
| Document opened | **Supplement to Mathematics Education Key Learning Area Curriculum Guide: Learning Content of Primary Mathematics.** Prepared by the Curriculum Development Council, recommended for use in schools by the Education Bureau (EDB), HKSARG, **2017**. Read in full (learning targets, learning content tables P1-P6, flow chart). |
| URL | https://www.edb.gov.hk/attachment/en/curriculum-development/kla/ma/curr/pmc2017_e.pdf |
| Parent document (named in the supplement's preamble, not itself opened) | Mathematics Education Key Learning Area Curriculum Guide (Primary 1 - Secondary 6) (2017). Related EDB page seen in search results: https://www.edb.gov.hk/attachment/en/curriculum-development/kla/ma/curr/Ch2.pdf [not opened]. |
| Status | Official EDB text, English. Whether a later amendment replaced the 2017 supplement is [UNVERIFIED]. A 2024/2025 EDB textbook-writing guideline seen in search results describes the same five strands. |
| Typical ages | P1 about 6-7 through P6 about 11-12 [UNVERIFIED: not stated in the supplement]. |

### 2.2 Structure and notable features (all from the supplement)

- **Five strands in primary:** Number, Algebra (P5-P6 only), Measures, Shape and Space, Data Handling. Primary lesson time is 285-356 hours per key stage (12-15% of curriculum time).
- **Further Learning Unit: Inquiry and investigation (10 hours every year P1-P6).** The supplement describes it as time for "learning activities from different learning units, for example, activities on enrichment topics, cross-learning unit activities" to "inquire, communicate, reason and conceptualise". This is the closest match to the program's inquiry slogan in any of the four systems.
- **Enrichment Topics, optional, every year:** Sudoku (P1), sorting methods (P1), time-recording devices and block charts (P2), curve stitching and the map-colouring problem (P3), Eulerian paths (Seven Bridges of Konigsberg) and sorting diagrams (P4), Chinese and Roman numerals and exploring 3-D shapes (P5), rotational symmetry and non-metric units (P6).
- **Remarks, not just objectives,** are given per unit with a suggested time in hours, and several remarks say what is not required (for example "Students are not required to use the term inclusion relation"; "Students are not required to measure the angles at the centre of a pie chart").
- Calculators are mentioned only for converting non-metric units (P6 enrichment 6E2). I found no abacus in the document.

### 2.3 Grade by grade (unit names and codes from the flow chart and tables)

| Grade | Number and Algebra | Measures | Shape and Space | Data Handling |
|---|---|---|---|---|
| P1 | numbers to 20 and to 100; basic add/sub; add/sub (I) to two digits | length (I)(II); money (I); time (I) | 3-D shapes (I); 2-D shapes; directions and positions (I) | none in the flow chart (sorting is an enrichment topic) |
| P2 | 3-digit and 4-digit numbers; add/sub (II)(III) up to 3 digits, "subtraction with borrowing is required"; basic multiplication with the multiplication table 0-10; basic division (remainder required) | length (III); money (II); time (II) | 3-D shapes (II); angles (right, acute, obtuse), perpendicular lines; directions (II); quadrilaterals (I) | pictograms |
| P3 | 5-digit numbers; multiplication (I) (2-digit x 1-digit); division (I) with remainders; four operations (I) with brackets; fractions (I) (equivalent fractions, like-denominator add/sub within 1) | km and mm; time (III)(IV) incl. 24-hour; capacity; weight (g, kg) | quadrilaterals (II) incl. parallel lines; triangles | bar charts (I) |
| P4 | multiplication (II); division (II); multiples and factors (prime and composite numbers up to 100, sieve of Eratosthenes); common multiples and factors; four operations (II); fractions (II) (proper, improper, mixed; expand and reduce); decimals (I)(II) (to 4 places) | perimeter (I); area (I) (squares, rectangles) | quadrilaterals (III) (rhombus, inclusion of types); dissecting shapes; directions (III) (8 compass points) | bar charts (II) |
| P5 | multi-digit numbers (rounding to millions); fractions (III)(IV)(V) (x and ÷ by whole numbers, fraction as quotient or ratio); decimals (III); **Algebra:** letters for numbers, simple equations (I) using a balance | area (II) (parallelogram, triangle, trapezium, polygons); volume (I) | circles; 3-D shapes (III) (cross sections, nets of cubes, cuboids, cylinders) | compound bar charts |
| P6 | decimals (IV)(V); percentages (I)(II); **Algebra:** simple equations (II) | angle (degree); volume (II); perimeter (II) (circle, pi); speed; area (III) (circle) | symmetry (axial) | averages; broken-line graphs; pie charts; uses and abuses of statistics |

Not in the Hong Kong primary supplement (searched for, absent): negative numbers ("whole numbers" is defined as non-negative integers), probability, counting methods, sequences or patterns as a unit, triangle angle-sum, ratio notation (the ":" symbol is explicitly not required at P5).

### 2.4 Coverage: major Hong Kong topics with no or little program lesson

- Written multi-digit multiplication and long division (P3-P4) and mixed operations beyond order-of-operations puzzles: the program teaches multiplication through arrays and puzzles (2.3, 3.3), not as a procedure.
- Decimal operations (P4-P6), and money with decimals.
- Circles (P5 circle properties, P6 pi, circumference, circle area).
- Pie charts (P6), compound bar charts (P5).
- Directions and positions (P1-P4) beyond lesson 4.6's compass work; telling time to the minute at P1-P2 (lesson 2.9 covers it as a sub-skill).
- Properties of quadrilaterals and their inclusion relations (P2-P4); triangle classification.
- Ratio and direct proportion language (P5).

### 2.5 What a family moving between systems would notice

- **Hong Kong's own "Inquiry and investigation" time** means the program's style is familiar to Hong Kong teachers; the contents themselves are separate.
- **"Borrowing" is the official term** ("Subtraction with borrowing is required", P2), where Singapore teachers tend to say "regrouping".
- **Multiplication table range is 0-10 at P2**, earlier than Singapore's staged tables (lesson 3.3 teaches 6-9 to Level 3, one year after Hong Kong).
- **Weight versus mass:** the supplement tells teachers "not to mention the term mass" at P3 for g and kg because of everyday usage.
- **Algebra and equations arrive at P5**, a year before Singapore's usual placement of formal algebra, and Hong Kong has no primary probability or negative numbers at all, so Level 6 lessons 6.3, 6.5 and 6.6 are brand-new content there.
- **Decimals and area of rectangles at P4, but protractor and degree only at P6** (the surprise for families coming from Japan, China or Korea, where angles are measured at G3-4).
- Bar models and diagram conventions are not specified in the supplement; textbook conventions are [UNVERIFIED].

### 2.6 Which levels fit a Hong Kong child best (cautious)

- Number-and-operation lessons follow Hong Kong's year numbers closely, so **Level N fits Primary N** for Levels 1-3 and for most number lessons in Level 4-5.
- Level 3 area and perimeter (3.7) and Level 4 fractions (4.4) and decimals (4.5) match P4, so a **P3 child may find Level 3 stretches in geometry (area, perimeter) but easy in numbers (numbers to 10 000 and the 6-9 tables are P2 content)**.
- Level 4 angles with a protractor (4.6), symmetry (4.8) and line graphs (4.9) are P5-P6 content in Hong Kong, so a **P4 child will find these new; a P6 child will find them familiar**.
- Level 6 gives Hong Kong P6-P7 children topics Hong Kong primary does not teach (negatives, counting, probability, modular arithmetic).
- Treat this as a guide only; placement should still come from the program's diagnostic.


## 3. Mainland China (national standard; Shanghai and Beijing)

### 3.1 Sources

| Item | Detail |
|---|---|
| Document opened | **义务教育数学课程标准（2022年版）** (Compulsory Education Mathematics Curriculum Standards, 2022 edition), Ministry of Education of the PRC, issued 21 April 2022; the PDF is marked "以此为准" (authoritative), 9 May 2022. 189 pages, a scanned-image PDF. I read the pages on course nature, core competencies, stage objectives, and all primary content (number, geometry, statistics and probability, integrated practice) by viewing page images. Chinese only. |
| URL (notice page) | https://www.moe.gov.cn/srcsite/A26/s8001/202204/t20220420_619921.html |
| URL (PDF) | http://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220510531636118932.pdf |
| English | No official English translation of the mathematics standard was found. A British Council-hosted English translation seen in search results is of the English-language standard, not mathematics. English-language research papers on the 2022 standard exist [SECONDARY], for example a Beijing Normal University comparison with the OECD Learning Framework 2030 (https://guok.bnu.edu.cn/lwzz/a2eaabdaca654c7ea3def379f90ad5be.htm), which I did not rely on. |
| Shanghai and Beijing | Local textbooks and local requirements (Shanghai and Beijing both use locally approved textbook series) were **not** reviewed. Everything below is the national standard. The standard itself notes that a "five-four" system (primary school of 5 years) exists alongside the "six-three" system, with the second stage then covering grades 3-5 [verified in the standard text]. |
| Typical ages | Grade 1 about 6-7 through Grade 6 about 11-12 [UNVERIFIED: not stated in the standard]. |

### 3.2 Structure and notable features (verified in the standard unless marked)

- **Four content domains:** Number and Algebra (two themes in primary: "Number and Operations", "Quantity Relations"), Figures and Geometry ("Recognition and Measurement of Figures", "Position and Movement of Figures"), Statistics and Probability ("Data Classification", "Collection, Organisation and Presentation of Data", "Possibility of Random Phenomena"), and Integration and Practice (thematic activities, with project learning allowed in stage 3).
- **Stages of two years:** stage 1 grades 1-2, stage 2 grades 3-4, stage 3 grades 5-6, stage 4 grades 7-9.
- **"Four basics" (四基):** the standard's course-nature section states that mathematics learning builds "basic knowledge and basic skills, basic ideas and basic activity experience".
- **"Three abilities" (三会):** observing the real world with a mathematical eye, thinking with a mathematical mind, expressing with mathematical language.
- **Core competencies named in primary:** number sense, quantity sense, symbol awareness, operational ability, geometric intuition, spatial awareness, reasoning awareness, data awareness, model awareness, application awareness and innovation awareness.
- **Integration and Practice** replaces ad-hoc enrichment with named thematic activities. Stage 1: "Math game sharing", "Happy Shopping Street" (RMB), "Where is time" (hours, minutes, seconds), "My classroom" (position and direction), "Body rulers", "Math comic strip". Stage 2: "Secrets of year, month and day" (24-hour clock), "Cao Chong weighs the elephant" (g, kg, tonne, equal quantities), "Find the treasure" (8 directions), "Stories of measures and weights". Stage 3: "How to express quantities with opposite meaning" (negative numbers), "Campus plan", "Mathematics in sport", project learning ("Nutritious lunch", "Water is the source of life").
- **Calculators:** stage 2 explicitly allows calculators for calculation and exploring patterns. **Abacus:** stage 1 content (1) says pupils "know that an abacus can show multi-digit numbers".
- The standard states its own teaching hints per domain, including that fractions, decimals and whole numbers should be taught as one consistent system around "counting units" (计数单位), and that "unknown to known" transformation is the thinking behind multi-digit multiplication and division.

### 3.3 Stage by stage (content requirements from the standard)

| Stage (grades) | Number and quantity relations | Figures and geometry | Statistics and probability | Integration and practice |
|---|---|---|---|---|
| 1 (G1-2) | numbers within 10 000 and place value (abacus); symbols <, =, >; meaning of the four operations and the link between them; add/sub; multiplication and division facts (tables, 表内乘除法); fluent mental add/sub within 20; add/sub of two- and three-digit numbers; patterns in simple situations | recognise solids (cuboid, cube, cylinder, sphere) and plane shapes; classify shapes; compose shapes; cm and m; estimating and measuring length; sense of translation, rotation, axial symmetry | data classification | RMB, time to the second, directions, body measures |
| 2 (G3-4) | numbers above 10 000 (wan, yi); multi-digit multiplication and division; first fractions and decimals (like-denominator fraction add/sub, one-decimal-place add/sub); four mixed operations (mainly two steps, at most three, with small and medium brackets); commutative, associative, distributive laws, written with letters; total = parts, total price = unit price x quantity, distance = speed x time; estimation; equal quantities | line segment, ray, line, parallel and perpendicular; angle, protractor, 30/45/60/90 degree set squares; km, dm, mm, cm2, dm2, m2; classify triangles and quadrilaterals (isosceles, equilateral; trapezoid, parallelogram); perimeter and area of rectangles and squares; translation, rotation, axial symmetry | collecting and organising data; bar charts; **mean (average)**; reading media charts | year, month, day, 24-hour clock; g, kg, tonne; eight directions |
| 3 (G5-6) | multiples of 2, 3, 5; common multiples and LCM; common factors and GCD; odd, even, prime and composite; decimals and fractions in four operations and mixed operations (up to three steps); division and fractions; equality properties; letters for general relationships; ratio and proportion; proportional quantities y/x = k; **negative numbers (introductory, in thematic activity only)** | triangle inequality; **triangle angle sum 180 degrees**; circle, sector, circumference and pi, circle area; km2 and hectare; area of parallelogram, triangle, trapezoid; volume and capacity units; cuboid, cube, cylinder, cone and nets; views from front, side, top; position by direction and distance, ordered pairs (natural numbers) on grid paper; scale; translation, rotation, axial symmetry on grid paper | line and pie charts; **percentages (statistical meaning, discount, tax, interest)**; qualitative possibility of random events and listing all possible outcomes | negative numbers, campus plan, projects |

Not in the primary standard (searched for, absent): numeric probability, counting rules (only "list all possible results"), sequences or nth-term rules, solving equations (the standard's Number and Algebra table puts "equations and inequalities" in stage 4), median and mode, clock arithmetic.

### 3.4 Coverage: major Chinese topics with no or little program lesson

- Written multi-digit multiplication and division (stage 2) and decimal and fraction operations beyond the program's fraction lessons.
- Circles (circumference, pi, area), sectors, cylinders and cones, nets, views, surface area.
- Proportion (direct proportion and the y = kx form), ratio and "proportional distribution", scale.
- Position and movement: ordered pairs and grid positions, translation and rotation on a grid, scale drawing (stage 3); the program has no coordinate lesson.
- Pie charts and line charts as a reading skill (lesson 4.9 covers line graphs).
- Money (RMB) and the thematic activities as such; lesson 2.6 covers the arithmetic of coins.
- Classification of triangles and quadrilaterals (stage 2).

### 3.5 What a family moving between systems would notice

- **A more arithmetic-heavy start:** by the end of grade 2 the standard expects tables, fluent add/sub within 20 and numbers up to 10 000, so lesson 3.1 (numbers to 10 000) and 3.3 (6-9 tables) are review for a Chinese child of that age.
- **Four basics and the "unknown to known" idea:** the standard names basic ideas and activity experience as goals, not just skills. In the program the "Notice it, test it, explain why" routine lines up reasonably with "basic activity experience", but that is a loose match.
- **Four-digit grouping of big numbers** (wan = 10^4, yi = 10^8) instead of three-digit groups; the standard says pupils "use wan and yi as units to express large numbers" at stage 2.
- **Order of operations with two kinds of brackets** (small and medium) at stage 2, one stage before Singapore's usual placement of such work.
- **Mean at G3-4, percentages and angle sums at G5-6.** The program's Level 5 angle and percent lessons are on grade, but Level 6 mean (6.9) is earlier than usual in China.
- **Negative numbers appear only as an introductory thematic activity** in stage 3 and are formally taught in secondary school; lesson 6.3 (adding and subtracting negatives) goes beyond the primary standard.
- **Shanghai and Beijing differences:** I could not check local textbook series. Do not assume local sequences match the national stage bands exactly [UNVERIFIED].
- **Chanting the multiplication table (口诀) and a "line segment diagram" for word problems** are widely reported textbook practices [SECONDARY / UNVERIFIED]; the standard names neither.

### 3.6 Which levels fit a Chinese child best (cautious)

- Grades 1-2 (ages about 6-8): **Level 1 and Level 2**; both are on the standard's grade-2 content, and number work in Level 2 (3-digit) is slightly behind the standard's ten-thousand range.
- Grades 3-4 (ages about 8-10): **Level 3 and Level 4**; area and perimeter (3.7), angles with a protractor (4.6) and mean are all stage 2.
- Grades 5-6 (ages about 10-12): **Level 5 and Level 6**; Level 5's area, volume, percentage and fraction lessons are stage 3, Level 6's negatives, probability (numeric) and algebra are ahead of the primary standard.
- Within a band the year is set by the textbook; use the program's diagnostic.


## 4. Japan (Tokyo; national Course of Study)

### 4.1 Sources

| Item | Detail |
|---|---|
| Current document (Japanese) | **小学校学習指導要領（平成29年告示）解説 算数編** (Commentary on the Elementary School Course of Study, announced 2017: Arithmetic/Mathematics), MEXT, July 2017. Official, Japanese only. I read the table of contents, the summary of the revision and the grade-by-grade content chart (figure 1, pages 10-15), and searched the body for specific topics. Full implementation from April 2020 (stated in its preface). |
| URL | https://www.mext.go.jp/content/20211102-mxt_kyoiku02-100002607_04.pdf |
| Official English text | The MEXT English page lists only the **General Provisions** of the 2017 course of study in English. For mathematics, the only official MEXT English text is the **2008-2009 revision, "Arithmetic"** (https://www.mext.go.jp/component/english/__icsFiles/afieldfile/2011/03/17/1303755_004.pdf), which I read in full. MEXT page: https://www.mext.go.jp/en/policy/education/elsec/title02/detail02/1373859.htm |
| English translation of the 2008 commentary | [SECONDARY] CRICED, University of Tsukuba (ed. M. Isoda), *Elementary School Teaching Guide for the Japanese Course of Study: Mathematics (Grade 1-6)* with the English translation on the opposite page, January 2010: https://www.criced.tsukuba.ac.jp/math/apec/ICME12/Lesson_Study_set/ElementarySchoolTeachingGuide-Mathmatics-JP-EN.pdf (I read the preface only). |
| How the two were combined | The grade chart below uses the 2008 English text as the base and applies the 2017 changes listed in the 2017 commentary: metric-system structure moved down to G3-G5; speed moved G6 to G5; fraction x integer and fraction ÷ integer moved G5 to G6; prime numbers moved G5 to lower secondary year 1; mean, median, mode and frequency classes moved lower secondary year 1 to G6; dot plots added at G6; the strand "Quantitative Relations" became "Changes and Relationships" plus "Data Utilisation". |
| Typical ages | Grade 1 about 6-7 through Grade 6 about 11-12 [UNVERIFIED: not stated in the documents I read]. |

### 4.2 Structure and notable features

- **Strands (2017):** Numbers and Calculations; Geometrical Figures; Measurement; Changes and Relationships; Data Utilisation. (2008: Numbers and Calculations; Quantities and Measurements; Geometrical Figures; Mathematical Relations.)
- **Mathematical activities** are required in every grade; the 2008 text lists them under each grade (for example G2: "find properties and rules of the multiplication by constructing and observing multiplication tables"; G5: "inductively think and explain that the sum of the three angles of a triangle is equal to 180 degrees").
- **Thinking and expressing:** the 2008 text asks teachers to include "thinking by using words, numbers, algebraic expressions, figures, diagrams, tables and graphs, and explaining and communicating their thoughts among themselves". Lesson study and structured problem solving are well documented features of Japanese practice; the CRICED preface cites Isoda et al. (2007) *Japanese Lesson Study in Mathematics* [SECONDARY]. The course of study itself prescribes content and activities, not a lesson format.
- **Terms and symbols are listed by grade** so that vocabulary is controlled (for example "sum, difference, product, quotient, proper fraction, improper fraction, mixed fraction, parallel, perpendicular" at G4).
- **Soroban (abacus):** G3 (number representation, add/sub) and G4 (calculation); the 2008 text also says soroban or other teaching aids should be used in the lower grades to deepen understanding of numbers.
- **Estimation and mental calculation** are explicit; column algorithms are taught from G2.
- **Programming:** the 2017 commentary says programming may be done in connection with the G5 regular-polygon construction topic (repeat the same steps, change one number to get different polygons); that is the one place a topic in this program (lesson 6.7) is tied to code.
- **Pi is taken as 3.14**, and the Japanese percentage idea "buai" is touched on at G5.

### 4.3 Grade by grade (2008 English text plus 2017 shifts)

| Grade | Numbers and calculations | Measurement | Geometrical figures | Relations and data |
|---|---|---|---|---|
| G1 | numbers to 100 (3-digit in simple cases); numbers as sums or differences; ten as a unit; add of two one-digit numbers and subtract; simple two-digit add/sub | compare length, area, volume directly and with arbitrary units; read clock times | recognise shapes and their features; position words (front, back, left, right) | expressions for add/sub; pictures and diagrams for quantities |
| G2 | 4-digit numbers; 1/2 and 1/4; column add/sub; **multiplication table up to 9 x 9**; two-digit x one-digit in simple cases | mm, cm, m; mL, dL, L; days, hours, minutes | triangles and quadrilaterals; squares, rectangles, right triangles; box shapes | simple tables and graphs; expressions for x |
| G3 | man (10^4); x10 and x100; add/sub of 3- and 4-digit numbers; multiplication by 2- and 3-digit numbers; **division (remainders; 1-digit divisors)**; decimals to tenths with add/sub; fractions as unit fractions, simple add/sub; **soroban** | km; g and kg; seconds; elapsed time; metric prefix structure (2017) | isosceles and equilateral triangles; **angle**; circle, sphere (radius, diameter) | box-expressions; **bar graphs** |
| G4 | oku and cho; **rounding, estimation**; division by 2-digit divisors; decimals x and ÷ by whole numbers; like-denominator fractions, equal fractions; soroban | **area** (cm2, m2, km2; rectangle); **angle in degrees**; are, hectare | parallel and perpendicular; parallelogram, rhombus, trapezoid; cube, cuboid, **nets**; position | **mixed-operation and bracket expressions, formulas**; laws of operations; **broken-line graphs**; two varying quantities; simple ratio (2017) |
| G5 | even and odd; divisors and multiples (GCD, LCM); decimals x and ÷; **fractions: unlike denominators, equal fractions, division as fraction**; (prime numbers moved to secondary in 2017) | **area of triangle, parallelogram, rhombus, trapezoid; volume** (cm3, m3); average of measured values; **per-unit quantity and speed** (2017) | polygons, regular polygons; **congruence**; circumference ratio; prisms and cylinders; **angle sums of triangle (180) and quadrilateral (360)** | **percentage**; proportional relationships (simple); pie and band graphs |
| G6 | **fraction x and ÷ fraction** (and by integers, 2017); consolidating decimals and fractions | area of circle; volume of prisms and cylinders; approximate area | enlargement and reduction; **line symmetry and point symmetry** | letters (a, x) in expressions; **ratio**; proportion, inverse proportion; **mean, median, mode, frequency tables, dot plots**; **possible cases (systematic listing)** |

Not in the Japanese primary documents I read (searched for, absent): money as a mathematical topic (the word appears only in moral education), negative numbers (lower secondary year 1), numeric probability (lower secondary), clock arithmetic, sequences as such, equation solving (lower secondary).

### 4.4 Coverage: major Japanese topics with no or little program lesson

- Multi-digit multiplication and division algorithms (G3-G4), decimal x and ÷ (G4-G5), fraction x and ÷ beyond lessons 5.2-5.3.
- Circles (G3 radius and diameter, G5 pi, G6 area), congruence (G5), enlargement and reduction (G6), nets of prisms and cylinders, volume of prisms and cylinders (G6).
- Proportion and inverse proportion, ratio (G6).
- Position (G4) and coordinates.
- Soroban (G3-G4): the program has none; the abacus method is a real Japanese primary feature.
- Pie and band graphs (G5), frequency tables and dot plots (G6).
- Quadrilateral families (parallelogram, rhombus, trapezoid at G4).

### 4.5 What a family moving between systems would notice

- **Multiplication table up to 9 x 9 (九九) in G2**, not 0-10. Learned and recited in Japan; recitation of 九九 is a widely reported school practice [SECONDARY / UNVERIFIED in the standard, which says only "make the multiplication table up to 9 times 9" by exploring properties, and "learn" it].
- **"Carry up" and "carry down" (繰り上がり, 繰り下がり)** appear in the commentary where Singapore says regrouping, and Hong Kong says "borrowing". Column forms (筆算) from G2.
- **Four-digit grouping** (man, oku, cho) for big numbers; the 2008 text says splitting into 3-digit groups is only "touched upon" at G4.
- **dL is an official unit** at G2 (mL, dL, L) and is rarely used in the other three systems.
- **No money and no 24-hour clock in the content list**; clock reading at G1, time units at G2, seconds at G3.
- **Fractions at G2 to G3, decimals at G3**, earlier than Hong Kong, China and Korea; **fraction multiplication and division at G6**, with the reciprocal idea.
- **Angles measured with a protractor at G4**, **area at G4**, **percentages, volume, speed and angle sums at G5**, matching the program's Level 4-5 lessons.
- **Soroban** is a taught method, not just a tool.
- **Diagrams:** the 2008 text refers generally to "figures, diagrams and number lines"; named tape-diagram and number-line diagram conventions are widely used in textbooks [SECONDARY / UNVERIFIED in the documents I read].
- **Combinatorics at G6, probability only in secondary:** lesson 6.5 is on grade, lesson 6.6 is ahead of the primary curriculum, lesson 6.3 (negatives) is secondary year 1 content.

### 4.6 Which levels fit a Japanese child best (cautious)

- G1-G2 (ages about 6-8): **Level 1 and Level 2.** Level 3 (numbers to 10 000, 6-9 tables) is review of G2 material.
- G3-G4 (ages about 8-10): **Level 3 and Level 4**; Japanese fractions and decimals are earlier than the program's Level 2/Level 4 sequence, so those lessons are likely easy.
- G5-G6 (ages about 10-12): **Level 5 and Level 6**; Level 5 area, volume, rate and percent are on grade, Level 6 combinatorics matches G6, and negative numbers, algebra equations and numeric probability are ahead.
- Level 4 factors (4.1) and Level 3 area (3.7) are G4-G5 topics, so a G3 child is a year or two ahead of the curriculum on those. Placement should come from the diagnostic.


## 5. South Korea (Seoul; national 2022 revised curriculum)

### 5.1 Sources

| Item | Detail |
|---|---|
| Document opened | **2022 개정 수학과 교육과정** (2022 Revised Mathematics Curriculum), Ministry of Education, Republic of Korea. I read the full curriculum text (content system, achievement standards for elementary grade bands 1-2, 3-4, 5-6, and the interpretation notes) from a **publisher's reproduction**: Visang textbook company's file "2022 개정 초등 수학과 교육과정.pdf", whose running footer shows it is part of the 3-1 teacher's guide (수학 3-1 교사용 지도서). [SECONDARY: a textbook publisher's reproduction of the official text, PDF dated May 2024]. |
| URL | https://dn22.vivasam.com/VS/ES/MAT/106393/promo_library/ref_common/2022%20%EA%B0%9C%EC%A0%95%20%EC%B4%88%EB%93%B1%20%EC%88%98%ED%95%99%EA%B3%BC%20%EA%B5%90%EC%9C%A1%EA%B3%BC%EC%A0%95.pdf |
| Official source | The official text is a Ministry of Education notice published through the National Curriculum Information Center (NCIC). I did not reach the NCIC site, so the notice number is [UNVERIFIED] (I believe 2022-33; not confirmed in the text I read). The content-system structure and achievement-standard codes ([2수01-01] and so on) are as printed in the reproduction. |
| English | No official English translation of the mathematics curriculum was found. Search results gave only Korean journal abstracts in English [SECONDARY] confirming the four content areas and the five competencies. |
| Roll-out | The 2022 revision is being phased in from 2024 to 2026 by grade [UNVERIFIED: from search snippets, not from the curriculum text]. Textbooks are produced by publishers, so the year within a band is set by textbooks, which I did not review. |
| Typical ages | Elementary grades 1-6 about ages 6-12 in international age counting [UNVERIFIED: not stated in the text]. |

### 5.2 Structure and notable features (verified in the text)

- **Four content areas used from elementary through middle school:** Numbers and Operations (수와 연산), Change and Relationships (변화와 관계), Shapes and Measurement (도형과 측정), Data and Possibility (자료와 가능성). Each area has core ideas plus three categories: knowledge and understanding, process and skills, value and attitude.
- **Five mathematics competencies:** problem solving (문제해결), reasoning (추론), communication (의사소통), connection (연결), information processing (정보처리). The general curriculum adds numeracy, digital and language literacy as foundational literacies.
- **Grade bands:** 1-2, 3-4, 5-6 (then middle school 1-3). Achievement standards are coded by band: [2수..] for grades 1-2, [4수..] for 3-4, [6수..] for 5-6.
- **Process emphasis:** the interpretation notes repeatedly ask for "finding missing information", "changing the conditions to make a new problem" and "checking whether the problem-solving process is valid" (in the 3-4 and 5-6 bands); "exploring why a calculation works" (계산 원리를 탐구) is the verb used for most operation standards. This is the closest of the four documents to the program's "Explain why".
- **Digital tools and calculators:** calculators may be used when calculation skill is not the aim (3-4 band), and "digital tools" are named for graph drawing (bar and line graphs in 3-4, band and pie graphs in 5-6). **Mathematical modelling** is named as a value and attitude in middle school.
- No abacus found in the text (searched).

### 5.3 Band by band (achievement standards, by code)

| Band | Numbers and operations | Change and relationships | Shapes and measurement | Data and possibility |
|---|---|---|---|---|
| 1-2 | 0 to 100 and up to 4-digit numbers, place value; decompose and compose numbers; add/sub within two digits (sums may exceed 100); relation between add and sub; box in add/sub sentences; meaning of multiplication, **multiplication table (곱셈구구)** | find and make patterns in objects, designs and numbers (repeating or increasing) | cuboid, cylinder, sphere; triangle, square, circle (intuitive); stacking cubes, positions; compare length, capacity, weight, area; **time to the minute, hour/minute/day/week/month/year**; cm and m; length estimation, add/sub of lengths | classify; tables; graphs with symbols |
| 3-4 | numbers above 10 000; **3-digit add/sub**; multiplication by 1- and 2-digit numbers; **division (1- and 2-digit divisors, quotient and remainder)**; estimation; **fractions (unit, proper, improper, mixed; compare; like-denominator add/sub); decimals to 3 places and add/sub to 2 places** | rules in numbers and arithmetic arrays; equals sign for equal quantities | **line, segment, ray; angle, right, acute, obtuse; perpendicular and parallel; slide, flip, turn; circle (centre, radius, diameter, compass); isosceles, equilateral, right, acute, obtuse triangles; rectangle, square, trapezoid, parallelogram, rhombus; polygons, regular polygons; seconds; mm, km; L, mL; g, kg, tonne; degree and protractor; angle sums of triangles and quadrilaterals** | pictograph, bar graph, line graph; data collection |
| 5-6 | **mixed operations (order)**; ranges (above, below, at least, under, at most); **rounding up, down, off**; **factors and GCD; multiples and LCM**; **equal fractions, reduce, common denominator; unlike-denominator add/sub; fraction x and ÷; (whole) ÷ (whole) as fraction or decimal; decimal x and ÷** | **correspondence tables (box and triangle expressions); ratio; rate (ratio value, as fraction, decimal or percent); proportion; proportional division** | **congruence; line and point symmetry; cuboid and cube; prism and pyramid; cylinder, cone, sphere; nets; cube-stack views; perimeter; area units; area of rectangle, parallelogram, triangle, trapezoid, rhombus; circumference, pi, circle area; surface area; volume** | **mean; band and pie graphs; "possibility" expressed as a number for simple events (0, 1/2, 1), with coin, dice and spinner experiments** |

Not in the Korean primary standards (searched for, absent): negative numbers (introduced with the integers and rational numbers in middle school), algebraic expressions with letters (middle school; "box" and "triangle" symbols only in primary), equations (middle school; only proportion equations in 5-6), speed (the word does not appear in the elementary standards), counting rules (middle school), prime factorisation (middle school; the notes say it is not used to find GCD in primary), median and mode (middle school), money (the primary standards I read do not list it).

### 5.4 Coverage: major Korean topics with no or little program lesson

- Written multiplication and division algorithms (3-4 band) and decimal and fraction operations (5-6 band) beyond lessons 4.4, 4.5, 5.2, 5.3.
- Shapes: triangles and quadrilaterals as classified families, circles with a compass (3-4), slides, flips and turns (3-4), congruence (5-6), cylinders, cones, prisms, pyramids, surface area.
- Ratio, rate as a percent, proportion and proportional division (5-6).
- Band and pie graphs (5-6).
- Time units to the second, seconds, durations (3-4; partly lesson 3.9).
- Estimation with rounding up and down (5-6; lesson 4.2 covers rounding).
- Perimeter, area and volume are in the program but the Korean sequence is later (see below).

### 5.5 What a family moving between systems would notice

- **Korea is later for add/sub with 3 digits (3-4 band), division (3-4), and especially perimeter, area and volume (5-6 band):** a Level 3 area and perimeter lesson (3.7) is two to three years ahead of the Korean standard, and Level 4 composite area (4.7) is one to two years ahead. Level 2's 3-digit add/sub (2.2) is a band ahead.
- **Korea is earlier for angle sums of triangles and quadrilaterals (3-4 band, "infer in several ways and explain")** and regular polygons, so Level 5 angle chasing (5.8) and Level 6 turtle geometry (6.7) are on grade or review.
- **"Possibility" (가능성) is numeric in the 5-6 band, but only for simple events** (the notes give 0, 1/2 and 1, with coin, dice and spinner experiments); Hong Kong, China and Japan do not teach numeric probability in primary. Lesson 6.6 is on topic but goes further (all 36 outcomes of two dice, fairness). Counting (6.5), negatives (6.3) and algebra (6.4) are middle school.
- **Range words**: 이상 (at least), 이하 (at most), 초과 (more than), 미만 (less than) are formal 5-6 band vocabulary for number ranges (6수01-02).
- **Weight and mass:** the notes say that primary school does not strictly distinguish weight and mass (as Hong Kong's supplement also recommends).
- **No money, no speed** in the elementary standard (unlike Hong Kong and China for money, Japan and Hong Kong for speed).
- **Multiplication table (곱셈구구) in the 1-2 band**, tables traditionally learned by recitation (구구단) [SECONDARY / UNVERIFIED; the curriculum says only to "understand the multiplication table and multiply one-digit numbers"].
- **Textbook-level conventions** (how subtraction with exchange is named, bar or line-segment diagrams, how percent is first drawn) are set by approved textbooks and were not reviewed [UNVERIFIED].
- **A new curriculum rolling out:** families may meet different edition textbooks depending on the grade (see roll-out above).

### 5.6 Which levels fit a Korean child best (cautious)

- Grades 1-2 (about ages 6-8): **Level 1**, and Level 2 for children comfortable with 3-digit numbers; Level 2 fractions and 3-digit add/sub are later in Korea.
- Grades 3-4 (about ages 8-10): **Level 3 and Level 4**. Number and operation lessons fit; geometry lessons are further ahead, and the diagnostic result (not age) should decide.
- Grades 5-6 (about ages 10-12): **Level 5 and Level 6**; Level 5 area, volume, percent and fractions are on band, Level 6 probability is on topic (deeper than the standard's simple-event version), and negatives, equations and counting are ahead of the primary standard.
- Because Korea teaches geometry measurement later and number operations at a similar pace, a Korean child may be placed a level lower in geometry-heavy lessons; the program lets a family change level before lesson 1.


## 6. Cross-jurisdiction summary

### 6.1 Where the four systems agree and differ (from the documents above)

| Topic | HK | China | Japan | Korea |
|---|---|---|---|---|
| Multiplication table | P2, table 0-10 | G1-2 | G2, up to 9 x 9 | 1-2 band |
| Division with remainder | P2 concept, P3 | G3-4 (multi-digit division; remainder not named in the text I read) | G3 | 3-4 band |
| Fractions first taught | P3 | G3-4 | G2 (1/2, 1/4), G3 | 3-4 band |
| Decimals first taught | P4 | G3-4 | G3 (tenths) | 3-4 band |
| Area of rectangle | P4 | G3-4 | G4 | 5-6 band |
| Protractor and degree | P6 | G3-4 | G4 | 3-4 band |
| Percent | P6 | G5-6 | G5 | 5-6 band |
| Volume of cuboid | P5 | G5-6 | G5 | 5-6 band |
| Mean (average) | P6 | G3-4 | G5 (measured values), G6 | 5-6 band |
| Letters / algebra | P5 | G3-4 (letters for laws), G5-6 | G6 | middle school |
| Negative numbers | secondary | G5-6 intro only | lower secondary | middle school |
| Counting / probability | none | G5-6 qualitative | G6 counting; probability secondary | 5-6 band simple numeric; counting middle school |
| Abacus | none found | mentioned G1-2 | soroban G3-4 | none found |
| Money | P1-2 | G1-2 (thematic) | not listed | not listed |

### 6.2 Program coverage of the four curricula's grade 1-6 topics: the common gaps

Topics that appear in the primary curriculum of **all four** systems and have no dedicated lesson in the program (the program is an enrichment course, not a syllabus, so gaps are expected):

1. Written multi-digit multiplication and long division, decimal operations, and fraction x and ÷ beyond lessons 5.2-5.3.
2. Circles: circumference, pi, circle area (HK P5-6, China G5-6, Japan G3-6, Korea 3-4 and 5-6 bands).
3. Ratio and proportion (HK P5, China G5-6, Japan G6, Korea 5-6).
4. Cylinders, cones, prisms, surface area and volume of solids beyond cuboids.
5. Position and movement: coordinates, translation, rotation, reflection, scale (China stage 2-3, Japan G4 and G6, Korea 3-4, HK P1-4 directions).
6. Pie charts and compound or band graphs (HK P5-6, China G5-6, Japan G5, Korea 5-6).
7. Classification of triangles and quadrilaterals as families (HK P2-4, China G3-4, Japan G2-4, Korea 3-4).
8. Time reading and calendar arithmetic as a topic (lesson 2.9, 3.9 touch it).

Topics the program covers that **none** of the four primary documents contain as a topic: clock (modular) arithmetic and ciphers (6.8) and nth-term sequences (6.1). Topics outside most primary curricula: negatives, counting, probability, algebra (Level 6). These are the Level 6 enrichment choices and are consistent with the program's "ahead of the syllabus" label there, but they should not be called "common curriculum topics".

### 6.3 Cautions for readers using the matrix

- The program's lessons are **inquiry puzzles at a chosen depth**, not syllabus units. A "SAME" cell means the topic is taught in the same grade; it does not mean the program's lesson content or difficulty matches a school's.
- Hong Kong and Japan name single grades; China and Korea name two-year bands.
- Most Chinese and Japanese content was read in the original language. Chinese was read from page images of the ministry PDF; Japanese from the ministry commentary text; Korean from the publisher's reproduction. The Hong Kong and Japanese 2008 English texts are official English.
- Everything in the "family would notice" sections that I marked `[SECONDARY]` or `[UNVERIFIED]` is general-knowledge colour, not curriculum fact.

## 7. What is safe to claim

**Supported by this research and safe to say** (with the caveat that these are internal research notes):

- "Topics in the Math Inquirers lessons are commonly taught in primary schools in many curricula, including Hong Kong, Mainland China, Japan and South Korea." This is supported: 36 of the 55 single-topic lessons are taught in the same or an earlier grade in Hong Kong, 47 in China, 40 in Japan and 39 in Korea (matrix tallies in section 1), and the lessons that are later or absent are mostly the Level 6 enrichment topics.
- "Our program was written independently as enrichment; the level names follow the Singapore primary year, and each level is a three-year age band." (A fact about the program, not about other curricula.)
- For specific topics, a family-facing page can say, for example, that multiplication tables, fractions, area and perimeter, angles, percentages and mean are taught in primary school in these four places, and that the grade differs by place. That statement is supported by section 6.1, which cites each document.
- Hong Kong's primary curriculum includes optional enrichment topics (Sudoku, sorting, Eulerian paths, map colouring) and ten hours a year of "Inquiry and investigation" (2017 EDB supplement). Korea's 2022 curriculum names five mathematics competencies (problem solving, reasoning, communication, connection, information processing). China's 2022 standard names "four basics" including basic activity experience. Japan's course of study lists mathematical activities for every grade. These are fair neutral statements about the four systems; they are not claims about this program.

**Do not claim:**

- Alignment, equivalence, endorsement, accreditation, approval or recognition by, or affiliation with, any ministry or curriculum body: the Hong Kong Education Bureau and Curriculum Development Council, the Ministry of Education of the PRC (or any Shanghai or Beijing authority), MEXT, the Korean Ministry of Education or KICE. None of this research supports such a claim, and the program has no relationship with any of them.
- That the program "follows", "covers", "prepares children for" or "is mapped to" any of these curricula as a whole, or that a child in those systems "needs" a level. The mapping is partial, by lesson topic, and several lessons are intentionally ahead of the curriculum.
- That the program helps children "get ahead" in those school systems, or improves exam results. No evidence of that was gathered.
- Any specific "same grade" statement for China or Korea at the single-year level: the standards use two-year bands and the year is set by textbooks, which I did not review.
- Anything about Shanghai, Beijing or Tokyo local textbooks or local curricula; I read only the national documents.
- Any statement marked `[UNVERIFIED]` or `[SECONDARY]` above.

**Suggested wording if one line is wanted:** "Topics are commonly taught in many curricula; the grade they appear in varies by country." Keep it general and do not name ministries.

## 8. Source list (one place)

1. Hong Kong EDB/CDC, *Supplement to Mathematics Education KLA Curriculum Guide: Learning Content of Primary Mathematics* (2017): https://www.edb.gov.hk/attachment/en/curriculum-development/kla/ma/curr/pmc2017_e.pdf (opened, full).
2. Ministry of Education of the PRC, *义务教育数学课程标准（2022年版）*: notice page https://www.moe.gov.cn/srcsite/A26/s8001/202204/t20220420_619921.html ; PDF http://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220510531636118932.pdf (opened as page images; pages on course nature, competencies, stage goals, content requirements for number, geometry, statistics, integrated practice).
3. MEXT, *小学校学習指導要領（平成29年告示）解説 算数編* (2017): https://www.mext.go.jp/content/20211102-mxt_kyoiku02-100002607_04.pdf (opened; revision summary and figure 1 read, body searched).
4. MEXT, Course of Study 2008-2009, "Arithmetic" (English): https://www.mext.go.jp/component/english/__icsFiles/afieldfile/2011/03/17/1303755_004.pdf (opened, full). MEXT English page: https://www.mext.go.jp/en/policy/education/elsec/title02/detail02/1373859.htm
5. [SECONDARY] CRICED, University of Tsukuba (ed. Isoda), *Elementary School Teaching Guide for the Japanese Course of Study: Mathematics* (2010): https://www.criced.tsukuba.ac.jp/math/apec/ICME12/Lesson_Study_set/ElementarySchoolTeachingGuide-Mathmatics-JP-EN.pdf (preface only).
6. [SECONDARY] Visang, 2022 개정 초등 수학과 교육과정 (reproduction of the Korean Ministry of Education text, 3-1 teacher's guide): https://dn22.vivasam.com/VS/ES/MAT/106393/promo_library/ref_common/2022%20%EA%B0%9C%EC%A0%95%20%EC%B4%88%EB%93%B1%20%EC%88%98%ED%95%99%EA%B3%BC%20%EA%B5%90%EC%9C%A1%EA%B3%BC%EC%A0%95.pdf (opened, full).
7. Program sources: `docs/levels_and_placement.md`, `hp/lessons.js`, `p2..p6/content/l1..l10.js`.

Not reached or not used: Korea NCIC (official portal), KICE, EDB parent curriculum guide Chapter 2, UNESCO IBE and OECD summaries (searched, nothing usable on primary grade content).
