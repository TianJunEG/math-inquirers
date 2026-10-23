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
