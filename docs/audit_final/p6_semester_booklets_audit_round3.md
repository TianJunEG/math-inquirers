# Independent audit, round 3: Primary 6 early-finisher booklets (Semester 1 and Semester 2)

Auditor: independent narrow check (not the builder, not the round-1 or round-2 auditor's files). Date: 24 Oct 2026. Branch `claude/great-fermi-1hv4vc`, after round-2 fixes (commit `6509f53`) and the colour-page guard (`a91e866`). Read-only apart from this report. Nothing rebuilt: every check is on the committed PDFs in `school/p6/out` (and `S2_pupil.html` for angle measurements).
Read first: `p6_semester_booklets_audit.md`, `p6_semester_booklets_audit_round2.md`, `colour_page_guard_note.md`, `docs/school_books/p6_semester_booklets_plan.md`, `p6_semester_booklets_build_report.md`, `BUILD_REPRODUCIBILITY.md`, `p6_outcome_wording.md`, and the MOE syllabus PDF (Primary 6 pp. 43-44; data only).

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **Content ready.** All 20 pages hand-solved, 20 of 20 agree with the key. One Medium (coverage claims, M1), Lows only otherwise. Still DRAFT by the owner's rule (lawyer, pupil trial, photocopier). |
| Semester 2 | **Content ready after the same text fix (M1).** All 20 pages hand-solved, 20 of 20 agree with the key. No wrong key, no unsolvable page, no page with two answers. Still DRAFT. |

**No High.** Round-2 M1 (angle labels), M2 (S2-01 item 4 "square"), M3 (key sentences) and L1 (colour boxes) are fixed in the committed PDFs. One new Medium: the front-matter coverage table and the key tags claim item types that are not on three colour or mixed pages.

## 1. What changed since round 2 (PDF diff, 90 dpi, committed PDFs against `6d8683a`)

Pixel-different pupil pages: **S1-09, S2-01, S2-02, S2-04, S2-07, S2-08, S2-09, S2-12, S2-20** (9). The other 31 pupil pages are pixel-identical to the PDFs round 2 solved. Page counts are unchanged: Puzzles 20 and 20, FrontMatter 5 and 5, Keys 9 and 10, Complete Packs 25 and 25. Pages are A4 (595 x 842 pt) throughout.

## 2. Hand-solve (sample far above 40%: all 40 pages)

I solved every page myself from the rendered image or the PDF text (script only for arithmetic and for the angle measurements), then compared with the printed key. **40 of 40 agree.** This covers all 20 two-star pages, all three colour-by-code pages, every page changed since round 2 and every page flagged in rounds 1 and 2.

| Page | My answer (before the key) | Word | Key |
|---|---|---|---|
| S1-01 | 2/25 C, 3/13 R, 1/27 E, 2/15 A, 5/27 M, 3/56 Y | CREAMY | agrees |
| S1-02 | maze: (1,2) (1,3) (2,3) (3,3) (4,3) (4,2) (4,1) (3,1), 8 boxes; (1,4) and (4,4) are dead ends; unique | route | agrees |
| S1-03 (2 star) | 2 M, 2/9 O, 9 N, 1/10 K, 3 E, 5 Y | MONKEY | agrees |
| S1-04 | S, H, R, I, M, P (X and F unused) | SHRIMP | agrees |
| S1-05 | 48 T, 15 E, 9 A, 54 C, 27 U, 44 P | TEACUP | agrees |
| S1-06 | 12 B, 16 A, 20 N, 30 D, 147 I, 70 T | BANDIT | agrees |
| S1-07 (2) | 2:7:4 D, 7:5:1 E, 5:6:2 V, 1:2:2 O, 6:4:3 U, 4:1:3 R | DEVOUR | agrees |
| S1-08 (2) | 4:1 F, 2:7 A, 1/6 T, 7/12 H, 3/8 O, 3:4 M | FATHOM | agrees |
| S1-09 (2, colour) | Y 12, R 20, B 36, G 45, O 60. Top: 60 O, 60 O (star), 60 O (star); roof 36 B, 36 B (squares); body 12 Y, 45 G, 12 Y (circles); wheels 45 G, 45 G (triangles); bottom 20 R, 20 R, 20 R (crosses). Tally Y2 R3 B2 G3 O3 | tally | agrees; each shape mark joins parts of one colour |
| S1-10 | 640 F, 160 R, 190 U, 660 I, 360 T, 480 Y | FRUITY | agrees |
| S1-11 | route from START (2,2): (1,2) (1,3) (1,4) (2,4) (3,4) (4,4) (4,3), 8 boxes; dead ends (1,1) and (3,2); unique | route | agrees |
| S1-12 (2) | 5% S, 400 Q, 30% U, 420 A, 320 R, 340 E | SQUARE | agrees |
| S1-13 | k÷3 S, n+4 T, 6y U, t-7 D, p-9 I, 8w O | STUDIO | agrees |
| S1-14 | W, A, L, R, U, S (J and X unused) | WALRUS | agrees |
| S1-15 (2) | dominoes close in the order B O T A N Y (values 40, 17, 48, 18, 39, 53) | BOTANY | agrees |
| S1-16 (2) | w 6 C, p 26 R, k 2 A, n 29 F, y 3 T, t 23 Y | CRAFTY | agrees |
| S1-17 | 176 C, 88 O, 154 U, 22 S, 66 I, 44 N | COUSIN | agrees |
| S1-18 (2) | 50.24 F, 153.86 R, 200.96 O, 314 Z, 12.56 E, 28.26 N | FROZEN | agrees |
| S1-19 (2) | 19.25 H, 38.5 U, 25 N, 72 G, 100 R, 308 Y (S and Q unused) | HUNGRY | agrees |
| S1-20 (2) | P 42, O 68.25, L 94.5, I 371, C 385, E 614.25 | POLICE | agrees |
| S2-01 | 1036 S, 273 U, 42 N, 476 D, 64 A, 56 Y | SUNDAY | agrees |
| S2-02 (2) | 100 W, 76 A, 54 L, 64 N, 142 U, 25 T | WALNUT | agrees |
| S2-03 | 8 C, 14 O, 5 U, 11 G, 12 A, 15 R | COUGAR | agrees |
| S2-04 | route (1,2) (2,2) (3,2) (4,2) (4,3) (4,4) (3,4) (2,4), 8 boxes; dead ends (1,3) and (2,1); unique | route | agrees |
| S2-05 (2) | 45 C, 52 A, 9 N, 14 O, 6 P, 49 Y (Z and F unused) | CANOPY | agrees |
| S2-06 (2) | 8 N, 11 U, 50 M, 14 B, 93 E, 40 R | NUMBER | agrees |
| S2-07 | 100 P, 116 E, 137 A, 46 N, 95 U, 75 T | PEANUT | agrees |
| S2-08 (2) | 37 W, 86 I, 38 Z, 15 A, 75 R, 55 D | WIZARD | agrees |
| S2-09 | 129 S, 70 T, 80 R, 90 O, 72 N, 50 G (L and K unused) | STRONG | agrees |
| S2-10 | 29 F, 82 A, 57 B, 13 R, 35 I, 74 C | FABRIC | agrees |
| S2-11 (2) | 36 D, 17 O, 73 N, 186 K, 33 E, 37 Y | DONKEY | agrees |
| S2-12 (2, colour) | Y 27, R 36, B 48, G 64, O 72. Left and right mirror parts agree; tally Y2 R4 B2 G4 O2 | tally | agrees |
| S2-13 (2) | Badminton 45%: 180 F, 2 I, 40 G, 80 U, 340 R, 45 E | FIGURE | agrees |
| S2-14 | F 1/6, A 3/8, M 7/12, I 1 1/3, L 7 1/2, Y 8 3/4 | FAMILY | agrees |
| S2-15 (2) | 77 M, 30 A, 91 G, 117 N, 80 E, 108 T | MAGNET | agrees |
| S2-16 | 100.48 S, 157 H, 200.96 A, 14 D, 615.44 O, 82.24 W | SHADOW | agrees |
| S2-17 | route (4,2) (4,1) (3,1) (2,1) (2,2) (2,3) (1,3) (1,4), 8 boxes; (1,1) and (4,3) dead ends; unique | route | agrees |
| S2-18 | 90 T, 20 U, 54 R, 436 K, 36 E, 45 Y | TURKEY | agrees |
| S2-19 (2) | loop from START: W O M B A T (values 49, 4, 15, 24, 38, 12) | WOMBAT | agrees |
| S2-20 (2, colour) | Y 15 (four), R 24 (three), B 35 (two), G 48 (three), O 60 (two): 12÷1/4 and 32÷2/3 = 48; 3÷1/5, 12÷4/5, 25% of 60, 75% of 20 = 15; 7÷1/5, 21÷3/5 = 35; 4n+12=252 n=60 and 5n+20 = 60; 6n+20=164 n=24, 6n+12 = 24, average 24; 5n+6=246 n=48 | tally | agrees |

Colour pages: the pupil sheet and key print the same questions, the tally matches my count, and the small shape marks (S1-09) or mirror position (S2-12, S2-20) join only parts of the same colour. The key and the page agree on every part.

### Not-to-scale angle pages (S2-07, 08, 09), re-measured from the drawn points in `S2_pupil.html`

Unknown angle, drawn against true: S2-07 115.8/100, 97.5/116, 146.7/137, 63.6/46, 106.2/95, 84.3/75; S2-08 24.9/37, 75.2/86, 28.9/38, 24.3/15, 86.9/75, 45.2/55; S2-09 143.1/129, 50.1/70, 62.4/80, 73.0/90, 81.5/72, 82.6/50. **Every unknown is drawn 9.3 to 32.6 degrees away from the truth** (smallest S2-08 item 4, 9.3 degrees, then S2-09 item 5, 9.5), so the key's "at least 9 degrees" is now true (round-2 M3a fixed; builder changed the floor from 7 to 9 for answers under 30). No unknown or given angle is drawn under 24 degrees. Acute stays acute and obtuse stays obtuse for every given label and every unknown (checked all 18 figures against the 88 to 92 degree band the generator uses). Measuring and choosing the nearest table value therefore does not give the word.

Label association (round-2 M1): on the committed PDFs the `?` and each number now sit at their own arc on S2-07 items 3 and 4, and S2-08 item 1 (`106°` on the D arc, `?` on the small A arc). Fixed. See L4 for the two figures that are still crowded.

## 3. Code words

- 33 words in P6, all different: BANDIT BOTANY CANOPY COUGAR COUSIN CRAFTY CREAMY DEVOUR DONKEY FABRIC FAMILY FATHOM FIGURE FROZEN FRUITY HUNGRY MAGNET MONKEY NUMBER PEANUT POLICE SHADOW SHRIMP SQUARE STRONG STUDIO SUNDAY TEACUP TURKEY WALNUT WALRUS WIZARD WOMBAT. No two are anagrams. MONKEY (S1-03) and DONKEY (S2-11) differ by one letter and sit in different booklets (the pupil cannot reach one from the other). None is printed on any pupil page or front matter.
- I read "Code word / Word" from the Answer Key PDFs of P1 to P6 myself (not by running `refresh_other_words.py`, which writes `p5/gen/other_levels_words.json`). **No P6 word is a P5 word** (P5 is clean). **30 of the 33 P6 words are also code words in P1, P2, P3 or P4**; only SUNDAY, COUGAR and STRONG are unique to P6. Examples: DONKEY in P1 S2, P2 S2, P3 S2, P4 S2; FIGURE in P2 S2, P3 S1, P4 S1; WIZARD, FRUITY, CREAMY, FROZEN and others in three levels. Earlier audits (P4 round 3, P5 round 3) record cross-level repetition as an owner decision, not a P6 defect; P6 has no check against the other levels (P5's `validate.py` has one). See L1.
- The round-2 anagram, single-slip and ordering tests for the words are unchanged (no word changed since round 2).

## 4. Black-and-white photocopy readiness

- All eight PDFs contain no raster images and no non-grey drawing colour (PyMuPDF over every vector path: 0 coloured paths). No flat grey; the committed `validation_report.txt` reports 744 checks, 0 failed (I did not re-run it).
- No colour-only information: colour pages carry the colour names and a Y/R/B/G/O writing option and, on S1-09, shape marks; the key states the colour of each part in words; S2-12 and S2-20 use mirror position.
- Minimum text size on all pupil pages (Puzzles, FrontMatter, Pack) 7.99 pt (about 8). Answer-key pages have 7.23 pt letters (colour-letter thumbnails of the three colour pages; teacher side only, see L3).
- **Box sizes (round-2 L1 fixed):** colour-page answer boxes are now 9.8 mm (S1-09) and 10.0 mm (S2-12, S2-20), up from 8.0 and 8.2. Other answer boxes are 13 mm high and 20 to 58 mm wide; letter boxes on matching and choice pages are 8 mm; the check-strip boxes are 7 mm (one letter each).
- Hatching (S1-20 L and P, S2-01 items 3 and 4, S2-02 item 1): visible in a 150 dpi 1-bit render; the thin lines break into dashes in the narrow sliver of S2-01 item 3. Cannot be proved without a copier (L2).
- No coin or banknote picture anywhere in P6 (no image streams; "$" appears only in text), so nothing to reproduce; `coin_reproduction_check.md` does not apply.
- Page counts: each Puzzles booklet has 20 pages (even). FrontMatter has 5, Keys 9 and 10, Complete Packs 25: odd counts are by design (single-sided A4). A duplex print of a pack ends with a blank back (info).

## 5. MOE outcome numbers

Compared the printed numbers with the syllabus PDF pages 43 and 44 (and the Foundation pages as quoted in `p6_outcome_wording.md`): Fractions 1.1 and 1.2; Percentage 1.1 and 1.2; Ratio 1.1 to 1.7; Algebra 1.1 to 1.5; Area and Circumference of Circle 1.1 to 1.3 (printed as "Area and Volume 1.x"); Volume of Cube and Cuboid 2.1 to 2.5; Geometry 1.1; Statistics 1.1 and 1.2. **All numbers exist and carry the right meaning**; the key's first page now says "the outcome numbers follow the syllabus; the notes on each tag are our own words", which is true (round-2 M3b fixed). Cover and licence page have no alignment claim; only "Not affiliated with or endorsed by the Ministry of Education, Singapore." No price, "MOE-aligned", SASMO, PSLE or GEP wording in any of the eight PDFs.

## 6. Findings

**High: none.**

### Medium

- **M1. Coverage table and key tags name item types that are not on five pages.** The S1 and S2 front matter ("What the booklet covers") and the key tags and teacher notes say:
  - **S1-09** (Colour the Car): Ratio 1.3 (dividing a quantity in a ratio), and the key note says "a share of a quantity shared in a ratio". The page has no such item (items are missing terms, percentage of a number, the whole, and "before a percentage increase").
  - **S2-20** (Colour the Elephant): Ratio 1.3. No ratio item on the page.
  - **S2-19** (Mixed Bag): Primary 6 Foundation Area and Volume 2.1 to 2.3, "volume of a cuboid" in the key note, and "volume" in the printed topic line (a pupil sees "... letters and volume"). The twelve halves have no volume item.
  - **S2-12** (Colour the Butterfly): "Area and Volume 2.1 a missing dimension of a cuboid" and "2.2 edge of a cube from its volume". The cuboid and cube items give the dimensions and ask for the volume (3x3x4, 3x4x4, 2x4x6, cube edge 3); only the two "height from volume and base area" items are 2.3.
  The numbers are real syllabus lines, but the front matter lists these pages under lines the pupil does not practise there. This is the front-matter claim a school reads. Fix: remove S1-09 and S2-20 from Ratio 1.3 (S1-09 stays under 1.2, 1.6, Percentage 1.1 and 1.2), remove S2-19 from Foundation 2.1 to 2.3 and the word "volume" from its topic and note, and for S2-12 keep only AV 2.3 (and note "volume of a cuboid or cube" as earlier-year content) in the key, the tags and the coverage table. Alternatively add a matching item. Text-only change.

### Low

- **L1. Code words repeat across levels.** 30 of 33 P6 words are also codes in P1 to P4 (section 3). Not a P6 rule so far; if the owner wants one word set per level, P6 needs 30 new words plus a check like P5's `validate.py` line against `other_levels_words.json`. Owner decision (carried from earlier rounds).
- **L2. Thin hatch.** In 1-bit the hatch is dashed in narrow slivers (S2-01 item 3 and S1-20 L and P). Test on a real copier.
- **L3. Key thumbnails use 7.23 pt letters** (S1 key p.4, S2 key pp.5, 8): below the 8 pt rule the validator checks (the validator reports 8.0 pt, so it misses these). Teacher side only.
- **L4. S2-08 items 1 and 3 are crowded** at 150 dpi 1-bit: `106°` and `?` close to the line AE in item 1; `104°`, `?` and the diagonal AC meet in item 3. Readable, and each number is on its own arc.
- **L5. Square and cube-root signs have no overbar** (S2-04, S2-19: "√4 + 4"; "√121 + 4"); the cube-root index "3" is small. Same as round-2 L3 and L7; the key's answers assume the root of the first number only.
- **L6. S1-19 item 4:** answer box still touches the item card's border (round-2 L8, not fixed).
- **L7. Foundation pages:** S2-13, S2-17, S2-18 and part of S2-19 are Primary 4 and 5 or Foundation lines for a Standard pupil. The front-matter note now reads "Pages tagged Primary 6 Foundation revise earlier-year content and are Foundation-..." (fixed in substance). Owner kept them (decision 2).
- **L8. Two-step equations on S1-16 and S2-20.** The syllabus line does not say how many steps; the key's note names them. Teacher-note suggestion from round 2 (add "check your scheme of work") not required.
- **L9. Reproducibility.** The committed PDFs need the repo's `fonts` folder to rebuild; a fresh container build differs in line wrapping (documented in `BUILD_REPRODUCIBILITY.md` and the colour-page guard note). I did not rebuild; all findings are on the committed PDFs.

### Round-2 status

| Round 2 | Status now |
|---|---|
| M1 label association (S2-07 items 3 and 4, S2-08 item 1) | **Fixed** on the PDFs (section 2) |
| M2 S2-01 item 4 square | **Fixed**: "square 28 cm" printed under the figure |
| M3a "at least 9 degrees" | **Fixed**: smallest drawn offset is 9.3 degrees |
| M3b "outcome lines are quoted" | **Fixed**: key says numbers follow the syllabus, notes are our words |
| M3c S2-09 decoys "180 minus the answers of two of the figures" | **Fixed** |
| L1 colour-page boxes 8.0 and 8.2 mm | **Fixed**: 9.8 and 10.0 mm; the guard commit `a91e866` adds a sheet-versus-PDF text check (validator lines present) |
| L2 word-list note, L3 cube-root, L5 and L6, L8 | L3, L8 still open (Low); L5 (stray comma in S2-02 instruction) and L6 (acute and obtuse flip) fixed |

## 7. What I could not check

- No photocopier, pupil trial or teacher read-through; no lawyer review of the licence.
- I did not re-run `validate.py` or `similarity_check.py`; the three pages replaced in round 2 were already compared with private sources in round 2 and no page text changed except the nine pages above (layout, not wording). I did not re-run the dictionary slip tests: no code word changed since round 2.
- The cross-level word check reads the Answer Key PDFs as they stand today; other levels may still change.

## 8. Fixes applied (24 Oct 2026)

Text and layout only. No puzzle, answer, code word or colour-page content changed; the three colour pages keep their pictures, parts, keys and tallies.

| Finding | Fix |
|---|---|
| M1 S1-09 | Ratio 1.3 removed from the page's tags (now Ratio 1.2, 1.6, Percentage 1.1, 1.2), from the key's tag note and from the teacher note ("a share of a quantity shared in a ratio" deleted). Front-matter table: Ratio 1.3 now lists S1-06 only. |
| M1 S2-20 | Ratio 1.3 removed from the tags and the teacher note ("a share in a ratio"). Front-matter table: Ratio 1.3 now S2-15, S2-19. |
| M1 S2-19 | The word "volume" removed from the printed topic line (now "...roots and letters"), from the key's tag note and from the teacher note; Primary 6 Foundation Area and Volume 2.1 to 2.3 removed from its outcome ids (it stays on S2-06). Ratio 1.3, Volume 2.5 and the rest are unchanged (the page has a ratio half and a root half). |
| M1 S2-12 | Only Volume 2.3 and Statistics 1.1, 1.2 are tagged. The key note says the volume-from-the-edges parts are earlier-year content. Front-matter table: Volume 2.1 now S2-03 only, Volume 2.2 now S2-05 only. |
| L3 | Colour-letter thumbnails on the teacher key (S1 key p.4, S2 key pp.5 and 8) enlarged from 7.2 pt to 8.9 pt. |
| L6 | S1-19: the gap between the figure and the "Perimeter" or "Area" word is 1 mm on this page's cards, so item 4's box now has about 2.3 mm clear of the card border (was touching). Answers untouched. |

Every outcome line is still practised by at least one page (the validator's coverage check passes; Ratio 1.3, Volume 2.1, 2.2 and Foundation Volume are carried by other pages).

Rebuild and checks: rebuilt per `docs/school_books/BUILD_REPRODUCIBILITY.md` into the default `school/p6/out` (fonts load). Pixel diff (70 dpi, per page) against the committed PDFs: changed pages only S1 key p.4 (S1-09 entry), S2 key pp.5 and 8 (S2-12 and S2-20 entries), S2 Front Matter p.5 (coverage table), S1 Front Matter p.5 (coverage table), S1-19, S2-19 and the same pages inside the Complete Packs. All other pages are pixel-identical. Text diff of the changed files shows only the lines above. `validate.py` (default outdir): 753 checks, 0 failed, no failures (keys match the solved pages; the validator re-solves every page from its printed content).

### Cross-level code words (L1) and the missing check

P6's `validate.py` has no check against other levels' code words (P5's has, using `p5/gen/other_levels_words.json`). I did not add one: 30 of the 33 P6 words are already codes in P1 to P4, so a hard check would fail on the owner-accepted repetition, and an always-passing line would only mislead. If the owner decides one word set per level, P6 needs 30 new words and then a check like P5's (`refresh_other_words.py` writes the list from the other levels' Answer Key PDFs).

### Still open

L1 (cross-level words, owner decision), L2 (hatch on a real copier), L4 (S2-08 crowding), L5 (overbars), L7 and L8 (owner decisions), and everything in section 7 (copier, pupil trial, lawyer).
