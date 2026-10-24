"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 4: Area of Triangle ("Triangle Areas").

The questions are the ones printed in the Level 5 holiday workbook, lesson 4: Start here Q1 to Q5 (p5/content/l4.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l4.js qbank) and Go further B1 to B3 (the last three
'challenge' questions) and the "Make up your own" prompt (gaps.js), in the printed order, exactly as p5/workbook_html.js prints them.  Every answer is recomputed
by an INDEPENDENT checker below (the shoelace formula on the corner coordinates of the drawn figure, or a search over whole-number pairs, never 1/2 x base x height
copied from the printed answer); build_holiday.py stops if a checker and the printed answer differ.  Every figure is drawn from the same coordinates.
"""
import math, os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401
import p5fig2 as G          # noqa: E402

META = dict(level=5, lesson=4, key='p5', title='Triangle Areas', workbook_title='TRIANGLE AREAS', topic='Area of Triangle', strand='Geometry',
            sources=['p5/content/l4.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['Area of a triangle = 1/2 × base × height. The height meets the base at a right angle (the little square), even when it is outside the triangle. A slanting side is not the height. '
                   'Triangles with the same base and the same height have the same area.',
                   'Type the number of cm² (square centimetres). The drawings are to scale. Some questions ask you to explain or to draw: do those on paper if you like, then compare with the model answer after you submit.'])
ST = 'Geometry'
F = Fraction


def D(**k):
    k.setdefault('strand', ST)
    return k


# ---------------------------------------------------------------- checkers: coordinates in cm (y up), the same numbers the figures are drawn from
def shoelace(pts):
    s = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))
    return abs(F(s, 2))


def whole(v):
    v = F(v)
    assert v.denominator == 1, v
    return int(v)


def length(p, q):
    d2 = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    r = math.isqrt(d2)
    assert r * r == d2, (p, q)
    return r


TRI_A = [(0, 0), (8, 0), (0, 6)]
TRI_B = [(0, 0), (14, 0), (5, 12)]
TRI_C = [(0, 0), (9, 0), (15, 8)]
RECT_Q2 = {'A': (0, 6), 'B': (10, 6), 'C': (10, 0), 'D': (0, 0)}
P_PT, Q_PT = (2, 6), (7, 6)
QUAD = {'A': (0, 0), 'B': (4, 5), 'C': (14, 0), 'D': (9, -3)}
R4 = {'A': (0, 8), 'B': (12, 8), 'C': (12, 0), 'D': (0, 0), 'E': (4, 8), 'F': (12, 4)}


def apex_height(tri):
    """Height of a triangle that has its base on the line y = 0 (the first two points): the vertical distance of the third point."""
    return abs(tri[2][1])


def not_needed(tri):
    """Lengths shown on a triangle that are not the base and not the height: the two slanting sides."""
    a, b, c = tri
    return sorted([length(a, c), length(b, c)])


def pairs_for_area(area):
    """Right-angled triangles with whole-number short sides (a, b), a <= b, and the given area: a x b must be double the area."""
    out = []
    for a in range(1, 2 * area + 1):
        for b in range(a, 2 * area + 1):
            if shoelace([(0, 0), (a, 0), (0, b)]) == area:
                out.append((a, b))
    return out


def flat(pairs):
    return [x for p in pairs for x in p]


def height_from_area(area, base):
    found = [h for h in range(1, 400) if F(base * h, 2) == area]
    assert len(found) == 1
    return found[0]


def a3_height():
    found = [h for h in range(1, 200) if F(9 * h, 2) == 6 * 6]
    assert len(found) == 1
    return found[0]


def b1_height():
    legs = (15, 20)
    assert legs[0] ** 2 + legs[1] ** 2 == 25 ** 2
    area = shoelace([(0, 0), (legs[1], 0), (0, legs[0])])
    return height_from_area(area, 25)


def b2_area(small):
    return whole(shoelace([(0, 0), (10, 10), (10 + small, small)]))


def b3_area():
    h = height_from_area(54, 12)              # the height from A to BC
    return whole(F(4 * h, 2))


SQ = 'cm²'

ITEMS = [
    # ================= Start here (workbook lesson 4: Q1 to Q5)
    D(id='1a', tier='core', no='1(a)', type='fields', skill='area of a triangle', answer=[48, 24],
      q='Find the area of triangle (a). The drawing is to scale.\nStart here: triangle (a) is half of an 8 cm by 6 cm rectangle.', frame='Half of {f1} = {f2} cm²', svg=G.q1a(),
      check=lambda: [8 * 6, whole(shoelace(TRI_A))],
      hint='The rectangle is 8 cm long and 6 cm wide. What is its area? The triangle is half of it.',
      steps=['The rectangle is 8 cm by 6 cm: 8 × 6 = 48 cm².', 'Triangle (a) is half of the rectangle: 48 ÷ 2 = 24.', 'The area of (a) is 24 cm². (Also 1/2 × 8 × 6 = 24.)'],
      src=['triangle (a) is half of an 8 cm by 6 cm rectangle: half of ______ = ______ cm².', 'Find the area of each triangle. The drawings are to scale.']),
    D(id='1b', tier='core', no='1(b)', type='number', skill='area of a triangle', answer=84,
      q='Find the area of triangle (b). The drawing is to scale. The height makes a right angle (the little square) with the base. A slanting side is NOT the height.', svg=G.q1b(),
      check=lambda: whole(shoelace(TRI_B)),
      hint='Which side is the base? Which dashed line makes a right angle with it? Multiply those two lengths and take half.',
      steps=['The base is 14 cm. The height is the dashed line, 12 cm: it meets the base at a right angle.', 'Area = 1/2 × base × height = 1/2 × 14 × 12 = 84.',
             'The area is 84 cm². The slanting sides, 13 cm and 15 cm, are not the height, so they are not used.'],
      src=['In (b) and (c) the height makes a right angle (the little square) with the base. A slanting side is NOT the height.', 'Area of (b) =']),
    D(id='1c', tier='core', no='1(c)', type='number', skill='height outside the triangle', answer=36,
      q='Find the area of triangle (c). The drawing is to scale. The height makes a right angle (the little square) with the base. A slanting side is NOT the height.', svg=G.q1c(),
      check=lambda: whole(shoelace(TRI_C)),
      hint='The dashed line is only there so that the height can meet the base at a right angle. Use the base of the triangle itself, the solid side, not the dashed part.',
      steps=['The base is the solid side, 9 cm. The dashed extension is only there to reach the height.', 'The height is 8 cm.', 'Area = 1/2 × 9 × 8 = 36 cm². The 17 cm side is slanting, so it is not used.'],
      src=['Area of (c) =']),
    D(id='1d', tier='core', no='1(d)', type='set', ordered=False, grouped=False, skill='base and height', answer=[13, 15],
      q='Look at triangle (b) again. Which lengths did you NOT need to find its area? Type them in cm.', svg=G.q1b(), check=lambda: not_needed(TRI_B),
      hint='Which two lengths did you multiply to find the area? Which lengths are left over?',
      steps=['The area uses the base, 14 cm, and the height, 12 cm.', 'The other two lengths, 13 cm and 15 cm, are slanting sides. They are not at a right angle to the base, so they are not needed.'],
      src=['In (b), which lengths did you NOT need?']),

    D(id='2a', tier='core', no='2(a)', type='number', skill='same base, same height', answer=30,
      q='ABCD is a rectangle 10 cm by 6 cm. P is a point on AB.\nFind the area of triangle PDC.', svg=G.q2('P'), check=lambda: whole(shoelace([P_PT, RECT_Q2['D'], RECT_Q2['C']])),
      hint='Triangle PDC has DC as its base. How far is P above DC?',
      steps=['The base is DC = 10 cm.', 'P is on AB, which is 6 cm above DC, so the height is 6 cm.', 'Area = 1/2 × 10 × 6 = 30 cm².'],
      src=['ABCD is a rectangle 10 cm by 6 cm. P and Q are points on AB.', 'Area of triangle PDC =']),
    D(id='2b', tier='core', no='2(b)', type='number', skill='same base, same height', answer=30,
      q='ABCD is a rectangle 10 cm by 6 cm. Q is a point on AB.\nFind the area of triangle QDC.', svg=G.q2('Q'), check=lambda: whole(shoelace([Q_PT, RECT_Q2['D'], RECT_Q2['C']])),
      hint='Triangle QDC has DC as its base, too. How far is Q above DC?',
      steps=['The base is DC = 10 cm.', 'Q is on AB, which is 6 cm above DC, so the height is 6 cm.', 'Area = 1/2 × 10 × 6 = 30 cm².'],
      src=['Area of triangle QDC =']),
    D(id='2c', tier='core', no='2(c)', type='selfcheck', open=False, skill='same base, same height', facts=[(10, 6), (10, 6)],
      q='ABCD is a rectangle 10 cm by 6 cm. P and Q are points on AB.\nExplain why triangle PDC and triangle QDC have the same area. Write your idea, then compare it with the model answer.', svg=G.q2_both(False),
      check=lambda: [(length(RECT_Q2['D'], RECT_Q2['C']), RECT_Q2['A'][1] - RECT_Q2['D'][1]) for _ in (P_PT, Q_PT)], sol_fig=lambda f: G.q2_both(True),
      hint='Look at the base DC of each triangle and at how high P and Q are above DC. What is the same?',
      steps=['Both triangles have the same base, DC = 10 cm.', 'P and Q are both on AB, which is 6 cm above DC, so both triangles have the same height, 6 cm.', 'Same base and same height means the same area: 1/2 × 10 × 6 = 30 cm² each.',
             'A good explanation says “same base” and “same height”, even though the two triangles look different.'],
      src=['Explain why the two triangles have the same area.']),

    D(id='3a', tier='core', no='3(a)', type='fields', skill='splitting a figure into triangles', answer=[5, 35],
      q='Find the area of the figure ABCD. Split it into two triangles along AC.\nStart here: AC = 14 cm is the base of BOTH triangles. Read the two heights from the picture. Triangle ABC first.',
      frame='Height of triangle ABC = {f1} cm.  Area of ABC = {f2} cm²', svg=G.q3(),
      check=lambda: [QUAD['B'][1], whole(shoelace([QUAD['A'], QUAD['B'], QUAD['C']]))],
      hint='The height of ABC is the dashed line from B down to AC. Then use 1/2 × 14 × height.',
      steps=['The height from B to AC is 5 cm (read it from the picture).', 'Area of ABC = 1/2 × 14 × 5 = 35 cm².'],
      src=['Find the area of the figure ABCD. Split it into two triangles along AC.', 'Height of triangle ABC = ______ cm. Area of ABC = ______ cm²']),
    D(id='3b', tier='core', no='3(b)', type='fields', skill='splitting a figure into triangles', answer=[3, 21],
      q='Find the area of the figure ABCD. Split it into two triangles along AC.\nAC = 14 cm is the base of BOTH triangles. Now triangle ACD.',
      frame='Height of triangle ACD = {f1} cm.  Area of ACD = {f2} cm²', svg=G.q3(),
      check=lambda: [-QUAD['D'][1], whole(shoelace([QUAD['A'], QUAD['C'], QUAD['D']]))],
      hint='The height of ACD is the dashed line from D up to AC. Then use 1/2 × 14 × height.',
      steps=['The height from D to AC is 3 cm (read it from the picture).', 'Area of ACD = 1/2 × 14 × 3 = 21 cm².'],
      src=['Height of triangle ACD = ______ cm. Area of ACD = ______ cm²']),
    D(id='3c', tier='core', no='3(c)', type='number', skill='splitting a figure into triangles', answer=56,
      q='Find the area of the whole figure ABCD. Split it into two triangles along AC.', svg=G.q3(), check=lambda: whole(shoelace([QUAD['A'], QUAD['B'], QUAD['C'], QUAD['D']])),
      hint='The figure is made of the two triangles ABC and ACD. Find each area, then put them together.',
      steps=['Area of ABC = 1/2 × 14 × 5 = 35 cm² and area of ACD = 1/2 × 14 × 3 = 21 cm².', 'Area of ABCD = 35 + 21 = 56 cm².'],
      src=['Area of ABCD =']),

    D(id='4a', tier='core', no='4(a)', type='number', skill='taking away from a rectangle', answer=96,
      q='ABCD is a rectangle. Find the area of the rectangle ABCD.', svg=G.q4(), check=lambda: whole(shoelace([R4['A'], R4['B'], R4['C'], R4['D']])),
      hint='Read the length and the width of the rectangle from the picture.',
      steps=['The rectangle is 12 cm long and 8 cm wide.', 'Area = 12 × 8 = 96 cm².'],
      src=['ABCD is a rectangle. Find the area of the shaded triangle DEF.', 'Area of the rectangle ABCD =']),
    D(id='4b', tier='core', no='4(b)', type='fields', skill='taking away from a rectangle', answer=[16, 24],
      q='ABCD is a rectangle. The three white triangles are what is left over when the shaded triangle DEF is taken away. Each has a square corner, so each is half of a rectangle.\n'
        'Example: ADE is half of 4 cm by 8 cm, so ADE = 16 cm².\nFind the areas of the other two white triangles.',
      frame='EBF = {f1} cm²    FCD = {f2} cm²', svg=G.q4(),
      check=lambda: [whole(shoelace([R4['E'], R4['B'], R4['F']])), whole(shoelace([R4['F'], R4['C'], R4['D']]))],
      hint='Find the two sides of each white triangle that meet at the square corner. Each triangle is half of the rectangle with those two sides.',
      steps=['EBF has its square corner at B: EB = 8 cm and BF = 4 cm. It is half of 8 by 4: 32 ÷ 2 = 16 cm².', 'FCD has its square corner at C: FC = 4 cm and CD = 12 cm. It is half of 4 by 12: 48 ÷ 2 = 24 cm².'],
      src=['Start here: the three white triangles are what is left over. Each has a square corner, so each is half of a rectangle. Example: ADE is half of 4 cm by 8 cm, so ADE = 16 cm².', 'ADE = 16 cm² EBF = ______ cm² FCD = ______ cm²']),
    D(id='4c', tier='core', no='4(c)', type='number', skill='taking away from a rectangle', answer=40,
      q='ABCD is a rectangle. Find the area of the shaded triangle DEF.', svg=G.q4(), check=lambda: whole(shoelace([R4['D'], R4['E'], R4['F']])),
      sol_fig=lambda got: G.q4(True),
      hint='The shaded triangle is the rectangle with the three white triangles taken away. Find the area of each white triangle.',
      steps=['The rectangle is 96 cm². The three white triangles are ADE = 16 cm², EBF = 16 cm² and FCD = 24 cm².', 'The white triangles together: 16 + 16 + 24 = 56 cm².', 'Shaded area = 96 − 56 = 40 cm².'],
      src=['Area of the shaded triangle DEF =']),

    D(id='5a', tier='core', no='5(a)', type='number', skill='area of a triangle', answer=24,
      q='Mei draws a triangle with a base of 8 cm and a height of 6 cm.\nWhat is the area of Mei’s triangle?', check=lambda: whole(shoelace([(0, 0), (8, 0), (3, 6)])),
      hint='Area = 1/2 × base × height.',
      steps=['Area = 1/2 × 8 × 6 = 24 cm².'],
      src=['Mei draws a triangle with a base of 8 cm and a height of 6 cm.', 'What is the area of Mei’s triangle?']),
    D(id='5b', tier='core', no='5(b)', type='number', skill='finding a height from the area', answer=4,
      q='Mei draws a triangle with a base of 8 cm and a height of 6 cm. Siti’s triangle has the same area but a base of 12 cm.\nWhat is the height of Siti’s triangle? (Type the number of cm.)',
      check=lambda: height_from_area(whole(shoelace([(0, 0), (8, 0), (3, 6)])), 12),
      hint='First find the area of Mei’s triangle. Then ask: 1/2 × 12 × height must be that area.',
      steps=['Mei’s triangle has area 1/2 × 8 × 6 = 24 cm².', 'Siti’s triangle also has area 24 cm²: 1/2 × 12 × height = 24, so 6 × height = 24.', 'The height is 24 ÷ 6 = 4 cm.'],
      src=['Siti’s triangle has the same area but a base of 12 cm. What is its height?']),
    D(id='5c', tier='core', no='5(c)', type='selfcheck', open=False, skill='different triangles with the same area', facts=[(1, 48), (2, 24), (3, 16), (4, 12), (6, 8), (8, 6), (12, 4), (16, 3), (24, 2), (48, 1)],
      q='Mei draws a triangle with a base of 8 cm and a height of 6 cm.\nOne more triangle with the same area as Mei’s: write its base and its height in cm. Then compare with the model answer.',
      check=lambda: [(b, h) for b in range(1, 49) for h in range(1, 49) if F(b * h, 2) == 24 and (b, h) not in ((8, 6),) or False][:0] or sorted((b, 48 // b) for b in range(1, 49) if 48 % b == 0),
      hint='Choose a base you like. Then think: what height gives the same area as Mei’s triangle?',
      steps=['Mei’s triangle has area 24 cm², so base × height must be 48 (because 1/2 × base × height = 24).', 'Any base and height that multiply to 48 work. For example: base 16 cm and height 3 cm, or base 6 cm and height 8 cm, or base 12 cm and height 4 cm.',
             'Check yours: multiply your base by your height. Is it 48?'],
      src=['One more triangle with the same area:  base ______ cm, height ______ cm']),

    # ================= Investigation: Find all the ways
    D(id='C0', tier='invest', no='C (easy first step)', type='number', skill='area of a right-angled triangle', answer=6,
      q='Find all the ways.\nEasy first step: draw a right-angled triangle on squared paper with short sides 3 cm and 4 cm. What is its area?', check=lambda: whole(shoelace([(0, 0), (3, 0), (0, 4)])),
      hint='A right-angled triangle is half of a rectangle. Which rectangle?',
      steps=['The triangle is half of a 3 cm by 4 cm rectangle: 3 × 4 = 12 cm².', 'Half of 12 = 6 cm².'],
      src=['Easy first step: draw a right-angled triangle on squared paper with short sides 3 cm and 4 cm. What is its area?']),
    D(id='Ca', tier='invest', no='C(a)', type='set', ordered=True, grouped=False, skill='listing all the ways', answer=flat(pairs_for_area(6)),
      q='On square grid paper (1 square = 1 cm), a right-angled triangle has its two short sides along the grid lines, and they are whole numbers of cm. The area is exactly 6 cm². '
        'Find ALL such triangles (a triangle turned round is the same triangle).\nType each triangle as its two short sides, the smaller number first, one triangle after another. Start with the triangle whose smaller short side is smallest.',
      check=lambda: flat(pairs_for_area(6)),
      hint='The triangle is half of a rectangle. What area must that rectangle have? Which whole numbers multiply to that?',
      steps=['Each triangle is half of a rectangle, so the rectangle has area 2 × 6 = 12 cm².', 'The two short sides are whole numbers that multiply to 12: 1 and 12, 2 and 6, 3 and 4.',
             '(4 and 3 is the same triangle as 3 and 4 turned round.)', 'The three triangles are 1 and 12, 2 and 6, 3 and 4.'],
      src=['On square grid paper (1 square = 1 cm), draw right-angled triangles whose two short sides are along the grid lines and are whole numbers of cm, and whose area is exactly 6 cm². Find ALL of them (a triangle turned round is the same triangle).']),
    D(id='Cw', tier='invest', no='C(a) how do you know', type='selfcheck', open=False, skill='explaining why a list is complete', facts=pairs_for_area(6),
      q='How do you know you have them all? Write your idea, then compare it with the model answer.', check=lambda: pairs_for_area(6),
      hint='Is there a way to go through the possible short sides one by one so that none is missed?',
      steps=['The two short sides multiply to 12. List the whole numbers that go into 12 in order: 1, 2, 3, 4, 6, 12.', 'Pair each with its partner: 1 and 12, 2 and 6, 3 and 4. After 3 and 4 the pairs only repeat, turned round (4 and 3, 6 and 2, 12 and 1).',
             'A good answer lists the possibilities in order, so that none is missed, and says why the pairs repeat.'],
      src=['How do you know you have them all?']),
    D(id='Cb', tier='invest', no='C(b) mark the corner', type='selfcheck', paper=True, open=False, skill='same base, same height', facts=3,
      q='Now keep the base 4 cm along the bottom. Mark where the top corner can go so that the area is still 6 cm². Mark several places on paper (square grid paper helps), then check your marks against the picture on screen.',
      check=lambda: height_from_area(6, 4),
      sol_fig=lambda f: G.inv_line(f),
      hint='Pick a place for the top corner, draw the triangle and work out its area. Is it 6 cm²? Try another place.',
      steps=['Area = 1/2 × base × height. With a base of 4 cm and an area of 6 cm², the height is 3 cm.', 'The top corner can go anywhere that is 3 cm above the base, on a straight line parallel to the base.',
             'The corner does not have to be above the end of the base: the triangle can lean over.'],
      src=['Now keep the base 4 cm along the bottom. Mark where the top corner can go so that the area is still 6 cm².']),
    D(id='Cb2', tier='invest', no='C(b) how high', type='number', skill='same base, same height', answer=3,
      q='The base is 4 cm along the bottom and the area is still 6 cm². How high above the base must the top corner be? (Type the number of cm.)', check=lambda: height_from_area(6, 4),
      hint='Area = 1/2 × base × height. You know the area and the base.',
      steps=['6 = 1/2 × 4 × height, so 6 = 2 × height.', 'The height is 3 cm.'],
      src=['Now keep the base 4 cm along the bottom. Mark where the top corner can go so that the area is still 6 cm².']),
    D(id='Cbn', tier='invest', no='C(b) what do you notice', type='selfcheck', open=False, skill='noticing patterns', facts=True,
      q='What do you notice about all the possible top corners? Write your idea, then compare it with the model answer.',
      check=lambda: all(shoelace([(0, 0), (4, 0), (x, 3)]) == 6 for x in range(-8, 13)),
      hint='Look at how high each possible top corner is above the base. What is the same?',
      steps=['Every possible top corner is the same height above the base, 3 cm. They all lie on one straight line parallel to the base.', 'Same base (4 cm) and same height (3 cm) always give the same area, 1/2 × 4 × 3 = 6 cm², however far the triangle leans.',
             'A good answer says that the corners are in a line, 3 cm above and parallel to the base.'],
      src=['What do you notice about all the possible top corners?']),
    D(id='Cc10', tier='invest', no='C(c) 10 cm²', type='number', skill='listing all the ways', answer=3,
      q='Same rules as before: a right-angled triangle, short sides along the grid lines, whole numbers of cm (a triangle turned round is the same triangle).\nWhat if the area is 10 cm²? How many right-angled triangles can you find?',
      check=lambda: len(pairs_for_area(10)),
      hint='The triangle is half of a rectangle. What area must that rectangle have? List the whole-number pairs that multiply to it.',
      steps=['The rectangle has area 2 × 10 = 20 cm². The short sides multiply to 20.', 'The pairs are 1 and 20, 2 and 10, 4 and 5 (4 and 5 is the last pair that is not a repeat).', 'There are 3 triangles.'],
      src=['What if the area is 10 cm²? 12 cm²? How many right-angled triangles can you find each time?']),
    D(id='Cc12', tier='invest', no='C(c) 12 cm²', type='number', skill='listing all the ways', answer=4,
      q='Same rules as before. What if the area is 12 cm²? How many right-angled triangles can you find?', check=lambda: len(pairs_for_area(12)),
      hint='The triangle is half of a rectangle. What area must that rectangle have? List the whole-number pairs that multiply to it.',
      steps=['The rectangle has area 2 × 12 = 24 cm². The short sides multiply to 24.', 'The pairs are 1 and 24, 2 and 12, 3 and 8, 4 and 6.', 'There are 4 triangles.'],
      src=['12 cm²? How many right-angled triangles can you find each time?']),
    D(id='Ccm', tier='invest', no='C(c) which area', type='choice', skill='listing all the ways', options=['6 cm²', '10 cm²', '12 cm²'], answer='12 cm²',
      q='You found right-angled triangles with an area of 6 cm², 10 cm² and 12 cm². Which area gave the most triangles?',
      check=lambda: max((6, 10, 12), key=lambda a: len(pairs_for_area(a))) and f'{max((6, 10, 12), key=lambda a: len(pairs_for_area(a)))} cm²',
      hint='Count the triangles for each of the three areas, then compare the three numbers.',
      steps=['6 cm² gives 3 triangles, 10 cm² gives 3 and 12 cm² gives 4.', '12 cm² gave the most. It is double of 12, which is 24, and 24 has more pairs of factors than 12 or 20.'],
      src=['Which area gave the most?']),

    # ================= Think harder (A1 to A4)
    D(id='A1', tier='stretch', no='A1', type='number', skill='finding a height from the area', answer=9,
      q='A triangle has an area of 45 cm². Its base is 10 cm. What is its height?', check=lambda: height_from_area(45, 10),
      hint='1/2 × base × height = area. What is half of the base? What do you multiply it by to get the area?',
      steps=['1/2 × 10 × height = 45, so 5 × height = 45.', 'The height is 45 ÷ 5 = 9 cm.'],
      src=['A triangle has an area of 45 cm². Its base is 10 cm. What is its height?']),
    D(id='A2', tier='stretch', no='A2', type='number', skill='right-angled triangle', answer=96,
      q='A right-angled triangle has sides of 12 cm, 16 cm and 20 cm. What is its area?', svg=G.a2(),
      check=lambda: (lambda legs: whole(shoelace([(0, 0), (legs[1], 0), (0, legs[0])])))(sorted([12, 16, 20])[:2]) if 12 ** 2 + 16 ** 2 == 20 ** 2 else None,
      hint='In a right-angled triangle, two sides meet at the right angle. Which two are they? The longest side is slanting.',
      steps=['The two sides that meet at the right angle are 12 cm and 16 cm. The 20 cm side is slanting.', 'Area = 1/2 × 12 × 16 = 96 cm².'],
      src=['A right-angled triangle has sides of 12 cm, 16 cm and 20 cm. What is its area?']),
    D(id='A3', tier='stretch', no='A3', type='number', skill='finding a height from the area', answer=8,
      q='A triangle and a square have the same area. The square has sides of 6 cm. The triangle has a base of 9 cm. What is the height of the triangle?', svg=G.a3(), check=a3_height,
      hint='Find the area of the square first. The triangle has that area too.',
      steps=['The square has area 6 × 6 = 36 cm².', 'The triangle has the same area: 1/2 × 9 × height = 36, so 9 × height = 72.', 'The height is 72 ÷ 9 = 8 cm.'],
      src=['A triangle and a square have the same area. The square has sides of 6 cm. The triangle has a base of 9 cm. What is the height of the triangle?']),
    D(id='A4', tier='stretch', no='A4', type='number', skill='comparing areas', answer=42,
      q='A triangle and a rectangle have the same base, 12 cm, and the same height, 7 cm. What is the difference between their areas?', svg=G.a4(),
      check=lambda: whole(12 * 7 - shoelace([(0, 0), (12, 0), (4, 7)])),
      hint='Find the area of the rectangle and the area of the triangle. Then take one from the other.',
      steps=['The rectangle has area 12 × 7 = 84 cm².', 'The triangle has area 1/2 × 12 × 7 = 42 cm².', 'The difference is 84 − 42 = 42 cm².'],
      src=['A triangle and a rectangle have the same base, 12 cm, and the same height, 7 cm. What is the difference between their areas?']),

    # ================= Go further (B1 to B3)
    D(id='B1', tier='challenge', no='B1', type='number', skill='height to a slanting base', answer=12,
      q='A right-angled triangle has sides of 15 cm, 20 cm and 25 cm. What is its height when the 25 cm side is the base?', svg=G.b1(), check=b1_height,
      hint='Find the area using the two sides that meet at the right angle. Then use the same area with the 25 cm side as the base.',
      steps=['The sides that meet at the right angle are 15 cm and 20 cm. Area = 1/2 × 15 × 20 = 150 cm².', 'With the 25 cm side as the base: 1/2 × 25 × height = 150, so 25 × height = 300.', 'The height is 300 ÷ 25 = 12 cm.'],
      src=['A right-angled triangle has sides of 15 cm, 20 cm and 25 cm. What is its height when the 25 cm side is the base?']),
    D(id='B2a', tier='challenge', no='B2(a)', type='number', skill='same base, same height', answer=50,
      q='Two squares stand side by side on a line, touching: a big square of side 10 cm and a small square of side 6 cm. Join the bottom-left corner of the big square, the top-right corner of the big square and the top-right corner of the small square to make a triangle.\n'
        'What is its area?', svg=G.b2(6), check=lambda: b2_area(6),
      hint='Put the triangle in a rectangle and take away the white triangles around it. Or look for a base and a height of the triangle that you can use.',
      steps=['Put the triangle in a rectangle 16 cm by 10 cm: 160 cm².', 'The three white right-angled triangles are 1/2 × 16 × 6 = 48, 1/2 × 6 × 4 = 12 and 1/2 × 10 × 10 = 50 cm².', 'The triangle is 160 − 48 − 12 − 50 = 50 cm².'],
      src=['Two squares stand side by side on a line, touching: a big square of side 10 cm and a small square of side 6 cm. Join the bottom-left corner of the big square, the top-right corner of the big square and the top-right corner of the small square to make a triangle. What is its area?']),
    D(id='B2b', tier='challenge', no='B2(b)', type='number', skill='same base, same height', answer=50,
      q='Try again with a small square of side 4 cm (the big square still has sides of 10 cm). Join the same three corners: the bottom-left corner of the big square, the top-right corner of the big square and the top-right corner of the small square.\nWhat is the area of the triangle?',
      svg=G.b2(4), check=lambda: b2_area(4),
      hint='Use the same method as for the 6 cm square.',
      steps=['Put the triangle in a rectangle 14 cm by 10 cm: 140 cm².', 'The three white right-angled triangles are 1/2 × 14 × 4 = 28, 1/2 × 4 × 6 = 12 and 1/2 × 10 × 10 = 50 cm².', 'The triangle is 140 − 28 − 12 − 50 = 50 cm².'],
      src=['Try again with a small square of side 4 cm.']),
    D(id='B2n', tier='challenge', no='B2 notice', type='selfcheck', open=False, skill='noticing patterns', facts=[50, 50],
      q='Look at your two answers for the two small squares (6 cm and 4 cm). What do you notice? Write your idea, then compare it with the model answer.', check=lambda: [b2_area(6), b2_area(4)],
      hint='Compare the two areas with the area of the big square.',
      steps=['Both areas are 50 cm². That is half of the big square: 100 ÷ 2 = 50.', 'It would be 50 cm² for any small square. Here is why: the top-right corner of every small square is on a straight line through the bottom-right corner of the big square, parallel to the long diagonal of the big square.',
             'So the triangle has the same base (the diagonal of the big square) and the same height as the half of the big square, and the same base and same height means the same area.'],
      src=['What do you notice?']),
    D(id='B3', tier='challenge', no='B3', type='number', skill='same height, different bases', answer=18,
      q='Triangle ABC has an area of 54 cm². D is a point on BC with BD = 4 cm and DC = 8 cm. What is the area of triangle ABD?', svg=G.b3(), check=b3_area,
      hint='Find the height of triangle ABC from A down to BC. Triangle ABD has the same height.',
      steps=['BC = 4 + 8 = 12 cm. Area of ABC = 1/2 × 12 × height = 54, so 6 × height = 54 and the height from A is 9 cm.', 'Triangle ABD has base BD = 4 cm and the same height, 9 cm.', 'Area of ABD = 1/2 × 4 × 9 = 18 cm².'],
      src=['Triangle ABC has an area of 54 cm². D is a point on BC with BD = 4 cm and DC = 8 cm. What is the area of triangle ABD?']),
    D(id='pose', tier='challenge', no='Make up your own', type='selfcheck', open=True, skill='making up a problem',
      q='Make up your own. Draw a rectangle, label its sides, and join points to make a shaded triangle. Work out its area, then swap with a partner. (Think for 30 seconds before anyone speaks.)',
      hint='Pick the sides of the rectangle first. Put points on the sides at lengths you can work with, like the middle or a quarter of the way along.',
      steps=['This question is open: many puzzles are right.', 'Check your puzzle by finding the shaded area in TWO ways: split it into triangles, or take the white triangles away from the rectangle. The answers must agree.',
             'Sample: ABCD is a rectangle 10 cm by 6 cm, E is the middle of AB and F is the middle of BC. The shaded triangle is DEF (D is the bottom-left corner). Taking away: 60 − 15 − 7.5 − 15 = 22.5 cm².'],
      src=['Draw a rectangle, label its sides, and join points to make a shaded triangle. Work out its area, then swap with a partner.']),
]


# ---------------------------------------------------------------- variants: a template with an oracle (the shoelace formula on corner coordinates) for number items with readable numbers
def _b_oracle(e):
    return whole(shoelace([(0, 0), (e['b'], 0), (3, e['h'])]))


def _a1_oracle(e):
    return height_from_area(e['a'], e['b'])


def _a4_oracle(e):
    return whole(e['b'] * e['h'] - shoelace([(0, 0), (e['b'], 0), (1, e['h'])]))


def _b3_oracle(e):
    h = height_from_area(e['area'], e['BD'] + 12 - e['BD'])          # BC = BD + DC = 12 in every variant
    return whole(F(e['BD'] * h, 2))


VARIANTS = {
    '1b': dict(
        base=dict(b=14, h=12),
        tpl=dict(vars=dict(b=[10, 12, 14, 16, 18], h=[6, 8, 9, 12]), derive=dict(sl='h + 4'),
                 q='A triangle has a base of {b} cm. The height that meets the base at a right angle is {h} cm. One of its slanting sides is {sl} cm long.\nWhat is the area of the triangle?', answer='b * h / 2',
                 hint='A slanting side is not the height. Use the base and the height that meets it at a right angle.',
                 steps=['The slanting side of {sl} cm is not used.', 'Area = 1/2 × {b} × {h}.', 'The area is {ans} cm².']),
        oracle=_b_oracle),
    'A1': dict(
        base=dict(a=45, b=10),
        tpl=dict(vars=dict(a=[30, 45, 60], b=[5, 6, 10, 15]),
                 q='A triangle has an area of {a} cm². Its base is {b} cm. What is its height?', answer='2 * a / b',
                 hint='1/2 × base × height = area. Double the area, then share it by the base.',
                 steps=['1/2 × {b} × height = {a}, so {b} × height = 2 × {a}.', 'The height is {ans} cm.']),
        oracle=_a1_oracle),
    'A4': dict(
        base=dict(b=12, h=7),
        tpl=dict(vars=dict(b=[8, 10, 12, 14, 16], h=[5, 6, 7, 9]),
                 q='A triangle and a rectangle have the same base, {b} cm, and the same height, {h} cm. What is the difference between their areas?', answer='b * h - b * h / 2',
                 hint='Find the area of the rectangle and the area of the triangle. Then take one from the other.',
                 steps=['The rectangle has area {b} × {h}. The triangle has area 1/2 × {b} × {h}.', 'The difference is {ans} cm².']),
        oracle=_a4_oracle),
    'B3': dict(
        base=dict(area=54, BD=4),
        tpl=dict(vars=dict(area=[36, 48, 60, 72, 84, 96], BD=[2, 3, 4, 6]), derive=dict(DC='12 - BD'),
                 q='Triangle ABC has an area of {area} cm². D is a point on BC with BD = {BD} cm and DC = {DC} cm. What is the area of triangle ABD?', answer='area * BD / 12',
                 hint='Triangle ABC and triangle ABD have the same height, from A down to BC. Find that height first.',
                 steps=['BC = {BD} + {DC} = 12 cm. The height from A is found from the area of ABC: 1/2 × 12 × height = {area}.', 'Triangle ABD has base {BD} cm and the same height.', 'The area of ABD is {ans} cm².']),
        oracle=_b3_oracle),
}


polish(ITEMS, VARIANTS)
