# Independent audit, round 3: Primary 3 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent third-round check (narrow). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`. Nothing pushed, no PR, nothing edited except this report.
Subject: the PDFs in `school/p3/out` as they stand (`P3_S1/S2_Puzzles`, `_Answer_Key`, `_FrontMatter`; mtime 22:09). Baseline = the round-2 audited build, commit `0752669` (21:30). The data files were not used; the page content comes from the PDFs only.

## Verdict

| Booklet | Content ready? |
|---|---|
| Semester 1 | **Yes.** All 20 pages hand-solved from the render before the key was read: 20 of 20 agree. No High, no Medium. |
| Semester 2 | **Yes.** All 20 pages hand-solved: 20 of 20 agree. No High, no Medium. Two Low notes (R3-1, R3-2). |

Every round-2 item the builder claimed to fix is fixed on the page (section 3). The three new words are unique and clean (section 4). Stroke claims are true as stated (section 2). Both booklets stay DRAFT by the owner's rule (real copier test, pupil trial, lawyer not done).

## 1. What changed against the round-2 build (text diff and 100 dpi pixel diff, per page)

- Pixel diff (difference over 40 grey levels): **all 40 pupil pages differ** (8 000 to 320 000 pixels). Cause: the borders went from 0.26 to 0.53 mm on every card, box, pill and table rule, so every page changes. Smallest changes: P3-14 (8 400), P3-39 (8 800), P3-40 (10 400), the colour pages, where only the card borders changed.
- Text diff (`pdftotext`, whitespace ignored): pupil pages changed in words on **P3-04, 06, 22 (none: wrap only), 24, 28, 29, 30, 34, 35, 36**. Details: P3-04 card letters F L I G H T to W I S D O M; P3-06 six new sums and a new code table (SWIVEL); P3-24 and P3-28 only line wraps (item 6 of P3-28, item 2 of P3-24, item 6 of P3-24); P3-29 instruction now "Write each answer in the box. Use the code table." (two lines); P3-30 code table 6 Z, 7 T, 10 X, 11 D, 13 R, 14 U, 16 E, 18 O, 26 Q (areas 7, 10, 11, perimeters 14, 16, 18); P3-34 helper box one line; P3-35 stems; P3-36 label positions (A and B beyond the line ends, P moved), letters of item 6 reordered.
- Keys: only P3-04, 06, 30 (new answers and words) and P3-36 (exits x = 3, 2, 1, 2, 3, 1).
- Front matter S1: text identical. S2: only Angles 1.1 now "concepts of angle" (the 16 round-2 lines plus this one = 17).
- Packs follow the puzzle PDFs (not diffed separately).

## 2. Stroke widths (read from the PDF vectors, `pymupdf`, stroke width converted to mm; filled hairlines checked too)

Every stroked path on every pupil page is **0.50 mm or more**, except exactly the exceptions the builder listed:
- tier star outlines 0.24 mm (1 or 2 per page, equal to the number of stars; filled black);
- P3-20 coin motifs 0.40 (9 strokes) and 0.42 (1);
- colour pages marks and picture strokes 0.40 (P3-14: 16, P3-39: 17) and 0.41 (P3-40: 14).
Measured as claimed: cards, boxes, pills, tables 0.53; beaker ticks 0.51 and 0.63, hatching 0.51; dial ticks 0.50 and 0.73; stopwatch ticks 0.54 and 0.71; P3-27 clock ticks 0.52 and 0.61; P3-34 arcs 0.53 and rays 0.59; P3-36 grid 0.55; P3-37/38 gridlines 0.50 to 0.60.
**Not in the builder's list, found now (R3-1, Low):** the fraction bars in the numerals of P3-15 to P3-19 (and the small rule between number and colour name on the three colour cards) are drawn as filled rectangles **0.26 mm** thick (about one pixel at 100 dpi). They are part of the text, so the "0.5 mm" rule does not reach them. In 1-bit at 100 and 150 dpi they survive; in the extreme light proxy they thin. Add to the copier-test note.

## 3. Hand solutions, per page (solved from the render, key read afterwards; vector end points used for dials, angles, lines and the P3-36 lattice)

| Page | Changed | My solution | Key | Notes |
|---|---|---|---|---|
| S1-01 (P3-01) | borders | 4132 Q, 2023 U, 14 I, 7406 V, 60 E, 7090 R: QUIVER | agree | |
| S1-02 (P3-02) | borders | route (4,4) (3,4) (2,4) (2,3) (2,2) (2,1) (1,1) (1,2), 8 boxes | agree | unique |
| S1-03 (P3-03) | borders | 8203 C, 9861 A, 9736 N, 1348 O, 1089 P, 1369 Y: CANOPY | agree | |
| S1-04 (P3-04) | **text** | A: 2473 W, 7234 I, 7423 S; B: 8054 D, 7154 O, 976 M: **WISDOM** | agree | new word |
| S1-05 (P3-05) | borders | P, O, L, I, C, E: POLICE | agree | |
| S1-06 (P3-06) | **text** | 8504 S, 5848 W, 7733 I, 6618 V, 4191 E, 9253 L: **SWIVEL** | agree | new word |
| S1-07 | borders | route (4,3) (4,4) (3,4) (2,4) (2,3) (2,2) (2,1) (1,1), all 48 | agree | |
| S1-08 | borders | 8 T, 9 R, 1 I, 3 C, 4 K, 2 Y: TRICKY | agree | |
| S1-09 | borders | route (1,3) (1,2) (2,2) (3,2) (4,2) (4,3) (4,4) (3,4), all 6 | agree | |
| S1-10 | borders | P, U, B, L, I, C: PUBLIC | agree | |
| S1-11 | borders | 1 T, 0 H, 13 R, 2 I, 11 V, 7 E: THRIVE | agree | |
| S1-12 | borders | 3, 7, 8, 4 (tile 4 right), 4, 6; loop closes | agree | |
| S1-13 | borders | 95 F, 105 I, 1230 G, 149 U, 1208 R, 2115 E: FIGURE | agree | |
| S1-14 (P3-14) colour | borders | yellow 4, red 4, blue 4, green 2, orange 2; each mark pair (star red, triangle blue, square green, plus yellow, dot blue, moon orange) agrees | agree | pupil vs key page: same 16 parts, same marks, same questions (side-by-side render); tally agrees |
| S1-15 | borders | S, H, R, I, M, P: SHRIMP | agree | |
| S1-16 | borders | route (4,4) (3,4) (2,4) (2,3) (2,2) (2,1) (3,1) (4,1) | agree | |
| S1-17 | borders | 10 G, 8 O, 4 P, 12 H, 6 E, 9 R: GOPHER | agree | |
| S1-18 | borders | J, U, N; I, O, R: JUNIOR | agree | |
| S1-19 | borders | S, C, R, I, B, E: SCRIBE | agree | |
| S1-20 | borders, coins | $6.85 U, $4.50 P, $5.85 D, $4.67 A, $9.45 T, $7.80 E: UPDATE | agree | coins legible at 100 dpi |
| S2-01 (P3-21) | strokes | 700 D, 500 O, 300 N, 450 K, 350 E, 100 Y: DONKEY | agree | level line thicker than hatching; read at 250 dpi |
| S2-02 | borders | route (2,3) (1,3) (1,2) (1,1) (2,1) (3,1) (4,1) (4,2) | agree | |
| S2-03 (P3-23) | strokes | 8 kg F, 7 kg R, 450 g U, 9 kg I, 850 g T, 950 g Y: FRUITY | agree | needle tips meet the ticks cleanly |
| S2-04 | borders, wraps | 4500 W, 4700 A, 7350 L, 2500 N, 4000 U, 4100 T: WALNUT | agree | |
| S2-05 | borders | W, O, M; B, A, T: WOMBAT | agree | |
| S2-06 (P3-26) | strokes | 30 D, 95 E (hand at 35 s), 300 V, 280 O, 6 U, 70 R: DEVOUR | agree | |
| S2-07 (P3-27) | strokes | 0305 S; 0936 A; 1405 U; 2212 C; 6:30 pm Y: SAUCY | agree | clock at 1-bit, section 5 |
| S2-08 | borders, wraps | V, O, Y, A, G, E: VOYAGE | agree | |
| S2-09 (P3-29) | **text, layout** | 95 M, 100 E, 1715 A, 0640 D, 170 O, 55 W: **MEADOW** | agree | timetable, section 6 |
| S2-10 (P3-30) | **text** | A 7 cm2 T, 14 U; B 10 X, 16 E; C 11 D, 18 O (counted from a 250 dpi crop, perimeter by 4n - 2 adjacencies): **TUXEDO** | agree | new word |
| S2-11 | borders | 32 B, 16 O, 150 W, 36 M, 42 A, 38 N: BOWMAN | agree | |
| S2-12 | borders | 40 B, 49 A, 36 N, 84 D, 70 I, 64 T: BANDIT | agree | |
| S2-13 (P3-33) | strokes | W (B larger area 5/6), O (10/10), R (6/7), K (12/10), S (10/12): WORKS | agree | |
| S2-14 (P3-34) | **text, strokes** | angles from vertex and ray end points: 60.0 B, 90.0 I, 50.0 R, 90.0 C, 140.2 H: BIRCH | agree | helper box one line; 1-bit, section 5 |
| S2-15 (P3-35) | **text** | AB/other slopes: item 1 AB 45, P 135 so P (B); 2 R 63.4 (L); 3 Q 63.4 (I); 4 R 45 (M); 5 AB 116.6, Q 26.6 so Q (P): BLIMP | agree | stems "Choose the line that is parallel (perpendicular) to AB." |
| S2-16 (P3-36) | **text, layout** | lattice from vector coordinates (P at (1,2), (2,3), (1,4), (2,2), (1,2), (2,2); lines drawn): exits x = 3, 2, 1, 2, 3, 1 = V, O, L, U, M, E: VOLUME | agree | section 7 |
| S2-17 (P3-37) | strokes | 15 S, 40 P, 30 R, 25 U, 120 C, 10 E: SPRUCE | agree | |
| S2-18 (P3-38) | strokes | 14 K, 70 N, 10 I, 190 G, 40 H, 50 T: KNIGHT | agree | |
| S2-19 (P3-39) colour | borders | yellow 2, red 3, blue 4, green 4, orange 4 (17 parts); marks pairs agree | agree | pupil vs key: same questions and marks; tally agrees |
| S2-20 (P3-40) colour | borders | yellow 2, red 4, blue 4, green 2, orange 2 (14 parts); left/right pairs equal | agree | pupil vs key: same questions; tally agrees |

**40 of 40 agree, including the 33 pages the builder did not re-solve.** Thickening obscured nothing: the beaker level line, dial needles, stopwatch hand, hands of both clocks, and the unit lines of the figures remain separable from ticks and hatching.

## 4. Code words

- P3 has 31 code words (the 32 hits of the key line include the word FINISH). All 31 are different from each other.
- The three replaced words, checked with `english-words` (web2 17 468 six-letter, gcide 11 122), `wordfreq` top 100 000 and top 500 000 (13 889 and 46 288 six-letter) and the builder's own lists (`words_en` 56 421, `words_common` 4 355); union 57 060. All three are in all dictionaries.

| Word | Page | Other order (719 rearrangements) | Single slip to any other table letter | Any one letter changed to any A-Z | Anagram |
|---|---|---|---|---|---|
| WISDOM | P3-04 (letters on the cards) | none | none (30) | WIGDOM, WINDOM (a surname), WISDOT, but G, N, T are not on the page | only itself |
| SWIVEL | P3-06 (9-letter table) | none | none (48) | SNIVEL, SWIVET, but N and T are not in the table | only itself |
| TUXEDO | P3-30 (9-letter table) | none | none (48) | none | only itself |

Information only (two slips, as in round 2, not claimed): SWIVEL to SWIPES (V to P and L to S); TUXEDO to TEREDO. One slip plus a reordering gives QUOTED, TOURED, ROUTED, DETOUR from TUXEDO, PELVIS from SWIVEL, WIDOWS from WISDOM: two errors at once. The teacher note "one or two wrong answers very rarely do" stays fair.
- Other levels: the Answer Key PDFs of `school/p1` to `p6/out`, read as they stand (P4 to P6 may still change), contain none of TUXEDO, WISDOM or SWIVEL, in the Check result lines or anywhere in the text. They also do not appear in the pupil PDFs of other levels.

## 5. Legibility at 1-bit (`pdftoppm -mono`, 100 and 150 dpi) and in copier proxies

- **P3-27 clock:** at 100 dpi the ring and the 60 minute ticks fuse into a thick ring with ragged dashes; the hour ticks, numerals and both hands remain clear. Clock 2 (hour hand between 9 and 10, minute hand at 7) and clock 3 (minute hand at 1, hour hand a little past 2) read correctly. At 150 dpi the minute ticks are separable. The answers rest on the hour numerals and hands, not on single minute ticks. Fine.
- **P3-34 angles:** at 100 and 150 dpi all five angles, rays and arcs are present and the five answers are unchanged. (In round 2 the arcs disappeared in the light proxy; now they survive 1-bit.)
- **P3-36:** at 100 dpi the grid, A and B labels (with halo), P and the top letters read; the thick AB is clear of the labels.
- **P3-37/38, dark copier proxy** (blur, threshold 175): ten black gridlines and the black bars are heavy but every bar top reads (Band 35 and Chess 15 on a line; Fri 10 on its line); white gaps between lines stay about 1.5 mm. Light proxy: lines and bars intact.
- **Extreme light proxy (blur, threshold 105) on P3-21, 23, 27, 29:** borders (0.53 mm) now survive on every page (round 2: they faded). The regular-weight small text fades, as in round 2 (R2-7): on P3-29 the timetable's cell text, which carries the data, drops out. **R3-2 (Low):** timetable text and the stems on P3-29 are regular weight; keep P3-29 on the copier-test list (it is not on it) or print the timetable cells in the semi-bold weight.

## 6. P3-29 (Time Detective)

Timetable (A, B, E) bottom edge to the tops of the question boxes: 12 px at 100 dpi = **about 3 mm** (round 2: 0.2 mm). The two instruction lines fit; the page has no overflow. Bus C and Bus D are given inside the questions; Bus E 1840 h to 2130 h is a same-day journey. Boxes: unit after the box (min, h) as before; every answer unique; MEADOW agrees. Code table has no entry that two different sums can reach (45, 55, 80, 95, 100, 170, 230, 0640, 1715).

## 7. P3-36 (Draw the Lines): can an item be read two ways?

Grid 6 by 6 cells (7 lines, 17 pt apart), the letters stand over the grid lines at x = 0 to 6. Exits computed from the vector lattice: 1 parallel, P (1,2), AB 45 degrees: top at x = 3 (V); 2 perpendicular to a horizontal AB: x = 2 (O); 3 parallel to a vertical AB: x = 1 (L); 4 perpendicular to the bottom-edge AB: x = 2 (U); 5 parallel, AB 45 degrees, P (1,2): x = 3 (M); 6 perpendicular to AB (slope 1/2): P (2,2) to (1,0): E. No exit is at a corner, none at x = 0 or x = 6 except none (all 1 to 3); P is never on the bottom edge; A and B are beyond or beside the line ends with a halo and are not overprinted by the thick line; the wrong construction (parallel instead of perpendicular) lands on a different letter, never on the same one. The "no two ways" requirement is met. **Low note (R3-3):** in item 3 the top row shows a letter P (x = 2) while the page also names a point P; the answer (L) is not affected, but a rename of that letter would remove a possible look-alike.

## 8. Other checks

- **Reading load (12 words).** Instructions, stems and clues: none over 12 words once the item number and "Topic:" are left out (the long hits of the scan are two merged blocks and two item stems that reach 13 only if the circled number is counted, as in round 2). The new P3-29 instruction (10 words total), P3-35 stems (9) and P3-34 helper box (15 words in a boxed note, not an instruction) pass; check strips up to 18.
- **P3-34/35 layout:** the helper box now sits on one line; P3-35 question column wider, stems wrap to four lines, no overlap with the letter pills.
- **Outcome line.** Angles 1.1 now reads "concepts of angle" in the S2 front matter; S1 front matter identical to round 2.
- **Colour pages, pupil page against key page.** Same questions on both (text compare of expressions plus side-by-side renders), same marks, the key's colours equal my hand colouring, tallies equal the printed check strip on all three.

## 9. Remaining items

| Id | Severity | Item |
|---|---|---|
| R3-1 | Low | Fraction bars 0.26 mm on P3-15 to 19 (and the rule under the number on the colour cards): outside "0.5 mm"; add to the copier test; README and build report say "every stroke is 0.50 mm or more" apart from the three listed exceptions, which is not true of these. |
| R3-2 | Low | P3-29 timetable (regular weight) fades in an extreme light copy; add P3-29 to the copier test list. |
| R3-3 | Low | P3-36 item 3 has a letter P on the top edge as well as the point P. |
| Info | - | Cross-level word policy (13 of the 31 P3 words are used in other levels, see round 2); TUXEDO, WISDOM, SWIVEL are free. |
| Info | - | No real copier, no pupil trial, lawyer not done (unchanged). |

## 10. What I did not do

- `validate.py` not re-run; the builder's report says 744 checks, 0 failed.
- Not read: the data files, the private-source similarity (unchanged text apart from the new numbers).
- Complete packs were not diffed separately; P4, P5, P6 keys were read as they stand and may still change.
