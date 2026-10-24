# Round-2 independent audit: Primary 2 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent (not the builder). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`, HEAD `573bb86`. Nothing was edited, pushed or PR'd; only this report was added.
Subject: `school/p2/out/P2_S1_*` and `P2_S2_*` (Puzzles 20 pp, FrontMatter 5 pp, Complete_Pack 25 pp, Answer_Key 11 / 9 pp). Compared with `docs/audit_final/p2_semester_booklets_audit.md` (round 1) and the "Audit round 1" section of `docs/school_books/p2_semester_booklets_build_report.md`.

Method. The pupil PDFs were rendered (100 dpi; 150 dpi 1-bit; 300 to 600 dpi crops for dials, coins and fractions). Every page the fixes touched was **solved by hand from the image before the key was read**; P2-39 (the new house) was coloured by hand part by part. Dial and clock readings were also measured from pixels. Code words were tested with a list larger than the builder's (python `english-words` web2 plus `wordfreq` top 150 000, 4 to 7 letters).

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **Print-ready as to content.** All hand-solves agree with the key, no code word has a second real arrangement, the round-1 High is closed. Only Low items remain (below), plus the owner's items. |
| Semester 2 | **Print-ready as to content, one owner decision outstanding (M3, time durations on P2-29/31/40).** All hand-solves agree, no second word, coins now legible. |

Both remain DRAFT by the owner's own rule (lawyer approves licence wording; owner compares coin and note art with real money; no pupil trial; no real photocopier test). Nothing found in this round blocks a print run once those owner items are cleared. No High and no new Medium.

## 1. Hand-solve of the changed pages (from the image, then compared with the key)

All agree with the key: **0 wrong, 0 unsolvable, 0 with two answers.**

| Page | My answer from the image | Result |
|---|---|---|
| S1-02 P2-38 Rocket | 250 R x2 (top quarters), 340 B x4 (side circles, 3 hundreds 4 tens, 100 more than 240), 120 Y x3 (two mid cells, nose base), 560 O x2, 470 G x4 (centre, two wings, nose). Tally Y3 R2 B4 G4 O2 = strip; every left/right pair matches | agree |
| S1-06 P2-11 | 580, 790, 194, 630, 704, 326: A N S W E R: ANSWER | agree |
| S1-10 P2-13 | 424-298 digit 2; 560+291 digit 6; 538 digit 5; 558-180 digit 8; 740-317 digit 4; 144+230 digit 1: C R E A M Y | agree |
| S1-16 P2-20 | T, T, F, F, T, F: W I Z A R D (item 4 now divides by 3: "27 / 3 = 8" false) | agree |
| S1-17 P2-39 House | blue 35 x4 (circle, ellipse, two roof panels), green 40 x3 (roof top, two halves of the ball), red 28 x3, orange 45 x3, yellow 24 x4 (tower, three base blocks). Tally Y4 R3 B4 G3 O3 = strip. Mark sets: moon B,B; triangle B,B; star G,G; square R,R; dot O,O,O; plus Y,Y,Y: all consistent | agree, strip rule true |
| S1-18 P2-15 | 1/12, 2/3, 7/12 (counted 4 x 3 grid), 1/4, 4/5, 1/5: F R O Z E N | agree |
| S1-19 P2-21 | Set A smallest first B O T; Set B greatest first A N Y: BOTANY | agree |
| S1-20 P2-22 | 1/6, 4/5, 11/12, 9/12, 3/8, 7/12: F A T H O M | agree |
| S2-01 P2-06 | $2.65, $1.85, $2.90, $6.15, $10.25, $2.45: S A I L O R | agree |
| S2-04 P2-24 | purses S 2.10, P 1.15, C 1.40, U 2.20, A 3.00, M 1.70; items 1.40 C, 3.00 A, 1.70 M, 1.15 P, 2.20 U, 2.10 S: C A M P U S | agree |
| S2-06 P2-25 | needles measured: 9 kg (110 deg), 8 kg (84 deg), 250 g, 150 g, 1 kg, 950 g: F I G U R E (measured 9.09, 8.11, 255.6, 157.4, 1.09, 957 on the scales; nearest labelled mark clear each time) | agree |
| S2-08 P2-27 | 25 kg, 60 g, 5 kg, 3 kg, 8 l, 5 g: H U N G R Y | agree |
| S2-09 P2-28 | Set A heaviest first: P 3 kg, E 2 kg, A 1 kg; Set B least first: N 5, U 7, T 8: P E A N U T | agree |
| S2-10 P2-07 | 9:19, 3:52, 7:24, 4:47, 7:21, 1:25: T E A C U P (minute hands measured from pixels: 18.8, about 53, 24.0, 46.6, 21.0, 24.7 minutes; each within the one-minute reading error of the printed time) | agree |
| S2-11 P2-30 | 210, 4 (250 = 4 h 10), 180, 30, 85, 5: T O N G U E | agree |
| S2-13 P2-31 | Drawing 55, Story time 35, 11:10 to 11:15 = 5, 45 + 35 = 80, 8:00 to 9:30 = 90, 70 - 55 = 15: B A N D I T | agree |
| S2-14 P2-32 | small open square, open circle, open triangle, large triangle, upward large triangle, filled circle: B E H I N D | agree |
| S2-15 P2-33 | small filled square, filled square, filled circle, small circle, wide filled rectangle, open down-triangle: C O B A L T | agree |
| S2-16 P2-34 | cylinder, cuboid, sphere, cone, cube, cuboid: B A C K U P | agree |
| S2-18 P2-36 | key = 2: Blue 14, Yellow 10, Green - Black = 16 - 8 = 8, Green + Red = 20, total 52, Yellow - Red = 6: D O N K E Y | agree |
| S2-19 P2-37 | 200 / 10 = 20 pictures; 3 + 5 + 6 + 2 = 16, so mangoes 4 pictures (unique). Answers 4, 40, 20, 10 (30 vs 40), 30 (50 vs 20), 200: F A M I L Y | agree |
| S2-20 P2-40 | blue 90 x4, orange 135 x2, red 75 x4, green 105 x2, yellow 45 x2; every left/right pair matches the tally strip | agree |

Also looked at, unchanged: S1-12 P2-04 (L E N G T H), instructions on S1-05 ("Make a 3-digit number.") and S1-13 ("The sharer gets a share too."): both present.

## 2. Code words (new and old)

- Anagrams of all 32 code words (all permutations, both lists): **no second real word for any**. Hits are only non-words or misspellings: duclos, warnes, danity, lenght, solari, cubone, trung, tounge, mazie, feith, ifthe, theif. The new words CAMPUS, TEACUP, FATHOM, HUNGRY, DONKEY, FAMILY, BOTANY, BEHIND, COBALT, BACKUP, BANDIT, FIGURE, PEANUT, WIZARD, TONGUE, ANSWER, CREAMY: none.
- All 32 words are distinct (13 on S1, 19 on S2; the other pages are routes, loops, colour pages).
- Single slip (one answer replaced by any other letter in that page's code table), 13 changed code-table pages (P2-04, 06, 07, 11, 13, 15, 22, 24, 25, 30, 31, 36, 37): **0 real words**. SIRING (round-1 L5) is gone (P2-07 now TEACUP; "siring" and "jailor" are on the reject list).
- Lettered-choice pages, every combination of the printed letters: P2-20 (64), P2-27, 32, 33, 34 (729 each): the only word on each page is the intended one.
- Ordering pages: P2-21 and P2-28, all 720 permutations and all within-set swaps: only BOTANY and PEANUT. P2-24 (purse letters), all 720 permutations of S P C U A M: only CAMPUS.
- Two-slip words still exist on some pages (as in round 1). The booklets claim only single slips and rearrangements, so this is information only.

## 3. Key against the pupil pages

Read the key text for P2-04, 06, 07, 11, 13, 15, 20, 21, 22, 24, 25, 27, 28, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40 and the two colour key pages (rocket, house, with the colours printed in brackets): **all answers and code words equal my hand-solves.** Pack = FrontMatter + Puzzles (text identical, both booklets). Page counts 20 / 5 / 25 / 11 and 9. The word "dinosaur" appears in no PDF. `validation_report.txt`: 747 checks, 0 failed. Colour pictures: every part label sits inside its region.

## 4. Photocopy (1-bit) checks

- **P2-15 fractions: closed.** Shaded parts are black fills with a 26 px (about 1.1 mm at 600 dpi) white line between them (round 1 measured 0.17 mm). Outer outline to shaded fill is 3 to 4 px, which merges harmlessly. At 150 dpi 1-bit, and with 1 px of simulated toner spread, every shaded cell and pie wedge can still be counted.
- **Coins P2-06 / P2-24: mostly closed.** "cents" and "dollar" are now about 7.7 pt on every coin, and at 150 dpi 1-bit they read on all coins; numerals, coin art and the notes are clear. Residual: see L-A.
- **Colour pages (rocket, house, butterfly):** at 150 dpi 1-bit every mark (moon, star, triangle, square, dot, plus) is distinct and inside its part, the boxes (about 7.5 mm) are clear and no label is cut. See L-C for the 3-digit boxes.

## 5. Round-1 findings: closure

| # | Round-1 finding | Status now |
|---|---|---|
| H1 | Dinosaur check strip contradicts a correct colouring | **Closed.** House verified by hand (section 1): no eye or decoration, no mark on a boundary, strip rule true. |
| M1 | "cents" too small on coins | **Closed for legibility** (7.7 pt, reads at 1-bit); a small residual in L-A. |
| M2 | Fractions hairline gap | **Closed** (1.1 mm). |
| M3 | Durations from start and end times sit on the P3 outcome (P2-29, 31, 40) | **Open, by design.** The coordinator held it for the owner. P2-31 items 3 and 5 and the P2-40 clock-interval parts are the cases. Owner must accept or trim; not a defect in the printing. |
| M4 | Colour-box size | **Closed** for 2-digit, tight for 3-digit (L-C). |
| M5 | P2-10 "make the number", P2-09 same words | **Closed** ("Make a 3-digit number."; key note says touching boxes can share words). |
| L1, L3, L4, L5, L6, L7, L10, L11 | | Closed: L3 line present; L4 now divides by 3; SIRING gone; plan rows regenerated (P2-40 now Time 2.1 to 2.3); validate label "on average per page"; "purse" no longer on P2-06; cuboids about 2 : 1. |
| L8 | Two parts "1 h 30 min = [ ]" and "1 h 15 min = [ ]" on P2-40 have no unit after the box | Open (builder left it); Low, see L-D. |
| L9 | Clock numerals | Info only. |
| L12 | "Not affiliated with MOE" sentence on P2 licence pages | Owner item, open. |

## 6. Remaining items (all Low except the owner decision)

- **L-A. 5 cent coin: the word "cents" still touches the dashed inner ring** at both ends (clear at 400 dpi; the 10 cent coin nearly touches). It reads at 150 dpi 1-bit, but the build report says "placed clear of the dashed ring", which is not true for the 5 cent coin. With a heavy toner (a 1 px spread at 150 dpi simulated) "cents" on 5, 10 and 20 cent coins becomes a blob, though the numerals stay clear. Suggest dropping the dashed ring on the 5 and 10 cent coins or setting "cents" 0.3 mm higher. Does not change any answer.
- **L-B. Stale text in the key and README.** The S2-15 (P2-33) key prints internal labels as answers: "1) sizecol: C; 2) two: O; 3) two: B; 4) shapesize: A; 5) two: L; 6) turn: T". The teacher note on the same page lists "half circle", which the page does not use. `school/p2/README.md` line 77 still says "S1-17 (P2-39) Colour the Dinosaur". The teacher-facing key is not for pupils, so Low.
- **L-C. Three-digit answers in the 7.5 mm boxes (rocket, butterfly)** are tight for a pencil (three digits need about 8 mm). The page also lets a pupil write Y/R/B/G/O instead; round-1 M4 asked for 9 x 6 mm. Acceptable; widen if the layout allows.
- **L-D. P2-40 units:** two parts print "1 h 30 min = [ ]" and "1 h 15 min = [ ]" with no unit after the box. Add "min" (the colour key says minutes, so the page is solvable).
- **L-E. M3 (owner).** Durations from a start and finish are P3 outcome Time 2.2. Owner decision pending; if accepted, add one line to the plan's "outside the Primary 2 list" section.
- **L-F. Owner, unchanged:** the not-affiliated sentence on P2 licence pages (L12); lawyer approval of the licence wording; coin and note art check against real money; a pupil trial and a real photocopier test (toner and heavy-ink machines both, using S1-18, S2-01 and S2-04) before the first print run.

## 7. Items checked and found fine

Front matter (annual licence, publisher line, registered office, DRAFT stamps on cover, licence, notes and key, "KEY page n of N", no price or MOE-aligned wording, school-name line) is as in round 1. The house page uses only tables of 2, 3, 4, 5 and 10 and only numbers to 45. P2-38 no longer repeats a question (seed 306). No other page changed apart from those listed in the build report.
