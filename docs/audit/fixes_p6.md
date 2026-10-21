# Fixes applied for the P6 audit (docs/audit/audit_p6.md)

Date: 2026-10-22. Source edited: `p6/content/l1.js` to `l10.js`, `rebuild/gen_p6l1.py` to `gen_p6l10.py`, `p6/guide.js`, `p6/SPEC.md`, `p6/data.js` (comment), and one shared file (see "Shared files"). Nothing was committed or published.

## Important limitation (read first)

Scratch block names and colours could not be checked online (the audit said so too). I used only Scratch 3 palette names I am sure of: `when green flag clicked` (drawn "when [flag] clicked" in Scratch), `move () steps`, `turn ↻ () degrees` / `turn ↺ () degrees`, `go to x: () y: ()`, `point in direction ()`, `say () for () seconds`, `ask () and wait`, `answer`, `set [] to ()`, `change [] by ()`, `repeat`, `repeat until`, `if then`, `if then else`, operators `+ - * / mod pick random join letter () of () length of ()`, list blocks `item # of () in []`, `item () of []`, `length of []`, and Pen `pen down` and `erase all`. Our slide and workbook drawings use simplified colours, and every lesson's online text now says so ("find blocks by the category name on the left, not by colour"). The three behaviours in items 2, 5 and 6 of the checklist below are from knowledge, not from a test.

### 7-point editor check (10 minutes, before the programme goes out)
Open scratch.mit.edu and confirm:
1. The hat block reads "when [flag] clicked" (our slides write "when green flag clicked").
2. The turn blocks show arrow icons (↻ and ↺), not the words "right" and "left".
3. The names `item # of ( ) in [list]`, `item ( ) of [list]` and `length of [list]` (and that `item # of` finds a letter whichever case it is typed in).
4. The Sensing category (ask and wait, answer) is light blue.
5. The list blocks are red-orange (Variables palette).
6. `( ) mod ( )` with a negative number returns a non-negative result (-4 mod 26 gives 22).
7. Sprite fencing at the stage edge for the L7 sizes (octagon, 10-gon, 12 to 15 sides, 9 and 20 point stars, 10-point star), started from the standard set-up x: -50 y: 100, direction 90. Also run the L8 machine once with a message containing spaces (MYNO SC PEX, shift 16 gives CODE IS FUN).

### "Where is each block?" cheat sheet (for tutors; same wording as the audit, shortened)
Motion: move, turn ↻ / ↺, go to x y, point in direction, set x to, change x by, x position. Looks: say, say for seconds. Events: when green flag clicked. Control: repeat, repeat until, if, if else. Sensing: ask and wait, answer. Operators: + - * / mod, pick random, join, letter of, length of, = < >, and. Variables: Make a Variable, set, change, and the list blocks (item #, item of, length of list). Pen extension (L7): erase all, pen down.

## Per issue

| # | Sev | Status | What was done |
|---|---|---|---|
| 1 | High | Applied | Every `when start clicked` is now `when green flag clicked` in `l5.js`, `l6.js`, `gen_p6l5.py` (3), `gen_p6l6.py` (2). Also normalised the older `when flag clicked` to `when green flag clicked` in L3, L4, L9, L10 (content and generators) so all 10 lessons agree. Grep shows no `start clicked` left outside the audit file. |
| 2 | High | Applied | L1 Q5 palette block is `say (n) for (1) seconds` (key says one term per second). L1 `teachtrace` slide also had a plain `say` inside a loop: fixed (not in the audit). L2 Q6 block A is `say (d) for (1) seconds`, key "8 numbers, one per second". L2 `teachplan` drawing, answer and notes fixed. I did not add the report's extra parenthetical to the L1 Q5 question (it pushed the page to 3 pages); the palette block itself carries the fix. |
| 3 | High | Applied | New slide `p6l8-teachloop` draws the whole machine (set shift, ask, set code to empty, set i, repeat length of answer, letter i of answer, if item # of > 0 then the three cipher blocks else join the letter, change i, say code) and notes that the tutor gives the loop pre-built so children add only the three cipher blocks. Spaces are handled in the starter (if / else), "keep spaces" removed from the extension text, the exact starter-project sentence added to `lesson.online`, Q2 now says to type capitals and that the starter keeps spaces. `gen_p6l8.py` `blocks()` gained if / else drawing (local to that file). Space bug and the fix verified in Python (see below). The `.sb3` file itself is not built (see 7). |
| 4 | High | Applied | New slide `p6l7-setup` (erase all, go to x: -50 y: 100, point in direction 90, pen down) with sizes. Caption "after set-up" on the drawing slides, explore notes, workbook header, Q1, Q2 and Q4 (move 120 for the 9-point star, 100 for the 20-point star, 30 for 24 sides, 10 for 36 sides). I simulated every drawing from (-50, 100): the report's "move 80 up to 15 sides" does NOT fit (12-gon at move 80 reaches y = -199), so the slides use move 80 up to 10 sides and move 50 for 12 to 15 sides. The extension rosette goes off the stage from the standard start (y = 236), so it now says to start at go to x: 0 y: 0. |
| 5 | High | Applied | All L7 block drawings (slides, workbook, aria-labels) read `turn ↻ (N) degrees`; explore notes and the set-up slide say it is the clockwise arrow block ("turn right" kept in speech); pseudo-code in the question bank and deck data also uses `turn ↻`. |
| 6 | Med | Applied | L4 note now "Sensing (light blue)"; L8 note now "list blocks are red-orange, in the Variables palette". Simplified-colours sentence added to the online text of all 10 lessons (content and title-slide notes). Cheat sheet is in this file, not printed as a page (optional in the audit). |
| 7 | Med | Partly | Done: the L1 sentence about sending blocks in the chat replaced by "share your Scratch window and build the four blocks together"; same fix in L2; L5, L8, L9, L10 now say the tutor shares `.sb3` files (File, Load from your computer) with links as a backup; scratch.mit.edu needs no account noted in L1. NOT done: building the eight `.sb3` files (`p6/starters/`). They cannot be created or tested without the Scratch editor; the L8 whole-machine slide and the L10 starter slides give the blocks. Tutors must build and save them once. |
| 8 | Med | Applied | L5 menu board now numbers the teas and toppings (1 milk, 2 green, 3 taro; 1 pearls, 2 jelly), explore step 4 and the notes explain that 21 means green with pearls, title notes tell the tutor the starter says numbers. |
| 9 | Med | Applied | L3 `online` text, L3 title notes and explore notes: type the minus with the keyboard minus key, do not paste from the slide. |
| 10 | Med | Partly | Time slots applied to all of L1 to L9 and the tutor guide: worksheet 40 to 75, ws2 now ends at 72 (check-together 72 to 75), talk 75 to 82, exit 82 to 90 (slide labels, title notes, per-slide notes, `guide.js` routine table and lesson sections). L9 challenge and diagram slides relabelled 62 to 75. NOT done: moving one item per lesson from the worksheet to Think Harder (L2 Q5, L5 Q5b, L6 Q4d, L7 Q5, trimming L7 Q1). Each move changes question numbers, keys, slides, previews and the Think Harder page contents and would need a page-layout check; the extra 5 to 6 minutes per page 2 was applied instead. Recommend revisiting after a pilot. |
| 11 | Med | Applied | L10 timeline: warm-up 0 to 5 (single slide; `p6l10-warm2` removed, its questions kept as spare in the relay notes), challenge round 5 to 22, starters 22 to 29, break 29 to 32, plan and build 32 to 62, showcase 62 to 87 (3 min plus 20 s switch), exit and certificates 87 to 90 (talk 87 to 88, exit 88 to 90). Slide labels, title notes, per-slide notes and a Lesson 10 note in the tutor guide updated. Homework line added to the L9 `close` (also in the L9 exit notes). No-screen-share option added (L10 online, showcase notes, title notes). Build target "a working copy of one starter with one change is full marks" added. Note: 8 children x 3 min 20 s is about 27 minutes, so the 25 minutes assumes the next child is ready while the previous one answers questions (said in the notes). |
| 12 | Med | Applied | L4 Q1(c) table is IN 1, 2, 3, 4, 20, OUT 1, 5, 9, 13, ? (rule 4n - 3, answer 77, key unchanged); check-together note updated. |
| 13 | Med | Applied | `l7.js` challenge items 8 and 9 replaced with the report's wording and answers (square + octagon + octagon, triangle + 12-gon + 12-gon; turn 60 draws the hexagon, turn 120 a triangle twice round). Both programs fit the stage. |
| 14 | Med | Applied | L3 challenge 9 rewritten (level 1 is ground, B1 below, count the levels one by one), answer still 6. |
| 15 | Med | Partly | `SPEC.md` now states which blocks are assumed known and which are taught in lesson; L2 `we3` main program is now only the counter (`say count`), with the if / else prime / not prime version moved to the extension text and notes; L3 explore notes tell the tutor to make the variable live in the screen share. NOT done: the 10-minute Scratch warm-up video or handout (needs to be recorded or designed). |
| 16 | Low | Applied | Covered by the L7 set-up slide (includes erase all) and the "after set-up" captions. |
| 17 | Low | Applied | L5 note now "say 23 and 24, which are not real outfits". |
| 18 | Low | Applied | L8 online text and explore notes: coded names held up on paper or read out, no private chat. |
| 19 | Low | Applied | L9 `talkAns` reworded as in the report. |
| 20 | Low | Applied | `gen_p6l9.py` and `gen_p6l10.py` now set the footer to "Math Inquirers P6  •  Notice it. Test it. Explain why." (checked: no P6 slide has "Holiday Program" in the footer). `p6/data.js` comment fixed (p6/content). |
| 21 | Low | Skipped | Optional design change (silent brain-break alternatives); not a typo or wording fix. |
| 22 | Low | Skipped | Optional spelling choice (dice / die). |
| 23 | Low | Partly | L10 Python prints "factor(s)"; L7 workbook Python box says the output is 144.0 720.0 and needs Python turtle (for example Trinket). L2 list-comprehension snippet left as is (optional). |
| 24 | Low | Applied | L3 Q7(b) rewritten ("After the loop she is at -28 m. One more block: change depth by ___ . What number brings her back to 0 m?"). |

### "Sec 1 bridge" and "appear in Secondary 1" overstatements (task priority)
- `p6/SPEC.md`: "bridges to Secondary 1 maths" is now "enrichment toward secondary maths and coding" with a note on which topics are met directly in lower secondary and which are enrichment; table column renamed "Maths (enrichment toward secondary maths)".
- `p6/content/l10.js`: `talkAns` no longer says all topics appear in Secondary 1 (now "enrichment toward secondary maths and coding, not a preview of exam topics"); the talk question and the closing line no longer promise Secondary 1 use. `gen_p6l10.py` end slide: "Ready for Secondary 1" is now "Ten lessons of maths and code".
- Parent pack: `hp/parent_pack_level.py` label "Secondary 1 bridge" is now "Maths and coding bridge" for P6. `p6/parent_side.json` had no overstatement, so it is unchanged.
- L6 online text says probability is enrichment; L9 online text says the mean is familiar and the new parts are lists, loops, median, mode and misleading averages.
- Left as is (accurate per the audit): L3 and L4 lines saying negative numbers and algebra with a letter are met in Secondary 1, `guide.js` "going into Secondary 1", `levels/mklevel.py`.

## Python re-verification of changed answers
Run with python3 (script in the session scratchpad):
- L1 Q5: 20 terms of 4, 10, 16, ... end at 118 = 6 x 20 - 2.
- L2 Q6: factors of 40 are 1, 2, 4, 5, 8, 10, 20, 40 (8 numbers). L2 `we3`: count is 4 for 15 (not prime), 2 for 13 (prime), 4 for 6 and 8 (matches Q3 and `teachtrace`).
- L3: 7 x -4 = -28 (Q7); lift from level 4 to B3 is 6 moves (challenge 9).
- L4 Q1(c): 4n - 3 gives 1, 5, 9, 13 and 77 at n = 20.
- L7: 90+135+135 = 90+120+150 = 60+150+150 = 360; turn 60 x 6 = 360 (hexagon), turn 120 x 6 = 720 (triangle twice). Stage simulation from (-50, 100), heading 90: triangle, square, pentagon, hexagon (move 100), 8 to 10 sides (move 80), 12 and 15 sides (move 50), 24 sides (move 30), 36 sides (move 10), Ben's nonagon (move 80, turn 120), {5/2} move 150, {8/3} move 200, {9/2} turn 80 move 150, {9/4} move 120, {20/3} move 100 and the 10-point star move 150 all stay inside the 480 x 360 stage. Not fitting: 12 sides at move 80, {20/3} at move 150, the rosette from the standard start.
- L8: the machine with the space check gives CODE IS FUN (MYNO SC PEX, shift 16), WPGGH (PIZZA, 7), BFD (WAY, 5), MATH IS FUN (PDWK LV IXQ, 23), PHHW DW WKH PUW (shift 3); without the check a space becomes a letter (CODEPISPFUN), confirming the audit.

## Files changed
- Content: `p6/content/l1.js`, `l2.js`, `l3.js`, `l4.js`, `l5.js`, `l6.js`, `l7.js`, `l8.js`, `l9.js`, `l10.js`.
- Builders: `rebuild/gen_p6l1.py` to `gen_p6l10.py` (L7 gains `p6l7-setup`, L8 gains `p6l8-teachloop`, L10 loses `p6l10-warm2`).
- P6 only: `p6/guide.js` (times, Lesson 10 timing note), `p6/SPEC.md`, `p6/data.js` (comment only).
- Docs: `docs/audit/fixes_p6.md` (this file).
- Shared file touched (unavoidable, backward compatible): `hp/parent_pack_level.py`, one line, the label changes only when the level number is 6; levels 1 to 5 are unchanged. No other shared file (`slidekit.py`, `restyle.py`, `build_level.sh`, `scheme.py`) was edited. Note `levels/scheme.py` still says "non-routine puzzles tagged to the school syllabus" for every level, which is not accurate for P6; left alone because it is shared.

## Regenerated and rebuilt
- Deck keys regenerated with `python3 rebuild/gen_p6lN.py` and then `python3 levels/restyle.py split/p6lN` for N = 1 to 10: `p6l1`, `p6l2`, `p6l3`, `p6l4`, `p6l5`, `p6l6`, `p6l7`, `p6l8`, `p6l9`, `p6l10` (all 10; every lesson had at least a time label, online text or block change). Slide counts: L1 26, L2 26, L3 25, L4 26, L5 26, L6 27, L7 27, L8 27, L9 26, L10 25. No slide overflows (checked with `rebuild/preview.py`).
- `bash levels/build_level.sh 6` run: workbook (45 pages, the same count as before the fixes; L1, L2 and L7 pages were trimmed so each lesson is still 2 worksheet pages and 2 Think Harder pages), tutor guide PDF and docx, weekly PDFs and zip, parent pack (Weekly Dose), and the scheme of work.
- Not done by me: publishing or re-uploading the decks anywhere (the deck URLs in `outputs/deck_urls_*.json` now point to old versions of all 10 P6 decks).
