from lib import *
U = 'L4U07'
POLY = lambda shapes, **kw: dict({'type': 'l4_poly', 'shapes': shapes, 'cell': 36, 'width_mm': 100}, **kw)
def L_(pts, labels=(), **kw):
    return dict({'pts': pts, 'labels': list(labels)}, **kw)

learn = {
 'intro': 'Area is the space inside a shape, in cm². Perimeter is the distance round the edge, in cm. For a shape with square corners, take a piece away from a big rectangle, or split it into rectangles.',
 'example': {
  'problem': 'The shape has square corners. Find its area and its perimeter.',
  'figure': POLY([L_([[0, 0], [10, 0], [10, 4], [6, 4], [6, 6], [0, 6]], [{'seg': 0, 'text': '10 cm'}, {'seg': 5, 'text': '6 cm'}, {'seg': 2, 'text': '4 cm'}, {'seg': 3, 'text': '2 cm', 'in': True}])], cell=22, width_mm=82),
  'steps': ['Big rectangle: 10 × 6 = 60. The missing corner is 4 × 2 = 8. Area = 60 − 8 = 52.', 'Push the steps out to make a rectangle. The perimeter is 10 + 6 + 10 + 6 = 32.'],
  'answer': 'Area 52 cm². Perimeter 32 cm.'},
 'example2': {
  'problem': 'Rectangles with whole-cm sides have an area of 18 cm². Find the perimeter of each one.',
  'figure': {'type': 'l4_table', 'head': ['Length', 'Width', 'Perimeter'], 'rows': [['18', '1', '38'], ['9', '2', '22'], ['6', '3', '18']], 'cell_h': 44, 'font': 26, 'width_mm': 78},
  'steps': ['List the pairs that multiply to 18 in order: 1 × 18, 2 × 9, 3 × 6.', 'Perimeter = 2 × (length + width).'],
  'answer': 'The smallest perimeter is 18 cm, from 6 cm by 3 cm.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to do it',
           'steps': ['Missing sides: use the opposite sides.',
                     'Area: split into rectangles, or take a piece away.',
                     'Perimeter: push the steps out to a rectangle.']},
 'facts': {'title': 'Good to know', 'lines': ['Rectangle: area = length × width.', 'Perimeter = 2 × (length + width).', 'A square has 4 equal sides.']},
 'try': {'id': U + '-L01', 'text': 'A rectangle is 12 cm long and 5 cm wide. A 3 cm by 2 cm corner is cut off. What is the area of the shape that is left? {b} cm²',
         'answer': A(54),
         'explanation': 'The rectangle has an area of 12 × 5 = 60 cm². The corner has an area of 3 × 2 = 6 cm². 60 − 6 = 54 cm².'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'The shape has square corners. Find the missing sides a and b. Then find the area and the perimeter.',
  fig=POLY([L_([[0, 0], [11, 0], [11, 3], [7, 3], [7, 8], [0, 8]], [{'seg': 0, 'text': '11 cm'}, {'seg': 1, 'text': '3 cm'}, {'seg': 2, 'text': 'a'}, {'seg': 3, 'text': 'b', 'in': True}, {'seg': 4, 'text': '7 cm'}, {'seg': 5, 'text': '8 cm'}])], cell=24, width_mm=84),
  parts=[P('a', 'a = {b} cm   b = {b} cm', A(4, 5, text='a = 4 cm, b = 5 cm')),
         P('b', 'Area: {b} cm²', A(68)), P('c', 'Perimeter: {b} cm', A(38))],
  figside=True,
  why='(a) The top is 11 cm and the bottom is 7 cm, so a = 11 − 7 = 4 cm. The left is 8 cm and the right is 3 cm, so b = 8 − 3 = 5 cm. (b) Split: 11 × 3 + 7 × 5 = 33 + 35 = 68 cm². Or take away: 11 × 8 − 4 × 5 = 88 − 20 = 68 cm². (c) Push the steps out: 2 × (11 + 8) = 38 cm.'))
S.append(item(U+'-S02', 'start', 1, 'A 12 cm by 9 cm rectangle has a corner cut off. The corner is shown with a dashed line.',
  fig=POLY([L_([[0, 0], [7, 0], [7, 4], [12, 4], [12, 9], [0, 9]], [{'seg': 4, 'text': '12 cm'}, {'seg': 5, 'text': '9 cm'}, {'seg': 1, 'text': '4 cm', 'in': True}, {'seg': 2, 'text': '5 cm'}], dashed=[[[7, 0], [12, 0]], [[12, 0], [12, 4]]])], cell=24, width_mm=84),
  parts=[P('a', 'Area of the whole rectangle: {b} cm²', A(108)), P('b', 'Area of the corner cut off: {b} cm²', A(20)), P('c', 'Area of the shape left: {b} cm²', A(88))],
  figside=True,
  why='(a) 12 × 9 = 108 cm². (b) The corner is 5 cm by 4 cm: 5 × 4 = 20 cm². (c) 108 − 20 = 88 cm².'))
S.append(item(U+'-S03', 'start', 1, 'Every rectangle here has whole-cm sides and covers 28 cm². Fill in the table. The length is the greater side.',
  fig={'type': 'l4_table', 'head': ['Length', 'Width', 'Perimeter'], 'rows': [['28', '', ''], ['14', '', ''], ['7', '', '']], 'cell_h': 54, 'font': 28, 'width_mm': 100, 'first_col_head': True},
  parts=[P('a', 'Fill in the table.', A(1, 58, 2, 32, 4, 22, text='1 and 58, 2 and 32, 4 and 22')),
         P('b', 'The least perimeter is {b} cm', A(22))],
  figside=True,
  why='28 ÷ 28 = 1, 28 ÷ 14 = 2 and 28 ÷ 7 = 4. The perimeters are 2 × (28 + 1) = 58, 2 × (14 + 2) = 32 and 2 × (7 + 4) = 22. The least is 22 cm, from the shape that is nearest to a square.'))
S.append(item(U+'-S04', 'start', 2, 'Each shape is made of 5 square tiles that are each 1 cm by 1 cm. The tiles touch along whole sides.',
  fig={'type': 'l4_tiles', 'shapes': [{'cells': [[0, 0], [1, 0], [0, 1], [1, 1], [0, 2]], 'name': 'A'}, {'cells': [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]], 'name': 'B'}, {'cells': [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]], 'name': 'C'}], 'cell': 42, 'width_mm': 100},
  parts=[P('a', 'The area of each shape: {b} cm²', A(5)),
         P('b', 'The perimeters of A, B and C: {b} cm, {b} cm, {b} cm', A(10, 12, 12)),
         P('c', 'The shape with the least perimeter is {circ:A|B|C}', A('A'))],
  why='Each shape has 5 tiles, so the area is 5 cm². Count the edges round each shape. A: 10 cm. B: 5 + 5 + 1 + 1 = 12 cm. C: the plus sign has 12 cm. A is the most compact shape, so it has the least perimeter.'))
S.append(item(U+'-S05', 'start', 2, 'The staircase has 4 equal steps. Each step is 3 cm across and 2 cm high.',
  fig=POLY([L_([[0, 8], [12, 8], [12, 6], [9, 6], [9, 4], [6, 4], [6, 2], [3, 2], [3, 0], [0, 0]], [{'seg': 0, 'text': '12 cm'}, {'seg': 9, 'text': '8 cm'}, {'seg': 1, 'text': '2 cm'}, {'seg': 2, 'text': '3 cm'}])], cell=22, width_mm=78),
  parts=[P('a', 'Perimeter: {b} cm', A(40)), P('b', 'Area: {b} cm²', A(60))],
  figside=True,
  why='(a) Push the steps out. The staircase fits in a rectangle that is 12 cm by 8 cm, so the perimeter is 2 × (12 + 8) = 40 cm. (b) The rows are 12, 9, 6 and 3 cm long and each is 2 cm high: 2 × (12 + 9 + 6 + 3) = 2 × 30 = 60 cm².'))
S.append(item(U+'-S06', 'start', 2, 'A photo is 12 cm long and 9 cm wide. It sits in a frame that is 2 cm wide all round.',
  fig=POLY([dict({'pts': [[0, 0], [16, 0], [16, 13], [0, 13]], 'hole': [[2, 2], [14, 2], [14, 11], [2, 11]], 'fill': 'hatch', 'hole_labels': [{'seg': 0, 'text': '12 cm'}, {'seg': 1, 'text': '9 cm'}]})], cell=16, width_mm=70),
  parts=[P('a', 'Photo and frame: {b} cm by {b} cm', A(16, 13, text='16 cm by 13 cm')),
         P('b', 'Area of the frame only: {b} cm²', A(100))],
  figside=True,
  why='(a) The frame adds 2 cm on each side: 12 + 2 + 2 = 16 and 9 + 2 + 2 = 13. (b) The whole is 16 × 13 = 208 cm². The photo is 12 × 9 = 108 cm². The frame is 208 − 108 = 100 cm².'))
S.append(item(U+'-S07', 'start', 3, 'Cut a 10 cm by 3 cm strip on the dashed line. Join the 2 pieces to make a 5 cm by 6 cm rectangle.',
  fig=POLY([L_([[0, 0], [10, 0], [10, 3], [0, 3]], [{'seg': 0, 'text': '10 cm'}, {'seg': 1, 'text': '3 cm'}], dashed=[[[5, 0], [5, 3]]]),
            L_([[0, 0], [5, 0], [5, 6], [0, 6]], [{'seg': 0, 'text': '5 cm'}, {'seg': 1, 'text': '6 cm'}], dashed=[[[0, 3], [5, 3]]], ox=14.5)], cell=20, width_mm=135),
  parts=[P('a', 'The area of the strip is {b} cm² and the area of the rectangle is {b} cm².', A(30, 30)),
         P('b', 'The perimeter of the strip is {b} cm and of the rectangle is {b} cm.', A(26, 22)),
         ],
  why='(a) 10 × 3 = 30 cm² and 5 × 6 = 30 cm². Cutting and moving pieces does not change the area. (b) Strip: 2 × (10 + 3) = 26 cm. Rectangle: 2 × (5 + 6) = 22 cm. The perimeter changed from 26 cm to 22 cm, so moving pieces can change the perimeter.'))
S.append(item(U+'-S08', 'start', 3, 'A rectangle has an area of 72 cm². Its length is 9 cm.',
  parts=[P('a', 'Its width is {b} cm', A(8)), P('b', 'Its perimeter is {b} cm', A(34))],
  why='(a) 72 ÷ 9 = 8 cm. (b) 2 × (9 + 8) = 34 cm.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S09', 'start', 3, 'A hall floor is 12 m long and 8 m wide. It is covered with square tiles that are each 2 m by 2 m.',
  parts=[P('a', 'How many tiles cover the floor? {b} tiles', A(24)), P('b', 'The tiles along the edge are dark. How many tiles are dark? {b} tiles', A(16))],
  why='(a) 12 ÷ 2 = 6 tiles along the length and 8 ÷ 2 = 4 tiles along the width. 6 × 4 = 24 tiles. (b) The tiles not along the edge make a block of 4 by 2 = 8 tiles. 24 − 8 = 16 dark tiles.',
  space={'rows': ['Working:', '']}))

T.append(item(U+'-T01', 'think', 4, 'A square is cut into 2 identical rectangles, as shown. Each rectangle has a perimeter of 30 cm. The area of the square is {b} cm².',
  fig=POLY([L_([[0, 0], [8, 0], [8, 8], [0, 8]], dashed=[[[4, 0], [4, 8]]])], cell=14, width_mm=36, padx=14, pady=14),
  ans=A(100), hint='Each rectangle has 3 sides that equal the side of the square.', figright=True,
  why='Each rectangle is 1 whole side and 1 half side, twice round: 2 × (s + s/2) = 3 × s. So 3 sides of the square make 30 cm, and each side is 10 cm. The area of the square is 10 × 10 = 100 cm².',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T02', 'think', 4, 'Mei has 28 m of fence for a rectangular pen. The sides are whole numbers of metres.',
  parts=[P('a', 'The greatest area when the pen needs 4 fenced sides: {b} m²', A(49)),
         P('b', 'The greatest area when one side is a wall that needs no fence: {b} m²', A(98))],
  hint='For (b), the fence makes 2 short sides and 1 long side.',
  why='(a) The 4 sides use 28 m, so length + width = 14. The greatest area is a 7 m square: 7 × 7 = 49 m². (b) The fence is 2 widths and 1 length: 2w + l = 28. Try w = 7 and l = 14: area 98 m². Try w = 6, l = 16: 96. Try w = 8, l = 12: 96. The greatest is 98 m².',
  space={'rows': ['List:', '', '']}))
T.append(item(U+'-T03', 'think', 4, 'A garden is 12 m long and 9 m wide. Two paths, each 2 m wide, cross it. One path runs along the length and one runs across the width. What is the area of the garden that is NOT path? {b} m²',
  ans=A(70), hint='Slide the paths to the edge. The grass makes 1 rectangle.',
  why='Move the paths to the edges. The grass is then one rectangle that is 12 − 2 = 10 m long and 9 − 2 = 7 m wide: 10 × 7 = 70 m². Check: 108 − 24 − 18 + 4 = 70, because the crossing square is counted twice.',
  space={'rows': ['Working:', '', '']}))

G.append(item(U+'-G01', 'go', 5, 'Three identical squares are joined in an L shape. The perimeter of the L shape is 40 cm. Find its area.\n{b} cm²',
  fig={'type': 'l4_tiles', 'shapes': [{'cells': [[0, 0], [0, 1], [1, 1]]}], 'cell': 36, 'width_mm': 32},
  ans=A(75), hint='Count the sides of squares round the edge of the L shape.',
  figright=True,
  why='The edge of the L shape has 8 sides of squares. 40 ÷ 8 = 5 cm for 1 side. Each square has an area of 5 × 5 = 25 cm², so the L shape has 3 × 25 = 75 cm².',
  ))
G.append(item(U+'-G02', 'go', 5, 'Take a square with sides of 4 cm. Its area is 16 cm² and its perimeter is 16 cm. The numbers match! Find 1 other rectangle with whole-cm sides where they match.\nLength {b} cm   Width {b} cm',
  ans=A(6, 3, text='Length 6 cm, width 3 cm'), hint='Try a width of 1, then 2, then 3. Does the area equal the perimeter?',
  why='Try width 3: length 6 gives an area of 18 cm² and a perimeter of 2 × 9 = 18 cm. For width 1 and width 2, no length works: width 2 gives 2l and 2l + 4. Widths of 4 or more give only the 4 by 4 square. So the other rectangle is 6 cm by 3 cm.',
  space={'rows': ['Try:']}))
G.append(item(U+'-G03', 'go', 5, 'Two strips, each 10 cm by 2 cm, cross in the middle. Together they make a plus shape.',
  fig=POLY([L_([[4, 0], [6, 0], [6, 4], [10, 4], [10, 6], [6, 6], [6, 10], [4, 10], [4, 6], [0, 6], [0, 4], [4, 4]])], cell=14, width_mm=40, padx=14, pady=14),
  parts=[P('a', 'Area of the plus shape: {b} cm²', A(36)), P('b', 'Perimeter of the plus shape: {b} cm', A(40))],
  hint='The middle square is part of both rectangles.',
  figright=True,
  why='(a) 10 × 2 + 10 × 2 = 40, but the 2 cm by 2 cm square in the middle is counted twice: 40 − 4 = 36 cm². (b) Each of the 4 arms is 4 cm long and 2 cm wide. Round one arm the edge is 4 + 2 + 4 = 10 cm, so 4 arms make 40 cm.',
  ))
G.append(item(U+'-G04', 'go', 5, 'A square floor is covered with square tiles. The tiles along the edge are dark and all the others are light.',
  parts=[P('a', 'The floor is 8 tiles by 8 tiles. How many dark tiles? {b}', A(28)),
         P('b', 'A floor has 60 dark tiles. How many tiles long is the floor? {b}', A(16))],
  hint='Take the light block away from the whole floor.',
  why='(a) The light tiles make a 6 by 6 block: 36. The floor has 64 tiles, so 64 − 36 = 28 dark tiles. (b) A floor n tiles long has 4 × n − 4 dark tiles. 4 × n − 4 = 60 gives n = 16. Check: 16 × 16 = 256 and 14 × 14 = 196, and 256 − 196 = 60.',))

C.append(item(U+'-C01', 'quiz', None, 'Find the area of the shape. {b} cm²',
  fig=POLY([L_([[0, 0], [9, 0], [9, 3], [4, 3], [4, 7], [0, 7]], [{'seg': 0, 'text': '9 cm'}, {'seg': 1, 'text': '3 cm'}, {'seg': 4, 'text': '4 cm'}, {'seg': 5, 'text': '7 cm'}])], cell=18, width_mm=47, pady=50),
  ans=A(43), figright=True,
  why='Split into 9 × 3 = 27 and 4 × 4 = 16: 27 + 16 = 43 cm². Or 9 × 7 − 5 × 4 = 63 − 20 = 43 cm².'))
C.append(item(U+'-C02', 'quiz', None, 'A rectangle has an area of 60 cm² and a length of 12 cm. Find its perimeter. {b} cm',
  ans=A(34), why='The width is 60 ÷ 12 = 5 cm. The perimeter is 2 × (12 + 5) = 34 cm.'))
C.append(item(U+'-C03', 'quiz', None, 'A 10 cm by 7 cm photo has a frame 1 cm wide on every side. Find the area of the frame alone. {b} cm²',
  ans=A(38), why='The whole is 12 cm by 9 cm = 108 cm². The photo is 10 × 7 = 70 cm². 108 − 70 = 38 cm².'))
C.append(item(U+'-C04', 'quiz', None, 'Every rectangle has whole-cm sides and covers 24 cm². Find the least perimeter any of them can have. {b} cm',
  ans=A(20), why='The pairs are 1 × 24, 2 × 12, 3 × 8 and 4 × 6, with perimeters 50, 28, 22 and 20. The least is 20 cm, from 4 cm by 6 cm.'))

unit = {'schema_version': 1, 'level': 4, 'unit': 7, 'id': U, 'title': 'Area Architects II', 'topic': 'Area and perimeter', 'holiday_lesson': 7,
        'goal': 'I can find the area and the perimeter of shapes with square corners. I can compare rectangles with the same area.',
        'learn': learn, 'items': S + T + G + C}
write(7, unit)
