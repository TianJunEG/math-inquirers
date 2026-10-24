# Holiday workbooks: print-readiness check, round 2 (23 Oct 2026)

Independent final checker, audit only (nothing edited except this report; nothing pushed). Print order Fri 6 Nov 2026, freeze Mon 2 Nov. Round 1: `holiday_print_readiness.md`.
Files: printer files `outputs/print/bw/Math_Inquirers_P1..P6_Workbook_PRINT.pdf` (1-bit, A4), colour soft copies `outputs/print/Math_Inquirers_P1..P6_Workbook_PRINT.pdf`, `print_spec.json`, `bw_spec.json`, `docs/printing/*`, designed workbooks, tutor guides, weekly zips, kit cards.
Method: all 410 pages of the six B&W files viewed (2 to 3 pages per image, 100 dpi; suspect figures re-rendered at 200 to 250 dpi). Scripts: text under 8 pt, off-page text, ink within 4 mm of the page edge, near-empty pages, text colour and white-on-pattern scan, page counts and blank parity (colour and B&W). Colour print text equals the designed workbook text page for page in all six levels, and every print file is newer than all sources under `hp/ p2/ ... p6/`. Weekly zips and guides compared with the designed workbooks.

## 1. Verdict per level

| Level | Print pages / sheets | Verdict | Why |
|---|---|---|---|
| 1 (P1) | 68 / 34 | **GO** | Nothing High or Medium on the printer file. |
| 2 (P2) | 74 / 37 | **GO** | Round-1 p32 clip and orange "take-home" fixed. Weekly zip problem is not a printer problem (see 3.1). |
| 3 (P3) | 70 / 35 | **GO** | Investigation tables fixed. |
| 4 (P4) | 74 / 37 | **GO** | Kit pages fixed; count 76 to 74 verified. |
| 5 (P5) | 62 / 31 | **GO** | Orange text fixed. One Medium (p33 tag text on a dot fill), optional. |
| 6 (P6) | 62 / 31 | **GO** | Round-1 High (cut-out code cards) fixed. |

No High item remains in any printer file. One High remains outside the printer files: the Week 1 student PDFs of Level 2 and Level 6 (3.1).

## 2. Round-1 findings, re-checked on the current files

| Round-1 item | Result | Evidence |
|---|---|---|
| H-A P6 code cards unreadable | **FIXED** | P6 print p57: ten white cards, dashed outline, black text 14 pt or more, a small patterned stripe only on the left. Caption now on two lines, complete. Blank back p58. |
| H-B quote_request L6 58/29 | **FIXED** | Table: 68/34, 74/37, 70/35, 74/37, 62/31, 62/31 = files = `print_spec.json`. |
| H-C dispatch list paths | **FIXED** | `dispatch_list.md` and `dispatch_list_template.csv` point to `outputs/print/bw/...`. |
| N1 orange text ghost (P5, P2) | **FIXED** | No text with luma 0.35 to 0.9 left except the teal 1f7a6f headings (solid in B&W) and grey 666666 running heads. Scan of rendered B&W: no text region with a 10 to 60 percent ink fill apart from P2 p15 "cloth", p20 "R", p49 "red: 64 cm" (all solid enough, Low). "After question n", "take-home", "Make up your own" read clearly (P5 p3, p8, p13 ...; P2 p4). |
| N2 P2 p32 tick labels clipped | **FIXED** | 65c to 100c and $26 to $50 complete. |
| N3 P5 p21 A4 labels | **FIXED** (small Low left) | "7 cm" no longer clipped. The rectangle's "7 cm" sits on the dotted fill and is slightly ghosted (Low). |
| N4 P4 kit pages clipped | **FIXED** | P4 p59 to p73: six columns of cards with right cut line, captions complete, clock page 86 percent, "Bring from home" box complete ("Lessons 7 and 8"). No ink in the 4 mm edge band on any page. |
| N5 P6 Scratch blocks white on hatch | **MOSTLY FIXED** | Blocks on p4, 9, 14, 19, 23, 24, 28, 29, 33, 34, 41, 47 now have black text. Plan blocks "when green flag clicked" (p4, p9) and "set count to" are still on a light hatch with black text: readable (Low). |
| N6 P3 Investigation tables | **FIXED** | P3 p23, 39, 45, 51, 57: white header cells, black text, bordered rows. |
| N7 bw_spec.json and old-count docs | **PARTLY** | `bw_spec.json` now has P1 to P6 (68, 74, 70, 74, 62, 62). `docs/holiday_readiness.md` line 88 still says "Printing 58 to 76 pages" and `docs/product/face_to_face_pilot_plan.md` line 233 still says "P1, 64 print pages" (line 27 and 255 are correct). Low. |
| N8 B&W files not in git | **OPEN** | `.gitignore` lines 28 to 29 still ignore `outputs/print/bw/*.pdf`. The files exist only on this disk. Medium: copy out before sending (SHA-256 in section 6). |
| Low items (thin rule at page top, certificate "Date" wrap, footer 6.4 pt, nearly empty pages, Venn titles, L2 grid pale) | unchanged, still Low | Rule at top of continuation pages: P4 p55 and others. Certificate "Date:" line wraps on L1 p67, L3 p67, L4 p73 and L6 p61. |

Round-1 diagram items (section 2 of round 1) were re-looked at on these pages and are still fixed: L1 p16, p25, p35, p40, p51; L2 p15, p18, p26, p28, p35, p38, p44, p48, p51, p53; L3 p18, p19, p24, p36, p41, p45, p47, p49, p50, p52, p53; P4 p24, p54; P5 p4, p8, p23, p27, p29, p41; P6 p24.

## 3. Remaining issues

### 3.1 High (not in the printer files)

| # | File | Problem | Change |
|---|---|---|---|
| H1 | `p2/Math_Inquirers_P2_Weekly_PDFs.zip`, `Week1_Student_Pages.pdf` (19 pages) and `p6/Math_Inquirers_P6_Weekly_PDFs.zip`, `Week1_Student_Pages.pdf` (13 pages) | The Lesson 1 "Start here" pages are missing. P2: designed workbook pages 3, 4, 5 (digit detectives, digit riddles). P6: designed pages 3, 4 (Code the pattern, Q1 to Q6). The week file starts with the journal, then jumps to the Finish page of Lesson 1. All other pages of all six levels are present (checked page by page against the designed workbooks; only the cover is intentionally not in the zips). Cause: `hp/weekly_level.py` finds a lesson start by the first line matching "Lesson N"; the first Start-here page of those two levels begins with different text. Round 1 reported "none missing"; that was wrong for these two. | Fix the lesson-start detection in `hp/weekly_level.py` for P2 and P6 (start lesson 1 at the page after the journal), rebuild P2 and P6 weekly zips, re-run the page compare. Does not change the printer files. Needed before any family receives the weekly PDFs. |

### 3.2 Medium

| # | File and page | Problem | Change |
|---|---|---|---|
| M1 | P5 B&W p33 (L7 No.2) | Shop A price tag has its data ("$160 before GST", "20% OFF today!", "9% GST added at the till") printed black on a dense dot fill. Readable at 100 dpi, ghosted at 250 dpi. P5 table header rows (p4, p33, p34, p44, p49) are also bold black on a dot fill. | `p5` figure for the tag: use a white fill with a dashed or hatched border; table headers: lighter pattern. Optional, accept if no time. |
| M2 | Printer files not in git (N8) | See above. | Copy out; keep the SHA-256 list. |

### 3.3 Low

- P5 p21: "7 cm" in the rectangle sits on the dot fill (A4 figure).
- P6 hatched plan blocks (p4, p9, p14) and P6 Lesson headers that wrap to three lines (p33 "Lesson / 7", "ANGLES / IN / POLYGONS"; Scratch file name close to the Tool-of-the-day box).
- Footer 6.4 pt on every page; template notes 6.7 to 7.8 pt in L2, L3, L5; P6 code and Python text 7.0 to 7.8 pt; P5 figure text min 7.4 pt (L8 A4). None carries question data except P6 code (7 pt, legible).
- Certificate "Date:" wraps to a second line (L1 p67, L3 p67, L4 p73, L6 p61).
- Nearly empty pages (design): L1 p34, p36, p37, p48, p53; L2 p5, p11, p29, p52; L3 p21, p41, p48, p54; L4 p10, p31, p57; L5 p17, p32; L6 p27, p35, p50, p55. Cut-out content pages are sparse by nature (P4 p61, p63, p69; P5 p55, p57, p59; P6 p59).
- `docs/printing/quote_request.md`: the holiday-workbook part never says that the cut-out pages are meant for cutting (the term-book part does). Add one line, optionally ask for a perforation price.
- Stale counts: `docs/holiday_readiness.md` line 88 ("58 to 76 pages"), `docs/product/face_to_face_pilot_plan.md` line 233 ("P1, 64 print pages").
- Tutor guides carry no workbook page numbers (only "page 1 / page 2" per lesson, still true). P1 and P3 guides (10:33 to 10:34) and P2 (12:44), P4 to P6 (13:10 to 13:11) predate the last workbook rebuilds; their keys did not change (checked: P4 L4 GF5 30 sweets, P4 L1 Q3 3 red 4 blue, P4 L10 15th from the back, P5 Q5 $120/$36, P5 L3 Q2 Siti 48 Mei 36, P6 L5 Q5 20 and 8 with 12 through P, P6 L8 Q3 BFD, P6 L9 Q4 $22).

## 4. Page counts and structure (all agree)

| Level | Designed | Colour print | B&W | `print_spec.json` | `bw_spec.json` | Blank pages (even) | Cut-out front pages |
|---|---|---|---|---|---|---|---|
| 1 | 61 | 68 | 68 | 68 / 34 | 68 | 56, 58 ... 68 (7) | 57, 59, 61, 63, 65, 67 |
| 2 | 66 | 74 | 74 | 74 / 37 | 74 | 60 ... 74 (8) | 59, 61 ... 73 |
| 3 | 63 | 70 | 70 | 70 / 35 | 70 | 58 ... 70 (7) | 59, 61 ... 69 |
| 4 | 65 | 74 | 74 | 74 / 37 | 74 | 58 ... 74 (9) | 59, 61 ... 73 |
| 5 | 57 | 62 | 62 | 62 / 31 | 62 | 54, 56 ... 62 (5) | 53 to 61 odd |
| 6 | 58 | 62 | 62 | 62 / 31 | 62 | 56 ... 62 (4) | 57, 59, 61 |

All A4 (595.9 x 842.9 pt). Colour and B&W have the same blank pages. Every cut-out section starts on an odd page and has a blank back (each cut-out page is followed by a blank page). No blank or near-empty page outside the cut-out and design cases above. No ink in the 4 mm edge band of any B&W page; no off-page text; no text under 6.4 pt (6.4 pt is only the footer). No contents page exists in the holiday workbooks (journal lists lessons without page numbers), so no contents page can be wrong.

## 5. Weekly zips and tutor guides

- Weekly zips (student pages) newer than their workbooks: P1 13:37:43, P2 13:37:46, P3 13:37:50 (workbooks 13:37:15 to 13:37:29), P4 and P5 14:12 (workbooks 13:38), P6 14:12:11 (workbook 14:11:49). Every student page in every zip equals a page of the final workbook (no stale page). Missing pages: H1 only.
- Guides: see Low list; they refer only to "page 1 / page 2" of a lesson, which matches the final layouts of all six levels (checked on P4 L10, P5 L1 to L10, P6 L5, L7 to L9).

## 6. Docs

- `docs/printing/quote_request.md`: counts and files OK for all six levels and the term-book table; kit card table OK (three `_PRINT_BW` files, A5 148 x 210 mm, 2 pages each, verified). Only the Low note above.
- `docs/printing/dispatch_list.md` and `dispatch_list_template.csv`: path now `outputs/print/bw/Math_Inquirers_P<level>_Workbook_PRINT.pdf`; columns agree between the two files.

## 7. Spot-solve (34 changed or risky questions against the printed pages and keys)

All agree; no figure gives the answer away or contradicts it.
P6 L5 No.5 (hatched circle at column 2, row 2 from the bottom; 20 routes, 8 avoiding P; key grid "1 0 1 2" matches); P4 L1 Q3 ("Most packs", 18 and 24: 6 packs, 3 red, 4 blue); P5 L1 No.6 (ticks 2 499 000 to 2 501 000 every 500; circle 2 499 500, 2 500 000, 2 500 499; (b) 2 499 500 and 2 500 499; key matches); P3 L10 No.1 (200 - 150 = 50, Lime juice 50, dashed "?" base); P3 L9 No.5 (1 h 25 min; 4:35 + 50 min = 5:25 pm with two 25-minute hops; line from 7:00 so 9:15 - 1 h 50 = 7:25 pm); P5 L2 No.5 ($120, book $36); P5 L3 No.2 (Siti 48, Mei 36); P5 L3 A1 ($120); P5 L3 A4 (Ben $80); P5 L5 No.3 (27 l, 33 l, 12 cm); P5 L5 No.4 (rise 5 cm, 20 cm); P5 L5 B3 (12 cm); P5 L6 No.1 (9:25 am), No.4 (20 min); P5 L7 No.3 ($100 then $80; Siti wrong); P5 L9 No.3 (8 adult), No.4 (14 fifties), No.5 (15 correct; 80 impossible); P5 L10 No.2 ($63), No.3 (Mei $60, Ravi $55), A1 ($60); P4 L4 GF5 (30 sweets, 42 for 7); P4 L10 No.4 (18 people, 15th from the back), No.5 (a 8 tables of 6, 60 to 90, 77 impossible), No.6 (Ben 10); P4 p24 No.7 (150 pages); P6 L3 No.2 (warmest 3 pm, rise 11, fall 9, midnight -25); P6 L7 No.3 (720 degrees); P6 L8 No.3 (WAY gives BFD); P6 L9 No.1 (mean 6), No.4 (mean $22, median $15, mode $12); P2 L6 No.3 (35c, $24), No.5 ($1.00).

## 8. Printer-pack checklist

Send ONLY these six B&W files (1-bit 600 dpi, A4, duplex, flip on the long edge, left binding, do not scale, do not remove blank pages):

| File (`outputs/print/bw/`) | Pages | Sheets | Cut-out pages (blank back follows each; keep) |
|---|---|---|---|
| `Math_Inquirers_P1_Workbook_PRINT.pdf` | 68 | 34 | 57, 59, 61, 63, 65, 67 |
| `Math_Inquirers_P2_Workbook_PRINT.pdf` | 74 | 37 | 59, 61, 63, 65, 67, 69, 71, 73 |
| `Math_Inquirers_P3_Workbook_PRINT.pdf` | 70 | 35 | 59, 61, 63, 65, 67, 69 |
| `Math_Inquirers_P4_Workbook_PRINT.pdf` | 74 | 37 | 59, 61, 63, 65, 67, 69, 71, 73 |
| `Math_Inquirers_P5_Workbook_PRINT.pdf` | 62 | 31 | 53, 55, 57, 59, 61 |
| `Math_Inquirers_P6_Workbook_PRINT.pdf` | 62 | 31 | 57, 59, 61 |

(In every file the certificate is the last front page, e.g. P4 p73, P6 p61; it has a blank back.)

Do NOT send: the colour files in `outputs/print/` (soft copies), designed PDFs, tutor guides, weekly zips, `outputs/print/bw/term/*` (term books, a different order).
Quantities (`quote_request.md`): 5 to 30 workbooks a week at first; quote bands 1-9, 10-49, 50+; one workbook per parcel (siblings may share); ask for 80 / 100 / 120 gsm prices, spiral or wire-o on the left, cover options (a) none, (b) clear front and card back; one sample each of Level 1 and Level 4 before committing. Staff send one batch a day with `dispatch_list_template.csv` (the `workbook_file` column points into `outputs/print/bw/`).
Inquirer Kit cards (separate A5, 148 x 210 mm, 2 pages, 250 gsm card suggested, B&W): `outputs/kit/Math_Inquirers_Toolbox_Card_A_6-8_PRINT_BW.pdf` (Levels 1 and 2), `..._B_8-10_PRINT_BW.pdf` (Levels 3 and 4), `..._C_10-13_PRINT_BW.pdf` (Levels 5 and 6); 1 per child per workbook plus about 10 percent spare; quote per 50, 100, 250; never the `_SCREEN_colour` files.
Before sending: (1) copy the six B&W files off this disk (N8) and check the SHA-256 below; (2) tell the printer the cut-out pages are for cutting and page 1 is the cover; (3) order the L1 and L4 samples first; (4) fix H1 before families get weekly PDFs.

## 9. SHA-256 (full)

B&W printer files:
- P1 `78b81d7aa77abe36b9bd7d821fd8214f1c444c5cf419a70c213f728414c2345a`
- P2 `f5996738c56156e6be313590949282e32b525b5465165315278a6c7ff18caabf`
- P3 `34de949963cae2fcb558942fceb022c564b38ac0c59583a86bb847c470a33ad1`
- P4 `794e7fffe37f16af10544578418529fe37a2ce08d42c95f8fad0bd3b2bd00d13`
- P5 `6de5f70259ba6ae55b21af34db415c3c134136cf5653ac4b3935171c0a45da7e`
- P6 `4be91216c9eb2e49d627a72fdf7937c7bf36f76727bdf5a25ee0f312f856f382`

Colour print files (soft copy):
- P1 `86b532b231b3fa88f403d0bb12da872d86488ddbe6786226068547f1ad9d739a`
- P2 `81184db0691f3705501a6a49fff8bf5d4a8958d472001995a83c10caa1879aee`
- P3 `926fe961e931f31387121c1142150c78823f90cf273ea88478cff19d9fc20178`
- P4 `7159fe623d464398789902795907b3e7e1c153b91fccf850102be848d73137e4`
- P5 `a13e7a532926b2c892bcb7620726bee640c90ec05a45190246fbd877095cb17c`
- P6 `b7d920dad10011453e2247593ccf80acd4fbc8c3ca3cb6f051d45f45cd630532`

## 10. Limits

B&W files are raster only (no text layer), so text checks were done on the colour files and look checks on the B&W render; the B&W page images were assumed to come from the same colour page (counts, blank pages and visual content agreed on every page viewed). Pages were viewed at about 100 dpi, so small differences in unchanged body text were not read word by word. Not judged on a real printer. No Scratch or Python code was run.
