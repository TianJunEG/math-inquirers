# Audit round 5 of the daily teasers (after fix round 4)

Independent, read-only audit of `website/teasers/` on branch `claude/great-fermi-1hv4vc` (teaser files identical to commit 2901716; `git diff 2901716 HEAD -- website` is empty), 24 Oct 2026.
Nothing in the repo was edited except this file. Every build, verifier run, screen and browser run used copies under `/dev/shm`. `website/dist` was never touched.
Method: my own code for the near-copy screens, the year model and the browser checks (scripts in `/dev/shm/aud`, not committed); the builder's verifier and tests were only re-run, never trusted.

## Verdict

**NO-GO to release the current Nov and Dec bank. CONDITIONAL GO to start writing January, level by level, once the conditions in section 8 are met (C1 first).**

Why, in four lines:
1. The four round-4 High items and `L4-fanten` are gone, and nothing of that kind came back. Structure, rotation, reproducibility, flag-off and the browser are all clean (my own code agrees with the builder).
2. My own screen found **3 new High near-copies of our own books** (identical question or identical numbers, with the answer printed in our material) that the widened verifier did not report and that are not in `REVIEW_TRIAGE.md`: `L6-dice8`, `L4-clockfive`, `L5-tank`. All three are unchanged since round 3, so round 4 did not look at them.
3. All **124 puzzles I hand-solved agree with the bank and have one answer** (every one of the 106 puzzles replaced or rewritten in round 4 is in the sample). Two wordings are ambiguous (`L2-recyclegrid`, `L6-tintpaint`). Explanations are correct and kind.
4. Same-puzzle-at-several-levels is the main thing a family would notice: 23 clusters, 74 of 366 puzzles, tell the same story or use the same sentence frame at 2 to 4 levels with new numbers. The literal owner ruling (same numbers and same answer) is met; the intent (a different story) is not, for about 15 of the clusters.

## Summary table

| # | Task | Result |
|---|---|---|
| 1 | Own near-copy screen, 6,707 files (624 PDFs by `pdftotext`), 962,000 sentences, 5 rules | R4 High items and `L4-fanten`: gone. **3 new High**, 11 Medium frame copies (section 1) |
| 2 | Hand-solve 124 puzzles (18 to 23 per level; all 106 changed in round 4 plus 18 unchanged) | **124 of 124 agree**, one answer each; 2 ambiguous wordings, 2 Low leaks (section 2) |
| 3 | Same-level and cross-level duplication | no same-level pair is "the same puzzle"; 5 close pairs; cross-level: 0 FAIL by the literal rule, 23 clusters by story (section 3) |
| 4 | Level fit vs `docs/moe/syllabus_by_level.md` | all 11 round-3 level items fixed; 13 new Low/Medium fit notes (section 4) |
| 5 | `verify_bank.py` twice (`PYTHONHASHSEED` 1 and 12345, different `TMPDIR`), `--selftest`, source lock | byte-identical reports, 0 FAIL, selftest 0 problems; lock works but is loose (section 5) |
| 6 | Year model, own code, loss of 2 at every level | L1 and L2 survive any 2 (1,830 of 1,830 pairs) and random triples; L3 to L6 survive 2 in 30 of 30 draws (section 6) |
| 7 | Browser (scratch build, flag on) | builder's suite 482 checks, 0 failed; my own: all pass (section 7) |
| 8 | GO / NO-GO, per level, what a parent sees | section 8 |

## 1. Near-copy screen with my own code

Corpus (snapshot digest differs from the builder's only because other agents add files under `practice/`): every text-like file of `outputs docs practice school split rebuild hp p2..p6 term extension deck diag levels tutor portal ops k2 taster website (without teasers, dist, preview)`, including `docs/books/private_*`, `.docx`, and the text of every PDF. 6,707 files, 961,997 sentences.
Rules (my code, windows of 1 to 3 sentences in one file): **A** IDF-weighted content-word overlap of 0.45 or more with 3 or more shared words; **B** 67% of the question's numbers in the window plus 3 shared words; **C** 3 or more masked four-grams; **N** all numbers and the answer in the window; **G** shared word 3-grams that contain a number (catches "30 cm by 25 cm" and "2 m 45 cm"); **S** a single question sentence of 4 or more content words with Jaccard 0.6 or more against one source sentence.
Calibration: replaying the five round-4 High wordings (`selftest_probes.json`, `round4_high`) as if they were puzzles, rules A to C flag all five with score 1.2 or more. So the screen can see that kind of copy.

**Round-4 High items: confirmed gone.** `L1-fanlines`, `L3-grid33`, `L3-flagstrip`, `L3-fourtiles`, `L4-fanten` are not in the bank, and no question in the bank mentions a fan of lines, squares or rectangles in a grid, "red, red, blue, green" or squares joined edge to edge. The replacements are original in the screen (`L1-tilewall`, `L3-albumpages`, `L3-moneybox`, `L3-raffledays`, `L4-tokenstall` show no window match).

### High (3): identical question or identical numbers to our own books; the verifier gave no FAIL and the triage file does not mention them

| Puzzle | Source in our own material | Why it is a copy |
|---|---|---|
| `L6-dice8` (1 Nov) "Two fair dice are rolled ... probability of a total of 8, as a fraction in its simplest form" | `practice/holiday/p6/06/lesson.py`, Exit slip (a): "Roll two dice and add. What is the probability that the total is 8? Write the fraction in its simplest form." answer 5/36; its steps list the five pairs | same frame, same total, same answer, same simplest-form instruction |
| `L4-clockfive` (29 Nov) "At 5 o'clock, what is the smaller angle between a clock's hour hand and its minute hand?" | `outputs/designed/Math_Inquirers_P5_Question_Bank.pdf` and `p5/content/l8.js`: "What is the smaller angle between the hands of a clock at 5 o'clock? At 8 o'clock?" answer "150° at 5 o'clock (5 × 30°)" | same question, same time, answer printed in our book |
| `L5-tank` (29 Nov) "Jun Hao pours 6 litres ... base of the tank measures 30 cm by 25 cm. What is the depth of the water?" (8 cm) | `split/p5l5/project/slides/p5l5-exit.html`, `outputs/schemes/Math_Inquirers_P5_Scheme_of_Work.pdf`, `practice/holiday/p5/05`: "A tank has a base 30 cm by 25 cm and water 8 cm deep ... (b) How many litres of water are in the tank?" (6 L) | the same tank, the same base, the same 6 L and 8 cm, asked the other way round |

Why the verifier missed them: `L6-dice8` and `L4-clockfive` are one-sentence questions with few content words, so the window rules (A, A2) have too little to match; `L5-tank` has all its numbers in the source but not 1000, and the answer is in a neighbouring sentence, so rule N (all numbers) does not fire. My rule S and rule G catch all three.

### Medium (11): the same frame as our books with other numbers (answer not printed), or a stated fact that is the answer

- `L4-chairs24`: "Mr Tan puts 24 chairs in equal rows" against "Mr Tan puts 20 chairs in equal rows. There must be at least 2 rows ..." (`practice/holiday/p2/03/lesson.py`, `outputs/print/Math_Inquirers_P2_Workbook_PRINT.pdf`). Same name, same sentence, one number changed.
- `L3-tilearrays`: "She puts all of them in equal rows ... 2 rows of 24 and 24 rows of 2 are different ways" against `extension/data/l3_u03.json` / L3 Extension Workbook "Mei puts 30 tiles in equal rows ... 2 rows of 15 and 15 rows of 2 are different ways" and `split/p4l1` ("2 rows of 20 and 20 rows of 2 are different ways"). `L3-tilearrays` and `L4-chairs24` are also the same puzzle at two levels (divisors of 48 and of 24).
- `L4-theatrerows`: "A hall has N rows. Row 1 has 15 seats ... each next row has 3 more" against the L3 Extension Workbook "A hall has 8 rows. Row 1 has 7 seats. Each row has 2 more seats ... (b) The hall has ___ seats in all."
- `L3-cardcorners` (a corner square cut from a card, perimeter left) against `school/p4/out/P4_S2_Puzzles.pdf` "A card is 23 cm by 9 cm. A corner piece, a square of side 5 cm, is cut off. Find the perimeter of the card left." (and `L5-cutcard` is the same trick).
- `L3-keyringtray` ("a tray holds 12 pink, 10 orange and 8 purple keyrings ... at least one of every colour", 23) against `docs/sasmo/g2_original_problems_draft.md` 5.3 "A jar has 9 mint, 6 lemon and 5 cherry sweets ... at least one of each of the 3 flavours" (same frame; `L5-colourdraw` is the next item of that draft).
- `L1-shapeclue` ("2 straight sides and 1 curved edge", quarter circle) against `split/p2l8/.../p2l8-teach1.html` and `rebuild/gen_p2l8.py`: "A quarter circle has 2 straight sides and 1 curved side."
- `L2-solidclue` ("2 flat faces and 1 curved face", cylinder) against the P2 Question Bank ("Which solid has 2 flat faces that are circles and 1 curved face?") and `extension/l2/author/u08.py`.
- `L6-waterbarrel` (80 by 50 by 45 cm, litres) against `p5/content/l6.js` / P5 Question Bank "tank 60 cm long, 50 cm wide and 45 cm high ... 135 L" (two of three sides identical).
- `L2-tworopes` ("One rope is 2 m 45 cm long ...") against the P3 Question Bank and `docs/audit/gifted_fixes_p3.md` "A ribbon is 2 m 45 cm long. 2 m 45 cm = ____ cm" (same length, same conversion).
- `L3-twentyfour` ("starts at 8:35 pm and lasts 1 hour 50 minutes") against the Level 3 Placement Check (`outputs/diagnostics/Math_Inquirers_Level3_Placement_Check.pdf`, `diag/content/p3.json`): "A film starts at 2:45 p.m. and lasts 1 hour 50 minutes." A child who took the diagnostic meets the same duration.
- `L4-tilefigures` ("Figure 1 uses 5 tiles, Figure 2 uses 9 ...") against `docs/books/p6_non_routine_catalogue.md` EX-PAT-2 "Figure 1 uses 5 sticks, Figure 2 uses 8, Figure 3 uses 11".

Low (frame only, generic): `L2-deliveryrobot` (routes right and down, `term/l1/lessons/l33.json`), `L5-savingsinterest` ("The bank pays 5% interest ..." in the P5 booklet), `L5-town`, `L3-floortiles2` (P3 booklet "Mei's garden is a rectangle 12 m long and 7 m wide"), `L6-merlion` (letter shift), `L1-purse`, `L1-bigtwo`.

Other REVIEW lines: the triage file has 197 "accepted" rows, but they collapse to 56 template reasons (81 "number only in the wording", 53 "planning or exam-catalogue note"); it is a pattern classification, not per-line evidence. It would not have found the three High items (none is a REVIEW line). Low.

## 2. Hand-solved sample (124 puzzles, from the question text only)

Method: question text and figure text only; bank answer opened after my own answer. 18 L1, 19 L2, 22 L3, 21 L4, 21 L5, 23 L6 = 124. This is every puzzle that is new or rewritten in round 4 (63 + 43 = 106, i.e. far more than the 40 asked) plus 18 unchanged ones (3 per level, random).

- **124 of 124 agree with the bank; each has exactly one answer.** Differences were format only (`5 1/2` against `11/2`, `11.50` against `11.5`, the number words `nineteen` against `19`), and the page accepts the variants (section 7).
- Explanations and hints: all arithmetic right; no hint gives the answer away except as noted; tone calm ("Not yet"). The explanations of `L6-savingsbox` (signed changes) and `L1-counterbox`, `L1-hiddensum` (derive before stating) are fixed.
- **Medium, ambiguous wording:** `L2-recyclegrid` says "The weeks gave 30, 50 and 50 kg in all." If the three totals are not read in week order, the answer is 33 or 13 (orders 30-50-50, 50-30-50 and 50-50-30 all fit every other number). Say "In week 1 both classes together recycled 30 kg, in week 2 50 kg and in week 3 50 kg." `L6-tintpaint`: "Tin A holds 4 times as much paint as Tin B, and 45 mL more" can be read as A = 4B + 45 (no answer). Only the reading "and 45 mL more than Tin B" gives 60. Say "Tin A holds 4 times as much paint as Tin B. Tin A holds 45 mL more than Tin B."
- Low: `L1-fourodds` shows the example "1 + 3 + 5 + 11" whose total, 20, is even, which already answers the question; `L1-marblegame` hint ("leave a number in the 5 times table") nearly gives 4; `L1-tapefold` assumes the snip is not on a crease (fine, say "not at a fold"); ids that no longer match the text: `L4-notebooks` (rulers), `L5-ballholder` (paint).
- Items I checked for a second solution and found none: `L2-canoetrips` 13, `L5-riverboat` 13, `L2-lanternring` 5, `L5-circleout` 4, `L4-tokenstall` 34, `L4-bikelock` 6763 (d=3 only), `L6-keyclaims` Nurul, `L4-fourclaims` Siti, `L4-heightline` 13, `L6-shelfbooks` 9, `L5-digitsum36` 156789.

## 3. Duplication under the owner ruling

**Within each level (all 1,830 pairs per level, parent view).** No pair is "the same puzzle". Close pairs a parent could notice: `L2-tilebed` + `L2-hallfloor` (a rectangle of tiles or stones in rows, 7 Nov and 10 Dec); `L6-waterbarrel` + `L6-tankdepth` (cuboid tank, litres and 1000 cm³, 17 Nov and 28 Dec); `L6-testmean` + `L6-quizmean` + `L6-twoclasses` (marks and mean); `L1-oddnumber` + `L1-fivetable` and `L4-oddtable` + `L4-sevens` (times-table membership). Each level has 61 distinct sub-structures, no `same_idea_groups` group twice, no family more than 3 in 61 days, no family on consecutive days, no repeated answer of 10 or more, no single-digit answer over its cap (my own check of the bank).

**Across levels, the literal ruling (same answer and shared numbers; same set of numbers).** Zero violations by the rule as the builder states it (numbers 0, 1, 2 excluded). By the strict reading with 2 counted, one pair: `L1-cardstrip` and `L2-ticketnotes` (answer 28, numbers 2 and 30; different stories, a coincidence; Low). The same answer 13 appears in `L2-canoetrips` and `L5-riverboat` (a boat crossing, different numbers) and the same set `{3, 4, 8}` in `L2-cakeshare` and `L5-cafemenu` (Low).

**Across levels, story skeleton (the intent: a different story at each level).** 23 clusters, 74 puzzles (L1 12, L2 14, L3 12, L4 13, L5 16, L6 7). The verifier's skeleton rule does not see them because it needs 4 shared "story words" and these clusters differ in the nouns.

| Cluster | Puzzles | What repeats |
|---|---|---|
| nth weekday of a month | `L1-libraryday`, `L2-fourthsunday`, `L3-secondthursday`, `L5-fourthwednesday` | L2, L3, L5 are the same sentence: "In one month, the Nth is a Thursday. What is the date of the Kth Sunday?" |
| value of a digit | `L2-digitvalue2`, `L3-digitvalue6482`, `L4-digitvalue83517`, `L5-sevendigit` | "In the number N, how much more is the value of the digit X than the value of the digit Y?" at three levels |
| solids counted together | `L2-edgecount`, `L3-solidedges`, `L4-vertices`, `L5-prismpyramid` | L4 and L5 share the sentence "A triangular prism has two triangle ends and three rectangle sides." |
| facing and turning | `L1-westturns`, `L3-turnsfour`, `L4-robotturns`, `L5-robotfive` | person, robot, drone: the same puzzle |
| two overlapping groups | `L3-clubs`, `L4-schoolclubs`, `L5-schooltwo`, `L6-codingclub` | "In a school of N, a have X, b have Y, c have neither: both?" four times |
| who did it, statements | `L3-keyholder`, `L4-fourclaims`, `L5-ballholder`, `L6-keyclaims` | children say one thing each, "exactly k are true" |
| times-table count | `L1-fivetable`, `L3-eights`, `L4-sevens`, `L5-twelves` | one sentence frame |
| fold once and cut | `L1-tapefold`, `L2-foldcut`, `L5-scrollfold` | tape, strip, ribbon: the same story |
| take-away game | `L1-marblegame`, `L2-stickgame`, `L4-reachtotal` | sweets, sticks, a running total |
| knockout | `L1-marblecontest`, `L3-badmintonko` | one rule text, 44 against 36 |
| circle elimination | `L2-lanternring`, `L5-circleout` | 10 in a ring, every 2nd and every 3rd |
| rows that grow, summed | `L2-tinstack`, `L4-theatrerows`, `L5-stairs60`, `L6-gaussjar` | "A shop stacks tins / cans in rows" at L2 and L6 |
| boat crossings | `L2-canoetrips`, `L5-riverboat` | answer 13 at both |
| add the previous two | `L4-addpattern`, `L6-recurrence` | |
| cuboid tank and litres | `L5-tank`, `L6-tankdepth`, `L6-waterbarrel` | `L5-tank` and `L6-tankdepth` are the same pour-and-measure-depth puzzle |
| wait for the next bus or ferry | `L2-busstop`, `L4-ferry` | "every 25 / 35 minutes, the first at ..., arrives at ..." |
| border tiles, checkerboard | `L1-tilewall`, `L2-hallfloor`, `L2-tilebed`, `L5-floortiles5`, `L3-chessboard` | `L1-tilewall` and `L2-hallfloor` differ only in the numbers and the colours |
| corner cut from a rectangle | `L3-cardcorners`, `L5-cutcard`, `L5-cornerscard`, `L6-flagcloth` | |
| also | `L1-numpattern`/`L3-moneybox`, `L1-signsgap`/`L4-signcard`, digit cards (`L1-bigtwo` to `L5-cardsmax5`), digit clues (`L1-secret63`, `L2-secret643`, `L4-bikelock`), `L1-seatrow`/`L2-cinemarow` | |

The README says the rule is "a different story, different numbers and a different difficulty" for a sub-structure at several levels. About 15 of the 23 clusters break the first of the three. Recommendation to the owner: either accept the clusters as "same idea, different age" (and say so on the site), or require a different question as well as a different story (rule below, C3).

## 4. Level fit against the MOE syllabus files

Round-3 level items all fixed (checked): `order_ops.evaluate` only L5 and L6 (`L6-leftright` and `L5-bracketmult`), `sorting.overlap_both` from L3 on (no L1 or L2 use), pencil lift, diagonal squares and three sets retired, `strategy.fake_coin` L4 and L6 with the P3 cite and the "enrichment" mark, `rate.speed_distance` L6 only, `L1-campdays` in 7s, `L2-sevens` in 4s.
New or remaining notes (the 106 changed puzzles checked one by one; the rest by sub-structure):

| Severity | Item | Note |
|---|---|---|
| Medium | `L3-fruitsums` (three symbols, three equations) | simultaneous equations at Primary 3 (symbols are not in MOE before P6; the hint is good, the task is heavy) |
| Medium | `L4-flour` (3 2/3 + 1 5/6 as a mixed number) | adding mixed numbers is P5 (NA Fractions 2.1); P4 only has fractions to 12ths and mixed numbers as notation |
| Low | `L2-stripchain` (7 strips of 8 cm), `L2-hallfloor` (9 by 9 stones) | tables of 7, 8, 9 are P3 (P2 has 2, 3, 4, 5, 10) |
| Low | `L2-ladderrungs` (80 cm in 8 gaps), `L2-sevens` (98 divided by 4) | division by 8 and division with a remainder are P3 |
| Low | `L1-tilewall` (5 by 9 = 45), `L1-counterbox` (44 halved), `L1-circlekids` (60 halved), `L1-whichsun` (24 halved) | P1 multiplies within 40 and divides within 20 |
| Low | `L1-fourodds` (odd and even rule) | odd and even numbers are P2 (Whole Numbers 1.6) |
| Low | `L1-campdays`, `L1-libraryday`, `L3-funrun`, `L3-tripbooking` (weeks, dates) | weeks and the calendar are not a printed outcome; fine as general knowledge |
| Low | `L3-bakery` (14 boxes of 15) | two-digit by two-digit multiplication is P4 (P3 is up to three digits by one digit) |
| Low | `L3-barpieces` (3/8 = ?/32) | P3 equivalent fractions have denominators up to 12 |
| Low | `L5-pumpjob` (9 pumps, 12 hours: 6 pumps) | work and time is not the MOE "rate" outcome (a total from rate and units fits, but this is inverse proportion) |
| Low | `L6-hiddenpair` (divisible by 6 using the digit sum) | the divisibility test for 3 is not an MOE outcome; fine with the hint |
| Low | `L6-councilpick`, `L5-lilypads`, `L5-climbing` (arrangements, paths, combinations) | counting methods are not in the syllabus at any level; enrichment, make-a-list works |
| Low | `L4-heightline`, `L6-shelfbooks` (13 and 9 adjacent swaps) | the inversion count is long for ages 9 to 12; the hints are good |

## 5. `verify_bank.py` reproducibility and the source lock

- Full-tree copy (6,679 files, 1,357.9 MB, digest `2e75b63d34f1e200`), run twice: `PYTHONHASHSEED=1` / `TMPDIR` A and `PYTHONHASHSEED=12345` / `TMPDIR` B (so the PDF text cache was rebuilt independently). Both: month 11 **0 FAIL, 95 REVIEW**; month 12 **0 FAIL, 85 REVIEW**; structure rules 0 FAIL; capacity 0 FAIL; exit 0. `VERIFY_REPORT.md` (both months) and `STRUCTURE_REPORT.md` are **byte-identical** across the two runs (cmp). They equal the committed reports except for the source-digest line (other agents added files to `practice/`). Each run takes about two minutes.
- `--selftest`: 72 cases, 0 problems, 88 kinds checked.
- Source lock: removing 160 files from `term` (6%) gives exit 2 "INVALID VERIFICATION ... source root term has 2370 files, the lock needs at least 2403": it works. **Loose where it matters:** the lock needs 95% of the current counts, so `practice` may lose 81 files (lock 223, actual 304), `outputs` 15, `split` 91, `school` 24. I deleted 63 `practice` files including `practice/holiday/p6/06/lesson.py` (the file behind `L6-dice8`) and the lock still passed (the run proceeded). The must-exist list does not contain `practice/holiday/p6/06`, `split/p5l5` or the Question Bank PDFs. Make the minimums 99% and list the three source files behind section 1 as required (C2).

## 6. Year model, my own code (independent of `year_model.py`, `taxonomy.py`, `verify_bank.py`)

Usable units per level (retired removed, `same_idea_groups` counted once, the fixed-page sub-structure excluded): **L1 71, L2 89, L3 110, L4 110, L5 106, L6 106** (README says 111, 111, 107, 107 for L3 to L6: stale by one; `STRUCTURE_REPORT.md` is right).

- **L1 and L2** (rotation of the 61 released days, simulated for 12 consecutive real years including 29 Feb 2028, 2032, 2036): 0 violations (every gap 60 days or more; family at most 3 in 60 days; no family on consecutive days). Spares: L1 10, L2 28. Loss of any one sub-structure can be re-filled (L1 at least 7 spares fit, L2 at least 21). **Loss of any 2 of the 61 used: 0 failures in 1,830 of 1,830 pairs at both levels; 150 of 150 random triples at both levels.** The L1 spare pool of 10 is the thinnest margin in the project (structure only; each refill still needs six new stories).
- **L3 to L6** (integer program, HiGHS: one unit a day on 366 dates; once per calendar quarter; 30-day gap across quarter boundaries, circular; family at most 3 a quarter and never on consecutive days; Nov and Dec fixed to the bank): feasible at all four levels. **Loss of 2 unreleased units: 30 of 30 random draws feasible at each level; loss of 2 released units (puzzle must be rewritten as well): 6 of 6 at each level.** Larger losses (4 draws each): lose 6: 4 of 4 at every level; lose 10: L3 4 of 4, L4 4 of 4, L5 0 of 4, L6 2 of 4; lose 14: L3 0, L4 1, L5 0, L6 0 of 4. Worst case for 2 lost (both from one of the 5 widest unreleased families): L5 15 of 15 and L6 15 of 15 feasible. A random loss of 10 is proven infeasible at L5 (HiGHS status 8) and feasible in one more L6 draw. Family cap 2 is infeasible at every level (so the cap of 3 is binding). Margins in order: L3 and L4 comfortable, L6 thin, L5 thinnest (consistent with the builder's N-2).
- Not modelled by anyone: the year of text answers (section 8).

## 7. Browser spot check (scratch build with `MI_TEASERS=1` under `/dev/shm`; Chromium via Playwright)

- `test_flag_off.py` on the real tree: **15 checks, 0 failed**; `git status website` empty; `website/dist` untouched; committed `mi_signup.html` and `level_pages/*.html` carry no teaser while `site_enabled` is false.
- Builder's `test_site.py` on my scratch build: **482 checks, 0 failed.**
- My own script, for all six level pages:
  - **Rollover from 3 time zones** (Pacific/Kiritimati, America/Los_Angeles, Asia/Kolkata) at 9 instants around Singapore midnight (30 Nov to 1 Dec, 14 to 15 Dec, 31 Dec to 1 Jan, 31 Oct to 1 Nov, 15:59:50Z and 16:00:05Z): **162 of 162 show exactly the Singapore-date puzzle** from my own copy of the bank; at 1 Jan and 31 Oct (no released puzzle) the fixed puzzle, no date label, no request for a month file.
  - **Fallback:** 15 Jan 2027, 24 Oct 2026, 29 Feb 2028, 30 Jun 2027: 24 of 24 show the fixed puzzle (answer button visible), no `/teasers/` request.
  - **No JavaScript:** 6 of 6 pages show the fixed puzzle in `#pzBox`, visible.
  - **All 366 puzzles at 390 px** (light; 55 more in dark): right puzzle for the date, no sideways scroll (scrollWidth 390), the puzzle box inside the viewport, **smallest text 14 px or more** at load, after a wrong answer with the hint, and after a correct answer (366 of 366 each). Three figures scroll inside their box by design.
  - **Answer formats**, typed into the real input, for all 366: the shown answer, the raw answer, **"It is X"**, **"The answer is X"**, and "It's X": all accepted (366 of 366 for each). Spot variants: `$11.5`, `11.5`, `$11.50.`, `5 1/2`, `11/2`, `5.5`, `1/8` and `0.125`, `25 th`, `34 prizes`, `Odd.`, `farid`, `a quarter circle`, `quarter-circle` accepted; `10/44` gets the kind "write it in simplest form".
  - Low: `nineteen` for `L4-numbercards20` gets "Try writing your answer with digits"; `the 25th`, `13 December`, `5½` and `Farid plays cricket` are not accepted (a child may type them). The page takes `19`.
- Not re-tested by me: the page left open across midnight (the builder's suite covers it).

## 8. GO / NO-GO for writing January (2 batches of about 30 per level, each audited before release)

**Release of the current bank: NO-GO** (3 High). **January: CONDITIONAL GO**, per level:

| Level | Decision | Conditions before January is released | A parent would notice over a year |
|---|---|---|---|
| 1 | **GO** to write now | C2, C3, C5; six-return packs for the thin sub-structures first; the 10 spares are the only margin | Every idea comes back 6 times a year (every 61 days) with a new story: the child's "count the gaps / lists / pairs" puzzles. Some sit above P1 (odd and even, halving, 5 by 9). Text answers are names and "even/white/south": 7 in two months, so about 40 a year |
| 2 | **GO** | C2, C3, C5; fix `L2-recyclegrid`; `L2-solidclue`, `L2-tworopes` to replace | As L1, plus tiles/floors (`L2-tilebed`, `L2-hallfloor`) twice a quarter, a bus and a ferry wait at L2 and L4; about 15% of puzzles need the P3 tables or division |
| 3 | **GO after C1** | replace `L3-tilearrays`, `L3-cardcorners`, `L3-keyringtray`, `L3-twentyfour`; `L3-fruitsums` is heavy | Same sentence as the Level 2 and Level 5 pages (weekday dates, digit value, overlapping clubs, who-did-it); three perimeter/area puzzles a quarter |
| 4 | **GO after C1** | replace `L4-clockfive` (High), `L4-chairs24`, `L4-theatrerows`; fix `L4-flour` | Siblings at 4 and 5 see the same prism sentence, digit-value sentence and turning puzzle; the "numbers 1 to 20 in words" and take-away game feel like Level 1 and 2 ideas with larger numbers |
| 5 | **GO after C1** | replace `L5-tank` (High); thinnest year margin (losing 10 units breaks the year, 6 is fine): add 4 or more sub-structures with solver, checker and cite before April | Cuboid tank, notched card, border tiles each appear again at Level 6; "who-did-it" for the third time in the family |
| 6 | **GO after C1** | replace `L6-dice8` (High); rewrite `L6-tintpaint`; `L6-waterbarrel` against `L5`'s tank; margin thin (losing 10 breaks half the draws) | Probability three times a quarter (`L6-dice8`, `L6-threecoins`, `L6-twored`) and four "marks and mean" puzzles; the enrichment items (`L6-pearltray`, `L6-councilpick`) are the hardest in the year |

| # | Condition (exact) | Closes |
|---|---|---|
| C1 | Replace `L6-dice8`, `L4-clockfive`, `L5-tank` with new frames and the 11 Medium frame copies of section 1 (`L4-chairs24`, `L3-tilearrays`, `L4-theatrerows`, `L3-cardcorners`, `L3-keyringtray`, `L1-shapeclue`, `L2-solidclue`, `L6-waterbarrel`, `L2-tworopes`, `L3-twentyfour`, `L4-tilefigures`). Retire the frames in `taxonomy.json` (`retired_frames`): a dice-total probability; angle between clock hands at a whole hour; a tank of given base with litres; chairs or tiles in equal rows; rows of seats that grow; a card with a corner cut off; the colour-pigeonhole draw. Re-run the screen. | High, Medium |
| C2 | Verifier: add (a) a one-sentence rule S (a question sentence of 4 or more content words that matches one source sentence by 0.6 or more is a FAIL unless the same sentence is in `stock_phrases.txt`); (b) a number-with-unit 3-gram rule G (3 or more shared such grams in a window is a REVIEW, 5 a FAIL); (c) the answer-and-two-numbers-in-a-3-sentence-window rule with the answer counted; replay `L6-dice8`, `L4-clockfive`, `L5-tank`, `L4-chairs24` in `selftest_probes.json`; raise every lock minimum to 99% of the current count and add `practice/holiday/p6/06`, `split/p5l5` and `outputs/designed` to `must_exist`. Say in the triage that the reasons are template classes. | Medium (tooling) |
| C3 | Owner decision on the 23 clusters of section 3 (the intent of "a different story at each level"). Suggested rule, checkable: the same sub-structure at two levels needs a different question or figure, not only a different noun; no more than 2 levels may share a sentence frame; the same sentence (weekday date, digit value, prism sentence, overlapping sets) at 3 or 4 levels is a FAIL. Apply to Nov and Dec and to the January plan. | Medium |
| C4 | Fix the level notes of section 4 that matter: `L3-fruitsums`, `L4-flour`, `L3-bakery`, `L2-stripchain`, `L1-fourodds`; update `taxonomy.json` levels and README counts (111/111/107/107 should be 110/110/106/106; round 4 "61 replaced, 262 unchanged" should be 63 and 260). | Medium, Low |
| C5 | Wording: `L2-recyclegrid`, `L6-tintpaint`, `L1-fourodds` example; a second reader for every January explanation; hand-solve at least 15 puzzles a level before release, new items first (as in section 2). | Medium |
| C6 | Text answers (M-7): plan 40 or more distinct text answers per level for the year (names, directions, shapes) or reduce text answers; at present 4 to 7 per level in 61 days. | Medium |
| C7 | Before any release: the verifier on the full tree twice with different `PYTHONHASHSEED`, `--selftest`, `year_model.py`, `test_flag_off.py`, `test_site.py`, and an independent screen with rules A, B, C, N, G and S on the January batch. Keep L1 and L2 on `YEAR_PLAN.md`; keep spares in reserve (L1 10, L5 and L6 thin). | Medium |

## Severity list

- **High (3):** `L6-dice8`, `L4-clockfive`, `L5-tank` (identical question or numbers with our own books; not reported by the verifier; not on the triage list).
- **Medium (about 25):** 11 frame copies of our books; 23 cross-level clusters (74 puzzles) that tell the same story; `L2-recyclegrid` and `L6-tintpaint` wording; `L3-fruitsums` and `L4-flour` above level; verifier blind spots (one-sentence questions, units, lock slack); text-answer plan; thin year margin at L5, L6 and the L1 spare pool.
- **Low:** 11 small level-fit notes; explanations that nearly give the answer (`L1-fourodds`, `L1-marblegame`); ids that no longer match the text (`L4-notebooks`, `L5-ballholder`); stale README counts; answer formats a child may type (`nineteen`, `the 25th`, `13 December`); the triage reasons are templates; the literal 2-number coincidence `L1-cardstrip`/`L2-ticketnotes`.
