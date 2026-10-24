"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 8: Angle and Line Detectives (Angles, perpendicular and parallel lines).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l8.js: Start here = the lesson's workbook()
pages; Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Extra question = deck.takeHome (printed as "Take-home");
the Investigation = p3/gifted.json lesson 8).  Every answer is recomputed by an INDEPENDENT checker below (the size of each angle from its arms, the corners of each
outline, every pair of lines of each letter, the right angles at every meeting point, the staircase outlines, every six-sided shape on a small lattice, the hands of
the clock), never a copy of the printed answer; build_holiday.py stops if a checker and the printed answer differ.  The figures are the workbook's own data
(p3/content/l8.js: the six angles, the four shapes, the fan of lines, the letters, the grid with the lines, the window; p3/figs_l3.js is the source of the clocks),
drawn larger, one angle / shape / letter per card; the checks just below stop the build if the data here differs from the printed figures.
"""
import itertools, os, re, sys
from math import gcd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p3lib import *         # noqa: E402,F401
from p3lib_w4 import *      # noqa: E402,F401

META = dict(level=3, lesson=8, key='p3', title='Angle and Line Detectives', workbook_title='ANGLE AND LINE DETECTIVES', topic='Angles, Perpendicular and Parallel Lines', strand='Angles and lines',
            sources=['p3/content/l8.js', 'p3/gifted.json'],
            intro=['A right angle is a square corner, like the corner of a page. To make a right-angle checker, fold a piece of paper twice so that the fold lies exactly on itself: the corner is a right angle.',
                   'The size of an angle is how far it opens, not how long its arms are. Parallel lines never meet and stay the same distance apart. Perpendicular lines meet at a right angle. Type the answers here.'])
D4 = figs4()
PR = D4['printed']
ANG = D4['data']['ANG']
SK = 'Angles and lines'
EXTRA = 'Extra practice (not for the lesson). '


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def one(solutions):
    return solutions[0] if len(solutions) == 1 else None


# ---------------------------------------------------------------- the data of the figures equals the printed workbook figures
assert [a[0] for a in ANG] == list('abcdef')
_Q2 = {'A': (40, 54, 3), 'B': (175, 54, 3), 'C': (300, 0, 5), 'D': (440, 54, 3)}
for _k, (_x0, _y0, _H) in _Q2.items():       # u = 28, y up inside the shape
    _pts = ' '.join(f'{_x0 + a * 28:.1f},{_y0 + (_H - b) * 28:.1f}' for a, b in SHAPES[_k])
    assert f'points="{_pts}"' in PR['l8_q2'], f'shape {_k}'
for _i, _ch in enumerate('EHTLZN'):          # the letters: 50 wide, 80 tall, top 16, 95 px apart
    for a, b, c, d in LETTER_SEGS[_ch]:
        _x = 45 + _i * 95
        assert f'<line x1="{_x + a:.1f}" y1="{16 + b:.1f}" x2="{_x + c:.1f}" y2="{16 + d:.1f}"' in PR['l8_q4'], f'letter {_ch}'
PTS = {'A': (1, 6), 'B': (5, 2), 'D': (3, 4), 'C': (7, 5), 'E': (9, 6), 'F': (13, 4), 'G': (11, 5)}
for _n, (_a, _b) in PTS.items():
    assert f'<circle cx="{28 + _a * 36}" cy="{14 + _b * 36}" r="5.5"' in PR['l8_q5'], f'point {_n}'
assert PR['l8_q3'].count('<line') == 6 and 'x1="190.0" y1="196.0"' in PR['l8_q3']          # the fan: 6 lines from one point
assert 'x="20" y="15" width="200" height="130"' in PR['l8_q6'] and 'x1="120.0" y1="15.0" x2="120.0" y2="145.0"' in PR['l8_q6'] and 'x1="20.0" y1="80.0" x2="220.0" y2="80.0"' in PR['l8_q6']
assert all(f'{k}:00' in PR['l8_t3'] for k in range(1, 12))                                 # the eleven clocks

KIND = ['Smaller than a right angle', 'A right angle', 'Bigger than a right angle']


def angle_kind(letter):
    size = [a for a in ANG if a[0] == letter][0][2]            # how far the arms open, in degrees
    return KIND[0] if size < 90 else (KIND[1] if size == 90 else KIND[2])


def angle_item(letter, steps):
    return I(id=f'1{letter}', tier='core', no=f'1 (angle {letter})', label=f'1 {letter}', type='choice', skill='comparing angles with a right angle', options=KIND,
             answer={'a': KIND[1], 'b': KIND[0], 'c': KIND[2], 'd': KIND[1], 'e': KIND[2], 'f': KIND[0]}[letter],
             svg=angle_fig(ANG, letter),
             q=f'Use a right-angle checker (the corner of a piece of paper, or the one you folded) to test angle {letter}. Is it smaller than a right angle, a right angle, or bigger than a right angle?',
             check=lambda: angle_kind(letter),
             hint='Put the corner of the checker into the angle with one arm of the checker along one arm of the angle. Where is the other arm of the angle?', steps=steps,
             src=['Use the right-angle checker you folded in Explore (fold a new one if you lost it). Use it to sort the angles a to f.'])


def poly_item(letter, answer, steps, extra_q=''):
    return I(id=f'2{letter}', tier='core', no=f'2 (shape {letter})', label=f'2 {letter}', type='number', skill='right angles inside a shape', answer=answer,
             svg=shape_fig(SHAPES[letter], f'Shape {letter}', f'Shape {letter}: a figure made of straight sides'),
             q=f'How many right angles are INSIDE shape {letter}? Check every corner with your checker. A corner that dents INTO the shape is bigger than a right angle: do not count it. (Shape A has 8: its 4 dent corners are not counted.) Type the number.',
             check=lambda: corner_kinds(SHAPES[letter])[0],
             hint='Go round the shape and check each corner with the checker. Count the square corners that are inside the shape.', steps=steps,
             src=['How many right angles are INSIDE each shape? Check every corner with your checker. A corner that dents INTO the shape is bigger than a right angle: do not count it. A is done for you.'])


def lines_between(n):
    """How many angles n lines from one point make: every angle is the gap between two of the lines; found by taking every pair of lines."""
    return sum(1 for i in range(n) for j in range(i + 1, n))


def made_of(n):
    """[number of angles made of 1 small angle, of 2, ..., of n-1]: the angle between line i and line j is made of j - i small angles."""
    out = [0] * (n - 1)
    for i in range(n):
        for j in range(i + 1, n):
            out[j - i - 1] += 1
    return out


def letter_kind(ch):
    raw = letter_raw(ch)
    par, perp = len(pairs_parallel(raw)) > 0, len(pairs_perpendicular(raw)) > 0
    return 'Both' if par and perp else ('Parallel lines only' if par else ('Perpendicular lines only' if perp else 'Neither'))


LETTER_OPTS = ['Parallel lines only', 'Perpendicular lines only', 'Both', 'Neither']


def letter_item(ch, answer, steps, extra=False):
    return I(id=f'4{ch}', tier='core', no=f'4 (letter {ch})', label=f'4 {ch}', type='choice', skill='parallel and perpendicular lines', options=LETTER_OPTS, answer=answer,
             svg=letter_fig(ch),
             q=(EXTRA if extra else '') + f'Parallel lines never meet and stay the same distance apart, like train tracks. Perpendicular lines meet at a right angle (a square corner). Look at the letter {ch}. Which kind of lines does it have?',
             check=lambda: letter_kind(ch),
             hint='Look for two lines that stay the same distance apart. Then look for two lines that meet in a square corner.', steps=steps,
             src=['Look at the lines in these letters. Parallel lines never meet and stay the same distance apart, like train tracks. Perpendicular lines meet at a right angle (a square corner).'])


# ---- Q5: the grid with the lines (A(1,6) B(5,2) D(3,4) C(7,5), E(9,6) F(13,4) G(11,5)); steps are (across, down the page)
def norm(d):
    g = gcd(abs(d[0]), abs(d[1]))
    return (d[0] // g, d[1] // g)


def base_dir(a, b):
    return (PTS[b][0] - PTS[a][0], PTS[b][1] - PTS[a][1])


def parallel_dir(a, b):
    """The steps of a line parallel to the line through points a and b: the same steps."""
    return norm(base_dir(a, b))


def perpendicular_dir(a, b):
    """The steps of a line perpendicular to the line through a and b: swap the two steps and turn one of them round."""
    dx, dy = base_dir(a, b)
    return norm((-dy, dx))


BOX_AB = (0, 10, 0, 7)
BOX_EF = (6, 14, 0, 7)
PTS_AB = {k: PTS[k] for k in 'ABCD'}
PTS_EF = {k: PTS[k] for k in 'EFG'}
CAND_A = [(1, PTS['C'], (2, -1)), (2, PTS['C'], (1, -1)), (3, PTS['C'], (1, 1)), (4, PTS['C'], (1, -2))]
CAND_B = [(1, PTS['D'], (1, 2)), (2, PTS['D'], (2, 1)), (3, PTS['D'], (1, 1)), (4, PTS['D'], (2, -1))]
CAND_C = [(1, PTS['G'], (1, -1)), (2, PTS['G'], (2, 1)), (3, PTS['G'], (1, -2)), (4, PTS['G'], (1, 2))]
CAP_AB = 'A square grid with line AB and the points C and D. C is not on AB. D is on AB.'
CAP_EF = 'A square grid with line EF. G is on EF.'


def parallel_line_no(cands, a, b):
    d0 = base_dir(a, b)
    return one([n for n, P, d in cands if d[0] * d0[1] - d[1] * d0[0] == 0 and (P[0] - PTS[a][0]) * d0[1] - (P[1] - PTS[a][1]) * d0[0] != 0])


def perpendicular_line_no(cands, a, b):
    d0 = base_dir(a, b)
    return one([n for n, P, d in cands if d[0] * d0[0] + d[1] * d0[1] == 0])


def way_text(d):
    """'1 square right and 1 square up' for steps (across, down the page)."""
    return f'{abs(d[0])} square{"s" if abs(d[0]) != 1 else ""} {"right" if d[0] > 0 else "left"} and {abs(d[1])} square{"s" if abs(d[1]) != 1 else ""} {"down" if d[1] > 0 else "up"}'


def draw_item(iid, no, label, point, a, b, kind, box, pts, cap, hint, steps, src, q):
    ans = (lambda: (PTS[point], parallel_dir(a, b))) if kind == 'par' else (lambda: (PTS[point], perpendicular_dir(a, b)))
    return I(id=iid, tier='core', no=no, label=label, type='selfcheck', paper=True, marking_mode='self', skill='parallel and perpendicular lines',
             svg=lines_fig(box, 28 if box == BOX_AB else 34, pts, (a, b), caption=cap),
             sol_fig=lambda got: lines_fig(box, 28 if box == BOX_AB else 34, pts, (a, b), answer=got, caption=cap + ' The correct line is drawn in green.'),
             check=ans, q=q, hint=hint, steps=steps, src=src)


def cand_item(iid, no, label, cands, box, pts, a, b, which, answer_no, q, hint, steps, src, kind):
    fn = parallel_line_no if kind == 'par' else perpendicular_line_no
    return I(id=iid, tier='core', no=no, label=label, type='choice', skill='parallel and perpendicular lines', options=['Line 1', 'Line 2', 'Line 3', 'Line 4'], answer=f'Line {answer_no}',
             svg=lines_fig(box, 28 if box == BOX_AB else 34, pts, (a, b), cands=cands, caption=(CAP_AB if box == BOX_AB else CAP_EF) + ' Four numbered lines go through ' + which + '.'),
             check=lambda: f'Line {fn(cands, a, b)}', q=q, hint=hint, steps=steps, src=src)


STAIR_Q = lambda n: f'A {n}-step staircase'
FORMS = {k: stairs_fig(k, f'A {k}-step staircase made of squares', decreasing=False) for k in range(1, 5)}
HEXAGON = hexagon_right_angles(3)
RECT_RAW = [((0, 0), (3, 0)), ((3, 0), (3, 2)), ((3, 2), (0, 2)), ((0, 2), (0, 0))]
HASH_RAW = [((1, 0), (1, 3)), ((2, 0), (2, 3)), ((0, 1), (3, 1)), ((0, 2), (3, 2))]


def stair_row(n, ans, steps):
    return I(id=f'I8-{n}', tier='invest', no=f'8(a) {n}-step', label=f'Inv {n} step' + ('s' if n > 1 else ''), type='fields', skill='counting corners in order', answer=ans,
             svg=FORMS[n],
             q=f'Count the corners of this {n}-step staircase. How many corners have an inside angle that is a right angle? How many have an inside angle BIGGER than a right angle? How many corners are there altogether?',
             frame=grp('Right angles {f1}      Bigger {f2}      All corners {f3}'),
             check=lambda: list(stair_counts(n)),
             hint='Go round the edge of the staircase corner by corner. Use a table: write each corner as a right angle or a bigger angle, so that you do not miss one or count one twice.', steps=steps,
             src=['Count the corners of each staircase where the inside angle is a right angle. Then count the corners where the inside angle is BIGGER than a right angle. Draw the 4-step staircase and fill in the table.'])


ITEMS = [
    # ================= Start here (workbook lesson 8, No.1 to No.6)
    angle_item('a', ['Angle a is turned round, but it still fits the corner of the checker exactly.', 'The size of an angle is how far it opens, and the way it is turned does not change that.', 'Angle a is a right angle.']),
    angle_item('b', ['Put the checker into angle b with one arm along one arm of the angle.', 'The other arm of angle b is inside the corner of the checker: angle b opens less than a right angle.', 'Angle b is smaller than a right angle.']),
    angle_item('c', ['Put the checker into angle c with one arm along one arm of the angle.', 'The other arm of angle c is outside the corner of the checker: angle c opens more than a right angle.', 'Angle c is bigger than a right angle.']),
    angle_item('d', ['Angle d has one short arm and one long arm, but the length of the arms does not change the size of an angle.', 'The corner of the checker fits angle d exactly.', 'Angle d is a right angle.']),
    angle_item('e', ['Put the checker into angle e with one arm along one arm of the angle.', 'The other arm of angle e is well outside the corner of the checker: angle e opens a lot more than a right angle.', 'Angle e is bigger than a right angle.']),
    angle_item('f', ['Angle f has long arms, but long arms do not make an angle bigger. Only how far the arms open matters.', 'Put the checker into angle f: the other arm is inside the corner of the checker, so f opens less than a right angle.', 'Angle f is smaller than a right angle.']),

    poly_item('B', 6, ['Shape B is a staircase with 3 steps. Check each corner with the checker.', 'The corners on the outside are right angles: 6 of them. The 2 corners that dent into the shape are bigger than a right angle, so they are not counted.', 'Shape B has 6 right angles inside.']),
    poly_item('C', 3, ['Shape C is like a house. Check each corner with the checker.', 'The two bottom corners are right angles, and the top of the roof is a right angle too. The 2 corners at the sides of the roof are bigger than a right angle.', 'Shape C has 3 right angles inside.']),
    poly_item('D', 2, ['Shape D has a long bottom and a slanted right side. Check each corner with the checker.', 'Only the 2 square corners on the left are right angles. The other 2 corners are not.', 'Shape D has 2 right angles inside.']),

    I(id='3a-parts', tier='core', no='3(a) small ones', label='3(a) parts', type='fields', skill='counting in order', answer=[5, 4, 3, 2, 1], svg=fan_fig(6),
      frame=grp('made of 1: {f1}      made of 2: {f2}      made of 3: {f3}      made of 4: {f4}      made of 5: {f5}'),
      q='These 6 lines all start at point O. (Example: 3 lines make 3 angles: 1 + 1 + 1.) Count the angles. How many angles are made of 1 small angle? Of 2 small angles next to each other? Of 3, of 4 and of 5? Fill in the boxes.',
      check=lambda: made_of(6),
      hint='Count the small ones first. Then count the ones made of 2 small ones side by side, and so on. Go in order so that you miss none.',
      steps=['6 lines make 5 small angles between neighbouring lines.', 'Made of 2 small angles: 4. Made of 3: 3. Made of 4: 2. Made of 5: 1.', 'The numbers are 5, 4, 3, 2 and 1.'],
      src=['These 6 lines all start at point O. (Example: 3 lines make 3 angles: 1 + 1 + 1.)', 'How many angles? Count the small ones first, then those made of 2 small ones, and so on.', 'Made of 1: ___ 2: ___ 3: ___ 4: ___ 5: ___']),
    I(id='3a-total', tier='core', no='3(a) total', label='3 total', type='number', skill='counting in order', answer=15, svg=fan_fig(6),
      q='These 6 lines all start at point O. How many angles are there altogether? Type the number.',
      check=lambda: lines_between(6),
      hint='Count in an organised way: the small angles first, then the angles made of 2 small ones, and so on. Then add.',
      steps=['Count the angles by size: 5 small ones, then 4 made of 2, then 3, 2 and 1.', '5 + 4 + 3 + 2 + 1 = 15.', 'There are 15 angles.'],
      src=['These 6 lines all start at point O.', 'Total: ________']),
    I(id='3b', tier='core', no='3(b)', label='3(b)', type='number', skill='finding a pattern', answer=28, svg=fan_fig(8),
      q=EXTRA + 'Look for a pattern. 8 lines start at one point, spread out like these. How many angles are there? Type the number.',
      check=lambda: lines_between(8),
      hint='Count the angles for 2 lines, 3 lines, 4 lines ... What do you add each time?',
      steps=['2 lines make 1 angle, 3 lines make 3, 4 lines make 6. The jumps are 2, 3, 4 ...', 'With 8 lines the angles are 7 + 6 + 5 + 4 + 3 + 2 + 1.', '7 + 6 + 5 + 4 + 3 + 2 + 1 = 28 angles.'],
      src=['Take-home. Look for a pattern. 8 lines start at one point, spread out like these. How many angles are there?']),

    letter_item('E', 'Both', ['Parallel: the top, middle and bottom lines go across and never meet.', 'Perpendicular: each of those lines meets the upright line in a square corner.', 'The letter E has both.']),
    letter_item('H', 'Both', ['Parallel: the two upright lines never meet.', 'Perpendicular: the line across meets each upright line in a square corner.', 'The letter H has both.']),
    letter_item('T', 'Perpendicular lines only', ['The letter T has just two lines. The top line and the stem meet in a square corner: perpendicular.', 'No two lines stay the same distance apart, so there are no parallel lines.', 'The letter T has perpendicular lines only.']),
    letter_item('L', 'Perpendicular lines only', ['The letter L has just two lines. They meet in a square corner: perpendicular.', 'They are not parallel, because they meet.', 'The letter L has perpendicular lines only.']),
    letter_item('Z', 'Parallel lines only', ['Parallel: the top line and the bottom line never meet.', 'The slanted line does not meet any line in a square corner, so there are no perpendicular lines.', 'The letter Z has parallel lines only.'], extra=True),
    letter_item('N', 'Parallel lines only', ['Parallel: the two upright lines never meet.', 'The slanted line does not meet either upright line in a square corner, so there are no perpendicular lines.', 'The letter N has parallel lines only.'], extra=True),
    I(id='4b', tier='core', no='4(b)', label='4(b)', type='fields', skill='parallel and perpendicular lines', answer=[3, 3], svg=letter_fig('E'), frame=grp('Parallel pairs {f1}      Perpendicular pairs {f2}'),
      q='In the letter E, how many pairs of parallel lines are there? How many pairs of perpendicular lines? Fill in the boxes.',
      check=lambda: [len(pairs_parallel(letter_raw('E'))), len(pairs_perpendicular(letter_raw('E')))],
      hint='Name the 4 lines of E: the upright line and 3 lines across. Make a list of every pair of lines and test each pair.',
      steps=['The 3 lines across are parallel to each other: top and middle, top and bottom, middle and bottom. That is 3 pairs.', 'Each line across meets the upright line in a square corner. That is 3 pairs of perpendicular lines.', 'The numbers are 3 and 3.'],
      src=['In the letter E: pairs of parallel lines ____ pairs of perpendicular lines ____']),

    draw_item('5a-draw', '5(a) draw', '5(a) draw', 'C', 'A', 'B', 'par', BOX_AB, PTS_AB, CAP_AB, 'Look at the steps of the line AB: how many squares across and how many up each time? A parallel line keeps the same steps.',
              ['AB goes 1 square right and 1 square up at each step.', 'A line through C that goes 1 square right and 1 square up at each step has the same steps, so it is parallel to AB and never meets it.', 'Draw it with a ruler through C, and check it with the answer shown.'],
              ['Use a ruler. Draw on the grid.', 'Through C, draw a line parallel to AB.'], 'Use a ruler. Through C, draw a line parallel to AB.'),
    cand_item('5a-pick', '5(a) which line', '5(a) pick', CAND_A, BOX_AB, PTS_AB, 'A', 'B', 'C', 2, 'Which numbered line through C is parallel to AB? (Parallel lines never meet.)',
              'Look at the steps of AB: how many squares across and how many up each time? Which numbered line has the same steps?',
              ['AB goes 1 square right and 1 square up at each step.', 'Line 2 goes 1 square right and 1 square up at each step too, so it never meets AB.', 'The parallel line is Line 2.'],
              ['Through C, draw a line parallel to AB.'], 'par'),
    draw_item('5b-draw', '5(b) draw', '5(b) draw', 'D', 'A', 'B', 'perp', BOX_AB, PTS_AB, CAP_AB, 'Look at the steps of AB. For a perpendicular line, swap the two numbers and turn one of the steps round.',
              ['AB goes 1 square right and 1 square up at each step.', 'A perpendicular line meets AB at a right angle. Swap the steps and turn one of them round: 1 square right and 1 square DOWN at each step.', 'Draw it with a ruler through D, and check it with your right-angle checker and the answer shown.'],
              ['Use a ruler. Draw on the grid.', 'Through D, draw a line perpendicular to AB.'], 'Use a ruler. Through D, draw a line perpendicular to AB.'),
    cand_item('5b-pick', '5(b) which line', '5(b) pick', CAND_B, BOX_AB, PTS_AB, 'A', 'B', 'D', 3, 'Which numbered line through D is perpendicular to AB? (Perpendicular lines meet at a right angle.)',
              'Check each numbered line with your right-angle checker where it crosses AB. Or swap the steps of AB and turn one round.',
              ['AB goes 1 square right and 1 square up at each step.', 'Swap the steps and turn one round: 1 square right and 1 square down. Line 3 goes 1 square right and 1 square down.', 'Line 3 crosses AB at a right angle.'],
              ['Through D, draw a line perpendicular to AB.'], 'perp'),
    draw_item('5c-draw', '5(c) draw', '5(c) draw', 'G', 'E', 'F', 'perp', BOX_EF, PTS_EF, CAP_EF, 'Look at the steps of EF. Swap the two numbers and turn one of the steps round, then check with your right-angle checker.',
              ['EF goes 2 squares right and 1 square up at each step.', 'A perpendicular line: swap the steps and turn one of them round. That gives 1 square right and 2 squares DOWN (or 1 square left and 2 squares up) at each step.', 'Draw it with a ruler through G, and check it with your right-angle checker and the answer shown.'],
              ['Think harder (if you have time): through G, draw a line perpendicular to EF. Check it with your checker.'], 'Think harder (if you have time): through G, draw a line perpendicular to EF. Use a ruler and check it with your right-angle checker.'),
    cand_item('5c-pick', '5(c) which line', '5(c) pick', CAND_C, BOX_EF, PTS_EF, 'E', 'F', 'G', 4, 'Think harder (if you have time). Which numbered line through G is perpendicular to EF?',
              'Check each numbered line with your right-angle checker where it crosses EF. Or swap the steps of EF and turn one round.',
              ['EF goes 2 squares right and 1 square up at each step.', 'Swap the steps and turn one round: 1 square right and 2 squares down. Line 4 goes 1 square right and 2 squares down.', 'Line 4 crosses EF at a right angle.'],
              ['Think harder (if you have time): through G, draw a line perpendicular to EF. Check it with your checker.'], 'perp'),

    I(id='6-points', tier='core', no='6 (points)', label='6 points', type='fields', skill='counting right angles in order', answer=[4, 8, 4], svg=window_fig(),
      frame=grp('Corners {f1}      Where lines meet the sides {f2}      In the middle {f3}'),
      q='(if time) Visit every point where lines meet in this window. How many right angles are at the 4 corners altogether? At the 4 points where the lines meet the sides? At the middle point?',
      check=lambda: (lambda per: [sum(v for v in per.values() if v == 1), sum(v for v in per.values() if v == 2), sum(v for v in per.values() if v == 4)])(right_angles_at_points(window_raw())[1]),
      hint='At a corner, 2 lines meet. Where a line meets a side, 3 lines meet. In the middle 4 lines meet. How many right angles does each kind of point make?',
      steps=['Each of the 4 corners has 1 right angle: 4.', 'Each of the 4 points where a line meets a side has 2 right angles: 4 × 2 = 8.', 'The middle point has 4 right angles. The numbers are 4, 8 and 4.'],
      src=['(if time) How many right angles can you find in this window?', 'Visit every point where lines meet. Write how many right angles are at each point, then add.']),
    I(id='6-total', tier='core', no='6 (total)', label='6 total', type='number', skill='counting right angles in order', answer=16, svg=window_fig(),
      q='(if time) How many right angles can you find in this window? Visit every point where lines meet. Type the number.',
      check=lambda: right_angles_at_points(window_raw())[0],
      hint='Write how many right angles are at each point where lines meet, then add them all.',
      steps=['Corners: 4 × 1 = 4. Where the lines meet the sides: 4 × 2 = 8. The middle: 4.', '4 + 8 + 4 = 16.', 'There are 16 right angles.'],
      src=['(if time) How many right angles can you find in this window?', 'Right angles altogether:  ________']),

    # ================= Investigation (Investigation and look back page, No.8: Staircase corners: find the pattern)
    I(id='I8-easy', tier='invest', no='8 easy step', label='Inv easy', type='number', skill='counting corners in order', answer=6, svg=FORMS[2],
      q='A 1-step staircase is 1 square. A 2-step staircase has 3 squares (a column of 2 beside a column of 1). Easy first step: count the corners of the 2-step staircase. Type the number.',
      check=lambda: stair_counts(2)[2],
      hint='Go round the edge and count every corner, including the one that dents into the shape. Put a dot on each corner as you count.',
      steps=['The 1-step staircase is one square: 4 corners.', 'The 2-step staircase: go round the edge. There are 5 square corners on the outside and 1 corner that dents in.', '5 + 1 = 6 corners.'],
      src=['Easy first step: draw the 1-step and 2-step staircases. Count the corners of the 2-step staircase.']),
    stair_row(1, [4, 0, 4], ['A 1-step staircase is one square.', 'All 4 corners are right angles and none is bigger than a right angle.', 'Right angles 4, bigger 0, all corners 4.']),
    stair_row(2, [5, 1, 6], ['Go round the outside of the 2-step staircase.', '5 corners are right angles and 1 corner dents in (its inside angle is bigger than a right angle).', 'Right angles 5, bigger 1, all corners 6.']),
    stair_row(3, [6, 2, 8], ['Go round the outside of the 3-step staircase.', '6 corners are right angles and 2 corners dent in (inside angles bigger than a right angle).', 'Right angles 6, bigger 2, all corners 8.']),
    stair_row(4, [7, 3, 10], ['Go round the outside of the 4-step staircase.', '7 corners are right angles and 3 corners dent in (inside angles bigger than a right angle).', 'Right angles 7, bigger 3, all corners 10.']),
    I(id='I8-ten', tier='invest', no='8(b) 10-step', label='Inv 10 steps', type='fields', skill='finding a pattern', answer=[13, 9, 22],
      frame=grp('Right angles {f1}      Bigger {f2}      All corners {f3}'),
      q='Look at your table for 1, 2, 3 and 4 steps. What pattern do you see? Use it to fill in the row for a 10-step staircase without drawing.',
      check=lambda: list(stair_counts(10)),
      hint='Look at each column of the table on its own. What changes each time you add a step?',
      steps=['The right-angle corners go 4, 5, 6, 7 ...: the number of steps + 3. The bigger corners go 0, 1, 2, 3 ...: the number of steps - 1.', 'For 10 steps: 10 + 3 = 13 right angles and 10 - 1 = 9 bigger corners.', 'All corners: 13 + 9 = 22.'],
      src=['What pattern do you see? Use it to fill in the 10-step row without drawing.']),
    I(id='I8-even', tier='invest', no='8(c)', label='Inv even', type='choice', skill='finding a pattern', options=['No, sometimes it is odd', 'Yes, it is always even'], answer='Yes, it is always even',
      q='Look at the number of ALL corners of a staircase: 4, 6, 8, 10 ... Is the number of corners always an even number?',
      check=lambda: 'Yes, it is always even' if all(stair_counts(n)[2] % 2 == 0 for n in range(1, 60)) else 'No, sometimes it is odd',
      hint='Look at the numbers of all corners in your table. What do you add each time you add a step?',
      steps=['The total number of corners for 1 to 4 steps is 4, 6, 8 and 10, then 22 for 10 steps.', 'Each new step adds 2 corners, so the total always stays even. (Checked by computer for staircases of 1 to 59 steps.)', 'So the number of corners is always even.'],
      src=['Is the number of corners always an even number? Why do you think so?']),
    I(id='I8-why', tier='invest', no='8(c) explain', label='Inv why', type='selfcheck', open=True, marking_mode='self', skill='explaining why',
      q='Explain why the number of corners of a staircase is always even. What does one more step add? Write your idea, then compare with the answer shown.',
      check=lambda: [stair_counts(n)[2] - stair_counts(n - 1)[2] for n in range(2, 40)],
      hint='Put one more step on a staircase. Which new corners appear, and does any corner disappear?',
      steps=['Each new step adds 2 corners: one new right angle and one new corner that dents in.', 'Starting from 4 corners and adding 2 each time, the total is 4, 6, 8, 10 ... always even.', 'The rule is: all corners = 2 × the number of steps + 2.'],
      src=['Is the number of corners always an even number? Why do you think so?']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1-shape', tier='stretch', no='T1 (shape)', label='T1 shape', type='choice', skill='properties of shapes', options=['A square', 'A rhombus (a diamond)', 'A rectangle', 'A triangle'], answer='A rectangle',
      q='I have 4 sides and 4 right angles. My sides are not all the same length. What shape am I?',
      check=lambda: one([n for n, (sides, rights, equal) in {'A square': (4, 4, True), 'A rhombus (a diamond)': (4, 0, True), 'A rectangle': (4, 4, False), 'A triangle': (3, 0, False)}.items() if sides == 4 and rights == 4 and not equal]),
      hint='A shape with 4 right angles has 4 square corners. Which of these shapes can have sides of different lengths?',
      steps=['A shape with 4 sides and 4 right angles is a square or a rectangle.', 'A square has all its sides the same length. This shape does not.', 'I am a rectangle.'],
      src=['I have 4 sides and 4 right angles. My sides are not all the same length. What shape am I?']),
    I(id='T1-pairs', tier='stretch', no='T1 (parallel)', label='T1 parallel', type='number', skill='parallel lines', answer=2,
      q='I have 4 sides and 4 right angles. My sides are not all the same length. How many pairs of parallel lines do I have? Type the number.',
      check=lambda: len(pairs_parallel(RECT_RAW)),
      hint='Draw the shape and find the sides that never meet and stay the same distance apart.',
      steps=['A shape with 4 right angles and sides of different lengths is a rectangle.', 'The two long sides are parallel, and the two short sides are parallel.', 'That is 2 pairs of parallel lines.'],
      src=['How many pairs of parallel lines do I have?']),
    I(id='T2', tier='stretch', no='T2', label='T2', type='number', skill='right angles inside a shape', answer=6,
      svg=squares_fig([(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)], 'A U shape', 'A U shape made of 5 squares: 3 squares in a row with 1 more square on top of each end square', cols=5, rows=4, c=44),
      q='A U shape is made of 5 squares: 3 squares in a row with 1 more square on top of each end square. How many right angles are inside it? Type the number.',
      check=lambda: (lambda r: r[0] if poly_area(U_SHAPE) == 5 else None)(corner_kinds(U_SHAPE)),
      hint='Count all the corners of the U. Then take away the corners that dent into the shape.',
      steps=['The U has 8 corners.', 'The 2 corners at the bottom of the gap dent into the shape: inside they are bigger than a right angle, so they are not counted.', '8 - 2 = 6 right angles inside.'],
      src=['A U shape is made of 5 squares: 3 squares in a row with 1 more square on top of each end square. How many right angles are inside it?']),
    I(id='T3-small', tier='stretch', no='T3 (smaller)', label='T3 smaller', type='set', ordered=False, skill='angles on a clock', answer=[1, 2, 10, 11], svg=clocks_fig(),
      q='Look at a clock face. For each o’clock time from 1 o’clock to 11 o’clock, look at the angle between the hands (the short way round). Which times make an angle SMALLER than a right angle? Type the hours with commas.',
      check=lambda: [h for h in range(1, 12) if hands_angle(h) < 90],
      hint='A right angle is a quarter turn. At 3 o’clock the hands make a quarter turn. Which hours are less than that, going either way round?',
      steps=['Every hour the hour hand turns 30 degrees, so 3 hours make a quarter turn (a right angle).', 'The times with the hands closer than 3 hours apart the short way round are 1, 2, 10 and 11 o’clock.', 'Smaller than a right angle: 1, 2, 10 and 11.'],
      src=['Look at a clock face. For each o’clock time from 1 o’clock to 11 o’clock, is the angle between the hands (the short way round) smaller than, the same as, or bigger than a right angle? Put each time in the right group.']),
    I(id='T3-right', tier='stretch', no='T3 (right angle)', label='T3 right', type='set', ordered=False, skill='angles on a clock', answer=[3, 9], svg=clocks_fig(),
      q='Look at the clock faces. Which o’clock times make a RIGHT angle between the hands (the short way round)? Type the hours with commas.',
      check=lambda: [h for h in range(1, 12) if hands_angle(h) == 90],
      hint='A right angle is a quarter turn. How many hours is a quarter of the way round the clock?',
      steps=['A quarter of the way round the clock is 3 hours.', 'At 3 o’clock the hands are 3 hours apart. At 9 o’clock they are 3 hours apart the other way round.', 'Right angle: 3 and 9 o’clock.'],
      src=['Put each time in the right group.']),
    I(id='T3-big', tier='stretch', no='T3 (bigger)', label='T3 bigger', type='set', ordered=False, skill='angles on a clock', answer=[4, 5, 6, 7, 8], svg=clocks_fig(),
      q='Look at the clock faces. Which o’clock times make an angle BIGGER than a right angle between the hands (the short way round)? Type the hours with commas.',
      check=lambda: [h for h in range(1, 12) if hands_angle(h) > 90],
      hint='Which hours are more than a quarter turn (3 hours) apart, the short way round?',
      steps=['The hands are more than 3 hours apart, the short way round, at 4, 5, 6, 7 and 8 o’clock.', 'At 6 o’clock the hands are 6 hours apart and make a straight line, which is bigger than a right angle.', 'Bigger than a right angle: 4, 5, 6, 7 and 8.'],
      src=['Put each time in the right group.']),
    I(id='T4-par', tier='stretch', no='T4 (parallel)', label='T4 parallel', type='number', skill='parallel lines', answer=2, svg=hash_fig(),
      q='The # sign is made of 4 lines: 2 upright lines and 2 lines across. How many pairs of parallel lines does it have? Type the number.',
      check=lambda: len(pairs_parallel(HASH_RAW)),
      hint='Name the lines: 2 upright lines and 2 lines across. Which pairs of lines never meet?',
      steps=['The 2 upright lines are parallel to each other: 1 pair.', 'The 2 lines across are parallel to each other: 1 pair.', 'That is 2 pairs of parallel lines.'],
      src=['The # sign is made of 4 lines: 2 upright lines and 2 lines across. How many pairs of parallel lines does it have? How many pairs of perpendicular lines?']),
    I(id='T4-perp', tier='stretch', no='T4 (perpendicular)', label='T4 perp.', type='number', skill='perpendicular lines', answer=4, svg=hash_fig(),
      q='The # sign is made of 4 lines: 2 upright lines and 2 lines across. How many pairs of perpendicular lines does it have? Type the number.',
      check=lambda: len(pairs_perpendicular(HASH_RAW)),
      hint='Make a list: each upright line with each line across. Which pairs meet at a square corner?',
      steps=['Each upright line meets each line across at a right angle.', '2 upright lines × 2 lines across = 4 pairs.', 'That is 4 pairs of perpendicular lines.'],
      src=['How many pairs of perpendicular lines?']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Extra question (printed as "Take-home")
    I(id='G5', tier='challenge', no='G5', label='G5', type='selfcheck', open=True, marking_mode='open', skill='making up a riddle',
      q='Make up your own "Which shape am I?" riddle about a shape on square grid paper. Use words like sides, right angles, parallel and perpendicular, and give 3 clues. Draw the answer. Then check: can a partner draw a DIFFERENT shape that fits your clues? If yes, add a clue.',
      check=lambda: corner_kinds([(0, 0), (2, 0), (2, 1), (1, 1), (1, 3), (0, 3)]),
      hint='Draw your secret shape first, like an L or a rectangle. Then write what is special about it. Do the clues fit another shape too?',
      steps=['Answers vary. Check that the drawn shape fits every clue and that the clues are about sides, right angles and parallel lines.', 'Example: "I have 6 straight sides. I have 5 right angles inside me. I have one dent." (An L shape.) Other shapes could fit the first two clues, so the third clue matters.'],
      src=['Make up your own "Which shape am I?" riddle about a shape on square grid paper.']),
    I(id='G6', tier='challenge', no='G6', label='G6', type='number', skill='counting right angles in order', answer=24, svg=row_fig(6),
      q='A long rectangle is cut into 6 squares in a row by 5 lines. How many right angles can you find? Type the number.',
      check=lambda: right_angles_at_points(row_raw(6))[0],
      hint='Visit every point where lines meet. How many right angles are at each kind of point? Then add.',
      steps=['The 4 corners have 1 right angle each: 4.', 'Each of the 5 lines meets the top and the bottom of the rectangle. That is 10 points with 2 right angles each: 10 × 2 = 20.', '4 + 20 = 24 right angles.'],
      src=['A long rectangle is cut into 6 squares in a row by 5 lines. How many right angles can you find?']),
    I(id='G7-can', tier='challenge', no='G7 (can it?)', label='G7 yes/no', type='choice', skill='right angles inside a shape', options=['Yes', 'No'], answer='No',
      q='Can a 6-sided shape have 6 right angles inside it?',
      check=lambda: 'Yes' if 6 in HEXAGON else 'No',
      hint='Draw some 6-sided shapes with square corners, like an L. Count the right angles inside each one. Can you find one with 6?',
      steps=['Try drawing: an L shape has 6 sides and 5 right angles inside, and one corner that dents in.', 'Every time we try to make all 6 corners square, a corner turns out to dent in.', 'A 6-sided shape cannot have 6 right angles inside. (A proof is not expected.)'],
      src=['Can a 6-sided shape have 6 right angles inside it? What is the most right angles a 6-sided shape can have inside?']),
    I(id='G7-most', tier='challenge', no='G7 (most)', label='G7 most', type='number', skill='right angles inside a shape', answer=5,
      q='What is the most right angles a 6-sided shape can have inside it? Type the number.',
      check=lambda: max(HEXAGON),
      hint='Draw a 6-sided shape with as many square corners as you can. Count the right angles inside.',
      steps=['An L shape has 6 sides and 5 right angles inside.', 'Trying other 6-sided shapes never gives more than 5.', 'The most is 5.'],
      src=['What is the most right angles a 6-sided shape can have inside?']),
    I(id='TH-a', tier='challenge', no='Extra (a)', label='Extra (a)', type='choice', skill='parallel lines', options=['Yes', 'No'], answer='No',
      q=EXTRA + 'Do the two long edges of a ruler ever meet?',
      check=lambda: 'Yes' if segments_meet(((0, 0), (30, 0)), ((0, 3), (30, 3))) else 'No',
      hint='Think of the two rails of a train track. Do they ever meet?',
      steps=['The two long edges of a ruler stay the same distance apart.', 'Lines that stay the same distance apart never meet. They are parallel.', 'So the answer is No.'],
      src=['Do the two long edges of a ruler ever meet?']),
]

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
# the three parallel / perpendicular answers on the grid agree with the printed answers (same steps; swap and turn)
assert parallel_dir('A', 'B') == (1, -1) and perpendicular_dir('A', 'B') in ((1, 1), (-1, -1)) and perpendicular_dir('E', 'F') in ((1, 2), (-1, -2))
assert corner_kinds(SHAPES['A'])[0] == 8


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '3b': dict(
        base=dict(n=8),
        tpl=dict(vars=dict(n=[5, 6, 7, 9, 10, 12]),
                 q=EXTRA + 'Look for a pattern. {n} lines start at one point, spread out like a fan. How many angles are there? Type the number.',
                 answer='n*(n-1)//2', hint='Count the angles for 2 lines, 3 lines, 4 lines ... What do you add each time?',
                 steps=['2 lines make 1 angle, 3 lines make 3, 4 lines make 6. The numbers added are 2, 3, 4 ...', 'With {n} lines, add the numbers from 1 up to one less than {n}.', 'There are {ans} angles.']),
        oracle=lambda e: lines_between(e['n']), fig=lambda env: fan_fig(env['n'])),
    'G6': dict(
        base=dict(k=6),
        tpl=dict(vars=dict(k=[4, 5, 7, 8]), derive=dict(j='k-1'),
                 q='A long rectangle is cut into {k} squares in a row by {j} lines. How many right angles can you find? Type the number.',
                 answer='4*k', hint='Visit every point where lines meet. How many right angles are at each kind of point? Then add.',
                 steps=['The 4 corners have 1 right angle each: 4.', 'Each of the {j} lines meets the top and the bottom of the rectangle: that is 2 × {j} points with 2 right angles each.', 'Add them to the 4 corners: {ans} right angles.']),
        oracle=lambda e: right_angles_at_points(row_raw(e['k']))[0], fig=lambda env: row_fig(env['k'])),
    'I8-4': dict(
        base=dict(n=4),
        tpl=dict(vars=dict(n=[5, 6, 7, 8]),
                 q='Count the corners of this {n}-step staircase. How many corners have an inside angle that is a right angle? How many have an inside angle BIGGER than a right angle? How many corners are there altogether?',
                 frame=grp('Right angles {f1}      Bigger {f2}      All corners {f3}'), answers=dict(f1='n+3', f2='n-1', f3='2*n+2'),
                 hint='Go round the edge of the staircase corner by corner. Write each corner as a right angle or a bigger angle, so that you do not miss one or count one twice.',
                 steps=['Go round the outside of the staircase.', 'Count the square corners and the corners that dent in (inside angle bigger than a right angle).', 'The numbers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2', 'f3'), stair_counts(e['n']))), fig=lambda env: stairs_fig(env['n'], f'A {env["n"]}-step staircase made of squares', decreasing=False)),
    'I8-ten': dict(
        base=dict(n=10),
        tpl=dict(vars=dict(n=[8, 9, 11, 12, 15]),
                 q='Use the pattern to fill in the row for a {n}-step staircase without drawing.',
                 frame=grp('Right angles {f1}      Bigger {f2}      All corners {f3}'), answers=dict(f1='n+3', f2='n-1', f3='2*n+2'),
                 hint='Look at each column of your table on its own. What changes each time you add a step?',
                 steps=['Use the pattern of each column of the table.', 'Right-angle corners: the number of steps + 3. Bigger corners: the number of steps - 1.', 'The numbers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2', 'f3'), stair_counts(e['n'])))),
}
