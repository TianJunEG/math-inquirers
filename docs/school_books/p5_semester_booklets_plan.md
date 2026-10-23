# Primary 5 early-finisher puzzles: two semester booklets (plan)

Date: 24 Oct 2026. Model: `docs/school_books/p2_semester_booklets_plan.md` and the P1 and P2 build reports and audits. Pipeline: `school/p5/` (copied from `school/p2/`; no other level and no shared library was edited). Build report and open items: `docs/school_books/p5_semester_booklets_build_report.md`.

## 0. Decisions this plan follows

Owner decisions (`docs/terms/owner_decisions.md`): two booklets per level, Semester 1 (typical Terms 1 and 2) and Semester 2 (Terms 3 and 4), 20 single-sided pupil pages each, 10 one-star and 10 two-star; self-checking; pure black and white; no Mi; teacher notes say schools vary; annual licence (lawyer wording DRAFT); publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers"; registered office and contact email as in P2; DRAFT stamps; no MOE or SASMO claim beyond "The mathematics syllabus is published by the Ministry of Education, Singapore."; the not-affiliated sentence on the cover only (P2-NOTAFFIL-FRONT); "Pictures are not actual size." in the teacher notes; original material only; no price. No coin or note pictures at Primary 5 (the money pages here are prices as text), so COINS-FIX-SIZE is not exercised.

Reading load (plan.md section 11): Primary 5 = at most 16 words a sentence, at most 4 instruction sentences, check strip at most 24 words; checked in `validate.py`.

**Syllabus source.** The outcome lines and their numbers are copied as printed in the Primary Mathematics Syllabus P1 to P6 (2021 edition, updated October 2025), Primary 5 Standard, pages 41 and 42 (the PDF was read after the first build; the first build had used the repository summary `docs/moe/syllabus_by_level.md`). Only the outcome-line wording is copied; everything else is our own. See `docs/school_books/p5_outcome_wording.md`.

**Differences between the brief and the syllabus (decided by the syllabus, as the brief asked to confirm).** The brief lists "average" and "pie charts" as Primary 5. The syllabus has no Statistics strand in Primary 5 Standard; pie charts are Primary 4; average is Primary 6; ratio is Primary 6. None of the four is used. The 2020 to 2024 school papers (`docs/books/p5_school_paper_patterns.md`) set ratio and average at Primary 5; that is the old syllabus and is not used here.

## 1. Gap analysis: every Primary 5 outcome line against the pages

One row per outcome line of the syllabus (numbered as the PDF numbers them). Every line is practised by at least one page.

| Outcome line (syllabus number and wording) | Pages | Coverage |
|---|---|---|
| Whole Numbers 1.1: reading and writing numbers in numerals and in words (numbers up to 10 million) | S1-01, S1-02 | Part: reading and choosing numerals and words; writing number words by hand is not checked |
| Whole Numbers 2.1: multiplying and dividing by 10, 100, 1000 and their multiples without calculator | S1-03, S1-04 | Full |
| Whole Numbers 2.2: order of operations without calculator | S1-05, S1-06, S1-07 | Full |
| Whole Numbers 2.3: use of brackets without calculator | S1-05, S1-06, S1-07 | Full |
| Fractions 1.1: dividing a whole number by a whole number with quotient as a fraction | S1-08 | Full (one page) |
| Fractions 1.2: expressing fractions as decimals | S1-09 | Full, terminating decimals only (one page) |
| Fractions 2.1: adding and subtracting mixed numbers | S1-10, S1-11 | Full |
| Fractions 2.2: multiplying a proper/improper fraction and a whole number without calculator | S1-12, S1-13, S1-16 | Full |
| Fractions 2.3: multiplying a proper fraction and a proper/improper fraction without calculator | S1-14, S1-15, S1-16 | Full |
| Fractions 2.4: multiplying two improper fractions | S1-15 | Full (inside P5-15) |
| Fractions 2.5: multiplying a mixed number and a whole number | S1-15 | Full (inside P5-15) |
| Decimals 1.1: multiplying and dividing decimals (up to 3 decimal places) by 10, 100, 1000 and their multiples without calculator | S1-17, S1-18 | Full |
| Decimals 1.2: converting a measurement from a smaller unit to a larger unit in decimal form, and vice versa (kilometres and metres; metres and centimetres; kilograms and grams; litres and millilitres) | S1-19, S1-20 | Full |
| Percentage 1.1: expressing a part of a whole as a percentage | S2-01, S2-02 | Full |
| Percentage 1.2: use of % | S2-01, S2-02 | Full |
| Percentage 1.3: finding a percentage part of a whole | S2-02, S2-03, S2-04, S2-05 | Full |
| Percentage 1.4: finding discount, GST and annual interest | S2-02, S2-03, S2-04, S2-05 | Full: discount, GST at 9%, one year of simple interest (compound interest not used) |
| Rate 1.1: rate as the amount of a quantity per unit of another quantity | S2-06, S2-07 | Full: no speed wording |
| Rate 1.2: finding rate, total amount or number of units given the other two quantities | S2-06, S2-07 | Full: rate, total, number of units |
| Area of Triangle 1.1: concepts of base and height of a triangle | S2-08, S2-09 | Full |
| Area of Triangle 1.2: area of triangle | S2-09, S2-10, S2-11 | Full |
| Area of Triangle 1.3: finding the area of composite figures made up of rectangles, squares and triangles | S2-11 | Full for a rectangle plus or minus a triangle (one page only) |
| Volume 2.1: building solids with unit cubes | S2-12 | Part: counting cubes in a drawing; building with real cubes cannot be checked |
| Volume 2.2: measuring volume in cubic units, cm³/m³, excluding conversion between cm³ and m³ | S2-13 | Full (one page); no conversion between cm3 and m3, as in the syllabus line |
| Volume 2.3: drawing cubes and cuboids on isometric grid | S2-12 | Part: reading isometric drawings only; drawing on an isometric grid is not checked |
| Volume 2.4: volume of a cube/cuboid | S2-12, S2-13, S2-14, S2-15 | Full |
| Volume 2.5: finding the volume of liquid in a rectangular tank | S2-15 | Full |
| Volume 2.6: relationship between ℓ (or mℓ) with cm³ | S2-14, S2-15 | Full |
| Geometry 1.1: angles on a straight line | S2-16, S2-17, S2-20 | Full |
| Geometry 1.2: angles at a point | S2-16, S2-17 | Full |
| Geometry 1.3: vertically opposite angles | S2-16, S2-17, S2-20 | Full |
| Geometry 1.4: finding unknown angles | S2-16, S2-17, S2-18, S2-20 | Full |
| Geometry 2.1: properties of isosceles triangle, equilateral triangle, right-angled triangle | S2-18, S2-20 | Full |
| Geometry 2.2: angle sum of a triangle | S2-18, S2-20 | Full |
| Geometry 2.3: finding unknown angles without additional construction of lines | S2-18, S2-20 | Full |
| Geometry 3.1: properties of parallelogram, rhombus, trapezium | S2-19 | Part: statements and angles; no drawing, no diagonals |
| Geometry 3.2: finding unknown angles without additional construction of lines | S2-19 | Part: statements and angles; no drawing, no diagonals |

**Not covered, or only in part (for the owner).** Pupil drawing cannot be checked on a printed page: drawing cubes and cuboids on an isometric grid (VO 2.3), drawing a triangle of a given area, completing figures; building with real unit cubes (VO 2.1); writing number words by hand. Printed substitutes read a drawing instead. Fraction pages use denominators to 12 (to 50 for fraction-to-decimal); percentage uses simple interest only (the syllabus says "annual interest" only; P5-25 uses one year of simple interest, on the auditor's reading of school papers; compound interest would be an extra and is not used). Word problems "with a model" (bar models) are not drawn: the syllabus summary does not name bar models.

## 2. Primary 6 and other content excluded (never used)

From the syllabus: ratio in any form (a:b, "for every"); average, mean, pie charts and any statistics; fraction division (a fraction by a whole number or by a fraction); finding the whole from a percentage and percentage increase or decrease as a topic (GST and a price after a percentage added are Primary 5 "finding GST"); algebra and letters for unknowns (boxes and "?" only; angles are named by points as in the syllabus "∠" use); circles, radius, circumference, pi; finding a missing dimension of a cuboid from its volume, a water level from a volume, cube roots; speed (the word is never used); prime numbers, negative numbers, probability, coordinates, surface area, median and mode, pentagon and hexagon. `validate.py` scans the pupil pages and the key for these words.

## 3. Mechanisms (the audits of P1 and P2 asked for more variety)

Code word 16 pages, lettered choices 6 and true-or-false rows 2 (one of them with three choices: true, false, not possible to tell), route 4, matching 4, ordering 3, colour by code 2, balance (put the answer back) 1, magic square 1, number-chain loop 1: 40 pages. Code-word pages are 16 of 40 (P2 had 23). Each page keeps one answer. Tiers: two stars never mean a new topic, only two steps or two clues.

## 4. The 40-page allocation

Typical order, schools vary. Semester 1 holds whole numbers, order of operations, fractions and decimals; Semester 2 holds percentage, rate, area of triangles, volume and angles. Pages are numbered P5-01 to P5-40 in booklet order, so the footer reads S1-07 (P5-07) and S2-07 (P5-27).

### Semester 1 (Terms 1 and 2)

| Pos | Page | Title | Stars | Outcomes | Mechanism |
|---|---|---|---|---|---|
| S1-01 | P5-01 | Millions | 1 | Whole Numbers: numbers to 10 million | Lettered choices (place value); Word from the letters of the right choices (6 letters) |
| S1-02 | P5-02 | Seven Digits | 2 | Whole Numbers: numbers to 10 million | Code-breaker (digit cards); Code word (6 letters) |
| S1-03 | P5-03 | Zero Hunt | 1 | Whole Numbers: multiply and divide by 10, 100, 1000 and multiples | Ordering (lettered cards); Letters of the cards in the order asked spell a word (6 letters) |
| S1-04 | P5-04 | Multiples Route | 2 | Whole Numbers: multiply and divide by 10, 100, 1000 and multiples | Maze / path; Route: the line must reach FINISH through the right number of boxes, every box following the rule |
| S1-05 | P5-05 | Colour the Rocket | 1 | Whole Numbers 2.2, Whole Numbers 2.3 | Colour by code (pupils colour with their own crayons); Colour key and tally: every answer must be on the key, the number of parts of each colour must match the box, and the parts in the same place on the left and on the right match |
| S1-06 | P5-06 | Brackets Match | 2 | Whole Numbers 2.2, Whole Numbers 2.3 | Matching (lettered cards); Letters of the matching cards, tile 1 to 6, spell a word |
| S1-07 | P5-07 | Both Sides Equal | 2 | Whole Numbers 2.2, Whole Numbers 2.3 | Balance (put the answer back); Put every number back in its box: both sides of every line must be equal |
| S1-08 | P5-08 | Sharing Equally | 1 | Fractions 1.1 | Code-breaker (division as a fraction); Code word (6 letters) |
| S1-09 | P5-09 | Fractions as Decimals | 1 | Fractions 1.2 | Matching (lettered cards); Letters of the matching cards, tile 1 to 6, spell a word |
| S1-10 | P5-10 | Mixed Number Magic | 2 | Fractions 2.1 | Magic square (mixed numbers); Total: all eight lines of the square must make the printed total |
| S1-11 | P5-11 | Mixed Number Route | 1 | Fractions 2.1 | Maze / path; Route: the line must reach FINISH through the right number of boxes, every box following the rule |
| S1-12 | P5-12 | Fraction Chain | 1 | Fractions 2.2 | Number chain (loop); Loop: following the arrows round, the last arrow must give the start number again |
| S1-13 | P5-13 | Fraction of a Quantity | 1 | Fractions 2.2 | Code-breaker (fractions of quantities); Code word (6 letters) |
| S1-14 | P5-14 | Fraction Products | 2 | Fractions 2.3 | Ordering (lettered cards); Letters of the cards in the order asked spell a word (6 letters) |
| S1-15 | P5-15 | Big Products | 2 | Fractions 2.3, Fractions 2.4, Fractions 2.5 | Lettered choices (fraction products); Word from the letters of the right choices (6 letters) |
| S1-16 | P5-16 | Remainder Stories | 2 | Fractions 2.2, Fractions 2.3 | Code-breaker (two-step fraction stories); Code word (6 letters) |
| S1-17 | P5-17 | Point Shift | 1 | Decimals 1.1 | Code-breaker (decimal point shifts); Code word (6 letters) |
| S1-18 | P5-18 | True or False | 2 | Decimals 1.1 | True or false table; Word from the letters of the right choices (6 letters) |
| S1-19 | P5-19 | Measures in Decimals | 1 | Decimals 1.2 | Lettered choices (units); Word from the letters of the right choices (6 letters) |
| S1-20 | P5-20 | Unit Switch | 2 | Decimals 1.2 | Code-breaker (measures in stories); Code word (6 letters) |

### Semester 2 (Terms 3 and 4)

| Pos | Page | Title | Stars | Outcomes | Mechanism |
|---|---|---|---|---|---|
| S2-01 | P5-21 | How Many Percent? | 1 | Percentage: a part of a whole as a percentage | Code-breaker (percentages); Code word (6 letters) |
| S2-02 | P5-22 | Colour the Butterfly | 1 | Percentage: a part of a whole as a percentage, Percentage: a percentage part of a whole, Percentage 1.4 | Colour by code (pupils colour with their own crayons); Colour key and tally: every answer must be on the key, the number of parts of each colour must match the box, and the parts in the same place on the left and on the right match |
| S2-03 | P5-23 | Sale Prices | 2 | Percentage 1.4, Percentage: a percentage part of a whole | Ordering (lettered cards); Letters of the cards in the order asked spell a word (6 letters) |
| S2-04 | P5-24 | GST Match | 2 | Percentage 1.4, Percentage: a percentage part of a whole | Matching (lettered cards); Letters of the matching cards, tile 1 to 6, spell a word |
| S2-05 | P5-25 | Annual Interest | 2 | Percentage 1.4, Percentage: a percentage part of a whole | Code-breaker (interest in money stories); Code word (6 letters) |
| S2-06 | P5-26 | Rate Cards | 1 | Rate | Lettered choices (rate); Word from the letters of the right choices (6 letters) |
| S2-07 | P5-27 | Rate Stories | 2 | Rate | Code-breaker (rate stories); Code word (6 letters) |
| S2-08 | P5-28 | Height Hunt | 1 | Area of triangle: base, height and area | Lettered choices (figures); Word from the letters of the right choices (6 letters) |
| S2-09 | P5-29 | Triangle Areas | 1 | Area of triangle: base, height and area | Code-breaker (areas of triangles); Code word (6 letters) |
| S2-10 | P5-30 | Triangle Route | 2 | Area of triangle: base, height and area | Maze / path; Route: the line must reach FINISH through the right number of boxes, every box following the rule |
| S2-11 | P5-31 | Composite Figures | 2 | Area of triangle: composite figures, Area of triangle: base, height and area | Code-breaker (composite areas); Code word (6 letters) |
| S2-12 | P5-32 | Count the Cubes | 1 | Volume 2.1, Volume 2.3, Volume 2.4 | Code-breaker (cubes in a cuboid); Code word (6 letters) |
| S2-13 | P5-33 | Cuboid Volumes | 1 | Volume 2.4, Volume: cubic units (cm³, m³) | Code-breaker (volumes); Code word (6 letters) |
| S2-14 | P5-34 | Tank Match | 2 | Volume 2.4, Volume 2.6 | Matching (lettered cards); Letters of the matching cards, tile 1 to 6, spell a word |
| S2-15 | P5-35 | Tank Tales | 2 | Volume 2.5, Volume 2.6, Volume 2.4 | Code-breaker (tank stories); Code word (6 letters) |
| S2-16 | P5-36 | Angle Route | 1 | Geometry 1.1, Geometry 1.2, Geometry 1.3, Geometry 1.4 | Maze / path; Route: the line must reach FINISH through the right number of boxes, every box following the rule |
| S2-17 | P5-37 | Find the Angle | 1 | Geometry 1.1, Geometry 1.2, Geometry 1.3, Geometry 1.4 | Lettered choices (figures); Word from the letters of the right choices (6 letters) |
| S2-18 | P5-38 | Triangle Angles | 1 | Geometry: angle sum of a triangle, Geometry: properties of triangles, Geometry 1.4 | Code-breaker (angles in triangles); Code word (6 letters) |
| S2-19 | P5-39 | Shape Statements | 2 | Geometry: parallelogram, rhombus, trapezium, Geometry 1.4 | True or false table (three choices); Word from the letters of the right choices (6 letters) |
| S2-20 | P5-40 | Angle Chains | 2 | Geometry 1.4, Geometry: angle sum of a triangle, Geometry 1.1, Geometry 1.3, Geometry: properties of triangles | Code-breaker (angle chains); Code word (6 letters) |

## 5. Ranges and notation

Whole numbers to 10 million with a space between groups of three digits from five digits up; decimals to 3 places; fractions stacked, mixed numbers as whole plus stacked fraction; sign ×, ÷; % sign; units cm, cm², cm³, m³, ℓ and mℓ (the ℓ sign; the litre sign comes from a fallback font, embedded and viewed), ° for degrees, ∠ for angles; money as $4.50 (two places when cents appear); GST 9%; percentages and rates as whole numbers. Instruction sentences at most 16 words.

## 6. Mechanics for self-checking

As in P2: every answer feeds a letter or a closing rule; wrong values give no letter or a decoy letter; the letters of each code word have exactly one arrangement that is a word, tested against about 242 000 words (the P2 129 000-word list plus the public web2, gcide and wordfreq lists); no single letter in another slot, no swap and no wrong choice, order or matching spells a word (every combination is enumerated). The new mechanisms: magic square (K3: every line makes the printed total), number-chain loop (K8: the last arrow returns to the start number), put the answer back (K7).

## 7. Verification per page

A generator with a seed; an independent solver that reads the PRINTED text or drawing (an exact-fraction expression reader for arithmetic, drawn face counts for cubes, the segment coordinates for the height of a triangle, labels in the figures for areas and angles); the wrong-answer enumeration of `validate.py` (95% or better on every page); the word test; a key entry; a viewed render and a 1-bit copy; all 40 pages hand-solved from the render (build report).
