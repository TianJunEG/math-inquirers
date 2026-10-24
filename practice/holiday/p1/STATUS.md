# Level 1 (P1, ages 6-8) holiday online practice, week 1 (lessons 1 and 2)

Not deployed. No website, Supabase or server change. Build and test: `python3 practice/holiday/build_holiday.py p1 N` then `python3 practice/holiday/test_holiday.py p1 N` (N = 1, 2). Output in `practice/holiday/p1/0N/dist/` (git-ignored); proof screenshots in `practice/holiday/p1/0N/proof/`.

Week 1 = lessons 1 and 2 (`website/data/beta_schedule.json`: lessons `n` 1 and 2 of group L1A). Source of the questions: `hp/workbook_html.js` (the designed workbook), `hp/qbank.json` (Think harder = stretch 1 to 4, Go further = challenge last 3, as the workbook builder slices them), `hp/gaps.json` (Investigation). These are hand-written code, not machine-readable item data, so each question was extracted by hand into `p1/0N/lesson.py` with an independent checker; the build refuses to write unless every `src` string is found in those source files.

| | Lesson 1 Number patterns | Lesson 2 Number bonds |
|---|---|---|
| Items (cards) | 31 | 34 |
| Auto-marked (number, boxes, set, choice) | 18 | 24 |
| Self-check, with a model answer (explain / notice / write the rule) | 11 | 9 |
| Paper-only self-check with a figure of the correct drawing | 2 (frog hops) | 1 (magic triangle) |
| Unavailable online | 0 | 0 |
| Variant families (template + oracle, every combination run) | 3 (104 combos) | 3 (197 combos) |
| Printed text shown unchanged / reworded for the screen | 19 / 12 | 20 / 14 |

Every auto-marked answer equals an independent checker (loops, enumeration, brute-force magic-triangle search). Self-check items that state a fact (a list, a gap, a total) are checked the same way; only 3 explanations have no objective fact (L1 4(b) and 5(b) are checked for the numbers they cite; L2 "Why do you think it works?" is open).

## Not mirrored from the printed workbook, and why
- Look-back box, "Tool of the day" strategy card, "After question 3 you may choose" banner, Name/Group/Date line: paper routine pieces, not questions.
- The printed answer lines/ruled lines: replaced by boxes, a text box, or (self-check) a model answer.
- Lesson 1 Q3 (colour the landings) and 3(a) (cross the landings) cannot be done on the screen: shown as paper-only with the note and a drawn correct number line. Lesson 2 Q5 is auto-marked as the numbers; the triangle is drawn on screen; C3(c) is paper-only.
- A printed question is split into cards: parts `(a)(b)`; "next two numbers" and "rule" (L1 Q2); "Is she right?" and "Explain" (L2 4(e), T1, T3, T2, T4, C1); Think harder / Go further questions with an answer plus an explain part. L1 Q4 gets two extra cards ("Write both lists first": Ali's list, Mei's list); since the Week 1 audit these two are self-check (paper) cards, not auto-marked. L1 Q5's table and Box 10 are one card of 8 boxes.
- Added wording: L1 Investigation 1 says "(Do not write 0)"; L1 3(b) says "up to 20"; L1 2 rule cards say "type it in words, like add 2 or take away 5". Printed L2 Q4 labels its parts a, (b), c, (d), e (a printing quirk); online they are 4(a) to 4(e).
- The gaps.json "check" questions (Check yourself) are not in the printed workbook and are not included.
- Variants exist only for skip counting, missing numbers, next-two numbers (L1) and the = sign, bonds of 20, bonds of 10 to 20 (L2).

## Runner changes (shared, `practice/ext/public/sheet.js`)
Added: a text answer type (same normalisation as `practice/submit/mark.js`), an Investigation tier shown between Start here and Think harder, `paper` self-check items (no text box, the paper note, a figure of the correct drawing under the solution), `shown` for the displayed answer. Shared files also changed for server marking: `practice/submit/make_keys.py` (holiday path and text branch, backward compatible). `practice/ext/test_ext.py`, `test_submit.py` and the two node mark/handler tests still pass.

## Open questions
1. DECIDED: typed rule wordings (L1 Q2 "add 3", "take away 3", "add 4") are self-check, so a correct but unusual wording is never marked wrong. The `text` answer type stays in the runner and in `mark.js`/`make_keys.py` for closed single-word or number answers; lesson 1 and 2 use none.
2. DONE: `practice/submit/make_keys.py holiday p1 N` makes the server keys (with a `text` branch, product 'holiday', per-item tags); `test_holiday.py` step 6 checks that `mark.js` marks every item as the page does.
3. The dots are drawn as circles, not the workbook's stars; the number line is drawn as two rows on screen (0 to 10, 10 to 20) so the numbers are readable on a phone.

## Week 1 audit fixes (items, 24 Oct 2026; see AUDIT_WEEK1_L1_3.md)
- M6 L2 5(a): now a `fields` card, "between 1 and 2 / 2 and 3 / 3 and 1" with answers 6, 4, 5 (position checked; checker requires a unique solution for corners 1, 2, 3).
- M3 L2 5(b) hint no longer says the corners; it suggests trying corners and testing a side.
- Low: L1 rule cards (42 words) now about 25 words; L1 Investigation 1, L1 C3 and L2 Investigation 1 shortened (meaning kept, printed text still in `src`); L1 4 Ali/Mei lists are self-check.

---

# Week 2 (lessons 3 and 4)

Not deployed. No website, Supabase, server or shared-runner change (`sheet.js`, `practice/submit/*`, `build_holiday.py`, `hlib.py`, `test_holiday.py` untouched). Build and test: `python3 practice/holiday/build_holiday.py p1 N` then `python3 practice/holiday/test_holiday.py p1 N` (N = 3, 4); both pass (RESULT: OK, no console errors, no horizontal scroll at 390 and 360 px, figure text at least 11.5 px). Output in `practice/holiday/p1/0N/dist/` (git-ignored); proof screenshots (390 px and 900 px, light and dark) in `practice/holiday/p1/0N/proof/`. New file `practice/holiday/p1/p1lib.py` holds the figure helpers for these two lessons (fruit, cat, dog, fish, star and shape pictures, picture graphs, numbered pattern rows, tally table, stick rows, dot triangles); no coin or note pictures.

Week 2 = lessons 3 and 4 (`website/data/beta_schedule.json`, group L1A: lesson 3 Tue 1 Dec, lesson 4 Fri 4 Dec). Sources: `hp/workbook_html.js` (Start here), `hp/qbank.json` (Think harder = stretch[0:4], Go further = challenge[-3:], as the workbook builder slices them), `hp/gaps.json` (Investigation); hand-written code, so each question was extracted by hand into `p1/0N/lesson.py` with an independent checker; the build refuses to write unless every `src` string is found in those sources. Printed answers checked against the Tutor Guide answer key (Level 1 Tutor Guide, lesson 3 key and "Think harder, Go further and Investigation" table).

| | Lesson 3 Picture graphs | Lesson 4 Patterns |
|---|---|---|
| Items (cards) | 23 | 26 |
| Auto-marked (choice, number, boxes, set) | 13 | 21 |
| Self-check with a model answer (explain / compare) | 6 (3 of them open: no objective fact) | 3 |
| Paper-only self-check with a figure of the correct drawing | 4 (group tally, two Investigation graphs, Go further 3) | 2 (Investigation 1, Go further 3) |
| Unavailable online | 0 | 0 |
| Variant families (template + oracle, every combination run) | 3 (298 combos: T2, T3, C2) | 3 (24 combos: T2, C1, T4) |
| Printed text shown unchanged / reworded for the screen | 20 / 3 | 14 / 12 |

Every checker is independent of the printed answer: lesson 3 counts the pictures of the drawn graph, searches by loops (banana/orange votes, pictures for a key, all graphs for Go further 3: exactly two); lesson 4 builds each pattern place by place by going round its set, and counts the distinct sticks of the drawn rows of triangles and squares (no formula), and dots row by row. Investigation 2 (lesson 4) is checked over all 27 sets of three shapes, Investigation 3 over all orders of four different shapes.

## Audited week 1 mistakes avoided from the start
- No card shows another card's answer in its stem or hint: each stem gives only its own data; hints nudge (which places finish a set, count in 2s) and never state a result; the worked examples (tally, bead pattern) are different from the question numbers.
- Position kept: lesson 4 Q1, Q4 and Think harder 1 ask for the shape in a named place (choice), not a sum; lesson 4 7(a) is seven labelled boxes (4 to 10 triangles), not one total; lesson 3 Q4 asks which two fruits (a pair of names), not a number.
- Explanations (3 Q6(b), 4 Q4(d), 7(c), 8(b), Investigation why) and every list-with-reasons are self-check, never typed text. Lists are typed with commas (Investigation 3 of lesson 4: places up to 20, `4,8,12,16,20` or with spaces both accepted).
- One figure per card that needs one (a small picture graph or pattern row), no long repeated riddle; wording for the screen ("choose the shape", "do this on paper").
- Long rows are wrapped into two numbered rows so every place is readable on a 390 px phone.

## Not mirrored from the printed workbook, and why
- Name/Group/Date line, Tool of the day card, "After question 3 you may choose" banner, Look-back box: paper routine pieces, not questions.
- Lesson 3: Part B (the group's own vote with tally marks, Q8 and Q9) cannot be done alone on a screen: the vote and tally table are a paper-only card ("Vote") with a drawn example tally; Q8 and Q9 are open self-check cards (the answer depends on the group). The Investigation is split into five cards: draw the 1-child graph (paper, correct graph shown), draw the 2-children graph (paper), compare the two graphs, "could the key be 3?" (choice) and why (self-check). Q6 is split into 6(a) Yes/No (auto) and 6(b) why (self-check). Pictures are redrawn as simple icons (apple, banana, orange, grape, watermelon; cat, dog, fish; stars), not the workbook art. Go further 3 (make your own graph) is paper-only and the correct drawing shows both graphs.
- Lesson 4: "Draw the missing shapes in places 8 and 9" (Q1) and the other "write the shape in the box" questions become choices (Q1(a), Q1(b), Q2, Q3, Q4(a)(b)(c), Q5, Q6, Think harder 1, 3): shape names typed as words cannot be matched reliably, and a choice keeps the printed meaning (which shape is in place n). Q7(a) table is seven labelled boxes. Q8 is split into the number (auto) and "show how you worked it out" (8(b), self-check). Q4(d) "How do you know?" is a self-check card. Go further 3 ("ask a partner") is paper-only: "ask a friend or a grown-up". Investigation: draw-your-own (paper), "is Mei always right" (choice, checked over all 27 sets), "which places match place 4" (list of places up to 20, added "up to 20").
- Added wording: "Use only whole pictures" (lesson 3 Investigation 4), "up to 20" (lesson 4 Investigation 3), "Which shape goes in place 8?" (lesson 4 Q1).
- The gaps.json "check" questions (Check yourself) are not in the printed workbook and are not included (as in week 1).
- Variants only where a template with an oracle exists and no figure is needed (lesson 3 T2, T3, C2; lesson 4 T2, C1, T4); items whose question is a drawn graph or pattern have no variant.

## Open questions
1. Shape and colour answers (lesson 4) are choices, not typed words. If you want typed words (e.g. "triangle") the `text` type exists, but every spelling and plural would need a list; I judged choices safer for ages 6 to 8.
2. Lesson 3 Q6(a) "Is Mei right?" is auto-marked No (printed key: "Only our class voted"); its checker encodes that fact (the graph is one class), so it is a judgement item. Say if you would rather make it self-check.
3. The nav shows "Investigation" on every Investigation button (the shared runner shows the first word of the card number); each button has an aria-label with the full number. A shorter number scheme ("Inv 1") would need a runner change.
4. 7(a) in lesson 4 asks for the seven numbers 9 to 21; the answer for 10 triangles (21) is also the answer of 7(d), as printed.

---

# Week 3 (lessons 5 and 6)

Not deployed. No website, Supabase, server or shared-file change (`sheet.js`, `practice/submit/*`, `build_holiday.py`, `hlib.py`, `test_holiday.py` untouched). Build and test: `python3 practice/holiday/build_holiday.py p1 N` then `python3 practice/holiday/test_holiday.py p1 N` (N = 5, 6); both give RESULT: OK. Proof screenshots in `practice/holiday/p1/0N/proof/`. New figure helpers appended to `p1/p1lib.py` (number machine strip, IN/OUT table, queue, marble bars, snail wall, ways table). No coin or note pictures: coins are words and numbers.

Week 3 = lessons 5 and 6 (`website/data/beta_schedule.json`, group L1A: lesson 5 Tue 8 Dec, lesson 6 Fri 11 Dec). Sources: `hp/workbook_html.js` (Start here), `hp/qbank.json` (Think harder = stretch[0:4], Go further = challenge[-3:]), `hp/gaps.json` (Investigation; lesson 6 also the extra Think harder T5 "Dollars"). Hand-written code, so items were extracted by hand with independent checkers (try every number / every combination of coins / simulate the snail); the build refuses to write unless every `src` string is in those sources. Printed answers agree with the Tutor Guide key.

| | Lesson 5 Mystery number | Lesson 6 Coin combos |
|---|---|---|
| Items (cards) | 27 | 27 |
| Auto-marked | 24 | 17 |
| Self-check with a model answer | 1 (I4 why) | 9 |
| Open (make up your own) | 2 (take-home, G3) | 1 (G3) |
| Paper-only | 0 | 0 |
| Unavailable online | 0 | 0 |
| Variant families (every combination run) | 9 (480 combos) | 3 (25 combos) |

## Not mirrored / changed from the print, and why
- Look-back box, Tool card, Name line, "After question 3" banner: paper routine, not questions.
- L5 2(b) is three cards: the rule (choice), the missing OUT, "OUT 30 means IN". L5 T3 is rule (choice) plus the two numbers. L5 G1 is IN (number) plus "what does a one-step machine add" (number). Rules are choices, not typed words (typed rule wordings are self-check by earlier decision).
- L5 Investigation: "Mei says OUT is always the same as IN. Is Mei always right?" became a choice ("What does she find?") so its stem does not give away the answers of Investigation 1 (3, 10, 25); the "why" is a self-check.
- L5 Q3 bars: Ali's bar is drawn; the child colours Mei's and Ben's on paper if they like (hint says so). L5 4(b) "draw circles" says "on paper". G2 asks "Type the day number".
- L6 Q1 and Q2 (write the ways / the table) and T4 are self-check lists with the correct table shown after Submit. Fewest and most coins in Q1 are asked as the coin values (set, "20" and "5, 5, 5, 5"), which keeps "which way" rather than just a count. Q3(a) is split into the number of coins and which coins. T1 and T4 each also get a "how many" number card (not printed; the Tutor Guide gives 2 and 6). Q2 prints the example "20¢ + 5¢" which is one of the answers, so the screen example is "10¢ + 5¢".
- L6 coin pictures (tray, purse, Ben's two coins, coin rows, notes) are not drawn (no coin or note images); the stems say the coins in words. Q5 and Q6 are `text` with the accepted forms 35, 35¢, 35 cents (the shared number matcher does not accept the ¢ sign).
- L6 T5 Dollars (printed extra Think harder) is included: (a) values of the fewest notes/coins (set), (b) Yes/No and why.
- The Check yourself questions of gaps.json are not in the print and are not included. L6 Investigation extension (put the 10¢ away) is tutor-only and not included.
- Variants only where a template with an oracle exists and the question text carries everything (L5 1(a), 1(b), 1(c), T4, 3(b), 4(a), 4(b), T3 find, G2; L6 3(a), T3, T2).

## Print-inherent answer coincidences (kept, not fixable without changing the printed numbers)
L5 3(c) "6 more" is the 6 of "6 fewer"; L5 1(a) prints 12 which is the answer of 1(b); L6 Q4 prints 35¢ which is the answer of Q5, and T3 prints 45¢ which is the answer of Q6; L6 Q2 prints "4 ways" while 20¢ also has 4 ways (no count card is asked for 20¢ or 25¢).

## Open questions
1. Typed ways of paying (L6 Q1, Q2, T4, 3(b)) are self-check; an auto-marked version would need a "list of sets" answer type.
2. L5 3(c) and the L6 Q4/Q5 chains above: say if you want the stems changed from the print.

## Week 3 L1-3 audit follow-up (item level)
M1 answer leaks reworded, M2 explicit short nav labels, remainder-0 variants excluded (P3 L5 3(b)), long stems shortened, doubled "Make up your own"/"Take-home" lead-ins removed. Print-inherent chains kept as printed (P1 L5 Go further 1(a)/(b), 3(c); P1 L6 Q4/Q5, T3/Q6; P3 L6 5(b), T3). P1 L6 Q5/Q6 keep cents only (printed answers are in cents).
