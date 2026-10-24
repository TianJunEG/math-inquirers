# Level 5 (key p5, ages 10 to 12) online holiday practice: week 2 (lessons 3 and 4)

Built and tested, not deployed (dist is git-ignored). Build: `python3 practice/holiday/build_holiday.py p5 3` (and `p5 4`); test: `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 practice/holiday/test_holiday.py p5 3` (and `p5 4`). Both end RESULT: OK.
Sources: `p5/03/lesson.py`, `p5/04/lesson.py` (items, independent checkers, variants), `p5/p5fig2.py` (figures drawn from cm coordinates and bar models). Week 1 notes are in STATUS.md.
Week 2 = L5 lessons 3 and 4 (website/data/beta_schedule.json: L5A sessions 3 and 4, 4 and 6 Dec): lesson 3 "Before and After" (Fraction Word Problems), lesson 4 "Triangle Areas" (Area of Triangle).

| | Lesson 3 | Lesson 4 |
|---|---|---|
| items | 30 | 35 |
| auto-marked | 26 | 28 |
| self-check (compare with model answer) | 4 (3 with a checked fact, 1 open) | 6 (5 with a checked fact, 1 open) |
| paper-only (drawing) | 0 | 1 (Investigation C(b): mark the top corner; correct picture shown after Submit) |
| unavailable | 0 | 0 |
| variant families (all combinations equal an oracle) | 4 (54 combinations) | 4 (76 combinations) |
| question text as printed / reworded | 24 / 6 | 19 / 16 |

Mirrors the printed workbook (p5/workbook_html.js): Start here Q1 to Q5, Investigation, Think harder A1 to A4, Go further B1 to B3, "Make up your own", in printed order. Every printed sentence used is checked to occur in the source files. Every auto item has an independent checker (search over the story numbers with exact fractions, forward simulation, shoelace formula on the figure's corner coordinates, whole-number pair search); the build stops if it differs from the printed answer. Answers agree with the printed keys in p5/content/l3.js and l4.js.

## Not mirrored exactly, and why
- Split cards (so that any card can be opened first and no card shows another's answer): L3 1(b) = choice (too much or too little) plus the amount; the printed "not $30" is not shown because it is the answer of 1(a). L3 3(a) = two boxes, a choice and an explain self-check. L3 4(a) is one choice that pairs which quantity stays the same with its value ("The difference: $24" or "The total: $76"). L3 5(b) = three cards. L3 4 "Start here" (gift of $10) is its own two cards. L4 1(a) merges the printed "half of __ = __ cm²" scaffold with the area box so the answer is not repeated. L4 Investigation (b) = a paper task (mark the corners), a number (how high) and a "what do you notice" self-check; (c) = two numbers and a choice.
- L4 Investigation (a) is typed as the short sides of each triangle, smaller number first, triangles in order (an ordered list, so the pairing is checked); the count is not told. Easy first step answer (6) is stated in (a) by the printed question itself.
- L4 5(c) "one more triangle with the same area" has many right answers, so it is a self-check (the model answer lists the pairs, base x height = 48). L3 Investigation (c) rule and all "explain" parts are self-checks.
- Take-home stars are not shown (everything is available online). Printed "draw the bars" lines are optional aids; figures are redrawn as inline SVG (Q1 triangles one per card at a readable size, bar models, to scale from cm coordinates). Question figures never show an answer; solution pictures (Ravi's bar, swap before/after, Monday/Tuesday units, the L4 corner line, the L4 white triangles) are built from the checked values.
- L3 Think harder A2 and L4 4(b) use labelled boxes (no order rule needed). Frames put units before the box ("EBF (cm²): [ ]") so a label never separates from its box on a phone.
- A phone calculator is fine; the page has none. Typed units (cm, cm², $) after a number are accepted by the shared runner.

## Open questions
- L4 4(b): the printed example "ADE = 16 cm²" equals the answer for EBF (a coincidence in the workbook numbers); the other box must also be right, so it cannot be copied alone.
- L4 Investigation (a): is the "smaller number first, in order" typing rule too fiddly on a phone? (Alternative: a self-check.)
- Nothing here has been seen by a child. Difficulty and timing are untested.

No shared file was changed.
