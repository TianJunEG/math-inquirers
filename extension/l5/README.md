# Level 5 Extension Workbook: author notes for the audit

Built 23 Oct 2026 by the Level 5 author agent with the Level 1 pipeline (`extension/tools/build.py --level 5`). Ages 10-12, self-study, answers inside the book, black-and-white print edition plus colour soft copy. No price, no MOE / GEP / SASMO claim, no tutor or class dependence. Pushed to claude/great-fermi-1hv4vc.

## Files owned by Level 5

| Path | What |
|---|---|
| `extension/data/l5_u01.json` ... `l5_u10.json` | the 10 units (Learn it with worked example, how-to and Try; Start here 11-14 items; Think harder 3; Go further 3-4; Check yourself 4) |
| `extension/verify/l5_uNN_checks.py` | independent answer checks, one function per item (see "Answer checks") |
| `extension/tools/figs_l5_core.py` | figure types `l5_cards`, `l5_table`, `l5_numline`, `l5_bars`, `l5_grid100`, `l5_clues` |
| `extension/tools/figs_l5_geom.py` | `l5_poly`: triangles, quadrilaterals, grids, angle arcs, right-angle marks, side labels (all drawn to scale from coordinates) |
| `extension/tools/figs_l5_solid.py` | `l5_solid` (tanks, water, blocks, cuboids), `l5_cubes` (isometric cubes) |
| `extension/tools/figs_l5_pat.py` | `l5_pat` (matchstick, tile, dot and chair patterns) |
| `extension/l5/` | this file, `PROGRESS.md`, `TOOL_REQUESTS.md` |
| `outputs/extension/L5/` | the PDFs and `build_report.json` |

All type names start with `l5_` so they cannot clash with another level's plug-ins. No shared file was edited.

## Units and the holiday lesson each follows

| Unit | Title (book) | Holiday lesson | Items | Beyond items (label "Beyond Level 5: ...") |
|---|---|---|---|---|
| 1 | Big number puzzles | 1 Million puzzles | 26 | G1 counting choices |
| 2 | Fractions at work | 2 Fraction feats | 26 | G1 dividing a fraction, G4 a sum that collapses |
| 3 | Change and compare | 3 Before and after | 26 | none |
| 4 | Half the box | 4 Triangle areas | 23 | G3 corner triangles |
| 5 | Fill it up | 5 Volume vault | 25 | G1 cubes with tunnels |
| 6 | Rates and deals | 6 Rate racers | 25 | G1 average rate |
| 7 | Out of 100 | 7 Percentage puzzles | 25 | T2 working back from a percentage, T3 a charge in the total, G1 two rises in a row, G2 boiling away |
| 8 | Chase the angle | 8 Angle chasers | 23 | G1 angles of a regular pentagon, G2 clock angles |
| 9 | Rules for patterns | 9 Pattern generalisers | 22 | G1 adding a pattern, G2 handshakes |
| 10 | Pick a start | 10 Challenge day | 23 | G3 the worst case |

244 items in all (the count includes the Try on each Learn it page). Start here has 11 to 14 items instead of 13 to 14 in the geometry, pattern and logic units because their figures are large (see "Space"). Percentage increase or decrease and finding the whole from a percentage (P6 in the holiday spec) appear only as beyond items on Think harder / Go further. No ratio notation, speed, circles, negative numbers or algebra letters are used.

## Type map: what each unit mirrors, and what is new

1. Place value and words, rounding, digit cards (greatest, smallest, multiple of 5), closest to a target (both sides), digit riddle by clues, estimate to catch wrong answers, one pair of brackets, a "find all" range after rounding, large-number word problems. New numbers, new riddles (all riddle solutions are unique by search), new contexts (towns, stadium, factory, printing press).
2. Fraction as division, comparing by the shortfall, fraction of a quantity, unlike denominators, fraction of a remainder forwards and backwards (bar model), sum of two different unit fractions (test in order, stop when under half), number-line mixed numbers, digit cards for the greatest and smallest sum, patterns of fractions.
3. Before and after: total stays the same (give and take), difference stays the same (equal gifts, ages), one amount stays the same (beads, jar), "fraction as many as", fraction of a remainder backwards. All with bar models.
4. Triangle area with the right height (slanting sides as decoys), same base and same height, missing base or height, composite shapes, shaded areas by taking away, outside height, grid triangles, listing base-height pairs.
5. Cuboid volume by layers, litres and cm3, water depth and volume, water added or removed, stone displacement, packing cubes that cannot be cut, painted cubes, pouring between tanks, block standing in a tank, filling with a leak, cuboid from three face areas.
6. Rate tables, cost of one, better buy (same number of items or cost of one), taps and printers working together with a leak, "each extra 30 minutes or part of it", two plans compared, rate from a drip, doing a job together (pretend amount).
7. Percent from the hundred grid and bars, 10 percent / 5 percent / 1 percent building, discount then 9 percent GST on the reduced cost, percentage of a remainder, second-item-half-cost against a discount, the up-then-down trap, comparing marks.
8. Angle chasing with reasons: straight line, point, vertically opposite, triangle sum, isosceles, equilateral, parallelogram, rhombus, trapezium, all cases of an isosceles triangle, reasons to circle, clock angles.
9. Growing patterns (matchstick hexagons, plus-shaped tiles (Learn), U-shaped tiles, tables and chairs, double staircases, L-layers), the rule in words, far figures and backwards, number patterns, guess and check with a table, supposition (legs), marks with a penalty, adding a pattern.
10. Logic grids (worked example and a 4 by 4), working backwards (number and fraction versions), two numbers from a sum and a difference, counting squares and rectangles by size, who is lying, age difference, supposition, systematic listing, digit counting, worst-case thinking.

Same skills as the holiday program, with new numbers and contexts. After three audit rounds the items whose story, question and numbers matched a holiday item were replaced with new frames (each audit's class B list was checked against the holiday lines in `p5/content`). Many items are still "same type, new numbers" (class A): that is the design, and the Welcome text promises only new numbers and stories.

## Answer checks (`verify/l5_uNN_checks.py`)

Every item and every part has a function that recomputes the answer without reading the book:
- number units: exact `Fraction` arithmetic, brute force over all numbers or all permutations (digit riddles, cards, bracket placements, closest-to-target);
- geometry (units 4 and 8): figures are constructed from the data in the question (coordinates, rays, equal sides, parallel sides) and the asked length, area or angle is measured with the shoelace formula, point-to-line distance or `atan2`; no angle fact is used to get an answer;
- solids (unit 5): cubes are counted, painted cubes simulated, tunnels removed cell by cell;
- patterns (unit 9): each figure is built and its sticks, tiles or chairs counted; "which figure" is a search;
- logic and counting (unit 10): every permutation or case is tried.

`extension/verify/run_checks.py --level 5`: 10 unit files, 416 answers checked, 0 problems.

## Gates (all run on this build)

| Gate | Result |
|---|---|
| answers | 416 answers, 0 mismatches |
| duplicates (`dup_check.py --level 5`) | 0 shared 7-word runs with the holiday program or the private source texts; the skeleton REVIEW list was read: 52 lines, all "same sentence form, new numbers" (for example the sharing question, backwards money, tank base and water depth; the list was re-read after the audit fixes); none is a reworded holiday question |
| wording | 0 errors |
| black and white | print PDF: 0 colour pixels, no flat grey (the soft copy is colour) |
| fill and overflow | every unit page between 0.85 and 1.00 of the body, no overflow |
| pages | print 100 pages (even), soft copy 99; contents and answer page numbers come from the build |

## Choices and workarounds (shared tools not edited)

- Beyond items use the item key `beyond` (the renderer now prints "Beyond Level 5"). The Welcome text comes from `levels.json` (no ruler line for Level 5).
- `wording_lint.py` treats "ten thousands" and "two hundred" as quantities written as words. Level 5 writes "ten-thousand" with a hyphen in place-value names and uses numerals in "write the number" items.
- Titles in the book are child-facing ("Half the box"); the holiday lesson title is in the contents line ("Triangle areas") and the "follows Holiday Program Lesson N" line.
- Items inside a unit are numbered in page order; the generators sort by page and the checks use the same ids.
- Money is written with decimals ($0.70, $4.40); cents only in coin questions ("20¢ coins"). 9 percent GST is used as in the holiday program.
- The word "price" and "sale" are not used (the linter bans them); the text says "cost", "discount", "reduced cost".

## Space and the print rules

- Geometry, solid and pattern figures use fixed scales (`mm` per unit) so lengths on paper are proportional; labels are at least 10 pt (the figure renderer raises small text). Pattern tiles and sticks are 7 to 8 mm; chairs in the table pattern and the 1 cm grid cells in two area items are about 5 mm (a deliberate trade for page space; list in "Open points").
- Hatching (print) replaces yellow; water is drawn with wave lines, not shading; text labels have a white halo so a label that crosses a line stays readable in print. Nothing is meant by colour alone: shaded parts are also named in the text or by letters.

## Changes after the independent audit (`AUDIT.md`)

- H1: the Why lines of unit 9 were shifted because the short Whys were applied before the items were renumbered; fixed in the generator (the override now runs after renumbering). All 244 Whys were re-read against their items.
- H2: about 45 items were replaced or reframed (units 1 to 10), with new numbers, contexts and checks. Closest cases were changed first (unit 9 staircase, unit 5 container, painted cubes, tank floors, block and face areas, unit 3 Siti items, unit 6 printers and parking, unit 7 shoes and gift, unit 10 age and logic items).
- H3: unit 9 Start here 5 is now a U-shaped pattern (rule 3 x figure + 2, figure with 98 tiles); the Learn page keeps the plus sign.
- Learn pages: unit 9 has a supposition box, unit 8 a Reasons box with isosceles, parallelogram and trapezium facts, units 1, 2, 5 and 6 have one more box line (rounding 5, fraction of a fraction, pouring and packing, teams and leaks).
- Answer boxes: `{bw}` is used for mixed numbers, money with cents, 14 400 and sport names.
- Ambiguities: unit 4 base and height pairs, unit 2 mixed-number and simplest-form requests, "Read" instead of "Mark", unit 1 "do not join digits".
- Give-aways removed: the drawn construction lines in unit 4 Go further 3 and unit 8 Think harder 3, the pre-cut bars in units 2 and 3, hints that stated the whole method (now start-only).
- Figures: unit 4 Start here 1, 5 and Check yourself 1, unit 8 Start here 1, 6, 7, Go further 3 and Check yourself 4 were redrawn or relabelled.
- The letter n is no longer used in unit 9.

## Changes after audit round 2 (`AUDIT_ROUND2.md`)

- R1 to R3 fixed: unit 3 Start here 6 (counters, fraction given, some removed), unit 9 Start here 5 (U shape, rule 5 x figure + 2, 92 tiles), unit 4 Start here 9 (triangle and rectangle, 15 by 8 and 5 wide).
- R4: about 17 more items got a new frame as well as new numbers: unit 2 S06; unit 3 T01, T02; unit 4 S06(b), C02; unit 5 S13, G03; unit 6 S13, T03; unit 7 S13, T02, G01, G02; unit 9 G03; unit 10 S06 (prize boxes), S07, S12. Items that remain "same skill, new numbers" are listed as class A in the audits; the Welcome text promises only new numbers and stories.
- Figures: unit 4 Start here 1 redrawn (isosceles 12 by 8 and 14 by 12), unit 8 Start here 6 now asks angle BCD (no label collisions), Go further 3 no longer shows a tick pattern that claims DB = AC, the unit 8 Try labels moved, unit 4 Check yourself 1 right-angle mark smaller. Unit 9 Start here 5 uses tiles of 6.6 mm (page space).
- Learn: unit 9 has a worked supposition example and a marks-and-penalty line; unit 8 names the rhombus.
- Whys: unit 1 S12 lists all three pairs, unit 1 T01 has no letter variable, unit 4 C03 uses only the 4 cm shown. Unit 7 T03 is back to 9 percent GST ($545). Unit 2 G04 now has the Beyond label. Unit 10 S03 lost the redundant clue.


## Changes after audit round 3 (`AUDIT_ROUND3.md`)

- New frames (holiday lines read first): unit 4 S01 (triangles 18 by 12 and 25 by 12) and S06 (parallelogram 16 by 9), S09 (metres and centimetres); unit 5 G03 (cube volumes) and T03 (wall lifted out of a tank); unit 6 T03 (fuel, supposition); unit 7 S13 (percent of the whole from a part), T03 (service charge), G01 (two rises), G02 (salt water); unit 8 C01 (OD halves an angle); unit 3 S12 (parts of money).
- Unit 4 Check yourself 3 no longer hatches the triangle, so the dashed height shows; the Learn Reasons box in unit 8 has the equilateral line and a clearer trapezium line; the unit 9 marks line says "costs its marks plus the penalty"; unit 10 S12 reads "greater than".

1. Page count is 100 after shortening about 140 Why lines (owner decision L5-TRIM). The Why texts are now very short; some units explain less than the holiday program does.
2. Child trial and a cold read audit have not been done for Level 5. The hints are one line of at most 68 characters (checked); the Go further and Think harder difficulty is untested with children.
3. Objects under 8 mm: chairs in the unit 9 tables item (5 mm), the tiles of unit 9 Start here 5 (6.6 mm), the grid squares in the unit 4 grid items (3.9 and 4.0 mm cells, 1 cm squares) and the unit 10 grids (5.3 mm cells), the matchstick hexagons in the Try. All are legible at print size.
4. The printer proof and the 600 dpi 1-bit file (Print_BW.pdf) are produced by the shared build; the dotted grid and the hatching have only been checked at 200 dpi (`bw_check.py`) and by `print/check_bw.py`.
5. `verify_all.sh 5` was not used as a whole because its black-and-white step scans every level's output; the same steps were run one by one for Level 5.
