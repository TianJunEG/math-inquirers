"""Independent checks for Level 4 Unit 8 (symmetry and nets).  Nets are folded by rolling a cube over them with 3 x 3 rotation matrices (a net works when
the 6 cells touch 6 different faces); dice questions use the same matrices; symmetry counts are found by testing every mirror image / every subset."""
import itertools
from common import load_unit
CHECKS = {}
U = load_unit(4, 8)
ITEM = {i['id']: i for i in [U['learn']['try']] + U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mv(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))


I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ROLL = {'E': ((0, 0, 1), (0, 1, 0), (-1, 0, 0)), 'N': ((1, 0, 0), (0, 0, 1), (0, -1, 0))}
ROLL['W'] = tuple(zip(*ROLL['E']))
ROLL['S'] = tuple(zip(*ROLL['N']))
STEP = {'E': (1, 0), 'W': (-1, 0), 'N': (0, -1), 'S': (0, 1)}      # grid rows grow downwards = towards the south


def transpose(a):
    return tuple(zip(*a))


def down_face(M):
    """The object axis that touches the table: the vector v with M v = (0, 0, -1)."""
    return mv(transpose(M), (0, 0, -1))


def fold(cells):
    cells = [tuple(c) for c in cells]
    seen = {cells[0]: I3}
    todo = [cells[0]]
    while todo:
        c = todo.pop()
        for d, (dx, dy) in STEP.items():
            nb = (c[0] + dx, c[1] + dy)
            if nb in cells and nb not in seen:
                seen[nb] = mm(ROLL[d], seen[c])
                todo.append(nb)
    if len(seen) != 6:
        return None
    faces = {c: down_face(M) for c, M in seen.items()}
    return faces if len(set(faces.values())) == 6 else None


def opposite_cells(faces):
    return {c: next(o for o, f in faces.items() if f == tuple(-x for x in faces[c])) for c in faces}


def lbl(item_id, k=0):
    return {tuple(map(int, key.split(','))): v for key, v in ITEM[item_id]['figure']['shapes'][k]['labels'].items()}


@check('L4U08-L01')
def _():
    return s([7 - 4])


@check('L4U08-S01')
def _():
    sh = ITEM['L4U08-S01']['figure']['shapes']
    return [sh_['name'] for sh_ in sh if fold(sh_['cells'])]


@check('L4U08-S02')
def _():
    sh = ITEM['L4U08-S02']['figure']['shapes'][0]
    faces = fold(sh['cells'])
    assert faces
    opp = opposite_cells(faces)
    L = lbl('L4U08-S02')
    inv = {v: k for k, v in L.items()}
    return {'a': [L[opp[inv['P']]]], 'b': [L[opp[inv['Q']]]], 'c': [L[opp[inv['S']]]]}


@check('L4U08-S03')
def _():
    sh = ITEM['L4U08-S03']['figure']['shapes'][0]
    faces = fold(sh['cells'])
    assert faces
    opp = opposite_cells(faces)
    L = {k: v for k, v in lbl('L4U08-S03').items()}
    known = {k: int(v) for k, v in L.items() if v != ''}
    assert all(known[a] + known.get(opp[a], 0) != 7 or opp[a] not in known for a in known)
    blanks = sorted([k for k, v in L.items() if v == ''], key=lambda c: (c[1], c[0]))
    out = []
    for b in blanks:
        partner = opp[b]
        assert partner in known, 'blank has no known opposite'
        out.append(7 - known[partner])
    assert sorted(list(known.values()) + out) == [1, 2, 3, 4, 5, 6]
    return s(out)


def mirror_count(shaded, axis_kind, at):
    """shaded is a list of [row, col]; the dashed line lies between cells (at is the number of cells before the line)."""
    S = {tuple(x) for x in shaded}
    if axis_kind == 'v':
        assert all(c < at for r, c in S), 'a shaded square is not on the same side of the line'
        M = {(r, int(2 * at - 1 - c)) for r, c in S}
    else:
        assert all(r < at for r, c in S), 'a shaded square is not on the same side of the line'
        M = {(int(2 * at - 1 - r), c) for r, c in S}
    assert not (S & M)
    return len(S | M)


@check('L4U08-S04')
def _():
    f = ITEM['L4U08-S04']['figure']
    return s([mirror_count(f['shade'], f['axis']['kind'], f['axis']['at'])])


def lines_of_symmetry(cells):
    S = {tuple(c) for c in cells}
    xs = [c[0] for c in S]
    ys = [c[1] for c in S]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w, h = x1 - x0, y1 - y0
    maps = [lambda c: (x0 + x1 - c[0], c[1]), lambda c: (c[0], y0 + y1 - c[1])]
    if w == h:
        maps += [lambda c: (x0 + (c[1] - y0), y0 + (c[0] - x0)), lambda c: (x0 + (y1 - c[1]), y0 + (x1 - c[0]))]
    return sum(1 for m in maps if {m(c) for c in S} == S)


@check('L4U08-S05')
def _():
    sh = ITEM['L4U08-S05']['figure']['shapes']
    return dict(zip('abcd', [[str(lines_of_symmetry(x['cells']))] for x in sh]))


@check('L4U08-S06')
def _():
    f = ITEM['L4U08-S06']['figure']
    R, C = f['rows'], f['cols']
    S = {tuple(x) for x in f['shade']}
    ways = []
    for r in range(R):
        for c in range(C):
            if (r, c) in S:
                continue
            T = S | {(r, c)}
            vert = all((rr, C - 1 - cc) in T for rr, cc in T)
            horiz = all((R - 1 - rr, cc) in T for rr, cc in T)
            if vert or horiz:
                ways.append((r, c))
    return {'a': s([len(ways)])}


@check('L4U08-S07')
def _():
    top, front = 6, 4
    bottom, back = 7 - top, 7 - front
    allf = {1, 2, 3, 4, 5, 6}
    sides = allf - {top, bottom}
    return {'a': s([bottom]), 'b': s([back]), 'c': s([sum(sides)])}


@check('L4U08-S08')
def _():
    return s([6 * 3 * 3])



@check('L4U08-S09')
def _():
    f = ITEM['L4U08-S09']['figure']
    return s([mirror_count(f['shade'], f['axis']['kind'], f['axis']['at'])])


@check('L4U08-S10')
def _():
    e = 5
    return {'a': s([12 * e]), 'b': s([6 * e * e])}


@check('L4U08-T01')
def _():
    opp = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}          # six faces; face f is opposite opp[f], every other pair shares an edge
    best_a = best_b = 0
    for mask in range(64):
        red = [f for f in range(6) if mask >> f & 1]
        no_edge = all(opp[a] == b for a in red for b in red if a != b)
        no_opp = all(opp[a] != b for a in red for b in red if a != b)
        if no_edge:
            best_a = max(best_a, len(red))
        if no_opp:
            best_b = max(best_b, len(red))
    return {'a': s([best_a]), 'b': s([best_b])}



@check('L4U08-T02')
def _():
    faces = range(1, 7)
    two = {(7 - a) + (7 - b) for a in faces for b in faces if a + b == 9}
    three = {(7 - a) + (7 - b) + (7 - c) for a in faces for b in faces for c in faces if a + b + c == 12}
    sides = {sum(f for f in faces if f not in (t, 7 - t)) for t in faces}
    assert len(two) == len(three) == len(sides) == 1
    return {'a': s(two), 'b': s(three), 'c': s(sides)}


@check('L4U08-T03')
def _():
    assert ITEM['L4U08-T03']['figure']['axis']['kind'] == 'd'
    cells = [(r, c) for r in range(3) for c in range(3)]
    n = 0
    for sub in itertools.combinations(cells, 4):
        S = set(sub)
        if all((c, r) in S for r, c in S):
            n += 1
    return s([n])


@check('L4U08-G01')
def _():
    cubes = list(itertools.product(range(3), repeat=3))
    painted = lambda c: sum(1 for x in c if x in (0, 2))
    return {k: s([sum(1 for c in cubes if painted(c) == n)]) for k, n in zip('abcd', (3, 2, 1, 0))}


@check('L4U08-G02')
def _():
    cells = [(r, c) for r in range(5) for c in range(5)]
    maps = [lambda r, c: (r, 4 - c), lambda r, c: (4 - r, c), lambda r, c: (c, r), lambda r, c: (4 - c, 4 - r)]
    lines = [sum(1 for m in maps if m(r, c) == (r, c)) for r, c in cells]
    return {'a': s([sum(1 for n in lines if n >= 1)]), 'b': s([sum(1 for n in lines if n == 1)])}



@check('L4U08-G03')
def _():
    # object axes: top = +z (1), bottom = -z (6), north = +y (2), south = -y (5), east = +x (3), west = -x (4)
    name = {(0, 0, 1): 1, (0, 0, -1): 6, (0, 1, 0): 2, (0, -1, 0): 5, (1, 0, 0): 3, (-1, 0, 0): 4}
    M = I3
    for d in 'NEN':
        M = mm(ROLL[d], M)
    top = mv(transpose(M), (0, 0, 1))
    bottom = down_face(M)
    return {'a': s([name[top]]), 'b': s([name[bottom]])}


@check('L4U08-C01')
def _():
    sh = ITEM['L4U08-C01']['figure']['shapes'][0]
    return ['Yes' if fold(sh['cells']) else 'No']


@check('L4U08-C02')
def _():
    cells = [(c, r) for c in range(3) for r in range(2)]      # a 3 by 2 rectangle of squares
    S = set(cells)
    n = sum(1 for m in (lambda c: (2 - c[0], c[1]), lambda c: (c[0], 1 - c[1])) if {m(c) for c in S} == S)
    return s([n])


@check('L4U08-C03')
def _():
    return s([7 - 2, 7 - 3])


@check('L4U08-C04')
def _():
    return s([6 * 4 * 4])
