# Fix round 6 (audit AUDIT_ROUND6, conditions G1 to G6 and items H1, H2, M1, M2, M4, M7)

Written 24 Oct 2026. Scope: `website/teasers/`, `docs/terms/owner_decisions.md` (one entry, ANSWER-WINDOW). Jan to Oct are **not** written. `website/mi_signup.html`, `website/level_pages/*.html` and `website/dist` are untouched (the flag is off; `test_flag_off.py` passes).
Owner frame ruling (a story or frame appears at ONE level only) and the answer window below are adopted defaults of the owner's delegate, revocable.

## 1. Closed / not closed

| Item | Status | What was done | What is left |
|---|---|---|---|
| H1, frame rule (G1) | Closed | `verify_bank.py` scores the function-word skeleton of every sentence window (section 2). 0.80 is a REVIEW line, 0.90 a FAIL unless the pair is in `frame_ledger.json`. Replayed on the 39 audit pairs in `--selftest`: 18 score 0.80 or more. | The rule is a net for frames, not for stories: 21 of the 39 audit pairs (for example a paper chain and a ribbon line) use other sentences for the same story and are caught only by a reader. |
| H1, the 22 Tier A groups (G2) | Closed | Every group has one keeper level; every other puzzle has a new story, new sentence frames, other numbers and, where the kind allowed, another ask (section 3). 43 puzzles of the 22 groups are rewritten or replaced, 7 more for the audit's clusters and 5-run pairs, and 18 others for level fit, the answer window and the text gate (68 in all). | 15 Tier B pairs at 0.90 or more stay, in `frame_ledger.json` (section 2). |
| H2, answer budget (G3) | Closed | Full-year answer rule dropped at Levels 3 to 6, ANSWER-WINDOW in force (section 4); budget table in `batches/YEAR_PLAN.md`; README; `docs/terms/owner_decisions.md`. Five answer collisions of the Nov and Dec bank under the new rule were fixed. | None. |
| M2, source lock (G5) | Closed | Bytes per root and per folder plus a manifest of 6,748 paths (section 5). | The digest line still changes with any file of the tree. |
| M1, Level 5 (4 new sub-structures) | Closed | Five new Level 5 sub-structures with solver, independent checker, worked examples and cite (section 6). Level 5 slack 2 to 10; the year model survives 8 lost sub-structures in 3 of 3 draws (was 2). | Level 5 family-capped quarter capacity 102 against 92 (slack 10); the decision on `arrays.border_tiles` at Level 5 is no longer urgent. |
| M3, text answers (G4) | Closed as a gate | Six text-answer asks coded; gate in the verifier from January; January allocation in `TEXT_ANSWER_PLAN.md` section 6; the Level 1 and 2 rotation holds at least 4 text answers in every month (section 7). | The January to October puzzles. |
| M4, nine pairs at 5 shared runs | Closed | Seven of the nine pairs rewritten, two (the stock "taller" frames) left, section 3.2. | None. |
| M5, `L2-riceleft` | Closed | Replaced by a Level 2 shop-choice puzzle. | |
| M7, level fit: 8 above, 10 well below | Closed | All 18 changed (section 3.3). | |
| G6, second reader | Closed | 102 puzzles hand-solved, 17 per level (section 8). | A second reader for the January batch, when it exists. |
| M6, Tier B logic genres at 4 to 6 levels | Open, accepted | In the ledger with reason. | See section 10. |

## 2. The frame rule (`verify_bank.py`, `frame_ledger.json`)

* **Skeleton.** A sentence becomes a list of tokens: numbers `#`, names `N`, the function words of the verifier's `FUNC` list kept, every other word `W`; a list of three or more numbers ("14 cm, 9 cm, 21 cm and 17 cm") one token `L`. A second form collapses runs of `W` and of `N`.
* **Windows.** One or two neighbouring sentences with at least ten words. A window made only of the stock comparison sentence ("Ali is taller than Ben.") and bare asks of under five words ("Who is the shortest?") is skipped.
* **Score.** The best `difflib` sequence ratio over all window pairs (raw and collapsed form) of two puzzles of the **same sub-structure or same-idea group at different levels**.
* **Verdict.** 0.80 or more: a REVIEW line in `STRUCTURE_REPORT.md`; 0.90 or more: a FAIL unless the pair is in `frame_ledger.json` with a reason and the hash of both wordings (an edit of either question ends the protection). The ten-word minimum, the two-sentence window and the number-list token were chosen after trying 5, 6, 8 and 10 words and windows of 1, 2 and 3 sentences on the audit pairs and on the bank: at 5 words every pair of bare asks ("How many different ways can it take?") scores 1.00, 25 of the 39 audit pairs are found but 45 pairs of the bank would fail; at 10 words 18 are found and 15 fail.
* **Test on the audit pairs.** `selftest_probes.json` section `round6_frames` holds the 39 same-frame pairs of AUDIT_ROUND6 (Tier A groups and the 5-run pairs) in their round-5 wording. The audit kept its own list of 28 pairs outside the repository (scripts in `/dev/shm/a6` only), so these 39 are rebuilt from its tables. The rule scores **18 of 39 at 0.80 or more** (8 of them at 0.90 or more); the other 21 score 0.00 to 0.79: they tell the same story in other sentences (a paper chain of strips and a line of ribbons, a seat row and a bench row) or consist of stock sentences. The audit's own skeleton found 25 of its 28 on a looser metric (sentences of 5 words); that setting here finds 25 of the 39, at the price of 45 failing pairs on the bank.
* **Result on the bank.** 49 pairs of one sub-structure at two levels score 0.80 or more: 15 at 0.90 or more are all Tier B and are in the ledger; 34 are REVIEW lines. None of the 36 puzzles that replace Tier A members scores 0.80 or more against a puzzle of its group.
* **Draft months.** `verify_bank.py 01` now loads a month that is not released as a draft and compares it with every released month and the other drafts (all structure, frame and answer-window rules), as G1 asks.

## 3. What changed: 68 puzzles against the round-5 bank (58 replaced by another sub-structure or story with a new id, 10 reworded with the same id)

### 3.1 The 22 Tier A groups (keeper level first; the others are the rewrites)

| # | Group | Kept | Rewritten (old id -> new id) |
|---|---|---|---|
| A1 | am and pm hours | L3 (`marketstall` -> `stallminutes`, now minutes between 7:15 am and 1:45 pm) | L4 `shuttlehours` -> `airportshuttle` (6:40 am to 10:20 pm less a 75-minute break) |
| A2 | pm time plus a trip, four digits | L3 `harbourcruise` | L6 `ferrytrip24` -> `islandroutes` (which stop on the quickest of several boat routes) |
| A3 | strips with an overlap | L1 `paperchain` | L2 `ribbonline` -> `hosepieces` (how many pieces, given the total) |
| A4 | one free for every k | L3 `cupoffer` | L1 `toycars` -> `stickersheets` (single price against a set price, the saving); L2 `notebooks` -> `hairclips`; L4 `brushoffer` -> `gluesticks` (pack against single); L5 `badgeshops` -> `nametagpacks` (three pack sizes, no free items) |
| A5 | minutes and seconds to seconds | L3 `playlist` | L4 `sciencevideos` -> `parkpaths` (first stop on the shortest path, text answer); L5 `relaylegs` -> `snailrace` (which snail is fastest, text answer) |
| A6 | number names in A to Z order | L1 `wordcards` | L2 `wordorder` -> `numbershelf`; L4 `numbercards20` -> `spellingbee` |
| A7 | checkerboard | L3 `chessboard` | L1 `kitchenfloor` -> `noticeboard`; L4 `quiltpatches` -> `cupcaketray` |
| A8 | neighbour swaps | L4 `heightline` | L2 `fewestswaps` -> `beadsticks` (six beads); L6 `shelfbooks` -> `parcelbelt` (seven parcels) |
| A9 | three of six cards | L1 `cardtriple` | L2 `cardtriple2` -> `tilescore` |
| A10 | two bags or necklaces | L1 `twobags` | L3 `beadnecklaces` -> `ropepieces` (a rope cut in two) |
| A11 | rounding, how many round to X | L4 `roundprices` | L5 `scaleround` -> `postalscale` (to the nearest 10 g; was 50 g, above the level) |
| A12 | halfway | L1 `lampbench` | L4 `halfway4` -> `ferrypier` (the middle is known, find the far end: new kind `halfway_end`); L5 `buoyhalf` -> `sailheight` (new sub-structure, height of a right-angled triangle) |
| A13 | north, east, south legs | L2 `beetle` | L1 `streetwalk` -> `bakerywalk`; L5 `shiptrip` -> `dronepaths` (five legs) |
| A14 | up, down, up, down | L2 `tankwater` | L1 `robottrack` -> `stonehops`; L3 `balloonrise` -> `kitegusts` (ends at, not greatest); L4 `liftmin` -> `liftfloors` (lowest floor); L5 `hikeheight` -> `rhombuscut` (new sub-structure, angles in a rhombus) |
| A15 | digits of 1 to N | L3 `albumpages` | L1 `storypages` -> `lockerdigits`; L5 `typeset` -> `sportsbibs` (85 to 124, crosses 99) |
| A16 | three people, two with more | L3 `shells3` | L2 `threesavers` -> `runlaps` (one has fewer); L4 `canclasses` -> `grandchildren` |
| A17 | most minus least | L2 `savingsrange` | L1 `kiteheights` -> `craneboard` (who folded the most: text answer); L3 `books` -> `petvotes`; L5 `zoogates` -> `shoptakings` |
| A18 | bundles of 1000, 100, 10, ones | L1 `eggtrays` | L2 `pencilboxes` -> `walletmoney` (notes and coins); L4 `seedshop` -> `moneypurse` (who has more money: text answer) |
| A19 | four in one times table | L1 `oddnumber` | L4 `oddtable` -> `bluelockers` |
| A20 | only two coin sizes, how many prices | L1 `drinksmachine` | L2 `ticketnotes` -> `ticketstrips`; L4 `tokenstall` -> `pencilpacks` |
| A21 | choose three different jobs | L5 `committee` | L4 `podium` -> `stageline`; L6 `councilpick` -> `lettercodes` (four letters of eight) |
| A22 | race places | L2 `cyclerace` | L1 `racerun` -> `swimturn`; L2 `racesecond` -> `cousinages` (also the 5-run pair with `L3-race`) |

Clusters of section 3.1 of the audit that were still open: solids counted (L2 `edgecount` -> `windowsolids`, corners of a shelf of solids; L3 `solidedges` kept), secret 63 (L2 `lockernumber` -> `blocknumber`), seat row (L2 `hallseats` -> `ferrybenches`), digit value (A18), floor tiling (A7).

### 3.2 The nine pairs at exactly 5 shared runs

| Pair | Now |
|---|---|
| `L1-twodice` / `L5-spinners8` | L5 -> `codelock` (two codes typed one after the other, sum 30) |
| `L2-deliveryrobot` / `L5-lilypads` (and `L4-puddle`) | L5 -> `ladybirdgrid` (5 by 4 grid, one junction avoided, ask unchanged but other numbers and wording); `L4-puddle` kept (blocked corner at another place, other grid) |
| `L2-racesecond` / `L3-race` | L2 -> `cousinages` (older than, the oldest) |
| `L3-harbourcruise` / `L6-ferrytrip24` | L6 -> `islandroutes` |
| `L4-sunflower` / `L6-savingsbox` (and `L5-treegrowth`) | L5 -> `pondlevel` and L6 -> `coffeecups`, both the biggest fall |
| `L4-brushoffer` / `L5-badgeshops` | both rewritten (A4) |
| `L1-shortestkid`, `L4-fivechildren`, `L6-secondtallest` | the stock frame "X is taller than Y": left (audit: Low); they stay in the structure report at 5 runs |

### 3.3 Level fit

| Puzzle | Problem | Now |
|---|---|---|
| `L1-pianotime` (above) | 1 h 35 min to minutes is P2 | `L1-marbleswap`: who has more marbles after a gift (add and subtract within 100) |
| `L2-riceleft` (above) | kg and g across units is P3; assembled from two Question Bank starters | `L2-markershops`: which of three shops is cheapest |
| `L3-squarepicture` (above) | side of a square from its area is P4 | `L3-posterribbon`: perimeter of a rectangle |
| `L3-pairproduct` (above) | 21 x 22 | sum 53, product 282, the numbers are 6 and 47 |
| `L5-bakeryprices` (above) | three equations in three symbols | two items, two lines |
| `L5-scaleround` (above) | nearest 50 g, not in P4 | `L5-postalscale`, nearest 10 g |
| `L6-parkvisitors` (above) | nearest ten thousand | nearest thousand |
| `L5-shapelines` (above) | pentagon, hexagon, octagon in no MOE list | square, rectangle, rhombus, parallelogram |
| `L3-marketstall`, `L4-shuttlehours` (below) | hours between two am and pm times (P1 to P2) | minutes between times with minutes; the Level 4 one with a break (new kind `clock_span`) |
| `L4-seedshop` (below) | P2 place value | `L4-moneypurse`, a four-step money comparison |
| `L5-hikeheight` (below) | P3 | `L5-rhombuscut` (P5 angles in a rhombus) |
| `L5-buoyhalf` (below) | P3 to P4 | `L5-sailheight` (P5 triangle area, height on the longest side) |
| `L4-sciencevideos`, `L5-relaylegs` (below) | seconds, P3 | `L4-parkpaths`, `L5-snailrace` |
| `L6-ferrytrip24` (below) | P3 | `L6-islandroutes` |
| `L6-juiceleft` (below) | P4 decimals | `L6-fishtank` (volume of a cuboid in litres, P5 to P6) |
| `L6-helmetsale` (below) | P5 discount | the price before a 30% discount (P6 find the whole) |

## 4. ANSWER-WINDOW (H2)

* **Rule** (Levels 3 to 6): the same answer value may not recur within a level within 60 days (365- and 366-day year, circular); the same answer with the same sub-structure (or same-idea group) never within 92 days. Single digits are not exempt, so a 60-day window holds at most 9 of them. Levels 1 and 2 keep their rules (L1L2-GAP60: not twice within 60 days, a single digit at most twice).
* **Where.** `verify_bank.py` (`answer_window_rules`; the old `MAX_SMALL` and the full-year rule are gone), `taxonomy.json` (`answer_window_l36_days` 60, `answer_same_sub_days` 92), README, `batches/YEAR_PLAN.md` (budget table and "what is left"), `docs/terms/owner_decisions.md` (ANSWER-WINDOW, adopted default, revocable).
* **Budget.** The Nov and Dec bank holds 2 to 6 single-digit answers per level at Levels 3 to 6 (peak in any 60 days: 6, 6, 2, 3 against a limit of 9). The 305 puzzles still to write may hold at most 46 single-digit answers per level at Levels 3 to 6 (15%), against the 29 to 31% of the old rule. The two-digit values (90 a window) are never the binding limit.
* **Violations under the new rule found in the round-5 bank, fixed:** `L3-magic`, `L3-raffledigits` and `L3-barpieces` (answer 8, three times in 42 days), `L3-missednumber` and `L3-cryptsum` (9), `L4-fakecoin` and `L4-reachtotal` (4), `L6-clockafter` and `L6-goldbach` (5). Changed: `raffledigits` (digit sum 7), `barpieces` (2/3 = 10/15), `missednumber` (1 to 16, 124), `reachtotal` (59), `goldbach` (134).

## 5. Source lock (M2)

* `source_lock.json`: minimum **bytes** per root (97% of the bytes when written) and per near-copy folder, besides the files (99%).
* `source_manifest.tsv`: every one of the 6,748 source paths with its size. A key file (PDF, `docs/books`, `p5/p6` content JS, holiday `lesson.py`, anything under `must_exist`) missing or cut to under half of its size, or more than 0.5% of all paths missing or cut, is an invalid verification (exit 2).
* `--selftest` replays the audit's attack on a listing of this tree: book text, PDFs and lesson files emptied with paths and counts kept (refused), a third of all files emptied (refused), no PDFs (refused), one PDF missing (refused), 2% of the practice files gone (refused), a tracked-only tree (refused), and the real tree (accepted).

## 6. Level 5 sub-structures and text-answer asks (M1, G4)

Coded in `kinds_r4.py` (solver), `brute_r4.py` (independent checker, never imports the solvers: coordinates and angles for the quadrilaterals, pieces dealt out one at a time, every simple path of a map, Python's own evaluator for brackets, minute-by-minute clocks), `samples_r4.py` (worked instances and 30 `EXAMPLES` written as puzzles), `taxonomy.json` (levels, cite, `round: 6`). `--selftest` proves solver, checker and written answer agree on every one.

| Sub-structure | Levels | Cite | Examples |
|---|---|---|---|
| `angles.parallelogram_rhombus` | 5 | P5 MG geometry p.42 | parallelogram, rhombus (diagonal halves the angle, isosceles triangle), trapezium |
| `fractions.whole_division` | 5 | P5 NA fractions 1.1, 1.2 p.41 | 7 m in 4 pieces, 5 cakes among 6 children, 7 kg in 8 bags as a decimal |
| `rate.compare_rates` (text) | 5 | P5 NA rate p.41 | three taps, three typists |
| `order_ops.bracket_placements` | 5 | P5 NA whole numbers 2.2, 2.3 p.41 | greatest value, how many values, how many placements give 35 |
| `triangle_area.two_heights` | 5 | P5 MG triangle area p.42 | 6-8-10, 9-12-15, 15-20-25 |
| `graphs.who_has_most` (text) | 1 to 5 | P1 to P4 | who has the most, the least, the second most |
| `money.cheaper_shop` (text) | 2 to 5 | P2 to P4 money | three shops |
| `word_problems.who_has_more` (text) | 1 to 6 | P1, P3, heuristics | gifts, winnings, spending |
| `networks.first_stop` (text) | 2 to 6 | P2, P3, heuristics | first or last stop on the shortest route |
| `shapes.classify_triangle` (text) | 3 to 6 | P3, P4, P5 | by sides, by two angles |
| `measurement.heavier_after_units` (text) | 3 to 6 | P3, P5 NA decimals 1.2 | 2 kg 300 g, 2,350 g, 2.4 kg |

The audit asked for at least 4 new Level 5 sub-structures: 5 are added (and six text-answer asks, all usable at Level 5). Level 5 usable units 102 to 113.

## 7. Text-answer gate and the Level 1 and 2 rotation (G4)

* `taxonomy.json`: `text_min_per_month` 3 at Levels 1 to 4, 4 at Levels 5 and 6; `text_gate_months_exempt` 11 and 12. `verify_bank.py`: "only N text-answer puzzles in month MM, the gate from January is M" is a FAIL.
* The January bank is not written, so `TEXT_ANSWER_PLAN.md` section 6 marks the plan (which asks can supply the January text answers at each level).
* **Levels 1 and 2 are fixed by the rotation**: January is the Nov puzzles of the same days, and the round-5 bank had 1 text answer in Nov, 6 and 7 in Dec, so every other month of the year would have held 1 or 2. Fixed in the released bank: one text puzzle added at Level 1 (`craneboard`), three at Level 2 (`quizscores`, `schoolwalks`, `cardgame`), two text puzzles moved from December to November at each level (`shortestkid`, `westturns`; `cousinages`, `cakeshare`), and `build_bank.py order()` now spreads the text-answer puzzles over the month. `batches/YEAR_PLAN.md` proves at least 4 text answers in every calendar month of a 365- and a 366-day year at both levels. (The dates of all Level 1 and Level 2 puzzles changed; those of Levels 3 to 6 did not.)
* Text answers now (Nov and Dec, 61 days): L1 8, L2 9, L3 4, L4 6, L5 4, L6 4.

## 8. Second reader (G6)

`second_reader_round6.py`: 17 puzzles per level, 102 in all, the 68 new or rewritten puzzles first, the rest drawn with seed 6606 from the unchanged ones. Every puzzle was solved from its printed question, in plain Python written for that question (it imports none of `kinds*`, `brute*`, `build_bank`, `verify_bank`, `taxonomy`), and compared with the bank afterwards. Result in `batches/SECOND_READER_ROUND6.md`:

| Level | Puzzles | Agree |
|---|---|---|
| 1 | 17 | 17 |
| 2 | 17 | 17 |
| 3 | 17 | 17 |
| 4 | 17 | 17 |
| 5 | 17 | 17 |
| 6 | 17 | 17 |

Each has exactly one answer. Along the way the reader found, and the author fixed, nothing the checkers had missed; the reading-load lines (11 questions over the sentence or word limit of their level, found by the verifier) were shortened.

## 9. Results of the full run

| Check | Result |
|---|---|
| `build_bank.py` | bank rebuilt; `--plan` wrote `YEAR_PLAN.md`, 0 violations |
| `verify_bank.py` full tree | month 11: 0 FAIL, 111 REVIEW; month 12: 0 FAIL, 84 REVIEW; structure 0 FAIL; capacity 0 FAIL (6,748 source files, 1,361.7 MB, digest b73b29ef75c4dead; source lock with bytes and manifest satisfied) |
| `--selftest` | 148 PASS, 0 problems (the 39 audit pairs, answer windows, the lock attacks, 13 new kinds, 30 example puzzles) |
| `second_reader_round6.py` | 102 puzzles, 0 disagreements |
| `year_model.py` | 0 problems; cap 3 feasible at Levels 3 to 6; Level 5 survives the loss of 8 sub-structures in 3 of 3 draws |
| `test_flag_off.py` | 15 checks, 0 failed |
| `test_check.js` | 143 checks, 0 failed |
| `test_site.py` (scratch build in `/dev/shm`, flag on) | 483 checks, 0 failed |

## 10. Open items and owner decisions

1. **Tier B pairs (the only item that is a real decision).** 15 pairs of puzzles on one sub-structure at two levels still score 0.90 or more by the frame rule and are accepted in `frame_ledger.json` as "the same idea at another age" (logic genres `logic_match` at five levels, `combinations`, sticks displays, stock money frames). That follows the audit's own classification (section 3.2 Tier B) and is an adopted default of the delegate. If the owner holds that even these are "the same frame", each needs a rewrite (about 30 puzzles); delete the ledger and the verifier lists them.
2. January to October puzzles: not written. January: a level-by-level conditional GO as in AUDIT_ROUND6 section 9, now with G1 to G6 met in the tools; the batch itself still needs its own audit.
3. The 34 REVIEW frame lines (0.80 to 0.89) and the new REVIEW lines of round 6 are in `batches/REVIEW_TRIAGE.md` section D.
4. The frame rule finds 18 of the 39 audit pairs; a reader must still look at January puzzles that reuse a Tier A story.
5. Text-answer counts reach the 40 a year plan only if the January allocation of `TEXT_ANSWER_PLAN.md` section 6 is followed (Level 6 has exactly 10 text-capable sub-structures for a need of 10).
