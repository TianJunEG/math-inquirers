# Independent audit: Primary 5 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent (not the builder). Branch `claude/great-fermi-1hv4vc`. Nothing pushed, no PR, nothing edited except this report.
Subject: `school/p5/out/P5_S1_*` and `P5_S2_*` (Puzzles 20 pp, FrontMatter 5 pp, Answer_Key 9 pp, Complete_Pack 25 pp). Read first: `p5_semester_booklets_build_report.md`, `p5_semester_booklets_plan.md`, `p5_outcome_wording.md`, `school/p5/README.md`, `docs/moe/syllabus_by_level.md`, `docs/school_books/plan.md` (reading-load table, section 11), `docs/terms/owner_decisions.md`, `validation_report.txt` (737 checks, 0 failed; not rerun), the P2 and P3 audits as models, and `docs/books/p5_school_paper_patterns.md`.

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **Content ready, minor edits.** All 20 pages solved by hand agree with the key; all code words are unique and no wrong placement, single slip or other choice spells a word. No Primary 6 leakage. Needs the similarity edits (M3) and the Low items. |
| Semester 2 | **Content ready after fixes.** All 20 pages agree with the key. Fix H1 (P5-39 has no stated question), M1 (P5-40 clipped labels), M2 (P5-29 instruction and labels), M3 (similarity), M4 (P5-25 multi-year interest). |

No wrong key, no page with two answers, no unsolvable page, no Primary 6 leakage. One High (an unstated question, not a wrong answer). Both booklets stay DRAFT by the owner's own rule (lawyer, real photocopier test, pupil trial, syllabus PDF are not done).

## 1. Hand-solve (all 40 pages) and code words

Method: every pupil page rendered at 100 dpi and viewed. Figure pages were also viewed at 220 to 600 dpi crops: P5-21 bars (segments counted by pixel runs: item 2 is 8 of 20, item 3 is 1 of 20, the segments are 3.5 mm), P5-29, 31, 32 (the three edges of each cuboid counted), 36 (all 16 cells), 37, 40. I solved with my own arithmetic from the printed page before reading the key text. Honest limit: pages S1-19, S1-20, S2-03 to S2-07 and S2-15 are text-only and were solved from the PDF text layer (identical to the printed text), not from a viewed image. **40 of 40 agree with the key; 0 wrong; 0 with two answers; 0 unsolvable.** Colour pages P5-05 and P5-22: every part solved; tallies (yellow 2 red 4 blue 3 green 3 orange 3; yellow 2 red 2 blue 2 green 4 orange 4) and every left/right pair agree.

Code words. Dictionary: `english_words` web2 and gcide (6-letter, 20 205 words), `wordfreq` top 100 000 (strict, 13 889 six-letter words) and top 500 000 (wide, 46 290; it contains names and junk). This is not the builder's 242 000-word list. Tests: all 719 rearrangements of each word; for the 16 table pages every single slip and every two-slip pair over the page's code-table letters; for the 8 choice pages every combination of the row letters; for the 7 ordering and matching pages all 719 orders. **No real word from any rearrangement or from any choice combination. No real word from any single slip.** Single-slip hits exist only in the wide list and are junk or names (FROBEN, FAMILI, ERIDGE, STUDII, BOTANA; STRONA from choices). All 31 words are different from each other. Two slips at once (information only, not claimed): FROZEN to BROKEN, PEANUT to PLANET, FAMILY to FAIRLY, FRIDGE to DREDGE or FRIEZE, FRUITS to TRUSTS, CAMPUS to CALLUS, CAUCUS, PAMPAS, BANDIT to BANDAI, DEVOUR to DEVORE, WIZARD to IZZARD. The notes say "one or two wrong answers very rarely do": fair.

**P5-07** (no code word): checked by substitution. I solved the six lines (10, 88, 21, 184, 7, 14); each has exactly one whole-number answer, and putting the number back tests the line completely, so this check is in fact stronger than a code word. Weakness is only for a pupil who does not substitute. Accept.
**P5-12** (two cancelling slips): the loop multiplies to 1, so a carried slip returns to 48 only if a second slip restores the right value, that is, the pupil writes the correct circle without multiplying from their own previous one. Very unlikely. Accept; the notes already say so.
**P5-10**: unique by linear algebra; all nine numbers distinct; total 21 3/4 matches all eight lines.

| Page | My answer from the page | Key | Notes |
|---|---|---|---|
| P5-01 | 5000 F; L; 9 060 005 I; 4 020 401 G; 1 552 683 H; 6 187 282 T: FLIGHT | agree | none |
| P5-02 | 2 056 789; 3 045 789 (smallest odd, 3 047 895 is bigger); 9 867 410; 9 865 310; 1 023 457; 9 765 430: FROZEN | agree | none |
| P5-03 | 9, 25, 38, 260, 99 860, 677 200: BACKUP | agree | none |
| P5-04 | route (2,1) (1,1) (1,2) (1,3) (2,3) (3,3) (4,3) (4,4), 8 boxes; dead ends (1,4), (4,2) | agree, unique | none |
| P5-05 | 36 36 30 30 18 18 18 36 18 12 12 24 24 24 30 | agree | tally and mirror pairs hold |
| P5-06 | 24 C, 27 R, 29 A, 56 F, 70 T, 290 S: CRAFTS | agree | none |
| P5-07 | 10, 88, 21, 184, 7, 14 | agree | no code word, see above |
| P5-08 | 1/4, 1/5, 2 3/4, 1 5/6, 7/8, 1 4/5: DEVOUR | agree | L: juice frame, M3 |
| P5-09 | 0.14 B, 0.15 E, 0.625 H, 0.875 I, 1.2 N, 2.35 D: BEHIND | agree | none |
| P5-10 | 2 1/4, 9 3/4, 3 1/2, 12 1/4, 6 | agree | none |
| P5-11 | route (2,4) (1,4) (1,3) (1,2) (1,1) (2,1) (3,1) (4,1); dead ends (3,4), (3,2) | agree, unique | none |
| P5-12 | 40, 70, 77, 35, 56; back to 48 | agree | cancelling slips: see above |
| P5-13 | 28, 30, 14, 63, 25, 12: PEANUT | agree | L: "film lasts 18 minutes" |
| P5-14 | 1/10, 5/27, 8/21, 63/100, 5/7, 1 1/32: MELODY | agree | none |
| P5-15 | 2 1/12 C, 14 1/4 R, 9 1/6 E, 1 2/7 A, 6 2/5 M, 1 13/15 Y: CREAMY | agree | none |
| P5-16 | 4, 9, 18, 19, 8, 3: FAMILY | agree | M3 frames |
| P5-17 | 0.37, 5510, 56, 0.9, 0.06, 0.688: POLICE | agree | none |
| P5-18 | F, T, T, T, F, T: FIGURE | agree | L: row 1 letter F and label F |
| P5-19 | 7.944, 3.26, 8.615, 70, 86, 11: HUNGRY | agree | none |
| P5-20 | 2750, 333, 4980, 3206, 2034, 30: FRUITS | agree | none |
| P5-21 | 10, 40, 5, 30, 75, 98: FRIDGE | agree | bars 20 parts: legible, see section 4 |
| P5-22 | 40 20 25 40 / 20 40 40 25 / 12 60 60 / 12 60 60 | agree | L: topic line names GST, no GST part |
| P5-23 | $15, 22.50, 25.50, 60, 200, 225: THIRDS | agree | none |
| P5-24 | $49.05 W, 59.95 A, 65.40 L, 168.95 R, 174.40 U, 179.85 S: WALRUS | agree | M3 sentence |
| P5-25 | $150, 54, 1260, 8, 50, 530: STUDIO | agree | M4 (multi-year) |
| P5-26 | 5, 9.60, 6, 12, 48, 3: STRONG | agree | M3 |
| P5-27 | 30, 45, 54, 72, 24, 70: WISDOM | agree | M3 |
| P5-28 | HF, KG, NU, JT, SQ (perpendicular, about 94 degrees in the drawing), PG: COUSIN | agree | L: item 5 relies on the drawing |
| P5-29 | 20, 18, 21, 55, 72, 30: SHRIMP | agree | M2 |
| P5-30 | route (4,3) (4,4) (3,4) (2,4) (1,4) (1,3) (1,2) (1,1); dead ends (4,2), (2,2) | agree, unique | labels cut sides (L) |
| P5-31 | 48, 20 (notch 8 x 4 / 2 = 16 from 32... see note), 36, 32, 68, 27: TEACUP | agree | item 2 is 8 x 4 minus a notch of base 8 and height 3: 32 - 12 = 20 |
| P5-32 | 16, 9, 8, 6, 4, 2: BANDIT (edges counted at 220 dpi) | agree | none |
| P5-33 | 240, 45, 144, 175, 343, 147: CURFEW | agree | labels 8.5 pt |
| P5-34 | F 12, A 15, T 19.2, H 20, O 22.5, M 48: FATHOM | agree | none |
| P5-35 | 24, 62, 54, 69, 672, 8: CAMPUS | agree | M3 frame |
| P5-36 | route (4,1) (4,2) (4,3) (4,4) (3,4) (2,4) (2,3) (1,3), every ? = 70; dead ends (3,1), (2,2); the other cells give 95, 55, 80, 55, 90, 55 | agree, unique | dense, see section 4 |
| P5-37 | 60, 70, 115, 40, 50, 145 (item 6 vertically opposite): KNIGHT | agree | labels 10 pt |
| P5-38 | 78, 60, 61, 98, 101, 30: WIZARD | agree | labels 7.8 pt, M1 |
| P5-39 | F, N, T, T, F, T: CANOPY (on the reading "is the last angle consistent with the rest") | agree | **H1** |
| P5-40 | 114, 56, 73, 109, 147, 136: BOTANY | agree | **M1** labels clipped |

(Note on the P5-31 row: the answer is 20, as the key says. Item 2 is rectangle 8 x 4 = 32 minus a notch of base 8 and height 3 = 12.)

## 2. Leakage and coverage

Leakage: a word scan of all 40 pupil pages and both keys for ratio, average, mean, speed, prime, negative, algebra, "for every", radius, circle (as a shape), pie, median, mode, compound, probability, coordinates, symmetry: none (the only "circle" hits are the instruction "circle the letter" and "in its circle"). Numbers: whole numbers to 9 867 419; fractions with denominators to 12 (to 50 for decimal conversion); decimals to 3 places; no fraction division, no whole from a percentage, no percentage change as a topic (P5-22's "40 + 50% of 40" is the price-after-percentage-added type that the plan allows under GST), no missing dimension, no water level from volume, no letter unknowns. P5-40 uses the exterior angle through two steps (straight line plus angle sum), which the page labels "two steps": acceptable, no theorem is needed.

**Average, pie charts, ratio: is the exclusion right? Verified against the syllabus PDF** (coordinator addendum: 2021 Primary Mathematics Syllabus, updated Oct 2025, read as data; Primary 5 pp. 41-42, Primary 4 p. 40, Primary 6 p. 43-44). **Yes, the exclusion is right.** The Primary 5 pages have no Statistics strand. "Tables, Line Graphs and Pie Charts" (1.1 completing a table, 1.2 reading tables, line graphs and pie charts) is on the Primary 4 page; "Average of a Set of Data" (1.1, 1.2) and the whole Ratio sub-strand (1.1 to 1.7) are on the Primary 6 pages. This also agrees with the 2025 school papers in `p5_school_paper_patterns.md`.

**Outcome wording against the PDF (`p5_outcome_wording.md`): the 32 lines match in substance; differences, all small:** (a) the PDF numbers every line and the file prints numbers only for some: Whole Numbers 1.1 (read and write in numerals and in words) and 2.1 (multiply and divide by 10, 100, 1000 and multiples) are unnumbered in the file; Percentage 1.1 to 1.3, Rate 1.1 and 1.2, Area of Triangle 1.1 to 1.3, Volume 2.2 (cubic units, "excluding conversion between cm3 and m3"), Triangle 2.1 to 2.3 and Parallelogram 3.1, 3.2 are unnumbered; the numbers can now be printed from the PDF. (b) PDF Volume 2.1 is "building solids with unit cubes" (file: "building cubes and cuboids"). (c) PDF Geometry 2.3 and 3.2 add "finding unknown angles without additional construction of lines", which the file folds into the angle-sum and quadrilateral lines. (d) Whole Numbers 1.1 does not say "up to 10 million" in the line itself (the heading "Numbers up to 10 million" does). None changes a page. The file's header ("PDF not in the repository") is now out of date.

Coverage against the 32 outcome lines: every line has at least one page (checked page by page against the plan table). Thin lines, as the builder says: Fractions 2.4 (P5-15 rows 1 and 6 only), 2.5 (P5-15 rows 2 and 5), Fractions 1.1 and 1.2 (one page each), Area composite (one page, P5-31), Volume cubic units (P5-33), Parallelogram, rhombus, trapezium (P5-39, which has the H1 problem). The "not covered" paragraph (drawing on isometric grid, building with cubes, handwriting number words) is honest.

**Simple interest on P5-25.** The syllabus line (PDF, Percentage 1.4) is "finding discount, GST and annual interest" and does not say simple, compound or how many years; the 2025 school papers in the repository use one-year questions ("at the end of each year", "after 1 year", "for one year"). The page says plainly that the interest is the same each year and is a percentage of the money first saved, so no compound idea leaks. But 3 of the 6 items (1500 for 2 years, 600 for 3 years, 500 for 3 years with "money in the bank") go beyond what the papers show and shade towards "interest for several years". It is not secondary content, but it is the one place a Primary 5 pupil is asked to multiply an annual amount by years. Recommendation (M4): make all six items one year, or at most two years with the sentence kept; replace the 3-year items.

## 3. Reading load

plan.md section 11 table gives **16 words a sentence, 4 instruction sentences for Primary 5** (plan.md line 248 says 24 for P5 to P6 check wording; the table and the build report use 16, which I accept). Judgement: 16 is right for 10 and 11 year olds; the pages are in fact mostly at or under 12. Longest sentences I found: P5-05 and P5-22 strip "Parts in the same place on the left and on the right have the same colour." 16; P5-08 "Divide. Give a fraction, or a mixed number if the answer is more than 1." 15; P5-25 "The interest is the same each year: the percentage of the money first saved." 14; P5-16 item 3 15; P5-10 "Every row, every column and both long diagonals make the same total." 12. Instruction sentences per page: at most 4 (P5-08, P5-25). No change needed. The validator's 16-word and 4-sentence checks pass.

## 4. 1-bit photocopy legibility (every page, at zoom)

Method: all 40 pages at 200 dpi grey, two proxies (a light copier: blur and threshold 100 that loses strokes under about 0.3 mm; a dark copier: threshold 175 that thickens), crops of every figure page viewed in both; vector stroke widths read from the PDF; label font sizes read from the PDF; 1-bit 150 dpi renders of a key page and a front-matter page viewed. Pupil pages are pure black and white (0 non-black-and-white drawing operations; no flat grey on any page). Builder's 1-bit loss on pupil pages 12.83% and 13.58% (limit 25%).

- Stroke widths: card frames and some rules 0.26 mm; figure lines 0.38 to 0.49 mm on P5-21 (bar gaps 0.5 mm, white gaps in shaded runs 0.85 mm), P5-29, 31, 32, 33 (0.39 to 0.49), 36, 37 (0.45), 38 (0.42), 40 (0.38 to 0.42), P5-10 and P5-30 grid lines 0.49. Many figure strokes are under 0.5 mm. They survived both proxies for P5-32 cubes, P5-36 and P5-37 angles and P5-21 bars (all counted correctly in the light proxy).
- P5-21 20-part bars: 3.5 mm segments, 0.5 mm separators, shaded runs separated by 0.85 mm white: countable in both proxies. In the dark proxy the shaded 8 of item 2 can merge, but the 12 white segments still count. Adequate; include in the real copier test.
- P5-32: cubes legible in both proxies, edges 0.42 mm; item 1 and 3 (the interior lines) are the weakest, still clear.
- P5-36: 16 cells at about 41 mm; labels 10 pt; in the dark proxy "134°" and "113°" nearly close up. The label 117° touches the FINISH tag. Legible; Low.
- P5-37: labels 10.2 pt, clear.
- **P5-38 and P5-40: labels 7.8 to 8.3 pt and "?" 7.8 pt (P5-38) or 9 pt (P5-40)**; in the light proxy the degree signs disappear and "114°" nearly joins. The builder's "figures are small" worry is correct here; the others (P5-29 9 pt, P5-31 8.9 pt, P5-33 8.5 pt) are borderline.
- **P5-40 items 1 and 5: the apex labels "48°" and "114°" are clipped at the top** (confirmed at 600 dpi: the upper part of the glyphs is cut, the card frame touches them). M1.
- Figure widths: P5-31 figures are 22 to 25 mm wide, P5-33 cuboids about 28 mm, P5-29 triangles about 30 to 35 mm, P5-38 about 40 mm. The builder's 49 mm is the card width, not the figure.
- Answer boxes: value boxes 16 to 22 mm by 12.5 mm or more on the pages I measured; colour-page boxes 9 mm (P5-05, P5-22; the audited P2 rule); check-strip letter boxes about 10.5 mm (the 12 mm rule is for value boxes; Low). P5-10 fraction boxes 11 to 12 mm.
- **Front-matter ink-loss limit 32% to 35%:** measured 32.27 and 32.25 (front matter), 33.57 and 34.74 (keys). The metric compares small bold-and-regular text against a grey render, so 11 pt prose scores high without being unreadable. I viewed the 1-bit key page (KEY 7) at 150 dpi: fully legible. Accept 35% for the teacher-only front matter and keys; do not raise it for pupil pages (limit 25%, actual 13%). The key at 34.74% has only 0.26 points of headroom: next change may trip it; fix by raising the key body size by 0.5 pt rather than the limit.

## 5. Similarity

Private sources (`docs/books/private_*`, `docs/sasmo/private_*`, 72 files in all groups, 681 000 words) compared by 4, 5 and 6 word shingles against every pupil sentence: **no 7-word run and no scenario copied.** Hits are generic (instructions, "How much money did she spend in all?", "8 cm by 12 cm" in a different question). Annual interest appears in P6 private records as "interest at the end of one year", all with one year.

Holiday Level 5 (`p5/content/*.js`) and extension Level 5 (`extension/data/l5_*.json`), owner policy: school booklets must not duplicate extension items. Near-duplicates (frames, not numbers):
- **P5-08 item 5** "7 litres of juice are poured equally into 8 jugs. How much juice is in each jug?": holiday L2 "4 litres of juice are poured equally into 6 bottles. How much juice is in each bottle?" (same sentence frame), extension u02 "5 litres of juice fill 6 equal bottles".
- **P5-16** fraction-of-the-remainder stories: extension u02 example "Mei uses 1/3 of [a 180 cm ribbon]... then 1/4 of the ribbon left" and L5U02-L01 "Mei has 120 beads. She uses 1/4 ... then 2/3 of the rest"; P5-16 item 5 is "Mei ... 1/5 of them ... 2/3 of the rest" and item 6 is a ribbon. Holiday L3 "Siti had $60. She spent 1/4 of it on a book and 1/3 of the remainder" against P5-16 item 4 "Hana had $25. She spent 2/5 of it on a book and 3/5 of the rest on a pen" (item 3 reuses Siti).
- **P5-26 and P5-27** rate: extension u06 "A tap fills 18 litres in 3 minutes", "6 pens cost $4.20", "A machine fills 24 bottles in 4 minutes"; P5-26 and 27 use "A tap fills 20 ℓ in 4 minutes", "A pen costs $1.20", "A machine makes 18 bolts in 2 hours". The P5-27 instruction "Find the amount for 1 unit, then answer the question." is the extension u03 line "Find 1 unit. Then answer the question." and u06 "a rate for 1 unit".
- **P5-24** "GST is 9% of the price before GST" is extension u07-S05 "GST is 9% of the cost before GST" and holiday L7.
- **P5-21 item 5** "15 out of 20 pupils walk to school" against extension u07 "7 out of 20 pupils cycle".
- **P5-35 items 1 and 3** tank sentences against holiday L5 "A glass tank is 50 cm long, 30 cm wide and 40 cm high. The water in it is 18 cm deep" (generic but the same sentence skeleton).
Numbers always differ. This is M3: reword these items (different objects and sentence shapes) so the two editions are not recognisably the same.

## 6. Front matter, keys, teacher notes

Annual licence: yes ("This is an annual licence: it covers one school year and is renewable"). Publisher line and registered office: yes. Contact email with "business email for now": cover, licence, notes, keys. DRAFT stamps on cover, licence, notes and keys; none on pupil pages. "Not affiliated with or endorsed by the Ministry of Education, Singapore." once, on the cover only; licence page has the permitted factual syllabus sentence; no SASMO, "align", "approved by MOE", price or Mi anywhere in the 6 PDFs. "Pictures are not actual size." in the notes. Page counts 20, 5, 9, 25; ten one-star and ten two-star pages in each booklet (counted). Footers carry both numbers. No coins or notes at P5 (the money pages are prices as text), so no real-proportion check applies.
Low items: the teacher notes say the excluded topics are "Primary 6 or Primary 4 content in the syllabus summary": "syllabus summary" is an internal document and the sentence is a claim about the Ministry syllabus; reword to "not used in these booklets". The front-matter note says figures are not drawn to scale unless a page says so; the key note on P5-38 says "Figures are drawn to scale in these pages"; P5-28 item 5 depends on the drawing and no page says so; make the notes consistent. Key P5-27 prints "30ℓ", "45min", "72bolts" without spaces.

## 7. Findings

### High
**H1. P5-39 (S2-19) Shape Statements: the page never says which statement is judged.** The rows give a shape, a parallel pair and two angles; the legend says "T = true. F = false. N = not possible to tell." but there is no claim to call true or false. The key's reading (is the last angle consistent with the others, given the shape's properties) is the only one that gives one answer (F, N, T, T, F, T), and a pupil cannot know it. Fix: end each row with a sentence such as "∠K = 79°. Is this true?" or instruct "Use the first angle. Is the second angle as given true, false or not possible to tell?". A pupil also has to know that K and N are on the same leg of KLMN, which a figure would settle; the plan says no drawing is used, so at least name the legs in words ("∠K and ∠N are on the same side").

### Medium
**M1. P5-40 (S2-20) clipped and small labels.** Items 1 ("48°") and 5 ("114°"): the top of the label is cut by the card frame. All labels are 8.1 to 8.3 pt and the "?" 9 pt; on P5-38 labels are 7.8 pt including the "?". Enlarge labels to at least 10 pt (as P5-37) and move the apex labels inside the card. Add P5-38 and P5-40 to the real photocopier test.
**M2. P5-29 (S2-09) instruction and labels.** "The height is the dashed line" is false for items 2, 3, 4 and 5, where the height is a solid side with a right-angle mark and a length. Reword ("The height is the length at a right angle to the base"). Item 1 (obtuse): the "5 cm" label sits on the slanted side, with a white halo through it, and touches the dashed height, so it can be read as the length of the slanted side. Item 4: the "11 cm" halo breaks the hypotenuse. Same halo gaps in the sides on P5-30 (row 1 column 2) and P5-31 (item 4, right notch line).
**M3. Similarity with extension and holiday Level 5.** P5-08 item 5, P5-16 (items 1 to 6 as frames), P5-21 item 5, P5-24 statement, P5-26 and P5-27 rate frames and instruction, P5-35 items 1 and 3: see section 5. Rewrite scenarios and sentence shapes; keep numbers and tasks.
**M4. P5-25 multi-year interest.** Items 1, 2 and 6 ask for 2 and 3 years; the papers in the repository use one year. Make all six one-year (or two at most), and keep the explicit "same each year" sentence.
**M5. Small figures on P5-31, 33 (labels 8.5 to 8.9 pt, figures 22 to 28 mm) and P5-29 (9 pt).** Legible in both proxies; a pupil trial should test them with P5-36, 37, 38, 40 and the P5-21 bars, as the builder says. If space allows enlarge by 20 percent.

### Low
- L1. 28 of the 31 code words already appear in the keys of at least one other level (for example PEANUT, TEACUP, BANDIT, FATHOM, CAMPUS, COUSIN, SHRIMP, FAMILY, FIGURE; only CRAFTS, MELODY, THIRDS and KNIGHT are new). Not an error; a school buying several levels will see them again.
- L2. P5-22 topic line says "discount and GST", no part uses GST.
- L3. P5-18 row 1: the letter for false is F next to the label F.
- L4. P5-28 item 5 depends on the drawing (SQ is about 94 degrees to FE, no right-angle mark); the notes say figures are not to scale.
- L5. P5-36: the 117° label touches the FINISH tag; dense figures (labels 10 pt) lose spacing in the dark proxy.
- L6. P5-07: 4 cm of blank band above and below the six lines; P5-12, 16 similar.
- L7. Check-strip letter boxes 10.5 mm; colour-page value boxes 9 mm (P2 precedent).
- L8. P5-13 item 6 "A film lasts 18 minutes" is odd; P5-10 check strip writes "21 3/4" on a line while the page stacks it.
- L9. Teacher-note wording about "syllabus summary" and the scale inconsistency (section 6).
- L10. The key's P5-27 answer spacing.
- L11. Key ink-loss headroom 0.26 points (section 4).

## 8. The builder's decisions: recommendations

1. **Outcome lines in our own words:** accept; add the PDF numbers now that it is available (section 2), still make no alignment claim.
2. **Exclude average, pie charts and ratio:** right for all three (confirmed on the PDF: pie charts Primary 4, average and ratio Primary 6). No preview page in the school booklets (they would break "no next-level content"); a labelled preview stays in the extension book if wanted.
3. **Semester 1 fractions and decimals, Semester 2 geometry and percentage:** accept; the notes say to use any page when its topic is taught.
4. **Simple interest only:** accept simple, restrict to one year (M4).
5. **GST 9%:** correct for current papers; the page states it. Accept.
6. **Front-matter ink-loss limit 35%:** accept for teacher-only pages, not for pupil pages; keep pupil limit 25%.
7. **Colour-by-code with a vendored Primary 5 bank:** accept for now; merge `banks_p5.py` and the percentage rules into `school/colour_by_code` before another level copies the library (as the P3 audit said).
8. **P5-07 without a code word:** accept; substitution is a complete check.
9. **P5-39 three-way form:** keep the form, fix the wording (H1).
10. **P5-12 cancelling slips and P5-10 shortcut:** accept; both are documented.
11. **Answer boxes 9 mm on the colour pages:** accept (P2 precedent); the rest are 12 mm or more.

## 9. What I could not check

- No real photocopier; light and dark are software proxies at 200 dpi. A real light-copier test of P5-21, 29, 31, 33, 36, 37, 38, 40 is still needed.
- The syllabus PDF was supplied late and read only for pp. 37 to 44 (Primary 4 to 6) as data; the "annual interest" line gives no number of years, so M4 is a judgement from the school papers, not a syllabus rule.
- My word list is not the builder's 242 000-word list (web2, gcide, wordfreq top 500 000). Two-slip coincidences were listed for information only; three-slip and other multi-error cases were not enumerated. Pupil-written wrong values that map to no letter were not tested.
- Similarity is lexical (shingle and keyword); a reworded scenario with the same idea would not be found. Private sources are catalogues and summaries, not full papers.
- Pages S1-19, S1-20, S2-03 to S2-07, S2-15 were solved from the text layer, not from a viewed image.
- I did not rerun the 2.5-minute validation; I read `validation_report.txt` (737 checks, 0 failed) and re-derived the keys independently.
- No pupil trial; no lawyer review of the licence.
