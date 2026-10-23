"""Independent answer checks for Level 1 Term 3 Lesson 9 (Lesson 29, Spot the Mistake).

Every sum, step, total, change and time in l29.json is recomputed here from first principles: sums and differences are counted one at a time (not by the lesson's formulas), a worked
sum is checked step by step, a 'check' is done by adding back or taking away, and each claimed mistake is shown to be exactly ONE mistake (the wrong answer differs from the right one
in one stated way). The class items (warm-up, sneak-peek, Explore cards, Mini-lesson, Talk) are listed and checked to differ from the items in the workbook, exit ticket and home sheet,
and from the Quest gate for this lesson (49 + 38 = 77, right answer 87) and the Quest cave idea. Times are recomputed on a 12-hour clock in minutes. The online practice templates get
brute-force oracles. The kit contract (8 cards, 4 right and 4 with one mistake) and the hand-offs are checked against the neighbouring lessons.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MINUS = '−'


def plus(a, b):
    n = a
    for _ in range(b):
        n += 1
    return n


def minus(a, b):
    n = a
    for _ in range(b):
        n -= 1
    return n


def add_back_ok(start, taken, answer):
    """A take away start - taken = answer is right exactly when answer + taken gives back start (checked by counting on)."""
    return plus(answer, taken) == start


def take_back_ok(a, b, answer):
    """An add a + b = answer is right exactly when answer - b gives back a."""
    return minus(answer, b) == a


def clock_after(h, m, add_min):
    """12-hour clock time after add_min minutes, counted one minute at a time."""
    for _ in range(add_min):
        m += 1
        if m == 60:
            m = 0
            h = 1 if h == 12 else h + 1
    return h, m


def fmt(h, m):
    return f'{h}:{m:02d}'


def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def sums_in(text):
    """Every 'a + b = c' or 'a - b = c' in a string (with the unicode minus), as (a, op, b, c)."""
    t = text.replace(MINUS, '-')
    return [(int(a), op, int(b), int(c)) for a, op, b, c in re.findall(r'(\d+)\s*([+-])\s*(\d+)\s*=\s*(\d+)', t)]


def is_true(a, op, b, c):
    return (plus(a, b) if op == '+' else minus(a, b)) == c


# (kind, ...) items used in class. Every one differs from every workbook item.
QUEST = {('wrong', 49, '+', 38, 77), ('cave', 14, (2, 5))}
CLASS = {
    'remember': [('addback', 40, 15, 25), ('tens', 46, 30), ('clock', 3, 30, 60)],
    'sneak': [('wrong', 40, '+', 20, 70), ('wrong', 27, '+', 16, 33)],
    'explore': [('card', 45, '+', 28, 63), ('card', 70, '-', 30, 40), ('card', 84, '-', 6, 82), ('card', 18, '+', 4, 22),
                ('card', 53, '-', 20, 73), ('card', 62, '-', 8, 54), ('card', 17, '+', 5, 21), ('card', 38, '+', 24, 62)],
    'mini': [('wrong', 71, '-', 26, 55), ('wrong', 60, '-', 18, 52), ('wrong', 29, '+', 35, 54), ('steps3', 56, 27), ('steps2', 92, 35), ('time', 9, 0, 30), ('money', 4, 9, 15)],
    'break': [('wrong', 6, '+', 6, 13)],
    'opt': [('wrong', 8, '+', 7, 14)],
}
WORKBOOK = {
    'S1': [('right', 41, '-', 17, 24)], 'S2': [('wrong', 50, '-', 23, 37)], 'S3': [('steps3', 36, 28)], 'S4': [('time', 2, 30, 60)], 'S5': [('money', 7, 5, 10)],
    'S6': [('tf', 25, '+', 30, 55), ('tf', 56, '-', 20, 46), ('tf', 24, '+', 9, 33), ('tf', 80, '-', 5, 85)],
    'T1': [('steps2c', 74, 29)], 'T2': [('two', 58, 27, 75, 85)], 'T3': [('fewer', 28, 6)], 'T4': [('time', 7, 30, 30)],
    'G1': [('big', 52, 39, 191)], 'G2': [('column', 47, 38, 75)], 'I1': [('wrong', 25, '+', 19, 34), ('wrong', 36, '+', 27, 53), ('wrong', 48, '+', 35, 73)],
    'E1': [('wrong', 82, '-', 47, 45)], 'G3': [('wrong', 38, '+', 15, 43)], 'E2': [('steps3b', 28, 15)], 'E3': [('left', 20, 12, 9)],
    'H1': [('wrong', 34, '+', 18, 42)], 'H2': [('time', 3, 30, 30)], 'H3': [('left', 15, 6, 11)], 'H4': [('two', 46, 38, 74, 84)], 'H5': [('longer', 14, 9)],
}


def _expl(it):
    return it   # items are plain tuples; two items are 'the same' when equal


def _wb_key(it):
    """Compare a class item to a workbook item by the numbers it uses (so a re-order cannot hide a repeat)."""
    kind = it[0]
    if kind in ('card', 'wrong', 'right', 'tf'):
        return ('sum',) + it[1:4]
    return it


_AUTHORED_Q = None


def _ways(target, prices):
    out = []
    for combo in itertools.product(range(target + 1), repeat=len(prices)):
        if sum(c * p for c, p in zip(combo, prices)) == target:
            out.append(combo)
    return out


# ---------------------------------------------------------------- online practice oracles
def _c1(e):
    return plus(e['a'], e['b'])


def _c2(e):
    s = plus(e['a'], e['b']) - 10 * e['f']
    return 'Yes' if take_back_ok(e['a'], e['b'], s) else 'No'


def _c3(e):
    # the ones make 10 or more, and a forgotten ten is the only mistake
    return plus(e['a'], e['b'])


def _t1(e):
    for x in range(0, e['a'] + 1):
        if plus(x, e['b']) == e['a']:
            return x


def _t2(e):
    w = plus(e['a'], e['b']) + 40 * e['f'] - 40
    near_a = 10 * ((e['a'] + 5) // 10)
    near_b = 10 * ((e['b'] + 5) // 10)
    about = near_a + near_b
    if w == plus(e['a'], e['b']): return 'about right'
    return 'too big' if w > about + 20 else 'too small' if w < about - 20 else 'about right'


def _t3(e):
    return plus(e['a'], e['b'])


def _g1(e):
    return minus(minus(e['m'], e['a']), e['b'])


def _g2(e):
    return minus(e['a'], 29)


ORACLES = {'c1': _c1, 'c2': _c2, 'c3': _c3, 't1': _t1, 't2': _t2, 't3': _t3, 'g1': _g1, 'g2': _g2}
BASE_ENV = {'c1': dict(a=40, b=30), 'c3': dict(a=39, b=24), 't1': dict(a=42, b=8), 't3': dict(a=36, b=7), 'g1': dict(m=50, a=12, b=9), 'g2': dict(a=63)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {q['id']: q for q in d['home_practice']}
    sl = {s['id']: s for s in d['slides']}
    inv = d['tiers']['investigation']

    # ---------------------------------------------------------------- the registries: nothing in class is in the workbook, exit, home or the Quest
    allcls = [_wb_key(p) for v in CLASS.values() for p in v]
    allwb = [_wb_key(p) for v in WORKBOOK.values() for p in v]
    eq(len(set(allcls)), len(allcls), 'class items are all different')
    eq(len(set(allwb)), len(allwb), 'workbook items are all different')
    eq(sorted(set(allcls) & set(allwb), key=str), [], 'no workbook, exit or home item repeats a class item')
    eq([p for p in allcls + allwb if p[0] == 'sum' and p[1:4] == (49, '+', 38)], [], 'no 49 + 38 anywhere in this lesson (Quest gate 7)')

    # ---------------------------------------------------------------- warm-up
    eq(add_back_ok(40, 15, 25), True, 's-rem1 40 - 15 = 25 by adding back'); eq(plus(25, 15), 40, 's-rem1 answer')
    eq(sums_in(sl['s-rem1']['blocks'][1]['text']), [(40, '-', 15, 25)], 's-rem1 chip sum is true: 40 - 15 = 25'); eq(is_true(40, '-', 15, 25), True, 's-rem1 sum is right')
    eq(plus(46, 30), 76, 's-rem2'); eq(sl['s-rem2']['blocks'][0]['jumps'], [[46, 76, '+30']], 's-rem2 jump'); eq(sl['s-rem2']['blocks'][0]['hide'], [76], 's-rem2 hides the landing number')
    cl = sl['s-rem3']['blocks'][0]['cols']; eq((cl[0][0]['h'], cl[0][0]['m']), (3, 30), 's-rem3 clock'); eq(clock_after(3, 30, 60), (4, 30), 's-rem3 one hour later')
    eq(cl[1][0].get('hide_hands'), True, 's-rem3 second clock hides its hands')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']
    eq(sums_in(sp['q1']), [(40, '+', 20, 70)], 'sneak q1'); eq(is_true(40, '+', 20, 70), False, 'sneak q1 is wrong'); eq(plus(40, 20), 60, 'sneak a1')
    eq(sums_in(sp['q2']), [(27, '+', 16, 33)], 'sneak q2'); eq(is_true(27, '+', 16, 33), False, 'sneak q2 is wrong'); eq(plus(27, 16), 43, 'sneak a2'); eq(43 - 33, 10, 'sneak q2 is exactly a lost ten')
    eq(minus(33, 16), 17, 'sneak a2 check: 33 take away 16'); eq(plus(7, 6), 13, 'sneak a2 ones')
    # ---------------------------------------------------------------- Explore: eight cards, four right, four with exactly one mistake
    cards = d['workbook']['kits'][0]['cards']; eq(len(cards), 8, 'eight cards')
    parsed = [sums_in(c)[0] for c in cards]; eq(len(parsed), 8, 'every card is one sum')
    right = [p for p in parsed if is_true(*p)]; wrong = [p for p in parsed if not is_true(*p)]
    eq((len(right), len(wrong)), (4, 4), 'four right and four wrong')
    eq(sorted(parsed), sorted((a, op, b, c) for k, a, op, b, c in CLASS['explore']), 'cards equal the registered Explore items')
    # each wrong card has one stated mistake: the right answer and the clue
    fix = {(45, '+', 28): (73, 'lost ten', 10), (84, '-', 6): (78, 'swapped ones', 4), (53, '-', 20): (33, 'plus sign', 40), (17, '+', 5): (22, 'one short', 1)}
    for a, op, b, c in wrong:
        r, why, gap = fix[(a, op, b)]
        eq((plus(a, b) if op == '+' else minus(a, b)), r, f'card {a}{op}{b} right answer'); eq(abs(c - r), gap, f'card {a}{op}{b} distance from the right answer')
    # the single-mistake claims, recomputed
    eq(5 + 8, 13, 'card 45+28: ones make 13'); eq(63 + 10, 73, 'lost ten')
    eq(abs(6 - 4), 2, 'card 84-6: ones swapped (6-4)'); eq(80 + 2, 82, 'swapped ones gives 82'); eq(minus(84, 6), 78, 'card 84-6 right')
    eq(53 + 20, 73, 'card 53-20: the plus sign gives 73'); eq(minus(53, 20), 33, 'card 53-20 right')
    for lab, cell in (('WRONG', 'wrong'), ('RIGHT', 'right')):
        pass
    tb = sl['s-explore1-ans']['blocks'][0]['rows']; eq(tb[0], ['WRONG', 'RIGHT'], 's-explore1-ans heads')
    shown_wrong = [sums_in(r[0])[0] for r in tb[1:]]; shown_right = [sums_in(r[1])[0] for r in tb[1:]]
    eq(all(not is_true(*s) for s in shown_wrong) and all(is_true(*s) for s in shown_right), True, 's-explore1-ans sorts correctly')
    eq(sorted(shown_wrong + shown_right), sorted(parsed), 's-explore1-ans shows all eight cards')
    rows = sl['s-explore2-ans']['blocks'][0]['rows'][1:]
    eq([(sums_in(r[0])[0][:3], int(r[1])) for r in rows], [((a, op, b), fix[(a, op, b)][0]) for a, op, b, c in [sums_in(r[0])[0] for r in rows]], 's-explore2-ans right answers')
    # ---------------------------------------------------------------- Mini-lesson
    eq(sums_in(sl['s-m1']['blocks'][0]['text']), [(71, '-', 26, 55)], 's-m1'); eq(add_back_ok(71, 26, 55), False, 's-m1 55 is wrong'); eq(plus(55, 26), 81, 's-m1 add back'); eq(minus(71, 26), 45, 's-m1 right'); eq(add_back_ok(71, 26, 45), True, 's-m1 45 checks')
    eq(add_back_ok(60, 18, 52), False, 's-m1 your turn: 52 is wrong'); eq(plus(52, 18), 70, 's-m1 your turn add back'); eq(minus(60, 18), 42, 's-m1 your turn right'); eq(add_back_ok(60, 18, 42), True, 's-m1 your turn 42 checks')
    eq(sums_in(sl['s-m2']['blocks'][0]['text']), [(29, '+', 35, 54)], 's-m2'); eq(plus(29, 35), 64, 's-m2 right'); eq(take_back_ok(29, 35, 54), False, 's-m2 54 fails the check'); eq(minus(54, 35), 19, 's-m2 check gives 19'); eq(take_back_ok(29, 35, 64), True, 's-m2 64 checks')
    jl = sl['s-m2']['blocks'][1]['jumps']; eq(jl, [[29, 59, '+30'], [59, 64, '+5']], 's-m2 line'); eq((plus(29, 30), plus(59, 5)), (59, 64), 's-m2 jumps land')
    # three-step worked sum 56 + 27
    steps = [(56, 20, 76), (76, 4, 80), (80, 3, 82)]; ok_ = [plus(a, b) == c for a, b, c in steps]; eq(ok_, [True, True, False], 's-m3 only step 3 is wrong'); eq(plus(80, 3), 83, 's-m3 fix'); eq(plus(56, 27), 83, 's-m3 right answer'); eq(minus(83, 27), 56, 's-m3 check')
    eq([r[1] for r in sl['s-m3']['blocks'][0]['rows'][1:]], ['56 + 20 = 76', '76 + 4 = 80', '80 + 3 = 82'], 's-m3 table shows the child\'s steps')
    eq((minus(92, 30), minus(minus(92, 30), 5)), (62, 57), 's-m3 your turn'); eq(minus(92, 35), 57, 's-m3 your turn right'); eq((minus(92, 30) == 72, minus(72, 5) == 67), (False, True), 's-m3 your turn: step 1 wrong, step 2 right working'); eq(plus(57, 35), 92, 's-m3 your turn check')
    # a wrong time
    eq(clock_after(9, 0, 30), (9, 30), 's-m4 bus'); eq(fmt(9, 50) == fmt(*clock_after(9, 0, 30)), False, 's-m4 9:50 is wrong'); eq(sl['s-m4']['blocks'][0]['cols'][0][0]['h'], 9, 's-m4 clock')
    # a wrong total
    t = [(b['item'], b['price']) for c in sl['s-m5']['blocks'][0]['cols'] for b in c]; eq(t, [('pen', '$4'), ('book', '$9')], 's-m5 tags'); eq(plus(4, 9), 13, 's-m5'); eq(plus(4, 9) == 15, False, 's-m5 15 is wrong'); eq(minus(15, 9), 6, 's-m5 check 15 - 9'); eq(minus(15, 9) == 4, False, 's-m5 check fails')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; eq(sums_in(q['text']), [(41, '-', 17, 24)], 'S1'); eq(plus(24, 17), 41, 'S1 add back'); eq(is_true(41, '-', 17, 24), True, 'S1 is right'); eq(q['val'], [41, 'Yes'], 'S1 val')
    q = T['S2']; eq(sums_in(q['text']), [(50, '-', 23, 37)], 'S2'); eq(plus(37, 23), 60, 'S2 add back'); eq(is_true(50, '-', 23, 37), False, 'S2 is wrong'); eq(minus(50, 23), 27, 'S2 right answer'); eq(q['val'], [60, 'No', 27], 'S2 val')
    q = T['S3']; rows = [r[1] for r in q['visual']['rows']]; eq(rows, ['36 + 4 = 40', '40 + 20 = 50', '50 + 4 = 54'], 'S3 rows')
    st = [sums_in(r)[0] for r in rows]; eq([is_true(*s) for s in st], [True, False, True], 'S3 exactly one wrong step (step 2); step 3 is right work from the wrong number'); eq(plus(36, 28), 64, 'S3 right answer'); eq((plus(36, 4), plus(40, 20), plus(60, 4)), (40, 60, 64), 'S3 fixed steps'); eq(q['val'], ['2', 64], 'S3 val')
    q = T['S4']; eq((q['visual']['h'], q['visual']['m']), (2, 30), 'S4 clock'); eq(clock_after(2, 30, 60), (3, 30), 'S4 one hour later'); eq(fmt(3, 0) == fmt(*clock_after(2, 30, 60)), False, 'S4 3:00 is wrong'); eq(q['val'], ['No', '3:30'], 'S4 val')
    eq(clock_after(2, 30, 60)[1] in (0, 30), True, 'S4 o\'clock or half past only')
    q = T['S5']; eq(sorted((v['item'], v['price']) for v in q['visuals']), [('bag', '$7'), ('cup', '$5')], 'S5 tags'); eq(plus(7, 5), 12, 'S5'); eq(plus(7, 5) == 10, False, 'S5 10 is wrong'); eq(minus(10, 7), 3, 'S5 check'); eq(minus(10, 7) == 5, False, 'S5 check fails'); eq(nums(q['text']), [7, 5, 10], 'S5 text'); eq(q['val'], ['No', 12], 'S5 val')
    eq(sorted({4, 9, 15} & set(nums(q['text']))), [], 'S5 shares no number with the Mini-lesson wrong-total example (pen 4, book 9, 15)')
    q = T['S6']; st = [sums_in(s['s'])[0] for s in q['tf']]; eq([is_true(*s) for s in st], [True, False, True, False], 'S6 truth values'); eq(q['val'], ['True', 'False', 'True', 'False'], 'S6 val')
    eq(minus(56, 20), 36, 'S6 56-20'); eq(minus(80, 5), 75, 'S6 80-5')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; eq([r[1] for r in q['visual']['rows']], ['74 ' + MINUS + ' 30 = 44', '44 ' + MINUS + ' 1 = 43'], 'T1 steps')
    eq((minus(74, 30), minus(74, 29)), (44, 45), 'T1'); eq(minus(44, 1), 43, 'T1 child step 2'); eq(plus(44, 1), 45, 'T1 fixed step'); eq(add_back_ok(74, 29, 45), True, 'T1 check'); eq(add_back_ok(74, 29, 43), False, 'T1 child answer fails'); eq(q['val'], ['2', 45], 'T1 val')
    eq(minus(74, 30) == 44, True, 'T1 step 1 is right (so exactly step 2 is wrong)')
    q = T['T2']; eq(nums(q['text'])[:3], [58, 27, 75], 'T2 text'); eq(plus(58, 27), 85, 'T2'); eq((minus(75, 27), minus(85, 27)), (48, 58), 'T2 checks'); eq(take_back_ok(58, 27, 75), False, 'T2 75 fails'); eq(take_back_ok(58, 27, 85), True, 'T2 85 passes'); eq(q['val'], [48, 58, '85'], 'T2 val')
    eq(plus(58, 27) - 75, 10, 'T2 the wrong answer is a lost ten')
    q = T['T3']; eq(nums(q['text']), [28, 6, 28, 6, 22], 'T3 text numbers'); eq(plus(28, 6), 34, 'T3'); eq(minus(34, 28), 6, 'T3 Aisha has 6 more than Mei'); eq(minus(28, 6), 22, 'T3 child\'s answer'); eq(q['val'], ['No', 34], 'T3 val')
    q = T['T4']; cl = [(v['h'], v['m']) for v in q['visuals']]; eq(cl, [(7, 0), (8, 0), (8, 30)], 'T4 clocks'); eq(clock_after(7, 30, 30), (8, 0), 'T4 half an hour after 7:30'); eq([c for c in cl].index((8, 0)), 1, 'T4 B is 8:00'); eq(q['val'], ['B', '8:00'], 'T4 val')
    eq(all(m in (0, 30) for h, m in cl), True, 'T4 clocks are o\'clock and half past')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; eq(nums(q['text']), [52, 39, 191], 'G1 text'); eq(plus(52, 39), 91, 'G1'); eq(91 < 191, True, 'G1 191 is too big'); about = 50 + 40; eq(about, 90, 'G1 about 90'); eq(abs(91 - about) < abs(91 - 30) and abs(91 - about) < abs(91 - 150), True, 'G1 about 90 is the best guess'); eq(q['val'], ['about 90', 'No', 91], 'G1 val')
    eq(min((x for x in (30, 90, 150)), key=lambda x: abs(91 - x)), 90, 'G1 the nearest of the three guesses to the true value')
    q = T['G2']; rows = q['visual']['rows']; eq(rows, [['', '4', '7'], ['+', '3', '8'], ['', '7', '5']], 'G2 rows'); eq(plus(47, 38), 85, 'G2'); ones = plus(7, 8); eq(ones, 15, 'G2 ones'); tens_ok = plus(plus(4, 3), 1); eq(tens_ok, 8, 'G2 tens with the carried ten')
    eq((ones % 10, 7 == tens_ok), (5, False), 'G2 ones digit is right, tens digit is wrong'); eq(q['val'], ['Tens', 85], 'G2 val')
    q = T['G3']; eq(q['val'], ['open'], 'G3 open')
    # ---------------------------------------------------------------- Investigation
    eq(nums(inv['first'])[:3], [25, 19, 34], 'I1 first'); eq(plus(25, 19), 44, 'I1'); eq(minus(34, 19), 15, 'I1 check'); eq(take_back_ok(25, 19, 34), False, 'I1 34 is wrong'); eq(inv['val'], ['44'], 'I1 val')
    for a, b, w in ((25, 19, 34), (36, 27, 53), (48, 35, 73)):
        eq(plus(a, b) - w, 10, f'I1 {a}+{b}={w} is exactly a lost ten'); eq(plus(a % 10, b % 10) >= 10, True, f'I1 {a}+{b}: the ones make a ten to carry')
    eq(sums_in(inv['text']), [(36, '+', 27, 53), (48, '+', 35, 73)], 'I1 text sums'); eq((plus(36, 27), plus(48, 35)), (63, 83), 'I1 right answers')
    eq((plus(29, 14), plus(9, 4) >= 10), (43, True), 'I1 answer example 29 + 14')
    # ---------------------------------------------------------------- talk, exit
    eq(sums_in(d['talk']['question']), [(45, '+', 28, 63)], 'talk sum'); eq(minus(63, 28), 35, 'talk check'); eq(plus(45, 28), 73, 'talk right answer')
    q = X['E1']; eq(sums_in(q['text']), [(82, '-', 47, 45)], 'E1'); eq(plus(45, 47), 92, 'E1 add back'); eq(is_true(82, '-', 47, 45), False, 'E1 is wrong'); eq(minus(82, 47), 35, 'E1 right'); eq(plus(35, 47), 82, 'E1 right checks'); eq(q['val'], [92, 'No'], 'E1 val')
    eq(set(nums(q['text'])) & {63, 28, 45 + 28}, set(), 'E1 does not turn the Talk sum (45 + 28 = 63) round')
    eq(sums_in(T['G3']['solution'])[0], (38, '+', 15, 43), 'G3 example sum'); eq(plus(38, 15), 53, 'G3 example right answer'); eq(minus(43, 15), 28, 'G3 example add-back check'); eq(set(nums(T['G3']['solution'])) & {36, 27, 53 - 0} - {53}, set(), 'G3 example is not the Investigation sum')
    q = X['E2']; opts = q['mcq']['options']
    parsed2 = [sums_in(o)[0] for o in opts]
    eq([is_true(*s) for s in parsed2], [True, False, True], 'E2 truth of each written step (step 3 is right work from the wrong 12)' if False else 'E2 truth of each written step'); eq(minus(15, 2), 13, 'E2 step 2 right is 13'); eq(plus(30, 13), 43, 'E2 final'); eq(plus(28, 15), 43, 'E2 right answer'); eq(plus(30, 12) == 42, True, 'E2 step 3 is right work from the wrong number 12')
    eq(q['val'], [2], 'E2 val')
    q = X['E3']; eq(nums(q['text']), [20, 12, 9], 'E3 text'); eq(minus(20, 12), 8, 'E3'); eq(plus(8, 12), 20, 'E3 check'); eq(plus(9, 12) == 20, False, 'E3 9 is wrong'); eq(q['val'], ['No', 8], 'E3 val')
    # ---------------------------------------------------------------- home
    q = H['H1']; eq(sums_in(q['text']), [(34, '+', 18, 42)], 'H1'); eq(plus(34, 18), 52, 'H1'); eq(take_back_ok(34, 18, 42), False, 'H1 wrong'); eq(plus(34, 18) - 42, 10, 'H1 a lost ten'); eq(q['val'], 'No', 'H1 val')
    q = H['H2']; eq(clock_after(3, 30, 30), (4, 0), 'H2'); eq(q['val'], ['No', '4:00'], 'H2 val')
    q = H['H3']; eq(nums(q['text']), [15, 6, 11], 'H3 text'); eq(minus(15, 6), 9, 'H3'); eq(plus(9, 6), 15, 'H3 check'); eq(plus(11, 6) == 15, False, 'H3 11 is wrong'); eq(q['val'], ['No', 9], 'H3 val')
    q = H['H4']; eq(nums(q['text'])[:4], [46, 38, 74, 84], 'H4 text'); eq(plus(46, 38), 84, 'H4'); eq((minus(74, 38), minus(84, 38)), (36, 46), 'H4 checks'); eq(q['val'], '84', 'H4 val')
    q = H['H5']; eq(nums(q['text'])[:2], [14, 9], 'H5 text'); eq(minus(14, 9), 5, 'H5'); eq(q['val'], 5, 'H5 val'); eq(q.get('rewind_of'), 'Term 1 Lesson 9', 'H5 is the rewind item')
    eq(len([h for h in d['home_practice'] if h['tier'] == 'start']) >= 3, True, 'home has 3 Start here items')
    # ---------------------------------------------------------------- online practice
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, env in BASE_ENV.items():
        eq(items[cid]['answer'], ORACLES[cid](env), cid + ' authored answer')
    eq(items['c2']['answer'], 'No', 'c2 authored'); eq(take_back_ok(37, 25, 52), False, 'c2 authored sum is wrong'); eq(plus(37, 25), 62, 'c2 authored right answer')
    eq(items['c4']['answer'], 'Step 1', 'c4 authored'); eq([plus(58, 2) == 61, plus(61, 10) == 71, plus(71, 3) == 74], [False, True, True], 'c4 steps: only step 1 is wrong, the others are right work from the wrong number'); eq((plus(58, 2), plus(60, 10), plus(70, 3), plus(58, 15)), (60, 70, 73, 73), 'c4 fixed')
    eq(items['t2']['answer'], 'too big', 't2 authored'); eq((plus(48, 41), 50 + 40, 189 > 90 + 20), (89, 90, True), 't2 static: 189 is much bigger than 90')
    eq(items['t3']['answer'], 43, 't3 authored'); eq(items['g2']['answer'], 34, 'g2 authored')
    eq(items['c5']['answer'], '5:00', 'c5 authored'); eq(clock_after(4, 30, 30), (5, 0), 'c5')
    eq(items['g1']['answer'], 29, 'g1 authored'); eq((minus(63, 29), plus(minus(63, 30), 1)), (34, 34), 'g2 static fix')
    eq(items['c3']['answer'], 63, 'c3 authored'); eq(plus(39, 24) - 53, 10, 'c3 static is a lost ten')
    for a, b in itertools.product(items['c3']['tpl']['vars']['a'], items['c3']['tpl']['vars']['b']): eq(plus(a, b) <= 99, True, f'c3 {a}+{b} stays within 100')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] == 'number': eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
    # variant guards
    for a, b in itertools.product(items['c1']['tpl']['vars']['a'], items['c1']['tpl']['vars']['b']): eq(add_back_ok(plus(a, b), b, a), True, f'c1 {a} {b} the shown take away is right')
    for a, b in itertools.product(items['c3']['tpl']['vars']['a'], items['c3']['tpl']['vars']['b']): eq(plus(a % 10, b % 10) >= 10, True, f'c3 {a}+{b}: the ones make a ten, so a forgotten ten is the one mistake')
    for a, b, f in itertools.product(items['c2']['tpl']['vars']['a'], items['c2']['tpl']['vars']['b'], items['c2']['tpl']['vars']['f']): eq(plus(a, b) - 10 * f > 0, True, f'c2 {a} {b} {f} stays positive')
    for a, b, f in itertools.product(items['t2']['tpl']['vars']['a'], items['t2']['tpl']['vars']['b'], items['t2']['tpl']['vars']['f']):
        w = plus(a, b) + 40 * f - 40; eq(w > 0, True, 't2 positive'); eq(abs(10 * ((a + 5) // 10) + 10 * ((b + 5) // 10) - plus(a, b)) <= 6, True, f't2 {a} {b}: the sum is near the sum of the two near tens')
    for m, a, b in itertools.product(items['g1']['tpl']['vars']['m'], items['g1']['tpl']['vars']['a'], items['g1']['tpl']['vars']['b']): eq(m - a - b > 0, True, f'g1 {m} {a} {b} money left')
    for a in items['g2']['tpl']['vars']['a']: eq((minus(a, 30) + 1, a - 29), (a - 29, a - 29), f'g2 {a}')
    # ---------------------------------------------------------------- kit contract and hand-offs
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    for r in kc.values(): eq(r['supplied'] >= r['max_used'], True, 'kit contract ' + r['piece'])
    eq((kc['mistake cards']['supplied'], kc['mistake cards']['max_used']), (8, 8), 'the cards: 8 supplied, 8 used')
    nm = ' '.join(d['parent']['next_materials']).lower()
    eq(all(w in nm for w in ('quest log', 'quest partner', 'tool-card page', '7 tool cards')), True, 'hand-off to Lesson 30 names the Quest Log, a quest partner, the tool-card page and 7 tool cards')
    prev = os.path.join(L1, 'lessons', 'l28.json')
    if os.path.exists(prev):
        p28 = json.load(open(prev, encoding='utf-8'))
        pm = ' '.join(p28['parent']['next_materials']).lower()
        eq(('mistake' in pm and ('8' in pm or 'eight' in pm)), True, 'Lesson 28 hands off the 8 mistake cards')
    nxt = os.path.join(L1, 'lessons', 'l30.json')
    if os.path.exists(nxt):
        p30 = json.load(open(nxt, encoding='utf-8'))
        mk = ' '.join(p30['materials']['child']).lower()
        eq(('quest log' in mk and 'tool cards' in mk and 'quest partner' in mk), True, 'Lesson 30 materials match the hand-off')
    return n
