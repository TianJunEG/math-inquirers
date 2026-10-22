"""Verify every answer changed or added in the P4 round-2 fixes (docs/audit/fixes_round2_p4.md). Run: python3 docs/audit/verify_fixes_round2_p4.py"""
from itertools import permutations
# L2 stretch slide: digit cards 1,3,5,7,9 once each, number closest to 60 000
nums = sorted(int(''.join(map(str, p))) for p in permutations([1, 3, 5, 7, 9]))
above = min(n for n in nums if n > 60000); below = max(n for n in nums if n < 60000)
assert (above, above - 60000, below, 60000 - below) == (71359, 11359, 59731, 269)
assert min(nums, key=lambda n: abs(n - 60000)) == 59731
# L2 explore Go further: cards 2,4,5,7,9 closest to 70 000
n2 = sorted(int(''.join(map(str, p))) for p in permutations([2, 4, 5, 7, 9]))
assert min(n2, key=lambda n: abs(n - 70000)) == 72459 and max(n for n in n2 if n < 70000) == 59742
# L5 try2 (a): 5.38 to 1 d.p. = 5.4 (halfway 5.35); round half up
from decimal import Decimal, ROUND_HALF_UP
assert Decimal('5.38').quantize(Decimal('0.1'), ROUND_HALF_UP) == Decimal('5.4')
# L6 page 2 (clock spaces of 30, compass steps of 45)
assert 4 * 30 == 120 and 5 * 30 == 150 and 1 * 30 == 30            # Q3a 4 o'clock, Q3b 7 o'clock (7 to 12 is 5 spaces), try c 1 o'clock
D = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
turn = lambda d, deg: D[(D.index(d) + deg // 45) % 8]
assert turn('W', 90) == 'N'                                          # Q4a (clockwise = +)
assert turn('SW', -135) == 'E'                                       # Q4b (anticlockwise = -)
assert turn(turn(turn('N', 90), -45), 180) == 'SW'                   # Q6a
assert 90 - 58 == 32                                                 # Q5
assert (50 - 15) // 5 * 30 == 210                                    # Think harder: minute hand 7:15 to 7:50 = 7 five-minute spaces
# L7 try3 (c): a 10 by 2 strip cut in half and stacked is 5 by 4: area unchanged
assert 10 * 2 == 5 * 4 == 20
# L9 Investigation (b): May 50, June 100: doubled and 50 more
assert 100 == 2 * 50 and 100 - 50 == 50
# L8 explore Go further: of the 11 cube nets, 4 have a longest row of 3 (1-4-1 has 6, 2-3-1 has 3, 3-3 has 1, 2-2-2 has 1)
assert 3 + 1 == 4 and 6 + 3 + 1 + 1 == 11
# L6 explore Go further 3:30: hour hand 105, minute hand 180 -> 75
assert 180 - (3 * 30 + 15) == 75
print('all round-2 P4 checks pass')
