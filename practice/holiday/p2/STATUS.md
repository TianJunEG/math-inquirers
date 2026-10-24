# Level 2 (P2, ages 7 to 9) holiday online practice, week 1 (lessons 1 and 2)

Built 24 Oct 2026. Not deployed, nothing sent, no website/dist or Supabase change. Week 1 = lessons 1 and 2 (`website/data/beta_schedule.json`, Level 2 groups: lesson 1 Tue 24 Nov, lesson 2 Fri 27 Nov).

Build and test (shared scripts, nothing in them changed):

    python3 practice/holiday/build_holiday.py p2 1      # -> practice/holiday/p2/01/dist/   (git-ignored)
    python3 practice/holiday/build_holiday.py p2 2
    python3 practice/holiday/test_holiday.py p2 1       # browser test + screenshots into p2/01/proof/
    python3 practice/holiday/test_holiday.py p2 2

Sources of the questions (the printed workbook is hand-written code, not data, so each question was extracted from the workbook source into a structured item
with an independent checker; the build stops unless every printed fragment is found in the source and every checker equals the printed answer):
`p2/content/l1.js` and `l2.js` (`workbook()` = Start here; `qbank.stretch` first four = Think harder 1 to 4; `qbank.challenge` last three = Go further 5 to 7, exactly as
`p2/workbook_html.js` prints them), `p2/gaps.json` (Investigation), `p2/workbook_html.js` (the "Make up your own" line). Figures: the printed ones from
`p2/workbook_body.html` (digit cards, 1000-chart pieces, missing-digit columns, magic square, bar model), magic triangles from `hlib.magic_triangle`,
the ten-blocks picture of Think harder 3 redrawn for a phone (the printed one is too small at 390 px).

## Items

| | Lesson 1 Digit detectives | Lesson 2 Missing digit mysteries |
|---|---|---|
| Items | 39 | 41 |
| Start here | 21 | 22 |
| Investigation | 4 | 5 |
| Think harder | 8 | 10 |
| Go further (and Make up your own) | 6 | 4 |
| Auto-marked (number, fields, set, choice) | 31 | 31 |
| Self-check, typed or spoken explanation (never auto-marked) | 8 | 8 |
| Paper-only self-check (drawing, with a figure of the correct drawing) | 0 | 2 (5(b) fill the second triangle, Think harder 1 draw the triangle) |
| Unavailable online | 0 | 0 |
| Variant families ("Try a similar one", every combination run against an independent oracle) | 6 (1a, 1b, 4b, 5a, 5b, 5d: 1,675 combinations) | 6 (1a, 2a, 3a, 3b, 3c, 6: 1,332 combinations) |

Every item has a hint, worked steps and a skill tag. The printed multi-part questions are split into one card per part; a printed "explain" or "how do you know" line is
a separate self-check card (the example reasoning is shown after submit, never marked).

## Not mirrored exactly, and why

- Printed table "Start with 2 / Start with 4 / Start with 7" (L1 Q2a) and the free list lines are one typed list ("247, 274, ...", any order accepted). The child still needs the three starting cards to find them.
- L1 Q4 and L2 Q1, Q2, Q4, Q5: the printed boxes in the pictures are typed in numbered boxes inside a sentence that names the position ("Top row: 347, [ ], [ ]"), with the printed picture above.
- L2 Q5(a) "fill in all the circles" and Q5(b) "fill in the second triangle": 5(a) is typed (corner, right side, bottom). 5(b) has many right drawings (a triangle can be turned or flipped), so it is a paper self-check with one correct drawing shown; the corner numbers are auto-marked separately.
- L2 Go further 5 (find ALL the ways): the child types the first number of each way (507, 517, ... 597), because the second number is then fixed; the full pairs are in the worked solution.
- L2 Q6: the printed "Draw a model" lines and the "Answer ____ and ____" line become one typed list of two numbers (the printed bar model is shown with the question).
- Printed "take-home" star marks are not shown on screen (they are a printing-order cue only).
- Investigation (L1 "Mirror numbers", L2 "Odd or even?") has an "easy first step" in the printed page; it is kept inside the first Investigation card.
- Strategy card, "Tool of the day", "Looking back" and the name/date line are print-only and are not online items.
- No items use coin or note pictures; every figure is drawn.

## Open questions for the owner

1. L1 1(b) (6 hundreds, 15 tens and 2 ones) is 752. The printed workbook has no answer line for Start here, so the independent checker is the only source; worth a glance when the printed answer key is cross-checked.
2. Free typing of explanations: should a tutor see the typed self-check text in the submission (the shared runner stores it), or only the marks? (Decision SUBMIT-TO-TUTOR says answers go to the tutor; this is just a reminder that explanations are included.)
3. Second Think harder / Go further items in `qbank` that are not printed in the workbook (Think harder 5 to 8, Go further 1 to 6 of the bank) are not online: the brief mirrors the printed pages only. They could be added as optional extras if wanted.

## Week 1 audit fixes (items, 24 Oct 2026; see AUDIT_WEEK1_L1_3.md)
- M2 L2 5(a) circles no longer says "160 is between them" (uses "your answer to 5(a) between"); L2 4(b) and 4(d) hints no longer state the total 150.
- M3 L2 5(a) circles hint (false rule "the corner is the smallest") replaced by a test-it hint; L2 5(b) and Think harder 1 hints no longer say "the biggest numbers go in the corners"; L2 4(a) hint no longer names the diagonal; L1 Investigation 4 and Think harder 4 hints no longer give the counter-example.
- Wording: "Write them in the boxes" is now "Type each one in its box"; L1 2(a) says "Type every number".
