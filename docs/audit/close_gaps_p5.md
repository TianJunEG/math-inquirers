# Close three gifted-style gaps: P5

Date: 2026-10-22. Not committed. Only P5 files were changed (no levels/*, rebuild/slidekit.py, hp/*).

## What was added to every lesson (L1 to L10)
1. **Warm-up check (pre-check / skip-ahead).** Two new-setting questions on the key idea (not recall), 3 minutes at the start. In the deck (new slide `p5lK-check`, after the title, answers click in, full answers and listening points in notes), in the tutor guide (new 2 to 5 min segment with a question/listen-for table and 2 script lines), and a printed "Fast track" note under each lesson header on workbook page 1. The script says how to run it: whiteboards, one child explains, never record scores; a child right on both and able to say why goes to the Think Harder pages and the Open Investigation while the group works page 1; online groups of up to 8: send page numbers in the chat or use a breakout room, the child rejoins for talk time; offered to the whole group as a choice, nobody labelled, anyone can swap. The warm-up game and quick questions were shortened to minutes 3 to 9 (1 or 2 rounds) to make room.
2. **Open investigation.** One new task per lesson on a new final workbook page ("Open investigation", 3 parts, 7 answer lines) with a tutor model answer and what to look for in the guide (table "Open investigation"). Types: L1 What if we change the target? L2 Is it always true (difference of neighbouring unit fractions)? L3 What if we change the total? L4 Find all (right-angled triangles of area 6 cm2, then the top corner line, then other areas). L5 Find all (boxes of 48 cubes, then 64). L6 Find all (taps used one at a time for 24 litres, then 25). L7 Is it always true (order of two discounts, and 20% then 10% is not 30%)? L8 Find all (isosceles triangles with angles in tens of degrees, then multiples of 15). L9 Is it always true (sum of the first n odd numbers is n squared, then even numbers). L10 Find the pattern (1 or 2 steps staircase, Fibonacci, then 3 steps).
3. **Reflection "What was hard?".** On the last workbook page of each lesson: "The hardest part was ...", "I got unstuck by ..." (five drawn tick boxes plus a line), "Next time I will try ...". One closing slide (`p5lK-reflect`, last in the deck, after the exit ticket) and 2 tutor-script lines in the closing segment (1 minute, share one or two, never grade, praise strategy not speed). A short explainer of all three features was added to the "How to use the scripts" part of the guide.

Source of the new text: `p5/content/gaps.js` (merged by `p5/data.js`). Slides: `rebuild/p5_gaps.py`, called at the end of each `rebuild/gen_p5lK.py`. Workbook and guide: `p5/workbook_html.js`, `p5/guide.js`.

## Page counts (before, after)
| File | Before | After |
|---|---|---|
| Student workbook | 47 | 57 (+1 per lesson: the Open Investigation + reflection page. It could not fit on the full Think Harder pages; the Fast track note fits on existing page 1) |
| Tutor guide | 69 | 81 (checks, investigation tables, scripts) |
| Weekly dose | 26 | 26 |
Decks: each lesson +2 slides (L1 28, L2 27, L3 26, L4 27, L5 27, L6 27, L7 28, L8 28, L9 28, L10 29).

## Verification (Python brute force, exact arithmetic)
L1: cards 3, 6, 7, 9 closest to 7000 is 6973 (27 away; 7369 is 369); one pair of brackets in 4 + 6 x 5 - 3 gives only 16, 31 or 47; cards 0,1,2,4,5,7,8: winners 3M 2 875 410 below, 4M 4 012 578 above, 5M 5 012 478 above, 6M 5 874 210 below, 7M 7 012 458, 8M 8 012 457 (all permutations searched). L2: 1/n - 1/(n+1) = 1/(n(n+1)) for n up to 1999; 1/6+1/12+1/20 = 3/10. L3: totals 1 to 100, "exactly twice" is possible only when 3 divides the total; 48/12 gives 8. L4: pairs with product 12, 20, 24: 3, 3, 4 triangles (6, 10, 12 cm2). L5: boxes with whole-number edges: 48 gives 9, 64 gives 7. L6: 24 litres gives 5 ways, 25 litres gives 4 ways. L7: for every pair of whole-number discounts 1% to 99% the order does not matter, and a% then b% never equals (a+b)% off. L8: eight isosceles triangles with angles in tens of degrees, five with multiples of 15. L9: sum of first n odd numbers = n squared and first n even = n(n+1) for n up to 2999. L10: staircase ways 1, 2, 3, 5, 8, 13, 21, 34 (recursive count); with 3-steps 3 steps gives 4 and 4 steps gives 7. Check answers worked by hand and re-run: L5 20 litres and 5 cm rise; L6 15 minutes and Mei faster (1.25 vs 1.2); L7 $48.60 and 26; L9 39 and figure 25; L10 $24 and 8 squares.

## Slide overflow
All 10 decks previewed. Two existing slides had small overflows before this work (p5l1-explore1 by 7 px, p5l4-explore1 by 1 px); fixed by reducing the step text from 34 to 32 px in gen_p5l1.py and gen_p5l4.py. No overflow now. New slides end above y 920.

## No unicode box or shape glyphs (coordinator rule)
Grepped the P5 content, generators and builders: no existing instances, nothing replaced. New tick boxes in the workbook and on the reflection slide are drawn bordered shapes, not glyphs. No missing-digit puzzles were added, so column_png was not needed. The new check questions are text only; no drawn diagrams were added to the check slides (the L4, L9 and L10 check questions describe a rectangle, a dot pattern and a grid in words), which is a known small gap.

## Rebuilt
`rebuild/gen_p5l1..10.py`, `levels/restyle.py split/p5lK` for each, `bash levels/build_level.sh 5`, `python3 levels/mkextras.py 5` (self-check OK).
