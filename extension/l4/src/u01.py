from lib import *
U = 'L4U01'

learn = {
 'intro': 'A factor goes into a number exactly. A multiple is in a times table. Write factors in pairs, in order, and stop when the pairs meet.',
 'example': {
  'problem': 'Find all the factors of 54.',
  'figure': {'type': 'l4_table', 'head': ['Try', 'Pair'], 'rows': [['1', '1 × 54'], ['2', '2 × 27'], ['3', '3 × 18'], ['4, 5', 'no'], ['6', '6 × 9'], ['7, 8', 'no']], 'widths': [1, 2], 'cell_h': 50, 'font': 28, 'width_mm': 66},
  'steps': ['Try 1, 2, 3 in order. Write a pair each time the number goes in.',
            '4 and 5 do not go into 54. 6 × 9 = 54 is a pair.',
            '7 and 8 do not go in, and the next number, 9, is already used. The pairs have met, so stop.'],
  'answer': 'The factors of 54 are 1, 2, 3, 6, 9, 18, 27, 54.'},
 'example2': {
  'problem': 'Lamp A flashes every 4 seconds. Lamp B flashes every 10 seconds. They flash together now. After how many seconds do they next flash together?',
  'figure': {'type': 'l4_table', 'head': ['Lamp', 'Flashes after these seconds'], 'rows': [['A', '4, 8, 12, 16, 20'], ['B', '10, 20']], 'widths': [1, 3], 'cell_h': 50, 'font': 26, 'width_mm': 80},
  'steps': ['List the multiples of each number.', 'Find the first number in both lists.'],
  'answer': 'They next flash together after 20 seconds.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to hunt',
           'steps': ['Factors: try 1, 2, 3 in order. Stop when the pairs meet.',
                     'Common factors: list both numbers, then pick the numbers in both lists.',
                     'Common multiples: list the multiples of both. The first number in both lists is the least.']},
 'facts': {'title': 'Good to know', 'lines': ['A pair like 6 × 6 counts as one factor.', 'So 36 has 9 factors, an odd number.']},
 'try': {'id': U + '-L01', 'text': 'Write all the factors of 45, in order.\n{ll}',
         'answer': A(1, 3, 5, 9, 15, 45, text='1, 3, 5, 9, 15, 45'),
         'explanation': '1 × 45, 3 × 15 and 5 × 9 are the pairs. 2 and 4 do not go into 45. After 5 comes 9, which is already used, so stop.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'Fill in the factor pairs of 56. Some numbers do not go in.',
  parts=[P('a', '1 × 56   2 × {b}   4 × {b}   7 × {b}', A(28, 14, 8, text='2 × 28, 4 × 14, 7 × 8')),
         P('b', 'How many factors does 56 have? {b} factors', A(8, text='8 factors'))],
  why='3, 5 and 6 do not go into 56. The pairs 1 × 56, 2 × 28, 4 × 14 and 7 × 8 give 8 factors. The next number, 8, is already used.'))
S.append(item(U+'-S02', 'start', 1, 'Write all the factors of 66, in order from the smallest.\n{ll}',
  ans=A(1, 2, 3, 6, 11, 22, 33, 66),
  why='1 × 66, 2 × 33, 3 × 22 and 6 × 11. Then 7, 8, 9 and 10 do not go into 66, and 11 is already used.'))
S.append(item(U+'-S03', 'start', 1, 'A class has 32 children. The teacher makes equal teams. Every child is in a team. There is more than 1 team and more than 1 child in a team. List every team size that is possible.\n{ll}',
  ans=A(2, 4, 8, 16),
  why='Team sizes are factors of 32 other than 1 and 32: 2, 4, 8 and 16. For example, 4 children in a team gives 8 teams.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S04', 'start', 1, 'Circle True or False.',
  parts=[P('a', '7 is a factor of 91. {circ:True|False}', A('True')),
         P('b', '54 is a multiple of 8. {circ:True|False}', A('False')),
         P('c', '9 is a factor of 108. {circ:True|False}', A('True')),
         P('d', '65 is a multiple of 13. {circ:True|False}', A('True'))],
  why='(a) 7 × 13 = 91. (b) The multiples of 8 are 48, 56, so 54 is not one. (c) 9 × 12 = 108. (d) 13 × 5 = 65.'))
S.append(item(U+'-S05', 'start', 1, 'Write the first 6 multiples of each number. Then find the least number that is in both lists.',
  parts=[P('a', 'Multiples of 9: {ll}', A(9, 18, 27, 36, 45, 54)),
         P('b', 'Multiples of 12: {ll}', A(12, 24, 36, 48, 60, 72)),
         P('c', 'Least common multiple: {b}', A(36))],
  why='Count in 9s and in 12s. The first number in both lists is 36 (4 nines and 3 twelves).'))
S.append(item(U+'-S06', 'start', 2, 'Find the common factors of 28 and 42.',
  parts=[P('a', 'Factors of 28: {ll}', A(1, 2, 4, 7, 14, 28)),
         P('b', 'Factors of 42: {ll}', A(1, 2, 3, 6, 7, 14, 21, 42)),
         P('c', 'Common factors: {ll}', A(1, 2, 7, 14)),
         P('d', 'Greatest common factor: {b}', A(14))],
  why='28 = 1 × 28, 2 × 14, 4 × 7. 42 = 1 × 42, 2 × 21, 3 × 14, 6 × 7. The numbers in both lists are 1, 2, 7 and 14. The greatest is 14.'))
S.append(item(U+'-S07', 'start', 2, 'Ravi has 30 red marbles and 45 blue marbles. He fills equal bags and no marble is left out. Each bag holds the same number of red marbles, and the same number of blue marbles.',
  parts=[P('a', 'What is the most bags he can fill? {b} bags', A(15, text='15 bags')),
         P('b', 'Then each bag has {b} red and {b} blue.', A(2, 3, text='2 red and 3 blue'))],
  why='The number of bags is a common factor of 30 and 45. The common factors are 1, 3, 5 and 15, so the greatest is 15. Each bag has 30 ÷ 15 = 2 red and 45 ÷ 15 = 3 blue.',
  space={'rows': ['Factors of 30: {ll}', 'Factors of 45: {ll}']}))
S.append(item(U+'-S08', 'start', 2, 'Kumar jogs every 10 days. Aisha jogs every 15 days. They both jog today.',
  parts=[P('a', 'They next jog together after {b} days.', A(30)),
         P('b', 'How many more times do they jog together in the next 100 days? {b} times', A(3))],
  why='The least common multiple of 10 and 15 is 30 (10, 20, 30 and 15, 30). They jog together after 30, 60 and 90 days. The next, 120 days, is after the 100 days. That is 3 times.',
  space={'rows': ['Kumar: 10, 20, {l}', 'Aisha: 15, 30, {l}']}))
S.append(item(U+'-S09', 'start', 2, 'Who am I? I am between 50 and 100. Both 6 and 7 go into me exactly.\nI am {b}.',
  ans=A(84),
  why='A number in both the 6 and 7 times tables: 42, 84. Only 84 is between 50 and 100.'))
S.append(item(U+'-S10', 'start', 3, 'Count the factors of each number.',
  fig={'type': 'l4_table', 'head': ['Number', '8', '14', '18', '27', '32', '49'], 'rows': [['How many factors?', '', '', '', '', '', '']], 'widths': [3.4, 1, 1, 1, 1, 1, 1], 'cell_h': 64, 'font': 28, 'first_col_head': True, 'width_mm': 165},
  parts=[P('a', 'Write the number of factors under each number.', A(4, 4, 6, 4, 6, 3, text='8: 4, 14: 4, 18: 6, 27: 4, 32: 6, 49: 3')),
         P('b', 'Which number in the table has exactly 3 factors? {b}', A(49))],
  why='8: 1, 2, 4, 8. 14: 1, 2, 7, 14. 18: 1, 2, 3, 6, 9, 18. 27: 1, 3, 9, 27. 32: 1, 2, 4, 8, 16, 32. 49: 1, 7, 49. Only 49 has 3 factors.'))
S.append(item(U+'-S11', 'start', 3, 'Mei buys pens in packs of 6 and rubbers in packs of 8. She wants the same number of pens and rubbers.',
  parts=[P('a', 'What is the fewest of each she can buy? {b} of each', A(24)),
         P('b', 'How many packs of pens is that? {b} packs', A(4)),
         P('c', 'How many packs of rubbers is that? {b} packs', A(3))],
  why='The least common multiple of 6 and 8 is 24 (6, 12, 18, 24 and 8, 16, 24). 24 ÷ 6 = 4 packs of pens and 24 ÷ 8 = 3 packs of rubbers.',
  space={'rows': ['Multiples of 6: {l}', 'Multiples of 8: {l}']}))
S.append(item(U+'-S12', 'start', 3, 'I am a factor of 60. I am a multiple of 5. I am greater than 10 and less than 30. Write every number that fits.\n{l} {l}',
  ans=A(15, 20, unordered=True),
  why='The factors of 60 are 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60. Of these, 15 and 20 are multiples of 5 between 10 and 30.'))
S.append(item(U+'-S13', 'start', 3, 'Find out which numbers have an odd count of factors.',
  parts=[P('a', 'How many factors does 64 have? {b}', A(7)),
         P('b', 'How many factors does 81 have? {b}', A(5)),
         P('c', 'Which has an odd count of factors, 72 or 49? {circ:72|49}', A(49))],
  why='64: 1, 2, 4, 8, 16, 32, 64 is 7 factors. 81: 1, 3, 9, 27, 81 is 5 factors. 49 = 7 × 7 pairs with itself, so it has 3 factors (odd). 72 has 12 factors.'))

T.append(item(U+'-T01', 'think', 4, 'A number between 10 and 100 is in the 3 times table and in the 8 times table. Its tens digit is greater than its ones digit. Its digits add up to 9. What is the number?\n{b}',
  ans=A(72), hint='Which numbers are in both the 3 and 8 times tables?', space={'rows': ['Working:', '']},
  why='A multiple of 3 and 8 is a multiple of 24: 24, 48, 72, 96. The digits add to 9 only for 72 (7 + 2). 7 is greater than 2.'))
T.append(item(U+'-T02', 'think', 4, 'Ben has more than 50 stickers and fewer than 100. He packs them in 4s and 3 are left over. He packs them in 5s and 3 are left over. He packs them in 6s and 3 are left over. How many stickers does he have?\n{b}',
  ans=A(63), hint='Take 3 away. What number is in the 4, 5 and 6 times tables?', space={'rows': ['Working:', '', '']},
  why='Without the 3 left over, the number is in the 4, 5 and 6 times tables, so it is a multiple of 60. 60 + 3 = 63 is between 50 and 100. The next one, 123, is too big.'))
T.append(item(U+'-T03', 'think', 4, 'Two gears have marks that touch at the start. Gear A has 12 teeth. Gear B has 18 teeth. They turn together until the marks touch again.',
  parts=[P('a', 'How many teeth go past the touching point? {b} teeth', A(36, text='36 teeth')),
         P('b', 'Gear A turns {b} times and gear B turns {b} times.', A(3, 2, text='A 3 times and B 2 times'))],
  hint='The number of teeth is a multiple of both 12 and 18.', space={'rows': ['Working:', '', '']},
  why='The least common multiple of 12 and 18 is 36. Gear A: 36 ÷ 12 = 3 turns. Gear B: 36 ÷ 18 = 2 turns.'))

G.append(item(U+'-G01', 'go', 5, 'What is the least number that has exactly 10 factors? Show the factors you found.\n{b}',
  ans=A(48), hint='Count the factors of some numbers between 20 and 60.',
  why='48 has 1, 2, 3, 4, 6, 8, 12, 16, 24, 48: 10 factors. Numbers below 48 have fewer: for example 36 has 9, 40 has 8 and 42 has 8.',
  space={'rows': ['My factor lists: {ll}']}))
G.append(item(U+'-G02', 'go', 5, 'Beyond Level 4: Three common multiples\nThree lighthouses flash at 12:00:00. Lighthouse A flashes every 6 seconds, B every 8 seconds and C every 9 seconds.',
  parts=[P('a', 'They next flash together after {b} seconds.', A(72)),
         P('b', 'How many times do they flash together in the next 10 minutes? Do not count 12:00:00. {b} times', A(8, text='8 times'))],
  hint='A common multiple of 3 numbers is in all 3 lists.',
  why='The least common multiple of 6, 8 and 9 is 72. 10 minutes is 600 seconds. 72 × 8 = 576 is less than 600 and 72 × 9 = 648 is more, so they flash together 8 times.'))
G.append(item(U+'-G03', 'go', 5, 'Muffins are sold only in boxes of 4 and boxes of 7. Some numbers of muffins cannot be bought exactly. For example, you cannot buy exactly 5. What is the greatest number that cannot be bought exactly?\n{b}',
  ans=A(17), hint='Write the numbers 1 to 30 and cross out those you can make.',
  why='List the amounts you can make: 4, 7, 8, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23 and every larger number. 17 is not on the list, and 17 − 7 = 10 and 17 − 14 = 3 are not multiples of 4. Every number from 18 up can be made.',
  space={'rows': ['Boxes I can make: {l}']}))
G.append(item(U+'-G04', 'go', 5, 'A rectangle has an area of 84 cm². Its length and width are whole numbers of centimetres. Its perimeter is 38 cm. Find its length and its width.\nThe length is the greater side. Length {b} cm   Width {b} cm',
  ans=A(12, 7, text='Length 12 cm, width 7 cm'), hint='Write the factor pairs of 84. Find the pair that adds to 19.',
  why='Half the perimeter is 19, so length + width = 19. The factor pairs of 84 are 1 and 84, 2 and 42, 3 and 28, 4 and 21, 6 and 14, 7 and 12. Only 7 and 12 add to 19.'))

C.append(item(U+'-C01', 'quiz', None, 'Write all the factors of 52, in order.\n{ll}', ans=A(1, 2, 4, 13, 26, 52),
  why='1 × 52, 2 × 26 and 4 × 13. Then 5 to 12 do not go into 52, and 13 is already used.'))
C.append(item(U+'-C02', 'quiz', None, 'Siti swims every 6 days. Wei swims every 9 days. They both swim today. In how many days will they next swim on the same day? {b} days',
  ans=A(18), why='Multiples of 6: 6, 12, 18. Multiples of 9: 9, 18. The first number in both lists is 18.'))
C.append(item(U+'-C03', 'quiz', None, 'Kumar has 40 red pens and 64 blue pens. He makes identical sets with none left over. How many sets can he make at most? {b} sets',
  ans=A(8), why='The factors of 40 and 64 that are in both lists are 1, 2, 4, 8. The greatest is 8 (5 red and 8 blue in each set).'))
C.append(item(U+'-C04', 'quiz', None, 'I am a multiple of 7. I am a factor of 84. My digits add up to 5. Who am I? {b}',
  ans=A(14), why='The factors of 84 that are multiples of 7 are 7, 14, 21, 28, 42 and 84. Only 14 has digits that add up to 5 (1 + 4).'))

unit = {'schema_version': 1, 'level': 4, 'unit': 1, 'id': U, 'title': 'Factor Hunters', 'topic': 'Factors and multiples', 'holiday_lesson': 1,
        'goal': 'I can list every factor of a number in order. I can find common factors and common multiples and use them to solve sharing and timetable puzzles.',
        'learn': learn, 'items': S + T + G + C}
write(1, unit)
