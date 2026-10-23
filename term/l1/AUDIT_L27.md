# Self-audit: Level 1 Term 3 Lesson 7 (Fill the Grid)

Table from the final validator run (`python3 term/l1/tools/validate.py 27`, built files included); judgement lines written by the author after viewing every output. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present |
| Every answer verified independently (verify/lNN_checks.py) | PASS | verify: 188 answer checks by independent script passed (term/l1/verify/l27_checks.py) |
| Online practice variants verified (expression, oracle, runner JS) | PASS | practice: 18 template variants verified three ways (expression, brute-force oracle, runner JavaScript calc) |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | timing: 11 parts, contiguous, sum = 90 minutes exactly |
| Slides and script linked (each slide once, in its part) | PASS | link: 28 slides each shown exactly once, all question ids resolve |
| Tier counts and completeness (answer, hint, solution, mistakes) | PASS | tiers: counts, completeness (answer, hint, worked solution, mistakes), exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording: no banned labels or claims in child and parent text |
| Recording cues short, with child action | PASS | rec: 11 cues, each at most 26 words, each with an action line |
| Spare-time menu present | PASS | spare: 3 spare-time activities, 11 optional minutes (not in the 90 sum), rules present |
| No copied contest text | PASS | copy: no 7-word overlap with docs/sasmo analysis/solution notes or docs/books (originals only) |
| Mascot used modestly | PASS | mascot: Mi on 4 slides, short friendly lines only |
| Workbook page fill (model) | PASS with warning | pages: workbook page 3 content ends at 54% of the page (target at least 85%): add a question or bigger writing space |
| Real PDF page count and fill | PASS | outputs: Workbook PDF 6 pages, fill (measured on the PDF) 95%, 87%, 96%, 92%, 97%, 83% |
| No template leak (other lesson titles, Lesson 1 text) | PASS | template leak: no other lesson title or stray Lesson 1 text in the built files |

Timing: script 67.8 min of 90, slow-class 80.2 min. Workbook fill (measured on the PDF): 95%, 100%, 54%, 100%, 23%, 81%, 100%, 15%.

## Judgement lines (author)

- Tier principle: PASS. Start here (5 questions, about 15 modelled minutes) is approachable: the missing shape in a row (three rows), true or false for three rows, a 3 by 3 grid with the reason chosen from two options (not written), a grid read aloud in words checked by its columns, and a count of circles. Think harder (3): elimination in a 3 by 3 grid from two clues (the non-routine LOG item, brute-force unique), how many shapes could go in a box, and which swaps keep a correct grid correct (tested with the tiles). Go further (3) is beyond Primary 1 on purpose and named Four by Four: a 4 by 4 digit grid from nine clues, from six clues, and the counts in a 5 by 5 grid. Said plainly to families on the parent page, in the guide and in `moe.note`; never "MOE-aligned".
- Age-appropriateness: PASS. One idea (one of each in every row and column, so every box has a reason). Explore is 11 minutes with tiles before any written work, with a hint that only the top row is kept. Every question is read aloud, shapes are circle, square, triangle only (digits only at Go further), and Start here never asks for a written reason.
- Joining cold: PASS. The warm-up shows a missing shape in a row, a missing digit in 1 to 4 and a pair of rows to compare. `safe_to_miss` is true: no later lesson needs it, and the Quest gate on it is a Start here item.
- Safeguarding and privacy: PASS. Main room only, no paper to the camera, ticks against the answer slide, WhatsApp route only on the parent page, small-parts line for the tiles, nobody cuts in the lesson, seated option in the movement break. The wrong claim in Talk time is "a child".
- Pictures and pages: PASS with limits. Viewed every workbook page, the key, home sheet, parent page and all 28 slides. Fixes while viewing: single-column shape pictures printed as large as the page (column questions changed to rows; the column idea is taught in class and tested in S3 and T3), grid pictures too tall for a page (labels removed, boxes named by place, one question moved to words only), the sneak-peek and mini-lesson slides overflowed (grids set to size s, the chip removed, the column picture replaced by a list). Limit: the Mat 2 (4 by 4) picture on the kit page is cut off at the right edge by the template (its right column falls outside the 700-unit page), so the printed mat 2 shows 3 and a bit columns. Go further does not need the mat (the grids are in the book), but the kit page should be fixed in `figs3.grid_tiles` (see the report).

## Instrument A (0 to 2 each)

1 Low floor, high ceiling: 2 (one missing shape in a row; a 4 by 4 grid from six clues). 2 Depth over speed: 2 (Explore is 11 minutes with real tiles, find both grids with one top row). 3 Generalise: 2 (what stays correct when rows are swapped; how many of each digit a 5 by 5 grid holds). 4 Justify: 2 (sneak-peek "I know because", Talk time, S3 reason choice). 5 Multiple paths: 1 (row-first, column-first, crossing out). 6 Challenge ladder: 2. 7 Student-led inquiry: 1 (how many grids have the same top row). 8 Complexity / context: 1 (puzzle context only). 9 Problem posing: 2 (cover and find, the optional make-a-puzzle item, online g3). 10 Metacognition: 1 (look-back, check every row and column). 11 Pacing: 1. 12 Extension, not acceleration: 2.

Total: 19 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled.
- New topic with no Primary 1 school-paper evidence: all wording is unverified (decision D13); this is the lesson a tutor may swap or skip.
- Panel pictures cannot be shrunk in the workbook (a template limit): single grid pictures are about 45% of a page, so each page holds two grid questions at most. The workbook therefore uses grid pictures in S3 and T1 only and states other items in rows or in words.
- Online practice has no rewind items (the runner cannot assemble them yet). Online figures are static (the runner draws the grid picture without variants); the variants are the number items.
- Mat 2 on the kit page is clipped by the template (see above). The Term 3 Quest gate for this lesson (a 3 by 3 grid with five boxes filled) is not in this file; Lesson 30's author must use a grid that differs from every grid shown here.
