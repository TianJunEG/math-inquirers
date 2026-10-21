# Fixes for the P4 gifted-style audit (docs/audit/gifted_p4.md)

Nothing was published and nothing was committed. Shared files (rebuild/slidekit.py, hp/*, levels/*) were NOT edited. Only `p4/content/l1.js` to `l10.js` and `rebuild/gen_p4l1.py` to `gen_p4l10.py` were changed (plus the two audit documents and `docs/audit/verify_gifted_p4.py`). The tier principle used: Core (and the workbook core pages) = low floor, startable with objects, drawing, counting, lists, guess-and-check or earlier-level skills; Think Harder = the taught idea in a new setting; Challenge = completed topic plus extension (multi-step, generalise, justify, combine, open-ended, "what if"). Bank order was kept so the printed Think Harder pages (Stretch 1-4 and the last three Challenge items) and the two Challenge slides (which each reuse bank items) still line up; every lesson now has one make-up-your-own / justify prompt in the Challenge bank, printed where a slot was free (slide Challenge items were left where they were).

Notation: C = Core bank, S = Stretch bank (S1-S4 print on the Think Harder page), X = Challenge bank (X7-X9 print), Q = workbook core-page question.

## Per lesson

### Lesson 1 Factor Hunters
- C1-C6 rewritten from formal tasks to objects: sweets in bags (use 12 counters), a frog jumping in 7s, sharing 52 stickers in two steps, counting in 3s and 5s, rectangles from 20 tiles, free sticker every 3rd and pen every 4th purchase (1-12). Old items (factors of 12; multiples of 7; "is 4 a factor of 52"; common multiple of 3 and 5; factor pairs of 20; smallest multiple of 4 and 6) were Core tier violations (vocabulary and formal method). Answers verified.
- Workbook Q5c: "Find ALL numbers 1-60 with exactly 3 factors" (Think Harder content) -> "Is 49 a number with exactly 3 factors? List its factors" (answer yes: 1, 7, 49). The find-all (4, 9, 25, 49) is now Stretch S4 (prints as Think Harder 4); the old "multiple of 7, digits add to 11" moved to S6 and "most factors under 30" to S7; "multiples of both 4 and 9" dropped. Key, ws2ans slide and slide notes updated.
- X5 laps -> "Ben says a multiple of 4 and 6 must be a multiple of 24: test it" (justify; answer: 12 is a counterexample, common multiples are multiples of 12). X7 three bells -> "Bus C gap so all three meet next at 9:36: find ALL (4, 12, 36), then make up a puzzle" (problem posing; verified by brute force).
- Tier moves: three bells (X7) dropped; laps (X5) replaced.

### Lesson 2 Big Number Puzzles
- C3 (round 27 649) and C6 (round 6352) now say "closer to which?" with a number line and the halfway mark. C1, C2, C4, C5 unchanged (earlier-level skills).
- Workbook Q2: star removed. Q2b ("rounds to 5350 to the nearest 10 AND 5400 to the nearest 100, find ALL") -> "rounds to 5350 to the nearest 10, find ALL (5345 to 5354, 10 numbers)". The two-clue version is Stretch S5 (replaced "smallest number that rounds to 80 000", which duplicated the taught example). Key, ws1ans slide, ws1 preview and notes updated; the optional two-clue teaching slide `p4l2-we4` is relabelled optional.
- S7 ("how many 5-digit numbers have all digits the same", core level) -> concert crowds 38 000 and 41 000 (smallest difference 2001, largest 3999).
- X4 (Mei x 6 = 24 000, one step) removed; the "digits different, add to 10" item moved up; X8 is a make-up-your-own riddle (model: rounds to 30 000, digits different, sum 12, odd: unique number 30 261, brute-forced). X7 and X9 left where the Challenge slides use them.

### Lesson 3 Operation Detectives
- C1-C4 (bare order-of-operations calculations) -> stories whose number sentence comes from the situation: 18 stickers + 6 packs of 3; 18 boys and 6 girls each buy 3 tickets; a 56 cm ribbon cut in 7, take 2; 90 children with 30 in 5 teams, one team leaves. C5 and C6 unchanged.
- Workbook Q1 stem gets a story hint (36 + 14 x 5 is 36 stickers and 5 packs of 14). Q3d (two pairs of brackets) removed from the page and moved to Stretch S10 (key, ws1 preview, ws1ans slide and notes updated).
- S7 (one number sentence for noodles and drinks, core level) -> use 2, 3, 4, 5 once each in a + b x c - d for the biggest answer (21; brute-forced).
- X1 now "four 4s make each of 1 to 5"; X2 (Collatz) and X3 (sum 1000, 4 times) removed; new X6 "3 times as many stickers; after a gift of 20 they are equal" (Siti 20, Ravi 60); X9 is a make-up task: change the number trick to end in 10, and invent a four-step trick that always ends in 3.

### Lesson 4 Fraction Frontier
- C1, C2, C4, C5, C6 (bare conversions and unlike fractions) -> pizza slices in thirds, chocolate quarters, counters in 4 and 3 groups, two folded strips (5/6 vs 2/3), a ribbon marked in tenths. C3 kept in spirit (32 counters in 4 groups, then "what fraction").
- Workbook: Q1 "Draw more bars if you need them"; Q4 "Your fraction wall or a drawing helps"; Q6 hint (a strip of 12 boxes, shade 1/3 then 3/4).
- X1 (twelfths between 1/4 and 2/3: Q6 with new numbers) -> "equal to 3/4, numerator and denominator add to 28". X6 (cake, one step per fraction) -> "Ben gives 1/3 to Ali and 1/4 to Mei, Ali gets 2 more: 24". X7 is the make-up task (1/2 and 1/3 taken, 5 left: 30; what if 7 left: 42; make up your own).

### Lesson 5 Decimal Detectives
- C1-C5 -> $3.47 from coins, $0.90 vs $0.89, "is 7.46 closer to 7.4 or 7.5" (number line), $1.25 x 3 (kept as money), a metre stick cut in tenths and hundredths (0.47 m), and a zoom-in number line (3.6 then 3.65). Old C1-C5 needed decimal notation and rounding.
- Workbook: Q2c deleted (it duplicated Stretch 1) and Q7 (starred mystery decimal) removed from the page; the mystery decimal is now Stretch S4 (4.687, unique by brute force). Key, ws1/ws2 previews, answer slides and the optional teach slide notes updated.
- X7 (cards 1,2,4,8 closest to 50, a repeat of S8) -> make up your own "closest to" puzzle, with "what if the target changes" (model cards 3,5,6,9: 39.65 for 40, 53.69 for 50).

### Lesson 6 Angle Turns
- C1-C6 start from a body turn ("stand and face the front"), a page corner (90 degrees), a compass written out with 45 degree steps, and a clock with 12 equal gaps.
- Workbook Q5c (two overlapping squares, Challenge level) removed; figure redrawn with panels (a) and (b) only (viewBox 380 wide). The idea is Challenge X9 (which already prints the overlap picture). Key, ws2ans slide, teachrect notes updated.
- S8 (rectangle corner 27 degrees, a Core repeat) -> "minute hand turns 150 degrees from 2:10: 2:35". X4 and X5 (minute and hour hand facts) replaced by "angle at 4:10" (65 degrees) and "Mei: 2 o'clock and 10 o'clock make the same angle: justify, find other pairs"; the duplicate 9:30 item is replaced by X7, a make-up task (choose a half-past time; model 9:30 = 105 degrees).

### Lesson 7 Area Architects II
- C1-C6 are draw-and-count tasks: squared paper, 12 tiles making every rectangle, walking round the edge, and "6 by 6 with a 2 by 2 corner cut: area 32, perimeter 24 unchanged". Old C3 (square perimeter 36 -> area) replaced; old C6 needed the push-out insight with no drawing.
- Workbook unchanged (all questions sit on a grid, so a child can count squares first).
- X3 (24 m fence, list pairs) merged with X4 into one item (a: no wall 36 m2, b: wall 72 m2). X6 (49 m2 garden + 2 m) -> a pattern task with +1, +2, +3 m (gains 15, 32, 51). X7 is the make-up task (fence, with or without a wall, prove by listing; model: 30 m, 56 m2 and 112 m2). X8 and X9 stay where the Challenge slides use them.

### Lesson 8 Symmetry and Nets
- C2 and C3 ("lines of symmetry" unexplained) -> fold a paper square (4 ways) and a paper rectangle (2 ways); C1 and C4 now say "hold a box / look at a dice"; C5 -> which of A, B, F, H, L, T fold to match (A, B, H, T); C6 -> tape 6 squares in a row.
- Workbook Q6b "why can no other square work?" (proof) -> "choose a square that does NOT work: where would its partner have to be?". Key unchanged (2 ways).
- S8 and slide Stretch item 3 (lines of symmetry of a 2 by 4 rectangle, a Core repeat) -> shade a 3 by 3 grid with exactly 1 line (3 squares) and exactly 2 lines (2 squares; brute-forced: 4 ways). X2 (recall: 11 nets) -> "show a cube net cannot have 5 in a row; most is 4". X4 replaced by the three-dice tower moved up; X7 is "design your own dice net with opposite faces adding to 7" (model 2,1,5,6 with 3 above and 4 below the 1).

### Lesson 9 Data Detectives
- C1, C4, C5 gain a small scaffold (draw the scale / sketch the graph / draw a bar for each). C2, C3, C6 unchanged.
- X4 (210 books + 15 each, three additions) removed; the "scale starts at 200" item moved up; X9 is the make-up task (choose a scale that makes 52, 54, 56, 58 look like a huge increase and one that makes it look flat; which is fair?).

### Lesson 10 Challenge Day
- C1-C6 gain small scaffolds (list your tries, draw 8 animals with 2 legs first, undo from 70, draw the queue, try 1 then 2 then 3 fifty-cent coins).
- X6 (half, +6, x3 = 48, a repeat of Q3b) removed; the uncle-and-Ben item moved up; X9 is the make-up task (your own heads-and-legs puzzle with one answer; explain why 12 heads and 35 legs is impossible: legs are always even).

## Numeric verification
`python3 docs/audit/verify_gifted_p4.py` (exact fractions and brute force; prints "all ok"). It covers every new or changed numeric answer and every find-all or unique claim: factor and multiple lists, the Bus C answers {4, 12, 36}, Ben's claim, exactly-3-factors numbers up to 60, rounding ranges (5345-5354, 5350-5354, concert differences 2001 and 3999, riddle 30 261 unique), the "biggest answer" 21, the four 4s expressions, 3 times as many (20 and 60), the number tricks, marbles 24 and sweets 30 / 42, decimal items and the unique mystery decimal 4.687, clock angles (65, 105, 75, 60 and the o'clock mirror pairs), 2:35, the area and fence answers (15, 32, 51; 36, 72, 56, 112), 3 by 3 symmetry counts (1 line, 2 lines, 6 ways, 2 ways), the A B H T letters, and the heads-and-legs model (6 cars, 4 motorcycles). The earlier open-box result (8 of 12 pentominoes fold, 11 hexomino nets) was re-checked by folding code.

## Regenerated deck keys
`rebuild/gen_p4l1.py` to `gen_p4l10.py` were run for all ten decks, then `python3 levels/restyle.py split/p4lK` on each. Decks changed in content: p4l1 (Q5c answer and notes), p4l2 (Q2b, ws1 preview and answers, we4 note), p4l3 (Q3d removed from the preview, answers and notes), p4l5 (Q2c and Q7 removed from previews and answer slides, teachclue note), p4l6 (Q5c removed from the answer slide, teachrect note), p4l8 (slide Stretch item 3). p4l4, p4l7, p4l9 and p4l10 regenerate unchanged (their slide Stretch and Challenge items were already compliant). Slide counts: 26, 26, 27, 28, 27, 26, 27, 26, 25, 27 as before. Slide checker (no font under 24 px, at most 200 elements, notes under 4000 characters) found nothing new; `rebuild/preview.py` on p4l1, p4l5, p4l6, p4l8 reported no OVERFLOW.

## Final page counts (re-measured)
| File | Pages | Before |
|---|---|---|
| Student workbook (designed PDF) | 47 | 47 (every lesson still 2 core pages + 2 Think Harder pages; no spill) |
| Tutor guide PDF | 66 | 64 |
| Weekly Dose of Thinking Math (parent pack) | 25 | 25 |
| Weekly PDFs (student pages per week) | 13, 8, 8, 8, 9 | same |
| Weekly PDFs (tutor pages per week) | 11, 10, 12, 12, 11 | 10, 10, 11, 12, 11 |
| Question bank (outputs/designed) | 28 | 22 |
| Weekly email pack | 12 | 12 |
| Free taster | 5 | 5 |
| What Learners Get | 1 | 1 |

The question bank grew by six pages because the rewritten Core items (objects, scaffolds) and the make-up Challenge items are longer, so each lesson now takes two pages; that file has no page-count constraint. The tutor guide grew because the lesson keys and Think Harder answers are longer. Built with `bash levels/build_level.sh 4` and `python3 levels/mkextras.py 4` (self-check OK).

## Known limits
- Workbook core pages are still guided practice after teaching; the "borderline" questions listed in docs/audit/gifted_p4.md keep a formal method in the full solution. They are the next thing to look at if the core pages are to be made fully tier-compliant.
- The make-up Challenge answers are models; a tutor has to check children's own puzzles by hand.
- The rubric scores barely move (average 13.9 to 14.5 out of 24) because the session design (fixed clock, tutor-led teach block, Think Harder for finishers) is unchanged.
