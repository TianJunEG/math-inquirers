from lib import *

u = Unit(3, 'Times table tricks', 'Tables of 6, 7, 8 and 9',
         'I can use facts I know to find new times table facts. I can find patterns and solve number puzzles.')


def mult_row(n, blanks):
    """grid figure: the n times table from 1 to 10 with some answers left empty"""
    return {'type': 'l3_grid', 'head_col': True, 'cw': 60, 'ch': 56, 'fs': 28, 'width_mm': 134, 'rows': [
        ['n'] + list(range(1, 11)),
        [f'{n} × n'] + [None if k in blanks else n * k for k in range(1, 11)]], 'col_w': [96] + [58] * 10}


u.learn(
    'A times table fact you do not know can be built from facts you do know. Split a rectangle of dots into two smaller rectangles.',
    {'problem': 'There are 7 rows with 6 dots in each row. How many dots are there in all?',
     'figure': {'type': 'l3_array', 'rows': 7, 'cols': 6, 's': 44, 'split_row': 5, 'width_mm': 56}, 'side': True,
     'steps': ['The dashed line splits the dots into 5 rows and 2 rows.',
               '5 × 6 = 30 and 2 × 6 = 12.',
               'Add the 2 parts: 30 + 12 = 42.',
               'So 7 × 6 = 42.'],
     'answer': '7 × 6 = 42. There are 42 dots.'},
    {'title': 'Ways to find a fact',
     'steps': ['Split into facts you know: 5 ×, 2 ×, 10 ×.', 'For 9 ×: take 1 group away from 10 groups.',
               'Check with the last digit.']},
    {'text': 'There are 6 rows with 8 dots in each row. Split them into 3 rows and 3 rows. How many dots are there in all? {b}',
     'figure': {'type': 'l3_array', 'rows': 6, 'cols': 8, 's': 44, 'split_row': 3, 'width_mm': 72}, 'figright': True, 'answer': A('48'),
     'explanation': '3 × 8 = 24 and 3 × 8 = 24. Then 24 + 24 = 48. So 6 × 8 = 48.'})

u.u['learn']['tight'] = True

# ---------------- Start here (pages 1 to 3)
u.S(1, 'Write the missing answers in the 8 times table.', A(['32', '48', '72'], '32, 48, 72', list=True),
    figure=mult_row(8, {4, 6, 9}),
    why='The answers go up by 8 each time. 8 × 4 = 32, 8 × 6 = 48 and 8 × 9 = 72.')
u.S(1, 'Write the answers.', parts=[
    P('a', '6 × 8 = {b}', A('48')), P('b', '7 × 9 = {b}', A('63')), P('c', '9 × 6 = {b}', A('54')), P('d', '8 × 7 = {b}', A('56'))],
    partsrow=True,
    why='6 × 8 = 48, 7 × 9 = 63, 9 × 6 = 54 and 8 × 7 = 56. Swap the numbers to check: 8 × 6 = 48.')
u.S(1, 'You know that 8 × 5 = 40. Use it to find the other facts.', parts=[
    P('a', '8 × 6 = {b}', A('48')), P('b', '8 × 4 = {b}', A('32')), P('c', '8 × 10 = {b}', A('80')), P('d', '8 × 9 = {b}', A('72'))],
    why='(a) One more 8: 40 + 8 = 48. (b) One less 8: 40 - 8 = 32. (c) Double 8 × 5: 80. (d) 8 × 10 = 80, take away one 8: 72.')
u.S(1, 'Ali packs 7 eggs in each box. He fills 9 boxes.', parts=[
    P('a', 'He packs {b} eggs.', A('63')), P('b', 'Then he packs 56 eggs into boxes of 7. He fills {b} boxes.', A('8'))],
    why='(a) 9 × 7 = 63. (b) 56 ÷ 7 = 8, because 7 × 8 = 56.')
u.S(1, 'Find my number. It is in the 7 times table, and it is greater than 50 and less than 80. Its digits add up to 9. {b}', A('63'),
    why='The numbers in the 7 times table between 50 and 80 are 56, 63, 70 and 77. Their digits add up to 11, 9, 7 and 14. Only 63 has digits that add up to 9.')
u.S(2, 'The dashed line splits 7 rows of 9 dots into 2 parts.', parts=[
    P('a', 'The top part has 5 × 9 = {b} dots.', A('45')), P('b', 'The bottom part has 2 × 9 = {b} dots.', A('18')),
    P('c', 'There are {b} dots in all.', A('63'))],
    figure={'type': 'l3_array', 'rows': 7, 'cols': 9, 's': 36, 'split_row': 5, 'width_mm': 80}, figside=True,
    why='5 × 9 = 45 and 2 × 9 = 18. Add: 45 + 18 = 63. So 7 × 9 = 63.')
u.S(2, 'Fill in the missing answers.', parts=[P('', 'A = {b}   B = {b}   C = {b}   D = {b}', A(['48', '42', '63', '56'], 'A = 48, B = 42, C = 63, D = 56', list=True))],
    figure={'type': 'l3_grid', 'head_row': True, 'head_col': True, 'cw': 70, 'ch': 56, 'width_mm': 84, 'rows': [
        ['×', 6, 7, 8, 9], [6, 36, 42, {'t': 'A', 'fill': 'none', 'dash': True}, 54], [7, {'t': 'B', 'fill': 'none', 'dash': True}, 49, 56, {'t': 'C', 'fill': 'none', 'dash': True}],
        [8, 48, {'t': 'D', 'fill': 'none', 'dash': True}, 64, 72]]},
    why='Each cell is the row number × the column number. A = 6 × 8 = 48. B = 7 × 6 = 42. C = 7 × 9 = 63. D = 8 × 7 = 56.')
u.S(2, 'A row number times a column number makes each product. Write the missing numbers in the heading cells.', A(['6', '7', '9', '8'], 'Columns 6 and 7. Rows 9 and 8.', list=True),
    figure={'type': 'l3_grid', 'head_row': True, 'head_col': True, 'cw': 70, 'ch': 52, 'width_mm': 54, 'rows': [
        ['×', None, None], [None, 54, 63], [None, 48, 56]]},
    why='54 and 63 are in the same row. Both are in the 9 times table: 54 = 9 × 6 and 63 = 9 × 7. So the row number is 9 and the columns are 6 and 7. The second row: 48 = 8 × 6 and 56 = 8 × 7, so the row number is 8.')
u.S(3, 'Write the last digit of each answer. Do not find the whole answer.', parts=[
    P('a', '6 × 13   {b}', A('8')), P('b', '8 × 27   {b}', A('6')), P('c', '9 × 45   {b}', A('5')), P('d', '7 × 68   {b}', A('6'))],
    why='Only the last digits matter. (a) 6 × 3 = 18 ends in 8. (b) 8 × 7 = 56 ends in 6. (c) 9 × 5 = 45 ends in 5. (d) 7 × 8 = 56 ends in 6.')
u.S(3, 'Mei puts 30 tiles in equal rows. There are at least 2 rows and at least 2 tiles in each row. List ALL the ways.', parts=[
    P('', 'There are {b} ways.', A('6'))],
    space={'table': {'cols': ['rows', 'tiles in each row'], 'rows': 6}},
    why='Check the number of rows from 2 upwards: 2 rows of 15, 3 rows of 10, 5 rows of 6, 6 rows of 5, 10 rows of 3 and 15 rows of 2. 4 rows does not work because 30 is not in the 4 times table. That is 6 ways.')
u.S(3, 'Which of these numbers are in the 6 times table?\n24, 38, 42, 56, 60\n{ll}', A(['24', '42', '60'], '24, 42, 60', list=True),
    why='6 × 4 = 24, 6 × 7 = 42 and 6 × 10 = 60. The numbers 38 and 56 are not: 6 × 6 = 36 and 6 × 9 = 54, and the next answer after 54 is 60.')
u.S(3, 'Mei buys 6 packs of 8 stickers. Ben buys 7 packs of 7 stickers.', parts=[
    P('a', 'Who has more stickers?   {circ:Mei|Ben}', A('Ben')), P('b', 'How many more? {b}', A('1'))],
    why='Mei has 6 × 8 = 48 stickers. Ben has 7 × 7 = 49 stickers. Ben has 49 - 48 = 1 more.')

# ---------------- Think harder
u.T('Ben writes the 7 times table from 7 × 1 to 7 × 30. How many of his answers end in 4? {b}', A('3'),
    hint='Which number times 7 ends in 4? Then find the next ones.',
    why='7 × 2 = 14 ends in 4. The last digits of the 7 times table repeat every 10 numbers, so the next ones are 7 × 12 = 84 and 7 × 22 = 154. 7 × 32 is beyond 7 × 30. That makes 3 answers.',
    space={'rows': ['The 7 times table:', '', 'The answers ending in 4:', '']})
u.T('The row numbers and column numbers are all from 6 to 9. Find the empty cells A to D. You can write in the heading cells to help you.', parts=[
    P('a', 'A = {b}', A('54')), P('b', 'B = {b}', A('56')), P('c', 'C = {b}', A('56')), P('d', 'D = {b}', A('64'))],
    partsrow=True,
    figure={'type': 'l3_grid', 'head_row': True, 'head_col': True, 'cw': 78, 'ch': 56, 'width_mm': 64, 'rows': [
        ['×', None, None, None], [None, 42, 48, {'t': 'A', 'fill': 'none', 'dash': True}], [None, 49, {'t': 'B', 'fill': 'none', 'dash': True}, 63],
        [None, {'t': 'C', 'fill': 'none', 'dash': True}, {'t': 'D', 'fill': 'none', 'dash': True}, 72]]}, figside=True,
    hint='Start with 49. Which row and column make 49?',
    why='49 = 7 × 7, so row 2 and column 1 are both 7. Then 42 = 6 × 7 gives row 1 = 6, and 48 = 6 × 8 gives column 2 = 8. 63 = 7 × 9 gives column 3 = 9. 72 = 8 × 9 gives row 3 = 8. A = 6 × 9 = 54, B = 7 × 8 = 56, C = 8 × 7 = 56 and D = 8 × 8 = 64.')
u.T('Two numbers have a product of 63 and a sum of 16. What are the 2 numbers? {b} and {b}', A(['7', '9'], '7 and 9', list=True),
    hint='List the pairs of numbers that multiply to make 63.',
    why='The pairs that multiply to 63 are 1 and 63, 3 and 21, 7 and 9. Their sums are 64, 24 and 16. Only 7 and 9 add up to 16.',
    space={'rows': ['Pairs that multiply to 63:', '', '']})

# ---------------- Go further
u.G('Beyond Level 3: Digit sums and the 9s.\nAdd the digits again and again: 684 gives 6 + 8 + 4 = 18, then 1 + 8 = 9. Numbers in the 9 times table always end at 9. Which of these are in it?\n738, 825, 963, 1089\n{ll}',
    A(['738', '963', '1089'], '738, 963, 1089', list=True),
    hint='Add the digits of each number. Keep adding until 1 digit is left.',
    why='738: 7 + 3 + 8 = 18, then 1 + 8 = 9. 825: 8 + 2 + 5 = 15, then 1 + 5 = 6, so not. 963: 9 + 6 + 3 = 18, then 9. 1089: 1 + 0 + 8 + 9 = 18, then 9. Check: 738 = 9 × 82, 963 = 9 × 107, 1089 = 9 × 121.')
u.G('Beyond Level 3: Adding every row.\nA hall has 8 rows. Row 1 has 7 seats. Each row has 2 more seats than the row before.', parts=[
    P('a', 'Row 8 has {b} seats.', A('21')), P('b', 'The hall has {b} seats in all.', A('112'))],
    figure={'type': 'l3_grid', 'head_col': True, 'cw': 56, 'ch': 52, 'fs': 26, 'width_mm': 118, 'col_w': [94] + [56] * 8, 'rows': [
        ['Row', 1, 2, 3, 4, 5, 6, 7, 8], ['Seats', 7, 9] + [None] * 6]},
    hint='Pair the first and last rows. Then the next pair.',
    why='The seats go 7, 9, 11, 13, 15, 17, 19, 21. Row 8 has 21 seats. Pair them: 7 + 21 = 28, 9 + 19 = 28, 11 + 17 = 28, 13 + 15 = 28. There are 4 pairs, so 4 × 28 = 112 seats.')
u.G('Make your own 2 by 2 grid puzzle with numbers from 6 to 9. Show 3 products. Only ONE answer may fit. Swap it with a grown-up.',
    A('56', 'Answers vary. Example: the products 42, 48 and 49 are shown. The row numbers are 6 and 7 and the column numbers are 7 and 8, so the hidden product is 56.'),
    hint='Pick the row and column numbers first. Then multiply.',
    why='Check that each shown product belongs to the numbers you chose. Check that no other row and column numbers from 6 to 9 give the same 3 products. In the example, 42 = 6 × 7 and 48 = 6 × 8 give row 6 and columns 7 and 8. Also 49 = 7 × 7 gives row 7. The hidden product is 7 × 8 = 56.',
    space={'rows': ['{ll}']})
u.G('Ben multiplies a number by 8.', parts=[
    P('a', 'His answer ends in 6. The last digit of his number could be {b} or {b}.', A(['2', '7'], '2 or 7', list=True)),
    P('b', 'His answer ends in 5. The last digit of his number could be {circ:0|2|5|7|none}.', A('none'))],
    hint='List the last digits of 8 × 1 up to 8 × 10.',
    why='The last digits of the 8 times table are 8, 6, 4, 2, 0, 8, 6, 4, 2, 0. A last digit of 6 comes from 8 × 2 and 8 × 7. A last digit of 5 never comes: every answer in the 8 times table is even.')

# ---------------- Check yourself
u.C('A box holds 8 pens. How many pens are in 7 boxes? {b}', A('56'), why='7 × 8 = 56. Check: 8 × 7 = 56.')
u.C('You know that 5 × 7 = 35. Use it to find 6 × 7. {b}', A('42'), why='6 × 7 is one more 7 than 5 × 7: 35 + 7 = 42.')
u.C('What is the last digit of 7 × 56? {b}', A('2'), why='Only 7 × 6 matters for the last digit. 7 × 6 = 42 ends in 2. (7 × 56 = 392.)')
u.C('Mei has 54 apples. She puts 6 apples in each bag. How many bags does she need? {b}', A('9'), why='54 ÷ 6 = 9, because 6 × 9 = 54.')
u.save()
