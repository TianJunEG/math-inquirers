"""Independent checks for Level 5 Unit 6 (Rate racers): rates are simulated minute by minute or solved with exact Fraction arithmetic;
money is kept in cents (integers) and printed with two decimals."""
import itertools
import math
from fractions import Fraction as Fr

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def money(cents):
    cents = Fr(cents)
    assert cents.denominator == 1, cents
    return f'{int(cents) // 100}.{int(cents) % 100:02d}'


def fmt(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{float(x):g}'


def minutes_until(target, start, step, limit=10000):
    """Simulate: add `step` each minute (list of changes by minute) until the amount reaches target."""
    amount, t = start, 0
    while amount < target and t < limit:
        t += 1
        amount += step
    return t


def half_hour_lots(minutes_after_first_hour):
    """Number of half hours or parts of a half hour."""
    lots, left = 0, minutes_after_first_hour
    while left > 0:
        lots += 1
        left -= 30
    return lots


@check('L5U06-L01')
def _():
    per = Fr(24, 4)
    return [fmt(per * 11)]


@check('L5U06-S01')
def _():
    per = Fr(18, 3)
    return [fmt(per), fmt(per * 5), fmt(per * 8)]


@check('L5U06-S02')
def _():
    one = Fr(420, 6)
    return {'a': [money(one)], 'b': [money(one * 9)]}


@check('L5U06-S03')
def _():
    per = Fr(36, 4)
    return {'a': [fmt(per)], 'b': [fmt(per * 25)], 'c': [fmt(Fr(270) / per)]}


@check('L5U06-S04')
def _():
    a, b = Fr(250, 5), Fr(360, 8)
    return {'a': [money(a)], 'b': [money(b)], 'c': ['Pack A' if a < b else 'Pack B']}


@check('L5U06-S05')
def _():
    x = (15 // 3) * 240
    y = (15 // 5) * 375
    return {'a': [money(x)], 'b': [money(y)], 'c': ['Shop X' if x < y else 'Shop Y']}


@check('L5U06-S06')
def _():
    return {'a': [str(14 + 6)], 'b': [str(minutes_until(200, 0, 14 + 6))]}


@check('L5U06-S07')
def _():
    return [str(minutes_until(300, 0, 25 - 10))]


@check('L5U06-S08')
def _():
    return [str(minutes_until(900, 0, 40 + 20))]


@check('L5U06-S09')
def _():
    minutes = 2 * 60 + 20
    return [money(200 + 80 * half_hour_lots(minutes - 60))]


@check('L5U06-S10')
def _():
    tank, t = 240, 0
    after9 = None
    while tank > 0:
        tank -= 15
        t += 1
        if t == 9:
            after9 = tank
    return {'a': [str(after9)], 'b': [str(t)]}


@check('L5U06-S11')
def _():
    per_min = 4 * (60 // 10)
    return {'a': [str(per_min)], 'b': [str(per_min * 60)], 'c': [fmt(Fr(per_min * 60, 1000))]}


@check('L5U06-S12')
def _():
    t = lambda v: 'True' if v else 'False'
    cans = Fr(360, 6) * 12 == 720            # 12 cans at 60 cents each = 720 cents
    # (b) a counter-example to 'a larger pack is always the better buy': 8 pencils for $4.40 (55c each) against 5 for $2.50 (50c each)
    larger_always_better = Fr(440, 8) < Fr(250, 5)
    return {'a': [t(cans)], 'b': [t(larger_always_better)], 'c': [t(5 + 7 == 12)]}


@check('L5U06-S13')
def _():
    for visits in range(1, 100):
        if 2000 + 400 * visits == 800 * visits:
            return [str(visits)]


@check('L5U06-S14')
def _():
    per_second = Fr(3, 2) / 20
    return [fmt(per_second * 5 * 60)]


@check('L5U06-T01')
def _():
    best = None
    for a, b, c in itertools.product(range(0, 8), repeat=3):
        if 5 * a + 8 * b + 12 * c == 32:
            cost = 300 * a + 470 * b + 690 * c
            best = cost if best is None else min(best, cost)
    return [money(best)]


@check('L5U06-T02')
def _():
    job = 12 * 20          # any common multiple works: pages
    rate = Fr(job, 12) + Fr(job, 20)
    return [fmt(Fr(job) / rate)]


@check('L5U06-T03')
def _():
    one_printer_one_minute = Fr(480, 4) / 6
    return [fmt(one_printer_one_minute * 6 * 5)]


@check('L5U06-G01')
def _():
    t1 = Fr(60, 6)
    t2 = Fr(60, 12)
    return [fmt(Fr(120) / (t1 + t2))]


@check('L5U06-G02')
def _():
    a, b, t = 90, 10, 0
    while a != b:
        a -= 5
        b += 3
        t += 1
        assert t < 1000
    return [str(t)]


@check('L5U06-G03')
def _():
    water, t = 0, 0
    while water < 200:
        t += 1
        water += 8 + (12 if t > 5 else 0)
    return [str(t)]


@check('L5U06-C01')
def _():
    return [fmt(Fr(54, 3) * 8)]


@check('L5U06-C02')
def _():
    a, b = Fr(400, 5), Fr(600, 8)
    return {'a': ['5 mangoes' if a < b else '8 mangoes'], 'b': [money(min(a, b))]}


@check('L5U06-C03')
def _():
    return [str(minutes_until(160, 0, 9 + 11 - 4))]


@check('L5U06-C04')
def _():
    minutes = 2 * 60 + 45
    return [money(150 + 60 * half_hour_lots(minutes - 60))]
