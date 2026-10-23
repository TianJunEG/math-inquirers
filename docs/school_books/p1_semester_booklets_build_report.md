# Primary 1 semester booklets: build report (running progress note)

Branch `claude/great-fermi-1hv4vc`, started 23 Oct 2026. Built per `p1_semester_booklets_plan.md` and the owner decisions in `docs/terms/owner_decisions.md` ("23 Oct 2026 (evening)"). Not pushed, no PR. The independent audit is the owner's separate step and was NOT run.

## Progress (update after every wave)

- [x] (a) Parameterised `build.py`, `validate.py`, `render.py` for two booklets (outputs `P1_S1_*`, `P1_S2_*`; page counts follow `gen/outcomes.py`), outcome map of the 32 PDF lines, footer codes `S1-07 (P1-08)`, per-booklet front matter and key, `docs/moe/syllabus_by_level.md` extended with the PDF wording, P1-03 sharer line, P1-13 and P1-16 retags.
- [x] Wave 1: N01 Story Sums (P1-21, S1-10), N02 Two-Step Stories (P1-22, S2-20)
- [x] Wave 2: N10 Stack It Up (P1-23, S2-07), N04 Words and Numbers (P1-24, S1-03), N05 Count the Crowd (P1-25, S1-01), N06 Chart Patterns (P1-26, S1-15). N06 is a code-word page, not the plan's K2 hidden picture (a 3-mark picture rejects only about 2/3 of wrong numbers; the 95% rule needs K1)
- [x] Wave 3: N13 Which Two Items? (P1-27, S2-13), N14 Fewest Coins (P1-28, S2-11), N17 How Long Does It Last? (P1-29, S2-16), N18 Morning or Evening? (P1-30, S2-15). Clock numerals redrawn (even placement, larger) for all clocks.
- [x] Wave 4: N15 Shortest to Longest (P1-31, S1-18), N16 Measure and Draw (P1-32, S2-08), N19 Shape Builder (P1-33, S1-16), N20 replaced by Finish the Figure (P1-34, S1-17), N21 Read the Picture Graph (P1-35, S2-17), N22 Graph Detective Two (P1-36, S2-19)
- [x] Wave 5: N09 Bonds and Families (P1-37, S1-08), N03 More or Fewer (P1-38, S1-12), N11 Share and Group (P1-39, S2-02), N12 True or False (P1-40, S2-05). validate.py: 770 checks, 0 failed (all 40 pages)
- [x] Added scope (coordinator, owner approved diagrams): P1-05 arrays, P1-03 and P1-13 bigger objects, clock numerals (P1-06, 18, 29), P1-07 drawn people. CBC-13 / mini clocks / coins / rulers in the colour gallery: not done (see `docs/audit_final/diagrams_extension_p1.md`, P1 section)
- [x] Final: `validate.py` 775 checks, 0 failed; outputs regenerated and committed; README rewritten

## What was built

Two booklets of 20 pupil pages each, built by `school/p1/build.py` and checked by `school/p1/validate.py` (775 checks, 0 failed; about 3 to 4 minutes). Page order and the two page numbers come from `school/p1/gen/outcomes.py`.

| Output (school/p1/out) | Pages |
|---|---|
| `P1_S1_Puzzles.pdf`, `P1_S2_Puzzles.pdf` | 20 and 20 |
| `P1_S1_FrontMatter.pdf`, `P1_S2_FrontMatter.pdf` (cover, licence, teacher notes x 2, contents and outcome coverage) | 5 and 5 |
| `P1_S1_Complete_Pack.pdf`, `P1_S2_Complete_Pack.pdf` | 25 and 25 |
| `P1_S1_Answer_Key.pdf`, `P1_S2_Answer_Key.pdf` | 10 and 9 |

Semester 1 is 10 one-star and 10 two-star pages. Semester 2 is 9 one-star and 11 two-star pages since the owner made P1-39 a two-star page (P39-TWO); no other page was rebalanced. Footers print both numbers, for example `S1-07 (P1-08)`. All 32 syllabus outcome lines (wording copied from the PDF, now also in `docs/moe/syllabus_by_level.md`) are exercised by at least one page; validate.py checks this and that every tag number belongs to the page's own outcome ids.

The 20 new pages (final ids in build order):

| Wave | Page | Booklet position | Stars | Check |
|---|---|---|---|---|
| 1 | P1-21 Story Sums (N01) | S1-10 | 2 | code word MONKEY |
| 1 | P1-22 Two-Step Stories (N02) | S2-20 | 2 | code word GUITAR |
| 2 | P1-23 Stack It Up (N10) | S2-07 | 1 | DONKEY |
| 2 | P1-24 Words and Numbers (N04) | S1-03 | 1 | route (domino maze of words and numerals, 2 ordinal links) |
| 2 | P1-25 Count the Crowd (N05) | S1-01 | 1 | CLOTH |
| 2 | P1-26 Chart Patterns (N06) | S1-15 | 2 | PEANUT |
| 3 | P1-27 Which Two Items? (N13) | S2-13 | 2 | MAGNET (letters of the chosen pairs) |
| 3 | P1-28 Fewest Coins (N14) | S2-11 | 1 | STAMP |
| 3 | P1-29 How Long Does It Last? (N17) | S2-16 | 1 | SAILOR |
| 3 | P1-30 Morning or Evening? (N18) | S2-15 | 1 | route (sensible am or pm boxes) |
| 4 | P1-31 Shortest to Longest (N15) | S1-18 | 1 | BLANK (5 letters, longest strip is a decoy) |
| 4 | P1-32 Measure and Draw (N16) | S2-08 | 1 | STRING (letter ruler) |
| 4 | P1-33 Shape Builder (N19) | S1-16 | 2 | total 16 + TRUNK |
| 4 | P1-34 Finish the Figure (N20 replaced) | S1-17 | 2 | FROG (matching right half) |
| 4 | P1-35 Read the Picture Graph (N21) | S2-17 | 1 | TURKEY |
| 4 | P1-36 Graph Detective Two (N22) | S2-19 | 2 | total + second sum (K3) |
| 5 | P1-37 Bonds and Families (N09) | S1-08 | 2 | loop closes (K8) |
| 5 | P1-38 More or Fewer (N03) | S1-12 | 2 | GLORY (5 letters, one decoy amount) |
| 5 | P1-39 Share and Group (N11) | S2-02 | 1 | SPONGE |
| 5 | P1-40 True or False (N12) | S2-05 | 2 | TEACUP (letter of the ticked T or F) |

Every new page has: a generator with its own seed; an independent solver that reads the printed text or drawing (clock hands, strip widths, drawn edges, symbols per row, objects per svg) and not the generator's data; the wrong-answer enumeration (every single slip, and every wrong arrangement on the logic pages, at 95% or better: all 40 pages in `verification.json` reject 100% of single slips); the word test (one arrangement only, no slip, swap or wrong placement spells a word of the 129 000-word list; decoy letters where a page leaves one item out); a key with the answers and the check result; a viewed render (colour and a 1-bit photocopy simulation of every page, plus contact sheets of both booklets). Colour-by-code pages are unchanged in design (3 of 40: P1-01, 12, 14). The eight code words the owner kept are untouched.

## Hand-solved sample

13 of the 20 new pages were solved by hand from the rendered page, not the key, then compared with the key: P1-21, 22, 23, 25 (counted from a zoomed image, which found a clipped row, fixed), 27, 28, 29 (clock read from a 200 dpi crop), 33 (shapes counted from a 90 dpi crop), 35, 36, 37, 38, 39 and 40 (counted twice; P1-25 is the one where the first hand count disagreed). The other pages (P1-24, 26, 30, 31, 32, 34) rely on the independent solvers and on looking at the render; the audit should hand-solve these.

## Differences from the plan and weak points (honest list)

1. **P1-26 (N06) is a code-word page, not a K2 hidden picture.** A closed set of three marks can reject only about two thirds of wrong numbers; the 95% rule needs a letter per answer. The chart piece, the 10 more and 10 less items and the growing table are as planned.
2. **P1-37 (N09) is the loop only.** The plan also had "write the other sentence" and "list every pair that makes 10 and count them". Neither could be given a self-check of 95% or better without printing the answer, so they were dropped; the inverse idea is used every time a part is found from the whole. The loop checks every empty circle (all single slips rejected); two wrong numbers that cancel on a link with two empty circles are possible (at most one such link per page).
3. **P1-34 (N20 replaced) is checked by matching, not by drawing.** The pupil copies the figure's right half on a grid, then picks the printed right half (lettered) that matches; the page cannot see the drawing. Cells are 6 mm (small for crayons). The owner asked for a printed match; this is the weakest page for the outcome "copying figures".
4. **P1-32 (N16)**: the drawn line is not seen by the page either; the pupil finds the letter at the end mark of the ruler. The length of measured bars is read through a code ruler.
5. **P1-38 (N03)** uses 5 children and 6 amounts (one decoy) like P1-04, not the 4 by 4 of the plan, so that the word test and the guess test hold. It has more than, fewer than (reversed) and a give-to-make-the-same clue.
6. **P1-19 (Shape Count)** already contained half and quarter circles when this build started (the plan said to add them). No change was needed.
7. **Titles changed** to fit the header: Shortest to Longest (was Longer, Shorter, Longest), Chart Patterns, Share and Group, True or False, Measure and Draw.
8. **P1-05** now has arrays; factors are 2 to 5 (10 dropped) and products stay within 25 so the arrays fit. **P1-13** bags hold their things in two rows; totals within 24. **P1-07** has drawn people.
9. **P1-18 and P1-06 clocks** and all clocks on the new pages: numerals on a true circle, larger; minute hand stops inside the numerals.
10. **P1-30 (N18)**: which times suit which event is a judgement (for example dinner 6:00 to 8:00 pm). The table is in the generator and, separately, the solver; a teacher should glance at the eight events.
11. **P1-23 (N10)**: the syllabus gives no limit for algorithms; the safe reading used is within 100 and no renaming.
12. Page 27 (Which Two Items?) and page 40 use letters on choices; a pupil can guess by trying pairs, which is the intended guess-and-check.
13. The licence page carries the sentence "Not affiliated with or endorsed by the Ministry of Education, Singapore." as plan section 6a lists it; validate.py allows that one sentence (and the following sentence about who publishes the syllabus) on front matter and nowhere else. The owner said no MOE claims: this is a disclaimer, not a claim, but say if it should go.
14. The four old PDFs of the single 20-page pack were removed from `school/p1/out`; the booklets replace them.
15. Not done: CBC gallery diagram fixes (CBC-13 graph icons, tiny mini clocks, coins and rulers in `school/colour_by_code`), number lines for P1-02, 10, 11, a composite picture for P1-19. The booklets use only P1-01, 12 and 14 from the colour library.
16. Another process commits the working tree as "Checkpoint" commits, so some of my small commits contain nothing new; the history of wave 1 to 5 is still visible (`P1 booklets, wave N` commits).

## Items for the owner

- Titles and the working product names (Semester 1, Semester 2), the publisher line, licence wording and term: still DRAFT placeholders; the licence page covers one booklet only. Entity and year are CONFIRMED by the owner ((c) 2026 Preciouslyours Pte Ltd, printed in every pupil footer); the registered office is 66 Tannery Ln, Singapore 347805 (licence page).
- Accept P1-34 and P1-32 as checked by matching, not by seeing the pupil's drawing, or ask for a different page.
- A pupil trial (4 to 6 children), ideally with P1-24 (domino route), P1-32 (rulers), P1-34 (copy), P1-37 (loop) and P1-17, P1-29 clocks, and a real photocopier test with crayons for the three colour pages.
- Whether the "problem solving" tag (P1-16, 22, 27, 28, 38, 39) and its teacher-note sentence are right; the key marks them.
- Ordinals: P1-24 reaches tenth; P1-07 still stops at fifth.
- Whether the one not-affiliated sentence stays on the licence page.
- Whether to draw the CBC gallery diagram fixes and the other B items of the diagram audit (not in this build).
- The independent audit (hand-solve at least the six pages named above, mono copy test, V9 non-copy check): the owner's next step, not run here.

## Audit round 1: fixes made (23 Oct 2026, after `docs/audit_final/p1_semester_booklets_audit.md`)

validate.py: 781 checks, 0 failed. Page counts unchanged (20 / 5 / 25 / key 10 and 9, all even per booklet). Every changed page was re-solved by hand from the rendered image (P1-03, 05, 12, 13, 21, 25, 28, 30, 33, 38, 39; P1-22, 34 re-checked against their solvers and the render) and viewed in colour and as a 1-bit copy.

| Finding | Fix |
|---|---|
| H1 P1-12 | Every part now has a thick write-on line in place of the small square box (a box looks like one of the squares being counted); the label "Corners:" is printed wherever the part is large enough (3 of 17 parts; the rest are too small to hold shapes, label and line, so they show shapes and the thick line only); the instruction says "Write it on the thick line". Marks are now triangle, square, star, cross, circle, moon (hexagon and diamond removed everywhere in the colour library). Hand count of all 17 parts matches the tally (yellow 3, red 4, blue 3, green 3, orange 4). |
| H2 P1-33 | A real "form a figure" task was added: a small outline is shown and the pupil picks which two pieces make it (three lettered sets with different total areas); its letter is the sixth letter of the code word, which is now BUDGIE (six boxes). The independent check compares the drawn outline's area with each set. 2D Shapes 1.2 is now genuinely practised; "all 32 outcomes covered" holds (validate.py checks it). P1-33 also says squares and rectangles are different kinds here. |
| H3 | Both answer keys carry the DRAFT stamp and the contact email. While entity and year are unconfirmed the pupil footers drop the "(c) 2026 Preciouslyours Pte Ltd" line (a `--final` build prints it); the footer keeps "Photocopy licence: ____ (school name) only", the blank line the licence sentence describes. Still owner items: entity, year, publisher line, licence wording and term, registered office. Keys now print "Key page n of N" and the right footer example. |
| M1 objects | Counted objects drawn at 9 to 11 mm cells (the round-1 text said this was the picture size; the glyph measured 5 to 7 mm, see Round 2): P1-25, 21, 03, 39, 13 and the P1-05 arrays at 8 mm (rows of at most 4). To fit, counts were reduced (P1-21 first groups at most 7; P1-13 totals within 16; P1-05 groups of 2 to 4 with products within 20; P1-03 objects 8.6 mm, 10 per row) and the answers and code tables regenerated, so keys changed. P1-22 stories no longer carry pictures (not a counting task). |
| M2 P1-34 | Grid 4 by 3 cells of 9 mm (was 6 by 4 of 6 mm); the right half is two columns. |
| M3 P1-28 | Purses: four, two per row, coins 1.2 times larger; "cents" lettering larger on every coin page. |
| M4 P1-39 | "The sharer gets a share too." is now an instruction line at the top. Star level not changed (pupil trial). |
| M5 P1-38 | Clue 4: "Kumar gives 7 stickers to Ben. Then they have the same number." |
| M6 notes | Loop bullet no longer claims a printed total; the problem-solving sentence names examples that are in that booklet. |
| M7 cover and notes | Cover: "Almost every puzzle checks itself"; the notes say that on Finish the Figure (S1) and Measure and Draw (S2) the check tests matching and reading, not the drawing. |
| M8 colour pages | Pupil instruction: "No crayon? Write Y, R, B, G or O."; notes: light crayons, a dark one hides the number on a copy. Space for a letter in the smallest parts was not re-checked. |
| M9, L3 P1-30 | No 12:00 or 12:30 times and no "recess" event; the event list is seven events. |
| L1 | Notes add that two wrong answers at once were not all tested. The single-slip words SIRING (P1-32) and JAILOR (P1-29) found by the audit were not changed. |
| L2 | Done with H1. |
| L4 | P1-01 no longer tagged 1.1; P1-38 tagged 1.5 instead of 1.4 (all 32 outcomes still covered). |
| L5 | Done with H2. |
| L6 | Notes name the offset-ruler extension. |
| L7 | Minute hands already stop inside the numeral ring (build wave 3). |
| L8 | Tile labels on P1-37 made smaller. S2-12 box spacing and S1-11 icon size not touched. |
| L9 | Done with H3. |

Not fixed or left for the owner: the entity, year, publisher and licence placeholders (H3); the eight-wording question of the not-affiliated sentence (kept on the licence page only, as asked); pupil-trial questions (stars of P1-39, fairness of the P1-31 trap); coin art comparison (L10); P1-12 parts too small to carry the label (3 of 17 labelled); the P1-01 and P1-14 colour pages were regenerated with the new marks and checked by validate.py, their small-part letter space not re-measured; validate.py thresholds loosened slightly for the small-print pages (front matter 1-bit ink loss 32%, key flat-grey blocks 90 per page, both anti-aliasing of small text on pure black and white PDFs).

## Round 2 (after `docs/audit_final/p1_semester_booklets_audit_round2.md`) and owner confirmations

validate.py: 783 checks, 0 failed. Page counts unchanged (20 / 5 / 25; keys 10 and 9). Every changed page viewed in colour and as a 1-bit copy and re-solved by hand from the image (P1-03, 05, 12, 13, 21, 25, 39; P1-22 re-checked).

| Finding | Fix |
|---|---|
| H1 P1-12 doorknob dot | The doorknob decoration was removed from the house picture (`cbc_vendor/pictures.py`); the only black dots are now the three twin marks, all on orange parts. Hand count of all 17 parts again matches the tally (Y3 R4 B3 G3 O4). |
| M1 code tables | Tables are one row of at most nine narrower boxes with smaller type (P1-21 now eight boxes); letters no longer touch the edges (viewed on P1-21, 03, 13, 05, 28, 22). |
| M2 object size | Objects were redrawn at sizes chosen from measured glyph boxes (300 dpi render of each picture in a 20 mm cell): apple 8.0 x 9.0 mm at size 11; star 8.6 x 8.1 at 9.2; ball 8.2 x 8.2 at 9.0; cat 8.9 x 8.1 at 9.8; drum 8.3 x 8.1 at 10.2; boat 9.0 x 8.2 at 10.5; flower 8.1 x 10.3 at 10.5; car 12.7 x 8.1 and bird 12.3 x 8.0 on the fact pictures. So every counted picture is at least 8 mm in both directions. Balloons, fish, kites, sweets and dogs were dropped from counted pages (too narrow to reach 8 mm without taking the page). Counts were reduced again so pages fit: P1-21 first groups at most 6, P1-03 at most 9 rows in all with 8 objects per row, P1-13 bags at 10.8 mm pitch, P1-05 two or three groups, P1-39 at most 12 objects. Answers, code tables and keys regenerated. The round-1 text "8 to 10 mm" gave the cell size, not the picture; the corrected claim is the table above. Pupil-page `validate.py` also fails any object clipped by its svg. |
| L1 P1-22 | Third instruction line: "Code table: use the last box." |
| L4 licence and footer | Licence sentence and footer now agree: the footer reads "(c) 2026 Preciouslyours Pte Ltd. Photocopy licence. School (write name): ____ only. Not for resale." (or the school name when built with --school) and the licence sentence names that line. |
| Owner: entity and year | The (c) 2026 Preciouslyours Pte Ltd line prints on every pupil footer again in the normal build, and the licence page ends with the same line; "owner to confirm" removed. DRAFT stamps stay on cover, licence, teacher notes and both keys. The key footer is a separate short line ("Teacher answer key: not for pupils, not for resale") with the same (c) line. |
| Owner: registered office | `render.py` REG_OFFICE = 66 Tannery Ln, Singapore 347805 on the licence page; the DRAFT banner now lists only the licence term and the cover publisher line as still open. validate.py asserts the address. |

Still open (owner): publisher line on the cover, licence wording and term (lawyer), pupil trial, coin-art comparison, the star level of P1-39, and the CBC gallery diagram fixes.

## Round 3 (after `docs/audit_final/p1_semester_booklets_audit_round3.md`, no High)

validate.py: 783 checks, 0 failed; page counts unchanged. Changed pages viewed in colour and as 1-bit copies and re-solved by hand (P1-03, 05, 13, 21, 25, 39).

- **S2-01 nine-box code table:** digits and letters made smaller and the boxes respaced; all nine boxes now clear (viewed on P1-03, 13, 21, 25, 39, 05).
- **Grouping rings (P1-03):** the dashed ring now ends 0.6 mm before the next picture.
- **Blank box:** the teacher notes now say that a box left blank gives no letter and the check cannot see it (MONEY from MONKEY on S1-10 and CLOT from CLOTH on S1-01 are only reachable that way); the P1-21 note no longer claims the wrong operation never spells the word without that condition. The pages themselves were not changed.
- **Object margin:** counted pictures sized about 4% larger (apple 11.5, flower 10.9, star 9.6, ball 9.4, cat 10.2, drum 10.6, boat 10.9 mm cells), so every glyph is now about 8.3 mm or more rather than 8.0 to 8.1. P1-13 was regenerated (bag pitch 11.0 mm, totals from 6 to 16, new code table and key) to fit.
- **S1-04 marks:** NOT changed. Marks of 2.0 mm half-size (about 25% larger) were tried; every seed tried then produced a repeated question in the colour library (V2b), and 1.9 is the size at which the page is unique and clear. The marks in the check strip are larger, as before.

## Owner decisions after round 3

- **P39-TWO:** P1-39 Share and Group (S2-02) is now two stars on the page header, the contents table and the key. Semester 2 therefore has 9 one-star and 11 two-star pages (was 10 / 10); Semester 1 is unchanged at 10 / 10. validate.py now expects 10 / 10 for Semester 1 and 9 / 11 for Semester 2. No other page was changed; tell me if you want a two-star page swapped to one star to restore the balance.
- **PUBLISHER-OK:** both covers print "Preciouslyours Pte Ltd, trading as Math Inquirers".
- **LICENCE-ANNUAL:** the licence page has a Term section: an annual licence covering one school year, renewable; wording to be approved by a lawyer before any school receives the booklet. The DRAFT banner on the licence page now lists only the licence wording (lawyer approval) as open; the cover banner lists only that the cover wording and title are not final. validate.py asserts the publisher line, the annual licence sentence and the lawyer sentence (785 checks, 0 failed).

Items for the owner now still open: licence wording (lawyer approval), the final cover title wording, pupil trial, coin-art comparison, CBC gallery diagram fixes, and the one not-affiliated sentence (kept on the licence page only).
