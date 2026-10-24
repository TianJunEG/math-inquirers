# Second independent audit: Primary 1 early-finisher puzzle pilot (school/p1, after the fix pass)

Audited 23 Oct 2026, branch `claude/great-fermi-1hv4vc`, committed outputs `out/P1_Complete_Pack.pdf` (25 pages) and `out/P1_Answer_Key.pdf` (10 pages). Audit only: no pack file was changed (all scripts ran on a scratch copy; scratch files are not committed).

Method: every page rendered with `pdftoppm` at 80 dpi (colour), at 150 dpi grey and converted to 1-bit at 150 dpi, and read as a P1 pupil, as a teacher with 30 pupils and as a Singapore P1 teacher. The 20 pupil pages were checked for colour pixels (0 on all 25 pack pages). Every puzzle was solved from the printed page, not from the generator (by hand, then by brute force for the logic pages, magic square and maze; the rulers were measured in pixels; the clocks were read from the hand angles). Self-checks were attacked by script with a real English word list (150 000 words, not the 400-word list in `gen/common.py`): every single-letter slip, every two-letter slip and every swap on the eight code-word pages, every wrong arrangement on the logic and ordering pages, every swap and two-part slip on the three colour pages, and every wrong set of counts on the graph page. A pack was also built with a 68-character school name to test the footer. `validate.py` was re-run on a copy: 322 checks, 0 failed (matches the README). Checked against `README.md`, `AUDIT.md`, `AUDIT_FIXES.md`, `docs/school_books/plan.md`, `docs/terms/owner_decisions.md` (addenda 5 to 10, 23 Oct entries), `docs/moe/syllabus_by_level.md`, `docs/books/p1_school_paper_patterns.md` and `term/l1/WORDING_GUIDE.md`.

## 1. Verdict

**Close to ready for a pilot; not yet ready to send to a school.** The first audit's serious faults are really fixed: all 20 pages have one correct solution that matches the key, the logic grids now reject 119 of 119 wrong arrangements, the division sign and the circular check are gone, the black-and-white print is clean (no grey, no colour, lines at least 0.57 pt), no Mi, no price and no affiliation wording appears on any pupil page, money uses 50¢, and the three colour pages tally correctly (I re-derived every part). What remains is of a different kind. (1) The "Check it" hints name the answer ("It crosses a river" for BRIDGE, "You live in it" for HOUSE), so on 14 pages a bright child can guess the word and read the answers off the code table without doing the puzzle, which defeats the practice the product sells; this is worst on the two logic grids. (2) Several statements on the pages and in the key are false or unusable: the rocket's "two sides match" rule fails for the two round parts, the house check refers to "the two windows" that the picture does not show, the key describes clue types that are not on P1-04 and P1-07, and the P1-18 note claims half-hour additions that cross the hour when none do. (3) P1-20's check never tests the two questions the pupil answers, and the "more/fewer" slip passes it. (4) P1-16 has no worked example of the grid although the fix log says it has. (5) P1-18 reads 5-minute clocks on three of five items, against the o'clock/half past rule, and the pack has no one-star time page. (6) The placeholders on the cover, licence and notes pages are not marked as placeholders. None of these needs new puzzle design; all are one-line or one-page edits. After items 1 to 6 and the tier fix for P1-07 the pack is a sound pilot.

| Verdict | Pages |
|---|---|
| Ready | P1-02, P1-03, P1-05, P1-08, P1-10, P1-13, P1-14, P1-15, P1-17, P1-19 |
| Minor fixes | P1-01, P1-04, P1-06, P1-07, P1-09, P1-11, P1-12, P1-16, P1-18, P1-20 |
| Rework | none |

Findings: 1 High, 8 Medium, 13 Low (22 new). First-audit findings: 20 fixed, 6 partly fixed, 2 not fixed (section 3).

## 2. Page table (independent solution, checks attacked, score out of 10)

Score = pupil clarity, self-check strength, syllabus fit, print legibility together. "Slips" = my own enumeration with a real word list.

| Page | Tier | My solution (matches key) | Unique? | Self-check test | Verdict | Score |
|---|---|---|---|---|---|---|
| P1-01 Colour the Rocket | 1 | 15 parts: 1 yellow x2, 2 red x2, 3 blue x3, 4 green x4, 5 orange x4 (re-derived part by part) | yes | Tally rejects all 150 single slips; two-part slips pass 8 of 1680 (0.5%). The "mirror" rule is wrong for the two round parts (F-new 3) | Minor fixes | 7 |
| P1-02 Mystery Numbers | 2 | 66, 85, 36, 56, 26 = CLOUD | yes (each riddle one number, every clue needed) | 0 of 45 single slips and 1 of 810 two-letter slips make a real word (FLOOD) | Ready | 8 |
| P1-03 Number Cards | 1 | 22 B, 43 R, 71 I, 78 D, 80 G, 85 E = BRIDGE | yes | No other order of the six letters is a word (719 of 719); hint gives the word away (F-new 1) | Ready | 7.5 |
| P1-04 Sticker Grid | 2 | Ben 12, Siti 23, Ali 63, Mei 78, Kumar 99; HOUSE | yes (1 of 120) | 119 of 119 wrong arrangements rejected (no anagram of HOUSE); but the page can be solved from the hint without clues (F-new 1); key note wrong (F-new 6) | Minor fixes | 6.5 |
| P1-05 Missing Numbers | 1 | 40, 15, 42, 30, 29, 11 = FLOWER | yes | 0 of 60 single, 0 of 1500 two-letter slips pass | Ready | 8.5 |
| P1-06 Shape Riddles | 2 | J square, A half circle, C triangle, K quarter circle, E circle, T rectangle = JACKET | yes | No anagram of JACKET; every single slip gives a non-word | Minor fixes (tier light) | 7 |
| P1-07 The Queue | 2 | Jenny, Aisha, Ali, Ravi, Lily = TIGER | yes (four direct clues, Ravi by elimination) | 119 of 119 wrong orders rejected | Minor fixes (tier, key note) | 6 |
| P1-08 Make Twelve | 1 | (3,5) 8+4, (2,5), (2,4), (2,3), (3,3), (4,3), (5,3), (5,2), (5,1), (4,1) = 10 boxes (row, column from 1) | yes (one simple route; 13 boxes make 12, 3 are dead ends) | Route must end at FINISH, 10 boxes, every box 12: shortest shortcut ignoring the rule is 6 boxes, so rejected | Ready | 8.5 |
| P1-09 Magic Square | 2 | 4 9 2 / 3 5 7 / 8 1 6 | yes, also with repeats allowed (9^6) and with rows and columns only | The eight totals are the constraint itself: strongest check in the pack | Minor fixes | 7.5 |
| P1-10 Take Away Code | 1 | 8, 5, 11, 6, 4, 3 = CASTLE | yes | 1 of 60 single slips makes a real word: answering 6 for 17 - 6 gives CATTLE (only the hint rejects it) | Ready | 8 |
| P1-11 Shape Sums | 2 | circle 4, square 9, triangle 3; star 6, diamond 2, five-sided 7 = SPRING | yes | 0 of 48 single slips pass; WIRING after two slips (1 of 960) | Minor fixes | 7 |
| P1-12 Colour the House | 1 | 17 parts: yellow 3, red 4, blue 4, green 3, orange 3 (re-derived); exactly 2 of the 6 wall/window parts red | yes | 204 of 204 single slips rejected; swaps of two parts pass 37 of 115, two-part slips 1.7%; "two windows" cannot be found (F-new 4) | Minor fixes | 6.5 |
| P1-13 Equal Groups | 1 | 2x5=10, 5x5=25, 3x6=18, 3x8=24, 2x8=16, 5x4=20 = PLANET | yes | 0 of 60 single, 0 of 1500 two-letter slips pass | Ready | 8 |
| P1-14 Colour the Ice Cream | 2 | 12 parts: yellow 2, red 2, blue 4, green 2, orange 2 (re-derived); every mirror pair matches | yes | 1200 of 1200 slips rejected; 0 swaps and 0 two-part slips pass | Ready | 8 |
| P1-15 Coin Purses | 1 | 80, 60, 40, 25, 95 = PIANO | yes | 0 of 45 single slips; DIANA after two slips (1 of 810) | Ready | 8.5 |
| P1-16 Shop Prices | 2 | pen $12 B, book $15 A, ball $5 S, kite $8 K, cup $7 E; ball + pen $17 T = BASKET | yes (1 of 120) | 119 of 119 wrong arrangements rejected; wrong total gives a non-word; no worked example on the page (F-new 5); hint gives the word away | Minor fixes | 6.5 |
| P1-17 How Long? | 1 | 4, 5, 10, 2, 8, 6 cm = PENCIL (strip ends measured at 59.2 px per cm at 150 dpi) | yes | 0 of 54 single, 0 of 1215 two-letter slips pass | Ready | 8 |
| P1-18 Clock Time | 2 | 8:10 -> 9:10 T; 1:25 -> 1:55 I; 1:30 -> 2:30 M; 11:25 -> 11:55 E; 11:00 -> 12:00 R = TIMER (hand angles read) | yes | Every wrong time is a non-word; 5-minute reading against the o'clock/half past rule (F-new 7) | Minor fixes | 6.5 |
| P1-19 Shape Count | 1 | rectangles 5, triangles 4, circles 2, half circle 1, quarter circles 3 (total 15) = SHAPE | yes | Total plus word; swapping the rectangle and half-circle counts gives PHASE and still totals 15 (Low) | Ready | 8 |
| P1-20 Fruit Graph | 2 | Apple 4, Banana 4, Orange 8, Grape 5, Pear 3; a) Orange; b) 5 | yes | Total 24 rejects every single slip, but a) and b) are not checked and a more/fewer reversal passes (F-new 2) | Minor fixes | 6 |

## 3. Status of every first-audit finding

| # | First-audit finding | Status | Evidence now |
|---|---|---|---|
| F1 | P1-04 and P1-16 check passed 120 of 120 | Fixed | Letter beside each number or price. Brute force: only the correct arrangement spells HOUSE or BASKET; no other arrangement of those letters is a word. New weakness: the hints (F-new 1) |
| F2 | P1-12 and P1-14 slip detection 72 to 76% | Fixed | Pages replaced by colour-by-code; 100% single-slip rejection; my swap and two-part-slip tests pass 0.5%, 1.7% and 0% |
| F3 | ÷ sign on P1-14 | Fixed | No ÷ in the pack PDFs or the key |
| F4 | P1-20 circular check | Fixed | Three difference clues fix every row; total 24 appears only in the check. (A new gap: F-new 2) |
| F5 | No logic-grid how-to | Partly fixed | P1-04 has the Zed/Yan cross-and-tick box. P1-16 has the same four instruction lines but no example box, although `AUDIT_FIXES.md` says both pages carry one (F-new 5) |
| F6 | Tier labels not honest | Partly fixed | P1-19 now one star (right). P1-06 is now the shape-riddle page. P1-07 was moved to two stars, but it is the easiest logic page (four direct clues): wrong the other way (F-new 8). P1-08 (25 sums) stays one star |
| F7 | Key states wrong facts | Partly fixed | The listed errors are gone ($3 more, decoy lists, P1-08 box values 8, 10, 11, 13, 14, 16 all correct). New wrong statements of the same kind: P1-04, P1-05, P1-07, P1-18 (F-new 6) |
| F8 | P1-01 rods | Fixed | Page replaced by the Rocket |
| F9 | P1-03 labels | Fixed | Rows labelled "number" and "letter" at the left, boxes aligned |
| F10 | Strand balance | Partly fixed | Shapes 3 pages, add/subtract 4; but multiplication fell to one page and whole numbers is still 7 of 20 (F-new 12) |
| F11 | "80c" in key | Fixed | Key and pages use ¢ throughout; no `\d+c` in any text |
| F12 | P1-02 layout | Fixed | Each clue is its own line; no stranded "6." |
| F13 | P1-09 words and boxes | Fixed | "across" and "down"; total boxes 13.5 x 11.9 mm measured, on the 12 mm limit |
| F14 | P1-06 labels | Fixed | Page replaced; START and FINISH on P1-08 sit inside their boxes |
| F15 | P1-13 labels | Fixed | Boxes labelled bags, dots, total |
| F16 | P1-17 print | Fixed | Numerals below the ruler border, 1 mm ticks half height, "print at 100%" in notes and key |
| F17 | P1-18 hands and wording | Fixed | Hands at least 25 degrees apart (read from the angles), "What is the time 1 hour later?" |
| F18 | Key thumbnails | Partly fixed | Small solved pictures on 8 of 20 entries (the picture, grid and route pages), text only on the other 12; three full answer pages for the colour pages. `AUDIT_FIXES.md` says "on each entry": overclaim. Pages are fuller (last entry page is about 45% used) |
| F19 | Teacher notes thin | Fixed | Time, when to use, if the check fails, stars and photocopying all present. The "when to use" list is inconsistent (F-new 17) |
| F20 | Wording | Fixed | "Arrange the numbers in order", "Find the missing number", "more ... than" frames |
| F21 | P1-07 empty half | Partly fixed | Boxes now fill the left 60%; the right 35% beside the queue is still empty |
| F22 | Workload | Fixed | 36-sum page gone; P1-14 has 12 parts; stated times in notes |
| F23 | Front-matter placeholders | **Not fixed** | Text unchanged and not marked as draft anywhere (F-new 9) |
| F24 | Alignment wording | Fixed | Key says "references are for your planning only and are not printed on the pupil pages"; the "tell pupils" sentence is gone; none on pupil pages |
| F25 | Mazes passable by breaking the rule | Fixed | Check counts boxes (10) and every box must make 12; shortest shortcut ignoring the rule is 6 boxes |
| F26 | Key jargon | Fixed | No K-codes, "script", "tri" or "pent" in the key; "five-sided shape" |
| F27 | Odd prices | Fixed | $5, $7, $8, $12, $15 (a $12 pen is still a little odd; Low) |
| F28 | Outcome numbers unverified | **Not fixed** | README still lists it as open; `validate.py` only tests that each number is inside the P1 range, not that the number is the right outcome |

## 4. New findings

Severity: High = the pupil's practice or check is defeated, content unsuitable for P1, or an owner rule broken; Medium = a real classroom or teacher problem to fix before a pilot; Low = polish.

### High

**F-new 1. The check-strip hints give away the code word, so the puzzle can be bypassed on 14 pages.** Location: check strips of P1-02 ("Is it in the sky?"), P1-03 ("It crosses a river"), P1-04 ("You live in it"), P1-05 ("garden plant"), P1-06 ("You can wear it"), P1-07 ("an animal"), P1-10 ("where a king lives"), P1-11 ("a season"), P1-13 ("in space"), P1-15 ("a music maker"), P1-16 ("You carry shopping in it"), P1-17 ("used for writing"), P1-18, and the letter-count boxes. Evidence: on P1-04 the pupil writes HOUSE in the five boxes and reads off Ali H = 63, Mei O = 78, Siti U = 23, Ben S = 12, Kumar E = 99 from the chips, without reading one clue. P1-03: BRIDGE gives the order 22, 43, 71, 78, 80, 85 from the card letters. P1-16: BASKET gives the five prices and the code table gives the total letter T. On the code-breaker pages the code table contains only the answer letters plus four or five decoy letters, so a guessed word is confirmed at once. This breaks plan rule SC-2 ("reveal a wrong answer without revealing the right one") and plan test V4 (guess resistance), neither of which `validate.py` runs; the 100% rejection figures measure slips, not guessing. For a pupil who finishes early this removes the practice; the teacher would see correct pages from a child who did no sums. Fix: drop the category hint on every page (the strip already says "Do they spell a word?"), or keep a hint only on pages where the answers are computed from many numbers (P1-13, P1-15), never on the logic and ordering pages; add V4 to `validate.py` (a dictionary guess from the letter count and the hint must leave more than one candidate).

### Medium

**F-new 2. P1-20: the check does not test the two questions the pupil answers, and a more/fewer reversal passes it.** Evidence: the strip says only "Count all the circles. Is the total 24?". A pupil with the right graph who writes b) 4 instead of 5, or a) Grape, is told nothing. Also Grape = Banana + 1 and Pear = Banana - 1 are symmetric, so a pupil who reverses "more" and "fewer" on both clues draws Grape 3 and Pear 5: total 4 + 4 + 8 + 3 + 5 = 24, still passes. All 5 wrong permutations of the three drawn counts (8, 5, 3) also total 24. `validate.py` counts only slips in the drawn counts (23 of 23). The teacher note "a pupil who misreads a clue gets a different total" is therefore not always true. Fix: change one clue so the two sides are not symmetric ("Pear has 2 fewer than Banana") and add a check that covers a) and b) (for example print a small code table for the answers to a) and b), or ask for a total of the two answers that must equal a printed number).

**F-new 3. P1-01: the "mirror" rule is false for the two round parts.** Location: check strip "parts that mirror each other have the same colour", key note and full answer page. Evidence: the planet and moon circles sit symmetrically at the left and right of the rocket, but their questions give 1 (yellow, 50 + 1 = 51) and 3 (blue, 43 = 4 tens 3 ones); the key's own thumbnail shows Y and B. In the picture code they are not a mirror pair (only the wings, nose, top, mid, base halves are). A pupil with a correct page is told two parts must match, recolours one, and breaks the tally; a teacher spot-checking sees the contradiction. Fix: add a clause to the page ("not the round parts at the sides"), or change the two circle questions so both have the same answer, or drop the circles from the symmetry text.

**F-new 4. P1-12: the check refers to "the two windows", which the picture does not show, and the answer boxes are inconsistent.** Evidence: the strip says "One colour each: the two sides of the roof; the two windows; both tree top parts." The house has no window panes: the only way to know which two parts are windows is the generator (the left and right top wall parts, both red). A pupil may choose the middle part (8, orange) and conclude the page is wrong. Four parts (sun, roof top, bottom-left wall, upper tree top) print "Corners?" with no box to write in, others print a 3.4 mm box (too small for a child to write a number in) and others a "Corners: []" label. Fix: draw a cross-bar in the two window parts (and a knob is already on the door), or say "the two top side parts"; use one label style with a box of at least 8 mm.

**F-new 5. P1-16 has no worked example of the logic grid, although the fix log says it does.** Evidence: `AUDIT_FIXES.md` F5: "P1-04 and P1-16 carry a printed cross-and-tick example box". The rendered P1-16 shows the instructions "Cross a box if a clue says no. Tick a box if it must be yes." and nothing else; `howto_grid()` is called only from the P1-04 builder (`gen/pages_numbers.py` line 176). A teacher who hands out P1-16 alone (the product's rule: every page standalone) gives a 6-year-old a grid with no example. Fix: add the same small box to P1-16 (there is room beside the clues).

**F-new 6. Key notes still state things that are not on the page (the first audit's F7, regenerated by hand-typed text).** Evidence: P1-04 note "Clues use more than, fewer than, greatest, smallest, second greatest": the four clues use only "fewer than" and "more than". P1-07 note "Clues use ordinal numbers, in front of, behind and next to": the clues are "2nd", "3rd", "last", "first"; the page topic line also promises "before and behind". P1-05 note lists rules "1, 2, 3, 5, 10": no row counts in 5s (rows are +1, +2, +10, -10, -2, +3). P1-18 note says "some half-hour additions cross the hour": none do (1:25 -> 1:55, 11:25 -> 11:55); "the decoy times in the table are the time shown": none of 8:10, 1:25, 1:30, 11:25 is in the table; "hands never closer than 25 degrees (except at o'clock)": the o'clock clock (11:00) is 30 degrees. The validator catches only numbers of 11 or more. Fix: delete the clause or generate each note from the page data, and extend the rule to quoted words (a note may name a comparison word only if it occurs in the page text).

**F-new 7. P1-18 reads 5-minute times on three of five clocks; there is no one-star time page.** Evidence: 8:10, 1:25 and 11:25 against the owner's P1 rule "o'clock and half past" (D5 allows 5-minute digits only in Term 4; `p1_school_paper_patterns.md` section 2: 5-minute times appear only in Term 4 review papers). Clock 3 (half past 1) and clock 5 (11 o'clock) are the only core-level items. The pack has no page at all on o'clock and half past, the core P1 time topic (Term 3), and the page is two stars, so a teacher whose class has only met o'clock and half past cannot use it. The teacher notes warn to "check your scheme of work" but do not say 5-minute reading is Term 4. Fix: use o'clock and half past on all five clocks for a one-star version (keeping "1 hour later" and "half an hour later" as the second step), or label P1-18 as Term 4 in the contents and notes; if both are wanted, trade a lighter page (P1-07) for a one-star time page.

**F-new 8. Tier honesty: P1-07 is two stars but is the easiest logic page; P1-06 is light; P1-08 is heavy for one star.** Evidence: P1-07 gives "Aisha is 2nd, Ali is 3rd, Lily is last, Jenny is first": every clue is one direct fact and Ravi is the leftover; no clues are combined (the stated two-star rule is "two steps or two clues to combine"). P1-06 (two stars) is naming shapes from two attributes, easier than P1-02 and P1-04. P1-08 (one star) is 25 additions and a route search. Fix: P1-07 to one star, or give it clues such as "Ravi is behind Ali" and "Lily is behind Ravi" (then the topic line "before and behind" is true); keep ten and ten by moving P1-08 to two stars if P1-07 goes to one.

**F-new 9. Cover, licence and teacher-notes pages: placeholders are not marked as placeholders.** Evidence: the cover prints "Preciouslyours Pte Ltd" in the place where a product line would go, below a blank "This pack belongs to"; the licence page states terms as final ("You may ... You may not ..."), "© 2026 Preciouslyours Pte Ltd. All rights reserved.", "Bound or loose-leaf printed sets can be ordered in bulk. Ask the publisher for a quote." (no contact, and no printed set exists yet), and "The licence is for the edition bought". `AUDIT_FIXES.md` says these were "left as placeholders" (open questions 2 and 9), but nothing on the page says draft; if this PDF were sent to a school it would carry unreviewed licence text and an offer that cannot be fulfilled. Fix: until the owner or a lawyer approves, stamp "DRAFT licence wording: owner to confirm" on the licence page (not on pupil pages), mark the entity and year as to be confirmed in the README table, and replace "Ask the publisher for a quote" with "Printed sets: details to follow" or delete the line.

### Low

**F-new 10. P1-09 "corner lines" is not P1 wording and no diagonals are drawn.** The instruction "Both corner lines make 15" and the boxes "Corner to corner: [] and []" have no picture of the two diagonals; a pupil who ignores them still reaches the one solution (checked: rows and columns alone give one solution), but the check strip then counts "eight totals". Fix: draw two dotted arrows corner to corner and say "Both slanting lines make 15".

**F-new 11. P1-11 uses an outline square as an unknown, which looks like a blank answer box.** In the first set "[] + [] = 18" shows two empty squares exactly like the answer boxes; "Is it a season?" (SPRING) is not a season in Singapore. Fix: make the shapes distinct (a heart, a cross) and use "Is it a time of year?" or choose a different six-letter code word.

**F-new 12. Topic balance and syllabus fit gaps.** All four add/subtract pages stay within 20 (P1 syllabus 2.5 to 2.7 is within 100; only the P1-15 coin sums reach 95); division within 20 (3.4) is absent; multiplication is one page (plan: two); numbers in words, and drawing or copying figures (syllabus 1.1, Geometry 1.4) are absent; whole numbers is 7 of 20. Content on every page is within the P1 syllabus (no prime, fraction, decimal, coordinate; the pentagon appears only as an unnamed icon). Plan unit table for 20 pages suggests 3 pages for add/subtract: one could move to within 100 and one to sharing equally (as pictures, no ÷).

**F-new 13. Two weak word-checks with a larger dictionary.** P1-10 single slip: 17 - 6 answered 6 (copying the subtracted number) spells CATTLE; P1-19 swapping the rectangle and half-circle counts spells PHASE and keeps the total 15 (P1-19 has no hint). `gen/common.py` tests real-word collisions against a 400-word list; the pupil's test is "any English word". Fix: use a large word list in `validate.py` (a SCOWL size-35 list) and re-pick the decoy letters; for P1-19 give the five shapes counts that cannot swap into a word.

**F-new 14. Colour pages: inline answer boxes are about 3.4 mm.** On P1-01, 12 and 14 the missing-number boxes inside the picture are too small to write a number in, so the pupil's working is invisible to a teacher and a slip is hard to trace. The check works (colour tally), so this is Low. Fix: larger boxes where the part allows, and for pencil-only classes allow writing the first letter of the colour (Y, R, B, G, O) in the part; the tally then works on a black-and-white pencil copy (addendum 10 intent).

**F-new 15. Footer breaks with a long school name.** A 68-character name (for example "Saint Gabriel's Presbyterian Primary School (Junior Section, Annex Campus)") wraps the footer onto two lines and splits the page code ("P1-" / "01"); the first audit's test used 62 characters. Fix: let the name shrink or truncate, or put the page code on its own line.

**F-new 16. Page instructions exceed the plan's limits.** Ten pages (P1-03, 04, 05, 07, 08, 09, 11, 16, 18, 20) print four instruction sentences; plan section 3 says "3 lines max" and the P1 row of the reading table says "Page instruction max 2 sentences". Each sentence is short (at most 8 words), so reading load is acceptable; the plan or the pages should be changed to agree.

**F-new 17. Teacher note "When to use" is incomplete.** It names "money, time, length, shapes and picture graphs" and lists P1-06 and P1-15 to P1-20, but omits P1-12 (shapes) and P1-13 (multiplication, usually Term 3 or 4), and says nothing of P1-18's Term 4 content.

**F-new 18. Clock face ticks are tiny.** Only the twelve 5-minute ticks are drawn, each about 0.7 mm long, and at 150 dpi 1-bit they look like stray commas beside the numerals. Hands are fine. Fix: draw the ticks 1.5 mm long, or remove them.

**F-new 19. Key typography and layout.** Answers print as "22B , 43R , 71I" with a space before each comma; entries on page 7 of the key use less than half the page. Cosmetic.

**F-new 20. `AUDIT_FIXES.md` overclaims in two places.** F5 (both grid pages have an example: only one) and F18 ("small solved picture on each entry": 8 of 20). Correct the log when the pack is next changed.

**F-new 21. P1-03 and P1-10 pages are sparse.** Page fill is 58% (P1-03) and 68% (P1-10); a large gap sits between the instructions and the puzzle on both. Fine for P1 pupils; tighten if a page is needed.

**F-new 22. Outcome numbers in the key are still unchecked (carried from F28).** Examples: "3.1 to 3.3 (concept of multiplication, sign x, multiplying within 40)", "2.1 to 2.7 (adding more than two 1-digit numbers)". Tags need to be compared with the syllabus PDF before the first pilot copy leaves the building.

## 5. Ranked top 10

1. F-new 1: hints give the code word away; the two logic grids and the ordering page can be solved without the maths (High).
2. F-new 2: P1-20 check misses a) and b), and a more/fewer reversal passes (Medium).
3. F-new 3: P1-01 "mirror" rule is false for the two round parts (Medium).
4. F-new 5: P1-16 has no worked example of the grid (Medium; fix log says it does).
5. F-new 7: P1-18 reads 5-minute clocks against the o'clock/half past rule and there is no one-star time page (Medium).
6. F-new 4: P1-12 check refers to windows that are not drawn; answer boxes inconsistent (Medium).
7. F-new 6: key notes still describe clues that are not on the page (P1-04, 05, 07, 18) (Medium).
8. F-new 9: cover, licence and notes placeholders are not marked as draft; unfulfillable "ask for a quote" (Medium).
9. F-new 8: tier labels: P1-07 (two stars) is the easiest logic page; P1-08 (one star) is heavy (Medium).
10. F-new 12: no add/subtract within 100, no sharing, one multiplication page (Low, but a Singapore teacher will notice).

## 6. What was checked and found sound (so it is not re-audited)

Unique solutions on all 20 pages (brute force: P1-04, P1-07, P1-09 with and without repeats, P1-16; maze P1-08 one simple route; clue by clue P1-02; part by part P1-01, 12, 14). Black and white: 0 coloured pixels on all 25 pack pages, no grey tint, 1-bit render keeps every line, text and tick. Money uses 50¢ everywhere (coins drawn by value, ¢ in the answer unit, key in ¢). No Mi, no price, no MOE, "aligned" or "affiliated" wording in the pack; the key names the syllabus edition and pages only as a planning reference. No ÷ anywhere. Every instruction sentence has at most 8 words, every number is a numeral, reading level matches the P1 school-paper frames ("Arrange the numbers in order. Begin with the smallest."). Footer school-name field present on all 20 pupil pages and all key pages, filled by `--school`; the front-matter "Licensed to" line and cover fill too. Syllabus fit: nothing beyond P1 on any page (no prime, fraction, decimal, coordinate; the five-sided shape is unnamed). The colour pages' tallies, the P1-14 mirror pairs and the 17-part house tally all re-derive correctly. Rulers on P1-17 are 10.0 mm per cm at 150 dpi and the strip ends sit on the ticks. The key's answers, routes (P1-08 matches my route square for square), the three full answer pages and the thumbnails match my solutions.

Not done (open, as before): a real photocopier test with crayons, a pupil trial, the V9 non-copy comparison, checking each outcome number against the syllabus PDF.
