# Weekly student PDFs: Lesson 1 "Start here" fix (H1 of the round-2 print readiness report)

## Reproduction and root cause
`hp/weekly_level.py` found the start of each lesson as the first designed-workbook page whose first non-empty line (from `pdftotext -layout`) matches `Lesson N`. Two things break that:

- P2 p3 and P6 p3: with `-layout` the first line is a side banner ("START HERE. After question 3 ..." in P2, "SEQUENCES" in P6), so the label "Lesson 1" is not first. Lesson 1 then started at its Finish page (P2 p6, P6 p5), and designed pages 3 to 5 (P2) and 3 to 4 (P6) were dropped from Week 1.
- Found while comparing (same cause, not listed in the report): P6 Lesson 3 start page (p13) prints "NEGATIVE NUMBERS" before "Lesson 3". It was put in Week 1 and the Week 2 file began at the Finish page. Old P6 Week 2 had 8 pages, Week 3 had 13.

## Fix (hp/weekly_level.py only; no printed workbook or print file is touched)
The start of lesson N is the first page, other than the journal, whose first six non-empty lines in reading order (`pdftotext` without `-layout`, joined) contain `Lesson N`. About 10 lines changed, in the lesson-start loop only.

## Rebuild and comparison
All six zips were rebuilt with `weekly_level.py` from the current designed workbooks and tutor guides (P1 uses `hp/` and `outputs/designed/Math_Inquirers_Weekly_PDFs.zip`). For every weekly student PDF, each page's text (whitespace-normalised, pdftotext) was matched exactly to a designed workbook page; page counts match the ranges below; every page matched one workbook page, none twice. Union of the five weeks = every designed page except p1 (cover, intentionally not in the zips). Journal is p2, kit/cut-outs and extra pages go to Week 1, the certificate (last page) to Week 5.

| Level (designed pages) | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 (61) | 3-7 | 8-12 | 13-17 | 18-23 | 24-28 | 29-33 | 34-39 | 40-44 | 45-50 | 51-55 |
| P2 (66) | 3-8 | 9-14 | 15-19 | 20-24 | 25-30 | 31-36 | 37-42 | 43-47 | 48-53 | 54-58 |
| P3 (63) | 3-7 | 8-12 | 13-17 | 18-23 | 24-28 | 29-33 | 34-39 | 40-45 | 46-51 | 52-57 |
| P4 (65) | 3-8 | 9-14 | 15-19 | 20-24 | 25-29 | 30-37 | 38-42 | 43-47 | 48-52 | 53-57 |
| P5 (57) | 3-7 | 8-12 | 13-17 | 18-22 | 23-27 | 28-32 | 33-37 | 38-42 | 43-47 | 48-52 |
| P6 (58) | 3-7 | 8-12 | 13-17 | 18-22 | 23-27 | 28-32 | 33-38 | 39-44 | 45-50 | 51-55 |

Weekly student PDFs (pages = designed workbook pages; Week 1 = journal p2 + L1-L2 + kit; Week 5 = L9-L10 + certificate):

| Level | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 |
|---|---|---|---|---|---|
| P1 | 16 = 2-12, 56-60 | 11 = 13-23 | 10 = 24-33 | 11 = 34-44 | 12 = 45-55, 61 |
| P2 | 20 = 2-14, 59-65 | 10 = 15-24 | 12 = 25-36 | 11 = 37-47 | 12 = 48-58, 66 |
| P3 | 16 = 2-12, 58-62 | 11 = 13-23 | 10 = 24-33 | 12 = 34-45 | 13 = 46-57, 63 |
| P4 | 20 = 2-14, 58-64 | 10 = 15-24 | 13 = 25-37 | 10 = 38-47 | 11 = 48-57, 65 |
| P5 | 15 = 2-12, 53-56 | 10 = 13-22 | 10 = 23-32 | 10 = 33-42 | 11 = 43-52, 57 |
| P6 | 13 = 2-12, 56-57 | 10 = 13-22 | 10 = 23-32 | 12 = 33-44 | 12 = 45-55, 58 |

Result of the compare: all 30 weekly PDFs match, no designed page missing or duplicated (cover excluded).

## What changed against the zips in git
- P2: Week 1 19 to 20 pages (the missing Start-here pages back; the old file also lacked pages elsewhere, the old zip was older than the current workbook). Weeks 3, 4, 5 also changed (13/10/10 to 12/11/12).
- P6: Week 2 8 to 10, Week 3 13 to 10, Week 5 9 to 12 (Lesson 3 start page moved to Week 2; Week 5 was short in the old zip). Week 1 13 pages (Lesson 1 Start here back, Lesson 3 pages out).
- P1: the tracked zip (`outputs/designed/Math_Inquirers_Weekly_PDFs.zip`) was stale against the current workbook (Week 1 12, Week 3 12, Week 5 14 pages; now 16, 10, 12). It is rebuilt.
- P3, P4, P5: rebuilt output is text-identical to the tracked zips, so the tracked files were left as they are.
- Tutor-script PDFs are unchanged in every level.

## Check by eye
Week 1 of P2: page 2 is "Lesson 1 NUMBERS TO 1000 / Digit detectives" (Start here, workbook page 3); P6: page 2 is "Lesson 1 / Code the pattern" (workbook page 3). Both follow the journal on page 1.

## Other fixes in this pass
- `docs/holiday_readiness.md` line 88: "58 to 76 pages" to "62 to 74 pages (68 / 74 / 70 / 74 / 62 / 62 for Levels 1 to 6)".
- `docs/product/face_to_face_pilot_plan.md` line 233: "P1, 64 print pages" to "P1, 68 print pages".
- `docs/printing/quote_request.md` (holiday-workbook part): one line telling the printer the cut-out pages are for cutting out, with page numbers by level (from the readiness report: L1 57-67 odd, L2 59-73 odd, L3 59-69 odd, L4 59-73 odd, L5 53-61 odd, L6 57-61 odd; blank back follows each).
