"""Helper for docs/audit/journey_p5.md. Read-only analysis: prints the numbers quoted in the report.
Run:  python3 -I docs/audit/journey_p5.py
Part 1 holds the reviewer's 1-5 scores (judgements, each justified in the report) and computes the heatmap.
Part 2 re-verifies the P5 diagnostic arithmetic and computes placement probabilities (exact, no random numbers).
"""
from fractions import Fraction as F

# ---------------------------------------------------------------- PART 1
# order of the six scores: Participate, Fit(raw: 3 = just right, <3 too hard, >3 too easy), Fun, Confidence, Motivation, Social/online
S = {
 1: {'L': (3, 2, 3, 3, 3, 3), 'M': (4, 3, 4, 4, 4, 4), 'H': (5, 4, 3, 4, 3, 3)},
 2: {'L': (3, 2, 3, 2, 2, 3), 'M': (4, 3, 4, 3, 4, 4), 'H': (4, 4, 4, 4, 4, 3)},
 3: {'L': (2, 1, 3, 2, 2, 2), 'M': (3, 2, 3, 3, 3, 4), 'H': (4, 3, 4, 4, 4, 3)},
 4: {'L': (4, 2, 4, 4, 3, 3), 'M': (5, 3, 5, 4, 4, 4), 'H': (4, 4, 4, 4, 4, 3)},
 5: {'L': (3, 2, 4, 3, 3, 2), 'M': (4, 3, 5, 4, 4, 3), 'H': (5, 4, 4, 4, 4, 3)},
 6: {'L': (3, 1, 3, 2, 2, 2), 'M': (4, 2, 4, 3, 4, 4), 'H': (5, 4, 4, 4, 4, 3)},
 7: {'L': (4, 2, 4, 3, 4, 3), 'M': (5, 3, 5, 4, 5, 4), 'H': (5, 4, 4, 4, 4, 3)},
 8: {'L': (3, 2, 3, 3, 2, 3), 'M': (4, 3, 4, 4, 3, 4), 'H': (4, 4, 5, 5, 4, 3)},
 9: {'L': (4, 2, 4, 3, 3, 3), 'M': (4, 3, 4, 4, 4, 4), 'H': (5, 4, 5, 5, 5, 3)},
 10: {'L': (3, 2, 4, 3, 3, 2), 'M': (4, 3, 5, 4, 4, 3), 'H': (4, 3, 5, 4, 5, 3)},
}
TITLES = {1: 'Million Puzzles', 2: 'Fraction Feats', 3: 'Before and After', 4: 'Triangle Areas', 5: 'Volume Vault',
          6: 'Rate Racers', 7: 'Percentage Puzzles', 8: 'Angle Chasers', 9: 'Pattern Generalisers', 10: 'Challenge Day'}


def fitq(f):  # fit quality for averaging: 3 (just right) -> 5, 2 or 4 -> 3, 1 or 5 -> 1
    return 5 - 2 * abs(f - 3)


def mean6(t):
    return (t[0] + fitq(t[1]) + t[2] + t[3] + t[4] + t[5]) / 6


print('PART 1 heatmap (mean of six scores; Fit converted to fit quality)')
cells = []
print('Lesson | LOW | MIDDLE | HIGH | lesson mean')
for n in range(1, 11):
    m = {k: mean6(S[n][k]) for k in 'LMH'}
    for k in 'LMH':
        cells.append((m[k], n, k))
    print(n, TITLES[n], *['%.2f' % m[k] for k in 'LMH'], '%.2f' % (sum(m.values()) / 3))
for k, nm in zip('LMH', ['LOW', 'MIDDLE', 'HIGH']):
    print(nm, 'level mean %.2f' % (sum(mean6(S[n][k]) for n in S) / 10),
          ' per dimension:', ['%.2f' % (sum((S[n][k][i] if i != 1 else fitq(S[n][k][1])) for n in S) / 10) for i in range(6)])
print('weakest 8 cells:', [('L%d-%s' % (n, k), round(v, 2)) for v, n, k in sorted(cells)[:8]])
print('strongest 5 cells:', [('L%d-%s' % (n, k), round(v, 2)) for v, n, k in sorted(cells, reverse=True)[:5]])

# Timetable facts from the deck title notes (identical for lessons 1-9; lesson 10 has certificates at 88-90)
T = dict(check=(0, 3), warm=(3, 9), explore=(9, 21), teach=(21, 33), brk=(33, 37), ws1=(37, 49), chk1=(49, 51),
         teach2=(51, 57), ws2=(57, 72), chk2=(72, 76), talk=(76, 82), exit=(82, 90))
print('\nDeck timetable minutes:', {k: v[1] - v[0] for k, v in T.items()}, 'sum', sum(v[1] - v[0] for v in T.values()))
print('Worksheet working time (pages 1+2):', (T['ws1'][1] - T['ws1'][0]) + (T['ws2'][1] - T['ws2'][0]), 'min; check-together time:',
      (T['chk1'][1] - T['chk1'][0]) + (T['chk2'][1] - T['chk2'][0]), 'min')
# Tutor-guide timetable (p5/guide.js): worksheet 40-70 = pairs 40-52, alone 52-62, stretch/challenge 62-70; talk 70-80; exit 80-90
print('Guide timetable: page 2 alone = 10 min (52-62) vs deck 15 min (57-72); talk 70-80 (10 min) vs deck 76-82 (6 min)')
# HIGH child, passes the check: minutes spent on material already shown mastered (estimate)
passive = {'quick Qs in warm-up (6-9)': 3, 'mini-lesson teach1/try/we (21-33), about two thirds': 8, 'ws1 answers (49-51)': 2,
           'teach before page 2 (51-57), about 5': 5, 'ws2 answers (72-76), about 3': 3, 'exit ticket + reflection wait (82-90), about 4': 4}
print('HIGH low-demand minutes (estimate):', sum(passive.values()), passive)

# ---------------------------------------------------------------- PART 2
print('\nPART 2')
print('Answer checks: W1', F(5, 6) - F(1, 3), '| W2', F(24, 10) / 6, '| W3', 24 * 35, '| W4 width', 36 // 2 - 11, 'area', (36 // 2 - 11) * 11)
print('M1', round(4386512, -5), '| M2 total', F(24) / (F(3, 5) * F(2, 3)), '| M3', F(2 * 40, 16), '| M4', F(50 * 30 * 40, 1000) / 6,
      '| M5', F(40) * F(6, 10) * F(1, 4), '| M6', 360 - 90 - 110 - 75, '| S1', [n * n + 1 for n in range(1, 11)][-1],
      '| S2', [(3 * b, b) for b in range(1, 1000) if 3 * b - 18 == 2 * (b + 18)])
# common-error values quoted in the tutor key
print('error values: W1 4/3?', F(5 - 1, 6 - 3), '| W4 wrong width 36-22 =', 36 - 22, '| M5 25% of 40 =', 40 * 25 // 100, '| M2 1/3 of whole + 2/5 =',
      F(2, 5) + F(1, 3), 'left', 1 - F(2, 5) - F(1, 3))
print('Isosceles replacement for M6: AB=AC, A=50 -> B =', (180 - 50) // 2)
print('W3 replacement 3/4 of 48 =', 48 * 3 // 4)


def pb(ps):  # Poisson-binomial distribution of the number correct
    d = [1.0]
    for p in ps:
        n = [0.0] * (len(d) + 1)
        for i, v in enumerate(d):
            n[i] += v * (1 - p)
            n[i + 1] += v * p
        d = n
    return d


print('\n8 equally hard items, per-item chance p: P(6-8), P(4-5), P(0-3), P(same band on two sittings)')
for p in [.3, .4, .5, .55, .6, .65, .7, .75, .8, .85, .9]:
    d = pb([p] * 8)
    b = (sum(d[6:]), sum(d[4:6]), sum(d[:4]))
    print(p, [round(x, 3) for x in b], round(sum(x * x for x in b), 3), ' SE of score = %.2f marks' % (8 * p * (1 - p)) ** .5)
# pure guessing on open-answer items
for g in (.02, .05):
    d = pb([g] * 8)
    print('pure guessing, chance %.2f per item: P(>=6)=%.2e P(>=4)=%.2e P(>=1)=%.3f' % (g, sum(d[6:]), sum(d[4:]), 1 - d[0]))

# per-question chance of a correct answer (ASSUMPTIONS, see report): W1-W4, M1-M6, S1-S2
PROF = {
    'Strong for age (P5, about 11, top 15%)':   [.98, .97, .99, .93, .97, .90, .92, .88, .93, .70, .55, .45],
    'Typical for age (P5, about 11)':           [.85, .80, .92, .65, .75, .50, .65, .50, .70, .35, .18, .07],
    'Weak for age (P5, about 11)':              [.55, .50, .80, .30, .50, .15, .30, .15, .40, .15, .03, .01],
    'Younger and strong (9-10, finished P4)':   [.97, .95, .98, .90, .85, .60, .25, .20, .40, .35, .30, .15],
    'Older and weak (12, past P5)':             [.60, .55, .85, .35, .60, .20, .50, .30, .55, .35, .04, .01],
    'Guesser / rusher (typical ability)':       [.60, .70, .85, .35, .50, .25, .45, .25, .35, .50, .08, .03],
}
M6NEW = {'Strong for age (P5, about 11, top 15%)': .93, 'Typical for age (P5, about 11)': .65, 'Weak for age (P5, about 11)': .35,
         'Younger and strong (9-10, finished P4)': .50, 'Older and weak (12, past P5)': .50, 'Guesser / rusher (typical ability)': .45}


def r1(w, m, s):  # current rule on main + stretch out of 8
    sc = m + s
    if sc >= 6:
        return 'P5 + try P6 check' if (sc == 8 and w == 4) else 'P5'
    if sc >= 4:
        return 'P5 with support, or P4 (warm-up <= 2)' if w <= 2 else 'P5 with support'
    return 'P4'


def r2(w, m, s):  # proposed rule on main out of 6; stretch is a flag only
    if m >= 5:
        return 'P5 + try P6 check' if (m == 6 and w == 4 and s >= 1) else 'P5'
    if m >= 3:
        return 'P5 with support, or P4 (warm-up <= 2)' if w <= 2 else 'P5 with support'
    return 'tutor chat first (warm-up 3-4)' if w >= 3 else 'P4'


def outcomes(ps, rule):
    dw, dm, ds = pb(ps[:4]), pb(ps[4:10]), pb(ps[10:])
    out = {}
    for w, a in enumerate(dw):
        for m, b in enumerate(dm):
            for s, c in enumerate(ds):
                k = rule(w, m, s)
                out[k] = out.get(k, 0) + a * b * c
    return out


def fmt(o):
    return ', '.join('%s %d%%' % (k, round(100 * v)) for k, v in sorted(o.items(), key=lambda x: -x[1]) if v >= .005)


for name, ps in PROF.items():
    dw, dm, ds = pb(ps[:4]), pb(ps[4:10]), pb(ps[10:])
    E = lambda d: sum(i * v for i, v in enumerate(d))
    tot = pb(ps[4:])
    print('\n' + name, '| expected warm %.1f/4, main %.1f/6, stretch %.1f/2, score/8 %.1f' % (E(dw), E(dm), E(ds), E(tot)))
    print('  score/8 distribution:', [round(x, 2) for x in tot])
    print('  CURRENT rule + current items :', fmt(outcomes(ps, r1)))
    ps2 = ps[:9] + [M6NEW[name]] + ps[10:]
    print('  current rule + new M6        :', fmt(outcomes(ps2, r1)))
    print('  PROPOSED rule + new M6       :', fmt(outcomes(ps2, r2)))
