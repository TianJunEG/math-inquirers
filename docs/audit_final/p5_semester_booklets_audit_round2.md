# Independent audit, round 2: Primary 5 early-finisher booklets (Semester 1 and Semester 2)

Auditor: independent. Branch `claude/great-fermi-1hv4vc`, HEAD `b8b91f5`. Nothing pushed, no PR, nothing edited except this report.
Compared: `school/p5/out/P5_S*_*.pdf` now against the commit audited in round 1 (`45065b2`). Round 1 report: `p5_semester_booklets_audit.md`. Syllabus PDF read as data only.

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **Content ready.** All 14 code-word pages re-solved by hand from the render: 14 of 14 agree with the key. Every code word unique. Only Low items remain. |
| Semester 2 | **Content ready after one small edit: replace the code word MELODY on P5-31 (S2-11), which repeats a Primary 3 word (S1-06).** All 17 code-word pages and all changed non-word pages re-solved: 0 wrong keys. Remaining items are Low or Medium-small (section 6). |

All round 1 findings are fixed as claimed except the label sizes (section 4): the labels are larger than before on P5-29, 31, 33, 38 and 40, but they are 9.0 to 10.2 pt, not "about 11 pt", and P5-36 and P5-37 were not changed at all. They stay legible. Both booklets stay DRAFT by the owner's rule.

## 1. Changed pages, found by diffing text and rendered pixels against `45065b2`

Method: every page of the six PDFs extracted with PyMuPDF; text compared line by line and the page rendered at 150 dpi compared pixel by pixel with the old commit.

**Pupil pages changed: 34 of 40.** Unchanged (text and pixels identical): S1-04 (P5-04), S1-05 (P5-05), S1-07 (P5-07), S1-11 (P5-11), S1-12 (P5-12) and S2-16 (P5-36). These are the pages with no code word, except P5-36 (below). Changed pixels only, no text change: S2-10 (P5-30, taller route cells). Front matter: only pages 4 (teacher notes) and 5 (contents with PDF numbering) changed in both booklets; cover, licence and contact pages are identical. S1 key: pages 1 to 8 changed; S2 key grew from 9 to 10 pages.

**P5-36 and P5-37 were not enlarged.** The brief says labels on P5-36, 37, 38, 40 were enlarged to about 11 pt. Measured from the PDF text spans: P5-36 is 10.1 pt (31 labels) and 10.9 pt in both versions, pixel-identical to round 1; P5-37 is 10.2 pt in both versions (only numbers and options changed); P5-38 went from 7.8 to 10.0 pt; P5-40 from 8.1 to 9.0 pt (angle labels and "?") to 9.7 and 10.2 pt. The build report's "4.1 mm type, about 11.6 pt" is the SVG unit before the figure is scaled into the card, not the printed size.

| Page | What changed | Hand-solved from the render | Key | Notes |
|---|---|---|---|---|
| S1-01 P5-01 | code letters reseeded | F R U I T S | FRUITS, agree | |
| S1-02 P5-02 | digit cards and answers changed | 2 056 789 P, 9 843 210 L, 1 028 469 A, 7 543 210 C, 7 695 210 E, 1 023 467 D | PLACED, agree | |
| S1-03 P5-03 | cards changed | 9, 25, 38, 260, 99 860, 677 200 = T O W A R D | TOWARD, agree | |
| S1-06 P5-06 | cards and tiles | 24 F, 27 A, 29 V, 56 O, 70 U, 290 R | FAVOUR, agree | |
| S1-08 P5-08 | paint and rice reframe, table | 7/8 M, 1/2 O, 1 7/9 D, 1 1/3 E, 2/5 S, 1 6/7 T (cards in order of the question) | MODEST, agree | reframe ok (section 5) |
| S1-09 P5-09 | cards | 0.14 F, 0.15 I, 0.625 R, 0.875 M, 1.2 L, 2.35 Y | FIRMLY, agree | |
| S1-10 P5-10 | check sentence only (fraction now stacked) | 2 1/4, 9 3/4, 3 1/2, 12 1/4, 6, total 21 3/4 | agree | unique; all eight lines hold |
| S1-13 P5-13 | table | 28 S, 30 T, 14 R, 63 A, 25 N, 12 D | STRAND, agree | |
| S1-14 P5-14 | cards | 1/10 P, 5/27 O, 8/21 D, 63/100 I, 5/7 U, 1 1/32 M | PODIUM, agree | |
| S1-15 P5-15 | choices | 2 1/12 Q, 14 1/4 U, 9 1/6 I, 1 2/7 R, 6 2/5 K, 1 13/15 Y | QUIRKY, agree | |
| S1-16 P5-16 | six new stories, spacing | 9 P, 3 E, 6 R, 5 I, 4 O, 15 D | PERIOD, agree | frames, section 5 |
| S1-17 P5-17 | table | 0.37 F, 5510 O, 56 U, 0.9 R, 0.06 T, 0.688 H | FOURTH, agree | |
| S1-18 P5-18 | true/false rows | F, T, T, T, F, T = M O V I E S | MOVIES, agree | |
| S1-19 P5-19 | choices | 7.944 H, 3.26 A, 8.615 R, 70 D, 86 L, 11 Y | HARDLY, agree | |
| S1-20 P5-20 | table | 2750 A, 333 S, 4980 P, 3206 E, 2034 C, 30 T | ASPECT, agree | |
| S2-01 P5-21 | stories reframed, bars, table | 10% (1 of 10), 40% (8 of 20 counted at 250 dpi), 5% (1 of 20), 30%, 75%, 98% | BRANDS, agree | |
| S2-02 P5-22 | topic line only | all 14 parts solved (5% of 800 = 40, 20% of 100 = 20, 50% of 50 = 25, 80 - 50% of 80 = 40, 40% of 50 = 20, 10% of 400 = 40, 5 out of 20 = 25%, 10 out of 25 = 40%, 10% of 120 = 12, 12 out of 100 = 12%, 80 - 25% of 80 = 60, 100 - 40% of 100 = 60, 40 + 50% of 40 = 60, 150 out of 250 = 60%): yellow 2, red 2, blue 2, green 4, orange 4; mirror pairs hold | tally, agree | topic line now two lines, fine |
| S2-03 P5-23 | cards | $15 L, 22.50 A, 25.50 U, 60 G, 200 H, 225 S | LAUGHS, agree | |
| S2-04 P5-24 | GST sentence, cards | $49.05 F, 59.95 U, 65.40 S, 168.95 I, 174.40 O, 179.85 N | FUSION, agree | |
| S2-05 P5-25 | all six one year | 1025 T, 24 Y, 48 P, 520 I, 60 N, 404 G | TYPING, agree | |
| S2-06 P5-26 | five new items | 5 W, 9.60 A, 6 R, 12 M, 48 T, 3 H | WARMTH, agree | |
| S2-07 P5-27 | six new items | 154 D, 20 I, 55 G, 48 E, 18 S, 121 T | DIGEST, agree | |
| S2-08 P5-28 | wording, scale sentence | HF H, KG O, NU U, JT R, SQ L, PG Y | HOURLY, agree | angles of the SVG measured: the right one is exactly 90, every other line 26 to 35 degrees off |
| S2-09 P5-29 | numbers, labels | 35 B, 27 I, 25 R, 18 T, 16 H, 77 S | BIRTHS, agree | |
| S2-10 P5-30 | taller cells | route (4,3) (4,4) (3,4) (2,4) (1,4) (1,3) (1,2) (1,1), 8 boxes; (4,2) and (2,2) dead ends; unique | agree | |
| S2-11 P5-31 | numbers | 36 M, 34 E, 10 L, 30 O, 27 D, 33 Y | MELODY, agree | **repeats P3** |
| S2-12 P5-32 | cubes | 3x3x2 = 18 J, 2x2x2 = 8 O, 2x1x2 = 4 I, 3x2x1 = 6 N, 4x3x1 = 12 E, 4x2x2 = 16 D (edges counted at 220 dpi) | JOINED, agree | |
| S2-13 P5-33 | numbers | 567 S, 126 U, 252 R, 616 E, 27 L, 196 Y | SURELY, agree | |
| S2-14 P5-34 | numbers | 12 T, 15 A, 19.2 L, 20 K, 22.5 E, 48 D | TALKED, agree | |
| S2-15 P5-35 | six new items | 125 F, 28 O, 30 R, 70 M, 36 A, 650 T | FORMAT, agree | pond, section 5 |
| S2-17 P5-37 | numbers | 60 B, 70 A, 115 C (adjacent to 65), 40 K, 50 E, 145 D (vertically opposite) | BACKED, agree | |
| S2-18 P5-38 | numbers, labels 10 pt | 56 L, 100 I, 48 F, 60 T, 91 E, 28 D | LIFTED, agree | |
| S2-19 P5-39 | rewritten | F, N, T, T, F, T = M A T R I X | MATRIX, agree | section 3 |
| S2-20 P5-40 | numbers, labels | 140 C, 79 O, 130 S, 92 T, 133 L, 110 Y | COSTLY, agree | |

Also re-solved and unchanged: P5-36 route (4,1) (4,2) (4,3) (4,4) (3,4) (2,4) (2,3) (1,3), every ? = 70, unique, 8 boxes. **34 of 34 changed pages: 0 wrong keys, 0 with two answers, 0 unsolvable.** I solved before reading the key and read the key text afterwards. The 31 code words are the S1 14 plus S2 17 listed above.

## 2. Code words

Dictionaries: `english_words` web2 (17 468 six-letter words) and gcide (11 122), `wordfreq` top 100 000 (13 889 six-letter, "strict") and top 500 000 (46 290, "wide"; it contains names and junk). Not the builder's list. The letters of each page were read from the printed page and checked against the PDF text.
Tests: table pages (16): the 719 rearrangements, every single slip (any other table letter in one box) and, as information, every two-slip pair. Choice and true/false pages (8): every combination of row letters (729 or 64). Ordering and matching pages (7): all 720 orders.
Result: **no real word in web2, gcide or strict from any rearrangement, single slip or choice combination.** The only hits are in the wide list and are junk or names: peaced, placek, domest, strnad, strana, peroid, espect, branda, britsh, surley, formam, formar, matche. Two slips at once (information): PLACED to PEAKED, MODEST to MODEMS or ODDEST, STRAND to STRATA, TYPING to PIPING or TILING, DIGEST to DETEST, JOINED to DONNED, FORMAT to FORGOT, LIFTED to FITTED, JILTED or TILTED, COSTLY to JUSTLY: rare, and the notes already say so.
All 31 words differ from each other. **Against P1 to P4 and P6 (read from each level's Answer Key and `verification.json`): 30 are new, one repeats: MELODY is also the code word of P3 S1-06 (Big Sums).** The build report says "none equals a word used by P1 to P4 or P6" and `other_levels_words.json` does not contain it: that claim is wrong for MELODY. Also the build report lists 30 words and says 31 (BIRTHS, the P5-29 word, is missing from the list).

## 3. P5-39 forced answer

The page now says "Use the shape and the given angle. Is the claim true, false or not possible to tell?", names the parallel pair and both legs of each trapezium, and gives "Given: angle a. Claim: angle b."
Rows 1, 3, 4, 5, 6 are forced: row 1 K and N are on the same leg of KLMN so K + N = 180, claim 79 is F; row 3 rhombus neighbours 79 + 101 = 180, T; row 4 U and V on the same leg, 61 + 119 = 180, T; row 5 parallelogram neighbours, 62 is F; row 6 opposite angles, T.
**Row 2 (EFGH, F = 54, claim H = 54, key N) is the one place a pupil could reasonably differ.** F and H are opposite angles and sit on different legs, so N is the answer a Primary 5 pupil is taught. But H = 54 would give E = 126 = 180 - F, which makes EH parallel to FG. So: if "trapezium" means at least one pair of parallel sides, the claim can be true (a parallelogram) or false, so N; if it means exactly one pair (the form several Primary school books use), the claim is impossible and the answer is F. A strong pupil who reasons this way writes F and gets the letter F, the word becomes MFTRIX, not a word, so the check catches it, but the key and notes ("two angles that are not on the same non-parallel side cannot be found from each other") do not mention the definition. Recommendation: replace row 2 by a claim that is N under both definitions (for example Given: angle E = 70, Claim: angle H = 70 in a trapezium with EF parallel to HG: E and H are on the same leg, so this is F; an N row must use angles on different legs and a given that does not force a parallelogram, for example Given: angle E = 70, Claim: angle G = 70, which is N under both definitions only if a parallelogram is allowed, so check this before using it) or state in the notes that trapezium means at least one pair of parallel sides. Low to Medium. Everything else about the page is a fix: one question, one forced answer, no figure needed.

## 4. Legibility, 1-bit, and reading load

- Proxies (150 dpi, light copier: blur and threshold 100; dark copier: threshold 175) viewed for P5-29, 30, 31, 33, 36, 37, 38, 40 and the angle figures at zoom. All figure digits are readable in both. Weak points: P5-40 "144" and "128" nearly close up in the dark proxy; the degree sign is the first thing lost in the light proxy on P5-38 and P5-40 (labels 10 pt and 9.7 pt); P5-36 is dense (16 cells, 10.1 pt) but all labels are separate in both proxies and "117" no longer touches FINISH; P5-31 and P5-29 dashed lines are thin in the light proxy but countable. The apex labels on P5-38 and P5-40 are no longer clipped. Builder's 1-bit losses 13.39 and 13.62 % (limit 25 %); front matter 32.4 %; keys 29.5 and 31.4 %, so the key headroom (L11 of round 1) is now comfortable.
- Measured label sizes: P5-29 9.3 pt (was 9.0), P5-31 9.3 (8.9), P5-33 9.0 (8.5), P5-36 10.1, P5-37 10.2, P5-38 10.0 (was 7.8), P5-40 9.7 to 10.2 (8.1 to 9.0). Smallest angle figures: P5-40 items 1 to 6 (arcs about 5 mm, angle labels 9.7 pt) and P5-38 item 6 (right-angle mark 2 mm, label 10 pt): readable. Wording to correct in the build report: the labels are 9 to 10 pt printed, not 11.6 pt. Still a real pupil-trial and photocopier item.
- **Reading load: sentence length is fine** (instruction and question sentences at most 14 words on the changed pages, plan limit 16). **Instruction sentences: P5-38 and P5-40 have 5** ("Find the angle marked ? in each triangle. Ticks show sides of equal length. A square shows a right angle. Write the angle in the box. Use the code table."; P5-40 the same shape), against the plan table limit of 4. The validator counts list entries, not sentences, so it passes. This was already so in round 1 and missed then. Fix: merge or drop "Use the code table." Low.

## 5. Reframes against the closest source items (`extension/data/l5_*.json`, `p5/content/*.js`)

Method: all 2 483 own-material strings against every pupil sentence on the changed pages (sequence ratio and shared 4-grams), then the closest items read in full.
- **P5-08** (paint among 5 cans; rice among 7 bowls): closest is holiday L2 "4 litres of juice are poured equally into 6 bottles. How much juice is in each bottle?" (ratio 0.45). Objects, verb and numbers differ; only the "How much X is in each Y?" question remains. **Pass.**
- **P5-16** (kites, club money, seeds, buns, paint, library books): the generic two-step frame is the skill itself. Closest: L3 "Mei spent 2/5 of her money on a bag and 1/2 of the remainder on shoes" (club spent on prizes and food, same frame), and extension u02 "A shop sells 1/3 of its eggs in the morning. It sells 1/4 of the rest in the afternoon" against item 4 (buns, morning and afternoon, same frame, different goods and numbers). No scenario or number reused. **Pass; Low:** item 4 mirrors the egg item.
- **P5-21** (seeds, pencils): the "x out of 20" frame remains, nothing closer than 0.57. **Pass.**
- **P5-24** ("The shop adds GST of 9% to each price."): nothing similar remains. **Pass.**
- **P5-26** (sprinkler, kites, cook, baker, sand, cloth): extension u06 has "A tap fills 18 litres in 3 minutes", "An oven bakes 36 rolls in 4 minutes", "A printer prints 90 pages in 6 minutes (15 a minute)". Item 3 (cook, 15 pancakes a minute, 90 pancakes) shares the pair 15 and 90 with the printer example. **Pass with a Low:** change item 3's numbers.
- **P5-27** (bus, tailor, pens, farmer, cleaner, Ali): the frame "N things in a minutes, how many in b minutes" matches u06 "A machine fills 24 bottles in 4 minutes. How many in 11 minutes?" and "A copier makes 54 copies in 3 minutes. How many in 8 minutes?" for items 1 and 4 (farmer 32 eggs in 4 minutes, 6 minutes: same 4 minutes). The instruction "find the amount for 1 unit" is gone. **Pass; Low:** this frame is shared with every rate problem; vary item 4's time.
- **P5-35** (bin, paddling pool, pond, sink and jug, tub, box): scenarios differ. **Two number overlaps:** item 3 pond floor 60 cm by 50 cm with walls 40 cm is the tank "60 cm × 50 cm × 40 cm" of extension u05 (a tap filling a tank); item 5 tub base 40 by 30, 30 cm high resembles "A tub 45 cm long, 40 cm wide and 30 cm high is full of water". Different tasks. Low: change one dimension in each.
- **P5-35 pond sentence (the unreviewed change):** "The pond floor is 60 cm by 50 cm and the walls are 40 cm high. After the rain there is water up to 10 cm. How many ℓ is that?" It reads correctly: the water is 10 cm deep, 60 x 50 x 10 = 30 000 cm3 = 30 ℓ; the 40 cm is a distractor (a pupil who uses it gets 120, not in the table). Short (13 words longest). "up to 10 cm" could be said "is 10 cm deep" and "that" could be "the water"; neither changes the answer. **Pass.**
Verdict on the seven: no sentence skeleton is copied now beyond the generic rate, fraction-of-the-rest and tank skeletons; the numbers overlaps above are Low. Private sources: not rerun (round 1: no 7-word run; the changed text has only shorter generic phrases).

## 6. Front matter, owner decisions

Cover, licence, contact email, "annual licence", DRAFT stamps, one "not affiliated" sentence, no SASMO, align or approved wording: unchanged and present (the licence, not-affiliated and business-email phrases are present in both front matters; no "MOE" or "align" in the pupil pages). Teacher-note edits: the figures are sketches except P5-28; excluded topics "are not used in these booklets" (round 1 L9 fixed); outcome lines now numbered as in the PDF. Owner decisions are unchanged in the build report (average, pie charts, ratio excluded; simple interest, one year; GST 9%; semester split). One stale text left in the S2 key: the notes of P5-28, P5-29 and P5-30 describe "a length beside a slanted side that is not needed" and "heights outside the triangle (the base extended with a dotted line)", which the pages do not show. P5-18 key lines print the false statement ("885 ÷ 10 = 8.85") as if it were the answer; add "(true value 88.5)".

## 7. Remaining items

**Medium (fix before print)**
1. M1. MELODY (P5-31) repeats P3 S1-06. Reseed P5-31 and add every other level's words to `other_levels_words.json` (also fix the build report: 31 words, BIRTHS missing from its list).

**Low**
- L1. P5-39 row 2: answer depends on the trapezium definition (section 3); key notes do not say.
- L2. P5-38 and P5-40: 5 instruction sentences (limit 4); the validator counts list entries.
- L3. Label sizes are 9.0 to 10.2 pt, not "about 11 pt"; P5-36 and P5-37 not enlarged. Correct the report and keep them in the photocopier test.
- L4. Own-material numbers: P5-35 pond (60, 50, 40) and tub; P5-26 item 3 (15 and 90); P5-27 item 4 (4 minutes); P5-16 item 4 frame.
- L5. Key notes for P5-28, 29, 30 mention features not on the pages; P5-18 key prints the false statement as the answer line.
- L6. P5-40 items 2 and 4: the "?" is inside the triangle with no arc at the apex; a pupil could read it as the base angle (the 65 or 36 is not in the code table, so the check shows it).
- L7. Carried from round 1 and still open: pupil trial, real photocopier test, lawyer review, the colour-page 9 mm boxes, check-strip boxes 10.5 mm.

Content-ready? **S1 yes. S2 yes once MELODY is replaced; L1 is the one pedagogical item worth fixing at the same time.** No wrong key anywhere and no page with two answers. Primary 6 leakage was not rescanned in full this round; the changed content (percentage of one year, rate, area, volume, angle) stays inside the Primary 5 lines I read on the pages.
