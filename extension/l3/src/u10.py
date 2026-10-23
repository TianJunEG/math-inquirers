from lib import *

u = Unit(10, 'Think it through', 'Mixed puzzles',
         'I can start a puzzle by drawing it, listing it or making a table. I can read a bar graph and solve logic puzzles.')


def hexes(n):
    """segments of n hexagons joined in a row (side 1, pointy top); shared sides are drawn once"""
    verts = [(0, 0.5), (0.866, 0), (1.732, 0.5), (1.732, 1.5), (0.866, 2), (0, 1.5)]
    edges = set()
    for k in range(n):
        v = [(round(x + 1.732 * k, 3), y) for x, y in verts]
        for i in range(6):
            a, b = v[i], v[(i + 1) % 6]
            edges.add(tuple(sorted([a, b])))
    return [[a[0], a[1], b[0], b[1]] for a, b in sorted(edges)]


def graph(cats, vals, mx, step, w=118, **kw):
    d = {'type': 'l3_bargraph', 'cats': cats, 'values': vals, 'max': mx, 'step': step, 'width_mm': w}
    d.update(kw)
    return d


u.learn(
    'To start a puzzle, try one of 3 ways. Draw it, list it, or make a table. Then check every clue.',
    {'problem': 'Kumar is 6th from the front and 3rd from the back of a line. Count the children in the whole line.',
     'figure': {'type': 'l3_queue', 'n': 8, 'marks': {'6': 'Kumar'}, 'width_mm': 120},
     'steps': ['Draw the line. Put Kumar in 6th place from the front.', 'Kumar is 3rd from the back, so 2 children are behind him.',
               '5 children are in front of Kumar, then Kumar, then 2 behind: 5 + 1 + 2 = 8.', 'Check: 6 + 3 - 1 = 8.'],
     'answer': 'There are 8 children in the line.'},
    {'title': 'Three ways to start',
     'steps': ['Draw it: make a picture of the puzzle.', 'List it: write every case in order.', 'Table: write what you know in rows and columns.', 'Check your answer against every clue.']},
    {'text': 'Lily is 3rd from the front and 9th from the back of a line. The line has {b} children.', 'answer': A('11'),
     'explanation': '2 children are in front of Lily and 8 are behind her. 2 + 1 + 8 = 11. Check: 3 + 9 - 1 = 11.'})
u.u['learn']['tight'] = True

# ---------------- Start here (pages 1 to 3)
u.S(1, 'The bar graph shows the books 4 children read. Kumar read 15 more books than Siti. Draw Kumar’s bar on the graph.', parts=[
    P('a', 'Most books: {b}', A('Mei')),
    P('b', 'Mei read {b} more than Ben.', A('15')),
    P('c', 'Kumar read {b}.', A('25')),
    P('d', 'In all they read {b}.', A('105'))],
    figure=graph(['Ali', 'Ben', 'Mei', 'Siti', 'Kumar'], [25, 15, 30, 10, None], 35, 5, 100, unit_label='books', h=260), figside=True,
    why='(a) The tallest bar is Mei’s. (b) 30 - 15 = 15. (c) Siti read 10 books, so Kumar read 10 + 15 = 25. (d) 25 + 15 + 30 + 10 + 25 = 105.')
u.S(1, 'The graph shows the stamps 3 clubs collected. Each thin line is 10 stamps.', parts=[
    P('a', 'Club A: {b}', A('70')), P('b', 'Club B: {b}', A('110')),
    P('c', 'Club C: {b}', A('90')), P('d', 'All 3: {b}', A('270'))],
    figure=graph(['Club A', 'Club B', 'Club C'], [70, 110, 90], 140, 20, 86, minor=10, unit_label='stamps', h=250), figside=True,
    why='The labelled lines go up in 20s and there is a thin line halfway between them, so each thin line is 10. A is at 70, B is at 110 and C is at 90. Together: 70 + 110 + 90 = 270.')
u.S(1, 'The 3rd of a month is a Tuesday.', parts=[
    P('a', 'The 24th is a   {circ:Mon|Tue|Wed|Thu|Fri|Sat|Sun}', A('Tue')), P('b', 'The 30th is a   {circ:Mon|Tue|Wed|Thu|Fri|Sat|Sun}', A('Mon'))],
    space={'rows': ['Working:']},
    why='(a) From the 3rd to the 24th is 21 days, which is 3 weeks. So the 24th is a Tuesday again. (b) From the 3rd to the 30th is 27 days = 3 weeks and 6 days. 6 days after Tuesday is Monday.')
u.S(2, 'Each child has a different fruit. Kumar has neither the apple nor the banana. The child with the orange has a name with 4 letters. Wei does not have the apple. Use ticks and crosses in the grid.', parts=[
    P('a', 'Kumar has the {circ:apple|banana|grapes|orange}', A('grapes')), P('b', 'Aisha has the {circ:apple|banana|grapes|orange}', A('apple')),
    P('c', 'Wei has the {circ:apple|banana|grapes|orange}', A('banana')), P('d', 'Lily has the {circ:apple|banana|grapes|orange}', A('orange'))],
    figure={'type': 'l3_grid', 'head_row': True, 'head_col': True, 'corner': True, 'cw': 100, 'ch': 44, 'fs': 24, 'col_w': [100, 100, 110, 110, 110], 'width_mm': 100,
            'rows': [['', 'apple', 'banana', 'grapes', 'orange'], ['Kumar', None, None, None, None], ['Aisha', None, None, None, None], ['Wei', None, None, None, None], ['Lily', None, None, None, None]]},
    why='Only Lily has a name with 4 letters, so Lily has the orange. Kumar has neither the apple nor the banana, and the orange is taken, so Kumar has the grapes. Wei does not have the apple, so Wei has the banana. Aisha has the apple.')
u.S(2, 'Draw it. Count the children in each line.', parts=[
    P('a', 'Ravi is 3rd from the front. Mei is last. 5 children stand between them. The line has {b} children.', A('9')),
    P('b', 'Aisha is 8th from the front and 3rd from the back. The line has {b} children.', A('10'))],
    space={'rows': ['Draw it:']},
    why='(a) Ravi is 3rd. The 5 children between are 4th to 8th. Mei is 9th and last. (b) 7 children are in front of Aisha and 2 are behind her: 7 + 1 + 2 = 10.')
u.S(2, 'A café meal is 1 drink and 1 snack. The drinks are milk and tea. The snacks are a bun, a pie and fruit. List every different meal.', parts=[
    P('a', 'Write the list below.', A(['milk bun', 'milk pie', 'milk fruit', 'tea bun', 'tea pie', 'tea fruit'], 'milk bun, milk pie, milk fruit, tea bun, tea pie, tea fruit', list=True)),
    P('b', 'There are {b} meals with milk.', A('3')),
    P('c', 'There are {b} meals with a bun or a pie.', A('4'))],
    space={'rows': ['My list:']},
    why='Fix the drink and list the snacks in order: milk bun, milk pie, milk fruit, then tea bun, tea pie, tea fruit. 3 meals have milk. The meals with a bun or a pie are milk bun, milk pie, tea bun and tea pie: 4.')
u.S(3, 'Hexagons are joined in a row with sticks. 1 hexagon needs 6 sticks. 2 hexagons need 11 sticks. 3 hexagons need 16 sticks. Make a table.', parts=[
    P('a', '6 hexagons need {b} sticks.', A('31')), P('b', '41 sticks make {b} hexagons.', A('8'))],
    figure={'type': 'l3_segs', 'segs': hexes(3), 'k': 46, 'pad': 14, 'width_mm': 50},
    space={'table': {'cols': ['hexagons', 'sticks'], 'rows': 4}},
    why='Each new hexagon adds 5 sticks. The table goes 1: 6, 2: 11, 3: 16, 4: 21, 5: 26, 6: 31. For 41 sticks, count on: 7 hexagons need 36 and 8 hexagons need 41.')
u.S(3, 'Which numbers fit all the clues? The number is even and has 3 digits. It is less than 400. Its digits add up to 9, and none is 0. The tens digit is more than the ones digit.\n{ll}',
    A(['162', '252', '342'], '162, 252 and 342', list=True),
    why='The hundreds digit is 1, 2 or 3. The ones digit is even and not 0, so it is 2, 4 or 6, and the tens digit is greater. With 1: tens + ones = 8, so 6 and 2. With 2: tens + ones = 7, so 5 and 2. With 3: tens + ones = 6, so 4 and 2. The numbers are 162, 252 and 342.')
u.S(3, 'I think of a number. I multiply it by 3 and take away 4. The answer is 17. My number is {b}.', A('7'),
    space={'rows': ['Working backwards:']},
    why='Work backwards. Add 4 to 17: 21. Divide by 3: 7. Check: 7 × 3 = 21, and 21 - 4 = 17.')
u.S(3, 'Aisha has $10. A juice costs $1.85 and a sandwich costs $3.40. She buys 2 juices and 1 sandwich. Her change is ${bw}.', A('2.90'),
    why='2 juices cost 2 × 1.85 = 3.70. With the sandwich: 3.70 + 3.40 = 7.10. Change: 10.00 - 7.10 = 2.90.')

# ---------------- Think harder
u.T('A grid is made of 2 rows of 3 small squares. Count the rectangles of every size, squares included. {b}', A('18'),
    figure={'type': 'l3_grid', 'rows': [[None, None, None], [None, None, None]], 'cw': 70, 'ch': 60, 'width_mm': 46}, figside=True,
    hint='Count the small squares first. Then the wider ones.',
    space={'rows': ['Height 1, width 1, 2, 3:', 'Height 2, width 1, 2, 3:']},
    why='Height 1: width 1 gives 6, width 2 gives 4 (2 in each row), width 3 gives 2. Height 2: width 1 gives 3, width 2 gives 2, width 3 gives 1. In all: 6 + 4 + 2 + 3 + 2 + 1 = 18.')
u.T('One of Ben, Aisha and Wei broke a cup. They each say 1 thing: Ben “Wei did it”, Aisha “Not me”, Wei “Ben is lying”. Exactly 1 of them tells the truth. Who broke the cup?   {circ:Ben|Aisha|Wei}', A('Aisha'),
    hint='Pick one child. Are exactly 1 of the 3 sayings true?',
    space={'rows': ['My tests:', '', '']},
    why='If Ben did it: Aisha tells the truth, and Wei tells the truth (Ben’s words are a lie). That is 2 true statements. If Wei did it: Ben and Aisha both tell the truth. If Aisha did it: Ben lies, Aisha lies and Wei tells the truth. That is exactly 1. So Aisha did it.')
u.T('A shop sold 185 pencils in 4 days. Tuesday sold 15 more than Monday. Wednesday sold twice as many as Monday. Thursday sold 10 fewer than Wednesday.', parts=[
    P('a', 'Monday: {b}', A('30')), P('b', 'Tuesday: {b}', A('45')), P('c', 'Wednesday: {b}', A('60')), P('d', 'Thursday: {b}', A('50'))],
    partsrow=True,
    hint='Draw Monday as 1 bar. Then draw the other days with it.',
    space={'rows': ['Draw your bars:', '']},
    why='Monday is 1 box. Tuesday is 1 box and 15. Wednesday is 2 boxes. Thursday is 2 boxes take away 10. In all: 6 boxes + 15 - 10 = 6 boxes + 5 = 185. So 6 boxes = 180 and 1 box = 30. Monday 30, Tuesday 45, Wednesday 60, Thursday 50. Check: 30 + 45 + 60 + 50 = 185.')

# ---------------- Go further
u.G('Count the squares of every size in a 4 by 4 grid. Begin with the small ones.', parts=[
    P('a', '1 by 1 squares: {b}', A('16')), P('b', '2 by 2 squares: {b}', A('9')), P('c', '3 by 3 squares: {b}', A('4')),
    P('d', 'All the squares: {b}', A('30'))],
    partsrow=True,
    hint='A 2 by 2 square can sit in 3 places across and 3 down.',
    why='There are 16 small squares. A 2 by 2 square fits in 3 places across and 3 down: 9. A 3 by 3 square fits in 2 places across and 2 down: 4. There is 1 big square. 16 + 9 + 4 + 1 = 30.')
u.G('Beyond Level 3: A balance puzzle.\n9 coins look the same. One is lighter. You have a balance scale.', parts=[
    P('a', 'With 3 coins, you can always find the light coin in {b} weighing.', A('1')),
    P('b', 'With 9 coins, you can always find it in {b} weighings.', A('2'))],
    hint='Put 3 coins on each side. What does the scale tell you?',
    why='(a) Put 1 coin on each side. If the scale tips, the light coin is on the high side. If it balances, it is the coin left out. That is 1 weighing. (b) Weigh 3 coins against 3 coins. This shows which group of 3 has the light coin. Then use the 1 weighing from (a). That is 2 weighings.')
u.G('Ali has 8 coins. They are 10¢ coins and 20¢ coins, worth $1.50 in all. Find how many coins of each kind.', parts=[
    P('a', '{b} ten-cent coins', A('1')), P('b', '{b} twenty-cent coins', A('7'))],
    hint='Try 4 of each. How much are they worth?',
    space={'table': {'cols': ['10¢ coins', '20¢ coins', 'value'], 'rows': 2}},
    why='If all 8 coins were 10¢, they would be worth 80¢. They are worth 150¢, which is 70¢ more. Changing one 10¢ coin to a 20¢ coin adds 10¢, so 7 coins are 20¢ and 1 coin is 10¢. Check: 10 + 7 × 20 = 150.')
u.G('Make up a logic puzzle with 3 friends and 3 sports. Write 3 clues. Only ONE answer may fit. Swap with a grown-up.', A('Lily: chess', 'Answers vary. Example: Lily, Wei and Kumar each play a different game: chess, ball or cards. Lily does not play ball. Wei plays neither chess nor cards. Kumar does not play chess. Answer: Lily plays chess, Wei plays ball, Kumar plays cards.'),
    hint='Pick the answer first. Then write clues that rule out the others.',
    space={'rows': ['My clues:', '', '']},
    why='Check that your clues are true for your answer and that every other arrangement breaks a clue. In the example, Wei plays ball (clue 2), then Kumar cannot play chess (clue 3), so Kumar plays cards and Lily plays chess.')

# ---------------- Check yourself
u.C('Each dashed line is 10. Tuesday sold {b} more than Monday.', A('30'),
    figure=graph(['Mon', 'Tue', 'Wed'], [20, 50, 30], 60, 20, 68, minor=10, unit_label='pencils', h=95), figright=True,
    why='Monday is at 20 and Tuesday is at 50. 50 - 20 = 30.')
u.C('In a line, 2 children stand in front of Ben and 6 children stand behind him. The line has {b} children.', A('9'),
    why='2 + 1 + 6 = 9. Do not forget Ben.')
u.C('Lily is shorter than Mei. Mei is shorter than Ben. Ben is shorter than Aisha. Who is the 2nd tallest?   {circ:Lily|Mei|Ben|Aisha}', A('Ben'),
    why='From the shortest: Lily, Mei, Ben, Aisha. The tallest is Aisha, so the 2nd tallest is Ben.')
u.C('Look for a pattern. 2, 6, 10, 14, ... The 8th number is {b}.', A('30'),
    why='The numbers go up by 4. The 8th number is 2 + 7 × 4 = 30.')
u.save()
