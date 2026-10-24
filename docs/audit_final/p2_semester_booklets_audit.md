# Independent audit: Primary 2 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent (not the builder). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`. Nothing was pushed, no PR. Nothing in the builder's files was edited; only this report was added.
Subject: `school/p2/out/P2_S1_*` and `P2_S2_*` (Puzzles 20 pp, FrontMatter 5 pp, Complete_Pack 25 pp, Answer_Key 11 / 9 pp). Read first: `docs/school_books/p2_semester_booklets_build_report.md`, `p2_semester_booklets_plan.md`, `p2_outcome_wording.md`, `school/p2/README.md`, `docs/terms/owner_decisions.md`; model: the three P1 audits.

Method. All 40 puzzle pages were rendered (100 dpi, with 170 to 300 dpi crops for dials, clocks, solids, coins and fractions) and **solved by hand from the image before the key was opened**, then compared with the key (including P2-39, which the builder never coloured). The MOE syllabus was read from pages 33 to 36 of the supplied PDF (P2 and, to look for leakage, P3). Code words and every lettered-choice page were tested with my own word lists (python `english-words` web2: 262 866 entries; `wordfreq` top 150 000: 139 677 entries; larger than the builder's 129 000). Photocopy behaviour: greyscale/1-bit renders at 150 dpi (threshold 100 and 128), a colour scan at 50 dpi of all 8 PDFs (0 coloured pixels), flat-grey block scan, 600 dpi gap measurement, `pdffonts`, `pdftotext -bbox` for text sizes. Complete Pack = FrontMatter + Puzzles (text identical, both booklets).

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **NOT ready to print yet.** All answers are correct and every code word is unique. One High (H1: the Colour the Dinosaur check strip contradicts a correct colouring) and two Mediums that touch S1 pages (M2 hairline fractions, M4 boxes too small for 3-digit values on the rocket). Fix H1, re-render, then it is ready apart from the owner's items. |
| Semester 2 | **Content ready; fix two Mediums, then ready.** No wrong, ambiguous or unsolvable page. M1 (the word "cents" on 5 and 10 cent coins, S2-01 and S2-04) and M3 (hour-duration pages sit on the P3 outcome "finding start, finish or duration") need a decision or edit. Front matter obeys the owner decisions. |

Both: still DRAFT by the owner's own rule (lawyer approves licence wording; owner compares coin/note art with real money; no pupil trial and no real photocopier test).

## Hand-solve results (all 40 pages)

**40 of 40 agree with the key. 0 wrong keys, 0 unsolvable, 0 with two answers.** (The builder hand-solved 39; P2-39 was not coloured by them. I coloured it fully: all 15 parts, tally yellow 3 red 4 blue 3 green 3 orange 2, matches. The one thing that fails is the mark rule, see H1.)

| Page | My answer (from the image) | Result |
|---|---|---|
| S1-01 P2-01 | 848, 682, 717, 200, 512, 704: CLOUDS | agree |
| S1-02 P2-38 | 120 Y, 120 Y, 470 G, 470 G, 560 O (centre, two circles, nose), 470 G x2 (mid), 250 R x2, 340 B x3 (wings, "three hundred and forty"). Tally Y2 R2 B3 G4 O4, left/right pairs match | agree |
| S1-03 P2-09 | 259, 538, 319, 454, 746, 883, 864, 789: 8 boxes (three boxes share the words "eight hundred and eighty-three"; only one continues, see L1) | agree, unique |
| S1-04 P2-12 | 454, 748, 336, 308, 418, 388, 396, 774: 8 boxes; 208 and 362 are dead ends | agree, unique |
| S1-05 P2-10 | 285, 275, 401, 621, 718, 509: CURFEW | agree (see L2: 509) |
| S1-06 P2-11 | 580, 790, 194, 630, 704, 326: FATHOM | agree |
| S1-07 P2-17 | 498, 988, 202, 918, 773: VALET (each riddle unique, checked by enumeration) | agree |
| S1-08 P2-02 | 523, 557, 436, 506, 152, 524: DAINTY | agree |
| S1-09 P2-03 | target 655: 455+200, 653+2, 855-200, 660-5, 255+400, 625+30, 647+8, 585+70: 8 boxes; (3,1) and (2,2) are dead ends | agree, unique |
| S1-10 P2-13 | 0, 3, 4, 1, 5, 2: CREAMY | agree |
| S1-11 P2-18 | 180, 427, 755, 521, 520, 569: SPONGE | agree |
| S1-12 P2-04 | 7, 20, 9, 10, 18, 16: LENGTH | agree |
| S1-13 P2-05 | 3, 8, 4, 6, 7, 9: NUMBER (item 6 only works as 3 people, see L3) | agree |
| S1-14 P2-14 | target 10: 1x10, 20/2, 2x5, 40/4, 100/10, 10x1, 50/5: 7 boxes | agree, unique |
| S1-15 P2-19 | 6, 6, 3, 2, 7, 2; the loop closes | agree |
| S1-16 P2-20 | T, T, F, F, T, F: WALNUT (item 4 divides by 9, see L4) | agree |
| S1-17 P2-39 | 35 B, 28 R x2 (+2 body parts), 24 Y x3, 45 O x2, 35 B x2 (legs), 40 G x3 | agree; mark check fails, see H1 |
| S1-18 P2-15 | 1/12, 2/3, 7/12, 1/4, 4/5, 1/5: FROZEN (cells counted at 170 dpi) | agree |
| S1-19 P2-21 | B A N then D I T: BANDIT | agree |
| S1-20 P2-22 | 1/6, 4/5, 11/12, 9/12, 3/8, 7/12: ANSWER | agree |
| S2-01 P2-06 | $2.65, $1.85, $2.90, $6.15, $10.25, $2.45: SAILOR | agree |
| S2-02 P2-16 | $0.49, 937, 706, $6.04, $2.24, $3.41: MAGNET | agree |
| S2-03 P2-23 | B O U (6.50, 6.90, 6.95), N C E (3.95, 3.50, 3.40): BOUNCE | agree |
| S2-04 P2-24 | purses B 1.35, E 1.20, L 1.70, K 1.15, U 2.50, C 1.55 -> B, U, C, K, L, E: BUCKLE | agree |
| S2-05 P2-08 | 3, 5, 8, 4 (starts at 1), 9 (starts at 1): GRUNT | agree |
| S2-06 P2-25 | needle angles measured: 9 kg, 8 kg, 250 g, 150 g, 1 kg, 950 g: CRAFTY | agree |
| S2-07 P2-26 | 1, 4, 3, 6, 7, 8: FRUITY | agree |
| S2-08 P2-27 | 25 kg, 60 g, 5 kg, 3 kg, 8 l, 5 g: GUITAR | agree |
| S2-09 P2-28 | M 3 kg, I 2 kg, G 1 kg; H 5, T 7, Y 8 l: MIGHTY | agree |
| S2-10 P2-07 | hand angles measured from pixels: 9:19, 3:52, 7:24, 4:47, 7:21, 1:25: STRING | agree |
| S2-11 P2-30 | 180, 5, 3, 220, 65, 55: SQUARE | agree |
| S2-12 P2-29 | 3:05 to 4:30 = 1 h 25; 42 min; 3 h 7; 4 h 9; 7:10 to 7:55 = 45 min: MAIZE | agree |
| S2-13 P2-31 | 25, 30, 15, 100, 165, 50: TEACUP | agree |
| S2-14 P2-32 | large open triangle, triangle, wide open rectangle, wide filled rectangle, large open circle, large up-triangle: WALRUS | agree |
| S2-15 P2-33 | B O T A N Y | agree |
| S2-16 P2-34 | sphere, cuboid, sphere, cylinder, cone, cube: DEVOUR | agree |
| S2-17 P2-35 | cube 5, cuboid 2, cone 1, cylinder 4, sphere 3 = 15: THIEF | agree |
| S2-18 P2-36 | 14, 10, 8, 20, 52, 6 (key = 2): COUSIN | agree |
| S2-19 P2-37 | pears 20, mangoes 30 = 6 pictures: 6, 30, 20, 5, 10, 110: FIGURE | agree |
| S2-20 P2-40 | 90 B x4 (1 h 30 twice, 11:20-12:50, 1:45-3:15), 135 O x2, 75 R x4, 105 G x2, 45 Y x2; left/right pairs match | agree |

## Code words (item 2)

- Anagrams of all 32 code-word letter sets (all permutations, both lists): **no other real word for any of the 32 words.** Only non-words or names appear in the larger list (DUCLOS, DANITY, LENGHT, WARNES, SOLARI, CUBONE, LUBECK, TRUNG, UGARIT, MAZIE, FEITH, THEIF). So every ordering page (S1-19, S2-03, S2-09, S2-04) is clean for all wrong orderings.
- Lettered-choice pages tested on every combination of the printed letters: S1-16 (64 combinations), S2-08, S2-14, S2-15, S2-16 (729 each): **none spells any other word.**
- Single slips (one answer replaced by any other letter of that page's code table), 23 code-table pages: one hit, **SIRING on S2-10 (P2-07)** (STRING, T replaced by I: the pupil would have to write 4:47 for the 3:52 clock). The builder claims "no single letter put in another slot makes a word", so the word list used by `kit.py` lacks *siring*; this is the same word the P1 audit found on P1 S2-08 (STRING) and was reused (L5). Two-slip words exist (CLOCKS, JAUNTY, BROKEN, PALLOR, PARLOR, SAVIOR, TIRING, SIZING, MEMBER, RUBBER, BUMPER, JUMPER, THIGH, JAIME, SITING): the booklets only claim single slips and rearrangements, so this is information only.

## Findings

### High

**H1. S1-17 (P2-39) Colour the Dinosaur: the check strip's "same small mark, same colour" rule is false for the correct colouring.** The page shows three parts carrying the same black dot: the head circle, the upper-right body quarter and the lower-left body quarter. The head dot is the picture's *eye* (`pictures.py` dinosaur: `b.decor('<circle cx="38" cy="28" r="2.8" …>')`), in the same glyph as the twin mark for body_ur and body_ll. Correct colours: head 35 = blue, the two body quarters 45 = orange. A pupil who colours correctly and then reads "Parts with the same small mark have the same colour" (strip shows the dot) finds a contradiction and will recolour a correct answer. Two further problems on the same page: the tail (6 x 4 = 24, yellow) carries no mark, and the dot and the plus on the oval's right edge sit on the boundary between a body quarter and the tail, so which part each belongs to is unclear. The builder noted that P2-39 was never coloured; this is what colouring finds. Fix: draw the eye as a ring or a different shape (or drop it), keep all marks fully inside their part and away from boundaries, and give the tail its mark (or state in the strip that the tail has none). Check P2-38 and P2-40 do not contain the same eye pattern (they do not: no twin marks, only mirror pairs).

### Medium

**M1. Coins: the word "cents" on 5 and 10 cent coins is too small (S2-01 P2-06, S2-04 P2-24).** The build report quotes "about 2.5 mm". That is the height of the word's text box. Measured: font about 5.2 pt on the 5 cent coin (word width 5.0 mm, x-height 0.9 mm, capital/ascender 1.3 mm) and 5.9 pt on the 10 cent coin; 7 pt on 20 cent, 8 pt on 50 cent. The letters on the 5 cent coin also touch the dashed inner ring (viewed at 300 dpi, and at 1-bit). The numeral (2.4 mm) is readable; the unit word is not, on a photocopy. This is the P1 audit's M3 (1.5 mm "cents") left essentially unfixed. A pupil can still infer cents from the 5 and the coin size, and the page still scores, but "cents" is the point of Money 1.1 and 1.4. Fix: put "cents" at 7 pt or more on every coin (coins 14 mm or larger), or print "5c" style numerals with the cents sign inside a clear ring gap. The five original motifs and the note art are unchanged owner item (D1 in `coin_reproduction_check.md`).

**M2. S1-18 (P2-15) Parts of a Whole: shaded cells are separated only by a hairline of white.** Measured at 600 dpi: the white line between shaded cells in item 3 (7/12), item 2 (2/3) and the wedges of item 5 (4/5) is about 4 px, about 0.17 mm. At 150 dpi 1-bit it survives, but on a toner photocopy a 0.2 mm gap closes and the shaded cells of items 2, 3 and 5 become one black block, so the pupil cannot count the shaded or total parts (the outline of the unshaded cells is clear, the shaded ones are not). Fix: draw cell borders in black on the shaded cells too (or hatch the shaded cells with diagonal lines) so every part keeps a line at least 0.4 mm wide. Any shaded-part picture in the 1-bit test should be re-checked after the change.

**M3. Time: the pages ask for start and end times and the duration (S2-12 P2-29, S2-13 P2-31, S2-20 P2-40); the syllabus puts this in Primary 3.** P2 Time 2.2 reads "measuring time in hours and minutes". The P3 outcome (page 36) reads: "2.2 finding the starting time, finishing time or duration given the other two quantities". Items such as 7:37 pm to 10:44 pm (3 h 7 min), 6:30 pm to 10:39 pm (4 h 9 min), "From the end of Music to the start of Science", 10:20 to 12:35 and 11:20 to 12:50 are exactly that. The plan's "Excluded as above Primary 2" list does not name it. This is a judgement, not a clear error (P2 school books do ask "how long?" on a clock face), but with odd minutes and three hours across a half-day, three pages lean on a P3 outcome. Owner decision: either accept and say so in the plan, or limit durations to the clock-face items and whole-or-half-hour/5-minute steps within one or two hours, and drop the cross-hour digital items. Also the build report (weak point 8) mentions noon crossing: no page in the booklets crosses noon on S2-12 (all pm); S2-13 has Art 11:55 am to 12:20 pm (fine, labelled).

**M4. Colour-by-code answer boxes are too small for the answers (S1-02 P2-38, S2-20 P2-40; also S1-17).** The small box printed in each part is about 5.5 mm square (measured on the image). The rocket and butterfly answers are 3-digit (120, 250, 340, 470, 560; 45 to 135 min) and the notes tell pupils to write Y, R, B, G or O in each part. A 3-digit answer does not fit a 5.5 mm box for a 7-year-old's pencil (about 3 mm digits, a 9 mm-wide number). Most pupils will just colour. Fix: boxes 9 x 6 mm or a "= ___" line for 3-digit sheets, or an explicit "answer in your head" line.

**M5. Page conventions that make the check say "wrong" on a defensible answer.** (a) S1-05 item 6 (0 5 9, smallest number): 509 is the intended answer (a number cannot begin with 0). The page says only "Make the number"; a pupil who writes 059 or 59 gets no letter and a failed check. Add "a 3-digit number" to the instruction. (b) S1-03 (see L1) three boxes carry identical words. Neither is a wrong answer; both are page-wording fixes.

### Low

**L1. S1-03 (P2-09) Words and Numbers: three adjacent boxes share the words "eight hundred and eighty-three"** (feet 706, 939, 864); only 864 continues to FINISH. Both other boxes are dead ends by design, the 8-box count catches them, but the instruction "Go to the box with the word for your number" does not say that a pupil may meet more than one choice and the key's description of the wrong turns ("digits swapped, teen and ty mixed up, a zero in the wrong place") does not describe this page. Update the key note, or change the dead-end words.

**L2. S1-05 item 6** see M5(a).

**L3. S1-13 (P2-05) item 6 "Kumar shares 27 grapes equally with 2 friends".** The answer (9) needs 3 people. 27 is not divisible by 2, so the pupil can find the right reading, but the key's note says "'shares with 3 friends' means 4 people", which is not this page. The P1 audit's M4 (sharer rule) in a milder form. Put one line at the top: "The sharer gets a share too."

**L4. S1-16 (P2-20) item 4 "If 3 x 9 = 27, then 27 / 9 = 2."** Divides by 9; tables of 6 to 9 are Primary 3 (3.1). The fact family is P2 (3.3), but a divisor of 9 is outside the tables of 2, 3, 4, 5, 10. Replace with 27 / 3 = 8 or a fact with the 4 or 5 table (for example "If 4 x 7 = 28, then 28 / 4 = 6").

**L5. SIRING (S2-10 STRING)** see Code words: repeats the P1 audit finding. Change the code word or add *siring* to the builder's reject list; no other word on the page is affected.

**L6. Plan table is stale.** `p2_semester_booklets_plan.md` (section 1 table and section 2b) still lists P2-40 as "2D Shapes 1.1, 3D Shapes 2.1"; the page and key are Time 2.1 to 2.3. The plan says its tables were regenerated after the build; they were not for that row. The front matter and key are correct.

**L7. `validate.py` grey-block test is a total budget, not "per page".** It tests `blocks < limit x pages` (sum over all pages), so one grey patch could pass. I tested my own way: per-page blocks with a 40-215 grey value at the four corners (the builder's measure) are up to 195 on key page 1, 188 on S2 key page 1, 67 on S1-17, 53 on front pages; but blocks that are really flat (6 x 6 px with spread under 25 grey levels) are **0 in every page of all six PDFs**: what is counted is the edge of small text. So the raise from 90 to 130 is **sound for the keys** (text edges; viewed in 1-bit at 150 dpi: legible; the keys are teacher copies), but the label "per page" is wrong and the keys' ink-loss figure 34.5% is within 0.5 point of the 35% limit. Suggest changing the report wording to "average per page", and keep a flat-block test (as above) in `validate.py`.

**L8. Colour pages: S2-20 (P2-40)** has two parts "1 h 30 min = [ ]" with no unit after the box (the others print min). The key says 90 min; add "min". Colour-by-code small parts for pencil copies: all parts large enough for one letter on both pages (viewed); not a defect.

**L9. Clock numerals on S2-12 (P2-29).** The four small clocks have numerals of about 6.6 pt (box 8.6 pt) and radius about 12 mm: readable at 150 dpi 1-bit (viewed), but the minute hand on the two item-1 and item-5 clocks must be read on a 5-minute mark, so there is no problem. Info only.

**L10. S2-01 and S2-04 say "purse"** but no purse is drawn (S2-01 has plain rows). No effect on answers.

**L11. S2-17 (P2-35) cuboid in row 1, position 2 is 1.6 : 1 (front face).** Cube faces are 1.0 : 1, the other cuboid is 2.0 : 1, S2-16 uses 2.8 : 1. Distinct on the page; for 1-star safety make the weakest cuboid at least 2 : 1, and say in the teacher note that a cube has six equal faces.

**L12. Disclaimer sentence.** Owner decision DISCLAIMER-KEEP says the "Not affiliated with or endorsed by the Ministry of Education, Singapore" sentence stays on the **P1** booklet licence pages. The P2 licence pages carry it too (the build report lists it as the one sentence to approve). Owner to confirm that "also on P2" is intended.

## Judgement on the builder's 14 weak points

| # | Weak point | Verdict |
|---|---|---|
| 1 | Mechanism repetition (23 of 40 code-word pages) | Confirmed and accepted: it follows the owner's self-check decision; 23 + 9 lettered + 4 routes + 1 loop + 3 colour. Variety is in content and layout; a pupil trial should check boredom. Low. |
| 2 | Code tables with up to 10 boxes in 2 rows | Accepted. Viewed all: no letter touches an edge; no problem. |
| 3 | Coin art, "cents" about 2.5 mm | **Disagree: M1.** The text box is 2.7 mm but the letters are 0.9 to 1.3 mm. Owner's comparison with real money still open. |
| 4 | P2-07 clock 6 on a 5-minute mark; careful pupil | Accepted. Only one clock of six (1:25) sits on a 5-minute mark; four are within 1 to 2 minutes of a decoy (7:21, 7:22, 7:24, 7:26). Fair for a one-star page that is about telling time to the minute; hand angles measured from the image agree with the key to under one degree. |
| 5 | 3D drawings, cube/cuboid by proportion | Accepted with L11. Cube faces are square (measured); the weakest cuboid is 1.6:1. |
| 6 | Ordering pages say "something is wrong, not what" | Accepted. All 720 permutations of each of S1-19, S2-03, S2-09, S2-04: no other word. |
| 7 | Drawn work not seen | Accepted (nothing asks the pupil to draw; stated in the plan). |
| 8 | P2-29 mixes clocks and digital; noon | Content correct, but see **M3** (duration given start and end is P3 2.2). No noon crossing on this page. |
| 9 | Blank box invisible to the check | Accepted; stated in the teacher notes and the key. |
| 10 | Colour-by-code pages | **Disagree: H1** (eye = twin mark), plus M4 (box size). Colour-by-code mirror pairs and tallies on P2-38 and P2-40 are correct; P2-39 now coloured by hand. Money/measurement sheets not used (good: "l" for litres). |
| 11 | No real photocopier test, no pupil trial | Open owner item. Add M2 as a reason for a real toner test of S1-18 and S2-01/S2-04 before printing. |
| 12 | The litre sign "ℓ" from a fallback font | Accepted: LiberationSans/Serif embedded in the PDF (checked with `pdffonts`); the sign renders as a curly "l", and S2-26 and S2-27 are the only pupil pages that print it. |
| 13 | Counted object sizes | Accepted: apples 9 mm, boats 9.7 mm, faces 10.5 mm, discs about 9 mm (measured), solids 17 mm or more. |
| 14 | "Checkpoint" commits mix files | Accepted. `git ls-files school/p2` is clean in the working tree (44 files, PDFs, validation report); the many modified extension and term files in `git status` are not P2's. |

## Syllabus check (item 3)

Read against pages 33 and 34 of the PDF (updated Oct 2025); the P3 pages (35, 36) read to find leakage.
- The 30 outcome lines in `p2_outcome_wording.md` match the PDF word for word. Each is practised by at least one page (verified from the key tags and the coverage tables in the front matter). Part-coverage (WN 1.3 writing words, ME 1.1 real instruments, GE 1.1 making patterns) is honestly listed in the plan.
- Page tags use the PDF's numbering. The one stale spot is L6.
- Nothing from P3 beyond **M3** (durations from start and end times) and **L4** (a division by 9). Checked and clear: tables only 2, 3, 4, 5, 10 (7, 6 and 9 appear only as the other factor, for example 2 x 7, 4 x 6); fractions with denominators up to 12, like and unit fractions only, no equivalence, no unlike fractions (S1-20 uses 1 - 1/12, within one whole); money in decimal notation with comparisons and conversion, no adding decimal money; length in metres only (cm is P1), mass kg/g, volume litres only (no ml, no km); no seconds, no 24-hour time; picture graph keys 2, 5, 10 (no bar graphs); 3D shapes five solids only; 2D shapes circle, triangle, rectangle, square. Numbers all within 1000.
- Whole-number tasks stay within three digits; the S1-11 stories are two-step, fine for P2.

## Front matter and owner decisions (item 5)

Read the cover, licence, teacher notes and key of both booklets (text and images).
- Annual licence ("This is an annual licence: it covers one school year and is renewable"): yes (decision LICENCE-ANNUAL).
- Publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers" on the cover: yes (PUBLISHER-OK). The footer copyright reads "Preciouslyours Pte Ltd" as confirmed.
- Registered office "66 Tannery Ln, Singapore 347805" on the licence page: yes. Contact pypteltd@gmail.com ("business email for now, to be changed later") on cover, licence, notes and key: yes.
- DRAFT stamps on cover, licence, teacher notes and the answer keys (the P1 audit's H3 about an unstamped key is fixed): yes. Puzzle pages carry no stamp (correct).
- No "MOE-aligned", SASMO, price, Mi or approval wording on any pupil page, cover, notes or key. The only MOE mention is the licence-page not-affiliated sentence, and the key's "Mathematics Syllabus, Primary (2021 edition, pages 33 and 34)" as a reference (not a claim). See L12 for the one wording question.
- School name: footer line "School (write name): ____ only" and the licence note agree (the P1 audit H3 about "set when the booklet is made" is fixed).
- Cover says "Almost every puzzle checks itself" (the P1 M7 fix); the notes say a blank box is invisible to the check.
- Teacher notes now say "Light crayons work best" and give the pencil-only route; the pupil page says "No crayon? Write Y, R, B, G or O." (P1 M8 fixed).
- Key pages print "KEY page n of N" (P1 L9 fixed).

## Photocopy and layout (item 4, 6, 7)

- All 8 PDFs: A4, pure black and white (colour scan of all pages: zero), no embedded images, fonts embedded (Fredoka, Nunito Sans, Liberation for the sign and the cent sign).
- Flat grey: none in any PDF (see L7). The raised key limit (90 to 130) is justified by the data; the "per page" label and the weak total-budget test are the only issues.
- 1-bit (150 dpi, thresholds 100 and 128): lines, boxes, ruler and clock ticks, dial ticks and litre hatching survive; weak spots are M1 and M2. Puzzle pages lose 11.7% to 14.2% of ink in the builder's test (limit 25%); front matter about 30% (limit 32%); keys 34.4% to 34.5% (limit 35%): borderline but they are small teacher print, viewed legible in 1-bit.
- Coin and note art: original, black and white, dashed ring; sizes in M1. The notes are drawn at about 21 x 14 mm and not true proportion (no SPECIMEN needed because they are not copies; MAS notes rules apply to reproductions). D1 stays open for the owner.
- Cube versus cuboid: see L11 and weak point 5. 5-measured objects 9 mm and above (weak point 13). Dials and clocks read accurately by angle. Scales: kg dials read to the unit tick, g dials to the 50 g tick; litre containers to the unit. All as the key states.

## What to fix, in order

1. H1: P2-39 eye/twin mark, the tail mark and mark positions; re-colour by hand once.
2. M1: "cents" on coins (S2-01, S2-04).
3. M2: hairline shading on S1-18.
4. M3: owner decision on duration pages; then edit S2-12, S2-13, S2-20 or note it in the plan.
5. M4, M5, L1 to L5, L8, L11: small page edits (box size, one instruction line, key notes).
6. L6, L7: documents and the validator label.
7. Owner items unchanged: licence wording (lawyer), compare coin and note art with real money, real photocopier test, pupil trial, L12, and whether fractions belong in Semester 1.

Nothing else found: no wrong key, no puzzle with two answers, no page that cannot be solved, every code word unique, no P3 topic beyond M3 and L4.
