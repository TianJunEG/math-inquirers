# Independent audit: Level 3 Extension Workbook (self-study, with answers, ages 8-10)

Cold read on 23 Oct 2026 by a model in a fresh session (no child tested). Report only: no book, data or tool file was edited. Files: `outputs/extension/L3/*Soft_Copy_Colour.pdf`, `*Print_BW.pdf` (102 pages, 1-bit 600 ppi, viewed), `*_vector.pdf` (text), `extension/data/l3_u01..u10.json`, `extension/l3/README.md`, `PROGRESS.md`, `TOOL_REQUESTS.md`. Method modelled on `extension/l2/AUDIT.md` and `extension/l4/AUDIT.md`.

Per the coordinator's note, two known points are NOT audited: the "Beyond Level 3" text workaround and the default Welcome ruler line (true for Level 3: Unit 9 S2 is a real ruler, measured 10.00 mm per cm in the print file). Note the shared tool fix landed at 15:47, after the L3 PDFs (15:34-15:36), so L3 must be rebuilt to pick up the per-level Welcome notes and `{bw}`.

## Method and coverage
- **Every item solved by hand** (all 225 items, 10 Learn "Try" items, about 460 answers), reading the printed question, not the verify scripts. Then a brute-force of my own for the risky ones: cryptarithms AB+AC=BBD (unique 5,1,9,0) and ABC+BC=CAB (unique 2,6,3); digit-sum 8 sets; sevens 1-200 (40); 4-digit clue riddle (3804); digit sums 4 and 5 (10, 15); greatest/smallest sums (1595, 605, 194); remainder riddles (67, 58, 31, 29, 71); coins that cannot be made (1,2,4,7); fraction pieces (unique 0,2,4); 14 cm wire (3 rectangles); area 36 / perimeter 26 (9 by 4); clue number (162, 252, 342); coins (1 and 7); pencils (30/45/60/50); ages; bus times; liar puzzle (Aisha). `run_checks.py --level 3`: 460 answers, 0 mismatches.
- **Result: 0 wrong answers, 0 unsolvable items, 0 wrong "Why" lines** (one unit slip in a Why, Low 3). The maths is sound and the tiers are sensible. The problems are repeats of holiday items, a few unreadable or ambiguous figures, answer-box size, and Learn pages that skip ideas the first Start here items need.
- **Pages.** Print edition: pp. 1-82 viewed as images at 100 dpi two-up, zoomed at 220-600 dpi on pp. 50, 58, 63, 64, 65, 75; answer pages 80-102 checked as text (page references checked by script: every "page N" and every unit start 80, 82, 85, 87, 89, 91, 93, 96, 98, 100 matches the contents and data). Soft copy checked by text. Print PDF: 102 gray 1-bit CCITT images, 600 ppi, correct.
- **Duplicates.** Ran `dup_check.py --level 3` (0 FAIL; the private sources are present, so the external check really ran) and my own sentence-level and 3-gram comparison against every string in `p3/content/*.js`, and against all private paper files (`docs/books/private_*`, `docs/sasmo/private_*`; 19 814 lines). No SASMO, school or paper names appear in the book. No private-source copy found; closest are generic frames (see M9).

## Verdict
**Not ready to sell: ship after fixes.** Maths and keys are good, layout and B&W are clean for 98 percent of pages. Four High items must be fixed first: a dozen items that are the holiday items with new numbers, an unreadable Check yourself graph, answer boxes too narrow for times and money, and Learn pages that miss the idea the first Start here items test. A child trial is still needed for pace and reading load.

## Findings

### High

**H1. Items that are the holiday item with the numbers changed (same story, same structure).** The README says "none a repeat" because `dup_check` reads only 7-word runs; the skeleton REVIEW list hides these. A child who attended will recognise them. Read against `p3/content/*.js`:
| L3 item (page) | Holiday source | Shared |
|---|---|---|
| U9 T1 (p66) buses every 20 min from 06:50, ride 25, school by 08:15, latest bus | l9 "Buses leave the interchange every 25 minutes ... 06:40 ... 35 minutes ... 08:30. Which is the latest bus" | whole item |
| U9 S8 (p64) box of 6 books 2 kg 250 g, empty box 450 g, one book | l9 box with 4 books 1 kg 50 g, empty 250 g | whole item |
| U9 T2 (p66) night bus 22:50 to 02:10, how long | l9 night train 22:40 to 01:15 | structure and question |
| U9 G4 (p67) film 1 h 55 min ends 00:20, when start | l9 film 1 h 50 min ends 9:15 pm | structure |
| U9 C3 (p68) film 6:45 pm to 8:10 pm | l9 swimming 3:45 pm to 5:10 pm | same times pattern |
| U10 T1 (p73) 7 friends shake hands | l10 6 children shake hands once, how many handshakes | whole item |
| U10 S9 (p72) two numbers add to 60, greater 14 more | l10 two numbers add to 50, 12 more | whole item |
| U10 C3 (p75) cards 1, 4 and 7 make 3-digit numbers, how many even | l10 same cards 1, 4, 7, which are even | same cards |
| U7 T3 (p52) 9 by 6 rectangle, 3 by 2 cut from a corner, then from the middle of a long side | l7 10 by 8, 4 by 3, same two cuts, same question | whole item |
| U5 S6(b) (p36) number between 70 and 80 divided by 9, remainder as great as possible | l5 between 60 and 70 divided by 8, "as big as it can be" | whole item |
| U5 S5 (p36), S13 (p37), Try (p34) bags of marbles with leftovers; "how many more to make one more" | l5 Ravi packs marbles in bags of 8, 12 bags 5 left; Mei 53 beads, bracelets of 8, "how many more beads for one more" | story, structure |
| U3 T1, G4, C2, C3 (pp24, 25, 26) Ben writes the 7 times table, how many end in 4; Ben multiplies by 8, last digit; "You know 5x7=35, find 6x7"; "last digit of 7x56" | l3 same four items with 6 and 9 times | structure, "Ben", wording |
| U1 T2 (p10) digits 7 in 1 to 200; U1 T3 (p10) Mei 1 and 2, 10th in list; U1 S9 (p8) pattern 4000 up 500 "is 6800 in it" | l1 digit 5 in 1 to 100; Mei cards 1-4, 10th; pattern 1000 up 7 "is 1100 in it" | structure |
| U4 Try (p27) 480 stamps, 215 fewer; U4 S11 (p30) | l4 512 stamps, 139 fewer; Ben 79 fewer than Ali | story |
| U6 T2 (p45) "I am a fraction equal to 2/5 ... " | l6 "I am a fraction equal to 3/4 ... " | frame, "I am a fraction equal to" |
| U8 T3 (p59) staircase, right angles inside, 4 steps then 8 | l8 staircase 3 steps has 6 right angles, find 4, 5, 10 | whole idea |
| U10 Learn example and Try (p69) 6th from front 3rd from back; U10 S5(b) | l10 "5th from front 4th from back of a queue" | same type, "Mei" |
Fix: new story and structure for at least U9 T1, S8, T2, U10 T1, S9, C3, U7 T3, U5 S6(b), U3 T1/G4/C2/C3 and U8 T3; accept the rest as "same type". Then re-run the unit checks, `dup_check`, build.

**H2. U10 Check yourself Q1 (p75): the graph's axis labels are an unreadable black smudge.** The graph is about 50 by 20 mm; the labels 0, 5, 10 ... 40 overprint each other (confirmed at 300 dpi). The child must read Monday and Tuesday and subtract; gridlines can be counted but the labels cannot be read. Enlarge the graph (at least 40 mm tall) or label every 10. U10 S2 (p70) is fine; the same check applies to any other small graph.

**H3. Answer boxes about 16 mm wide are too narrow for 5-7 character answers.** Boxes measure about 16 by 10 mm. Too narrow: times with "pm" (U9 S10(b) "4:35 pm", S10(c) "6:30 pm", G2(a) "4:28 pm", G2(b) "4:37 pm": 7 characters, about 28 mm needed); 24-hour times (U9 T1 "07:50", G4 "22:25", S9(a)-(c) "06:15", "13:40", "21:05", S11(c) "11:25"); money with decimals (U4 S9 "24.85", U9 S7(a) "14.45"; also "0.95", "4.05", "2.65", "2.90", "4.80", "5.20"). Use the new `{bw}` wide box for these (the data does not use it yet).

**H4. Learn it pages do not teach what the first Start here items need (self-study gap, age 8-9).** Each Learn page has one or two worked examples; these ideas appear cold:
- **U4 (p27):** the Learn page only does "more than". Start here 5 and 10 (times as many, 4 equal boxes), 6 (total and difference), 7 (equalising, half the gap), 8 (compare with the previous day) have no worked example. S5 even gives the finished model.
- **U5 (p34):** goal says "decide what the remainder means"; Start here 3 and 9 (26 people in cars of 5, need 6) have no example of rounding up.
- **U6 (p41):** equivalent fractions by multiplying top and bottom (S10, S7, T3) are not taught (the wall in the example has only halves, quarters, eighths). The slash style "3/4" in all question text is not the stacked style the child sees in the wall (see M2).
- **U1 (p6):** only cards; place value and "1000 more" are not shown. Low risk.
Add one short worked line or a second example on each page (the L2 audit round did this).

### Medium

**M1. Second readings and answer give-aways.**
- **U8 S10 (p58):** the "X" sits inside the L-shape next to the inner corner with no arc. A child with a paper corner sees an exact right angle on the outside of the dent and says "Siti is right". Key is "No, greater than". Draw an arc inside the shape. (S2 gives the rule "A dent is greater than a right angle", which also spoils the idea.)
- **U7 T3(c) (p52):** "the same 3 m by 2 m piece cut from the MIDDLE of a long side": 3 along the side gives 34 m (key); 2 along the side gives 36 m. Say "with the 3 m side along the edge".
- **U3 S10 (p23):** "List ALL the ways" and "There are [ ] ways": 15 rows of 2 and 2 rows of 15 count as 2 ways (6, key) or 1 (3 in all). The table has exactly 6 blank rows, which gives away the answer. Use 8 rows, and say 2 rows of 15 is different from 15 rows of 2.
- **U5 G4(b) (p39):** four boxes for "orders he cannot fill" gives the count. Use a line.
- **U10 T3 (p73):** begins "A graph shows the pencils sold on 4 days" but no graph is shown (the page then says "Draw your bars"). Reword: "Draw a bar graph if you like."
- **U7 S7 (p50):** the labels "b" and "a" sit side by side near the inner corner, away from their edges. Move "a" above the horizontal edge and "b" beside the vertical edge.
- Hints that are the whole method, so the question is already solved: U5 G2 "It is always 2 less than a table number", U9 T3 "Take away the extra $1.50 for each notebook first", U4 T2, U7 T1 ("Each rectangle is 8 cm by 4 cm"), U1 T2 plus its working-line labels "1 to 99 / 100 to 200 / Total", U10 T2 (labels "If Ben did it" ...), U2 T1 ("What is B?"). Hints should start the child, not finish.

**M2. Fractions in text are written 3/4 (README admits it).** Stems, parts and Learn text print "5/8", "3/4 = 1/2 + 1/[ ]", "[ ]/12" in running text, next to figures with stacked fractions. For 8-9-year-olds this is a different notation and a place where "5/16" is easy to misread. Prefer stacked fractions in the Learn page and in the answer boxes, or at least in the Learn page. Equivalent forms: all boxes force the denominator (/6, /8, /12), so correct equivalent answers are not marked wrong; only U6 S2 (two free boxes) could attract 2/3 for 4/6 (unlikely, six parts shown) and U6 T1 (a child listing 1/2 for 6/12). Add "write the fraction with the bottom number shown" in S2 and T1.

**M3. Age fit: Think harder items that are Primary 5-6 methods and unlabelled.** U5 T3 (each gets 3, 11 left; each gets 5, 7 short: excess and shortage), U5 T2 (three remainders), U4 T3 (age gap, "twice as old"), U4 T1, U2 G1 (ABC+BC=CAB), U2 T3 (magic square total), U9 T3 (two bills). Labelled "Beyond" appears only on Go further. They are solvable but heavy for 8-9 in a 20-25 minute session 3 (Think harder plus Check yourself). Add the Beyond label or move to Go further, or lengthen session 3 in the pace plan.

**M4. Draw-the-problem unit does not ask the child to draw.** U4 S1, S2, S5 print a finished bar model; only S6, S7, S10 and the Think harder items have a "Draw your model" box. Make S5 a blank model with the labels to fill.

**M5. List lines too short for the answer.** U1 S7 (six 4-digit numbers on a 95 mm line), U10 S6(a) (six 3-digit numbers), U1 S4. Use a line of at least 130 mm.

**M6. Welcome page and equipment.** (Beyond-note and ruler line excluded as agreed.) The Welcome page does not say "you will need a pencil, rubber and ruler" (U8 T2 says "Use a ruler"; U8 uses a paper corner as a right angle checker; the Learn page says this in week 8). Add to `levels.json` `welcome_equipment` for Level 3: "a pencil, a rubber, a ruler and a piece of paper with a square corner (Unit 8)".

**M7. U8 figures are small.** S1 angles A-F have arms of 15-20 mm, S2 shapes are 20 mm across; a paper corner is bigger than the angle. All are legible in 1-bit, and arcs are drawn (better than L4). Enlarge to 25-30 mm if space allows. U7 T3 figure is 36 mm with 8 pt labels. U2 G2 pyramid is 60 mm wide with about 7 pt numbers ("200", "X", "440").

**M8. Think harder or Go further no harder than Start here:** U9 T2 (same as S10), U3 T3 (list pairs), U8 G1 (degrees; labelled), U6 G4, U7 T1 (a one-step perimeter). Fine for a self-study book; swap one in U3 and U9 if room.

**M9. Close to private-paper frames (not copies).** U2 S12 "The sum of 2 numbers is 9000. One number is 3475. What is the other number?" (same frame as a private P3 item, "sum of both numbers is 100, one is 37"); U1 S11 "I am a 4-digit number... greatest odd digit... 3 less than" (same clue types as a private CA1 riddle); U5 C4 "number between 20 and 30, remainder 2 and 4" (same type as a private item). All are standard types with different numbers; reword S11 (use "less than the hundreds digit") if you want distance.

### Low
1. **Contents (p4)** prints each unit title twice ("Digits, cards and clues" then "Number sleuths (numbers to 10 000) · follows ..."). Print one title; the holiday-lesson text can go.
2. **"DRAFT licence text, for owner and lawyer approval. Not final."** is printed on p2 in both editions (shared by all levels). Remove before sale.
3. **U7 S3(c) Why** says "36 ÷ 4 = 9 cm" but the item is in m. Fix the unit.
4. **Certificate (p77)** Mi's trophy plaque carries garbled pseudo-text (asset). Blank it.
5. **U1 S8(c)** "3, 4, 6, 9, 13" growing differences are not taught before they appear in Start here (the G2 beyond item teaches them later). Move to Think harder or add a hint.
6. **U5 G1(c)** and U3 G4(a): the second answer box or full stop falls on the next line, easy to miss.
7. **U6 S3** the circling letters are in a row above the figure, away from the shapes; fine, but a letter list next to each shape is clearer. U8 Try/C1 "a" falls alone at the right edge of the choice line.
8. Money: Why lines print "2.90", "5.20"; a child writing "2.9" should be accepted: say so in the answers page note.
9. **Ages "8-10"** on the cover while the grade is Primary 3 (8-9): fine, but confirm the brief ("ages 8-9").
10. U9 S5 jug scale ticks are 1.8 mm apart; legible in 1-bit (checked) but at the limit. U9 S11 clocks distinguished only by thickness and length: fine.
11. U6 S9 arrows hide the tick underneath; counting from 0 still works.
12. Pace plan p5 sub-headings are 8.7 pt (the only text under 9 pt).

## What is good (so nobody breaks it)
Contents, pace plan and every "answers on page N" are correct (verified by script); each Learn it has a worked example, how-to box and a Try with its answer at the back; every item has an answer and a Why; answer type is large; hints are one line and upside down; Check yourself has score, What next and Look back; 1-bit print is clean (hatching, dashes, no grey; clocks, jugs, dot grids, ruler all legible); the real-size ruler is exactly 10.00 mm per cm; the open "make up your own" items carry a unique-solution example; page fill and overflow are fine; no Level 1 text; no SASMO or school names.

## Ranked top 10
1. **H1** Replace the 15 or so holiday clones (U9 T1, S8, T2, G4, C3; U10 T1, S9, C3; U7 T3; U5 S6b; U3 T1/G4/C2/C3; U8 T3; U1 T2/T3).
2. **H2** U10 Check yourself graph labels unreadable (p75).
3. **H3** Widen answer boxes for times and money ({bw}): 4 seven-character times, about 14 others.
4. **H4** Add worked lines to Learn pages U4, U5, U6 (and U1).
5. **M1** U8 S10 angle X ambiguity (add an arc); U7 T3(c) orientation.
6. **M1** U3 S10 six-row table gives the answer; U5 G4(b) four boxes.
7. **M1** U10 T3 "A graph shows" with no graph.
8. **M2** Stacked fractions in Learn page and boxes instead of 3/4 text.
9. **M3** Label or move the Primary 5-6 Think harder items (U5 T2/T3, U4 T3); check session 3 length with a child.
10. **M1/M5** Hints that give the method, and writing lines too short (U1 S7, U10 S6a); then Low 1-4 (contents titles, DRAFT line, U7 S3 Why unit, plaque).

After the fixes: rebuild (to pick up the per-level Welcome and `{bw}`), re-run `verify_all.sh 3`, and run a child trial.
