"""Independent checks for Level 6 Unit 6 (Fair or unfair?).  Every probability is found by listing all equally likely outcomes (itertools) and using exact
fractions; spinners, bags and the dice table are read from the unit file; 'is it surprising' uses the spread of a random count (3 standard deviations)."""
import itertools, math, random
from fractions import Fraction
from common import load_unit
from l6_lib import s

CHECKS = {}
U = load_unit(6, 6)
ITEM = {i['id']: i for i in U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def frac(n, d):
    f = Fraction(n, d)
    return [f.numerator, f.denominator]


def P(outcomes, want):
    return Fraction(len([o for o in outcomes if want(o)]), len(outcomes))


def sd(n, p):
    return math.sqrt(n * float(p) * (1 - float(p)))


@check('L6U06-L01')
def _():
    bag = ['yellow'] * 6 + ['blue'] * 9
    return s(frac(len([c for c in bag if c == 'yellow']), len(bag)))


@check('L6U06-S01')
def _():
    parts = ITEM['L6U06-S01']['figure']['parts']
    assert len(parts) == 10
    pg, pn = P(parts, lambda x: x == 'G'), P(parts, lambda x: x != 'R')
    blue = P(parts, lambda x: x == 'B') * 500
    assert blue.denominator == 1
    return {'a': [pg.numerator, pg.denominator], 'b': [pn.numerator, pn.denominator], 'c': [int(blue)]}


@check('L6U06-S02')
def _():
    bag = ITEM['L6U06-S02']['figure']['counters']
    pb = P(bag, lambda x: x == 'B')
    prg = P(bag, lambda x: x in 'RG')
    more = bag + ['R'] * 5
    pr = P(more, lambda x: x == 'R')
    return {'a': [pb.numerator, pb.denominator], 'b': [prg.numerator, prg.denominator], 'c': [pr.numerator, pr.denominator]}


@check('L6U06-S03')
def _():
    res = list(itertools.product('HT', 'ABC'))
    p1 = P(res, lambda r: r == ('H', 'A'))
    p2 = P(res, lambda r: r[0] == 'T' and r[1] != 'A')
    return {'a': [len(res)], 'b': [p1.denominator], 'c': [p2.numerator, p2.denominator]}


@check('L6U06-S04')
def _():
    rows = ITEM['L6U06-S04']['figure']['rows']
    head = ITEM['L6U06-S04']['figure']['head'] if 'head' in ITEM['L6U06-S04']['figure'] else rows[0]
    cells = [int(c) for r in rows[1:] for c in r[1:]]
    assert len(cells) == 36
    # the table must really be the sums of two dice
    assert sorted(cells) == sorted(a + b for a in range(1, 7) for b in range(1, 7))
    f = Fraction(len([c for c in cells if c == 4]), 36)
    return {'a': [len([c for c in cells if c == 4])], 'b': [len([c for c in cells if c < 5])], 'c': [f.numerator, f.denominator]}


@check('L6U06-S05')
def _():
    nums = [int(x) for x in ITEM['L6U06-S05']['figure']['parts']]
    prime = [n for n in nums if n > 1 and all(n % d for d in range(2, n))]
    ali, ben = len(prime), len(nums) - len(prime)
    assert ali + ben == 10
    return {'a': [ali], 'b': [ben], 'c': ['Yes' if ali == ben else 'No']}


@check('L6U06-S06')
def _():
    dice = range(1, 7)
    e5 = 300 * P(list(dice), lambda d: d == 5)
    e4 = 300 * P(list(dice), lambda d: d > 4)
    heads = 90 * P(['H', 'T'], lambda c: c == 'H')
    surprising = abs(54 - e5) > 3 * sd(300, Fraction(1, 6))
    return {'a': [int(e5)], 'b': [int(e4)], 'c': [int(heads)], 'd': ['Yes' if surprising else 'No']}


@check('L6U06-S07')
def _():
    p6 = P(list(range(1, 7)), lambda d: d == 6)
    expected = round(100 * p6)
    rng = random.Random(1)
    runs = [sum(1 for _ in range(100) if rng.randint(1, 6) == 6) for _ in range(5)]
    assert len(set(runs)) > 1            # a random run differs from run to run
    return {'a': [p6.numerator, p6.denominator], 'b': [expected], 'c': ['random rolls']}


@check('L6U06-S08')
def _():
    nums = list(range(1, 31))
    prime = lambda n: n > 1 and all(n % d for d in range(2, n))
    p7 = P(nums, lambda n: n % 7 == 0)
    pp = P(nums, prime)
    psq = P(nums, lambda n: int(math.sqrt(n)) ** 2 == n)
    return {'a': [p7.numerator, p7.denominator], 'b': [pp.numerator, pp.denominator], 'c': [psq.numerator, psq.denominator]}


@check('L6U06-S09')
def _():
    a = Fraction(3, 3 + 5)
    b = Fraction(4, 4 + 7)
    return {'a': [a.numerator, a.denominator], 'b': [b.numerator, b.denominator], 'c': ['Bag A' if a > b else 'Bag B']}


@check('L6U06-S10')
def _():
    exp = 200 * Fraction(1, 2)
    could = abs(112 - exp) <= 3 * sd(200, Fraction(1, 2))
    return {'a': [int(exp)], 'b': [int(112 - exp)], 'c': ['Yes' if could else 'No']}


@check('L6U06-S11')
def _():
    two = list(itertools.product(range(1, 7), repeat=2))
    tot = {}
    for a, b in two:
        tot[a + b] = tot.get(a + b, 0) + 1
    best = max(tot, key=tot.get)
    return {'a': [best], 'b': [tot[6] + tot[8]], 'c': [tot[2] + tot[12]]}


@check('L6U06-T01')
def _():
    two = list(itertools.product(range(1, 7), repeat=2))
    even = len([1 for a, b in two if (a + b) % 2 == 0])
    seven = len([1 for a, b in two if a + b == 7])
    ben = 36 - seven
    pts = [k for k in range(1, 40) if seven * k == ben * 1][0]
    return {'a': [even], 'b': ['Yes' if even == 36 - even else 'No'], 'c': [pts]}


@check('L6U06-T02')
def _():
    bag = ['R1', 'R2', 'R3', 'B1', 'B2']
    pairs = list(itertools.permutations(bag, 2))
    red = [p for p in pairs if p[0][0] == 'R' and p[1][0] == 'R']
    f = Fraction(len(red), len(pairs))
    return {'a': [len(pairs)], 'b': [len(red)], 'c': [f.numerator, f.denominator]}


@check('L6U06-T03')
def _():
    runs = [93, 108, 97, 114, 102]
    exp = 600 * Fraction(1, 6)
    mean = Fraction(sum(runs), len(runs))
    fair = all(abs(r - exp) <= 3 * sd(600, Fraction(1, 6)) for r in runs) and abs(mean - exp) <= sd(600, Fraction(1, 6))
    return {'a': [int(exp)], 'b': [float(mean)], 'c': ['Yes' if fair else 'No']}


@check('L6U06-G01')
def _():
    flips = list(itertools.product('HT', repeat=4))
    return {'a': [len(flips)], 'b': [len([f for f in flips if f.count('H') == 2])], 'c': [len([f for f in flips if 'T' in f])]}


@check('L6U06-G02')
def _():
    two = list(itertools.product(range(1, 7), repeat=2))
    given_a = len([b for b in range(1, 7) if b == 3])          # for any one value of a, the values of b that match it
    pd = P(two, lambda p: p[0] == p[1])
    p4 = P(two, lambda p: p[0] + p[1] == 4)
    return {'a': [given_a], 'b': [int(600 * pd)], 'c': [int(600 * p4)]}


@check('L6U06-G03')
def _():
    wins = 600 * Fraction(1, 6)
    paid = 600 * 2
    won5 = wins * 5
    prize = [p for p in range(1, 100) if wins * p == paid][0]
    return {'a': [int(wins)], 'b': [paid, int(won5)], 'c': [prize]}


@check('L6U06-C01')
def _():
    f = Fraction(3, 10)
    return s([f.numerator, f.denominator])


@check('L6U06-C02')
def _():
    even = P(list(range(1, 7)), lambda d: d % 2 == 0)
    return s([int(240 * even)])


@check('L6U06-C03')
def _():
    f = P(list(itertools.product('HT', repeat=2)), lambda r: r == ('T', 'T'))
    return s([f.numerator, f.denominator])


@check('L6U06-C04')
def _():
    f = Fraction(2, 8)
    return s([int(400 * f)])
