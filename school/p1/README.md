# Early Finisher Puzzles, Primary 1 (pilot)

Pilot of the school early-finisher puzzle workbook (plan: `docs/school_books/plan.md`; owner decisions: `docs/terms/owner_decisions.md` addenda 5 to 10).
20 single-sided A4 pages, every page self-checking, pure black and white, school name printed in each page footer, teacher answer key with syllabus topic tags.
Not for sale as is: it is a pilot for owner review (see open questions).

## Regenerate

```
cd school/p1
python3 build.py --school "Name of School"   # omit --school to print a blank line to write the name on
python3 validate.py                          # 322 checks; exit code 1 on any failure
```

Needs: python3 with `playwright` (chromium), `pypdf`, `Pillow`; poppler (`pdftoppm`, `pdfinfo`, `pdffonts`, `pdftotext`); fonts from `/fonts/node_modules/@fontsource` (Fredoka, Nunito Sans).
All puzzles are generated from fixed seeds, so a rebuild gives identical puzzles. Only the footer changes with `--school`.

Outputs in `out/`:

| File | Pages | Use |
|---|---|---|
| `P1_Puzzles.pdf` | 20 | The pupil pages P1-01 to P1-20. Photocopy these. |
| `P1_FrontMatter.pdf` | 5 | Cover, photocopy licence, teacher notes (2 pages, with pack contents), contents list |
| `P1_Complete_Pack.pdf` | 25 | Front matter (5) + puzzles (20): the whole printable pack |
| `P1_Answer_Key.pdf` | 10 | Teacher key: intro and topic coverage, then answers, check result, syllabus tag, note and a small solved picture for each page, then one full answer page for each colour-by-code page |
| `verification.json`, `validation_report.txt` | | Machine record of every check, including the wrong-answer enumeration per page |

The committed PDFs are built without a school name (blank line in the footer). `out/*.html` and `out/bilevel_check/` are regenerated and not committed.

## Code layout

- `gen/common.py` code tables (K1), single-slip tests, SVG shapes, reading-level helper.
- `gen/pages_numbers.py` pages 2 to 5 and 7; `gen/pages_arith.py` pages 8 to 11 and 13; `gen/pages_measure.py` pages 6 and 15 to 20; `gen/pages_cbc.py` the colour-by-code pages 1, 12 and 14, built with the picture and topic generator copied unchanged from `school/colour_by_code` (commit ebff080) into `cbc_vendor/` so later edits there cannot change this pack. Each `pageNN()` makes the puzzle from a seed, re-solves it with separate solver code (brute force, exhaustive route search, or reading the answer back from the drawn picture), and hands `validate.py` a `model` (right answers, possible values of each answer, the pupil's check as a function) for the independent wrong-answer enumeration.
- `render.py` HTML/CSS (black and white only), page frame, front matter, key. `build.py` makes the PDFs. `validate.py` runs all checks.

## Puzzle inventory

Tier: 1 = one star, 2 = two stars. Check mechanisms use the plan's codes: K1 code word, K2 hidden picture, K3 check-sum/total, K4 grid consistency, K6 route closes, K7 put the answer back. "Enumeration" = the share of single wrong answers (or wrong arrangements) the pupil's own check rejects, counted by `validate.py` independently of the generator; the generator's own solver checks (unique solution, check works) are listed as V1/V2 in `out/validation_report.txt`.

| Page | Topic tag (P1 syllabus) | Puzzle type | Tier | Self-check | Enumeration (see below) |
|---|---|---|---|---|---|
| P1-01 Colour the Rocket | Place value: tens and ones (NA Whole Numbers 1.1-1.3) | Colour by code (CBC): 15 parts, tens-and-ones questions, key of 5 numbers to 5 colours; pupils use own crayons | 1 | K1 colour key + K3 tally of colours + matching parts | 150/150 wrong answers rejected (100%) |
| P1-02 Mystery Numbers | Numbers to 100: digits, more and less (1.1-1.5) | Number riddles, 3 to 4 clues each, every clue needed | 2 | K1 + K7, 5 letters | 100%; 495/495 |
| P1-03 Number Cards | Ordering numbers to 100 (1.4, 1.5) | Order 6 cards smallest to greatest; rows labelled number / letter | 1 | K1 letters in order, 6 letters | 719/719 wrong orders rejected |
| P1-04 Sticker Grid | Comparing numbers to 100 (1.4, 1.5) | Logic grid 5 x 5 with a cross-and-tick example | 2 | K1 letter beside each number, read down the list = HOUSE; K4 as a hint | 119/119 wrong placements rejected |
| P1-05 Missing Numbers | Number patterns (1.6) | 6 patterns, one missing number each | 1 | K1, 6 letters | 100%; 600/600 |
| P1-06 Shape Riddles | 2D shapes: name and describe (Geometry 1.1) | 6 two-part riddles (straight and curved sides) matched to 6 shapes | 2 | K1 shape letters in riddle order, 6 letters (JACKET) | 719/719 wrong orders rejected |
| P1-07 The Queue | Ordinal numbers 1st to 5th (1.7) | Logic (queue of 5) | 2 | K1 shirt letters + K4 | 119/119 wrong orders rejected |
| P1-08 Make Twelve | Addition within 20 (2.1-2.7) | Maze 5 x 5 on sums that make 12 | 1 | K6 with a box count (10 boxes, every box makes 12) | 240/240 single wrong boxes rejected |
| P1-09 Magic Square | Adding three 1-digit numbers (2.1-2.7) | Magic square, 3 givens | 2 | K3, 8 line totals = 15 | 100%; 48/48 |
| P1-10 Take Away Code | Subtraction within 20, missing number (2.1-2.7) | Code-breaker | 1 | K1 + K7, 6 letters | 100%; 114/114 |
| P1-11 Shape Sums | Add and subtract within 20, find the number (2.1-2.7) | Picture equations (two sets of 3 shapes) | 2 | K7 + K1, 6 letters | 100%; 48/48 |
| P1-12 Colour the House | 2D shapes: corners of triangle, square, rectangle, circle (Geometry 1.1) | Colour by code: 17 parts, count corners | 1 | K1 colour key + K3 tally + matching parts + "exactly 2 of 6 wall and window parts are red" | 204/204 (100%) |
| P1-13 Equal Groups | Multiplication: equal groups (3.1-3.3) | Code-breaker (count bags and dots; boxes labelled bags, dots, total) | 1 | K1, 6 letters | 100%; 234/234 |
| P1-14 Colour the Ice Cream | Number patterns, counting in 2s, 5s, 10s (1.6; leads to multiplication) | Colour by code: 12 parts, missing number in a count pattern | 2 | K1 colour key + K3 tally + mirror parts | 1200/1200 (100%) |
| P1-15 Coin Purses | Money: cents up to $1 | Code-breaker | 1 | K1, 5 letters | 100%; 475/475 |
| P1-16 Shop Prices | Money: dollars, more and less | Logic grid 5 x 5, letter beside each price, plus a total looked up in a code table | 2 | K1 (BASKET: 5 price letters + 1 total letter) | 119/119 wrong placements rejected; total 100% |
| P1-17 How Long? | Length in cm (Measurement 1.1-1.3) | Code-breaker (read a ruler drawn at 10 mm to 1 cm) | 1 | K1, 6 letters | 100%; 66/66 |
| P1-18 Clock Time | Time to 5 minutes, 1 hour and half hour later (Measurement 2.1-2.4) | Code-breaker (clock faces; hands never closer than 25 degrees) | 2 | K1, 5 letters | 100%; 715/715 |
| P1-19 Shape Count | 2D shapes, shapes in a figure (Geometry 1.1, 1.3) | Count shapes + code | 1 | K3 (total 15) + K1, 5 letters | 100%; 40/40 |
| P1-20 Fruit Graph | Picture graphs (Statistics) | Graph detective, 3 missing rows from 3 difference clues | 2 | K3: the total (24) is only in the check strip, not a clue | 100%; 27/27 |

Mix: 10 one-star, 10 two-star. Strands: whole numbers 7 pages (P1-01, 02, 03, 04, 05, 07, 14), add/subtract 4, multiply 1, money 2, length 1, time 1, shapes 3 (P1-06, 12, 19), picture graph 1. Types (20): 3 colour by code (P1-01, 12, 14), 6 code-breakers or code pages (P1-10, 13, 15, 17, 18, 19), 1 maze, 3 logic pages (grid P1-04 and P1-16, queue P1-07), 1 magic square, 1 picture-equation page, 1 number-riddle page, 1 shape-riddle page, 1 pattern page, 1 ordering page, 1 graph detective.

Stars (how decided): one star = one skill as usually taught; two stars = the same topics with two steps or two clues to combine. After the audit P1-07 moved to two stars, P1-19 to one star, and the old two-star count-on maze was replaced by the two-star shape-riddle page (P1-06).

How the wrong-answer enumeration works (`validate.py`, section 1b, independent of the generator): for every page it tries every single change of one answer and counts how many the pupil's own check rejects. Two rates must be at least 95%: plausible slips (plus or minus 1, 2, 3, 4, 5 or 10 for number answers; any other value for letters, boxes or times) and every other value in the page's range. Logic and ordering pages are also tested on every wrong arrangement (all permutations: 119 or 719). The build fails if any rate is below 95%. P1-14's all-values rate is exactly 95.0% (two of 40 other values, 4 or 12 or 20, land on the key); the plausible-slip rate is 100%.

Notes on the table:
1. Mazes: the enumeration replaces one box of the right route by any other box on the grid; the route check (adjacent boxes, every box makes 12, 10 boxes, starts at START, ends at FINISH) rejects all 240.
2. The code words use distinct letters each. The "does a wrong answer spell another real word" test uses a built-in list of about 350 common words, not a full dictionary, so it is weaker than the plan's V4/V5 (open question 5).
3. The wrong-arrangement test for P1-04, P1-07 and P1-16 uses the same word list; anagrams of HOUSE, TIGER and BASKET that are real words but not on the list would pass the pupil's check.

## What validate.py checks

- Every puzzle record: unique solution, the check works with the right answers, numbers in the P1 range (V1, V2, V7); and, for every page, the wrong-answer enumeration with a 95% floor (V3, see above).
- Wording and content rules on all printed text: no division sign, money as 50¢ never 50c, no column/diagonal/divide on pupil pages, no Mi, MOE, alignment or affiliation wording on pupil pages or front matter, no price or quote wording, o'clock and half past in the key, every number of 11 or more in a teacher note found on the page, syllabus numbers inside the P1 ranges of `docs/moe/syllabus_by_level.md`, answer boxes at least 12 mm high.
- Colour-by-code pages: the sheet's own checks (one answer per part, all five colours used, tally, matching parts) and a wrong-answer enumeration of every region and every wrong value (at least 95%).
- Reading level (V8, simplified): instruction and clue sentences at most 8 words, at most 4 instruction lines, check text at most 18 words.
- Layout in the browser for all 20 pages (also front matter and key): no overflow, no text clipped, every element inside the 14.5 mm print-safe margin, puzzle content fills at least 55% of the puzzle area, text at least 8 pt, puzzle area never touches the check strip.
- Fonts embedded, A4, 20 / 5 / 25 / 6 pages, school-name footer and page code on every page, file sizes (all under 2 MB).
- Black and white (owner addendum 10): only `#000` and `#fff` in the HTML/CSS, no opacity, alpha or gradients, SVG strokes at least 0.2 mm and rule borders at least 0.25 mm (0.57 pt and 0.7 pt; the minimum asked is 0.5 pt), every PDF page (pupil pages, front matter, key) rendered at 150 dpi as 1-bit and compared with greyscale: bilevel keeps the ink (at most 25% loss on pupil pages, 30% on the text-only front matter, 35% on the key, which has small text) and no flat grey tint areas (at most 40 anti-aliasing blocks per page, 75 on the key). The 1-bit pages for the pupil pack are written to `out/bilevel_check/` and were viewed. No clue relies on colour: hatching, solid black and labels are used; START and FINISH are white text on solid black.

Not covered by any script: the hand check of every page picture (done by viewing every changed page at 70 dpi and clocks, rulers and the new pictures at 150 dpi 1-bit), and any check of age-appropriate content beyond the word rules above.

## Syllabus items not covered by a puzzle

Reading and writing numbers in words, measuring and drawing a line to the nearest cm, am and pm, copying figures on a dot or square grid, forming figures from shapes, the number sentence signs on their own. Ordinals stop at 5th (syllabus goes to 10th). Division and sharing do not appear (the P1-14 sharing boxes were removed when it became a colour-by-code page); multiplication appears on one page (P1-13, equal groups; P1-14 counting in 2s, 5s and 10s leads to it). The owner may want to swap pages if wider coverage matters.

## Page rules used

Black and white only; A4, 15 mm margins (all content inside 14.5 mm); body text 15 pt, check text 14 pt, footer 8 pt; instruction sentences at most 8 words; numerals for quantities; answer boxes at least 12 mm high (checked); money written 50¢, times as o'clock and half past in text; all puzzles original (own generators, own number sets; no contest, book or past-paper problem used). No Mi, no alignment or affiliation wording on pupil pages. The licence page and teacher notes carry no endorsement claim; the key names the syllabus edition in plain words.

## Open questions for the owner

1. Product name: "Early Finisher Puzzles, Primary 1" is a working title. Final school-neutral name?
2. Publisher line on every page is "(c) 2026 Preciouslyours Pte Ltd" with the licence wording "Photocopy licence: [school] only. Not for resale." Entity name, year and the wording need owner (and lawyer) approval. The licence page text is a draft in `render.py` (`licence()`); no price, contact address or term (perpetual or annual) is stated yet.
3. (Resolved, owner instruction 23 Oct.) The weak mark-by-answer pages are replaced by three colour-by-code pages (P1-01, P1-12, P1-14; 3 of 20). Pupils need crayons in five colours; the printed page is black and white and the colour words are in the key. Owner to say whether 3 is right (4 would need a fourth strand swap) and whether crayons can be assumed in early-finisher trays.
4. Teacher key states the syllabus edition and page numbers (Primary 1, pages 31 and 32, 2021 edition) in plain text. Keep, or move to the product page?
5. Larger word list and a proper reading-level word list for the V4, V5 and V8 tests are not built; the checks here are simplified.
6. A pupil trial (4 to 6 children) is still needed: especially P1-06 and P1-08 mazes, the 10-square rods on P1-01, the ruler on P1-17 (read against a drawn ruler, not a school ruler) and the clocks on P1-18.
7. Independent audit (plan section 11): hand-solve 20% of pages, mono photocopy test on a real copier, and the V9 non-copy comparison against `hp/qbank.json`, which is not run here.
8. Is 10 one-star and 10 two-star the right split, and is the strand spread acceptable (whole numbers 7 of 20, number and algebra 14 of 20, multiplication only 1 page)? Is "1 star" labelling shown to pupils only as star symbols plus the teacher note?
9. Printed bulk option: the front matter says copies can be ordered. Print route, loose-leaf layout and prices are not decided.
