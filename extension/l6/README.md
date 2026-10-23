# Level 6 Extension Workbook: audit-ready notes

Written 23 Oct 2026 by the Level 6 author agent. Pipeline, spec and QA plan: `docs/extension_books/plan.md`, `extension/README.md`.
Ages 11 to 13. Ten units follow the ten holiday lessons of the P6 post-PSLE program (`p6/content/l1.js` to `l10.js`), as a maths-and-coding bridge.
All coding items are paper-and-pencil: code blocks are printed (our own simple blocks, not Scratch art), the child predicts, traces, fills gaps, plans and finds bugs. No computer is needed.

## Files (everything Level 6 owns)

| Path | What |
|---|---|
| `extension/data/l6_u01.json` .. `l6_u10.json` | the ten units (schema as Level 1), generated from `extension/l6/src/uNN.py` |
| `extension/l6/src/uNN.py`, `lib.py`, `whys.py` | author sources. `python3 extension/l6/src/uNN.py` writes the JSON and fits the Start here items to pages. `whys.py` holds shortened answer explanations for the 30 longest items (page budget, see below) |
| `extension/l6/tools/measure.py` | measures every item in the real stylesheet and suggests the 3 Start here pages (each page 86 to 98.5 percent full) |
| `extension/verify/l6_uNN_checks.py`, `l6_lib.py` | independent answer checks (below) |
| `extension/tools/figs_l6_core.py`, `figs_l6_geo.py` | figure plug-ins, all type names start with `l6_` |
| `extension/l6/PROGRESS.md`, `TOOL_REQUESTS.md` | progress and shared-tool requests |
| `outputs/extension/L6/` | the two PDFs and `build_report.json` |

## Figures (all drawn from specs, black text on light fill, nothing told by colour)
`l6_code` (our code blocks; kinds are told by shape and words; blank slots are dashed boxes; optional trace table beside the code), `l6_grid` (tables, letter table, dice table, sieve), `l6_nline`, `l6_vline` (number line, thermometer), `l6_machine` (IN, steps, OUT, with undo arrows), `l6_tree` (factor tree), `l6_cards`, `l6_sticks` (matchstick patterns), `l6_model` (bar model), `l6_dots` (people joined by lines), `l6_routes` (street grid), `l6_spinner`, `l6_bag`, `l6_turtle` (path of a turtle, computed from commands), `l6_clock`, `l6_bars` (bar chart). Objects are at least 8 mm; text in figures is 11 to 13 pt or more (the renderer raises anything below 10 pt).
The matchstick, route, turtle and dot figures are computed from the same facts the checks use (edges counted, paths enumerated), but the check files recompute the answers separately.

## Units (each: Learn it with worked example, 11 Start here, 3 Think harder, 3 Go further, 4 Check yourself; unit 10 has 14 Start here)

| Unit | Title (holiday lesson) | Start here item types (mirrors the holiday type, new numbers and contexts) | Beyond items (labelled) |
|---|---|---|---|
| 1 | Code the pattern (1) | matchstick table and rule, difference and nth term table, is it a term, trace a loop (say before change), plan a loop, off-by-one bug, story rule, match the rule, jumps counted, code that says a rule, spot the mistake in a rule | T: none. G1 second differences (staircases), G3 triangle numbers |
| 2 | Prime hunters (2) | factor pairs, circle the primes, factor tree, trace a factor counter (mod), Goldbach pairs, divisibility tests, remainder test of 113, riddles, odd number of factors, mod in a loop, rows of cards | G1 counting factors from primes |
| 3 | Below zero (3) | order, read a line and a thermometer, add and subtract by jumps, missing number, distance, trace a sprite on x, fill blocks, money below 0, floors with no level 0, distance from 0 | T1 subtracting a negative, G3 calendar with no year 0 |
| 4 | Algebra machines (4) | guess my rule from a table (plus and minus), order of steps, missing step, run backwards, ask and answer code, plan a search loop, expressions with n, rate rule, number trick, branching machine | G1 n on both sides |
| 5 | Every possible way (5) | multiplication rule, coin and dice table, handshakes, nested loops, grid routes with filled corners, passwords, podium, nested loop of pairs, digit cards with 0, diagonals, rectangles in a row | G1 count the opposite, G3 counting chain |
| 6 | Fair or unfair? (6) | spinner and bag fractions, coin and spinner table, two dice table, fair game, expected counts, simulation code, numbers 1 to 30, compare bags, coin run, most likely total | G1 at least one, G3 expected winnings |
| 7 | Turtle geometry (7) | table of turn and inside angle, which program closes, trace total turned, irregular polygon last turn, inside angle sum, plan 30 sides, whole-number sides, 10-point star, rectangle program, tiling around a point, k times the turn | G1 coordinates of a spiral, G2 angle sum of star points, G3 a polygon that looks like a circle |
| 8 | Secret codes (8) | clock hours, mod, weekdays, encode, decode, trace a letter code, crack from THE, combine shifts, 24-hour clock, wrap-round loop, jumps on a clock | G1 changing shift, G3 check digits |
| 9 | Data detectives (9) | mean lists (with 0 and decimals), level the towers, total from mean, missing value, change of mean, median and mode, misleading pay, bar chart, list loop, change every value, add a value | G1 pairing, G3 frequency table |
| 10 | Showcase challenge (10) | the nine ideas in a mixed round (14 items), read a program, put the steps of planning in order | G1 and G2 plan programs |

Learn it pages: one worked example (with figure), a how-to box, and a Your turn item, as in Level 1.

## Originality and the duplicate gate
- Every problem is original: contexts, numbers and wording are new. Where the holiday lesson uses a type (for example the matchstick table, handshakes, the two-dice table, the Caesar code, Goldbach, the 100th term), the extension item keeps the type and changes numbers, objects and parts.
- `python3 extension/verify/dup_check.py --level 6`: no 7-word run shared with `p6/` or with the private source texts (48 files checked, 519,102 grams). The REVIEW list (same sentence skeleton, numbers differ) was read in full. Items closest to a holiday item were changed after the review (unit 3 worked example and Try, unit 4 Check yourself 2, unit 6 Check yourself 1, unit 9 Check yourself 3). The remaining REVIEW lines are standard stems ("write ... as a product of primes", "set n to ..., repeat ..., change n by ...", "a bag has ... red and ... blue"); they were accepted as "similar type, new numbers".
- No MOE, GEP, SASMO or price words (the wording lint checks the claim and price words). No tutor or class dependence. The licence text is the shared one from `build.py`.

## Answers: independent checks
`extension/verify/l6_uNN_checks.py` recomputes every answer of every item and every part (528 answers over the ten units, Try items included). Methods: stepping on a number line or clock one place at a time, listing every case with `itertools`, trial division, exact fractions, running the printed code blocks with the small interpreter in `l6_lib.py` (it reads the program from the unit file, so a program that differs from its answer is caught), a turtle simulator for unit 7, reading printed tables and charts from the unit file. Simulations that use random numbers are checked by the exact probability, and "is it surprising?" items by 3 standard deviations. Open parts (a twist, a test the child writes) carry no answer and are marked as such in the Why line. All 526 agree with the printed key. Every item was also solved by hand while writing it.

## Layout and gates
- `python3 extension/tools/build.py --level 6`, then `extension/verify_all.sh 6` (run_checks, dup_check, wording_lint, build, bw_check, print/check_bw, fill_check). Last result: see the end of `PROGRESS.md`.
- Every unit page is at least 85 percent full before the leftover space is shared out (measured by the build); no page overflows. Start here pages were fitted with `measure.py` (it also reorders items between pages when needed, so item numbers on a page follow the printed order, not the id order).
- Print edition is black and white (1-bit 600 dpi after conversion); code blocks are black text on white, no hatching behind text. Soft copy uses pale yellow and blue fills only.
- Long answers: the answer section is 21 pages (80 to 100) and the whole book is 100 pages in both editions (answers start on page 80, divider on 79, one blank page 78 in print). To keep it at 100, about 60 of the longest Why lines were shortened (`whys.py`). The plan's fallback (6 pages per unit) was not needed and is a shared-config change.

## Decisions and open points (for the owner and the audit)
1. Items per unit: 22 (11 + 3 + 3 + 4 + the Your turn item), 25 in unit 10. The plan said about 24; code and figure items are tall (a six-block program is about 70 mm), so more items would not fit the 7-page grid at 86 percent fill.
2. Beyond label: uses the shared `beyond` key (the renderer prints "Beyond Level 6"). Welcome notes and the print note come from `levels.json` (no rulers).
3. Audit fixes (second pass): items that sat too close to holiday P6 items were given new stories and frames (units 3, 4, 5, 6, 8, 9, 10); give-aways removed from hints and stems; Learn pages gained the factor-tree and divisibility tests (unit 2), a clock example (unit 8), median/mode/missing-value lines (unit 9). The code legend "Reading the code blocks" sits on the unit 4 Learn page (the only Learn page with room for it); the first code item in unit 1 points to it (page 27), and it covers set, change, say, ask, repeat, repeat until, if/else, mod, pick random, item and length of list, the turn arrow and the dashed blank.
4a. Round 2 (AUDIT_ROUND2.md): the unit 3 Learn step 2, the two stale Why overrides (units 5 and 6), and the clone items in units 3 (card game), 9 (cakes) and 10 (S1, S7, S9, S13, G2c, C1) were replaced; unit 10 G1 now prints `answer`; unit 2 teaches the tests for 4 and 9; unit 7 states the angle sum.
4. Not done (needs people): child trial of reading load and pace, owner review of tier difficulty, an independent cold audit of the maths and wording, printer proof. Coding items were never run in Scratch (the blocks are our own drawings with Scratch-like names); the programs were run by the checker's interpreter.
5. Items that use a decimal answer: unit 9 (2.75, 6.4 and 6.5, 19.2, 54.5, 1.3, 5.6, 102.8 in unit 6). The answer boxes are plain boxes; the key gives the decimal.
6. The fill gate is met on the natural layout; the ruled boxes are then stretched to share the leftover space, so some boxes have extra blank space for working.
