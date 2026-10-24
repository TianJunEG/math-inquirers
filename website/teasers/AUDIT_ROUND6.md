# Audit round 6 of the daily teasers (after fix round 5)

Independent, read-only audit of `website/teasers/` on branch `claude/great-fermi-1hv4vc` (HEAD a358092), 24 Oct 2026. Nothing in the repo was edited except this file. Every corpus build, verifier run, year model, site build and browser run used copies under `/dev/shm/a6` (full-tree copy for the verifier, a scratch copy of `website/` for the flag-on build). `website/dist` was never touched; the real `website/` stayed clean (`git status website` empty).
Method: my own code for the near-copy screens, the hand-solving, the cross-level frame scan, the year model and the browser checks (scripts in `/dev/shm/a6`, not committed). The builder's verifier, `--selftest`, `test_flag_off.py`, `test_check.js` and `test_site.py` were only re-run, never trusted.

## Verdict

**Release of the Nov and Dec bank: NO-GO (one High, see H1). January: CONDITIONAL GO, level by level, once the conditions in section 9 hold (G1 to G6 for every level, plus the level rows).**

The round-5 fixes did what they said for the things the last audit named; what is wrong now is of a different kind (no copies of our books, no wrong answers):

1. **The 3 High and the 11 Medium of round 5 are gone**, and my screen (all 14 old wordings are flagged when replayed as puzzles) finds no new High or Medium copy of our own books or PDFs among the 366 puzzles. Only Low residue (section 1).
2. **103 puzzles hand-solved, 103 agree with the bank, one answer each** (all 82 puzzles that changed in round 5 plus 21 unchanged; 17 to 18 per level). The two ambiguous wordings of round 5 are fixed (`L6-tintpaint`) or acceptable (`L2-recyclegrid`, Low).
3. **H1 (new, High): the owner ruling "the same story or sentence frame at ONE level only" is not met, and the claim in `FIXES_ROUND5.md` that it is met is wrong.** Besides the 23 audited clusters, a scan of all 104 sub-structures that sit at two or more levels finds **22 groups where a parent would see the same puzzle again** (same sentence frame, nouns and numbers changed), **19 of the 22 contain a puzzle written or rewritten in round 5, and in 8 groups both members are round-5 work** (for example `L3-marketstall` and `L4-shuttlehours`: same frame, same answer 15). The verifier reports 0 FAIL because it needs 6 shared masked four-word runs and ignores runs found in 8 or more questions; a function-word skeleton rule would see 25 of the 28 pairs I checked.
4. **H2 (new, High for planning): the year is not feasible as ruled at Levels 3 to 6 because of the answer rule** (an answer of 10 or more once per level and year). In Nov and Dec 51 to 62% of the answers are whole numbers below 100; the 305 puzzles still to write may have only 29 to 31% (89 to 95 values are left). The verifier tracks single digits only.
5. Reproducibility, flag-off, rollover, fallback, no-JS, answer formats and layout are all clean. Reproducibility: two full-tree runs (`PYTHONHASHSEED` 1 and 12345, separate `TMPDIR`) give byte-identical reports. Year model: feasible at all six levels; **Level 5 tolerates only 2 more retired sub-structures** (3 is proven infeasible) and nothing was added there in round 5 although the last audit asked for it.

## Summary table

| # | Task | Result |
|---|---|---|
| 1 | Own near-copy screen, 6,752 files (PDFs by `pdftotext`), 972,784 sentences, rules A, B, C, N, G, S | 3 High and 11 Medium of round 5: gone. **No new High or Medium copy of our books.** 9 Low matches (section 1) |
| 2 | Hand-solve a new stratified sample | **103 of 103 agree**, 17 or 18 per level, all 82 changed puzzles included (section 2) |
| 3 | The 23 clusters; other frames at two or more levels | 15 of the 23 closed, 8 only partly; **22 further groups with the same frame at 2 to 6 levels** (section 3, **H1**) |
| 4 | Nine pairs at exactly 5 shared runs | **6 of 9 are the same puzzle to a parent**, 3 are the stock "X is taller than Y" frame (section 4) |
| 5 | Level fit against `docs/moe/syllabus_by_level.md` | `L3-beadnecklaces` and `L4-longestwalk` fit; 8 puzzles above their level, 10 well below (section 5) |
| 6 | Verifier twice, source lock | byte-identical; `--selftest` 112 pass; **the lock checks counts only**: it accepted a tree with 27% of the bytes gone (section 6) |
| 7 | Year model, loss of 2 at every level | feasible; exact tolerance L1 8, L2 21, L3 6, L4 5, **L5 2**, L6 7 critical losses; **H2** answer budget (section 7) |
| 8 | Browser, scratch build | all pass: 216 rollover, 24 fallback, 6 no-JS, 6,324 matcher checks, 366 puzzles at 390 px (section 8) |
| 9 | GO / NO-GO and the text-answer shortfall | section 9 |

## 1. Near-copy screen with my own code

Corpus: every text-like file and every PDF under the repository except `website/teasers`, `website/preview`, `dist`, fonts and mascot: 6,752 files, 972,784 sentences (a fresh build; 45 files more than at round 5). Rules, in windows of 1 to 3 sentences in one file: **A** idf-weighted content-word overlap of 0.45 or more with 3 or more shared words; **B** 67% of the numbers plus 3 shared words; **C** 3 or more masked four-grams; **N** all numbers and the answer in the window; **G** shared word 3-grams that contain a number; **S** one question sentence of 4 or more content words with Jaccard 0.6 or more against one source sentence.
Calibration: replaying the 14 round-4 wordings of `L6-dice8`, `L4-clockfive`, `L5-tank` and the 11 Medium as if they were puzzles, the screen flags 13 of 14 by A, B, C, N or S and `L2-tworopes` by rule G ("2 m 45 cm", 4 shared grams), so all 14. So the screen can see that kind of copy.

**Confirmed gone.** None of the 14 ids is in the bank, and no question mentions two dice, clock hands, a tank, equal rows, "Row 1 has", a corner cut off a card with a perimeter question, or the colour-pigeonhole draw. The 63 new ids and 19 rewrites (82 puzzles) show no window match above incidental level.

**New matches (all Low; none needs a replacement):**

| Puzzle | Source in our own material | Note |
|---|---|---|
| `L2-riceleft` | P3 Question Bank, start-here items S2 "A bag of rice weighs 3060 g." and S3 "4 ℓ 500 ml - 1 ℓ 750 ml ... Hint: write both in ml first" | same noun phrase, the same 750, the same method, and P3 content at Level 2; looks assembled from two starters. Low to Medium |
| `L2-gardenfence` | `school/p3/gen/pages_s2c.py` "{name}'s garden is a rectangle {a} m long and {b} m wide" | first sentence only; the book asks the area, this asks the fence. Low (as `L3-floortiles2`, carried) |
| `L2-ticketnotes` | Extension L2 workbook "pay exactly $7 using $1 coins, $2 notes and $5 notes" | same notes, other question. Low |
| `L1-biscuithalves`, `L2-toyboxshape`, `L3-cuboidclue` | P2 Question Bank, `split/p2l8` "Cube, cuboid, cylinder or cone?" | the genre "clue about faces, name the solid" with the same option list; clues differ. Low |
| `L4-brushoffer` | `docs/audit/gifted_fixes_p5.md` "shop Y 4 for $3.00 plus 1 free" | note about a replaced item. Low |
| `L6-helmetsale` | `practice/holiday/p5/07` "A $100 bag is on sale. Shop 1 takes 20% off" | other ask. Low |
| `L6-merlion`, `L5-savingsinterest`, `L5-town` | P6 Question Bank, P5 booklets | carried from round 5, unchanged. Low |

Rules S, N and G on the 82 changed puzzles give nothing else. The verifier's 114 + 100 REVIEW lines were not re-triaged; the 9 structure REVIEW lines are judged in section 4.

## 2. Hand-solved sample (103 puzzles, from the question text only)

Method: question and code text only, bank answer opened after my own answer. Seeded random draw (seed 66): every one of the **82 puzzles that changed in round 5** (63 new ids, 19 reworded) plus unchanged ones to reach at least 17 per level: **L1 17, L2 18, L3 17, L4 17, L5 17, L6 17 = 103** (82 changed, 21 unchanged), including `L2-recyclegrid` and `L6-tintpaint`.

- **103 of 103 agree with the bank, each with exactly one answer.** (One slip of my own: first pass `L1-wordcards`, I miscounted the place in the alphabetical list; re-derived: eight, five, four, nine, **one** is 5th, the bank is right.) Differences in format only.
- Checked for a second solution and found none: `L4-dronefly` 27 (the 57 m is first reached after an up move), `L5-scaleround` 50 (725 to 774), `L4-brushoffer` $40, `L5-bakeryprices` $6 (unique: 4 + 5 ball = 19), `L5-circleout` 4, `L3-beadnecklaces` 10, `L6-hiddenpair` 10 (2 and 8), `L4-heightline` 9, `L6-shelfbooks` 6, `L3-chessboard` 33, `L1-chairblock` 34, `L2-ticketnotes` 28, `L4-secretspread` 96 (Monday counted as 3).
- **`L6-tintpaint`**: now "Tin A holds 4 times as much paint as Tin B. Tin A holds 45 mL more paint than Tin B." One reading. Fixed.
- **`L2-recyclegrid`**: "Weeks 1, 2 and 3 gave 30, 50 and 50 kg in all." One reading in the natural order (33 kg); a child who reads the three totals in another order gets 13 kg. Low: say "In week 1 both classes recycled 30 kg together, in week 2 50 kg, in week 3 50 kg."
- Explanations and hints: arithmetic right everywhere. Low: `L2-oddboxes` hint example "3, 5, 7 and 4" is the case in the question and adds to 19, odd (leaks the answer); `L5-bakeryprices` explanation posits "if a ball costs $3" without saying why (a child cannot tell the answer is unique); `L3-pairproduct` explanation states 21 and 22 without a way to find them; `L2-lessonend` asks for "the hour only" (8 for 8:45), an odd request, but unambiguous.

## 3. Same story or sentence frame at more than one level (H1)

### 3.1 The 23 clusters of round 5

| Cluster | Now |
|---|---|
| weekday date, times-table count (L1 `cymbalbeats`, L3 `eights`), facing and turning, clubs, four claims, fold and cut, knock-out, circle out, boat crossing, recurrence, ferry wait, money box, sign card, big sum, due date | **closed** (15) |
| digit value (L2 `pencilboxes`, L4 `seedshop`) | **moved, not closed**: the two now share one frame "boxes of 100, packs of 10, singles / sacks of 1000, bags of 100, cups of 10, loose" |
| solids counted (L2 `edgecount`, L3 `solidedges`) | still the same ask "How many edges do X and Y have altogether?" |
| take-away game (L2 `stickgame`, L4 `reachtotal`) | kept by the builder, same game, other frame. Low |
| floor tiling | **not closed**: `L1-kitchenfloor`, `L3-chessboard`, `L4-quiltpatches` are the same checkerboard frame (alternate colours, top-left corner is X, how many Y); `L3-chessboard` and `L4-quiltpatches` both have 14 rows |
| secret 63 (L1 `secret63`, L2 `lockernumber`) | still the same frame "N-digit number, digits add to, one digit is k more" |
| seat row (L1 `seatrow`, L2 `hallseats`) | still numbered seats in rows at two adjacent levels. Low |
| stairs, tins, game pay (L2, L5, L6) | same maths, other stories. Accepted |

### 3.2 Other groups still at two or more levels (my scan)

For each of the 104 sub-structures (same-idea groups counted once) that sit at two or more levels I compared the questions by hand and with a function-word skeleton (content words masked). "R5" means written or rewritten in round 5.

**Tier A: a parent would call it the same puzzle again (22 groups).**

| # | Puzzles (levels) | What repeats |
|---|---|---|
| A1 | `L3-marketstall` R5, `L4-shuttlehours` R5 | "opens at 5 am, closes at 8 pm / runs from 7 am until 10 pm, how many hours each day": same ask, same hint, **same answer 15**; both easy for their level |
| A2 | `L3-harbourcruise` R5, `L6-ferrytrip24` R5 | pm departure plus hours and minutes, "write the time ... as four digits, like 0915", a boat trip |
| A3 | `L1-paperchain` R5, `L2-ribbonline` R5 | "N strips/ribbons in a line, each X cm, at every join/knot Y cm is lost" |
| A4 | `L1-toycars`, `L3-cupoffer`, `L4-brushoffer` R5, `L5-badgeshops` R5 | "Shop B gives 1 X free for every k X you buy": **four levels**, L4 and L5 nearly word for word |
| A5 | `L3-playlist`, `L4-sciencevideos` R5, `L5-relaylegs` R5 | three or four times in minutes and seconds, "how many seconds altogether" |
| A6 | `L1-wordcards` R5, `L2-wordorder`, `L4-numbercards20` | number names on cards in alphabetical order, "which number is in place k" |
| A7 | `L1-kitchenfloor` R5, `L3-chessboard`, `L4-quiltpatches` R5 | checkerboard (3.1) |
| A8 | `L2-fewestswaps`, `L4-heightline` R5, `L6-shelfbooks` R5 | "only neighbours may swap, fewest swaps"; round 5 made L4 and L6 both six items |
| A9 | `L1-cardtriple`, `L2-cardtriple2` R5 | "six number cards, exactly three add to T, the biggest/smallest of them" |
| A10 | `L1-twobags`, `L3-beadnecklaces` R5 | "into two bags/necklaces ... 5 and 19 is the same split as 19 and 5" |
| A11 | `L4-roundprices`, `L5-scaleround` R5 | "rounds every price/mass to the nearest k; exactly halfway rounds up; how many different ... round to X" |
| A12 | `L1-lampbench`, `L4-halfway4`, `L5-buoyhalf` R5 | two things at A m and B m, "exactly halfway, how far from the start" |
| A13 | `L1-streetwalk`, `L2-beetle`, `L5-shiptrip` R5 | N, E/W, S legs, "fewest to get back along the roads" |
| A14 | `L2-tankwater`, `L3-balloonrise`, `L4-liftmin`, `L5-hikeheight` R5 (+ `L1-robottrack`) | start value, up, down, up, down: five levels |
| A15 | `L1-storypages`, `L3-albumpages`, `L5-typeset` R5 | numbers 1 to N written, "how many digits" |
| A16 | `L2-threesavers`, `L3-shells3`, `L4-canclasses` R5 | three people, two "k more than the first", total |
| A17 | `L1-kiteheights` R5, `L2-savingsrange`, `L3-books`, `L5-zoogates` | "how much more has the most than the least": four levels |
| A18 | `L1-eggtrays`, `L2-pencilboxes` R5, `L4-seedshop` R5 | bundles of 1000, 100, 10 and singles |
| A19 | `L1-oddnumber`, `L4-oddtable` | "four of these numbers are in one times table, one is not, which?" |
| A20 | `L1-drinksmachine`, `L2-ticketnotes` R5, `L4-tokenstall` | "only two kinds of coin/note/token, no change, prices 1 up to N, how many can be paid" |
| A21 | `L4-podium`, `L5-committee`, `L6-councilpick` | "choose three different jobs from N people": 7, 9, 11 |
| A22 | `L1-racerun`, `L2-cyclerace` (+ `L2-racesecond`, `L3-race`) | a race with 30 runners/riders, passes 5; ranking by "faster than" at two adjacent levels |

R5 = 19 of the 22 groups contain a round-5 puzzle (all but A19, A21, A22); both members are round-5 work in 8 groups: A1, A2, A3, A4, A5, A7, A8, A18.

**Tier B: same idea and ask, other story (accepted as "same idea at another age", but they add up).** The logic genres: `logic_match` at all six levels with the same cast Ali, Ben, Chen, Dina (L3 to L6) and the same sentences "X does not play A or B. Y plays C", and `logic_order.rank` at all six levels; `money.unitary_price` L3 to L6 ("N kg cost $X, how much do M kg cost"); `unit_convert` L2 to L5; `handshakes` L1 to L5; `combinations` L1 to L5 ("A set is one X and one Y"); `L2-toyboxshape`/`L3-cuboidclue` (R5, "is it a cube, a cone, ...?") and `L2-oddboxes`/`L3-sixodds` (R5)/`L5-oddsum` (odd or even); `L5-orangeprofit`/`L6-tvprofit` (both answer 25, the same ratio 4 : 5); `L5-walkmeet`/`L6-walkers`; `L4-dollarshare`/`L5-stampgive`; `L3-missednumber`/`L5-lostnumber`; `L2-swaphana`/`L4-swaphundreds` (the same clause "swaps the hundreds digit and the ones digit"); `L1-oddbig`/`L2-sortrule2`/`L3-cardkeep` ("keeps only the numbers that are ...").

**Why the verifier does not see it.** The cross-level rule needs 6 shared masked four-word runs for the same sub-structure (8 for any pair) and does not count runs found in 8 or more questions of the bank, so a frame that is repeated widely counts less. Nouns differ, so the runs differ. I tried a function-word skeleton (content words to `W`, numbers to `#`, names to `N`; best sentence pair, sequence ratio) on the 336 cross-level pairs of one sub-structure: it gives 0.80 or more for 25 of my 28 test pairs (123 pairs in all, 41 at 0.95 or more, many of them the stock logic frames). That is the shape of rule C below.

**Owner-ruling check on numbers and answers.** By the builder's literal rule: 0 violations. Same answer plus one shared number of 10 or more (the rule needs two): `L6-helmetsale`/`L5-penboxes` (85 and 68), `L5-pumpjob`/`L2-sevens`, `L1-racerun`/`L2-clubdays`, `L1-chairblock`/`L5-routeplan`, `L1-marblesmore`/`L2-seesaw`, `L3-houses`/`L6-pondfish`, `L3-mat168`/`L4-liftmin`. Different stories, coincidences. Low.

## 4. The nine pairs at exactly 5 shared runs

| Pair | Same to a parent? |
|---|---|
| `L1-twodice` / `L5-spinners8` | **Yes**: ordered pairs that add to 10, "Count A3 with B7 ... as different" and "A 3 on the first spinner ... is different from"; answers 5 and 7 |
| `L2-deliveryrobot` / `L5-lilypads` | **Yes**: 4 right and 3 down in any order at both levels (35 and 17 with a blocked pad); `L4-puddle` also has a blocked corner "2 blocks east and 1 south", so three levels |
| `L2-racesecond` / `L3-race` | **Yes**: "A is faster than B ... Who came second / finished third?" with the same sentence frame and a race at both |
| `L3-harbourcruise` / `L6-ferrytrip24` | **Yes** (A2); both round-5 work |
| `L4-sunflower` / `L6-savingsbox` | **Yes**: "A line graph shows the X at the end of each Y: values. What was the biggest rise/growth?" (+ `L5-treegrowth`) |
| `L4-brushoffer` / `L5-badgeshops` | **Yes** (A4); both round-5 work |
| `L1-shortestkid` / `L4-fivechildren`, `L1-shortestkid` / `L6-secondtallest`, `L4-fivechildren` / `L6-secondtallest` | No for the first two (different length and ask, the stock frame "X is taller than Y"); the L4/L6 pair is close (a five-person chain with the same words) but Low |

## 5. Level fit against `docs/moe/syllabus_by_level.md`

- **Replaced items.** `L3-beadnecklaces` (25 beads, two unlabelled necklaces, each at least 3): P3 whole numbers and listing, fits; but it is the frame of `L1-twobags` (A10). `L4-longestwalk` (5/6, 7/9, 3/4 km): comparing unlike fractions is P3 and the common denominator 36 is above the P4 limit of 12, but the hint gives it and the task is easier than the removed mixed-number addition (P5): fits (Low). The other replacements in the table of section 3 of `FIXES_ROUND5.md` were read one by one.
- **Above the level (8, all Low to Medium):** `L1-pianotime` (1 h 35 min to minutes is P2; P1 has one hour or half an hour only); `L2-riceleft` (subtracting kg and g across units is P3 "compound units"); `L3-squarepicture` (the side of a square from its area is P4 p.39); `L3-pairproduct` (21 × 22 is two-digit by two-digit, P4); `L5-bakeryprices` (three equations in three symbols; letters are P6); `L5-scaleround` (rounding to the nearest 50 g; P4 has 10, 100, 1000); `L6-parkvisitors` (nearest ten thousand); `L5-shapelines` (pentagon, hexagon, octagon are in no MOE shape list; line symmetry is P4, fine). `L6-sweettin` is probability, which the syllabus has at no level (accepted as enrichment since round 3).
- **Well below the level (10, Low):** `L3-marketstall` and `L4-shuttlehours` (am/pm hours, P1 to P2), `L4-seedshop` (P2 place value), `L5-hikeheight` (P3), `L5-buoyhalf` (P3/P4), `L4-sciencevideos` and `L5-relaylegs` (P3 seconds), `L6-ferrytrip24` (P3), `L6-juiceleft` (P4), `L6-helmetsale` (P5). Four of my 17 Level 6 puzzles are P3 to P5 content. This is a mix of days, not an error, but it is also why A1 and A2 look like the same puzzle: both are the easy sibling of a Level 3 idea placed at Level 4 or 6.
- Retired/limited sub-structures from round 3 and 4 are still absent where they should be; the six retired in round 5 are in no level.

## 6. Reproducibility and the source lock

- **Two full-tree runs** on copies of the whole working tree (6,748 source files, 1,361.5 MB, digest `9df6827f45c36ddc`): run A `PYTHONHASHSEED=1`, run B `PYTHONHASHSEED=12345`, separate `TMPDIR` (so the PDF text cache was rebuilt twice). Both: month 11 **0 FAIL, 114 REVIEW**; month 12 **0 FAIL, 100 REVIEW**; structure 0 FAIL; capacity 0 FAIL. `VERIFY_REPORT.md` of both months, `STRUCTURE_REPORT.md` and the console output are **byte-identical** (`cmp`). They equal the committed reports except for the digest line (the working tree differs from the one behind the committed reports: other agents changed files under `practice/`).
- `--selftest`: 112 PASS, 0 problems (25 s). Builder's `test_check.js` 143 checks, `test_site.py` on my scratch build 483 checks, `test_flag_off.py` 15 checks: all pass.
- **Source lock realism.** It holds file counts per root and per folder (99% of the counts), 617 PDFs, and a list of paths that must exist. It is count-only: `bytes_at_update` is written and never read. I emptied (truncated to 0 bytes, paths and counts kept) all text files of `docs/books`, every `practice/holiday/**/lesson.py`, the PDFs of `outputs/designed` and `outputs/print`, and the JS of `p5`/`p6`: 998 MB instead of 1,361 MB, a third of the text the near-copy checks read. The lock **did not refuse**; the run produced 6 FAIL for other reasons and exit 1, with no "INVALID VERIFICATION". `--selftest` did notice (1 problem), because the probes need their sources. So: a tree with the right number of empty files is accepted. **M2.** Fix: also enforce a minimum of bytes per root and a manifest of paths with sizes for the ~620 PDFs and the files behind the probes.
- The digest line changes with any file, so two honest runs a day apart differ by one line; compare reports without it (as the builder says).

## 7. Year model, my own code

Units per level (retired removed, `same_idea_groups` once, the fixed-page sub-structure excluded): **L1 71, L2 87, L3 108, L4 106, L5 102, L6 104** (equal to the README). Family-capped capacity (family at most 3 per quarter) is Σ min(3, units per family): **69, 82, 98, 97, 94, 99** against 61 (L1, L2) or the 92 days of the longest quarter (L3 to L6): slack **8, 21, 6, 5, 2, 7**.

- **L1 and L2** (rotation of 61 days, the released Nov and Dec are the cycle; family at most 3, never adjacent, wrap-around checked): 0 problems in the released cycle. Loss of any 1, any 2 (1,830 of 1,830 pairs) and 400 random triples of the 61 used: all refillable at both levels. `arrays.border_tiles` (extended to Level 1 in round 5, used by `L1-chairblock`) is **not** a real dependence: without it L1 has 70 units and capacity 68; border_tiles invalid plus any 2 other losses is still refillable in all 1,770 cases at L1 and L2. The "slack 10" is units minus 61; the true limit is 8 critical losses. **Risk: Low.**
- **L3 to L6** (integer program, HiGHS: one unit a day on 366 dates, once per calendar quarter, no unit twice within 30 days circularly, family at most 3 per quarter and never on consecutive days, Nov and Dec fixed to the bank): **feasible at all four levels.** Loss of two sub-structures at every level, 8 random draws of critical (family of 3 or fewer) unreleased units, 6 draws of released units (the day is unfixed and rewritten), 4 mixed draws: **all feasible at L3, L4, L5, L6.** The tolerance is exactly the slack, which I confirmed by solving: losing 6 / 5 / 2 / 7 critical units is feasible at L3 / L4 / L5 / L6, losing 7 / 6 / 3 / 8 is infeasible. Four critical units lost: L3, L4, L6 feasible (3 of 3 each), **L5 infeasible (3 of 3)**.
- **Level 5 (M1).** Slack 2 means three retirements break the year. 73 of its 102 units are critical; several already carry a note a future audit may use (`strategy.fake_coin` enrichment, `counting_routes.grid_routes` and `rate.work_and_time` flagged in round 5 as outside the syllabus, `symbols.symbol_equations` above the level), and the last two audits retired 15 and 6 sub-structures. With `arrays.border_tiles` invalid (it is a P3 idea used below level) capacity is 93 and **border_tiles invalid plus 2 other losses is infeasible (4 of 4)**. Round 5 asked for 4 or more new Level 5 sub-structures before April; none were added and the usable units fell from 106 to 102. Risk: **Medium, high impact.**
- **H2: answer budget at L3 to L6 (not in `year_model.py`, not in the verifier).** The verifier fails a repeated answer at a level for the whole year (line 871). Whole numbers below 100 are used up fast: single digits at most 4 times each, two-digit values 10 to 99 once (90 values).

| Level | Answers below 100 in Nov and Dec (share) | Single digits left (36 minus used) | Two-digit values left | May still be below 100 in the next 305 puzzles |
|---|---|---|---|---|
| 3 | 37 of 61 (61%) | 29 | 60 | 89 (**29%**) |
| 4 | 33 (54%) | 30 | 63 | 93 (30%) |
| 5 | 31 (51%) | 33 | 62 | 95 (31%) |
| 6 | 38 (62%) | 32 | 56 | 88 (29%) |

So January to October must have at least 70% of their answers at 100 or more, a fraction, a decimal or a word, while Nov and Dec have 39 to 49%. Counting puzzles (handshakes, patterns, ways) naturally give small answers; authors will have to scale the numbers up or the owner relaxes the rule (for example: an answer of 10 or more may return after 90 days, as the 60-day rule at Levels 1 and 2). Also the digit 8 at Level 3 is already used 3 times of 4 (`L3-magic`, `L3-barpieces`, `L3-raffledigits`, the last one new in round 5).

## 8. Browser spot check (scratch build, flag on, Chromium via Playwright)

- `test_flag_off.py` on the real tree: **15 checks, 0 failed**; the committed signup and level pages equal the flag-off generator output and carry no teaser; `site_enabled` is false; `git status website` empty.
- **Rollover from 3 time zones** (Pacific/Kiritimati, America/Los_Angeles, Asia/Kolkata), six level pages, 12 instants (10 s before and 5 s after Singapore midnight at the end of 30 Nov, 14 Dec, 31 Dec, 31 Oct 2027, 1 Nov and 31 Oct 2026): **216 of 216 show the Singapore-date puzzle** from my own copy of the bank, or, on the three dates with no released puzzle (1 Jan, 31 Oct 2027, 31 Oct 2026), the fixed puzzle with the answer button visible and no date.
- **Fallback:** 15 Jan 2027, 24 Oct 2026, 29 Feb 2028, 30 Jun 2027 on six pages: 24 of 24 show the fixed puzzle and request no `/teasers/` file; with `/teasers/*` blocked the two built-in months still show (6 of 6).
- **No JavaScript:** 6 of 6 pages show the fixed puzzle in `#pzBox`, visible.
- **Answer formats** with the page's own `MiTeaser.check` on the exported month files: 6,324 accept/reject checks over all 366 puzzles (the shown answer, the raw answer, "It is X", "It's X", "The answer is X", spaces, a full stop, units, number words from "nineteen" to "one hundred and five", wrong values, the other options): **0 bad**. Edge cases all as wanted: "nineteen", "Nineteen." for 19 (ok), "eighteen" (no); "the 25th", "25th" (ok), "the 24th" (no); "13 December", "December 13", "13th of December", "on 13 Dec" (ok), "13 November", "14 December" (no); "five and a half", "5 1/2", "5.5" for 11/2 (ok); lettered options "b", "(B)", "option b" for the second option (ok), "c", "e", "north or east", "not east" (no), "facing east" (ok). Low: "2 thirds" is not accepted; "Not Kumar, Siti" is refused (any "not" fails).
- No puzzle uses `choices` yet, so choice answers were tested only through the matcher (as above), not through a puzzle on a page.
- **Layout: all 366 puzzles at 390 px** (light), and 72 more in dark: the right puzzle for the date, no sideways scroll (`scrollWidth` 390), the puzzle box inside the viewport, **smallest text 14 px or more at load, after a wrong answer with the hint, and after a right answer** (366 of 366 each, 72 of 72 each in dark).
- Builder's `test_site.py` on my scratch build: **483 checks, 0 failed.** `test_check.js`: 143 checks, 0 failed.

## 9. GO / NO-GO

**Nov and Dec bank, release: NO-GO** until H1 is dealt with (replace the later or the round-5 member of each Tier A group of section 3.2, about 25 puzzles of 366, or the owner accepts "same idea, new story" in writing for named groups). Nothing else blocks it.

**January, per level: CONDITIONAL GO.** What exactly must hold before January is written (G) and before it is released:

| # | Condition (all levels) |
|---|---|
| G1 | A frame rule in `verify_bank.py`: for puzzles at different levels in the same sub-structure or same-idea group, the best sentence pair by function-word skeleton (content words, numbers, names masked) at 0.80 or more is a REVIEW line with a ledger of accepted pairs, 0.90 or more a FAIL; no exemption for runs found in 8 or more questions inside such a pair; the stock families (`logic_order`, `logic_match`, `logic_truth`) are exempt only for the sentence "X is taller than Y" itself. Every January puzzle is compared with all released puzzles and with the other drafts of the same batch. |
| G2 | The Tier A groups of section 3.2 resolved in Nov and Dec, or listed as accepted by the owner. |
| G3 | The answer budget (H2): either an owner decision relaxing the yearly answer rule at Levels 3 to 6, or a "whole numbers below 100 left" table in the verifier and a January batch with no more than about 9 such answers per level (29% of 31). |
| G4 | The new text-answer asks written first (solver, independent checker, sample, cite), at least two per level; the January batch has at least 3 text answers per level (4 at L5 and L6); from January the "below 3 a month" line is a FAIL, not a WARNING. |
| G5 | Source lock: enforce bytes per root and a path manifest (M2). |
| G6 | A second reader hand-solves at least 15 puzzles per level of the January batch, new items first, and the batch is run through my screens (A, B, C, N, G, S) as well as the builder's. |

| Level | Decision | Level-specific conditions |
|---|---|---|
| 1 | **GO** | G1 to G6. R5 members of Tier A to resolve: `L1-wordcards`, `L1-kitchenfloor`, `L1-paperchain`, `L1-kiteheights` (and the older `L1-toycars`, `L1-oddnumber`, `L1-racerun`). The six returns a year need six stories per sub-structure: keep a ledger. `arrays.border_tiles` is not a risk. Text answers 6 of 61, the closest to target |
| 2 | **GO** | G1 to G6; `L2-ribbonline`, `L2-pencilboxes`, `L2-cardtriple2`, `L2-lockernumber`, `L2-ticketnotes`; `L2-riceleft` is P3 content assembled from two Question Bank starters (replace or move to L3); 21 critical losses of slack |
| 3 | **GO** | G1 to G6; `L3-marketstall`, `L3-harbourcruise`, `L3-beadnecklaces`, `L3-raffledays`; `L3-squarepicture` is P4 (side of a square from its area); the digit 8 has one use left; the answer budget bites first here (61% below 100) |
| 4 | **GO** | G1 to G6; the largest cleanup: `L4-shuttlehours`, `L4-brushoffer`, `L4-sciencevideos`, `L4-quiltpatches`, `L4-seedshop`, `L4-heightline`, `L4-canclasses`; slack 5 critical losses |
| 5 | **CONDITIONAL, thinnest year** | G1 to G6, and before March at least 4 new Level 5 sub-structures with solver, checker and cite (the round-5 audit asked; not done) and a written decision on `arrays.border_tiles` at L5; `L5-badgeshops`, `L5-relaylegs`, `L5-buoyhalf`, `L5-scaleround`, `L5-shiptrip`, `L5-hikeheight`, `L5-typeset` (7 round-5 twins); `L5-bakeryprices` is above the level |
| 6 | **GO** | G1 to G6; `L6-ferrytrip24`, `L6-shelfbooks`; a third of my Level 6 sample is P3 to P5 content (`L6-juiceleft`, `L6-helmetsale`, `L6-parkvisitors`); probability is outside the syllabus; slack 7 |

### The text-answer shortfall: is it a release blocker?

**No, not for Nov and Dec; yes, as a gate for January onward and a dated milestone for the year.**

- Nov and Dec hold 25 text answers of 366 (L1 6, L2 5, L3 4, L4 4, L5 3, L6 3: 5 to 10% against the owner's 11%). Each is correct and the page accepts the natural wordings (section 8), so a visitor is not harmed; the shortfall is variety, not correctness.
- The numbers in the plan are tight. 40 a year at Levels 3 to 6 means 10 text-capable sub-structures each used in all four quarters: **zero slack**, one retirement gives 36. Set the hard target at 36 (about 10%) and plan 12 text-capable sub-structures, or count word and letter answers from any sub-structure whose answer set is closed ("which is cheaper, A or B", "which is longer").
- **Do not buy text answers with more of the same genres.** The cheap ones (`logic_match`, `logic_order`, `logic_truth`) already repeat their frame and their cast (Ali, Ben, Chen, Dina) at four to six levels, which is H1. The new asks in `TEXT_ANSWER_PLAN.md` section 3 (who has the most in a table, which shop, a latin-square cell, a place on the shortest route, classify a triangle) are the right ones; each new text puzzle goes through G1.
- Enforce it at the batch, not at the year: from January the verifier fails a month with fewer than 3 text answers at a level (4 at L5, L6) and the plan's own order (asks first, puzzles second) holds. Answer-budget H2 helps here: a word is a distinct answer outside the 10 to 99 range.

## Severity list

- **High (2):** **H1** the owner ruling "one frame, one level" is not met (22 Tier A groups, 19 with a round-5 puzzle, 8 with two), the closure claim in `FIXES_ROUND5.md` is wrong and the verifier cannot see it; **H2** the yearly answer rule makes Levels 3 to 6 unfeasible as ruled (29 to 31% of the remaining puzzles may be a whole number below 100, against 51 to 62% now), untracked.
- **Medium:** M1 Level 5 year tolerates 2 retirements, 4 new sub-structures asked and not added; M2 the source lock is count-only (accepted a tree with 27% of the bytes gone); M3 text answers 5 to 10% against 11% (not a blocker, a January gate); M4 six of the nine 5-run pairs are the same puzzle; M5 `L2-riceleft` is P3 content assembled from two Question Bank starters (Low to Medium); M6 Tier B logic genres at four to six levels with one cast; M7 level fit: 8 puzzles above their level and 10 well below.
- **Low:** the 9 Low matches of section 1; `L2-recyclegrid` reading order; hint leak `L2-oddboxes`; thin explanations `L5-bakeryprices`, `L3-pairproduct`; `L1-pianotime` P2 content; `L2-lessonend` "hour only"; "2 thirds" and "Not Kumar, Siti" not accepted; same answer plus one big shared number in 7 pairs; the digest changes with any file of the tree.

## How to reproduce

Scripts and outputs are in `/dev/shm/a6` (not committed): `mkcorpus.py`, `screen2.py` (A, B, C, N), `screen5.py`, `screen6.py` (G), `screen_s.py` (S), `cross.py` and `skel.py` (cross-level frames), `year.py`, `ip.py`, `loss.py`, `bound.py`, `l12.py` (year model), `br1.py` to `br3.py` (browser), `vA.log`/`vB.log` (verifier runs).
