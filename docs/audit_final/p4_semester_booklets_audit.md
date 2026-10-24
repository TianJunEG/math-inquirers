# Independent audit: Primary 4 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent (not the builder). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`. Nothing pushed, no PR, nothing edited except this report.
Subject: `school/p4/out/P4_S1_*` and `P4_S2_*` (Puzzles 20 pp, FrontMatter 5 pp, Answer_Key 10 / 9 pp, Complete_Pack 25 pp), `verification.json`, `validation_report.txt`.
Read first: `p4_semester_booklets_build_report.md`, `p4_semester_booklets_plan.md`, `school/p4/README.md`, `p4_outcome_wording.md`, `docs/school_books/plan.md` (reading table: P4 = 14 words a sentence, 4 instruction sentences), `docs/terms/owner_decisions.md`, the P2, P3 and P6 audits. The MOE syllabus PDF (owner upload) was read as data: Primary 4 (printed pp. 37 to 40) and Primary 5 (printed pp. 41 to 42).

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 (P4-01 to P4-20) | **Content correct, needs medium edits.** All 20 pages solved by hand agree with the key; every code word is unique; no Primary 5 content. Fix M2 (P4-08, P4-20 sentence length), M3 (P4-19 arm over the numbers), M4 (P4-05, P4-11 box size), M5 and M6 (key and teacher-note text), M7 (FM2.5). |
| Semester 2 (P4-21 to P4-40) | **Content correct, needs medium edits.** All 20 pages agree with the key; P4-37 "row by row" is now right (FLIGHT). Fix M1 (P4-37 and P4-38 echo our extension unit L4U09), M2 (P4-30, P4-38), M4 (P4-40), M5, M6 (S2-13 teacher note), M7 (RS2.2 claim). |

No High. No wrong key, no page with two answers, no unsolvable page, no code word that is another word by rearrangement or single slip. Both booklets stay DRAFT by the owner's own rule (lawyer, real copier, pupil trial).

## 1. Hand-solve of all 40 pages and code words

Method: every pupil page rendered at 90 dpi and viewed, then 200 to 400 dpi crops for the drawn pages (bars, angles, protractors, number lines, figures, dot grids, symmetry grids, solids, nets). I solved every page from the image before opening the key text. For P4-19 I also read the arm and base end points from the SVG in `out/S1_pupil.html` (the image agrees: items 2, 3, 4 read right from the image; items 1, 5, 6 read left). Arithmetic was also re-run in a script (all products, quotients, gcds, riddle uniqueness over 1 to 999, both mazes by exhaustive search, fractions, decimals, perimeters and areas). **40 of 40 agree with the key; 0 wrong, 0 with two answers.** Colour pages P4-05, 11, 40: counts and twin marks all agree with the printed strip and with the key's page images.

**P4-37 "row by row" is right now.** Missing cells in reading order: 4A Chess 11, 4B Drama 13, 4B Total 30, 4C Chess 7, 4C Art 12, Total Drama 36 = F L I G H T. The key lists 11, 13, 30, 7, 12, 36 in that order. The grand total 93 is not circular (rows and columns are the check).

Code words. Dictionaries I built (not the builder's): `english_words` web2 (17 468 six-letter words) and gcide (11 120), `wordfreq` top 100 000 (13 808) and top 500 000 (45 651), plus the builder's own list (40 333 six-letter). "Strict" = on wordfreq top 100 000 and on web2 or gcide (5 829 words, the words a child could meet). For each of the 33 pages with a word (31 code-word or choice pages plus the two ordering and matching pages P4-22 and P4-29 counted among them): all 719 rearrangements, every single slip (one answer replaced by any letter on that page's code table or card set), every two-slip pair on the code-table pages, every other way of choosing on the 9 lettered-choice pages (up to 4 096 combinations, P4-24), all 720 orders on P4-22 and P4-29. Results:
- **Rearrangements and single slips: no hit in the strict or the mid list on any page.** In the widest list only names or typos appear (CREAMY: MARCEY, CREARY; WALRUS: WALRAS; STUDIO: STUDII; FAMILY: FAMILI; FRIDGE: ERIDGE; DONKEY: CONKEY, ZONKEY (a real but rare hybrid word; Z is the fraction-card decoy for row 1 and a decimal card is asked, so it is not a natural slip)).
- Two wrong answers at once (information only; the teacher notes say "very rarely" and "Two wrong answers at once were not all tested", which is fair): CREAMY to CREEPY, WALRUS to GALLUS, CAMPUS to CALLUS or CAUCUS, POLICE to ELLICE, FRIDGE to DRUDGE or GRUDGE or DREDGE, CANOPY to CANARY, FATHOM to HATHOR, FAMILY to FAIRLY or LAZILY, BANDIT to BANGIN or DANGIT, HUNGRY to PUGGRY, PEANUT to PENNET, FRUITY to FRUTTI.
- All 33 intended words are on the strict list (real, child-safe words). No word repeats within the booklets.

| Page | My answer from the image | Key | Issue refs |
|---|---|---|---|
| P4-01 | 43 602 H, 3000 U, 80 N, 31 510 G, 60 000 R, 30 466 Y: HUNGRY | agree | none |
| P4-02 | B 52 660, A 42 079, C 41 063, K 12 907, U 67 850, P 20 080: BACKUP | agree | none |
| P4-03 | 25 300, 43 500, 4800, 12 500, 9800, 10 000: CREAMY | agree | none |
| P4-04 | route (1,1),(1,2),(2,2),(3,2),(3,3),(3,4),(3,5),(4,5),(5,5),(5,4),(5,3), 11 boxes, three dead ends, unique | agree | L16 (two exact half cases) |
| P4-05 | Y 4, R 3, B 3, G 3, O 3; marks agree | agree | M4 |
| P4-06 | Yes, No, Yes, Yes, Yes, No: TEACUP | agree | L (two-option rows) |
| P4-07 | route (1,4),(2,4),(2,3),(2,2),(2,1),(3,1),(4,1),(4,2), 8 boxes, unique | agree | L9 (1 star but 4-digit tests of 7) |
| P4-08 | 11, 4, 12, 15, 8, 7: FROZEN | agree | M2 (item 6 has 15 words) |
| P4-09 | 15, 81, 46, 27, 49, 119: PEANUT | agree | M7, L8 |
| P4-10 | 26 145, 14 319, 18 234, 20 727, 11 753, 13 580: FRUITY | agree | L6 |
| P4-11 | Y 3, R 4, B 3, G 2, O 3; marks agree | agree | M4 |
| P4-12 | 2086, 685, 1, 314, 354, 824: SHRIMP | agree | L6 |
| P4-13 | 1432, 716, 4296, 1074, 358, back to 179 | agree | M6 (teacher note) |
| P4-14 | 9/5, whole number 1 (1 5/8), 4, 44, 6, 20: FIGURE | agree | L7 |
| P4-15 | 1 1/2, 2 3/4, 2 1/2, 7/8, 3 3/4, 2 3/4: FABRIC | agree | M6 (teacher note) |
| P4-16 | 6, 8, 15, 18, 12, 28: WALRUS | agree | none |
| P4-17 | 7/10, 1/5, 13/10, 1/10, 1/2, 8/9: BANDIT | agree | none |
| P4-18 | LXS, SZX, XRQ, QLR, XQL, PNS: CURFEW (arcs read at 220 dpi) | agree | L2 |
| P4-19 | 55 (base left), 45, 70, 115, 95 (left), 130 (left): CAMPUS | agree | **M3** |
| P4-20 | 18, 10, 150, 20, 32, 12: POLICE | agree | M2 (item 5 has 17 words), L10 |
| P4-21 | 9.748, 4, 0.003, 55, 0.201, 74: STUDIO | agree | none |
| P4-22 | Set A W I Z (0.22, 0.582, 0.8); Set B A R D (4.9, 4.89, 4.797): WIZARD | agree | L9 |
| P4-23 | D, O, N, K, E, Y: DONKEY | agree | none |
| P4-24 | 4.95, 9.87, 2.9, 4.9, 8, 9: COBALT | agree | none |
| P4-25 | 3.08, 2.33, 3.33, 2.58, 1.58 (all eight lines 6.99) | agree | none |
| P4-26 | 27.04, 6.53, 3.625, 2.56, 11.2, 1.9: FAMILY | agree | L10 |
| P4-27 | 5, 16, 13, 12, 7, 6: FRIDGE | agree | L1 |
| P4-28 | area 74, perimeter 42, area 64, perimeter 48, perimeter 34, area 55: WALNUT | agree | L1 |
| P4-29 | C38 R44 A66 F40 T42 Y72: CRAFTY (T 42/30, F 51/40, C 48/38, Y 72/46, A 66/36, R 67/44, all twelve distinct) | agree | L1 |
| P4-30 | 192, 68, 24, 128, 32, 48: CANOPY | agree | M2 (item 5 has 18 words), L10 |
| P4-31 | F, T, F, F, F, T: BOTANY | agree | none |
| P4-32 | T, U, R, K, E, Y: TURKEY | agree | L3 |
| P4-33 | Yes, No, Yes, No, Yes, Yes: WOMBAT | agree | M6 (teacher note) |
| P4-34 | 28, 4, 5, 40, 2, 3: FATHOM (fig 1 shades 14 on the left; fig 2 shades 20 on top) | agree | L4 |
| P4-35 | square pyramid, cylinder, cube, cone, cuboid, triangular prism: DEVOUR | agree | L11 |
| P4-36 | pyramid, prism, no solid (2x2 block), cuboid, cube, cube: BOUNTY (both cube nets folded by hand) | agree | L4 |
| P4-37 | 11, 13, 30, 7, 12, 36: FLIGHT | agree | **M1** |
| P4-38 | 25, 35, 10, 15, 65, 30: COUSIN | agree | **M1**, M2 (item 6 has 16 words) |
| P4-39 | 80, 120, 40, 200, 240, 160: SHADOW (slices 3, 2, 1, 2; 40 pupils a slice) | agree | none |
| P4-40 | Y 4, R 2, B 2, G 2, O 2; marks agree | agree | M4 |

## 2. Coverage, the two gaps, leakage

**Outcome wording.** I parsed the 42 outcome lines of the Primary 4 pages of the PDF and compared them, line by line and word by word, with `p4_outcome_wording.md`: 42 of 42 match (ids in order, wording identical except for the joining of bullets). Nothing beyond outcome-line wording is quoted in the key or front matter.

**Coverage against the pages (my own reading of each page, not the plan).** 40 of 42 lines have a page, as claimed. The two gaps are honest and are listed in the front matter: AN1.3 (drawing an angle) and NT4.2 (drawing solids). Points where the claim is stronger than the page:
- **FM2.5 (common multiples of two 1-digit numbers) is practised only with the pair 3 and 9, twice (P4-09 items 2 and 4).** Because 9 is a multiple of 3, a common multiple is just a multiple of 9. A pupil never meets a pair like 4 and 6 (M7).
- **RS2.2 (drawing rectangles and squares)**: P4-32 asks the pupil to pick a lettered point, not to draw. The build report says "partly"; the contents list in both front matters prints "Rectangle and Square 2.2 drawing rectangles and squares S2-12" with no qualifier (M7). LS3.3 (shade the mirror half) is fair: the pupil is told to shade and the counts test it.
- NU1.3 (comparing and ordering whole numbers) is three "greatest of / smallest of" parts on one colour page (P4-05). Honest in the plan ("thin"); Low.
- DM3.3 one question (P4-26 item 6); FA3.1 only sums of two fractions, as the outcome says.
- AN1.2 covers reading a drawn protractor only; the plan and teacher notes say so.

**Primary 5 leakage (pp. 41 and 42): none found.** Searched pupil text and checked the maths of every page against P5: no percentage, rate, ratio, average, order of operations or brackets, no multiplying or dividing by 10/100/1000 of decimals, no fraction division or fraction by fraction, no mixed-number addition, no general fraction-to-decimal conversion (all denominators are factors of 100: 5, 20, 25, 50, 100), no unit conversion, no triangle area or properties of triangles or parallelograms, no volume, no angles on a straight line or at a point, no 7-digit numbers. Fractions: unlike denominators at most two (P4-17, P4-20 item 5: 3/8 and 1/4). Decimals to 3 places, operations to 2. Division with remainder and decimal quotients (29 / 8 = 3.625) are within DM3.2. The T and trapezium figures on P4-33 are used only for symmetry; the words trapezium, isosceles and triangle properties are not printed on a pupil page.

## 3. Reading load (plan.md table, Primary 4: 14 words a sentence, at most 4 instruction sentences)

Instructions: three sentences each, all within the limit. **Four story or question sentences are over 14 words** (numbers and fractions each counted as one word; I parsed the pupil HTML, splitting at . ? !):
- P4-08 item 6: "A common factor of 28 and 98 is greater than 2 and less than 14." (15)
- P4-20 item 5: "Aisha spent 3/8 of her savings on a toy and 1/4 of her savings on a card." (17)
- P4-30 item 5: "Two identical rectangles, 10 cm by 3 cm, are joined along their long sides to make one rectangle." (18)
- P4-38 item 6: "How many more books were borrowed on the busiest day than on the quietest day?" (16)
The build report says the two long-story pages are "12 to 14 words"; they are not, and the validator (`validate.py` V8) misses them because it splits only at "." and reads only a few element classes, so question sentences ending in "?" and the P4-08, P4-38 cards are never measured. The "check_lines" limit is also looser than the plan's (16 to 20). The builder's own reading list (13-word sentences on P4-20 items 1 and 3) is fine. M2.

## 4. Photocopy (1-bit) legibility

Method. Every page rendered at 300 dpi grey, reduced by area averaging to 100 dpi and 150 dpi, thresholded at 50% to 1-bit (harsher than a 600 dpi copier). All 40 pupil pages were viewed at 100 dpi 1-bit (two per sheet, P4-19, 32, 34, 36, 38, 39 singly) and 8 of the drawn pages again at 150 dpi or 250 to 400 dpi crops (P4-14, 15, 18, 19, 28, 29, 32, 36). Vector check with PyMuPDF on all 40 PDF pages: only black (0,0,0) and white; no images; no grey fill or stroke; no non-black text colour; no flat grey. DRAFT appears on front matter and keys only, never on a pupil page.

Thin lines (under 0.5 mm, measured from the PDF, all above the owner's 0.5 pt floor):

| Where | Width | 1-bit result |
|---|---|---|
| card borders, rules, boxes, every page | 0.24 to 0.26 mm | survive at 100 dpi |
| P4-19 protractor minor ticks (222 strokes), inner arc | 0.35 mm | survive, but see M3 |
| P4-34 grid (160 strokes) | 0.35 mm | survive; some rows look heavier at 100 dpi (builder weak point 4) |
| P4-32 dot-grid outlines and P4-18 angle figures | 0.39 to 0.41 mm | survive; dots 1.1 mm light but present |
| P4-04, 05, 11, 40, 14, 13, 36, 15 inner lines | 0.40 to 0.45 mm | survive |
| P4-38 and P4-39 dashed lines (half-lines, slice lines) | about 0.35 mm | survive at 100 dpi, faint; the notes already say use normal toner |

Flat grey: none (pure black and white); the validation report's own check agrees. Footer text is 8 pt and breaks up at 100 dpi 1-bit (not at 150); it is the licence line, Low. Check-strip letter boxes measure 10.3 to 10.6 mm wide by 11.6 mm high, under the 12 mm rule (answer boxes 26 to 34 mm by 12 to 13.5 mm are fine); same as P3 L7, Low. **Colour-page answer boxes are 8.0 mm, not 9 mm as the build report says (M4).**

Per-page reading at 1-bit: nothing lost on any page. Items to note: P4-14 item 2 bars (8-cell bars of 30 mm, cells 3.3 mm with a white inset) countable at 100 dpi but dense; P4-15 number lines clean (minor ticks 0.3 mm); P4-19 arm covers printed numbers (M3); P4-28 item 2 label touches the number badge (L1); P4-32 circled letters small (L3); P4-36 nets drawn at two different line weights (L4).

## 5. Similarity

Private sources: 49 files, of which 27 are text or data (18 md, 5 jsonl, 3 txt, 1 tsv; the tsv was not scanned, 3.5 million characters scanned) and 22 are scripts. As in the P3 audit they are catalogues, summaries and records of papers, not full question text. Own content: `p4/content/l1.js` to `l10.js` (holiday Level 4 lessons) and `extension/data/l4_u01..u10.json`.
- **Private, 6-word runs** (every page, instructions included): only generic frames ("what is the value of the digit 3", "write the missing number in the box", "I am a multiple of 7", "the length of a rectangle is", numbers 1 2 3 4 5 6). **Private, numbers plus words** (two or more shared numbers with three or more shared content words; one shared number with four or more shared words): the only hits are false (a page footer matched a record year). No page repeats a private question with its numbers. This is a lexical check; a reworded same idea would not show.
- **Own content, 6-word runs**: "value of the digit 6 in" (extension u02, u05), "I am a multiple of 7" (u01 and l1), "start at 0 on the arm along the base" (u06), "How many squares are shaded in" (u08), "find the area and the perimeter", "a path 2 m wide goes" and "cut from one corner" (l7), "equal pieces how long is each piece" (l5), "2/5 of a number is" (l4).
- **Closer matches found by reading the extension units (M1):**
  - **P4-38 "Books borrowed from a school library in one week" (line graph, Mon to Sat, values 30, 45, 35, 55, 45, 25; questions: read one day, read another, two days together, a rise, a difference)** against extension **L4U09-S01** (library visitors, line graph, Mon to Sat, values 30, 45, 25, 60, 55, 95; "each line is worth 10"; Thursday, Tuesday, "Monday and Tuesday together") and S02 (greatest increase). Same scenario family, same days, same first two values (30, 45), the same dashed or solid half-line reading.
  - **P4-37 "Pupils in three classes who chose each club"** (rows 4A, 4B, 4C, a Total row and column, six missing numbers, "row by row") against extension **L4U09-S03** ("The table shows the library books 3 classes borrowed. Each row and each column adds up to its total. Write the missing numbers." rows 4A, 4B, 4C, Total row and column, six empty boxes, "Go row by row"). The numbers differ; the item design, the labels and the six-box count are the same.
  Owner addendum 6 and your rule say the school books must not duplicate our extension items. The numbers are not identical, so this is not a literal copy, but a school buying both products would see the same item twice. Fix by changing the scenario and labels (not 4A, 4B, 4C; not a library; not Mon to Sat starting 30, 45) and re-seeding.
- **Lower overlaps, own content (L10):** P4-20 item 4 "2/5 of a number is 8. What is the number?" is `l4.js` "2/5 of a number is 16. What is the number?" with a new number. P4-26 item 4 ribbon cut into equal pieces is `l5.js` "A ribbon 4.8 m long is cut into 6 equal pieces. How long is each piece?" (new numbers). P4-30 item 4 "A path 2 m wide goes round the outside" is `l7.js` "A path 2 m wide goes all round a lawn 10 m long and 6 m wide" (same width); P4-30 item 2 (square cut from a corner, perimeter) echoes the `l7.js` exit ticket and extension u07 (rectangle 12 by 9 with a corner cut off). P4-09 riddles "I am a multiple of 7 ..." echo extension u01-C04. P4-34 (shade the mirror half and count shaded squares) is the item type of extension u08-S04. P4-19's "Start at 0 on the arm along the base" is the u06 explanation wording. Figure data (L-shapes 6/4/9/10, 5/5/3/7, U 3/3/4/8/10, T figures) were compared with the extension `l4_poly` entries (10/6/4/2, 11/3/7/8, 12/9/7/4, 12/8 stairs, 9/3/4/7): none repeat.
- Scenario nouns searched in own content (chess, library, borrowed, noodles, soup, pasta, ferry, tank, tray, eggs, ribbon, stickers): only the ribbon and the library/classes cases above.

## 6. Front matter, keys, teacher notes against the owner decisions

Checked the cover, licence, two notes pages, contents and coverage list, and both keys, as text and images.
- Two booklets per level, 20 single-sided A4 pages each (20 + 20; fronts 5; keys 10 and 9; packs 25 each): yes. 10 one-star and 10 two-star in each: yes (counted from the key). Black and white, photocopy-ready: yes (section 4). Code word with no second real-word arrangement: yes (section 1). Colour-by-code pages: three (P4-05, 11, 40). Annual licence ("covers one school year and is renewable"): yes. Publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers" on the cover, registered office 66 Tannery Ln on the licence page, contact pypteltd@gmail.com marked "business email for now": yes. DRAFT on cover, licence, notes, keys: yes; none on pupil pages. Originals only: yes (section 5). No price anywhere, no Mi, no SASMO.
- **"Not affiliated with or endorsed by the Ministry of Education, Singapore." appears once, on the cover only; the licence page has the factual "The mathematics syllabus is published by the Ministry of Education, Singapore."** Text search of the 8 PDFs for MOE, Ministry, SASMO, align, approved, endorse: nothing else. Compliant.
- "Pictures are not actual size." is in the teacher notes (front matter page 4 of both booklets). Colour pages are geometric vehicle pictures (bus, lorry, ferry) made of boxes and circles, no cartoon animals; the owner asked for "a few mature-style (geometric) pages" at P4 to P6: acceptable, though a bus, lorry and ferry are not mosaic or mandala.
- **M5. Both keys cite the wrong syllabus pages.** "Primary 4 content in the Mathematics Syllabus, Primary (2021 edition, pages 33 and 34)" is the Primary 2 citation, copied from the P2 template (`school/p4/render.py` line 357). Primary 4 is printed pp. 37 to 40 (P2 pp. 33 to 34, P3 pp. 35 to 36). Fix the sentence (and note the key still prints the generic "Problem solving marks a page..." line, which is true here: the S1 and S2 notes list the pages).
- **M6. Teacher-facing text that contradicts the pages.** (a) S1 notes, "Loop. The numbers on touching tiles must match all the way round the loop": P4-13 is a ring of arrows ("Do you come back to the start number?"), not tiles; it is the P2 domino text. (b) S2 notes, "Total. The whole count must make the total printed in the strip (the graph pages add a second sum)": no strip prints a total except P4-25 (6.99, in the instruction as well); the graph pages have none. (c) S2-13 key teacher note describes "a rectangle cut along its middle, along its diagonal ... Two show no line ... (a scalene triangle and a trapezium with a right angle have none)": the page shows an isosceles trapezium and a T with no line (both have one line of symmetry, answer Yes), a triangle with a line, a kite, a T with a horizontal line, a pentagon. (d) S1-15 note: "halves, thirds, quarters, fifths, sixths or eighths ... from 0, 1, 2 or 3, each three units long": the page uses halves, quarters and eighths only and its first line runs 1 to 4. (e) S1-19 note: "The decoy letters stand for 180 minus the angle (the wrong scale)": no table value is 180 minus an answer (125, 135, 110, 65, 85, 50 are absent), so a wrong-scale reading simply is not in the table; and "an arm never lies over a printed number" is false (M3). (f) the S2-19 (P4-39) key note says "thin dotted lines"; the lines are dashed. These are all in the answer-key voice, not on pupil pages; fix before a teacher reads them.
- M7 coverage wording: see section 2.

## 7. Findings

### High
None.

### Medium
**M1. P4-37 and P4-38 echo extension unit L4U09 (S03 table and S01 library graph).** Details in section 5. Fix: change scenario, row and column labels and the first values, re-seed, re-run `validate.py`.

**M2. Four sentences over the 14-word limit and a validator blind spot (P4-08 item 6, P4-20 item 5, P4-30 item 5, P4-38 item 6).** Suggested rewrites: P4-08 item 6 "Pick the common factor of 28 and 98 between 2 and 14." (12). P4-20 item 5 "Aisha spent 3/8 of her savings on a toy and 1/4 on a card." (14). P4-30 item 5 "Two 10 cm by 3 cm rectangles are joined along their long sides." (13) then "Find the perimeter." P4-38 item 6: "How many more books on the busiest day than on the quietest?" Also make V8 split at "?" and "!" and cover all card classes.

**M3. P4-19 protractor: the arm lies over printed numbers and the readable precision is tight (items 1, 2, 4, 5).** The key and the generator note claim "an arm never lies over a printed number". Measured on the render: item 1 (125 degrees from the right) runs over the outer 120 and the inner 60 (the 6 is struck through, visible at 150 dpi 1-bit); item 2 (45) covers the outer 40 and the inner 140; item 4 (115) covers the outer 120 and inner 60; item 5 (85) touches the outer 80. Items 3 and 6 are clear. The inner scale carries numbers only at 40, 60, 120, 140, so item 5 (95 on the inner scale) has no nearby inner number and the pupil must count from 60 or read the outer 85 and subtract from 180. A 5 degree tick is 1.35 mm apart on the inner scale and 2.4 mm on the outer, under a 1.0 mm arm that hides the tick it sits on. Decoys are at least 5 apart so a slip of 5 is caught, and a wrong-scale reading is absent from the table (a pupil learns the scale is wrong, which is a hint). See decision 4.

**M4. Colour pages P4-05, 11, 40: answer boxes are 8.0 mm square (not 9 mm), against 12 to 13 mm on P3's colour pages and 12 mm elsewhere in P4.** They must hold "20 000", "3.05", "1260". The P2 audit accepted about 9 mm for three-digit answers; here 6 characters. A pupil writing a 5-digit number in 8 mm will not be legible to the teacher. Fix: 11 mm squares or 14 mm wide by 9 mm high boxes; check no label collides (the validator's label check exists).

**M5. Key cites "pages 33 and 34" of the syllabus for Primary 4 (both keys).** Should be pages 37 to 40. `school/p4/render.py:357`.

**M6. Teacher-note statements that do not match the pages** (loop wording S1 notes; "graph pages add a second sum" S2 notes; S2-13, S1-15 and S1-19 key notes; "dotted" S2-39). Section 6.

**M7. Coverage claims stronger than the pages: FM2.5 only for the pair 3 and 9 (P4-09 items 2 and 4); RS2.2 listed as covered in the contents with no "partly".** Fix: make P4-09 item 4 use two unrelated 1-digit numbers (for example 4 and 6) and either add "partly" to RS2.2 in the front matter or rename it "choosing the corner that completes the shape".

### Low
**L1. Label collisions and tight labels.** P4-28 item 2: "3 cm" (left side of the T) touches the circled number 2 (0.5 mm overlap). The two stacked "6 cm" labels at the stem (P4-28 item 2) and the stacked "4 cm" and "7 cm" at the stem of F (P4-29) are readable but close; the first is the horizontal ledge, the second the stem. P4-27 items 4 and 6: "perimeter 74 cm" and "perimeter 36 cm" fill the rectangle from side to side and touch the borders. Cards on P4-30 almost abut (1 mm gap).
**L2. P4-18 items 5 and 6:** the letter a sits off-centre (right of the middle arm in item 5, left in item 6) over an arc that spans all three arms; the decoys catch it, but a pupil may read a as the near part. Centre it above the arc or on the arc's far end beyond the arms.
**L3. P4-32:** circled letters are 7.6 pt (below the 8 pt rule the validator reports); circle about 3.4 mm; dots 1.1 mm. Two of three choices are far from the shape in every item (C and B in item 2, M and A in item 1), so the page is easier than a two-star implies. Make decoys near the shape (one grid step off).
**L4. P4-34 grid rows look uneven at 100 dpi (anti-aliasing); P4-36 nets are drawn at two weights (about 0.44 mm and about 1.0 mm).** Both survive 1-bit.
**L5. Check-strip letter boxes 10.3 to 10.6 by 11.6 mm** (under 12 mm).
**L6. P4-10 and P4-12 give no working space** although they say "Work out each product in columns" and "Divide". Teachers will need scrap paper. (Builder weak point 9: only the product is checked.)
**L7. P4-14 item 2** says "Write the shaded amount as a mixed number. What is the whole number?" and offers one box for the whole number only; bars are 8-cell bars of 30 mm, dense.
**L8. P4-09:** item 3's third clue "I am a factor of 92" is already implied by "a common factor of 46 and 92" (redundant, not wrong); items 2 and 4 use the same pair (3 and 9); the line breaks leave the single words "60.", "9.", "92.", "54." alone on a line.
**L9. Tiering.** P4-07 (1 star) tests 4-digit numbers for multiples of 7, heavier than several 2-star pages; P4-22 (2 stars) is three plus three decimal cards (one skill in two directions) and the page is half empty; P4-37 (1 star) needs a four-step chain to find 4B's total. Suggest P4-22 to 1 star and P4-37 to 2 stars (keeps 10 and 10 in S2); P4-07 is the one to keep an eye on in a pupil trial.
**L10. Own-content frames** (section 5): P4-20 item 4, P4-26 item 4, P4-30 items 2 and 4, P4-09, P4-19 wording, P4-34 item type.
**L11. P4-35:** the cube (item 3) has a square front face, but an oblique drawing cannot show that depth equals width; the cuboid (item 5) is clearly long. Accepted convention; keep the cuboid at least twice as long (it is). The square pyramid (item 1) shows two faces and no visible square; there is only one pyramid choice, so it is safe.
**L12. Half cases in P4-04:** 29 500 about 30 000 (nearest 1000, on the route) and 21 455 about 21 460 (a dead end) are exact halves. The teacher note says pupils round half up; the pupil page does not say so. A pupil taught differently would find no route. Low because round-half-up is the Singapore convention.
**L13. Two-option rows (P4-06, 31, 33) have 64 combinations;** a pupil can try them against the word check. The notes admit guessing is possible; keep as is.
**L14. Colour pages are weakly self-checking by design:** the tally and the twin marks let a pupil place a colour without computing it. The key and notes say so; acceptable.

### Information
- The symbols about (≈) and angle (∠) are drawn as pictures, so they are not selectable text.
- P4-39 item 6 ("How many pupils are in half of the pie chart?" = 160) needs no reading of the chart.
- The builder's claim "0 failed of 736 checks" is true of the checks that exist; V8 (reading) and the 12 mm answer-box check do not cover the findings M2 and M4.

## 8. The builder's decisions (the build report lists six): my recommendation

1. **Licence wording, title, Ministry sentence stay DRAFT until owner and lawyer approve:** agree. Keep the not-affiliated sentence on the cover only (it is). Run `build.py --final` only after the lawyer; re-run the front-matter checks after fixing M5 and M6.
2. **Gaps AN1.3 and NT4.2:** keep them as stated gaps in this edition. A self-check printed on the page is the owner's rule (addendum 8). If you want AN1.3 later, the measured check K9 in `plan.md` works for an angle: "Draw angle ABC of 70 degrees with AB and BC 6 cm; the ends A and C should be 6.9 cm apart, give or take 2 mm" (2 x 6 x sin 35 degrees); it depends on 100% printing and a ruler, so test it on a real copier first. NT4.2 has no comparable check; leave it to lessons.
3. **Colour pages:** keep the three abstract boxy pictures (they fit "geometric, not cartoon animals"); do not commission art yet. **Do not keep 8 mm boxes**: enlarge to at least 11 mm (M4). Correct the build report (8, not 9 mm).
4. **Protractor numbers:** neither of the two options. Every 10 degrees on the inner scale is too crowded at a 15 mm radius. Instead: print numbers at every 20 on both scales (add inner 80 and 100), choose arms at 10 degrees from a multiple of 20 or at least 8 degrees from any label (angles 30, 50, 70, 90, 110, 130, 150 are clear), thin the arm from 1.0 to 0.7 mm, and keep the code table steps at 10 apart. This removes M3 and still tests choice of scale and counting ticks.
5. **Split of the year** (S1 whole numbers, factors and multiples, four operations, fractions, angles; S2 decimals, area, rectangle and square, symmetry, solids, data): acceptable. Nothing in a page depends on the split and the notes say schools vary. Whether angles belong in Term 2 or Term 3 differs by school; consider a one-line note that S1-18, S1-19 may be used later.
6. **One and two stars:** the reading "two steps or two clues" holds for most pages. Confirm it, and re-tier P4-22 to 1 star and P4-37 to 2 stars (L9). A short pupil trial of P4-07, P4-19, P4-34 and P4-36 would show whether the 1-star and 2-star labels are right.

## 9. validation_report.txt

Read in full: 736 PASS, 0 failed. It does cover the word tests I repeated (V2, V3, V3c, V3d, V3e, V4), the independent solvers, tier counts, outcome coverage, stroke widths, 12 mm answer boxes (colour pages excluded), 8 pt text, black and white, and 1-bit ink loss at 150 dpi. Gaps in what it checks: sentence length for "?" sentences and card text (M2), colour-page answer-box size (M4), the 7.6 pt circled letters on P4-32 (L3), the key's syllabus page numbers (M5), prose claims in the teacher notes (M6), and similarity to our own content (the build report's check covers only the private sources). I did not rerun it.

## 10. What I could not check

- A real photocopier and real print: all 1-bit results are simulations at 100 and 150 dpi. A 600 dpi copier is kinder; a worn or toner-saver copy is harsher for the 0.24 mm borders and the 0.35 mm ticks and dashed lines.
- Real pupils: no reading trial, no timing, no check that Primary 4 children can read the inner scale on P4-19 or fold the nets on P4-36.
- The lawyer and the licence wording; the Preciouslyours business details beyond what is printed.
- Similarity is lexical (word and number match) and by my reading of the own-content items. It cannot prove that no school paper has the same idea in other words. The private folders are summaries, not full papers; one tsv was not scanned. I did not compare with the other levels' extension data.
- The syllabus PDF: I read Primary 4 (pp. 37 to 40) and Primary 5 (pp. 41 to 42) only, and used it as data. Whether the typical term order in decision 5 matches the 2027 school calendar is not in the PDF.
- Thin-line widths come from PyMuPDF stroke widths (they match a 1 px CSS border = 0.26 mm). Text sizes come from the PDF font sizes. I did not rebuild any PDF.
