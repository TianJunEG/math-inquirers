# Early Finisher Puzzles, Primary 1: two semester booklets (pilot)

Two booklets of 20 single-sided A4 pages each (Semester 1 = Terms 1 and 2, Semester 2 = Terms 3 and 4; the split follows the typical order, schools vary), 40 pages in all, P1-01 to P1-40.
Every page is self-checking, pure black and white, with the school name and a page code like `S1-07 (P1-08)` in the footer, and each booklet has its own teacher answer key with outcome tags.
Not for sale as is: a pilot for owner review. Cover, licence and teacher notes carry DRAFT stamps, the business email pypteltd@gmail.com and the registered office address (66 Tannery Ln, Singapore 347805) until the owner and a lawyer approve the wording; the entity and year in the footer (c) line are confirmed by the owner.
Plan: `docs/school_books/p1_semester_booklets_plan.md`; build report and open items: `docs/school_books/p1_semester_booklets_build_report.md`; owner decisions: `docs/terms/owner_decisions.md` (23 Oct 2026, evening). Earlier audits of the 20-page pilot: `AUDIT*.md`, `AUDIT_FIXES*.md`.

## Regenerate

```
cd school/p1
python3 build.py --school "Name of School"   # both booklets; omit --school to print a blank line to write the name on
python3 build.py --booklet S1                # one booklet
python3 build.py --final                     # leave out the DRAFT stamps (only after the owner and a lawyer approve the front matter)
python3 validate.py                          # about 770 checks; exit code 1 on any failure (about 3 minutes)
python3 validate.py --partial                # work in progress: not every one of the 40 pages exists yet
```

Needs: python3 with `playwright` (chromium), `pypdf`, `Pillow`, `shapely`, `fonttools`, `brotli`, `numpy`, `scipy`; poppler (`pdftoppm`, `pdfinfo`, `pdffonts`, `pdftotext`); fonts from `fonts/node_modules/@fontsource` (Fredoka, Nunito Sans).
All puzzles come from fixed seeds, so a rebuild gives identical puzzles. Only the footer changes with `--school`.

Outputs in `out/` (committed: the PDFs, `verification.json`, `validation_report.txt`; not committed: `out/*.html`, `out/bilevel_check/`):

| File | Pages | Use |
|---|---|---|
| `P1_S1_Puzzles.pdf`, `P1_S2_Puzzles.pdf` | 20 each | The pupil pages. Photocopy these. |
| `P1_S1_FrontMatter.pdf`, `P1_S2_FrontMatter.pdf` | 5 each | Cover, photocopy licence, teacher notes (2 pages), contents and outcome coverage |
| `P1_S1_Complete_Pack.pdf`, `P1_S2_Complete_Pack.pdf` | 25 each | Front matter + puzzles |
| `P1_S1_Answer_Key.pdf`, `P1_S2_Answer_Key.pdf` | see report | Teacher key: answers, check result, syllabus outcome numbers, notes, small solved pictures, full answer pages for colour-by-code pages |

The four PDFs of the old single 20-page pack (`P1_Puzzles.pdf` and so on) were removed: the booklets replace them.

## Code layout

- `gen/outcomes.py`: the 32 Primary 1 outcome lines in the syllabus PDF's wording, which outcomes each page exercises, and the page order of each booklet (the only place the split is defined).
- `gen/common.py` code tables, the word lists (`gen/words_en.txt.gz`, about 129 000 words; `gen/words_common.txt.gz`), SVG shapes, object art. `gen/art.py` extra objects (bird, flower, pets, toys). `gen/css_new.py` CSS of the new pages.
- Old pages: `gen/pages_numbers.py` (P1-02, 04, 07), `gen/pages_arith.py` (P1-03, 05, 08 to 11, 13), `gen/pages_measure.py` (P1-06, 15 to 20), `gen/pages_cbc.py` (P1-01, 12, 14; picture library vendored in `cbc_vendor/`).
- New pages (P1-21 to P1-40): `gen/pages_stories.py` (21, 22, 39, 40), `gen/pages_num2.py` (23 to 26, 37, 38), `gen/pages_money_time.py` (27 to 30), `gen/pages_meas2.py` (31 to 36).
  Each `pageNN()` makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED text or drawing (not the generator's data), and hands `validate.py` a `model` (right answers, the values each answer could take, the pupil's check as a function) for the independent wrong-answer enumeration.
- `render.py` HTML/CSS, page frame, front matter and key per booklet. `build.py` makes the PDFs. `validate.py` runs all checks.

## The 20 new pages

| Code | Title | Stars | Outcomes | Check |
|---|---|---|---|---|
| S1-10 (P1-21) | Story Sums | 2 | Addition and Subtraction 2.1, Addition and Subtraction 2.2, Addition and Subtraction 2.7 | K1 code word |
| S2-20 (P1-22) | Two-Step Stories | 2 | Addition and Subtraction 2.1, Addition and Subtraction 2.2, Addition and Subtraction 2.5, Addition and Subtraction 2.7 | K1 code word |
| S2-07 (P1-23) | Stack It Up | 1 | Addition and Subtraction 2.5, Addition and Subtraction 2.6 | K1 code word |
| S1-03 (P1-24) | Words and Numbers | 1 | Whole Numbers 1.3, Whole Numbers 1.7 | K6 route closes at FINISH through the stated number of boxes |
| S1-01 (P1-25) | Count the Crowd | 1 | Whole Numbers 1.1, Whole Numbers 1.4 | K1 code word |
| S1-15 (P1-26) | Chart Patterns | 2 | Whole Numbers 1.6, Whole Numbers 1.2, Whole Numbers 1.5 | K1 code word |
| S2-13 (P1-27) | Which Two Items? | 2 | Money 1.1, Addition and Subtraction 2.5 | K1 letters of the chosen items, cheaper first, spell a word |
| S2-11 (P1-28) | Fewest Coins | 1 | Money 1.1 | K1 code word |
| S2-16 (P1-29) | How Long Does It Last? | 1 | Time 2.3, Time 2.4, Time 2.1 | K1 code word |
| S2-15 (P1-30) | Morning or Evening? | 1 | Time 2.1, Time 2.2 | K6 route closes at FINISH through the stated number of boxes |
| S1-18 (P1-31) | Shortest to Longest | 1 | Length 1.2, Length 1.3 | K1 letters of the strips, shortest first, spell a word |
| S2-08 (P1-32) | Measure and Draw | 1 | Length 1.1, Length 1.2, Length 1.4 | K1 code word |
| S1-16 (P1-33) | Shape Builder | 2 | 2D Shapes 1.1, 2D Shapes 1.2, 2D Shapes 1.3 | K3 the five counts add to 16 + K1 code word |
| S1-17 (P1-34) | Finish the Figure | 2 | 2D Shapes 1.4 | K1 letter of the matching right half in each row spells a word |
| S2-17 (P1-35) | Read the Picture Graph | 1 | Picture Graphs 1.1 | K1 code word |
| S2-19 (P1-36) | Graph Detective Two | 2 | Picture Graphs 1.1 | K3 the total of all stars, and a second sum that uses the answers to a) and b) |
| S1-08 (P1-37) | Bonds and Families | 2 | Addition and Subtraction 2.1, Addition and Subtraction 2.2, Addition and Subtraction 2.3 | K8 the loop closes: every number joined by = matches |
| S1-12 (P1-38) | More or Fewer | 2 | Whole Numbers 1.4, Addition and Subtraction 2.1 | K4 grid + K1 letter beside each amount spells a word |
| S2-02 (P1-39) | Share and Group | 1 | Multiplication and Division 3.1, Multiplication and Division 3.4 | K1 code word |
| S2-05 (P1-40) | True or False | 2 | Multiplication and Division 3.1, Multiplication and Division 3.2, Multiplication and Division 3.3 | K1 letter of the ticked answer in each row spells a word |

The 20 earlier pages keep their numbers P1-01 to P1-20 (inventory and enumeration rates in `AUDIT_FIXES_3.md` and `out/verification.json`). Changes made while building the booklets: P1-03 sharer line, P1-05 arrays, P1-13 bigger bags (totals within 24), P1-07 drawn people, clock numerals redrawn (P1-06, 18, 29), P1-13 and P1-16 retagged.

## Rules every page keeps

Black and white only (#000/#fff, strokes at least 0.57 pt); A4 with 15 mm margins; instruction sentences at most 8 words, at most 3 lines; answer boxes at least 12 mm high; money as 50¢; times as o'clock and half past in words, 5-minute times as digits, am and pm without full stops; no division sign, fractions, odd or even, or shapes beyond the six on the syllabus list; no Mi, MOE, alignment or price wording (the licence page has one not-affiliated sentence). Code words: exactly one arrangement of the letters is a word, so no wrong placement of the answers spells a word, tested against the 129 000-word list. Wrong-answer enumeration at 95% or better on every page. See `validate.py` for the full list.

## Open questions for the owner

See `docs/school_books/p1_semester_booklets_build_report.md`, section "Items for the owner".
