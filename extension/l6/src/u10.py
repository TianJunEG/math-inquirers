"""Level 6 Unit 10: Showcase challenge (mixed maths and code).  Follows holiday lesson 10."""
from lib import *

U = 'L6U10'
I = []
X = '×'
M = '−'

learn = {
    'intro': 'A good puzzle program starts with maths. Find the answer by hand first, then turn the rule into blocks, then test it with a number you already know the answer for.',
    'example': {
        'problem': 'Plan a program. It asks for n and says the day n days after Monday. The list days holds Monday to Sunday.',
        'figure': code([['look', 'ask (n?) and wait'], ['var', 'set pos to (answer mod 7 + 1)'], ['look', 'say (item pos of days)']]),
        'steps': ['Idea: a week is a clock with 7 days, so we need n mod 7.',
                  'By hand: 10 days after Monday. 10 mod 7 = 3, so the day is Thursday.',
                  'Blocks: a list starts at item 1, so use item (n mod 7 + 1) of days.',
                  'Test with known values: n = 10 gives Thursday, n = 0 and n = 7 give Monday.'],
        'answer': 'The program says item 4 of days, Thursday, when n = 10.'},
    'howto': {'title': 'How to plan a puzzle program',
              'steps': ['Pick a maths idea and find an answer by hand.',
                        'Turn the rule into blocks: input, rule, output.',
                        'Test with a value you know. Also try 0 or 1.',
                        'Add a twist, then explain why it works.']},
    'try': IT(U, 'L', 1, 0, 'The user types 19. What does the program above say? {l}',
              '19 mod 7 = 5, because 19 = 2 × 7 + 5. pos = 5 + 1 = 6, and item 6 of days is Saturday.',
              answer=A(['Saturday'], 'Saturday')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'A pattern uses 10, 17, 24, 31, ... tiles.',
            f'The difference is 7. Each term is 3 more than 7, 14, 21, 28, so the rule is 7n + 3. The 50th term is 7 {X} 50 + 3 = 353. '
            f'7n + 3 = 164 gives 7n = 161, so n = 23.',
            parts=[P('a', f'The rule is {{b}} {X} n + {{b}}.', [7, 3], '7, 3'),
                   P('b', 'The 50th term is {b}.', [353]),
                   P('c', '164 is term number {b}.', [23])],
            partsrow=True))
I.append(IT(U, 'S', 2, 1,
            'Test numbers for factors. Remember: stop when d × d is more than the number.',
            '91 = 7 × 13, 93 = 3 × 31, 95 = 5 × 19, 99 = 9 × 11, 105 = 5 × 21 and 111 = 3 × 37 are not prime. So the primes are 97, 101, 103, 107 and 109. '
            '330 = 33 × 10 = 3 × 11 × 2 × 5.',
            parts=[P('a', 'The primes between 90 and 110 are {ll}', [97, 101, 103, 107, 109], '97, 101, 103, 107, 109', list=True),
                   P('b', 'Write 330 as a product of primes: {ll}', [2, 3, 5, 11], '2 × 3 × 5 × 11', list=True)]))
I.append(IT(U, 'S', 3, 1,
            f"Mei's bank balance is {M}6 dollars, so she owes the bank. She pays in 15 dollars and then spends 20 dollars.",
            f'{M}6 + 15 = 9. Then 9 {M} 20 = {M}11. From {M}6 up to 21 is 6 steps to 0 and 21 more: 27.',
            parts=[P('a', 'Her balance is now {b} dollars.', [-11], f'{M}11'),
                   P('b', 'Later her balance goes from −6 to 21 dollars. It rises by {b} dollars.', [27])]))
I.append(IT(U, 'S', 4, 1,
            'Run the machines backwards.',
            f'(a) OUT 43: 43 + 7 = 50, and 50 ÷ 5 = 10. (b) 6n + 1 = 79 gives 6n = 78 and n = 13.',
            parts=[P('a', f'A machine does {X} 5, then {M} 7. OUT is 43. IN = {{b}}', [10]),
                   P('b', f'OUT = 6n + 1 and OUT is 79. IN = {{b}}', [13])]))
I.append(IT(U, 'S', 5, 2,
            'Count every possible way.',
            f'(a) 3 {X} 5 {X} 2 = 30. (b) 9 friends: 9 {X} 8 ÷ 2 = 36. (c) 4 choices, then 3, then 2: 4 {X} 3 {X} 2 = 24.',
            parts=[P('a', 'A menu has 3 starters, 5 mains and 2 drinks. A meal is one of each: {b} meals.', [30]),
                   P('b', '9 friends: every pair shakes hands once: {b} handshakes.', [36]),
                   P('c', 'Cards 2, 4, 6 and 8: {b} different 3-digit numbers, using no card twice.', [24])]))
I.append(IT(U, 'S', 6, 2,
            'Think about fair and likely.',
            f'(a) 8 counters, 5 red: 5/8. (b) 1/6 {X} 1200 = 200. (c) An even number is 2, 4 or 6, and 1, 3 or 5 is the other 3 numbers: 3 out of 6 each, so the game is fair.',
            parts=[P('a', 'A bag has 5 red and 3 blue counters. P(red) = {b}/{b}.', [5, 8], '5/8'),
                   P('b', 'A dice is rolled 1200 times. About {b} of the rolls are 4s.', [200]),
                   P('c', 'Ali wins on an even number. Ben wins on 1, 3 or 5. Is it fair?   {circ:Yes|No}', ['Yes'])]))
I.append(IT(U, 'S', 7, 2,
            'A turtle turns 4° at every corner of a regular polygon.',
            f'360 ÷ 4 = 90 sides. The inside angle is 180 {M} 4 = 176°.',
            parts=[P('a', 'The polygon has {b} sides.', [90]),
                   P('b', 'Each inside angle is {b}°.', [176])],
            partsrow=True))
I.append(IT(U, 'S', 8, 2,
            'Clocks and codes.',
            f'(a) 4 + 75 = 79. 79 mod 12 = 7, because 6 {X} 12 = 72. (b) M = 12, A = 0, T = 19, H = 7. Add 9: 21, 9, 28, 16. 28 {M} 26 = 2. The letters are V, J, C, Q.',
            parts=[P('a', 'It is 4 o\'clock. In 75 hours it is {b} o\'clock.', [7]),
                   P('b', 'Code MATH with a shift of 9: {l}', ['VJCQ'])]))
I.append(IT(U, 'S', 9, 3,
            'Averages.',
            f'(a) The total of 4 numbers is 4 {X} 15 = 60. 11 + 19 + 14 = 44, so the 4th is 16. (b) In order: 4, 9, 12, 15. The middle two are 9 and 12, so the median is halfway between them: 10.5.',
            parts=[P('a', 'The mean of 4 numbers is 15. Three of them are 11, 19 and 14. The 4th is {b}.', [16]),
                   P('b', 'The median of 15, 4, 9, 12 is {b}.', [10.5])]))
I.append(IT(U, 'S', 10, 3,
            'A game starts with a score of 50. This code plays 8 rounds. Run it by hand.',
            'Each round takes away 8: 42, 34, 26, 18. The score 18 is below 20, so it resets to 50 after round 4. Rounds 5 to 8 repeat the pattern: 42, 34, 26, 18, and the score resets to 50 again after round 8. '
            'After round 6 the score is 34.',
            fig=code([['var', 'set score to (50)'], ['ctl', 'repeat (8)', [['var', f'change score by ({M}8)'], ['ctl', 'if <(score) {lt} (20)> then', [['var', 'set score to (50)']]]]], ['look', 'say (score)']]),
            parts=[P('a', 'After round 6 the score is {b}.', [34]),
                   P('b', 'The score first resets to 50 after round {b}.', [4]),
                   P('c', 'The program says {b}.', [50])],
            figside=True))
I.append(IT(U, 'S', 11, 3,
            'The steps of planning a program are mixed up. A: Test with a value you know. B: Do the maths by hand. C: Build the blocks. D: Pick a maths idea. E: Add a twist.',
            'You need an idea (D) before you can do the maths (B). You build the blocks (C) after the maths, test them (A) once they exist, and add a twist (E) when the basic version works.',
            answer=A(['D', 'B', 'C', 'A', 'E'], 'D, B, C, A, E', list=True),
            space={'rows': ['The order is {ll}']}))

I.append(IT(U, 'S', 12, 3,
            'A program runs: set n to 11, then repeat 25 times: change n by 6. Then it says n.',
            f'n goes 11, 17, 23, ... and after 25 jumps it is 11 + 25 {X} 6 = 161. From the 1st term to the 26th term is 25 jumps, so 161 is the 26th term. The rule is 6n + 5 (6 {X} 26 + 5 = 161).',
            parts=[P('a', 'The program says {b}.', [161]),
                   P('b', 'That is term number {b} of 11, 17, 23, ...', [26]),
                   P('c', f'The rule for the sequence is {{b}} {X} n + {{b}}.', [6, 5], '6, 5')],
            partsrow=True))
I.append(IT(U, 'S', 13, 3,
            'Roll 2 dice and multiply the numbers. There are 36 equally likely results.',
            f'A product of 12 comes from 2 and 6, 3 and 4, 4 and 3, 6 and 2: 4 results. The product is odd only when both numbers are odd: 3 {X} 3 = 9 results, 9/36 = 1/4. '
            f'1/4 {X} 360 = 90.',
            parts=[P('a', '{b} of the 36 products are 12.', [4]),
                   P('b', 'P(product is odd) = {b}/{b} in simplest form.', [1, 4], '1/4'),
                   P('c', 'The dice are rolled 360 times. About {b} products are odd.', [90])]))
I.append(IT(U, 'S', 14, 3,
            'A sprite starts at x = 15. It repeats 7 times: change x by −4.',
            f'7 moves of {M}4 make {M}28. 15 {M} 28 = {M}13. After 4 repeats x = 15 {M} 16 = {M}1, which is the first time below 0 (after 3 repeats x = 3).',
            parts=[P('a', 'After the 7 repeats, x = {b}.', [-13], f'{M}13'),
                   P('b', 'x is below 0 for the first time after repeat {b}.', [4])],
            partsrow=True, space={'rows': ['Working:']}))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            'A sequence has the rule 6n − 1. Look at its first 10 terms.',
            '5, 11, 17, 23, 29, 35, 41, 47, 53, 59. 35 = 5 × 7 is the only one that is not prime, so 9 of the 10 are prime. '
            '6n is even and an even number take away 1 is odd, so every term is odd.',
            parts=[P('a', '{b} of the first 10 terms are prime.', [9]),
                   P('b', 'The one that is not prime is {b}.', [35]),
                   P('c', 'Is every term odd?   {circ:Yes|No}', ['Yes'])],
            hint='Write out the 10 terms. Test each for factors.', partsrow=True, space={'rows': ['Terms:', '']}))
I.append(IT(U, 'T', 2, 4,
            'Ali has taken 5 tests. His mean score is 74. After the 6th test his mean is 76.',
            f'The 5 tests total 5 {X} 74 = 370. The 6 tests total 6 {X} 76 = 456. The 6th score is 456 {M} 370 = 86.',
            parts=[P('a', 'The 5 scores add up to {b}.', [370]),
                   P('b', 'After the 6th test the total is {b}.', [456]),
                   P('c', 'The 6th score is {b}.', [86])],
            hint='Total = mean × how many. Do it for 5 tests and for 6.', partsrow=True, space={'rows': ['Working:', '']}))
I.append(IT(U, 'T', 3, 4,
            'A 2-digit number has digits that add to 10. Reversing its digits gives another 2-digit number.',
            '19, 28, 37, 46, 55, 64, 73, 82, 91 have digits adding to 10. The primes are 19, 37 and 73 (the others are even, or 55 and 91 = 7 × 13). '
            'Reversed: 19 gives 91, which is not prime. 37 gives 73 and 73 gives 37, both prime.',
            parts=[P('a', 'The primes with digits that add to 10 are {l}', [19, 37, 73], '19, 37, 73', list=True),
                   P('b', 'Those whose reverse is also prime are {b} and {b}.', [37, 73], '37 and 73')],
            hint='List all numbers with digit sum 10. Cross out the non-primes.', space={'rows': ['Working:', '', '']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            'A taxi fare is 7 dollars for 2 km and 16 dollars for 5 km, by one rule. Plan the meter.',
            f'From 2 km to 5 km is 3 km more, and the fare rises by 16 {M} 7 = 9 dollars, so each km costs 9 ÷ 3 = 3 dollars. Then 7 = 3 {X} 2 + 1, so there is a 1 dollar start fee. The rule is n {X} 3 + 1. '
            f'A 20 km ride costs 3 {X} 20 + 1 = 61 dollars. A fare of 49 dollars means 3n = 48, so n = 16. (For your twist, test with a ride you can price by hand first.)',
            fig=code([['look', 'ask (km?) and wait'], ['look', f'say (answer {X} ? + ?)']]),
            parts=[P('a', f'say (n {X} {{b}} + {{b}})', [3, 1], '3, 1'),
                   P('b', 'A 20 km ride costs {b} dollars.', [61]),
                   P('c', 'A fare of 49 dollars is a ride of {b} km.', [16])],
            hint='How many km apart are 2 km and 5 km? How much more is the fare?', figright=True, partsrow=True))
I.append(IT(U, 'G', 2, 5,
            'A spinner has 8 equal parts numbered 1 to 8. This program spins it 800 times and counts the numbers greater than 6.',
            f'The numbers greater than 6 are 7 and 8, which is 2 results out of 8, so 1/4. 1/4 {X} 800 = 200. The numbers greater than 4 are 5, 6, 7 and 8, which is 4 out of 8, so the count would be 1/2 {X} 800 = 400. '
            f'A real run is near these numbers, not exactly equal.',
            fig=code([['var', 'set count to (0)'], ['ctl', 'repeat (800)', [['ctl', 'if <(pick random 1 to 8) {gt} (6)> then', [['var', 'change count by (1)']]]]], ['look', 'say (count)']]),
            parts=[P('a', 'P(greater than 6) = {b}/8', [2]),
                   P('b', 'The program says about {b}.', [200]),
                   P('c', 'If the test were greater than 4, it would say about {b}.', [400])],
            figside=True))
I.append(IT(U, 'G', 3, 5,
            'This code stops when n reaches 1. Run it by hand.',
            f'n = 6: 6, 3, 10, 5, 16, 8, 4, 2, 1. That is 8 steps (halve if even, or 3n + 1 if odd). n = 7: 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 is 16 steps. '
            f'The largest number reached from 7 is 52.',
            fig=code([['var', 'set steps to (0)'],
                      ['ctl', 'repeat until <(n) = (1)>', [['ctl', 'if <(n mod 2) = (0)> then', [['var', f'set n to (n ÷ 2)']], [['var', f'set n to (n {X} 3 + 1)']]], ['var', 'change steps by (1)']]],
                      ['look', 'say (steps)']]),
            parts=[P('a', 'With n = 6 it says {b}.', [8]),
                   P('b', 'With n = 7 it says {b}.', [16]),
                   P('c', 'Starting at 7, the largest value n takes is {b}.', [52])],
            figside=True))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            f'4, 11, 18, 25, ... The rule is {{b}} {X} n {M} {{b}}.',
            f'The difference is 7. Each term is 3 less than 7, 14, 21, 28, so the rule is 7n {M} 3.',
            answer=A([7, 3], '7, 3')))
I.append(IT(U, 'C', 2, 6,
            f'{M}7 + 12 {M} 9 = {{b}}',
            f'{M}7 + 12 = 5. Then 5 {M} 9 = {M}4.',
            answer=A([-4], f'{M}4')))
I.append(IT(U, 'C', 3, 6,
            'A bag holds 7 red counters and 8 blue counters. P(red) = {b}/{b} in simplest form.',
            '7 red out of 15 counters is 7/15, which is already in simplest form.',
            answer=A([7, 15], '7/15')))
I.append(IT(U, 'C', 4, 6,
            'It is 3 o\'clock. In 100 hours it will be {b} o\'clock.',
            f'3 + 100 = 103. 103 mod 12 = 7, because 8 {X} 12 = 96. It will be 7 o\'clock.',
            answer=A([7], '7')))

write_unit(10, 'Showcase challenge', 'Mixed maths and code',
           'I can use ideas from all the units in a mixed challenge, and plan a small puzzle program: maths first, then blocks, then tests.', learn, I)
