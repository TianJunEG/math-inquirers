# Level 1 extension book: audit 4 (licence page and copy check), 23 Oct 2026

## Licence / contact page (build.py, `licence()`)
- Registered office placeholder replaced with "66 Tannery Ln, Singapore 347805" (owner decision). Copyright line already read "Preciouslyours Pte Ltd ... trading as Math Inquirers" (publisher line). Email stays pypteltd@gmail.com. The DRAFT licence line stays until a lawyer approves (annual licence term is the school-book decision; this personal-use licence text is unchanged).
- grep for "owner to add" in extension/: only historical audit notes remain (AUDIT.md, AUDIT_2.md, NOTES.md line 13 is now stale for the address, left for the owner/other agents; not a printed page).
- Rebuilt Level 1. `extension/verify_all.sh 1`: ALL GATES PASSED. Pages 98 (even) in colour and B&W. Pages 3-4 (contents) text identical before and after; answer pages unchanged (only the p2 text changed). Page 2 and page 8 viewed in colour and B&W: p2 Contact box wraps to 2 lines and fits; p8 unchanged.

## External duplicate gate (extension/verify/dup_check.py --level 1)
- Private sources were present and used: external corpus 48 files, 519,102 7-word runs (docs/books/private_*, docs/sasmo/private_*); holiday corpus 5 files; own term lessons 40 files.
- 247 question texts checked. FAIL: 0 (no shared 7-word run with holiday or external sources). External check truly ran (the "NOT run" warning did not appear).
- 16 WARN lines (shared 7-word runs with our own term lessons, e.g. U01-S12, U02-S01, U05-S11, U09-S07): own text, shared phrasing only, allowed by the gate.
- 23 REVIEW (skeleton) items, read by hand: L1U01-L01, S04, S05, S13, T01, T02; L1U02-S02, S06, S07, T03; L1U05-example, S10, T02, G02; L1U06-S12; L1U08-S11, C03; L1U09-example, S03, S04, T02; L1U10-S13, C03.
  Verdict: all 23 ORIGINAL. They match the holiday bank only as short generic frames (fill-in-the-blanks, "starts on N and hops M", "N cubes long", change from a coin, "between N and M"), each with new numbers and different questions or extra parts; none is a distinctive sentence.
- Extra check beyond the tool: the same masked-digit skeleton test (6-word runs) against the EXTERNAL private sources. Hits were all generic frames (blank-filling rows, "a number is between # and #", "each picture stands for # stickers", "how many ... altogether"), longest contiguous run 9 to 11 tokens, mostly bare number slots. Items hit: U01-S04/S05/S10/C02/C04, U02-S02/S03/S06/S09/S10/G01/G03, U03-S02/G03/C03, U04-S01/G01, U05-L01/S10/S12/G02, U06-S09/S12/T02, U08-S05/S10/S11/C03, U09-S10/G03, U10-S01/S03. Verdict: all ORIGINAL (generic stems, different contexts, numbers and structure).

## Fixes
None needed. No data json or check was changed; no source text was copied into any committed file.
