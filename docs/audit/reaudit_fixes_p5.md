# Level 5 fix pass after the re-audit (content and wording only)

Date: 2026-10-22. Scope: Level 5 (ages 10-12) sources `p5/content/l1..l10.js`, `p5/content/gaps.js`, `p5/data.js`, `p5/workbook_html.js`, `p5/guide.js` (the lead's recording cues were left alone), `rebuild/gen_p5l*.py`, `rebuild/p5_gaps.py` and one new helper `rebuild/p5_printed.py`. Not touched: `diag/*`, `levels/*`, `rebuild/slidekit.py`, `hp/*`, `website/*`, `docs/levels_and_placement.md`. Nothing committed. No pacing or timeline change (the timeline rows are the same except the choice sentence). Every new or changed number was checked in Python (exact fractions or brute force); the checks are listed at the end.

Rebuilt: all ten decks (`gen_p5l1..10.py`, then `levels/restyle.py split/p5lK`, all previewed: no slide overflows), `bash levels/build_level.sh 5`, `python3 levels/mkextras.py 5` (self-check OK).

## Final page counts

| File | Before | After |
|---|---|---|
| Student workbook | 57 | **57** (5 pages per lesson kept: page 1, page 2, Investigation, Think harder, Go further) |
| Tutor guide | 102 (the committed build with recording cues) | 102 |
| Weekly dose pack | 26 | 26 |
| Question bank | 28 | 28 |
| Weekly email pack / Free taster / What Learners Get | 12 / 5 / 1 | 12 / 5 / 1 |
| Decks (slides each, L1..L10) | 26 to 29 each (per the re-audit) | 30, 29, 29, 31, 30, 30, 30, 30, 30, 31 (the extra slides are the optional printed Think harder / Go further slides, see item 4) |

Words on workbook pages 1 and 2 together (counted from the PDF text, so they include the title, the plan line, figure labels and tables): L1 588 -> 572, L2 559 -> 533, L3 579 -> 557, L4 516 -> 533, L5 639 -> 602, L6 634 -> 560, L7 443 -> 460, L8 539 -> 552, L9 463 -> 463, L10 507 -> 507. See item 2 for why this is not near 300.

## 1. The choice line (new defect)

Old: every Start-here page said "After question 3 you may choose", but page 1 ends at Q2 in L3, L4, L8 and L9.
New: `p5/data.js` now computes where the page break really falls (it runs each lesson's workbook builder and counts the questions before the page break) and exports `pageOne` and `choiceQ(n)`: 3 in L1, L2, L5, L6, L7, L10 and **2 in L3, L4, L8, L9**. Used by:
* `p5/workbook_html.js`: "After question 2/3 you may choose: carry on, or try Think harder." (checked in the PDF text, ten lines, 2 in the four lessons).
* `p5/guide.js` (per lesson), the script text in `p5/data.js` (per lesson), the generic guide bullet ("question 2 or 3, the line on each page 1 gives the number"), the TIMELINE row ("At the end of page 1 you may choose ..."), `rebuild/p5_gaps.py` (the page-1 slide card and its notes use the lesson's number) and the title-slide notes in every `gen_p5lK.py` (number written per lesson).

## 2. Start-here pages

Eleven items that needed the lesson's own method (V) and what was done (all answers unchanged unless stated; keys, slide check answers and notes were updated to match):

| Item | Old | New |
|---|---|---|
| L1 Q3 six-clue riddle | one "START HERE" line | the same riddle (answer 7 253 609) in three steps: (a) the two starts 7 2 5 ... and 7 3 6 ..., (b) which start breaks "all digits different", (c) finish with clues 5 and 6 |
| L1 Q6 range plus find ALL with a digit sum | needed the whole method | Q6 is now "circle which numbers round to 2 500 000" and "smallest and greatest" on the number line; the find-ALL with digit sum 9 (6 numbers) is Think harder A3. Q2(c) (closest to 6 000 000) moved to Think harder A4 |
| L2 Q2 unlike-denominator subtraction and unit fractions | start line for 7/10 only, then 9/20 and 3/8 two ways | a full worked example (7/10 = 1/2 + 1/5, with the fraction wall tip), then 9/20 and 2/3 (each has exactly one way); 3/8 in two ways is Think harder A1 |
| L3 Q2 ratio after a swap | figure only | adds a ratio-table way in: "3/4 as many means 3 and 4, then 6 and 8, then 9 and 12 ... until the total is 84" |
| L3 Q5 unchanged-part bar | box with 3/7 red, 30 red added | Q5 is now a jar of 12 red and 8 blue beads with 10 more red (which colour did not change, blue fraction 2/5 then 4/15); the original problem (70 beads at first, 100 now) is Think harder A2 |
| L4 Q4 shaded triangle by subtracting | three white triangles | "each white triangle has a square corner, so it is half of a rectangle", with ADE = 16 worked |
| L5 Q4 water rise | no entry | "Start here" layer idea: base 40 x 25 = 1000 cm2, a 1 cm layer is 1000 cm3. The stone part (d) moved to the question bank |
| L6 Q4(c) split 900 pages | hardest part of the page | removed from the page, now a bank Think harder-pool item (540 pages); Q4 (a) and (b) stay |
| L7 Q5 two wholes in a table | table only | adds "10% of 40 is ..., so 60% is ..." |
| L8 Q3 four-step chain | no model | the first step is worked ("angle ADB = 62 degrees because AB = AD, base angles equal (E)") |
| L8 Q4 parallelogram plus isosceles chain | four steps | two steps with reasons (ADC, DEA); AEC and EAB are Think harder A3 on the same figure |

Borderline items: marked "(try this one if you like)": L1 Q5(d), L2 Q4(c), L3 Q3(b), L6 Q3(d), L6 Q5(b). Moved out of the page to the bank: L5 Q4(d) stone, L5 Q6(c) equal depth (8 cm), L6 Q2(c) 20 cans (three ways, cheapest $13.64), L2 Q6(c) closest to 1 (11/12). Removed as redundant: L2 Q1(b) ribbon, L3 Q1(d). L4 Q1 now starts from "triangle (a) is half of an 8 by 6 rectangle". Left as they were (each already has a Start-here line or a printed scaffold): L4 Q3, L5 Q3, L5 Q5 (start shortened), L6 Q2(a)(b) and Q5(a), L7 Q2, Q3, Q4, L8 Q2 and Q5 (a start line was added to Q5), L9 Q5(b), L10 Q2 and Q3.

Page-2 plans: L5 "Q4 (a) to (c) and Q5" -> "Q4 (a) (b), then Q6 (a) (b)"; L6 "Q4 (a), Q6 (a) and then Q5" -> "Q4 (a), then Q6 (a) (b)"; L7 "Q4 (a) to (c) and Q5" -> "Q4 (a) to (c)"; L8 "Q3 (a) (b) and Q4 (a) (b)" -> "Q4 (a) (b), then Q3 (b)". No plan now starts on L5 Q5 or L6 Q5.

Words: trimmed stems and hints and removed the try-this parts above; the totals fell 3 to 12 percent in eight lessons (table above), L4 and L7 and L8 rose by a few words because a worked start was added. **Not reached: 300 words.** The counts include the title block, plan and choice lines, figure labels and tables; with 5 to 6 items per lesson and the way-in lines the two pages cannot honestly drop to 300 without cutting items, which the pass did not do.

## 3. Figures on Think harder (and two Go further) items

SVG figures are part of the lesson content (`fig` on the question-bank item) and print under the item in the workbook and next to it on the slide. The questions that need them: L4 A2 (right triangle 12, 16, 20), A3 (square and triangle, height ?), A4 (rectangle and triangle, same base and height); L5 A1 (box 9 by 6 by 5), A4 (3 by 4 by 5 painted cuboid); L8 A1 (parallelogram, A = 3 x B), A3 (the Q4 figure, cropped), A4 (square with equilateral triangle CDE). Go further: L4 B1, B2 (two squares and the triangle), B3; L5 B2, B3 (tank and block); L8 B1, B2; L9 B1 (diamond dot figures 1 to 3). The L8 figures are built from coordinates with the lesson's `chk()` angle checks (the build would throw if a drawn angle disagreed).

## 4. Slides and numbering

* Printed items now have unique numbers: Start here Q1 to Q6, Think harder **A1 to A4**, Go further **B1 to B3**, Investigation **C** (was 1 to 4, 5 to 7 and 8). The guide, key rows, slide notes and L7's "Think harder A1/A2" labels were renamed to match.
* The slide Think harder slides now print exactly the workbook's A1 to A4 (from the same content, via `rebuild/p5_printed.py`), with the same figures and the answers in the notes; the old slide-only items (for example L3 "3/8 ticket", L5 "tank 1/5 to 3/5", L6 "bath 168 l", L7 "$90 jacket", L8 "rhombus ADC 130") no longer appear. New slides `stretch2`, `gofurther`, `gofurther2` (and `3` where needed) hold the rest; every slide has the one "Make up your own" card under Go further.
* The old Go further slides (`challenge`) now hold only the extras that are not printed (labelled E1, E2 and "extra, not in your workbook"); the "see it" and "walk-through" slides were relabelled to B1/B2 or E1/E2 to match. In L8 both old extras were already printed, so that slide was dropped. Where an old extra was the same as a printed item it is not shown twice.
* Drawn diagrams on the sneak-peek (check) slides, which the re-audit says were missing in L1, L3, L4, L5, L6, L8 and L10: L1 the four digit cards, L3 the two bars (Ali 40, Mei 20), L4 the 6 by 4 grid with the diagonal, L5 the 4 by 3 by 2 box, L6 the 12-litre bar cut into 4 minutes, L8 the right angle with the 30 degree line, L10 the empty 3 by 3 logic table. (L2, L7, L9 already had one.)

## 5. Old labels

"Finished early?" on the L7 ws2 slide is now "Want more? Try the Think harder page. A1 and A2 have a teaching slide first." The "Finished early:" tutor prompts in the explore hints of all ten lessons are now "If a pair wants more:", and `p5/guide.js` "Quick finishers" is "Pairs who want more". No "strong thinkers", "early finishers" or "Finished early" text remains in `p5/`, the Level 5 slides or the generators.

## 6. Problem posing and protected think time

* One "Make up your own" prompt per lesson (`pose` in `p5/content/gaps.js`) is printed at the bottom of the Go further page in a dashed box, ends with "(Think for 30 seconds before anyone speaks.)", appears on the Go further slide and as a row in the tutor guide's Think harder and Go further table (answer: open-ended, check a partner can solve it and exactly one answer fits). No page was added (workbook still 57).
* Protected think time: the explore prediction script in every lesson ("Think for 30 seconds before anyone speaks, and before you touch the objects. Silent thinking. I will show the clock.") and the talk-time rules, which now also cover the Investigation first step and the make-up-your-own prompt. The explore slide notes carry the same line. It uses time inside the existing explore and talk blocks.

## 7. MOE wording (Level 5 only)

"Preview of P6" and "P6 skill" wording is gone from the workbook, slides and content: the Think harder banner is plain, L7's banner reads "A1 is a puzzle that goes further: percentage change", the Go further banner is "a puzzle that goes further", L2's objective and bank item say "a puzzle that goes further", the L7 objective, teaching-slide title and notes say the same, and the L1 hook no longer says "before P6". The L2 lesson slide no longer says "This is a P6 skill". Fraction by whole number and percentage change still appear, only labelled as puzzles that go further. L2 Q1 now says "Remember: 3 / 4 = 3/4 (3 pizzas shared by 4 children)" instead of "a / b". No Level 5 printed item uses "mean".

## Not fixed, and why

* 300 words per Start-here page (see item 2).
* L8 Q3 and Q4 still lean on the printed fact strip (A to F) for an untaught child; a worked first step and fewer steps make them approachable but a child who has not met the angle facts will still need that strip (the explore of tearing corners is the physical way in).
* Some borderline items were left (listed above) because each already carries a printed scaffold.
* `p5/content/inv.js` model answers use "n" for a general number ("n x (n + 1)") in tutor-only text. Left as it is (not printed for children; it is tied to a figure).
* `p5/guide.js` still says "going into P6, the PSLE year" in the level descriptor (an age statement, not a topic claim).
* The slide-only Think harder items listed in item 4 were dropped from the slides, not moved to the bank.

## For the lead (files outside this pass)

* `levels/mkextras.py` line 340 still prints "a short Challenge Screening Set and Challenge Group for children who show the signs" in the parent pack, and line 283 prints "Extension for fast finishers" (taster). The what-is-not-included block also uses "the Gifted Education Programme" in a disclaimer.
* `docs/levels_and_placement.md` and `diag/*` untouched, as agreed.
* The question bank gets longer lists in L2 (9 Think harder), L5 (10), L6 (10) and L1 (9); it is still 28 pages.

## Checks run (Python, exact arithmetic or brute force)

L1: 7 253 609 is the only 7-digit number meeting the six clues; start 7 3 fails Clue 1; numbers rounding to 2 500 000 run from 2 499 500 to 2 500 499 and the digit-sum-9 ones are 2 500 002, 011, 020, 101, 110, 200; closest to 7 000 000 with 1, 2, 5, 6, 7, 8, 9 is 6 987 521 (12 479 away). L2: 7/10 = 1/2 + 1/5, 9/20 = 1/4 + 1/5, 2/3 = 1/2 + 1/6 each have exactly one way; 3/8 has exactly two (1/4 + 1/8, 1/3 + 1/24); digits 1 to 4, closest sum to 1 is 11/12. L3: only 48 and 36 fit Q2; jar 2/5 and 4/15; box 70 and 100 beads. L4: ADE 16, EBF 16, FCD 24, shaded 40; Q1(a) 24. L5: 3000 cm3 and 8 cm. L6: whole-pack ways to 20 cans cost $13.64, $14.24, $14.60 (three ways). L7: 10% of 40 = 4, 24 girls. L8: DEA 62, AEC 118, EAB 62; every drawn angle passed the `chk()` checks.
