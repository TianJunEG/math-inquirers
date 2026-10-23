import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

def stacks(*sts, **kw):
    d = {'type': 'l2_cubes', 'stacks': [{'label': l, 'heights': h} for l, h in sts]}
    d.update(kw)
    return d

SEMI, QUA, SQ, TRI = 'semicircle', 'quarter', 'square', 'triangle'

learn = {
 'intro': 'Shapes can be put together and taken apart. A half circle has 1 straight side. A quarter circle has 2 straight sides. To count shapes, work in order and count one kind at a time.',
 'example': {
  'problem': 'How many squares of all sizes are in this grid? It is 2 squares long and 2 squares high.',
  'figure': {'type': 'l2_grid', 'values': [['', ''], ['', '']], 'cell': 80, 'width_mm': 40}, 'side': True,
  'steps': ['Count the small squares first: 4.', 'Look for bigger squares. One square is 2 by 2: the whole grid. That is 1.', 'Add: 4 + 1 = 5 squares.'],
  'answer': '5 squares in all.'},
 'howto': {'title': 'How to count shapes', 'steps': ['Count the smallest shapes first.', 'Then count the next size up.', 'Keep going to the biggest.', 'Add the counts.']},
 'facts': {'title': 'Solids', 'lines': ['Cube: 6 flat square faces.', 'Cylinder: 2 flat circles and 1 curved face.', 'Cubes in a stack: count layer by layer.']},
 'try': {'text': 'How many squares of all sizes are in a grid 2 squares high and 3 squares long? {b}', 'answer': A('8'),
         'explanation': 'Small squares: 2 rows of 3 is 6. Squares 2 by 2: 2 of them. 6 + 2 = 8 squares. There is no 3 by 3 square because the grid is only 2 high.'}}

items = [
 I('start', 1, 'Look at the solids. How many flat faces does each solid have?', figure={'type': 'l2_solids', 'items': [{'kind': k, 'label': l} for k, l in (('cube', 'cube'), ('cylinder', 'cylinder'), ('cone', 'cone'), ('sphere', 'sphere'))], 'width_mm': 120},
   partsrow=True, parts=[P('a', 'Cube: {b}', '6'), P('b', 'Cylinder: {b}', '2'), P('c', 'Cone: {b}', '1'), P('d', 'Sphere: {b}', '0')],
   why='A cube has 6 flat square faces. A cylinder has 2 flat faces (circles) and 1 curved face. A cone has 1 flat face (a circle) and 1 curved face. A sphere has no flat face: it is all curved.'),
 I('start', 1, 'Count each kind of piece.', figure={'type': 'l2_pieces', 'items': [SEMI, QUA, SQ, TRI, QUA, SEMI, TRI, SQ, QUA, TRI, SEMI, QUA], 'per_row': 6, 'width_mm': 125},
   partsrow=True, parts=[P('a', 'Half circles: {b}', '3'), P('b', 'Quarter circles: {b}', '4'), P('c', 'Squares: {b}', '2'), P('d', 'Triangles: {b}', '3')],
   why='Go through the pieces one kind at a time. Half circles: 3. Quarter circles: 4. Squares: 2. Triangles: 3. Check: 3 + 4 + 2 + 3 = 12 pieces.'),
 I('start', 1, 'All the circles are the same size.', partsrow=True, parts=[
   P('a', '{b} quarter circles make 1 half circle.', '2'), P('b', '3 half circles make {b} quarter circles.', '6'), P('c', '12 quarter circles make {b} whole circles.', '3')],
   why='(a) 2 quarters make a half. (b) Each half is 2 quarters, so 3 halves are 6 quarters. (c) 4 quarters make 1 circle, so 12 quarters make 3 circles.'),
 I('start', 2, 'Count every square of every size in this grid. Start with the smallest.', figure={'type': 'l2_grid', 'values': [['', '', ''], ['', '', ''], ['', '', '']], 'cell': 70, 'width_mm': 44}, figside=True,
   parts=[P('a', '1 by 1 squares: {b}', '9'), P('b', '2 by 2 squares: {b}', '4'), P('c', '3 by 3 squares: {b}', '1'), P('d', 'All the squares: {b}', '14')],
   why='1 by 1 squares: 3 rows of 3 is 9. 2 by 2 squares: they can start in 2 places across and 2 places down, so 4. 3 by 3 square: the whole grid, 1. Total: 9 + 4 + 1 = 14.'),
 I('start', 2, 'Count the cubes in each stack. Every cube sits on the table or on another cube. Stack A is 1 cube deep. Stacks B and C are 2 cubes deep. At the back they are just like at the front.',
   figure=stacks(('A', [[3, 2, 1]]), ('B', [[2, 1], [2, 1]]), ('C', [[2, 2, 1], [2, 2, 1]]), width_mm=150),
   partsrow=True, parts=[P('a', 'A: {b} cubes', '6'), P('b', 'B: {b} cubes', '6'), P('c', 'C: {b} cubes', '10')],
   why='A: 3 + 2 + 1 = 6. B has 2 rows, and each row has 2 + 1 = 3 cubes, so 2 × 3 = 6. C has 2 rows of 2 + 2 + 1 = 5 cubes, so 2 × 5 = 10.'),
 I('start', 2, 'Count the triangles of all sizes. Start with the smallest.', figure={'type': 'l2_trilines', 'apex': 2, 'across': 0, 'width_mm': 62}, figside=True,
   parts=[P('a', 'Small triangles: {b}', '3'), P('b', 'Triangles made of 2 small ones: {b}', '2'), P('c', 'The whole triangle: {b}', '1'), P('d', 'All the triangles: {b}', '6')],
   why='The 2 lines from the top cut the triangle into 3 small triangles. 2 small ones next to each other make a bigger triangle: there are 2 such pairs. The whole triangle is 1 more. 3 + 2 + 1 = 6.'),
 I('start', 3, 'Which solid am I? Circle it.', partsrow=True, parts=[
   P('a', 'I have 6 square faces.   {circ:cube|cone|sphere}', 'cube'), P('b', 'I have 1 flat circle and 1 curved face.   {circ:cone|cylinder|cube}', 'cone'),
   P('c', 'I roll and have no flat face.   {circ:sphere|cube|cylinder}', 'sphere'), P('d', 'I have 2 flat circles.   {circ:cone|cylinder|sphere}', 'cylinder')],
   why='(a) Only a cube has 6 square faces. (b) A cone has one flat circle (its base) and one curved face. (c) A sphere is curved all over. (d) A cylinder has 2 flat circles, one at each end.'),
 I('start', 3, 'Put the pieces together. Circle the shape you make.', partsrow=True, parts=[
   P('a', '2 half circles make a   {circ:circle|square|triangle}', 'circle'), P('b', '2 same squares make a   {circ:rectangle|circle|triangle}', 'rectangle'),
   P('c', '4 quarter circles make a   {circ:circle|half circle|square}', 'circle')],
   why='(a) 2 half circles make 1 whole circle. (b) 2 same squares joined side by side make a longer shape with 4 square corners: a rectangle. (c) 4 quarter circles make a whole circle.'),
 I('start', 3, 'Ali builds a stack of cubes. The bottom layer is 5 cubes long and 2 cubes wide. The stack has 3 layers that are all the same.',
   figure=stacks((None, [[3] * 5, [3] * 5]), width_mm=72), figside=True,
   parts=[P('a', 'Each layer has {b} cubes.', '10'), P('b', 'The stack has {b} cubes.', '30')],
   why='(a) A layer is 2 rows of 5: 5 + 5 = 10 cubes. (b) 3 layers of 10 cubes: 10 + 10 + 10 = 30 cubes.'),
 I('start', 3, 'Name the flat faces.', partsrow=True, parts=[
   P('a', 'Each face of a cube is a   {circ:square|circle|triangle}', 'square'), P('b', 'Each flat face of a cylinder is a   {circ:circle|square|triangle}', 'circle'),
   P('c', 'The flat face of a cone is a   {circ:triangle|circle|square}', 'circle')],
   why='(a) A cube has 6 faces and each one is a square. (b) The 2 flat faces of a cylinder are circles. (c) The flat face of a cone is its base, a circle.'),
 # Think harder
 I('think', 4, 'Beyond: a net folds up into a solid. Which nets fold up into a cube? Each square must land on a NEW face.', beyond='Cube nets',
   figure={'type': 'l2_nets', 'nets': [{'label': 'A', 'cells': [[1, 0], [1, 1], [1, 2], [1, 3], [0, 1], [2, 1]]}, {'label': 'B', 'cells': [[0, 0], [0, 1], [1, 1], [1, 2], [2, 2], [2, 3]]},
                                       {'label': 'C', 'cells': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 2]]}, {'label': 'D', 'cells': [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]}], 'width_mm': 150},
   partsrow=True, parts=[P('a', 'A   {circ:Yes|No}', 'Yes'), P('b', 'B   {circ:Yes|No}', 'Yes'), P('c', 'C   {circ:Yes|No}', 'No'), P('d', 'D   {circ:Yes|No}', 'No')],
   hint='Squares in a straight line of 5 do not fold into 6 faces.',
   why='A is a cross: a row of 4 squares folds into the 4 sides, one square is the top and one is the bottom. B is a staircase of 3 pairs and folds into a cube. C has a row of 5 squares: the 5th square would land on the same face as the 1st, so it does not fold. D has a 2 by 2 block of squares: those 4 squares cannot all be different faces, so it does not fold.'),
 I('think', 4, 'Count the rectangles in a row of 4 squares. A square is a rectangle too.', figure={'type': 'l2_grid', 'values': [['', '', '', '']], 'cell': 76, 'width_mm': 66},
   partsrow=True, parts=[P('a', '1 square long: {b}', '4'), P('b', '2 squares long: {b}', '3'), P('c', '3 squares long: {b}', '2'), P('d', '4 squares long: {b}   All: {b}', ['1', '10'], '1 and 10 in all')],
   hint='A rectangle 2 squares long can start in 3 places.',
   why='1 square long: 4. 2 squares long: they start at square 1, 2 or 3, so 3. 3 squares long: they start at square 1 or 2, so 2. 4 squares long: 1. Total: 4 + 3 + 2 + 1 = 10.'),
 I('think', 4, 'A triangle is cut by 2 lines from the top corner to the bottom and 1 line across the middle.', figure={'type': 'l2_trilines', 'apex': 2, 'across': 1, 'width_mm': 56}, figside=True,
   partsrow=False, parts=[P('a', 'Triangles with their bottom on the base: {b}', '6'), P('b', 'Triangles with their bottom on the line across: {b}', '6'), P('c', 'All the triangles: {b}', '12')],
   hint='Count the triangles that sit on each line separately.',
   why='The 2 lines from the top and the 2 sloping sides make 4 lines from the top. Choosing 2 of them gives 6 triangles on each line that runs across: 3 small ones, 2 made of 2 parts and 1 made of 3 parts. There are 2 lines across (the base and the middle line): 6 + 6 = 12 triangles.'),
 # Go further
 I('go', 5, 'Beyond: a pyramid of cubes has 5 layers. The top layer is 1 by 1, then 2 by 2, then 3 by 3, then 4 by 4. The bottom layer is 5 by 5.', beyond='Square numbers in a pyramid', parts=[
   P('a', 'The bottom layer has {b} cubes.', '25'), P('b', 'The pyramid has {b} cubes.', '55')],
   hint='Add the layers: 1 + 4 + 9 ...',
   why='(a) 5 by 5 = 25 cubes. (b) 1 + 4 + 9 + 16 + 25 = 55 cubes.'),
 I('go', 5, 'A big cube is built from small cubes: 4 long, 4 wide and 4 high. All the outside is painted. Sort the small cubes by how many faces are painted.', partsrow=True, parts=[
   P('a', '3 faces painted: {b}', '8'), P('b', '2 faces painted: {b}', '24'), P('c', '1 face painted: {b}', '24'), P('d', 'No paint: {b}', '8')],
   hint='Corners, edges, faces, inside. Check they make 64.',
   why='3 faces: the 8 corners. 2 faces: each of the 12 edges has 2 cubes between the corners, so 24. 1 face: each of the 6 faces has a 2 by 2 middle, so 6 × 4 = 24. No paint: the middle block is 2 by 2 by 2, so 8. Check: 8 + 24 + 24 + 8 = 64 = 4 × 4 × 4.'),
 I('go', 5, 'Design a stack with exactly 24 cubes. Write the cubes in each layer. Many answers are right.', value='open',
   atext='Open. Examples: 4 long, 3 wide and 2 high is 12 + 12 = 24. Or layers of 12, 8 and 4 cubes: 12 + 8 + 4 = 24.', space={'rows': ['Stack 1:']},
   hint='A layer must sit on a layer at least as big.',
   why='Example 1: 4 by 3 by 2: each layer has 12 cubes and there are 2 layers: 24. Example 2: a layer of 4 by 3 (12), a layer of 4 by 2 (8) and a layer of 2 by 2 (4): 12 + 8 + 4 = 24.'),
 I('go', 5, 'How many rectangles of all sizes are in a grid 2 squares high and 3 squares long? A square is a rectangle too. {b}', figure={'type': 'l2_grid', 'values': [['', '', ''], ['', '', '']], 'cell': 66, 'width_mm': 50}, figside=True, value='18',
   hint='Sort them by size: 1 by 1, 1 by 2, 1 by 3, 2 by 1, 2 by 2, 2 by 3.',
   why='1 by 1: 6. 1 high and 2 long: 4. 1 high and 3 long: 2. 2 high and 1 long: 3. 2 high and 2 long: 2. 2 high and 3 long: 1. Total: 6 + 4 + 2 + 3 + 2 + 1 = 18.'),
 # Check yourself
 I('quiz', 0, 'Which solid has 1 flat face and 1 curved face?   {circ:cube|cone|cylinder}', value='cone', why='A cone has a flat circle for its base and one curved face. A cylinder has 2 flat faces.'),
 I('quiz', 0, 'All the circles are the same size. 3 half circles make {b} quarter circles.', value='6', why='1 half circle is 2 quarter circles. 3 half circles make 3 × 2 = 6 quarter circles.'),
 I('quiz', 0, 'A stack is 4 cubes long, 3 cubes wide and 2 cubes high. How many cubes? {b}', value='24', why='One layer is 4 × 3 = 12 cubes. There are 2 layers: 12 + 12 = 24.'),
 I('quiz', 0, 'How many squares of all sizes are in a grid 2 high and 3 long? {b}', value='8', why='Small squares: 6. Squares 2 by 2: 2. Total: 6 + 2 = 8.'),
]
build(8, 'Shape builders', '2D and 3D shapes', 'I can name half circles and quarter circles. I can count shapes and cubes in order. I can use layers to count a stack.', learn, items, snug=['start1', 'start2', 'start3'])
