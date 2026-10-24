# Independent audit, round 2: Primary 3 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent second-round check (not the builder, not the round-1 auditor). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`. Nothing pushed, no PR, nothing edited except this report.
Subject: `school/p3/out/P3_S1_*` and `P3_S2_*` as committed in `0752669` (identical in the working tree). Baseline = the PDFs audited in round 1 (`807633a`, the same files as `1f9676e`, 20:15 build). The MOE syllabus PDF (Primary 3, pp. 35-36) was used as data only; only outcome-line wording is quoted.
Read: `docs/audit_final/p3_semester_booklets_audit.md`; the second-pass and syllabus sections of `p3_semester_booklets_build_report.md`; plan; `school/p3/README.md`; `p3_outcome_wording.md`.

## Verdict

| Booklet | Content ready? |
|---|---|
| Semester 1 | **Yes.** All 15 changed pages hand-solved from the image before the key was read: 15 of 15 agree. No High, no Medium. |
| Semester 2 | **Yes, with two small print-side items (R2-1, R2-2) and one wording miss (R2-4).** All 19 changed pages hand-solved: 19 of 19 agree. No High. |

Every round-1 Medium (M1 to M4) is fixed on the page as claimed (details in section 4). All 31 code words are unique inside P3 and no wrong placement, single slip, anagram or other way of choosing spells another word in any of five dictionaries. Both booklets stay DRAFT by the owner's rule (real photocopier test, pupil trial, lawyer not done). What I found that the builder's report does not say: (a) not every thin stroke was thickened (R2-1); (b) one outcome line (Angles 1.1) still differs from the PDF (R2-4); (c) 13 of the 31 P3 code words are used in another level (section 6, table for the coordinator).

## 1. Which pages changed (text diff and pixel diff against the audited commit)

Method: `pdftotext` per page and 100 dpi greyscale render per page, old (`807633a`) against new (HEAD); any pixel difference over 40 grey levels counts. Result: **34 of 40 pupil pages changed; 6 are pixel-identical** (S1-07, S1-09, S1-12, S1-16, S1-18, S2-20 = P3-07, 09, 12, 16, 18, 40). Front matter: text diff shows only the outcome-line wording and one teacher-note sentence (section 5). Keys: only the answers and code words of reseeded pages, the removed "Problem solving" sentence (both keys) and wording changes. Complete packs: pupil pages 6 to 25 are identical in text to the puzzle PDFs.

"Solved" = I solved the page from the rendered image (100 dpi, 200 to 300 dpi crops for dials, beakers, figures, clocks; hands, lines and angles also checked from the PDF's vector coordinates) **before** reading the key, then compared with the key text. 34 of 34 agree. Boxes in the Change column: T = text, P = pixels only.

| Booklet page (P3) | Change | My solution from the image | Key | Notes |
|---|---|---|---|---|
| S1-01 (P3-01) Place Value | T: stems 4 and 6 now "Write the number: ...", strip | 4132 Q, 2023 U, 14 I, 7406 V, 60 E, 7090 R: **QUIVER** | agree | extension frame gone |
| S1-02 (P3-02) Words and Numbers | T: instruction two sentences (8 and 9 words) | route (4,4) (3,4) (2,4) (2,3) (2,2) (2,1) (1,1) (1,2): 8 boxes, dead ends 4704, 2369; unique | agree | |
| S1-03 (P3-03) Digit Cards | T: "Build the largest odd number" etc. | 8203 C, 9861 A, 9736 N, 1348 O, 1089 P, 1369 Y: **CANOPY** | agree | frame differs from extension u01 |
| S1-04 (P3-04) Compare and Order | T: reseeded cards | A: F 2473, L 7234, I 7423; B: G 8054, H 7154, T 976: **FLIGHT** (was COUSIN) | agree | |
| S1-05 (P3-05) Number Patterns | P and strip | 4000 P, 3290 O, 4090 L, 5200 I, 8500 C, 4900 E: **POLICE** | agree | |
| S1-06 (P3-06) Big Sums | T: code table letters | 7877 M, 2053 E, 1789 L, 4269 O, 7074 D, 6764 Y: **MELODY** (was TEACUP) | agree | sums unchanged |
| S1-08 (P3-08) Missing Digits | T: new sums | 8 T, 9 R, 1 I, 3 C, 4 K, 2 Y: **TRICKY** (was FATHOM) | agree | |
| S1-10 (P3-10) True or False | strip | P, U, B, L, I, C: **PUBLIC** | agree | |
| S1-11 (P3-11) Remainders | strip | 1 T, 0 H, 13 R, 2 I, 11 V, 7 E: **THRIVE** | agree | |
| S1-13 (P3-13) Multiply and Divide | T: new numbers | 95 F, 105 I, 1230 G, 149 U, 1208 R, 2115 E: **FIGURE** | agree | word kept, answers new |
| S1-14 (P3-14) Colour the Fish | P: eye is a ring | yellow 4, red 4, blue 4, green 2, orange 2; every mark pair (star red, triangle blue, square green, plus yellow, dot blue, moon orange) agrees | agree | ring, clearly different from the dot mark; survives both copier proxies |
| S1-15 (P3-15) Equal Fractions | strip | S, H, R, I, M, P: **SHRIMP** | agree | |
| S1-17 (P3-17) Fraction Gaps | T: topic line | 10 G, 8 O, 4 P, 12 H, 6 E, 9 R: **GOPHER** | agree | |
| S1-19 (P3-19) Fraction Sums | strip | 1 S, 5 C, 8 R, 6 I, 2 B, 7 E: **SCRIBE** | agree | |
| S1-20 (P3-20) Money Sums | T: five new questions | $6.85 U, $4.50 P, $5.85 D, $4.67 A, $9.45 T, coins 10c+20c+$5+50c+$2 = $7.80 E: **UPDATE** | agree | coin art legible |
| S2-01 (P3-21) Jugs and Beakers | T: code table; P: hatching | 700 D, 500 O, 300 N, 450 K, 350 E, 100 Y: **DONKEY** | agree | answers new, word kept |
| S2-02 (P3-22) Equal Measures | T: topic, unit stays with the box | route (2,3) (1,3) (1,2) (1,1) (2,1) (3,1) (4,1) (4,2): 8 boxes; (3,3) is a dead end; unique | agree | |
| S2-03 (P3-23) Kilograms and Grams | T/P: dials redrawn | needle angles: 8 kg, 7 kg, 450 g, 9 kg, 850 g, 950 g: 8000 F, 7000 R, 450 U, 9000 I, 850 T, 950 Y: **FRUITY** | agree | answers new; numerals now at least 0.8 mm from the ring |
| S2-04 (P3-24) Road Trip | T: topic, item 3 | 4500 W, 4700 A, 7350 L, 2500 N, 4000 U, 4100 T: **WALNUT** | agree | |
| S2-05 (P3-25) Order the Measures | T: Set B heading | A: W 2 km 5 m, O 2 km 50 m, M 2500 m; B: B 7400 g, A 7 kg 40 g, T 7 kg 4 g: **WOMBAT** | agree | all cards in each set are the same kind |
| S2-06 (P3-26) Seconds | P: strokes | hand 30 s D; hand at 35 s (30.0 degrees from the 6) so 95 E; 300 V, 280 O, 6 U, 70 R: **DEVOUR** | agree | |
| S2-07 (P3-27) The 24-Hour Clock | P: strokes | 0305 S; hour hand 288 degrees (9.6 h) = 9:36 am, 0936 A; 62.5 degrees = 2:05 pm, 1405 U; 2212 C; 6:30 pm Y: **SAUCY** | agree | minute ticks still 0.31 mm (R2-1) |
| S2-08 (P3-28) Start and Finish | T: letters | 2:25 pm V, 55 min O, 6:15 am Y, 2:10 pm A, 1 h 50 G, 5:25 pm E: **VOYAGE** (was VOLUME) | agree | |
| S2-09 (P3-29) Time Detective | T: timetable and items 3, 4 | A 0825-1000 = 95 min M; B 1055-1235 = 100 min E; C 1450 + 2 h 25 = 1715 A; D 0900 - 2 h 20 = 0640 D; **E 1840-2130 = 170 min O**; wait 1000 to 1055 = 55 min W: **MEADOW** (was WISDOM) | agree | Bus E now a same-day journey; table sits 0.2 mm above the question boxes (R2-3) |
| S2-10 (P3-30) Square Units | T/P: figures and strokes | A 8 cm2 C, perimeter 14 O; B 9 U, 18 G; C 11 A, 20 R: **COUGAR** (was CAMPUS) | agree | figures B and C are new (old B 9/16, C 12/18) |
| S2-11 (P3-31) Perimeter | T: code table | 32 B, 16 O, 150 W, 36 M, 42 A, 38 N: **BOWMAN** (was PEANUT) | agree | every side labelled |
| S2-12 (P3-32) Area Sums | T: code table | 40 B, 49 A, 36 N, 84 D, 70 I, 64 T: **BANDIT** | agree | |
| S2-13 (P3-33) Same or Different? | P: strokes | areas 5/6 B larger; perimeters 10/10 same; areas 6/7 B; perimeters 12/10 A; 10/12 B: **WORKS** | agree | |
| S2-14 (P3-34) Right Angles | T: reframed | 60 degrees smaller B, 90 I, 50 smaller R, 90 (turned, dot product 0) C, 140 greater H: **BIRCH** | agree | angles from vector end points |
| S2-15 (P3-35) Line Detective | T/P: new geometry, letters | slopes: AB 45, P 135 so P; AB 63.4, R 63.4 so R; Q 63.4 so Q; AB 45, R 45 so R; AB 116.6, Q 26.6 so Q: B, L, I, M, P: **BLIMP** (was BLUNT) | agree | gaps and labels in section 4 |
| S2-16 (P3-36) Draw the Lines | T: letters, grid 0.46 mm | lines drawn on the grid: V, O, L, U, M, E: **VOLUME** (was SWIVEL) | agree | R2-2 |
| S2-17 (P3-37) Bar Graph Detective | P: gridlines | 15 S, 40 P, 30 R, 25 U, 120 C, 10 E: **SPRUCE** | agree | |
| S2-18 (P3-38) Different Scales | T: questions 2 to 6 | 14 K, 70 N, 10 I, 190 G, 40 H, 50 T: **KNIGHT** (was TUXEDO) | agree | bar tops checked against the axes |
| S2-19 (P3-39) Colour the House | T: topic; strip | 17 parts: yellow 2, red 3, blue 4, green 4, orange 4; every mark pair agrees | agree | |

Unchanged and not re-solved: S1-07, 09, 12, 16, 18 and S2-20 (pixel-identical, so round 1's solves stand).

## 2. Code words: uniqueness

Dictionaries: `english-words` web2 (234 450) and gcide (114 029); `wordfreq` top 100 000 (94 139 alphabetic, strict set) and top 500 000 (292 993, wide set); the builder's own list `school/p3/gen/words_en.txt.gz` (262 445) and `words_common.txt.gz` (20 000). A string counts as a word if it is in any of these.
- Code-table pages (19): all 719 rearrangements, every single slip (one answer replaced by any other letter of that page's code table) and every two-slip pair. **Rearrangement hits: none. Single-slip hits: none.**
- Lettered-choice pages (8: P3-10, 15, 27, 28, 33, 34, 35, 36): every other way of choosing (64 to 15 625 combinations). **None spells a word.**
- Ordering pages (P3-04, 18, 25): all 719 wrong orders. **None.**
- All 31 code words differ from each other inside P3 (14 in S1, 17 in S2).
- Information only, two slips at once (not claimed by the booklets): JUICER (QUIVER), CANARY (CANOPY), HOPPER and POPPER (GOPHER), UPTAKE (UPDATE), COLLAR (COUGAR), BATMAN (BOWMAN), DANGIT, BANGIN and BANDAI (BANDIT), DENNEY, DONNED, BONNEY (DONKEY), MENDON, MADDOW (MEADOW), FRUTTI, PRUITT (FRUITY), DEVORE (DEVOUR). Nothing for MELODY, TRICKY, FIGURE, KNIGHT, SPRUCE (strict list). The teacher note "one or two wrong answers very rarely do" stays fair.
- Not a child-safety review of the words; none looks unsuitable. BOWMAN is also a surname.

## 3. Reading load (12 words) and strokes

**12-word rule.** Every sentence of every pupil page (all text blocks, split at . ? !). Instruction, stem and clue sentences: **none over 12 words** when the circled item number and the label "Topic:" are not counted, which is how `validate.py` counts. If they are counted, six reach 13: the topics of S1-03 and S2-04, S2-04 item 1, S2-08 item 1, S1-10 item 3 (and "Topic:" blocks run together with the instruction on the colour pages). Sentences of exactly 12: S1-12 "Write the numbers for the empty circles, tile 1 to tile 6.", S1-20 item 1, S2-12 item 4, the topics of S1-01, S1-09, S1-10, S1-12, S2-05. Check strips, over 12 and within 18: S1-14 (13 words) and S2-19, S2-20 (13, 16); S2-20's "Parts in the same place on the left and on the right have the same colour." is 16. All reworded pages (P3-02, 24 item 3, 34, 38 item 6, topics of 17, 22, 24, 28, 39) pass. Rule met.

**Strokes** (widths read from the PDF's vector data, not from the generator's attributes; checked also by distance transform of 400 dpi renders). Thickened as claimed: P3-30 and P3-33 unit lines (0.35 to at least 0.5), P3-37 and P3-38 gridlines (0.30 to at least 0.5), P3-36 grid (0.24 to 0.46), P3-21 hatching (0.36 to 0.39), P3-26 stopwatch ticks (0.42).
- **Not met everywhere (R2-1):** P3-27 clock minute ticks 96 strokes at **0.31 mm**; P3-34 angle arcs 5 strokes at **0.29 mm**. Both unchanged from round 1. Many drawn strokes sit between 0.35 and 0.5 mm: beaker hatching 0.39 (the build report says 0.5), dial and stopwatch ticks 0.42 to 0.46, P3-36 grid 0.46, angle rays 0.47, coin motifs and colour-page marks 0.40 to 0.42 (coins as intended).
- Every card, answer box, pill and table border on every page is **0.26 mm**, not the 0.4 to 0.5 mm in `css_p3.py` (the browser snaps CSS borders to one device pixel). Same in round 1; the rule "strokes at least 0.5 mm" in the README is therefore not literally true for borders.
- Clutter: dark-copier proxy of the thickened pages (P3-37, 38, 36, 21, 23, 14, 20): bars, levels, needles and lines stay clear. P3-37 and P3-38 are heavy (ten black gridlines of 0.5 mm meet the black bars, bar tops merge with the line at their height) but every value still reads; P3-21 level line is still the thickest line.

## 4. Round-1 items re-checked

- **M1, P3-35.** All five pictures: smallest distance between two lines (centre to centre) 5.1, 3.8, 4.7, 8.5, 6.0 mm; the closest pair of thin lines (item 2, Q and R) is 3.1 mm edge to edge, so the lines are at least 3 mm apart. Letters A and B now sit beyond the line ends (1.0 to 1.6 mm from the line); P, Q, R 0.5 to 2.6 mm (R in item 3 and Q in item 4 sit 0.5 mm under a line end, not overprinted). Word BLIMP, one right line per question, decoys are neither parallel nor perpendicular.
- **M2, reading load.** Section 3.
- **M3, P3-23 dials.** Gap between the numerals and the outer edge of the ring, measured on all six dials at 400 dpi: 0.80 to 0.84 mm for the 5 and 500 at the top, 1.1 to 1.2 mm for every other numeral. Round 1 measured 0.04 to 0.3 mm on dials 1, 2 and 6 (800, 900, 1000 overprinting the ring). **Fixed.** Needles read from vector end points: 8 kg, 7 kg, 450 g, 9 kg, 850 g, 950 g.
- **M4, extension overlap.** P3-34, P3-03 and P3-01 sentences share no 5-word run with `extension/data/l3_u01..u10.json` or `p3/content/l3.js`. Residual, Low: P3-35's stems "Which line is perpendicular to line AB?" and "Which line is parallel to line AB?" are word for word the stems of extension u08 (numbers and pictures differ). Generic wording; owner addendum 6 asks only that the questions of the two editions not be identical.
- **P3-29 Bus E.** Now 1840 h to 2130 h, same day, 170 min; no journey crosses midnight; all four-digit times with h.
- **L1 to L9.** L1 plan and README read "Colour the House": yes. L2 S2 notes no longer name S1-20; the key prints the "Problem solving" sentence only if a page has that tag: removed from both keys. L6 fish eye is a ring: yes. L7 check-strip boxes: 11.6 mm square in the path (about 11.9 mm outer with the border), three per strip 11.4 wide: the 12 mm rule is met within 0.1 to 0.6 mm; fine. L8 P3-22 "= [ ] m": the unit stays with the box. L9 P3-25 Set B heading "heaviest first": yes.
- **1-bit legibility, changed pages.** I viewed all changed pages at 100 dpi and the drawn pages at 200 to 300 dpi (dials, beakers, hatching, clocks, figures, lines, angles, bar graphs, colour pages, coins), plus an extreme light-copier proxy (blur, threshold 105) and a dark-copier proxy (threshold 175) of P3-14, 20, 21, 23, 27, 34, 35, 36, 37, 38. I did not re-run the builder's 150 dpi mono test (the validation report shows ink loss under the limits). Findings: dials, needles, level lines, lines of P3-35, grids of P3-36, bars, coins read in both proxies. In the extreme light proxy the 0.26 mm borders and the regular-weight small text fade (same as round 1) and the P3-27 minute ticks and the P3-34 angle arcs disappear (R2-1); in the dark proxy nothing fuses except what R2-2 notes. A real copier test is still the right test.

## 5. The 15 corrected outcome lines, and the front matter

Compared the front-matter coverage tables of both booklets (pp. 4 to 5) and `p3_outcome_wording.md` with the PDF's Primary 3 pages. **16 lines changed in the front matter, not 15** (the report's own list has 16 names): Whole Numbers 1.2; Fractions 1.2, 1.3, 1.4, 2.1; Length, Mass and Volume 1.1, 1.2, 1.3; Area and Perimeter 1.1, 1.2, 1.3, 1.4; Angles 1.2; Perpendicular and Parallel Lines 2.1; Bar Graphs 1.1, 1.2. All 16 now match the PDF word for word (bullets joined; "ml" as the PDF prints it). The other 17 lines were already word for word, **except one**:
- **R2-4. Angles 1.1** reads "concept of an angle" in the S2 front matter, `p3_outcome_wording.md` (line 62), the plan (line 148) and `gen/outcomes.py` (line 36); the PDF line is "concepts of angle". The builder's "the other 19 were already word for word" is wrong for this line. Fix: change the three places, rebuild S2 front matter, and say 16 (or 17).
- The key's "Notes on the tag" are short paraphrases written for teachers, not outcome lines (for example "perimeter of a rectilinear figure, a rectangle and a square", "reading and interpreting bar graphs", "identifying perpendicular and parallel lines"); the key was not changed. If the owner wants every printed outcome phrase to be the PDF's, these also differ; the front matter is where the lines are printed.

Front matter otherwise unchanged: same 5 pages each; cover, licence, DRAFT stamps, publisher line, not-affiliated sentence (cover only) untouched; the S2 teacher note now says "a light setting can thin the fine lines of the scales, grids and graphs" in place of the coins sentence. Keys 9 and 10 pages; packs 25 and 25; pupil pages identical in the packs.

## 6. Cross-level code words (for the coordinator)

Source: the `Check result:` line of every entry in `school/p1..p6/out/P?_S?_Answer_Key.pdf` (pdftotext), read from the working tree at about 21:45 on 23 Oct 2026 (P5 keys were being rebuilt; P4 and P6 were at their last commit). 190 code or check words: P1 30, P2 32, P3 31, P4 33, P5 31, P6 33; 116 distinct. **40 words are used in more than one level** (none twice inside one level). Of the 31 P3 words, **13 are used in another level; 18 are P3 only** (QUIVER, TRICKY, THRIVE, PUBLIC, GOPHER, JUNIOR, SCRIBE, UPDATE, SAUCY, VOYAGE, MEADOW, BOWMAN, WORKS, BIRCH, BLIMP, VOLUME, SPRUCE, KNIGHT).
- New collisions created by the P3 reseed: COUGAR (P6-23), FLIGHT (P4-38), MELODY (P5-31). The replacements for COUSIN, TEACUP, FATHOM, CAMPUS, PEANUT cleared P3 of those words but they remain in P1, P2, P4 and P6 (rows below).
- The 4 kept words (DONKEY, FRUITY, FIGURE, BANDIT) are in P1/P2 and also in P4 and P6; CANOPY, DEVOUR, POLICE, SHRIMP, WALNUT, WOMBAT are shared with P4 and P6 as well.
- Largest overlap is between P4 and P6 and between P1 and P2 (not P3's business; rows kept for the coordinator).

| Word | Pages | Levels | In P3 |
|---|---|---|---|
| BACKUP | P2-34, P4-02 | 2 |  |
| BANDIT | P2-31, P3-32, P4-17, P6-06 | 4 | yes |
| BOTANY | P2-21, P4-30, P6-15 | 3 |  |
| CAMPUS | P2-24, P4-36 | 2 |  |
| CANOPY | P3-03, P4-34, P6-25 | 3 | yes |
| COBALT | P2-33, P4-24 | 2 |  |
| COUGAR | P3-30, P6-23 | 2 | yes |
| COUSIN | P1-10, P4-37, P6-17 | 3 |  |
| CRAFTY | P4-29, P6-16 | 2 |  |
| CREAMY | P2-13, P4-03, P6-01 | 3 |  |
| CURFEW | P2-10, P4-18 | 2 |  |
| DEVOUR | P3-26, P4-31, P6-07 | 3 | yes |
| DONKEY | P1-23, P2-36, P3-21, P4-23, P6-31 | 5 | yes |
| FABRIC | P4-15, P6-30 | 2 |  |
| FAMILY | P1-11, P2-37, P4-19, P6-34 | 4 |  |
| FATHOM | P2-22, P4-35, P6-08 | 3 |  |
| FIGURE | P2-25, P3-13, P4-14, P6-33 | 4 | yes |
| FLIGHT | P3-04, P4-38 | 2 | yes |
| FROZEN | P1-16, P2-15, P4-08, P6-18 | 4 |  |
| FRUITY | P2-26, P3-23, P4-10, P6-10 | 4 | yes |
| HUNGRY | P2-27, P4-01, P6-19 | 3 |  |
| LENGTH | P1-17, P2-04 | 2 |  |
| MAGNET | P1-27, P2-16, P6-35 | 3 |  |
| MELODY | P3-06, P5-31 | 2 | yes |
| MONKEY | P1-21, P6-03 | 2 |  |
| NUMBER | P1-13, P2-05, P6-26 | 3 |  |
| PEANUT | P1-26, P2-28, P4-09, P6-27 | 4 |  |
| POLICE | P3-05, P4-20, P6-20 | 3 | yes |
| SAILOR | P1-29, P2-06 | 2 |  |
| SHADOW | P1-03, P2-29, P4-39, P6-36 | 4 |  |
| SHRIMP | P3-15, P4-12, P6-04 | 3 | yes |
| SPONGE | P1-39, P2-18 | 2 |  |
| SQUARE | P1-05, P6-12 | 2 |  |
| STUDIO | P4-21, P6-13 | 2 |  |
| TEACUP | P1-40, P2-07, P4-06, P6-05 | 4 |  |
| TURKEY | P1-35, P4-26, P6-38 | 3 |  |
| WALNUT | P3-24, P4-28, P6-22 | 3 | yes |
| WALRUS | P4-16, P6-14 | 2 |  |
| WIZARD | P2-20, P4-22, P6-28 | 3 |  |
| WOMBAT | P3-25, P4-33, P6-39 | 3 | yes |

## 7. Remaining items

**Must or should do before printing (small):**
- **R2-1 (Medium-Low).** Thicken the P3-27 minute ticks (0.31 mm) and the P3-34 angle arcs (0.29 mm) to at least 0.35 mm (better 0.5), or accept them and add S2-07 and S2-14 to the real-copier test list; correct the claims in the build report ("at least 0.5 mm", hatching "0.5 mm") and the README to the measured values (beaker hatching 0.39, ticks 0.42 to 0.46, grid 0.46, borders 0.26). No page becomes unsolvable if these fade: the hour ticks, the numerals and the rays carry the answer.
- **R2-4 (Low).** Angles 1.1 wording to "concepts of angle" in `outcomes.py`, `p3_outcome_wording.md`, the plan; rebuild the S2 front matter. Correct the count in the report to 16.
- **R2-6 (coordinator).** Decide the cross-level policy for code words (section 6) before P4 to P6 are final.

**Low:**
- **R2-2. P3-36 (S2-16).** Item 5: the label A is overprinted by the top end of the thick line AB (new since round 1). Items 3 and 6 end exactly at the top corners of the grid (L at the top-left corner, E at the top-right corner), so a line drawn a little to the side leaves through the side edge; the letter is still the only sensible answer. Move the A label off the line and consider shifting P in items 3 and 6 so the answers fall on a vertex that is not a corner.
- **R2-3. P3-29 (S2-09).** The timetable's bottom border is 0.2 mm above the tops of question boxes 1 and 2 (the same in round 1). Add 3 mm of space.
- **R2-5. P3-35.** The two question stems equal extension u08's (generic wording).
- **R2-7.** Thin regular-weight text and 0.26 mm borders drop out in an extreme light copy (same as round 1, ties to the real copier test).
- Round-1 Low L4, L10, L11 to L14 not re-checked (not in the list of changes).

## 8. What I did not do

- `validate.py` not re-run (about 25 minutes); I read `out/validation_report.txt` (744 checks, 0 failed, all lines PASS) and found nothing wrong in it. My independent hand-solves and word search agree with it.
- No real copier and no pupils. Judgements on stroke fade come from the vector widths and from two simulations.
- Private-source similarity not repeated (round 1 found none; the changed sentences are all new but short and generic). Only the extension and `p3/content/l3.js` overlap was re-run.
- P3-40 and the five unchanged S1 pages were not re-solved (pixel-identical to the audited versions).
- The cross-level table reads keys as they stand; P4, P5 and P6 are still being revised by other builders, so the table will go stale.
