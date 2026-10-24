# Independent audit: Level 2 Extension Workbook (self-study, with answers, ages 7-9)

Audited 23 Oct 2026, desk review by a model in a fresh session (no child tested). Report only: nothing in the book, data, tools or the author's notes was edited. Branch `claude/great-fermi-1hv4vc`, nothing pushed. Files read: `extension/l2/AUDIT_NOTES.md`, `README.md`, `TOOL_REQUESTS.md`, `PROGRESS.md`; `outputs/extension/L2/*Soft_Copy_Colour.pdf`, `*Print_BW.pdf` (100 pages each; 1-bit CCITT 600 ppi, correct print format), `*Print_BW_vector.pdf` (text only); `extension/data/l2_u01..u10.json`. Method modelled on `extension/l4/AUDIT.md`.

## Method and coverage (honest)
- **Items.** I solved all 212 items plus the 10 "Your turn" items by hand (not a sample of 8 per unit), from the printed wording and the rendered figures, and compared each with the printed answer. I did not use the author's `l2_uNN_checks.py` as a source. Afterwards I ran my own short brute force on about 25 risky items: digit-card counts (U1 T01 = 12 and 6; mirror numbers = 90; 255), digit 7 counts (20, 40), odd numbers with tens digit 0 and digit sum 11, bicycles and tricycles (3 ways), 33 in U3 T03, arrays of 24 (6 ordered pairs), frogs (4, 16, 28, 40), pay-$7 ways (6, pieces 2 to 7), pay-35¢ ways (6), 95¢ in 4 coins (unique), reachable amounts with 5, 10, 20, 20 (11), shares of 9 (3 ways), rectangles in 2 by 3 (18), saving table (day 4 level, day 5 +$5). All agreed. I then ran `verify/run_checks.py --level 2` (493 answers, 0 mismatches), `wording_lint.py` (0 errors), `dup_check.py` (OK, also at 5-word runs), `bw_check.py` (chroma 0.0, max flat grey 0.0002) and `fill_check.py` (OK).
- **Result: 0 wrong answers, 0 unsolvable items.** Several items have a second defensible reading or a wrong or shifted "Why" (Section M2, M3). No answer is wrong; the problems are wording, labelling, repeats and the self-study promise.
- **Pages.** Print edition pp. 1, 3, 6-75 (all unit pages, two-up at 80 dpi) and 76-77 viewed as images; zooms at 200-250 dpi of pp. 22, 37, 57, 59, 63, 65, 73. Answer pages 80-100 read as text (they come from the same data; the unit start pages 80, 82 ... 98 match the Contents, and every answer's "page" matches where I saw the item). Colour edition read as text and compared line by line with the print vector file: the only differences are the licence line, the footer layout and the two Welcome sentences in H1. Colour figure pages were not viewed.
- Not testable here: what a 7-year-old actually does with the Learn it pages, pace, and handwriting size in the boxes.

## Verdict
**Ready to sell after fixes.** The maths is clean (0 wrong keys in 222 items, 493 values), the layout is tidy and legible in 1 bit, every page number matches, there is no price, no SASMO/MOE text and no colour dependence. Three High items must be fixed first: leftover Level 1 text (the Welcome rulers sentence and the "Beyond Level 1" labels), repeats of holiday items (one is word for word), and the Unit 9 (and Unit 8) Learn it pages that do not teach what Start here uses. All are small edits except the new items for the repeats, which need the answer checks and a rebuild. A child trial is still needed for reading load and pace.

## Findings

### High

**H1. Leftover Level 1 text (both editions).**
- **Print p3 "For the grown-up", last bullet: "The rulers in Unit 9 are printed at real size."** Level 2 Unit 9 has no ruler and no figure that must be at real size (the soft copy p3 says "Print at 100 percent so the rulers are true size", also stale). This is a Level 1 Unit 9 (Length) leftover. Delete it. Nothing on p3 or the pace plan needs equipment (pencil only), so no replacement is needed.
- **"Beyond Level 1: ..." on 11 items** (pp. 11, 18, 25, 32, 39, 46, 53, 59, 60, 67, 74). In a Level 2 book this says the item is beyond Level 1, which is not what is meant (6 times table, thousands, equal fractions, cube nets and the rest are beyond Level 2). The author knows (TOOL_REQUESTS item 1) and left it because "it is true in meaning"; it is not: a reader sees "Level 1" in a Level 2 book, and a parent may think the book is mislabelled. Fix: the shared `render.py` (use `unit["level"]`), a one-word change that also corrects Levels 3 to 6.
- The same 8 items also open their stem with "Beyond:" (U3 G01, U5 G01, U6 G01, U7 G01, U8 T01, U8 G01, U9 G01, U10 G01), so the word appears twice ("Beyond Level 1: Cube nets" in the label, "Beyond: a net folds ..." in the text). Remove the stem word.
- Nothing on the Welcome page explains the label; add one line ("Beyond means ahead of the school year; skipping it is fine").

**H2. Repeats of holiday items (same frame, numbers or wording nearly the same).** I compared every item stem with the 1,255 text strings of `p2/content/l1..l10.js` by word overlap and read the top 30. `dup_check.py` finds no shared 7-word run, but its REVIEW list shows only skeletons. The ones a child who attended will recognise:
| Item (page) | Holiday source | What is shared |
|---|---|---|
| U4 S01 (p28) "Count in 4s. Fill in the next numbers. 4, 8, 12, [ ], [ ], [ ]" | l4.js "Count in 4s. Fill in the next three numbers: 4, 8, 12, __, __, __" | **identical item, same answer** |
| U4 T03 (p31) triangle chain 3, 5, 7 sticks; "Ben has 40 sticks, the most triangles ..., sticks left over" | l4.js houses of sticks 5, 9, 13; "Ben has 40 sticks. The most houses ..., how many sticks are left" | story shape, name, 40, both questions |
| U5 G04 (p39) "A machine does + 5, then x 2. Ravi puts a number in. Then he puts the OUT straight back in. The final OUT is 70" | l5.js "x 2 then - 4, Ravi puts a number in, then puts the OUT straight back in again. The final OUT is 12" | name, wording, structure (listed in AUDIT_NOTES; I agree it is too close) |
| U5 C03 (p40) "A machine does x 5, then - 3. The OUT is 32. What went IN?" | l5.js "A machine does x 4, then + 13. The OUT is 45. What went IN?" | frame word for word |
| U2 G04 (p18) "The same number goes in both boxes. [ ] + 175 = 625 - [ ]" | l2.js "[ ] + 150 = 550 - [ ]" | same type, same sentence |
| U8 G01 (p60) pyramid of cubes, layers 1 by 1, 2 by 2, ... | l8.js same story with 4 layers | story and question |
| U8 T02 (p59) "Count the rectangles in a row of 4 squares. A square is a rectangle too." | l8.js "rectangles in a row of 3 squares ... (A square is a rectangle too.)" | wording and idea |
| U4 T01 (p31) "starts at 3. It goes up 2, then up 4 ... Will it say 41 / 40?" | l4.js "starts at 2, up 5, then up 1 ... Will it ever say 50 / 51?" | frame |
| U7 T02 (p52) quarter, then half of what is left | l7.js half, then half of what is left | (in AUDIT_NOTES) |
| U5 S06 (p36) "multiplies by one number and then adds another. IN 3 gives OUT 11 ..." | l5.js "multiplies by a number, then adds a number. IN 1 gives OUT 9 ..." | frame |
Also U9 T01, U9 T02, U10 T03, U6 T01, U4 T02 listed in AUDIT_NOTES section 2 are, as the author says, same idea with new numbers. Fix: replace at least U4 S01 (change numbers and the first item type, e.g. count in 3s from 6, or start mid-list), U4 T03, U5 G04, U5 C03, U2 G04 with a new story or structure; the rest can stay as "same type". Then rerun the `l2_uNN_checks.py`, `dup_check.py` and the build.
- Private sources: no 7-word run (OK) and at 5 words only stock phrases ("my digits add up to", "how many different ways are", "i am a number between", "has 2 legs and a"). No SASMO, MOE, GEP or school-paper wording and no "price" anywhere in either PDF (grep of the colour text and the vector file).

**H3. Self-study promise not met on some Learn it pages (Unit 9 worst, then Unit 8).** Each Learn it has one worked example, a how-to box, a facts box and a Try, and the example is good. But the first Start here items need topics the page never shows.
- **Unit 9 (p62).** The page is only a balance example. Start here 1 (read three analogue clocks to 5 minutes, p63), 2 (am and pm), 3 and 4 (elapsed time), 6 (the 5 l and 8 l jugs), 9 and 10 (kg and g, m and cm) are taught by one line each or not at all ("Count on in 5s to the next hour first"; "1 kg = 1000 g. 1 m = 100 cm"). Nothing shows what the hour hand and minute hand mean, or how to pour. Start here 6 has instructions for each pour, so a child can follow it, but it is 73 words, the longest Start here item in the book. A child who has not met clocks at school cannot do p63 alone. Fix: a second small figure on p62 (one clock read with the "count in 5s" and one timeline for "9:35 to 11:05") or move the balance to Think harder and let Learn it teach time.
- **Unit 8 (p55).** The example counts squares in a 2 by 2 grid. Stacks of cubes (S05, S09, C03) are taught by one line ("count layer by layer"), with no isometric picture on the page; half and quarter circles are described in words only; cone and sphere are not in the Solids box (Cube and Cylinder only), yet S01(c), (d), S07 and C01 need them. Fix: add a stack figure with the layer count to the example and "Cone: 1 flat circle and 1 curved face. Sphere: no flat face" to the Solids box.
- **Unit 7 (p48).** Better than the author feared: the worked example, "How to name a fraction" and "Remember" cover naming, like fractions, complements and "more parts is smaller". Not taught but used: reading a fraction wall (S04) and a number line cut in 8 (S09), and "1/5 each when 5 children share" (S08). One small number line in the example would fix S09. The plain-text "3/8" is acceptable at this age (TOOL_REQUESTS item 4 still stands: stacked fractions would read better).
- Smaller gaps: U6 S04 ("find every way") and U10 S07 (logic grid) are scaffolded only by the stem text and one tips line; U3 S09 and G04 (arrays of equal rows) rely on the previous array question.

### Medium

**M1. Two Start here and Think harder items have a second defensible answer or unclear wording.**
- **U3 T02(d) (p24).** "A pen has 6 animals, hens and pigs ... Could she count 12 legs?" The key is Yes (6 hens, no pig). A child who reads "hens and pigs" as "some of each" answers No and is marked wrong. U3 T01 says "at least 1 of each" and this item should say "all hens is allowed" or drop (d).
- **U3 G04 (p25).** "How many different arrays can he make?" Key 6 counts 2 by 12 and 12 by 2 as different. A child who treats them as the same gets 3. Say "A 2 by 12 array and a 12 by 2 array are different."
- **U4 S03(b) (p28).** "The 6th letter E is in place [ ]." Read quickly this is "the 6th letter, which is E" (it is C). It means the sixth E (place 28). Write "The 6th E is in place".
- **U10 S08 (p72) and U10 C04, U7 C04.** Key "3/6", "7/12", "4/12". A child who writes 1/2 or 1/3 is correct but marked wrong (equal fractions are beyond the book). Add "Write it in sixths / twelfths" or note "other correct forms are accepted".
- **U3 S01 (p21).** The key is "3 x 7 = 21 and 7 x 3 = 21" in that order; a child who reads columns first writes 7 x 3 first and looks wrong. Accept either order in the key text.
- **U9 S06(b) (p64).** "Pour the 3 l in" does not say from where (from the 8 l jug into the 5 l jug). Add "from the 8 l jug".
- **U6 S10 (p44), U4 S08, U5 S05 (p36).** Several answer orders matter for a self-marker (U10 S05(b) greatest then smallest is clear; U5 S05 prints "11, 23, 8, 10" but the table cells in reading order are 8, 10, 11, 23; U6 S10 key 50, 20, 20, 5 vs a child's 20, 20, 5, 50). Add "(any order)" or print the answer beside the cell.

**M2. A "Why" line is wrong or shifted.** U2 G02 (p18) Why reads "(a) 495. (b) 693. (c) Both have 9 in the middle. (d) The answer is always a multiple of 99 ...". The item has parts (a) two boxes (495 and 693), (b) middle digit, (c) 954 - 459; there is no (d). The letters are shifted by one, so a child checking (b) is told 693. The answers are right. It looks like a casualty of the 27 shortenings: rewrite with the right letters.

**M3. Other Why lines.** The 27 shortened lines still explain in the great majority of cases (average 137 characters, longest 222; each gives the working and a check). Weak ones that only restate the sum and give no reason: U2 S09 ("(a) 368 + 457 = 825 ..."), U3 S06, U2 S11, U10 S10, U3 G01(d). Acceptable for plain calculation items, but U2 S09 and U3 S06 could say "add the hundreds, tens, ones" / "groups of". U2 S01 shows the column sums but not which digit is the missing one; add "so the missing digit is 9" at each column. Page count is tight (exactly 100), so changes must be net zero.

**M4. Hints and wording that give an answer away.**
- U2 T01 (p17) hint "Try the 3 smallest corners." is the whole answer to (a). Replace with "Which numbers are used in 2 sides?" (the first sentence already says it; drop the second).
- U8 T01 (p59) hint "A line of 5 squares cannot fold into a cube." answers (c) directly and is the only clue the item needs. Use "Which net has a row of 5?" style, or remove the hint from (c).
- U6 S04(b) "[ ] $2 notes and [ ] $1 coin" and U10 S06(b) "[ ] coin of 10¢ and [ ] coins of 20¢": the singular "coin" gives the 1. Use "coin(s)" or "$1 coins".
- U4 G02 hint "They land together every 12. Why 12?" and U10 G02 hint "5¢, 10¢, 15¢ ..." give the method of (b) and (a). Fine as hints but they leave little to find.
- Figures do not give answers away (wall, number lines, clocks and bar models show data, not the result).

**M5. Tier honesty.**
- Start here items that are Think harder in difficulty for a 7 to 8 year old: U2 S01 and S02 (three or two sums with two hidden digits and carrying or borrowing; six missing digits per item), U4 S07 (two lists to 40, the common numbers), U6 S04 (every way, a seven-row table), U8 S05 (isometric stacks with hidden cubes; the stem is clear but this is Year 2 spatial work), U9 S06 (73 words). Reasonable if the page remains a path, but two of them (U2 S02, U6 S04) are better in Think harder.
- Think harder items no harder than Start here: U3 T02, U5 T03 (both "try a few and spot the rule"), U6 T03 (one-step bar), U9 T01 (swap and divide), U2 T02 (compare by shifting). Each unit's Think harder contains at least one real second-idea item (U1 T01, U3 T01, U4 T03, U5 T02, U7 T03, U8 T03, U9 T03, U10 T01), so the tier is mostly honest.
- Go further has real extension in every unit and the "beyond" items sit only in Think harder or Go further (confirmed: 11 labelled, none in Start here). Unlabelled but hard: U8 G02 (painted cubes, 8/24/24/8), U9 G04 (clock gains 3 minutes), U2 G01 (three pair totals). They are fine as challenge items; U8 G02 is Primary 5 level and could carry the "Beyond" label.

**M6. 9 to 11 Start here items per unit: acceptable.** The plan says 13 to 14, Level 1 had 9 to 14, Level 3 10 to 14, Level 4 8 to 13. Level 2 has the fewest but its items are multi-part: the book has 493 answer values (about 49 per unit, more than Level 4's 422). A unit gets 3 pages of Start here with 3 to 4 items each, which fits two 20-minute sessions. The downside is repetition: most skills appear once or twice (U7 has one item each for naming, comparing, adding like fractions and a number line), so a child who gets a part wrong has no second chance before Think harder. I would accept it, because the pages are full (82 to 100 percent) and adding items pushes the count over 100; I would trade items instead: move U2 S02 and U6 S04 to Think harder and add a short easy item in their place.

**M7. Answer boxes are about 16 mm wide, tight for 5-character answers.** Money and fraction answers such as 10.80, 27.40, 10.00, 12/12, 9/12, 4/12, 7/10 and the 4-digit 1250, 2300, 3000 fill most of the box for a 7 to 8 year old's handwriting. The 16 x 11 mm size follows the plan; widen the boxes for answers of 5 or more characters (the U6 and U7 pages have space), as the L4 audit asked.

**M8. Figure and drawing issues.**
- U3 S04 (p22): the animals are crude: each dog's tail runs into the next animal's head, the duck's bill overlaps the neighbour, and the word "dog" or "duck" touches the bottom of the legs, so legs look longer. Legs are still countable (4 and 2) but this is the weakest drawing in the book.
- U5 S08 (p37) and U9 S08 (p65): the number on the hatched part ("3", "27") is readable but heavy in 1 bit; a white label box behind the digit would help.
- U9 S01 (p63): clock B's minute-hand tip runs through the numeral 10 (still readable).
- U10 T01 (p73): the 4 by 4 logic grid is small (62 mm, header text about 10 pt); readable and the only place on the page that needs care.
- Fine in 1 bit: hatched fractions and cubes (the 200 dpi check and my 250 dpi look agree), number lines, the stack figures, net figures (about 8 mm squares), tally marks, picture graphs with half-circle (G01: the half symbol is visible).

**M9. Pace plan wording.** "20 to 25 minutes" for session 1 (a Learn it page of about 150 words, a worked example and a Try, plus 3 to 4 Start here items) and session 3 (3 Think harder items with working lines plus 4 Check yourself items) is optimistic for 7 to 8 year olds, as in the L4 audit. Session 3 could be 25 to 30 minutes, or Check yourself moves to the weekend. Needs the child trial.

### Low
1. **Contents (p4)** prints each unit title twice ("Digit detectives" then "Digit detectives (numbers to 1000) · follows ..."). Print it once.
2. **Welcome p3** step 3 says "Stuck? Find the hint" but Start here and Check yourself have no hints (they are on Think harder and Go further only). Say "On Think harder and Go further, find the hint."
3. **Cover and About say "Ages 7-9"**; the brief for this level is 7 to 8. The content is Year 2 to early Year 3; decide whether 9 is intended (the Go further items would suit it).
4. **Certificate (p77)**: Mi's trophy plaque carries pseudo-text (same as L4 Low 9); replace the plaque with a blank.
5. **"DRAFT licence text, for owner and lawyer approval. Not final."** is printed on p2 of both editions; remove before sale.
6. **Output folder** contains `*_Print_BW_vector.pdf` next to the two sellable files; it is a build source, and the file name does not say so. Move or rename it before packaging.
7. **U3 S07(a)** "What is the most number of boxes" reads oddly; use "the greatest number".
8. **U4 S06** (sticks and squares figure): the three small figures are labelled "1 square" etc. at 8 pt-ish; fine.
9. **U9 S04** the stem contains "Hint: draw a timeline." in a Start here item that has no hint line; the "Draw a timeline" box already does this.
10. **U1 S06(a)**: "(a) The greatest number is [ ] and the smallest is [ ]" depends on S05; a child with a wrong list is marked wrong twice. Fine for a self-study book, but say "from your list".
11. **Hatched or dashed shapes:** the half-picture in U10 G01 is drawn as a half-filled circle with a dotted outline; a child may count the dotted part. A label "half" in the key would help.
12. **U2 S06 Why** claims Ben "forgot that the tens had lent 1 ten". Correct for his 346 (a plausible slip), but stated as fact; say "Ben may have forgotten".
13. **Colour edition** was not viewed page by page; text identical to print apart from the H1 sentence and the licence line.

## Originality and compliance (summary)
- `dup_check.py --level 2` with the private sources present (48 external files, 519,102 7-grams): no shared 7-word run with the holiday bank or external texts; the REVIEW list (37 entries) is stock frames ("cards # # and # once each", "# hundreds # tens and # ones", "a number between # and #", "i take away # i get #", "equal slices") and was read. My own similarity scan found the real repeats in H2; AUDIT_NOTES section 2 listed 7 of the 10, and U4 S01 (identical) and U4 T03 and U5 C03 were not listed.
- No price, no SASMO, MOE, GEP, olympiad or test-result claim; "private-enrichment book, not an official school or examination book" is the only disclaimer. No tutor or class dependence ("You do not need to have joined it"). Cast: Ali, Mei, Siti, Ben, Kumar, Aisha, Ravi, Lily, plus Mr Lim.

## Checks that passed
100 pages in both files, even count, cover to answers; Contents (6, 13, 20, 27, 34, 41, 48, 55, 62, 69), answer start pages (80 to 98) and the pace plan numbers all match; every item's answer page matches its printed page (I checked every unit's pages 1-3 of Start here against the pictures); every item has an answer and a "Why" (type 9.8 pt or larger on every page; the only text under 9.8 pt is the 9 pt running footer); every Learn it has a worked example, how-to box, facts box and a Try with its answer at the back; Check yourself has the score box, the "What next?" rule and Look back in every unit; hints are one line (68 characters at most), upside down; boxes and ruled lines are present for lists and working; no overflow or clipping seen on any page; no colour-only meaning (hatching, dashes, shapes); the 1-bit file has no grey; 10 open items each print an example whose uniqueness I confirmed (U1 G04, U2 G03, U3 G03, U4 G04, U5 G03, U6 G03, U7 G03, U8 G03, U9 G03, U10 G03 are clear for a 7 to 9 year old; U3 G03 and U8 G03 are almost trivially satisfiable).

## Ranked top 10
1. Delete "rulers in Unit 9" from Welcome (both editions); fix "Beyond Level 1" to the level and drop the duplicate "Beyond:" in the stem (H1).
2. Replace the repeated holiday items: U4 S01 (identical), U4 T03, U5 G04, U5 C03, U2 G04 (H2).
3. Teach clocks, time and jugs on the Unit 9 Learn it; add a stack figure and the cone and sphere lines to Unit 8 (H3).
4. Fix the second readings: U3 T02(d), U3 G04, U4 S03(b), U10 S08 and the equal-fraction forms (M1).
5. Rewrite the U2 G02 Why (letters shifted by one) (M2).
6. Remove answer-giving hints and singular "coin" (M4).
7. Widen answer boxes for 5-character answers (M7).
8. Move U2 S02 and U6 S04 to Think harder and add easy Start here items instead; keep 100 pages (M5, M6).
9. Redraw the U3 S04 animals and give the hatched numbers a white backing (M8).
10. Contents titles twice, hint wording on the Welcome page, certificate plaque, DRAFT line, vector file name (Low).

## What a child trial still has to answer
Whether a 7-year-old can read the clocks (U9 p63) and count the stacks (U8 p57) from the Learn it page alone; whether 20 to 25 minutes is enough for session 1 and session 3; whether the 16 mm boxes are used for money and fraction answers; whether Think harder feels harder than Start here (U2 S01 to S02 take longer than any Think harder item); whether the hatched "3" and "27" are read correctly.
