# Early Finisher Puzzles, Primary 1 (pilot)

Pilot of the school early-finisher puzzle workbook (plan: `docs/school_books/plan.md`; owner decisions: `docs/terms/owner_decisions.md` addenda 5 to 10).
20 single-sided A4 pages, every page self-checking, pure black and white, school name printed in each page footer, teacher answer key with syllabus topic tags.
Not for sale as is: it is a pilot for owner review (see open questions). The cover, licence and teacher notes carry DRAFT stamps and contact placeholders until the owner and a lawyer approve the wording.
Second audit (`AUDIT_2.md`) and its fixes: `AUDIT_FIXES_2.md`. First audit: `AUDIT.md`, `AUDIT_FIXES.md`.

## Regenerate

```
cd school/p1
python3 build.py --school "Name of School"   # omit --school to print a blank line to write the name on
python3 build.py --final                     # leave out the DRAFT stamps (only after the owner and a lawyer approve the front matter)
python3 validate.py                          # 381 checks; exit code 1 on any failure (about 40 seconds)
```

Needs: python3 with `playwright` (chromium), `pypdf`, `Pillow`, `shapely`, `fonttools`, `brotli`, `numpy`, `scipy`; poppler (`pdftoppm`, `pdfinfo`, `pdffonts`, `pdftotext`); fonts from `/fonts/node_modules/@fontsource` (Fredoka, Nunito Sans).
All puzzles are generated from fixed seeds, so a rebuild gives identical puzzles. Only the footer changes with `--school`.

Outputs in `out/`:

| File | Pages | Use |
|---|---|---|
| `P1_Puzzles.pdf` | 20 | The pupil pages P1-01 to P1-20. Photocopy these. |
| `P1_FrontMatter.pdf` | 5 | Cover, photocopy licence, teacher notes (2 pages, with pack contents), contents list (all DRAFT-stamped unless built with `--final`) |
| `P1_Complete_Pack.pdf` | 25 | Front matter (5) + puzzles (20): the whole printable pack |
| `P1_Answer_Key.pdf` | 11 | Teacher key: intro and topic coverage, then answers, check result, syllabus tag, note and a small solved picture where one helps (picture, grid, route, magic square and graph pages), then one full answer page for each colour-by-code page |
| `verification.json`, `validation_report.txt` | | Machine record of every check, including the wrong-answer enumeration per page |

The committed PDFs are built without a school name (blank line in the footer). `out/*.html` and `out/bilevel_check/` are regenerated and not committed.

## Code layout

- `gen/common.py` code tables and the code-word tests, the large word lists (`gen/words_en.txt.gz`, about 129 000 words of 2 to 8 letters; `gen/words_common.txt.gz`, the 20 000 most frequent), SVG shapes, reading-level helper.
- `gen/pages_numbers.py` pages 2, 4, 7; `gen/pages_arith.py` pages 3, 5, 8, 9, 10, 11, 13; `gen/pages_measure.py` pages 6, 15 to 20; `gen/pages_cbc.py` the colour-by-code pages 1, 12 and 14, built with the picture and topic generator copied unchanged from `school/colour_by_code` (commit e7d74e1, after its audit fixes) into `cbc_vendor/` so later edits there cannot change this pack. Each `pageNN()` makes the puzzle from a seed, re-solves it with separate solver code (brute force, exhaustive route search, reading the answer back from the drawn picture, or the library's independent text evaluator), and hands `validate.py` a `model` (right answers, possible values of each answer, the pupil's check as a function) for the independent wrong-answer enumeration.
- `render.py` HTML/CSS (black and white only), page frame, front matter, key. `build.py` makes the PDFs. `validate.py` runs all checks.

## Puzzle inventory

Tier: 1 = one star, 2 = two stars. Check mechanisms use the plan's codes: K1 code word, K3 check-sum/total, K4 grid consistency, K6 route closes, K7 put the answer back. "Enumeration" = the share of single wrong answers (or wrong arrangements) the pupil's own check rejects, counted by `validate.py` independently of the generator. Every code-word page also records V3 (no single slip and no swap of two answers spells another word of the 129 000-word list), V4 (guess resistance, see below). Syllabus tags use the outcome numbers or ranges of the Primary 1 section of `docs/moe/syllabus_by_level.md`; `validate.py` checks every topic phrase against that file (F28).

| Page | Topic tag (P1 syllabus) | Puzzle type | Tier | Self-check | Enumeration (plausible slips; all values) |
|---|---|---|---|---|---|
| P1-01 Colour the Rocket | Whole Numbers 1.1 to 1.3 (count a set, tens and ones) | Colour by code (CBC): 15 parts, tens-and-ones questions, key of 5 numbers to 5 colours | 1 | tally + matching left and right parts (6 pairs, all true) | 118/118; 150/150; double slips 1678/1680, swaps 86/88 |
| P1-02 Mystery Numbers | Whole Numbers 1.1 to 1.5 (numbers to 100, compare) | Number riddles, 3 clues each, every clue needed | 2 | K1 + K7, 5 letters (CLOUD) | 60/60; 495/495 |
| P1-03 Fair Shares | Multiplication and Division 3.4 (dividing within 20: sharing and grouping, no division sign) | Code-breaker: share dots equally among plates, put dots into groups of | 1 | K1 + K7, 6 letters (FRIEND) | 56/56; 114/114 |
| P1-04 Sticker Grid | Whole Numbers 1.4, 1.5 (compare and order numbers) | Logic grid 5 x 5 with a cross-and-tick example | 2 | K1 letter beside each number, read down the list = BELOW | arrangements 117/119 (the 2 others are the real words BOWEL and ELBOW) |
| P1-05 Times Code | Multiplication and Division 3.1 to 3.3 (sign x, multiplying within 40) | Code-breaker: a x b, groups of, missing factor (the second multiplication page) | 2 | K1 + K7, 6 letters (SQUARE) | 65/65; 234/234 |
| P1-06 What Time Is It? | Time 2.1 (tell time: o'clock and half past) | Code-breaker: six clocks, o'clock and half past only | 1 | K1, 6 letters (SECOND) | 138/138; 138/138 |
| P1-07 The Queue | Whole Numbers 1.7 (ordinal numbers first to tenth) | Logic (queue of 5; two clues compare two children) | 2 | K1 shirt letters read 1st to 5th = SNAKE | arrangements 117/119 (the others are SNEAK and a second real word) |
| P1-08 Make Twelve | Addition and Subtraction 2.1 to 2.7 (add within 20, mental calculation) | Maze 4 x 4 on sums that make 12 | 1 | K6 with a box count (8 boxes, every box makes 12) | 120/120 |
| P1-09 Magic Square | Addition and Subtraction 2.1 to 2.7 (adding more than two 1-digit numbers) | Magic square, 3 givens, both corner-to-corner lines drawn | 2 | K3, 8 line totals = 15 | 42/42; 48/48 |
| P1-10 Take Away Code | Addition and Subtraction 2.1 to 2.7 (subtract within 20, inverse relationship) | Code-breaker | 1 | K1 + K7, 6 letters (STREAM) | 63/63; 114/114 |
| P1-11 Big Number Sums | Addition and Subtraction 2.1 to 2.7 (within 100: 2-digit and ones, 2-digit and tens, missing number) | Code-breaker | 2 | K1 + K7, 6 letters (FAMILY) | 71/71; 594/594 |
| P1-12 Colour the House | Geometry 1.1 (identify, name, describe 2D shapes) | Colour by code: 17 parts, count corners; matching parts carry small marks | 1 | tally + small marks (6 sets) | 156/156; 204/204; double 2174/2176, swaps 112/114 |
| P1-13 Equal Groups | Multiplication and Division 3.1 to 3.3 (equal groups, sign x, within 40) | Code-breaker (count bags and dots; boxes labelled bags, dots, total) | 1 | K1, 6 letters (NUMBER) | 71/71; 234/234 |
| P1-14 Colour the Ice Cream | Whole Numbers 1.6 (number patterns; counting in 2s, 5s, 10s) | Colour by code: 12 parts, missing number in a count pattern | 2 | tally + matching left and right parts | 144/144; 1200/1200; double 1055/1056, swaps 56/57 |
| P1-15 Coin Purses | Money (count money in cents up to $1) | Code-breaker | 1 | K1, 5 letters (PIANO) | 59/59; 475/475 |
| P1-16 Shop Prices | Money (dollars up to $100) with 2.1 to 2.7 | Logic grid 5 x 5 with a cross-and-tick example, letter beside each price, plus a total looked up in a code table | 2 | K1 (MONDAY: 5 price letters + 1 total letter) | arrangements 119/119; total letter 58/58 |
| P1-17 How Long? | Length 1.1 to 1.3 (measure in cm) | Code-breaker (read a ruler drawn at 10 mm to 1 cm) | 1 | K1, 6 letters (LENGTH) | 50/50; 66/66 |
| P1-18 Clock Time | Time 2.1 and 2.4 (to 5 minutes; 1 hour and half an hour later) | Code-breaker (clock faces; at least 3 of 5 clocks are 5-minute times) | 2 | K1, 5 letters (OCEAN) | 715/715 |
| P1-19 Shape Count | Geometry 1.1, 1.3 (name 2D shapes; shapes in a figure) | Count shapes + code | 1 | K3 (total 15) + K1, 5 letters (ADULT) | 34/34; 40/40 |
| P1-20 Fruit Graph | Statistics: picture graphs | Graph detective, 3 missing rows from 3 difference clues (Grape and Pear differ by different amounts) | 2 | K3 the total (22), and a second sum: the row chosen in a) plus the answer to b) | 40/40 |

Mix: 10 one-star (P1-01, 03, 06, 08, 10, 12, 13, 15, 17, 19), 10 two-star (P1-02, 04, 05, 07, 09, 11, 14, 16, 18, 20). Strands: whole numbers 5 (P1-01, 02, 04, 07, 14), add/subtract 4 (P1-08, 09, 10, 11), multiplication and sharing 3 (P1-03, 05, 13), money 2, time 2 (P1-06, 18), shapes 2 (P1-12, 19), length 1, picture graph 1. Types: 3 colour by code, 11 code-breakers (P1-02, 03, 05, 06, 10, 11, 13, 15, 17, 18, 19), 3 logic pages (P1-04, 07, 16), 1 maze, 1 magic square, 1 graph detective. (P1-19 counts and also uses a code.)

Stars (how decided): one star = one skill as usually taught; two stars = the same topics with two steps or two clues to combine (a missing-number step, a clue that compares two things, two checks to satisfy). P1-07 now has two clues that compare two children (in front of, behind, next to), so it is a two-star page; P1-08 is a 4 x 4 grid (16 sums, 8-box route) so it is a light one-star page; P1-06 is the one-star time page (o'clock and half past only), P1-18 is the two-star time page (5 minutes plus 1 hour or half an hour later) and is marked in the notes as a late-year page.

### Code-word pages: what the strip says and what is tested

The check strip on a code-word page is "Write the letters in order. Do they spell a word?" and nothing more: no category hint (the first version said "Is it in the sky?", which let a pupil guess the word and read the answers off the table). `validate.py` fails any strip that says "Is it ..." or names a category.
- V3: a slip that changes one answer to any other value, and a swap of two answers, must not spell any word of a list of about 129 000 English words (`gen/words_en.txt.gz`: two public word lists plus the 80 000 most frequent words). The table's decoy letters are chosen from letters that cannot form a word with the code word (`bad_letters`), so this holds by construction and by enumeration.
- V4 guess resistance: at least 3 common words (the 20 000 most frequent words) can be made from the letters in the code table, so the word cannot be guessed from its length. On the three logic pages the letters printed beside the numbers (or on the shirts) can be arranged into at least 2 common words (P1-04 BELOW or BOWEL or ELBOW; P1-07 SNAKE or SNEAK; P1-16 MONDAY or DYNAMO). This lowers but does not remove the chance that a bright pupil guesses from the letters; the key and the notes say so. A page where two arrangements are both real words accepts the second word as correct (2 of 119 wrong arrangements on P1-04 and P1-07, so 98.3% are rejected).

How the wrong-answer enumeration works (`validate.py`, section 1b, independent of the generator): for every page it tries every single change of one answer and counts how many the pupil's own check rejects. Two rates must be at least 95%: plausible slips (plus or minus 1, 2, 3, 4, 5 or 10 for number answers; any other value for letters, boxes or times) and every other value in the page's range. Logic and ordering pages are also tested on every wrong arrangement (all permutations: 119). The colour-by-code pages are also tested on every double slip (every pair of regions, every pair of wrong colours) and every swap, 95% each. The build fails if any rate is below 95%.

## What validate.py checks

- Every puzzle record: unique solution, the check works with the right answers, numbers in the P1 range (V1, V2, V7); and, for every page, the wrong-answer enumeration with a 95% floor (V3); code pages: no slip or swap spells a word of the large list (V3, V3c), guess resistance (V4); colour pages: the library's independent evaluator re-solves every printed question from its text and picture, and the printed left-right rule is true (no two parts sit in mirror-image places without being a declared pair).
- Coverage within the 20-page budget: add and subtract within 100, sharing and grouping, two multiplication pages, a one-star o'clock and half past page and the five-minute page; strand counts.
- Wording and content rules on all printed text: no division sign, money as 50¢ never 50c, no column/diagonal/divide on pupil pages, no window/wall/scale wording (parts a pupil cannot find), no Mi, MOE, alignment or affiliation wording on pupil pages or front matter, no price or quote wording, no category hint in a check strip, o'clock and half past in the key, every number of 11 or more in a teacher note found on the page, every clue word named in a teacher note (more than, fewer than, greatest, in front of, behind, ones digit ...) occurs on its page, syllabus numbers inside the P1 ranges and every topic phrase found in `docs/moe/syllabus_by_level.md`, answer boxes at least 12 mm high.
- Front matter: DRAFT stamps and the contact placeholder present (unless built with `--final`), none on pupil pages. A 68-character school name keeps the footer on one line with the page code (the name shrinks with an ellipsis).
- Reading level (V8, simplified): instruction and clue sentences at most 8 words, at most 3 instruction lines, check text at most 18 words (P1-20 has two checks: at most 34).
- Layout in the browser for all 20 pages (also front matter and key): no overflow, no text clipped, every element inside the 14.5 mm print-safe margin, puzzle content fills at least 55% of the puzzle area, text at least 8 pt, puzzle area never touches the check strip; every label of every colour-by-code part inside its own region, clear of outlines and decorations (pupil pages and key answer pages).
- Fonts embedded, A4, 20 / 5 / 25 / 11 pages, school-name footer and page code on every page, file sizes (all under 2 MB).
- Black and white (owner addendum 10): only `#000` and `#fff` in the HTML/CSS, no opacity, alpha or gradients, SVG strokes at least 0.2 mm and rule borders at least 0.25 mm (0.57 pt and 0.7 pt; the minimum asked is 0.5 pt), every PDF page (pupil pages, front matter, key) rendered at 150 dpi as 1-bit and compared with greyscale: bilevel keeps the ink (at most 25% loss on pupil pages, 30% on the text-only front matter, 35% on the key, which has small text) and no flat grey tint areas. The 1-bit pages for the pupil pack are written to `out/bilevel_check/` and were viewed.

Not covered by any script: the hand check of every page picture (done by viewing every changed page at 70 dpi, and clocks, rulers and the new icons at 150 dpi 1-bit), and any check of age-appropriate content beyond the word rules above.

## Syllabus items not covered by a puzzle

Reading and writing numbers in words, measuring and drawing a line to the nearest cm, am and pm, copying figures on a dot or square grid, forming figures from shapes, the number sentence signs on their own, ordinals beyond 5th, naming a shape from a description (the shape-riddle page was dropped for the new coverage pages). Add and subtract within 100 is P1-11 (no renaming), sharing and grouping is P1-03, multiplication is P1-05 and P1-13.

## Page rules used

Black and white only; A4, 15 mm margins (all content inside 14.5 mm); body text 15 pt, check text 14 pt, footer 8 pt; instruction sentences at most 8 words and at most 3 lines; numerals for quantities; answer boxes at least 12 mm high (checked); money written 50¢, times as o'clock and half past in text (5-minute times only on P1-18); all puzzles original (own generators, own number sets; no contest, book or past-paper problem used). No Mi, no alignment or affiliation wording on pupil pages. The licence page and teacher notes carry no endorsement claim; the key names the syllabus edition in plain words.

## Open questions for the owner

1. Product name: "Early Finisher Puzzles, Primary 1" is a working title. Final school-neutral name?
2. Publisher line, entity, year, licence wording, term of the licence (perpetual or annual) and a contact address: the cover, licence page and teacher notes now say DRAFT and show `[contact email or phone: to be added by the owner]`. The pupil-page footers still print "(c) 2026 Preciouslyours Pte Ltd" (owner to confirm entity and year); build with `--final` once approved and fill the contact placeholder in `render.py` (`CONTACT`).
3. Colour-by-code: 3 of 20 pages (P1-01, 12, 14). Pupils need crayons in five colours; a pencil-only copy can write Y, R, B, G, O in each part (stated in the notes). Owner to say whether 3 is right and whether crayons can be assumed in early-finisher trays. The library's label boxes inside the colour pictures are about 4 mm, too small to write a number in; the check does not depend on them.
4. Teacher key states the syllabus edition and page numbers (Primary 1, pages 31 and 32, 2021 edition) in plain text. Keep, or move to the product page? Outcome numbers are given as the ranges that `docs/moe/syllabus_by_level.md` supports; the individual numbers within 2.1 to 2.7 are not asserted.
5. A pupil trial (4 to 6 children) is still needed: especially the maze, the ruler on P1-17, the clocks on P1-06 and P1-18, and whether a pupil reads the letters on the logic pages and guesses.
6. Independent audit round 3 (plan section 11): hand-solve 20% of pages, mono photocopy test on a real copier, and the V9 non-copy comparison against `hp/qbank.json`, which is not run here.
7. Is 10 one-star and 10 two-star the right split? Strand spread: whole numbers 5, add/subtract 4, multiplication and sharing 3, money 2, time 2, shapes 2, length 1, graph 1. Is "1 star" labelling shown to pupils only as star symbols plus the teacher note?
8. Printed bulk option: the licence page now says "Printed sets: details to follow". Print route, loose-leaf layout and prices are not decided (prices are on hold).
