# Self-audit: Level 1 Term 3 Lesson 8 (Make a Table)

Table from the final validator run (`python3 term/l1/tools/validate.py 28`, built files included); judgement lines written by the author after viewing every output. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present |
| Every answer verified independently (verify/lNN_checks.py) | PASS | verify: 115 answer checks by independent script passed (term/l1/verify/l28_checks.py) |
| Online practice variants verified (expression, oracle, runner JS) | PASS | practice: 63 template variants verified three ways (expression, brute-force oracle, runner JavaScript calc) |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS with warning | timing: opening uses only 1:22 of 2:00 |
| Slides and script linked (each slide once, in its part) | PASS | link: 29 slides each shown exactly once, all question ids resolve |
| Tier counts and completeness (answer, hint, solution, mistakes) | PASS | tiers: counts, completeness (answer, hint, worked solution, mistakes), exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording: no banned labels or claims in child and parent text |
| Recording cues short, with child action | PASS | rec: 11 cues, each at most 26 words, each with an action line |
| Spare-time menu present | PASS | spare: 3 spare-time activities, 11 optional minutes (not in the 90 sum), rules present |
| No copied contest text | PASS | copy: no 7-word overlap with docs/sasmo analysis/solution notes or docs/books (originals only) |
| Mascot used modestly | PASS | mascot: Mi on 4 slides, short friendly lines only |
| Workbook page fill (model) | PASS with warning | pages: workbook page 4 content ends at 78% of the page (target at least 85%): add a question or bigger writing space |
| Real PDF page count and fill | PASS with warning | outputs: Workbook page 6 is 51% full (target at least 85%) |
| No template leak (other lesson titles, Lesson 1 text) | PASS | template leak: no other lesson title or stray Lesson 1 text in the built files |

Timing: script 66.6 min of 90, slow-class 78.9 min. Workbook fill (measured on the PDF): 82%, 84%, 81%, 78%, 97%.

## Judgement lines (author)

- Tier principle: PASS. Start here (5 questions, about 17 modelled minutes): count the sticks in 1, 2 and 3 squares, a two-row table of equal groups (3 red beads for every 2 blue), continue the squares table, a day-by-day table of pages read, and true or false from the table. The ratio table and the day table are Primary 1 school-paper patterns (23 Oct paper study). Think harder (3): the 10th and 20th triangle picture from a table with the rule double and add 1 in words, why no row of triangles uses an even number of sticks, and a table with one wrong number. Go further (3) is beyond Primary 1 on purpose and named Picture 100: the 100th picture and the 50th, working back from a total of sticks, and the squares against the triangles. Said plainly to families in the parent page, guide and `moe.note`.
- Age-appropriateness: PASS. One idea (a table shows how it grows, then we go on). Explore is 11 minutes with strips before any writing; guess before building; letters for a rule are never used (words only); every question is read aloud.
- Joining cold: PASS. The warm-up counts in 2s, doubles two numbers and fills a missing number in a small table. `safe_to_miss` is false: the Quest has a gate on it.
- Safeguarding and privacy: PASS. Main room only, no paper to the camera, ticks against the answer slide, WhatsApp route only on the parent page, paper strips (never matches or toothpicks), nobody cuts in the lesson, seated option in the hop break. The wrong claim in Talk time is "a child".
- Pictures and pages: PASS. Viewed every workbook page, key, home sheet, parent page and the slides. Fixes while viewing: the parent page ran onto a second page (text shortened), Start here and Think pages under 85% (sub-parts added), slide tables enlarged, the stick picture put beside the list on the Explore slide. The stick pictures come from the template (`stick_pattern`); their lines are drawn at one weight, which is clear at slide size and smaller at workbook size.

## Instrument A (0 to 2 each)

1 Low floor, high ceiling: 2 (count the sticks in 3 squares; the 100th picture). 2 Depth over speed: 2 (Explore is 11 minutes with strips, guess then build). 3 Generalise: 2 (double and add 1; why the row is always odd; squares against triangles). 4 Justify: 2 (sneak-peek "I know because", Talk time, T2). 5 Multiple paths: 2 (count on, double and add 1, take away the first and share). 6 Challenge ladder: 2. 7 Student-led inquiry: 1. 8 Complexity / context: 1 (sweets, beads, pages, sticks). 9 Problem posing: 1 (the spare-time make-a-table item, online practice). 10 Metacognition: 1. 11 Pacing: 1. 12 Extension, not acceleration: 2.

Total: 19 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled.
- A new topic: the plan has no Primary 1 outcome for a growing shape pattern, so the placement is flagged for a tutor or the owner. The ratio and day tables are Primary 1 items; the stick pattern is not.
- Online practice has no rewind items (the runner cannot assemble them yet). The Term 3 Quest gate for this lesson (triangles use 3, 5, 7 sticks; the next number and the sticks for 5 triangles) uses numbers that Explore and the mini-lesson also use (5 triangles is the guess in Explore round 3): Lesson 30's author should keep the gate and expect those children to recognise it, or change the gate to squares.
- Strip count: 14 supplied, at most 13 used (4 squares, or 6 triangles, in the Investigation).
