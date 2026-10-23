from lib import *

u = Unit(2, 'Cryptarithm crackers', 'Addition and subtraction',
         'I can find missing digits in sums and take-aways. I can solve magic squares and number pyramids.')
H4 = ['Th', 'H', 'T', 'O']


def vs(l1, sign, l2, res, w=64):
    return {'type': 'l3_vsum', 'heads': H4, 'width_mm': w, 'lines': [
        {'sign': '', 'cells': l1}, {'sign': sign, 'cells': l2, 'rule': True}, {'sign': '', 'cells': res}]}


u.learn(
    'In a missing-digit sum, work one column at a time. Start with the ones. Remember to add the digit you carried.',
    {'problem': 'Find the 2 missing digits in this sum.',
     'figure': vs([4, 5, None, 7], '+', [1, None, 6, 8], [5, 8, 9, 5], 64),
     'steps': ['Ones: 7 + 8 = 15. Write 5 and carry 1.',
               'Tens: ? + 6 + 1 carried must end in 9. So ? is 2.',
               'Hundreds: 5 + ? makes 8. So ? is 3.',
               'Check the thousands: 4 + 1 = 5. It matches.'],
     'answer': '4527 + 1368 = 5895. The missing digits are 2 and 3.'},
    {'title': 'How to find a missing digit',
     'steps': ['Look at the ones column first.', 'Write the carried 1 above the next column.',
               'For a take-away, turn it round and add to check.']},
    {'text': 'Find the missing digit. {b}\n3?48 + 2517 = 5965', 'answer': A('4'),
     'explanation': 'Ones: 8 + 7 = 15, write 5 and carry 1. Tens: 4 + 1 + 1 = 6. Hundreds: ? + 5 makes 9, so ? is 4. Thousands: 3 + 2 = 5.'})

# ---------------- Start here (pages 1 to 3)
u.S(1, 'Find the missing digit in each sum.', parts=[
    P('a', '3?46 + 1251 = 4597    The missing digit is {b}.', A('3')),
    P('b', '26?9 + 1435 = 4104    The missing digit is {b}.', A('6'))],
    why='(a) Ones 6 + 1 = 7 and tens 4 + 5 = 9 are fine. Hundreds: ? + 2 = 5, so ? is 3. (b) Ones: 9 + 5 = 14, carry 1. Tens: ? + 3 + 1 ends in 0, so ? is 6 and 10 is made. Check: 2669 + 1435 = 4104.')
u.S(1, 'Find the missing digit in each take-away.', parts=[
    P('a', '6405 - 2?18 = 3687    The missing digit is {b}.', A('7')),
    P('b', '9?30 - 4617 = 4513    The missing digit is {b}.', A('1'))],
    why='Turn each one round and add. (a) 3687 + 2718 = 6405, so the digit is 7. (b) 4513 + 4617 = 9130, so the digit is 1.')
u.S(1, 'A theatre sells 3875 tickets on Saturday and 2968 tickets on Sunday.', parts=[
    P('a', 'It sells {b} tickets in all.', A('6843')), P('b', 'It sells {b} more tickets on Saturday than on Sunday.', A('907'))],
    why='(a) 3875 + 2968 = 6843. (b) 3875 - 2968 = 907. Check: 2968 + 907 = 3875.')
u.S(1, 'A baker has 8000 g of flour. He uses 2475 g on Monday and 3150 g on Tuesday. How many grams of flour are left? {b} g',
    A('2375'), why='First add what he used: 2475 + 3150 = 5625. Then 8000 - 5625 = 2375. Check: 5625 + 2375 = 8000.')
u.S(1, 'Siti works out 5000 - 1768 = 3342.', parts=[
    P('a', 'Check by adding: 3342 + 1768 = {b}', A('5110')),
    P('b', 'Is Siti right?   {circ:Yes|No}', A('No')),
    P('c', 'The correct answer is {b}.', A('3232'))],
    why='The check should give back 5000, but 3342 + 1768 = 5110. So Siti is not right. 5000 - 1768 = 3232. Check: 3232 + 1768 = 5000.')
u.S(1, 'Look for a pattern.', parts=[
    P('a', '2641 + {b} = 9999', A('7358')), P('b', '10 000 - 2641 = {b}', A('7359'))],
    why='(a) Each digit and its partner add up to 9: 2 and 7, 6 and 3, 4 and 5, 1 and 8. That gives 7358. (b) 10 000 is 1 more than 9999, so the answer is 1 more than 7358.')
u.S(2, 'Every row, column and diagonal has the same total.', parts=[
    P('a', 'The magic total is {b}.', A('1050')),
    P('b', 'A = {b}   B = {b}   C = {b}', A(['400', '250', '500'], 'A = 400, B = 250, C = 500', list=True))],
    why='The middle row is complete: 550 + 350 + 150 = 1050. Top row: 200 + 450 + A = 1050, so A = 400. Left column: 200 + 550 + 300 = 1050. Middle column: 450 + 350 + B = 1050, so B = 250. Bottom row: 300 + 250 + C = 1050, so C = 500.',
    figure={'type': 'l3_grid', 'rows': [[200, 450, {'t': 'A', 'fill': 'none', 'dash': True}], [550, 350, 150], [300, {'t': 'B', 'fill': 'none', 'dash': True}, {'t': 'C', 'fill': 'none', 'dash': True}]],
            'cw': 90, 'ch': 64, 'width_mm': 56}, figside=True)
u.S(2, 'A brick is made by adding the 2 bricks below it.', parts=[
    P('a', 'P = {b}', A('750')), P('b', 'Q = {b}', A('480'))],
    why='P and 830 make the top brick: 830 + P = 1580, so P = 750. Q and 270 make P: Q + 270 = 750, so Q = 480. Check: 350 + 480 = 830.',
    figure={'type': 'l3_pyramid', 'rows': [[1580], [830, '@P'], [350, '@Q', 270]], 'width_mm': 78}, figside=True)
u.S(2, 'Find the 2 missing digits.', parts=[
    P('a', 'The digit in the hundreds place of the top number is {b}.', A('6')),
    P('b', 'The digit in the tens place of the number being added is {b}.', A('9'))],
    why='Ones: 2 + 6 = 8. Tens: 5 + ? ends in 4, so ? is 9 and 1 is carried. Hundreds: ? + 4 + 1 ends in 1, so ? is 6 and 1 is carried. Thousands: 3 + 2 + 1 = 6. Check: 3652 + 2496 = 6148.',
    figure=vs([3, None, 5, 2], '+', [2, 4, None, 6], [6, 1, 4, 8], 60), figside=True)
u.S(2, 'Each letter stands for a digit. The same letter always means the same digit. Find the digit.', parts=[
    P('a', 'A3 + 2A = 56    A = {b}', A('3')),
    P('b', 'C5 + C5 = 90    C = {b}', A('4'))],
    why='(a) Try A = 3: 33 + 23 = 56. It works. (b) Two equal numbers add up to 90, so each is 45. Then C = 4.')
u.S(3, 'Find the 2 missing digits.', parts=[
    P('a', 'The digit in the hundreds place of the top number is {b}.', A('5')),
    P('b', 'The digit in the tens place of the number taken away is {b}.', A('4'))],
    why='Turn it round: 3657 + 2845 = 6502 (the missing digit of the number taken away is its tens digit 4). Or subtract by columns: 12 - 5 = 7, then 10 - 1 - 4 = 5, then 15 - 1 - 8 = 6, then 6 - 1 - 2 = 3. The top number is 6502.',
    figure=vs([6, None, 0, 2], '-', [2, 8, None, 5], [3, 6, 5, 7], 60), figside=True)
u.S(3, 'The sum of 2 numbers is 9000. One number is 3475. What is the other number? {b}', A('5525'),
    why='9000 - 3475 = 5525. Check: 3475 + 5525 = 9000.')
u.S(3, 'Use the cards once each to make two 3-digit numbers.', parts=[
    P('a', 'The greatest sum is {b}.', A('1595')), P('b', 'The smallest sum is {b}.', A('605'))],
    why='For the greatest sum, put the 2 greatest digits in the hundreds places. Then the next 2 in the tens places, and the last 2 in the ones places: 800 + 700 + 50 + 40 + 3 + 2 = 1595. For the smallest sum, do the same with the smallest digits first: 200 + 300 + 40 + 50 + 7 + 8 = 605.',
    figure={'type': 'l3_cards', 'items': [2, 3, 4, 5, 7, 8]})
u.S(3, 'A school collects 1875 cans in Week 1, 2430 cans in Week 2 and 1790 cans in Week 3.', parts=[
    P('a', 'It collects {b} cans in all.', A('6095')), P('b', 'It collects {b} more cans in Week 2 than in Week 3.', A('640'))],
    why='(a) 1875 + 2430 = 4305, and 4305 + 1790 = 6095. (b) 2430 - 1790 = 640. Check: 1790 + 640 = 2430.')

# ---------------- Think harder
u.T('Letters hide digits. The same letter is the same digit. Different letters are different digits.\nAB + AC = BBD', parts=[
    P('a', 'A = {b}', A('5')), P('b', 'B = {b}', A('1')), P('c', 'C = {b}', A('9')), P('d', 'D = {b}', A('0'))],
    hint='Two 2-digit numbers add up to less than 200. What is B?',
    why='Two 2-digit numbers make less than 200, so B = 1 and the answer starts 11. Ones: B + C = 1 + C ends in D. Tens: A + A + carry makes 11, so A = 5 with carry 1. Then 1 + C must be 10, so C = 9 and D = 0. Check: 51 + 59 = 110.',
    partsrow=True, space={'rows': ['My tries:', '']})
u.T('Use the cards 1, 3, 5, 6 and 8 once each. Make a 3-digit number and a 2-digit number. What is the smallest sum you can make? {b}', A('194'),
    figure={'type': 'l3_cards', 'items': [1, 3, 5, 6, 8]}, figright=True,
    hint='Which digits are worth the least? Which places are worth most?',
    why='The smallest digit, 1, goes in the hundreds place. The next smallest, 3 and 5, go in the two tens places. The others, 6 and 8, go in the ones places. For example 136 + 58 = 194, and every way of placing the digits like this gives 194.',
    space={'rows': ['My tries:', '', '']})
u.T('Look at this magic square. Every row, column and diagonal has the same total.', parts=[
    P('a', 'The magic total is {b}.', A('630')),
    P('b', 'A = {b}', A('240')), P('c', 'E = {b}', A('300'))],
    hint='The middle number is in 4 lines. Add those 4 lines.',
    why='Add the middle row, the middle column and the 2 diagonals. The middle number is counted 4 times, and every other number once, so 4 totals = all 9 numbers + 3 times the middle number. All 9 numbers make 3 totals, so the total is 3 times the middle: 3 x 210 = 630. Then A = 630 - 120 - 270 = 240 and E = 630 - 120 - 210 = 300.',
    figure={'type': 'l3_grid', 'rows': [[120, 270, {'t': 'A', 'fill': 'none', 'dash': True}], [{'t': '', 'fill': 'none', 'dash': True}, 210, {'t': '', 'fill': 'none', 'dash': True}], [180, {'t': '', 'fill': 'none', 'dash': True}, {'t': 'E', 'fill': 'none', 'dash': True}]],
            'cw': 90, 'ch': 64, 'width_mm': 56}, figside=True)

# ---------------- Go further
u.G('Letters hide digits. The same letter is the same digit. Different letters are different digits.\nABC + BC = CAB', parts=[
    P('a', 'A = {b}', A('2')), P('b', 'B = {b}', A('6')), P('c', 'C = {b}', A('3'))],
    hint='Look at the ones: C + C ends in B. List the choices for C.',
    why='Ones: C + C ends in B. Tens: B + B (+ carry) ends in A. Hundreds: A (+ carry) is C. Try C = 3: then B = 6, carry 0. Tens: 6 + 6 = 12, so A = 2 and carry 1. Hundreds: 2 + 1 = 3 = C. Check: 263 + 63 = 326. No other digits work.',
    partsrow=True, space={'rows': ['My tries:']})
u.G('Beyond Level 3: Pyramids with a hidden number.\nA brick is made by adding the 2 bricks below it. The 2 bricks marked X are equal. Find X. {b}',
    A('440'),
    figure={'type': 'l3_pyramid', 'rows': [[3280], [None, None], [None, None, None], [200, '@X', '@X', 440]], 'width_mm': 92},
    hint='Guess a number for X. Fill the pyramid. Is the top too big?',
    why='In this pyramid the end bricks of the bottom row count once in the top brick and the 2 middle bricks count 3 times each. So 200 + 3 X + 3 X + 440 = 3280. That is 640 + 6 X = 3280, so 6 X = 2640 and X = 440. Check: the next row is 640, 880, 880; then 1520, 1760; then 3280.',
    space={'rows': ['My guesses:']})
u.G('Beyond Level 3: Reversing digits.\nReverse the digits of a 2-digit number and add the 2 numbers.', parts=[
    P('a', '36 + 63 = {b}', A('99')), P('b', '58 + 85 = {b}', A('143')), P('c', '47 + 74 = {b}', A('121')),
    P('d', 'Each answer is in the {b} times table.', A('11'))],
    hint='Add the tens digit and ones digit. Compare with the answers.',
    why='99 = 9 x 11, 143 = 13 x 11, 121 = 11 x 11. Here is why. A 2-digit number with digits A and B is 10 A + B. Its reverse is 10 B + A. Together they make 11 A + 11 B, which is 11 x (A + B). So the answer is always in the 11 times table.',
    partsrow=True)
u.G('Make up a number pyramid puzzle of your own. The bottom row has 3 bricks. Show exactly 3 bricks and hide the other 3, so that only ONE answer fits. Swap puzzles with a grown-up.',
    A('800', 'Answers vary. Example: top brick 800, middle left brick 370, bottom right brick 180 shown. The hidden bricks are 430 (middle right), 250 (bottom middle) and 120 (bottom left).'),
    hint='Make a full pyramid first. Then hide 3 bricks.',
    why='Check that your pyramid adds up correctly and that the 3 shown bricks fix all the others. In the example: 800 - 370 = 430, then 430 - 180 = 250, then 370 - 250 = 120.',
    space={'rows': ['Draw my pyramid:']})

# ---------------- Check yourself
u.C('Find the missing digit. {b}\n4?72 + 2519 = 7091', A('5'),
    why='Ones: 2 + 9 = 11, carry 1. Tens: 7 + 1 + 1 = 9. Hundreds: ? + 5 ends in 0, so ? is 5 and 1 is carried. Thousands: 4 + 2 + 1 = 7.')
u.C('Find the missing digit. {b}\n8?04 - 3569 = 4635', A('2'),
    why='Turn it round: 4635 + 3569 = 8204, so the missing digit is 2.')
u.C('A brick is made by adding the 2 bricks below it. The brick M is {b}.', A('520'),
    figure={'type': 'l3_pyramid', 'rows': [[1160], ['@M', 640], [240, 280, 360]], 'width_mm': 60}, figright=True,
    why='M is the sum of 240 and 280: 240 + 280 = 520. Check: 520 + 640 = 1160.')
u.C('A zoo has 9000 visitors in 3 days. On Friday 2845 visitors come. On Saturday 3260 come. How many come on Sunday? {b}', A('2895'),
    why='2845 + 3260 = 6105. Then 9000 - 6105 = 2895. Check: 6105 + 2895 = 9000.')
u.save()
