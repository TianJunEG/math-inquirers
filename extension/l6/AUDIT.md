# Independent audit: Level 6 Extension Workbook (self-study, with answers, ages 11-13)

Audited 23 Oct 2026, cold read by a model in a fresh session (no child tested). Report only: nothing in the book, data, builders or tools was edited; nothing pushed. Modelled on `extension/l2/AUDIT.md` and `extension/l4/AUDIT.md`.

Files read: `extension/l6/README.md`, `PROGRESS.md`, `TOOL_REQUESTS.md`, `src/whys.py`; `extension/data/l6_u01..u10.json`; `outputs/extension/L6/*Print_BW.pdf` (100 pages, 1-bit CCITT, 4958x7016 = 600 ppi), `*Print_BW_vector.pdf` (text), `*Soft_Copy_Colour.pdf` (100 pages); `p6/content/l1..l10.js` (holiday program).

Note on timing: the coordinator rebuilt Level 6 while I was auditing (data files and PDFs rewritten 15:47 to 15:51; the "Beyond Level 6" label now comes from the shared `beyond` key and the Welcome ruler sentence is gone). Everything below about the book is from the rebuilt PDFs (copied to scratch at 15:51; `build_report.json` of 15:51 agrees: 100 + 100 pages, no problems, lowest fill 0.86) and the current JSON. A few of my first notes were from the earlier build; those are marked "fixed in rebuild".

## Method and coverage (honest)
- **Every item solved by hand**, all parts: 10 Learn-it examples, 10 Try items and 233 numbered items (22 per unit, 25 in unit 10; 11 Start here + 3 Think harder + 3 Go further + 4 Check yourself, 14 Start here in unit 10) compared with the printed answer and Why. Not the 10 per unit asked: all of them.
- **Every code item hand-traced** from the printed blocks (not from the builder's interpreter): U1 S4 S5 S6 S10 T2 G3; U2 S4 S10 G3; U3 S7 S8 T2 G2; U4 S6 S7 S11 G3; U5 S4 S8 G2; U6 S7 G2; U7 S3 S6 S8 S9 G1 G3; U8 S6 S10 G2; U9 S9 G2; U10 Learn, S10 G1 G3. Then 14 of the riskiest loops re-run in a throw-away Python script of my own (not the builder's `l6_lib.py`): U8 G2 (hour 5), U8 S10 (7, 14, 21, 2, 9), U1 G3 (14, 105), U3 T2 (6 repeats, 60), U5 G2 (12 and 27), U7 G1 coordinates (-20, 20 and -60, 60), U10 G3 (6/1/0 and found), U2 G3, U4 G3, U1 T2, U2 S4. All agree with the key.
- **Result: 0 wrong answers, 0 unsolvable items, 0 wrong Why lines.** The 526 keyed answers are right (I also ran `run_checks.py --level 6`: OK, `wording_lint.py`: 0 errors, `dup_check.py --level 6`: OK, 233 texts, 7-word gate clean against holiday and the 48 private files). The problems are about **originality, teaching, ambiguity and a few give-aways**, not arithmetic.
- **Pages.** Print edition (1-bit) viewed as images, two-up at 80 dpi: pp. 1, 3, 5, 6-12, 13-19, 20-27, 28-33, 34-39, 41-42, 44-53, 55-60, 62-67, 69-74, 77, 79, 92. Zooms at 150-220 dpi of p. 39 (code block) and p. 42 (spinner); a zoom of p. 38 failed while the file was briefly missing in the rebuild, so the route figure with X was seen at 80 dpi only. Pages 4, 40, 43, 54, 61, 68, 75, 76 and the answer pages 80-100 (except 92) were read as text from the vector PDF, not viewed; text spot checks of 80, 81, 82 and 100. Colour edition read as text and compared with print; not viewed page by page. Answer-box sizes measured with PyMuPDF on pp. 31, 45, 53, 67, 74.
- **Not done:** no child trial (reading load, pace), no owner tier review, no printer proof. Not run in real Scratch.

## Verdict
**Ready after fixes, not before.** Maths, keys, tier structure, page numbers, licence page, 1-bit print file and B&W legibility are in good shape. Three Highs must be fixed first: (1) a block of items too close to holiday P6 items (the spec says new contexts), (2) no legend for the code blocks although the book says "you do not need to have joined the holiday program", (3) a handful of answers given away on the page. All are small edits; the clone items need replacement items and a re-run of the checks.

## Findings

### High

**H1. Items too close to holiday P6 items (same story frame, same structure, numbers changed).** `dup_check.py` is clean at 7 words (all hits are stock stems), but I compared every L6 sentence with every holiday sentence (ratio and 5/6-word runs, numbers masked) and read the top 45. A child who did the holiday program will recognise these:

| L6 item (page) | Holiday source | What is shared |
|---|---|---|
| U10 G1 "Plan a Mystery Machine. A random n from 1 to 20 ... shows 5n - 2" (p74) and U10 S9 "program chooses a secret n between 1 and 20 ... n x 4 + 3, shows 31, smallest, largest" (p71) | `l10.js` Starter A "Mystery Machine: the computer picks n from 1 to 20, shows 3n + 4; out 25 -> 7; smallest OUT for n from 1 to 20 is 7" | name, frame, all three questions (backwards, smallest, largest) |
| U10 G2 "Plan a Lucky Number program: repeat 1000 times: roll 2 dice and add. If the total is 11..." (p74) | `l10.js` Starter C "Lucky Seven: roll two dice 1000 times, count the 7s; expect about 167" and workbook "Lucky Seven, changed to count 8s" | name, 1000 rolls, 36 results, "about", only 7 -> 11 |
| U10 G3 "tests whether n is prime ... found" (p74) | `l10.js` Starter B "Prime or Not?: a loop counts the factors of n with mod" | same program idea |
| U4 S7 "Plan a search. Find n when 7n - 4 = 73 by trying n = 0, 1, 2, ... Fill in the blanks." (p29) | `l4.js` Q6 "Plan a search. Find n when 8n - 5 = 91 by trying n = 0, 1, 2, 3 ..." | the whole opening sentence |
| U4 S5 "Run each machine backwards to find n. Check by going forwards." (p30) | `l4.js` "Run each machine backwards to find n. Then check by going forwards." | the whole sentence (not caught: dup_check stops at a sentence break) |
| U9 T1 "Five whole numbers have a mean of 7 and a median of 6. Their only mode is 4, and the largest number is 13." (p66) | `l9.js` "Five whole numbers have a mean of 9, a median of 8 and a mode of 8. The smallest is 5 and the largest is 14." (and "mean of 6, median 5, only one mode 2") | frame, method, answer shape |
| U9 Try "The mean of 4 numbers is 12. Three of them are 9, 15 and 10. The 4th number is" (p62) and U9 T3 "mean of 3 numbers is 6.4; two of them are 5.5 and 7.2" (p66) | `l9.js` "mean of 4 test scores is 15. Three of them are 12, 18 and 14"; "mean of 3 numbers is 9. Two of them are 5 and 12. What is the third number?" | whole item |
| U5 S3(a) "With 6 friends there are [15] handshakes" (p35) | `l5.js` exit ticket "Six friends meet. Every pair shakes hands once. How many handshakes?" 15 | same number, same answer; the 5-friend pentagon is the holiday mini example too |
| U5 S4 "1 main, 1 drink, 1 fruit; 4, 3, 2" (p36) | `l5.js` "Mei packs 4 T-shirts, 3 pairs of shorts and 2 caps" | same numbers 4 x 3 x 2 = 24, same questions (add one more choice) |
| U6 S5 "Ali and Ben spin 1 to 10; Ali wins on a prime" (p43) | `l6.js` "spinner with 10 equal parts numbered 1 to 10, probability of a prime? 4/10" | same spinner, same numbers |
| U3 worked example "It is -6 C at 6 a.m. By noon it rises 11 degrees. By night it falls 13" (p20) | `l3.js` "It is -4 C at 6 a.m. It rises 9 degrees by noon, then falls 7 degrees by night" | story frame (6 a.m., noon, night), same two-jump structure. The README says this was changed; the frame was not |
| U3 S10 "In a car park the floors are L3 ... B3. There is no floor 0. Count the floors one by one." (p23) | `l3.js` "no level 0 ... level 4 down to B3 ... Count the levels one by one" and "Count the floors one by one" | the trick, the B1/B2/B3 labels, the sentence |
| U8 worked example "Code the word ZIP with a shift of 7" (p55) | `l8.js` "Code the word PIZZA with a shift of 7" | sentence, shift 7, and Z-I-Z-like letters |
| U10 S3 "A diver is at -18 m. She rises 7 m and then dives 12 m." (p70) | `l3.js` "A submarine is at -120 m. It rises 45 m, then dives 70 m." | structure |
| U9 S7 "A cafe has 7 staff ... 1500 ... 9500. Mean / median / which is better" (p64) | `l9.js` "A shop has 10 staff. Nine earn $2000 and the manager earns $11 000" and Q4 "$22 (154 / 7) ... $69" | misleading-pay frame |

Fix: replace the first nine rows (at least) with new stories and a different shape (Mystery Machine and Lucky Seven are named programs the holiday children built; give them different names and tasks), re-run `l6_uNN_checks.py`, `dup_check.py` and the build. The last six are acceptable as "similar type, new numbers" if the owner agrees, but U3's worked example and U8's ZIP example are in the Learn pages, so they matter more.

**H2. No legend for the code blocks (self-study, "you do not need to have joined").** About 45 of 233 items are code items and every one assumes the reader knows what the printed blocks do. Nowhere in the book (Welcome, Learn pages, pace plan) is there a "How to read the blocks" box: what `repeat 4`, `repeat until`, `if ... then ... else`, `set x to`, `change x by`, `say x for 1 seconds` (says it, then goes on), `n mod d` (remainder), `pick random 1 to 6`, `item i of list`, `length of list`, `ask ... and wait` / `answer`, `turn clockwise` (the arrow symbol) mean, and that the dashed round slot is a blank to fill. Only some are explained in item stems (U4 S6 explains "answer"; U2 Learn explains mod; U9 S9 does not explain `item i of`). A child without the holiday program or Scratch meets `repeat until` and `if/else` in U1 G3, U2 S4, U3 T2 without a word. Add one box to the U1 Learn page (or a "Code key" strip on p. 3 or p. 5) and, in U7, one line: the arrow means "turn clockwise".

**H3. Answers given away on the page.**
- **U7 Think harder 1 (p52):** (a) "After **18** repeats it has turned [1800]" and (c) "It first faces the start direction after [18] repeats". The key to (c) is printed in (a); (b) "that is 5 full turns" then shows 1800 is a multiple of 360. Reword (a) as "After 10 repeats" and (b) as "after 18 repeats ... how many full turns" only after (c) is hidden, or drop 18 from (a).
- **U10 Go further 1 (p74):** the stem says the machine "shows 5n - 2", then (a) asks `say (n x [5] - [2])`: a copy exercise. **U10 Go further 2 (p74):** (a) "The program repeats [1000] times" is in the stem. Both are the "Plan" items that the holiday lesson meant as open tasks. Hide the rule (give only OUT for two values) and ask for the rule.
- **Hints that hold the answer:** U2 Think harder 1 hint "Count the factors of 12, 16, 24, 36 and 48" lists exactly the three answers (16, 36, 48) plus two decoys. U9 Think harder 1 hint "The 2 smallest are 4 and 4. Use the total for the other" states the central deduction and two of the five numbers. U2 Go further 1 hint states the counting method for 72. Replace with a nudge ("Where must the two 4s sit if 6 is the middle one?"; "Try some numbers between 10 and 60").

### Medium

**M1. Learn pages (self-study) teach only part of the unit.** Each Learn page has a worked example, how-to box and Try (good), but items then use skills the page never shows:
- **U2 (p13):** only prime testing is shown. Factor tree and "write as a product of primes" (S3, C3, U10 S2), divisibility tests for 3, 4 and 9 (S6: "Use the divisibility tests") and factor pairs (S1) are not taught. Add a mini factor tree and the three tests.
- **U8 (p55):** only the Caesar example. Clock and weekday arithmetic with mod (S1-S3, S9, T2, C1, C4) has one sentence; a child must work out "50 hours later" alone. Add "7 + 50 = 57; 57 - 48 = 9" as a second example.
- **U9 (p62):** only the mean. Median and mode are two lines in the how-to box; no example for a missing value (S3, S4, T3) although "Total = mean x how many" is in the intro. Add one line each.
- **U5 (p34):** only the multiplication rule. Routes by adding corners (S8), digit cards with 0 (S9), diagonals/pairs (S10), counting rectangles (S11) and "count the opposite" are not shown.
- **U7 (p48):** the star that winds round more than once (S8, G2) is not shown.

**M2. U5 Go further 2 (p39) is ambiguous: `if (a x b mod 2) = 0`.** Read as (a x b) mod 2 the code says 12 (key); read as a x (b mod 2) it says 8 (checked), and both readings are legal in most languages. Put brackets: `((a x b) mod 2)`. Same style `answer mod 7 + 1` (U10 Learn) is fine because it is left to right, but bracket it too.

**M3. U4 Start here 7 (p29) says "stickers" for marbles.** "Siti has n marbles ... (b) all 3 together have [45] stickers. (c) All 3 together have [5] x n + [5] stickers." Change to "marbles" (two places).

**M4. Try and Check-yourself items that repeat items in the same unit or the book.**
- U6 Try (p41) "6 yellow and 9 blue, P(yellow)" and U6 Check yourself 1 (p47) "9 red and 6 blue, P(blue)": the same numbers with colours swapped, answer 2/5 both; U10 C3 is 2/5 again.
- U7 Try (p48) "A regular polygon has 18 sides ... turn, inside angle" is U7 Start here 5 (a)(b) (p50) word for word (18 sides, 20 and 160), and C1 (40 sides) is the same again. Make the Try a different n.
- U1 Start here 2(b) "3, 8, 13, 18" (p7) is U10 Check yourself 1 (p75) (rule 5n - 2, same sequence). Five items in U1/U10 use a difference of 7 (the holiday example also uses 7): vary.

**M5. U7 Go further 1 (p53): directions are never defined.** The arrow "turn (clockwise)" and "y goes up" are not stated anywhere, yet the answer (-20, 20) depends on both. A child who thinks the arrow means a left turn or y goes down gets (-20, -20). State both in the stem. (Also covered by H2: the arrow symbol needs a key.)

**M6. Second readings (small each).**
- U2 S5 (p14) "write 26 as a sum of 2 primes. Find every way": 13 + 13 is in the key; say "the two primes may be the same".
- U7 S10 (p51) "6 triangles", "3 squares", "2 hexagons and 2 triangles": the key needs regular shapes (60, 90, 120). Say "regular".
- U9 S5(c) (p64) "Take away the value 14": from the original list (key 11), but (b) just added 20; a child who keeps the 20 gets 13.5. Say "From the first list, take away".
- U5 S6(b) (p36) "Ali must win gold": Ali is not one of the 5 runners named. Say "Ali is one of the runners".
- U6 S7(b) (p42) "The code says about [17]": the exact value is 16.7; a child who writes 16 is marked wrong. The key should accept 16 or 17, or the box should say "to the nearest whole number".
- U8 S11 (p58) "visit [4] different numbers": counts the start 12 as visited; say "including 12".
- U6 S10 (p44) 112 heads in 200 is 1.7 standard deviations; "Yes, could be fair" is right but borderline for a child; fine, but a number nearer 106 would teach the point better.

**M7. Hints that state the whole method (first hint should only start).** U1 T1 "Take 5 x n away from a start number", U1 T3 "Share the rise equally", U3 T1 and G3 ("A number line with 0 would be 1 step too short" is the whole trick), U4 T1 ("undo Y first, then undo X"), U5 T1 ("Count to X and from X separately. Then multiply"), U7 T1 ("Find the first multiple of 100 that is also a multiple of 360"), U7 T2/T3, U8 T3, U9 G3, U10 G3. Same finding as the Level 1 and Level 4 audits (M6, M4).

**M8. A few of the ~60 shortened Why lines no longer explain.**
- **U9 T1:** "the mode 4 is also the smallest, so the first two are 4 and 4": no reason is given why the mode must appear twice and both must be below the median 6. Add "4 must appear twice to be the only mode, and both 4s are below the middle".
- **U2 T1 and U2 G1(c):** "Smaller numbers have fewer" / "no smaller number has 12" is asserted, not shown. Add the check (the numbers below 16 with 5 factors: none).
- **U9 S7:** "The owner's 9500" but the stem never says the 9500 is the owner.
- **U10 G1:** ends "(For your twist, test by hand first: n = 4 shows 18.)" but the item has no twist part.
- **U10 S2:** mentions 111 (outside 90 to 110).
- The rest I read (all 60 in `whys.py`) still explain in plain words; the loop-trace Whys (U1 S4, U2 S4, U3 S7, U8 S7, S10) are good.

**M9. Pace plan optimistic for sessions 1 and 2 (p5).** Session 2 is two Start here pages: for example unit 1 (pp. 8-9) is 8 items, 3 of them code with traces; unit 7 pp. 50-51 is 8 items with turtle figures. For a 11-13 child 20 to 25 minutes is tight (about 3 minutes an item). Session 1 is the dense Learn page plus a full Start here page. Say "25 to 30 minutes" or move Check yourself to the weekend page. Needs the child trial.

### Low
1. **Contents (p4)** prints every unit title twice ("Code the pattern" and "Code the pattern . follows Holiday Program Lesson 1 . answers on page 80"). Print the title once. (Same as Level 4 Low 1.)
2. **Welcome (p3), after rebuild:** the ruler sentence is gone (fixed in rebuild). New line "The figures are printed at their real size" (print) and "Print at 100 percent so the figures stay the right size" (soft) mean nothing for Level 6 (nothing is measured). Delete both. "Beyond Level 6 means ahead of the school year" is fine and the label is now a badge in the frame of each item (fixed in rebuild; checked p11, p25, p46, p53, p60, p67, p74).
3. **Stale notes:** `README.md` decisions 2 and 3, `PROGRESS.md` "Open" and `TOOL_REQUESTS.md` items 1, 2 and 5 describe the old label and the ruler sentence. Update after the rebuild.
4. **Page 78 is blank in both editions** (no text, no page number). Right for a bound book (verso of the certificate, answers start on a right-hand page 79); in the soft copy it is a wasted page. Optional: print "This page is left blank" or drop it from the soft copy. Contents (pp. 6, 13, 20, 27, 34, 41, 48, 55, 62, 69), My progress 76, certificate 77, answers 79-100 and all ten "answers on page" numbers (80, 82, ... 98) are correct; each answer's "page N" matches the question page for every entry I checked (unit 1 in full, units 7, 10 spot checks).
5. **Answer boxes** are 15.3 to 15.6 mm by 9.5 mm: fine for three and four characters (2880, 1200, 2.75, 54.5); **U6 T3(b) "102.8"** (5 characters) is tight. U5 S8 (p37): the dashed route circles are about 8 mm; the "10" that a child must write in the End circle is tight. U1 and others use 15 mm boxes for fractions: fine.
6. **Yes/No and option words** ("Yes No", "50 64 72", "A B C") are plain text; the item stems do not always say "Circle" (U1 S4(a), U2 S9(b)). Say it once on p. 3 ("Circle the word you choose").
7. **U3 Learn (p20):** the "-13" arc runs through the "-8" label.
8. **Tone/age:** page banners "Nearly there. You can do it." and the Mi dolphin on the cover, Welcome and certificate are the Level 1 style; for 11-13 the banners are a little young. The certificate trophy plaque has pseudo-text (also in Level 4 audit Low 9). Consider a plainer certificate for Level 6.

## Compliance and originality
- **No price anywhere** and no SASMO, MOE, GEP, PSLE, olympiad or "private" wording in the 100 pages (grep of both PDFs and the JSON; the only hits are "private-enrichment book" on p2, which is the shared licence line, "tuition centres" and "class" in a story). No tutor or class dependence ("You do not need to have joined it"). Licence page present (Preciouslyours Pte Ltd, UEN, DRAFT line in both editions; owner to remove before sale).
- **`dup_check.py --level 6`:** OK; REVIEW list (35 lines) read: all stock skeletons; the real repeats are in H1. Contest-style items (triangle numbers U1 G3, Fibonacci staircase U5 G3, Chinese remainder U8 T1, check digits U8 G3, reversible primes U10 T3, 10-point star U7 S8) are standard puzzles, written freshly; nothing matched the private source texts.
- **Beyond items** all sit in Think harder or Go further (none in Start here), as the plan requires. Syllabus level: factor-count formula (U2 G1), second differences (U1 G1), subtracting a negative (U3 T1), at-least-one (U6 G1), expected winnings (U6 G3), star angles (U7 G2), changing shift and check digits (U8) are labelled; unlabelled items that go past school level: U7 G3 (circle circumference from 3.14) is labelled; U4 G2 (consecutive numbers with n) is not but is fine.
- **B&W print:** pages are 1-bit CCITT at 600 ppi, 100 pages. Code blocks are black text on white with dashed blanks, spinner letters, number lines, thermometer, route grids, bar charts, turtle polygon and sieve tables are all legible at 80 dpi and clean at 150-220 dpi; nothing depends on colour (shape and words tell block kinds). The 1-bit halftone of Mi is acceptable.
- **Pages overflow/fill:** `build_report.json` 15:51: no overflow, lowest fill 0.86, 0 problems, 100 + 100 pages.

## What passed
- All 526 answers and every Why are right (hand solved, not checked against the builder's script). Hints 11 pt, one line, printed upside down. Every unit has Learn it (worked example, how-to box, Your turn) + 3 Start here + Think harder + Go further + Check yourself with score and Look back, 7 pages. Answer keys say the answer first, then Why, then the page. Contents, pace plan and answer-section page numbers are right. Writing space is generous (Working lines, trace tables 5 to 6 rows, number-line lines).
- Tier structure reads well; Start here is school range for 11-13, Think harder is multi-step with a hint, Go further is longer or Beyond. Reading load is low (short sentences).

## Ranked top 10 (fix in this order)
1. **H1** Replace the 9 to 15 items that copy a holiday frame, above all the Learn pages (U3 example, U8 ZIP) and unit 10's Mystery Machine / Lucky Seven / Prime or Not (U10 S9, G1, G2, G3), U4 S7 and S5, U9 T1, Try and T3, U5 S3 and S4, U6 S5.
2. **H2** Add a "How to read the blocks" key (one box on the U1 Learn page or p. 3): repeat, repeat until, if/else, set and change, say, mod, random, list items, ask/answer, the clockwise arrow, dashed slots.
3. **H3** Remove the give-aways: U7 T1 (18 in (a) and (c)), U10 G1(a) and G2(a), the hints in U2 T1 and U9 T1 (and U2 G1).
4. **M1** Add the missing teaching to the Learn pages of units 2, 8 and 9 (factor tree and divisibility tests; mod on a clock; median, mode and missing value), then 5 and 7.
5. **M2** Bracket `((a x b) mod 2)` in U5 G2 (answer 12 or 8 depending on the reading).
6. **M3** U4 S7: "stickers" -> "marbles" in (b) and (c).
7. **M4** Change the Try items that are repeated in the unit (U6 Try = C1, U7 Try = S5) and the repeated sequence U1 S2(b) = U10 C1.
8. **M5** U7 G1: say the arrow is clockwise and y goes up.
9. **M6 and M8** Fix the second readings (U2 S5, U7 S10, U9 S5(c), U5 S6, U6 S7, U8 S11) and the Why lines that no longer explain (U9 T1, U2 T1/G1, U10 G1 "twist", U9 S7 "owner").
10. **M9** Pace plan: "25 to 30 minutes" or move Check yourself to the weekend page; then run the child trial.

Also tidy after the rebuild: Low 1 (Contents titles twice), Low 2 (real-size sentences), Low 3 (README/PROGRESS/TOOL_REQUESTS notes).
