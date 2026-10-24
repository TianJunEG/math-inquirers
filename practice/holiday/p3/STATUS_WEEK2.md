# Level 3 (ages 8 to 10, key p3): online practice for holiday WEEK 2 (lessons 3 and 4)

Week 2 = lessons 3 and 4 (`website/data/beta_schedule.json`: group L3A, Tue 1 Dec and Fri 4 Dec 2026). Built and tested, NOT deployed; no website/dist, Supabase or sending. Week 1 is described in `STATUS.md` (same folder).

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
