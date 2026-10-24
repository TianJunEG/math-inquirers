#!/usr/bin/env python3
"""Independent circular year check for the daily teasers (fix round 3).

    python3 website/teasers/year_model.py            # all levels, quick (a few robustness trials)
    python3 website/teasers/year_model.py --full     # more robustness trials
    python3 website/teasers/year_model.py 1 2        # chosen levels only

Written separately from verify_bank.py / build_bank.py / taxonomy.py: it reads only taxonomy.json, the two released banks
(batches/m11, batches/m12) and batches/YEAR_PLAN.md, and rebuilds the owner's rules itself.

Levels 1 and 2 (L1L2-GAP60): parse the 61-row rotation of YEAR_PLAN.md, lay it on the 366 dates of a leap year starting 1 Nov and check, for a 366-day
and a 365-day (29 Feb removed) circular year: every sub-structure at least 60 days from itself, a family at most 3 times in any 60 consecutive days, no family
on two consecutive days, and that the plan's sub-structures equal the released banks'.  Then how many failed sub-structures the rotation survives:
each failed sub-structure needs a spare sub-structure (usable at the level, not in the rotation) whose family fits all 6 of its slots.

Levels 3 to 6 (TEASER-STRICT): an integer program (HiGHS through scipy) with one sub-structure per day over the 366 dates, each sub-structure at most once per
calendar quarter, each family at most 3 times per quarter, any two uses of a sub-structure at least 30 days apart round the year (so across the quarter
boundaries, 31 Dec to 1 Jan included), no family on consecutive days, and the released November and December sub-structures fixed.  It reports whether a year
exists, whether one exists with the stricter family cap 2, and how many unreleased sub-structures can be lost (seeded random trials) before no year exists.
It models structure only, not answers, stories or frames.
"""
import calendar
import datetime as dt
import json
import os
import random
import re
import sys
import time

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import coo_matrix

HERE = os.path.dirname(os.path.abspath(__file__))
TAX = json.load(open(os.path.join(HERE, 'taxonomy.json'), encoding='utf-8'))
RELEASED = ['11', '12']


def dates(leap=True):
    out = []
    for m in range(1, 13):
        n = calendar.monthrange(2028 if leap else 2027, m)[1]
        for d in range(1, n + 1):
            out.append('%02d-%02d' % (m, d))
    return out


def usable(level):
    return sorted(s for s, d in TAX['subs'].items() if level in d['levels'])


def fam(sub):
    return sub.split('.')[0]


def bank(level):
    out = {}
    for mm in RELEASED:
        for e in json.load(open(os.path.join(HERE, 'batches', 'm%s' % mm, 'bank.json'), encoding='utf-8'))['levels'][str(level)]:
            out[e['date']] = e['sub']
    return out


# ------------------------------------------------------------------ Levels 1 and 2
def parse_plan(level):
    txt = open(os.path.join(HERE, 'batches', 'YEAR_PLAN.md'), encoding='utf-8').read()
    part = txt.split('## Level %d' % level)[1].split('## Level')[0]
    rows = re.findall(r'^\| (\d+) \| (\d\d-\d\d) \| ([a-z_0-9.]+) \|', part, re.M)
    return [(int(k), d, s) for k, d, s in rows]


def rotation_year(level, leap):
    """sub-structure on every date of the year, laid out from 1 Nov: day k (0-based from 1 Nov in a 366-day year) uses plan row k mod 61."""
    rows = parse_plan(level)
    assert len(rows) == 61, len(rows)
    subs = [s for _, _, s in rows]
    seq366 = dates(True)
    start = seq366.index('11-01')
    order366 = seq366[start:] + seq366[:start]
    plan = {}
    for k, d in enumerate(order366):
        plan[d] = subs[k % 61]
    ds = dates(leap)
    return [(d, plan[d]) for d in ds]


def check_rotation(level):
    problems = []
    for leap in (True, False):
        year = rotation_year(level, leap)
        n = len(year)
        by_sub, by_fam = {}, {}
        for i, (d, s) in enumerate(year):
            by_sub.setdefault(s, []).append(i)
            by_fam.setdefault(fam(s), []).append(i)
        mingap = 10 ** 6
        for s, pos in by_sub.items():
            for a in range(len(pos)):
                for b in range(a + 1, len(pos)):
                    g = min(abs(pos[a] - pos[b]), n - abs(pos[a] - pos[b]))
                    mingap = min(mingap, g)
        if mingap < 60:
            problems.append('%d-day year: a sub-structure returns after %d days' % (n, mingap))
        worst = 0
        consec = 0
        for f, pos in by_fam.items():
            ps = set(pos)
            for i in pos:
                if (i + 1) % n in ps:
                    consec += 1
            for i in pos:
                worst = max(worst, sum(1 for t in range(60) if (i + t) % n in ps))
        if worst > 3:
            problems.append('%d-day year: a family %d times in 60 days' % (n, worst))
        if consec:
            problems.append('%d-day year: %d family repeats on consecutive days' % (n, consec))
        print('  L%d %d-day year: minimum circular gap %d, worst family in 60 days %d, consecutive family days %d' % (level, n, mingap, worst, consec))
    b = bank(level)
    rows = parse_plan(level)
    mism = [d for _, d, s in rows if b.get(d) != s]
    # the plan's table lists the released sub-structure of each date (first 61 dates); compare with the released banks
    print('  L%d plan against the released banks: %d mismatches in %d rows' % (level, len(mism), len(rows)))
    if mism:
        problems.append('plan differs from the bank on %s' % mism[:5])
    return problems


def robustness_rotation(level, trials=200, seed=7):
    """Replace a failed sub-structure everywhere (all its slots in the year) by an unused sub-structure that keeps every family rule."""
    rows = parse_plan(level)
    used = [s for _, _, s in rows]
    spares = [s for s in usable(level) if s not in used]
    year = [s for _, s in rotation_year(level, True)]
    n = len(year)
    slot = {}
    for i, s in enumerate(year):
        slot.setdefault(s, []).append(i)

    def fits(sp, slots, current):
        """can sub-structure sp take `slots` without breaking the family rules, given the year `current` (None = an empty slot)?"""
        f = fam(sp)
        pos = {i for i, s in enumerate(current) if s is not None and fam(s) == f} | set(slots)
        for i in slots:
            if ((i + 1) % n) in pos or ((i - 1) % n) in pos:
                return False
        for i in pos:
            if sum(1 for t in range(60) if (i + t) % n in pos) > 3:
                return False
        return True
    ok_single = []
    for s in sorted(slot):
        base = [None if x == s else x for x in year]
        if any(fits(sp, slot[s], base) for sp in spares):
            ok_single.append(s)
    print('  L%d: %d spare sub-structures; one failed sub-structure can be replaced for %d of %d rotation slots' % (level, len(spares), len(ok_single), len(slot)))
    rnd = random.Random(seed)
    res = {'spares': len(spares), 'replaceable_single': len(ok_single)}
    for k in (1, 2, 3, 5, 8, 12):
        good = 0
        for _ in range(trials):
            fails = rnd.sample(sorted(slot), k)
            cur = [None if x in fails else x for x in year]
            pool = list(spares)
            rnd.shuffle(pool)
            done = True
            for s in fails:
                for sp in pool:
                    if fits(sp, slot[s], cur):
                        for i in slot[s]:
                            cur[i] = sp
                        pool.remove(sp)
                        break
                else:
                    done = False
                    break
            good += done
        res['lose%d' % k] = '%d/%d' % (good, trials)
        print('  L%d: %d failed sub-structures replaced by spares in %d of %d random draws' % (level, k, good, trials))
    return res


# ------------------------------------------------------------------ Levels 3 to 6
def quarter_of(d):
    return (int(d[:2]) - 1) // 3


def build_ip(level, fam_cap=3, drop=(), gap=30, no_consecutive=True):
    subs = [s for s in usable(level) if s not in drop]
    fixed = bank(level)
    ds = dates(True)
    D, S = len(ds), len(subs)
    sidx = {s: i for i, s in enumerate(subs)}
    var = lambda d, s: d * S + s
    rows, cols, vals, lo, hi = [], [], [], [], []
    r = 0

    def add(terms, a, b):
        nonlocal r
        for c in terms:
            rows.append(r)
            cols.append(c)
            vals.append(1.0)
        lo.append(a)
        hi.append(b)
        r += 1
    for d in range(D):                                  # one sub-structure a day
        add([var(d, s) for s in range(S)], 1, 1)
    fams = {}
    for s in subs:
        fams.setdefault(fam(s), []).append(sidx[s])
    for q in range(4):
        qd = [d for d, x in enumerate(ds) if quarter_of(x) == q]
        for s in range(S):                              # once per quarter
            add([var(d, s) for d in qd], 0, 1)
        for f, ss in fams.items():                      # a family at most fam_cap times per quarter
            add([var(d, s) for d in qd for s in ss], 0, fam_cap)
    for s in range(S):                                  # any two uses at least `gap` days apart, round the year
        for d in range(D):
            add([var((d + t) % D, s) for t in range(gap)], 0, 1)
    if no_consecutive:
        for f, ss in fams.items():
            for d in range(D):
                add([var(d, s) for s in ss] + [var((d + 1) % D, s) for s in ss], 0, 1)
    ub = np.ones(D * S)
    lb = np.zeros(D * S)
    for d, x in enumerate(ds):
        if x in fixed:
            s = fixed[x]
            if s not in sidx:
                return None, 'released sub-structure %s is not usable at level %d' % (s, level)
            for t in range(S):
                if t != sidx[s]:
                    ub[var(d, t)] = 0
            lb[var(d, sidx[s])] = 1
    A = coo_matrix((vals, (rows, cols)), shape=(r, D * S)).tocsr()
    return (A, np.array(lo), np.array(hi), lb, ub, D * S), None


def solve(level, limit=300, **kw):
    t = time.time()
    m, err = build_ip(level, **kw)
    if err:
        return None, err, 0
    A, lo, hi, lb, ub, nv = m
    res = milp(c=np.zeros(nv), constraints=LinearConstraint(A, lo, hi), integrality=np.ones(nv), bounds=Bounds(lb, ub),
               options={'time_limit': limit, 'presolve': True})
    return res.status, res.message, time.time() - t


def verdict(status):
    return {0: 'feasible', 2: 'INFEASIBLE', 1: 'time limit', 3: 'unbounded', 4: 'error'}.get(status, str(status))


def levels_3_6(level, trials, seed=11):
    out = {}
    st, msg, t = solve(level)
    print('  L%d cap 3: %s (%.0f s)' % (level, verdict(st), t))
    out['cap3'] = verdict(st)
    st2, _, t2 = solve(level, fam_cap=2)
    print('  L%d cap 2 (the stricter reading): %s (%.0f s)' % (level, verdict(st2), t2))
    out['cap2'] = verdict(st2)
    released = set(bank(level).values())
    free = [s for s in usable(level) if s not in released]
    rnd = random.Random(seed + level)
    for k in (1, 3, 5, 8, 12):
        good = 0
        for _ in range(trials):
            drop = rnd.sample(free, k)
            stk, _, _ = solve(level, drop=tuple(drop), limit=120)
            good += (stk == 0)
        print('  L%d: %d unreleased sub-structures lost: a year still exists in %d of %d random draws' % (level, k, good, trials))
        out['lose%d' % k] = '%d/%d' % (good, trials)
    print('  L%d: usable %d, released %d, unreleased %d' % (level, len(usable(level)), len(released), len(free)))
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    lvls = [int(a) for a in args] or [1, 2, 3, 4, 5, 6]
    full = '--full' in sys.argv
    allres, bad = {}, []
    for lv in lvls:
        print('Level %d' % lv)
        if lv <= 2:
            p = check_rotation(lv)
            bad += ['L%d: %s' % (lv, x) for x in p]
            allres[lv] = robustness_rotation(lv, trials=500 if full else 200)
        else:
            allres[lv] = levels_3_6(lv, trials=5 if full else 3)
            if allres[lv]['cap3'] != 'feasible':
                bad.append('L%d: no year exists with the family cap 3' % lv)
    print('\nindependent year check: %d problem(s)' % len(bad))
    for b in bad:
        print('  ', b)
    json.dump(allres, open(os.path.join(HERE, 'batches', 'YEAR_MODEL_RESULT.json'), 'w'), indent=1, default=str)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
