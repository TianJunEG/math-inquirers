# Independent audit: holiday online practice, week 2 (lessons 3 and 4), Levels 1, 2, 3

Branch claude/great-fermi-1hv4vc, 24 Oct 2026. Read-only audit; this is the only file written (plus git-ignored `dist/` and `practice/submit/out/`). `test_holiday.py` was not run. Method: read the week 1 audits, the three STATUS week 2 sections and owner_decisions; built all six lessons (`build_holiday.py pN N`), served `dist`, drove Chromium (390, 360, 900 px, light and dark); read every question from the page data with the answers hidden and solved it by hand first (with figures viewed in screenshots), then compared with stored answers, the worked steps, the printed workbook (pdftotext of the Student Workbooks) and the Tutor Guide keys; ran `make_keys.py holiday pN N` and `mark.js`.

## Verdict
**Content and marking: PASS. Release: fix the Medium items first (none is High).**
- All 135+ items hand-solved (L1: 23 + 26, L2: 33 + 44, L3: 37 + 32). Every stored answer equals my solution and the printed Tutor Guide key or qbank answer. No wrong answer key. Worked solutions are all correct except one (M1).
- Client and server marking agree (random right/wrong/blank mixes through the page vs `mark.js`: 0 mismatches in all six). About 2,100 accepted/near-miss strings through `mark.js`: 0 failures. The shared block of `sheet.js` and `mark.js` is identical. No external request, no console error, no horizontal scroll at 390/360/900 px, tap targets at least 40 px.
- All 48 variant families re-derived by me from the displayed template (parity, divisibility, positive results, no zero remainders where a remainder is asked): all correct.
- Nothing from private sources (all `src` are the printed workbook, qbank, gaps/gifted).

## Medium
**M1. P3 L3 8(b) worked solution is false.** Step 2 says the 6 times table 6, 12, 18 ... 72 has digit sums "6, 3, 9, 6, 3, 9, 6, 3, 9, 6, 3, 9" and step 3 "Every digit sum is 3, 6 or 9". Really 48 gives 12 and 66 gives 12. The answer option (digit sums are in the 3 times table, 12 included) is right and matches the Tutor Guide; the steps contradict it and a child who adds 4 + 8 will be confused. Fix the list (6, 3, 9, 6, 3, 9, 6, 12, 9, 6, 12, 9) and say "3, 6, 9 or 12".

**M2. Nav buttons cannot be told apart.** P1 L3/L4: three to five buttons all read "Investigation". P2 L3: five "Investigation", eight "Think", five "Go", one "Make". P2 L4: seven "Investigation", six "Think", eight "Go"; also 1(c), 2(c), 6(c) twice. P3 L3 and L4: many repeats (1(a), 1(b), 2(b), 3(b), 5(a), 5(c), 8(a) twice, 8(c) three times, T3, G6 twice, "Extra" twice; L4 5(b), 6(c), 8(a), 8(b)). Only the aria-label has the full name. A 7 to 9 year old cannot find "Think harder 5" or "8(c) triple". Use the id scheme P3 started (T1, G5), add a letter or short name for split cards (5(b)b / "why"), and for P1/P2 use T1 to T4, G5 to G7, I1 to I7.

**M3. Answers leaked between cards (any card can be opened first).**
- P2 L4 Investigation (c) (self-check) says "Why is every number in exactly one of the patterns?" which answers both marked cards "can a number be in two" and "in none" (No, No).
- P2 L3 Go further 5: the stem says "any number of wheels up to 36", so the next card "could he count 37?" is No by reading.
- P3 L4 8(c) explain hint: "The difference between their ages is 8 every year" is the answer of 8(b) same.
- P3 L3 5(c) why asks "why the number of ways is odd" (5(b) = 7 is odd) and P3 L3 G7 hint ("63 times table: list those up to 200 and add the digits") is two steps of the solution; P3 L3 4(a) hint "56 ÷ 7 gives the first column number" gives column 1 (8).
- P2 L3 T2(c) hint "odd or even?" tells the answer of T2(a) (Siti); P2 L3 hint on 2(b) is a method, acceptable.
- Same-answer chains kept from print (Low): P1 L4 7(a) table (7 triangles = 15 sticks) gives 8(a); P1 L4 7(a) 10 triangles = 7(d); P2 L3 3(table) shows 20 legs after 3 swaps = 3(a); P2 L4 C5a stem "they both say 12" is the first answer of 6(c).
Reword (for example "give your reason" without the conclusion) or show the figure only after Submit.

**M4. Solution figures clipped or small.** P1 L4 C3 solution figure: caption "so place 33 is bead 3 of the set:" is cut off and the answer bead (green) is hidden (clip test: "G", "green"). At 360 px the same figure text is 10.9 px; P3 L4 G5 solution figure text is 10.6 px at 360 px (below the 11 px rule; the builders' test only checked 360 px for questions). Enlarge the viewBox or the font and make the figure taller.

**M5. Reports classify P3 differently from D8 (amended).** `make_keys.py` exports every P3 self-check as `none` (open): P3 L3 8 items, L4 5 items, including L4 G5, a paper-only drawing item with the correct drawing shown, and items that "compare with the answer shown" (3(b), 5(b) mistake, 6(c) why). D8 says paper-only items are recorded as self-marked and excluded from auto-marked percentages; P3 reports will show zero self-checks and show these as "open". P1 and P2 export `self` (and P1 L3 7, 8, 9 as `none`, which is right). Decide: keep `open` only for items with no objective answer, and set `open=False` for items with a model answer or a drawing.

## Low
- L1. Reading load for age: P1 L3 C3 47 words; P2 L3 3(table) 64, T1(a) 56, C5(c) 58; P2 L4 I1 54; P3 L3 5(a rows) 66, 6(a) 60, 8 easy 62, G5 56; P3 L4 8 easy 51. Level 1/2 cards repeat the whole stem on each part; shorten the later parts.
- L2. P3 L4 1(b): the figure shows "1250 buns" and a "?" for the leftover, which belongs to 1(a); 1(b) asks the difference of 486 and 378, so the figure misleads.
- L3. P1 L3 6(a) hint "Read the sentence above the graph again" but the card has no sentence above the graph (it is in the About box); "class party" is the only clue.
- L4. P3 L3 8(b): the correct choice is the longest and most technical option; it stands out. Same for P3 L3 8(a)/L4 option lists with a long correct text.
- L5. Nothing accepts number words ("five") or "5 cm" for fields with a printed unit other than the unit rule: "five" is wrong in all number boxes (Level 1, age 6 to 8 may type it; the keypad is numeric on tablets). Units and trailing full stop are accepted (checked).
- L6. P1 L3 Investigation 5 hint "Count in 3s for each row: 3, 6, 9" partly states the reason (self-check, so only a hint issue).
- L7. P2 L3 3(table) asks only the Legs row; STATUS already raises it (open question 1).
- L8. Order of tiers: Investigation is listed before Think harder (print order is Think harder, Go further, Investigation). Declared in STATUS; EXTRAS-VISIBLE adopted.
- L9. "Make up your own" button reads "Make" (P2). Covered by M2.

## What I checked, by item
1. **Hand-solve and print.** Every item, from the question text and figures (counted the graph: 6, 5, 8, 3, 5; the array 4 by 5; the tray 3 rows of 10, 12 visible; pattern T C C S S; ABCD; triangle sticks; tables of square tables; grid puzzle unique: rows 7, 9, 6, columns 8, 6, 9; bar models). Examples independently derived: P1 L3 C3 has exactly two graphs; P2 L3 T1 tricycles 1, 3, 5; C6 27; C7 5 hens 3 goats; P2 L4 C7 8 and 20, C6 tower 17 (50 yes) and 100 no; P3 L3 2(a) 3 and 9, T4 28 and 91, G7 126; P3 L4 I8 table, double in 3 years, triple never. All equal stored answers and the Tutor Guide / qbank. No online question changes the printed meaning or loses information needed to answer (reworded parts keep the printed numbers; P2 L4 Investigation "pick any number" is fixed to 26, declared; P2 L3 3 splits the printed hens/goats question, declared).
2. **Accepted answers.** Right: plain, spaces, trailing "." and ".0", unit words, "$", leading zero, `,` `;` space "and" separators, brackets, trailing comma, three-digit lists without spaces (`126,189`), any order for unordered sets. Wrong: plus/minus 1 and 2, times 10, concatenation, blank, missing/extra/duplicate list members, one changed member, reversed or swapped boxes, ordered lists in another order (P2 L3 6(b), T1(b), P3 L3 5(a) rows/chairs, P3 L3 4(a)/(b)). All behave. Week 1 H1 (comma without space) is fixed.
3. **Flow.** Free selection, skip, hint, reload keeps answers, "N questions have no answer yet. Submit anyway?" counts only marked blanks, Keep working returns, solutions absent before Submit and present for all items after (including paper-only with the note and the correct-drawing figure: P1 L3 vote, I1, I2, C3; P1 L4 I1, C3; P3 L4 G5), inputs locked, "Change my answers" hides solutions.
4. **Leaks.** M3 and the Low chains. Hints elsewhere nudge and do not give the answer. Variant example numbers (for instance P3 L4 4: "Try Ben = 50") are never the answer.
5. **Child-friendliness.** Kind feedback; Singapore wording ($, Mr Tan, Mr Lim, vans, trip, stickers); no coin or note images; no "circle", "cross out", "take-home" in questions (P1 L4 4(a) hint "draw in the empty boxes on paper" and P3 L3 5(a) "Write" are fine). M1, L1.
6. **Accessibility and layout.** No horizontal scroll, no clipped page text, targets at least 40 px, figures on a white panel in dark mode (readable), figure text at least 11 px at 390 px; M2, M4. Input modes: lists `text`, numbers `numeric` (verified through the page); "Use commas" helper present on list cards.
7. **Server parity.** `make_keys.py` for all six; marking modes: P1 L3 auto 13, self 7, none 3; P1 L4 21/5; P2 L3 26/7; P2 L4 35/9; P3 L3 29 auto, 8 none; P3 L4 27 auto, 5 none (M5). `mark.js` equals the page on every case tried.
8. **Variants.** P1 L3 T2, T3, C2 (298); P1 L4 T2, T4, C1; P2 L3 3a, 4a, 4b, 5a, 5b; P2 L4 2c, 3a, 4b, 4c, 5b, T3, C6a; P3 L3 1b, 2b, 3a, T2; P3 L4 15 families. I re-derived each answer formula and checked that all combinations give whole answers (4b/5b remainders never 0 where asked; halving items always even).
9. **Private sources.** None.
