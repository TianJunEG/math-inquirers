# Level 6 term-time year plan (ages 11-13, maths + coding bridge)

## Verified against MOE syllabus (Oct 2025)

Every MOE statement below was first marked [to verify]. They have now been checked against the official PDF (`docs/moe/syllabus_by_level.md`; PDF page numbers). All [to verify] flags on MOE placement are resolved; the only unconfirmed items are Secondary 1 and 2 years, which are not in the primary syllabus. Corrections:

| Lesson | Was | Now (page) |
|---|---|---|
| 1 Code the Pattern | "letter rule is secondary [to verify]" | Number-sequence patterns are P1 to P4; nth-term formulas are not in primary; expressions such as 3a are P6 Algebra 1.2 (p. 43). "6n - 4" uses P6 notation but the nth-term idea is secondary. |
| 2 Prime Hunters | "primes are a secondary topic [to verify]" | Confirmed: **"prime" appears nowhere in the primary syllabus**. Factors are P4 (p. 37). |
| 3 Below Zero | "secondary topic" | Confirmed: no negative numbers in primary. |
| 4 Algebra Machines | "P6 [to verify]; brackets and both-sides are secondary-style" | Confirmed P6 (Algebra 1.1 to 1.5, p. 43): letter for unknown, simple expressions, substitution, simple linear equations "involving whole number coefficient only". Brackets: 1.3 says "excluding brackets". Unknown on both sides is not stated. |
| 7 Turtle Geometry | "polygon sums secondary [to verify]" | P6 has unknown angles in composite figures of square, rectangle, triangle, parallelogram, rhombus, trapezium (p. 44). Polygon angle sums and star polygons are not in primary. |
| 10 Ratio Recipes | "Ratio (Number P6)" | Confirmed P6 (1.1 to 1.7, p. 43); the syllabus **excludes ratios involving fractions and decimals**. |
| 11 Fractions of Fractions | "x and divide (P5/P6 [to verify])" | Fraction x fraction is **P5** (p. 41). Dividing a proper fraction by a whole number and a whole number or proper fraction by a proper fraction are **P6** (1.1, 1.2, p. 43). Dividing by an improper fraction or mixed number is not listed. |
| 12 Percent Change Detective | "P6 [to verify]" | Percentage increase/decrease and finding the whole are **P6** (p. 43). Discount, GST and annual (simple) interest are P5 (p. 41). Repeated change and compound growth are beyond primary. |
| 13 Rate and Speed Stories | "speed moved out of P6 in 2021 [to verify]" | **"Speed" is in no primary year.** Rate is P5 (p. 41). Speed, average speed and distance-time graphs are secondary. Retitle "Rate Stories" or label the speed items as secondary. |
| 14 Circles and Pi | "P6" | Confirmed P6: circle area and circumference, semicircle, quarter circle and composite figures (p. 44). |
| 15 Volume and Nets | "surface area (P6; nets P4 [to verify])" | Nets are **P4** (p. 39). Volume of cuboid is **P5** (p. 42); P6 adds only inverse problems (dimension, edge of a cube, height from volume and base area, face area, p. 44). **Surface area is not in the primary syllabus.** |
| 16 Angle Chasing | "(P6 and Sec 1 [to verify])" | Angles on a line, at a point, vertically opposite and triangle sum are **P5** (p. 42); composite-figure angles P6 (p. 44). Angles between parallel lines (transversals) are not in primary. |
| 17 Symmetry and Transformations | "Hong Kong P6 rotational symmetry; secondary" | Line symmetry is **P4** (p. 39). Rotation, translation, tessellation and rotational symmetry are not in primary. |
| 24 Powers and Roots | "(Sec 1)" | Only the use of the square-root and cube-root signs, for a side from an area and an edge from a volume, is P6 (2.5, p. 44); powers are not named. |
| 25 Factors, HCF and LCM | "Sec 1 [to verify]" | Common factors and common multiples are **P4** (p. 37); the names HCF and LCM and prime factorisation are not in primary. |
| 28 Statistics That Mislead | "pie P4 [to verify]" | Confirmed **P4** (p. 40); average **P6** (p. 44); median, mode, scatter plots not in primary. |
| Coverage table | "Decimals: **Gap**: no decimal lesson" | P6 Standard has **no Decimals strand** (decimals are P4 and P5), so this is not a P6 gap. |
| Coverage table | "Rate and speed ... Speed may be secondary now [to verify]" | Rate is P5; speed is in no primary year. |

Syllabus outcomes the plan misses or only touches: P6 fraction division with a whole number or proper fraction as a skill (lesson 11 is one lesson); the inverse volume problems (15 touches); percentage of "find the whole" (12 touches); algebra notation "a ÷ 3 or a/3" and simplifying simple expressions (4, 19). Things we teach that are not in the syllabus at any primary year: sequences with nth term, primes, negative numbers, counting rules, probability, modular arithmetic, ciphers, scale factors, inequalities, coordinates, linear graphs, binary, scatter plots, logic and proof, surface area, transformations.

Draft for the owner, 2026-10-22. This is a plan, not lessons. Nothing here has been tested with children. MOE year placements are taken from `docs/audit/moe_alignment_p4_p6.md`, which has now been verified against the official syllabus PDF (see the verified block above). No SASMO file exists for this level yet (only `docs/sasmo/g1_analysis.md`), so the olympiad-type list in section 4 comes from general knowledge of contest habits, not from a contest analysis.

Format: 4 terms x 9 lessons x 90 minutes, live online, groups of up to 8, one lesson a week. A term of about 10 weeks leaves one buffer week (make-up lesson, end-of-term check, public-holiday slip). Do not hardcode dates; check each year's MOE calendar, because Term 4 is often shorter.

## 1. Design principles

- **The year has one arc: Notice patterns, Scale and compare, Generalise with letters and code, Model and decide.** Term 1 (adapted holiday course) asks "what is the rule?"; Term 2 "how do quantities scale together?" (ratio, percent, rate, circles, volume); Term 3 "how do we say it for every case?" (algebra, graphs, powers, factors, binary); Term 4 "what can we trust?" (data, chance, logic, a capstone build).
- **Spiral by new setting, never by repeat.** Each Term 2-4 lesson opens with a 5-minute "from before" warm-up that uses an earlier idea in a new setting (primes in HCF, nth term in straight-line graphs, simulation in estimating pi). The Think harder tier is where an earlier idea returns on purpose. The spiral map is in section 3.
- **Problem solving is taught as named moves.** Term 1 introduces moves informally (try small cases, make a table, draw a model). Term 2 names them (before-and-after model, unit method, supposition). Term 3 adds "write it as an equation" and "check by brute force in code". Term 4 adds proof-like moves (counterexample, parity, work backwards, pigeonhole) and a free choice of tool. Each term ends with a mixed lesson where the child picks the move.
- **Inquiry is built up in three steps.** Term 1: notice and test given examples. Term 2: ask "what if I change this number?" and record what changes and what stays the same. Term 3: pose your own question and test it by hand and in code. Term 4: choose a question, plan, build, test, explain why, present (capstone, lessons 35-36).
- **Coding is a thinking tool, never the goal.** The maths comes first and code is how we test it. The code strand and tier labels are in section 4 and keep the holiday rule: small programs, block names from the official Scratch 3 palette, our own block drawings, no accounts, nothing uploaded. Python arrives in Term 3 as a bridge, always with the Scratch version beside it.
- **Tiers follow the program principle.** Start here = core, approachable without being taught first. Think harder = the taught idea in a new setting. Go further = mastery plus extension, including "find all", "is it always true?" and "make up your own". Labels stay neutral (no gifted wording, no ranking). Any contest-style items are our own originals; tutor-only solution notes and Scratch answer keys never go to families. This is not PSLE drill, and we do not promise exam results.

## 2. Term-by-term lessons

Tier lines: S = Start here, T = Think harder, G = Go further. MOE strand names follow section 5.

### Term 1: Patterns, numbers and first code (adapted holiday course, 9 lessons)

| No | Title and big idea | Topics (strand; other countries) | Tiers (one line each) | Thinking skill |
|---|---|---|---|---|
| 1 | Code the Pattern: a rule lets you jump to the 100th term | Number patterns, nth term (Number and Algebra; letter rule is secondary; 3a-style notation is P6); Scratch loop and variable | S: continue a growing pattern and fill a table. T: write the rule, test "is 50 in the list?". G: two sequences that meet; rule from two far terms | Generalising |
| 2 | Prime Hunters: every number is built from primes | Factors, primes, prime factorisation (Number; primes are not in the primary syllabus); if, mod, counter | S: factor pairs of a number, sort by number of factors. T: factor tree, test a number by small divisors. G: numbers with exactly 3 factors; Goldbach, "always true?" | Classifying |
| 3 | Below Zero: numbers go on past zero | Negative numbers (secondary topic; Hong Kong primary has none); sprite on a number line | S: read temperatures on a vertical line. T: several lift and sea-level moves. G: find all pairs with a - b = 7; spot a wrong sign rule | Representing on a model |
| 4 | Algebra Machines: write the rule with a letter | Algebra: letter as unknown, simple equations (P6, p. 43); brackets are excluded at P6 and both-sides is not stated, so those are secondary-style | S: guess my rule from IN/OUT. T: write OUT = 3n + 2, run it backwards. G: two machines, same OUT; form the equation | Working backwards |
| 5 | Every Possible Way: count each case once | Counting (not an MOE primary topic; compound events US G7); nested loops | S: list outfits in order. T: multiplication rule, handshakes. G: digit numbers with 0, no double count | Systematic listing |
| 6 | Fair or Unfair?: chance as fractions | Probability (not MOE primary; Australia Y7, US G7); random and 1000 trials | S: spinner and dice, fair or not. T: all 36 outcomes, make a game fair. G: why 1000 runs are near, not equal; test "two outcomes means fair" | Testing a claim |
| 7 | Turtle Geometry: one trip round turns 360 degrees | Angles in polygons, turn angle (nearest MOE: angles in geometric figures P6; polygon sums not in primary); Pen blocks | S: draw a square and triangle by turning. T: turn = 360 / sides; inside angle. G: star polygons; sides from an angle | Predicting and checking |
| 8 | Secret Codes: counting that wraps round | Clock (modular) arithmetic, Caesar ciphers (not in any curriculum we checked); lists, mod | S: clock sums. T: mod 12 and mod 7 calendar puzzles. G: crack a code; shift 13 decodes itself, why? | Cycles |
| 9 | Showcase Round: use it all, build a puzzle | Mixed spiral of 1-8 (all Number, Algebra, Geometry strands); a small program | S: change one number in a working starter and predict. T: twist the starter's rule. G: invent a puzzle with one answer and explain why | Choosing a move |

### Term 2: Scale and compare (ratio, fractions, percent, rate, shape)

All new. This is where Level 6 touches P6 strands, as reasoning lessons, not drill.

| No | Title and big idea | Topics (strand; other countries) | Tiers | Thinking skill |
|---|---|---|---|---|
| 10 | Ratio Recipes: parts, not amounts | Ratio, equivalent ratios, a:b:c, sharing in a ratio (Number P6); bar models; Sec 1 ratio | S: share with counters in 1:3. T: same amount added to both parts (what stays the same). G: three-way ratio, one given difference; make up a ratio puzzle with one answer | Modelling with bars |
| 11 | Fractions of Fractions: area models | Fraction x fraction (P5); division by a whole number or proper fraction (P6); Singapore model drawing | S: fold paper for 1/2 of 1/3. T: divide a fraction by a whole, then by a fraction, by picture. G: telescoping product 1/2 x 2/3 x ... ; why does dividing by 1/2 double? | Visualising |
| 12 | Percent Change Detective: up 20 then down 20 | Percentage: discount, GST, interest (P5); increase and decrease, find the whole (P6); repeated change is beyond primary; compound loop in code | S: 10% and 25% of a price with a grid. T: find the original after a discount. G: +20% then -20%, is it back to start? Interest over 10 years | Spotting hidden wholes |
| 13 | Rate Stories | Rate (P5, revisited); unit rates, comparing rates (per hour, per item), tables and simple line graphs of change; speed removed from the program (not in any primary year, owner decision) | S: read a rate from a table. T: compare two rates in a new setting. G: which rate is better value, and why? | Comparing change |
| 14 | Circles and Pi: measure it, then estimate it | Circumference and area of circles (P6; Hong Kong P6 pi); estimate pi with random dots in code | S: measure round objects at home, find the ratio. T: composite shapes with semicircles. G: why is area ~ 3.14 r x r? dart-throwing estimate (spiral of lesson 6) | Estimating |
| 15 | Volume and Nets: cubes in boxes | Volume of cube and cuboid (P5; inverse problems P6), nets (P4), surface area (not in primary); painted-cube counts | S: build a cuboid from 24 cubes, list all. T: water level rises; pour between tanks. G: painted-cube counts for n x n x n; same volume, least surface | Seeing in 3D |
| 16 | Angle Chasing | Angles in geometric figures: lines, triangles, parallel lines (P5 for lines, points and triangles; P6 for composite figures; parallel-line angles not in primary); turtle spiral | S: angles on a line and at a point. T: isosceles and exterior angle puzzles. G: a chase needing two steps and a proof sentence; use the polygon turn from lesson 7 | Chaining deductions |
| 17 | Symmetry and Transformations | Symmetry, reflect, rotate, translate, tessellate (Hong Kong P6 rotational symmetry; secondary); My Block with an input | S: fold and mirror shapes. T: rotation of order n. G: which regular shapes tessellate, and why (angle sum) | Visualising change |
| 18 | Scale Model Studio: lengths, areas, volumes | Scale factor: perimeter x k, area x k x k, volume x k x k x k (ratio, area, volume); program that scales a drawing; mixed round | S: enlarge a shape on grid paper by 2. T: cost of paint when the model doubles. G: predict then check area and volume factors; find a surprising case | Synthesising |

### Term 3: Say it for every case (algebra, graphs, powers, factors, binary; Python bridge)

All new. Python starts here, always next to the Scratch version.

| No | Title and big idea | Topics (strand; other countries) | Tiers | Thinking skill |
|---|---|---|---|---|
| 19 | Letters and Brackets: area models | Simplify, substitute, expand a(b + c) with rectangles (Algebra P6; expand is Sec 1); Python intro: print, variable, input | S: area of a split rectangle, numbers only. T: write and expand 3(n + 2). G: are two expressions always equal? test, then prove with area | Generalising |
| 20 | Equations on a Balance | Solve linear equations, unknown on both sides (P6 simple; both sides Sec 1-2); `for` and `if` to check by brute force | S: balance picture with weights. T: two-step and both-sides. G: build an equation with a given answer; why brute force needs a limit | Keeping it balanced |
| 21 | At Least, At Most | Inequalities, number-line solution sets, integer solutions (Sec 1); list solutions with a loop | S: "at least 5" on a line. T: solve 2n + 1 < 15, count whole solutions. G: smallest n so that plan A beats plan B | Describing a set |
| 22 | Maps with Numbers | Coordinates, four quadrants (Sec 1; Hong Kong, Australia earlier); distance, shapes, reflection; turtle `goto` | S: plot and name points. T: find the fourth corner of a shape. G: reflect across a line, find the rule for (x, y) | Linking algebra and geometry |
| 23 | Straight-Line Stories | Linear graphs from tables, gradient as rate, intersection (Sec 1-2); links to nth term (L1) and rate (L13) | S: plot a table of a taxi fare. T: read the gradient and starting value. G: when do two plans cost the same? what if the lines are parallel? | Reading a graph |
| 24 | Powers and Roots | Squares, cubes, powers, square roots of perfect squares (Sec 1); doubling vs adding growth | S: square numbers from dot patterns. T: 2 to the 10th by doubling; compare growth. G: last digit of powers (spiral of mod); number of ancestors | Seeing growth |
| 25 | Factors, HCF and LCM | HCF and LCM by prime factorisation (common factors and multiples are P4; the HCF/LCM names and prime factorisation are not in primary); gears and meeting problems; Euclid's method in code | S: common factors of 12 and 18 by lists. T: LCM for two buses. G: HCF with Euclid; why does the method stop? | Using structure |
| 26 | Binary and Twenty Questions | Binary numbers, place value in base 2 (not MOE; school computing); binary search | S: count to 15 with 4 switches. T: convert both ways. G: guess 1 to 100 in 7 questions, why 7? | Representing |
| 27 | Term 3 Studio: build a puzzle maker | Mixed round of 19-26; a short Python or Scratch puzzle program, with a check by hand | S: change a working template. T: extend with a loop and a test. G: add a rule that makes the answer unique; explain | Choosing a move |

### Term 4: What can we trust? (data, chance, logic, capstone)

All new, except deliberate spirals (flagged). Children who finish PSLE before this term can run longer builds; see section 7.

| No | Title and big idea | Topics (strand; other countries) | Tiers | Thinking skill |
|---|---|---|---|---|
| 28 | Statistics That Mislead | Average, pie charts, line graphs, misleading scales (average P6; pie charts and line graphs P4); mean, median, outlier is a **deliberate spiral** of the cut holiday lesson 9, in new data; list program | S: read a pie chart and a bar chart. T: how one extreme value moves mean and median. G: redraw a graph so it misleads; spot the trick | Critical reading |
| 29 | Scatter and Spreadsheets | Scatter plots, correlation vs cause (Sec 2-3; US G8); class data collected in a spreadsheet | S: plot pairs of data. T: describe a trend, predict. G: two things move together, give a third cause | Questioning data |
| 30 | Two-Stage Chance | Tree diagrams, independent events, expected value (Sec 2; spiral of lesson 6); Monty Hall simulation | S: two coins on a tree. T: the chance of both, one or neither. G: Monty Hall, simulate then explain | Predict then simulate |
| 31 | Counting with Constraints | Arrangements, selections, Pascal's triangle (not in primary curricula; spiral of lesson 5); nested loops | S: arrange 3 books. T: with repeats; teams from a class. G: Pascal row sums, route counts | Systematic counting |
| 32 | Patterns That Grow | Triangular numbers, Fibonacci, recursion (spiral of lesson 1; not MOE); recursive count in code | S: stack squares and balls. T: find the rule from the previous term. G: closed form for triangular numbers; why 2 numbers apart | Recursion |
| 33 | Logic and Proof | Venn diagrams, logic grids, true/false, counterexample, parity (not MOE primary; Hong Kong enrichment) | S: logic grid with 3 children. T: Venn with overlap. G: prove "odd + odd = even"; find a counterexample | Proving |
| 34 | Olympiad-Style Workshop | Heuristics: work backwards, supposition, invariants, pigeonhole (PSLE heuristics P1-6; contest style) with original problems | S: heads and legs by table. T: supposition and before-after. G: pigeonhole and invariant problems; write a clear solution | Choosing a strategy |
| 35 | Capstone 1: Plan and Prototype | Mixed (all strands); child picks a question (a game, a simulator, a visual), maths by hand first, prototype in Scratch or Python | S: pick a template and change it. T: add a rule and test. G: pose an open question; plan a test | Planning |
| 36 | Capstone 2: Test, Explain, Present | Mixed spiral round; 3-minute showcase with a "why it works" slide | S: show and explain one test. T: show a bug found and fixed. G: show a limit or extension; answer a peer's question | Explaining |

## 3. How the holiday lessons are reused

| Holiday lesson | Where | Treatment and why |
|---|---|---|
| L1-L8 | Term 1, lessons 1-8 | Kept in order, because each already has a guide, slides, workbook, qbank, Scratch starter (`p6/scratch/starters`) and the audit fixes (warm-up check, open investigation, reflection). Change: one weekly slot instead of two, so the A/B halves become a longer lesson plus take-home; re-time using `p6/budget.json`. |
| L9 Data Detectives | **Cut from Term 1**, content moves to Term 4 lesson 28 | The mean alone is below a P6 child's level (audit calls it BELOW); median and outlier are the new part. The `L9_Mean_Machine.sb3` starter is reused there. This is a deliberate spiral, not a duplicate. |
| L10 Showcase | **Trimmed** to Term 1 lesson 9 | Keep the mixed round and starters A-D (`L10A-D`); drop the full build time: 3-minute showcase of an edited starter. Merging L9 into it was rejected because a data lesson cannot share one 90-minute slot with a showcase. |
| Spiral of holiday ideas | Terms 2-4 | Primes (lesson 25), negatives (lesson 22), nth term (lesson 23, 32), counting (31), probability (30), polygon turn (16), mod (24), mean (28). Each opens as a warm-up, not a reteach. |

Not reused: none of the 27 new lessons repeats a holiday lesson's objective. Code starters for lessons 10-36 are all new (about 18 coding lessons need a starter, section 6).

Coding strands by term: **A Test it with loops and variables** (T1: loop, variable, if, mod, list, Pen); **B Structure it** (T2: My Blocks with inputs, nested loops, 1000-trial simulation, scale a drawing); **C Python bridge** (T3: print, input, `for`, `if`, `def`, lists, turtle; every task also in Scratch); **D Build it** (T4: lists, recursion, simulation, spreadsheet, capstone). Python is optional in T3 and a free choice in T4.

## 4. Coverage check

MOE strand names and year placement are now verified (see the top block). Legend: M = main lesson, t = touched in a warm-up or tier, blank = not covered.

| MOE Primary 6 strand | T1 | T2 | T3 | T4 | Comment |
|---|---|---|---|---|---|
| Whole numbers (the four operations, factors, multiples) | t | | M (25) | | Contexts only; no drill |
| Fractions (x and / by fractions) | | M (11) | | | One lesson; school does far more |
| Decimals | | t (12, 14) | | | Not a P6 Standard strand (decimals are P4 and P5), so not a P6 gap |
| Percentage | | M (12) | | t (28) | School practice outpaces us (multi-step, GST, discount chains) |
| Ratio | | M (10) | t (23) | | Same |
| Rate | | M (13) | M (23) | | Rate is P5; speed removed from the program |
| Algebra (letter, expressions, simple equations) | M (4) | | M (19-21) | | Strongest strand |
| Average (total = average x number) | | | | M (28) | Moved from holiday L9 |
| Pie charts and data | | | | M (28-29) | |
| Angles in geometric figures | M (7) | M (16) | | | |
| Area, perimeter, circles | | M (14, 18) | | | |
| Volume of cube and cuboid, nets | | M (15) | | | |
| Symmetry and transformations | | M (17) | M (22) | | |
| PSLE multi-step word problems and heuristics | t | t | t | M (34) | **School practice clearly outpaces us**; not a goal of this program |

Beyond primary (enrichment): negatives, primes, counting, probability, modular arithmetic, powers, binary, coordinates and straight-line graphs, logic and proof. Honest flags: no timed practice, no past-paper drill, only one lesson on each big P6 topic. Say "after the PSLE" or "alongside school", never "P6 maths" or "aligned to MOE" (audit wording rule).

Olympiad-type problem moves worked in (original problems only, no contest items copied; no Level 6 file exists, so verify against a SASMO Grade 5-8 file once one is added): try small cases (L1, L31); systematic listing with no double count (L5, L31); work backwards (L4, L34); supposition and heads-and-legs (L34); before-and-after bar model (L10, L12); parity and invariants (L33, L34); remainder cycles for "which day / last digit" (L8, L24); pigeonhole (L34); unit method (L10, L13); choose a variable and form an equation (L19-20); counterexample and "find all" (all Go further items). Contest-style Go further items are written fresh and kept tutor-private until released as practice.

## 5. Assessment and progress

**End-of-term check (10 questions, 25 minutes, in the buffer week or the first 25 minutes of lesson 9; no grade, no ranking):**
- Q1-5 Start here: familiar-context items parallel to the term's main ideas, no new vocabulary.
- Q6-8 Think harder: the same idea in a new setting.
- Q9 Go further: one "find all" or "is it always true?" item.
- Q10 Explain: "write one sentence on why" or "trace this code and say what it prints".

Topics per term: T1 sequence rule, factors, signed moves, machine backwards, counting, fair game, turn angle, clock sum, code trace; T2 ratio share, fraction of fraction, percent change, rate, circle, volume, angle chase, scale; T3 expand, solve, inequality, coordinates, graph, power, HCF/LCM, binary; T4 mean and outlier, scatter, tree, arrangement, recursion, logic, strategy. Mark each strand "secure / growing / not yet" and use it to plan support for the next term (and to decide the catch-up pack for late joiners).

**Parent report line per term (neutral, evidence based; no scores or predictions):**
- T1: "This term [Name] tested number patterns, primes, negatives, chance, angles and codes, in Scratch. [Name] showed [one observed example]. Next term we move to ratio, percent and shapes."
- T2: "[Name] worked on ratio, fractions, percent, rates, circles and volume through models. We noticed [one example]. Next term: algebra, graphs and a first step into Python."
- T3: "[Name] wrote rules with letters, solved equations, read straight-line graphs and tried [Scratch/Python]. We noticed [one example]. Next term: data, chance and a final project."
- T4: "[Name] built and presented [project title], explaining why it works. We noticed [one example]. Suggested next step: [Level / same level next year / a topic to try at home]."

## 6. Work to turn the plan into the full set

Per new lesson: tutor guide section, about 25 slides, 2 workbook pages plus Think harder pages, qbank (6 core, 8 stretch, 9 challenge), warm-up check, open investigation, reflection, and a Scratch (and from Term 3 Python) starter with answer key (tutor only). Every numeric answer and "find all" claim brute-force checked in Python, as in the audits.

| Term | Work | Rough effort |
|---|---|---|
| T1 | Re-time 8 lessons for one weekly slot; trim L10 into lesson 9; fix "average" wording and secondary-style tags from the audit; write term handout and Scratch warm-up | about 7-8 person-days |
| T2 | 9 new lessons, 4-5 new Scratch starters, scale-model synthesis | about 20 person-days |
| T3 | 9 new lessons, 6-7 Scratch starters plus Python versions, environment choice | about 22 person-days |
| T4 | 9 new lessons, 5 starters (reuse Mean Machine), capstone templates and rubric | about 20 person-days |
| All | Four end-of-term checks and answer keys, four parent reports, tier-map and syllabus-map entries, parent-facing term outline, tutor training | about 8-10 person-days |

Total about 75-80 person-days from a human-only baseline. These are guesses from the size of the holiday set (ten lessons, about 280 slides); a drafting tool can cut writing time, but checking answers, Scratch/Python testing in a real editor (not yet done for the existing `.sb3` files) and tutor review will not shrink much. Suggested order: T1 first (reuse), then T2 before the next intake, T3 and T4 on a rolling basis a term ahead.

## 7. Open questions for the owner

1. Who is the intake: children in P6 (PSLE written exams, usually Sept-Oct, fall in Term 3-4), children after PSLE only, or also Sec 1 (age 13)? Term 3 may clash with prelims; should it be lighter, with the Studio lesson optional?
2. Are Term 2 entries allowed (catch-up pack), or Term 1 only? Do 11-13 year olds need a gap term after the holiday course?
3. Python: which environment (offline editor, or a browser tool with no account) fits our no-accounts, nothing-uploaded rule?
4. How closely should Term 2 follow the MOE P6 syllabus (ratio, percent)? The PDF has been checked: ratio is P6 (p. 43). May we name PSLE on the page, and with what wording?
5. Is Term 1 L9 (data) moved to Term 4 acceptable, or keep the mean in Term 1 for continuity with the holiday course?
6. Which SASMO grade levels does ages 11-13 map to? A Grade 5-8 file is needed for section 4.
7. Homework and take-home work: expected weekly, or none?
8. Do parents get a placement diagnostic per term, or only the existing level diagnostic?
9. Word limits for the year: is 4 x 9 lessons with a buffer week fixed, or can Term 4 be 8 lessons if the term is short?
