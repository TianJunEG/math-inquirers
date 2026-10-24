# Second-round independent audit: Level 3 Extension Workbook

Cold read on 23 Oct 2026 by a model in a fresh session (no child tested). Report only: nothing but this file was written. Files read: `outputs/extension/L3/*Print_BW.pdf` (100 pages, 1-bit CCITT 600 ppi, viewed), `*_vector.pdf` and `*Soft_Copy_Colour.pdf` (text), `extension/data/l3_u01..u10.json`, git history (the round-1 version `dfb0db1` diffed against HEAD), `p3/content/l1..l10.js`, `AUDIT.md`, `PROGRESS.md`, `README.md`.

## Method
- Every answer in the PDF text was read from the printed question and worked by hand (not from the verify scripts): all 75 items that changed since round 1 (found by diff), plus every Start here / Think harder / Go further / Check item in the book on a second pass. 0 wrong answers, 0 unsolvable items, 0 ambiguous keys except the two figure points under M2 and M3 below. `run_checks --level 3`: 459 answers, 0 mismatches (agrees).
- Brute-force by hand-checked reasoning for the risky new ones: digits multiplying to 8 (10 numbers); 1,2,3,4 numbers over 2500 (12) and 7th smallest (2134); 50-60 by 7 with remainder 6 (55 only); pool lessons end 11:00; homework 1 h 20 min; night shift ends 07:15; 2 by 3 grid has 18 rectangles; liar puzzle (Aisha only); pencils 30/45/60/50; fruit grid; clue number 162/252/342; 3 and 5 egg boxes (1, 2, 4, 7); 2/5 with gap 9 is 6/15; plus-sign shape (8 right angles, 4 dents; 10 corners and 3 dents gives 7); 4 cm and 3 cm squares (25, 22, 22); watch 8 min slow; jug puzzle.
- Holiday comparison: (1) fuzzy whole-item match of every L3 stem against every string in `p3/content/*.js` (digits and names normalised); (2) sentence-level 4-gram skeleton match; (3) targeted reading of the sources for each round-1 H1 row. `dup_check --level 3`: OK, 0 FAIL, 14 REVIEW lines (reviewed, see C-list). `wording_lint --level 3`: 0 errors, 169 warnings.
- Pages viewed as images at 90 dpi: 3, 4, 5, 6, 10, 11, 23, 27, 30, 34, 36, 41, 50, 52, 57, 58, 59, 63 to 67, 69 to 73, 75, 77; zoomed at 200 to 300 dpi: 58 (angle X), 59 (dot grid), 70 and 75 (bar graphs). Page numbers: every unit start (6, 13, 20, 27, 34, 41, 48, 55, 62, 69), the answer-unit starts (80, 82, 84, 86, 88, 90, 92, 94, 96, 98), the pace plan and the "page N" references checked in both PDFs; all correct, both editions 100 pages, build report 0 problems, no overflow.

## Verdict
**Almost sell-ready: one short fix pass, then ship. Not sell-ready as it stands.** The mathematics and the keys are sound, the layout is clean, and all four round-1 High points are mostly closed. But the "clone" fix is incomplete: five items are still the holiday item with new numbers or a new noun, one is an exact copy of a holiday question, and one new edit introduced a wrong name in a question. These are quick text edits. A child trial for pace and reading load is still outstanding (as in round 1).

## Round-1 High and Medium: status

| Round 1 | Status | Evidence |
|---|---|---|
| H1 holiday clones (about 15 items) | **Mostly closed, 5 still open** | Closed with a genuinely new idea and numbers: U9 T1 (pool lessons), S8 (melon and apples), T2 (homework with break), G4 (night shift), C3 (bus trip); U10 T1 (rectangles in a 2 by 3 grid), S9 (think of a number), C3 (new cards, see C6); U7 T3 (two squares joined); U3 T1 (Aisha, tens digit odd), G4 (square numbers), C3 (63 in the 6 table); U8 T3 (plus sign); U1 T2 (digits multiply to 8), T3 (1 to 4 cards), S9 (3000 down 250); U4 Try and S11 (new nouns). **Still open: see C1 to C6.** |
| H2 U10 Check Q1 graph unreadable | **Closed** | Labels 0, 20, 40, 60 with dashed lines at 10; clean at 300 dpi; Monday 20, Tuesday 50, answer 30 correct. The S1 graph (labels every 5) also clean. |
| H3 answer boxes too narrow | **Closed** | `{bw}` boxes on all times with pm, 24-hour times and money (U4 S9, S12, T2; U9 S6, S7, S9 to S12, T1, G2, G4, C4; U10 S10). All fit, none runs off the page (viewed pp. 30, 31, 64 to 67). |
| H4 Learn pages miss ideas | **Partly closed** | U1: good (worked example plus a new Try, "greatest even number", which is a real step up). U4: "More models" box has three one-line rules (times as many, total and difference, same after giving); no worked numbers, "half the gap moves" is cryptic for an 8-year-old. U5: one rule added ("a leftover person still needs a seat: use 1 more group"), no worked example, although the Learn page has about 15 percent blank space at the bottom. U6: rule line "multiply top and bottom by the same number. 1/3 = 2/6 = 4/12" added; the wall shows only halves, quarters, eighths. See M1. |
| M1 U8 S10 angle X | **Closed** | A 3/4 arc is now drawn inside the dent (viewed at 300 dpi); the X mark touches the arc (cosmetic, L4). The spoiler rule in S2 was removed, which created M4 below. |
| M1 U7 T3(c) orientation | **Closed** | Item replaced. |
| M1 U3 S10 six blank rows | **Closed** | 8 rows; "2 rows of 15 and 15 rows of 2 are different ways" is stated. (But the Why is now just "That is 6 ways", see M5.) |
| M1 U5 G4(b) four boxes | **Closed** | A line. |
| M1 U10 T3 "A graph shows" with no graph | **Closed** | Reworded; "Draw your bars" kept. |
| M1 U7 S7 labels a, b | **Closed** | "b" beside the vertical edge, "a" above the horizontal edge. |
| M1 hints that give the method | **Closed** | U9 T3, U4 T2, U10 T2 hints and labels reworded; U5 G2, U7 T1 hints no longer finish the problem. |
| M2 fractions printed as 3/4 | **Open (accepted by builder)** | Still slash text in stems, boxes and Learn. Figures are stacked. Not a blocker, but the Learn page is where the child first meets the two styles. |
| M3 Primary 5-6 Think harder unlabelled | **Closed** | `Beyond Level 3` badge on U2 T3, U4 T1/T3/G2, U5 T3, U9 T3 and the Go further items; the badge renders correctly (viewed pp. 11, 66, 67). U5 T2 (three remainders) is the only heavy item left unlabelled; fine. |
| M4 draw-the-problem unit | **Closed** | U4 S5 now has a blank "Draw your model". |
| M5 list lines too short | **Closed** | Lines now long enough on U1 S7, U10 S6. |
| M6 Welcome equipment | **Closed** | "You will need: a pencil, a rubber, a ruler and a paper corner." Welcome page fill 97.7 percent, 5.8 mm to spare, no overflow, no long notes. |
| M7 small U8 figures | Open, accepted | S1 widened from 100 to 110 mm. Legible in 1-bit. |
| M9 close to private frames | Accepted | |
| Low 1 contents titles | **Closed** | Child title plus one subtitle line. |
| Low 2 DRAFT licence line | **Open** | Still printed on p2 in both editions ("DRAFT licence text, for owner and lawyer approval. Not final."). Shared asset; must go before sale. |
| Low 3 U7 S3 Why unit | **Closed** | "36 / 4 = 9 m". |
| Low 4 certificate plaque | **Open** | Still pseudo-text on the plaque (p77). Shared asset. |

## Remaining items

### Must fix before selling (clones and one bug)
**C1. U6 Think harder 2 (p45) is the holiday item, wording nearly verbatim.** L3: "A fraction is equal to 2/5. Its bottom number is 9 more than its top number. Write the fraction." Holiday l6: "A fraction is equal to 2/3. Its bottom number is 4 more than its top number. What is the fraction?" The round-1 fix only dropped "I am". Use a different condition (for example "top and bottom add up to 21", or "bottom is double the top plus 1" family) and a different frame.

**C2. U5 Start here 6(b) (p36) is still the holiday item.** L3: "A number between 50 and 60 is divided by 7. The remainder is as great as it can be." Holiday l5: "A number between 60 and 70 is divided by 8. The remainder is as big as it can be. What is the number?" Only numbers changed (twice). Change the idea, for example "the greatest 2-digit number that leaves remainder 5 when divided by 8", or "the smallest number over 50 that leaves the greatest remainder when divided by 6".

**C3. U5 Start here 5 (p36) is the holiday oranges item with coins.** L3: "9 full piles of 5 and 4 left, then stack again in piles of 6: how many piles, how many left." Holiday l5: "Siti fills 9 bags with 7 oranges each and has 5 left. She packs all the oranges again into bags of 8. How many full bags? How many are left over?" Same 9, same structure; the round-1 note named the marbles version (also in l5) and this is the same family. Change structure, for example give the total and ask for the groups, or "piles of 5 leave 4, piles of 6 leave 1: find the number between 40 and 60".

**C4. U7 Check yourself 2 (p54) is a word-for-word holiday question; U7 Learn Try is the other holiday warm-up.** C2: "A square has sides of 6 cm. Its perimeter is __ cm." = holiday l7 warm-up "A square has sides of 6 cm. What is its perimeter?" (answer 24, same). Learn Try (p48): "A rectangle is 8 cm long and 3 cm wide. Area and perimeter" matches the holiday warm-up "A rectangle is 8 cm by 3 cm. What is its area?" Also U7 S4 and C4 reuse the holiday frame "A rectangle has a perimeter of 12 cm. Its length is 4 cm" (30/9 and 22/4). Change at least C2 and the Try numbers; S4 and C4 can stay as "same type".

**C5. U3 Check yourself 2 (p26) is still the holiday frame.** "You know that 10 x 8 = 80. Use it to find 9 x 8." Holiday l3: "You know 5 x 9 = 45. Use it to find 6 x 9." It was a round-1 row and only the numbers changed. Replace with a different kind of question (for example "Fill in 7 x 8 = 7 x 4 + 7 x __").

**C6. U10 Check yourself 3 (p75) is the same item as the holiday cards question with other cards.** L3: "Use the cards 2, 5 and 6 once each to make 3-digit numbers. __ of the numbers are odd." Holiday l10: "Make all the 3-digit numbers you can with the digit cards 1, 4 and 7 (use each card once). Which of them are even?" Start here 6 in the same unit is the same type (cards 3, 6, 9, list, count the even ones), so the unit now asks it twice. Replace C3 with something else from the unit (a table or a graph reading).

**C7. U5 Think harder 3 (p38) is the holiday pens-and-pupils item.** L3 "Aisha shares crayons among her cousins. 3 each: 11 not used. 5 each: 7 more needed. How many cousins? How many crayons?" Holiday l5: "Mr Lim gives pens to his pupils. 4 each: 10 left over. 6 each: 4 short. How many pupils? How many pens?" Same frame and answer method with new numbers. Round 1 only called it Primary 5 to 6; it is also a clone. Change to a different structure (for example three plans, or a total with a different relation) or move to Beyond with a new story.

**C8. U4 Start here 11 (p30) has a wrong name in the question (introduced by the replace).** "Kumar says the shop has 54 + 18 = 72 blue pens. (a) Is **Ravi** right?" The key and Why say "Kumar added instead of subtracting". Fix the part to "Is Kumar right?". (The round-1 version said Ravi in both places; the stem was changed and the part was not.)

### Should fix
**M1. Learn pages are still thin for U4 and U5 (H4 residue).** Add one worked line each: U4, one line per model (for example "Ben has 3 times as many as Ali, 48 in all: 4 equal boxes, 12 each"; "Both get 5 more: the gap stays"); U5, a one-line round-up example (26 people, cars of 5: 5 cars leave 1 person, so 6 cars). U5 Learn has room.

**M2. U8 Think harder 2 (p59): the label C is next to the wrong dot.** The C dot is in column 3 of the top row (label drawn 26 units to its left), but the label sits between columns 2 and 3 and touches the column-2 dot ("." then "C" then ". "). A child who starts at the column-2 dot follows a perpendicular that ends under Q, and is marked wrong (key R). Put the label above the dot or ring the dot. The Why also reads "reaches the dot at 3 across, 4 up, then (4, 2), then the bottom row at R" (coordinates the child never sees); rewrite as "Go 1 across and 2 down, again and again, until you reach the bottom row."

**M3. U8: the word "dent" is no longer explained anywhere in the child's pages.** The S2 rule that defined it was removed (good, it was a spoiler), but Think harder 3 asks "It has __ dents" and its hint says "Count the dents first". Add one phrase to the Learn page, "a corner that points into the shape (a dent) is greater than a right angle", and use "dent" consistently (also used in U7).

**M4. U8 Check yourself 2 (p61) "Circle each letter with 2 parallel lines. E H V T": the key is E and H, and the Why says "E has 3 parallel arms".** A child who reads "2" literally circles H only and is marked wrong. Reword: "Circle each letter that has parallel lines." (Also S3(a) counts F, which has 2 parallel arms.)

**M5. Shortened Whys.** Mean length 124 characters; 99 percent still explain. Weak spots for a self-study child:
- **U3 S10 (p23) Why = "That is 6 ways."** It used to list 2 x 15 to 15 x 2. A child who found 4 ways cannot see what was missed. Restore the list ("2 rows of 15, 3 of 10, 5 of 6, 6 of 5, 10 of 3, 15 of 2").
- **U7 Check 1 and 2 (p54)** "9 x 5 = 45 cm²." and "4 x 6 = 24 cm." say nothing about why (area = length x width; 4 equal sides).
- **U2 Think harder 3 (p17)** the magic-total argument lost its link ("which is 3 totals + 3 x the middle" with no "4 lines = 4 totals"); a child cannot follow it. It is a Beyond item, so low risk.
- U8 T2 Why (M2) and U9 C04 "5.00 - 2.35 = 2.65" (fine).
All other short Whys are just a sum (a Start here with an arithmetic answer) and are adequate, and the checks ("Check: ...") that were cut were not needed.

**M6. U4 Think harder 1 and U4 Start here 10 are the holiday marbles story.** L3 T1: "Kumar and Wei have 84 marbles in all. Kumar has 3 times as many as Wei. Kumar gives some to Wei so they have the same." Holiday l4: "Ben had 3 times as many marbles as Ravi. Ben gave Ravi 20 marbles, and then they had the same number. How many did Ben have at first?" Same story and idea; the question is reversed and the total is given. Accept as "same type" or change the noun and the unknown. Also U4 T3 "Ravi is 7 years old" repeats the holiday "Ravi is 7 years old ... in how many years" (different question).

**M7. U9 Start here 4 (p63) is the holiday juice jug item.** "2 l 500 ml, cups of 400 ml: how many cups, how much left" vs l9 "A 2 l bottle of juice is poured into cups. Each cup holds 300 ml. How many cups? How much left?" Same type; accept, or change the story. The U9 Learn example (ribbon 2 m 35 cm) uses the exact 2 m 35 cm = 235 cm of the holiday mini-lesson and the Learn film (2:50 pm) matches the holiday 2:50 pm items; move one number each.

### Low
- L1. U10 T1 (p73): "1 by 2: 1 by 3: ..." never says rows by columns (the Why says 2 wide, 1 tall). The total does not depend on it, but the part counts do; add "(rows by columns)".
- L2. U10 Check Q1 (p75): the dashed lines are not explained on this page (Q is 50, on a dashed line). Add "Each dashed line is 10."
- L3. U10 S5(a) and S5(b) both answer 9, and the Learn example and Try both answer 8; vary one so a child cannot copy.
- L4. U8 S10: the X mark overlaps the angle arc; move the X outside the arc.
- L5. U5 S13 "Divide 47 by 4, 5, 6, 7, 8" is the holiday "Mei has 29 beads, bags of 4, 5, 6: which leaves the most" idea; accept.
- L6. U1 Learn (a 4-digit "Th H T O" line and a Try) is fine; U1 S11 and C-list frames are generic, accepted.
- L7. `wording_lint`: 169 WARN, 0 errors. Nearly all are "no command or question word" on fill-in sentences ("The line has [ ] children.") and day abbreviations (Mon, Tue ...). U10 T3 now fine. U10 Check 1 and 2 (and U5 C01, U9 C01, C02) are sentence-completion items with the blank inside a sentence: acceptable for this age and unambiguous. No change required.
- L8. Pace plan sub-headings under 9 pt (round-1 Low 12) not re-measured; certificate plaque and DRAFT line are shared assets (round-1 Low 2 and 4).

## What was checked and is fine
- All new Learn content: U1 (Try 8314 correct), U4 (rules), U5 (rule), U6 (rule, 7/12 < 2/3 uses 1/3 = 2/6 = 4/12), U10 (6th from front, 3rd from back, 8 children; Try Lily 8). Wording is plain and sentences are short.
- U10 Check yourself Q1 graph: readable (see H2). U10 S1 graph (draw Kumar's bar): labels 0 to 35 in 5s, all legible at 300 dpi, answer 25 for Kumar fits the grid.
- `{bw}` boxes: width right for "4:35 pm", "21:05", "24.85", "14.45", "07:15", "11:00" (viewed). Narrow boxes remain only for 1 to 3 character answers.
- "Beyond Level 3" badge text and placement (Go further and Think harder pages, for example pp. 11, 66, 67): correct, one line, no clash with the item number.
- Contents, pace plan and every unit's answer start page (80 to 98) match the PDF; item references "page N" checked on a sample of about 10 (all correct).
- 1-bit legibility at zoom of changed pages: bar graphs (pp. 70, 75), clocks and jugs (pp. 64, 65), plus sign and dot grid (p59), L-shape with arc (p58), staircase of squares (p52): all clean, no grey, no filled blobs.
- No SASMO, school or paper names; no private-source copy (`dup_check` external scan ran: OK).

## Ranked fix list (for the builder)
1. C8 fix "Is Ravi right?" to Kumar (U4 S11).
2. C1, C2, C3, C5, C6, C7: replace or restructure these six items (U6 T2, U5 S6b, U5 S5, U3 C2, U10 C3, U5 T3).
3. C4: change U7 C2 and the U7 Learn Try (exact holiday numbers).
4. M2: relabel dot C on U8 T2 and simplify its Why; M3 define "dent" on the U8 Learn page; M4 reword U8 Check Q2.
5. M5: restore the list in the U3 S10 Why and add a reason to U7 C1/C2 Whys.
6. M1: one worked line each on the U4 and U5 Learn pages.
7. L1, L2, L3, then the shared assets (DRAFT licence line, plaque).
8. Rebuild, run `verify_all.sh 3`, and run a child trial.

After items 1 to 5 I would call the book sell-ready (maths, answers, layout and 1-bit print all pass); 6 to 8 are polish plus the trial.
