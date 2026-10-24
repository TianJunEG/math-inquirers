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
