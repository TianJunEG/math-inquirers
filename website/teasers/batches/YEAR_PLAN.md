# Year plan: the Level 1 and 2 rotation (owner L1L2-GAP60) and the answer budget for all levels (ANSWER-WINDOW)

Day k of the year, counted from 1 Nov (366 dates, 29 Feb included), uses the sub-structure of released day k mod 61.  366 = 6 x 61, so a sub-structure returns exactly 61 days later (60 days in an ordinary year, because 29 Feb is missing).  A new story and new numbers are written for every return; the answer of a puzzle must not equal any answer within 60 days (checked by verify_bank.py as the months are written).

## Level 1

Checked with the gap rules for a 365-day and a 366-day year: no violation.

| Released day | Date | Sub-structure | Later dates it returns on |
|---|---|---|---|
| 1 | 11-01 | digit_cards.make_number | 01-01, 03-02, 05-02, 07-02, 09-01 |
| 2 | 11-02 | counting_pairs.handshakes | 01-02, 03-03, 05-03, 07-03, 09-02 |
| 3 | 11-03 | clock_reading.minute_hand | 01-03, 03-04, 05-04, 07-04, 09-03 |
| 4 | 11-04 | coins.cannot_pay | 01-04, 03-05, 05-05, 07-05, 09-04 |
| 5 | 11-05 | bonds.part_whole | 01-05, 03-06, 05-06, 07-06, 09-05 |
| 6 | 11-06 | graphs.who_has_most | 01-06, 03-07, 05-07, 07-07, 09-06 |
| 7 | 11-07 | bonds.pairs_to_total | 01-07, 03-08, 05-08, 07-08, 09-07 |
| 8 | 11-08 | arrays.border_tiles | 01-08, 03-09, 05-09, 07-09, 09-08 |
| 9 | 11-09 | division.share | 01-09, 03-10, 05-10, 07-10, 09-09 |
| 10 | 11-10 | digit_puzzles.digit_clues | 01-10, 03-11, 05-11, 07-11, 09-10 |
| 11 | 11-11 | number_line.equal_marks | 01-11, 03-12, 05-12, 07-12, 09-11 |
| 12 | 11-12 | clock_reading.am_pm | 01-12, 03-13, 05-13, 07-13, 09-12 |
| 13 | 11-13 | graphs.pictograph_scale | 01-13, 03-14, 05-14, 07-14, 09-13 |
| 14 | 11-14 | digit_puzzles.count_by_digit_rule | 01-14, 03-15, 05-15, 07-15, 09-14 |
| 15 | 11-15 | digit_display.segments | 01-15, 03-16, 05-16, 07-16, 09-15 |
| 16 | 11-16 | growing_pattern.doubling | 01-16, 03-17, 05-17, 07-17, 09-16 |
| 17 | 11-17 | number_names.alphabetical | 01-17, 03-18, 05-18, 07-18, 09-17 |
| 18 | 11-18 | counting_line.cuts_and_pieces | 01-18, 03-19, 05-19, 07-19, 09-18 |
| 19 | 11-19 | arrays.checkerboard | 01-19, 03-20, 05-20, 07-20, 09-19 |
| 20 | 11-20 | counting_line.race_places | 01-20, 03-21, 05-21, 07-21, 09-20 |
| 21 | 11-21 | logic_order.rank | 01-21, 03-22, 05-22, 07-22, 09-21 |
| 22 | 11-22 | arrays.seat_number | 01-22, 03-23, 05-23, 07-23, 09-22 |
| 23 | 11-23 | counting_range.days_in_common | 01-23, 03-24, 05-24, 07-24, 09-23 |
| 24 | 11-24 | counting_line.position_from_back | 01-24, 03-25, 05-25, 07-25, 09-24 |
| 25 | 11-25 | bonds.three_cards_total | 01-25, 03-26, 05-26, 07-26, 09-25 |
| 26 | 11-26 | sorting.order_by_digit_rule | 01-26, 03-27, 05-27, 07-27, 09-26 |
| 27 | 11-27 | calendar.weeks_and_days | 01-27, 03-28, 05-28, 07-28, 09-27 |
| 28 | 11-28 | graphs.table_total | 01-28, 03-29, 05-29, 07-29, 09-28 |
| 29 | 11-29 | spatial.turns_facing | 01-29, 03-30, 05-30, 07-30, 09-29 |
| 30 | 11-30 | counting_choices.combinations | 01-30, 03-31, 05-31, 07-31, 09-30 |
| 31 | 12-01 | missing_number.missing_digit | 01-31, 04-01, 06-01, 08-01, 10-01 |
| 32 | 12-02 | place_value.digits_written | 02-01, 04-02, 06-02, 08-02, 10-02 |
| 33 | 12-03 | spatial.net_displacement | 02-02, 04-03, 06-03, 08-03, 10-03 |
| 34 | 12-04 | place_value.swap_digits | 02-03, 04-04, 06-04, 08-04, 10-04 |
| 35 | 12-05 | spatial.circle_opposite | 02-04, 04-05, 06-05, 08-05, 10-05 |
| 36 | 12-06 | shapes.name_the_shape | 02-05, 04-06, 06-06, 08-06, 10-06 |
| 37 | 12-07 | bar_model.sum_difference | 02-06, 04-07, 06-07, 08-07, 10-07 |
| 38 | 12-08 | number_names.letters_in_words | 02-07, 04-08, 06-08, 08-08, 10-08 |
| 39 | 12-09 | number_grid.grid_totals | 02-08, 04-09, 06-09, 08-09, 10-09 |
| 40 | 12-10 | multiplication.groups | 02-09, 04-10, 06-10, 08-10, 10-10 |
| 41 | 12-11 | measurement.ruler_offset | 02-10, 04-11, 06-11, 08-11, 10-11 |
| 42 | 12-12 | logic_match.match_people_things | 02-11, 04-12, 06-12, 08-12, 10-12 |
| 43 | 12-13 | multiplication.two_kinds_total | 02-12, 04-13, 06-13, 08-13, 10-13 |
| 44 | 12-14 | place_value.build_number | 02-13, 04-14, 06-14, 08-14, 10-14 |
| 45 | 12-15 | moves.ups_and_downs | 02-14, 04-15, 06-15, 08-15, 10-15 |
| 46 | 12-16 | symbols.symbol_equations | 02-15, 04-16, 06-16, 08-16, 10-16 |
| 47 | 12-17 | word_problems.compare_amounts | 02-16, 04-17, 06-17, 08-17, 10-17 |
| 48 | 12-18 | money.shopping | 02-17, 04-18, 06-18, 08-18, 10-18 |
| 49 | 12-19 | sorting.odd_one_out | 02-18, 04-19, 06-19, 08-19, 10-19 |
| 50 | 12-20 | repeating_pattern.cycle | 02-19, 04-20, 06-20, 08-20, 10-20 |
| 51 | 12-21 | number_line.halfway | 02-20, 04-21, 06-21, 08-21, 10-21 |
| 52 | 12-22 | logic_grid.latin_square | 02-21, 04-22, 06-22, 08-22, 10-22 |
| 53 | 12-23 | sorting.rule_count | 02-22, 04-23, 06-23, 08-23, 10-23 |
| 54 | 12-24 | number_properties.multiples_count | 02-23, 04-24, 06-24, 08-24, 10-24 |
| 55 | 12-25 | missing_number.equal_sides | 02-24, 04-25, 06-25, 08-25, 10-25 |
| 56 | 12-26 | word_problems.who_has_more | 02-25, 04-26, 06-26, 08-26, 10-26 |
| 57 | 12-27 | clock_reading.hours_on | 02-26, 04-27, 06-27, 08-27, 10-27 |
| 58 | 12-28 | number_grid.hundred_chart | 02-27, 04-28, 06-28, 08-28, 10-28 |
| 59 | 12-29 | measurement.overlapping_chain | 02-28, 04-29, 06-29, 08-29, 10-29 |
| 60 | 12-30 | money.offers | 02-29, 04-30, 06-30, 08-30, 10-30 |
| 61 | 12-31 | counting_pairs.dice_sum_ways | 03-01, 05-01, 07-01, 08-31, 10-31 |

## Level 2

Checked with the gap rules for a 365-day and a 366-day year: no violation.

| Released day | Date | Sub-structure | Later dates it returns on |
|---|---|---|---|
| 1 | 11-01 | digit_puzzles.digit_clues | 01-01, 03-02, 05-02, 07-02, 09-01 |
| 2 | 11-02 | durations.elapsed | 01-02, 03-03, 05-03, 07-03, 09-02 |
| 3 | 11-03 | bonds.part_whole | 01-03, 03-04, 05-04, 07-04, 09-03 |
| 4 | 11-04 | arrays.seat_number | 01-04, 03-05, 05-05, 07-05, 09-04 |
| 5 | 11-05 | fractions.parts_left | 01-05, 03-06, 05-06, 07-06, 09-05 |
| 6 | 11-06 | logic_order.rank | 01-06, 03-07, 05-07, 07-07, 09-06 |
| 7 | 11-07 | bar_model.three_amounts | 01-07, 03-08, 05-08, 07-08, 09-07 |
| 8 | 11-08 | number_properties.odd_even_rule | 01-08, 03-09, 05-09, 07-09, 09-08 |
| 9 | 11-09 | counting_routes.grid_routes | 01-09, 03-10, 05-10, 07-10, 09-09 |
| 10 | 11-10 | clock_reading.am_pm | 01-10, 03-11, 05-11, 07-11, 09-10 |
| 11 | 11-11 | arrays.border_tiles | 01-11, 03-12, 05-12, 07-12, 09-11 |
| 12 | 11-12 | number_line.equal_marks | 01-12, 03-13, 05-13, 07-13, 09-12 |
| 13 | 11-13 | bonds.three_cards_total | 01-13, 03-14, 05-14, 07-14, 09-13 |
| 14 | 11-14 | graphs.most_least_gap | 01-14, 03-15, 05-15, 07-15, 09-14 |
| 15 | 11-15 | multiplication.two_kinds_total | 01-15, 03-16, 05-16, 07-16, 09-15 |
| 16 | 11-16 | missing_number.missing_digit | 01-16, 03-17, 05-17, 07-17, 09-16 |
| 17 | 11-17 | fractions.unit_compare | 01-17, 03-18, 05-18, 07-18, 09-17 |
| 18 | 11-18 | sorting.fewest_swaps | 01-18, 03-19, 05-19, 07-19, 09-18 |
| 19 | 11-19 | counting_line.race_places | 01-19, 03-20, 05-20, 07-20, 09-19 |
| 20 | 11-20 | counting_pairs.handshakes | 01-20, 03-21, 05-21, 07-21, 09-20 |
| 21 | 11-21 | digit_cards.make_number | 01-21, 03-22, 05-22, 07-22, 09-21 |
| 22 | 11-22 | coins.cannot_pay | 01-22, 03-23, 05-23, 07-23, 09-22 |
| 23 | 11-23 | symbols.symbol_equations | 01-23, 03-24, 05-24, 07-24, 09-23 |
| 24 | 11-24 | number_names.alphabetical | 01-24, 03-25, 05-25, 07-25, 09-24 |
| 25 | 11-25 | networks.first_stop | 01-25, 03-26, 05-26, 07-26, 09-25 |
| 26 | 11-26 | graphs.pictograph_scale | 01-26, 03-27, 05-27, 07-27, 09-26 |
| 27 | 11-27 | division.reverse_division | 01-27, 03-28, 05-28, 07-28, 09-27 |
| 28 | 11-28 | place_value.swap_digits | 01-28, 03-29, 05-29, 07-29, 09-28 |
| 29 | 11-29 | counting_range.days_in_common | 01-29, 03-30, 05-30, 07-30, 09-29 |
| 30 | 11-30 | calendar.date_in_month | 01-30, 03-31, 05-31, 07-31, 09-30 |
| 31 | 12-01 | counting_line.cuts_and_pieces | 01-31, 04-01, 06-01, 08-01, 10-01 |
| 32 | 12-02 | series_sum.add_in_pairs | 02-01, 04-02, 06-02, 08-02, 10-02 |
| 33 | 12-03 | logic_grid.latin_square | 02-02, 04-03, 06-03, 08-03, 10-03 |
| 34 | 12-04 | clock_reading.minute_hand | 02-03, 04-04, 06-04, 08-04, 10-04 |
| 35 | 12-05 | measurement.overlapping_chain | 02-04, 04-05, 06-05, 08-05, 10-05 |
| 36 | 12-06 | graphs.who_has_most | 02-05, 04-06, 06-06, 08-06, 10-06 |
| 37 | 12-07 | bar_model.sum_difference | 02-06, 04-07, 06-07, 08-07, 10-07 |
| 38 | 12-08 | guess_check.sum_product | 02-07, 04-08, 06-08, 08-08, 10-08 |
| 39 | 12-09 | shapes.solid_parts | 02-08, 04-09, 06-09, 08-09, 10-09 |
| 40 | 12-10 | networks.shortest_route | 02-09, 04-10, 06-10, 08-10, 10-10 |
| 41 | 12-11 | moves.ups_and_downs | 02-10, 04-11, 06-11, 08-11, 10-11 |
| 42 | 12-12 | logic_match.match_people_things | 02-11, 04-12, 06-12, 08-12, 10-12 |
| 43 | 12-13 | growing_pattern.doubling | 02-12, 04-13, 06-13, 08-13, 10-13 |
| 44 | 12-14 | missing_number.equal_sides | 02-13, 04-14, 06-14, 08-14, 10-14 |
| 45 | 12-15 | measurement.unit_convert | 02-14, 04-15, 06-15, 08-15, 10-15 |
| 46 | 12-16 | shapes.name_the_shape | 02-15, 04-16, 06-16, 08-16, 10-16 |
| 47 | 12-17 | place_value.build_number | 02-16, 04-17, 06-17, 08-17, 10-17 |
| 48 | 12-18 | number_properties.multiples_count | 02-17, 04-18, 06-18, 08-18, 10-18 |
| 49 | 12-19 | strategy.take_away_game | 02-18, 04-19, 06-19, 08-19, 10-19 |
| 50 | 12-20 | repeating_pattern.cycle | 02-19, 04-20, 06-20, 08-20, 10-20 |
| 51 | 12-21 | spatial.net_displacement | 02-20, 04-21, 06-21, 08-21, 10-21 |
| 52 | 12-22 | money.cheaper_shop | 02-21, 04-22, 06-22, 08-22, 10-22 |
| 53 | 12-23 | paper_folding.fold_and_cut | 02-22, 04-23, 06-23, 08-23, 10-23 |
| 54 | 12-24 | money.offers | 02-23, 04-24, 06-24, 08-24, 10-24 |
| 55 | 12-25 | perimeter_area.perimeter_basic | 02-24, 04-25, 06-25, 08-25, 10-25 |
| 56 | 12-26 | money.shopping | 02-25, 04-26, 06-26, 08-26, 10-26 |
| 57 | 12-27 | word_problems.who_has_more | 02-26, 04-27, 06-27, 08-27, 10-27 |
| 58 | 12-28 | number_grid.grid_totals | 02-27, 04-28, 06-28, 08-28, 10-28 |
| 59 | 12-29 | durations.hours_to_minutes | 02-28, 04-29, 06-29, 08-29, 10-29 |
| 60 | 12-30 | word_problems.compare_amounts | 02-29, 04-30, 06-30, 08-30, 10-30 |
| 61 | 12-31 | invariant.one_less | 03-01, 05-01, 07-01, 08-31, 10-31 |

## Text answers per calendar month under the rotation (Levels 1 and 2)

A calendar month is a window of the released order, so the number of text-answer puzzles in each month of the year is fixed by the 61 released days. From January a month needs 3 text answers at Levels 1 and 2 (`text_min_per_month`); the table is the smallest and the largest count over a 365-day and a 366-day year.

| Level | Text answers in the 61 released days | Fewest in a month | Month | Most in a month | Verdict |
|---|---|---|---|---|---|
| 1 | 8 | 4 | 01 | 4 | ok |
| 2 | 9 | 4 | 01 | 5 | ok |


## Answer budget (ANSWER-WINDOW, replaces the full-year answer rule of rounds 3 to 5)

Levels 3 to 6: the same answer value never twice within 60 days (and never with the same sub-structure within 92 days). A 60-day window can hold at most 9 different single-digit answers and 90 different two-digit answers; every other answer (100 or more, a fraction, a decimal, a word) is limited only by the window. Levels 1 and 2: a single digit at most twice in 60 days (18), any other answer once.

| Level | Puzzles | Single digit | 10 to 99 | 100 or more | Fraction, decimal | Text | Peak single digits in 60 days (limit) | Peak 10 to 99 in 60 days (limit 90) |
|---|---|---|---|---|---|---|---|---|
| 1 | 61 | 10 | 43 | 0 | 0 | 8 | 10 (18) | 43 |
| 2 | 61 | 9 | 33 | 9 | 1 | 9 | 9 (18) | 33 |
| 3 | 61 | 6 | 29 | 18 | 4 | 4 | 6 (9) | 28 |
| 4 | 61 | 6 | 25 | 19 | 5 | 6 | 6 (9) | 25 |
| 5 | 61 | 2 | 30 | 20 | 5 | 4 | 2 (9) | 30 |
| 6 | 61 | 3 | 35 | 13 | 6 | 4 | 3 (9) | 35 |

## Text answers per level (TEXT_ANSWER_PLAN.md)

Target: about 3 or 4 text-answer puzzles a month at every level, so that a year holds 40 or more (every text answer is used once per level).

| Level | Puzzles so far | Text-answer puzzles | Per 30 days | Projected in 365 | Target | Verdict |
|---|---|---|---|---|---|---|
| 1 | 61 | 8 | 3.9 | 48 | 40 | ok |
| 2 | 61 | 9 | 4.4 | 54 | 40 | ok |
| 3 | 61 | 4 | 2.0 | 24 | 40 | WARNING: below the plan |
| 4 | 61 | 6 | 3.0 | 36 | 40 | WARNING: below the plan |
| 5 | 61 | 4 | 2.0 | 24 | 40 | WARNING: below the plan |
| 6 | 61 | 4 | 2.0 | 24 | 40 | WARNING: below the plan |

### What is left for January to October (305 puzzles a level)

ANSWER-WINDOW (owner delegate, adopted default, revocable: `docs/terms/owner_decisions.md`) replaces the rule "an answer of 10 or more once per level and year", which AUDIT_ROUND6 H2 showed to be unreachable at Levels 3 to 6 (29 to 31% of the remaining puzzles could be a whole number below 100). The new limits are per window of 60 days, so they renew all year:

| Level | Single-digit answers | Two-digit answers (10 to 99) | 100 or more, fraction, decimal, word | Same answer and same sub-structure |
|---|---|---|---|---|
| 1, 2 | at most 2 of each digit in 60 days (18 in all) | each value once in 60 days (90 values) | each value once in 60 days | not twice within 60 days (the sub-structure gap) |
| 3 to 6 | each digit once in 60 days (**9 in all, about 15% of the puzzles**) | each value once in 60 days (90 values: never the binding limit) | each value once in 60 days | never twice within 92 days, also across a quarter boundary |

Over the 305 puzzles still to write, a level may therefore hold at most 46 single-digit answers (Levels 3 to 6) or 92 (Levels 1 and 2). The released Nov and Dec bank uses 10 at Level 1, 9 at Level 2, 6 at Level 3, 6 at Level 4, 2 at Level 5, 3 at Level 6 in its 61 days. The two-digit values (90 a window) and everything from 100 up are never the binding limit; the window of 9 single digits is, so counting puzzles (handshakes, patterns, ways) must be scaled up. A text answer counts like any other value: the same word may not be the answer twice within 60 days at Levels 3 to 6, so a closed set of 4 words (the compass, odd or even) can supply at most 4 answers in a window of 60 days.

