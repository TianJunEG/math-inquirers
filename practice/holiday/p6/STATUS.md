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
