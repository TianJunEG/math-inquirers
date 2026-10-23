"""Level 6 Unit 2: Prime hunters (factors, primes, prime factorisation, mod).  Follows holiday lesson 2."""
from lib import *

U = 'L6U02'
I = []

learn = {
    'intro': 'A factor divides a number exactly. Factors come in pairs, and a prime has exactly 2 factors: 1 and itself. '
             'In code, n mod d is the remainder, and a remainder of 0 means d is a factor.',
    'example': {
        'problem': 'Is 97 prime? Show your test.',
        'figure': grid([['d', '2', '3', '5', '7'], ['97 mod d', '1', '1', '2', '6']], [32, 18, 18, 18, 18], rowhead=True),
        'steps': ['A prime has only 2 factors. We look for any factor besides 1 and 97.',
                  'Test the primes 2, 3, 5 and 7. Stop at 7, because 11 × 11 = 121 is already more than 97.',
                  'Find the remainder 97 mod d for each. None of them is 0.',
                  'A program that counts the factors of 97 ends with count = 2.'],
        'answer': '97 is prime: it has no factor except 1 and 97.'},
    'howto': {'title': 'How to test whether n is prime',
              'steps': ['Try the primes 2, 3, 5, 7, ... in order.',
                        'Find n mod d. A remainder of 0 means d is a factor.',
                        'Stop when d × d is more than n.',
                        'No remainder was 0? Then n is prime.',
                        'Quick tests: an even last digit means 2 is a factor, digits adding to a multiple of 3 means 3 is a factor, and a last digit of 0 or 5 means 5 is a factor.',
                        'Factor tree: split a number into 2 factors again and again. The ends that cannot split are primes: 60 = 6 × 10 = 2 × 3 × 2 × 5.']},
    'try': IT(U, 'L', 1, 0, 'Is 143 prime?  {circ:Yes|No}   If not, 143 = {b} × {b}.',
              'Test 2, 3, 5 and 7: each leaves a remainder (143 mod 7 = 3). Then test 11, because 11 × 11 = 121 is less than 143: 11 × 13 = 143. '
              'So 143 is not prime.',
              answer=A(['No', 11, 13], 'No, 11 × 13')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'Factors come in pairs. Use pairs to find all the factors.',
            '42: 1 × 42, 2 × 21, 3 × 14, 6 × 7, so 8 factors. 100: 1 × 100, 2 × 50, 4 × 25, 5 × 20 and 10 × 10. '
            'The pairs give 8 factors and 10 pairs with itself, so 9 in all.',
            parts=[P('a', 'The factors of 42 are {ll}', [1, 2, 3, 6, 7, 14, 21, 42], '1, 2, 3, 6, 7, 14, 21, 42', list=True),
                   P('b', '100 has {b} factors.', [9]),
                   P('c', 'The factor of 100 that pairs with itself is {b}.', [10])]))
I.append(IT(U, 'S', 2, 1,
            'Circle every prime number in the table.',
            'Test each number. 51 = 3 × 17, 57 = 3 × 19, 63 = 7 × 9, 69 = 3 × 23 and 77 = 7 × 11 are not prime. '
            'The primes are 53, 59, 67, 73 and 79. They have no factor except 1 and themselves.',
            fig=grid([['51', '53', '57', '59', '63'], ['67', '69', '73', '77', '79']], [24, 24, 24, 24, 24], ch=11),
            answer=A([53, 59, 67, 73, 79], '53, 59, 67, 73, 79', list=True, unordered=True)))
I.append(IT(U, 'S', 3, 1,
            'Finish the factor tree of 84. Split each number until only primes are left.',
            '84 = 4 × 21, 4 = 2 × 2 and 21 = 3 × 7. The ends of the tree are 2, 2, 3 and 7, so 84 = 2 × 2 × 3 × 7. '
            '90 = 9 × 10 = 3 × 3 × 2 × 5, so 90 = 2 × 3 × 3 × 5.',
            fig={'type': 'l6_tree', 'tree': {'v': '84', 'kids': [{'v': '4', 'kids': [{'v': ''}, {'v': ''}]}, {'v': '21', 'kids': [{'v': ''}, {'v': ''}]}]}},
            parts=[P('a', '84 = {b} × {b} × {b} × {b}', [2, 2, 3, 7], '2 × 2 × 3 × 7'),
                   P('b', 'Write 90 as a product of primes: {ll}', [2, 3, 3, 5], '2 × 3 × 3 × 5', list=True)],
            figright=True))
I.append(IT(U, 'S', 4, 1,
            'This code counts the factors of n. Fill in the trace table.',
            'n mod d for d = 1 to 6: 0, 0, 2, 0, 0, 2, so the count goes 1, 2, 2, 3, 4, 4. The code says 4. But 20 has 6 factors: 1, 2, 4, 5, 10 and 20. '
            'The loop stops at d = 6 and misses 10 and 20. To count every factor, repeat 20 times.',
            fig=code([['var', 'set n to (20)'], ['var', 'set d to (1)'], ['var', 'set count to (0)'],
                      ['ctl', 'repeat (6)', [['ctl', 'if <(n) mod (d) = (0)> then', [['var', 'change count by (1)']]], ['var', 'change d by (1)']]],
                      ['look', 'say (count)']],
                     trace={'cols': ['d', 'n mod d', 'count'], 'rows': 6, 'first': [1, 2, 3, 4, 5, 6], 'cw': 19, 'ch': 8}),
            parts=[P('a', 'The code says {b}.', [4]),
                   P('b', 'To count all the factors of 20, change repeat 6 to repeat {b}.', [20])]))
I.append(IT(U, 'S', 5, 2,
            'Write 26 as a sum of 2 primes. The 2 primes may be the same. Find every way.',
            'Try each prime and see if 26 take away that prime is also prime: 26 − 3 = 23, 26 − 7 = 19 and 26 − 13 = 13 all work. '
            '26 − 2, 26 − 5, 26 − 11, 26 − 17 are 24, 21, 15 and 9, which are not prime. There are 3 ways.',
            fig=grid([['2', '3', '5', '7', '11', '13', '17', '19', '23', '29']], [13] * 10, ch=10),
            answer=A(['3 + 23', '7 + 19', '13 + 13'], '3 + 23, 7 + 19, 13 + 13', list=True, unordered=True),
            space={'rows': ['{ll}']}))
I.append(IT(U, 'S', 6, 2,
            'Use the divisibility tests. Circle Yes or No.',
            '(a) 372: the last 2 digits, 72, are in the 4 times table (72 = 4 × 18), so Yes. (b) 2457: the digits add to 2 + 4 + 5 + 7 = 18, a multiple of 3, so Yes. '
            '(c) 6835: the digits add to 22, which is not a multiple of 9, so No.',
            parts=[P('a', 'Is 372 a multiple of 4?   {circ:Yes|No}', ['Yes']),
                   P('b', 'Is 2457 a multiple of 3?   {circ:Yes|No}', ['Yes']),
                   P('c', 'Is 6835 a multiple of 9?   {circ:Yes|No}', ['No'])]))
I.append(IT(U, 'S', 7, 2,
            'Test whether 113 is prime. You only need to test 2, 3, 5 and 7.',
            '113 = 56 × 2 + 1, 113 = 37 × 3 + 2, 113 = 22 × 5 + 3 and 113 = 16 × 7 + 1. No remainder is 0, and the next prime 11 is too big (11 × 11 = 121), so 113 is prime. '
            '119 = 7 × 17, so 119 is not prime.',
            parts=[P('a', '113 mod 2 = {b}, mod 3 = {b}, mod 5 = {b}, mod 7 = {b}', [1, 2, 3, 1], '1, 2, 3, 1'),
                   P('b', 'Is 113 prime?   {circ:Yes|No}', ['Yes']),
                   P('c', 'Is 119 prime?   {circ:Yes|No}   If not, 119 = {b} × {b}.', ['No', 7, 17], 'No, 7 × 17')]))
I.append(IT(U, 'S', 8, 2,
            'Who am I? Each riddle has only one answer.',
            '(a) The primes between 40 and 60 are 41, 43, 47, 53 and 59. Only 53 has digits that add to 8. '
            '(b) The primes between 60 and 80 are 61, 67, 71, 73 and 79. Adding 2 gives 63, 69, 73, 75, 81, and only 73 is prime, so I am 71.',
            parts=[P('a', 'I am a prime number between 40 and 60. My digits add to 8. I am {b}.', [53]),
                   P('b', 'I am a prime number between 60 and 80. If you add 2 to me, you get another prime. I am {b}.', [71])]))
I.append(IT(U, 'S', 9, 3,
            'Most numbers have an even number of factors. Some do not.',
            '(a) 81: 1 × 81, 3 × 27 and 9 × 9 give 1, 3, 9, 27, 81. (b) 9 is paired with itself. '
            '(c) 64 = 8 × 8 is a square, so it has an odd number (7). 50 has 6 factors and 72 has 12.',
            parts=[P('a', '81 has {b} factors.', [5]),
                   P('b', 'The factor of 81 that pairs with itself is {b}.', [9]),
                   P('c', 'Which has an odd number of factors?   {circ:50|64|72}', ['64'])]))
I.append(IT(U, 'S', 10, 3,
            'Predict what this code says.',
            'x goes 7, 14, 21, 28, 35, 42, 49, 56, 63, 70. The code says x only when x mod 2 = 0, that is when x is even. '
            'It says 14, 28, 42, 56 and 70. The first is 14, there are 5 numbers, and the last is 70.',
            fig=code([['var', 'set x to (0)'], ['ctl', 'repeat (10)', [['var', 'change x by (7)'], ['ctl', 'if <(x) mod (2) = (0)> then', [['look', 'say (x) for (1) seconds']]]]]]),
            parts=[P('a', 'The first number it says is {b}.', [14]),
                   P('b', 'It says {b} numbers.', [5]),
                   P('c', 'The last number it says is {b}.', [70])],
            figside=True))
I.append(IT(U, 'S', 11, 3,
            'Ali has 36 cards. He puts them in equal rows, with at least 2 rows and at least 2 cards in each row.',
            'The number of rows must be a factor of 36 other than 1 and 36: 2, 3, 4, 6, 9, 12 and 18. That is 7 ways. '
            '(2 rows of 18 and 18 rows of 2 count as different ways.)',
            parts=[P('a', 'The number of rows could be {ll}', [2, 3, 4, 6, 9, 12, 18], '2, 3, 4, 6, 9, 12, 18', list=True),
                   P('b', 'There are {b} different ways.', [7])]))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            'Find the smallest number with exactly this many factors.',
            '(a) 16 has 1, 2, 4, 8, 16: 5 factors, and no smaller number has 5. (b) 36 has 1, 2, 3, 4, 6, 9, 12, 18, 36: 9 factors. '
            '(c) 48 has 1, 2, 3, 4, 6, 8, 12, 16, 24, 48: 10 factors. Numbers below 48 have fewer.',
            parts=[P('a', '5 factors:  {b}', [16]),
                   P('b', '9 factors:  {b}', [36]),
                   P('c', '10 factors:  {b}', [48])],
            hint='Check numbers in order. Count their factors until you reach 5.', partsrow=True, space={'rows': ['Working:', '']}))
I.append(IT(U, 'T', 2, 4,
            'A number is 2 × 3 × p, where p is a prime greater than 5. The number is less than 100.',
            'p can be 7, 11 or 13: 2 × 3 × 7 = 42, 2 × 3 × 11 = 66 and 2 × 3 × 13 = 78. p = 17 gives 102, which is too big. '
            '42 has factors 1, 2, 3, 6, 7, 14, 21, 42, so 8 factors. 66 and 78 also have 8.',
            parts=[P('a', 'The possible numbers are {l}', [42, 66, 78], '42, 66, 78', list=True),
                   P('b', 'Each of them has {b} factors.', [8]),
                   P('c', 'Which of them is a multiple of 11?   {circ:42|66|78}', ['66'])],
            hint='Try p = 7, then the next primes. Stop at 100.', space={'rows': ['Working:', '']}))
I.append(IT(U, 'T', 3, 4,
            'Find all the primes between 100 and 120.',
            'Test 2, 3, 5 and 7 only, because 11 × 11 = 121 is above 120. 101, 103, 107, 109 and 113 have no factor from the list. '
            'The odd non-primes are 105 (5), 111 (3), 115 (5), 117 (3) and 119 (7). Pairs that differ by 2: 101 and 103, 107 and 109. '
            '(c) The odd multiples of 7 are 105 = 7 \u00d7 15 and 119 = 7 \u00d7 17.',
            parts=[P('a', 'The primes are {ll}', [101, 103, 107, 109, 113], '101, 103, 107, 109, 113', list=True),
                   P('b', 'Pairs of primes that differ by 2: {b} pairs.', [2]),
                   P('c', 'Two odd numbers between 100 and 120 are multiples of 7. They are {b} and {b}.', [105, 119], '105 and 119')],
            hint='Cross out even numbers first. Then test 3, 5 and 7.', space={'rows': ['Working:', '']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            'Break a number into primes, then count its factors. Each factor uses some of the primes.',
            '(a) 72: 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72 is 12 factors. In 2 × 2 × 2 × 3 × 3 a factor uses 0 to 3 twos (4 choices) and 0 to 2 threes (3 choices): 4 × 3 = 12. '
            '(b) 180 = 2 × 2 × 3 × 3 × 5: 3 × 3 × 2 = 18 factors. (c) 60 = 2 × 2 × 3 × 5 has 3 × 2 × 2 = 12 factors. Smaller numbers have fewer.',
            parts=[P('a', 'List the factors of 72, then count them: {b}', [12]),
                   P('b', '180 = 2 × 2 × 3 × 3 × 5 has {b} factors.', [18]),
                   P('c', 'The smallest number with exactly 12 factors is {b}.', [60])],
            hint='Break 72 into primes first. Then count the choices for each prime.',
            beyond='Counting factors', space={'rows': ['Factors of 72:']}))
I.append(IT(U, 'G', 2, 5,
            'Use the sieve to find the primes up to 60. Start by crossing out 1. Then do this for 2, 3, 5 and 7: ring the number and cross out its other multiples.',
            'Cross out multiples of 2, 3, 5 and 7. The next prime, 11, has 11 × 11 = 121, which is above 60, so you can stop at 7. '
            'The numbers left are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59: that is 17 primes. The 10th is 29.',
            fig=grid([[str(r * 10 + c + 1) for c in range(10)] for r in range(6)], [11] * 10, ch=8, fs=17),
            parts=[P('a', 'There are {b} primes up to 60.', [17]),
                   P('b', 'The 10th prime is {b}.', [29])],
            hint='Why can you stop at 7? Think of 8 × 8.', partsrow=True))
I.append(IT(U, 'G', 3, 5,
            'This code looks for the smallest factor of n that is greater than 1. Run it.',
            'n = 221: d goes 2, 3, ... and stops at 13, because 221 mod 13 = 0. It says 13, after 11 repeats (d = 2 to 13). '
            'n = 97: d keeps going until d = 97, because 97 is prime. It says 97. If the code says n itself, then n is prime.',
            fig=code([['var', 'set d to (2)'], ['ctl', 'repeat until <(n) mod (d) = (0)>', [['var', 'change d by (1)']]], ['look', 'say (d)']]),
            parts=[P('a', 'With n = 221 it says {b}.', [13]),
                   P('b', 'With n = 221 the repeat runs {b} times.', [11]),
                   P('c', 'With n = 97 it says {b}.', [97])],
            hint='Write d each time. It stops when n mod d is 0.', figside=True))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            'List all the factors of 40.  {ll}',
            '40 = 1 × 40 = 2 × 20 = 4 × 10 = 5 × 8. The factors are 1, 2, 4, 5, 8, 10, 20 and 40.',
            answer=A([1, 2, 4, 5, 8, 10, 20, 40], '1, 2, 4, 5, 8, 10, 20, 40', list=True)))
I.append(IT(U, 'C', 2, 6,
            'Is 147 prime?  {circ:Yes|No}',
            'The digits add to 1 + 4 + 7 = 12, a multiple of 3, so 3 divides 147 (147 = 3 × 49). It is not prime.',
            answer=A(['No'], 'No')))
I.append(IT(U, 'C', 3, 6,
            'Write 140 as a product of primes.  {ll}',
            '140 = 2 × 70 = 2 × 2 × 35 = 2 × 2 × 5 × 7. Every number here is prime.',
            answer=A([2, 2, 5, 7], '2 × 2 × 5 × 7', list=True)))
I.append(IT(U, 'C', 4, 6,
            '47 mod 6 = {b} and 100 mod 8 = {b}.',
            '47 = 7 × 6 + 5, so the remainder is 5. 100 = 12 × 8 + 4, so the remainder is 4.',
            answer=A([5, 4], '5, 4')))

write_unit(2, 'Prime hunters', 'Primes and factors',
           'I can find all the factors of a number, test whether it is prime and write it as a product of primes. I can count factors with a loop.', learn, I)
