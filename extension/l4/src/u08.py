from lib import *
U = 'L4U08'
TILES = lambda shapes, **kw: dict({'type': 'l4_tiles', 'shapes': shapes, 'cell': 36, 'width_mm': 150}, **kw)
def net(cells, name=None, labels=None):
    d = {'cells': cells, 'shade': False}
    if name: d['name'] = name
    if labels: d['labels'] = labels
    return d
GRID = lambda R, C, cs=44, **kw: dict({'type': 'l4_grid', 'rows': R, 'cols': C, 'cell': cs, 'width_mm': 90}, **kw)

NET_A = [[0, 1], [1, 1], [2, 1], [3, 1], [0, 0], [2, 2]]
NET_B = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 1], [3, 1]]
NET_C = [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2]]
NET_D = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [2, 0]]
NET_E = [[0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1]]
NET_F = [[0, 1], [1, 1], [2, 1], [3, 1], [0, 0], [3, 0]]

learn = {
 'intro': 'A net is a flat shape that folds into a solid. A cube net has 6 squares. In a line of 3 squares, the 2 end squares are opposite faces. On a dice, opposite faces add up to 7.',
 'example': {
  'problem': 'Does this net fold into a cube? Which face is opposite P?',
  'figure': TILES([net([[0, 1], [1, 1], [2, 1], [3, 1], [1, 0], [2, 2]], labels={'0,1': 'P', '1,1': 'Q', '2,1': 'R', '3,1': 'S', '1,0': 'T', '2,2': 'U'})], cell=34, width_mm=62),
  'steps': ['Choose a base. The row of 4 squares wraps round as walls.', 'One square is above the row and one is below. They make the lid and the base.', 'P and R have 1 square between them. They are opposite.'],
  'answer': 'It folds into a cube. R is opposite P.'},
 'example2': {
  'problem': 'Complete the figure. The dashed line must be a line of symmetry.',
  'figure': GRID(4, 6, 40, shade=[[0, 2], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 2]], axis={'kind': 'v', 'at': 3}, width_mm=68),
  'steps': ['Flip each shaded square across the line.', 'The partner is the same distance from the line.'],
  'answer': 'Each shaded square gets a partner the same distance from the line.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to do it',
           'steps': ['Net: choose a base. Fold the squares round it in your head.',
                     'A net needs 1 base, 1 lid and 4 walls.',
                     'Symmetry: count squares from the line to the partner.']},
 'facts': {'title': 'Good to know', 'lines': ['Dice: opposite faces add up to 7.', 'A rectangle has 2 lines of symmetry. A square has 4.', 'No fold: 4 squares at one corner, or 5 in a row.']},
 'try': {'id': U + '-L01', 'text': 'Opposite faces of a dice add up to 7. What number is opposite 4? {b}',
         'answer': A(3),
         'explanation': '4 + 3 = 7, so 3 is opposite 4.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'Which of these nets fold into a cube? Circle the letters.',
  fig=TILES([net(NET_A, 'A'), net(NET_B, 'B'), net(NET_C, 'C'), net(NET_D, 'D')], cell=36, gap=0.8, width_mm=160),
  ans=A('A', 'C', text='A and C', unordered=True),
  why='Fold each net in your head. A: the row of 4 makes the walls, and one square above and one below make the lid and the base. It folds. B: the 2 by 2 block of squares has 4 squares meeting at a corner, but only 3 faces of a cube meet at a corner. D: 5 squares in a row wrap round and the 5th covers the 1st. C: the staircase folds into a cube.'))
S[-1]['answer']['text'] = 'A and C'
S.append(item(U+'-S02', 'start', 1, 'The net folds into a cube. Name the letter opposite each one.',
  fig=TILES([net(NET_E, labels={'0,0': 'P', '1,0': 'Q', '2,0': 'R', '2,1': 'S', '3,1': 'T', '4,1': 'U'})], cell=36, width_mm=92),
  parts=[P('a', 'Opposite P: {b}', A('R')), P('b', 'Opposite Q: {b}', A('T')), P('c', 'Opposite S: {b}', A('U'))], partsrow=True,
  why='In the row of 3 squares P, Q, R, the 2 ends P and R are opposite. Q and T are opposite (1 square between them going round the step). The last pair is S and U.'))
S.append(item(U+'-S03', 'start', 1, 'Each pair of opposite faces on a dice has a total of 7. Fill in the blank squares. Go row by row.',
  fig=TILES([net(NET_A, labels={'0,0': '1', '0,1': '2', '1,1': '3', '2,1': '', '3,1': '', '2,2': ''})], cell=40, width_mm=78),
  ans=A(5, 4, 6, text='5, 4, 6 (row by row)'),
  why='Find the opposite squares. 2 and the third square of the row are opposite, so that square is 7 − 2 = 5. 3 and the fourth square are opposite, so it is 7 − 3 = 4. 1 and the bottom square are opposite, so it is 7 − 1 = 6.'))
S[-1]['answer']['list'] = True
S.append(item(U+'-S04', 'start', 2, 'Fold on the dashed line. Shade squares so the 2 halves match. How many squares are shaded in all? {b}',
  fig=GRID(6, 8, 44, shade=[[5, 1], [5, 2], [5, 3], [4, 1], [4, 2], [4, 3], [3, 1], [3, 2], [3, 3], [2, 2], [2, 3], [1, 3]], axis={'kind': 'v', 'at': 4}, width_mm=66),
  ans=A(24), why='There are 12 shaded squares on the left of the line. Each needs a partner on the right, so 12 more squares are shaded. 12 + 12 = 24.'))
S.append(item(U+'-S05', 'start', 2, 'How many lines of symmetry does each shape have?',
  fig=TILES([dict({'cells': [[0, 0], [1, 0], [2, 0], [1, 1]], 'shade': False, 'name': 'A'}), dict({'cells': [[0, 0], [1, 0], [2, 0], [3, 0]], 'shade': False, 'name': 'B'}), dict({'cells': [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]], 'shade': False, 'name': 'C'}), dict({'cells': [[0, 0], [1, 0], [1, 1], [2, 1]], 'shade': False, 'name': 'D'})], cell=36, gap=0.9, width_mm=124),
  parts=[P('a', 'A: {b}', A(1)), P('b', 'B: {b}', A(2)), P('c', 'C: {b}', A(4)), P('d', 'D: {b}', A(0))], partsrow=True,
  why='A has 1 line (down the middle). B has 2 lines (along its length and across its middle). C, the plus sign, has 4 lines (up-down, across and the 2 diagonals). D has none: it looks the same when turned half way round, but no fold makes the halves match.'))
S.append(item(U+'-S06', 'start', 2, 'There are 2 dashed lines. Shade 1 more square. The halves must then match on one of the lines.',
  fig=GRID(5, 5, 46, shade=[[1, 2], [2, 0], [2, 2], [2, 4], [3, 2], [4, 1]], axes=[{'kind': 'v', 'at': 2.5}, {'kind': 'h', 'at': 2.5}], width_mm=60),
  parts=[P('a', 'How many different squares can you shade? {b}', A(2))], figside=True,
  why='Look for a shaded square with no partner. Only the one in the bottom row has none. For the up-down line, its partner is in the bottom row on the right. For the across line, its partner is in the top row, above it. Each fix works for one line, so there are 2 ways.'))
S.append(item(U+'-S07', 'start', 3, 'A dice sits on a table. The top face shows 6 and the face in front shows 4.',
  parts=[P('a', 'The bottom face shows {b}', A(1)), P('b', 'The face at the back shows {b}', A(3)),
         P('c', 'The 4 side faces add up to {b}', A(14))],
  why='Opposite faces add up to 7. The bottom is 7 − 6 = 1. The back is 7 − 4 = 3. The 4 side faces are 2 opposite pairs, and 7 + 7 = 14.'))
S.append(item(U+'-S08', 'start', 3, 'A dice net is made of 6 squares. Each square is 3 cm by 3 cm. Find the area of the card. {b} cm²',
  ans=A(54), why='Each square has an area of 3 × 3 = 9 cm². The net has 6 squares: 6 × 9 = 54 cm².'))
S.append(item(U+'-S09', 'start', 3, 'Shade squares so the top and bottom halves match on the dashed line. How many are shaded in all? {b}',
  fig=GRID(8, 6, 40, shade=[[3, 0], [3, 1], [3, 2], [3, 3], [2, 1], [2, 2], [2, 4], [1, 2], [1, 3], [0, 2]], axis={'kind': 'h', 'at': 4}, width_mm=60),
  ans=A(20), why='There are 10 shaded squares above the line. Each needs a partner below the line, so 10 more squares are shaded. 10 + 10 = 20.'))
S.append(item(U+'-S10', 'start', 3, 'A cube has edges of 5 cm.',
  parts=[P('a', 'All 12 edges are 5 cm long. The edges add up to {b} cm', A(60)), P('b', 'The area of its net is {b} cm²', A(150))], partsrow=True,
  why='(a) 12 × 5 = 60 cm. (b) Each face is 5 × 5 = 25 cm², and the net has 6 faces: 6 × 25 = 150 cm².'))

T.append(item(U+'-T01', 'think', 4, 'Mei paints each face of a cube red or blue.',
  parts=[P('a', 'No 2 red faces may share an edge. The most red faces is {b}', A(2)),
         P('b', 'Now red faces may share an edge, but no 2 red faces may be opposite. The most red faces is {b}', A(3))],
  hint='Which faces share an edge with a given face?',
  why='(a) A face shares an edge with 4 faces and is opposite just 1. Two opposite red faces do not share an edge. A third red face would touch one of them. So the most is 2. (b) Take 3 faces that meet at one corner. They are not opposite each other, so 3 red faces work. A 4th red face would be opposite one of them. So the most is 3.',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T02', 'think', 4, 'Mei sees 3 faces of a dice at the same corner. Their numbers add up to 10.',
  parts=[P('a', 'The numbers she can see, smallest first: {b} {b} {b}', A(1, 4, 5)), P('b', 'The numbers she cannot see, smallest first: {b} {b} {b}', A(2, 3, 6))],
  hint='At a corner, the 3 faces are from 3 different opposite pairs.',
  why='The pairs are 1 and 6, 2 and 5, 3 and 4. She sees one number from each pair, so no two of the 3 numbers add up to 7. The only choice with a total of 10 is 1, 5 and 4. The hidden faces are opposite: 6, 2 and 3.',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T03', 'think', 4, 'On a 3 by 3 grid, shade exactly 3 squares. A fold down the middle must make the halves match. How many patterns can you make? {b}',
  fig=GRID(3, 3, 44, axis={'kind': 'v', 'at': 1.5}, width_mm=42),
  ans=A(10), hint='Middle-column squares match themselves. The others come in pairs.',
  why='The 3 shaded squares are 3 from the middle column, or 1 from the middle column and 1 pair. 3 in the middle column: 1 way. 1 in the middle column (3 choices) and 1 pair (3 rows to choose): 3 × 3 = 9 ways. 1 + 9 = 10.',
  figright=True, space={'rows': ['List:', '', '']}))

G.append(item(U+'-G01', 'go', 5, 'Beyond Level 4: Painted cubes\nPaint all the outside faces of a big cube that is 3 by 3 by 3. Then cut it into 27 small cubes.',
  parts=[P('a', 'Small cubes with 3 painted faces: {b}', A(8)), P('b', 'Small cubes with 2 painted faces: {b}', A(12)),
         P('c', 'Small cubes with 1 painted face: {b}', A(6)), P('d', 'Small cubes with no paint: {b}', A(1))],
  hint='Corners, edges and faces of the big cube. Count each kind.',
  why='3 painted faces: the 8 corner cubes. 2 painted faces: 1 cube in the middle of each of the 12 edges, so 12. 1 painted face: 1 cube in the middle of each of the 6 faces, so 6. No paint: the cube in the very middle, so 1. Check: 8 + 12 + 6 + 1 = 27.'))
G.append(item(U+'-G02', 'go', 5, 'Shade just 1 square of a 5 by 5 grid. Some squares give a picture with a line of symmetry. The line can go up-down, across or along a diagonal.',
  fig=GRID(5, 5, 40, axes=[{'kind': 'v', 'at': 2.5}, {'kind': 'h', 'at': 2.5}], width_mm=52),
  parts=[P('a', 'The number of squares that give at least 1 line of symmetry: {b}', A(17)),
         P('b', 'The number that give exactly 1 line: {b}', A(16))],
  hint='Try a corner square, then an edge square, then the middle.',
  why='A single square has a line of symmetry when it lies on the middle row, the middle column or a diagonal. Middle row: 5 squares. Middle column: 5 squares, with 1 shared. That is 9. Each diagonal has 5 squares, and the middle is shared again, so the diagonals add 8 more squares. In all 9 + 8 = 17. The middle square has 4 lines. Every other one has exactly 1: 17 − 1 = 16.',
  figright=True))
G.append(item(U+'-G03', 'go', 5, 'A dice has 1 on top, 2 facing north and 3 facing east. It rolls north, then east, then north again. A roll north puts the north face on the table. A roll east puts the east face on the table.',
  parts=[P('a', 'The top face is now {b}', A(6)), P('b', 'The bottom face is now {b}', A(1))],
  hint='Write the top, north and east faces after each roll.',
  why='Start: top 1, bottom 6, north 2, south 5, east 3, west 4. Roll north: the north face 2 lands on the table, so the top is 5, the bottom is 2, the north face is 1 and the south face is 6. Roll east: the east face 3 lands on the table, so the top is 4, the bottom is 3, the east face is 5 and the west face is 2. Roll north: the north face 1 lands on the table, so the bottom is 1 and the top is the old south face, 6.',
  ))

C.append(item(U+'-C01', 'quiz', None, 'Does this net fold into a cube? {circ:Yes|No}',
  fig=TILES([net(NET_F)], cell=34, width_mm=34), ans=A('No'), figright=True,
  why='Both extra squares are above the row of 4, on the same side. When the row wraps round, they land on the same face. So the net does not fold.'))
C.append(item(U+'-C02', 'quiz', None, 'A rectangle has a different length and width. How many lines of symmetry does it have? {b}', ans=A(2),
  why='It can be folded along the middle in 2 ways, and the halves match. The diagonals do not work.'))
C.append(item(U+'-C03', 'quiz', None, 'A dice has 2 on top and 3 in front. The bottom shows {b} and the back shows {b}.', ans=A(5, 4, text='bottom 5, back 4'),
  why='Opposite faces add up to 7. The bottom is 7 − 2 = 5 and the back is 7 − 3 = 4.'))
C.append(item(U+'-C04', 'quiz', None, 'A cube has edges of 4 cm. Its net has an area of {b} cm².', ans=A(96),
  why='Each face is 4 × 4 = 16 cm². The net has 6 faces: 6 × 16 = 96 cm².'))

unit = {'schema_version': 1, 'level': 4, 'unit': 8, 'id': U, 'title': 'Symmetry and Nets', 'topic': 'Symmetry and nets', 'holiday_lesson': 8,
        'goal': 'I can tell which nets fold into a cube and which faces are opposite. I can complete a figure so that a line is a line of symmetry.',
        'learn': learn, 'items': S + T + G + C}
write(8, unit)
