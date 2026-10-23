"""Independent checks for Level 2 Unit 2 (adding and subtracting to 1000): missing digits are found by trying every digit."""
import itertools
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U02-' + i] = f
        return f
    return d


def fill(tpl, ds):
    it = iter(ds)
    return int(''.join(next(it) if c == '?' else c for c in tpl) if False else ''.join(str(next(it)) if c == '?' else c for c in tpl))


def solve_add(a, b, total):
    """a, b: strings with '?' ; returns list of digit tuples (in reading order) with a + b = total."""
    q = a.count('?') + b.count('?')
    out = []
    for ds in itertools.product(range(10), repeat=q):
        A = fill(a, ds[:a.count('?')]); B = fill(b, ds[a.count('?'):])
        if A + B == total:
            out.append(ds)
    return out


def solve_sub(a, b, diff):
    q = a.count('?') + b.count('?')
    out = []
    for ds in itertools.product(range(10), repeat=q):
        A = fill(a, ds[:a.count('?')]); B = fill(b, ds[a.count('?'):])
        if A - B == diff:
            out.append(ds)
    return out


def one(sol):
    assert len(sol) == 1, sol
    return s(sol[0])


@check('L01')
def _():
    return one(solve_add('5?4', '337', 891))


@check('S01')
def _():
    return {'a': one(solve_add('2?4', '35?', 603)), 'b': one(solve_add('4?8', '?26', 874)), 'c': one(solve_add('?65', '2?8', 703))}


@check('S02')
def _():
    return {'a': one(solve_sub('8?5', '26?', 568)), 'b': one(solve_sub('5?2', '?47', 265))}


@check('S03')
def _():
    f = lambda t: [x for x in range(0, 1001) if t(x)][0]
    return {'a': s([f(lambda x: 270 + 140 == 300 + x)]), 'b': s([f(lambda x: 840 - 300 == x - 200)]), 'c': s([f(lambda x: 360 + x == 400 + 150)]),
            'd': ['True' if 199 + 250 == 200 + 249 else 'False']}


@check('S04')
def _():
    g = [[100, None, 300], [None, 250, None], [200, None, 400]]
    sols = []
    for ds in itertools.product(range(0, 801, 50), repeat=4):
        t, l, r, b = ds
        M = [[100, t, 300], [l, 250, r], [200, b, 400]]
        lines = [sum(row) for row in M] + [sum(M[i][j] for i in range(3)) for j in range(3)] + [M[0][0] + M[1][1] + M[2][2], M[0][2] + M[1][1] + M[2][0]]
        if len(set(lines)) == 1:
            sols.append((M, lines[0]))
    assert len(sols) == 1
    M, tot = sols[0]
    return {'a': s([tot]), 'b': s([M[0][1], M[1][0], M[1][2], M[2][1]])}


@check('S05')
def _():
    sol = [(b, b + 80) for b in range(0, 461) if b + b + 80 == 460]
    b, a = sol[0]
    return {'a': s([460 - 80]), 'b': s([b]), 'c': s([a])}


@check('S08')
def _():
    return s([x for x in range(0, 501) if x + 135 + 210 == 500])


@check('S06')
def _():
    return {'a': s([346 + 278]), 'b': ['Yes' if 614 - 278 == 346 else 'No'], 'c': s([614 - 278])}


@check('S07')
def _():
    taken = [x for x in range(0, 345) if 345 - x == 128][0]     # the story: 345 start, some taken away, 128 left
    opts = {'(1)': 345 + taken == 128, '(2)': 345 - taken == 128, '(3)': taken - 345 == 128, '(4)': 128 - taken == 345}
    good = [k for k, v in opts.items() if v]
    assert len(good) == 1
    return {'a': good, 'b': s([taken])}


@check('S09')
def _():
    return {'a': s([368 + 457]), 'b': s([702 - 385]), 'c': s([249 + 394]), 'd': s([910 - 466])}


@check('S10')
def _():
    f = lambda t: s([x for x in range(0, 1001) if t(x)])
    return {'a': f(lambda x: 340 + x == 1000), 'b': f(lambda x: 485 + x == 1000), 'c': s([1000 - 755]), 'd': f(lambda x: x + 75 == 1000)}


@check('S11')
def _():
    left = 500 - 287
    return {'a': s([left]), 'b': s([left - 120])}


@check('T01')
def _():
    nums = [120, 135, 150, 165, 180, 195]

    def corners(side):
        found = set()
        for p in itertools.permutations(nums):
            c0, c1, c2, m01, m12, m20 = p
            if c0 + m01 + c1 == side and c1 + m12 + c2 == side and c2 + m20 + c0 == side:
                found.add(tuple(sorted((c0, c1, c2))))
        return found
    a, b = corners(450), corners(495)
    assert len(a) == 1 and len(b) == 1
    return {'a': s(list(a)[0]), 'b': s(list(b)[0])}


@check('T02')
def _():
    T = lambda b: 'True' if b else 'False'
    return {'a': [T(468 + 199 == 467 + 200)], 'b': [T(350 + 240 == 340 + 260)], 'c': [T(502 + 99 == 500 + 101)], 'd': [T(275 + 275 == 250 + 310)]}


@check('T03')
def _():
    sol = [(a, b, c) for b in range(0, 531) for a in [b + 60] for c in [b - 40] if c >= 0 and a + b + c == 530]
    assert len(sol) == 1
    a, b, c = sol[0]
    return {'a': s([b]), 'b': s([a]), 'c': s([c])}


@check('G01')
def _():
    sol = [(a, m, r) for a in range(0, 541) for m in [540 - a] for r in [610 - m] if a + r == 450 and r >= 0 and m >= 0]
    assert len(sol) == 1
    a, m, r = sol[0]
    return {'a': s([a]), 'b': s([m]), 'c': s([r])}


@check('G02')
def _():
    rv = lambda n: int(str(n)[::-1])
    d = lambda n: abs(n - rv(n))
    mid = {str(d(742))[1], str(d(831))[1]}
    assert len(mid) == 1
    # the pattern holds for every 3-digit number with different end digits
    assert all(str(d(n)).zfill(3)[1] == '9' for n in range(100, 1000) if n % 10 != n // 100)
    return {'a': s([d(742), d(831)]), 'b': list(mid), 'c': s([d(954)])}


@check('G03')
def _():
    sol = solve_add('4?6', '37?', 801)
    assert len(sol) == 1 and sol[0] == (2, 5)
    return ['open']


@check('G04')
def _():
    f = lambda a, b, c: s([x for x in range(0, 1001) if x + a == b - x])
    return {'a': f(175, 625, 0), 'b': f(240, 800, 0)}


@check('C01')
def _():
    return one(solve_add('2?6', '43?', 689))


@check('C02')
def _():
    return s([x for x in range(0, 1001) if 530 + 160 == 600 + x])


@check('C03')
def _():
    return s([x for x in range(0, 801) if 175 + x + 350 == 800])


@check('C04')
def _():
    sol = [(small, small + 60) for small in range(0, 421) if 2 * small + 60 == 420]
    return s([sol[0][0]])
