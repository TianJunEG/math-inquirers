# Early Finisher Puzzles, Primary 3: two semester booklets (pilot)

Two booklets of 20 single-sided A4 pages each (Semester 1 = Terms 1 and 2, Semester 2 = Terms 3 and 4; the split follows the typical order, schools vary), 40 pages in all, P3-01 to P3-40 (Semester 1 is P3-01 to P3-20, Semester 2 is P3-21 to P3-40; the footer code prints both numbers, for example `S2-07 (P3-27)`).
Every page is self-checking, pure black and white, with the school name line and the copyright line in the footer, and each booklet has its own teacher answer key with outcome tags. Each booklet is 10 one-star and 10 two-star pages.
Not for sale as is: a pilot for owner review. Cover, licence, teacher notes and keys carry DRAFT stamps, the business email pypteltd@gmail.com and the registered office address (66 Tannery Ln, Singapore 347805); the licence is an annual licence whose wording is for a lawyer to approve.
Plan: `docs/school_books/p3_semester_booklets_plan.md`; build report and open items: `docs/school_books/p3_semester_booklets_build_report.md`; outcome wording: `docs/school_books/p3_outcome_wording.md`; owner decisions: `docs/terms/owner_decisions.md`.

This pipeline was copied from `school/p2` (P1, P2 and `school/colour_by_code` are not touched by it) and parameterised for Primary 3: 34 outcome lines, reading load 18 words a sentence, numbers to 10 000, tables 6 to 9, division with remainder, equivalent fractions and simplest form, money in decimal notation, km, m, cm, kg, g, ℓ, mℓ, seconds, the 24-hour clock, start, finish and duration, area and perimeter, right angles, perpendicular and parallel lines and bar graphs.

## Regenerate

```
cd school/p3
python3 build.py --school "Name of School"   # both booklets; omit --school to print a blank line to write the name on
python3 build.py --booklet S1                # one booklet
python3 build.py --final                     # leave out the DRAFT stamps (only after the owner and a lawyer approve the front matter)
python3 validate.py                          # every check; exit code 1 on any failure (about 12 minutes)
python3 validate.py --partial                # work in progress
python3 similarity_check.py                  # compare the printed text with the private sources (counts only; needs the gitignored docs/books/private_* files)
python3 preview.py 1 2 3 --dpi 75 --bw       # developer preview: PNGs of pupil pages
```

Needs: python3 with `playwright` (chromium), `pypdf`, `Pillow`, `shapely`, `fonttools`, `brotli`, `numpy`, `scipy`, `wordfreq` (only to rebuild the word list); poppler (`pdftoppm`, `pdfinfo`, `pdffonts`, `pdftotext`); fonts from `fonts/node_modules/@fontsource` (Fredoka, Nunito Sans).
All puzzles come from fixed seeds, so a rebuild gives identical puzzles. Only the footer changes with `--school`.

Outputs in `out/`: `P3_S1_Puzzles.pdf`, `P3_S2_Puzzles.pdf` (20 pages each, photocopy these), `P3_S?_FrontMatter.pdf` (5 pages), `P3_S?_Complete_Pack.pdf`, `P3_S?_Answer_Key.pdf`, `verification.json`, `validation_report.txt`, `similarity_report.txt` (committed); `out/*.html` and `out/bilevel_check/` are not committed.

## Code layout

- `gen/outcomes.py`: the 34 outcome lines, the outcomes of each page (filled when `build.py` runs) and the page order of each booklet.
- `gen/common.py` code tables, word lists (`words_en.txt.gz`: 262 542 words), SVG shapes; `gen/kit.py` safe code words, routes, the standard code-word record; `gen/p3kit.py` number formatting, the code-word page, lettered-choice pages, 4-digit vertical sums; `gen/art.py`, `art2.py` (clocks, coins, notes from P2), `art3.py` (new Primary 3 drawings and their readers); `gen/css_p3.py` CSS.
- Page modules: `gen/pages_s1a.py` (P3-01 to 05), `pages_s1b.py` (06 to 09), `pages_s1c.py` (10 to 13), `pages_s1d.py` (15 to 20), `pages_s2a.py` (21 to 25), `pages_s2b.py` (26 to 29), `pages_s2c.py` (30 to 33), `pages_s2d.py` (34 to 38), `pages_cbc.py` (14, 39, 40: colour by code from `cbc_vendor/`, a copy of `school/colour_by_code` with a Primary 3 bank file `banks_p3.py`).
  Each `pageNN()` makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED text or drawing (not the generator's data), and hands `validate.py` a `model` for the independent wrong-answer enumeration.
- `render.py` HTML/CSS, page frame, front matter and key per booklet. `build.py` makes the PDFs. `validate.py` runs all checks. `similarity_check.py` compares with the private sources.

## The 40 pages

| Code | Title | Stars | Check |
|---|---|---|---|
| S1-01 (P3-01) | Place Value | 1 | K1 code word (6 letters) |
| S1-02 (P3-02) | Words and Numbers | 1 | K6 route closes at FINISH through the stated number of boxes |
| S1-03 (P3-03) | Digit Cards | 2 | K1 code word (6 letters) |
| S1-04 (P3-04) | Compare and Order | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S1-05 (P3-05) | Number Patterns | 2 | K1 the letter of the right choice in each row spells a word (6 letters |
| S1-06 (P3-06) | Big Sums | 1 | K1 code word (6 letters) |
| S1-07 (P3-07) | Mental Pairs | 1 | K6 route closes at FINISH |
| S1-08 (P3-08) | Missing Digits | 2 | K1 code word (6 letters) |
| S1-09 (P3-09) | Tables Maze | 1 | K6 route closes at FINISH |
| S1-10 (P3-10) | True or False Tables | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S1-11 (P3-11) | Remainders | 1 | K1 code word (6 letters) |
| S1-12 (P3-12) | Fact Families | 2 | K8 the loop closes: every number joined by = matches |
| S1-13 (P3-13) | Multiply and Divide | 2 | K1 code word (6 letters) |
| S1-14 (P3-14) | Colour the Fish | 2 | CBC colour by code (tally and matching parts) |
| S1-15 (P3-15) | Equal Fractions | 1 | K1 the letter of the right choice in each row spells a word (6 letters |
| S1-16 (P3-16) | Simplest Form | 1 | K6 route closes at FINISH |
| S1-17 (P3-17) | Fraction Gaps | 2 | K1 code word (6 letters) |
| S1-18 (P3-18) | Fraction Order | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S1-19 (P3-19) | Fraction Sums | 2 | K1 code word (6 letters) |
| S1-20 (P3-20) | Money Sums | 1 | K1 code word (6 letters) |
| S2-01 (P3-21) | Jugs and Beakers | 1 | K1 code word (6 letters) |
| S2-02 (P3-22) | Equal Measures | 1 | K6 route closes at FINISH |
| S2-03 (P3-23) | Kilograms and Grams | 1 | K1 code word (6 letters) |
| S2-04 (P3-24) | Road Trip | 2 | K1 code word (6 letters) |
| S2-05 (P3-25) | Order the Measures | 2 | K1 letters in order spell a word (6 letters) + K4 each card used once |
| S2-06 (P3-26) | Seconds | 1 | K1 code word (6 letters) |
| S2-07 (P3-27) | The 24-Hour Clock | 1 | K1 the letter of the right choice in each row spells a word (5 letters |
| S2-08 (P3-28) | Start and Finish | 2 | K1 the letter of the right choice in each row spells a word (6 letters |
| S2-09 (P3-29) | Time Detective | 2 | K1 code word (6 letters) |
| S2-10 (P3-30) | Square Units | 1 | K1 code word (6 letters) |
| S2-11 (P3-31) | Perimeter | 1 | K1 code word (6 letters) |
| S2-12 (P3-32) | Area Sums | 2 | K1 code word (6 letters) |
| S2-13 (P3-33) | Same or Different? | 2 | K1 the letter of the right choice in each row spells a word (5 letters |
| S2-14 (P3-34) | Right Angles | 1 | K1 the letter of the right choice in each row spells a word (5 letters |
| S2-15 (P3-35) | Line Detective | 1 | K1 the letter of the right choice in each row spells a word (5 letters |
| S2-16 (P3-36) | Draw the Lines | 2 | K1 the letter on the top edge where the drawn line ends spells a word  |
| S2-17 (P3-37) | Bar Graph Detective | 1 | K1 code word (6 letters) |
| S2-18 (P3-38) | Different Scales | 2 | K1 code word (6 letters) |
| S2-19 (P3-39) | Colour the House | 2 | CBC colour by code (tally and matching parts) |
| S2-20 (P3-40) | Colour the Butterfly | 2 | CBC colour by code (tally and matching parts) |

## Rules every page keeps

Black and white only (#000/#fff, strokes at least 0.57 pt); A4 with 15 mm margins; instruction and clue sentences at most 18 words, at most 3 lines; answer boxes at least 12 mm high; counted squares 8 mm; money as $3.45 (two decimal places); no Mi, MOE, alignment or price wording (the cover has the one not-affiliated sentence, the licence page the factual syllabus sentence). Code words: exactly one arrangement of the letters is a word, tested against 262 542 words. Wrong-answer enumeration at 95% or better on every page. See `validate.py` for the full list.
