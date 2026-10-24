# Level 2 (P2, ages 7 to 9) holiday online practice, week 1 (lessons 1 and 2)

Built 24 Oct 2026. Not deployed, nothing sent, no website/dist or Supabase change. Week 1 = lessons 1 and 2 (`website/data/beta_schedule.json`, Level 2 groups: lesson 1 Tue 24 Nov, lesson 2 Fri 27 Nov).

Build and test (shared scripts, nothing in them changed):

    python3 practice/holiday/build_holiday.py p2 1      # -> practice/holiday/p2/01/dist/   (git-ignored)
    python3 practice/holiday/build_holiday.py p2 2
    python3 practice/holiday/test_holiday.py p2 1       # browser test + screenshots into p2/01/proof/
    python3 practice/holiday/test_holiday.py p2 2

Sources of the questions (the printed workbook is hand-written code, not data, so each question was extracted from the workbook source into a structured item
with an independent checker; the build stops unless every printed fragment is found in the source and every checker equals the printed answer):
`p2/content/l1.js` and `l2.js` (`workbook()` = Start here; `qbank.stretch` first four = Think harder 1 to 4; `qbank.challenge` last three = Go further 5 to 7, exactly as
`p2/workbook_html.js` prints them), `p2/gaps.json` (Investigation), `p2/workbook_html.js` (the "Make up your own" line). Figures: the printed ones from
`p2/workbook_body.html` (digit cards, 1000-chart pieces, missing-digit columns, magic square, bar model), magic triangles from `hlib.magic_triangle`,
the ten-blocks picture of Think harder 3 redrawn for a phone (the printed one is too small at 390 px).

## Items

| | Lesson 1 Digit detectives | Lesson 2 Missing digit mysteries |
|---|---|---|
| Items | 39 | 41 |
| Start here | 21 | 22 |
| Investigation | 4 | 5 |
| Think harder | 8 | 10 |
| Go further (and Make up your own) | 6 | 4 |
| Auto-marked (number, fields, set, choice) | 31 | 31 |
| Self-check, typed or spoken explanation (never auto-marked) | 8 | 8 |
| Paper-only self-check (drawing, with a figure of the correct drawing) | 0 | 2 (5(b) fill the second triangle, Think harder 1 draw the triangle) |
| Unavailable online | 0 | 0 |
| Variant families ("Try a similar one", every combination run against an independent oracle) | 6 (1a, 1b, 4b, 5a, 5b, 5d: 1,675 combinations) | 6 (1a, 2a, 3a, 3b, 3c, 6: 1,332 combinations) |

Every item has a hint, worked steps and a skill tag. The printed multi-part questions are split into one card per part; a printed "explain" or "how do you know" line is
a separate self-check card (the example reasoning is shown after submit, never marked).

## Not mirrored exactly, and why

- Printed table "Start with 2 / Start with 4 / Start with 7" (L1 Q2a) and the free list lines are one typed list ("247, 274, ...", any order accepted). The child still needs the three starting cards to find them.
- L1 Q4 and L2 Q1, Q2, Q4, Q5: the printed boxes in the pictures are typed in numbered boxes inside a sentence that names the position ("Top row: 347, [ ], [ ]"), with the printed picture above.
- L2 Q5(a) "fill in all the circles" and Q5(b) "fill in the second triangle": 5(a) is typed (corner, right side, bottom). 5(b) has many right drawings (a triangle can be turned or flipped), so it is a paper self-check with one correct drawing shown; the corner numbers are auto-marked separately.
- L2 Go further 5 (find ALL the ways): the child types the first number of each way (507, 517, ... 597), because the second number is then fixed; the full pairs are in the worked solution.
- L2 Q6: the printed "Draw a model" lines and the "Answer ____ and ____" line become one typed list of two numbers (the printed bar model is shown with the question).
- Printed "take-home" star marks are not shown on screen (they are a printing-order cue only).
- Investigation (L1 "Mirror numbers", L2 "Odd or even?") has an "easy first step" in the printed page; it is kept inside the first Investigation card.
- Strategy card, "Tool of the day", "Looking back" and the name/date line are print-only and are not online items.
- No items use coin or note pictures; every figure is drawn.

## Open questions for the owner

1. L1 1(b) (6 hundreds, 15 tens and 2 ones) is 752. The printed workbook has no answer line for Start here, so the independent checker is the only source; worth a glance when the printed answer key is cross-checked.
2. Free typing of explanations: should a tutor see the typed self-check text in the submission (the shared runner stores it), or only the marks? (Decision SUBMIT-TO-TUTOR says answers go to the tutor; this is just a reminder that explanations are included.)
3. Second Think harder / Go further items in `qbank` that are not printed in the workbook (Think harder 5 to 8, Go further 1 to 6 of the bank) are not online: the brief mirrors the printed pages only. They could be added as optional extras if wanted.

## Week 1 audit fixes (items, 24 Oct 2026; see AUDIT_WEEK1_L1_3.md)
- M2 L2 5(a) circles no longer says "160 is between them" (uses "your answer to 5(a) between"); L2 4(b) and 4(d) hints no longer state the total 150.
- M3 L2 5(a) circles hint (false rule "the corner is the smallest") replaced by a test-it hint; L2 5(b) and Think harder 1 hints no longer say "the biggest numbers go in the corners"; L2 4(a) hint no longer names the diagonal; L1 Investigation 4 and Think harder 4 hints no longer give the counter-example.
- Wording: "Write them in the boxes" is now "Type each one in its box"; L1 2(a) says "Type every number".


# Week 2 (lessons 3 and 4), built 24 Oct 2026

Lesson 3 Legs, wheels and arrays (Tue 1 Dec) and lesson 4 Pattern machines (Fri 4 Dec), `website/data/beta_schedule.json`, Level 2 groups. Not deployed, nothing sent, no website/dist or Supabase change; the shared files (`sheet.js`, `practice/submit/*`, `build_holiday.py`, `hlib.py`, `test_holiday.py`) are untouched. Only `p2/p2lib.py` (this level's own helpers) was extended.

    python3 practice/holiday/build_holiday.py p2 3      # -> practice/holiday/p2/03/dist/   (git-ignored)
    python3 practice/holiday/build_holiday.py p2 4
    python3 practice/holiday/test_holiday.py p2 3       # browser test + screenshots into p2/03/proof/
    python3 practice/holiday/test_holiday.py p2 4

Sources: `p2/content/l3.js`, `l4.js` (`workbook()` = Start here; `qbank.stretch` first four = Think harder 1 to 4; `qbank.challenge` last three = Go further 5 to 7, exactly as `p2/workbook_html.js` prints them), `p2/gaps.json` (Investigation), `p2/workbook_html.js` (the "Make up your own" line). Printed figures come from `p2/workbook_body.html` (array, cups tray, cycles, shape pattern, letter tiles, bead string, flower, square tables, stick houses); the stickers-and-plates, van, hens pen, towers, the two number lines for the frogs and every table are redrawn for a phone (the printed ones are too small or crowded at 390 px). Checkers read the pictures where they can (counters and cups of the array and tray, the shapes and letters of the patterns from the figure's own description).

## Items

| | Lesson 3 | Lesson 4 |
|---|---|---|
| Items | 33 | 44 |
| Start here | 14 | 22 |
| Investigation | 5 | 7 |
| Think harder | 8 | 6 |
| Go further (and Make up your own) | 6 | 9 |
| Auto-marked (number, fields, set, choice) | 26 | 35 |
| Self-check, typed or spoken explanation (never auto-marked) | 7 | 9 |
| Paper-only self-check (drawing) | 0 | 0 |
| Unavailable online | 0 | 0 |
| Variant families ("Try a similar one", every combination run against an independent oracle) | 5 (3a, 4a, 4b, 5a, 5b: 70 combinations) | 7 (2c, 3a, 4b, 4c, 5b, T3, C6a: 97 combinations) |

Every item has a hint, worked steps and a skill tag. Browser test: both lessons RESULT OK (every answer typed correctly, wrong and skipped answers, reload, 70 and 97 variants, 390/360/900 px light and dark, no horizontal scroll, figure text at least 11 px).

## Not mirrored exactly, and why

- Printed multi-part questions are one card per part; a printed "explain / how do you know / what do you notice" line is a separate self-check card (example shown after submit, never marked).
- L3 Q1 "two multiplication / two division sentences": one card each with the six boxes, and the stem says what each sentence starts with (rows first, then counters in a row; share into the rows, then groups the size of a row), so the order is fixed and can be marked.
- L3 Q3 and L4 Q4(a), Q5(a): the printed table is drawn as a figure with the printed cells filled; the child types the next cells of ONE row in order (the legs after 1 to 4 swaps; the petals; the children). The hens/goats rows of the printed table are not asked: the question that follows asks hens and goats in two boxes. 
- L3 Q6 (20 chairs): the printed table (rows 2 to 10, chairs in each row, works?) becomes two cards: the numbers of rows that work (a list), then the chairs in each row for those, fewest rows first (ordered list).
- L3 Think harder 1 (find ALL the ways): the number of tricycles for every way (a list), then the bicycles for the same ways in order; the full pairs are in the worked solution.
- L3 Go further 5 is three cards (Mei right? could he count 37? why legs never 25), the third a self-check that does not state that 25 wheels is possible, so it does not give away the first card.
- L4 Q1 and Think harder: "What shape is in place 20?" is typed in print; online it is a choice of triangle, circle or square (the three shapes are in the picture), and Q2(a) a choice of M, A, T, H, so a spelling slip is not marked wrong. Q2(b) is a number.
- L4 Q6 (two lists): Ali's and Mei's lists are typed from where the printed line stops ("3, 6, 9, ...", "4, 8, 12, ..."), in order; "Both say" is a list; "what do you notice" is a self-check.
- L4 Investigation: "write each pattern up to 30" is three typed lists (after the numbers printed in the question); "pick any number from 1 to 30, which pattern?" is fixed to 26 (so it can be marked); "can a number be in two / in none?" are two Yes/No cards.
- L4 Go further 6 (towers) "Is there a tower with exactly 50 cubes? With exactly 100?" are two Yes/No cards, and the explanation a self-check. L4 Go further 7: the two frog number lines are redrawn as two lines of 0 to 15 and 15 to 30 each.
- Printed "take-home" stars are not shown on screen; the print-only strategy card, "Tool of the day", "Looking back" and the name/date line are not online items.
- No coin or note pictures; every figure is drawn.
- The Investigation and Think harder buttons in the question list all read "Investigation", "Think", "Go" (the runner shows the first word of the label); the full label is in each button's accessible name and at the top of the card. Shared runner behaviour, not changed.

## Week 1 audit points applied from the start

No card gives another card's answer in its question or hint (L3 Go further 5 explain, L3 Think harder 2 "who", L4 Investigation cards state only what the patterns are); hints nudge and give no answer or one-case rule; no example equals an answer; the printed position/pairing is kept (hens then goats, rows then chairs, each and left over, ordered table cells); screen wording ("type", "picture a line", "on paper if you like", no "circle the", no "take-home"); lists of at most 9 numbers with a comma; typed explanations are self-check.

## Open questions for the owner

1. L3 Q3 asks only the Legs row of the printed table (the hens and goats rows are shown for the first column only), then hens and goats in two boxes. Should the child also type the hens and goats for each swap?
2. L4 Investigation "pick any number": fixed to 26 so it can be auto-marked; the open "pick any number" version is lost. Fine, or should it be a self-check where the child picks and tests several numbers?
3. L3 and L4 qbank items not printed in the workbook (Think harder 5 to 9 and Go further 1 to 6 of the bank) are not online, as in week 1.


# Week 3 (lessons 5 and 6), built 24 Oct 2026

Lesson 5 Mystery number machines (Tue 8 Dec) and lesson 6 Market Day (Fri 11 Dec), `website/data/beta_schedule.json` (Level 2 groups: lesson 5 = Tue 8 Dec, lesson 6 = Fri 11 Dec; week 3 = lessons 5 and 6 confirmed). Not deployed, nothing sent, no website/dist or Supabase change. The shared files (`sheet.js`, `practice/submit/*`, `build_holiday.py`, `hlib.py`, `test_holiday.py`) are untouched; only this level's `p2/p2lib.py` was extended (number-machine boxes, bar models, count-up number lines, price tags, money helpers and money checkers).

    python3 practice/holiday/build_holiday.py p2 5      # -> practice/holiday/p2/05/dist/   (git-ignored)
    python3 practice/holiday/build_holiday.py p2 6
    python3 practice/holiday/test_holiday.py p2 5       # browser test + screenshots into p2/05/proof/
    python3 practice/holiday/test_holiday.py p2 6

Sources: `p2/content/l5.js`, `l6.js` (`workbook()` = Start here; `qbank.stretch` first four = Think harder 1 to 4; `qbank.challenge` last three = Go further 5 to 7, exactly as `p2/workbook_html.js` prints them), `p2/gaps.json` (Investigation), `p2/workbook_html.js` (the "Make up your own" line). Every answer has an independent checker that does not use the "undo" rule or "biggest piece first": machines are run forwards and the unknown is found by trying numbers; stories are solved by trying numbers; the fewest pieces of money come from counting up from 0 (dynamic programming) and every way to pay is listed by trying every combination (the build stops if any checker differs from the printed answer, and the Level 2 printed keys agree).

## Items

| | Lesson 5 | Lesson 6 |
|---|---|---|
| Items | 28 | 36 |
| Start here | 12 | 20 |
| Investigation | 6 | 5 |
| Think harder | 6 | 4 |
| Go further (and Make up your own) | 4 | 7 |
| Auto-marked (number, fields, set, choice, money text) | 24 | 29 |
| Self-check, typed explanation or list compared with a shown answer (never auto-marked) | 2 (Inv 3, Inv 5) | 6 (the four "notes and coins" lists of Q1, 4(a) why, G6d notice) |
| Open (make-up-your-own, no objective fact) | 2 (Inv 6 your own trick, Make up your own) | 1 (Make up your own) |
| Paper-only self-check (drawing) | 0 | 0 |
| Unavailable online | 0 | 0 |
| Variant families ("Try a similar one", every combination run against an independent oracle) | 5 (1a, 1b, 1c, 4, T2: 408 combinations) | 3 (3b, T1, C5: 45 combinations) |

Every item has a hint, worked steps and a skill tag. Browser test: both lessons RESULT OK (every answer typed correctly, wrong and skipped answers, reload, variants, 390/360/900 px light and dark, no horizontal scroll, figure text at least 11 px).

## Not mirrored exactly, and why

- Printed multi-part questions are one card per part; a printed "explain / what do you notice" is a separate self-check card (example shown after submit, never marked).
- L5 Q2 (tables): the printed table is drawn with its empty cells; the child types the missing cells in one sentence of boxes (OUT for IN 4 and IN 10, then IN for OUT 17 and OUT 29; 2(b) the four OUT numbers in order).
- L5 Q3: the two "?" bars become two boxes in the order the bars are (after giving 24, then at first); the figure draws the three bars (the printed labels "Gave 24" are now "After giving 24"). L5 Q5(c) "always the same answer?" is a Yes/No card (the printed answer line is free); the "order of the steps matters" reason is in the worked solution only, as the printed key has it.
- L5 Think harder and Go further: printed "Draw bars" / "Draw a bar for each child" are dropped because the bar model is drawn on screen (the same figure as the printed page); the child may still draw on paper. Think harder 1 is three cards (the machine, IN 10, OUT 26) sharing one figure card of the facts instead of repeating the riddle three times.
- L5 Investigation: "Try 5 different starting numbers" is fixed to 3, 10 (the printed easy first step) and 7, 12, 40; "try a big and a small number" is fixed to 1 and 100; "make your own trick" is open (two tested examples shown after submit). The "what do you notice" and "is it ALWAYS true, say why" cards are self-check.
- L6 Q1 (the table): each row (curry puff, notebook, umbrella, bicycle) is two cards: "write the notes and coins you use" (typed, self-check: it can be written in many ways, so it is compared with the answer shown) and "how many pieces" (auto-marked). The printed picture of the item is not shown (a decorative icon) and the printed picture of the coins and notes is a plain-text list (no coin or note pictures; the list also says there is no $20 note).
- L6 Q2 (the table of ways): the printed table (way, $5, $2, $1, pieces) is not typed as 24 boxes; (a) is the number of ways, "2 pieces altogether" is the printed last column as one ordered list (most $5 notes first, then most $2 notes: the order is stated), and (b) two ways with exactly 4 pieces are typed in six boxes (way with more $5 notes first). The printed picture ($5 note, $2 note, $1 coin) is not drawn.
- L6 Q3 and Q4: printed change number lines are redrawn (with the start and end marked; no hops drawn: the child chooses the hops). Q3(b) is two cards: the change, then the notes for it (how many $10, $5, $2 notes). Q4(b) "find ALL the pairs" is one ordered list of prices (smaller price first in each pair, pairs in order of the smaller price), so the number of pairs is not given away.
- L6 Q5 and 3(a) are the only text items: the amount may be typed as 35, 35c, 35 cents, $0.35, 0.35, 100, 1.00, $1.00, 1 dollar ... (all listed in the data). Q6 (find all the ways) is two ordered lists: the number of stickers for each way (most stickers first), then the erasers for the same ways.
- L6 Investigation "table of how many coins each amount needs, 5 to 95 cents" is three ordered lists (5 to 30, 35 to 60, 65 to 95), so the whole table is typed but no card has more than 7 numbers. Think harder 3 (sets of 4 coins) is typed in cents (a $1 coin is 100), biggest coin first and the set with the biggest coin first. Go further 6 is four cards (could Mei be right, could Siti be right, all the amounts typed in cents, what do you notice).
- Printed "take-home" star marks are not shown (a printing-order cue). The strategy card, "Tool of the day", "Looking back" and the name/date line are print-only.

## Week 1 and 2 audit points applied from the start

No card gives another card's answer in its stem, hint or example (the Think harder 1 cards share one figure; the Investigation "why" card does not say the trick always works; 6(a) and 6(b) both state the order rule instead of saying "the same ways as before"; Go further 6 Mei and Siti are separate Yes/No cards that do not name the answer; 4(a) explain does not say the answer); hints nudge and none states the answer or a one-case rule; no example equals an answer; the printed pairing is kept (IN and OUT, rows and columns of the Q2 table, pairs of prices, stickers with erasers); labels are unique and clear (1(a) list, 1(a), Inv 1 ... Inv 6, T1a, T1b, G6a ...); lists have at most 8 numbers with a comma; every typed explanation is self-check; screen wording ("type", no "circle" or "take-home"); worked steps were checked to be true for every case they name (the variant steps too).

## Open questions for the owner

1. The shared matcher does not read a cent sign after a number in a NUMBER box (`35¢` would be marked wrong: `¢` is not a letter in the unit rule). In these two lessons the only answers in cents are typed as text with all the writings listed (3(a), Q5) or as numbers in a list ("in cents", digits are read wherever they are), and the boxes say "Type the number of cents". If more money lessons follow (week 4 onwards), allowing `¢` in the unit rule of `sheet.js` and `mark.js` would help every level.
2. L6 Q1 "the notes and coins I use" is a typed self-check, not auto-marked (many writings, and a child may list them in any order). Should it become a choice among a few written-out sets, so that it counts as auto-marked, or stay self-check?
3. L5 Q5(d) says "the same OUT as Mei", which tells a child that Ali's machine usually needs a different IN than Mei's; it is the printed wording and Q5(c) (always the same?) is a separate card. Reword in the print, or accept?
4. L5 and L6 qbank items not printed in the workbook (Think harder 5 to 9 and Go further 1 to 6 of the bank) are not online, as in weeks 1 and 2.

## Week 3 L1-3 audit follow-up (item level)
M1 answer leaks reworded, M2 explicit short nav labels, remainder-0 variants excluded (P3 L5 3(b)), long stems shortened, doubled "Make up your own"/"Take-home" lead-ins removed. Print-inherent chains kept as printed (P1 L5 Go further 1(a)/(b), 3(c); P1 L6 Q4/Q5, T3/Q6; P3 L6 5(b), T3). P1 L6 Q5/Q6 keep cents only (printed answers are in cents).


# Week 4 (lessons 7 and 8), built 24 Oct 2026

Lesson 7 Fair Shares (Tue 15 Dec) and lesson 8 Shape Builders (Fri 18 Dec), `website/data/beta_schedule.json` (Level 2 groups: lesson 7 = Tue 15 Dec, lesson 8 = Fri 18 Dec; week 4 = lessons 7 and 8 confirmed). Not deployed, nothing sent, no website/dist or Supabase change. The shared files are untouched; this level's new helpers are in `p2/p2lib_w4.py` (fraction bars, circle and grid, the six shapes, strips, robot, net places figure and every independent checker).

    python3 practice/holiday/build_holiday.py p2 7      # -> practice/holiday/p2/07/dist/   (git-ignored)
    python3 practice/holiday/build_holiday.py p2 8
    python3 practice/holiday/test_holiday.py p2 7       # browser test + screenshots into p2/07/proof/
    python3 practice/holiday/test_holiday.py p2 8

Sources: `p2/content/l7.js`, `l8.js` (`workbook()` = Start here; `qbank.stretch` first four = Think harder 1 to 4; `qbank.challenge` last three = Go further 5 to 7, exactly as `p2/workbook_html.js` prints them), `p2/gaps.json` (Investigation), `p2/workbook_html.js` (the "Make up your own" line). Independent checkers: the parts of each of the six shapes are measured by sampling points (a shape is "quarters" only if its 4 parts have the same area); shaded and equal parts are counted from the drawing; fractions use exact fractions and are written over the printed bottom number (9/12 is not reduced); the robot's pieces are counted from the drawing (3 points, rectangle, chord of the arc); squares and rectangles by trying every size and corner; the triangles of the figure from its marked points and drawn lines; cubes one at a time; nets by rolling a cube over them; painted cubes by looking at every small cube; the shapes of squares by growing them one square at a time.

## Items

| | Lesson 7 | Lesson 8 |
|---|---|---|
| Items | 40 | 29 |
| Start here | 21 | 14 |
| Investigation | 5 | 5 |
| Think harder | 8 | 6 |
| Go further (and Make up your own) | 6 | 4 |
| Auto-marked (number, fields, set, choice, text) | 32 | 22 |
| Self-check, typed explanation (never auto-marked) | 7 | 5 |
| Open (make-up-your-own) | 1 | 1 |
| Paper-only self-check (drawing, with a figure of the correct drawing) | 0 | 2 (Inv 2 and Inv 4: the shapes of 3 and of 4 squares) |
| Unavailable online | 0 | 0 |
| Variant families (every combination run against an independent oracle) | 5 (2a, 4a, 4e, 5a, G5: 167 combinations) | 5 (1c, 2a altogether, 3b, T1, G7 4 by 4: 51 combinations) |

Every item has a hint, worked steps and a skill tag. Browser test: both lessons RESULT OK (every answer typed correctly, wrong and skipped answers, reload, variants, 390/360/900 px light and dark, no horizontal scroll, figure text at least 11 px).

## Not mirrored exactly, and why

- Fractions are typed in two boxes (top number, bottom number) so the bottom number is checked (3/10 for 2/5 + 1/5 is wrong); equal fractions are not accepted there (equivalent fractions are a P3 topic).
- L7 Q1 "circle the quarters" is typed letters (A, C, E, F, any order). Q1(a) "choose one shape that is not quarters, explain" is a self-check. Q2 (three pictures) is one card each with four boxes (shaded and not shaded). The bars printed as "colour the bars to help you" are drawn uncoloured; the child may draw on paper.
- L7 Q3(c), Think harder 2, 3, 4: each "is she right / can he be right" is a Yes/No card plus a separate explain card whose stem is neutral ("Explain what you think about her idea"). Think harder 3's "what is the right answer" is its own card; its picture is a plain bar (the printed picture shows 5/8 shaded).
- L7 Q5(c) "who eats more, how much more" is two cards; Q6 is a choice plus an explain card (the printed "colour the bars" is shown as the correct bars after submit).
- L7 Investigation: the physical fraction strips are drawn as one picture; (a) and (b) are boxes "how many pieces of each kind, type 0 if that kind cannot do it" (so no card says which kinds work), (c) Yes/No plus explain.
- L7 Go further 6 (find ALL the ways to share 10 pieces among 3 children with different numbers): three ordered lists of four numbers (smallest, middle and biggest number of each way, ways in a stated order), so the pairing is kept and the number of ways is not told. Go further 7 (unit fractions between 1/7 and 1/4) is the list of bottom numbers.
- L8 Q1 robot: the printed table is four boxes in a sentence; (a) "which most" is a choice; (c) is a number (3) plus a "show how" self-check. Q2 and Q3: the printed table is one card of four boxes, then the "altogether" in its own card. Q2(b) triangles: bottom line and across line, then altogether.
- L8 Q4(a) letters typed. Q4(b) "add ONE square, draw it on the grid": the screen cannot draw on the grid, so the 10 empty squares next to the shape are numbered and the child types the numbers of all the places that work (4 places; the printed key says "under any one of the 4 squares of the row", which agrees). 
- L8 Investigation: counts (2 and 5) are number cards, the drawing of all the shapes is a paper-only self-check with the correct drawing shown after submit, (c) "how do you know" is a self-check. The printed nets, stacks, layers and the grid and triangle of Q2 are the workbook's own figures; Think harder 2 and Go further 6 show a plain grid (the printed page has none: the child draws one).
- Think harder 3 and 4 (nets): "cut out nets E and F and fold" becomes "if you have the cut-out nets, fold them; if not, picture rolling a cube over the net".
- Printed "take-home" star marks are not shown; the strategy card, "Tool of the day", "Looking back" and the name/date line are print-only.
- No coin or note pictures; every figure is drawn.

## Week 1 to 3 audit points applied from the start

No card gives another card's answer in its question or hint (the explain cards are neutral; Think harder 3 uses an unshaded bar; the Investigation boxes allow 0; the Go further 6 cards do not say how many ways); hints nudge and none states the answer or a one-case rule; no example equals an answer; the printed pairing and position are kept (top and bottom number, sizes in table order, bottom line and line across, smallest/middle/biggest of the same way); explicit unique labels of at most 12 characters; typed explanations are self-check, make-up is open; every variant has its own picture or the text is complete.

## Open questions for the owner

1. L8 Q4(b) became "type the numbers of the squares that work" (auto-marked) because the page cannot draw on a grid. Fine, or should it be a paper-only self-check?
2. L8 Q1(c) and L7 Q1(a) (the printed take-home explanations) are self-checks: worked example shown after submit.
3. L7 and L8 qbank items not printed in the workbook (Think harder 5 to 8 and Go further 1 to 6 of the bank) are not online, as in weeks 1 to 3.


# Week 5 (lessons 9 and 10), built 24 Oct 2026

Lesson 9 Measure Masters (Tue 22 Dec) and lesson 10 Puzzle Day (Thu 24 Dec), `website/data/beta_schedule.json` (Level 2 group L2A: lesson 9 = 2026-12-22, lesson 10 = 2026-12-24; week 5 = lessons 9 and 10 confirmed). Not deployed, nothing sent, no website/dist or Supabase change. The shared files (`sheet.js`, `practice/submit/*`, `build_holiday.py`, `hlib.py`, `test_holiday.py`) are untouched; this level's new helpers are in `p2/p2lib_w5.py` (jug simulator and search, redrawn scales, clocks, jugs, ribbon, time line, picture graph, towers and clue cards, readers that count the pictures back, typed forms of a time, the weights, staircase and logic brute force).

    python3 practice/holiday/build_holiday.py p2 9      # -> practice/holiday/p2/09/dist/   (git-ignored)
    python3 practice/holiday/build_holiday.py p2 10
    python3 practice/holiday/test_holiday.py p2 9       # browser test + screenshots into p2/09/proof/
    python3 practice/holiday/test_holiday.py p2 10

Sources: `p2/content/l9.js`, `l10.js` (`workbook()` = Start here; `qbank.stretch` first four = Think harder 1 to 4; `qbank.challenge` last three = Go further 5 to 7, exactly as `p2/workbook_html.js` prints them), `p2/gaps.json` (Investigation), `p2/workbook_html.js` (the "Make up your own" line). Independent checkers (none uses the printed answer or the "undo" rule): the balance scales are solved by TRYING numbers of grams (the statements are read from the labels of the figure the child sees); the jug puzzles are run step by step in a simulator and every "fewest steps" comes from a breadth-first search over all states (2 and 1 litre: 2 and 4 steps; 4 litres: 3 more steps after the printed three; 3 litres with 2 and 7: 4; 5 litres with 3 and 7: 8); the clocks' hands are copied from the printed clocks and READ BACK from the angles in the redrawn picture; times are counted on in minutes; the weights puzzle tries every set of three; the ribbons are laid on a number line; the picture graph, the cake strip and the towers are COUNTED from the drawings; digit-card numbers by trying every order; coins and dishes by trying every number of coins and plates; both logic puzzles by trying every arrangement (exactly one fits); the savings, the bus and the key-less graph by trying numbers or running a table; the staircase by listing every way.

## Items

| | Lesson 9 | Lesson 10 |
|---|---|---|
| Items | 31 | 41 |
| Start here | 17 | 19 |
| Investigation | 3 | 7 |
| Think harder | 6 | 8 |
| Go further (and Make up your own) | 5 | 7 |
| Auto-marked (number, fields, set, choice, text) | 23 | 35 |
| Self-check, typed (never auto-marked) | 7 (1(c) show how, 2(a), 2(b), 3 jug steps, Inv 3, Think harder 4 jug, Go further 5 jug) | 4 (Inv 1 and Inv 3 lists of ways, Inv 6 pattern, Think harder 4 why) |
| Open (make-up-your-own) | 1 | 1 |
| Paper-only self-check (drawing, with the correct drawing shown after Submit) | 0 | 1 (1(b): Thursday's pictures on the graph) |
| Unavailable online | 0 | 0 |
| Variant families (every combination run against an independent oracle) | 4 (4(a), 4(b), 5(c), T3: 196 combinations) | 7 (1(a), 3(b), 6(a), T1, T2 day, T3, G5: 216 combinations) |

Every item has a hint, worked steps and a skill tag. Browser test: both lessons RESULT OK (every answer typed correctly, wrong and skipped answers, reload, variants, 390/360/900 px light and dark, no horizontal scroll, figure text at least 11 px). The typed times were also run through `mark.js` by hand (7:25 am, 7:25am, 7.25 am, 7:25 a.m., "It is 7:25 am" right; 7:25 with no am/pm in 5(a), 7:35 am, 7:25 pm wrong; 5(b) and Go further 7 also accept the time with no am/pm).

## Not mirrored exactly, and why

- Printed multi-part questions are one card per part; a printed "show how" is a separate self-check card (example shown after Submit, never marked).
- Figures redrawn for a phone (the printed ones are too small and their labels collide at 390 px): the balance scales (Q1, Think harder 1 and 3, Go further 6; the pans now carry short labels such as "2 apples" that say only what the question says), the jugs, the Q3 jug table (steps 1 to 3 filled, rows 4 to 7 empty), the two clocks (hands copied from the printed ones), the ribbons, the Think harder 2 time line, the picture graph and the towers (counted back from the new drawing). The printed cake strip is used as printed. The empty Go further 7 time line of the print (just "8:15 am" on an empty line) is not shown.
- L9 jug questions (Q2(a), Q2(b), Q3, Think harder 4, Go further 5): "write the steps" cannot be auto-marked (many right ways), so each is a typed self-check with a worked way generated from the simulator (always true), PLUS an auto-marked companion card "fewest number of steps" (2, 4, 3 more, 4, 8; a step is one fill, one empty or one pour; it says "Do the steps question first"). The companion cards are not printed questions; they are added so each jug puzzle has something that can be marked.
- L9 Q3: the printed table of steps is shown as a figure (the first three steps done); the child writes the next steps and how much is in each jug in the box.
- L9 Q1(c) "show how you know" is a typed self-check after the number card. Q4(b) (take-home) repeats the red 64 cm and blue 18 cm shorter facts in its own stem so it does not depend on the answer of 4(a).
- L9 Q5(a): two text cards (clock A, clock B) typed with am or pm ("7:25 am", "7:25am", "7.25 am", "7:25 a.m."); Q5(b) and Go further 7 are text cards too (the printed answer lines are free). Q5(c) is the number of minutes.
- L9 Investigation (Weights puzzle): (a) is the list of masses from 1 g to 7 g (all seven), (b) is typed as the weights of every good set, three numbers per set, smallest first, sets in counting order (1 2 3 1 2 4), (c) is a self-check ("what do they have in common"); the printed "easy first step" is in the hint of the first card.
- L10 Q1(b) "draw Thursday's pictures on the graph" cannot be done on the screen: paper-only self-check with the correct graph (5 pictures) shown after Submit, plus an auto-marked card "how many pictures should Thursday have". The printed words "Draw the pictures for Thursday here" are not shown on the graph.
- L10 Q3 (table): the table card is the totals in cents for 1, 2 and 3 fifty-cent coins (150, 180, 210; the printed first row 0 coins = 120 is in the stem), then the two numbers of coins. L10 Q4 (logic grid) and Go further 6 (coins): the tick-and-cross table is not drawn (the child can draw it on paper); the clues are in a picture card and Q4 is four Choice cards (Ali, Mei, Siti, Ben; Siti's follows directly from clue 1, as printed). Go further 6 is one card of four boxes in cents ($1 is 100).
- L10 Q5(a) and (b) are typed as a fraction in two boxes (top number, bottom number: 5/10 is not reduced); 5(c) is typed names, most first.
- L10 Q6: the table cells 4, 5 and 6 are one card of three numbers; the printed "Tower 8" and "which tower has 36" are number cards.
- L10 Investigation (Staircase): (a) and (b) are a typed list of all the ways (self-check, shown with the worked list) plus a count card each ("Do the list question first"); (c) is the table of ways for 1 to 5 steps (five numbers, in order), a pattern self-check and the number for 6 steps (13, worked out from the pattern).
- L10 Think harder 2 (table of savings): the table is typed as the totals for days 1 to 7 for Mei and for Ali (so no card tells how many days are needed), then "which day does Mei FIRST have more". Think harder 4 is two Yes/No cards (49, 50) and a neutral explain card. Go further 7 is four cards (plates of chicken rice, smallest and biggest total, can they cost $30, can they cost every whole-dollar amount from the smallest to the biggest).
- Printed "take-home" star marks are not shown; the strategy card, "Tool of the day", "Looking back", the cut-outs and the name/date line are print-only. Lesson 10 is the Puzzle Day lesson and is mirrored exactly as printed (nothing is a project lesson here; the Make up your own puzzle for next year's group is open, with an example shown after Submit).
- No coin or note pictures; every figure is drawn.

## Week 1 to 4 audit points applied from the start

No card gives another card's answer in its stem, hint or example (the jug "steps" and "fewest steps" cards are separate and do not state the number of steps; the T4 explain card is neutral; the staircase table card does not give the number of ways for 6 steps; Think harder 2 asks seven days for both children so the answer day is not hinted; the Investigation (c) card does not state what the good sets share); hints nudge and none states the answer or a one-case rule; no example equals an answer ("like 9:10 pm", "like 2 3 4 before 2 3 5"); the printed pairing and position are kept (the three numbers of each weight set together, Ali/Ben/Mei/Siti in the stem's order, Swimming then Football, top and bottom numbers of the fractions); screen wording (no "circle", "cross out", "take-home"; paper-only cards say so); explicit unique labels of at most 12 characters; typed explanations are self-check, make-up is open; "count" cards come after the list cards and say so; every variant keeps the question possible and whole (picture, key, coin and bus numbers constrained) and has its own picture or a complete text; solution sentences were generated from the simulators or checked by hand (the jug steps cannot be false).

## Open questions for the owner

1. The "fewest number of steps" companion cards for the jug puzzles are additions (not printed): fine to keep, or should the jug puzzles be self-check only?
2. L10 Q1(b) (draw the pictures) is a paper-only self-check plus a "how many pictures" number card; L10 Q4 and Go further 6 lose the tick-and-cross table (no way to tick on screen). Fine?
3. L9 Investigation (b) is typed as "1 2 3 1 2 4" (sets one after another, smallest first). The grouping is unusual for a child; a different layout (two Yes/No cards per set) would give away that two sets exist.
4. L9 and L10 qbank items not printed in the workbook (Think harder 5 to 10 and Go further 1 to 6 of the bank) are not online, as in weeks 1 to 4.
