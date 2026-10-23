# What an independent auditor should check (Level 2 Extension Workbook)

Written by the author agent. The author did not audit its own work: every point below is open for a cold reader.

## 1. Answers (the highest risk)
- Every one of the 493 answer values has an independent recomputation in `extension/verify/l2_uNN_checks.py` (enumeration, brute force, simulation: cube nets are folded by rolling a die, jugs by breadth-first search, logic puzzles by trying every assignment, money in whole cents). 0 mismatches at the last run. The author also solved every item by hand while writing it.
- Please solve every item cold from the printed page (not from the key) and compare. Things the checks cannot see: a figure that disagrees with its text; a question that has a second correct answer the check did not think of; an explanation sentence that is wrong while the answer is right (the checks do not read the "Why" lines).
- Items that need a picture to answer, check the picture against the key: U1 S02 (blocks 3 flats, 12 rods, 4 ones = 424), S09 (number line arrows at 340 and 370), S10 (1000 chart pieces); U4 S02, S03 (pattern strips), T02; U5 S08 (boxes); U7 S01 (equal parts), S02, S04 (fraction wall), S09 (number line); U8 S02 (pieces), S05 (cube stacks A, B, C: counts 6, 6, 10), S06 and T03 (triangles), T01 (nets A to D); U9 S01 (clocks 4:35, 8:50, 11:15), S05 and G02 (scales); U10 S01, S02, T02, G01 (picture graphs), S04 (tally), S07 and T01 (logic grids).
- Open items (answer "open"): U1 G04, U3 G03, U4 G04, U5 G03, U6 G03, U7 G03, U8 G03, U9 G03, U10 G03. Each prints an example answer; the check proves the example has exactly one solution. Confirm the example is correct and the task is clear to a 7 to 9 year old.
- Items with a hidden-cube reading (U8 S05): the text states "Stack A is 1 cube deep. Stacks B and C are 2 cubes deep. At the back they are just like at the front." Check this is unambiguous.

## 2. Originality
- `dup_check.py --level 2`: no shared 7-word run with the holiday Level 2 program, the private source texts (when present) or the term lessons. The REVIEW list (same sentence skeleton, other numbers) was read: every line is a question TYPE the holiday lesson also uses (digit cards, hens and goats style legs puzzles, "I think of a number", pizza fractions, money change, jugs and times). Items that are close in structure to a holiday item and deserve a second opinion: U5 G04 (machine put back in twice; holiday uses x2 then -4, here +5 then x2, answer 10), U9 T01 (balance: 4 plums = 1 pear; holiday: 3 apples = 1 pomelo), U9 T02 (5 l and 7 l jugs; holiday uses 3 l and 5 l, 2 l and 7 l, 3 l and 7 l), U10 T03 (saving tables, $2 per day more against $5 a day; holiday $3 against $10), U7 T02 (quarter then half of the rest), U6 T01 (35¢ with 5¢, 10¢, 20¢; holiday 40¢), U4 T02 (stars in places 2 mod 5; holiday 3rd of 5). They differ in numbers and wording, not in idea. If the owner wants a stricter rule ("no same structure"), these are the ones to replace first.
- No contest, SASMO, school-paper or book question was copied; the catalogue and the paper-pattern notes were used for question TYPES only.

## 3. Tier honesty, reading load and wording
- `wording_lint.py` has 0 errors. Warnings (names outside the list, no command word) are label words and "Why" lines.
- Check Think harder really is harder than Start here (a Think harder item should need a second idea), and Go further has real extension (every unit has one or two "beyond" items, only in Think harder or Go further, each labelled).
- Read the explanations as a parent would: 222 entries, average about 140 characters. The answer section is 21 pages (Level 1 has 17); the 27 longest explanations were shortened to bring the book to exactly 100 pages. Check that the shortened explanations still explain.
- "Self-study" claim: hints are upside down; the worked example sits on every Learn it page; each unit has a Try item. Is each Learn it page enough to start Start here 1 without a teacher? Weakest: U7 (fractions are taught in 4 lines), U8 (counting method for stacks is taught only by the worked grid), U9 (balances and jugs are taught by one balance example).

## 4. Layout and print
- Every unit page is 82 to 100 percent full before leftover space is shared out; no overflow; the book has an even page count; Contents and answer page numbers were checked against the PDF text.
- Black and white: no colour dependence by design (hatching for shaded parts, solid dots for counters, circles / squares / triangles differ by shape). `bw_check.py` and `print/check_bw.py` must pass on the 1-bit file. Look at hatched fractions and cubes in the 1-bit file (small right faces of cubes are hatched; the 200 dpi check measures colour and flat grey only).
- Figures: objects are about 8 mm or more except the smallest items (the fraction wall rows, pattern boxes are 12 mm; the nets in U8 T01 are about 8 mm; the clock and scale labels are 10 pt). Check legibility of the dithered area of Mi only on cover, welcome and certificate (shared template).
- Writing space: answer boxes are 16 x 11 mm; two-digit and decimal answers fit; long lists use a ruled line (`{ll}`). Check that fraction answers like 12/12 fit the box.

## 5. Open points for the owner (not author decisions)
- Page count is exactly 100 (the upper end of the plan target); any added item or longer explanation pushes it over (decision D12).
- The beyond label in the shared renderer prints "Beyond Level 1" in every book (TOOL_REQUESTS.md item 1).
- The shared lint forbids the word "price"; the money unit uses "cost" and "tag" instead (TOOL_REQUESTS.md item 5).
- Licence page contact: handled by the shared build text (not edited here).
