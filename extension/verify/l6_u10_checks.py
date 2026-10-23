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
    d = -6
    for _ in range(15):
        d += 1
    for _ in range(20):
        d -= 1
    return {'a': [d], 'b': [steps(-6, 21)]}


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
    fourth = [x for x in range(0, 100) if mean([11, 19, 14, x]) == 15][0]
    ys = sorted([15, 4, 9, 12])
    return {'a': [fourth], 'b': [(ys[1] + ys[2]) / 2]}


@check('L6U10-S10')
def _():
    prog = prog_of('L6U10-S10')
    tr = []
    env, said = run(prog, trace=tr)
    first = [i + 1 for i, e in enumerate(tr) if e['score'] == 50][0]
    return {'a': [tr[5]['score']], 'b': [first], 'c': [said[0]]}


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
    pairs = [(2, 7), (5, 16)]
    rules = [(a, b) for a in range(0, 20) for b in range(-20, 20) if all(a * n + b == v for n, v in pairs)]
    assert len(rules) == 1
    a, b = rules[0]
    rate = [m for m in range(0, 20) if (16 - 7) == m * (5 - 2)][0]
    ride = [n for n in range(0, 100) if a * n + b == 49][0]
    prog = prog_of('L6U10-G01')
    assert any('?' in blk[1] for blk in prog)            # the printed code has the rule blanked out
    assert rate == a
    return {'a': [a, b], 'b': [a * 20 + b], 'c': [ride]}


@check('L6U10-G02')
def _():
    prog = prog_of('L6U10-G02')
    spins = range(1, 9)
    mult3 = len([n for n in spins if n % 3 == 0])
    evens = len([n for n in spins if n % 2 == 0])
    rep = [b for b in prog if b[1].startswith('repeat')][0][1]
    times = int(rep.split('(')[1].rstrip(')'))
    return {'a': [mult3], 'b': [round(times * Fraction(mult3, 8))], 'c': [round(times * Fraction(evens, 8))]}


@check('L6U10-G03')
def _():
    prog = prog_of('L6U10-G03')
    out = {}
    for n0 in (6, 7):
        env, said = run(prog, env={'n': n0})
        out[n0] = said[0]
    n, top = 7, 7
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        top = max(top, n)
    return {'a': [out[6]], 'b': [out[7]], 'c': [top]}


@check('L6U10-C01')
def _():
    a, b = fit_rule([(1, 4), (2, 11), (3, 18), (4, 25)])
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
    f = Fraction(7, 15)
    return s([f.numerator, f.denominator])


@check('L6U10-C04')
def _():
    return s([clock(3, 100)])
