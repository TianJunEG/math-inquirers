"""Re-audit of Math Inquirers Level 4: helper arithmetic (READ-ONLY on content).
Run: python3 docs/audit/reaudit_p4.py
Prints (1) verification of answer keys re-checked in the re-audit, (2) the exact placement
probabilities of the six pretend children under the CURRENT diagnostic rule in diag/build_diag.py,
(3) cut-score noise table, (4) before/after comparisons computed from the scores typed in below.
"""
from itertools import product, permutations, combinations
from fractions import Fraction as F
from math import gcd, comb

lcm = lambda a, b: a * b // gcd(a, b)
nf = lambda n: sum(1 for d in range(1, n + 1) if n % d == 0)

def verify():
    ok = []
    ok.append(('L1 exactly-3-factors <=60', [n for n in range(1, 61) if nf(n) == 3] == [4, 9, 25, 49]))
    ok.append(('L1 bus C gap', [c for c in range(1, 200) if lcm(lcm(6, 9), c) == 36] == [4, 12, 36]))
    ok.append(('L1 remainder-1 number', [n for n in range(2, 100) if all(n % d == 1 for d in (2, 3, 4, 5, 6))] == [61]))
    ok.append(('L1 investigation (c) six pairs', [(a, b) for a in range(2, 13) for b in range(a + 1, 13) if lcm(a, b) == 12] ==
               [(2, 12), (3, 4), (3, 12), (4, 6), (4, 12), (6, 12)]))
    ok.append(('L2 digit-sum 2 numbers', len([n for n in range(10000, 100000) if sum(map(int, str(n))) == 2]) == 5))
    ok.append(('L2 digit-sum 3 count', sum(1 for n in range(10000, 100000) if sum(map(int, str(n))) == 3) == 15))
    rd = lambda n, k: (n + k // 2) // k * k
    ok.append(('L2 double rounding breaks only at 450-499', all(450 <= n % 1000 <= 499 for n in range(100000) if rd(rd(n, 100), 1000) != rd(n, 1000))))
    ok.append(('L3 1?2?3?4?5?6=7 two ways', len([s for s in product('+-', repeat=5) if eval('1%s2%s3%s4%s5%s6' % tuple(s)) == 7]) == 2))
    ok.append(('L3 12?4?5=15 unique', [(a, b) for a in '+-*/' for b in '+-*/' if abs(eval('12%s4%s5' % (a, b)) - 15) < 1e-9] == [('/', '*')]))
    ok.append(('L4 twelfths between 1/3 and 3/4', [n for n in range(1, 12) if F(1, 3) < F(n, 12) < F(3, 4)] == [5, 6, 7, 8]))
    ok.append(('L4 half = third + 3', [n for n in range(1, 100) if F(n, 2) == F(n, 3) + 3] == [18]))
    ok.append(('L5 mystery decimal 4.687', [(4000 + t * 100 + h * 10 + u) / 1000 for t in range(10) for h in range(10) for u in range(10)
               if h == t + 2 and 4 + t + h + u == 25 and 4.65 <= (4000 + t * 100 + h * 10 + u) / 1000 < 4.75] == [4.687]))
    ok.append(('L6 three-angle sets of 90 (multiples of 10)', len({tuple(sorted(t)) for t in product(range(10, 90, 10), repeat=3) if sum(t) == 90}) == 7))
    ok.append(('L7 area 40 perimeter 26', [(a, 40 // a) for a in range(1, 41) if 40 % a == 0 and 2 * (a + 40 // a) == 26] == [(5, 8), (8, 5)]))
    ok.append(('L7 24 m fence, wall', max(a * (24 - 2 * a) for a in range(1, 12)) == 72))
    cells = [(r, c) for r in range(3) for c in range(3)]
    def syms(S):
        S = set(S); n = 0
        for f in (lambda r, c: (r, 2 - c), lambda r, c: (2 - r, c), lambda r, c: (c, r), lambda r, c: (2 - c, 2 - r)):
            n += {f(*x) for x in S} == S
        return n
    ok.append(('L8 5 squares 4 lines: 2 ways', sum(1 for S in combinations(cells, 5) if syms(S) == 4) == 2))
    ok.append(('L8 2 squares up-down symmetric: 6', sum(1 for S in combinations(cells, 2) if {(r, 2 - c) for r, c in S} == set(S)) == 6))
    ok.append(('L9 four teams', [(2 * b, b, b + 10, 22) for b in range(1, 100) if 2 * b + b + (b + 10) + 22 == 100] == [(34, 17, 27, 22)]))
    ok.append(('L9 tanks meet after 4h', [h for h in range(20) if 80 - 6 * h == 20 + 9 * h] == [4]))
    ok.append(('L10 ring toss 3&5 impossible', [n for n in range(1, 21) if not any(3 * a + 5 * b == n for a in range(8) for b in range(5))] == [1, 2, 4, 7]))
    ok.append(('L10 $4 pens $7 books = $50', [(p, n) for n in range(8) for p in range(14) if 4 * p + 7 * n == 50] == [(9, 2), (2, 6)]))
    for name, v in ok:
        print(('PASS ' if v else 'FAIL ') + name)

# ------------------------------------------------------------------ diagnostic
def pb(ps):
    """exact Poisson-binomial distribution of the number correct."""
    d = [1.0]
    for p in ps:
        n = [0.0] * (len(d) + 1)
        for k, x in enumerate(d):
            n[k] += x * (1 - p); n[k + 1] += x * p
        d = n
    return d

def rule(W, M, S):
    """current rule in diag/build_diag.py (page 3): main score decides, warm-up<=2 steers down only in the 2-3 row, stretch only suggests try-up in the 4-6 row"""
    if M >= 4:
        return 'JOIN+TRYUP' if S >= 1 else 'JOIN'
    if M >= 2:
        return 'CHAT->L3' if W <= 2 else 'CHAT(L4+support)'
    return 'DOWN(L3)'

# per-question success probabilities, order: warm-up 4, main 6, stretch 2.
PROFILES = {
 '1 strong for age (P4)':      ([.97,.97,.97,.97], [.92,.92,.92,.85,.90,.90], [.55,.45], 'L4', {'JOIN','JOIN+TRYUP'}),
 '2 typical for age (P4)':     ([.90,.85,.90,.85], [.85,.85,.75,.60,.70,.80], [.12,.08], 'L4', {'JOIN','JOIN+TRYUP','CHAT(L4+support)'}),
 '3 weak for age (P4)':        ([.60,.40,.70,.50], [.30,.40,.30,.15,.25,.40], [.02,.01], 'L3', {'DOWN(L3)','CHAT->L3'}),
 '4 younger but strong (age 8-9, not yet taught)': ([.97,.95,.97,.95], [.70,.60,.35,.30,.40,.80], [.20,.10], 'L4 with support', {'JOIN','JOIN+TRYUP','CHAT(L4+support)'}),
 '5 older but weak (age 11)':  ([.60,.50,.70,.50], [.50,.50,.40,.20,.35,.55], [.03,.02], 'L3', {'DOWN(L3)','CHAT->L3'}),
 '6 rusher / guesser (able)':  ([.80,.75,.80,.75], [.55,.55,.45,.35,.40,.55], [.08,.05], 'L4', {'JOIN','JOIN+TRYUP','CHAT(L4+support)'}),
}

def diag():
    print('\n== six profiles, exact outcome probabilities under the CURRENT rule ==')
    for name, (w, m, s, right, okset) in PROFILES.items():
        dw, dm, ds = pb(w), pb(m), pb(s)
        out = {}
        for W, pw in enumerate(dw):
            for M, pm in enumerate(dm):
                for S, ps in enumerate(ds):
                    r = rule(W, M, S); out[r] = out.get(r, 0) + pw * pm * ps
        mean = sum(k * x for k, x in enumerate(dm))
        good = sum(v for k, v in out.items() if k in okset)
        print(f'{name}: expected main {mean:.2f}/6  right level={right}  P(sensible placement)={good:.0%}')
        for k in ('JOIN+TRYUP', 'JOIN', 'CHAT(L4+support)', 'CHAT->L3', 'DOWN(L3)'):
            if k in out: print(f'     {k:18s} {out[k]:.0%}')

    print('\n== cut-score noise: 6 main questions, same true p on each ==')
    print('true p | P(main>=4 join) | P(2-3 chat) | P(0-1 down)')
    for p in (.3, .4, .5, .6, .7, .8, .9):
        d = pb([p] * 6)
        print(f'{p:.1f}    | {sum(d[4:]):.0%}            | {d[2] + d[3]:.0%}        | {d[0] + d[1]:.0%}')
    print('\nlucky guessing: free response, no multiple choice -> P(guess right) ~0 per item; P(>=4 of 6 by guessing) ~ 0')
    print('\nOLD placement doc (docs/levels_and_placement.md) says 70% / 40-69% / <40% of the whole test; JSON block diag/content/p4.json "placement" says 6-8 of 8 / 4-5 / 0-3; build_diag.py ignores both')

# ------------------------------------------------------------------ scores typed in from the re-audit
CRIT = ['C1 low-floor/high-ceiling', 'C2 depth over speed', 'C3 generalisation', 'C4 justification', 'C5 multiple paths', 'C6 challenge ladder',
        'C7 student-led talk', 'C8 complexity/context', 'C9 creativity/posing', 'C10 metacognition', 'C11 pacing/compacting', 'C12 extension not acceleration']
# now (re-audit) per lesson 12 criteria
NOW = {
 1: [2,1,2,2,1,2,2,1,2,2,1,2], 2: [2,1,2,2,1,2,2,1,1,2,1,2], 3: [2,1,2,2,1,2,2,1,2,2,1,2], 4: [2,1,2,1,2,2,2,1,2,2,1,2], 5: [2,1,2,2,1,2,2,1,2,2,1,2],
 6: [2,1,1,1,1,2,2,1,2,2,1,2], 7: [2,1,2,2,2,2,2,1,1,2,1,2], 8: [2,1,2,2,1,2,2,1,2,2,1,2], 9: [2,1,1,2,1,2,2,2,2,2,1,2], 10: [2,1,1,1,2,2,2,1,2,2,1,2],
}
PERS = ['LOW', 'MIDDLE', 'HIGH']
DIM = ['participate', 'difficulty fit', 'fun', 'confidence', 'motivation', 'social/online']
JNOW = {  # lesson -> persona -> six scores
 1: {'LOW': [4,2,4,3,3,3], 'MIDDLE': [5,4,4,4,4,4], 'HIGH': [5,3,4,4,4,3]},
 2: {'LOW': [4,2,3,3,3,3], 'MIDDLE': [5,4,3,4,3,4], 'HIGH': [5,3,4,4,4,4]},
 3: {'LOW': [4,2,3,2,3,3], 'MIDDLE': [5,4,3,4,3,4], 'HIGH': [5,3,3,4,3,3]},
 4: {'LOW': [3,2,3,2,3,3], 'MIDDLE': [4,3,3,3,3,4], 'HIGH': [5,3,3,4,3,3]},
 5: {'LOW': [3,2,3,2,2,3], 'MIDDLE': [4,3,3,3,3,4], 'HIGH': [5,3,3,4,3,4]},
 6: {'LOW': [3,2,4,3,3,3], 'MIDDLE': [4,4,4,3,4,4], 'HIGH': [5,3,4,4,4,4]},
 7: {'LOW': [4,2,3,3,3,3], 'MIDDLE': [4,3,4,3,4,4], 'HIGH': [5,3,4,4,4,3]},
 8: {'LOW': [5,3,4,4,4,3], 'MIDDLE': [5,4,5,4,4,4], 'HIGH': [5,3,4,4,4,4]},
 9: {'LOW': [4,3,3,3,3,3], 'MIDDLE': [5,4,3,4,3,4], 'HIGH': [5,3,3,4,3,3]},
 10: {'LOW': [4,2,4,3,3,3], 'MIDDLE': [5,3,4,3,4,4], 'HIGH': [5,4,5,4,4,4]},
}

def scores():
    print('\n== rubric now ==')
    tot = {n: sum(v) for n, v in NOW.items()}
    for n in NOW: print(n, tot[n], NOW[n])
    print('mean', sum(tot.values()) / 10)
    print('criterion means', [round(sum(NOW[n][i] for n in NOW) / 10, 2) for i in range(12)])
    print('\n== journey now ==')
    for n in JNOW:
        print(n, {p: round(sum(JNOW[n][p]) / 6, 2) for p in PERS})
    for p in PERS:
        print(p, 'mean', round(sum(sum(JNOW[n][p]) / 6 for n in JNOW) / 10, 2),
              'dims', [round(sum(JNOW[n][p][i] for n in JNOW) / 10, 2) for i in range(6)])

if __name__ == '__main__':
    verify(); diag(); scores()
