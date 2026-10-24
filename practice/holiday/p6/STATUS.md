# Level 6 (ages 11-13) online practice, holiday week 1 (lessons 1 and 2)

Build: `python3 practice/holiday/build_holiday.py p6 1` (and `2`); test: `python3 practice/holiday/test_holiday.py p6 1` (and `2`). dist is git-ignored; nothing is deployed.
Sources: `p6/content/l1.js`, `l2.js` (the workbook is hand-written JS, so each question was extracted by hand into `p6/NN/lesson.py`), `p6/content/gaps.json` (Investigation).
Figures: the code blocks are the workbook's own `blocks()` drawing, called through `p6/blocks_bridge.js`; the matchstick picture and factor trees are redrawn larger for phones (`p6lib.py`).
Checkers: every item has an independent checker (loops, or the block-program interpreter `p6lib.run`); the build fails if one differs from the printed answer. Week 1 = lessons 1 and 2 (Thu 26 Nov and Sat 28 Nov, group L6A).

| Lesson | Items | Auto-marked | Self-check (shown solution) | Paper-only (drawing/planning code) | Variant families |
|---|---|---|---|---|---|
| 1 Code the Pattern | 37 | 30 | 4 | 3 | 3 (117 combinations vs oracle) |
| 2 Prime Hunters | 44 | 37 | 4 | 3 | 1 (12 combinations) |

Unavailable (no item at all): none of the printed questions is dropped. Scratch itself is never run in the page.

Not mirrored one-to-one, and why
- Written-answer boxes become typed answers: rules for the nth term are two number boxes (type a minus sign for a negative); lists of primes/factors are comma lists; "Prime?" and "How many?" columns are one multiple-choice item per number; "Explain" parts are separate self-check items with the key facts checked by code. Most items are therefore "reworded" in the build report (11 and 15 as printed exactly).
- Exit slips are placed at the end of Start here (the runner needs core before investigation); the Finish-page "Looking back" tick-box and the optional Python corner boxes are not questions and are not included.
- Goldbach / sum-of-two-primes questions ask for the smaller prime of each pair (a list is easy to mark).
- Decimal answer (L1 Think harder 4b): difference and rule are text items with several accepted wordings; the 100th term is a number item.
- Think harder = the first three stretch items plus the one moved from Start here, as printed; Go further = the last three challenge items.

Shared files touched (backward compatible): `test_holiday.py` now accepts text items with an `accept` list (no `rule`). Run the Level 1 test again before relying on it.

Open questions
- Should "explain" items be marked by a tutor once submit-to-tutor is live (they are self-check only now)?
- Palette figures (planning code) are drawn from the workbook blocks; the sb3 starter files are not linked from the page.

## Audit fixes (week 1)
L1 3(b2) no longer says that 101 is a term; "Take-home" removed from the screen text; the examples in T4(b) no longer equal the answers. L2 3(b) why no longer prints the answer; T1(a) and T1(b) hints no longer list the factor pairs.

# Level 6 online practice, holiday week 2 (lessons 3 and 4)

Build: `python3 practice/holiday/build_holiday.py p6 3` (and `4`); test: `python3 practice/holiday/test_holiday.py p6 3` (and `4`). dist is git-ignored; nothing is deployed, no Supabase change, nothing sent. Week 2 = lessons 3 and 4 (Thu 3 Dec and Sat 5 Dec, group L6A, from website/data/beta_schedule.json).
Sources: `p6/content/l3.js`, `l4.js` (the workbook is hand-written JS, so each question was extracted by hand into `p6/03/lesson.py`, `p6/04/lesson.py`) and `p6/content/gaps.json` (Investigation). New helper files (only for Level 6): `p6/w2lib.py` (figures and the block-program interpreter) and `p6/blocks_bridge2.js`. No shared file was edited.
Figures: the code blocks are drawn by the workbook's own `blocksSvg()` (through `blocks_bridge2.js`), and the SAME list of blocks is run by `w2lib.run`, so a picture and its checked answer cannot disagree. Number lines, tables, machines, the sea-level picture, the number-trick steps and the age bars are drawn as inline svg (the workbook draws its figures with the questions inside them; here the questions are text and only the figure is drawn). No coin or note images.
Checkers: every item has an independent checker (loops that run the machine on the numbers in the question, the interpreter for the code questions, and an evaluator that tests every accepted writing of an algebra rule for n = -6 to 30); the build fails if one differs from the printed answer.

| Lesson | Items | Auto-marked | Self-check (shown solution) | Paper-only (drawing) | Variant families |
|---|---|---|---|---|---|
| 3 Below Zero | 36 | 34 | 1 (temperature story) | 1 (Investigation: pairs on a number line, with a drawn solution) | 3 (168 combinations vs oracle) |
| 4 Algebra Machines | 41 | 36 | 5 (explanations, two-machines, Investigation) | 0 | 3 (910 combinations vs oracle) |

Unavailable (no item at all): none. Every Start here question (Q1 to Q7), the exit slip, the Investigation, the first four Think harder and the last three Go further questions are present. Scratch itself is never run in the page.

Not mirrored one-to-one, and why
- Written-answer boxes become typed answers: "Write the number at each letter", "Write < or >" (one choice item per gap), lists in order, the rule boxes "OUT = [ ] x n + [ ]" (type a minus sign for a take-away), "Check: ____" lines. Most items are therefore "reworded" in the build report.
- The "Check by going forwards" lines of L4 Q3(a)-(d) are not typed boxes: the check is in the worked solution (the question text says to check). L4 Q6(c) "Check by running the machine backwards" is two number boxes (96, 12).
- L3 Q2(a) is a choice among the five times; L3 Q6(b) asks for the number in "change floor by ( )" (-1); L3 Q6(c) is two boxes (floor, basement number) and says floor -1 is basement 1 (the print only says 0 = ground floor).
- L4 Q2(b) and Q7(b) steps 4 and 5: the algebra rule (for example (n + 3) x 4, 2n + 6) is a `text` item. Each accepted writing (with or without "OUT =", 4(n+3), (n+3)x4, 4n+12 ... ) is checked by evaluating it for n = -6 to 30 at build time, and about 70 right and wrong strings were run through `mark.js` (wrong ones such as 4n-12, n+3x4, (n+3)+4 are refused). Step 6 (the answer 3) is a number item. This is the one place where a typed rule is auto-marked.
- L4 Q5 (trace table) is two items (the values of n, then what the sprite says); Q7 (number trick) is shown as a six-step picture on each of its cards instead of repeating the riddle.
- The "Take-home" star on L4 Q7 is called "Bonus question" on screen. The optional Python corners (L3 Q7, L4 Q4) are not questions and are not included. Cutting and pasting the minus sign from the page is not needed: typing the keyboard minus sign is accepted everywhere.
- Think harder = the first four stretch questions as printed (no question was moved from Start here in these two lessons); Go further = the last three challenge questions.
- L3 Investigation (draw the pairs on a number line) is paper-only: a drawn number line with the arcs is shown after submit. L4 Investigation (find all the machines) has a text box and the table of machines as the solution; both are self-check.

Item rules from the week 1 audits were applied from the start: no card shows another card's answer (a later part's figure shows blanks, never the earlier part's filled plan; hints say how to find, not what); hints nudge; examples never equal an answer; explanations and "make up your own" are self-check; screen wording (no "circle", "cross out", "take-home"); the list answers are `set` items; minus signs are matched exactly; the two-or-three box answers keep the printed order.

Open questions
- Should the algebra-rule items (L4 Q2(b) P and Q, Q7(b) steps 4 and 5) stay auto-marked from the verified list of writings, or be self-check like other written rules?
- L4 Investigation and L3 Investigation could later be marked by a tutor once submit-to-tutor is live (they are self-check only now).
- The sb3 starter files are not linked from the page.

# Level 6 online practice, holiday week 3 (lessons 5 and 6)

Build: `python3 practice/holiday/build_holiday.py p6 5` (and `6`); test: `python3 practice/holiday/test_holiday.py p6 5` (and `6`). dist is git-ignored; nothing is deployed, no Supabase change, nothing sent. Week 3 = lessons 5 and 6 (Thu 10 Dec and Sat 12 Dec, group L6A, confirmed in website/data/beta_schedule.json).
Sources: `p6/content/l5.js`, `l6.js` (hand-written JS, so each question was extracted into `p6/05/lesson.py`, `p6/06/lesson.py`) and `p6/content/gaps.json` (Investigation). New Level 6 helpers only: `p6/w3lib.py`, `p6/blocks_bridge3.js`. No shared file was edited.
Figures: the code blocks, digit cards, street grid and spinner are drawn by the workbook's own `blocks()`, `cards()`, `grid()`, `spinner()` (through the bridge), and the SAME program list is run by the checkers. The difference table, empty sample-space tables, route counts, ways-to-pay table and winners grids are inline svg. No coin or note images.
Checkers (all independent): itertools/loops over the cases, a walk over every route on the grid, an interpreter for the nested block programs (with a per-say trace), and for the random programs the exact expected count found by listing every equally likely outcome (no simulation). The build fails if one differs from the printed answer.

| Lesson | Items | Auto-marked | Self-check (shown solution) | Paper-only | Variant families |
|---|---|---|---|---|---|
| 5 Every Possible Way | 38 | 34 | 4 (1 open: make up a puzzle) | 0 | 5 (76 combinations vs oracle) |
| 6 Fair or Unfair? | 41 | 34 | 7 (1 open: design a fair game) | 0 | 5 (164 combinations vs oracle) |

Unavailable (no item at all): none. Scratch is never run in the page.

Not mirrored one-to-one, and why
- Written-answer boxes become typed answers. L5 Q3 trace table = three cards (rows 1-2, 3-4, 5-6: a, b and what it says). L5 Q5 grid circles = three row cards plus (a) and (b); the print's star "Take-home" is called "Bonus question". L5 Q2(b) "write the multiplication" is a positional box item (choices per digit, then the total). L6 Q4 table = four row cards (rows 3 to 6; the filled cells are shown as printed).
- Fractions: two boxes "numerator / denominator" where the print says simplest form (L6 Q1, Q5, exit slip); a typed fraction (equal forms accepted, e.g. 4/10 for 2/5) where it does not. "Is it fair / is the code broken / do you agree" is a choice card plus a separate explain card (self-check).
- L5 Q6 gaps: the two repeats are boxes and the "if" test is a text item whose accepted writings (a<b, b>a, a>b ...) are all verified by running the program. The printed hint "when a is smaller than b" is moved to the hint line. The L6 plan has the same split (6, 6, a = b).
- L5 Investigation (find ALL the ways to pay 50 cents): first step, total (12) and with a 50-cent coin (13) are number items; the organised list and "how I made sure" is a self-check with the 12 ways drawn as a table. L6 Investigation: three game cards, "Is Ali right?", and a self-check for the fix; the physical coin tally of the first step is optional text (not checked).
- L6 empty 6 by 6 tables of Think harder 2 and Go further 6/7 are shown as empty tables (as printed) with a note to fill them on paper. The optional Python corners are not questions and are not included. L5 Q3 "In Scratch" run is traced, not run.
- Think harder = first three stretch questions plus the moved one (as printed, T4 (a) and (b)); Go further = last three challenge questions.
- Printed hints that gave an answer (L5 Q6 "a smaller than b", L6 Q1(d) "close to the expected number, not exactly") are not in the stem; the hints nudge instead.

Audit rules applied from the start: no stem, hint, frame or figure shows another card's answer (later parts show gaps, never earlier filled plans or tables); examples never equal an answer (the "join" example is 75, the rule examples are different tests); explanations and make-up-your-own are self-check / open; every list answer is a set (the 9 two-digit numbers are ordered); minus signs not needed here; frames use label + box groups; explanations marked `self`.

Open questions
- Should "is it fair / is the code broken" choice cards stay auto-marked (they are checked by exact fractions or a standard-deviation test) or be self-check with their explanation?
- L6 Go further 7 and L5/L6 Investigations could later be tutor-marked once submit-to-tutor is live.
- The sb3 starter files (L5_Every_Order, L6_Chance_Lab) are not linked from the page.

# Level 6 online practice, holiday week 4 (lessons 7 and 8)

Build: `python3 practice/holiday/build_holiday.py p6 7` (and `8`); test: `python3 practice/holiday/test_holiday.py p6 7` (and `8`), both RESULT: OK. dist is git-ignored; nothing is deployed, no Supabase change, nothing sent. Week 4 = lessons 7 and 8 (Thu 17 Dec and Sat 19 Dec, group L6A, confirmed in website/data/beta_schedule.json).
Sources: `p6/content/l7.js`, `l8.js` (hand-written JS, so each question was extracted into `p6/07/lesson.py`, `p6/08/lesson.py`) and `p6/content/gaps.json` (Investigation). New Level 6 helpers only: `p6/w4lib.py`, `p6/blocks_bridge4.js`. No shared file was edited.
Figures: L7 code blocks and the corner picture are drawn by the workbook's own `blocks()` and `cornerFig()` (through the bridge); the program lists drawn are the printed ones (every block text is asserted to be in l7.js) and the checkers read the numbers from the same lists. L7 star dots, L8 letter-number strip (two rows of 13 so it is readable on a phone), clock and week circles, the clock jumps and the tables are inline svg. The L8 code machine (three blocks) is redrawn with the same blocks and colours broken into rows so the text stays readable at 390 px (its three block texts are asserted to be in l8.js). No coin or note images.
Checkers (all independent): a small turtle that walks the program (corners visited, total turning, home or not), the angle sum (n - 2) x 180 / n for regular polygons (so 360 / n is never used to check itself), brute force over the number of sides, a Caesar coder that moves letters along the alphabet, the code machine run on a list with item 1 = A, clock and week answers by counting on one step at a time, remainders by taking the divisor away again and again, every shift tried for the cracks. The build fails if one differs from the printed answer.

| Lesson | Items | Auto-marked | Self-check (shown solution) | Paper-only (drawing) | Open (no objective fact) | Variant families |
|---|---|---|---|---|---|---|
| 7 Turtle Geometry | 45 | 38 | 6 | 1 (draw the 9-point star, with the drawn star shown) | 1 (design your own star) | 5 (119 combinations vs oracle) |
| 8 Secret Codes | 40 | 35 | 4 | 0 | 1 (write your own coded message) | 4 (208 combinations vs oracle) |

Unavailable (no item at all): none. Scratch is never run in the page.

Not mirrored one-to-one, and why
- L7 "Try it first" (quarter turns, degrees altogether) = two number cards. Q1 table = five row cards (9, 10, 36 sides; turn 24; inside 165), each with the "sides x turn" box as printed; the printed first row (3 sides, with its 360) is not shown in the stems so no card shows another's answer. Q1(a) "what do you notice" and Q1(b) "is Mei right" are a choice card plus a separate explain card (self-check). The print's "Test two rows in Scratch" is not a question.
- L7 Q2: the blank "draw your prediction" frame becomes a choice (what does it draw) plus an explain card; "Fix it: change ___ to ___" is two boxes. Q3: the trace table is two row cards (rows 4 to 6, rows 7 to 9; rows 1 to 3 are given in the stem as printed) and then (a) to (d). Q4: the star table row is one fields card; the "draw your star" part is a paper-only card with the correct drawing. Q5 (print: Take-home star, shown as "Bonus question"): each inside angle (five boxes), all added (five boxes), the 180, and the rule (type just the rule, for example (n - 2) x 180; the runner accepts equal polynomials but not a leading "total ="; the stem says so).
- L7 Investigation: the first step plus one card per turn t = 40, 72, 100, 120, 144, 150 (repeats and times round, two boxes), then a self-check card for what changes and what stays the same, with the whole table drawn in the solution. The row for t = 90 is the first-step card.
- L7 Go further C2 (three regular polygons round a point): printed answer is "one other set"; many sets are right (computed: 9 other sets of three polygons, any order), so it is a text card of sides, all of them accepted. C1 (design a star) is open. C3 is a choice (which turn draws a hexagon) plus an explain card.
- L8 Q1 (a), (b), (c) number cards; (d), (e) weekday choices. Q2 (a), (b) are text cards (typed coded or decoded words, spaces and case do not matter). Q3: three row cards (n, n + 5, m for W, A, Y) and the program says (text BFD); the printed "code letter" column is not a separate box (the letters are in the answer to (a)). Q4 (a) is two cards (the repeated word, then the English word), (b) is "what shift turns T into B" worded without the words THE or BPM so no card gives another's answer. Q5 (print: Take-home star, shown as "Bonus question"): (a) (b) number, (c) choice plus explain, (d) number.
- L8 Investigation: first step (C with shift 8, then 18), CAT with shift 8 (KIB), CAT with 8 then 18, two other shifts that add to 26 (always CAT), "is it always true" (choice) with an explain card, and "find ALL shifts that are their own decoder" (a list, answer 13). Think harder T4 (moved) is two cards (the three mods, then decode the whole message). Go further: C1 own message (open), C2 (21), C3 clock jumps of 5 and of 4 (two choices) plus an explain card.
- The optional Python corners (L7 and L8) and the "Looking back" tick-box are not questions and are not included. The L7 and L8 sb3 starter files are not linked from the page.
- Think harder = the first three stretch questions plus the one moved from Start here (L7: 20-point star as two cards; L8: mod sums and the whole message); Go further = the last three challenge questions, as printed.

Audit rules applied from the start: no stem, hint, example or figure shows another card's answer (the L7 Scratch step sizes, the first printed row and the L8 repeated word are kept out of other cards); hints nudge; explain cards ask for what the child notices (neutral stems); every solution statement was recomputed (for example "in this table the turns that divide 360 are 40, 72, 90 and 120" instead of a general rule that fails for turns such as 240); text answers with several valid forms accept the computed set; the list answers are `set` items; minus signs are real minus signs in worked steps; code is drawn as blocks only and nothing asks the child to run code.

Open questions
- Should the algebra-rule item L7 5(b) accept "total = (n - 2) x 180"? The shared runner ignores only the word OUT before "=", so "total =" is marked wrong (the stem asks for the rule alone).
- Should the explain items (L7 1(a), 1(b), 2(a), Inv notice, C3(b); L8 5(c), Exit (b), Inv (a), C3(c)) be marked by a tutor once submit-to-tutor is live? They are self-check now.
- L7 C2 accepts every computed set of three polygons (typed as sides). If the owner wants only the printed two sets (4, 8, 8 and 3, 12, 12) it is a one-line change.

# Level 6 online practice, holiday week 5 (lessons 9 and 10)

Build: `python3 practice/holiday/build_holiday.py p6 9` (and `10`); test: `python3 practice/holiday/test_holiday.py p6 9` (and `10`). dist is git-ignored; nothing is deployed, no Supabase change, nothing sent. Week 5 = lessons 9 and 10 (Thu 24 Dec and Sat 26 Dec, group L6A, confirmed in website/data/beta_schedule.json).
Sources: `p6/content/l9.js`, `l10.js` (hand-written JS, so each question was extracted into `p6/09/lesson.py`, `p6/10/lesson.py`) and `p6/content/gaps.json` (Investigation). New Level 6 helpers only: `p6/w5lib.py`, `p6/blocks_bridge5.js`. No shared file was edited.
Figures: code blocks, hexagon chains and both dot plots are drawn by the workbook's own `blocks()`, `hexChains()` and `FG.dotPlot()` (through the bridge); the same program list is drawn and run by `w5lib.run`. Spinner table, empty tables and the worked-example programs are svg. No coin or note images.
Checkers (all independent): exact means with Fractions, median by sorting, mode by counting, missing values by searching, the block-program interpreter, brute force for primes/factors/sequences, clock by counting on, regular polygon by (n - 2) x 180 / n, probabilities by listing every equally likely outcome, and a search over all lists of five numbers that proves the Go further 'mean mystery' example is unique.

| Lesson | Items | Auto-marked | Self-check (shown solution, paper-only included) | of which paper-only | Open (no objective fact) | Variant families |
|---|---|---|---|---|---|---|
| 9 Data Detectives | 59 | 52 | 6 (5 compare + C2b) | 1 (C2b plan a program, correct blocks shown; counted inside the 6) | 1 (C1 mean mystery) | 7 (672 combinations vs oracle) |
| 10 Showcase Challenge | 37 | 29 | 4 (2 compare + 6a + C2b) | 2 (6a blocks plan, C2b spinner program; counted inside the 4) | 4 (Q5 plan, 6b tests, Exit slip, C1) | 10 (223 combinations vs oracle) |

Auto + self-check + open = items (59 and 37); the paper-only items are already inside self-check, so they are not added again. Unavailable (no item at all): none. Scratch is never run in the page.

Not mirrored one-to-one, and why
- L9 Q1(c) is a five-box card; the plus sign is not accepted by the shared matcher ('+1' is wrong), so the stem says to type just the number for above and a minus sign for below. L9 Q3 is a predict (choice) plus a new-mean (number) card for each of (a) to (d). Q4(e) is a fairness choice, a mean-or-median choice and an explain card; the print's "$22" is not repeated in the stem so no card shows 4(a)'s answer. Q5 trace table = four row cards (i at the start, item i, total at the end), then (a), the two-blocks choice and the new answer. Q6 (print: Take-home star, shown as "Bonus question"): mean, days hotter, the two blanks (choices) and what it says.
- L9 Investigation: first step (mean), then mean / median / mode cards for the original and for the 14 changed to 24, to 4 and to 7 (the mean of the last, 6.6, is a text answer, type a decimal), a self-check "what changes, what stays the same" and "change TWO numbers and keep the mean" (self-check, total must stay 40). Think harder = the first four stretch questions (T3 write five numbers with mean 6 and mode 4 is self-check with a worked example); Go further = the last three (C1 open, C2 explain plus a paper-only program plan, C3 two number cards).
- L10 Q1: sticks for 10 hexagons, the rule (text, any equal algebra writing, "sticks =" label accepted), 101 sticks, then what the code says and which chain it checks. Q2 (Take-home, "Bonus question"): 49, the primes of 84 (comma list), and the smaller prime of each way to make 40 (list; the stem does not say how many). Q3 four number cards. Q4: n = 9 and OUT 58 (two cards), factors of 91 and prime? (two cards), and about how many 8s (choice among five, plus an explain card). The print says "do the part for your starter"; all three are online.
- L10 Q5 (plan table), Q6 (blocks plan, test table) and the exit slip are the showcase project and have no single answer: Q5, Q6 tests and the exit slip are open; Q6 blocks is paper-only. Each shows a worked example (Starter A with the rule changed to x 5 then - 2, 8 blocks, three tests with hand-worked results), all computed. The "ready to show?" tick-box and the optional Python corner are not questions and are not included.
- L10 Think harder: T1 to T3 and the moved digit-cards question (how many numbers, how many even, probability 1/3 as three cards). Go further: C1 (open), the spinner (probability 1/8 plus a paper-only program plan) and 6n - 1 (is 2027 in it: Yes; first term bigger: 2033). The model's "338th term" is in the solution of C3(a).
- Hints and examples follow the audits: no card reveals another card's answer; hints nudge; explain cards are neutral; every claim in a solution was recomputed.

Open questions
- The shared matcher does not read '+1' (a leading plus sign) as 1; L9 1(c) works around it in the stem. Should '+N' be accepted for number boxes?
- Should L9 Investigation (a)/(b), T3, C2(a) and the L10 open planning items be marked by a tutor once submit-to-tutor is live (self-check or open now)?
- The L10 'about 139' item is a five-way choice because a typed estimate (139, 140, 138.9) cannot be marked fairly; confirm.
- The sb3 starter files for the L10 starters are not linked from the page.

Week 5 audit fixes: L9 intro and hint no longer state 'total = mean x how many'; L10 2(a) hint softened; L10 C2(a) says the table shows the layout only (work on paper).
