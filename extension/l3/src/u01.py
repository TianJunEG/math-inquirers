from lib import *

u = Unit(1, 'Digits, cards and clues', 'Numbers to 10 000',
         'I can read, build and order 4-digit numbers. I can use clues to find a mystery number.')
cards = lambda *d: {'type': 'l3_cards', 'items': list(d)}

u.learn(
    'A 4-digit number has thousands, hundreds, tens and ones. The place decides what a digit is worth. A 0 can never be the first digit.',
    {'problem': 'Use the cards 7, 0, 4 and 9 once each. Make the greatest and the smallest 4-digit number.',
     'figure': cards(7, 0, 4, 9),
     'steps': ['Greatest: put the greatest digit in the thousands place. Then the next greatest. This gives 9740.',
               'Smallest: the first digit cannot be 0. Use the smallest digit that is not 0: the 4.',
               'Put the other digits in order after it, smallest first: 0, 7, 9. This gives 4079.'],
     'answer': 'Greatest 9740. Smallest 4079.'},
    {'title': 'How to make a number from cards',
     'steps': ['Th H T O: the place decides the worth. 1000 more changes the thousands digit.', 'Odd or even? Choose the ones digit first.',
               'Making a list? Fix the first digit, then list the rest from smallest.']},
    {'text': 'Make the greatest even number with the cards 3, 8, 1 and 4. Use each card once. {b}', 'figure': cards(3, 8, 1, 4),
     'answer': A('8314'),
     'explanation': 'An even number ends in 8 or 4. With 4 last, the other cards in order give 8314. With 8 last, the best is 4318. So 8314 is greater.'})

# ---------------- Start here, page 1
u.S(1, 'Look at the place value chart.', parts=[
    P('a', 'Write the number. {b}', A('4072')), P('b', 'The digit 7 is worth {b}.', A('70'))],
    why='Read the places from the left: 4 thousands, 0 hundreds, 7 tens and 2 ones make 4072. The 7 is in the tens place, so it is worth 70.',
    figure={'type': 'l3_grid', 'rows': [['Th', 'H', 'T', 'O'], [4, 0, 7, 2]], 'head_row': True, 'cw': 96, 'ch': 60, 'width_mm': 76}, figright=True)
u.S(1, 'Write each number in digits.', parts=[
    P('a', '6 thousands, 5 hundreds and 9 ones  {b}', A('6509')),
    P('b', '2 thousands and 15 tens  {b}', A('2150')),
    P('c', '5 thousands, 12 hundreds and 3 ones  {b}', A('6203'))],
    why='(a) 6000 + 500 + 9 = 6509. (b) 15 tens is 150, so 2000 + 150 = 2150. (c) 12 hundreds is 1200, so 5000 + 1200 + 3 = 6203.')
u.S(1, 'Fill in the blanks.', parts=[
    P('a', '1000 more than 6457 is {b}.', A('7457')), P('b', '100 less than 3050 is {b}.', A('2950')),
    P('c', '10 more than 8995 is {b}.', A('9005')), P('d', '1 less than 7000 is {b}.', A('6999'))],
    why='(a) Only the thousands digit changes: 7457. (b) 3050 - 100 = 2950. (c) 8995 + 10 = 9005, and the 9 hundreds carry. (d) 7000 - 1 = 6999.')
u.S(1, 'Arrange the numbers in order. Begin with the smallest.\n5830, 5083, 5380, 5038',
    A(['5038', '5083', '5380', '5830'], '5038, 5083, 5380, 5830', list=True),
    space={'rows': ['My order:']},
    why='All four start with 5 thousands. Compare the hundreds next: 0, 0, 3, 8. Then compare the tens of 5038 and 5083: 3 is less than 8.')
u.S(1, 'A shop has 3 boxes of 1000 pins, 14 packs of 100 pins and 6 loose pins. How many pins are there in all? {b}',
    A('4406'), why='3 boxes are 3000 pins. 14 packs are 1400 pins. 3000 + 1400 + 6 = 4406.')

# ---------------- page 2
u.S(2, 'Use the cards once each in every number.', parts=[
    P('a', 'The greatest number {b}', A('8752')), P('b', 'The smallest number {b}', A('2578')),
    P('c', 'The greatest odd number {b}', A('8725')), P('d', 'The smallest odd number {b}', A('2587'))],
    why='(a) Greatest digits first: 8752. (b) Smallest digits first, no 0 here: 2578. (c) The ones digit must be 7 or 5. With 5 last, 8725 beats 8527. (d) With 7 last, 2587 beats 2785.',
    figure=cards(2, 7, 5, 8))
u.S(2, 'List every 4-digit number that can be made with the cards 3, 0, 0 and 5. Begin with the smallest.',
    A(['3005', '3050', '3500', '5003', '5030', '5300'], '3005, 3050, 3500, 5003, 5030, 5300', list=True),
    why='The first digit is 3 or 5, never 0. After 3, the 5 can go in the hundreds, tens or ones place: 3005, 3050, 3500. After 5, the same way: 5003, 5030, 5300. That is 6 numbers.',
    figure=cards(3, 0, 0, 5), space={'rows': ['My list:']})
u.S(2, 'Write the next 2 numbers in each pattern.', parts=[
    P('a', '2300, 2600, 2900, {b}, {b}', A(['3200', '3500'], '3200, 3500 (add 300)', list=True)),
    P('b', '9000, 8750, 8500, {b}, {b}', A(['8250', '8000'], '8250, 8000 (subtract 250)', list=True)),
    P('c', '6, 14, 22, 30, {b}, {b}', A(['38', '46'], '38, 46 (add 8)', list=True))],
    why='(a) Add 300 each time. (b) Subtract 250 each time. (c) Add 8 each time: 30 + 8 = 38 and 38 + 8 = 46.')
u.S(2, 'A pattern starts at 3000 and goes down by 250 each time.', parts=[
    P('a', 'Is 1900 in the pattern?   {circ:Yes|No}', A('No')),
    P('b', 'The first number below 1900 in the pattern is {b}.', A('1750'))],
    why='The pattern goes 3000, 2750, 2500, 2250, 2000, 1750. It jumps over 1900 and lands on 1750.')
u.S(3, 'Look at the number line.', parts=[
    P('a', 'Arrow A points to {b}.', A('6150')), P('b', 'Arrow B points to {b}.', A('6450')), P('c', 'Arrow C points to {b}.', A('6350'))],
    why='Each small mark is 50. A is halfway from 6100 to 6200: 6150. B is halfway from 6400 to 6500: 6450. C is halfway from 6300 to 6400: 6350.',
    figure={'type': 'l3_nline', 'lo': 6000, 'hi': 6500, 'step': 50, 'lab': 100, 'W': 760, 'width_mm': 152,
            'marks': [{'at': 6150, 'text': 'A'}, {'at': 6450, 'text': 'B'}, {'at': 6350, 'text': 'C'}]})

# ---------------- page 3
u.S(3, 'I am a 4-digit number. My thousands digit is 6, my tens digit is 0, and my hundreds digit is 3 less than 6. My ones digit is the greatest odd digit. What number am I? {b}',
    A('6309'), why='The thousands digit is 6. The hundreds digit is 6 - 3 = 3. The tens digit is 0. The greatest odd digit is 9. The number is 6309.')
u.S(3, 'Ravi says the greatest odd number from the cards 9, 4, 6 and 2 is 9642.', parts=[
    P('a', 'Is he right?   {circ:Yes|No}', A('No')),
    P('b', 'The greatest odd number from the cards is {b}.', A('6429'))],
    why='9642 ends in 2, so it is even. The only odd card is 9, so 9 must be in the ones place. The other cards in order are 6, 4, 2. The number is 6429.',
    figure=cards(9, 4, 6, 2))
u.S(3, 'Look at the number 5737.', parts=[
    P('a', 'The first 7 is worth {b}.', A('700')), P('b', 'The second 7 is worth {b}.', A('7')),
    P('c', 'The first 7 is worth {b} more than the second 7.', A('693'))],
    why='The first 7 is in the hundreds place: 700. The second 7 is in the ones place: 7. 700 - 7 = 693.')

# ---------------- Think harder
u.T('The digits of a 4-digit number are all different and add up to 8. The number is even.', parts=[
    P('a', 'The greatest it can be is {b}.', A('5210')), P('b', 'The smallest it can be is {b}.', A('1034'))],
    hint='Find the sets of 4 different digits that add up to 8 first.',
    why='Only two sets of 4 different digits add up to 8: 0, 1, 2, 5 and 0, 1, 3, 4. Even numbers need an even last digit. The greatest even number is 5210. The smallest is 1034.',
    space={'rows': ['Sets of digits:', 'Numbers I tried:', '']})
u.T('Count the 3-digit numbers whose digits multiply to make 8. No digit is 0. {b}', A('10'),
    hint='List the sets of 3 digits first. Then arrange each set.',
    why='The sets of 3 digits are 1, 1, 8 and 1, 2, 4 and 2, 2, 2. The set 1, 1, 8 makes 118, 181, 811: 3 numbers. The set 1, 2, 4 makes 124, 142, 214, 241, 412, 421: 6 numbers. The set 2, 2, 2 makes 222: 1 number. 3 + 6 + 1 = 10.',
    space={'rows': ['Sets of digits:', 'Numbers:', '']})
u.T('Mei makes 4-digit numbers with the cards 1, 2, 3 and 4. She uses each card once.', parts=[
    P('a', '{b} of the numbers are greater than 2500.', A('12')), P('b', 'The 7th smallest number is {b}.', A('2134'))],
    hint='List them from the smallest. Fix the first digit.',
    why='Every number that starts with 1 or 2 is below 2500, because the second digit is at most 4. So only numbers that start with 3 or 4 are greater than 2500: 6 + 6 = 12. In order the list begins 1234, 1243, 1324, 1342, 1423, 1432, and the 7th is 2134.',
    space={'rows': ['My list:', '', '']})

# ---------------- Go further
u.G('Beyond Level 3: Counting digit sums.\nCount the 3-digit numbers with a digit sum of 4. List them by first digit.', parts=[
    P('a', 'Digit sum 4: {b} numbers.', A('10')),
    P('b', 'Use the pattern. Digit sum 5: {b} numbers.', A('15'))],
    hint='Fix the first digit. See how the counts grow: 1, 2, 3, ...',
    why='Sum 4: first digit 4 gives 1 number (400), 3 gives 2 (310, 301), 2 gives 3, 1 gives 4. That is 1 + 2 + 3 + 4 = 10. Sum 5 goes up to 5 numbers for first digit 1: 1 + 2 + 3 + 4 + 5 = 15.',
    space={'rows': ['First digit 4:', 'First digit 3:']})
u.G('Beyond Level 3: Growing jumps.\nLook at the jumps between the numbers. Write the next 2 numbers.\n5, 8, 14, 23, 35, {b}, {b}',
    A(['50', '68'], '50, 68', list=True),
    hint='Write the jumps between the numbers. What do you see?',
    why='The jumps are 3, 6, 9, 12. Each jump is 3 more than the one before. The next jumps are 15 and 18: 35 + 15 = 50 and 50 + 18 = 68.',
    space={'rows': ['Jumps:']})
u.G('Make up your own number riddle. Choose a secret number with 4 digits, then write 3 clues. Test your clues: exactly ONE number must fit. Swap riddles with a grown-up.',
    A('7423', 'Answers vary. Example: I am between 7000 and 8000. My hundreds digit is double my tens digit. My ones digit is 1 more than my tens digit. My digits add up to 16. The only number is 7423.'),
    hint='Pick the number first. Then write clues about its digits.',
    why='Check that every clue is true for your secret number. Then list the numbers that fit clue 1, and cross out those that fail clue 2, and so on. In the example, the tens digit t gives 7 + 2t + t + (t + 1) = 16, so t = 2 and the number is 7423.',
    space={'rows': ['Clue 1:', 'Clue 2:', 'Clue 3:']})
u.G('Find the secret number. It is greater than 3000 and less than 4000. Its digits are all different and add up to 15. The tens digit is 0, and the hundreds digit is double the ones digit. {b}',
    A('3804'), hint='Try ones digit 1, 2, 3 and 4. Check each sum.',
    why='The thousands digit is 3 and the tens digit is 0. If the ones digit is o, the hundreds digit is 2o, so 3 + 2o + 0 + o = 15 and o = 4. The hundreds digit is 8. The number is 3804.')

# ---------------- Check yourself
u.C('In 7258, the digit 2 is worth {b}.', A('200'), why='The 2 is in the hundreds place, so it is worth 200.')
u.C('Write the next 2 numbers. 6500, 6000, 5500, {b}, {b}', A(['5000', '4500'], '5000, 4500', list=True), why='Subtract 500 each time: 5500 - 500 = 5000 and 5000 - 500 = 4500.')
u.C('Make the smallest 4-digit number from the cards 6, 1, 0 and 5. Use each card once. {b}', A('1056'),
    why='The first digit cannot be 0, so use 1. Then the rest in order: 0, 5, 6. The number is 1056.', figure=cards(6, 1, 0, 5), figright=True)
u.C('Ali has 5 boxes of 1000 beads, 12 bags of 100 beads and 8 loose beads. How many beads does he have? {b}', A('6208'),
    why='5 boxes are 5000. 12 bags are 1200. 5000 + 1200 + 8 = 6208.')
u.save()
