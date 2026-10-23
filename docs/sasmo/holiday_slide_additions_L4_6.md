# Holiday slide and tutor-bank additions, Levels 4 to 6 (owner decision GAPS-SLIDES-NOW)

Written 23 Oct 2026. Source of the plan: `docs/sasmo/holiday_skill_coverage.md` sections 4 to 6 (proposals, host lessons, tools), 7 (tool mapping) and 8 (slide/bank route). The sibling job for Levels 1 to 3 is in `docs/sasmo/holiday_slide_additions_L1_3.md`.

## 1. What was added (counts)

| Level | Slide items (optional slides) | Bank items (same skill, new numbers) | Decks changed | Ratio previews included |
|---|---|---|---|---|
| 4 | 11 | 9 | 6 | no |
| 5 | 25 | 21 | 9 | 7 (see section 4) |
| 6 | 20 | 18 | 8 | no (percentage and rate tasters only) |
| Total | 56 | 48 | 23 | |

Every item is an ADDITION. No printed question was swapped. Nothing printed, no print file, no `outputs/print/**`, no weekly PDF, no workbook file and no `pN/content/*.js` was edited, so no workbook page number or question number changed. The hidden 850 px spacer in `p5/wb_pdf.py` was not touched.

## 2. How it is built (so it survives a rebuild)

- Data: `levels/gap_items.py` (the only place the items live). Each item has the skill, one of the 8 strategy names from `levels/spine.json` as its tool, question lines, answer, SAY / ASK / LISTEN FOR, a worked WHY for the tutor, and a same-skill variant with its own answer.
- Slides: `levels/gap_slides.py` writes one optional slide per item (`split/pNlM/project/slides/pNlM-gap-<id>.html`, pill "Optional, if you finish early", a "Tool: ..." chip, answer on a click, SAY / ASK / LISTEN FOR / WHY and the variant in the speaker notes) and puts it in `deck.json` just before the talk (or showcase) slide. It is wired into `levels/restyle.py` after `mi_deco`, so `gen_*` rebuild followed by `restyle.py` keeps the slides. It is idempotent: the second `restyle.py` run over all 30 Level 4-6 decks changed 0 files.
- Bank and tutor sheet: `levels/gap_bank.py` writes `p4/qbank_skills.json`, `p5/qbank_skills.json`, `p6/qbank_skills.json` (same format as the Level 1-3 job: slide items and bank items) and the digital tutor sheets `outputs/skill_additions/Math_Inquirers_L4_Skill_Additions_Tutor_Sheet.{html,pdf}` (L5, L6 likewise). These are digital tutor material, not printed.
- Tutor console data: `tutor/build_data.py 4`, `5`, `6` rebuilt. The new slides are marked optional and sit in the part of the lesson before them, so they add no minutes. Every one of the 30 lessons still totals 90.0 minutes.
- Checks: `levels/gap_verify.py` (independent brute-force or exact-arithmetic checker for every answer and every variant answer: 104 checks, 0 failures) and `levels/gap_dupcheck.py` (7-word-run check, logic copied from `extension/verify/dup_check.py`, against the holiday text of all levels, the term lessons, the extension data and the git-ignored private source files; a hit in a private file prints only the file name). Result: no shared 7-word run. No source question text was read into any file.
- Layout: all 56 slides rendered at 1920 by 1080 and viewed (contact sheets); no overflow after two fixes (a table and a spinner were too tall). Mi is not placed on any new slide (Mi stays on title, break and the last slide only; `mi_deco` is unchanged).

Wording follows `term/l1/WORDING_GUIDE.md` scaled up: numerals, fixed command words (Find, How many, Count), names from the standard cast, no teaching inside a question, no price, no claim about any exam. The notes use "say the answer together on three"; nothing is held up to the camera.

## 3. Every new item

Slide ids are the slide files. "Check done" names the independent check; all items also passed the duplicate check. The bank variant of each item (where marked) is in the speaker notes, `pN/qbank_skills.json` and the tutor sheet.

### Level 4

| Lesson | Slot (slide id) | Skill | Tool | Answer | Check done |
|---|---|---|---|---|---|
| L4.1 | `p4l1-gap-digit` (Think harder) + bank variant | Digit tests for 3 and 6 | Spot the pattern | (a) 724: digit sum 13, no. 618: digit sum 15, yes. (b) The box can be 2 or 8: 582 and 588. | filter 580-589 for multiples of 6; digit sums by code; 7-word duplicate check clean |
| L4.1 | `p4l1-gap-weekday` (Think harder) + bank variant | Weekdays and remainders | Make a table | (a) Thursday. (b) Monday. | calendar dates (datetime); 7-word duplicate check clean |
| L4.2 | `p4l2-gap-cr1` (Think harder) + bank variant | Letter sums | Guess and check | P = 5, Q = 1, R = 9, S = 0.  Check: 51 + 59 = 110. | all 10P4 digit assignments: exactly 1 solution; 7-word duplicate check clean |
| L4.2 | `p4l2-gap-cr2` (Go further) | Letter sums, a longer one | Guess and check | D = 8, A = 3, E = 1, C = 4, B = 0.  Check: 883 + 148 = 1031. | all digit assignments: exactly 1 solution; 7-word duplicate check clean |
| L4.3 | `p4l3-gap-pair` (Go further) + bank variant | Adding a list by pairing | Try something simpler | (a) 11 numbers. (b) 286. | list built and summed by code; 7-word duplicate check clean |
| L4.3 | `p4l3-gap-gap` (Think harder) + bank variant | Gaps that grow | Make a table | (a) 23 coins. (b) 57 coins. | sequence rebuilt with growing gaps; 7-word duplicate check clean |
| L4.6 | `p4l6-gap-fan` (Go further) + bank variant | Triangles by size | List every way | (a) 3 triangles of size 1, 2 of size 2, 1 of size 3. (b) 6 triangles altogether. | all pairs of base points, grouped by span; 7-word duplicate check clean |
| L4.9 | `p4l9-gap-spin` (Think harder) | Spinners with unequal parts | Draw it | (a) 1/6. (b) Yellow. (c) About 30 times (green about 20, blue about 10). | exact fractions (Fraction); 7-word duplicate check clean |
| L4.10 | `p4l10-gap-time` (Think harder) + bank variant | Timetables, trying both orders | List every way | (a) The post office first. (b) 4:05 pm. | both orders simulated minute by minute (opening and closing times); 7-word duplicate check clean |
| L4.10 | `p4l10-gap-dice` (Think harder) + bank variant | Smallest and largest totals | List every way | (a) 4. (b) 24. (c) 3 and 25 are impossible. | all 6^4 rolls enumerated; 7-word duplicate check clean |
| L4.10 | `p4l10-gap-stages` (Think harder) + bank variant | Counting in two stages | List every way | (a) 24 outfits. (b) 22 outfits. | all 4x3x2 outfits enumerated, pair removed; 7-word duplicate check clean |

### Level 5

| Lesson | Slot (slide id) | Skill | Tool | Answer | Check done |
|---|---|---|---|---|---|
| L5.1 | `p5l1-gap-digit` (Think harder) + bank variant | Digit sums and the greatest number | Guess and check | (a) 35. (b) 97542. | all 5-card permutations; 7-word duplicate check clean |
| L5.1 | `p5l1-gap-parity` (Think harder) + bank variant | Regroup first, then work out | Try something simpler | (a) 17 000. (b) (i), (ii) and (iv) are odd. (iii) is even. | expressions evaluated, parity read off; 7-word duplicate check clean |
| L5.1 | `p5l1-gap-cr1` (Think harder) | Letter sums | Guess and check | A = 1, B = 0, C = 8, D = 9, E = 3.  Check: 888 + 131 = 1019. | all digit assignments: exactly 1 solution; 7-word duplicate check clean |
| L5.1 | `p5l1-gap-cr2` (Go further) | A multiplication in letters | Guess and check | K = 8, M = 4, N = 3, P = 6.  Check: 84 × 4 = 336. | all digit grids: exactly 1 solution; 7-word duplicate check clean |
| L5.2 | `p5l2-gap-r4` (Think harder) + bank variant | Ratio and fractions (preview) | Draw it | (a) 3/8. (b) 5/8. (c) 15 red counters. | exact fractions; 7-word duplicate check clean |
| L5.3 | `p5l3-gap-r1` (Preview) | What is a ratio? (preview) | Draw it | (a) 6 tins of white, because 4 : 6 is the same ratio as 2 : 3. (b) 5 units altogether. One unit is 20 ÷ 5 = 4 tins. Blue 8 tins, white 12 tins. | arithmetic by Fraction; 7-word duplicate check clean |
| L5.3 | `p5l3-gap-r2` (Preview) + bank variant | Equal ratios and simplest form (preview) | Make a table | (a) 6 : 9. (b) 2 : 3 (divide both numbers by 3). (c) 15 cups of water. (d) 18. | gcd and scaling; 7-word duplicate check clean |
| L5.3 | `p5l3-gap-r3` (Preview) + bank variant | Sharing in a ratio (preview) | Draw it | (a) 9 parts. (b) 5 stickers. (c) Mei 20 stickers and Siti 25 stickers. (d) 5 more stickers. | division checked (exact); 7-word duplicate check clean |
| L5.5 | `p5l5-gap-dice` (Go further) + bank variant | Dice and hidden faces | Act it out | 17 dots. | all die orientations: total is constant; 7-word duplicate check clean |
| L5.6 | `p5l6-gap-pack` (Go further) + bank variant | Totals you cannot make | Make a table | (a) 5, 8, 10, 13, 15, 16, 18, 20. (b) 27. | reachable totals by table up to 400; 7-word duplicate check clean |
| L5.6 | `p5l6-gap-catch` (Think harder) + bank variant | Catching up | Make a table | (a) 300 m. (b) 20 m. (c) 15 minutes. | minute-by-minute simulation; 7-word duplicate check clean |
| L5.6 | `p5l6-gap-work` (Go further) + bank variant | Three workers | Make a table | (a) 120 bricks. (b) 16 minutes. | minute-by-minute simulation; 7-word duplicate check clean |
| L5.6 | `p5l6-gap-r5` (Think harder) + bank variant | Equal ratios and scaling (preview) | Make a table | (a) 15 cups of water. (b) 10 cups of rice. (c) 12 + 30 = 42 cups altogether. | scaling arithmetic; 7-word duplicate check clean |
| L5.7 | `p5l7-gap-r6` (Think harder) + bank variant | Ratio and percentage (preview) | Draw it | (a) 3/5. (b) 40%. (c) 18 boys. | exact fractions; 7-word duplicate check clean |
| L5.8 | `p5l8-gap-year` (Think harder) + bank variant | Weekdays in a year | Spot the pattern | (a) 52 weeks and 1 day. (b) 53 Tuesdays. (c) Tuesday. (d) Wednesday. | calendar (datetime, 2019); no other weekday has 53; 7-word duplicate check clean |
| L5.9 | `p5l9-gap-last` (Think harder) + bank variant | Last digits of products | Spot the pattern | (a) 9. (b) 4. | pow(.,.,10); 7-word duplicate check clean |
| L5.9 | `p5l9-gap-range` (Think harder) + bank variant | Multiples in a range | Try something simpler | (a) 57 multiples of 7. (b) 28 multiples of 14. | list of multiples counted; 7-word duplicate check clean |
| L5.9 | `p5l9-gap-gaps` (Think harder) + bank variant | The gap of the gaps | Make a table | (a) The gaps are 1, 3, 5, 7. They go up by 2 each time. (b) 51 blocks. (c) 83 blocks. | sequence rebuilt; 7-word duplicate check clean |
| L5.9 | `p5l9-gap-woven` (Think harder) + bank variant | Two sequences woven together | Spot the pattern | (a) 38 and 19. (b) 31. (c) 22. | formula checked against the shown terms; 7-word duplicate check clean |
| L5.9 | `p5l9-gap-op` (Think harder) + bank variant | A rule from examples | Make a table | (a) 30. (b) 7. | all integer rules p*a*b+q*a+r*b+s fitting the 4 examples give one answer; 7-word duplicate check clean |
| L5.10 | `p5l10-gap-tri` (Think harder) | Triangles by size | List every way | 12 triangles. | exact geometry: every triple of segments tested for a real triangle; 7-word duplicate check clean |
| L5.10 | `p5l10-gap-bounds` (Think harder) + bank variant | Counting numbers in bounds | List every way | 9 numbers: 303, 312, 321, 330, 402, 411, 420, 501, 510. | all 299 numbers filtered; 7-word duplicate check clean |
| L5.10 | `p5l10-gap-pile` (Go further) + bank variant | Least possible, the fullest bag | Guess and check | 8 marbles. | all 4-subsets of 1-23 summing to 23; 7-word duplicate check clean |
| L5.10 | `p5l10-gap-evencap` (Go further) + bank variant | Greatest possible with a rule | Guess and check | 56. | all 6-subsets of 1-12; 7-word duplicate check clean |
| L5.10 | `p5l10-gap-r7` (Go further) + bank variant | Ratio and the difference (preview) | Draw it | (a) 3 parts. (b) 8 marbles. (c) Kumar 56 marbles and Wei 32 marbles. | exact arithmetic; 7-word duplicate check clean |

### Level 6

| Lesson | Slot (slide id) | Skill | Tool | Answer | Check done |
|---|---|---|---|---|---|
| L6.1 | `p6l1-gap-rate` (Go further) + bank variant | Meeting and catching up | Draw it | (a) 1.5 hours. (b) 10:30. | exact fractions and clock arithmetic; 7-word duplicate check clean |
| L6.1 | `p6l1-gap-tele` (Think harder) + bank variant | Sums that cancel | Spot the pattern | (a) 1/12. It is the same as 1/(3 × 4). (b) 7/30. | exact Fraction sum of 7 terms; 7-word duplicate check clean |
| L6.2 | `p6l2-gap-d9` (Think harder) + bank variant | Digit sums for 3 and 9 | Spot the pattern | (a) 6 372 and 5 481. (b) 7 296. | divisibility by code; 7-word duplicate check clean |
| L6.2 | `p6l2-gap-d45` (Go further) + bank variant | Tests for 5 and 9 together | List every way | 6 030, 6 930 and 6 435. | all 100 digit pairs tested; 7-word duplicate check clean |
| L6.2 | `p6l2-gap-zero` (Think harder) + bank variant | Zeros at the end | Try something simpler | 4 zeros. | product multiplied out; 7-word duplicate check clean |
| L6.4 | `p6l4-gap-pct` (Think harder) + bank variant | Percentage change, with units | Draw it | (a) $80. (b) 20 more stickers. | exact arithmetic; 7-word duplicate check clean |
| L6.4 | `p6l4-gap-pipe` (Think harder) + bank variant | A rate as an equation | Make a table | (a) 20 litres each minute. (b) 18 minutes. (c) 90 minutes. | arithmetic; 7-word duplicate check clean |
| L6.4 | `p6l4-gap-short` (Think harder) + bank variant | Shortcuts before calculating | Try something simpler | (a) 1. (b) 65. | both expressions evaluated; 7-word duplicate check clean |
| L6.5 | `p6l5-gap-votes` (Go further) + bank variant | Worst case, the runner-up | Act it out | 5 more votes. | every split of the remaining votes tested; 7-word duplicate check clean |
| L6.5 | `p6l5-gap-socks` (Think harder) + bank variant | Worst case, how many to be sure | Act it out | (a) 4 socks. (b) 7 socks. (c) 15 socks. | every draw vector enumerated (worst case); 7-word duplicate check clean |
| L6.5 | `p6l5-gap-size` (Think harder) + bank variant | Squares and rectangles by size | List every way | (a) 26 squares. (b) 90 rectangles. | every rectangle in the grid enumerated; 7-word duplicate check clean |
| L6.5 | `p6l5-gap-derange` (Go further) + bank variant | Nobody in their own place | List every way | 9 ways. | all 24 permutations listed; 7-word duplicate check clean |
| L6.7 | `p6l7-gap-perim` (Think harder) + bank variant | Perimeter of a staircase | Try something simpler | (a) 48 cm. (b) 80 cm. | outline polygon built and its edges summed; 7-word duplicate check clean |
| L6.7 | `p6l7-gap-quarter` (Go further) + bank variant | A quarter circle in a square | Draw it | 21.5 cm². | 100 - 3.14 x 100 / 4; 7-word duplicate check clean |
| L6.7 | `p6l7-gap-clock` (Think harder) + bank variant | Angle between the clock hands | Draw it | (a) 20°. (b) 65°. | hand angles computed; 7-word duplicate check clean |
| L6.8 | `p6l8-gap-cr1` (Think harder) | Letters stand for digits | Guess and check | D = 5, E = 7, C = 3, A = 1, B = 4.  Check: 573 + 771 = 1344. | all digit assignments: exactly 1 solution; 7-word duplicate check clean |
| L6.8 | `p6l8-gap-cr2` (Go further) | Letters stand for digits, a longer one | Guess and check | B = 9, D = 5, E = 6, A = 1, C = 0.  Check: 956 + 105 = 1061. | all digit assignments: exactly 1 solution; 7-word duplicate check clean |
| L6.8 | `p6l8-gap-last` (Think harder) + bank variant | Last digit of a power | Spot the pattern | (a) 2. (b) 9. | pow(.,.,10); 7-word duplicate check clean |
| L6.9 | `p6l9-gap-pct2` (Think harder) + bank variant | Percentages from a table | Make a table | (a) 8 children. (b) 45%. (c) 35%. | exact fractions; 7-word duplicate check clean |
| L6.10 | `p6l10-gap-pack` (Go further) + bank variant | The greatest total you cannot make | Make a table | 23 stickers. | reachable totals by table up to 400; 7-word duplicate check clean |

Level 4 placement notes: the spinner item went to Lesson 9 (Data Detectives, tables and graphs) instead of Lesson 10 (the report allowed either L10 or L8); all other hosts follow the report. Level 5 and 6 hosts follow the report, with the ratio items placed as in section 4.

## 4. Level 5 ratio strand (owner decision of 23 Oct 2026: ratio IS in the Level 5 holiday, as a preview)

The earlier instruction to leave ratio notation out was reversed. Seven slide items teach `a : b` from first principles and are labelled on the slide "PREVIEW: a Primary 6 topic, beyond Level 5. A taste, not a test." (no examination body is named). The notes carry a one-sentence spoken label and each item uses the bar model the Level 5 course already uses.

| Idea | Slide (host lesson) |
|---|---|
| Meaning of a ratio ("for every"), equivalent ratios, a worked example of a share with a total, link to the bar model | `p5l3-gap-r1` (L5.3 Before and After) |
| Equivalent ratios (scaling up and down), simplest form | `p5l3-gap-r2` (L5.3) |
| Part-whole with a total, "one part" reasoning | `p5l3-gap-r3` (L5.3) |
| Ratio and fractions (a : b gives a/(a+b) of the whole) | `p5l2-gap-r4` (L5.2 Fraction Feats) |
| Equal ratios and scaling with a table (a rate is a ratio in disguise) | `p5l6-gap-r5` (L5.6 Rate Racers) |
| Ratio and percentage | `p5l7-gap-r6` (L5.7 Percentage Puzzles) |
| Ratio and a given difference ("the difference in parts is the difference in amounts") | `p5l10-gap-r7` (L5.10 Challenge Day) |

Not included, on purpose: ratio with a change (before and after), three-part ratios, ratio of three quantities, averages. `p5/SPEC.md` still says ratio notation is avoided in the printed program; that sentence is now out of date for the slides and should be reworded by the owner when the v2 spec is written (not edited here, to keep the printed spec frozen).

What a PRINTED v2 workbook addition would need (Level 5):
1. A decision on where ratio sits in the printed lessons: the natural place is a short "Ratio preview" box on the Think harder or Go further page of Lessons 3 (after the bar-model pages), 2 and 7, or one full page in Lesson 3 replacing an over-served bar-model item. Printed additions must REPLACE an existing printed item (the page count of each lesson is fixed).
2. For each printed item: the question in the workbook, the answer key line, the tutor-guide answer line, the question-number references in the guide and the weekly PDF, and the deck's matching slide kept in step (these slide items can be reused word for word).
3. The workbook, guide, weekly zip and print PDF rebuilt and checked against `outputs/print/print_spec.json` (page counts, blank backs, cut-out pages), plus a B&W check (`print/check_bw.py`). The 850 px spacer in `p5/wb_pdf.py` must stay.
4. A short vocabulary line for the kit or the start-here page ("a : b is read 'a to b'; it means for every a there are b"), and an owner decision on whether the notation appears in the Level 5 parent pack.
5. Estimated cost (report section 8): about 1.5 agent-hours per printed swap plus 3 hours of per-level overhead.

## 5. What a child and a tutor see, and honest limits

- The slides are "Optional, if you finish early": they reach children who finish early and tutors who set them live. They do not give every child independent practice (the report says the same about the slide route). The tutor sheet PDFs hold the same text for tutors who prefer paper to the phone.
- Bank items exist only as tutor material (JSON, tutor sheet and speaker notes). They are not wired into `hp/qbank.json`, the Question Bank PDF or `practice/` (those read other files and could reach a printed or published page).

## 6. Not done, and why

1. Tutor guides (`p4/guide.js`, `p5/guide.js`, `p6/guide.js`, with their PDF, HTML, docx, weekly zips): NOT rebuilt. A guide rebuild also rebuilds the weekly PDFs that embed frozen workbook pages and the print files. The items reach the tutor through the speaker notes (tutor phone), `tutor/data` and the tutor sheet PDFs. If the owner wants them inside the guide, add an appendix from `pN/qbank_skills.json` after the freeze lifts.
2. Online practice (`practice/`) and the Level 1 Question Bank doc: not changed (see section 5).
3. Items the report said to leave to the extension book or not build: visual perception, picture-heavy spatial items (Level 5 got one dice item only; Level 6 none), packing, grid-rule and circle-colouring puzzles, Level 4 rate per minute, balance chains, rope items, and Level 6 clock-hand similar triangles. Also not built: Level 5 average, Level 4 shaded-area fraction comparison (low rank), Level 6 data and Venn items.
4. Report proposals that became bank variants or lesson-level notes rather than separate slides: Level 4 mixed-number pairing and a second weekday question (the variants), Level 6 two-pack "largest impossible total" at L5 (done once at L5.6 and once at L6.10, the second is the Level 6 version).
5. Print additions (Go further print swaps proposed in the report) are all left for the next holiday cycle (v2), as decided.
6. Stopwatch timing of the tutor reading these slides was not done; they are optional and take no budgeted minutes.
7. Pre-existing problem found, not changed: regenerating `split/p5l10` with `rebuild/gen_p5l10.py` produces a different Think harder slide and an extra `p5l10-stretch2` slide compared with the committed deck (the committed deck and the generator are out of step). Do not regenerate Level 5 Lesson 10 without checking that. `tutor/data/p5l4.notes.json` was also stale by one character; it was left as committed.

## 7. Decks to republish (the coordinator republishes later; nothing was published here)

Level 4: p4l1, p4l2, p4l3, p4l6, p4l9, p4l10.
Level 5: p5l1, p5l2, p5l3, p5l5, p5l6, p5l7, p5l8, p5l9, p5l10.
Level 6: p6l1, p6l2, p6l4, p6l5, p6l7, p6l8, p6l9, p6l10.
