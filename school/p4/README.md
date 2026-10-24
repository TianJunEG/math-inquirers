# Early Finisher Puzzles, Primary 4: two semester booklets (draft)

Two booklets of 20 single-sided A4 pages each (Semester 1 = Terms 1 and 2, Semester 2 = Terms 3 and 4; the split follows the typical order, schools vary), 40 pages in all, P4-01 to P4-40 (build order; the footer code prints both numbers, for example `S1-07 (P4-07)`).
Every page is self-checking where a printed page can check it, pure black and white, with the school name line and the copyright line in the footer, and each booklet has its own teacher answer key with outcome tags in the syllabus PDF's wording. Each booklet is 10 one-star and 10 two-star pages.
Not for sale as is: a draft for owner review. Cover, licence, teacher notes and keys carry DRAFT stamps, the business email pypteltd@gmail.com and the registered office address (66 Tannery Ln, Singapore 347805); the licence is an annual licence (one school year, renewable) whose wording is for a lawyer to approve. The cover carries the one sentence that the booklet is not affiliated with or endorsed by the Ministry of Education, Singapore.
Plan: `docs/school_books/p4_semester_booklets_plan.md`; build report and open items: `docs/school_books/p4_semester_booklets_build_report.md`; outcome wording: `docs/school_books/p4_outcome_wording.md`.

This pipeline was copied from `school/p2` (P2 is not touched by it) and parameterised for Primary 4: 42 outcome lines (pages 37 to 40 of the syllabus PDF), reading load (14 words a sentence, 4 instruction sentences at most), numbers to 100 000 (a gap in 5-digit numbers), factors and multiples, long multiplication and division, mixed numbers, fractions of a set, decimals to 3 places, area and perimeter of rectilinear figures, angles and the protractor, symmetry, solids and nets, tables, line graphs and pie charts. Percentage, ratio, average, area of a triangle and volume are Primary 5 and are not used.

## Regenerate

```
cd school/p4
python3 build.py --school "Name of School"   # both booklets; omit --school to print a blank line to write the name on
python3 build.py --booklet S1                # one booklet
python3 build.py --final                     # leave out the DRAFT stamps (only after the owner and a lawyer approve the front matter)
python3 validate.py                          # every check; exit code 1 on any failure (a few minutes)
python3 validate.py --partial                # work in progress: not every one of the 40 pages exists yet
python3 preview.py 1 2 3 --dpi 75 --bw       # developer preview: PNGs of pupil pages
```

Needs: python3 with `playwright` (chromium), `pypdf`, `Pillow`, `shapely`, `fonttools`, `brotli`, `numpy`, `scipy`; poppler (`pdftoppm`, `pdfinfo`, `pdffonts`, `pdftotext`); fonts from `fonts/node_modules/@fontsource` (Fredoka, Nunito Sans).
All puzzles come from fixed seeds, so a rebuild gives identical puzzles. Only the footer changes with `--school`.

Outputs in `out/`: `P4_S1_Puzzles.pdf`, `P4_S2_Puzzles.pdf` (20 pages each, photocopy these), `P4_S?_FrontMatter.pdf` (5 pages), `P4_S?_Complete_Pack.pdf`, `P4_S?_Answer_Key.pdf`, `verification.json`, `validation_report.txt` (committed); `out/*.html` and `out/bilevel_check/` are not committed.

## Code layout

- `gen/outcomes.py`: the 42 outcome lines in the syllabus PDF's wording, the outcomes of each page (filled from the pages when `build.py` runs) and the page order of each booklet (the only place the split is defined).
- `gen/common.py` code tables, word lists (about 241 000 words), SVG shapes; `gen/kit.py` safe code words (distinct letters, one arrangement, no single letter placed in another slot making a word), the standard code-word record, route helpers, lettered-choice rows; `gen/kit4.py` Primary 4 builders (numbers with a gap, decimals and fractions, code and choice pages, ordering cards, routes in a maze with dead ends); `gen/art4.py` fraction bars, number lines, angle figures, protractor, number ring; `gen/art5.py` rectilinear figures with labelled sides; `gen/art6.py` dot-grid corners, mirror figures, symmetry grids, solids and nets; `gen/art7.py` line graph and pie chart; `gen/css_p4.py`, `gen/css_p4b.py` CSS.
- Page modules: `gen/pages_a.py` (P4-01 to 04, 06 to 10), `pages_b.py` (12 to 20), `pages_c.py` (21 to 30), `pages_d.py` (31 to 39), `pages_cbc.py` (05, 11 and 40, colour by code from `cbc_vendor/`, a copy of `school/colour_by_code` with Primary 4 banks).
  Each `pageNN()` makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED text or drawing (not the generator's data), and hands `validate.py` a `model` for the independent wrong-answer enumeration.
- `render.py` HTML/CSS, page frame, front matter and key per booklet. `build.py` makes the PDFs. `validate.py` runs all checks.

## The 40 pages

| Code | Title | Stars | Check |
|---|---|---|---|
| S1-01 (P4-01) | Place Value | 1 | K1 code word (6 letters) |
| S1-02 (P4-02) | Words and Numerals | 1 | K1 letters of the matching cards spell a word (6 letters), 4 decoy car |
| S1-03 (P4-03) | Number Patterns | 2 | K1 code word (6 letters) |
| S1-04 (P4-04) | Round It | 1 | K6 route closes at FINISH |
| S1-05 (P4-05) | Colour the Bus | 2 | K1 colour key + K3 tally of colours (+ matching parts) |
| S1-06 (P4-06) | Factor or Not? | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S1-07 (P4-07) | Multiples Maze | 1 | K6 route closes at FINISH |
| S1-08 (P4-08) | Common Factors | 2 | K1 code word (6 letters) |
| S1-09 (P4-09) | Number Riddles | 2 | K1 code word (6 letters) |
| S1-10 (P4-10) | Long Multiplication | 1 | K1 code word (6 letters) |
| S1-11 (P4-11) | Colour the Lorry | 2 | K1 colour key + K3 tally of colours (+ matching parts) |
| S1-12 (P4-12) | Division | 2 | K1 code word (6 letters) |
| S1-13 (P4-13) | Number Ring | 2 | K8 the loop closes: the last arrow brings the pupil back to the start  |
| S1-14 (P4-14) | Mixed or Improper | 1 | K1 code word (6 letters) |
| S1-15 (P4-15) | Fraction Number Line | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S1-16 (P4-16) | Fraction of a Set | 1 | K1 code word (6 letters) |
| S1-17 (P4-17) | Fraction Sums | 2 | K1 code word (6 letters) |
| S1-18 (P4-18) | Name the Angle | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S1-19 (P4-19) | Protractor Readings | 2 | K1 code word (6 letters) |
| S1-20 (P4-20) | Fraction Stories | 2 | K1 code word (6 letters) |
| S2-01 (P4-21) | Decimal Place Value | 1 | K1 code word (6 letters) |
| S2-02 (P4-22) | Order the Decimals | 1 | K1 letters in order spell a word (6 letters) + each card used once |
| S2-03 (P4-23) | Decimal Match | 1 | K1 letters of the matching cards spell a word (6 letters), 4 decoy car |
| S2-04 (P4-24) | Rounding Decimals | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S2-05 (P4-25) | Magic Decimals | 2 | K3 every row, column and corner-to-corner line makes the same total |
| S2-06 (P4-26) | Decimal Shares | 2 | K1 code word (6 letters) |
| S2-07 (P4-27) | Missing Sides | 1 | K1 code word (6 letters) |
| S2-08 (P4-28) | L-Shapes | 1 | K1 code word (6 letters) |
| S2-09 (P4-29) | Match the Figures | 2 | K1 letters of the matching figures spell a word (6 letters), the lette |
| S2-10 (P4-30) | Joined Shapes | 2 | K1 code word (6 letters) |
| S2-11 (P4-31) | Shape Facts | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S2-12 (P4-32) | Complete the Corner | 2 | K1 the letter of the point that completes each shape spells a word (6  |
| S2-13 (P4-33) | Mirror Lines | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S2-14 (P4-34) | Complete the Figure | 2 | K1 code word (6 letters) |
| S2-15 (P4-35) | Name the Solid | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S2-16 (P4-36) | Which Net? | 2 | K1 the letter of the right choice in each row spells a word (6 letters |
| S2-17 (P4-37) | Complete the Table | 2 | K3 rows and columns add to their totals + K1 code word (6 letters) |
| S2-18 (P4-38) | Line Graph Detective | 1 | K1 code word (6 letters) |
| S2-19 (P4-39) | Pie Chart | 2 | K1 code word (6 letters) |
| S2-20 (P4-40) | Colour the Ferry | 2 | K1 colour key + K3 tally of colours (+ matching parts) |

## Rules every page keeps

Black and white only (#000/#fff, strokes at least 0.57 pt); A4 with 15 mm margins; every sentence on a page at most 14 words (a fraction counts as one word), at most 4 instruction sentences; answer boxes at least 12 mm high (14 by 11 mm on the colour-by-code pages); no Mi, MOE, alignment or price wording (the cover has one not-affiliated sentence). Code words: exactly one arrangement of the letters is a word, so no wrong placement of the answers spells a word, tested against the 241 000-word list. Wrong-answer enumeration at 95% or better on every page. See `validate.py` for the full list.
