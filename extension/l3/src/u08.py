from lib import *

u = Unit(8, 'Corners and lines', 'Angles and lines',
         'I can compare angles with a right angle. I can find perpendicular and parallel lines. I can count angles in a figure.')


SHAPES_ABC = ([[0, 0, 4, 0], [4, 0, 4, 2], [4, 2, 2, 2], [2, 2, 2, 4], [2, 4, 0, 4], [0, 4, 0, 0]] +
              [[x + 6, y, x2 + 6, y2] for x, y, x2, y2 in [(0, 4, 4, 4), (4, 4, 4, 3), (4, 3, 3, 3), (3, 3, 3, 0), (3, 0, 1, 0), (1, 0, 1, 3), (1, 3, 0, 3), (0, 3, 0, 4)]] +
              [[x + 12, y, x2 + 12, y2] for x, y, x2, y2 in [(0, 0, 4, 0), (4, 0, 3, 4), (3, 4, 0, 4), (0, 4, 0, 0)]])
SHAPES_ABCD = ([[0, 0, 4, 0], [4, 0, 4, 3], [4, 3, 0, 3], [0, 3, 0, 0]] +
               [[x + 6, y, x2 + 6, y2] for x, y, x2, y2 in [(0, 0, 4, 0), (4, 0, 4, 3), (4, 3, 2, 4.5), (2, 4.5, 0, 3), (0, 3, 0, 0)]] +
               [[x + 12, y, x2 + 12, y2] for x, y, x2, y2 in [(0, 0, 4, 0), (4, 0, 4, 2), (4, 2, 2, 4), (2, 4, 0, 4), (0, 4, 0, 0)]] +
               [[x + 18, y, x2 + 18, y2] for x, y, x2, y2 in [(0, 0, 4, 0), (4, 0, 5, 3), (5, 3, 1, 3), (1, 3, 0, 0)]])
import math as _m
_ang = [10, 55, 100, 145]
FAN4 = [[0, 0, round(3.4 * _m.cos(_m.radians(a)), 2), round(3.4 * _m.sin(_m.radians(a)), 2)] for a in _ang]
GRID1 = [[1, 1, 5, 3], [2, 5, 4, 1], [0, 4, 4, 2], [2, 0, 6, 2], [4, 4, 6, 6]]
LADDER = [[0, 0, 0, 4], [3, 0, 3, 4], [0, 1, 3, 1], [0, 2, 3, 2], [0, 3, 3, 3]]
PLUS = [[1, 0, 2, 0], [2, 0, 2, 1], [2, 1, 3, 1], [3, 1, 3, 2], [3, 2, 2, 2], [2, 2, 2, 3], [2, 3, 1, 3], [1, 3, 1, 2], [1, 2, 0, 2], [0, 2, 0, 1], [0, 1, 1, 1], [1, 1, 1, 0]]
STAIRS = [[0, 0, 4, 0], [4, 0, 4, 1], [4, 1, 3, 1], [3, 1, 3, 2], [3, 2, 2, 2], [2, 2, 2, 3], [2, 3, 1, 3], [1, 3, 1, 4], [1, 4, 0, 4], [0, 4, 0, 0]]

# letters as line segments (x right, y up), 3 wide and 4 high
LET = {'F': [(0, 0, 0, 4), (0, 4, 3, 4), (0, 2, 2, 2)], 'V': [(0, 4, 1.5, 0), (1.5, 0, 3, 4)],
       'N': [(0, 0, 0, 4), (0, 4, 3, 0), (3, 0, 3, 4)], 'L': [(0, 4, 0, 0), (0, 0, 3, 0)],
       'E': [(0, 0, 0, 4), (0, 4, 3, 4), (0, 2, 2.5, 2), (0, 0, 3, 0)], 'H': [(0, 0, 0, 4), (3, 0, 3, 4), (0, 2, 3, 2)],
       'T': [(0, 4, 3, 4), (1.5, 4, 1.5, 0)], 'Y': [(0, 4, 1.5, 2), (3, 4, 1.5, 2), (1.5, 2, 1.5, 0)], 'Z': [(0, 4, 3, 4), (3, 4, 0, 0), (0, 0, 3, 0)]}


def letters(names, wm, gap=1.6):
    sg = []
    for i, n in enumerate(names):
        ox = i * (3 + gap)
        sg += [{'p': [x1 + ox, y1, x2 + ox, y2], 'w': 11} for x1, y1, x2, y2 in LET[n]]
    return {'type': 'l3_segs', 'segs': sg, 'k': 36, 'width_mm': wm, 'pad': 24}


def poly(pts, wm, k=40, labels=None, texts=None, **kw):
    d = {'type': 'l3_poly', 'pts': pts, 'k': k, 'width_mm': wm, 'labels': labels or [], 'texts': texts or []}
    d.update(kw)
    return d


u.learn(
    'An angle is made where 2 lines meet. A right angle is a square corner, like the corner of a page. Use the corner of a piece of paper as a right angle checker.',
    {'problem': 'Use a right angle checker. Is each angle smaller than, equal to, or greater than a right angle?',
     'figure': {'type': 'l3_angles', 'items': [{'deg': 50, 'rot': 15, 'label': 'P'}, {'deg': 90, 'rot': 5, 'label': 'Q'}, {'deg': 130, 'rot': 0, 'label': 'R'}], 'cols': 3, 'width_mm': 134},
     'steps': ['Put the paper corner on the point where the lines meet.', 'Line up one side of the paper with one line.',
               'Look at the other line. If it is inside the corner, the angle is smaller. If it is outside, the angle is greater.'],
     'answer': 'P is smaller than a right angle. Q is a right angle. R is greater than a right angle.'},
    {'title': 'Lines to remember',
     'steps': ['Perpendicular lines meet at a right angle.', 'Parallel lines never meet. They stay the same distance apart.',
               'Count angles in order: the small ones first.', 'A corner that points into a shape is a dent. A dent is greater than a right angle.']},
    {'text': 'Use a right angle checker. This angle is   {circ:smaller than|equal to|greater than}   a right angle.',
     'figure': {'type': 'l3_angles', 'items': [{'deg': 70, 'rot': 10}], 'cols': 1, 'width_mm': 44}, 'figright': True,
     'answer': A('smaller than'), 'explanation': 'The second line is inside the corner of the checker, so the angle is smaller than a right angle.'})
u.u['learn']['tight'] = True

# ---------------- Start here (pages 1 to 3)
u.S(1, 'Use a right angle checker on each angle. Write the letters.', parts=[
    P('a', 'Smaller than a right angle: {l}', A(['B', 'E'], 'B and E', list=True)),
    P('b', 'A right angle: {l}', A(['A', 'F'], 'A and F', list=True)),
    P('c', 'Greater than a right angle: {l}', A(['C', 'D'], 'C and D', list=True))],
    figure={'type': 'l3_angles', 'items': [{'deg': 90, 'rot': 20, 'label': 'A'}, {'deg': 55, 'rot': 0, 'label': 'B'}, {'deg': 125, 'rot': 40, 'label': 'C'},
                                           {'deg': 150, 'rot': 10, 'label': 'D'}, {'deg': 40, 'rot': 60, 'label': 'E'}, {'deg': 90, 'rot': 100, 'label': 'F'}], 'cols': 3, 'ch': 176, 'width_mm': 110},
    why='A and F fit the checker exactly, so they are right angles. B and E are inside the corner of the checker, so they are smaller. C and D stick out past the corner of the checker, so they are greater.')
u.S(1, 'Count the right angles INSIDE each shape. Check each corner with your paper corner.', parts=[
    P('a', 'A: {b} right angles', A('5')), P('b', 'B: {b} right angles', A('6')), P('c', 'C: {b} right angles', A('2'))],
    partsrow=True,
    figure={'type': 'l3_segs', 'k': 30, 'pad': 44, 'width_mm': 90, 'segs': SHAPES_ABC, 'labels': [{'x': 2, 'y': -0.9, 't': 'A'}, {'x': 8, 'y': -0.9, 't': 'B'}, {'x': 14, 'y': -0.9, 't': 'C'}]},
    why='Shape A is an L. It has 5 right angles, and its dent is greater than a right angle. Shape B has 6 right angles and 2 dents. Shape C has right angles only at its 2 left corners. Its 2 sloping corners do not fit the checker.')
u.S(1, 'Look at the letters.', parts=[
    P('a', 'Circle each letter with 2 PARALLEL lines.   {circ:F|V|N|L}', A(['F', 'N'], 'F and N', list=True)),
    P('b', 'Circle each letter with 2 PERPENDICULAR lines.   {circ:F|V|N|L}', A(['F', 'L'], 'F and L', list=True))],
    figure=letters(['F', 'V', 'N', 'L'], 64),
    why='F has 2 parallel arms and a stem that meets them at right angles. V has 2 sloping lines that are neither parallel nor perpendicular. N has 2 parallel upright lines, but its sloping line is not perpendicular to them. L has 2 lines that meet at a right angle.')

u.S(2, 'These 4 lines all start at point O. Count the angles. Count the small ones first.', parts=[
    P('a', 'Angles made of 1 small angle: {b}', A('3')), P('b', 'Made of 2 small angles: {b}', A('2')),
    P('c', 'Made of 3 small angles: {b}', A('1')), P('d', 'Angles in all: {b}', A('6'))],
    figure={'type': 'l3_segs', 'k': 44, 'pad': 30, 'width_mm': 58, 'segs': FAN4, 'labels': [{'x': 0, 'y': 0, 't': 'O', 'dx': -22, 'dy': 24}]}, figside=True,
    why='There are 3 small angles. The next size is made of 2 small angles side by side: 2 of those. Then 1 angle made of all 3 small ones. 3 + 2 + 1 = 6 angles.')
u.S(2, 'Look at the lines on the dot grid.', parts=[
    P('a', 'Which line is PARALLEL to line AB?   {circ:P|Q|R|S}', A('R')),
    P('b', 'Which line is PERPENDICULAR to line AB?   {circ:P|Q|R|S}', A('P'))],
    figure={'type': 'l3_segs', 'k': 44, 'pad': 36, 'width_mm': 62, 'dots': [7, 7], 'segs': GRID1,
            'labels': [{'x': 1, 'y': 1, 't': 'A', 'dx': -24, 'dy': 22}, {'x': 5, 'y': 3, 't': 'B', 'dx': 26}, {'x': 2, 'y': 5, 't': 'P', 'dx': -4, 'dy': -26}, {'x': 0, 'y': 4, 't': 'Q', 'dx': -26},
                       {'x': 6, 'y': 2, 't': 'R', 'dx': 26}, {'x': 6, 'y': 6, 't': 'S', 'dx': 26}]},
    why='Line AB goes 4 across and 2 up. R goes 4 across and 2 up too, so it never meets AB: parallel. P goes 2 across and 4 down, which turns AB through a right angle: perpendicular. Q and S slope in other ways.')
u.S(2, 'A ladder has 2 upright rails and 3 rungs. Each rung meets a rail at right angles.', parts=[
    P('a', 'Where one rung meets the 2 rails there are {b} right angles.', A('4')), P('b', 'The ladder has {b} right angles in all.', A('12'))],
    figure={'type': 'l3_segs', 'k': 40, 'pad': 24, 'width_mm': 40, 'segs': LADDER}, figside=True,
    why='At each end of a rung, the rung and the rail make 2 right angles (one above the rung and one below it). A rung has 2 ends, so 4 right angles. 3 rungs make 3 × 4 = 12 right angles.')

u.S(3, 'Mei faces north. She makes turns of a right angle.', parts=[
    P('a', 'She turns 1 right angle to the right. She faces   {circ:N|E|S|W}', A('E')),
    P('b', 'From north, she turns 3 right angles to the right. She faces   {circ:N|E|S|W}', A('W')),
    P('c', 'From north, she turns 2 right angles to the left. She faces   {circ:N|E|S|W}', A('S'))],
    why='Going round to the right, north is followed by east, south and west. (a) 1 turn: east. (b) 3 turns: west. (c) 2 turns to the left from north: west, then south. Two right angles in either direction face the opposite way: south.')
u.S(3, 'Fill in the blanks.', parts=[
    P('a', 'A rectangle has {b} right angles.', A('4')), P('b', 'A rectangle has {b} pairs of parallel sides.', A('2')),
    P('c', 'A triangle has at most {b} right angle.', A('1')),
    P('d', 'Two sides that meet at a corner of a square are   {circ:parallel|perpendicular}', A('perpendicular'))],
    why='(a) Each corner of a rectangle is a right angle: 4. (b) The 2 long sides are parallel and the 2 short sides are parallel: 2 pairs. (c) If a triangle had 2 right angles, those sides would be parallel and never meet to make a triangle. (d) The sides of a square meet at right angles.')
u.S(3, 'Circle True or False.', parts=[
    P('a', 'Lines that are perpendicular cross at a right angle.   {circ:True|False}', A('True')),
    P('b', 'Parallel lines meet if you make them long enough.   {circ:True|False}', A('False')),
    P('c', 'One line can be perpendicular to 2 parallel lines.   {circ:True|False}', A('True')),
    P('d', 'Two lines that cross are always perpendicular.   {circ:True|False}', A('False'))],
    why='(a) That is what perpendicular means. (b) Parallel lines never meet. (c) A line across 2 rails of a ladder is perpendicular to both. (d) Lines can cross at any angle. Only some crossings make right angles.')
u.S(3, 'Siti says angle X is a right angle.', parts=[
    P('a', 'Is she right?   {circ:Yes|No}', A('No')),
    P('b', 'Angle X is   {circ:smaller than|equal to|greater than}   a right angle.', A('greater than'))],
    figure=poly([[0, 0], [4, 0], [4, 2], [2, 2], [2, 4], [0, 4]], 62, 36, texts=[{'x': 1.2, 'y': 1.2, 'text': 'X', 'size': 36}], arcs=[{'x': 2, 'y': 2, 'r': 0.7, 'a0': 90, 'a1': 360}]), figside=True,
    why='Angle X is a dent. It points into the shape. A checker does not fit inside it: the angle is greater than a right angle.')

# ---------------- Think harder
u.T('Lines from a point O make angles. 2 lines give 1 angle, 3 lines give 3 angles and 4 lines give 6 angles.', parts=[
    P('a', 'With 5 lines there are {b} angles.', A('10')), P('b', 'With 7 lines there are {b} angles.', A('21'))],
    hint='Small angles first: 4. Then angles made of 2 small ones: 3.',
    space={'rows': ['Working:']},
    why='With 5 lines there are 4 small angles. Then 3 angles made of 2 small angles, 2 made of 3, and 1 made of 4. 4 + 3 + 2 + 1 = 10. With 7 lines the small angles are 6: 6 + 5 + 4 + 3 + 2 + 1 = 21.')
u.T('Draw a line from C that is PERPENDICULAR to line AB. Use a ruler. Make it reach the bottom row of dots.', parts=[
    P('a', 'Your line reaches the bottom row at   {circ:P|Q|R|S}', A('R'))],
    figure={'type': 'l3_segs', 'k': 44, 'pad': 52, 'width_mm': 70, 'dots': [7, 7], 'segs': [[0, 2, 4, 4]],
            'labels': [{'x': 0, 'y': 2, 't': 'A', 'dx': -26, 'dy': 20}, {'x': 4, 'y': 4, 't': 'B', 'dx': 26}, {'x': 2, 'y': 6, 't': 'C', 'dy': -32},
                       {'x': 2, 'y': 0, 't': 'P', 'dy': 40}, {'x': 4, 'y': 0, 't': 'Q', 'dy': 40}, {'x': 5, 'y': 0, 't': 'R', 'dy': 40}, {'x': 6, 'y': 0, 't': 'S', 'dy': 40}]},
    figside=True,
    hint='AB goes 2 across and 1 up. Turn it a quarter turn.',
    why='AB goes 2 across for every 1 up. A line perpendicular to it goes 1 across and 2 down. From C, keep going 1 across and 2 down until you reach the bottom row: R.')
u.T('Look at the steps. All its corners are square.', parts=[
    P('a', 'It has {b} dents.', A('3')), P('b', 'It has {b} right angles inside.', A('7')),
    P('c', 'Another shape with square corners has 14 corners and 5 dents. It has {b} right angles inside.', A('9'))],
    figure={'type': 'l3_segs', 'k': 30, 'pad': 20, 'width_mm': 44, 'segs': STAIRS}, figside=True,
    hint='Count the dents first. Which corners are left?',
    why='The steps have 10 corners. 3 of them dent into the shape: they are greater than a right angle. The other 7 fit a checker. In (c) the 14 corners are right angles or dents: 14 - 5 = 9 right angles.')

# ---------------- Go further
u.G('Beyond Level 3: Degrees.\nA right angle is 90 degrees.', parts=[
    P('a', '2 right angles make a straight line: {b} degrees.', A('180')), P('b', '4 right angles make a full turn: {b} degrees.', A('360')),
    P('c', 'Half of a right angle is {b} degrees.', A('45')), P('d', '3 right angles make {b} degrees.', A('270'))],
    partsrow=True,
    hint='Add the right angles: 90 + 90 + ...',
    why='(a) 90 + 90 = 180. (b) 4 × 90 = 360. (c) 90 ÷ 2 = 45. (d) 3 × 90 = 270.')
u.G('Beyond Level 3: Lines and a third line.\nTwo upright lines both cross the long line at right angles.', parts=[
    P('a', 'The 2 upright lines are   {circ:parallel|perpendicular}', A('parallel')),
    P('b', 'A line is perpendicular to one of 2 parallel lines. Is it also perpendicular to the other?   {circ:Yes|No}', A('Yes'))],
    figure={'type': 'l3_segs', 'k': 44, 'pad': 24, 'width_mm': 62, 'segs': [[0, 0, 6, 0], [1.5, -1.2, 1.5, 1.8], [4.5, -1.2, 4.5, 1.8]]},
    hint='Do the 2 upright lines ever meet?',
    why='(a) Two lines that are perpendicular to the same line stay the same distance apart and never meet: they are parallel. (b) A line that crosses 2 parallel lines makes the same angle with both. So a right angle with one means a right angle with the other.')
u.G('A board has 2 lines across and 2 lines up.', parts=[
    P('a', 'There are {b} pairs of parallel lines.', A('2')), P('b', 'The lines make {b} right angles where they cross.', A('16')),
    P('c', 'A board with 3 lines across and 3 lines up makes {b} right angles.', A('36'))],
    figure={'type': 'l3_segs', 'k': 40, 'pad': 20, 'width_mm': 38, 'segs': [[0, 1, 3, 1], [0, 2, 3, 2], [1, 0, 1, 3], [2, 0, 2, 3]]}, figside=True,
    hint='Each place where 2 lines cross makes 4 right angles.',
    why='(a) The 2 lines across are parallel and the 2 lines up are parallel: 2 pairs. (b) The lines cross in 2 × 2 = 4 places, and each crossing has 4 right angles: 16. (c) 3 × 3 = 9 crossings, 9 × 4 = 36 right angles.')

# ---------------- Check yourself
u.C('Use a right angle checker. This angle is   {circ:smaller than|equal to|greater than}   a right angle.', A('greater than'),
    figure={'type': 'l3_angles', 'items': [{'deg': 120, 'rot': 15}], 'cols': 1, 'width_mm': 44}, figright=True,
    why='The second line sticks out past the corner of the checker, so the angle is greater than a right angle.')
u.C('Circle each letter that has parallel lines.   {circ:E|H|V|Y}', A(['E', 'H'], 'E and H', list=True),
    figure=letters(['E', 'H', 'V', 'Y'], 58),
    why='E has 3 parallel arms. H has 2 parallel upright lines. V has 2 sloping lines that are not parallel. Y has no pair of parallel lines.')
u.C('A rectangle has {b} pairs of parallel sides.', A('2'), why='The 2 long sides are parallel and the 2 short sides are parallel.')
u.C('Ben faces east. He turns 1 right angle to the left. He faces   {circ:N|E|S|W}', A('N'), why='Turning left from east, the next direction is north.')
u.save()
