# Level 1 extension units 5 and 6: type map to the holiday program

Written 23 Oct 2026. Holiday source: `hp/lessons.js` lessons 5 (Mystery Number, working backwards) and 6 (Coin Combos, money), `hp/qbank.json`. Original examples reused from `docs/books/p1_non_routine_catalogue.md` types BACK, GC, CMP only as types, not as texts. Money wording per `docs/books/p1_school_paper_patterns.md` (50¢ style, $1 = 100¢ only as a conversion).

## Unit 5, Back to the start (holiday lesson 5)
| Item | Holiday type mirrored | What is new |
|---|---|---|
| S01, S03, S04, L01 | one-step "I think of a number" (add / take away) | cup, biscuits, arrow boxes; no "I think of a number" wording |
| S02 | four secret numbers | new numbers, add and take away mixed |
| S05, S06, S09, C02 | two-step stories, undo in reverse order | pencils, lift, arrow chain with two empty boxes |
| S07, T02, C03 | number machine IN / OUT, rule, one-step machine | table with empty cells; two-step machine collapsed to one step |
| S08, C01, C04 | undo as a missing-number sentence | includes 18 - [ ] = 11 |
| S10, S11, T03 | queue problems (counted twice) | 2 behind, behind from front place, 7th from front and 4th from back |
| S12 | more / fewer stories | both directions in one item |
| S13, S14 | check going forwards, true / false | a wrong-number test |
| T01 | three-step story | scaffolded parts a to c |
| G01 (beyond: Undoing a double) | none (new) | add a number to itself, then undo; original |
| G02 | order of steps | with a case where the order cannot be swapped (5 - 9) |
| G03 | snail climbing a wall | frog in a well, 12 steps, solved by working backwards from the top |

## Unit 6, Pay the exact amount (holiday lesson 6)
| Item | Holiday type mirrored | What is new |
|---|---|---|
| S01, S02, C01 | count coins; notes | picture rows, $19 from notes |
| S03 | exchange coins | $1 as 100¢ |
| S04, S05, C02 | pay exactly with 2 or 3 coins | riddle "Two of me make 40¢" |
| S06, S07, S09, C03 | totals, change, how much more | shop tags figure; no decimals |
| S08, T03 | which toys for an exact amount | one answer ($12) and two answers ($15) |
| S10 | compare sets | purses A and B |
| S11 | all ways with two coin kinds (table) | 40¢ with 20¢ and 10¢ |
| S12 | true / false on coin sums | $1 = ten 10¢ coins |
| S13 | fewest coins | 40¢ and 90¢ |
| S14 | choose coins from a row | circle the coins for 65¢ |
| T01 | exactly 4 coins, find every set | 65¢, 2 sets |
| T02 | two coin kinds and a total | 7 coins, 50¢ (guess and check table) |
| G01 (beyond: Sharing money equally) | none (new) | equal sharing, and a "cannot share 50¢ with 20¢ and 10¢" case |
| G02 | dollar notes, change | working back from change to the price of one item |
| G03 | fewest notes and coins | $38 |
| C04 | none | $1 against 85¢ (conversion) |

Checks: every answer is recomputed in `extension/verify/l1_u05_checks.py` and `l1_u06_checks.py` by forward simulation or by enumeration of all coin multisets (never by undoing the steps).
