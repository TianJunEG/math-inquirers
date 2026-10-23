from lib import *

u = Unit(8, 'Angle and line detectives', 'Angles, perpendicular lines and parallel lines',
         'I can compare angles with a right angle. I can find perpendicular and parallel lines. I can count angles in a figure.')

# letters as line segments (x right, y up), 3 wide and 4 high
LET = {'F': [(0, 0, 0, 4), (0, 4, 3, 4), (0, 2, 2, 2)], 'V': [(0, 4, 1.5, 0), (1.5, 0, 3, 4)],
       'N': [(0, 0, 0, 4), (0, 4, 3, 0), (3, 0, 3, 4)], 'L': [(0, 4, 0, 0), (0, 0, 3, 0)],
       'E': [(0, 0, 0, 4), (0, 4, 3, 4), (0, 2, 2.5, 2), (0, 0, 3, 0)], 'H': [(0, 0, 0, 4), (3, 0, 3, 4), (0, 2, 3, 2)],
       'T': [(0, 4, 3, 4), (1.5, 4, 1.5, 0)], 'Z': [(0, 4, 3, 4), (3, 4, 0, 0), (0, 0, 3, 0)]}


def letters(names, wm, gap=1.6):
    sg = []
    for i, n in enumerate(names):
        ox = i * (3 + gap)
        sg += [[x1 + ox, y1, x2 + ox, y2] for x1, y1, x2, y2 in LET[n]]
    return {'type': 'l3_segs', 'segs': sg, 'k': 36, 'width_mm': wm, 'pad': 24}


def poly(pts, wm, k=40, labels=None, texts=None, **kw):
    d = {'type': 'l3_poly', 'pts': pts, 'k': k, 'width_mm': wm, 'labels': labels or [], 'texts': texts or []}
    d.update(kw)
    return d


u.learn(
    'An angle is made where 2 lines meet. A right angle is a square corner, like the corner of a page. Use the corner of a piece of paper as a right angle checker.',
    {'problem': 'Use a right angle checker. Is each angle smaller than, equal to, or greater than a right angle?',
     'figure': {'type': 'l3_angles', 'items': [{'deg': 50, 'rot': 15, 'label': 'P'}, {'deg': 90, 'rot': 5, 'label': 'Q'}, {'deg': 130, 'rot': 0, 'label': 'R'}], 'cols': 3, 'width_mm': 134},
     'steps': ['Put the corner of the paper on the point where the 2 lines meet.', 'Line up one side of the paper with one line.',
               'Look at the other line. If it is inside the corner, the angle is smaller. If it is outside, the angle is greater.'],
     'answer': 'P is smaller than a right angle. Q is a right angle. R is greater than a right angle.'},
    {'title': 'Lines to remember',
     'steps': ['Perpendicular lines meet at a right angle.', 'Parallel lines never meet. They stay the same distance apart.',
               'Count angles in order: the small ones first.']},
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
                                           {'deg': 150, 'rot': 10, 'label': 'D'}, {'deg': 40, 'rot': 60, 'label': 'E'}, {'deg': 90, 'rot': 100, 'label': 'F'}], 'cols': 3, 'ch': 175, 'width_mm': 134},
    why='A and F fit the checker exactly, so they are right angles. B and E are inside the corner of the checker, so they are smaller. C and D stick out past the corner of the checker, so they are greater.')
u.S(1, 'How many right angles are INSIDE each shape? Check each corner. A dent is greater than a right angle. Do not count it.', parts=[
    P('a', 'Shape A has {b} right angles.', A('5')), P('b', 'Shape B has {b} right angles.', A('6')), P('c', 'Shape C has {b} right angles.', A('4'))],
    figure={'type': 'l3_segs', 'k': 30, 'pad': 20, 'width_mm': 134, 'segs': (
        [[0, 0, 4, 0], [4, 0, 4, 2], [4, 2, 2, 2], [2, 2, 2, 4], [2, 4, 0, 4], [0, 4, 0, 0]] +
        [[x + 6, y, x2 + 6, y2] for x, y, x2, y2 in [(0, 4, 4, 4), (4, 4, 4, 3), (4, 3, 3, 3), (3, 3, 3, 0), (3, 0, 1, 0), (1, 0, 1, 3), (1, 3, 0, 3), (0, 3, 0, 4)]] +
        [[x + 12, y, x2 + 12, y2] for x, y, x2, y2 in [(0, 0, 4, 0), (4, 0, 3, 4), (3, 4, 0, 4), (0, 4, 0, 0)]]),
            'labels': [{'x': 2, 'y': -0.9, 't': 'A'}, {'x': 8, 'y': -0.9, 't': 'B'}, {'x': 13.5, 'y': -0.9, 't': 'C'}]},
    why='Count the corners that fit a checker. Shape A is an L: 5 right angles, and the dent is greater. Shape B has 6 right angles and 2 dents. Shape C has 2 right angles at the bottom left and top left... see the key picture: 2 sloping corners are not right angles.')
