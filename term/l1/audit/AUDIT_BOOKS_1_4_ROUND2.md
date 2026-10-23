# Independent audit, round 2: Level 1 term books 1-4 (lessons 1-20)

Date 23 Oct 2026, branch claude/great-fermi-1hv4vc. Audit only: nothing edited except this file, nothing pushed, no PR.
Audited: the 12 colour PDFs in `outputs/print/term/` (Book 1-4 workbook, key, home pack) and the 12 B&W PDFs in `outputs/print/bw/term/`; loose Toolbox Card A (`outputs/kit/..._Toolbox_Card_A_6-8_PRINT_BW.pdf` and the SCREEN colour file); L10 tutor guide PDF for timing. Context read: AUDIT_BOOKS_1_4.md, RETROFIT_REPORT.md (sections 8-10), DIAGRAM_FIXES.md, TOOLBOX_CARD_AUDIT.md / _FIXES.md, TERMCHECK.md (sections 1-3, 7), owner_decisions.md (grep).

Method in short: text of all 24 PDFs extracted (pdftotext) and read; every lesson page of the four colour workbooks and the five content sheets of each home pack rendered and looked at (90-105 dpi, zooms at 250-600 dpi where a figure carried information); font sizes measured on every workbook page with PyMuPDF; B&W compared to colour page by page and zoomed at 600 dpi 1-bit; similarity run with my own 5- and 6-word run test against `hp/` (qbank.json, tutor guide, workbook html, gaps.json), `extension/data/l1_u01-u10.json`, `docs/books/private_p1..p6_papers`, `private_word_problems_notes.md`, `docs/sasmo/private_*` (47 files, 5.4 MB).

## Verdict

**Not print-ready yet; close.** Every workbook question, home item and Quest gate in Books 1-4 was solved by hand from the rendered page and agrees with the key: **no wrong answer, no wrong figure found** (all four H1-M7 items of round 1 that touched answers or figures are fixed: Quest "4 pages", snail, L4 G3 block, L6 G1 labels, L9 key $4, "Such means the same kind"). Page counts are even (46/44/46/46, 22/32/22/30, 12/14/12/14), contents page numbers are right in all 12 books, kit pages sit on fronts with blank backs, B&W equals colour page for page.

What stops a clean release:
- **1 High:** the M5 text-size fix removed the answer space of two questions (Book 1 p23, T3 and T4).
- **Mediums:** the M5 claim "nothing below 12.5 pt" is not true as stated (exit tickets are 12.0 pt, statement tables 11.3, instruction lines 11.0, chips 6.1); stale "In my head" survives in the Quest Tutor Notes of Keys 2 and 4; home-sheet intro text collides with the first question tab on 9 sheets; one home figure gives its answer; four pages ask for a written reason with no space; several new/rewritten items are same-frame twins of own-material or private items (original-only rule).

## Highs

**H1. Book 1 p23 (Lesson 3, Think harder): T3 and T4 have no place to write.** T3 asks "Write all the numbers that fit" (answer 51, 53, 71, 73, 75) and T4 "Write all the two-digit numbers you can make" (six numbers); the boxes hold only the digit cards (and "There are ___ numbers" for T4). There is not one writing line or blank for the list. The page is a "trim the last writing line" page (RETROFIT/DIAGRAM_FIXES list: "L3 p3"); the trim took the lines from T1-T4 and the intro drops to 11.0 pt. A child cannot show the answer the key expects. Fix: give T3 and T4 a line or blank each (move the "how you know" lines out, or move T4 to Go further).

## Mediums

**M1. "In my head" is still in the Quest Tutor Notes of Key 2 (p24, "The tool row and the I checked tick") and Key 4 ("...a child who circles In my head is telling you the truth").** Source `term/l1/tools/b_quest.py` line 226. The Quest Logs themselves now say "No tool" (checked: Book 2 and Book 4 workbook text 0 "In my head"), but the keys were not covered by the CARD-FIX follow-through. Change to "No tool" and rebuild Keys 2 and 4 (colour and B&W).

**M2. The M5 claim "no question font below 12.5 pt" is wrong as worded. Measured on all 182 workbook pages (colour PDFs; B&W is raster, but it is page-identical to colour):**
- Main question lines: **13.1 pt** on every lesson page (13.4 on part labels). Nothing at 11.2 pt any more: M5 itself is fixed (cf. 10.6/11.2 in round 1).
- **Exit-ticket questions (E1-E3): 12.0 pt on all 20 lessons** (pages 7, 15, 23, 33/35 etc.). Below 12.5.
- True/False statement tables ("Wei is 3rd.", "5 x 4 = 20", "Kumar has 3 + 4 = 7 apples.") and "Jumps of 5"/"Groups" table cells: **11.3 pt** (B3 pp 3, 21, 30, 39; B4 pp 4, 13).
- The italic page-instruction line ("Use counters or draw a picture to help. Choose any question...") drops to **11.0 pt** on the tightened pages: B1 p23; B2 pp 5, 19, 21, 33, 35; B3 pp 22, 37, 39; B4 pp 13, 37.
- Quest Log intro box 12.4 pt; Quest "Tool I used" row **9.0 pt (Book 2) and 7.9 pt (Book 4, eight names, "I checked" wraps to a second line)**; Quest gate questions 13.9 pt.
- Small figure text: balance tile labels "9 red", "6 blue" **7.0 pt** (B2 p20, L8 S6); L10/L20 tool-name chips **6.1 pt** (report says 6.5; B2 p33, B4 p35); look-back box 8.5 pt.
- **Minimum of the main question text: 13.1 pt. Minimum of anything a child must read to answer: 11.0 pt (instruction lines), 11.3 pt (statement tables), 12.0 pt (exit tickets).** If the owner's rule is 12.5, exit tickets and statements need a size bump (exit tickets have room on every look-back page: E1-E3 are short).

**M3. Pages that dropped the last writing line, judged for room to write** (list from DIAGRAM_FIXES, Books 1-4 pages: B1 p23; B2 pp 5, 19, 21, 33, 35; B3 pp 22, 37, 39; B4 pp 13, 37):
- Enough room: B2 pp 19, 33 (answers are blanks and a draw box), B3 pp 22, 37, 39 (G2 box, tables, draw boxes), B2 p35 and B4 p13 for the numeric answers.
- **Not enough where the page itself asks for writing:** B1 p23 (H1). B2 p5 (L6 Think harder): intro says "write how you know", T1/T2 have only the calculation blanks. B2 p21 (L8 Think harder): intro says "write how you know"; T1 (b) is "I know because ____" with a 20 mm blank, T2-T4 no line, and the page has about 20 mm unused at the foot (page fit looks too tight for the free space). B4 p37 (L20 Think harder): the page says "Say why you chose it" but there is no line for the reason; T1 (c) only circles Table/Strip. B4 p13 (L17): none for T-items. A 6-8 year old would answer the numbers; the "write how you know" habit (a spine goal) is not supported on these pages.

**M4. Home-pack intro paragraph collides with the first question tab ("No.1") on 12 of the 20 sheets**: last line of the grey intro text is cut by the tab: B1 pp 5 and 7 (L2, L3); B2 pp 3, 5, 7, 9, 11 (all five); B3 pp 5, 9, 11 (L2, L4, L5; the L1 and L3 sheets clear it); B4 pp 5 and 7 (L7, L8). Clear: B1 pp 3, 9, 11; B3 pp 3, 7; B4 pp 3, 9, 11. Zoomed at 170-250 dpi: the tab covers the descenders and on B1 p5 the words "they show what to try next". Shared home layout: the intro is 5 lines and the question box starts at a fixed height. Same fix for all.

**M5. Book 1 home p9 (Lesson 4, No.2): the mini-grid gives the answer.** It shows 47 48 49 / 57 (58, ringed) 59 / 67 **?** 69, and the question is "a counter is on 58, it moves down 1 row, which number is it on?" The neighbours 67 and 69 give 68 away. The figure also sits above the "Start here" tag, not beside the text like the others. Fix: leave the cell blank without neighbours, or drop the figure.

**M6. Similarity, original-only rule (frames, not identical items; no 7-word run anywhere):**
- **Book 2 L10 T2 (red book on a shelf, 5 on the left, 3 on the right, 9 books) is the TERMCHECK queue frame re-skinned**, with the same two counts as the Quest secret cave of the same book (Ali, 5 in front, 3 behind, 9 children), so two items in Book 2 are one item. The source frame: private "Devi is in the 4th position in the queue ... 5 people behind her. How many people are there in the queue?", SASMO "16 pupils in front of Jimmy and 5 classmates behind him", hp "Ben is 4th in a queue. There are 3 children behind him. How many children are in it?", extension l1_u05 "Kumar is 6th in a queue. There are 2 children behind him. How many children are there in the queue altogether?" TERMCHECK section 7 itself says the Quest secret cave keeps the queue frame (RV, deferred). My view: T2 is the same structure with a scenario change, so the TC verdict is only half closed.
- **Book 3 L1 T1 and home H4** ("Mei is 5th from the front and 5th from the back ... how many children?", "Jenny is 4th from the front and 4th from the back") are the hp qbank item "Zoe is 6th from the front of a queue and 6th from the back. How many children are in the queue?" with other numbers. Home H5 ("Ali is in the middle ... Ben") repeats names and opener of hp "Five children stand in a line. Ali is in the middle. Ben is just in front of Ali" (round 1 M9, unchanged). Book 3 S5/E2 ("Mei is 5th from the front in a line of 6") match extension l1_u05 "Aisha stands 5th from the front in a line of 12".
- **Book 3 L2 T2** "Ali has 30 stickers. Mei has 18 stickers. Ali gives some stickers to Mei. Then they have the same number." = extension l1_u02 "Ali has 16 stickers. Mei has 8 stickers. Ali gives some of his stickers to Mei. Now each child has an equal number of stickers." (same two names, same sentence frame, other numbers).
- **Retrofit items:** Book 2 L7 T5 (Kumar had some plums, gave away 23, now 45, at first?) and L10 T5 (Lily had some badges, gave 8, aunt gave 5, now 20, "go backwards ... at first") use the frame of extension "Ben had some marbles. He gave 5 to Mei, then won 3. Now he has 12. How many did he start with?" and "Ben had some stickers. He gave away 6, got 4 ... how many did he have at first?" (give/get, now, find the start; L10 T5 has the same two-step structure). Common stock family, no long run, but not "no similar item". Book 2 home L10 H4 "Ben has 9 sweets. He has 4 fewer than Kumar" repeats extension l1_u05 "Ben has 9 sweets. He has 6 fewer than Jenny." (same opener, new question). Book 3 L3 S1 and home L3 H2 open "A cup hides some counters" as extension l1_u05 does.
- Not changed since round 1 and still RV in TERMCHECK: Book 3 home L5 H5 (tricycle 3 wheels; private "A tricycle has 3 wheels") and L5 G1 wheels, Book 4 L10 T1 saving $3 a week.
- Checked clean (no run of 5 with any corpus beyond spine chrome): Book 2 L8 T5 (6, 9, 15), Book 3 L5 T3 (apples true/false), Book 4 L7 T4 (16 marbles true/false), L7 T1 (19 sweets groups of 4, part c), L10 snail, L10 story-step items except as above. Shared chrome strings ("Pick one problem from today. There are no right answers. You can pass. Nobody reads it out.", tool definitions) also occur in the holiday P1 workbook/tutor guide: that is the spine wording, fine.

**M7. Timing, L10 slow class 86:52: plausible overall, two soft spots.** Totals check (73:46 quick, 86:52 slow, 3:08 left). Dividing the slow total by the quick total (1.178) per part: Quest 17:14 to about 20:18 (window 20:00), Workbook 21:16 to 25:05 (window 24:00), Look-back 1:53 to 2:13 (window 2:00); these overruns (1:36 in all) are covered by unused time in earlier parts (about 1:51 before the Quest) and in the flex block, so it holds, but the Quest ("never shorten") and Workbook have no margin of their own. The trim cut Explore child time to 45-50 s per round (acting out a two-step story with counters, ages 6-8, online), while the guide's slide notes for the same rounds still say "Round 1, about 3 minutes" (script itself runs about 1:38). The tutor sees two numbers; the first trial lesson should time Explore. The exit-ticket heading "Exit ticket (minutes 35 to 55)" in the guide is stale (the exit is not done live).

## Lows

- B3 L3 Think harder and Go further use "x" ("x means groups of", "circle x circle = 25") two lessons before Equal Groups (round 1, unchanged; stated in-page).
- B4 L7 G1 (c): three dashed answer lines of different lengths (round 1 Low, unchanged, p14).
- B2 Quest p44 and B4 Quest p46 (secret cave): the label "because" in front of "I chose it because ____" reads "because I chose it because" (doubled word).
- B4 Quest Yes/No are pill buttons on gates 2, 7 and the cave, plain words everywhere else in the book.
- Keys: B4 key still says "the page generator draws only a few figure types" (round 1 Low); B2 key says "Quest v2: under every gate ..." (developer wording, tutor only); B4 key group-advice sheet names "Lessons 11 to 13", "Lessons 14 to 19" (absolute numbers) while the gate table and the rest use "Term 2 Lesson N"; B2 uses "Lessons 1 to 4" in-term. Tutor-only. Key 2 p32 is a blank page (padding to even count), p25 holds six bullets only.
- Wording: B4 L9 "Such means the same kind" / "6 such cups" is a hard word for 6-8; "Ben shares 20 biscuits equally with his 3 cousins" (B4 L7 T2, answer 5) is ambiguous for a 7-year-old (who is in the group?), by design as a trap, but there is no hint on the page; "Amelia" and "Jason" appear in Book 4/3 where the other names are Mei, Ali, Ben, Siti. Gate 8 in Book 2 wording "Write one number sentence for each step. The last number you write is how many stickers Mei has now" is long (two sentences, 30 words), fine for a Quest.
- Look-back "Tool I used" row prints four icons (Books 1-2) or six (Books 3-4) with no names; the Toolbox Card shows icon plus name, and the chips of L10 and L20 show names at 6.1 pt. Icons alone are not mapped to the card inside the lesson pages.
- Small figures still small: B1 L5 S1 ten-frames about 20 mm wide with a "+" about 1 mm (readable at 600 dpi 1-bit, tiny at normal view); B4 L6 S3 straw bundles about 12 mm; B2 L8 S6 and home balance tiles (7.0 pt); B2 L10 T3 bar labels (8.2 pt, "+5", "-3" about 5 mm). All remain readable at native 600 dpi 1-bit; a photocopy of a print was not tested.
- Kit pages: tens-bar kit page repeats 4 times in Book 2 and 3 times in Book 1 (paper only); B4 L10 kit still calls the 7 cut-outs "tool cards" next to the "Toolbox Card" (decision: cut-outs stay "tool cards"; consistent in all 4 books and the L20 notes).
- Quest "No tool" is on the Quest log and the L20 kit pieces but not on the card (the card has eight tools only; by design, TOOLBOX_CARD_FIXES H3).
- Home sheets with a figure that is only decoration: B3 home L1 H1/H2 (6 and 9 children), B3 home L5 H1.

## What was checked and found OK

- **Answers (whole of Books 1-4, all tiers, exit tickets, investigations by reasonableness, home 40 items, both Quest logs including secret caves).** Book 2 Quest: 39 / 67 and 44 / 83 / 12 and 42 / 82 and 43 / 6 and 20 / 6 cm and 10 cm / 45 and 42 / 9. Book 4 Quest: 5 and 16 / No and 6 / even and 20 / 24 and 6 / 20 and 13 / $4 and $20 / 8 and No / 6 and 16 / No and 10. All equal the key. Picture-dependent items re-solved from the picture, not the key: B1 L1 S1 (26), E1 (48), L3 S3 (Mei 38, Ben 41), L4 G3 (79, 79; 115, 115), L5 ten-frames; B2 L6 S1 (3 bundles 7 singles), S7 (36 on the line), T3 (both frogs 46), G1 line with 10 and 100 labels; L8 S1, S2 balances (1 button), S6; L9 rulers S4 (9, 13), S6 (7), T2 (line A from the 2 to the 9 mark, 7 cm), T3 (9.3, 12.6 so 9 and 13), snail G2 (plain bar 4 to 13, 8 and 14); L10 story steps (arrows carry words only, never the result); B3 L1 line-ups (every named child sits on the labelled place: Aisha 2nd, Jenny 2nd, Wei/Lily 1st/3rd, Ben 5th, Ali 3rd, Mei 9th, Jason 6th counted from the right door), G1 round table; L2 strips (all bars to true scale: 12/8, 15+7, 31+15, 45/30, 40 = 16+24, 30/18, 52/34, 52 books 33/19, 90 = 20/30/40); L3 all 14 picture equations (S2 6, S3 8, S4 5, S5 6, T1 6/7, T2 True/False, T3 3/5, G1 5/7/11, G2 8/6, G3 5/4, E1 9, E2 8, E3 7); L4 pairs; L5 groups (3 bags of 5, plates 3/1/2 cookies); B4 L6 ladybirds, tables, frog line; L7 dots and sweets (19, 14, 12); L8 strips (S3 strip 2, T2/T4/G2 to scale); L9 strips and price pictures; L10 G3 (star 6, heart 4); Quest gate pictures (39 sticks, arrow at 67, 7 + 5 frames, 3 and 8 cards).
- Figures new or enlarged this round: Book 3 L1 line-ups are now large and correct (10 children per row legible, about 7 mm each), the 6-child round table clear; L8 S1 beam cropped and level; story-step piles, digit cards (0 included), bar-model brackets (hatched missing piece) and the hundred-square cell hatching all read in colour and B&W.
- **Other home figures** (all 25 content sheets): each figure matches its text (bundles 4 + 5, 3 + 8; ten-frames 9 + 5; number lines 40/45/50, 50/56/60, 44-74 with 47 and 71; balances; ruler 4 to 15; story steps; bags 3 + 1, 4 x 4 stickers; plates; strips). Only M5 above gives an answer.
- **Pointers, contents, counts:** workbook, key and home contents page numbers all match the first page of each lesson (checked programmatically: workbooks 3/11/21/31/39, 3/11/19/27/33/41, 3/11/19/29/37, 3/11/19/27/35/43; keys 3/7/11/15/19 (/23), 3/6/10/14/18 (/22); home 3/5/7/9/11 (/13)). "Term N Lesson M" pointers in the Quest tutor notes match the slot map (Book 2 gates 1-8: T1 L1, L2, L3, L5, L6, L8, L9, secret L10; Book 4: T2 L1+L2, L3, L4+L6, L5+L7, L8, L9). Book 1 contents names the Toolbox Card and the "four tools carry a small Term 1 tag" line; Books 2-4 do not mention the card (decision CARD-BOOK1). Kit pages: B1 9/17/19/27/29/37/45, B2 9/17/25/39, B3 9/17/25/27/35/43/45, B4 9/17/25/33/41, all on fronts, backs with no text and 0.0 ink. Print bar on the Book 2 Quest page: end ticks 99.2 mm apart centre to centre, 100.0 mm outer; rulers on L9 pages measure 9.999-10.000 mm per cm (page content scaled so they stay 1:1).
- **Toolbox Card A:** names "Toolbox Card" on both pages; tools 1 Spot the pattern, 2 List every way, 3 Draw it, 8 Act it out tagged "Term 1" (the four of Book 1: L1 Act it out, L2 Draw it, L3 List every way, L4 Spot the pattern); the card definitions equal the chip text word for word (Act it out, Draw it, List every way, Spot the pattern, Work backwards); the look-back box wording and the three questions equal the card back; **the stuck chant in L20 (l20.json lines 712, 725, 1533) "Wait. Try a tool. Try a smaller case. Ask." equals the card's "When I am stuck" panel exactly.** Card PRINT_BW is 2 pages, 1-bit, 3500 x 4958 px.
- **B&W:** page-for-page image comparison of all 12 pairs: only the covers differ (colour vs grey); no page with an outlier. At 600 dpi 1-bit the L10 and L20 chips (icon plus name at 6.1 pt, six names), the Quest tool rows (7.9 pt) and the look-back icons (about 7 mm) are legible; hatched yellow, stippled tiles and dithered "?" cards stay distinct; "R" and "Y" letters on counters survive.
- Round 1 items closed and verified: H1, M1-M4, M7, M8 (Quest note now says "every gate is Start here level"), L10 chip names, "No tool" on the Quest rows (9 per Book 2 log, 8-9 per Book 4 log).

## Per-lesson table (book / lesson)

| Book-Lesson | Answers (wb, home, key) | Figures | Layout / size | Other |
|---|---|---|---|---|
| B1 L1 | OK | OK | OK | none |
| B1 L2 | OK | OK | home p5 intro/tab clash (M4) | none |
| B1 L3 | OK | OK (S3 38/41, digit cards) | **p23 T3/T4 no answer space (H1)**; instruction 11.0 pt | home p7 clash (M4) |
| B1 L4 | OK | OK (G3 block, 100 squares) | OK | **home p9 figure shows 68 (M5)** |
| B1 L5 | OK | ten-frame "+" tiny (Low) | OK | none |
| B2 L6 | OK | OK (S1, S7, T3, G1 labels) | p5 no "how you know" space (M3), 11.0 pt | home p3, p5 clash |
| B2 L7 | OK | OK | p13 tight, fine | T5 frame (M6) |
| B2 L8 | OK | OK; tile labels 7.0 pt | p19 11.0 pt; **p21 11.0 pt, short blanks, free space unused (M3)** | home p7 clash |
| B2 L9 | OK | OK (rulers 1:1, snail plain bar) | OK | home p9 clash |
| B2 L10 | OK | OK (story-step piles, T3/G3 bars) | p33, p35 11.0 pt, no lines on p35; chip 6.1 pt | **T2 = queue frame, same 5/3/9 as Quest cave (M6)**; T5 frame; home H4 opener; home p11 clash; timing note (M7) |
| B2 Quest | OK (all 8 gates + cave) | OK | tool row 9.0 pt; doubled "because" | Key 2: "In my head" (M1), "Quest v2" (Low) |
| B3 L1 | OK | OK (line-ups large, table) | OK | T1/home H4/S5/E2 = hp and extension frames (M6) |
| B3 L2 | OK | OK (scale) | OK | T2 = extension l1_u02 frame (M6) |
| B3 L3 | OK | OK (14 equations) | p22 11.0 pt | "x" before L5 (Low); "cup hides" opener |
| B3 L4 | OK | OK | home p9 clash | none |
| B3 L5 | OK | OK | p37, p39 11.0 pt | home H5 tricycle (RV, unchanged); home p11 clash |
| B4 L6 | OK | OK | OK; straws small | none |
| B4 L7 | OK | OK | p13 11.0 pt, no lines (M3); G1(c) lines (Low) | home p5 clash |
| B4 L8 | OK | OK (strips to scale) | OK | home p7 clash |
| B4 L9 | OK ($4 key fixed) | OK | OK | "Such means" (Low) |
| B4 L10 | OK | OK | **p37 11.0 pt, no space for "say why" (M3)**; chip 6.1 pt | T1 pre-printed table (Low, round 1) |
| B4 Quest | OK (all 8 gates + cave) | OK | tool row 7.9 pt; pills; doubled "because" | Key 4: "In my head" (M1), "page generator", absolute lesson numbers (Low) |

## What I could not check

- Physical print: no ruler on paper, no photocopy or fax test, no cutting test of kit pages, no check of 1-bit legibility after a photocopy of a print.
- The B&W PDFs carry no text layer (CCITT 1-bit images). Font sizes and text are taken from the colour PDFs; B&W was compared by image (only covers differ), not by reading its text.
- Kit pages were checked for position, blank back and text, but only the 100 square (B1 p37) was looked at as an image; their cut-out counts follow round 1.
- Keys were read in full as text and the Book 2 Quest notes were rendered; other key pages were not looked at as images. Open-ended items (investigations, "many answers are right", own-puzzle items) were checked against the key's reasoning, not solved exhaustively.
- Similarity is my own re-implementation (5- and 6-word runs plus reading the hits) over 47 corpus files; the original TERMCHECK scripts are not in the repository, and parts of the private papers that are not text (PDFs, images) were not searched. Names (Mei, Ali, Ben ...) are common to all material, so frame matches are listed by judgement, not by score.
- Child comprehension (6-8) judged against WORDING_GUIDE by eye, not with children; reading load of investigations not re-measured.
- Timing is the validator's model plus my per-part ratio estimate for L10; no live trial. The L20 timing (85:44) and others were not re-derived this round.
- Online practice, slides, decks, parent summaries, the loose L10/L20 Quest Log and parent-note PDFs (only the copies inside the books), the SCREEN colour Toolbox Cards B and C.
