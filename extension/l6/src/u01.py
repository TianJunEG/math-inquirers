"""Level 6 Unit 1: Code the pattern (sequences, the nth term, loops).  Follows holiday lesson 1."""
from lib import *

U = 'L6U01'
I = []

learn = {
    'intro': 'A rule for the nth term jumps straight to any term, such as the 100th. The difference tells you which times table to compare with. '
             'A loop in code adds the difference again and again, so you can test your rule.',
    'example': {
        'problem': 'A sequence begins 9, 14, 19, 24, ... Find the rule that gives term n. Then find the 100th term.',
        'figure': grid([['n', '1', '2', '3', '4'], ['5 × n', '5', '10', '15', '20'], ['term', '9', '14', '19', '24']], [26, 18, 18, 18, 18], rowhead=True),
        'steps': ['The difference is 5, so compare each term with the 5 times table.',
                  'Each term is 4 more than the number above it. The rule is 5n + 4.',
                  'Check the 4th term: 5 × 4 + 4 = 24. It matches.',
                  'The 100th term is 5 × 100 + 4 = 504.',
                  'Test it in code: set term to 9, then repeat 99 times: change term by 5. The 100th term is 99 jumps after the 1st term.'],
        'answer': 'The rule is 5n + 4. The 100th term is 504.'},
    'howto': {'title': 'How to find the rule for the nth term',
              'steps': ['Find the difference between neighbouring terms.',
                        'Write that times table under n: 5, 10, 15, ...',
                        'Find how much to add or take away to reach each term.',
                        'Check the rule on 2 terms. Then use it for any term.']},
    'try': IT(U, 'L', 1, 0, 'A sequence starts 3, 10, 17, 24, ...\nThe rule for the nth term is {b} \u00d7 n \u2212 {b}. The 100th term is {b}.',
              'The difference is 7, so compare with 7, 14, 21, 28. Each term is 4 less than the number under it. The rule is 7n \u2212 4. '
              'The 100th term is 7 \u00d7 100 \u2212 4 = 696.',
              answer=A([7, 4, 696], '7, 4, 696')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'Matchsticks make 2 rows of squares. Pattern 2 has 2 columns and pattern 3 has 3 columns.',
            'Count: pattern 1 has 7 sticks, pattern 2 has 12, pattern 3 has 17. Each new column adds 5 sticks, so the rule is 5n + 2 (5 × 1 + 2 = 7). '
            'Pattern 40: 5 × 40 + 2 = 202. For 92 sticks: 5n + 2 = 92, so 5n = 90 and n = 18.',
            fig={'type': 'l6_sticks', 'shape': 'sq', 'rows': 2, 'ks': [1, 2, 3], 'side': 9},
            parts=[P('a', 'Pattern 3 has {b} sticks. Each new column adds {b} sticks.', [17, 5], '17, 5'),
                   P('b', 'The rule: sticks = {b} × n + {b}', [5, 2], '5, 2'),
                   P('c', 'Pattern 40 has {b} sticks.', [202]),
                   P('d', 'Pattern {b} has 92 sticks.', [18])],
            figright=True, partsrow=True))
I.append(IT(U, 'S', 2, 1,
            'Complete the table for each sequence.',
            '(a) The difference is 6. Compare with 6, 12, 18, 24: each term is 2 more, so 6n + 2 and 6 × 100 + 2 = 602. '
            '(b) The difference is 5. Each term is 2 less than 5, 10, 15, 20, so 5n − 2 and 5 × 100 − 2 = 498.',
            answer=A(['6', '6n + 2', '602', '5', '5n - 2', '498'], '(a) 6, 6n + 2, 602   (b) 5, 5n − 2, 498', list=True),
            fig=grid([['(a) 8, 14, 20, 26, ...', '', '', ''], ['(b) 3, 8, 13, 18, ...', '', '', '']], [50, 25, 38, 24],
                     head=['Sequence', 'Difference', 'Rule for term n', 'Term 100'], ch=10)))
I.append(IT(U, 'S', 3, 1,
            'A sequence has the rule 5n + 2. Its first terms are 7, 12, 17, 22, ...',
            '(a) 157 − 2 = 155 = 5 × 31, so 157 is the 31st term. (b) 205 − 2 = 203 is not a multiple of 5. The terms end in 2 or 7, so 205 is not one. '
            '(c) 5 × 60 + 2 = 302.',
            parts=[P('a', 'Is 157 a term?  {circ:Yes|No}   If yes, it is term number {b}.', ['Yes', 31], 'Yes, term 31'),
                   P('b', 'Is 205 a term?  {circ:Yes|No}', ['No']),
                   P('c', 'The 60th term is {b}.', [302])]))
I.append(IT(U, 'S', 4, 1,
            'Trace the code. The sprite says x first, then changes it. Fill in the trace table. The key to the code blocks is on page 27.',
            'Loop 1: it says 3, then x becomes 9. Loop 2: says 9, x becomes 15. Loop 3: says 15, x becomes 21. Loop 4: says 21, x becomes 27. '
            'The last number said is 21 but x ends as 27. With repeat 50 it says the 1st term, then 49 jumps later it says 3 + 49 × 6 = 297.',
            fig=code([HAT, ['var', 'set x to (3)'], ['ctl', 'repeat (4)', [['look', 'say (x) for (1) seconds'], ['var', 'change x by (6)']]]],
                     trace={'cols': ['Loop', 'x said', 'x after'], 'rows': 4, 'first': [1, 2, 3, 4], 'cw': 21}),
            parts=[P('a', 'The last number it says is {b}.', [21]),
                   P('b', 'With repeat 50, the last number it says is {b}.', [297])],
            partsrow=True))
I.append(IT(U, 'S', 5, 2,
            'Complete the code so that the sprite says the first 15 terms of 11, 18, 25, 32, ...',
            'The 1st term is 11, so set n to 11. Each jump adds 7. The sprite says a term, then changes n, and 15 terms need 15 says: repeat 15. '
            'The last number said is the 15th term: 7 × 15 + 4 = 109.',
            fig=code([HAT, ['var', 'set n to ( )'], ['ctl', 'repeat ( )', [['look', 'say (n) for (1) seconds'], ['var', 'change n by ( )']]]]),
            parts=[P('a', 'set n to {b}', [11]),
                   P('b', 'repeat {b}', [15]),
                   P('c', 'change n by {b}', [7]),
                   P('d', 'The last number it says is {b}.', [109])],
            figside=True))
I.append(IT(U, 'S', 6, 2,
            "Siti's code should say the 30th term of 4, 9, 14, 19, ...",
            'The loop adds 5 thirty times: 4 + 5 × 30 = 154. That is the 31st term. The 30th term is 5 × 30 − 1 = 149. '
            'From the 1st to the 30th term there are only 29 jumps, so use repeat 29.',
            fig=code([HAT, ['var', 'set n to (4)'], ['ctl', 'repeat (30)', [['var', 'change n by (5)']]], ['look', 'say (n)']]),
            parts=[P('a', 'Her code says {b}.', [154]),
                   P('b', 'The 30th term really is {b}.', [149]),
                   P('c', 'To fix it, change repeat 30 to repeat {b}.', [29])],
            figside=True))
I.append(IT(U, 'S', 7, 2,
            'Ali has $15 on Day 1. Every day after that he adds $7. So on Day 2 he has $22.',
            'Each day adds $7, so the rule is 7n + 8 (7 × 1 + 8 = 15). (a) Day 4: 7 × 4 + 8 = 36. (c) Day 30: 7 × 30 + 8 = 218. '
            '(d) 7n + 8 is more than 200 when 7n is more than 192. 7 × 27 = 189 is too small, 7 × 28 = 196 works: Day 28 (he has $204).',
            parts=[P('a', 'On Day 4 he has ${b}.', [36]),
                   P('b', 'Money on Day n = {b} × n + {b} dollars.', [7, 8], '7, 8'),
                   P('c', 'On Day 30 he has ${b}.', [218]),
                   P('d', 'He first has more than $200 on Day {b}.', [28])],
            partsrow=True))
I.append(IT(U, 'S', 8, 2,
            'Circle the rule that gives each sequence. Test n = 1 and n = 2.',
            'Put n = 1 and n = 2 into each rule. (a) 5 × 1 − 1 = 4 and 5 × 2 − 1 = 9. (b) 3 × 1 + 7 = 10 and 3 × 2 + 7 = 13. '
            '(c) 8 × 1 − 5 = 3 and 8 × 2 − 5 = 11. The other rules fail on the 1st term.',
            parts=[P('a', '4, 9, 14, 19, ...   {circ:4n + 1|5n - 1|5n + 4}', ['5n - 1'], '5n − 1'),
                   P('b', '10, 13, 16, 19, ...   {circ:3n + 10|10n + 3|3n + 7}', ['3n + 7']),
                   P('c', '3, 11, 19, 27, ...   {circ:8n + 3|8n - 5|3n + 8}', ['8n - 5'], '8n − 5')]))
I.append(IT(U, 'S', 9, 3,
            'A program begins on the 1st term of a sequence. Each repeat moves it on to the next term.',
            'The 1st term needs 0 repeats and each repeat adds 1 to the term number. (a) 60 − 1 = 59 repeats. (b) 1 + 40 = the 41st term. '
            '(c) 25 − 8 = 17 repeats. The repeats count the jumps, not the terms.',
            parts=[P('a', 'To reach the 60th term, repeat {b} times.', [59]),
                   P('b', 'After repeat 40, the sprite is at term number {b}.', [41]),
                   P('c', 'To go from the 8th term to the 25th term, repeat {b} times.', [17])],
            partsrow=True))
I.append(IT(U, 'S', 10, 3,
            'This code uses n as a counter and says a rule. Predict what it says.',
            '(a) n = 1, 2, 3 give 3 × 1 + 1 = 4, 7, 10. (b) The 8th number is 3 × 8 + 1 = 25. '
            '(c) 5, 9, 13 go up by 4, so use 4 × n + 1: 4 × 1 + 1 = 5.',
            fig=code([HAT, ['var', 'set n to (1)'], ['ctl', 'repeat (8)', [['look', 'say (3 × n + 1) for (1) seconds'], ['var', 'change n by (1)']]]]),
            parts=[P('a', 'It starts: {l}', [4, 7, 10], '4, 7, 10', list=True),
                   P('b', 'The last number it says is {b}.', [25]),
                   P('c', 'To say 5, 9, 13, ... use {b} × n + {b}', [4, 1], '4, 1')],
            figside=True))
I.append(IT(U, 'S', 11, 3,
            'Aisha looks at 2, 8, 14, 20, ... The difference is 6, so she says the rule is 6n.',
            'The rule 6n gives 6 for the 1st term, but the 1st term is 2. Each term is 4 less than 6n: 6 − 4 = 2, 12 − 4 = 8. '
            'The difference only tells you the times table. You must still compare with the terms.',
            parts=[P('a', 'Is she right?  {circ:Yes|No}', ['No']),
                   P('b', 'The rule 6n gives {b} for the 1st term, but the 1st term is {b}.', [6, 2], '6, 2'),
                   P('c', 'The correct rule is {b} × n − {b}.', [6, 4], '6, 4')]))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            'A sequence goes down by the same amount each time: 58, 53, 48, 43, ...',
            '(a) The terms go down by 5, so take 5n from a number. 5 × 1 = 5 and 58 + 5 = 63, so the rule is 63 − 5n. (b) 63 − 50 = 13. '
            '(c) 63 − 5n stays above 0 while 5n is less than 63. 5 × 12 = 60 gives 3 and 5 × 13 = 65 would be below 0, so term 12.',
            parts=[P('a', 'The rule for the nth term is {b} − 5n.', [63]),
                   P('b', 'The 10th term is {b}.', [13]),
                   P('c', 'The last term above 0 is term number {b}.', [12])],
            hint='By how much do the terms change each step? Build the rule from it.', partsrow=True, space={'rows': ['Working:']}))
I.append(IT(U, 'T', 2, 4,
            'Program P starts at the 1st term of 6, 10, 14, 18, ... Program Q starts at the 5th term of the same sequence. Both change by 4 each repeat.',
            'The 5th term is 4 × 5 + 2 = 22. Q adds 4 sixteen times: 22 + 64 = 86. Q has moved 16 terms on, so it ends at term 5 + 16 = 21. '
            'P starts at the 1st term, so it needs 21 − 1 = 20 repeats. Check: 6 + 20 × 4 = 86.',
            fig=code([['hat', 'Program Q'], ['var', 'set n to (22)'], ['ctl', 'repeat (16)', [['var', 'change n by (4)']]], ['look', 'say (n)']]),
            parts=[P('a', 'Q ends at term number {b}.', [21]),
                   P('b', 'To end at the same term, P must repeat {b} times.', [20]),
                   P('c', 'Both programs say {b}.', [86])],
            hint='Count how many terms Q moves on. P starts 4 terms earlier.', figside=True))
I.append(IT(U, 'T', 3, 4,
            'A sequence goes up by the same amount each time. Its 4th term is 23 and its 9th term is 53.',
            'From the 4th to the 9th term is 9 − 4 = 5 jumps. The terms rose by 30, so each jump is 30 ÷ 5 = 6. '
            'Going back 3 jumps from the 4th term: 23 − 18 = 5. The rule is 6n − 1 (6 × 4 − 1 = 23).',
            parts=[P('a', 'From the 4th term to the 9th term is {b} jumps.', [5]),
                   P('b', 'Each jump is {b}.', [6]),
                   P('c', 'The 1st term is {b}.', [5]),
                   P('d', 'The rule is {b} × n − {b}.', [6, 1], '6, 1')],
            hint='How many jumps are there between the 2 known terms?', partsrow=True, space={'rows': ['Working:']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            'Matchsticks make staircases. Look at staircases 1, 2 and 3.',
            'The extra sticks each time are 6 (4 to 10), then 8 (10 to 18). They go up by 2 each time, so the next extras are 10 and 12: 18 + 10 = 28 and 28 + 12 = 40. '
            'For staircase 10 add the extras 6, 8, ..., 22 to 4: 4 + 126 = 130. (The rule is n × n + 3n, which is not a times table plus a number.)',
            fig={'type': 'l6_sticks', 'shape': 'stairs', 'ks': [1, 2, 3], 'side': 8},
            parts=[P('a', 'Count the sticks. Staircase 2 has {b} and staircase 3 has {b}.', [10, 18], '10, 18'),
                   P('b', 'The extra sticks go up by the same amount each time. Staircase 4 has {b} sticks and staircase 5 has {b}.', [28, 40], '28, 40'),
                   P('c', 'Staircase 10 has {b} sticks.', [130])],
            hint='Find how many extra sticks each staircase adds. Look for a pattern.',
            beyond='Second differences', figright=True))
I.append(IT(U, 'G', 2, 5,
            'A sprite says these numbers in order: 3, 20, 7, 25, 11, 30, 15, 35, ...',
            'Places 1, 3, 5, ... say 3, 7, 11, 15: they go up by 4. Places 2, 4, 6, ... say 20, 25, 30, 35: they go up by 5. '
            'Place 15 is the 8th of the first kind: 3 + 7 × 4 = 31. Place 20 is the 10th of the second kind: 20 + 9 × 5 = 65.',
            parts=[P('a', 'Places 1, 3, 5, ... go up by {b}. Places 2, 4, 6, ... go up by {b}.', [4, 5], '4, 5'),
                   P('b', 'The number in place 15 is {b}.', [31]),
                   P('c', 'The number in place 20 is {b}.', [65])],
            hint='Split it into 2 sequences. Which one is place 15 in?', partsrow=True))
I.append(IT(U, 'G', 3, 5,
            'What does this code say? Write t after each repeat.',
            't after each repeat: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105. The repeat stops the first time t is above 100, which is after repeat 14, '
            'so k is 14 and t is 105. (These are the triangle numbers 1, 3, 6, 10, ...: the amount added is 1 more each time.)',
            fig=code([['var', 'set t to (0)'], ['var', 'set k to (0)'], ['ctl', 'repeat until <(t) {gt} (100)>', [['var', 'change k by (1)'], ['var', 'change t by (k)']]], ['look', 'say (k)']]),
            parts=[P('a', 'The code says {b}.', [14]),
                   P('b', 'When it stops, t is {b}.', [105])],
            hint='Write t after every repeat: 1, 3, 6, ... Where does it pass 100?',
            beyond='Triangle numbers', figside=True))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            'Find the rule for 9, 16, 23, 30, ... The rule is {b} × n + {b}. The 100th term is {b}.',
            'The difference is 7. Each term is 2 more than 7, 14, 21, 28, so the rule is 7n + 2. The 100th term is 7 × 100 + 2 = 702.',
            answer=A([7, 2, 702], '7, 2, 702')))
I.append(IT(U, 'C', 2, 6,
            'Is 125 a term of 7, 12, 17, 22, ...?  {circ:Yes|No}',
            'The rule is 5n + 2. 125 − 2 = 123 is not a multiple of 5. The terms end in 2 or 7, so 125 is not a term.',
            answer=A(['No'], 'No')))
I.append(IT(U, 'C', 3, 6,
            'The code is: set n to 8, then repeat 20 times: change n by 6. At the end n = {b}, which is term number {b} of 8, 14, 20, ...',
            '8 + 20 \u00d7 6 = 128. From the 1st term to the 21st term there are 20 jumps, so 128 is the 21st term. Check: 6 \u00d7 21 + 2 = 128.',
            answer=A([128, 21], '128, term 21')))
I.append(IT(U, 'C', 4, 6,
            'Mei starts at n = 5. She repeats 4 times: change n by 3, then say n. What is the first number it says?  {b}',
            'The code changes n before it says it. 5 + 3 = 8, so the first number said is 8, not the 1st term 5. To say 5 first, say n before changing it.',
            answer=A([8], '8')))

learn['tight'] = True
write_unit(1, 'Code the pattern', 'Sequences and the nth term',
           'I can find the rule for the nth term of a pattern and use it for the 100th term. I can test my rule with a loop.', learn, I)
