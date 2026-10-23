import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

learn = {
 'intro': 'A 3-digit number has hundreds, tens and ones. Where a digit sits tells you what it is worth. To find every number from some digit cards, make a list in order.',
 'example': {
  'problem': 'Use the digit cards 4, 1 and 7 once each. List every 3-digit number you can make. Which is the biggest? Which is the smallest?',
  'figure': {'type': 'l2_cards', 'items': [4, 1, 7], 'width_mm': 60},
  'steps': ['Put 1 in the hundreds place. Swap the other two cards: 147 and 174.',
            'Put 4 in the hundreds place: 417 and 471.',
            'Put 7 in the hundreds place: 714 and 741.',
            'Check: 3 cards start the list, and each starts 2 numbers. 3 x 2 = 6 numbers.'],
  'answer': '147, 174, 417, 471, 714, 741. Biggest 741, smallest 147.'},
 'howto': {'title': 'How to list in order', 'steps': ['Fix one card in the hundreds place.', 'Swap the other two cards.', 'Do the same for each card.', 'Count: cards x 2 = how many numbers?']},
 'facts': {'title': 'Place value', 'lines': ['624 is 6 hundreds, 2 tens and 4 ones.', '10 tens make 1 hundred, so 12 tens is 120.', '0 cannot be the hundreds digit. 047 is not a 3-digit number.']},
 'try': {'text': 'Use the cards 9, 0 and 3 once each. How many 3-digit numbers can you make? {b}', 'figure': {'type': 'l2_cards', 'items': [9, 0, 3], 'width_mm': 50},
         'answer': A('4', '4'), 'explanation': 'List in order: 309, 390, 903, 930. A number cannot start with 0, so 039 and 093 do not count.'}}

items = [
 # ---- Start here, page 1
 I('start', 1, 'Place value. Fill in the blanks.', parts=[
   P('a', '3 hundreds, 5 tens and 6 ones = {b}', '356'), P('b', '8 hundreds, 0 tens and 4 ones = {b}', '804'),
   P('c', '590 = 5 hundreds and {b} tens', '9'), P('d', 'In 837, the digit 3 is worth {b}', '30')],
   why='(a) 300 + 50 + 6 = 356. (b) 800 + 0 + 4 = 804. (c) 590 is 500 + 90, and 90 is 9 tens. (d) The 3 is in the tens place, so it is worth 30.'),
 I('start', 1, 'Look at the base-ten blocks.', figure={'type': 'l2_blocks', 'groups': [{'flats': 3, 'rods': 12, 'ones': 4}], 'rods_per_row': 6, 'ones_per_row': 2, 'width_mm': 150},
   parts=[P('a', 'The blocks show the number {b}', '424'), P('b', 'Swap 10 rods for 1 flat. Now there are {b} flats, {b} rods and {b} ones.', ['4', '2', '4'], '4, 2, 4')],
   why='(a) 3 flats are 300, 12 rods are 120 and 4 ones are 4. 300 + 120 + 4 = 424. (b) 10 rods make 1 flat, so 12 rods become 1 flat and 2 rods: 4 flats, 2 rods, 4 ones.'),
 I('start', 1, 'Use the digit cards 8, 1 and 5 once each. Write every 3-digit number you can make in the table.', figure={'type': 'l2_cards', 'items': [8, 1, 5], 'width_mm': 56},
   value=['158', '185', '518', '581', '815', '851'], atext='158, 185, 518, 581, 815, 851', lst=True,
   space={'table': {'cols': ['Start with 1', 'Start with 5', 'Start with 8'], 'rows': 2}},
   why='Start with 1: 158 and 185. Start with 5: 518 and 581. Start with 8: 815 and 851. 3 cards x 2 = 6 numbers.'),
 I('start', 1, 'Use your list from the question before.', parts=[
   P('a', 'The biggest number is {b} and the smallest is {b}.', ['851', '158'], '851 and 158'),
   P('b', 'Which number is closest to 600? {b}', '581'),
   P('c', 'How many of your numbers are odd? {b}', '4')],
   why='(a) The biggest digit goes first for the biggest number: 851. The smallest digit goes first for the smallest: 158. (b) 581 is only 19 away from 600; 518 is 82 away. (c) A number is odd if it ends in 1, 3, 5, 7 or 9: 185, 581, 815 and 851 are odd.'),
 # ---- page 2
 I('start', 2, 'Use the cards 6, 0 and 4 once each.', figure={'type': 'l2_cards', 'items': [6, 0, 4], 'width_mm': 56}, parts=[
   P('a', 'Write every 3-digit number you can make.  {ll}', ['406', '460', '604', '640'], '406, 460, 604, 640', lst=True),
   P('b', 'How many numbers did you write? {b}', '4')],
   why='0 cannot be the hundreds digit, so only 6 or 4 can start. Start with 4: 406 and 460. Start with 6: 604 and 640. That is 4 numbers.'),
 I('start', 2, 'Write <, = or > in each circle.', parts=[
   P('a', '745   {circ:<|=|>}   754', '<'), P('b', '306   {circ:<|=|>}   296', '>'),
   P('c', '5 hundreds 2 tens   {circ:<|=|>}   502', '>'), P('d', '88 tens   {circ:<|=|>}   880', '=')],
   why='(a) The hundreds are the same; 4 tens is less than 5 tens, so 745 < 754. (b) 3 hundreds is more than 2 hundreds, so 306 > 296. (c) 5 hundreds 2 tens is 520, and 520 > 502. (d) 88 tens is 880, so they are equal.'),
 I('start', 2, 'Arrange the numbers in order. Begin with the smallest.\n508,   85,   580,   805', value=['85', '508', '580', '805'], atext='85, 508, 580, 805', lst=True,
   space={'rows': ['{ll}']}, why='85 has only 2 digits, so it is the smallest. 508, 580 and 805 are 3-digit numbers. Compare the hundreds, then the tens: 508 < 580 < 805.'),
 I('start', 2, 'Look at the number line. It goes from 300 to 400.', figure={'type': 'l2_nline', 'lo': 300, 'hi': 400, 'step': 10, 'labels': [300, 350, 400], 'arrows': [{'at': 340, 'label': 'A'}, {'at': 370, 'label': 'B'}], 'width_mm': 150},
   parts=[P('a', 'Arrow A shows the number {b}', '340'), P('b', 'Arrow B shows the number {b}', '370'), P('c', 'B is {b} more than A.', '30')],
   why='Each mark is 10 more. (a) A is 4 marks after 300: 340. (b) B is 7 marks after 300: 370. (c) 370 - 340 = 30.'),
 I('start', 2, 'Words and numbers.', parts=[
   P('a', 'Write in numbers: four hundred and nine   {b}', '409'), P('b', 'Write in numbers: six hundred and fifty-two   {b}', '652'),
   P('c', 'Write in words: 570   {ll}', 'five hundred and seventy', 'five hundred and seventy'), P('d', 'Write in words: 813   {ll}', 'eight hundred and thirteen', 'eight hundred and thirteen')],
   why='(a) 400 + 9 = 409. (b) 600 + 50 + 2 = 652. (c) 570 is 5 hundreds and 70. (d) 813 is 8 hundreds and 13.'),
 # ---- page 3
 I('start', 3, 'These are pieces cut from a 1000 chart. Each row has 10 numbers. Fill in the empty squares.',
   figure={'type': 'l2_chart', 'pieces': [{'label': 'Piece A', 'rows': [[571, 572, None], [None, 582, 583], [591, None, None]]}, {'label': 'Piece B', 'rows': [['', None, ''], [None, 645, None], ['', None, '']]}], 'width_mm': 150},
   parts=[P('a', 'Piece A: write the 4 missing numbers in the empty squares.', ['573', '581', '592', '593'], '573, 581, 592, 593 (left to right, top to bottom)', lst=True),
          P('b', 'Piece B: write the 4 missing numbers in the empty squares.', ['635', '644', '646', '655'], '635, 644, 646, 655 (top, left, right, bottom)', lst=True),
          P('c', 'On the chart, the square 3 below 612 holds {b}', '642')],
   why='One square right is 1 more. One square down is 10 more. (a) 573, 581 = 582 - 1, 592 = 582 + 10, 593 = 583 + 10. (b) Above 645 is 635, left is 644, right is 646, below is 655. (c) 3 squares down is 30 more: 612 + 30 = 642.'),
 I('start', 3, 'I am a 3-digit number. My hundreds digit is 6. My ones digit is 2 less than my tens digit. My digits add up to 14. What number am I? {b}', value='653',
   why='The tens digit and ones digit add up to 14 - 6 = 8. The tens digit is 2 more than the ones digit: 5 and 3. So the number is 653.'),
 I('start', 3, 'I am a 3-digit number. My hundreds digit is 3. My digits add up to 7. List all the numbers I could be.', parts=[
   P('a', 'The numbers are:  {ll}', ['304', '313', '322', '331', '340'], '304, 313, 322, 331, 340', lst=True), P('b', 'How many numbers could I be? {b}', '5')],
   why='The tens and ones digits add up to 7 - 3 = 4: 0 and 4, 1 and 3, 2 and 2, 3 and 1, 4 and 0. That gives 304, 313, 322, 331 and 340.'),
 I('start', 3, 'Circle True or False.', parts=[
   P('a', '5 tens and 12 ones is the same as 62.   {circ:True|False}', 'True'), P('b', '7 hundreds is the same as 700 tens.   {circ:True|False}', 'False'),
   P('c', 'In 909, the two 9s are worth the same.   {circ:True|False}', 'False'), P('d', '10 hundreds is the same as 1000.   {circ:True|False}', 'True')],
   why='(a) 50 + 12 = 62, true. (b) 7 hundreds is 700, which is 70 tens, so false. (c) One 9 is worth 900 and the other is worth 9, so false. (d) 10 hundreds make 1000, true.'),
 I('start', 3, 'List the odd numbers between 412 and 424.', parts=[
   P('a', 'The odd numbers are:  {ll}', ['413', '415', '417', '419', '421', '423'], '413, 415, 417, 419, 421, 423', lst=True), P('b', 'How many odd numbers are there? {b}', '6')],
   why='Odd numbers end in 1, 3, 5, 7 or 9. From 413 count on in 2s: 413, 415, 417, 419, 421, 423. 424 is not odd and 412 is not between.'),
 # ---- Think harder
 I('think', 4, 'Use the cards 1, 4, 6 and 9. Pick 3 different cards each time. How many even 3-digit numbers can you make? {b}', value='12', figure={'type': 'l2_cards', 'items': [1, 4, 6, 9], 'width_mm': 70},
   hint='Fix the ones digit first. An even number ends in 4 or 6.',
   why='Even numbers end in 4 or 6. Ones digit 4: use 2 of 1, 6, 9 for the other places: 3 x 2 = 6 numbers. Ones digit 6: use 2 of 1, 4, 9: 6 numbers. 6 + 6 = 12.'),
 I('think', 4, 'I am an odd 3-digit number. My tens digit is 0. My digits add up to 11. List all the numbers I could be.', value=['209', '407', '605', '803'], atext='209, 407, 605, 803', lst=True,
   space={'rows': ['{ll}']}, hint='The hundreds and ones digits add up to 11. The ones digit is odd.',
   why='The hundreds and ones digits add up to 11 and the ones digit is odd: (2, 9), (4, 7), (6, 5), (8, 3). (10, 1) is not allowed. The numbers are 209, 407, 605 and 803.'),
 I('think', 4, 'Ali writes the numbers 1 to 100 in a row. How many times does he write the digit 7? {b}', value='20',
   hint='Count the 7s in the ones place. Then count the 7s in the tens place.',
   why='7s in the ones place: 7, 17, 27, ... 97 is 10 numbers. 7s in the tens place: 70 to 79 is 10 numbers. 77 has two 7s and is counted in both lists. 10 + 10 = 20.'),
 # ---- Go further
 I('go', 5, '10 hundreds make 1 thousand. We write 1 thousand as 1000.', beyond='Thousands', parts=[
   P('a', '4 thousands, 2 hundreds, 0 tens and 7 ones = {b}', '4207'), P('b', '1000 more than 2650 = {b}', '3650'), P('c', '25 hundreds = {b}', '2500')],
   hint='A thousand is 10 hundreds. Write the thousands digit first.',
   why='(a) 4000 + 200 + 0 + 7 = 4207. (b) Adding 1000 adds 1 to the thousands digit: 2650 becomes 3650. (c) 20 hundreds is 2000 and 5 hundreds is 500, so 2500.'),
 I('go', 5, 'A mirror number reads the same forwards and backwards, such as 262 and 909. How many 3-digit mirror numbers are there? {b}', value='90',
   hint='The ones digit must match the hundreds digit. Count the choices.',
   why='The hundreds digit can be 1 to 9: 9 choices. The tens digit can be 0 to 9: 10 choices. The ones digit must be the same as the hundreds digit. 9 x 10 = 90.'),
 I('go', 5, 'I am a 3-digit number. My tens digit is 5. My digits add up to 12. When my hundreds digit and ones digit swap places, the new number is 297 more than me. What number am I? {b}', value='255',
   hint='The hundreds and ones digits add up to 7. Try pairs and swap them.',
   why='The hundreds and ones digits add up to 12 - 5 = 7. Try 156: swapping gives 651, which is 495 more. Try 255: swapping gives 552, which is 297 more. So the number is 255.'),
 # ---- Check yourself
 I('quiz', 0, '7 hundreds and 13 tens = {b}', value='830', why='13 tens is 130. 700 + 130 = 830.'),
 I('quiz', 0, 'Use the cards 5, 0 and 8 once each. Write the biggest even 3-digit number. {b}', value='850', figure=None, why='An even number ends in 0 or 8. To be biggest, try 8 first: 850 ends in 0, so it is even. 850 is bigger than 580 and 508.'),
 I('quiz', 0, 'Count back in 10s.   312,   302,   292,   {b},   {b}', value=['282', '272'], atext='282, 272', why='Take away 10 each time. 292 - 10 = 282 and 282 - 10 = 272.'),
 I('quiz', 0, 'On a 1000 chart with 10 numbers in a row, the number directly below 596 is {b}', value='606', why='One square down is 10 more. 596 + 10 = 606.'),
]
build(1, 'Digit detectives', 'Numbers to 1000', 'I can read and build 3-digit numbers. I can list every number from a set of digit cards and use patterns on a 1000 chart.', learn, items)
