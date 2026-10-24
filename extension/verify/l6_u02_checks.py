"""Independent checks for Level 6 Unit 2 (Prime hunters).  Factors are found by trial division, primes by testing every smaller number (no sieve), the printed code is run
by the l6_lib interpreter, and the tables printed in the book are read from the unit file."""
from common import load_unit
from l6_lib import run, s

CHECKS = {}
U = load_unit(6, 2)
ITEM = {i['id']: i for i in U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


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


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


@check('L6U02-L01')
def _():
    f = factors(143)
    return ['Yes' if len(f) == 2 else 'No', f[1], f[2]]


@check('L6U02-S01')
def _():
    f100 = factors(100)
    self_pair = [d for d in f100 if d * d == 100][0]
    return {'a': s(factors(42)), 'b': [len(f100)], 'c': [self_pair]}


@check('L6U02-S02')
def _():
    cells = [int(c) for row in ITEM['L6U02-S02']['figure']['rows'] for c in row]
    return s([c for c in cells if is_prime(c)])


@check('L6U02-S03')
def _():
    return {'a': s(prime_factors(84)), 'b': s(prime_factors(90))}


@check('L6U02-S04')
def _():
    prog = prog_of('L6U02-S04')
    env, said = run(prog)
    n = 20
    all_f = len(factors(n))
    # smallest number of repeats that counts every factor of n
    r = next(r for r in range(1, 100) if run([prog[0], prog[1], prog[2], ['ctl', f'repeat ({r})', prog[3][2]], prog[4]])[1][0] == all_f)
    return {'a': [said[0]], 'b': [r]}


@check('L6U02-S05')
def _():
    ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert all(is_prime(p) for p in ps) and ps == [n for n in range(1, 30) if is_prime(n)]
    return [f'{a} + {26 - a}' for a in ps if a <= 26 - a and is_prime(26 - a)]


@check('L6U02-S06')
def _():
    return {'a': ['Yes' if 372 % 4 == 0 else 'No'], 'b': ['Yes' if 2457 % 3 == 0 else 'No'], 'c': ['Yes' if 6835 % 9 == 0 else 'No']}


@check('L6U02-S07')
def _():
    small = [d for d in factors(119) if d > 1][0]
    return {'a': [113 % 2, 113 % 3, 113 % 5, 113 % 7], 'b': ['Yes' if is_prime(113) else 'No'], 'c': ['Yes' if is_prime(119) else 'No', small, 119 // small]}


@check('L6U02-S08')
def _():
    a = [n for n in range(41, 60) if is_prime(n) and sum(map(int, str(n))) == 8]
    b = [n for n in range(61, 80) if is_prime(n) and is_prime(n + 2)]
    assert len(a) == 1 and len(b) == 1
    return {'a': s(a), 'b': s(b)}


@check('L6U02-S09')
def _():
    odd = [n for n in (50, 64, 72) if len(factors(n)) % 2 == 1]
    assert len(odd) == 1
    return {'a': [len(factors(81))], 'b': [[d for d in factors(81) if d * d == 81][0]], 'c': s(odd)}


@check('L6U02-S10')
def _():
    env, said = run(prog_of('L6U02-S10'))
    return {'a': [said[0]], 'b': [len(said)], 'c': [said[-1]]}


@check('L6U02-S11')
def _():
    rows = [r for r in range(2, 37) if 36 % r == 0 and 36 // r >= 2]
    return {'a': s(rows), 'b': [len(rows)]}


def smallest_with(k):
    n = 1
    while len(factors(n)) != k:
        n += 1
    return n


@check('L6U02-T01')
def _():
    return {'a': [smallest_with(5)], 'b': [smallest_with(9)], 'c': [smallest_with(10)]}


@check('L6U02-T02')
def _():
    nums = [6 * p for p in range(6, 100) if is_prime(p) and 6 * p < 100]
    counts = {len(factors(n)) for n in nums}
    assert len(counts) == 1
    m11 = [n for n in nums if n % 11 == 0]
    return {'a': s(nums), 'b': s(counts), 'c': s(m11)}


@check('L6U02-T03')
def _():
    ps = [n for n in range(101, 120) if is_prime(n)]
    twins = [(a, b) for a in ps for b in ps if b - a == 2]
    m7 = [n for n in range(101, 120) if n % 2 == 1 and n % 7 == 0]
    return {'a': s(ps), 'b': [len(twins)], 'c': s(m7)}


@check('L6U02-G01')
def _():
    n12 = smallest_with(12)
    return {'a': [len(factors(72))], 'b': [len(factors(2 * 2 * 3 * 3 * 5))], 'c': [n12]}


@check('L6U02-G02')
def _():
    fig = ITEM['L6U02-G02']['figure']
    nums = [int(c) for row in fig['rows'] for c in row]
    assert nums == list(range(1, 61))
    alive = set(nums) - {1}
    for p in (2, 3, 5, 7):
        alive -= {m for m in nums if m % p == 0 and m != p}
    must = [p for p in range(2, 20) if is_prime(p) and p * p <= 60]      # primes whose multiples must be crossed out
    assert must == [2, 3, 5, 7]
    assert alive == {n for n in nums if is_prime(n)}
    ps = sorted(alive)
    return {'a': [len(ps)], 'b': [ps[9]]}


@check('L6U02-G03')
def _():
    prog = prog_of('L6U02-G03')
    out = {}
    for n in (221, 97):
        trace = []
        env, said = run(prog, env={'n': n}, trace=trace)
        out[n] = (said[0], len(trace))
    return {'a': [out[221][0]], 'b': [out[221][1]], 'c': [out[97][0]]}


@check('L6U02-C01')
def _():
    return s(factors(40))


@check('L6U02-C02')
def _():
    return ['Yes' if is_prime(147) else 'No']


@check('L6U02-C03')
def _():
    return s(prime_factors(140))


@check('L6U02-C04')
def _():
    return s([47 % 6, 100 % 8])
