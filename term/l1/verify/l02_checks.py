"""Independent answer checks for Lesson 2 (Number Words and the Number Line).

Every answer in l02.json is recomputed here from first principles (a real number line as a list, frogs that hop one step
at a time, a number-name generator and parser, enumeration of candidates), not by re-using the lesson's own expressions.
run(d) returns the number of checks; any failure raises AssertionError.
"""

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}


def name_of(n):
    """The English name of a whole number from 0 to 100."""
    if n < 20:
        return ONES[n]
    if n == 100:
        return 'one hundred'
    t, o = divmod(n, 10)
    return TENS[t] + ('-' + ONES[o] if o else '')


def number_of(word):
    """Parse a number name back to a number (independent of name_of: uses its own tables)."""
    word = word.strip().lower()
    if word == 'one hundred':
        return 100
    ones = {w: i for i, w in enumerate(ONES)}
    tens = {w: 10 * k for k, w in TENS.items()}
    if '-' in word:
        a, b = word.split('-')
        return tens[a] + ones[b]
    return tens[word] if word in tens else ones[word]


def line(lo, hi, step=1):
    """The marks on a number line from lo to hi."""
    return list(range(lo, hi + 1, step))


def nearer_ten(n):
    """Which ten is nearer, found by counting hops along the line. None when exactly halfway."""
    marks = line(0, 100, 10)
    below = max(m for m in marks if m <= n)
    above = min(m for m in marks if m >= n)
    hops_down = len([x for x in line(below, n)]) - 1
    hops_up = len([x for x in line(n, above)]) - 1
    if hops_down == hops_up:
        return None
    return below if hops_down < hops_up else above


def two_tens(n):
    """The two tens a number lies between (lower, upper)."""
    marks = line(0, 100, 10)
    below = max(m for m in marks if m <= n)
    above = min(m for m in marks if m > n)
    return below, above


def between_count(a, b):
    return len([x for x in line(a, b) if a < x < b])


def fill_equal_jumps(first, last, boxes):
    """Boxes between first and last that make equal jumps; returns (marks, jump) found by trying every jump size."""
    jumps = boxes + 1
    for j in range(1, 101):
        if first + jumps * j == last:
            return [first + j * k for k in range(1, boxes + 1)], j
    raise AssertionError('no equal jump')


def frogs_meet(a, b):
    """Two frogs hop towards each other one step at a time; return where they meet."""
    x, y = a, b
    while x < y:
        x += 1
        if x == y:
            break
        y -= 1
    return x


# ---- oracles for the online-practice templates (brute force, independent of the template expressions)
ORACLES = {
    'c1': lambda e: line(e['n'], e['n'] + 1)[-1],
    'c2': lambda e: line(e['n'] - 1, e['n'])[0],
    'c4': lambda e: [x for x in line(e['a'], e['a'] + 3) if x not in (e['a'], e['a'] + 1, e['a'] + 3)][0],
    'c5': lambda e: two_tens(e['n'])[1],
    't1': lambda e: nearer_ten(10 * e['t'] + e['o']),
    't2': lambda e: nearer_ten(10 * e['t'] + e['o']),
    't3': lambda e: between_count(e['a'], e['a'] + e['g']),
    'g1': lambda e: fill_equal_jumps(e['a'], e['a'] + 4 * e['j'], 3)[0][1],
    'g2': lambda e: frogs_meet(e['a'], e['a'] + 2 * e['d']),
    'g3': lambda e: len(line(0, e['m'], e['j'])),
}
BASE_ENV = {'c1': dict(n=39), 'c2': dict(n=60), 'c4': dict(a=27), 'c5': dict(n=47), 't1': dict(t=4, o=7), 't2': dict(t=6, o=2),
            't3': dict(a=28, g=7), 'g1': dict(a=0, j=5), 'g2': dict(a=28, d=12), 'g3': dict(m=100, j=10)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    O = {i['id']: i for i in d['online_practice']['items']}

    # ---- the number-name tools themselves: round trip over the whole line
    for k in range(0, 101):
        eq(number_of(name_of(k)), k, 'name round trip ' + str(k))
    eq(name_of(40), 'forty', 'forty has no u'); eq(name_of(14), 'fourteen', 'fourteen'); eq(name_of(15), 'fifteen', 'fifteen')
    eq(name_of(100), 'one hundred', 'hundred')

    # ---- sneak-peek
    eq([x for x in line(18, 22) if x not in (18, 19, 21, 22)], [20], 'sneak q1 first blank')
    eq(line(21, 23)[-1], 23, 'sneak q1 second blank (23 follows 22)')
    eq(d['sneak_peek']['val1'], 20, 'sneak val1 is the first missing number')
    eq(nearer_ten(38), 40, 'sneak q2: 38 is nearer 40')
    eq((38 - 30, 40 - 38), (8, 2), 'sneak q2 hops')

    # ---- Start here
    # S1: the line 8 to 14 with boxes under 10 and 12
    eq([m for m in line(8, 14) if m in (10, 12)], T['S1']['val'], 'S1')
    eq(T['S2']['val'], [[x for x in line(26, 30) if x not in (26, 27, 28, 30)][0], [x for x in line(37, 41) if x not in (37, 38, 40)][0], line(37, 41)[-1], line(70, 71)[0]], 'S2')
    eq(line(37, 41), [37, 38, 39, 40, 41], 'S2b whole line')
    eq(T['S3']['val'], [34, 36, 59, 61, 78, 80], 'S3')
    for m, (b, a) in {35: (34, 36), 60: (59, 61), 79: (78, 80)}.items():
        eq((line(m - 1, m)[0], line(m, m + 1)[-1]), (b, a), f'S3 around {m}')
    eq(T['S4']['val'], [number_of('fifteen'), number_of('fifty'), number_of('twenty-four')], 'S4')
    eq(T['S5']['val'], [name_of(20), name_of(40)], 'S5')
    bank = {'twenty', 'forty', 'sixty', 'eighty'}
    eq(set(T['S5']['val']) <= bank, True, 'S5 answers are all in the word bank')
    shown = [0, 10, 20, None, 40, None, 60, 70, None, 90, 100]
    eq([m for m, s_ in zip(line(0, 100, 10), shown) if s_ is None], T['S6']['val'], 'S6 blanks are 30, 50, 80')
    eq(len(shown), 11, 'S6 has 11 marks')
    eq(T['S7']['val'], list(two_tens(23)) + list(two_tens(68)), 'S7')
    eq(T['S8']['val'], [line(59, 60)[-1]], 'S8: after 59 comes 60')
    eq(divmod(60, 10), (6, 0), 'S8: 60 is 6 tens 0 ones')

    # ---- Think harder
    eq(T['T1']['val'], [nearer_ten(47), nearer_ten(89)], 'T1')
    eq((len(line(40, 47)) - 1, len(line(47, 50)) - 1), (7, 3), 'T1a hops')
    eq((len(line(60, 62)) - 1, len(line(62, 70)) - 1), (2, 8), 'T1b hops')
    eq((len(line(89, 90)) - 1, len(line(80, 89)) - 1), (1, 9), 'T1c hops')
    eq(T['T2']['val'], [between_count(28, 35)], 'T2')
    eq([x for x in line(28, 35) if 28 < x < 35], [29, 30, 31, 32, 33, 34], 'T2 list')
    eq((len(line(28, 35)) - 1, len(line(28, 35))), (7, 8), 'T2 slips: 7 hops, 8 with both ends')
    cands = [m for m in range(1, 100)
             if 50 < m < 60 and nearer_ten(m) == 60 and (m - 1) == (50 + 60) // 2 and (50 + 60) % 2 == 0]
    eq(cands, [56], 'T3 unique number')
    eq(T['T3']['val'], cands, 'T3')
    eq([m for m in range(51, 60) if nearer_ten(m) == 60], [56, 57, 58, 59], 'T3 after clue 2')
    eq(nearer_ten(55), None, 'T3: 55 is exactly halfway')
    eq(T['T4']['val'], line(97, 100) + [len(line(96, 100)) - 1], 'T4')

    # ---- Go further
    g1 = T['G1']['val']
    marks_a, j_a = fill_equal_jumps(0, 30, 2)
    marks_b, j_b = fill_equal_jumps(10, 30, 3)
    marks_c, j_c = fill_equal_jumps(50, 62, 3)
    eq(g1, marks_a + [j_a] + marks_b + [j_b] + marks_c + [j_c], 'G1')
    eq((marks_a, j_a, marks_b, j_b, marks_c, j_c), ([10, 20], 10, [15, 20, 25], 5, [53, 56, 59], 3), 'G1 values')
    eq(T['G2']['val'], [frogs_meet(28, 52)], 'G2')
    eq((52 - 28, (52 - 28) // 2), (24, 12), 'G2 hops')
    eq(frogs_meet(28, 52) - 28, 52 - frogs_meet(28, 52), 'G2 both frogs make the same number of hops')
    eq(T['G3']['val'], 'open', 'G3 is an open task')
    mk = fill_equal_jumps(15, 35, 3)
    eq(mk, ([20, 25, 30], 5), 'G3 example')
    eq(T['G3']['answer'].count('20, 25, 30'), 1, 'G3 answer text states the example')

    # ---- Investigation: every number from 41 to 49, then the same between every two tens
    near = {m: nearer_ten(m) for m in range(41, 50)}
    eq([m for m in near if near[m] == 40], [41, 42, 43, 44], 'I1 nearer 40')
    eq([m for m in near if near[m] == 50], [46, 47, 48, 49], 'I1 nearer 50')
    eq([m for m in near if near[m] is None], [45], 'I1 halfway')
    for t in range(0, 10):
        for o in range(1, 10):
            m = 10 * t + o
            want = None if o == 5 else (10 * t if o < 5 else 10 * t + 10)
            eq(nearer_ten(m), want, f'I1 rule for {m}')
    eq(len([m for m in range(11, 100) if m % 10 and nearer_ten(m) is None]), 9, 'I1: 9 halfway numbers, one between each pair of tens (15 .. 95)')
    eq(nearer_ten(43), 40, 'I1 first step'); eq((len(line(40, 43)) - 1, len(line(43, 50)) - 1), (3, 7), 'I1 first-step hops')

    # ---- Talk, exit, optional
    eq((number_of('fourteen'), number_of('forty')), (14, 40), 'talk: fourteen is 14, forty is 40')
    eq(number_of('forty') > number_of('fourteen'), True, 'talk: forty is bigger')
    eq(divmod(14, 10), (1, 4), 'talk: 14 is ten and 4'); eq(divmod(40, 10), (4, 0), 'talk: 40 is 4 tens')
    eq(X['E1']['val'], [number_of('seventy-three')], 'E1')
    eq(X['E2']['val'], list(two_tens(76)), 'E2')
    eq(X['E3']['val'], [line(99, 100)[-1]], 'E3')
    eq(100 // 2 // 2, 25, 'optional slide: halfway between 0 and 50')
    eq((len(line(0, 25)) - 1, len(line(25, 50)) - 1), (25, 25), 'optional slide: 25 is 25 hops from each end')
    eq(nearer_ten(63), 60, 'M3: 63 is nearer 60'); eq((len(line(60, 63)) - 1, len(line(63, 70)) - 1), (3, 7), 'M3 hops')
    # Spare-time M1: one after a number changes only the ones digit exactly when the ones digit is not 9
    for m in range(10, 99):
        only_ones = (m + 1) // 10 == m // 10
        eq(only_ones, m % 10 != 9, 'M1 ' + str(m))
    eq(((23 + 1) // 10 == 23 // 10, (58 + 1) // 10 == 58 // 10, (69 + 1) // 10 == 69 // 10), (True, True, False), 'M1 chosen numbers')
    eq(len(str(99 + 1)), 3, 'M1: 99 plus one has three digits')

    # ---- Home practice
    H = {h['id']: h for h in d['home_practice']}
    eq(H['H1']['val'], [48, 50], 'H1'); eq(line(46, 50), [46, 47, 48, 49, 50], 'H1 line')
    eq(H['H2']['val'], [number_of('thirteen'), number_of('thirty'), number_of('nineteen'), number_of('ninety')], 'H2')
    eq(H['H3']['val'], list(two_tens(83)), 'H3')
    eq(H['H4']['val'], nearer_ten(56), 'H4'); eq((len(line(56, 60)) - 1, len(line(50, 56)) - 1), (4, 6), 'H4 hops')
    eq(H['H5']['val'], 'open', 'H5')
    eq(fill_equal_jumps(20, 40, 3), ([25, 30, 35], 5), 'H5 example')

    # ---- Online practice authored answers at their own numbers
    eq(O['c1']['answer'], ORACLES['c1'](BASE_ENV['c1']), 'c1'); eq(O['c2']['answer'], ORACLES['c2'](BASE_ENV['c2']), 'c2')
    eq(O['c3']['answer'], str(number_of('forty-two')), 'c3'); eq(O['c3']['answer'] in O['c3']['options'], True, 'c3 option')
    eq(O['c4']['answer'], ORACLES['c4'](BASE_ENV['c4']), 'c4'); eq(O['c5']['answer'], ORACLES['c5'](BASE_ENV['c5']), 'c5')
    eq(O['c6']['answer'], 'thirty', 'c6'); eq(number_of('thirty') > number_of('thirteen'), True, 'c6 value')
    for tid in ('t1', 't2', 't3', 'g1', 'g2', 'g3'):
        eq(O[tid]['answer'], ORACLES[tid](BASE_ENV[tid]), tid)
    eq(O['t4']['answer'], cands[0], 't4')
    # the static questions in the items really ask what the answer says
    eq(fill_equal_jumps(0, 20, 3), ([5, 10, 15], 5), 'g1 text example: middle box is 10')
    eq(frogs_meet(28, 52), O['g2']['answer'], 'g2 text example')
    eq(len(line(0, 100, 10)), O['g3']['answer'], 'g3 text example: 11 marks')
    eq(len(line(0, 100, 10)) - 1, 10, 'g3 slip: 10 jumps')
    # slips are real wrong answers a child could give
    eq(O['c1']['slips'][1]['a'], [30], 'c1 slip 30 is a wrong answer for one after 39'); eq(30 != ORACLES['c1'](BASE_ENV['c1']), True, 'c1 slip')
    # every template variant has a clean question: derived numbers are in range and the halfway number never appears
    for o in (1, 2, 3, 4, 6, 7, 8, 9):
        for t in range(2, 9):
            eq(nearer_ten(10 * t + o) is not None, True, f't1/t2 variant {10 * t + o} is not halfway')
    for a in (10, 16, 28, 34):
        for dd in (6, 10, 12, 15):
            eq((a + 2 * dd) <= 100, True, f'g2 variant {a},{dd} stays on the line')
    return n
