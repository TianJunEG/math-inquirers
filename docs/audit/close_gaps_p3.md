# P3 close-the-gaps: reflection, pre-check / fast track, open investigation

Scope: P3 files only (`p3/*`, `p3/content/*`, `rebuild/gen_p3l*.py`, new `rebuild/p3_gifted.py`, new `p3/gifted.json`). No shared file touched (`levels/*`, `rebuild/slidekit.py`, `hp/*` unchanged). Nothing committed or published.

## How it is built
- `p3/gifted.json` holds, per lesson: the 2 Warm-up check questions (answer and "listen for" reason), the Investigation (intro, parts, optional table or figure, tutor model answer) and the lesson-specific "hardest part" tick options. `docs/audit/mkgifted_p3.py` regenerates it.
- `p3/workbook_html.js`: Fast track note under each lesson header; pointer line on the Think Harder page; one new page per lesson, "INVESTIGATE AND LOOK BACK", with the Investigation and the "Look back: What was hard?" box (3 prompts, glyph-free drawn tick boxes).
- `p3/guide.js`: per lesson, a Warm-up check block in the warm-up (minutes 2-5; game moves to 5-10), a "Running the fast track" block, a Look-back block in the exit-ticket segment (say lines, share one, never grade, praise strategy not speed), and the check answers and Investigation model answer in each lesson's key. A program-level paragraph explains the three routines.
- `rebuild/p3_gifted.py` (called from each `gen_p3lK.py` before the slides are written): adds the `warmcheck` slide (2-5 min, after the title) and the `reflect` slide (88-90 min, last), re-times the warm-up game slides (5-8 and 8-10 min) and updates the title-slide time plan. 2 slides added per lesson (the limit).

## What was added to every lesson
| L | Warm-up check (2 questions, new setting) | Open investigation (printed) | Type |
|---|---|---|---|
| 1 | stickers in boxes/packs/bundles; smallest odd number from 4, 0, 9, 3 (3049) | cards 1,2,3,4 vs 0,1,2,3: 24 vs 18 numbers, what stays the same | what if we change |
| 2 | working back from 4000; missing digit A in 3A47 + 2865 = 6212 | reverse a 3-digit number and subtract: always 99 x (first - last) | is it always true |
| 3 | which numbers are in the 7 table; 6 x 14 and 6 x 6 from 6 x 7 | digit sums in the 9, 3, 6, 4 tables (9 x 11 = 99 is a counterexample) | is it always true |
| 4 | give half the difference; pen and book $9, $5 apart | Mei 13, brother 5: table of ages, double and triple | what stays the same |
| 5 | number from 7 x 5 + 4; impossible remainders for 6 | 3 numbers in a row, exactly one in the 3 table; 4 in a row; 2 in a row | is it always true |
| 6 | 1/4 vs 1/3 misconception; eighths in 3/4 | all ways to make 3/4 from 1/2, 1/4, 1/8 (6 ways); then 1 whole (9) | find all the ways |
| 7 | area from perimeter 14 and side 3; same area, different perimeters | square to (n+1) by (n-1): perimeter same, area down 1 | what if we change |
| 8 | right angles in the two triangles from a diagonal; parallel and perpendicular | staircase corners: right angles = steps + 3, dents = steps - 1 | find the pattern |
| 9 | 2 kg 40 g vs 2400 g; film 15:50 + 1 h 25 min | all ways to pay 50 cents with 5c, 10c, 20c (12 ways) | find all the ways |
| 10 | orders with Ben in front of Mei; reading a bar scale | handshakes: 1, 3, 6, 10, 15; 10 friends = 45; 20 impossible | draw it, list it, table |

Fast track (true to the program: live online groups of 8, tutor may give children different pages): both answers right AND can say why, then the child starts Think Harder and the Investigation at minute 40 while the group works the core pages; they still join explore and mini-lesson; check-in at about minute 52; back together for talk time; nobody labelled; the check decides again every lesson. Core stays manageable without the fast track (nothing was removed or moved off the core pages).

## Page and slide counts (before, after)
| Item | Before | After |
|---|---|---|
| Student workbook | 48 | 58 (+1 page per lesson: the Investigate and Look back page; it could not fit on the Challenge page, which only has about a quarter of a page free) |
| Per lesson workbook pages (core, Think Harder, Challenge, new) | 4 | 5 |
| Tutor guide | 60 | 75 |
| Weekly pack (zip, Weekly Dose PDF) | 25 | 25 |
| Slides per lesson | 27, 26, 26, 26, 26, 26, 25, 25, 26, 27 | each +2: 29, 28, 28, 28, 28, 28, 27, 27, 28, 29 |

Week packs now carry 16/10/10/10/11 student pages (incl. journal, cut-outs and certificate in weeks 1 and 5).

## Verification
- `python3 docs/audit/verify_gifted_p3.py` brute-forces every claim: ALL PASS (see the script for each line). Examples: L1 counts 18 and 24 and the start-with-1 list; L2 reverse-subtract equals 99 x (first - last) for every 3-digit number with first > last; L3 digit sums (9 x 11 = 99 gives 18, so "always 9" is false; the 3, 6, 9 tables always give a multiple of 3; the 4 table does not); L4 double only in 3 years, triple only 1 year ago; L5 exactly one multiple among n consecutive numbers (n = 3, 4) but not for 2 and 3; L6 6 ways for 3/4 and 9 for 1 whole; L7 perimeter same and area exactly 1 less for sides 2 to 499; L8 staircase counts by constructing each polygon; L9 12 ways, fewest 3 coins, most 10; L10 handshakes.
- Decks regenerated with `rebuild/gen_p3lK.py`, then `python3 levels/restyle.py split/p3lK` for K = 1..10; `rebuild/preview.py` reports no OVERFLOW on any slide; no slide notes over 4000 characters (max 1295 in the new slides); element counts under 200.
- `bash levels/build_level.sh 3` and `python3 levels/mkextras.py 3` run clean (P3 self-check OK). No unicode box or shape glyph in any P3 PDF, zip, slide or source file.

## Extra rule: no unicode box or shape glyphs (coordinator message)
Replaced in `p3/content/l2.js`, `rebuild/gen_p3l2.py` (about 140 instances of box, circle, triangle, diamond and star glyphs, all in L2) and the optional-question star (L1, L6):
- Missing digits written as a box in text now use letters A, B, C, D (for example 3A82 + 14B9 = 5141) in questions, scripts, hints, keys, notes and the question bank.
- Shape-code puzzles now use letters: AB + B = BA (A = 8, B = 9); AA + BB = CBC (9, 2, 1); AA + BB + CC = ABC (1, 9, 8); ABC - CB = CAB (7, 3, 6); ABC + ACB = CBA (4, 5, 9, the 459 + 495 = 954 puzzle); the workbook Q6 puzzle is AB + AB + AB = CAB; the teach-shape slide is AB + BA = CAC.
- Slides: the exit-ticket sum, the teach-shape slide and the Challenge "see it" slide use `levels/diagrams.py column_png` PNGs (embedded as data URIs); the teach slides for missing digits use drawn letter tiles in the existing SVG column sums (shape drawings removed).
- "(if time)" markers: the star glyph was dropped in L1, L2 and L6 (the page text already says "if time").
- The 4-by-4 empty-box figures on slides and the workbook column sums (drawn rectangles) were kept: they are drawings, not glyphs.
