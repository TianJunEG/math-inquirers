# Final fixes, Levels 1 to 4 and shared files (23 Oct 2026)

Scope: the "remaining 10%" from `docs/holiday_readiness.md` sections 2 to 5 for Levels 1 to 4 and the shared diagnostic and scheme files. Nothing pushed. Levels 5 and 6, `term/`, `school/`, `website/` untouched. No child has used any of this material; all timing is still modelled.

## Level 1

| Finding | Action |
|---|---|
| Bank Think harder / Challenge residue (L1 #8-9, L2 #1-3 and #8-12, plus the other flat items on the re-audit list) | 20 bank items in `hp/qbank.json` replaced by items that need the lesson idea in a new setting (a claim to test, an error to find, a "does it ever" question, a table, a short list-all). Printed T1-T4 and C1-C3, slides, bank, guide, Weekly Dose rebuilt from the same file. Hand checks: 50, 44 ... 2 never reaches 0; circle 5, square 2; apple 5 to 9 pictures (7 graphs); back-track 17; 4 ways 6+4 ... 9+1. |
| Go further with no diagram | New `rebuild/p1chdiag.py` draws a "Go further: see it" picture slide (`lN-chdiag`) for the three printed Go further items of every lesson (problem shown, never the answer), after `lN-challenge`, optional. All 10 decks rebuilt. |
| Lesson 10 titled "Challenge Day" | Renamed "Puzzle Day" in `hp/lessons.js` and every L1 output (guide, workbook kit card, deck titles, tutor console data). Also renamed in Levels 2 to 4 (`p2..p4/content/l10.js`, `l9.js` close line, SPEC, decks) so Levels 1 to 4 agree. Level 5 still says Challenge Day (not my scope). |
| `hp/trial6.js` wording | "Show me" now means show only the tutor, board held low, nobody holds a board up before the class. Trial docx/pdf rebuilt. |
| Reading load of the heaviest Core pages | Wording of the page-3 header and Lesson 9 Q2 / Lesson 2 Q5 hint shortened. After the fix the most word-heavy Start here page has about 140 real words (the high pdftotext counts, 200+, are blanks and digits). Left at that: pages are mostly numerals. |
| Layout defect found while viewing: Lesson 5 Q3 text outside its box (indented hint / clue lines closed the question box in about 25 places, Levels 1 workbook) | `hp/wb_pdf.py` now keeps indented plain paragraphs inside the open question box. Workbook still 58 pages; viewed contact sheet of pages 3 to 52 and page 24. Not applied to P2 to P4 (their pages look correct and a change could move page counts). |
| One 4-minute break for 6 to 8 year olds | Added a 30-second "stand, stretch, sit" reset after the page-1 check (slide chip on `l1-ws1ans`, tutor script, time plan text). Taken from the 2-minute check slot, so no clock boundary moves; every lesson budget still sums to 90 (`hp/budget.json`). Optional: skip if more than a minute behind. A real pilot is still the only test. |

## Level 2

| Finding | Action |
|---|---|
| Stranded "Fraction strips" heading on kit page 60 | `p2/kit.js`: page break before the heading. Strips now start with their heading on page 61 (viewed). Page count still 66; print spec 74 pages, unchanged. |
| Q5 triangle (b) had no question line | Added "Each side adds up to 420. Fill in the second triangle. Which numbers are in the corners?" (`p2/content/l2.js`; viewed, page 11; page count unchanged). |
| 8 near-Core Think harder bank items, Go further C1 one technique | These two audit entries were about the Level 1 Lesson 2 bank (L1 L2 #1-3, #8-12) and its magic-triangle Go further C1; fixed under Level 1 above (C1 is now "two circles and a square", a two-equation puzzle; C3 keeps the magic triangle with new numbers). In the Level 2 bank, Lesson 4 Challenge C1 (lights every 3 and 5 seconds, a re-skin of Core Q6 and a Level 3 idea) replaced by the "up 5 then up 1" pattern: says 50 but never 51 (checked). |
| Diagnostic wording ("a.m./p.m.", hidden "5?") | Shared files; see below. |

## Level 3

| Finding | Action |
|---|---|
| `split/p3l9` orphan slides showing "a.m." | Checked every deck: no orphan or missing slide files in any `split/*/deck.json` order; no "a.m." in `split/p3l9`. Nothing to delete. |
| "(finishing P3)" in `levels/mkextras.py` and `levels/scheme.py` | `mkextras.py` already used "builds on Primary N maths" (HEAD). `levels/scheme.py` now says "ages 6 to 8 (builds on Primary 1 maths)" ... "ages 11 to 13, after the PSLE". Level guides P2, P3, P4 and their SPEC files changed from "children finishing Primary N" to the same age plus "builds on" wording. Schemes of work rebuilt. |

## Level 4

| Finding | Action |
|---|---|
| Lesson 3 (order of operations, a P5 preview) and Lesson 6 angle items must be labelled stretch beyond P4 | `p4/guide.js`: new "Syllabus" row in the overview and a "Syllabus note" row in Lessons 3 and 6 ("stretch beyond P4 ... never describe as P4-aligned"; clock-hand and compass turns are enrichment). Guide docx and pdf rebuilt (text found twice in the pdf). |
| Challenge C1 re-skin | The "C1 re-skin of Core Q6 (lights every 3 and 5 seconds)" in the audit is the Level 2 Lesson 4 item (reaudit_fixes_p2.md); fixed there (see Level 2). I found no matching Level 4 item in the Level 4 audits. |

## Shared files

| Finding | Action |
|---|---|
| `diag/build_diag.py` never printed `childNote`, `tutorKey` | `childNote` printed in the "How it works" card; `tutorKey` printed as a "Tutor note" on the Tutor Key (new text in `diag/content/p1..p6.json`). All 12 diagnostic PDFs rebuilt. |
| "$2.05" header ("2.05 and $2.05") | Key header now: "70 cents and 70c" (Level 1) or with "3/4 and three quarters" (Levels 2 to 6). Verified none of the 6 keys still contains it. |
| "Open to a year either side" | Not in the rebuilt placement checks (0 matches in all six); `docs/levels_and_placement.md` says there is no year-either-side rule. |
| `levels/scheme.py` "Think Harder pages (stretch and challenge)" | Now "2-page Start here worksheet, then Think harder, Go further and an Investigation with a Look-back (printed for every child, who may choose any of them; nobody is placed in a group)". |
| `docs/levels_and_placement.md` thresholds | Score defined as 4 warm-up + 6 main out of 10, so each mark is 10%; 7-10 / 4-6 / 0-3 / 9-10 level-up identical in `diag/build_diag.py`, `levels/mkextras.py` and the doc. Website files not edited. |

## Rebuilt and checked

Rebuilt: Level 1 to 4 workbooks, print PDFs (`print_spec.json`: 64, 74, 64, 76 pages, unchanged), tutor guides, Weekly PDFs, Weekly Dose, question banks, schemes, decks (`split/l1..l10` and the L10 titles in p2l10, p3l10, p4l10), diagnostics 1 to 6, tutor console data for Levels 1 to 4.
Scripts run: `verify_close_gaps_p1` (41 passed), `verify_close_gaps_p4`, `verify_gifted_p4`, `verify_fixpass_p3`, `verify_gifted_p3` all pass. `verify_fixpass_p1` and `verify_fixpass_p4` fail on checks that were already stale at HEAD (a "scoring" key and "diag minutes 40" that the diagnostic JSON no longer carries; the placement rule moved to 30 minutes). Not edited.

## Left, and why

* Pace and timing for 6 to 8 year olds: only a pilot with a child shows it.
* P2 to P4 `wb_pdf.py` not given the box fix (see Level 1).
* Level 5 "Challenge Day" title, Level 5 and 6 items: other agent.
* Owner decision: whether Levels 2 to 4 should also say "Puzzle Day" (done here for consistency; revert is three small edits per level).
