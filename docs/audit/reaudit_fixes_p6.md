# Level 6 fixes after the re-audit (wording and content only)

Date 2026-10-22. Source: `docs/audit/reaudit_p6.md`. Nothing committed. Every changed answer was checked in Python (simulation or brute force); see "Verified" below.

## Items fixed (old -> new)

| # | Item | Old | New |
|---|---|---|---|
| 1 | Looking back (`p6/workbook_html.js` finish page, every lesson) | did well / hardest part / what helped | adds a third line "Next time I could try", still optional ("write pass for any line"). Tutor guide line (`p6/guide.js`, Looking back) now lists it. |
| 2a | Bank L1 Challenge X1 (Core-level squares) | tiles in pattern 10 and 11 | "Rule 5n + 2, every 4th term circled: first three circled terms, constant difference?, rule for the mth circled term, 50th circled term". Answer 22, 42, 62; difference 20; 20m + 2; 1002. |
| 2b | Bank L2 Challenge X1 (largest prime below 200) | one more prime test | "Smallest number with exactly 8 factors, then the smallest ODD one, and why is it bigger". 24 and 105. |
| 2c | Bank L3 X3 (6 repeats of -30) | single step | "Start x = 200, repeat until x < -100 [change x by 50, -80]: repeats and final x; what start gives exactly -100 after 8 repeats". 11 repeats, x = -130; start 140. |
| 2d | Bank L3 X4 (`-3-4` vs `-3-(-4)`) | one subtraction | "Ali: subtracting a negative always gives a bigger answer. Test on 3 examples, justify with a number line, what about subtracting a positive". |
| 2e | Bank L10 X4 (50 as sum of two primes) | repeat of the L2 idea | "nth term 4n + 1: all prime terms among the first 15, is any term even, explain". Primes 5, 13, 17, 29, 37, 41, 53, 61; none even. |
| 2f | Core code notation: L1 C5, L4 C6, L7 C2 (and L7 C4 for the same symbol) | bare code | each block is glossed in plain words in the item ("set n to 10 means n starts as 10", "answer is what you typed", "turn ↻ 60 turns right, clockwise, by 60 degrees"). Answers unchanged. |
| 2g | Start here, Lesson 7 (entirely post-teaching) | table first | New "Try it first" box above Q1: walk a square on the floor (or draw it), count quarter turns, total degrees (4 and 360). No tools, no formula. Key (tutor guide) and the deck `ws1` note include it. Page 1 re-fitted (table rows and Ben's drawing frame made slightly smaller) so the page count is unchanged. |
| 2h | Start here items that depended on teaching (scaffolds only, answers unchanged) | | L1 Q2 hint "the 100th term is 99 jumps after the 1st"; L1 Q3 "each term is 4 more than the one before"; L2 Q3 "6 mod d = left over"; L5 Q6 hint that each handshake is counted once (a smaller than b); L6 Q5 "a die shows 1 to 6; a double is both dice the same"; L8 Q5 worked example "shift 2 then shift 3 is shift 5". |
| 3 | Lesson 10 timing | guide "showcase 62-87, 3 minutes each plus 20 s; exit 87-90" vs deck 62-85, 2:30 | Guide now matches the deck: showcase 62-85 (two rounds of 4, 2:30 each plus a 20 s switch, 8 x 2:50 = 22:40), talk 85-86, exit slip 86-88, looking back and certificates 88-90. The guide's earlier blocks also matched to the deck: challenge round 8-23, starter projects 23-30, break 30-32. Total stays 90 minutes. |
| 4a | "mean" -> MOE term "average" (L9) | "mean" only | "average (mean)" introduced once in the deck title line, the key-idea slide, the hook script and workbook Q1(b). Later uses stay "mean". |
| 4b | `p6/SPEC.md` stale "children know ... rate and speed" | speed listed | "ratio and rate". The phrase does not appear in the printed PDFs. |
| 4c | "beyond the syllabus" | | not found in any Level 6 printed text (guide, content, workbook). No change needed. No syllabus-alignment claim added. |

## Verified (Python, exact)
L1 X1: terms 22, 42, 62, diff 20, 50th circled = 1002. L2 X1: smallest with 8 factors 24, smallest odd 105 (next odd 135) by brute force to 500. L3 X3: simulation gives 11 repeats and x = -130; 8 repeats from x = 140 gives -100. L3 X4 examples checked. L10 X4: prime terms of 4n + 1 for n = 1..15 brute-forced.

## Not fixed, and why
- Start-here items that are the taught method (L1 Q2/Q3, L7 Q2/Q4/Q5, L8 Q5, L6 Q2, L9 Q2/Q4, L10 Q2-Q6) still need the lesson; I added scaffolds, not replacements, because the pages are full to the line and replacing items would change keys, deck answer slides and the weekly packs. Moving the L7 star formula to Think harder was not done for the same reason.
- Scratch starter files and the pre-lesson handout: lead is planning those.
- Pacing, check-together slot for Think harder, L9 revision load, L10 showcase opt-out printed on the child page (timing audit running).
- Reflect slide in the decks (slidekit) does not name the new line; shared file, not edited.

## Diagnostic or shared-file issues seen (not edited)
- `diag/content/p6.json` still carries `notes.placement`, `mainNote`, etc. that the unified build ignores; the "warm-up decides" claim is false in the shipped PDF.
- Diagnostic key still says "for example 2.05 and $2.05"; "Open to a year either side" header; "Skills covered" list; the 0-1 row offers only Level 5 (no age note for a 13-year-old).
- `docs/levels_and_placement.md` (70% / 40-69% / under 40%) disagrees with the shipped rule.
- Question bank, taster and learner pages still say "Ages 11-13 (finishing P6)" while the diagnostics say "after the PSLE" (`levels/` and `diag/` text).
- `hp/common_html.js` `H.p` escapes strings; HTML boxes must be passed as arrays (noted for other authors).

## Rebuilt and final page counts
Decks: `rebuild/gen_p6l1..10.py` then `levels/restyle.py split/p6lK` (all ten). Printed: `bash levels/build_level.sh 6`, `python3 levels/mkextras.py 6` (self-check OK).

| File | Pages (before -> after) |
|---|---|
| Student workbook | 55 -> 55 |
| Tutor guide | 102 -> 102 |
| Weekly dose | 25 -> 25 |
| Question bank | 28 -> 29 (longer glossed Core items and new Challenge items) |
| Weekly email pack | 12 -> 12 |
| Free taster | 5 -> 5 |
| What learners get | 1 -> 1 |
