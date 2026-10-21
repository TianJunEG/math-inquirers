#!/usr/bin/env python3
"""P3 journey review helper. Run: python3 docs/audit/journey_p3.py
Read-only. Part A verifies arithmetic claims used in the report, Part B models the diagnostic
(item probabilities are my judgement, stated below), Part C computes the heatmap from the score tables,
Part D counts the reading load of the warm-up checks."""
import json, itertools, re, os
from fractions import Fraction
from math import comb
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')

# ---------------------------------------------------------------- Part A: arithmetic checks
print('== A. Diagnostic answer key and a few content claims ==')
d = json.load(open(f'{ROOT}/diag/content/p3.json'))
chk = {}
chk['W1 47+38'] = 47 + 38 == 85
chk['W2 305-128'] = 305 - 128 == 177
chk['W3 4x8'] = 4 * 8 == 32
chk['W4 24/3'] = 24 // 3 == 8
chk['C1 2_7+358=645 -> 8'] = [a for a in range(10) if 200 + 10 * a + 7 + 358 == 645] == [8]
chk['C2 3x as many, total 48 -> 36'] = [m for m in range(49) if m == 3 * (48 - m)] == [36]
chk['C3 52/8 = 6 r 4'] = divmod(52, 8) == (6, 4)
chk['C4 3/4 = 9/12'] = Fraction(3, 4) == Fraction(9, 12)
chk['C5 9x4 = 36'] = 9 * 4 == 36
chk['C6 2:45pm + 1h50 = 4:35pm'] = (14 * 60 + 45 + 110) == 16 * 60 + 35
chk['S1 6n-4=38 -> 7'] = [n for n in range(100) if 6 * n - 4 == 38] == [7]
chk['S2 digits 2,5,8 distinct 2-digit -> 6'] = len(list(itertools.permutations([2, 5, 8], 2))) == 6
for k, v in chk.items():
    print(('OK   ' if v else 'FAIL ') + k)
# is every key answer in diag json consistent? (print for the eye)
for sec in ('foundation', 'core', 'stretch'):
    print(sec, [x['a'] for x in d[sec]])

# alternative answers a fair marker must accept (unit / rows-left-over issues)
print('Q9 alternative accepted forms: 36, 36 cm2, 36 sq cm, 36 square cm  -> the key says "36 square cm" only and the question says "with units"')

print('\n== A2. Spot checks of lesson items quoted in the report ==')
g = json.load(open(f'{ROOT}/p3/gifted.json'))
# L1 check: smallest odd number from 4,0,9,3
odd = sorted(int(''.join(p)) for p in itertools.permutations('4093') if p[0] != '0' and int(p[-1]) % 2)
print('L1 smallest odd from 4,0,9,3 =', odd[0], '(key 3049)')
# L2 check: 3A47+2865=6212
print('L2 check A =', [a for a in range(10) if int(f'3{a}47') + 2865 == 6212], '(key 3)')
# proposed easier L2 check: 2A5 + 134 = 389
print('proposed L2 check 2A5+134=389 -> A =', [a for a in range(10) if 200 + 10 * a + 5 + 134 == 389])
# proposed L2 workbook Q1(b): 5_2 - 216 = 316
print('proposed L2 Q1b 5A2-216=316 -> A =', [a for a in range(10) if 500 + 10 * a + 2 - 216 == 316])
# L3 check: 7 table among 49,54,63,74,84
print('L3 7-table members', [x for x in (49, 54, 63, 74, 84) if x % 7 == 0])
# L5 check: n/7 = 5 r 4
print('L5 check n =', 7 * 5 + 4)
# L6 check: 3/4 = ?/8
print('L6 check eighths in 3/4 =', Fraction(3, 4) * 8)
# L7 check: perimeter 14, side 3
print('L7 check area =', 3 * (14 // 2 - 3))
# L9 check
print('L9 check 2kg40g vs 2400g:', 2040, 'vs 2400; 15:50+1h25 =', divmod(15 * 60 + 50 + 85, 60))
# L9 party planner: can the pair spend exactly $20? items in cents, need >=1 food and punch bottles giving >=2 l (one 2 l bottle = 1 unit)
items = {'pizza': 890, 'wings': 650, 'puffs': 420, 'punch': 315, 'cupcakes': 575, 'balloons': 240}
sols = []
for n in itertools.product(range(0, 4), repeat=6):
    cost = sum(c * k for c, k in zip(items.values(), n))
    if cost == 2000 and n[3] >= 1 and (n[0] + n[1] + n[2] + n[4]) >= 1:
        sols.append(n)
print('L9 explore: ways to spend exactly $20 =', len(sols), sols[:3])
best = max((sum(c * k for c, k in zip(items.values(), n)), n) for n in itertools.product(range(0, 4), repeat=6)
           if sum(c * k for c, k in zip(items.values(), n)) <= 2000 and n[3] >= 1 and (n[0] + n[1] + n[2] + n[4]) >= 1)
print('   best <= $20:', best)
# L9 workbook Q3: best 3 of 5 items
pr = {'Book': 785, 'Pen set': 460, 'Puzzle': 690, 'Stickers': 235, 'Water bottle': 550}
combos = sorted(((sum(pr[k] for k in c), c) for c in itertools.combinations(pr, 3) if sum(pr[k] for k in c) <= 2000), reverse=True)
print('L9 Q3 best 3 things:', combos[0], '(key: book, pen set, puzzle $19.35)')
print('   Book+Puzzle+Water bottle =', 785 + 690 + 550)
# L10 Q6: 3-digit odd, digit sum 6, hundreds > tens, no zero
s = [n for n in range(100, 1000) if n % 2 and sum(map(int, str(n))) == 6 and '0' not in str(n) and int(str(n)[0]) > int(str(n)[1])]
print('L10 Q6 numbers:', s, '(key 411, 321, 213)')
# L5 Q4b: <50, 2-digit, r5 mod 6, r3 mod 4
print('L5 Q4b', [n for n in range(10, 50) if n % 6 == 5 and n % 4 == 3])
# L8 inv: staircase corners rule
print('L8 inv: corners = 2n+2 ->', [2 * n + 2 for n in range(1, 5)], 'n=10:', 2 * 10 + 2)
# L4 check
print('L4 check pen/book: pen =', (9 - 5) // 2)
# L7 inv: square a -> (a+1)(a-1)
print('L7 inv: area drop always', {a * a - (a + 1) * (a - 1) for a in range(2, 500)})
# L1 inv: 0,1,2,3 four-digit numbers
print('L1 inv: 4-digit numbers from 0,1,2,3 =', len([p for p in itertools.permutations('0123') if p[0] != '0']))
# L6 inv: ways to make 3/4 with 1/2,1/4,1/8
ways = [(h, q, e) for h in range(2) for q in range(4) for e in range(7) if Fraction(h, 2) + Fraction(q, 4) + Fraction(e, 8) == Fraction(3, 4)]
print('L6 inv ways for 3/4:', len(ways))
# L9 inv: 50c with 5,10,20
w = [(a, b, c) for a in range(3) for b in range(6) for c in range(11) if 20 * a + 10 * b + 5 * c == 50]
print('L9 inv ways for 50c:', len(w))

# ---------------------------------------------------------------- Part B: diagnostic model
print('\n== B. Diagnostic placement model ==')
Q = ['W1', 'W2', 'W3', 'W4', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'S1', 'S2']
# probability that the child gets each question mark (judgement; see report for the reasoning behind each)
PROFILES = {
    'A strong-for-age (9, top of P3)':            [.98, .95, .97, .98,  .92, .85, .90, .90, .88, .85,  .65, .85],
    'B typical-for-age (9, mid P3)':              [.95, .85, .92, .95,  .80, .60, .70, .70, .70, .65,  .30, .65],
    'C weak-for-age (9, struggling)':             [.85, .55, .70, .80,  .40, .15, .25, .25, .35, .30,  .05, .30],
    'D younger strong (8, end of P2, strong)':    [.97, .90, .95, .97,  .80, .45, .25, .35, .35, .55,  .40, .75],
    'E older weak (10, P4 but weak)':             [.90, .60, .80, .85,  .55, .20, .40, .40, .40, .40,  .10, .35],
    'F rusher/guesser (9, typical ability)':      [.80, .50, .80, .90,  .45, .30, .40, .45, .35, .30,  .20, .35],
}


def dist(ps):
    """Poisson-binomial distribution of the number of marks."""
    d = [1.0]
    for p in ps:
        nd = [0.0] * (len(d) + 1)
        for k, v in enumerate(d):
            nd[k] += v * (1 - p)
            nd[k + 1] += v * p
        d = nd
    return d


def place(main, warm):
    if main >= 6:
        return 'P3 (try P4 if 8/8 + warm 4/4)' if (main == 8 and warm == 4) else 'P3'
    if main >= 4:
        return 'P2 (comfort)' if warm <= 2 else 'P3 + support'
    return 'P2'


for name, ps in PROFILES.items():
    w, m = ps[:4], ps[4:]
    dm = dist(m); dw = dist(w)
    join = sum(dm[6:]); sup = sum(dm[4:6]); down = sum(dm[:4])
    # joint with warm-up for the 4-5 band
    sup_down = sum(dm[k] * sum(dw[:3]) for k in (4, 5))
    sup_ok = sum(dm[k] * sum(dw[3:]) for k in (4, 5))
    up = dm[8] * dw[4]
    exp = sum(k * v for k, v in enumerate(dm))
    print(f'{name}\n   expected main score {exp:.2f}/8  E[warm] {sum(w):.2f}/4  P(6-8 join)={join:.2f}  P(4-5)={sup:.2f} (support {sup_ok:.2f}, sent down by warm<=2 {sup_down:.2f})  P(0-3 down)={down:.2f}  P(8/8 & 4/4 try P4)={up:.3f}')
    print('   score distribution 0..8:', ' '.join(f'{x:.2f}' for x in dm))
    print(f'   P(main 0-3 AND warm-up 4/4, i.e. told to go down although the level-below skills are all there) = {sum(dm[:4])*dw[4]:.2f}')

# pure random guess (open answers): chance of a mark per main question
guess = [.10, .02, .01, .08, .02, .02, .02, .10]
dg = dist(guess)
print('pure random guesser: P(>=4 marks) = %.4f, P(>=6) = %.6f' % (sum(dg[4:]), sum(dg[6:])))

# luck: iid model on the 8 scored questions
print('\niid model, 8 scored questions: P(join >=6), P(4-5), P(<=3) by true chance p per question')
for p in (.9, .8, .75, .7, .65, .6, .5, .4, .3):
    dd = dist([p] * 8)
    print(f'  p={p:.2f}  expected {8*p:.1f}  join {sum(dd[6:]):.2f}  mid {sum(dd[4:6]):.2f}  down {sum(dd[:4]):.2f}')

# realistic ability scale: shift all main-item logits of the typical child by theta
import math
base = PROFILES['B typical-for-age (9, mid P3)'][4:]


def shift(ps, th):
    return [1 / (1 + math.exp(-(math.log(p / (1 - p)) + th))) for p in ps]


print('\nability ladder (typical child item pattern, logit shift theta):')
print(' theta  E[score]  P(join) P(mid) P(down)  P(two sittings land in different bands)')
for th in (-3, -2, -1.5, -1, -.5, 0, .5, 1, 1.5, 2, 3):
    dd = dist(shift(base, th)); bands = (sum(dd[:4]), sum(dd[4:6]), sum(dd[6:]))
    diff = 1 - sum(b * b for b in bands)
    print(f'  {th:+.1f}   {sum(k*v for k,v in enumerate(dd)):.2f}     {bands[2]:.2f}    {bands[1]:.2f}   {bands[0]:.2f}     {diff:.2f}')

# stretch items inflate? what if S2 is really core-easy: score a child who gets all 6 core wrong but S1+S2 right
print('\nchild with 0/6 core and 2/2 stretch scores 2 (down). child with 3/6 core + S2 only = 4 -> support instead of down (S2 is a one-step listing task)')

# ---------------------------------------------------------------- Part C: heatmap
print('\n== C. Journey scores ==')
DIM = ['Participate', 'Fit', 'Fun', 'Confidence', 'Motivation', 'Social']
S = {  # lesson -> persona -> six scores
    1: {'LOW': [4, 3, 4, 3, 3, 3], 'MID': [5, 4, 4, 4, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    2: {'LOW': [3, 2, 3, 2, 3, 3], 'MID': [4, 3, 4, 3, 4, 4], 'HIGH': [5, 4, 5, 4, 5, 4]},
    3: {'LOW': [2, 2, 3, 2, 3, 2], 'MID': [4, 3, 4, 4, 4, 3], 'HIGH': [5, 4, 5, 5, 5, 4]},
    4: {'LOW': [4, 3, 4, 3, 3, 3], 'MID': [5, 4, 4, 4, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    5: {'LOW': [3, 2, 3, 2, 3, 3], 'MID': [4, 3, 4, 4, 4, 4], 'HIGH': [5, 4, 4, 4, 5, 4]},
    6: {'LOW': [4, 3, 3, 3, 3, 3], 'MID': [5, 4, 4, 4, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    7: {'LOW': [3, 3, 4, 3, 3, 3], 'MID': [4, 4, 4, 4, 4, 4], 'HIGH': [5, 3, 5, 4, 5, 4]},
    8: {'LOW': [3, 2, 3, 3, 3, 3], 'MID': [4, 3, 4, 4, 4, 4], 'HIGH': [5, 4, 5, 4, 5, 4]},
    9: {'LOW': [2, 1, 3, 2, 3, 2], 'MID': [3, 3, 4, 3, 4, 3], 'HIGH': [5, 4, 5, 4, 5, 4]},
    10: {'LOW': [4, 3, 4, 4, 4, 3], 'MID': [5, 4, 5, 4, 5, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
}
cells = []
print('Lesson |  LOW  | MIDDLE | HIGH | lesson mean')
for n in range(1, 11):
    ms = {k: sum(v) / 6 for k, v in S[n].items()}
    cells += [(ms[k], n, k) for k in ms]
    print(f'  L{n:<2}  | {ms["LOW"]:.2f}  | {ms["MID"]:.2f}   | {ms["HIGH"]:.2f} | {sum(ms.values())/3:.2f}')
for k in ('LOW', 'MID', 'HIGH'):
    print(k, 'mean over lessons: %.2f' % (sum(sum(S[n][k]) / 6 for n in S) / 10),
          '| per dimension:', {DIM[i]: round(sum(S[n][k][i] for n in S) / 10, 2) for i in range(6)})
cells.sort()
print('weakest 5:', [(round(a, 2), f'L{n}', k) for a, n, k in cells[:5]])
print('strongest 3:', [(round(a, 2), f'L{n}', k) for a, n, k in cells[-3:][::-1]])

# ---------------------------------------------------------------- Part D: warm-up check reading load
print('\n== D. Warm-up check (minute 2 to 5): words per question and who can start ==')
for n in range(1, 11):
    c = g[str(n)]['check']
    wds = [len(re.findall(r"[A-Za-z0-9$¢']+", re.sub(r'\[\[.*?\]\]', 'f', x['q']))) for x in c]
    print(f'  L{n}: words {wds}')

# ---------------------------------------------------------------- Part E: proposed replacements and a revised rule
print('\n== E. Proposed changes ==')
nums = [10 * a + b for a in (2, 5, 8, 0) for b in (2, 5, 8, 0) if a != b and a != 0]
print('proposed S2 (digits 2,5,8,0; no leading 0; different digits):', len(nums), sorted(nums))
print('current S2 (2,5,8):', len([1 for a in (2, 5, 8) for b in (2, 5, 8) if a != b]))
print('alt stretch "7 table, 40-60, digit sum 11":', [n for n in range(40, 61) if n % 7 == 0 and sum(map(int, str(n))) == 11])
print('L9 Q3 rounding check: 8 + 7 + 6 = 21 (rounded) shows book+puzzle+bottle is over $20 only just; exact total 20.25')


def place2(main, warm):
    if main >= 6: return 'join'
    if main >= 4: return 'join+support' if warm >= 3 else 'chat (P2 option)'
    return 'P3 with tutor chat' if warm == 4 else 'P2'


def place1(main, warm):
    if main >= 6: return 'join'
    if main >= 4: return 'join+support' if warm >= 3 else 'P2 option'
    return 'P2'


print('profile: current rule P(P2 recommended outright) vs revised rule P(P2 recommended outright)')
for name, ps in PROFILES.items():
    dw = dist(ps[:4]); dm = dist(ps[4:])
    cur = sum(dm[m] * dw[w] for m in range(9) for w in range(5) if place1(m, w) == 'P2')
    new = sum(dm[m] * dw[w] for m in range(9) for w in range(5) if place2(m, w) == 'P2')
    print(f'  {name}: current {cur:.2f}  revised {new:.2f}')
