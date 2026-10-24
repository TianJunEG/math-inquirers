"""Independent checks for Level 5 Unit 5 (Volume vault): volumes by counting cubes or exact arithmetic, painted cubes by simulation."""
import itertools
from fractions import Fraction as Fr

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def fmt(x):
    x = Fr(x)
    if x.denominator == 1:
        return str(x.numerator)
    return f'{float(x):g}'


def count_cubes(l, w, h):
    return sum(1 for _ in itertools.product(range(l), range(w), range(h)))


def painted_faces(n):
    """{number of painted faces: count} for an n x n x n cube painted on the outside."""
    out = {}
    for x, y, z in itertools.product(range(n), repeat=3):
        k = sum(1 for c in (x, y, z) if c in (0, n - 1)) if n > 1 else 3
        # a coordinate on a boundary gives 1 painted face (n = 1 does not occur here)
        out[k] = out.get(k, 0) + 1
    return out


@check('L5U05-L01')
def _():
    base = 25 * 20
    return [fmt(10 + Fr(1500, base))]


@check('L5U05-S01')
def _():
    # 5 long, 2 wide, 3 high: the front bottom row, the bottom layer, all the cubes
    front_row = sum(1 for x, y, z in itertools.product(range(5), range(2), range(3)) if y == 0 and z == 0)
    layer = sum(1 for x, y, z in itertools.product(range(5), range(2), range(3)) if z == 0)
    return {'a': [str(front_row)], 'b': [str(layer)], 'c': [str(count_cubes(5, 2, 3)), str(count_cubes(5, 2, 3))]}


@check('L5U05-S02')
def _():
    return {'a': [str(count_cubes(9, 6, 5))], 'b': [str(count_cubes(7, 7, 7))]}


@check('L5U05-S03')
def _():
    h = next(h for h in range(1, 100) if count_cubes(8, 5, h) == 200)
    side = next(s for s in range(1, 100) if s * s * 4 == 144)
    return {'a': [str(h)], 'b': [str(side)]}


@check('L5U05-S04')
def _():
    return {'a': [fmt(Fr(35, 10) * 1000)], 'b': [fmt(Fr(12000, 1000))], 'c': [fmt(Fr(count_cubes(50, 40, 30), 1000))]}


@check('L5U05-S05')
def _():
    water = 40 * 30 * 12
    full = 40 * 30 * 25
    return {'a': [str(water)], 'b': [fmt(Fr(water, 1000))], 'c': [fmt(Fr(full - water, 1000))]}


@check('L5U05-S06')
def _():
    rise = Fr(5 * 1000, 40 * 25)
    return {'a': [fmt(rise)], 'b': [fmt(7 + rise)]}


@check('L5U05-S07')
def _():
    return [str(24 * 15 * (11 - 8))]


@check('L5U05-S08')
def _():
    fall = Fr(9 * 1000, 60 * 30)
    return {'a': [fmt(fall)], 'b': [fmt(20 - fall)]}


@check('L5U05-S09')
def _():
    sets = {tuple(sorted(t)) for t in itertools.product(range(1, 31), repeat=3) if t[0] * t[1] * t[2] == 30}
    return {'a': [str(len(sets))], 'b': [str(min(sum(t) for t in sets))]}


@check('L5U05-S10')
def _():
    d = painted_faces(3)
    return {'a': [str(d[3])], 'b': [str(d[2])], 'c': [str(d[1])], 'd': [str(d.get(0, 0))]}


@check('L5U05-S11')
def _():
    return [str((32 // 6) * (20 // 6) * (14 // 6))]


@check('L5U05-S12')
def _():
    return [fmt(Fr(45 * 40 * 30, 60 * 30))]


@check('L5U05-S13')
def _():
    b_water = Fr(3, 4) * 40
    for cap in range(1, 1000):
        if Fr(3, 5) * cap == b_water:
            return [str(cap)]


@check('L5U05-S14')
def _():
    t = lambda v: 'True' if v else 'False'
    return {'a': [t(1000 == 10 * 10 * 10)], 'b': [t(count_cubes(2, 3, 4) == count_cubes(3, 3, 3))], 'c': [t(count_cubes(4, 6, 8) == 2 * count_cubes(2, 3, 4))]}


@check('L5U05-T01')
def _():
    for n in range(3, 40):
        if painted_faces(n).get(0, 0) == 64:
            return [str(n ** 3)]


@check('L5U05-T02')
def _():
    vol = 50 * 20 * 24
    return [fmt(Fr(vol, 50 * 20 + 25 * 20))]


@check('L5U05-T03')
def _():
    water = 20 * 40 * 18
    depth = Fr(water, 60 * 40)
    assert depth < 18                      # the depth falls: the water spreads over the whole floor
    return [fmt(depth)]


@check('L5U05-G01')
def _():
    n = 6
    mid = (2, 3)       # the 2 middle cells of each axis (indexes 2 and 3)
    removed = set()
    for a, b, c in itertools.product(range(n), repeat=3):
        in_tunnel_x = b in mid and c in mid      # tunnel along x
        in_tunnel_y = a in mid and c in mid
        in_tunnel_z = a in mid and b in mid
        if in_tunnel_x or in_tunnel_y or in_tunnel_z:
            removed.add((a, b, c))
    return [str(n ** 3 - len(removed))]


@check('L5U05-G02')
def _():
    cap = Fr(60 * 50 * 40, 1000)
    minutes, water = 0, Fr(0)
    while water < cap:
        water += 9 - 1
        minutes += 1
    return [str(minutes)]


@check('L5U05-G03')
def _():
    vol_b = 8 * 5 ** 3
    sols = [e for e in range(1, 200) if e ** 3 == vol_b]
    assert len(sols) == 1
    return [str(sols[0])]


@check('L5U05-C01')
def _():
    return [str(count_cubes(12, 5, 4))]


@check('L5U05-C02')
def _():
    return [fmt(Fr(18 * 1000, 50 * 30))]


@check('L5U05-C03')
def _():
    return [str(painted_faces(5)[2])]


@check('L5U05-C04')
def _():
    return [str(20 * 15 * (14 - 10))]
