# SASMO Grade 4 (Primary 4) contest paper: what it tests and how Level 4 prepares for it

Analysis only. No lesson files and no term plan were changed. Contest problems are not reproduced: they are referred to by paper and question number (19-12 is 2019, Question 12) with a short skill tag. My answer checks are in the git-ignored `docs/sasmo/private_solution_notes_g4.md`.

## 1. What was analysed, and how far to trust it

- **One paper only.** The uploaded file is the printed practice booklet "Primary 4 (Grade 4) GEP Practice, 2019, Contest Problems with Full Solutions" (Henry Ong and Merlan Nagidulin, copyright SIMCC). The cover and the solutions heading disagree about the year (the questions pages say 2019, the running header on the solution pages says 2020); the cover and the title "Solutions to SASMO 2019 Primary 4" say 2019, so I treat it as 2019. 22 PDF pages: cover, questions 1 to 25 (pp 2 to 11), solutions (pp 13 to 22). **One paper = 25 problems.** That is a very small sample: a type with one or two problems is "seen once", not "tested".
- Format as printed: Section A is Q1 to 15, five options (A to E, E is "none of the above"), 2 points each, minus 1 for a wrong answer, 0 for none (15 problems). Section B is Q16 to 25, whole-number answer, 4 points each, no penalty (10 problems). That makes a maximum of 70. The booklet pages with the time limit and the rules are not in the file, so I cannot state the exam length for Grade 4. (The 2022 Grade 2 paper uploaded at the same time prints 1 hour 30 minutes, no calculators, and a minimum stay of 1 hour. I would not assume Grade 4 is the same.)
- **All 25 problems have the publisher's worked solution in the file**, so nothing had to be solved from scratch. I re-derived every answer that depends on the text alone (19-1, 3 to 7, 9 to 13, 15, 16, 18, 19, 21 to 25) and checked the counting ones (19-13, 18, 19, 22, 24, 25) by a short brute-force script. All agreed with the booklet. Problems that depend on a drawing (19-2, 8, 14, 17, 20, and the scales in 15) I followed from the publisher's solution and checked against the picture where I could read it; I did not re-solve them independently. 19-8 (which rope forms a knot) cannot be checked in words at all.
- Categories are my single-coder judgement. Each problem is filed under its main skill only.
- The contest is not the school syllabus. This paper uses a divisibility test, factorial notation (introduced in the question), adding mixed numbers (a Primary 5 outcome in Singapore, which the term plan already labels "P5 preview"), a probability question and a rope-knot picture. Level 4 teaches "Primary 4 plus thinking", so some gaps below are by design. Whether to close them is the owner's call.
- Cross-grade context, not merged into counts: SASMO Grade 2 (`g2_analysis.md`, seven papers) and Grade 3 (`g3_analysis.md`, two papers) were analysed separately. I mention a repeat across grades only where it is plain from those files.

## 2. Catalogue

Band is how hard the item reads as presented (my judgement from position, marks and number of steps): E = one step or known fact, M = two or three steps with a known method, H = needs a case split, an insight or a long careful count. Status is how well the **Level 4 holiday lessons** (L1 to L10, `p4/content`) prepare the item today (section 4): P = prepared, Part = partly, Gap = nothing in the program. Section 4 also checks the **Level 4 term plan** separately.

| ID | Sec | Skill tag | Thinking move | Band | Status |
|---|---|---|---|---|---|
| 19-1 | A | Number sequence, gaps grow by 3 | Write the gaps, see the gaps rise evenly | E | Part |
| 19-2 | A | Triangles in a fish picture | Count by size (1-part, 2-part ...) | M | Part |
| 19-3 | A | Digit in 2_4 so it is divisible by 6 | Even already, digit-sum test for 3 | E | Gap |
| 19-4 | A | Weekday from "day before yesterday" | Work out today, then tomorrow | M | Part |
| 19-5 | A | Spinner: which event is most likely | Count favourable sectors | E | Gap |
| 19-6 | A | Four dice: which total is impossible | Smallest and largest possible | M | Gap |
| 19-7 | A | Factorial: hours in a month | Break 720 into a product 1 x 2 x 3 ... | H | Part |
| 19-8 | A | Which rope forms a knot | Trace over and under crossings | H | Gap |
| 19-9 | A | Routes by two stages (3 and 4 choices) | Multiply the choices | E | Part |
| 19-10 | A | Boxes diagram, find the rule, missing top | Test a rule on every diagram | M | Part |
| 19-11 | A | Sum of six mixed numbers | Simplify, pair fractions that make wholes | M | Part |
| 19-12 | A | Best rate per minute of four plans | Price over minutes as fractions, common denominator | M | Part |
| 19-13 | A | Two films, fixed show times, earliest finish | Try both orders | M | Part |
| 19-14 | A | Largest fraction of area shaded, five figures | Count shaded and total in half squares, compare | H | Part |
| 19-15 | A | Three balance scales, heaviest toy | Chain the comparisons | M | Part |
| 19-16 | B | Sum of the numbers 31 to 41 | Pair first and last | E | Gap |
| 19-17 | B | Frame of 8 equal rectangles and a square | Side of the big square from the small one | M | P |
| 19-18 | B | Smallest 3-digit number whose digit product is 3-digit | Bounds on each place, try the smallest hundreds digit | H | Gap |
| 19-19 | B | Multiple of 7 that leaves 2 when divided by 9 | List the numbers that leave 2, find the first multiple of 7 | M | P |
| 19-20 | B | Bar chart with unlabelled lines, then a fifth of the total | Find the unit from the clue, read every bar | M | P |
| 19-21 | B | Tables and chairs, change, "4 times as many" | Bar model: difference stays a fixed number of units | M | P |
| 19-22 | B | Digit 3 in every 8-digit date of a year | Count by place for day and month, year has no 3 | H | Part |
| 19-23 | B | Four-digit letter addition | Ones column first, then carries | M | Gap |
| 19-24 | B | Four 2-digit numbers from digits 1 to 8 with hints | Candidates from each hint, then cross out | H | Part |
| 19-25 | B | Lego pieces: lose some, give a fraction, three rounds | Work backwards with a bar model | H | P |

Totals: band E 5 (19-1, 3, 5, 9, 16), M 13 (2, 4, 6, 10, 11, 12, 13, 15, 17, 19, 20, 21, 23), H 7 (7, 8, 14, 18, 22, 24, 25). Status P 5, Part 13, Gap 7.

## 3. Frequency by type

| Type | All | A | B | Where it appears |
|---|---|---|---|---|
| Divisibility, factors, remainders (digit test, factorial, "leaves 2") | 3 | 2 | 1 | 19-3, 19-7, 19-19 |
| Counting figures and ways (triangles, route choices, digits in dates) | 3 | 2 | 1 | 19-2, 19-9, 19-22 |
| Number sequences and rules (gaps that grow, rule in boxes) | 2 | 2 | 0 | 19-1, 19-10 |
| Sums by pairing (a run of numbers, mixed numbers that pair to wholes) | 2 | 1 | 1 | 19-11, 19-16 |
| Time, calendar, schedules | 2 | 2 | 0 | 19-4, 19-13 |
| Chance and bounds (spinner, sum of four dice) | 2 | 2 | 0 | 19-5, 19-6 |
| Fractions: compare shaded areas, fractions of what is left | 2 | 1 | 1 | 19-14, 19-25 |
| Digit puzzles (digit product, hints on four numbers) | 2 | 0 | 2 | 19-18, 19-24 |
| Letter-digit addition (cryptarithm) | 1 | 0 | 1 | 19-23 |
| Rate (best price per minute) | 1 | 1 | 0 | 19-12 |
| Balance-scale comparison chains | 1 | 1 | 0 | 19-15 |
| Spatial (rope and knot) | 1 | 1 | 0 | 19-8 |
| Area and perimeter | 1 | 0 | 1 | 19-17 |
| Reading a bar chart | 1 | 0 | 1 | 19-20 |
| Bar-model word problem | 1 | 0 | 1 | 19-21 |

What stands out (one paper, so indicative only):
- **Section A is again mostly short-reach items**: 4 of the 7 "Gap" problems are Section A (19-3, 5, 6, 8) and all are 2-point items with a minus-1 penalty. A child who has never met a digit test for 6, a spinner or a four-dice bound loses easy points. The other 3 gaps (19-16, 18, 23) are Section B.
- **Section B holds the reasoning**: the cryptarithm, both digit puzzles, the "work backwards" fractions, the date count, the frame and the bar-model problem are all in Section B. Four of the seven H-band problems (19-18, 22, 24, 25) are 4-point items.
- **Several types repeat the Grade 2 and Grade 3 papers in a harder coat**: a sequence with growing gaps; a sum made easy by pairing; a divisibility test (Grade 3 had four); a letter-digit sum; a timetable with two films to try in both orders (Grade 3 had the same move); working backwards through a story with fractions; counting figures by size; balance scales; and "which total is impossible" (Grade 3 had the three-dice version). This is the most useful finding for planning: **the same thinking moves are asked at every grade; only the numbers grow.**
- Number size: answers stay under 1200 except the 4-digit letter sum (9034) and the factorial. Fractions go to quarters, thirds and 25ths; mixed-number addition is a P5 outcome.
- Reading load is light. 5 of 25 depend on a drawing (19-2, 8, 14, 17, 20) plus the three scales in 19-15.

## 4. How Level 4 maps to it

### 4a. The ten Level 4 holiday lessons

L1 Factor Hunters; L2 Big Number Puzzles; L3 Operation Detectives; L4 Fraction Frontier; L5 Decimal Detectives; L6 Angle Turns; L7 Area Architects II; L8 Symmetry and Nets; L9 Data Detectives; L10 Challenge Day. Tiers in each question bank: Start here = Core (C1 to C6), Think harder = Stretch (S1 to S8 or more, of which the first four print on the workbook), Go further = Challenge (C1 to C9, of which the last three print). I searched `p4/content/*.js` and `p4/SPEC.md` for: divisible, digit sum, cryptarithm, letters stand, pairing, Gauss, spinner, chance, likely, probability, best buy, per minute, calendar, day of the week, timetable, cinema, triangles, balance, knot, factorial. Matches and misses are the basis of the table.

| Type | What Level 4 already has | Start here / Think harder | Go further would need | Verdict |
|---|---|---|---|---|
| Divisibility, factors, remainders | L1: factors, common multiples, "exactly 3 factors" (S4), numbers with 1 left over (C2, C8), the lockers (C9), "multiples of 4 or 6" (C1) | 19-19 is the L1 move exactly (C2 and C8 list the numbers that leave a remainder, then pick the multiple). 19-7 (factorial) uses factor pairs, L1 S1 and S7 | **No digit test for 3 or for 6 anywhere** (searched: no "divisible", no digit sum). "A number is in the 6 table if it is in the 2 and the 3 tables" is not taught. Factorial notation is never met | 19-19 **prepared**; 19-3 **real gap**, cheap to close; 19-7 partial |
| Counting figures and ways | L1 S5 and C5 list-all; L8 C8 counts ways to shade; L10 C1 counts numbers with a 7 in them; L2 C3 and C7 count digit-restricted numbers | "Count by size" in a drawing is only used for angles in a fan (L6 S6, C2: 4 + 3 + 2 + 1) | Multiplying choices when there are two stages (no item says "3 ways then 4 ways"); triangles by size; digits counted over dates (needs place-by-place counting, L10 C1 is the nearest) | Partial: all three |
| Number sequences and rules | L2 S3 (constant step), L3 S6 and C5 (add the two before, work back), L9 C1 and C6 (steady changes) | Constant steps and Fibonacci-type chains are covered | Gaps that grow evenly (the 19-1 sequence); a rule found from three or four diagrams (19-10) and tested on all | Partial |
| Sums by pairing | L3 uses brackets and number chains; no item pairs a run of numbers | None | A run of consecutive numbers (31 to 41), a list of mixed numbers that pair into wholes (19-11), "first plus last". The `Gauss` idea appears nowhere in `p4/content` | **Real gap**; cheap and very repeatable across grades |
| Time, calendar, schedules | L6 clock-hand angles only. No duration, timetable or calendar item in L1 to L10 except L1's "buses meet again" | None | Weekday arithmetic with "day before yesterday"; a two-event timetable (try both orders). Term-plan lesson 3.8 is planned for this | **Gap in the holiday course** (planned later) |
| Chance and bounds | None. `spinner`, `chance`, `likely` do not appear | None | Count the favourable sectors; smallest and largest total of 4 dice so a total is impossible | **Real gap**, small, both Section A |
| Fractions (compare, of what is left) | L4 is strong: compare unlike denominators (S1, S3), fraction of a set (S2, S9), two fractions of one whole (C2, C5, C6), "of the rest" (C9) | 19-25 is L4 C9 and L3 C8 in a new story | Shaded areas with half squares, then compare with a common denominator (19-14: only whole-square shading in L4) | 19-25 **prepared**; 19-14 partial |
| Digit puzzles | L2 is built for them: digit cards, "find all", riddles with several clues (S1, S2, S5, S8, C4, C7, C8); L5 S4 mystery decimal | 19-24 (hints on four numbers) is the L2 S8 and L5 S4 move with more clues | A bound on a product of digits (19-18): "largest product if the hundreds digit is 1, then if 2 ..." | Partial |
| Letter-digit addition | **None** in L1 to L10 (the term "cryptarithm" does not appear; L3 mentions "missing signs", not missing digits) | None | The whole strand: carries, "different letters, different digits", ones column first | **Real gap** (Level 2 and Level 3 do teach it) |
| Rate | L5 S9 (divide a length), L5 S5 (price of one) | "Price of one item" is covered | Compare "price per minute" of several plans using fractions with a common denominator (19-12) | Partial |
| Balance-scale chains | L5 C2 (3 apples and a pear, subtract one balance from another); L9 mass puzzles | The "take one from the other" move is covered | Chains where a heavier-than conclusion has to be passed along ("a train is heavier than a ship, so ...") | Partial |
| Spatial (rope and knot) | None. L8 is nets and symmetry | None | Not a teachable skill in words; the paper has one | **Gap**, thin evidence, low value |
| Area and perimeter | L7: frames, composite shapes, "push the steps out" (S4, C2, C4) | 19-17 is L7 S5 (path round a lawn) turned round | None | **Prepared** |
| Bar chart | L9: scales, unit lines, steady changes (S2, S7, C3, C4 where each line is worth a number) | The "find what a line is worth from a clue" move is L9 S2 | None | **Prepared** |
| Bar-model word problem | L3 S1, S11, C6 ("times as many", one amount given away); L9 C7 | 19-21 is L3 C6 with sold and bought | None | **Prepared** |

### 4b. The Level 4 term plan (`docs/terms/level_4_year_plan.md`, Terms 1 to 4)

The plan was written before this file existed (its evidence line says no Grade 4 file was available). Lesson numbers below are T.L (term.lesson). I read the plan's tier lines; they are one-line briefs, so a "yes" means the topic is named, not that a worked item exists.

| Type | Plan lesson(s) that touch it | Verdict | Real gap |
|---|---|---|---|
| Divisibility, factors, remainders | 1.3 Factor Hunters (S sharing, T meet again, G odd number of factors); 2.2 Remainder Riddles (G: numbers with given remainders) | 19-19 **prepared** (2.2 G). 19-3 digit test for 6: **not named** | Digit tests for 3 and 6; "2 and 3 means 6" |
| Counting figures and ways | 3.1 G (rectangles in a grid); 3.9 S (count shapes); 4.4 Solve a Smaller Problem (count digits); 4.5 Make a Systematic List ("count without listing" is only G) | Mostly **prepared** | Move "multiply the choices" from G to T in 4.5; add triangles by size to 3.1 or 3.9 |
| Number sequences and rules | 4.3 Patterns and Rules in Words (S continue, T the 20th term, G rule for sums); section 4 lists "sequences by gap of the gaps" as a planned move | **Prepared**, if the "gap of the gaps" is made a Start here or Think harder item and not left as a note | The rule-in-boxes diagram |
| Sums by pairing | 4.3 G ("rule for sums"); section 4 lists "pairing 1 to n" | **Planned** but only as Go further, and in Term 4 | Bring a first pairing item forward (see section 5) |
| Time, calendar | 3.8 Time Travellers (S start and end, T crossing noon, G meeting times with cycles); 2.2 T ("what day in 100 days") | Partly planned. "Two events, try both orders" and "day before yesterday" language are not named | Add both to 3.8 (T tier) |
| Chance and bounds | **None** (probability is not in the plan; Level 2's plan has a chance lesson) | **Gap** | A short routine in 4.5 or the 1.9 Challenge Day |
| Fractions | 1.4, 2.4 (equivalent), 2.5 What Is Left? (S one-step, T two steps, G work backwards from the last piece), 2.6 | 19-25 **prepared** (2.5 G). 19-14: 2.4 and 3.6 do not name shaded-area comparison | Add "compare shaded fractions of a grid with half squares" at T in 2.4 |
| Digit puzzles | 1.1 Big Number Puzzles (S digit cards, T work back, G riddles with several digit conditions) | **Prepared**; 19-18 (digit product) is a small addition to 1.1 G | |
| Letter-digit addition | **None** (no lesson names cryptarithms or letter puzzles; 2.1 G lists "digit-swap and last-digit puzzles") | **Gap** | Add to 2.1 G or 1.1 T (see section 5) |
| Rate | 2.7 Decimals in Money and Measures (G: "which of three shops is cheapest per unit of a stated size") | **Prepared** at G only. 19-12 is a Section A item (E band) | Promote to T in 2.7 |
| Balance-scale chains | None named. 2.3 Bar Model Builder I and 4.7 Suppose and Compare are the nearest | **Gap** (small) | Add one item to 4.7 T |
| Spatial (rope) | 3.7 Cubes and Cuboids Unfolded is about cubes, views and nets | **Not a fit**; evidence is one item | None |
| Area and perimeter | 1.6, 3.3, 3.4 Frames and Paths | **Prepared** | |
| Bar chart | 4.1 Data Detectives II | **Prepared** | |
| Bar-model word problem | 2.3 Bar Model Builder I, 2.5, 4.6 Working Backwards | **Prepared** | |

## 5. Biggest gaps, in the order I would weigh them

1. **Letter-digit addition (cryptarithms): 1 problem here, but it is in 8 of the 10 SASMO papers I have now seen (Grade 2: 2014, 2016, 2018, 2020, 2022; Grade 3: 2019, 2020; Grade 4: 2019), always a Section B item.** Level 2 and Level 3 teach it; **neither the Level 4 holiday course nor the term plan mentions it.** This is the largest gap against the contest evidence.
2. **Divisibility tests (3, 6) and combined conditions: 3 problems here, and the Grade 3 papers had four more.** Cheap to teach (digit sum; "in the 2 and 3 tables means the 6 table"). 19-3 is a 2-point Section A item that is solved in under 30 seconds by a child who knows the test.
3. **Sums by pairing: 2 problems here; every Grade 2 paper from 2015 to 2022 that I have seen has one, and Grade 3 had one in each paper.** The holiday course never teaches it, and the term plan has it only as a Term 4 Go further.
4. **Chance and bounds (spinner, "this total is impossible"): 2 problems, both Section A.** Nothing in either plan. The "impossible total" move was in the Grade 3 papers too.
5. **Time and schedule items (two films, weekday from a phrase): 2 problems.** The term plan has it in 3.8 (Term 3), so a child in the holiday course meets neither.
6. **Growing-gap sequences and rules found from a diagram: 2 problems.** Prepared by L2 and L3 only for constant steps.
7. **Balance-scale chains (1) and rate by fractions (1) and digit product (1):** small shares; two are already covered at Go further in the term plan.
8. **The rope and knot item (1):** no recommendation; one problem and a picture task.

## 6. Where Think harder and Go further need extension

- **Think harder is generally well pitched.** The E and M items in the prepared types (19-17, 19-19, 19-20, 19-21, 19-25) would be comfortable for a child who finishes L3, L4, L7 and L9 Think harder. The same holds for the hint puzzle 19-24 after L2 and L5.
- **Go further has no item at all for the gap types in section 5.** The draft problems in `g4_original_problems_draft.md` are written as Go further, with the note that for four of them (cryptarithms, digit tests, pairing, chance) a Start here and a Think harder step should be written before them, because the idea has never been met.
- The contest has no "make up your own" items; Go further does. That is a program choice, not a gap.

## 7. Honest notes where evidence is thin

- One paper, 25 problems, one coder. A single occurrence is not a trend. The strongest evidence in this file is not 19-23 alone but the cross-paper repeats, and those come from my own earlier Grade 2 and Grade 3 categories, not from a fresh re-count.
- I did not re-solve the picture-based items (19-2, 8, 14, 17, 20 and the three scales in 19-15). 19-14 in particular depends on how the publisher read the half squares.
- I searched the lesson content by keyword. An item that exists only in slides, scripts, the Weekly Dose or the tutor guide would be missed. L5 (decimals) and L6 (angles) have no counterpart in this paper, so the contest evidence says nothing about those two lessons either way. L8 (symmetry and nets) has only the rope item.
- The paper uses 4-digit sums, a factorial and mixed-number addition; the last is a Primary 5 outcome. This file does not recommend teaching it earlier.
- The file's front matter (time limit, rules, scoring advice) is absent for Grade 4. Scoring is the only format information I can state, from the section headings: A 2 points with minus 1, B 4 points.
- Contest exam skills (option elimination with negative marking, "none of the above" answers, writing a four-digit answer into a grid) are not maths and no plan teaches them. The term plan's Term 4 challenge day gives one taste.
- No lesson, slide, workbook, question-bank file or term plan was changed. The term plan's "Evidence status" line (no Grade 4 file exists) is now out of date; I left it alone.
