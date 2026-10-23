# Colour by Code: picture and topic generator (Primary 1: 14 sheets, Primary 2: 15 sheets; levels 3 to 6 plug in)

A worksheet is an outline picture cut into 12 to 18 regions. Each region holds one question for the level. The answers are
five key values and each value has a colour word (yellow, red, blue, green, orange). The page is printed black and white and
the pupil colours it with their own crayons. The picture and the topic are separate: any picture can take any topic bank of any level.

Page contents: title and stars (1 or 2, drawn like the school puzzle pilot), name and class lines, one instruction line, the key
(answer value over colour word), the picture, a "Check your work" box, and a footer with a school-name field, the worksheet code, the level and the topic.
Every worksheet has a pupil page and a teacher-answers page (answers filled in and underlined, colour in brackets).
No price, no brand or syllabus-alignment claims on any page; no Mi.

## Run

```
python3 build.py [--level 2] [--school "School name"] [--only CBC-P2-03]   # writes out/pN/*.pdf (pupil, teacher, contact_sheet) and out/pN/html/; no --level = every level
python3 verify.py [--level 2]                                              # exit code 1 on any failure; writes out/pN/verification.txt, .json and inventory.md
python3 compat.py [--level 2]                                              # which picture x topic x tier combinations build (Markdown table)
python3 preview.py fish owl                                                # debug picture: outlines and the label boxes found for each region (red)
```

Needs: python3 with `shapely`, `fonttools` and `brotli`, `playwright` (chromium), `pillow`, `numpy`, `scipy`; poppler (`pdftoppm`, `pdftotext`, `pdfinfo`, `pdffonts`);
the repo fonts folder (`fonts/node_modules/@fontsource`: Fredoka 600 and 700, Nunito Sans). Without `--school` the footer prints a blank "School name: ____" line to fill in.
Outputs: `out/p1/` (Primary 1, fourteen sheets) and `out/p2/` (Primary 2, fifteen sheets), each with `contact_sheet.pdf`, `verification.txt/.json`, `inventory.md`, `compat.md`.

## Files

| file | what it does |
|---|---|
| `textcheck.py` | the independent evaluator: re-solves every printed question from its text (and, for picture questions, from what a reader decodes from the picture: clock hands, ruler ends, coins, dots, graph rows, tally, solids, fraction parts). Does not import a bank. A new question form needs a new rule here or `verify.py` fails |
| `qcore.py` | the question core for every level: `Q`, `EQ`, `SEM`, `Tier`, `Bank`, `T()`; the equation re-evaluator (plain, money in $ and ¢, x and the division sign) |
| `banks.py` | the level registry: finds every `banks_pN.py` in this folder, exposes `banks(level)`, `gallery(level)`, `rules(level)` |
| `banks_p1.py`, `banks_p2.py` | one file per level: `LEVEL`, `RULES`, `BANKS` (topic banks) and `GALLERY` (the worksheets of that level) |
| `geom.py` | shapely helpers (circle, ellipse, polygon, mirror, smooth blob) on a 180 x 200 mm canvas |
| `pictures.py` | the picture library (`@picture` functions return regions); shared by all levels |
| `labelbox.py` | finds the largest label rectangles inside a region, kept 1 mm from the outline and clear of decorations (cached in `cache/`, not committed) |
| `art.py` | small pictures inside regions: clock, coins, notes, cash, ruler, flat shapes, solids, fraction bars and circles, equal groups, dot arrays, balance, picture graph, tally, base-ten blocks, shape row, pattern row |
| `metrics.py` | conservative text widths from the real font files (kerning ignored, +4 %) |
| `layout.py` | fits a label (text lines and optional art) into a region's boxes, largest font first (4.9 mm down to 4.2 mm for pupils) |
| `sheet.py` | assigns answers to regions, picks a fitting question for each, writes the HTML page |
| `worksheets.py` | gathers the galleries of all levels (older callers) |
| `build.py`, `verify.py`, `compat.py`, `preview.py` | tools (see Run) |
| `out/` | PDFs, contact sheets, verification and inventory per level; `out/pN/html/` is regenerated and not committed |

## Levels: how to add Primary 3 to 6 by writing only a bank file

Create `banks_p3.py` (then `banks_p4.py` and so on) next to `banks_p2.py`. Nothing else in the library is edited: `banks.py` finds the file, `build.py`, `verify.py` and `compat.py` loop over every level, and output goes to `out/p3/`.

```python
from qcore import *          # Q, EQ, SEM, Tier, Bank, T, BOX, MINUS, TIMES, DIVIDE, mark
import art as A               # ready-made small pictures (or build an Art yourself, see below)
LEVEL = 3
RULES = dict(allow_division_sign=True, time_words_only=False)       # wording rules the verifier applies to this level's pages
def _tables(tier): ...        # returns the list of question forms: form(answer, rng) -> Q or None
BANKS = {"mult": Bank("mult", "Multiplication", "Multiplication: tables of 6, 7, 8 and 9",
            "Multiply. Find the answer in the key. Colour the part with that colour.",
            {1: T([24, 28, 32, 36, 42], range(0, 1001), _tables(1)), 2: T([...], range(...), _tables(2), disp=str)})}
GALLERY = [dict(id="CBC-P3-01", picture="castle", bank="mult", tier=1, seed=401), ...]     # 10 to 12 sheets, mixed stars, at least 5 pictures and 6 topics
```

Rules for a bank (checked by `verify.py`): per tier five distinct key values that are all inside the `domain` (every value a pupil could write; any hashable value works: ints, `(h, m)` times, `(a, b)` fractions, `(n, "kg")` measures); a form returns `None` when the wanted answer cannot be made in that form; `Q.holds(v)` is true for the intended answer and for no other domain value (the verifier tries every domain value on every sample question); equations built with `EQ` are re-evaluated from their printed text (set `money=True` for `$1.20` and `65¢`); each form may set `q.extra = lambda answer: bool` to check the picture or text independently of the generator (decode a clock, a graph, a balance); give each answer at least two compact forms (one or two short lines) or small regions will not fit; one-star and two-star tiers differ by key values and forms, never by a different template. `GALLERY` entries need `id`, `picture`, `bank`, `tier`, `seed`; `python3 compat.py --level 3` shows which pictures take which bank, and a gallery sheet must have no repeated question (`dups` is 0; try another seed).

A level only needs more than a bank file when its topics need a picture that `art.py` does not have (for example a bar graph, an angle or a net at P3 and P4). Then add a function to `art.py` (or build the `Art` inside the bank file): `Art(svg, w, h, min_scale, meta)` with local mm coordinates, text in `style="font-size:..px"`, strokes at least 0.3 mm, black and white only, no taller than 11 mm if it must fit the smallest labels, and put what a reader would decode in `meta` so that the bank's `q.extra` can check it. No change to `sheet.py`, `layout.py`, `build.py` or `verify.py` is needed.

## Verification (what `verify.py` checks, every level)

* Banks (every bank of the level, both tiers, hundreds of sample questions; pictures and text are decoded by `q.extra` where a bank sets it: clock hands, ruler, coins and notes, fraction parts, dots, balance, graph rows, tally, solids): each question has exactly one answer in the bank's domain and it is the intended one; printed equations are re-evaluated from their printed text; clock hands are decoded from the drawn angles, coin and note values, ruler start and end, and shape counts are re-added.
* Pictures: 12 to 18 regions, valid polygons, no overlaps, exact mirror pairs, and a label box at least 28 mm wide by 12 mm high fits every region.
* Worksheets: every question has one answer and it is a key value; all five colours used at least twice; the tally printed on the page equals the tally of the answers (read back from the PDF text); mirror pairs and same-colour groups hold; the counted-subset check ("exactly N red scales") is true and printed correctly.
* Single-slip detection: every wrong answer in the bank's domain is tried in every region, one at a time, and the page's own checks must catch at least 95 percent (fails below). A wrong answer with no crayon colour is caught by the key; a wrong answer with a colour is caught by the tally (always) and often by the mirror, group or subset check as well (the `caught_by_structure_checks` figure in `verification.json`, 37 to 100 percent, shows how much the second checks add without the tally).
* Text fit: label sizes come from conservative font metrics; then the real browser measures the bounding box of every label and tests a grid of points against the region's fill and outline and against the decorations (eye, door knob, mast).
* Legibility: 1-bit render at 150 dpi (ink loss at most 25 percent per page, at most 40 percent per label), no flat grey tints, every region stays a separate white area in the 1-bit image.
* Pages: one A4 page, fonts embedded, outline 0.9 mm, only black and white, margins and no overflow, footer school-name field, wording rules (cents written 50¢ not 50c, o'clock and half past only, no division sign, no price or alignment wording).

## Add a picture

Open `pictures.py`, copy one of the small functions (`rocket` is the simplest symmetric one, `fish` the simplest non-symmetric one):

```python
@picture
def kite():
    b = Builder("kite", "Kite", symmetric=True, blurb="...")
    b.pair("wing", P((90, 10), (20, 80), (90, 80)))      # left region; the right one is its mirror image and must be the same colour
    b.add("tail_bow", C(90, 150, 20))                   # a single region
    b.decor('<circle cx="40" cy="40" r="3" fill="#000"/>', C(40, 40, 3))   # fixed black detail (labels keep clear of it)
    b.group(["a", "b"], "the two ...")                  # regions that must share a colour (text printed in the check box)
    b.subset(ids, "The fish has {n} scales. Exactly {c} of them {are} {colour}.")   # counted check printed on the page
    return b.done()
```

Rules: canvas 180 x 200 mm; regions must tile without overlapping (use `-` to cut one shape out of another); every region needs a 28 mm wide, 12 mm high clear rectangle; keep 12 to 18 regions. Run `python3 preview.py kite` (red boxes show where labels will sit; fix any region that is too small), then `python3 compat.py`.
A symmetric picture gets the mirror check automatically; a non-symmetric picture should have a `subset` check (the "exactly N red scales" kind) and as many `group`s as the drawing naturally has. Add the picture to a worksheet in `worksheets.py`, run `build.py` and `verify.py`.

## Primary 3 to 6: topic plan from `docs/moe/syllabus_by_level.md` (to be written as bank files when the school paper-pattern files land)

The Primary 2 banks used `docs/books/p2_school_paper_patterns.md` for wording and ranges. `docs/books/p4_school_paper_patterns.md` exists; the Primary 3, 5 and 6 pattern files had not landed when this was written. Plan (bank id: topic, tiers by the usual one-star and two-star split):

| level | bank files to write (syllabus pages) | new art probably needed |
|---|---|---|
| P3 (pp. 35 to 36) | numbers to 10 000 (place value, compare, patterns); add and subtract to 4 digits; tables of 6, 7, 8, 9 and mixed tables; division with remainder; multiply and divide 3 digits by 1 digit; equivalent fractions, simplest form, compare unlike fractions, add and subtract related fractions; money add and subtract in decimal notation; km, ml, compound units; time in seconds, start, finish and duration, 24-hour clock; area and perimeter of rectangles and squares; angles (right angle, bigger or smaller), perpendicular and parallel lines; bar graphs | bar graph, angle, grid with a shape, 24-hour clock |
| P4 (pp. 37 to 40) | numbers to 100 000, rounding; factors and multiples; four operations (4 digits x 1 digit, 3 digits x 2 digits, division 4 digits); mixed numbers and improper fractions, fraction of a set, add and subtract with up to two denominators; decimals to 3 places, add and subtract, multiply and divide by 1 digit; area and perimeter of composite figures, missing side; angles in degrees, rectangle and square properties, line symmetry, nets; table, line graph, pie chart | protractor angle, symmetry grid, net, pie chart, line graph |
| P5 (pp. 41 to 42) | whole numbers x and divide by 10, 100, 1000; order of operations; fractions (mixed number add and subtract, fraction x fraction, fraction of a quantity); decimals x and divide by 10, 100, 1000 and unit conversion; percentage (part, discount, GST, interest); rate; area of triangle, composite figures; volume of cube and cuboid, litre and cm3; angles on a line, at a point, vertically opposite; triangle and quadrilateral properties | triangle with sides, cuboid with dimensions, angle diagram |
| P6 (pp. 43 to 44) | divide a fraction by a whole number and by a fraction; percentage (whole from part, increase and decrease); ratio (a:b, a:b:c, equivalent, divide a quantity); algebra (letters, simplify, substitute, simple equations); area and circumference of a circle, semicircle, quarter circle, composite; volume with a missing dimension; unknown angles in composite figures; average | circle and sector, ratio bar, composite figure |

Practical notes for these levels: the key display for fractions, ratios and percentages is a string from `disp`; keep domains finite (fractions as `(numerator, denominator)`, ratios as `(a, b)`); numbers wider than about 12 characters need two-line forms; the verifier's wording rules per level come from `RULES` (add a pattern there if a level needs a new rule). The division sign is allowed from level 2.

## Primary 2 gallery (verified)

| id | picture | topic | stars | key (answers, in colour order yellow, red, blue, green, orange) | regions | checks printed on the page | single-slip detection | min text | verification |
|---|---|---|---|---|---|---|---|---|---|
| CBC-P2-01 | Rocket | Numbers to 1000: place value, order | 1 | 120, 250, 340, 470, 560 | 15 | tally, mirror pairs | 15000/15000 = 100.0% | 4.4 mm | PASS |
| CBC-P2-02 | Car | Addition within 1000, with renaming | 2 | 412, 536, 653, 724, 841 | 13 | tally, same-colour groups, car has 5 body and window parts count | 13000/13000 = 100.0% | 4.9 mm | PASS |
| CBC-P2-03 | Elephant | Subtraction within 1000, with renaming | 2 | 158, 247, 364, 475, 586 | 14 | tally, mirror pairs | 14000/14000 = 100.0% | 4.9 mm | PASS |
| CBC-P2-04 | House | Multiplication: tables of 2, 3, 4, 5 and 10 | 1 | 6, 12, 15, 20, 30 | 17 | tally, same-colour groups, house has 6 wall and window parts count | 1700/1700 = 100.0% | 4.9 mm | PASS |
| CBC-P2-05 | Castle | Division: sharing and grouping | 1 | 2, 3, 4, 5, 6 | 17 | tally, mirror pairs | 1700/1700 = 100.0% | 4.9 mm | PASS |
| CBC-P2-06 | Owl | Fractions: compare, add and subtract like fractions | 1 | 1/2, 1/3, 1/4, 2/3, 3/4 | 14 | tally, mirror pairs | 910/910 = 100.0% | 4.4 mm | PASS |
| CBC-P2-07 | Dinosaur | Money: cents, dollars and change | 2 | 35¢, 65¢, 135¢, 185¢, 250¢ | 15 | tally, same-colour groups, dinosaur's body has 4 parts count | 30000/30000 = 100.0% | 4.7 mm | PASS |
| CBC-P2-08 | Fish | Time to the minute | 1 | 2:10, 4:25, 6:45, 8:35, 10:50 | 16 | tally, same-colour groups, fish has 6 scales count | 11504/11504 = 100.0% | 4.2 mm | PASS |
| CBC-P2-09 | Sailboat | Length, mass and volume: cm, m, g, kg and l | 1 | 5 cm, 9 cm, 4 kg, 8 kg, 6 l | 13 | tally, same-colour groups, boat has 4 sails count | 65052/65052 = 100.0% | 4.9 mm | PASS |
| CBC-P2-10 | Car | Picture graphs and tally marks | 2 | 12, 15, 20, 30, 40 | 13 | tally, same-colour groups, car has 5 body and window parts count | 1300/1300 = 100.0% | 4.9 mm | PASS |
| CBC-P2-11 | Butterfly | 2D and 3D shapes and shape patterns | 1 | 1, 2, 3, 4, 6 | 14 | tally, mirror pairs | 280/280 = 100.0% | 4.7 mm | PASS |
| CBC-P2-12 | Ice Cream | Odd and even numbers | 2 | 200, 301, 402, 503, 604 | 12 | tally, mirror pairs | 12000/12000 = 100.0% | 4.5 mm | PASS |

Primary 2 sheets: castle, car, elephant and dinosaur are new pictures; the seven Primary 1 pictures are used too (rocket, house, owl, sailboat, fish, butterfly, ice cream). Two-star sheets use larger ranges or two-step items (3-digit sums with renaming, three addends, "reversal" stories, tables to 45, $ and cents conversions, minutes in a duration, tally and keys of 3, 4, 5 and 10).
Contact sheet: `out/p2/contact_sheet.pdf` (page 1 pupil pages, page 2 teacher pages). Verification report: `out/p2/verification.txt` (572 checks, 0 failures) and `out/p2/verification.json`.

## Primary 1 gallery (verified)

| id | picture | topic | stars | key (answers, in colour order yellow, red, blue, green, orange) | regions | checks printed on the page | single-slip detection | min text | verification |
|---|---|---|---|---|---|---|---|---|---|
| CBC-01 | Rocket | Number bonds to 10 | 1 | 1, 2, 3, 4, 5 | 15 | tally, mirror pairs | 150/150 = 100.0% | 4.9 mm | PASS |
| CBC-02 | Fish | Addition within 20 | 2 | 13, 14, 15, 16, 17 | 16 | tally, same-colour groups, fish has 6 scales count | 320/320 = 100.0% | 4.9 mm | PASS |
| CBC-03 | Butterfly | Subtraction within 20 | 2 | 7, 8, 9, 10, 11 | 14 | tally, mirror pairs | 280/280 = 100.0% | 4.9 mm | PASS |
| CBC-04 | House | Place value: tens and ones | 1 | 1, 2, 3, 4, 5 | 17 | tally, same-colour groups, house has 6 wall and window parts count | 170/170 = 100.0% | 4.9 mm | PASS |
| CBC-05 | Ice Cream | Counting in 2s, 5s and 10s | 2 | 60, 65, 70, 75, 80 | 12 | tally, mirror pairs | 1200/1200 = 100.0% | 4.9 mm | PASS |
| CBC-06 | Owl | Comparing and ordering numbers to 100 | 2 | 55, 60, 65, 70, 75 | 14 | tally, mirror pairs | 1400/1400 = 100.0% | 4.9 mm | PASS |
| CBC-07 | Sailboat | Money: coins and notes, ¢ and $ | 1 | 10¢, 20¢, 30¢, 40¢, 50¢ | 13 | tally, same-colour groups, boat has 4 sails count | 260/260 = 100.0% | 4.7 mm | PASS |
| CBC-08 | Fish | Time: o'clock and half past | 1 | 2 o'clock, 4 o'clock, 6 o'clock, half past 3, half past 7 | 16 | tally, same-colour groups, fish has 6 scales count | 368/368 = 100.0% | 4.4 mm | PASS |
| CBC-09 | Ice Cream | Length in centimetres | 1 | 2 cm, 3 cm, 4 cm, 5 cm, 6 cm | 12 | tally, mirror pairs | 240/240 = 100.0% | 4.8 mm | PASS |
| CBC-10 | House | Shapes: corners and straight sides | 1 | 3, 4, 6, 7, 8 | 17 | tally, same-colour groups, house has 6 wall and window parts count | 204/204 = 100.0% | 4.9 mm | PASS |

Reading the table: "single-slip detection" counts every wrong value in the bank's domain, tried in every region; the page's checks catch every one (tally), and the same figure is also required to hold for the wrong values that do have a crayon colour. Two-star sheets use larger numbers or two-step items (three-number sums, "subtract then add", counting back, middle number, dollars with notes, a clock plus a time after).
The contact sheet is `out/contact_sheet.pdf` (page 1 pupil pages, page 2 teacher pages).

## Picture library

| id | regions | matching rules |
|---|---|---|
| rocket | 15 | 5 mirror pairs |
| fish | 16 | tail parts match, two fins match, counted check on the 6 scales |
| house | 17 | roof sides match, two windows match, tree-top halves match, counted check on the 6 wall and window parts |
| butterfly | 14 | 7 mirror pairs |
| icecream | 12 | 5 mirror pairs |
| owl | 14 | 5 mirror pairs |
| sailboat | 13 | three hull parts match, counted check on the 4 sails |
| castle | 17 | 7 mirror pairs (clouds, tower roofs and walls, keep, doors) |
| car | 13 | two wheels match, counted check on the 5 body and window parts |
| elephant | 14 | 6 mirror pairs (ears, head parts, clouds, ground) |
| dinosaur | 15 | two legs match, two neck parts match, counted check on the 4 body parts |

## Topic banks (Primary 2; key values per tier)

| bank | 1 star key | 2 star key | forms (layouts) |
|---|---|---|---|
| numbers | 120, 250, 340, 470, 560 | 105, 218, 346, 407, 639 | hundreds-tens-ones expanded, words to number, 1, 10 or 100 more or less, greatest, smallest, between, count on, base-ten blocks; 2 star: regrouped (3 hundreds 11 tens), middle number |
| pattern | 210, 300, 350, 420, 500 | 135, 248, 376, 480, 615 | missing number in a pattern of 2s, 3s, 4s, 5s, 10s, 100s forwards or back, with or without the rule, start and count on; 2 star: which number does not belong (not in the gallery) |
| oddeven | 9, 12, 15, 18, 21 | 200, 301, 402, 503, 604 | odd or even number just after, just before, smallest greater, greatest less, which is odd or even, between, short pattern |
| add | 135, 252, 341, 428, 563 | 412, 536, 653, 724, 841 | sum, reversed, missing addend, "add to", "the sum of", "more than", sold then sold, at first; 2 star: three addends |
| sub | 125, 237, 346, 458, 569 | 158, 247, 364, 475, 586 | difference, missing number, "subtract from", "difference between", "fewer than", story, reversal ("46 more than Jane"); 2 star: two steps |
| mult | 6, 12, 15, 20, 30 | 24, 28, 35, 40, 45 | times, groups of, repeated addition, "multiply by", dot array, boxes of dots, bags; 2 star: times plus, times as many |
| div | 2 to 6 | 6 to 10 | divide, share equally, boxes needed, divide into groups, missing factor, sharer counted ("with her 3 friends"), related facts; 2 star: most friends |
| frac | 1/2, 1/3, 1/4, 2/3, 3/4 | 1/6, 3/8, 5/8, 7/10, 5/12 | shaded bar or circle, not shaded, "n of m equal parts", make 1 whole, add and subtract like fractions, compare unit fractions, compare like fractions (written 1/2) |
| money | $1.20, $2.35, $3.05, $4.50, $6.80 | 35¢, 65¢, 135¢, 185¢, 250¢ | notes and coins pictured, add amounts, change from $5 to $50, two items, more than, cents to dollars, greatest and smallest of three amounts; 2 star: dollars to cents, make $1 |
| time | 2:10, 4:25, 6:45, 8:35, 10:50 | 45, 75, 90, 105, 135 minutes | clock face (hands decoded), minutes past and to, minutes later and before, hours later; 2 star: hours and minutes to minutes, from a time to a time, a film, am times |
| measure | 5 cm, 9 cm, 4 kg, 8 kg, 6 l | 35 cm, 60 cm, 250 g, 450 g, 12 l | ruler strip, cut off, add, balance with identical objects, kg together, lighter than, litres left, 1 m or 1 kg minus a part |
| graph | 6, 8, 10, 15, 20 | 12, 15, 20, 30, 40 | picture graph with key 2, 3, 4, 5 or 10 (read a row, how many more, total, one row), tally marks |
| shape | 1, 2, 3, 4, 6 | 5, 7, 8, 9, 12 | flat and curved surfaces of solids (pictured and in words), count a shape in a row, straight sides, pattern count in 8 to 12 shapes; 2 star: surfaces of two or three solids, straight sides in all |

## Topic banks (Primary 1; key values per tier)

| bank | 1 star key | 2 star key | forms (layouts) |
|---|---|---|---|
| add | 8, 9, 10, 11, 12 | 13, 14, 15, 16, 17 | sum, reversed, missing addend, "more than", "make"; 2 star: three numbers, two-step, one of three missing |
| sub | 2 to 6 | 7 to 11 | difference, missing number, "fewer than", "take away"; 2 star: two-step, subtract then add |
| bonds | 1 to 5 (to 10) | 5 to 9 (to 20) | six forms of the bond equation |
| place | 1 to 5 | 5 to 9 | tens and ones in a number, expanded forms; 2 star: 10 more or less then tens digit |
| count | 10, 15, 20, 25, 30 | 60, 65, 70, 75, 80 | missing number in a 2s, 5s or 10s pattern, forwards and back, with or without the rule; 2 star: start and count on |
| compare | 20, 30, 40, 50, 60 | 55, 60, 65, 70, 75 | greatest, smallest, 1 more or less, 10 more or less, between; 2 star: middle number, two-step |
| money | 10¢ to 50¢ | $12, $14, $16, $18, $20 | coins or notes pictured, sums, missing amount, change, "more than", "fewer than" |
| time | 2, 4, 6 o'clock; half past 3, 7 | half past 8, 9 o'clock, half past 10, 11 o'clock, half past 12 | clock face (hands decoded and verified), written time, 1 hour or half an hour later or before |
| length | 2 to 6 cm | 7 to 11 cm | strip on a ruler (from 0 or from another mark), sums and differences in cm, "longer", "shorter", cut off |
| shapes | 3, 4, 6, 7, 8 corners | 6, 8, 12, 14, 16 (corners plus straight sides) | triangle, square, rectangle and circle pictured, one or two shapes |

## Which pictures take which topics

Number is the smallest text size used (mm); `-` means some region is too small for any question of that bank. Full tables: `out/p1/compat.md` and `out/p2/compat.md` (regenerate with `python3 compat.py --level N`).
Primary 1: 207 of 220 picture, topic and tier combinations build.
Primary 2: 267 of 286 picture, topic and tier combinations build.
Primary 2 gaps: clock questions need a region about 18 mm high, picture graphs with several rows need about 22 mm, so the smaller pictures (rocket, elephant, castle) take graph and 2D/3D shape banks only through their one-row and word forms; shape two stars builds on house, ice cream and dinosaur only. Use `compat.py` before putting a pair in a gallery.

## Decisions and notes

* Shapes use triangle, square, rectangle and circle only, so corners and straight sides are the same count and need no convention for half and quarter circles. Two stars adds corners and sides together.
* Time shows an hour-hand position halfway between numbers for half past, and uses only "o'clock" and "half past" in words. A written time such as 7:30 appears in some questions ("Which time is 7:30?") as digits only.
* Money at one star is cents (10¢ to 50¢), at two stars dollars to $20 with notes drawn as small rectangles; the minuend can go up to $28 in "dollars left" questions.
* Teacher pages use the pupil font size where they fit and shrink to 3.4 mm at the smallest; where a region is too small for the question plus the answer, the teacher label shows only the answer and the colour (`teacher_short_labels` in `verification.json`).
* Questions in the same worksheet are never repeated (checked); the generator falls back to a repeat only when a region is too small for any other form (does not happen in the gallery).
* Pictures are printed with 0.9 mm outlines; decorations (eye, door knob, mast, flag, antennae) are solid black or a plain line and are not coloured.

* Primary 2 picture graphs and tally are used (the papers show keys 2 to 10 and tally; no bar graph appears in the Primary 2 papers, bar graphs start at Primary 3 in the syllabus).
* Primary 2 time answers at one star are clock readings to 5 minutes; the two-star key is a duration in minutes. Minute-by-minute clock faces (3:07) are not drawn because the small face cannot show single minutes clearly.
* Primary 2 money: one star writes answers as $1.20 and two stars as cents (35¢); amounts under a dollar appear as 55¢ or $0.55; notes and coins are plain labelled shapes, not copies of real notes.
* Primary 2 fractions are written 1/2 with a slash (allowed at Primary 2); answers are compared as written (2/4 is not 1/2). Unit fractions up to twelfths appear at two stars.
* The Primary 1 teacher pages no longer print a doubled unit (a fix in the money bank: 40¢ not 40¢¢).
