"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 7: 2D Shapes ("Shape Safari").

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 7, Q1 to Q6; hp/qbank.json lesson 7 stretch[0:4] for Think harder and challenge[-3:] for Go further, as the
workbook builder slices them; hp/gaps.json lesson 7 for the Investigation).  The pictures are redrawn from the printed ones (hp/house.png, shapes6.png, trifigs_ab.png, grid2x2.png, tri_lines.png,
nested_sq.png).  Every answer is recomputed by an independent checker that works from the DRAWN GEOMETRY, not from the printed number: shapes are named from their corner coordinates (sides, equal
sides, square corners); the sides and corners of a polygon are counted from points along its boundary; triangles are counted by joining every triple of points of a figure that are pairwise joined by
drawn lines; squares are counted from the drawn unit edges of a grid; two same-size triangles are joined along a whole side in every way and the result is named; shapes of joined squares are listed
and turned/flipped copies merged.  The build stops if a checker and the printed answer (Tutor Guide answer key) differ.
"""
import itertools, math, os, sys
from collections import Counter
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p1lib import *      # noqa: E402,F401

META = dict(level=1, lesson=7, key='p1', title='Shape Safari', workbook_title='SHAPE SAFARI', topic='2D Shapes',
            strand='Shapes: 2D shapes',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['Shapes have sides and corners. Count the small shapes first, then the bigger shapes made of smaller ones.',
                   'Some questions ask you to draw. Do those on paper, then check your drawing against the answer shown on screen.'])

S = 'Shapes: 2D shapes'


def D(**k):
    return dict(strand=S, **k)


# ======================================================================== independent checkers (geometry)
def props(pts):
    """(number of corners, all sides equal, number of square corners) of a polygon given by its corner points."""
    n = len(pts)
    sides = [(pts[i][0] - pts[(i + 1) % n][0]) ** 2 + (pts[i][1] - pts[(i + 1) % n][1]) ** 2 for i in range(n)]
    right = 0
    for i in range(n):
        p, q, r = pts[i - 1], pts[i], pts[(i + 1) % n]
        ux, uy, vx, vy = p[0] - q[0], p[1] - q[1], r[0] - q[0], r[1] - q[1]
        if abs(ux * vx + uy * vy) <= 1e-9 * math.sqrt((ux * ux + uy * uy) * (vx * vx + vy * vy)):
            right += 1
    equal = all(abs(s - sides[0]) <= 1e-9 * sides[0] for s in sides)
    return n, equal, right


def shape_name(pts):
    """The name of a drawn shape, from its corners: None points = a round shape (circle)."""
    if pts is None:
        return 'circle'
    n, eq, right = props(pts)
    if n == 3:
        return 'triangle'
    if n == 4:
        return ('square' if eq else 'rectangle') if right == 4 else 'four-sided shape'
    return {5: 'pentagon', 6: 'hexagon', 8: 'octagon'}.get(n, f'{n}-sided shape')


def boundary(pts, per=4):
    """The outline of a polygon as many points: each side is cut into `per` equal pieces (so a side is not recognised by its number of points)."""
    out = []
    for i in range(len(pts)):
        a, b = pts[i], pts[(i + 1) % len(pts)]
        out += [(a[0] + (b[0] - a[0]) * k / per, a[1] + (b[1] - a[1]) * k / per) for k in range(per)]
    return out


def sides_and_corners(pts):
    """Straight sides = runs of the outline that keep the same direction; corners = outline points where the direction turns (cross product of the two steps)."""
    b = boundary(pts)
    m = len(b)
    steps = [(b[(i + 1) % m][0] - b[i][0], b[(i + 1) % m][1] - b[i][1]) for i in range(m)]
    unit = [tuple(round(v / math.hypot(*s), 5) + 0.0 for v in s) for s in steps]
    sides = sum(1 for i in range(m) if unit[i] != unit[i - 1])
    corners = sum(1 for i in range(m) if abs(steps[i - 1][0] * steps[i][1] - steps[i - 1][1] * steps[i][0]) > 1e-6 * math.hypot(*steps[i - 1]) * math.hypot(*steps[i]))
    return sides, corners


def regular(n, r=100):
    return regular_pts(n, 0, 0, r)


# ---- the house picture (drawing units: the printed 660 x 400 picture)
HOUSE = [('circle', 585, 68, 47, '#FFDC7A'),
         ('poly', [(150, 198), (510, 198), (510, 380), (150, 380)], '#F2E1C0'),                       # the house
         ('poly', [(295, 285), (370, 285), (370, 380), (295, 380)], '#C9B596'),                        # the door
         ('poly', [(180, 230), (230, 230), (230, 280), (180, 280)], '#C9E4F5'),                        # window 1
         ('poly', [(240, 230), (290, 230), (290, 280), (240, 280)], '#C9E4F5'),                        # window 2
         ('poly', [(420, 230), (470, 230), (470, 280), (420, 280)], '#C9E4F5'),                        # window 3
         ('poly', [(145, 193), (330, 75), (520, 193)], '#E8B4A0'),                                    # the roof
         ('line', 330, 75, 330, 8),                                                                     # the flag pole
         ('poly', [(335, 8), (425, 30), (335, 52)], '#E8503A')]                                       # the flag


def house_counts():
    c = Counter('circle' if p[0] == 'circle' else shape_name(p[1]) for p in HOUSE if p[0] in ('circle', 'poly'))
    return c


def house_row():
    c = house_counts()
    return [c['circle'], c['triangle'], c['square'], c['rectangle']]


def house_fig():
    return picture_parts(HOUSE, 660, 400, 'A house with a flag and a sun: a roof, a house, a door, three windows, a flag pole and a flag')


# ---- candidate shapes for "Who am I?" (corner points; None = round)
CANDS = {'Circle': None, 'Triangle': [(0, 0), (10, 0), (5, 9)], 'Square': [(0, 0), (10, 0), (10, 10), (0, 10)], 'Rectangle': [(0, 0), (14, 0), (14, 10), (0, 10)],
         'Pentagon': regular(5), 'Hexagon': regular(6)}
SHAPE_OPTS = list(CANDS)


def who_am_i(test):
    got = [nm for nm, pts in CANDS.items() if test(pts)]
    return got[0] if len(got) == 1 else None


# ---- counting triangles in a figure of drawn lines
def _pt(p):
    return (F(p[0]), F(p[1]))


def on_seg(p, s):
    (x1, y1), (x2, y2) = s
    if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) != 0:
        return False
    return min(x1, x2) <= p[0] <= max(x1, x2) and min(y1, y2) <= p[1] <= max(y1, y2)


def seg_cross(s, t):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = s[0], s[1], t[0], t[1]
    d = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if d == 0:
        return None
    a = F((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3), 1) / d
    b = F((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1), 1) / d
    return (x1 + a * (x2 - x1), y1 + a * (y2 - y1)) if 0 <= a <= 1 and 0 <= b <= 1 else None


def count_triangles(segs):
    """Triangles in a figure of drawn segments: every triple of the figure's points (ends of lines and where lines cross) that are joined in pairs by drawn lines and not on one line."""
    segs = [(_pt(a), _pt(b)) for a, b in segs]
    pts = {p for s in segs for p in s}
    for s, t in itertools.combinations(segs, 2):
        c = seg_cross(s, t)
        if c is not None:
            pts.add(c)
    pts = sorted(pts)
    joined = lambda p, q: any(on_seg(p, s) and on_seg(q, s) for s in segs)
    n = 0
    for p, q, r in itertools.combinations(pts, 3):
        if (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]) != 0 and joined(p, q) and joined(q, r) and joined(p, r):
            n += 1
    return n


def lines_figure(n):
    """A big triangle with n lines from the top corner to the bottom edge."""
    W = 12
    apex = (W // 2, 8)
    return [((0, 0), (W, 0)), ((0, 0), apex), ((W, 0), apex)] + [(apex, (F(W * i, n + 1), 0)) for i in range(1, n + 1)]


TRI_A = [((0, 0), (4, 0)), ((0, 0), (2, 3)), ((4, 0), (2, 3)), ((2, 3), (2, 0))]
SQ = [((0, 0), (3, 0)), ((3, 0), (3, 3)), ((3, 3), (0, 3)), ((0, 3), (0, 0))]
TRI_B = SQ + [((0, 3), (3, 0))]
SQ_BOTH = SQ + [((0, 3), (3, 0)), ((0, 0), (3, 3))]


# ---- counting squares in a figure of drawn unit edges
def grid_edges(a, b):
    E = set()
    for x in range(a + 1):
        E |= {((x, y), (x, y + 1)) for y in range(b)}
    for y in range(b + 1):
        E |= {((x, y), (x + 1, y)) for x in range(a)}
    return E


def count_squares(edges, W, H):
    """Squares of every size whose four sides are all drawn (every unit edge of each side is in the figure)."""
    E = set(edges)
    h = lambda x, y, l: all(((x + i, y), (x + i + 1, y)) in E for i in range(l))
    v = lambda x, y, l: all(((x, y + i), (x, y + i + 1)) in E for i in range(l))
    n = 0
    for s in range(1, min(W, H) + 1):
        for x in range(W - s + 1):
            for y in range(H - s + 1):
                if h(x, y, s) and h(x, y + s, s) and v(x, y, s) and v(x + s, y, s):
                    n += 1
    return n


def nested_edges():
    """A 4 x 4 drawing: the outline, a cross through the middle (2 x 2 squares), and a small cross inside ONE of the four squares (the top-right one)."""
    E = grid_edges(4, 4)
    keep = set()
    for (a, b) in E:
        horizontal = a[1] == b[1]
        inside_main = (a[1] in (0, 4) if horizontal else a[0] in (0, 4)) or (a[1] == 2 if horizontal else a[0] == 2)
        inside_small = (a[0] >= 2 and a[1] >= 2 and b[0] <= 4 and b[1] <= 4)
        if inside_main or inside_small:
            keep.add((a, b))
    return keep


# ---- two same-size triangles joined along a whole side
def simplify(pts):
    out = []
    n = len(pts)
    for i in range(n):
        p, q, r = pts[i - 1], pts[i], pts[(i + 1) % n]
        if (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0]) != 0:
            out.append(q)
    return out


def quad_name(pts):
    pts = simplify(pts)
    n = len(pts)
    if n == 3:
        return 'triangle'
    sq = [(pts[i][0] - pts[(i + 1) % n][0]) ** 2 + (pts[i][1] - pts[(i + 1) % n][1]) ** 2 for i in range(n)]
    right = sum(1 for i in range(n) if (pts[i - 1][0] - pts[i][0]) * (pts[(i + 1) % n][0] - pts[i][0]) + (pts[i - 1][1] - pts[i][1]) * (pts[(i + 1) % n][1] - pts[i][1]) == 0)
    par = pts[1][0] - pts[0][0] == pts[2][0] - pts[3][0] and pts[1][1] - pts[0][1] == pts[2][1] - pts[3][1]
    if right == 4:
        return 'square' if len(set(sq)) == 1 else 'rectangle'
    if par:
        return 'parallelogram'
    if (sq[0] == sq[1] and sq[2] == sq[3]) or (sq[1] == sq[2] and sq[3] == sq[0]):
        return 'kite'
    return 'four-sided shape'


def join_triangles(tri):
    """All ways to put a copy of the triangle against it along a WHOLE side (the copy on the other side of that side): the joined polygon and its name."""
    tri = [_pt(p) for p in tri]
    out = []
    for i in range(3):
        a, b, c = tri[i], tri[(i + 1) % 3], tri[(i + 2) % 3]
        bx, by = b[0] - a[0], b[1] - a[1]
        t = ((c[0] - a[0]) * bx + (c[1] - a[1]) * by) / (bx * bx + by * by)
        foot = (a[0] + t * bx, a[1] + t * by)
        mirror = (2 * foot[0] - c[0], 2 * foot[1] - c[1])        # the copy turned over the side
        turned = (a[0] + b[0] - c[0], a[1] + b[1] - c[1])        # the copy turned half a turn about the middle of the side
        for d in {mirror, turned}:
            poly = [c, a, d, b]
            out.append((poly, (a, b, d), quad_name(poly)))
    return out


RIGHT_ISOS = [(0, 0), (2, 0), (0, 2)]          # a square cut along a diagonal
RIGHT_345 = [(0, 0), (4, 0), (0, 3)]


def names_from(tri):
    return sorted({nm for _, _, nm in join_triangles(tri)})


def pair_item(tri, name, fill2='#BFE3E0'):
    """A poly_row item for the first way that makes `name`: both triangles shaded, with a label."""
    for poly, second, nm in join_triangles(tri):
        if nm == name:
            return ([([(float(x), float(y)) for x, y in tri], '#FDF3D0'), ([(float(x), float(y)) for x, y in second], fill2)], {'triangle': 'bigger|triangle'}.get(nm, nm))
    raise ValueError(name)


# ---- shapes made of joined squares (turned or flipped copies are the same shape)
def free_polyominoes(n):
    def norm(cells):
        mx, my = min(c[0] for c in cells), min(c[1] for c in cells)
        return tuple(sorted((c[0] - mx, c[1] - my) for c in cells))

    def canon(cells):
        forms = []
        cur = list(cells)
        for _ in range(2):
            for _ in range(4):
                cur = [(-y, x) for x, y in cur]
                forms.append(norm(cur))
            cur = [(-x, y) for x, y in cur]
        return min(forms)
    shapes = {canon([(0, 0)])}
    for _ in range(n - 1):
        nxt = set()
        for sh in shapes:
            for (x, y) in sh:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    c = (x + dx, y + dy)
                    if c not in sh:
                        nxt.add(canon(list(sh) + [c]))
        shapes = nxt
    return sorted(shapes, key=lambda s: (-max(c[0] for c in s), s))


def quad_shapes_figure():
    """The two four-sided shapes of Think harder 4: a long rectangle and a slanted shape (no square corners)."""
    rect = [(0, 0), (6, 0), (6, 3), (0, 3)]
    slant = [(1, 0), (7, 0), (6, 3), (0, 3)]
    return rect, slant


# ======================================================================== the items
ITEMS = [
    # ================= Start here
    D(id='1', tier='core', no='1', label='1', type='fields', skill='naming shapes in a picture', answer=[1, 2, 3, 2],
      q='Count the shapes in the house picture. Fill in how many of each. A square counts as a square only, not as a rectangle.',
      frame='Circle: {f1}   Triangle: {f2}\nSquare: {f3}   Rectangle: {f4}', svg=house_fig(), check=house_row,
      hint='Look at the whole picture, from the sky to the ground. Count each kind of shape one at a time.',
      steps=['The sun is a circle: 1 circle.', 'The roof and the flag are triangles: 2 triangles.',
             'The 3 windows are squares: 3 squares. The house and the door are rectangles: 2 rectangles.'],
      src=['Count the shapes in the house picture.']),
    D(id='1a', tier='core', no='1(a)', label='1(a)', type='choice', skill='comparing counts of shapes', options=['Circle', 'Triangle', 'Square', 'Rectangle'], answer='Square',
      q='Look at the house picture. Which shape is there the most of? A square counts as a square only.', svg=house_fig(),
      check=lambda: (lambda c: c.most_common(1)[0][0].capitalize() if c.most_common(2)[0][1] > c.most_common(2)[1][1] else None)(house_counts()),
      hint='Count each kind of shape. Which kind has the biggest number?',
      steps=['Count each kind: circles 1, triangles 2, squares 3, rectangles 2.', '3 is the biggest number, so there are most squares.'],
      src=['Which shape is there the most of?']),
    D(id='1b', tier='core', no='1(b)', label='1(b)', type='number', skill='counting shapes', answer=8,
      q='How many shapes are there altogether in the house picture? A square counts as a square only.', svg=house_fig(), check=lambda: sum(house_counts().values()),
      hint='Count every shape once. Do not count a shape twice.',
      steps=['There is 1 circle, 2 triangles, 3 squares and 2 rectangles.', '1 + 2 + 3 + 2 = 8.', 'There are 8 shapes altogether.'],
      src=['How many shapes altogether?']),

    D(id='2', tier='core', no='2', label='2', type='fields', skill='sides and corners', answer=[4, 4, 5, 5, 6, 6, 8, 8],
      q='Sides and corners. A circle has 0 straight sides and 0 corners. A triangle has 3 sides and 3 corners. Fill in the table for the other shapes.',
      frame='Square: {f1} sides, {f2} corners\nPentagon: {f3} sides, {f4} corners\nHexagon: {f5} sides, {f6} corners\nOctagon: {f7} sides, {f8} corners', svg=shape_gallery(),
      check=lambda: [v for n in (4, 5, 6, 8) for v in sides_and_corners(regular(n))],
      hint='Take one shape at a time. Count its straight sides, then count its corners. Go round the edge so you do not count one twice.',
      steps=['Square: 4 straight sides and 4 corners.', 'Pentagon: 5 sides and 5 corners. Hexagon: 6 sides and 6 corners.', 'Octagon: 8 sides and 8 corners.'],
      src=['Sides and corners. Look at the shapes, then fill in the table.']),
    D(id='2a', tier='core', no='2(a)', label='2(a)', type='selfcheck', open=False, marking_mode='self', skill='sides and corners',
      q='Think about the circle, triangle, square, pentagon, hexagon and octagon. What do you notice about the number of sides and the number of corners?', svg=shape_gallery(),
      check=lambda: all(s == c for s, c in (sides_and_corners(regular(n)) for n in (3, 4, 5, 6, 8))),
      hint='Compare the two numbers for one shape. Then compare them for another shape.',
      steps=['A triangle has 3 sides and 3 corners. A square has 4 and 4. A pentagon has 5 and 5.', 'Every shape with straight sides has the same number of sides as corners.',
             'A circle has 0 sides and 0 corners, so it fits too. Any answer that says the two numbers are the same is good.'],
      src=['What do you notice about the number of sides and corners?']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='number', skill='sides and corners', answer=7,
      q='A shape has 7 straight sides. How many corners does it have?', check=lambda: sides_and_corners(regular(7))[1],
      hint='Think about the triangle, the square and the pentagon. How do their sides and corners go together?',
      steps=['A triangle has 3 sides and 3 corners, a square has 4 and 4, a pentagon has 5 and 5.', 'A closed shape with straight sides has as many corners as sides.', 'So a shape with 7 sides has 7 corners.'],
      src=['A shape has 7 sides. How many corners does it have?']),

    D(id='3a', tier='core', no='3(a)', label='3(a)', type='choice', skill='describing shapes', options=SHAPE_OPTS, answer='Square',
      q='Who am I? I have 4 sides, all the same length, and 4 square corners.',
      check=lambda: who_am_i(lambda p: p is not None and props(p) == (4, True, 4)),
      hint='Which shapes have 4 sides? Then check that all the sides are the same length.',
      steps=['A rectangle and a square both have 4 sides and 4 square corners.', 'In a square all 4 sides are the same length. In this rectangle they are not.', 'I am a square.'],
      src=['I have 4 sides, all the same length, and 4 square corners.']),
    D(id='3b', tier='core', no='3(b)', label='3(b)', type='choice', skill='describing shapes', options=SHAPE_OPTS, answer='Circle',
      q='Who am I? I have no corners and no straight sides.', check=lambda: who_am_i(lambda p: p is None),
      hint='Which shape on the list is round all the way?',
      steps=['A triangle, square, rectangle, pentagon and hexagon all have straight sides and corners.', 'Only the circle has no straight sides and no corners.', 'I am a circle.'],
      src=['I have no corners and no straight sides.']),
    D(id='3c', tier='core', no='3(c)', label='3(c)', type='choice', skill='describing shapes', options=SHAPE_OPTS, answer='Hexagon',
      q='Who am I? I have 6 sides.', check=lambda: who_am_i(lambda p: p is not None and len(p) == 6),
      hint='How many sides does each shape on the list have?',
      steps=['Triangle 3 sides, square and rectangle 4 sides, pentagon 5 sides.', 'The hexagon has 6 sides.', 'I am a hexagon.'],
      src=['I have 6 sides.']),

    D(id='4A', tier='core', no='4(A)', label='4 pic A', type='number', skill='counting triangles', answer=3,
      q='How many triangles can you find in picture A? Count the small ones first, then the bigger ones.', svg=seg_svg(TRI_A, 4, 3, 54, 'Picture A: a triangle with a line from the top corner to the middle of the bottom'),
      check=lambda: count_triangles(TRI_A),
      hint='Count the small triangles first. Then look for a bigger triangle made of more than one small triangle.',
      steps=['The middle line cuts the big triangle into 2 small triangles.', 'The two small triangles together make 1 bigger triangle: the whole shape.', '2 + 1 = 3 triangles.'],
      src=['How many triangles can you find in each picture? Count the small ones first, then the bigger ones.']),
    D(id='4B', tier='core', no='4(B)', label='4 pic B', type='number', skill='counting triangles', answer=2,
      q='How many triangles can you find in picture B? Count the small ones first, then the bigger ones.', svg=seg_svg(TRI_B, 3, 3, 62, 'Picture B: a square with a line from one corner to the opposite corner'),
      check=lambda: count_triangles(TRI_B),
      hint='Count the small triangles first. Is there a bigger triangle made of more than one small triangle?',
      steps=['The line from corner to corner cuts the square into 2 small triangles.', 'Together the two small triangles make a square, not a triangle.', 'There are 2 triangles.'],
      src=['How many triangles can you find in each picture? Count the small ones first, then the bigger ones.']),

    D(id='5', tier='core', no='5', label='5', type='selfcheck', paper=True, skill='putting shapes together',
      q='Two triangles of the same size are put together along one side. Draw one shape you can make. What is it called?',
      facts=['kite', 'parallelogram', 'rectangle', 'triangle'], check=lambda: names_from(RIGHT_345),
      sol_fig=lambda f: poly_row([pair_item(RIGHT_345, 'rectangle'), pair_item(RIGHT_345, 'parallelogram')], caption='Two triangles with a square corner, put together'),
      hint='Cut two triangles of the same size from paper if you can. Try putting different sides together.',
      steps=['Here is one example. Take two triangles of the same size with a square corner.', 'Put them together along the longest side: they can make a rectangle. Put them together along a short side instead (turn one round) and they can make a parallelogram.',
             'Any correct shape with its right name is good.'],
      src=['Two triangles of the same size are put together along one side. Draw one shape you can make. What is it called?']),
    D(id='6', tier='core', no='6', label='6', type='number', skill='counting squares', answer=5,
      q='How many squares can you find in this picture? Count the small ones first, then the bigger one.', svg=grid_fig(2, 2, 58, 'A big square cut into 4 equal small squares'),
      check=lambda: count_squares(grid_edges(2, 2), 2, 2),
      hint='Count the small squares first. Then look for a bigger square made of more than one small square.',
      steps=['There are 4 small squares.', 'The whole picture is also a square: 1 more.', '4 + 1 = 5 squares.'],
      src=['How many squares can you find in this picture? Count the small ones first, then the bigger one.']),

    # ================= Investigation
    D(id='I1', tier='invest', no='Investigation 1', type='selfcheck', paper=True, skill='joining squares', label='Inv 1',
      q='Join 3 squares so that whole sides touch. Draw one shape you can make.',
      facts=2, check=lambda: len(free_polyominoes(3)),
      sol_fig=lambda f: polyomino_row([sorted(free_polyominoes(3), key=lambda s: -max(c[0] for c in s))[0]], caption='One shape made of 3 squares with whole sides touching'),
      hint='Use paper squares or counters. Slide one square so a whole side touches a whole side.',
      steps=['Put one square down. Put a second square so a whole side touches.', 'Put the third square so a whole side touches too. Corners that only touch at a point do not count.', 'Any shape of 3 squares with whole sides touching is good.'],
      src=['Join 3 squares so that whole sides touch. Draw one shape you can make.']),
    D(id='I2', tier='invest', no='Investigation 2', type='number', skill='joining squares', label='Inv 2', answer=2,
      q='How many different shapes can you make with 3 squares? Turning or flipping a shape does not make a new one.', check=lambda: len(free_polyominoes(3)),
      hint='Use paper squares or counters. Make one shape, then try to make a different one. Turn each shape to test if it is new.',
      steps=['Start with a straight line of 3 squares.', 'Move one end square so the shape bends: this is a bent shape, like an L.', 'Turning or flipping these does not make new shapes. There are 2 shapes.'],
      src=['How many different shapes can you make with 3 squares? Turning or flipping a shape does not make a new one.']),
    D(id='I3', tier='invest', no='Investigation 3', type='number', skill='joining squares', label='Inv 3', answer=5,
      q='Now try with 4 squares. How many different shapes can you make? Turning or flipping a shape does not make a new one.', check=lambda: len(free_polyominoes(4)),
      hint='Use paper squares or counters. Start with a straight line, then move one square at a time. Keep a list of the new shapes.',
      steps=['Start with a line of 4 squares.', 'Move one square at a time: you can make an L, a T, an S (or Z) and a big square.', 'A turned or flipped shape is not new. There are 5 shapes.'],
      src=['Then try with 4 squares.']),
    D(id='I4', tier='invest', no='Investigation 4', type='selfcheck', paper=True, skill='joining squares', label='Inv 4',
      q='Draw each different shape you can make with 3 squares.', facts=2, check=lambda: len(free_polyominoes(3)),
      sol_fig=lambda f: polyomino_row(free_polyominoes(3), caption='Both shapes of 3 squares'),
      hint='Draw a shape, then turn your paper. Do not draw the same shape twice.',
      steps=['A straight line of 3 squares.', 'A bent shape of 3 squares, like an L.', 'Turned or flipped copies are the same shape.'],
      src=['Draw each shape.']),
    D(id='I5', tier='invest', no='Investigation 5', type='selfcheck', paper=True, skill='joining squares', label='Inv 5',
      q='Draw each different shape you can make with 4 squares.', facts=5, check=lambda: len(free_polyominoes(4)),
      sol_fig=lambda f: polyomino_row(free_polyominoes(4), caption='All 5 shapes of 4 squares'),
      hint='Draw a shape, then turn your paper. Keep checking that every shape is new.',
      steps=['A line of 4 squares, an L, a T, an S (or Z) and a big square.', 'A shape that is only turned or flipped is the same shape.', 'Whole sides must touch.'],
      src=['Draw each shape.', 'Then try with 4 squares.']),
    D(id='I6', tier='invest', no='Investigation 6', type='selfcheck', open=False, marking_mode='self', skill='explaining a search', label='Inv 6',
      q='How do you know you have found all the shapes of 3 squares and of 4 squares?', facts=[2, 5], check=lambda: [len(free_polyominoes(3)), len(free_polyominoes(4))],
      hint='Did you start with a line and then move one square at a time? Did you check each new shape against the others?',
      steps=['Start with a line. Then move one square at a time, and each time ask: is this a new shape, or only a turned or flipped one?',
             'When every move gives a shape you already have, there are no more.', 'Any answer that explains a way to check is good.'],
      src=['Use paper squares or counters to help.']),

    # ================= Think harder
    D(id='T1', tier='stretch', no='T1', label='T1', type='choice', skill='putting shapes together', options=['Yes', 'No'], answer='Yes',
      q='Two same-size triangles like this can make a square. Can they also make a bigger triangle?',
      svg=poly_row([([([(float(x), float(y)) for x, y in RIGHT_ISOS], '#FDF3D0')], 'one triangle')], caption='One triangle with a square corner'),
      check=lambda: 'Yes' if 'triangle' in names_from(RIGHT_ISOS) else 'No',
      hint='Cut out two triangles like this. Try putting different sides together. Which sides line up in a straight line?',
      steps=['Put two of the triangles together along a short side, so the other two short sides make one straight line.', 'The two triangles then make one bigger triangle.',
             'Yes. Putting them together along the long side makes a square instead.'],
      src=['Two same-size triangles can make a square. Can they also make a bigger triangle? Draw how.']),
    D(id='T1b', tier='stretch', no='T1 draw', label='T1 draw', type='selfcheck', paper=True, skill='putting shapes together',
      q='Try it with two paper triangles like the one in the picture. Draw the different shapes you can make by joining two of them along a whole side.', svg=poly_row([([([(float(x), float(y)) for x, y in RIGHT_ISOS], '#FDF3D0')], 'one triangle')], caption='One triangle with a square corner'),
      facts=['parallelogram', 'square', 'triangle'], check=lambda: names_from(RIGHT_ISOS),
      sol_fig=lambda f: poly_row([pair_item(RIGHT_ISOS, 'square'), pair_item(RIGHT_ISOS, 'triangle'), pair_item(RIGHT_ISOS, 'parallelogram')], per_row=3, box=80, caption='Two triangles put together in three ways'),
      hint='Put two triangles side by side. Join a short side to a short side, then the long side to the long side.',
      steps=['Along the long side the two triangles make a square.', 'Along a short side they can make a bigger triangle (the other short sides line up in a straight line) or a parallelogram (turn one triangle round so it points the other way).', 'Draw any of these.'],
      src=['Draw how.']),
    D(id='T2', tier='stretch', no='T2', label='T2', type='number', skill='counting squares', answer=8,
      q='How many squares are in a grid 3 squares long and 2 squares high? Count the small squares and the bigger squares.', svg=grid_fig(3, 2, 50, 'A grid 3 squares long and 2 squares high'), check=lambda: count_squares(grid_edges(3, 2), 3, 2),
      hint='Count the small squares first. Then look for bigger squares made of 4 small squares.',
      steps=['There are 6 small squares.', 'Squares made of 4 small squares (2 long and 2 high): there are 2 of them.', '6 + 2 = 8 squares.'],
      src=['How many squares are in a grid 3 squares long and 2 squares high?']),
    D(id='T3', tier='stretch', no='T3', label='T3', type='number', skill='counting triangles', answer=8,
      q='A square has both diagonals drawn (lines joining opposite corners). How many triangles can you find? Count the small ones first.',
      svg=seg_svg(SQ_BOTH, 3, 3, 62, 'A square with both diagonals drawn'), check=lambda: count_triangles(SQ_BOTH),
      hint='Count the small triangles at the middle first. Then look for bigger triangles made of two small ones.',
      steps=['The two lines cut the square into 4 small triangles.', 'Two small triangles side by side make a bigger triangle. There are 4 of these (top, bottom, left and right).', '4 + 4 = 8 triangles.'],
      src=['A square has both diagonals drawn (lines joining opposite corners). How many triangles can you find? Count the small ones first.']),
    D(id='T4', tier='stretch', no='T4', label='T4', type='selfcheck', paper=True, skill='rectangles and four-sided shapes',
      q='Draw a shape with 4 straight sides that is NOT a square. Is it a rectangle? How do you know?',
      facts=['rectangle', 'four-sided shape'], check=lambda: [shape_name(p) for p in quad_shapes_figure()],
      sol_fig=lambda f: poly_row([([(quad_shapes_figure()[0], '#BFE3E0')], 'rectangle|4 square corners'), ([(quad_shapes_figure()[1], '#F6B8A4')], 'not a rectangle|no square corners')], per_row=2, box=110,
                                 caption='Two shapes with 4 straight sides that are not squares'),
      hint='Look at the corners of your shape. Are they all square corners?',
      steps=['A long shape with 4 square corners is a rectangle. A square is not what we want, so make the sides different lengths.', 'A slanted shape with 4 sides has no square corners, so it is not a rectangle.',
             'Your shape is a rectangle only if all 4 corners are square corners.'],
      src=['Draw a shape with 4 straight sides that is NOT a square. Is it a rectangle? How do you know?']),

    # ================= Go further
    D(id='C1', tier='challenge', no='Go further 1', label='G1', type='fields', skill='counting triangles in growing figures', answer=[15, 21],
      q='A big triangle has lines drawn from its top corner to the bottom. With 1 line there are 3 triangles, with 2 lines 6, with 3 lines 10. How many triangles with 4 lines? With 5 lines?',
      frame='With 4 lines: {f1} triangles.   With 5 lines: {f2} triangles.', svg=tri_lines_fig([(1, 3), (2, 6), (3, 10)]),
      check=lambda: [count_triangles(lines_figure(4)), count_triangles(lines_figure(5))],
      hint='Look at how many more triangles each new line adds: from 3 to 6, then from 6 to 10. Draw a big triangle with 4 lines to check.',
      steps=['The numbers grow by 3, then by 4: 3, 6, 10. The next steps add 5, then 6, then 7.', '10 + 5 = 15 triangles with 4 lines. 15 + 6 = 21 triangles with 5 lines.',
             'Check by drawing: count the small triangles first, then the bigger ones made of 2, 3 ... small ones.'],
      src=['A big triangle has lines drawn from its top corner to the bottom. With 1 line there are 3 triangles, with 2 lines 6, with 3 lines 10. How many triangles with 4 lines? With 5 lines? Draw it to check.']),
    D(id='C2', tier='challenge', no='Go further 2', label='G2', type='number', skill='counting squares', answer=9,
      q='Draw a square and cut it into 4 equal squares. Then cut ONE of those small squares into 4 even smaller squares. How many squares can you find altogether? Count the small ones first, then the bigger ones.',
      svg=edges_fig(nested_edges(), 4, 4, 34, fills=[(2, 2, 2, 2, '#BCDDF4')], caption='A square cut into 4 equal squares, with one of them cut into 4 smaller squares'),
      check=lambda: count_squares(nested_edges(), 4, 4),
      hint='Count the tiny squares first. Then the medium squares. Then the biggest square. Do not forget the whole picture.',
      steps=['There are 4 tiny squares in the one square that was cut again.', 'There are 4 medium squares: the 3 that were not cut and the 1 that was cut into tiny squares.', 'The whole picture is 1 big square. 4 + 4 + 1 = 9 squares.'],
      src=['Draw a square and cut it into 4 equal squares. Then cut ONE of those small squares into 4 even smaller squares. How many squares can you find altogether? Count the small ones first, then the bigger ones.']),
    D(id='C3', tier='challenge', no='Go further 3', label='G3', type='selfcheck', paper=True, marking_mode='open', skill='making a counting puzzle',
      q='Draw your own triangle-counting puzzle: a big triangle with some lines inside. Count the triangles. Ask a friend or a grown-up to count them too. Do you both get the same number? If not, find out who missed some.',
      facts=[3, 6], check=lambda: [count_triangles(lines_figure(1)), count_triangles(lines_figure(2))],
      sol_fig=lambda f: tri_lines_plain(2, 'An example puzzle: a big triangle with 2 lines from the top corner'),
      hint='Draw a big triangle. Put some lines inside it from a corner to the bottom. Count the small triangles first, then the bigger ones.',
      steps=['Here is one example: a big triangle with 2 lines from the top corner to the bottom has 6 triangles.', 'Count the small ones first, then the bigger ones made of 2, 3 ... small ones.',
             'Your own puzzle gives its own number. If you and your friend get different numbers, count again together.'],
      src=['Draw your own triangle-counting puzzle: a big triangle with some lines inside. Count the triangles. Swap with a partner. Do you both get the same number? If not, find out who missed some.']),
]


# ---- variant families (every combination is run against the oracle by the build)
VARIANTS = {
    '2b': dict(base=dict(n=7),
               tpl=dict(vars=dict(n=[5, 6, 8, 9, 10, 11, 12]), q='A shape has {n} straight sides. How many corners does it have?', answer='n',
                        hint='Think about the triangle, the square and the pentagon. How do their sides and corners go together?',
                        steps=['A closed shape with straight sides has as many corners as sides.', 'A shape with {n} sides has {n} corners.']),
               oracle=lambda e: sides_and_corners(regular(e['n']))[1]),
    'T2': dict(base=dict(a=3, b=2),
               tpl=dict(vars=dict(a=[3, 4, 5, 6], b=[2, 3]), q='How many squares are in a grid {a} squares long and {b} squares high? Count the small squares and the bigger squares.', answer='b*(b+1)*(3*a-b+1)//6',
                        hint='Count the small squares first. Then look for bigger squares made of more small squares.',
                        steps=['Count the small squares: {a} in each row, and {b} rows.', 'Then count the squares made of 4 small squares, and (if there are 3 rows) the squares made of 9.', 'There are {ans} squares altogether.']),
               fig=lambda e: grid_fig(e['a'], e['b'], 40 if e['a'] <= 5 else 34, f'A grid {e["a"]} squares long and {e["b"]} squares high'),
               oracle=lambda e: count_squares(grid_edges(e['a'], e['b']), e['a'], e['b'])),
    'C1': dict(base=dict(a=4, b=5),
               tpl=dict(vars=dict(a=[4, 5], b=[6, 7]), q='A big triangle has lines drawn from its top corner to the bottom. With 1 line there are 3 triangles, with 2 lines 6, with 3 lines 10. How many triangles with {a} lines? With {b} lines?',
                        frame='With {a} lines: {f1} triangles.   With {b} lines: {f2} triangles.', answers=dict(f1='(a+1)*(a+2)//2', f2='(b+1)*(b+2)//2'), paper=True,
                        hint='Look at how many more triangles each new line adds: from 3 to 6, then from 6 to 10. Keep going.',
                        steps=['The numbers grow by 3, then by 4, then by 5 and so on.', 'Keep adding one more each time until you reach {a} lines and then {b} lines.', 'The answers are {ans}.']),
               oracle=lambda e: dict(f1=count_triangles(lines_figure(e['a'])), f2=count_triangles(lines_figure(e['b'])))),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and not _d.get('open') and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
habit_tag(ITEMS, 'Notice', ['2a'])
