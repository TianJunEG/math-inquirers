# Closing three gifted-style gaps: Math Inquirers P2

Brief: `docs/audit/close_gaps_p2.txt`. P2 files only. Nothing committed. Shared files (`levels/*`, `rebuild/slidekit.py`, `hp/*`) not edited.

## What was added (every lesson 1 to 10)

Single source for the new content: `p2/gaps.json` (read by `p2/data.js`, `p2/workbook_html.js`, `p2/guide.js` and, through the new helper `rebuild/p2gaps.py`, by all ten `rebuild/gen_p2lK.py`).

| Gap | Workbook | Deck | Tutor guide |
|---|---|---|---|
| (a) Reflection "What was hard?" | Last Think Harder page: a box with tick faces (easy / OK / tricky), "The hardest part was ...", "I got unstuck by ..." (4 tick options per lesson), "Next time I will try ...". Replaces the older plain "Look back" lines. | Slide `p2lK-reflect`, minutes 88 to 90, after the exit ticket | Segment "88 to 90: What was hard? and closing": 2 script lines (SAY: 1 minute, no marks; DO: share one, never grade, praise strategy not speed) |
| (b) Pre-check / skip-ahead | A "FAST TRACK" note printed in the lesson header band on the first worksheet page | Slide `p2lK-precheck`, minutes 1 to 4: 2 questions in a new setting; answers on click; notes say how to run it | Segment "1 to 4: Warm-up check": SAY line, 3 DO lines (how to run, who goes fast track, nobody labelled), a table with answers and what to listen for |
| (c) Open investigation | Q8 on the Challenge page, "Open investigation: ..." | Not a slide (workbook task); the fast-track children use it | Table "Open investigation" with model answer and what to look for, plus a Q8 line in the lesson's answer key |

How the fast track fits the program (groups of up to 8, online): the check is at minutes 1 to 4; a child who gets both right and can say why works on the Think Harder pages and Q8 from minute 36 (own breakout room, or on the main screen with the tutor visiting at about minute 40) while the group does the core pages; a right answer without a reason stays with the group; nobody is labelled; children can move either way at any time; everyone still joins explore, the mini-lesson, the check-together slides and talk time. The Core page is still manageable without prior teaching (tier principle unchanged).

Timing changes (deck and guide): opening 0 to 1, warm-up check 1 to 4, warm-up game 4 to 6 (2 minutes), quick questions 6 to 8 (use questions 1, 3, 5 if short), exit ticket 80 to 88, reflection 88 to 90. The title-slide time plans were updated.

## Per lesson

| L | Warm-up check (Q1, Q2) | Open investigation (Q8) | Verified by brute force |
|---|---|---|---|
| 1 | 4, 0, 7 digit cards, how many numbers (4); "5 hundreds 13 tens" is 630 | Mirror numbers: all from 200 to 299 (10); are they all odd? (no) | 10 mirror numbers 200-299; 90 in 100-999; cards 4,0,7 give 407, 470, 704, 740 |
| 2 | 4A6 + 237 = 683 (A = 4); 300 + 150 = 290 + B (160) | Odd or even? odd+odd, odd+even, even+even, and with subtraction | parity rule for all 3-digit pairs (add and take away) |
| 3 | cars and scooters, 6 toys 16 wheels (2 and 4); 4 rows of 5 with 2 rows covered (10) | Where tables meet: 2 and 5 (10..50), 3 and 5 (15, 30, 45), 4 and 5 (20, 40); in both 2 and 5 tables is the 10 table | all three lists; "in both 2 and 5 means in 10 table" up to 100 |
| 4 | 22nd shape of a group of 4 (moon); rows 3, 7, 11 gives row 6 (23) | Three counting patterns start 1, 2, 3 add 3: every number in exactly one; with add 4 need 4 | partition of 1-99 into the 3 patterns |
| 5 | ÷ 2 then + 7 gives 12 (IN 10); add 8 then halve gives 9 (10) | Magic trick (n+5, double, -10, halve) always returns n; make your own | identity for 1-999 |
| 6 | change from 85¢ (10¢ + 5¢); 3 drinks $1.60, $5 (enough, 20¢ left) | Most coins with 5¢, 10¢, 20¢, 50¢: 85¢ and 95¢ need 4 | fewest-coin table for 5¢ to 95¢ (dynamic programming) |
| 7 | 1/5 or 1/8 of a prata (1/5); 3/8 + 2/8 eaten, left (3/8) | Fraction strips: cover 1/2 with one kind (quarters 2, sixths 3, eighths 4), 1/3 (sixths), 1/4 (eighths); thirds never cover a half | exact fractions |
| 8 | stack 5 by 2 plus 3 on top (13); 2 semicircles + 1 quarter in quarters (5) | Squares joined edge to edge: 3 squares give 2 shapes, 4 squares give 5 (turns and flips the same; 7 if flips count) | shape enumeration: 1, 1, 2, 5 (12 for 5 squares) |
| 9 | melon = 2 apples = 6 plums (6); 5 ℓ and 2 ℓ jugs make 1 ℓ | Weights puzzle: sets of three from 1-5 g that make every mass 1-6 g: exactly {1,2,3} and {1,2,4} | all 10 sets |
| 10 | 9 shapes, 31 sides (4 squares); snail in a 7 m well (day 3) | Staircase of 1 or 2 steps: 1, 2, 3, 5, 8 ways; 6 steps 13 | enumeration of step sequences |

Also checked: jug reachability for L9 Q2 (BFS), L1 Q1 (permutations), L8 shapes (rotation and reflection normalisation), L10 sides and snail (loops).

## Unicode box and shape glyphs (extra rule from the lead)

No box, circle or star glyph remains in P2 source or in any built P2 PDF (searched for the box, black square, circle, star, triangle and diamond characters).
- L2: all 55 box glyphs in `p2/content/l2.js` and 71 in `rebuild/gen_p2l2.py` (scripts, notes, key text, question bank, slide text) replaced by letters A to E (for example 4A7 + 28B = 723, 245 + 130 = 200 + E, "AB7 + 4CD = 1000"). The L2 workbook and slide column sums were already drawn pictures (SVG yellow boxes), not glyphs, so they were left as they are.
- L5: the two number-machine SVG pictures that printed a box glyph now print the letters A and B.
- L10: the box in the relay card and answer notes became the letter A; the picture-graph dots and stars in the station card, Challenge items and question bank became the word "picture" ("each picture stands for 5 books").
- `levels/diagrams.py` `column_png` was not needed because the existing figures are already vector pictures.
The check mark in a few notes is not a box or shape glyph and was left.

## Page counts (before / after)

| File | Before | After |
|---|---|---|
| Student workbook | 52 | 52 (every lesson has the same number of pages as before: 5, 5, 4, 4, 4, 4, 4, 4, 4, 4) |
| Tutor guide | 63 | 80 (warm-up check, investigation and reflection per lesson) |
| Weekly Dose | 24 | 24 |
| Question Bank | 25 | 25 |
| Weekly email pack | 12 | 12 |
| Free taster / What Learners Get | 5 / 1 | 5 / 1 |
| Decks (slides) | 25, 26, 26, 25, 26, 26, 27, 27, 26, 31 | 27, 28, 28, 27, 28, 28, 29, 29, 28, 33 (plus 2 each) |

To fit the workbook, Challenge answer lines were cut from 4 to 3 (2 in lessons 4, 5, 8, 10), the Think Harder spacing was tightened a little, and the fast-track note sits in the empty right side of the lesson header band. The new Q8 has 2 answer lines (children use scrap paper for the rest; in L8 a drawing grid replaces them).

## Verification
- All ten decks regenerated with `rebuild/gen_p2lK.py`, restyled with `python3 levels/restyle.py split/p2lK`, rendered with `rebuild/preview.py`: no OVERFLOW lines; all notes at most 4000 characters.
- `bash levels/build_level.sh 2` and `python3 levels/mkextras.py 2` ran clean ("P2 self-check: OK").
- Warm-up check, Fast Track and "What was hard" appear 10 times each in the guide and workbook text (once per lesson).

## Not done / for the lead
- `levels/mkextras.py` requires every answer-key row to be named Q1, Q2, ..., so the investigation model answer is printed in the guide (as "Q8" and in its own table) and not added to `lesson.key`.
- The helper `rebuild/p2gaps.py` and `p2/gaps.json` are new P2 files; other levels could reuse them with their own gaps file.
