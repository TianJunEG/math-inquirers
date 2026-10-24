"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 7: Turtle Geometry (angles in polygons; pen drawing with turns).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l7.js workbook(): the "Try it first" walk, Start here Q1 to Q5; the Finish page: the Investigation
(p6/content/gaps.json lesson 7) and the exit slip (l7.js lesson.exit); Think harder = the first three l7.js qbank.stretch questions plus the one moved there from Start here
(l7.js moved); Go further = the last three l7.js qbank.challenge questions).  Every answer is recomputed by an INDEPENDENT checker below: a small turtle that walks the drawn program
(corners it stands on, total turning), the angle sum (n - 2) x 180 shared by n corners (so the 360 / n rule never checks itself), and brute force over the number of sides.
build_holiday.py stops if a checker and the printed answer differ.  Scratch is not run in the page.
"""
import itertools, math, os, re, sys
from fractions import Fraction
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..'))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
import w2lib as W2      # noqa: E402
import w4lib as W       # noqa: E402

M = W.MINUS
META = dict(level=6, lesson=7, key='p6', title='Turtle Geometry', workbook_title='TURTLE GEOMETRY', topic='Angles in Polygons', strand='Angles and coding',
            sources=['p6/content/l7.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. The turtle walks forward and turns right (clockwise). The code is drawn as blocks: read it and work out what it does.',
                   'The turn is how far the turtle swings at a corner. The inside angle is the angle inside the shape at that corner: turn + inside angle = 180°. The total turning is all the turns added up.',
                   'Type angles as numbers (you may add the ° sign). Questions with "explain" are for you to check against the worked solution.'])
GE, CG = 'Angles in polygons', 'Coding and angles'

# ---------------------------------------------------------------- the programs as printed (workbook() in l7.js), drawn by the workbook's own blocks()
Q2PROG = [['event', 'when green flag clicked'], ['pen', 'pen down'], ['ctrl', 'repeat {9}', [['motion', 'move {80} steps'], ['motion', 'turn ↻ {120} degrees']]]]
Q3PROG = [['event', 'when green flag clicked'], ['var', 'set {total} to {0}'], ['pen', 'pen down'],
          ['ctrl', 'repeat {9}', [['motion', 'move {150} steps'], ['motion', 'turn ↻ {80} degrees'], ['var', 'change {total} by {80}']]], ['looks', 'say {total}']]
Q2_LABEL = "Ben's program: when green flag clicked, pen down, repeat 9: move 80 steps, turn clockwise 120 degrees."
Q3_LABEL = 'Program: when green flag clicked, set total to 0, pen down, repeat 9: move 150 steps, turn clockwise 80 degrees, change total by 80; then say total.'
_src = open(os.path.join(HERE_, '..', '..', '..', '..', 'p6', 'content', 'l7.js'), encoding='utf-8').read()
for _prog in (Q2PROG, Q3PROG):          # the programs drawn here are the printed ones: every block text must be in the workbook file
    for _blk in _prog:
        assert f"'{_blk[1]}'" in _src, _blk
        for _k in (_blk[2] if len(_blk) > 2 else []):
            assert f"'{_k[1]}'" in _src, _k


def slots(prog):
    """The numbers in the white slots of a program, in reading order (so the checkers read the program as drawn)."""
    out = []
    for blk in prog:
        out += re.findall(r'\{(-?\d+)\}', blk[1])
        if len(blk) > 2:
            out += slots(blk[2])
    return [int(x) for x in out]


Q2_REP, Q2_STEP, Q2_TURN = slots(Q2PROG)
_s3 = slots(Q3PROG)
Q3_REP, Q3_STEP, Q3_TURN = _s3[1], _s3[2], _s3[3]
assert _s3 == [0, 9, 150, 80, 80]


def code2():
    return W.blocks(Q2PROG, Q2_LABEL)


def code3():
    return W.blocks(Q3PROG, Q3_LABEL)


CORNER = W.corner_fig()


def totals(rep, turn):
    """Running total after each repeat, found by walking the turtle (not by multiplying)."""
    return [W.turtle(k, turn)['total'] for k in range(1, rep + 1)]


def row(n):
    inside = W.inside_of_regular(n)
    turn = 180 - inside
    return [W.whole(turn), W.whole(inside), W.whole(n * turn)]


def closes_after(turn, limit=2000):
    return next(r for r in range(1, limit) if W.turtle(r, turn)['home'])


def classify(rep, turn):
    t = W.turtle(rep, turn)
    if t['corners'] == 3 and t['rounds'] > 1:
        return 'An equilateral triangle, drawn 3 times over'
    if t['corners'] == rep and t['rounds'] == 1:
        return f'A regular {rep}-sided polygon'
    if t['corners'] == rep and t['rounds'] > 1:
        return f'A {rep}-point star'
    return 'something else'


def valid_triples():
    """Three regular polygons (3 or more sides each) whose inside angles add up to exactly 360 degrees, found by trying all sizes up to 60 sides."""
    out = set()
    for a in range(3, 61):
        for b in range(a, 61):
            for c in range(b, 61):
                if W.inside_of_regular(a) + W.inside_of_regular(b) + W.inside_of_regular(c) == 360:
                    out.add((a, b, c))
    return sorted(out)


TRIPLES = valid_triples()
GIVEN = (4, 6, 12)
OTHERS = [t for t in TRIPLES if t != GIVEN]
assert GIVEN in TRIPLES and (4, 8, 8) in OTHERS and (3, 12, 12) in OTHERS and len(TRIPLES) == 10


def triple_writings():
    out = []
    for t in OTHERS:
        for p in sorted(set(itertools.permutations(t))):
            out += [','.join(map(str, p)), ' '.join(map(str, p))]
    return out


def inv_table_rows():
    return [[str(t), str(closes_after(t)), str(W.turtle(closes_after(t), t)['rounds']), 'polygon' if W.turtle(closes_after(t), t)['rounds'] == 1 else 'star'] for t in (40, 72, 90, 100, 120, 144, 150)]


ITEMS = [
    # ================= Try it first, and Start here (workbook Lesson 7, Q1 to Q5)
    dict(id='TRYa', tier='core', no='Try it first (a)', type='number', strand=GE, skill='turning once round', answer=4, label='Try (a)',
         q='Imagine you walk a square: take a step forward, turn right by 90°, and repeat until you are back home facing the way you began. How many quarter turns (turns of 90°) do you make?',
         check=lambda: closes_after(90),
         hint='Try it standing up, or sketch the path. Count your turns until you are home and facing the way you started.',
         steps=['A square has 4 corners and you turn right by 90° at each one.', 'So you make 4 quarter turns.'],
         src=['Quarter turns: ____']),
    dict(id='TRYb', tier='core', no='Try it first (b)', type='number', strand=GE, skill='turning once round', answer=360, label='Try (b)',
         q='Imagine you walk a square: take a step forward, turn right by 90°, and repeat until you are back home facing the way you began. How many degrees did you turn altogether?',
         check=lambda: W.turtle(closes_after(90), 90)['total'],
         hint='Each turn is 90°. Add up all the turns you made on the way home.',
         steps=['You turned 90° four times: 90 + 90 + 90 + 90 = 360.', 'That is one full turn.'],
         src=['Degrees altogether: ____']),

    dict(id='1r9', tier='core', no='1 (9 sides)', type='fields', strand=GE, skill='turn and inside angle of a regular polygon', svg=CORNER, label='1 row 9',
         q='Regular polygons. Fill in the row of the table for a regular polygon with 9 sides. (The first row of the table is a triangle: turn 120°, inside angle 60°.)',
         frame='Turn angle {f1}°   Inside angle {f2}°   Sides × turn {f3}', answer=[40, 140, 360], check=lambda: row(9),
         hint='Going once round, the turtle comes home facing the way it started. How far has it turned altogether, and how is that shared between the corners? The inside angle and the turn make a straight line.',
         steps=['Going once round the polygon the turtle turns 360° altogether, shared equally by 9 corners: 360 ÷ 9 = 40°.', f'Inside angle = 180° {M} 40° = 140°.', 'Sides × turn = 9 × 40° = 360°.'],
         src=['Regular polygons. Fill in the table (forwards and backwards).']),
    dict(id='1r10', tier='core', no='1 (10 sides)', type='fields', strand=GE, skill='turn and inside angle of a regular polygon', svg=CORNER, label='1 row 10',
         q='Regular polygons. Fill in the row of the table for a regular polygon with 10 sides.',
         frame='Turn angle {f1}°   Inside angle {f2}°   Sides × turn {f3}', answer=[36, 144, 360], check=lambda: row(10),
         hint='The turn is the same at every corner, and the turns make the whole trip round once. Then the inside angle and the turn make a straight line.',
         steps=['360° shared by 10 corners: 360 ÷ 10 = 36°.', f'Inside angle = 180° {M} 36° = 144°.', 'Sides × turn = 10 × 36° = 360°.'],
         src=['Regular polygons. Fill in the table (forwards and backwards).']),
    dict(id='1r36', tier='core', no='1 (36 sides)', type='fields', strand=GE, skill='turn and inside angle of a regular polygon', svg=CORNER, label='1 row 36',
         q='Regular polygons. Fill in the row of the table for a regular polygon with 36 sides. (In Scratch you would move 10 steps for this one.)',
         frame='Turn angle {f1}°   Inside angle {f2}°   Sides × turn {f3}', answer=[10, 170, 360], check=lambda: row(36),
         hint='Share the whole trip round once between the 36 equal corners. Then use the straight line.',
         steps=['360° shared by 36 corners: 360 ÷ 36 = 10°.', f'Inside angle = 180° {M} 10° = 170°.', 'Sides × turn = 36 × 10° = 360°.'],
         src=['Regular polygons. Fill in the table (forwards and backwards).']),
    dict(id='1rt24', tier='core', no='1 (turn 24°)', type='fields', strand=GE, skill='working backwards from the turn', svg=CORNER, label='1 turn 24',
         q='Regular polygons, backwards. A regular polygon has a turn angle of 24° at each corner. Fill in its row of the table.',
         frame='Sides {f1}   Inside angle {f2}°   Sides × turn {f3}', answer=[15, 156, 360],
         check=lambda: [W.sides_with_turn(24), W.whole(W.inside_of_regular(W.sides_with_turn(24))), W.sides_with_turn(24) * 24],
         hint='How many turns of 24° does the turtle need to come home facing the way it started? The inside angle and the turn make a straight line.',
         steps=['The turns must add up to 360°: 360 ÷ 24 = 15 sides.', f'Inside angle = 180° {M} 24° = 156°.', 'Sides × turn = 15 × 24° = 360°.'],
         src=['Regular polygons. Fill in the table (forwards and backwards).']),
    dict(id='1ri165', tier='core', no='1 (inside 165°)', type='fields', strand=GE, skill='working backwards from the inside angle', svg=CORNER, label='1 inside 165',
         q='Regular polygons, backwards. A regular polygon has an inside angle of 165° at each corner. Fill in its row of the table.',
         frame='Sides {f1}   Turn angle {f2}°   Sides × turn {f3}', answer=[24, 15, 360],
         check=lambda: [W.sides_with_inside(165), W.whole(180 - 165), W.sides_with_inside(165) * 15],
         hint='Start with the straight line: what is the turn? Then how many turns of that size make the trip round once?',
         steps=[f'Turn = 180° {M} 165° = 15°.', 'The turns add up to 360°: 360 ÷ 15 = 24 sides.', 'Sides × turn = 24 × 15° = 360°.'],
         src=['Regular polygons. Fill in the table (forwards and backwards).']),
    dict(id='1a', tier='core', no='1(a)', type='selfcheck', strand=GE, skill='explaining the 360 total', label='1(a)',
         q='Regular polygons. Look at the last column of your table (sides × turn). What do you notice, and why does this happen? Write your reason, then check it against the worked solution.',
         facts=[360], check=lambda: sorted({row(n)[2] for n in (3, 9, 10, 36)} | {W.sides_with_turn(24) * 24, W.sides_with_inside(165) * 15}),
         sol_fig=lambda f: W.table_svg(['Sides', 'Turn', 'Inside', 'Sides × turn'], [[str(n), f'{row(n)[0]}°', f'{row(n)[1]}°', f'{row(n)[2]}°'] for n in (3, 9, 10, 15, 24, 36)],
                                       'The table: every row has sides times turn equal to 360 degrees', [64, 64, 70, 100], 15, 28),
         hint='Look at the whole column. Is the number the same each time? Think about where the turtle is at the end of the trip.',
         steps=['Every row gives 360°.', 'Going once round a closed shape, the turtle ends where it began, facing the way it began. That is exactly one full turn, 360°.', 'The turns at all the corners add up to that full turn, so sides × turn = 360° every time.'],
         src=['What do you notice about the last column? Why does this happen?']),
    dict(id='1b', tier='core', no='1(b)', type='choice', strand=GE, skill='is this inside angle possible', options=['Yes, she is right', 'No, she is not right'], answer='No, she is not right', label='1(b)',
         svg=CORNER, q='Mei says a regular polygon can have inside angles of 130°. Is she right?',
         check=lambda: 'Yes, she is right' if W.sides_with_inside(130) is not None else 'No, she is not right',
         hint='Find the turn that goes with an inside angle of 130°. Could the turtle come home after a whole number of those turns?',
         steps=[f'Turn = 180° {M} 130° = 50°.', '360 ÷ 50 = 7.2. A polygon cannot have 7.2 sides.', 'So no regular polygon has inside angles of 130°.'],
         src=['Mei says a regular polygon can have inside angles of 130°. Is she right? Explain.']),
    dict(id='1b-why', tier='core', no='1(b) explain', type='selfcheck', strand=GE, skill='explaining with the turn', label='1(b) why', svg=CORNER,
         q='Mei says a regular polygon can have inside angles of 130°. Explain whether she is right. Write your reason, then check it against the worked solution.',
         facts=dict(turn=50, sides=7.2), check=lambda: dict(turn=180 - 130, sides=360 / (180 - 130)),
         hint='Use the straight line to find the turn. Then think about how many turns the turtle needs to make one full turn.',
         steps=[f'The turn at each corner would be 180° {M} 130° = 50°.', 'The turns must add up to 360°, so the polygon would have 360 ÷ 50 = 7.2 sides.', 'The number of sides must be whole, so Mei is not right.'],
         src=['Mei says a regular polygon can have inside angles of 130°. Is she right? Explain.']),

    dict(id='2a', tier='core', no='2(a)', type='choice', strand=CG, skill='predicting what a turtle program draws', svg=code2(), label='2(a)',
         options=['A regular nonagon', 'An equilateral triangle, drawn 3 times over', 'A regular hexagon', 'A 9-point star'], answer='An equilateral triangle, drawn 3 times over',
         q='Ben wants a regular nonagon (9 sides). Predict what his program draws. What does the turtle draw?',
         check=lambda: classify(Q2_REP, Q2_TURN),
         hint='Look at the turn. Where is the turtle after 3 moves? Then what does it do on moves 4 to 9?',
         steps=[f'Each turn is 120°. After 3 moves the turtle has turned 360° and is back where it started, facing the way it started.', 'Moves 4 to 9 repeat the same triangle twice more.', 'So it draws an equilateral triangle, 3 times over.'],
         sol_fig=lambda f: W.star_fig(3, 1, 'An equilateral triangle: the turtle goes round it 3 times', labels=False),
         src=['Ben wants a regular nonagon (9 sides). Predict what his program draws']),
    dict(id='2a-why', tier='core', no='2(a) explain', type='selfcheck', strand=CG, skill='explaining with the total turning', svg=code2(), label='2(a) why',
         q="Ben wants a regular nonagon (9 sides). Explain what his turtle really draws. Write your reason, then check it against the worked solution.",
         facts=dict(corners=3, rounds=3), check=lambda: dict(corners=W.turtle(Q2_REP, Q2_TURN)['corners'], rounds=W.whole(W.turtle(Q2_REP, Q2_TURN)['rounds'])),
         hint='Follow the turtle for a few moves. How far has it turned after 3 moves? Where is it then?',
         steps=['Each corner turns the turtle by 120°, so after 3 moves it has turned 360° and is back at the start, facing the way it began.', 'The next moves go over the same triangle again, so only 3 corners are ever used and the triangle is drawn 3 times.'],
         src=['What does the turtle draw? Explain.']),
    dict(id='2b', tier='core', no='2(b)', type='number', strand=CG, skill='total turning', svg=code2(), label='2(b)', answer=1080,
         q="What is the total turning of Ben's program (all the turns added up)?", check=lambda: W.turtle(Q2_REP, Q2_TURN)['total'],
         hint='How many turns does the program make, and how big is each one?',
         steps=['The program makes 9 turns of 120° each.', '9 × 120° = 1080°.', '1080° is 3 full turns.'],
         src=['Total turning  ________ °']),
    dict(id='2c', tier='core', no='2(c)', type='fields', strand=CG, skill='fixing a program', svg=code2(), label='2(c)',
         q='Fix it so that Ben\'s program draws a regular nonagon. Which number must change, and what must it change to?',
         frame='Change the turn from {f1} to {f2}', answer=[120, 40],
         check=lambda: [Q2_TURN, next(t for t in range(1, 360) if W.turtle(Q2_REP, t)['corners'] == Q2_REP and W.turtle(Q2_REP, t)['rounds'] == 1)],
         hint='The nonagon has 9 equal corners. The turtle should turn one full turn altogether. How much is each turn?',
         steps=['The repeat 9 and the move stay the same. Only the turn changes.', 'Nine equal turns make one full turn of 360°: 360 ÷ 9 = 40.', 'Change the turn from 120 to 40.'],
         src=['(c) Fix it: change']),

    dict(id='3r1', tier='core', no='3 rows 4-6', type='fields', strand=CG, skill='tracing a running total', svg=code3(), label='3 rows 4-6',
         q='Trace the code. The program keeps a running total of how far the turtle has turned. The table is done for you for repeats 1 to 3: after repeat 1 the total is 80, after repeat 2 it is 160 and after repeat 3 it is 240. What is the total after the next three repeats?',
         frame='After repeat 4: {f1}   after repeat 5: {f2}   after repeat 6: {f3}', answer=[320, 400, 480], check=lambda: totals(Q3_REP, Q3_TURN)[3:6],
         hint='Each repeat adds the same amount to the total. Carry on from 240.',
         steps=['Each repeat changes total by 80.', '240 + 80 = 320, 320 + 80 = 400, 400 + 80 = 480.'],
         src=['Trace the code. The program keeps a running total of how far the turtle has turned.']),
    dict(id='3r2', tier='core', no='3 rows 7-9', type='fields', strand=CG, skill='tracing a running total', svg=code3(), label='3 rows 7-9',
         q='Trace the code. The program keeps a running total of how far the turtle has turned. After repeat 6 the total is 480. What is the total after repeats 7, 8 and 9?',
         frame='After repeat 7: {f1}   after repeat 8: {f2}   after repeat 9: {f3}', answer=[560, 640, 720], check=lambda: totals(Q3_REP, Q3_TURN)[6:9],
         hint='Keep adding the amount that "change total by" adds each time.',
         steps=['480 + 80 = 560, 560 + 80 = 640, 640 + 80 = 720.'],
         src=['Trace the code. The program keeps a running total of how far the turtle has turned.']),
    dict(id='3a', tier='core', no='3(a)', type='number', strand=CG, skill='tracing code', svg=code3(), label='3(a)', answer=720,
         q='Trace the code. At the end the sprite says the total. What does it say?', check=lambda: totals(Q3_REP, Q3_TURN)[-1],
         hint='The sprite says the last value of total, after all the repeats.',
         steps=['After the 9th repeat the total is 720.', 'The sprite says 720.'],
         src=['The sprite says  ________']),
    dict(id='3b', tier='core', no='3(b)', type='number', strand=CG, skill='times round', svg=code3(), label='3(b)', answer=2,
         q='Trace the code. How many times does the turtle go round (how many full turns does it make altogether)?', check=lambda: W.whole(W.turtle(Q3_REP, Q3_TURN)['rounds']),
         hint='How many degrees is one full turn? How many full turns fit into the total turning?',
         steps=['One full turn is 360°.', '720 ÷ 360 = 2.', 'The turtle goes round 2 times.'],
         src=['Times the turtle goes round  ________']),
    dict(id='3c', tier='core', no='3(c)', type='choice', strand=CG, skill='what shape does the code draw', svg=code3(), label='3(c)',
         options=['A regular nonagon', 'A 9-point star', 'A hexagon', 'A triangle'], answer='A 9-point star',
         q='Trace the code. It draws a ... ?', check=lambda: classify(Q3_REP, Q3_TURN),
         hint='Look at the turn and the number of repeats. Does the turtle visit 9 different corners? Does it go round once or more than once?',
         steps=['It makes 9 moves and visits 9 different corners.', 'It goes round 2 times, not once, so the corners are not next to each other: it is a star, not a polygon.', 'It draws a 9-point star.'],
         sol_fig=lambda f: W.star_fig(9, 2, 'The 9-point star: every 2nd dot joined', labels=False),
         src=['It draws a  __________________']),
    dict(id='3d', tier='core', no='3(d)', type='number', strand=CG, skill='point angle of a star', svg=code3(), label='3(d)', answer=100,
         q='Trace the code. What is the angle at each point of the shape? (Point angle = 180° − turn.)', check=lambda: 180 - Q3_TURN,
         hint='The turn at each corner is in the program. Use the straight line.',
         steps=[f'The turn is 80°.', f'Point angle = 180° {M} 80° = 100°.'],
         src=['Point angle  ________ °']),

    dict(id='4t', tier='core', no='4', type='fields', strand=GE, skill='planning a star', label='4',
         svg=W.two_rings(5, 2, 9, 0, '5 points, 2 times round', '9 points', 'Left: a 5-point star already drawn by joining every second dot of 5 dots. Right: 9 dots numbered 0 to 8 round a circle.'),
         q='Plan a star, then test it (move 120 for the 9-point star). Turn = 360° × times round ÷ points. Point angle = 180° − turn. The 5-point star goes round 2 times: total turning 720°, turn 144°, point angle 36°. Now fill in the 9-point star that goes round 4 times.',
         frame='Total turning {f1}°   Turn angle {f2}°   Point angle {f3}°', answer=[1440, 160, 20],
         check=lambda: (lambda t: [t['total'], W.whole(Fraction(t['total'], 9)), 180 - W.whole(Fraction(t['total'], 9))])(W.turtle(9, 160)),
         hint='Total turning = 360° × the number of times round. Share it between the 9 corners to get the turn. Then use the straight line.',
         steps=['Total turning = 4 × 360° = 1440°.', 'Turn = 1440° ÷ 9 = 160°.', f'Point angle = 180° {M} 160° = 20°.', '(Check: a turn of 160° visits 9 different corners and goes round 4 times.)'],
         src=['Plan a star, then test it (move 120 for the 9-point star). Fill in the 9-point row.']),
    dict(id='4d', tier='core', no='4 (draw)', type='selfcheck', paper=True, strand=GE, skill='drawing a star', label='4 draw',
         svg=W.two_rings(5, 2, 9, 0, '5 points, 2 times round', '9 points', 'Left: a 5-point star already drawn by joining every second dot of 5 dots. Right: 9 dots numbered 0 to 8 round a circle.'),
         q='Draw your 9-point star (the one that goes round 4 times) by joining the 9 dots. The 5-point star on the left joins every 2nd dot.',
         facts=dict(dots=9, step=4), check=lambda: dict(dots=9, step=next(k for k in range(1, 9) if W.turtle(9, 40 * k)['rounds'] == 4)),
         sol_fig=lambda f: W.star_fig(f['dots'], f['step'], 'The 9-point star: every 4th dot joined', labels=True),
         hint='The 5-point star goes round 2 times and joins every 2nd dot. How many times round is your star?',
         steps=['The star goes round 4 times, so join every 4th dot: 0 to 4, 4 to 8, 8 to 3, and so on.', 'After 9 lines you are back at dot 0 and every dot has been used.'],
         src=['9 points: draw your star']),

    dict(id='5ang', tier='core', no='5 inside angles', type='fields', strand=GE, skill='inside angles of regular polygons', label='5 each', svg=CORNER,
         q='Add up the inside angles of regular polygons. Fill in the inside angle of each regular polygon. (Use your table from Q1 for 10 sides.)',
         frame='3 sides: {f1}°   4 sides: {f2}°   5 sides: {f3}°   6 sides: {f4}°   10 sides: {f5}°', answer=[60, 90, 108, 120, 144],
         check=lambda: [W.whole(W.inside_of_regular(n)) for n in (3, 4, 5, 6, 10)],
         hint='For each shape, find the turn first, then use the straight line.',
         steps=['3 sides: turn 120°, inside 60°. 4 sides: turn 90°, inside 90°.', '5 sides: turn 72°, inside 108°. 6 sides: turn 60°, inside 120°.', '10 sides: turn 36°, inside 144°.'],
         src=['Add up the inside angles of regular polygons (use Q1 for 10 sides).']),
    dict(id='5sum', tier='core', no='5 all added', type='fields', strand=GE, skill='angle sum of a polygon', label='5 added', svg=CORNER,
         q='Add up the inside angles of regular polygons. Fill in what ALL the inside angles of each regular polygon add up to.',
         frame='3 sides: {f1}°   4 sides: {f2}°   5 sides: {f3}°   6 sides: {f4}°   10 sides: {f5}°', answer=[180, 360, 540, 720, 1440],
         check=lambda: [W.whole(n * W.inside_of_regular(n)) for n in (3, 4, 5, 6, 10)],
         hint='Each inside angle is the same. How many inside angles are there in each shape?',
         steps=['3 × 60° = 180°. 4 × 90° = 360°. 5 × 108° = 540°.', '6 × 120° = 720°. 10 × 144° = 1440°.'],
         src=['Add up the inside angles of regular polygons (use Q1 for 10 sides).']),
    dict(id='5a', tier='core', no='5(a)', type='number', strand=GE, skill='pattern in the angle sum', label='5(a)', answer=180,
         q='Add up the inside angles of regular polygons. Each time the polygon gets one more side, the total of the inside angles goes up. By how many degrees?',
         check=lambda: (lambda d: d.pop() if len(d) == 1 else None)({W.whole((n + 1) * W.inside_of_regular(n + 1) - n * W.inside_of_regular(n)) for n in range(3, 40)}),
         hint='Look at the row you filled in for 3, 4, 5 and 6 sides. How much bigger is each answer than the one before?',
         steps=['The totals for 3, 4, 5 and 6 sides are 180°, 360°, 540°, 720°.', 'Each is 180° more than the one before.'],
         src=['One more side adds  ______ °']),
    dict(id='5b', tier='core', no='5(b)', type='text', algebra=True, var='n', strand=GE, skill='rule for the angle sum', label='5(b)',
         q='Add up the inside angles of regular polygons. For a polygon with n sides, write the total of all its inside angles as a rule with n (type just the rule, like 3n + 1, which is a different rule; do not type "total =").',
         accept=W2.verified_forms(['(n-2)*180', '(n - 2) × 180', '180*(n-2)', '180(n-2)', '180×(n-2)', '(n-2)×180', '180n-360', 'n*180-360', 'n × 180 - 360', '180 × n - 360'], lambda n: (n - 2) * 180),
         shown='(n − 2) × 180', check=lambda: '(n-2)*180' if all(W.whole(k * W.inside_of_regular(k)) == (k - 2) * 180 for k in range(3, 60)) else None,
         hint='Look at the totals for 3, 4, 5 and 6 sides. Each side adds the same amount. What is the total for 2 sides, if the pattern carried on?',
         steps=['The total goes up by 180° for each side, and a 3-sided shape gives 180°.', 'So the total is (n − 2) × 180°.', 'Check: n = 6 gives 4 × 180° = 720°. Another way to write it: n × 180° − 360°.'],
         src=['For n sides:  total = ______________']),

    dict(id='Xa', tier='core', no='Exit slip (a)', type='number', strand=GE, skill='sides from the turn', label='Exit (a)', answer=72,
         q='A turtle draws a regular polygon and turns 5° at every corner. How many sides does the polygon have?', check=lambda: W.sides_with_turn(5),
         hint='The turtle must turn one full turn altogether. How many turns of 5° is that?',
         steps=['360° ÷ 5° = 72.', 'The polygon has 72 sides.'],
         src=['A turtle draws a regular polygon and turns 5° at every corner. How many sides does the polygon have? What is each inside angle?']),
    dict(id='Xb', tier='core', no='Exit slip (b)', type='number', strand=GE, skill='inside angle from the turn', label='Exit (b)', answer=175,
         q='A turtle draws a regular polygon and turns 5° at every corner. What is each inside angle?', check=lambda: W.whole(W.inside_of_regular(W.sides_with_turn(5))),
         hint='The turn and the inside angle make a straight line.',
         steps=[f'Inside angle = 180° {M} 5° = 175°.'],
         src=['A turtle draws a regular polygon and turns 5° at every corner. How many sides does the polygon have? What is each inside angle?']),

    # ================= Investigation (printed on the Finish page)
    dict(id='I0', tier='invest', no='Investigation first step', type='fields', strand=CG, skill='repeats until the turtle is home', label='Inv first',
         q='What if the turn changes? A turtle repeats [move 100, turn ↻ 90]. How many repeats until it first faces the way it started, and how many times has it gone round by then?',
         frame='Repeats {f1}   times round {f2}', answer=[4, 1], check=lambda: [closes_after(90), W.whole(W.turtle(closes_after(90), 90)['rounds'])],
         hint='Add up the turns, 90, 180, ... until the total is a whole number of full turns.',
         steps=['4 turns of 90° add up to 360°, one full turn.', 'The turtle needs 4 repeats and has gone round once.'],
         src=['First step: a turtle repeats [move 100, turn 90]. How many repeats until it faces the way it started?']),
] + [
    dict(id=f'I{t}', tier='invest', no=f'Investigation t = {t}', type='fields', strand=CG, skill='repeats until the turtle is home', label=f'Inv t {t}',
         q=f'What if the turn changes? A turtle repeats [move 100, turn ↻ {t}] until it first faces the way it started. How many repeats, and how many times does it go round?',
         frame='Repeats {f1}   times round {f2}', answer=[closes_after(t), W.whole(W.turtle(closes_after(t), t)['rounds'])],
         check=(lambda t=t: [next(r for r in range(1, 2000) if (r * t) % 360 == 0), W.whole(Fraction(next(r for r in range(1, 2000) if (r * t) % 360 == 0) * t, 360))]),
         hint='Keep adding the turn until the total is a multiple of 360 (a whole number of full turns).',
         steps=[f'Add {t}° again and again until the total is a multiple of 360°.', f'{closes_after(t)} × {t}° = {closes_after(t) * t}°, which is {W.whole(W.turtle(closes_after(t), t)["rounds"])} full turn' + ('s' if W.turtle(closes_after(t), t)['rounds'] != 1 else '') + '.'],
         src=['Make a table for t = 40, 72, 90, 100, 120, 144 and 150: how many repeats, and how many times does it go round?'])
    for t in (40, 72, 100, 120, 144, 150)
] + [
    dict(id='Iex', tier='invest', no='Investigation notice', type='selfcheck', strand=CG, skill='what changes, what stays the same', label='Inv notice',
         q='Look at your table for t = 40, 72, 90, 100, 120, 144 and 150. What changes when t changes? What stays the same? Write your answer, then check it against the worked solution.',
         facts=[(t, closes_after(t)) for t in (40, 72, 90, 100, 120, 144, 150)], check=lambda: [(t, closes_after(t)) for t in (40, 72, 90, 100, 120, 144, 150)],
         sol_fig=lambda f: W.table_svg(['Turn t', 'Repeats', 'Times round', 'Shape'], inv_table_rows(), 'For each turn t: the repeats, the times round and the shape drawn', [60, 78, 102, 84], 15, 28),
         hint='Compare the rows. What do repeats × t always make? When does the turtle go round only once?',
         steps=['What changes: the number of repeats and the shape (a polygon when the turtle goes round once, a star when it goes round more than once).', 'What stays the same: the turns always add up to a whole number of full turns, so repeats × t = 360 × times round.',
                'When t divides 360 the turtle goes round once and draws a polygon; otherwise it goes round more than once and draws a star.'],
         src=['What changes when t changes? What stays the same?']),

    # ================= Think harder (first three Think harder questions, then the one moved from Start here)
    dict(id='T1', tier='stretch', no='T1', type='number', strand=GE, skill='sides from a ratio of angles', answer=10, label='T1',
         q='Each inside angle of a regular polygon is 4 times its turn angle. How many sides does the polygon have?',
         check=lambda: next(n for n in range(3, 400) if W.inside_of_regular(n) == 4 * (180 - W.inside_of_regular(n))),
         hint='The turn and the inside angle make 180°. If the inside angle is 4 times the turn, how many equal parts is 180° split into?',
         steps=['Turn + 4 × turn = 180°, so 5 equal parts make 180° and one part (the turn) is 36°.', '360 ÷ 36 = 10 sides.', '(Check: the inside angle is 144°, which is 4 × 36°.)'],
         src=['Each inside angle of a regular polygon is 4 times its turn angle. How many sides does the polygon have?']),
    dict(id='T2', tier='stretch', no='T2', type='number', strand=GE, skill='angle sum from an inside angle', answer=1260, label='T2',
         q='Each inside angle of a regular polygon is 140°. What do all its inside angles add up to?',
         check=lambda: W.whole(W.sides_with_inside(140) * W.inside_of_regular(W.sides_with_inside(140))),
         hint='First find how many sides there are. The turn and the inside angle make a straight line.',
         steps=[f'Turn = 180° {M} 140° = 40°, so there are 360 ÷ 40 = 9 sides.', '9 × 140° = 1260°.', '(Check: (9 − 2) × 180° = 1260°.)'],
         src=['Each inside angle of a regular polygon is 140°. What do all its inside angles add up to?']),
    dict(id='T3', tier='stretch', no='T3', type='fields', strand=GE, skill='the last turn of a shape', label='T3',
         q="Mei's turtle draws a shape with 4 sides. Its first three turns are 70°, 100° and 90°. It comes home facing the same way after going round once. What is its last turn, and what is the inside angle at that corner?",
         frame='Last turn {f1}°   inside angle {f2}°', answer=[100, 80],
         check=lambda: (lambda last: [last, 180 - last])(next(x for x in range(1, 360) if 70 + 100 + 90 + x == 360)),
         hint='Going round once, all the turns add up to one full turn. How much of the full turn is left? Then use the straight line.',
         steps=[f'The four turns add up to 360°: 70 + 100 + 90 = 260, and 360 {M} 260 = 100.', f'The last turn is 100°.', f'Inside angle = 180° {M} 100° = 80°.'],
         src=["Mei's turtle draws a shape with 4 sides. Its first three turns are 70°, 100° and 90°."]),
    dict(id='T4a', tier='stretch', no='T4(a)', type='fields', strand=GE, skill='planning a star', label='T4 (a)',
         q='Plan a 20-point star that goes round 3 times (move 100). Find the total turning, the turn angle and the point angle.',
         frame='Total turning {f1}°   turn angle {f2}°   point angle {f3}°', answer=[1080, 54, 126],
         check=lambda: (lambda t: [t, W.whole(Fraction(t, 20)), 180 - W.whole(Fraction(t, 20))])(3 * 360),
         hint='Total turning = 360° × times round. Share it between the corners. Then use the straight line.',
         steps=['Total turning = 3 × 360° = 1080°.', 'Turn = 1080° ÷ 20 = 54°.', f'Point angle = 180° {M} 54° = 126°.'],
         src=['Plan a 20-point star that goes round 3 times (move 100). Find the total turning, the turn angle and the point angle.']),
    dict(id='T4b', tier='stretch', no='T4(b)', type='choice', strand=GE, skill='comparing point angles', label='T4 (b)',
         options=['The 20-point star', 'The 9-point star in Q4'], answer='The 9-point star in Q4',
         q='Which has sharper points: the 20-point star that goes round 3 times, or the 9-point star that goes round 4 times (Q4)? A sharper point has a smaller point angle.',
         check=lambda: 'The 20-point star' if 180 - Fraction(3 * 360, 20) < 180 - Fraction(4 * 360, 9) else 'The 9-point star in Q4',
         hint='Find the point angle of each star. Which is smaller?',
         steps=[f'The 20-point star has point angle 180° {M} 54° = 126°.', f'The 9-point star has point angle 180° {M} 160° = 20°.', '20° is smaller than 126°, so the 9-point star has sharper points.'],
         src=['Which has sharper points, this star or the 9-point star in Q4?']),

    # ================= Go further (last three Go further questions)
    dict(id='C1', tier='challenge', no='C1', type='selfcheck', open=True, marking_mode='open', strand=GE, skill='designing a star', label='C1',
         svg=W.two_rings(9, 0, 20, 0, '9 dots', '20 dots', 'Two circles of dots to draw stars on: 9 dots numbered 0 to 8, and 20 dots with every fifth one numbered.', r=52, every2=5),
         q='Design your own star. Choose the number of points p and how many times it goes round, k, so that the turn angle 360° × k ÷ p is a WHOLE number and p and k share no common factor. Give the turn angle, the point angle (180° − turn) and the code. Explain why your star closes after p repeats. Then compare with the example in the worked solution.',
         sol_fig=lambda f: W.star_fig(8, 3, 'Example: 8 points, every 3rd dot joined', labels=True),
         hint='Try p = 8 or 12 or 10 and a k that is smaller than p. Check that 360 × k ÷ p is a whole number. Does k share a factor with p?',
         steps=['Open: many stars work. Example: 8 points going round 3 times: turn = 360 × 3 ÷ 8 = 135°, point angle 45°; code repeat 8 [move 100, turn ↻ 135].', 'After 8 repeats it has turned 8 × 135° = 1080° = 3 full turns, so it faces the way it started and the star closes.',
                'If p and k share a factor, the star closes sooner and is a smaller shape repeated (for example 9 points going round 3 times is just a triangle).'],
         src=['Design your own star. Choose the number of points p and how many times it goes round, k']),
    dict(id='C2', tier='challenge', no='C2', type='text', strand=GE, skill='regular polygons round a point', label='C2',
         accept=triple_writings(), shown='4, 8, 8',
         q='A square, a hexagon and a 12-sided shape fit exactly around a point: 90° + 120° + 150° = 360°. Find one other set of three regular polygons whose inside angles add up to 360° (hint: the answer uses a square or a triangle). Type the number of sides of each polygon, for example 5, 7, 9 (that is not a right set).',
         check=lambda: '4,8,8' if '4,8,8' in triple_writings() and all(W.inside_of_regular(a) + W.inside_of_regular(b) + W.inside_of_regular(c) == 360 for a, b, c in OTHERS) else None,
         sol_fig=lambda f: W.table_svg(['Polygons', 'Inside angles', 'Total'], [['4, 8, 8', '90° + 135° + 135°', '360°'], ['3, 12, 12', '60° + 150° + 150°', '360°']], 'Two sets that work: square, octagon, octagon and triangle, 12-gon, 12-gon', [90, 150, 60], 15, 30),
         hint='Find the inside angle of a square (or a triangle). What is left to share between the other two polygons? Try making them the same.',
         steps=['A square has inside angle 90°, so the other two must add up to 270°. Two equal polygons would have 135° each: that is a regular octagon.', 'So square + octagon + octagon: 90° + 135° + 135° = 360°.', 'Or triangle + 12-gon + 12-gon: 60° + 150° + 150° = 360°.',
                'Other sets also work, such as ' + ', '.join('(' + ', '.join(map(str, t)) + ')' for t in OTHERS if t not in ((4, 8, 8), (3, 12, 12))) + ' sides.'],
         src=['A square, a hexagon and a 12-sided shape fit exactly around a point']),
    dict(id='C3a', tier='challenge', no='C3(a)', type='choice', strand=CG, skill='hexagon or triangle', label='C3 (a)',
         options=['Turn 60', 'Turn 120'], answer='Turn 60',
         q='A turtle runs repeat 6 [move 100, turn ↻ turn] with the turn 120 or the turn 60. Which turn draws a hexagon?',
         check=lambda: next(f'Turn {t}' for t in (60, 120) if W.turtle(6, t)['corners'] == 6 and W.turtle(6, t)['rounds'] == 1),
         hint='A hexagon has 6 equal corners and the turtle goes round it once. Test each turn: how far has the turtle turned altogether after 6 repeats?',
         steps=['Turn 60: 6 × 60° = 360°, one full turn, so it draws a hexagon.', 'Turn 120: 6 × 120° = 720°, two full turns.'],
         sol_fig=lambda f: W.two_rings(6, 1, 6, 2, 'turn 60', 'turn 120', 'Left: a hexagon, joining every dot to the next. Right: a triangle, joining every second dot', r=48, labels1=False, labels2=False),
         src=['Try turn 120 and turn 60 with repeat 6 and move 100. Which one draws a hexagon?']),
    dict(id='C3b', tier='challenge', no='C3(b)', type='selfcheck', strand=CG, skill='explaining why not a star', label='C3 (b)',
         q='A turtle runs repeat 6 [move 100, turn ↻ 120]. It does not make a 6-point star. Explain why not. Write your reason, then check it against the worked solution.',
         facts=dict(corners=3, rounds=2), check=lambda: dict(corners=W.turtle(6, 120)['corners'], rounds=W.whole(W.turtle(6, 120)['rounds'])),
         hint='Follow the turtle. After how many moves is it back at the start, facing the way it began? How many different corners does it stand on?',
         steps=['Turn 120 makes 6 × 120° = 720°, two full turns.', 'But the turtle is back at the start after only 3 moves, so it only visits 3 corners and draws a triangle twice over.', 'A 6-point star needs 6 different corners.'],
         src=['Why does the other not make a 6-point star?']),
]

for _it in ITEMS:
    if _it.get('frame'):
        _it['frame'] = W.nb(_it['frame'])

P.finish(ITEMS)

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
VARIANTS = {
    '2b': dict(base=dict(n=9, t=120),
               tpl=dict(vars=dict(n=[3, 4, 5, 6, 8, 9, 10, 12], t=[40, 45, 60, 72, 90, 100, 120, 150]),
                        q='A turtle runs: repeat {n} [move 80, turn ↻ {t} degrees]. What is the total turning (all the turns added up)?', answer='n*t',
                        hint='How many turns does the program make, and how big is each one?',
                        steps=['The program makes {n} turns of {t}° each.', '{n} × {t}° = {ans}°.']),
               oracle=lambda e: W.turtle(e['n'], e['t'])['total']),
    'Xa': dict(base=dict(t=5),
               tpl=dict(vars=dict(t=[5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90]),
                        q='A turtle draws a regular polygon and turns {t}° at every corner. How many sides does the polygon have?', answer='360//t',
                        hint='The turtle must turn one full turn altogether. How many turns of {t}° is that?',
                        steps=['360° ÷ {t}° = {ans}.', 'The polygon has {ans} sides.']),
               oracle=lambda e: W.sides_with_turn(e['t'])),
    'Xb': dict(base=dict(t=5),
               tpl=dict(vars=dict(t=[5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90]),
                        q='A turtle draws a regular polygon and turns {t}° at every corner. What is each inside angle?', answer='180-t',
                        hint='The turn and the inside angle make a straight line.',
                        steps=['Inside angle = 180° − {t}° = {ans}°.']),
               oracle=lambda e: W.whole(W.inside_of_regular(W.sides_with_turn(e['t'])))),
    'T1': dict(base=dict(k=4),
               tpl=dict(vars=dict(k=[1, 2, 3, 4, 5, 8, 9, 11, 17]),
                        q='Each inside angle of a regular polygon is {k} times its turn angle. How many sides does the polygon have?', answer='2*(k+1)',
                        hint='The turn and the inside angle make 180°. If the inside angle is {k} times the turn, how many equal parts is 180° split into?',
                        steps=['Turn + {k} × turn = 180°, so ({k} + 1) equal parts make 180°.', 'The turn is 180° ÷ ({k} + 1), and 360° ÷ that turn = {ans} sides.']),
               oracle=lambda e: next(n for n in range(3, 400) if W.inside_of_regular(n) == e['k'] * (180 - W.inside_of_regular(n)))),
    'T2': dict(base=dict(a=140),
               tpl=dict(vars=dict(a=[108, 120, 135, 140, 144, 150, 156, 160, 162, 165, 168, 170]), derive=dict(t='180-a', n='360//(180-a)'),
                        q='Each inside angle of a regular polygon is {a}°. What do all its inside angles add up to?', answer='n*a',
                        hint='First find how many sides there are. The turn and the inside angle make a straight line.',
                        steps=['Turn = 180° − {a}° = {t}°.', 'The turns add up to 360°, so there are 360 ÷ {t} = {n} sides.', '{n} × {a}° = {ans}°.']),
               oracle=lambda e: W.whole(W.sides_with_inside(e['a']) * W.inside_of_regular(W.sides_with_inside(e['a'])))),
}
