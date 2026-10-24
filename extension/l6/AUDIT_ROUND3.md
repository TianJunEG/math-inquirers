# Independent audit, round 3: Level 6 Extension Workbook (self-study, with answers, ages 11-13)

Audited 23 Oct 2026, cold read, branch `claude/great-fermi-1hv4vc` (HEAD 5e74989, L6 data and PDFs already committed). Report only: nothing in the book, data, builders or tools was edited; nothing pushed; no PRs. A tutor's real Scratch run is still outstanding and was not part of this check.

## What I did
- Read `AUDIT_ROUND2.md`, `PROGRESS.md`, `README.md`, `TOOL_REQUESTS.md`, `src/whys.py`.
- **Diffed the ten `extension/data/l6_uNN.json` against the commit audited in round 2 (`117023b`), field by field.** The changes are listed in the next section. All other items are byte-identical to the version audited in round 2.
- **Pages read as text** (print vector PDF): 1-7, 13, 16, 20, 23, 27, 48, 52, 63, 69-75, 76-81, 98-100, plus every answer page by script. **Pages viewed as 1-bit images** (the shipped CCITT 600 ppi file, rendered at 100 ppi, zooms at 200 ppi): 1, 3, 4, 7, 13, 20, 27, 48, 72, 74. The colour PDF text-diffed against the print vector: identical apart from the two edition lines on p. 2, line breaks and page-number position.
- **Every Why on the answer pages compared with its question.** All 223 items printed side by side (stem, parts, code, answer, Why) and read. All 60 `whys.py` overrides checked: each equals the explanation in the data file, and all 223 explanations appear verbatim on the answer pages (script). An automatic check that every number in an answer also appears in its Why found nothing unexplained. **No Why is stale; no Why disagrees with its stem or key.**
- **Hand-solved every changed item** (no `l6_lib.py`, no interpreter) and **hand-traced every changed code item** (U10 S10 score game; U10 G1, G2, G3; U10 Learn program; U1 S3 unchanged trace).
- **Sentence frames:** the changed items compared with every sentence of `p6/content/l1..l10.js` by masked-number similarity script, then by reading the holiday items it surfaced (l6 spinner pair, l7 inside-angle items, l9 mini 2, l4 taxi, l3 sea level).
- Answer-page citations: all 223 entries cite a page that holds the question with that number (script plus the printed layout). Contents, pace plan and "answers on page" numbers checked against the pages.

## Items that changed since round 2 (from the data diff)
| Unit, id (printed place) | Change |
|---|---|
| U1 S4 (p. 7 item 3) | text adds "The key to the code blocks is on page 27." |
| U2 Learn (p. 13) | how-to step 5 adds the tests for 4 and 9 |
| U3 Learn example (p. 20) | step 2 rewritten ("move 9 steps left to -12. This jump does not cross 0.") |
| U3 S10 (p. 23 item 11) | sea-level heights replaced by a card game (-35, 48, -6 points; 83, 29, 60) |
| U4 Learn (p. 27) | goal and intro shortened; legend rewritten and extended (set, change, say, ask, repeat, repeat until, if/else, mod, pick random, item, length of list, turn arrow, dashed blank) |
| U5 S3 (p. 35 item 4, answers p. 88) | Why overridden text now matches the chess club (28, 55, 12) |
| U6 S5 (p. 43 item 5, answers p. 90) | Why now matches the multiples-of-3 spinner (4, 8, No) |
| U7 Learn (p. 48) | new step 4: "All the inside angles of a polygon add to sides x 180 - 360" |
| U9 S4 (p. 63 item 4) | test scores replaced by a baker's cakes (34; 40) |
| U10 S1 (p. 70 item 1) | 10, 17, 24, 31 replaced by 8, 14, 20, 26 (6n + 2; 302; 27) |
| U10 S7 (p. 71 item 7; was the "turns 4" turtle) | now "inside angles of 165 each": turn 15, 24 sides |
| U10 S9 (p. 71 item 9, part a; was the clone) | now a 5-day trip, mean 13 km, four given: 12 |
| U10 S13 (p. 72 item 13) | two dice multiplied replaced by two spinners (1-4, 1-3) added: 2, 1/6, 40 |
| U10 G1 (p. 74) | part (a) prints `answer`; "(For your twist...)" dropped from the Why |
| U10 G2 (p. 74) | wording shortened; part (c) now "over 3": 500 (was "greater than 4": 400) |
| U10 C1 (p. 75) | 4, 11, 18, 25 replaced by 3, 7, 11, 15 (4n - 1) |
| U10 Learn example (p. 69) | `answer mod 7 + 1` split into `set r to (answer mod 7)` and `set pos to (r + 1)` |
| U10 list order | items 5 and 6 and the ids S07 to S12 sit in a different list order; content of S2-S6, S8, S10, S11, S12, S14 identical to round 2 |
| Template (all L6 pages) | Contents prints each unit title once; trophy plaque on Mi blanked (cover and Welcome checked) |

## Verdict
**Conditionally sell-ready.** All three Highs from round 2 are closed and checked from the printed pages; every changed item is right by hand; every Why on the answer pages matches its current item; the book is 100 pages in both editions, legible in 1-bit, page numbers are right. **One item the builder was asked to do is only partly done:** the code legend. It was not moved earlier, and Welcome and the pace plan do not point to it; the only pointer is one sentence on U1 item 3 (p. 7) that sends a Unit 1 child forward to the Unit 4 Learn page. This is a Medium, a one-line fix (a sentence on Welcome and on p. 6, or moving the box). If the owner accepts the pointer on p. 7, the book can go on sale now, still subject to the tutor's real Scratch run, a child trial of reading load and pace, the printer proof and removal of the DRAFT licence line.

## Per-item status (round-2 asks)
| # | Ask | Status | Evidence from the pages |
|---|---|---|---|
| H1 | U3 Learn worked example step 2 false sentence | **DONE** | p. 20: "From -3, move 9 steps left to -12. This jump does not cross 0." -8 + 5 = -3, -3 - 9 = -12, check -8 + 5 - 9 = -12. Agrees with the box ("If the jump crosses 0 ... "). Answer page of the Try (-11) unchanged and right. The "-9" arc still runs through the "-12" label (see Low 1); "0." wraps alone onto a second line. |
| H2 | Stale override Whys, U5 item 4 and U6 item 5, and any others | **DONE** | p. 88 item 4 Why: "8 players: 1 + ... + 7 = 28. 11 players: ... 55. 66 = 1 + ... + 11, so there are 12 players." Right for 28, 55, 12. p. 90 item 5: "multiples of 3 up to 12 are 3, 6, 9, 12: Ali 4, Ben the other 8. 4 is not 8: not fair." Right (4/12, 8/12, No). All 60 overrides now equal the data; all 223 Whys read against their stems: none stale. The Why on p. 99 for U10 item 2 mentions 111 (outside 90-110) as before (Low 3). |
| H3 | U10 Start here 8(a) clone | **DONE** | p. 71 item 9(a): "5 days, mean 13 km, 9, 15, 12 and 17 km. On day 5: ___." Hand: 65 - 53 = 12. Not the holiday 4-numbers / mean 15 / 44 / 16 item. (Printed as item 9; the round-2 "8(a)" was the same item by an earlier numbering.) Part (b) median of 15, 4, 9, 12 = 10.5 right. |
| L1 | Code legend moved earlier, or pointed to from Welcome | **NOT DONE (partly)** | Still on p. 27 (U4 Learn). Welcome (p. 3), pace plan (p. 5) and U1 Learn (p. 6) do not mention it. Only pointer: p. 7 item 3, "The key to the code blocks is on page 27." U2 and U3 code items (pp. 14-16, 22-23, 25) have no pointer. |
| L2 | Legend extended with set, change, say, ask-and-wait, length of list, clearer if/else | **DONE in part** | p. 27 now lists set x to, change x by, say x, ask ... and wait, repeat, repeat until, if/else, mod, pick random, item i of, length of list, turn arrow, dashed box. Readable at 200 ppi 1-bit. **Not clearer:** the if/else line is unchanged ("if <test> then / else: choose a part"). The old "answer: what the user typed in" line is gone and "ask ... and wait: gives answer" is terse. See "Can a child read Units 1-3" below. |
| F1 | U10 item 13 (two dice product, odd, 1/4) | **DONE** | p. 72 item 13: two spinners 1-4 and 1-3 added. By hand: 12 results; total 3 = (1,2),(2,1) = 2; 2/12 = 1/6; 240/6 = 40. Different operation, question and answers from holiday l6 (dice product odd 9/36 = 1/4). Residual: a 3-part and a 4-part spinner pair is the holiday l6 challenge set-up (there multiplied, "even wins"). Low. |
| F2 | U10 item 10 (turtle turns 4 at each corner) | **DONE** | p. 71 item 7: "inside angles of 165 each: turn 15, 24 sides" (180 - 165 = 15, 360 / 15 = 24). Different sentence and direction from holiday l7 ("turns 5 at every corner ... sides, inside angle"). Technique is the holiday's worked-example type (174 gives 6 gives 60 sides); type reuse only. |
| F3 | U10 Go further 2(c) ("greater than 4", about 400) | **DONE** | p. 74 item 2(c): "over 3: about ___" = 5/8 x 800 = 500. Part (a) 2/8, (b) 200 (7 and 8 pass), all hand-traced; the block is `if pick random 1 to 8 > 6`. No longer the holiday dice item. |
| F4 | U9 S4 (mean 82 test scores frame) | **DONE (type reuse remains)** | p. 63 item 4: baker, 5 days, mean 40, 35, 52, 38, 41: 200 - 166 = 34; 6th day 40. Story, numbers and sentences new. The structure (missing value, then a further value equal to the mean keeps the mean) is the same as holiday l9 mini 2; and the same missing-value shape now appears in U9 Try, S3, S4, T3, C3 and U10 S9 (see Low 6). |
| F5 | U3 S10 (sea-level heights) | **DONE** | p. 23 item 11: card game scores -35, 48, -6: 48 + 35 = 83 points; -6 - (-35) = 29; 48 + 12 = 60. No holiday echo found (no "sea level", cave, boat, diver). |
| F6 | U10 Go further 1 (n vs answer; twist line) | **DONE** | p. 74: block prints `say (answer x ? + ?)`, part (a) is `say (answer x [] + [])`. Why no longer ends with "(For your twist ...)". Hand: 7 at 2 km, 16 at 5 km: +9 for 3 km = 3 per km, 7 = 6 + 1: 3n + 1; 20 km = 61; 49 = 3n + 1 gives 16. A taxi theme also appears in holiday l4 ($4 start plus $2 a km, n km, $30) but with a given rule and different task; not a clone. |
| F7 | U2 Learn must teach divisibility tests for 4 and 9 | **DONE** | p. 13 step 5: "Last 2 digits in the 4 times table mean 4 is a factor. Digits adding to a multiple of 9 mean 9 is a factor." p. 16 item 8: 372 (72 in the 4 times table) Yes; 2457 (digit sum 18) Yes for 3; 6835 (digit sum 22) No for 9. All agree with the key. Step 5 is dense but legible. |
| F8 | U7 T2 hint: inside-angle sum | **DONE** | p. 48 Learn step 4: "All the inside angles of a polygon add to sides x 180 - 360." p. 52 T2 hint "What do the inside angles of an n-sided shape add up to?" is now answerable from the Learn page. Hand: 2340 = n x 180 - 360 gives n = 15; each inside angle 156; turn 24. Key agrees. |
| Lows | (see below) | **Mostly DONE** | See table below. |

### Lows asked for
| Low | Status |
|---|---|
| Contents prints each title once | **DONE** (p. 4 viewed: "Code the pattern / follows Holiday Program Lesson 1 . answers on page 80"). |
| Blank trophy plaque | **DONE** (cover p. 1 and Welcome p. 3 viewed: "Mi" on the shirt only, no garbled plaque text; Mi's desk is close to the intro sentence but does not touch it). |
| U10 Learn `answer mod 7 + 1` unbracketed | **DONE** (two blocks: `set r to (answer mod 7)`, `set pos to (r + 1)`; Learn step 3 says the same; hand: 10 gives r 3, pos 4, Thursday; 19 gives r 5, pos 6, Saturday, key agrees). |
| U10 G1 twist line | **DONE** (see F6). |
| U3 "-9" arc over the "-12" label | **NOT DONE** (p. 20 viewed: the arc still crosses the "-12" tick label). |
| U10 S2 Why lists 111 (outside 90-110) | **NOT DONE** (Why p. 98 unchanged). |
| U2 T1 / G1(c) "no smaller number" | **NOT DONE** (unchanged; true, just asserted). |
| U9 T3 and G3 hints state the method | **NOT DONE** (unchanged, Low). |
| Difference 7 recurs | **Partly**: U10 S1 (was 7n + 3) and C1 (was 7n - 3) changed; U1 Try (7n - 4), U1 C1 (7n + 2) and U1 S8 (+$7) remain. |
| Page 78 blank | Unchanged: blank in both editions; the reason (answers start on a right-hand page) is explained in the README but nothing is printed on the page. Fine in a bound book. |
| Tone (dolphin, "Nearly there. You can do it.") | Unchanged, Low. |

## Can a child read every kind of block used in Units 1-3?
Block kinds used in Units 1-3 (from the data): `when green flag clicked`, `set x to`, `change x by`, `say x`, `say x for 1 seconds`, `repeat n`, `repeat until <x > n>`, `repeat until <n mod d = 0>`, `if <n mod d = 0> then`, `if <a > b> then ... else`, and the label "Program Q".
- Explained on p. 27: set, change, say, repeat, repeat until, if/else (tersely), mod. "say x for 1 seconds" is the same as "say x" except for the pause: a child will cope.
- **Not explained anywhere:** `when green flag clicked` (a start block; obvious to a Scratch child, not to a beginner), the comparison signs `>` in `repeat until <x > 40>` and `if <a > b>`, and the "Program Q" label (the item text says it).
- **Position:** the first code item a child meets is p. 7 item 3 (and p. 6's Learn text mentions a loop in words). The key is 20 pages ahead on a page for another unit. Because p. 7 says "on page 27", a child can find it; but p. 3 (Welcome), p. 5 (pace plan) and p. 6 do not tell the child that a key exists, and the later code items in Units 2 and 3 do not point to it.
- Judgement: a determined child can read Units 1-3, helped by the item stems (U1 S4 explains "says x first, then changes it"; U3 S7 "changes x, then says it"; U3 T2 explains the stop rule; U2 G3 "looks for the smallest factor"). A child who has never seen code will hit `repeat until` and `if/else` on pp. 11, 14, 22, 24 and 25 before p. 27 unless they find the one pointer. Recommended: add "Code blocks are explained on page 27" to Welcome ("For the grown-up" or "How to use this book") and to p. 6, and add one line for `when green flag clicked` and `>`; or move the box to p. 6.

## Hand-solving and hand-trace record (changed items)
- U3 Learn: -8 + 5 = -3; -3 - 9 = -12. U3 S10: 48 - (-35) = 83; -6 - (-35) = 29; 48 + 12 = 60.
- U9 S4: 5 x 40 = 200; 35 + 52 + 38 + 41 = 166; 34; a 6th day of 40 keeps the mean at 40 (240 / 6 = 40). U10 S9: 65 - 53 = 12; sorted 4, 9, 12, 15: median 10.5.
- U10 S1: 6n + 2; 6 x 50 + 2 = 302; 6n = 162, n = 27. S7: turn 15, 24 sides. S13: 2/12 = 1/6; 240 / 6 = 40. S8 unchanged: 4 + 75 = 79 mod 12 = 7; MATH + 9 = VJCQ. S12 unchanged: 11 + 25 x 6 = 161, term 26, rule 6n + 5.
- U10 S10 (score game, p. 72): rounds give 42, 34, 26, 18 -> reset to 50 (round 4); 42 (5), 34 (6), 26 (7), 18 -> 50 (8). After round 6: 34; first reset after round 4; says 50. Key 34, 4, 50 correct. The `if` is drawn inside the `repeat` and the `set score to 50` inside the `if` (p. 72 viewed).
- U10 G1: 3n + 1, 61, 16. G2: 2, 200, 500. G3 (unchanged): n = 6: 6, 3, 10, 5, 16, 8, 4, 2, 1 is 8 steps; n = 7: 16 steps, maximum 52. Key agrees.
- U10 C1 3, 7, 11, 15: 4n - 1. Other U10 items (S2 to S6, S8, S10 to S14, T1 to T3, C2 to C4, Learn Try) re-solved: all agree with the key.
- U2 S6 (4 and 9 tests): 72 is 4 x 18 Yes; 18 is a multiple of 3 Yes; 22 is not a multiple of 9 No. U7 T2: n = 15, 156, 24.
- No answer of the 223 differs from the printed key.

## Welcome, Beyond, contents, page counts, blank page
- **Welcome (p. 3):** no real-size or ruler line; "Beyond Level 6 is ahead of school. You may skip it." present; Mi at the desk is clear of the text; no overflow. **No pointer to the code key** (L1).
- **Beyond badge:** "Beyond Level 6: title" is printed in the frame of 17 items (units 1 to 9; U10 has none, correct).
- **Contents (p. 4):** pages 6, 13, 20, 27, 34, 41, 48, 55, 62, 69, My progress 76, certificate 77, Answers 79 all match; "answers on page" 80, 82, 84, 86, 88, 90, 92, 94, 96, 98 match where each unit's answers start. Pace plan (p. 5) page ranges match the units.
- **Page count:** 100 pages in the print 1-bit, the print vector and the soft copy. `build_report.json`: 200 pages in the two editions, none over, lowest fill 0.86 (print p. 15), no problems, B/W check 0 failures.
- **Page 78:** blank in both editions (no text, no number), the left page behind the certificate so that Answers opens on a right-hand page. Explained in `README.md`; not printed. Fine.
- **Answer pages:** 21 pages (80 to 100), 223 entries (22 per unit, 25 in unit 10). Every entry cites the page of its question.
- **1-bit legibility of changed pages (viewed):** p. 20 (number line labels, one arc over the "-12" label), p. 27 (legend about 11 pt, clear at 200 ppi), p. 72 (score code, small `<` between "score" and "20" clear), p. 74 (all three code figures clear; `n / 2` and `n x 3 + 1` legible; the question marks in `answer x ? + ?` legible), p. 13 and p. 48 text clear. p. 7, 3, 4 and 1 fine.

## New findings
No new High. No new wrong answer, no stale Why.
**Medium**
1. **Code key is still 20 pages after the first code item and Welcome does not point to it** (L1 above); the if/else line is not clearer, and `when green flag clicked` and `>` are not explained.
2. `PROGRESS.md` is not updated for the round-2 fixes (it still says "code legend on the unit 4 Learn page" and lists no round-2 changes; `README.md` has them).

**Low**
3. U10 S2 Why (p. 98) names 111, outside the range asked (90 to 110).
4. p. 20: "-9" arc crosses the "-12" label; "0." wraps onto its own line.
5. U10 S12 (p. 71 item 10, unchanged) shares a frame with holiday l3: "set n to 10, then repeat 5 times: change n by -4. Then say n."; the L6 version is "set n to 11, then repeat 25 times: change n by 6. Then it says n." Numbers, size and questions differ.
6. The "mean, N given values, find the last, then add a value" shape now recurs six times (U9 Try, S3, S4, T3, U10 S9, U9 C3); U9 S8 still says "stickers". Vary one or two if the owner wants.
7. U10 S13 uses a 3-part and a 4-part spinner like holiday l6 (operation and questions differ).

## Remaining items, in order
1. Add one line to Welcome and p. 6 ("Code blocks are explained on page 27") and one line for `when green flag clicked` and `>`; optionally reword if/else ("if the test is true, do the first part; if not, do the else part"). Rebuild.
2. Update `PROGRESS.md`.
3. Low 3 and 4 (111; the arc), at the owner's choice.
4. Not for the author: tutor's real Scratch run (my hand traces prove the answers, not that every block exists and behaves identically in Scratch), child trial of reading load and the "20 to 25 minutes" pace (M6 from round 2 remains open for this reason), owner review of tier difficulty, printer proof, owner/lawyer removal of the DRAFT licence line.
