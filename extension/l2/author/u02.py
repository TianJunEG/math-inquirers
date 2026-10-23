import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

learn = {
 'intro': 'A missing digit is a mystery to solve. Start at the ones column and ask: was a ten carried? The = sign means "is the same as".',
 'example': {
  'problem': 'Find the missing digits in this sum.',
  'figure': {'type': 'l2_vsum', 'op': '+', 'rows': ['3?5', '24?', '617'], 'width_mm': 56}, 'side': True,
  'steps': ['Ones: 5 + ? must end in 7. So the missing digit is 2.',
            'Tens: ? + 4 must end in 1. 11 is possible: 7 + 4 = 11. Write 1 and carry 1.',
            'Hundreds: 3 + 2 + 1 carried = 6. It matches.',
            'Check: 375 + 242 = 617.'],
  'answer': 'The missing digits are 7 and 2.'},
 'howto': {'title': 'How to find a missing digit', 'steps': ['Start at the ones column.', 'Ask: was a ten carried?', 'Move left, one column at a time.', 'Check by adding the whole numbers.']},
 'facts': {'title': 'Balance', 'lines': ['= means "is the same as".', '260 + 150 = 410, so 300 + [ ] must be 410.', 'The box is 110.']},
 'try': {'text': 'Find the missing digit.   5?4 + 337 = 891   The digit is {b}', 'answer': A('5'), 'explanation': 'Ones: 4 + 7 = 11, write 1 and carry 1. Tens: 5 + 3 + 1 = 9, so the missing digit is 5. Check: 554 + 337 = 891.'}}

def vs(op, rows, label=None):
    d = {'op': op, 'rows': rows}
    if label:
        d['label'] = label
    return d

items = [
 I('start', 1, 'Find the missing digits. Write one digit in each empty box.',
   figure={'type': 'l2_vsum', 'sums': [vs('+', ['2?4', '35?', '603'], '(a)'), vs('+', ['4?8', '?26', '874'], '(b)'), vs('+', ['?65', '2?8', '703'], '(c)')], 'width_mm': 150},
   parts=[P('a', 'Sum (a): write the missing digits, top number first.', ['4', '9'], '4 and 9 (444... see Why)', lst=True),
          P('b', 'Sum (b): write the missing digits, top number first.', ['4', '4'], '4 and 4', lst=True),
          P('c', 'Sum (c): write the missing digits, top number first.', ['4', '3'], '4 and 3', lst=True)],
   why='(a) Ones: 4 + 9 = 13, carry 1. Tens: 4 + 5 + 1 = 10, carry 1. Hundreds: 2 + 3 + 1 = 6. So 244 + 359 = 603. (b) Ones: 8 + 6 = 14, carry 1. Tens: 4 + 2 + 1 = 7. Hundreds: 4 + 4 = 8. So 448 + 426 = 874. (c) Ones: 5 + 8 = 13, carry 1. Tens: 6 + 3 + 1 = 10, carry 1. Hundreds: 4 + 2 + 1 = 7. So 465 + 238 = 703.'),
 I('start', 1, 'Find the missing digits in these subtractions. Try a digit and check it. Check: answer + the number taken away = the start number.',
   figure={'type': 'l2_vsum', 'sums': [vs('-', ['8?5', '26?', '568'], '(a)'), vs('-', ['5?2', '?47', '265'], '(b)')], 'width_mm': 110},
   parts=[P('a', 'Sum (a): write the missing digits, top number first.', ['3', '7'], '3 and 7', lst=True), P('b', 'Sum (b): write the missing digits, top number first.', ['1', '2'], '1 and 2', lst=True)],
   why='Turn each one into an addition. (a) 568 + 267 = 835: ones 8 + 7 = 15, tens 6 + 6 + 1 = 13, hundreds 5 + 2 + 1 = 8. So 835 - 267 = 568. (b) 265 + 247 = 512: ones 5 + 7 = 12, tens 6 + 4 + 1 = 11, hundreds 2 + 2 + 1 = 5. So 512 - 247 = 265.'),
 I('start', 1, 'The = sign means "is the same as". Fill in the boxes.', partsrow=True, parts=[
   P('a', '270 + 140 = 300 + {b}', '110'), P('b', '840 - 300 = {b} - 200', '740'), P('c', '360 + {b} = 400 + 150', '190'),
   P('d', '199 + 250 = 200 + 249   {circ:True|False}', 'True')],
   why='(a) 270 + 140 = 410, and 410 - 300 = 110. (b) 840 - 300 = 540, and 540 + 200 = 740. (c) 400 + 150 = 550, and 550 - 360 = 190. (d) 199 is 1 less than 200 and 250 is 1 more than 249, so both sides are 449.'),
 I('start', 2, 'This is a magic square. Every row, column and corner-to-corner line has the same total.',
   figure={'type': 'l2_grid', 'values': [[100, None, 300], [None, 250, None], [200, None, 400]], 'cell': 80, 'width_mm': 60}, figside=True,
   parts=[P('a', 'The magic total is {b}', '750'),
          P('b', 'Fill in the 4 empty squares.', ['350', '450', '50', '150'], '350 (top), 450 (left), 50 (right), 150 (bottom)', lst=True)],
   why='A line with all 3 numbers: 100 + 250 + 400 = 750. Top row: 750 - 100 - 300 = 350. Left column: 750 - 100 - 200 = 450. Right column: 750 - 300 - 400 = 50. Bottom row: 750 - 200 - 400 = 150.'),
 I('start', 2, 'Ali and Ben have 460 stickers altogether. Ali has 80 more than Ben.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Ben', 'segs': [{'w': 6, 'unknown': True, 't': '?'}]}, {'label': 'Ali', 'segs': [{'w': 6, 'unknown': True, 't': '?'}, {'w': 2.6, 't': '80'}]}], 'brace': {'text': '460', 'rows': [0, 1]}, 'width_units': 400, 'width_mm': 110},
   parts=[P('a', 'Take away the extra 80: 460 - 80 = {b}', '380'), P('b', 'Ben has {b} stickers.', '190'), P('c', 'Ali has {b} stickers.', '270')],
   why='Without the extra 80, both have the same, and together they have 380. Half of 380 is 190, so Ben has 190. Ali has 190 + 80 = 270. Check: 190 + 270 = 460.'),
 I('start', 2, 'Mei had 500 beads. She used some for a necklace and 135 for a bracelet. 210 beads were left. How many beads did she use for the necklace? {b}', value='155',
   space={'rows': ['Working:']}, why='Work backwards: 210 beads are left and 135 were used for the bracelet, so 210 + 135 = 345 beads were not used for the necklace... 500 - 345 = 155 beads were used for the necklace. Check: 155 + 135 + 210 = 500.'),
 I('start', 2, 'Ben wrote 614 - 278 = 346. He checks by adding.', parts=[
   P('a', '346 + 278 = {b}', '624'), P('b', 'Is Ben right?   {circ:Yes|No}', 'No'), P('c', 'The correct answer is {b}', '336')],
   why='(a) 346 + 278 = 624. (b) A right answer would give 614 when you add back, so Ben is wrong. (c) 614 - 278: ones 14 - 8 = 6, tens 0 lent 1 so borrow again 10 + 0 - 1 - 7 = 2... in short 614 - 278 = 336. Check: 336 + 278 = 614.'),
 I('start', 3, 'Ali had 345 stickers. He gave some away. Now he has 128 stickers.\n(1) 345 + [ ] = 128      (2) 345 - [ ] = 128\n(3) [ ] - 345 = 128      (4) 128 - [ ] = 345', parts=[
   P('a', 'Which number sentence matches the story?   {circ:(1)|(2)|(3)|(4)}', '(2)'), P('b', 'How many stickers did Ali give away? {b}', '217')],
   why='(a) He starts with 345 and takes some away, so 345 - [ ] = 128, which is (2). (b) 345 - 128 = 217. Check: 128 + 217 = 345.'),
 I('start', 3, 'Add or subtract.', partsrow=True, parts=[
   P('a', '368 + 457 = {b}', '825'), P('b', '702 - 385 = {b}', '317'), P('c', '249 + 394 = {b}', '643'), P('d', '910 - 466 = {b}', '444')],
   why='(a) 368 + 457 = 825. (b) 702 - 385 = 317. (c) 249 + 394 = 643. (d) 910 - 466 = 444. Check each answer by doing the opposite.'),
 I('start', 3, 'Make 1000. Fill in the missing number.', partsrow=True, parts=[
   P('a', '340 + {b} = 1000', '660'), P('b', '485 + {b} = 1000', '515'), P('c', '1000 - 755 = {b}', '245'), P('d', '{b} + 75 = 1000', '925')],
   why='(a) 1000 - 340 = 660. (b) 1000 - 485 = 515. (c) 1000 - 755 = 245. (d) 1000 - 75 = 925. Tip: make the ones 10, the tens 9 and the hundreds 9 to reach 999, then add 1.'),
 I('start', 3, "Lily's book has 500 pages. She has read 287 pages.", parts=[
   P('a', 'How many pages are left? {b}', '213'), P('b', 'Then she reads 120 more pages. How many pages are left now? {b}', '93')],
   why='(a) 500 - 287 = 213. (b) 213 - 120 = 93.'),
 # Think harder
 I('think', 4, 'Put the numbers 120, 135, 150, 165, 180 and 195 in the circles of each triangle, once each. In triangle A every side adds up to 450. In triangle B every side adds up to 495.',
   figure={'type': 'l2_triangle', 'triangles': [{'values': [None] * 6, 'caption': 'Triangle A: sides 450'}, {'values': [None] * 6, 'caption': 'Triangle B: sides 495'}], 'width_mm': 160},
   parts=[P('a', 'Triangle A: the 3 corner numbers are {ll}', ['120', '135', '150'], '120, 135, 150', lst=True), P('b', 'Triangle B: the 3 corner numbers are {ll}', ['165', '180', '195'], '165, 180, 195', lst=True)],
   hint='Corner numbers are used in 2 sides. Try the 3 smallest corners.',
   why='A: corners 120, 135, 150. Between 120 and 135: 450 - 255 = 195. Between 135 and 150: 450 - 285 = 165. Between 150 and 120: 450 - 270 = 180. B: corners 165, 180, 195. Between 165 and 180: 150. Between 180 and 195: 120. Between 195 and 165: 135. Each side adds up to 495.'),
 I('think', 4, 'Circle True or False. Do not add both sides. Say why on the line.', parts=[
   P('a', '468 + 199 = 467 + 200   {circ:True|False}', 'True'), P('b', '350 + 240 = 340 + 260   {circ:True|False}', 'False'),
   P('c', '502 + 99 = 500 + 101   {circ:True|False}', 'True'), P('d', '275 + 275 = 250 + 310   {circ:True|False}', 'False')],
   space={'rows': ['Why (b):']}, hint='Move the same amount from one number to the other.',
   why='(a) 468 is 1 more than 467 and 199 is 1 less than 200: true. (b) 350 is 10 more than 340, but 240 is 20 less than 260, so the sides are 590 and 600: false. (c) 502 is 2 more than 500 and 99 is 2 less than 101: true. (d) 275 + 275 = 550 and 250 + 310 = 560: false.'),
 I('think', 4, 'Ali, Ben and Siti have 530 stickers altogether. Ali has 60 more than Ben. Siti has 40 fewer than Ben.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Ali', 'segs': [{'w': 5, 'unknown': True, 't': '?'}, {'w': 2, 't': '60'}]}, {'label': 'Ben', 'segs': [{'w': 5, 'unknown': True, 't': '?'}]}, {'label': 'Siti', 'segs': [{'w': 3, 'unknown': True, 't': '?'}]}], 'brace': {'text': '530', 'rows': [0, 2]}, 'width_units': 400, 'width_mm': 112},
   parts=[P('a', 'Ben has {b} stickers.', '170'), P('b', 'Ali has {b} stickers.', '230'), P('c', 'Siti has {b} stickers.', '130')],
   hint='Make all 3 bars the same length as Ben\'s bar.',
   why='Add 40 to Siti and take 60 off Ali: now all three have the same as Ben, and the total is 530 + 40 - 60 = 510... so 3 equal parts do not add to 510. Check again: Siti has 40 fewer, so adding 40 makes her equal to Ben (530 + 40 = 570). Ali has 60 more, so take 60 away (570 - 60 = 510). Three Bens are 510, so Ben has 170. Ali has 170 + 60 = 230 and Siti has 170 - 40 = 130. Check: 230 + 170 + 130 = 530.'),
 # Go further
 I('go', 5, 'Ali and Mei have 540 stickers together. Mei and Ravi have 610 together. Ali and Ravi have 450 together. How many stickers does each child have?', parts=[
   P('a', 'Ali has {b}', '190'), P('b', 'Mei has {b}', '350'), P('c', 'Ravi has {b}', '260')],
   space={'rows': ['Working:']}, hint='Add the 3 totals, then halve. That is all 3 children together.',
   why='Add the 3 totals: 540 + 610 + 450 = 1600. Each child is counted twice, so all 3 together have 800. Ravi = 800 - 540 = 260. Ali = 800 - 610 = 190. Mei = 800 - 450 = 350. Check: 190 + 350 = 540, 350 + 260 = 610, 190 + 260 = 450.'),
 I('go', 5, 'Swap the hundreds digit and the ones digit of a number. Then subtract the smaller number from the greater.', beyond='Patterns in subtraction', parts=[
   P('a', '742 and 247:  742 - 247 = {b}', '495'), P('b', '831 and 138:  831 - 138 = {b}', '693'), P('c', 'What is the middle digit of both answers? {b}', '9'), P('d', 'Use the pattern: 954 - 459 = {b}', '495')],
   hint='Look at the middle digit and the digit sum of each answer.',
   why='(a) 742 - 247 = 495. (b) 831 - 138 = 693. (c) Both answers have 9 in the middle. (d) The answer to a reverse-and-subtract is always a multiple of 99. 954 - 459 = 495. The hundreds digits 9 and 4 differ by 5, and 5 x 99 = 495.'),
 I('go', 5, 'Make your own missing-digit sum. Write 2 missing digits in an addition of two 3-digit numbers, so that only ONE pair of digits works. Many answers are right.', value='open',
   atext='Open. Example: 4?6 + 37? = 801 (426 + 375). Test every digit for each box: only 2 and 5 work.',
   space={'rows': ['My sum:', 'My answer:']}, hint='Start with a full sum. Then hide a digit in each number.',
   why='Example: 426 + 375 = 801. Ones: 6 + ? must end in 1, so the ones box is 5. That carries 1. Tens: ? + 7 + 1 must end in 0, so the tens box is 2. Check that no other digit fits in each box.'),
 I('go', 5, 'The same number goes in both boxes. Find it. Check your answer.', parts=[
   P('a', '[ ] + 175 = 625 - [ ]    The number is {b}', '225'), P('b', '[ ] + 240 = 800 - [ ]    The number is {b}', '280')],
   hint='Both sides must be equal. Try a number and check it.',
   why='(a) Move the box: 2 boxes = 625 - 175 = 450, so one box is 225. Check: 225 + 175 = 400 and 625 - 225 = 400. (b) 2 boxes = 800 - 240 = 560, so one box is 280. Check: 280 + 240 = 520 and 800 - 280 = 520.'),
 # Check yourself
 I('quiz', 0, 'Find the missing digits. Write them in the boxes.', figure={'type': 'l2_vsum', 'op': '+', 'rows': ['2?6', '43?', '689'], 'width_mm': 56}, value=['5', '3'], atext='5 and 3', lst=True,
   why='Ones: 6 + 3 = 9, so the bottom box is 3. Tens: 5 + 3 = 8, so the top box is 5. Check: 256 + 433 = 689.'),
 I('quiz', 0, '530 + 160 = 600 + {b}', value='90', why='530 + 160 = 690, and 690 - 600 = 90.'),
 I('quiz', 0, 'Ravi had 800 stickers. He gave 175 to Mei and some to Ben. He had 350 left. How many stickers did he give to Ben? {b}', value='275', why='800 - 175 = 625. 625 - 350 = 275. Check: 175 + 275 + 350 = 800.'),
 I('quiz', 0, 'Two numbers add up to 420. One is 60 more than the other. What is the smaller number? {b}', value='180', why='Take away the extra 60: 420 - 60 = 360. Half of 360 is 180. The numbers are 180 and 240.'),
]
build(2, 'Missing digit mysteries', 'Adding and subtracting to 1000', 'I can find missing digits in 3-digit sums. I can balance number sentences and solve magic squares and triangles.', learn, items, snug=['start1', 'start2', 'start3'])
