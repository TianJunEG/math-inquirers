# Round 3 independent audit: Level 4 Extension Workbook

Audited 23 Oct 2026, desk review, fresh session. Branch `claude/great-fermi-1hv4vc` at 5e74989. Report only: nothing in the book, data or tools was edited, nothing pushed. Files: `outputs/extension/L4/*Print_BW.pdf` (100 pp, 1-bit CCITT 600 ppi), `*_vector.pdf`, `*Soft_Copy_Colour.pdf`. Compared against the round-2 commit 117023b and against `p4/content/l1.js` to `l10.js` (all question, answer and workbook strings, about 1250 lines, read by sentence frame).

## Verdict

**Not yet sell-ready on content policy; sell-ready on maths and production.**

- Maths: all 32 changed items hand-solved from the printed page, 0 wrong answers, 0 unsolvable, every printed key and Why matches the page.
- Production: 100 pages in all three files, Contents has no repeated titles, certificate plaque is blank, contents and answer page numbers all correct, 1-bit pages legible, nothing changed outside the 32 listed items.
- **Open High (policy):** the owner policy was "new story AND new frame". **11 of the 27 replaced items still use the holiday frame** (some with the same numbers); a further 7 are borderline. The first drafts changed the story and numbers but kept the holiday structure. See table A. Either rewrite those 11, or the owner accepts "same type, new story" and the Welcome sentence ("with new numbers and stories") stays as it is (it is then true).
- Everything else is Low.

## A. The 27 replaced items: new story and new frame? (hand-solved, compared with holiday text)

Key: **OK** = new story and new frame. **Borderline** = new story, same basic frame (the skill itself forces it). **Too close** = same frame as a holiday item, only story or numbers changed.

| Item | Hand-solve vs key | Holiday item compared | Verdict |
|---|---|---|---|
| U1 S8 jogging every 12 and 18 days | 36 and 2 (36, 72; 108 is past 100) agrees | L1 Bus 33 every 10 and Bus 51 every 15, "every 30 minutes 5 times": LCM then count in a window | Borderline |
| U3 T2 number tower 5, ?, 11, top 52 | 18 agrees | none (L3 number chains are different) | **OK** (no figure drawn, see Lows) |
| U3 T3 Kumar 5 times Siti, 90 stickers, gives some, equal | 15 and 30 agrees | L3 "Ravi has 3 times as many stickers as Siti. Ravi gives 20 of his stickers to Siti, now the same": same characters pair, same object, same bar-model frame | **Too close** |
| U4 S11 jug 2 1/2 L, cups of 1/4 L | 10 and 1 agrees | L4 "9 scoops, each 1/4 cup, how many cups" (divide by a unit fraction) | OK (mild overlap only) |
| U4 T1 fraction equal to 2/3, top + bottom 35 | 14/21 agrees | L4 "I am a fraction equal to 3/4. My numerator and denominator add up to 28. Who am I?" | **Too close** (same frame; same device) |
| U4 T2 goals 2/5 and 1/4, other 21 | 60 agrees | L4 "1/4 are red and 1/3 are blue. The other 10 marbles are green. How many marbles?" | **Too close** (frame identical, story changed) |
| U4 T3 1/3 boys, 3/4 of girls glasses, 18 | 36 agrees | L4 "24 children, 3/8 wear glasses" (glasses reused, different task) | OK |
| U5 S9 two bags 8.8 kg, 3 times | 2.2 and 6.6 agrees | L5 money bar model; "3 times as" is in L3, not L5 | OK |
| U5 S10 4 books 2.8 kg, pencil case 0.35 | 0.7, 1.05, 2.45 agrees | L5 "box with 6 cans 2.85 kg, empty box 0.45, each can, box with 2 cans" | Borderline (share a total, add the container) |
| U5 G1 cat, dog, rabbit pair weighings | 2.4 agrees (cat 3.5, dog 5.8) | L5 "3 apples and 1 pear / 1 apple and 1 pear" differs | **OK** |
| U6 G1 four angles on a line, each 10 more | 30 and 60 agrees | L6 Go further "180 cut into three angles, multiples of 30" (different constraint) | OK |
| U6 G2 dancer 90 cw then 45 acw, pairs | 8 and SW (21 = 2 x 8 + 5) agrees | L6 "A robot faces N. It turns 45 clockwise again and again. After how many turns does it first face N again? Which way after 30 turns?" | **Too close** (same two questions; only the repeated unit changed) |
| U6 G3 pizza slices 1, 2, 3, 3 parts of 360 | 40 and 120 agrees | L6 "corner of a square cut into 3 angles, middle twice the smallest, biggest 3 times" (same ratio-parts frame; pizza word is from L4 fractions) | Borderline |
| U7 S6 lawn 16 by 10, square pond 4 | 144 and 68 agrees; figure to scale | L7 "path round a lawn", "garden with two paths, area NOT path" (region minus hole) | Borderline |
| U7 T1 perimeter 42, length 5 more | 104 agrees (13 by 8) | L7 "area 40 and perimeter 26, find sides" (different) | **OK** |
| U7 T2 rectangles of area 36 cm2, how many, greatest perimeter | 5 and 74 agrees | L1 "36 tiles: 5 rectangles 1x36 ... 6x6"; L7 "Which rectangle with area 36 has the smallest perimeter?"; L7 "list every rectangle with area 30, smallest perimeter" | **Too close** (same 36, same count 5, same list task) |
| U7 T3 tray 15 by 9, 3 cm square cut from each of 4 corners | 99 and 48 agrees | L7 "A 3 cm by 3 cm square is cut from each of the four corners of a 12 cm by 8 cm rectangle. Find the area and the perimeter of the shape that is left" (answer 60 and 40, perimeter unchanged) | **Too close** (same 3 cm squares, same two parts, same trick) |
| U7 G3 two overlapping 6 cm squares | 68 and 40 agrees; figure to scale | L6 two overlapping squares is about angles | **OK** |
| U8 T2 Ravi, 3 dice faces at a corner, product 36 | 2,3,6 and 1,4,5 agrees (only 6x2x3) | L8 "Mei looks at a dice from a corner, so she sees 3 faces. They add up to 12. Which three numbers can she see?" | **Too close** (same set-up, same one-from-each-pair reasoning, sum changed to product, hidden numbers added) |
| U8 T3 3 by 3 grid, 4 squares, diagonal fold | 12 (3 + 9) agrees; figure correct | L8 shading squares for symmetry is open-answer, not a count | OK (see D) |
| U9 S4 stickers, two lines, Kumar +10, Aisha +5 | 50, 5, 10, 80 agrees | L9 Q3 money-box graph: Ali +10 a week, Mei +5 a week, Mei dashed with square points, lines meet, "saves each week", "same amount in week" | **Too close** (same figure design, same rates, same questions) |
| U9 S5 tank table, minute 2 = 31, minute 5 = 55 | 8 and 87 agrees | L9 Q4 "Siti reads more pages each day, always the same number more. Fill in the table": Day 1 to 5, row `_, 14, _, _, 26` | **Too close** (same 5-column table, same blanks, same rule) |
| U10 S2 50 L tank, 3 L bucket, 8 L can, at least 1 each | 2 ways, 6 and 4 agrees | L10 take-home "$4 pens and $7 notebooks for exactly $50. Find ALL the ways" (answer 2 ways) | **Too close** (same total 50, same answer count 2, same working row idea; this was the round-2 clone and only the nouns changed) |
| U10 S3 17 tickets at $6 and $10, $134 | 102, 32, 8 agrees | L10 bicycles/tricycles, spiders/ants, 10c and 50c coins: "suppose all the same, swap" | Borderline |
| U10 S4 13 rice bags 3 kg and 5 kg, 49 kg | 5 and 8 agrees | same L10 family | Borderline |
| U10 S5 magic pot x3, -8, /2 gives 20 | 16 agrees | L10 "half, then $4, left $11"; "double, add 7, get 43" (work backwards) | Borderline (and S6 on the same page is the same frame, see C) |
| U10 S12 2 digits differ by 4, multiple of 7 | 84 agrees (only one) | L10 "I am a multiple of 7 between 50 and 80, digits add up to 11. Who am I?" and "2-digit, digits add to 11, swap is 27 more" | **Too close** (same "Who am I", same multiple of 7, same digit clue device) |

Totals: **OK 9, Borderline 7, Too close 11.** The 11 to rewrite first, worst first: U7 T3, U7 T2, U10 S2, U9 S4, U9 S5, U4 T1, U10 S12, U6 G2, U8 T2, U3 T3, U4 T2.

Suggested new frames (not done, for the writer): U7 T3 an L-shaped room with a corner stool (cut-out, perimeter question); U7 T2 "same perimeter, which has the bigger area"; U10 S2 a "how many different totals can you make" coin or stamp question; U9 S4 a bar or two-table comparison instead of two rising lines; U9 S5 a table with a rule given as words ("each row is 4 more than the one above") and ask for a missing middle value; U4 T1 compare two fractions by missing numerator; U10 S12 a code or lock puzzle; U6 G2 a clock or compass with an unknown turn; U8 T2 a net with numbers and a sum on a face; U3 T3 a money transfer between two jars with a difference given; U4 T2 a time-based fraction ("of the day").

## B. The two named Why fixes

| Item | Result |
|---|---|
| U2 G1(c) Why (p83) | Done. "1445 becomes 1450, 1500, 2000, but in one go it is 1000. No 4-digit number below 1445 does this." Checked: 1444 gives 1440, 1400, 1000 (same), nothing in 1000 to 1444 reaches 1500 at the second step; answer 1445 correct. |
| U10 S7 Why (p99) | Done. "A rabbit hops, so Mei does not have the rabbit." Logic: Ali dog, Ben fish, Mei not rabbit so cat, Siti rabbit. Correct. |

## C. The Lows

| Low | Status |
|---|---|
| U1 S8(b) wording | **Done.** p8: "In the next 100 days, they jog together [ ] times." Clear. (Item itself: see table A.) |
| "-180" stub on the p42 protractor | **Done.** Viewed at 300 dpi: the baseline numbers (180, 0 left and 180, 0 right) sit under the baseline, nothing runs through them. The Learn it protractor (p41) is also clean. The 52 degree key still reads correctly (inner scale from the left arm). |
| U9 C1 value on a line (70) | **Done.** p68: "Each line is worth 10", Wednesday dot is on the 70 gridline, 70 is the key. Legible at 300 dpi. |
| Wrapped boxes U2 C1, U7 S6, U10 T2 | **Done.** p19 three wide boxes on one row; p50 (a) and (b) boxes clear; p73 five boxes on one row, last one wide. |
| Hints | **Done** where changed: U10 T2 "Join the clues into 2 groups. Which group can go last?" fits; U7 T1 "Length + width is half of the perimeter." fits; U7 T3, U6 G1 to G3, U4 T1 to T3, U3 T2 and T3, U5 G1 hints all match the new items. |
| Contents titles repeated | **Done** (see E). |

New Lows found this round (none blocks sale):
1. **U3 T2** (p24) describes a three-level number tower in words only; a small drawn tower would remove the guess about the layout.
2. **U9 S4** (p64): the two series are drawn offset left and right of each week tick, so "the 2 lines meet at 80" is read as equal height, not a visible crossing; the page does not say what one gridline is worth (labels every 20, gridlines every 10; the C1 item does say it). Add "Each line is worth 10."
3. **U8 T3** (p59): text says "dotted diagonal"; the drawing is dashed. Say "dashed".
4. **U10** now has five two-kinds-of-thing items in one unit (S2, S3, S4, S10, T1, plus G2 and C1 coin and bike puzzles) and S5 is the same work-backwards frame as S6 on the same page. It is the Puzzle Day unit, so type repetition is expected, but S2 to S4 in a row is a lot.
5. **U5 S10** (p37) and **U6 G1** (p46) have no working row. Both are short mental or one-line items, and the cards still have blank space below the answer boxes, so the child can write there; U5 S9 has the bar model as scaffolding. Acceptable; add one line to U6 G1 if space on p46 allows (it is full).
6. **U7 p52** working rows: T1 three lines, T2 three lines, T3 two lines (for two parts). Enough room.
7. **U5 p37**: the card for S9 to S12 is full, but every item has either a model, a working row or space. OK.

## D. U8 T3 diagonal grid figure (p59)

Correct and clear. A 3 by 3 grid with a dashed diagonal from top-left to bottom-right corner running exactly through the three diagonal squares, extending slightly past the corners. Counting: 3 squares lie on the diagonal and 3 pairs mirror across it. 4 shaded squares = 2 pairs (3 ways) or 1 pair plus 2 diagonal squares (3 x 3 = 9) = 12. Matches key and hint ("Squares on the diagonal match themselves. The others come in pairs."). The check script's new `'d'` axis in `figs_l4_core.py` draws the line corner to corner. The hint and key are consistent with the picture.

## E. Contents, plaque, page numbers

- **Contents (p4):** each unit title appears once with "follows Holiday Program Lesson N · answers on page X" and the start page. No duplicates. Layout clean.
- **Certificate (p77):** plaque on the trophy base is blank, nothing garbled; name line, date and signature lines present.
- **Page count:** print 100, vector 100, colour 100 (all A4); print file is 100 images, gray, 1 bit, CCITT.
- **Page numbers checked against the pages:** About 2, Welcome 3, Contents 4, Pace plan 5, Units start 6, 13, 20, 27, 34, 41, 48, 55, 62, 69 (all match), Progress 76, Certificate 77, p78 blank, Answers divider 79, answers start 80, 82, 84, 86, 88, 90, 92, 94, 96, 98 (all match the "answers on page" lines). The "page N" reference printed beside every answer matches the question page (spot-checked 40 changed and unchanged entries).
- **Colour edition:** word-for-word equal to print on all 100 pages except the two intended differences (p2 "printed book / soft copy", p3 print note).
- Still open for the coordinator: the line "DRAFT licence text, for owner and lawyer approval. Not final." is on p2 in both editions.

## F. 1-bit legibility of changed pages

Viewed pages 4, 8, 18, 19, 24, 29, 31, 37, 39, 41, 42, 46, 50, 52, 53, 59, 64, 68, 70 to 73, 77 at 100 dpi and the figures on 42, 53, 59, 64 and 68 at 300 dpi from the 1-bit CCITT image. All text, hatching, markers (circle against square, solid against dashed), dotted gridlines, the protractor scales, the grid and the overlapping squares are crisp. No grey, no clipping. The graph legend on p64 reads (solid line with circle, dashed line with square).

## G. Nothing else changed unexpectedly (diff 117023b to HEAD)

Data files: only these 32 items differ; no ids added, removed or reordered; no unit-level field (title, learn, goal) changed.

| Unit | Item ids changed | Fields | Reason |
|---|---|---|---|
| 1 | S08 | text, parts, space, explanation | clone replaced + Low |
| 2 | G01 | explanation | Why fix |
| 2 | C01 | text | wide-box wrap |
| 3 | T02, T03 | text, hint, answer/parts, explanation | clones replaced |
| 4 | S11, T01, T02, T03 | text, parts or answer, hint, explanation | clones replaced |
| 5 | S09, S10, G01 | text, figure (S09), parts or answer, space (S10), hint, explanation | clones replaced |
| 6 | G01, G02, G03 | text, parts, hint, space (G01), explanation | clones replaced |
| 7 | S06, T01, T02, T03, G03 | text, figure, parts or answer, hint, space, explanation | clones replaced (T01 hint replaced too) |
| 8 | T02, T03 | text, parts or answer, hint, figure (T03 new diagonal axis), explanation | clones replaced |
| 9 | S04, S05, C01 | text, figure, parts, explanation; C01 answer 70 and figure | clones replaced + Low |
| 10 | S02, S03, S04, S05, S12 | text, parts or answer, figure (S05), space, hint, explanation | clones replaced |
| 10 | S07 | explanation | Why fix |
| 10 | T02 | hint, parts | wrap + hint fix |

Count: 27 clone replacements as announced + U2 G01, U2 C01, U9 C01, U10 S07, U10 T02 = 32. Other changed files: `extension/tools/figs_l4_core.py` (+`'d'` diagonal axis, used by U8 T3 only), `figs_l4_geom.py` (protractor baseline numerals dropped 20 units under the baseline), `extension/l4/src/trims.py` (answer-page Why lines for the changed items), the `src/uNN.py` and `verify/l4_uNN_checks.py` for the same items, README (424 answers), PROGRESS, AUDIT_ROUND2 (Fixes section), `build_report.json`, and the three L4 PDFs; the shared template change (no repeated titles on Contents, blank plaque, `extension/tools/build.py`, `extension/assets/mi_trophy_clean*.png`) also touches other levels' files and build reports and was not reviewed here beyond L4 pages 4 and 77. Text diff of the rebuilt vector PDF against round 2: only pages 4, 8, 19, 24, 30, 31, 37, 39, 41, 42, 46, 50, 52, 53, 59, 64, 70 to 73 and answer pages 80, 83, 85, 87 to 100 differ, which is exactly the changed items plus the shifted answer flow. I did not re-run `run_checks.py`, `dup_check.py` or `wording_lint.py`.

## H. Done / not done summary

| Request | Done? |
|---|---|
| 1 Each of the 27 is a new story AND frame | **Not done: 11 too close, 7 borderline, 9 OK** (table A). Stories are all new; frames mostly not. |
| 1 Hand-solve each and compare with key | Done: 27 of 27 agree. |
| 2 U2 G1(c) Why (1445) | Done |
| 2 U10 S7 rabbit reason | Done |
| 3 U1 S8(b) | Done |
| 3 "-180" stub p42 | Done |
| 3 U9 C1 value on a line | Done |
| 3 wrapped boxes U2 C1, U7 S6, U10 T2 | Done |
| 3 hints | Done |
| 4 Working rows U5 p37, U6 p46, U7 p52 | Done with notes: U5 S10 and U6 G1 have no working row but have free space; U7 p52 fine |
| 5 U8 T3 diagonal grid correct and clear | Done (minor wording: dashed, not dotted) |
| 6 Contents, plaque, 100 pages, page numbers | Done (DRAFT licence line still present, a known open item) |
| 7 1-bit legibility | Done |
| 8 No unexpected changes | Done, all 32 items listed |

## Before sale, in order

1. Decide the policy. If "new story and new frame" stands, rewrite the 11 Too-close items (worst first: U7 T3, U7 T2, U10 S2, U9 S4, U9 S5, U4 T1, U10 S12, U6 G2, U8 T2, U3 T3, U4 T2), then re-solve, re-run the checks and rebuild. If "new story, same skill type" is the policy, the book can go and nothing else here blocks it.
2. The small Lows (U3 T2 drawing, U9 S4 "each line is worth 10", "dashed").
3. Remove the DRAFT licence line when the owner and lawyer approve the text.
4. Child trial for pace, reading load of the Learn it pages, Unit 6 with a protractor.

## Fixes made after round 3 (23 Oct)

Eleven "too close" items rewritten with a new frame as well as a new story (compared by hand with `p4/content/l*.js`): U3 T3 (two jars: total and difference, then equalise: 27 and 15), U4 T1 (least and greatest n with 1/2 < n/9 < 5/6: 5 and 7), U4 T2 (fractions of a 24-hour day: 5 hours), U6 G2 (Ferris wheel with 12 seats: 7, 150, 10), U7 T2 (three squares from their areas, perimeter of the row: 26, with figure), U7 T3 (two 8 by 3 rectangles joined two ways: 28 and 38), U8 T2 (top and bottom faces of dice add to 7: 5, 9, 14), U9 S4 (journey graph with a rest: 40, 1, 5, 30; "each line is worth 10 km"), U9 S5 (rows of seats, rule in words: 35 and 70), U10 S2 (totals from 5¢, 10¢, 50¢ coins: 7 and 3), U10 S12 (lock code: 603). Lows: U3 T2 has a drawn number tower, U8 T3 says "dashed", U10 S6 is now a film-session time puzzle (S5 keeps the magic pot), working rows added to U5 S10 and U6 G1. The seven borderline items were left. Every new answer is recomputed in `verify/l4_uNN_checks.py` (425 answers, 0 mismatches); 100 pages.
