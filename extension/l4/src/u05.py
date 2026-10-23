from lib import *
U = 'L4U05'
def NLN(lo, hi, step, labs, marks=(), shade=(), w=150, **kw):
    return dict({'type': 'l4_numline', 'min': lo, 'max': hi, 'minor': step, 'major': hi - lo, 'labels': {k: v for k, v in labs.items()}, 'labels_only': True,
                 'marks': list(marks), 'shade': list(shade), 'width_mm': w, 'W': 720}, **kw)
BARS = lambda rows, **kw: dict({'type': 'l4_bars', 'rows': rows, 'width_mm': 110, 'unit': 56}, **kw)

learn = {
 'intro': 'On a number line, first find what one small step is worth. To compare decimals, line up the decimal points and compare place by place from the left.',
 'example': {
  'problem': 'What number does the arrow show?',
  'figure': NLN(4.5, 4.6, 0.01, {4.5: '4.5', 4.6: '4.6'}, [{'v': 4.57, 'kind': 'arrow', 'text': '?'}], w=80, W=540),
  'steps': ['4.5 to 4.6 has 10 steps. 1 step = 0.01.', 'The arrow is 7 steps after 4.5.'],
  'answer': 'The arrow shows 4.57.'},
 'example2': {
  'problem': 'A number has 2 decimal places. It rounds to 6.3 to 1 decimal place. What are the least and greatest it can be?',
  'figure': NLN(6.2, 6.4, 0.01, {6.2: '6.2', 6.25: '6.25', 6.3: '6.3', 6.35: '6.35', 6.4: '6.4'}, [{'v': 6.25, 'kind': 'dot'}, {'v': 6.35, 'kind': 'ring'}], shade=[[6.25, 6.35]], w=80, W=540),
  'steps': ['6.25 is halfway, so it rounds up to 6.3.', '6.35 rounds up to 6.4, so the last number is 6.34.'],
  'answer': 'Least 6.25 and greatest 6.34.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to do it',
           'steps': ['Number line: find what 1 small step is worth.',
                     'Compare: line up the points. Add zeros to fill the gaps.',
                     'Round: find the 2 neighbours. Halfway rounds up.']},
 'facts': {'title': 'Place value', 'figure': {'type': 'l4_table', 'head': ['ones', '.', 'tenths', 'hundredths', 'thousandths'], 'rows': [['3', '.', '4', '0', '5']], 'widths': [1, 0.5, 1.3, 1.7, 2], 'cell_h': 50, 'font': 26, 'width_mm': 84},
           'lines': ['3.405 has 4 tenths, 0 hundredths and 5 thousandths.']},
 'try': {'id': U + '-L01', 'text': 'Round 8.46 to 1 decimal place. {b}',
         'answer': A('8.5'),
         'explanation': '8.46 is between 8.4 and 8.5. The halfway mark is 8.45. 8.46 is after it, so it rounds up to 8.5.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'Each small step on the number line is the same size. Write the number each arrow shows.',
  fig=NLN(5, 6, 0.1, {5: '5', 6: '6'}, [{'v': 5.3, 'kind': 'arrow', 'text': 'A'}, {'v': 5.8, 'kind': 'arrow', 'text': 'B'}], w=150),
  parts=[P('a', 'A = {b}', A('5.3')), P('b', 'B = {b}', A('5.8'))], partsrow=True,
  why='From 5 to 6 there are 10 steps, so each step is 0.1. A is 3 steps after 5: 5.3. B is 8 steps after 5: 5.8.'))
S.append(item(U+'-S02', 'start', 1, 'Now each small step is 0.01. Write the number each arrow shows.',
  fig=NLN(0.4, 0.5, 0.01, {0.4: '0.4', 0.5: '0.5'}, [{'v': 0.43, 'kind': 'arrow', 'text': 'C'}, {'v': 0.48, 'kind': 'arrow', 'text': 'D'}], w=150),
  parts=[P('a', 'C = {b}', A('0.43')), P('b', 'D = {b}', A('0.48')), P('c', 'Which arrow shows a number that rounds to 0.5? {circ:C|D}', A('D'))], partsrow=True,
  why='From 0.4 to 0.5 there are 10 steps, so each step is 0.01. C is 3 steps after 0.4: 0.43. D is 8 steps after 0.4: 0.48. 0.48 is past the halfway mark 0.45, so it rounds to 0.5.'))
S.append(item(U+'-S03', 'start', 1, 'Each small step is 0.001. Write the number the arrow shows.',
  fig=NLN(3.42, 3.43, 0.001, {3.42: '3.42', 3.43: '3.43'}, [{'v': 3.427, 'kind': 'arrow', 'text': 'E'}], w=150),
  parts=[P('a', 'E = {b}', A('3.427'))],
  why='From 3.42 to 3.43 there are 10 steps, so each step is 0.001. E is 7 steps after 3.42: 3.427.'))
S.append(item(U+'-S04', 'start', 2, 'Circle the correct sign.',
  parts=[P('a', '4.06  {circ:>|<|=}  4.6', A('<')), P('b', '0.38  {circ:>|<|=}  0.308', A('>')),
         P('c', '12.5  {circ:>|<|=}  12.50', A('=')), P('d', '7.09  {circ:>|<|=}  7.1', A('<'))],
  why='(a) 4.06 has 0 tenths and 4.6 has 6 tenths. (b) 0.38 has 8 hundredths and 0.308 has 0 hundredths. (c) 12.50 is 12.5 with a 0 added. (d) 7.09 is 7.09 and 7.1 is 7.10, and 10 hundredths is more than 9.'))
S.append(item(U+'-S05', 'start', 2, 'Write the numbers in order. Begin with the smallest.\n5.205   5.25   5.052   5.5   5.025\n{ll}',
  ans=A('5.025', '5.052', '5.205', '5.25', '5.5'),
  why='Write each with 3 decimal places: 5.205, 5.250, 5.052, 5.500, 5.025. All have 5 ones. Compare the tenths: 5.025 and 5.052 have 0 tenths, then 5.205 and 5.250 have 2 tenths, then 5.500. 5.025 comes before 5.052, and 5.205 comes before 5.250.'))
S.append(item(U+'-S06', 'start', 2, 'Write the value of the digit 6 in each number.',
  parts=[P('a', '4.562: {b}', A('0.06')), P('b', '6.043: {b}', A('6')), P('c', '0.936: {b}', A('0.006'))], partsrow=True,
  why='In 4.562 the 6 is in the hundredths place: 0.06. In 6.043 it is in the ones place: 6. In 0.936 it is in the thousandths place: 0.006.'))
S.append(item(U+'-S07', 'start', 2, 'Round 6.847.',
  parts=[P('a', 'Nearest 1: {b}', A(7)), P('b', 'Nearest 0.1: {b}', A('6.8')), P('c', 'Nearest 0.01: {b}', A('6.85'))],
  space={'rows': ['Working:']},
  why='(a) 6.847 is between 6 and 7 and is past 6.5, so 7. (b) 6.847 is between 6.8 and 6.9. The halfway mark is 6.85, so it rounds to 6.8. (c) 6.847 is between 6.84 and 6.85. The halfway mark is 6.845, so it rounds up to 6.85.'))
S.append(item(U+'-S08', 'start', 2, 'Ali buys a ruler for $1.85 and a notebook for $2.40. He pays with a $5 note. How much change does he get? ${b}',
  ans=A('0.75'), why='$1.85 + $2.40 = $4.25. $5.00 − $4.25 = $0.75, which is 75¢.',
  space={'rows': ['Working:', '']}))
S.append(item(U+'-S09', 'start', 3, 'Siti\'s bag and Ali\'s bag have a mass of 8.8 kg together. Ali\'s bag is 3 times as heavy as Siti\'s bag.',
  fig=BARS([{'label': 'Siti', 'segs': [{'u': 1}]}, {'label': 'Ali', 'segs': [{'u': 1}, {'u': 1}, {'u': 1}]}], vbrace={'text': '8.8 kg'}, width_mm=120, unit=40, row_h=38, gap=14),
  parts=[P('a', 'Siti\'s bag: {b} kg', A('2.2')), P('b', 'Ali\'s bag: {b} kg', A('6.6'))], partsrow=True,
  why='Siti\'s bag is 1 unit and Ali\'s bag is 3 units. 4 units = 8.8 kg, so 1 unit = 8.8 ÷ 4 = 2.2 kg. Ali\'s bag is 3 × 2.2 = 6.6 kg.'))
S.append(item(U+'-S10', 'start', 3, '4 identical books have a mass of 2.8 kg. A pencil case has a mass of 0.35 kg.',
  parts=[P('a', 'One book: {b} kg', A('0.7')), P('b', 'One book and the pencil case: {b} kg', A('1.05')),
         P('c', '3 books and the pencil case: {b} kg', A('2.45'))],
  why='(a) 2.8 ÷ 4 = 0.7 kg. (b) 0.7 + 0.35 = 1.05 kg. (c) 3 × 0.7 = 2.1, and 2.1 + 0.35 = 2.45 kg.'))
S.append(item(U+'-S11', 'start', 3, 'Find the value of each.',
  parts=[P('a', '4.7 + 2.35 = {b}', A('7.05')), P('b', '9.2 − 3.64 = {b}', A('5.56')),
         P('c', '2.5 × 4 = {b}', A(10)), P('d', '7.2 ÷ 6 = {b}', A('1.2'))],
  why='(a) 4.70 + 2.35 = 7.05. (b) 9.20 − 3.64 = 5.56. (c) 2.5 × 4 = 10. (d) 7.2 ÷ 6 = 1.2, because 6 × 1.2 = 7.2.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S12', 'start', 3, 'Write each as a decimal.',
  parts=[P('a', '7/10 = {b}', A('0.7')), P('b', '19/100 = {b}', A('0.19')), P('c', '3 1/2 = {b}', A('3.5')), P('d', '2 3/4 = {b}', A('2.75'))], partsrow=True,
  why='(a) 7 tenths is 0.7. (b) 19 hundredths is 0.19. (c) 1/2 = 5/10 = 0.5, so 3.5. (d) 3/4 = 75/100 = 0.75, so 2.75.'))

T.append(item(U+'-T01', 'think', 4, 'A number has 3 decimal places. Rounded to 2 decimal places it is 4.27.',
  parts=[P('a', 'The least it can be: {b}', A('4.265')), P('b', 'The greatest it can be: {b}', A('4.274'))],
  hint='Find the halfway marks next to 4.27. Which ones round to 4.27?',
  why='4.265 is halfway between 4.26 and 4.27, so it rounds up to 4.27. 4.275 would round up to 4.28, so the greatest is 4.274.',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T02', 'think', 4, 'Use the digit cards 1, 4, 6 and 9 and a decimal point. Use every card once. The point goes between 2 digits. Make the number that is closest to 20.\n{b}',
  ans=A('19.64'), hint='List the numbers that start with 1 and with 9. Which are near 20?',
  why='Numbers just below 20 start with 19: 19.64 and 19.46. 19.64 is 0.36 below 20 and 19.46 is 0.54 below. Numbers that start with 14 or 16 are further away, and the numbers above 20 start with 41, 46, 49, 61 and so on, which are much further.',
  space={'rows': ['List:', '', '']}))
T.append(item(U+'-T03', 'think', 4, 'A mug costs $2.40 more than a cup. 3 mugs and 2 cups cost $17.20 altogether.',
  parts=[P('a', 'A cup costs ${b}', A('2.00')), P('b', 'A mug costs ${b}', A('4.40'))],
  hint='Change the 3 mugs into cups. How much extra is that?',
  why='If every mug cost the same as a cup, the 5 items would cost $17.20 − 3 × $2.40 = $17.20 − $7.20 = $10.00. So a cup costs $10.00 ÷ 5 = $2.00 and a mug costs $4.40. Check: 3 × $4.40 + 2 × $2.00 = $13.20 + $4.00 = $17.20.',
  space={'rows': ['Draw a bar model here.', '', '']}))

G.append(item(U+'-G01', 'go', 5, 'A cat and a dog have a mass of 9.3 kg together. The dog and a rabbit have a mass of 8.2 kg. The cat and the rabbit have a mass of 5.9 kg. Find the mass of the rabbit.\n{b} kg',
  ans=A('2.4'), hint='Add the 3 totals. Each animal is counted twice.',
  why='Each animal is counted twice in 9.3 + 8.2 + 5.9 = 23.4 kg, so all three together are 11.7 kg. The rabbit is 11.7 − 9.3 = 2.4 kg.',
  space={'rows': ['Working:', '']}))
G.append(item(U+'-G02', 'go', 5, 'Mei has 12 coins. They are all 10¢ coins and 50¢ coins. Altogether they are worth $3.60. How many 50¢ coins does she have? {b}',
  ans=A(6), hint='Suppose all 12 coins are 10¢. How much money is that?',
  why='If all 12 coins were 10¢, the total would be $1.20. The real total is $2.40 more. Changing a 10¢ coin into a 50¢ coin adds 40¢. $2.40 ÷ 40¢ = 6 coins. So she has 6 coins of 50¢ and 6 coins of 10¢. Check: $3.00 + $0.60 = $3.60.',
  space={'rows': ['Working:', '']}))
G.append(item(U+'-G03', 'go', 5, 'Four children share $20.40. Each child gets $0.60 more than the one before. The youngest gets the least.',
  parts=[P('a', 'The youngest gets ${b}', A('4.20')), P('b', 'The oldest gets ${b}', A('6.00'))],
  hint='Take away the extras first: 0.60, 1.20 and 1.80.',
  why='The extras are $0 + $0.60 + $1.20 + $1.80 = $3.60. Without them the 4 children share $20.40 − $3.60 = $16.80, so the youngest gets $16.80 ÷ 4 = $4.20. The oldest gets $4.20 + $1.80 = $6.00. The amounts are $4.20, $4.80, $5.40 and $6.00.',
  space={'rows': ['Working:']}))
G.append(item(U+'-G04', 'go', 5, 'A pattern starts 0.35, 0.40, 0.45, 0.50 and goes on in the same way.',
  parts=[P('a', 'The 20th number is {b}', A('1.3')), P('b', 'Which place in the pattern is 2.05? Place {b}', A(35))],
  hint='Each place adds 0.05. How many steps after the 1st?',
  why='The pattern adds 0.05 each time. The 20th number is 0.35 + 19 × 0.05 = 0.35 + 0.95 = 1.30. For 2.05, the number of steps from 0.35 is (2.05 − 0.35) ÷ 0.05 = 34, so it is the 35th number.',
  space={'rows': ['Working:']}))

C.append(item(U+'-C01', 'quiz', None, 'Write the numbers in order. Begin with the smallest.\n6.07   6.7   6.007   6.17\n{ll}', ans=A('6.007', '6.07', '6.17', '6.7'),
  why='With 3 decimal places: 6.070, 6.700, 6.007, 6.170. In order: 6.007, 6.070, 6.170, 6.700.'))
C.append(item(U+'-C02', 'quiz', None, 'Round 7.846 to the nearest whole number {b}, 1 decimal place {b}, 2 decimal places {b}', ans=A(8, '7.8', '7.85'),
  why='7.846 is past 7.5, so 8. It is below 7.85, so 7.8. It is past 7.845, so 7.85.'))
C.append(item(U+'-C03', 'quiz', None, 'Siti buys 4 notebooks at $1.35 each and pays $10. Her change is ${b}', ans=A('4.60'),
  why='4 × $1.35 = $5.40. $10.00 − $5.40 = $4.60.'))
C.append(item(U+'-C04', 'quiz', None, 'Rounding to 1 decimal place gives 3.6. The number has 2 decimal places. The least is {b} and the greatest is {b}.', ans=A('3.55', '3.64', text='Least 3.55, greatest 3.64'),
  why='3.55 is halfway between 3.5 and 3.6, so it rounds up to 3.6. 3.65 would round up to 3.7, so the greatest is 3.64.'))

unit = {'schema_version': 1, 'level': 4, 'unit': 5, 'id': U, 'title': 'Decimal Detectives', 'topic': 'Decimals', 'holiday_lesson': 5,
        'goal': 'I can read decimals on number lines, compare and order them and round them. I can solve money and mass puzzles with bar models.',
        'learn': learn, 'items': S + T + G + C}
write(5, unit)
