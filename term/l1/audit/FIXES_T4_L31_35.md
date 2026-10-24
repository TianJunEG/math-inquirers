# Fixes for AUDIT_T4_L31_35 (Lessons 31 to 35)

Files changed: `lessons/l31.json` to `l35.json`, `verify/l34_checks.py`, `verify/l35_checks.py`, and the hand-off text of `lessons/l20.json`, `l21.json`, `l30.json`. No shared tool was edited (an edit to `b_print.py` was refused: out of scope).
Status: FIXED / PARTLY / NOT FIXED (reason).

## Lesson 31
| Finding | Status |
|---|---|
| H1 kit shapes a third of the size | FIXED by the shared tool (circles and squares now 88 mm, 3 kit pages). Lesson text now says "pages 6 to 8", rectangles are "marked with faint grid lines" (a 4 by 2 grid), not "3 faint lines". L30 hand-off says 3 pages. |
| M2 Investigation first step has no answer box | PARTLY: a long answer line is printed ("Write the number: ______"). A square box needs a `b_print.py` change (inv text does not convert `[]`). |
| M3 faint lines/gaps | FIXED by the tool (grey lines, 6 mm gaps). |
| M4 s-m5-ans wording | FIXED ("One of the 2 parts is bigger than one of the 4 parts"). Guide "papers to the camera" line fixed by the tool (needs rebuild: done). |
| Low: parent grammar, duplicated guide phrase | FIXED. |
| Low: look-back wrap, "half circle" wrap, home Q3/Q4 no picture | NOT FIXED (template: `b_print.py`, home sheet has no picture slot). |

## Lesson 32
| Finding | Status |
|---|---|
| M1 T2 2 by 2 block counted as a big square | FIXED: "Count the small shapes one by one. Do not count a big shape made of small ones", column "Small squares", hint and mistakes updated. |
| M2 S5 split sentence and mixed answer styles | FIXED: "Circle the word that finishes each sentence", sentences have no blank. "half circle" wrap NOT FIXED (template). |
| M3 s-m1 shows the answer while the tutor asks | FIXED: question slide has only the cards; made shapes and answers appear on the next slide (reveal). |
| M4 Investigation drawing box small | PARTLY: two drawing boxes instead of one; the page is full, so no larger. Deck workbook slide thumbnails: tool. |
| Lows (kit gaps, home pictures, "We use them again") | Kit gaps and "We use them again": tool. Home pictures NOT FIXED. |

## Lesson 33
| Finding | Status |
|---|---|
| M1 kit grids unlabelled | FIXED by the tool (frames and "Grid n"). |
| M2 tiny Investigation and E1 grids | FIXED: both grids now fill the 230 px column (size 100, about 15 mm per dot). |
| M3 exit slide thumbnails | NOT FIXED here (the `qs` slide block draws the item picture; checked on the rebuilt deck only). Larger source grid helps. |
| M4 "Count the Routes" name missing on child page | FIXED (T1 starts "Count the Routes."). |
| Lows | G3 sentence split into three lines (a, b, c). Caption "Right, up, right, up" now matches "2 right, 2 up, 1 right, 1 up". Left and down removed from the mini-lesson (s-m3 answer, script, note); practice t3 hint says left is the opposite of right. Home H3 is one question. G1 box overlap: tool. |

## Lesson 34
| Finding | Status |
|---|---|
| M1 S3 convention | FIXED: S3, S4 and T1 now say "Top stack: back left. Right stack: back right. Left stack: front left. Bottom stack: front right." The class slide s-m2 teaches the same four names. Options carry letters A, B, C. |
| M2 cube pictures tiny | FIXED: sizes raised (S1, S2, S3, S4, T1 and exit E1 at 55 to 70 percent; the tool also crops to the stack). Deck thumbnails: tool. |
| M3 class and workbook numbers reused | FIXED: S3, S4 (now 3, 0 / 2, 1, with "write 0 if there is no stack"), T1 (9 cubes, 7 seen, 2 hidden) and T2 (fold at the TOP, holes above and below the fold line; class fold is on the left) differ from the class items. `verify/l34_checks.py` recomputes every new picture (hidden cubes by projection, fold by reflection). |
| M4 option labels | FIXED: opened-paper options in T2 and G1 are tagged A, B, C and the questions ask "A, B or C". |
| M5 kit squares | NOT FIXED: the generic `cards` kit is shared with 20 lessons (tools note). "We use them again" removed by the tool. |
| M6 plural bugs in practice | FIXED by choosing variant numbers (t2 steps 2 to 4; c3 stacks 3 and 4 cubes). |
| Lows | Home Q4 reworded. Look-back wrap, home pictures: NOT FIXED (template). |

## Lesson 35
| Finding | Status |
|---|---|
| H1 online t3 unanswerable | FIXED: the missing-piece item now has word choices ("a plain circle", "a striped circle", ...) and the picture is the 2 by 2 grid only. `verify/l35_checks.py` updated. |
| M2 tiny tiles | PARTLY: 5-tile items now 3 per row (about 20 mm), T2 shows the grid and the lettered options on separate lines (options about 14 mm), larger grid. 4-tile items S3, S6, E2 and the 6-tile T3 are width-limited (a 2-per-row version made the workbook 10 pages): NOT FIXED. B&W: still to check when Book 7 is assembled. |
| M3 kit cards by kind of object | FIXED: sets are the lesson's features on one picture (2 suns and 5 suns: number; big and small: size; striped and dotted: pattern). Explore, answer slide, script and verify updated. |
| M4 page instruction | FIXED (hint_p2 and S5: "tiles that are different"). |
| Lows | Home Q2 reworded. Kit "We use them again": tool. |
| Coordinator item: PDF promise | FIXED: parent line now "If anything is missing or damaged, message us on WhatsApp". No family-facing page of L31 to L35 promises a PDF or a resend; the draft policy remains only in tutor_prep (tutor-only). |

## Hand-offs
- `l20.json`: next-term card on `s-end`, the goodbye SAY line and `parent.next_materials` now say: the Term 3 book, tear out the clock page, a grown-up cuts out the 6 clock hands (faces can stay), keep the $1 tokens (Lesson 24), a real clock helps; `tutor_prep` has a hand-off reminder. `l21.json` `tutor_prep` updated to match.
- `l22.json`: checked, hand-off from L21 already true; no change.
- `l30.json`: hand-off to L31 now lists the 3 fold-shapes pages (pages 6 to 8), a ruler, a coloured pencil and 8 small things (or draw 8 dots) for the warm-up, on the next card, the goodbye SAY line, the slide note and `parent.next_materials`.

## Cross-lesson (X)
X1 Book 7 B&W: not built here. X2: fixed by the tool. X3, X4, X6: template, not fixed.
