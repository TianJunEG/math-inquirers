# Level 5 Extension Workbook: author notes for the audit

Built 23 Oct 2026 by the Level 5 author agent with the Level 1 pipeline (`extension/tools/build.py --level 5`). Ages 10-12, self-study, answers inside the book, black-and-white print edition plus colour soft copy. No price, no MOE / GEP / SASMO claim, no tutor or class dependence. Not pushed.

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
| 2 | Fractions at work | 2 Fraction feats | 26 | G1 dividing a fraction |
| 3 | Change and compare | 3 Before and after | 26 | none |
| 4 | Half the box | 4 Triangle areas | 23 | G3 corner triangles |
| 5 | Fill it up | 5 Volume vault | 25 | G1 cubes with tunnels |
| 6 | Rates and deals | 6 Rate racers | 25 | G1 average rate |
| 7 | Out of 100 | 7 Percentage puzzles | 25 | T2 working back from a percentage, T3 GST in the cost, G1 percentage change |
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
7. Percent from the hundred grid and bars, 10 percent / 5 percent / 1 percent building, discount then 9 percent GST on the reduced cost, percentage of a remainder, buy-2-get-1-free against a discount, the up-then-down trap, comparing marks.
8. Angle chasing with reasons: straight line, point, vertically opposite, triangle sum, isosceles, equilateral, parallelogram, rhombus, trapezium, all cases of an isosceles triangle, reasons to circle, clock angles.
9. Growing patterns (matchstick hexagons, plus-shaped tiles, tables and chairs, staircases, L-layers), the rule in words, far figures and backwards, number patterns, guess and check with a table, supposition (legs), marks with a penalty, adding a pattern.
10. Logic grids (worked example and a 4 by 4), working backwards (number and fraction versions), two numbers from a sum and a difference, counting squares and rectangles by size, who is lying, age difference, supposition, systematic listing, digit counting, worst-case thinking.

No holiday question is repeated. Numbers, contexts and often the question are different even where the type is the same.

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
| duplicates (`dup_check.py --level 5`) | 0 shared 7-word runs with the holiday program or the private source texts; the skeleton REVIEW list was read: 52 lines, all "same sentence form, new numbers" (for example the sharing question, backwards money, tank base and water depth); none is a reworded holiday question |
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

## Open points for the owner or the next agent

1. Page count is 100 after shortening about 140 Why lines (owner decision L5-TRIM). The Why texts are now very short; some units explain less than the holiday program does.
2. Child trial and a cold read audit have not been done for Level 5. The hints are one line of at most 68 characters (checked); the Go further and Think harder difficulty is untested with children.
3. Objects under 8 mm: chairs in the unit 9 tables item, the grid squares in two unit 4 items, the matchstick hexagons in the Try (all 5 mm or more).
4. The printer proof and the 600 dpi 1-bit file (Print_BW.pdf) are produced by the shared build; the dotted grid and the hatching have only been checked at 200 dpi (`bw_check.py`) and by `print/check_bw.py`.
5. `verify_all.sh 5` was not used as a whole because its black-and-white step scans every level's output; the same steps were run one by one for Level 5.
