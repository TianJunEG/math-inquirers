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
