# Level 6 term-time year plan (ages 11-13, maths + coding bridge)

## Revision for 10-week terms and new Term 1

Revised 2026-10-22 to match `docs/terms/owner_decisions.md` (owner decisions of 22 Oct 2026). Still a plan, not lessons; nothing here has been tried with children.

**What changed**

- **40 lessons, 10 per term** (was 36, 9 per term). One lesson is added to every term (below).
- **Term 1 is ten new lessons.** Holiday graduates start Term 1, so Term 1 no longer adapts the holiday course. The holiday course (`p6/content/l1.js` to `l10.js`; `docs/levels_and_placement.md`) stays a standalone foundation course. No term lesson reuses a holiday lesson, slide, workbook or Scratch starter. Holiday topics return only as the first 6-minute warm-up (section 3).
- **Lesson numbering is now 1-40.** Terms 2-4 keep their lessons and their order; only the numbers move (map below). Every lesson number in this file is the new one unless it says "old".
- **Contest-style items sit at Think harder**, with a harder Go further follow-up where useful. Moved up from Go-further-only: telescoping sums and unfolding a continued fraction (lesson 12); trains passing each other (14); factorial trailing zeros (27); counting triangles by size and rearrangements with nobody in their own place (34); pigeonhole, unattainable totals (two pack sizes) and the repeated-move cycle (37). Already at Think harder and kept there: digit-sum tests (5), pairing sums (4), gaps and posts (6), rounding intervals (1), last digits (26), cryptarithm (36), worst case (37), chance (33, with Start here limited to listing outcomes). No contest-style item is at Start here.
- **Mid-year joiners**: each term has a one-line "Can a new child join cold?" note and an exam-period "safest to skip" note. The added lesson of each term is built to be stand-alone: nothing later depends on it.
- **Speed** stays only as the owner-approved Level 6 enrichment preview in lesson 14, labelled secondary-school.
- The "Revision after SASMO review" and "Verified against MOE syllabus" blocks below are kept with the new numbering. The effort estimate (section 6), assessment (section 5) and open questions (section 7) are refreshed.

**Old to new lesson numbers**

| Old (36-lesson plan) | New (40-lesson plan) |
|---|---|
| 1-9 (Term 1, adapted holiday) | Replaced by new lessons 1-10. Old 2 (digit tests) survives as new lesson 5. Old 1, 3-9 are holiday-only topics now. |
| 10-17 | 11-18 |
| 18 (Scale Models) | 20 |
| 19-26 | 21-28 |
| 27 (Term 3 Studio) | 30 |
| 28-34 | 31-37 |
| 35-36 (Capstones) | 39-40 |
| (added) | 9, 19, 29, 38 |

**The four added lessons.** Each is a real lesson with the three tiers (tables in section 2). They take the best remaining gaps from the "Gaps left" list and `docs/sasmo/g6_analysis.md`:

| Lesson | Title | Why this one |
|---|---|---|
| 9 (Term 1) | Tiling, Bounds and Overlaps | Packing and tiling bounds (15-14, 20-5), overlapping-square dissection (19-23) and a taste of similar triangles (20-23): four items that had no home, one idea (an area count can prove something impossible). |
| 19 (Term 2) | Mixtures, Fair Shares and Best Buys | Equal sharing of a total (15-18), mixed solutions (21-14) and best value from bundles (21-10): all gap or part-gap items that rest on "track the total first", a Term 2 synthesis of ratio, percent and rate. |
| 29 (Term 3) | Reachable Numbers and Rule Grids | Number pyramids and picture-rule grids (22-6, 19-15), consecutive sums (22-13, positive whole numbers only), calculator-key puzzles (21-6, with the keys fully specified). **Thinnest evidence of the four** (five single items); if the owner prefers, swap it for a plain Term 3 problem-solving studio. |
| 38 (Term 4) | Seeing Solids | The five spatial items (19-3, 20-9, 21-3, 21-5, 22-2), all Section A where a wrong answer costs a mark. Gets a full lesson so lesson 16 can stay light. It sits before the two capstone lessons so the project pair stays together. |

## Revision after SASMO review

Revised 2026-10-22 against `docs/sasmo/g6_analysis.md` (five Grade 6 papers, 2015 and 2019 to 2022, 125 problems; type counts below are from its section 3) and the MOE checks in `docs/moe/verification_report.md` and `docs/moe/syllabus_by_level.md`. Rules kept: every verified MOE placement unchanged; contest work sits in Think harder (with a harder Go further follow-up), and Start here stays core and approachable. No contest problem is copied. Items from `docs/sasmo/g6_original_problems_draft.md` are named only as **candidate practice** (draft, untried with children, tutor-private until reviewed). The Python and Scratch coding strand (section 3 and the code ideas in each row) is kept, and each change below keeps or adds a small program.

**Numbering.** The table was written against the old 1-36 numbering. **The plan now runs 1-40** (10 lessons a term, see the top section). The first column gives the new number with the old one in brackets. The 36-lesson wording "no lesson moved between terms" still holds for Terms 2-4: only the numbers shifted.

### Lessons changed (new number (old) -> what, why, evidence)

Evidence counts are problems in the five papers (of 125).

| Lesson | Old -> new, why, evidence |
|---|---|
| 5 (2) | Prime Hunters and Digit Tests -> **Divisibility Detectives**, a new Term 1 lesson (primes are holiday-only now and are not reused). Digit-sum tests for 3 and 9, "45 means 5 and 9" and a filter-with-mod program, at Think harder and Go further. Divisibility tests were a real gap. 5 test items in 4 papers (15-7, 19-8, 20-8, 21-9, 21-25); candidate practice: draft section 1 |
| 12 (11) | Go further widened: telescoping sums, unfolding a continued fraction, biggest value from digit boxes (was product only). **Now telescoping sums and the continued fraction sit at Think harder**, the harder forms at Go further. 6 nested-fraction items (15-10, 19-17, 20-18, 21-8, 21-13, 22-14) |
| 14 (13) | Rate and Speed Stories -> Rates, Work and Trains. Combined rate (pipe and leak, two workers), trains with length, opposite and same direction. **Speed kept as owner-approved enrichment preview**, labelled secondary-school. Trains passing in opposite directions now at Think harder. 9 items (15-15, 15-18, 19-10, 19-22, 20-7, 20-21, 21-10, 21-12, 22-20) |
| 16 (15) | Volume and Nets -> Volume, Nets and Views. A light "seeing in 3D" step (top view of a block stack, dice opposite faces). The heavier spatial items (rotations, touching dice, edges, painted cubes) now live in lesson 38. 5 items (19-3, 20-9, 21-3, 21-5, 22-2) |
| 17 (16) | Angle Chasing: clock-hand angles as a warm-up and S/T item (6 degrees and 0.5 degrees per minute). 2 items (19-12, 20-15) |
| 20 (18) | Scale Models and Same-Height Triangles: triangles on the same base and height (T and G). Perimeter by sliding sides **moved to lesson 7** (new Term 1 area and perimeter lesson). 3 area-dissection items (19-23, 21-24, 22-22), supporting 15-20, 20-13, 22-3 |
| 21 (19) | Letters and Brackets: difference-of-squares shortcut and "factor out the common number" as a recurring 5-minute opener (T and G). The arithmetic form is first met in lesson 4; here it is the algebra form. 2 explicit (20-1, 21-1), 7 computation items in all |
| 26 (24) | Powers and Roots: last digit of powers at Think harder, last two digits at Go further. The remainder cycle is taught from scratch in the lesson (the holiday clock lesson is only a warm-up). 6 last-digit and zeros items (15-4, 15-17, 15-25, 20-12, 20-16, 21-16) |
| 27 (25) | Factors, HCF and LCM: trailing zeros of a product **and of a factorial at Think harder** (count 2s and 5s); LCM of lap times; the sum-of-two-factorials form at Go further; link back to the lesson 5 tests (15-17, 20-12, 19-22) |
| 31 (28) | Statistics That Mislead: bar chart with no scale numbers (read the gridline unit) in S and T. 3 items (20-6, 22-17, 21-24) |
| 34 (31) | Counting with Constraints: counting figures by size and rearrangements with nobody in their own place; **both start at Think harder** with a small case, the larger figure and five gifts at Go further. 7 items (15-8, 19-4, 19-16, 20-17, 22-15, 22-16, 22-24) |
| 36 (33) | Logic and Proof -> Logic, Proof and Digit Puzzles. Cryptarithms (leading digit first, then carries, brute-force check in code) in T and G. 5 items, one in every paper since 2019 (19-24, 20-24, 21-22, 21-23, 22-21) |
| 37 (34) | Olympiad-Style Workshop: worst-case counting, unattainable totals with two pack sizes, a repeated-move cycle and pigeonhole, **now all at Think harder** with invariants and harder cases at Go further. 5 items in 2019 to 2022 (19-21, 20-3, 20-22, 21-19, 22-18) |

Lessons with no change from the SASMO review (old numbers in brackets): 11 (10), 13 (12), 15 (14), 18 (17), 22-25 (20-23), 28 (26), 30 (27), 32 (29), 33 (30), 35 (32), 39-40 (35-36). The analysis found sequences, algebra, counting basics, remainders, ratio, percent and circles already matched. Old lessons 1, 3, 4, 6-9 were holiday lessons; they are no longer part of the term plan.

### Gaps left unaddressed, and why

- **Homed by the four added lessons:** packing and tiling bounds (15-14, 20-5), overlapping-square dissections (19-23) and similar triangles (20-23) in lesson 9; number-pyramid and grid rules (22-6, 19-15), consecutive sums (22-13) and calculator presses (21-6) in lesson 29; equal sharing of a total (15-18) and mixtures (21-14) in lesson 19; spatial items in lesson 38. Rounding intervals (15-9) are a Think harder item in lesson 1.
- **Still thin:** single-occurrence items inside those lessons (one or two per paper) prepare the type but do not train it. 22-13, 21-6 and 22-24 have ambiguities in the source; our versions fix the rules ourselves.
- **Exam technique** (option elimination, negative marking, four-digit answer grid): not maths, and ruled out for post-PSLE children by the Level 6 SPEC.
- **The contest is Grade 6 only.** Level 6 spans ages 11-13, so the weights may differ for Grade 7; no Grade 7 file exists.
- **Limit of the change:** each gap-type has a home as a tier item or one lesson, so the plan prepares the contest types, it does not train them.

## Verified against MOE syllabus (Oct 2025)

Every MOE statement below was checked against the official PDF (`docs/moe/syllabus_by_level.md`; PDF page numbers). Rows for Terms 2-4 keep their earlier checks with the new lesson numbers. Rows for the **new Term 1 lessons** were added in the 22 Oct 2026 rework and checked against the same file; any statement not found there is marked [to verify]. Secondary 1 and 2 placements are not in the primary syllabus and remain unconfirmed.

| Lesson | Was | Now (page) |
|---|---|---|
| 1 Big and Small Numbers (new) | none | Place value, comparing and rounding to the nearest 10, 100 or 1000 are **P4** (p. 37); decimals to 3 places, comparing and rounding to a whole number, 1 or 2 places are P4 (p. 38); multiplying and dividing by 10, 100, 1000 and numbers to 10 million are **P5** (p. 41). "Largest or smallest number that rounds to a given value" is our contest-style extension, not a syllabus outcome. |
| 2 Fractions on the Number Line (new) | none | Equivalent fractions, simplest form and comparing unlike fractions (denominators up to 12) are **P3** (p. 35); mixed numbers and improper fractions are **P4** (p. 37). A fraction between two fractions is not stated. |
| 3 Three Names for One Number (new) | none | Decimal-fraction conversion (denominator a factor of 10 or 100) is **P4** (p. 38); fractions as decimals by division and "a part as a percentage" are **P5** (p. 41). Repeating decimals are not in primary. |
| 4 Number Shortcuts (new) | none | Order of operations and brackets are **P5** (p. 41); the syllabus does not list "order of operations before P5". Mental strategies such as compensation and pairing sums are not listed. [to verify the wording of any mental-calculation outcome before it goes on a page] |
| 5 Divisibility Detectives (new; old 2) | "primes are a secondary topic [to verify]" | Confirmed earlier: **"prime" appears nowhere in the primary syllabus**, so primes are holiday enrichment and are not taught here. Factors and multiples, testing whether a 1-digit number is a factor of a number within 100, and common factors are **P4** (p. 37). Digit-sum tests for 3 and 9 and "45 means 5 and 9" are beyond that. |
| 6 Rules That Look Back (new) | none | Number-sequence patterns are **P1 to P4** (pp. 31-37), not P5 or P6. Rules from the previous term, interleaved sequences and period are enrichment. |
| 7 Area and Perimeter Puzzles (new) | none | Perimeter of a rectilinear figure is **P3** (p. 36); missing side from area or perimeter and composite figures of rectangles and squares are **P4** (p. 39); triangle composites **P5** (p. 42). Fixed-perimeter greatest-area is not stated. |
| 8 Fractions of a Quantity (new) | none | Fraction as part of a set is **P4** (p. 37); multiplying a fraction by a whole number **P5** (p. 41). "Fraction of what is left" chains are word-problem practice; the syllabus lists no such outcome. |
| 9 Tiling, Bounds and Overlaps (new) | none | Area of rectangles and squares P3-P4 (pp. 36, 39), composite figures P4 (p. 39). Packing bounds, overlaps by add-and-subtract and similar triangles are not in primary (similar triangles are secondary). |
| 11 Ratio Recipes (old 10) | "Ratio (Number P6)" | Confirmed P6 (1.1 to 1.7, p. 43); the syllabus **excludes ratios involving fractions and decimals**. |
| 12 Fractions of Fractions (old 11) | "x and divide (P5/P6 [to verify])" | Fraction x fraction is **P5** (p. 41). Dividing a proper fraction by a whole number and a whole number or proper fraction by a proper fraction are **P6** (1.1, 1.2, p. 43). Dividing by an improper fraction or mixed number is not listed. |
| 13 Percent Change Detective (old 12) | "P6 [to verify]" | Percentage increase/decrease and finding the whole are **P6** (p. 43). Discount, GST and annual (simple) interest are P5 (p. 41). Repeated change and compound growth are beyond primary. |
| 14 Rates, Work and Trains (old 13) | "speed moved out of P6 in 2021 [to verify]" | **"Speed" is in no primary year.** Rate is P5 (p. 41). Speed, average speed and distance-time graphs are secondary. Speed items are labelled secondary-school (owner-approved enrichment). |
| 15 Circles and Pi (old 14) | "P6" | Confirmed P6: circle area and circumference, semicircle, quarter circle and composite figures (p. 44). |
| 16 Volume, Nets and Views (old 15) | "surface area (P6; nets P4 [to verify])" | Nets are **P4** (p. 39). Volume of cuboid is **P5** (p. 42); P6 adds only inverse problems (dimension, edge of a cube, height from volume and base area, face area, p. 44). **Surface area is not in the primary syllabus.** |
| 17 Angle Chasing (old 16) | "(P6 and Sec 1 [to verify])" | Angles on a line, at a point, vertically opposite and triangle sum are **P5** (p. 42); composite-figure angles P6 (p. 44). Angles between parallel lines (transversals) are not in primary. Polygon angle sums are not in primary (revisited as a warm-up only). |
| 18 Symmetry and Transformations (old 17) | "Hong Kong P6 rotational symmetry; secondary" | Line symmetry is **P4** (p. 39). Rotation, translation, tessellation and rotational symmetry are not in primary. |
| 22 Equations on a Balance (old 20) | none | Letters, simple expressions and simple linear equations with whole-number coefficients are **P6** (Algebra 1.1 to 1.5, p. 43); brackets are excluded (1.3); unknown on both sides is not stated. The holiday "Algebra Machines" is the same P6 material, a warm-up here only. |
| 26 Powers and Roots (old 24) | "(Sec 1)" | Only the use of the square-root and cube-root signs, for a side from an area and an edge from a volume, is P6 (2.5, p. 44); powers are not named. |
| 27 Factors, HCF and LCM (old 25) | "Sec 1 [to verify]" | Common factors and common multiples are **P4** (p. 37); the names HCF and LCM and prime factorisation are not in primary. |
| 31 Statistics That Mislead (old 28) | "pie P4 [to verify]" | Confirmed **P4** (p. 40); average **P6** (p. 44); median, mode, scatter plots not in primary. |
| Holiday topics used only as warm-ups | (old rows for lessons 1-4, 7) | Number-sequence patterns P1-P4; nth-term formulas not in primary; letters P6 (Algebra 1.2, p. 43); negative numbers and primes in no primary year; polygon angle sums not in primary. Unchanged, kept for the warm-up list in section 3. |
| Coverage table | "Decimals: **Gap**: no decimal lesson" | P6 Standard has **no Decimals strand** (decimals are P4 and P5), so this is not a P6 gap. Term 1 now has two decimal lessons (1, 3). |
| Coverage table | "Rate and speed ... Speed may be secondary now [to verify]" | Rate is P5; speed is in no primary year. |

Syllabus outcomes the plan misses or only touches: P6 fraction division with a whole number or proper fraction as a skill (lesson 12 is one lesson); the inverse volume problems (16 touches); percentage of "find the whole" (13 touches); algebra notation "a ÷ 3 or a/3" and simplifying simple expressions (21, 22). Things we teach that are not in the syllabus at any primary year: sequences with recurrence rules, digit-sum tests, negative-number coordinates, counting rules, probability, remainder cycles, ciphers, scale factors, inequalities, coordinates, linear graphs, binary, scatter plots, logic and proof, surface area, transformations, packing bounds.

Draft for the owner, 2026-10-22. This is a plan, not lessons. Nothing here has been tested with children. MOE year placements are taken from `docs/audit/moe_alignment_p4_p6.md`, which has been verified against the official syllabus PDF (see the verified block above). The olympiad-type list in section 4 comes from the Grade 6 SASMO analysis (`docs/sasmo/g6_analysis.md`); a Grade 7 analysis does not exist.

Format: 4 terms x 10 lessons x 90 minutes (40 lessons a year), live online, groups of up to 8, one lesson a week. A school term is about 10 weeks, so there is no spare week: public-holiday slips and a short Term 4 are covered by the recording, make-up days, and the stand-alone lesson named in each term (the lesson to skip). Do not hardcode dates; check each year's MOE calendar. Places open every term; a joiner pays a prorated fee for the lessons left (`owner_decisions.md`).

## 1. Design principles

- **The year has one arc: Build the number toolkit, Scale and compare, Generalise with letters and code, Model and decide.** Term 1 (all new) asks "what is this number made of, and how do I compare it?" (place value, fractions, decimals, percent, divisibility, sequences, area); Term 2 "how do quantities scale together?" (ratio, percent change, rate, circles, volume); Term 3 "how do we say it for every case?" (algebra, graphs, powers, factors, binary); Term 4 "what can we trust?" (data, chance, logic, a capstone build).
- **Spiral by new setting, never by repeat.** Each Term 2-4 lesson opens with a 6-minute "remember" warm-up, which is the only place an earlier lesson or a holiday topic is revisited (section 3). The Think harder tier is where an earlier idea returns on purpose. **No lesson assumes an earlier term except through that warm-up**, so a child can join at the start of any term.
- **Problem solving is taught as named moves.** Term 1 introduces moves informally (try small cases, make a table, draw a model, work backwards). Term 2 names them (before-and-after model, unit method, supposition). Term 3 adds "write it as an equation" and "check by brute force in code". Term 4 adds proof-like moves (counterexample, parity, work backwards, pigeonhole) and a free choice of tool. Each term ends with a mixed lesson where the child picks the move.
- **Inquiry is built up in three steps.** Term 1: notice and test given examples. Term 2: ask "what if I change this number?" and record what changes and what stays the same. Term 3: pose your own question and test it by hand and in code. Term 4: choose a question, plan, build, test, explain why, present (capstone, lessons 39-40).
- **Coding is a thinking tool, never the goal.** The maths comes first and code is how we test it. The code strand and tier labels are in section 4 and keep the holiday rule: small programs, block names from the official Scratch 3 palette, our own block drawings, no accounts, nothing uploaded. Python arrives in Term 3 as a bridge, always with the Scratch version beside it.
- **Tiers follow the program principle.** Start here = core, approachable without being taught first. Think harder = the taught idea in a new setting, **and where contest-style items sit** (digit-sum tests, pairing sums, gaps and posts, chance, cryptarithms, worst-case counting and similar), never Start here and never only Go further. Go further = mastery plus extension, including "find all", "is it always true?" and "make up your own". Labels stay neutral (no gifted wording, no ranking). Any contest-style items are our own originals; tutor-only solution notes and Scratch answer keys never go to families. This is not PSLE drill, and we do not promise exam results.
- **Speed stays out of the primary-style work.** The only speed content in the year is the owner-approved, secondary-labelled enrichment in lesson 14.

## 2. Term-by-term lessons

Tier lines: S = Start here, T = Think harder, G = Go further. MOE strand names follow section 4. **(+)** marks the lesson added by the 10-week rework. Each term ends with a "Can a new child join cold?" line and an "Exam period" line.

### Term 1: Build the number toolkit (10 new lessons)

All new. Holiday graduates start here, so nothing adapts a holiday lesson: each warm-up may revisit one holiday topic for 6 minutes and then the lesson moves to a different topic or a deeper treatment (section 3). Order follows the MOE strands a child needs before Term 2 (numbers, fractions, decimals and percent, then area, then fraction word problems).

| No | Title and big idea | Topics (strand; other countries) | Tiers (one line each) | Thinking skill |
|---|---|---|---|---|
| 1 | Big and Small Numbers: place value tells you how big | Place value to millions and 3 decimal places, x and / by 10, 100, 1000, rounding (Number P4-P5; rounding intervals are contest-style); `round`, `join`, digit-by-digit in a loop | S: read, write and compare numbers with decimals on a place-value chart; what x10 does to each digit. T: round to 10, 100 and 0.1; the smallest and largest numbers that round to a given value; biggest and smallest from digit cards. G: estimate a sum by rounding and say whether it is too high or too low; when does round-then-add differ from add-then-round? | Estimating |
| 2 | Fractions on the Number Line: every fraction has a home | Equivalent fractions, comparing unlike fractions, mixed numbers and improper fractions, benchmarks 0, 1/2, 1 (Number P3-P4); compare two fractions by a loop | S: fold paper and place fractions on a line; equivalent fractions by folding. T: order five unlike fractions by benchmark and by common denominator; find a fraction between two others. G: list every fraction in lowest terms with denominator up to 6 between 0 and 1, in order; is the "mediant" of two fractions always between them? | Comparing |
| 3 | Three Names for One Number: fraction, decimal, percent | Convert among fraction, decimal and percent (Number P4-P5); fractions that end and fractions that repeat (not in primary); long-division program | S: 1/2, 1/4, 1/5, 3/4 on a hundred grid as decimal and percent. T: order a mix of forms and pick the smallest; 1/8 and 3/8 by division; 1/3 and 1/7 by long division and the repeating block. G: for which n up to 30 does 1/n end? why does 1/7 repeat after 6 digits at most? | Translating |
| 4 | Number Shortcuts: spot the structure | Mental strategies, order of operations and brackets (Number P5; pairing sums and "multiply by 999" are contest-style); loop that checks a shortcut on many numbers | S: compensation (x 99, + 101), splitting and recombining, making tens. T: pairing sums (1 + 2 + ... + 100, and with an odd count); factoring out a common number (such as a decimal shared by every term); x 999 as x 1000 minus x 1. G: say why a shortcut works with a picture; invent a calculation that has a shortcut | Seeing structure |
| 5 | Divisibility Detectives: the digits can tell you the factors | Factors, multiples, tests for 2, 5, 10 (Number P4); digit-sum tests for 3 and 9, "45 means 5 and 9" (enrichment, contest-style); filter with `mod` and digit sum | S: tests for 2, 5, 10 and the last two digits for 4; sort numbers by which tests they pass. T: digit-sum tests for 3 and 9 and why they work; 6, 12 and 45 as combinations; fill the missing digit so a number passes. G: smallest number that uses every digit once and is a multiple of 45; digit-box puzzles with two blanks; "is it always true that ...?" | Using structure |
| 6 | Rules That Look Back: the next term depends on the last | Sequences with a rule from the previous term, interleaved sequences, repeating periods, gaps and posts (Number; sequences are P1-P4, the rest enrichment); list-building loop | S: continue a growing pattern; find the difference; gaps that grow 1, 2, 3, .... T: rule from the previous term (times 2 minus 1); two interleaved rules; the 100th term of a repeating pattern; fence posts versus gaps. G: a sequence whose gaps are the squares; where a number appears n times, which term is the 100th? | Generalising |
| 7 | Area and Perimeter Puzzles: the same fence, a different field | Area and perimeter of rectangles, squares and rectilinear figures, composite figures, perimeter by sliding sides (Measurement P3-P4); loop through all rectangles of one area | S: perimeter of a staircase shape by sliding the sides; split a composite shape into rectangles. T: same perimeter, different areas; fixed perimeter, greatest area (table); missing side from area; four rectangles in two layouts, which has the longer perimeter? G: which rectangle of area 36 has the least perimeter, and is a square always best? | Comparing measures |
| 8 | Fractions of a Quantity: draw the bar, then work backwards | Fraction of a set, fraction of what is left, working backwards (Number P4-P5); bar model; loop that takes a fraction of the remainder | S: fraction of a set with a bar. T: spend 1/4 then 1/3 of the rest; work backwards from what is left; the smallest total so that every fraction is a whole number. G: a chain of three "fraction of the rest" steps run backwards; make up a story with a whole-number answer | Modelling with bars |
| 9 | (+) Tiling, Bounds and Overlaps: an area count can prove it is impossible | Packing and tiling bounds, overlapping squares by add and subtract, nested triangles by scale (Measurement; bounds are contest-style, not in primary); program that counts tile positions | S: tile a floor with 1 x 2 and 2 x 2 tiles and count by area. T: the area bound (how many 2 x 4 cards from a 5 x 7 sheet at most?) and then build it; two overlapping squares, shaded part = A + B - overlap. G: a case where the area bound is not reached and why (colouring); a small triangle inside a big one with parallel sides, area ratio | Bounding |
| 10 | Term 1 Studio: build a number toy | Mixed round of 1-9; a small program (a quiz, a converter, a puzzle checker), tested by hand first | S: change one number in a working starter and predict. T: add a loop and a test to the starter. G: add a rule so the puzzle has exactly one answer, and explain | Choosing a move |

**Can a new child join cold?** Yes. Term 1 needs only P5 arithmetic and fractions. The 6-minute warm-ups revisit holiday topics (lesson 5: factor trees; 6: nth term; 8: function machines run backwards; 3: remainders and clock wrap) as short reminders with a one-line card for a child who never took the holiday course.

**Exam period.** Safest to skip or make up (recorded, or a holiday class): **lesson 9**. It is stand-alone; lesson 10 uses only 1-8.

### Term 2: Scale and compare (ratio, fractions, percent, rate, shape)

All new. This is where Level 6 touches P6 strands, as reasoning lessons, not drill. Lessons keep their order; numbers moved up by one (old 10-17 are 11-18).

| No | Title and big idea | Topics (strand; other countries) | Tiers | Thinking skill |
|---|---|---|---|---|
| 11 | Ratio Recipes: parts, not amounts | Ratio, equivalent ratios, a:b:c, sharing in a ratio (Number P6); bar models; Sec 1 ratio | S: share with counters in 1:3. T: same amount added to both parts (what stays the same). G: three-way ratio, one given difference; make up a ratio puzzle with one answer | Modelling with bars |
| 12 | Fractions of Fractions: area models, then nested and telescoping | Fraction x fraction (P5); division by a whole number or proper fraction (P6); Singapore model drawing | S: fold paper for 1/2 of 1/3. T: divide a fraction by a whole, then by a fraction, by picture; unfold a continued fraction from the bottom; a short telescoping sum 1/(1 x 2) + 1/(2 x 3) + .... G: telescoping product 1/2 x 2/3 x ... and the sum 1/(n(n+2)); biggest value from digit boxes; why does dividing by 1/2 double? | Visualising |
| 13 | Percent Change Detective: up 20 then down 20 | Percentage: discount, GST, interest (P5); increase and decrease, find the whole (P6); repeated change is beyond primary; compound loop in code | S: 10% and 25% of a price with a grid. T: find the original after a discount. G: +20% then -20%, is it back to start? Interest over 10 years | Spotting hidden wholes |
| 14 | Rates, Work and Trains | Rate (P5, revisited); combined rate (pipe and leak, two workers), trains with length; speed, average speed, distance-time graphs. Speed is not in the primary syllabus (MOE Oct 2025); **kept as owner-approved enrichment, labelled a secondary-school preview** because rate or speed appears in all 5 SASMO papers | S: rate as amount per unit (P5); read a distance-time picture. T: meet-in-the-middle journeys; two diggers or a tap and a leak, add the rates; a train through a tunnel; two trains passing in opposite directions (add the speeds). G: trains going the same way; average speed there and back; steeper line means? | Comparing change |
| 15 | Circles and Pi: measure it, then estimate it | Circumference and area of circles (P6; Hong Kong P6 pi); estimate pi with random dots in code | S: measure round objects at home, find the ratio. T: composite shapes with semicircles. G: why is area ~ 3.14 r x r? dart-throwing estimate (the random-number block is taught in the lesson) | Estimating |
| 16 | Volume, Nets and Views: cubes in boxes | Volume of cube and cuboid (P5; inverse problems P6), nets (P4), surface area (not in primary); top view of a block stack and dice opposite faces (views not named in primary); rotations, touching dice and painted cubes are in lesson 38 | S: build a cuboid from 24 cubes, list all. T: water level rises; pour between tanks; draw the top view of a block stack; dice with opposite faces summing to 7. G: find an edge from a volume; same volume, least surface | Seeing in 3D |
| 17 | Angle Chasing (and clock hands) | Angles in geometric figures: lines, triangles, parallel lines (P5 for lines, points and triangles; P6 for composite figures; parallel-line angles not in primary); clock-hand angles (enrichment); turtle spiral | S: angles on a line and at a point; the angle between clock hands on the hour. T: isosceles and exterior angle puzzles; hands move 6 and 0.5 degrees a minute, so the angle at 3:20. G: a chase needing two steps and a proof sentence, using the polygon turn (360 / sides, re-taught in the warm-up); when do the hands first overlap after 6 o'clock? | Chaining deductions |
| 18 | Symmetry and Transformations | Symmetry, reflect, rotate, translate, tessellate (Hong Kong P6 rotational symmetry; secondary); My Block with an input | S: fold and mirror shapes. T: rotation of order n. G: which regular shapes tessellate, and why (angle sum) | Visualising change |
| 19 | (+) Mixtures, Fair Shares and Best Buys: track the total first | Mixed solutions and concentration (percent P5-P6), equal sharing of a total (spare-tyre wear), best value from bundles (Rate P5); loop over bundle combinations | S: price per unit, which pack is cheaper; salt as a percent of a salt-and-water mix. T: mix two solutions (total salt over total mass); five tyres share the wear of one trip; stamp bundles for the best income. G: how much water to add to reach 10%; make up a fair-share puzzle with one answer | Tracking a total |
| 20 | Scale Models and Same-Height Triangles: lengths, areas, volumes | Scale factor: perimeter x k, area x k x k, volume x k x k x k (ratio, area, volume); triangles on the same base with the same height (triangle area P5); program that scales a drawing; mixed round | S: enlarge a shape on grid paper by 2. T: cost of paint when the model doubles; shade a triangle in a rectangle and slide its apex along a line (area stays). G: predict then check area and volume factors; cut a shape into same-height triangles to find a shaded fraction; find a surprising case | Synthesising |

**Can a new child join cold?** Yes. The 6-minute warm-up covers equivalent fractions, fraction of a quantity, fraction-decimal-percent, and area of a rectangle (a one-page bar-model card is sent). Lesson 11 starts from counters, not from earlier ratio.

**Exam period.** Safest to skip or make up: **lesson 19** (stand-alone; lesson 20 does not use it).

### Term 3: Say it for every case (algebra, graphs, powers, factors, binary; Python bridge)

All new. Python starts here, always next to the Scratch version. Old 19-26 are 21-28; old 27 (Studio) is 30.

| No | Title and big idea | Topics (strand; other countries) | Tiers | Thinking skill |
|---|---|---|---|---|
| 21 | Letters and Brackets: area models and shortcuts | Simplify, substitute, expand a(b + c) with rectangles (Algebra P6; expand is Sec 1); shortcut openers: factor out a common number, square minus its neighbours' product (the arithmetic form of these is met in lesson 4); Python intro: print, variable, input | S: area of a split rectangle, numbers only. T: write and expand 3(n + 2); factor out the common number to speed a sum. G: are two expressions always equal? test, then prove with area; why n x n minus (n - 1)(n + 1) is always 1 | Generalising |
| 22 | Equations on a Balance | Solve linear equations, unknown on both sides (P6 simple; both sides Sec 1-2); `for` and `if` to check by brute force | S: balance picture with weights. T: two-step and both-sides. G: build an equation with a given answer; why brute force needs a limit | Keeping it balanced |
| 23 | At Least, At Most | Inequalities, number-line solution sets, integer solutions (Sec 1); list solutions with a loop | S: "at least 5" on a line. T: solve 2n + 1 < 15, count whole solutions. G: smallest n so that plan A beats plan B | Describing a set |
| 24 | Maps with Numbers | Coordinates, four quadrants (Sec 1; Hong Kong, Australia earlier); distance, shapes, reflection; turtle `goto`; negative numbers on an axis are introduced in the warm-up | S: plot and name points. T: find the fourth corner of a shape. G: reflect across a line, find the rule for (x, y) | Linking algebra and geometry |
| 25 | Straight-Line Stories | Linear graphs from tables, gradient as rate, intersection (Sec 1-2); warm-up revisits rate (lesson 14) and sequences (lesson 6) | S: plot a table of a taxi fare. T: read the gradient and starting value. G: when do two plans cost the same? what if the lines are parallel? | Reading a graph |
| 26 | Powers and Roots | Squares, cubes, powers, square roots of perfect squares (Sec 1); doubling vs adding growth; remainder cycles taught here | S: square numbers from dot patterns. T: 2 to the 10th by doubling; compare growth; last digit of powers by finding the cycle. G: last two digits of a product or power; number of ancestors | Seeing growth |
| 27 | Factors, HCF, LCM and Trailing Zeros | HCF and LCM by lists and prime factorisation (common factors and multiples are P4; the HCF/LCM names and prime factorisation are not in primary); gears, lap times and meeting problems; zeros at the end of a product or factorial (count 2s and 5s); Euclid's method in code | S: common factors of 12 and 18 by lists. T: LCM for two buses or two runners on a lap; zeros at the end of a product and of a factorial, by pairing 2s and 5s. G: zeros at the end of a sum of two factorials; HCF with Euclid; why does the method stop? | Using structure |
| 28 | Binary and Twenty Questions | Binary numbers, place value in base 2 (not MOE; school computing); binary search | S: count to 15 with 4 switches. T: convert both ways. G: guess 1 to 100 in 7 questions, why 7? | Representing |
| 29 | (+) Reachable Numbers and Rule Grids: what can you make, and what is the rule? | Number pyramids and picture-rule grids, consecutive sums of positive whole numbers, calculator-key puzzles with the keys fully stated (not in primary; evidence is five single items); brute-force check in code | S: fill a number pyramid from the known cells; name each feature of a grid and its rule. T: which numbers can be written as a run of consecutive positive numbers; reach a target using only the keys +3 and x2 (our own rules, fully stated); a picture-rule grid. G: which numbers can never be made with the keys, and why; a pyramid with a missing top | Finding the rule |
| 30 | Term 3 Studio: build a puzzle maker | Mixed round of 21-29; a short Python or Scratch puzzle program, with a check by hand | S: change a working template. T: extend with a loop and a test. G: add a rule that makes the answer unique; explain | Choosing a move |

**Can a new child join cold?** Yes. The warm-up covers unit rates and reading a bar model, a letter as the unknown ("a number machine run backwards"), and the number line below zero. Python is introduced from nothing in lesson 21, so this is a good term for a child new to coding (the Scratch version always sits beside it).

**Exam period.** Safest to skip or make up: **lesson 29** (stand-alone; the Studio, lesson 30, uses 21-28 only).

### Term 4: What can we trust? (data, chance, logic, capstone)

All new, with the warm-up as the only link back. Children who finish PSLE before this term can run longer builds; see section 7. Old 28-34 are 31-37; old 35-36 are 39-40.

| No | Title and big idea | Topics (strand; other countries) | Tiers | Thinking skill |
|---|---|---|---|---|
| 31 | Statistics That Mislead | Average (taught from scratch, total = average x number), pie charts, line graphs, misleading scales (average P6; pie charts and line graphs P4); mean, median, outlier (warm-up may revisit the holiday data lesson, in new data); list program | S: average as a fair share; read a pie chart and a bar chart, including one with no numbers on the scale (find the unit from a given bar). T: how one extreme value moves mean and median; percent from a bar chart by gridline units. G: redraw a graph so it misleads; spot the trick | Critical reading |
| 32 | Scatter and Spreadsheets | Scatter plots, correlation vs cause (Sec 2-3; US G8); class data collected in a spreadsheet | S: plot pairs of data. T: describe a trend, predict. G: two things move together, give a third cause | Questioning data |
| 33 | Two-Stage Chance | Tree diagrams, independent events, expected value (Sec 2); Monty Hall simulation; the random-number block and "fair or unfair" are re-met in the warm-up | S: list the outcomes of two coins on a tree (no chances yet). T: the chance of both, one or neither. G: Monty Hall, simulate then explain | Predict then simulate |
| 34 | Counting with Constraints | Arrangements, selections, counting figures by size (triangles, rectangles), rearrangements, Pascal's triangle (not in primary curricula); nested loops | S: arrange 3 books by listing in order. T: with repeats; teams from a class; count rectangles in a small grid by size; triangles in a small figure by size; rearrangements with nobody in their own place (3 and 4 things). G: triangles in a larger figure; five gifts, nobody gets their own; Pascal row sums, route counts | Systematic counting |
| 35 | Patterns That Grow | Triangular numbers, Fibonacci, recursion (warm-up revisits lesson 6; not MOE); recursive count in code | S: stack squares and balls. T: find the rule from the previous term. G: closed form for triangular numbers; why 2 numbers apart | Recursion |
| 36 | Logic, Proof and Digit Puzzles | Venn diagrams, logic grids, true/false, counterexample, parity, cryptarithms (not MOE primary; Hong Kong enrichment) | S: logic grid with 3 children. T: Venn with overlap; a one-line addition with letters: leading digit first, then carries. G: prove "odd + odd = even"; find a counterexample; a letter multiplication with every answer, checked by a nested-loop program | Proving |
| 37 | Olympiad-Style Workshop | Heuristics: work backwards, supposition, invariants, pigeonhole, worst case, unattainable totals, cycles in a repeated move (PSLE heuristics P1-6; contest style) with original problems | S: heads and legs by table; work backwards one step. T: supposition and before-after; worst case with socks in a dark drawer (2 colours); pigeonhole with odd and even; the largest total you cannot make with two stamp sizes; a repeated move that cycles. G: invariants; three stamp sizes; worst case with three colours; write a clear solution | Choosing a strategy |
| 38 | (+) Seeing Solids: rotate it in your head | Views of block stacks, which figure is a rotation, dice in a line with touching faces, edges and faces of a solid, painted cubes in a stack (spatial; not in primary); program that counts painted faces | S: build a stack from cubes and draw its top, front and side views. T: which of four figures is a rotation (count by layer); dice in a line whose touching faces sum to 8; edges of a solid (faces x sides / 2); cubes with exactly three painted faces in a pyramid. G: painted-cube counts for n x n x n and for a flat block; how many cubes show no face? | Seeing in 3D |
| 39 | Capstone 1: Plan and Prototype | Mixed (all strands); child picks a question (a game, a simulator, a visual), maths by hand first, prototype in Scratch or Python | S: pick a template and change it. T: add a rule and test. G: pose an open question; plan a test | Planning |
| 40 | Capstone 2: Test, Explain, Present | Mixed spiral round; 3-minute showcase with a "why it works" slide | S: show and explain one test. T: show a bug found and fixed. G: show a limit or extension; answer a peer's question | Explaining |

**Can a new child join cold?** Yes for lessons 31-38. The warm-up covers reading a bar chart, listing outcomes, and extending a number pattern. A child who joins now meets the capstone (39-40) with a template (the S tier), a weaker but valid project.

**Exam period.** Safest to skip or make up: **lesson 38** (stand-alone; the capstones need only the maths of the earlier lessons). Do not skip 39, because 40 builds on it. Term 4 is often shorter: if one lesson must go, it is 38.

## 3. Holiday course: no reuse

The holiday course is a standalone foundation course. **No term lesson reuses, shortens or adapts a holiday lesson**, and no holiday workbook page, qbank item, slide or Scratch starter (`p6/scratch/starters`) is reused in a term lesson. A holiday graduate starting Term 1 does not repeat anything.

The only link is the first 6-minute warm-up of a lesson, which may revisit a holiday topic in new numbers, with a one-line card so a child who did not take the holiday course can join in. Holiday topics each term's warm-ups revisit:

| Term | Holiday topics revisited in warm-ups (lesson) |
|---|---|
| T1 | Factor trees and primes (5); nth term and "predict the 100th" (6); function machines run backwards (8); remainders and clock wrap (3, in the repeating-decimal block) |
| T2 | Function machines for the unknown in a ratio (11); turn angle of a polygon (17); random numbers (15); clock wrap for the clock-hand lesson (17) |
| T3 | Negative numbers on a line (24); algebra machines (21, 22); remainders and cycles (26); primes and factor trees (27); nth term and rate (25) |
| T4 | Mean and outlier (31); fair or unfair, random trials (33); counting basics (34); nth term (35); parity and mod (36) |

Coding strands by term (all starters are new; roughly 28 of the 40 lessons carry a small program): **A Test it with loops and variables** (T1: loop, variable, `if`, `mod`, list, `round` and `join`, one Pen drawing for tilings); **B Structure it** (T2: My Blocks with inputs, nested loops, 1000-trial simulation, scale a drawing, loop over bundles); **C Python bridge** (T3: print, input, `for`, `if`, `def`, lists, turtle; every task also in Scratch); **D Build it** (T4: lists, recursion, simulation, spreadsheet, capstone). Python is optional in T3 and a free choice in T4.

## 4. Coverage check

MOE strand names and year placement are verified (see the top block). Legend: M = main lesson, t = touched in a warm-up or tier, blank = not covered. Every strand still has a main lesson.

| MOE Primary 6 strand | T1 | T2 | T3 | T4 | Comment |
|---|---|---|---|---|---|
| Whole numbers (the four operations, factors, multiples) | M (1, 4, 5) | | M (27) | t (36) | Contexts only; no drill; digit tests (5), trailing zeros (27), cryptarithms (36) |
| Fractions (x and / by fractions) | M (2, 8) | M (12) | | | Term 1 builds the P3-P5 base; lesson 12 is the P6 step; school does far more |
| Decimals | M (1, 3) | t (13, 15) | | | Not a P6 Standard strand (decimals are P4 and P5), so not a P6 gap |
| Percentage | t (3) | M (13, 19) | | t (31) | School practice outpaces us (multi-step, GST, discount chains) |
| Ratio | | M (11, 19) | t (25) | | Same |
| Rate and speed | | M (14, 19) | M (25) | | Rate is P5; speed is not in primary (enrichment, owner-approved preview); lesson 14 also carries combined rate, work and trains |
| Algebra (letter, expressions, simple equations) | | | M (21-23) | | First formal algebra is Term 3 (the holiday algebra is only a warm-up); strongest strand once there |
| Average (total = average x number) | | | | M (31) | Taught from scratch in lesson 31 |
| Pie charts and data | | | | M (31-32) | Bar chart without scale numbers added (31) |
| Angles in geometric figures | | M (17) | | | |
| Area, perimeter, circles | M (7, 9) | M (15, 20) | | | |
| Volume of cube and cuboid, nets | | M (16) | | t (38) | Views and dice added as enrichment (16, 38) |
| Symmetry and transformations | | M (18) | M (24) | | |
| PSLE multi-step word problems and heuristics | t (6, 8) | t | t | M (37) | **School practice clearly outpaces us**; not a goal of this program |

Beyond primary (enrichment): negatives, primes, counting, probability, remainder cycles, powers, binary, coordinates and straight-line graphs, logic and proof. Honest flags: no timed practice, no past-paper drill, only one lesson on each big P6 topic. Say "after the PSLE" or "alongside school", never "P6 maths" or "aligned to MOE" (audit wording rule).

Olympiad-type problem moves worked in (original problems only; none copied from a contest; checked against `docs/sasmo/g6_analysis.md`, Grade 6 only): try small cases (L6, L34); systematic listing with no double count (L34); counting figures by size and rearrangements (L34); work backwards (L8, L37); supposition and heads-and-legs (L37); before-and-after bar model (L11, L13); parity and invariants (L36, L37); worst case, unattainable totals and repeated-move cycles (L37); digit-sum tests and cryptarithms (L5, L36); rounding intervals (L1); pairing sums (L4); remainder cycles and last digits (L26); trailing zeros and lap-time LCM (L27); combined rate, trains and work (L14); fair sharing and mixtures (L19); nested and telescoping fractions (L12); packing bounds (L9); pigeonhole (L37); unit method (L11, L14); choose a variable and form an equation (L21-22); consecutive sums and number pyramids (L29); views and painted cubes (L38); counterexample and "find all" (all Go further items). Contest-style items are written fresh at Think harder and kept tutor-private until released as practice. Still not covered: see "Gaps left unaddressed" at the top.

## 5. Assessment and progress

**End-of-term check (10 questions, one per lesson, 25 minutes, in the first 25 minutes of the term's last full lesson; Term 4: in lesson 39 so presentations in 40 keep their time; no grade, no ranking):** question k comes from the term's k-th lesson, written at the tier below.
- Q1-5 Start here: familiar-context items parallel to the lesson's main idea, no new vocabulary.
- Q6-8 Think harder: the same idea in a new setting.
- Q9 Go further: one "find all" or "is it always true?" item.
- Q10 Explain: "write one sentence on why" or "trace this code and say what it prints".

Questions by term (lesson in brackets): **T1** place value or rounding (1), fraction order (2), conversion (3), shortcut (4), divisibility test (5), sequence rule (6), area and perimeter (7), fraction of a quantity (8), tiling bound (9), code trace of the studio program (10). **T2** ratio share (11), fraction of fraction (12), percent change (13), rate or combined rate (14), circle (15), volume (16), angle chase or clock hands (17), symmetry (18), mixture or fair share (19), scale (20). **T3** expand (21), solve (22), inequality (23), coordinates (24), graph (25), power or last digit (26), HCF/LCM or trailing zeros (27), binary (28), reachable numbers (29), trace code (30). **T4** mean and outlier (31), scatter (32), tree (33), arrangement or count by size (34), recursion (35), logic or cryptarithm (36), strategy (37), views or rotation (38), plan a test (39), explain the project (40). Mark each strand "secure / growing / not yet" and use it to plan support for the next term, and to decide the catch-up card for a mid-year joiner.

**Parent report line per term (neutral, evidence based; no scores or predictions):**
- T1: "This term [Name] worked on place value, fractions, decimals and percent, number shortcuts, divisibility tests, sequence rules and area, with a small program most weeks. [Name] showed [one observed example]. Next term we move to ratio, rates and shapes."
- T2: "[Name] worked on ratio, fractions, percent, rates, circles and volume through models. We noticed [one example]. Next term: algebra, graphs and a first step into Python."
- T3: "[Name] wrote rules with letters, solved equations, read straight-line graphs and tried [Scratch/Python]. We noticed [one example]. Next term: data, chance and a final project."
- T4: "[Name] built and presented [project title], explaining why it works. We noticed [one example]. Suggested next step: [Level / same level next year / a topic to try at home]."

## 6. Work to turn the plan into the full set

Per new lesson: tutor guide section, about 25 slides, 2 workbook pages plus Think harder pages, qbank (6 core, 8 stretch, 9 challenge), warm-up check, open investigation, reflection, and a Scratch (and from Term 3 Python) starter with answer key (tutor only). Every numeric answer and "find all" claim brute-force checked in Python, as in the audits. **All 40 lessons are new**: no holiday lesson, slide or starter is reused, so there is no cheap "adapt the holiday course" term any more.

| Term | Work | Rough effort |
|---|---|---|
| T1 | 10 new lessons (the new Term 1), about 8 new Scratch starters, term handout, the one-line holiday-topic cards for the warm-ups; brute-force checks for the rounding, fraction-list, digit-test and tiling items | about 25-26 person-days |
| T2 | 10 lessons (9 as before plus the new lesson 19), 5-6 starters, scale-model synthesis; drawings for lessons 14, 16, 17, 19 | about 25-26 person-days |
| T3 | 10 lessons (the new lesson 29 included), 7-8 Scratch starters plus Python versions, environment choice | about 25-27 person-days |
| T4 | 10 lessons (the new lesson 38 included), 6 starters, capstone templates and rubric; drawings for lessons 34 and 38 (block figures need care, see open questions); cryptarithm brute-force starter for 36 | about 25-26 person-days |
| All | Four end-of-term checks and answer keys, four parent reports, tier-map and syllabus-map entries, parent-facing term outline, a catch-up card per term for joiners, tutor training | about 9-11 person-days |

Total about 109-116 person-days from a human-only baseline (was 82-88 for 36 lessons with 9 reused as holiday; the rise is Term 1 now new and four added lessons, about 2.5 days a lesson). These are guesses from the size of the holiday set (ten lessons, about 280 slides); a drafting tool can cut writing time, but checking answers, Scratch/Python testing in a real editor (not yet done for the existing `.sb3` files) and tutor review will not shrink much. Suggested order: Term 1 first (it is the entry for every holiday graduate), then Term 2 before the next intake, Terms 3 and 4 on a rolling basis a term ahead. Mid-year joiners mean every term is an entry point, so the catch-up cards cannot wait.

## 7. Open questions for the owner

Answered by the 22 Oct 2026 decisions and dropped: cohort and start term (places open every term, mid-year joiners prorated), whether a Term 2 entry is allowed, gap term after the holiday course (graduates go straight to Term 1/3/2), Term 1 reuse of the holiday course (no reuse), 4 x 9 lessons (now 4 x 10), term price handling and full-term discount (5%; the term price itself is still open at the programme level).

1. **Intake age.** Is the intake children in P6 (PSLE written exams, usually Sept-Oct, fall in Term 3-4), children after PSLE only, or also Sec 1 (age 13)? Term 3 and 4 may clash with prelims and PSLE; is lesson 29 or 38 the right one to make optional, or should a P6 child get a lighter pace?
2. **Python environment:** an offline editor, or a browser tool with no account? It must fit our no-accounts, nothing-uploaded rule.
3. **PSLE wording.** How closely should Term 2 follow the MOE P6 syllabus (ratio, percent)? The PDF has been checked: ratio is P6 (p. 43). May we name PSLE on the page, and with what wording?
4. **Grade 7.** Level 6 spans ages 11-13, which may sit across SASMO Grades 6 and 7. Only a Grade 6 analysis exists. Is a Grade 7 file wanted before the contest weights are trusted?
5. **Homework and take-home work:** expected weekly, or none?
6. **Placement.** Do parents and mid-year joiners get a placement diagnostic per term, or only the existing level diagnostic (`docs/levels_and_placement.md`)? How does a joiner without the holiday course meet the warm-up cards?
7. **Short terms.** Term 4 is often shorter than 10 weeks. Is the answer "skip the stand-alone lesson, rest by recording" (this plan), or fewer lessons with a smaller fee?
8. **Lesson 29.** Its evidence is five single items. Keep it as the Term 3 added lesson, or replace it with a plain problem-solving studio?
9. **Lessons 5, 14, 16, 34 and 37 and contest-style items.** Is it right for them to carry the contest additions at Think harder (this plan), or should any gap type (digit tools, worst case, rate) get a full lesson at the cost of an existing one? The plan now holds at 40 lessons either way.
10. **Draft practice problems.** The items in `docs/sasmo/g6_original_problems_draft.md` are untried with children. Who reviews them before they are used as candidate practice?
11. **Hand-drawn figures.** Lessons 16, 34 and 38 need careful block and triangle figures (the same issue as Level 3 lessons 22 and 23 below). Who draws and checks them?
12. **Speed preview (lesson 14).** Owner-approved enrichment, labelled secondary-school. Confirm the wording on the parent page, and whether to keep the label when the child is in P6.

**Kept in view (KIV) from other levels, not decided here:** Level 5 lessons 28 and 29 may merge; Level 5 lesson 32 may be too full; a secondary speed preview in Level 5 lesson 15 (Level 6 keeps speed only as the owner-approved enrichment in lesson 14); Level 3 lessons 22 and 23 need hand-drawn figures. They stay listed as open questions and this plan does not resolve them.

## Non-routine assignments (owner decision, 23 Oct 2026)

The owner asked that the non-routine question types found in school papers sit inside every term plan. Source: `docs/books/p6_non_routine_catalogue.md` (text-free summary of 2778 non-routine questions in 122 Primary 6 preliminary and weighted-assessment papers from schools, 2020 to 2026; the questions themselves are in a private, gitignored file) and `docs/books/p6_school_paper_patterns.md` (wording, ranges, pictures and the fit/gap table). **Every one of the 40 lessons now names its non-routine work: a heuristic or reasoning type, the tier where it sits (Think harder or Go further, never Start here) and, where one exists, original examples with scripted answers.** Lesson authors write their own items; school and contest questions are never copied.

How to read this section.

- Type codes (14 types): LOG logical reasoning, true or false, compass; CMP comparison and average; BACK work backwards, fraction or percent of the remainder; CTX unfamiliar context or hidden fact (tariff, rate, tap); LIST systematic list, greatest and least, packing; EXP algebra and explain; GC guess and check, supposition; PAT pattern; DIAG draw or read a diagram, view or solid; TAB table or graph; EQ unit, ratio and equal-share model; WAYS most, least, best buy, count the ways; CHAL build or draw from data; GEO geometry chain. Primary 5 had 16 types; MULTI and POSE are dropped because at Primary 6 nearly every item is multi-step and none was open-ended.
- **T** = Think harder, **G** = Go further. Status **N** = new assignment: no Level 6 lesson is written yet, so every entry is a plan. Contest-style puzzles already named in the lesson tables above are not repeated here; the types below are the school-paper question types that sit beside them.
- The example IDs (`EX-EQ-1` and so on) are original questions with scripted answers in `docs/books/p6_non_routine_catalogue.md`. An entry with no example ID is a plan line for the author to write.
- School papers name no heuristic in the stem at Primary 6. They do name the tool ("Draw a rectangle with the same area", "Express your answer in terms of n", "Take pi as 3.14"), and the 2026 papers ask for a reason ("circle the words ... because"). Think harder items may carry the tool; Go further items drop it.

### Non-routine lesson by lesson

| # | Lesson | Non-routine types (tier, status): what | Catalogue items |
|---|---|---|---|
| 1 | Big and Small Numbers | LIST (T, N): use all four digit cards once for the number closest to a target; CTX (G, N): rounding in a story: how many whole pieces of 0.35 m from 5 m; EXP (T, N): "correct to 1 decimal place": say which digit decides | EX-LIST-4 |
| 2 | Fractions on the Number Line | CMP (T, N): which of three unlike fractions is closest to 1/2; LOG (T, N): true, false or not possible to tell about fractions on a line; EQ (G, N): what fraction of a figure of identical shapes is shaded | (author's own items) |
| 3 | Three Names for One Number | CMP (T, N): order a mix of fractions, decimals and percents, smallest to greatest; EXP (T, N): which is greater, 3/8 or 0.37 or 38%, and how you know; TAB (G, N): complete a three-column fraction, decimal, percent table from one clue | (author's own items) |
| 4 | Number Shortcuts | CMP (T, N): total = average x number: five numbers, then a sixth makes the average change; EXP (T, N): a bracket item such as 7 x (54 - 24 / 6) + 4, with the order written out; LOG (G, N): which is greater without computing | EX-CMP-1 |
| 5 | Divisibility Detectives | LIST (T, N): list every number under 100 that is a multiple of two numbers; LOG (T, N): six factors and 3 is one: multiple of 3, even, less than 10?; LIST (G, N): which numbers have an odd number of factors | EX-LIST-1, EX-LOG-1, EX-LIST-5 |
| 6 | Rules That Look Back | PAT (T, N): sum of the first 99 digits of a repeating block; PAT (T, N): sticks in the nth figure and which figure uses 152; PAT (G, N): a zigzag table with four columns: which column holds 923 | EX-PAT-1, EX-PAT-2, EX-PAT-4 |
| 7 | Area and Perimeter Puzzles | CHAL (T, N): draw every rectangle of a given area and list the perimeters; CHAL (G, N): draw right-angled triangles of a given area on a grid; EXP (T, N): perimeter of a figure in terms of p | EX-CHAL-1, EX-CHAL-2 |
| 8 | Fractions of a Quantity | BACK (T, N): spend 2/5, then 1/3 of the rest: work back from what is left; BACK (T, N): a tank 3/8 full becomes 7/8 full: capacity; EQ (G, N): what fraction of her money was spent on the last item | EX-BACK-1, EX-BACK-2 |
| 9 | Tiling, Bounds and Overlaps | GEO (T, N): midpoints of two sides of a square: area of the corner triangle; LIST (T, N): the most 1 x 2 tiles that fit, and why a count of area proves it; CHAL (G, N): draw two overlapping rectangles with a given overlap area | EX-GEO-3 |
| 10 | Term 1 Studio | GC (T, N): coins of two kinds for an exact total: guess, check and code; LOG (T, N): a three-statement true, false or not possible table about a result; CHAL (G, N): write a puzzle with exactly one answer and check it by program | EX-GC-1, EX-LOG-4 |
| 11 | Ratio Recipes | EQ (T, N): a ratio and a transfer that makes the parts equal; EQ (G, N): a ratio before and after both people spend or gain; LOG (T, N): ratio statements read from a bar graph: true, false or not possible; TAB (T, N): a pie chart sector gives a count: find another sector | EX-EQ-1, EX-EQ-3, EX-LOG-4, EX-TAB-2 |
| 12 | Fractions of Fractions | EQ (G, N): a fraction of one quantity equals a fraction of another: total; BACK (T, N): fruit in a ratio, a fraction of one and a count of the other sold, equal left; CMP (T, N): what fraction of the whole figure is the nested part | EX-EQ-2, EX-BACK-3 |
| 13 | Percent Change Detective | BACK (T, N): 35% sold, then 30% of the rest: work back to the start; EQ (T, N): two shops, different discounts, same price paid: the other usual price; CTX (T, N): GST at 9 percent forwards and backwards; TAB (T, N): percent of a total read from a table or pie chart | EX-BACK-4, EX-EQ-4, EX-CTX-5 |
| 14 | Rates, Work and Trains | CTX (T, N): two cars leave towns apart at different speeds: when do they meet (preview); CTX (T, N): a tap fills a tank of given base: minutes to a depth; EQ (G, N): pour from a full tank into an empty one until the heights match; CTX (G, N): a late start and an early finish at the same distance | EX-CTX-2, EX-CTX-4, EX-EQ-5 |
| 15 | Circles and Pi | GEO (T, N): a quarter circle in a rectangle: the area left over (pi 22/7); GEO (G, N): semicircles on a line: perimeter and area in terms of pi; PAT (T, N): circular beads along a 100 cm chain: how many of one colour | EX-GEO-2 |
| 16 | Volume, Nets and Views | DIAG (T, N): top view gives the cubes, front view gives the heights; DIAG (G, N): the most cubes that can be added without changing either view; GEO (T, N): which face does not fit the net, and the perimeter of the net | EX-DIAG-1, EX-DIAG-2 |
| 17 | Angle Chasing | GEO (T, N): isosceles triangle on a parallelogram: angle chase; GEO (T, N): parallel lines cut by a transversal: co-interior angles; LOG (T, N): angle statements: true, false or not possible to tell; EXP (G, N): circle the words: "is isosceles because ..." | EX-GEO-1, EX-GEO-4 |
| 18 | Symmetry and Transformations | CHAL (T, N): shade squares to complete a figure with a given line of symmetry; LOG (T, N): how many of these shapes have at least one line of symmetry; DIAG (G, N): complete a net so the whole net has a line of symmetry | (author's own items) |
| 19 | Mixtures, Fair Shares and Best Buys | WAYS (T, N): buy 3 get 1 free: the least cost for a number of items; WAYS (T, N): single price or 10 for a price: the least cost for 27; CTX (T, N): charges in steps: "every additional half hour or part of it"; EQ (T, N): a paint mixture in a ratio and what fraction is one colour | EX-WAYS-2, EX-WAYS-4, EX-CTX-1 |
| 20 | Scale Models and Same-Height Triangles | CHAL (T, N): draw a triangle with a quarter of a rectangle's area and an obtuse angle; EQ (T, N): area A is 5 times C and B is 12 times A: A as a fraction of the whole; GEO (G, N): triangles on the same base and height | EX-CHAL-3 |
| 21 | Letters and Brackets | EXP (T, N): stamps at n cents paid with $5: change in terms of n; EXP (T, N): a pen and a notebook $2 dearer: cost of 3 pens and 2 notebooks; EXP (G, N): is the sum of three consecutive numbers always a multiple of 3? | EX-EXP-4, EX-EXP-1, EX-EXP-3 |
| 22 | Equations on a Balance | EXP (T, N): a letter for a child's age: ages in two years, total given; EQ (T, N): an equation from a perimeter with a letter; GC (G, N): tickets at two prices: check by brute force in code | EX-EXP-2, EX-GC-2 |
| 23 | At Least, At Most | LIST (T, N): the greatest number of cubes that fit in a box (rounding down); WAYS (T, N): "at least" score to win a prize: the highest score that did not win; LOG (G, N): the least number that satisfies two conditions | EX-LIST-3 |
| 24 | Maps with Numbers | LOG (T, N): face north, turn 135 clockwise then 225 anti-clockwise; LOG (G, N): south-east of the house and north of the school: mark the point; TAB (T, N): read a position and a direction from a grid | EX-LOG-2 |
| 25 | Straight-Line Stories | TAB (T, N): the steepest 10-minute interval on a graph; TAB (G, N): postage or a tariff graph with two slopes; CTX (T, N): a tiered water tariff: the volume for a given bill | EX-TAB-1, EX-TAB-3, EX-CTX-3 |
| 26 | Powers and Roots | LIST (G, N): which numbers have an odd number of factors (squares); PAT (T, N): the last digit of a power by finding the cycle; LOG (T, N): a square number between two limits | EX-LIST-5 |
| 27 | Factors, HCF, LCM and Trailing Zeros | LIST (T, N): lights blink every 4, 6 and 9 seconds: together again after; LIST (T, N): packs of 30 and 22 that make 732 exactly: the fewest boxes; LIST (G, N): as many identical bags as possible from two counts | EX-LIST-6, EX-LIST-2 |
| 28 | Binary and Twenty Questions | LOG (T, N): twenty questions: what is the best first question; LOG (G, N): order four runners from clues, no ties; GC (G, N): guess a number by halving: why 7 questions | EX-LOG-3 |
| 29 | Reachable Numbers and Rule Grids | CMP (T, N): a 3 by 3 frame on a number table: the average of the eight numbers; PAT (T, N): fill a number pyramid from a rule; CHAL (G, N): build a rule grid with exactly one solution | EX-CMP-5 |
| 30 | Term 3 Studio | LOG (T, N): order four runners from clues; BACK (T, N): undo a chain of steps to find the start; CHAL (G, N): write a puzzle with exactly one answer and test it by program | EX-LOG-3, EX-BACK-3 |
| 31 | Statistics That Mislead | CMP (T, N): a wrongly typed mark: the correct average; CMP (G, N): greatest possible difference given an average; TAB (T, N): a pie chart sector gives a count: find another sector; LOG (T, N): a three-statement true, false or not possible table from a bar graph | EX-CMP-4, EX-CMP-2, EX-TAB-2, EX-LOG-4 |
| 32 | Scatter and Spreadsheets | TAB (T, N): the steepest interval on a graph; CMP (G, N): average of five classes and the average of the other three; LOG (G, N): two things move together: what can and cannot be said | EX-TAB-1, EX-CMP-3 |
| 33 | Two-Stage Chance | WAYS (T, N): list every way to make $1.00 from three coins; WAYS (G, N): the most batches from two ingredients; LOG (T, N): is the game fair: true, false or not possible to tell | EX-WAYS-1, EX-WAYS-3 |
| 34 | Counting with Constraints | WAYS (T, N): list every way to make $1.00 from three coins; LIST (G, N): how many rectangles in a small grid, by size; GC (T, N): two kinds of ticket and a total: how many of each | EX-WAYS-1, EX-GC-2 |
| 35 | Patterns That Grow | PAT (T, N): sticks in the nth figure and which figure uses 152; PAT (G, N): stacked cups: how many cups make a given height; EXP (G, N): write the nth term and the figure with a given perimeter | EX-PAT-2, EX-PAT-3 |
| 36 | Logic, Proof and Digit Puzzles | LOG (T, N): six factors and 3 is one: multiple of 3, even, less than 10?; LOG (T, N): order four runners from clues; LIST (T, N): use all four digits once for the number closest to a target; EXP (G, N): is the sum of three consecutive numbers always a multiple of 3? | EX-LOG-1, EX-LOG-3, EX-LIST-4, EX-EXP-3 |
| 37 | Olympiad-Style Workshop | GC (T, N): coins of two kinds for an exact total; GC (G, N): notes of two values and a condition after paying; BACK (T, N): 35% sold, then 30% of the rest: work back; WAYS (G, N): the most batches from two ingredients; CMP (G, N): greatest possible difference given an average | EX-GC-1, EX-GC-3, EX-BACK-4, EX-WAYS-3, EX-CMP-2 |
| 38 | Seeing Solids | DIAG (T, N): top view gives the cubes, front view gives the heights; DIAG (T, N): a painted 3 x 3 x 3 cube cut up: cubes with exactly two painted faces; DIAG (G, N): the most cubes that can be added without changing either view | EX-DIAG-1, EX-DIAG-3, EX-DIAG-2 |
| 39 | Capstone 1: Plan and Prototype | EXP (T, N): explain why a test result fits your rule; CHAL (G, N): pose an open question with more than one answer and plan a test; LOG (T, N): which of three claims can your test support | (author's own items) |
| 40 | Capstone 2: Test, Explain, Present | EXP (T, N): explain why it works in one sentence; CHAL (G, N): answer a peer's question about your limit or extension; CMP (T, N): compare two designs by a fair test | (author's own items) |

### Matrix: type by lesson (the spiral across the year)

`N` = planned in a lesson not yet written; `.` = not planned. Lessons 1 to 40 in four groups of ten (one group per term).

```
Lesson        1234567890 1234567890 1234567890 1234567890
Term          1111111111 2222222222 3333333333 4444444444
LOG           .N.NN....N N.....NN.. ..NN.N.N.N NNN..N..N.
CMP           .NNN...... .N........ ........N. NN....N..N
BACK          .......N.. .NN....... .........N ......N...
CTX           N......... ..NN....N. ....N..... ..........
LIST          N...N...N. .......... ..N..NN... ...N.N....
EXP           N.NN..N... ......N... NN........ ....NN..NN
GC            .........N .......... .N.....N.. ...N..N...
PAT           .....N.... ....N..... .....N..N. ....N.....
DIAG          .......... .....N.N.. .......... .......N..
TAB           ..N....... N.N....... ...NN..... NN........
EQ            .N.....N.. NNNN....NN .N........ ..........
WAYS          .......... ........N. ..N....... ..NN..N...
CHAL          ......N.NN .......N.N ........NN ........NN
GEO           ........N. ....NNN..N .......... ..........
```

Count of lessons per type (all new; no Level 6 lesson is written):

| Type | Lessons | Terms with it | School items (2778) |
|---|---|---|---|
| LOG | 17 | T1, T2, T3, T4 | 158 |
| CMP | 9 | T1, T2, T3, T4 | 128 |
| BACK | 5 | T1, T2, T3, T4 | 229 |
| CTX | 5 | T1, T2, T3 | 269 |
| LIST | 8 | T1, T3, T4 | 106 |
| EXP | 11 | T1, T2, T3, T4 | 122 |
| GC | 5 | T1, T3, T4 | 50 |
| PAT | 5 | T1, T2, T3, T4 | 107 |
| DIAG | 3 | T2, T4 | 131 |
| TAB | 7 | T1, T2, T3, T4 | 238 |
| EQ | 9 | T1, T2, T3 | 586 |
| WAYS | 5 | T2, T3, T4 | 62 |
| CHAL | 9 | T1, T2, T3, T4 | 110 |
| GEO | 5 | T1, T2 | 482 |

Every type appears in at least 2 terms. Types not in all four terms: CTX, LIST, GC, DIAG, EQ, WAYS, GEO. They are rare in the papers, and owner decision 6 asks only for contest-style items at Think harder. The four types the papers use most (EQ, GEO, CTX, TAB) are in 9, 5, 5, 7 lessons.

GEO (geometry chains, the second largest group in the papers) is only in lessons 9, 15, 16, 17 and 20 by design: angle and area chains are taught in the geometry lessons and appear in Think harder there. The EQ and BACK types are shared between lessons 8, 11, 12, 13, 14 and 19.

### Notes: what the Primary 6 papers change in this plan

Evidence is in `docs/books/p6_school_paper_patterns.md` (sections 1, 5 and 6). These are plan changes for the lesson authors; the lesson tables above are not edited here, so the wording below overrides them where they differ.

- **Average comes earlier (lesson 31, lessons 4 and 8).** Average is set in nearly every preliminary paper (80 of 87) and in every year (about 170 recorded items). Lesson 31 teaches it in Term 4. Add one Think harder average item to lesson 4 (EX-CMP-1) so that a child who joins in Term 1 has met "total = average x number", and keep lesson 31 as the full lesson (EX-CMP-4, EX-CMP-2).
- **Lesson 17: parallel lines and a reason.** The plan says angles between parallel lines are not in primary. The papers set them in every year from 2021 (parallelogram, trapezium and rhombus chains, and "AD is parallel to BC"), and the 2026 papers ask for a reason in words ("parallel because the angles add to 180", "isosceles because equal angles"). Teach co-interior and alternate angles at Think harder and the one-line reason at Go further (EX-GEO-4).
- **Lesson 14: lead with taps and tanks, keep speed as the preview.** km/h and m/min items run 2022 to 2025 (12 to 19 recorded a year); none was recorded in the 2026 papers. Tap and tank rates (litres or cm per minute, pouring until the heights match) stay in 2026. The preview label stands; the opening items are taps (EX-CTX-4, EX-EQ-5).
- **Lesson 11: ratio after a change, two boxes, ratio from a chart.** Ratio is in 33 recorded 2026 items. Typical: "5 : 4, then 56 women joined, now 3 : 4", two boxes in different ratios with a times-as-many link, ratio of areas. Add these at Think harder (EX-EQ-1, EX-EQ-3).
- **True, false or not possible to tell (about 60 items; every year).** Add a three-statement tick table, as a five-minute item, to lessons 2, 11, 17, 31 and 33 (EX-LOG-4). Name the third choice in the stem.
- **Draw-on-a-grid items (about 110).** Add a draw item to lessons 7, 9, 18 and 20: same area, same perimeter, a rhombus from two sides, a triangle with a quarter of a rectangle's area and an obtuse angle (EX-CHAL-1 to EX-CHAL-3). Say how the drawing is marked.
- **Ratio and percent in Term 1 at school.** The Term 1 weighted assessment (WA1, March) sets ratio, fractions and percentage; the Term 2 one (WA2, May) sets circles, GST, interest, algebra and angles. Our plan teaches ratio (lesson 11) and percent (lesson 13) in Term 2. This is acceptable for an "alongside school" program. Optional: a six-minute ratio warm-up in lesson 8 or 9 (share in a ratio of two, ratio of three) so a Term 1 child has met the idea. Lesson 11 stays the full treatment.
- **Lesson 18: trim rotation and tessellation.** The papers set line symmetry ("shade to complete a figure", "how many have a line of symmetry") and nothing else; rotation, translation and tessellation are enrichment.
- **Lesson 15: pi 3.14 first.** "Take pi as 3.14" is about 2.5 times as common as 22/7, and "in terms of pi" occurs. Use 22/7 only where a diameter is a multiple of 7. Semicircles and quarter circles on a grid of equal squares are the standard figure.
- **Lesson 13: GST at 9 percent** (7 percent in 2021 and earlier; none recorded in 2026), two shops at equal price, and a further $ off after a percent discount (EX-EQ-4, EX-CTX-5).
- **Charges in steps and best buys (lessons 19, 25).** "Every additional half hour or part of it", a buy-n-get-1-free deal and "10 for $28" appear every year (EX-CTX-1, EX-WAYS-2, EX-WAYS-4).
- **Compass and turns (lesson 24).** About 60 items 2021 to 2025, none in 2026. Keep it as a six-minute warm-up and say it is optional (EX-LOG-2).
- **Lessons 23, 26, 28, 32, 33 and coordinates in lesson 24 have no school counterpart.** The papers read contain no probability, inequality, negative number, binary, scatter plot or coordinate item. They stay as enrichment; the non-routine items assigned to them use the school types (list, true or false, graph reading) so each lesson still has a link to what school sets.
- **Algebra is one letter, whole-number coefficients, no brackets** ("change in terms of n", "value of 9c - 3 + 2c when c = 7"). Lessons 21 and 22 use that range for Start here and Think harder; expanding brackets and unknowns on both sides stay at Go further.
- **Picture dependence.** About half of the recorded items needed a picture (angle figures, composite shapes on a grid, nets, block views, pie charts and bar graphs, line graphs with two taps). A digital or printed page must carry a drawing for the same kind of item.
- **Marks and form.** Paper 2 items are 4 or 5 marks with parts (a), (b) and sometimes (c); (b) uses (a). Think harder two-part items follow that form; Go further may add a third part. The last question of Paper 2 has three stages and 5 marks; Go further items should look like it.
