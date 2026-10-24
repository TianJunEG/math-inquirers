"""Independent checks for Level 1 Unit 1 (Number patterns). Every function recomputes the answer from the question
data (simulation or brute force), never by copying the answer from the JSON. Return a value list, or a dict {part: value list}."""
from common import arith, s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


@check('L1U01-L01')
def _():
    return s(arith(3, 5, 5)[1:])


@check('L1U01-S01')
def _():
    q = arith(8, 2, 6); assert q[1] == 10 and q[5] == 18
    return s([q[2], q[4]])


@check('L1U01-S02')
def _():
    q = arith(15, 5, 6); assert q[1] == 20 and q[5] == 40
    return s([q[2], q[4]])


@check('L1U01-S03')
def _():
    q = arith(7, 10, 6); assert q[5] == 57
    return s([q[3], q[4]])


@check('L1U01-S04')
def _():
    seq = [5, 9, 13, 17]
    step = seq[1] - seq[0]; assert all(seq[i + 1] - seq[i] == step for i in range(3))
    return {'a': s(arith(5, step, 6)[4:]), 'b': s([step])}


@check('L1U01-S05')
def _():
    seq = [21, 18, 15, 12]
    step = seq[0] - seq[1]; assert all(seq[i] - seq[i + 1] == step for i in range(3))
    return {'a': s(arith(21, -step, 6)[4:]), 'b': s([step])}


@check('L1U01-S06')
def _():
    seq = [7, 11, 15, 19]
    diffs = {seq[i + 1] - seq[i] for i in range(3)}
    assert len(diffs) == 1
    d = diffs.pop()
    options = {3: 'add 3', 4: 'add 4', 5: 'add 5'}
    return [options[d]]


@check('L1U01-S07')
def _():
    seq = [30, 26, 22, 18]
    down = all(seq[i + 1] < seq[i] for i in range(3))
    step = seq[0] - seq[1]
    return {'a': ['Down' if down else 'Up'], 'b': s([step]), 'c': s([seq[-1] - step])}


@check('L1U01-S08')
def _():
    q = arith(3, 3, 6)
    return {'a': s([q[4]]), 'b': s([q[5]])}


@check('L1U01-S09')
def _():
    q = arith(1, 2, 4)
    return {'a': s([q[3]]), 'b': s([q[1] - q[0]])}


@check('L1U01-S10')
def _():
    seq = [9, 12, 15, 17, 21, 24]
    step = seq[1] - seq[0]
    bad = [i for i, v in enumerate(seq) if v != seq[0] + step * i]
    assert bad == [3] and seq[3] == 17
    return s([seq[0] + step * bad[0]])


@check('L1U01-S11')
def _():
    q = arith(30, -2, 6); assert q[5] == 20
    return s([q[2], q[4]])


@check('L1U01-S12')
def _():
    amounts = {}
    for day in range(1, 6):
        amounts[day] = 5 * day
    return s([amounts[5]])   # Mon..Fri = days 1..5


@check('L1U01-S13')
def _():
    return s([v for v in arith(3, 4, 20) if v <= 31])


@check('L1U01-S14')
def _():
    return s(arith(20, -5, 5)[1:])


@check('L1U01-T01')
def _():
    lands = [v for v in arith(2, 5, 20) if v <= 60]
    return {'a': ['Yes' if 37 in lands else 'No'], 'b': ['Yes' if 40 in lands else 'No']}


@check('L1U01-T02')
def _():
    ali = [v for v in arith(4, 4, 30) if v <= 50]
    mei = [v for v in arith(10, 10, 10) if v <= 50]
    both = [v for v in ali if v in mei]
    gaps = {both[i + 1] - both[i] for i in range(len(both) - 1)}
    assert len(gaps) == 1
    return {'a': s(both), 'b': s(gaps)}


@check('L1U01-T03')
def _():
    sols = []
    for first in range(0, 30):
        for step in range(1, 30):
            q = arith(first, step, 5)
            if q[1] == 10 and q[4] == 25:
                sols.append((first, step))
    assert len(sols) == 1
    first, step = sols[0]
    return {'a': s([4 - 1]), 'b': s([step]), 'c': s([first])}


@check('L1U01-G01')
def _():
    def dots(n):   # count the dots of triangle n row by row (row r has r dots)
        total = 0
        for r in range(1, n + 1):
            total += r
        return total
    assert [dots(1), dots(2), dots(3)] == [1, 3, 6]
    return {'a': s([dots(4)]), 'b': s([dots(5)]), 'c': s([dots(7)])}


@check('L1U01-G02')
def _():
    mei = [v for v in arith(1, 3, 40) if v <= 40]
    ali = [v for v in arith(2, 5, 40) if v <= 40]
    return s(sorted(set(mei) & set(ali)))


@check('L1U01-G03')
def _():
    return s([j for j in range(1, 40) if 20 in [v for v in arith(2, j, 30) if v <= 20]])


@check('L1U01-C01')
def _():
    return s(arith(14, 4, 6)[4:])


@check('L1U01-C02')
def _():
    q = arith(40, -5, 6)
    return s([q[4], q[5], 5])


@check('L1U01-C03')
def _():
    return ['Yes' if 30 in arith(6, 4, 20) else 'No']


@check('L1U01-C04')
def _():
    seq = [11, 16, 21, 27, 31, 36]
    step = seq[1] - seq[0]
    bad = [i for i, v in enumerate(seq) if v != seq[0] + step * i]
    assert len(bad) == 1
    return s([seq[0] + step * bad[0]])
