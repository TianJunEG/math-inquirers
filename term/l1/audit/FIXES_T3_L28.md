# Fix pass, Term 3 Lesson 8 (lesson 28, Make a Table)

Against `WORKBOOK_AUDIT_L28.md` (WB), `GUIDE_DECK_AUDIT_L28.md` (GD) and `HOME_PARENT_PRACTICE_AUDIT_L28.md` (HP). Rebuilt with `bash term/l1/build.sh 28`: validator 28 pass, 0 FAIL (verify script extended, 123 checks); parts sum to 90, none over (script 67:53, slow 80:25); workbook fills 87, 90, 90, 85, 99% (kit page 51%, 6 pages as designed); home 93%; parent 99%; template leak clean; no slide overflow. Viewed: all 6 workbook pages, key page 2, parent page, slides s-explore1, s-ws1, s-ws2, s-exit, s-opt. Not touched: shared tools, `l20.json`, other lessons.

| Finding | Action |
|---|---|
| WB 1 / GD 3 / HP 1 `stick_pattern` merges sticks (Medium) | Shared figure (`figs3.stick_pattern`, shared deck and online use). S1 now shows three pictures (1, 2 and 3 squares) instead of one, so (a) and (b) each have a picture; the stick drawing itself is listed for the tool owner (separate bars with gaps). |
| WB 2 kit strips 6 mm, cut cells 3.7 mm apart (Medium) | Shared tool (`figs3.stick_strips`). Kit intro now carries the "no printer or no cutting" line. Listed. |
| WB 3 / GD 4 / GD 5 E3 tests odd and even, not taught (Medium) | E3 is now "Rows of triangles use 3, 5, 7 and 9 sticks ... Each new triangle needs 2 more sticks. 8 triangles need ____ sticks" (17; class stops at 7 triangles). The Mini-lesson says once, after the sharing explanation, "Three, five, seven, nine, eleven: every number is odd. Remember that word, odd." (slide note, script line); `joining_cold.assumes` names odd and even (Term 2 Lesson 14); T2's hint uses the word. Answer slide, key, tutor guide and checker updated. |
| WB 4 T3 names "Ben" (Medium) | "A child made a table for squares in a row. One number is wrong." |
| WB 5 / GD 1 / HP 9 `l20.json` hand-off (Medium) | `l20.json` is owned by the Term 2 fix agent: not edited. Mismatch reported in FINAL_FIXES_T3.md item 1. |
| WB 6 tables end before the asked number (Low) | S2 has a spare fifth column (10 blue beads is group 5) and S3 a spare seventh column (7 squares); both questions say "The last column is spare." Verify script checks the columns. |
| WB 7 Investigation drawing box (Low) | Not done: page 5 is 99% full and a drawing box spills the look-back to a new page (tried in Lesson 27). |
| WB 8 / GD 9 optional slide repeats S3 (Low) | Optional slide now gives 1 to 5 squares and asks 9 squares (28 sticks); script, note and checker updated. |
| WB 9 / GD 8 "about 16 minutes" (Low) | "About 18" (3.5 + 4 + 4.5 + 3 + 3) in `timing.notes` and the Work NOTE. |
| WB 10 / HP 5 "We use them again" (Low) | Printed by `b_print.py` (shared); the parent page now says the strips are not needed again. Listed. |
| WB 11 look-back wrap (Low) | Shared template. Listed. |
| WB 12 T2(b) wording (Low) | "Are the sticks in a row of triangles always odd, or always even? Circle one." |
| WB 13 / HP 8 term line (Low) | "Your child is learning to give a reason for each step." |
| GD 2 workbook slide tables tiny (Medium) | The tables of S2, S3 and S4 are repeated large under the questions (S3 and S4 side by side) on s-ws1 and s-ws2; slide notes say so. The thumbnails in the question rows remain (`qs` block is shared). |
| GD 6 Explore round 1 does not say the strip is shared (Low) | SAY, slide item 3 and the note now say the second triangle joins the first and shares one strip, like the picture. |
| GD 7 Explore camera (Low) | Added: tilting the camera to the table is allowed; a face need not be in view; nothing is held up to the camera. |
| GD 10 REC cue before DO (Low) | Opening follows the Term 1 fix (REC, three SAY lines, story line, then DO "Greet the whole group warmly. Do not use children's first names on the recording."); tutor prep matches. |
| GD 11 "papers to the camera 30 s" (Low) | Printed by `tools/b_guide.py` (shared). Listed. |
| HP 2 try-at-home 1 gives no rule (Medium) | "Make a table: 2 spoons of sugar in each cup. 1 cup 2 spoons, 2 cups 4 spoons, 3 cups ___. How many spoons for 5 cups?" |
| HP 3 rewind items (Low) | Runner (shared). |
| HP 4 H3, H4 pictures on the home sheet (Low) | The print tool has no picture slot for home items (shared). Listed. |
| HP 6 recording sentence (Low) | Parent next line: "Please do not share the recording." (the tool prints "Every lesson is recorded ..."; a longer sentence spilled the page). |
| HP 7 H4 answer wording (Low) | "So the first square and 12 more make 13 squares." |
| Hand-off to Lesson 29 | Checked against `l29.json`: 8 mistake cards, the mat is not cut: consistent (checker enforces). Quest gate for this lesson is in Lesson 30 (not edited). |

## Shared-tool needs (for FINAL_FIXES_T3.md)
1. `figs3.stick_pattern`: draw each stick as its own bar with a small gap or alternating tone; at least 25 mm tall in print (workbook, deck and online).
2. `figs3.stick_strips`: 8 mm strips, 6 mm gaps; "We use them again" kit sentence in `b_print.py`.
3. `b_print.py`: home items have no picture slot; look-back wrap. `b_guide.py`: "papers to the camera 30 s". `b_deck.py`: `qs` thumbnails of tables are too small.
