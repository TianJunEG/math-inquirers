# Rebuild report: Level 1 lessons 1-19 and 23-29 after the shared-tool fixes

Built one lesson at a time with `bash term/l1/build.sh NN`, then `python3 term/l1/tools/validate.py NN`. Lessons 20-22 and 30-40 were not touched.

## Result per lesson (validator, after the one tool fix below)
| Lesson | Build | Validator |
|---|---|---|
| 01-19 | ok | 0 FAIL (warnings only, 0 to 8 per lesson) |
| 23, 24, 26, 27, 28, 29 | ok | 0 FAIL |
| 25 | ok | FAIL on first build (see below), 0 FAIL after the fix |

## Regression found and fixed
- **L25 (price tags kit):** workbook had 7 pages, 6 designed. The kit page held only the heading and note (22 % full) and the 12 price tags spilled to a page of their own. Cause: the new 54 by 44 mm tags, 4 rows, 6 mm gaps made the drawing 209 mm tall; it did not fit the space left on the kit page. Fix in `term/l1/tools/figs3.py` (`price_tags`): the SVG height no longer includes the trailing gap after the last row (`34 + rows*(ch+gap) - gap + 2`). Tag size and 6 mm gaps are unchanged. After rebuild: 6 designed pages, 0 FAIL. L25 is the only lesson with a `price_tags` kit.

## What was looked at (rendered pages)
For each of 17 lessons I looked at workbook page 1, the tutor guide first page (and checked the timing line by text), kit page 1 where the lesson has one, and a deck slide with the footer: 1, 5, 9, 11, 12, 13, 16, 19, 23, 24, 25, 26, 27, 28, 29 (L25 workbook all 7 pages before the fix, kit page after).
- Clocks (11, 23, 24, 29): numerals clear of the hands, hands fit the face, centre dots visible.
- Money (24-26): coin kit at a readable size with gaps, notes, price tags in 3 by 4 grid; workbook money pictures are not clipped.
- Shape/grid/strip kits (27 tiles and mats, 28 strips, 13 ten-frames): all pieces whole on the page, mats not clipped.
- Guide timing line: every guide checked says "Nobody holds paper ... up to the camera"; no "30 s" camera wording remains.
- Deck slides: footer "Math Inquirers Term N ..." present, no overlap.
No overflowing page, broken figure or text overlap seen apart from L25.

## Books
`python3 print/make_term_books.py --level 1 --first 1 --last 20 --size 5 --per-term 10` ran for lessons 1-20 (L20's output already existed and validated 0 FAIL). B&W conversion and check: see final message. Outputs are git-ignored and not committed.
