from lib import *
U = 'L4U02'
NL = lambda mn, mx, labs, marks=None, **kw: dict({'type': 'l4_numline', 'min': mn, 'max': mx, 'minor': 100, 'major': 500, 'labels': labs, 'labels_only': True, 'marks': marks or [], 'width_mm': 160}, **kw)

learn = {
 'intro': 'To round a number, find the two neighbours it lies between. Halfway rounds up. To work backwards from a rounded number, find the smallest and the largest numbers that round to it.',
 'example': {
  'problem': 'Round 46 382 to the nearest 1000.',
  'figure': NL(46000, 47000, {46000: '46 000', 46500: '46 500', 47000: '47 000'}, [{'v': 46382, 'kind': 'arrow', 'text': '46 382'}], width_mm=76, minor=250, W=520),
  'steps': ['46 382 is between 46 000 and 47 000.', 'The halfway mark is 46 500. 46 382 is before it.'],
  'answer': '46 382 rounds to 46 000.'},
 'example2': {
  'problem': 'A number rounds to 8000 to the nearest 1000. What are the smallest and the largest it can be?',
  'figure': NL(7000, 9000, {7000: '7000', 7500: '7500', 8000: '8000', 8500: '8500', 9000: '9000'}, [{'v': 7500, 'kind': 'dot'}, {'v': 8500, 'kind': 'ring'}], shade=[[7500, 8500]], minor=500, W=520, width_mm=76),
  'steps': ['7500 is halfway, so it rounds up to 8000.', '8500 rounds up to 9000, so the last number is 8499.'],
  'answer': 'Smallest 7500 and largest 8499.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to round',
           'steps': ['Find the 2 neighbours, such as 46 000 and 47 000.',
                     'Find the halfway number. Halfway rounds up.',
                     'To work backwards, find where the rounding changes.']},
 'facts': {'title': 'Place value', 'figure': {'type': 'l4_table', 'head': ['10 000s', '1000s', '100s', '10s', '1s'], 'rows': [['3', '5', '2', '0', '6']], 'cell_h': 54, 'font': 26, 'width_mm': 78},
           'lines': ['35 206 = 30 000 + 5000 + 200 + 6', 'Halfway rounds up: 46 500 goes up to 47 000.']},
 'try': {'id': U + '-L01', 'text': 'Round 52 718 to the nearest 100. {b}',
         'answer': A(52700),
         'explanation': '52 718 is between 52 700 and 52 800. The halfway mark is 52 750. 52 718 is before it, so it rounds down to 52 700.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'Round each number. Write the answers in the table.',
  fig={'type': 'l4_table', 'head': ['Number', 'Nearest 10', 'Nearest 100', 'Nearest 1000'], 'rows': [['38 746', '', '', ''], ['70 049', '', '', ''], ['9996', '', '', '']], 'widths': [1.2, 1.4, 1.5, 1.6], 'cell_h': 72, 'font': 28, 'first_col_head': True, 'width_mm': 165},
  ans=A(38750, 38700, 39000, 70050, 70000, 70000, 10000, 10000, 10000, list=True),
  why='38 746: the 6 ones round up to 38 750. To the nearest 100, 46 is under 50, so 38 700. To the nearest 1000, 746 is over 500, so 39 000. 70 049: 70 050, 70 000, 70 000. 9996 is 4 away from 10 000, so all three roundings are 10 000.'))
S.append(item(U+'-S02', 'start', 1, 'Write the value of the digit 6 in each number.',
  parts=[P('a', '46 281: {b}', A(6000)), P('b', '60 912: {b}', A(60000)), P('c', '83 062: {b}', A(60))],
  partsrow=True,
  why='46 281 has 6 in the thousands place, so it is worth 6000. In 60 912 it is in the ten thousands place: 60 000. In 83 062 it is in the tens place: 60.'))
S.append(item(U+'-S03', 'start', 1, 'Write each number in figures.',
  fig={'type': 'l4_table', 'head': ['In words', 'In figures'], 'rows': [['forty-two thousand and seven', ''], ['sixty thousand, nine hundred', ''], ['eight thousand and thirty', '']], 'widths': [3, 1.4], 'cell_h': 72, 'font': 28, 'first_col_head': True, 'width_mm': 150},
  ans=A(42007, 60900, 8030, list=True),
  why='forty-two thousand and seven is 42 007: 42 thousands, no hundreds, no tens and 7 ones. sixty thousand, nine hundred is 60 900. eight thousand and thirty is 8030.'))
S.append(item(U+'-S04', 'start', 1, 'Write the numbers in order. Begin with the greatest.\n58 304   58 340   58 034   58 430\n{ll}',
  ans=A(58430, 58340, 58304, 58034),
  why='All four have 58 thousands. Compare the hundreds: 4, 3, 3, 0. The two with 3 hundreds are 58 340 and 58 304, and 340 is greater than 304.'))
S.append(item(U+'-S05', 'start', 2, 'The arrows point to numbers on the line. Each small step is 100.',
  fig=NL(24000, 25000, {24000: '24 000', 24500: '24 500', 25000: '25 000'}, [{'v': 24300, 'kind': 'arrow', 'text': 'A'}, {'v': 24800, 'kind': 'arrow', 'text': 'B'}], W=760, width_mm=160),
  parts=[P('a', 'A is {b}', A(24300)), P('b', 'B is {b}', A(24800)),
         P('c', 'Which thousand is B closer to? {b}', A(25000))],
  why='There are 5 steps of 100 between 24 000 and 24 500. A is 3 steps after 24 000: 24 300. B is 3 steps after 24 500: 24 800. 24 800 is past the halfway mark 24 500, so it is closer to 25 000.'))
S.append(item(U+'-S06', 'start', 2, 'A match had 36 482 people watching. Round the number of people to the nearest 1000 and to the nearest 100.',
  parts=[P('a', 'Nearest 1000: {b}', A(36000)), P('b', 'Nearest 100: {b}', A(36500))],
  partsrow=True,
  why='36 482 is between 36 000 and 37 000, and it is before the halfway mark 36 500, so it rounds to 36 000. To the nearest 100 it is between 36 400 and 36 500, and 82 is more than 50, so 36 500.'))
S.append(item(U+'-S07', 'start', 2, 'A town has 12 000 people after rounding to the nearest 1000. Find the least number of people it could have, and the greatest.',
  parts=[P('a', 'Least: {b}', A(11500)), P('b', 'Greatest: {b}', A(12499))],
  partsrow=True,
  why='11 500 is halfway between 11 000 and 12 000 and rounds up to 12 000. 12 500 would round up to 13 000, so the largest is 12 499.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S08', 'start', 2, 'A number rounds to 4700 to the nearest 100.',
  parts=[P('a', 'The smallest it can be is {b}', A(4650)), P('b', 'The largest it can be is {b}', A(4749)),
         P('c', 'How many whole numbers could it be? {b}', A(100))],
  partsrow=True,
  why='4650 is halfway between 4600 and 4700, so it rounds up. 4750 would round to 4800, so the largest is 4749. From 4650 to 4749 there are 100 numbers.'))
S.append(item(U+'-S09', 'start', 3, 'A ferry carries 4018 people on each trip. It makes 5 trips.',
  parts=[P('a', 'Round 4018 to the nearest 1000. Estimate the total: {b}', A(20000)),
         P('b', 'Find the exact total: {b}', A(20090)),
         P('c', 'The exact total is {circ:more|less} than the estimate.', A('more'))],
  why='4018 rounds to 4000, and 5 × 4000 = 20 000. The exact total is 5 × 4018 = 20 090. 4018 was rounded down, so the exact total is more.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S10', 'start', 3, 'I have 5 digits. Round me to the nearest 1000 and you get 52 000. My hundreds digit is 7. My tens digit is 5 and my ones digit is 2. Who am I?\nI am {b}.',
  ans=A(51752),
  why='Numbers that round to 52 000 are from 51 500 to 52 499. With 7 hundreds the number must be 51 7__, because 52 7__ is too big. Then the tens and ones give 51 752.'))
S.append(item(U+'-S11', 'start', 3, 'Use the digit cards 2, 4, 0, 7 and 9. Use each card once.',
  parts=[P('a', 'The greatest number: {b}', A(97420)), P('b', 'The least number: {b}', A(20479)),
         P('c', 'The greatest odd number: {b}', A(94207))],
  why='Greatest: put the greatest digits first, 97 420. Least: 0 cannot go first, so start with 2: 20 479. Odd: the ones digit must be 7 or 9. Ending in 7 gives 94 207 and ending in 9 gives 74 209, so 94 207 is greater.'))
S.append(item(U+'-S12', 'start', 3, 'Find the rule. Write the next 2 numbers.',
  parts=[P('a', '31 600, 32 600, 33 600, {b}, {b}', A(34600, 35600)),
         P('b', '70 400, 68 900, 67 400, {b}, {b}', A(65900, 64400)),
         P('c', '4997, 5000, 5003, 5006, {b}, {b}', A(5009, 5012))],
  why='(a) Add 1000 each time. (b) Take away 1500 each time: 67 400 − 1500 = 65 900, then 64 400. (c) Add 3 each time: 5006 + 3 = 5009, then 5012.'))
S.append(item(U+'-S13', 'start', 3, 'Circle the correct sign.',
  parts=[P('a', '45 009  {circ:>|<}  45 090', A('<')), P('b', '8999  {circ:>|<}  10 000', A('<')),
         P('c', '62 100  {circ:>|<}  62 010', A('>')), P('d', '30 000 + 700  {circ:>|<}  30 070', A('>'))],
  why='(a) 45 009 has 0 tens, 45 090 has 9 tens, so it is smaller. (b) 8999 has 4 digits. (c) 62 100 has 1 hundred, 62 010 has none. (d) 30 000 + 700 is 30 700, which is greater than 30 070.'))

T.append(item(U+'-T01', 'think', 4, 'Cards: 1, 3, 4, 6, 8. Use each card once. Make the 5-digit number nearest to 40 000.\n{b}',
  ans=A(38641), hint='Check one number just below 40 000 and one just above.',
  why='Just below 40 000: the greatest number that starts with 3 is 38 641, which is 1359 away. Just above 40 000: the least number that starts with 4 is 41 368, which is 1368 away. 38 641 is closer.',
  space={'rows': ['Working:', '', '']}))
T.append(item(U+'-T02', 'think', 4, 'Two crowds were counted. To the nearest 1000, one crowd was 41 000 and the other was 28 000.',
  parts=[P('a', 'The smallest possible total of both crowds: {b}', A(68000)),
         P('b', 'The largest possible total of both crowds: {b}', A(69998))],
  hint='Add the 2 smallest numbers. Then add the 2 largest.',
  why='The smallest crowds are 40 500 and 27 500: 68 000. The largest are 41 499 and 28 499: 69 998.',
  space={'rows': ['Working:', '', '']}))
T.append(item(U+'-T03', 'think', 4, 'A 5-digit number has 5 different digits. It rounds to 70 000 to the nearest 10 000.',
  parts=[P('a', 'The greatest it can be: {b}', A(74986)), P('b', 'The least it can be: {b}', A(65012))],
  hint='Numbers that round to 70 000 run from 65 000 to 74 999.',
  why='Greatest: 74 999 is the top, but its digits repeat. Using 7, 4, then the greatest digits left gives 74 986. Least: 65 000 repeats the 0, so use 65 012.',
  space={'rows': ['Working:', '']}))

G.append(item(U+'-G01', 'go', 5, 'Ravi rounds 36 449 in 3 steps. First to the nearest 10, then that answer to the nearest 100, then that answer to the nearest 1000.',
  parts=[P('a', 'After the 3 steps he gets {b}', A(37000)),
         P('b', 'Round 36 449 to the nearest 1000 in one go: {b}', A(36000)),
         P('c', 'Rounding 1 step at a time gives a wrong answer for some 4-digit numbers. What is the least 4-digit number where it does? {b}', A(1445))],
  hint='Which numbers end in 4 and 5 just before a change?',
  why='36 449 becomes 36 450, then 36 500, then 37 000. In one go it is 36 000, because 449 is below 500. For part (c), 1445 becomes 1450, then 1500, then 2000, but in one go it is 1000. Any 4-digit number below 1445 gives the same answer both ways.'))
G.append(item(U+'-G02', 'go', 5, 'Beyond Level 4: Counting by place\nBen writes the whole numbers from 1 to 1000. How many of them contain at least one 7?\n{b}',
  ans=A(271), hint='Count the numbers with no 7. Choose each digit in turn.',
  why='Count the numbers with no 7. Think of 3 digits, from 000 to 999. Each digit can be any of 9 digits (not 7): 9 × 9 × 9 = 729. That includes 000, which is not in the list, and it leaves out 1000, which has no 7, so 729 numbers from 1 to 1000 have no 7. So 1000 − 729 = 271 have a 7.',
  space={'rows': ['Working:', '']}))
G.append(item(U+'-G03', 'go', 5, 'Two patterns are woven together: 12 000, 3, 11 000, 6, 10 000, 9, and so on.',
  parts=[P('a', 'The 9th number is {b}', A(8000)), P('b', 'The 10th number is {b}', A(15))],
  hint='Take every second number. You get 2 patterns.',
  why='The numbers in places 1, 3, 5 ... are 12 000, 11 000, 10 000, 9000, 8000. The 9th is the 5th of these: 8000. The numbers in places 2, 4, 6 ... are 3, 6, 9, 12, 15. The 10th is the 5th of these: 15.'))
G.append(item(U+'-G04', 'go', 5, 'Some numbers round to 7000 to the nearest 1000. Siti says they all round to 7000 to the nearest 100 too.',
  parts=[P('a', 'Is she right? {circ:Yes|No}', A('No')),
         P('b', 'How many of the whole numbers that round to 7000 to the nearest 1000 also round to 7000 to the nearest 100? {b}', A(100))],
  hint='Find the first and last numbers for each rounding.',
  why='To the nearest 1000, the numbers are 6500 to 7499. To the nearest 100, they are 6950 to 7049. For example, 7400 is in the first list but rounds to 7400 to the nearest 100. The numbers in both lists are 6950 to 7049: 100 numbers.'))

C.append(item(U+'-C01', 'quiz', None, 'Round 25 962.   To the nearest 10: {b}   100: {b}   1000: {b}',
  ans=A(25960, 26000, 26000, text='25 960, 26 000, 26 000'),
  why='25 962: the 2 ones round down to 25 960. The last two digits, 62, are over 50, so 26 000. The last three digits, 962, are over 500, so 26 000.'))
C.append(item(U+'-C02', 'quiz', None, 'To the nearest 100, 8300 people came to a show. The least could be {b} and the greatest could be {b}.',
  ans=A(8250, 8349, text='Least 8250, greatest 8349'),
  why='8250 is halfway between 8200 and 8300 and rounds up to 8300. 8350 would round up to 8400, so the greatest is 8349.'))
C.append(item(U+'-C03', 'quiz', None, 'Cards: 4, 0, 7, 1, 8. Use each card once. Make the least odd 5-digit number. {b}',
  ans=A(10487), why='The ones digit must be 7 or 1. Ending in 7 lets 1 go first: 10 487. Ending in 1 needs 4 first: 40 781. 10 487 is less.'))
C.append(item(U+'-C04', 'quiz', None, 'Find the rule. Write the next 2 numbers. 53 200, 51 700, 50 200, {b}, {b}',
  ans=A(48700, 47200), why='Each number is 1500 less than the one before: 50 200 − 1500 = 48 700, then 47 200.'))

unit = {'schema_version': 1, 'level': 4, 'unit': 2, 'id': U, 'title': 'Big Number Puzzles', 'topic': 'Numbers to 100 000', 'holiday_lesson': 2,
        'goal': 'I can round numbers to the nearest 10, 100 and 1000. I can work backwards from a rounded number and solve digit puzzles.',
        'learn': learn, 'items': S + T + G + C}
write(2, unit)
