# Round 4 independent audit: Level 4 Extension Workbook

Audited 23 Oct 2026, desk review, fresh session. Branch `claude/great-fermi-1hv4vc` at 6c3ae57. Report only: nothing in the book, data or tools was edited, nothing pushed. Maths and layout were checked from the PDFs in `outputs/extension/L4/` (print 1-bit 600 ppi, vector, colour), not from the data. The data was used only for the diff against 5e74989 (the commit audited in round 3) and the holiday text `p4/content/l1.js` to `l10.js` for the frame comparison. I did not re-run `run_checks.py`, `dup_check.py` or `wording_lint.py`.

## Verdict

**Maths and production: sell-ready. Content policy ("new story AND new frame"): not met. Two of the eleven rewrites are still clones, and four more still overlap the holiday text.**

- Maths: every changed item hand-solved from the printed page, 0 wrong, 0 unsolvable, every key and Why agrees with the page.
- Production: 100 pages in all three files, contents and answer page numbers right, changed pages fit and read clearly at 1 bit.
- **High (policy): U7 T2** is now a near word-for-word copy of a holiday question (see below). It was a clone in round 3 and is a worse clone now.
- **Medium (policy): U3 T3** is the same frame as a holiday question (total, difference, "give some so they are equal"). Round 3's suggested frame for it ("money transfer between two jars with a difference given") was a poor suggestion: that frame already exists in L3. That is my error, not the builder's.
- **Medium: U8 T2** (dice) and **U4 T1** (fraction with a fixed denominator between two fractions) overlap holiday items closely. **U7 T3** and **U9 S5** are Borderline.
- Everything else is OK or Low.

If the owner accepts "same skill, new story and new numbers" the book can ship now and the Welcome sentence stays true. If the rule is "new frame", rewrite U7 T2 and U3 T3 at minimum, and ideally U8 T2 and U4 T1.

## A. Per-item table (11 rewrites plus the Lows)

Hand-solve column: result from the printed page. Frame column: judged against p4/content.

| Item (page) | Hand-solve vs key and Why | Holiday item compared | Frame verdict |
|---|---|---|---|
| U3 T3 two jars $84, red $30 more (p24) | Blue 27, red 57, equal 42, move 15. Agrees with key (27, 15) and Why. | L3 q-bank: "Ali has $56 more than Ben. Together they have $300. (a) How much does Ben have? (b) Ali gives Ben some so they have the same amount." Same two questions in the same order, same method (take away the gap, halve), same idea (the gift is half the gap). | **Too close (Medium).** New nouns and numbers only. |
| U4 T1 n with 1/2 < n/9 < 5/6 (p31) | n/9 > 4.5 gives n at least 5. n/9 < 7.5 gives n at most 7. Least 5, greatest 7. Agrees. | L4 page 2 Q6: "Find ALL the fractions with denominator 12 bigger than 1/3 but smaller than 3/4" (also the L4 extension "a fraction between 2/3 and 3/4"). Same device: fixed denominator between two fractions, solved by common denominator. Round-3 clone (top plus bottom 28) is gone. | **Too close (Medium, judgement).** A harder variant (needs 18, asks least and greatest) but the same frame and method. |
| U4 T2 fractions of a 24-hour day (p31) | 8 sleep, 6 school, 10 left, half is 5. Agrees. | L4 "Siti read 2/5 Monday, half of what was left Tuesday, 45 pages left" and "Mei takes 1/2, Ali 1/3, 5 left". Those find the whole from the rest. This one goes forward from a known whole. | **OK** |
| U6 G2 Ferris wheel 12 seats (p46) | Bottom is seat 7. Seats 2 to 9 are 7 steps = 210, smaller way 150. 270 / 30 = 9 steps, 1 + 9 = seat 10. Agrees (7, 150, 10). | No wheel in the holiday text. It is a clock face in disguise (30 degrees a space, L6 clock-hands angles; turns as in L6 compass turns), but the questions are new. | **OK** (mild skill overlap, expected) |
| U7 T2 three squares 4, 9, 16 cm2 side by side (p52) | Sides 2, 3, 4. Shape fits a 9 by 4 box, perimeter 26. Agrees. Figure is to scale, steps correct. | **L7 q-bank: "Three squares with sides 2 cm, 3 cm and 4 cm stand side by side in a row on the same line, smallest on the left. Find the area and the perimeter of the figure." Answer there: perimeter 26 by pushing the steps out to a 9 by 4 rectangle.** Same squares, same order, same answer 26, same method. Only the givens are disguised as areas. | **Too close (High).** Worse than the round-3 version. |
| U7 T3 two 8 by 3 rectangles joined two ways (p52) | 8 by 6 gives 28. 16 by 3 gives 38. Agrees. | L7: "A 6 by 4 rectangle is cut into two 6 by 2 rectangles put end to end to make 12 by 2. How much longer is the new perimeter?" (28 against 20) and "6 by 4 and 3 by 2 joined, find the area". Same idea (join or rearrange rectangles, compare perimeters), different task. The L7 lesson text also has an 8 by 6 rectangle with perimeter 28, by coincidence. | **Borderline.** The builder is right that it overlaps, but it is a different set-up (identical pieces, two ways, both answers asked). Acceptable if the owner allows same-skill. |
| U8 T2 dice top and bottom add to 7 (p59) | (a) 14 - 9 = 5, (b) 21 - 12 = 9, (c) 21 - 7 = 14. Agrees. | L8 q-bank has all three parts: "top 3, bottom?" and "three dice stacked, top 5, hidden faces" (a), (b); "dice on a table, four sides and top add to 19, bottom?" (uses 21); "Ali says the 4 side faces always add to 14. Is he right?" (c). Corner-face item is gone. | **Too close (Medium).** Each part restates a holiday question with new numbers. |
| U9 S4 Ravi's cycling graph with a rest (p64) | At 2 h 40 km. Flat from hour 2 to 3: 1 h. Steepest hour ends at 5: 90 - 60 = 30. Agrees (40, 1, 5, 30). Graph points read correctly (0, 20, 40, 40, 60, 90). | L9 Q1 sugarcane graph: single line, read values, biggest increase "steepest line". The money-box two-line frame is gone. | **Borderline.** Distance graph with a flat rest is new; "steepest part" is the same skill as L9 Q1. |
| U9 S5 rows of seats, rule in words (p64) | 8, 11, 14, 17, 20. Row 10 = 8 + 27 = 35. Sum 70. Agrees. | L9 Q4: "Siti reads more pages each day, always the same number more. Fill in the table", 5-column table, `_ 14 _ _ 26`. Same table shape and same arithmetic-sequence idea. Different: rule given, only one value, asks row 10 and a sum. | **Borderline** (nearer OK than clone). |
| U10 S2 totals from 5c, 10c, 50c (p70) | Totals 5, 10, 15, 50, 55, 60, 65: 7. Above 50: 55, 60, 65 = 3. Agrees. | None found (L10 "Ben, 6 coins of 10c and 50c" is a heads-and-value puzzle, and "ring toss totals" is an extension with unlimited rings). | **OK** |
| U10 S12 lock code 603 (p72) | Last digit d, first 2d, middle 0, sum 3d = 9, d = 3: 603 (unique). Agrees. | L10 "Who am I" digit clues (multiple of 7, digits add to 11, swap is 27 more). Different clue set, no "who am I", no multiples. | **OK** |

Lows from round 3:

| Low | Result |
|---|---|
| U3 T2 tower drawn (p24) | **Done.** Three-level tower, 52 on top, 5, dashed "?", 11 on the bottom, middle row blank. Crisp at 300 dpi 1-bit. Answer 18 matches (23 and 29). |
| U8 T3 "dashed" (p59) | **Done.** Text says "dashed diagonal", figure is dashed. |
| U10 S6 film session (p71) | **Done and correct.** 3:20 - 1:45 = 1:35, minus 15 min = 1:20 pm. No holiday counterpart. Key "1:20" matches the "pm" box. |
| U5 S10 working row (p37) | **Done.** One "Working:" row. |
| U6 G1 working row (p46) | **Done.** One "Working:" row. |
| U6 G2 and G3 rows dropped (p46) | See B. |
| U9 S4 "Each line is worth 10 km" | **Done** (p64, also tick labels every 20, dotted line every 10). |

## B. Page fit, legibility, dropped working rows

Viewed at 80 dpi: pages 24, 31, 37, 46, 52, 53, 59, 64, 65, 70, 71, 72. Figures on 24, 52 and 64 viewed at 300 dpi from the 1-bit image.

- All changed pages fit. No overflow, no clipped text, answer boxes and hint lines intact. Contents of pages 31, 37, 52, 59, 64, 70 to 72 sit well inside the cards.
- 1-bit legibility: tower on p24 (the dashed "?" box has two short broken dashes at the left join but reads clearly), the staircase outline on p52, and the cycling graph on p64 (open circles, dotted grid, flat rest, labels) are all crisp. No grey.
- **U6 p46 (the page the builder asked about).** G1 now has a "Working:" line. **G2 (three parts) and G3 (two parts) have no working row at all**: the cards are tight, the page is full, and there is only a hint line under each. G2 (b) and (c) are two-step (210 then 150; 270 / 30 then count) and a child would have to write in the margin or on the box edges. Round 3 asked that dropped rows leave room to write; here they do not for G2. **Low (Medium for a 9 to 10 year old).** Fix if wanted: drop G4's two answer rows into one line to free one working row, or shorten G2 (a).
- p52: U7 T2 has 3 working lines and a figure, T3 has 2 working lines: fine. p31: T1 has 3 working lines, T2 has 2. p72: S12 has a "Try:" line. p64: S5 has a "Working:" line but S4 has none (not needed).
- U10 S12 Why (p99) reads a little awkwardly: "The last digit and twice the last digit make 3 times last = 9". The logic is right. Low wording.

## C. Page count, contents, answer pages

- Page count: print 100, vector 100, colour 100, A4. Print file is 1-bit gray CCITT 600 ppi.
- Contents (p4) lists unit starts 6, 13, 20, 27, 34, 41, 48, 55, 62, 69 and answers on 80, 82, 84, 86, 88, 90, 92, 94, 96, 98. Verified from the page headers: unit pages begin on exactly those numbers, the Answers divider is p79, the first unit answer heading falls on 80, 82, ..., 98 (checked page by page, p90 and p92 start with "Unit 6" and "Unit 7" headings after a spill, which matches). Progress p76, Certificate p77.
- The "page N" printed with every changed answer matches the question page (U3 24, U4 31, U6 46, U7 52, U8 59, U9 64, U10 70 to 72).

## D. Nothing else changed

Diffed 5e74989 to HEAD. Text of the vector PDF differs on exactly these pages: 24, 31, 37, 46, 52, 59, 64, 70, 71, 72 and answer pages 85, 87, 92 to 95, 97 to 100, which is the 18 changed items plus the shifted answer flow. All other pages are byte-identical in text.

Changed items in `extension/l4/src/` (u01, u02 untouched):

| Unit | Items changed | Reason |
|---|---|---|
| U3 | T02 (figure added, text), T03 | tower drawing, jars rewrite |
| U4 | T01, T02 | rewrites |
| U5 | S09 (figure only: bar row height 38 to 32, gap 14 to 8, to make room; text and answer unchanged), S10 (working row) | **unlisted change in S09**, harmless |
| U6 | G01 (working row), G02 (rewrite, "List:" row dropped), G03 (working row dropped) | as announced |
| U7 | T02 (with figure), T03 | rewrites |
| U8 | T02 (rewrite), T03 ("dotted" to "dashed") | as announced |
| U9 | S04 (graph rebuilt), S05 | rewrites |
| U10 | S02, S06, S12 | rewrites and film puzzle |

Also changed: `extension/verify/l4_u03` to `l4_u10_checks.py` for the same items, `extension/l4/README.md`, `PROGRESS.md`, the L4 PDFs and `build_report.json`. No ids added, removed or reordered, and no unit-level field changed. The same commit range also touches L5 and L6 sources and PDFs, `extension/l6/*` and a `term/l1` audit file; those are separate work and were not reviewed here.

## E. Done and not done

| Request | Done? |
|---|---|
| Hand-solve all 11 rewrites and the Lows against key and Why | Done, 0 errors. |
| Frame check against p4 content | Done: 4 OK or new (U4 T2, U6 G2, U10 S2, U10 S12), 2 Borderline-new (U9 S4, U9 S5), 1 Borderline-overlap (U7 T3), 4 Too close (U7 T2 High; U3 T3, U8 T2, U4 T1 Medium). The builder's own claim, "only U8 T2 and U7 T3 overlap", is wrong: U7 T2 is a verbatim holiday item, and U3 T3 and U4 T1 follow holiday frames. |
| Page fit and 1-bit legibility | Done, clean. |
| Dropped working rows leave room (U6 p46) | **Not fully:** G2 and G3 have no row (see B). |
| 100 pages, contents, answer page numbers | Done, correct. |
| Nothing else changed | Done, one unlisted figure-size tweak (U5 S09). |

## Before sale, in order

1. Decide the policy. If "new frame" holds: rewrite U7 T2 (for example "same perimeter, which of these shapes has the bigger area", or an L-shape from three squares given by area where the question is area not perimeter), U3 T3 (the common alternatives are three-way shares or "a total and a ratio" rather than "total and difference"), and preferably U8 T2 and U4 T1 (for U4 T1, use equivalent fractions in a story, or a number-line position, not a denominator-between-two-fractions task). Re-solve, rerun the checks and rebuild.
2. Optionally give U6 G2 a working row.
3. Remove the DRAFT licence line on p2 when the owner and lawyer approve the text (still present, a known open item).
4. Child trial for pace and reading load.
