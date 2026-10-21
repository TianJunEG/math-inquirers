# Close gaps, level P4 (warm-up check, fast track, open investigation, reflection)

Nothing committed. Files touched (P4 only): p4/content/l1.js to l10.js (new `gaps` export), p4/workbook_html.js, p4/wb_pdf.py (one CSS line), p4/guide.js, rebuild/gen_p4l1.py to gen_p4l10.py, docs/audit/verify_close_gaps_p4.py, this file. Shared files (levels/*, rebuild/slidekit.py, hp/*) not edited.

## What was added to every lesson
- Warm-up check (1 to 4 min): 2 questions on the key idea in a new setting, with answers and "a good reason sounds like" in the deck notes and the tutor guide. One new deck slide (`p4lK-check`, after the title).
- Fast track: printed note at the top of the new workbook page; tutor guide explains the rule (both right AND can say why, then start on the Think Harder pages plus Open investigation at minute 34; everyone still joins explore, mini-lesson, page checks, talk time, exit ticket, reflection; message sent privately, nobody labelled, changes each lesson, can return to page 1 any time). True to the program: printed workbook, groups of up to 8 online, so each child just turns to a different page.
- Open investigation: one printed task per lesson with a tutor model answer and "look for" notes in the guide answer key.
- Reflection "What was hard?": 3 prompts (hardest part / got unstuck by, with tick boxes / next time), one closing slide (`p4lK-reflect`, last slide; in L10 just before the certificates slide), 2 tutor-script lines plus a lesson-specific modelled example (1 minute, share one, never graded, praise strategy not speed).
- Timing: opening 0-1, check 1-4, game 4-6 (one short round), quick questions 6-8, exit ticket 85-88, reflection 88-90 (L10: 88-89, then certificates). Deck labels, title notes, tutor guide and routine table updated to match.

| L | Open investigation (type) | Verified claim |
|---|---|---|
| 1 | Bus meeting times (what if / find all) | 6 pairs of gaps in 2..12 meeting at 12 min; lcm table |
| 2 | Double rounding (always true?) | False: breaks exactly for last three digits 450-499 (5 000 numbers below 100 000) |
| 3 | Make targets 1-12 from 2,3,4,5 (find all, swap) | All of 1-20 reachable; 12 model sentences evaluated |
| 4 | Sharing 24 stickers (what if) | Whole-number unit fractions of 24: 1/2,1/3,1/4,1/6,1/8,1/12; smallest set for 1/2..1/6 is 60 |
| 5 | Between two decimals (always true?) | 9 three-place decimals between 0.35 and 0.36 |
| 6 | Splitting a corner (find all) | 7 sets for 90 in 10s; 3 sets for 180 in 30s |
| 7 | Bigger area, bigger perimeter? | False (1x11 vs 4x4); 6 rectangles of perimeter 24 |
| 8 | Row of four net (always true?) | True: all 16 placements fold (cube-folding simulation); 0 of 6 with both squares on one side; 11 cube nets confirmed |
| 9 | Three plants (what if) | Tables, B always 10 above A, C meets B in week 5 |
| 10 | Ring toss 3 and 5 (find all) | Impossible: 1,2,4,7 only; with 4 and 6 only 2 and odd |

Warm-up check answers are also checked in docs/audit/verify_close_gaps_p4.py (prints "all ok").

## Page and slide counts (before to after)
- Student workbook: 47 to 57 (+1 page per lesson, a new last page "Open investigation and What was hard?" holding the fast-track note, the task and the reflection; it could not fit on the full Think Harder/Challenge pages, core pages unchanged at 2).
- Tutor guide: 66 to 79. Weekly dose PDF: 25 to 25 (weekly student/tutor splits regenerated). Question bank 28, email pack 12, taster 5, one-pager 1 (unchanged).
- Slides per deck: +2 each (L1 28, L2 28, L3 29, L4 30, L5 29, L6 28, L7 29, L8 28, L9 27, L10 29). No overflow reported by rebuild/preview.py; all speaker notes under 4000 chars. restyle.py run on each deck; build_level.sh 4 and mkextras.py 4 ran (self-check OK).

## Glyph rule (no box/shape characters)
Replaced in P4: L3 mini2 "8 ○ 5 ○ 3 = 37" now "8 ? 5 ? 3 = 37 (each ? is a sign)"; L3 bank "□ + □ × □ − □" now "a + b × c − d" with a, b, c, d as the four numbers; L3 "□ × □ − □ = 30" now "a × a − a = 30"; L5 warm-up "□.□□" (content and slide notes) now "three empty boxes with a decimal point after the first" (the slide already drew real boxes); L5 "3.□5 < 3.42" (bank and Think Harder slide) now "3.A5 < 3.42, A is one digit". My new tick boxes are drawn with CSS, not glyphs. Not changed: the check mark glyph in worked-example text and the L10 logic-grid instruction (not boxes or unknowns); say if you want these replaced too. No missing-digit column puzzles exist in P4, so column_png was not needed.
