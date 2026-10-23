"""Independent checks for Level 5 Unit 3 (Before and after): every answer is found by searching over whole-number situations."""
from fractions import Fraction as Fr

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def fs(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'


@check('L5U03-L01')
def _():
    # Kumar 60, Wei 30 is the example; the Try has Jason 70, Amelia 50: search the number of stickers given
    for g in range(0, 71):
        j, a = 70 - g, 50 + g
        if Fr(j) == Fr(3, 5) * a:
            return [str(g)]


@check('L5U03-S01')
def _():
    m = 80
    book = m * Fr(1, 4)
    rest = m - book
    pen = rest * Fr(1, 3)
    return {'a': [fs(book)], 'b': [fs(pen)], 'c': [fs(rest - pen)]}


@check('L5U03-S02')
def _():
    lily, ravi = 22 - 5, 14 + 5
    return {'a': [str(lily)], 'b': [str(ravi)], 'c': [str(lily + ravi)]}


@check('L5U03-S03')
def _():
    ben, aunt = 12 + 6, 41 + 6
    return {'a': [str(ben), str(aunt)], 'b': [str(41 - 12), str(aunt - ben)]}


@check('L5U03-S04')
def _():
    for g in range(0, 39):
        if 38 - g == 24 + g:
            return [str(g)]


@check('L5U03-S05')
def _():
    wear = Fr(5, 12) * 48
    return [fs(48 - wear - wear)]


@check('L5U03-S06')
def _():
    green, yellow = 15, 9
    yellow2 = yellow + 6
    changed = 'yellow' if yellow2 != yellow else 'green'
    unchanged = 'green' if changed == 'yellow' else 'yellow'
    return {'a': [unchanged], 'b': [fs(Fr(green, green + yellow))], 'c': [fs(Fr(green, green + yellow2))]}


@check('L5U03-S07')
def _():
    for money in range(5, 500, 5):
        if money - Fr(2, 5) * money == 45:
            return {'a': [fs(Fr(money, 5))], 'b': [str(money)]}


@check('L5U03-S08')
def _():
    for pen in range(1, 100):
        book = 3 * pen          # the pen costs 1/3 as much as the book
        if pen + book == 28:
            return {'a': [str(book)], 'b': [str(pen)]}


@check('L5U03-S09')
def _():
    for siti in range(1, 100):
        mei = Fr(3, 4) * siti
        if mei.denominator == 1 and siti + mei == 56:
            return {'a': [str(siti)], 'b': [fs(mei)]}


@check('L5U03-S10')
def _():
    return {'a': ['the total'], 'b': ['the difference'], 'c': ['the blue beads']}


@check('L5U03-S11')
def _():
    ravi, ben = 45 + 15, 21 + 15
    return {'a': [str(ravi)], 'b': [str(ben)], 'c': [str(ravi - ben)]}


@check('L5U03-S12')
def _():
    for m in range(12, 1000, 12):
        left = m - m / 4
        left -= left / 3
        if left == 30:
            return [str(m)]


@check('L5U03-S13')
def _():
    for full in range(1, 5000):
        if Fr(5, 6) * full - 250 == Fr(1, 2) * full:
            return [str(full)]


@check('L5U03-S14')
def _():
    # (a) total after a gift between two children, (b) difference after equal gifts, (c) 1/2 as many <=> 2 times as many
    a = (22 - 5) + (14 + 5) != 22 + 14
    b = (45 + 5) - (21 + 5) == 45 - 21
    mei, ali = 7, 14
    c = (Fr(mei) == Fr(1, 2) * ali) == (ali == 2 * mei)
    t = lambda v: 'True' if v else 'False'
    return {'a': [t(a)], 'b': [t(b)], 'c': [t(c)]}


@check('L5U03-T01')
def _():
    for m in range(15, 1000, 15):
        mon = Fr(2, 5) * m
        tue = Fr(1, 3) * (m - mon)
        if mon + tue == 90:
            return [str(m)]


@check('L5U03-T02')
def _():
    for siti in range(1, 120):
        mei = 120 - siti
        s2, m2 = siti - 10, mei + 10
        if Fr(s2) == Fr(3, 5) * m2:
            return [str(siti)]


@check('L5U03-T03')
def _():
    for y in range(1, 100):
        if Fr(10 + y) == Fr(1, 3) * (38 + y):
            return [str(y)]


@check('L5U03-G01')
def _():
    for cara in range(1, 100):
        ben = cara + 10
        ali = 2 * ben
        if cara + ben + ali == 150:
            return {'a': [str(cara)], 'b': [str(ben)], 'c': [str(ali)]}


@check('L5U03-G02')
def _():
    for total in range(10, 1000):
        children = Fr(2, 5) * total
        adults = total - children
        if children.denominator != 1:
            continue
        # 15 adults leave and 15 children come in
        if children + 15 == Fr(1, 2) * total and adults - 15 == Fr(1, 2) * total:
            return [str(total)]


@check('L5U03-G03')
def _():
    for total in range(7, 2000, 7):
        red = Fr(2, 7) * total
        if red >= 24 and Fr(red - 24) == Fr(1, 6) * (total - 24):
            return [str(total)]


@check('L5U03-G04')
def _():
    for ali in range(3, 120, 3):
        ben = 120 - ali
        a2, b2 = ali - ali // 3, ben + ali // 3
        if b2 == 3 * a2:
            return [str(ali)]


@check('L5U03-C01')
def _():
    for m in range(10, 1000, 10):
        left = m - m / 5
        left -= left / 2
        if left == 24:
            return [str(m)]


@check('L5U03-C02')
def _():
    for g in range(0, 47):
        if 46 - g == 30 + g:
            return [str(g)]


@check('L5U03-C03')
def _():
    for gift in range(0, 300):
        if Fr(30 + gift) == Fr(3, 4) * (50 + gift):
            return [str(gift)]


@check('L5U03-C04')
def _():
    blue, yellow = 18, 12 + 20
    return {'a': ['blue'], 'b': [fs(Fr(blue, blue + yellow))]}
