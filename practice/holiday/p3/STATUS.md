# Level 3 (ages 8 to 10, key p3): online practice for holiday WEEK 1 (lessons 1 and 2)

Week 1 = lessons 1 and 2 (`website/data/beta_schedule.json`: group L3, Tue and Fri, lessons n=1,2 in the first week). Built, tested, NOT deployed; no website/dist, Supabase or sending.

Build and test (shared script and runner, nothing of them edited):

    python3 practice/holiday/build_holiday.py p3 1      # -> practice/holiday/p3/01/dist   (git-ignored)
    python3 practice/holiday/test_holiday.py p3 1       # Chromium, 390 px and 900 px, light and dark; proofs in p3/01/proof
    (same with 2)                                       # serve: python3 -m http.server -d practice/holiday/p3/01/dist 8792

## Where the questions come from
The printed workbook is built by `p3/workbook_html.js` from `p3/content/lN.js` (Start here = `workbook(H)`, Think harder 1 to 4 = `qbank.stretch[0..3]`, Go further 5 to 7 = `qbank.challenge[-3:]`, Take-home = `deck.takeHome`) and `p3/gifted.json` (Investigation). It is code, not data, so the structured items in `p3/0N/lesson.py` were written from those exact sources; `build_holiday.py` fails unless every printed fragment (`src`) occurs in those source files. The figures are the workbook's own: `figs_p3.js` compiles the helper functions of `p3/content/l1.js` and `l2.js` (cards, column sums, magic square, pyramids) and prints them as SVG, including completed versions used as the correct-answer pictures. `p3lib.py` holds small brute-force helpers.

## Counts (every item has a hint, a worked solution, tags strand and skill)
| Lesson | Items | Auto-marked | Self-check (never auto-marked) | Paper-only drawing | Types | Variant families (combinations all equal the oracle) |
|---|---|---|---|---|---|---|
| 1 Number Sleuths (Numbers to 10 000) | 38 | 34 | 4 | 0 | number 19, fields 8, set 4, choice 3, selfcheck 4 | 4 (351) |
| 2 Cryptarithm Crackers (Addition and Subtraction) | 32 | 26 | 6 | 0 | number 12, fields 11, set 3, selfcheck 6 | 4 (95) |

Each lesson: Start here (all printed questions including the "(if time)" ones), Investigation (No. 8 with the "Easy first step"), Think harder 1 to 4, Go further 5 to 7, Take-home pair. Items by tier L1: core 23, invest 5, stretch 5, challenge 5; L2: core 15, invest 5, stretch 4, challenge 5 (the shared runner lists Investigation before Think harder; the printed order is Think harder, Go further, Investigation).
Checkers: every answer is recomputed by loops or brute force over the numbers in the question (permutations of cards, all digit assignments, all 4-digit numbers, pyramid/magic-square line tests, 8! splits for the 4-digit difference); puzzles that print "the only way" are checked to have exactly one solution. All 10 self-check items are "explain", "notice" or "make up your own" prompts; each still carries a check of the fact the model answer states (for example that every reverse-subtraction answer is 99 times the digit gap, checked for all 3-digit numbers).

## Not mirrored one to one, and why
- No drawing/ruler task exists in these two lessons, so no paper-only items; "Make up your own" puzzles (L1 Go further 5, L2 Go further 5) and the Investigation "try 4 more numbers" are open self-checks with an example shown after submit.
- Lists (L1 No. 2, 6; Think harder 2; Investigation 8(a)) are typed with commas, any order accepted (the book asks for "in order"; order is not marked). The "How many ...?" part of each is its own number item so it is auto-marked.
- Digit-card questions where the printed answer lines are several numbers (L2 No. 2(a), 2(b), 2(c), Go further 6) ask for the sum or difference to be typed (many pairs of numbers give the same sum, 1173 or 381) and, in a second card each (2(a) places, 2(b) places, 2(c) places), for the two cards in the hundreds places, which is the same for every best way (checked by brute force). Reworded items on screen: L1 8, L2 7 (the report line "reworded"); the printed text is in each item's `src`.
- Printed lines for working ("write all the numbers", "write your tries", the look-back page, tool-of-the-day card, strategy card, name/date line) are not items. The "Look back" reflection is a paper routine and has no online version.
- Cut-out digit cards: the cards are drawn on screen, so no cutting is needed. L2 Think harder 3 has a pyramid picture that the printed page does not have (the page only describes it in words); added so the child can see it.
- No variants for the card-arrangement questions (L1 No. 1 to 2, Think harder 1 to 2, L2 No. 2): their answers come from permutations, which the shared template language (arithmetic only) cannot express. Variants exist where the answer is arithmetic: L1 3(a), 4(a), 4(b), Take-home (a); L2 5(a), 5(c), Think harder 4, Take-home (a).

## Open questions for the owner
1. Should the Investigation and Take-home pair be shown by default, or hidden behind "Want more?" like the printed "You choose" box? (They are shown as their own groups now.)
2. The printed workbook says "Think harder" is optional; online all groups are visible. Keep?

## Week 1 audit fixes (items, 24 Oct 2026; see AUDIT_WEEK1_L1_3.md)
- M1 L2 1(a): the three boxes are now named by number (top number 3_47, second number 25_8, answer _025) instead of "left to right"; stored order unchanged (4, 7, 6), matches the printed key 3447 + 2578 = 6025.
- M2 no card reveals another card's answer: L1 1(e) and its hint say "your answer to 1(d)"; L1 3(d) "which number comes right after 5000" is now conditional ("If 5000 is in the pattern"); L1 6(b) notice no longer states the counts; L1 8(c) why no longer says 18 numbers; L1 8(c) hint no longer says none start with 0; L2 3(a) fill no longer states the magic total; L2 3(b) shows the unfinished square (the finished one only in the solution) and its hint no longer lists the sums; L2 5(b) no longer prints the filled equations; L2 5(c) hint says "your answer to 5(a)".
- M3 L2 hints that named the answer reworded (2(a), 2(b) place hints; 2(c) "like 4 and 3").
- M6 L2 2(a), 2(b), 2(c): new `places` cards ask which two cards sit in the hundreds places.
- L11 L2 Think harder 2 says two letters may be the same digit here.


---

# Level 3 (ages 8 to 10, key p3): online practice for holiday WEEK 2 (lessons 3 and 4)

Week 2 = lessons 3 and 4 (`website/data/beta_schedule.json`: group L3A, Tue 1 Dec and Fri 4 Dec 2026). Built and tested, NOT deployed; no website/dist, Supabase or sending. Week 1 is described above.

Build and test (shared script and runner, none of them edited):

    python3 practice/holiday/build_holiday.py p3 3      # -> practice/holiday/p3/03/dist   (git-ignored)
    python3 practice/holiday/test_holiday.py p3 3       # Chromium, 390 and 900 px, light and dark; proofs in p3/03/proof
    (same with 4)                                       # serve: python3 -m http.server -d practice/holiday/p3/03/dist 8792

## Where the questions come from
The printed workbook is built by `p3/workbook_html.js` from `p3/content/l3.js` and `l4.js` (Start here = `workbook(H)`, Think harder 1 to 4 = `qbank.stretch[0..3]`, Go further 5 to 7 = `qbank.challenge[-3:]`, Take-home = `deck.takeHome`) and `p3/gifted.json` (Investigation). It is code, not data, so the structured items in `p3/03/lesson.py` and `p3/04/lesson.py` were written from those exact sources; `build_holiday.py` fails unless every printed fragment (`src`) occurs in them. Figures are the workbook's own: `figs_p3_w2.js` compiles `arraySvg` (l3.js), `q1Fig/q2Fig/q3Fig` (l4.js) and takes the bar models of `p3/figs_l3.js` (Q4, Q5, Q6, Think harder 1 to 4, Go further 7); the times-table strips (Q1, Q2) and the grid puzzle (Q4) are redrawn in `p3lib.py` (`times_fig`, `grid_fig`) from the printed tables. `figs_p3_w2.js` also widens each figure's viewBox so that the row labels ("Ali before", "3rd piece", "150 altogether") are not clipped when the builder raises figure text to 12 px on a phone.

## Counts (every item has a hint, a worked solution, tags strand and skill)
| Lesson | Items | Auto-marked | Self-check (never auto-marked) | Paper-only | Types | Variant families (combinations all equal the oracle) |
|---|---|---|---|---|---|---|
| 3 Times Table Treasure (Tables of 6, 7, 8 and 9) | 37 | 29 | 8 | 0 | fields 9, number 8, choice 6, set 6, selfcheck 8 | 4 (56) |
| 4 Model Makers (Word problems: bar models) | 32 | 27 | 4 | 1 | number 14, fields 10, choice 3, selfcheck 5 | 15 (312) |

Items by tier: L3 core 21, Investigation 7, Think harder 5, Go further 4; L4 core 14, Investigation 8, Think harder 4, Go further 6 (G5 to G7, then the Extra pair). The shared runner lists Investigation before Think harder; the printed order is Think harder, Go further, Investigation.
Unavailable online (nothing is unavailable that the printed pages ask a child to answer): the "Look back" reflection page and the strategy card (paper routines, as in week 1).
Checkers: every answer is recomputed by loops over the numbers of the question (times tables built by repeated adding, last digits of the table, all 5 unknown numbers of the grid in 1 to 10 with exactly one solution, every number of rows for 36 chairs, digit sums of the tables, ages year by year, every bar-model story by trying the unknown number). Puzzles that print "the only way" are checked to have exactly one solution. Every self-check item that states a fact (for example the swap when Mei gives 38) also carries a check of that fact.

## Not mirrored one to one, and why
- Typed written answers ("Finish the sentences", "Explain", "What do you notice? Why?") are self-check items with a model answer. Where a printed written answer has an objective part, an auto-marked companion card checks it: L3 1(a) tens digits and ones digits (choice, from the 9 times table), L3 1(b) "what is 9 × 8 really", 2(b) last digit (number) with its explanation as a self-check, 3(b) "9 × 6" (number) with the split as a self-check, 5(c) the way with no partner (two boxes) with the why as a self-check; L4 5(b) "test Ravi's idea" (boxes), 6(c) what happened to the difference (choice); Investigation: the digit sum and what the child "notices" are choice or number cards.
- L3 Q5 (36 chairs): the printed table pairs the number of rows with the chairs in each row. Online: 5(a) rows (a list, smallest first, order is marked) and 5(a) chairs "in the same order" (second list, order marked), so the pairing is checked; 5(b) is the count and 5(c) names the way with no partner (6 rows of 6). The printed hints that show examples that are answers ("3 rows of 12 is different from 12 rows of 3", "like 2 rows of 18 and 18 rows of 2") are reworded with other numbers so that no card gives another card's answer.
- L3 Q4 (grid): row and column numbers (4(a), order kept: rows top to bottom, columns left to right) and the missing products (4(b)) are two cards with the same grid picture. The printed hint "And 81 = 9 × 9" is not shown (it is an answer); the hint asks which two numbers from 1 to 10 make 81.
- L3 Q6(a) "circle the ones that are also in the 6 times table (6, 12, 18, 24 ...)": typed list, the example list stops at 18 so that 24 (an answer) is not shown.
- L3 Investigation 8(a) to 8(c): "Easy first step" (the 9 times table to 9 × 6) and 8(a) (9 × 11, 9 × 12) are boxes; "Is the total ALWAYS 9" and "Is the 4 times table the same?" are choices; the 4 times table digit sums are boxes; "What do you notice about the 3 and 6 tables" is a choice (every digit sum is in the 3 times table); "What can you say about the 3, 6 and 9 times tables" is a self-check.
- L4 Investigation: the printed table has 6 rows (now to 5 years) and four columns. Online: the easy first step is row 1 (difference and total, the printed easy step gives the ages), then two cards of boxes (ages for 2 to 5 years; difference and total for now and 2 to 5 years). "What stays the same / what changes / how" = a choice and a number ("the total goes up by 2"); "double", "triple" = a number (3 years) and a choice (triple: not from now on) plus an explain self-check.
- L4 G5 (make up your own story, draw its model) is paper-only (never auto-marked); the correct-drawing figure after Submit is the model of the model answer (Ali 50, Ben 20, Ali gives 15, 35 each), drawn on screen.
- L4 Think harder and Go further have a figure only where the printed page has one (T1 to T4, G7); L4 Q1 to Q6 use the printed bar-model skeletons (given numbers and question marks).
- L4 "Take-home (a)" and "(b)" are called "Extra (a)" and "(b)" and say "Extra practice (not for the lesson)" (paper wording "take-home" avoided on screen). Lesson 3 has no Take-home pair in the workbook (`deck.takeHome` is empty).
- Wording for screens: no "circle", "cross out" or "write on the page" in the stems; "(if time)" is kept as printed. Nav labels: Think harder items are T1 to T4, Go further G5 to G7, Investigation 8, 8(a)..., so that each button says which question it is (week 1 showed "Think" and "Investigation" on every button).
- No variants for the grid, the chair lists, the digit-sum cards and the riddles (no arithmetic template with an oracle); variants exist where the answer is arithmetic: L3 1(b) 9 × n, 2(b) last digit of t × n, 3(a) split array, Think harder 2 last digit of a × a × a; L4 15 families (Q1(a), Q1(b), Q2(a), Q3(a), Q3(b), Q4, Q5(a), Q6(a), Think harder 1 to 4, Go further 6, Extra (a) and (b)).

## Open questions for the owner
1. Same as week 1: should the Investigation (and the Extra pair) be shown by default, or hidden behind "Want more?" like the printed "You choose" box? Think harder is "optional" in print; online all groups are visible.
2. Lesson 3 Investigation: "Is the total ALWAYS 9?" is answered No because of 9 × 11 = 99 (digit sum 18). The model answer also says 18 is itself in the 9 times table (the gifted.json model answer). Fine for ages 8 to 10, or too much?
3. L3 5(a) marks the order of the two lists (smallest number of rows first, chairs in the same order). Say if the order should not be marked (then the pairing is no longer checked).


---

# Level 3 (ages 8 to 10, key p3): online practice for holiday WEEK 3 (lessons 5 and 6)

Week 3 = lessons 5 and 6 (`website/data/beta_schedule.json`: group L3A, Tue 8 Dec and Fri 11 Dec 2026, lessons n=5 and n=6; `p3/content/l5.js` and `l6.js` also say `week: 3`). Built and tested, NOT deployed; no website/dist, Supabase or sending. Weeks 1 and 2 are described above. The shared files (sheet.js, submit/*, build_holiday.py, hlib.py, test_holiday.py) and the earlier lessons were not edited.

Build and test (shared script and runner):

    python3 practice/holiday/build_holiday.py p3 5      # -> practice/holiday/p3/05/dist   (git-ignored)
    python3 practice/holiday/test_holiday.py p3 5       # Chromium, 390 and 900 px, light and dark; proofs in p3/05/proof
    (same with 6)                                       # serve: python3 -m http.server -d practice/holiday/p3/05/dist 8792

## Where the questions come from
The printed workbook is built by `p3/workbook_html.js` from `p3/content/l5.js` and `l6.js` (Start here = `workbook(H)`, Think harder 1 to 4 = `qbank.stretch[0..3]`, Go further 5 to 7 = `qbank.challenge[-3:]`, Take-home = `deck.takeHome`) and `p3/gifted.json` (Investigation). It is code, not data, so the structured items in `p3/05/lesson.py` and `p3/06/lesson.py` were written from those exact sources; `build_holiday.py` fails unless every printed fragment (`src`) occurs in them. Figures: `figs_p3_w3.js` compiles `shareSvg` (l5.js: 47 counters, 6 plates) and takes the empty bars of `p3/figs_l3.js` (Q5 fence, Think harder 2 to 4, Go further 6) and the printed wall, shapes and cards of l6.js. `p3lib_w3.py` redraws the fraction wall, the five shapes (A to E) and the ten partner cards larger (the printed row is about 50 px per shape on a phone), draws the "pieces" and the "ways" bars, and holds the fraction helpers; the shape item checkers count the equal and the shaded parts of the PRINTED figure's svg and the build stops if they differ from the key (4/1, 8/2, 6/2, 12/3, 8/3).

## Counts (every item has a hint, a worked solution, tags strand and skill)
| Lesson | Items | Auto-marked | Self-check (never auto-marked) | Paper-only drawing | Types | Variant families (combinations all equal the oracle) |
|---|---|---|---|---|---|---|
| 5 Remainder Riddles (Division) | 38 | 35 | 3 | 0 | number 13, fields 13, choice 4, set 3, text 2, selfcheck 3 | 12 (375) |
| 6 Fraction Walls (Fractions) | 55 | 48 | 5 | 2 | text 29, choice 10, number 5, fields 4, selfcheck 7 | 3 (124) |

Items by tier: L5 core 19, Investigation 8, Think harder 4, Go further 7 (G5 to G7 and the Extra pair); L6 core 31, Investigation 8, Think harder 7, Go further 9 (G5 to G7 and the Extra pair). The shared runner lists Investigation before Think harder; the printed order is Think harder, Go further, Investigation.
Self-checks: L5 make-up riddle (open, no objective fact), Investigation "explain why", G6 "explain how you know" (all carry a checked fact); L6 Think harder 2 "show how", Investigation "how do you know you have all", G5 make-up riddle (open) and "which numbers work", G7 "another fraction"; paper-only with a drawn correct answer: Investigation "list every way" and G6 "find all the ways" (the bars of every way are drawn after Submit).
Unavailable online (nothing is unavailable that the printed pages ask a child to answer): the "Look back" reflection page and strategy card (paper routines, as in weeks 1 and 2). Counting with counters/cups (explore activity) is a lesson activity, not a workbook question.
Checkers: every answer is recomputed by counting up in the divisor, trying every number or day (the 100-day questions step one day at a time), cross-multiplying for equal fractions, exact `Fraction` arithmetic for sums, differences and orders, counting the shaded and equal parts of the printed shapes figure, and trying every way to fill a bar with halves, quarters and eighths (6 ways for 3/4, 9 for 1 whole, 2 with exactly 5 pieces). Puzzles that print "only one" (Q4 "I am", T2, Q6 tables, G7 pens, Q6 partner cards) are checked to have exactly one solution. Every self-check that states a fact also carries a check of it (for example that 3 in a row always has exactly one multiple of 3, and that the fractions equal to 3/4 have top plus bottom in the 7 times table).

## Not mirrored one to one, and why
Lesson 5
- Q1(c) "What is wrong? Write the correct answer." is two cards: a choice (the remainder 11 is bigger than 7) and boxes for 8 remainder 4.
- Q4(a): the printed table has a candidate row and a "remainder when divided by 4" row. Online: the list of numbers for the first clue (set, any order) and the "I am" number. The remainders-by-4 row is not its own card (it would have to print the list, which is the other card's answer).
- Q6: the printed table (children for 1 to 6 tables, both ways) is two cards of boxes (2 to 6 tables; the first column is given in the stem); (a) tables and children, (b) empty seats are self-contained stories (they do not depend on (a) on screen).
- Q2, Q3, Q5 as printed. 5(a) remainders is typed with commas (any order). "(Draw them to help)" became "Draw a picture on paper to help if you like".
- Investigation (three in a row): the printed "try 5 starting numbers of your own" is fixed to 7, 25, 61, 118 and 152 (one above 100); "Is it always exactly one?" and the 4-in-a-row and 2-in-a-row changes are choice and boxes cards; "Explain why" is a self-check. The printed intro says that exactly one of 14, 15, 16 is in the 3 times table (15); that sentence is not shown on screen, so that no card gives away the answer of "is it always exactly one?" (14, 15, 16 stay as the example).
- Go further 6 asks two day cards (after and ago, typed day name or the first three letters) and an explain self-check. Go further 5 (make up) is open and marked "open" in the tutor report.
- Variants: where an arithmetic template with an oracle exists (1a, 1b, 2a to 2d, 3a, 3b, T1, T4, Extra (a), Extra (b)); none for riddles, lists, the table puzzle, G6/G7, because their answers are lists, days or searches (no template language for them).

Lesson 6
- Typed fractions: a fraction is typed with a slash (`5/7`), any equal fraction is accepted (`10/14`, `3/6` for `1/2`) through `equiv_frac`; lists (2(g), T4) accept equal fractions in the same order, also with `<` between them. T1 (bottom number 12) and G7 are exact forms / a list of accepted fractions (see below).
- Q1(d) "what do you notice about the top and bottom numbers" is a choice (each bottom number is double its top number); the printed "(c) take-home" is kept as Q1(c) with the on-screen note "Extra practice (not for the lesson)". The Q6 take-home partner puzzle is five cards (one per yellow card, type the blue card's fraction) with the ten cards drawn in two rows.
- Q2 circles (a) to (f) are six choice cards (greater, less or equal), (g) is a typed order.
- Q3: (a) "which shapes have exactly 1/4" is typed letters (any order). The printed (b) asks only the OTHER shapes, which would reveal the answer of (a), so (b) is five cards (every shape, A to E, any equal fraction accepted).
- Q4: the printed example "1/2 + 1/4 = 2/4 + 1/4 = 3/4" is the answer of 4(c) (3/4 = 9/12), so the example in the hint is 1/5 + 1/10 = 2/10 + 1/10 = 3/10. The wall is shown on 4(b), 4(c), 4(d) only (it has no fifths or tenths).
- Think harder 1: two cards (the list with bottom number 12, and 2/3 = ?/12). Think harder 2 "show how you know" is a choice plus a self-check.
- Go further 5: make up (open), "does it work for ANY number" (choice) and "which numbers work, and why" (self-check). Go further 6: how many ways (number) and the list (paper-only, drawn answer). Go further 7: one fraction between 2/3 and 3/4 is auto-marked against every n/d with bottom number up to 60 that lies between them (found by cross-multiplying); "another one" is a self-check with examples. A correct fraction with a bottom number above 60 would be marked wrong.
- Investigation (find all the ways to make 3/4): one half left (fraction), ways with one half (2), with no half (4), in all (6), the list (paper-only, the six ways drawn), "how do you know you have them all" (self-check), "more or fewer ways for 1 whole" (choice) and how many (9). The pieces figure is shown on each card so that the setup is not repeated in words.
- Variants: only the equal-fraction box cards (1(a), 1(b), 1(c)): the variant engine makes number and box answers only, not typed fractions.

## Week 1 and 2 audit rules applied from the start
No card shows another card's answer in a stem, hint or figure (checked by reading every card: for example G5 "any number?" does not say which numbers work, I8 easy no longer says "exactly one", 3(b) asks every shape); hints nudge without giving the answer; examples never equal an answer (Q4 example, make-up hints use other numbers); solutions are true for every case they name (the "n numbers in a row" statement and "more ways for 1 whole" are checked by loops); positions/pairings kept (Q6 partner per yellow card, shape letters, row/column of the table as labelled boxes); no long riddle repeated: the Investigation pieces and the party tables are in the card boxes; screen wording ("type", "write down", no circle or cross out); unique nav labels set where two cards share a printed number; self-checks have `marking_mode` set (explain = self, make-up = open).

## Open questions for the owner
1. Typed fractions (Level 3 Lesson 6): children type `3/4`; there is no fraction keypad or stacked fraction box. Fine for ages 8 to 10, or should we add a fraction input to the shared runner?
2. G7 (a fraction between 2/3 and 3/4) accepts any fraction with a bottom number up to 60. Enough, or should the tutor mark it by hand?
3. 3(b) is five cards (all shapes) rather than the printed "the other shapes" to avoid giving the answer of 3(a). Keep?
4. Same as weeks 1 and 2: should the Investigation and Extra pairs be visible by default or behind "Want more?"

## Week 3 L1-3 audit follow-up (item level)
M1 answer leaks reworded, M2 explicit short nav labels, remainder-0 variants excluded (P3 L5 3(b)), long stems shortened, doubled "Make up your own"/"Take-home" lead-ins removed. Print-inherent chains kept as printed (P1 L5 Go further 1(a)/(b), 3(c); P1 L6 Q4/Q5, T3/Q6; P3 L6 5(b), T3). P1 L6 Q5/Q6 keep cents only (printed answers are in cents).


---

# Level 3 (ages 8 to 10, key p3): online practice for holiday WEEK 4 (lessons 7 and 8)

Week 4 = lessons 7 and 8 (`website/data/beta_schedule.json`: group L3A, Tue 15 Dec and Fri 18 Dec 2026, lessons n=7 and n=8; `p3/content/l7.js` and `l8.js` also say `week: 4`). Built and tested, NOT deployed; no website/dist, Supabase or sending. Weeks 1 to 3 are described above. Shared files (sheet.js, submit/*, build_holiday.py, hlib.py, test_holiday.py) and earlier lessons were not edited.

Build and test:

    python3 practice/holiday/build_holiday.py p3 7      # -> practice/holiday/p3/07/dist   (git-ignored)
    python3 practice/holiday/test_holiday.py p3 7       # Chromium, 390 and 900 px, light and dark; proofs in p3/07/proof
    (same with 8)

## Where the questions come from
Same as weeks 1 to 3: `p3/workbook_html.js` builds the workbook from `p3/content/l7.js` and `l8.js` (Start here = `workbook(H)`, Think harder 1 to 4 = `qbank.stretch[0..3]`, Go further 5 to 7 = `qbank.challenge[-3:]`, Extra = `deck.takeHome`) and `p3/gifted.json` (Investigation). Items are in `p3/07/lesson.py` and `p3/08/lesson.py`; `build_holiday.py` fails unless every printed fragment occurs in those sources. Figures: `figs_p3_w4.js` prints the workbook's own figures and data (cells of figures A to D, the six angles) from the generator functions; `p3lib_w4.py` redraws them larger, one angle / shape / letter per card, and the lesson files assert that the data (L-shape, staircase, L of 4 squares, shape outlines, letter lines, grid points, fan, window, clocks) equals the printed figures. Clocks and the U shape/# sign/long rectangle are drawn on screen (the printed pages have no picture for Think harder 2, 4 and Go further 6).

## Counts (every item has a hint, a worked solution, tags strand and skill)
| Lesson | Items | Auto-marked | Self-check | Paper-only drawing | Types | Variant families (all combinations equal the oracle) |
|---|---|---|---|---|---|---|
| 7 Area Architects (Area and perimeter) | 42 | 38 | 4 (2 open make-up/own-square) | 0 | fields 12, number 11, choice 7, set 5, text 3, selfcheck 4 | 10 (168) |
| 8 Angle and Line Detectives (Angles, perpendicular and parallel lines) | 48 | 43 | 2 | 3 | choice 19, number 13, fields 8, set 3, selfcheck 5 | 4 (19) |

Checkers: every answer is recomputed from the figure data: squares and square edges (area, perimeter of A to D, the staircase, every fixed shape of 5 squares for Go further 6), the shoelace rule for the L-shape, every pair of sides for parallel/perpendicular (letters, # sign), corners of each outline by turn direction (right angles vs dents), right angles at every meeting point (window, row of squares), the hands of the clock (30 degrees an hour), staircase outlines for 1 to 59 steps, all six-sided shapes on a 3 by 3 lattice (most right angles is 5, 6 never occurs), directions of lines by cross and dot products.

## Not mirrored one to one, and why
- Lesson 7 Q1 table: one card per figure (A to D, area and perimeter boxes), then (a) a choice of the pair and (b) typed letters. Q2 list of gardens: lengths, widths and areas are three ordered lists (longest length first, order marked so the pairing is checked), plus a count card and the biggest-area card; the printed "Check: perimeter" column is not an item. Q4: missing sides (boxes), area, perimeter; the printed hint "across = 10 - 6, down = 7 - 4" is not shown (it is the answer). Q5(c) is three cards (perimeter, area, how much more). Q6 ("draw it"): the on-screen version marks nine places A to I where the new square could go; the child types the letter (any of eight for 12 cm, only E for 10 cm) and answers Yes/No for 8 cm plus an explain self-check. The L shape pictures show the squares as drawn; the printed two grids are one picture.
- Lesson 7 Investigation: easy step (4 boxes), what changed (choice), the 6 cm and 10 cm squares (4 boxes each), own square (open), always true (choice, tested for sides 2 to 40) and an explain self-check with the "move the bottom row" picture. Think harder 1 is three cards (lengths, perimeters in the same order, the shortest). Go further 5 (make up) is open.
- Lesson 8 Q1: six cards, one angle each (bigger picture); the paper checker is used on the screen as before. Q2: shapes B, C, D (A is "done for you" and quoted in the stem). Q3: counts by size (5 boxes), total, and the take-home 8 lines. Q4: one card per letter (parallel only / perpendicular only / both / neither) instead of two Yes/No rows; Z and N are marked "Extra practice". Q5: drawing with a ruler stays paper-only (the correct line is drawn after Submit); each drawing has a companion card "which numbered line" (auto-marked) so the idea is checked; the printed hint "try 1 right and 2 down" is not shown (it is the answer of the companion). Q6: points card (4 corners, 4 side points, middle) and total.
- Lesson 8 Investigation: easy step, four rows of the table (one card per staircase with its picture), the 10-step prediction, always even (choice) and why (self-check). Think harder 3 is three set cards (smaller, right, bigger); Go further 5 (make up) is open; Go further 7 is two cards (can it, the most). The hexagon claim is checked by brute force on a 3 by 3 lattice only (plus the printed note "a proof is not expected").
- Not items: "Look back" page, strategy card, fold-the-checker activity (explained in the About box).
- Variants only where an arithmetic template with an oracle exists: L7 fence count, Q3, Q4 area/perimeter (with their own L-shape pictures), Q5 staircase area/perimeter (with pictures), 8(b) 6 cm square, Think harder 2, Go further 7, Extra; L8 take-home fan (with fan picture), Go further 6 (with picture), staircase rows 4 and 10 steps.

## Audit rules applied from the start
No stem, hint, example or figure shows another card's answer (Q5 hint of the printed paper task omitted; Investigation stems do not state the pattern; 6(c) explain is neutral; letter/line cards do not name the result); hints nudge; solutions are checked true for the cases they name; explicit unique labels (at most 12 characters, no "?"); screen wording; make-up and explain cards have marking_mode set.

## Open questions for the owner
1. Lesson 7 Q6 and Lesson 8 Q5 are drawing tasks on paper in print. Online they use lettered places / numbered lines (auto-marked); the real drawing stays paper-only. Fine?
2. Same as earlier weeks: should the Investigation and Extra question be visible by default or behind "Want more?"
3. Lesson 8 uses a paper right-angle checker against the phone screen. Acceptable, or add an on-screen checker later?


# Level 3 (ages 8 to 10, key p3): online practice for holiday WEEK 5 (lessons 9 and 10)

Week 5 = lessons 9 and 10, the last two lessons of the programme (`website/data/beta_schedule.json`: group L3A, Tue 22 Dec and Thu 24 Dec 2026, lessons n=9 and n=10, 25 Dec is a no-lesson day; `p3/content/l9.js` and `l10.js` also say `week: 5`, session A and B). Built and tested, NOT deployed; no website/dist, Supabase or sending. Shared files (sheet.js, submit/*, build_holiday.py, hlib.py, test_holiday.py) and earlier lessons were not edited; `practice/ext/test_ext.py` and the `practice/submit` tests still pass. Lesson 10 is the showcase lesson ("Puzzle Day"): it is mirrored as printed (bar graph, CCA logic grid, queues, digit cards, matchstick squares, a number riddle, handshakes); its paper tasks are self-check or open cards with a model answer.

Build and test:

    python3 practice/holiday/build_holiday.py p3 9      # -> practice/holiday/p3/09/dist   (git-ignored)
    python3 practice/holiday/test_holiday.py p3 9       # Chromium, 390 and 900 px, light and dark; proofs in p3/09/proof
    (same with 10)

## Where the questions come from
Same as weeks 1 to 4: `p3/workbook_html.js` builds the workbook from `p3/content/l9.js` and `l10.js` (Start here = `workbook(H)`, Think harder 1 to 4 = `qbank.stretch[0..3]`, Go further 5 to 7 = `qbank.challenge[-3:]`, Extra = `deck.takeHome`) and `p3/gifted.json` (Investigation). Items are in `p3/09/lesson.py` and `p3/10/lesson.py`; `build_holiday.py` fails unless every printed fragment occurs in those sources. Figures: `figs_p3_w5.js` prints the workbook's own figures (ribbon, 24-hour strip, time lines, bus line, bar models, queues, drinks graph, matchstick squares, digit cards, the five item pictures) from the generator functions; `p3lib_w5.py` redraws them larger for a 390 px phone (every text at least 12.5 px; no rotated text, no nested svg) and the lesson files assert that their data (the ribbon pieces, strip hours, time-line ticks, bus line, bar-model labels, queue positions, the four drinks bars at 4 px per cup, digit cards, the printed sticks table, the five prices, the printed clues) equals the printed figures. Pictures drawn that the print has none for: the Think harder 3 triangles in a row, the shared clue cards (see below).

## Counts (every item has a hint, a worked solution, tags strand and skill)
| Lesson | Items | Auto-marked | Self-check | Paper-only drawing | Types | Variant families (all combinations equal the oracle) |
|---|---|---|---|---|---|---|
| 9 Measure and Money Masters (length, mass, volume, money, time) | 42 | 37 | 5 (4 compare with a model answer, 1 make-up G7 open) | 0 | fields 16, number 12, text 7, selfcheck 5, choice 2 | 16 (832) |
| 10 Puzzle Day (mixed puzzles: bar graphs and logic) | 36 | 32 | 4 (2 explain, 1 paper drawing of the Lime juice bar, 1 make-up G5 open) | 1 | number 14, choice 9, fields 5, set 3, selfcheck 4, text 1 | 8 (124) |

Checkers: every answer is recomputed, not copied. Lesson 9: changing units by adding and taking away (cm, g, ml); bags ordered by grams; every set of 3 things from the price list (the best set under $20 is unique: book, pen set, puzzle, $19.35, change 65 cents; the next best is $17.95); 12-hour to 24-hour conversions; every time sum and difference in minutes since midnight (swimming, piano, film, shop hours); the six buses listed 25 minutes apart (next bus after 08:15, latest bus to arrive by 08:30); cups counted by taking 300 ml away one at a time; the box, bottle and pens-and-files puzzles by search; every way of paying 50 cents tried one coin at a time (12 ways, equal to the printed list in `gifted.json`, fewest 3 coins, most 10 coins). Lesson 10: Lime juice from the 200 total and the four bars; every pair of drinks for 100; every way to give four CCAs (one fits the clues) and every way to give three pets (one fits); queues built child by child; every number made from the digit cards (6 numbers, 2 odd, 582 closest to 600); sticks counted from the squares and triangles (3n + 1, 2n + 1); every number that fits the riddle (213, 321, 411); every amount from three coins (7); every 4-digit number from 3, 0, 6, 9; the class papers by trying every kg for 3P2; handshakes counted pair by pair (none equals 20 for any group size up to 199).

## Not mirrored one to one, and why
- Lesson 9 Q1 is six cards (a to f; (f) shows the ribbon picture). Q2(a) puts letters on the four bags (C, D, B, A, "lightest first"); the printed "write the masses in order" would need typed masses in three different units. 2(b) "Explain Ben's mistake" is a self-check card (neutral wording) plus an auto-marked card "how many grams is 1 kg 30 g". Q3: yes/no and the total for (a); the three names and the change for (b) (names accepted in any order, "pen set"/"pens"). Q4 table: four cards (7:15 am, 3:40 pm, 20:05, 12:30 pm); 24-hour answers are typed in two boxes (hours : minutes). The printed strip is drawn as two rows (am, pm) so the labels fit a phone. (b) yes/no plus an explain self-check. Q5 (a), (b), (c): hours-and-minutes boxes and "hours : minutes pm" boxes (so the variants can be checked); Q6: the printed table of buses is one text card (2nd to 6th bus), then next bus, wait and arrival at school. The printed "(if time)" labels are dropped.
- Lesson 9 Investigation: the easy step is a card on swapping 5-cent coins (it does not show a way); the list of ways is a self-check card (the table of all 12 ways is shown after Submit) with auto-marked companions (ways by number of 20-cent coins, total, the fewest-coin way, the most-coin way) and an explain self-check. Not items: the "Look back" tick boxes, the tool-of-the-day boxes.
- Lesson 10 Q1: the graph card (Lime juice missing), most, difference, Lime juice, the Lime juice bar on paper (paper-only self-check, the drawn bar is shown after Submit), the two drinks that make 100. Q2 CCA grid: the tick-and-cross grid itself is a paper tool and is not an item; the clues are one shared picture card and the four children are four choice cards (Ali, Mei, Ravi, Siti). Q3: two queue cards with the printed pictures (the printed picture of 3(a) already shows both counts, as printed). Q4: the list (ordered), the odd count and the closest to 600. Q5: the table of 4, 5 and 6 squares, 8 squares, and 31 sticks. Q6 riddle: unordered list, printed hint kept.
- Lesson 10 Investigation: handshakes for 3 to 6 friends, how many more each row has, the pattern (explain self-check), 10 friends, "could it be 20?" (yes/no) and why (explain). The printed "easy first step" (draw 3 dots, count the lines, then 4 dots) is the hint of the first card because as a card it would be the answer of the first box. Think harder 1 is a list card plus a count card ("Do the list question first"); Think harder 2 is one shared clue picture and three pet cards; Go further 5 (make up a logic puzzle) is open and the model puzzle is verified (unique answer, and the fourth clue can be dropped). Go further 6 and 7 have no printed picture (the print says "a bar graph shows..." without drawing it), so none is drawn.
- Variants only where an arithmetic template with an oracle exists (no variants for text, set or choice items): L9 1(a) to 1(f), 4(a) am and pm conversion, 5(a) to 5(c), Think harder 1 to 3, Go further 5, Extra (a); L10 queues 3(a) and 3(b), odd numbers from other cards, sticks 5(a) and 5(b), Think harder 3, both Extra questions.

## Audit rules applied from the start
Weeks 1 to 4 audits read. No stem, hint, example or figure shows another card's answer (the CCA and pet cards share one clue picture and say only "Use the clues"; the explain cards for 17:00 and for 20 handshakes are neutral; the easy step is not a card; the bus-table hint does not give the 2nd bus; the swap card does not show a way); hints nudge and state no one-case rule (the 12:30 pm solution says to add 12 only from 1 pm; "every other set that fits in $20 costs less"); the count cards say "Do the list question first"; money accepted as $1.60, 1.60, 160 cents (and the cents answer also as $0.65); times with a space before pm, "8.05 pm", "p.m"; letter lists in any separator; no "(if time)", "cross out" or "take-home" wording in cards; explicit short unique labels (at most 12 characters, number first, no digit-letter-digit); reading load kept to about 45 words or fewer per card; make-up and explain cards have marking_mode set; no coin or note pictures (the five item pictures are the workbook's own small icons).

## Open questions for the owner
1. Lesson 10 Q2 (CCA logic grid) and the Lime juice bar: the grid is a paper tool, so online it is four choice cards (auto-marked) with the clues shown once. Is that acceptable, or should an on-screen tick/cross grid be added later (shared runner change)?
2. Times of day are typed in two boxes ("hours : minutes"); a child who types "5:25" into the first box is marked wrong. Fine for ages 8 to 10, or should the runner learn to read "5:25" in one box?
3. Lesson 9 Q4 conversion cards say "Write ... in 24-hour time" and the printed hint "after 12 noon add 12" is only said for pm times after 1 pm (12:30 pm stays 12:30). Fine?
4. Same as earlier weeks: should the Investigation and Extra questions be visible by default, and do the Lesson 10 certificate and the "Look back" page need an online counterpart?

## Week 5 audit fixes (24 Oct 2026, lessons 9 and 10)
- L9 clock-time boxes are labelled "Hours:" and "Minutes:" so the runner sets time=True automatically (a whole time typed in the first box, empty minutes = 0). order_forms also accepts "C < D < B < A" (true, lightest first), "Bag C ..." and "C. D. B. A."; L10 1(d) accepts "Milo & Kopi". Variants no longer add "Draw it on paper if it helps".
- "Draw circles" hints reworded ("Picture circles"), "Hint: Hint:" doubled prefix removed, G5 and G7 stems shortened (G7 no longer says "A bar graph shows" when no graph is drawn).
