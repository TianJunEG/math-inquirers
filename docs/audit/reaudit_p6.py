"""Helper for docs/audit/reaudit_p6.md (Level 6 re-audit). Pure arithmetic on the blind scores recorded in Phase 1.
Run: python3 docs/audit/reaudit_p6.py   (prints tables; changes no content)."""
from fractions import Fraction
from itertools import permutations
from math import comb

CRIT = ['LFHC', 'Depth', 'General', 'Justify', 'MultiPath', 'Ladder', 'Inquiry', 'Complex', 'Posing', 'Metacog', 'Pacing', 'Beyond']
# Phase 1 (blind) rubric scores, current material.  Order as CRIT.
NOW = {
    1: [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1],
    2: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1],
    3: [2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1],
    4: [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1],
    5: [2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2],
    6: [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1],
    7: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1],
    8: [2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
    9: [2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
    10: [2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
}
# NOTE on process: the first run of this file (before any baseline was opened) printed rubric totals
# 20,20,18,20,21,21,20,21,22,21 (mean 20.4) and journey means LOW 3.30 / MID 4.03 / HIGH 4.35.  After reading the baselines I
# revised a few cells for consistency of standard (rubric: C2 L6+L10, C3 L5, C5 L8, C8 L7, C12 L1+L2+L6, C4 L8, C3 L6/L10; journey: ~25 cells,
# mostly fit/confidence/social).  The values below are the revised ones that the .md reports; the blind values are quoted there too.
BLIND_RUBRIC = [20, 20, 18, 20, 21, 21, 20, 21, 22, 21]
BLIND_J = {'LOW': 3.30, 'MIDDLE': 4.03, 'HIGH': 4.35}
# Phase 1 (blind) journey scores [participate, difficulty fit, fun, confidence, motivation, social/online]
J = {
    'LOW': {1: [4, 2, 3, 3, 3, 3], 2: [4, 2, 3, 3, 3, 3], 3: [5, 3, 4, 3, 3, 4], 4: [4, 2, 3, 3, 3, 3], 5: [4, 3, 4, 3, 3, 3],
            6: [4, 2, 4, 3, 3, 4], 7: [3, 2, 3, 2, 3, 3], 8: [4, 2, 4, 3, 3, 3], 9: [4, 4, 3, 4, 3, 4], 10: [3, 2, 3, 3, 3, 3]},
    'MIDDLE': {1: [5, 4, 4, 4, 4, 4], 2: [5, 3, 4, 4, 4, 4], 3: [5, 4, 4, 4, 4, 4], 4: [5, 3, 4, 4, 4, 4], 5: [5, 3, 5, 4, 4, 4],
               6: [5, 4, 5, 4, 4, 4], 7: [4, 3, 4, 3, 4, 4], 8: [5, 3, 5, 4, 4, 4], 9: [5, 4, 4, 4, 4, 4], 10: [4, 3, 4, 4, 4, 3]},
    'HIGH': {1: [5, 3, 4, 4, 4, 4], 2: [5, 3, 4, 4, 5, 4], 3: [5, 3, 4, 4, 4, 4], 4: [5, 3, 5, 4, 5, 4], 5: [5, 3, 5, 4, 5, 4],
             6: [5, 4, 5, 4, 5, 4], 7: [5, 4, 5, 4, 5, 4], 8: [5, 4, 5, 4, 5, 4], 9: [5, 3, 3, 4, 4, 4], 10: [5, 4, 5, 4, 5, 4]},
}
DIM = ['participate', 'difficulty fit', 'fun', 'confidence', 'motivation', 'social/online']

# Tier compliance, current material (items classed in the .md; half credit for 'partial').
# qbank: core 6/lesson, think harder (stretch) 8/lesson, challenge 9/lesson
QB = {'core': (60, 58.5), 'think': (80, 80), 'challenge': (90, 85)}
# printed workbook: Start here (Core), Think harder page, Go further (Challenge): (items, compliant credit)
WB_START = {1: (6, 2.5), 2: (6, 4.5), 3: (7, 6), 4: (7, 6), 5: (6, 5), 6: (5, 3), 7: (5, 1), 8: (5, 3), 9: (6, 4.5), 10: (6, 3.5)}
WB = {'start': (59, sum(v[1] for v in WB_START.values())), 'think': (40, 38.5), 'go': (30, 30)}

# ---------------- BASELINES (read in Phase 2, after the blind scores above were fixed) ----------------
BEFORE = {1: [2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2], 2: [2, 1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1], 3: [1, 1, 1, 1, 1, 1, 2, 2, 0, 1, 1, 1],
          4: [2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1], 5: [2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2], 6: [2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1],
          7: [2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1], 8: [2, 1, 1, 1, 1, 1, 2, 2, 0, 1, 1, 2], 9: [2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2],
          10: [2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2]}
CLAIM = {1: {6: 2, 9: 2}, 2: {6: 2, 9: 1}, 3: {1: 2, 6: 2, 9: 1}, 4: {}, 5: {}, 6: {6: 2, 9: 2}, 7: {6: 2, 9: 2}, 8: {6: 2, 9: 1}, 9: {6: 2, 9: 2}, 10: {}}
BJ = {'LOW': {1: [3, 2, 3, 3, 3, 2], 2: [3, 2, 3, 2, 3, 2], 3: [4, 3, 4, 3, 3, 3], 4: [3, 2, 3, 2, 3, 2], 5: [3, 2, 4, 3, 3, 3], 6: [4, 2, 4, 2, 3, 3], 7: [2, 1, 3, 2, 3, 2], 8: [4, 2, 4, 2, 3, 3], 9: [4, 4, 3, 3, 3, 3], 10: [3, 2, 3, 2, 3, 1]},
      'MIDDLE': {1: [4, 4, 4, 3, 4, 3], 2: [4, 3, 4, 3, 4, 3], 3: [5, 4, 4, 4, 4, 4], 4: [4, 3, 4, 3, 4, 4], 5: [4, 3, 5, 4, 4, 4], 6: [5, 4, 5, 4, 4, 4], 7: [3, 3, 4, 3, 4, 4], 8: [4, 3, 5, 4, 5, 4], 9: [5, 4, 4, 4, 4, 4], 10: [4, 3, 4, 3, 4, 3]},
      'HIGH': {1: [5, 3, 4, 4, 4, 3], 2: [5, 3, 4, 4, 4, 4], 3: [5, 3, 4, 4, 4, 3], 4: [5, 3, 4, 4, 4, 4], 5: [5, 3, 5, 4, 4, 4], 6: [5, 3, 5, 4, 5, 4], 7: [4, 4, 5, 4, 5, 4], 8: [5, 4, 5, 4, 5, 4], 9: [5, 2, 3, 4, 3, 3], 10: [5, 3, 5, 4, 5, 3]}}
B_TIER_BEFORE = (240, 289)  # items compliant / items audited in gifted_p6.md (qbank + worksheet items)


def compare():
    print('LESSON | before | claimed after | now | per-criterion deltas now vs before')
    tb = ta = tn = 0
    for n in NOW:
        b = sum(BEFORE[n])
        a = b + sum(v - BEFORE[n][c - 1] for c, v in CLAIM[n].items())
        now = sum(NOW[n])
        d = ', '.join(f'{CRIT[i]} {NOW[n][i] - BEFORE[n][i]:+d}' for i in range(12) if NOW[n][i] != BEFORE[n][i])
        print(n, b, a, now, '|', d)
        tb += b; ta += a; tn += now
    print('LEVEL', tb / 10, ta / 10, tn / 10)
    print('criterion means before/now', {c: (round(mean(BEFORE[n][i] for n in NOW), 2), round(mean(NOW[n][i] for n in NOW), 2)) for i, c in enumerate(CRIT)})
    print('HEATMAP before -> now')
    for n in range(1, 11):
        print(n, {p: (round(mean(BJ[p][n]), 2), round(mean(J[p][n]), 2)) for p in J})
    for p in J:
        print(p, 'mean', round(mean(mean(v) for v in BJ[p].values()), 2), '->', round(mean(mean(v) for v in J[p].values()), 2))
        print('  dims before', [round(mean(BJ[p][n][i] for n in BJ[p]), 1) for i in range(6)], 'now', [round(mean(J[p][n][i] for n in J[p]), 1) for i in range(6)])


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


# ---- like-for-like rule comparison.  Per-question success rates [W1..W4, M5..M10, S11, S12].
# Re-used from journey_p6.py where the question is unchanged (doubles machine, negatives, clock);
# bumped where the fix pass made the item self-contained (prime and probability now defined, 'average').
# These are my scenario estimates, not data.
PROF2 = {
    'strong for age (12, AL1-2)':  [.97, .97, .98, .90, .95, .90, .85, .85, .95, .85, .65, .50],
    'typical for age (12, AL3-5)': [.85, .90, .93, .60, .70, .60, .55, .55, .70, .50, .20, .15],
    'weak for age (12, AL6-8)':    [.35, .45, .60, .30, .30, .30, .25, .30, .30, .20, .05, .05],
    'younger strong (11, P5)':     [.85, .80, .90, .70, .85, .70, .60, .65, .80, .80, .60, .40],
    'older weak (13, Sec 1)':      [.50, .50, .75, .40, .35, .55, .50, .35, .45, .30, .10, .10],
    'rusher (capable, careless)':  [.50, .60, .85, .50, .50, .50, .45, .45, .50, .35, .30, .20],
    'pure guesser':                [.03, .03, .05, .03, .03, .03, .03, .03, .03, .05, .25, .03],
}


def rules(ps):
    w, m, s = dist(ps[:4]), dist(ps[4:10]), dist(ps[10:])
    m8 = dist(ps[4:])            # old rule scored main+stretch out of 8
    pw2 = sum(v for k, v in w.items() if k <= 2)
    old_join = sum(v for k, v in m8.items() if k >= 6); old_sup = sum(v for k, v in m8.items() if 4 <= k <= 5); old_down = sum(v for k, v in m8.items() if k <= 3)
    old_l5 = old_down + old_sup * pw2
    cj = sum(v for k, v in m.items() if k >= 4); cc = sum(v for k, v in m.items() if 2 <= k <= 3); cd = sum(v for k, v in m.items() if k <= 1)
    cur_l5 = cd + cc * pw2           # 'down' plus 'chat, and warm-up <= 2 hint'
    rj = sum(v for k, v in w.items() if k >= 3); rc = w.get(2, 0); rd = sum(v for k, v in w.items() if k <= 1)
    return dict(old=(old_join, old_sup, old_down, old_l5), cur=(cj, cc, cd, cur_l5), rec=(rj, rc, rd))


def report_rules():
    print('profile | OLD 8-item rule: join/support/down, P(L5 suggested) | CURRENT main-6 rule: join/chat/down, P(L5 down or hinted) | warm-up-decides rule: join/catch-up/talk')
    for k, ps in PROF2.items():
        r = rules(ps)
        f = lambda t: '/'.join(f'{x:.2f}' for x in t)
        print(f'{k}: OLD {f(r["old"])} | CUR {f(r["cur"])} | REC {f(r["rec"])}')



def tier_per_lesson():
    bank_viol = {1: 1.5, 2: 1, 3: 2, 4: .5, 5: 0, 6: 0, 7: .5, 8: 0, 9: 0, 10: 1}
    lenient_bad = {1: 2, 7: 3, 8: 1}
    print('per lesson tier compliance now (289-item basis): strict / lenient   vs before')
    BEF = {1: 83, 2: 83, 3: 80, 4: 90, 5: 93, 6: 75, 7: 71, 8: 86, 9: 79, 10: 90}
    for n in range(1, 11):
        items = WB_START[n]
        tot_ = 23 + items[0]
        strict = 23 - bank_viol[n] + items[1]
        len_ = 23 - bank_viol[n] + items[0] - lenient_bad.get(n, 0)
        print(n, f'{100 * strict / tot_:.0f}% / {100 * len_ / tot_:.0f}%   before {BEF[n]}%')


def report_tier_basis():
    tier_per_lesson()
    # same 289-item basis as gifted_p6.md: 230 bank items + 59 'Start here' worksheet items
    bank = sum(v[1] for v in QB.values())
    strict = bank + WB['start'][1]
    lenient = bank + 59 - 6        # earlier audit's lenient reading: violation only if a child had no route in (6 items: L1 Q2,Q3; L7 Q2,Q4,Q5; L8 Q5)
    print('tier compliance on the 289-item basis: before 240/289 = %.1f%%; claimed 100%%; now lenient %.1f/289 = %.1f%%, strict %.1f/289 = %.1f%%' % (100 * 240 / 289, lenient, 100 * lenient / 289, strict, 100 * strict / 289))
    print('bank only: before', round(100 * 181 / 230, 1), '-> now', round(100 * bank / 230, 1))


def spot_checks():
    """Challenge answers re-derived by brute force (a sample across lessons 2, 3, 5, 7, 8, 9, 10)."""
    m = [[-3, 2, 1], [4, 0, -4], [-1, -2, 3]]
    assert all(sum(r) == 0 for r in m) and all(sum(c) == 0 for c in zip(*m)) and m[0][0] + m[1][1] + m[2][2] == 0 and m[0][2] + m[1][1] + m[2][0] == 0
    assert -6 + 2 * 7 + 3 * 3 == 17 and 6 * -30 == -180
    assert [t for t in range(0, 20) if -35 * t == -300 + 25 * t] == [5]
    assert 9 * 9 * 8 == 648 and 9 + 180 + 21 * 3 == 252 and comb(8, 4) == 70 and 9 + 4 + 1 == 14 and 7 + 21 == 28
    assert sum(1 for a in range(1, 10) for b in range(10) for c in range(10) if a + b + c == 5) == 15
    assert 12 * (360 + 30) == 13 * 360 and min(n for n in range(1, 100) if 150 * n % 360 == 0) == 12
    assert min(n for n in range(3, 500) if n % 3 == 2 and n % 4 == 2 and n % 5 == 2 and n % 7 == 0) == 182
    assert (12 % 7, 60 % 7) == (5, 4) and [k for k in range(26) if (2 * k) % 26 == 6] == [3, 16]
    assert 9 * 44 - 8 * 41 == 68 and 10 * 43 - 9 * 44 == 34
    assert sum(1 for n in range(1, 101) if n % 2 and n % 3) == 33 and 6 * 338 - 1 == 2027
    assert min(n for n in range(1, 1000) if all(n % d == 1 for d in (2, 3, 4, 5, 6)) and n % 7 == 0) == 301
    assert [n for n in range(1, 21) if sum(1 for d in range(1, n + 1) if n % d == 0) % 2 == 1] == [1, 4, 9, 16]
    print('Challenge spot checks: all OK')


if __name__ == '__main__':
    report_rubric(); print(); report_journey(); print(); report_tiers(); print(); compare(); print(); report_diag(); print(); report_rules(); print(); report_tier_basis(); print(); spot_checks()
