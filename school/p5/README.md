# Early Finisher Puzzles, Primary 5: two semester booklets (draft)

Two booklets of 20 single-sided A4 pages (Semester 1 = Terms 1 and 2, Semester 2 = Terms 3 and 4; typical order, schools vary), P5-01 to P5-40, footer `S1-07 (P5-07)`. Every page is self-checking, pure black and white, ten one-star and ten two-star pages per booklet. Cover, licence, teacher notes and keys carry DRAFT stamps; the licence is an annual licence for a lawyer to approve. Pipeline copied from `school/p2` (nothing else edited).
Plan: `docs/school_books/p5_semester_booklets_plan.md` (outcome gap analysis, page table, exclusions). Build report and weak points: `docs/school_books/p5_semester_booklets_build_report.md`. Outcome lines: `docs/school_books/p5_outcome_wording.md` (copied from the syllabus PDF, pp. 41-42).

## Regenerate

```
cd school/p5
python3 build.py --school "Name of School"   # both booklets; omit --school for a blank line
python3 build.py --booklet S1
python3 build.py --final                     # no DRAFT stamps (only after owner and lawyer approve)
python3 validate.py                          # all checks, about 2.5 minutes; exit code 1 on a failure
python3 preview.py 1 2 3 --dpi 75 --bw       # PNG preview of pupil pages
```
Needs python3 with playwright (chromium), pypdf, Pillow, shapely, fonttools, brotli, numpy, scipy; poppler; the fonts in `fonts/node_modules/@fontsource`; for the word list only a rebuild of `gen/words_en.txt.gz` needs `english-words` and `wordfreq`. Seeds are fixed, so rebuilds are identical. Outputs in `out/`: Puzzles, FrontMatter, Complete_Pack, Answer_Key per booklet, `verification.json`, `validation_report.txt` (html and `bilevel_check/` are not committed).

## Code layout

- `gen/outcomes.py` outcome lines (own wording), booklet order. `gen/kit.py` safe code words, `gen/kit5.py` exact-fraction reader of printed arithmetic and the page builders (code word, lettered choices, ordering, matching, route). `gen/art5.py` figures with data-attributes the solvers read. `gen/numwords.py` numbers in words.
- Pages: `pages_s1a.py` (P5-01 to 07 except 05), `pages_s1b.py` (08 to 13), `pages_s1c.py` (14 to 20), `pages_s2a.py` (21, 23 to 27), `pages_s2b.py` (28 to 35), `pages_s2c.py` (36 to 40), `pages_cbc.py` (05 and 22, colour by code from `cbc_vendor/` with `banks_p5.py`). Each `pageNN()` makes the puzzle from a seed, re-solves it with separate code that reads the printed text or drawing, and hands `validate.py` a model for the wrong-answer enumeration.
- `render.py` HTML/CSS, front matter and key. `build.py` makes the PDFs. `validate.py` runs the checks.
