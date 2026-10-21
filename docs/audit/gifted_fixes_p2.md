# Fixes after the gifted-style audit: Math Inquirers P2

Source audit: `docs/audit/gifted_p2.md` (as found). Nothing committed or published. Shared files (`rebuild/slidekit.py`, `hp/*`, `levels/*`) were **not** edited. Every new or changed numeric answer was checked in Python (exact arithmetic, and every "find all" or "only one answer" claim by brute force: digit and card counts, coin ways, triangle totals, grid square counts, jug reachability, logic-puzzle solution counts).

## What was done in every lesson

- Challenge items that only repeated a worksheet or Think Harder task were replaced or upgraded (extension, generalise, justify, combine, "what if"). One problem-posing or "make up your own" prompt was added to the Challenge tier of every lesson (L1 riddle, L2 sums with one or many answers, L3 legs puzzle, L4 pattern, L5 story, L6 price list, L7 cake story, L8 cube stack, L9 jug puzzle, L10 puzzle for next year).
- Think Harder items that needed nothing from the lesson were replaced (L1, L2, L6, L8, L10); Core-page questions without an entry point got a scaffold (counters, hint, tip, drawing) or a relabel, with answers unchanged (L1 Q6, L2 Q2 and Q5, L3 Q7, L4 Q3, L6 Q5, L9 Q1 and Q3).
- Workbook Think Harder pages (`p2/workbook_html.js`): a "Look back" prompt (which puzzle was hardest, how did you start, what next time) with two answer lines was added under the Challenge items (P2 file, not shared). It fits without a new page.
- Order in each Challenge list: where a new open-ended item would have landed in the first two slots (which the Weekly Dose parent pack prints) it was moved to the middle (L2, L3, L4, L5, L9, L10). Challenge 7-9 (printed on the workbook) are all genuine extension items.
- To keep the Weekly Dose at 24 pages, some long answers were shortened (L3, L5, L6, L7, L8, L9, L10 answers; all still correct). The Question Bank grew from 21 to 25 pages because the open-ended items have longer answers.
- Keys, tutor script notes, title notes and slide notes: no worksheet answer changed, so worksheet keys and check slides are unchanged. Slides that print bank items (Stretch and Challenge slides, notes) were updated in L4, L5, L6, L8, L10.

## Per lesson (old item -> new item, tier)

### Lesson 1 Digit Detectives
- Workbook Q6b (core page): same question, scaffold added: "Tip: use 3 counters ... 1 in the hundreds box, share the other 2 between tens and ones". Answer unchanged (6 numbers).
- Think Harder 4: "Ben counts back in 100s from 980" (Core-level) -> "Mei says swapping the tens and ones digits always makes the number smaller. Is she right? When does it stay the same?" (generalise; not always, same when the two digits match).
- Challenge 4: "tens double ones, digits add to 10, who am I?" (one step) -> problem posing: "make up your own 3-digit riddle with exactly ONE answer; say how many numbers fit after each clue" (sample 324 checked: 100, 7, 1 numbers).
- Challenge 6: "closest to 500 from 0, 2, 5, 8" (one step) -> "How many numbers from three DIFFERENT cards of 0, 2, 5, 8? Why not 4 x 3 x 2?" (18).

### Lesson 2 Missing Digit Mysteries
- Workbook Q2 (core page): hint reworded as try-and-check ("answer plus take-away = start") and a borrow tip for (b). Q5a: start hint "try 110 and 120 as two corners". Answers unchanged.
- Think Harder 6: "125 + 250 + box = 1000" (Core-level) -> "Which is bigger, 347 + 258 or 350 + 255? Explain without adding." (equal, 605).
- Challenge 2: magic square 101-109 (repeat of Stretch 7) -> problem posing: "make a two-box sum with ONE answer, and one with MORE than one; what is different?" (4box6 + 37box = 801 unique, checked).
- Challenge 4: triangle 100-600, side 900 (scaled copy) -> "smallest and biggest side total from 110-160? Find side total 400. Could it be 380? Why?" (390 to 420; only 390, 400, 410, 420 possible, brute-forced).

### Lesson 3 Legs, Wheels and Arrays
- Workbook Q7: "Challenge!" label removed; wording "use counters or the table to find ALL the ways". Answer unchanged.
- Challenge 1: 20 wheels bikes/trikes (copy of Q7) -> "Ali says every number from 4 to 30 makes an array (at least 2 rows, 2 in each row). Find ALL that cannot." (5, 7, 11, 13, 17, 19, 23, 29).
- Challenge 2: crayon boxes and packs (one swap step) -> problem posing: make up a one-answer "how many of each" puzzle, then change it to have NO answer.
- Challenge 3: ducks and cows (standard) -> "10 hens and goats: ALL possible numbers of legs? Why never 21 or 42?" (20, 22, ..., 40: 11 numbers).
- Challenge 5: muffin rows (two simple steps) -> bicycles, tricycles and toy cars: 9 vehicles, 28 wheels, at least one of each, find ALL (3 ways, brute-forced).

### Lesson 4 Pattern Machines
- Workbook Q3: "Challenge!" removed; tip to draw the string in groups or use counters. Answer unchanged.
- Challenge 1: total of 1, 2, 3, 4 repeating (repeat of Stretch 5) -> problem posing: own 4-shape pattern, three far-place questions, then change the group to 5 (which answers change?).
- Challenge 7: Mei's 10th vs Ben's 8th (trivial) -> "Ali counts in 3s, Mei in 4s; both say 12; next number both say? List all up to 100; what do you notice?" (24; 12, 24, ... 96, every 12).
- Challenge 8 (printed on the workbook, on the Challenge slide): towers of 2, 5, 8 cubes, "which has 29?" (one step) -> also "is there a tower with exactly 50? with 100?" (tower 10, tower 17, none: every tower is 1 less than a 3 times table number). Slide text, answers and walk-through notes updated.

### Lesson 5 Mystery Number Machines
- Workbook: unchanged (Q2b already has the "try x2, x3, x4" scaffold; judged compliant).
- Challenge 1: "double, add 6, divide by 2" -> problem posing: own before-and-after story, then change one number (what happens to the start?). (Sample checked: 45 -> 43.)
- Challenge 3 (also on the Challenge slide): "Ben gives Ali 5 marbles, both 20" (one step) -> also "how many MORE did Ben have than Ali at first? Why not 5? What if he gave 8?" (25 and 15, 10 more, 16 more; the gap is double the gift). Slide and notes updated.
- Challenge 4: "half, then $6, $9 left" (copy of Stretch 3) -> "x2 then +1: can the OUT be 20? Which OUTs from 10 to 20 are possible?" (never even; 11, 13, 15, 17, 19).

### Lesson 6 Market Day
- Workbook Q5b: tip "draw his money as a bar cut in half". Q6 answer lines 4 -> 3 to hold the page count.
- Think Harder 3: "70c change from $1" (duplicates Core 4) -> "How many ways to pay 40c with 5c, 10c, 20c coins? List in order." (9 ways).
- Think Harder 4: "$30 - $12 - $5" (arithmetic) -> "Pens $3, books $7, 6 things, $30: how many of each? Make a table." (3 and 3).
- Challenge 1 (also on the Challenge slide): "10 coins of 10c or 20c worth $1.50" (repeat of Stretch 6) -> also "write ALL the totals 10 such coins can make; could it be $1.55?" (5 and 5; $1.00 to $2.00 in 10c steps, 11 totals). Slide, notes and walk-through updated.
- Challenge 4: "$1 with 20c and 50c coins" (one step) -> "which amounts 10c to $1 can be paid with only 20c and 50c coins, which cannot, why?" (all but 10c and 30c).
- Challenge 5: "$2 in 20c vs $2 in 50c" (division) -> problem posing: a 5-snack price list so that exactly TWO baskets cost exactly $1 (sample 50, 30, 20, 60, 40 checked).

### Lesson 7 Fair Shares
- Workbook: unchanged.
- Challenge 1: chocolate bar one-step count -> "Three children, 10 equal pieces, each a DIFFERENT number of pieces: find ALL the ways" (4 ways, brute-forced).
- Challenge 5: "1/3 of a strip of 6 squares" (fraction of a set, P3, one step) -> problem posing: own 10-piece cake story with 2/10 left; check the shares make a whole.
- Challenge 6: "1/4 of 8 slices" (P3 idea, one step) -> "Ali says the bigger the bottom number the bigger the fraction. Is he right? Show with bars; how do you pick the bigger of two with the same bottom number?"

### Lesson 8 Shape Builders
- Workbook: unchanged (all four questions compliant).
- Think Harder 1 (printed on the workbook): "quarter circles in 3 semicircles" -> "stack: bottom layer 4 by 3, middle 3 by 2, 1 on top; how many?" (19).
- Think Harder 6: "triangles in a square with one diagonal" -> "How many rectangles in a row of 3 squares joined side by side?" (6).
- Think Harder 7: "2x2x2 cube minus 1 cube" -> "3 by 2 by 3 stack, take off the top layer, then the 4 corners of the new top: how many left?" (8).
- Slide Stretch 1: "quarter circles in 2 circles and a semicircle" -> "rectangles in a row of 4 squares" (10). Notes updated.
- Challenge 1 (also on the Challenge slide): "squares in a 4 by 3 grid" -> also "another grid, longer than high and at least 2 high, also has exactly 20 squares: find ALL such grids" (4 by 3 and 7 by 2; checked 20 by 1 excluded by the rule). Slide text and notes updated.
- Challenge 3: "3 semicircles + 1 quarter circle" (one step) -> problem posing: design your own stack of exactly 20 cubes, then a different one.

### Lesson 9 Measure Masters
- Workbook Q1c: tip added ("on Scale 3, melon = apple + 4 lemons"). Q3: "Think harder!" -> "Next puzzle", cups and rice. Q3 text shortened to hold the page count. Answers unchanged.
- Challenge 1: "melon = 12 lemons" (one idea repeated) -> problem posing: own jug puzzle, then "with 4 L and 6 L jugs, can you ever measure 5 L? Why?" (never: only 2, 4, 6; all even, brute-forced).

### Lesson 10 Challenge Day
- Workbook: unchanged.
- Think Harder 3: pencils arithmetic -> "A bus: half got off, 6 got on, 14 now; how many at the start? Draw a bar." (16).
- Challenge 1: two numbers, sum 100, difference 30 -> "Which sets of three DIFFERENT digit cards make exactly 4 numbers? Write a rule." (exactly the sets with a 0: 36 sets, brute-forced).
- Challenge 2: digit riddle (one step) -> "School-journey logic puzzle: take away ONE clue at a time; which clue could go?" (none: removing any clue gives 8, 4 or 2 answers; brute-forced).
- Challenge 3: 8 bikes and trikes, 20 wheels -> "12 equal slices shared by Mei, Ben (2 more), Ali (2 more again): fractions and weight" (2/12, 4/12, 6/12; 600 g).
- Challenge 4: 9 coins 10c and 20c -> "saves 20c, 40c, 60c, ...: first day the TOTAL is MORE than $2?" (day 5; day 4 is exactly $2).
- Challenge 5: ages 7, 8, 9 (trivial ordering) -> problem posing: "make up your own challenge puzzle with a hint and exactly one answer".
- Challenge 9 (printed on the workbook, on the Challenge slide): hawker plates and bowls -> also "smallest and biggest total for 7 dishes? Can it cost $30? Every whole dollar in between?" ($21, $28, no, yes). Slide, notes updated.

## Rubric after the fixes (my re-estimate, same 12 criteria)

| Lesson | Before | After | Main changes |
|---|---|---|---|
| 1 | 12 | 16 | C3 +1 (swap claim), C6 +1, C9 +1, C10 +1 |
| 2 | 13 | 17 | C3 +1, C6 +1, C9 +1 (compare one answer vs many), C10 +1 |
| 3 | 12 | 17 | C3 +1, C6 +1, C9 +2 (posing and "change it to no answer"), C10 +1 |
| 4 | 15 | 18 | C6 +1, C9 +1, C10 +1 |
| 5 | 14 | 17 | C3 +1, C9 +1, C10 +1 |
| 6 | 13 | 17 | C3 +1, C6 +1, C9 +1, C10 +1 |
| 7 | 14 | 17 | C3 +1, C9 +1, C10 +1 |
| 8 | 11 | 14 | C6 +1, C9 +1, C10 +1 |
| 9 | 15 | 18 | C3 +1, C9 +1, C10 +1 |
| 10 | 14 | 16 | C3 +1, C6 +1, C10 +1 |

Average 13.3 -> 16.7. Tier compliance after the fixes: 100% by the same checks (every flagged item replaced, upgraded or scaffolded). Verdicts: nine lessons stay "partly"; Lesson 8 moves from mainly enrichment-practice to partly. No lesson reaches 19.

## Regenerated decks, restyled with `levels/restyle.py`

split/p2l4 (25 slides), split/p2l5 (26), split/p2l6 (26), split/p2l8 (27), split/p2l10 (31). Generators changed: rebuild/gen_p2l4.py, gen_p2l5.py, gen_p2l6.py, gen_p2l8.py, gen_p2l10.py (Stretch/Challenge slide text, notes and walk-through lines only; the diagram slides are unchanged). No slide overflow reported by rebuild/preview.py. Decks for L1, L2, L3, L7, L9 needed no change.

## Files changed

p2/content/l1.js ... l10.js; p2/workbook_html.js (look-back lines); rebuild/gen_p2l4.py, l5, l6, l8, l10; outputs rebuilt by `bash levels/build_level.sh 2` and `python3 levels/mkextras.py 2` (p2/*.pdf, p2/P2_Holiday_Program_Guide.docx, p2/Math_Inquirers_P2_Weekly_PDFs.zip, outputs/designed/Math_Inquirers_P2_*.pdf, outputs/schemes/Math_Inquirers_P2_Scheme_of_Work.pdf).

## Final page counts

| File | Before | After |
|---|---|---|
| Student workbook | 52 | 52 (per-lesson page counts identical to before) |
| Tutor guide | 63 | 63 |
| Weekly Dose of Thinking Math | 24 | 24 |
| Question Bank | 21 | 25 (longer open-ended answers) |
| Weekly email pack | 12 | 12 |
| Free taster / What Learners Get | 5 / 1 | 5 / 1 |

## Not done, for the lead to decide

- `levels/mkextras.py` (shared) says Core "builds fluency", Think Harder is "two-step problems ... larger numbers"; the new tier principle (low-floor Core, Think Harder = the taught idea in a new setting, Challenge = mastery plus extension) is not stated in the Question Bank or parent pack text. Not edited because it is shared by all levels.
- The remaining rubric gaps are design, not content: pacing flexibility and compacting (C11), multiple solution paths as tasks (C5), depth over speed (C2).
