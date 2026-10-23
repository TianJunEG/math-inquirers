# Final fixes, Level 1 Term 3 (Lessons 21 to 30): shared-tool and cross-lesson needs

Each fix agent appends one section for its lessons. Lesson-level detail is in `FIXES_T3_LNN.md`.

## Lessons 21 and 22 (Term 3 Lessons 1 and 2): needs outside the lesson files

Lesson fix details: `FIXES_T3_L21.md`, `FIXES_T3_L22.md`.

**Owned by another agent (report only)**

1. `lessons/l20.json` hand-off to Lesson 21 is still wrong (validator WARN on `validate.py 21`): `parent.next_materials` says "Your Term 3 workbook (from your printed term book) for the first lesson" and "A toy or real clock with a face, if you have one (optional)". It must say: your Term 3 book is in the house, tear out the clock page and a grown-up cuts out the 6 clock hands (the 2 faces can stay on the page or be cut), keep the $1 tokens (needed in Lesson 24), a real clock helps. Same edit in the `s-end` slide, the goodbye SAY line and `tutor_prep`. Lesson 21's `tutor_prep` tells the tutor to message families until this is done.

**Shared tools (not edited)**

2. `tools/figs3.py clock_kit`: faces are 46 mm across (spec 80 mm or more, two fit side by side) and the minute hands (39 mm) are longer than the face radius (23 mm), so a laid hand overhangs the face; hands have no centre dot; cut outlines are 2.5 mm and 3.7 mm apart (rule: 6 mm); the line "Lay a hour hand and a minute hand on a face, with the ends" is clipped at the right edge ("the enc") and should read "an hour hand"; the heading says "cut out both" (faces) while the contract counts 6 pieces. Suggested sizes: faces 80 mm, minute hands about 36 mm, hour hands about 24 mm.
3. `tools/figs3.py event_cards` (Lesson 22): the mat is two boxes about 70 x 55 mm, smaller than four 34 x 33 mm cards, so cards cannot sit in them; headings are cut off ("a.m. (night", "p.m. (aftern") and print a.m. and p.m. with full stops (lesson text is am and pm); the card outlines are 3.4 to 3.9 mm apart; `lab[:12]` truncates the heading. The lesson data now gives every card a time label (shortened to fit 156 units); make the mat boxes about 85 x 100 mm each, label them "am (night and morning)" and "pm (afternoon and evening)", and print "We use them again" only if a later lesson does (none does).
4. Time answer boxes `digital: "[]"` print about 10 x 4.5 mm; "10:30" needs about 22 x 9 mm (Lessons 21 and 22 S1, T1, E1).
5. Exit ticket sits on workbook page 5 with the Investigation and look-back at a smaller type size and with 20 to 27 mm clocks; a half-page exit ticket with 35 mm clocks and a 45 mm drawing face would fix the repeated finding. Raising the clock sizes in lesson data spills the look-back onto a seventh page (tried and reverted in Lesson 21).
6. Deck: `s-ws1` and `s-ws2` (S2 and S6 cards) touch the footer line; the `qs` rows on `s-exit` draw the clocks about 65 px wide (125 px at 1080p); `size` on clocks inside `qs` rows is ignored.
7. `tools/b_guide.py`: the timing assumptions line still prints "papers to the camera 30 s" (default 9 says no paper hold-ups).
8. Runner: "4-5-6" is read as 4, minus 5, minus 6 (treat a hyphen between digits as a separator or say "Use commas"); non-digit input in set and box items says "Type or choose an answer first" instead of the digit message used by number items; a minute above 59 has no range hint.
9. Answer key header reads "Lesson 1, What Time Is It?" and "Lesson 2" without "Term 3" (the workbook, home and parent headers do say "Term 3 . Lesson N").

## Lessons 25 and 26 (Term 3 Lessons 5 and 6): needs outside the lesson files

Details: `FIXES_T3_L25.md`, `FIXES_T3_L26.md`.

1. `tools/figs2.py` icon `ball` reads as a globe: redraw (panels or stripes). L25 and L26 now use a jar and other items; `lessons/l24.json` (not mine) still pictures a ball.
2. `tools/figs3.py price_tags`: 6 mm gaps between cut cells, centre the grid, larger tags (page 15% empty).
3. `tools/b_guide.py`: remove "papers to the camera 30 s". `tools/b_print.py`: rewind label "Practice from earlier: Term 1 Lesson N" on Term 3 child sheets; look-back check boxes wrap; no figures on the home sheet.
4. `qs` slides show table and bar-model thumbnails too small (L25 S2, L26 S6): size option.
5. Runner: "Term 3" in the sub line; a `set`/list item for "which two tags cost exactly $N" and "list every way" (L25 and L26 online).
6. L24 hand-off to L25 (price tags) checked true; `l26.json` hand-off to L27 now names the last page of the Lesson 27 workbook.

## Lessons 27 and 28 (Term 3 Lessons 7 and 8): needs outside the lesson files

Lesson fix details: `FIXES_T3_L27.md`, `FIXES_T3_L28.md`.

**Owned by another agent (report only)**

1. `lessons/l20.json` hand-off to Term 3 (clock page cut out by a grown-up, $1 tokens kept): still not corrected; reported in both lessons.
2. `l30.json` Quest gate for Lesson 27 (a 3 by 3 grid with five boxes filled) and for Lesson 28 (triangles 3, 5, 7 sticks): the numbers and grids must differ from the class and workbook ones (`verify/l27_checks.py` lists every Lesson 27 grid).

**Shared tools (not edited)**

3. `tools/figs3.py grid_tiles` (Lesson 27): mat 2 (4 by 4) loses its last column (the table is wider than the page, 3 columns and a stump); tile cut cells 2.7 mm apart (rule 6 mm, page 62% full, so tiles can be 22 mm with 6 mm gaps).
4. `tools/figs3.py stick_strips` (Lesson 28): strips 6 mm tall with 3.7 mm between cut cells; make 8 mm strips and 6 mm gaps (page about 50% full). `stick_pattern`: collinear sticks merge into single lines in print, deck and online; draw each stick as a separate bar with a small gap or alternating tone, at least 25 mm tall.
5. `tools/b_print.py`: kit sentence "We use them again" is wrong for the grid tiles and the strips (no later lesson uses them); home practice items cannot carry a picture (Lesson 27 H3 and H4 need a small grid, Lesson 28 H3 and H4 a stick picture); look-back boxes wrap and orphan "I would like to pass".
6. `tools/b_guide.py`: timing assumptions still print "papers to the camera 30 s".
7. `tools/b_deck.py`: a one-column `panel` is drawn at the full slide width (it cannot show a column of tiles); the tiny box label in `panel` cannot be enlarged; `qs` rows draw table thumbnails far too small (Lesson 28 slides s-ws1 and s-ws2: the tables are now repeated large as separate blocks).
