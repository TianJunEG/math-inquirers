# Independent audit: Level 5 Extension Workbook (self-study, with answers, ages 10-12 on the cover)

Audited 23 Oct 2026, cold read by a model in a fresh session (no child tested). Report only: nothing in the book, data, builders or tools was edited; nothing pushed. Modelled on `extension/l2/AUDIT.md`, `l3/AUDIT.md` and `l6/AUDIT.md`.

Files read: `extension/l5/README.md`, `PROGRESS.md`, `TOOL_REQUESTS.md`; `extension/data/l5_u01..u10.json`; `outputs/extension/L5/*Print_BW.pdf` (100 pages, 1-bit CCITT, 4958 x 7016 = 600 ppi), `*Print_BW_vector.pdf` (text), `*Soft_Copy_Colour.pdf` (99 pages), `build_report.json`; the holiday program text `p5/content/l1..l10.js`, `p5/SPEC.md`; `extension/config/levels.json`.

Note on the brief: the brief says "age fit 10-11"; the cover, `levels.json` and README say "Ages 10-12". I judged against 10-12 and flag the mismatch (Low 3).

## Method and coverage (honest)
- **Every item solved by hand, all parts.** 10 Learn-it examples, 10 Try items and 234 numbered items (Start here 11 to 14, Think harder 3, Go further 3 or 4, Check yourself 4 per unit), each compared with the printed answer and Why. This is more than the 12 per unit asked. I did not use `verify/l5_uNN_checks.py`. Where hand work needs enumeration I wrote my own throw-away scripts (not the builder's): digit-card maxima and minima (U1 T03, U2 T03), all bracket placements (U1 S07, C03), all four-number expressions with and without concatenation (U1 G03), unit-fraction pairs (U2 G02), cuboid triples (U5 S09), pack combinations (U6 T01), rectangle counts (U10 T02). Every other item by arithmetic or reasoning.
- **Result: 0 wrong answers, 0 unsolvable items, all 10 Try items right, all riddles unique** (U1 S12, T01; U10 T01 re-derived). The printed key is right for every item. The problems are in the Why lines (one unit is misaligned), originality, teaching, a few give-aways, answer boxes, figure clutter and a few second readings.
- **Pages.** Print edition viewed as images, two-up at 80 dpi: pp. 6-79 (all of them) and 96-97. Zooms at 200-220 dpi: pp. 6, 13, 28, 29 (three zooms), 32, 33, 35, 56, 57, 59, 60, 61. Pages 1-5 and 80-95, 98-100 read as text (vector PDF); p. 78 and p. 100 confirmed blank (pixel check). Colour edition: text compared with print page by page (identical apart from page-number side and 3 characters on p. 2); one page (28) viewed.
- Tools run: `dup_check.py --level 5` (OK, 7-word gate clean; the REVIEW list, 52 lines, read); `wording_lint.py --level 5` (0 errors, 14 warnings, all cast-list or "no command word" notes, none a real fault). Then my own frame comparison (below).
- **Not done:** no child trial, no printer proof, no check on a real 600 dpi print. Answer pages 80-95 not viewed as images (read as text, with Why compared against the JSON).

## Verdict
**Ready after fixes, not before.** Maths, keys, page numbers (print 100 / soft 99, contents and answer pages), B&W legibility of the 1-bit file and the Beyond / Welcome labels are in good shape. Two Highs must be fixed first: (1) four wrong Why lines in unit 9 (the Why printed under a question is the Why of a different question), (2) a systematic closeness to the holiday program's own questions, with about 25 items that share the holiday item's story frame, question and key numbers (the book's Welcome page promises "new numbers and stories"). A third High is a give-away that is cheap to fix (U9 Start here 5 repeats the Learn page). Everything else is Medium or Low.

## Findings

### High

**H1. Unit 9: four Why lines belong to other questions (printed on answer pages 96 and 97).** In `l5_u09.json` the `explanation` of Start here 5, 6, 7 and 8 is shifted by one item:

| Item (page) | Printed answer | Printed Why is really the Why of |
|---|---|---|
| S05 plus-sign tiles (p64) | (a) 17 (b) 61 (c) 4, 1 (d) 20 | S04 "Each is 5 more. (a) 27, 32. (b) 7 + 9 x 5 = 52. (c) 93 is not a multiple of 5: no." |
| S06 tickets $9 / $5, 15 tickets, $107 (p64) | (a) 8 (b) 7 | S07 stools "All stools: 51 legs, 10 short. Each chair adds 1 leg: 10 chairs, 7 stools." |
| S07 stools and chairs, 61 legs (p64) | (a) 10 (b) 7 | S08 quiz "All right: 60. ... (60 - 39) / 7 = 3 wrong, so 9 right." |
| S08 quiz 12 questions (p64) | (a) 3 (b) 9 | S09 tables "Each table adds 4 chairs. (a) 4 x 5 + 2 = 22. (b) 4 and 2. (c) 48 / 4 = 12." |

S09 itself has its own correct Why, so the S09 text is printed twice. The true Whys for S05 and S06 do not exist in the book. A child who marks S06 wrong and reads "All stools: 51 legs" will be misled. Fix: rewrite the four `explanation` fields (S05: 4 x 4 + 1 = 17, 4 x 15 + 1 = 61, rule, 80 / 4 = 20; S06: all children $75, $32 short, each adult adds $4, so 8 adults; S07 and S08 take the texts now under S06 and S07). I checked every Why in the other nine units against its question and answer: no other mismatch.

**H2. Systematic closeness to the holiday-program (P5) questions.** `dup_check.py` is clean at 7 words, but the README's own REVIEW list ("same sentence form, new numbers") understates what a child who did the holiday program will meet. I extracted every string of `p5/content/l1..l10.js`, compared each Level 5 item sentence by sentence (numbers masked, shingle overlap, then the top 90 read), and then read all holiday workbook, qbank and answer-key items by hand. Almost every Level 5 item has a holiday twin with the same story, same question and same sub-question order. About 70 of 244 items are "same type, new numbers"; **about 25 also share a key number, a name, a rule or the answer** (class B). Class B (print pages in brackets):

| Level 5 item | Holiday source | What is shared |
|---|---|---|
| U9 Think harder 2 staircase (p66) "figure 1 has 1 tile, 2 has 3, 3 has 6, 4 has 10. Figure 10 has [55]" | `l9.js` "step 1 is 1 square, step 2 adds a column of 2 (3 altogether)... staircase with 10 steps" | same item, same figure 10, same answer 55, same hint "figure n adds a column of n" |
| U9 Start here 2 (p63) "sticks = [ ] x hexagons + [ ]. 20 hexagons need [ ]" and Why "(not double 51)" | `l9.js` "Matchstick houses... Each new house adds __ sticks. Why not 6? Rule: sticks = __ x houses + __. For 20 houses" | frame, 20, the "why not double" idea |
| U9 Go further 3 (p67) "30 questions, 4 marks, wrong loses 1, blank 0. Ali leaves 3 blank, scores 73" | `l9.js` "25 questions, 4 marks, 1 taken away, blank 0. Mei left 3 blank and scored 68" | 4 / 1 / 0 / 3 blank, the same question |
| U9 Start here 6 (p64) tickets $9 / $5, 15 tickets, $107 "Make a table to guess and check" | `l9.js` "Guess and check with a table. Adult tickets... $12... child $7. 15 tickets for $145" | frame, 15 tickets, the instruction |
| U9 Check yourself 2 (p68) "dots = 3 x figure number + 2" | `l9.js` "number of dots = 3 x figure number + 2" | same rule |
| U9 Think harder 1 (p66) purse of 20c and 50c coins; U10 Go further 2 (p74) 10c / 20c / 50c with "as many 10c as 50c" | `l9.js` "Siti has 30 coins... 20c and 50c"; `l10.js` "25 coins of 50c, 10c and 20c... twice as many 10c as 50c" | same coin kinds, same relation, same supposition method |
| U10 Start here 3 (p70) three owners, three animals, "owns neither the parrot nor the goldfish. X does not own the goldfish" | `l10.js` "Ravi, Siti and Ben... a rabbit, a hamster and a bird. Ravi has no bird and no hamster. Siti has no hamster. Who has the bird?" | clue pattern 2-1-ask the third, identical |
| U10 Start here 4 (p70) "Two numbers add up to 52. The larger is 14 more than the smaller" | `l10.js` "Two numbers add up to 40 and the bigger is 8 more than the smaller" | whole sentence |
| U10 Start here 6 (p71) vase, three children, three statements | `l10.js` Q5 "Ali, Ben and Mei... broke a vase. Ali says... Exactly ONE is lying" | same story, same ask (truth/lie flipped) |
| U10 Start here 7 (p71) "In how many years will Dad be 3 times as old as Ali?" | `l10.js` "In how many years will Mum be exactly 3 times as old as Mei?" | question |
| U10 Start here 12 (p72) "numbers from 1 to 60. How many times does he write the digit 5?" | `l10.js` "digit 4 appears... from 1 to 50" | whole item |
| U10 Go further 1 (p74) "3-digit numbers do the digits sum to 7? Make an ordered list" | `l10.js` "3-digit numbers have digits that add up to 5? List them all in order" | whole item |
| U10 Think harder 2 (p73) "squares and the rectangles in a 2 by 4 grid. A square also counts as a rectangle" | `l10.js` "3 by 4 grid... (a square counts as a rectangle)... count by size" | item and the hint |
| U8 Start here 1 (p56) "lines AB and CD meet at O. Angle AOC = 64. (a) BOC (b) BOD (c) AOD"; Check yourself 1 (p61) the same again | `l8.js` "lines AB and CD cross at O... Angle BOC, BOD, AOD" | same figure, same three angles in the same order |
| U8 Start here 6 (p57) rhombus ABC = 124, diagonal AC, find BAC | `l8.js` "Rhombus ABCD has angle ABC = 100. The diagonal AC is drawn. Find angle BAC" | sentence and question |
| U8 Start here 7 (p57) trapezium AB parallel to DC, A = 75, B = 110, find C and D | `l8.js` "In trapezium ABCD, AB is parallel to DC. DAB 84, ABC 97. Find ADC and BCD" | sentence and question |
| U8 Start here 8 (p57) and Check yourself 4 (p61) "BDC straight, AB = AD, ABD = 55 / **62**, DAC = 30 / 40" | `l8.js` "D is on BC and AB = AD. Angle B = **62** and angle DAC = 38" | frame; C04 also has the same 62 |
| U7 Start here 13 (p51) "Aisha has $200. She spends 40% on shoes. 25% of the rest on a gift" | `l7.js` "Siti had $200. She spent 40% on shoes and 50% of the rest on a bag" | $200, 40%, shoes, "the rest" |
| U7 Start here 9 (p50) "T-shirts $20. Shop P buy 2 get 1 free. Shop Q 30% off each" | `l7.js` "cereal $15 in two shops. Shop X: Buy 3, get 1 free. Shop Y: 30% off... Mei buys 4" | frame and the 30% |
| U7 Go further 1 (p53) "percentage increase from $20 to $50, decrease from $50 to $20. The change is always compared with the amount you start from" | `l7.js` "chicken rice $4 to $5... (a) increase (b) decrease... percentage change = the change out of the amount you START with" | frame, hint |
| U7 Go further 2 (p53) "40 children, 40% boys, 25% of the boys and 50% of the girls wear glasses, what percentage of the group" | `l7.js` "800 pupils, 45% boys, 20% of the boys and 30% of the girls take the bus, what percentage of all" | whole item |
| U7 Think harder 3 (p52) "$218 with GST... How much GST is in $218?" and Think harder 2 "After a 20% discount, a bag costs $60" | `l7.js` "$109, GST included... How much GST is in the price?" (218 = 2 x 109); "After a 20% discount, a shirt costs $40" | item, 20%, double the number |
| U6 Start here 8 (p43) "Printer P 40 pages a minute. Printer Q **20** pages a minute... one job of **900** pages" | `l6.js` "Printer P 30... Printer Q **20**... A job has **900** pages. Both printers start together" | Q = 20 and 900 pages, the question |
| U6 Go further 3 (p46) "Tap A on at the start, tap B **5** minutes later" | `l6.js` "P starts alone. After **5** minutes, Q joins in" | structure and 5 |
| U6 Start here 13 (p44) "Gym plan A $20 a month and $4 a visit. Plan B $8 a visit, no fee" | `l6.js` "Gym A $30 to join and then $4 for each visit. Gym B no joining fee... $7 each visit" | frame and $4 |
| U6 Think harder 3 (p45) "4 printers print 480 sheets in 6 minutes... 6 printers, 5 minutes" | `l6.js` "3 machines make 360 masks in 4 minutes... 5 machines in 6 minutes" | whole item |
| U6 Think harder 2 (p45) "printer P needs 12 minutes, printer Q 20 minutes... both work" | `l6.js` "tap fills a bath in 12 minutes... empties in 20 minutes"; "P 6 min, Q 3 min together" | 12 and 20, the method |
| U6 Check yourself 4 (p47) "$1.50 for the first hour, then $0.60 for each extra 30 minutes (a part counts as a whole one)" | `l6.js` "$1.50 for the first hour and $1 for every half hour or part of a half hour" | $1.50, the rule |
| U5 Start here 12 (p37) "A cube-shaped container with edges of 30 cm is full of water. All the water goes into an empty tank with a 60 x 45 floor. Find the depth" | `l5.js` "A cube-shaped container with 20-cm edges is full of water. All of it is poured into an empty tank with a base 50 by 32. How deep" | the whole item |
| U5 Start here 13 (p37) "A tank is 2/5 full. Then 18 litres more go in and it is 7/10 full. Capacity" | `l5.js` "A tank is 1/3 full... After 12 l more... 3/5 full. How many litres does the tank hold" | the whole item |
| U5 Think harder 1 (p38) "54 small cubes have exactly 1 painted face. How many small cubes make the big cube" | `l5.js` "96 small cubes have exactly one painted face. How many small cubes are there altogether" | the whole item |
| U5 Think harder 2 (p38) tank A 40 x 30, tank B 30 x 20, pour until equal depth | `l5.js` container A 30 x 20, tank B 40 x 30, pour, pour back until equal | same two floors, roles swapped |
| U5 Think harder 3 (p38) block 10 x 20 x 15 stands upright in a 40 x 20 tank, water 9 cm | `l5.js` block 10 x 10 x 15 stood upright, base 30 x 20, water 10 cm | same item (15 cm, 20 cm) |
| U5 Go further 3 (p39) "areas of 3 faces of a cuboid 24, 36, 54" | `l5.js` "Three faces of a cuboid have areas 12, 15, 20" | whole item |
| U5 Start here 6 (p36) "tank floor 50 x 20, level 6 cm, 4 litres poured in" | `l5.js` "base 50 by 20, water 8 cm deep. Ali pours in 3 l" | same floor, same story |
| U5 Start here 1 (p35) "4 cubes along the length, 3 along the width, 2 layers: cubes in 1 layer, layers, cubes" | `l5.js` "box 3 long, 2 wide, 2 high: bottom layer, layers, altogether" | the same three sub-questions |
| U4 Check yourself 2 (p33), Start here 9 (p30) | `l4.js` "area 42, base 12, height" and "square 6 cm, triangle base 9" | frame, base 12 (C02) |
| U3 Think harder 2 (p24) "Siti and Mei have 120 beads altogether. Siti gives 10 to Mei. Then Siti has 3/5 as many as Mei. How many did Siti have at first" | `l3.js` "Siti and Mei had 84 stickers altogether. Siti gave Mei 12. Then Siti had 3/4 as many as Mei" | names, frame, question |
| U3 Think harder 1 (p24) "Siti uses 2/5... 1/3 of what is left" | `l3.js` "Siti spent 2/5 on a dress and 1/3 of the remainder on shoes" | name, 2/5, 1/3 |
| U3 Start here 1 (p21) "Aisha has $80. A book takes 1/4. A pen takes 1/3 of the money then left" | `l3.js` "Siti had $60. 1/4 on a book and 1/3 of the remainder on a T-shirt" | 1/4 then 1/3, the same three-part question |
| U3 Start here 11 (p23) "Ravi has $45. Ben has $21. Their mother gives each boy $15" | `l3.js` "Ravi had $45 and Ben had $15. Their aunt gave each..."; "Their mother gave each of them" | Ravi, Ben, $45, "gives each" |
| U3 Start here 2, 3, 4, 5, 6 (p21-22) | `l3.js` "Ali 18 counters, Mei 6... gives 4... total before and after"; "Ben is 10, his father 38. In 5 years... how many years older"; "Ali had 26 stamps, Ravi 34... same number"; "40 pupils, 3/8 boys, how many more girls"; "jar of beads... which colour did not change" | each is the same item, new numbers (S03 keeps the name Ben, S04 Ali's stamps) |
| U2 Start here 1 (p14), 6 (p15) | `l2.js` "5 pizzas are shared equally among 8 children. Each gets __ of a pizza"; "Ali had 60 marbles. 1/3 to Mei and 1/2 of the remainder to Ben" | whole sentence; the same 1/3 to Mei and a second fraction to Ben |
| U2 Go further 3 (p18) bounce, "after the 3rd bounce 27 cm", (a) the start (b) first under half | `l2.js` "Every hour 1/3 let out. After 3 hours 16 litres. (a) full tank (b) after how many hours less than half" | same two questions, same shape |
| U2 Go further 4 (p18) "1/3 + 1/15 + 1/35 + 1/63" | `l2.js` "1/6 + 1/12 + 1/20 + 1/30 + 1/42 ... Hint 1/6 = 1/2 - 1/3" | same trick, same hint idea |
| U1 Start here 1, 5, 6, 7, 14 (p7-9), Check yourself 3 (p12) | `l1.js` "In 6 482 315, the digit 4 stands for __. How many thousands make 3 250 000"; "Estimate each answer by rounding"; "Put ONE pair of brackets"; "Circle each one that rounds to 2 500 000" | S01 has the same three sub-questions in order; **the table in S05 is the number 6 482 315, the holiday's own example**; S06 and S07 keep the holiday's sentences |

Two things make this a High, not a Low. First, the Welcome page promises "the same ideas as the Holiday Program, with new numbers and stories", but for these items the story is the same. A child who did the holiday program can answer from memory (U9 Think harder 2: the staircase answer 55). Second, the README says "No holiday question is repeated"; that is not true of class B. Earlier audits (`l6/AUDIT.md` H1, `l2`, `l3`) treated this as High. **Recommendation:** replace at least the class B items with new stories and a different second question, keeping the topic; the same-type items (class A) can stay if the owner accepts "same skills, new numbers" as the design, but then the Welcome sentence should say "new numbers" only. After replacement: re-run `l5_uNN_checks.py`, `dup_check.py` and the build. Units 3, 5, 6, 7, 9 and 10 are worst, units 1, 4 and 8 are mostly type-level.

**H3. Unit 9 Start here 5 gives its answers away (p64).** The Learn page (p62) prints "Rule: tiles = 4 x figure number + 1 ... Figure 20 has 81 tiles" for the same plus pattern. S05 then asks (c) "tiles = [4] x figure number + [1]" and (d) "The figure with 81 tiles is figure [20]". Both are copies of the worked example; the stem also states "a middle tile and 4 arms of n tiles each". Replace S05 with a new pattern (for example arms of n + 1 tiles, or a 3-arm shape) and ask for a different far figure.

### Medium

**M1. Learn pages (self-study) teach only part of the unit.** Each has a worked example, how-to and Try, which is good. The items then use methods the page never shows:
- **U9 (p62):** supposition ("suppose all are ..., how many short, each swap adds ...") is used in Start here 6, 7, 8, Think harder 1, Go further 3, Check yourself 3 (seven items) and never taught. It first appears in hints. Add a second worked example. Sums of sequences (T02, T03, G01) are also untaught.
- **U8 (p55):** the "Reasons" box lists only straight line, point, triangle. Parallelogram, rhombus and trapezium facts (opposite angles equal, neighbouring angles add to 180) and isosceles base angles are used in S05-S08, S12(c), T01, T03 and first appear in the answer Whys. Add them to the box.
- **U2 (p13):** only the fraction of a remainder. Unit-fraction sums (S07, T01, G02), unlike denominators (S02, S04), fraction x fraction (S11) and mixed numbers are not shown.
- **U5 (p34):** only stone displacement. Painted cubes (S10, T01, C03), packing whole cubes (S11) and pouring between tanks (T02) are not shown.
- **U6 (p41):** combined rates, leak, and "a part of 30 minutes counts as a whole one" are not shown (the last is in the stem of S09 only).
- **U1 (p6):** rounding, estimating and bracket placement (S03, S06, S07) are not shown; the half-up rule for 4 500 000 in S14 is not stated.

**M2. Answer boxes: every `{b}` is 15.3-15.6 mm x 9.3-9.5 mm; the wide `{bw}` box is never used.** Measured in the vector PDF on pp. 14, 19, 73. Too small for:
- **U10 Think harder 1 (p73) (a)-(d):** the child writes a sport ("swimming", "badminton", 9 letters) in a 15 mm box. Use `{bw}` or a line.
- **Mixed numbers** (U2 S01(c), S05, S10, S11(c), T03(a) "5 1/6"): a stacked fraction needs about 6 mm of height and the whole number a further 5 mm of width; tight for a 10-year-old.
- **U7 Start here 14 "$ [292.50]"** (6 characters) and similar 5 to 6 character answers (U5 S05(a) 14400, U6 T01 $18.50).
Use `{bw}` for these.

**M3. Ambiguity and equivalent forms marked wrong.**
- **U4 Start here 11(a) (p30):** "How many different pairs of base and height are possible? [6]". Key counts 3 and 6, 6 and 3 as different. A child who counts 3 (a 3 by 6 and a 6 by 3 triangle are the same area) is marked wrong. Say "base first, height second".
- **U2 Think harder 3(a) (p17):** "The greatest sum is [5 1/6]". The stem says "The fractions need not be proper" and the box does not ask for a mixed number; 31/6 is equal and natural but not in the key. Add "(mixed number)" or accept both.
- **U2 Start here 7 (p15):** "7/12 - 1/3 = [ ]. So 7/12 = 1/3 + [ ]". The first box has no "simplest form"; 3/12 is a correct first answer and the second box would then be marked by the wrong key.
- **U2 Start here 10 (p15):** "Mark Mei's points A and B on the number line" but A and B are already drawn. Say "Read".
- **U2 Think harder 1 (p17):** "Stop when the first fraction is less than half of 2/5". 1/5 is equal to half, not less; the Why says "1/5 is half of 2/5, so stop". Say "is not greater than half".
- **U1 Go further 3 (p11):** "You may use + - x / and brackets": concatenation (34 + ...) is not forbidden; I checked: it still cannot make 99 or 100, so the key survives. Say "do not join digits" to be safe.
- **U7 Go further 3 (p53) and U3 Go further 2, 3:** finding the whole from a part (P6 idea) is unlabelled; see M7.

**M4. Give-aways in figures and stems (besides H3).**
- **U4 Go further 3 (p32):** the figure already draws the dashed line D to C; the hint (printed upside down) says "Join D to C". The key step is on the page. Same in **U8 Think harder 3 (p59)**: the dashed D to E (triangle ADE) is drawn, then the hint "What kind of triangle is ADE?".
- **U2 Start here 12 (p16) and U3 Start here 7 (p22):** the bar model is pre-cut into equal parts with "book / lunch / left" and "bag / left" printed; the unit lesson is "draw a bar model" and the child only reads it.
- **U2 Think harder 1 (p17):** "Try 1/3 first" hands over the first fraction; the same item type was just taught in Start here 7.
- **Hints that state the whole method** (a first hint should only start): U1 G03 "Try 3 x 4 x 9" (the answer is that minus 7); U2 G01, G02, G03, G04; U3 T01 "Cut the whole into 15 equal units" (the key idea), G03; U4 T02, G01, G02, G03; U5 G01; U6 T02 "Pretend the job has 60 pages"; U7 T02, T03, G03; U8 T01, T03, G03; U9 T01, G02; U10 G02 "Join a 10c coin and a 50c coin as a pair". Same finding as `l6` M7 and the Level 1 and 4 audits. One start-only hint plus the full method in the Why would keep Think harder and Go further hard.
- **U3 Think harder 1 (p24):** the amount spent in all ($90, 9 units of 15) equals the amount left after Monday (9 units). A child who reads "$90" as the rest after Monday gets the same total, $150, by a wrong route. Change the numbers.

**M5. Figures: clutter or an ambiguous mark in the 1-bit print.** All viewed at 200-220 dpi.
- **U4 Start here 1 (p28):** triangle (a) is 19 mm x 12 mm; the label "4 cm" sits on the dashed height and on the right-angle mark, "5 cm" and "5 cm" crowd the slants. In (b) "12 cm" overlaps the dashed line and touches the right-hand slant.
- **U4 Check yourself 1 (p33):** the triangle is 44 mm x 9 mm; the "5 cm" label covers its own dashed height (visible as a 3 mm tick) and the right-angle mark is under 1 mm.
- **U4 Start here 5 (p29):** the "5 cm" label is beside the slanted side, with no visible height line; it reads as the slant length.
- **U8 Start here 6 (p57):** at A the labels "(a)" and "(b)" overlap the small arcs, the dashed diagonal and a stray equal-side tick; a child cannot tell which angle (a) is (the stem names them, but the picture is the point of the item).
- **U8 Start here 1 (p56):** the arcs close into a full circle round O and the "O" and "(b)" touch.
- **U8 Go further 3 (p60):** AB = AC is marked with one tick on the part AD, next to the two ticks of AD = DC. AD then carries "|" and "||" and looks self-contradictory. Put the single tick on DB.
- **U8 Think harder 3 (p59):** the "80 degrees" label sits on the dashed line.
- **U8 Start here 7 (p57):** the trapezium's legs are 75 and 70 degrees to the base, so it looks like a parallelogram; a child who sees "parallelogram" gets C = 75, wrong. A flatter leg on one side would remove the trap that the item does not mean to set.
- **U8 Start here 2 (p56):** the degree sign after the box wraps to the next line.
- **U4 Go further 3 (p32):** the shaded triangle ADE is about 7 mm wide; the hatching is a few stripes. Fine as a shape, tiny as a target.

**M6. Weak or non-explaining Why lines (the ~140 shortened ones).** I read all 244. Most still explain in plain words (the bar-model, loop and supposition ones are good). These no longer explain for a child checking alone:
- **U10 Think harder 1:** "Wei: football. Ben: swimming. Kumar: badminton. Aisha: tennis." No reasoning, no table, and this is the first 4 by 4 logic grid in the book. Needs "Clue 3 leaves Wei only football. Then Ben (not tennis, not badminton) has swimming. Kumar (not swimming, not tennis) has badminton. Aisha has tennis."
- **U10 Start here 5:** "(a) 9. (b) 2 x 2 = 4. (c) 1. (d) 14." Does not say why a 2 by 2 square fits 4 times.
- **U9 Go further 2:** "5 x 4 / 2 = 10": does not say why divide by 2 (the hint does).
- **U10 Think harder 3:** "14 is 2/3 of 21. 21 - 3 = 18. 18 is 3/4 of 24." No why for 21.
- **U8 Start here 2, 3, 4, 9:** only subtractions, although the unit's goal is "give a reason for every step". Add the reason words ("angles on a straight line", "angles of a triangle").
- **U4 Check yourself 3:** "Rectangle 60 + triangle 1/2 x 6 x 4 = 12" does not say where 4 comes from (14 - 10).
- **U3 Think harder 1:** see M4 (the "rest is 9 units ... 9 units = $90" wording confuses spent and left).
- **U1 Start here 12:** says the pairs "1 and 2, or 4 and 8, repeat a digit" and omits the pair 2 and 4 (also repeats the 2 in 472). **U1 Think harder 1** does not show that t = 5 is the only digit that works.
- Whys that the answer lines themselves complete well: U1 S04, S08, U2 S06, T02, U5 G01, U6 S09, U7 S06, U10 S10 and S11.

**M7. Learn pages and the stock "unit method" for a possible P6 preview.** No "ratio" word, no a : b and no speed, circles or negative numbers anywhere (grep of data and both PDFs). So the book is consistent with the owner decision that ratio is a labelled P6 preview in Level 5: there is nothing to label for ratio notation. What remains is the unit-bar idea "Mei has 3/4 as many as Siti ... 3 units and 4 units" in unit 3 (Learn example, Try, S08, S09, T02, T03, G03, G04). It is the same as the holiday program's lesson 3, it is stated as a fraction of a quantity, not as a ratio, and the Beyond label would be wrong for it. I recommend leaving it; if the owner wants the P6 preview made explicit, add one sentence on the unit 3 Learn page. Beyond labels are right on the 14 items they appear on (all in Think harder or Go further, none in Start here). Not labelled but of the same kind: U7 Go further 3 (finding the whole from a percentage), U6 Think harder 2 (combined job rates), U2 Go further 4 (telescoping sum). Label or accept.

**M8. README claims that the book does not meet.** (a) "No holiday question is repeated" (see H2). (b) "No ... algebra letters": the letter n is used as a variable in unit 9: Learn step 1 "In figure n each arm has n tiles", Start here 5 stem "Figure n ... n tiles", Think harder 2 hint "Figure n adds a column of n tiles", Go further 2 hint "n people each shake n - 1 hands". `p5/SPEC.md` rules out letters ("algebra with letters is P6"). Replace with "the number of the figure" or label as beyond. (c) Open point 3: "Objects under 8 mm ... all 5 mm or more": the grids in U4 Start here 7 (4.4 mm cells) and Go further 2 (4.0 mm cells) are smaller; the unit 10 grids are 5.3 mm; the chairs in U9 Start here 9 are 5 mm circles. All legible, but the note is wrong. (d) `TOOL_REQUESTS.md` items 1, 2 and 4 are stale (the Beyond label and Welcome are now fixed; README says so, TOOL_REQUESTS says the opposite).

**M9. Pace plan optimistic for sessions 1 and 3 (p5).** Session 1 is the Learn page plus Start here page 1; unit 5 (pp. 34-35) is a full Learn page and 4 items with 3D figures. Session 3 is Think harder plus Check yourself (pp. 38 and 40 in unit 5: 3 hard items and 4 more). "About 20 to 25 minutes" needs the child trial. No fix without data; say "20 to 30 minutes" or move Check yourself to the weekend.

### Low
1. **Contents (p4)** prints every unit title twice ("Big number puzzles" above "Million puzzles . follows Holiday Program Lesson 1 . answers on page 80"). For a book that says "you do not need to have joined" the line "follows Holiday Program Lesson N" is a dependency and the second title (Million puzzles) is a holiday name the child never met. Print one title.
2. **Welcome (p3) wording.** "Practice for the same ideas as the Holiday Program ... with new numbers and stories" is true of the ideas but not of H2's items; the ruler and "real size" sentences are gone (checked p3 of both editions), "Beyond Level 5 is ahead of school" is right, and the Beyond label is the shared badge ("Beyond Level 5: Counting choices") on all 14.
3. **Age line.** Cover says "Ages 10-12", brief says 10-11: confirm. Start-here items below the age: U3 S02, S03, S11 (22 - 5, +6 years), U5 S01, U4 S02, U9 S01-S04 are P2-P4 level. Fine as a warm-up, but the hexagon pattern in unit 9 is the setting of six items (Try, S01, S02, S03, S11(b), C04).
4. **Tone and shared assets.** Banners "Nearly there. You can do it." and the dolphin on the cover and certificate are the Level 1 style; the trophy plaque on the certificate has pseudo-text (also `l4`, `l6` Low). Licence page still prints "DRAFT licence text" and the temporary email (known, in NOTES).
5. **"private" wording.** p2: "This is a private-enrichment book" and "tuition centres" (the shared licence line). No "SASMO", "MOE", "GEP", "PSLE", "olympiad", "gifted", "price" or "tutor" anywhere in either PDF or the JSON (grep). "Holiday Program (our school-holiday course)" is the only product reference.
6. **Blank pages.** Print p78 (verso of the certificate) and p100 are blank (checked at pixel level); the soft copy keeps p78 blank and drops p100. Page numbers 1-99 are identical in both editions, contents and the ten "answers on page N" (80, 82, ... 98) are right, and every answer's "page N" matches its question page (checked in full for U9 and on pp. 96-97; the other answer pages were read as text only, not item by item).
7. **Check-yourself repeats.** U5 C03 repeats the type of S10, U10 C02 of S02, U10 C04 of S05, U8 Check yourself 1 is the same crossing-lines figure as Start here 1 (and the holiday's). Vary.
8. **Coincidence answers.** U4 S06: (a) and (b) are both 63; a child who copies (a) into (b) is marked right.
9. **Other small second readings.** U1 S14 and S09 rely on "half rounds up" (not stated). U6 S02/S04 "$0.70" vs "$0.7": the key prints two decimals; accept both. U10 S06 "Exactly one ... is telling the truth" is clear.
10. **Soft copy colour:** page 28 viewed, shading is a flat yellow in place of hatch; fine. Text identical to print on every page.

## Compliance and originality (summary)
- **Price:** none. **SASMO / competition / tutor / school-system claims:** none. **Private wording:** only the shared licence line (Low 5).
- **B&W print:** pages are 1-bit CCITT at 600 ppi, 100 pages, `check_bw_failures` 0. Cards, hatch (with white halo behind "gift", "bow", "book", "123"), wave water, dotted grids, number lines, bar models, logic grids and angle arcs are legible at 80 dpi and clean at 200-220 dpi. Nothing depends on colour. Problems are the label collisions in M5, not the render.
- **Fill and overflow:** `build_report.json`: no overflow, lowest fill 0.86 (pp. 21, 22, 43, 45, 63), 0 problems.
- **Ratio:** consistent with the decision (M7).
- **Age fit:** sentences are short (at most 22 words by lint); the reading load is fine; Think harder and Go further difficulty is untested.

## What passed
- All 416 keyed values (10 Try items and 234 numbered items, counted by part) are right, every riddle has one solution, every figure is drawn to scale and matches its text (I checked all triangle, angle, tank and grid figures against the numbers).
- The structure (Learn it with worked example, how-to and Your turn; 11 to 14 Start here; 3 Think harder; 3 or 4 Go further; 4 Check yourself with score, What next and Look back) reads well for a self-study child. Hints are one line, upside down, absent on Check yourself. Answers say the answer first, then Why, then the page.
- Beyond items are all on Think harder or Go further and are labelled; no item uses ratio notation.

## Ranked top 10 (fix in this order)
1. **H1** Unit 9 Whys for S05-S08 (answer pages 96-97): rewrite four `explanation` fields.
2. **H2** Replace the class B items (about 25, table above), starting with the unit 9 staircase (answer 55 is the holiday's), unit 5 (cube-container, 2/5 to 7/10 tank, 54 painted cubes, tank floors 40 x 30 / 30 x 20, upright block), unit 3 (Siti 2/5 and 1/3, Siti and Mei beads, Ravi $45), unit 7 ($200 / 40% shoes, "30% off vs buy 3 get 1", the 20% to $60 and the $218) and unit 6 (900-page job with Q = 20, gym $4, $1.50 parking, 4 printers). Then update the Welcome sentence.
3. **H3** Unit 9 Start here 5: copies the Learn example (rule and 81 to figure 20).
4. **M1** Learn pages: add supposition (U9), parallelogram / rhombus / trapezium and isosceles facts (U8), then U2, U5, U6.
5. **M2** Use the wide `{bw}` box (U10 T01 sports; mixed numbers; $292.50).
6. **M5** Figure clutter: U4 S01(a)(b), C01, S05 label; U8 S06, S01, G03 tick, T03 label; consider the U8 S07 trapezium.
7. **M3** Second readings: U4 S11(a) ordered pairs; U2 T03 mixed vs improper; U2 S07 3/12; U2 S10 "Mark" to "Read"; U2 T01 "less than half".
8. **M4** Give-aways: pre-drawn construction (U4 G03, U8 T03), pre-cut models (U2 S12, U3 S07), "Try 1/3 first", and hints that state the whole method; U3 T01 coincidence.
9. **M6** Why lines that do not explain (U10 T01, S05, T03; U8 S02/S03/S04/S09; U9 G02; U4 C03; U1 S12).
10. **M8 and Low 1 to 3** README claims (algebra letter n, "no repeats", 5 mm), stale TOOL_REQUESTS, Contents titles printed twice, age line. Then the child trial.
