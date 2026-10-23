"""Level 6 Unit 5: Every possible way (counting).  Follows holiday lesson 5."""
from lib import *

U = 'L6U05'
I = []
X = '×'

learn = {
    'intro': 'To count every possible case, list them in order and do not miss one. Choices made one after another multiply. '
             'When the order does not matter, each pair is counted twice, so halve the total.',
    'example': {
        'problem': 'A cafe sells 3 sandwiches and 4 drinks. A meal is 1 sandwich and 1 drink. How many different meals are there?',
        'figure': grid([['', 'Tea', 'Juice', 'Milk', 'Water'], ['Egg', '1', '2', '3', '4'], ['Ham', '5', '6', '7', '8'], ['Tuna', '9', '10', '11', '12']],
                       [22, 22, 22, 22, 22], rowhead=True, ch=8.5),
        'steps': ['Fix one sandwich. It goes with each of the 4 drinks, so there are 4 meals.',
                  'There are 3 sandwiches, so there are 3 groups of 4 meals.',
                  f'3 {X} 4 = 12 meals. Each cell of the table is one meal.',
                  f'Add a choice of 2 fruits. Every meal splits in 2 ways: 12 {X} 2 = 24.'],
        'answer': '12 meals (24 meals if there is also a choice of 2 fruits).'},
    'howto': {'title': 'How to count every possible way',
              'steps': ['List the choices in order. Fix the first choice, then run through the next.',
                        f'Choices made one after another multiply: 3 {X} 4.',
                        'If the order does not matter, each pair is counted twice. So halve.',
                        'Check a small case by listing it all.']},
    'try': IT(U, 'L', 1, 0, 'A pizza place has 4 crusts and 6 toppings. A pizza has 1 crust and 1 topping. How many different pizzas are there? {b}',
              f'Choices one after another multiply: 4 {X} 6 = 24. Check: each of the 4 crusts goes with 6 toppings, which makes 4 groups of 6.',
              answer=A([24], '24')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'A lunch box has 1 main, 1 drink and 1 fruit. There are 4 mains, 3 drinks and 2 fruits.',
            f'Choices one after another multiply: 4 {X} 3 {X} 2 = 24. With 4 drinks: 4 {X} 4 {X} 2 = 32. A lunch with juice has only 1 drink choice: 4 {X} 1 {X} 2 = 8.',
            parts=[P('a', 'There are {b} different lunches.', [24]),
                   P('b', 'The shop adds 1 more drink. Now there are {b} lunches.', [32]),
                   P('c', 'Juice is one of the 3 drinks. {b} lunches have juice.', [8])]))
I.append(IT(U, 'S', 2, 1,
            'Flip a coin and roll a dice. A result looks like H3 (heads and 3). Use the table to list the results.',
            'The coin has 2 results and the dice has 6, so 2 × 6 = 12 results, one for each cell. Tails with more than 4: T5 and T6, so 2. '
            'Heads with an even number: H2, H4 and H6, so 3.',
            fig=grid([['', '1', '2', '3', '4', '5', '6'], ['H', '', '', '', '', '', ''], ['T', '', '', '', '', '', '']], [14, 16, 16, 16, 16, 16, 16], rowhead=True, ch=8),
            parts=[P('a', 'There are {b} different results.', [12]),
                   P('b', 'Tails and a number greater than 4: {b} results.', [2]),
                   P('c', 'Heads and an even number: {b} results.', [3])],
            partsrow=True))
I.append(IT(U, 'S', 3, 1,
            'At a party, any 2 friends shake hands exactly once.',
            'Each new friend shakes hands with all the friends before. 6 friends: 1 + 2 + 3 + 4 + 5 = 15. 8 friends: 1 + 2 + ... + 7 = 28. '
            '36 = 1 + 2 + ... + 8, so there are 9 friends. (Another way: 8 × 7 ÷ 2 = 28.)',
            fig={'type': 'l6_dots', 'groups': [{'n': 5, 'all': True, 'caption': '5 friends: 10 handshakes', 'r': 12}]},
            parts=[P('a', 'With 6 friends there are {b} handshakes.', [15]),
                   P('b', 'With 8 friends there are {b} handshakes.', [28]),
                   P('c', 'A party has 36 handshakes. There are {b} friends.', [9])],
            figside=True))
I.append(IT(U, 'S', 4, 2,
            'The inner loop does all its repeats each time the outer loop goes round. Predict what the sprite says.',
            'A is said once for each turn of the outer repeat: 3 times. B is said 5 times in each turn: 3 × 5 = 15 times. In all it says 3 + 15 = 18 things.',
            fig=code([['ctl', 'repeat (3)', [['look', 'say (A) for (1) seconds'], ['ctl', 'repeat (5)', [['look', 'say (B) for (1) seconds']]]]]]),
            parts=[P('a', 'It says A {b} times.', [3]),
                   P('b', 'It says B {b} times.', [15]),
                   P('c', 'In all it says {b} things.', [18])],
            figside=True))
I.append(IT(U, 'S', 5, 2,
            'A walker goes only right or up from Start to End. Each number shows how many routes reach that corner. Fill in the empty circles.',
            'A corner is reached from the corner on its left or the corner below, so add those 2 numbers. Middle row: 2, 3, 4. Top row: 3, 6, 10. There are 10 routes to End.',
            fig={'type': 'l6_routes', 'cols': 3, 'rows': 2, 'cell': 15,
                 'nums': {'0,0': 1, '1,0': 1, '2,0': 1, '3,0': 1, '0,1': 1, '0,2': 1, '1,1': None, '2,1': None, '3,1': None, '1,2': None, '2,2': None, '3,2': None}},
            parts=[P('a', 'There are {b} routes from Start to End.', [10])],
            figside=True))
I.append(IT(U, 'S', 6, 2,
            'A password has 3 letters. Each letter is A, B, C or D.',
            f'Letters may repeat: 4 {X} 4 {X} 4 = 64. No repeats: 4 choices, then 3, then 2: 4 {X} 3 {X} 2 = 24. First letter A and repeats allowed: 1 {X} 4 {X} 4 = 16.',
            parts=[P('a', 'Letters may repeat: {b} passwords.', [64]),
                   P('b', 'No letter may repeat: {b} passwords.', [24]),
                   P('c', 'Letters may repeat, and the first letter is A: {b} passwords.', [16])]))
I.append(IT(U, 'S', 7, 2,
            'There are 5 runners in a race. Gold, silver and bronze go to 3 different runners.',
            f'Gold has 5 choices, then silver 4, then bronze 3: 5 {X} 4 {X} 3 = 60. If Ali wins gold, silver has 4 choices and bronze 3: 4 {X} 3 = 12.',
            parts=[P('a', 'The medals can be given in {b} different ways.', [60]),
                   P('b', 'Ali must win gold. Then there are {b} ways.', [12])]))
I.append(IT(U, 'S', 8, 3,
            'This code lists pairs. The outer repeat changes a and the inner repeat changes b. Predict what it says.',
            'For each a the inner repeat says 2 numbers: 11, 12, then 21, 22, then 31, 32. The 3rd is 21 and it says 6 numbers. '
            'With 4 inner repeats it says 3 × 4 = 12 numbers.',
            fig=code([['var', 'set a to (1)'], ['ctl', 'repeat (3)', [['var', 'set b to (1)'], ['ctl', 'repeat (2)', [['look', 'say (a × 10 + b) for (1) seconds'], ['var', 'change b by (1)']]], ['var', 'change a by (1)']]]]),
            parts=[P('a', 'The 3rd number it says is {b}.', [21]),
                   P('b', 'It says {b} numbers.', [6]),
                   P('c', 'With repeat 4 as the inner repeat, it says {b} numbers.', [12])],
            figside=True))
I.append(IT(U, 'S', 9, 3,
            'Make 3-digit numbers from the cards, using no card twice. A number cannot start with 0.',
            f'First digit: 3 choices (not 0). Second digit: 3 choices (0 is allowed, but not the card already used). Third digit: 2 choices. 3 {X} 3 {X} 2 = 18. '
            'Odd numbers end in 1 or 3. For each ending, the first digit has 2 choices (not 0 and not the ending) and the middle digit has 2: 2 × 2 × 2 = 8.',
            fig={'type': 'l6_cards', 'cards': ['0', '1', '2', '3'], 'card': 11},
            parts=[P('a', 'There are {b} different numbers.', [18]),
                   P('b', '{b} of them are odd.', [8])],
            figside=True))
I.append(IT(U, 'S', 10, 3,
            'An octagon has 8 corners. Join every pair of corners with a straight line.',
            f'Every pair of corners gives a line: 8 {X} 7 ÷ 2 = 28. 8 of the lines are the sides, so 28 − 8 = 20 are diagonals. '
            f'10 corners: 10 {X} 9 ÷ 2 = 45 lines, 10 are sides, so 35 diagonals.',
            fig={'type': 'l6_dots', 'groups': [{'n': 8, 'r': 14, 'edges': []}]},
            parts=[P('a', 'There are {b} lines in all.', [28]),
                   P('b', 'Diagonals (lines that are not sides): {b}', [20]),
                   P('c', 'A shape with 10 corners has {b} diagonals.', [35])],
            figside=True))
I.append(IT(U, 'S', 11, 3,
            'A rectangle in a row of squares can be 1, 2, 3, ... squares long. Count every rectangle.',
            'In a row of 5: 5 of length 1, 4 of length 2, 3 of length 3, 2 of length 4, 1 of length 5: 5 + 4 + 3 + 2 + 1 = 15. '
            'In a row of 7: 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28.',
            fig=grid([['', '', '', '', '']], [13] * 5, ch=13),
            parts=[P('a', 'This row of 5 squares has {b} rectangles.', [15]),
                   P('b', 'A row of 7 squares has {b} rectangles.', [28])],
            figside=True))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            'A walker goes only right or up from Start to End. X is a point on the way.',
            'Routes to X: right 2 and up 1, so 3 routes (RRU, RUR, URR). Routes from X to End: right 2 and up 2, so 6 routes. Every route through X is one of the 3 followed by one of the 6: 3 × 6 = 18.',
            fig={'type': 'l6_routes', 'cols': 4, 'rows': 3, 'cell': 10, 'mark': ['2,1']},
            parts=[P('a', 'Routes from Start to X: {b}. Routes from X to End: {b}.', [3, 6], '3, 6'),
                   P('b', 'Routes that go through X: {b}.', [18])],
            hint='Count the routes to X and from X separately. Then multiply.', figright=True, partsrow=True))
I.append(IT(U, 'T', 2, 4,
            'You have 4 digit cards: 1, 2, 3, 4. Put all 4 cards in a row to make a 4-digit number.',
            'First digit 4 choices, then 3, then 2, then 1: 24 numbers. Even numbers end in 2 or 4: 2 choices for the last digit and 3 × 2 × 1 for the rest, 12. '
            'Multiples of 4 need the last 2 digits to be 12, 24 or 32. Each leaves 2 numbers (for example 3412 and 4312): 3 × 2 = 6.',
            parts=[P('a', 'There are {b} numbers in all.', [24]),
                   P('b', '{b} of them are even.', [12]),
                   P('c', '{b} of them are multiples of 4.', [6])],
            hint='Which two-digit endings are in the 4 times table?', partsrow=True))
I.append(IT(U, 'T', 3, 4,
            'P is not on the line. A triangle uses P and 2 of the points on the line.',
            'Each pair of points on the line makes one triangle with P. 4 points: 4 × 3 ÷ 2 = 6 pairs. 5 points: 5 × 4 ÷ 2 = 10. 8 points: 8 × 7 ÷ 2 = 28. '
            'This is the handshake count again.',
            fig={'type': 'l6_dots', 'groups': [{'pts': [[26, 0, 'P'], [0, 20, '1'], [13, 20, '2'], [26, 20, '3'], [39, 20, '4'], [52, 20, '5']],
                                                  'edges': [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 2], [2, 3], [3, 4], [4, 5]]}]},
            parts=[P('a', 'With 4 points on the line there are {b} triangles.', [6]),
                   P('b', 'With 5 points there are {b} triangles.', [10]),
                   P('c', 'With 8 points there are {b} triangles.', [28])],
            hint='Each triangle is a pair of points on the line. Count pairs.', figright=True, partsrow=True))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            'A code has 3 digits. Each digit is 1, 2, 3, 4 or 5, and digits may repeat.',
            f'All codes: 5 {X} 5 {X} 5 = 125. Codes with no 5 use only 1, 2, 3 or 4: 4 {X} 4 {X} 4 = 64. Every other code has at least one 5: 125 − 64 = 61.',
            parts=[P('a', 'There are {b} codes in all.', [125]),
                   P('b', '{b} codes have no 5.', [64]),
                   P('c', '{b} codes have at least one 5.', [61])],
            hint='Count the codes with no 5. Take them from the total.', beyond='Count the opposite'))
I.append(IT(U, 'G', 2, 5,
            'This code checks every pair of numbers a and b. Predict what it says.',
            f'The outer and inner repeats each run 4 times, so 4 {X} 4 = 16 pairs are checked. a {X} b is odd only when both a and b are odd: 2 {X} 2 = 4 pairs (1 and 3 with 1 and 3). '
            f'So 16 − 4 = 12 pairs have an even product. With 6 and 6: 36 pairs, 3 {X} 3 = 9 odd, 27 even.',
            fig=code([['var', 'set count to (0)'], ['var', 'set a to (1)'],
                      ['ctl', 'repeat (4)', [['var', 'set b to (1)'],
                                             ['ctl', 'repeat (4)', [['ctl', f'if <(a {X} b mod 2) = (0)> then', [['var', 'change count by (1)']]], ['var', 'change b by (1)']]],
                                             ['var', 'change a by (1)']]],
                      ['look', 'say (count)']]),
            parts=[P('a', 'It checks {b} pairs.', [16]),
                   P('b', 'It says {b}.', [12]),
                   P('c', 'Both repeats change to 6. It says {b}.', [27])],
            hint='When is a × b odd? Count those pairs first.', figside=True))
I.append(IT(U, 'G', 3, 5,
            'A child climbs a staircase. Each move goes up 1 step or 2 steps. Count the ways to reach the top.',
            '3 steps: 1+1+1, 1+2, 2+1 is 3 ways. The last move onto step n is 1 step from step n − 1 or 2 steps from step n − 2, so ways(n) = ways(n − 1) + ways(n − 2). '
            'Ways for 1, 2, 3, 4, 5, 6, 7, 8 steps: 1, 2, 3, 5, 8, 13, 21, 34. So 4 steps: 5, 6 steps: 13, 8 steps: 34.',
            parts=[P('a', '3 steps: {b} ways.', [3]),
                   P('b', '4 steps: {b} ways.', [5]),
                   P('c', '6 steps: {b} ways.', [13]),
                   P('d', '8 steps: {b} ways.', [34])],
            hint='Look at the last move. It was 1 step or 2 steps.', partsrow=True, beyond='A counting chain'))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            'A cafe has 5 soups and 3 breads. A meal is 1 soup and 1 bread. There are {b} different meals.',
            f'Choices one after another multiply: 5 {X} 3 = 15.',
            answer=A([15], '15')))
I.append(IT(U, 'C', 2, 6,
            'In a league of 5 teams, each team meets each of the others at home and away. There are {b} matches.',
            f'Each of the 5 teams plays 4 other teams at home: 5 {X} 4 = 20 matches. (Each pair is counted once for home and once for away.)',
            answer=A([20], '20')))
I.append(IT(U, 'C', 3, 6,
            'Cards 2, 5 and 8 make 3-digit numbers when each card is used once. How many numbers? {b}',
            f'3 choices, then 2, then 1: 3 {X} 2 {X} 1 = 6 (258, 285, 528, 582, 825, 852).',
            answer=A([6], '6')))
I.append(IT(U, 'C', 4, 6,
            'A code is 2 letters from A to E, then 1 digit from 1 to 4. Letters and digits may repeat. There are {b} codes.',
            f'5 {X} 5 {X} 4 = 100.',
            answer=A([100], '100')))

write_unit(5, 'Every possible way', 'Counting',
           'I can count every possible case without missing one or counting one twice. I can use multiplication for choices made one after another.', learn, I)
