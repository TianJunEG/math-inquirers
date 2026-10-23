from lib import *

u = Unit(5, 'What is left over?', 'Division with remainders',
         'I can divide with a remainder. I can decide what the remainder means in a story. I can find a mystery number.')
DAYS = '{circ:Mon|Tue|Wed|Thu|Fri|Sat|Sun}'

u.learn(
    'When we share or make groups, some may be left over. The leftover is the remainder. It is always smaller than the number we divide by.',
    {'problem': 'Ali has 38 stickers. Each bag takes 5 stickers. How many bags can he fill? How many stickers are left over?',
     'figure': {'type': 'l3_groups', 'n': 38, 'k': 5, 'cols': 3, 'width_mm': 120},
     'steps': ['Find the greatest fact that is not more than 38. 5 × 7 = 35.',
               'Subtract to find what is left: 38 - 35 = 3.',
               'Write it as 38 ÷ 5 = 7 remainder 3.',
               'Check: 7 × 5 + 3 = 38.'],
     'answer': '7 full bags, with 3 stickers left over.'},
    {'title': 'How to divide with a remainder',
     'steps': ['Find the greatest table fact that fits in the number.',
               'Subtract it to find the remainder.', 'Check: groups × size + remainder = start.', 'A leftover person still needs a seat: use 1 more group.']},
    {'text': 'A baker packs 43 buns into boxes of 6. She fills {b} boxes and has {b} buns left over.',
     'answer': A(['7', '1'], '7 full boxes, 1 bun left over', list=True),
     'explanation': '6 × 7 = 42 and 43 - 42 = 1. So 43 ÷ 6 = 7 remainder 1. Check: 7 × 6 + 1 = 43.'})
u.u['learn']['tight'] = True

# ---------------- Start here (pages 1 to 3)
u.S(1, 'The dots are put into groups of 4.', parts=[
    P('a', 'There are {b} full groups.', A('4')), P('b', 'There are {b} dots left over.', A('3'))],
    figure={'type': 'l3_groups', 'n': 19, 'k': 4, 'cols': 3, 'width_mm': 122},
    partsrow=True,
    why='Count the solid boxes: 4 groups of 4 dots make 16 dots. The dashed box has the 3 dots left over. So 19 ÷ 4 = 4 remainder 3.')
u.S(1, 'Divide.', parts=[
    P('a', '38 ÷ 7 = {b} remainder {b}', A(['5', '3'], '5 remainder 3', list=True)),
    P('b', '50 ÷ 8 = {b} remainder {b}', A(['6', '2'], '6 remainder 2', list=True)),
    P('c', '61 ÷ 9 = {b} remainder {b}', A(['6', '7'], '6 remainder 7', list=True)),
    P('d', '75 ÷ 6 = {b} remainder {b}', A(['12', '3'], '12 remainder 3', list=True))],
    why='(a) 7 × 5 = 35 and 38 - 35 = 3. (b) 8 × 6 = 48 and 50 - 48 = 2. (c) 9 × 6 = 54 and 61 - 54 = 7. (d) 6 × 12 = 72 and 75 - 72 = 3.')
u.S(1, 'Divide. Then decide what the leftover means.', parts=[
    P('a', '26 people go in cars of 5. They need {b} cars.', A('6')),
    P('b', '37 cm of ribbon, cut in 6 cm pieces, gives {b} whole pieces.', A('6')),
    P('c', 'Ravi has $30. A toy costs $4. He buys {b} toys.', A('7')),
    P('d', 'Then he has $ {b} left.', A('2'))],
    why='(a) 26 ÷ 5 = 5 remainder 1. The 1 person left over still needs a car, so 6 cars. (b) 37 ÷ 6 = 6 remainder 1: 6 whole pieces. (c) 30 ÷ 4 = 7 remainder 2: 7 toys. (d) The remainder is the money left: $2.')
u.S(1, 'Kumar says 59 ÷ 7 = 7 remainder 10.', parts=[
    P('a', 'The remainder 10 is greater than {b}.', A('7')),
    P('b', 'The right answer is {b} remainder {b}.', A(['8', '3'], '8 remainder 3', list=True))],
    why='A remainder must be smaller than the number we divide by. 10 is greater than 7, so another group of 7 fits. 7 × 8 = 56 and 59 - 56 = 3. So 59 ÷ 7 = 8 remainder 3.')

u.S(2, 'Ali stacks coins in piles of 5. He makes 9 full piles and has 4 coins left over.', parts=[
    P('a', 'Ali has {b} coins.', A('49')),
    P('b', 'He stacks all the coins again in piles of 6. He makes {b} piles and has {b} coins left.', A(['8', '1'], '8 piles, 1 coin left', list=True))],
    why='(a) 9 × 5 = 45, and 45 + 4 = 49. (b) 49 ÷ 6: 6 × 8 = 48 and 49 - 48 = 1. So 8 full piles and 1 coin left.')
u.S(2, 'Think about remainders.', parts=[
    P('a', 'List every remainder that is possible when a number is divided by 5.\n{ll}', A(['0', '1', '2', '3', '4'], '0, 1, 2, 3, 4', list=True)),
    P('b', 'A number between 50 and 60 is divided by 7. The remainder is as great as it can be. The number is {b}.', A('55'))],
    why='(a) A remainder is always smaller than 5, so it can be 0, 1, 2, 3 or 4. (b) The greatest remainder for 7 is 6. The numbers with remainder 6 are 6, 13, 20, ... 48, 55, 62. Only 55 is between 50 and 60.')
u.S(2, 'Look for a pattern. Write the remainder when each number is divided by 4.', parts=[
    P('a', 'Fill in the empty cells.', A(['0', '1', '2', '3', '0', '1', '2', '3'], '0, 1, 2, 3, 0, 1, 2, 3', list=True)),
    P('b', 'When 30 is divided by 4 the remainder is {b}.', A('2')),
    P('c', 'When 100 is divided by 4 the remainder is {b}.', A('0'))],
    figure={'type': 'l3_grid', 'head_col': True, 'cw': 56, 'ch': 52, 'fs': 26, 'width_mm': 124, 'col_w': [160] + [54] * 8, 'rows': [
        ['Number', 12, 13, 14, 15, 16, 17, 18, 19], ['Remainder'] + [None] * 8]},
    why='The remainders go 0, 1, 2, 3 and then start again. (b) 30 = 28 + 2, and 28 is in the 4 times table, so the remainder is 2. (c) 100 = 4 × 25, so the remainder is 0.')
u.S(2, 'Find a number between 30 and 40. Dividing it by 6 gives remainder 1. Dividing it by 4 gives remainder 3.', parts=[
    P('a', 'The numbers that leave remainder 1 when divided by 6 are {b} and {b}.', A(['31', '37'], '31 and 37', list=True)),
    P('b', 'The number I am looking for is {b}.', A('31'))],
    why='Between 30 and 40, 6 × 5 = 30 and 6 × 6 = 36, so the numbers are 30 + 1 = 31 and 36 + 1 = 37. Now test them with 4: 31 ÷ 4 = 7 remainder 3 (right). 37 ÷ 4 = 9 remainder 1 (not right). The number is 31.')

u.S(3, '52 children go on a trip. Each bus has 9 seats.', parts=[
    P('a', 'The children need {b} buses.', A('6')),
    P('b', 'The last bus has {b} children.', A('7')),
    P('c', '{b} seats on the last bus are empty.', A('2'))],
    why='52 ÷ 9 = 5 remainder 7. 5 full buses are not enough, because 7 children are left. So they need 6 buses. The last bus has 7 children, and 9 - 7 = 2 seats are empty.')
u.S(3, 'The letters A, B, C and D repeat in this order.', parts=[
    P('a', 'The 30th letter is {b}.', A('B')), P('b', 'The 32nd letter is {b}.', A('D'))],
    figure={'type': 'l3_grid', 'head_col': True, 'cw': 56, 'ch': 52, 'fs': 26, 'width_mm': 120, 'col_w': [100] + [56] * 8, 'rows': [
        ['Place', 1, 2, 3, 4, 5, 6, 7, 8], ['Letter', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']]},
    why='The pattern repeats every 4 letters. 30 ÷ 4 = 7 remainder 2, so the 30th letter is the 2nd letter of the pattern: B. 32 ÷ 4 = 8 with no remainder, so the 32nd letter is the last letter of the pattern: D.')
u.S(3, 'Mei has 8 bags with 9 beads in each bag, and 5 loose beads. She shares all the beads equally among 9 friends.', parts=[
    P('a', 'Mei has {b} beads in all.', A('77')),
    P('b', 'Each friend gets {b} beads and {b} beads are left over.', A(['8', '5'], '8 beads each, 5 left over', list=True))],
    why='(a) 8 × 9 = 72, and 72 + 5 = 77. (b) 77 ÷ 9: 9 × 8 = 72 and 77 - 72 = 5. Each friend gets 8 beads and 5 beads are left over.')
u.S(3, 'Circle each number that has remainder 3 when you divide it by 5.\n{circ:18|23|33|41|48}', A(['18', '23', '33', '48'], '18, 23, 33 and 48', list=True),
    why='A number leaves remainder 3 when it is 3 more than a number in the 5 times table. 18 = 15 + 3, 23 = 20 + 3, 33 = 30 + 3 and 48 = 45 + 3. 41 is 1 more than 40, so it leaves remainder 1.')
u.S(3, 'Divide 47 by each of 4, 5, 6, 7 and 8. Which number gives the greatest remainder?   {circ:4|5|6|7|8}', A('8'),
    why='47 ÷ 4 = 11 remainder 3. 47 ÷ 5 = 9 remainder 2. 47 ÷ 6 = 7 remainder 5. 47 ÷ 7 = 6 remainder 5. 47 ÷ 8 = 5 remainder 7. The greatest remainder is 7, from dividing by 8.')

# ---------------- Think harder
u.T('Today is Tuesday.', parts=[
    P('a', '45 days from today it will be   ' + DAYS, A('Fri')),
    P('b', '20 days ago it was   ' + DAYS, A('Wed'))],
    hint='A week has 7 days. Divide by 7 and use the remainder.',
    why='(a) 45 ÷ 7 = 6 remainder 3. After 6 weeks it is Tuesday again. Then 3 more days: Wednesday, Thursday, Friday. (b) 20 ÷ 7 = 2 remainder 6. Go back 2 weeks to Tuesday, then back 6 more days: Wednesday.',
    space={'rows': ['Working:', '']})
u.T('Find the 2-digit number. Dividing it by 5 gives remainder 2. Dividing it by 3 gives remainder 1. Dividing it by 4 gives remainder 3. {b}', A('67'),
    hint='Begin with the clue that gives the fewest numbers to list.',
    why='The 2-digit numbers that leave remainder 2 when divided by 5 end in 2 or 7. Test them with 3 and 4. 67 = 66 + 1 (66 is in the 3 times table) and 67 = 64 + 3 (64 is in the 4 times table). No other number works.',
    space={'rows': ['My list:', 'Tests:', '']})
u.T('Aisha shares crayons among her cousins. If each cousin gets 3 crayons, 11 crayons are not used. If each cousin gets 5 crayons, she needs 7 more. How many cousins are there? How many crayons does she have?', beyond='Too many and too few', parts=[
    P('a', 'There are {b} cousins.', A('9')), P('b', 'She has {b} crayons.', A('38'))],
    hint='Compare the 2 plans: each cousin gets 2 more crayons.',
    why='Giving each cousin 2 more crayons uses the 11 crayons that were not used and needs 7 more: 11 + 7 = 18 crayons. So 18 ÷ 2 = 9 cousins. The crayons: 9 × 3 + 11 = 38. Check: 9 × 5 = 45 and 45 - 38 = 7 more are needed.',
    space={'rows': ['Working:', '']})

# ---------------- Go further
u.G('Beyond Level 3: Remainders when you add and double.\nA number leaves remainder 3 when divided by 7.', parts=[
    P('a', 'Add 5 to it. The new remainder is {b}.', A('1')),
    P('b', 'Double it. The new remainder is {b}.', A('6')),
    P('c', 'Another number leaves 5 when divided by 8. Doubled, it leaves {b}.', A('2'))],
    hint='Try a number like 10 (remainder 3 when divided by 7). Test it.',
    why='(a) 3 + 5 = 8, and 8 ÷ 7 leaves remainder 1. Test: 10 + 5 = 15 and 15 ÷ 7 = 2 remainder 1. (b) 3 + 3 = 6, which is smaller than 7. Test: 20 ÷ 7 = 2 remainder 6. (c) 5 + 5 = 10, and 10 ÷ 8 leaves remainder 2. Test: 13 doubled is 26, and 26 ÷ 8 = 3 remainder 2.',
    space={'rows': ['My test numbers:']})
u.G('Ali has between 20 and 100 marbles. Counting in 3s leaves 1 over. Counting in 4s leaves 2 over. Counting in 5s leaves 3 over. How many marbles does he have? {b}', A('58'),
    hint='For each clue, how far is the number from a full group?',
    why='1 left over when counting in 3s is the same as being 2 short of a full group. Counting in 4s with 2 left is 2 short too, and counting in 5s with 3 left is 2 short. So the number is 2 less than a number in the 3, 4 and 5 times tables. The first such number is 60 (and then 120). 60 - 2 = 58. Check: 58 ÷ 3 = 19 r 1, 58 ÷ 4 = 14 r 2, 58 ÷ 5 = 11 r 3.')
u.G('Make up your own number riddle: a range and 2 remainder clues. Only ONE number may fit. Swap with a grown-up.',
    A('17', 'Answers vary. Example: I am between 10 and 25. When I am divided by 4 the remainder is 1. When I am divided by 3 the remainder is 2. The only number is 17.'),
    hint='Pick your number first. Then find its remainders.',
    why='Check that your number gives the remainders you wrote, and list the numbers that fit your first clue. Test each with the second clue. In the example, the numbers with remainder 1 when divided by 4 are 13, 17 and 21. Only 17 leaves remainder 2 when divided by 3.',
    space={'rows': ['My riddle:', 'The numbers I tested:']})
u.G('Beyond Level 3: Making numbers with 2 sizes.\nBen sells eggs in boxes of 3 and boxes of 5. An order must be whole boxes.', parts=[
    P('a', 'Can he fill an order for 11 eggs?   {circ:Yes|No}', A('Yes')),
    P('b', 'Orders from 1 to 15 he CANNOT fill:\n{ll}', A(['1', '2', '4', '7'], '1, 2, 4 and 7', list=True))],
    hint='List the orders he can fill. Which numbers are missing?',
    why='Orders he can fill: 3, 5, 6 (3 + 3), 8 (3 + 5), 9, 10, 11 (3 + 3 + 5), 12, 13 (3 + 5 + 5), 14 (3 + 3 + 3 + 5), 15. So the orders he cannot fill are 1, 2, 4 and 7.')

# ---------------- Check yourself
u.C('Divide. 52 ÷ 8 = {b} remainder {b}', A(['6', '4'], '6 remainder 4', list=True), why='8 × 6 = 48 and 52 - 48 = 4. So 52 ÷ 8 = 6 remainder 4.')
u.C('A bus holds 9 people. How many buses are needed for 40 people? {b}', A('5'), why='40 ÷ 9 = 4 remainder 4. The 4 people left over need another bus: 5 buses.')
u.C('Mei packs 25 muffins into boxes of 6. How many muffins are left over? {b}', A('1'), why='6 × 4 = 24 and 25 - 24 = 1. One muffin is left over.')
u.C('Find a number between 20 and 30. It leaves remainder 2 when divided by 3 and remainder 4 when divided by 5. {b}', A('29'),
    why='The numbers from 20 to 30 that leave remainder 2 when divided by 3 are 20, 23, 26 and 29. Of these, only 29 leaves remainder 4 when divided by 5 (25 + 4).')
u.save()
