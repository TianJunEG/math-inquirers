# Independent audit 3: Primary 1 puzzle pack and the colour-by-code library (23 Oct 2026)

Scope: `school/p1/out/P1_Complete_Pack.pdf` (25 pages: 5 front matter + 20 puzzle pages) and `P1_Answer_Key.pdf` (11 pages), after `AUDIT_FIXES_2.md`; and `school/colour_by_code/out/p1` (14 sheets) and `out/p2` (15 sheets), pupil and teacher pages, after `school/colour_by_code/AUDIT_FIXES.md`. Report only; nothing was fixed. The project's `validate.py` and `verify.py` were not run or trusted.

## Method (all mine, none from the project's scripts)
- Every pupil question was solved by me from the rendered PNG (110 dpi, clocks and rulers at 200+ dpi) or from extracted text, then compared with the answer key and with the code word or colour tally. All 20 P1 pages and all 29 colour sheets (about 400 coloured parts) were solved and checked; every answer matched the key and every printed tally was correct.
- Check-strength tests re-implemented from scratch (Python, own word lists: `english-words` web2 + gcide, and `wordfreq` for "common"): single slips, every two-answer slip, every swap, on all 11 code-word pages; full permutation enumeration on the 3 logic pages; a colour-check simulator (tally + mirror pairs or small marks) on 7 colour pages (single, double, swap and triple slips); a P1-19 sum-preserving search; a P1-20 search over all drawn rows and answers.
- Pages viewed: every pack page, all 11 key pages, all 29 teacher pages, pupil pages at zoom where a picture mattered (clocks, rulers, coins, ordinal rows). Purity tested on the PDF drawing operators (fill, stroke, text colour, images, opacity) for all 60 PDFs.
- `build.py --final` and a normal build were run into scratch folders; the repository was not touched. A normal rebuild has the same text as the committed PDFs.

## Verdict
The pack is correct and safe to pilot: no wrong answer, no wrong key entry, no grey, no Mi, no MOE/GEP/SASMO claim, no price. There is no High finding. The Medium findings are one check that can be passed with a wrong answer (P1-20), logic-page notes that overstate their check (P1-04, P1-07), the colour sheets' compare questions that can be answered from the key without comparing, a ruler item that is not read from 0 (CBC-09), clock legibility on the small colour-sheet clocks (P2-08, CBC-08), and two Primary 2 items that go beyond the syllabus summary (P2-07, P2-09).

## Findings, ranked

### High
None.

### Medium
| # | Where | Finding | Evidence |
|---|---|---|---|
| M1 | P1-20 Fruit Graph | The check can be passed with wrong answers. Reading the first two clues with Apple and Banana exchanged (Orange = Banana + 2 = 5, Grape = Apple + 2 = 7, Pear 2) keeps the total at 22; the pupil then answers a) Grape and b) 3 and the second sum is 7 + 3 = 10. Both strip questions say "yes". The cause is that the two clues add the same amount (+2), so the more/fewer fix (test V3e) does not cover a base swap. | Enumerated all rows 0 to 9 and all answers: 359 non-intended combinations pass; among internally consistent pupils 5 pass: (O,G,P) = (5,7,2) with a) Grape, b) 3; (3,8,3); (1,9,4); (8,3,3); (9,1,4). Every other single reading slip fails. Fix idea: make the two +2 clues different amounts and the base fruits' counts such that no exchange keeps the total. |
| M2 | P1-04, P1-07 (and the "wrong word" claim) | A wrong arrangement can still spell a word. P1-04: BOWEL and ELBOW (2 of 119 wrong orders). P1-07: SNEAK (Jenny, Aisha, Lily, Ali, Ravi). This is deliberate (V4 wants at least 2 words from the letters), but the key note for P1-04 says "A wrong placement puts the letters in the wrong order, so the word does not appear", which is false. P1-16 has none. No single swap spells a word on any logic page; the escapes need three or more children or prices misplaced. | Permutation enumeration (P1-04 5! = 120, P1-07 5! = 120, P1-16 5! = 120 with the sum letter). Fix: reword the key note (and the teacher notes) to "most wrong placements"; or accept. |
| M3 | CBC-06, P2-01, P2-07, P2-12 (and any bank with Smallest/Greatest/Middle/odd/even choices) | Every "choose one of three numbers" question has exactly one number that is on the colour key, so a pupil can colour by key lookup without comparing. CBC-06: 5 of 5; P2-01: 7 of 7; P2-07: 5 of 6 (the other has two key numbers); P2-12: 3 of 3. The tally still holds, so the check cannot show it. | Read from the teacher pages. Fix idea: put two key numbers in each triple, or choose decoys that are all not on the key and use a 5-option row. |
| M4 | CBC-09 (P1), ruler item 1 | The strip is drawn from 2 to 4 on a 0 to 5 ruler, not from 0. Reading the right end gives 4, which is another colour on the key; the intended answer is 2. P1 pupils measure from 0 (P1-17 says so). The other two rulers start at 0. The ruler is also about 3.7 mm per "cm", not real size. | Vector coordinates: ruler ticks at 216.3 (0), 237.3 (2), 258.2 (4); strip 237.3 to 258.2. |
| M5 | P2-08 (open item), CBC-08 | Clock legibility. Clock faces are 17 to 18 mm across, numerals 7.1 pt, hour and minute hands both thick and similar in length. Two of the four P2-08 clocks have hands under 30 degrees apart: 4:25 (hands 17.5 degrees apart: they merge into one wedge) and 10:50 (25 degrees). The "never closer than 30 degrees" rule only exists in the P1 pack pages (P1-06, P1-18 use 35 mm clocks with a thin minute hand). CBC-08 (Primary 1) uses the same small clocks, with comfortable angles (45 to 120 degrees) but 7 pt numerals. | Rendered at 230 dpi; angle arithmetic from the printed times. Fix idea: 28 mm faces, thin long minute hand, angle limit, as in the pack. |
| M6 | P2-07 (open item) | Decimal sums. "$0.85 + 50 cents = 135 cents" and "$1.20 + $0.15 = 135 cents" are add-and-subtract of money in decimal notation, which `docs/moe/syllabus_by_level.md` lists at Primary 3 (p. 35); Primary 2 (p. 33) is "compare and convert between decimal notation and cents only". The footer tag "cents, dollars and change" also names "change", which the sheet does not contain. | See "Open items" below: the syllabus summary is right. Fix: replace the two decimal sums with conversions, whole-cent sums or "make $1" items. |
| M7 | P2-09 | Items "1 kg - 750 g = 250 g" and "1 kg - 550 g = 450 g" need 1 kg = 1000 g. Converting between kg and g (and m and cm) is listed at Primary 3 (p. 36) in the syllabus summary; Primary 2 (p. 34) lists the units and compare/order. The fix log presents "1 m minus cm, 1 kg minus g" as a Primary 2 improvement. | Teacher page of CBC-P2-09. Fix: keep g plus g, cm plus cm, litres; or tag as a stretch item. |
| M8 | P1-01, P1-12, P1-14 (and every colour sheet) | Answer boxes inside the picture are about 3 mm. The teacher notes say "the boxes are large for young hands" and the README rule says boxes at least 12 mm high; neither is true here. A pupil cannot write a digit in them, so "Find the missing number" is a mental task. The notes already offer writing Y, R, B, G or O instead. | Measured on 110 dpi renders. Fix: change the notes, or enlarge the boxes. |
| M9 | CBC-12 (P1), CBC-08 (P1), CBC-05 and P1-14, P2-04, P2-14 | Duplicate or near-duplicate questions remain, although AUDIT_FIXES says duplicates were removed by content: CBC-12 has 12 / 2, 6 / 3 and 16 / 4 each twice ("Share 12 by 2" and "Share 12 sweets equally among 2 children"; "6 in 3 equal groups" and "Divide 6 apples into 3 equal groups"; "16 pens, 4 in a box" and "16 pencils, 4 in a box"); CBC-08 prints "Match the time: 2:00" and "2:00 is which time?"; CBC-05 and P1-14 print "60, 65, 70, __" twice (once headed "Count in 5s"). P2-04 and P2-14 repeat each multiplication fact in 2 to 4 wordings (P2-04: 10 x 3 three ways, 2 x 10 three ways; P2-14: 7 x 4 four ways). | Teacher pages. The duplicate test ignores wording only for picture questions and does not treat "Count in 5s:" headed and unheaded sequences as equal. |

### Low
| # | Where | Finding |
|---|---|---|
| L1 | Code pages P1-02, 03, 05, 06, 10, 11, 13, 15, 17, 18, 19 | Guessing the word from the code table letters: 3 to 11 real words of the right length can be built from the table letters (CLOUD, COULD, WOULD; FRIEND, FINDER, REWIND, WINDER; SQUARE with 10 others; STREAM with 8; SECOND, SCORED, CENSOR; FAMILY, MAINLY, INFAMY; NUMBER, JUMPER, BUMPER; PIANO, PANIC; LENGTH, GLUTEN, NUTMEG; OCEAN with 5; ADULT, VAULT). The guess is no longer prompted by the strip, but a bright pupil has a 1 in 3 or better chance. Documented by the project as a limit. |
| L2 | Code pages, double slips | Real words after two wrong answers (my list): CLOCK (P1-02), RECORD (P1-06), STREET and STRESS (P1-10), BUMMER, BUMPER, JUMPER, MEMBER, RUBBER (P1-13: 5 of 1500, 99.67% rejected), VAULT (P1-19, rejected by the total of 15). Single slips and swaps: 0 real words on all 11 pages. AUDIT_FIXES_2 states 99.94% to 100%; P1-13 is below that on my dictionary. |
| L3 | P1-07 | Topic line and contents say "in front of and behind"; the page uses "behind" and "next to" only. The key note hard-codes "ordinal numbers (2nd, 3rd)" but the page's ordinal clue is "4th". |
| L4 | P1-14, CBC-05 | See M9. Also the unpaired top circle and bottom triangle can swap colours without detection (1 swap in 57). |
| L5 | Colour sheets, escapes | My simulator reproduces the project's figures. Undetected double slips: P1-01 2 of 1680; P1-12 2 of 2176; P1-14 1 of 1056; CBC-02 1 of 1920; CBC-07 1 of 1248; CBC-12 3 of 2176 (3 escaping triples as well); CBC-06 0 of 1456. All are swaps of two parts that have no pair or mark. Single slips 100% everywhere. |
| L6 | P1-12, CBC-10, CBC-02, CBC-04, P2-04, P2-13 | A solid black dot sits in one region (door knob, fish eye, castle door). It is not one of the listed marks. A child may look for its partner. |
| L7 | P1-16 | The price pills nearly touch the "How to use the grid" box and the last clue nearly touches the grid header. The code table lists "$7 = X" while the price pill says "$7 = A": two letters for one price on one page. |
| L8 | P1-20 strip | The check strip is three lines and 30 words ("Count the circles in the row you chose in a). Add your answer to b). Is the sum 10?"): heavy for the reading level of the page. |
| L9 | P1-17 | Hatching and ruler ticks are 0.25 to 0.3 mm strokes. Fine on a laser printer; thin for a poor photocopy. All other strokes are 0.4 mm or heavier. |
| L10 | Key, P1-04 | The small solved grid has no row or column labels. P1-06 key entry lists only right answers (the decoys are described in words). |
| L11 | Key, syllabus ranges | P1-01 "1.1 to 1.3" (1.3 is reading and writing numbers, not used); P1-04 "1.4, 1.5" (1.4 is compare sets); P1-17 "Length 1.1 to 1.3" (1.3 compare and order, not used). Ranges are wider than the content. P1-11 item 4 "67 - __ = 33" subtracts a 2-digit number that is not a multiple of ten; the P1 listing is "2-digit and ones" and "2-digit and tens". |
| L12 | P1-12 / CBC-10 | Topic "Shapes: corners": corners are not named in the Primary 1 geometry outcomes (they fall under "describe"). Acceptable, but the key labels the page "identify, name, describe 2D shapes". |
| L13 | CBC-08 teacher page | "Match the time: 2:00", "6:00 is the same as which time?", "3:30 is which time?" and "7:30 is which time?" show only a colour (or the answer without the question). Teacher cannot see the printed digital times. |
| L14 | CBC-P2-12 | "Odd before 504" and "Even after 199" are ambiguous (any odd number before 504); the key and the colour key fix it to the next one. |
| L15 | Contact sheets (`contact_sheet.pdf`) | Raster thumbnails (8-bit colour images, anti-aliased greys). They are galleries, not photocopy pages. |
| L16 | Front matter, `--final` | With `--final`, the licence no longer has any contact line ("Printed sets: details to follow."). The footer name is cut with "..." for a 68+ character school name, so the licence holder is truncated on every page. |
| L17 | CBC-07, CBC-08, CBC-13, CBC-14 | Small pictures: coins 6 to 7 mm with 9 pt labels, clock numerals 7 pt, ruler numerals 7.6 pt, face icons about 3 mm. Hard for 6 and 7 year olds. |
| L18 | Art | Geometric line art; the dinosaur (P2-07, P2-14) is hard to name, the ice cream reads as a snowman with a cone, and 11 pictures serve 29 sheets (5 butterflies, 5 ice creams). Region sizes are fine for crayon (smallest parts are about 20 mm across; the P1 pack colour pages are the same pictures). |

## The 22 earlier findings (`AUDIT_2.md`): are they really fixed?
| Earlier finding | Status now | My evidence |
|---|---|---|
| F-new 1 hints name the word | Fixed | Every code strip reads "Write the letters in order. Do they spell a word?" (the logic strips say "Read ... letters ... Do they spell a word?"); no category word on any of the 20 pages or the key. Residue: L1 (guessable from letters). |
| F-new 2 P1-20 strip | Partly | The more/fewer reversal and a wrong single answer are caught; a base swap is not (M1). The second check also adds a hard-to-read line (L8). The old finding that b) named the fruit that answers a) is fixed (b names Apple and Pear). |
| F-new 3 P1-01 mirror rule | Fixed | The two circles, the two fins, the two top parts and four more pairs are real mirror pairs and share a colour; the rule on the page is true (checked part by part). |
| F-new 4 P1-12 wording | Fixed | No "windows". Parts carry small marks; the check lists six marks. Residue: L6. |
| F-new 5 P1-16 worked example | Fixed | The Zed / Yan box is on P1-16 and P1-04. |
| F-new 6 key notes wrong | Mostly | P1-02, 04, 05, 08, 09, 11, 13, 15, 17, 18, 19 notes checked against the pages and true, except the P1-04 "word does not appear" sentence (M2) and the P1-07 "(2nd, 3rd)" (L3). The key and answers are generated from the page data (`render.key_entry` takes `p["key"]` and `p["note"]` from the same dict that draws the page); my independent answers equal the key on all 20 pages. |
| F-new 7 clock pages | Fixed | P1-06 is only o'clock and half past, thick short hour hand, thin long minute hand, 35 mm faces: all six read correctly (SECOND). P1-18 reads 8:10, 1:25, 1:30, 11:25, 11:00 (3 of 5 at 5 minutes) and the time-later answers give OCEAN. Hands are at least 30 degrees apart. |
| F-new 8 tiers | Accepted | 10 one-star and 10 two-star pages; P1-07 two clues compare children; P1-08 is a light 4 x 4. |
| F-new 9 placeholders | Fixed | DRAFT boxes on cover, licence, both teacher-note pages; none on the 20 puzzle pages. `python3 build.py --final` builds with no "DRAFT", no brackets and no contact text (L16). |
| F-new 10 P1-09 corner lines | Fixed | Two small squares with dashed diagonals; the solution is unique (4 9 2 / 3 5 7 / 8 1 6). |
| F-new 11 P1-11 | Fixed (page replaced) | |
| F-new 12 coverage | Fixed | Fair shares, times code, big number sums are present and correct. |
| F-new 13 word checks | Fixed | Single slips and swaps give no real word on all 11 pages in my dictionaries; doubles per L2. |
| F-new 14 colour boxes 3.4 mm | Not fixed (M8) | |
| F-new 15 long school name | Fixed | A 90-character name is shortened with "...": footer stays on one line (L16). |
| F-new 16 instruction lines | Fixed | Every page has three instruction lines or fewer, sentences of 8 words or fewer. |
| F-new 17 when-to-use list | Fixed | P1-06 and P1-18 explained; list matches the pages. |
| F-new 18 tiny clock ticks | Fixed | 2 mm hour ticks visible on P1-06 and P1-18. |
| F-new 19 key typography | Fixed | No stranded text on the 11 key pages. |
| F-new 20 overclaim in AUDIT_FIXES | Corrected | |
| F-new 21 sparse pages | Fixed | Pages fill at least 70% of the area; P1-07 right side beside the queue still has white space (the clue list is short) but the page is balanced. |
| F-new 22 / F28 outcome numbers | Mostly | Ranges are inside the P1 section of the syllabus summary; three are wider than the content (L11). |

## P1 pack: my solutions and check tests (all single answers use table values)
| Page | Tier | My answers | Word / check | Single slips that spell a real word | Double slips, swaps |
|---|---|---|---|---|---|
| P1-01 Rocket | 1 | 15 parts: yellow 3, red 4, blue 2, green 4, orange 2 (matches key) | tally + mirror pairs | 0 of 60 pass | 2 of 1680 pass (centre parts), 2 of 84 swaps |
| P1-02 | 2 | 66 85 36 56 26 | CLOUD | 0 of 45 | CLOCK 1 of 810; swaps 0 of 10; every clue needed (checked) |
| P1-03 | 1 | 6 3 8 5 4 2 | FRIEND | 0 of 60 | 0 of 1500 |
| P1-04 | 2 | Ali 63 B, Mei 78 E, Siti 23 L, Ben 12 O, Kumar 99 W (unique) | BELOW | n/a | BOWEL and ELBOW pass (M2) |
| P1-05 | 2 | 20 4 5 30 6 10 | SQUARE | 0 of 60 | 0 of 1500 |
| P1-06 | 1 | 8:00 4:00 9:00 1:30 11:30 2:30 | SECOND | 0 of 54 | RECORD 1 of 1215 |
| P1-07 | 2 | Jenny, Aisha, Ali, Ravi, Lily (unique) | SNAKE | n/a | SNEAK passes (M2) |
| P1-08 | 1 | unique route (4,1) (3,1) (2,1) (1,1) (1,2) (1,3) (2,3) (2,4), 8 boxes; 2 other 12-boxes are dead ends | route | n/a | any path ending at FINISH with every box 12 is this path |
| P1-09 | 2 | 4 9 2 / 3 5 7 / 8 1 6 (unique) | eight totals 15 | n/a | the totals are the constraint |
| P1-10 | 1 | 9 7 4 8 5 16 | STREAM | 0 of 60 | STREET, STRESS 2 of 1500 |
| P1-11 | 2 | 21 81 94 34 27 23 | FAMILY | 0 of 60 | 0 of 1500 |
| P1-12 House | 1 | 17 parts: yellow 4, red 2, blue 4, green 3, orange 4 | tally + marks | 0 of 68 pass | 2 of 2176, 2 of 114 swaps |
| P1-13 | 1 | 10 25 18 24 16 20 | NUMBER | 0 of 60 | 5 of 1500 (L2) |
| P1-14 Ice cream | 2 | 12 parts: yellow 2, red 2, blue 3, green 3, orange 2 | tally + pairs | 0 of 48 | 1 of 1056, 1 of 57 swaps |
| P1-15 | 1 | 80 60 40 25 95 | PIANO | 0 of 45 | 0 of 810 |
| P1-16 | 2 | pen 12 M, book 15 O, ball 5 N, kite 8 D, cup 7 A, sum 17 Y (unique) | MONDAY | n/a | no wrong arrangement is a 6-letter word |
| P1-17 | 1 | 4 5 10 2 8 6 cm (strip ends read against the 1 cm ticks; tick spacing checked as 1 mm in the PDF) | LENGTH | 0 of 54 | 0 of 1215 |
| P1-18 | 2 | 9:10 1:55 2:30 11:55 12:00 | OCEAN | 0 of 40 | 0 of 640 |
| P1-19 | 1 | rectangle 1, triangle 2, circle 5, half circle 3, quarter circle 4 (total 15) | ADULT | 0 of 35 | 193 sum-preserving wrong answers (1 to 3 slips): none a word |
| P1-20 Fruit | 2 | Apple 5, Banana 3, Orange 7, Grape 5, Pear 2; a) Orange; b) 3; total 22; 7 + 3 = 10 | two sums | caught | M1 |

## Colour-by-code library: all sheets solved
P1 (14): CBC-01 rocket bonds, 02 fish addition, 03 butterfly subtraction, 04 house tens and ones, 05 ice cream patterns (identical to P1-14), 06 owl compare, 07 sailboat money, 08 butterfly time, 09 ice cream length, 10 house shapes (identical to P1-12), 11 car multiplication, 12 castle sharing, 13 picture graphs, 14 ordinals. P2 (15): P2-01 numbers to 1000, 02 addition, 03 subtraction, 04 multiplication, 05 division, 06 fractions (hatched, not solid black: fixed), 07 money, 08 time, 09 measures, 10 graphs and tally, 11 shapes, 12 odd and even, 13 patterns, 14 multiplication, 15 fractions.
For every sheet I solved each printed question, compared with the teacher page, and checked the tally: 29 of 29 match; every answer is a key value. The F1 error of the first audit (CBC-06 "10 less than a, then 1 more") is fixed: 64 -> 55, 84 -> 75 are right. The shaded fraction bars are hatched. Fractions are stacked. Findings M3, M4, M5, M6, M7, M9, L5, L13, L14, L17, L18 come from this part. Syllabus footers are accurate except P2-07 ("change"), P2-09 (kg and g), P2-10 ("tally marks", not in the syllabus summary; known).

## B&W purity, print and legibility
- All 25 + 11 pack and key pages and all 58 pupil/teacher colour pages: only black (0) and white (1) for strokes, fills and text; no images; no opacity below 1. The only raster files are the two `contact_sheet.pdf` (L15). No grey fills anywhere; hatching is black lines.
- P1 text sizes: instructions about 15 pt, code boxes 14 pt; smallest text on a puzzle page is 8.5 to 9.4 pt (clock numerals P1-18, shape labels). Colour sheets: region text 10.5 pt; coins 9 pt, clock numerals 7 pt, ruler numerals 7.6 pt (L17).
- Teacher key: clear; page 1 has the strand table and an honest "not covered" list; every entry has answers, the check result, a note, and a small solved picture where it helps; three full-size colour answer pages. Usable in about 10 seconds per page.
- No Mi, no MOE, GEP, SASMO, "approved", "aligned" or price anywhere in the pack, key or 58 colour pages (text search). The key cites "Mathematics Syllabus, Primary (2021 edition, pages 31 and 32)" for planning only; the syllabus PDF is not in the repository, so the page numbers are as recorded in `docs/moe/syllabus_by_level.md`.
- Originality: 7-word overlap against `docs/books/*.md` and `private_p1` to `private_p6` files (52 files, 4 MB): 10 of the 60 PDFs have a hit; all are number lists ("2 3 4 5 6 7 8", "tables of 2, 3, 4, 5 and 10") or the generic riddle opening "my ones digit is 6. my tens digit is" (P1-02), which is also in our own wording notes and is an idiom, not a copied question. No question text is copied.

## Open items
**P2-07 decimal sums: which file is right?** The syllabus summary (`docs/moe/syllabus_by_level.md`, P2 p. 33 and P3 p. 35) is right for the syllabus: P2 money is dollars and cents, decimal notation, compare, and convert between decimal notation and cents only; "add and subtract money in decimal notation" is a Primary 3 line. The paper-patterns file (`docs/books/p2_school_paper_patterns.md` section 3.6) does not contradict this: it says story prices are whole dollars up to $100 and whole cents to 95 cents, decimals appear for reading and ordering ($14.05 versus $14.50), and mixed notation appears in single items ("60 cents and $__ make $1"). I read all 72 money records in `private_p2_papers/records.jsonl`: none adds or subtracts two decimal-dollar amounts. Three items use cents and a decimal answer ("85 cents, a marble costs $0.20, how much is the aeroplane? $0.45"; "50 cents + 30 cents, answer in dollars $1.30"; "$2 minus 65 cents and 25 cents = $1.10"). So "$1.20 + $0.15" is outside both sources; "$0.85 + 50 cents" is a mixed-notation item that a paper might use but is still above the syllabus line. Recommendation: replace both with conversions, "make $1", or whole-cent sums (M6).

**P2-08 clock legibility:** still open and real (M5): small faces, equal-weight hands, 4:25 and 10:50 hands within 25 degrees, 7 pt numerals.

## Not covered
Pupil trial; real photocopier test with crayons; the syllabus PDF itself (only the project's summary was available); the P3 to P6 colour sheets (not in scope); `validate.py` and `verify.py` were deliberately not used.
