import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

learn = {
 'intro': 'Equal groups are everywhere: legs, wheels, rows of counters. An array shows rows of equal groups. When you share, some may be left over.',
 'example': {
  'problem': 'A yard has 6 animals, ducks (2 legs) and dogs (4 legs). There are 16 legs altogether. How many ducks and how many dogs?',
  'figure': {'type': 'l2_table', 'cols': ['Try', '1', '2', '3'], 'rows': [['Ducks', '6', '5', '4'], ['Dogs', '0', '1', '2'], ['Legs', '12', '14', '16']], 'widths': [1.5, 1, 1, 1], 'first_bold': True, 'width_mm': 78}, 'side': True,
  'steps': ['Start with all ducks: 6 ducks have 12 legs.', 'Swap 1 duck for 1 dog. That adds 2 legs: 14.', 'Swap again: 16 legs. Stop!', 'Check: 4 ducks and 2 dogs. 8 + 8 = 16 legs and 4 + 2 = 6 animals.'],
  'answer': '4 ducks and 2 dogs.'},
 'howto': {'title': 'How to find how many of each', 'steps': ['Start with all of one kind.', 'Swap one at a time. Write the total.', 'Stop at the number you need.', 'Check both clues.']},
 'facts': {'title': 'Arrays and sharing', 'lines': ['3 rows of 4: 3 × 4 = 12 and 4 × 3 = 12.', '12 ÷ 3 = 4 and 12 ÷ 4 = 3.', '17 shared among 5: 3 each and 2 left over.']},
 'try': {'text': 'There are 3 animals, ducks and dogs. They have 10 legs altogether. How many dogs are there? {b}', 'answer': A('2'),
         'explanation': 'Start with 3 ducks: 6 legs. Swap 1 duck for a dog: 8 legs. Swap again: 10 legs. So 1 duck and 2 dogs. Check: 2 + 8 = 10 legs.'}}

items = [
 I('start', 1, 'Look at the array of counters.', figure={'type': 'l2_array', 'rows': 3, 'cols': 7, 'width_mm': 78}, figside=True,
   parts=[P('a', '{b} × {b} = {b}      {b} × {b} = {b}', ['3', '7', '21', '7', '3', '21'], '3 × 7 = 21 and 7 × 3 = 21 (either order)'),
          P('b', '{b} ÷ {b} = {b}      {b} ÷ {b} = {b}', ['21', '3', '7', '21', '7', '3'], '21 ÷ 3 = 7 and 21 ÷ 7 = 3 (either order)')],
   why='There are 3 rows with 7 counters in each row. 3 × 7 = 21 and 7 × 3 = 21. Share 21 into 3 rows: 21 ÷ 3 = 7. Put 21 in rows of 7: 21 ÷ 7 = 3.'),
 I('start', 1, 'A baking tray has the same number of cookies in every row. A towel covers some of the cookies.',
   figure={'type': 'l2_array', 'rows': 4, 'cols': 8, 'cloth': {'r0': 2, 'c0': 4, 'r1': 3, 'c1': 7, 'label': 'towel'}, 'width_mm': 92}, figside=True,
   parts=[P('a', 'How many cookies are in each row? {b}', '8'), P('b', 'How many cookies are on the whole tray? {b}', '32'), P('c', 'How many are under the towel? {b}', '8')],
   why='(a) The top row has 8 cookies, and every row has the same number. (b) 4 rows of 8 is 32. (c) You can see 8 + 8 + 4 + 4 = 24 cookies. 32 - 24 = 8 are under the towel.'),
 I('start', 1, 'Look at the plates. Circle True or False.', figure={'type': 'l2_groups', 'groups': [5, 5, 5, 5], 'per_row': 3, 'width_mm': 112}, partsrow=True,
   parts=[P('a', 'There are 4 groups of 5.   {circ:True|False}', 'True'), P('b', '5 + 5 + 5 = 15 shows all the counters.   {circ:True|False}', 'False'),
          P('c', '4 × 5 = 20 matches the picture.   {circ:True|False}', 'True'), P('d', 'There are 5 plates with 4 counters on each.   {circ:True|False}', 'False')],
   why='(a) 4 plates with 5 counters each: true. (b) 5 + 5 + 5 is only 3 plates, so 15 is not all of them: false. (c) 4 groups of 5 is 4 × 5 = 20: true. (d) The picture shows 4 plates of 5, not 5 plates of 4: false.'),
 I('start', 2, 'Look at the animals.', figure={'type': 'l2_legs', 'items': [{'kind': 'dog', 'n': 3}, {'kind': 'duck', 'n': 2}], 'names': True, 'width_mm': 130},
   parts=[P('a', '3 dogs have {b} legs.', '12'), P('b', '2 ducks have {b} legs.', '4'), P('c', 'All the animals have {b} legs.', '16')],
   why='(a) 3 groups of 4: 4 + 4 + 4 = 12. (b) 2 groups of 2: 2 + 2 = 4. (c) 12 + 4 = 16.'),
 I('start', 2, 'A pen has 8 animals, ducks and rabbits. A duck has 2 legs and a rabbit has 4 legs. There are 26 legs altogether. Start with all ducks. Swap 1 duck for 1 rabbit each time.',
   figure={'type': 'l2_table', 'cols': ['Ducks', '8', '7', '6', '5', '4', '3'], 'rows': [['Rabbits', '0', '1', '2', '3', '4', '5'], ['Legs', '16', '18', None, None, None, None]], 'first_bold': True, 'widths': [1.6, 1, 1, 1, 1, 1, 1], 'width_mm': 146},
   parts=[P('a', 'Write the 4 missing numbers of legs in the table.', ['20', '22', '24', '26'], '20, 22, 24, 26', lst=True),
          P('b', 'There are {b} ducks and {b} rabbits.', ['3', '5'], '3 ducks and 5 rabbits')],
   why='Each swap adds 2 legs: 16, 18, 20, 22, 24, 26. 26 legs is 3 ducks and 5 rabbits. Check: 6 + 20 = 26 legs and 3 + 5 = 8 animals.'),
 I('start', 2, 'Use groups to find the answer.', partsrow=True, parts=[
   P('a', '6 boxes have 4 pencils in each box. How many pencils? {b}', '24'), P('b', '30 sweets go equally into 5 bags. How many in each bag? {b}', '6'),
   P('c', '45 stickers go in packs of 5. How many packs? {b}', '9'), P('d', 'How many wheels do 6 cars have? Each car has 4 wheels. {b}', '24')],
   why='(a) 6 boxes of 4 pencils: 6 × 4 = 24. (b) Share 30 into 5 equal bags: 30 ÷ 5 = 6. (c) How many groups of 5 in 45? 45 ÷ 5 = 9. (d) 6 cars with 4 wheels each: 6 × 4 = 24.'),
 I('start', 3, 'Siti has 37 biscuits. She packs 5 biscuits in each box.', parts=[
   P('a', 'What is the greatest number of boxes she can fill? {b}', '7'), P('b', 'How many biscuits are left over? {b}', '2'), P('c', 'How many more biscuits does she need to fill 1 more box? {b}', '3')],
   why='(a) 7 × 5 = 35 and 8 × 5 = 40 is too many, so 7 boxes. (b) 37 - 35 = 2 left over. (c) 5 - 2 = 3 more biscuits fill another box.'),
 I('start', 3, '47 people go to a farm. Each minibus holds 10 people.', parts=[
   P('a', 'How many minibuses must they use? {b}', '5'), P('b', 'How many seats will be empty? {b}', '3')],
   why='(a) 4 minibuses hold 40 people. 7 people are left, and they need a minibus too, so 5 minibuses. (b) 5 minibuses hold 50 people. 50 - 47 = 3 empty seats.'),
 I('start', 3, 'Mr Lim puts 18 plant pots in equal rows. There must be 2 rows or more and 2 pots or more in each row. Write the pots in each row. Write no if it does not work.',
   figure={'type': 'l2_table', 'cols': ['Rows', '2', '3', '4', '5', '6', '7', '8', '9'], 'rows': [['Pots'] + [None] * 8], 'first_bold': True, 'widths': [2.2, 1, 1, 1, 1, 1, 1, 1, 1], 'width_mm': 150},
   parts=[P('a', 'Fill in the table.', ['9', '6', 'no', 'no', '3', 'no', 'no', '2'], '9, 6, no, no, 3, no, no, 2', lst=True), P('b', 'How many different ways are there? {b}', '4')],
   why='Rows that share 18 equally work: 2 rows of 9, 3 rows of 6, 6 rows of 3, 9 rows of 2. 4, 5, 7 and 8 rows leave some pots over, so no. 4 ways.'),
 I('start', 3, 'Share 24 sweets equally.', parts=[
   P('a', 'Among 3 children, each child gets {b}', '8'), P('b', 'Among 4 children, each child gets {b}', '6'), P('c', 'Among 10 children, each child gets {b}. Left over: {b}.', ['2', '4'], '2 each and 4 left over'),
   P('d', 'Siti shares them with her 3 friends. Each person gets {b}', '6')],
   why='(a) 24 ÷ 3 = 8. (b) 24 ÷ 4 = 6. (c) 10 × 2 = 20, so each gets 2 and 24 - 20 = 4 are left. (d) Siti and her 3 friends are 4 people, so 24 ÷ 4 = 6.'),
 # Think harder
 I('think', 4, 'A shop has bicycles (2 wheels) and tricycles (3 wheels), at least 1 of each. There are 21 wheels altogether. Find ALL the ways.', parts=[
   P('a', 'How many different ways are there? {b}', '3'), P('b', 'What is the fewest number of vehicles you can have? {b}', '8')],
   figure={'type': 'l2_table', 'cols': ['Tricycles', '1', '2', '3', '4', '5', '6'], 'rows': [['Their wheels', '3', '6', '9', '12', '15', '18'], ['Wheels left', None, None, None, None, None, None]], 'first_bold': True, 'widths': [2.2, 1, 1, 1, 1, 1, 1], 'width_mm': 150},
   hint='Bicycles use 2 wheels each. So wheels left must be even.',
   why='Tricycles have 3 wheels. 1 tricycle leaves 18 wheels: 9 bicycles. 3 leave 12: 6 bicycles. 5 leave 6: 3 bicycles. 2, 4 and 6 leave an odd number and 7 leaves none. So 3 ways, with 10, 9 and 8 vehicles. The fewest is 8.'),
 I('think', 4, 'A pen has 6 animals. Each is a hen (2 legs) or a pig (4 legs). All 6 may be hens. Mei counts the legs. Could she count this number?', partsrow=True, parts=[
   P('a', '18 legs   {circ:Yes|No}', 'Yes'), P('b', '25 legs   {circ:Yes|No}', 'No'), P('c', '26 legs   {circ:Yes|No}', 'No'), P('d', '12 legs   {circ:Yes|No}', 'Yes')],
   space={'rows': ['Why 25 is not possible:']}, hint='All hens is 12 legs. Each swap adds 2 legs. All pigs is 24.',
   why='All hens: 12 legs. Each swap adds 2, up to all pigs: 24. Totals: 12, 14 ... 24. (a) 18: yes. (b) 25 is odd: no. (c) 26 is over 24: no. (d) 12: yes.'),
 I('think', 4, 'I am a number between 30 and 50. Put me in groups of 3 and nothing is left. Put me in groups of 4 and 1 is left. Put me in groups of 5 and 3 are left. What is my number? {b}', value='33',
   space={'rows': ['Working:']}, hint='List the numbers that go into groups of 3 first.',
   why='Groups of 3 with none left over: 30, 33, 36, 39, 42, 45, 48. Groups of 4 with 1 left: 33 and 45. Groups of 5 with 3 left: 33 has 3 left, 45 has none. So 33.'),
 # Go further
 I('go', 5, 'The 6 times table. 6 × 5 = 30, and 6 more is 6 × 6.', beyond='The 6 times table', partsrow=True, parts=[
   P('a', '6 × 6 = {b}', '36'), P('b', '6 × 8 = {b}', '48'), P('c', '54 ÷ 6 = {b}', '9'), P('d', '6 × 7 = {b}', '42')],
   hint='Count on in 6s from 30. Or double the 3 times table.',
   why='(a) 30 + 6 = 36. (b) 6 × 8 is double 3 × 8 = 24, so 48. (c) 6 × 9 = 54, so 54 ÷ 6 = 9. (d) 36 + 6 = 42.'),
 I('go', 5, 'Mei has 9 bags. Some bags hold 3 apples. The other bags hold 5 apples. She has 35 apples altogether.', parts=[
   P('a', 'There are {b} bags of 3 apples and {b} bags of 5 apples.', ['5', '4'], '5 bags of 3 and 4 bags of 5'), P('b', 'Could 9 bags hold 40 apples? {circ:Yes|No}', 'No')],
   space={'rows': ['Why (b):']}, hint='Start with all bags of 3. Each swap adds 2 apples.',
   why='(a) All 9 bags of 3 apples: 27 apples. Each swap of a 3-bag for a 5-bag adds 2: 29, 31, 33, 35 after 4 swaps. So 4 bags of 5 and 5 bags of 3. (b) The totals are 27, 29, 31 ... always odd. 40 is even, so it cannot be done.'),
 I('go', 5, 'Make your own puzzle. Use stools (3 legs) and chairs (4 legs). Choose how many pieces and how many legs, so that there is only ONE answer. Many answers are right.', value='open',
   atext='Open. Example: 6 pieces and 21 legs gives 3 stools and 3 chairs (9 + 12 = 21). It is the only answer because each swap adds 1 leg.',
   space={'rows': ['My puzzle:', 'My answer:']}, hint='Pick the answer first. Then count the legs.',
   why='Example: 3 stools and 3 chairs have 9 + 12 = 21 legs and 6 pieces. Starting with 6 stools (18 legs), each swap to a chair adds 1 leg, so 21 legs needs exactly 3 swaps.'),
 I('go', 5, 'Ali has 24 counters. He makes arrays with 2 rows or more and 2 counters or more in each row. A 2 by 12 array and a 12 by 2 array are different. How many different arrays can he make? {b}', value='6',
   hint='Try 2 rows, 3 rows, 4 rows ... up to 12 rows.', space={'rows': ['Working:']},
   why='Rows that share 24 equally: 2 rows of 12, 3 rows of 8, 4 rows of 6, 6 rows of 4, 8 rows of 3, 12 rows of 2. 5, 7, 9, 10 and 11 rows do not work. That is 6 arrays.'),
 # Check yourself
 I('quiz', 0, 'A tray has 3 rows with 8 cups in each row. How many cups are there? {b}', value='24', why='3 rows of 8: 8 + 8 + 8 = 24.'),
 I('quiz', 0, 'How many legs do 5 dogs and 4 ducks have altogether? {b}', value='28', why='5 dogs: 5 × 4 = 20 legs. 4 ducks: 4 × 2 = 8 legs. 20 + 8 = 28.'),
 I('quiz', 0, '47 pencils go in boxes of 10. Full boxes: {b}  Left over: {b}', value=['4', '7'], atext='4 boxes and 7 pencils', why='4 boxes hold 40 pencils. 47 - 40 = 7 are left over.'),
 I('quiz', 0, '9 animals, birds (2 legs) and rabbits (4 legs), have 24 legs. How many rabbits? {b}', value='3', why='9 birds have 18 legs. Each swap to a rabbit adds 2 legs: 20, 22, 24 after 3 swaps. So 3 rabbits and 6 birds. Check: 12 + 12 = 24.'),
]
build(3, 'Legs, wheels and arrays', 'Multiplication and division', 'I can read an array and write its sentences. I can find how many of each from a table. I can share with leftovers.', learn, items, snug=['start1', 'start2', 'start3'])
