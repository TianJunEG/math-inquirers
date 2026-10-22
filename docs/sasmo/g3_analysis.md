# SASMO Grade 3 (Primary 3) contest papers: what they test and how Level 3 prepares for it

Analysis only. No lesson files were changed. Contest problems are not reproduced: they are referred to by paper and question number (19-12 is 2019, Question 12) with a short skill tag. Question text, answers and my solution checks are in the git-ignored `docs/sasmo/private_solution_notes_g3.md`.

## 1. What was analysed, and how far to trust it

- One file: the printed practice book "SASMO Primary 3 (Grade 3) GEP Practice, 2019 and 2020 contest problems with full solutions" (SIMCC, 2021). The 26 PDF pages (two book pages per scan) hold the cover, preliminaries, the 2019 questions (book pp 9-21), the 2020 questions (pp 22-33), then worked solutions to both papers (pp 34-53). **Two distinct papers = 50 problems.**
- Format, as printed in the book: 25 questions per paper. Section A = Q1 to 15, five options (A to E, E is "none of the above"), 2 marks, minus 1 for a wrong answer, 0 for none (30 problems). Section B = Q16 to 25, whole-number answer, 4 marks, no penalty (20 problems). The book's "Introduction", "Competition and Prizes" and "Problem Solving Strategies" pages are not in the file, so I cannot say the exam length or the scoring cut-offs.
- **Every one of the 50 problems already has a publisher's worked solution in the file.** Nothing had to be solved from scratch. I independently re-checked every answer that depends only on the text (about 35); all agreed with the book. About 15 problems depend on a drawing (19-2, 19-4, 19-7, 19-9, 19-11, 19-12, 19-15, 19-16, 20-3, 20-6, 20-15, 20-18, 20-21 and the pictogram and bar graph of 19-18 and 20-19). For those I followed the publisher's solution and checked it against the picture where I could read it; I did not re-solve them independently.
- Categories are my single-coder judgement; each problem is filed under its main skill only, so counts are indicative. **Two papers is a very small sample.** A type with 1 to 3 problems is "occasionally seen", not "tested every year". Differences between 2019 and 2020 are probably noise.
- The contest is not the school syllabus. It uses divisibility tests, summing a long list, fence-post counting and 3D views that the Primary 3 scheme in `p3/SPEC.md` does not list. Level 3 teaches "Primary 3 plus thinking", so some gaps below are by design. Whether to close them is the owner's call.

## 2. Catalogue

Band is how hard the item reads as presented (my judgement from its position, marks and number of steps): E = one step or known fact, M = two or three steps with a known method, H = needs a case split, an insight or a long careful count. Status is how well Level 3 prepares the item today (section 4): P = prepared, Part = partly, Gap = nothing in the program.

| ID | Sec | Skill tag | Thinking move | Band | Status |
|---|---|---|---|---|---|
| 19-1 | A | Add and subtract a list | Pair numbers that make tens | E | Part |
| 19-2 | A | Dot-circle picture pattern | Count each colour by position, see three interleaved patterns | M | Gap |
| 19-3 | A | Sums of three dice | Smallest and largest possible, so which total is impossible | M | Part |
| 19-4 | A | Top view of a block figure | Compare one feature at a time, eliminate | M | Gap |
| 19-5 | A | Race order | Chain the clues | E | P |
| 19-6 | A | Colour by door versions | List or multiply the choices | E | Part |
| 19-7 | A | Mirror image of a picture | Check left and right feature by feature | M | Gap |
| 19-8 | A | 4-digit number divisible by 3, digit is even | Digit-sum test, then filter | E | Gap |
| 19-9 | A | Balloons carry toy animals | Compare two pictures, find the difference | M | Part |
| 19-10 | A | Two films, fixed show times | Try both orders, use a timetable | M | Part |
| 19-11 | A | Missing shape in a 3 by 3 | Combine and remove rule across rows | M | Gap |
| 19-12 | A | Figures of equal squares | Count squares for area, count sides for perimeter | M | P |
| 19-13 | A | Pages read go down by 2 a day | Sequence plus 7-day cycle | H | Part |
| 19-14 | A | Two-digit numbers divisible by 2 and 3 | Same as divisible by 6, count the multiples, remove the 1-digit one | M | Part |
| 19-15 | A | Balance scales of toys | Chain the comparisons, order the toys | H | Gap |
| 19-16 | B | Rectangles in a house picture | Count by size (1-part, 2-part ...) | M | Part |
| 19-17 | B | Two-number operator | Find the rule from four examples, apply it | H | Gap |
| 19-18 | B | Picture graph, then share equally | Read with a key, total, divide, compare | M | Part |
| 19-19 | B | Three people, stamps | Bar model with a "less than" | M | P |
| 19-20 | B | Number sentence with a box twice | Collect the boxes, undo | M | Part |
| 19-21 | B | 3-digit number from clues | Bar model or list on the digit relations | M | P |
| 19-22 | B | Two ticket prices, total, fewer than 14 people | Try the largest count and work down, check | H | P |
| 19-23 | B | How many times digit 1 is written, pages 1 to 130 | Count by place (ones, tens, hundreds) | H | Part |
| 19-24 | B | Multiplication grid with a sum column | Bounds first, then try the few cases | H | Part |
| 19-25 | B | Subtraction cryptarithm | Rewrite as addition, fix the leading digit | M | P |
| 20-1 | A | Sum of nine 3-digit numbers | Pair to make tens and hundreds | E | Part |
| 20-2 | A | Tens and ones subtraction in words | Place value to numbers | E | P |
| 20-3 | A | Faces in a 3 by 3 (two features) | Each feature runs its own cycle | E | Gap |
| 20-4 | A | Day of the week, 40th day | Remainder after 7 | M | P |
| 20-5 | A | Multiples of 6 between 14 and 100 | Divide, then take away the ones before the start | M | Part |
| 20-6 | A | Cubes stacked in a corner | Count stack by stack | M | Gap |
| 20-7 | A | Late arrival, minutes of travel | Time line, 1:47 to 4:12 | M | P |
| 20-8 | A | Sequence 1, 3, 7, 15, 31 | Gaps double | E | P |
| 20-9 | A | 4-digit number 3P78 divisible by 3 | Digit-sum test, count the digits | M | Gap |
| 20-10 | A | Counting numbers with only odd digits | List in order, find the 31st | M | Part |
| 20-11 | A | Four weights, three clues | Eliminate by odd or even and multiples | M | P |
| 20-12 | A | Share oranges by what each paid | Price per orange, then multiply | M | Part |
| 20-13 | A | Tank weighed with two amounts of water | Subtract the two weighings | M | P |
| 20-14 | A | Lanterns on both sides of a river | Gaps then posts, double | M | Gap |
| 20-15 | A | Faces of a pyramid | Compare faces feature by feature | H | Gap |
| 20-16 | B | Sum of 30 terms going down by 1 | Pair first and last | M | Gap |
| 20-17 | B | Rectangle made longer, new perimeter | Two lengths change, so perimeter changes by double | M | Part |
| 20-18 | B | Triangles in a star figure | Count by size | H | Part |
| 20-19 | B | Bar graph, six months | Read each bar, add | E | P |
| 20-20 | B | Train of operations, final number 30 | Work backwards | E | P |
| 20-21 | B | Shaded region on a grid | Join half squares into whole squares | M | Part |
| 20-22 | B | Boxes, packets, baskets with prices | Swap pairs, then find each | M | Part |
| 20-23 | B | Matchstick digits, exactly 17 sticks | Most digits, then biggest first digit | H | Gap |
| 20-24 | B | Seven numbers in a Y of circles, equal line sums | The total of the three lines counts the centre three times | H | Part |
| 20-25 | B | Addition cryptarithm RQQR | Leading digit, then ones, then tens | M | P |

Totals: band E 10, M 30, H 10. Status P 15, Part 21, Gap 14.

## 3. Frequency by type

| Type | All | A | B | Where it appears |
|---|---|---|---|---|
| Computation and number sentences (pairing; balance; undo a chain) | 4 | 2 | 2 | 19-1, 19-20, 20-1, 20-20 |
| Place value and digit-restricted counting | 4 | 2 | 2 | 19-21, 19-23, 20-2, 20-10 |
| Multiples and divisibility (tests, counting multiples in a range) | 4 | 4 | 0 | 19-8, 19-14, 20-5, 20-9 |
| Time and calendar | 4 | 4 | 0 | 19-10, 19-13, 20-4, 20-7 |
| Spatial: top view, mirror, cube stack, pyramid faces | 4 | 4 | 0 | 19-4, 19-7, 20-6, 20-15 |
| Counting: figures, choices, gaps and posts | 4 | 2 | 2 | 19-6, 19-16, 20-14, 20-18 |
| Number patterns and rules (gaps, series sum, operator) | 3 | 1 | 2 | 19-17, 20-8, 20-16 |
| Picture patterns (missing shape, faces grid) | 3 | 3 | 0 | 19-2, 19-11, 20-3 |
| Logic and ordering (bounds, chains, elimination) | 3 | 3 | 0 | 19-3, 19-5, 20-11 |
| Symbol and balance-scale equations | 3 | 2 | 1 | 19-9, 19-15, 20-22 |
| Bar model, difference, price per item | 3 | 2 | 1 | 19-19, 20-12, 20-13 |
| Area and perimeter | 3 | 1 | 2 | 19-12, 20-17, 20-21 |
| Cryptarithms | 2 | 0 | 2 | 19-25, 20-25 |
| Number-grid and shape-sum puzzles | 2 | 0 | 2 | 19-24, 20-24 |
| Guess and check, optimise under a limit | 2 | 0 | 2 | 19-22, 20-23 |
| Graphs (picture graph, bar graph) | 2 | 0 | 2 | 19-18, 20-19 |

What stands out:
- **Section A is mostly short-reach thinking, not Section B style.** All 4 divisibility and multiples items, all 4 time and calendar items, all 4 spatial items, all 3 picture patterns and all 3 logic items are in Section A. 11 of the 14 "Gap" items are Section A, so a child who has never met them loses easy 2-mark questions to a minus-1 penalty.
- **Section B is where reasoning lives**: both cryptarithms, both grid and shape-sum puzzles, both guess-and-check items, both graph items and 4 of the 7 number-pattern and counting items are Section B.
- **Repeats across the two years** (same skill, new numbers): divisibility by 3 (19-8 and 20-9), multiples counted in a range (19-14 and 20-5), a cryptarithm (19-25 and 20-25), a weekday from a count of days (19-13 and 20-4), counting figures by size (19-16 and 20-18), and a shape-sum puzzle of the same kind (19-24 and 20-24). These are the best candidates for any contest-oriented practice.
- Number size: 4-digit numbers appear only in sums and divisibility; answers reach 4540 and 1221. Multiplication is mostly tables up to 10 by 10, but a few items need 71 by 15 (20-16) or 132 divided by 11 (20-14), a step beyond the SPEC's "no 2-digit multipliers or divisors" line.
- Reading load is light. Several items carry the thinking in a drawing (about 15 of 50 depend on one).

## 4. How Level 3 maps to it

Level 3 lessons: L1 Number Sleuths; L2 Cryptarithm Crackers; L3 Times Table Treasure; L4 Model Makers; L5 Remainder Riddles; L6 Fraction Walls; L7 Area Architects; L8 Angle and Line Detectives; L9 Measure and Money Masters; L10 Challenge Day. Tiers in each question bank: Start here = Core (C1 to C6), Think harder = Stretch (TH1 to TH8 or 9, of which TH1 to TH4 print on the workbook), Go further = Challenge (GF1 to GF9, of which GF7 to GF9 print). Item numbers below are the order in `p3/content/lN.js` (1-based).

| Type | Level 3 prepares it | Start here / Think harder | Go further would need | Verdict |
|---|---|---|---|---|
| Computation, number sentences, undo chains | L2: column work, "opposite operation", magic squares and pyramids; L2 TH4 (add 1099 or 1999 by mistake) and TH7 (9999 minus, then 10 000) use compensation; L5 and L9 name working backwards | Backwards chains of 4 operations and "pair to make 10 or 100" are not practised | Short mental-strategy routine: pairing, compensating (999 + 1998), undoing a four-step chain; a box that appears on both sides of "=" | Partial: small extension |
| Place value, digit clues, restricted-digit counting | L1 is built for this: 4-digit clue puzzles (GF5), counting digits (TH6, 1 to 100; GF3, pages to 120), listing in order, odd digits only (GF1) | Covered | The "nth counting number when only some digits are allowed" and counting one digit's occurrences across 3 places (19-23, 20-10) | **Prepared**; light extension |
| Multiples and divisibility | L3 tables and last digits (TH3, GF3 numbers divisible by 6 and 9 up to 200, GF6 sweets shared 6, 9, 4 ways); L5 division and remainders | Counting multiples in a range ("how many from 14 to 100") is nowhere; the digit-sum test for 3 is nowhere (L3 only notes digit sums of the 9s table) | Test for 3 from digits, "divisible by 2 and 3 means by 6", counting multiples by division and taking away the early ones, "A or B" counting | **Real gap**; cheap to close; all four items are Section A |
| Cryptarithms | L2 throughout: core carrying, TH5 to TH8, GF3, GF4, GF9 (ABC + ACB = CBA); rewriting subtraction as addition is taught ("check by adding") | Covered | Nothing new needed | **Strongest match** |
| Number-grid and shape-sum puzzles | L2 magic squares and GF5 (nine numbers, magic total = total of all three rows divided by 3); L3 GF1 multiplication square | Shapes where one cell belongs to several lines (centre of a Y, corners of a triangle) are not met | The "add the line sums, the shared cell counts extra, so the total must be a multiple of 3" argument; finding the biggest or smallest | Partial: extension |
| Number patterns and rules | L1 TH7 is the 1, 3, 7, 15, 31 sequence (so 20-8 is covered); L10 C5, TH3 (sticks), GF6 (table of jumps) | Constant steps and doubling covered | Sum of an evenly stepping list by pairing (20-16, no Gauss-style work in the program); rules for two-number operators (19-17); gaps that grow by 2 | Partial; two sub-gaps |
| Picture patterns | Nothing specific; L3 trains "look for a pattern" with numbers | Missing-shape and faces-in-a-grid items are not practised | One warm-up routine: name each feature, find each feature's own cycle | **Gap**; low priority (one routine) |
| Spatial: top view, mirror, cube stacks, nets | Nothing. L4 uses cube towers as bars only; L7 and L8 are flat | None | A short spatial strand: cubes on a grid with heights, front and top views, mirror, folding and punching, painted cubes | **Real gap**; all Section A; best taught with real cubes |
| Logic and ordering | L10: logic grid, queues, TH2 pets, TH6 order, GF4 who ate the kueh | Covered | "Smallest and largest possible, so this total is impossible" (19-3); parity arguments | **Prepared**; small extension |
| Symbol and balance-scale equations | L4 GF2 (pens and a box, $25 and $35), GF6 (jugs and cups), TH8 sugar and flour | Equations built from two baskets: covered. Picture or balance-scale comparisons of three or more objects (19-15) are not | Chains of "2 of A = 3 of B" to order objects; two bags that differ by one item | Partial |
| Bar model, difference, unit price | L4 strong: part-whole, comparison, times as many, before and after; L9 GF7 (bottle half poured) is the same move as 20-13 | Covered | Price per piece when money is shared by what each paid (20-12); the P3 SPEC avoids ratio, so keep it as "price per sweet" | **Prepared** |
| Guess and check, optimise | L10 C2 (guess, check, improve); L9 TH5 (20¢ and 50¢ coins, 9 coins, $3) is the 19-22 move | Covered | "Most digits for a fixed amount of sticks, then make the biggest number" (20-23: L10 has matchstick patterns but never this); fewest and most pieces | Partial |
| Time and calendar | L9: durations, 24-hour clock, time lines; GF3 (station clock 10 minutes fast) is 20-7; L5 GF8 (day of week 100 days on) is 20-4; L5 TH6 (50th shape) is the cycle idea | Covered | Try-both-orders timetable (19-10: L9 TH4 is a one-route bus); a sequence that also has a 7-day cycle (19-13); counting backwards in days | **Prepared**; small extension |
| Counting figures, choices, gaps and posts | L1 listing, L8 organised counting (angles at a point, GF2 staircase), L10 GF2 squares in a 3 by 3 and GF3 handshakes | Counting rectangles or triangles by size in a drawing is only touched (squares); lamp-post-and-gap counting is nowhere (L10's "4th from front, 6th from back" is a cousin) | Multiply choices with a restriction; rectangles by size in a grid; gaps and posts, on a line and on a ring | **Real gap**, partial |
| Area and perimeter | L7: perimeter, area, "change the shape" (push out, cut, fill); TH8 (6 squares, biggest perimeter) is 19-12; GF3, GF4 | Shaded-region by joining half squares (20-21): L7 lists "cut up or fill in" but I found no half-square item | "Lengthen one side by x, the perimeter grows by 2x" (20-17) | **Prepared**; light extension |
| Graphs | L10 core C4 (scale with halves), TH5, GF4, GF9 (bar graph) | Bar graphs with a scale: covered | A pictogram with a key that is not 1 (19-18). Level 1 has picture graphs but Level 3 has none | **Prepared** for bar graphs |

### Summary of status across the 50 problems

- **Prepared (P) 15**: mostly cryptarithms, bar models, graphs, area, time, place value, logic, working backwards, the doubling sequence.
- **Partly prepared (Part) 21**: the method is taught but the contest twist is not (pairing, counting by size, try-both-orders, price per item, series).
- **Gap 14**: 19-2, 19-4, 19-7, 19-8, 19-11, 19-15, 19-17, 20-3, 20-6, 20-9, 20-14, 20-15, 20-16, 20-23. Spatial and picture items are 7 of the 14; divisibility, fence-post, series sum, operator, balance scales and sticks are the other 7.

## 5. Biggest gaps, in the order I would weigh them

1. **Spatial thinking (top view, mirror, cube stacks, nets): 4 problems, plus 3 picture-pattern problems that use the same eye.** All Section A, nothing in the program. Cheapest fix is a recurring 5-minute warm-up with real cubes or a cube drawing, not a lesson. (Texts for it are in the drafts file; the picture-only items need drawings.)
2. **Divisibility by 3 and counting multiples in a range: 4 problems, every one a Section A item, repeated across both years.** Short teaching (digit sum; "2 and 3 means 6"; "100 divided by 6, then take away the ones before 14") would turn an easy 2-mark item into a safe one. These are not in the Primary 3 scheme the SPEC lists, so it is an owner decision whether to teach them.
3. **Counting systematically, especially gaps and posts and objects by size: 4 problems.** The "number of lamps is one more than the number of gaps" trap is the same off-by-one the L10 queue item hints at, but it is never taught as such.
4. **Series by pairing and rule discovery: 3 problems (19-17, 20-8, 20-16).** 20-8 is covered. The other two are Section B and the 4-mark ones.
5. **Mental pairing for long sums: 2 problems (19-1, 20-1), both the first question.** Level 3 teaches careful column work; contest openers reward "make tens".
6. **Optimising with a fixed resource (20-23) and shape sums where one cell is in several lines (20-24).** Both are the hardest items in the 2020 paper (band H).

## 6. Where Think harder and Go further need extension

- **Think harder is generally well pitched** for the contest's M-band problems in L1, L2, L4, L5, L7, L9 and L10. The contest's E and M items would mostly be comfortable for a child who finishes the printed Think harder pages. The exceptions are the gap types in section 5, where Start here and Think harder both have nothing.
- **Go further does not yet reach the contest's H band in the gap types.** Existing Go further items (for example L1 GF3, L2 GF9, L4 GF2, L5 GF8, L9 GF7, L10 GF2) cover the H-band items in prepared types. For the gap types there is no Go further item, and Think harder is empty too, so the draft problems in `g3_original_problems_draft.md` are written as Go further and flagged as draft until the owner decides whether to add a Start here and a Think harder step before them.
- Go further asks open-ended "make up your own" and "change one number" items (posing, extension). The contest has none of that. That is fine; it is a program choice, not a gap.

## 7. Honest notes where evidence is thin

- Two papers, 50 problems, one coder. Frequencies are indicative. One occurrence of a type is not a trend.
- Picture-based items: status "Gap" for the spatial types assumes the figures need the 3D skill the solutions describe; I did not re-run them independently.
- I read lesson content in `p3/content/*.js` and `p3/SPEC.md` and the earlier audits (`audit_p3.md`, `gifted_p3.md`). I searched for keywords (mirror, top view, cube, divisible by 3, digit sum, lantern, post, balance, picture graph, Gauss-style sums, matchstick) and found no matches for the Gap types. The slides, scripts and the Weekly Dose were not re-read item by item, so an item that exists only there would be missed. Lessons 6 and 8 have no contest counterpart in these two papers: no fractions problem and no angle problem appeared, so the contest evidence says nothing about those two lessons either way.
- Contest-specific skills the program does not train and these papers do reward: option elimination on a five-choice paper with negative marking, "none of the above" answers, writing a whole-number answer in a grid. They are exam skills, not maths, and the program has no timed practice.
- Level 3's SPEC bars multipliers and divisors of 2 digits and ratio. 20-12 (share by what each paid), 20-14 (132 divided by 11) and 20-16 (71 times 15) sit just outside it. The drafts keep within the SPEC.
- No lesson, slide, workbook or question-bank file was changed.
