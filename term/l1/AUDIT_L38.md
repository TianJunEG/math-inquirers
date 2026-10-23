# Self-audit: Level 1 Term 4 Lesson 8 (Lesson 38, Graph Detectives)

Self-audit written by the author from the validator results of the last build. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present; passes `schema/lesson.schema.json` |
| Every answer verified independently (verify/lNN_checks.py) | PASS | 191 checks: picture-graph rows read from the figure (a row with empty boxes is never read as a number), things counted in the key (1, 2 or 3 at a time, half a picture is half the key), 'how many more' and 'fewer' by pairing pictures one to one, missing rows by trying every size (exactly one fits each total), G2 by trying every number of ducks, geese and hens (exactly one set), class and workbook graphs registered with their keys and shown to differ |
| Online practice variants verified (expression, oracle, runner JS) | PASS | 157 template variants verified three ways |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | script 66:07 of 90:00, slow-class 78:23; no part over in either model (Explore 10:53 and Mini-lesson 10:54 of 11:00 in the slow class) |
| Slides and script linked (each slide once, in its part) | PASS | 32 slides each shown exactly once |
| Tier counts and completeness | PASS | Start here 6, Think harder 3, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | no banned labels or claims |
| Recording cues short, with child action | PASS | 11 cues, at most 26 words |
| Spare-time menu present | PASS | 3 activities (11 optional minutes, not in the 90) |
| No copied contest text | PASS | no 7-word overlap with the external sources |
| Mascot used modestly | PASS | Mi on 4 slides, short lines with no numbers |
| Real PDF page count and fill | PASS | workbook 5 pages (no kit page): 98, 89, 98, 100, 94 percent; home sheet 1 page (91 percent), home answers 1 page, parent page 1 page, key 3 pages |
| Kit contract | PASS | no kit; nothing to find and nothing to cut out |
| Beyond item | PASS | Missing Bar at G1, with the key-of-2 reading at T2 and T3, named in `moe.note` and `beyond`, never at Start here |
| No template leak | PASS | checked on the built files |

## Judgement lines (author)

- Tier principle: PASS. Start here is the Primary 1 reading of a picture graph with 1 picture for 1 thing (most, the same number, how many more, how many in all, True or False, kinds, fewer, most), two shared graphs of four rows each. Think harder is completing a graph from a total and a difference clue (school-level), reading a key of 2 with how many more, and a child who reads the pictures and not the key. Go further is Missing Bar (each picture stands for 3), clues for three kinds of birds, and which question a graph cannot answer. Nothing with a key above 1, and nothing about what a graph cannot tell us, is in Start here, the exit ticket or home slots 1 to 4 (owner decision on picture graphs, 23 Oct).
- Age-appropriateness for 6 to 8: PASS. One idea (read the key first). Objects first: dots and loops on the child's own paper make '1 picture is 2 dots' before any graph with a key of 2. Counts stay within 25. Stems are one or two short sentences and the tutor reads every question aloud.
- Joining cold: PASS, and honestly marked NOT safe to miss (the Quest gate reads a key of 2). The warm-up re-teaches reading a graph, counting in 2s and 3s and a row with a key of 2, so a child who missed Lesson 37 can follow.
- Safeguarding and privacy consistent: PASS. No small pieces, nothing held to the camera, no private chat, made-up data only (no class poll, no counts by child), WhatsApp number only on the grown-up pages.
- Pictures and pages viewed at readable size: PASS with limits. All 5 workbook pages, the key, home sheet, home answers, parent page and all 32 slides were viewed. Workbook graphs are drawn small (about 6 mm pictures in Start here) to keep two shared graphs and six questions on two pages; the key is left out where the stem says what one picture stands for and drawn wherever the key is 2 or 3.

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2 (a key of 1 to a key of 3 and a missing bar); 2 Depth over speed: 2 (every answer is checked by matching, counting in the key and adding back); 3 Generalise: 2 (the same key rule for 1, 2 and 3); 4 Justify: 2 (the Talk question and T3); 5 Multiple paths: 1; 6 Challenge ladder: 2; 7 Student-led inquiry: 1 (the Investigation); 8 Complexity / context: 1; 9 Problem posing: 2 (the Investigation asks for a question the graph can and cannot answer, and a spare-time puzzle); 10 Metacognition: 1; 11 Pacing / compacting: 1; 12 Extension, not acceleration: 2.

Total: 19 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled. No Primary 1 paper uses a key above 1 or asks what a graph cannot tell us, so those parts are beyond the papers and the wording is unverified. The missing bar from a total and a difference clue is a real school item (Ai Tong, Term 4).
- Workbook graphs are small to fit the page; the shared `picture_graph` figure draws a fixed 54-unit picture, so a larger graph needs a bigger `size` and a longer page (a shared-tool note for the report).
- Hand-offs: Lesson 37's `next_materials` says nothing to cut out, which matches this lesson. The hand-off to Lesson 39 follows pre-flight section 5 (the tool-and-problem cards page of Book 8, 15 cards cut out by a grown-up); `lessons/l39.json` did not exist when this lesson was written, so it must say the same.
