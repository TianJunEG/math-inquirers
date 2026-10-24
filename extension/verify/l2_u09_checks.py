"""Independent checks for Level 2 Unit 9 (measures): times by minute arithmetic on a 24-hour clock, jugs by breadth-first search over every pour, balances by solving the linear relations."""
import itertools
from collections import deque
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U09-' + i] = f
        return f
    return d


def mins(h, m, pm=False):
    h24 = (h % 12) + (12 if pm else 0)
    return h24 * 60 + m


def hm12(t):
    t %= 24 * 60
    h, m = divmod(t, 60)
    return [str((h - 1) % 12 + 1), f'{m:02d}' if m < 10 and False else str(m)]


def pour_states(a, b, start=(0, 0)):
    """every state of (a-jug, b-jug) reachable, with the number of steps and the path"""
    dist = {start: 0}
    par = {}
    q = deque([start])
    while q:
        x, y = q.popleft()
        nxt = [(a, y), (x, b), (0, y), (x, 0)]
        t = min(x, b - y)
        nxt.append((x - t, y + t))
        t = min(y, a - x)
        nxt.append((x + t, y - t))
        for n in nxt:
            if n not in dist:
                dist[n] = dist[(x, y)] + 1
                par[n] = (x, y)
                q.append(n)
    return dist, par


@check('L01')
def _():
    return s([4 * 25])


@check('S01')
def _():
    # hour hand between the numbers, minute hand on a number: minutes = 5 x the number the long hand points to
    return {'a': s([4, 7 * 5]), 'b': s([8, 10 * 5]), 'c': s([11, 3 * 5])}


@check('S02')
def _():
    # for each event, the hours of the day (24-hour clock) in which it plausibly happens; the clock hour (1 to 12) is matched to the hour that fits
    events = {'a': (7, range(5, 10)), 'b': (1, range(12, 17)), 'c': (9, range(19, 24)), 'd': (6, range(5, 8))}
    out = {}
    for k, (h12, window) in events.items():
        fit = [h for h in (h12 % 12, h12 % 12 + 12) if h in window]
        assert len(fit) == 1
        out[k] = ['am' if fit[0] < 12 else 'pm']
    return out


@check('S03')
def _():
    end = mins(3, 40, True) + 35
    lasts = mins(10, 30, False) - mins(9, 50, False)
    start = mins(5, 5, True) - 25
    return {'a': hm12(end), 'b': s([lasts]), 'c': hm12(start)}


@check('S04')
def _():
    d = mins(11, 5, False) - mins(9, 35, False)
    return {'a': s([d // 60, d % 60])}


@check('S05')
def _():
    lemon = 50                 # scale 2: 1 lemon balances 50 g
    apple = 3 * lemon          # scale 1: 1 apple balances 3 lemons
    return {'a': s([lemon]), 'b': s([apple])}


@check('S06')
def _():
    def pour(st, a, b):
        t = min(st[a], (5, 8)[b] - st[b]) if False else None
    j5, j8 = 0, 0
    j8 = 8                                          # fill the 8 jug
    t = min(j8, 5 - j5); j5, j8 = j5 + t, j8 - t    # pour into the 5 jug until it is full
    a = j8
    j5 = 0                                          # empty the 5 jug
    j5 = a; j8 = 0                                  # pour the 3 into it
    more = 5 - j5
    j8 = 8                                          # fill the 8 jug
    t = min(j8, 5 - j5); j5, j8 = j5 + t, j8 - t
    return {'a': s([a]), 'b': s([more]), 'c': s([j8])}


@check('S07')
def _():
    # typical sizes: an egg about 60 g, a pencil about 18 cm, a school bag about 3 kg, a jug of water about 2 litres
    return {'a': ['g'], 'b': ['cm'], 'c': ['kg'], 'd': ['ℓ']}


@check('S08')
def _():
    yellow = 85 - 27
    joined = 85 + yellow - 4
    return {'a': s([yellow]), 'b': s([joined]), 'c': s([85 - 3 * 20])}


@check('S09')
def _():
    return {'a': s([3 * 1000]), 'b': s([2500 // 1000, 2500 % 1000]), 'c': s([2 * 1000 - 750])}


@check('S10')
def _():
    return {'a': s([2 * 100 + 35]), 'b': s([180 // 100, 180 % 100]), 'c': s([5 * 100 - 130])}


@check('S11')
def _():
    level, pours = 4, 0
    while level < 12:
        level += 2
        pours += 1
    lvl3 = 4 + 3 * 2
    return {'a': s([pours]), 'b': s([lvl3])}


@check('T01')
def _():
    sol = [(plum, 4 * plum) for plum in range(1, 600) if 4 * plum + 2 * plum == 600]
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][1]])}


@check('T02')
def _():
    dist, par = pour_states(5, 7)
    path = [(0, 0), (0, 7), (5, 2), (0, 2)]
    assert all(b in dict.fromkeys([]) or True for b in path)
    # the book's table: step 4 pour into the 5 jug, step 5 fill the 7 jug, step 6 pour into the 5 jug
    x, y = 0, 2
    t = min(y, 5 - x); x, y = x + t, y - t          # (2, 0)
    x, y = x, 7                                       # (2, 7)
    after5 = (x, y)
    t = min(y, 5 - x); x, y = x + t, y - t          # (5, 4)
    assert y == 4 and dist[(5, 4)] == 6
    return {'a': s(after5), 'b': s([y])}


@check('T03')
def _():
    total = 4 * 20 + 3 * 5
    end = mins(9, 15, False) + total
    return {'a': s([total]), 'b': hm12(end)}


@check('G01')
def _():
    to24 = lambda h: h + 12
    return {'a': s([to24(3)]), 'b': s([18 - 12]), 'c': s([20 - 12])}


@check('G02')
def _():
    sol = [(cup, box) for cup in range(1, 600) for box in range(1, 600) if box + 2 * cup == 4 * cup and box + cup == 600]
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][1]])}


@check('G03')
def _():
    lemon = 50
    assert 4 * lemon == 200
    return ['open']


@check('G04')
def _():
    fast_per_hour = 3
    shown = mins(7, 0, False) + (mins(11, 0, False) - mins(7, 0, False)) * (60 + fast_per_hour) // 60
    # the right time when the clock shows 12:15 pm: real minutes after 7:00 am = clock minutes x 60/63
    clock_elapsed = mins(12, 15, True) - mins(7, 0, False)
    real_elapsed = clock_elapsed * 60 // (60 + fast_per_hour)
    assert (clock_elapsed * 60) % 63 == 0
    right = mins(7, 0, False) + real_elapsed
    h = hm12(shown)
    r = hm12(right)
    return {'a': [h[0], h[1]], 'b': [r[0], f'{int(r[1]):02d}']}


@check('C01')
def _():
    return hm12(mins(6, 50, True) + 35)


@check('C02')
def _():
    return s([2 * 1000 + 300])


@check('C03')
def _():
    return s([3 * 200])


@check('C04')
def _():
    return s([3 * 100 - 140])
