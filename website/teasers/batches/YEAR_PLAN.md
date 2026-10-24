# Year plan for Levels 1 and 2 (owner L1L2-GAP60)

Day k of the year, counted from 1 Nov (366 dates, 29 Feb included), uses the sub-structure of released day k mod 61.  366 = 6 x 61, so a sub-structure returns exactly 61 days later (60 days in an ordinary year, because 29 Feb is missing).  A new story and new numbers are written for every return; the answer of a puzzle must not equal any answer within 60 days (checked by verify_bank.py as the months are written).

## Level 1

Checked with the gap rules for a 365-day and a 366-day year: no violation.

| Released day | Date | Sub-structure | Later dates it returns on |
|---|---|---|---|
| 1 | 11-01 | counting_pairs.handshakes | 01-01, 03-02, 05-02, 07-02, 09-01 |
| 2 | 11-02 | counting_line.race_places | 01-02, 03-03, 05-03, 07-03, 09-02 |
| 3 | 11-03 | counting_range.days_in_common | 01-03, 03-04, 05-04, 07-04, 09-03 |
| 4 | 11-04 | digit_puzzles.digit_clues | 01-04, 03-05, 05-05, 07-05, 09-04 |
| 5 | 11-05 | counting_choices.combinations | 01-05, 03-06, 05-06, 07-06, 09-05 |
| 6 | 11-06 | graphs.most_least_gap | 01-06, 03-07, 05-07, 07-07, 09-06 |
| 7 | 11-07 | number_names.alphabetical | 01-07, 03-08, 05-08, 07-08, 09-07 |
| 8 | 11-08 | division.share | 01-08, 03-09, 05-09, 07-09, 09-08 |
| 9 | 11-09 | bonds.three_cards_total | 01-09, 03-10, 05-10, 07-10, 09-09 |
| 10 | 11-10 | arrays.checkerboard | 01-10, 03-11, 05-11, 07-11, 09-10 |
| 11 | 11-11 | digit_cards.make_number | 01-11, 03-12, 05-12, 07-12, 09-11 |
| 12 | 11-12 | graphs.table_total | 01-12, 03-13, 05-13, 07-13, 09-12 |
| 13 | 11-13 | bonds.part_whole | 01-13, 03-14, 05-14, 07-14, 09-13 |
| 14 | 11-14 | digit_puzzles.count_by_digit_rule | 01-14, 03-15, 05-15, 07-15, 09-14 |
| 15 | 11-15 | counting_line.position_from_back | 01-15, 03-16, 05-16, 07-16, 09-15 |
| 16 | 11-16 | calendar.weeks_and_days | 01-16, 03-17, 05-17, 07-17, 09-16 |
| 17 | 11-17 | number_line.equal_marks | 01-17, 03-18, 05-18, 07-18, 09-17 |
| 18 | 11-18 | clock_reading.minute_hand | 01-18, 03-19, 05-19, 07-19, 09-18 |
| 19 | 11-19 | sorting.order_by_digit_rule | 01-19, 03-20, 05-20, 07-20, 09-19 |
| 20 | 11-20 | graphs.pictograph_scale | 01-20, 03-21, 05-21, 07-21, 09-20 |
| 21 | 11-21 | bar_model.sum_difference | 01-21, 03-22, 05-22, 07-22, 09-21 |
| 22 | 11-22 | digit_display.segments | 01-22, 03-23, 05-23, 07-23, 09-22 |
| 23 | 11-23 | arrays.seat_number | 01-23, 03-24, 05-24, 07-24, 09-23 |
| 24 | 11-24 | counting_line.cuts_and_pieces | 01-24, 03-25, 05-25, 07-25, 09-24 |
| 25 | 11-25 | growing_pattern.doubling | 01-25, 03-26, 05-26, 07-26, 09-25 |
| 26 | 11-26 | arrays.border_tiles | 01-26, 03-27, 05-27, 07-27, 09-26 |
| 27 | 11-27 | bonds.pairs_to_total | 01-27, 03-28, 05-28, 07-28, 09-27 |
| 28 | 11-28 | clock_reading.am_pm | 01-28, 03-29, 05-29, 07-29, 09-28 |
| 29 | 11-29 | coins.cannot_pay | 01-29, 03-30, 05-30, 07-30, 09-29 |
| 30 | 11-30 | clock_reading.hours_on | 01-30, 03-31, 05-31, 07-31, 09-30 |
| 31 | 12-01 | money.shopping | 01-31, 04-01, 06-01, 08-01, 10-01 |
| 32 | 12-02 | place_value.digits_written | 02-01, 04-02, 06-02, 08-02, 10-02 |
| 33 | 12-03 | repeating_pattern.cycle | 02-02, 04-03, 06-03, 08-03, 10-03 |
| 34 | 12-04 | durations.hours_to_minutes | 02-03, 04-04, 06-04, 08-04, 10-04 |
| 35 | 12-05 | counting_pairs.dice_sum_ways | 02-04, 04-05, 06-05, 08-05, 10-05 |
| 36 | 12-06 | number_line.halfway | 02-05, 04-06, 06-06, 08-06, 10-06 |
| 37 | 12-07 | word_problems.compare_amounts | 02-06, 04-07, 06-07, 08-07, 10-07 |
| 38 | 12-08 | missing_number.equal_sides | 02-07, 04-08, 06-08, 08-08, 10-08 |
| 39 | 12-09 | number_grid.hundred_chart | 02-08, 04-09, 06-09, 08-09, 10-09 |
| 40 | 12-10 | money.offers | 02-09, 04-10, 06-10, 08-10, 10-10 |
| 41 | 12-11 | place_value.swap_digits | 02-10, 04-11, 06-11, 08-11, 10-11 |
| 42 | 12-12 | measurement.overlapping_chain | 02-11, 04-12, 06-12, 08-12, 10-12 |
| 43 | 12-13 | shapes.name_the_shape | 02-12, 04-13, 06-13, 08-13, 10-13 |
| 44 | 12-14 | logic_grid.latin_square | 02-13, 04-14, 06-14, 08-14, 10-14 |
| 45 | 12-15 | number_names.letters_in_words | 02-14, 04-15, 06-15, 08-15, 10-15 |
| 46 | 12-16 | sorting.odd_one_out | 02-15, 04-16, 06-16, 08-16, 10-16 |
| 47 | 12-17 | measurement.ruler_offset | 02-16, 04-17, 06-17, 08-17, 10-17 |
| 48 | 12-18 | spatial.circle_opposite | 02-17, 04-18, 06-18, 08-18, 10-18 |
| 49 | 12-19 | number_grid.grid_totals | 02-18, 04-19, 06-19, 08-19, 10-19 |
| 50 | 12-20 | missing_number.missing_digit | 02-19, 04-20, 06-20, 08-20, 10-20 |
| 51 | 12-21 | multiplication.two_kinds_total | 02-20, 04-21, 06-21, 08-21, 10-21 |
| 52 | 12-22 | place_value.build_number | 02-21, 04-22, 06-22, 08-22, 10-22 |
| 53 | 12-23 | symbols.symbol_equations | 02-22, 04-23, 06-23, 08-23, 10-23 |
| 54 | 12-24 | spatial.net_displacement | 02-23, 04-24, 06-24, 08-24, 10-24 |
| 55 | 12-25 | logic_match.match_people_things | 02-24, 04-25, 06-25, 08-25, 10-25 |
| 56 | 12-26 | number_properties.multiples_count | 02-25, 04-26, 06-26, 08-26, 10-26 |
| 57 | 12-27 | sorting.rule_count | 02-26, 04-27, 06-27, 08-27, 10-27 |
| 58 | 12-28 | spatial.turns_facing | 02-27, 04-28, 06-28, 08-28, 10-28 |
| 59 | 12-29 | moves.ups_and_downs | 02-28, 04-29, 06-29, 08-29, 10-29 |
| 60 | 12-30 | logic_order.rank | 02-29, 04-30, 06-30, 08-30, 10-30 |
| 61 | 12-31 | multiplication.groups | 03-01, 05-01, 07-01, 08-31, 10-31 |

## Level 2

Checked with the gap rules for a 365-day and a 366-day year: no violation.

| Released day | Date | Sub-structure | Later dates it returns on |
|---|---|---|---|
| 1 | 11-01 | calendar.date_in_month | 01-01, 03-02, 05-02, 07-02, 09-01 |
| 2 | 11-02 | counting_range.days_in_common | 01-02, 03-03, 05-03, 07-03, 09-02 |
| 3 | 11-03 | counting_choices.combinations | 01-03, 03-04, 05-04, 07-04, 09-03 |
| 4 | 11-04 | symbols.symbol_equations | 01-04, 03-05, 05-05, 07-05, 09-04 |
| 5 | 11-05 | place_value.swap_digits | 01-05, 03-06, 05-06, 07-06, 09-05 |
| 6 | 11-06 | digit_puzzles.digit_clues | 01-06, 03-07, 05-07, 07-07, 09-06 |
| 7 | 11-07 | arrays.border_tiles | 01-07, 03-08, 05-08, 07-08, 09-07 |
| 8 | 11-08 | graphs.pictograph_scale | 01-08, 03-09, 05-09, 07-09, 09-08 |
| 9 | 11-09 | bonds.part_whole | 01-09, 03-10, 05-10, 07-10, 09-09 |
| 10 | 11-10 | division.reverse_division | 01-10, 03-11, 05-11, 07-11, 09-10 |
| 11 | 11-11 | fractions.parts_left | 01-11, 03-12, 05-12, 07-12, 09-11 |
| 12 | 11-12 | arrays.seat_number | 01-12, 03-13, 05-13, 07-13, 09-12 |
| 13 | 11-13 | sorting.fewest_swaps | 01-13, 03-14, 05-14, 07-14, 09-13 |
| 14 | 11-14 | bonds.three_cards_total | 01-14, 03-15, 05-15, 07-15, 09-14 |
| 15 | 11-15 | bar_model.three_amounts | 01-15, 03-16, 05-16, 07-16, 09-15 |
| 16 | 11-16 | coins.cannot_pay | 01-16, 03-17, 05-17, 07-17, 09-16 |
| 17 | 11-17 | counting_line.cuts_and_pieces | 01-17, 03-18, 05-18, 07-18, 09-17 |
| 18 | 11-18 | graphs.most_least_gap | 01-18, 03-19, 05-19, 07-19, 09-18 |
| 19 | 11-19 | durations.hours_to_minutes | 01-19, 03-20, 05-20, 07-20, 09-19 |
| 20 | 11-20 | counting_routes.grid_routes | 01-20, 03-21, 05-21, 07-21, 09-20 |
| 21 | 11-21 | multiplication.two_kinds_total | 01-21, 03-22, 05-22, 07-22, 09-21 |
| 22 | 11-22 | digit_cards.make_number | 01-22, 03-23, 05-23, 07-23, 09-22 |
| 23 | 11-23 | durations.elapsed | 01-23, 03-24, 05-24, 07-24, 09-23 |
| 24 | 11-24 | counting_line.race_places | 01-24, 03-25, 05-25, 07-25, 09-24 |
| 25 | 11-25 | number_properties.odd_even_rule | 01-25, 03-26, 05-26, 07-26, 09-25 |
| 26 | 11-26 | number_names.alphabetical | 01-26, 03-27, 05-27, 07-27, 09-26 |
| 27 | 11-27 | counting_pairs.handshakes | 01-27, 03-28, 05-28, 07-28, 09-27 |
| 28 | 11-28 | number_line.equal_marks | 01-28, 03-29, 05-29, 07-29, 09-28 |
| 29 | 11-29 | missing_number.missing_digit | 01-29, 03-30, 05-30, 07-30, 09-29 |
| 30 | 11-30 | clock_reading.am_pm | 01-30, 03-31, 05-31, 07-31, 09-30 |
| 31 | 12-01 | repeating_pattern.cycle | 01-31, 04-01, 06-01, 08-01, 10-01 |
| 32 | 12-02 | logic_grid.latin_square | 02-01, 04-02, 06-02, 08-02, 10-02 |
| 33 | 12-03 | place_value.build_number | 02-02, 04-03, 06-03, 08-03, 10-03 |
| 34 | 12-04 | measurement.unit_convert | 02-03, 04-04, 06-04, 08-04, 10-04 |
| 35 | 12-05 | growing_pattern.doubling | 02-04, 04-05, 06-05, 08-05, 10-05 |
| 36 | 12-06 | invariant.one_less | 02-05, 04-06, 06-06, 08-06, 10-06 |
| 37 | 12-07 | number_grid.grid_totals | 02-06, 04-07, 06-07, 08-07, 10-07 |
| 38 | 12-08 | measurement.overlapping_chain | 02-07, 04-08, 06-08, 08-08, 10-08 |
| 39 | 12-09 | shapes.name_the_shape | 02-08, 04-09, 06-09, 08-09, 10-09 |
| 40 | 12-10 | clock_reading.minute_hand | 02-09, 04-10, 06-10, 08-10, 10-10 |
| 41 | 12-11 | missing_number.equal_sides | 02-10, 04-11, 06-11, 08-11, 10-11 |
| 42 | 12-12 | networks.shortest_route | 02-11, 04-12, 06-12, 08-12, 10-12 |
| 43 | 12-13 | logic_order.rank | 02-12, 04-13, 06-13, 08-13, 10-13 |
| 44 | 12-14 | series_sum.add_in_pairs | 02-13, 04-14, 06-14, 08-14, 10-14 |
| 45 | 12-15 | measurement.compound_units | 02-14, 04-15, 06-15, 08-15, 10-15 |
| 46 | 12-16 | bar_model.sum_difference | 02-15, 04-16, 06-16, 08-16, 10-16 |
| 47 | 12-17 | guess_check.sum_product | 02-16, 04-17, 06-17, 08-17, 10-17 |
| 48 | 12-18 | strategy.take_away_game | 02-17, 04-18, 06-18, 08-18, 10-18 |
| 49 | 12-19 | multiplication.groups | 02-18, 04-19, 06-19, 08-19, 10-19 |
| 50 | 12-20 | money.shopping | 02-19, 04-20, 06-20, 08-20, 10-20 |
| 51 | 12-21 | shapes.solid_parts | 02-20, 04-21, 06-21, 08-21, 10-21 |
| 52 | 12-22 | paper_folding.fold_and_cut | 02-21, 04-22, 06-22, 08-22, 10-22 |
| 53 | 12-23 | number_properties.multiples_count | 02-22, 04-23, 06-23, 08-23, 10-23 |
| 54 | 12-24 | logic_match.match_people_things | 02-23, 04-24, 06-24, 08-24, 10-24 |
| 55 | 12-25 | moves.ups_and_downs | 02-24, 04-25, 06-25, 08-25, 10-25 |
| 56 | 12-26 | perimeter_area.perimeter_basic | 02-25, 04-26, 06-26, 08-26, 10-26 |
| 57 | 12-27 | word_problems.compare_amounts | 02-26, 04-27, 06-27, 08-27, 10-27 |
| 58 | 12-28 | fractions.unit_compare | 02-27, 04-28, 06-28, 08-28, 10-28 |
| 59 | 12-29 | money.offers | 02-28, 04-29, 06-29, 08-29, 10-29 |
| 60 | 12-30 | sorting.rule_count | 02-29, 04-30, 06-30, 08-30, 10-30 |
| 61 | 12-31 | spatial.net_displacement | 03-01, 05-01, 07-01, 08-31, 10-31 |

