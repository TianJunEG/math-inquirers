# Independent audit, round 2: Primary 4 early-finisher booklets (Semester 1 and Semester 2)

Auditor: independent (not the builder). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc` at `c9b72b9`. Nothing pushed, no PR, nothing edited except this report.
Subject: the PDFs in `school/p4/out` (Puzzles, FrontMatter, Answer_Key; the Complete_Pack files were not re-read). Round 1: `p4_semester_booklets_audit.md`. Baseline for the diff: the P4 PDFs at commit `d0ddbe6` (identical to `1477ad1`, the build audited in round 1). The syllabus PDF (Primary 4, pp. 37 to 40) was used as data only. I solved from the page images first and read the key after.

## Verdict

**Content-ready (the booklets stay DRAFT by the owner's rule: lawyer, real copier, pupil trial). No High, no wrong key, no page with two answers, no code word that another real word can replace.** All 22 pages that changed in substance were solved by hand from the image and agree with the key. One Medium (instruction sentences, P4-04 and the colour pages, a page-text edit, section 5) and a decision for the owner on code words repeated across levels (section 3). The round 1 fixes M1 to M7 are applied; M1 (echo of the extension unit L4U09) is reduced to a Low.

| Round 1 item | Round 2 state |
|---|---|
| M1 P4-37/38 echo L4U09 | Mostly fixed. Scenarios, labels, numbers are new. Same format remains (Low, section 4). |
| M2 four long sentences, V8 blind spot | Fixed. All four are 14 words or fewer; V8 now splits at . ? ! ; :. Instruction *sentence count* is still unmeasured (new M1 below). |
| M3 P4-19 arm over numbers | Fixed (section 2). |
| M4 colour boxes 8 mm | Now 13.9 x 10.9 mm (measured). Holds 4 digits; "20 000" is tight (section 6). |
| M5 syllabus pages | Fixed: both keys say "pages 37 to 40". |
| M6 teacher notes | Fixed (checked each one against the page, section 7). |
| M7 FM2.5, RS2.2 | Fixed: P4-09 pairs are 2 and 9, 2 and 7, 2 and 3; contents list says "(partly: the pupil only chooses the corner)". |

## 1. Which pages changed (text and pixel diff, PDF against PDF)

Method: PyMuPDF text per page and 100 dpi greyscale pixel difference (threshold 40) for all 6 PDFs, old against new. 36 of the 40 pupil pages changed. **Unchanged: P4-07, P4-13, P4-25, P4-29.** Front matter: only the pages named in section 7 changed (cover, licence, notes page 1, page 2, S1 page 4 and S1 page 5 are identical).

**Strip-only change** (check strip now two lines "Write the letters in / order. Do they spell a word?", 12 mm letter boxes; the only pixel difference is the strip at y 258 to 271 mm): P4-01, 02, 03, 06, 14, 15, 16, 17, 18, 21, 23, 24, 33, 39. I solved all of them again from the image in round 1 and their answers and words are unchanged; the key text for these pages is identical.

**Changed in substance** (22 pages; the strip change is also on most of them). My answer is from the image before the key.

| Page | What changed | My hand-solve from the image | Key | Notes |
|---|---|---|---|---|
| P4-04 Round It | New line "A number half way rounds up."; "Step only on true statements." | 11-box route (1,1),(1,2),(2,2),(3,2),(3,3),(3,4),(3,5),(4,5),(5,5),(5,4),(5,3); exhaustive search finds exactly one route, 11 boxes | agree | Half cases 21 455 (route) and 29 500 (route), 31 950, 12 445 now settled by the sentence. 6 instruction sentences (M1). |
| P4-05 Colour the Bus | All parts new; boxes 13.9 x 10.9 mm | 400 yellow 4, 3000 red 3, 4500 blue 3, 7000 green 3, 20 000 orange 3; the six small marks agree with the strip | agree | "Round 19 950 to nearest 100" is a half case, the rule is printed on P4-04 only (Low). |
| P4-08 Common Factors | Item 6 now "Pick the common factor of 28 and 98 between 2 and 14." | 11, 4, 12, 15, 8, 7 = FROZEN | agree | "between" leaves 2 and 14 open, but neither is in the code table (Low). |
| P4-09 Number Riddles | All six clues new, common multiples of 2 and 9, 2 and 7, 2 and 3 | 54 P, 80 E, 98 A, 43 N, 48 U, 186 T = PEANUT; each riddle has one answer by search | agree | Single numbers "9." "7." "3." wrap alone onto a line (Low). |
| P4-10 Long Multiplication | Space between the rule and the answer box (about 10 mm) | 26 145 F, 14 319 R, 18 234 U, 20 727 I, 11 753 T, 13 580 Y = FRUITY | agree | Space is small for items 4 to 6 (Low). |
| P4-11 Colour the Lorry | All parts new | 1260 yellow 3, 1680 red 4, 2520 blue 3, 3360 green 2, 5040 orange 3; marks agree | agree | Two marks (star and plus) are both red: fine, the strip says same mark means same colour, not the converse. |
| P4-12 Division | Taller cards | 2086 S, 685 H, 1 R, 314 I, 354 M, 824 P = SHRIMP | agree | Cards about 25 mm tall: still little room for long division (Low). |
| P4-19 Protractor | Numbers every 20 degrees (inner 80 and 100 added), arm 0.7 mm, angles 30 to 150, new table | 130 (base left), 70 (base left), 110 (base right), 90, 50, 30 (base left): F A M I L Y | agree | Section 2. |
| P4-20 Fraction Stories | Item 4 and item 5 reworded | 18 P, 10 O, 150 L, 20 I, 32 C, 12 E = POLICE | agree | Item 5 is exactly 14 words. |
| P4-22 Order the Decimals | Now 1 star | Set A W I Z (0.22, 0.582, 0.8); Set B A R D (4.9, 4.89, 4.797) = WIZARD | agree | Star changed in the page, key, contents (S2 10 and 10). |
| P4-26 Decimal Shares | Items 1, 2, 4, 5, 6 new numbers; item 4 now shared ribbon | 23.52 T, 2.46 U, 3.625 R, 2.82 K, 6.25 E, 2.1 Y = TURKEY | agree | |
| P4-27 Missing Sides | "perimeter" label on 2 lines | 5 F, 16 R, 13 I, 12 D, 7 G, 6 E = FRIDGE | agree | No label touches a border now. |
| P4-28 L-Shapes | Figures moved down (label collision) | 74 W, 42 A, 64 L, 48 N, 34 U, 55 T = WALNUT | agree | The two stacked "6 cm" labels on the T (item 2) are both 6, harmless. |
| P4-30 Joined Shapes | Items 1 to 6 reframed (4 squares in a row, card with corner cut, pool tiles, two cards) | 400 B, 64 O, 32 T, 156 A, 40 N, 48 Y = BOTANY | agree | Item 5 still has a unique answer (join along the long sides = 10 by 10). |
| P4-31 Shape Facts | New word | D, E, V, O, U, R = DEVOUR | agree | |
| P4-32 Complete the Corner | Letters enlarged (10 pt), new decoys | B, O, U, N, T, Y: corners read from the dot positions; item 6 vectors (2,1) and (-1,2) checked | agree | BOUNTY. |
| P4-34 Complete the Figure | Grid 0.4 mm; new figures | Fig 1 shaded left side 20, so 40 C; row 5 gives 2 A; column 6 mirrors column 5, 6 N; Fig 2 upper part 17, so 34 O; column 3: 2 up, so 4 P; row 10 mirrors row 1, 1 Y = CANOPY | agree | |
| P4-35 Name the Solid | New word | F, A, T, H, O, M (square pyramid, cylinder, cube, cone, cuboid, triangular prism) = FATHOM | agree | Cube versus cuboid is the usual oblique-drawing convention (round 1 L11, unchanged). |
| P4-36 Which Net? | Nets at one line weight; new word | pyramid C, triangular prism A, 2x2 block so no solid M, cuboid P (unequal strip), cube U, cube S (cube nets folded in a script: item 5 yes, item 6 yes, item 3 no) = CAMPUS | agree | |
| P4-37 Stickers won by three teams | New table, 2 stars | Red Wk2 11 C, Red Wk3 13 O, Blue Wk1 12 U, Blue total 32 S, Total Wk1 33 I, Total Wk3 37 N; column and row sums close (33, 23, 37 = 93) = COUSIN | agree | Solution is unique; chain is four steps, two stars is right. |
| P4-38 Swimming club graph | New graph | Jan 15, Feb 15, Mar 40, Apr 10, May 20, Jun 50; answers 20 F, 15 L, 10 I, 30 G, 65 H, 40 T = FLIGHT | agree | Points are on the dashed half lines. |
| P4-40 Colour the Ferry | Boxes 13.9 x 10.9 mm; parts new | 0.6 yellow 4, 1.25 red 2, 2.4 blue 2, 3.05 green 2, 5 orange 2; marks agree | agree | |

Answer-key diff (the `Answers:` lines, the code words and the teacher notes of every changed page) agrees with my solves line by line. `validate.py` run: not re-run by me; `validation_report.txt` says 735 checks, 0 failed (I counted 735 PASS, 0 FAIL).

## 2. P4-19 protractor, in detail

- Reading: I read all six arms from the image (and again at 300 dpi crops): each arm lies exactly on an unlabelled 10 degree tick halfway between two printed numbers (the printed numbers are 20 apart on both scales), so the pupil must count one tick from a printed number or read the half-way tick. 130 and 50 (item 1), 70 and 110 (items 2, 3), 90 (item 4), 50 (item 5), 30 (item 6) are all read correctly.
- Arm against numbers: **no arm lies over a printed number.** The arm passes between "60" and "80" (inner) in items 2 and 3 and between the inner "120" and "140" in items 1 and 5, with under 1 mm of clearance at 300 dpi (the arm nearly touches the edge of the inner "120"/"140" in items 1 and 5; Low). At 150 dpi 1-bit the arms and all numbers stay separate.
- Decoys: the table is 30, 50, 70, 90, 110, 120, 130, 140. The wrong-scale reading is in the table for items 1, 2, 3, 5 (50 for 130, 110 for 70, 70 for 110, 130 for 50) and 120 and 140 catch an off-by-one-tick slip on 110 and 130. Item 4 (90) has no wrong scale; item 6's wrong-scale value (150) is not in the table, so a pupil who reads the wrong scale finds no match and learns it. Reasonable, as in round 1.
- Item 6 and item 1: which base arm is used (left or right) decides the scale; the instruction "Start at 0 on the arm along the base" covers it.
- Key note now says "10 degrees from the nearest printed number and never over one": true.

## 3. Code words

Dictionaries (mine): `english_words` web2 (17 468 six-letter words) and gcide (11 122), `wordfreq` top 100 000 (13 808) and top 500 000 (45 651); "strict" = on wordfreq 100 000 and web2 or gcide (5 829 words). All 33 intended words are on the strict list (FRIDGE is on gcide and both wordfreq lists, not web2).

Tests, for each of the 33 pages with a word (the 20 code-table pages and the lettered, matching and ordering pages):
- All 719 rearrangements of the six letters: **no other word on any list**, except the name MARCEY (CREAMY, top 500 000 only).
- Single slip (one answer replaced by any letter printed on that page): **no hit** on web2, gcide or wordfreq 100 000 on any page. Only wider-list oddities: FAMILI, BOTANA, STUDII, FABRIS, WALRAS, LATHOM, CRATTY, CREARY, KOBALT, WAMPUS, KAMPUS (none is a natural word).
- Lettered-choice pages P4-31, 32, 35, 36 (also done with the actual row choices): every other way of choosing (63, 728, 728, 728 combinations): no word on any list. P4-36 CAMPUS, P4-32 BOUNTY, P4-35 FATHOM, P4-31 DEVOUR are safe. (With any letter of the whole page allowed, DEVOUR to DETOUR or DEVOUT, BOUNTY to COUNTY or BOUNCY and WOMBAT to COMBAT appear, but those letters are not offered in that row.)
- Two wrong answers at once (information only, strict list): CREAMY to CREEPY, POLICE to ELLICE, FRIDGE to DREDGE/DRUDGE/GRUDGE, WALRUS to GALLUS, TURKEY to TURRET, TEACUP to TEAGUE, WIZARD to IZZARD, COBALT to TYBALT, WOMBAT to TOMCAT, FATHOM to FANDOM/HATHOR, FABRIC to FIBRIN/RUBRIC, CURFEW to CURLED/CURLER/CURSED/SURFER, DEVOUR to DEVOTE. The teacher notes say this is possible and rare. The new words TURKEY, BOTANY, CANOPY, FAMILY, COUSIN, FLIGHT have none (TURKEY has TURRET as a two-slip word).
- No word repeats inside the two booklets (33 different words).

**Across levels (new Low or owner decision): not distinct.** From the Answer_Key PDFs of all six levels: P4 words also used at P1: 6 (COUSIN, DONKEY, FAMILY, PEANUT, SHADOW, TURKEY); at P2: 18 (BACKUP, BANDIT, BOTANY, CAMPUS, COBALT, CREAMY, CURFEW, DONKEY, FAMILY, FATHOM, FIGURE, FROZEN, FRUITY, HUNGRY, PEANUT, SHADOW, TEACUP, WIZARD); at P3: 11 (BANDIT, CANOPY, DEVOUR, DONKEY, FIGURE, FLIGHT, FRUITY, POLICE, SHRIMP, WALNUT, WOMBAT); at P5: 0; at P6: 26 of 33. The builder reseeded to avoid repeats inside one booklet only. A school that buys two levels meets the same word on different pages, which does no harm to a pupil but makes the books look like one pool of words, and 26 of 33 shared with P6 is a lot. P6 PDFs have uncommitted changes in the working tree (git status), so the P6 count may move. "Where feasible": P5 shows it is feasible. Decision for the owner; I would not block content on it.

## 4. Echo of our own content: P4-37 and P4-38 against extension/data/l4_*.json and p4/content/*.js

I opened `extension/data/l4_u09.json` and searched all ten `l4_*.json` and all `p4/content/l*.js` (my own check, not the builder's).
- **P4-37 stickers table.** Not an echo of numbers, labels or story (no "sticker", "Red", "Blue", "Green", "team" table in any file). Remaining shared design with L4U09-S03 ("Fill in the 6 empty boxes. Go row by row.", head Week 1, Week 2, Total, rows plus Total row, six boxes): the P4 page has Week 1 to Week 3, three rows, a Total row and column, six boxes and the instruction "row by row". This is the generic syllabus item (completing a table from totals), different scenario and numbers. **Low** (was Medium).
- **P4-38 swimming graph.** No "swim", "club", "joined" in the line graphs. Shares only the month labels starting at Jan (L4U09-S06 has Jan to Apr, 4 points; P4-38 has Jan to Jun) and the question frame "From X to Y went up by". Values (15, 15, 40, 10, 20, 50) and the half-line reading are different from S01 (30, 45, 25, 60, 55, 95). **Low.**
- Other new framings: P4-20 item 4 (cards in a pile), P4-26 item 4 (shared ribbon), P4-30 items 1 to 4 (4 squares in a row, card with corner cut, 4 small squares, pool tiles): no matching text in the own content. **P4-30 item 5** ("two 10 cm by 5 cm cards joined along their long sides, find the perimeter") is still the frame of `l4_u07.json` ("two identical rectangles 8 cm by 3 cm joined along a whole side", perimeter for each way). Low (new numbers, one way only).
- P4-18 "a", P4-09 clue frames "I am a multiple of ...", P4-19 "Start at 0 on the arm along the base", P4-34 shading the mirror half and counting: generic frames; same view as round 1.

## 5. Reading load against the plan table (P4: 14 words a sentence, 4 instruction sentences)

- **Sentence length.** I split the text of all 40 pupil pages at . ? ! ; : (a fraction as one word) and checked every question and clue sentence: none over 14. The four round 1 sentences: P4-08 item 6 (12 words), P4-20 item 5 (14), P4-30 item 5 (13 plus "Find the perimeter"), P4-38 item 6 ("How many more joined in the busiest month than the quietest?", 11). P4-37 instruction: four sentences.
- **M1 (new, Medium): instruction sentence count.** The validator counts lines (`len(p["instr"])`), not sentences. Counting sentences in the printed instruction block: **P4-04 has 6** (it had 5 in round 1; the new "A number half way rounds up." made it 6: "Each box says: number, about, rounded number. Start at START. Move up, down, left or right. Step only on true statements. A number half way rounds up. Do not step on a box twice."), and **P4-05, 11, 40 have 5** (the colour pages: "Work out the answer in each part. Find it in the key. Colour the part. No crayon? Write Y, R, B, G or O."). Table limit is 4. Round 1 wrongly said all were three. Suggest for P4-04: "Start at START. Move up, down, left or right. Step on true statements only. Half way rounds up." (4) and make V8 count sentences. The colour pages are the same text as P2 and P3 and are accepted there; keep as is if the owner agrees, or join to "Colour the part (no crayon? write Y, R, B, G or O)".
- P4-12, 17, 22, 08, 30, 37 have exactly 4. P4-02, 15, 25, 27 and others have 3.

## 6. 1-bit legibility, changed pages

Vector check on all 40 pupil pages: only black (0,0,0) and white; no images; no flat grey; no text colour other than black (white text only inside black START/FINISH labels on P4-04, P4-07); lowest stroke 0.24 mm (borders); smallest text 8 pt (the footer, as in round 1). 1-bit renders (300 dpi grey, area-averaged to 100 dpi and 150 dpi, threshold 50%), viewed whole at 100 dpi (P4-05, 32, 34, 36, 38) and at 150 dpi (P4-19, P4-34 grid):
- P4-19: arms, tick marks, inner and outer numbers all separate at 150 dpi; legible at 100 dpi.
- P4-32: dots and the 10 pt circled letters legible at 100 dpi; footer text breaks up (known, Low).
- P4-34: the 0.4 mm grid is complete at 150 dpi; at 100 dpi some rows are thin and uneven (anti-aliasing). Count squares survive.
- P4-36: the nets, one weight; cube nets clear.
- P4-38: dashed half lines survive at 100 dpi, faint (as round 1).
- P4-05, 11, 40: boxes, circles and marks clear. **Boxes measure 13.9 x 10.9 mm** (PDF drawing). They hold 4 digit values and decimals (5040, 3360, 1.25, 3.05). **"20 000" (P4-05, three boxes) is tight:** 6 characters in 13.9 mm is about 2.3 mm a character; a Primary 4 hand will run to the edge or write smaller. The box is below the 12 mm height rule by 1.1 mm; the colour pages are not in the V8 12 mm check. Severity Low: the colour pages ask for working out and colouring; the pupil can write Y, R, B, G, O. If you want to touch it, make the P4-05 boxes about 17 mm wide.
- Check strip letter boxes: 11.4 x 11.6 mm centre-line (about 12 mm outer); satisfied, borderline.

## 7. Front matter and keys

- Cover, licence, notes page 1 and 2, S1 contents page: unchanged. **Changed:** S1 notes page (loop bullet now "Following the arrows round the ring, the last arrow must bring the pupil back to the start number", true for P4-13), S2 notes page (totals bullet now "magic square, the table with totals", true for P4-25 and P4-37), S2 contents (P4-22 1 star, P4-37 2 stars; 10 and 10 in each booklet from the verification file; RS2.2 "(partly: the pupil only chooses the corner)"). Keys: both cite pages 37 to 40; P4-15, P4-19 (no longer wrong), P4-33 and P4-38 and P4-39 ("dashed") notes now match the pages (checked each against the image).
- "Not affiliated with ... Ministry of Education" still once, on the cover; no other wording about the Ministry; DRAFT on cover, licence, notes, keys and none on pupil pages (not re-read in full; PDF text diff shows no other change).

## 8. Remaining items

| # | Item | Severity |
|---|---|---|
| M1 | P4-04 prints 6 instruction sentences and the colour pages 5 (limit 4); validator counts lines | Medium (page text, 5 minutes) |
| O1 | Code words are shared across levels (26 of 33 with P6, 18 with P2, 11 with P3, 6 with P1, none with P5) | Low, owner decision |
| L1 | P4-37 and P4-38 keep the format of L4U09 (Week columns, "row by row", Jan-start months); P4-30 item 5 keeps the l4_u07 frame | Low |
| L2 | P4-05 "20 000" in a 13.9 x 10.9 mm box; colour boxes 1.1 mm under 12 mm | Low |
| L3 | P4-18 items 5 and 6: the letter a sits off-centre above one arc spanning three arms. I judge it **Low, accept**: the arc is one arc over all three arms, the page says "angle a is the marked angle", the three names are different and the only name that spans the outer arms is the right one | Low |
| L4 | P4-09, P4-19, P4-34 own-content frames ("I am a multiple of...", "Start at 0 on the arm along the base", mirror shading and counting): generic, new numbers. **Low, accept.** | Low |
| L5 | P4-10 and P4-12: about 10 mm (P4-10) and 25 mm cards (P4-12) of working space; items 4 to 6 on P4-10 need two partial products and a sum | Low |
| L6 | P4-05 "Round 19 950 to nearest 100" and P4-04 half cases: the rule "half way rounds up" is printed only on P4-04 | Low |
| L7 | P4-08 item 6 "between 2 and 14" (ends open, but not in the table); P4-09 single numbers wrap alone onto a line; P4-28 two stacked "6 cm" | Low |
| L8 | P4-19: arms nearly touch the inner "120"/"140" labels (items 1, 5); wrong-scale value 150 absent for item 6 | Low |
| L9 | P4-34 grid uneven at 100 dpi 1-bit (complete at 150 dpi); footer 8 pt breaks up at 100 dpi | Low |
| L10 | Two-wrong-answers-at-once words (section 3, strict list), as stated in the notes | Information |

## 9. What I could not check

A real copier and real pupils; the lawyer and licence; whether a Primary 4 child can read the inner scale on P4-19 or the half-way tick (a trial of P4-19, P4-34 and P4-36 is still worth doing); the Complete_Pack PDFs (assumed to be the concatenation of the files read); I did not re-run `validate.py`. Similarity is lexical plus my reading of the own-content items; the private source folders were not re-scanned this round (round 1 found no private overlap, and the changed pages use new numbers).
