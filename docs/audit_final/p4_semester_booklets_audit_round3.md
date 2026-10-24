# Independent audit, round 3: Primary 4 early-finisher booklets (Semester 1 and 2)

Auditor: independent (not the builder). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc` at `2b45cc4`. Nothing pushed, no PR, nothing edited except this report.
Subject: the PDFs in `school/p4/out` (Puzzles, Answer_Key, FrontMatter). Baseline for the diff: the same PDFs at `c9b72b9`, the build audited in round 2. I solved every changed page from the page image before reading the key. I did not read the data files and did not re-run `validate.py`.

## Verdict

**Content-ready (the booklets stay DRAFT by the owner's rule: lawyer, real copier, pupil trial).** All 7 pupil pages that changed in substance were solved by hand and agree with the key. No wrong key, no page with two answers, no code word that a real word replaces by one slip, 33 distinct words in P4. The footer is now legible at 100 dpi 1-bit. Round 2 M1 (instruction sentence count) is fixed. Remaining items are Low: the "Working" lines give almost no room (R3-1), the half-way sentence on pages with no rounding (R3-2), a stale key note on P4-11 (R3-3), "20 000" still tight (R3-4).

## 1. Which pages changed (text and 100 dpi pixel diff, round-2 build against now)

- **Footer only (bold 8 pt):** all 40 pupil pages (pixel difference only at y 279 to 281 mm, x 16 to 154 mm) and every other key page (they differ only in a thin strip about 2 to 3 mm high at x 16 to 121 mm, the same bold-text change; the text is identical). Front matter: no change at all (text and pixels).
- **Changed in substance (7 pupil pages, 3 key pages):** P4-04, P4-05, P4-10, P4-11, P4-12, P4-30, P4-40. Key pages with text change: P4-05 and P4-11 (colour-page key, the question lists). P4-04, P4-30, P4-40 key text is unchanged and still agrees with the page.
- Not changed beyond the footer: the other 33 pupil pages (their text is identical).

## 2. Per-page table (my answer from the image first, then the key)

| Page | What changed | My hand-solve | Key | Result |
|---|---|---|---|---|
| P4-04 Round It | 4 instruction sentences; "A number half way rounds up." | True boxes (row, column): (1,1) (1,2) (1,3) (2,2) (2,4) (3,1) (3,2) (3,3) (3,4) (3,5) (4,5) (5,3) (5,4) (5,5). False ones I checked: 16 625 (half, up = 16 630), 36 421, 75 411, 18 543 (18 500), 68 290, 79 686, 62 958, 31 950 (half, up = 32 000), 12 445 (half, 12 450), 25 875 (half, 25 880), 70 243. Only route to FINISH: (1,1),(1,2),(2,2),(3,2),(3,3),(3,4),(3,5),(4,5),(5,5),(5,4),(5,3) = 11 boxes, no box twice. Dead ends (1,3), (2,4), (3,1): exactly the 3 in the teacher note. 29 500 is on the route and needs the half-way rule, which is now printed | agree | Pass. 4 sentences |
| P4-05 Colour the Bus | Content changed | Triangle: 100 more than 2900, 1000 less than 4000, 3 in 13 968 = 3000 red (3). Square: 100 + 300, 4 in 28 410 = 400 yellow (2). Star: 2 in 25 356, twenty thousand, 19 500 to nearest 1000 (half, up) = 20 000 orange (3). Plus: 100 less than 7100, greatest of 6990/6900/7000, smallest of 7000/7101/7001 = 7000 green (3). Circle: four hundred, 4 in 73 476 = 400 yellow (2). Moon: 500 + 4000, both patterns = 4500 blue (3). Tally yellow 4, red 3, blue 3, green 3, orange 3; the printed tally and the 16 marks agree. Every answer is on the key | agree (answers, tally, the 16 colour letters R Y O Y O G G O Y G Y R R B B B in reading order) | Pass. 3 sentences |
| P4-10 Long Multiplication | "Working" line under each sum | 26 145 F, 14 319 R, 18 234 U, 20 727 I, 11 753 T, 13 580 Y = FRUITY | agree | Pass; R3-1 |
| P4-11 Colour the Lorry | Content changed | Triangle 8 x 630, 840 x 6, 2 x 2520 = 5040 orange (3). Star 140 x 12, box x 3 = 5040 (1680) red (2). Circle 140 x 9, box x 6 = 7560 (1260), 2520 / 2 = 1260 yellow (3). Plus 120 x 14, 6720 / 4 = 1680 red (2). Square 480 x 7, 210 x 16 = 3360 green (2). Moon 7 x 360, 4 x 630, 9 x 280 = 2520 blue (3). Tally yellow 3, red 4, blue 3, green 2, orange 3: matches the page | agree (answers, tally, the 15 colour letters O R Y R R Y R Y G O G O B B B) | Pass; R3-2, R3-3 |
| P4-12 Division | "Working" line in each card | 8344 / 4 = 2086 S; 4110 / 6 = 685 H; 8878 / 3 = 2959 r 1, so 1 R; 2198 / 7 = 314 I; 2124 / 6 = 354 M; 6598 / 8 = 824 r 6, so 824 P = SHRIMP | agree | Pass; R3-1 |
| P4-30 Joined Shapes | Item 5 reframed | 1) 4 squares in a row, perimeter 10 s = 100, s = 10, area 400 B. 2) corner cut: perimeter unchanged, 2(23 + 9) = 64 O. 3) side 16, small side 8, perimeter 32 T. 4) outer 27 x 16 = 432, pool 276, tiles 156 A. **5) Two 10 cm by 5 cm tiles touch along their long sides: the 10 cm sides coincide, the shape is 10 by 10, perimeter 40 N.** The shared side is not counted (a pupil who adds the two perimeters gets 60 and a single tile 30 = X, 60 is not in the table). Other readings (short sides touching = 20 x 5 = 50) do not fit the words "long sides" and 50 is not in the table. 6) width 4, length 12, area 48 Y = BOTANY | agree (key note: "two rectangles joined along their long sides") | Pass. Item 5 has one answer. 12 words, 4 sentences |
| P4-40 Colour the Ferry | 3 instruction sentences | Triangle 2.5 x 2, 0.87 + 4.13 = 5 orange (2). Square 0.61 to 1 dp, 1.74 - 1.14 = 0.6 yellow (2). Star 3.11 - 0.71, 2.35 + 0.05 = 2.4 blue (2). Plus 30/50, greatest of 0.58/0.599/0.6 = 0.6 yellow (2). Circle 25/20, 7.5 / 6 = 1.25 red (2). Moon 0.61 x 5, 0.01 less than 3.06 = 3.05 green (2). Tally yellow 4, red 2, blue 2, green 2, orange 2 | agree | Pass |

## 3. Instruction sentences and the 14-word limit

I split the instruction block of all 40 pupil pages at . ? ! ; (text taken from the PDF, with line positions). **No page has more than 4 sentences.** P4-04: 4 (it was 6). P4-05, 11, 40: 3 (they were 5). P4-07, 12, 17, 30 (S2-10), S2-02, S2-08, S2-17: 4. Every other page: 3. Round 2 M1 is closed. The colour pages' instruction is set in 13 pt (the other pages 15 pt); legible.

I split all pupil text at . ? ! ; : and counted words per sentence (item numbers and topic lines excluded): the longest question or clue sentence is 14 words or fewer on every page. P4-30 item 5 is 12 words ("Two 10 cm by 5 cm tiles touch along their long sides.") plus 7 ("Find the perimeter of both together."). The sentence counter in the validator now agrees with mine.

## 4. Code words

Method as in round 2 (web2, gcide, wordfreq 100 000 and 500 000; "strict" = wordfreq 100 000 and web2 or gcide). I read the 33 words from the key PDFs and the code tables from the pupil PDFs.
- **33 words, 33 distinct, none repeated in P4** (HUNGRY BACKUP CREAMY TEACUP FROZEN PEANUT FRUITY SHRIMP FIGURE FABRIC WALRUS BANDIT CURFEW FAMILY POLICE STUDIO WIZARD DONKEY COBALT TURKEY FRIDGE WALNUT CRAFTY BOTANY DEVOUR BOUNTY WOMBAT CANOPY FATHOM CAMPUS COUSIN FLIGHT SHADOW). The code words did not change in this round (P4-10 FRUITY, P4-12 SHRIMP, P4-30 BOTANY re-derived by hand above).
- **Anagrams (719 rearrangements each):** none on any list, except MARCEY for CREAMY (a name, wordfreq 500 000 only).
- **Single slip** (one letter replaced by any letter printed on that page, a superset of the letters offered in the row): no hit on the code-table pages. Hits only on whole-page letter sets of choice pages: CURLEW (P4-18; L is not offered in item 4's row, whose letters are P, N, F, so not reachable), KOBALT (not a word), DETOUR/DEVOUT (P4-31), BOUNCY/COUNTY (P4-32), COMBAT (P4-33), WAMPUS (not a word). The row-letter check of round 2 stands (the pages are unchanged).
- **Any wrong placement** (ordered 6 of the 9 table letters, P4-01, 08, 09, 10, 12, 30): real words exist but all need at least 3 wrong answers at once: P4-10 FRUITY to PURITY (3 wrong), PURIFY (4); P4-12 SHRIMP to PURISM, SQUIRM (4), PRIMUS (6); P4-30 BOTANY to BOUNTY, BUTOXY, JOYANT (3 wrong each; BOUNTY is also the P4-32 word) and further words at 5; P4-09 BEATUP at 3, P4-01 MURPHY at 4. Minimum distance 3: rare, as the teacher notes say. Information only (L-info, unchanged).

## 5. 1-bit legibility (300 dpi grey, area-averaged to 100 and 150 dpi, threshold 50%)

- **Vector check** of the 7 changed pages: only black and white, no images, no flat grey, white text only in the START/FINISH tags.
- **Footer** is now bold (flag 20, 8 pt) on every page. At 100 dpi the old light footer broke up ("Prec.ous.yours", "Sc.oo."); the bold one reads in full ("(c) 2026 Preciouslyours Pte Ltd. Photocopy licence. School (write name):"); the copyright sign is the weakest glyph, still readable. At 150 dpi: clear. The licence text ends at 154 mm and the page id starts at 175.7 mm on every page (gap 21.7 mm), the page id ends at 195 mm: no overflow (the P4-16 overflow noted by the builder is gone).
- **Colour boxes:** measured 15.5 x 10.9 mm (13.9 x 10.9 before) on P4-05, 11 and 40. Borders are complete at 150 dpi, no touching. A Primary 4 hand writing "20 000" (5 digits and a gap) still needs about 15 to 17 mm, so the three "20 000" boxes on P4-05 stay snug (Low, R3-4); 4 digit values and decimals fit.
- P4-05, 11, 40 viewed whole at 100 dpi: marks (triangle, square, star, plus, circle, moon), fractions 30/50 and 25/20 (small, readable), check strip, all legible. P4-04 (25 boxes, 8 pt "nearest ..." line), P4-10, 12 and 30 viewed at 100 dpi: legible; small "Working" captions legible.

## 6. Remaining items

| # | Item | Severity |
|---|---|---|
| R3-1 | **"Working" lines do not give working space.** P4-10: the thin line sits 3 mm under the sum rule and the box starts 8 mm under it (caption included); items 4 to 6 need two partial products and a sum. P4-12: items 1 and 2 have about 7 to 12 mm above the line, items 3 to 6 have about 3 mm between the question and the line (item 4 line at 148 mm). A one-line check ("314 x 7 = 2198") fits; a column or short-division layout does not. The caption promises more than the page gives. Either drop the caption or accept that working goes on scrap paper | Low |
| R3-2 | "A number half way rounds up." is also printed on P4-11 (no rounding at all) and P4-40 (one rounding, 0.61 not a half case); only P4-04 and P4-05 (19 500) use it. Harmless; a pupil may wonder | Low |
| R3-3 | P4-11 key teacher note was not updated for the new content: it lists "a multiplication followed by a subtraction" and "4 digits by 1 digit", neither is on the rebuilt page (the page has 3 digits by 1, 3 by 2, a missing factor, divisions, a story) | Low (key text) |
| R3-4 | P4-05 "20 000" in a 15.5 x 10.9 mm box is still snug (see section 5) | Low |
| R3-5 | P4-30 item 5 wording: "touch along their long sides" is unambiguous only if the whole 10 cm sides coincide; this is the natural reading and no decoy in the table collides with another reading | Info |
| Carried | Code words shared across levels (round 2 O1, unchanged, owner decision); P4-37/38 and P4-30 item 5 frame echo extension L4U09/l4_u07 (round 2 L1); P4-34 grid uneven at 100 dpi 1-bit | Low |

## 7. What I could not check

A real copier and real pupils (a trial of P4-04, 05 and 12 is worthwhile); the lawyer and licence; the Complete_Pack PDFs (assumed to be the concatenation); `validate.py` (not re-run); the key wording of the unchanged pages beyond the pixel and text diff against the round-2 build.
