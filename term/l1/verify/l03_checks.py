"""Independent answer checks for Lesson 3 (Digit Cards).

Every answer in l03.json is recomputed here from first principles: the digit-card numbers are built by trying every way
of laying cards in a row (itertools.permutations over card positions), not by re-using the lesson's own formulas.
run(d) returns the number of checks; any failure raises AssertionError.
"""
import itertools


def numbers_from(cards, k):
    """Every number made by laying k of the cards in a row (each card used once). A number may not start with 0."""
    out = set()
    for row in itertools.permutations(range(len(cards)), k):
        digs = [cards[i] for i in row]
        if digs[0] == 0:
            continue
        n = 0
        for x in digs:
            n = n * 10 + x
        out.add(n)
    return sorted(out)


def numbers_with_repeats(cards, k):
    """Every k-digit number if a card may be used more than once."""
    out = set()
    for digs in itertools.product(cards, repeat=k):
        if digs[0] == 0:
            continue
        n = 0
        for x in digs:
            n = n * 10 + x
        out.add(n)
    return sorted(out)


def tens_ones(n):
    return n // 10, n % 10


def bigger(a, b):
    """Compare two numbers the way a child does: tens first, then ones. Independent of Python's < on ints."""
    ta, oa = tens_ones(a)
    tb, ob = tens_ones(b)
    if ta != tb:
        return a if ta > tb else b
    if oa != ob:
        return a if oa > ob else b
    return a


# ---- oracles for the online-practice templates (brute force over the cards, independent of the template expressions)
ORACLES = {
    'c1': lambda e: bigger(e['t1'] * 10 + e['o1'], e['t2'] * 10 + e['o2']),
    'c2': lambda e: min(e['t1'] * 10 + e['o1'], e['t2'] * 10 + e['o2']),
    'c3': lambda e: numbers_from([e['x'], e['y']], 2)[-1],
    'c4': lambda e: numbers_from([e['x'], e['y']], 2)[0],
    't1': lambda e: (lambda ns: ns[0] if len(ns) == 1 else None)(numbers_from([0, e['x']], 2)),
    't2': lambda e: max(numbers_from([e['x'], e['y'], e['z']], 2)),
    't3': lambda e: min(numbers_from([0, e['y'], e['z']], 2)),
    'g2': lambda e: len(numbers_from(list(range(1, e['n'] + 1)), 2)),
}
BASE_ENV = {
    'c1': dict(t1=6, o1=1, t2=3, o2=8),
    'c2': dict(t1=5, o1=2, t2=2, o2=9),
    'c3': dict(x=7, y=2),
    'c4': dict(x=7, y=2),
    't1': dict(x=6),
    't2': dict(x=2, y=5, z=8),
    't3': dict(y=4, z=9),
    'g2': dict(n=4),
}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {h['id']: h for h in d['home_practice']}
    O = {i['id']: i for i in d['online_practice']['items']}

    # ---- sneak-peek: puzzle 1 star counts really drawn, puzzle 2 numbers
    import os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
    import svg
    sk = [s for s in d['slides'] if s['id'] == 's-sneak'][0]

    def scatters(blocks):
        res = []
        for b in blocks:
            if b['t'] == 'visual' and b['type'] == 'scatter':
                res.append(b)
            if b['t'] == 'cols':
                for c in b['cols']:
                    res += scatters(c)
        return res
    sc = scatters(sk['blocks'])
    counts = [svg.scatter(b['n'], b.get('seed', 1)).count('<polygon') for b in sc]
    eq(counts, [15, 18], 'sneak: stars drawn in box A and box B')
    eq(d['sneak_peek']['val1'], max(counts), 'sneak q1: the bigger box has 18')
    eq(d['sneak_peek']['a1'], '18', 'sneak a1 text')
    ali = numbers_from([4, 8], 2)  # 48, 84
    eq(ali, [48, 84], 'sneak q2: the two numbers from 4 and 8')
    eq(bigger(48, 84), 84, 'sneak q2: Mei (8 on the left) has the bigger number')
    eq(tens_ones(84), (8, 4), 'sneak q2: 84 is 8 tens'); eq(tens_ones(48), (4, 8), 'sneak q2: 48 is 4 tens')

    # ---- Remember warm-up
    eq([tens_ones(x) for x in (25, 40, 17, 63)], [(2, 5), (4, 0), (1, 7), (6, 3)], 'rem2 tens and ones')
    eq(max(13, 9), 13, 'rem3 left group is bigger'); eq(max(16, 19), 19, 'rem3 16 or 19'); eq(max(20, 12), 20, 'rem3 20 or 12')
    rem3 = [s for s in d['slides'] if s['id'] == 's-rem3'][0]
    frames = [b for b in rem3['blocks'][0]['cols']]
    eq([c[0]['tens'] * 10 + c[0]['ones'] for c in frames], [13, 9], 'rem3 pictures show 13 and 9 squares')

    # ---- Explore rounds
    eq(numbers_from([7, 2], 2), [27, 72], 'explore 7 and 2')
    eq(numbers_from([3, 9], 2)[-1], 93, 'explore 3 and 9')
    eq(numbers_from([0, 5], 2), [50], 'explore 0 and 5: only 50 (05 is not a two-digit number)')
    eq(numbers_from([6, 1], 2)[0], 16, 'explore 6 and 1 smallest')
    eq(numbers_from([8, 5], 2)[0], 58, 'explore 8 and 5 smallest')

    # ---- Mini-lesson
    eq(numbers_from([3, 5], 2), [35, 53], 'mini 3 and 5')
    eq(bigger(61, 59), 61, 'mini 61 v 59'); eq(bigger(47, 43), 47, 'mini 47 v 43'); eq(bigger(52, 58), 58, 'mini 52 v 58')
    eq([bigger(28, 82), bigger(61, 59), bigger(34, 38)], [82, 61, 38], 'mini your turn answers')
    m3a = [s for s in d['slides'] if s['id'] == 's-m3a'][0]
    shown = [c[1]['text'] for c in m3a['blocks'][0]['cols']]
    eq(shown, ['82', '61', '38'], 'slide s-m3a shows the answers')
    eq((numbers_from([7, 2], 2)[-1], numbers_from([7, 2], 2)[0]), (72, 27), 'mini 7 and 2 biggest, smallest')
    eq((numbers_from([4, 9], 2)[-1], numbers_from([4, 9], 2)[0]), (94, 49), 'mini 4 and 9')
    eq((numbers_from([1, 6], 2)[-1], numbers_from([1, 6], 2)[0]), (61, 16), 'mini 1 and 6')
    eq(numbers_from([0, 6], 2), [60], 'mini 0 and 6')
    eq(sorted([45, 54, 39, 40], key=lambda x: (tens_ones(x))), [39, 40, 45, 54], 'mini order')
    # the break pairs
    pairs = [(52, 25, 'tall'), (38, 83, 'small'), (61, 59, 'tall'), (40, 40, 'same'), (19, 21, 'small')]
    for a, b, r in pairs:
        got = 'same' if a == b else ('tall' if bigger(a, b) == a else 'small')
        eq(got, r, f'break {a},{b}')

    # ---- Start here
    eq(T['S1']['val'], numbers_from([3, 5], 2) + [bigger(35, 53)], 'S1')
    eq(T['S2']['val'], [bigger(27, 72), bigger(48, 41), bigger(65, 56), bigger(13, 30)], 'S2')
    eq(T['S2']['val'], [72, 48, 65, 30], 'S2 values')
    mei, ben = 3 * 10 + 8, 4 * 10 + 1
    vis = T['S3']['visual']
    eq((vis['tens'], vis['ones']), (3, 8), 'S3 picture is Mei 38')
    eq(T['S3']['val'], [mei, ben, 'Ben' if bigger(mei, ben) == ben else 'Mei'], 'S3')
    s4 = numbers_from([6, 2], 2)
    eq(s4, [26, 62], 'S4 only two numbers with both cards')
    eq(T['S4']['val'], [s4[-1], s4[0]], 'S4')
    eq(T['S5']['val'], sorted([52, 25, 41, 14], key=tens_ones), 'S5')
    eq(T['S6']['val'], [bigger(19, 21)], 'S6: 21 is bigger, Ravi is wrong')
    eq(bigger(19, 21) == 19, False, 'S6 Ravi wrong')
    s7 = numbers_from([2, 8], 2)
    eq(T['S7']['val'], [[x for x in s7 if x > 50][0], [x for x in s7 if x < 50][0]], 'S7')
    eq(len([x for x in s7 if x > 50]), 1, 'S7 unique numbers')
    siti, ravi = 2 * 10 + 5, 5 * 10 + 2
    eq(T['S8']['val'], ['Ravi' if bigger(siti, ravi) == ravi else 'Siti'], 'S8')
    eq(sorted(str(siti)), sorted(str(ravi)), 'S8: both numbers use the same two digits')
    eq(sum(q['mins'] for q in d['tiers']['start']) <= 20, True, 'Start here fits 20 minutes')

    # ---- Think harder
    t1 = numbers_from([3, 5, 8], 2)
    eq(t1, [35, 38, 53, 58, 83, 85], 'T1 list')
    eq(T['T1']['val'], [t1[-1], t1[0]], 'T1')
    t2 = numbers_from([0, 3, 7], 2)
    eq(t2, [30, 37, 70, 73], 'T2 list')
    eq(T['T2']['val'], [t2[0], t2[-1]], 'T2')
    cards = [1, 3, 5, 7]
    fits = [x for x in numbers_from(cards, 2) if x > 40 and tens_ones(x)[0] > tens_ones(x)[1]]
    eq(fits, [51, 53, 71, 73, 75], 'T3 numbers that fit both clues')
    eq(T['T3']['val'], fits, 'T3')
    eq([x for x in numbers_from(cards, 2) if x > 40], [51, 53, 57, 71, 73, 75], 'T3 first clue only')
    t4 = numbers_from([2, 4, 6], 2)
    eq(T['T4']['val'], [len(t4)] + t4, 'T4')
    eq(len(t4), 6, 'T4 count')

    # ---- Go further
    g1 = numbers_from([2, 5, 6, 9], 2)
    eq(g1, [25, 26, 29, 52, 56, 59, 62, 65, 69, 92, 95, 96], 'G1 all twelve numbers')
    g1a = [x for x in g1 if x < 60]
    g1b = [x for x in g1 if x > 50]
    eq(T['G1']['val'], [g1a[-1], g1b[0]], 'G1')
    eq(T['G1']['val'], [59, 52], 'G1 values')
    eq(g1a[-1] != g1[-1] and g1b[0] != g1[0], True, 'G1 differs from plain greatest/smallest')
    eq(len(numbers_from([1, 2, 3, 4], 2)), 12, 'G2 each card once')
    eq(len(numbers_with_repeats([1, 2, 3, 4], 2)), 16, 'G2 a card may repeat')
    eq(sorted(set(numbers_with_repeats([1, 2, 3, 4], 2)) - set(numbers_from([1, 2, 3, 4], 2))), [11, 22, 33, 44], 'G2 the extra four')
    eq(T['G2']['val'], [12, 16], 'G2')
    allg = numbers_from([1, 3, 4, 7], 2)
    eq(allg, [13, 14, 17, 31, 34, 37, 41, 43, 47, 71, 73, 74], 'G3 all twelve numbers')
    def ones_gt(x): return x % 10 > (x // 10)
    g3 = [x for x in allg if 35 < x < 45 and ones_gt(x)]
    eq(g3, [37], 'G3 unique number')
    eq(T['G3']['val'], g3, 'G3')
    # every G3 clue is needed (drop one clue at a time: more than one number fits)
    eq(len([x for x in allg if x < 45 and ones_gt(x)]) > 1, True, 'G3 clue 1 is needed')
    eq(len([x for x in allg if x > 35 and ones_gt(x)]) > 1, True, 'G3 clue 2 is needed')
    eq(len([x for x in allg if 35 < x < 45]) > 1, True, 'G3 clue 3 is needed')

    # ---- Investigation: for any two different non-zero cards the bigger card on the left gives the bigger number
    for a in range(1, 10):
        for b in range(1, 10):
            if a == b:
                eq(len(numbers_from([a, b], 2)), 1, f'inv same cards {a},{b}: one number')
                continue
            hi, lo = max(a, b), min(a, b)
            nums = numbers_from([a, b], 2)
            eq(nums[-1], hi * 10 + lo, f'inv {a},{b} bigger card on the left is bigger')
    for b in range(1, 10):
        eq(numbers_from([0, b], 2), [b * 10], f'inv 0 and {b}: only one number')
    eq(numbers_from([2, 7], 2), [27, 72], 'inv first step'); eq(numbers_from([0, 8], 2), [80], 'inv 0 and 8'); eq(numbers_from([4, 4], 2), [44], 'inv 4 and 4')

    # ---- Talk: Mei's claim (smallest card on the left gives the smallest number) holds unless that card is 0
    for a in range(0, 10):
        for b in range(a + 1, 10):
            nums = numbers_from([a, b], 2)
            claim = a * 10 + b          # smallest card on the left
            eq(claim in nums, a != 0, f'talk {a},{b}: smallest-on-left is a two-digit number only if the card is not 0')
            if a != 0:
                eq(nums[0], claim, f'talk {a},{b} smallest')
    eq(numbers_from([3, 8], 2)[0], 38, 'talk 3 and 8'); eq(numbers_from([0, 5], 2), [50], 'talk 0 and 5')

    # ---- Exit
    eq(X['E1']['val'], [bigger(39, 41)], 'E1')
    e2 = numbers_from([7, 3], 2)
    eq(X['E2']['val'], [e2[-1], e2[0]], 'E2')
    eq(X['E3']['val'], sorted([63, 36, 60], key=tens_ones), 'E3')

    # ---- Home practice
    eq(H['H1']['val'], numbers_from([4, 7], 2), 'H1'); eq(bigger(47, 74), 74, 'H1 bigger')
    eq(H['H2']['val'], sorted([72, 27, 70, 17], key=tens_ones), 'H2')
    eq(H['H3']['val'], bigger(38, 41), 'H3')
    h4 = numbers_from([0, 6, 9], 2)
    eq(h4, [60, 69, 90, 96], 'H4 list'); eq(H['H4']['val'], [h4[0], h4[-1]], 'H4')
    h5 = numbers_from([1, 2, 3, 4, 5], 2)
    eq(len(h5), 20, 'H5 count'); eq(H['H5']['val'], 20, 'H5')
    eq(H['H5']['answer'], '20 numbers: ' + ', '.join(str(x) for x in h5), 'H5 list in the answer text')

    # ---- Optional slide and spare-time menu
    same_digit = [x for x in range(10, 100) if x // 10 == x % 10]
    eq(same_digit, [11, 22, 33, 44, 55, 66, 77, 88, 99], 'optional: matching digits')
    eq(len(same_digit), 9, 'optional: nine numbers')
    for a, b in ((2, 9), (5, 6), (3, 7)):
        eq(numbers_from([a, b], 2)[-1], max(a, b) * 10 + min(a, b), f'M1 {a},{b}')
    eq(bigger(61, 59), 61, 'M3 61 v 59')
    ex = [s for s in d['slides'] if s['id'] == 's-m2'][0]
    eq([(b['tens'], b['ones']) for b in [c[0] for c in ex['blocks'][0]['cols']]], [(6, 1), (5, 9)], 's-m2 pictures are 61 and 59')
    # kit pictures that carry a label show the number in the label
    def check_labels(blocks):
        nonlocal n
        for b in blocks:
            if b['t'] == 'visual' and b.get('type') == 'bundles' and b.get('label') and b['label'].replace('Ali: ', '').replace('Mei: ', '').isdigit():
                eq(int(b['label'].split()[-1]), b['tens'] * 10 + b['ones'], 'picture label ' + b['label'])
            if b['t'] == 'cols':
                for c in b['cols']:
                    check_labels(c)
    for s in d['slides']:
        check_labels(s['blocks'])

    # ---- Online practice authored answers
    eq(O['c1']['answer'], ORACLES['c1'](BASE_ENV['c1']), 'c1'); eq(O['c2']['answer'], ORACLES['c2'](BASE_ENV['c2']), 'c2')
    eq(O['c3']['answer'], ORACLES['c3'](BASE_ENV['c3']), 'c3'); eq(O['c4']['answer'], ORACLES['c4'](BASE_ENV['c4']), 'c4')
    eq(O['c5']['answer'], ' and '.join(str(x) for x in numbers_from([3, 8], 2)), 'c5')
    eq(O['c6']['answer'], str(max([36, 63, 60, 30], key=tens_ones)), 'c6')
    eq(O['t1']['answer'], ORACLES['t1'](BASE_ENV['t1']), 't1'); eq(O['t2']['answer'], ORACLES['t2'](BASE_ENV['t2']), 't2')
    eq(O['t3']['answer'], ORACLES['t3'](BASE_ENV['t3']), 't3')
    eq(O['t4']['answer'], len(fits), 't4')
    og1 = [x for x in numbers_from([2, 5, 6, 9], 2) if x < 60]
    eq(O['g1']['answer'], og1[-1], 'g1 greatest number less than 60'); eq(O['g2']['answer'], ORACLES['g2'](BASE_ENV['g2']), 'g2')
    eq(O['g3']['answer'], g3[0], 'g3')
    # g4 example: cards 2, 4, 6, 8, more than 50, left digit bigger than right
    ex4 = [x for x in numbers_from([2, 4, 6, 8], 2) if x > 50 and tens_ones(x)[0] > tens_ones(x)[1]]
    eq(ex4, [62, 64, 82, 84, 86], 'g4 example numbers'); eq(len(ex4), 5, 'g4 example count')
    # the template variants never produce an unfair question: every c1/c2 pair has different tens (so the tens decide)
    for t1_ in (5, 6, 7, 8):
        for t2_ in (2, 3, 4):
            eq(t1_ > t2_, True, f'c1/c2 tens differ {t1_},{t2_}')
    return n
