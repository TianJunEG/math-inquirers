# Structure report (taxonomy.json)

Sources searched (whole working tree, tracked or not): 3818 files, 70.1 MB, sha256 4f118fdfe49b3d053939379a.  Files per root: deck 158, diag 12, docs 413, extension 255, hp 35, k2 3, levels 20, mascot 4, ops 4, outputs 27, p1 1, p2 24, p3 24, p4 24, p5 25, p6 35, portal 44, practice 235, print 6, rebuild 87, releases 1, review 1, school 364, split 1801, taster 2, term 40, tutor 130, website 42, worker 1.

Rules. Levels 3 to 6 (TEASER-STRICT): per level and calendar quarter at most 1 puzzle per sub-structure and 3 per family; the same sub-structure never within 30 days of itself across a quarter boundary; an answer of 10 or more appears once per level and a single digit at most 4 times. Levels 1 and 2 (L1L2-GAP60): the same sub-structure at least 60 days apart (circular, 365- and 366-day year), a family at most 3 times in any 60 days and never on consecutive days, an answer not repeated within 60 days and a single-digit answer at most 2 times in 60 days. All levels: no repeated frame, no two puzzles with most numbers or the same story in common; the sub-structures used by the fixed puzzles on the level pages (counting_choices.digit_cards_arrangements, fractions.fraction_of_remainder, multiples.common_multiple, remainders.two_conditions, sequence.count_on, sequence.which_term) are never used by the bank.

- Level 1 (gap rule, 60 days): 61 puzzles, 61 distinct sub-structures (none twice within the gap), 39 families, most in one family 3
- Level 2 (gap rule, 60 days): 61 puzzles, 61 distinct sub-structures (none twice within the gap), 42 families, most in one family 3
- Level 3, quarter 4: 61 puzzles, 61 distinct sub-structures, 46 families, most in one family 3
- Level 4, quarter 4: 61 puzzles, 61 distinct sub-structures, 40 families, most in one family 3
- Level 5, quarter 4: 61 puzzles, 61 distinct sub-structures, 42 families, most in one family 3
- Level 6, quarter 4: 61 puzzles, 61 distinct sub-structures, 36 families, most in one family 3

## Capacity of the taxonomy (true numbers, after merging look-alike sub-structures)

Levels 1 and 2 (gap rule): a sub-structure may be used floor(365 / gap) times a year, so 365 puzzles need ceil(365 / uses) sub-structures; the owner-chosen minimum slack is 10 (a removed or retired sub-structure must not break a year). A family may supply at most 3 puzzles in any 60 days, so the families must also be wide enough: sum over families of min(subs, cap) per 60 days must reach the number of days.
Levels 3 to 6 (quarter rule): one use per sub-structure and at most 3 per family per quarter, so a quarter of up to 92 days needs sum over families of min(3, subs in the family) >= 92.

| Level | Sub-structures | Families | Rule | Uses per sub a year | Needed | Slack | True capacity (family-capped) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | 73 | 41 | gap 60 days | 6 | 61 | 12 | 420 a year | ok |
| 2 | 97 | 51 | gap 60 days | 6 | 61 | 36 | 552 a year | ok |
| 3 | 126 | 56 | once a quarter | 1 per quarter | 92 | 22 | 114 per quarter | ok |
| 4 | 129 | 62 | once a quarter | 1 per quarter | 92 | 25 | 117 per quarter | ok |
| 5 | 121 | 58 | once a quarter | 1 per quarter | 92 | 21 | 113 per quarter | ok |
| 6 | 109 | 55 | once a quarter | 1 per quarter | 92 | 12 | 104 per quarter | ok |

## Retired sub-structures (the frame is in our own books, so no level may use it)

- `calendar.weekday_after`: round 3: "which day of the week N days later" is in our books at Levels 1, 3, 4, 5 and 6 (Skill Additions sheets, term l1, holiday P3 week 5, extension l6_u08)
- `clock_reading.mirror_time`: round 3: "looks at a wall clock in a mirror" is in docs/sasmo/g1_original_problems_draft.md 4.3
- `coins.make_amount`: round 3: the frame "pay exactly N cents with 5-, 10- and 20-cent coins: how many different sets" is in our own books (docs/audit mkgifted_p3.py and holiday P6 week 5); the fewest-coins version was retired earlier for the same reason
- `containers.jug_pouring`: round 3: the jug puzzle (a 4 L jug and a 9 L jug with no marks) is in our P2 lesson 9 (split/p2l9)
- `counting_line.posts_loop`: round 3: posts and gaps on a path or round a pond is in the Skill Additions sheets (L2-POST1, L2-POST2, rebuild/skill_items_l1_3.py)
- `cubes.dice_faces`: round 3: three dice in a tower with opposite faces adding to 7 is in levels/gap_items.py (the Level 2 gap items)
- `digit_puzzles.sum_of_all_digits`: same structure as extension l5_u01 (add all the digits written from 1 to 999); replaced by new structures
- `function_machine.find_the_rule`: round 3: IN and OUT machine with a hidden rule is in the P2 tutor guide, the P6 Algebra Machines lesson and the SASMO drafts
- `growing_pattern.growing_gaps`: round 3: same frame as holiday P1 lesson 1 (the gaps are 1, 2, 3, 4 ...)
- `growing_pattern.stick_row`: same structure as catalogue EX-PAT-1; replaced by new structures
- `modular.last_digit_power`: round 3: "multiply 7 by itself 45 times: last digit" is in docs/sasmo/g6_original_problems_draft.md 2.2
- `moves.climb_and_slip`: same structure and story as our own hp question bank G5 and extension l1_u05; replaced by new structures
- `number_arrangement.triangle_sides`: round 3: the verifier found the same story as docs/sasmo/g3_original_problems_draft.md (numbers on the sides of a triangle with equal side sums); kept as a tested kind but not used
- `number_grid.number_pyramid`: round 3: same frame as extension l3_u02 (pyramids with a hidden number)
- `polygons.turtle_repeat`: round 3: "walk a square: forward, turn on the spot, until back at the start" is in p6/content/l7.js
- `rate.fill_with_leak`: round 3: tap and leak is in extension l5_u05

Usable sub-structures of round 3 that no released puzzle uses yet (each has a solver, an independent checker, a sample and a citation; their stories are checked when a month uses them): 0.

## Full-year answer rule at Levels 3 to 6 (feasibility)

| Level | Puzzles so far | Single-digit answers so far | Share | Projected single-digit answers in 365 | Allowed (9 values x 4) | Verdict |
|---|---|---|---|---|---|---|
| 3 | 61 | 5 | 8% | 30 | 36 | ok |
| 4 | 61 | 5 | 8% | 30 | 36 | ok |
| 5 | 61 | 3 | 5% | 18 | 36 | ok |
| 6 | 61 | 4 | 7% | 24 | 36 | ok |

Structure FAIL count (all released months): 0

Capacity verdict for the full year (a plan for January to October, not a defect of the released months): 0 CAPACITY FAIL

Skeleton matches with our own sources that were reviewed by hand (same masked wording, but no shared numbers): 0
