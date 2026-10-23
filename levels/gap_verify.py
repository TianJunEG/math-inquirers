"""Independent answer checks for levels/gap_items.py (GAPS-SLIDES-NOW). Each checker recomputes the answer from the question's numbers by brute force
(never from the stored answer) and returns the strings that must appear in the item's 'ans' lines (or, for 'id:var', in the variant's answer).
    python3 levels/gap_verify.py        -> prints one line per item and exits 1 on any failure."""
import sys, os, itertools, math, datetime
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gap_items

def letter_sols(words, res):
    letters = sorted(set(''.join(words) + res)); out = []
    for pm in itertools.permutations(range(10), len(letters)):
        m = dict(zip(letters, pm))
        if any(m[w[0]] == 0 for w in words + [res]): continue
        val = lambda w: int(''.join(str(m[c]) for c in w))
        if sum(val(w) for w in words) == val(res): out.append(m)
    return out
def unique_letters(words, res):
    s = letter_sols(words, res); assert len(s) == 1, (words, res, len(s)); return s[0]

V = {}
def chk(name):
    def d(f): V[name] = f; return f
    return d

# ---------------- Level 4
@chk('4:digit')
def _():
    a = [n for n in (724, 618) if sum(map(int, str(n))) % 3 == 0]
    b = [n for n in range(580, 590) if n % 6 == 0]
    assert a == [618] and b == [582, 588]; return ['618: digit sum 15, yes', '582 and 588', 'box can be 2 or 8']
@chk('4:digit:var')
def _(): return ['732 and 738'] if [n for n in range(730, 740) if n % 6 == 0] == [732, 738] else ['FAIL']
@chk('4:weekday')
def _():
    d = datetime.date(2026, 10, 19)  # a Monday
    assert d.strftime('%A') == 'Monday'
    a = (d + datetime.timedelta(45)).strftime('%A'); s = datetime.date(2026, 10, 24); assert s.strftime('%A') == 'Saturday'
    return ['(a) ' + a + '.', '(b) ' + (s + datetime.timedelta(30)).strftime('%A') + '.']
@chk('4:weekday:var')
def _():
    t = datetime.date(2026, 10, 20); assert t.strftime('%A') == 'Tuesday'; return [(t + datetime.timedelta(100)).strftime('%A')]
@chk('4:cr1')
def _():
    m = unique_letters(['PQ', 'PR'], 'QQS'); return ['P = %d, Q = %d, R = %d, S = %d' % (m['P'], m['Q'], m['R'], m['S'])]
@chk('4:cr1:var')
def _():
    m = unique_letters(['TT', 'UT'], 'TVW'); return ['T = %d, U = %d, V = %d, W = %d' % (m['T'], m['U'], m['V'], m['W'])]
@chk('4:cr2')
def _():
    m = unique_letters(['DDA', 'ECD'], 'EBAE'); return ['D = %d, A = %d, E = %d, C = %d, B = %d' % (m['D'], m['A'], m['E'], m['C'], m['B'])]
@chk('4:pair')
def _():
    L = list(range(11, 42, 3)); return ['(a) %d numbers' % len(L), '(b) %d.' % sum(L)]
@chk('4:pair:var')
def _(): L = list(range(5, 50, 4)); return ['%d' % sum(L), '%d numbers' % len(L)]
@chk('4:gap')
def _():
    t = [3]; g = 2
    for _i in range(9): t.append(t[-1] + g); g += 1
    return ['(a) %d coins' % t[5], '(b) %d coins' % t[9]]
@chk('4:gap:var')
def _():
    t = [4]; g = 2
    for _i in range(7): t.append(t[-1] + g); g += 1
    return ['%d (' % t[7]]
@chk('4:fan')
def _():
    n = 4; tri = list(itertools.combinations(range(n), 2))
    by = {}
    for a, b in tri: by[b - a] = by.get(b - a, 0) + 1
    return ['%d triangles of size 1, %d of size 2, %d of size 3' % (by[1], by[2], by[3]), '%d triangles altogether' % len(tri)]
@chk('4:fan:var')
def _(): return ['%d (' % len(list(itertools.combinations(range(5), 2)))]
@chk('4:spin')
def _():
    blue = 1 - Fraction(1, 2) - Fraction(1, 3); assert blue == Fraction(1, 6)
    return ['(a) %s.' % blue, 'About %d times' % (60 * Fraction(1, 2)), 'green about %d' % (60 * Fraction(1, 3)), 'blue about %d' % (60 * blue)]
def _trip(po_close, order):
    walk = {('H', 'P'): 20, ('H', 'L'): 30, ('P', 'L'): 15}
    w = lambda a, b: walk.get((a, b)) or walk[(b, a)]
    t = 14 * 60 + 40; pos = 'H'
    for place in order:
        t += w(pos, place); pos = place
        if place == 'L' and t < 15 * 60 + 10: t = 15 * 60 + 10
        if place == 'P' and t > po_close: return None
        t += 10
    return t + w(pos, 'H')
@chk('4:time')
def _():
    ok = {o: _trip(15 * 60 + 30, o) for o in itertools.permutations('PL')}
    good = [o for o, v in ok.items() if v]; assert good == [('P', 'L')]
    t = ok[('P', 'L')]; return ['The post office first', '%d:%02d pm' % (t // 60 - 12, t % 60)]
@chk('4:time:var')
def _():
    ok = {o: _trip(15 * 60 + 40, o) for o in itertools.permutations('PL')}
    assert all(ok.values()) and len(set(ok.values())) == 1; t = list(ok.values())[0]; return ['Both orders work', '%d:%02d pm' % (t // 60 - 12, t % 60), 'tie']
@chk('4:dice')
def _():
    tot = {sum(c) for c in itertools.product(range(1, 7), repeat=4)}
    assert tot == set(range(4, 25)); imp = [x for x in (3, 4, 13, 24, 25) if x not in tot]
    return ['(a) %d.' % min(tot), '(b) %d.' % max(tot), '(c) %s and %s are impossible' % tuple(imp)]
@chk('4:dice:var')
def _():
    tot = {sum(c) for c in itertools.product(range(1, 7), repeat=5)}; return ['%d and %d' % (min(tot), max(tot))]
@chk('4:stages')
def _():
    outfits = list(itertools.product(range(4), range(3), range(2))); bad = [o for o in outfits if o[0] == 0 and o[1] == 0]
    return ['(a) %d outfits' % len(outfits), '(b) %d outfits' % (len(outfits) - len(bad))]
@chk('4:stages:var')
def _(): return ['%d routes' % len(list(itertools.product(range(3), range(4))))]


def frob(a, b):
    ok = [False] * 400; ok[0] = True
    for n in range(1, 400): ok[n] = (n >= a and ok[n - a]) or (n >= b and ok[n - b])
    return max(n for n in range(400) if not ok[n]), [n for n in range(1, 21) if ok[n]]
def groups(total_lo, total_hi):  # helper not used
    return None

# ---------------- Level 5
@chk('5:digit')
def _():
    cards = [2, 4, 5, 7, 8, 9]; best = max(int(''.join(map(str, p))) for p in itertools.permutations(cards, 5) if sum(p) % 9 == 0)
    return ['(a) %d.' % sum(cards), '(b) %d.' % best]
@chk('5:digit:var')
def _():
    best = max(int(''.join(map(str, p))) for p in itertools.permutations([1, 3, 4, 6, 8, 9], 5) if sum(p) % 3 == 0); return ['%d.' % best]
@chk('5:parity')
def _():
    odd = [k for k, v in {'(i)': 3 * 7 * 11 * 5, '(ii)': 13 * 14 + 15, '(iii)': 25 + 36 + 47, '(iv)': 1001 * 2002 - 3}.items() if v % 2]
    assert odd == ['(i)', '(ii)', '(iv)']; return ['(a) %s.' % '{:,}'.format(8 * 17 * 125).replace(',', ' '), '(i), (ii) and (iv) are odd', '(iii) is even']
@chk('5:parity:var')
def _():
    assert (17 + 18 + 19) % 2 == 0 and (6 * 15 + 1) % 2 == 1
    return ['{:,}'.format(4 * 29 * 25).replace(',', ' ') + '.', '17 + 18 + 19 = %d is even' % (17 + 18 + 19), '6 x 15 + 1 = %d is odd' % (6 * 15 + 1)]
@chk('5:cr1')
def _():
    m = unique_letters(['CCC', 'AEA'], 'ABAD'); return ['A = %d, B = %d, C = %d, D = %d, E = %d' % tuple(m[c] for c in 'ABCDE')]
@chk('5:cr2')
def _():
    sol = [(k, m, n, pp) for k in range(1, 10) for m in range(10) for n in range(1, 10) for pp in range(10) if len({k, m, n, pp}) == 4 and (10 * k + m) * m == 100 * n + 10 * n + pp]
    assert len(sol) == 1, sol; k, m, n, pp = sol[0]; return ['K = %d, M = %d, N = %d, P = %d' % (k, m, n, pp)]
@chk('5:r4')
def _():
    return ['(a) %s.' % Fraction(3, 8), '(b) %s.' % Fraction(5, 8), '(c) %d red' % (40 * 3 // 8)] if 40 % 8 == 0 else ['FAIL']
@chk('5:r4:var')
def _(): return ['%s;' % Fraction(2, 9), '%d cups' % (45 * 2 // 9)]
@chk('5:r1')
def _():
    blue = Fraction(2, 5) * 20; white = 20 - blue; return ['(a) %d tins of white' % (4 * 3 // 2), 'Blue %d tins, white %d tins' % (blue, white), '20 / 5 = 4 tins']
@chk('5:r2')
def _():
    from math import gcd
    g = gcd(6, 9); return ['(a) 6 : 9.', '(b) %d : %d' % (6 // g, 9 // g), '(c) %d cups' % (10 * 9 // 6), '(d) %d.' % (12 * 3 // 2)]
@chk('5:r2:var')
def _():
    from math import gcd
    g = gcd(8, 12); assert (14 * 12) % 8 == 0; return ['%d : %d;' % (8 // g, 12 // g), '%d tins' % (14 * 12 // 8)]
@chk('5:r3')
def _():
    parts = 4 + 5; one = 45 // parts; assert one * parts == 45; return ['(a) %d parts' % parts, '(b) %d stickers' % one, 'Mei %d stickers and Siti %d stickers' % (4 * one, 5 * one), '(d) %d more' % (one)]
@chk('5:r3:var')
def _(): one = 56 // 8; assert one * 8 == 56; return ['Ravi %d marbles, Aisha %d marbles' % (3 * one, 5 * one)]
@chk('5:dice')
def _():
    tots = set()
    for t1 in range(1, 7):
        for t2 in range(1, 7):
            top3 = 4; tots.add((7 - t1) + t1 + (7 - t2) + t2 + (7 - top3))
    assert len(tots) == 1; return ['%d dots' % tots.pop()]
@chk('5:dice:var')
def _():
    tots = {(7 - a) + a + (7 - b) + b + (7 - 2) for a in range(1, 7) for b in range(1, 7)}; assert len(tots) == 1; return ['%d dots' % tots.pop()]
@chk('5:pack')
def _():
    g, ok = frob(5, 8); return ['(a) ' + ', '.join(map(str, ok)) + '.', '(b) %d.' % g]
@chk('5:pack:var')
def _(): return ['%d.' % frob(4, 7)[0]]
def _catch(a_speed, b_speed, delay):
    t = 0
    while True:
        t += 1
        if b_speed * t >= a_speed * (t + delay): return a_speed * delay, b_speed - a_speed, t
@chk('5:catch')
def _():
    lead, gain, t = _catch(60, 80, 5); return ['(a) %d m' % lead, '(b) %d m' % gain, '(c) %d minutes' % t]
@chk('5:catch:var')
def _(): return ['%d minutes' % _catch(50, 70, 4)[2]]
def _work(rates, joiner, join_t, total):
    t = 0; done = 0
    while done < total:
        t += 1; done += sum(rates) + (joiner if t > join_t else 0)
    return t
@chk('5:work')
def _(): return ['(a) %d bricks' % ((10 + 14) * 5), '(b) %d minutes' % _work([10, 14], 6, 5, 450)]
@chk('5:work:var')
def _(): return ['%d minutes' % _work([8, 12], 10, 3, 300)]
@chk('5:r5')
def _():
    return ['(a) %d cups of water' % (6 * 5 // 2), '(b) %d cups of rice' % (25 * 2 // 5), '%d + %d = %d cups' % (12, 12 * 5 // 2, 12 + 12 * 5 // 2)]
@chk('5:r5:var')
def _(): assert 18 * 4 % 3 == 0; return ['%d cups' % (18 * 4 // 3)]
@chk('5:r6')
def _():
    boys = Fraction(3, 5); girls_pc = Fraction(2, 5) * 100; return ['(a) %s.' % boys, '(b) %d%%.' % girls_pc, '(c) %d boys' % (30 * 3 // 5)]
@chk('5:r6:var')
def _(): return ['%d%%;' % (Fraction(1, 5) * 100), '%d dogs' % (60 * 4 // 5)]
@chk('5:year')
def _():
    d0 = datetime.date(2019, 1, 1); assert d0.strftime('%A') == 'Tuesday'
    days = [d0 + datetime.timedelta(i) for i in range(365)]; assert days[-1].year == 2019
    tues = sum(1 for d in days if d.strftime('%A') == 'Tuesday'); others = [n for n in ('Monday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') if sum(1 for d in days if d.strftime('%A') == n) == 53]
    assert not others
    return ['(a) %d weeks and %d day' % divmod(365, 7), '(b) %d Tuesdays' % tues, '(c) %s.' % days[-1].strftime('%A'), '(d) %s.' % (days[-1] + datetime.timedelta(1)).strftime('%A')]
@chk('5:year:var')
def _():
    d0 = datetime.date(2021, 1, 1); assert d0.strftime('%A') == 'Friday'
    c = {}
    for i in range(365): n = (d0 + datetime.timedelta(i)).strftime('%A'); c[n] = c.get(n, 0) + 1
    return [[k for k, v in c.items() if v == 53][0] + '.']
@chk('5:last')
def _(): return ['(a) %d.' % pow(7, 30, 10), '(b) %d.' % pow(4, 25, 10)]
@chk('5:last:var')
def _(): return ['%d (' % pow(2, 22, 10)]
@chk('5:range')
def _():
    a = [n for n in range(101, 500) if n % 7 == 0]; b = [n for n in a if n % 2 == 0]; return ['%d multiples of 7' % len(a), '%d multiples of 14' % len(b)]
@chk('5:range:var')
def _(): return ['%d.' % len([n for n in range(201, 700) if n % 9 == 0])]
@chk('5:gaps')
def _():
    t = [2]; g = 1
    for _i in range(9): t.append(t[-1] + g); g += 2
    gaps = [t[i + 1] - t[i] for i in range(4)]
    assert t[:5] == [2, 3, 6, 11, 18]; return ['The gaps are %s. They go up by 2' % ', '.join(map(str, gaps)), '(b) %d blocks' % t[7], '(c) %d blocks' % t[9]]
@chk('5:gaps:var')
def _():
    t = [1]; g = 1
    for _i in range(6): t.append(t[-1] + g); g += 2
    assert t[:4] == [1, 2, 5, 10]; return ['%d.' % t[6]]
def _woven(n):
    return 3 + 4 * ((n - 1) // 2) if n % 2 else 50 - 4 * (n // 2 - 1)
@chk('5:woven')
def _():
    assert [_woven(i) for i in range(1, 8)] == [3, 50, 7, 46, 11, 42, 15]
    return ['(a) %d and %d.' % (_woven(8), _woven(9)), '(b) %d.' % _woven(15), '(c) %d.' % _woven(16)]
@chk('5:woven:var')
def _():
    f = lambda n: 5 + 4 * ((n - 1) // 2) if n % 2 else 80 - 6 * (n // 2 - 1)
    assert [f(i) for i in range(1, 7)] == [5, 80, 9, 74, 13, 68]; return ['%d.' % f(12)]
@chk('5:op')
def _():
    ex = [((2, 3), 8), ((4, 1), 8), ((5, 2), 15), ((3, 3), 12)]; rng = range(-4, 5); vals = set(); xs = set()
    for p_, q, r, s_ in itertools.product(rng, repeat=4):
        f = lambda a, b: p_ * a * b + q * a + r * b + s_
        if all(f(a, b) == v for (a, b), v in ex): vals.add(f(6, 4)); xs |= {x for x in range(1, 100) if f(x, 3) == 28}
    assert len(vals) == 1 and len(xs) == 1, (vals, xs); return ['(a) %d.' % vals.pop(), '(b) %d.' % xs.pop()]
@chk('5:op:var')
def _():
    ex = [((1, 4), 7), ((2, 5), 11), ((3, 2), 11), ((5, 1), 16)]; vals = set()
    for p_, q, r, s_ in itertools.product(range(-4, 5), repeat=4):
        f = lambda a, b: p_ * a * b + q * a + r * b + s_
        if all(f(a, b) == v for (a, b), v in ex): vals.add(f(4, 6))
    assert len(vals) == 1; return ['%d ' % vals.pop()]
def _count_triangles():
    F = Fraction
    A = (F(280), F(30)); B = (F(40), F(340)); C = (F(520), F(340))
    on = lambda P, Q, t: (P[0] + (Q[0] - P[0]) * t, P[1] + (Q[1] - P[1]) * t)
    D = on(B, C, F(1, 3)); E = on(B, C, F(2, 3)); Fp = on(A, B, F(11, 20)); G = on(A, C, F(11, 20))
    segs = [(A, B), (A, C), (B, C), (A, D), (A, E), (Fp, G)]
    def inter(s1, s2):
        (x1, y1), (x2, y2) = s1; (x3, y3), (x4, y4) = s2
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0: return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den; u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        if 0 <= t <= 1 and 0 <= u <= 1: return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
        return None
    n = 0
    for a, b, c in itertools.combinations(range(6), 3):
        p1, p2, p3 = inter(segs[a], segs[b]), inter(segs[b], segs[c]), inter(segs[a], segs[c])
        if None in (p1, p2, p3) or len({p1, p2, p3}) < 3: continue
        cross = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        if cross != 0: n += 1
    return n
@chk('5:tri')
def _(): return ['%d triangles.' % _count_triangles()]
@chk('5:bounds')
def _():
    L = [n for n in range(301, 600) if sum(map(int, str(n))) == 6]; return ['%d numbers: %s.' % (len(L), ', '.join(map(str, L)))]
@chk('5:bounds:var')
def _(): return ['%d.' % len([n for n in range(201, 500) if sum(map(int, str(n))) == 5])]
@chk('5:pile')
def _():
    best = min(max(c) for c in itertools.combinations(range(1, 24), 4) if sum(c) == 23); return ['%d marbles.' % best]
@chk('5:pile:var')
def _(): return ['%d.' % min(max(c) for c in itertools.combinations(range(1, 31), 5) if sum(c) == 30)]
@chk('5:evencap')
def _(): return ['%d.' % max(sum(c) for c in itertools.combinations(range(1, 13), 6) if sum(c) % 2 == 0)]
@chk('5:evencap:var')
def _(): return ['%d.' % max(sum(c) for c in itertools.combinations(range(1, 11), 5) if sum(c) % 2 == 1)]
@chk('5:r7')
def _():
    one = 24 // (7 - 4); assert one * 3 == 24; return ['(a) %d parts' % (7 - 4), '(b) %d marbles' % one, 'Kumar %d marbles and Wei %d marbles' % (7 * one, 4 * one)]
@chk('5:r7:var')
def _(): one = 36 // 3; return ['Mei %d stickers, Siti %d stickers' % (5 * one, 2 * one)]

# ---------------- Level 6
@chk('6:rate')
def _():
    t = Fraction(60, 15 + 25); lead = 40 * Fraction(1, 2); t2 = lead / (60 - 40)
    mins = 9 * 60 + 30 + int(t2 * 60); return ['(a) %s hours.' % float(t), '(b) %d:%02d.' % (mins // 60, mins % 60)]
@chk('6:rate:var')
def _(): return ['%d hours' % (90 // (20 + 25))]
@chk('6:tele')
def _():
    s = sum(Fraction(1, n * (n + 1)) for n in range(3, 10)); return ['(a) %s' % (Fraction(1, 3) - Fraction(1, 4)), '(b) %s.' % s]
@chk('6:tele:var')
def _(): return ['%s ' % sum(Fraction(1, n * (n + 1)) for n in range(2, 8))]
@chk('6:d9')
def _():
    ns = [6372, 5481, 7296]; nine = [n for n in ns if n % 9 == 0]; three = [n for n in ns if n % 3 == 0 and n % 9]
    f = lambda L: ' and '.join('{:,}'.format(n).replace(',', ' ') for n in L); return ['(a) %s.' % f(nine), '(b) %s.' % f(three)]
@chk('6:d9:var')
def _(): return [' and '.join('{:,}'.format(n).replace(',', ' ') for n in (4536, 8127, 3705) if n % 9 == 0) + ' (']
@chk('6:d45')
def _():
    L = [int('6%d3%d' % (a, b)) for a in range(10) for b in range(10) if int('6%d3%d' % (a, b)) % 45 == 0]
    return [', '.join('{:,}'.format(n).replace(',', ' ') for n in L[:-1]) + ' and ' + '{:,}'.format(L[-1]).replace(',', ' ') + '.'] if False else ['6 030, 6 930 and 6 435.'] if sorted(L) == [6030, 6435, 6930] else ['FAIL']
@chk('6:d45:var')
def _():
    L = sorted(int('7%d2%d' % (a, b)) for a in range(10) for b in range(10) if int('7%d2%d' % (a, b)) % 45 == 0); assert L == [7020, 7425, 7920]; return ['7 020, 7 920 and 7 425.']
@chk('6:zero')
def _():
    n = 12 * 15 * 20 * 25 * 35; z = len(str(n)) - len(str(n).rstrip('0')); return ['%d zeros.' % z, '%s' % '{:,}'.format(n).replace(',', ' ')] if False else ['%d zeros.' % z]
@chk('6:zero:var')
def _():
    n = 16 * 25 * 35 * 40; z = len(str(n)) - len(str(n).rstrip('0')); return ['%d zeros' % z]
@chk('6:pct')
def _():
    first = Fraction(60) / (1 - Fraction(25, 100)); ali = 50 * Fraction(120, 100); ben = 50 * Fraction(80, 100); return ['(a) $%d.' % first, '(b) %d more' % (ali - ben)]
@chk('6:pct:var')
def _(): return ['$%d.' % (Fraction(90) / (1 - Fraction(40, 100)))]
@chk('6:pipe')
def _():
    net = 24 - 4; return ['(a) %d litres' % net, '(b) %d minutes' % (360 // net), '(c) %d minutes' % (360 // 4)]
@chk('6:pipe:var')
def _(): return ['%d minutes' % (500 // (30 - 5))]
@chk('6:short')
def _(): return ['(a) %d.' % (83 * 83 - 82 * 84), '(b) %d.' % round(0.65 * 27 + 0.65 * 73)]
@chk('6:short:var')
def _(): return ['%d and %d' % (46 * 46 - 45 * 47, round(2.4 * 35 + 2.4 * 65))]
def _votes(a, m, r, rest):
    for x in range(rest + 1):
        win = True
        for to_m in range(rest - x + 1):
            to_r = rest - x - to_m
            if not (a + x > m + to_m and a + x > r + to_r): win = False
        if win: return x
@chk('6:votes')
def _(): return ['%d more votes' % _votes(9, 7, 4, 11)]
@chk('6:votes:var')
def _(): return ['%d more votes' % _votes(12, 9, 5, 14)]
def _sure(counts, ok):
    """worst case: largest draw with no success, +1 (search over all draw vectors)"""
    best = 0
    for d in itertools.product(*[range(c + 1) for c in counts]):
        if not ok(d): best = max(best, sum(d))
    return best + 1
@chk('6:socks')
def _():
    c = (8, 6, 5); return ['(a) %d socks' % _sure(c, lambda d: max(d) >= 2), '(b) %d socks' % _sure(c, lambda d: max(d) >= 3), '(c) %d socks' % _sure(c, lambda d: d[1] >= 2)]
@chk('6:socks:var')
def _(): return ['%d pens' % _sure((7, 5, 4), lambda d: max(d) >= 2)]
def _rects(cols, rows):
    sq = rc = 0
    for x1 in range(cols + 1):
        for x2 in range(x1 + 1, cols + 1):
            for y1 in range(rows + 1):
                for y2 in range(y1 + 1, rows + 1):
                    rc += 1; sq += (x2 - x1 == y2 - y1)
    return sq, rc
@chk('6:size')
def _(): sq, rc = _rects(5, 3); return ['(a) %d squares' % sq, '(b) %d rectangles' % rc]
@chk('6:size:var')
def _(): return ['%d (' % _rects(4, 3)[0]]
@chk('6:derange')
def _():
    L = [''.join(map(str, p)) for p in itertools.permutations([1, 2, 3, 4]) if all(p[i] != i + 1 for i in range(4))]
    assert L == '2143, 2341, 2413, 3142, 3412, 3421, 4123, 4312, 4321'.split(', '); return ['%d ways' % len(L)]
@chk('6:derange:var')
def _(): return ['%d ways' % len([p for p in itertools.permutations([1, 2, 3]) if all(p[i] != i + 1 for i in range(3))])]
def _stair_perimeter(steps, w):
    pts = [(0, 0), (steps * w, 0)]
    # build the outline: up the right edge and then down the steps to the left edge
    x, y = steps * w, 0; pts = [(0, 0), (x, 0)]
    for i in range(steps):
        y += w; pts.append((x, y)); x -= w; pts.append((x, y))
    # last point (0, steps*w) closes back to (0, 0)
    assert pts[-1] == (0, steps * w)
    return sum(abs(pts[i][0] - pts[(i + 1) % len(pts)][0]) + abs(pts[i][1] - pts[(i + 1) % len(pts)][1]) for i in range(len(pts)))
@chk('6:perim')
def _(): return ['(a) %d cm' % _stair_perimeter(4, 3), '(b) %d cm' % _stair_perimeter(10, 2)]
@chk('6:perim:var')
def _(): return ['%d cm' % _stair_perimeter(6, 5)]
@chk('6:quarter')
def _(): return ['%s cm' % (100 - 3.14 * 100 / 4)]
@chk('6:quarter:var')
def _(): return ['%d cm' % round(400 - 3.14 * 400 / 4)]
def _hands(h, m):
    a = abs((h % 12) * 30 + m * 0.5 - m * 6); return min(a, 360 - a)
@chk('6:clock')
def _(): return ['(a) %d' % _hands(3, 20), '(b) %d' % _hands(4, 10)]
@chk('6:clock:var')
def _(): return ['%d' % _hands(2, 40)]
@chk('6:cr1')
def _():
    m = unique_letters(['DEC', 'EEA'], 'ACBB'); return ['D = %d, E = %d, C = %d, A = %d, B = %d' % tuple(m[c] for c in 'DECAB')]
@chk('6:cr2')
def _():
    m = unique_letters(['BDE', 'ACD'], 'ACEA'); return ['B = %d, D = %d, E = %d, A = %d, C = %d' % tuple(m[c] for c in 'BDEAC')]
@chk('6:last')
def _(): return ['(a) %d.' % pow(2, 45, 10), '(b) %d.' % pow(13, 30, 10)]
@chk('6:last:var')
def _(): return ['%d ' % pow(7, 2026, 10)]
@chk('6:pct2')
def _():
    o = 80 - 36 - 20 - 16; return ['(a) %d children' % o, '(b) %d%%' % (Fraction(36, 80) * 100), '(c) %d%%' % (Fraction(20 + o, 80) * 100)]
@chk('6:pct2:var')
def _(): t = 60 - 27 - 15 - 12; return ['%d%%' % (Fraction(t, 60) * 100)]
@chk('6:pack')
def _(): return ['%d stickers' % frob(4, 9)[0]]
@chk('6:pack:var')
def _(): return ['%d.' % frob(5, 6)[0]]

def run():
    bad = 0
    for it in gap_items.ITEMS:
        for kind, key, text in (('ans', f"{it['lv']}:{it['id']}", ' '.join(it['ans'])), ('var', f"{it['lv']}:{it['id']}:var", it['var'][1] if it.get('var') else None)):
            if text is None: continue
            f = V.get(key)
            if f is None: print('NO CHECKER', key); bad += 1; continue
            try: need = f()
            except AssertionError as e: print('ASSERT FAIL', key, e); bad += 1; continue
            miss = [x for x in need if x not in text]
            print(('OK   ' if not miss else 'FAIL ') + key + ('' if not miss else '  missing: %s | in: %s' % (miss, text))); bad += bool(miss)
    print('%d items, %d failures' % (len(gap_items.ITEMS), bad)); return bad
if __name__ == '__main__':
    sys.exit(1 if run() else 0)
