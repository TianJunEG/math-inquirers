# Self-audit: Level 1 Term 4 Lesson 7 (Lesson 37, Make Your Own Graph)

Self-audit written by the author from the validator results of the last build. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present; passes `schema/lesson.schema.json` |
| Every answer verified independently (verify/lNN_checks.py) | PASS | 224 checks: trays counted cell by cell, picture-graph rows read from the figure (a row with empty boxes is never read as a number), tallies rebuilt stroke by stroke for 0 to 20 and read back, 'how many more' by pairing pictures one to one, missing rows by trying every size, G2 by trying every number of stickers for the four children (exactly one set fits), key of 2 by counting in 2s, class and workbook numbers registered and shown to differ |
| Online practice variants verified (expression, oracle, runner JS) | PASS | 156 template variants verified three ways |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | script 65:06 of 90:00, slow-class 77:08; no part over in either model; Explore is the fullest part in the slow class (10:44 of 11:00) |
| Slides and script linked (each slide once, in its part) | PASS | 32 slides each shown exactly once |
| Tier counts and completeness | PASS | Start here 6, Think harder 3, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | no banned labels or claims |
| Recording cues short, with child action | PASS | 11 cues, at most 26 words |
| Spare-time menu present | PASS | 3 activities (11 optional minutes, not in the 90) |
| No copied contest text | PASS | no 7-word overlap with the external sources |
| Mascot used modestly | PASS | Mi on 4 slides, short lines with no numbers |
| Real PDF page count and fill | PASS | workbook 6 pages: 98, 99, 98, 95, 96 percent; kit page 75 percent (a mat, short pages are allowed); home sheet 1 page (99 percent), home answers 1 page, parent page 1 page, key 3 pages |
| Kit contract | PASS | 1 graph mat supplied, 1 used (Explore); 12 small things from home, 12 sorted |
| Beyond item | PASS | One Picture Is Two at G1 (Go further), named in `moe.note` and `beyond`, never at Start here |
| No template leak | PASS | checked on the built files |

## Judgement lines (author)

- Tier principle: PASS. Start here is counting kinds on a tray, reading a tally, reading a graph (more, in all, fewest, True or False), and drawing a graph from numbers, all with 1 picture for 1 thing and numbers of 8 or fewer in a row. Think harder is a tally with a table, choosing a question the graph can answer, and a missing row from a total (work backwards). Go further is a key where each picture stands for 2 and half a picture (One Picture Is Two, beyond Primary 1 on purpose), clues for four children, and writing a question. Nothing non-routine is in Start here, the exit ticket or home slots 1 to 3.
- Age-appropriateness for 6 to 8: PASS. One idea (a graph answers a question: sort, count, picture). Objects first: real things from the house, sorted into piles, then drawn on a mat. Counts stay at 12 things. Reading load: stems of one or two short sentences; the tutor reads every question aloud.
- Joining cold: PASS, and honestly marked NOT safe to miss. The warm-up re-teaches reading a graph, counting in 2s and sorting; the next lesson and the Quest gate read graphs the way this lesson draws them.
- Safeguarding and privacy consistent: PASS. Small things stay on the table, no food, nothing held to the camera, no private chat, the data are made up or the child's own things (no class poll, no counts by child), WhatsApp number only on the grown-up pages.
- Pictures and pages viewed at readable size: PASS with limits. All 6 workbook pages, the key, home sheet, home answers, parent page, kit page and all 32 slides were viewed. The mixed tray is drawn with the shared `table` figure, whose icons are about 9 mm on paper: readable, but smaller than the graph pictures (a shared-tool need, see the report). Graphs in the workbook are drawn small to fit six pages, with the key left out where the question says what one picture stands for.

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2 (sorting real things to a key of 2 and a half picture); 2 Depth over speed: 2 (a graph is checked three ways: matching, counting, the total); 3 Generalise: 2 (any set of things can be sorted and pictured); 4 Justify: 1 (the talk question and the choose-a-question items, no written reason); 5 Multiple paths: 1; 6 Challenge ladder: 2; 7 Student-led inquiry: 2 (the child chooses the things, the kinds and the question); 8 Complexity / context: 1; 9 Problem posing: 2 (G3, the Investigation and a spare-time puzzle); 10 Metacognition: 1; 11 Pacing / compacting: 1; 12 Extension, not acceleration: 2.

Total: 19 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled. No Primary 1 paper collects, tallies or sorts for a graph (papers only read or complete one), so those parts are activity and the wording is unverified.
- The jumbled tray depends on the shared `table` figure and is small on paper. The graph mat is a column graph while the workbook graphs are rows (the lesson says to turn the mat on its side).
- Hand-off checked against `lessons/l36.json` (written after this lesson): its `parent.next_materials` names the Book 8 graph-mat page with no cutting, about 12 small things from the house in 3 or 4 kinds (not food) and optional coloured pencils, which is exactly what this lesson needs. This lesson's own hand-off to Lesson 38 says nothing to cut out, matching Lesson 38.
