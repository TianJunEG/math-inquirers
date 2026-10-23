import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

def pg(rows, key, **kw):
    d = {'type': 'l2_pgraph', 'rows': [{'label': l, 'n': n} for l, n in rows], 'key': key}
    d.update(kw)
    return d

TB = lambda cols, rows, w=140, ws=None, **kw: dict({'type': 'l2_table', 'cols': cols, 'rows': rows, 'first_bold': True, 'widths': ws or [1.8] + [1] * (len(cols) - 1), 'width_mm': w}, **kw)

learn = {
 'intro': 'A puzzle is easier when you know how to start. Draw it. List it in order. Make a table. Then check every clue.',
 'example': {
  'problem': 'Lily has 7 coins. Each coin is 10¢ or 20¢. They are worth $1.10 altogether. How many of each coin?',
  'figure': TB(['10¢ coins', '7', '6', '5', '4', '3'], [['20¢ coins', '0', '1', '2', '3', '4'], ['Total', '70¢', '80¢', '90¢', '100¢', '110¢']], w=90, ws=[1.8, 1, 1, 1, 1, 1], size=30), 'side': False,
  'steps': ['Start with 7 coins of 10¢. That is 70¢.', 'Swap one 10¢ for a 20¢. The total goes up by 10¢ each time.', 'Stop when the total is 110¢: 3 coins of 10¢ and 4 coins of 20¢.', 'Check: 30¢ + 80¢ = 110¢ and 3 + 4 = 7 coins.'],
  'answer': '3 coins of 10¢ and 4 coins of 20¢.'},
 'howto': {'title': 'Ways to start', 'steps': ['Draw it: a picture or a bar.', 'List it: write every case in order.', 'Make a table: try 1, 2, 3 ...', 'Check against every clue.']},
 'facts': {'title': 'Tips', 'lines': ['Graph: read the key first.', 'Logic grid: tick one box. Cross out the rest of its row and column.', 'List in order so no case is missed.']},
 'try': {'text': 'The key of a graph says each picture is 5 children. Maths has 6 pictures. How many chose maths? {b}', 'answer': A('30'),
         'explanation': 'Each picture is 5 children. 6 pictures: 5, 10, 15, 20, 25, 30. So 30 children chose maths.'}}

items = [
 I('start', 1, 'Read the picture graph. Look at the key first.', figure=pg([('Football', 6), ('Swimming', 4), ('Chess', 3), ('Art', 5)], {'value': 5}, width_mm=118),
   partsrow=True, parts=[P('a', 'Chess: {b} children', '15'), P('b', 'More children chose football than swimming: {b}', '10'), P('c', 'Children altogether: {b}', '90')],
   why='Each picture stands for 5 children. (a) Chess has 3 pictures: 3 × 5 = 15. (b) Football has 2 more pictures than swimming: 2 × 5 = 10 more. (c) 6 + 4 + 3 + 5 = 18 pictures, and 18 × 5 = 90 children.'),
 I('start', 1, '75 children chose a club. The Art row is not drawn yet.', figure=pg([('Football', 5), ('Swimming', 3), ('Chess', 4), ('Art', None)], {'value': 5}, width_mm=118),
   partsrow=True, parts=[P('a', 'Art needs {b} pictures.', '3'), P('b', '{b} children chose Art.', '15')],
   why='75 children is 75 ÷ 5 = 15 pictures altogether. The other rows have 5 + 3 + 4 = 12 pictures. So Art needs 15 - 12 = 3 pictures, which is 15 children.'),
 I('start', 2, 'Ali counts the pets in his street. He makes a tally chart. A group of 5 has 4 strokes and a slash.', figure={'type': 'l2_tally', 'rows': [{'label': 'Cats', 'n': 7}, {'label': 'Dogs', 'n': 12}, {'label': 'Fish', 'n': 4}], 'width_mm': 88},
   partsrow=True, parts=[P('a', 'Dogs: {b}', '12'), P('b', 'More dogs than cats: {b}', '5'), P('c', 'All the pets: {b}', '23')],
   why='Count in 5s for each group with a slash, then add the strokes. Dogs: 5 + 5 + 2 = 12. Cats: 5 + 2 = 7. Fish: 4. (b) 12 - 7 = 5. (c) 7 + 12 + 4 = 23.'),
 I('start', 2, 'The cards 7, 0 and 5 can build 3-digit numbers. Use each card once.', figure={'type': 'l2_cards', 'items': [7, 0, 5], 'width_mm': 44},
   parts=[P('a', 'List every number in order:  {ll}', ['507', '570', '705', '750'], '507, 570, 705, 750', lst=True), P('b', 'The greatest is {b} and the smallest is {b}.', ['750', '507'], '750 and 507'), P('c', 'How many are between 600 and 800? {b}', '2')],
   why='0 cannot be first. Start with 5: 507, 570. Start with 7: 705, 750. (b) Greatest 750, smallest 507. (c) 705 and 750 are between 600 and 800: 2 numbers.'),
 I('start', 2, 'Ben has 6 coins. Each coin is 10¢ or 20¢. They are worth $1.10 altogether. Fill in the table.',
   figure=TB(['10¢ coins', '6', '5', '4', '3', '2', '1'], [['20¢ coins', '0', '1', '2', '3', '4', '5'], ['Total', '60¢', '70¢', None, None, None, None]], w=104, ws=[1.9, 1, 1, 1, 1, 1, 1], size=30),
   parts=[P('a', 'Write the 4 missing totals: {ll}', ['80', '90', '100', '110'], '80¢, 90¢, 100¢, 110¢', lst=True), P('b', 'Ben has {b} coins of 10¢ and {b} coins of 20¢.', ['1', '5'], '1 coin of 10¢ and 5 coins of 20¢')],
   why='Each swap of a 10¢ for a 20¢ adds 10¢: 60, 70, 80, 90, 100, 110. $1.10 is the last column: 1 coin of 10¢ and 5 coins of 20¢. Check: 10 + 100 = 110 and 1 + 5 = 6 coins.'),
 I('start', 3, 'Ali, Mei and Ravi each have 1 fruit: an apple, a banana or a mango. Mei has the mango. Ali does not have the apple.', figure={'type': 'l2_lgrid', 'rows': ['Ali', 'Mei', 'Ravi'], 'cols': ['apple', 'banana', 'mango'], 'width_mm': 80}, figside=True,
   parts=[P('a', 'Ali has the {bw}', 'banana'), P('b', 'Mei has the {bw}', 'mango'), P('c', 'Ravi has the {bw}', 'apple')],
   why='Mei has the mango, so cross out mango for Ali and Ravi. Ali does not have the apple and not the mango, so Ali has the banana. Ravi has the apple.'),
 I('start', 3, 'Mei cuts a pizza into 6 equal slices. She eats 1/6 and Ali eats 2/6. Each slice is 100 g. Write fractions in sixths.', parts=[
   P('a', 'They eat {b} of the pizza.', '3/6'), P('b', '{b} of the pizza is left.', '3/6'), P('c', 'The mass of the pizza left is {b} g.', '300')],
   why='(a) 1/6 + 2/6 = 3/6. (b) 6/6 - 3/6 = 3/6. (c) 3 slices left, 3 × 100 g = 300 g.'),
 I('start', 3, 'Aisha buys 3 pens. Each pen costs $1.20. She pays with a $5 note.', parts=[
   P('a', 'The pens cost $ {b}', '3.60'), P('b', 'Her change is $ {b}', '1.40')],
   why='(a) $1.20 + $1.20 + $1.20 = $3.60. (b) $5 - $3.60 = $1.40. Count on: $3.60 to $4 is 40¢, then $1 more makes $5.'),
 I('start', 1, 'I am a number between 40 and 60. I am in the 5 times table. My digits add up to 10. What number am I? {b}', value='55',
   why='Numbers between 40 and 60 in the 5 times table: 45, 50, 55. Digit sums: 4 + 5 = 9, 5 + 0 = 5, 5 + 5 = 10. So the number is 55.'),
 I('start', 3, 'A hall has 4 rows of 10 chairs. 28 children sit down.', parts=[
   P('a', 'The hall has {b} chairs.', '40'), P('b', '{b} chairs are empty.', '12')],
   why='(a) 4 rows of 10: 4 × 10 = 40. (b) 40 - 28 = 12 empty chairs.'),
 # Think harder
 I('think', 4, 'Ali, Mei, Siti and Ben like swimming, chess, art or tennis, one each. Mei likes chess. Ali does not like chess or art. Siti does not like swimming or tennis. Ben does not like tennis.',
   figure={'type': 'l2_lgrid', 'rows': ['Ali', 'Mei', 'Siti', 'Ben'], 'cols': ['swim', 'chess', 'art', 'tennis'], 'cell': 82, 'width_mm': 62}, figside=True,
   parts=[P('a', 'Ali: {bw}', 'tennis'), P('b', 'Mei: {bw}', 'chess'), P('c', 'Siti: {bw}', 'art'), P('d', 'Ben: {bw}', 'swimming')],
   hint='Tick Mei and chess. Cross out the rest of its row and column.',
   why='Siti is not swimming or tennis, and chess is taken, so Siti has art. Ali is not chess or art, so Ali has swimming or tennis. Ben is not tennis, so Ben has swimming. Ali has tennis.'),
 I('think', 4, 'The key was lost. Apples have 7 pictures and pears have 3. 20 more children chose apples.', figure=pg([('Apples', 7), ('Pears', 3)], None, width_mm=88),
   partsrow=True, parts=[P('a', 'Each picture stands for {b} children.', '5'), P('b', 'Apples: {b} children', '35'), P('c', 'Pears: {b} children', '15')],
   hint='4 more pictures is 20 children. How many in 1 picture?',
   why='Apples have 7 - 3 = 4 more pictures than pears. 4 pictures are 20 children, so 1 picture is 20 ÷ 4 = 5 children. Apples: 7 × 5 = 35. Pears: 3 × 5 = 15. Check: 35 - 15 = 20.'),
 I('think', 4, 'Pump A adds 2 l in minute 1, 4 l in minute 2, 6 l in minute 3, and so on. Pump B adds 5 l every minute. Compare the totals in the tank.',
   partsrow=True, parts=[P('a', 'Pump A first adds more than pump B by minute {b}.', '5'), P('b', 'Then pump A has {b} l more.', '5')],
   hint='Add each minute to the total of the minute before.',
   why='Pump A adds 2, 4, 6, 8, 10 so its totals are 2, 6, 12, 20, 30. Pump B adds 5 a minute: 5, 10, 15, 20, 25. At minute 4 they are level at 20 l. At minute 5 pump A has 30 l and pump B has 25 l, so pump A has 5 l more.'),
 # Go further
 I('go', 5, 'Half a picture. Each picture stands for 10 children, so half a picture stands for 5 children.', beyond='Half pictures',
   figure=pg([('Dogs', 3.5), ('Cats', 2.5)], {'value': 10}, width_mm=90),
   partsrow=True, parts=[P('a', 'Dogs: {b} children', '35'), P('b', 'Cats: {b} children', '25'), P('c', 'More dogs than cats: {b}', '10')],
   hint='3 pictures is 30. Add the half picture.',
   why='(a) 3 pictures are 30 and half a picture is 5: 35. (b) 2 pictures are 20 and half a picture is 5: 25. (c) 35 - 25 = 10.'),
 I('go', 5, 'Ali has one 5¢ coin, one 10¢ coin and two 20¢ coins. He pays with one or more of them.', parts=[
   P('a', 'How many different amounts can he pay? {b}', '11'), P('b', 'Can he pay 60¢? {circ:Yes|No}', 'No')],
   hint='List the amounts in order: 5¢, 10¢, 15¢ ...',
   why='All 4 coins are worth 5 + 10 + 20 + 20 = 55¢, so 60¢ is too much. The amounts are 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 and 55: 11 amounts. Every multiple of 5 from 5¢ to 55¢ works.'),
 I('go', 5, 'Make your own logic puzzle. Three children have a cat, a dog and a fish. Write 2 clues so only ONE answer fits. Many answers are right.', value='open',
   atext='Open. Example: Ali, Mei and Ravi have a cat, a dog and a fish. Mei has the fish. Ali does not have the cat. Then Ali has the dog and Ravi has the cat.', space={'rows': ['My clues:']},
   hint='Pick the answer first. Then write clues that rule out the rest.',
   why='A good puzzle has exactly one answer. Example: Mei has the fish (so Ali and Ravi have the cat and the dog). Ali does not have the cat, so Ali has the dog and Ravi has the cat. Try to find a second answer: there is none.'),
 I('go', 5, 'Ali buys 8 stickers. Small stickers cost 30¢. Large stickers cost 50¢. He pays $3.40 altogether.', parts=[
   P('a', 'He buys {b} small stickers and {b} large stickers.', ['3', '5'], '3 small and 5 large'), P('b', 'Could 8 stickers cost $3.30? {circ:Yes|No}', 'No')],
   hint='Start with 8 small stickers. Each swap adds 20¢.',
   why='8 small stickers cost $2.40. Each swap to a large adds 20¢: $2.60, $2.80, $3.00, $3.20, $3.40. That is 5 swaps: 5 large, 3 small. Totals rise in 20¢ steps, so $3.30 never happens.'),
 # Check yourself
 I('quiz', 0, 'Each picture stands for 10 children. How many children chose Tuesday? {b}', figure=pg([('Monday', 3), ('Tuesday', 5)], {'value': 10}, width_mm=84), figright=True, value='50', why='Tuesday has 5 pictures. Each picture is 10 children. 5 × 10 = 50 children.'),
 I('quiz', 0, 'Use the digit cards 1, 0 and 4 once each. How many 3-digit numbers can you make? {b}', value='4', why='0 cannot be first. Start with 1: 104, 140. Start with 4: 401, 410. That is 4 numbers.'),
 I('quiz', 0, 'Ali, Ben and Mei have red, blue and green. Mei has blue. Ali does not have red. Ben has {b}', value='red', why='Mei has blue. Ali does not have red, so Ali has green. Ben has red.'),
 I('quiz', 0, 'A pizza has 12 slices. 5/12 is eaten. Left, in twelfths: {b}', value='7/12', why='12/12 - 5/12 = 7/12 is left.'),
]
build(10, 'Puzzle day', 'Mixed puzzles', 'I can choose a way to start a puzzle. I can read picture graphs and logic grids. I can check my answer against every clue.', learn, items, snug=['start1', 'start2', 'start3'])
