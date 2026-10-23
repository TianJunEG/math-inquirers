# Extension Workbook, Level 1 (self-study, with answers)

Product: owner decisions of 22-23 Oct 2026 (docs/terms/owner_decisions.md). Ten units follow the ten Holiday Program Level 1 lessons, new questions only. No price printed. Printed copy black and white, soft copy colour.

## Output
`outputs/extension/L1/`
- `Math_Inquirers_L1_Extension_Workbook_Soft_Copy_Colour.pdf` (96 pages, colour, bookmarks)
- `Math_Inquirers_L1_Extension_Workbook_Print_BW.pdf` (96 pages, even, mirrored 12 mm gutter, answers start on a right-hand page, blank page 78 only for parity)
- `build_report.json` (page fill and overflow per page)

Page order: cover (name box), About this book (copyright and personal-use licence, DRAFT wording for the owner and lawyer; business email and registered office are placeholders), Welcome, Contents, Pace plan (11 weeks, 3 sessions), 10 units of 7 pages, My progress, Certificate, (blank), Answers divider, Answers (17 pages, short "Why" for every item).

## Build
```
npm install --prefix fonts          # fonts used by the build
python3 extension/tools/build.py --level 1
extension/verify_all.sh 1           # answers, duplicates, wording, build, B&W, page fill
```
Needs python3 with playwright (chromium), pypdf, PyMuPDF, Pillow, numpy. The external duplicate gate reads gitignored `docs/books/private_*` and `docs/sasmo/private_*`.

## Inventory
Items per tier = Start here / Think harder / Go further / Check yourself (plus one try-it per unit).

| Unit | Topic | Items per tier | Beyond item | Verification |
|---|---|---|---|---|
| 1 | Hops and rules (Number patterns) | 14 / 3 / 3 / 4 | Triangle numbers | answers, 7-gram, wording, B&W, fill: pass |
| 2 | Make 10 and 20 (Number bonds) | 13 / 3 / 4 / 4 | Making two amounts equal | answers, 7-gram, wording, B&W, fill: pass |
| 3 | Read and draw graphs (Picture graphs) | 10 / 3 / 3 / 4 | Keys bigger than 1; Comparing two keys; Build a graph from clues | answers, 7-gram, wording, B&W, fill: pass |
| 4 | Patterns that go on (Repeating and growing patterns) | 13 / 3 / 3 / 4 | Jumps that grow; Two ways to build; Two patterns together | answers, 7-gram, wording, B&W, fill: pass |
| 5 | Back to the start (Working backwards) | 14 / 3 / 3 / 4 | Undoing a double | answers, 7-gram, wording, B&W, fill: pass |
| 6 | Pay the exact amount (Money) | 14 / 3 / 3 / 4 | Sharing money equally | answers, 7-gram, wording, B&W, fill: pass |
| 7 | Shape detective (2D shapes) | 9 / 3 / 3 / 4 | Fold lines | answers, 7-gram, wording, B&W, fill: pass |
| 8 | Clues and sorting (Logic and sorting) | 11 / 3 / 3 / 4 | Truth and lies; Yes or no questions | answers, 7-gram, wording, B&W, fill: pass |
| 9 | How long is it? (Length) | 14 / 3 / 3 / 4 | Posts and gaps | answers, 7-gram, wording, B&W, fill: pass |
| 10 | Mix and solve (Mixed puzzles) | 14 / 3 / 3 / 4 | Doubling | answers, 7-gram, wording, B&W, fill: pass |

## Verification results (last run)
- Independent answer checks: 403 answers, 0 mismatches.
- Duplicate check: 247 question texts, 0 shared 7-word runs with the holiday Level 1 workbook and bank or the private sources; REVIEW lines (same skeleton, other numbers) are accepted as "similar type". Cross-unit check: only stock command phrases are shared.
- Wording lint: 0 errors (warnings are label words and some command-less stems).
- B&W: 96 pages, max chroma 0.00000, max flat grey 0.00003.
- Page fill: every unit page 86 to 100 percent, no overflow.
- All 96 print pages and a colour contact sheet were viewed.

## Open for the owner
Licence wording, contact details, price (none printed), printer proof, child trial, independent cold-read audit.
