# Fix round 5 (audit AUDIT_ROUND5, conditions C1 to C7)

Written 24 Oct 2026. Scope: `website/teasers/` and `outputs/owner_review/teasers_preview/` only. Jan to Oct are **not** written. `website/mi_signup.html`, `website/level_pages/*.html` and `website/dist` are untouched (the flag is off; `test_flag_off.py` passes).
Owner ruling for C3 (adopted): **new story AND new frame**. Every story or sentence frame now appears at one level only; where the maths structure is shared across levels the surface frame, numbers and difficulty differ.

## 1. Closed / not closed

| Condition | Status | What was done | What is left |
|---|---|---|---|
| C1 (3 High, 11 Medium frame copies) | Closed | All 14 replaced by new stories on new frames (L6-dice8 -> L6-sweettin, L4-clockfive -> L4-shuttlehours, L5-tank -> L5-busline, L4-chairs24 -> L4-vanroute, L3-tilearrays -> L3-raffledigits, L4-theatrerows -> L4-concerttickets, L3-cardcorners -> L3-squarepicture, L3-keyringtray -> L3-marketstall, L1-shapeclue -> L1-biscuithalves, L2-solidclue -> L2-toyboxshape, L6-waterbarrel -> L6-helmetsale, L2-tworopes -> L2-riceleft, L3-twentyfour -> L3-harbourcruise, L4-tilefigures -> L4-quiltpatches). Seven frames added to `retired_frames`; six sub-structures retired (`strategy.worst_case`, `factors.rectangular_arrays`, `figure_rule.nth_figure`, `angles.clock_hands`, `probability.two_dice_sum`, `volume.water_depth`). | None |
| C2 (verifier) | Closed | New rules: one-sentence match (S), same sentence with other numbers (S3), question-window match, number-unit grams (G), answer-plus-numbers window (N2), cross-level sentence-frame rule. Probed with the round 3 and 5 wordings in `--selftest` (112 cases). `source_lock.json` at 99% of current counts, folder minimums, and the verifier fails if the listed practice, split, outputs, p5 and school files are missing. Non-accepted REVIEW lines have dispositions (`batches/REVIEW_TRIAGE.md`, section C). | The dispositions are the author's reading |
| C3 (23 cross-level clusters, 74 puzzles) | Closed (see 2) | Each cluster has one keeper level; the other puzzles got a new story, a new frame, other numbers and difficulty, or a different sub-structure. The new cross-level frame rule finds 0 FAIL on the full bank (it also found about 15 extra pairs while the work was in progress; all reworded). | Nine pairs at exactly 5 shared runs (REVIEW, one run from FAIL) |
| C4 (level fit, counts) | Closed | L3-fruitsums (three simultaneous equations at P3) -> L3-beadnecklaces; L4-flour (mixed-number addition is P5) -> L4-longestwalk; the 11 Low level-fit items fixed (section 5). README counts updated and the stale numbers fixed. | Level 5 slack is 2 |
| C5 (wording, answer matcher) | Closed | L2-recyclegrid weekly-totals order, L6-tintpaint ambiguity ("Tin A holds 45 mL more paint than Tin B"), L1-fourodds example leak (replaced by L1-paperchain). `teasers.js` accepts "nineteen", "twenty-one", "two thirds", "five and a half", "5 1/2", "the 25th", "on the 13th", "13 December", with negatives. `test_check.js` (143 checks) and `test_site.py` (483 checks). | None |
| C6 (text answers) | Plan and support done, puzzles not written | `TEXT_ANSWER_PLAN.md`; `P(..., choices=, labels=)` data support; `build_bank.py` keeps the choices and uses the other options as the listed wrong answers; page accepts the letter of a lettered option and a short sentence round a name; verifier checks choices and prints a "Text answers per level" table with WARNING lines. | Text answers now: L1 6, L2 5, L3 4, L4 4, L5 3, L6 3 in 61 days, i.e. 18 to 36 a year against 40+. The puzzles of 2027 are to be written (plan section 5) |
| C7 (full re-run) | Closed | Section 6. | Second reader (section 7) |

## 2. The 23 cross-level clusters (keeper level)

| Cluster idea | Kept at | Others |
|---|---|---|
| second Thursday of the month, date by weekday | L3-secondthursday | other levels: new frame or other sub-structure |
| digit value in 6482 | L3-digitvalue6482 | L2 and L4 versions rewritten or replaced |
| edges of a solid | L3-solidedges, L2-edgecount | L2 and L3 use different solids and frames |
| turns facing west | L1-westturns | L3 replaced by L3-sixodds |
| clubs and members | L3-clubs | others replaced |
| four claims | L4-fourclaims | others replaced |
| sums of eights | L3-eights | others replaced |
| fold and cut | L2-foldcut | others replaced |
| stick game, reach the total | L2-stickgame and L4-reachtotal | different frames and numbers |
| badminton knockout | L3-badmintonko | others replaced |
| circle out | L5-circleout | others replaced |
| tin stack, stairs | L2-tinstack and L5-stairs60 | different frames |
| river boat | L5-riverboat | others replaced |
| recurrence | L6-recurrence | L4-addpattern replaced |
| ferry | L4-ferry | L2-canoetrips replaced by L2-fruitbags |
| floor tiling | L1-kitchenfloor, L2-tilebed, L3-chessboard | three different frames |
| cut card, flag cloth | L5-cutcard and L6-flagcloth | different frames |
| money box | L3-moneybox | others replaced |
| sign card | L4-signcard | others replaced |
| big sum | L1-bigtwo and L3-bigsumcards | different frames |
| secret 63 | L1-secret63 | L2 rewritten as L2-lockernumber |
| seat row | L1-seatrow | L2-cinemarow rewritten as L2-hallseats |
| due date, trip booking | L2-duedate, L3-tripbooking | fixed |

Details of every old and new puzzle are in section 3.

## 3. What changed: 82 puzzles against the round-4 bank (49 replaced by another sub-structure, 33 rewritten)

- Level 1, replaced by a puzzle on another sub-structure (7): `L1-fourodds` (number_properties.odd_even_rule) by `L1-paperchain` (measurement.overlapping_chain); `L1-libraryday` (calendar.nth_weekday_date) by `L1-parcellabel` (place_value.swap_digits); `L1-marblecontest` (invariant.one_less) by `L1-bibscores` (sorting.order_by_digit_rule); `L1-marblegame` (strategy.take_away_game) by `L1-chairblock` (arrays.border_tiles); `L1-numpattern` (sequence.alternating_steps) by `L1-wordcards` (number_names.alphabetical); `L1-signsgap` (symbols.insert_signs) by `L1-pianotime` (durations.hours_to_minutes); `L1-tapefold` (paper_folding.fold_and_cut) by `L1-kiteheights` (graphs.most_least_gap)
- Level 1, rewritten with the same sub-structure (6): `L1-circlekids`; `L1-counterbox`; `L1-fivetable` as `L1-cymbalbeats`; `L1-shapeclue` as `L1-biscuithalves`; `L1-tilewall` as `L1-kitchenfloor`; `L1-whichsun`
- Level 2, replaced by a puzzle on another sub-structure (5): `L2-busstop` (durations.timetable_wait) by `L2-birdfish` (symbols.symbol_equations); `L2-canoetrips` (moves.ferry_trips) by `L2-fruitbags` (multiplication.two_kinds_total); `L2-fourthsunday` (calendar.nth_weekday_date) by `L2-oddboxes` (number_properties.odd_even_rule); `L2-hallfloor` (arrays.checkerboard) by `L2-lessonend` (clock_reading.minute_hand); `L2-lanternring` (spatial.circle_elimination) by `L2-inkblot` (missing_number.missing_digit)
- Level 2, rewritten with the same sub-structure (10): `L2-cinemarow` as `L2-hallseats`; `L2-digitcards3` as `L2-lockcode`; `L2-digitvalue2` as `L2-pencilboxes`; `L2-ladderrungs`; `L2-recyclegrid`; `L2-secret643` as `L2-lockernumber`; `L2-sevens`; `L2-solidclue` as `L2-toyboxshape`; `L2-stripchain` as `L2-ribbonline`; `L2-tworopes` as `L2-riceleft`; reworded only: `L2-signsscale`, `L2-cardtriple2`, `L2-ticketnotes`
- Level 3, replaced by a puzzle on another sub-structure (7): `L3-cardcorners` (perimeter_area.notched_perimeter) by `L3-squarepicture` (perimeter_area.perimeter_basic); `L3-fruitsums` (symbols.symbol_equations) by `L3-beadnecklaces` (bonds.pairs_to_total); `L3-keyholder` (logic_truth.truth_tellers) by `L3-cuboidclue` (shapes.name_the_shape); `L3-keyringtray` (strategy.worst_case) by `L3-marketstall` (clock_reading.am_pm); `L3-tilearrays` (factors.rectangular_arrays) by `L3-raffledigits` (digit_puzzles.count_by_digit_rule); `L3-tripbooking` (calendar.date_in_month) by `L3-carousel` (spatial.circle_opposite); `L3-turnsfour` (spatial.turns_facing) by `L3-sixodds` (number_properties.odd_even_rule)
- Level 3, rewritten with the same sub-structure (4): `L3-bakery`; `L3-barpieces`; `L3-booksales` as `L3-museumshows`; `L3-twentyfour` as `L3-harbourcruise`; reworded only: `L3-pairproduct`, `L3-raffledays`
- Level 4, replaced by a puzzle on another sub-structure (12): `L4-addpattern` (growing_pattern.recurrence) by `L4-canclasses` (bar_model.three_amounts); `L4-bikelock` (digit_puzzles.digit_clues) by `L4-sciencevideos` (durations.minutes_seconds); `L4-chairs24` (factors.rectangular_arrays) by `L4-vanroute` (measurement.compound_units); `L4-clockfive` (angles.clock_hands) by `L4-shuttlehours` (clock_reading.am_pm); `L4-flour` (fractions.arithmetic) by `L4-longestwalk` (fractions.compare_order); `L4-robotturns` (spatial.turns_facing) by `L4-badgerow` (repeating_pattern.cycle); `L4-schoolclubs` (sorting.overlap_both) by `L4-secretspread` (growing_pattern.doubling); `L4-sevens` (number_properties.multiples_count) by `L4-dronefly` (sequence.alternating_steps); `L4-theatrerows` (series_sum.add_in_pairs) by `L4-concerttickets` (counting_range.count_numbers); `L4-threedigitsum` (digit_cards.max_sum) by `L4-muralwall` (perimeter_area.area_rectangle); `L4-tilefigures` (figure_rule.nth_figure) by `L4-quiltpatches` (arrays.checkerboard); `L4-vertices` (shapes.solid_parts) by `L4-brushoffer` (money.offers)
- Level 4, rewritten with the same sub-structure (2): `L4-digitvalue83517` as `L4-seedshop`; `L4-heightline`; reworded only: `L4-visitortable`
- Level 5, replaced by a puzzle on another sub-structure (13): `L5-ballholder` (logic_truth.truth_tellers) by `L5-buoyhalf` (number_line.halfway); `L5-cardsmax5` (digit_cards.max_sum) by `L5-relaylegs` (durations.minutes_seconds); `L5-colourdraw` (strategy.worst_case) by `L5-badgeshops` (money.offers); `L5-cornerscard` (triangle_area.cut_corners) by `L5-scaleround` (rounding.count_that_round); `L5-floortiles5` (arrays.border_tiles) by `L5-shapelines` (symmetry.lines_total); `L5-fourthwednesday` (calendar.nth_weekday_date) by `L5-typeset` (place_value.digits_written); `L5-prismpyramid` (shapes.solid_parts) by `L5-hikeheight` (moves.ups_and_downs); `L5-robotfive` (spatial.turns_facing) by `L5-bakeryprices` (symbols.symbol_equations); `L5-schooltwo` (sorting.overlap_both) by `L5-busroutes5` (counting_pairs.handshakes); `L5-scrollfold` (paper_folding.fold_and_cut) by `L5-gategrid` (growing_pattern.stick_grid); `L5-sevendigit` (place_value.build_number) by `L5-shiptrip` (spatial.net_displacement); `L5-tank` (volume.water_depth) by `L5-busline` (graphs.pie_sector); `L5-twelves` (number_properties.multiples_count) by `L5-fastwatch` (clock_reading.faulty_clock)
- Level 6, replaced by a puzzle on another sub-structure (5): `L6-codingclub` (sorting.overlap_both) by `L6-parkvisitors` (rounding.round_to_place); `L6-dice8` (probability.two_dice_sum) by `L6-sweettin` (probability.one_pick); `L6-keyclaims` (logic_truth.truth_tellers) by `L6-juiceleft` (decimals.add_subtract); `L6-tankdepth` (volume.water_depth) by `L6-ferrytrip24` (clock_reading.twenty_four_hour); `L6-waterbarrel` (volume.capacity_in_litres) by `L6-helmetsale` (percentage.add_or_take_off)
- Level 6, rewritten with the same sub-structure (3): `L6-gaussjar` as `L6-gamepay`; `L6-shelfbooks`; `L6-tintpaint`; reworded only: `L6-prawns`, `L6-hiddenpair`

Other wording fixes: L2-recyclegrid, L6-tintpaint (C5); L3-bakery 7 boxes of 36; L3-barpieces 2/3 = ?/12; L4-heightline 6 children; L6-shelfbooks 6 books.

## 4. Retired and new in `taxonomy.json`

* Retired (levels emptied, reason recorded): `strategy.worst_case`, `factors.rectangular_arrays`, `figure_rule.nth_figure`, `angles.clock_hands`, `probability.two_dice_sum`, `volume.water_depth`.
* New: `probability.one_pick` (Level 6). `number_properties.odd_even_rule` now Levels 2 to 6; `arrays.border_tiles` extended to Levels 1 to 6 (restores the Level 1 slack of 10).
* Seven new `retired_frames`: dice_total, clock_hands_angle, tank_litres_depth, equal_rows_ways, seat_rows_grow, card_corner_cut, colour_pigeonhole.

## 5. The 11 Low level-fit items

L1-counterbox, L1-circlekids, L1-whichsun and L1-tilewall (numbers kept within P1); L2-stripchain, L2-ladderrungs and L2-sevens (numbers within P2); L3-bakery (7 boxes of 36); L3-barpieces (2/3 = ?/12); L4-heightline (6 children); L6-shelfbooks (6 books).

## 6. Results of the full run

| Check | Result |
|---|---|
| `build_bank.py` | bank rebuilt; `--plan` wrote `YEAR_PLAN.md`, 0 violations |
| `verify_bank.py` full tree, run A and run B (PYTHONHASHSEED different) | month 11: 0 FAIL, 114 REVIEW; month 12: 0 FAIL, 100 REVIEW; structure 0 FAIL; capacity 0 FAIL. The three reports are byte-identical except the tree digest line (the working tree changed by 40 sentences between the two runs: other agents' files; same 6748 files) |
| `--selftest` | 112 cases pass |
| Brute checks | 0 problems: every puzzle has exactly one answer |
| `year_model.py` | independent year check: 0 problems (cap 3 feasible at Levels 3 to 6; cap 2 infeasible as before) |
| `test_flag_off.py` | pass; the committed signup and level pages equal the flag-off generator output and carry no teaser code; `website/dist` untouched |
| `test_check.js` | 143 checks pass |
| `test_site.py` (built in /dev/shm with the flag on) | 483 checks, 0 failed |
| Preview | `build_preview.py` re-run; the 8 screenshots refreshed |

Capacity (family-capped, per quarter against 92): L3 98 (slack 6), L4 97 (5), L5 94 (2), L6 99 (7); Levels 1 and 2: slack 10 and 26.

## 7. Open

1. **No second reader** for the 82 changed puzzles. Before release someone other than the author hand-solves 15 a level, the new items first.
2. Level 5 slack is 2 (94 against 92); Level 1 slack is exactly 10 and rests on the `arrays.border_tiles` extension.
3. Text-answer counts are below the 40 a year plan at all six levels (the verifier warns). Support exists; the puzzles are not written.
4. REVIEW dispositions are the author's own reading. Nine structure pairs sit at 5 shared runs, one short of a FAIL.
5. L1-westturns (facing and turning) overlaps in subject with extension Level 3 unit 8 (`extension/l3/src/u08.py`); different story and numbers, kept.
6. Accepted rather than changed: the weeks-and-dates items (L1-campdays, funrun), the enrichment items, L5-pumpjob and L6-hiddenpair.
7. Jan to Oct 2027 are not written.
8. The source-lock digest changes whenever any file in the working tree changes; compare reports without the digest line.
