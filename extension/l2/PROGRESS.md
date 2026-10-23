# Level 2 extension workbook: progress

Status: ALL TEN UNITS DONE. Full build and all gates passed (see below). Nothing remains except audits and owner decisions.

| Unit | Title | Items (S / T / G / C) | Status |
|---|---|---|---|
| 1 | Digit detectives | 11 / 3 / 4 / 4 | done: data, checks, gates, pages viewed, committed |
| 2 | Missing digit mysteries | 11 / 3 / 4 / 4 | done |
| 3 | Legs, wheels and arrays | 10 / 3 / 4 / 4 | done |
| 4 | Pattern machines | 10 / 3 / 4 / 4 | done |
| 5 | Mystery number machines | 10 / 3 / 4 / 4 | done |
| 6 | Market day | 10 / 3 / 4 / 4 | done |
| 7 | Fair shares | 9 / 3 / 4 / 4 | done |
| 8 | Shape builders | 10 / 3 / 4 / 4 | done |
| 9 | Measure masters | 11 / 3 / 4 / 4 | done |
| 10 | Puzzle day | 10 / 3 / 4 / 4 | done |

Final gates (last full run): run_checks 493 answers, 0 mismatches; dup_check OK (REVIEW list read, see AUDIT_NOTES.md); wording_lint 0 errors; bw_check and print/check_bw OK; fill_check OK; page count soft 100, print 100 (even); contents and answer page numbers match the PDF.

## Issues and notes
- Page count is exactly 100. To get there the 27 longest "Why" lines were shortened (the book was 102 pages). Any addition needs a matching cut (plan decision D12: 6 pages per unit).
- The beyond label prints "Beyond Level 1" (shared renderer); see TOOL_REQUESTS.md.
- The shared lint forbids the word "price": the money unit says "cost" and "tag".
- Start here has 9 to 11 items per unit (plan: 13 to 14). At the Level 2 type size and with figures, 9 to 11 items fill three pages; adding more overflows (fill_check). Total 212 items plus 10 Try items.
- Items that are close in structure to a holiday item are listed in AUDIT_NOTES.md section 2.
- The scratchpad folder is shared with other agents; this agent's scratch files are under scratchpad/l2w.

## If work must resume
Edit `extension/l2/author/uNN.py`, run it, update `extension/verify/l2_uNN_checks.py` (ids follow printed order), then `python3 extension/tools/build.py --level 2 --units N --no-bw --out <scratch>` for a quick view and the full gate list in README.md.
