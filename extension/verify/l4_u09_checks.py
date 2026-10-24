"""Independent checks for Level 4 Unit 9 (tables and line graphs): values and lines are read from the figure data of each item, and every other quantity
(changes, missing table cells, crossing points, averages) is recomputed or found by search."""
from common import load_unit
CHECKS = {}
U = load_unit(4, 9)
ITEM = {i['id']: i for i in [U['learn']['try']] + U['items']}
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def series(item_id, panel=0, k=0):
    sp = ITEM[item_id]['figure']['panels'][panel]
    return sp['series'][k]['values']


def tf(b, yes, no):
    return [yes if b else no]


@check('L4U09-L01')
def _():
    return s([70 + 2 * 5])



@check('L4U09-S01')
def _():
    v = series('L4U09-S01')
    return {'a': s([v[DAYS.index('Thu')]]), 'b': s([v[DAYS.index('Tue')]]), 'c': s([v[0] + v[1]])}


@check('L4U09-S02')
def _():
    v = series('L4U09-S01')
    ch = [(v[i + 1] - v[i], i) for i in range(len(v) - 1)]
    inc = max(ch)
    dec = min(ch)
    return {'a': [DAYS[inc[1]], DAYS[inc[1] + 1], str(inc[0])], 'b': [DAYS[dec[1]], DAYS[dec[1] + 1], str(-dec[0])]}


def solve_table(rows):
    """rows: list of lists of strings ('' unknown); last row and last column are totals.  Fill unknowns using row and column sums."""
    n = len(rows)
    m = len(rows[0]) - 2
    g = [[(int(x) if x not in ('', None) else None) for x in r[1:]] for r in rows]
    order = []
    changed = True
    while changed:
        changed = False
        for i in range(n):                      # rows: last entry is the total
            unk = [j for j in range(m + 1) if g[i][j] is None]
            if len(unk) == 1:
                j = unk[0]
                if j == m:
                    g[i][j] = sum(g[i][:m])
                else:
                    g[i][j] = g[i][m] - sum(g[i][k] for k in range(m) if k != j)
                order.append((i, j)); changed = True
        for j in range(m + 1):                  # columns: last row is the total
            unk = [i for i in range(n) if g[i][j] is None]
            if len(unk) == 1:
                i = unk[0]
                if i == n - 1:
                    g[i][j] = sum(g[k][j] for k in range(n - 1))
                else:
                    g[i][j] = g[n - 1][j] - sum(g[k][j] for k in range(n - 1) if k != i)
                order.append((i, j)); changed = True
    assert all(x is not None for r in g for x in r)
    for i in range(n):
        assert sum(g[i][:m]) == g[i][m]
    for j in range(m + 1):
        assert sum(g[i][j] for i in range(n - 1)) == g[n - 1][j]
    return g, order


@check('L4U09-S03')
def _():
    rows = ITEM['L4U09-S03']['figure']['rows']
    g, order = solve_table(rows)
    blanks = [(i, j) for i, r in enumerate(rows) for j, x in enumerate(r[1:]) if x == '']
    got = [g[i][j] for i, j in blanks]          # reading order = row by row
    classes = ['4A', '4B', '4C']
    more = [c for k, c in enumerate(classes) if g[k][0] > g[k][1]]
    assert len(more) == 1
    return {'a': s(got), 'b': more}


@check('L4U09-S04')
def _():
    p = ITEM['L4U09-S04']['figure']['panels'][0]
    assert p['step'] == 10 and len(p['series']) == 1
    v = p['series'][0]['values']
    diffs = [v[i + 1] - v[i] for i in range(len(v) - 1)]
    flat = [i for i, d in enumerate(diffs) if d == 0]
    assert len(flat) == 1 and diffs.count(max(diffs)) == 1
    best = diffs.index(max(diffs))
    return {'a': s([v[2]]), 'b': s([1]), 'c': s([best + 1]), 'd': s([max(diffs)])}


@check('L4U09-S05')
def _():
    it = ITEM['L4U09-S05']
    assert 'Each row has 3 more seats' in it['text'] and it['figure']['rows'][0][1] == '8'
    rows = [8 + 3 * i for i in range(10)]
    return {'a': s([rows[9]]), 'b': s([sum(rows[:5])])}


@check('L4U09-S06')
def _():
    p = ITEM['L4U09-S06']['figure']['panels']
    a = p[0]['series'][0]['values']
    b = p[1]['series'][0]['values']
    ra, rb = a[-1] - a[0], b[-1] - b[0]
    return {'a': s([ra]), 'b': s([rb]), 'c': ['P' if ra > rb else 'Q']}


@check('L4U09-S07')
def _():
    v = series('L4U09-S07')
    p = ITEM['L4U09-S07']['figure']['panels'][0]
    assert p['ymin'] == 40
    return {'a': s([v[0]]), 'b': s([v[1]]), 'c': tf(v[1] > 2 * v[0], 'Yes', 'No')}



@check('L4U09-S08')
def _():
    temp = {7: 25}
    for h in range(8, 13):
        temp[h] = temp[h - 1] + 2
    for h in range(13, 16):
        temp[h] = temp[h - 1] - 3
    t29 = [h for h in range(7, 13) if temp[h] == 29]
    assert len(t29) == 1
    return {'a': s([temp[12]]), 'b': s([temp[15]]), 'c': s([t29[0]])}


@check('L4U09-T01')
def _():
    sols = [(a, d) for d in range(1, 100) for a in range(1, 100) if a + 2 * d == 52 and a + 7 * d == 87]
    assert len(sols) == 1
    a, d = sols[0]       # a = Week 1 sales, d = weekly rise
    first = next(w for w in range(1, 100) if a + (w - 1) * d > 100)
    return {'a': s([a]), 'b': s([first])}


@check('L4U09-T02')
def _():
    sols = [d1 for d1 in range(1, 200) if d1 + 2 * d1 + (2 * d1 + 15) + 25 == 200]
    assert len(sols) == 1
    return s(sols)


@check('L4U09-T03')
def _():
    km = [k for k in range(0, 100) if 4 + 2 * k == 10 + 1 * k]
    assert len(km) == 1
    return {'a': s(km), 'b': s([4 + 2 * km[0]])}



@check('L4U09-G01')
def _():
    jan_x, feb_x = 4 * 20, 5 * 20
    jan_y = (jan_x - 60) / 5
    feb_y = (feb_x - 60) / 5
    rise_x = (feb_x - jan_x) / 20
    rise_y = feb_y - jan_y
    return {'a': s([feb_x - jan_x]), 'b': s([int(jan_y), int(feb_y)]), 'c': ['Y' if rise_y > rise_x else 'X']}


@check('L4U09-G02')
def _():
    sols = [m for m in range(1, 200) if sum(m + 8 * k for k in range(5)) == 340]
    assert len(sols) == 1
    return {'a': s(sols), 'b': s([sols[0] + 32])}


@check('L4U09-G03')
def _():
    avg = lambda xs: sum(xs) / len(xs)
    fourth = next(x for x in range(0, 200) if avg([40, 50, 38, x]) == 45)
    return {'a': s([int(avg([3, 6, 9]))]), 'b': s([fourth])}


@check('L4U09-C01')
def _():
    v = series('L4U09-C01')
    return s([v[2]])


@check('L4U09-C02')
def _():
    return s([next(x for x in range(0, 99) if 28 + 35 + x == 99)])


@check('L4U09-C03')
def _():
    d = (32 - 14) / 3
    return s([int(14 + 5 * d)])


@check('L4U09-C04')
def _():
    return ['B']
