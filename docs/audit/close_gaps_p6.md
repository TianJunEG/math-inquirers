# Close three gifted-style gaps: P6 (age band 11-13)

Date: 2026-10-22. Nothing committed. No shared file edited (`levels/*`, `rebuild/slidekit.py`, `hp/*` untouched).

## What was added to every one of the 10 lessons

1. **Reflection "What was hard?"**: a boxed block at the end of the last workbook page of each lesson with three short-write prompts ("The hardest part was", "I got unstuck by", "Next time I will try"); one closing slide (`p6lK-reflect`, after the exit ticket); in the tutor guide, a SAY line and a DO line in the Exit ticket section (1 minute, share one sentence, never grade it, praise strategy not speed, with a lesson-specific example such as "you counted the jumps").
2. **Warm-up check / Fast track**: a 3-minute check of two new-setting questions on the lesson's key idea (answer plus a reason) as slide `p6lK-check` (right after the title, answers on click), with full answers in the tutor guide Warm-up section. Printed "FAST TRACK" note at the top of the first Think Harder page, plus a one-line pointer in the header of worksheet page 1. The tutor script explains: the 3 minutes come out of the 10-minute warm-up; read every board; a child with both right and a sensible reason gets a private chat message and starts on the Think Harder pages at minute 40 (still joins Explore, mini-lesson, Talk time); nobody is announced or labelled, it is not a mark, any child may choose the main pages, a stuck child goes back. This matches how the programme runs (groups of up to 8 online, printed workbook, tutor can give different children different pages).
3. **Open investigation**: one box at the end of the second Think Harder page (after the existing problem-posing item), with the model answer and "look for" notes in the tutor guide (Stretch and challenge table, and an "Investigation" line in each lesson's answer key).

Data lives in `p6/content/gaps.json` (read by `p6/data.js`, `p6/guide.js`, `p6/workbook_html.js` and `rebuild/p6_gaps.py`). Each `rebuild/gen_p6lK.py` now ends with `p6_gaps.apply(K)`, so regenerating a deck gives the complete deck.

## Per lesson

| L | Warm-up check (answers) | Open investigation (type) |
|---|---|---|
| 1 | Taxi $3 + $2 per km, 20 km (43); is 50 in 7, 12, 17, ... (no) | What if we join squares, pentagons, hexagons in a row? Sticks = (k-1)n + 1 (what changes / stays the same) |
| 2 | 31 children in equal teams (prime, no); 36 vs 37 factors (9 vs 2) | Is "two different primes never add to a prime" always true? No: 4 pairs below 20, all use 2 (is it always true) |
| 3 | Freezer -18 vs fridge 4 (22); sprite -40, +25, -60 (-75) | Find all pairs from -5, -3, -1, 0, 2, 4, 6 with a - b = 7 (3 pairs); then 3 (2 pairs) (find all) |
| 4 | Phone plan 3n + 10, 7 GB (31); cost 52 (14 GB) | All "x a, + b" machines (a 1-9, b 0-9) with IN 4 OUT 17 (3); OUT 21 (3) (find all) |
| 5 | Café 3x4x2 (24); 5 chess clubs (10, not 20) | Pay 50c with 5c, 10c, 20c coins: 12 ways (13 with a 50c coin) (find all) |
| 6 | Spinner 3 red 5 blue (5/8, unfair); two coins match/differ (fair) | "Two outcomes means fair": coin, six/not six, total 7/not 7 (only the coin is fair) (is it always true) |
| 7 | 40 degree turns (9 corners); 90, 120, 60 then ? (90) | Table of repeats and rounds for t = 40, 72, 90, 100, 120, 144, 150; turns = 360 x rounds (what changes / stays the same) |
| 8 | 8 o'clock + 30 h (2 o'clock); Wednesday + 100 days (Friday) | Shift a then 26 - a undoes (CAT-KIB-CAT); only shift 13 is its own decoder (is it always true / find all) |
| 9 | Mean 10, three numbers known (10); pocket money with an outlier (median/mode) | 4, 6, 7, 9, 14: change the 14 to 24, 4, 7; mean always moves, median sometimes (what if / what stays) |
| 10 | 4, 9, 14, 19: is 2026 a term (no); ordered 2-letter codes from 4 letters (12) | Primes in 7n - 3 up to 100: 11, 53, 67; why never a multiple of 7 (find all) |

## Verification

`python3 docs/audit/verify_gaps_p6.py`: all checks OK. Every "find all" count and "always true" claim is brute-forced (28 prime pairs and the "must contain 2" claim to 200; 3 and 2 pairs for the differences; 3 and 3 machines; 12 coin ways; fair/unfair games by listing 36 outcomes; repeats and rounds for 7 turn angles; the only self-decoding shift is 13 and shift a then 26 - a returns every letter; mean/median/mode table; primes in 7n - 3). `python3 docs/audit/verify_gifted_p6.py` still passes.

## Extra rule: no box or shape glyphs

Replaced the two existing instances in P6: Lesson 10 workbook "Ready to show?" checkboxes (three ballot-box glyphs) became "[  ]"; Lesson 4 challenge diagram (`rebuild/gen_p6l4.py`, machine boxes drawn with a square glyph) now labels the unknowns with the letters A and B in the drawn boxes. No new glyphs were added (grep of content, scripts, generators and all 280 slide files finds none). No missing-digit puzzles exist in P6, so `levels/diagrams.py` was not needed.

## Page counts (before = after the earlier gifted-fix pass)

| File | Before | After |
|---|---|---|
| Student workbook | 45 | 45 |
| Tutor guide | 71 | 82 |
| Weekly Dose of Thinking Math | 25 | 25 |
| Question Bank | 28 | 28 |
| Weekly Email Pack | 12 | 12 |
| Free Taster | 5 | 5 |
| What Learners Get | 1 | 1 |

Workbook: no page added. To make room, Think Harder answer lines were cut (Stretch 3 to 2 lines; Challenge 5 and 6 from 4 to 2, Challenge 7 from 4 to 3). Tutor guide: +11 pages, from the warm-up check table, fast-track instructions, reflection lines and the investigation answer in each lesson. Decks: 2 slides added per lesson (26, 26, 25, 26, 26, 27, 27, 27, 26, 25 becomes 28, 28, 27, 28, 28, 29, 29, 29, 28, 27).

Decks regenerated with `rebuild/gen_p6l1.py` to `gen_p6l10.py`, each followed by `python3 levels/restyle.py split/p6lK`. The new slides were rendered at 1920 x 1080 and checked: nothing below y 920 (excluding the footer), no overlap. Then `bash levels/build_level.sh 6` and `python3 levels/mkextras.py 6` (self-check OK).

## Caveats

- The 3-minute check is taken from inside the 10-minute warm-up (game cut to about 3 minutes, first three quick questions only); slide time labels on the older warm-up slides still say 0-5 and 5-10.
- The reflection box is on the last page of each lesson (the Challenge page), so the tutor says "last page of today's lesson"; children who never reach the Think Harder pages still turn to it.
- Lesson 10 has its own timing plan; the check and reflection use the same 3 and 1 minutes.
