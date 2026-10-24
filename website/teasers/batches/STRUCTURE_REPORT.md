# Structure report (taxonomy.json)

Rules: per level and calendar quarter at most 1 puzzle per sub-structure and 3 per family (kind); no answer repeats inside a level; the sub-structures used by the fixed puzzles on the level pages (counting_choices.digit_cards_arrangements, fractions.fraction_of_remainder, multiples.common_multiple, remainders.two_conditions, sequence.count_on, sequence.which_term) are never used by the bank.

- Level 1, quarter 4: 61 puzzles, 61 distinct sub-structures, 33 families, most in one family 3
- Level 2, quarter 4: 61 puzzles, 61 distinct sub-structures, 34 families, most in one family 3
- Level 3, quarter 4: 61 puzzles, 61 distinct sub-structures, 38 families, most in one family 3
- Level 4, quarter 4: 61 puzzles, 61 distinct sub-structures, 41 families, most in one family 3

Structure FAIL count (all released months): 4
- FAIL L4: answer 24 repeats (L4-giftbags, L4-evens4)
- FAIL L4: answer 13 repeats (L4-floorstrip, L4-noticeboard)
- FAIL L4: answer 17 repeats (L4-brickpyramid, L4-liftmin)
- FAIL L4: L4-liftmin and L4-shellpiles share the numbers ['3', '5', '8', '9']

Skeleton matches with our own sources that were reviewed by hand (same masked wording, but no shared numbers): 3
- REVIEW L1-equalbox [12-16]: skeleton 0.60 like ""q": "Fill in the missing number: 30 + 30 = 40 + ___", "answer": 20, "hint": "30 went up by 10 to 40. What hap ..." (term/l1/lessons/l08.json), shared numbers 0
- REVIEW L3-petshop [12-13]: skeleton 0.60 like "Ben does not choose juice or milk. Aisha does not choose tea. Kumar does not choose milk. Who chooses juice? ..." (extension/data/l5_u10.json), shared numbers 0
- REVIEW L4-yearlater [12-16]: skeleton 0.79 like "Answer: 14:30. Solution: Magic first gives 12:10 to 13:00 and then Puppet 13:15 to 14:30; Puppet first gives 1 ..." (docs/sasmo/g4_original_problems_draft.md), shared numbers 0
