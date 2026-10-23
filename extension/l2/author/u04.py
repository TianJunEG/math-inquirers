import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

def pat(items, **kw):
    d = {'type': 'l2_pattern', 'items': items}
    d.update(kw)
    return d

learn = {
 'intro': 'A repeating pattern is one group again and again. The last shape of each group is in a times table. A growing pattern goes up by the same number each step. A table helps.',
 'example': {
  'problem': 'This pattern repeats again and again. What is the 26th shape?',
  'figure': pat(['triangle', 'circle', 'circle', 'square'] * 3, per_row=12, sep=4, width_mm=150),
  'steps': ['One group has 4 shapes: triangle, circle, circle, square.', 'Groups end in the 4 times table: 4, 8, 12, 16, 20, 24.', 'Place 24 is the last shape of a group, a square.', 'Place 25 starts again with a triangle. Place 26 is a circle.'],
  'answer': 'The 26th shape is a circle.'},
 'howto': {'title': 'How to find a far place', 'steps': ['Find the size of one group.', 'Count in groups to near your place.', 'That place is the LAST shape of a group.', 'Count on to your place.']},
 'facts': {'title': 'Growing patterns', 'lines': ['Each step adds the same number.', 'A table shows the steps and the rule.', 'Check: is the number in the pattern?']},
 'try': {'text': 'The pattern star, square, square repeats again and again. What is the 14th shape?   {circ:star|square}', 'answer': A('square'),
         'explanation': 'One group has 3 shapes. 12 is in the 3 times table, so place 12 is the last shape of a group. Place 13 is a star and place 14 is a square.'}}

TB = lambda cols, rows, w=150, ws=None, **kw: {'type': 'l2_table', 'cols': cols, 'rows': rows, 'first_bold': True, 'widths': ws or [2.2] + [1] * (len(cols) - 1), 'width_mm': w, **kw}

items = [
 I('start', 1, 'Each step takes away 5. Write the next numbers.   60,   55,   50,   {b},   {b},   {b}', value=['45', '40', '35'], atext='45, 40, 35', why='Take away 5 each time: 50 - 5 = 45, 45 - 5 = 40, 40 - 5 = 35. These numbers are in the 5 times table.'),
 I('start', 1, 'This pattern repeats. Here are places 1 to 10.', figure=pat(['star', 'square', 'square', 'circle', 'star', 'square', 'square', 'circle', 'star', 'square'], width_mm=150),
   partsrow=True, parts=[P('a', 'Place 16 is a   {circ:star|square|circle}', 'circle'), P('b', 'Place 22 is a   {circ:star|square|circle}', 'square'), P('c', 'Place 33 is a   {circ:star|square|circle}', 'star')],
   why='One group has 4 shapes. (a) 16 ends a group: a circle. (b) 20 ends a group, so 21 is a star and 22 is a square. (c) 32 ends a group, so 33 is a star.'),
 I('start', 1, 'Ali writes the letters of CHESS again and again.', figure=pat(list('CHESSCHESS'), width_mm=150),
   partsrow=True, parts=[P('a', 'The 17th letter is {b}', 'H'), P('b', 'The 6th E is in place {b}', '28'), P('c', 'In 30 letters there are {b} letters S.', '12')],
   why='One group is C, H, E, S, S. (a) 15 ends a group, so 16 is C and 17 is H. (b) E is 3rd in a group: 3, 8, 13, 18, 23, 28. (c) 6 groups with 2 S each: 12.'),
 I('start', 1, 'A bead string has 1 square bead, then 4 round beads, again and again. Here are the first 10 beads.', figure=pat(['square', 'circle', 'circle', 'circle', 'circle', 'square', 'circle', 'circle', 'circle', 'circle'], width_mm=150, numbers=False),
   parts=[P('a', 'The string has 8 square beads. How many round beads are there? {b}', '32'), P('b', 'How many beads are on the string altogether? {b}', '40')],
   why='One group has 1 square and 4 round beads, 5 beads in all. 8 square beads means 8 groups. (a) 8 groups of 4 round beads: 8 × 4 = 32. (b) 8 groups of 5 beads: 8 × 5 = 40. Check: 8 + 32 = 40.'),
 I('start', 2, 'Each pizza is cut into 4 slices.', figure=TB(['Pizzas', '1', '2', '3', '4', '5', '6'], [['Slices', '4', None, None, None, None, None]]),
   parts=[P('a', 'Fill in the table.', ['8', '12', '16', '20', '24'], '8, 12, 16, 20, 24', lst=True), P('b', '10 pizzas have {b} slices.', '40'), P('c', '28 slices make {b} pizzas.', '7'),
          P('d', '14 slices make {b} pizzas and {b} slices are left over.', ['3', '2'], '3 pizzas and 2 slices')],
   why='Each pizza adds 4 slices: 4, 8, 12, 16, 20, 24. (b) 10 × 4 = 40. (c) 4 × 7 = 28. (d) 3 pizzas use 12 slices, and 14 - 12 = 2 slices are left over.'),
 I('start', 2, 'Sticks make a chain of squares. 1 square uses 4 sticks, 2 squares use 7 sticks and 3 squares use 10 sticks.', figure={'type': 'l2_sticks', 'kind': 'sq', 'counts': [1, 2, 3], 'width_mm': 96},
   parts=[P('a', '4 squares use {b} sticks.', '13'), P('b', '6 squares use {b} sticks.', '19'), P('c', '8 squares use {b} sticks.', '25')],
   why='Each new square adds 3 sticks: 4, 7, 10, 13, 16, 19, 22, 25. (a) 13. (b) 19. (c) 25. Another way: 8 squares need 8 × 3 = 24 sticks, plus 1 extra for the first side. 24 + 1 = 25.'),
 I('start', 3, 'Find the rule. Then write the next 2 numbers.', parts=[
   P('a', '7, 12, 17, 22, {b}, {b}    The rule is   {circ:add 4|add 5|add 7}', ['27', '32', 'add 5'], '27, 32 and add 5'),
   P('b', '50, 44, 38, {b}, {b}    The rule is   {circ:subtract 5|subtract 6|subtract 7}', ['32', '26', 'subtract 6'], '32, 26 and subtract 6')],
   why='(a) Each number is 5 more: 22 + 5 = 27 and 27 + 5 = 32. (b) Each number is 6 less: 38 - 6 = 32 and 32 - 6 = 26.'),
 I('start', 2, 'Siti counts in 3s from 3. Ravi counts in 5s from 5. Write each list up to 40 on the lines below the questions.', parts=[
   P('a', 'The numbers they both say are:  {ll}', ['15', '30'], '15 and 30', lst=True), P('b', 'The next number they both say is {b}', '45')],
   space={'rows': ['Siti: 3, 6, 9,', 'Ravi: 5, 10, 15,']},
   why='Siti: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39. Ravi: 5, 10, 15, 20, 25, 30, 35, 40. Both say 15 and 30. They meet every 15, so the next is 30 + 15 = 45.'),
 I('start', 3, 'A pattern goes triangle, circle, circle, again and again. Here are places 1 to 9.', figure=pat(['triangle', 'circle', 'circle'] * 3, width_mm=130),
   partsrow=True, parts=[P('a', '24 shapes make {b} groups of 3.', '8'), P('b', 'There are {b} circles in the first 24 shapes.', '16'), P('c', 'There are {b} triangles in the first 24 shapes.', '8')],
   why='(a) 24 ÷ 3 = 8 groups. (b) Each group has 2 circles: 8 × 2 = 16. (c) Each group has 1 triangle: 8 × 1 = 8. Check: 16 + 8 = 24.'),
 I('start', 3, 'Towers of cubes grow in the same way. Tower 1 is 5 cubes tall. Tower 2 is 7 cubes tall. Tower 3 is 9 cubes tall.', figure=TB(['Tower', '1', '2', '3', '4', '5', '6'], [['Cubes', '5', '7', '9', None, None, None]]),
   parts=[P('a', 'Fill in the table.', ['11', '13', '15'], '11, 13, 15', lst=True), P('b', 'Tower 10 has {b} cubes.', '23'), P('c', 'Tower {b} has 19 cubes.', '8')],
   space={'rows': ['Working:']},
   why='Each tower has 2 more cubes: 5, 7, 9, 11, 13, 15, 17, 19, 21, 23. Tower 10 has 23 cubes and tower 8 has 19 cubes. Another way: tower n has n × 2 + 3 cubes, so tower 10 has 20 + 3 = 23.'),
 # Think harder
 I('think', 4, 'A beetle starts at 0. It hops 3, then 1, then 3, then 1 ... It lands on 3, 4, 7, 8, 11 ...', parts=[
   P('a', 'Will it land on 27? {circ:Yes|No}', 'Yes'), P('b', 'Will it land on 26? {circ:Yes|No}', 'No'), P('c', 'Will it land on 40? {circ:Yes|No}', 'Yes')],
   space={'rows': ['Working:']}, hint='Write the landing places. Look at the 4 times table.',
   why='Every 2 hops the frog goes 4 further: 3, 4, 7, 8, 11, 12, 15, 16 ... It lands on the 4 times table and on the number 3 before each one. 27 = 24 + 3: yes. 26 is between 24 and 27: no. 40 = 4 × 10: yes.'),
 I('think', 4, 'This pattern repeats. Here are places 1 to 10. Could a star be in this place?', figure=pat(['square', 'star', 'circle', 'circle', 'triangle'] * 2, width_mm=140),
   partsrow=True, parts=[P('a', 'Place 17   {circ:Yes|No}', 'Yes'), P('b', 'Place 22   {circ:Yes|No}', 'Yes'), P('c', 'Place 35   {circ:Yes|No}', 'No'), P('d', 'Place 47   {circ:Yes|No}', 'Yes')],
   hint='Stars are 2 more than a number in the 5 times table.',
   why='The star is the 2nd of 5 shapes: places 2, 7, 12, 17, 22 ... (2 more than the 5 times table). 17 and 22: yes. 35 is the last shape: no. 47 = 45 + 2: yes.'),
 I('think', 4, 'A toy train has an engine and carriages. The engine holds 2 children. Each carriage holds 5 children.',
   figure=TB(['Carriages', '0', '1', '2', '3'], [['Children', '2', '7', '12', None]], w=110, ws=[1.8, 1, 1, 1, 1], size=30),
   parts=[P('a', '4 carriages hold {b} children.', '22'), P('b', '8 carriages hold {b} children.', '42'), P('c', '37 children fill {b} carriages.', '7')],
   hint='Each carriage adds 5. The engine is extra.',
   why='Each carriage adds 5 children, and the engine holds 2: 2, 7, 12, 17, 22 ... (a) 4 carriages: 2 + 20 = 22. (b) 8 carriages: 2 + 40 = 42. (c) 37 - 2 = 35 children are in carriages, and 35 ÷ 5 = 7 carriages.'),
 # Go further
 I('go', 5, '1, 4, 9, 16 are square numbers: 1 × 1, 2 × 2, 3 × 3, 4 × 4.', beyond='Square numbers', parts=[
   P('a', '6 × 6 = {b}', '36'), P('b', 'The next 2 square numbers after 25 are {b} and {b}.', ['36', '49'], '36 and 49'), P('c', 'The 10th square number is {b}', '100')],
   hint='A square number is a number times itself.',
   why='(a) 6 × 6 = 36. (b) After 5 × 5 = 25 come 6 × 6 = 36 and 7 × 7 = 49. (c) 10 × 10 = 100. The gaps grow by 2 each time: 3, 5, 7, 9 ...'),
 I('go', 5, 'Frog A lands on 4, 8, 12 ... (jumps of 4). Frog B starts on 1 and lands on 4, 7, 10 ... (jumps of 3).', parts=[
   P('a', 'Up to 30, they both land on {b}, {b} and {b}.', ['4', '16', '28'], '4, 16 and 28', lst=True), P('b', 'The next number they both land on is {b}', '40'),
   P('c', 'Frog C starts at 2 and jumps 4. Do A and C ever land on the same number? {circ:Yes|No}', 'No')],
   hint='They land together every 12. Why 12?',
   why='Frog A: 4, 8, 12 ... 40. Frog B: 1, 4, 7 ... 40. Both: 4, 16, 28, then 40: every 12, because 12 is in the 3 and 4 times tables. Frog C lands 2 more than the 4 times table, so it never meets Frog A.'),
 I('go', 5, 'The pattern star, circle, circle, square, square repeats again and again. Ravi says place 40 is a star. Siti says place 40 is a square.', parts=[
   P('a', 'Who is right? {circ:Ravi|Siti}', 'Siti'), P('b', 'Place 43 is a   {circ:star|circle|square}', 'circle')],
   hint='Place 40 is in the 5 times table. It is the last shape.',
   why='One group has 5 shapes and 40 is in the 5 times table, so place 40 is the last shape of a group: a square. Siti is right. Place 41 is a star, place 42 and place 43 are circles.'),
 I('go', 5, 'Make your own pattern of 4 shapes. It repeats again and again. Many answers are right.', value='open',
   atext='Open. Example: triangle, square, circle, circle. Place 28 ends a group, so place 29 is a triangle and place 30 is a square.',
   space={'rows': ['Draw the first 8 shapes:', 'Place 30 is a:']}, hint='Place 28 is the last shape of a group. Count on from there.',
   why='Example: triangle, square, circle, circle repeats. Groups end at 4, 8, ... 28. Place 28 is a circle, so place 29 is a triangle and place 30 is a square.'),
 # Check yourself
 I('quiz', 0, 'The pattern star, circle, square repeats again and again. The 20th shape is a   {circ:star|circle|square}', value='circle', why='One group has 3 shapes. 18 is in the 3 times table, so place 18 is a square. Place 19 is a star and place 20 is a circle.'),
 I('quiz', 0, 'Each box has 5 pens. 9 boxes have {b} pens.', value='45', why='9 groups of 5: 5, 10, 15, 20, 25, 30, 35, 40, 45.'),
 I('quiz', 0, 'Count in 4s from 4 and in 5s from 5, up to 40. How many numbers are in both lists? {b}', value='2', why='Ali says 4, 8, ... 40. Mei says 5, 10, ... 40. Both say 20 and 40. That is 2 numbers.'),
 I('quiz', 0, 'Tower 1 has 3 cubes, tower 2 has 7 and tower 3 has 11. Tower 6 has {b} cubes.', value='23', why='Each tower has 4 more: 3, 7, 11, 15, 19, 23. Tower 6 has 23 cubes.'),
]
build(4, 'Pattern machines', 'Patterns with multiplication', 'I can find far places in a repeating pattern. I can use a table and a rule for a growing pattern. I can find numbers that two counting patterns share.', learn, items, snug=['start1', 'start2', 'start3'])
