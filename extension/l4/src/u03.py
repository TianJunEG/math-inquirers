from lib import *
U = 'L4U03'
BARS = lambda rows, **kw: dict({'type': 'l4_bars', 'rows': rows, 'width_mm': 120, 'unit': 56}, **kw)
u = lambda n=1, **k: dict({'u': n}, **k)

learn = {
 'intro': 'A bar model shows a "times as many" story. Each equal part is one unit. To go back to the start of a number machine, undo each step in the opposite order.',
 'example': {
  'problem': 'Mr Tan has 3 times as many red pens as blue pens. He has 156 pens in all. How many blue pens does he have?',
  'figure': BARS([{'label': 'Blue', 'segs': [u()]}, {'label': 'Red', 'segs': [u(), u(), u()]}], vbrace={'text': '156'}, width_mm=82, unit=48),
  'steps': ['Blue is 1 unit and red is 3 units. That is 4 units.', '4 units = 156, so 1 unit = 156 ÷ 4 = 39.'],
  'answer': 'He has 39 blue pens.'},
 'example2': {
  'problem': 'I think of a number. I add 9 and then multiply by 4. The answer is 68. What is my number?',
  'figure': {'type': 'l4_flow', 'items': [None, None, 68], 'ops': ['+ 9', '× 4'], 'back': ['÷ 4', '− 9'], 'width_mm': 82},
  'steps': ['Undo the steps in the opposite order.', 'Undo × 4 with ÷ 4: 68 ÷ 4 = 17. Undo + 9 with − 9: 17 − 9 = 8.'],
  'answer': 'My number is 8. Check: 8 + 9 = 17 and 17 × 4 = 68.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to solve it',
           'steps': ['Bar models: draw one bar for each quantity. Count the units.',
                     'Divide the total by the number of units.',
                     'Machines: start from the end and undo each step. Check by going forward.']},
 'facts': {'title': 'Opposites', 'lines': ['+ and − undo each other.', '× and ÷ undo each other.', '"4 times as many" is 4 units.']},
 'try': {'id': U + '-L01', 'text': 'A shop has 114 pens and rulers. The number of pens is 5 times the number of rulers. How many rulers are there? {b}',
         'answer': A(19),
         'explanation': 'Rulers are 1 unit and pens are 5 units: 6 units in all. 6 units = 114, so 1 unit = 114 ÷ 6 = 19 rulers.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'Find the value of each.',
  parts=[P('a', '3706 × 4 = {b}', A(14824)), P('b', '85 × 47 = {b}', A(3995)),
         P('c', '7524 ÷ 6 = {b}', A(1254)), P('d', '8150 ÷ 5 = {b}', A(1630))],
  why='(a) 3706 × 4 = 12 000 + 2800 + 24 = 14 824. (b) 85 × 47 = 85 × 40 + 85 × 7 = 3400 + 595 = 3995. (c) 6 × 1254 = 7524. (d) 5 × 1630 = 8150.',
  space={'rows': ['Working:', '']}))
S.append(item(U+'-S02', 'start', 1, 'Round each number to the nearest 1000. Then estimate the answer.',
  parts=[P('a', '4986 × 4 is about {b}', A(20000)), P('b', '9120 ÷ 3 is about {b}', A(3000)),
         P('c', '7020 − 2980 is about {b}', A(4000))],
  why='(a) 4986 rounds to 5000 and 5000 × 4 = 20 000. (b) 9120 rounds to 9000 and 9000 ÷ 3 = 3000. (c) 7020 rounds to 7000 and 2980 rounds to 3000, and 7000 − 3000 = 4000.'))
S.append(item(U+'-S03', 'start', 1, 'A hall has 28 rows of 36 chairs. Then 45 chairs are broken and taken away. How many chairs are left in the hall? {b} chairs',
  ans=A(963), why='28 × 36 = 1008 chairs at first. 1008 − 45 = 963 chairs are left.',
  space={'rows': ['Working:', '']}))
S.append(item(U+'-S04', 'start', 1, 'A baker packs 5468 buns into boxes of 8.',
  parts=[P('a', 'How many full boxes does she fill? {b} boxes', A(683)),
         P('b', 'How many buns are left over? {b} buns', A(4))],
  why='5468 ÷ 8 = 683 with a remainder of 4, because 8 × 683 = 5464 and 5468 − 5464 = 4.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S05', 'start', 2, 'A farm has 4 times as many hens as ducks. There are 385 hens and ducks in all. How many ducks are there? {b} ducks',
  fig=BARS([{'label': 'Ducks', 'segs': [u()]}, {'label': 'Hens', 'segs': [u(), u(), u(), u()]}], vbrace={'text': '385'}, width_mm=105, unit=52),
  ans=A(77), why='Ducks are 1 unit and hens are 4 units: 5 units in all. 5 units = 385, so 1 unit = 385 ÷ 5 = 77 ducks.'))
S.append(item(U+'-S06', 'start', 2, 'A ruler and a pencil case cost $47 together. The pencil case costs $9 more than the ruler.',
  fig=BARS([{'label': 'Ruler', 'segs': [u(2)]}, {'label': 'Pencil case', 'segs': [u(2), u(0.8, k='q', t='$9')]}], vbrace={'text': '$47'}, width_mm=105, unit=52),
  parts=[P('a', 'The ruler costs ${b}', A(19)), P('b', 'The pencil case costs ${b}', A(28))],
  partsrow=True,
  why='Take away the extra $9: $47 − $9 = $38. Two equal parts are $38, so the ruler costs $38 ÷ 2 = $19. The pencil case costs $19 + $9 = $28.'))
S.append(item(U+'-S07', 'start', 2, 'Mei picks a secret number. She multiplies it by 6, takes away 9, then divides by 3. She gets 31. What is her number? {b}',
  fig={'type': 'l4_flow', 'items': [None, None, None, 31], 'ops': ['× 6', '− 9', '÷ 3'], 'width_mm': 130},
  ans=A(17), why='Work backwards. 31 × 3 = 93. 93 + 9 = 102. 102 ÷ 6 = 17. Check: 17 × 6 = 102, 102 − 9 = 93, 93 ÷ 3 = 31.',
  ))
S.append(item(U+'-S08', 'start', 2, 'A number trick. Start with a number. Multiply by 3, add 12, then divide by 3. Last, subtract the number you started with.',
  parts=[P('a', 'Start with 6. You end with {b}', A(4)), P('b', 'Start with 15. You end with {b}', A(4)),
         P('c', 'Whatever you start with, you end with {b}', A(4))],
  why='6 × 3 = 18, 18 + 12 = 30, 30 ÷ 3 = 10, 10 − 6 = 4. 15 × 3 = 45, 45 + 12 = 57, 57 ÷ 3 = 19, 19 − 15 = 4. Multiplying by 3 and then dividing by 3 gives back the number. The 12 ÷ 3 adds 4, and taking away the number leaves 4.',
  ))
S.append(item(U+'-S09', 'start', 3, 'Find the missing numbers.',
  parts=[P('a', '7 × {b} = 4249', A(607)), P('b', '{b} ÷ 9 = 124', A(1116)),
         P('c', '5000 − {b} = 2738', A(2262)), P('d', '{b} + 1905 = 6400', A(4495))],
  why='(a) 4249 ÷ 7 = 607. (b) 124 × 9 = 1116. (c) 5000 − 2738 = 2262. (d) 6400 − 1905 = 4495.'))
S.append(item(U+'-S10', 'start', 3, 'Mrs Lee buys 6 notebooks at $3 each and 4 pens at $2 each. She pays with $50. What is her change? ${b}',
  ans=A(24), why='6 × $3 = $18 and 4 × $2 = $8. The cost is $18 + $8 = $26. The change is $50 − $26 = $24.',
  space={'rows': ['Working:', '']}))
S.append(item(U+'-S11', 'start', 3, 'In a chain, add the last 2 numbers to make the next number. Fill in the missing numbers.',
  parts=[P('a', '4, 9, {b}, 22, {b}', A(13, 35)), P('b', '{b}, 6, 11, {b}, 28', A(5, 17))],
  space={'rows': ['Working:']},
  why='(a) 4 + 9 = 13. Then 9 + 13 = 22 and 13 + 22 = 35. (b) 11 + 6 = 17 and 6 + 11 = 17. The first number is 11 − 6 = 5. Check: 5 + 6 = 11, 6 + 11 = 17 and 11 + 17 = 28.'))
S.append(item(U+'-S12', 'start', 3, 'Kumar picked 3 times as many mangoes as Aisha. They picked 480 mangoes in all. How many more mangoes did Kumar pick than Aisha? {b} mangoes',
  ans=A(240), why='Aisha has 1 unit and Kumar has 3 units: 4 units in all. 1 unit = 480 ÷ 4 = 120. Kumar has 360 and Aisha has 120. The difference is 2 units: 240.',
  space={'rows': ['Draw a bar model here.', '']}))

T.append(item(U+'-T01', 'think', 4, 'Beyond Level 4: Order of operations\nRule: do brackets first, then × and ÷, then + and −. Work from the left.',
  parts=[P('a', '60 − 4 × 9 + 12 ÷ 3 = {b}', A(28)), P('b', '5 × (13 + 7) − 6 = {b}', A(94))],
  hint='In part (a), do 4 × 9 and 12 ÷ 3 before anything else.',
  why='(a) 4 × 9 = 36 and 12 ÷ 3 = 4. Then 60 − 36 + 4 = 24 + 4 = 28. (b) Brackets first: 13 + 7 = 20. Then 5 × 20 = 100 and 100 − 6 = 94.',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T02', 'think', 4, 'A number tower has 3 numbers at the bottom: 5, a missing number and 11. Each number above is the sum of the 2 numbers just below it. The top number is 52. What is the missing number? {b}',
  ans=A(18), hint='Write the 2 numbers in the middle row. They add up to 52.',
  why='The middle row is 5 + ? and ? + 11, and these add up to 52. So 5 + 11 + 2 × ? = 52, 2 × ? = 36 and ? = 18. The middle row is 23 and 29.',
  space={'rows': ['Working:', '', '']}))
T.append(item(U+'-T03', 'think', 4, 'Kumar and Siti have 90 stickers altogether. Kumar has 5 times as many as Siti. Kumar gives some stickers to Siti. Then they have equal amounts.',
  parts=[P('a', 'Siti at first: {b} stickers', A(15)), P('b', 'Kumar gives Siti {b} stickers', A(30))],
  hint='Each of them ends with half of the 90 stickers.',
  why='Siti is 1 unit and Kumar is 5 units. 6 units = 90, so 1 unit = 15. Siti has 15 and Kumar has 75. Equal shares are 45 each, so Kumar gives 75 − 45 = 30.',
  space={'rows': ['Draw a bar model here.', '', '']}))

G.append(item(U+'-G01', 'go', 5, 'Beyond Level 4: Signs and brackets\nRule: brackets first, then × and ÷, then + and −.',
  parts=[P('a', 'Write + − × or ÷ in each circle: 9 ○ 4 ○ 6 = 30', A('×', '−', text='9 × 4 − 6')),
         P('b', 'Put ONE pair of brackets in 7 + 3 × 8 − 4 to make 76. Write the numbers inside the brackets: {b} + {b}', A(7, 3, text='(7 + 3) × 8 − 4'))],
  hint='For (a), estimate first. A big answer needs ×.',
  why='(a) 9 × 4 = 36 and 36 − 6 = 30. The other signs do not give 30. (b) (7 + 3) × 8 − 4 = 10 × 8 − 4 = 76. Brackets round 3 × 8 give 7 + 24 − 4 = 27, and brackets round 8 − 4 give 7 + 3 × 4 = 19.',
  space={'rows': ['Try:']}))
G.append(item(U+'-G02', 'go', 5, 'Ben and Mei both save for a bike. Plan A: start with $15 and save $8 each week. Plan B: start with $0 and save $13 each week.',
  fig={'type': 'l4_table', 'head': ['Week', '0', '1', '2', '3', '4'], 'rows': [['Plan A', '$15', '', '', '', ''], ['Plan B', '$0', '', '', '', '']], 'widths': [1.6, 1, 1, 1, 1, 1], 'cell_h': 50, 'font': 26, 'first_col_head': True, 'width_mm': 140},
  parts=[P('a', 'In which week do both plans have the same amount? Week {b}', A(3)),
         P('b', 'How much is that? ${b}', A(39))],
  hint='Fill in the table. Look at the gap between the plans each week.',
  why='Plan A has $15, $23, $31, $39. Plan B has $0, $13, $26, $39. Both have $39 in week 3. Each week Plan B gains $5 on Plan A, and the start gap is $15, so 15 ÷ 5 = 3 weeks.'))
G.append(item(U+'-G03', 'go', 5, 'Fill in the missing digits.\n3 □ 4 × 7 = 2 □ 3 8',
  parts=[P('a', 'The missing digit in 3 □ 4 is {b}', A(3)), P('b', 'The missing digit in 2 □ 3 8 is {b}', A(3))],
  hint='Start with the ones: what is 4 × 7?',
  why='4 × 7 = 28, which ends in 8, as needed. 3□4 × 7 = 2128 + 70 × □ must be 2□38. Trying 3 gives 2128 + 210 = 2338. Check: 334 × 7 = 2338. So both missing digits are 3.',
  space={'rows': ['Try:', '']}))

C.append(item(U+'-C01', 'quiz', None, 'Find the value.   4728 × 5 = {b}   9135 ÷ 7 = {b}',
  ans=A(23640, 1305, text='23 640 and 1305'), why='4728 × 5 = 23 640 (4728 × 10 = 47 280, then half). 9135 ÷ 7 = 1305, because 7 × 1305 = 9135.'))
C.append(item(U+'-C02', 'quiz', None, 'Ali saves $15 a week for 12 weeks. Then he spends $64. How much money does he have left? ${b}',
  ans=A(116), why='15 × 12 = 180, so he saves $180. $180 − $64 = $116.'))
C.append(item(U+'-C03', 'quiz', None, 'There are 4 times as many red cars as blue cars. There are 275 cars in all. How many red cars are there? {b}',
  ans=A(220), why='Blue is 1 unit and red is 4 units: 5 units. 1 unit = 275 ÷ 5 = 55. Red is 4 × 55 = 220.'))
C.append(item(U+'-C04', 'quiz', None, 'I think of a number. I add 17, multiply by 3 and take away 20. The answer is 94. What is my number? {b}',
  ans=A(21), why='Work backwards. 94 + 20 = 114. 114 ÷ 3 = 38. 38 − 17 = 21.'))

unit = {'schema_version': 1, 'level': 4, 'unit': 3, 'id': U, 'title': 'Operation Detectives', 'topic': 'Four operations', 'holiday_lesson': 3,
        'goal': 'I can solve multi-step problems with the four operations. I can use bar models for "times as many" and work backwards through a number machine.',
        'learn': learn, 'items': S + T + G + C}
write(3, unit)
