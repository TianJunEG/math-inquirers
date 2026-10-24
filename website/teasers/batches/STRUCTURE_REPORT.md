# Structure report (taxonomy.json)

Sources searched (whole working tree, tracked or not): 6667 files, 1357.8 MB, sha256 59eff2d11509a27b04095132.  Files per root: deck 158, diag 12, docs 416, extension 257, hp 41, k2 5, levels 20, mascot 4, ops 14, outputs 180, p1 1, p2 27, p3 27, p4 27, p5 28, p6 38, portal 45, practice 292, print 6, rebuild 87, releases 1, review 1, school 474, split 1801, taster 2, term 2530, tutor 130, website 42, worker 1.

Rules. Levels 3 to 6 (TEASER-STRICT): per level and calendar quarter at most 1 puzzle per sub-structure and 3 per family; the same sub-structure never within 30 days of itself across a quarter boundary; an answer of 10 or more appears once per level and a single digit at most 4 times. Levels 1 and 2 (L1L2-GAP60): the same sub-structure at least 60 days apart (circular, 365- and 366-day year), a family at most 3 times in any 60 days and never on consecutive days, an answer not repeated within 60 days and a single-digit answer at most 2 times in 60 days. All levels: no repeated frame, no two puzzles with most numbers or the same story in common; the sub-structures used by the fixed puzzles on the level pages (counting_choices.digit_cards_arrangements, fractions.fraction_of_remainder, multiples.common_multiple, remainders.two_conditions, sequence.count_on, sequence.which_term) are never used by the bank.

- Level 1 (gap rule, 60 days): 61 puzzles, 61 distinct sub-structures (none twice within the gap), 39 families, most in one family 3
- Level 2 (gap rule, 60 days): 61 puzzles, 61 distinct sub-structures (none twice within the gap), 43 families, most in one family 3
- Level 3, quarter 4: 61 puzzles, 61 distinct sub-structures, 43 families, most in one family 3
- Level 4, quarter 4: 61 puzzles, 61 distinct sub-structures, 41 families, most in one family 3
- Level 5, quarter 4: 61 puzzles, 61 distinct sub-structures, 42 families, most in one family 3
- Level 6, quarter 4: 61 puzzles, 61 distinct sub-structures, 34 families, most in one family 3

## Capacity of the taxonomy (true numbers, after merging look-alike sub-structures)

Levels 1 and 2 (gap rule): a sub-structure may be used floor(365 / gap) times a year, so 365 puzzles need ceil(365 / uses) sub-structures; the owner-chosen minimum slack is 10 (a removed or retired sub-structure must not break a year). A family may supply at most 3 puzzles in any 60 days, so the families must also be wide enough: sum over families of min(subs, cap) per 60 days must reach the number of days.
Levels 3 to 6 (quarter rule): one use per sub-structure and at most 3 per family per quarter, so a quarter of up to 92 days needs sum over families of min(3, subs in the family) >= 92.

| Level | Sub-structures | Families | Rule | Uses per sub a year | Needed | Slack | True capacity (family-capped) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | 71 | 41 | gap 60 days | 6 | 61 | 10 | 414 a year | ok |
| 2 | 93 | 48 | gap 60 days | 6 | 61 | 32 | 528 a year | ok |
| 3 | 115 | 51 | once a quarter | 1 per quarter | 92 | 13 | 105 per quarter | ok |
| 4 | 115 | 56 | once a quarter | 1 per quarter | 92 | 14 | 106 per quarter | ok |
| 5 | 107 | 53 | once a quarter | 1 per quarter | 92 | 7 | 99 per quarter | ok |
| 6 | 100 | 52 | once a quarter | 1 per quarter | 92 | 3 | 95 per quarter | ok |

## Retired sub-structures (the frame is in our own books, so no level may use it)

- `calendar.weekday_after`: round 3: "which day of the week N days later" is in our books at Levels 1, 3, 4, 5 and 6 (Skill Additions sheets, term l1, holiday P3 week 5, extension l6_u08)
- `clock_reading.mirror_time`: round 3: "looks at a wall clock in a mirror" is in docs/sasmo/g1_original_problems_draft.md 4.3
- `coins.amounts_made`: round 4: "he picks some coins: how many different totals" is extension l4 u10 S02 and docs/audit/gifted_p1.md
- `coins.make_amount`: round 3: the frame "pay exactly N cents with 5-, 10- and 20-cent coins: how many different sets" is in our own books (docs/audit mkgifted_p3.py and holiday P6 week 5); the fewest-coins version was retired earlier for the same reason
- `containers.jug_pouring`: round 3: the jug puzzle (a 4 L jug and a 9 L jug with no marks) is in our P2 lesson 9 (split/p2l9)
- `counting_grid.diagonal_squares`: round 4: w + h - gcd is not in the MOE syllabus (the P4 factors cite did not support it)
- `counting_grid.rectangles_in_grid`: round 4: all the rectangles of a grid is the same frame as the squares in a grid (split/l7, split/p2l8, term l36, extension L3 workbook)
- `counting_grid.squares_in_grid`: round 4: all the squares of a grid is in tutor/data/p1l7.notes.json (3 by 3 = 14), split/l7, split/p2l8 and the extension L3 workbook; AUDIT_ROUND4 High
- `counting_grid.triangles_in_fan`: round 4: triangles in a fan of lines from one corner is in the P1 Student Workbook (Go further C1: 3 triangles, 6, 10; how many with 4 lines), split/l7 and holiday P5; AUDIT_ROUND4 High
- `counting_line.posts_loop`: round 3: posts and gaps on a path or round a pond is in the Skill Additions sheets (L2-POST1, L2-POST2, rebuild/skill_items_l1_3.py)
- `counting_ways.stairs_steps`: round 4: climbing 1 or 2 steps is in the P5 workbook (Ali climbs a staircase) and the L6 extension; one strip story ran at four levels
- `cubes.dice_faces`: round 3: three dice in a tower with opposite faces adding to 7 is in levels/gap_items.py (the Level 2 gap items)
- `cubes.painted`: round 4: a painted cube cut into small cubes is in split/p5l4, extension l5_u05 (L5U05-T01) and the L2 and L5 extension workbooks
- `digit_puzzles.palindromes`: round 4: palindromes in a range are in the P4 and P5 Question Banks ("5-digit palindromes between 40 000 and 50 000")
- `digit_puzzles.sum_of_all_digits`: same structure as extension l5_u01 (add all the digits written from 1 to 999); replaced by new structures
- `function_machine.find_the_rule`: round 3: IN and OUT machine with a hidden rule is in the P2 tutor guide, the P6 Algebra Machines lesson and the SASMO drafts
- `growing_pattern.growing_gaps`: round 3: same frame as holiday P1 lesson 1 (the gaps are 1, 2, 3, 4 ...)
- `growing_pattern.stick_row`: same structure as catalogue EX-PAT-1; replaced by new structures
- `measurement.container_and_contents`: round 4: "a jug full of water weighs 1.45 kg, half full 0.85 kg: mass of the empty jug" is Go further 7 of the P4 holiday week 5 lesson (practice/holiday/p4/05/lesson.py); the jar and rice and the juice bottle were the same frame
- `modular.last_digit_power`: round 3: "multiply 7 by itself 45 times: last digit" is in docs/sasmo/g6_original_problems_draft.md 2.2
- `moves.climb_and_slip`: same structure and story as our own hp question bank G5 and extension l1_u05; replaced by new structures
- `networks.draw_without_lifting`: round 4: odd-vertex parity at ages 8 to 12 is not in the MOE syllabus (the P2 Geometry cite did not support it)
- `number_arrangement.triangle_sides`: round 3: the verifier found the same story as docs/sasmo/g3_original_problems_draft.md (numbers on the sides of a triangle with equal side sums); kept as a tested kind but not used
- `number_grid.number_pyramid`: round 3: same frame as extension l3_u02 (pyramids with a hidden number)
- `polygons.turtle_repeat`: round 3: "walk a square: forward, turn on the spot, until back at the start" is in p6/content/l7.js
- `polyominoes.count_shapes`: round 4: "4 squares joined edge to edge: 5 different shapes" is stated in the P4 Question Bank, P4 workbook and split/l7 key; AUDIT_ROUND4 High
- `rate.fill_with_leak`: round 3: tap and leak is in extension l5_u05
- `shapes.cube_net_opposite`: round 4: "a net of six squares marked A to F: which letter is opposite" is item 2 of the P4 holiday week 4 lesson 8 (practice/holiday/p4/08), and split/p5l4; a text net is also hard for ages 9 to 12
- `sorting.three_sets`: round 4: three-set inclusion-exclusion is not in the MOE syllabus (only "Problem solving" was cited)
- `stacks.layers_of_cubes`: round 4: layers of 1, 4, 9 ... cubes is in rebuild/skill_items_l1_3.py and the L2 Skill Additions sheet, and one story ran at three levels

Usable sub-structures of round 3 that no released puzzle uses yet (each has a solver, an independent checker, a sample and a citation; their stories are checked when a month uses them): 0.

## Full-year answer rule at Levels 3 to 6 (feasibility)

| Level | Puzzles so far | Single-digit answers so far | Share | Projected single-digit answers in 365 | Allowed (9 values x 4) | Verdict |
|---|---|---|---|---|---|---|
| 3 | 61 | 6 | 10% | 36 | 36 | ok |
| 4 | 61 | 6 | 10% | 36 | 36 | ok |
| 5 | 61 | 3 | 5% | 18 | 36 | ok |
| 6 | 61 | 4 | 7% | 24 | 36 | ok |

Structure FAIL count (all released months): 4
- FAIL L1-rulerbill (L1) and L4-wheelcount (L4): same answer 29 and shared numbers ['3', '4'] at two levels
- FAIL L2-tilebed (L2) and L5-floortiles5 (L5): the same story skeleton at two levels (shared words paint,row,tile,touch)
- FAIL L3-bandmatch (L3) and L6-sixclubs (L6): the same story skeleton at two levels (shared words drum,guitar,instrument,piano,play,violin)
- FAIL L4-clockfive (L4) and L5-clockangle (L5): the same story skeleton at two levels (shared words clock,hand,hour,minute,smaller)

Capacity verdict for the full year (a plan for January to October, not a defect of the released months): 0 CAPACITY FAIL

Skeleton matches with our own sources that were reviewed by hand (same masked wording, but no shared numbers): 0
