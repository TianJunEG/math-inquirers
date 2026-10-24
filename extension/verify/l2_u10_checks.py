"""Independent checks for Level 2 Unit 10 (mixed puzzles): graphs are read with their key, logic puzzles are solved by trying every assignment, coin puzzles by enumeration."""
import itertools
from fractions import Fraction as Fr
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U10-' + i] = f
        return f
    return d


def perms(cards):
    return sorted({int(''.join(map(str, p))) for p in itertools.permutations(cards, 3) if p[0] != 0})


@check('L01')
def _():
    return s([6 * 5])


@check('S01')
def _():
    pics = {'Football': 6, 'Swimming': 4, 'Chess': 3, 'Art': 5}
    key = 5
    return {'a': s([pics['Chess'] * key]), 'b': s([(pics['Football'] - pics['Swimming']) * key]), 'c': s([sum(pics.values()) * key])}


@check('S02')
def _():
    key, total = 5, 75
    pics = {'Football': 5, 'Swimming': 3, 'Chess': 4}
    art = [n for n in range(0, 40) if (sum(pics.values()) + n) * key == total]
    assert len(art) == 1
    return {'a': s(art), 'b': s([art[0] * key])}


@check('S03')
def _():
    ok = [n for n in range(41, 60) if n % 5 == 0 and sum(int(c) for c in str(n)) == 10]
    assert len(ok) == 1
    return s(ok)


@check('S04')
def _():
    def tally(n):                      # groups of 5 (4 strokes and a slash) then single strokes
        return (n // 5) * 5 + n % 5
    cats, dogs, fish = tally(7), tally(12), tally(4)
    return {'a': s([dogs]), 'b': s([dogs - cats]), 'c': s([cats + dogs + fish])}


@check('S05')
def _():
    L = perms([7, 0, 5])
    return {'a': s(L), 'b': s([max(L), min(L)]), 'c': s([sum(1 for n in L if 600 < n < 800)])}


@check('S06')
def _():
    rows = [(a, 6 - a, 10 * a + 20 * (6 - a)) for a in range(6, 0, -1)]
    totals = [r[2] for r in rows]
    assert totals[:2] == [60, 70]
    sol = [r for r in rows if r[2] == 110]
    assert len(sol) == 1
    return {'a': s(totals[2:]), 'b': s([sol[0][0], sol[0][1]])}


@check('S07')
def _():
    people, fruits = ['Ali', 'Mei', 'Ravi'], ['apple', 'banana', 'mango']
    sols = [p for p in itertools.permutations(fruits) if p[1] == 'mango' and p[0] != 'apple']
    assert len(sols) == 1
    return {'a': [sols[0][0]], 'b': [sols[0][1]], 'c': [sols[0][2]]}


@check('S08')
def _():
    eaten = Fr(1, 6) + Fr(2, 6)
    left = 1 - eaten
    return {'a': [f'{int(eaten * 6)}/6'], 'b': [f'{int(left * 6)}/6'], 'c': s([int(left * 6) * 100])}


@check('S09')
def _():
    cost = 3 * 120
    return {'a': [f'{cost // 100}.{cost % 100:02d}'], 'b': [f'{(500 - cost) // 100}.{(500 - cost) % 100:02d}']}


@check('S10')
def _():
    chairs = 4 * 10
    return {'a': s([chairs]), 'b': s([chairs - 28])}


@check('T01')
def _():
    people, acts = ['Ali', 'Mei', 'Siti', 'Ben'], ['swimming', 'chess', 'art', 'tennis']
    sols = []
    for p in itertools.permutations(acts):
        a, m, si, b = p
        if m != 'chess':
            continue
        if a in ('chess', 'art'):
            continue
        if si in ('swimming', 'tennis'):
            continue
        if b == 'tennis':
            continue
        sols.append(p)
    assert len(sols) == 1
    return {'a': [sols[0][0]], 'b': [sols[0][1]], 'c': [sols[0][2]], 'd': [sols[0][3]]}


@check('T02')
def _():
    sol = [(key, 7 * key, 3 * key) for key in range(1, 20) if 7 * key - 3 * key == 20]
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][1]]), 'c': s([sol[0][2]])}


@check('T03')
def _():
    mei = ali = 0
    first = None
    for day in range(1, 20):
        mei += 2 * day
        ali += 5
        if mei > ali and first is None:
            first = (day, mei - ali)
    return {'a': s([first[0]]), 'b': s([first[1]])}


@check('G01')
def _():
    key = 10
    dogs, cats = 3.5, 2.5
    return {'a': s([int(dogs * key)]), 'b': s([int(cats * key)]), 'c': s([int((dogs - cats) * key)])}


@check('G02')
def _():
    coins = [5, 10, 20, 20]
    amounts = set()
    for r in range(1, 5):
        for sub in itertools.combinations(range(4), r):
            amounts.add(sum(coins[i] for i in sub))
    return {'a': s([len(amounts)]), 'b': ['Yes' if 60 in amounts else 'No']}


@check('G03')
def _():
    people, pets = ['Ali', 'Mei', 'Ravi'], ['cat', 'dog', 'fish']
    sols = [p for p in itertools.permutations(pets) if p[1] == 'fish' and p[0] != 'cat']
    assert len(sols) == 1 and sols[0] == ('dog', 'fish', 'cat')
    return ['open']


@check('G04')
def _():
    sol = [(a, 8 - a) for a in range(0, 9) if 30 * a + 50 * (8 - a) == 340]
    assert len(sol) == 1
    totals = {30 * a + 50 * (8 - a) for a in range(0, 9)}
    return {'a': s(sol[0]), 'b': ['Yes' if 330 in totals else 'No']}


@check('C01')
def _():
    return s([5 * 10])


@check('C02')
def _():
    return s([len(perms([1, 0, 4]))])


@check('C03')
def _():
    people, cols = ['Ali', 'Ben', 'Mei'], ['red', 'blue', 'green']
    sols = [p for p in itertools.permutations(cols) if p[2] == 'blue' and p[0] != 'red']
    assert len(sols) == 1
    return [sols[0][1]]


@check('C04')
def _():
    return [f'{int((1 - Fr(5, 12)) * 12)}/12']
