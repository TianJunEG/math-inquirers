# Independent audit, round 2: Primary 6 early-finisher booklets (Semester 1 and Semester 2)

Auditor: independent second-round check (not the builder, not the round-1 auditor's files). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`, HEAD `6d8683a` (PDFs built 23 Oct 2026 21:01). Nothing pushed, no PR, no builder file edited; only this report was added.
Round 1 audited commit `1c50639`; I diffed the PDFs of that commit against the working tree (text and 100 dpi pixels, both booklets). Read: `docs/audit_final/p6_semester_booklets_audit.md`, `docs/school_books/p6_semester_booklets_build_report.md`, `p6_semester_booklets_plan.md`, `p6_outcome_wording.md`, `docs/school_books/plan.md` (reading-load table), the MOE syllabus PDF (Primary 6 Standard pp. 43-44, Foundation pp. 49-50, and the Primary 4 and 5 pages for placement; data only).

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **Content ready.** Four pages changed (S1-12, 14, 19, 20); all hand-solved, all agree with the key. Only lows remain. Still DRAFT by the owner's rule (lawyer, pupil trial, photocopier). |
| Semester 2 | **Content ready after three small fixes** (M1 label association on two angle figures, M2 one figure that needs the word "square", M3 three false or loose sentences in the key). No wrong key, no unsolvable page. Still DRAFT. |

**No High.** 18 pages changed since round 1; all 18 were solved by hand from the PDF image before looking at the key, and 18 of 18 agree (0 wrong keys, 0 pages with two answers). The other 22 pages are pixel-identical to the PDFs round 1 solved, so round 1's 22 solves stand. All 33 code words differ; no other real word is reachable (section 3). Outcome numbers on both keys are all correct against the PDF (section 5). The three new pages are original (section 7).

## 1. Which pages changed (diff of round-1 PDFs against the current PDFs)

Changed by pixels and text (18): **S1-12, S1-14, S1-19, S1-20, S2-01, S2-02, S2-04, S2-05, S2-06, S2-07, S2-08, S2-09, S2-10, S2-11, S2-13, S2-14, S2-15, S2-16**. The build report lists 15 re-solved pages; the three it leaves out (S1-14, S1-19, S2-05) changed only by the new "Two cards are not used" sentence, and S1-12 by a shortened instruction. Unchanged (22): S1-01 to 11, 13, 15 to 18; S2-03, 12, 17, 18, 19, 20. Note: **S2-12, S2-20 and S1-09 (colour pages) are pixel-identical to round 1**, so the "colour-page boxes 9 mm" change is not in the PDFs (see L1).

### Per-page table of the changed pages

"Mine" is my answer from the image, before the key. Key agrees in every row.

| Page | What changed | My answer from the image | Code word | Check of the change | Page verdict |
|---|---|---|---|---|---|
| S1-12 P6-12 Percent Stories | Instruction shortened to 3 sentences | 5% S, 400 Q, 30% U, 420 A, 320 R, 340 E | SQUARE | Text otherwise identical | OK |
| S1-14 P6-14 Simplify | "Use each card once. Two cards are not used." | 14p+12 W, 6a+5 A, 14k+14 L, 5y+12 R, 5w+5 U, 7t+12 S; J and X unused | WALRUS | 8 cards, 6 items: sentence now true | OK |
| S1-19 P6-19 Half and Quarter | same sentence; pi 22/7 | 19.25 H, 38.5 U, 25 N, 72 G, 100 R, 308 Y; S (44 cm) and Q (25 cm²) unused | HUNGRY | OK. Item 4's answer box touches the card border (L8) | OK |
| S1-20 P6-20 Curves and Corners | Arch figures O, E: dimension line along the square's side and the word "square"; hatch 0.55 | P 42, O 68.25, L 94.5, I 371, C 385, E 614.25 | POLICE | Arch fix works: "7 cm" and "21 cm" are now clearly the square's side; semicircle diameter = side. Hatching visible at 150 dpi 1-bit | OK |
| S2-01 P6-21 Shaded Shapes | Item 2 arch fixed; hatch 0.55 | 1036 S, 273 U, 42 N, 476 D, 64 A, 56 Y | SUNDAY | Item 2 fixed. **Item 4 (only "28 cm"; hatched square with a semicircle cut out) has no "square" and no second dimension: 476 needs the square reading (M2)** | OK after M2 |
| S2-02 P6-22 Perimeter Pick | Item 4 arch fixed; instructions to 5 sentences | W 100, A 76, L 54, N 64, U 142, T 25 | WALNUT | Item 4 fixed. Instruction reads "Find the perimeter, of the hatched part if there is hatching." (stray comma, L5) | OK |
| S2-04 P6-24 Root Maze | Retitled; bigger bold cube-root sign | Equal to 6: route (1,2) (2,2) (3,2) (4,2) (4,3) (4,4) (3,4) (2,4), 8 boxes; dead ends (1,3) and (2,1); unique | route | Cube-root index "3" legible at 150 dpi 1-bit but still small (L3) | OK |
| S2-05 P6-25 Base and Height | "Two cards are not used" | 45 cm² C, 52 cm² A, 9 cm N, 14 cm O, 6 cm P, 49 cm² Y; Z (9 cm²) and F (46 cm²) unused | CANOPY | OK | OK |
| S2-06 P6-26 Tank Stories | Tank dimensions changed (no 80x50x20 tank) | 8 N, 11 U, 50 M, 14 B, 93 E, 40 R | NUMBER | Item 3: 30 l is 3/4 of the tank, depth 37.5, height 50. Item 6 40x50x40 half full = 40 l. No tank now matches a private entry (section 7) | OK |
| S2-07 P6-27 Angles in Figures | Not to scale; labels re-placed | 120 P, 85 E, 136 A, 22 N, 122 U, 80 T | PEANUT | Section 2. Label association weak on items 3 and 4 (M1) | OK after M1 |
| S2-08 P6-28 More Angles | Not to scale; code word SPONGE to WIZARD | 35 W, 78 I, 36 Z, 15 A, 75 R, 29 D | WIZARD | Section 2. Item 1 crowded (110 label on the far side of CD, `?` on line AE) | OK after M1 |
| S2-09 P6-29 Angle Match | Not to scale; "Two cards are not used" | 129 S, 70 T, 80 R, 90 O, 72 N, 50 G; L (100) and K (110) unused | STRONG | Section 2. Cards L and K are 180 minus the answers of items 3 and 2 | OK |
| S2-10 P6-30 Average | Code word CURFEW to FABRIC | 29 F, 82 A, 57 B, 13 R, 35 I, 74 C | FABRIC | Same questions as round 1 | OK |
| S2-11 P6-31 Missing Value | Code word FABRIC to DONKEY | 36 D, 17 O, 73 N, 186 K, 33 E, 37 Y | DONKEY | Same questions | OK |
| S2-13 P6-33 Pie Chart | Code word DONKEY to FIGURE; Foundation tag | Badminton 45%: 180 F, 2 I, 40 G, 80 U, 340 R, 45 E | FIGURE | Chart, labels and sectors consistent (20, 10, 15, 10 and the 45 left) | OK |
| **S2-14 P6-34 Fraction Order (new)** | Replaces Net or Not | I 1/2 ÷ 3/8 = 1 1/3; L 5 ÷ 2/3 = 7 1/2; M 1/3 ÷ 4/7 = 7/12; Y 7 ÷ 4/5 = 8 3/4; A 3/4 ÷ 2 = 3/8; F 5/6 ÷ 5 = 1/6. Order smallest first: F A M I L Y | FAMILY | Correct and unique order (smallest gap between answers 5/24). Two items per type as the key says | OK |
| **S2-15 P6-35 Ratio Stories (new)** | Replaces Taps and Rates | 1) 132 pupils 5:7, girls 77 M; 2) 7:2, $75 more, Jun $30 A; 3) 4:9, 28 red, 91 G; 4) 2:4:7, 18 red, 117 N; 5) 4:1, 80% E; 6) 5:9, 60, Jun 108 T | MAGNET | Correct, one answer each, no ambiguity. Longest sentence 15 words | OK |
| **S2-16 P6-36 Circle Choices (new)** | Replaces Mixed Numbers | 1) 100.48 S; 2) 157 H; 3) 200.96 A; 4) r = 87.92/6.28 = 14 D; 5) 615.44 O; 6) 50.24 + 32 = 82.24 W | SHADOW | Correct; pi 3.14 stated; wrong options are typical slips. Large empty gaps above and below the list (cosmetic) | OK |

## 2. The not-to-scale angle pages (S2-07, 08, 09), the key point of round 2

**Method.** The data attributes in `school/p6/out/S2_pupil.html` carry both the drawn point (cx, cy) and the true point (data-tx, data-ty). I computed the angle at every drawn arc from the drawn points and compared it with the label or the true value; I also checked three pictures by eye from the PDF (S2-09 item 3, drawn about 109 degrees, matches the HTML's 111). Nothing printed shows the true shape, and the page says "Not drawn to scale: work it out, do not measure." (instructions on all three pages; teacher notes and front matter agree).

| Page, item | True answer | Drawn (what a protractor reads) | Off by | Measuring then picking the nearest table value gives |
|---|---|---|---|---|
| S2-07 1 | 120 | 108.6 | 11.4 | right (120) |
| S2-07 2 | 85 | 56.4 | 28.6 | wrong (70) |
| S2-07 3 | 136 | 150.7 | 14.7 | wrong (141) |
| S2-07 4 | 22 | 29.8 | **7.8** | right (22) |
| S2-07 5 | 122 | 133.6 | 11.6 | wrong (136) |
| S2-07 6 | 80 | 95.8 | 15.8 | wrong (85) |
| S2-08 1 | 35 | 23.1 | 11.9 | wrong (29) |
| S2-08 2 | 78 | 88.5 | 10.5 | right (78) |
| S2-08 3 | 36 | 49.6 | 13.6 | right (36) |
| S2-08 4 | 15 | 23.3 | **8.3** | wrong (29) |
| S2-08 5 | 75 | 91.9 | 16.9 | wrong (78) |
| S2-08 6 | 29 | 36.3 | **7.3** | wrong (36) |
| S2-09 1 | 129 | 143.1 | 14.1 | right (129) |
| S2-09 2 | 70 | 50.1 | 19.9 | wrong (50) |
| S2-09 3 | 80 | 111.1 | 31.1 | wrong (card K 110, an unused card) |
| S2-09 4 | 90 | 73.0 | 17.0 | wrong (72) |
| S2-09 5 | 72 | 81.5 | 9.5 | wrong (card R 80) |
| S2-09 6 | 50 | 27.5 | 22.5 | right (50) |

Result: **a pupil who measures and takes the nearest code-table entry gets 2 of 6 letters on each page and never the word** (the word needs all six). The measured values are not the answers (smallest gap 7.3 degrees). Every labelled arc is also drawn 7 to 31 degrees away from its label, so measuring contradicts the printed numbers, as the page warns. No drawn angle is below 23 degrees. No figure looks broken: triangles, rhombi, parallelograms, trapezia and the square figures are plausible shapes with equal-side ticks and parallel chevrons in place; no side is very short. **The three items under 30 degrees are drawn only 7.3 to 8.3 degrees off, below the "at least 9" the task and the key promise** (the builder's own rule was 7 for answers under 30; the S2-07 teacher note still says "at least 9 degrees"). I judge 7 degrees enough in practice (a protractor read of 29.8 for 22 is clearly not 22), so this is a wording fix in the key, not a figure fix (M3).

**Looks reasonable and unambiguous?** Mostly yes. Weak points (M1 and L6):
- **S2-07 item 3**: the `92°` label sits below the base, 10 mm from its own arc at A and on the other side of line BC. It is solvable (92 as a base angle of an isosceles triangle is impossible), but a pupil has to reason about which arc it labels.
- **S2-07 item 4**: the `?` is placed against the left end of the big arc at A, while the arc at B (the one the question asks for) carries no label nearby and `136°` sits under side AB. A pupil who reads the figure first, not the sentence, attaches `?` to the wrong arc. The sentence "Find angle ABD" resolves it.
- **S2-08 item 1**: `110°` is above side CD, on the other side of the line from its arc at D, and nearer to C. The `?` sits on line AE (the line is broken by the halo) next to a very small arc at A. At 120 dpi 1-bit this item and S2-08 item 4 (`?` between the tick on DE and line AE, tick on DC crossing AE) are the most crowded; still legible.
- L6: the distortion flips acute and obtuse for given angles on four figures (S2-07 item 5 label 79 drawn 97 degrees; S2-07 item 6 label 100 drawn 84; S2-09 item 3 label 100 drawn 69, and its `?` for 80 drawn 111; S2-09 item 6 label 80 drawn 120). It is allowed by "not to scale" but a pupil who sketches will notice.

## 3. Code words: uniqueness

All 33 words: CREAMY, MONKEY, SHRIMP, TEACUP, BANDIT, DEVOUR, FATHOM, FRUITY, SQUARE, STUDIO, WALRUS, BOTANY, CRAFTY, COUSIN, FROZEN, HUNGRY, POLICE, SUNDAY, WALNUT, COUGAR, CANOPY, NUMBER, PEANUT, WIZARD, STRONG, FABRIC, DONKEY, FIGURE, FAMILY, MAGNET, SHADOW, TURKEY, WOMBAT (read from the two keys). **No duplicate, no two are anagrams.** MONKEY (S1-03) and DONKEY (S2-11) differ by one letter; they sit in different booklets and the letter M is not on the S2-11 table, so it is not reachable.

**Dictionaries (my own, not the builder's pipeline):** python `english-words` 2.0.2 (web2 and gcide), `wordfreq` 3.1.1 top 250 000 (alphabetic), and the builder's `words_en.txt.gz` (207 399). Union, six-letter entries: 47 369 words; common list (wordfreq top 30 000 and builder's `words_common`): 5 875. Hits were judged by hand.

Tests, on the changed code-word pages (SQUARE, SUNDAY, NUMBER, PEANUT, WIZARD, FABRIC, DONKEY, FIGURE, MAGNET) and the choice, matching and ordering pages (WALNUT, SHADOW, WALRUS, HUNGRY, CANOPY, STRONG, POLICE, FAMILY):
- code-table pages: all 720 orderings of the six letters, every single slip using any letter on that page's table, every single slip using any of 26 letters, double slips with table letters (common list);
- choice pages (S2-02, S2-16): all 3^6 = 729 selections; matching pages (S1-14, S1-19, S2-05, S2-09): every way to give the six items different cards from the eight (20 160 strings each); ordering pages (S1-20, S2-14): all 720 orders.

Result: **no other real word by any rearrangement, any single slip with a table letter, any choice, any card assignment or any ordering, on any of the 17 pages.** The only non-page word found anywhere is `stronk` (matching, S2-09; slang, not a word). Single slip with a letter that is not on the table (not reachable by a pupil): WIZARD gives LIZARD (needs L, not on the table), DONKEY gives MONKEY, HONKEY (not on the table), SUNDAY gives SUNDAE and SUNDRY, SQUARE gives SQUIRE. Double slips (two wrong answers at once, common list): SUNDAY to SANDAL; NUMBER to BUMMER, BUMPER, JUMPER, MEMBER, RUBBER; DONKEY to CONVEY, DOCKED, JOCKEY; MAGNET to MANNED. Each needs two simultaneous slips; the teacher notes already say two wrong answers were not all tested. SPONGE is gone (WIZARD replaces it); no vulgar or alarming word is reachable by one slip. The replaced words (FABRIC, DONKEY, FIGURE, NUMBER, MAGNET, SHADOW, FAMILY, WIZARD) are all clean.

The teacher notes still say "about 207 000 words"; the validator's single-slip test on code-table pages uses 129 000 words (L-G of round 1, not changed; my test with the union list confirms the claim).

## 4. Foundation-track pages and two-step equations (scope against the PDF)

I read the Primary 4, 5 and 6 pages for placement.

- **Pie charts (S2-13), decimal multiply/divide (S2-17), discount and GST (S2-18), tank volume (S2-06):** each is a Primary 6 Foundation line (pp. 49-50), but for a **Standard** pupil each was met earlier: pie charts as reading from pie charts in Primary 4 (p. 40, 1.2); decimals as multiply/divide by 10, 100, 1000 and by a 1-digit number in Primary 4 and 5 (pp. 38, 41); discount, GST, annual interest as Primary 5 Percentage 1.4 (p. 41); liquid in a rectangular tank as Primary 5 Volume 2.5 (p. 42). They are therefore **Primary 4 and 5 revision for the Standard pupil**, not Primary 6 content, and the tag "Primary 6 Foundation" is true but does not tell the teacher that. Judgement: **acceptable as revision in the Semester 2 (Terms 3 and 4) booklet** because these are the topics a Primary 6 class revisits in Term 3 and 4 papers and the key tags are honest, the page count is small (4 of 20 plus the mixed pages), and the owner decided to keep them (build report decision 2). Two fixes are cheap: (a) change the front-matter sentence "Pages tagged Primary 6 Foundation practise lines of the Foundation track that Standard pupils also meet" to say what is true, "revisit lines that Standard pupils met in Primary 4 and 5 and that the Foundation track repeats in Primary 6"; (b) keep the cover claim "Primary 6" but do not call these pages Standard content anywhere. If the owner wants only Standard content, replace S2-17 first (Primary 4 and 5 decimals, least likely to be asked in Primary 6 papers), then S2-13.
- **Two-step equations on S1-16:** the only syllabus statement is Algebra 1.5, "simple linear equations involving whole number coefficient only" (p. 43). It does not limit the number of steps; "whole number coefficient only" limits the coefficient, not the steps. The Foundation track has no algebra, so this is Standard-only. Items 1, 2, 3 and 6 are two-step (9w − 14 = 40; 2p + 15 = 67; 6k + 18 = 30; 2t + 12 = 58); items 4 and 5 are one-step. Verdict: **in scope as written** (equations of the form ax + b = c with whole-number a, b, c fit the line) and a two-star page; I cannot prove from the PDF that every school teaches two-step, so keep the existing key sentence and add "check your scheme of work" to the S1-16 teacher note. The same applies to S2-20 (3n + 6, 2n + 4 = 52, 3n + 15 = 120, 8n + 3 = 283).

## 5. Keys: outcome numbers and wording against the PDF

**Numbers: all correct.** For all 40 pages I compared the numbers on the tag with the PDF and with what the page asks.
- Fractions 1.1, 1.2; Percentage 1.1, 1.2; Ratio 1.1 to 1.7 in the PDF's order (1.1 notation, 1.2 equivalent ratios, 1.3 dividing a quantity in a ratio, 1.4 simplest form, 1.5 ratio of two or three quantities, 1.6 missing term, 1.7 fraction and ratio); Algebra 1.1 to 1.5; "Area and Volume 1.1 to 1.3" = Area and Circumference of Circle 1.1 to 1.3; "Area and Volume 2.1 to 2.5" = Volume of Cube and Cuboid 2.1 to 2.5; Geometry 1.1 = Special Quadrilaterals 1.1; Statistics 1.1 and 1.2: all match the PDF.
- Foundation tags: Statistics 1.1 (pie charts), Decimals 1.1, Percentage 1.3 and 1.4, Area and Volume 2.1 to 2.3 (S2-06, S2-19): all match p. 49-50.
- Each changed page's tag fits its items (S2-14: FR1.1 and 1.2; S2-15: RA1.2, 1.3, 1.6, 1.7; S2-16: AV1.1, 1.2; S2-05: VO2.3, 2.4, 2.2; S2-06: VO2.3 and Foundation 2.2, 2.3; S2-04: VO2.5).
- Minor: the key prints "Area and Volume 2.1" for the Standard line and "Primary 6 Foundation Area and Volume 2.1 to 2.3" for the Foundation one; both strands in the PDF are called "Area and Volume" with different line numbers (Standard 1.x = circles, Foundation 1.x = triangle area). The word "Foundation" is printed whenever it is the Foundation line; fine.

**Wording: not what the key claims.** The first page of both keys says "The outcome lines are quoted from the syllabus; the notes on each tag are our own words". In the entries, the outcome line is **not** printed as a quote; only the number and a note in the builder's words appear, and the notes are a mix: S1-16 and S2-10/11 copy the PDF's words (ok), but most are paraphrase (S2-03 "a missing dimension" for the PDF's "one dimension"; S2-07 "squares, rectangles, triangles, parallelograms, rhombuses and trapeziums" for the PDF's singular list; S2-14 "dividing by a proper fraction"). The Ratio, Fractions and Algebra lines in `p6_outcome_wording.md` are the PDF's verbatim wording, but `outcomes.py` shows only the short phrases on the printed pages. So the key's sentence is wrong either way. Fix: either print the PDF's lines verbatim in the entries (the PDF is data, copy only the outcome lines) or change the sentence to "the notes on each tag are our own words, the numbers are the syllabus's" (M3). The cover and licence page carry no alignment claim (owner addendum 7 is respected).

## 6. 1-bit legibility of the changed pages

Method: `pdftoppm -mono` at 120, 150, 200 and 300 dpi of every changed page; stroke widths and text sizes from the PDF paths (PyMuPDF).
- Minimum text 8.0 pt (footer only) and minimum stroke 0.24 mm (check strip) on every changed page. No flat grey; the hatch is vector lines (pitch 2.0, width 0.55 units in the SVG, about 0.4 mm in print), the old 0.35 value is gone. At 150 dpi mono S1-20 L and P, S2-01 items 3 and 4 and S2-02 item 1 are clearly hatched, though the lines break into dashes in the narrow sliver at the top of the quarter-circle figures; test on a real copier with the thin hatch (L-D of round 1 still stands).
- Arch figures (S1-20 O and E, S2-01 item 2, S2-02 item 4): the dimension line, the word "square" and the dashed diameter are all readable at 150 dpi mono; the word "square" is 6.5 to 7 pt, thin; fine.
- Angle pages at 300 dpi mono: the halos that cut the lines behind `36°`, `43°`, `?`, `108°`, `122°` leave the text readable. At 120 dpi mono S2-08 items 1 and 4 are crowded (small arc, tick, `?` and line meet within 3 mm).
- S2-04: the cube-root index "3" is 1.5 mm tall at 150 dpi 1-bit; distinguishable from the square-root sign (L3). The square-root sign has no overbar, so "√16 + 2" relies on spacing to show the root is of 16 only; school pupils are used to it, but a bar or brackets would remove the doubt (L7).
- S1-19 item 4: the answer box's right side coincides with the item card's border and merges into a thick line at 1-bit (L8). Not a legibility failure.
- New pages S2-14, 15, 16: plain text, boxes of 10 to 12 mm, clean at 100 dpi mono.

## 7. Similarity of the three new pages and the changed pages

My own passes: 5-word runs with at least two content words, and a number-scenario pass (three or more shared non-trivial numbers and three or more shared content words), against (a) all private sources (`docs/books/private_p1..p6_papers` records, notes and tables, `docs/books/private_*.md`, `docs/sasmo/private_*.md`: 23 194 entries) and (b) our own holiday `p6/content/*.js` and `extension/data/l6_*.json` (6 680 text entries).
- **S2-14 Fraction Order:** 0 hits in both sets.
- **S2-15 Ratio Stories:** one 5-word run, "ratio of boys to girls" (private entry is a different question: boys to girls 3:4 and children to adults 1:2); number hits (15, 30, 35, 28, 80) are coincidental in non-ratio private entries and in `p6/content/l4.js` (Level 4 numbers), none a scenario. No shared scenario with a private ratio item or an extension Level 6 item.
- **S2-16 Circle Choices:** no phrase hit. Number overlaps (3.14 with 32, 14, 28) are shared by common circle numbers; the one with answer 82.24 belongs to a private question about overlapping semicircles with a different given (the figure and the question differ). No scenario match.
- **Changed pages:** S2-06 (new tank sizes) shares 40, 20, 30 with a private "empty tank 40 by 20 by 80" entry only in the numbers (different question, different stem); the old 80 x 50 x 20 tank of round 1 is gone. S2-11 and S2-10 have phrase hits ("the average of 7 numbers is", "average mass of 3 boys") that are generic frames with different numbers and operations (taken away, not joined). S1-20: "semicircles and quarter circles" is the outcome's own words.
- **Own material:** no school-booklet page repeats a holiday Level 6 lesson or an `l6_*.json` item.
No 7-word run, no scenario copy. The builder's `similarity_report.txt` (0 flags, run with the original pages) is consistent with my passes; I did not re-run it.

## 8. Reading load (plan.md table: Primary 6, 18 words a sentence, 5 instruction sentences)

Question sentences on the changed pages: longest 17 words (S2-06 item 6, "A tank 40 cm long, 50 cm wide and 40 cm high is half full of water."), then 15 (S2-15 items), 14 (S2-13 item 2, S2-05 item 1). Instructions: all changed pages have 3 to 5 sentences (S1-19, S1-20 4 to 5; S2-02 5; S2-09 5; S2-07 and S2-08 4). The long instruction of S2-09 wraps with one orphan word ("measure."). **Within the limit everywhere.** Vocabulary suits ages 11 to 13. The extra sentences "Marks show equal sides and parallel lines" and "Not drawn to scale: work it out, do not measure." use words the pupil knows.

## 9. Front matter against the owner decisions (both FrontMatter PDFs, both keys, both packs)

Checked and unchanged: annual licence (one school year, renewable); cover publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers"; registered office 66 Tannery Ln, Singapore 347805 on the licence page; (c) 2026 Preciouslyours Pte Ltd; DRAFT stamps on cover, licence, notes and keys; contact pypteltd@gmail.com marked temporary; licence wording marked for a lawyer; "Not affiliated with or endorsed by the Ministry of Education, Singapore." on the cover only; licence page has only the factual "The mathematics syllabus is published by the Ministry of Education, Singapore."; no price, no "MOE-aligned", SASMO, PSLE or GEP wording (searched all eight PDFs); no Mi; 20 single-sided pages per booklet, 10 one-star and 10 two-star; black and white; Complete_Pack text equals FrontMatter + Puzzles in both booklets (25 pages each); key 9 and 10 pages. Changed text: the "Drawings" and "Revision pages" notes, the contents list titles and the coverage table (it now lists "Primary 6 Foundation ..." lines). The sentence "Almost every puzzle checks itself" on the cover remains (not needed; L-M of round 1).

## 10. Findings

**High: none.**

### Medium

- **M1. Label association on three angle figures.** (a) S2-07 item 3: `92°` is under the base and detached from its arc at A. (b) S2-07 item 4: `?` touches the arc at A while the question asks for the arc at B; `136°` sits under AB. (c) S2-08 item 1: `110°` above CD, on the far side of the line from its arc. All are solvable from the sentence, but they are the exact failure mode the round-1 M4 asked to remove ("`?` next to its arc"). Fix: place each number inside its own arc or touching it on the side of the angle, and add a check to the angle reader that the nearest arc to each label is its own (distance and side) so a future change cannot reintroduce it.
- **M2. S2-01 item 4 (hatched square with a semicircle cut out) shows only "28 cm".** The answer 476 needs a square (784 − 308). Same defect class as round 1's M2; the arch figures were fixed but this one was not. Fix: add the word "square" (as on the arch figures) or label the side.
- **M3. Three sentences in the keys are not true as printed.** (a) S2-07 teacher note: the unknown angle differs "by at least 9 degrees"; three items are 7.3, 7.8 and 8.3 (answers under 30 degrees; builder's own rule is 7). (b) First page of both keys: "The outcome lines are quoted from the syllabus"; the entries print numbers and paraphrased notes (section 5). (c) S2-09 teacher note: "Two cards are decoys: 180 minus the answer to one figure"; the decoys L (100) and K (110) are 180 minus the answers of two figures (items 3 and 2). Fix the sentences; the content and numbers are right.

### Low

- **L1.** Build report: "colour-page boxes are 9.0 mm". The three colour pages are pixel-identical to round 1 and the answer boxes are still 8.0 mm (S1-09) and 8.2 mm (S2-12, S2-20). `pages_cbc.py` sets 9.0 only while building and the PDF did not change. Two-digit answers fit; correct the report or rebuild.
- **L2.** The validator's single-slip test on code-table pages still uses 129 000 words against the "about 207 000" in the teacher notes (round 1 L-G). My own test with a larger union passes.
- **L3.** Cube-root index small (S2-04; the domino sign on S2-19 is unchanged and still small, as the build report says).
- **L4.** S2-02 instruction "Find the perimeter, of the hatched part if there is hatching." has a stray comma.
- **L5.** Key S2-14: mixed numbers printed as `1_1⁄3`, `7_1⁄2`, `8_3⁄4` (underscore). Use a space or the stacked form used on the page.
- **L6.** The not-to-scale distortion flips acute and obtuse for given angles on S2-07 items 5 and 6 and S2-09 items 3 and 6 (section 2). Consider capping the distortion so the type of each given angle stays the same (acute, right, obtuse).
- **L7.** Root signs have no overbar (S2-04, S2-19): "√4 + 4" could be read as the root of 8; add a vinculum or a space convention to the teacher note.
- **L8.** S1-19 item 4: the answer box touches the item card's border.
- **L9.** The front-matter sentence "practise lines of the Foundation track that Standard pupils also meet" should say that Standard pupils met these lines in Primary 4 and 5 (section 4); the page tags otherwise correct.
- **L10.** Tag names: the Standard "Area and Volume 1.x" and the Foundation "Area and Volume 1.x" are different lines; the key tags always say "Foundation" for the second; keep that rule if the key is edited. Remaining from round 1: P6-18 item 2 needs 43.96 ÷ 6.28 (a calculator may help); P6-39 still has the small domino cube-root; P6-13 key note fixed.
- **L11.** S2-16 has large empty gaps above and below the six questions; a cosmetic spacing change would use the page better.

### Round-1 items, status

| Round 1 | Status now |
|---|---|
| M1 angle figures to scale | **Fixed** (all unknowns 7.3 to 31.1 degrees off, labels true, page and key say so); wording slip in key (M3a); label flips (L6) |
| M2 arch figures | **Fixed** on S1-20 O and E, S2-01 item 2, S2-02 item 4 (dimension line and "square"); **S2-01 item 4 remains (new M2)** |
| M3 outcome numbers | Numbers **all correct** against the PDF; wording statement wrong (new M3b) |
| M4 label collisions | Mostly fixed (no label on a line or tick except by design with a halo); association remains on three items (new M1) |
| L-A card sentence | Fixed on S1-14, S1-19, S2-05, S2-09 |
| L-B instruction length | Fixed (at most 5 sentences) |
| L-C, L-D, L-E, L-G | Cube root bigger on S2-04 only; hatch 0.55 not yet copier-tested; box claim still wrong (L1); word-list note unchanged (L2) |
| L-F tank equals private tank | Fixed (dims changed) |
| L-H key text slips | Fixed (S1-08, 13, 15, 20); S2-04 retitled Root Maze |
| L-I SPONGE | Fixed (WIZARD) |
| L-J pi balance | 3.14 on S1-18 and S2-16 |
| L-K, L-L, L-M | K superseded by not-to-scale; L and M unchanged |
| Round 1 decision 1 (replace Primary 4 and 5 pages) | Nets, rate and mixed numbers replaced by three Primary 6 Standard pages; the four Foundation pages stay (section 4) |

## 11. What I could not check

- No real photocopier, no pupil trial, no teacher read-through (needed for the thin hatch, the cube-root index, M1 and "does a pupil see which arc the number belongs to").
- Lawyer approval of the licence wording.
- `validate.py` (742 checks) and `similarity_check.py` were not re-run; I did my own solves, dictionary tests, similarity passes and measurements on the committed PDFs and on `S2_pupil.html`. The HTML and the PDF agree on the three figures I measured by eye.
- Private sources are summaries and short records: I ran phrase and number-scenario passes only, not paraphrase similarity. I did not read the Drive originals.
- My dictionaries do not hold every word: a word outside web2, gcide and wordfreq would not be found; double slips and three-answer errors were tested only on the common list.
- The PDF does not say how many steps a linear equation takes or which of the Primary 6 Standard pupils' papers contain two-step equations.
