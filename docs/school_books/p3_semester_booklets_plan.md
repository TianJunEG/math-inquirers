# Primary 3 early-finisher puzzles: two semester booklets (plan)

Date: 24 Oct 2026. Models: `docs/school_books/p2_semester_booklets_plan.md` and the P1 and P2 build reports and audits. Pipeline: `school/p3/` (copied from `school/p2/`; P1, P2 and `school/colour_by_code` were not edited). Build report and weak points: `docs/school_books/p3_semester_booklets_build_report.md`. Outcome wording: `docs/school_books/p3_outcome_wording.md`.

## 0. Decisions this plan follows, and what could not be checked

Owner decisions (`docs/terms/owner_decisions.md`, including SCHOOLBOOKS-P3-6-GO of 24 Oct 2026): two booklets, **Semester 1** (typical school Terms 1 and 2) and **Semester 2** (Terms 3 and 4), 20 single-sided A4 pupil pages each, 10 one-star and 10 two-star, self-checking, pure black and white, photocopy-ready, no Mi; teacher notes say that schools vary; annual licence (wording DRAFT for a lawyer, P2-LAWYER-WAIT); publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers"; registered office and contact email as in the P2 front matter; DRAFT stamps on cover, licence, teacher notes and keys; the sentence "Not affiliated with or endorsed by the Ministry of Education, Singapore." on the **cover only** (P2-NOTAFFIL-FRONT) and the factual "The mathematics syllabus is published by the Ministry of Education, Singapore." on the licence page; no claim of MOE or SASMO affiliation or alignment; "Pictures are not actual size." in the teacher notes; original problems only; coins at real proportions and notes 2:1 (COINS-FIX-SIZE; the real-image variant of the money pages stays held back pending a lawyer); footer codes with both numbers.

**Syllabus wording.** The 34 outcome lines were re-read against the syllabus PDF (Primary Mathematics Syllabus P1 to P6, 2021 edition, updated October 2025, Primary 3 on printed pages 35 and 36) on 23 Oct 2026, and the wording in `p3_outcome_wording.md` now follows the PDF's outcome lines (bullets joined into the line). One reading note: Length, Mass and Volume 1.3 says "converting a measurement in compound units to the smaller unit, and vice versa"; the pages mainly go from compound units to the smaller unit, and the vice versa direction (a number of metres written as km and m) is practised only a little, so it is listed as a partial gap.

Sources read: `docs/school_books/plan.md` (templates, reading load: Primary 3 = 18 words a sentence as the brief says; plan.md's own table says 12, the brief overrides), `owner_decisions.md`, `syllabus_by_level.md`, the P2 README, plan, build report and the three P2 audit rounds, the three P1 audit rounds, `docs/books/p3_school_paper_patterns.md` and `p3_non_routine_catalogue.md` (question TYPES only, nothing copied), `coin_note_specs.md`. The private sources (`docs/books/private_*`, `docs/sasmo/private_*`, gitignored) were used only for the similarity check (`school/p3/similarity_check.py`, section 7).

## 1. Gap analysis: the 34 Primary 3 outcome lines against what early-finisher pages can do

An early-finisher page is one printed page with a built-in check, so some verbs of the syllabus can be practised only in part. "Full" means the page asks the pupil to do what the line says; "Part" means a printed substitute is used.

| Outcome line | Pages | Coverage |
|---|---|---|
| Whole Numbers 1.1 counting in hundreds/thousands | P3-01, P3-05 | Full (counting in hundreds and thousands inside number patterns and place value) |
| Whole Numbers 1.2 notation, representations, place values | P3-01, P3-03 | Full (discs for thousands, hundreds, tens, ones; digit cards) |
| Whole Numbers 1.3 reading and writing numbers in numerals and words | P3-02 | Part: reading words and matching numerals; a pupil cannot write number words by hand and be checked |
| Whole Numbers 1.4 comparing and ordering | P3-03, P3-04 | Full |
| Whole Numbers 1.5 patterns in number sequences | P3-05 | Full (one rule, and two steps that take turns) |
| Addition and Subtraction 2.1 algorithms up to 4 digits | P3-06, P3-08 | Full (vertical sums, renaming across zeros, missing digits) |
| Addition and Subtraction 2.2 mental calculation, two 2-digit numbers | P3-07 | Part: the answer is checked, the mental method cannot be enforced on paper |
| Multiplication and Division 3.1 tables of 6, 7, 8, 9 | P3-09, P3-10, P3-12, P3-14 | Full |
| Multiplication and Division 3.2 multiplying and dividing within the tables | P3-09, P3-10, P3-12, P3-14 | Full |
| Multiplication and Division 3.3 division with remainder | P3-11 | Full (remainder, full groups, left over, least number of boxes) |
| Multiplication and Division 3.4 algorithms up to 3 digits by 1 digit | P3-13 | Full (columns for multiplying; division answered, with working left to the pupil) |
| Multiplication and Division 3.5 mental calculation within the tables | P3-09, P3-10, P3-14 | Part (as 2.2) |
| Fractions 1.1 equivalent fractions | P3-15, P3-17, P3-18 | Full (shaded figures and numerals) |
| Fractions 1.2 simplest form | P3-16 | Full (recognising simplest form); the pupil does not write a simplified fraction, which a route cannot check |
| Fractions 1.3 comparing and ordering unlike fractions (denominators up to 12) | P3-18 | Full |
| Fractions 1.4 equivalent fraction given the denominator or numerator | P3-17 | Full |
| Fractions 2.1 adding and subtracting two related fractions within one whole | P3-19 | Full (the answer's denominator is printed; the pupil writes the numerator) |
| Money 1.1 adding and subtracting money in decimal notation | P3-20, P3-40 | Full (prices, change, notes and coins drawn at real proportions) |
| Length, Mass and Volume 1.1 measuring length in km and volume in ml | P3-21, P3-23, P3-24 | Part: volume in mℓ is read from drawn beakers; **length in km is met only in word problems and conversions** (no kilometre can be measured or drawn on a page); mass dials are extra |
| Length, Mass and Volume 1.2 compound units | P3-22, P3-24, P3-25, P3-39 | Full |
| Length, Mass and Volume 1.3 converting (km and m, m and cm, kg and g, l and ml) | P3-22, P3-23, P3-24, P3-25, P3-39 | Full for km to m, kg to g and ℓ to mℓ; **m to cm only as m to cm** (never cm to m) |
| Time 2.1 seconds | P3-26 | Part: reading a stopwatch face and changing minutes and seconds; timing is not possible on paper |
| Time 2.2 start, finish or duration | P3-28, P3-29 | Full (12-hour with am and pm, and the 24-hour clock; across noon and midnight) |
| Time 2.3 24-hour clock | P3-27, P3-29 | Full (analogue and digital, to the minute) |
| Area and Perimeter 1.1 concepts | P3-30, P3-31, P3-33 | Full by recognition (area and perimeter of the same figure side by side) |
| Area and Perimeter 1.2 area in square units, cm2, m2 | P3-30, P3-32, P3-33 | Full (no conversion between cm² and m², as in the syllabus summary) |
| Area and Perimeter 1.3 perimeter of a rectilinear figure, rectangle, square | P3-31, P3-33 | Full (every side of a rectilinear figure is labelled: missing sides are Primary 4) |
| Area and Perimeter 1.4 area of a rectangle and a square | P3-32 | Full |
| Angles 1.1 concept | P3-34 | Part: recognition only (comparing a drawn angle with a right angle); making an angle by turning cannot be checked |
| Angles 1.2 right angles, greater or smaller | P3-34 | Full |
| Perpendicular and Parallel Lines 2.1 identify | P3-35 | Full |
| Perpendicular and Parallel Lines 2.2 draw | P3-36 | **Part: the drawing itself is not seen.** The pupil draws and reads off the letter where the line meets the edge of a lettered grid; the letter is the evidence |
| Bar Graphs 1.1 reading and interpreting | P3-37, P3-38 | Full (drawing a bar is not asked) |
| Bar Graphs 1.2 different scales on the axis | P3-38 | Full (a scale of 2 and a scale of 10 on one page; a scale of 5 with a number on every second line on P3-37) |

**Not covered, or only in part (for the owner):** writing number words by hand (WN 1.3), any real measuring (a ruler, a jug, a stopwatch), the idea of an angle beyond comparison with a right angle, the pupil's own drawing (P3-36, bars not drawn), mental calculation as a method (AS 2.2, MD 3.5), kilometres as a measured length (ME 1.1) and cm to m. The teacher notes say so in a paragraph "What a printed page cannot check".

**Excluded as above Primary 3** (owner decision pattern of P2-REMOVE-P3, applied one level up; checked by `validate.py` in the printed text): factors and multiples; numbers of five digits or more (10 000 is the upper bound and appears only in a topic line); rounding and estimating and the sign ≈; decimals other than money in dollars and cents; fraction and decimal conversion; mixed numbers and improper fractions; fraction of a set; adding fractions with unrelated denominators; multiplication by a 2-digit number and division of a 4-digit number; tables beyond 9; missing sides of a rectilinear figure and area of a composite figure; area of a triangle; naming angles with three letters, measuring angles in degrees and drawing angles with a protractor; line symmetry, nets and solids; line graphs, pie charts and tables as a taught skill; average; ratio; percentages; negative numbers; speed. Division with a remainder is Primary 3; so are the 24-hour clock and start, finish and duration (these were removed from P2).

## 2. The 40-page allocation

Typical order, schools vary. Page numbers P3-01 to P3-40 are the page order of the two booklets: Semester 1 holds P3-01 to P3-20 and Semester 2 holds P3-21 to P3-40, so a footer reads `S1-07 (P3-07)` in Semester 1 and `S2-07 (P3-27)` in Semester 2. The split follows the order in which Primary 3 papers are typically set (`p3_school_paper_patterns.md`, section 2: numbers, operations and tables, then fractions and money in Terms 1 and 2; measures, time, area and perimeter, angles, lines and graphs in Terms 3 and 4). Schools vary (graphs and mass often come in Term 2, fractions often again in Term 4); the notes say to hand out any page when its topic has been taught. Money Sums (P3-20) sits in Semester 1 and the money sheet P3-40 in Semester 2.

Mechanisms: K1 code word, K1 letters of the right choices (lettered choice), K1 letters of ordered cards, K6 route, K8 loop, K1 letters where drawn lines end, CBC colour by code. Stars: 1 or 2; two-star never means a new topic, only two steps, two clues or bigger numbers.

### 2a. Semester 1 (Terms 1 and 2): 10 one-star, 10 two-star

| Pos | Page | Title | Outcomes | Stars | Mechanism |
|---|---|---|---|---|---|
| S1-01 | P3-01 | Place Value | Whole Numbers 1.1, Whole Numbers 1.2 | 1 | K1 code word (6 letters) |
| S1-02 | P3-02 | Words and Numbers | Whole Numbers 1.3 | 1 | K6 route closes at FINISH through the stated number of boxes |
| S1-03 | P3-03 | Digit Cards | Whole Numbers 1.2, Whole Numbers 1.4 | 2 | K1 code word (6 letters) |
| S1-04 | P3-04 | Compare and Order | Whole Numbers 1.4 | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S1-05 | P3-05 | Number Patterns | Whole Numbers 1.1, Whole Numbers 1.5 | 2 | K1 the letter of the right choice in each row spells a word (6 letters, 2 decoy letters in each row) |
| S1-06 | P3-06 | Big Sums | Addition and Subtraction 2.1 | 1 | K1 code word (6 letters) |
| S1-07 | P3-07 | Mental Pairs | Addition and Subtraction 2.2 | 1 | K6 route closes at FINISH |
| S1-08 | P3-08 | Missing Digits | Addition and Subtraction 2.1 | 2 | K1 code word (6 letters) |
| S1-09 | P3-09 | Tables Maze | Multiplication and Division 3.1, Multiplication and Division 3.2, Multiplication and Division 3.5 | 1 | K6 route closes at FINISH |
| S1-10 | P3-10 | True or False Tables | Multiplication and Division 3.1, Multiplication and Division 3.2, Multiplication and Division 3.5 | 1 | K1 the letter of the right choice in each row spells a word (6 letters, 1 decoy letters in each row) |
| S1-11 | P3-11 | Remainders | Multiplication and Division 3.3 | 1 | K1 code word (6 letters) |
| S1-12 | P3-12 | Fact Families | Multiplication and Division 3.1, Multiplication and Division 3.2 | 2 | K8 the loop closes: every number joined by = matches |
| S1-13 | P3-13 | Multiply and Divide | Multiplication and Division 3.4 | 2 | K1 code word (6 letters) |
| S1-14 | P3-14 | Colour the Fish | Multiplication and Division 3.1, Multiplication and Division 3.2, Multiplication and Division 3.5 | 2 | CBC colour by code (tally and matching parts) |
| S1-15 | P3-15 | Equal Fractions | Fractions 1.1 | 1 | K1 the letter of the right choice in each row spells a word (6 letters, 2 decoy letters in each row) |
| S1-16 | P3-16 | Simplest Form | Fractions 1.2 | 1 | K6 route closes at FINISH |
| S1-17 | P3-17 | Fraction Gaps | Fractions 1.1, Fractions 1.4 | 2 | K1 code word (6 letters) |
| S1-18 | P3-18 | Fraction Order | Fractions 1.3, Fractions 1.1 | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S1-19 | P3-19 | Fraction Sums | Fractions 2.1 | 2 | K1 code word (6 letters) |
| S1-20 | P3-20 | Money Sums | Money 1.1 | 1 | K1 code word (6 letters) |

### 2b. Semester 2 (Terms 3 and 4): 10 one-star, 10 two-star

| Pos | Page | Title | Outcomes | Stars | Mechanism |
|---|---|---|---|---|---|
| S2-01 | P3-21 | Jugs and Beakers | Length, Mass and Volume 1.1 | 1 | K1 code word (6 letters) |
| S2-02 | P3-22 | Equal Measures | Length, Mass and Volume 1.2, Length, Mass and Volume 1.3 | 1 | K6 route closes at FINISH |
| S2-03 | P3-23 | Kilograms and Grams | Length, Mass and Volume 1.1, Length, Mass and Volume 1.3 | 1 | K1 code word (6 letters) |
| S2-04 | P3-24 | Road Trip | Length, Mass and Volume 1.1, Length, Mass and Volume 1.2, Length, Mass and Volume 1.3 | 2 | K1 code word (6 letters) |
| S2-05 | P3-25 | Order the Measures | Length, Mass and Volume 1.2, Length, Mass and Volume 1.3 | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S2-06 | P3-26 | Seconds | Time 2.1 | 1 | K1 code word (6 letters) |
| S2-07 | P3-27 | The 24-Hour Clock | Time 2.3 | 1 | K1 the letter of the right choice in each row spells a word (5 letters, 2 decoy letters in each row) |
| S2-08 | P3-28 | Start and Finish | Time 2.2 | 2 | K1 the letter of the right choice in each row spells a word (6 letters, 2 decoy letters in each row) |
| S2-09 | P3-29 | Time Detective | Time 2.2, Time 2.3 | 2 | K1 code word (6 letters) |
| S2-10 | P3-30 | Square Units | Area and Perimeter 1.1, Area and Perimeter 1.2 | 1 | K1 code word (6 letters) |
| S2-11 | P3-31 | Perimeter | Area and Perimeter 1.3, Area and Perimeter 1.1 | 1 | K1 code word (6 letters) |
| S2-12 | P3-32 | Area Sums | Area and Perimeter 1.2, Area and Perimeter 1.4 | 2 | K1 code word (6 letters) |
| S2-13 | P3-33 | Same or Different? | Area and Perimeter 1.1, Area and Perimeter 1.2, Area and Perimeter 1.3 | 2 | K1 the letter of the right choice in each row spells a word (5 letters, 2 decoy letters in each row) |
| S2-14 | P3-34 | Right Angles | Angles 1.1, Angles 1.2 | 1 | K1 the letter of the right choice in each row spells a word (5 letters, 2 decoy letters in each row) |
| S2-15 | P3-35 | Line Detective | Perpendicular and Parallel Lines 2.1 | 1 | K1 the letter of the right choice in each row spells a word (5 letters, 2 decoy letters in each row) |
| S2-16 | P3-36 | Draw the Lines | Perpendicular and Parallel Lines 2.2 | 2 | K1 the letter on the top edge where the drawn line ends spells a word (6 letters, 4 decoy letters on each edge) |
| S2-17 | P3-37 | Bar Graph Detective | Bar Graphs 1.1 | 1 | K1 code word (6 letters) |
| S2-18 | P3-38 | Different Scales | Bar Graphs 1.1, Bar Graphs 1.2 | 2 | K1 code word (6 letters) |
| S2-19 | P3-39 | Colour the House | Length, Mass and Volume 1.2, Length, Mass and Volume 1.3 | 2 | CBC colour by code (tally and matching parts) |
| S2-20 | P3-40 | Colour the Butterfly | Money 1.1 | 2 | CBC colour by code (tally and matching parts) |

Mechanism count over the 40 pages: 19 code-word pages (47.5%; P2 had 23 of 40), 8 lettered-choice pages, 3 ordering pages, 5 routes, 1 loop, 3 colour-by-code pages and 1 draw-and-read-off page (P3-36).

### 2c. Outcome coverage (generated from the built pages)

| Outcome line | Wording | Pages |
|---|---|---|
| Whole Numbers 1.1 | counting in hundreds/thousands | P3-01, P3-05 |
| Whole Numbers 1.2 | number notation, representations and place values (thousands, hundreds, tens, ones) | P3-01, P3-03 |
| Whole Numbers 1.3 | reading and writing numbers in numerals and in words | P3-02 |
| Whole Numbers 1.4 | comparing and ordering numbers | P3-03, P3-04 |
| Whole Numbers 1.5 | patterns in number sequences | P3-05 |
| Addition and Subtraction 2.1 | addition and subtraction algorithms (up to 4 digits) | P3-06, P3-08 |
| Addition and Subtraction 2.2 | mental calculation involving addition and subtraction of two 2-digit numbers | P3-07 |
| Multiplication and Division 3.1 | multiplication tables of 6, 7, 8 and 9 | P3-09, P3-10, P3-12, P3-14 |
| Multiplication and Division 3.2 | multiplying and dividing within the multiplication tables | P3-09, P3-10, P3-12, P3-14 |
| Multiplication and Division 3.3 | division with remainder | P3-11 |
| Multiplication and Division 3.4 | multiplication and division algorithms (up to 3 digits by 1 digit) | P3-13 |
| Multiplication and Division 3.5 | mental calculation involving multiplication and division within the multiplication tables | P3-09, P3-10, P3-14 |
| Fractions 1.1 | equivalent fractions | P3-15, P3-17, P3-18 |
| Fractions 1.2 | expressing a fraction in its simplest form | P3-16 |
| Fractions 1.3 | comparing and ordering unlike fractions with denominators of given fractions not exceeding 12 | P3-18 |
| Fractions 1.4 | writing the equivalent fraction of a fraction given the denominator or the numerator | P3-17 |
| Fractions 2.1 | adding and subtracting two related fractions within one whole with denominators of given fractions not exceeding 12 | P3-19 |
| Money 1.1 | adding and subtracting money in decimal notation | P3-20, P3-40 |
| Length, Mass and Volume 1.1 | measuring length in kilometres (km) and volume of liquid in millilitres (ml) | P3-21, P3-23, P3-24 |
| Length, Mass and Volume 1.2 | measuring length/mass/volume (of liquid) in compound units | P3-22, P3-24, P3-25, P3-39 |
| Length, Mass and Volume 1.3 | converting a measurement in compound units to the smaller unit, and vice versa (kilometres and metres; metres and centimetres; kilograms and grams; litres and millilitres; numbers involved should be within easy manipulation) | P3-22, P3-23, P3-24, P3-25, P3-39 |
| Time 2.1 | measuring time in seconds | P3-26 |
| Time 2.2 | finding the starting time, finishing time or duration given the other two quantities | P3-28, P3-29 |
| Time 2.3 | 24-hour clock | P3-27, P3-29 |
| Area and Perimeter 1.1 | concepts of area and perimeter of a plane figure | P3-30, P3-31, P3-33 |
| Area and Perimeter 1.2 | measuring area in square units, cm2 and m2, excluding conversion between cm2 and m2 | P3-30, P3-32, P3-33 |
| Area and Perimeter 1.3 | perimeter of rectilinear figure, rectangle, square | P3-31, P3-33 |
| Area and Perimeter 1.4 | area of rectangle/square | P3-32 |
| Angles 1.1 | concept of an angle | P3-34 |
| Angles 1.2 | right angles, angles greater than/smaller than a right angle | P3-34 |
| Perpendicular and Parallel Lines 2.1 | perpendicular and parallel lines | P3-35 |
| Perpendicular and Parallel Lines 2.2 | drawing perpendicular and parallel lines | P3-36 |
| Bar Graphs 1.1 | reading and interpreting data from bar graphs | P3-37, P3-38 |
| Bar Graphs 1.2 | using different scales on axis | P3-38 |

## 3. Ranges, wording and notation

Numbers to 10 000: four-digit numbers are written without a space (4132), a five-digit number would take a space (10 000, not used on a pupil page). Tables 6 to 9 (and the tables they link to, 2 to 5, as in a division fact); division with remainder with divisors 4 to 9; 3-digit by 1-digit multiplication and division. Fractions: stacked numerator over denominator, denominators up to 12. Money: dollar sign with two decimal places ($3.45, $0.50, $20.00); the sign for cents appears only on the coin drawings. Units: km, m, cm, kg, g, ℓ and mℓ (the script l as in the P2 booklets); cm² and m². Time: 12-hour times as 3:45 pm (no full stops), 24-hour times with four digits and h (1535 h); durations as 1 h 50 min and 280 s. Signs × and ÷. Instruction and clue sentences at most 18 words (the brief's Primary 3 reading load; the plan's own table says 12, which would not fit "Compare Figure A and Figure B" style pages as well), at most 3 instruction lines; check strip at most 18 words. Original names, numbers and scenarios: nothing copied from school papers or contest text (section 7).

## 4. Page modules and the pipeline

Copied from `school/p2` and parameterised: `gen/outcomes.py` (34 lines, page order), `gen/kit.py` (code words from a curated list of about 80 safe 5- and 6-letter words, tested against the **262 542-word** list: the 129 000-word list of P1 and P2 plus the 400 000 most frequent English words of `wordfreq`), `gen/p3kit.py` (the standard code-word page, lettered-choice page, 4-column vertical sums, number formatting), `gen/art3.py` (discs with thousands, beakers in mℓ, dials, stopwatch, unit-square figures, labelled rectilinear figures, angles, lines, bar graphs), `gen/art2.py` (clocks to the minute, coins and notes at real proportions, from P2), page modules `pages_s1a..s1d`, `pages_s2a..s2d`, `pages_cbc.py` (three colour-by-code pages from `cbc_vendor/`, a vendored copy of `school/colour_by_code` with a new `banks_p3.py`; the three small changes to the vendored copy are listed in the build report), `render.py` and `build.py`, `validate.py`.

## 5. Self-checking (the answer must be shown wrong, not shown right)

Every answer feeds a letter or a closing rule; wrong values give no letter or a decoy letter; the letters of each code word have exactly one arrangement that is a word, no single letter in another slot makes a word and no swap makes a word (tested against 262 542 words). Lettered-choice pages are tested against every other way of choosing (up to 15 624 combinations per page). Ordering pages are tested against all 719 wrong orders. Routes have exactly one route (exhaustive search from the printed text) and a stated number of boxes. The colour pages check the tally and matching marks.

## 6. Lessons carried from the P1 and P2 audits (and where they are applied)

Objects the pupil counts are at least 8 mm (unit squares are 8 mm, discs 9 mm); answer boxes at least 12 mm high; shaded fractions are black fills separated by a white line; no flat grey (the beaker hatching is a line every 3 mm and was viewed in 1-bit); code tables are at most two rows with room round every letter; every code word has exactly one real-word arrangement; the check rejects at least 95% of single wrong answers and wrong arrangements (enumerated in `validate.py`); a blank box is named in the notes as invisible to the check; no decoration looks like a mark that the check talks about (the colour pages use the vendored fixes: no eye or knob, 9 mm answer boxes); answers are unique; Primary 4 content is checked by a word and notation test; time durations are Primary 3 and are therefore allowed here; coin art is original at real proportions; front matter, footers and keys agree on the code, the star mix and the page counts; every page is solved by hand from the rendered image.

## 7. Verification per page

A generator with a seed; an independent solver that reads the printed text or drawing (bar heights against the printed axis, clock hands, beaker levels, dial needles, the squares of a figure, side labels, the arms of an angle, the end points of lines, the grid points of a drawn line) and not the generator's data; wrong-answer enumeration in `validate.py`; the word test; a key entry; a viewed render and a 1-bit photocopy simulation; every page solved by hand from the rendered image (report). `similarity_check.py` compares the printed text of all pupil pages and keys with the private sources (7-word runs, same numbers with shared words, same sentence template) and prints counts only.
