# Structure report (taxonomy.json)

Sources searched (whole working tree, tracked or not): 3818 files, 69.9 MB, sha256 07be370cdf611f6bf2274ee2.  Files per root: deck 158, diag 12, docs 413, extension 255, hp 35, k2 3, levels 20, mascot 4, ops 4, outputs 27, p1 1, p2 24, p3 24, p4 24, p5 25, p6 35, portal 44, practice 235, print 6, rebuild 87, releases 1, review 1, school 364, split 1801, taster 2, term 40, tutor 130, website 42, worker 1.

Rules. Levels 3 to 6 (TEASER-STRICT): per level and calendar quarter at most 1 puzzle per sub-structure and 3 per family; the same sub-structure never within 30 days of itself across a quarter boundary; an answer of 10 or more appears once per level and a single digit at most 4 times. Levels 1 and 2 (L1L2-GAP60): the same sub-structure at least 60 days apart (circular, 365- and 366-day year), a family at most 3 times in any 60 days and never on consecutive days, an answer not repeated within 60 days and a single-digit answer at most 2 times in 60 days. All levels: no repeated frame, no two puzzles with most numbers or the same story in common; the sub-structures used by the fixed puzzles on the level pages (counting_choices.digit_cards_arrangements, fractions.fraction_of_remainder, multiples.common_multiple, remainders.two_conditions, sequence.count_on, sequence.which_term) are never used by the bank.

- Level 1 (gap rule, 60 days): 61 puzzles, 61 distinct sub-structures (none twice within the gap), 39 families, most in one family 3
- Level 2 (gap rule, 60 days): 61 puzzles, 61 distinct sub-structures (none twice within the gap), 42 families, most in one family 3
- Level 3, quarter 4: 61 puzzles, 61 distinct sub-structures, 45 families, most in one family 3
- Level 4, quarter 4: 61 puzzles, 61 distinct sub-structures, 40 families, most in one family 3
- Level 5, quarter 4: 61 puzzles, 61 distinct sub-structures, 43 families, most in one family 3
- Level 6, quarter 4: 61 puzzles, 61 distinct sub-structures, 36 families, most in one family 3

## Capacity of the taxonomy (true numbers, after merging look-alike sub-structures)

Levels 1 and 2 (gap rule): a sub-structure may be used floor(365 / gap) times a year, so 365 puzzles need ceil(365 / uses) sub-structures; the owner-chosen minimum slack is 10 (a removed or retired sub-structure must not break a year). A family may supply at most 3 puzzles in any 60 days, so the families must also be wide enough: sum over families of min(subs, cap) per 60 days must reach the number of days.
Levels 3 to 6 (quarter rule): one use per sub-structure and at most 3 per family per quarter, so a quarter of up to 92 days needs sum over families of min(3, subs in the family) >= 92.

| Level | Sub-structures | Families | Rule | Uses per sub a year | Needed | Slack | True capacity (family-capped) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | 73 | 41 | gap 60 days | 6 | 61 | 12 | 420 a year | ok |
| 2 | 99 | 52 | gap 60 days | 6 | 61 | 38 | 558 a year | ok |
| 3 | 130 | 58 | once a quarter | 1 per quarter | 92 | 24 | 116 per quarter | ok |
| 4 | 132 | 63 | once a quarter | 1 per quarter | 92 | 27 | 119 per quarter | ok |
| 5 | 124 | 60 | once a quarter | 1 per quarter | 92 | 24 | 116 per quarter | ok |
| 6 | 112 | 57 | once a quarter | 1 per quarter | 92 | 15 | 107 per quarter | ok |

## Full-year answer rule at Levels 3 to 6 (feasibility)

| Level | Puzzles so far | Single-digit answers so far | Share | Projected single-digit answers in 365 | Allowed (9 values x 4) | Verdict |
|---|---|---|---|---|---|---|
| 3 | 61 | 6 | 10% | 36 | 36 | ok |
| 4 | 61 | 6 | 10% | 36 | 36 | ok |
| 5 | 61 | 2 | 3% | 12 | 36 | ok |
| 6 | 61 | 4 | 7% | 24 | 36 | ok |

Structure FAIL count (all released months): 0

Capacity verdict for the full year (a plan for January to October, not a defect of the released months): 0 CAPACITY FAIL

Skeleton matches with our own sources that were reviewed by hand (same masked wording, but no shared numbers): 0
