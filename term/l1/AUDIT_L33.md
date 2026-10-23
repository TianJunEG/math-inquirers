# Self-audit: Level 1 Term 4 Lesson 3 (Lesson 33, Copy on the Grid)

Self-audit written by the author from the validator results of the last build. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present |
| Every answer verified independently (verify/lNN_checks.py) | PASS | verify: 275 answer checks (routes enumerated by depth-first search and rebuilt by corner numbers; copies tested by translated edge sets) |
| Online practice variants verified (expression, oracle, runner JS) | PASS | practice: template variants verified three ways |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS with warning | script 67:30 of 90, slow class 79:48; Mini-lesson is 12:07 in the slow-class model (11:00 allocated), absorbed by the 5-minute flex buffer |
| Slides and script linked (each slide once, in its part) | PASS | 34 slides each shown exactly once |
| Tier counts and completeness | PASS | Start here 6, Think harder 3, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | no banned labels or claims |
| Recording cues short, with child action | PASS | 11 cues, at most 26 words |
| Spare-time menu present | PASS | 3 activities, 11 optional minutes |
| No copied contest text | PASS | no 7-word overlap with external source text |
| Mascot used modestly | PASS | Mi on 3 slides |
| Real PDF page count and fill | PASS | workbook 6 pages: 100, 96, 99, 96, 98 percent; kit page 63 percent (short by design); home 1 page, parent 1 page |
| Kit contract | PASS | grid page supplies 3 route grids and 2 copy grids; the most a task uses is 3 and 2 |
| No template leak | PASS | checked on the built files |

## Judgement lines (author)

- Tier principle (Start here approachable and not contest-style; Think harder = taught idea in a new setting; Go further = mastery plus extension): PASS. Start here is copy by counting steps, say a move as right and up, follow directions, pick the exact copy, finish a rectangle and steps against dots. Routes only at Think harder and Go further (Count the Routes, listing, a repeating path, corner numbers, a route that must pass a corner).
- Age-appropriateness for 6 to 8 (reading load, one new idea, objects before symbols): PASS. One idea: count steps between dots. Objects first (grid page and a button). Stems are one or two short sentences; the tutor reads every question.
- Joining cold: PASS. Rows and columns, steps between dots and right and up are re-taught with pictures; fairly safe to miss, with a Quest gate noted.
- Safeguarding and privacy consistent between script, slides and guide: PASS. Recording notice before recording, no first names while recording, no papers or drawings to the camera, no private chat, WhatsApp number only in the grown-up page, wrong working only to 'a child'.
- Pictures and pages viewed at readable size, nothing clipped or overlapping: PASS. All 6 workbook pages, kit page, key, home sheet, parent page and all 34 slides viewed. Question pictures on the workbook are small (grids are held to 250 px by the shared style); drawing tasks use grids 4 steps across at most.

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2 - copying at the floor; corner numbers and a route through a corner above;
2 Depth over speed: 2 - steps not dots, list in order so none is missed;
3 Generalise: 2 - every route has the same steps (Investigation);
4 Justify: 2 - Talk question and how do you know prompts;
5 Multiple paths: 2 - many routes to one dot;
6 Challenge ladder: 2 - Start, Think, Go, Investigation;
7 Student-led inquiry: 1 - children choose pages; routes are discovered in the Mini-lesson;
8 Complexity / context: 1 - abstract grids, little story;
9 Problem posing: 2 - G3 and the spare-time puzzle;
10 Metacognition: 1 - look-back, Talk;
11 Pacing / compacting: 1 - flex buffer and skip order only;
12 Extension, not acceleration: 2 - counting routes is a new way of thinking, not later content.

Total: 20 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled. No school-paper evidence for grid copying: wording unverified. The kit page heading "draw the other half" (shared tool) does not match copying; the intro line explains the dashed line.
- Shared-tool needs are listed in the report: fold_punch folded stage does not mark the fold edge; fold_shapes prints 28 mm shapes; grid has no dot labels and counts only in squares.
