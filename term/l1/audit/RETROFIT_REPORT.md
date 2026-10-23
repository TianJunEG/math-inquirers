# Retrofit report: RETROFIT-NOW (lessons 1-20), re-audit of 13, 19, 20, 27, 30, and late owner decisions

23 Oct 2026, branch `claude/great-fermi-1hv4vc`. Nothing pushed. Deferred as instructed: the rewrite of the six TERMCHECK "too close" lessons (10, 21, 23, 24, 28, 36) stays after 6 Nov; only the lesson 10 timing trim and the chip names (below) touch lesson 10.

## 1. RETROFIT-NOW: thin non-routine spots (year plan section 8.3)
The spine routine, look-back and Toolbox Card were already applied by the integration. What remained under RETROFIT-NOW were the three thin non-routine types. One Think harder item (or one reworked item) per spot, all original, none of the 18 TERMCHECK items touched. Tool: `term/l1/tools/retrofit_nonroutine.py` (idempotent, used for the first pass; later page fits were hand edits). Each lesson: `contest_moves`, the Think harder STUCK line in the script, `verify/lNN_checks.py` updated.

| Lesson | Type | Change |
|---|---|---|
| 7 Take Away, Count Up | work backwards (start unknown) | new T5: Mei gave away 23 beads, has 45, how many at first (68) |
| 8 Balance and Swap | three-number number sentences | new T5: 6, 9 and 15, four sentences plus "9 - 6 = 15, true?" (No) |
| 10 Story Steps | work backwards, two steps | new T5: Lily's stamps, gave 8, got 5, now 20 (15, then 23). Page 3 now fits by cutting writing lines of T1, T3 |
| 15 Equal Groups | true/false about equal groups | T3 (Kumar, 3 plates of 4, "says 7 apples", a + b) turned into a True/False pair: "3 + 4 = 7 apples" (False) and "4 plates with 3 on each hold the same apples" (True). Reason: page 3 had no room for a fifth item |
| 17 Sharing and Grouping | true/false about sharing | new T4: 16 marbles shared among 3, 4, 6 with none left over (F, T, F). To make room the old T4 (17 stickers, bags of 5, 3 more to fill a bag) was merged into T1 as part (c) ("needs 1 more sweet for another group of 4"); T1's picture is 2 rows of 10 |

Workbook page counts unchanged (6 pages each; all books keep the same page counts). Validate 0 FAIL for all five.

## 2. Re-audit of lessons 13, 19, 20, 27, 30 (workbook, home, wording)
Method: every child-facing text of each lesson (workbook, exit, home, online, look-back, parent page) read against WORDING_GUIDE; every question independently solved by hand (all answers right); every workbook page and home sheet rendered and read in colour; "Term N Lesson M" pointers checked against the slot map; kit and hand-off claims checked against the next lesson. Online practice answers solved by hand (all 55 items agree; the 3-way variant check in validate passes). The Playwright runner was not re-run (templates unchanged, validate's variant check passes).

Real faults found and fixed:
1. L19 G2 hint described a different problem ("then 4 pens, then what is left from $20"); now "find 1 pen, then 5 pens, then take away from $30".
2. L19 next_materials said "Quest Log (3 pages)"; the log is 4 pages (checked in `out/l20`). Fixed.
3. L20 hand-off (parent page and spoken goodbye) said "Lesson 24"; families see Term 3 Lesson 4. Fixed; the slide line also shortened under the 40-word reading limit.
4. L13 kit shape cards used colours different from the shapes in the workbook (circle yellow vs pink, triangle green vs yellow, star yellow vs lilac). Kit colours now match the pictures.
5. L20 G1 (c): "Shop A / Shop B" choice words wrapped into four words. Question shortened ("Where does 1 pen cost less? Circle one."); L20 investigation first step had no question, now says Mei's number is 6 and asks for one more puzzle; T1 draw-stroke warning (36) was a false estimate (a strip of 5 boxes): `draw_strokes: 6`.
6. L30 S1 stem "Then look at the game." was a hidden second scenario; now "Look at the clock. A bus leaves at 7:30. The trip takes 1 hour." (the game is part b).
7. L27 tutor-only notes said "Lesson 30"; now "Term 3 Lesson 10".

Found, not changed (judgement calls):
- L13 S3(b) "Mei says 8 + 9 is 1 more than 8 + 8" teaches inside a Start here question (WORDING_GUIDE rule 24). Kept: the item is what tests the "double and one more" idea retired from the Doubles lesson.
- L20 kit has 7 tool cards ("In my head" is the seventh) while the lesson and parent page say six tools. Kept, consistent in all texts.
- L27 S1 table has an empty last cell (layout of 2 x 4). A single 7-cell row overlapped the words, so it was left.
- L30 home sheet item 1: the "$" and the blank wrap onto two lines. Cosmetic, shared home layout.
- L13 pictures of the circle and heart are both pink (outline and dot tell them apart; B&W fine).
- Term 3 parent pages do not state "beyond Primary 1 on purpose" (lessons 21-40 put it in the tutor script only; Term 1-2 lessons put it on the parent page). Consistent within each term; owner may want one rule.
- Beyond field (preflight T9): L1-19 still lack the `beyond` field (validator requires it from Term 3 only). Not part of the decision text, not done.

## 3. Late owner decisions
- SPINE-CHOICES-OK: spine rows for 13 (Work backwards, Act it out), 19 (Draw it, Make a table), 27 (Spot the pattern, Act it out) kept, no change.
- L10-TRIM: lesson 10 slow-class total 90:00 -> 86:52 (3:08 saved): modelled child work and response seconds cut in Remember (response times), Explore (rounds 1-3: 70/60/70 -> 50/45/50 s), Mini-lesson (55/60/40 -> 40/45/30 s) and the choice-time block (170 -> 120 s). No slides or content removed. These are modelled seconds only: the first trial lesson should still time it. Normal-class script need 73:46 (was 76:22).
- CHIP-NAMES: the page-1 chip of choose lessons 10, 20, 30, 40 now prints each tool name (6.5 pt) under its icon (`tools/spine_term.py`, `wb_chip`). Pages still fit (6, 6, 6, 5 pages). Lesson 39 is also a choose lesson and got the same chip when rebuilt; it was not rebuilt here, so its PDF still shows icons only: rebuild 39 if wanted (open choice).
- Names at 6.5 pt are small; icon plus name is readable in the colour render, B&W readability should be glanced at on a printed copy.

## 4. Open owner choices
1. Lesson 39 chip names (same code; needs a rebuild of 39 and books 7-8 if wanted; Book 8 is not affected by lesson 39 rebuild unless run).
2. Whether to add `beyond` to lessons 1-19 (T9).
3. Whether Term 3-4 parent pages should say "beyond Primary 1 on purpose".
4. Lesson 15 now has one fewer calculation item (T3 became True/False) and lesson 17 one fewer item (old T4 merged); confirm that is acceptable or choose which Think harder item to drop for a fifth in future page designs.
5. Rewrite of 10, 21, 23, 24, 28, 36 after 6 Nov (deferred, not touched except the timing trim and chip in 10).

## 5. Unsure
- The retrofit items are original but have not been through the TERMCHECK similarity run (the private files); run it on 7 T5, 8 T5, 10 T5, 15 T3, 17 T4 before print.
- True/False layout for lessons 15 and 17 is the existing `tf` table; 2 rows in lesson 15 (not 3) to fit the page.
- Lesson 10 trim only changes the timing model, not what the tutor says.

## 6. Books
All 8 books rebuilt (colour): workbook pages 46/44/46/46/42/44/48/42, keys 22/32/22/30/22/32/22/32, home 12/14/12/14/12/14/12/14, all even, unchanged. B&W: see section 7.

## 7. Validation and B&W
`validate.py` on all 40 lessons after the final builds: 0 FAIL. All 24 colour term PDFs have even page counts (listed in section 6). B&W: `print/make_bw_print.py --only BookN_ --resume` run per book (the all-at-once run stalls), then `print/check_bw.py`: all 24 term PDFs ok, max non-grey 0.00000, page counts equal the colour books.
