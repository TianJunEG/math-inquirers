"""Level 6 Unit 6: Fair or unfair? (probability, fair games, simulations).  Follows holiday lesson 6."""
from lib import *

U = 'L6U06'
I = []
X = '×'

SPIN10 = ['R', 'B', 'R', 'G', 'B', 'R', 'B', 'G', 'R', 'R']          # 5 R, 3 B, 2 G
sums = [[str(a + b) for b in range(1, 7)] for a in range(1, 7)]

learn = {
    'intro': 'A probability is the number of ways you want, out of all the equally likely outcomes. A game is fair when every player has the same probability of winning. '
             'In many tries we expect about probability × tries, but a real run varies.',
    'example': {
        'problem': 'A bag has 12 counters: 5 red (R), 4 blue (B) and 3 green (G). One is picked without looking. What is the probability of blue? '
                   'About how many blues in 600 picks, if the counter goes back each time?',
        'figure': {'type': 'l6_bag', 'counters': ['R'] * 5 + ['B'] * 4 + ['G'] * 3, 'cols': 6},
        'steps': ['All 12 counters are equally likely to be picked.',
                  '4 of the 12 are blue, so P(blue) = 4/12 = 1/3.',
                  f'In 600 picks we expect 1/3 {X} 600 = 200 blues.',
                  'A real run gives a number near 200, not exactly 200. Each pick is random.'],
        'answer': 'P(blue) = 1/3. About 200 blues in 600 picks.'},
    'howto': {'title': 'How to find a probability',
              'steps': ['Count all the equally likely outcomes.',
                        'Count the outcomes you want.',
                        'Write wanted/all as a fraction and simplify it.',
                        f'Expected number = probability {X} number of tries. A real run is close, not exact.']},
    'try': IT(U, 'L', 1, 0, 'A bag has 6 yellow and 9 blue counters. One is picked without looking.\nP(yellow) = {b}/{b} in simplest form.',
              '15 counters in all and 6 are yellow: 6/15. Divide the top and bottom by 3: 2/5.',
              answer=A([2, 5], '2/5')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'The spinner has 10 equal parts. R is red, B is blue and G is green. Give fractions in simplest form.',
            f'There are 10 equally likely parts. Green: 2 parts, so 2/10 = 1/5. Not red: 3 blue + 2 green = 5 parts, so 5/10 = 1/2. '
            f'Blue is 3/10, and 3/10 {X} 500 = 150.',
            fig={'type': 'l6_spinner', 'parts': SPIN10, 'r': 19},
            parts=[P('a', 'P(green) = {b}/{b}', [1, 5], '1/5'),
                   P('b', 'P(not red) = {b}/{b}', [1, 2], '1/2'),
                   P('c', 'In 500 spins, about {b} are blue.', [150])],
            figside=True))
I.append(IT(U, 'S', 2, 1,
            'One counter is picked from the bag. R is red, B is blue and G is green. Give fractions in simplest form.',
            f'The bag has 4 + 5 + 6 = 15 counters. Blue: 5/15 = 1/3. Red or green: 4 + 6 = 10, so 10/15 = 2/3. '
            f'With 5 more red counters there are 9 red out of 20: 9/20.',
            fig={'type': 'l6_bag', 'counters': ['R'] * 4 + ['B'] * 5 + ['G'] * 6, 'cols': 5},
            parts=[P('a', 'P(blue) = {b}/{b}', [1, 3], '1/3'),
                   P('b', 'P(red or green) = {b}/{b}', [2, 3], '2/3'),
                   P('c', '5 more red counters are put in. Now P(red) = {b}/{b}.', [9, 20], '9/20')],
            figside=True))
I.append(IT(U, 'S', 3, 1,
            'A coin is flipped and a spinner with 3 equal parts A, B and C is spun. A result looks like HB. Use the table to list the results. Give fractions in simplest form.',
            'The coin has 2 results and the spinner has 3, so 2 × 3 = 6 equally likely results, one for each cell. HA is 1 of the 6, so 1/6. '
            'Tails with B or C: TB and TC, so 2/6 = 1/3.',
            fig=grid([['', 'A', 'B', 'C'], ['H', '', '', ''], ['T', '', '', '']], [14, 20, 20, 20], rowhead=True, ch=9),
            parts=[P('a', 'There are {b} different results.', [6]),
                   P('b', 'P(heads and A) = 1/{b}.', [6]),
                   P('c', 'P(tails and not A) = {b}/{b}', [1, 3], '1/3')],
            partsrow=True))
I.append(IT(U, 'S', 4, 2,
            'Two dice, red and blue, are rolled and added. The table shows all 36 equally likely totals. Give fractions in simplest form.',
            'Count in the table. Total 4 is 1+3, 2+2 and 3+1: 3 totals. Totals less than 5 are 2, 3 and 4: 1 + 2 + 3 = 6 totals. '
            '3 out of 36 is 1/12.',
            fig=grid([['+', '1', '2', '3', '4', '5', '6']] + [[str(a)] + sums[a - 1] for a in range(1, 7)], [12] * 7, rowhead=True, ch=7.5),
            parts=[P('a', '{b} of the 36 totals are 4.', [3]),
                   P('b', '{b} of the 36 totals are less than 5.', [6]),
                   P('c', 'P(total is 4) = {b}/{b}', [1, 12], '1/12')],
            figside=True))
I.append(IT(U, 'S', 5, 2,
            'Ali and Ben spin this spinner with the numbers 1 to 10. Ali wins on a prime number. Ben wins on any other number.',
            'The primes from 1 to 10 are 2, 3, 5 and 7, so Ali wins on 4 of the 10 numbers. Ben wins on the other 6 (1, 4, 6, 8, 9, 10). '
            '4 is not equal to 6, so the game is not fair: Ben is more likely to win.',
            fig={'type': 'l6_spinner', 'parts': [str(k) for k in range(1, 11)], 'r': 19},
            parts=[P('a', 'P(Ali wins) = {b}/10', [4]),
                   P('b', 'P(Ben wins) = {b}/10', [6]),
                   P('c', 'Is the game fair?   {circ:Yes|No}', ['No'])],
            figside=True))
I.append(IT(U, 'S', 6, 2,
            'A dice is rolled 300 times and a coin is flipped 90 times. Give the number you expect.',
            f'(a) 1/6 {X} 300 = 50. (b) 5 or 6 is 2 out of 6, so 1/3 {X} 300 = 100. (c) 1/2 {X} 90 = 45. '
            '(d) 54 is close to 50, so it is not surprising. A random run is rarely exactly the expected number.',
            parts=[P('a', 'About {b} fives.', [50]),
                   P('b', 'About {b} numbers greater than 4.', [100]),
                   P('c', 'About {b} heads in 90 flips.', [45]),
                   P('d', 'A run gives 54 fives. Is that surprising?   {circ:Yes|No}', ['No'])],
            partsrow=True))
I.append(IT(U, 'S', 7, 2,
            'This code rolls a dice 100 times and counts the sixes. Predict what happens.',
            f'One roll is 6 with probability 1/6. In 100 rolls we expect 1/6 {X} 100 = 16.7, so about 17. '
            'The answers differ because every roll is random, so each run gives a slightly different count.',
            fig=code([['var', 'set hits to (0)'], ['ctl', 'repeat (100)', [['ctl', 'if <(pick random 1 to 6) = (6)> then', [['var', 'change hits by (1)']]]]], ['look', 'say (hits)']]),
            parts=[P('a', 'The chance of a 6 on one roll is {b}/{b}.', [1, 6], '1/6'),
                   P('b', 'The code says about {b}.', [17]),
                   P('c', '5 runs give 14, 19, 17, 21, 15. Why?   {circ:random rolls|broken code}', ['random rolls'])],
            figside=True))
I.append(IT(U, 'S', 8, 3,
            'Cards are numbered 1 to 30. One card is drawn without looking. Give fractions in simplest form.',
            'There are 30 equally likely numbers. Multiples of 7: 7, 14, 21, 28 is 4, so 4/30 = 2/15. Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 is 10, so 10/30 = 1/3. '
            'Squares: 1, 4, 9, 16, 25 is 5, so 5/30 = 1/6.',
            parts=[P('a', 'P(multiple of 7) = {b}/{b}', [2, 15], '2/15'),
                   P('b', 'P(prime) = {b}/{b}', [1, 3], '1/3'),
                   P('c', 'P(square number) = {b}/{b}', [1, 6], '1/6')]))
I.append(IT(U, 'S', 9, 3,
            'Bag A has 3 red and 5 blue counters. Bag B has 4 red and 7 blue counters. You want to pick a red counter.',
            'Bag A: 3 red out of 8, so 3/8. Bag B: 4 red out of 11, so 4/11. Compare with a common bottom number, 88: 3/8 = 33/88 and 4/11 = 32/88. 33 is greater than 32, so Bag A gives the better chance.',
            parts=[P('a', 'In Bag A, P(red) = {b}/{b}.', [3, 8], '3/8'),
                   P('b', 'In Bag B, P(red) = {b}/{b}.', [4, 11], '4/11'),
                   P('c', 'Which bag gives the better chance of red?   {circ:Bag A|Bag B}', ['Bag A'])]))
I.append(IT(U, 'S', 10, 3,
            'Ravi flips a fair coin 200 times and gets 112 heads.',
            f'(a) 1/2 {X} 200 = 100. (b) 112 − 100 = 12. (c) A random run is not exactly 100 each time. 112 is not far from 100, so the coin could still be fair.',
            parts=[P('a', 'About {b} heads are expected.', [100]),
                   P('b', 'The difference from the expected number is {b}.', [12]),
                   P('c', 'Could the coin still be fair?   {circ:Yes|No}', ['Yes'])]))
I.append(IT(U, 'S', 11, 3,
            'Two dice are rolled and added. The totals 2 to 12 are not equally likely.',
            'The totals 2 to 12 are not equally likely. 7 happens 6 ways, which is the most. 6 happens 5 ways and 8 happens 5 ways: 10/36. '
            '2 (1+1) and 12 (6+6) happen 1 way each: 2/36.',
            parts=[P('a', 'The most likely total is {b}.', [7]),
                   P('b', 'P(total is 6 or 8) = {b}/36', [10]),
                   P('c', 'P(total is 2 or 12) = {b}/36', [2])]))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            'Two dice are rolled and added. In Game 1, Ali wins on an even total and Ben wins on an odd total.',
            'An even total needs both dice odd (3 \u00d7 3 = 9 ways) or both dice even (3 \u00d7 3 = 9 ways): 18 of the 36. So 18/36 each: fair. '
            'Game 2: Ali wins on 7, which is 6/36, and Ben on the other 30/36. If Ali scores 5 points a win and Ben scores 1, then 6 × 5 = 30 and 30 × 1 = 30: fair.',
            parts=[P('a', 'Game 1: Ali wins on {b} of the 36 totals.', [18]),
                   P('b', 'Is Game 1 fair?   {circ:Yes|No}', ['Yes']),
                   P('c', 'Game 2: Ali wins on a total of 7. Ben wins on every other total and scores 1 point for a win. For a fair game Ali must score {b} points for a win.', [5])],
            hint='Fair means the winning points are equal over many games.', space={'rows': ['Working:']}))
I.append(IT(U, 'T', 2, 4,
            'A bag has 3 red counters (R1, R2, R3) and 2 blue counters (B1, B2). Two counters are taken out one after another. The first is not put back. Give fractions in simplest form.',
            'The first counter has 5 choices and the second has 4: 5 × 4 = 20 equally likely ordered pairs. Both red: 3 choices, then 2: 6 pairs. '
            '6/20 = 3/10.',
            parts=[P('a', 'There are {b} equally likely ordered pairs.', [20]),
                   P('b', '{b} of them are both red.', [6]),
                   P('c', 'P(both red) = {b}/{b}', [3, 10], '3/10')],
            hint='List the pairs: R1R2, R1R3, R1B1, ... Is R2R1 different?', partsrow=True, space={'rows': ['Working:']}))
I.append(IT(U, 'T', 3, 4,
            'A program rolls a dice 600 times and counts the 3s. Five runs give 93, 108, 97, 114 and 102.',
            f'(a) 1/6 {X} 600 = 100. (b) 93 + 108 + 97 + 114 + 102 = 514, and 514 ÷ 5 = 102.8. '
            f'(c) Every run is near 100 and the mean is very close to 100, so the dice looks fair.',
            parts=[P('a', 'The expected number of 3s is {b}.', [100]),
                   P('b', 'The mean of the 5 runs is {b}.', [102.8]),
                   P('c', 'Does the dice look fair?   {circ:Yes|No}', ['Yes'])],
            hint='Add the 5 numbers, then divide by 5.', partsrow=True, space={'rows': ['Working:']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            'A coin is flipped 4 times.',
            'Each flip has 2 results, so 2 × 2 × 2 × 2 = 16 equally likely outcomes. Exactly 2 heads: HHTT, HTHT, HTTH, THHT, THTH, TTHH is 6, so 6/16. '
            'At least one tail is every outcome except HHHH: 15/16.',
            parts=[P('a', 'There are {b} equally likely outcomes.', [16]),
                   P('b', 'P(exactly 2 heads) = {b}/16', [6]),
                   P('c', 'P(at least one tail) = {b}/16', [15])],
            hint='Which single outcome has no tails? Take it from all 16.', partsrow=True, space={'rows': ['Working:']}, beyond='Probability of at least one'))
I.append(IT(U, 'G', 2, 5,
            'This code rolls 2 dice 600 times. Predict what it says.',
            'For any a, only 1 of the 6 values of b matches it: 1 out of 6. So we expect 1/6 × 600 = 100 doubles. '
            'The pairs that add to 4 are 1+3, 2+2 and 3+1: 3 of 36, which is 1/12. 1/12 × 600 = 50.',
            fig=code([['var', 'set doubles to (0)'], ['ctl', 'repeat (600)', [['var', 'set a to (pick random 1 to 6)'], ['var', 'set b to (pick random 1 to 6)'], ['ctl', 'if <(a) = (b)> then', [['var', 'change doubles by (1)']]]]], ['look', 'say (doubles)']]),
            parts=[P('a', 'For a given a, b matches it in {b} out of 6 ways.', [1]),
                   P('b', 'It says about {b}.', [100]),
                   P('c', 'Change a = b to a + b = 4. It says about {b}.', [50])],
            hint='List the pairs (a, b) that add to 4.', figside=True))
I.append(IT(U, 'G', 3, 5,
            'A game costs 2 dollars to play. You roll a dice and win a prize if you roll a 6. You play 600 times.',
            'A 6 comes up about 1/6 × 600 = 100 times. You pay 600 × 2 = 1200 dollars. If the prize is 5 dollars you win about 100 × 5 = 500 dollars, so you lose money. '
            'The game is fair when the winnings equal what you paid: 100 × prize = 1200, so the prize is 12 dollars.',
            parts=[P('a', 'You win about {b} times.', [100]),
                   P('b', 'You pay {b} dollars. With a 5-dollar prize you win about {b} dollars.', [1200, 500], '1200, 500'),
                   P('c', 'The game is fair when the prize for a 6 is {b} dollars.', [12])],
            hint='Fair means the money won equals the money paid.', space={'rows': ['Working:']}, beyond='Expected winnings'))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            'A bag has 9 red and 6 blue counters. P(blue) = {b}/{b} in simplest form.',
            '15 counters in all and 6 are blue: 6/15. Divide the top and bottom by 3: 2/5.',
            answer=A([2, 5], '2/5')))
I.append(IT(U, 'C', 2, 6,
            'A dice is rolled 240 times. About {b} of the rolls are even numbers.',
            f'Even numbers are 2, 4 and 6, so the probability is 3/6 = 1/2. 1/2 {X} 240 = 120.',
            answer=A([120], '120')))
I.append(IT(U, 'C', 3, 6,
            'Two coins are flipped. P(2 tails) = {b}/{b}.',
            'The outcomes are HH, HT, TH and TT, which are equally likely. Only TT has 2 tails: 1/4.',
            answer=A([1, 4], '1/4')))
I.append(IT(U, 'C', 4, 6,
            'A spinner has 8 equal parts and 2 are green. In 400 spins about {b} are green.',
            f'P(green) = 2/8 = 1/4. 1/4 {X} 400 = 100.',
            answer=A([100], '100')))

write_unit(6, 'Fair or unfair?', 'Probability',
           'I can write a probability as a fraction, decide whether a game is fair, and say what to expect from many tries.', learn, I)
