from lib import *

u = Unit(6, 'Build a wall', 'Fractions',
         'I can use a fraction wall to find equal fractions. I can compare fractions and add and subtract them.')
CMP = '{circ:<|=|>}'


def bars(items, cols=2, w=120, **kw):
    d = {'type': 'l3_fshapes', 'items': items, 'cols': cols, 'width_mm': w}
    d.update(kw)
    return d


u.learn(
    'A fraction wall shows one whole cut into equal parts. A longer piece of the wall is a greater fraction. To compare fractions, look at where the pieces end.',
    {'problem': 'Which is greater, 5/8 or 3/4? Use the fraction wall.',
     'figure': {'type': 'l3_wall', 'dens': [4, 8], 'shade': {'4': [0, 1, 2], '8': [0, 1, 2, 3, 4]}, 'width_mm': 100},
     'steps': ['Shade 5/8 on the row of eighths.', 'Shade 3/4 on the row of quarters.',
               'The end of 3/4 lines up with the end of 6/8.', '6/8 is more than 5/8, so 3/4 is greater.'],
     'answer': '3/4 is greater than 5/8.'},
    {'title': 'How to compare and add fractions',
     'steps': ['Equal fractions: multiply top and bottom by the same number. 1/3 = 2/6 = 4/12.', 'To add or subtract, change both to the same bottom number.',
               'Add or subtract the top numbers. Keep the bottom number.']},
    {'text': 'Circle <, = or >.   7/12 ' + CMP + ' 2/3', 'answer': A('<'),
     'explanation': '2/3 = 8/12 on the wall. 7/12 is less than 8/12, so 7/12 < 2/3.'})
u.u['learn']['example2'] = {'problem': 'What is 1/2 + 1/4? Use the fraction wall.',
    'figure': {'type': 'l3_wall', 'dens': [2, 4], 'shade': {'2': [0], '4': [0, 1, 2]}, 'width_mm': 100},
    'steps': ['On the wall, 1/2 is the same length as 2/4.', 'Add the quarters: 2/4 + 1/4 = 3/4.'], 'answer': '1/2 + 1/4 = 3/4.'}
u.u['learn']['tight'] = True

# ---------------- Start here (pages 1 to 3)
u.S(1, 'Use the fraction wall to fill in the blanks.', parts=[
    P('a', '1/3 = {b}/6 = {b}/12', A(['2', '4'], '1/3 = 2/6 = 4/12', list=True)),
    P('b', '2/3 = {b}/6 = {b}/12', A(['4', '8'], '2/3 = 4/6 = 8/12', list=True)),
    P('c', '5/6 = {b}/12', A('10', '5/6 = 10/12'))],
    figure={'type': 'l3_wall', 'dens': [3, 6, 12], 'width_mm': 124},
    why='Line up the rows. 1 third is the same length as 2 sixths and 4 twelfths. 2 thirds is 4 sixths and 8 twelfths. 5 sixths is 10 twelfths.')
u.S(1, 'Write the fraction of each shape that is shaded.', parts=[
    P('a', 'A = {b}/{b}', A(['3', '8'], '3/8', list=True)), P('b', 'B = {b}/{b}', A(['4', '6'], '4/6', list=True)),
    P('c', 'C = {b}/{b}', A(['7', '10'], '7/10', list=True)), P('d', 'D = {b}/{b}', A(['2', '5'], '2/5', list=True))],
    figure=bars([{'kind': 'bar', 'n': 8, 'shade': [0, 1, 2], 'label': 'A'}, {'kind': 'bar', 'n': 6, 'shade': [0, 1, 2, 3], 'label': 'B'},
                 {'kind': 'bar', 'n': 10, 'shade': [0, 1, 2, 3, 4, 5, 6], 'label': 'C'}, {'kind': 'bar', 'n': 5, 'shade': [0, 1], 'label': 'D'}], cols=2, w=120, ch=92),
    partsrow=True,
    why='The bottom number is the number of equal parts in the whole shape. The top number is the number of shaded parts. A: 3 of 8. B: 4 of 6. C: 7 of 10. D: 2 of 5.')
u.S(1, 'Which shapes are cut into EQUAL parts? Circle the letters.   {circ:A|B|C|D}', A(['A', 'C'], 'A and C', list=True),
    figure=bars([{'kind': 'bar', 'n': 4, 'label': 'A'}, {'kind': 'bar', 'n': 4, 'cuts': [0.15, 0.55, 0.8], 'label': 'B'},
                 {'kind': 'circle', 'n': 6, 'label': 'C'}, {'kind': 'circle', 'n': 4, 'angles': [150, 60, 90, 60], 'label': 'D'}], cols=2, w=120, ch=126),
    why='A fraction needs equal parts. A has 4 equal parts and C has 6 equal sectors. B and D have parts of different sizes.')
u.S(2, 'Circle <, = or > in each part.', parts=[
    P('a', '5/8 ' + CMP + ' 3/8', A('>')), P('b', '1/3 ' + CMP + ' 1/4', A('>')),
    P('c', '2/4 ' + CMP + ' 4/8', A('=')), P('d', '3/4 ' + CMP + ' 5/6', A('<'))],
    why='(a) Same bottom number: 5 parts are more than 3 parts. (b) Thirds are larger pieces than quarters. (c) 2/4 = 4/8. (d) 3/4 = 9/12 and 5/6 = 10/12, and 9 is less than 10.')
u.S(2, 'Arrange the fractions in order. Begin with the smallest.\n5/6, 1/3, 1/2, 2/3\n{ll}', A(['1/3', '1/2', '2/3', '5/6'], '1/3, 1/2, 2/3, 5/6', list=True),
    why='Write each one in sixths: 5/6, 2/6, 3/6, 4/6. The order of the tops is 2, 3, 4, 5. So the order is 1/3, 1/2, 2/3, 5/6.')
u.S(2, 'Fill in the blanks.', parts=[
    P('a', '3/10 + 4/10 = {b}/10', A('7')), P('b', '5/8 - 2/8 = {b}/8', A('3')),
    P('c', '9/12 - 4/12 = {b}/12', A('5')), P('d', '1 - 3/10 = {b}/10', A('7'))],
    why='When the bottom numbers are the same, add or subtract the top numbers and keep the bottom number. (d) 1 whole is 10/10, and 10/10 - 3/10 = 7/10.')
u.S(2, 'Change to the same bottom number. Then fill in the blanks.', parts=[
    P('a', '1/2 + 1/4 = {b}/4', A('3')), P('b', '1/3 + 1/6 = {b}/6', A('3')),
    P('c', '3/4 - 1/8 = {b}/8', A('5')), P('d', '5/6 - 1/2 = {b}/6', A('2'))],
    why='(a) 1/2 = 2/4, so 2/4 + 1/4 = 3/4. (b) 1/3 = 2/6, so 2/6 + 1/6 = 3/6. (c) 3/4 = 6/8, so 6/8 - 1/8 = 5/8. (d) 1/2 = 3/6, so 5/6 - 3/6 = 2/6.')
u.S(3, 'A cake is cut into 12 equal slices. Ali eats 3 slices. Ben eats 4 slices.', parts=[
    P('a', 'Ali and Ben eat {b}/12 of the cake.', A('7')), P('b', '{b}/12 of the cake is left.', A('5')),
    P('c', 'Ben eats {b}/12 more of the cake than Ali.', A('1'))],
    why='(a) 3/12 + 4/12 = 7/12. (b) The whole cake is 12/12, so 12/12 - 7/12 = 5/12. (c) 4/12 - 3/12 = 1/12.')
u.S(3, 'Look at the number line from 0 to 1. It is cut into equal steps.', parts=[
    P('a', 'A = {b}/8', A('3')), P('b', 'B = {b}/8', A('5')), P('c', 'C = {b}/8', A('7')),
    P('d', 'Which arrow shows 1/2?   {circ:A|B|C|D}', A('D'))],
    figure={'type': 'l3_fline', 'den': 8, 'W': 720, 'marks': [{'at': 3, 'text': 'A'}, {'at': 5, 'text': 'B'}, {'at': 7, 'text': 'C'}, {'at': 4, 'text': 'D'}], 'width_mm': 120},
    why='There are 8 equal steps, so each step is 1/8. A is 3 steps from 0: 3/8. B is 5 steps: 5/8. C is 7 steps: 7/8. D is 4 steps: 4/8, which is half of the line.')
u.S(3, 'Fill in the blanks to make equal fractions.', parts=[
    P('a', '3/4 = {b}/12', A('9')), P('b', '2/5 = {b}/10', A('4')),
    P('c', '1/2 = 5/{b}', A('10')), P('d', '6/8 = 3/{b}', A('4'))],
    partsrow=True,
    why='Multiply or divide the top and the bottom by the same number. (a) 4 × 3 = 12, so 3 × 3 = 9. (b) 5 × 2 = 10, so 2 × 2 = 4. (c) 1 × 5 = 5, so 2 × 5 = 10. (d) 6 ÷ 2 = 3, so 8 ÷ 2 = 4.')
u.S(3, 'Siti says 3/8 + 2/8 = 5/16.', parts=[
    P('a', 'Is she right?   {circ:Yes|No}', A('No')), P('b', 'The right answer is {b}/8.', A('5'))],
    why='When the parts are the same size, only the top numbers are added. The bottom number stays 8. 3/8 + 2/8 = 5/8.')

# ---------------- Think harder
u.T('Look at the fractions with bottom number 12. List every one between 1/3 and 2/3.\n{ll}', A(['5/12', '6/12', '7/12'], '5/12, 6/12 and 7/12', list=True),
    hint='Change 1/3 and 2/3 into twelfths first.',
    why='1/3 = 4/12 and 2/3 = 8/12. The twelfths between 4/12 and 8/12 are 5/12, 6/12 and 7/12. The fractions 4/12 and 8/12 are not between.',
    space={'rows': ['Working:', '', '', '']})
u.T('Ben writes fractions that are equal to 3/4. He adds the top number and the bottom number.', parts=[
    P('a', 'The sum is 28 for the fraction {b}/{b}.', A(['12', '16'], '12/16', list=True)),
    P('b', 'The sum is 42 for the fraction {b}/{b}.', A(['18', '24'], '18/24', list=True))],
    hint='Write equal fractions of 3/4. Add the top and bottom each time.',
    why='Equal fractions of 3/4 are 3/4, 6/8, 9/12, 12/16, 15/20, 18/24. Their sums are 7, 14, 21, 28, 35, 42. So 12/16 has sum 28 and 18/24 has sum 42.',
    space={'rows': ['My list:', '', '']})
u.T('A jug is full of juice. Mei drinks 1/4 of the jug. Ali drinks 1/3 of the jug.', parts=[
    P('a', 'Together they drink {b}/12 of the jug.', A('7')), P('b', '{b}/12 of the jug is left.', A('5'))],
    hint='Change quarters and thirds into twelfths first.',
    why='1/4 = 3/12 and 1/3 = 4/12. (a) 3/12 + 4/12 = 7/12. (b) 12/12 - 7/12 = 5/12 of the jug is left.',
    space={'rows': ['Working:', '', '']})

# ---------------- Go further
u.G('Beyond Level 3: Adding fractions with top number 1.\nWrite each as 2 fractions with top number 1.', parts=[
    P('a', '3/4 = 1/2 + 1/{b}', A('4')), P('b', '5/6 = 1/2 + 1/{b}', A('3')), P('c', '7/12 = 1/3 + 1/{b}', A('4'))],
    hint='Take away the first fraction. What is left over?',
    why='(a) 3/4 - 1/2 = 3/4 - 2/4 = 1/4. (b) 5/6 - 1/2 = 5/6 - 3/6 = 2/6 = 1/3. (c) 7/12 - 1/3 = 7/12 - 4/12 = 3/12 = 1/4.',
    partsrow=True)
u.G('A whole bar is filled with exactly 6 pieces. The pieces are 1/2, 1/4 or 1/8 of the bar. How many of each?', parts=[
    P('a', '{b} halves, {b} quarters and {b} eighths.', A(['0', '2', '4'], '0 halves, 2 quarters, 4 eighths', list=True))],
    hint='Eighths are the smallest. Most of the 6 pieces must be small.',
    why='Write everything in eighths: a half is 4, a quarter is 2, an eighth is 1. The 6 pieces must make 8 eighths. With no halves: 2 quarters (4) and 4 eighths (4) make 8. Using 1 half is not possible with 6 pieces: the other 5 pieces would have to make 4 eighths, but each is at least 1.',
    space={'rows': ['My tries:']})
u.G('Colour the bar. Draw lines in 1/2 of the bar. Draw dots in 1/3 of the bar. Leave the rest white.', parts=[
    P('a', '{b} parts are white.', A('2')), P('b', 'That is the same as 1/{b} of the bar.', A('6'))],
    figure=bars([{'kind': 'bar', 'n': 12}], cols=1, w=124, ch=84, bw=420, cw=520),
    hint='1/2 of 12 parts is 6 parts. How many parts for 1/3?',
    why='1/2 of the bar is 6 parts and 1/3 of the bar is 4 parts. 6 + 4 = 10 parts are coloured, so 2 parts are white. 2/12 is the same as 1/6.')
u.G('Make up a fraction story about a pizza cut into 8 equal slices. The answer to your story must be 5/8.', A('5/8', 'Answers vary. Example: Ali eats 3/8 of a pizza and Mei eats 2/8 of it. Together they eat 5/8 of the pizza.'),
    hint='Pick 2 fractions with bottom number 8 that add up to 5/8.',
    why='Check that your fractions all have the same bottom number, and that the story gives 5/8. In the example, 3/8 + 2/8 = 5/8.',
    space={'rows': ['My story:', 'My answer:']})

# ---------------- Check yourself
u.C('Write the fraction that is shaded. {b}/8', A('5'), figure=bars([{'kind': 'bar', 'n': 8, 'shade': [0, 1, 2, 3, 4]}], cols=1, w=70, ch=100), figright=True,
    why='The bar has 8 equal parts and 5 are shaded. The fraction is 5/8.')
u.C('Circle <, = or >.   5/8 ' + CMP + ' 3/4', A('<'), why='3/4 = 6/8. 5/8 is less than 6/8, so 5/8 < 3/4.')
u.C('5/8 - 1/4 = {b}/8', A('3'), why='1/4 = 2/8, so 5/8 - 2/8 = 3/8.')
u.C('Fill in the blank. 2/3 = {b}/12', A('8'), why='3 × 4 = 12, so 2 × 4 = 8. 2/3 = 8/12.')
u.save()
