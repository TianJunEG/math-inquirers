# Level 5 (key p5, ages 10 to 12) online holiday practice: week 5 (lessons 9 and 10)

Built and tested, not deployed (dist is git-ignored). Build: `python3 practice/holiday/build_holiday.py p5 9` (and `p5 10`); test: `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 practice/holiday/test_holiday.py p5 9` (and `p5 10`). Both end RESULT: OK.
Sources: `p5/09/lesson.py`, `p5/10/lesson.py` (items, independent checkers, variants) and `p5/p5fig5.py` (figures, new this week). Earlier weeks: STATUS.md, STATUS_WEEK2.md to STATUS_WEEK4.md. No shared file and no `p5lib.py` change.
Week 5 = L5 lessons 9 and 10 (website/data/beta_schedule.json, group L5A: session 9 = Wed 23 Dec 16:45 (moved from Fri 25 Dec), session 10 = Sun 27 Dec 16:15): lesson 9 "Pattern Generalisers" (Patterns and Number Sense), lesson 10 "Challenge Day" (Mixed Strategies, the showcase lesson).

| | Lesson 9 | Lesson 10 |
|---|---|---|
| items | 42 | 35 |
| auto-marked | 34 | 28 |
| self-check (compare with model answer) | 7 (all with a checked fact) | 5 (all with a checked fact; incl. the paper-only A2 list) |
| open (make up your own / which start did you use, no objective fact) | 1 | 2 |
| paper-only (inside self-check) | 0 | 1 (A2 list) |
| unavailable (not mirrored) | 0 whole questions | 0 whole questions |
| variant families (all combinations equal an oracle) | 16 (513 combinations) | 9 (124 combinations) |
| question text as printed / reworded | 13 / 29 | 13 / 21 |

Item types, L9: number 18, fields 9, choice 6, text 1 (money), self-check 8. L10: number 11, fields 8, choice 6, text 2 (a fraction, four names), set 1 (15 numbers in order), self-check 6.

Mirrors the printed workbook (p5/workbook_html.js): Start here Q1 to Q5 (L9) and Q1 to Q6 (L10) from p5/content/l9.js and l10.js, the Investigation (inv.js), Think harder A1 to A4 (first four `qbank.stretch`), Go further B1 to B3 (last three `qbank.challenge`) and the "Make up your own" prompt (gaps.js), in printed order. Every printed sentence used is checked to occur in those files (the build stops otherwise).
Independent checkers: L9 counts the chairs (free sides of every square table) and the sticks (the lines of the drawn houses; the drawn circles and lines are asserted equal to the count), the dots of a diamond, finds every rule a x n + b by trying all pairs, tries every split for tickets, coins and quiz marks, and writes out the digits of the counting numbers. L10 tries all 24 arrangements against every clue (dishes, chairs), runs the money puzzles forwards from every start with exact fractions, counts squares by position, tests what each child says for each culprit, lists the ways to climb (compositions) and finds the tank capacity by search. The printed answer must equal the checker or the build stops.

## Not mirrored exactly, and why
Lesson 9
- Q1(d) "Ben says 10 tables seat 22, so 20 tables seat 44" is reworded without the numbers (they are the 1(a) answer): a Yes/No choice, a number card (20 tables seat 42) and a self-check "explain what you notice when the tables are doubled". Think harder A2 drops "= 2 × 40 + 2" from the stem (it is the 1(b) rule).
- Q2(a) "why not 6?" is a separate self-check (the number card says only "how many sticks does each new house add"). Q2(b) is the rule (two boxes) plus a card for 20 houses; Q2(c) is two boxes.
- Q3 table: the printed first row is in the stem; online it is a number card (cost of 10 adult and 5 child tickets), a too much / too little choice (stem does not give the total) and the final answer (two boxes). The child's own table stays on paper.
- Q4(a) is two cards (value if all 20¢, typed as money; the 30¢ rise); 4(b) has a self-check "check against both facts". Q5(b) is three cards (1, 2, 3 wrong), a choice (can 80 be her score) and a self-check "explain".
- Investigation: the easy first step is a number card (9); (a) asks the totals for 4, 5 and 6 odd numbers (the first three are in the stem of the easy step), then a choice "what kind of numbers" and a card for 10 odd numbers; (b) is a choice "always true?" plus a self-check with the L-shaped dot picture shown after Submit; (c) is four totals, the first 20 even numbers, and a self-check for the rule in words.
- Think harder A1 is a choice (colour of the 50th bead) plus a number; A4 is the three sums, a self-check "what do you notice" and the first 20 odd numbers. Go further B1 to B3 are one card each.
- The matchstick, table and diamond pictures show no counts; the printed "draw figures 1, 2 and 3" in the make-up prompt is on paper, and "ask a partner" is dropped.
Lesson 10 (mirrors the printed Challenge Day page; the take-home stars are not shown)
- Q1: the printed tick-and-cross grid cannot be filled on screen, so the four clues are drawn once as a card and there is one choice card per child (Ali, Ben, Mei, Siti). Q2 is the money left puzzle plus a card for the two middle amounts (before the gift, before lunch). Q3 is two boxes plus a self-check "check against both clues". Q4 is (a) 1 by 1, (b) 2 by 2 and 3 by 3, (c) the total and a self-check "how do you know none are bigger". Q5 is a table card (liars for each child) and the choice of who broke the vase. Q6(a) is a number; 6(b) "which start did you use" is open.
- Investigation: easy step (3 ways), a self-check list of the ways for 4 steps and a count card after it ("do the list first"), the table up to 6 steps (5 and 6 steps), a choice for the pattern (the stem does not list the numbers), a self-check for the last-jump reason, 8 steps, and the 3-step what-if.
- Think harder A2 is a list written on paper (self-check, list shown after submit), a marked count card (15) and a marked card for the smallest and biggest number (104, 500); the other cards are one each. Go further B1 is two cards (litres, fraction); B3 is the four names typed (names accepted with commas, spaces, "and" or "then").
- A calculator is not needed. Paper-only items: none.

## Audited mistakes avoided from the start (week 1 to 4 audits)
No stem, hint, example or solution figure shows another card's answer (a search of every number answer of 2 or more digits against every other card's stem, hint, frame: only numbers given in the problems repeat, for example 20 questions / 20 tables / 20 litres, $12 and 30 coins). Explain cards have neutral stems ("Explain what you find out about...", "Explain what you notice about..."); the Investigation stems do not state results of earlier parts; the choice card for the pattern does not list the sequence; hints are nudges and none states a rule true for one case only (every hint is on request only). Count cards come after the list card and say "Do the list question first". Wording for screens (no "circle", "cross out", "swap"). Labels are explicit, short, unique and number-first. Variants are constrained so every one is a possible question (integer answers, no zero or negative amounts, "marks" never "1 marks"), and every variant that changes a picture brings its own (bar models, grid, diamond) or reuses the unchanged pattern picture. Solution texts were checked for false generalisations ("more rows means more end chairs" holds for every number of rows; "Mum is always 32 years older" is the case it names).

## Open questions
- Lesson 10 Q1 has no tick-and-cross grid (the print's working space). Is a choice card per child enough, or should a drag-style grid item be built later?
- Week 5 audit: Think harder A2 is now a self-check list plus marked count and ends (no 15-number typing). L9 A2 says '8 separate rows'; L9 B2 variants no longer give a negative score.
- Three Investigation cards ask for the pattern in several small steps (lesson 9 (a) to (c); lesson 10 (a) to (c)); this is more auto-marking than the print has. Is that wanted for the last lessons?
- Nothing here has been seen by a child. Difficulty and timing are untested.

No shared file was changed.
