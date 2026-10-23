# Colour by Code: picture and topic generator (Primary 1)

A worksheet is an outline picture cut into 12 to 18 regions. Each region holds one Primary 1 question. The answers are
five key values and each value has a colour word (yellow, red, blue, green, orange). The page is printed black and white and
the pupil colours it with their own crayons. The picture and the topic are separate: any picture can take any topic bank.

Page contents: title and stars (1 or 2, drawn like the school puzzle pilot), name and class lines, one instruction line, the key
(answer value over colour word), the picture, a "Check your work" box, and a footer with a school-name field and the worksheet code.
Every worksheet has a pupil page and a teacher-answers page (answers filled in and underlined, colour in brackets).
No price, no brand or syllabus-alignment claims on any page.

## Run

```
python3 build.py [--school "School name"] [--only CBC-03]   # writes out/*.pdf (pupil, teacher, contact_sheet) and out/html/
python3 verify.py                                           # exit code 1 on any failure; writes out/verification.txt, .json and inventory.md
python3 compat.py                                           # which picture x topic x tier combinations build
python3 preview.py fish owl                                 # debug picture: outlines and the label boxes found for each region (red)
```

Needs: python3 with `shapely`, `fonttools` and `brotli`, `playwright` (chromium), `pillow`, `numpy`, `scipy`; poppler (`pdftoppm`, `pdftotext`, `pdfinfo`, `pdffonts`);
the repo fonts folder (`fonts/node_modules/@fontsource`: Fredoka 600 and 700, Nunito Sans). Without `--school` the footer prints a blank "School name: ____" line to fill in.

## Files

| file | what it does |
|---|---|
| `geom.py` | shapely helpers (circle, ellipse, polygon, mirror, smooth blob) on a 180 x 200 mm canvas |
| `pictures.py` | the picture library (`@picture` functions return regions) |
| `labelbox.py` | finds the largest label rectangles inside a region, kept 1 mm from the outline and clear of decorations (cached in `cache/`, not committed) |
| `banks.py` | topic banks: key values, domain, question forms; question objects know their own answer test |
| `art.py` | small pictures inside regions: clock, coins, notes, ruler with strip, shapes |
| `metrics.py` | conservative text widths from the real font files (kerning ignored, +4 %) |
| `layout.py` | fits a label (text lines and optional art) into a region's boxes, largest font first (4.9 mm down to 4.2 mm for pupils) |
| `sheet.py` | assigns answers to regions, picks a fitting question for each, writes the HTML page |
| `worksheets.py` | the gallery: id, picture, bank, tier, seed |
| `build.py`, `verify.py`, `compat.py`, `preview.py` | tools (see Run) |
| `out/` | PDFs, contact sheet, verification and inventory (about 6 MB); `out/html/` is regenerated and not committed |

## Verification (what `verify.py` checks)

* Banks (every bank, both tiers, hundreds of sample questions): each question has exactly one answer in the bank's domain and it is the intended one; printed equations are re-evaluated from their printed text; clock hands are decoded from the drawn angles, coin and note values, ruler start and end, and shape counts are re-added.
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

## Add a topic

In `banks.py` write question forms `form(answer, rng) -> Q or None` (return `None` when the answer cannot be made in this form). Use `EQ([...lines with BOX...], answer)` for equations (checked by evaluating the printed text) or `SEM(lines, holds, answer_text)` where `holds(v)` is true only for the answer. Give a form several layouts (one line, two lines, art above or beside the text) and several wordings so regions of different size can take it; at least two compact forms are needed or small regions will not fit. Register it in `build_banks()` with, per tier: five key values, the domain of values a pupil could write, the list of forms, and the key display (for example `lambda v: f"{v}¢"`). Use P1 wording from `docs/books/p1_school_paper_patterns.md` (50¢ not 50c, o'clock and half past only, "more than", "fewer than"). `verify.py` then tests the bank itself.

## Gallery (verified)

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

Number is the smallest text size used (mm); `-` means some region is too small for any question of that bank. 135 of 140 combinations build; the ones that do not are rocket x time 1 star, owl x time 1 star, owl x shapes 2 star, sailboat x shapes 1 and 2 star.
Regenerate with `python3 compat.py`.

| picture | add 1★ | add 2★ | sub 1★ | sub 2★ | bonds 1★ | bonds 2★ | place 1★ | place 2★ | count 1★ | count 2★ | compare 1★ | compare 2★ | money 1★ | money 2★ | time 1★ | time 2★ | length 1★ | length 2★ | shapes 1★ | shapes 2★ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rocket | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.8 | 4.8 | 4.9 | 4.7 | 4.7 | - | 4.5 | 4.8 | 4.9 | 4.3 | 4.2 |
| fish | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.8 | 4.7 | 4.9 | 4.3 | 4.3 | 4.9 | 4.9 | 4.2 | 4.2 |
| house | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.7 | 4.8 | 4.7 | 4.3 | 4.9 | 4.9 | 4.8 | 4.4 |
| butterfly | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.8 | 4.8 | 4.9 | 4.9 | 4.7 | 4.8 | 4.9 | 4.2 | 4.4 |
| icecream | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.3 | 4.4 | 4.9 | 4.8 | 4.3 | 4.7 |
| owl | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.8 | 4.8 | - | 4.4 | 4.8 | 4.8 | 4.3 | - |
| sailboat | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.9 | 4.6 | 4.2 | 4.9 | 4.9 | - | - |

135 of 140 picture, topic and tier combinations build.


## Decisions and notes

* Shapes use triangle, square, rectangle and circle only, so corners and straight sides are the same count and need no convention for half and quarter circles. Two stars adds corners and sides together.
* Time shows an hour-hand position halfway between numbers for half past, and uses only "o'clock" and "half past" in words. A written time such as 7:30 appears in some questions ("Which time is 7:30?") as digits only.
* Money at one star is cents (10¢ to 50¢), at two stars dollars to $20 with notes drawn as small rectangles; the minuend can go up to $28 in "dollars left" questions.
* Teacher pages use the pupil font size where they fit and shrink to 3.4 mm at the smallest; where a region is too small for the question plus the answer, the teacher label shows only the answer and the colour (`teacher_short_labels` in `verification.json`).
* Questions in the same worksheet are never repeated (checked); the generator falls back to a repeat only when a region is too small for any other form (does not happen in the gallery).
* Pictures are printed with 0.9 mm outlines; decorations (eye, door knob, mast, flag, antennae) are solid black or a plain line and are not coloured.
