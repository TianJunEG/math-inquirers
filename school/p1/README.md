# Early Finisher Puzzles, Primary 1 (pilot)

Pilot of the school early-finisher puzzle workbook (plan: `docs/school_books/plan.md`; owner decisions: `docs/terms/owner_decisions.md` addenda 5 to 10).
20 single-sided A4 pages, every page self-checking, pure black and white, school name printed in each page footer, teacher answer key with syllabus topic tags.
Not for sale as is: it is a pilot for owner review (see open questions).

## Regenerate

```
cd school/p1
python3 build.py --school "Name of School"   # omit --school to print a blank line to write the name on
python3 validate.py                          # 197 checks; exit code 1 on any failure
```

Needs: python3 with `playwright` (chromium), `pypdf`, `Pillow`; poppler (`pdftoppm`, `pdfinfo`, `pdffonts`, `pdftotext`); fonts from `/fonts/node_modules/@fontsource` (Fredoka, Nunito Sans).
All puzzles are generated from fixed seeds, so a rebuild gives identical puzzles. Only the footer changes with `--school`.

Outputs in `out/`:

| File | Pages | Use |
|---|---|---|
| `P1_Puzzles.pdf` | 20 | The pupil pages P1-01 to P1-20. Photocopy these. |
| `P1_FrontMatter.pdf` | 4 | Cover, photocopy licence, teacher notes (with pack contents), contents list |
| `P1_Complete_Pack.pdf` | 24 | Front matter (4) + puzzles (20): the whole printable pack |
| `P1_Answer_Key.pdf` | 8 | Teacher key: intro and topic coverage, then answers, check result, syllabus tag and note for each page |
| `verification.json`, `validation_report.txt` | | Machine record of every check |

The committed PDFs are built without a school name (blank line in the footer). `out/*.html` and `out/bilevel_check/` are regenerated and not committed.

## Code layout

- `gen/common.py` code tables (K1), single-slip tests, SVG shapes, reading-level helper.
- `gen/pages_numbers.py` pages 1 to 7; `gen/pages_arith.py` pages 8 to 14; `gen/pages_measure.py` pages 15 to 20. Each `pageNN()` makes the puzzle from a seed and then re-solves it with separate solver code (brute force, exhaustive route search, or reading the answer back from the drawn picture) and records the result.
- `render.py` HTML/CSS (black and white only), page frame, front matter, key. `build.py` makes the PDFs. `validate.py` runs all checks.

## Puzzle inventory

Tier: 1 = one star, 2 = two stars. Check mechanisms use the plan's codes: K1 code word, K2 hidden picture, K3 check-sum/total, K4 grid consistency, K6 route closes, K7 put the answer back. "Script result" = the generator's own solver checks (unique solution, check works) passed, then the single-slip detection rate (share of single wrong answers that make the check fail, over every value in the page's number range).

| Page | Topic tag (P1 syllabus) | Puzzle type | Tier | Self-check | Script result |
|---|---|---|---|---|---|
| P1-01 Tens and Ones | Counting: tens and ones (NA Whole Numbers 1.1-1.3) | Code-breaker (count rods and dots) | 1 | K1, 6 letters | 3/3 pass; slips 534/534 |
| P1-02 Mystery Numbers | Numbers to 100: digits, more and less (1.1-1.5) | Number riddles, 3 to 4 clues each, every clue needed | 2 | K1 + K7, 5 letters | 4/4; 495/495 |
| P1-03 Number Cards | Ordering numbers to 100 (1.4, 1.5) | Order 6 cards smallest to greatest | 1 | K1 letters in order, 6 letters | 4/4; all 5 neighbour swaps break the word |
| P1-04 Sticker Grid | Comparing numbers to 100 (1.4, 1.5) | Logic grid 5 x 5 | 2 | K4 | 3/3; unique of 120 placements |
| P1-05 Missing Numbers | Number patterns (1.6) | 6 patterns, one missing number each | 1 | K1, 6 letters | 4/4; 600/600 |
| P1-06 Count On Maze | Number patterns, count on by 5 (1.6) | Maze 5 x 5 with dead ends | 2 | K6 | 2/2; exactly 1 route |
| P1-07 The Queue | Ordinal numbers 1st to 5th (1.7) | Logic (queue of 5) | 1 | K1 shirt letters + K4 | 3/3; unique of 120 orders |
| P1-08 Make Twelve | Addition within 20 (2.1-2.4, 2.7) | Maze 5 x 5 on sums that make 12 | 1 | K6 | 3/3; exactly 1 route |
| P1-09 Magic Square | Adding three 1-digit numbers (2.4) | Magic square, 3 givens | 2 | K3, 8 line totals = 15 | 2/2; unique of 362 880 arrangements; 48/48 |
| P1-10 Take Away Code | Subtraction within 20, missing number (2.1-2.3, 2.7) | Code-breaker | 1 | K1 + K7, 6 letters | 5/5; 114/114 |
| P1-11 Shape Sums | Add and subtract within 20, find the number (2.1-2.4) | Picture equations (two sets of 3 shapes) | 2 | K7 + K1, 6 letters | 4/4; 48/48 |
| P1-12 Shade the Picture | Add and subtract within 100, no renaming (2.5-2.7) | Colour by answer, heart | 1 | K2 | 3/3; see note 1 |
| P1-13 Equal Groups | Multiplication: equal groups (3.1, 3.2) | Code-breaker (count bags and dots) | 1 | K1, 6 letters | 4/4; 234/234 |
| P1-14 Times and Share | Multiplication within 40, division within 20 (3.2-3.4) | Colour by answer, house | 2 | K2 | 3/3; see note 1 |
| P1-15 Coin Purses | Money: cents up to $1 | Code-breaker | 1 | K1, 5 letters | 4/4; 475/475 |
| P1-16 Shop Prices | Money: dollars, more and less | Logic grid 5 x 5 with "$ more than" clues | 2 | K4 | 4/4; unique of 120 placements |
| P1-17 How Long? | Length in cm (Measurement 1.1-1.3) | Code-breaker (read a ruler drawn at 10 mm to 1 cm) | 1 | K1, 6 letters | 3/3; 66/66 |
| P1-18 Clock Time | Time to 5 minutes, 1 hour and half hour later (Measurement 2.1-2.4) | Code-breaker (clock faces) | 2 | K1, 5 letters | 4/4; 714/715 |
| P1-19 Shape Count | 2D shapes, shapes in a figure (Geometry 1.1, 1.3) | Count shapes + code | 2 | K3 (total 15) + K1, 5 letters | 4/4; 40/40 |
| P1-20 Fruit Graph | Picture graphs (Statistics) | Graph detective, 3 missing rows from clues | 2 | K3 (total circles) | 5/5; 12/12 |

Mix: 10 one-star, 10 two-star. Strands: whole numbers 7 pages, add/subtract 5, multiply/divide 2, money 2, length 1, time 1, shapes 1, picture graph 1. Types: 7 code-breakers or code pages, 2 colour-by-answer, 2 mazes, 2 logic grids plus the queue, 1 magic square, 1 picture-equation page, 1 riddle page, 1 pattern page, 1 ordering page, 1 shape count, 1 graph.

Notes on the "Script result" column:
1. Colour-by-answer pages (P1-12, P1-14): a slip changes the picture only when it moves an answer into or out of the shaded set, so only 72% and 76% of the tested slips (plus or minus 1 or 10; plus or minus 1 or 2) show up. This is below the plan's 98% target (V3). Decoy answers are placed next to the shaded values to push the rate up. See open question 3.
2. Mazes: the "slip" figures are the number of dead-end decoy boxes (a wrong step leads nowhere); the route check itself is exact (exhaustive search finds one route).
3. Order, logic and grid pages count wrong full arrangements, not single slips.
4. The code words (ROCKET, CLOUD, BRIDGE, PLANET and others) use distinct letters each. The "does a slip spell another real word" test uses a built-in list of about 350 common words, not a full dictionary, so it is a weaker test than the plan's V4/V5 (open question 5).

## What validate.py checks

- Every puzzle record: unique solution, the check works with the right answers, the check fails for single slips, numbers in the P1 range (V1, V2, V3, V7).
- Reading level (V8, simplified): instruction and clue sentences at most 8 words, at most 4 instruction lines, check text at most 18 words.
- Layout in the browser for all 20 pages (also front matter and key): no overflow, no text clipped, every element inside the 14.5 mm print-safe margin, puzzle content fills at least 55% of the puzzle area, text at least 8 pt, puzzle area never touches the check strip.
- Fonts embedded, A4, 20 / 4 / 24 / 8 pages, school-name footer and page code on every page, file sizes (all under 2 MB).
- Black and white (owner addendum 10): only `#000` and `#fff` in the HTML/CSS, no opacity, alpha or gradients, SVG strokes at least 0.2 mm and rule borders at least 0.25 mm (0.57 pt and 0.7 pt; the minimum asked is 0.5 pt), every PDF page (pupil pages, front matter, key) rendered at 150 dpi as 1-bit and compared with greyscale: bilevel keeps the ink (at most 25% loss on pupil and front pages, 35% on the key, which has small text) and no flat grey tint areas. The 1-bit pages for the pupil pack are written to `out/bilevel_check/` and were viewed. No clue relies on colour: hatching, solid black and labels are used; START and FINISH are white text on solid black.

Not covered by any script: the hand check of every page picture (done once by viewing every page at 50 dpi and a sample at 150 dpi), and any check of age-appropriate content beyond the word rules above.

## Syllabus items not covered by a puzzle

Reading and writing numbers in words, measuring and drawing a line to the nearest cm, am and pm, copying figures on a dot or square grid, forming figures from shapes, the number sentence signs on their own. Ordinals stop at 5th (syllabus goes to 10th). Division and multiplication appear on two pages only. The owner may want to swap pages if wider coverage matters.

## Page rules used

Black and white only; A4, 15 mm margins (all content inside 14.5 mm); body text 15 pt, check text 14 pt, footer 8 pt; instruction sentences at most 8 words; numerals for quantities; answer boxes at least 12 mm high; all puzzles original (own generators, own number sets; no contest, book or past-paper problem used). No Mi, no alignment or affiliation wording on pupil pages. The licence page and teacher notes carry no endorsement claim; the key names the syllabus edition in plain words.

## Open questions for the owner

1. Product name: "Early Finisher Puzzles, Primary 1" is a working title. Final school-neutral name?
2. Publisher line on every page is "(c) 2026 Preciouslyours Pte Ltd" with the licence wording "Photocopy licence: [school] only. Not for resale." Entity name, year and the wording need owner (and lawyer) approval. The licence page text is a draft in `render.py` (`licence()`); no price, contact address or term (perpetual or annual) is stated yet.
3. Colour-by-answer pages detect fewer slips (72% and 76%). Accept, add a check-sum line (for example "row 3 has 4 shaded boxes"), or replace them with code-word pages?
4. Teacher key states the syllabus edition and page numbers (Primary 1, pages 31 and 32, 2021 edition) in plain text. Keep, or move to the product page?
5. Larger word list and a proper reading-level word list for the V4, V5 and V8 tests are not built; the checks here are simplified.
6. A pupil trial (4 to 6 children) is still needed: especially P1-06 and P1-08 mazes, the 10-square rods on P1-01, the ruler on P1-17 (read against a drawn ruler, not a school ruler) and the clocks on P1-18.
7. Independent audit (plan section 11): hand-solve 20% of pages, mono photocopy test on a real copier, and the V9 non-copy comparison against `hp/qbank.json`, which is not run here.
8. Is 10 one-star and 10 two-star the right split, and is the strand spread acceptable (whole numbers 7 of 20)? Is "1 star" labelling shown to pupils only as star symbols plus the teacher note?
9. Printed bulk option: the front matter says copies can be ordered. Print route, loose-leaf layout and prices are not decided.
