"""Independent checks for Level 6 Unit 10 (Showcase challenge).  Mixed items: every answer is recomputed with the same kind of brute force as in the unit it
comes from (stepping, listing, trial division), and the printed programs are run by the l6_lib interpreter."""
import itertools
from fractions import Fraction
from common import load_unit
from l6_lib import run, s, fit_rule

CHECKS = {}
U = load_unit(6, 10)
ITEM = {i['id']: i for i in U['items']}
ALPHA = [chr(65 + k) for k in range(26)]
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


def factors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def is_prime(n):
    return n > 1 and len(factors(n)) == 2


def prime_factors(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    return out


def steps(a, b):
    n, x = 0, a
    while x != b:
        x += 1 if b > a else -1
        n += 1
    return n


def clock(h, k, size=12, first=1):
    for _ in range(abs(k)):
        h += 1 if k > 0 else -1
        if h > first + size - 1:
            h = first
        if h < first:
            h = first + size - 1
    return h


def step_letter(ch, k):
    i = ALPHA.index(ch)
    for _ in range(abs(k)):
        i += 1 if k > 0 else -1
        if i == 26:
            i = 0
        if i == -1:
            i = 25
    return ALPHA[i]


def ask_hook(value):
    return {r'ask \(': lambda t, env, kids: env.__setitem__('answer', value)}


def mean(xs):
    t = Fraction(0)
    for x in xs:
        t += Fraction(x)
    return t / len(xs)


@check('L6U10-L01')
def _():
    prog = U['learn']['example']['figure']['prog']
    env, said = run(prog, env={'days': DAYS}, hooks=ask_hook(19))
    return [said[0]]


@check('L6U10-S01')
def _():
    seq = [10 + 7 * k for k in range(0, 60)]
    a, b = fit_rule([(k + 1, v) for k, v in enumerate(seq[:5])])
    return {'a': [a, b], 'b': [seq[49]], 'c': [seq.index(164) + 1]}


@check('L6U10-S02')
def _():
    return {'a': s([n for n in range(91, 110) if is_prime(n)]), 'b': s(prime_factors(330))}


@check('L6U10-S03')
def _():
    d = -18
    for _ in range(7):
        d += 1
    for _ in range(12):
        d -= 1
    return {'a': [d], 'b': [steps(-6, 9)]}


@check('L6U10-S04')
def _():
    return {'a': [[n for n in range(0, 200) if n * 5 - 7 == 43][0]], 'b': [[n for n in range(0, 200) if 6 * n + 1 == 79][0]]}


@check('L6U10-S05')
def _():
    return {'a': [len(list(itertools.product(range(3), range(5), range(2))))], 'b': [len(list(itertools.combinations(range(9), 2)))],
            'c': [len(list(itertools.permutations([2, 4, 6, 8], 3)))]}


@check('L6U10-S06')
def _():
    bag = ['R'] * 5 + ['B'] * 3
    p = Fraction(len([c for c in bag if c == 'R']), len(bag))
    ali = len([d for d in range(1, 7) if d % 2 == 0])
    ben = len([d for d in (1, 3, 5)])
    return {'a': [p.numerator, p.denominator], 'b': [int(1200 * Fraction(1, 6))], 'c': ['Yes' if ali == ben else 'No']}


@check('L6U10-S07')
def _():
    n = [n for n in range(3, 400) if n * 4 == 360][0]
    return {'a': [n], 'b': [180 - 4]}


@check('L6U10-S08')
def _():
    return {'a': [clock(4, 75)], 'b': [''.join(step_letter(c, 9) for c in 'MATH')]}


@check('L6U10-S09')
def _():
    fifth = [x for x in range(0, 100) if mean([10, 12, 18, 20, x]) == 14][0]
    ys = sorted([3, 11, 7, 9])
    return {'a': [fifth], 'b': [int((ys[1] + ys[2]) / 2)]}


@check('L6U10-S10')
def _():
    prog = prog_of('L6U10-S10')
    out = {n: run(prog[1:], env={'n': n})[1][0] for n in range(1, 21)}
    secret = [n for n, v in out.items() if v == 31][0]
    return {'a': [secret], 'b': [min(out.values())], 'c': [max(out.values())]}


@check('L6U10-S11')
def _():
    must_before = [('D', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'E')]       # idea, hand maths, blocks, test, twist
    good = [p for p in itertools.permutations('ABCDE') if all(p.index(x) < p.index(y) for x, y in must_before)]
    assert len(good) == 1
    return list(good[0])


@check('L6U10-S12')
def _():
    env, said = run([['var', 'set n to (11)'], ['ctl', 'repeat (25)', [['var', 'change n by (6)']]], ['look', 'say (n)']])
    seq = [11 + 6 * k for k in range(0, 60)]
    a, b = fit_rule([(k + 1, v) for k, v in enumerate(seq[:5])])
    return {'a': [said[0]], 'b': [seq.index(said[0]) + 1], 'c': [a, b]}


@check('L6U10-S13')
def _():
    two = list(itertools.product(range(1, 7), repeat=2))
    twelve = len([1 for a, b in two if a * b == 12])
    odd = Fraction(len([1 for a, b in two if (a * b) % 2 == 1]), 36)
    return {'a': [twelve], 'b': [odd.numerator, odd.denominator], 'c': [int(360 * odd)]}


@check('L6U10-S14')
def _():
    env, said = run([['var', 'set x to (15)'], ['ctl', 'repeat (7)', [['var', 'change x by (-4)']]]])
    first = None
    x = 15
    for k in range(1, 8):
        x -= 4
        if x < 0 and first is None:
            first = k
    return {'a': [env['x']], 'b': [first]}


@check('L6U10-T01')
def _():
    terms = [6 * n - 1 for n in range(1, 11)]
    notprime = [t for t in terms if not is_prime(t)]
    return {'a': [len([t for t in terms if is_prime(t)])], 'b': s(notprime), 'c': ['Yes' if all(t % 2 == 1 for t in terms) else 'No']}


@check('L6U10-T02')
def _():
    five = 5 * 74
    six = 6 * 76
    return {'a': [five], 'b': [six], 'c': [six - five]}


@check('L6U10-T03')
def _():
    nums = [10 * a + b for a in range(1, 10) for b in range(0, 10) if a + b == 10]
    primes = [n for n in nums if is_prime(n)]
    both = [n for n in primes if is_prime(int(str(n)[::-1]))]
    return {'a': s(primes), 'b': s(both)}


@check('L6U10-G01')
def _():
    out = {n: n * 5 - 2 for n in range(1, 21)}
    a, b = fit_rule([(1, out[1]), (2, out[2])])
    secret = [n for n, v in out.items() if v == 48][0]
    return {'a': [a, -b], 'b': [min(out.values()), max(out.values())], 'c': [secret]}


@check('L6U10-G02')
def _():
    two = list(itertools.product(range(1, 7), repeat=2))
    ways = len([1 for a, b in two if a + b == 11])
    return {'a': [1000], 'b': [ways], 'c': [round(1000 * Fraction(ways, 36))]}


@check('L6U10-G03')
def _():
    prog = prog_of('L6U10-G03')
    t53, t49 = [], []
    env53, said53 = run(prog, env={'n': 53}, trace=t53)
    env49, said49 = run(prog, env={'n': 49}, trace=t49)
    return {'a': [len(t53)], 'b': [said49[0]], 'c': [said53[0]]}


@check('L6U10-C01')
def _():
    a, b = fit_rule([(1, 3), (2, 8), (3, 13), (4, 18)])
    return s([a, -b])


@check('L6U10-C02')
def _():
    x = -7
    for _ in range(12):
        x += 1
    for _ in range(9):
        x -= 1
    return s([x])


@check('L6U10-C03')
def _():
    f = Fraction(4, 10)
    return s([f.numerator, f.denominator])


@check('L6U10-C04')
def _():
    return s([clock(3, 100)])
