# Primary 6 semester booklets: build report (DRAFT)

Branch `claude/great-fermi-1hv4vc`. Pipeline `school/p6` (a P6 version of the audited P2 pipeline). Plan and gap analysis: `docs/school_books/p6_semester_booklets_plan.md`. Outcome wording: `docs/school_books/p6_outcome_wording.md`.

## What was built

- Two booklets, S1 (Terms 1 and 2) and S2 (Terms 3 and 4): 40 pupil pages (P6-01 to P6-40), 10 one-star and 10 two-star in each. Footer codes print both numbers, for example `S1-07 (P6-07)`.
- `school/p6/out/`: `P6_S1_Puzzles.pdf`, `P6_S2_Puzzles.pdf`, `P6_S1_FrontMatter.pdf`, `P6_S2_FrontMatter.pdf`, `P6_S1_Answer_Key.pdf`, `P6_S2_Answer_Key.pdf`, `P6_S1_Complete_Pack.pdf`, `P6_S2_Complete_Pack.pdf`, `validation_report.txt`, `verification.json`, `similarity_report.txt`.
- `python3 validate.py`: 744 checks, 0 failed (final run, after the last edit).
- `python3 similarity_check.py` against the private sources (gitignored; read for comparison only): 40 pages, 342 items, 11 848 private entries, 0 flags (rules: no 7-word run, no same scenario with the same numbers, no same sentence structure). Earlier runs flagged four generic sentences (P6-03, P6-10 x2, P6-12); they were reworded. The report holds counts only, no private text.
- Vendored, not shared: `school/p6/cbc_vendor` (copy of the colour-by-code library with a P6 bank `banks_p6.py` and `p6_*` text rules). No file in `school/colour_by_code`, `school/p1` or `school/p2` was edited. No library change is wanted.

## Source limit (plain statement)

The Ministry of Education syllabus PDF is **not in the repository**. Outcome wording beyond `docs/moe/syllabus_by_level.md` cannot be copied or verified here. The outcome ids and the Ratio 1.1 to 1.7 order come from our own summary of that file; check them against the PDF before any claim is printed.

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
| S2-04 (P6-24) | Roots and Edges | 1 | VO2.5, VO2.2 | Maze / path |
| S2-05 (P6-25) | Base and Height | 2 | VO2.3, VO2.4, VO2.2 | Matching |
| S2-06 (P6-26) | Tank Stories | 2 | VO2.3, RV5.VO | Code-breaker |
| S2-07 (P6-27) | Angles in Figures | 1 | GE1.1 | Code-breaker |
| S2-08 (P6-28) | More Angles | 2 | GE1.1 | Code-breaker |
| S2-09 (P6-29) | Angle Match | 1 | GE1.1 | Matching |
| S2-10 (P6-30) | Average | 1 | ST1.1 | Code-breaker |
| S2-11 (P6-31) | Missing Value | 2 | ST1.2 | Code-breaker |
| S2-12 (P6-32) | Colour the Butterfly | 2 | VO2.1, VO2.2, VO2.3, ST1.1, ST1.2 | Colour by code |
| S2-13 (P6-33) | Pie Chart | 2 | RV4.ST, RV5.PC | Code-breaker |
| S2-14 (P6-34) | Net or Not | 1 | RV4.NET | Choice table |
| S2-15 (P6-35) | Taps and Rates | 2 | RV5.RA, RV5.VO | Code-breaker |
| S2-16 (P6-36) | Mixed Numbers | 1 | RV5.FR | Ordering |
| S2-17 (P6-37) | Decimal Maze | 1 | RV4.DE | Maze / path |
| S2-18 (P6-38) | GST and Discount | 1 | RV5.PC | Code-breaker |
| S2-19 (P6-39) | Mixed Bag | 2 | FR1.2, RA1.3, AL1.4, ST1.1, VO2.5, RV5.PC, RV5.VO | Domino loop |
| S2-20 (P6-40) | Colour the Elephant | 2 | RV5.PC, FR1.2, AL1.4, AL1.5, RA1.3, ST1.1 | Colour by code |

## Hand-solve

All 40 pages were solved by hand from the rendered images of the final build (1-bit, 100 dpi, as a photocopy would be) and then compared with the answer keys: **40 of 40 solved and 40 of 40 matched the key** (code words: CREAMY, MONKEY, TEACUP, BANDIT, DEVOUR, FATHOM, FRUITY, SQUARE, STUDIO, WALRUS, BOTANY, CRAFTY, COUSIN, FROZEN, HUNGRY, POLICE, SUNDAY, WALNUT, COUGAR, CANOPY, MAGNET, PEANUT, SPONGE, STRONG, CURFEW, FABRIC, DONKEY, FAMILY, NUMBER, SHADOW, TURKEY, WOMBAT, SHRIMP (P6-04); the four routes, the three colour pages and the P6-33/34 chart and net pages were checked cell by cell, counts and mirror colours included). Earlier hand-solve passes found and fixed content errors (pronouns, a degenerate item, an angle of exactly 90 degrees, label clipping, a maze without its trap cells, repeated values); the final pass found none. Two solver-vs-page checks were also done by script (independent `calc()` on printed text, angle, pie and net readers; the net reader folds a rolling cube and finds exactly 11 nets).

Layout checks done on every page, in colour and as a 1-bit simulation: no flat grey, no tiny text, answer boxes at least 12 mm high with enough width, figures clear. The final code words were frozen before the solve; do not change any page text without re-solving (code words move when upstream pages change).

## Weak points

1. P6-20, P6-21, P6-22: the square-with-semicircle figures show one number inside the square (its side). It is read as the side, and the semicircle diameter equals the side; a pupil may need the teacher to say so.
2. P6-27, P6-28, P6-29: angles are drawn to scale, so a pupil could measure. The page says "Do not measure" but cannot stop it.
3. P6-33 (pie chart) and P6-34 (nets) and P6-35 (rate) are not Primary 6 outcomes in our syllabus summary; the brief listed them. Treated as revision of Primary 4 and 5.
4. About half the pages (19 of 40) use the code-word mechanism, so the book can feel repetitive. More conversions are possible.
5. Answer-box sizes on dense pages (P6-09, 32, 40 colour pages; P6-07) are at the minimum.
6. The check cannot see a blank box, and two wrong answers at once were not all tested.
7. P6-39 and P6-40 mix topics ("problem solving") and carry several outcome tags; the key tags them as such.
8. Trapezium angles on one line (co-interior angles between parallel lines, P6-27 item 1 and 6, P6-29 item 3) are treated as a Primary 5 property.
9. Photocopier test and a pupil trial have not been done.

## Decisions for the owner

1. Speed, pie charts and nets: the brief named them, but they are not Primary 6 outcome lines in our summary (speed is Primary 7 in some schemes). Keep as revision pages, or replace with Primary 6 content (more circles, ratio problem solving)? No page uses speed.
2. Ratio numbering 1.1 to 1.7 follows our summary's list order and is unverified against the PDF.
3. The page that links two ratios (P6-07, two stars) is treated as problem solving within RA1.5; confirm it is wanted.
4. GST is 9% (the current Singapore rate); money pages use $ and decimals.
5. Value of pi: each page states 3.14 or 22/7 and never both. Confirm that the pairing (22/7 where the radius or diameter is a multiple of 7) is acceptable.
6. Coin pages are absent (none is needed at Primary 6).
7. Lawyer hold: licence wording is a placeholder and must be approved before any school receives a booklet. Contact email pypteltd@gmail.com is the business email for now. Registered office 66 Tannery Ln, Singapore 347805.
8. Whether to convert some code-word pages to other mechanisms (see weak point 4).
9. Pupil trial and photocopier test before release.

## Uncertain

- The syllabus wording (see the source limit). The pipeline's slip test counts a wrong answer as rejected unless it spells one of about 207 000 words; very rare double slips were not tested.
