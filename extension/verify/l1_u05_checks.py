"""Independent checks for Level 1 Unit 5 (Working backwards): every answer is found by forward simulation / brute force over start values,
never by undoing the steps (so a wrong 'undo' in the book cannot be repeated here)."""
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def find_start(steps, end, lo=0, hi=200):
    """The one start value in lo..hi that ends at `end` when the steps (functions) are run forwards; never goes below 0."""
    sols = []
    for x in range(lo, hi + 1):
        v, ok = x, True
        for f in steps:
            v = f(v)
            if v < 0:
                ok = False
                break
        if ok and v == end:
            sols.append(x)
    assert len(sols) == 1, sols
    return sols[0]


add = lambda k: (lambda v: v + k)
sub = lambda k: (lambda v: v - k)


@check('L1U05-L01')
def _():
    return s([find_start([add(6)], 15)])


@check('L1U05-S01')
def _():
    return s([find_start([add(5)], 13)])


@check('L1U05-S02')
def _():
    return {'a': s([find_start([add(8)], 13)]), 'b': s([find_start([add(7)], 15)]),
            'c': s([find_start([sub(5)], 9)]), 'd': s([find_start([sub(6)], 12)])}


@check('L1U05-S03')
def _():
    return s([find_start([sub(4)], 9)])


@check('L1U05-S04')
def _():
    return s([find_start([add(9)], 17)])


@check('L1U05-S05')
def _():
    return s([find_start([sub(3), add(8)], 14)])


@check('L1U05-S06')
def _():
    start = find_start([add(7), sub(3)], 15)
    return s([start + 7, start])   # middle box, start box


@check('L1U05-S07')
def _():
    # the machine: find the one rule k with IN 6 -> OUT 10, then run it forwards / search for the IN
    k = [k for k in range(0, 30) if 6 + k == 10][0]
    out9 = 9 + k
    in_for_17 = [x for x in range(0, 60) if x + k == 17][0]
    out15 = 15 + k
    return {'a': s([k]), 'b': s([out9, in_for_17, out15])}


@check('L1U05-S08')
def _():
    solve = lambda f, target: [x for x in range(0, 100) if f(x) == target]
    r = lambda f, t: s([solve(f, t)[0]])
    return {'a': r(lambda x: x + 6, 15), 'b': r(lambda x: x - 4, 9), 'c': r(lambda x: 18 - x, 11)}


@check('L1U05-S09')
def _():
    return s([find_start([sub(4), add(6)], 11)])


@check('L1U05-S10')
def _():
    # 6th place, 2 behind: count the places
    queue = list(range(1, 7)) + ['b1', 'b2']
    return s([len(queue)])


@check('L1U05-S11')
def _():
    queue = list(range(1, 13))   # places 1..12, Aisha is place 5
    return s([len([q for q in queue if q > 5])])


@check('L1U05-S12')
def _():
    siti = [x for x in range(0, 60) if x + 6 == 15][0]
    jenny = [x for x in range(0, 60) if x - 6 == 9][0]
    return {'a': s([siti]), 'b': s([jenny])}


@check('L1U05-S13')
def _():
    tf = lambda b: 'True' if b else 'False'
    return {'a': [tf(9 + 4 - 6 == 7)], 'b': [tf(12 - 5 + 3 == 9)], 'c': [tf(8 + 7 - 4 == 11)]}


@check('L1U05-S14')
def _():
    x = find_start([add(6)], 15)
    return {'a': ['Yes' if x == 21 else 'No'], 'b': s([x])}


@check('L1U05-T01')
def _():
    # Mei gives 5, gets 8, gives 4, ends with 13. Simulate forwards for each start.
    start = find_start([sub(5), add(8), sub(4)], 13)
    before_last = start - 5 + 8      # amount just before she gives 4 to Siti
    before_ben = start - 5           # amount just before Ben gives 8
    return {'a': s([before_last]), 'b': s([before_ben]), 'c': s([start])}


@check('L1U05-T02')
def _():
    steps = [add(9), sub(4)]
    run = lambda x: sub(4)(add(9)(x))
    k = {run(x) - x for x in range(0, 50)}
    assert len(k) == 1
    k = k.pop()
    return {'a': s([k]), 'b': s([run(11)]), 'c': s([find_start(steps, 30)])}


@check('L1U05-T03')
def _():
    # all queue lengths n where place 7 from the front is also place 4 from the back
    ns = [n for n in range(1, 60) if n - 7 + 1 == 4]
    assert len(ns) == 1
    n = ns[0]
    return {'a': s([7 - 1]), 'b': s([n - 7]), 'c': s([n])}


@check('L1U05-G01')
def _():
    dbl = lambda x: x + x
    b = [x for x in range(0, 60) if dbl(x) + 4 == 18]
    c = [x for x in range(0, 60) if dbl(x) - 5 == 11]
    assert len(b) == 1 and len(c) == 1
    return {'a': s([6 + 6]), 'b': s(b), 'c': s(c)}


@check('L1U05-G02')
def _():
    def run(start, ops):
        v = start
        for o, k in ops:
            v = v + k if o == '+' else v - k
            if v < 0:
                return None
        return v
    a = run(12, [('+', 6), ('-', 9)])
    b = run(12, [('-', 9), ('+', 6)])
    c = run(5, [('+', 6), ('-', 9)])
    d = run(5, [('-', 9), ('+', 6)])
    return {'a': s([a]), 'b': s([b]), 'c': s([c]), 'd': ['Yes' if d is not None else 'No']}


@check('L1U05-G03')
def _():
    pos, day = 0, 0
    while True:
        day += 1
        pos += 4
        if pos >= 12:
            return {'a': s([day])}
        pos -= 2


@check('L1U05-C01')
def _():
    return s([find_start([add(7)], 16)])


@check('L1U05-C02')
def _():
    return s([find_start([sub(5), add(9)], 17)])


@check('L1U05-C03')
def _():
    return s([find_start([sub(6)], 9)])


@check('L1U05-C04')
def _():
    return s([find_start([sub(7)], 8)])
