# Level 4 Extension Workbook: audit-ready notes

Self-study extension workbook for ages 9 to 11, 10 units that follow the 10 Level 4 holiday lessons (`p4/content/l1.js` to `l10.js`), built with the Level 1 pipeline in `extension/`. Plan and spec: `docs/extension_books/plan.md`. Progress and resume point: `PROGRESS.md`. Tool changes asked for: `TOOL_REQUESTS.md` (none made).

## Files (all owned by Level 4)

| Path | What |
|---|---|
| `extension/data/l4_u01.json` to `l4_u10.json` | the 10 units (generated; do not edit by hand) |
| `extension/l4/src/uNN.py`, `lib.py`, `fold.py` | the unit sources that write the JSON (`python3 extension/l4/src/u05.py`), authoring helpers, and a cube-net folding helper used in Unit 8 |
| `extension/verify/l4_uNN_checks.py` | independent answer checks, one per unit |
| `extension/tools/figs_l4_core.py` | tables, bar models (with braces), number lines, cell grids, number-machine flows |
| `extension/tools/figs_l4_geom.py` | angles, protractor, fan of rays, 8-point compass, clock faces, split corners |
| `extension/tools/figs_l4_area.py` | shapes with square corners on a grid (labels, dashed cuts, frames), tile shapes, cube nets |
| `extension/tools/figs_l4_data.py` | line graphs (one or two lines, one or two panels with their own scales) |
| `outputs/extension/L4/` | the two PDFs and `build_report.json` |

## Content per unit

Item counts include 4 Check yourself items; each unit also has a worked example, a second worked example, a How-to box, a facts box and a "Your turn" try item (all answered at the back). "Beyond" items carry the first line "Beyond Level 4: <name>" (the shared `beyond` key prints "Beyond Level 1", see TOOL_REQUESTS.md) and sit only in Think harder or Go further.

| Unit | Title | Start / Think / Go / Check | Beyond item |
|---|---|---|---|
| 1 | Factor Hunters | 13 / 3 / 4 / 4 | G02 three common multiples |
| 2 | Big Number Puzzles | 13 / 3 / 4 / 4 | G02 counting by place |
| 3 | Operation Detectives | 12 / 3 / 3 / 4 | T01 order of operations, G01 signs and brackets (order of operations is a P5 preview in the holiday spec) |
| 4 | Fraction Frontier | 13 / 3 / 4 / 4 | G02 unit fractions |
| 5 | Decimal Detectives | 12 / 3 / 4 / 4 | none |
| 6 | Angle Turns | 10 / 3 / 4 / 4 | T01 angles on a line and at a point |
| 7 | Area Architects II | 9 / 3 / 4 / 4 | none |
| 8 | Symmetry and Nets | 10 / 3 / 3 / 4 | G01 painted cubes |
| 9 | Data Detectives | 8 / 3 / 3 / 4 | G03 average |
| 10 | Puzzle Day | 12 / 3 / 4 / 4 | G04 number cycles |

229 items with a try item each; about 420 separately checked answers. Units 6 to 9 have 8 to 10 Start here items instead of 13 because their figures (protractor, nets, grids, graphs) are large; the pages are as full as the fill gate allows (see "Page budget").

Type map (holiday lesson type, then what the Start here items do with new numbers and contexts):
1. Factor pairs in order, common factors (bags), common multiples (buses, lamps, packs), exactly-3-factor numbers (odd number of factors), multiple riddles. Think harder: digit riddle, left-over riddle, gears.
2. Rounding to 10, 100, 1000 with number lines, smallest and largest that round to a value, estimating, digit riddles, digit-card puzzles, number patterns. Think harder: closest to a target, bounds of a sum, distinct-digit bounds.
3. Multi-digit operations, estimating, multi-step stories, "times as many" and "more than" bar models, working backwards through machines, a number trick, sum chains. Order of operations only as labelled beyond items.
4. Improper fractions and mixed numbers (bars, number line), fraction of a set and whole from a part (bar models), comparing and ordering unlike fractions, equivalent fractions. Think harder: riddle, two fractions of a whole, fraction of the rest.
5. Zooming number lines (0.1, 0.01, 0.001), comparing and ordering, place value, rounding and rounding backwards, money and mass with bar models.
6. Measuring and reading a protractor, a fan of rays, 8-point compass turns and reversing a turn, clock angles, minute hand degrees, corners of rectangles.
7. Composite figures (missing sides, split or take away, push the steps out), fixed area with several perimeters, tiles, cutting and rearranging, frames and borders.
8. Which nets fold into a cube, opposite faces and dice nets, completing symmetric figures, lines of symmetry, shading one more square.
9. Reading line graphs and the scale, greatest increase and decrease, missing values in tables with totals, two lines on one graph, graphs whose scales mislead, equal steps.
10. Guess and check with a table, suppose all the same (heads and legs), working backwards, logic grid, queues, ages.

## How the rules were met

- **Original problems.** Every item was written for this book from the lesson types only. `extension/verify/dup_check.py --level 4` passes (no shared 7-word run with `p4/` or with the private external texts). The REVIEW list (same sentence skeleton with other numbers) was read: all remaining entries are stock command skeletons such as "write all the factors of # in order", "round # to # decimal place", "use the digit cards # # #", "a number that rounds to # #" or "a rectangle has an area of #"; they are the same question TYPE with new numbers and contexts, which is the product brief. No item was kept whose numbers or story match a holiday item (several first drafts were rewritten because they matched holiday numbers or stories, for example a lockers puzzle, packs of 36 pencils and 48 rubbers, and the 3-4-5-6 chain numbers).
- **No claims, no price, no tutor.** `wording_lint.py` bans MOE, GEP, SASMO, PSLE, syllabus and price words; there is no tutor or class reference. Contact and licence text are produced by the build (not edited).
- **Answers.** Each answer was solved by hand while writing and then recomputed by `l4_uNN_checks.py` (no copying of the book value): arithmetic by Python, unknowns by exhaustive search (all factor pairs, every number in a range, every subset), logic puzzles by trying every arrangement, symmetry and perimeters by counting edges and mirror images, nets by rolling a cube over them with rotation matrices, dice by the same matrices. Where a figure decides the answer (angles, protractor, graphs, tables, shapes) the check reads the figure data from the unit file and cross-checks every printed label against the drawing (arc labels against ray directions, side labels against edge lengths, nets against the folding simulation). 427 answers checked, 0 mismatches. The runner is the shared Level 1 runner (its mutation test was done for Level 1).
- **Figures.** Large (text 10 pt or more through `figs.MIN_PT`, shapes about 8 mm per unit square or larger), drawn with the project palette only so the print edition becomes black, white and hatching. Nothing relies on colour: the two lines of a graph differ by dash and marker and carry a legend; hatching marks shaded squares; the dashed lines of symmetry are dashed. Number lines and rulers need not start at 0 (Unit 5 and Unit 9 use scales that start elsewhere, with a zigzag mark on the axis). Money is written with cents ($0.75, 50¢).
- **Beyond-syllabus items** only in Think harder and Go further with the label (list above).
- **Tiers.** Start here is school-range with a worked example, Think harder is a school-paper Section C part (a) with a one-line hint, Go further is a harder or longer chain, Check yourself has 4 quick items and the score rule.
- **Wording.** `wording_lint.py` passes (sentence length at most 20 words, mean 12, at most 5 sentences per stem, one-line hints of at most 68 characters, no quantity written as a word). Numbers of 5 digits or more use a non-breaking space between thousands (47 285); 4-digit numbers have no space (4982).

## Answer-page notes

Answers are one per item with "Why" lines; `render.answer_blocks` prints the page of the question. Answers to open "draw it" tasks are not asked: every item has a number, word, letter or list answer so the independent check can verify it.

## Page budget

Each unit is 7 pages (Learn it, 3 Start here, Think harder, Go further, Check yourself). The fill gate (85 percent or more of every unit page, no overflow) fixed the number of items per page, with working rows (writing space) added where a page was short. The Level 4 body type is 16 px with 8 mm ruled lines and 16 x 10 mm answer boxes (`config/levels.json`); 5-digit answers fit the boxes.

## Known limits and things for a person

- No child trial yet (reading load, hint use, writing space, whether Unit 6 is too hard without a protractor: the unit asks the child to have a 180 degree protractor and a ruler, said on its Learn it page; the printed arms in Start here 1 are about 40 mm long and the child is told to extend them with a ruler).
- The Welcome page text is the shared one; it does not mention the protractor.
- Unit 6 Start here 1 (measure with your own protractor) can only be marked with a tolerance of about 2 degrees; the printed answer is exact and says so.
- Unit 5 and Unit 9 reuse a few phrases such as "Show your working" only as "Working:" lines; nothing else is shared with other units. Cross-unit duplicates inside Level 4 were not checked by a script.
- Page images were viewed for every unit page in the colour edition at 72 to 80 dpi, and the print edition is checked by `bw_check.py` and `print/check_bw.py` (see PROGRESS.md for the final run).
