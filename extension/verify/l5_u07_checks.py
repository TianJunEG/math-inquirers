"""Independent checks for Level 5 Unit 7 (Percentage puzzles): exact Fraction arithmetic; discounts, GST and remainders are simulated step by step."""
from fractions import Fraction as Fr

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def m(x):
    """Money: whole dollars without cents, otherwise two decimals."""
    x = Fr(x)
    if x.denominator == 1:
        return str(x.numerator)
    cents = x * 100
    assert cents.denominator == 1, x
    return f'{float(x):.2f}'


def pc(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{float(x):g}'


def percent_of(p, amount):
    return Fr(p, 100) * amount


def as_percent(part, whole):
    return Fr(part, whole) * 100


@check('L5U07-L01')
def _():
    cost = Fr(75)
    cost -= percent_of(20, cost)
    cost += percent_of(9, cost)
    return [m(cost)]


@check('L5U07-S01')
def _():
    shaded = 38
    return {'a': [pc(as_percent(shaded, 100))], 'b': [pc(as_percent(100 - shaded, 100))]}


@check('L5U07-S02')
def _():
    return {'a': [m(percent_of(10, 340))], 'b': [m(percent_of(5, 340))], 'c': [m(percent_of(15, 340))]}


@check('L5U07-S03')
def _():
    return {'a': [pc(as_percent(18, 25))], 'b': [pc(as_percent(7, 20))]}


@check('L5U07-S04')
def _():
    disc = percent_of(15, 120)
    return {'a': [m(percent_of(10, 120))], 'b': [m(disc)], 'c': [m(120 - disc)]}


@check('L5U07-S05')
def _():
    gst = percent_of(9, 64)
    return {'a': [m(gst)], 'b': [m(64 + gst)]}


@check('L5U07-S06')
def _():
    money = Fr(150)
    money -= percent_of(20, money)
    money -= percent_of(40, money)
    return [m(money)]


@check('L5U07-S07')
def _():
    n = 40
    walk, cycle = percent_of(35, n), percent_of(25, n)
    return {'a': [m(walk)], 'b': [m(cycle)], 'c': [m(n - walk - cycle)]}


@check('L5U07-S08')
def _():
    q1, q2 = as_percent(21, 30), as_percent(34, 50)
    return {'a': [pc(q1)], 'b': [pc(q2)], 'c': ['Quiz 1' if q1 > q2 else 'Quiz 2']}


@check('L5U07-S09')
def _():
    p = 2 * (16 - percent_of(15, 16))        # 15% off each cap
    q = 16 + Fr(16, 2)                       # second cap at half price
    return {'a': [m(p)], 'b': [m(q)], 'c': ['Shop P' if p < q else 'Shop Q']}


@check('L5U07-S10')
def _():
    c = Fr(50)
    c += percent_of(20, c)
    up = c
    c -= percent_of(20, c)
    return {'a': [m(up)], 'b': [m(c)], 'c': ['Yes' if c == 50 else 'No']}


@check('L5U07-S11')
def _():
    return {'a': [pc(as_percent(2, 5))], 'b': [pc(as_percent(3, 4))]}


@check('L5U07-S12')
def _():
    t = lambda v: 'True' if v else 'False'
    a = percent_of(50, 80) == 40
    b = percent_of(10, 90) == 9
    cost = Fr(100)
    cost -= percent_of(20, cost)
    cost -= percent_of(10, cost)
    c = cost == 100 - percent_of(30, 100)
    return {'a': [t(a)], 'b': [t(b)], 'c': [t(c)]}


@check('L5U07-S13')
def _():
    money = Fr(240)
    money -= percent_of(30, money)
    money -= percent_of(25, money)
    return [m(money)]


@check('L5U07-S14')
def _():
    sofa = Fr(250)
    sofa += percent_of(9, sofa)
    return [m(sofa + 20)]


@check('L5U07-T01')
def _():
    c = Fr(200)
    c -= percent_of(10, c)
    c -= percent_of(20, c)
    return {'a': [m(c)], 'b': [pc(as_percent(200 - c, 200))]}


@check('L5U07-T02')
def _():
    # search the old cost (in cents) whose 20% discount gives $60
    for cents in range(1, 100000):
        old = Fr(cents, 100)
        if old - percent_of(25, old) == 60:
            return [m(old)]


@check('L5U07-T03')
def _():
    for cents in range(1, 100000):
        before = Fr(cents, 100)
        if before + percent_of(8, before) == 432:
            return [m(percent_of(8, before))]


@check('L5U07-G01')
def _():
    return {'a': [pc(as_percent(75 - 60, 60))], 'b': [pc(as_percent(75 - 60, 75))]}


@check('L5U07-G02')
def _():
    girls = percent_of(60, 50)
    boys = 50 - girls
    badges = percent_of(30, girls) + percent_of(20, boys)
    return [pc(as_percent(badges, 50))]


@check('L5U07-G03')
def _():
    blue, red = percent_of(60, 50), 50 - percent_of(60, 50)
    for added in range(0, 1000):
        if Fr(blue + added, 50 + added) == Fr(80, 100):
            return [str(added)]


@check('L5U07-C01')
def _():
    return {'a': [m(percent_of(10, 180))], 'b': [m(percent_of(5, 180))], 'c': [m(percent_of(15, 180))]}


@check('L5U07-C02')
def _():
    c = Fr(40)
    c -= percent_of(25, c)
    c += percent_of(9, c)
    return [m(c)]


@check('L5U07-C03')
def _():
    money = Fr(80)
    money -= percent_of(25, money)
    money -= percent_of(50, money)
    return [m(money)]


@check('L5U07-C04')
def _():
    return ['Test 1' if as_percent(33, 50) > as_percent(16, 25) else 'Test 2']
