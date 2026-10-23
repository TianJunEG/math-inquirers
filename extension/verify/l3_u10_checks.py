"""Independent checks for Level 3 Unit 10 (Puzzle day): graphs are read from the bar heights, logic puzzles are solved by trying every
arrangement, lists are made by brute force, and tables are built row by row."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def only(xs):
    xs = list(xs)
    assert len(xs) == 1, xs
    return xs[0]


@check('L3U10-L01')
def _():
    front, back = 2, 7
    line = [None] * (front + back - 1)
    return s([len(line)])


@check('L3U10-S01')
def _():
    bars = {'Ali': 25, 'Ben': 15, 'Mei': 30, 'Siti': 10}
    kumar = bars['Siti'] + 15
    bars['Kumar'] = kumar
    return {'a': [max(bars, key=bars.get) if max(bars, key=bars.get) != 'Kumar' else 'Kumar'], 'b': s([bars['Mei'] - bars['Ben']]), 'c': s([kumar]), 'd': s([sum(bars.values())])}


@check('L3U10-S02')
def _():
    v = {'A': 70, 'B': 110, 'C': 90}     # bar tops read between the labelled lines (thin line = 10)
    return {'a': s([v['A']]), 'b': s([v['B']]), 'c': s([v['C']]), 'd': s([sum(v.values())])}


@check('L3U10-S04')
def _():
    names = ['Kumar', 'Aisha', 'Wei', 'Lily']
    fruits = ['apple', 'banana', 'grapes', 'orange']
    sols = []
    for p in itertools.permutations(fruits):
        have = dict(zip(names, p))
        if have['Kumar'] in ('apple', 'banana'):
            continue
        owner = [n for n in names if have[n] == 'orange'][0]
        if len(owner) != 4:
            continue
        if have['Wei'] == 'apple':
            continue
        sols.append(have)
    h = only(sols)
    return {'a': [h['Kumar']], 'b': [h['Aisha']], 'c': [h['Wei']], 'd': [h['Lily']]}


@check('L3U10-S05')
def _():
    # (a) positions: Ravi 3rd, 5 between, Mei last
    a = 3 + 5 + 1
    # (b) 8th from the front and 2nd from the back: build the line and search its length
    b = only(n for n in range(1, 40) if n - 2 + 1 == 8)
    return {'a': s([a]), 'b': s([b])}


@check('L3U10-S06')
def _():
    nums = sorted({int(''.join(p)) for p in itertools.permutations('369')})
    return {'a': s(nums), 'b': s([sum(1 for n in nums if n % 2 == 0)]), 'c': s([min(nums, key=lambda n: abs(n - 700))])}


@check('L3U10-S07')
def _():
    sticks = {1: 6}
    for n in range(2, 12):
        sticks[n] = sticks[n - 1] + 5          # each new hexagon shares one side with the last
    assert (sticks[2], sticks[3]) == (11, 16)
    return {'a': s([sticks[6]]), 'b': s([only(n for n, v in sticks.items() if v == 41)])}


@check('L3U10-S08')
def _():
    out = [n for n in range(100, 400) if n % 2 == 0 and sum(map(int, str(n))) == 9 and '0' not in str(n) and (n // 10) % 10 > n % 10]
    return s(out)


@check('L3U10-S09')
def _():
    sols = [(a, b) for a in range(0, 61) for b in range(0, 61) if a + b == 60 and b == a + 14]
    return s(only(sols))


@check('L3U10-S03')
def _():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    def day_of(date):
        d = days.index('Tue')
        for _ in range(date - 3):
            d = (d + 1) % 7
        return days[d]
    return {'a': [day_of(24)], 'b': [day_of(30)]}


@check('L3U10-S10')
def _():
    cents = 1000 - (2 * 185 + 340)
    return [f'{cents // 100}.{cents % 100:02d}']


@check('L3U10-T01')
def _():
    n = 7
    return s([sum(1 for a, b in itertools.combinations(range(n), 2))])


@check('L3U10-T02')
def _():
    culprits = []
    for culprit in ('Ben', 'Aisha', 'Wei'):
        ben_true = (culprit == 'Wei')
        aisha_true = (culprit != 'Aisha')
        wei_true = (not ben_true)            # Wei says Ben is telling a lie
        if sum([ben_true, aisha_true, wei_true]) == 1:
            culprits.append(culprit)
    return [only(culprits)]


@check('L3U10-T03')
def _():
    sols = []
    for mon in range(1, 100):
        tue, wed, thu = mon + 15, 2 * mon, 2 * mon - 10
        if mon + tue + wed + thu == 185:
            sols.append((mon, tue, wed, thu))
    mon, tue, wed, thu = only(sols)
    return {'a': s([mon]), 'b': s([tue]), 'c': s([wed]), 'd': s([thu])}


@check('L3U10-G01')
def _():
    n = 4
    by_size = {k: (n - k + 1) ** 2 for k in range(1, n + 1)}
    return {'a': s([by_size[1]]), 'b': s([by_size[2]]), 'c': s([by_size[3]]), 'd': s([sum(by_size.values())])}


@check('L3U10-G02')
def _():
    # least number of weighings that always finds the light coin among n coins (balance scale), by recursion over every way to split
    from functools import lru_cache

    @lru_cache(None)
    def f(n):
        if n == 1:
            return 0
        best = 99
        for a in range(1, n // 2 + 1):
            rest = n - 2 * a
            worst = max(f(a), f(rest) if rest else 0)
            best = min(best, 1 + worst)
        return best
    return {'a': s([f(3)]), 'b': s([f(9)])}


@check('L3U10-G03')
def _():
    sols = [(t, w) for t in range(0, 9) for w in range(0, 9) if t + w == 8 and 10 * t + 20 * w == 150]
    t, w = only(sols)
    return {'a': s([t]), 'b': s([w])}


@check('L3U10-G04')
def _():
    people = ['Lily', 'Wei', 'Kumar']
    games = ['chess', 'ball', 'cards']
    sols = []
    for p in itertools.permutations(games):
        have = dict(zip(people, p))
        if have['Lily'] == 'ball':
            continue
        if have['Wei'] in ('chess', 'cards'):
            continue
        if have['Kumar'] == 'chess':
            continue
        sols.append(have)
    h = only(sols)
    return [f'Lily: {h["Lily"]}']


@check('L3U10-C01')
def _():
    return s([35 - 20])


@check('L3U10-C02')
def _():
    return s([4 + 5 - 1])


@check('L3U10-C03')
def _():
    nums = {int(''.join(p)) for p in itertools.permutations('147')}
    return s([sum(1 for n in nums if n % 2 == 0)])


@check('L3U10-C04')
def _():
    seq = [2]
    while len(seq) < 8:
        seq.append(seq[-1] + 4)
    return s([seq[7]])
