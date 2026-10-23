"""Level 6 Unit 7: Turtle geometry (angles in polygons, turn angles, stars).  Follows holiday lesson 7."""
from lib import *

U = 'L6U07'
I = []
X = '×'
M = '−'
D = '°'
TURN = '↻'


def mv(n):
    return ['move', f'move ({n}) steps']


def tn(a):
    return ['turn', f'turn {TURN} ({a}) degrees']


learn = {
    'intro': 'A turtle moves forward and turns. Going once round a closed shape, it turns 360° in all and faces the way it began. '
             'In a regular polygon with n sides every turn is 360° ÷ n, and the inside angle is 180° − the turn.',
    'example': {
        'problem': 'A turtle draws a regular polygon with 10 sides. Find the turn at each corner and the inside angle.',
        'figure': {'type': 'l6_turtle', 'cmds': [['repeat', 10, [['move', 60], ['turn', 36]]]], 'step_mm': 0.22, 'labels': {'1': '36°'}},
        'steps': ['Going once round, the turtle turns 360° in all.',
                  'There are 10 equal turns: 360° ÷ 10 = 36° at each corner.',
                  f'The turn and the inside angle make a straight line: 180° {M} 36° = 144°.',
                  f'In code: repeat 10 [move 60, turn {TURN} 36].'],
        'answer': 'The turn is 36° and the inside angle is 144°.',
        'side': True},
    'howto': {'title': 'How to find the angles of a regular polygon',
              'steps': ['Going once round, the turtle turns 360° in all.',
                        'Turn = 360° ÷ number of sides.',
                        'Inside angle = 180° − turn.',
                        'Test it in code: repeat (sides) [move, turn].']},
    'try': IT(U, 'L', 1, 0, 'A regular polygon has 9 sides. The turn at each corner is {b}° and the inside angle is {b}°.',
              f'360° ÷ 9 = 40° for the turn. The inside angle is 180° {M} 40° = 140°.',
              answer=A([40, 140], '40°, 140°')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'Complete the table for regular polygons.',
            'Turn = 360 ÷ sides and inside angle = 180 − turn. 5 sides: turn 72, inside 108. 12 sides: turn 30, inside 150. '
            'Turn 18: 360 ÷ 18 = 20 sides, inside 162. Inside 172: turn 8, and 360 ÷ 8 = 45 sides.',
            fig=grid([['5', '', ''], ['12', '', ''], ['', '18°', ''], ['', '', '172°']], [34, 34, 40], head=['Sides', 'Turn', 'Inside angle'], ch=9),
            answer=A(['72', '108', '30', '150', '20', '162', '45', '8'], 'Row 1: 72°, 108°.  Row 2: 30°, 150°.  Row 3: 20 sides, 162°.  Row 4: 45 sides, 8°.', list=True)))
I.append(IT(U, 'S', 2, 1,
            f'Program A: repeat 10 [move 40, turn {TURN} 36].  Program B: repeat 12 [move 40, turn {TURN} 30].  Program C: repeat 6 [move 40, turn {TURN} 30]. '
            'One of them draws a regular polygon with inside angles of 150°.',
            'Inside 150° means a turn of 180° − 150° = 30°, and 360° ÷ 30° = 12 sides: Program B. Program C also turns 30°, but only 6 × 30 = 180° in all. '
            'That is half a turn, so the path does not close.',
            parts=[P('a', 'The program is   {circ:A|B|C}', ['B']),
                   P('b', 'Program C turns {b}° in all, so its path   {circ:closes|does not close}', [180, 'does not close'], '180°, does not close')]))
I.append(IT(U, 'S', 3, 1,
            'Trace the code. Write the total turned after each repeat, and the turn from the start direction (the total with every full 360° taken away).',
            'The total turned grows by 100 each repeat: 100, 200, 300, 400, 500. Take away 360 when the total passes it: 500 − 360 = 140. '
            'The turtle faces 140° from its start direction, not 0°, so it is not facing the way it began.',
            fig=code([['ctl', 'repeat (5)', [mv(40), tn(100)]]], trace={'cols': ['Repeat', 'Total', 'From start'], 'rows': 5, 'first': [1, 2, 3, 4, 5], 'cw': 21, 'ch': 8.5}),
            parts=[P('a', 'After repeat 5 the turn from the start is {b}°.', [140]),
                   P('b', 'Is the turtle facing the way it started?   {circ:Yes|No}', ['No'])],
            partsrow=True))
I.append(IT(U, 'S', 4, 2,
            f'A turtle walks round a closed shape with 5 sides. Its first 4 turns are 60{D}, 85{D}, 110{D} and 50{D}. It faces the way it started when it is back.',
            f'All the turns add to 360{D}. The first 4 add to 60 + 85 + 110 + 50 = 305, so the last turn is 360 {M} 305 = 55{D}. The inside angle there is 180 {M} 55 = 125{D}. '
            f'The 5 inside angles add to 5 {X} 180 {M} 360 = 540{D}.',
            parts=[P('a', 'The last turn is {b}°.', [55]),
                   P('b', 'The inside angle there is {b}°.', [125]),
                   P('c', 'The 5 inside angles add up to {b}°.', [540])],
            partsrow=True, space={'rows': ['Working:']}))
I.append(IT(U, 'S', 5, 2,
            'A regular polygon has 18 sides. Find its angles.',
            f'Turn: 360 ÷ 18 = 20{D}. Inside angle: 180 {M} 20 = 160{D}. All 18 inside angles: 18 {X} 160 = 2880{D}. '
            f'Check with (18 {M} 2) {X} 180 = 16 {X} 180 = 2880.',
            parts=[P('a', 'The turn at each corner is {b}°.', [20]),
                   P('b', 'Each inside angle is {b}°.', [160]),
                   P('c', 'All the inside angles add up to {b}°.', [2880])],
            space={'rows': ['Working:']}))
I.append(IT(U, 'S', 6, 2,
            'A turtle draws a regular shape with 30 sides. Fill in the blanks.',
            f'30 sides need 30 repeats. The turn is 360 ÷ 30 = 12{D}. The inside angle is 180 {M} 12 = 168{D}.',
            fig=code([['ctl', 'repeat ( )', [mv(30), ['turn', f'turn {TURN} ( ) degrees']]]]),
            parts=[P('a', 'repeat {b}', [30]),
                   P('b', 'turn {b} degrees', [12]),
                   P('c', 'Each inside angle is {b}°.', [168])],
            figside=True))
I.append(IT(U, 'S', 7, 2,
            'Circle each turn angle that draws a regular polygon. The number of sides must be a whole number.',
            f'The turn must divide 360 exactly. 360 ÷ 24 = 15 sides, ÷ 30 = 12, ÷ 45 = 8, ÷ 72 = 5 and ÷ 120 = 3 sides. '
            f'360 ÷ 50, 64, 100 and 150 are not whole numbers.',
            fig=grid([['24°', '30°', '45°', '50°', '64°', '72°', '100°', '120°', '150°']], [15] * 9, ch=10),
            answer=A([24, 30, 45, 72, 120], f'24{D}, 30{D}, 45{D}, 72{D}, 120{D}', list=True, unordered=True)))
I.append(IT(U, 'S', 8, 3,
            'A turtle draws a star with 10 points and winds round the centre 3 times. It runs repeat 10 [move 80, turn ↻ ?].',
            f'Going round 3 times, the turtle turns 3 {X} 360 = 1080{D} in all. 1080 ÷ 10 = 108{D} at each point. The angle at each point is 180 {M} 108 = 72{D}.',
            parts=[P('a', 'The total turning is {b}°.', [1080]),
                   P('b', 'Each turn is {b}°.', [108]),
                   P('c', 'The angle at each point is {b}°.', [72])],
            space={'rows': ['Working:']}))
I.append(IT(U, 'S', 9, 3,
            'This code draws a rectangle that is not a square. Predict it.',
            f'The rectangle has 4 right-angle turns: 4 {X} 90 = 360{D}. The turtle walks 100 + 50 + 100 + 50 = 300 steps. With 80 instead of 50: 100 + 80 + 100 + 80 = 360 steps.',
            fig=code([['ctl', 'repeat (2)', [mv(100), tn(90), mv(50), tn(90)]]]),
            parts=[P('a', 'The turtle turns {b}° in all.', [360]),
                   P('b', 'It walks {b} steps in all.', [300]),
                   P('c', 'Change 50 to 80. It walks {b} steps.', [360])],
            figside=True))
I.append(IT(U, 'S', 10, 3,
            'Regular shapes fit around a point when their inside angles add to 360°. Check each group.',
            f'Triangle angle 60: 6 {X} 60 = 360. Square angle 90: 3 {X} 90 = 270, which is less than 360, so there is a gap of 90. Hexagon angle 120: 2 {X} 120 + 2 {X} 60 = 360.',
            parts=[P('a', '6 triangles: {b}°', [360]),
                   P('b', '3 squares: {b}°. Is there a gap?   {circ:Yes|No}', [270, 'Yes'], '270°, Yes'),
                   P('c', '2 hexagons and 2 triangles: {b}°', [360])]))
I.append(IT(U, 'S', 11, 3,
            'Each inside angle is a few times the turn angle. Find the number of sides.',
            f'Turn + inside = 180. If the inside angle is k times the turn, then (k + 1) {X} turn = 180. k = 2: turn 60, so 6 sides. k = 5: turn 30, so 12 sides. k = 8: turn 20, so 18 sides.',
            parts=[P('a', '2 times as big: {b} sides.', [6]),
                   P('b', '5 times as big: {b} sides.', [12]),
                   P('c', '8 times as big: {b} sides.', [18])],
            partsrow=True, space={'rows': ['Working:']}))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            f'A turtle repeats [move 40, turn {TURN} 100] again and again until it first faces the start direction again.',
            f'After k repeats the total turned is 100k. It faces the start direction when 100k is a multiple of 360: 100k = 1800 first, at k = 18 (1800 ÷ 100). '
            f'1800 = 5 {X} 360, so it has turned round 5 times and draws an 18-point star.',
            parts=[P('a', 'It first faces the start direction after {b} repeats.', [18]),
                   P('b', 'By then it has turned {b}° in all.', [1800]),
                   P('c', 'That is {b} full turns.', [5])],
            hint='Try the total turned after 1, 2, 3 ... repeats.', partsrow=True, space={'rows': ['Working:', '']}))
I.append(IT(U, 'T', 2, 4,
            'All the inside angles of a regular polygon total 2340°.',
            f'The sum of the inside angles is (n {M} 2) {X} 180, so n {M} 2 = 2340 ÷ 180 = 13 and n = 15. Each inside angle is 2340 ÷ 15 = 156{D}. The turn is 180 {M} 156 = 24{D}. '
            f'Check: 360 ÷ 24 = 15.',
            parts=[P('a', 'The polygon has {b} sides.', [15]),
                   P('b', 'Each inside angle is {b}°.', [156]),
                   P('c', 'Each turn is {b}°.', [24])],
            hint='What do the inside angles of an n-sided shape add up to?', partsrow=True, space={'rows': ['Working:', '']}))
I.append(IT(U, 'T', 3, 4,
            'A triangle, 2 squares and one more regular polygon fit around a point with no gap. All the sides are the same length.',
            f'The angles are 60 + 90 + 90 = 240. 360 {M} 240 = 120{D} is left. A regular polygon with inside angle 120{D} has turn 60{D}, so 360 ÷ 60 = 6 sides: a hexagon.',
            parts=[P('a', 'The inside angle of the fourth shape is {b}°.', [120]),
                   P('b', 'It has {b} sides.', [6])],
            hint='The angles must add to 360. What is left for the fourth?', space={'rows': ['Working:', '', '']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            'The turtle starts at x = 0, y = 0, facing right. A turn ↻ is clockwise. Up means y gets bigger.',
            f'Right 10, down 20, left 30, up 40 gives x = 10 {M} 30 = {M}20 and y = {M}20 + 40 = 20 after 4 repeats. The next 4 moves are right 50, down 60, left 70, up 80: x = {M}20 + 50 {M} 70 = {M}40 and y = 20 {M} 60 + 80 = 40. '
            f'Every 4 repeats adds {M}20 to x and 20 to y, so after 12 repeats it is at ({M}60, 60).',
            fig=code([['var', 'set n to (10)'], ['ctl', 'repeat (4)', [mv('n'), tn(90), ['var', 'change n by (10)']]]]),
            parts=[P('a', 'After 4 repeats: x = {b}, y = {b}', [-20, 20], f'{M}20, 20'),
                   P('b', 'After 12 repeats: x = {b}, y = {b}', [-60, 60], f'{M}60, 60')],
            hint='Make a table. Write x and y after each repeat.', beyond='Where does it end?'))
I.append(IT(U, 'G', 2, 5,
            'The angle at each point of a star is 180° − the turn. Add up all the point angles.',
            f'5-point star: turn 144, point angle 36, and 5 {X} 36 = 180. 8-point star going round 3 times: turn 135, point angle 45, and 8 {X} 45 = 360. '
            f'10-point star going round 3 times: turn 108, point angle 72, and 10 {X} 72 = 720.',
            parts=[P('a', '5-point star (turn 144°): the 5 point angles add to {b}°.', [180]),
                   P('b', '8-point star, 3 times round: the 8 point angles add to {b}°.', [360]),
                   P('c', '10-point star, 3 times round: each point angle is {b}° and they add to {b}°.', [72, 720], '72°, 720°')],
            hint='Find each turn first. Then subtract it from 180 and multiply.', beyond='Points of a star'))
I.append(IT(U, 'G', 3, 5,
            f'The turtle runs repeat 360 [move 1, turn {TURN} 1].',
            f'360 turns of 1{D} add to 360{D}, one full turn, so the path closes. Inside angle: 180 {M} 1 = 179{D}. The path is 360 steps long. For a circle, the distance round is about 3.14 {X} the distance across, '
            f'so the distance across is about 360 ÷ 3.14 = 114.6, which is 115 to the nearest whole number.',
            parts=[P('a', 'The path is {b} steps long.', [360]),
                   P('b', 'The distance across the shape is about {b} steps (use 3.14, nearest whole number).', [115])],
            hint='The path round the shape is about 3.14 times the distance across.', beyond='A polygon that looks like a circle'))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            f'A regular polygon has 40 sides. Each turn is {{b}}° and each inside angle is {{b}}°.',
            f'360 ÷ 40 = 9{D}. The inside angle is 180 {M} 9 = 171{D}.',
            answer=A([9, 171], '9°, 171°')))
I.append(IT(U, 'C', 2, 6,
            f'A turtle turns 10° at each corner of a regular polygon. The polygon has {{b}} sides.',
            f'360 ÷ 10 = 36 sides.',
            answer=A([36], '36')))
I.append(IT(U, 'C', 3, 6,
            f'A regular polygon has inside angles of 156° each. It has {{b}} sides.',
            f'The turn is 180 {M} 156 = 24{D}, and 360 ÷ 24 = 15 sides.',
            answer=A([15], '15')))
I.append(IT(U, 'C', 4, 6,
            f'A turtle goes round a closed 4-sided shape. Its first 3 turns are 95°, 80° and 105°. The last turn is {{b}}°.',
            f'The turns add to 360. 95 + 80 + 105 = 280, so the last turn is 360 {M} 280 = 80{D}.',
            answer=A([80], '80°')))

write_unit(7, 'Turtle geometry', 'Angles in polygons',
           'I can find the turn angle and the inside angle of a regular polygon. I can predict what a turtle program draws.', learn, I)
