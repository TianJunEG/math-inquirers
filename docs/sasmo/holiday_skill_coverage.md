# Holiday program vs SASMO skills: coverage map, gaps and proposed additions (Levels 1 to 6)

Docs only. No lesson, workbook, deck, question bank or tool file was changed. Written 23 Oct 2026.

Why this exists: owner decision of 23 Oct 2026 (`docs/terms/owner_decisions.md`, entry "extension books Levels 2-6"): we do NOT copy SASMO questions, but the SKILLS needed to answer such questions must be covered in the HOLIDAY program. The extension books stay 100% original items. This file is the skill-coverage map that decision asked for.

Privacy: no SASMO question text, no distinctive SASMO numbers and no paper/question IDs appear here. Skills are named generically and counts come from the committed analysis files (`docs/sasmo/g1_analysis.md` to `g6_analysis.md`, `k_analysis.md`). The git-ignored `private_*` sources were not needed.

## 0. How to read this file

**Mapping.** Level N = SASMO Grade N (Level 6 maps to Grade 6). The SEAMO Kindergarten sample (`k_analysis.md`) is a different organiser and is context only (section 1.4).

**Sources checked (current working tree, 23 Oct).** Level 1: `hp/lessons.js`, `hp/qbank.json`, `hp/gaps.json`. Levels 2 to 6: `pN/SPEC.md` and every item in `pN/content/l1.js` to `l10.js` (core, Think harder, Go further). Spine: `levels/spine.json`. I re-read every question bank and grepped all lesson content (lesson, deck, script, workbook text) for each gap skill (pairing, digit sum, divisibility, cryptarithm, calendar, ages, worst case, "to be sure", add-the-two-before, mirror/shadow/top view/room corner, triangles by size, ratio, speed, Latin square, largest impossible total, chance). The verdicts below are mine, checked against the analysis files; where they differ I say so.

**Verdict words.**
- **Covered**: a child practises the skill in a printed or live item in the holiday lessons.
- **Partly**: the underlying idea is practised but the contest form (format, size of numbers, a second step) is not.
- **Not covered**: no holiday item at all (grep and read both agree).

**Where an item reaches a child (marks used in evidence).** Rule from each `pN/SPEC.md` and `hp/workbook_html.js` / `hp/guide.js`:
- `*` = prints in the workbook: Think harder T1 to T4 (the first four stretch items) and the last three Go further items (G7 to G9 at Levels 2 to 6; the last three of the list at Level 1, which has 4 to 7 Go further items per lesson).
- `^` = on the live "Think harder slide" for early finishers: T5 to T7.
- no mark = tutor question bank only (the tutor can set it live; it is not on any page the child holds).
- "C" = Start here (core). Core items print too.
Two sneak-peek puzzles and one investigation per lesson also exist (`gaps.json`, `gaps.js`, `inv.js`); they are not counted as evidence of practice unless named.

**Strategy-card tools (the eight tools in `levels/spine.json`).** 1 Spot the pattern, 2 List every way, 3 Draw it, 4 Make a table, 5 Work backwards, 6 Guess and check, 7 Try something simpler, 8 Act it out. Each lesson has one "tool of the day" (spine `main`) plus up to three "also" tools; section 5 shows the host lesson's own tool so you can see whether a proposed skill fits it. Short names used below: Pattern, List, Draw, Table, Backwards, Guess, Simpler, Act out.

**Evidence strength (from the analyses).** Grade 1: 4 papers, 100 problems. Grade 2: 7 papers, 160 problems (8 of them out of the Level 2 table rule). Grade 3: 2 papers, 50. Grade 4: ONE paper, 25 (very thin; I lean on cross-grade repeats). Grade 5: 3 papers, 75. Grade 6: 5 papers, 125 (the 2015 paper has a different mix). A type with 1 to 3 problems is "occasionally seen", not "tested". Counts are single-coder and each problem is filed under one main skill.

**Delivery routes and the print freeze.** Workbooks are frozen for print on Mon 2 Nov (print order Fri 6 Nov). Decks, tutor guides and the question banks are digital. I have ASSUMED they are not part of the print freeze and can still change before the first lessons (Tue 24 Nov). That assumption needs the owner's confirmation (see section 7).

---

## 1. Level 1 (SASMO Grade 1: 100 problems, 4 papers)

### 1.1 Coverage table

| SASMO skill or question type (count) | Holiday lesson(s) and item evidence | Verdict | Strategy-card tools |
|---|---|---|---|
| Place value, tens and ones, digit cards, odd/even digit puzzles (14) | None. Every Level 1 lesson stays within about 50; no tens-and-ones, digit-card or 2-digit item exists in L1 to L10 (read and grepped). Odd/even is only sorting in L8 C5, C6. | Not covered | List, Table, Act out |
| Mental computation: make tens, balance both sides of "=", compensate (13; 12 are cheap Section A marks) | L2 bonds to 10 and 20 (C1 to C9); balance "=" in L2 T1*, T3*, T5^; L2 T11 (28 + __ = 30 style, bank). Not met: pairing 3 to 4 addends to make tens; adding two-digit numbers; compensating 38 + 25 style. | Partly | Simpler, Pattern, List |
| Sequences and rule patterns (10) | Constant steps and "find the rule": L1 C1 to C8, T1* to T4*, T5^ to T7^. Changing gaps: L1 G3 (gaps shrink, bank), L1 G4* (gaps grow by 1), L4 G4* (dot numbers 1, 3, 6, 10, 15). Not met: "each term is the sum of the two before", two rules woven together, rule per digit. | Partly | Pattern, Table |
| Visual perception: same picture, shadow, odd one out, missing piece (8, all Section A) | None. By design: practice effect, hard to teach in words (g1 and g2 analyses). | Not covered | none fits (at most Act out) |
| Time and calendar: clock chunks, durations, days of the week (7) | None anywhere in L1 to L10 (no clock, no calendar, no weekday cycle; "week" appears only as a saving-per-week pattern, L1 T12). | Not covered | Pattern (cycle of 7), Table, Draw (time line), Act out (paper clock) |
| Ordering and logic: chain comparisons, elimination (7) | L8: C1 to C4 chains, T1* to T4*, T5^ four pets grid, T6^, T8 and T9 bank; G1 (every label wrong, bank), G3 (all orders, bank), G5 two loops; L10 T6. Circular seating not met (minor). | Covered | Table, Draw, List |
| Bar-model word problems: compare, transfer, "times as many", ages (7, all Section B) | Difference and undo stories: L5 T1*, T2*, T6; L2 C8, G6*; L9 G4* (three pieces, plus and minus); L10 G3* (three children). Not met: "times as many", "in 3 years" ages, one group giving to another until equal. | Partly | Draw, Backwards |
| 3D and spatial: cube stacks, top view, folding (6, all Section A) | None. L9 uses cubes only as a unit of length; L7 T7* diagonal cuts are 2D. | Not covered | Act out, Draw |
| Counting figures: squares, triangles, dots by structure (6) | L7: T2*, T3*, T5^, T6^, T8 (squares and rectangles in grids, triangles in a diagonal square); G3 to G6 (triangles from lines 3, 6, 10; nested squares G5*). | Covered | List, Simpler, Table, Pattern |
| Counting ways: coins, pairs, orders, routes (5) | L2 T2*, T4*, T7^ (pairs); L6 T1* to T4*, T5^ (coin ways); L8 G3 (orders, bank); L10 T3, T5. Not met: two-stage choices, numbers from digit cards. | Covered (two-stage and digit-card forms missing) | List |
| Repeating patterns: find the core, predict far places (4) | L4: C1 to C7, T1* to T4*, T5^ to T7^, G2 (two cores together), G3, G5 (own pattern). | Covered | Pattern, Table |
| Picture equations with symbols (4, all Section B) | L2 T6^ (A + A + 4 = 20), T10 (same number in two boxes, bank), G5* (two circles and a square = 12; one circle and two squares = 9). Not met: subtract one line from another with three symbols; a times sign. | Partly | Guess, Table, Backwards |
| Measurement: length, capacity, weight, unit change (3) | L9 is length and unit chains only: T1* to T4* (ruler marks, two ribbons, clips and cubes, eraser-pencil-ruler chain), T6^, T10. Capacity and weight not met. | Covered for length; capacity and weight not | Draw, Table |
| Constraint grids: Latin square, digit-surround (3, all Section B) | L2 G7* (magic triangle with 2 to 7), L8 T5^ (four people, four pets). No 4 by 4 Latin square or digit-surround. | Partly | Table, Guess, List |
| Multiplication and division facts as the main skill (2) | Skip counting only (L1 in 2, 3, 4, 5, 10; L9 T5 equal pieces). No times sign, no equal groups with a remainder. | Partly (preparation only; boundary of the Primary 1 syllabus) | Pattern, Draw |
| Money (1) | L6 in full (C1 to C8, T1* to T10, G1 to G6). | Covered (over-prepared) | List, Table |

Type-level tally (100 problems, my reading): covered 26, partly 39, not covered 35 (the 35 = place value 14 + visual 8 + time 7 + 3D 6). The Grade 1 analysis already says the same: largest gaps are place value, two-digit mental arithmetic and changing-step sequences.

### 1.2 Gaps ranked by SASMO frequency (Grade 1)

| Rank | Gap | SASMO count | Verdict |
|---|---|---|---|
| 1 | Place value, tens and ones, digit cards | 14 | Not covered |
| 2 | Two-digit mental arithmetic, make tens, compensate | 13 | Partly |
| 3 | Sequences beyond a constant step (sum of two before, woven rules) | part of 10 | Partly |
| 4 | Visual perception | 8 | Not covered (by design) |
| 5 | Time and calendar | 7 | Not covered |
| 5= | Bar-model forms: times as many, ages, transfer | part of 7 | Partly |
| 7 | 3D cube stacks and folding | 6 | Not covered |
| 8 | Symbol equations, two or three symbols | 4 | Partly |
| 9 | Constraint grids (4 by 4) | 3 | Partly |
| 10 | Multiplication facts | 2 | Partly (syllabus edge) |

### 1.3 Proposals (generic item ideas, not items)

1. **Place value and digit cards (14).** Host: L2 Number Bond Inquiry (spine main List; the lesson's own skills line already says "structure of numbers, systematic listing"). Add one Go further (print, swap for a printed item of an over-served skill) in which a child makes every 2-digit number from two or three given digit cards and answers a "biggest, smallest, closest to a target" question; and one Think harder slide item on "how many tens and how many ones". Tools: List, Table, Act out (real digit cards). Extension fallback: the Level 1 extension unit 2 (follows lesson 2) can carry the volume, because this is a whole strand; the holiday needs only the entry point.
2. **Two-digit mental arithmetic (13).** Host: L2 (balance and "make 10"). One Think harder slide item: add a short list of numbers by pairing to tens, and one "compensate" step (add 9 as add 10 take 1), staying within 100. Tools: Simpler, Pattern.
3. **Changing-step sequences (rest of 10).** Host: L1 Count with the Frog (spine Pattern; G3 and G4 already do shrinking and growing gaps). One bank/slide item where each number is the sum of the two before, with a table of the "gap" column. Tools: Pattern, Table.
4. **Time and calendar (7).** Two hosts. L4 Pattern Inquiry (Pattern + Simpler): days of the week as a repeating core of 7, a Go further "what day is it N days later" item (print swap). L9 Measure It!: a Think harder slide item on reading o'clock and half past and on counting minutes in chunks on a paper clock. Tools: Pattern, Table, Act out. Extension fallback: extension unit 4 or 9 for volume of practice.
5. **Bar-model forms (rest of 7).** Hosts: L3 Fruit Party (Draw): a Think harder slide item where a picture graph key makes one row "twice as many" as another; L5 Mystery Number (Backwards): an "in 3 years" story where the gap between two ages stays the same. Tools: Draw, Backwards.
6. **3D cube stacks (6).** Host: L7 Shape Safari (skills line already says "spatial reasoning"). One bank item with real cubes: count the cubes in a drawn stack including one hidden behind another. Tools: Act out, Draw. Extension fallback is the better home for repeated practice because the items need drawings.
7. **Symbol equations (4).** Host: L2 (already has G5*). One bank item with three symbols where one line is subtracted from another. Tools: Guess, Table, Backwards.
8. **Visual perception (8): do not build a strand.** At most a 3-minute optional warm-up (spot the difference) in L7; the extension book is the home.
9. **Constraint grids and multiplication facts: leave to the extension book.** Evidence is thin (3 and 2 problems) and neither suits a holiday session.

### 1.4 Kindergarten context (SEAMO sample, not SASMO)

The 10-problem K sample (`k_analysis.md`) is spatial/visual 4, sequences 3, equations 3. Its gaps are the same as Level 1's: cube counting and cuts (no Level 1 item), add-the-two-before sequences, two-line picture equations, undo with doubling. Nothing extra is proposed for K; the Level 1 additions above close the Level 1 end of it. The K2 Starter Pack named in `k2/k2.py` has no file in the repository.

---

## 2. Level 2 (SASMO Grade 2: 160 problems, 7 papers)

Level 2 rule (`p2/SPEC.md`): tables 2, 3, 4, 5, 10 only; numbers to 1000; no decimals except money. Eight SASMO problems break it and are not chased.

### 2.1 Coverage table

| SASMO skill or question type (count) | Holiday lesson(s) and item evidence | Verdict | Strategy-card tools |
|---|---|---|---|
| Pairing sums: first and last make the same total (7 of the 17 "number sense" problems; one in nearly every paper since 2015) | None (grep: zero hits for pairing, first and last, or consecutive in P2 content). | Not covered | Simpler, Pattern, Draw |
| Other clever computing: digits by place, compensation (10) | L1 G9* (digit 3 in 300 to 399), G5 (digits on pages 1 to 120, bank), T3*; L2 C6, T4*, T7^ (compensation without adding). | Covered | Simpler, List |
| Picture and symbol equations, exchange chains, rule per shape (12) | L9 T1*, T3*, G8* (balance with fruit and cubes: substitute, remove from both sides); L2 G8* (three boxes from pair totals); L5 T1*, T9 (machine from two IN/OUT). Never posed as "a picture stands for a number" (two sums sharing pictures); exchange chains only by balance. | Partly (idea covered, format new) | Guess, Backwards, Table, Draw |
| Logic: order, elimination, tracking, "who can know" (11) | L10 C6 (height chain), T7^ (colours), G2 (4 people grid, take clues away, bank), G8* (coin ownership); L2 none. Not met: tracking transfers one by one, "I know your marble", card-flip logic. | Covered for order and elimination; tracking forms missing | Table, List, Draw |
| Bar-model word problems incl. transfers and fractions of money (11) | L5 T2*, T4*, G1, G3, G9*; L2 G8*; L6 T9, G6, G7* (half, then half); L7 G7*; L10 G3. Not met: "5 times as many" with totals to 300; leftover-in-both-shares. | Covered | Draw, Backwards |
| Counting figures and ways (11) | L8 T2*, T6^, G7*, G8* (5 by 5 squares), G9*; L3 T1*, T8; L6 T2*, T3*, T4* (ways to pay); L8 G2, G6 (triangles, bank). Not met: routes along a grid; triangles from chosen points. | Covered (routes and points missing) | List, Simpler, Table |
| Multiples, common multiples, remainders (9) | L3 T7^, T8, G6, G8*; L4 T5^, G7*, G9*. | Covered | List, Table, Pattern |
| Number sequences: sum of two before, growing or shrinking gaps, woven rules (8, in the first 10 questions of every paper) | L4 constant-step rules and "will 30 be in it" (T7^, G3); L4 G1 alternate +5, +1 (bank); L10 T2*, G4 (totals that grow by a growing amount, bank). Not met: gaps that grow or shrink by 1 or 2; add the two before; two rules woven. | Not covered in the contest form | Pattern, Table |
| 3D: cube stacks, room-corner views, nets, painted cubes (8) | L8 T1*, T3* (nets E, F), T4*, T7^, T8, G3, G4, G7*, G9* (painted cubes). Not met: room-corner pictures with walls; which flat net makes a pyramid; rotating a block picture. | Partly (layers strong) | Act out, Draw, Table |
| Fence-post and positions: gaps vs items, cuts vs pieces, queue places (7) | L9 T7^ (ribbons overlap), G2 (rope cuts, bank); L10 T8 (pieces and cuts, bank). Not met: posts along a path, queue from front and back, ring track. | Partly | Draw, Simpler, Act out |
| Age problems: the gap never changes (7) | None (grep: no "years old" item in P2). L5 G3 (equal totals after a transfer) is the same bar idea with no ages. | Not covered | Draw, Table, Guess |
| Calendar and days of the week (7 with time) | Time and durations are covered (L9 C4 to C6, T2*, T5^, T6^, G3, G9*). No weekday cycle, no "N days from today" anywhere in P2. | Not covered for calendar; covered for clock durations | Pattern, Table |
| Visual perception: mirror, shadow, same picture (7) | None. By design. | Not covered | none |
| Repeating and moving patterns (7) | L4: C2, C4, T1* to T3*, T5^ to T7^, G4, G6, G7* (strong for repeating). Not met: pieces moving round a grid; attribute tables. | Covered for repeating; movement missing | Pattern, Table |
| Letter-digit sums (5) | L2 T2* (three numbers, carry may exceed 1), G7* (four boxes, find all). Boxes, not letters; "different letters, different digits" never used at Level 2. | Partly (Level 3 L2 teaches the letters) | Guess, List, Backwards |
| Graphs and tables (5) | L10 C2, T1* (key of 5), T2* (table), G7* (lost key). | Covered | Table, Draw |
| Legs and heads (3), growing patterns (3), working backwards (3), money (2) | L3 T1*, T2*, T6^, G2, G3, G7*, G9*; L4 T4*, G2, G8*; L5 whole lesson; L6 whole lesson. | Covered (over-prepared) | Table, Guess, Backwards |
| Worst case: "how many to be sure" (3, written answers) | None in any P2 lesson (grep: no "to be sure", "worst", "pigeon"). | Not covered | Act out, List, Simpler |
| Constraint grids: hexagon minesweeper, digits that surround a square (3, last or second-to-last Section B item) | L10 G2 (4-person logic grid, bank) only. | Not covered | Guess, List, Table |
| Rate and doing things at the same time (2) | L9 T8 (tap adds litres each 10 minutes, bank); L9 G2 (time per cut). "More helpers, less time" not met. | Partly | Table, Simpler |
| Cross sums and pyramids (2) | L2 T1*, T8, T9, G4 (magic triangle and square). Pyramid format is new but the thinking is the same. | Covered | Guess, Table |
| One-offs (nine dots, one-stroke), optimise under a limit, measure from a picture (4 singles) | L6 G2 (most different snacks for a fixed amount) is the nearest. | Not covered (low frequency) | Guess, Draw |

Problem-level view from `g2_analysis.md` (160 problems): well prepared 50, close idea or extension 51, real gap 51, out of rule 8.

### 2.2 Gaps ranked by SASMO frequency (Grade 2)

| Rank | Gap | SASMO count | Verdict |
|---|---|---|---|
| 1 | Picture and symbol equations (format card) | 12 | Partly |
| 2 | Changing-gap and add-two-before sequences | 8 | Not covered |
| 2= | 3D: room-corner views, pyramid net, rotation | 8 | Partly |
| 4 | Pairing sums | 7 | Not covered |
| 4= | Age problems | 7 | Not covered |
| 4= | Calendar and weekday arithmetic | 7 | Not covered |
| 4= | Visual perception | 7 | Not covered (by design) |
| 4= | Fence-post, queue and ring positions | 7 | Partly |
| 9 | Letter-digit sums | 5 | Partly |
| 10 | Worst case | 3 | Not covered |
| 10= | Constraint grids | 3 | Not covered |
| 12 | Rate, helpers and time | 2 | Partly |

The analysis file weighs sequences, pairing and ages as the cheapest, most predictable marks (a changing-gap sequence is in the first 10 questions of all seven papers; a pairing sum appears in six of seven).

### 2.3 Proposals (generic item ideas)

1. **Picture and symbol equations (12).** Host: L9 Measure Masters (Table + Act out; the balance puzzles are already here). One bank item posed as "a picture stands for a number": two sums that share pictures, solved by comparing the sums. Tools: Guess, Backwards, Table. Delivery: slide/bank. Extension fallback: also fine for unit 9, but one card in the holiday is enough because the thinking is already taught.
2. **Changing-gap and add-two-before sequences (8).** Host: L4 Pattern Machines (Pattern + Table). One Think harder (print swap) where the gaps themselves grow by 1 each step, solved with a table that has a "gap" column, and one slide item where each number is the sum of the two before. Tools: Pattern, Table.
3. **3D (8).** Host: L8 Shape Builders (already the layers lesson). One slide item with cubes in the corner of a room (count by walls and floor). Tools: Act out, Draw. Extension fallback: pictures of rotation and nets need many drawings.
4. **Pairing sums (7).** Host: L2 Missing Digit Mysteries (the compensation items live here). One Go further (print swap): a run of numbers that pair up to a common total (words only, totals within 1000). Tools: Simpler (do 4 numbers first), Pattern, Draw (write it forwards and backwards).
5. **Age problems (7).** Host: L5 Mystery Number Machines (before-and-after bars). One Go further (print swap): "in 3 years" with the gap staying the same. Tools: Draw, Table, Guess.
6. **Calendar (7).** Host: L9 (weeks into days, "what day will it be N days on" as a cycle of 7) as a Think harder slide item. L4 is the alternative host (a calendar is a repeating core of 7). Tools: Pattern, Table.
7. **Fence-post and positions (7).** Host: L9 or L10. One slide item on posts along a straight path (gaps vs posts) and one on a queue "5th from front, 4th from back". Tools: Draw, Simpler.
8. **Letter-digit sums (5).** Host: L2. One slide item: the same missing-digit sum written with letters, "different letters mean different digits". Tools: Guess, List, Backwards.
9. **Worst case (3).** Host: L10 Puzzle Day (Act out + List is its working style). One Go further (print swap) with a bag of coloured counters, "how many must you take to be sure". Tools: Act out, List, Simpler.
10. **Constraint grids (3), rate (2), visual perception (7): leave to the extension book.** Constraint grids need drawn grids; rate is thin; visual perception is by design not a strand.

---

## 3. Level 3 (SASMO Grade 3: 50 problems, 2 papers)

Level 3 rule (`p3/SPEC.md`): no 2-digit multipliers or divisors, no ratio. A few SASMO items sit just outside (71 by 15, 132 divided by 11).

### 3.1 Coverage table

| SASMO skill or question type (count) | Holiday lesson(s) and item evidence | Verdict | Strategy-card tools |
|---|---|---|---|
| Pairing and series sums: pair numbers to make tens, first plus last (3, including both opening questions) | None (grep: nothing). L2 T4* (1099 vs 1999) and T7^ (9999 minus) use compensation only. | Not covered | Simpler, Pattern |
| Divisibility by 3 from digit sum; "2 and 3 means 6"; count multiples in a range (4, all Section A, repeated in both years) | L3 T1* (digit sums of the 9 times table), G3 (numbers up to 200 divisible by 6 and 9, bank), G6* no; L5 division. No test for 3, no "count multiples between two numbers". | Partly (digit-sum idea for 9 only) | Pattern, Table, Simpler |
| Place value and digit-restricted counting (4) | L1: T1* to T4*, T5^, T6^ (digit 5 in 1 to 100), G1 (odd digits), G3 (pages 1 to 120, bank), G6, G8*, G9*. | Covered | List, Table |
| Cryptarithms (2) | L2 strong: T1*, T2*, T3*, T4*, T6^ (AB + B = BA), T8, G1, G3, G4, G9* (ABC + ACB = CBA). | Covered (strongest match) | Guess, List, Backwards |
| Time and calendar (4, all Section A) | L9 C6, T2, T4* wait: T4* (timetable, one route), T6, T9, G3 (clock fast), G5; L5 G8* (day 100 days on), T6^ (50th shape cycle). Not met: two films, try both orders; a sequence that also has a 7-day cycle. | Covered (small extension) | Table, Draw, Pattern |
| Spatial: top view, mirror, cube stack in a corner, pyramid faces (4, all Section A) | None. L4 uses cube towers only as bars; L7 and L8 are flat. | Not covered | Act out, Draw |
| Picture patterns: missing shape, faces grid (3, all Section A) | None. | Not covered | Table, List (name each feature) |
| Counting: gaps and posts, rectangles or triangles by size, multiply choices (4) | L10 C1 (queue), G1, G8* (queue positions), G2 (squares 3 by 3, bank), G3 (handshakes, bank), T1*. Not met: lanterns on both sides of a river (gaps then posts, doubled); rectangles or triangles by size; choices with a restriction. | Partly | Draw, Simpler, List |
| Number patterns: rule from examples, two-number operator (1 operator, 1 series, 1 doubling) | Doubling covered at L1 T7^ (1, 3, 7, 15, 31 style). Operator from four examples: none. | Partly | Pattern, Table |
| Logic and ordering, bounds (3) | L10 C1, T2*, T6^, G4; "smallest and largest possible, so this total is impossible": not met. | Covered (bounds form missing) | List, Table, Guess |
| Symbol and balance equations incl. chains of 3 or more objects (3) | L4 T2*, T8, G2 (box and pens, $25 and $35), G6 (jugs and cups). Balance chains of three or more objects: not met. | Partly | Guess, Draw, Table |
| Bar model, difference, price per item (3) | L4 whole lesson; L9 G7*, G8*. | Covered | Draw, Backwards |
| Area and perimeter (3) | L7: T3*, T4*, G4, G6, G8, G9. Not met: half-square shaded regions; "lengthen one side by x". | Covered | Draw, List |
| Number grids and shape sums where one cell is in several lines (2, both Section B) | L2 T3* (pyramid), G5 (magic square). Not met: a Y or triangle where the centre counts three times. | Partly | Guess, Table |
| Guess and check, optimise under a limit (2) | L9 T5^ (20¢ and 50¢ coins, 9 coins); L10 C2. Not met: "most digits from a fixed number of sticks, then the biggest". | Partly | Guess, List |
| Graphs (2) | L10 C4, T5^, G5, G9*. Pictogram with key not 1 is not at Level 3. | Covered | Table, Draw |

Problem-level view from `g3_analysis.md`: prepared 15, partly 21, gap 14.

### 3.2 Gaps ranked by SASMO frequency (Grade 3)

| Rank | Gap | SASMO count | Verdict |
|---|---|---|---|
| 1 | Divisibility test for 3 and counting multiples in a range | 4 | Partly (test missing) |
| 1= | Spatial: top view, mirror, cube corner, pyramid | 4 | Not covered |
| 1= | Counting: gaps and posts, shapes by size | 4 | Partly |
| 4 | Pairing and series sums | 3 | Not covered |
| 4= | Picture patterns | 3 | Not covered |
| 4= | Balance and symbol chains | 3 | Partly |
| 7 | Shape-sum grid (shared cell) | 2 | Partly |
| 8 | Two-number operator | 1 | Not covered |
| 8= | Bounds, "this total is impossible" | 1 | Partly |
| 8= | Optimise with a fixed resource (sticks) | 1 | Partly |

### 3.3 Proposals

1. **Divisibility by 3 and multiples in a range (4).** Host: L3 Times Table Treasure (Pattern; T1* already looks at digit sums of the 9 table, so extend the same move to the 3 table). One Think harder slide item (digit sum of the 3 table, "in the 2 and the 3 table means in the 6 table") and one Go further (print swap) "how many multiples between two numbers, take away the early ones". Tools: Pattern, Table, Simpler.
2. **Spatial (4) and picture patterns (3).** Hosts: L7 Area Architects (squares on a grid: a top-view item with heights) and L10 Puzzle Day (a faces-in-a-grid item where each feature has its own cycle). Slide/bank only. Tools: Act out, Draw, Table. Extension fallback is better here for volume: these need many pictures, and real cubes cannot be assumed in every home. Do both a small holiday taster and an extension unit.
3. **Counting gaps and posts, shapes by size (4).** Host: L10 (queue items G1 and G8* sit here). One Go further (print swap) with lamp posts on both sides of a path (gaps then posts, doubled) and one slide item counting rectangles by size in a drawn house. Tools: Draw, Simpler, List.
4. **Pairing and series sums (3).** Host: L2 (compensation lives here). One Think harder slide item "add a list by pairing to tens and hundreds" and one Go further (print swap) for a stepping list by first plus last. Tools: Simpler, Pattern.
5. **Balance chains (3), shape-sum grid (2), operator (1), bounds (1), sticks (1).** Hosts: L4 (balance chain of three objects, Draw), L2 (shared-cell shape sum, Guess), L10 (operator from four examples; "smallest and largest possible so this total is impossible"; most digits from a fixed number of sticks). All slide/bank, one item each, low priority individually.

---

## 4. Level 4 (SASMO Grade 4: 25 problems, ONE paper)

One paper is thin evidence. `g4_analysis.md` leans on cross-grade repeats: the same thinking moves recur at every grade.

### 4.1 Coverage table

| SASMO skill or question type (count) | Holiday lesson(s) and item evidence | Verdict | Strategy-card tools |
|---|---|---|---|
| Divisibility: digit test for 6, remainders, factorial (3) | L1: T1* to T4* (factors), G2, G8* (remainder 1, divisors 2 to 6), G9*. "Multiple of 7 leaving 2" is the same move as G2/G8*. No digit test for 3 or 6, no "2 and 3 means 6", no factorial (grep: zero). | Partly (remainder form covered; digit test not) | Pattern, Table, List |
| Counting figures and ways: triangles by size, two-stage choices, digits in dates (3) | L8 G8 (ways to shade), L10 G1 (numbers with a 7), L2 G3, G7*, G9* (digit counting). Not met: "3 ways then 4 ways" multiplied; triangles by size in a drawing. | Partly | List, Simpler, Table |
| Number sequences: gaps that grow evenly, rule found from diagrams (2) | L2 T3 (constant step); L3 T6^ and G5 (each number the sum of the two before); L9 T3*, G1 (steady changes). Not met: gap of the gaps; rule from three or four diagrams. | Partly | Pattern, Table |
| Sums by pairing a run of numbers, mixed numbers that pair to wholes (2) | None. "Gauss" or pairing appears nowhere in P4 content. | Not covered | Simpler, Pattern |
| Time, calendar, schedules: weekday from a phrase, two events try both orders (2) | L6 clock-hand angles only; L1 T2*, G7* (meet again, multiples). No duration, timetable or weekday item. | Not covered | Table, Draw, Pattern |
| Chance and bounds: spinner, smallest and largest total of four dice (2, Section A) | None (grep: spinner, chance, likely, probability are absent from P4). | Not covered | List, Table |
| Fractions: compare shaded areas with half squares, fraction of what is left (2) | L4 whole lesson (T1* to T4*, T9, G2 to G9; "of the rest" G9, work-backwards G7). Shaded half squares compared by a common denominator: not met. | Covered (shaded-area comparison missing) | Draw, Backwards |
| Digit puzzles: digit product, hints on four numbers (2) | L2 T1*, T2*, T5^, G4; L5 T4*, T10, G1. | Covered | List, Guess |
| Letter-digit addition, cryptarithm (1; but present in 8 of the 10 Grade 2 to 4 papers) | None (grep: no "cryptarithm", no "each letter stands"). | Not covered | Guess, List, Backwards |
| Rate: best price per minute (1) | L5 T5 (price of one), T9 (divide a length). Comparing per-minute prices with a common denominator: not met. | Partly | Table, Draw |
| Balance-scale chains (1) | L5 G2 (3 apples and a pear, subtract one balance from another, bank). Chains to order objects: not met. | Partly | Draw, Table |
| Spatial: rope and knot (1) | None; not teachable in words. | Not covered (low value) | Act out |
| Area and perimeter (1) | L7 whole lesson. | Covered | Draw |
| Bar chart read, bar-model word problem (2) | L9 T1* to T4*, G7* to G9*; L3 T1*, T11, G6. | Covered | Table, Draw, Backwards |

Problem-level view from `g4_analysis.md` (25 problems): prepared 5, partly 13, gap 7.

### 4.2 Gaps ranked by SASMO frequency (Grade 4, backed by cross-grade repeats)

| Rank | Gap | Grade 4 count (plus cross-grade) | Verdict |
|---|---|---|---|
| 1 | Counting: two-stage choices, shapes by size, date digits | 3 | Partly |
| 1= | Divisibility test for 3 and 6; factorial | 1 to 2 of 3 (Grade 3 had 4, Grade 5 has 6) | Partly |
| 3 | Sequences with growing gaps, rule from diagrams | 2 | Partly |
| 3= | Pairing sums | 2 (every Grade 2 paper from 2015, Grade 3 both papers) | Not covered |
| 3= | Time, weekday, timetable | 2 (Grade 2: 7, Grade 3: 4) | Not covered |
| 3= | Chance and bounds | 2 (Grade 3 had the three-dice form) | Not covered |
| 7 | Cryptarithm | 1 (present in 8 of 10 papers across Grades 2 to 4) | Not covered |
| 7= | Rate per minute, balance chains, spatial rope | 1 each | Partly / Partly / Not covered |

### 4.3 Proposals

1. **Counting by stages and by size (3).** Host: L10 Puzzle Day (mixed heuristics). One slide item "3 ways then 4 ways, how many routes" (multiply the choices). Triangles by size: host L6 Angle Turns only as a bank fan-counting extension (L6 already counts angles in a fan); otherwise the extension book. Tools: List, Simpler, Table.
2. **Digit tests for 3 and 6 (3).** Host: L1 Factor Hunters (List; T4* and G8* are already about divisors). One Think harder slide item (digit sum for 3, "in the 2 table and the 3 table means the 6 table") and one Go further (print swap). Tools: Pattern, Table.
3. **Pairing sums (2).** Host: L3 Operation Detectives (chains and brackets live here). One Go further (print swap): a run of consecutive numbers by first plus last. Tools: Simpler, Pattern.
4. **Cryptarithm (1, but recurring).** Host: L2 Big Number Puzzles (digit riddles). One Think harder slide item and one Go further (print swap), same strand Level 3 teaches in its L2 (the Level 4 child may have never met it). Tools: Guess, List, Backwards.
5. **Chance and bounds (2).** Host: L10 (or L8 where dice appear). One Go further (print swap): "smallest and largest total of four dice, so which totals are impossible"; one slide item on a spinner with unequal sectors written as a fraction. Tools: List, Table.
6. **Time and weekdays (2).** Hosts: L1 (weekday after N days, a remainder question: fits the lesson's remainders) and L10 (a two-event timetable, try both orders). Slide/bank. Tools: Table, Pattern.
7. **Growing-gap sequences (2).** Host: L3 (add-two-before chains are already here at T6^, G5): add the gap-of-gaps step. Slide/bank. Tools: Pattern, Table.
8. **Rate per minute, balance chains, rope: leave to the extension book** (1 problem each; weak evidence).

---

## 5. Level 5 (SASMO Grade 5: 75 problems, 3 papers)

Level 5 SPEC deliberately avoids ratio notation (`a : b`), averages and speed (placed in P6). Some proposals below cross that line; they are flagged as owner decisions.

### 5.1 Coverage table

| SASMO skill or question type (count) | Holiday lesson(s) and item evidence | Verdict | Strategy-card tools |
|---|---|---|---|
| Ratio, percent, average (8) | Percent: L7 whole lesson (T1*, T2*, G7* to G9*). Units in word problems: L3 (T5, T8, T10, G4, G7*). No ratio notation, no averages anywhere in P5 (grep). Reading "a : b" as "a units to b units" never taught. | Partly (percent and units covered; notation and average not) | Draw, Table |
| Area, perimeter, volume (7) | L4 (T1* to T4*, G2 to G9), L5 (T1*, T4*, T5^ to T7^, G1, G6, G8). | Covered | Draw, Act out, Simpler |
| Systematic counting: figures, digits, arrangements, numbers within bounds (7) | L9 G5 (pages digits, bank), G9* (100th digit); L10 G2, G3 (rectangles by size), G4 (digit 4), T2; L1 T1*, T3*, G4 (palindromes). Not met: triangles by size in crossing lines; counting numbers inside bounds by cases on the first digit. | Partly | List, Simpler, Table |
| Word problems with units: ages, sets, extra and short, repeated halving (7) | L3 (C2, T3*, T7, G3, G7*, G8*, G9*), L10 G6 (monkey, bank). Two overlapping groups (Venn): not met. Extra and short: P3 L5 G9* has it, P5 does not. | Covered (overlap and extra-short missing) | Draw, Backwards |
| Divisibility, remainders, last digits, counting multiples in a range (6, five in Section A, two a year) | L10 T6^ (smallest number leaving 1) only; L1 digit-sum clue as a riddle. Nothing else (grep: no digit test, no "multiples between", no last digit of a power). | Not covered | Pattern, Table, Simpler |
| Computation and parity: regroup before calculating, which result is odd (5, every paper opens with these) | L1 brackets and estimation (T2*, T7, G5, G7*, T8, T9); parity only inside L9 T4*. No odd/even rules for results. | Partly | Simpler, Pattern |
| Number patterns: differences of differences, two sequences woven, operator from three examples (5, all Section A) | L9: C1 to C6 (linear), T4* (odd sums), G1, G7* (diamond figures 1, 5, 13), G6. Not met: gap of the gaps stated; two sequences woven; operator from examples. | Partly | Pattern, Table |
| Spatial: dice, rotated block figure, patterned cube faces, picture matrix, rope (5, all Section A) | L5 T4*, G8* (painted cubes) only. | Not covered (painted cubes only) | Act out, Draw |
| Logic and elimination (5) | L10 C4, G5, G9*, T4; L1 riddles; liars (workbook). Latin square with diagonals: not met. | Covered | Table, List |
| Least and greatest possible: parity cap, largest total you cannot make, minimise the biggest pile, a set with no multiples, equal-total matching (5; 3 in Section B, 3 band H; one or more each year) | L1 T4* ("test both sides of a target"), L10 T6^, L2 G5, L6 T2 (cheapest). None of the contest forms. | Not covered | Guess, List, Backwards |
| Fractions: of a remainder, undo, digit cards for fractions, nested (3) | L2 whole lesson (T9, G1 to G9*; telescoping G7*). Dividing by a fraction is beyond Level 5. | Covered | Draw, Backwards, Pattern |
| Speed and work rates (3) | L6: taps together (C5, T1*, G1), leak (T7), printers (T10), G3 machine starts later (bank), G8 candles, G9* bath and drain. "Catching up" and three builders: only G3/G8 partly. | Partly | Table, Draw |
| Cryptarithms and digit puzzles (3, all Section B) | None in P5 (Level 3 L2 teaches letters; Level 5 does not). | Not covered | Guess, List, Backwards |
| Colouring circles joined by lines (2) | None. | Not covered (low priority) | Guess, Draw |
| Whole-number totals: list every way to make a total (2) | L6 T2*, T6, L9 C6, T8, L10 T5, G8. | Covered | List, Table |
| Clocks and calendars: when do hands coincide, which weekday occurs most (2) | L8 T7^, T8 (angles of hands at o'clock); L9 T1* (cycle). No coincidence, no 365 = 52 weeks and 1 day. | Partly | Draw, Pattern |

Problem-level view from `g5_analysis.md` (75 problems): holiday prepared 18, partly 27, gap 30. (22 of the 30 gap items are Section A.)

### 5.2 Gaps ranked by SASMO frequency (Grade 5)

| Rank | Gap | SASMO count | Verdict |
|---|---|---|---|
| 1 | Ratio notation, average, ratio-with-change | 8 | Partly |
| 2 | Systematic counting: triangles by size, numbers within bounds | 7 | Partly |
| 3 | Divisibility, remainders, last digits, multiples in a range | 6 | Not covered |
| 4 | Computation opener and parity | 5 | Partly |
| 4= | Non-constant-step patterns | 5 | Partly |
| 4= | Spatial (dice, rotation, patterned faces) | 5 | Not covered |
| 4= | Least and greatest possible | 5 | Not covered |
| 8 | Speed and work (catching up, three workers) | 3 | Partly |
| 8= | Cryptarithms | 3 | Not covered |
| 10 | Colouring circles | 2 | Not covered |
| 10= | Clocks and calendars | 2 | Partly |

### 5.3 Proposals

1. **Ratio notation and average (8).** Owner decision first: P5 SPEC avoids notation on purpose. Cheap reading-skill version: host L3 Before and After (Backwards + Draw): one Think harder slide item written with "a : b" and solved with the units the child already knows; averages belong to Level 6 (L9) so leave them. Tools: Draw, Table. Extension fallback: a ten-minute vocabulary card in the extension unit 3 if the owner prefers the holiday to stay notation-free.
2. **Triangles by size and numbers within bounds (7).** Host: L10 Challenge Day (the rectangles-by-size items G2, G3 live here). One slide item counting triangles by size in a figure with crossing lines, and one counting numbers between two bounds by the first digit. Tools: List, Simpler, Table.
3. **Divisibility, remainders, last digits, multiples in a range (6).** Hosts: L1 Million Puzzles (digit-sum test for 3 and 9 as a riddle tool; Think harder print swap) and L9 Pattern Generalisers (Simpler + Pattern: last digit of a repeating product and counting multiples in a range; slide items). Tools: Pattern, Table, Simpler.
4. **Computation opener and parity (5).** Host: L1 as a 5-minute warm-up and one slide item (regroup before calculating; which result is odd). Tools: Simpler, Pattern.
5. **Non-constant-step patterns (5).** Host: L9 (Pattern Generalisers). One Think harder (print swap): gap of the gaps; one slide item: two sequences woven; one "operator from three examples". Tools: Pattern, Table.
6. **Least and greatest possible (5; the heaviest cluster by reward).** Host: L10 (Challenge Day, Go further) and L6 (packs and deals: "which totals cannot be paid with two pack sizes", slide). L10 gets one Go further (print swap): minimise the biggest pile or a parity cap. Tools: Guess, List, Backwards. Extension fallback is poor here: the skill is an argument ("why can no more be made"), best modelled live.
7. **Spatial (5).** Host: L5 Volume Vault (painted cubes already here; add dice with opposite faces and touching faces, bank). Tools: Act out, Draw. Extension fallback is better for picture-heavy practice.
8. **Cryptarithm (3, all 4-mark Section B).** Host: L1 (digit riddles, Guess). One Go further (print swap) with a letter addition. Tools: Guess, List, Backwards.
9. **Speed catching up, three workers, clock coincidences, colouring: slide/bank, one item each at most** (L6 for the first two, L8 for clocks). Colouring: leave to the extension book.

---

## 6. Level 6 (SASMO Grade 6: 125 problems, 5 papers)

Level 6 has no multiplier limit. Holiday L3 (negatives), L7 (turtle angles), L9 (means) and L6 (probability) have little or no SASMO counterpart: enrichment by design.

### 6.1 Coverage table

| SASMO skill or question type (count) | Holiday lesson(s) and item evidence | Verdict | Strategy-card tools |
|---|---|---|---|
| Divisibility, factors, LCM, remainders (14; 5 of them are digit tests for 3, 9, 45) | Factors, primes, LCM-like: L2 (T1* to T4*, G3, G8* eggs, G9* lockers), L8 (T3, G4, G5 remainders and cycles). Digit-sum tests: none (grep: zero). | Covered for factors and remainders; digit tests Not covered (5 of 14) | List, Pattern, Table |
| Sequences, patterns, periodic rules (11) | L1 whole lesson (T1* to T4*, G8*, G9*), L8 (T1*, T2*, T5^). | Covered | Pattern, Table |
| Ratio, percent, fraction word problems (10) | None in the holiday course (L9 is mean only; L4 G8* is an age problem with units). | Not covered | Draw, Table, Backwards |
| Logic, worst case, pigeonhole, optimising, largest impossible total (10) | None (grep: zero for "to be sure", "worst", "pigeon"). | Not covered | Act out, List, Simpler |
| Area, perimeter, circles, dissection (10) | None (L7 is angles only). | Not covered | Draw, Simpler, Act out |
| Rate, speed, work (9; in all five papers) | None in P6 (L4 T8* is a taxi fare, a rate in disguise, no speed). | Not covered | Table, Draw, Simpler |
| Digit counting and place value (8) | L5 T2*, T4*, G9* (digit sum 5), G3 (pages 1 to 120, bank), L1 T3*. | Covered | List, Simpler |
| Computation, identities, approximation (7, all Section A) | L4 machines only. No shortcut routine (square minus neighbours, factor out a common decimal). | Partly | Simpler, Pattern |
| Counting figures, arrangements, outcomes (7) | L5: C1 to C6, T1* to T4*, T5^ (diagonals), T6^ (rectangles in a strip), T7^ (orders), G1 (triangles from pentagon corners, bank), G6 (squares), G8*; L6 all 36 outcomes. Not met: triangles or rectangles by size in a drawing; rearrangements where nobody keeps their own place. | Partly | List, Simpler, Table |
| Fractions: nested, telescoping, optimising (6) | None in P6 (P5 L2 has telescoping at G7*; no P6 fraction lesson). | Not covered | Backwards, Draw, Pattern |
| Last digits, powers, trailing zeros (6) | L8 cycles and mod (T1*, T2*, T5^, T7), L2 T4* (code counts factors). Last digit of a power, trailing zeros, last two digits: not met. | Partly | Pattern, Table, Simpler |
| Algebra: equations, symbol and operator puzzles (5) | L4: T1* to T8, G1 to G9* (two machines G5, ages G8*). | Covered | Backwards, Guess, Table |
| Cryptarithms (5, all 4-mark Section B, one in every paper since 2019) | None (the P6 grep hits are Caesar "each letter", not letter sums). | Not covered | Guess, List, Backwards |
| Spatial: views, rotation, solids, painted cubes (5, all Section A) | None. | Not covered | Act out, Draw |
| Angles, clock hands, similar triangles (5) | L7 polygon turn angles (T1 to T8, G1 to G9*). Clock hand speeds (6 degrees and 0.5 degrees per minute): none at Level 6 (they are at Level 4 L6). | Partly | Draw, Pattern |
| Data, graphs, Venn counting (3) | L9 means (T1 to T8, G7* to G9*). Unlabelled bar chart and two-set counting: not met. | Partly | Table, Draw |
| Packing and tiling bounds (2), grid and picture-rule puzzles (2) | None. | Not covered (low priority) | Draw, Simpler |

Problem-level view from `g6_analysis.md` (125 problems): holiday prepared 24, partly 54, gap 47 (29 of the 47 in Section A). The term plan (Terms 2 to 4) would close 19 of those 47 only if its lessons are built; that is outside this file.

### 6.2 Gaps ranked by SASMO frequency (Grade 6)

| Rank | Gap | SASMO count | Verdict |
|---|---|---|---|
| 1 | Divisibility digit tests (3, 9, 45, "5 and 9 means 45") | 5 (of 14) | Not covered |
| 2 | Ratio, percent, fraction word problems | 10 | Not covered |
| 2= | Worst case, pigeonhole, largest impossible total, optimising | 10 | Not covered |
| 2= | Area, perimeter, circles, dissection | 10 | Not covered |
| 5 | Rate, speed, work | 9 | Not covered |
| 6 | Computation shortcuts | 7 | Partly |
| 6= | Counting by size, rearrangements | 7 | Partly |
| 8 | Nested and telescoping fractions | 6 | Not covered |
| 8= | Last digits, powers, trailing zeros | 6 | Partly |
| 10 | Cryptarithms | 5 | Not covered |
| 10= | Spatial | 5 | Not covered |
| 10= | Clock hands and similar triangles | 5 | Partly |
| 13 | Data: unlabelled bar chart, Venn | 3 | Partly |
| 14 | Packing bounds, grid-rule puzzles | 2 each | Not covered |

Note: ratio, percent and fraction, and area/circles, are whole-lesson topics in the term plan (L10, L12, L14). The holiday course cannot reasonably absorb them; it can carry a taster.

### 6.3 Proposals

1. **Digit tests and cryptarithms (10 combined; at least one every paper; the cryptarithms are all 4-mark items).** Hosts: L2 Prime Hunters (List + Simpler; digit sum for 3 and 9, "5 and 9 means 45", with the existing filter-with-mod code idea) and L8 Secret Codes (Pattern; "letters stand for digits" is a natural cousin of a cipher, and brute-force loops fit the coding bridge). Each gets one Go further (print swap) and one slide item. Tools: Guess, List, Backwards.
2. **Worst case, pigeonhole, unreachable totals (10).** Host: L5 Every Possible Way (Simpler + List): one Go further (print swap) "rest of the votes to the runner-up" worst case, one slide item with socks or counters (Act out). L10 Showcase: one slide item "largest total you cannot pay with two pack sizes". Tools: Act out, List, Simpler.
3. **Ratio, percent, fraction (10).** Taster only: L4 Algebra Machines gets one Think harder slide item with units and a before-and-after change; L9 gets one slide item "percent of a data set". The year plan (L10, L12) is the real home. Tools: Draw, Table, Backwards.
4. **Area, perimeter, circles, dissection (10).** Host: L7 Turtle Geometry (path perimeters of figures drawn by code, a staircase figure). Two slide items. Extension fallback is better for volume (needs drawings).
5. **Rate, speed, work (9).** Hosts: L1 Code the Pattern (two sequences meet, G8*, is already "catching up" in disguise: one Go further print swap on distance and speed, closing speed) and L4 Algebra Machines (distance = rate x time as an equation, pipes and leaks: slide items). Tools: Table, Draw, Simpler.
6. **Computation shortcuts (7).** Host: L4 as a 5-minute warm-up routine (one slide item each time): factor out a common number, square minus its neighbours. Tools: Simpler, Pattern.
7. **Counting by size, rearrangements (7).** Host: L5 (slide items): triangles by size, nobody in their own place. Tools: List, Simpler, Table.
8. **Nested and telescoping fractions (6).** Host: L1 (sequence sums; Pattern): telescoping sums as a slide item, building on P5 L2 G7*. Tools: Pattern, Backwards.
9. **Last digits, powers, trailing zeros (6).** Host: L8 (cycles) for last digit of a power (Go further print swap) and L2 for trailing zeros (counting 2s and 5s in a prime factorisation, slide item). Tools: Pattern, Table.
10. **Clock hands (part of 5).** Host: L7 (angles): one slide item with 6 degrees and 0.5 degrees per minute. Tools: Draw, Pattern.
11. **Spatial (5), packing (2), grid rules (2), unlabelled bar chart (3): leave to the extension book.**

---

## 7. Cross-level patterns, tool mapping and the print-freeze question

### 7.1 One skill, six levels (spiral)

The same thinking moves are asked at every grade; only the numbers grow (stated in `g4_analysis.md`). Writing one item family and scaling it by level is cheaper than six separate pieces of work. The strongest repeats:

| Skill | Grades where the analyses saw it | Holiday home that scales | Main tools |
|---|---|---|---|
| Pairing sums (first plus last) | G2 (7), G3 (3), G4 (2), G6 (1 explicit) | L2 at Levels 2 and 3; L3 at Level 4; L9 at Level 6 | Simpler, Pattern |
| Changing-gap and add-two-before sequences | G1 (part of 10), G2 (8), G3 (1), G4 (2), G5 (5) | L1 at Level 1; L4 at Level 2; L3 at Level 4; L9 at Level 5 | Pattern, Table |
| Digit tests and counting multiples in a range | G3 (4), G4 (3), G5 (6), G6 (5) | L3 at Level 3; L1 at Levels 4 and 5; L2 at Level 6 | Pattern, Table, Simpler |
| Cryptarithm / letter sums | G2 (5), G3 (2), G4 (1), G5 (3), G6 (5) | Already L2 at Level 3; add L2 at Level 2 (letters), L2 at Level 4, L1 at Level 5, L8 at Level 6 | Guess, List, Backwards |
| Worst case / least and greatest possible | G2 (3), G5 (5), G6 (10 with logic) | L10 at Level 2; L10 and L6 at Level 5; L5 and L10 at Level 6 | Act out, List, Guess |
| Time and calendar | G1 (7), G2 (7), G3 (4), G4 (2) | L4 or L9 at Levels 1 and 2; L1 and L10 at Level 4 | Pattern, Table |
| Age problems (gap never changes) | G1 (part of 7), G2 (7); covered from Level 3 | L5 at Levels 1 and 2 | Draw, Table |
| Spatial | all levels | Extension books (pictures, cubes) with a holiday taster in L7 or L8 | Act out, Draw |
| Triangles / shapes by size | G5 (2), G6 (3) | L10 at Level 5; L5 at Level 6 | List, Simpler |
| Visual perception | G1 (8), G2 (7), G3 (3) | Not built (by design) | none |

### 7.2 Strategy-card fit

Almost every proposed skill fits a tool the child already has: Pattern (sequences, calendars, digit tests, last digits), Simpler (pairing, area, rate, shortcuts), List (digit cards, cryptarithm cases, worst case, triangles by size), Table (sequences, rates, ages), Draw (ages, posts, ratio units, area), Backwards (cryptarithm ones column, telescoping, ages), Guess (cryptarithm, equations, grids, least and greatest), Act out (worst case with counters, cubes, clocks). Two have no good tool: visual perception and rope or knot items. The 8 tools are all used; none is missing for the proposed skills. The one tool-fit stretch: cryptarithm at L8 Secret Codes (main Pattern, not Guess). The skill still fits, because a cipher and a letter sum both ask "what does each symbol stand for", but the tutor should point at Guess and check on the card, not Pattern.

### 7.3 What stays out, on purpose

Visual perception (Grades 1 to 3, 8 + 7 + 3 problems) and the rope/knot item: not a strand. 6, 7, 8, 9 tables at Level 2 (rule). Option-elimination and answer-grid skills: exam technique, not maths, and the holiday has no timed practice.

---

## 8. Cost estimate (agent-hours, to add the proposed items)

One agent-hour = one hour of an agent working (same unit as `docs/school_books/plan.md` section 17). These are planning numbers, not measured. Assumptions:
- **Print item (swap one existing printed Think harder or Go further item for a new one):** about 1.5 h. Draft 0.3; independent solve and wrong-answer check 0.3; key, tutor-guide and deck text 0.2; regenerate workbook, guide and deck and visual check 0.4; audit 0.3.
- **Slide or bank item (T5 to T7 or tutor bank, no workbook change):** about 0.7 h (no workbook regeneration; one shared deck/guide rebuild per level).
- **Per-level fixed overhead:** 3 h when any printed page changes (validators, proof diff, rebuild, check against the print proof), 1 h when only slides and banks change.
- Because workbook pages are fixed, a new printed item must REPLACE an existing printed item (page space is the limit). Pick the item whose skill is over-served in that lesson.

The item counts below are the number of items proposed in each level's section above.

| Level | Proposed items | Printed swaps | Slide / bank | Hours (full, v2) | Hours (slide/bank only, before 24 Nov) | Hours (tiny: 2 print swaps) |
|---|---|---|---|---|---|---|
| 1 | 10 | 3 | 7 | 3 x 1.5 + 7 x 0.7 + 3 = about 12 | 7 x 0.7 + 1 = about 6 | 2 x 1.5 + 2 = 5 |
| 2 | 9 | 4 | 5 | 4 x 1.5 + 5 x 0.7 + 3 = about 12.5 | 5 x 0.7 + 1 = about 4.5 | 5 |
| 3 | 10 | 3 | 7 | 3 x 1.5 + 7 x 0.7 + 3 = about 12 | 7 x 0.7 + 1 = about 6 | 5 |
| 4 | 11 | 4 | 7 | 4 x 1.5 + 7 x 0.7 + 3 = about 14 | 7 x 0.7 + 1 = about 6 | 5 |
| 5 | 14 | 4 | 10 | 4 x 1.5 + 10 x 0.7 + 3 = about 16 | 10 x 0.7 + 1 = 8 | 5 |
| 6 | 21 | 6 | 15 | 6 x 1.5 + 15 x 0.7 + 3 = about 22.5 | 15 x 0.7 + 1 = about 11.5 | 5 |
| **Total** | **75** | **24** | **51** | **about 89 (round to 90)** | **about 42** | **about 30** |

Notes on the table:
- "Tiny" = at most two printed single-sentence swaps per level (no drawing), the cheapest high-count gaps (examples: pairing sums at Levels 2 and 3, digit test at Levels 3, 4 and 5, cryptarithm at Levels 4 and 6, changing-gap sequences at Levels 1 and 2). Even "tiny" needs a proof re-check after the Mon 2 Nov proof approval and before the Fri 6 Nov order, and the owner has only about 10 days. I would NOT recommend it unless the owner wants a particular skill printed in this cycle.
- **Unless the change is tiny and made before Mon 2 Nov, printed additions apply to a v2 / the next holiday cycle.** The full 89 hours is the v2 budget.
- Writing the item family once and scaling it by level (section 7.1) could take roughly 20 to 30 percent off the full figure; I have not applied that saving (untested assumption).
- Not included: owner time to approve items, tutor re-briefing, the Level 2 to 6 extension books (separate task), and any new figure drawings for spatial items (about 0.5 h per drawn figure extra).
- The slide/bank route (about 42 hours) reaches only children who finish early (the Think harder slide is for early finishers) and tutors who set bank items live. It is a real coverage gain but weaker than print: it does not give every child independent practice.

---

## 9. What to tell the owner (short)

1. **The holiday program already covers the reasoning habits SASMO rewards** (patterns, listing, bar models, working backwards, logic, area, money). It does not yet cover about a third of SASMO's skill types, and in each level the same few gaps account for most of it.
2. **Biggest gaps by level (from the SASMO counts).** Level 1: place value and tens and ones (14), two-digit mental arithmetic (13), time and calendar (7). Level 2: picture and symbol equations as a format (12), changing-gap sequences (8), pairing sums, ages and calendar (7 each). Level 3: divisibility by 3 and counting multiples (4), spatial (4), gaps-and-posts counting (4), pairing sums (3). Level 4: two-stage counting (3), digit tests, pairing sums, weekday and timetable, chance and bounds (2 each), cryptarithm (recurring). Level 5: ratio notation and average (8), counting triangles and numbers in bounds (7), divisibility and last digits (6), least and greatest possible (5), spatial (5). Level 6: digit tests and cryptarithms (10), worst case and pigeonhole (10), ratio and percent (10), area and circles (10), rate and speed (9).
3. **Most gaps are cheap to close and recur at several levels:** pairing sums, changing-gap and add-two-before sequences, digit tests for 3 and 9, cryptarithms, worst case, time and calendar. One item family per skill, scaled by level, fits a spiral through the 10 existing lessons. All map to strategy-card tools the child already has.
4. **Three kinds of gap should NOT go into the holiday:** visual perception (8 + 7 + 3 problems; not teachable in words), picture-heavy spatial items (best as extension-book pages, with only a small taster in L7, L8 or L5), and whole-topic gaps at Level 6 (ratio, percent, circles, speed), which are term-plan lessons, so the holiday should carry at most a one-item taster.
5. **Your wish to have the skills in the holiday itself can be met, but not in the printed workbooks this cycle.** The workbooks are frozen for print on Mon 2 Nov. Honest options: (a) do nothing in print, add the 51 slide and bank items (about 42 agent-hours) before the first lessons on Tue 24 Nov, if you confirm slides, guides and banks are not part of the print freeze; (b) also add two single-sentence printed swaps per level before Mon 2 Nov (about 30 agent-hours, risky in 10 days); (c) the full list of 75 items, 24 of them printed, as a v2 for the next holiday cycle (about 90 agent-hours).
6. **Decisions I need from you.** (i) Are slides, tutor guides and banks free to change after Mon 2 Nov? (ii) Should Level 5 teach reading "a : b" (the SPEC avoids ratio notation on purpose)? (iii) Do you want a Level 1 place-value entry point in lesson 2 even though Primary 1 numbers stay within about 50 in the holiday? (iv) Visual perception: confirm it stays out of the holiday and goes, if at all, to the extension books.
7. **Evidence caveat.** Grade 4 rests on one paper and Grade 3 on two; the strongest findings are the cross-grade repeats. Frequencies are single-coder. Before building anything large, a tutor should try a few of the proposed items with real children.
