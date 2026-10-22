# SASMO Grade 6 (Primary 6) contest papers: what they test and how Level 6 prepares for it

Analysis only. No lesson file and no term plan was changed. Contest problems are not reproduced: they are referred to by paper and question number (21-9 is 2021, Question 9) with a short, deliberately generic skill tag. Question text, answers and my solution checks are in the git-ignored `docs/sasmo/private_solution_notes_g6.md`.

## 1. What was analysed, and how far to trust it

- **Seven files uploaded, five distinct papers, 125 problems.** Every file was Grade 6 (Primary 6); none had to be skipped for being a different grade. Two are duplicates:

| File | What it is | Used as |
|---|---|---|
| `a26e8045` (27 pp) | SASMO **2015** Primary 6 contest with worked solutions | 2015 paper (older format, see below) |
| `86b1a32b` (22 pp) | SASMO **2019** Grade 6 contest with worked solutions | 2019 paper |
| `d287a9b2` (25 pp) | SASMO **2020** "GEP Practice" book, questions then solutions | 2020 paper |
| `5c159912` (24 pp) | SASMO 2020 Grade 6 questions and solutions, organiser PDF | **Duplicate** of the 2020 book (same 25 problems, all 25 answers identical); used only as a cross-check |
| `b20e8906` (11 pp) | SASMO **2021** Grade 6 contest questions, phone scan, no answers | 2021 paper |
| `7b845a79` (27 pp) | "SASMO Grade 6 Mock Test 7" from a practice website: **the same 25 problems as the 2021 paper**, with an answer key and worked solutions | **Duplicate** of the 2021 questions; its key is the only worked source for 2021 |
| `7dedbe2d` (14 pp) | SASMO **2022** Grade 6 contest questions, no answers; the question text is in Chinese | 2022 paper |

- **Where the answers came from.** 2015, 2019 and 2020 have the publisher's worked solutions. 2021's key is a third party's, not the organisers'. 2022 had no key: I solved it myself. I re-derived every text-only answer by hand or with a short brute-force script (about 90 of 125). All agreed with the sources. About 12 problems depend on a figure (for example 19-15, 19-16, 20-9, 21-3, 21-5, 22-2, 22-16, 22-22): for those I followed the source where there was one and checked it against the picture where I could read it. 22-16 (count triangles) I did not count at all.
- **Ambiguities I could not settle**, so the public pages avoid depending on them: 21-6 (what counts as a button press on the calculator), 22-13 (are negative integers allowed in a run of consecutive integers), 22-24 (ordered or unordered dice), 21-24 (the bars have no scale; only solvable with the key's unit read), and 2015's Q2 has a misprinted option list.
- **Format.** 2019 to 2022: 25 questions, Section A is Q1 to 15 (five options, A to E, E is "none of the above", 2 marks, minus 1 for a wrong answer; 75 problems) and Section B is Q16 to 25 (whole-number answer, 4 marks, no penalty; 50 problems). 2015: same split, 90 minutes, starting score 15, "show detailed working", minimum stay 1 h 15 min. The 2015 booklet and the practice-site copy of 2021 both give 90 minutes and no calculator.
- **Categories are my single-coder judgement**; each problem is filed under its main skill only, so counts are indicative. **Five papers from five different years is a small sample**, and 2015 was set to a different style (older, with more factor and divisibility items: 8 of its 25). A type with 1 to 3 problems is "occasionally seen", not "tested every year".
- **This is Grade 6 only.** Level 6 in the term plan is ages 11 to 13, which may sit across SASMO Grades 6 and 7; no Grade 7 file was supplied. The plan's open question 6 (which SASMO grades match this level) is still open.
- **The contest is not the Level 6 syllabus.** The holiday course is an enrichment and coding bridge (sequences, primes, negatives, algebra machines, counting, probability, polygons, mod, data). The contest is mostly P6 syllabus content (ratio, percent, circles, average, rate) plus Primary-school heuristics. The term plan (Terms 2 to 4) takes on much of that. Whether to close the remaining gaps is the owner's call.

## 2. Catalogue

Band is how hard the item reads as presented (my judgement from position, marks and steps): E = one step or known fact, M = two or three steps with a known method, H = needs a case split, an insight or a long careful count. **Holiday** = how well the 10-lesson holiday course (`p6/content/l1.js` to `l10.js`) prepares the item today: P = prepared, Part = the method is taught but the contest twist is not, Gap = nothing. **Term plan** = the same judgement for the 36-lesson plan (`docs/terms/level_6_year_plan.md`: Term 1 = holiday L1 to L8 plus the trimmed L10 as lesson 9; Terms 2 to 4 = lessons 10 to 36), with the lessons that would carry it. The plan lessons are not written yet, so this is what the plan lists, not what a built lesson teaches. L-numbers are plan lesson numbers.


### 2015 paper

| ID | Sec | Skill tag | Thinking move | Band | Holiday | Term plan |
|---|---|---|---|---|---|---|
| 15-1 | A | Tens and ones in words, then reverse | Words to numbers | E | P | P: primary level |
| 15-2 | A | Triangle cut into a square (equal area) | Same area, solve for the base | M | Part | Part: L14, L18 |
| 15-3 | A | Two-number operator | Find the rule from four examples | M | Part | Part: L4, L19 |
| 15-4 | A | Last digit of a power of 6 | Last digit repeats | E | Part | Part: L8, L24 |
| 15-5 | A | Sequence one more than the squares | Subtract 1, see squares | E | P | P: L1, L24 |
| 15-6 | A | Previous perfect-square year | Bracket between squares | E | P | P: L24 |
| 15-7 | A | Five-digit number with one missing digit, divisible by 6 | Test for 2 and for 3 | E | Gap | Gap |
| 15-8 | A | Rectangles in a 4 by 4 grid | Count by size, or by pairs of lines | M | Part | Part: L31 |
| 15-9 | A | Rounded height, lowest possible | Boundaries of rounding | E | Gap | Gap |
| 15-10 | A | Continued fraction | Work from the bottom up | M | Part | Part: L11 |
| 15-11 | A | 4-digit palindromes | Choose the free digits | M | P | P: L5, L31 |
| 15-12 | A | Sweets shared equally in four different ways | LCM | E | P | P: L2, L25 |
| 15-13 | A | Three different factors with a year number as product | Prime factors, group them | M | P | P: L2, L25 |
| 15-14 | A | Small cards cut from a large sheet | Area bound, then try cut patterns | H | Gap | Gap |
| 15-15 | A | Train through a tunnel | Distance is tunnel plus train | M | Part | Part: L13 |
| 15-16 | B | Two numbers with a given product, neither a multiple of 10 | Keep the 2s and 5s apart | M | P | P: L2 |
| 15-17 | B | Zeros at the end of a factorial | Count pairs of 2 and 5 | M | Part | Part: L2, L25 |
| 15-18 | B | Five tyres share the wear of a trip | Total tyre-distance shared | M | Gap | Gap |
| 15-19 | B | Four passers-by, only one tells the truth | Test each case | H | Part | Part: L33 |
| 15-20 | B | Rectangle cut in four: shaded area | Join the shaded pieces into one strip | M | Part | Part: L18 |
| 15-21 | B | Cuboid built from a year-number of cubes | Prime factors give the sides | M | P | P: L2, L15 |
| 15-22 | B | Remainders on division by 10 | Work with remainders only | M | P | P: L8 |
| 15-23 | B | Far term of a sequence where n repeats n times | Triangular numbers bracket it | H | Part | Part: L32 |
| 15-24 | B | Chairs: fractions of a total set out in rows | Whole-number fractions force divisibility | H | Part | Part: L11, L25 |
| 15-25 | B | Remainder of a large power of 3 on division by 4 | Cycle of remainders | M | P | P: L8, L24 |

### 2019 paper

| ID | Sec | Skill tag | Thinking move | Band | Holiday | Term plan |
|---|---|---|---|---|---|---|
| 19-1 | A | Digit sum of a product of two 3-digit numbers | Rewrite as 231 times 999 | M | Part | Part: L19 |
| 19-2 | A | Two voucher types, students with both | Add, compare with the total | E | Part | Part: L33 |
| 19-3 | A | Edges of a dodecahedron | Each edge is shared by two faces | M | Gap | Gap |
| 19-4 | A | Three books in a row, two next to each other | List every order | E | P | P: L5, L31 |
| 19-5 | A | Percent of cards given away | Original = given + left | E | P | P: L12 |
| 19-6 | A | Angle in a square and an equilateral triangle | Isosceles triangle, chain the angles | M | P | P: L16 |
| 19-7 | A | Four players, average and half | Units | M | P | P: L10 |
| 19-8 | A | Three rotations of a 3-digit number, even and divisible by 9 | Digit sum is a multiple of 9, all even | M | Gap | Gap |
| 19-9 | A | Which statement about 1 to 50 is false | Check each by counting | M | Part | Part: L5 |
| 19-10 | A | Pipe filling a leaking tank | Fraction of the tank per hour | M | Gap | Part: L13 |
| 19-11 | A | Day of the week 70 days on | Remainder after 7 | E | P | P: L8 |
| 19-12 | A | Hands of a clock overlap after 6 p.m. | Degrees per minute for each hand | H | Gap | Gap |
| 19-13 | A | Four athletes, exactly 3 truthful | Test who lied | M | Part | Part: L33 |
| 19-14 | A | Factorial that is a multiple of a given number | Largest prime factor | M | Part | Part: L2, L25 |
| 19-15 | A | Missing figure in a 3 by 3 of triangles | Combine two cells by a rule | M | Gap | Gap |
| 19-16 | B | Triangles in a figure | Count by size | M | Part | Part: L31 |
| 19-17 | B | Sum of halves, quarters, eighths ... | Each partial sum is one piece short of 1 | M | Part | Part: L11, L24 |
| 19-18 | B | Phone hours falling by the same percent | Repeated percentage | M | Part | Part: L12 |
| 19-19 | B | Sequence from days in each month | Notice month lengths | M | Part | Part: L1, L8 |
| 19-20 | B | Four people, three ratios | Make the totals equal | H | Part | P: L10 |
| 19-21 | B | 30 numbers, any 11 have an even product | Pigeonhole on the odd numbers, then parity | H | Gap | Part: L34 |
| 19-22 | B | Two runners meet again at A | LCM of the lap times | M | Part | Part: L13, L25 |
| 19-23 | B | Shaded part of two overlapping squares | Add triangles, take away triangles | H | Gap | Gap |
| 19-24 | B | Word addition, sum of four letters | Leading digit, then carries | H | Gap | Gap |
| 19-25 | B | Digit counting over every date of a year | Count by place | H | Part | Part: L5, L31 |

### 2020 paper

| ID | Sec | Skill tag | Thinking move | Band | Holiday | Term plan |
|---|---|---|---|---|---|---|
| 20-1 | A | Square minus the product of its neighbours | Difference of squares | E | Gap | Part: L19 |
| 20-2 | A | Sequence whose gaps are squares | Add 1, 4, 9, ... (squares) | M | Part | Part: L1, L32 |
| 20-3 | A | Two pack sizes: largest impossible total | Show every total from 12 on | M | Gap | Gap |
| 20-4 | A | Circle with four semicircles | Subtract the unshaded area | M | Gap | P: L14 |
| 20-5 | A | Rectangular tiles on a rectangular floor | Area bound, then build it | H | Gap | Gap |
| 20-6 | A | Bar chart, percent who chose C | Count gridline units | E | Part | P: L28 |
| 20-7 | A | Two diggers, different holes | Volume per hour, add the rates | M | Gap | Part: L13 |
| 20-8 | A | Five-digit number with two missing digits, divisible by 45 | Tests for 5 and for 9 | M | Gap | Gap |
| 20-9 | A | Cube whose top view is a clock | Eliminate feature by feature | M | Gap | Part: L15 |
| 20-10 | A | Chips eaten, ratio before and after | Make the totals equal | M | Part | P: L10, L12 |
| 20-11 | A | Clock hand tips travel in 24 hours | Circumference, count the turns | M | Gap | P: L14 |
| 20-12 | A | Zeros at the end of a sum of two factorials | Factor out 8!, count 2s and 5s | M | Part | Part: L25 |
| 20-13 | A | Four rectangles in two layouts | Perimeter by sliding sides | M | Part | Part: L18 |
| 20-14 | A | Five children, grade and school | Case analysis | M | Part | Part: L33 |
| 20-15 | A | Hour hand closest to minute hand | Degrees per minute for each hand | H | Gap | Gap |
| 20-16 | B | Last digit of a product of powers | Pair into 6s | M | Part | Part: L24 |
| 20-17 | B | Triangles in a figure | Count by size | H | Part | Part: L31 |
| 20-18 | B | Sum of fractions with products in the denominators | Telescoping | H | Gap | Part: L11 |
| 20-19 | B | Fruit ratios, 20 percent oranges | Make the totals equal | M | Part | P: L10 |
| 20-20 | B | Digits used for page numbers | Count digits by length | M | P | P: L5 |
| 20-21 | B | Two candles burning at different rates | Rate of burning | M | Gap | Part: L13 |
| 20-22 | B | Election, fewest more votes to be sure | Worst case, rest to the runner-up | M | Part | Part: L34 |
| 20-23 | B | Right-angled triangle BDC area | Similar triangles | H | Gap | Gap |
| 20-24 | B | 4-digit number times 9 is its reverse | Leading digit, then carries | M | Gap | Gap |
| 20-25 | B | Sum of nine 3-digit numbers round a circle | Each digit once in each place | M | Part | Part: L5 |

### 2021 paper

| ID | Sec | Skill tag | Thinking move | Band | Holiday | Term plan |
|---|---|---|---|---|---|---|
| 21-1 | A | Decimals and fractions with 0.14 in common | Factor it out | E | Part | Part: L19 |
| 21-2 | A | Every three adjacent squares have the same sum | Period of three | E | Part | Part: L1 |
| 21-3 | A | Which block figure is a rotation | Count blocks by layer | M | Gap | Part: L15 |
| 21-4 | A | Smallest of five fraction forms | Convert all to decimals | E | Part | P: L11 |
| 21-5 | A | Dice in a line, touching faces sum to 8 | Chain the face pairs | H | Gap | Gap |
| 21-6 | A | Calculator presses to get 1 from 2021 | Make 0, then add 1 | M | Gap | Gap |
| 21-7 | A | 12 equal rectangles, one side 36 cm | Length is 4 times width | M | Part | Part: L10, L18 |
| 21-8 | A | Eight digits in a nested fraction, largest value | Biggest on top, smallest below | H | Gap | Part: L11 |
| 21-9 | A | Ten different digits, smallest multiple of 45 | Tests for 5 and 9, smallest first | M | Gap | Gap |
| 21-10 | A | Stamps in bundles, best income | Price per stamp, then fill | H | Part | Part: L13 |
| 21-11 | A | Cake in 10 pieces, 250 g apart | Steps from the lightest | M | Part | Part: L1, L28 |
| 21-12 | A | Train and truck pass in opposite directions | Combined speed | M | Gap | Part: L13 |
| 21-13 | A | Average of four fractions, flip one | Only one term changes | H | Part | Part: L11, L28 |
| 21-14 | A | Salt solutions mixed | Salt over total | M | Gap | Part: L12 |
| 21-15 | A | Digit with 3 times as many to its right | Count digits by length | H | P | P: L5 |
| 21-16 | B | Last two digits of a product | Use the last two digits only | M | P | P: L8 |
| 21-17 | B | Two-row pattern, sum of the 100th column | Two interleaved rules | M | P | P: L1 |
| 21-18 | B | Two isosceles triangles | Angle chase | M | P | P: L16 |
| 21-19 | B | Fewest picks so one divides another | Pigeonhole by odd part | H | Gap | Part: L34 |
| 21-20 | B | Count the multiples of 3 among the digits | Spot the rule | M | Part | Part: L1 |
| 21-21 | B | Two children, cards, fractions before and after | Make the totals equal | M | P | P: L10 |
| 21-22 | B | Number read upside down is bigger by a given amount | Place values and flips | M | Gap | Gap |
| 21-23 | B | Word subtraction, smallest value | Rewrite as addition | H | Gap | Gap |
| 21-24 | B | Bar graph, rectangles with equal perimeters | List rectangles by area | H | Gap | Gap |
| 21-25 | B | Remainder when dividing by the digit sum | Biggest digit sums first | H | Gap | Gap |

### 2022 paper

| ID | Sec | Skill tag | Thinking move | Band | Holiday | Term plan |
|---|---|---|---|---|---|---|
| 22-1 | A | Fraction of two long sums | Compute both parts | E | P | P: primary level |
| 22-2 | A | Cube pyramid, exactly three painted faces | Count by layer | H | Gap | Part: L15 |
| 22-3 | A | Square with a shaded band | Parallelogram area | M | Gap | Part: L18 |
| 22-4 | A | Sequence with a times-and-subtract rule | Rule from the previous term | M | Part | Part: L32 |
| 22-5 | A | Spending percentages, find the whole | Percent of the whole | E | Part | P: L12 |
| 22-6 | A | Number pyramid with blank cells | Fill from the known cells | M | Gap | Gap |
| 22-7 | A | 10 classrooms, 10 students leave each | Equation | M | Part | P: L4, L20 |
| 22-8 | A | Two numbers: given difference and quotient | Bar model or equation | M | Part | P: L10, L20 |
| 22-9 | A | Digit sum of a number times a repunit | Small cases first | H | Part | Part: L1 |
| 22-10 | A | Animal symbol equations | Combine the equations | M | Part | P: L4, L20 |
| 22-11 | A | Three consecutive integers, product given | Estimate by cube root | M | Part | Part: L24 |
| 22-12 | A | 4-digit numbers with a given digit sum, below 2000 | List by first digit | M | P | P: L5 |
| 22-13 | A | Number as a sum of consecutive integers | Count by number of terms | M | Gap | Gap |
| 22-14 | A | Fraction written as a continued fraction | Split and flip | M | Part | Part: L11 |
| 22-15 | A | Five gifts, nobody gets her own | Count rearrangements | H | Gap | Part: L31 |
| 22-16 | B | Triangles in a figure | Count by size | H | Part | Part: L31 |
| 22-17 | B | Bar chart, average, 40 percent | Gridline units | M | Part | P: L28 |
| 22-18 | B | Marble piles, a move repeated 2000 times | Find the cycle | H | Gap | Part: L34 |
| 22-19 | B | Toy, book, cakes: fractions of what is left | Work backwards | M | Part | P: L11, L12 |
| 22-20 | B | Two cyclists meet on a road | Combined speed | M | Gap | Part: L13 |
| 22-21 | B | 4-digit number times a digit | Last digit, then size | M | Gap | Gap |
| 22-22 | B | Diagonal in five equal parts, shaded area | Triangles with the same height | H | Gap | Gap |
| 22-23 | B | Sum of ages now and in 6 years | Equation on totals | M | Part | P: L10, L20 |
| 22-24 | B | Two dice, higher number is odd | List the 36 outcomes | M | P | P: L6 |
| 22-25 | B | Longest digit string, no adjacent pair repeated | Count the pairs available | H | Gap | Gap |

Totals: 125 problems; band E 18, M 76, H 31. Holiday status: P 24, Part 54, Gap 47. Term-plan status: P 38, Part 59, Gap 28. By section: Section A (75 problems) holiday P 14, Part 32, Gap 29; Section B (50) P 10, Part 22, Gap 18.

## 3. Frequency by type

| Type | All | A | B | 2015 | 2019 | 2020 | 2021 | 2022 | Where it appears |
|---|---|---|---|---|---|---|---|---|---|
| Divisibility, factors, multiples, LCM, remainders | 14 | 9 | 5 | 8 | 2 | 1 | 2 | 1 | 15-6, 15-7, 15-12, 15-13, 15-16, 15-21, 15-22, 15-24, 19-8, 19-14, 20-8, 21-9, 21-25, 22-11 |
| Sequences, patterns, periodic rules | 11 | 7 | 4 | 2 | 2 | 1 | 4 | 2 | 15-5, 15-23, 19-11, 19-19, 20-2, 21-2, 21-11, 21-17, 21-20, 22-4, 22-13 |
| Ratio, percent and fraction word problems | 10 | 5 | 5 | 0 | 4 | 2 | 2 | 2 | 19-5, 19-7, 19-18, 19-20, 20-10, 20-19, 21-14, 21-21, 22-5, 22-19 |
| Logic, worst case, pigeonhole, optimising | 10 | 4 | 6 | 1 | 2 | 3 | 2 | 2 | 15-19, 19-13, 19-21, 20-3, 20-14, 20-22, 21-6, 21-19, 22-18, 22-25 |
| Area, perimeter, circles, dissection | 10 | 6 | 4 | 2 | 1 | 3 | 2 | 2 | 15-2, 15-20, 19-23, 20-4, 20-11, 20-13, 21-7, 21-24, 22-3, 22-22 |
| Rate, speed and work | 9 | 5 | 4 | 2 | 2 | 2 | 2 | 1 | 15-15, 15-18, 19-10, 19-22, 20-7, 20-21, 21-10, 21-12, 22-20 |
| Digit counting and place value | 8 | 5 | 3 | 1 | 2 | 2 | 1 | 2 | 15-11, 19-9, 19-25, 20-20, 20-25, 21-15, 22-9, 22-12 |
| Computation, identities, approximation | 7 | 7 | 0 | 2 | 1 | 1 | 2 | 1 | 15-1, 15-9, 19-1, 20-1, 21-1, 21-4, 22-1 |
| Counting figures, arrangements, outcomes | 7 | 3 | 4 | 1 | 2 | 1 | 0 | 3 | 15-8, 19-4, 19-16, 20-17, 22-15, 22-16, 22-24 |
| Fractions: nested, telescoping, optimising | 6 | 4 | 2 | 1 | 1 | 1 | 2 | 1 | 15-10, 19-17, 20-18, 21-8, 21-13, 22-14 |
| Last digits, powers, trailing zeros | 6 | 2 | 4 | 3 | 0 | 2 | 1 | 0 | 15-4, 15-17, 15-25, 20-12, 20-16, 21-16 |
| Algebra: equations, symbol and operator puzzles | 5 | 4 | 1 | 1 | 0 | 0 | 0 | 4 | 15-3, 22-7, 22-8, 22-10, 22-23 |
| Cryptarithms and digit puzzles | 5 | 0 | 5 | 0 | 1 | 1 | 2 | 1 | 19-24, 20-24, 21-22, 21-23, 22-21 |
| Spatial: views, rotation, solids, painted cubes | 5 | 5 | 0 | 0 | 1 | 1 | 2 | 1 | 19-3, 20-9, 21-3, 21-5, 22-2 |
| Angles, clock hands, triangle geometry | 5 | 3 | 2 | 0 | 2 | 2 | 1 | 0 | 19-6, 19-12, 20-15, 20-23, 21-18 |
| Data, graphs, Venn counting | 3 | 2 | 1 | 0 | 1 | 1 | 0 | 1 | 19-2, 20-6, 22-17 |
| Packing and tiling bounds | 2 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 15-14, 20-5 |
| Grid and picture-rule puzzles | 2 | 2 | 0 | 0 | 1 | 0 | 0 | 1 | 19-15, 22-6 |

What stands out:
- **The big five are divisibility and factors (14), sequences and periodic rules (11), and then ratio and percent, logic and worst case, and area and circles (10 each).** Rate and speed (9) is next, and it appears in **every one of the five papers**, including 2021 and 2022 after speed left the MOE primary syllabus. That is direct evidence for keeping lesson 13 as an enrichment lesson.
- **Cryptarithms: 5 problems, all Section B (4 marks each), one in every paper since 2019 and two in 2021** (19-24, 20-24, 21-22, 21-23, 22-21). Nothing in Level 6 or its plan teaches them. Level 3 has a whole lesson on them (L2 Cryptarithm Crackers), so the idea is already in the family of programs, just not at this level.
- **Divisibility tests: 5 problems in 4 papers** (15-7 for 6, 19-8 for 9, 20-8 for 45, 21-9 for 45, 21-25 digit sums). Level 6 teaches primes, factors, LCM and remainders well (L2, L8) but never the digit tests.
- **Counting figures by size (triangles, rectangles): 4 problems, 3 in the last four papers** (15-8, 19-16, 20-17, 22-16).
- **Worst case, pigeonhole and "largest impossible total": 4 to 5 problems in the last four papers** (19-21, 20-3, 20-22, 21-19, 22-18). They are 2 to 4 marks of reasoning that no lesson in Terms 1 to 3 names.
- **Section A is mostly short-reach items; Section B is where reasoning lives.** All 5 spatial items, all 7 computation items, all 2 packing items and all 2 grid-rule items are in Section A; all 5 cryptarithms are in Section B. 29 of the 47 holiday Gap items are in Section A, so a child who has never met them loses easy 2-mark items to a minus-1 penalty.
- **Repeats across years (same skill, new numbers):** triangle counting (19-16, 20-17, 22-16), divisibility by 9 or 45 (19-8, 20-8, 21-9), cryptarithm (19-24, 20-24, 22-21), last-digit or remainder cycles (15-4, 15-25, 20-16, 21-16), a before-and-after ratio (20-10, 21-21), nested fractions (15-10, 22-14), clock hands (19-12, 20-15), digit counting for page numbers (20-20, 21-15). These are the best candidates for contest-oriented practice.
- **Number size.** Answers go up to 4 digits (Section B grid), computation is mostly mental with clever structure (difference of squares, factoring 0.14, 231 x 999), and several items are decimals or fractions with an odd denominator (13, 17, 91). The Level 6 SPEC allows all of this; no multiplier limit applies.
- **Reading load is light**; about 12 of 125 depend on a drawing.
- **2015 looks different from 2019 to 2022.** It has no cryptarithm, no ratio-of-parts item and no spatial item, but 8 of 25 on divisibility and factors. Do not treat the 2015 mix as the current style.

## 4. How Level 6 maps to it

Level 6 holiday lessons: L1 Code the Pattern; L2 Prime Hunters; L3 Below Zero; L4 Algebra Machines; L5 Every Possible Way; L6 Fair or Unfair?; L7 Turtle Geometry; L8 Secret Codes; L9 Data Detectives; L10 Showcase Challenge. Tiers in each question bank: Start here = Core (C1 to C6), Think harder = Stretch (TH1 to TH8, of which TH1 to TH4 print on the workbook), Go further = Challenge (GF1 to GF9, of which GF7 to GF9 print). Plan lessons L10 to L36 are from the term plan (Term 2 = L10 to L18, Term 3 = L19 to L27, Term 4 = L28 to L36).

| Type | Holiday prepares it | Term plan adds | Go further would need | Verdict |
|---|---|---|---|---|
| Computation, identities, approximation | L4 machines only; no mental-strategy routine | L19 expand with area models | The square-minus-neighbours identity, "factor out the common decimal", rounding intervals | **Partial**; low cost: a recurring 5-minute "shortcut" opener |
| Fractions: nested, telescoping, optimising | Nothing | L11: fractions of fractions; telescoping *product* (G tier) | Unfolding a continued fraction, telescoping *sums* 1/(n(n+k)), halving sums, "biggest value from digit boxes" | **Partial**; 6 items, 4 in Section A |
| Ratio, percent, fraction word problems | None in the holiday course (L9 is mean only) | L10 ratio and before-after; L12 percent change and find the whole; the strongest match once Term 2 exists | Chains of three or four ratios, repeated percentage change, mixtures | **Prepared by the plan, not by the holiday**; 10 items |
| Algebra: equations, symbol and operator puzzles | L4 machines run backwards, guess and check; GF items with two machines | L19 to L21 | Equations from word totals (ages), two-input operators, balance of symbols | **Prepared**; light extension |
| Rate, speed, work | Nothing | L13 Rate and Speed Stories (speed kept as enrichment) | Combined rate, trains of given length through tunnels, opposite and same direction, pipes and leaks, equal sharing of a total distance | **Partial**; 9 items in all 5 papers, so keep L13 and widen it |
| Divisibility, factors, multiples, remainders | L2 factors, primes, prime factorisation (GF3: smallest number divisible by 2 to 6; GF8 eggs); L8 remainders and mod (GF4: remainders 2, 3, 4) | L25 HCF and LCM, Euclid in code | **Digit-sum tests for 3 and 9, "divisible by 45 = 5 and 9", test for 4, 6 and 12**, solving digit-box puzzles, LCM of lap times | **Real gap** for the tests (5 items); **Prepared** for factors, LCM, primes (the rest) |
| Last digits, powers, trailing zeros | L8 mod arithmetic and cycles (365 days, 100th letter); L2 prime factorisation | L24 Powers and Roots (G: last digit of powers); L25 | Trailing zeros by counting 2s and 5s, last two digits, remainders of powers | **Partial**; 6 items; cheap to close |
| Sequences, patterns, periodic rules | L1 is built for this (nth term, 100th term, two sequences that meet), L8 cycles | L32 recursion and triangular numbers | "Gaps are the squares", rule from the previous term (times 3 minus 1), a sequence where n repeats n times, sums of consecutive integers | **Prepared**; small extension |
| Counting: figures, arrangements, outcomes | L5: multiplication rule, handshakes, squares in a grid (3 by 3, 4 by 4), rectangles in a strip, listing in order; L6 all 36 outcomes | L31 Counting with Constraints | Triangles and rectangles by size in a drawing; rectangles in a grid by pairs of lines; rearrangements where nobody keeps their own | **Partial**; 7 items |
| Digit counting, place value | L5 GF3 (pages 1 to 120), 3-digit numbers by condition | L5 and L31 | Nothing major; sum of numbers around a circle (each digit once in each place) | **Prepared** |
| Cryptarithms and digit puzzles | **Nothing** | **Nothing** | A whole short strand: leading digit first, then carries; brute force in code (nested loops) | **Real gap**; 5 items, all Section B |
| Logic, worst case, pigeonhole, optimising | L5 GF: none; L9 none; no named logic lesson | L33 logic and proof; L34 pigeonhole and invariants | Worst-case reasoning ("rest of the votes to the runner-up"), "largest total you cannot make", cycles in a repeated move, liar puzzles | **Partial**; 10 items and the plan names only pigeonhole and invariants |
| Spatial: views, rotation, solids, painted cubes | Nothing | L15 Volume and Nets (painted-cube counts in G) | Rotating a block figure, top views, dice faces that touch, edges and faces of a solid, painted cubes in a stack | **Partial to Gap**; 5 items, all Section A |
| Area, perimeter, circles, dissection | Nothing (L7 is angles only) | L14 Circles and Pi, L18 Scale Model Studio | Triangles with the same base and height, rectangle dissections, perimeter by sliding sides, shaded bands | **Partial**; 10 items |
| Packing and tiling bounds | Nothing | Nothing | "Area bound, then build it", why the bound is sometimes not reached | **Gap**; 2 items (15-14, 20-5) |
| Angles, clock hands, triangle geometry | L7 turtle angles, polygon turns | L16 Angle Chasing | Hand speeds on a clock (6 degrees and 0.5 degrees per minute), similar triangles | **Partial**; angle chasing is covered, clock hands and similar triangles are not (3 items) |
| Data, graphs, Venn counting | L9 mean, list code | L28 Statistics That Mislead | Bar charts whose axis has no numbers (read gridline units); two-set counting | **Prepared** |
| Grid and picture-rule puzzles | Nothing | Nothing | One warm-up routine: name each feature, find its rule | **Gap**; 2 items, low priority |

### Summary of status across the 125 problems

- **Prepared (P): 24 holiday, 38 plan.** Mostly sequences, digit counting, place value, factors and LCM, remainders, ratio before-after, algebra with letters and the two P6 data items.
- **Partly prepared (Part): 54 holiday, 59 plan.** The method is taught, the contest twist is not.
- **Gap: 47 holiday, 28 plan.** The 28 items with no plan coverage at all: 15-7, 15-9, 15-14, 15-18, 19-3, 19-8, 19-12, 19-15, 19-23, 19-24, 20-3, 20-5, 20-8, 20-15, 20-23, 20-24, 21-5, 21-6, 21-9, 21-22, 21-23, 21-24, 21-25, 22-6, 22-13, 22-21, 22-22, 22-25. Five are cryptarithms, five are divisibility tests, three are clock hands or similar triangles, three are area dissections (19-23, 21-24, 22-22), two are packing, two are spatial, two are grid-rule puzzles, three are worst-case or optimising.
- **19 items go from holiday Gap to plan Part or P** only because Terms 2 to 4 exist on paper (rate, circles, same-total ratio, percent mixtures, nested fractions, pigeonhole, rearrangements). If those lessons are cut or shortened, those items revert to Gap.

## 5. Biggest gaps, in the order I would weigh them

1. **Digit tools: divisibility tests and the cryptarithm.** 10 problems (5 tests and 5 cryptarithms), at least one in every paper; the five cryptarithms are all 4-mark Section B items. Short teaching (digit sums for 3 and 9, "45 means 5 and 9", leading digit then carries) would turn these from blanks into scorable items. It also fits the program's coding bridge: a cryptarithm and a "divisible by 45" filter are both short nested-loop brute-force programs.
2. **Worst case, pigeonhole and "largest impossible total" (10 logic and optimising items; 5 of them in 2019 to 2022, at 2 to 4 marks).** The plan has one lesson (L34) with pigeonhole and invariants. Worst-case reasoning and the 3-and-7-pack problem are not named there.
3. **Rate, speed and work (9 items).** Plan has one lesson (L13). Combined rates, trains with length, opposite directions and equal sharing are the contest forms.
4. **Counting figures by size and rearrangements (7 items).** L31 would carry this; the holiday has squares and a strip of rectangles only.
5. **Nested fractions and telescoping sums (6 items).** L11's telescoping product does not transfer without a sum version and a continued-fraction step.
6. **Spatial (5 items) and clock hands (2 items), and area dissections (3 items).** All three are small and cheap, but each needs a drawing or a physical object.
7. **Last digits and trailing zeros (6 items).** Prepared for the cycle idea (L8, L24 GF); not for trailing zeros of a factorial or last two digits.
8. **Packing bounds (2 items), grid-rule puzzles (2 items), rounding intervals (1 item), consecutive sums (1 item), equal sharing of a total (15-18).** Single occurrences; evidence is too thin to build anything.

## 6. Where Think harder and Go further need extension

- **Think harder is generally well pitched** for the contest's M-band items in L1, L2, L4, L5, L8 and L10; and Term 2's L10, L12 and L14 will carry the ratio, percent and circle items. A child who finishes the printed Think harder pages would find most E and M items comfortable.
- **Go further does not reach the contest's H band in the gap types.** There is no Go further item on digit tests, cryptarithms, worst case, nested fractions, trains, spatial or packing, so the draft problems in `g6_original_problems_draft.md` are written as Go further and flagged as draft. Start here and Think harder are also empty for these, so the owner will need to decide whether to add an easier step first.
- **Go further asks "make up your own", "find all" and "is it always true?"**; the contest never does. That is a program choice, not a gap.
- **There is no timed practice and no exam-technique teaching** (option elimination with minus-1 marking, "none of the above" answers, whole-number answer grids). The program's SPEC rules this out for post-PSLE children, so it is not a gap to close here.

## 7. Honest notes where evidence is thin

- Five papers, 125 problems, one coder. One occurrence of a type is not a trend. The 2015 paper is a different era.
- **Grade 6 only.** The level covers ages 11 to 13. Grade 7 papers may weigh the types differently, and there may be a Grade 5 and 7 analysis by other people; none was used here.
- Source quality varies: 2015, 2019 and 2020 have publisher solutions; 2021's key came from a third party; 2022 had no key and I solved it myself. About 12 items depend on a figure; a few need a reading call I could not settle (listed in section 1).
- **Which lessons the holiday course really contains.** I read the lesson, qbank and workbook text in `p6/content/l1.js` to `l10.js` and `p6/SPEC.md`, the earlier audits (`audit_p6.md`, `gifted_p6.md`, `close_gaps_p6.md`) and the term plan. I searched for keywords (divisible, digit sum, last digit, zeros, factorial, pigeon, cryptarithm, upside, speed, solution, mixture, tiling, triangles, rectangles) and found no match for the gap types above except as listed. The slides, scripts, tutor guide and Weekly Dose were not re-read item by item, so an item that exists only there would be missed.
- **The term plan's lessons are not written.** "Term plan Part or P" means the plan lists the topic, not that a built lesson would teach the contest move.
- **No contest counterpart.** The contest has almost nothing on L3 negative numbers, L7 turtle and polygon angles, L17 symmetry and transformations, L21 to L23 inequalities, coordinates and straight-line graphs, L26 binary, L29 scatter and L30 tree diagrams (probability appeared once, 22-24). The contest evidence says nothing about these lessons either way. They are enrichment by design.
- Exam-only skills (five-choice paper, negative marking, answers in a four-digit grid) are not maths and not trained.
- No lesson, slide, workbook, question-bank or term-plan file was changed.

## 8. Term-plan lessons the evidence says to change (plan not edited)

| Lesson | Change suggested by the evidence |
|---|---|
| L2 Prime Hunters (Term 1) | Add digit-sum tests for 3 and 9 (and "5 and 9 means 45") as a Think harder or Go further step; a "filter with mod" program fits. |
| L11 Fractions of Fractions | Widen the Go further tier: telescoping *sums*, unfolding a continued fraction, "biggest value from digit boxes". |
| L13 Rate and Speed Stories | Keep speed as enrichment (rate appears in all five papers). Add combined rate (pipe and leak, two workers), trains with length, opposite and same direction, equal sharing of a total distance. |
| L15 Volume and Nets | Add a "seeing in 3D" step: rotate and match block figures, top views, dice faces that touch, edges of a solid. |
| L16 Angle Chasing | Add clock-hand angles (6 degrees and 0.5 degrees per minute) as a warm-up. |
| L18 Scale Model Studio (or L14) | Add same-base-same-height triangle area and rectangle dissections. |
| L19 Letters and Brackets | Add the "square minus its neighbours" identity and "factor out the common number" as shortcut items. |
| L24 Powers and Roots | Promote "last digit of powers" from Go further to Think harder; add last two digits. |
| L25 Factors, HCF and LCM | Add trailing zeros of a factorial (count 2s and 5s), LCM of lap times, and the tests from L2. |
| L31 Counting with Constraints | Add counting triangles and rectangles by size and rearrangements with nobody in their own place. |
| L33 Logic and Proof or L34 Olympiad-Style Workshop | Add cryptarithms (leading digit, carries, brute-force check) and worst-case counting ("rest of the votes"), unattainable totals with two pack sizes, a repeated-move cycle. L34 currently names only pigeonhole and invariants. |
| L28 Statistics That Mislead | Add a bar chart with no scale numbers (read gridline units). |

Lessons with no suggested change: L1, L4, L5, L8 (they match the contest's sequences, algebra, counting and remainder items already); L10, L12, L14 (ratio, percent and circles are well matched in the plan).
