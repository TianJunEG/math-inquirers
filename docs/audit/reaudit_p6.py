"""Helper for docs/audit/reaudit_p6.md (Level 6 re-audit). Pure arithmetic on the blind scores recorded in Phase 1.
Run: python3 docs/audit/reaudit_p6.py   (prints tables; changes no content)."""
from fractions import Fraction
from itertools import permutations
from math import comb

CRIT = ['LFHC', 'Depth', 'General', 'Justify', 'MultiPath', 'Ladder', 'Inquiry', 'Complex', 'Posing', 'Metacog', 'Pacing', 'Beyond']
# Phase 1 (blind) rubric scores, current material.  Order as CRIT.
NOW = {
    1: [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1],
    2: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
    3: [2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1],
    4: [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1],
    5: [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2],
    6: [2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2],
    7: [2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1],
    8: [2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2],
    9: [2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
    10: [2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2],
}
# Phase 1 (blind) journey scores [participate, difficulty fit, fun, confidence, motivation, social/online]
J = {
    'LOW': {1: [4, 2, 3, 3, 3, 3], 2: [4, 2, 3, 3, 3, 4], 3: [5, 3, 4, 4, 3, 4], 4: [5, 2, 4, 3, 3, 4], 5: [5, 3, 4, 4, 3, 4],
            6: [4, 2, 5, 3, 4, 4], 7: [3, 1, 3, 2, 2, 3], 8: [4, 2, 4, 3, 3, 3], 9: [5, 3, 3, 4, 3, 4], 10: [3, 2, 3, 3, 3, 3]},
    'MIDDLE': {1: [5, 4, 4, 4, 4, 4], 2: [5, 3, 4, 4, 4, 4], 3: [5, 4, 4, 4, 4, 4], 4: [5, 4, 4, 4, 4, 4], 5: [5, 4, 5, 4, 4, 4],
               6: [5, 3, 5, 4, 4, 4], 7: [4, 2, 4, 3, 3, 4], 8: [5, 3, 5, 4, 4, 4], 9: [5, 4, 4, 4, 4, 4], 10: [4, 3, 4, 4, 4, 3]},
    'HIGH': {1: [5, 4, 4, 4, 4, 4], 2: [5, 4, 4, 4, 5, 4], 3: [5, 3, 4, 4, 4, 4], 4: [5, 4, 5, 4, 5, 4], 5: [5, 4, 5, 4, 5, 4],
             6: [5, 4, 5, 4, 5, 4], 7: [5, 3, 5, 4, 5, 4], 8: [5, 4, 5, 4, 5, 4], 9: [5, 4, 4, 4, 4, 4], 10: [5, 4, 5, 4, 5, 4]},
}
DIM = ['participate', 'difficulty fit', 'fun', 'confidence', 'motivation', 'social/online']

# Tier compliance, current material (items classed in the .md; half credit for 'partial').
# qbank: core 6/lesson, think harder (stretch) 8/lesson, challenge 9/lesson
QB = {'core': (60, 58.5), 'think': (80, 80), 'challenge': (90, 85)}
# printed workbook: Start here (Core), Think harder page, Go further (Challenge): (items, compliant credit)
WB_START = {1: (6, 2.5), 2: (6, 4.5), 3: (7, 6), 4: (7, 6), 5: (6, 5), 6: (5, 3), 7: (5, 1), 8: (5, 3), 9: (6, 4.5), 10: (6, 3.5)}
WB = {'start': (59, sum(v[1] for v in WB_START.values())), 'think': (40, 38.5), 'go': (30, 30)}


def tot(d):
    return {k: sum(v) for k, v in d.items()}


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs)


def report_rubric():
    print('RUBRIC NOW')
    for n, v in NOW.items():
        print(n, sum(v), dict(zip(CRIT, v)))
    print('level mean', round(mean(sum(v) for v in NOW.values()), 2))
    print('criterion means', {c: round(mean(NOW[n][i] for n in NOW), 2) for i, c in enumerate(CRIT)})


def report_journey():
    for p, d in J.items():
        print(p, {n: round(mean(v), 2) for n, v in d.items()}, 'mean', round(mean(mean(v) for v in d.values()), 2))
        print('  dims', {DIM[i]: round(mean(d[n][i] for n in d), 2) for i in range(6)})
    print('all personas mean', round(mean(mean(mean(v) for v in d.values()) for d in J.values()), 2))
    lowfirst = {n: mean(J['LOW'][n]) for n in J['LOW']}
    print('weakest cells', sorted(((round(mean(J[p][n]), 2), p, n) for p in J for n in J[p]))[:6])


def report_tiers():
    qa = sum(v[0] for v in QB.values()); qb = sum(v[1] for v in QB.values())
    wa = sum(v[0] for v in WB.values()); wb = sum(v[1] for v in WB.values())
    print('qbank', qb, '/', qa, round(100 * qb / qa, 1), '%  per tier', {k: round(100 * v[1] / v[0], 1) for k, v in QB.items()})
    print('workbook', wb, '/', wa, round(100 * wb / wa, 1), '%  per tier', {k: round(100 * v[1] / v[0], 1) for k, v in WB.items()})
    print('all', round(100 * (qb + wb) / (qa + wa), 1))


# ---------------- diagnostic ----------------
# answers re-derived from the question text in diag/content/p6.json
def diag_checks():
    assert sorted(d for d in range(1, 25) if 24 % d == 0) == [1, 2, 3, 4, 6, 8, 12, 24]
    assert Fraction(6, 36) == Fraction(1, 6)
    assert 180 - 52 - 63 == 65
    n = 5
    for _ in range(4):
        n += 3
    assert n == 17
    assert [x for x in range(1, 25) if 2 * x + 5 == 31] == [13]
    pr = [x for x in range(30, 51) if x > 1 and all(x % d for d in range(2, x))]
    assert pr == [31, 37, 41, 43, 47] and len(pr) == 5
    assert -4 + 9 - 12 == -7
    assert Fraction(4 + 3, 12) == Fraction(7, 12)
    assert 5 * 12 - (8 + 10 + 15 + 11) == 16
    assert (10 + 17) % 12 == 3
    assert 4 + 3 * 49 == 151
    nums = [a * 100 + b * 10 + c for a, b, c in permutations([1, 2, 3, 4], 3) if c % 2 == 0]
    assert len(nums) == 12
    print('diagnostic key: all 12 answers verified')


def place_cur(main, warm):
    """Rule in diag/build_diag.py (page 3): decided by Main questions only; warm-up only tweaks the 2-3 band."""
    if main >= 4:
        return 'JOIN L6'
    if main >= 2:
        return 'CHAT + L6 with support' + ('; L5 may be more comfortable (warm-up<=2)' if warm <= 2 else '')
    return 'suggest L5'


# six pretend children: per-item success probability (warm-up W1..W4, main M5..M10, stretch S11..S12)
PROFILES = {
    'strong for age (12, AL1-2)': ([.97, .97, .95, .9], [.9, .9, .9, .95, .93, .85], [.6, .5], 'JOIN L6'),
    'typical for age (12)': ([.85, .8, .8, .6], [.7, .6, .75, .7, .75, .5], [.15, .1], 'JOIN L6'),
    'weak for age (12)': ([.35, .45, .5, .3], [.2, .25, .4, .35, .3, .15], [.02, .02], 'L5 or L6 with support'),
    'younger but strong (10)': ([.9, .85, .7, .6], [.8, .75, .7, .7, .3, .6], [.35, .3], 'JOIN L6 (maybe)'),
    'older but weak (13)': ([.45, .5, .55, .3], [.3, .3, .5, .45, .4, .2], [.03, .03], 'L5 content, but age 13'),
    'guesses / rushes (capable)': ([.4, .35, .75, .3], [.35, .3, .3, .45, .35, .25], [.1, .1], 'JOIN L6'),
}


def dist(ps):
    d = {0: 1.0}
    for p in ps:
        nd = {}
        for k, v in d.items():
            nd[k] = nd.get(k, 0) + v * (1 - p)
            nd[k + 1] = nd.get(k + 1, 0) + v * p
        d = nd
    return d


def report_diag():
    diag_checks()
    for name, (w, m, s, right) in PROFILES.items():
        dm = dist(m); dw = dist(w)
        join = sum(v for k, v in dm.items() if k >= 4); chat = sum(v for k, v in dm.items() if 2 <= k <= 3); down = sum(v for k, v in dm.items() if k <= 1)
        em = sum(p for p in m); ew = sum(w)
        print(f'{name}: expected warm {ew:.1f}, main {em:.1f}; modal result -> {place_cur(round(em), round(ew))}; P(join)={join:.2f} P(chat)={chat:.2f} P(down)={down:.2f}; right level: {right}')
    print('binomial noise (6 main items, true per-item rate p):')
    for p in [.2, .4, .5, .6, .7, .8, .9]:
        pm = lambda k: comb(6, k) * p ** k * (1 - p) ** (6 - k)
        print(p, 'down', round(pm(0) + pm(1), 3), 'chat', round(pm(2) + pm(3), 3), 'join', round(sum(pm(k) for k in range(4, 7)), 3))


if __name__ == '__main__':
    report_rubric(); print(); report_journey(); print(); report_tiers(); print(); report_diag()
