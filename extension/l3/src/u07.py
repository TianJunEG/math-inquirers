from lib import *

u = Unit(7, 'Area architects', 'Area and perimeter',
         'I can find the area and the perimeter of rectangles and of shapes made of squares.')


def rect(l, w, wm=60, **kw):
    d = {'type': 'l3_poly', 'pts': [[0, 0], [l, 0], [l, w], [0, w]], 'labels': [{'side': 0, 'text': f'{l} cm'}, {'side': 1, 'text': f'{w} cm'}], 'width_mm': wm}
    d.update(kw)
    return d


u.learn(
    'Area is the flat space inside a shape. We count squares and write cm². Perimeter is the distance all the way round the edge, in cm.',
    {'problem': 'The figure is made of squares that are 1 cm by 1 cm. Find its area and its perimeter.',
     'figure': {'type': 'l3_cells', 'rows': ['XXXXX', 'XX...'], 'width_mm': 62, 'cell': 52}, 'side': True,
     'steps': ['Area: count the squares. 5 + 2 = 7, so the area is 7 cm².',
               'Perimeter: add the sides all the way round. 5 + 1 + 3 + 1 + 2 + 2 = 14 cm.',
               'Check: the figure fits in a box 5 cm by 2 cm. 2 × (5 + 2) = 14 cm.'],
     'answer': 'Area 7 cm². Perimeter 14 cm.'},
    {'title': 'How to find area and perimeter',
     'steps': ['Area: count the squares, or length × width.', 'Perimeter: add all the sides.',
               'Rectangle: perimeter = 2 × (length + width).']},
    {'text': 'A rectangle is 8 cm long and 3 cm wide.', 'figure': rect(8, 3, 58), 'figright': True,
     'answer': None, 'explanation': ''})
tr = u.u['learn']['try']
tr.pop('answer'); tr.pop('text')
u.u['learn']['try'] = {'id': 'L3U07-L01', 'text': 'A rectangle is 8 cm long and 3 cm wide.\nIts area is {b} cm². Its perimeter is {b} cm.', 'figure': rect(8, 3, 58),
                       'answer': A(['24', '22'], 'Area 24 cm². Perimeter 22 cm.', list=True),
                       'explanation': 'Area: 8 × 3 = 24 cm². Perimeter: 8 + 3 + 8 + 3 = 22 cm, or 2 × (8 + 3) = 22 cm.'}
u.u['learn']['tight'] = True

# ---------------- Start here (pages 1 to 3)
u.S(1, 'Each small square is 1 cm by 1 cm. Find the area and the perimeter of each figure.', parts=[
    P('a', 'A: area {b} cm², perimeter {b} cm', A(['8', '12'], 'A: 8 cm², 12 cm', list=True)),
    P('b', 'B: area {b} cm², perimeter {b} cm', A(['6', '14'], 'B: 6 cm², 14 cm', list=True)),
    P('c', 'C: area {b} cm², perimeter {b} cm', A(['6', '10'], 'C: 6 cm², 10 cm', list=True)),
    P('d', 'The 2 figures with the same area but different perimeters are   {circ:A and B|A and C|B and C}', A('B and C'))],
    figure={'type': 'l3_cells', 'shapes': [{'rows': ['XXXX', 'XXXX'], 'label': 'A'}, {'rows': ['XXXX', 'X..X'], 'label': 'B'}, {'rows': ['XXX', 'XXX'], 'label': 'C'}], 'width_mm': 134},
    why='Area is the number of squares: A has 8, B has 4 + 2 = 6 and C has 6. Perimeter is the length of the edge: A is 2 × (4 + 2) = 12. B: the box round it is 4 by 2, with a perimeter of 12. The dent in the bottom adds a wall of 1 cm on each side: 12 + 2 = 14. C is 2 × (3 + 2) = 10. B and C have the same area, 6, but different perimeters.')
u.S(1, 'Find the area and the perimeter of each rectangle.', parts=[
    P('a', '8 cm long and 6 cm wide: area {b} cm², perimeter {b} cm', A(['48', '28'], 'Area 48 cm², perimeter 28 cm', list=True)),
    P('b', '11 m long and 4 m wide: area {b} m², perimeter {b} m', A(['44', '30'], 'Area 44 m², perimeter 30 m', list=True))],
    why='(a) Area 8 × 6 = 48. Perimeter 2 × (8 + 6) = 28. (b) Area 11 × 4 = 44. Perimeter 2 × (11 + 4) = 30.')
u.S(1, 'Look at squares.', parts=[
    P('a', 'A square has sides of 7 cm. Its perimeter is {b} cm.', A('28')), P('b', 'Its area is {b} cm².', A('49')),
    P('c', 'A square has a perimeter of 36 cm. Each side is {b} cm.', A('9'))],
    why='(a) 4 × 7 = 28. (b) 7 × 7 = 49. (c) The 4 sides are equal, so each is 36 ÷ 4 = 9 cm.')
u.S(1, 'A rectangle has a perimeter of 30 cm. Its length is 9 cm.', parts=[
    P('a', 'Its width is {b} cm.', A('6')), P('b', 'Its area is {b} cm².', A('54'))],
    why='Length + width is half of the perimeter: 30 ÷ 2 = 15. So the width is 15 - 9 = 6 cm. The area is 9 × 6 = 54 cm².')

u.S(2, 'A mat is 15 cm long and 9 cm wide. Square tiles with sides of 3 cm cover it exactly.', parts=[
    P('a', '{b} tiles fit along the length.', A('5')), P('b', '{b} tiles fit along the width.', A('3')),
    P('c', 'The mat needs {b} tiles in all.', A('15'))],
    why='(a) 15 ÷ 3 = 5. (b) 9 ÷ 3 = 3. (c) 5 rows of 3 tiles make 5 × 3 = 15 tiles.')
u.S(2, 'Mei has 14 cm of wire. She bends all of it into a rectangle. Each side is a whole number of cm. List ALL the rectangles.', parts=[
    P('a', 'There are {b} different rectangles.', A('3')), P('b', 'The one with the greatest area has an area of {b} cm².', A('12'))],
    space={'table': {'cols': ['length', 'width', 'area'], 'rows': 4}},
    why='Length + width = 14 ÷ 2 = 7. The pairs are 6 and 1 (area 6), 5 and 2 (area 10), 4 and 3 (area 12). That is 3 rectangles. The one closest to a square, 4 by 3, has the greatest area: 12 cm².')
u.S(2, 'Find the 2 missing sides a and b. Then find the area and the perimeter of the figure.', parts=[
    P('a', 'a = {b} cm', A('4')), P('b', 'b = {b} cm', A('3')),
    P('c', 'The area is {b} cm².', A('36')), P('d', 'The perimeter is {b} cm.', A('28'))],
    partsrow=True,
    figure={'type': 'l3_poly', 'pts': [[0, 0], [8, 0], [8, 3], [4, 3], [4, 6], [0, 6]], 'k': 34, 'width_mm': 96,
            'labels': [{'side': 0, 'text': '8 cm'}, {'side': 1, 'text': '3 cm'}, {'side': 2, 'text': 'a'}, {'side': 3, 'text': 'b'}, {'side': 4, 'text': '4 cm'}, {'side': 5, 'text': '6 cm'}]},
    why='a is the top of the lower part: 8 - 4 = 4 cm. b is the rest of the left height: 6 - 3 = 3 cm. Area: cut into a 4 by 6 rectangle and a 4 by 3 rectangle: 24 + 12 = 36 cm². Perimeter: push the steps out to a box 8 by 6: 2 × (8 + 6) = 28 cm.')
u.S(2, 'Each small square is 1 cm by 1 cm.', parts=[
    P('a', 'The area is {b} cm².', A('12')), P('b', 'The perimeter is {b} cm.', A('18')),
    P('c', 'Ben fills the gaps to make a 6 by 3 rectangle. He adds {b} squares.', A('6')),
    P('d', 'The perimeter of the rectangle is {b} cm.', A('18'))],
    figure={'type': 'l3_cells', 'rows': ['XXXXXX', 'XXXX..', 'XX....'], 'width_mm': 74, 'cell': 52},
    why='(a) 6 + 4 + 2 = 12 cm². (b) The staircase has the same perimeter as its box, 6 by 3: 2 × (6 + 3) = 18 cm. (c) The rectangle has 6 × 3 = 18 squares, so he adds 18 - 12 = 6. (d) 18 cm: filling the steps does not change the perimeter.')

u.S(3, 'Siti has a rectangular garden, 9 m long and 5 m wide. A fence goes all round it. She covers the garden with grass.', parts=[
    P('a', 'The fence is {b} m long.', A('28')), P('b', 'The grass covers {b} m².', A('45'))],
    why='(a) The fence is the perimeter: 2 × (9 + 5) = 28 m. (b) The grass covers the area: 9 × 5 = 45 m².')
u.S(3, 'Mei draws a rectangle 10 cm long and 2 cm wide. Ben draws a square with the same perimeter.', parts=[
    P('a', 'Each side of Ben’s square is {b} cm.', A('6')), P('b', 'Whose shape has the greater area?   {circ:Mei’s|Ben’s}', A('Ben’s')),
    P('c', 'It is greater by {b} cm².', A('16'))],
    why='(a) Mei’s perimeter is 2 × (10 + 2) = 24 cm, so Ben’s side is 24 ÷ 4 = 6 cm. (b) Ben’s area is 6 × 6 = 36 cm² and Mei’s area is 10 × 2 = 20 cm². (c) 36 - 20 = 16 cm².')
u.S(3, 'The figure of 4 squares has a perimeter of 10 cm. Ali adds ONE more square to it, in the place A, B or C.', parts=[
    P('a', 'Which places make the perimeter 12 cm?   {circ:A|B|C}', A(['A', 'B'], 'A and B', list=True)),
    P('b', 'Which place keeps the perimeter 10 cm?   {circ:A|B|C}', A('C'))],
    figure={'type': 'l3_cells', 'rows': ['.XXXA', '.CX..', '..B..'], 'width_mm': 60, 'cell': 52}, figside=True,
    why='A square that touches the figure along only 1 side adds 2 to the perimeter. A and B each touch 1 side, so the perimeter becomes 12 cm. C fits into the corner and touches 2 sides: it hides 2 cm of the old edge and adds 2 cm, so the perimeter stays 10 cm.')
u.S(3, 'Both shapes are made of 8 squares. Each square is 1 cm by 1 cm.', parts=[
    P('a', 'The row has a perimeter of {b} cm.', A('18')), P('b', 'The 2 by 4 rectangle has a perimeter of {b} cm.', A('12')),
    P('c', 'The shape with the smaller perimeter is the   {circ:row|2 by 4 rectangle}', A('2 by 4 rectangle'))],
    figure={'type': 'l3_cells', 'shapes': [{'rows': ['XXXXXXXX'], 'label': 'row', 'cell': 40}, {'rows': ['XXXX', 'XXXX'], 'label': '2 by 4', 'cell': 40}], 'cell': 40, 'width_mm': 120},
    why='(a) The row is 8 cm long and 1 cm wide: 2 × (8 + 1) = 18 cm. (b) 2 × (4 + 2) = 12 cm. (c) Both have area 8 cm², but the shape that is nearer to a square has the smaller perimeter.')
u.S(3, 'A square room has a floor area of 64 m².', parts=[
    P('a', 'Each side of the room is {b} m long.', A('8')), P('b', 'A border goes all round the floor. It is {b} m long.', A('32'))],
    why='(a) 8 × 8 = 64, so each side is 8 m. (b) The border is the perimeter: 4 × 8 = 32 m.')

# ---------------- Think harder
u.T('A square has sides of 8 cm. One straight cut makes it into 2 equal rectangles.', parts=[
    P('a', 'Each rectangle has a perimeter of {b} cm.', A('24')), P('b', 'The 2 rectangles together have a perimeter of {b} cm.', A('48')),
    P('c', 'That is {b} cm more than the perimeter of the square.', A('16'))],
    hint='Each rectangle is 8 cm by 4 cm. Draw it.',
    space={'rows': ['Draw the cut:']},
    why='Each rectangle is 8 cm by 4 cm, so its perimeter is 2 × (8 + 4) = 24 cm. Together: 48 cm. The square’s perimeter is 32 cm, and 48 - 32 = 16. The cut is 8 cm long and it appears on both pieces, so it adds 2 × 8 = 16 cm.')
u.T('A rectangle has an area of 36 cm² and a perimeter of 26 cm.', parts=[
    P('a', 'Its length is {b} cm.', A('9')), P('b', 'Its width is {b} cm.', A('4'))],
    hint='List pairs that multiply to 36. Then add each pair.',
    space={'rows': ['Pairs that multiply to 36:', '']},
    why='Length + width is 26 ÷ 2 = 13. The pairs that multiply to 36 are 1 and 36, 2 and 18, 3 and 12, 4 and 9, 6 and 6. The pair that adds up to 13 is 4 and 9. Check: area 9 × 4 = 36 and perimeter 2 × 13 = 26.')
u.T('A rectangle is 9 m long and 6 m wide. A rectangle 3 m by 2 m is cut out of one corner, as shown.', parts=[
    P('a', 'The area that is left is {b} m².', A('48')), P('b', 'The perimeter of the figure is {b} m.', A('30')),
    P('c', 'The same 3 m by 2 m piece is cut from the MIDDLE of a long side. The perimeter is then {b} m.', A('34'))],
    figure={'type': 'l3_poly', 'pts': [[0, 0], [9, 0], [9, 4], [6, 4], [6, 6], [0, 6]], 'k': 30, 'width_mm': 78,
            'labels': [{'side': 0, 'text': '9 m'}, {'side': 5, 'text': '6 m'}]}, figside=True,
    hint='Push the corner out. Then think about a notch in the middle.',
    why='(a) 9 × 6 = 54, and 54 - 6 = 48 m². (b) Cutting a corner does not change the perimeter: 2 × (9 + 6) = 30 m. (c) A notch in the middle of a side takes away 3 m of edge and adds 3 + 2 + 2 = 7 m of new edge, so the perimeter grows by 4: 34 m.')

# ---------------- Go further
u.G('Beyond Level 3: Perimeter patterns.\nSquares with sides of 1 cm are joined in a row. 1 square has a perimeter of 4 cm. 2 squares have 6 cm. 3 squares have 8 cm.', parts=[
    P('a', 'A row of 10 squares has a perimeter of {b} cm.', A('22')), P('b', 'A row with a perimeter of 30 cm has {b} squares.', A('14'))],
    hint='The perimeter goes up by 2 cm for each new square.',
    space={'rows': ['My pattern:']},
    why='Each new square adds 2 cm (1 cm on top and 1 cm below). The perimeter is 4 + 2 for every extra square. For 10 squares: 4 + 9 × 2 = 22 cm. For 30 cm: (30 - 4) ÷ 2 = 13 extra squares, so 14 squares.')
u.G('3 equal squares are joined in a row to make a rectangle. Its perimeter is 40 cm.', parts=[
    P('a', 'Each square has sides of {b} cm.', A('5')), P('b', 'The rectangle has an area of {b} cm².', A('75'))],
    hint='The rectangle is 3 sides of a square long and 1 side wide.',
    space={'rows': ['Draw it:']},
    why='The rectangle is 3 square sides long and 1 side wide, so its perimeter is 3 + 1 + 3 + 1 = 8 sides. 40 ÷ 8 = 5 cm. The area is 3 squares of 5 × 5 = 25 cm², so 75 cm².')
u.G('Beyond Level 3: A path round a pond.\nA pond is 6 m long and 4 m wide. A path 1 m wide goes all round the pond.', parts=[
    P('a', 'The pond and the path together make a rectangle {b} m by {b} m.', A(['8', '6'], '8 m by 6 m', list=True)),
    P('b', 'The area of the path is {b} m².', A('24'))],
    figure={'type': 'l3_poly', 'pts': [[0, 0], [8, 0], [8, 6], [0, 6]], 'extra': [{'pts': [[1, 1], [7, 1], [7, 5], [1, 5]]}], 'texts': [{'x': 4, 'y': 3, 'text': 'pond 6 m by 4 m'}],
            'labels': [{'side': 0, 'text': 'path 1 m wide'}], 'k': 26, 'width_mm': 78}, figside=True,
    hint='Find the area of the whole rectangle. Take away the pond.',
    why='The path adds 1 m on each side, so both lengths grow by 2 m: 6 + 2 = 8 and 4 + 2 = 6. The whole rectangle has an area of 8 × 6 = 48 m². The pond has 6 × 4 = 24 m². The path is 48 - 24 = 24 m².')
u.G('Beyond Level 3: The largest square tile.\nA floor is 12 m long and 10 m wide. It is covered exactly with square tiles of one size. The side of a tile is a whole number of metres.', parts=[
    P('a', 'The largest tile has sides of {b} m.', A('2')), P('b', 'The floor needs {b} of these tiles.', A('30'))],
    hint='The tile side must fit exactly in 12 and in 10.',
    space={'rows': ['My list:']},
    why='The side must divide both 12 and 10 exactly. 1 and 2 do. 3 does not divide 10, 4 does not, 5 does not divide 12, and 6 does not divide 10. So the largest side is 2 m. There are 6 tiles along and 5 tiles across: 30 tiles.')

# ---------------- Check yourself
u.C('A rectangle is 9 cm long and 5 cm wide. Its area is {b} cm².', A('45'), why='9 × 5 = 45 cm².')
u.C('A square has sides of 6 cm. Its perimeter is {b} cm.', A('24'), why='4 × 6 = 24 cm.')
u.C('Each small square is 1 cm by 1 cm. The area is {b} cm². The perimeter is {b} cm.', A(['7', '12'], 'Area 7 cm². Perimeter 12 cm.', list=True),
    figure={'type': 'l3_cells', 'rows': ['XXX', 'XX.', 'XX.'], 'width_mm': 48, 'cell': 52}, figright=True,
    why='Area: 3 + 2 + 2 = 7 cm². Perimeter: the figure fits in a 3 by 3 box and has no dents on the outside, so 2 × (3 + 3) = 12 cm.')
u.C('A rectangle has a perimeter of 22 cm. Its width is 4 cm. Its length is {b} cm.', A('7'),
    why='Length + width is 22 ÷ 2 = 11. The length is 11 - 4 = 7 cm.')
u.save()
