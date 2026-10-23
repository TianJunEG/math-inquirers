"""Independent checks for Level 3 Unit 9 (Measure and money masters): lengths, masses and volumes are changed to the smallest unit
(integers), money is counted in cents, and times are counted in minutes since midnight (24 hours = 1440 minutes)."""
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def only(xs):
    xs = list(xs)
    assert len(xs) == 1, xs
    return xs[0]


def dollars(c):
    return f'{c // 100}.{c % 100:02d}'


def mins(h, m, pm=None):
    if pm is True and h != 12:
        h += 12
    if pm is False and h == 12:
        h = 0
    return h * 60 + m


def clock12(total):
    total %= 1440
    h, m = divmod(total, 60)
    suffix = 'am' if h < 12 else 'pm'
    h12 = h % 12 or 12
    return f'{h12}:{m:02d} {suffix}'


def hhmm(total):
    h, m = divmod(total % 1440, 60)
    return f'{h:02d}:{m:02d}'


@check('L3U09-L01')
def _():
    ml = 2 * 1000 + 350 - 800
    return s([ml // 1000, ml % 1000])


@check('L3U09-S01')
def _():
    return {'a': s([3 * 100]), 'b': s([4 * 1000 + 50]), 'c': s([5 * 1000 + 300]), 'd': s(divmod(2750, 1000)), 'e': s(divmod(365, 100))}


@check('L3U09-S02')
def _():
    pencil = 11 - 3
    crayon = 13 - 6
    return {'a': s([pencil]), 'b': s([crayon]), 'c': s([pencil - crayon])}


@check('L3U09-S03')
def _():
    g = {'A': 1 * 1000 + 80, 'B': 1900, 'C': 1 * 1000 + 8, 'D': 1 * 1000 + 90}
    return sorted(g, key=g.get)


@check('L3U09-S04')
def _():
    total = 2 * 1000 + 500
    cups, left = 0, total
    while left >= 400:
        left -= 400
        cups += 1
    return {'a': s([cups]), 'b': s([left])}


@check('L3U09-S05')
def _():
    # the 3 jugs: scale marks every 50 ml; the water levels are read at mark numbers 7, 12 and 17
    marks = {'A': 7, 'B': 12, 'C': 17}
    ml = {k: 50 * v for k, v in marks.items()}
    return {'a': s([ml['A']]), 'b': s([ml['B']]), 'c': s([ml['C']]), 'd': s([ml['C'] - ml['A']])}


@check('L3U09-S06')
def _():
    cost = 265 + 140
    return {'a': [dollars(cost)], 'b': [dollars(500 - cost)]}


@check('L3U09-S07')
def _():
    book, puzzle, bottle, stickers = 620, 485, 340, 175
    three = book + puzzle + bottle
    return {'a': [dollars(three)], 'b': [dollars(2000 - three)], 'c': ['Yes' if three + stickers <= 2000 else 'No']}


@check('L3U09-S08')
def _():
    total = 2 * 1000 + 250
    books = total - 450
    return s([only(g for g in range(1, 2000) if 6 * g == books)])


@check('L3U09-S09')
def _():
    def to24(h, m, pm):
        return hhmm(mins(h, m, pm))
    def to12(hh, mm):
        t = clock12(hh * 60 + mm)
        return t.rsplit(' ', 1)[0]
    return {'a': [to24(6, 15, False)], 'b': [to24(1, 40, True)], 'c': [to24(9, 5, True)], 'd': [to12(16, 50)], 'e': [to12(20, 25)]}


@check('L3U09-S10')
def _():
    lasts = mins(6, 40, True) - mins(5, 25, True)
    ends = mins(3, 40, True) + 55
    starts = mins(8, 15, True) - (60 + 45)
    return {'a': s(divmod(lasts, 60)), 'b': [clock12(ends)], 'c': [clock12(starts)]}


@check('L3U09-S11')
def _():
    # clock faces: the long hand at number n means 5 n minutes; the short hand gives the hour (read from the drawing)
    def read(hour, long_hand_number):
        return f'{hour}:{5 * long_hand_number:02d}'
    return {'a': [read(4, 2)], 'b': [read(7, 9)], 'c': [read(11, 5)]}


@check('L3U09-T01')
def _():
    first, gap, ride, must = mins(6, 50), 20, 25, mins(8, 15)
    times = [first + gap * k for k in range(0, 10)]
    ok = [t for t in times if t + ride <= must]
    return [hhmm(max(ok))]


@check('L3U09-T02')
def _():
    start = mins(22, 50)
    arrive = mins(2, 10) + 1440
    return s(divmod(arrive - start, 60))


@check('L3U09-T03')
def _():
    sols = [(p, n) for p in range(1, 900) for n in [p + 150] if 2 * n + 3 * p == 900]
    p, n = only(sols)
    return {'a': [dollars(p)], 'b': [dollars(n)]}


@check('L3U09-G01')
def _():
    five, three = 5, 0
    # step 1: fill the 5 jug, pour into the 3 jug until it is full
    pour = min(five, 3 - three)
    five, three = five - pour, three + pour
    a = five
    # step 2: empty the 3 jug, pour the contents of the 5 jug into it, fill the 5 jug, pour until the 3 jug is full
    three = 0
    pour = min(five, 3 - three)
    five, three = five - pour, three + pour
    five = 5
    pour = min(five, 3 - three)
    five, three = five - pour, three + pour
    return {'a': s([a]), 'b': s([five])}


@check('L3U09-G02')
def _():
    slow = 8
    return {'a': [clock12(mins(4, 20, True) + slow)], 'b': [clock12(mins(4, 45, True) - slow)]}


@check('L3U09-G03')
def _():
    a, b = 640, 215
    ways = {dollars(a + b): 'sum', dollars(a - b): 'difference'}
    assert dollars(425) in ways and ways[dollars(425)] == 'difference'
    return [dollars(425)]


@check('L3U09-G04')
def _():
    start = (0 * 60 + 20) - (60 + 55)
    return [hhmm(start)]


@check('L3U09-C01')
def _():
    return s([2 * 100 + 40])


@check('L3U09-C02')
def _():
    return s([1 * 1000 + 200 - 700])


@check('L3U09-C03')
def _():
    return s(divmod(mins(8, 10, True) - mins(6, 45, True), 60))


@check('L3U09-C04')
def _():
    return [dollars(500 - 235)]
