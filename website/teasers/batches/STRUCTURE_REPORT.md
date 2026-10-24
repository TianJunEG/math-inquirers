# Structure report (taxonomy.json)

Sources searched (whole working tree, tracked or not): 6604 files, 1353.9 MB, sha256 f5d485ff197171466d84f60e.  Files per root: deck 158, diag 12, docs 416, extension 257, hp 41, k2 5, levels 20, mascot 4, ops 14, outputs 174, p1 1, p2 27, p3 27, p4 27, p5 28, p6 38, portal 45, practice 235, print 6, rebuild 87, releases 1, review 1, school 474, split 1801, taster 2, term 2530, tutor 130, website 42, worker 1.

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
| 1 | 70 | 40 | gap 60 days | 6 | 61 | 9 | 408 a year | FAIL: slack 9 below 10 (needs 71 or more sub-structures) |
| 2 | 93 | 48 | gap 60 days | 6 | 61 | 32 | 528 a year | ok |
| 3 | 116 | 51 | once a quarter | 1 per quarter | 92 | 13 | 105 per quarter | ok |
| 4 | 117 | 56 | once a quarter | 1 per quarter | 92 | 15 | 107 per quarter | ok |
| 5 | 111 | 53 | once a quarter | 1 per quarter | 92 | 11 | 103 per quarter | ok |
| 6 | 102 | 52 | once a quarter | 1 per quarter | 92 | 5 | 97 per quarter | ok |

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
- `modular.last_digit_power`: round 3: "multiply 7 by itself 45 times: last digit" is in docs/sasmo/g6_original_problems_draft.md 2.2
- `moves.climb_and_slip`: same structure and story as our own hp question bank G5 and extension l1_u05; replaced by new structures
- `networks.draw_without_lifting`: round 4: odd-vertex parity at ages 8 to 12 is not in the MOE syllabus (the P2 Geometry cite did not support it)
- `number_arrangement.triangle_sides`: round 3: the verifier found the same story as docs/sasmo/g3_original_problems_draft.md (numbers on the sides of a triangle with equal side sums); kept as a tested kind but not used
- `number_grid.number_pyramid`: round 3: same frame as extension l3_u02 (pyramids with a hidden number)
- `polygons.turtle_repeat`: round 3: "walk a square: forward, turn on the spot, until back at the start" is in p6/content/l7.js
- `polyominoes.count_shapes`: round 4: "4 squares joined edge to edge: 5 different shapes" is stated in the P4 Question Bank, P4 workbook and split/l7 key; AUDIT_ROUND4 High
- `rate.fill_with_leak`: round 3: tap and leak is in extension l5_u05
- `sorting.three_sets`: round 4: three-set inclusion-exclusion is not in the MOE syllabus (only "Problem solving" was cited)
- `stacks.layers_of_cubes`: round 4: layers of 1, 4, 9 ... cubes is in rebuild/skill_items_l1_3.py and the L2 Skill Additions sheet, and one story ran at three levels

Usable sub-structures of round 3 that no released puzzle uses yet (each has a solver, an independent checker, a sample and a citation; their stories are checked when a month uses them): 0.

## Full-year answer rule at Levels 3 to 6 (feasibility)

| Level | Puzzles so far | Single-digit answers so far | Share | Projected single-digit answers in 365 | Allowed (9 values x 4) | Verdict |
|---|---|---|---|---|---|---|
| 3 | 61 | 5 | 8% | 30 | 36 | ok |
| 4 | 61 | 5 | 8% | 30 | 36 | ok |
| 5 | 61 | 3 | 5% | 18 | 36 | ok |
| 6 | 61 | 4 | 7% | 24 | 36 | ok |

Structure FAIL count (all released months): 67
- FAIL L1: answer 18 repeats within 60 days (L1-tilewall and L1-woodpecker)
- FAIL L1: answer 18 repeats within 60 days (L1-tilewall and L1-libraryday)
- FAIL L1: answer 18 repeats within 60 days (L1-woodpecker and L1-libraryday)
- FAIL L1: answer 27 repeats within 60 days (L1-matchhouse and L1-traysame)
- FAIL L1: answer 28 repeats within 60 days (L1-cardstrip and L1-whichsun)
- FAIL L2: sub-structure group:days_in_a_range returns after 26 days (minimum 60, 365-day year): L2-clubdays and L2-ticketnumbers
- FAIL L2: sub-structure group:division_with_remainder returns after 11 days (minimum 60, 365-day year): L2-thinknumber and L2-schoolbus
- FAIL L2: sub-structure group:division_with_remainder returns after 19 days (minimum 60, 365-day year): L2-thinknumber and L2-mooncakes
- FAIL L2: sub-structure group:division_with_remainder returns after 8 days (minimum 60, 365-day year): L2-schoolbus and L2-mooncakes
- FAIL L2: sub-structure group:days_in_a_range returns after 26 days (minimum 60, 366-day year): L2-clubdays and L2-ticketnumbers
- FAIL L2: sub-structure group:division_with_remainder returns after 11 days (minimum 60, 366-day year): L2-thinknumber and L2-schoolbus
- FAIL L2: sub-structure group:division_with_remainder returns after 19 days (minimum 60, 366-day year): L2-thinknumber and L2-mooncakes
- FAIL L2: sub-structure group:division_with_remainder returns after 8 days (minimum 60, 366-day year): L2-schoolbus and L2-mooncakes
- FAIL L3 quarter 4: sub-structure group:division_with_remainder used 2 times: L3-erasers, L3-fairtables
- FAIL L4 quarter 4: sub-structure group:division_with_remainder used 2 times: L4-eggtrays30, L4-nametags
- FAIL L5 quarter 4: sub-structure group:box_volume used 2 times: L5-fishtank, L5-cubes
- FAIL L5 quarter 4: sub-structure group:overlapping_sets used 2 times: L5-threeclubs, L5-schooltwo
- FAIL L5 quarter 4: sub-structure group:division_with_remainder used 2 times: L5-divquotient, L5-eggboxes
- FAIL L6 quarter 4: sub-structure group:trace_a_loop used 2 times: L6-nested, L6-program
- FAIL L6 quarter 4: sub-structure group:ratio_after_a_change used 2 times: L6-redblue, L6-stickerratio
- FAIL L1-matchhouse (L1) and L3-mapshort (L3): same answer 27 and shared numbers ['12', '13'] at two levels
- FAIL L1-marblegame (L1) and L2-sudoku4 (L2): same answer 4 and shared numbers ['3', '4'] at two levels
- FAIL L1-marblegame (L1) and L2-stickgame (L2): the same story skeleton at two levels (shared words pile,should,sure,win,winn)
- FAIL L1-drinksmachine (L1) and L2-ticketnotes (L2): the same story skeleton at two levels (shared words change,machine,paid,price)
- FAIL L1-sudoku3 (L1) and L2-sudoku4 (L2): the same story skeleton at two levels (shared words bottom,column,fill,goe,grid,must,once,row,top)
- FAIL L1-sudoku3 (L1) and L3-magic (L3): the same story skeleton at two levels (shared words bottom,column,fill,grid,must,row)
- FAIL L1-oddbig (L1) and L6-cubeedges (L6): same answer 3 and shared numbers ['8', '12'] at two levels
- FAIL L2-lunchsets (L2) and L3-mealset (L3): same answer 24 and shared numbers ['3', '4'] at two levels
- FAIL L2-fewestswaps (L2) and L6-sevencards (L6): the same story skeleton at two levels (shared words card,fewest,lie,may,order,row,swap)
- FAIL L2-deliveryrobot (L2) and L3-robot (L3): the same story skeleton at two levels (shared words bottom,down,grid,move,order,reach,robot,route,top)
- FAIL L2-deliveryrobot (L2) and L4-puddle (L4): the same story skeleton at two levels (shared words bottom,down,grid,move,order,robot,route,top)
- FAIL L2-deliveryrobot (L2) and L5-blockedroute (L5): the same story skeleton at two levels (shared words block,bottom,delivery,down,grid,move,order,robot,route,top)
- FAIL L2-deliveryrobot (L2) and L6-detour (L6): the same story skeleton at two levels (shared words block,bottom,down,grid,move,order,route,top)
- FAIL L2-scarf (L2) and L4-dollarshare (L4): same answer 19 and shared numbers ['47'] at two levels
- FAIL L2-sudoku4 (L2) and L3-magic (L3): the same story skeleton at two levels (shared words bottom,column,fill,grid,must,row)
- FAIL L2-hallfloor (L2) and L3-chessboard (L3): the same story skeleton at two levels (shared words along,column,dark,light,row,top)
- FAIL L2-busroutes (L2) and L3-mapshort (L3): the same story skeleton at two levels (shared words kilometre,library,park,road,school,shortest)
- FAIL L2-bookcase (L2) and L3-bakery (L3): same answer 58 and shared numbers ['5', '7', '9'] at two levels
- FAIL L2-foldcut (L2) and L6-foldsix (L6): the same story skeleton at two levels (shared words across,cut,fold,made,middle,open,paper,piece,separate,straight,strip)
- FAIL L2-clubmatch (L2) and L5-subjects (L5): the same story skeleton at two levels (shared words chess,choir,club,drama,nor)
- FAIL L2-tankwater (L2) and L6-tankdiff (L6): the same story skeleton at two levels (shared words hold,litre,tank,water)
- FAIL L2-notebooks (L2) and L4-notebooks (L4): same answer 15 and shared numbers ['5', '6'] at two levels
- FAIL L3-fracmiddle (L3) and L4-flour (L4): the same numbers ['3', '4', '5', '8'] at two levels
- FAIL L3-cardsorder (L3) and L6-sevencards (L6): the same story skeleton at two levels (shared words biggest,card,row,smallest)
- FAIL L3-robot (L3) and L4-puddle (L4): the same story skeleton at two levels (shared words bottom,down,grid,move,order,robot,route,step,top)
- FAIL L3-robot (L3) and L5-blockedroute (L5): the same story skeleton at two levels (shared words bottom,down,grid,move,order,robot,route,top)
- FAIL L3-robot (L3) and L6-detour (L6): the same story skeleton at two levels (shared words bottom,down,grid,move,order,route,top)
- FAIL L3-twentyfour (L3) and L4-concert (L4): the same story skeleton at two levels (shared words end,hour,like,minute,start)
- FAIL L3-grid33 (L3) and L4-rects33 (L4): the same story skeleton at two levels (shared words across,down,draw,grid)
- FAIL L3-mapshort (L3) and L5-routeplan (L5): the same story skeleton at two levels (shared words home,kilometre,park,pool,road,shortest)
- FAIL L3-pencildrawing (L3) and L6-cubeedges (L6): the same story skeleton at two levels (shared words dot,draw,few,join,lift,line,must,once,pencil,straight)
- FAIL L3-barpieces (L3) and L6-sixfactors (L6): same answer 12 and shared numbers ['3', '4'] at two levels
- FAIL L3-cubetower (L3) and L5-cubetower9 (L5): the same story skeleton at two levels (shared words layer,top,tower,wider)
- FAIL L4-puddle (L4) and L5-blockedroute (L5): the same story skeleton at two levels (shared words bottom,down,grid,move,order,robot,route,top)
- FAIL L4-rects33 (L4) and L5-rects43 (L5): the same story skeleton at two levels (shared words across,down,grid,includ)
- FAIL L4-calc (L4) and L5-bracketmult (L5): the same story skeleton at two levels (shared words calculator,follow,operation,order,should,type)
- FAIL L4-sunflower (L4) and L5-sunflowerfall (L5): the same story skeleton at two levels (shared words biggest,end,graph,growth,height,line)
- FAIL L4-giftbags (L4) and L5-ropes (L5): same answer 42 and shared numbers ['84', '126'] at two levels
- FAIL L4-floorstrip (L4) and L6-tiles13 (L6): the same story skeleton at two levels (shared words cover,order,strip,tile,unit)
- FAIL L4-sundaes (L4) and L5-rects43 (L5): same answer 60 and shared numbers ['3', '4'] at two levels
- FAIL L4-sundaes (L4) and L6-stickerratio (L6): same answer 60 and shared numbers ['3', '5'] at two levels
- FAIL L4-chesssquares (L4) and L5-rects43 (L5): the same story skeleton at two levels (shared words across,down,includ,size)
- FAIL L4-fakecoin (L4) and L5-fakecoin5 (L5): the same story skeleton at two levels (shared words balance,certain,fake,fewest,little,scale,side,weighing)
- FAIL L4-fakecoin (L4) and L6-coinbound (L6): the same story skeleton at two levels (shared words balance,certain,fake,heavier,little,scale,weighing)
- FAIL L5-fakecoin5 (L5) and L6-coinbound (L6): the same story skeleton at two levels (shared words bag,balance,certain,fake,hold,little,scale,weighing)
- FAIL L5-blockedroute (L5) and L6-detour (L6): the same story skeleton at two levels (shared words along,block,bottom,down,goe,grid,move,order,route,top)
- FAIL L5-committee (L5) and L6-podium10 (L6): the same story skeleton at two levels (shared words club,job,member,secretary,treasurer)

Capacity verdict for the full year (a plan for January to October, not a defect of the released months): 1 CAPACITY FAIL
- CAPACITY FAIL Level 1: 70 sub-structures, 61 needed for 365 days at gap 60, slack 9; families allow 408 puzzles a year

Skeleton matches with our own sources that were reviewed by hand (same masked wording, but no shared numbers): 0
