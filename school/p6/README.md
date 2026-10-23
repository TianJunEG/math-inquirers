# Early Finisher Puzzles, Primary 6: two semester booklets (pilot)

Two booklets of 20 single-sided A4 pages each (Semester 1 = Terms 1 and 2, Semester 2 = Terms 3 and 4; the split follows the typical order, schools vary), 40 pages in all, P6-01 to P6-40 (build order; the footer code prints both numbers, for example `S1-07 (P6-17)`).
Every page is self-checking, pure black and white, with the school name line and the copyright line in the footer, and each booklet has its own teacher answer key with outcome tags in the syllabus PDF's wording. Each booklet is 10 one-star and 10 two-star pages.
Not for sale as is: a pilot for owner review. Cover, licence, teacher notes and keys carry DRAFT stamps, the business email pypteltd@gmail.com and the registered office address (66 Tannery Ln, Singapore 347805); the licence is an annual licence (one school year, renewable) whose wording is for a lawyer to approve.
Plan: `docs/school_books/p6_semester_booklets_plan.md`; build report and open items: `docs/school_books/p6_semester_booklets_build_report.md`; outcome wording: `docs/school_books/p6_outcome_wording.md`; owner decisions: `docs/terms/owner_decisions.md`.

This pipeline was copied from `school/p2` (P2 is not touched by it) and parameterised for Primary 6: the Standard-track outcomes of our summary (Primary 6 pages 43 and 44 and the Foundation pages 49 and 50 of the syllabus PDF, read 23 Oct 2026), reading load of 18 words a sentence, fractions divided by whole numbers and fractions, ratio, percentage, algebra with one letter, circles and composite figures, volume with square and cube roots, angles in figures, average, and a vendored colour-by-code library (`cbc_vendor`).

## Regenerate

```
cd school/p6
python3 build.py --school "Name of School"   # both booklets; omit --school to print a blank line to write the name on
python3 build.py --booklet S1                # one booklet
python3 build.py --final                     # leave out the DRAFT stamps (only after the owner and a lawyer approve the front matter)
python3 validate.py                          # every check; exit code 1 on any failure (several minutes)
python3 validate.py --partial                # work in progress: not every one of the 40 pages exists yet
python3 preview.py 1 2 3 --dpi 75 --bw       # developer preview: PNGs of pupil pages
```

Needs: python3 with `playwright` (chromium), `pypdf`, `Pillow`, `shapely`, `fonttools`, `brotli`, `numpy`, `scipy`; poppler (`pdftoppm`, `pdfinfo`, `pdffonts`, `pdftotext`); fonts from `fonts/node_modules/@fontsource` (Fredoka, Nunito Sans).
All puzzles come from fixed seeds, so a rebuild gives identical puzzles. Only the footer changes with `--school`.

Outputs in `out/`: `P6_S1_Puzzles.pdf`, `P6_S2_Puzzles.pdf` (20 pages each, photocopy these), `P6_S?_FrontMatter.pdf` (5 pages), `P6_S?_Complete_Pack.pdf`, `P6_S?_Answer_Key.pdf`, `verification.json`, `validation_report.txt` (committed); `out/*.html` and `out/bilevel_check/` are not committed.

## Code layout

- `gen/outcomes.py`: the Primary 6 outcome lines (our summary wording, the Ministry PDF is not in the repository), the revision lines, and the page order of each booklet (the only place the semester split lives).
- `gen/kit.py` and `gen/kit6.py`: safe code words (distinct letters, one arrangement, no wrong placement spells another word), code-word, route, choice, matching, ordering and domino-loop page makers with their checks. `gen/common.py`: code tables and word lists. `gen/figs.py`, `gen/angles.py`: circle, composite, cuboid, pie, net and angle figures with readers that re-measure the printed drawing. `gen/css_p6.py`: CSS.
- Page modules: `gen/pages_a.py` to `pages_g.py` (P6-01 to P6-40, except the colour pages), `gen/pages_cbc.py` (P6-09, 32, 40, colour by code via the vendored copy in `cbc_vendor`, with a P6 bank `banks_p6.py`).
  Each page is made from a seed, re-solved by separate solver code that reads the PRINTED text or drawing, and handed to `validate.py` with a `model` of its wrong answers.
- `render.py` HTML/CSS, page frame, front matter and key per booklet. `build.py` makes the PDFs. `validate.py` runs all checks. `similarity_check.py` compares the pupil text with the private, gitignored sources (counts only). `devcheck.py` quick layout check.

## The 40 pages

| Code | Title | Stars | Check |
|---|---|---|---|
| S1-01 (P6-01) | Fraction Shares | 1 | Code-breaker (fractions) |
| S1-02 (P6-02) | Dividing by Fractions | 1 | Maze / path |
| S1-03 (P6-03) | Fraction Stories | 2 | Choice table (stories) |
| S1-04 (P6-04) | Equal Ratios | 1 | Matching (equal ratios) |
| S1-05 (P6-05) | Missing Terms | 1 | Code-breaker (equivalent ratios) |
| S1-06 (P6-06) | Share in a Ratio | 1 | Code-breaker (sharing in a ratio) |
| S1-07 (P6-07) | Three Quantities | 2 | Code-breaker (ratio of three quantities) |
| S1-08 (P6-08) | Fractions and Ratios | 2 | Choice table (ratio and fraction) |
| S1-09 (P6-09) | Colour the Car | 2 | Colour by code (pupils colour with their own crayons) |
| S1-10 (P6-10) | Find the Whole | 1 | Code-breaker (percentage) |
| S1-11 (P6-11) | Percent Up and Down | 1 | Maze / path |
| S1-12 (P6-12) | Percent Stories | 2 | Code-breaker (percentage stories) |
| S1-13 (P6-13) | Letters for Numbers | 1 | Choice table (expressions) |
| S1-14 (P6-14) | Simplify | 1 | Matching (simplest form) |
| S1-15 (P6-15) | Substitute | 2 | Domino loop (substituting) |
| S1-16 (P6-16) | Find the Letter | 2 | Code-breaker (equations) |
| S1-17 (P6-17) | Round and Round | 1 | Code-breaker (circumference) |
| S1-18 (P6-18) | Circle Areas | 2 | Code-breaker (area) |
| S1-19 (P6-19) | Half and Quarter | 2 | Matching (areas and perimeters) |
| S1-20 (P6-20) | Curves and Corners | 2 | Ordering (areas of composite figures) |
| S2-01 (P6-21) | Shaded Shapes | 1 | Code-breaker (composite areas) |
| S2-02 (P6-22) | Perimeter Pick | 2 | Choice table (perimeters) |
| S2-03 (P6-23) | Cuboid Corners | 1 | Code-breaker (missing dimension) |
| S2-04 (P6-24) | Root Maze | 1 | Maze / path |
| S2-05 (P6-25) | Base and Height | 2 | Matching (base area, height, face) |
| S2-06 (P6-26) | Tank Stories | 2 | Code-breaker (tanks) |
| S2-07 (P6-27) | Angles in Figures | 1 | Code-breaker (unknown angles) |
| S2-08 (P6-28) | More Angles | 2 | Code-breaker (unknown angles) |
| S2-09 (P6-29) | Angle Match | 1 | Matching (angles) |
| S2-10 (P6-30) | Average | 1 | Code-breaker (average) |
| S2-11 (P6-31) | Missing Value | 2 | Code-breaker (average, total and number) |
| S2-12 (P6-32) | Colour the Butterfly | 2 | Colour by code (pupils colour with their own crayons) |
| S2-13 (P6-33) | Pie Chart | 2 | Code-breaker (pie chart) |
| S2-14 (P6-34) | Fraction Order | 1 | Ordering (fraction divisions) |
| S2-15 (P6-35) | Ratio Stories | 2 | Code-breaker (ratio stories) |
| S2-16 (P6-36) | Circle Choices | 1 | Choice table (circles) |
| S2-17 (P6-37) | Decimal Maze | 1 | Maze / path |
| S2-18 (P6-38) | GST and Discount | 1 | Code-breaker (GST, discount, interest) |
| S2-19 (P6-39) | Mixed Bag | 2 | Domino loop (mixed) |
| S2-20 (P6-40) | Colour the Elephant | 2 | Colour by code (pupils colour with their own crayons) |
