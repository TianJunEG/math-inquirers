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

Each booklet is 10 one-star and 10 two-star pages. Footers print both numbers, for example `S1-07 (P1-08)`. All 32 syllabus outcome lines (wording copied from the PDF, now also in `docs/moe/syllabus_by_level.md`) are exercised by at least one page; validate.py checks this and that every tag number belongs to the page's own outcome ids.

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

- Titles and the working product names (Semester 1, Semester 2), the publisher line, entity, licence wording and term: all still DRAFT placeholders; the licence page covers one booklet only.
- Accept P1-34 and P1-32 as checked by matching, not by seeing the pupil's drawing, or ask for a different page.
- A pupil trial (4 to 6 children), ideally with P1-24 (domino route), P1-32 (rulers), P1-34 (copy), P1-37 (loop) and P1-17, P1-29 clocks, and a real photocopier test with crayons for the three colour pages.
- Whether the "problem solving" tag (P1-16, 22, 27, 28, 38, 39) and its teacher-note sentence are right; the key marks them.
- Ordinals: P1-24 reaches tenth; P1-07 still stops at fifth.
- Whether the one not-affiliated sentence stays on the licence page.
- Whether to draw the CBC gallery diagram fixes and the other B items of the diagram audit (not in this build).
- The independent audit (hand-solve at least the six pages named above, mono copy test, V9 non-copy check): the owner's next step, not run here.
