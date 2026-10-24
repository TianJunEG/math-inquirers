# Independent re-audit 2: Level 1 Extension Workbook pilot (after FIXES.md)

Re-audited 23 Oct 2026, desk review by a model (no child tested). Files: `outputs/extension/L1/*Soft_Copy_Colour.pdf` and `*Print_BW.pdf` (96 pages each; the `*_vector.pdf` was used only for text comparison). Report only; nothing was edited. I did not use `extension/` check scripts. My own checks are in "Method".

## Method and coverage
- Text of all 96 colour pages read. Colour pages 1-77 all viewed as images (75 dpi, 3-page montages; zooms at 130-200 dpi of pp. 6, 27, 30, 54 and 55). Answer pages 79-96 read as text; pages 79-83, 90-92, 95 and 96 also viewed as images (84-89, 93, 94 text only). Print_BW pages viewed as images: 1, 3, 6, 22, 42, 43, 47, 55, 57, 63, 77; the other print pages were checked by comparing the vector print file's text with the colour text.
- Items: every question solved by me from the text and, for picture items, from the rendered figure (graph counts, rulers measured from pixel positions, towers, strips, Venn contents, Latin square). Compared with all printed answers and "Why" lines: **0 wrong answers, 0 mismatches between question and key except the wording problem M2 below.** Quick brute-force checks (own Python): 65 cent in 4 coins has exactly 2 sets (50+5+5+5, 20+20+20+5); 80, 70 and 40 cent in 3 coins each unique; 5c/10c 7 coins = 50 cent gives 4 and 3; 40 cent from 20c/10c has 3 ways; $38 needs 6 notes and coins (10,10,10,5,2,1); 14 marbles in 2 unequal bags 6 ways; 3 different numbers 1-6 sum 9 are 126, 135, 234; 4x4 Latin square (U8 GF2) has exactly one solution and it equals the printed key; 3s/4s lists (12 and 24 both; 4, 8, 16, 20 only 4s); 2s/5s loops (10, 20 both; 8 in neither); 5-14 loops (9, 11, 13 in both; 6 and 8 outside); 14 cubes in 3s and 4s unique (2 fours, 2 threes); 12 tiles 3 rectangles, 9 tiles 2; triangles in the 3-square strip 8; every ruler item (7, 5, 9, 7, 6, 9 cm) measured from the picture matches the key.
- Print edition: `pdfimages` shows 96 images, all gray, 1 bpc, CCITT G4, 4958x7016 px, 600 ppi. No text layer in the print file (vector file text is identical to colour except one removed line, below). All viewed print pages keep every figure; Venn loops solid versus dashed; coins and tags by border; cookies as dots; Mi as halftone. No information lost in the pages checked.
- Originality: 7-word overlap of the whole colour text (headers removed) against every file in `hp/` (pdf, docx, html, js, json) and all `docs/books/private_*` and `docs/sasmo/private_solution_notes_*` files present. 83 shared 7-grams, in about 30 runs: number runs ("3 7 11 15 19 23 27 31", "4 7 10 13 16 19 22"), stock definitions ("a triangle has 3 sides and 3 corners", "in 0 2 4 6 or 8", "our coins are 5 10 20 and 50", "there is always 1 gap fewer than"), and three of our own lines from the P1 Tutor Guide ("when one number goes up by 1 the other goes down by 1", "a ruler also when the object does not start at 0", "the equals sign means both sides have the same value"). From private extracts only trivial 7-grams ("fill in the missing numbers in the", "is the same as the number of"). **No item, story or sentence is copied from the private extracts.**
- Compliance scan of the colour text: no price, no "tutor", no MOE, GEP, SASMO or syllabus text ("It is not an official school or examination book" only). "You do not need a teacher" is the only teacher word. "Holiday Program" appears (p3 defines it; contents lines).

## Status of earlier findings

| # | Earlier finding | Status now |
|---|---|---|
| H1 | Placeholders, draft licence (p2) | **Still open (owner).** "[business email, owner to add]" and "[address, owner to add]" are on p2 in both files; UEN and licence wording unverified. Blocks sale. |
| H2 | Unit 8 Learn it | **Fixed** (p55): two worked examples (grid; Venn of 2-9 with even and more than 6, 8 in the middle, 3 and 5 outside), "How to use grids and loops" and "Odd and even" boxes, Try. Q5 no longer teaches. Only issue: dense and small type, see M3. |
| H3 | Unit 7 shape names | **Fixed** (p48 "Shape names" figure, 3 to 8 sides). Labels are 7-8 pt, see M3. |
| H4 | Unit 4 growing example | **Fixed** (p27 Worked example 2, table, +5 arcs, readable). |
| M5 | Pace plan | **Fixed.** p3, p5 and every Go further banner say weekend page; session 3 is Think harder and Check yourself (2 pages each session). |
| M6 | Hints | **Fixed in size and length:** 63 hints, about 11 pt, one line, at most 67 characters, upside down, none states an answer. A few still give the method, see L3. |
| M7 | Tiers | **Mostly fixed.** Swaps hold and all keys agree. U1 TH1, U4 TH3 and U10 TH3 are still no harder than a Start here item, see L4. |
| M8 | Writing space | **Mostly fixed:** U5 GF3 has 5 day lines, long lines for lists, U9 Q3 line is about 95 mm, U2 TH1 has 6 table rows for 6 ways. "Draw it" items still have one rule only, see L5. |
| M9 | Figure size | **Partly fixed.** Icons now about 6 to 6.5 mm, logic grid cells 8-14 mm, Venn numbers 15 pt on p57 with commas (no more "37"). Learn-it figures still small, see M3. |
| M10 | 1-bit print pipeline | **Fixed:** 600 dpi 1-bit CCITT, no grey. Printer proof still needed (owner). |
| M11 | Mi on cover | **Fixed** (about 20 percent of the page). |
| L12 | Header and lesson names | **Fixed** (contents and pace plan show title, topic and "follows Holiday Program Lesson N"; p3 defines it). |
| L13 | Try lines | **Fixed** (U9 ruler Try, U10 plant Try). |
| L14 | a/an in U7 Q1 | **Fixed for Q1.** Same slip remains in U7 TH3(a), see L6. |
| L15 | U9 Q5 pencil; U8 GF2 Why | **Fixed** (pencil drawn; Why now step by step; puzzle unique). |
| L16 | Ruler real size note | **Fixed** (p3 and p62, soft copy only). |
| L17 | Tear line | **Half fixed.** The tear line is gone and p78 is blank, but see M1. |
| L18 | Even defined two ways | **Fixed** (last digit; U10 Q9 Why uses it). |
| L19 | Child welcome | **Fixed** (3-line "For you" box). |
| Reported | Learn-it intro text overlaps the "Worked example" tab | **Still present**, see L1. |

## Findings

### High
1. **(open from audit 1, H1) Printed placeholders and draft licence on p2** (colour and print). Owner supplies email, address, UEN check and lawyer-approved licence, then rebuild. Nothing else blocks sale.

No new High found.

### Medium
**M1. "Self-study" versus "answers for grown-ups" (cover, p3, p79-96).** The cover says "Self-study", p3 says "You do not need a teacher" and the child box says "Do Check yourself. Then look at the answers." But p79 and every answer page header say "for grown-ups", p3 tells the grown-up "Read the reason together", the answer type is about 8.5 pt, and the Why lines are adult prose. A child cannot self-mark from them and the book does not say who does. Also "keep them in an envelope or cover them" cannot be done with a bound printed copy. Fix: one sentence on p3 (who marks), larger answers with a short "Answer" line first, or add a "check with a grown-up" step to the child box; say how the printed copy is to be bound (answers as a detachable booklet or a sealed section).

**M2. U8 Q8(b) (p57, key p92): the question and the key do not match.** The stem reads "(b) Numbers said in 4s but not in 3s:" with a single small box, which asks for the numbers (4, 8, 16, 20). The key is "4" (a count) and the Why says "6 - 2 = 4 are in 4s only". A child who writes the numbers is marked wrong. Fix: "(b) How many numbers are said in 4s but not in 3s?"

**M3. Learn-it figures and density for age 6-8 (M9 only partly fixed).** Measured from the PDF: p48 shape names 8.1 pt with "3 sides" 7.4 pt (shapes about 7 mm); p55 grid headings 8.9 pt, loop numbers 8.6 pt (about 3 mm), Try grid headings 8.5 pt; p27 two worked examples side by side with 9 pt step text. p55 now holds two worked examples, two boxes and a Try; with Start here 1 (p56, 5 items) in one 20 to 25 minute session 1 it is a lot for a solo 6 to 7 year old. Fix: raise those labels to at least 10 pt (shape names to two lines if needed), or move the "Odd and even" box and Try to p56 header space.

### Low
1. **Tab overlap (reported earlier, not fixed).** The "Worked example" tab touches and clips the descenders of the last intro line on **pp. 6, 13, 20, 34, 41, 48, 69** (clear on 27, 55, 62). About 1 mm; readable, looks untidy. Fix: 2 mm more space above the tab, or shorten the intro by one line.
2. **Soft-copy wording in the print edition.** p2 "This soft copy is licensed to the buyer", p3 "Printing the soft copy? Print at 100 percent" and the print file drops the "Real size when printed at 100%" note on p62 (right for print, but p3 still tells a print buyer to print). Make p2, p3 edition-specific.
3. **Hints that still hand over the method:** U10 TH3 (p73) hint "Undo the last step first" repeats the three "Undo" lines already printed on the page; U7 TH2 (p52) "Do 2 lines that meet make a larger triangle?" is the whole insight; U4 GF3 (p32) outlines the method; U1 TH3 (p10) "Draw the hops ... How far in all?". U6 TH1 (p45) hint leads to only one of the two sets. Nudge, not answer, so not blocking.
4. **Tier overlap.** U1 TH1 (2 plus 5s, will she land on 37 and 40) is no harder than Start here Q13; U4 TH3 (table, add 3 each day) repeats Q11; U10 TH3 (undo three steps) repeats Q12 and its writing lines give the steps. Think harder still has 3 items per unit. Still no "make your own" item (rubric criteria 5 and 9 stay 0).
5. **"Draw it" space is a single rule** (U5 Q10 and Q11 "Draw the queue", U9 TH1 "Draw the ribbon", U10 Q8 "Draw it"); a child needs a blank strip about 15 mm tall. U3 Q7 drawing boxes are 7.5 mm (small for drawing a face).
6. **a/an with option words:** U7 TH3(a) "The other is a [square / hexagon / octagon]" reads "a octagon". Use "The other is:".
7. **U3 Q5 key Why (p83) says "9 stars"**; the graph and key say stickers. U5 Q7(b) key "13, 13, 19" is in table order (IN, OUT, OUT) with no labels; say "IN 13, OUT 13, OUT 19".
8. **Contents (p4) lists neither Welcome nor the pace plan (p3, p5).** Print file has no text layer (not searchable, fine for press, but keep the vector file for accessibility).
9. **U6 Learn it (p41)** shows only "fewest coins"; its goal promises "all the ways" (Q11, TH1, TH3 need it). Hints cover it; add one line "list ways in a table" if space allows. Notes ($2, $5, $10) first appear in Q2 and GF3 without a line saying they are notes; fine for the P1 reader but unexplained.
10. Rubric score unchanged in spirit: student-led discussion 0 by design, multiple methods and problem posing 0.

## Checks that passed
96 pages in both files, even count; contents and answer page numbers correct (80, 81, 83, 84, 86, 88, 90, 91, 93, 95); p78 blank, answers begin on a front page (p79) so they can be printed separately; every item has a printed answer and a Why (63 hints, 4-item Check yourself, score rule and Look back in every unit); U8 Learn it, U7 names and U4 growing example all present and correct; hints upside down 11 pt, at most 67 characters; Check yourself graph and all picture counts agree with keys; icons, coins and ruler marks distinguishable in 1-bit; Venn and tags survive in black and white; print is 1-bit 600 dpi with no grey; no price, no MOE, GEP or SASMO, no tutor; originality clean.

## Ranked top 10
1. Placeholders and draft licence (High 1). 2. Self-study versus grown-up answers (M1). 3. U8 Q8(b) wording (M2). 4. Learn-it figure and type size, U8 density (M3). 5. Tab overlap on 7 pages (L1). 6. Soft-copy wording in the print edition (L2). 7. Draw-it space (L5). 8. Hints that give the method (L3). 9. Tier overlap U1 TH1, U4 TH3, U10 TH3 (L4). 10. "a octagon", "9 stars", key order (L6, L7).

## Verdict
Maths and answers are correct and the earlier High 2-4 and Mediums 5-11 are fixed. Sellable once the owner fills p2 (High 1) and the two small text fixes M1 and M2 are made; M3 and the Lows can follow. A child trial for pace and reading load is still needed (not replaceable by this review).
