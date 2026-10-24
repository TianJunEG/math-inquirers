# Level 5 (key p5, ages 10 to 12) online holiday practice: week 3 (lessons 5 and 6)

Built and tested, not deployed (dist is git-ignored). Build: `python3 practice/holiday/build_holiday.py p5 5` (and `p5 6`); test: `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 practice/holiday/test_holiday.py p5 5` (and `p5 6`). Both end RESULT: OK.
Sources: `p5/05/lesson.py`, `p5/06/lesson.py` (items, independent checkers, variants) and `p5/p5fig3.py` (figures, new for this week: oblique solids, tanks, rate table, shop boards, time line; and `dec_accepts` for decimal answers). Week 1 and 2 notes: STATUS.md, STATUS_WEEK2.md. No shared file and no `p5lib.py` change.
Week 3 = L5 lessons 5 and 6 (website/data/beta_schedule.json, group L5A: sessions 5 and 6 = Fri 11 and Sun 13 Dec): lesson 5 "Volume Vault" (Volume), lesson 6 "Rate Racers" (Rate).

| | Lesson 5 | Lesson 6 |
|---|---|---|
| items | 36 | 34 |
| auto-marked | 30 | 30 |
| self-check (compare with model answer) | 6 (4 with a checked fact, 2 open: "which box would you choose" and make up your own) | 4 (3 with a checked fact, 1 open: make up your own) |
| paper-only (drawing) | 0 | 0 |
| unavailable (not mirrored) | 0 whole questions | 0 whole questions |
| variant families (all combinations equal an oracle) | 10 (274 combinations) | 10 (114 combinations) |
| question text as printed / reworded | 19 / 17 | 18 / 16 |

Item types, L5: number 20, fields 6, set 2, text 1 (a decimal), choice 1, self-check 6. L6: number 15, fields 9, text 4 (a time and three money answers), choice 2, self-check 4.

Mirrors the printed workbook (p5/workbook_html.js): Start here Q1 to Q6 (p5/content/l5.js and l6.js, workbook()), the Investigation (p5/content/inv.js), Think harder A1 to A4 (first four `qbank.stretch`), Go further B1 to B3 (last three `qbank.challenge`) and the "Make up your own" prompt (gaps.js), in printed order. Every printed sentence used is checked to occur in those source files (the build stops otherwise). Every auto item has an independent checker (every unit cube listed and classified by its position; every whole-number box searched; water volumes matched by a search over the depth; minute-by-minute simulation of the machine, taps, printers and candles; a search over every mix of egg boxes; the half hours of a car park stay counted; a search over the minutes of two phone plans; exact fractions for the bath and the cats); the printed answer must equal it or the build stops. Answers also agree with the printed keys in l5.js and l6.js.

## Not mirrored exactly, and why
- Split cards (so that any card can be opened first, and no card shows another's answer): L5 1(b) = number plus a "how do you know" self-check; L5 2(a) = a self-check list plus a count; L5 Q5 table = 2-face row, 1-face row, no paint, and the "do they add up to 64" check (a self-check with a picture of the 64 cubes sorted by painted faces); L5 Investigation (a) = list (self-check) plus count, (b) = open "which would you choose" plus a typed "most like a cube" (3, 4, 4), (c) = count for 64 cubes plus a choice of which of 15, 16, 17, 18 cubes gives only one box shape (this is how "is there a number that gives only ONE box" is auto-marked). L6 1(a) table = two cards (1 and 5 minutes; 160 bottles and 12 minutes) with the table drawn, the answer cells shown as question marks; L6 6(a) table = one card per gym; L6 6(c) = which gym plus how many dollars cheaper; L6 Investigation (a) = list (self-check), count, and one pairing card ("tap B runs 6 minutes: how long does tap A run?"), (b) = the shortest way (fields: A minutes, B minutes) plus a "why" self-check, (c) = count for 25 litres plus a "what changes" self-check.
- L5 2(a) the typed list of 8 cuboids is a self-check (24 numbers on a phone keyboard is too fiddly); the count is auto-marked. L5 Investigation (a) is the same (27 numbers).
- L5 2(b), Investigation (b) "most like a cube": typed as the three edges, smallest first (a rule stated in the question).
- L6 Q5 Start here "circle every half hour" becomes "how many half hours after the first hour" (the time line is drawn; 1.15 p.m. is marked, as in the print). L6 3(a) and 3(b) say "ignore the crack": the print shows the crack on the picture but only uses it in 3(c).
- Take-home stars are not shown (everything is available online). The solids are drawn again as inline SVG (the workbook oblique drawing, but at a size and text size that read on a 390 px phone); the L5 Q4 cubes sit under the tank (same scale) and the L6 shop boards are stacked, the time line goes down. Question figures never show an answer; solution pictures (rate table filled in, P and Q bar with the checked minutes and pages, the numbered half hours, the 64 cubes sorted by paint) are built from the checked values.
- Decimal and money answers (L5 6(a) 14.4 litres, L6 5(a) 4.80, A2 9.60, A3 9.50, 1(b) the time 9.25 a.m.) are typed text with a generated list of accepted writings (14.4 / 14.40 / 14.4 l / 14.4 litres; $4.80 / 4.8 / 4.80; 9.25 a.m. / 9:25 am / 9.25).
- Frames put the unit before the box ("Base area, 40 × 25 (cm²): [ ]") or print ¢ after it, so a label never separates from its box on a phone (tested at 390 and 360 px).
- A phone calculator is fine; the page has none.

## Audited mistakes avoided from the start (week 1 and 2 audits)
No stem, hint, example or solution figure shows another card's answer (checked by a search of every answer against every other card's question, hint, frame and figure text: only numbers given in the problems repeat); examples are not answers (L5 C0 "1 × 1 × 12" is one of four boxes, the L6 time example is 8.05 a.m., the money example is 3.50); hints nudge and none states a rule that is only true for one case; the position or pairing a printed question tests is kept (L5 12 edges × 2 = 24 and 6 faces × 4 = 24, L6 "minutes for 160 bottles" and "bottles in 12 minutes" in the right columns, L6 candle height and hours); no long riddle is repeated (one short story per card); wording for screens ("type", no "circle" or "cross out"); list answers have grouped=False; explanation and "why" items are self-checks, not typed text; units are never required (cm, cm³, litres, minutes, cents words are accepted automatically), but the symbols ℓ and ¢ are not read by the shared number matcher, so the question says "Type just the number" and the frame prints ¢ after the box.

## Open questions
- Typed units: "27 ℓ" (the symbol) is refused in a number box ("27 l", "27 L", "27 litres" pass); "70¢" is refused too (frames print ¢ after the box and the stem says "Type just the numbers"). Both are in the shared matcher; tell me if you want them accepted.
- L6 Investigation (a)'s pairing card gives the child one way to check; the full list is a self-check. Is that enough auto-marking for the "find all the ways" skill?
- L5 Q5 "check" (do your four numbers add up to 64) is a self-check, because a Yes/No choice would always be "Yes" for a child who has the right numbers.
- Nothing here has been seen by a child. Difficulty and timing are untested.

No shared file was changed.
