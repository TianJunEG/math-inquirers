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
- CHIP-NAMES: the page-1 chip of choose lessons 10, 20, 30, 40 now prints each tool name under its icon (CORRECTED 24 Oct 2026: the old claim of 6.5 pt was wrong, the printed size was 6.1 pt; after FIXES_BOOKS_1_4_ROUND2 the measured size in the books is 12.6 pt for lessons 10 and 20 (4 and 6 names) and 9.6 pt for lessons 30, 39 and 40 (7 and 8 names, wrapped onto two or three lines)) (`tools/spine_term.py`, `wb_chip`). Pages still fit (6, 6, 6, 5 pages). Lesson 39 is also a choose lesson and got the same chip when rebuilt; it was not rebuilt here, so its PDF still shows icons only: rebuild 39 if wanted (open choice).
- Names at 6.5 pt (old figure, see above) were small; icon plus name is readable in the colour render, B&W readability should be glanced at on a printed copy.

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

## 8. Follow-ups (coordinator, same day)
1. **Lesson 39 chip names:** lesson 39 rebuilt; its page-1 chip now shows tool names like 10, 20, 30 and 40. Book 8 rebuilt colour and B&W. (Section 4 item 1 is closed.)
2. **Beyond line consistent:** every Term 1 to 4 parent summary now says some Think harder and Go further questions go past the school Primary 1 syllabus on purpose and that Start here stays within it (added to lessons 3 and 21 to 40; lessons 1, 2, 4 to 20 already had it). Section 4 item 3 is closed. Parent summaries are not in the books, so no book changed for this; lessons 3, 7, 10, 21 to 40 were rebuilt. Item 2 (a `beyond` metadata field on L1 to 19) is still open.
3. **Similarity run on the five retrofit items** (L7 T5, L8 T5, L10 T5, L15 T3, L17 T4, plus L17 T1 which changed): 5-word run test and content-word overlap against all 13,479 lines of the 21 private files (P1 to P6 lists and records, word-problem notes, SASMO notes). No 5-word run shared with a real source beyond 2 words of stock; no item reached "too close". Closest: L7 T5 (some beads, gave away, find the start) next to a P1 two-step beads entry and a "gave away, at first" family: same family, different numbers and structure, but the scenario was close enough that I changed it (beads to plums, Mei to Kumar). L10 T5 (stamps) shared the word "stamps at first" with a percent question; changed to badges. L8 T5, L15 T3, L17 T4 and L17 T1 had no similar item (best overlap 0.27 to 0.29, all different scenario). The similarity method here is my own re-implementation of the TERMCHECK method (run test plus content-word overlap), not the original script, and only the five items were read side by side.
4. **Validation:** validate.py on all 40 lessons: 0 FAIL. Colour books page counts unchanged and even (46/44/46/46/42/44/48/42; 22/32/22/30/22/32/22/32; 12/14 pattern). B&W re-converted for Books 1, 2 and 8 (the books whose content changed); Books 3 to 7 B&W files are older than the colour files but their content is identical (only lessons 3, 7, 10, 39 changed). check_bw.py: all 24 term PDFs ok, non-grey 0.00000.

## 9. Combined fix pass after the two independent audits (AUDIT_BOOKS_1_4.md, AUDIT_BOOKS_5_8_ROUND2.md)
All 40 lessons rebuilt after the last tool change, validate.py 0 FAIL on all 40, all 8 books rebuilt (colour: workbooks 46/44/46/46/42/44/48/42, keys 22/32/22/30/22/32/22/32, home 12/14/12/14/12/14/12/14, all even, unchanged) and converted to B&W per book.

### Books 1-4
- **H1 Quest Log pages (fixed).** The five "3 pages" strings in `l20.json` now say 4 pages; verified in the Book 4 key (sections 2.1 and 3.1) and the Book 4 home pack note.
- **M1 snail figure, L9 G2 (fixed).** The stretched bar with a shell is now a plain path bar labelled "The snail's way forward: 4 to 13"; no shell near the answer.
- **M2 L4 G3 layout (fixed).** The 4-square block is now centred above the questions at full text width (`hundred` figures accept `size` and `wide`); Yes/No sit at the end of their sentences.
- **M3 (fixed).** L19 page 3 now says "Such means the same kind."; L20 page 3 no longer mentions "where it says Choose".
- **M4 (fixed).** L19 investigation key says $4.
- **M5 shrunk text (NOT fixed).** The pages go to the smallest text size because the page-fit loop tightens any page over 96.5% full (class `tight3`, 15 px). The fills are 94 to 100% on exactly the pages that took the retrofit items; restoring 13 pt means removing or moving an item per page (for example L6 T4, L8 T4, L10 T4, L11/L13/L15 page 3 items, L17 page 3). That is an owner choice about which items go (they cannot be moved to page 4: Go further is also full). Left as is.
- **M6 tiny figures (partly fixed).** Enlarged: L3 S3 and L5 S4 (bundle figures at full width), L8 S6 (85%; S1 stays 60%: page 1 is already 100% full and it spilled when enlarged), L21 and L22 exit clocks (to 58-62%; the home-sheet clocks in lessons 21-30 are now 31 mm, were 22 mm), L32 S3 grid, L33 E1 and Investigation grids (70%), L34 T3 grid (65%) and T2 fold figures (80%), L35 E2 (90%). Tried and reverted because a page spilled: L8 S1 above 60%, L32 T2 wide, L35 S3/T3 wide, L36 T1 above 44%, and a blanket 1.25 to 1.35 scale on lessons 31-34 (all four spilled onto orphan pages). Not enlarged (no room on the page): L11 S3/T2 line-ups (10 children across one column), L35 T3 (6 tiles in a row), L34 S-page cube figures.
- **M7 L6 G1 number line (fixed).** The tick labels 10 and 100 were suppressed next to the tiles 7 and 97 (clash rule too wide); now printed. Shared tool `figs4.jump_lines`.
- **M8 Quest parent notes (fixed).** The sentence "goes beyond the Primary 1 syllabus on purpose, so a few gates may be new" is gone from the Term 1 to 4 Quest notes (L10, L20, L30, L40). Replaced by the true statement that every gate is Start here in fresh numbers (L40: except the picture graph key of 2 taught in Term 4 Lesson 8).

### Books 5-8
- **M1 L39 G1 (fixed).** One bar "In all" with Jason (1 part) and Jenny (3 parts) and the 36 bracket over the whole bar; part (b) no longer prints the answer to (a) (it asks for Jason by the table of tries; Jenny has its own part). Verify script updated.
- **M2 Book 8 Quest Log headings (fixed).** Page 2 "Gates 3 and 4", page 3 "Gates 5, 6 and 7". (Book 4's page 3 line "Circle Yes or No where you see it" is right: gate 7 has one.)
- **M3/M4 L35 fills and sun card (fixed).** Stripes and dots are now anchored to each shape's own centre with a finer pitch (identical shapes show identical fills; a turned triangle shows the same dots); the 5-sun kit card has smaller suns with space to the cut line. `figs3.panel` and `_sun_card`.
- **M5 clocks (fixed).** Exit-ticket clocks (L21 E1, E2; L22 E1, E3) enlarged; home clocks (lessons 21-30) now 31 mm.
- **M6 absolute lesson numbers (fixed).** Quest tutor notes, parent note and the gate table now use term-local numbers ("Term 3 Lesson 8"); the Quest builder prints "Term 3 Lesson 4" instead of "L24". Prose in `l30.json` and `l40.json` converted too.
- **M8 L22 T4 (fixed).** The question now says "A show is on until the next show starts."
- **M9 L34 G3 (fixed).** Question stays; the key now accepts 0 ("four numbers from 0 to 3 that add to 7", for example 3, 3, 1, 0).
- **M10 L39 T1 (fixed).** Key accepts Make a table as well as Try something simpler (part (a) is now an open choice).
- **Low fixed:** page numbers moved up 2 mm (now 5.5 mm from the bottom edge); "1 pages" fixed; stale tutor line "accept 5 or 5th ..." removed from `l30.json`.
- **Low not done:** L26 G1 spare row note, L27 S5 line giving away "a week has 7 days", L27 S1 empty cell, L28 "spare column" wording, L29 T1 teaching sentence, "bigger" in L40, Toolbox Card line for Book 8, Book 5 key sneak-peek questions, L21 E3 = home H1.

### DIAGRAM_FIXES (WAIT-DIAGRAMS): what is closed and what is not
Closed in this pass: L39 bracket, L9 snail, L4 G3 square block, L6 G1 number line labels, L35 pattern fills, 5-sun card, exit and home clocks (L21, L22), the enlargements listed under M6. Closed earlier (DIAGRAM_FIXES.md): picture graphs, balances, rulers, number lines (L6 S7, T3, G1/G2), L28 stick pictures, L35 labels, price tags, coins, groups.
Still open: L31 to L34 size pass (partly: only the figures listed under M6 were enlarged; the pages are full, so further enlargement needs items to move), L33 dot grids and L34 top views (only enlarged, not redrawn), L11 line-ups, L35 T3 tiles, L10 and L39 story-step card piles, L3 digit cards, the figure-less home sheets (about 85 items, no figure slot used beyond clocks), online-practice figures for L2, L3, L5, L10, L21 to L23. The books should not be called "diagram work closed" until the owner accepts these.

### L1-OWN-REPLACE: the five own-material overlaps, replaced
Each new item was hand-solved, the verify script rewritten, the key and home pack rebuilt, and checked against the holiday text (`hp/`: qbank.json, tutor guide, question bank, workbook HTML, 35 files, 153,505 words) and `extension/data/l1_u01..u10.json` for 6-word runs and shared 4-word frames.
1. **L40 Quest secret cave** (was Extension item 12, 5c, 10c, 15c Mon to Wed, Friday). Now Mi's bus fare: 20c on Day 1, 30c Day 2, 40c Day 3, 10c more each day. (a) Day 5 costs 60c. (b) It costs 80c on Day 7. One answer each. No 6-word run in the corpus.
2. **L40 G1** (was holiday "Two numbers add up to 12, one is 2 more": 5 and 7). Now two jars hold 12 shells, the blue jar 4 more than the red jar (table of every pair that makes 12, only 4 and 8 differ by 4). The beyond text and the online item c2 (now 16 shells, 6 more, red jar 5) changed with it. Frames with other numbers elsewhere in L40 (the child-in-another-class puzzle with 8 and 2, home H2 with 14 and 2, the G3 model puzzle) were not changed.
3. **L30 T3** (was Extension 3x3 logic, ball/kite/drum). Now Kumar, Lily and Wei and red, blue and green caps with three negative clues (Lily not red and not blue, Kumar not green, Wei not blue): Wei red, Kumar blue. One solution (brute force in the verify script). Extension has no 3x3 caps puzzle (names Kumar, Lily, Wei: 0 hits).
4. **L28 stick sequences** (was holiday 3, 5, 7 triangles and 4, 7, 10 squares, "up to 31"). Both rows now carry one handle stick: triangles 4, 6, 8, 10 (double the number, then add 2; always even) and squares 5, 8, 11, 14 (3 more each time). The whole lesson was re-authored on that frame: `stick_pattern` gets a `handle` option, all slides, script, tables, notes, Think harder (the odd and even idea became always even), Go further, Investigation (14 strips: 6 triangles or 4 squares use all 14), exit, home, online templates (new formulas) and L30's matching Mini-lesson example and Quest gate 5 (4, 6, 8, 10, 12; squares 5 to 26). Work-back items reworded to "Mi uses every stick" (the old "with none left over" frame is in the holiday item). Remaining overlap: bare number runs such as 5, 8, 11, 14 and 4, 6, 8, 10 also occur in the holiday as plain counting patterns (P1 "patterns 5, 8, 11, 14, what is the 10th number", Extension unit 4 "2, 5, 8, 11"), not as stick counts; owner may still want a different handle size.
5. **L36 home H4** (was "all the pairs that make 12", answer 6). Now Lily puts 8 marbles into a red and a blue cup, at least 1 in each, 7 ways.
The TERMCHECK private-source items for lessons 10, 21, 23, 24, 28 (S2 ratio table) and 36 (T2 outfits, home H2) are not touched.

### Not done or unsure
- M5 shrunk pages (above); M6 remainder; the DIAGRAM list; figure-less home sheets.
- L28 is a full lesson re-authoring (about 150 strings); the 6-word and frame check is clean, but the lesson has not had a read-through by a person, and the tutor guide timing was not re-measured (validate: unchanged structure, 0 FAIL).
- The L28 handle looks like one stick sticking out at the bottom left; check it on paper.


## 10. REWRITE-NOW (TERMCHECK too-close items) and Toolbox Card follow-through
**Rewrite (lessons 10, 21, 23, 24, 28, 36).** Closed and not closed per item: `audit/TERMCHECK.md` section 7. Summary: every TC item is replaced (L10 T2 and online t2; L21 mirror clock family; L23 E3, T3, G1, H4, online g1 and t3; L24 T3 and online t1; L28 S2 and, earlier, the stick sequences; L36 T2, H2, online c5 and, earlier, H4). Verify scripts, registries (class and workbook pair lists), spine and contest_moves, beyond items and tutor notes updated; validate 0 FAIL for all six lessons. The RV (review) items were not rewritten. Similarity method: my own re-implementation (7-word runs and content-word overlap) against docs/books/private_*, docs/sasmo/private_*, hp/ and extension/data/l1_*.json: no 7-word run for any new item.

**Toolbox Card follow-through (TOOLBOX_CARD_FIXES.md).**
- (a) "In my head" is now "No tool" in `tools/b_quest.py` (tool row, tutor notes and the grown-up note text), `l10.json`, `l20.json` (kit tool list and notes) and `l30.json`; the four Quest Log PDFs were rebuilt (checked: 9 "No tool" and 0 "In my head" in each). The lesson 20 kit page now says 7 tool cards (the six tools and No tool) and 8 problem cards, consistently (l20.json lines 58, 69, 3256, 3317; the old "6 tool cards and 6 problem cards" line was wrong). The cut-outs stay "tool cards"; the A5 card is "Toolbox Card" everywhere (lowercase variants fixed in l01, l10, l30, l39, l40).
- (b) The L20 and L30 notes "in the same words as the Toolbox Card" (Wait. Try a tool. Try a smaller case. Ask.) are now true: the card back carries exactly that routine. L01 tutor prep now says to keep the card open at the Look back side and how to send the soft copy (PRINT_BW, 100 percent, both sides, flip on the long edge).
- (c) Book 1 contents page uses the single name "Toolbox Card" (it already did).
- (d) Term 1: the Toolbox Card marks Spot the pattern, List every way, Draw it and Act it out with a small Term 1 tag. L01 and L10 tutor text and the Book 1 contents page now say so ("Four tools carry a small Term 1 tag: they are our four tools this term").
- Docs: `SPINE_TERM_DESIGN.md` 4.6, `docs/pedagogy/toolbox_card_notes.md` and `docs/pedagogy/spine_routine_spec.md` section 3 updated to the new card back.
- **levels/spine.json (one line, for the card owner):** `kit_line` changed from "Eight tools: see your Inquirer Kit card" to "Eight tools: see your Toolbox Card". It is read by `levels/spine_guide.js` and `levels/spine_deco.py` (holiday decks and guides, Lesson 1 only) at their next build; the card builder does not read it, so the card needs no rebuild for this.
- L19 hand-off line "Quest Log (3 pages ..." (second copy at l19.json ~3360) fixed to 4 pages.
