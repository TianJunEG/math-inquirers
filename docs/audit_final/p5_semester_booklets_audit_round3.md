# Independent audit, round 3: Primary 5 early-finisher booklets (Semester 1 and Semester 2)

Auditor: independent, narrow third-round check. Branch `claude/great-fermi-1hv4vc`, HEAD `1bdc8c6` (the P5 PDFs equal the round-2 fix commit `c2f0c88`; the working tree has unrelated modified P3 files, which another job is rebuilding). Nothing pushed, no PR, nothing edited except this report.
Compared: `school/p5/out/P5_S*_*.pdf` now against the build audited in round 2 (`b8b91f5`, the HEAD named in the round-2 report). Built data, `validate.py` and the build report were not used to solve anything: every page was solved from the rendered PDF first, the key was read afterwards.

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **Content ready.** Both changed pages (S1-05, S1-16) solved by hand: 2 of 2 agree with the key. |
| Semester 2 | **Content ready.** All 13 changed pupil pages solved by hand (the four re-themed pages, the six number changes, the four angle pages): 13 of 13 agree with the key, one answer per page. P5-39 holds for every reading of "trapezium". |

No wrong key, no page with two answers, no unsolvable page, no code word that repeats inside P5 or another level's word as the keys stand today. Everything left is Low (section 7). Two Low items are layout (a word touching an answer box on P5-16 item 6; a tight label on P5-37 item 2) and are worth a look before print. Both booklets stay DRAFT by the owner's rule. Real photocopier test, pupil trial and lawyer review are still open and are not done by this check.

## 1. Changed pages, found by diffing text and rendered pixels against `b8b91f5`

Method: PyMuPDF text compared page by page and 100 dpi renders compared pixel by pixel, all six PDFs (front matter, puzzles, key, both semesters). The two Complete Pack PDFs equal front matter plus puzzles page for page (text identical).

- Front matter: both booklets identical (text and pixels).
- **S1 pupil pages changed: 2 of 20** (S1-05, S1-16). **S2 pupil pages changed: 13 of 20** (S2-02, 05, 06, 07, 09, 11, 13, 15, 16, 17, 18, 19, 20). Unchanged in both text and pixels: S2-01, 03, 04, 08, 10, 12, 14 and every other S1 page.
- Keys: S1 key page 8 (P5-18 lines); S2 key pages 3 (P5-25), 4 (P5-26, 27, 28 note), 5 (P5-29, 30, 31), 7 (P5-35), 8 (P5-39), 9 (P5-40). Colour-page key pages (S1 p9, S2 p10) unchanged.

## 2. Per-page table (all hand-solved from the render before reading the key)

| Page | What changed | Hand solution | Key | Result |
|---|---|---|---|---|
| S1-05 P5-05 colour | instruction now 3 sentences ("Colour the part, or write Y, R, B, G or O if you have no crayon." is 16 words) | 12 ÷ 3 + 26 = 30 G, 27 ÷ 3 + 21 = 30 G, 44 − 32 ÷ 4 = 36 O, 8 + 7 × 4 = 36 O, (15 + 9) ÷ 3 + 10 = 18 R, (2 + 1) × 6 = 18 R, 49 ÷ 7 + 11 = 18 R, 45 ÷ 5 + 9 = 18 R, 11 + 5 × 5 = 36 O, 6 × (5 − 3) = 12 Y, 2 + 2 × 5 = 12 Y, 18 ÷ 2 + 15 = 24 B, 20 ÷ 4 + 19 = 24 B, 27 ÷ (3 + 6) × 8 = 24 B, 5 × (10 − 4) = 30 G. Tally Y 2, R 4, B 3, G 3, O 3 | agree, same 15 questions in the same places | pass |
| S1-16 P5-16 | item 4 now a florist | 9 P, 3 E, 6 R, 5 I, 4 O, 15 D (item 4: 18 roses, 2/3 = 12, rest 6, 5/6 = 5) | PERIOD, agree | pass; layout Low L1 |
| S1-18 key only | key line prints the true value | 5.9 × 600 = 3540, 885 ÷ 10 = 88.5 | agree | stale note fixed |
| S2-02 P5-22 colour | instruction 3 sentences | 5% of 800 = 40 G, 20% of 100 = 20 R, 50% of 50 = 25 B, 80 − 50% of 80 = 40 G, 40% of 50 = 20 R, 10% of 400 = 40 G, 10 out of 25 = 40% G, 5 out of 20 = 25% B, 10% of 120 = 12 Y, 12 out of 100 = 12% Y, 80 − 25% of 80 = 60 O, 100 − 40% of 100 = 60 O, 40 + 50% of 40 = 60 O, 150 out of 250 = 60% O. Tally Y 2, R 2, B 2, G 4, O 4; mirror pairs hold | agree, same 14 questions in the same places | pass |
| S2-05 P5-25 | new numbers, word COSTLY | $1236 C, $60 O, $20 S, $40 T, $206 L, $2050 Y | COSTLY, agree | pass |
| S2-06 P5-26 | word TYPING, item 3 = cook, 14 a minute, 84 | 5 ℓ T, $9.60 Y, 84 ÷ 14 = 6 min P, 96 ÷ 8 = 12 I, 4 × 12 = 48 N, $9 ÷ $3 = 3 m G | TYPING, agree | pass |
| S2-07 P5-27 | item 4 = mechanic, boxes aligned | 154 D, 125 ÷ 25/4 = 20 I, 55 G, 8 × 6 = 48 E, 144 ÷ 8 = 18 S, 11 × 11 = 121 T | DIGEST, agree | pass |
| S2-09 P5-29 | label 11.6 pt, full-width cards | 35 B, 27 I, 25 R, 18 T, 16 H, 77 S | BIRTHS, agree | pass |
| S2-11 P5-31 | word THIRDS, new numbers | 4 × 8 + ½ · 8 · 4 = 48 T, 8 × 3 + ½ · 8 · 3 = 36 H, 4 × 6 − ½ · 4 · 3 = 18 I, 4 × 6 + ½ · 5 · 6 = 39 R, 6 × 4 + ½ · 5 · 4 = 34 D, 8 × 6 − ½ · 8 · 4 = 32 S | THIRDS, agree | pass |
| S2-13 P5-33 | label 11.6 pt | 567 S, 126 U, 252 R, 616 E, 27 L, 196 Y | SURELY, agree | pass |
| S2-15 P5-35 | pond and tub numbers | 900 mℓ F, 8 ℓ O, 160 − 45 = 115 R, 75 ℓ M, 44 − 9 = 35 A, 50 × 50 × 20 = 50 ℓ T | FORMAT, agree | pass |
| S2-16 P5-36 | labels, taller cells | ? values by cell (row, col from top): (1,1) 95, (1,2) 55, (1,3) 70 FINISH, (1,4) 80, (2,1) 55, (2,2) 70, (2,3) 70, (2,4) 70, (3,1) 70, (3,2) 90, (3,3) 55, (3,4) 70, (4,1) to (4,4) 70. Only route from START: (4,1) (4,2) (4,3) (4,4) (3,4) (2,4) (2,3) (1,3), 8 boxes; (3,1) and (2,2) are dead ends | agree | pass |
| S2-17 P5-37 | labels 11.0 to 11.3 pt | 60 B, 70 A, 115 C, 40 K, 50 E, 145 D | BACKED, agree | pass; layout Low L2 |
| S2-18 P5-38 | title "Angle marked ?", labels 11.9 pt | 56 L, 100 I (base angles 40), 48 F, 60 T, 91 E, 28 D | LIFTED, agree | pass |
| S2-19 P5-39 | N rows rewritten | F, N, T, T, F, T = M A T R I X (section 3) | MATRIX, agree | pass |
| S2-20 P5-40 | word DEPTHS, new figures, apex arcs | exterior of 50 and 78 = 128 D, isosceles apex 58: base 61, exterior 119 E, 62 + 50 = 112 P, base angles 63 and 64 give apex 53 T, 53 and 43 give apex 84 H, apex 80: base 50, exterior 130 S | DEPTHS, agree | pass |

Unchanged pages S2-08 (P5-28) and S2-10 (P5-30) were looked at again only to test the key notes (section 6). **15 of 15 changed pupil pages: 0 wrong keys, 0 pages with two answers, 0 unsolvable.**

## 3. P5-39 row logic, solved independently

Rows read from the page, stated without the key:
1. KLMN, KL parallel to NM, legs KN and LM. N and K are the two ends of the leg KN, so they are co-interior and add to 180: K = 101, claim 79 is **F** under any definition.
2. EFGH, EF parallel to HG, legs EH and FG. H and G are the two ends of the parallel side HG, on different legs. Claim G = 54 with H = 54 is possible (an isosceles trapezium) and not forced (G = 70 is also possible; then E = 126 and F = 110, E + F is not 180, so the figure is a true trapezium with exactly one parallel pair). Both a true and a false case exist with exactly one parallel pair, so **N** holds whether "trapezium" means exactly one or at least one pair. This was the row that depended on the definition in round 2; it no longer does.
3. Rhombus ABCD, D and A are neighbours: A = 101, **T**.
4. TUVW, TU parallel to WV, legs TW and UV. U and V are the ends of the leg UV: V = 119, **T** under any definition.
5. Parallelogram WXYZ, W and X neighbours: X = 118, claim 62 is **F**.
6. Parallelogram PQRS, Q and S opposite: **T**.
F, N, T, T, F, T gives M, A, T, R, I, X. No row can be answered differently by a reader who uses the angle facts and the two stated sides. The one wrong turn left is the common belief that the base angles of any trapezium are equal (row 2 T gives W, word MWTRIX, not a word), which the check catches. The key note states the definition ("at least one pair") and why the N rows hold either way. Row letters were also run through the full 3^6 = 729 combinations (section 4): only the key word is a word.

## 4. Code words

Dictionaries: `english_words` web2 (17 468 six-letter words) and gcide (10 853), `wordfreq` top 100 000 ("strict", 13 889 six-letter) and top 500 000 ("wide", 46 290, with names and junk). Not the builder's list.
- **Inside P5:** all 31 words read back from the two P5 answer keys are different, and none is within one letter or an anagram of another P5 word.
- **Other levels as they stand today:** I read "Check result: Code word/Word" from every P1, P2, P3, P4 and P6 Answer Key PDF in `school/*/out`: 80 different words. **No P5 word is among them.** `gen/other_levels_words.json` has 86 words: all 80 plus six that no current key uses (blunt, budgie, build, melody, thief, wisdom: stale from earlier builds, harmless). The validate check reads that file, so it is only as current as its last refresh; P3 (working tree modified) and the other levels may still change, so re-read before print. Close pairs: FRUITS (P5) and FRUITY (P2, P3, P4, P6), one letter apart across books: Low, different books.
- **Heads-up outside P5:** the other levels repeat words among themselves as they stand: FIGURE and FRUITY are code words in P2, P3, P4 and P6 (FIGURE on P2 S2, P3 S1, P4 S1, P6 S2; FRUITY on P2 S2, P3 S2, P4 S1, P6 S1). Not a P5 item.
- **Changed P5 pages, wrong placements:** all rearrangements, every single slip (any other table letter in one box) on the nine table pages (16, 25, 27, 29, 31, 33, 35, 38, 40), and all combinations of the row letters on the three choice pages (26, 37, 39). No real word in web2, gcide or strict. Wide-list junk only: PEROID, BRITSH, SURLEY, FORMAR, FORMAM, MATCHE. P5-26 TYPING and P5-37 BACKED: nothing at all. Anagrams of each word: none.
- Two slips at once (information): COSTLY to JUSTLY, COOLLY; DIGEST to DETEST; THIRDS to THIRST (last two boxes), THIGHS; BIRTHS none; SURELY to SURREY; FORMAT to FORGOT, FORFAR; LIFTED to FITTED, TILTED, JILTED, LIDDED, TUFTED; DEPTHS none; PERIOD to PERCID. Rare, and the notes say so.

## 5. Colour pages P5-05 and P5-22: pupil page against key page

Method: both pages of each pair read with `pdftotext` and rendered side by side at 110 dpi. The multiset of question strings is identical (15 on the rocket, 14 on the butterfly; the key has one more line, the page footer). Part positions match one for one (dome halves, circles, fins, trapezium and nose of the rocket; wing quarters and the three lower wing bands of the butterfly). Coloured by hand: rocket yellow 2 (row below the middle), red 4 (the two rows beside the centre circle), blue 3 (fins and trapezium), green 3 (two circles and the nose), orange 3 (dome halves and centre circle); butterfly yellow 2, red 2, blue 2, green 4, orange 4. Each matches the printed tally, the key page colours and the miniature on the key note. The P6 pupil/key mismatch bug does not occur here. Left and right of each picture match.

## 6. Legibility, 1-bit, stale key notes, reading load, similarity

**Label sizes, measured from the PDF text spans (old to new):** P5-29 9.3 to 11.6 pt, P5-31 9.3 to 11.6, P5-33 9.0 to 11.6, P5-38 10.0 to 11.9, P5-40 9.7 to 11.6 (and 12.2), P5-37 10.2 to 11.3 (11.0 for the five "?" and a few labels), P5-36 degree labels 10.1 to 10.7 but the 15 "?" marks went from 10.9 to 10.4 (smaller: Low). The build report's figures are right.
**1-bit proxies at 150 dpi** (light copier: blur and threshold 100; dark copier: threshold 175) viewed at full size for P5-29, 31, 33, 36, 37, 38, 40: every number, degree sign and "?" is readable on both; P5-40 "117" and "116" no longer close up. Weak points, all Low: the white-on-black START and FINISH tags on P5-36 become hairline in the dark proxy; the thin card borders and the small "Angle marked ?" captions break up in the light proxy; the dashed lines on P5-31 are thin but countable; the 11 pt labels on P5-37 are heavy in the dark proxy ("36°", "145°"). Builder's 1-bit loss 13.7 % (limit 25 %).
**Reading load.** Instruction sentences counted from the rendered PDF text on all 40 pupil pages: at most 4 on every page (P5-36, 38, 40, 05, 22 now 3 or 4). Question sentences: longest are 16 words (P5-35 pond "The pond floor is 50 cm by 50 cm and the walls are 30 cm high."; P5-16 items 5 and 6) so inside the limit of 16; the colour-page instruction "Colour the part, or write Y, R, B, G or O if you have no crayon." is also 16 words, harder to read than the old two short sentences (Low, L3).
**Stale key notes.** P5-28 now says 1 of 6 bases is tilted and 0 heights fall outside: matches the page (item 5 base FE). P5-29: 0 and 0: matches. P5-30: "1 of the sixteen has the height outside the triangle (the base is then extended with a dotted line)": one figure (row 1, column 4) has its foot a hair outside, but the base extension is a few pixels long and solid, not a dotted line (L4). The generated wording ("1 of the six bases are tilted", "0 of the six figures have ...") is clumsy. P5-18 key now prints the correct classification and the true values. P5-25 note lists "the interest for two years" as a decoy, but the table decoys are $2060 (total when interest asked) and $194 (200 minus 6): no two-year decoy exists (L5). The P5-26, 27, 35, 36, 38, 39, 40 notes match the pages.
**Similarity** of the reframed items against all strings of `extension/data/l5_*.json` and `p5/content/*.js` (5 153 strings, sequence ratio and shared 4-grams): P5-16 item 4 (florist) closest 0.54 to L2 "Kumar has 120 marbles. He gives 1/5 ... 3/8 of the rest", same two-step frame, nothing copied. P5-26 item 3 (cook) 0.58 against u06 "A machine fills 24 bottles in 4 minutes ...", generic rate frame; the old 15 and 90 are gone. P5-27 item 4 (mechanic: 32 bikes in 4 days, 6 days) 0.65 against the same u06 bottle item: same "N in a, how many in b" skeleton and the shared "4" (Low, the frame is the skill). P5-35 pond (50 by 50, walls 30, water 20) 0.54 against "a tank floor is 50 cm × 30 cm and holds 18 litres": different task; tub (50 by 50 by 30) shares 50 and 30 with the 50 × 40 × 30 tank of u05: Low. No 4-gram run over 2 in the new text. Private-source similarity was not rerun (the changed text is shorter generic phrasing).

## 7. Remaining items

**Medium: none.**

**Low**
- L1. **P5-16 item 6: the word "of" touches the answer box** ("3/4 of" runs right up to the box edge; zero gap). It was already so in round 2 (render compared) and was missed. Narrow the text column or shorten the sentence.
- L2. **P5-37 item 2:** the "36°" label sits between the two sides of the V and nearly touches both lines; it merges in the dark proxy. Move it above the figure or widen the V.
- L3. Colour-page instruction is one 16-word sentence with a letter list; consider "Colour the part. No crayon? Write Y, R, B, G or O." in two short sentences if a fourth sentence is allowed (the colour pages have three).
- L4. P5-30 key note describes a dotted base extension the page does not clearly show; P5-28, 29 and 30 notes use awkward generated wording.
- L5. P5-25 key note lists a two-year decoy that is not in the code table.
- L6. P5-36 "?" marks are 10.4 pt, smaller than before; START and FINISH tags thin in a dark copy. P5-35 item 4 and P5-25 items split "30 / cm" and "1 / year?" across lines (cosmetic).
- L7. Code-word list: `other_levels_words.json` is a snapshot (86 words, 6 stale); other levels are still being revised. Re-read from the final keys before print. Other levels repeat FIGURE and FRUITY among themselves (not P5).
- L8. Carried: pupil trial, photocopier test, lawyer review, 9 mm colour-page boxes, 10.5 mm check-strip boxes.

## 8. What was not done

No pupil trial, no real photocopier test, no private-source similarity rerun, no read of the Primary 6 pages for leakage (the changed P5 content stays inside Primary 5 area, volume, angle, rate and percentage lines on the pages read).

**Content-ready? Yes, both semesters.** The Low items L1 and L2 are layout touches worth a five-minute fix at the final build; none changes an answer.
