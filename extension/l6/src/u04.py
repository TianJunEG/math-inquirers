"""Level 6 Unit 4: Algebra machines (rules with a letter, running machines backwards, simple equations).  Follows holiday lesson 4."""
from lib import *

U = 'L6U04'
I = []
M = '−'
X = '×'

learn = {
    'intro': 'A number machine follows a rule: IN goes in and OUT comes out. We write the rule with a letter, such as OUT = 4n + 3. '
             'To find the IN for a given OUT, run the machine backwards and undo the last step first.',
    'example': {
        'problem': f'A machine does {X} 7, then {M} 4. OUT is 45. What was IN?',
        'figure': {'type': 'l6_machine', 'chain': ['n', f'{X} 7', '', f'{M} 4', '45'], 'undo': [f'÷ 7', '+ 4']},
        'steps': [f'The rule is OUT = 7n {M} 4, so 7n {M} 4 = 45.',
                  'Undo the last step first. Undo take away 4 by adding 4: 45 + 4 = 49.',
                  f'Then undo {X} 7 by dividing by 7: 49 ÷ 7 = 7.',
                  f'Check forwards: 7 {X} 7 = 49, then 49 {M} 4 = 45.'],
        'answer': 'IN was 7.'},
    'howto': {'title': 'How to run a machine backwards',
              'steps': ['Write the steps in order, from IN to OUT.',
                        'Start at OUT. Undo the last step first.',
                        f'Use the opposite step: + undoes {M}, and {X} undoes ÷.',
                        'Check by running the machine forwards.']},
    'try': IT(U, 'L', 1, 0, f'A machine does {X} 4, then + 9. OUT is 41. What was IN? {{b}}',
              f'Undo the last step first: 41 {M} 9 = 32. Then undo {X} 4: 32 ÷ 4 = 8. Check: 8 {X} 4 + 9 = 41.',
              answer=A([8], '8')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'Guess my rule. The rule is: multiply n by a number, then add a number.',
            f'IN goes up by 2 each time and OUT goes up by 6, so each 1 of IN adds 3: the rule has {X} 3. 3 {X} 1 = 3, but OUT is 5, so add 2: OUT = 3n + 2. '
            f'Check IN 7: 3 {X} 7 + 2 = 23. IN 10 gives 32. For OUT 50: 3n = 48 and n = 16.',
            fig=grid([['IN', '1', '3', '5', '7'], ['OUT', '5', '11', '17', '23']], [22, 18, 18, 18, 18], rowhead=True, ch=10),
            parts=[P('a', f'OUT = {{b}} {X} n + {{b}}', [3, 2], '3, 2'),
                   P('b', 'IN 10 gives OUT {b}.', [32]),
                   P('c', 'OUT 50 comes from IN {b}.', [16])],
            partsrow=True))
I.append(IT(U, 'S', 2, 1,
            'Guess my rule. This time the machine takes a number away.',
            f'IN goes up by 2 and OUT goes up by 6, so the rule has {X} 3. 3 {X} 2 = 6, but OUT is 1, so take away 5: OUT = 3n {M} 5. '
            f'IN 20 gives 3 {X} 20 {M} 5 = 55. For OUT 100: 3n {M} 5 = 100, so 3n = 105 and n = 35.',
            fig=grid([['IN', '2', '4', '6', '8'], ['OUT', '1', '7', '13', '19']], [22, 18, 18, 18, 18], rowhead=True, ch=10),
            parts=[P('a', f'OUT = {{b}} {X} n {M} {{b}}', [3, 5], '3, 5'),
                   P('b', 'IN 20 gives OUT {b}.', [55]),
                   P('c', 'OUT 100 comes from IN {b}.', [35])],
            partsrow=True))
I.append(IT(U, 'S', 3, 1,
            f'Machine P does {X} 2, then + 6. Machine Q does + 6, then {X} 2. Use the same IN for both.',
            f'IN 7: P gives 7 {X} 2 = 14, then 20. Q gives 7 + 6 = 13, then 26. IN 10: P gives 26 and Q gives 32. '
            f'The order of the steps matters, so P and Q do not give the same OUT.',
            parts=[P('a', 'IN 7:  P gives {b}  and Q gives {b}.', [20, 26], '20, 26'),
                   P('b', 'IN 10:  P gives {b}  and Q gives {b}.', [26, 32], '26, 32'),
                   P('c', 'Do P and Q give the same OUT?   {circ:Yes|No}', ['No'])]))
I.append(IT(U, 'S', 4, 1,
            'A machine does two steps. Look at the first IN and OUT.',
            f'IN 5 times 3 is 15, so the middle box is 15. 15 + 4 = 19, so the last step is add 4. IN 9: 9 {X} 3 = 27, then 27 + 4 = 31.',
            fig={'type': 'l6_machine', 'chain': ['5', f'{X} 3', '', '+ ?', '19']},
            parts=[P('a', 'The middle box is {b}.', [15]),
                   P('b', 'The last step is add {b}.', [4]),
                   P('c', 'IN 9 gives OUT {b}.', [31])],
            partsrow=True))
I.append(IT(U, 'S', 5, 2,
            'Run each machine backwards to find n. Check by going forwards.',
            f'(a) 5n + 8 = 63: 63 {M} 8 = 55, 55 ÷ 5 = 11. (b) 9n {M} 7 = 74: 74 + 7 = 81, 81 ÷ 9 = 9. (c) (n + 4) {X} 6 = 66: 66 ÷ 6 = 11, 11 {M} 4 = 7. '
            f'(d) n ÷ 5 + 3 = 11: 11 {M} 3 = 8, 8 {X} 5 = 40.',
            parts=[P('a', f'5n + 8 = 63      n = {{b}}', [11]),
                   P('b', f'9n {M} 7 = 74      n = {{b}}', [9]),
                   P('c', f'(n + 4) {X} 6 = 66      n = {{b}}', [7]),
                   P('d', f'n ÷ 5 + 3 = 11      n = {{b}}', [40])],
            partsrow=True))
I.append(IT(U, 'S', 6, 2,
            f'The block "answer" holds the number you type. In code, {X} means times. Predict what the sprite says.',
            f'out = answer {X} 4 {M} 3. Type 9: 36 {M} 3 = 33. Type 25: 100 {M} 3 = 97. For 61, run it backwards: 61 + 3 = 64, then 64 ÷ 4 = 16.',
            fig=code([HAT, ['look', 'ask (IN?) and wait'], ['var', f'set out to (answer {X} 4 {M} 3)'], ['look', 'say (out)']]),
            parts=[P('a', 'You type 9. It says {b}.', [33]),
                   P('b', 'You type 25. It says {b}.', [97]),
                   P('c', 'It says 61. You typed {b}.', [16])],
            figside=True))
I.append(IT(U, 'S', 7, 2,
            f'Plan a search. Find n when 7n {M} 4 = 73 by trying n = 0, 1, 2, ... Fill in the blanks.',
            f'The search starts at 0 and adds 1 each time, until 7 {X} n {M} 4 is 73. 7 {X} 10 {M} 4 = 66 is too small and 7 {X} 11 {M} 4 = 73. It says 11. '
            f'Check backwards: 73 + 4 = 77 and 77 ÷ 7 = 11.',
            fig=code([['var', 'set n to ( )'], ['ctl', f'repeat until <(n {X} 7 {M} 4) = ( )>', [['var', 'change n by ( )']]], ['look', 'say (n)']]),
            parts=[P('a', 'set n to {b}', [0]),
                   P('b', 'repeat until it is {b}', [73]),
                   P('c', 'change n by {b}', [1]),
                   P('d', 'It says {b}.', [11])],
            figside=True))
I.append(IT(U, 'S', 8, 3,
            'Ali has n stickers. Mei has 5 more than Ali. Wei has 3 times as many as Ali.',
            f'Mei has n + 5 and Wei has 3 {X} n. When n = 8: Mei has 13, Wei has 24, and all 3 together have 8 + 13 + 24 = 45. '
            f'In general n + (n + 5) + 3n = 5n + 5.',
            parts=[P('a', 'When n = 8, Mei has {b} and Wei has {b}.', [13, 24], '13, 24'),
                   P('b', 'When n = 8, all 3 together have {b} stickers.', [45]),
                   P('c', f'All 3 together have {{b}} {X} n + {{b}} stickers.', [5, 5], '5, 5')]))
I.append(IT(U, 'S', 9, 3,
            'A phone plan costs 12 dollars a month, plus 3 dollars for each extra GB. n is the number of extra GB.',
            f'Cost = 3 {X} n + 12. 5 extra GB cost 3 {X} 5 + 12 = 27 dollars. For 60 dollars: 3n + 12 = 60, so 3n = 48 and n = 16.',
            parts=[P('a', '5 extra GB cost {b} dollars.', [27]),
                   P('b', f'The cost is {{b}} {X} n + {{b}} dollars.', [3, 12], '3, 12'),
                   P('c', 'With 60 dollars you can buy {b} extra GB.', [16])]))
I.append(IT(U, 'S', 10, 3,
            'Think of a number. Add 4. Multiply by 3. Take away 9. Divide by 3. Take away the number you first thought of.',
            f'Start with 7: 11, 33, 24, 8, then 8 {M} 7 = 1. Start with 12: 16, 48, 39, 13, then 13 {M} 12 = 1. With n the steps give n + 4, 3n + 12, 3n + 3, n + 1, and n + 1 {M} n = 1. '
            f'The answer is always 1.',
            parts=[P('a', 'Start with 7. You get {b}.', [1]),
                   P('b', 'Start with 12. You get {b}.', [1]),
                   P('c', f'Start with n. The steps give n + 4, 3n + 12, 3n + 3, n + 1, then {{b}}.', [1])]))
I.append(IT(U, 'S', 11, 3,
            'Predict what the sprite says.',
            f'6 is not more than 10, so it says 6 {X} 2 = 12. 15 is more than 10, so it says 15 {M} 10 = 5. For 8: the first branch gives answer {M} 10 = 8 when answer = 18, '
            f'and the second gives answer {X} 2 = 8 when answer = 4. Two numbers work.',
            fig=code([HAT, ['look', 'ask (IN?) and wait'], ['ctl', 'if <(answer) {gt} (10)> then', [['look', f'say (answer {M} 10)']], [['look', f'say (answer {X} 2)']]]]),
            parts=[P('a', 'You type 6. It says {b}.', [12]),
                   P('b', 'You type 15. It says {b}.', [5]),
                   P('c', 'Two different numbers make it say 8. They are {b} and {b}.', [4, 18], '4 and 18')],
            figside=True))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            f'Machine X does {X} 2, then + 3. Its OUT goes straight into Machine Y, which does {X} 3, then {M} 4.',
            f'IN 5: X gives 13, Y gives 39 {M} 4 = 35. For OUT 77, undo Y: 77 + 4 = 81, 81 ÷ 3 = 27. Undo X: 27 {M} 3 = 24, 24 ÷ 2 = 12. '
            f'The joined rule is 3(2n + 3) {M} 4 = 6n + 5. Check: 6 {X} 5 + 5 = 35 and 6 {X} 12 + 5 = 77.',
            parts=[P('a', 'IN 5 gives OUT {b}.', [35]),
                   P('b', 'OUT 77 comes from IN {b}.', [12]),
                   P('c', f'Joined, the rule is OUT = {{b}} {X} n + {{b}}.', [6, 5], '6, 5')],
            hint='For OUT 77, undo Y first, then undo X.', partsrow=True, space={'rows': ['Working:', '']}))
I.append(IT(U, 'T', 2, 4,
            'Ali is n years old. His brother is 4 years older. Their mother is 3 times as old as Ali. Together the 3 of them are 64 years old.',
            f'Ali n, brother n + 4, mother 3n. Together: n + (n + 4) + 3n = 5n + 4 = 64. So 5n = 60 and n = 12. Ali is 12, his brother is 16 and their mother is 36. Check: 12 + 16 + 36 = 64.',
            fig={'type': 'l6_model', 'rows': [{'label': 'Ali', 'segs': [{'w': 18, 't': 'n'}]},
                                              {'label': 'Brother', 'segs': [{'w': 18, 't': 'n'}, {'w': 10, 't': '4', 'dash': True}]},
                                              {'label': 'Mother', 'segs': [{'w': 18, 't': 'n'}, {'w': 18, 't': 'n'}, {'w': 18, 't': 'n'}]}],
                 'brace': {'t': '64 in all'}},
            parts=[P('a', f'Together: {{b}} {X} n + {{b}} = 64', [5, 4], '5, 4'),
                   P('b', 'Ali is {b} years old.', [12]),
                   P('c', 'Their mother is {b} years old.', [36])],
            hint='Add up the n boxes first. Then add the extra 4.', figside=True))
I.append(IT(U, 'T', 3, 4,
            f'A machine does {X} a number, then + or {M} a number. IN 3 gives OUT 13. IN 8 gives OUT 38.',
            f'IN goes up 5 (3 to 8) and OUT goes up 25 (13 to 38), so the {X} part is 25 ÷ 5 = 5. 5 {X} 3 = 15, but OUT is 13, so take away 2: OUT = 5n {M} 2. '
            f'For OUT 98: 5n = 100 and n = 20.',
            parts=[P('a', 'When IN goes up by 5, OUT goes up by {b}.', [25]),
                   P('b', f'The rule is OUT = {{b}} {X} n {M} {{b}}.', [5, 2], '5, 2'),
                   P('c', 'OUT 98 comes from IN {b}.', [20])],
            hint='How much does OUT go up for each 1 that IN goes up?', partsrow=True, space={'rows': ['Working:', '']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            f'Beyond Level 6: n on both sides.\nMachine A does {X} 4, then + 1. Machine B does {X} 2, then + 13. Is there an IN that gives the same OUT on both?',
            f'IN 2: A gives 9 and B gives 17, so B is ahead by 8. A gains 2 on B for every 1 that IN goes up (4 {M} 2 = 2). B\'s lead of 8 is gone after 4 more steps, at IN 6. '
            f'Both give 25: 4 {X} 6 + 1 = 25 and 2 {X} 6 + 13 = 25. As an equation, 4n + 1 = 2n + 13 gives 2n = 12.',
            parts=[P('a', 'IN 2: A gives {b} and B gives {b}.', [9, 17], '9, 17'),
                   P('b', 'The OUT numbers are the same when IN is {b}.', [6]),
                   P('c', 'That OUT is {b}.', [25])],
            hint='Make a table of IN, A and B. Look at how the gap changes.', space={'table': {'cols': ['IN', 'A', 'B'], 'rows': 5}}))
I.append(IT(U, 'G', 2, 5,
            'Call the smallest number n.',
            f'(a) n + (n + 1) + (n + 2) + (n + 3) = 4n + 6 = 130, so 4n = 124 and n = 31 (31, 32, 33, 34). '
            f'(b) Odd numbers go up by 2: n + (n + 2) + (n + 4) + (n + 6) + (n + 8) = 5n + 20 = 125, so n = 21. '
            f'(c) 4n + 6 = 100 gives 4n = 94 and n = 23.5, which is not a whole number: No.',
            parts=[P('a', '4 whole numbers in a row add up to 130. The smallest is {b}.', [31]),
                   P('b', '5 odd numbers in a row add up to 125. The smallest is {b}.', [21]),
                   P('c', 'Can 4 whole numbers in a row add up to 100?   {circ:Yes|No}', ['No'])],
            hint='Write each number with n. Add them up.', space={'rows': ['Working:', '']}))
I.append(IT(U, 'G', 3, 5,
            f'A search program tries n = 0, 1, 2, ... It stops when 7n {M} 3 is greater than 120.',
            f'7n {M} 3 > 120 needs 7n > 123, so n > 17.57: n = 18 gives 123. It says 18, and OUT is 123. If 120 changes to 123, then 123 is not greater than 123, so it keeps going to n = 19.',
            fig=code([['var', 'set n to (0)'], ['ctl', f'repeat until <(n {X} 7 {M} 3) {{gt}} (120)>', [['var', 'change n by (1)']]], ['look', 'say (n)']]),
            parts=[P('a', 'It says {b}.', [18]),
                   P('b', 'When it stops, 7n − 3 is {b}.', [123]),
                   P('c', 'If 120 changes to 123, it says {b}.', [19])],
            hint='Is 7n − 3 greater than 120? Careful with equal.', figside=True))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            f'IN 1, 2, 3, 4 give OUT 6, 11, 16, 21. The rule is OUT = {{b}} {X} n + {{b}}.',
            f'OUT goes up 5 for each 1 of IN, so {X} 5. 5 {X} 1 = 5, and OUT is 6, so add 1: OUT = 5n + 1.',
            answer=A([5, 1], '5, 1')))
I.append(IT(U, 'C', 2, 6,
            f'A machine does {X} 6, then {M} 7. OUT is 41. IN = {{b}}',
            f'Undo {M} 7: 41 + 7 = 48. Undo {X} 6: 48 ÷ 6 = 8. Check: 8 {X} 6 {M} 7 = 41.',
            answer=A([8], '8')))
I.append(IT(U, 'C', 3, 6,
            f'4n + 9 = 57.  n = {{b}}',
            f'57 {M} 9 = 48. 48 ÷ 4 = 12. Check: 4 {X} 12 + 9 = 57.',
            answer=A([12], '12')))
I.append(IT(U, 'C', 4, 6,
            'Ali has n sweets. Mei has 4 more. Together they have 30. n = {b}',
            f'n + (n + 4) = 2n + 4 = 30. So 2n = 26 and n = 13. Check: 13 + 17 = 30.',
            answer=A([13], '13')))

write_unit(4, 'Algebra machines', 'Rules with a letter and simple equations',
           'I can find the rule of a number machine from a table and write it with a letter. I can run a machine backwards to solve an equation.', learn, I)
