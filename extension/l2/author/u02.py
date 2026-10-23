import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

learn = {
 'intro': 'A missing digit is a mystery to solve. Start at the ones column and ask: did I carry? The = sign means "is the same as".',
 'example': {
  'problem': 'Find the missing digits in this sum.',
  'figure': {'type': 'l2_vsum', 'op': '+', 'rows': ['3?5', '24?', '617'], 'width_mm': 56}, 'side': True,
  'steps': ['Ones: 5 + ? must end in 7. So the missing digit is 2.',
            'Tens: ? + 4 must end in 1. 11 is possible: 7 + 4 = 11. Write 1 and carry 1.',
            'Hundreds: 3 + 2 + 1 carried = 6. It matches.',
            'Check: 375 + 242 = 617.'],
  'answer': 'The missing digits are 7 and 2.'},
 'howto': {'title': 'How to find a missing digit', 'steps': ['Start at the ones column.', 'Ask: did I carry?', 'Move left, one column at a time.', 'Check by adding the whole numbers.']},
 'facts': {'title': 'Balance', 'lines': ['= means "is the same as".', '260 + 150 = 410, so 300 + [ ] must be 410.', 'The box is 110.']},
 'try': {'text': 'Find the missing digit.   5?4 + 337 = 891   The digit is {b}', 'answer': A('5'), 'explanation': 'Ones: 4 + 7 = 11, write 1 and carry 1. Tens: 5 + 3 + 1 = 9, so the missing digit is 5. Check: 554 + 337 = 891.'}}

def vs(op, rows, label=None):
    d = {'op': op, 'rows': rows}
    if label:
        d['label'] = label
    return d

items = [
 I('start', 1, 'Find the missing digits. Each sum has 2. Write them in the answer boxes, top number first.',
   figure={'type': 'l2_vsum', 'sums': [vs('+', ['2?4', '35?', '603'], '(a)'), vs('+', ['4?8', '?26', '874'], '(b)'), vs('+', ['?65', '2?8', '703'], '(c)')], 'width_mm': 140},
   partsrow=True, parts=[P('a', 'Sum (a):  {b}  {b}', ['4', '9'], '4 and 9'),
          P('b', 'Sum (b):  {b}  {b}', ['4', '4'], '4 and 4'),
          P('c', 'Sum (c):  {b}  {b}', ['4', '3'], '4 and 3')],
   why='Work from the ones. (a) 4 + 9 = 13, so the bottom digit is 9 (carry 1). 4 + 5 + 1 = 10, so the top digit is 4. (b) 8 + 6 = 14 (carry 1). 4 + 2 + 1 = 7, so the top digit is 4. 4 + 4 = 8, so the bottom digit is 4. (c) 5 + 8 = 13 (carry 1). 6 + 3 + 1 = 10, so the bottom digit is 3. 4 + 2 + 1 = 7, so the top digit is 4.'),
 I('start', 1, 'Find the missing digits in these subtractions. Check each one by adding the answer to the number taken away. Write the digits top number first.',
   figure={'type': 'l2_vsum', 'sums': [vs('-', ['8?5', '26?', '568'], '(a)'), vs('-', ['5?2', '?47', '265'], '(b)')], 'width_mm': 110},
   partsrow=True, parts=[P('a', 'Sum (a):  {b}  {b}', ['3', '7'], '3 and 7'), P('b', 'Sum (b):  {b}  {b}', ['1', '2'], '1 and 2')],
   why='Turn each into an addition. (a) 568 + 267 = 835: 15, 13, 8 with carries. (b) 265 + 247 = 512: 12, 11, 5 with carries. So 835 - 267 = 568 and 512 - 247 = 265.'),
 I('start', 1, 'Both sides must have the same value. Fill in the boxes.', partsrow=True, parts=[
   P('a', '270 + 140 = 300 + {b}', '110'), P('b', '840 - 300 = {b} - 200', '740'), P('c', '360 + {b} = 400 + 150', '190'),
   P('d', '199 + 250 = 200 + 249   {circ:True|False}', 'True')],
   why='(a) 270 + 140 = 410, and 410 - 300 = 110. (b) 840 - 300 = 540, and 540 + 200 = 740. (c) 400 + 150 = 550, and 550 - 360 = 190. (d) 199 is 1 less than 200 and 250 is 1 more than 249, so both sides are 449.'),
 I('start', 2, 'This is a magic square. Every row, column and corner-to-corner line has the same total.',
   figure={'type': 'l2_grid', 'values': [[100, None, 300], [None, 250, None], [200, None, 400]], 'cell': 80, 'width_mm': 60}, figside=True,
   parts=[P('a', 'The magic total is {b}', '750'),
          P('b', 'Fill in the 4 empty squares.', ['350', '450', '50', '150'], '350 (top), 450 (left), 50 (right), 150 (bottom)', lst=True)],
   why='A line with all 3 numbers: 100 + 250 + 400 = 750. Top row: 750 - 100 - 300 = 350. Left column: 750 - 100 - 200 = 450. Right column: 750 - 300 - 400 = 50. Bottom row: 750 - 200 - 400 = 150.'),
 I('start', 2, 'Ali and Ben have 460 stickers altogether. Ali has 80 more than Ben.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Ben', 'segs': [{'w': 6, 'unknown': True, 't': '?'}]}, {'label': 'Ali', 'segs': [{'w': 6, 'unknown': True, 't': '?'}, {'w': 2.6, 't': '80'}]}], 'brace': {'text': '460', 'rows': [0, 1]}, 'width_units': 400, 'width_mm': 100},
   parts=[P('a', 'Take away the extra 80: 460 - 80 = {b}', '380'), P('b', 'Ben has {b} stickers.', '190'), P('c', 'Ali has {b} stickers.', '270')],
   why='Without the extra 80, both have the same, and together they have 380. Half of 380 is 190, so Ben has 190. Ali has 190 + 80 = 270. Check: 190 + 270 = 460.'),
 I('start', 2, 'Ben wrote 614 - 278 = 346. He checks by adding.', parts=[
   P('a', '346 + 278 = {b}', '624'), P('b', 'Is Ben right?   {circ:Yes|No}', 'No'), P('c', 'The correct answer is {b}', '336')],
   why='(a) 346 + 278 = 624. (b) A right answer would add back to 614, so Ben is wrong. (c) 614 - 278 = 336. Check: 336 + 278 = 614. Ben may have forgotten that the tens had lent 1 ten, so his tens digit is 1 too big.'),
 I('start', 3, 'Ali had 345 stickers. He gave some away. Now he has 128 stickers.\n(1) 345 + [ ] = 128      (2) 345 - [ ] = 128\n(3) [ ] - 345 = 128      (4) 128 - [ ] = 345', parts=[
   P('a', 'Which number sentence matches the story?   {circ:(1)|(2)|(3)|(4)}', '(2)'), P('b', 'How many stickers did Ali give away? {b}', '217')],
   why='(a) He starts with 345 and takes some away, so 345 - [ ] = 128, which is (2). (b) 345 - 128 = 217. Check: 128 + 217 = 345.'),
 I('start', 3, 'Mei had 500 beads. She used some for a necklace and 135 for a bracelet. 210 beads were left. How many beads did she use for the necklace? {b}', value='155',
   space={'rows': ['Working:']}, why='Take away what she used and what was left: 500 - 135 - 210 = 155. Check: 155 + 135 + 210 = 500.'),
 I('start', 3, 'Add or subtract.', partsrow=True, parts=[
   P('a', '368 + 457 = {b}', '825'), P('b', '702 - 385 = {b}', '317'), P('c', '249 + 394 = {b}', '643'), P('d', '910 - 466 = {b}', '444')],
   why='Add the ones, then the tens, then the hundreds, and carry. (a) 8 + 7 = 15, 6 + 5 + 1 = 12, 3 + 4 + 1 = 8: 825. (b) 702 - 385 = 317 (check 317 + 385 = 702). (c) 9 + 4 = 13, 4 + 9 + 1 = 14, 2 + 3 + 1 = 6: 643. (d) 910 - 466 = 444 (check 444 + 466 = 910).'),
 I('start', 3, 'Make 1000. Fill in the missing number.', partsrow=True, parts=[
   P('a', '340 + {b} = 1000', '660'), P('b', '485 + {b} = 1000', '515'), P('c', '1000 - 755 = {b}', '245'), P('d', '{b} + 75 = 1000', '925')],
   why='(a) 1000 - 340 = 660. (b) 1000 - 485 = 515. (c) 1000 - 755 = 245. (d) 1000 - 75 = 925. Tip: make the ones 10, the tens 9 and the hundreds 9 to reach 999, then add 1.'),
 I('start', 3, "Lily's book has 500 pages. She has read 287 pages.", parts=[
   P('a', 'How many pages are left? {b}', '213'), P('b', 'Then she reads 120 more pages. How many pages are left now? {b}', '93')],
   why='(a) Count on: 287 + 13 = 300 and 300 + 200 = 500, so 13 + 200 = 213 pages are left. (b) 213 - 120 = 93 pages.'),
 # Think harder
 I('think', 4, 'Fill the 6 circles with 120, 135, 150, 165, 180 and 195. Use each number once. Each side must add to 450.',
   figure={'type': 'l2_triangle', 'values': [None] * 6, 'width_mm': 56}, figright=True,
   partsrow=True, parts=[P('a', 'Corners: {b}, {b}, {b}.', ['120', '135', '150'], '120, 135, 150'),
          P('b', 'Sides add up to 495. Corners: {b}, {b}, {b}.', ['165', '180', '195'], '165, 180, 195')],
   hint='Which numbers are used in 2 sides?',
   why='450: corners 120, 135, 150, and the sides are 195, 165 and 180. 495: the corners are the 3 greatest numbers 165, 180, 195, and the sides are 150, 120 and 135.'),
 I('think', 4, 'Circle True or False. Do not add both sides.', partsrow=True, parts=[
   P('a', '468 + 199 = 467 + 200   {circ:True|False}', 'True'), P('b', '350 + 240 = 340 + 260   {circ:True|False}', 'False'),
   P('c', '502 + 99 = 500 + 101   {circ:True|False}', 'True'), P('d', '275 + 275 = 250 + 310   {circ:True|False}', 'False')],
   hint='Move the same amount from one number to the other.',
   why='(a) True: 1 more and 1 less. (b) False: 10 more but 20 less, so 590 and 600. (c) True: 2 more and 2 less. (d) False: 550 and 560.'),
 I('think', 4, 'Ali, Ben and Siti have 530 stickers altogether. Ali has 60 more than Ben. Siti has 40 fewer than Ben.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Ali', 'segs': [{'w': 5, 'unknown': True, 't': '?'}, {'w': 2, 't': '60'}]}, {'label': 'Ben', 'segs': [{'w': 5, 'unknown': True, 't': '?'}]}, {'label': 'Siti', 'segs': [{'w': 3, 'unknown': True, 't': '?'}]}], 'brace': {'text': '530', 'rows': [0, 2]}, 'width_units': 400, 'width_mm': 80},
   partsrow=True, parts=[P('a', 'Ben has {b} stickers.', '170'), P('b', 'Ali has {b} stickers.', '230'), P('c', 'Siti has {b} stickers.', '130')],
   hint='Make all 3 bars the same length as Ben\'s bar.',
   why='Ali has 60 more and Siti 40 fewer, so the 3 have 20 more than 3 Bens. 530 - 20 = 510, and 510 ÷ 3 = 170 for Ben. Ali 230, Siti 130. Check: 230 + 170 + 130 = 530.'),
 # Go further
 I('go', 5, 'Ali and Mei have 540 stickers together. Mei and Ravi have 610 together. Ali and Ravi have 450 together. How many stickers does each child have?', partsrow=True, parts=[
   P('a', 'Ali has {b}', '190'), P('b', 'Mei has {b}', '350'), P('c', 'Ravi has {b}', '260')],
   hint='Add the 3 totals, then halve. That is all 3 children together.',
   why='540 + 610 + 450 = 1600 counts each child twice, so all 3 have 800. Ravi 800 - 540 = 260. Ali 800 - 610 = 190. Mei 800 - 450 = 350.'),
 I('go', 5, 'Reverse a 3-digit number by swapping its first digit and last digit. Then take the smaller number from the greater.', beyond='Patterns in subtraction', parts=[
   P('a', '742 - 247 = {b}      831 - 138 = {b}', ['495', '693'], '495 and 693'), P('b', 'What is the middle digit of both answers? {b}', '9'), P('c', 'Use the pattern: 954 - 459 = {b}', '495')],
   hint='Look at the middle digit. Add the digits of each answer.',
   why='(a) 742 - 247 = 495 and 831 - 138 = 693. (b) Both have 9 in the middle. (c) The answer is always a multiple of 99: 954 - 459 = 495 (5 × 99, and 9 - 4 = 5).'),
 I('go', 5, 'Make your own missing-digit sum. Add two 3-digit numbers and hide 2 digits. Only ONE pair of digits may work. Many answers are right.', value='open',
   atext='Open. Example: 4?6 + 37? = 801 (426 + 375). Test every digit for each box: only 2 and 5 work.',
   space={'rows': ['My sum:']}, hint='Start with a full sum. Then hide a digit in each number.',
   why='Example: 426 + 375 = 801. Ones: 6 + ? must end in 1, so the ones box is 5. That carries 1. Tens: ? + 7 + 1 must end in 0, so the tens box is 2. Check that no other digit fits in each box.'),
 I('go', 5, 'Mei adds 198 to her number. Ali takes 102 away from 900. They get the same answer.', parts=[
   P('a', 'Mei\'s number is {b}', '600'), P('b', 'Ravi adds 299 to his number. Siti takes 201 away from 1000. Same answer. Ravi\'s number is {b}', '500')],
   hint='Work out the answer Ali gets first.',
   why='(a) Ali gets 900 - 102 = 798. Mei\'s number plus 198 is 798, so it is 798 - 198 = 600. (b) Siti gets 1000 - 201 = 799. Ravi\'s number is 799 - 299 = 500. Check: 500 + 299 = 799.'),
 # Check yourself
 I('quiz', 0, 'Write the 2 missing digits.', figure={'type': 'l2_vsum', 'op': '+', 'rows': ['2?6', '43?', '689'], 'width_mm': 26}, figright=True, value=['5', '3'], atext='5 and 3', lst=True,
   why='Ones: 6 + 3 = 9, so the bottom box is 3. Tens: 5 + 3 = 8, so the top box is 5. Check: 256 + 433 = 689.'),
 I('quiz', 0, '530 + 160 = 600 + {b}', value='90', why='530 + 160 = 690, and 690 - 600 = 90.'),
 I('quiz', 0, 'Ravi had 800 stickers. He gave 175 to Mei and some to Ben. 350 were left. How many did Ben get? {b}', value='275', why='800 - 175 = 625. 625 - 350 = 275. Check: 175 + 275 + 350 = 800.'),
 I('quiz', 0, 'Two numbers add up to 420. One is 60 more. What is the smaller number? {b}', value='180', why='Take away the extra 60: 420 - 60 = 360. Half of 360 is 180. The numbers are 180 and 240.'),
]
build(2, 'Missing digit mysteries', 'Adding and subtracting to 1000', 'I can find missing digits in 3-digit sums. I can balance number sentences and solve magic squares and triangles.', learn, items, snug=['start1', 'start2', 'start3'])
