# Holiday workbooks: final print-readiness check (23 Oct 2026)

Independent final checker, audit only (nothing edited except this report; nothing pushed). Print order Fri 6 Nov 2026, change freeze Mon 2 Nov.
Files checked: `outputs/print/Math_Inquirers_P1..P6_Workbook_PRINT.pdf` (colour, soft copy) and `outputs/print/bw/Math_Inquirers_P1..P6_Workbook_PRINT.pdf` (the printer files, 1-bit 600 dpi CCITT, A4), `print_spec.json`, `bw_spec.json`, `docs/printing/*`, designed workbooks, tutor guides, weekly zips.
Freshness: every print PDF (colour and B&W) is newer than its designed workbook and than every source file under `hp/ p2/ p3/ p4/ p5/ p6/`; text of every print PDF equals text of its designed workbook page for page (all six). No rebuild was needed or done.
Method: every page of all six B&W print files looked at (contact sheets, 6 pages each, 70 dpi), every changed or suspect figure re-rendered at 130 to 300 dpi; PyMuPDF scans for text under 8 pt, off-page text, blank pages, text colour that turns into a pattern in B&W; page counts and blank-page parity for colour and B&W; weekly zips and guides compared with the designed workbooks; 26 changed questions re-solved by hand against the printed keys.

## 1. Verdict per level

| Level | Print pages / sheets | Verdict | Why |
|---|---|---|---|
| 1 (P1) | 68 / 34 | **GO** | All review items fixed. Only Low cosmetics left. |
| 2 (P2) | 74 / 37 | **GO** | All review items fixed. Medium: p32 tick labels clipped at the bottom; "take-home" star labels print as ghost text on 15 pages. Fix p32 if the freeze allows; otherwise accept. |
| 3 (P3) | 70 / 35 | **GO** | All review items fixed. Medium: Investigation table headers and shaded rows are weak in B&W (p23, 39, 45, 51, 57). |
| 4 (P4) | 76 / 38 | **GO** | All review items fixed. Medium: cut-out pages p67, p69, p73 are clipped at the right edge (see 3.2). |
| 5 (P5) | 62 / 31 | **GO** | Both review Highs fixed. Medium: p21 label clipped; orange labels ("After question 3", "take-home", "Make up your own") print as ghost text on 40 pages. |
| 6 (P6) | 62 / 31 | **NO-GO until one High is fixed** | The cut-out "Unplugged code cards" (print p57) are unreadable in the B&W file (white text on dot/line patterns). Small fix in `p6/kit.js`, rebuild P6 print and B&W; page count does not change. |

Non-file Highs that must be fixed before the order or the printer quote goes out (documents, not PDFs): (a) `docs/printing/quote_request.md` still says Level 6 = 58 pages / 29 sheets, the file is 62 / 31; (b) `docs/printing/dispatch_list.md` and `dispatch_list_template.csv` tell staff to send `outputs/print/Math_Inquirers_P<level>_Workbook_PRINT.pdf`, which is the COLOUR file; the owner decision is to send only `outputs/print/bw/`.

## 2. Verification of every High and Medium finding in the two reviews

Page numbers are PRINT page numbers (the L1-3 review used source page numbers; they moved by +1 after lesson 7 of Level 3 and so on). All checked on the B&W print file, key ones also on colour.

### Reviews Levels 1 to 3

| Item | Result | Where it is now |
|---|---|---|
| H1 L1 L3 T1 picture-graph key | FIXED: "= 2 children" and half star "= 1 child" fit | L1 p16 |
| H2 L3 L10 No.1 Lime juice bar | FIXED: short dashed base with "?" above the axis, no height shown; key 50 | L3 p52 |
| H3 L3 L10 No.5 sticks captions | FIXED: "1 square / 2 squares / 3 squares" about 11 pt, nothing cut | L3 p53 |
| H4 L3 L9 No.5 time lines | FIXED: (b) second hop ends at an unlabelled "?" tick, both hops 25 min; (c) line starts at 7:00 so 7:25 is on it | L3 p47 |
| H5 L2 L7 No.3 fraction bars | FIXED: all bars unshaded, equal length, parts marked | L2 p38 |
| M1-1 L1 Venn | FIXED: loops large, overlap about 24 mm | L1 p40 |
| M1-2 L1 house flag and sun | FIXED: both clearly visible | L1 p35 |
| M1-3 L1 queue "front" | FIXED | L1 p25 |
| M1-4 L1 pet icons | FIXED: spaced, countable | L1 p51 |
| M2-1 L2 balances | FIXED (captions complete, scales apart). Residual Low: Scale 3 label "apple, 4 lemons" is crossed by the stand | L2 p48, p51, p53 |
| M2-2 weight labels | FIXED (no text under 8 pt in these figures) | L2 p48, p51, p53 |
| M2-3 C7 time line "8:15 am" | FIXED | L2 p53 |
| M2-4 T2 time line | FIXED | L2 p51 |
| M2-5 L6 T1 "Ben's money" | FIXED | L2 p35 |
| M2-6 L5 bar labels | FIXED (large) | L2 p26, p28 |
| M2-7 hens | FIXED (spaced) | L2 p15 |
| M2-8 bicycle captions | FIXED | L2 p18 |
| M2-9 L8 No.4b grid | PARTLY: dashed grid is darker, but some segments are still very pale (left part of the middle row). Low | L2 p44 |
| M2-11 L6 guide page references | FIXED and re-checked for all ten L2 lessons: every "Page 1 / 2 / 3: Qn" line in the guide matches the final pages | L2 guide |
| M3-1 L5 counters | FIXED: full circles | L3 p24 |
| M3-2 C5 brace label | FIXED | L3 p50 |
| M3-3 T3 box segment | FIXED: 1.25 book widths | L3 p49 |
| M3-4 "pm" label | FIXED: white box | L3 p47 |
| M3-5 L10 No.3 queues | FIXED: ordinals removed from (b), "3rd" off the connector | L3 p53 |
| M3-6 L8 No.2 shapes | FIXED: shapes about 1.5 times larger | L3 p41 |
| M3-7 staircase captions | FIXED | L3 p45 |
| M3-8 L4 bar labels | FIXED | L3 p18 |
| M3-9 L4 No.5 "?" | FIXED | L3 p19 |
| M3-10 L7 No.6 grids | FIXED: 6.9 mm cells | L3 p36 |
| M3-11 nearly empty pages | NOT changed (accepted by builder; see 3.6) | L3 p22, p41, p48, p54; L2 p5, p11, p29, p52 |

### Review Levels 4 to 6

| Item | Result | Where |
|---|---|---|
| H1 P5 L5 Go further B3 tank | FIXED: caption complete, block labels gone, "10" arrow, 30 cm and 20 cm clear | P5 p27 |
| H2 P5 L1 No.6 number line | FIXED: shaded band and title gone, five ticks kept | P5 p4 |
| M1 P5 L2 No.1(b) | FIXED: bars unshaded (3 and 5 equal parts), labels large | P5 p8 |
| M2 P5 L2 No.3 | FIXED: labels 9 pt or more | P5 p8 |
| M3 P5 L5 No.3 tank labels | FIXED | P5 p23 |
| M4 P5 L8 A4 | FIXED: "?" labels readable | P5 p41 |
| M5 red text in B&W | FIXED for figure text (P5 angle values, P4 queue and "? cm", P6 "turn 70", "$69" are now navy and solid). NOT fixed for body-text orange labels (new finding N1) | P5 p38 to p42 |
| M6 P6 route grid "P" | FIXED: boxed P sits in the cell next to the hatched circle | P6 p24 |
| M7 P4 jar bar | FIXED: undivided bar with three braces | P4 p24 |
| M8 P4 queue text | FIXED: navy | P4 p54 |
| M9 P5 printers bar | FIXED: P alone at 1/6, brace over the whole bar | P5 p29 |
| Low L9 guide wording P6 L7 to L9 | FIXED in `p6/content/l7.js` and guide rebuilt | P6 guide |

## 3. Remaining issues (fresh end-to-end pass)

Severity: High = unusable or wrong in print; Medium = fix if the freeze allows; Low = cosmetic.

### 3.1 High

| # | Level / file / page | Problem | Change |
|---|---|---|---|
| H-A | **P6 B&W, print p57** (source p56, "Cut-outs: Unplugged code cards (Lessons 1, 4 and 7)"; colour file is fine) | Nine of ten cut-out code cards (when green flag clicked, repeat 10, move 10 steps, turn right 90 degrees, say (answer), set n to 1, change n by 1, if ... then, ask ... and wait) have white text on dot or line patterns; only "pen down" (solid black) reads. The cards are used in L1, L4, L7 (guide p5). The caption is also cut at the right edge ("...before you build it on scre"). | In `p6/kit.js` (`K.codeCards()`): print each card with a white or very light fill, a thick outline and BLACK text (colour can stay on a left stripe); shorten or wrap the caption. Rebuild P6 (workbook, print, B&W) and re-run `print/check_bw.py`. No page-count change. |
| H-B | `docs/printing/quote_request.md`, workbook table | Level 6 row says 58 pages, 29 sheets. Actual and `print_spec.json`: 62 pages, 31 sheets. L1 to L5 rows are correct (68/34, 74/37, 70/35, 76/38, 62/31). | Change the row to 62 / 31. |
| H-C | `docs/printing/dispatch_list.md` (column `workbook_file`) and `dispatch_list_template.csv` | Point at `outputs/print/Math_Inquirers_P<n>_Workbook_PRINT.pdf` (colour). README_bw and the quote text say printers get only `outputs/print/bw/...`. | Change both to `outputs/print/bw/Math_Inquirers_P<n>_Workbook_PRINT.pdf`. |

### 3.2 Medium

| # | Level / file / page | Problem | Change |
|---|---|---|---|
| N1 | **P5 (40 pages) and P2 (15 pages), B&W** | Orange body text becomes a dotted ghost: P5 "After question 3 you may choose" on every Start here page 1 (p3, 8, 13, 18, 23, 28, 33, 38, 43, 48), the star "take-home" marker, "Make up your own."; P2 "take-home" marker (p4, 9, 10, 20, 21, 25, 32, 33, 37, 38, 43, 44 and more). Seen at 250 dpi: barely readable. The take-home marker decides what is homework. Colours: P5 #D9662B (luma 0.51), P2 #B45F06 (luma 0.43, just over the 0.42 threshold of `print/make_bw_print.py`). | Easiest: in `p5/workbook_html.js` (lines 29, 39, 57) and the P2 content (`p2/content/l*.js`, B45F06) use a dark colour (for example #8A3F10 for P5, #8A4504 for P2, luma under 0.40), or navy. Rebuild P2 and P5 print and B&W. Alternative: lower the converter threshold for text. |
| N2 | **P2 print p32** (L6 No.3, counting-up lines "65c to $1" and "$26 to $50") | Tick labels (65c, 70c ... 100c; $26 ... $50) are cut off at the bottom of the SVG (about 15 percent of the digits missing). Readable, but looks broken and it is the data of the question. Not in either review. | In `p2/figs_l2.js` (line 65, the two `svg(600, 96, ...)` calls) raise the viewBox height by about 14 units; check p32 still fits. |
| N3 | **P5 print p21** (L4 Think harder No.A4) | The rectangle's left height label is clipped to "m"; the triangle's "7 cm" is overprinted by the slanted side. | In `p5/content/l4.js` (A4 figure, line 200) add left margin and move the triangle label to the left of the dashed height. |
| N4 | **P4 kit pages, print p67, p69, p73** (source p62, p64, p66) | Content is clipped at the right edge: the 6th column of digit, point, sign and bracket cards has no right cut line and the caption ends "Decimal points: Les"; Graph grids caption ends "Print extra copies if you need then"; the clock page ends "Make a hole at each red dot, then jo", "Pizza circles ... (quarter" and the "Bring from home" box loses its last words ("Lessons 7" for "7 and 8"). The cards can still be cut. | In `p4/kit.js` / `p4/kit_extra.js` reduce the content width by about 12 px or the card size by 5 percent; rebuild P4. |
| N5 | **P6 in-page Scratch blocks, B&W** (print p4, 9, 14, 19, 23, 24, 28, 29, 33, 34, 41, 47) | Variable and motion blocks have white text on a hatch fill ("set n to", "change n by", "say total", "repeat", "set count to"); readable with effort, ghosted at 7 pt in some (p33). Orange, blue and green blocks only. | Same treatment as H-A in the workbook block style (black text on white fill with a pattern stripe), or darken the fills so the converter turns them solid black. |
| N6 | **P3 Investigation tables, print p23, p39, p45, p51, p57** | Header text 7.8 pt on a dotted fill; body rows on p51 and p57 become dense horizontal-line hatch, so the child writes on a pattern; "20-cent coins / 10-cent coins / 5-cent coins" header is hard to read. | Use a white or very light header fill with black text, no row tint. |
| N7 | **Docs and specs out of step with the files** | `outputs/print/bw/bw_spec.json` holds only six Level 1 Term 3 term-book rows and no P1 to P6 rows (the fix report says it was rewritten). `docs/holiday_readiness.md` lines 36 and 75 still say print pages 64, 74, 64, 76, 62, 58 and 55-page L6; `docs/product/face_to_face_pilot_plan.md` line 27 says "58-page designed workbook, 64 print pages" for Level 1. | Re-run `python3 print/make_bw_print.py --check` (or the L1-3 / L4-6 scripts) so `bw_spec.json` lists P1 to P6; correct the two docs. |
| N8 | **B&W printer files are not in git** (`.gitignore` line 28 `outputs/print/bw/*.pdf`) | The six files exist only on this disk (9.9 to 17.4 MB each, about 80 MB in total). Anyone cloning the branch gets the colour files only. | Copy them out now (checksums in section 6) or remove the ignore rule for these six files. |

### 3.3 Low

- Thin rule at the top of continuation pages, in the case of P4 p44 and p49 cutting the tops of the italic note "Page 2 is on your own...": also P4 p27, p50, p55, L1 p4, L3 p53. Fix by clipping overflow of the previous question box.
- Certificate "Date:" line wraps to a second line on L1 p67, L3 p67, L4 p75, L6 p61 (L2 and L5 fit).
- L1 p40 Venn: loop titles "Numbers less than 6 / Odd numbers" nearly touch.
- L2 p48: Scale 3 label crossed by the stand; "100g" trays tight.
- L2 p44 grid partly pale (M2-9 residual).
- Footer text is 6.4 pt on every page; L2 Start-here notes 6.7 pt and Tool-of-the-day text 7.3 pt; L3 7.8 pt template text; L5 Tool of the day, reflection box 6.9 pt; L5 and L2 "PLAY MONEY" 6.9 to 7 pt; P6 Scratch file names 7.5 pt and code text 7.0 to 7.8 pt. All template text from the design, none of it carries a question's data. Figure text is 7.8 pt or more everywhere except P6 code blocks (7.0 pt).
- Pages less than half full (design, accepted by builders): L1 p34 (after fix about half), p36, p37, p48, p53; L2 p5, p11, p29, p30, p52; L3 p22 (No.4 only), p41, p48 (No.6), p54; L4 p31, p33, p57; L5 p17, p32; L6 p27, p32, p50, p55.
- Cut-out sections: all start on an odd (front) print page, every cut-out page has a blank back. Cut-out content is black text on 1-bit patterns and readable in L1 to L5 (coins and notes: values read clearly).
- Cover, inquiry journal, certificate and footers are consistent; "Page N" on a print sheet is the source page number (for example print p57 shows "Page 56" in Level 1); nothing refers to print page numbers.
- No table of contents exists in the holiday workbooks (the journal page lists the 10 lessons without page numbers), so no contents page can be wrong.
- The Level 1 Word workbook (`hp/workbook.js`) and the decks still show older figures; neither goes to the printer.

### 3.4 Page counts and structure (all agree)

| Level | Designed | Print colour | Print B&W | `print_spec.json` | Blank backs (all even pages) | Cut-out front pages (print) |
|---|---|---|---|---|---|---|
| 1 | 61 | 68 | 68 | 68 / 34 sheets | 7 (56, 58 ... 68) | 57, 59, 61, 63, 65, 67 |
| 2 | 66 | 74 | 74 | 74 / 37 | 8 (60 ... 74) | 59, 61, 63, 65, 67, 69, 71, 73 |
| 3 | 63 | 70 | 70 | 70 / 35 | 7 (58 ... 70) | 59, 61, 63, 65, 67, 69 |
| 4 | 66 | 76 | 76 | 76 / 38 | 10 (58, 60 ... 76) | 59 to 75 odd (9 sheets) |
| 5 | 57 | 62 | 62 | 62 / 31 | 5 (54 ... 62) | 53, 55, 57, 59, 61 |
| 6 | 58 | 62 | 62 | 62 / 31 | 4 (56 ... 62) | 57, 59, 61 |

Colour and B&W have the same blank pages in every level. No unexpected blank or near-empty page. Left gutter alternates correctly. B&W files are A4, 1-bit, 600 dpi, CCITT G4; no colour (non-grey share 0). No off-page text in any file.
Note for L1 and L3 to L6: print p1 is the cover, so the printer's page count equals the designed page count plus the padding blanks.

### 3.5 Tutor guides, weekly PDFs, zips

- Weekly student PDFs (five weeks) of all six levels: every page has text identical to a page of the final designed workbook (60, 62, 62, 65, 56, 55 pages; none missing). All zips are newer than their workbook (L1 12:47 vs 12:44, L2 12:47 vs 12:45, L3 12:47:39 vs 12:47:08, L4 to L6 13:10 or later).
- Tutor guides: P2 (12:44) rebuilt after the L2 fix; P4 to P6 (13:10 to 13:11) after the final workbooks. P1 (10:34) and P3 (10:33) predate the last workbook rebuild; they hold keys only and the keys did not change. Every per-question page reference in the guides was checked against the final layout for Level 2 (all ten lessons), Level 1 L10 (Q9 on page 2), Level 5 (page 1 / page 2 lines) and Level 6 L7 to L9 (now say "next sheet"): consistent. Level 3 and 4 guides use only "page 1 / page 2" per lesson, still true.
- Guides for P1 to P6 say "Cut-outs used: ..." per level; the cut-out pages match.
- `outputs/workbook/Math_Inquirers_P1_Student_Workbook_Designed.pdf` is byte-identical to `hp/..._Designed.pdf`.

### 3.6 Consistency with `docs/printing/quote_request.md`

| Item | Status |
|---|---|
| Pages and sheets L1 to L5 | Match files and `print_spec.json` |
| Pages and sheets L6 | **Wrong (58 / 29 in the doc; file 62 / 31)**, see H-B |
| "1-bit, 600 dpi, no colour at all", A4, duplex flip long edge, left binding, keep blank pages | Match the B&W files |
| Cut-out pages "blank back" | True for all six |
| Term-book table (Book 1 to 8, key and home pack counts) | Match `outputs/print/bw/term/` (46, 44, 44, 48, 42, 44, 48, 42; keys 22/30/22/28 and 22/30/22/30; home packs 12/14 ...) |
| Kit card A5 table | Three `_PRINT_BW.pdf` files exist, A5, 2 pages each |
| Dispatch list | Wrong file path (colour), see H-C |

## 4. Spot-solve (26 changed questions, figure and text against the printed key)

All 26 agree with the key; no figure gives the answer away or contradicts it.

1. L1 L1 No.3 frogs in 4s and 5s: both land on 20.
2. L1 L1 No.5 stickers: box 10 = 29 (2, 5, 8 ... 29).
3. L1 L5 No.4(a) queue of 20, Mei 7th: 13 behind.
4. L1 L5 No.4(b) 3rd from front and 3rd from back: 5 children.
5. L1 L6 No.3 85c: 50 + 20 + 10 + 5, 4 coins.
6. L2 L3 No.3 hens and goats, 7 animals 20 legs: 4 hens, 3 goats.
7. L2 L3 No.4 23 stickers, 4 friends: 5 each, 3 left.
8. L2 L5 T2 Ben $42 now: $36 at first.
9. L2 L5 T3 Siti 30 beads: 36 at first.
10. L2 L7 No.3 bigger fractions 1/3 and 7/9; order 1/10, 1/5, 1/4, 1/2.
11. L2 L9 No.1 scales: apple 200 g, melon 400 g, lemon 50 g, 8 lemons.
12. L2 L9 Go further No.6 cube 100 g, ball 200 g.
13. L3 L4 No.4 150 marbles, 24 more: Ben 63, Ali 87.
14. L3 L4 No.5 85 and 47: 19 stickers, 66 each.
15. L3 L9 No.5 time lines: 1 h 25 min, 5:25 pm, 7:25 pm.
16. L3 L9 T3 box 250 g and four books 1 kg 50 g: 200 g each.
17. L3 L9 C5 bottle 1 kg 200 g, 750 g half poured out: 300 g.
18. L3 L10 No.1 drinks: Lime juice 50; Milo + Kopi = 100.
19. L3 L10 No.5 sticks: 8 squares 25 sticks, 31 sticks 10 squares.
20. P4 L1 Q3 18 and 24: 6 packs, 3 red 4 blue.
21. P4 L3 Q6 124 plates: laksa 31, chicken rice 93, 62 more.
22. P4 L4 Go further No.5 1/2 and 1/3 taken, 5 left: 30 sweets (key 30; part b 42).
23. P5 L2 Q5 2/5 game then half the rest, $36 left: $120 at first, book $36.
24. P5 L5 B3 tank 30 by 20, water 10 deep, block 10 by 10 by 15: 12 cm.
25. P5 L6 Q4 printers 30 and 20 a minute, 900 pages, P alone 5 min: 20 minutes.
26. P6 L5 Q5 grid routes: 20; 8 avoiding P (hatched circle at column 2, row 2 from the bottom). Also P6 L3 Q3: 15 m, 9 m, -13 m.

## 5. Printer-pack checklist

What to send: ONLY the six B&W files. Not the colour files in `outputs/print/` (soft copies for downloads), not the designed PDFs, not the guides or zips.

| File | Pages | Sheets | Cut-out pages (blank back, do not drop) | Quote quantity band |
|---|---|---|---|---|
| `outputs/print/bw/Math_Inquirers_P1_Workbook_PRINT.pdf` | 68 | 34 | print 57, 59, 61, 63, 65, 67 | quote 1-9, 10-49, 50+ copies; first order 1 sample |
| `.../P2_Workbook_PRINT.pdf` | 74 | 37 | 59 to 73 odd (8) | as above |
| `.../P3_Workbook_PRINT.pdf` | 70 | 35 | 59 to 69 odd (6) | as above |
| `.../P4_Workbook_PRINT.pdf` | 76 | 38 | 59 to 75 odd (9) | as above; sample 1 |
| `.../P5_Workbook_PRINT.pdf` | 62 | 31 | 53 to 61 odd (5) | as above |
| `.../P6_Workbook_PRINT.pdf` (after H-A) | 62 | 31 | 57, 59, 61 | as above |

Print settings to state: A4, black and white only, both sides, flip on the long edge, left binding (spiral or wire-o on the left long edge), do NOT remove or reflow blank pages, do not scale ("actual size", the files already carry a 12 mm gutter), 80 / 100 / 120 gsm prices, cover options (a) none and (b) clear front and card back.
Quantities (`quote_request.md`): 5 to 30 workbooks a week at first, quote bands 1-9 / 10-49 / 50+; one workbook per parcel (2 siblings may share a parcel); the quote text asks for one sample each of Level 1 and Level 4 before committing; staff send one batch order a day by the printer's cutoff using `dispatch_list_template.csv` (one row per parcel; after H-C the `workbook_file` column points into `outputs/print/bw/`).
Inquirer Kit card (separate, A5, 2 pages, 1 card per child per workbook, about 10 percent spare): `outputs/kit/Math_Inquirers_Toolbox_Card_A_6-8_PRINT_BW.pdf` (Levels 1 and 2), `..._B_8-10_...` (Levels 3 and 4), `..._C_10-13_...` (Levels 5 and 6); do not send the `_SCREEN_colour` files.
Not for this order: `outputs/print/bw/term/*` (term books, Level 1 only, a different order).
Before sending: tell the printer the cut-out pages are meant for cutting (optional perforation along the dashed lines is a quote option) and that the first page is the cover.
Before the order: (1) fix H-A and rebuild P6; (2) fix H-B and H-C; (3) decide whether N1 to N4 are done before the freeze; (4) copy the six B&W files out of this disk (N8) and compare with the checksums below; (5) order the L1 and L4 samples first.

## 6. Checksums of the files reviewed (first 16 hex of SHA-256)

B&W (printer) files: P1 13ffa24474a70537, P2 78d603674ef14384, P3 65de9630dc771f06, P4 0faa960f8afb2b90, P5 b998489b9bda6519, P6 8925a633fb511f6f (P6 will change after H-A).
Colour (soft copy): P1 a1c9edae3e1e2c39, P2 41764dfc91dca442, P3 a3710014ebef2f77, P4 27e08b33b603139c, P5 b0e5d4adc2ce5e6d, P6 49c1eaa399344686.

## 7. Limits of this check

Every page was viewed at about 70 dpi (readable layout, not every word); every figure listed in section 2 and every Medium/High item above was viewed at 130 to 300 dpi. Only 26 questions were re-solved; unchanged pages got a visual and text-scan pass, not a full re-solve. The B&W look was judged on rendered pages of the 1-bit files, not on a real printer. No Scratch or Python code was run.
