# Audit fixes, round 2: finding -> action (school/p1, 23 Oct 2026)

Source: `AUDIT_2.md` (22 findings: 1 High, 8 Medium, 13 Low). Scope: `school/p1` only. "Fixed" means rebuilt, validated (381 checks, 0 failed; `python3 validate.py`), and the page viewed (every pupil page at 70 dpi, clocks, ruler and new icons at 150 dpi 1-bit; front matter and all key pages at 70 dpi).
The colour-by-code agent had finished (`school/colour_by_code/AUDIT_FIXES.md` exists); its library at commit e7d74e1 was copied unchanged into `cbc_vendor/` and the three colour pages were rebuilt on it. CBC-06 (owl) is not used: the owl was not needed, so nothing depends on it.

## New page set (20 pages, 10 one-star and 10 two-star)

Dropped to make room: P1-03 Number Cards, P1-05 Missing Numbers (P1-14 and P1-02 still cover number order and patterns), P1-06 Shape Riddles, P1-11 Shape Sums. Added: P1-03 Fair Shares (sharing and grouping within 20, no division sign), P1-05 Times Code (second multiplication page), P1-06 What Time Is It? (one star, o'clock and half past), P1-11 Big Number Sums (add and subtract within 100). Page numbers of kept pages did not change. The cost: no page asks a pupil to name a shape from a description (listed under "not covered" in the README), and the pack has two shape pages instead of three.

| Strand | Pages | Count |
|---|---|---|
| Whole numbers | P1-01, 02, 04, 07, 14 | 5 (was 7) |
| Add and subtract | P1-08, 09, 10, 11 | 4 (11 now reaches 100) |
| Multiplication and sharing | P1-03, 05, 13 | 3 (was 1) |
| Money | P1-15, 16 | 2 |
| Time | P1-06 (one star), P1-18 (two stars) | 2 (was 1) |
| Shapes | P1-12, 19 | 2 (was 3) |
| Length, picture graph | P1-17, P1-20 | 1 each |

## High
| Finding | Status | What was done |
|---|---|---|
| F-new 1 hints give the code word away on 14 pages | fixed | Every code-word strip is now "Write the letters in order. Do they spell a word?" (the logic pages say "Read your ... letters ... Do they spell a word?"); no category hint anywhere. `validate.py` fails any strip that says "Is it ...", "Does it ..." or names the old categories. The strip never says what the word is. New test V4 (guess resistance) on every code page: at least 3 common words can be made from the letters in the code table; on the logic pages the letters beside the numbers, prices or on the shirts can be arranged into at least 2 common words (P1-04 BELOW or BOWEL or ELBOW; P1-07 SNAKE or SNEAK; P1-16 MONDAY or DYNAMO). Decoy letters are chosen with this in mind. Limit: V4 lowers but does not remove the chance that a bright pupil guesses a word from the letters; a pupil who also checks one row finds out. |

## Medium
| Finding | Status | What was done |
|---|---|---|
| F-new 2 P1-20 check misses a) and b); more/fewer reversal passes | fixed | The Grape and Pear clues now differ (Grape +2, Pear -1 on this seed; the generator requires different amounts), so exchanging "more" and "fewer" on any of the 7 subsets of clues changes the total (test V3e). A second check in the strip: "Count the circles in the row you chose in a). Add your answer to b). Is the sum 10?"; a wrong a) or b) changes the sum (single slips 40/40 and every wrong fruit or number rejected). Found while fixing: question b) printed the fruit that answers a) ("Orange has [] more than Pear"); b) now names two other fruits (test V2d). |
| F-new 3 P1-01 "mirror" rule false for the round parts | fixed | The rebuilt library pairs the two circles (a real mirror pair, 6 pairs), and a new test (V2c) fails any page whose printed left-right rule is false: no two parts may sit in mirror-image places without being a declared pair (checked on rocket and ice cream; the house has no left-right rule). The check text is the library's "Parts in the same place on the left and on the right have the same colour." |
| F-new 4 P1-12 "the two windows" not shown, boxes inconsistent | fixed | No such wording: the house now has small black marks on matching parts and the check reads "Parts with the same small mark have the same colour:" followed by the six marks (square, triangle, diamond, star, cross, hexagon). `validate.py` finds no "window", "wall" or "scale" on any pupil page. Label boxes inside the picture are still the library's (about 4 mm: too small to write in; the check does not rely on them; see F-new 14). |
| F-new 5 P1-16 no worked grid example | fixed | P1-16 now prints the same "How to use the grid" box as P1-04 (beside the clues). Instruction lines cut to 3. |
| F-new 7 P1-18 reads 5-minute times; no one-star time page | fixed | New one-star page P1-06 "What Time Is It?": six clocks, o'clock and half past only (test V1b: no other minutes, hands at least 25 degrees apart, no 12:00). P1-18 stays two stars as the five-minute page: at least 3 of its 5 clocks show a 5-minute time (test V1d), the topic line says "Time to 5 minutes", and the teacher notes say 5-minute reading is usually late in Primary 1. |
| F-new 6 key notes describe clues that are not on the page | fixed | Notes are generated from the page data: P1-02 and P1-04 list the clue kinds actually used; P1-07 lists the clue kinds used; P1-05 (the old pattern page) is gone; the P1-18 note now says "None of the half-hour additions cross the hour" or counts how many do, lists the decoy kinds that are really in the table, and states the real minimum hand angle (30 degrees). The validator checks that every clue word named in a note (more than, fewer than, less than, greatest, smallest, second greatest, ordinal, in front of, behind, next to, ones digit, tens digit, half-hour) occurs on its page, and that the P1-18 hour-crossing statement is one of the two true forms. |
| F-new 8 tier honesty | fixed | P1-07 now has two clues that compare two children (in front of, behind, next to), so two stars is right and the topic line "in front of and behind" is true. P1-08 is a 4 x 4 grid with an 8-box route (16 sums, was 25), a light one-star page. P1-06 (the light shape page) was replaced. The 10 and 10 split is kept. |
| F-new 9 placeholders not marked | fixed | Cover, licence and teacher-notes pages carry a "DRAFT" box with `[contact email or phone: to be added by the owner]`; the cover publisher line reads "[Publisher line: wording to be confirmed by the owner]"; the licence page title says (DRAFT), asks for the entity, year, licence term and contact, and "Ask the publisher for a quote" became "Printed sets: details to follow" (nothing is offered that cannot be supplied). Pupil pages carry no DRAFT stamp (test). `python3 build.py --final` leaves the stamps out once the owner and a lawyer approve. The footer still prints "(c) 2026 Preciouslyours Pte Ltd"; the README lists entity and year as open. |

## Low
| Finding | Status | What was done |
|---|---|---|
| F-new 10 P1-09 corner lines not drawn | fixed | Two small squares with a dashed corner-to-corner line sit beside the two total boxes; wording "Both lines from corner to corner make 15." (no "corner lines"). Viewed at 150 dpi 1-bit. |
| F-new 11 P1-11 outline square looks like a blank box; SPRING not a season | fixed (page replaced) | P1-11 is now "Big Number Sums"; the shape-sums page is gone. |
| F-new 12 coverage | fixed | Add and subtract within 100 (P1-11: 2-digit and ones, 2-digit and tens, two missing-number items; no renaming), sharing and grouping within 20 (P1-03), a second multiplication page (P1-05). Not covered, by choice: numbers in words, drawing figures, naming a shape from a description. |
| F-new 13 weak word-checks | fixed | The 400-word list is no longer the test: `gen/words_en.txt.gz` holds about 129 000 words. Code words were changed so none has a one-letter slip or a swap that spells another word (CASTLE/CATTLE, SHAPE/PHASE, PENCIL/PENCEL and similar pairs removed); decoy letters are drawn only from letters that cannot make a word. Enumerated: no single slip and no swap of two answers spells a word on any code page; two-answer slips rejected 99.94% to 100% on the 11 code pages (my own enumeration, not in `validate.py`). Words now: CLOUD, FRIEND, SQUARE, SECOND, STREAM, FAMILY, NUMBER, PIANO, LENGTH, OCEAN, ADULT (code pages) and BELOW, SNAKE, MONDAY (logic pages). |
| F-new 14 CBC inline boxes about 3.4 mm | partly | Not changed (library). The teacher notes now say pencil-only classes can write Y, R, B, G or O in each part so the tally and the matching parts work on a black-and-white copy (addendum 10). |
| F-new 15 footer breaks with a long school name | fixed | The school name is its own span that shrinks with an ellipsis; the code and licence text stay on one line. `validate.py` builds the pack with a 68-character name and checks that every pupil page's last line holds the page code and "Photocopy licence:". |
| F-new 16 instruction lines exceed the plan | fixed | Every page has at most 3 instruction lines (P1-20 went from 4 to 3); `validate.py` enforces it. Sentences are at most 8 words. |
| F-new 17 "when to use" incomplete | fixed | The list is generated from a flag on each page (P1-03, 05, 06, 12, 13, 15, 16, 17, 18, 19, 20) and states that P1-06 is o'clock and half past and P1-18 is late-year. |
| F-new 18 clock ticks tiny | fixed | The twelve hour ticks are about 2 mm long and 0.5 wide; viewed at 150 dpi 1-bit on P1-06 and P1-18. |
| F-new 19 key typography | fixed | The card-order page with "22B ," is gone; key pages repacked (11 pages). |
| F-new 20 `AUDIT_FIXES.md` overclaims | corrected here | F5 of the first log said both grid pages carry the example box: true only of P1-04 until this pass; P1-16 has it now. F18 said a small solved picture on each entry: it is on the picture, grid, route, magic-square and graph entries only (the README says so). `AUDIT_FIXES.md` itself is left as history. |
| F-new 21 P1-03 and P1-10 sparse | fixed | P1-03 (cards) is gone; P1-10 rows are taller (puzzle content 74% of the area). Every pupil page now fills at least 70% of its puzzle area (P1-07 70%, P1-04 72%, P1-10 and P1-11 74%). |
| F-new 22 / F28 outcome numbers unchecked | verified at range level | Every page's syllabus tag is checked by `validate.py` against the Primary 1 section of `docs/moe/syllabus_by_level.md`: each topic phrase (count a set, tens and ones, compare and order numbers, ordinals, number-sequence patterns, adding more than two 1-digit numbers, within 100, 2-digit plus ones without renaming, 2-digit plus tens, mental calculation within 20, inverse relationship, multiplying within 40, sign x, dividing within 20, count money in cents up to $1, dollars up to $100, length in cm, tell time to 5 minutes, durations of one hour or half hour, identify the shapes in a figure, picture graphs) must be found in that file, and every outcome number must lie in the stated ranges (Whole Numbers 1.1 to 1.7, 2.1 to 2.7, 3.1 to 3.4, Length 1.1 to 1.4, Time 2.1 to 2.4, Geometry 1.1 to 1.4). The summary numbers only some outcomes singly (1.4 compare sets, 1.6 patterns, 1.7 ordinals, 3.4 division); the tags therefore use ranges elsewhere, and P1-18 now says 2.1 and 2.4. Still to do by the owner: a look at the syllabus PDF itself (not in the repository) before a pilot copy leaves the building. The key says "where the syllabus lists several outcomes under one topic, the range is given". |
| F23 licence placeholders | marked | See F-new 9. |

## First-audit findings that were open
F6 (tier honesty), F7 (key states things that are not on the page), F10 (strand balance), F18, F23 and F28: see F-new 8, 6, 12, 20, 9 and 22 above. F5 (grid how-to) is complete: both grid pages print the example.

## Other changes
- `gen/common.py`: large word lists, `bad_letters`, `make_code_table` (re-rolls answers and decoys until no slip or swap makes a word and at least 3 common words fit the letters), `code_checks` (V2, V3, V3c, V4 on every code page).
- `gen/pages_cbc.py`: built on the new library (`S.flags` for the checks, `textcheck` for the independent re-solve of every printed question, double-slip and swap enumeration (95% each), label-in-region check in the browser). The three colour pages: P1-01 rocket (swaps 86/88, double slips 1678/1680), P1-12 house (112/114, 2174/2176), P1-14 ice cream (56/57, 1055/1056); single slips 100% on all three.
- `validate.py`: 381 checks (was 322).
- `render.py`: DRAFT stamps and contact placeholder, footer that cannot wrap, CSS for the new pages.

## Left open
Pupil trial; a real photocopier test with crayons; the V9 non-copy comparison; a syllabus PDF look at individual outcome numbers; the entity name, year, licence wording and contact address (owner and lawyer); whether three colour-by-code pages is right; larger answer boxes inside the colour pictures (library).
