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
