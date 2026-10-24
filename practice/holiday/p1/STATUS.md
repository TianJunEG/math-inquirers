# Level 1 (P1, ages 6-8) holiday online practice, week 1 (lessons 1 and 2)

Not deployed. No website, Supabase or server change. Build and test: `python3 practice/holiday/build_holiday.py p1 N` then `python3 practice/holiday/test_holiday.py p1 N` (N = 1, 2). Output in `practice/holiday/p1/0N/dist/` (git-ignored); proof screenshots in `practice/holiday/p1/0N/proof/`.

Week 1 = lessons 1 and 2 (`website/data/beta_schedule.json`: lessons `n` 1 and 2 of group L1A). Source of the questions: `hp/workbook_html.js` (the designed workbook), `hp/qbank.json` (Think harder = stretch 1 to 4, Go further = challenge last 3, as the workbook builder slices them), `hp/gaps.json` (Investigation). These are hand-written code, not machine-readable item data, so each question was extracted by hand into `p1/0N/lesson.py` with an independent checker; the build refuses to write unless every `src` string is found in those source files.

| | Lesson 1 Number patterns | Lesson 2 Number bonds |
|---|---|---|
| Items (cards) | 31 | 34 |
| Auto-marked (number, boxes, set, choice, text) | 21 | 24 |
| Self-check, with a model answer (explain / notice) | 8 | 9 |
| Paper-only self-check with a figure of the correct drawing | 2 (frog hops) | 1 (magic triangle) |
| Unavailable online | 0 | 0 |
| Variant families (template + oracle, every combination run) | 3 (104 combos) | 3 (197 combos) |
| Printed text shown unchanged / reworded for the screen | 19 / 12 | 20 / 14 |

Every auto-marked answer equals an independent checker (loops, enumeration, brute-force magic-triangle search). Self-check items that state a fact (a list, a gap, a total) are checked the same way; only 3 explanations have no objective fact (L1 4(b) and 5(b) are checked for the numbers they cite; L2 "Why do you think it works?" is open).

## Not mirrored from the printed workbook, and why
- Look-back box, "Tool of the day" strategy card, "After question 3 you may choose" banner, Name/Group/Date line: paper routine pieces, not questions.
- The printed answer lines/ruled lines: replaced by boxes, a text box, or (self-check) a model answer.
- Lesson 1 Q3 (colour the landings) and 3(a) (cross the landings) cannot be done on the screen: shown as paper-only with the note and a drawn correct number line. Lesson 2 Q5 is auto-marked as the numbers; the triangle is drawn on screen; C3(c) is paper-only.
- A printed question is split into cards: parts `(a)(b)`; "next two numbers" and "rule" (L1 Q2); "Is she right?" and "Explain" (L2 4(e), T1, T3, T2, T4, C1); Think harder / Go further questions with an answer plus an explain part. L1 Q4 gets two extra cards ("Write both lists first": Ali's list, Mei's list). L1 Q5's table and Box 10 are one card of 8 boxes.
- Added wording: L1 Investigation 1 says "(Do not write 0)"; L1 3(b) says "up to 20"; L1 2 rule cards say "type it in words, like add 2 or take away 5". Printed L2 Q4 labels its parts a, (b), c, (d), e (a printing quirk); online they are 4(a) to 4(e).
- The gaps.json "check" questions (Check yourself) are not in the printed workbook and are not included.
- Variants exist only for skip counting, missing numbers, next-two numbers (L1) and the = sign, bonds of 20, bonds of 10 to 20 (L2).

## Runner changes (shared, `practice/ext/public/sheet.js`)
Added: a text answer type (same normalisation as `practice/submit/mark.js`), an Investigation tier shown between Start here and Think harder, `paper` self-check items (no text box, the paper note, a figure of the correct drawing under the solution), `shown` for the displayed answer. `practice/ext/test_ext.py`, `test_submit.py` and the two node mark/handler tests still pass.

## Open questions
1. Rule answers (L1 Q2) are typed words. `hlib.rule_accepts` lists about 300 wordings ("add 3", "+3", "3 more", "goes up by 3 each time", a bare 3) so a correct but unusual wording (for example "count on in 3s") is marked "look again". If that is unacceptable, make them self-check (one line in `lesson.py`: change `type` to selfcheck).
2. `practice/submit/make_keys.py` reads `practice/ext/dist` and has no `text` branch or holiday path yet; holiday items carry `marking_mode`, `paper_only`, `tags` for it. The 3 text items of lesson 1 need that branch before server marking.
3. The dots are drawn as circles, not the workbook's stars; the number line is drawn as two rows on screen (0 to 10, 10 to 20) so the numbers are readable on a phone.
