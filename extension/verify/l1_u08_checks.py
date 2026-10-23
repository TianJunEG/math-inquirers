"""Independent checks for Level 1 Unit 8 (logic and sorting).  Orders, grids and clue puzzles are solved by trying every arrangement
against the clues (each puzzle must have exactly 1 solution); sorting by testing each number against the rule; number riddles by
scanning the range; the number grid by trying all rows; the yes/no questions by a small search."""
import itertools
from common import s, load_unit

CHECKS = {}
U = load_unit(1, 8)
ITEM = {it['id']: it for it in U['items']}
ITEM[U['learn']['try']['id']] = U['learn']['try']


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def only(xs):
    xs = list(xs)
    assert len(xs) == 1, f'{len(xs)} solutions: {xs}'
    return xs[0]


def orders(names, ok):
    """Every order (first to last) of names that satisfies ok(position_of)."""
    return [p for p in itertools.permutations(names) if ok({n: i + 1 for i, n in enumerate(p)})]


def say(n, k):
    return n % k == 0


# the worked example: Ravi tea, Jenny not milk
ex = [dict(zip(('Ravi', 'Jenny', 'Wei'), p)) for p in itertools.permutations(('milk', 'juice', 'tea'))]
ex = [a for a in ex if a['Ravi'] == 'tea' and a['Jenny'] != 'milk']
assert len(ex) == 1 and ex[0] == {'Ravi': 'tea', 'Jenny': 'juice', 'Wei': 'milk'}
# the picture in the worked example shows the same answer
_m = U['learn']['example']['figure']['marks']
assert [k for k, v in _m.items() if v == 'yes'] == ['0,2', '1,1', '2,0']


def assign(names, things, ok):
    return [dict(zip(names, p)) for p in itertools.permutations(things) if ok(dict(zip(names, p)))]


@check('L1U08-L01')
def _():
    sol = only(assign(['Mei', 'Ben', 'Kumar'], ['ball', 'kite', 'drum'], lambda a: a['Ben'] == 'drum' and a['Mei'] != 'ball'))
    return {'': [n for n, v in sol.items() if v == 'ball']}


@check('L1U08-S01')
def _():
    # older = earlier in the list of ages; order from oldest
    o = only(orders(['Siti', 'Wei', 'Jamie'], lambda p: p['Siti'] < p['Wei'] < p['Jamie']))
    return {'a': [o[0]], 'b': [o[-1]]}


@check('L1U08-S02')
def _():
    ben = 3
    return {'a': s([ben + 1]), 'b': s([ben - 1])}


@check('L1U08-S03')
def _():
    o = only(orders(['Ali', 'Mei', 'Ben', 'Siti'], lambda p: p['Ali'] == 1 and p['Mei'] == p['Ali'] + 1 and p['Ben'] == 4))
    return {'a': s([o.index('Siti') + 1]), 'b': list(o)}


@check('L1U08-S04')
def _():
    o = only(orders(['Ali', 'Mei', 'Ravi'], lambda p: p['Ali'] < p['Mei'] < p['Ravi']))   # tallest first
    tf = lambda b: 'True' if b else 'False'
    return {'a': [tf(o[-1] == 'Ravi')], 'b': [tf(o.index('Ali') < o.index('Ravi'))], 'c': [tf(o[0] == 'Mei')]}


@check('L1U08-S05')
def _():
    nums = [4, 7, 10, 13, 16, 9]
    return {'a': s([n for n in nums if n % 2 == 1]), 'b': s([n for n in nums if n % 2 == 0])}


@check('L1U08-S06')
def _():
    nums = range(5, 15)
    both = [n for n in nums if n > 8 and n % 2 == 1]
    out = [n for n in nums if not (n > 8) and not (n % 2 == 1)]
    return {'a': s([len(both)]), 'b': s(out)}


@check('L1U08-S07')
def _():
    f = ITEM['L1U08-S07']['figure']
    rule_a = lambda n: n % 2 == 1
    rule_b = lambda n: n > 10
    where = lambda n: ('ab' if rule_a(n) and rule_b(n) else 'a' if rule_a(n) else 'b' if rule_b(n) else 'out')
    wrong = [n for reg, ns in f['regions'].items() for n in ns if where(n) != reg]
    return s([only(wrong)])


@check('L1U08-S08')
def _():
    nums = range(1, 25)
    both = [n for n in nums if say(n, 3) and say(n, 4)]
    only4 = [n for n in nums if say(n, 4) and not say(n, 3)]
    return {'a': s(both), 'b': s([len(only4)])}


@check('L1U08-S09')
def _():
    sol = only(assign(['Ravi', 'Jenny', 'Wei'], ['apple', 'bun', 'pear'],
                      lambda a: a['Wei'] not in ('bun', 'pear') and a['Jenny'] != 'apple' and a['Ravi'] != 'pear'))
    return {'a': [sol['Ravi']], 'b': [sol['Jenny']], 'c': [sol['Wei']]}


@check('L1U08-S10')
def _():
    opts = [8, 12, 14, 16, 20]
    a = only([n for n in opts if not say(n, 4)])
    corners = {'triangle': 3, 'circle': 0, 'square': 4}
    b = only([k for k, v in corners.items() if v == 0])
    return {'a': s([a]), 'b': [b]}


@check('L1U08-S11')
def _():
    a = only([n for n in range(11, 20) if n % 2 == 1 and say(n, 5)])
    b = only([n for n in range(21, 30) if n % 2 == 0 and say(n, 3) and say(n, 4)])
    return {'a': s([a]), 'b': s([b])}


@check('L1U08-T01')
def _():
    names = ['Lily', 'Jason', 'Kumar', 'Aisha']
    sol = only(assign(names, ['drum', 'flute', 'piano', 'bell'],
                      lambda a: a['Lily'] not in ('drum', 'flute', 'piano') and a['Jason'] != 'piano' and a['Aisha'] != 'piano'
                      and a['Jason'] not in ('bell', 'drum')))
    assert (sol['Lily'], sol['Jason']) == ('bell', 'flute')
    return {'a': [sol['Kumar']], 'b': [sol['Aisha']]}


@check('L1U08-T02')
def _():
    nums = range(1, 21)
    both = [n for n in nums if say(n, 2) and say(n, 5)]
    out = [n for n in nums if not say(n, 2) and not say(n, 5)]
    return {'a': s([len(both)]), 'b': s([len(out)])}


@check('L1U08-T03')
def _():
    people = ['Mei', 'Aisha', 'Ravi', 'Ben', 'Siti']
    sols = [dict(zip(people, p)) for p in itertools.permutations([5, 6, 7, 8, 9])]
    sols = [a for a in sols if a['Mei'] == 9 and a['Aisha'] == 5 and a['Ravi'] < a['Ben'] < a['Siti']]
    sol = only(sols)
    return {'a': s([sol['Ben']]), 'b': s([sol['Siti']])}


@check('L1U08-G01')
def _():
    # statement -> truth value if `culprit` ate the biscuit
    def lies(culprit):
        said = {'Ali': culprit == 'Ben', 'Ben': culprit != 'Ben', 'Mei': culprit == 'Ali'}
        return sum(1 for v in said.values() if not v)
    return [only([c for c in ('Ali', 'Ben', 'Mei') if lies(c) == 1])]


@check('L1U08-G02')
def _():
    g = ITEM['L1U08-G02']['figure']['rows']
    perms = list(itertools.permutations([1, 2, 3, 4]))
    sols = []
    for rows in itertools.product(perms, repeat=4):
        if all(len({rows[i][j] for i in range(4)}) == 4 for j in range(4)) and \
           all(g[i][j] is None or g[i][j] == rows[i][j] for i in range(4) for j in range(4)):
            sols.append(rows)
    r = only(sols)
    return [' '.join(map(str, row)) for row in r]


@check('L1U08-G03')
def _():
    from functools import lru_cache

    @lru_cache(None)
    def f(n):   # fewest questions that always find 1 of n numbers (a question splits the group into 2 groups)
        if n == 1:
            return 0
        return 1 + min(max(f(k), f(n - k)) for k in range(1, n))
    sizes = {len([n for n in range(1, 5) if n > 2]), len([n for n in range(1, 5) if n <= 2])}   # "more than 2": the yes group and the no group
    return {'a': s([only(sizes)]), 'b': s([f(8)]), 'c': s([f(16)])}


@check('L1U08-C01')
def _():
    o = only(orders(['Siti', 'Ravi', 'Jamie'], lambda p: p['Siti'] < p['Ravi'] < p['Jamie']))
    return [o[-1]]


@check('L1U08-C02')
def _():
    return s([len([n for n in range(1, 11) if n % 2 == 0 and n > 5])])


@check('L1U08-C03')
def _():
    return s([only([n for n in range(21, 30) if n % 2 == 1 and say(n, 5)])])


@check('L1U08-C04')
def _():
    o = only(orders(['Ali', 'Mei', 'Ravi'], lambda p: p['Ali'] < p['Mei'] < p['Ravi']))   # taller first
    return ['Yes' if o.index('Ravi') < o.index('Ali') else 'No']
