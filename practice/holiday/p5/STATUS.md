# Level 5 (key p5, ages 10 to 12) online holiday practice: week 1 (lessons 1 and 2)

Built and tested, not deployed (dist is git-ignored). Build: `python3 practice/holiday/build_holiday.py p5 1` (and `p5 2`); test: `python3 practice/holiday/test_holiday.py p5 1` (and `p5 2`, needs PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers).
Sources are `practice/holiday/p5/01/lesson.py` and `02/lesson.py` (items, independent checkers, variants) and `practice/holiday/p5/p5lib.py` (checkers, accepted wordings, figures).

Week 1 = lessons 1 and 2 (website/data/beta_schedule.json: L5 lessons 1 and 2 are the first two sessions; Level 5 lesson 1 is "Million Puzzles", lesson 2 is "Fraction Feats").

## What mirrors the printed workbook (p5/workbook_html.js)
Start here Q1 to Q6 (p5/content/lN.js `workbook()`), the Investigation (p5/content/inv.js), Think harder A1 to A4 (first four `qbank.stretch`), Go further B1 to B3 (last three `qbank.challenge`) and the "Make up your own" prompt (gaps.js `pose`), in the printed order. Every printed sentence used is checked to occur in those source files (build stops otherwise).

| | Lesson 1 Million Puzzles | Lesson 2 Fraction Feats |
|---|---|---|
| items | 36 | 33 |
| auto-marked | 32 | 28 |
| self-check (compare with model answer) | 4 (3 with a checked fact, 1 open) | 5 (4 with a checked fact, 1 open) |
| paper-only (drawing/kit) | 0 | 0 |
| unavailable (not mirrored) | 0 whole questions | 0 whole questions |
| variant families (all combinations equal an oracle) | 2 (18 combinations) | 4 (26 combinations) |
| question text exactly as printed / reworded | 15 / 21 | 22 / 11 |

Item types: number, fields (boxes), set (typed list), choice, text (typed fractions, brackets and number lists, each with a generated list of accepted wordings), selfcheck. Every auto-marked item has an independent checker (search, simulation or exact fractions; for example every 7-digit number that fits the riddle clues is searched, all 24 card arrangements of the fraction sums are tried, every way of putting one pair of brackets in is tried, the tank is simulated); the printed answer must equal it or the build stops. Worked solutions are written for every item and are shown after Submit, including skipped questions.

## Not mirrored exactly, and why
- Workbook "take-home" stars are not shown: everything is available online.
- The Q3 place-value chart (M HTh TTh Th H T O) and the Q4 "My estimate" column are scratch work on paper; online the table row becomes one choice (Could be right / Must be wrong) and the estimate is in the worked solution.
- Q6(a) "circle each one" becomes "type the ones that round to 2 500 000" (a text list, any order, with or without commas inside the numbers).
- Q5 and Think harder A2 "put one pair of brackets in" are typed (the whole sum with brackets; x, *, × and -, − all accepted); wrong placements are marked wrong.
- Lesson 1 Investigation (b) "which side wins" is split into two auto-marked choices (targets 7 000 000 and 8 000 000) plus a self-check for "what do you notice"; (c) the rule is a self-check with the rule verified by search for every target from 2 to 8 million.
- Lesson 2: Q1(b) is a choice plus a self-check "explain" (with the picture of the shortfalls shown after Submit); "Explain how you know" and "how do you know when to stop" are self-checks. Think harder A1 and Go further B2 (two ways) use four boxes with a stated order rule (smaller bottom number first, smaller first way first) so that they can be auto-marked.
- Paper-only items: none. The week 1 Level 5 workbook has no ruler, kit or drawing task: the bars and the figures are printed aids and the drawings are optional ("draw a model"). The figures are drawn again as inline SVG (the workbook SVG text is too small for a 390 px phone): digit cards, the rounding number line, share bars (with the shortfall picture as the self-check solution), the sticker bar, Ravi's bar model, the digit-card fraction boxes, the 12-part bar.
- Calculator use is allowed in the printed lesson; the page has none. A phone calculator is fine.

## Shared files touched (backward compatible; Level 1 holiday test, test_ext.py, submit tests all re-run and pass)
- practice/ext/public/sheet.js: `toNum` ignores a leading `$` (so "$120" is read as 120); the boxes of a `fields` frame keep the word before a box and the punctuation after it together, so "1/" and its box never split across two lines.
- practice/submit/mark.js: same `$` rule (kept equal to sheet.js).
- practice/holiday/build_holiday.py: `.card .q{white-space:pre-line}` so a question can have line breaks (a clue list).

## Open questions
- Typed bracket answers on a phone keyboard (× and ÷ are awkward; x, * and / are accepted). If this is a problem, a native "choose where the brackets go" item type could be added.
- Fractions are typed as text and marked against a generated list of equivalent forms (mark.js already has a native `fraction` type with lowest-terms checking; the holiday build does not use it yet). "Simplest form" questions (Q4(b)) accept only the lowest terms.
- Nothing here has been seen by a child. All timing and difficulty is untested.

## Audit fixes (week 1)
L1 3(a) to 3(c): the six-clue riddle is now one card figure shown above each question. L1 6(a) example changed. L2 5(b) and 6(a) hints are kinder; the 6(a) example is 3 1/4. L2 B2 asks "How can the pizzas be cut?" again as a typed sum of two unit fractions (either of the two ways is marked right; the count is not told).
