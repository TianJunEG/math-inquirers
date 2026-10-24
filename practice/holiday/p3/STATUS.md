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
