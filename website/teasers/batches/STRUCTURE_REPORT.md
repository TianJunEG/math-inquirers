# Structure report (taxonomy.json)

Rules: per level and calendar quarter at most 1 puzzle per sub-structure and 3 per family (kind); no answer repeats inside a level; the sub-structures used by the fixed puzzles on the level pages (counting_choices.digit_cards_arrangements, fractions.fraction_of_remainder, multiples.common_multiple, remainders.two_conditions, sequence.count_on, sequence.which_term) are never used by the bank.

- Level 1, quarter 4: 61 puzzles, 61 distinct sub-structures, 33 families, most in one family 3
- Level 2, quarter 4: 61 puzzles, 61 distinct sub-structures, 34 families, most in one family 3
- Level 3, quarter 4: 61 puzzles, 61 distinct sub-structures, 38 families, most in one family 3
- Level 4, quarter 4: 61 puzzles, 61 distinct sub-structures, 41 families, most in one family 3
- Level 5, quarter 4: 61 puzzles, 61 distinct sub-structures, 41 families, most in one family 3
- Level 6, quarter 4: 61 puzzles, 61 distinct sub-structures, 33 families, most in one family 3

## Capacity of the taxonomy (full year)

A quarter has 90 to 92 days, and each sub-structure may be used once per level and quarter, so a level needs at least 92 sub-structures (and 31 families at 3 each) to fill a quarter, and the same sub-structures can be used again in the next quarter with a new story and new numbers.

| Level | Sub-structures offered | Families | Largest quarter it can fill | Needed (92) |
|---|---|---|---|---|
| 1 | 61 | 33 | 61 | short by 31 |
| 2 | 80 | 35 | 80 | short by 12 |
| 3 | 102 | 41 | 102 | enough |
| 4 | 108 | 44 | 108 | enough |
| 5 | 109 | 46 | 109 | enough |
| 6 | 105 | 50 | 105 | enough |

Structure FAIL count (all released months): 0

Skeleton matches with our own sources that were reviewed by hand (same masked wording, but no shared numbers): 2
- REVIEW L3-petshop [12-13]: skeleton 0.60 like "Ben does not choose juice or milk. Aisha does not choose tea. Kumar does not choose milk. Who chooses juice? ..." (extension/data/l5_u10.json), shared numbers 0
- REVIEW L4-yearlater [12-16]: skeleton 0.79 like "Example: "Between 20 and 50; ÷ 5 leaves 2; ÷ 6 leaves 4." Only 22 fits (22 = 4 × 5 + 2 = 3 × 6 + 4). With the  ..." (p3/content/l5.js), shared numbers 0
