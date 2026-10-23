"""Level 6 Unit 3: Below zero (negative numbers).  Follows holiday lesson 3."""
from lib import *

U = 'L6U03'
I = []
M = '−'     # the minus sign

learn = {
    'intro': 'Numbers below 0 have a minus sign. On a number line, greater numbers are to the right. To add, jump right. To subtract, jump left. '
             'When a jump crosses 0, split it at 0.',
    'example': {
        'problem': f'It is {M}5 °C at 6 a.m. By noon it rises 9 degrees. By night it falls 12 degrees. What is the temperature at night?',
        'figure': {'type': 'l6_nline', 'lo': -10, 'hi': 6, 'mm': 8, 'every': 2, 'marks': [{'at': -5, 'lab': '6 a.m.'}],
                   'jumps': [{'a': -5, 'b': 4, 'lab': '+9'}, {'a': 4, 'b': -8, 'lab': f'{M}12', 'below': True}], 'unit': '°C'},
        'steps': [f'Start at {M}5. Rising moves right. 5 steps reach 0, then 4 more steps: 4 °C at noon.',
                  'Falling moves left. From 4, 4 steps reach 0, then 8 more steps.',
                  f'The night temperature is {M}8 °C.',
                  f'Check by adding: {M}5 + 9 {M} 12 = {M}8.'],
        'answer': f'The temperature at night is {M}8 °C.'},
    'howto': {'title': 'How to add and subtract with negative numbers',
              'steps': ['Mark the start on the number line.',
                        'Adding moves right. Subtracting moves left.',
                        'If the jump crosses 0, split it at 0.',
                        'Check by jumping back to the start.']},
    'try': IT(U, 'L', 1, 0, f'It is {M}2 °C. It falls 7 degrees. What is the temperature now? {{b}} °C',
              f'Falling moves left. From {M}2 jump left 7 steps: {M}2 + ({M}7) = {M}9. Check: from {M}9 jump right 7 to reach {M}2.',
              answer=A([-9], f'{M}9')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'Put the numbers in order. Begin with the smallest.',
            f'The smallest number is the furthest left on the number line: {M}11, {M}6, {M}3, 0, 2, 8. '
            f'(b) On the number line, the number on the right is greater. {M}4 is to the right of {M}10, 0 is right of {M}2, and {M}15 is left of 1.',
            parts=[P('a', f'2, {M}6, {M}11, 0, {M}3, 8  gives  {{ll}}', [-11, -6, -3, 0, 2, 8], f'{M}11, {M}6, {M}3, 0, 2, 8', list=True),
                   P('b', f'Circle > or <:   {M}4  {{circ:>|<}}  {M}10        0  {{circ:>|<}}  {M}2        {M}15  {{circ:>|<}}  1', ['>', '>', '<'], '>, >, <')]))
I.append(IT(U, 'S', 2, 1,
            'Read the number line. Each mark is 1 step.',
            f'The labelled numbers are every 2 steps. A is 1 step right of {M}10, so {M}9. B is 1 step left of {M}2, so {M}3. C is 1 step left of 6, so 5. '
            f'From {M}9 to {M}3 is 6 steps and from {M}3 to 5 is 8 steps (3 steps to 0, then 5 more).',
            fig={'type': 'l6_nline', 'lo': -12, 'hi': 8, 'mm': 7, 'every': 2, 'marks': [{'at': -9, 'lab': 'A'}, {'at': -3, 'lab': 'B'}, {'at': 5, 'lab': 'C'}]},
            parts=[P('a', f'A = {{b}}   B = {{b}}   C = {{b}}', [-9, -3, 5], f'{M}9, {M}3, 5'),
                   P('b', 'From A to B is {b} steps. From B to C is {b} steps.', [6, 8], '6, 8')]))
I.append(IT(U, 'S', 3, 1,
            'The thermometer shows 3 readings on one day.',
            f'Read each mark: 6 a.m. is {M}6 °C, noon is 4 °C and 9 p.m. is {M}3 °C. From {M}6 up to 4 is 6 steps to 0 and 4 more: 10 degrees. '
            f'From 4 down to {M}3 is 4 steps to 0 and 3 more: 7 degrees.',
            fig={'type': 'l6_vline', 'lo': -8, 'hi': 6, 'mm': 6.5, 'marks': [{'at': -6, 'lab': '6 a.m.'}, {'at': 4, 'lab': 'noon'}, {'at': -3, 'lab': '9 p.m.'}], 'title': '°C'},
            parts=[P('a', 'At 6 a.m.: {b} °C', [-6], f'{M}6'),
                   P('b', 'At noon: {b} °C', [4]),
                   P('c', 'At 9 p.m.: {b} °C', [-3], f'{M}3'),
                   P('d', 'From 6 a.m. to noon it rose {b} degrees.', [10]),
                   P('e', 'From noon to 9 p.m. it fell {b} degrees.', [7])],
            figside=True))
I.append(IT(U, 'S', 4, 2,
            'Find the value of each one. Use a number line to help.',
            f'(a) From {M}6 jump right 10: 4 steps to 0, then 6 more: 4. (b) From 3 jump left 9: 3 steps to 0, then 6 more: {M}6. '
            f'(c) From {M}7 jump left 5: {M}12. (d) From {M}4 jump right 15: 4 steps to 0, then 11 more: 11.',
            parts=[P('a', f'{M}6 + 10 = {{b}}', [4]),
                   P('b', f'3 {M} 9 = {{b}}', [-6], f'{M}6'),
                   P('c', f'{M}7 {M} 5 = {{b}}', [-12], f'{M}12'),
                   P('d', f'{M}4 + 15 = {{b}}', [11])],
            partsrow=True))
I.append(IT(U, 'S', 5, 2,
            'Find the missing number.',
            f'(a) From {M}5 to 6 is 5 steps to 0 and 6 more: 11. (b) 4 {M} 7 = {M}3, so 7. (c) {M}6 + 8 = 2, so the missing number is {M}6. '
            f'(d) {M}4 {M} 5 = {M}9, so the missing number is {M}4.',
            parts=[P('a', f'{M}5 + {{b}} = 6', [11]),
                   P('b', f'4 {M} {{b}} = {M}3', [7]),
                   P('c', f'{{b}} + 8 = 2', [-6], f'{M}6'),
                   P('d', f'{{b}} {M} 5 = {M}9', [-4], f'{M}4')],
            partsrow=True))
I.append(IT(U, 'S', 6, 2,
            'How far is it from the first number to the second? Count the steps, splitting at 0.',
            f'(a) From {M}9 to 4: 9 steps to 0 and 4 more is 13. (b) From {M}6 to {M}1: 5 steps, no need to cross 0. '
            f'(c) From {M}14 to 31: 14 steps to 0 and 31 more is 45.',
            parts=[P('a', f'{M}9 to 4:  {{b}} steps', [13]),
                   P('b', f'{M}6 to {M}1:  {{b}} steps', [5]),
                   P('c', f'{M}14 °C to 31 °C:  {{b}} degrees', [45])],
            partsrow=True))
I.append(IT(U, 'S', 7, 2,
            'Trace the code. The sprite changes x, then says it.',
            f'x starts at 60. Loop 1: 60 {M} 25 = 35. Loop 2: 10. Loop 3: {M}15. Loop 4: {M}40. Loop 5: {M}65. '
            f'The 3rd number said is {M}15. The last is {M}65. The numbers below 0 are {M}15, {M}40 and {M}65: 3 of them.',
            fig=code([['var', 'set x to (60)'], ['ctl', 'repeat (5)', [['var', f'change x by ({M}25)'], ['look', 'say (x) for (1) seconds']]]],
                     trace={'cols': ['Loop', 'x said'], 'rows': 5, 'first': [1, 2, 3, 4, 5], 'cw': 24, 'ch': 8}),
            parts=[P('a', 'The 3rd number it says is {b}.', [-15], f'{M}15'),
                   P('b', 'The last number it says is {b}.', [-65], f'{M}65'),
                   P('c', 'It says {b} numbers that are below 0.', [3])],
            partsrow=True))
I.append(IT(U, 'S', 8, 2,
            'A sprite starts at x = 100. Fill in the blocks.',
            f'(a) 4 equal moves must go from 100 down to 0. That is 100 left in 4 moves, so each move is {M}25. '
            f'(b) 8 moves of {M}20 make {M}160, and 100 {M} 160 = {M}60.',
            fig=code([HAT, ['var', 'set x to (100)'], ['ctl', 'repeat (4)', [['var', 'change x by ( )']]]]),
            parts=[P('a', 'It ends at x = 0. change x by {b}', [-25], f'{M}25'),
                   P('b', f'With repeat 8 and change x by ({M}20), it ends at x = {{b}}.', [-60], f'{M}60')],
            figside=True))
I.append(IT(U, 'S', 9, 3,
            f'A balance of {M}15 dollars means Ali owes 15 dollars. Ali has 25 dollars.',
            f'(a) 25 {M} 40 = {M}15. (b) {M}15 + 30 = 15. (c) From {M}15 up to 20: 15 dollars to reach 0, then 20 more, 35 dollars.',
            parts=[P('a', 'He buys a game for 40 dollars. His balance is {b} dollars.', [-15], f'{M}15'),
                   P('b', 'Then he is given 30 dollars. His balance is {b} dollars.', [15]),
                   P('c', f'To go from {M}15 dollars up to 20 dollars, he needs {{b}} dollars.', [35])]))
I.append(IT(U, 'S', 10, 3,
            'In a car park the floors are L3, L2, L1, B1, B2 and B3. There is no floor 0. Count the floors one by one.',
            '(a) L3, L2, L1, B1, B2: that is 4 moves down. (b) B3, B2, B1, L1: 3 moves up. (c) L2, L1, B1: 2 moves down. '
            'A number line with 0 would give one move too many.',
            fig=grid([['L3', 'L2', 'L1', 'B1', 'B2', 'B3']], [17] * 6, ch=10),
            parts=[P('a', 'A car goes down from L3 to B2: {b} floors.', [4]),
                   P('b', 'A car goes up from B3 to L1: {b} floors.', [3]),
                   P('c', 'A car goes down from L2 to B1: {b} floors.', [2])]))
I.append(IT(U, 'S', 11, 3,
            'Think about how far each number is from 0.',
            f'(a) The distances from 0 are 9, 5, 3, 7 and 4. {M}3 is only 3 steps from 0. (b) {M}8 is 8 steps from 0 and 6 is 6 steps from 0, so {M}8 is further.',
            parts=[P('a', f'Circle the number closest to 0:   {M}9    5    {M}3    7    {M}4', [-3], f'{M}3'),
                   P('b', f'Which is further from 0?   {{circ:{M}8|6}}', [-8], f'{M}8')]))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            f'Beyond Level 6: Subtracting a negative number.\nTo find 6 {M} ({M}4), count the steps from {M}4 up to 6.',
            f'(a) 6 {M} ({M}4): from {M}4 to 6 is 10 steps. (b) {M}2 {M} ({M}5): from {M}5 to {M}2 is 3 steps. '
            f'(c) In both, subtracting a negative number gave the same answer as adding the matching positive number: 6 + 4 and {M}2 + 5.',
            parts=[P('a', f'6 {M} ({M}4) = {{b}}', [10]),
                   P('b', f'{M}2 {M} ({M}5) = {{b}}', [3]),
                   P('c', f'So taking away {M}4 gives the same result as adding {{b}}.', [4])],
            hint='How far is it from the second number up to the first number?', partsrow=True, space={'rows': ['Number line:', '']}))
I.append(IT(U, 'T', 2, 4,
            f'A sprite starts at x = {M}90. The loop stops as soon as x is greater than 40 at the start of a repeat.',
            f'Each repeat changes x by 35 {M} 10 = 25. After the repeats x is {M}65, {M}40, {M}15, 10, 35, 60. After 5 repeats x = 35, which is not greater than 40, so it repeats a 6th time. '
            f'It stops with x = 60.',
            fig=code([['var', f'set x to ({M}90)'], ['ctl', 'repeat until <(x) {gt} (40)>', [['var', 'change x by (35)'], ['var', f'change x by ({M}10)']]], ['look', 'say (x)']]),
            parts=[P('a', 'The loop repeats {b} times.', [6]),
                   P('b', 'The sprite says {b}.', [60])],
            hint='Write x after each repeat. Is it more than 40 yet?', figside=True))
I.append(IT(U, 'T', 3, 4,
            f'On Monday at noon it was 3 °C. On Tuesday it was 11 degrees colder than Monday. On Wednesday it was 6 degrees warmer than Tuesday. On Thursday it was {M}4 °C.',
            f'Tuesday: 3 {M} 11 = {M}8. Wednesday: {M}8 + 6 = {M}2. Thursday is {M}4, which is 2 below Wednesday. From Monday (3) to Thursday ({M}4): 3 steps to 0 and 4 more, so it fell 7 degrees.',
            parts=[P('a', 'Tuesday: {b} °C', [-8], f'{M}8'),
                   P('b', 'Wednesday: {b} °C', [-2], f'{M}2'),
                   P('c', 'From Monday to Thursday it fell {b} degrees.', [7])],
            hint='Draw a number line. Mark Monday first, then each change.', partsrow=True, space={'rows': ['Number line:', '']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            f'Two divers: A is at {M}12 m and goes down 4 m every minute. B is at {M}40 m and comes up 6 m every minute.',
            f'After 3 minutes A is at {M}12 {M} 12 = {M}24 and B is at {M}40 + 18 = {M}22. B is now above A. After 2 minutes A is {M}20 and B is {M}28, so B is still below. '
            f'After 5 minutes A is {M}32 and B is {M}10: the gap is 22 m.',
            parts=[P('a', 'After 3 minutes, A is at {b} m and B is at {b} m.', [-24, -22], f'{M}24, {M}22'),
                   P('b', 'B is first above A after minute {b}.', [3]),
                   P('c', 'After 5 minutes they are {b} m apart.', [22])],
            hint='Make a table: minute, depth of A, depth of B.', partsrow=True, space={'rows': ['Working:', '']}))
I.append(IT(U, 'G', 2, 5,
            'This code uses a and b. Run it for each pair of numbers.',
            f'It says how far apart a and b are. a = {M}8 and b = 5: a is not greater, so it says 5 {M} ({M}8) = 13. a = {M}3 and b = {M}9: a is greater, so it says {M}3 {M} ({M}9) = 6. '
            'The program always says the gap between a and b, whichever is greater.',
            fig=code([['ctl', 'if <(a) {gt} (b)> then', [['look', 'say (a − b)']], [['look', 'say (b − a)']]]]),
            parts=[P('a', f'a = {M}8 and b = 5. It says {{b}}.', [13]),
                   P('b', f'a = {M}3 and b = {M}9. It says {{b}}.', [6]),
                   P('c', f'a = {M}6 and b = {M}6. It says {{b}}.', [0])],
            hint='Is a greater than b? Choose the right branch first.', figside=True))
I.append(IT(U, 'G', 3, 5,
            'There is no year 0. The year after 1 BC is AD 1. Count the years one by one.',
            '(a) 5 BC, 4 BC, 3 BC, 2 BC, 1 BC: 4 steps. (b) 3 BC to 2 BC, 1 BC, AD 1, AD 2, AD 3, AD 4: 6 steps. '
            '(c) 10 BC to 1 BC is 9 steps, 1 step to AD 1, then 11 steps to AD 12: 21 years.',
            parts=[P('a', 'From 5 BC to 1 BC is {b} years.', [4]),
                   P('b', 'From 3 BC to AD 4 is {b} years.', [6]),
                   P('c', 'A person born in 10 BC dies in AD 12. They are {b} years old.', [21])],
            hint='A number line with 0 would be 1 step too short.', beyond='A calendar with no year 0', partsrow=True, space={'rows': ['Working:', '']}))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            f'{M}9 + 14 = {{b}}     6 {M} 13 = {{b}}',
            f'From {M}9 jump right 14: 9 steps to 0 and 5 more is 5. From 6 jump left 13: 6 steps to 0 and 7 more is {M}7.',
            answer=A([5, -7], f'5, {M}7')))
I.append(IT(U, 'C', 2, 6,
            f'Put in order, smallest first:  4, {M}7, {M}2, 0  {{ll}}',
            f'On a number line, from left to right: {M}7, {M}2, 0, 4.',
            answer=A([-7, -2, 0, 4], f'{M}7, {M}2, 0, 4', list=True)))
I.append(IT(U, 'C', 3, 6,
            f'It is {M}6 °C. It rises 11 degrees, then falls 8 degrees. It is now {{b}} °C.',
            f'{M}6 + 11 = 5. Then 5 {M} 8 = {M}3.',
            answer=A([-3], f'{M}3')))
I.append(IT(U, 'C', 4, 6,
            f'A sprite starts at x = 20. It runs repeat 3 [change x by {M}15]. Then x = {{b}}.',
            f'3 moves of {M}15 make {M}45. 20 {M} 45 = {M}25.',
            answer=A([-25], f'{M}25')))

learn['tight'] = True
write_unit(3, 'Below zero', 'Negative numbers',
           'I can order negative numbers and add and subtract by jumping along a number line. I can follow a variable that goes below 0 in code.', learn, I)
