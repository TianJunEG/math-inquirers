# Level 5 (key p5, ages 10 to 12) online holiday practice: week 4 (lessons 7 and 8)

Built and tested, not deployed (dist is git-ignored). Build: `python3 practice/holiday/build_holiday.py p5 7` (and `p5 8`); test: `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 practice/holiday/test_holiday.py p5 7` (and `p5 8`). Both end RESULT: OK.
Sources: `p5/07/lesson.py`, `p5/08/lesson.py` (items, independent checkers, variants) and `p5/p5fig4.py` (figures, new for this week: price tags, bar models, class table, and every angle figure; with a check of every printed angle). Week 1 to 3 notes: STATUS.md, STATUS_WEEK2.md, STATUS_WEEK3.md. No shared file and no `p5lib.py` change.
Week 4 = L5 lessons 7 and 8 (website/data/beta_schedule.json, group L5A: sessions 7 and 8 = Fri 18 and Sun 20 Dec): lesson 7 "Percentage Puzzles" (Percentage), lesson 8 "Angle Chasers" (Angles, triangles and quadrilaterals).

| | Lesson 7 | Lesson 8 |
|---|---|---|
| items | 53 | 40 |
| auto-marked | 43 | 29 |
| self-check (compare with model answer) | 8 (all with a checked fact) | 10 (all with a checked fact) |
| open (make up your own, no objective fact) | 2 (the "test two pairs of your own" and the make-up prompt) | 1 (make-up prompt) |
| paper-only (drawing) | 0 | 0 |
| unavailable (not mirrored) | 0 whole questions | 0 whole questions |
| variant families (all combinations equal an oracle) | 10 (119 combinations) | 11 (79 combinations) |
| question text as printed / reworded | 12 / 41 | 10 / 30 |

Item types, L7: fields 21, number 8, text 6 (decimal money), choice 8, self-check 10. L8: fields 12, number 12, choice 5, self-check 11.

Mirrors the printed workbook (p5/workbook_html.js): Start here Q1 to Q5 (p5/content/l7.js and l8.js, workbook()), the Investigation (p5/content/inv.js), Think harder A1 to A4 (first four `qbank.stretch`), Go further B1 to B3 (last three `qbank.challenge`) and the "Make up your own" prompt (gaps.js), in printed order. Every printed sentence used is checked to occur in those source files (the build stops otherwise).
Every auto item has an independent checker. L7: a percentage is built by adding 1% over and over, rises, cuts and discounts are applied step by step with exact fractions, a missing whole (the money Mrs Tan had, the price before GST) is found by a search, and the order of two discounts is tried for every pair of whole-number percentages from 1% to 99%. L8: every figure is rebuilt from coordinates (crossing lines, four rays round a point, parallelogram, rhombus, trapezium, the triangle with AB = AD, the parallelogram with E on DC, the square with an equilateral triangle outside and inside, the isosceles triangle with BD = BC) from the GIVEN facts only, and the unknown angles are measured with atan2; the isosceles triangles (one given angle, 30 degrees apart, all angles multiples of 10 or 15 degrees) are found by searching every base angle on a half-degree grid. The printed answer must equal the checker or the build stops. Answers also agree with the printed keys in l7.js and l8.js.

## Not mirrored exactly, and why
Lesson 7
- Q1 table is four cards (10% and 5%; 1%; 15% and 35%; 99%) because the 1% and 99% boxes are decimals ($2.40, $237.60: typed text with a generated list of accepted writings). 1(a) "how did you find 35%" and 1(b) "a quick way to find 99%" are self-checks.
- Q2: (d) is two cards (which shop; how many cents cheaper, typed in cents so that no decimal is needed). Q3(c) is a choice (is Siti right) plus a self-check that explains. Q4(d) is the percentage that is really left (number) plus a self-check that explains. Q5 table is three cards (the start-here 10% and 60%; the pupils row; the glasses row) and (a) the percentage of the class (the stem gives the story only, not the 14).
- Investigation: the easy first step, (a) both prices, "is one cheaper" as a three-way choice, (b) the two example pairs from the print (50% and 10%, 30% and 20%) as two auto cards, an open self-check for the child's own pairs, a choice "does the order ever change the price" and a self-check that explains, (c) the 30% off price, a choice and a self-check that explains.
- Think harder A2(a) is three cards (pays at each shop, which is the better buy, by how much) and A2(b) a fourth; A3 is the method (self-check) plus 15% of $46 (typed money). Go further B1 is a choice (is Ali right) plus the GST, B2 a choice plus the saving.
- The % sign is not read inside a number box by the shared matcher, so the frames print the % after the box and say "Type just the number".
- "Swap with a partner" is dropped from the make-up prompt (a screen has no partner). Take-home stars are not shown (everything is available online).
Lesson 8
- Every figure is redrawn as inline SVG, one figure per shape (the printed page has the parallelogram, rhombus and trapezium in one row; Q1 has two panels: the crossing lines for (a) to (c), the four angles at a point for (d)); drawings are labelled "not to scale" as in print. No figure shows an unknown angle; the solution pictures write the checked angles on the same drawing.
- Q1 (a) to (c) are one card of three boxes (BOC, BOD, AOD in the printed order); (d) is the missing angle plus a choice for the angle fact.
- Q2 "write each angle fact you use" is one self-check; Q3 "worked start" is in each stem as printed; the blanks "because the three angles of triangle ___ add up to ___" are a choice of triangle (the 180 is in the worked solution), "write each reason in words" is a self-check; Q4 "because opposite angles are ___" and "triangle DAE is ___" are choices.
- Q5(a) "find every case": the self-check list keeps the full task. Two auto cards then ask for the case where 50 is a base angle and the case where it is the top angle (these name the two cases, so a child who opens them first is told how to look). Q5(b) is a count (1) plus a self-check "how do you know".
- Investigation: (a) is a self-check list plus a count (8); (b) is a count of triangles with an angle over 90 and a choice of the equilateral; (c) is a count for multiples of 15 plus a self-check "what stays the same". Think harder A1 to A3 have a self-check for the printed "give your reason" or "write the reason for each step" (A2: "why only one answer"). Go further B3 is a self-check list plus a count (2).
- Paper-only items: none. The week 4 Level 5 workbook has no ruler, kit or drawing task.
- A calculator is not needed. The page has none; a phone calculator is fine in lesson 7.

## Audited mistakes avoided from the start (week 1 to 3 audits)
No stem, hint, example or solution figure shows another card's answer (checked by a search of every answer against every other card's question, hint, frame and figure text: only numbers given in the problems repeat; one leak found and fixed: the Q5(a) stem used to say "14 of them wear glasses"). Explain cards have neutral stems ("Explain what you notice about..."), and stems of later parts never state what an earlier part found. Examples are never answers. Hints nudge and none states a rule that is only true for one case. The position or pairing a printed question tests is kept (BOC, BOD, AOD; Girls, Boys, Whole class). Long stories are not repeated (the Q3 triangle is one sentence with a figure). Wording for screens ("type", no "circle"). Every list answer is a self-check list plus a count; every explanation is a self-check, not typed text; labels are explicit, short, unique and number-first. Variant figures: every variant that changes an angle brings its own picture (cross, four angles at a point, the parallelogram with E, the isosceles triangle, the A1 parallelogram label). Solution texts are true for every case they name (the "the base angle is never over 90" and "two angles of 110 add to 220" claims were recomputed by search).

## Open questions
- "60%" typed in a number box is not read by the shared matcher (the box prints the % after it and the stem says "Type just the number"); tell me if the % sign should be accepted.
- The count cards (lesson 8 Investigation (a): 8; B3: 2; lesson 7: none) tell the child how many to look for; the list card next to them is neutral. Is that enough auto-marking for the "find all the ways" skill?
- L8 Q5(a): the "base angle" and "top angle" cards name the cases that the print leaves the child to find.
- Nothing here has been seen by a child. Difficulty and timing are untested. Lesson 7 has 53 questions (the printed workbook has many parts), which is the longest Level 5 lesson so far.

No shared file was changed.
