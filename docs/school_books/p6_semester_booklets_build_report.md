# Primary 6 semester booklets: build report (DRAFT)

Branch `claude/great-fermi-1hv4vc`. Pipeline `school/p6` (a P6 version of the audited P2 pipeline). Plan and gap analysis: `docs/school_books/p6_semester_booklets_plan.md`. Outcome wording: `docs/school_books/p6_outcome_wording.md`. Independent audit answered here: `docs/audit_final/p6_semester_booklets_audit.md`.

## What was built

- Two booklets, S1 (Terms 1 and 2) and S2 (Terms 3 and 4): 40 pupil pages (P6-01 to P6-40), 10 one-star and 10 two-star in each. Footer codes print both numbers, for example `S1-07 (P6-07)`.
- `school/p6/out/`: Puzzles, FrontMatter, Answer_Key and Complete_Pack PDFs for S1 and S2, `validation_report.txt`, `verification.json`, `similarity_report.txt`.
- `python3 validate.py` (final run after the last edit): **744 checks, 0 failed** (final run after the round-2 fixes; one new check compares the questions on each colour page with the key).
- `python3 similarity_check.py` against the private sources (gitignored; read for comparison only): 40 pages, 343 items, 11 848 private entries, **0 flags** (no 7-word run, no same scenario with the same numbers, no same sentence structure).
- Vendored, not shared: `school/p6/cbc_vendor` (copy of the colour-by-code library, with a P6 bank `banks_p6.py`, `p6_*` text rules and a larger blank box). No file in `school/colour_by_code`, `school/p1` or `school/p2` was edited.

## Audit fixes (second pass, 23 Oct 2026)

The audit had no High. Fixed:

- **M1 angle figures were to scale.** P6-27, 28, 29 are now drawn deliberately NOT to scale: each figure is stretched by a general linear map (straight lines stay straight, parallel lines stay parallel) or, for the square figures, the apex is moved; the unknown angle is drawn at least 9 degrees off (at least 7 degrees larger when it is under 30), no drawn angle is below 20 degrees, and no side is much shorter than it was. Every label stays true. The pages say "Not drawn to scale: work it out, do not measure." and the teacher note says so. The independent reader now reads the true geometry carried in the figure (data attributes), so it still checks the key against the construction; it no longer measures the drawn picture. The key line "drawn accurately" was removed.
- **M2 arch figures.** The square-with-semicircle figures (P6-20 O and E, P6-21 item 2, P6-22 item 4) now have a dimension line along the side and the word "square" inside.
- **M3 outcome numbers.** The syllabus PDF was supplied; every number on the key was checked against pages 43 and 44 and is right (see the plan). The key now says the outcome lines are quoted from the syllabus (2021 edition, updated October 2025) and the notes on each tag are our own words; the sentence that implied the numbers came from our summary was removed. Foundation-track lines carry the label Primary 6 Foundation.
- **M4 label collisions.** Arc labels and vertex letters are now placed by a search that keeps text clear of every line, tick and other label (the `?` sits next to its arc, the letter E is off AB, 43 is off the side, the 136 and 132 texts are off the diagonals).
- **Topic placement (PDF).** Nets (P6-34), rate (P6-35) and mixed numbers (P6-36) are not Primary 6 and were replaced by Fraction Order (FR1.1, FR1.2; ordering), Ratio Stories (RA1.2, RA1.3, RA1.6, RA1.7; code word, two stars) and Circle Choices (AV1.1, AV1.2; pi as 3.14; lettered choices). Pie charts (P6-33), decimals (P6-37), GST and discount (P6-38) and tank volume (P6-26) are Primary 6 Foundation lines and stay, tagged Primary 6 Foundation. Speed is not in the syllabus and is not used.
- **Lows.** P6-14, 19, 25 and 29 now say "Use each card once. Two cards are not used." (eight cards for six items); instructions on P6-21, 22, 27, 28, 29 shortened to at most 5 sentences; the cube-root sign is larger and bold (P6-24, 39; the domino version on P6-39 is still small); hatch lines 0.55 mm (were 0.35); colour-page boxes are about 10 mm (were 8.2 mm; see round 2); P6-26 tank dimensions changed (the 80 by 50 by 20 tank is gone); SPONGE is banned as a code word and P6-28 now spells WIZARD; key text slips (S1-13 note, S1-20 and S1-08 and S1-15 tag notes) corrected; P6-24 retitled Root Maze and tagged VO2.5 only (no cube-edge item); P6-36 adds a second 3.14 page (P6-18 and P6-36).
- **Round 2 (second audit, `docs/audit_final/p6_semester_booklets_audit_round2.md`; no High).**
  - M1 label association: arc labels are now placed inside their own wedge and the search requires the nearest arc to be the label's own; S2-07, 28 and 29 were redrawn and their answers changed with the new random figures (P6-27: 100, 116, 137, 46, 95, 75; P6-28: 37, 86, 38, 15, 75, 55; code words PEANUT and WIZARD unchanged).
  - L6: an acute given angle stays acute and an obtuse one obtuse in the drawing; the unknown angle is now drawn at least 9 degrees off for every item (the note says so and is true).
  - M2: the S2-01 item 4 figure and the hatched square figures now print "square 28 cm" under the figure.
  - M3: the key says the outcome numbers follow the syllabus and the notes are our own words (not "quoted"); the S2-09 note says the decoys are 180 minus the answers of two figures.
  - L1 colour-page boxes: the real cause was that the 9 mm setting was applied while building the pupil page only, so the pupil page and the key could show different questions (the key then showed other items). The box size is now set in the library copy for both, and a new validate check compares the questions on each colour page with the key. Printed answer boxes on the three colour pages are now about 10 mm (11.0 units; 11.8 and above does not fit the sun region of the car). The target of 11 to 12 mm was not reached. The earlier statement "9.0 mm" was wrong and is withdrawn. Colour pages re-rolled: S1-09, S2-12 and S2-20 were hand-solved again (P6-40 now uses picture seed 2 because seed 4 left one label touching an outline).
  - L3: cube-root index larger (P6-24); on the P6-39 dominoes it is the same larger sign.
  - L4 comma in the S2-02 instruction removed; L5 the S2-14 key prints mixed numbers as `1 1⁄3`; L9 the front matter says Foundation-track pages revise earlier-year content and are Foundation-track lines. Foundation-track pages (pie charts, decimals, GST, tank) are kept as Semester 2 revision (the auditor's judgement).
- **Not changed.** Single-slip list size: the single-slip test on code-table pages uses the 129 000-word list and the choice, matching and ordering pages the 207 399-word list; the teacher note says "about 207 000". Not aligned (L-G); the larger list was confirmed by the auditor's own 426 000-word test. The cover keeps "Almost every puzzle checks itself" (a blank box is not seen by the check). P6-18 item 2 keeps its 43.96 / 6.28 step (a calculator may help). The code-word pages were not converted to other mechanisms (auditor's advice).

## Page table

| Page | Title | Stars | Outcomes | Mechanism |
|---|---|---|---|---|
| S1-01 (P6-01) | Fraction Shares | 1 | FR1.1 | Code-breaker |
| S1-02 (P6-02) | Dividing by Fractions | 1 | FR1.2 | Maze / path |
| S1-03 (P6-03) | Fraction Stories | 2 | FR1.1, FR1.2 | Choice table |
| S1-04 (P6-04) | Equal Ratios | 1 | RA1.1, RA1.2, RA1.4 | Matching |
| S1-05 (P6-05) | Missing Terms | 1 | RA1.2, RA1.6 | Code-breaker |
| S1-06 (P6-06) | Share in a Ratio | 1 | RA1.3, RA1.5 | Code-breaker |
| S1-07 (P6-07) | Three Quantities | 2 | RA1.1, RA1.4, RA1.5 | Code-breaker |
| S1-08 (P6-08) | Fractions and Ratios | 2 | RA1.7, RA1.5 | Choice table |
| S1-09 (P6-09) | Colour the Car | 2 | RA1.2, RA1.3, RA1.6, PC1.1, PC1.2 | Colour by code |
| S1-10 (P6-10) | Find the Whole | 1 | PC1.1 | Code-breaker |
| S1-11 (P6-11) | Percent Up and Down | 1 | PC1.2 | Maze / path |
| S1-12 (P6-12) | Percent Stories | 2 | PC1.1, PC1.2 | Code-breaker |
| S1-13 (P6-13) | Letters for Numbers | 1 | AL1.1, AL1.2 | Choice table |
| S1-14 (P6-14) | Simplify | 1 | AL1.3 | Matching |
| S1-15 (P6-15) | Substitute | 2 | AL1.4, AL1.2 | Domino loop |
| S1-16 (P6-16) | Find the Letter | 2 | AL1.5, AL1.3 | Code-breaker |
| S1-17 (P6-17) | Round and Round | 1 | AV1.1 | Code-breaker |
| S1-18 (P6-18) | Circle Areas | 2 | AV1.1 | Code-breaker |
| S1-19 (P6-19) | Half and Quarter | 2 | AV1.2 | Matching |
| S1-20 (P6-20) | Curves and Corners | 2 | AV1.3, AV1.2 | Ordering |
| S2-01 (P6-21) | Shaded Shapes | 1 | AV1.3 | Code-breaker |
| S2-02 (P6-22) | Perimeter Pick | 2 | AV1.2, AV1.3 | Choice table |
| S2-03 (P6-23) | Cuboid Corners | 1 | VO2.1 | Code-breaker |
| S2-04 (P6-24) | Root Maze | 1 | VO2.5 | Maze / path |
| S2-05 (P6-25) | Base and Height | 2 | VO2.3, VO2.4, VO2.2 | Matching |
| S2-06 (P6-26) | Tank Stories | 2 | VO2.3, PF.VO | Code-breaker |
| S2-07 (P6-27) | Angles in Figures | 1 | GE1.1 | Code-breaker |
| S2-08 (P6-28) | More Angles | 2 | GE1.1 | Code-breaker |
| S2-09 (P6-29) | Angle Match | 1 | GE1.1 | Matching |
| S2-10 (P6-30) | Average | 1 | ST1.1 | Code-breaker |
| S2-11 (P6-31) | Missing Value | 2 | ST1.2 | Code-breaker |
| S2-12 (P6-32) | Colour the Butterfly | 2 | VO2.1, VO2.2, VO2.3, ST1.1, ST1.2 | Colour by code |
| S2-13 (P6-33) | Pie Chart | 2 | PF.ST, PF.PC | Code-breaker |
| S2-14 (P6-34) | Fraction Order | 1 | FR1.1, FR1.2 | Ordering |
| S2-15 (P6-35) | Ratio Stories | 2 | RA1.2, RA1.3, RA1.6, RA1.7 | Code-breaker |
| S2-16 (P6-36) | Circle Choices | 1 | AV1.1, AV1.2 | Choice table |
| S2-17 (P6-37) | Decimal Maze | 1 | PF.DE | Maze / path |
| S2-18 (P6-38) | GST and Discount | 1 | PF.PC | Code-breaker |
| S2-19 (P6-39) | Mixed Bag | 2 | FR1.2, RA1.3, AL1.4, ST1.1, VO2.5, PF.PC, PF.VO | Domino loop |
| S2-20 (P6-40) | Colour the Elephant | 2 | PF.PC, FR1.2, AL1.4, AL1.5, RA1.3, ST1.1 | Colour by code |

## Hand-solve

- First pass: all 40 pages solved by hand from the rendered images (1-bit, 100 dpi) and compared with the keys: 40 of 40 agreed.
- After the audit fixes the changed pages were re-solved from the new renders: **15 pages** (and, in round 2, S2-07, 08, 09 and the three colour pages again) (S1-12, S1-20, S2-01, 02, 04, 06, 07, 08, 09, 10, 11, 13, 14, 15, 16; the code words that moved are S2-06 NUMBER, S2-08 WIZARD, S2-10 FABRIC, S2-11 DONKEY, S2-13 FIGURE; the three new pages spell FAMILY, MAGNET and SHADOW) and all 15 matched the key. The three colour pages and S2-19 were viewed again; the other 22 pages are unchanged in content since the first pass. Total hand-solved on the final content: 40 of 40 (25 from the first pass, 15 re-solved).
- Layout checks: every changed page was viewed in 1-bit; the angle pages and the arch figures in colour as well.

## Weak points

1. Angle figures are not to scale, so a few look odd (P6-28 item 4, P6-29 item 4); this is by design and the page says so.
2. The cube-root sign on dominoes (P6-39) is still small.
3. About half the pages (19 of 40) use the code-word mechanism.
4. The check cannot see a blank box, and two wrong answers at once were not all tested.
5. P6-39 and P6-40 mix topics; the key tags them as problem solving.
6. Photocopier test and a pupil trial have not been done.
7. Two-step equations (P6-16): the syllabus line does not say how many steps; keep or limit to one step.

## Decisions for the owner

1. The replaced pages (P6-34, 35, 36) are new and are the owner's to approve.
2. Foundation-track pages (pie charts, decimals, GST, tank volume) are in the Standard booklets and tagged Primary 6 Foundation. Keep, or replace them with more Standard content (ratio, circles)?
3. P6-07 (linking two ratios) kept as a two-star page.
4. GST 9% (the current Singapore rate).
5. Pi: 22/7 on 5 pages, 3.14 on 2 (P6-18, P6-36). More 3.14 pages are possible.
6. Lawyer hold: licence wording is a placeholder. Contact email pypteltd@gmail.com is the business email for now. Registered office 66 Tannery Ln, Singapore 347805.
7. Pupil trial and photocopier test before release.
