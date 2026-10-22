# SASMO Grade 2 (Primary 2) contest book: what it tests and how Level 2 prepares for it

Analysis only. No lesson files were changed. Contest problems are not reproduced here: they are referred to by year and question number (for example 16-13 is 2016, Question 13) and by a short skill tag. The question text, my own answer key and a few notes are in the git-ignored private file `docs/sasmo/private_solution_notes_g2.md`.

## 1. What was analysed, and how far to trust it

- One scanned book of 98 pages: "SASMO Primary 2 (Grade 2) GEP Practice, 5 Year Series, 2014 to 2018, Contest Problems with Full Solutions" (Henry Ong, Merlan Nagidulin, Rosa Anajao; copyright SIMCC 2018). It holds five papers and worked solutions for every problem (book pages 51 to 92). That is why no private solving was needed: the private file is only my independent answer check plus the places where the printed problem or solution needs care.
- **110 problems:** 2014 (15 questions), 2015 (20), 2016 (25), 2017 (25), 2018 (25). The 2014 and 2015 papers are shorter, so the format changed over the years.
- Format as printed: in 2014 and 2015, Q1 to Q10 are multiple choice (five options A to E) and the rest need a written answer; in 2016 to 2018, Q1 to Q15 are multiple choice and Q16 to Q25 are written answers. Totals: 65 early multiple-choice problems ("A") and 45 later written-answer problems ("B"). The book does not print marks per question or the time limit. It says only that a perfect score is 85 points; 15 questions at 3 marks plus 10 at 4 marks would make 85, but that is my inference, not stated. Calculators are not allowed.
- The book's own advice matches the Level 2 routine: draw a picture, make a list or table, try a simpler problem, use logic, guess and check, work backwards.
- Categories are my single-coder judgement. Each problem is filed under one main skill, so counts are indicative. About eight problems depend on pictures that I read from the scan. Four need care:
  - 15-19 as printed does not say what the brother has; the book's solution quietly assumes the remaining coins can be shared equally.
  - 14-15's solution text is muddled (it talks about "at least 5" segments, then shows the usual 4-segment path that goes outside the dots).
  - 16-13 depends on which cells are already filled in the cross figure; I used the book's answer.
  - 16-5 is read as two apples and three bananas, as the book does.
- The five papers are 2014 to 2018. Newer papers may differ. Five papers is a small sample: a type with 1 to 3 problems is "occasionally seen", not "tested".
- SASMO Grade 1 is analysed separately (`g1_analysis.md`). I did not merge counts across grades.
- The contest is not the school syllabus. It uses the 6 to 9 times tables, numbers above 1000 and kilometre to centimetre changes. Level 2 deliberately does not (`p2/SPEC.md`: only the 2, 3, 4, 5 and 10 tables, nothing above 1000). Three problems are outside Level 2 by rule (14-8, 17-18, 18-5); they are marked "out of rule" below.

## 2. Catalogue: frequency by type

A = early multiple choice, B = later written answer. Codes at the end of each row show my verdict per problem (W well prepared, E close idea but new format or extension needed, G real gap, X out of rule), in the order the problems are listed.

| Type (thinking move it needs) | All | A | B | Where it appears | Verdicts |
|---|---|---|---|---|---|
| Logic: order, elimination, track who gives what, "who can know" (tabulate, cross out, chain comparisons) | 9 | 6 | 3 | 14-12, 15-4, 16-9, 16-10, 16-18, 16-24, 17-2, 17-14, 18-14 | W E W E E W E E W |
| Number sense and clever computing: pair numbers to make tens, group repeated sums, count digits by place, careful reading | 10 | 6 | 4 | 14-1, 14-4, 14-8, 15-2, 15-14, 16-16, 17-17, 18-1, 18-8, 18-19 | G W X W G G G W W G |
| Multiples, common multiples, remainders (list the table, find the shared numbers, use the nearest multiple) | 7 | 3 | 4 | 14-5, 15-12, 16-11, 16-17, 17-7, 17-18, 18-20 | W W E W W X E |
| Bar-model word problems: sum and difference, "n times as many", transfers, leftovers, "take away the extra, share, give it back" | 7 | 1 | 6 | 14-13, 15-3, 15-11, 16-19, 16-20, 17-23, 18-22 | E E W W E W W |
| Picture and symbol equations, exchange chains, rules per shape (substitute; subtract one equation from another; undo) | 7 | 3 | 4 | 15-8, 15-16, 16-5, 17-13, 17-20, 18-21, 18-23 | E E E W E W E |
| Counting figures and ways: squares, triangles, dots, routes (count by size; count by structure; count routes) | 7 | 2 | 5 | 15-20, 16-23, 17-1, 17-21, 17-22, 18-3, 18-18 | W W E G W E G |
| Fence-post and cuts: gaps versus items, queue positions, cuts versus pieces | 5 | 3 | 2 | 14-2, 15-17, 15-18, 16-3, 17-12 | W E W W E |
| Number sequences: add the two before, steps that grow, two rules mixed | 5 | 5 | 0 | 14-3, 15-6, 16-4, 17-5, 18-7 | G G G G G |
| Age problems (the gap between two ages never changes) | 5 | 4 | 1 | 14-10, 15-10, 16-12, 16-22, 17-6 | G G G G G |
| Calendar, days of the week, unit change | 5 | 5 | 0 | 15-1, 15-5, 16-2, 18-5, 18-13 | G G G X G |
| 3D: cube stacks, room-corner views, rotation, nets | 5 | 4 | 1 | 15-13, 16-8, 16-14, 16-15, 17-10 | W E G E E |
| Visual perception: same picture, shadow, mirror, compare heights | 5 | 5 | 0 | 17-4, 17-11, 18-2, 18-4, 18-10 | G G G G G |
| Repeating and moving patterns (core length; moves in a grid; attribute tables) | 4 | 4 | 0 | 16-1, 17-3, 17-8, 18-11 | W W E E |
| Letter-digit sums (start in the ones column; carry limits) | 3 | 0 | 3 | 14-11, 16-25, 18-24 | E E E |
| Growing patterns (sticks, squares, tiles) | 3 | 2 | 1 | 14-14, 15-7, 18-12 | W E W |
| Working backwards (halves, give away, share) | 3 | 3 | 0 | 15-9, 17-15, 18-15 | W W E |
| Reading picture graphs and tables | 3 | 1 | 2 | 16-21, 17-16, 18-6 | W W E |
| Money | 2 | 1 | 1 | 14-9, 15-19 | W E |
| Legs and heads | 2 | 1 | 1 | 16-6, 18-17 | W W |
| Worst case ("how many must you take to be sure") | 2 | 0 | 2 | 15-15, 17-25 | G G |
| Rate and doing things at the same time | 2 | 1 | 1 | 16-7, 18-16 | G G |
| Cross-sum and addition-pyramid puzzles | 2 | 1 | 1 | 16-13, 17-19 | W E |
| Constraint grids (hexagon "minesweeper", digits that surround a square) | 2 | 0 | 2 | 17-24, 18-25 | G G |
| One-off puzzles (nine dots, one-stroke drawing) | 2 | 1 | 1 | 14-15, 17-9 | G G |
| Single problems: repeated exchange (14-6), careful reading (14-7), 2D shape composition (18-9) | 3 | 3 | 0 | 14-6, 14-7, 18-9 | E W E |

**Totals by my verdict:** well prepared 38 (35%), close idea but new format or extension needed 34 (31%), real gap 35 (32%), out of rule 3 (3%).

Repeats worth noticing (these are the most predictable parts of the contest):
- The add-the-two-before sequence appears in 2014 and again in 2015; a sequence appears in the first 7 questions every year.
- A picture or symbol equation appears every year from 2015 to 2018.
- A sum that is easy once you pair the numbers appears once a year from 2015 to 2018 (15-14, 16-16, 17-17, 18-19), always as a written answer.
- Letter-digit sums appear in 2014, 2016 and 2018; "how many must I take to be sure" in 2015 and 2017.
- Cubes in the corner of a room appear in 2016 and 2017.

## 3. Difficulty band as the paper presents it

- **Early multiple choice (65 problems)** is mostly short and visual: all 5 sequences, all 5 calendar and unit problems, all 5 visual-perception problems, all 4 repeating patterns, all 3 working-backwards problems and 4 of 5 age problems are here. Of these 65 problems, 22 are real gaps for Level 2 and 21 more need an extension. A child who is good at multi-step reasoning but has never met a changing-step sequence, an age problem or a calendar question loses cheap points.
- **Later written answers (45 problems)** is where reasoning lives: 6 of 7 bar-model problems, all 3 letter-digit sums, both worst-case problems, both constraint grids, 5 of 7 counting problems and 4 of 7 symbol equations. Of these 45, 13 are gaps and 13 more need an extension. The gap items here are the pairing sums (4), routes and points (2), worst case (2), constraint grids (2), and one each of rate, ages and the nine-dots puzzle.
- Difficulty also rises within each paper: the last two or three questions (for example 16-25, 17-24, 17-25, 18-24, 18-25) are letter-digit sums, grids or worst-case problems.

## 4. How Level 2 maps to it

Level 2 lessons: L1 numbers to 1000 (digit cards); L2 missing digits, add and take away within 1000; L3 legs, wheels, arrays and the 2, 3, 4, 5, 10 tables; L4 patterns with multiplication; L5 working backwards; L6 money; L7 fractions; L8 shapes, cube stacks, nets; L9 length, mass, volume, time, balance and jug puzzles; L10 mixed puzzles and logic. Tiers: Start here (core), Think harder (stretch), Go further (challenge and the open investigation).

| Type | What Level 2 already has | Tiers | Extension or gap | Verdict |
|---|---|---|---|---|
| Logic (9) | L10: ordering from clues, 3 by 3 logic grid, one answer only; Go further removes one clue at a time; L10 coin-order puzzle | Start here: chain of heights. Think harder: colours by elimination. Go further: four-person grid | Not met: tracking transfers one by one, "fits inside" chains with equal sizes, "I know your marble", card-flip logic. These are reading-and-tracking skills, not new topics | Prepared for order and elimination; **extension needed** for the other forms |
| Number sense and clever computing (10) | L1 digits printed on pages 1 to 120 and the digit 3 in 300 to 399 (same move as 18-8); L2 compensation (299 + 101 = 300 + 100); L3 equal groups | Go further L1, Think harder L2 | **Pairing sums (the first and last add to the same total) are not taught anywhere.** Order of operations with times zero and the 7 and 8 tables are out of rule | **Real gap** for pairing (4); rest prepared |
| Multiples and remainders (7) | L3: numbers in two tables, groups with leftovers; L4: lights flashing together, both counts, "one more than a multiple" | Think harder L3, Go further L3 and L4 | Contest multiples (15, 21) are bigger than Level 2 tables; the method is the same | **Well prepared**; keep numbers in rule |
| Bar-model word problems (7) | L2 boxes A, B, C from pair totals; L5 three children with extras, "twice as many", transfer between two boxes; L6 pen and pencil; L7 cake shares with extras; L10 cake slices | Go further in L2, L5, L6, L7, L10 | Not met: "5 times as many" with totals to 300, leftover-in-both-shares problems, corners counted twice, half-full container | **Well prepared**; extension for ratio, leftovers and corners |
| Symbol equations (7) | L9 balance puzzles (substitute, take one off both sides); L5 machines and rule finding; L2 [ ] + 150 = 550 − [ ] | Think harder L9, L5 | Never shown as "a picture stands for a number". Exchange chains are the L9 balance idea in another coat | **Prepared; one new card** to show the format |
| Counting figures and ways (7) | L8: squares by size, rectangles, triangles by line, 4 by 3 and 5 by 5 grids; L1, L3, L6 listing and "find all" | Think harder and Go further L8 | Not met: counting dots by structure, routes along a grid, triangles from chosen points | **Well prepared** for squares and triangles; extension for routes and points |
| Fence-post and cuts (5) | L9 ribbons with overlaps; rope cut into pieces (cuts versus pieces); L10 rope and pieces | Think harder, Go further L9 | Not met: floors, lamp posts, queue positions and circular tracks | **Prepared**; new contexts only |
| Number sequences (5) | L4: rules with a constant step, "will 30 be in the pattern" | Start here to Go further L4 | **Not met:** add the two before, steps that grow, two rules mixed. One sequence sits in the first 7 questions of every paper | **Real gap, small to teach** |
| Age problems (5) | L5 before-and-after bars; L5 "the gap at the start is double what was given" (same idea, no ages) | Go further L5 | **Not met:** ages in 3 years, "when I was your age", the age gap never changes | **Real gap**, easy to teach with L5 bars |
| Calendar and units (5) | L9 clock times and durations to 5 minutes, am and pm | Think harder L9 | **Not met:** days of the week cycle, "30 days from today", weeks to hours; kilometres to centimetres is out of rule | **Real gap** (calendar) |
| 3D (5) | L8: cube stacks by layer, stacks such as 4 by 2 by 2, steps and pyramids, painted cubes, nets A to F cut out and folded | Core to Go further L8 | Not met: room-corner pictures with walls, turning a block picture, dice faces | Layers **well prepared**; rotation is a gap; the audit already notes L8 is hard |
| Visual perception (5) | None | None | Same picture, shadow, mirror, compare heights. Partly a practice effect and hard to teach in words | **Real gap**, low value |
| Repeating and moving patterns (4) | L4 core and "far place" questions with multiples | Start here to Go further L4 | Not met: pieces that move round a 2 by 2 grid, attribute tables where each row is different | Repeating **well prepared**; movement **extension** |
| Letter-digit sums (3) | L2 missing digits with one or two boxes, "carry may be more than 1", find all (10 ways) | Go further L2 | Only the letters and "different letters, different digits" are new | **Prepared**; one new card |
| Growing patterns (3) | L4 stick rows (+4), towers (+3); L8 triangles in a triangle (3, 6, 10, 15) | Think harder L4, Go further L8 | Growth that itself grows (triangular numbers) is not asked as a prediction | Linear **well prepared**; growth **extension** |
| Working backwards (3) | L5 half then add, bars, shares; L6 half then spend; L10 bus and stickers | Core to Go further, three lessons | None | **Over-prepared** |
| Picture graphs and tables (3) | L10 picture graph with a key of 5 and 10, lost key | Think harder, Go further L10 | Tables of 4-digit scores go above 1000 | **Well prepared** |
| Money, legs and heads (4) | L6, L3 (hens and goats, bicycles, tricycles) | Core to Go further | None | **Over-prepared** |
| Worst case (2) | None | None | "How many to be sure". It is an act-it-out idea with a counter bag | **Real gap** (small share, both 4-mark style) |
| Rate and doing things together (2) | L9 tank and tap (a rate), no "more helpers, less time" | Think harder L9 | Egg-boiling and workers-and-days ideas | **Real gap** (thin: 2 problems) |
| Cross sums and pyramids (2) | L2 magic squares and triangles, guess and check | Think harder, Go further L2 | The addition pyramid is new, but it is the magic-triangle thinking | **Prepared** |
| Constraint grids (2) | L10 3 by 3 logic grid | Go further L10 | Hexagon grids and digits that surround a square | **Gap**, thin evidence |
| One-off puzzles (2) | None | None | Nine dots, one-stroke drawing. Fun, very low frequency | **Optional** |

## 5. Gaps in order of size

1. **Short sequences with a changing rule** (5 problems, all early). Cheap to teach, in the first 7 questions of the contest.
2. **Pairing sums** (4, one every year from 2015 to 2018, all written answers). Very cheap marks for a child who knows the trick.
3. **Age problems** (5, 4 of them early).
4. **Calendar and day-of-week arithmetic** (5, one out of rule).
5. **Visual perception and mirror or shadow items** (5, all early). Mostly a practice effect.
6. **Worst case** (2) and **rate** (2): small shares but distinct thinking moves, and both worst-case problems are written answers.
7. **3D rotation** (1 to 2) and **constraint grids** (2).

Extensions rather than gaps (idea exists, the contest format is new): logic forms (5), picture equations (5), counting routes and points (2), ratio and leftover bar models (3), letter-digit sums (3), moving patterns (2), growth by triangular numbers (1).

## 6. Recommendations

- Do not describe Level 2 as SASMO or olympiad preparation, and do not suggest results (this agrees with the gifted audit's list of claims to avoid). It is honest to say that about a third of these problems are types the level already teaches well, another third use thinking moves it already teaches in a different format, and the rest need new content.
- If the owner wants to close gaps, keep them as optional Go further cards and do not change Start here. Suggested homes: changing-step sequences next to L4; pairing sums in L2; ages in L5 beside the before-and-after bars; calendar and days of the week in L9; worst case as an act-it-out puzzle in L10; picture equations as one card in L9 beside the balance puzzles.
- Do not build a visual-perception strand. Two mirror-clock items are in the draft set if a warm-up is wanted.
- Keep every new item inside the Level 2 rules (tables 2, 3, 4, 5, 10; numbers to 1000; no decimals except money). The contest breaks these rules in three problems.
- Original practice drafts for gaps 1 to 7 and for the main extension types are in `docs/sasmo/g2_original_problems_draft.md` (draft, not yet in the program). Check them with a tutor before use.
- Before building anything big, get one more year's papers (2019 onwards) and a few real child attempts: the evidence here is one five-year book and my categorisation.

## 7. Addendum (22 Oct 2026): the 2020 and 2022 papers

Four files were uploaded after the sections above were written. Two of them add new Grade 2 papers; the others are duplicates or another grade.

### 7.1 What the new files were

| File (start of name) | Pages | What it is | New? |
|---|---|---|---|
| 9d30fa1a G2 | 24 | "Primary 2 (Grade 2) GEP Practice, 2020, Contest Problems with Full Solutions" (SIMCC). Questions pp 1 to 13, the publisher's worked solutions pp 14 to 24. | **New: 2020, 25 problems, solutions supplied** |
| a52eb14e "Sasmo Grade 2 past paper 2014-2018" | 66 | A phone scan of the question pages only of the 2014, 2015, 2016, 2017 and 2018 papers (pp 1 to 42, no solutions), followed by the same 2020 booklet again (pp 43 to 66). I spot-checked 2014 Q1 to Q15, 2015 Q1 to Q6 and 2018 Q5, Q6, Q24, Q25 against the book analysed above. | **Duplicate** of the 2014 to 2018 book and of the 2020 file; nothing new |
| ea383ceb "Untitled" | 16 | The official **SASMO 2022 Primary 2 contest paper**: cover with rules, a rough-working page, Q1 to Q25. **No answers or solutions.** | **New: 2022, 25 problems, no solutions (I solved them, privately)** |
| ce8a5cc9 G4 | 22 | Grade 4, 2019 (see `g4_analysis.md`) | Another grade |

The 2019 and 2021 Grade 2 papers are still missing, so the book's five years plus 2020 and 2022 make **seven papers and 160 problems**.

New format evidence from the 2022 cover and the section headings in both new papers: 25 questions in 1 hour 30 minutes (the minimum stay is 1 hour); no calculators; Section A is Q1 to 15, five options, **2 points each, minus 1 for a wrong answer, no penalty for blank**; Section B is Q16 to 25, **4 points each**, written as a 4-digit grid (answer 7 is shaded 0007). That is a maximum of 70. This **replaces my inference in section 1** that the book's perfect score of 85 was 15 questions at 3 marks plus 10 at 4 marks: the 2020 and 2022 papers print 2 and 4, and I do not know whether the older papers differed.

### 7.2 Catalogue of the new 50 problems

Verdict as in section 2: W = Level 2 prepares it, E = close idea or new format, G = real gap, X = out of rule for Level 2 (a 6, 7, 8 or 9 times table or a 2-digit by 1-digit step beyond the 2, 3, 4, 5, 10 tables). Difficulty bands were not rated for these.

| ID | Sec | Skill tag | Type | Verdict |
|---|---|---|---|---|
| 20-1 | A | Count dots in a ring by rows | Counting figures | E |
| 20-2 | A | Two missing items in a repeating strip | Repeating patterns | W |
| 20-3 | A | Months with exactly 30 days | Calendar | G |
| 20-4 | A | Match a key shape to a lock | Visual perception | G |
| 20-5 | A | Next term, gaps grow by 3 as they fall | Sequences | G |
| 20-6 | A | Two prices, total and difference | Bar model | W |
| 20-7 | A | Cubes in a room-corner stack | 3D | E |
| 20-8 | A | Age now from a past age, brother older, age later | Age | G |
| 20-9 | A | Three balance scales, three fruits | Symbol equations | E |
| 20-10 | A | Both sell the same, difference stays | Bar model | W |
| 20-11 | A | Exchange chain of pots and cups, one volume given | Symbol equations | E |
| 20-12 | A | 3 by 3 grid of plants, each feature cycles | Repeating patterns | E |
| 20-13 | A | Two-digit even numbers in the 3 and 5 tables | Multiples | W |
| 20-14 | A | Round table, who is in which year | Logic | E |
| 20-15 | A | Which flat net makes the pyramid | 3D | G |
| 20-16 | B | Sum of eight 2-digit numbers by pairing | Number sense | G |
| 20-17 | B | Triangles in a crown figure by size | Counting figures | W |
| 20-18 | B | Picture graph with a key of 7 | Graphs | X |
| 20-19 | B | Group a sentence: 3 x 13 + 5 x 13 = A x 8 | Number sense | X |
| 20-20 | B | Smallest number from exactly 27 matchsticks | Optimise under a limit (new type) | G |
| 20-21 | B | 3-digit even number from clues | Number sense | W |
| 20-22 | B | Ways for three different dice to total 12 | Counting ways | E |
| 20-23 | B | Heads and legs, cows and chickens | Legs and heads | W |
| 20-24 | B | Worst case: draws to be sure of 3 red | Worst case | G |
| 20-25 | B | Letter addition, 3-digit plus 2-digit | Letter-digit sums | E |
| 22-1 | A | Sum of eight numbers, pair to make tens | Number sense | G |
| 22-2 | A | Shadow of an animal | Visual perception | G |
| 22-3 | A | Next term, gaps grow by 1 as they fall | Sequences | G |
| 22-4 | A | Length of one object from a ruler and repeated copies in a picture | Measure from a picture (new) | E |
| 22-5 | A | Pyramid of cubes, painted, exactly 2 faces painted | 3D | E |
| 22-6 | A | Sum of evens minus sum of odds, 1 to 40 | Number sense | G |
| 22-7 | A | Opening hours with a break | Time | E |
| 22-8 | A | Greatest equal piece from two ribbons | Multiples | E |
| 22-9 | A | Nested shapes, missing figure | Repeating patterns | E |
| 22-10 | A | Sum of the first ten terms of "add the two before" | Sequences | G |
| 22-11 | A | Queue order from clues | Logic | W |
| 22-12 | A | Rows from front and back, place in the row, total desks | Fence-post and positions | E |
| 22-13 | A | Circle rule from three examples (a times b with a plus 1 each) | Symbol equations | X |
| 22-14 | A | Next year that uses only two digits | Number sense | E |
| 22-15 | A | Money: give half, then a third | Bar model | G |
| 22-16 | B | Picture graph with a key of 3 | Graphs | W |
| 22-17 | B | Triangles in a figure | Counting figures | W |
| 22-18 | B | Sentence with a shape times 6 | Symbol equations | X |
| 22-19 | B | Smallest 4-digit even number from four cards | Number sense | W |
| 22-20 | B | Ages: three times now, mother three times at 18 | Age | G |
| 22-21 | B | More and fewer than a day, total, find the first day | Bar model | W |
| 22-22 | B | Animal equations, one of them a square | Symbol equations | X |
| 22-23 | B | Trees every 7 m along paths of a plot | Fence-post and positions | E |
| 22-24 | B | Letter addition, 2-digit plus 2-digit | Letter-digit sums | E |
| 22-25 | B | Digits 1 to 8 around shaded squares | Constraint grids | G |

New 50 by verdict: W 12, E 17, G 16, X 5. By section: A 30, B 20.

### 7.3 Updated counts (110 + 50 = 160 problems)

By verdict: well prepared 50 (31%), close idea or extension 51 (32%), real gap 51 (32%), out of rule 8 (5%). Out-of-rule items rose from 3 to 8: five of the new 50 (10%) need the 6, 7, 8 or 9 table.

Type counts after adding the new papers (old count plus new): number sense and clever computing 17 (10 + 7); picture and symbol equations 12 (7 + 5); logic 11 (9 + 2); bar-model word problems 11 (7 + 4); counting figures and ways 11 (7 + 4); multiples 9 (7 + 2); number sequences 8 (5 + 3); 3D 8 (5 + 3); fence-post and positions 7 (5 + 2); age problems 7 (5 + 2); calendar and time 7 (5 + 2); visual perception 7 (5 + 2); repeating patterns 7 (4 + 3); letter-digit sums 5 (3 + 2); graphs and tables 5 (3 + 2); legs and heads 3 (2 + 1); worst case 3 (2 + 1); constraint grids 3 (2 + 1); two new single types, optimise under a limit (1) and measure from a picture (1). Types with no new problem keep their old counts (growing patterns 3, working backwards 3, money 2, rate 2, cross sums 2, one-offs 2, single problems 3). These sum to 160.

### 7.4 What the new papers add

- **Every earlier pattern repeats.** A changing-gap sequence is in the first 10 questions of all seven papers (2014 to 2018, 2020, 2022), and the 2022 paper has three sequence items. A sum that is easy once paired appears in 2015, 2016, 2017, 2018, 2020 and 2022 (twice in 2022). Age problems appear in 2014, 2015, 2016, 2017, 2020 and 2022. A letter-digit sum appears in five of the seven papers (2014, 2016, 2018, 2020, 2022); a "how many to be sure" worst case in three (2015, 2017, 2020). A "digits around a shaded square" or hexagon constraint grid is the last or second-to-last Section B item in 2017, 2018 and 2022. A triangle-counting figure is Q17 in both 2020 and 2022. Cubes in the corner of a room appear in 2016, 2017 and 2020.
- **Matchsticks.** 20-20 ("the smallest number from exactly 27 sticks") is a new type here and the same idea as the Grade 3 20-23 (`g3_analysis.md`): most digits for a fixed number of sticks, then the smallest first digit that still works. Two different grades in the same year suggests it is a recurring setter's idea. It is one problem per paper, so low priority.
- **Fractions of money.** 22-15 asks for half, then a third, of an amount of money between two people. Level 2's plan reaches "half of 36 sweets" at Go further only. This is the first fraction-of-an-amount item in the Grade 2 papers.
- **Out-of-rule content is growing.** The new X items are 20-18 (key of 7), 20-19 (x 8), 22-13 (6 x 9), 22-18 (x 6) and 22-22 (a square of 7). Do not chase them: keep Level 2 inside the 2, 3, 4, 5, 10 tables.
- **Unusual items worth a sentence.** 22-14 (the next year using two digits) and 22-8 (the greatest equal piece) are number-sense items in a new coat. 22-12 and 22-23 are the fence-post and position idea in a classroom and a plot of land (22-23 is ambiguous, see 7.5).

### 7.5 Evidence-thin notes for the new papers

- The 2022 paper has no answers in the file. I solved every 2022 problem except 22-2, and checked them by script where a script applies. Five need care: **22-2 (shadow) I did not solve** (picture only, no reliable reading); **22-4** reads a ruler from a drawing (stapler about 14 cm, so the eraser is 6 cm); **22-5** depends on whether the painted bottom of the pyramid counts (the first drawing shows the underside with a grid, so I read it as painted, giving 4; if the bottom is not painted the answer is 16, and both are answer options); **22-17** is 13 on my reading of the lines; **22-23** is 39 if the trees stand on every corner and are shared, 40 if the trees may avoid the corners, and the question's "greatest" does not settle which the setter meant. The 2022 answers are in the git-ignored `private_solution_notes_g2.md`.
- For 2020 I re-derived by hand all the answers that depend on text only (20-3, 5, 6, 8 to 11, 13, 16, 18 to 25) and they matched the booklet. The picture items (20-1, 2, 4, 7, 12, 15, 17) follow the publisher.
- Two papers added to five is still a small sample. A type with 1 to 3 problems is "occasionally seen", not "tested".

### 7.6 Effect on the gaps and recommendations in sections 5 and 6

- The order of gaps is unchanged, and the evidence for gaps 1 to 4 is stronger: changing-gap sequences (8 problems now), pairing sums (7), age problems (7), and calendar (7).
- **New items to place:** worst case moves up (3 papers, written answer each time); the constraint grid is now a 3-in-7 repeat; fractions of an amount of money has one new example; matchsticks is one new example.
- Visual perception is now 7 problems, all Section A. The recommendation stands: a three-minute warm-up routine, not a strand.
- The term-plan lessons that should change because of this evidence are listed in the session report, not here, since this file does not edit the plan.
