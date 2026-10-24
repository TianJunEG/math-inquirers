# Audit round 3: Level 1 term books 5 to 8 (lessons 21 to 40), independent, from the PDFs

Auditor: independent (not the builder, not the round 1 or round 2 auditor). Date 23 Oct 2026. Branch claude/great-fermi-1hv4vc, working tree clean at the start (HEAD 41f8af7). Nothing edited except this file; nothing pushed.
Files audited: `outputs/print/term/` (colour) and `outputs/print/bw/term/` (B&W), Workbook, AnswerKey_TUTOR and HomePack of Books 5 to 8 (24 PDFs), plus `outputs/kit/Math_Inquirers_Toolbox_Card_A_6-8_*` and the 20 tutor-guide PDFs `term/l1/out/l21..l40`. Page numbers are the printed page numbers (equal to PDF page index). Lessons are written "Term N Lesson M" as printed (Book 5 = Term 3 L1-5 = lessons 21-25, Book 6 = Term 3 L6-10 = 26-30, Book 7 = Term 4 L1-5 = 31-35, Book 8 = Term 4 L6-10 = 36-40).
Freshness check: all 24 PDFs (colour 22:58-22:59, B&W 23:00-23:06) are newer than every lesson JSON and tool file they depend on (latest JSON l21/l22 22:57:51, latest tool figs2.py 22:45); the lesson-level guides, workbooks and home sheets of the rewritten lessons are also newer than their JSON.

## 1. Verdict

| Book | Verdict |
|---|---|
| Book 5 (L21-25) | READY. No wrong answer. Mediums: exit-ticket clocks still small (22 to 25 mm), L21 G2/G3 part (b) gives away part (a). |
| Book 6 (L26-30) | READY. No wrong answer; the rewritten L28 is correct in every printed number. Mediums: "spare column" wording on L28 S2/S3, stale and absolute-number text in the tutor key (shared with Book 8). |
| Book 7 (L31-35) | READY with polish: draw boxes are very small after the M5 trimming (L32 G3, L35 G3), and the L33 T1/T2 route blanks are short. Isometric figures, hidden-cube counts and fold-and-punch all check out. |
| Book 8 (L36-40) | READY. No wrong answer; the five owner-replaced items (L36 H4, L30 T3, L40 cave, L40 G1, L28 sticks) are correct and unique. Mediums: tutor-key staleness (shared with Book 6) and the L40 G2/H2 frame that the owner replaced in G1. |

**No High.** No wrong printed answer, no workbook/key mismatch, no overflow past the text margin, no odd page count, no ink on any kit-page back, B&W content equals colour on all 8 books, page numbers clear of the footer. The Mediums are quick fixes except the similarity item (owner call).

## 2. What I did, and the counts

1. **Hand-solved every workbook question and every home item from the rendered pages** (text layer for wording and numbers, page images at 105 dpi for every figure, 220 to 400 dpi crops for every figure I could not read at page size). 308 workbook items (79/78/74/77 in Books 5/6/7/8: Start here, Think harder, Go further, exit tickets), the 20 investigations, all 100 home items, and all 8 gates plus secret cave of both Quest Logs (Book 6 pp41-44, Book 8 pp39-42). **Every printed answer in the keys and home answer sheets agrees with my own answer.** Method per figure type:
   - Clocks: read every clock of Books 5 and 6 (and the quest clock) from the picture, hour hand angle as well as minute hand (about 45 clocks, all agree with the key).
   - L28 stick pictures and tables (all of them): counted sticks in the S1 pictures (5, 8, 11), the T1 and T2 triangle pictures (3 triangles and a handle = 8 sticks; 4 triangles and a handle = 10 sticks, counted stick by stick at 400 dpi), every table row, the formulas (triangles 2n+2, squares 3n+2: 202, 302, 152, 22, 42, 32 sticks gives 15, 38 sticks gives 12, 14 strips give 6 triangles or 4 squares), the odd/even items, the wrong number in T3, the home H3/H4 pictures and the Quest gate 5.
   - Isometric cube items (L34 S1, S2, S3, S4, T1, G2, E1; L40 Quest gate 3): wrote my own ray-casting visibility check (viewer from front-right-above). Results match the key: S1 5 cubes, none hidden; S2 4 cubes, 3 visible, 1 hidden; S3 5 cubes, none hidden (view B); S4 6 cubes none hidden; T1 9 cubes, 7 visible 2 hidden; G2 8 cubes 7 visible 1 hidden; E1 4 cubes none hidden; Quest gate 3 6 cubes (5 visible, 1 hidden).
   - Counting by brute force: L24 ways to pay and fewest pieces; L23 plans (2 sets of jobs, any order); L26 T1, T2, G1 (6 ways, table has 7 rows), G2; L30 T3 caps (unique: Lily green, Wei red, Kumar blue); T4 (3 five-cent and 2 ten-cent); L33 routes (4, 6, grid 1 3 6 10, 3 x 2 = 6); L35 G1 shadow (only B is a rotation; A is the mirror image); L36 handshakes, squares in a 3 by 3 grid (14), flags (6), pairs summing 14 (3 pairs); L36 H2 (9), H4 (7 ways); L39 G1 to G3, T4; L40 G1 (only red 4, blue 8 differs by 4), cave (bus fare 60 and Day 7).
2. Figures read against text (answer given away? text and picture agree?) for all new, enlarged and home-sheet figures I looked at (about 120 workbook pages, 30 home and key pages, 14 kit pages).
3. M5 measured with PyMuPDF on every workbook page (section 4).
4. B&W against colour for all 8 books (24 pairs, section 6).
5. Similarity run (section 7). Timing tables of all 20 guides parsed (section 8).

## 3. Findings

### High
None.

### Medium

**M1. Tutor key, Book 6 and Book 8, Quest notes: stale "In my head".** Book 6 key p24 and Book 8 key p24 (Quest tutor notes, tool row paragraph) say "a child who circles In my head is telling you the truth". The Quest Logs and the keys' own tool row now say "No tool". RETROFIT_REPORT section 10(a) says the grown-up note text was converted; this sentence in the tutor notes was missed. Change to "No tool".

**M2. Tutor key, Book 6 and Book 8 (both pp30-31): absolute lesson numbers remain** in section 6 "Group advice for next term" and section 7 "The one line for the grown-up" ("Lessons 21 to 27", "Lessons 24 to 26", "Lesson 28", "Lesson 29", "Lessons 21 to 29" in Book 6; "Lessons 31 to 32", "33 to 34", "Lesson 36", "Lessons 37 to 40", "39 to 40" in Book 8). The books print "Term 3 Lesson 8". The wording in section 7 is copied into the note sent to a family ("Lessons 21 to 27. We looked at ..."), so a family will read lesson numbers that appear nowhere in their book. Round 2 M6 was reported fixed in RETROFIT section 9; the "Where it sits" line is fixed but these two tables are not. Use "Term 3, lessons 1 to 7" and so on.

**M3. M5 not met as stated: question text below 12.5 pt.** Measured (section 4): stems of Start here, Think harder and Go further are 13.1 pt (13.4 on a few pages), sub-part lines 12.7 pt, nothing is at 11.2 pt any more. But the **exit-ticket stems are 12.0 pt on all 20 lesson pages** (page 5 of every lesson, Book 5 pp7, 15, 23, 29, 39 and so on; they share the page with the Investigation and the look-back box), the **True/False statement cells are 11.3 pt** (10 tables: Book 5 p5; Book 6 pp5, 10, 18, 26; Book 7 pp5, 18, 26; Book 8 pp12, 19), and the italic hint line above the first question is 11.0 pt on about 30 pages. **Minimum question text: 11.3 pt (table cells); minimum stem: 12.0 pt (exit tickets).** If the rule is 12.5 pt for everything a child reads, 20 exit pages and 10 tables miss it; if the rule is for stems on the three tier pages, it is met.

**M4. Exit-ticket and draw clocks are still small (round 2 M5, partly fixed).** Measured face diameters: Start here clocks 33 to 39 mm; exit clocks 22 to 25 mm (Book 5 p7 E1 25 mm, E2 draw half past 5 23 mm; p15 E1 22 mm, E3 draw 9:25 22 mm; p23 E3 22 mm; S3 draw 3:20 on p11 26 mm; Book 6 p33 S1 24 mm, Quest gate 1 27 mm; home clocks 26 mm). They were 17 mm, so better, but the child still draws two hands with a ruler on a 22 mm face (E3 p15). The round 2 target was 35 to 40 mm.

**M5. Book 7, small draw and write space after the M5 trimming.**
- p18 L32 G3 "Draw a figure for a partner. It has exactly 2 triangles, 1 square and 1 rectangle": the box is about 15 mm high, but the kit pieces are 30 mm squares; no figure of four shapes fits at that size.
- p44 L35 G3 "Draw 4 tiles in a row": the box is about 12 mm high (tiles in the same book are 12 to 13 mm); the child cannot draw a row of 4 tiles with a different one.
- p27 L33 T1(a) and T2(a) "Write the other routes": one short blank of 65 mm (T1, three routes of four letters: about 14 characters plus spaces) and 86 mm (T2), no extra line. A 7-year-old will run out of line.
These are pages listed as "last writing line trimmed" in DIAGRAM_FIXES. Restore one line, or move the answer blank under the figure.

**M6. L28 S2 and S3 (Book 6 pp17-18): "The last column is spare" but the answer is in it.** S2 asks "Mei buys 5 rulers. How much do the 5 rulers cost?" and the table has columns 1 to 5, the fifth is "spare" (unlabelled blank). S3 (b) "7 squares need ___ sticks" and the table has columns 1 to 7, the seventh "spare". The answer can be written in the spare column. "Spare" is a hard word for age 6 and here it contradicts its use (round 2 L6, not done). Say "You may use the last column" or "Extra column".

**M7. L21 G2 and G3 (Book 5 p6), new "Hands Detective" items: part (b) gives away part (a).** G2: "(a) Is Ali right? Yes/No. (b) It is 20 minutes past ___" (the stem has already said "4 o'clock"; (b) tells the child the time is not 4 o'clock). G3: "(a) Is Lily right? ... (b) At half past 5 the short hand is half way between the 5 and the ___" (tells the child the short hand moved). The items are otherwise correct and unique (G1 25 minutes, G2 6:20, G3 No). Reword (b), or ask (b) first.

**M8. Similarity: the holiday "two numbers add up to N, one is K more than the other" frame remains in L40 G2 and home H2.** The owner replaced L40 G1 (holiday item add up to 12, 2 more). L40 G2 (Book 8 p36) is "Two numbers add up to 10. One number is 4 more than the other" and home H2 (Book 8 p11) "Two numbers add up to 14. One number is 2 more than the other"; same sentence frame as the holiday P1 item and the holiday question bank (hp/ qbank also holds "add up to 9 where one is 3 more than the other"). Different numbers. Not a copied item, but the same frame was the reason G1 was replaced. Owner call: keep as a frame with new numbers or reword ("A and B make 10 and A is 4 more").
Other outstanding frame overlaps (all RV items, not rewritten, listed so the owner can see them together): L36 T3 "A big square is made of 4 small squares, like the yellow one" (9-token run with the P1 catalogue and a private P4 record), L36 E2 "each box is one way to wear a hat and a scarf" (3 by 3 combinations, same family as a private P3 shirts-and-shorts question), L39 T3 "Siti is 4th from the front ... also 3rd from the back" (8-token run with the P1 catalogue), L23 G1/E3/H4 (backwards from an end time with 1 hour and half an hour; the family appears in a private school paper; different story, numbers and a third job). No 7-token run with any private source for any rewritten item (section 7).

### Low

L1. **L28 key T3 (Book 6 p12): stale "Watch for"**: "Choosing 5 because 16 comes after the wrong number." The table is 5, 8, 11, 13, 17, 20 and has no 16. Replace with "Choosing 5 because 17 comes after the wrong number" or delete.
L2. **L34 G2 key (Book 7 p16)**: "1 cube is hidden behind the front right tower". By ray-casting for the printed figure (back stacks 3 and 1, front stacks 2 and 2) the hidden cube is the bottom cube of the back-left stack (behind the front-left stack and the back-right stack). The answer 1 is right; the sentence is not.
L3. **L40 Quest gate 3 (Book 8 p40)**: "There are ___ cubes in all", answer 6, with one cube hidden (5 visible). "In all" is the only cue; L34 taught "you cannot see 1 cube". Add "Some cubes may be hidden."
L4. **Book 6 Quest gate 3 (p42)**: "The tags say $4, $5 and $6 in part c" is in the stem above the pictured tags $6 and $9; the tags for part (c) are not pictured. Answer (4 and 6) unique, wording hard to hold in mind. Show the three tags.
L5. **Tool-name chips on L30, L39, L40 are 6.1 pt** (Book 6 p33, Book 8 pp25, 33; page 1 of L36 to L38 and L31 to L35 have the single "Tool of the day" line). Present and correct (7 names on L30, 8 on L39/L40, same order and same icons as the Toolbox Card). Round 2 had 6.5 pt. Confirm on a printed proof. The look-back "Tool I used" row on every page 5 is icons only (no names) at about 6 mm per icon.
L6. **L33 S1 (Book 7 p25)**: the model grid and the empty grid are one lattice with a slightly larger gap (1.2 spacings) between them and no label or frame; a child may not see where to copy.
L7. **L35 stipple fills (Book 7 pp41-45, kit p47)**: much improved (identical shapes now show identical fills; tile pairs I checked, S1, S2, S6, E3, T1, are fair and the key is right). In the colour PDF the dots and hatch are a coarse bitmap pattern, blocky at 300 dpi and above (MuPDF render); in S6 the dot fill of tile A shows one more dot row than tile D (a rendering effect I could not confirm in another viewer; the key says A and D match). B&W is legible. Check on a printed proof. The 5-sun card: suns smaller, clear of the cut line, but the rays of neighbouring suns still touch (kit p47 row 1, card 4).
L8. **Home sheets still repeat the hand positions in words** (Book 5 pp3, 5: L21 H1 to H3, L22 H1, H2; round 2 L3, not done), so the 26 mm clock is not read. L21 E3 is still the same question as H1.
L9. **Duplicate home item**: L33 H5 (Book 7 p7) and L39 H5 (Book 8 p9) are the same question ("A cup hides some counters. The cup and 5 loose counters make 14 ...") with the same numbers.
L10. **Rounds-1-and-2 Lows still open**, unchanged: L26 G1 table has 7 rows for 5 ways still to find, no spare-row note (Book 6 p6); L27 S5 line above the question says "A week is 7 days" and (a) asks "A week has ___ days" (p10); L27 S1 table has an unlabelled eighth cell (p9); L29 T1 teaches inside the question ("That is a good first step", p27); "bigger" for numbers in L40 T3, E2 and H4; Book 5 key "Sneak-peek puzzles (not in the workbook)" prints answers only (pp5, 9, 13, 17, 21); contents page of every book still lists "tens bars, number lines" as kit examples; Book 6 p37 header still wraps to two lines; Book 5 kit p17 says the mat says "a.m. and p.m." while it says "am" and "pm"; L39 kit card 6 says "5 buns cost $15" while E3 says $20; no printed page in Books 5 to 8 tells families to keep the A5 Toolbox Card (the card itself, section 5, is consistent).
L11. **Small figures remain** (not enlarged because pages are full): L30 S1 clock 24 mm; Book 5 p37 T4 price tags about 14 mm with 8 pt prices; Book 5 home p9 H2 the $5 note is about 7 mm wide with a 3 pt "$5"; "PLAY MONEY" on every note is 3.3 pt (decorative); Book 6 Quest gate 5 triangle picture about 35 by 10 mm with 5 pt labels; Book 7 L35 E1 tiles about 12 mm.
L12. **Wording for age 6 to 8**: hard words that remain: "spare" (L28), "apart" (L40 G2 b), "difference" as a table column (L40 G1), "ringed" (L33), "cashier" (L25 E3), "Statement" (every True/False table), "exactly" (about 20 items), "fortnight" (defined in the stem, fine). L36 T3 "There are ___ big squares" gives no hint that every 2 by 2 square counts (answer 2 for the 3 by 2 figure); the yellow one is the example. L28 G3 "same number of pictures" for "same number of shapes".
L13. **L23 G1 number line (Book 5 p22)** has four boxes (2:15, 2:45, 3:15, 3:45) for two requested times; the 2:45 box in the middle of the painting arc is not asked. Harmless but a child may feel every box must be filled; say "Fill in the times you need".

### What is correct and was checked (no finding)
L21 T1 to T3 and G1 (7:15, 2:45; 8:30; false/true/true; 5 and 25); L21 G2 6:20 (clock drawn correctly, minute hand long and thin, hour hand short and thick); L22 T4 now says "A show is on until the next show starts" (fixed); L23 T3 Art 11:00 and Story time 12:00; L23 G1 3:45 and 2:15; L23 G2 12:30 and 1:00; L23 G3 3:30, 4:00, Mei; L23 E3 11:30; L24 T3 change 20c and rubber 30c; L28 S1 to E3 (all printed numbers right, section 2); L30 T3 and T4; L36 T2, H2, H4; L39 G1 bar model now to scale with the 36 bracket over the whole bar (round 2 M1 fixed; Jason 9, Jenny 27); L39 T1 key accepts Make a table (M10 fixed); L36 and L40 replaced items; Book 8 Quest headings "Gates 1 and 2 / 3 and 4 / 5, 6 and 7 / Gate 8 and the secret cave" and Book 6 headings match the gates on each page (M2 fixed); L34 G3 "0 is allowed" in the key (M9 fixed).

## 4. M5 measurement (PyMuPDF, colour workbooks, all 4 books)

Text size by role (points as printed, after the 0.943 content scale):
| Role | Size | Notes |
|---|---|---|
| Stem on Start here, Think harder, Go further | 13.1 (13.4 on a few pages, for example Book 5 pp13, 21, 37 and Book 6 pp19, 20) | no page below 13.1 |
| Sub-part lines (a), (b) | 12.7 | 397 lines, all 12.7 |
| Multiple-choice options | 13.1 | |
| Exit-ticket stems and sub-parts | 12.0 | all 20 lessons (M3) |
| True/False statement cells | 11.3 | 10 tables |
| Italic hint line under the page header | 11.0 to 12.0 | |
| Quest Log gate text | 13.9 | gate stems; "Mi says" box 12.4; page sub-heading 11.6; tool rows 7.9 |
| Tool-name chips | 6.1 | |
No page has question text at 11.2 pt (the old tight level). **Minimum question text 11.3 pt (table cells); minimum stem 12.0 pt (exit tickets).** Text edge scan: no word within 22 pt of the left or right edge on any page of the 12 colour PDFs.
Pages that dropped the last blank writing line (DIAGRAM_FIXES list for Books 5 to 8): I viewed those that carry free-writing, drawing or listing space. Room to write is adequate on L23 pp21-23 (all answers are inline blanks), L25 p37, L26 p5, L29 p27 (blanks inline, a work box where the question asks for it), L30 p35, L36 p36 G3 (2 lines), L40 p35 T1 (3 lines), Investigation boxes (4 lines each on every page 5). Not adequate: L32 G3, L35 G3, L33 T1(a) and T2(a), see M5.

## 5. Toolbox Card consistency (outputs/kit/Math_Inquirers_Toolbox_Card_A_6-8_PRINT_BW.pdf, text from the SCREEN colour copy)

- The card has 8 tools in the order Spot the pattern, List every way, Draw it, Make a table, Work backwards, Guess and check, Try something simpler, Act it out; Term 1 tags on 1, 2, 3 and 8. Back: Look back (3 questions, "Draw or write one word. Use a pencil.") and "When I am stuck: Wait. Try a tool. Try a smaller case. Ask."
- Book 5 to 7 page 1 "Tool of the day" lines carry the card's one-line descriptions verbatim (checked all eight). Book 8 chips L39 and L40 show all 8 names in the card's order with the card's icons (Try something simpler = square arrow grid). Book 6 L30 chip shows the 7 names (the card's tool 7 is not yet met in Term 3): consistent. The look-back box wording ("Pick one problem from today. There are no right answers. You can pass. Nobody reads it out." and the three questions) is identical to the card back.
- Quest Logs: tool row = tools met plus "No tool" (Book 6: 7 + No tool; Book 8: 8 + No tool), 9 "No tool" per Log; no "In my head" in any workbook page. Stale only in the keys (M1).
- Kit cards: L30 kit p39 has 7 tool cards, L39 kit p31 8 tool cards plus 8 problem cards (both match their captions).
- Naming: "Toolbox Card" for the A5 card, "tool cards" for the cut-outs, in all books. Book 5 to 8 pages do not mention the A5 card at all (L10 above).

## 6. B&W against colour and kit pages

- B&W files are newer than colour (23:00 to 23:06 against 22:58/22:59) for Books 1 to 8. Page counts equal. I compared all 24 pairs (every page, 100 dpi): global ink recall and precision per page, and a 20 px tile test (colour ink missing in B&W, or B&W black with no colour ink near). **Books 3 to 7 now match colour**: Workbooks, keys and home packs show no content difference. The only flagged tiles are dither tiles (stipple of kit pages, bag figures Book 8 p26) and one-tile footer-rule slivers on the keys (pp4, 12, 16, 20). Worst recall on any page 0.89 (kit pages that carry a light grid). Books 1 to 4 compared by the global test only: no difference.
- B&W has no text layer (unchanged); pages read by eye.
- 1-bit legibility viewed at 150 to 220 dpi: chips with tool names (legible, small), stipple tiles of L35 (A/B/D hatch against C dots distinguishable), the 12 pair cards (stripes versus dots distinguishable but fine), cube shading (top white, front hatch, right grey), coins, bar models with white number pills, clocks (legible; 22 mm faces tight for drawing).
- Kit pages (workbooks): Book 5 pp9, 17, 31, 33, 41; Book 6 pp15, 23, 31, 39; Book 7 pp9, 11, 13, 21, 23, 31, 39, 47; Book 8 pp9, 17, 31. Every one on an odd page, **backs pixel-blank in colour and B&W** (tested at 60 dpi: zero non-white pixels). Piece counts match captions where I counted: 16 coins, 13 notes, 12 tags (9 + 3 blank), 14 strips, 7 day cards, 8 mistake cards (4 right, 4 wrong: 45+28=63, 84-6=82, 53-20=73, 17+5=21 are wrong), 7 tool cards, 10 fold shapes (4 circles, 4 squares, 2 long rectangles), 9 pieces (6 squares and 3 rectangles of 2 squares), 11 pieces (6 triangles, 2 half circles, 2 quarter circles, 1 circle), 12 pair cards, 8 paper people, 16 tool and problem cards.
- Page counts even: workbooks 42/44/48/42, keys 22/32/22/32, home 12/14/12/14.
- Page numbers (round 2 L11): ink is now 5.3 to 5.6 mm from the bottom edge on every page of every file (colour and B&W), was 3.6 mm. The number is centred, the footer text sits at the left and right on a higher line: no collision on any of the 24 files (checked by word boxes on every page, and by eye on kit and Quest pages where the footer is lower).
- Contents pages: the page numbers equal the real first page of each lesson and of the Quest in all 12 files.

## 7. Similarity (own-material rule)

Method (my own implementation, not the TERMCHECK script): corpus of 55 files, 756,000 tokens: `docs/books/private_p1..p6_papers/*` (md, jsonl, txt, tsv), `docs/books/private_word_problems_notes.md`, `docs/sasmo/private_solution_notes_*`, `hp/` (qbank, qbank_skills, question bank, tutor guide, workbook html), `extension/data/l1_u01..u10.json`, the P1 to P6 catalogues and the word-problem drafts. Digits masked, 5-token runs; all workbook and home sentences of Books 5 to 8 (about 2,900 units) checked; chrome (look-back, kit and tool lines) ignored; hits needing 4 or more real words read by hand. Then keyword searches for each rewritten item (hands/clock moves, timetable and half-hour-before, give-back change, ruler and pen price tables, handle, caps, stripes, scoops, marbles in cups, bus fare, jars of shells).
Result: **no 7-token run with any private or holiday source for any rewritten or replaced item** (L21 Hands Detective, L23 T3/G1/E3/H4, L24 T3, L28 S2 and stick items, L30 T3 caps, L36 T2/H2/H4, L40 cave and G1). Longest shared runs are stock frames of 5 to 11 tokens ("Draw a picture or a bar of what the story says", "Ali buys a book for $9 and a pen for $6", "can exactly 21 sticks make", "Some are 5-cent coins and some are 10-cent coins", "Mei has 7 coins"), plus the frames in M8. The L28 plain number runs (5, 8, 11, 14 and 4, 6, 8, 10) appear in holiday units as plain counting patterns, not as stick counts (as RETROFIT says); owner may still prefer another handle size. The L23 work-backwards-from-an-end-time family is the same skill as a private school-paper time question (skill, not wording). Private text is not quoted here.

## 8. Timing (tutor guides L21 to L40, section 2 "Timing plan")

Parsed all 20 tables. Every plan is contiguous 0 to 90, with 11 segments, the row minutes sum to exactly 90, and the stated script total equals the sum of the row times within 2 seconds (rounding). Script need, quick class: 64:43 (L32) to 70:47 (L30); slow class (speech 10% slower, children and slide changes 20% slower): 76:36 (L32) to 83:21 (L30), always inside 90:00 with at least 6:39 buffer. L28 (rewritten): 68:41 quick, 81:20 slow, consistent with its neighbours (the number is unchanged from the table in the earlier audit's range; the rewrite did not move the total). L30 and L40 include the 20-minute Quest at minutes 35 to 55. Only the totals were checked, not the script word counts behind them.

## 9. Per-lesson table

"A" = every workbook item, exit item, investigation and home item hand-solved and equal to the key. HP = home pack.

| Lesson (Book, pages) | Answers | Figures | Findings |
|---|---|---|---|
| L21 Hands Detective (Book 5 pp3-9) | A | Clocks 33 to 39 mm (S, T, G), 22 to 25 mm (E1 to E3 and S3 draw) | M4, M7 (G2, G3). L8 (HP repeats hands). Old mirror clock gone. |
| L22 (pp11-17) | A | E1, E3 clocks 22 mm | M4. T4 sentence fixed. am/pm items rely on common sense (S5, E2 "afternoon"). |
| L23 (pp19-23) | A (Investigation: 2 sets of jobs, any order, key says so) | G1 number line, E3 clock 22 mm | M4, L13. All new items unique. |
| L24 (pp25-33) | A | coins and notes, T4 sets 7 to 10 mm | L11. T3 correct (20c, 30c). |
| L25 (pp35-41) | A | bar models to scale, tags | none |
| L26 (Book 6 pp3-7) | A | tags | L10 (G1 spare row). |
| L27 (pp9-15) | A | month page 1st = Wednesday used consistently (S5, T4, G2, E2, HP, Quest gate 4) | L10 (S1 empty cell, S5 gives away). |
| L28 (pp17-23) | A, every number checked (section 2) | S1, T1, T2 stick pictures and tables correct; handle drawn in line with the bottom stick | M6, L1, L12. No error found in the 150 strings I could read; no person has read it through (builder says so). |
| L29 (pp25-31) | A | clock S4, T4 | L10 (T1 teaches in the stem). |
| L30 (pp33-39) | A | chip with 7 names | L5, L11. T3 caps unique. |
| Quest Book 6 (pp41-44) | A (4:35 am 3:00 / 95 and $3 / ruler, $3, 4 and 6 / Monday and 10th / 10 and 12 / No, 87 / $15 / 3 five-cent and 1 ten-cent / 7 twos, or 2 fives and 2 twos, Yes) | clock 27 mm, gate 5 picture small | L4, L11, M1 (key). |
| L31 (Book 7 pp3-13) | A | shapes, 3 kit pages | none |
| L32 (pp15-23) | A (boat 2 triangles 2 squares; every triangle 8; staircase TFTF) | boat, house, tile cells | M5 (G3 box). |
| L33 (pp25-31) | A (4 right 1 up and so on; routes 4, 6; grid 4, 3, 6, 10) | dot grids now 2.6 mm dots, two-grid S1 | M5 (T1, T2 blanks), L6. |
| L34 (pp33-39) | A (cube counts by ray cast) | top views have labels and compass, correct | L2 (key sentence). |
| L35 (pp41-47) | A (S1 size, number, turn; S6 A and D; T1 C; T2 C; T3 circle, 10; G1 B; G2 D and B; E3 2) | fills fair, bitmap pattern | M5 (G3 box), L7. |
| L36 (Book 8 pp3-9) | A | grid, handshake, flag, squares | L12 (T3 "big squares"). M8 (E2, T3 overlap, RV). |
| L37 (pp11-17) | A (tallies 6, 8; 9, 5, 6; graph 3, 5, 8) | tray, tally, graphs | none |
| L38 (pp19-23) | A | graphs to scale, keys correct | none |
| L39 (pp25-31) | A | bar models to scale, chip with 8 names | L5. |
| L40 (pp33-37) | A (G1 4 and 8; G2 No, 2, 7 and 3; cave 60 and Day 7) | chip with 8 names | M8 (G2, H2 frame), L3 (Quest cubes), L12 ("apart"). |
| Quest Book 8 (pp39-42) | A (4, quarter, 9 / 3, 3 / 6, 2 / 2 and 3 / 7, 15 / 8, 6 / 22 / No, 8 / cave 60, Day 7) | cube stack, pentagon of 7 lines, graph | L3, M1 (key). |
| HP Books 5 to 8 (100 items) | A | home figures viewed on 14 sheets | L8, L9, L11. "Practice from earlier" tags point to the right lesson in all 20 sheets (checked against the titles of lessons 1 to 20). |

Cross-lesson pointers checked: "we use the clock again in Term 3 Lessons 2, 3 and 10" (clock is used in L22, L23 and L30 S1: correct); "the $1 coins are the tokens from Term 2 Lesson 9" (correct, Find One First has the tokens); play money and tags "come back in the next lesson and in the Quest" (L26 tags, Quest gate 2 coins, gate 3 tags: correct); kit lines for 14 strips and 7 tool cards match use; the L30 Quest gates match the lessons they review.

## 10. What I could not check

- No printed proof: real-size legibility of 6.1 pt tool names, 22 mm clocks, 3 pt note labels, toner density of the 1-bit stipple, and page numbers at 5.3 mm on a real printer are judged from renders. Only MuPDF was used to render; the L35 bitmap fills and the B&W dither could look different in Acrobat or a printer driver.
- B&W files have no text layer; I compared them to colour by pixels (tile test), so a changed digit in a region where both renders are dark would not be caught unless it moved ink; none was found.
- I read about 45 clocks and all hand-solved figure items at 105 dpi with zoom crops for the doubtful ones, not every one of the 80 clocks of Books 5 and 6 at high zoom (clocks on Quest and home sheets were read at page size).
- The L28 lesson (about 150 strings) was verified for numbers, pictures and key text; I did not judge tone beyond the printed workbook, key and home sheet. Slides, tutor-guide scripts (only the timing tables), parent summaries and online practice (the L28 and L36 online templates) were not audited.
- Similarity is against the files named in section 7 only; the original TERMCHECK scripts and any source outside the repository are not available. No private text is reproduced in this report.
- Decks, Books 1 to 4 content (compared to colour by B&W test only) and the A5 card beyond its text and layout were not audited.
