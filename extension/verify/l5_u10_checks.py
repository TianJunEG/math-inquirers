"""Independent checks for Level 5 Unit 10 (Challenge day): puzzles are solved by brute force over every possibility (permutations, all pairs, all
whole numbers) and by simulating each story forwards; nothing is copied from the book."""
import itertools
from fractions import Fraction as Fr

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def fs(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{float(x):g}'


def solutions(people, things, clues):
    return [dict(zip(people, p)) for p in itertools.permutations(things) if all(c(dict(zip(people, p))) for c in clues)]


@check('L5U10-L01')
def _():
    people, drinks = ['Ben', 'Kumar', 'Aisha'], ['tea', 'juice', 'milk']
    sols = solutions(people, drinks, [lambda a: a['Ben'] not in ('juice', 'milk'), lambda a: a['Aisha'] != 'tea', lambda a: a['Kumar'] != 'milk'])
    assert len(sols) == 1
    return [next(p for p, d in sols[0].items() if d == 'juice')]


@check('L5U10-S01')
def _():
    for n in range(1, 1000):
        if Fr(n * 3 + 8, 2) == 19:
            return [str(n)]


@check('L5U10-S02')
def _():
    for money in range(1, 1000):
        m = Fr(money)
        m -= m / 4
        m -= 6
        if m == 15:
            return [str(money)]


@check('L5U10-S03')
def _():
    runners = ['Ali', 'Mei', 'Siti']
    wins = set()
    for order in itertools.permutations(runners):                  # order[0] won, order[2] was last
        pos = {r: i for i, r in enumerate(order)}
        if pos['Ali'] != 0 and pos['Siti'] != 2 and pos['Mei'] > pos['Siti']:
            wins.add(order[0])
    assert len(wins) == 1
    return sorted(wins)


@check('L5U10-S04')
def _():
    pairs = [(a, b) for a in range(0, 100) for b in range(0, 100) if a + b == 75 and a - b == 19]
    assert len(pairs) == 1
    return {'a': [str(pairs[0][0])], 'b': [str(pairs[0][1])]}


def count_squares(w, h, size):
    return sum(1 for x in range(w) for y in range(h) if x + size <= w and y + size <= h)


@check('L5U10-S05')
def _():
    return {'a': [str(count_squares(3, 3, 1))], 'b': [str(count_squares(3, 3, 2))], 'c': [str(count_squares(3, 3, 3))],
            'd': [str(sum(count_squares(3, 3, k) for k in (1, 2, 3)))]}


@check('L5U10-S06')
def _():
    kids = ['Kai', 'Lin', 'Mo']
    ok = []
    for culprit in kids:
        said = {'Kai': culprit == 'Mo'}                       # "Mo ate it."
        said['Lin'] = culprit != 'Lin'                        # "I did not eat it."
        said['Mo'] = not said['Kai']                          # "Kai is lying."
        if sum(said.values()) == 1:
            ok.append(culprit)
    assert len(ok) == 1
    return ok


@check('L5U10-S07')
def _():
    for years in range(0, 200):
        if 2 * (8 + years) == 36 + years:
            return [str(years)]


@check('L5U10-S08')
def _():
    for start in range(1, 1000):
        s = Fr(start)
        s -= s / 3
        s -= s / 2
        if s == 12:
            return [str(start)]


@check('L5U10-S09')
def _():
    sols = [(c, 20 - c) for c in range(0, 21) if 4 * c + 2 * (20 - c) == 56]
    assert len(sols) == 1
    return {'a': [str(sols[0][0])], 'b': [str(sols[0][1])]}


@check('L5U10-S10')
def _():
    pairs = [(a, b) for a in range(1, 73) for b in range(a, 73) if a * b == 72 and a + b == 17]
    assert len(pairs) == 1
    return {'a': [str(pairs[0][0]), str(pairs[0][1])]}


@check('L5U10-S11')
def _():
    nums = sorted(int(''.join(map(str, p))) for p in itertools.permutations([1, 2, 3]))
    evens = [n for n in nums if n % 2 == 0]
    closest = min(nums, key=lambda n: abs(n - 250))
    return {'a': [str(len(nums))], 'b': [str(e) for e in evens], 'c': [str(closest)]}


@check('L5U10-S12')
def _():
    return [str(sum(str(n).count('7') for n in range(1, 81)))]


@check('L5U10-T01')
def _():
    people, sports = ['Ben', 'Kumar', 'Aisha', 'Wei'], ['swimming', 'tennis', 'football', 'badminton']
    clues = [lambda a: a['Ben'] not in ('tennis', 'badminton'), lambda a: a['Kumar'] not in ('swimming', 'tennis'),
             lambda a: a['Wei'] not in ('swimming', 'badminton', 'tennis')]
    sols = solutions(people, sports, clues)
    assert len(sols) == 1
    s = sols[0]
    return {'a': [s['Ben']], 'b': [s['Kumar']], 'c': [s['Aisha']], 'd': [s['Wei']]}


@check('L5U10-T02')
def _():
    w, h = 5, 2
    squares = sum(count_squares(w, h, k) for k in range(1, 3))
    rects = 0
    for x1, x2 in itertools.combinations(range(w + 1), 2):          # pick 2 vertical lines
        for y1, y2 in itertools.combinations(range(h + 1), 2):      # and 2 horizontal lines
            rects += 1
    return {'a': [str(squares)], 'b': [str(rects)]}


@check('L5U10-T03')
def _():
    for start in range(1, 1000):
        c = Fr(start)
        c -= c / 4
        c += 3
        c -= c / 3
        if c == 14:
            return [str(start)]


@check('L5U10-G01')
def _():
    return [str(sum(1 for n in range(100, 1000) if sum(map(int, str(n))) == 8 and len(set(str(n))) == 3))]


@check('L5U10-G02')
def _():
    sols = []
    for k in range(0, 16):                  # k coins of 5c and k coins of 20c
        ten = 30 - 2 * k
        if ten >= 0 and 5 * k + 20 * k + 10 * ten == 345:
            sols.append((k, ten))
    assert len(sols) == 1
    return {'a': [str(sols[0][0])], 'b': [str(sols[0][0])], 'c': [str(sols[0][1])]}


@check('L5U10-G03')
def _():
    # worst case search: the largest number of socks you can take with no two of the same colour, plus one
    colours = ['red', 'blue', 'black']
    most_without_pair = max(len(c) for r in range(0, 4) for c in itertools.combinations(colours, r))
    return [str(most_without_pair + 1)]


@check('L5U10-C01')
def _():
    for n in range(1, 1000):
        if (n + 7) * 4 == 60:
            return [str(n)]


@check('L5U10-C02')
def _():
    for money in range(5, 1000, 5):
        m = Fr(money)
        m -= Fr(2, 5) * m
        m -= 9
        if m == 12:
            return [str(money)]


@check('L5U10-C03')
def _():
    sols = [g for g in range(0, 10) if 4 * g + 2 * (9 - g) == 26]
    assert len(sols) == 1
    return [str(sols[0])]


@check('L5U10-C04')
def _():
    return [str(sum(count_squares(3, 2, k) for k in (1, 2)))]
