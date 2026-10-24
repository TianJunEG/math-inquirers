# Independent audit, round 2: Level 6 Extension Workbook (self-study, with answers, ages 11-13)

Audited 23 Oct 2026, cold read in a fresh session (no child tested, not run in Scratch). Report only: nothing in the book, data, builders or tools was edited; nothing pushed. Branch `claude/great-fermi-1hv4vc`, working tree clean.

## What I read and how
- Round 1 (`AUDIT.md`), `PROGRESS.md`, `README.md`, `TOOL_REQUESTS.md`, `src/whys.py`, the ten `extension/data/l6_uNN.json`, `p6/content/l1..l10.js`.
- **All 100 pages of the print vector PDF read as text** (`..._Print_BW_vector.pdf`), the colour PDF text-diffed against it (identical apart from page-number position and the two edition lines on p. 2), all 21 answer pages read line by line. The shipped 1-bit file is 100 pages of CCITT 4958x7016 (600 ppi); `build_report.json`: 100 + 100 pages, no overflow, lowest fill 0.86.
- **Print (1-bit) pages viewed as images:** 3, 4, 20, 27, 28, 35, 36, 39, 42, 43, 45, 71, 74; zooms at 200 ppi of the code legend (p. 27) and the Collatz block (p. 74). Other pages read as text only.
- **Changed items found by `git diff dfb0db1` (the commit the round-1 audit was written against) on the ten JSON files: 49 ids** (Learn examples, Learn intros, Try items, items). **All 49 solved by hand** (plus the unchanged items they sit next to, and the whole Unit 10 mixed round and Unit 8 and 9 answer pages), and each printed Why compared with the new stem.
- **Code items hand-traced from the printed blocks:** U4 S7 (7n-4 = 73, answer 11), U5 G2 (12 and 27), U6 S7, U7 G1 (turtle, (-20, 20) and (-60, 60), all 12 moves), U9 S10 and G2 (list loops, 6, 8, 7, 5.6, 8), U10 S10 (score 50: 42, 34, 26, 18 reset, 42, 34 ...; after round 6 = 34, first reset after round 4, ends 50), U10 G2 (2/8, 200, 400), U10 G3 (Collatz: 6 gives 8 steps; 7 gives 16 steps, max 52), U8 G2 (hour 5). All agree with the key. I did not use `l6_lib.py` or the verify scripts.
- **Sentence frames:** every L6 sentence (Learn examples, Try, stems and parts) compared with every sentence in `p6/content/*.js` by hand-written script (numbers masked, ratio) and then read; plus a targeted read of the holiday qbank and mini examples for the items round 1 listed.

## Verdict
**Not sell-ready yet: three small fixes first (all High), then ready apart from the tutor's real Scratch run.** The round-1 clean-up worked: all Highs from round 1 are closed in substance, the maths of 232 of 233 items and every code trace is right, the book is 100 pages, legible in 1-bit, page numbers are right. But the rewrite introduced three new defects that a child or tutor will hit:
1. **A false sentence in the U3 Learn page worked example** (p. 20).
2. **Two answer-page Why lines that still explain the OLD item** (p. 88 item 4, p. 90 item 5): the answer is right, the reason printed under it is for a different question.
3. **A new clone of a holiday item** (U10 Start here 8(a): same mean 15, the three known numbers add to the same 44, same answer 16).

After those three, plus the Mediums below as the owner sees fit, the book can go. The tutor's real Scratch run is still outstanding (the blocks are the book's own drawings; I did not run them in Scratch; nor has a child tried the reading load or pace).

## Round-1 findings: closed or not
| Round 1 | Status | Note |
|---|---|---|
| H1 clone: U10 Mystery Machine (S9, G1) | **Closed** | S10 is now a score-reset game; G1 a taxi fare rule. Both new, both solved (G1: 3n+1, 61, 16). |
| H1 clone: U10 Lucky Seven (G2) | Closed, one echo | Now an 8-part spinner counting numbers over 6 (200). Part (c) "greater than 4 ... about 400" lands on the holiday l6 qbank item (dice 1200 times, "bigger than 4", about 400). See M2. |
| H1 clone: U10 Prime or Not (G3) | **Closed** | Collatz loop, new. Hand-traced. |
| H1 clone: U4 S7 "Plan a search", U4 S5 "Run each machine backwards" | **Closed** | S7 reworded (now "This loop hunts for the n ... It tries 0, 1, 2 ... in turn"); same 7n-4 = 73 type, accepted as type reuse. S5 reworded. |
| H1 clone: U9 T1, Try, T3 | **Closed** | T1 ages (mean 8, median 7, only mode 5, oldest 12 gives 5, 5, 7, 11, 12: unique, solved). Try (Kumar saves, 9) and T3 (laps, 4.5) new. U9 S4 still has the holiday frame, see M2. |
| H1 clone: U5 handshakes (S3), outfits (S1) | **Open, because of H2 below** | S1 bike shop: 30, 36, 6, solved. S3 chess club: 28, 55, 12, solved, **but the printed Why is the old handshake text** (p. 88). |
| H1 clone: U6 S5 spinner | **Open, because of H2 below** | Now 1 to 12, Ali on multiples of 3: 4/12, 8/12, No, solved, **Why is the old prime text** (p. 90). |
| H1 clone: U3 and U8 Learn examples | U8 **closed** (JUMP shift 9, SDVY, solved). U3 **closed as a clone but broken as maths: H1 below.** | |
| H1 clone: U3 S10 floors | Closed, replaced by a near-clone | See M2 (sea-level heights; the holiday workbook Q3 is a sea-level picture). |
| H2 code legend | **Partly closed: M1** | Exists (p. 27) and is readable; but on the Unit 4 Learn page, after 13 code items. |
| H3 give-aways U7 T1, U10 G1a/G2a | **Closed** | U7 T1 no longer prints 18 (asks repeats first, then 1800, then 5); G1 gives two fares and asks for the rule; G2(a) is now the probability. |
| H3 hints U2 T1, U9 T1, U2 G1 | **Closed** (U2 G1 hint still names the method but the stem teaches it; Low) | |
| M1 Learn gaps | U2 factor tree **closed**, tests for 2, 3, 5 closed, **4 and 9 still missing (M4)**; U8 clock example **closed** (5 o'clock + 30 h = 11); U9 median, mode, missing value **closed** (how-to steps 3 to 5, and a missing-value Try); U5 routes and U7 star winding: left as before (stems explain; Low) | |
| M2 U5 G2 bracket | **Closed** | Now `set p to (a x b)` then `if (p mod 2) = 0`; hand-traced 12 and 27. U10 Learn `answer mod 7 + 1` still unbracketed (Low). |
| M3 "stickers" | **Closed** (marbles twice). | |
| M4 repeated Try items | **Closed** for U6 and U7 (Try now 5 white/15 black and 9 sides; U10 C1 4, 11, 18, 25). Difference 7 still appears five times (Low). | |
| M5 U7 G1 directions | **Closed** ("A turn is clockwise. Up means y increases."). | |
| M6 second readings | **Closed**: U2 S5 "may be the same", U7 S10 "Regular", U9 S5(c) "Start again from", U5 S7(b) "Ali is one of the runners", U6 S7(b) "To the nearest whole number", U8 S11 "including 12". | |
| M7 hints that state the method | Mostly closed (U1 T1, T3, U3 T1, G3, U4 T1, U5 T1, U7 T1, T2, U8 T3 reworded). Left: U9 T3, U9 G3 (Low). | |
| M8 Why lines | U9 T1, U9 S7 closed. **U10 G1 still ends "(For your twist ...)" with no twist in the item; U10 S2 Why still lists 111 (outside 90 to 110); U2 T1 and G1(c) still assert "no smaller number" (all Low).** | |
| M9 pace plan | **Not changed** ("20 to 25 minutes", Check yourself in session 3). Needs the child trial. | |
| Low 1 Contents titles twice | **Not fixed** (p. 4). | |
| Low 2 Welcome real-size line | **Closed**: Welcome (p. 3) has no ruler or real-size sentence; the Mi picture does not touch the text; no overflow. "Beyond Level 6 is ahead of school. You may skip it." is there. | |
| Beyond badge | **Closed**: badge in the frame of each item (checked p. 39; text on 11, 18, 24, 25, 32, 46, 53, 60, 67); U10 has none, right. | |
| Wide boxes | **Closed**: U6 T3(b) 102.8 now a wide box (p. 45 viewed). | |
| Page 78 blank | Unchanged (Low). | |

## Findings now

### High (fix before sale)
**H1. U3 Learn worked example, step 2 is false (p. 20, and `l6_u03.json` learn.example).** Freezer reads -8, rises 5 (to -3), falls 9. Printed: "2. Falling moves left. From -3, 3 steps reach 0, then 6 more steps." Falling from -3 moves away from 0; it never reaches 0. The answer (-12) and the check (-8 + 5 - 9 = -12) are right, so the example contradicts itself, and it contradicts the box beside it ("If the jump crosses 0, split it at 0": this jump does not cross 0). The old example (-6 rises 11 to 5, falls 13) did cross 0 and the sentence was right; the rewrite kept the sentence. This is the first worked example of the unit, on the page the child is told to read first. Fix: "From -3, move 9 steps left: -12" (and, if the unit wants a crossing example, choose numbers that cross, e.g. -3 + 8 = 5 then -9). Also the "-9" arc still runs through the "-12" label (old Low 7).

**H2. Two Why lines on the answer pages are for the old items (stale `whys.py` overrides).**
- **p. 88, U5 item 4 (chess club: 8, 11, 66 games; answers 28, 55, 12).** Printed Why: "Each new friend shakes hands with all the earlier friends. 6 friends: 1 + 2 + 3 + 4 + 5 = 15. 8 friends: 1 + ... + 7 = 28. 36 = 1 + ... + 8, so 9 friends." A child who gets (b) or (c) wrong reads a reason about 6 friends, 36 and 9. Source: `src/whys.py` line 42, key `L6U05-S03`.
- **p. 90, U6 item 5 (spinner 1 to 12, Ali on multiples of 3; answers 4, 8, No).** Printed Why: "The primes up to 10 are 2, 3, 5, 7: Ali wins on 4 numbers and Ben on the other 6. 4 is not 6, so it is not fair: Ben is favoured." This says Ben has 6 (the key says 8). Source: `whys.py` line 65, key `L6U06-S05`.
Fix: delete those two entries (the long form in `u05.py` and `u06.py` may be fine, check it) or rewrite them (chess: "Each new player plays all the earlier players: 8 players 1 + ... + 7 = 28; 11 players 1 + ... + 10 = 55; 66 = 1 + ... + 11, so 12 players." U6: "The multiples of 3 up to 12 are 3, 6, 9, 12: Ali wins on 4 numbers, Ben on the other 8. 4 is not 8, so it is not fair: Ben is favoured."). Rebuild. I read every printed Why against its stem; these two were the only mismatches. A cheap guard: a check that every `whys.py` key changed after its item's last edit is re-read.

**H3. U10 Start here 8(a) is a numeric clone of a holiday item (p. 71 item 8).** "The mean of 4 numbers is 15. Three of them are 11, 19 and 14. The 4th is __." Holiday `l9.js` mini2: "The mean of 4 test scores is 15. Three of them are 12, 18 and 14 ... Missing score = 60 - 44 = 16." Same mean, the three known add to 44 in both, same answer 16. The round-1 fix (old (a) was 14, 5 numbers) was better than this one. Change to e.g. mean 13 of 5 numbers with four given, or a story with different totals.

### Medium
**M1. Code legend is there but too late and too thin (p. 27).** "Reading the code blocks" is readable in 1-bit (eight lines, about 11 pt). It covers repeat, repeat until, if/else, mod, pick random, item i of, answer and the clockwise arrow, as asked. But (a) it sits on the Unit 4 Learn page; about 13 code items come before it (U1 S3, S5, S6, S10, T2, G3; U2 S5, S10, G3; U3 S7, S9, T2, G2) and Welcome, the pace plan and the U1 Learn page never point to it; (b) it does not explain the blocks every unit uses: `set x to`, `change x by`, `say ... for 1 seconds`, `ask ... and wait`, `length of list`, `when green flag clicked`, or that a dashed round slot is a blank; (c) "if <test> then / else: choose a part" and "repeat until <test>: stop when true" are terse for a child who has never coded. Fix (cheapest): one line on Welcome and on p. 6 "Code blocks are explained on page 27", add set/change/say to the legend, and word if/else as "if the test is true do the first part, if not do the else part". Better: move the box to p. 5 or the U1 Learn page.

**M2. Holiday frames still present (type reuse, with new numbers; owner decides).**
- U10 S13 (p. 72 item 13): "Roll 2 dice and multiply ... P(product is odd) = 1/4" is holiday `l6.js` qbank "Roll two dice and multiply the numbers. What is the probability that the answer is odd? 9/36 = 1/4": same question, same answer.
- U10 S10 (p. 72 item 10): "A turtle turns 4 at every corner of a regular polygon. Sides? Inside angle?" is the holiday `l7.js` exit ticket ("turns 5 at every corner. How many sides ... each inside angle?") with a number changed.
- U10 G2(c): see table above (400, "greater than 4").
- U9 S4 (p. 63): "4 test scores have a mean of 82. Three are 78, 90 and 85 ... A 5th score of __ keeps the mean" is the holiday l9 mini2 shape (and its answer line).
- U3 S10 (p. 23 item 11): "Heights are measured from sea level, 0 m. A cave -35, a cliff top 48, a boat -6: how far above the cave" is the holiday l3 "sea level" picture (seagull 9, diver -6, crab -15; how far above/below the diver), diver -6 and boat -6 included.
- U2 S3 (p. 14): "factor tree of 84" and "write 90 as a product of primes": the holiday challenge round writes 84 and 60 as products of primes.
- U10 G2 and U10 S9, U6 S5: still the holiday game types (spinner counting, Ali and Ben, missing mean).
None of these shares a long sentence run (`dup_check` stays clean); a child who did the holiday program will recognise the first two and U9 S4.

**M3. U10 G1 (p. 74): the code block prints `say (answer x ? + ?)` but part (a) asks `say (n x [ ] + [ ])`.** n is not defined in that code (the block uses `answer` from `ask km?`). A careful child asks "what is n?". Print `answer` in (a). The Why still ends with "(For your twist, start with a ride you can check by hand.)" and there is no twist part.

**M4. U2 Learn does not teach the tests that S6 uses (p. 13 and p. 16 item 8).** The box now teaches quick tests for 2, 3 and 5. S6 asks "Use the divisibility tests" for a multiple of 4 (372) and of 9 (6835). The 9 test is one line (digit sum); the 4 test (last two digits) is not shown. The items can be done by dividing, so this is small.

**M5. Unit 7 never teaches the angle sum (p. 52 T2, p. 50 item 4(c), 5(c)).** T2 now has the hint "What do the inside angles of an n-sided shape add up to?", which asks for a fact that the Learn page never gives (S4(c)'s Why derives 5 x 180 - 360). A strong child can derive it (each inside angle is 180 minus the turn, the turns add to 360), but a self-study child cannot look it up. One line in the Unit 7 how-to ("All the inside angles add to n x 180 - 360") fixes it.

**M6. Pace plan and Welcome unchanged (p. 3 and p. 5): "20 to 25 minutes" a session.** Session 2 is two Start-here pages (8 items, 3 to 4 code items in units 1, 7 and 10). Round-1 M9 stays open; only a child trial settles it.

### Low
1. **Contents (p. 4)** still prints every unit title twice ("Code the pattern / Code the pattern . follows Holiday Program Lesson 1 . answers on page 80"). Print the title once.
2. **U3 Learn (p. 20):** the "-9" arc passes through the "-12" label.
3. **Page 78 blank** in both editions; fine in the bound book, one wasted page in the soft copy.
4. **Difference 7 recurs:** U1 Try (7n - 4), U1 C1 (7n + 2), U10 S1 (7n + 3), U10 C1 (7n - 3), U1 S8 (+$7). Vary one or two.
5. **U10 Learn `answer mod 7 + 1`** is unbracketed (mod 8 or +1 after?). Print `((answer mod 7) + 1)`.
6. **Why lines that assert:** U2 T1 and G1(c) "numbers below 48 have fewer"; U10 S2 mentions 111 (outside 90 to 110).
7. **Hints that are the whole method:** U9 T3 ("Total = mean x how many. Then take away what you know." is also in the Learn box and the Try), U9 G3.
8. **Unit 5 and 7 Learn pages** still do not show routes by adding corners (the stem does), or a star that winds round more than once (S7 says "winds round the centre 3 times").
9. **1-bit legibility:** all pages checked are legible; the divide sign in the code figures (`n / 2` on p. 74) is a small glyph that reads like a plus at 100 ppi on screen; clear at print resolution (200 ppi zoom fine). Round answer boxes: 102.8 now fits.
10. **Tone (Low 8 of round 1):** the dolphin and "Nearly there. You can do it." banners are young for 11-13; unchanged.

## Compliance and checks
- No price, no SASMO/MOE/GEP/PSLE/olympiad wording seen in the 100 pages; licence page (p. 2) present with the DRAFT line, "private-enrichment book" shared wording. No tutor dependence.
- Contents (pp. 6, 13, 20, 27, 34, 41, 48, 55, 62, 69; My progress 76; certificate 77; Answers 79) match the pages. All ten "answers on page" numbers (80 to 98) match where each unit's answers start. Every answer entry cites the page of its question and that page holds a question with that number (checked by script and by eye for units 1 to 10). 223 answer entries (22 per unit, 25 in unit 10).
- Soft copy is the same text as print (diffed).
- Fill gate: no page over, lowest 0.86.

## Remaining items, in order
1. **H1** fix U3 Learn step 2 (and the arc over "-12").
2. **H2** correct `whys.py` for `L6U05-S03` and `L6U06-S05`; rebuild; re-read all Whys of changed items once more.
3. **H3** replace U10 S9(a).
4. **M1** point to the code key from Welcome and p. 6, add set/change/say/ask/length of list, simplify the if/else line.
5. **M3** U10 G1: `answer` vs `n`, drop the "twist" line.
6. **M2** owner decision on the type-reuse items (U10 S13, S10, G2(c); U9 S4; U3 S10); at least rewrite the U10 S10 and S13 stems.
7. **M4, M5** one line each in the U2 and U7 Learn boxes.
8. **M6** child trial for pace and reading load; then the Lows (Contents title once first).
9. **Outstanding, not for the author:** a tutor's real Scratch run of the code items (the blocks are the book's own drawings with Scratch-like names; I hand-traced them, which proves the answers, not that every block exists or behaves identically in Scratch), owner review of the tier difficulty, printer proof, owner/lawyer removal of the DRAFT licence line.
