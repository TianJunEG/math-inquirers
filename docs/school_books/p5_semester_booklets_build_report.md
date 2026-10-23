# Primary 5 semester booklets: build report

Branch `claude/great-fermi-1hv4vc`, 24 Oct 2026. Pipeline `school/p5/` (copied from `school/p2/`; P1, P2, other levels and `school/colour_by_code` not edited; a Primary 5 bank `banks_p5.py` and four percentage rules were added to the vendored copy `school/p5/cbc_vendor/`). Plan: `docs/school_books/p5_semester_booklets_plan.md`. Outcome wording note: `docs/school_books/p5_outcome_wording.md`. Not sent to anyone, no PR. The independent audit is a separate step and was NOT run by the builder.

## What was built

Two booklets of 20 single-sided A4 pupil pages (`out/P5_S1_Puzzles.pdf`, `P5_S2_Puzzles.pdf`), front matter of 5 pages each (cover, DRAFT licence, two pages of teacher notes, contents with coverage), complete packs of 25 pages and answer keys (9 pages each). 10 one-star and 10 two-star pages in each booklet. Footers read S1-07 (P5-07) and S2-07 (P5-27).

Page table, mechanisms and outcome tags: plan section 4. Mechanisms: code word 16, lettered choices 6, true or false 2, route 4, matching 4, ordering 3, colour by code 2, balance 1, magic square 1, number-chain loop 1.

## Validation

`python3 validate.py` (full, about 2.5 minutes): 737 checks, 0 failed (`out/validation_report.txt`, `out/verification.json`). Additions for Primary 5: no Primary 6 words on pupil pages or key; notation (no letter x for times, cm2 or ml written wrongly, 'degrees'); reading load 16 words a sentence; rendered answer boxes at least 12 mm high and 11 mm wide on the pupil pages; "Pictures are not actual size." and the not-covered note in the teacher notes; the key says the outcome wording is our own summary. Raised or changed limits: the front matter 1-bit ink-loss limit was raised from 32% to 35% (text-heavy notes at 11 pt; viewed); the page-fill and clue-word checks of P2 were adapted (the clue-word list names words a Primary 5 note could misquote).

## Hand-solved from the rendered image

All 40 pages were solved by hand from the 80 dpi render of the final PDFs (and the figure-heavy pages, the P5-21 bars and the P5-32 cubes from 120 to 150 dpi crops) before comparing with the key; every answer agreed (0 wrong keys, 0 pages with two answers). Code words: FLIGHT, FROZEN, BACKUP, CRAFTS, DEVOUR, BEHIND, PEANUT, MELODY, CREAMY, FAMILY, POLICE, FIGURE, HUNGRY, FRUITS, FRIDGE, THIRDS, WALRUS, STUDIO, STRONG, WISDOM, COUSIN, SHRIMP, TEACUP, BANDIT, CURFEW, FATHOM, CAMPUS, KNIGHT, WIZARD, CANOPY, BOTANY (31 distinct words; wrong-box words were enumerated by the script, not by hand). Routes (all 8 boxes, one route): P5-04, 11, 30, 36. Equations P5-07: 10, 88, 21, 184, 7, 14. Magic square P5-10: 2 1/4, 9 3/4, 3 1/2, 12 1/4, 6 (total 21 3/4). Chain P5-12: 40, 70, 77, 35, 56. Colour pages: P5-05 (yellow 2, red 4, blue 3, green 3, orange 3) and P5-22 (yellow 2, red 2, blue 2, green 4, orange 4), every part solved. Pages changed after a first solve (P5-21, 29, 30 and the word cascade of 25 to 40) were solved again on the final render. Colour renders were viewed for every page at 80 dpi; 1-bit copies at 150 dpi (shown reduced) were viewed as contact sheets of all 40 pages: legible, no flat grey.

## Similarity check

Every pupil page text was compared with the private sources (`docs/books/private_*` and `docs/sasmo/private_*`, 23 files, 241 880 seven-word runs): 0 shared seven-word runs; a loose same-numbers-and-words scan gave three false positives (shared colour-tally wording, one rice sentence and a fraction ribbon sentence with different numbers and structure). The question TYPES (fraction of the remainder, unit conversions, GST) are ordinary school types and were taken from `p5_school_paper_patterns.md`; no item, scenario or number set was copied. This check is mine only; the audit should repeat it.

## Weak points (honest list)

1. **Syllabus wording.** The PDF is not in the repository: outcome lines are our own summary of `syllabus_by_level.md`, numbers only where it prints them. Needs the PDF before any wording is claimed.
2. **Average, pie charts and ratio** are in the older school papers but not in the Primary 5 Standard summary; excluded (owner may want a preview page, as the holiday programme has for ratio).
3. **Figures are small.** Cards with figures are about 49 mm wide: base and height labels are about 3.9 mm type, angle figures in the route grid and the lettered-choice cards are smaller still (P5-36, 37, 40). Legible in the 1-bit copy, but a pupil trial should test P5-36, 37, 40 and the 20- and 25-part bars of P5-21 (segments 3.6 mm).
4. **Figures are drawn to scale in most pages but the notes say not to rely on it.** Exception: P5-28 (Height Hunt) relies on the drawing being to scale; the pupil may use a paper corner. A tilted base makes the right angle harder to see than the horizontal ones.
5. **Magic square P5-10** has the well-known 3 by 3 structure; the check strip and the printed total are the check. The four given numbers always allow a line-by-line solution (tested), but a pupil who knows magic squares may shortcut.
6. **Number chain P5-12** does not detect two slips that cancel (a different wrong number carried on); the notes say so. A blank circle is seen at once.
7. **Put-the-answer-back page P5-07** has no code word: the check is substitution; it is weakest against a pupil who does not substitute.
8. **P5-39** uses the three-way statement form (true, false, not possible to tell) of the school papers; "not possible to tell" is always the trapezium angles on different sides.
9. **Interest** (P5-25) is simple interest and says so; whether the syllabus line means simple only cannot be checked without the PDF.
10. **GST** is 9% and stated on the page (7% in older papers).
11. **P5-21** bars of 20 parts are the smallest counted objects (3.6 mm wide, taller than 8 mm).
12. **Colour-by-code** pages use the vendored library with a new Primary 5 bank: answer boxes 9 mm (the audited P2 rule), the pencil-only colour letters are written in the part; a two-line question form was used on P5-22 so that the 9 mm box fits. Small text on the 1-bit copy of P5-05 is about 9 pt.
13. **ℓ glyph** comes from a fallback font (embedded, viewed).
14. No real photocopier test, no pupil trial.
15. Another process commits the working tree as Checkpoint commits, so some files may appear in commits earlier than mine.
16. The word list for the code-word test is about 242 000 words (not 262 000): a union of the P2 list, web2, gcide and wordfreq (183 000 most frequent). Nothing found by the P1 and P2 audits was lost; `siring`, `jailor` and `sonic` are also on the reject list.

## Decisions needed from the owner

- Supply the syllabus PDF (or accept the own-words outcome lines) before any alignment sentence is used.
- Accept the exclusion of average, pie charts and ratio from Primary 5 (or ask for a labelled preview page).
- Whether Semester 1 should carry fractions and decimals and Semester 2 the geometry (schools vary; the notes say to use any page when its topic is taught).
- Simple interest only (P5-25).
- Lawyer wording, pupil trial and photocopier test as for P1 and P2.
- What the colour-by-code library change should be: this pack vendored its own Primary 5 bank. A shared `banks_p5.py` in `school/colour_by_code` would let the gallery use it (not done, library untouched as instructed).

## Library changes wanted (not made)

`school/colour_by_code/banks_p5.py` and the four percentage rules in `textcheck.py` (now in `school/p5/cbc_vendor/`).
