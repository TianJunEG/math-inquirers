# Independent audit: Primary 6 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent (not the builder). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`. Nothing was pushed, no PR, no builder file edited; only this report was added.
Subject: `school/p6/out/P6_S1_*` and `P6_S2_*` (Puzzles 20 pp, FrontMatter 5 pp, Complete_Pack 25 pp, Answer_Key 9 / 10 pp). Read first: `docs/school_books/p6_semester_booklets_build_report.md`, `p6_semester_booklets_plan.md`, `p6_outcome_wording.md`, `school/p6/README.md`, `docs/moe/syllabus_by_level.md`, `docs/school_books/plan.md`, `docs/terms/owner_decisions.md`, the P1 and P2 audits, and `school/p6/out/validation_report.txt`.

Method. All 40 pupil pages were rendered from the PDFs (110 dpi colour; 150 and 200 dpi 1-bit for every figure page, grids, dominoes, nets, pie and the three colour pages) and **solved by hand from the image before the key was read**; then compared with the key. The net page was also checked with my own rolling-cube fold script. Code words and every choice, matching, ordering and domino page were tested with **my own word lists**: python `english-words` 2.0.2 (web2 + gcide, 262 866 entries) joined with `wordfreq` top 250 000 (227 384 alphabetic entries), union 426 367 entries. This union is stricter than the builder's 207 399-word list because it holds proper names, slang and rare words; a hit is therefore judged by hand. Photocopy behaviour: 1-bit renders (poppler `-mono`) at 150 and 200 dpi, stroke widths and text sizes from the PDF (PyMuPDF), and box sizes measured from the PDF paths. Similarity: my own 5-word-run and number-scenario passes against `docs/books/private_*` (20 828 entries) and `docs/sasmo/private_*`, and against `p6/content/*.js` and `extension/data/l6_*.json`. The MOE syllabus PDF is not in the repository; Primary 6 outcomes are taken from `docs/moe/syllabus_by_level.md` only.

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **Content ready after two small fixes** (M2 for P6-20 figures O and E; M3 key outcome numbers). No wrong key, no ambiguous or unsolvable page apart from M2. Still DRAFT by the owner's rule (lawyer, pupil trial, photocopier). |
| Semester 2 | **Content ready after four fixes** (M1 angle figures drawn to scale; M2 arch figures P6-21 item 2 and P6-22 item 4; M3; M4 label collisions on P6-27/28). No wrong key. Seven of 20 pages are Primary 4 and 5 revision (owner decision 1). Still DRAFT. |

**No High.** 40 of 40 pages solved from the image and agree with the key (0 wrong keys, 0 unsolvable, 0 with two answers). All 33 code words are different and no other real word is reachable by a rearrangement or a single slip (details in section 2). Front matter follows the owner decisions (section 6).

## 1. Hand-solve of all 40 pupil pages (from the image, then compared with the key)

| Page | My answer from the image | Result |
|---|---|---|
| S1-01 P6-01 Fraction Shares | 2/25 C, 3/13 R, 1/27 E, 2/15 A, 5/27 M, 3/56 Y: CREAMY | agree |
| S1-02 P6-02 Dividing by Fractions | 16 divisions worked; boxes equal to 6: route (1,2) (1,3) (2,3) (3,3) (4,3) (4,2) (4,1) (3,1), 8 boxes; (1,4) and (4,4) dead ends; route unique | agree |
| S1-03 P6-03 Fraction Stories | 2 M, 2/9 O, 9 N, 1/10 K, 3 E, 5 Y: MONKEY | agree |
| S1-04 P6-04 Equal Ratios | S (4:7:6), H (5:3), R (7:9), I (5:8), M (9:8:2), P (4:9): SHRIMP; X and F unused | agree |
| S1-05 P6-05 Missing Terms | 48 T, 15 E, 9 A, 54 C, 27 U, 44 P: TEACUP | agree |
| S1-06 P6-06 Share in a Ratio | 12 B, 16 A, 20 N, 30 D, 147 I, 70 T: BANDIT | agree |
| S1-07 P6-07 Three Quantities | 2:7:4 D, 7:5:1 E, 5:6:2 V, 1:2:2 O, 6:4:3 U, 4:1:3 R: DEVOUR | agree |
| S1-08 P6-08 Fractions and Ratios | 4:1 F, 2:7 A, 1/6 T, 7/12 H, 3/8 O, 3:4 M: FATHOM | agree |
| S1-09 P6-09 Colour the Car | 60 O, 60 O, 60 O (stars), 36 B, 36 B (squares), 12 Y, 12 Y (dots), 45 G x3 (mid, two wheels), 20 R x3 (crosses). Tally Y2 R3 B2 G3 O3 and all five mark pairs match the strip | agree |
| S1-10 P6-10 Find the Whole | 640 F, 160 R, 190 U, 660 I, 360 T, 480 Y: FRUITY | agree |
| S1-11 P6-11 Percent Up and Down | 25% increases only; route (2,2) (1,2) (1,3) (1,4) (2,4) (3,4) (4,4) (4,3), 8 boxes; (1,1) and (3,2) dead ends; the "Down" 25% boxes are traps; unique | agree |
| S1-12 P6-12 Percent Stories | 5 S, 400 Q, 30 U, 420 A, 320 R, 340 E: SQUARE | agree |
| S1-13 P6-13 Letters for Numbers | k÷3 S, n+4 T, 6y U, t-7 D, p-9 I, 8w O: STUDIO | agree |
| S1-14 P6-14 Simplify | 14p+12 W, 6a+5 A, 14k+14 L, 5y+12 R, 5w+5 U, 7t+12 S: WALRUS; J and X unused | agree |
| S1-15 P6-15 Substitute | values: A 48 / 18, B 53 / 40 (START), O 40 / 17, T 17 / 48, N 18 / 39, Y 39 / 53; loop B O T A N Y closes: BOTANY | agree |
| S1-16 P6-16 Find the Letter | w=6 C, p=26 R, k=2 A, n=29 F, y=3 T, t=23 Y: CRAFTY | agree |
| S1-17 P6-17 Round and Round | 22/7: 176 C, 88 O, 154 U, 22 S, 66 I, 44 N: COUSIN | agree |
| S1-18 P6-18 Circle Areas | 3.14: 50.24 F, 153.86 R (r from C = 43.96), 200.96 O, 314 Z, 12.56 E, 28.26 N: FROZEN | agree |
| S1-19 P6-19 Half and Quarter | 19.25 H, 38.5 U, 25 N, 72 G, 100 R, 308 Y: HUNGRY; S and Q unused | agree |
| S1-20 P6-20 Curves and Corners | P 42, O 68.25 (reading "7 cm" as the side of a square), L 94.5, I 371, C 385, E 614.25: POLICE | agree (see M2) |
| S2-01 P6-21 Shaded Shapes | 1036 S, 273 U (square reading), 42 N, 476 D, 64 A, 56 Y: SUNDAY | agree (see M2) |
| S2-02 P6-22 Perimeter Pick | 100 W, 76 A, 54 L, 64 N (square reading), 142 U, 25 T: WALNUT | agree (see M2) |
| S2-03 P6-23 Cuboid Corners | 8 C, 14 O, 5 U, 11 G, 12 A, 15 R: COUGAR | agree |
| S2-04 P6-24 Roots and Edges | boxes equal to 6; route (1,2) (2,2) (3,2) (4,2) (4,3) (4,4) (3,4) (2,4), 8 boxes; (1,3) and (2,1) dead ends; unique | agree |
| S2-05 P6-25 Base and Height | 45 cm² C, 52 cm² A, 9 cm N, 14 cm O, 6 cm P, 49 cm² Y: CANOPY; Z and F unused | agree |
| S2-06 P6-26 Tank Stories | 64 M, 21 A, 8 G, 30 N, 40 E, 18 T: MAGNET | agree |
| S2-07 P6-27 Angles in Figures | 120 P, 85 E, 136 A, 22 N, 122 U, 80 T: PEANUT | agree |
| S2-08 P6-28 More Angles | 36 S, 54 P, 64 O, 15 N, 75 G, 24 E: SPONGE | agree |
| S2-09 P6-29 Angle Match | 129 S, 70 T, 80 R, 90 O, 72 N, 50 G: STRONG; L and K unused | agree |
| S2-10 P6-30 Average | 20 C, 13 U, 29 R, 31 F, 77 E, 30 W: CURFEW | agree |
| S2-11 P6-31 Missing Value | 78 F, 21 A, 35 B, 15 R, 135 I, 45 C: FABRIC | agree |
| S2-12 P6-32 Colour the Butterfly | 36 R, 64 G, 36 R, 72 O (left); 64 G, 36 R, 72 O, 36 R (right); 27 Y, 27 Y; 64 G x2; 48 B x2. Tally Y2 R4 B2 G4 O2; every left/right pair equal | agree |
| S2-13 P6-33 Pie Chart | Badminton 10%; 360 D, 3 O, 140 N, 180 K, 10 E, 40 Y: DONKEY | agree |
| S2-14 P6-34 Net or Not | my fold script: nets 1, 2, 4 fold; 3, 5, 6 do not. F A M I L Y (Yes Yes No Yes No No) | agree |
| S2-15 P6-35 Taps and Rates | 22 N, 405 U, 198 M, 7 B, 120 E, 480 R: NUMBER | agree |
| S2-16 P6-36 Mixed Numbers | S 1 1/9, H 2 1/6, A 2 3/4, D 5 1/4, O 6 2/3, W 6 11/12: SHADOW | agree |
| S2-17 P6-37 Decimal Maze | boxes equal to 2.4; route (4,2) (4,1) (3,1) (2,1) (2,2) (2,3) (1,3) (1,4), 8 boxes; (1,1) and (4,3) dead ends; unique | agree |
| S2-18 P6-38 GST and Discount | GST 9%: 90 T, 20 U, 54 R, 436 K, 36 E, 45 Y: TURKEY | agree |
| S2-19 P6-39 Mixed Bag | values M 4/15, T 38/12, W 12/49 (START), A 24/38, O 49/4, B 15/24; loop W O M B A T closes: WOMBAT | agree |
| S2-20 P6-40 Colour the Elephant | 48 G x4 (ears' top ovals and eyes row), 24 R x2, 60 O x2, 15 Y x3 (ears, ratio box), 35 B x3 (trunk, two bottom boxes). Tally Y3 R2 B3 G4 O2; pairs equal | agree |

Every answer is unique and unambiguous except the arch figures (M2). Decimals, percentages, ratios, GST (9%) and pi values were recomputed; no error found. The nets and the cuboid pages (which edge is `?`) are clear. Colour pages: no strip contradicts a correct colouring (the P2 H1 failure mode is absent).

## 2. Code words (my own dictionaries)

All 33 words are different: CREAMY, MONKEY, TEACUP, SHRIMP, BANDIT, DEVOUR, FATHOM, FRUITY, SQUARE, STUDIO, WALRUS, BOTANY, CRAFTY, COUSIN, FROZEN, HUNGRY, POLICE, SUNDAY, WALNUT, COUGAR, CANOPY, MAGNET, PEANUT, SPONGE, STRONG, CURFEW, FABRIC, DONKEY, FAMILY, NUMBER, SHADOW, TURKEY, WOMBAT. Tests, per page type:

- **19 code-table pages**: all 720 orderings of the six letters; every single slip using any letter on that page's code table; every single slip using any of 26 letters (stricter than needed); every double slip using table letters.
- **5 lettered-choice pages** (P6-03, 08, 13, 22, 34): every one of 3^6 = 729 (P6-34: 2^6 = 64) selections.
- **5 matching pages** (P6-04, 14, 19, 25, 29): every way of giving the six items different cards (8P6 = 20 160 strings).
- **4 ordering or loop pages** (P6-15, 20, 36, 39): all 720 orderings.

Result: **no ordinary English word other than the page's own is reachable by any rearrangement, any single slip, or any choice or card assignment.** Hits found, all judged not real pupil-level words:
- Rearrangements: SQUARE gives `arques` (name) and `sqaure` (misspelling); MAGNET gives `getman`; NUMBER gives `embrun` (a town). None is an English word.
- Single slip with table letters: SUNDAY gives `gunday`, `sanday`, `sundal` (names); NUMBER gives `nummer` (Dutch); TURKEY gives `purkey`, `tuckey` (surnames); SPONGE gives `spooge` (slang, a vulgar word, needs item 4 to carry 64 instead of 15). I would not call it a risk for pupils, but it is the only obscene-sense hit; it can be removed by changing the letter for 64 on P6-28 (L-I).
- Matching: STRONG gives `stronk` (slang). Choice pages and domino/ordering pages: no hit.
- Double slips (two wrong answers at once): common words are reachable on a few pages (CREAMY to CREEPY, NUMBER to BUMPER and JUMPER, COUSIN to COFFIN, CURFEW none, TURKEY to TUCKER and TURRET, DONKEY to DONNED). Each needs two simultaneous wrong answers; the teacher notes already say two wrong answers at once were not all tested, so this is consistent with what is claimed. Not a finding.
- Any distinct-letter string from a code table spells real words on most pages (for example JACKET and PACKET on P6-05); that is not a "wrong placement" and not claimed.
- Builder's report states "about 207 000 words" for the slip test; `validation_report.txt` shows the code-table pages used a 129 000-word list for the single-slip check (19 lines) and the 207 399-word list for the choice and matching pages (L-G). My larger union confirms the result.

## 3. Content: coverage and leakage

- **Coverage.** All 27 Primary 6 outcome lines in `docs/moe/syllabus_by_level.md` (fractions 1.1 and 1.2, percentage 1.1 and 1.2, ratio 1.1 to 1.7, algebra 1.1 to 1.5, circle, semicircle, quarter circle, composite figures, the four cuboid and cube lines, square and cube roots, angles in figures, average) are covered by at least one page. The ratio set (equal ratios, share, three quantities, fraction link) is well spread. No Primary 6 line is missing. Weak spots: S2 has no page on fraction division, ratio or percentage change except the two mixed pages; circles are S1 only.
- **Leakage.** None found. No speed, negative numbers, probability, coordinates, surface area, median or mode, simultaneous equations, brackets with letters, expanding, trigonometry, fractional or decimal ratios. P6-16 item 1 (9w - 14 = 40) and item 2 are two-step equations: the summary says "simple linear equations involving whole number coefficient only", which does not tell me whether two steps are in scope (cannot check, see section 9). The exterior-angle result and the trapezium rule (angles between parallels add to 180) are used on P6-27, 28, 29; trapezium is named in the outcome line, so I treat it as in scope.
- **Speed, pie charts, nets (owner decision 1).** No page uses speed. `docs/moe/syllabus_by_level.md` line 158 says the Primary 6 Foundation syllabus revisits rate, percentage, average and pie charts, so pie (P6-33) and rate (P6-35) are not outside the Primary 6 year; the build report's weak point 3 is slightly understated. Nets (P6-34) and decimals (P6-37) are Primary 4 only; mixed numbers (P6-36), GST (P6-38) and tank/volume (P6-26, 35) are Primary 5. Judgement: acceptable as revision because the keys tag them "Revisits", and Primary 6 Term 3 to 4 is revision-heavy in school. Recommendation under section 8.
- **Notation.** Pi: P6-17, 19, 20, 21, 22 say "Take π as 22/7"; P6-18 says "Take π as 3.14"; no page mixes. Every 22/7 page uses radii or diameters that are multiples of 7, every answer exact. GST is 9% (P6-38, stated on the page). Ratios are written `a : b` and `a : b : c` with spaces on every page. Algebra letters are k, n, p, t, w, y, a (never x), no brackets, `3n` and `k ÷ 3` forms as in the syllabus line. Fractions are in simplest form where stated. Money is `$` with whole dollars. Units ℓ, cm³ consistent.
- **Unique and unambiguous answers.** Fine everywhere, except **M2**.

## 4. Reading load (plan.md table: P6 at most 18 words a sentence, instruction at most 5 sentences)

Longest question sentences: P6-26 item 3 (18 tokens including numbers and units), P6-26 item 5 (16), P6-07 item 6 (15), P6-33 item 2 (14). All others are 14 or fewer. No sentence breaks the 18-word cap. Instructions longer than 5 sentences: P6-22 (7), P6-21, 27, 28, 29 (6 each); each sentence is short (3 to 10 words). Low (L-B). Vocabulary (ratio, equation, hatched, cuboid, perimeter, quotient not used) is suitable for ages 11 to 13. Names are the usual school names; pronouns are consistent.

## 5. Photocopy (1-bit) legibility and layout

No flat grey anywhere (validation: 0 flat blocks; I saw none). Minimum text on the pupil pages is 8.0 pt (footer only). Answer boxes: 8.2 mm squares for letter boxes, 10 to 12 mm for answer boxes, 24 x 10 mm and larger for the wide ones; colour-page boxes are 8.2 mm and hold two digits (the build report says "at least 12 mm high", which is not true for those boxes, but they exceed the owner's 6 mm and two digits fit; L-E). Figures checked at 150 and 200 dpi 1-bit:
- **Angle figures (P6-27, 28, 29):** lines, arcs, marks, vertex letters readable. Crowded: P6-28 item 4 (the `?` sits on line AE and the equal-side tick on DE touches it; the 15 degree wedge is tiny), P6-28 item 5 (letter E sits on line AB and reads as "-E-"; E is only 0.13 of the side above AB), P6-27 item 5 (the `43°` touches side AB), P6-27 item 4 and P6-28 item 6 (the `136°` and `132°` text lies on the diagonal BD), P6-29 item 2 (the `?` is placed between `40°` and the diagonal, away from the arc at B). The answers stay findable. See M4.
- **Nets (P6-34):** clear, six squares, thick lines.
- **Pie (P6-33):** 31 mm across, labels readable; Others and Badminton both 10% and look alike; fine.
- **Circles, semicircles (P6-17 to 22):** fine. Hatching is 0.24 to 0.26 mm lines about 1.2 mm apart: reads as stippled hatching at 150 dpi 1-bit; test on a real copier (L-D).
- **Mazes P6-02, 11, 24, 37:** fine. The cube-root glyph in P6-24 and P6-39 has a small index "3" (about 1.5 mm tall at 150 dpi 1-bit); distinguishable from the square-root sign but the first thing to fill in on a dark copy (L-C).
- **Dominoes P6-15, 39:** fine; START tag on the right half of the first domino, so the first letter is the START domino's letter (B, W); the check strip catches a wrong start.
- **Colour pages P6-09, 32, 40:** marks, key chips, cells and labels clear; the "no crayon" instruction is present; text sizes small but legible (P6-32 cuboid labels smallest).
- **Ratio models:** none in P6 (no bar models), nothing to check.

## 6. Front matter, keys, teacher notes against the owner decisions

Checked in both FrontMatter PDFs, both keys and both packs (Complete_Pack text equals FrontMatter + Puzzles). Annual licence ("annual licence: one school year and is renewable") present; publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers" on the cover; registered office 66 Tannery Ln, Singapore 347805 on the licence page; (c) 2026 Preciouslyours Pte Ltd; DRAFT stamps on cover, licence, teacher notes and key; contact pypteltd@gmail.com marked temporary; licence wording marked for a lawyer; the not-affiliated sentence is on the cover only, 6.5 to 7 pt, legible; the licence page keeps only the factual "The mathematics syllabus is published by the Ministry of Education, Singapore." No price, no "MOE-aligned", SASMO, PSLE or GEP wording anywhere (searched). Pupil pages carry the school-name line and licence footer. Two booklets of 20 single-sided pages, 10 one-star and 10 two-star each, black and white, no coins, no Mi, originals. One issue: **M3**. Minor: the S1-13 key note gives "K ÷ n for n ÷ K" (capital K, not a letter of the page); the S1-20 tag note ends with a stray "; 1.1"; the S1-08 and S1-15 tag notes explain only one of two numbers (L-H).

## 7. Similarity (my own passes)

- **Private sources** (`docs/books/private_*`, 20 828 entries, and `docs/sasmo/private_*`): 5-word runs containing at least two content words: 15 hits, all generic frames ("what fraction of the whole", "find the area of the", "the average of 4 numbers is", "needed to fill the tank", "find the missing number in"). I opened each matching private entry: they are short summaries with different numbers and scenarios. Number-scenario pass (three or more shared non-trivial numbers and two content words): 2 hits, both false except one: **P6-26 item 5 uses a tank 80 cm by 50 cm by 20 cm; a private Primary 5 entry has a tank 20 by 50 by 80** (different story: that one holds 1.2 ℓ and is poured out; ours is half full). Same numbers, different question; I would change one dimension (L-F). No 7-word run, no copied scenario. The builder's report (0 flags) is consistent with this.
- **Holiday Level 6** (`p6/content/*.js`, the "post-PSLE bridge" lessons) and **extension Level 6** (`extension/data/l6_*.json`): 3 trivial 5-word hits ("writing expressions with a letter", "how many sweets are left", colour tally words) and 4 number hits that I traced to l9.js (data lesson) as scattered numbers in one large file, not one question. No shared scenario found.

## 8. Findings

**High: none.**

### Medium

- **M1. Angle figures are drawn to scale, so a pupil with a protractor can read the answer (P6-27, P6-28, P6-29; this is an owner-brief failure mode).** The pages say "Do not measure" and the teacher notes say "drawn accurately so the pupil could measure". Examples measured: P6-27 item 1 angle B drawn about 64 deg for 60; P6-28 item 6 and P6-27 item 4 rhombi drawn at the printed 132 and 136; every `?` can be read to within 3 degrees, and the code table is spaced so a measured answer lands on the right letter. The check strip cannot see it. Fix: draw the figures not to scale (shift the shapes 8 to 15 degrees from the true value while keeping the given labels) and print "Not drawn to scale." on the three pages and in the teacher note; the builder's angle readers must be updated.
- **M2. One number inside an arch is not clearly the side (P6-20 figures O and E, P6-21 item 2, P6-22 item 4).** The figure is a body with a semicircle on top and a single label ("7 cm", "21 cm", "14 cm", "14 cm") written inside the body, with no dimension line and no word "square". It is not stated whether the number is the height of the body, the width, or the side of a square. The answers (68.25, 614.25, 273, 64) are right only for "a square body, semicircle diameter equal to the side". A pupil can also read it as the body's height and then lack the width. Items with two labels (P6-20 I and C; P6-21 item 1; P6-22 items 2 and 5) are unambiguous. This is exactly the weak point the builder named; the answer to the question asked is: **no, it is not clearly the side.** Fix: add a dimension line and the word "square" under the figure (or label both the width and the height), and change the page text to "The lower part is a square."
- **M3. The key and teacher notes print outcome numbers that are not in our syllabus summary, while saying none are given.** Both keys and both teacher pages say each tag uses "the outcome numbers of the Primary 6 Standard content in the Mathematics Syllabus, Primary (2021 edition, pages 43 and 44)" and that "where the summary gave no outcome number the key gives none". But the keys and "What the booklet covers" list "Area and Volume 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 2.4", "Geometry 1.1", "Statistics 1.1 and 1.2" and the Ratio numbers 1.1 to 1.7 as if official. The summary gives numbers only for Fractions, Percentage, Ratio, Algebra and Volume 2.5, and its own header says the ratio order is unverified. `p6_outcome_wording.md` admits these are the builder's own ids. A teacher reading the key would take them as the PDF's numbers. Fix: either verify against the PDF, or print the outcome wording without numbers (or "our reference" in brackets), and delete the sentence "gives none". Consistent with owner addendum 7 (wording of any alignment claim reviewed before publication).
- **M4. Label collisions on three angle pages (see section 5).** P6-28 item 4 `?` struck by line AE and the tick; P6-28 item 5 letter E on line AB; P6-27 item 5 `43°` touching the side; the `136°` and `132°` text over the diagonal; P6-29 item 2 `?` far from the arc. They survive 150 dpi 1-bit but will degrade on a worn copy. Fix with the same pass as M1 (move labels to a clear side, put the `?` in a white halo or beside its arc).

### Low

- **L-A.** "Use each card once" on P6-14, 19, 25, 29 while there are eight cards for six items (P6-04 says "Two cards are not used"). Use the same sentence on all five pages.
- **L-B.** Instruction sentences above the plan limit of 5: P6-22 (7), P6-21, 27, 28, 29 (6). Merge "Take π as 22/7. All lengths are in cm." and the last two instruction lines.
- **L-C.** Cube-root index small (P6-24, 39).
- **L-D.** Hatch lines 0.25 mm: include P6-20, 21, 22 in the real photocopier test; a copy on a heavy setting may close the gaps.
- **L-E.** Build report says answer boxes are at least 12 mm high; colour-page boxes are 8.2 mm (still over the owner's 6 mm, two digits fit). Correct the sentence.
- **L-F.** P6-26 item 5 tank 80 by 50 by 20 equals the dimensions of a private Primary 5 tank question. Change one number (for example 90 by 40 by 20: 36 ℓ half full, code table 40 becomes 36 and the word must be re-solved).
- **L-G.** Single-slip word test used 129 000 words on the code-table pages while the report and teacher notes say about 207 000. State one list or run the single-slip test with the larger list.
- **L-H.** Key text slips: S1-13 "K ÷ n for n ÷ K"; S1-20 tag note "; 1.1"; S1-08 and S1-15 tag notes incomplete; S2-04 is titled "Roots and Edges" and tagged VO2.2 but has no cube-edge-from-volume item (the "edge" is only the cube root); the S2-04 topic line mentions "the edge of a cube". Reword the title or tag.
- **L-I.** `spooge` (a vulgar slang hit) reachable by one slip on P6-28 (item 4 answer 15 written as 64). Swap the letters of 64 and 36 or 75 on that page and re-run its checks.
- **L-J.** Pi balance: 22/7 on 5 of 6 circle pages, 3.14 on one. The owner's own paper analysis (`docs/terms/owner_decisions.md`, Primary 6 papers) says 3.14 is more common in school papers than 22/7. Consider P6-19 or P6-22 with 3.14 (radius 10 or 20) so pupils meet both.
- **L-K.** P6-29 item 4: the drawing shows AC vertical and BCD horizontal, so the answer 90 can be seen without working.
- **L-L.** P6-18 item 2 needs 43.96 divided by 6.28; the teacher note says every number can be worked by hand. Say "a calculator may help" for that item.
- **L-M.** The word "Almost" on the cover ("Almost every puzzle checks itself") is not needed: all 40 pages have a check (blank boxes excepted).

### Information

- `validation_report.txt` (not rerun): 744 PASS, 0 FAIL, nothing skipped; stroke widths at least 0.25 mm, minimum text 8 pt, flat-grey budget respected, DRAFT stamps (6 per booklet) present. It matches my reading; I did not see any line that should be doubted. The builder's dependent checks (readers on printed text, drawing, pie and net) agree with my solves.
- The Complete Pack text is identical to FrontMatter + Puzzles in both booklets.

## 9. The builder's owner decisions: my recommendation on each

1. **Speed, pie charts, nets.** Keep pie (P6-33) and rate (P6-35): our own summary puts both in the Primary 6 Foundation revisit list, and GST/discount (P6-38) is a frequent school-paper topic. Replace **P6-34 (nets, Primary 4 only)** and **P6-37 (decimal maze, Primary 4)** with two Primary 6 pages (for example a S2 percent-change or fraction-division page, and a circle page), because S2 is the only booklet with 35% revision and no Primary 6 ratio or percentage page. If the owner prefers a revision-rich Term 4, keep as is; the tags are honest. Keep speed out.
2. **Ratio numbering 1.1 to 1.7.** Do not print any outcome numbers until the PDF is read (M3). Print the outcome wording only.
3. **P6-07 linking two ratios.** Keep; it is standard school work (Tom : Ravi and Ravi : Daniel), two stars, tagged as ratio of three quantities with a problem-solving note. Item 3 (needs scaling to match Ravi) is a good two-star step.
4. **GST 9%.** Correct (the rate since 1 Jan 2024). Keep "GST is 9%." on the page; add "from 2024" to the key note so a later change is easy to spot.
5. **Pi pairing.** Acceptable (22/7 only with multiples of 7, 3.14 with whole radii, never both on one page). Add one or two more 3.14 pages (L-J).
6. **No coin pages.** Agree; none is needed at Primary 6.
7. **Lawyer hold on the licence wording.** Agree; nothing is printed, sent or sold until the lawyer approves. Contact email and registered office are as the owner decided.
8. **Convert some code-word pages.** Do not convert. 19 of 40 are code-table pages, but another 14 pages (choice, matching, ordering, domino) also end in a word, and all share one mechanism the owner chose; the P2 booklets have the same pattern. Rebuilding needs a new solve and a 25-minute validation. If wanted, convert at most P6-27 and P6-28 (angles, the pages that also need M1/M4 edits) to matching.
9. **Pupil trial and photocopier test.** Yes, before release; they are the only way to settle L-C, L-D, M1 and the "does a pupil understand the arch label" question (M2).

## 10. What I could not check

- The MOE syllabus PDF (absent): outcome wording and numbers, the ratio list order (decision 2), whether two-step equations (P6-16) and the trapezium angle rule are inside the Primary 6 Standard lines, and whether pie charts and rate are Primary 6 lines for the Standard track.
- A real photocopier or printer (light and heavy toner), a pupil trial, a teacher read-through, whether 11 to 13 year olds find the pages the right length; reading load was judged from word counts only.
- Lawyer approval of the licence wording.
- The private sources are summaries and short records; I ran 5-word-run and number-scenario passes only. I did not read the Drive originals, and I did not test paraphrase similarity beyond the number and phrase passes.
- Double slips and three-answer errors were not tested exhaustively (the notes say so); I list the common-word double slips found in section 2.
- No dictionary is a perfect "real word" test: my union list includes names and slang, so hits were judged by hand; it may miss a word not in web2, gcide or wordfreq.
- I did not rerun the 25-minute validation, nor regenerate the PDFs; I audited the committed PDFs (HEAD `1c50639`, built 23 Oct 2026 20:18).
