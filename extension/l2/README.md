# Level 2 Extension Workbook (self-study, with answers)

Ten units follow the ten Holiday Program Level 2 lessons in order (`p2/content/l1.js` to `l10.js`), with new questions of similar types. Ages 7 to 9. No price, no MOE, GEP or SASMO claim, no tutor or class dependence. Printed copy black and white, soft copy colour.

## Where things are
| What | Where |
|---|---|
| Unit data (learn page, items, answers, hints, explanations) | `extension/data/l2_u01.json` ... `l2_u10.json` |
| Author scripts that write the JSON (edit these, then run them) | `extension/l2/author/u01.py` ... `u10.py`, helper `extension/l2/author/lib.py` |
| Independent answer checks (recompute every answer, never copy) | `extension/verify/l2_u01_checks.py` ... `l2_u10_checks.py` |
| Figure plug-ins (types all start with `l2_`) | `extension/tools/figs_l2_core.py` (cards, blocks, chart, nline, table, grid, vsum), `figs_l2_bars.py` (bar, triangle), `figs_l2_u03.py` (array, groups, legs), `figs_l2_u04.py` (pattern, sticks), `figs_l2_u05.py` (machine), `figs_l2_u06.py` (money, tags), `figs_l2_u07.py` (frac), `figs_l2_u08.py` (cubes, solids, pieces, nets, trilines), `figs_l2_u09.py` (scale, clock, jugs), `figs_l2_u10.py` (pgraph, tally, lgrid) |
| Output | `outputs/extension/L2/` (soft copy colour, print BW 1-bit, vector print source, `build_report.json`) |
| Progress and notes | `extension/l2/PROGRESS.md`, this file, `extension/l2/AUDIT_NOTES.md` |

## Build and gates
```
python3 extension/l2/author/uNN.py            # rewrite data/l2_uNN.json (optional)
python3 extension/tools/build.py --level 2    # full build (1-bit conversion takes a few minutes); add --no-bw --units N --out <dir> for quick views
python3 extension/verify/run_checks.py --level 2
python3 extension/verify/dup_check.py --level 2
python3 extension/verify/wording_lint.py --level 2
python3 extension/verify/bw_check.py outputs/extension/L2/*Print_BW.pdf
python3 extension/verify/fill_check.py --level 2
```
(`extension/verify_all.sh 2` runs the same gates in order.)

## Conventions used in this level
- `lib.build()` sorts the items by tier and printed page, so the number printed on the page, the number in the answer section and the item id (S01, S02 ...) always agree. Keep the order in an author script free; never rely on list order.
- Parts of an item (`P(...)`) hold the answer boxes: one `{b}` per answer value, `{ll}` for a list (set `lst=True`), `{circ:a|b}` for a choice. Answers inside a figure are written in the answer boxes below it, not in the picture.
- Fractions are written as plain text (`3/8`), money in dollars and cents (`$4.35`, `85¢`), multiplication `×`, division `÷`; subtraction uses a hyphen.
- Open items (make your own puzzle) carry `value: "open"`; their check function verifies that the book's example really has exactly one answer.
- "Beyond" items (not in the Level 2 school range) are only in Think harder and Go further and print a label "Beyond Level 1: ..." from the shared renderer (the renderer text says Level 1 for every level; see TOOL_REQUESTS.md).
- Hints are upside down, one line, 68 characters at most.
- Lint note: the shared lint forbids the word "price" (book price rule), so shop items say "cost" and "tag". It also forbids "biggest/bigger": use greatest/larger.
- The 7-word duplicate gate also looks at the holiday workbook text, so a holiday sentence frame ("pay exactly. Use the fewest notes and coins", "How many ... of all sizes", "no tutor") was reworded in every unit; the REVIEW list (same skeleton, other numbers) is expected and was read (see AUDIT_NOTES.md).

## Inventory (items per tier = Start here / Think harder / Go further / Check yourself; plus one Try item per unit)
| Unit | Title | Items | Beyond items |
|---|---|---|---|
| 1 | Digit detectives | 11 / 3 / 4 / 4 | Thousands |
| 2 | Missing digit mysteries | 11 / 3 / 4 / 4 | Patterns in subtraction |
| 3 | Legs, wheels and arrays | 10 / 3 / 4 / 4 | The 6 times table |
| 4 | Pattern machines | 10 / 3 / 4 / 4 | Square numbers |
| 5 | Mystery number machines | 10 / 3 / 4 / 4 | Letters for numbers |
| 6 | Market day | 10 / 3 / 4 / 4 | Halving money |
| 7 | Fair shares | 9 / 3 / 4 / 4 | Equal fractions |
| 8 | Shape builders | 10 / 3 / 4 / 4 | Cube nets; Square numbers in a pyramid |
| 9 | Measure masters | 11 / 3 / 4 / 4 | 24-hour clock |
| 10 | Puzzle day | 10 / 3 / 4 / 4 | Half pictures |

Total 212 items plus 10 Try items; 493 answer values independently checked.

## Result of the last full run
- Both PDFs have 100 pages (even): cover, About, Welcome, Contents, Pace plan, 10 units x 7 pages (pages 6 to 75), My progress (76), Certificate (77), blank (78), Answers divider (79, a right-hand page), answers 80 to 100.
- Gates: answers 0 mismatches; duplicates 0 shared 7-word runs; wording lint 0 errors; B&W 0 colour pixels, flat grey under 0.0005; every unit page 82 to 100 percent full, no overflow.
