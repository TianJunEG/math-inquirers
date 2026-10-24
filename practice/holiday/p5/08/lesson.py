"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 8: Angles, Triangles and Quadrilaterals ("Angle Chasers").

The questions are the ones printed in the Level 5 holiday workbook, lesson 8: Start here Q1 to Q5 (p5/content/l8.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l8.js qbank) and Go further B1 to B3 (the last three
'challenge' questions) and the "Make up your own" prompt (gaps.js), in the printed order, exactly as p5/workbook_html.js prints them.  Every answer is recomputed
by an INDEPENDENT checker below: each figure is rebuilt from coordinates (lines, triangles, parallelograms, a rhombus, a trapezium, a square with an equilateral
triangle) from the GIVEN facts only, and the unknown angles are MEASURED with atan2; the lists of isosceles triangles are found by searching every pair of base
angles; never by copying the printed answer.  build_holiday.py stops if a checker and the printed answer differ.  The figures are drawn from the same facts
(practice/holiday/p5/p5fig4.py, with a check of every printed angle).
"""
import math, os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401
import p5fig4 as G          # noqa: E402

META = dict(level=5, lesson=8, key='p5', title='Angle Chasers', workbook_title='ANGLE CHASERS', topic='Angles, Triangles and Quadrilaterals', strand='Geometry',
            sources=['p5/content/l8.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['An angle chase is a chain: find one angle, say WHY, and use it to find the next. Angles on a straight line add up to 180°. Angles at a point add up to 360°. '
                   'Where two straight lines cross, the angles opposite each other are equal. The angles of a triangle add up to 180°. An isosceles triangle has two equal base angles. '
                   'Angle BOC means the angle at O between the lines OB and OC: the letter in the middle is the corner.',
                   'Type the size of the angle in the box (a degree sign after the number is fine). The drawings are not to scale, so do not measure them: use the angle facts. '
                   'Some questions ask you to list or to explain: write your idea, then compare it with the model answer after you submit.'])
ST = 'Geometry'
F = Fraction

FACT_LINE = 'Angles on a straight line add up to 180°'
FACT_POINT = 'Angles at a point add up to 360°'
FACT_VERT = 'Vertically opposite angles are equal'
FACT_TRI = 'Angles in a triangle add up to 180°'


def D(**k):
    k.setdefault('strand', ST)
    return k


# ---------------------------------------------------------------- checkers: rebuild the figure from the given facts and measure (no formula copied from a printed answer)
def mp(v, r, deg):
    return (v[0] + r * math.cos(math.radians(deg)), v[1] + r * math.sin(math.radians(deg)))


def mang(v, a, b):
    d = abs(math.atan2(a[1] - v[1], a[0] - v[0]) - math.atan2(b[1] - v[1], b[0] - v[0])) * 180 / math.pi
    return 360 - d if d > 180 else d


def rnd(x):
    assert abs(x - round(x)) < 1e-6, x
    return int(round(x))


def isect(p, d, q, e):
    """The point where the line p + t d meets the line q + s e."""
    den = d[0] * e[1] - d[1] * e[0]
    t = ((q[0] - p[0]) * e[1] - (q[1] - p[1]) * e[0]) / den
    return (p[0] + t * d[0], p[1] + t * d[1])


def cross_lines(x):
    """Lines AB and CD cross at O with angle AOC = x.  Returns (BOC, BOD, AOD)."""
    O = (0, 0)
    A, B = mp(O, 1, 200), mp(O, 1, 20)
    C, Dd = mp(O, 1, 200 - x), mp(O, 1, 380 - x)
    assert abs(mang(O, A, C) - x) < 1e-9
    return rnd(mang(O, B, C)), rnd(mang(O, B, Dd)), rnd(mang(O, A, Dd))


def point_missing(a, b, c):
    """Four rays round a point with the angles a, b, c between neighbours: measure the angle between the last ray and the first."""
    O = (0, 0)
    rays = [mp(O, 1, 0), mp(O, 1, a), mp(O, 1, a + b), mp(O, 1, a + b + c)]
    assert rnd(mang(O, rays[0], rays[1])) == a and rnd(mang(O, rays[1], rays[2])) == b and rnd(mang(O, rays[2], rays[3])) == c
    return rnd(mang(O, rays[3], rays[0]))


def parallelogram(Aang):
    A, B = (0, 0), (120, 0)
    Dd = mp(A, 80, Aang)
    C = (Dd[0] + 120, Dd[1])
    assert rnd(mang(A, B, Dd)) == Aang
    return rnd(mang(B, A, C)), rnd(mang(C, B, Dd)), rnd(mang(Dd, A, C))


def rhombus(Pang):
    p, q = (0, 0), (100, 0)
    s = mp(p, 100, Pang)
    r = (s[0] + 100, s[1])
    assert rnd(mang(p, q, s)) == Pang
    return rnd(mang(q, p, r)), rnd(mang(p, q, r))


def trapezium(Aang, Bang):
    tA, tB = (0, 0), (100, 0)
    tD = mp(tA, 100, -Aang)
    C = isect(tB, (math.cos(math.radians(180 + Bang)), math.sin(math.radians(180 + Bang))), tD, (1, 0))
    assert rnd(mang(tA, tB, tD)) == Aang and rnd(mang(tB, tA, C)) == Bang
    return rnd(mang(tD, tA, C)), rnd(mang(C, tB, tD))


def triangle_chain(Bang, DAC):
    """Triangle ABC, D on BC with AB = AD, angle B and angle DAC given.  Returns (ADB, BAD, ADC, ACD)."""
    B, L = (0, 0), 100
    A = mp(B, L, Bang)
    t = A[0] + math.sqrt(L * L - A[1] ** 2)
    Dd = (t, 0)                                         # the other point of the line BC at distance AB from A
    assert abs(math.hypot(Dd[0] - A[0], Dd[1] - A[1]) - L) < 1e-9
    ad = math.atan2(Dd[1] - A[1], Dd[0] - A[0])
    th = ad + math.radians(DAC)                         # turn DAC degrees from AD towards C (anticlockwise, y up)
    C = isect(A, (math.cos(th), math.sin(th)), B, (1, 0))
    assert rnd(mang(A, Dd, C)) == DAC and C[0] > Dd[0]
    return rnd(mang(Dd, A, B)), rnd(mang(A, B, Dd)), rnd(mang(Dd, A, C)), rnd(mang(C, A, B))


def parallelogram_e(Babc):
    """Parallelogram ABCD with angle ABC = Babc and E on DC with DA = DE.  Returns (ADC, DEA, AEC, EAB)."""
    B, A = (0, 0), (-200, 0)
    C = mp(B, 100, 180 + Babc)
    Dd = (C[0] - 200, C[1])
    assert rnd(mang(B, A, C)) == Babc
    da = math.hypot(A[0] - Dd[0], A[1] - Dd[1])
    E = (Dd[0] + da, Dd[1])                             # on DC at distance DA from D
    assert E[0] < C[0]
    return rnd(mang(Dd, A, C)), rnd(mang(E, Dd, A)), rnd(mang(E, A, C)), rnd(mang(A, E, B))


def pe_triangle_dae(Babc):
    """The corners D, A, E of the parallelogram figure (same construction as parallelogram_e)."""
    B, A = (0, 0), (-200, 0)
    C = mp(B, 100, 180 + Babc)
    Dd = (C[0] - 200, C[1])
    da = math.hypot(A[0] - Dd[0], A[1] - Dd[1])
    return Dd, A, (Dd[0] + da, Dd[1])


def tri_kind(a, b, c):
    """isosceles / equilateral / right-angled / other, found from the side lengths and the angles."""
    s = sorted([math.hypot(a[0] - b[0], a[1] - b[1]), math.hypot(b[0] - c[0], b[1] - c[1]), math.hypot(a[0] - c[0], a[1] - c[1])])
    eq = [abs(s[0] - s[1]) < 1e-9, abs(s[1] - s[2]) < 1e-9]
    if all(eq):
        return 'equilateral'
    if any(eq):
        return 'isosceles'
    return 'right-angled' if abs(s[0] ** 2 + s[1] ** 2 - s[2] ** 2) < 1e-6 else 'other'


def square_equilateral():
    """Square ABCD with the equilateral triangle CDE outside it on DC.  Returns (ADE, DAE)."""
    A, B, C, Dd = (0, 0), (1, 0), (1, 1), (0, 1)
    E = (0.5, 1 + math.sqrt(3) / 2)
    return rnd(mang(Dd, A, E)), rnd(mang(A, Dd, E))


def isosceles_b1(Aang):
    """ABC isosceles with AB = AC and angle A given; D on AC with BD = BC.  Returns angle ABD."""
    A, L = (0, 0), 100
    B, C = mp(A, L, 270 - Aang / 2), mp(A, L, 270 + Aang / 2)
    assert rnd(mang(A, B, C)) == Aang
    u = ((A[0] - C[0]) / L, (A[1] - C[1]) / L)
    w = (C[0] - B[0], C[1] - B[1])
    t = -2 * (u[0] * w[0] + u[1] * w[1])
    Dd = (C[0] + t * u[0], C[1] + t * u[1])
    assert abs(math.hypot(Dd[0] - B[0], Dd[1] - B[1]) - math.hypot(*w)) < 1e-9
    return rnd(mang(B, A, Dd))


def square_inside_equilateral():
    A, B, C, Dd = (0, 0), (1, 0), (1, 1), (0, 1)
    E = (0.5, math.sqrt(3) / 2)
    assert rnd(mang(A, B, E)) == 60 and rnd(mang(B, A, E)) == 60
    return rnd(mang(E, Dd, C))


def halves(lo=1, hi=179):
    k = lo * 2
    while k <= hi * 2:
        yield F(k, 2)
        k += 1


def isosceles_all():
    """Every isosceles triangle on a half-degree grid, as a sorted tuple of three angles (the two equal angles are the base angles)."""
    out = []
    for b in halves(1, 89):
        top = 180 - 2 * b
        if top > 0:
            out.append(tuple(sorted((top, b, b))))
    return out


def isos_with(g):
    """The isosceles triangles that have an angle of g degrees (as the three angles, ascending)."""
    return [t for t in isosceles_all() if g in t]


def isos_30_apart():
    return [t for t in isosceles_all() if any(abs(x - y) == 30 for x in t for y in t)]


def tens_triangles(step):
    """(top, base) of every isosceles triangle whose three angles are all multiples of `step`, biggest top first."""
    out = []
    b = step
    while 180 - 2 * b > 0:
        top = 180 - 2 * b
        if top % step == 0:
            out.append((top, b))
        b += step
    return sorted(out, reverse=True)


def a1_angles():
    found = [(a, b) for a in range(1, 180) for b in range(1, 180) if a + b == 180 and a == 3 * b]
    assert len(found) == 1
    return found[0]


def deg3(t):
    return ', '.join(f'{int(x) if x == int(x) else float(x):g}°' for x in t)


CHAIN = triangle_chain(62, 38)
PE = parallelogram_e(56)
assert CHAIN == (62, 56, 118, 24) and PE == (56, 62, 118, 62)
TENS = tens_triangles(10)
FIFTEEN = tens_triangles(15)
assert len(TENS) == 8 and len(FIFTEEN) == 5

ABC_Q3 = 'In triangle ABC, D is on BC and AB = AD. Angle B = 62° and angle DAC = 38°. (Worked start: angle ADB = 62° because AB = AD, so the base angles are equal.)'
PE_Q = 'ABCD is a parallelogram. E is a point on DC with DA = DE. Angle ABC = 56°.'

ITEMS = [
    # ================= Start here (workbook lesson 8: Q1 to Q5)
    D(id='1abc', tier='core', no='1(a) to (c)', label='1(a)-(c)', type='fields', skill='angles on a line and vertically opposite', answer=[112, 68, 112],
      q='Straight lines AB and CD cross at O. Angle AOC is 68°.\nFind three more angles. (The drawing is not to scale, so do not use a protractor.)', svg=G.cross_fig(68),
      sol_fig=lambda f: G.cross_fig(68, True),
      frame='Angle BOC = {f1}°     Angle BOD = {f2}°     Angle AOD = {f3}°', check=lambda: list(cross_lines(68)),
      hint='A straight line is a half-turn, 180°. Where two lines cross, the angles opposite each other are equal.',
      steps=['Angle BOC is next to angle AOC on the straight line AB, so BOC = 180° − 68° = 112°.', 'Angle BOD is opposite angle AOC, so BOD = 68°.', 'Angle AOD is opposite angle BOC, so AOD = 112°.'],
      src=['Left: straight lines AB and CD cross at O. Right: four angles meet at a point. Drawings are not to scale, so do not use a protractor.', 'Angle BOC =', 'Angle BOD =', 'Angle AOD =']),
    D(id='1d', tier='core', no='1(d)', label='1(d)', type='fields', skill='angles at a point', answer=[65],
      q='Four angles meet at a point. They measure 95°, 130°, 70° and one more angle.\nFind the missing angle.', svg=G.point_fig(),
      sol_fig=lambda f: G.point_fig(sol=True), frame='The missing angle = {f1}°', check=lambda: [point_missing(95, 130, 70)],
      hint='A full turn is 360°.',
      steps=['The four angles round a point make a full turn, 360°.', '95° + 130° + 70° = 295°.', '360° − 295° = 65°.'],
      src=['The missing angle at the point on the right =']),
    D(id='1d2', tier='core', no='1(d) fact', label='1(d) fact', type='choice', skill='choosing an angle fact', options=[FACT_LINE, FACT_POINT, FACT_VERT, FACT_TRI], answer=FACT_POINT,
      q='Four angles meet at a point. Three of them measure 95°, 130° and 70°.\nWhich angle fact do you use to find the fourth angle?', svg=G.point_fig(),
      check=lambda: FACT_POINT if 95 + 130 + 70 + point_missing(95, 130, 70) == 360 else FACT_LINE,
      hint='The angles go all the way round the point.',
      steps=['The four angles together make a full turn round the point.', 'So the fact is: angles at a point add up to 360°.'],
      src=['Which angle fact did you use?']),

    D(id='2a', tier='core', no='2(a)', label='2(a)', type='fields', skill='angles in a parallelogram', answer=[108, 72, 108],
      q='ABCD is a parallelogram and angle A is 72°.\nFind the missing angles. (The drawing is not to scale.)', svg=G.parallelogram_fig(72), sol_fig=lambda f: G.parallelogram_fig(72, True),
      frame='Angle B = {f1}°     Angle C = {f2}°     Angle D = {f3}°', check=lambda: list(parallelogram(72)),
      hint='In a parallelogram, neighbouring angles add to 180° and opposite angles are equal.',
      steps=['Angle B is next to angle A, and neighbouring angles add to 180°: B = 180° − 72° = 108°.', 'Angle C is opposite angle A, so C = 72°.', 'Angle D is opposite angle B, so D = 108°.'],
      src=['Find the missing angles. Write each angle fact you use.', 'Parallelogram:   angle B =']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='fields', skill='angles in a rhombus', answer=[116, 32],
      q='PQRS is a rhombus and angle P is 64°. The diagonal PR is drawn.\nFind the missing angles. (The drawing is not to scale.)', svg=G.rhombus_fig(64), sol_fig=lambda f: G.rhombus_fig(64, True),
      frame='Angle PQR = {f1}°     Angle QPR = {f2}°', check=lambda: list(rhombus(64)),
      hint='A rhombus has 4 equal sides, so each triangle made by a diagonal is isosceles. Triangle PQR has PQ = QR.',
      steps=['Neighbouring angles of a rhombus add to 180°: PQR = 180° − 64° = 116°.', 'Triangle PQR is isosceles because PQ = QR, so the angles at P and R are equal.', 'QPR = (180° − 116°) ÷ 2 = 32°.'],
      src=['Rhombus:   angle PQR =']),
    D(id='2c', tier='core', no='2(c)', label='2(c)', type='fields', skill='angles in a trapezium', answer=[70, 100],
      q='ABCD is a trapezium with AB parallel to DC. Angle A is 110° and angle B is 80°.\nFind the missing angles. (The drawing is not to scale.)', svg=G.trapezium_fig(110, 80), sol_fig=lambda f: G.trapezium_fig(110, 80, sol=True),
      frame='Angle D = {f1}°     Angle C = {f2}°', check=lambda: list(trapezium(110, 80)),
      hint='In a trapezium, the angles between the parallel sides add to 180°. Which angle goes with D? Which goes with C?',
      steps=['Angle D and angle A are between the parallel sides AB and DC, so they add to 180°: D = 180° − 110° = 70°.', 'Angle C and angle B are between the parallel sides too: C = 180° − 80° = 100°.'],
      src=['Trapezium:   angle D =']),
    D(id='2f', tier='core', no='2 facts', label='2 facts', type='selfcheck', open=False, skill='giving angle facts', facts=('parallelogram', 'rhombus', 'trapezium'),
      q='Write the angle fact you used for each shape: the parallelogram, the rhombus and the trapezium. Write your idea, then compare it with the model answer.',
      check=lambda: ('parallelogram', 'rhombus', 'trapezium'), hint='Which angles were opposite? Which were neighbours? Which triangle did the diagonal make?',
      steps=['Parallelogram: neighbouring angles add to 180°, and opposite angles are equal.', 'Rhombus: neighbouring angles add to 180°, and the diagonal makes an isosceles triangle (two equal sides, so two equal angles), whose angles add to 180°.',
             'Trapezium: the angles between the parallel sides add to 180°.'],
      src=['Find the missing angles. Write each angle fact you use.']),

    D(id='3b', tier='core', no='3(b)', label='3(b)', type='number', skill='angle chase in a triangle', answer=56,
      q=ABC_Q3 + '\nFind angle BAD.', svg=G.tri_fig(), sol_fig=lambda f: G.tri_fig(('BAD',)),
      check=lambda: CHAIN[1], hint='Triangle ABD has two angles you already know. The three angles of a triangle add up to 180°.',
      steps=['In triangle ABD, angle ABD = 62° and angle ADB = 62°.', 'Angle BAD = 180° − 62° − 62° = 56°.'],
      src=['In triangle ABC, D is on BC and AB = AD. Angle B = 62° and angle DAC = 38°. Find each angle. Write each reason in words.', 'Angle BAD =']),
    D(id='3b2', tier='core', no='3(b) triangle', label='3(b) why', type='choice', skill='giving a reason', options=['triangle ABD', 'triangle ABC', 'triangle ADC'], answer='triangle ABD',
      q=ABC_Q3 + '\nAngle BAD is found because the three angles of one triangle add up to 180°. Which triangle?', svg=G.tri_fig(),
      check=lambda: [k for k, v in {'triangle ABD': [62, 62], 'triangle ABC': [62], 'triangle ADC': [38]}.items() if len(v) == 2][0], hint='Which triangle has the corner BAD, and two other angles that you already know?',
      steps=['Triangle ABD has the corner BAD, and its other two angles, ABD and ADB, are both 62°.', 'So the three angles of triangle ABD add up to 180°.'],
      src=['Angle BAD = ______  because the three angles of triangle ______ add up to ______°']),
    D(id='3c', tier='core', no='3(c)', label='3(c)', type='number', skill='angles on a straight line', answer=118,
      q=ABC_Q3 + '\nFind angle ADC.', svg=G.tri_fig(), sol_fig=lambda f: G.tri_fig(('ADC',)),
      check=lambda: CHAIN[2], hint='B, D and C are on one straight line. Angle ADB and angle ADC sit side by side on it.',
      steps=['Angle ADB is 62° and BDC is a straight line.', 'Angle ADC = 180° − 62° = 118°.'],
      src=['Angle ADC =']),
    D(id='3d', tier='core', no='3(d)', label='3(d)', type='number', skill='angle chase in a triangle', answer=24,
      q=ABC_Q3 + '\nFind angle ACD.', svg=G.tri_fig(), sol_fig=lambda f: G.tri_fig(('ACD',)),
      check=lambda: CHAIN[3], hint='Look at triangle ADC. You know angle DAC. What else can you find in it first?',
      steps=['In triangle ADC, angle DAC = 38° and angle ADC = 118°.', 'Angle ACD = 180° − 118° − 38° = 24°.'],
      src=['Angle ACD =']),
    D(id='3r', tier='core', no='3 reasons', label='3 reasons', type='selfcheck', open=False, skill='giving reasons', facts=(56, 118, 24),
      q='In triangle ABC, D is on BC and AB = AD. Write each reason in words: why is angle BAD, angle ADC and angle ACD what you found? Write your idea, then compare it with the model answer.', svg=G.tri_fig(),
      check=lambda: (CHAIN[1], CHAIN[2], CHAIN[3]), hint='Each answer used one angle fact: a triangle, a straight line, or a triangle again.',
      steps=['Angle BAD: the three angles of triangle ABD add up to 180°.', 'Angle ADC: angles on the straight line BC add up to 180°.', 'Angle ACD: the three angles of triangle ADC add up to 180°.'],
      sol_fig=lambda f: G.tri_fig(True),
      src=['Find each angle. Write each reason in words.']),

    D(id='4a', tier='core', no='4(a)', label='4(a)', type='number', skill='opposite angles of a parallelogram', answer=56,
      q=PE_Q + '\nFind angle ADC.', svg=G.para_e_fig(56), sol_fig=lambda f: G.para_e_fig(56, ('ADC',)),
      check=lambda: PE[0], hint='Look at the corner opposite angle B.',
      steps=['Angle ADC is opposite angle ABC in the parallelogram.', 'Opposite angles of a parallelogram are equal, so angle ADC = 56°.'],
      src=['ABCD is a parallelogram. E is a point on DC with DA = DE. Angle ABC = 56°.', 'Angle ADC =']),
    D(id='4a2', tier='core', no='4(a) reason', label='4(a) why', type='choice', skill='giving a reason', options=['equal', 'add up to 180°', 'add up to 360°'], answer='equal',
      q=PE_Q + '\nAngle ADC is found because opposite angles of a parallelogram are...', svg=G.para_e_fig(56),
      check=lambda: 'equal' if PE[0] == 56 else 'add up to 180°', hint='Compare angle ADC and angle ABC.',
      steps=['Angle ADC = 56° and angle ABC = 56°, so they are equal.'],
      src=['Angle ADC = _____ because opposite angles of a parallelogram are ______________']),
    D(id='4b', tier='core', no='4(b)', label='4(b)', type='number', skill='isosceles triangle in a parallelogram', answer=62,
      q=PE_Q + '\nFind angle DEA.', svg=G.para_e_fig(56), sol_fig=lambda f: G.para_e_fig(56, ('ADC', 'DEA')),
      check=lambda: PE[1], hint='DA = DE. Which two sides of triangle DAE are equal, and which angle is between them?',
      steps=['Triangle DAE is isosceles because DA = DE, and its top angle ADE is angle ADC = 56°.', 'The two base angles are equal: (180° − 56°) ÷ 2 = 62°.', 'Angle DEA = 62°.'],
      src=['Angle DEA =']),
    D(id='4b2', tier='core', no='4(b) reason', label='4(b) why', type='choice', skill='giving a reason', options=['isosceles', 'equilateral', 'right-angled'], answer='isosceles',
      q=PE_Q + '\nBecause DA = DE, triangle DAE is...', svg=G.para_e_fig(56),
      check=lambda: tri_kind(*pe_triangle_dae(56)), hint='Two of its sides are equal. What is a triangle with two equal sides called?',
      steps=['Two sides of triangle DAE are equal (DA = DE) and the third side is not marked equal.', 'A triangle with two equal sides is isosceles.'],
      src=['Angle DEA = _____ because DA = DE, so triangle DAE is ______________ and its three angles add up to ______°']),

    D(id='5l', tier='core', no='5(a) list', label='5(a) list', type='selfcheck', open=False, skill='finding every case', facts=isos_with(50),
      q='An isosceles triangle has one angle of 50°. What could the other two angles be? Find every case.\nList the triangles, then compare your list with the model answer.',
      check=lambda: isos_with(50), hint='Draw it. Is the 50° angle one of the two equal base angles, or the top angle? Try both.',
      steps=['The 50° angle can be one of the two equal base angles: then the other base angle is 50° too and the top angle is 180° − 100° = 80°. The triangle is 50°, 50°, 80°.',
             'The 50° angle can be the top angle: the two base angles are equal, (180° − 50°) ÷ 2 = 65° each. The triangle is 50°, 65°, 65°.', 'There are two triangles.'],
      src=['An isosceles triangle has one angle of 50°. What could the other two angles be? Find every case.', 'draw it. Is the 50° angle one of the two equal base angles, or the top angle? Try both.']),
    D(id='5b1', tier='core', no='5(a) base', label='5(a) base', type='fields', skill='isosceles triangle, given angle is a base angle', answer=[50, 80],
      q='An isosceles triangle has one angle of 50°.\nCase 1: the 50° angle is one of the two equal angles. Find the other two angles.',
      frame='The other equal angle: {f1}°     The third angle: {f2}°', check=lambda: [50, 180 - 2 * 50], hint='The two base angles are equal. What do the three angles add up to?',
      steps=['The other base angle is equal to the first one: 50°.', 'The top angle is 180° − 50° − 50° = 80°.'],
      src=['Is the 50° angle one of the two equal base angles, or the top angle?']),
    D(id='5b2', tier='core', no='5(a) top', label='5(a) top', type='fields', skill='isosceles triangle, given angle is the top angle', answer=[65, 65],
      q='An isosceles triangle has one angle of 50°.\nCase 2: the 50° angle is the one between the two equal sides. Find the other two angles.',
      frame='The other two angles: {f1}° and {f2}°', check=lambda: [(180 - 50) // 2] * 2, hint='The two base angles are equal. Share what is left of 180° between them.',
      steps=['180° − 50° = 130° is left for the two base angles.', 'They are equal, so each is 130° ÷ 2 = 65°.'],
      src=['Is the 50° angle one of the two equal base angles, or the top angle?']),
    D(id='5c', tier='core', no='5(b)', label='5(b)', type='number', skill='counting the isosceles triangles', answer=1,
      q='An isosceles triangle has one angle of 100°.\nHow many different triangles can you make? (Type the number.)', check=lambda: len(isos_with(100)),
      hint='Try the 100° angle as a base angle and as the top angle. Does each one work?',
      steps=['If 100° were a base angle, the other base angle would be 100° too, and 100° + 100° = 200° is already more than 180°.', 'So 100° is the top angle, and the base angles are (180° − 100°) ÷ 2 = 40° each.', 'There is only one triangle: 100°, 40°, 40°.'],
      src=['An isosceles triangle has one angle of 100°. How many different triangles can you make? Explain.']),
    D(id='5d', tier='core', no='5(b) explain', label='5(b) why', type='selfcheck', open=False, skill='explaining', facts=(40, 40, 100),
      q='An isosceles triangle has one angle of 100°. Explain how you know how many triangles there are. Write your idea, then compare it with the model answer.',
      check=lambda: tuple(int(x) for x in isos_with(100)[0]), hint='What would two angles of 100° add up to?',
      steps=['Two angles of 100° would already add up to 200°, more than the 180° in a triangle.', 'So the 100° angle must be the top angle, and the two equal base angles share 80°: 40° each.', 'A good answer says why 100° cannot be a base angle.'],
      src=['An isosceles triangle has one angle of 100°. How many different triangles can you make? Explain.']),

    # ================= Investigation: Find all the ways
    D(id='C0', tier='invest', no='C (easy first step)', label='C easy', type='fields', skill='top angle of an isosceles triangle', answer=[160, 140],
      q='Find all the ways.\nAn isosceles triangle has all three angles equal to a whole number of TENS of degrees (10°, 20°, 30° and so on).\nEasy first step: start with a base angle of 10°. The other base angle is also 10°. What is the top angle? Then try base angles of 20°.',
      frame='Base angles 10°, top angle: {f1}°     Base angles 20°, top angle: {f2}°', check=lambda: [180 - 2 * 10, 180 - 2 * 20],
      hint='The three angles add up to 180°. How much is left for the top angle after the two base angles?',
      steps=['Base angles 10° and 10°: the top angle is 180° − 20° = 160°.', 'Base angles 20° and 20°: the top angle is 180° − 40° = 140°.'],
      src=['Easy first step: start with a base angle of 10°. The other base angle is also 10°. What is the top angle? Write it as three angles. Then try 20°.']),
    D(id='Ca', tier='invest', no='C(a) list', label='C(a) list', type='selfcheck', open=False, skill='listing all the triangles', facts=TENS,
      q='An isosceles triangle has all three angles equal to a whole number of TENS of degrees (10°, 20°, 30° and so on). Find ALL the possible triangles. Write each as three angles.\nThen compare your list with the model answer.',
      check=lambda: tens_triangles(10), hint='Choose a base angle, then work out the top angle. Keep going: when must you stop?',
      steps=['Written as (top, base, base): ' + '; '.join(f'{t}, {b}, {b}' for t, b in TENS) + '.', 'Every base angle from 10° to 80° works. A base angle of 90° leaves 0° for the top angle, so there is no triangle.',
             'A good answer is a list in order, and says why it must stop at 80°.'],
      sol_fig=lambda f: G.iso_tens_fig(f),
      src=['An isosceles triangle has all three angles equal to a whole number of TENS of degrees (10°, 20°, 30° and so on). Find ALL the possible triangles. Write each as three angles.']),
    D(id='Ca2', tier='invest', no='C(a) how many', label='C(a) count', type='number', skill='counting all the triangles', answer=8,
      q='An isosceles triangle has all three angles equal to a whole number of TENS of degrees (10°, 20°, 30° and so on).\nDo the list question first. Now count the triangles in your list: how many are there? (Type the number.)', check=lambda: len(tens_triangles(10)),
      hint='List them in order of the base angle, and count the rows.',
      steps=['The base angles can be 10°, 20°, 30°, 40°, 50°, 60°, 70° or 80°.', 'That is 8 triangles.'],
      src=['Find ALL the possible triangles.']),
    D(id='Cb', tier='invest', no='C(b) over 90', label='C(b) over 90', type='number', skill='comparing the triangles', answer=4,
      q='Think about all the isosceles triangles with angles that are whole numbers of TENS of degrees.\nHow many of them have an angle bigger than 90°? (Type the number.)',
      check=lambda: len([1 for t, b in tens_triangles(10) if max(t, b) > 90]), hint='Look at your list. Which angle can be bigger than 90°: a base angle or the top angle?',
      steps=['A base angle is never bigger than 90°, because two of them are equal and would add up to more than 180°.', 'The top angle is bigger than 90° for the triangles with base angles 10°, 20°, 30° and 40°: tops of 160°, 140°, 120° and 100°.', 'That is 4 triangles.'],
      src=['How many of your triangles have an angle bigger than 90°?']),
    D(id='Cb2', tier='invest', no='C(b) equilateral', label='C(b) equil', type='choice', skill='the equilateral triangle',
      options=['100°, 40°, 40°', '80°, 50°, 50°', '60°, 60°, 60°', '40°, 70°, 70°'], answer='60°, 60°, 60°',
      q='Here are four of the isosceles triangles with angles that are whole numbers of tens of degrees (written as top, base, base).\nWhich one is equilateral?',
      check=lambda: [s for s, (t, b) in (('100°, 40°, 40°', (100, 40)), ('80°, 50°, 50°', (80, 50)), ('60°, 60°, 60°', (60, 60)), ('40°, 70°, 70°', (40, 70))) if t == b][0],
      hint='An equilateral triangle has three equal sides, so three equal angles.',
      steps=['An equilateral triangle has three equal angles.', 'Only 60°, 60°, 60° has all three angles equal (and 3 × 60° = 180°).'],
      src=['Which one is equilateral?']),
    D(id='Cc', tier='invest', no='C(c) multiples of 15', label='C(c) 15', type='number', skill='counting all the triangles', answer=5,
      q='What if the angles are multiples of 15° instead (15°, 30°, 45° and so on)?\nHow many isosceles triangles are there now? (Type the number.)', check=lambda: len(tens_triangles(15)),
      hint='Use the same plan as before: choose a base angle, then work out the top angle.',
      steps=['The triangles written as (top, base, base): ' + '; '.join(f'{t}, {b}, {b}' for t, b in FIFTEEN) + '.', 'Every top angle is also a multiple of 15°. That is 5 triangles.'],
      src=['What if the angles are multiples of 15° instead? How many triangles now? What stays the same in your method?']),
    D(id='Cc2', tier='invest', no='C(c) same method', label='C(c) method', type='selfcheck', open=False, skill='explaining a method', facts=(10, 15),
      q='What stays the same in your method when the angles are multiples of 15° instead of 10°? Write your idea, then compare it with the model answer.',
      check=lambda: (10, 15), hint='Think about the steps you took to make your list for tens of degrees.',
      steps=['Choose a base angle that is a multiple of the step, and work out the top angle: top = 180° − 2 × base.', 'Stop when the top angle would be 0° or less. The list is made the same way for 10° and for 15°.',
             'A good answer says that the base angle is chosen first, and the top angle comes from it.'],
      src=['What if the angles are multiples of 15° instead? How many triangles now? What stays the same in your method?']),

    # ================= Think harder (A1 to A4)
    D(id='A1', tier='stretch', no='A1', type='fields', skill='angles of a parallelogram with a ratio', answer=[135, 45],
      q='In parallelogram ABCD, angle A is 3 times angle B.\nFind angle A and angle B. (The drawing is not to scale.)', svg=G.a1_fig('3 × B'), sol_fig=lambda f: G.a1_fig(sol=(135, 45)),
      frame='Angle A = {f1}°     Angle B = {f2}°', check=lambda: list(a1_angles()),
      hint='Neighbouring angles of a parallelogram add up to 180°. Think of angle B as one part: how many parts is angle A?',
      steps=['Neighbouring angles A and B add up to 180°.', 'Angle B is 1 part and angle A is 3 parts, so 4 equal parts make 180°. One part is 180° ÷ 4 = 45°.', 'B = 45° and A = 3 × 45° = 135°.'],
      src=['In parallelogram ABCD, angle A is 3 times angle B. Find angle A and angle B. Give your reason.']),
    D(id='A1w', tier='stretch', no='A1 reason', label='A1 why', type='selfcheck', open=False, skill='giving a reason', facts=(135, 45),
      q='In parallelogram ABCD, angle A is 3 times angle B. Give your reason for the sizes of angle A and angle B. Write your idea, then compare it with the model answer.',
      check=lambda: a1_angles(), hint='Which two angles of a parallelogram are neighbours, and what do they add up to?',
      steps=['Neighbouring angles of a parallelogram add up to 180°.', 'A and B are neighbours: 4 equal parts make 180°, so B = 45° and A = 135°.'], sol_fig=lambda f: G.a1_fig(sol=(135, 45)),
      src=['In parallelogram ABCD, angle A is 3 times angle B. Find angle A and angle B. Give your reason.']),
    D(id='A2', tier='stretch', no='A2', type='fields', skill='isosceles triangle with a big angle', answer=[35, 35],
      q='An isosceles triangle has an angle of 110°.\nFind the other two angles.', frame='The other two angles: {f1}° and {f2}°', check=lambda: [int(x) for x in isos_with(110)[0] if x != 110],
      hint='The three angles add up to 180°. Is the 110° angle one of the two equal angles, or the odd one out?',
      steps=['The 110° angle is the top angle, and the base angles are equal.', '180° − 110° = 70° is shared by the two base angles: 70° ÷ 2 = 35° each.'],
      src=['An isosceles triangle has an angle of 110°. Find the other two angles. Why is there only one answer?']),
    D(id='A2w', tier='stretch', no='A2 why', label='A2 why', type='selfcheck', open=False, skill='explaining', facts=(35, 35, 110),
      q='An isosceles triangle has an angle of 110°. Explain why there is only one possible answer. Write your idea, then compare it with the model answer.',
      check=lambda: tuple(int(x) for x in isos_with(110)[0]), hint='What would happen if 110° were one of the two equal angles?',
      steps=['110° cannot be a base angle: two base angles of 110° would add up to 220°, more than 180°.', 'So 110° is the top angle, and the other two angles are 35° each.'],
      src=['An isosceles triangle has an angle of 110°. Find the other two angles. Why is there only one answer?']),
    D(id='A3', tier='stretch', no='A3', type='fields', skill='angle chase in a parallelogram', answer=[118, 62],
      q='ABCD is a parallelogram and E is a point on DC with DA = DE. Angle ABC = 56°. (The figure is the same one as in Start here Q4.)\nFind angle AEC and angle EAB.', svg=G.para_e_fig(56),
      sol_fig=lambda f: G.para_e_fig(56, ('ADC', 'DEA', 'AEC', 'EAB')),
      frame='Angle AEC = {f1}°     Angle EAB = {f2}°', check=lambda: [PE[2], PE[3]],
      hint='Work step by step: opposite angles, then the isosceles triangle DAE, then the straight line DC. Neighbouring angles of the parallelogram add to 180°.',
      steps=['Angle ADC = 56° (opposite angles). Angle DEA = (180° − 56°) ÷ 2 = 62° (DA = DE).', 'Angle AEC = 180° − 62° = 118° (angles on the straight line DC).',
             'Angle DAB = 180° − 56° = 124° (neighbouring angles), so angle EAB = 124° − 62° = 62°.'],
      src=['ABCD is a parallelogram and E is a point on DC with DA = DE. Angle ABC = 56°. (The figure is the same one as in Start here Q4.) Find angle AEC and angle EAB. Write the reason for each step.']),
    D(id='A3w', tier='stretch', no='A3 reasons', label='A3 reasons', type='selfcheck', open=False, skill='giving reasons', facts=(118, 62),
      q='ABCD is a parallelogram and E is a point on DC with DA = DE. Angle ABC = 56°.\nWrite the reason for each step of finding angle AEC and angle EAB. Write your idea, then compare it with the model answer.', svg=G.para_e_fig(56),
      check=lambda: (PE[2], PE[3]), hint='Each step uses one fact: opposite angles, an isosceles triangle, a straight line, neighbouring angles.',
      steps=['ADC = 56°: opposite angles of a parallelogram are equal.', 'DEA = 62°: DA = DE, so triangle DAE is isosceles and (180° − 56°) ÷ 2 = 62°.', 'AEC = 118°: angles on the straight line DC add up to 180°.',
             'DAB = 124°: neighbouring angles of a parallelogram add up to 180°; so EAB = 124° − 62° = 62°.'], sol_fig=lambda f: G.para_e_fig(56, ('ADC', 'DEA', 'AEC', 'EAB')),
      src=['Find angle AEC and angle EAB. Write the reason for each step.']),
    D(id='A4', tier='stretch', no='A4', type='fields', skill='square and equilateral triangle', answer=[150, 15],
      q='ABCD is a square. CDE is an equilateral triangle, and E is outside the square.\nFind angle ADE and angle DAE.', svg=G.a4_fig(), sol_fig=lambda f: G.a4_fig(True),
      frame='Angle ADE = {f1}°     Angle DAE = {f2}°', check=lambda: list(square_equilateral()),
      hint='Angle ADE is made of two corners side by side. Then look at triangle ADE: which two of its sides are equal?',
      steps=['Angle ADE = 90° (the square) + 60° (the equilateral triangle) = 150°.', 'DE = DC (equilateral) and DC = DA (square), so DA = DE and triangle ADE is isosceles.', 'Angle DAE = (180° − 150°) ÷ 2 = 15°.'],
      src=['ABCD is a square. CDE is an equilateral triangle, and E is outside the square. Find angle ADE and angle DAE.']),

    # ================= Go further (B1 to B3)
    D(id='B1', tier='challenge', no='B1', type='number', skill='longer angle chase', answer=30,
      q='ABC is an isosceles triangle with AB = AC and angle BAC = 40°. D is a point on AC with BD = BC.\nFind angle ABD. (Type the number of degrees.)', svg=G.b1_fig(40), sol_fig=lambda f: G.b1_fig(40, True),
      check=lambda: isosceles_b1(40), hint='Find the base angles of triangle ABC first. Then use BD = BC in triangle BCD.',
      steps=['Angles B and C of triangle ABC are (180° − 40°) ÷ 2 = 70° each.', 'In triangle BCD, BD = BC, so angle BDC = angle C = 70°, and angle CBD = 180° − 70° − 70° = 40°.', 'Angle ABD = 70° − 40° = 30°.'],
      src=['ABC is an isosceles triangle with AB = AC and angle BAC = 40°. D is a point on AC with BD = BC. Find angle ABD.']),
    D(id='B2', tier='challenge', no='B2', type='number', skill='longer angle chase', answer=150,
      q='ABCD is a square. E is a point inside it so that ABE is an equilateral triangle.\nFind angle DEC. (Type the number of degrees.)', svg=G.b2_fig(), sol_fig=lambda f: G.b2_fig(True),
      check=square_inside_equilateral, hint='Look for equal sides: AE equals AB because ABE is equilateral. What else equals AB?',
      steps=['AE = AB = AD, so triangle ADE is isosceles with angle DAE = 90° − 60° = 30°. Its base angles are (180° − 30°) ÷ 2 = 75°, so angle AED = 75°.',
             'In the same way angle BEC = 75°, and angle AEB = 60°.', 'The angles round E add up to 360°: angle DEC = 360° − 75° − 75° − 60° = 150°.'],
      src=['ABCD is a square. E is a point inside it so that ABE is an equilateral triangle. Find angle DEC.']),
    D(id='B3l', tier='challenge', no='B3 list', label='B3 list', type='selfcheck', open=False, skill='finding every case', facts=isos_30_apart(),
      q='In an isosceles triangle, one angle is 30° bigger than another angle. Find all the possible sets of three angles.\nList them, then compare your list with the model answer.',
      check=lambda: isos_30_apart(), hint='The angle that is 30° bigger could be the top angle or a base angle. Try both.',
      steps=['If the top angle is 30° bigger than a base angle, then 3 equal base-angle parts and 30° make 180°, so the base angle is 50° and the top angle is 80°: 50°, 50°, 80°.',
             'If a base angle is 30° bigger than the top angle, the top angle is 40° and the base angles are 70° each: 40°, 70°, 70°.', 'There are two sets.'],
      src=['In an isosceles triangle, one angle is 30° bigger than another angle. Find all the possible sets of three angles.']),
    D(id='B3c', tier='challenge', no='B3 how many', label='B3 count', type='number', skill='counting every case', answer=2,
      q='In an isosceles triangle, one angle is 30° bigger than another angle.\nDo the list question first. Now count the sets in your list: how many are there? (Type the number.)', check=lambda: len(isos_30_apart()),
      hint='Make a list of the possible triangles first.',
      steps=['The bigger angle can be the top angle (50°, 50°, 80°) or a base angle (40°, 70°, 70°).', 'That is 2 sets.'],
      src=['In an isosceles triangle, one angle is 30° bigger than another angle. Find all the possible sets of three angles.']),
    D(id='pose', tier='challenge', no='Make up your own', label='Make up', type='selfcheck', open=True, marking_mode='open', skill='making up a problem',
      q='Make up an angle puzzle with a triangle and a parallelogram (or a rhombus) that share a side. Give two or three angles and ask for one more. Then work out the answer yourself.',
      hint='Draw the shapes on paper first. Choose the given angles so that you can find the answer in two or three steps.',
      steps=['This question is open: many puzzles are right.', 'Check that every step of your answer has an angle fact as its reason, and that the angles you give do not contradict each other.',
             'Sample: ABCD is a parallelogram with angle ABC = 56°, and E is on DC with DA = DE. Find angle EAB: 62°.'],
      src=['Draw a triangle and a parallelogram that share a side. Give two or three angles and ask for one more.']),
]


# ---------------------------------------------------------------- variants: a template with an oracle that rebuilds the figure and measures
def _o_1abc(e):
    return dict(zip(('f1', 'f2', 'f3'), cross_lines(e['x'])))


def _o_1d(e):
    return point_missing(e['a'], e['b'], e['c'])


def _o_4a(e):
    return parallelogram_e(e['g'])[0]


def _o_4b(e):
    return parallelogram_e(e['g'])[1]


def _o_a3(e):
    r = parallelogram_e(e['g'])
    return dict(f1=r[2], f2=r[3])


def _o_5b1(e):
    t = [x for x in isos_with(e['g']) if x[0] == x[1] or x[1] == x[2]]
    base = [x for x in t if sorted(x).count(e['g']) == 2][0]          # g appears twice: g is a base angle
    return dict(f1=e['g'], f2=int(max(base) if max(base) != e['g'] else min(base)))


def _o_5b2(e):
    top = [x for x in isos_with(e['g']) if sorted(x).count(e['g']) == 1][0]
    b = [int(x) for x in top if x != e['g']]
    return dict(f1=b[0], f2=b[1])


def _o_a1(e):
    k = e['k']
    found = [(a, b) for a in range(1, 180) for b in range(1, 180) if a + b == 180 and a == k * b]
    assert len(found) == 1
    return dict(f1=found[0][0], f2=found[0][1])


def _o_a2(e):
    return dict(zip(('f1', 'f2'), [int(x) for x in isos_with(e['g'])[0] if x != e['g']]))


def _o_b1(e):
    return isosceles_b1(e['A'])


def _o_cc(e):
    return len(tens_triangles(e['s']))


finish(ITEMS)

VARIANTS = {
    '1abc': dict(
        base=dict(x=68),
        tpl=dict(vars=dict(x=[48, 52, 58, 68, 74, 82]),
                 q='Straight lines AB and CD cross at O. Angle AOC is {x}°.\nFind three more angles. (The drawing is not to scale, so do not use a protractor.)',
                 frame='Angle BOC = {f1}°     Angle BOD = {f2}°     Angle AOD = {f3}°', answers=dict(f1='180 - x', f2='x', f3='180 - x'),
                 hint='A straight line is a half-turn, 180°. Where two lines cross, the angles opposite each other are equal.',
                 steps=['Angle BOC is next to angle AOC on a straight line: 180° − {x}°.', 'Angle BOD is opposite angle AOC, and angle AOD is opposite angle BOC.', 'The three angles are {ans}.']),
        fig=lambda e: G.cross_fig(e['x']),
        oracle=_o_1abc),
    '1d': dict(
        base=dict(a=95, b=130, c=70),
        tpl=dict(vars=dict(a=[70, 95, 110], b=[100, 120, 130], c=[50, 70, 80]),
                 q='Four angles meet at a point. They measure {a}°, {b}°, {c}° and one more angle.\nFind the missing angle.', frame='The missing angle = {f1}°', answers=dict(f1='360 - a - b - c'),
                 hint='A full turn is 360°.', steps=['The four angles round a point make a full turn, 360°.', 'Add the three angles you know, {a}° + {b}° + {c}°, and take the total away from 360°.', 'The missing angle is {ans} degrees.']),
        fig=lambda e: G.point_fig(e['a'], e['b'], e['c']),
        oracle=lambda e: dict(f1=_o_1d(e))),
    '4a': dict(
        base=dict(g=56),
        tpl=dict(vars=dict(g=[48, 56, 64, 72, 76]),
                 q='ABCD is a parallelogram. E is a point on DC with DA = DE. Angle ABC = {g}°.\nFind angle ADC. (The drawing is not to scale.)', answer='g',
                 hint='Look at the corner opposite angle B.', steps=['Angle ADC is opposite angle ABC in the parallelogram.', 'Opposite angles of a parallelogram are equal, so angle ADC is {ans} degrees.']),
        fig=lambda e: G.para_e_fig(e['g']),
        oracle=_o_4a),
    '4b': dict(
        base=dict(g=56),
        tpl=dict(vars=dict(g=[48, 56, 64, 72, 76]),
                 q='ABCD is a parallelogram. E is a point on DC with DA = DE. Angle ABC = {g}°.\nFind angle DEA. (The drawing is not to scale.)', answer='(180 - g) / 2',
                 hint='DA = DE. Which two sides of triangle DAE are equal, and which angle is between them?',
                 steps=['Triangle DAE is isosceles because DA = DE, and its top angle ADE is equal to angle ABC, {g}°.', 'The two base angles are equal: (180° − {g}°) ÷ 2.', 'Angle DEA = {ans} degrees.']),
        fig=lambda e: G.para_e_fig(e['g']),
        oracle=_o_4b),
    '5b1': dict(
        base=dict(g=50),
        tpl=dict(vars=dict(g=[40, 50, 70, 80]),
                 q='An isosceles triangle has one angle of {g}°.\nCase 1: the {g}° angle is one of the two equal angles. Find the other two angles.',
                 frame='The other equal angle: {f1}°     The third angle: {f2}°', answers=dict(f1='g', f2='180 - 2 * g'),
                 hint='The two base angles are equal. What do the three angles add up to?',
                 steps=['The other base angle is equal to the first one: {g}°.', 'The top angle is 180° − {g}° − {g}°.', 'The angles are {ans}.']),
        oracle=_o_5b1),
    '5b2': dict(
        base=dict(g=50),
        tpl=dict(vars=dict(g=[20, 30, 40, 50, 70, 80]),
                 q='An isosceles triangle has one angle of {g}°.\nCase 2: the {g}° angle is the one between the two equal sides. Find the other two angles.',
                 frame='The other two angles: {f1}° and {f2}°', answers=dict(f1='(180 - g) / 2', f2='(180 - g) / 2'),
                 hint='The two base angles are equal. Share what is left of 180° between them.',
                 steps=['180° − {g}° is left for the two base angles.', 'They are equal, so share it between the two.', 'The base angles are {ans}.']),
        oracle=_o_5b2),
    'A1': dict(
        base=dict(k=3),
        tpl=dict(vars=dict(k=[2, 3, 4, 5]),
                 q='In parallelogram ABCD, angle A is {k} times angle B.\nFind angle A and angle B. (The drawing is not to scale.)', frame='Angle A = {f1}°     Angle B = {f2}°',
                 answers=dict(f1='180 * k / (k + 1)', f2='180 / (k + 1)'),
                 hint='Neighbouring angles of a parallelogram add up to 180°. Think of angle B as one part: how many parts is angle A?',
                 steps=['Neighbouring angles A and B add up to 180°.', 'Angle B is 1 part and angle A is {k} parts, so {k} + 1 equal parts make 180°.', 'The two angles are {ans}.'],
                 fig=G.a1_fig('{k} × B')),
        oracle=_o_a1),
    'A2': dict(
        base=dict(g=110),
        tpl=dict(vars=dict(g=[100, 110, 120, 130, 140, 150, 160]),
                 q='An isosceles triangle has an angle of {g}°.\nFind the other two angles.', frame='The other two angles: {f1}° and {f2}°', answers=dict(f1='(180 - g) / 2', f2='(180 - g) / 2'),
                 hint='The three angles add up to 180°. Is the {g}° angle one of the two equal angles, or the odd one out?',
                 steps=['Two angles of {g}° would add up to more than 180°, so the {g}° angle is the top angle.', '180° − {g}° is shared by the two equal base angles.', 'The other two angles are {ans}.']),
        oracle=_o_a2),
    'A3': dict(
        base=dict(g=56),
        tpl=dict(vars=dict(g=[48, 56, 64, 72, 76, 80]),
                 q='ABCD is a parallelogram and E is a point on DC with DA = DE. Angle ABC = {g}°.\nFind angle AEC and angle EAB. (The drawing is not to scale.)', frame='Angle AEC = {f1}°     Angle EAB = {f2}°',
                 answers=dict(f1='90 + g / 2', f2='90 - g / 2'),
                 hint='Work step by step: opposite angles, then the isosceles triangle DAE, then the straight line DC. Neighbouring angles of the parallelogram add to 180°.',
                 steps=['Angle ADC = {g}°. Angle DEA = (180° − {g}°) ÷ 2 (DA = DE).', 'Angle AEC = 180° − angle DEA (angles on the straight line DC).', 'Angle EAB = (180° − {g}°) − angle DEA. The two angles are {ans}.']),
        fig=lambda e: G.para_e_fig(e['g']),
        oracle=_o_a3),
    'B1': dict(
        base=dict(A=40),
        tpl=dict(vars=dict(A=[20, 30, 40, 50]),
                 q='ABC is an isosceles triangle with AB = AC and angle BAC = {A}°. D is a point on AC with BD = BC.\nFind angle ABD. (Type the number of degrees.)', answer='(180 - A) / 2 - A',
                 hint='Find the base angles of triangle ABC first. Then use BD = BC in triangle BCD.',
                 steps=['Angles B and C of triangle ABC are (180° − {A}°) ÷ 2 each.', 'In triangle BCD, BD = BC, so angle BDC = angle C and angle CBD = {A}°.', 'Angle ABD = angle ABC − angle CBD = {ans} degrees.']),
        fig=lambda e: G.b1_fig(e['A']),
        oracle=_o_b1),
    'Cc': dict(
        base=dict(s=15),
        tpl=dict(vars=dict(s=[10, 15, 18, 30, 45]),
                 q='An isosceles triangle has all three angles equal to a multiple of {s}° ({s}°, 2 × {s}°, 3 × {s}° and so on).\nHow many different triangles are there? (Type the number.)', answer='90 / s - 1',
                 hint='Choose a base angle, then work out the top angle. When must you stop?',
                 steps=['Choose a base angle that is a multiple of {s}°, and work out the top angle: 180° − 2 × the base angle.', 'The base angle must be less than 90°, or there is no top angle.', 'There are {ans} triangles.']),
        oracle=_o_cc),
}


polish(ITEMS, VARIANTS)

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Explain',
    'Two angles are on a straight line. One angle is 70 degrees. Find the other angle and explain how you know. Start: I know because ...',
    ['The other angle is 110 degrees.', 'For example: I know because angles on a straight line add up to 180 degrees, and 180 - 70 = 110.'],
    'What do angles on a straight line add up to?'))
