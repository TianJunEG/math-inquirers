# SASMO Grade 5 (Primary 5) contest papers: what they test and how Level 5 prepares for it

Analysis only. No lesson or term-plan file was changed. Contest problems are not reproduced: they are referred to by paper and question number (19-12 is 2019, Question 12) with a short skill tag. Question text, answers and my solution checks are in the git-ignored `docs/sasmo/private_solution_notes_g5.md`.

## 1. What was analysed, and how far to trust it

Two uploaded files, **three distinct papers (2019, 2020, 2021), 75 problems**.

- **File 1, 18 PDF pages: "SASMO 2021 Primary 5 (Grade 5) Contest Questions"**, re-typeset under a "YTO Maths Centre" cover. It is a cover plus 25 questions, one or two to a page. **It has no solutions and no introduction.** It is not the publisher's book, and it carries small typos (a "seashells" where the problem is about pencils). Section A is headed "2 points, minus 1 for a wrong answer"; Questions 16 to 25 have no options, and I treat them as Section B because the 2019 and 2020 papers have the same shape. The Section B heading page is not in the file.
- **File 2, 57 PDF pages: the printed book "SASMO Primary 5 (Grade 5), GEP Practice, 2019 and 2020 contest problems with full solutions"** (SIMCC, 2021). Cover and front matter (PDF pp 1-8), the 2019 questions (book pp 9-19), the 2020 questions (book pp 20-31), the 2019 solutions (pp 32-41), the 2020 solutions (pp 42-52), back cover. **The two contest papers (50 problems) come with publisher's solutions.** Its "Competition and Prizes" page says calculators are not permitted and that medals go to the top 8%, 12% and 20%. The "Introduction" pages are general study advice and say nothing about timing.
- **Format**, as printed: 25 questions per paper. Section A = Q1 to 15, five options (A to E; E is "none of the above" in most items, a different last option in a few), 2 points, minus 1 for a wrong answer. Section B = Q16 to 25, whole-number answer written in a 4-digit grid, 4 points, no penalty. So the printed marks give 15 x 2 + 10 x 4 = 70, while the prizes page says a perfect score is 85. I cannot reconcile the two and I do not know the exam length.
- **How answers were checked.** The 2019 and 2020 problems already have the publisher's answer; I re-derived about 37 of the 50 that depend only on the text, by brute-force script or by hand, and all agreed with the book. The other 13 depend on a drawing (19-6, 19-8, 19-11, 19-13, 19-15, 19-16, 19-18, 20-10, 20-13, 20-15, 20-16, 20-23, 20-24): I followed the book's solution and checked its arithmetic, not the picture. **The 2021 paper had no solutions, so all 25 are mine.** 21 were solved and checked by script or by hand. 21-7 and 21-11 are picture-only and I did not solve them. 21-9 prints with its fraction bar partly missing in the scan, so I solved the most natural reading (five digit boxes in one nested fraction) and it matched one of the options; 21-20 depends on bar heights I read from the scan. Treat those four as unverified.
- Categories, bands and statuses are my single-coder judgement; each problem is filed under its main skill only, so counts are indicative. **Three papers is a small sample.** A type with 1 to 3 problems is "occasionally seen". A skill that appears about twice in every year (divisibility, section 3) is the best-supported finding.
- **Level 5 evidence base.** I read the ten holiday lesson files (`p5/content/l1.js` to `l10.js`, every question-bank item), `p5/SPEC.md`, `p5/data.js`, the enrichment files `gaps.js` and `inv.js`, `docs/terms/level_5_year_plan.md`, and searched `docs/audit/*p5*` and `docs/moe/syllabus_by_level.md`. **The term plan is a draft with no lessons written.** "Term plan: P" below therefore means the plan names the topic in that lesson's row, not that content exists or has been tested.

## 2. Catalogue

Band is how hard the item reads (my judgement from position, marks and number of steps): E = one step or known fact, M = two or three steps with a known method, H = needs a case split, an insight or a long careful count. Holiday = how well the ten Level 5 holiday lessons prepare it today; Term plan = how well the year plan's lesson rows (Terms 1 to 4) would. P = prepared, Part = partly, Gap = nothing.

| ID | Sec | Skill tag | Thinking move | Band | Holiday | Term plan |
|---|---|---|---|---|---|---|
| 19-1 | A | Digit sum of a product | Regroup one factor so the product is a round number minus a small one | M | Gap | Part |
| 19-2 | A | Which result is odd | Odd/even rules for each operation | E | Part | P |
| 19-3 | A | Missing digit, divisible by 9 | Digit-sum test | E | Gap | P |
| 19-4 | A | Next term | Differences, then differences of the differences | M | Part | Part |
| 19-5 | A | Ratio before and after a gift | Units, then the new units after the gift | M | Part | P |
| 19-6 | A | Growing triangle of circles | Black count is a triangle number, white grows by 3, compare | M | P | P |
| 19-7 | A | Nested fraction | Work from the inside; needs dividing by a fraction | M | Gap | Gap |
| 19-8 | A | Which rope forms a knot | Trace crossings in a picture | E | Gap | Gap |
| 19-9 | A | Divisor with remainder 4 | A remainder means n divides the dividend minus the remainder; list its factors above the remainder | M | Gap | Part |
| 19-10 | A | Catching up | Head start divided by speed difference | M | Gap | Gap |
| 19-11 | A | Colour four circles, three colours | Choose one colour at a time, then multiply | M | Gap | Part |
| 19-12 | A | Average of two groups | Total watch time over total viewers, with units | M | Gap | Part |
| 19-13 | A | Overlapping squares, shaded triangle | Whole square minus three corner triangles | H | P | P |
| 19-14 | A | Four friends, one lies | Test each liar in turn | M | P | P |
| 19-15 | A | Missing figure in a 3 by 3 of triangles | Find a rule for combining pictures down each column | M | Gap | Gap |
| 19-16 | B | Triangles in a picture | Count by size | H | Part | Part |
| 19-17 | B | Digit 5 on a digital clock | Count by place: hours, minute tens, minute ones | H | P | P |
| 19-18 | B | Bar chart with a ratio | Read units from the chart, scale up to the ratio | M | Part | Part |
| 19-19 | B | Tap and drain together | Add and subtract rates as fractions of a tank | M | P | Part |
| 19-20 | B | 20 numbers, products and sum | The product rule caps the odd numbers, the sum rule caps them again, then build the smallest list | H | Gap | Part |
| 19-21 | B | Rectangles in a square, perimeter | Call the small square 1 unit, equate two sides | M | Part | Part |
| 19-22 | B | Addition cryptarithm (4 digits) | Ones column first, then the leading digit, then carries | M | Gap | Gap |
| 19-23 | B | Shells in boxes, extra and short | Extra plus short is the total gap; gap per box gives the number of boxes | M | Part | Part |
| 19-24 | B | Four 2-digit numbers from hints | Cases from the hints, eliminate | H | P | P |
| 19-25 | B | Notebooks and pens with a promotion | List all ways to spend exactly $82, compare totals | H | P | Part |
| 20-1 | A | Four-number sum with brackets | Regroup to cancel | E | Part | P |
| 20-2 | A | Fraction of a fraction, backwards | Undo each fraction | E | P | P |
| 20-3 | A | Largest score that cannot be made | Find a run of reachable totals as long as the smaller step; everything after is reachable | M | Gap | Gap |
| 20-4 | A | Percent of two groups combined | Boys in each, total, then percent | M | P | P |
| 20-5 | A | Pairs of whole numbers with sum 10 | List with the order not counting | E | P | P |
| 20-6 | A | Guess the number, shared digits | Each pair shares exactly one digit, so three digits | M | Part | P |
| 20-7 | A | Missing term | Two sequences woven together | M | Gap | Part |
| 20-8 | A | Two-digit multiples of 4 not of 8 | Count multiples in a range, subtract | M | Gap | Part |
| 20-9 | A | Roses and lilies, which count is possible | List all ways to make the total from the two group sizes | H | Part | Part |
| 20-10 | A | Shape operator | Find a rule from three shape examples | M | Gap | Gap |
| 20-11 | A | Melted cuboids, new height | Volume stays the same | E | P | P |
| 20-12 | A | Three mislabelled boxes | Assume each label right, find the contradiction | M | P | P |
| 20-13 | A | Rectangle with a corner cut, area ratio | Units and parts, area as a product | M | P | P |
| 20-14 | A | Hands of a clock closest | Minute hand 6 degrees and hour hand half a degree per minute | H | Part | Part |
| 20-15 | A | Missing piece of a patterned cube | Match three faces | M | Gap | Gap |
| 20-16 | B | Triangles in a figure | Count by size, many sizes, in a figure with crossing lines | H | Part | Part |
| 20-17 | B | Last digit of a product of powers | Pair the factors, then use the repeating last digit | M | Gap | Part |
| 20-18 | B | Three tanks, two ratios | Link the two ratios by a common total | H | Part | Part |
| 20-19 | B | 4-digit numbers between two bounds, no repeats | Count by cases on the first digit | M | Part | P |
| 20-20 | B | Adults, girls, boys as percents | Girls and boys as units of the total | H | Part | P |
| 20-21 | B | Page numbers, digits used | Count digits by number of digits | M | P | Part |
| 20-22 | B | Three builders | Rates as fractions, solve for each | H | Part | Gap |
| 20-23 | B | Square, four midpoints, shaded part | Dissect and rearrange into equal squares, then a fraction of one | H | Part | P |
| 20-24 | B | Least colours for a ten-circle figure | Find a 3-colouring, show 2 is impossible | H | Gap | Gap |
| 20-25 | B | Addition cryptarithm (5-digit sum) | Carry gives the leading digit, then work down the columns with parity | M | Gap | Gap |
| 21-1 | A | Four products added | Combine terms that share a factor | E | Gap | Part |
| 21-2 | A | Which result is odd | Odd/even rules, division included | E | Part | P |
| 21-3 | A | Largest area, perimeter fixed | Sides close together | M | Part | Part |
| 21-4 | A | Count n so that 17 plus n is a multiple of 9 | Range of multiples | M | Gap | Part |
| 21-5 | A | Sum that rises then falls | Mirror halves, minus the middle | M | Part | P |
| 21-6 | A | 5 by 5 square with diagonals | Fill forced cells | M | Gap | Part |
| 21-7 | A | Rotated block figure | Picture only, not solved here | M | Gap | Part |
| 21-8 | A | Missing digit, divisible by 9 | Digit-sum test | E | Gap | P |
| 21-9 | A | Largest fraction from digit cards | Biggest top, smallest bottom, test cases | H | Part | Part |
| 21-10 | A | Ages of four people | Express all by the youngest | M | P | P |
| 21-11 | A | Dice in an L, touching sums | Picture only, not solved here | M | Gap | Gap |
| 21-12 | A | Two purchases, find another | Combine the two to get the wanted amounts | M | Gap | P |
| 21-13 | A | Price up 40 percent, how many tickets | Same money, new price | M | Part | Part |
| 21-14 | A | Weekday that occurs most | 365 is 52 weeks and 1 day | M | Part | P |
| 21-15 | A | Fewest in the biggest pile, 7 piles | Others as big as allowed, still less | M | Gap | Part |
| 21-16 | B | Eight numbers, none a multiple of another | A set of primes is safe, so the smallest two are forced | H | Gap | Gap |
| 21-17 | B | Four-digit numbers with a digit product rule | List the products the two digits can make | M | P | P |
| 21-18 | B | Two clubs and no club | Count in at least one, then overlap | M | Gap | Gap |
| 21-19 | B | Upside-down digits, difference 825 | Which digits turn into digits, then try | H | Part | Part |
| 21-20 | B | Pencils moved by halves in a cycle | Work with a unit, find first unit giving whole numbers | H | Part | Part |
| 21-21 | B | Milk shared by fraction and ratio | Units of the whole, difference given | M | Part | Part |
| 21-22 | B | Shaded triangles in a square | Same base, same height | M | P | P |
| 21-23 | B | Money spent by fractions and dollars, backwards | Undo three times | M | P | P |
| 21-24 | B | Two shoppers, equal candies | Try which type each leaves out, least common total | H | Gap | Gap |
| 21-25 | B | Savings of two friends | Days until one runs out; two equations | H | Part | Part |

Totals: band E 10, M 45, H 20. **Holiday: P 18, Part 27, Gap 30. Term plan: P 28, Part 32, Gap 15.** By paper (P / Part / Gap): holiday 2019 7 / 7 / 11, 2020 7 / 10 / 8, 2021 4 / 10 / 11; term plan 2019 8 / 12 / 5, 2020 11 / 8 / 6, 2021 9 / 12 / 4. Section A has 45 items and Section B has 30.

## 3. Frequency by type

| Type | All | A | B | Where it appears |
|---|---|---|---|---|
| Ratio, percent, average | 8 | 4 | 4 | 19-5, 19-12, 19-18, 20-4, 20-18, 20-20, 21-13, 21-21 |
| Area, perimeter, volume | 7 | 4 | 3 | 19-13, 19-21, 20-11, 20-13, 20-23, 21-3, 21-22 |
| Systematic counting (figures, digits, arrangements) | 7 | 1 | 6 | 19-16, 19-17, 20-5, 20-16, 20-19, 20-21, 21-17 |
| Word problems with units (ages, sets, remainders, extra and short) | 7 | 2 | 5 | 19-23, 21-10, 21-12, 21-18, 21-20, 21-23, 21-25 |
| Divisibility, remainders, last digits | 6 | 5 | 1 | 19-3, 19-9, 20-8, 20-17, 21-4, 21-8 |
| Computation and parity | 5 | 5 | 0 | 19-1, 19-2, 20-1, 21-1, 21-2 |
| Number patterns, series, rules | 5 | 5 | 0 | 19-4, 19-6, 20-7, 20-10, 21-5 |
| Spatial and picture reasoning | 5 | 5 | 0 | 19-8, 19-15, 20-15, 21-7, 21-11 |
| Logic and elimination | 5 | 4 | 1 | 19-14, 19-24, 20-6, 20-12, 21-6 |
| Least and greatest possible | 5 | 2 | 3 | 19-20, 20-3, 21-15, 21-16, 21-24 |
| Fractions | 3 | 3 | 0 | 19-7, 20-2, 21-9 |
| Speed and work rates | 3 | 1 | 2 | 19-10, 19-19, 20-22 |
| Cryptarithms and digit puzzles | 3 | 0 | 3 | 19-22, 20-25, 21-19 |
| Colouring circles joined by lines | 2 | 1 | 1 | 19-11, 20-24 |
| Whole-number totals (shopping, equations) | 2 | 1 | 1 | 19-25, 20-9 |
| Clocks and calendars | 2 | 2 | 0 | 20-14, 21-14 |

What stands out:
- **The same skills come back every year.** Divisibility appears in Section A twice a year (19-3 and 19-9, 20-8 and 20-17, 21-4 and 21-8). "Which result is odd" is nearly the same question in 2019 and 2021 (19-2, 21-2), and the digit test for 9 is the same question in both (19-3, 21-8). Two cryptarithms (19-22, 20-25), two triangle counts (19-16, 20-16), two counts of multiples in a range (20-8, 21-4), two square dissections (20-23, 21-22), and a ratio-with-change item every year (19-5, 20-18, 21-21). These are the best candidates for contest-oriented practice.
- **Section A is mostly short-reach technique, Section B is reasoning.** All 5 computation, all 5 pattern, all 5 spatial, 5 of 6 divisibility and both calendar and clock items are in Section A. 22 of the 30 items the holiday course leaves as Gap are Section A: a child who guesses loses a point and one who skips loses the 2 points of an easy item. All 3 cryptarithms, 3 of 5 least-and-greatest items and 6 of 7 counting items are in Section B, 4 points each.
- **The hard end is mostly Section B.** 16 of the 20 band-H items are Section B, 4 are Section A (19-13, 20-9, 20-14, 21-9). 4 of the 20 are Gap in the holiday course and in the term plan alike: 19-20, 20-24, 21-16, 21-24.
- **What is absent from all 75 problems.** Decimals, angle facts in shapes (the only angle item is the clock), properties of parallelograms and trapeziums, tank water-level problems, and line graphs. See section 6.
- Number size is modest: answers reach 5000 (21-21) and 2688 (21-25). Reading load is light, but five items need ratio notation (19-5, 19-18, 20-13, 20-18, 21-21), which the Level 5 SPEC deliberately avoids. About 20 of 75 items lean on a picture.
- A "none of the above" option is the right answer for about 4 of the 43 solved Section A items (19-11, 20-9, 21-3, 21-14), roughly one in ten, so a child must not choose it by default.

## 4. How Level 5 maps to it

Holiday lessons: L1 Million Puzzles; L2 Fraction Feats; L3 Before and After; L4 Triangle Areas; L5 Volume Vault; L6 Rate Racers; L7 Percentage Puzzles; L8 Angle Chasers; L9 Pattern Generalisers; L10 Challenge Day. Tiers in each question bank: Start here = Core (C1 to C6), Think harder = Stretch (S1 to S8 or more), Go further = Challenge (C1 to C9). In the table, "L6 Go further C9" means the Challenge item 9 of lesson 6 and so on, in the order of `p5/content/lN.js`. Term plan lessons are numbered 1 to 36 as in `docs/terms/level_5_year_plan.md`.

| Type | Holiday course prepares it | Term plan lessons | What is missing | Verdict |
|---|---|---|---|---|
| Ratio, percent, average | L3 units and before-and-after; L7 percent of an amount, combined bus percent (Challenge C5), percent of a remainder (C9); L2 fraction of a remainder. No ratio notation, no averages | 4, 16 (average, labelled P6 preview), 19 to 21, 22 (units, no notation) | Reading "a : b" as "a units to b units" (4 items use it); linking two ratios through a shared part (20-18); inverse price and quantity (21-13); weighted average (19-12) | **Partial.** The thinking is taught; the notation is avoided on purpose, so a child can read the bar model but not the question |
| Area, perimeter, volume | L4 strong (same base and height, composite shapes); L5 (melting and moving volumes, tanks) | 6, 11, 12, 14 | An unknown side called "1 unit" (19-21); largest area for a fixed perimeter (21-3) | **Prepared** |
| Systematic counting | L9 digits used for page numbers (C5) and the 100th digit (C9); L10 digit appearances (C4), rectangles by size (C2, C3) | 25 (outfits, handshakes, digit-condition numbers), 8 | **Triangles by size in a figure with crossing lines** (19-16, 20-16, both band H, 8 of 85 points); counting numbers inside bounds by case (20-19) | **Partial**, one sub-gap |
| Word problems with units | L3 (ages, constant total, constant difference), L2 and L10 (fraction chains, undo), L10 Challenge C6 | 4, 22, 23, 33 | Two overlapping groups (21-18); extra and short (19-23); two-purchase equations (21-12, term plan 23 has it); repeated halving cycles (21-20) | **Mostly prepared** |
| Divisibility, remainders, last digits | **Nothing.** L10 Think harder S6 (remainder 1) and a digit-sum clue in L1 only | 2 (Think harder: missing digit so a number divides by 3, 4, 9), 30 (remainders in a cycle), 32 (odd, even, remainders) | Counting multiples in a range (20-8, 21-4); "divisor with a given remainder" (19-9); last digit of a product of powers (20-17) | **Real gap in the holiday course; partly closed by the term plan.** Two items a year, all but one Section A |
| Computation and parity | L1 brackets and estimation; parity only inside L9 C4 | 1, 32 | A habit of regrouping and cancelling before calculating; odd and even results | **Partial**, light fix; every paper opens with these |
| Number patterns, series, rules | L9 (linear rules, triangle numbers C1, odd sums S4) | 8, 24 (pairing sums) | Differences of the differences (19-4); two sequences woven together (20-7); rules from three examples (20-10) | **Partial**, three sub-gaps, all Section A |
| Spatial and picture reasoning | L5 painted cubes (S4, C8) only | 10 (views, nets, most and fewest cubes given views) | Dice with opposite faces, mentally rotating a block figure, patterned faces of a cube, matrix of pictures (19-15), rope (19-8) | **Real gap.** Plan lesson 10 covers views, not the contest's styles |
| Logic and elimination | L10 logic grid, liars (workbook Q5), seating (Challenge C9), L1 digit riddles | 31 | A 5 by 5 Latin square with diagonals (21-6) | **Prepared** |
| Least and greatest possible | L1 "test both sides of a target" is a cousin; L10 S6. Nothing else | 32 (a pigeonhole example); "extreme case" is named in the plan's move list but has no lesson | All five: a parity cap on a set (19-20), unreachable totals (20-3), minimise the biggest (21-15), a set with no multiples (21-16), equal-total matching (21-24) | **Real gap.** 3 of 5 are Section B, 3 of 5 band H |
| Fractions | L2 (unit fractions, of a remainder, digit cards for fractions S9, C5) | 3 | 19-7 needs dividing by a fraction, which the SPEC calls a P6 skill | **Prepared** except 19-7 (beyond level) |
| Speed and work rates | L6 combined taps (C1, C5, S1), leak (C9 is the 19-19 move), shared printers | 15 (rate; speed excluded; no combined rates) | Catching up (19-10, speed); three workers (20-22) | **Partial.** Combined rates live only in the holiday course; speed is left to Level 6 |
| Cryptarithms and digit puzzles | **Nothing** (Level 3 teaches them in its L2) | none | All 3 (all Section B) | **Real gap**; a child who came through Level 3 has seen them, a new joiner has not |
| Colouring circles joined by lines | Nothing | none (25 "simple tree diagrams" is a cousin for 19-11) | Both | **Gap**, 2 items, low priority |
| Whole-number totals | L6 S2, S6, C4 (packs and deals), L10 S5, C8 (coins), L9 supposition | 26 | Listing every way to make a total from two group sizes (20-9) | **Prepared**, light extension |
| Clocks and calendars | L8 S7, S8 (angle of hands, 5 and 8 o'clock); L9 S1 (cycle) | 30 | When hands coincide (20-14) | **Prepared** in the term plan |

### Summary of status across the 75 problems

- **Prepared (P) 18 in the holiday course, 28 in the term plan.** Mostly areas, logic, working backwards with fractions, ages, digit counting, one pipe-and-drain item.
- **Partly prepared 27 and 32**: the method is taught but the contest twist is not.
- **Gap 30 and 15.** In the holiday course: all 6 divisibility items, all 5 spatial, all 5 least-and-greatest, both colouring, 2 of 3 cryptarithms, and several pattern, computation and ratio items. **14 problems are a gap in both**: 19-7, 19-8, 19-10, 19-15, 19-22, 20-3, 20-10, 20-15, 20-24, 20-25, 21-11, 21-16, 21-18, 21-24. Only 3 holiday gaps are fully closed by the term plan row alone: 19-3, 21-8, 21-12.

## 5. Biggest gaps, in the order I would weigh them

1. **Least and greatest possible, and totals that cannot be made: 5 problems, 3 in Section B, 3 band H (19-20, 20-3, 21-15, 21-16, 21-24).** Nothing in the holiday course and no lesson in the term plan, although the plan lists "extreme case" among its moves. It is the hardest and best-weighted cluster and appears every year (1, 1 and 3).
2. **Divisibility, remainders, last digits: 6 problems, 5 in Section A, two every year.** Cheap to teach (digit sum for 3 and 9, counting multiples by division, "n goes into dividend minus remainder", repeating last digits). The term plan names part of it in lesson 2 and lesson 32; the holiday course has none.
3. **Spatial and picture items: 5 problems, all Section A** (dice and cube pictures, rotation, patterned faces, a matrix of pictures, a rope). Nothing in the program. Best handled with real cubes and drawings; lesson 10 in the plan teaches views, which is the neighbouring skill.
4. **Ratio notation: 5 problems use "a : b", 3 of them in Section B.** Children who have only seen units can still solve these once they can read the notation; a ten-minute vocabulary note would close most of it. This directly bears on open question 3 of the plan.
5. **Cryptarithms: 3 problems, all Section B (4 points each).** Absent from Level 5 although Level 3 has a whole lesson on them.
6. **Counting triangles by size: 2 problems, both band H, 4 points each.** Level 5 counts squares and rectangles, not triangles in crossing lines.
7. **Speed and combined work rates: 3 problems** (19-10, 19-19, 20-22). Combined rates are in the holiday course only; plan lesson 15 excludes both.
8. **Patterns that are not a constant step: 3 problems** (19-4, 20-7, 20-10), all Section A.
9. **Thin evidence, low priority**: colouring (2), overlapping groups (1), the 5 by 5 Latin square (1), a nested fraction that needs fraction division (1, beyond P5), mental rotation of a block figure (1).

## 6. Where Think harder and Go further need extension, and what has no contest counterpart

- **Think harder is well pitched** for the E and M items in the prepared types (L3, L4, L5, L6, L9, L10): those items are the same size as Stretch S3 to S8. The exceptions are the gap types above, where Start here and Think harder are both empty.
- **Go further reaches the contest's H band only in the prepared types** (examples: L4 C8, L6 C9, L9 C9, L10 C4 and C6, L3 C8). For the gap types there is no Go further item, so the drafts in `g5_original_problems_draft.md` are written as Go further and flagged as draft until the owner decides whether to add a Start here and a Think harder step before them.
- **Six term-plan lessons have no contest counterpart in these 75 problems**: 5 Decimal Sense, 13 Decimal Measures, 12 Tank Tales (the tank items here are pipe rates, not water level), 17 Graph Stories (graph reading is 2 items, both bar charts), 28 Angles in Shapes and 29 Triangles and Quadrilaterals (no angle or shape-property item at all; the plan itself notes both go beyond the primary syllabus). This is not evidence that they are wrong: they follow the school syllabus, not the contest. It only means the contest evidence does not support them.
- The contest has no open-ended "make up your own" items; Level 5's investigation pages and lessons 35 and 36 are a program choice, not a gap.

## 7. Recommendations (nothing was edited; for the owner)

Each line says what the evidence supports, not what to build.

1. **Lesson 32 Odd, Even, Remainders:** add a Go further strand "least and greatest possible" (parity cap on a set, minimise the biggest, no-multiples set), and the "n divides dividend minus remainder" trick as Think harder. Evidence: 19-9, 19-20, 21-15, 21-16.
2. **Lesson 2 Factor Finders:** keep the digit tests (3, 4, 9), add counting multiples in a range ("how many multiples of 4 but not of 8") and the digit-sum test for 3 as taught, not only as a missing-digit item. Evidence: 20-8, 21-4 and the digit-9 pair.
3. **Lesson 22 Unequal Parts:** read "a : b" aloud as "a units to b units", teach linking two ratios through a shared part (the 4 : 7 and 6 : 50 style), keep the problems solved with units. This answers open question 3 with a reading-skill, not a P6 topic. Evidence: 19-5, 19-18, 20-13, 20-18, 21-21.
4. **Lesson 10 Solid Views:** add dice with opposite faces summing to 7 and touching faces, cubes painted on some faces only, and one rotation item. A 5-minute recurring warm-up with real cubes may serve better than lesson time. Evidence: 20-15, 21-7, 21-11.
5. **Lesson 25 Count Without Counting:** add counting triangles by size (Think harder) and digits used when numbering pages (reuse holiday L9 C5 and C9, L10 C4). Evidence: 19-16, 20-16, 20-21, 19-17.
6. **Lesson 15 Rate in the Real World:** add taps, drains and builders working together (add the fractions of a job per hour); keep speed out, as Level 6 previews it. Evidence: 19-19, 20-22; speed is 1 problem in 75.
7. **Lesson 8 Pattern Generalisers and lesson 24 Number Stories:** add differences of differences, two sequences woven together, and an "operator from three examples" item. Evidence: 19-4, 20-7, 20-10.
8. **Lesson 1 Million Puzzles and lesson 2:** open each with a short "regroup before you calculate" and odd-or-even-result warm-up. Evidence: 19-1, 19-2, 20-1, 21-1, 21-2.
9. **Lesson 30 Clocks and Calendars:** add "when do the hands coincide" and "how often do they overlap" to Go further. Evidence: 20-14.
10. **A cryptarithm slot** in lesson 9 or 31 (a plan-level decision): 3 items, all Section B.
11. **Lesson 26 Supposition Studio:** add "list every way to make a total from two group sizes" and "extra and short" as Think harder. Evidence: 19-23, 20-9.
12. **Possibly merge lessons 28 and 29** into one and use the freed slot for a "least and greatest" lesson (recommendation 1). Owner's call: both lessons are school-syllabus content, and three papers cannot say they are worthless.

## 8. Honest notes where evidence is thin

- Three papers, 75 problems, one coder. Two of the 25 for 2021 are not solved, two more are uncertain, and none of the 2021 answers has a publisher's solution to check against.
- Picture-based items: the status "Gap" for spatial types assumes the figures need the 3D skill the solutions describe; I did not re-run them independently.
- I read lesson content in `p5/content/*.js` and the SPEC, and searched keywords (divisible, remainder, digit sum, mirror, rotate, cube, dice, knot, colour, triangles by size, last digit, clock, average, pairing, parity, speed, pipe, Venn, graph, cryptarithm, shortage). The slides, scripts, Weekly Dose and workbooks were not re-read item by item, so an item that exists only there would be missed. The term-plan statuses rest on lesson titles and topic rows only.
- **The plan says "There is no SASMO file for Level 5"** and that the olympiad moves in it are general. That line is now out of date; this file and the drafts are the Level 5 SASMO evidence. I did not edit the plan.
- The contest is not the school syllabus. It uses divisibility tests, ratio notation and combined work rates that the Level 5 SPEC either avoids or places in P6 (ratio, average, speed, percentage change). Whether to teach them is the owner's decision; recommendations 3 and 6 are written so they can be taken or left.
- Contest-specific skills the program does not train and these papers reward: negative marking with a 5-option paper, eliminating options, writing an answer in a 4-digit grid, working without a calculator. They are exam skills, not maths, and the program has no timed practice.
- I cannot say how long the exam is, how the 85-point maximum is reached, or what scores earn medals beyond "top 8%, 12%, 20%".
- No lesson, slide, workbook, question bank or term-plan file was changed.
