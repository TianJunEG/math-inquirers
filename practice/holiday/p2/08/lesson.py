"""Level 2 (P2) holiday lesson 8: SHAPE BUILDERS (2D and 3D shapes), week 4, second lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l8.js `workbook()` = Start here, p2/gaps.json lesson 8 `invest` = Investigation,
p2/content/l8.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by p2/workbook_html.js, and the
"Make up your own" line).  Every answer is recomputed by an INDEPENDENT checker: the pieces of the robot are counted from the drawing (3 points, a rectangle, the chord of an arc),
squares and rectangles by trying every size and corner, the triangles of the figure from its marked points and drawn lines, the cubes of a stack one at a time, the nets by
ROLLING A CUBE over them, the painted cubes by looking at every small cube, the shapes of squares by growing them one square at a time.  build_holiday.py stops if a checker
and the printed answer differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401
from p2lib_w4 import *      # noqa: E402,F401

STRAND = '2D and 3D shapes'
META = dict(level=2, lesson=8, key='p2', title='Shape builders', workbook_title='SHAPE BUILDERS', topic='2D and 3D Shapes', strand=STRAND,
            sources=['p2/content/l8.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['Count in order, one kind or one size at a time, so you do not miss one or count one twice. Cubes do not float: a cube on top sits on a cube underneath.',
                   'A net is a flat shape of 6 squares. If you have the cut-out nets, you can fold them. If not, picture rolling a cube over the net. Some questions ask you to draw on paper: do that first, then compare with the picture shown after you submit.'])

ROBOT = robot_fig()
GRIDS = printed_fig('a: a grid 4 squares long')
STACKS_FIG = printed_fig('Three stacks of cubes')
NETS_AD = printed_fig('4 shapes made of 6 squares')
NETS_EF = printed_fig('2 shapes made of 6 squares')
T1_FIG = printed_fig('Three layers of cubes seen from above')
C5_FIG = printed_fig('Four layers seen from above')
GRID22 = grid_plain(2, 2)
GRID55 = grid_plain(5, 5)
LINE6 = grid_plain(6, 1, 40)
PLACES = net_places_fig()
PLACES_SOL = net_places_fig(True)
KINDS = robot_kinds(ROBOT)


def layer_cubes(layers):
    """Cubes in layers of (long, deep), counted one cube at a time."""
    n = 0
    for cols, rows in layers:
        for _ in range(cols):
            for _ in range(rows):
                n += 1
    return n


def whole_circles(halves, quarters):
    """Whole circles from halves and quarters: turn everything into quarters (a half is 2 quarters), then make groups of 4."""
    q = quarters
    for _ in range(halves):
        q += 2
    g = 0
    while q >= 4:
        q -= 4
        g += 1
    return g


ITEMS = [
    # ================= Start here (workbook lesson 8, No.1 to No.4)
    dict(id='1', tier='core', no='1', label='1', type='fields', skill='naming and counting 2D pieces', svg=ROBOT, answer=[2, 3, 4, 2],
         q='The robot is made of pieces. Count each kind of piece and type how many.',
         frame='Squares {f1}   Triangles {f2}   Half circles {f3}   Quarter circles {f4}',
         check=lambda: [KINDS['square'], KINDS['triangle'], KINDS['half'], KINDS['quarter']],
         hint='Count one kind at a time. A half circle has 1 straight side and 1 curved side. A quarter circle has 2 straight sides that meet in a square corner, and 1 curved side.',
         steps=['Squares: the head and the body, 2.', 'Triangles: the hat and the two hands, 3.', 'Half circles: the two ears and the two feet, 4. Quarter circles: the two shoulders, 2.'],
         src=['The robot is made of pieces. Count each kind of piece and write how many in the boxes.']),
    dict(id='1a', tier='core', no='1(a)', label='1(a)', type='choice', options=['Squares', 'Triangles', 'Half circles', 'Quarter circles'], answer='Half circles', skill='comparing counts', svg=ROBOT,
         q='Look at the robot. Which kind of piece is there the most of?',
         check=lambda: max((('Squares', KINDS['square']), ('Triangles', KINDS['triangle']), ('Half circles', KINDS['half']), ('Quarter circles', KINDS['quarter'])), key=lambda p: p[1])[0],
         hint='Count each kind of piece in the robot, then compare the four counts.',
         steps=['There are 2 squares, 3 triangles, 4 half circles and 2 quarter circles.', '4 is the biggest count, so half circles are there the most.'],
         src=['Which kind is there the most of?']),
    dict(id='1b', tier='core', no='1(b)', label='1(b)', type='number', answer=11, skill='counting pieces', svg=ROBOT,
         q='How many pieces is the robot made of altogether?',
         check=lambda: sum(KINDS.values()),
         hint='Count every piece in the robot once. Do not count any piece twice.',
         steps=['2 squares + 3 triangles + 4 half circles + 2 quarter circles.', '2 + 3 + 4 + 2 = 11 pieces.'],
         src=['Pieces altogether?']),
    dict(id='1c', tier='core', no='1(c)', label='1(c)', type='number', answer=3, skill='half and quarter circles',
         q='Mei has 3 half circles and 6 quarter circles, all cut from same-size circles. How many whole circles can she make?',
         check=lambda: whole_circles(3, 6),
         hint='How many quarter circles make a half circle? Change everything into quarter circles first.',
         steps=['A half circle is 2 quarter circles, so 3 half circles are 6 quarter circles.', '6 + 6 = 12 quarter circles. 4 quarter circles make 1 whole circle.', '12 quarter circles make 3 whole circles.'],
         src=['Mei has 3 half circles and 6 quarter circles, all cut from same-size circles. How many whole circles can she make?']),
    dict(id='1d', tier='core', no='1(c) show how', label='1(c) how', type='selfcheck', open=False, skill='explaining with half and quarter circles',
         q='Mei has 3 half circles and 6 quarter circles, all cut from same-size circles. Show how you can work out how many whole circles she can make. Write your idea in the box.',
         facts=dict(quarters_altogether=12), check=lambda: dict(quarters_altogether=6 + 3 * 2),
         hint='Draw the pieces on paper if it helps. What could you change the half circles into?',
         steps=['Example: 1 half circle = 2 quarter circles. 3 half circles = 6 quarter circles. 6 + 6 = 12 quarter circles, and 4 quarter circles make a whole circle.', 'Any clear way of showing it is good.'],
         src=['Show how.']),

    dict(id='2a', tier='core', no='2(a)', label='2(a)', type='fields', skill='counting squares of every size', svg=GRIDS, answer=[16, 9, 4, 1],
         q='Count every shape. Work in order. Look at grid a. How many squares of each size are there?',
         frame='1 by 1: {f1}   2 by 2: {f2}   3 by 3: {f3}   4 by 4: {f4}',
         check=lambda: [squares_in_grid(4, 4)[s] for s in (1, 2, 3, 4)],
         hint='Slide a 2 by 2 window over the grid and count the places it fits: across and down. Do the same for the other sizes.',
         steps=['1 by 1: 4 across and 4 down, 16 small squares.', '2 by 2: it fits in 3 places across and 3 down, 9 squares. 3 by 3: 2 across and 2 down, 4 squares. 4 by 4: only 1.', 'The boxes are 16, 9, 4 and 1.'],
         src=['Count every shape. Work in order.', 'How many squares?']),
    dict(id='2a2', tier='core', no='2(a) altogether', label='2(a) all', type='number', answer=30, skill='counting squares of every size', svg=GRIDS,
         q='How many squares of ALL sizes are there altogether in grid a (4 squares long and 4 squares high)?',
         check=lambda: sum(squares_in_grid(4, 4).values()),
         hint='Count the squares of each size, one size at a time. Then add the counts.',
         steps=['16 squares of size 1 by 1, 9 of size 2 by 2, 4 of size 3 by 3 and 1 of size 4 by 4.', '16 + 9 + 4 + 1 = 30 squares.'],
         src=['Squares altogether']),
    dict(id='2b', tier='core', no='2(b)', label='2(b)', type='fields', skill='counting triangles', svg=GRIDS, answer=[6, 6],
         q='Look at the triangle b. It has 2 lines from the top corner to the bottom and 1 line across the middle. Count the triangles that sit on each line.',
         frame='On the bottom line {f1}   On the line across {f2}',
         check=lambda: list(triangles_in_fig()[:2]),
         hint='Count the triangles that sit on the bottom line and have their top at the top corner. Choose 2 points on the line: how many pairs of points are there?',
         steps=['The bottom line has 4 marked points. Each pair of points makes a triangle with the top corner: 6 pairs, so 6 triangles.', 'The line across also has 4 marked points, so 6 more triangles.', 'The boxes are 6 and 6.'],
         src=['Triangles on the bottom line:']),
    dict(id='2b2', tier='core', no='2(b) altogether', label='2(b) all', type='number', answer=12, skill='counting triangles', svg=GRIDS,
         q='How many triangles are there altogether in triangle b?',
         check=lambda: triangles_in_fig()[2],
         hint='Count the triangles that sit on the bottom line, then the ones that sit on the line across. Then add.',
         steps=['6 triangles sit on the bottom line and 6 sit on the line across.', '6 + 6 = 12 triangles.'],
         src=['altogether: ____']),

    dict(id='3a', tier='core', no='3(a)', label='3(a)', type='fields', skill='counting cubes in a stack', svg=STACKS_FIG, answer=[5, 8, 14],
         q='Count the cubes in each stack. Every cube is on the table or sits on top of another cube. Stack A is only 1 cube deep. Count the hidden cubes too.',
         frame='A {f1} cubes   B {f2} cubes   C {f3} cubes',
         check=lambda: [cubes_in(STACKS[k]) for k in 'ABC'],
         hint='Count layer by layer. A cube on top has to be sitting on a cube, even if you cannot see it.',
         steps=['A: 3 cubes in the bottom row and 2 on top, 5 cubes.', 'B: a cube 2 long, 2 deep and 2 high, 4 cubes in each layer and 2 layers, 8 cubes.', 'C: a bottom layer 3 by 3 (9 cubes), a layer 2 by 2 (4 cubes) and 1 cube on top: 14 cubes.'],
         src=['Count the cubes. Build stack A with your cubes first, then count.', 'Every cube is on the table or sits on top of another cube.']),
    dict(id='3b', tier='core', no='3(b)', label='3(b)', type='number', answer=13, skill='cubes in a big cube', svg=STACKS_FIG,
         q='Ravi wants to turn stack C into a big cube 3 cubes long, 3 cubes wide and 3 cubes high. How many more cubes does he need?',
         check=lambda: cubes_in([[3] * 3] * 3) - cubes_in(STACKS['C']),
         hint='How many cubes are in the big cube? How many are in stack C already?',
         steps=['The big cube has 3 layers of 9 cubes: 27 cubes.', 'Stack C has 14 cubes, so Ravi needs 27 − 14 = 13 more cubes.'],
         src=['Ravi wants to turn stack C into a big cube 3 cubes long, 3 cubes wide and 3 cubes high. How many more cubes does he need?']),

    dict(id='4a', tier='core', no='4(a)', label='4(a)', type='text', skill='nets of a cube', svg=NETS_AD, accept=list_forms(['A', 'C'], ordered=False), shown='A, C', equiv_frac=False,
         q='Which of the nets A to D fold up into a cube? Type the letters with commas. If you have the cut-out nets, fold them. If not, picture rolling a cube over each net.',
         check=lambda: ', '.join(k for k in 'ABCD' if folds_into_cube(cells_of(NETS[k]))),
         hint='Pick one square for the bottom and fold the others up, one at a time. Does each square land on a new face, or does one land on top of another?',
         steps=['Roll a cube over each net. For A and C every square lands on a different face, so they fold into a cube.', 'In B two squares land on the same face and in D two squares land on the same face, so B and D do not fold into a cube.', 'The nets that fold are A and C.'],
         src=['Circle the letters of the nets that fold up into a cube.']),
    dict(id='4b', tier='core', no='4(b)', label='4(b)', type='set', ordered=False, skill='nets of a cube', svg=PLACES, answer=[7, 8, 9, 10],
         q='Add ONE more square to this shape so that it folds into a cube. The empty squares next to the shape are numbered. Type the numbers of all the places that work.',
         check=lambda: [i + 1 for i, g in enumerate(net_places()[1]) if g], sol_fig=lambda got: PLACES_SOL,
         hint='Imagine the row of 4 squares wrapping round a cube. Which faces are still missing? Where could the last square go to make a missing face?',
         steps=['A square is a good place if the 6 squares fold into a cube with every face used once.', 'The new square can go under any one of the 4 squares of the row: these are the places 7, 8, 9 and 10 in the picture.', 'Any other place leaves two squares on the same face, or a row that is too long.'],
         src=['Add ONE more square to this shape so that it folds into a cube. Draw it on the grid.']),

    # ================= Investigation: Squares joined edge to edge
    dict(id='I1', tier='invest', no='Investigation (a)', label='Inv 1', type='number', skill='finding all the shapes of 3 squares', answer=2,
         q='Squares must touch along a whole side. A shape that is turned round or flipped over counts as the SAME shape. How many different shapes can you make with 3 squares joined edge to edge?',
         check=lambda: len(polyominoes(3)),
         hint='Join 2 squares edge to edge first. Then add a third square in every different place. Is the new shape just a turn or a flip of one you already have?',
         steps=['With 3 squares you can make a straight line of 3, or an L shape.', 'Every other way is a turn or a flip of one of these. So there are 2 different shapes.'],
         src=['Squares must touch along a whole side. A shape that is turned round or flipped over counts as the SAME shape.', 'Find ALL the different shapes you can make with 3 squares.']),
    dict(id='I2', tier='invest', no='Investigation (a) draw', label='Inv 2', type='selfcheck', paper=True, open=False, skill='finding all the shapes of 3 squares',
         q='Draw all the different shapes you can make with 3 squares on paper, on a grid if you have one.',
         facts=dict(n=2), check=lambda: dict(n=len(polyominoes(3))), sol_fig=lambda facts: polyominoes_fig(3),
         hint='Use 3 small squares of paper or tiles if you have them. Slide them around and draw each different shape.',
         steps=['The picture shows both shapes: the straight line and the L.', 'Check that each of your drawings is one of these, turned or flipped.'],
         src=['Find ALL the different shapes you can make with 3 squares.']),
    dict(id='I3', tier='invest', no='Investigation (b)', label='Inv 3', type='number', skill='finding all the shapes of 4 squares', answer=5,
         q='Now think about 4 squares joined edge to edge. Turns and flips count as the SAME shape. How many different shapes can you make?',
         check=lambda: len(polyominoes(4)),
         hint='Start with each of the shapes of 3 squares and add a fourth square in every different place. Leave out the ones that are a turn or a flip of one you already have.',
         steps=['The shapes are: a straight line of 4, a 2 by 2 square, an L, a T and a zigzag (S shape).', 'Every other way is a turn or a flip of one of these. So there are 5 different shapes.'],
         src=['Now find ALL the different shapes you can make with 4 squares.']),
    dict(id='I4', tier='invest', no='Investigation (b) draw', label='Inv 4', type='selfcheck', paper=True, open=False, skill='finding all the shapes of 4 squares',
         q='Draw all the different shapes you can make with 4 squares on paper, on a grid if you have one.',
         facts=dict(n=5), check=lambda: dict(n=len(polyominoes(4))), sol_fig=lambda facts: polyominoes_fig(4),
         hint='Use 4 small squares of paper or tiles if you have them. Slide them around and draw each different shape.',
         steps=['The picture shows all 5 shapes.', 'If you counted a flipped L or a flipped zigzag as different, you found 7 shapes. Turns and flips count as the same shape, so the answer is 5.'],
         src=['Draw each one on the grid.']),
    dict(id='I5', tier='invest', no='Investigation (c)', label='Inv 5', type='selfcheck', open=False, skill='explaining a complete search',
         q='How do you know you have found them all? Write your idea in the box.',
         facts=dict(counts_for_1_to_4=[len(polyominoes(n)) for n in (1, 2, 3, 4)]), check=lambda: dict(counts_for_1_to_4=[len(polyominoes(n)) for n in (1, 2, 3, 4)]),
         hint='Did you work in an order, for example starting with the straight line and moving one square at a time? How did you check each new shape against the others?',
         steps=['Example: I started with the straight line, then moved one square at a time to a new place. I turned each new shape to check it was not the same as one I already had.', 'Any idea that uses a system is good.'],
         src=['How do you know you have found them all?']),

    # ================= Think harder
    dict(id='T1', tier='stretch', no='Think harder 1', label='T1', type='number', answer=19, skill='counting cubes layer by layer', svg=T1_FIG,
         q='A stack of cubes has a bottom layer 4 cubes long and 3 cubes deep, a middle layer 3 cubes long and 2 cubes deep, and 1 cube on top. How many cubes are in the stack?',
         check=lambda: layer_cubes([(4, 3), (3, 2), (1, 1)]),
         hint='Count the cubes in each layer, one layer at a time. Then add the layers.',
         steps=['Bottom layer: 4 × 3 = 12 cubes. Middle layer: 3 × 2 = 6 cubes. Top: 1 cube.', '12 + 6 + 1 = 19 cubes.'],
         src=['A stack of cubes has a bottom layer 4 cubes long and 3 cubes deep, a middle layer 3 cubes long and 2 cubes deep, and 1 cube on top. How many cubes are in the stack?']),
    dict(id='T2', tier='stretch', no='Think harder 2', label='T2', type='number', answer=9, skill='counting rectangles', svg=GRID22,
         q='How many rectangles can you find in a grid 2 squares long and 2 squares high? Remember that a square is a rectangle too. Count them by size.',
         check=lambda: rectangles_in_grid(2, 2),
         hint='Count by size: first the small squares, then the rectangles that are 2 squares long, then the ones that are 2 squares tall, then the biggest.',
         steps=['4 small squares (1 by 1), 2 long ones (1 high, 2 long), 2 tall ones (2 high, 1 long) and the whole grid (2 by 2).', '4 + 2 + 2 + 1 = 9 rectangles.'],
         src=['How many rectangles can you find in a grid 2 squares long and 2 squares high?']),
    dict(id='T3a', tier='stretch', no='Think harder 3', label='T3', type='choice', options=['E', 'F'], answer='E', skill='nets of a cube', svg=NETS_EF,
         q='Which of the nets E and F folds up into a cube? If you have the cut-out nets, try folding them. If not, picture rolling a cube over each net.',
         check=lambda: next(k for k in 'EF' if folds_into_cube(cells_of(NETS[k]))),
         hint='Pick one square for the bottom and fold the others up, one at a time. Does each square land on a new face?',
         steps=['Roll a cube over net E: every square lands on a different face, so E folds into a cube.', 'Net F: two squares land on the same face, so F does not fold into a cube.'],
         src=['Cut out nets E and F from the cut-out page and try folding them. Which one folds up into a cube?']),
    dict(id='T3b', tier='stretch', no='Think harder 3 explain', label='T3 why', type='selfcheck', open=False, skill='explaining nets', svg=NETS_EF,
         q='Look at nets E and F. How do you know which one folds into a cube? Write your idea in the box.',
         facts=dict(E=folds_into_cube(cells_of(NETS['E'])), F=folds_into_cube(cells_of(NETS['F']))), check=lambda: dict(E=folds_into_cube(cells_of(NETS['E'])), F=folds_into_cube(cells_of(NETS['F']))),
         hint='Follow the squares as they fold up. What happens to the last squares? Does each one land on a face that is not used yet?',
         steps=['Example: When I fold net E, each square becomes a new face of the cube. When I fold net F, the long row wraps round the cube and two squares land on the same face.', 'Any idea that follows the folding is good.'],
         src=['How do you know?']),
    dict(id='T4a', tier='stretch', no='Think harder 4', label='T4', type='choice', options=['Yes', 'No'], answer='No', skill='nets of a cube', svg=LINE6,
         q='Six squares are joined in a straight line. Can they fold into a cube?',
         check=lambda: 'Yes' if folds_into_cube({(0, c) for c in range(6)}) else 'No',
         hint='Wrap the line of squares round a cube. Where does the 5th square land?',
         steps=['When you wrap the line round a cube, the 5th square lands on the same face as the 1st square.', 'So six squares in a straight line cannot fold into a cube.'],
         src=['Six squares are joined in a straight line. Can they fold into a cube? Explain.']),
    dict(id='T4b', tier='stretch', no='Think harder 4 explain', label='T4 why', type='selfcheck', open=False, skill='explaining nets', svg=LINE6,
         q='Six squares are joined in a straight line. Explain what you think happens when you try to fold them into a cube. Write your idea in the box.',
         facts=dict(line_of_6_folds=folds_into_cube({(0, c) for c in range(6)})), check=lambda: dict(line_of_6_folds=folds_into_cube({(0, c) for c in range(6)})),
         hint='Follow the squares as you wrap them round a cube. Which squares land on the same face?',
         steps=['Example: The first 4 squares wrap right round the cube. The 5th square lands on the same face as the 1st and the 6th on the same face as the 2nd, and two faces are left empty.', 'Any idea that follows the folding is good.'],
         src=['Can they fold into a cube? Explain.']),

    # ================= Go further
    dict(id='C5', tier='challenge', no='Go further 5', label='G5', type='number', answer=30, skill='counting cubes layer by layer', svg=C5_FIG,
         q='A pyramid of cubes has a top layer of 1 cube, then a layer 2 by 2, then a layer 3 by 3, then a bottom layer 4 by 4. How many cubes are there?',
         check=lambda: layer_cubes([(1, 1), (2, 2), (3, 3), (4, 4)]),
         hint='Count the cubes in each layer first. Then add the four layers.',
         steps=['The layers have 1, 4, 9 and 16 cubes.', '1 + 4 + 9 + 16 = 30 cubes.'],
         src=['A pyramid of cubes has a top layer of 1 cube, then a layer 2 by 2, then a layer 3 by 3, then a bottom layer 4 by 4. How many cubes are there?']),
    dict(id='C6', tier='challenge', no='Go further 6', label='G6', type='number', answer=55, skill='counting squares of every size', svg=GRID55,
         q='How many squares can you find in a grid 5 squares long and 5 squares high?',
         check=lambda: sum(squares_in_grid(5, 5).values()),
         hint='Count by size: 1 by 1 first, then 2 by 2, and so on. For each size, count the places it fits across and down.',
         steps=['1 by 1: 25. 2 by 2: 16. 3 by 3: 9. 4 by 4: 4. 5 by 5: 1.', '25 + 16 + 9 + 4 + 1 = 55 squares.'],
         src=['How many squares can you find in a grid 5 squares long and 5 squares high?']),
    dict(id='C7a', tier='challenge', no='Go further 7', label='G7 3 by 3', type='fields', skill='painted cubes', answer=[8, 12, 6, 1],
         q='A 3 by 3 by 3 cube is built from 27 small cubes and the whole outside is painted. Sort the small cubes. How many have paint on 3 faces, on 2 faces, on 1 face and on no faces?',
         frame='3 faces {f1}   2 faces {f2}   1 face {f3}   no paint {f4}',
         check=lambda: [painted_counts(3)[k] for k in (3, 2, 1, 0)],
         hint='Think about where the small cubes sit: the corners, the middles of the edges, the middles of the faces and the very middle. Do your four numbers add up to 27?',
         steps=['Paint on 3 faces: the 8 corners. On 2 faces: 12, one in the middle of each edge.', 'On 1 face: 6, the middle of each face. No paint: 1, the cube in the very centre.', '8 + 12 + 6 + 1 = 27.'],
         src=['A 3 by 3 by 3 cube is built from 27 small cubes and the whole outside is painted. Sort the small cubes: how many have paint on 3 faces, on 2 faces, on 1 face and on no faces?']),
    dict(id='C7b', tier='challenge', no='Go further 7 (4 by 4)', label='G7 4 by 4', type='number', answer=8, skill='painted cubes',
         q='What if the big cube is 4 by 4 by 4 and its whole outside is painted: how many small cubes have no paint?',
         check=lambda: painted_counts(4)[0],
         hint='The cubes with no paint are all inside. What shape do they make together? How long is each side of it?',
         steps=['Take off the outside layer of cubes on every side. What is left inside is a block 2 cubes long, 2 wide and 2 high.', '2 × 2 × 2 = 8 small cubes have no paint.'],
         src=['What if the big cube is 4 by 4 by 4: how many small cubes have no paint?']),
    dict(id='M', tier='challenge', no='Make up your own', label='Make', type='selfcheck', open=True, skill='making puzzles', marking_mode='open',
         q='Make up a stack of cubes with exactly 20 cubes. Draw its layers on paper.',
         hint='Think of a stack with 2 or more layers. Count the cubes in each layer, then add them up. Is the total 20?',
         steps=['Many answers are right. Example: a stack 5 long, 2 wide and 2 high has 5 × 2 × 2 = 20 cubes.', 'Another: four layers of 9, 6, 4 and 1 cubes. 9 + 6 + 4 + 1 = 20.'],
         src=['a stack of cubes with exactly 20 cubes. Draw its layers.']),
]
for _d in ITEMS:
    _d.setdefault('strand', STRAND)
    if _d['type'] == 'selfcheck':
        _d.setdefault('marking_mode', 'self')


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '1c': dict(
        base=dict(h=3, q=6),
        tpl=dict(vars=dict(h=[3, 5, 7], q=[2, 6, 10]), derive=dict(t='2*h+q'),
                 q='Mei has {h} half circles and {q} quarter circles, all cut from same-size circles. How many whole circles can she make?',
                 answer='(2*h+q)/4', hint='How many quarter circles make a half circle? Change everything into quarter circles first.',
                 steps=['Each half circle is 2 quarter circles, so {h} half circles and {q} quarter circles are {t} quarter circles.', '4 quarter circles make 1 whole circle, so the answer is {t} ÷ 4 = {ans}.']),
        oracle=lambda e: whole_circles(e['h'], e['q'])),
    '2a2': dict(
        base=dict(n=4),
        tpl=dict(vars=dict(n=[2, 3, 4, 5, 6]), answer='n*(n+1)*(2*n+1)/6',
                 q='A grid is {n} squares long and {n} squares high. How many squares of ALL sizes can you find altogether? Count by size.',
                 hint='Count the 1 by 1 squares first, then the 2 by 2 squares, and so on. Slide a window and count where it fits. Then add.',
                 steps=['Count the squares of every size: for each size, count the places it fits across and down.', 'Adding all the sizes gives {ans} squares.']),
        fig=lambda e: grid_plain(e['n'], e['n']),
        oracle=lambda e: sum(squares_in_grid(e['n'], e['n']).values())),
    '3b': dict(
        base=dict(k=3, c=14),
        tpl=dict(vars=dict(k=[3, 4], c=[9, 14, 18, 20]), derive=dict(big='k*k*k'),
                 q='A stack has {c} cubes. Ravi wants to turn it into a big cube {k} cubes long, {k} cubes wide and {k} cubes high. How many more cubes does he need?',
                 answer='k*k*k-c', hint='How many cubes are in the big cube? How many are in the stack already?',
                 steps=['The big cube has {k} layers of {k} × {k} cubes: {big} cubes.', 'The stack has {c} cubes, so he needs {big} − {c} = {ans} more cubes.']),
        oracle=lambda e: cubes_in([[e['k']] * e['k']] * e['k']) - e['c']),
    'T1': dict(
        base=dict(a=4, b=3, c=3, d=2),
        tpl=dict(vars=dict(a=[3, 4, 5], b=[3, 4], c=[2, 3], d=[2]), derive=dict(bl='a*b', ml='c*d'),
                 q='A stack of cubes has a bottom layer {a} cubes long and {b} cubes deep, a middle layer {c} cubes long and {d} cubes deep, and 1 cube on top. How many cubes are in the stack?',
                 answer='a*b+c*d+1', hint='Count the cubes in each layer, one layer at a time. Then add the layers.',
                 steps=['Bottom layer: {a} × {b} = {bl} cubes. Middle layer: {c} × {d} = {ml} cubes. Top: 1 cube.', '{bl} + {ml} + 1 = {ans} cubes.']),
        oracle=lambda e: layer_cubes([(e['a'], e['b']), (e['c'], e['d']), (1, 1)])),
    'C7b': dict(
        base=dict(n=4),
        tpl=dict(vars=dict(n=[3, 4, 5, 6, 7]), derive=dict(m='n-2'), answer='(n-2)*(n-2)*(n-2)',
                 q='A big cube is {n} by {n} by {n} small cubes, and its whole outside is painted. How many small cubes have no paint?',
                 hint='The cubes with no paint are all inside. What shape do they make together? How long is each side of it?',
                 steps=['Take off the outside layer of cubes on every side. What is left inside is a block {m} cubes long, {m} wide and {m} high.', '{m} × {m} × {m} = {ans} small cubes have no paint.']),
        oracle=lambda e: painted_counts(e['n'])[0]),
}
