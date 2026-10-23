# Early Finisher Puzzles, Primary 2: two semester booklets (pilot)

Two booklets of 20 single-sided A4 pages each (Semester 1 = Terms 1 and 2, Semester 2 = Terms 3 and 4; the split follows the typical order, schools vary), 40 pages in all, P2-01 to P2-40 (build order; the footer code prints both numbers, for example `S1-07 (P2-17)`).
Every page is self-checking, pure black and white, with the school name line and the copyright line in the footer, and each booklet has its own teacher answer key with outcome tags in the syllabus PDF's wording. Each booklet is 10 one-star and 10 two-star pages.
Not for sale as is: a pilot for owner review. Cover, licence, teacher notes and keys carry DRAFT stamps, the business email pypteltd@gmail.com and the registered office address (66 Tannery Ln, Singapore 347805); the licence is an annual licence (one school year, renewable) whose wording is for a lawyer to approve.
Plan: `docs/school_books/p2_semester_booklets_plan.md`; build report and open items: `docs/school_books/p2_semester_booklets_build_report.md`; outcome wording: `docs/school_books/p2_outcome_wording.md`; owner decisions: `docs/terms/owner_decisions.md`.

This pipeline was copied from `school/p1` (P1 is not touched by it) and parameterised for Primary 2: outcomes (30 lines of pages 33 and 34 of the syllabus PDF), reading load (10 words a sentence), numbers to 1000, money in decimal notation, minutes, kg, g, litres, fractions, tables of 2, 3, 4, 5, 10 and the sign ÷, 3D solids, picture graphs with scales.

## Regenerate

```
cd school/p2
python3 build.py --school "Name of School"   # both booklets; omit --school to print a blank line to write the name on
python3 build.py --booklet S1                # one booklet
python3 build.py --final                     # leave out the DRAFT stamps (only after the owner and a lawyer approve the front matter)
python3 validate.py                          # every check; exit code 1 on any failure (several minutes)
python3 validate.py --partial                # work in progress: not every one of the 40 pages exists yet
python3 preview.py 1 2 3 --dpi 75 --bw       # developer preview: PNGs of pupil pages
```

Needs: python3 with `playwright` (chromium), `pypdf`, `Pillow`, `shapely`, `fonttools`, `brotli`, `numpy`, `scipy`; poppler (`pdftoppm`, `pdfinfo`, `pdffonts`, `pdftotext`); fonts from `fonts/node_modules/@fontsource` (Fredoka, Nunito Sans).
All puzzles come from fixed seeds, so a rebuild gives identical puzzles. Only the footer changes with `--school`.

Outputs in `out/`: `P2_S1_Puzzles.pdf`, `P2_S2_Puzzles.pdf` (20 pages each, photocopy these), `P2_S?_FrontMatter.pdf` (5 pages), `P2_S?_Complete_Pack.pdf`, `P2_S?_Answer_Key.pdf`, `verification.json`, `validation_report.txt` (committed); `out/*.html` and `out/bilevel_check/` are not committed.

## Code layout

- `gen/outcomes.py`: the 30 outcome lines in the syllabus PDF's wording, the outcomes of each page (filled from the pages when `build.py` runs) and the page order of each booklet (the only place the split is defined).
- `gen/common.py` code tables, word lists (about 129 000 words), SVG shapes, object art; `gen/kit.py` safe code words (distinct letters, one arrangement, no single letter placed in another slot making a word), the standard code-word record, route helpers, vertical sums, lettered-choice rows; `gen/art.py` objects; `gen/art2.py` place-value discs, coins and notes (original art), clocks to the minute; `gen/css_p2.py` CSS.
- Page modules: `gen/pages_w1.py` (P2-01 to 08), `pages_w2.py` (09 to 16), `pages_w3.py` (17 to 24), `pages_w4.py` (25 to 32), `pages_w5.py` (33 to 37), `pages_cbc.py` (38 to 40, colour by code from `cbc_vendor/`, a copy of `school/colour_by_code`).
  Each `pageNN()` makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED text or drawing (not the generator's data), and hands `validate.py` a `model` for the independent wrong-answer enumeration.
- `render.py` HTML/CSS, page frame, front matter and key per booklet. `build.py` makes the PDFs. `validate.py` runs all checks.

## The 40 pages

| Code | Title | Stars | Check |
|---|---|---|---|
| S1-01 (P2-01) | Hundreds, Tens, Ones | 1 | K1 code word (6 letters) |
| S1-08 (P2-02) | Column Sums | 1 | K1 code word (6 letters) |
| S1-09 (P2-03) | Mental Jumps | 1 | K6 route closes at FINISH |
| S1-12 (P2-04) | Equal Groups | 1 | K1 code word (6 letters) |
| S1-13 (P2-05) | Share It Out | 1 | K1 code word (6 letters) |
| S2-01 (P2-06) | Dollars and Cents | 1 | K1 code word (6 letters) |
| S2-10 (P2-07) | Time to the Minute | 1 | K1 code word (6 letters) |
| S2-05 (P2-08) | Metres | 1 | K1 code word (5 letters) |
| S1-03 (P2-09) | Words and Numbers | 1 | K6 route closes at FINISH through the stated number of boxes |
| S1-05 (P2-10) | Digit Cards | 2 | K1 code word (6 letters) |
| S1-06 (P2-11) | Number Patterns | 2 | K1 code word (6 letters) |
| S1-04 (P2-12) | Odd or Even | 1 | K6 route closes at FINISH |
| S1-10 (P2-13) | Missing Digits | 2 | K1 code word (6 letters) |
| S1-14 (P2-14) | Times Table Maze | 1 | K6 route closes at FINISH |
| S1-18 (P2-15) | Parts of a Whole | 1 | K1 code word (6 letters) |
| S2-02 (P2-16) | Writing Money | 2 | K1 code word (6 letters) |
| S1-07 (P2-17) | Mystery Numbers | 2 | K1 code word (5 letters) |
| S1-11 (P2-18) | Story Sums to 1000 | 2 | K1 code word (6 letters) |
| S1-15 (P2-19) | Fact Families | 2 | K8 the loop closes: every number joined by = matches |
| S1-16 (P2-20) | True or False Tables | 2 | K1 the letter of the right choice in each row spells a word (6 letters |
| S1-19 (P2-21) | Fraction Order | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S1-20 (P2-22) | Fraction Sums | 2 | K1 code word (6 letters) |
| S2-03 (P2-23) | Which Costs More? | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S2-04 (P2-24) | Purse Match | 2 | K1 letters of the matching purses spell a word (6 letters) + K4 each p |
| S2-06 (P2-25) | Kilograms and Grams | 1 | K1 code word (6 letters) |
| S2-07 (P2-26) | Litres | 1 | K1 code word (6 letters) |
| S2-08 (P2-27) | Which Unit? | 1 | K1 the letter of the right unit in each row spells a word (6 letters,  |
| S2-09 (P2-28) | Order the Measures | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S2-12 (P2-29) | Match the Times | 2 | K1 letters of the matching clocks spell a word (6 letters) + K4 each c |
| S2-11 (P2-30) | Hours and Minutes | 1 | K1 code word (6 letters) |
| S2-13 (P2-31) | Time Detective | 2 | K1 code word (6 letters) |
| S2-14 (P2-32) | Shape Patterns | 1 | K1 the letter of the shape that comes next spells a word (6 letters, t |
| S2-15 (P2-33) | Pattern Rules | 2 | K1 the letter of the shape that comes next spells a word (6 letters, t |
| S2-16 (P2-34) | Meet the Solids | 1 | K1 the letter of the right name in each row spells a word (6 letters,  |
| S2-17 (P2-35) | Solid Sort | 2 | K3 the five counts add to 15 + K1 code word (5 letters) |
| S2-18 (P2-36) | Picture Graph Scales | 1 | K1 code word (6 letters) |
| S2-19 (P2-37) | Graph Detective Two | 2 | K1 code word (6 letters) |
| S1-02 (P2-38) | Colour the Rocket | 1 | K1 colour key + K3 tally of colours (+ matching parts) |
| S1-17 (P2-39) | Colour the House | 2 | K1 colour key + K3 tally of colours (+ matching parts) |
| S2-20 (P2-40) | Colour the Butterfly | 2 | K1 colour key + K3 tally of colours (+ matching parts) |

## Rules every page keeps

Black and white only (#000/#fff, strokes at least 0.57 pt); A4 with 15 mm margins; instruction sentences at most 10 words, at most 3 lines; answer boxes at least 12 mm high; money as 50¢ and $2.50 (two decimal places); no Mi, MOE, alignment or price wording (the licence page has one not-affiliated sentence). Code words: exactly one arrangement of the letters is a word, so no wrong placement of the answers spells a word, tested against the 129 000-word list. Wrong-answer enumeration at 95% or better on every page. See `validate.py` for the full list.
