#!/usr/bin/env python3
"""Level 2 (P2) RE-AUDIT helper. Holds the PHASE 1 (blind) scores, written before any earlier audit file was opened,
and recomputes every table used in docs/audit/reaudit_p2.md. Run: python3 docs/audit/reaudit_p2.py
Phase 2 baseline numbers (from gifted_p2.md, gifted_fixes_p2.md, journey_p2.md) are in the BASE section at the bottom
and were typed in only after Phase 1 was frozen."""
import itertools, json

# ---------------------------------------------------------------- PHASE 1: instrument A (12 criteria, 0/1/2)
CRIT = ['1 low floor/high ceiling', '2 depth over speed', '3 abstraction/generalisation', '4 justification',
        '5 multiple solution paths', '6 challenge ladder', '7 student-led inquiry/talk', '8 complexity/context',
        '9 creativity/problem posing', '10 metacognition', '11 pacing flexibility', '12 extension not acceleration']
NOW_A = {  # lesson -> 12 scores, in CRIT order
    1: [2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2],
    2: [2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2],
    3: [2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1],
    4: [2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2],
    5: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
    6: [2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2],
    7: [2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2],
    8: [2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2],
    9: [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2],
    10: [2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2],
}

# ---------------------------------------------------------------- PHASE 1: instrument B (six 1-5 scores)
DIM = ['participate', 'difficulty fit', 'fun', 'confidence', 'motivation', 'social/online']
NOW_B = {  # lesson -> persona -> six scores
    1: {'LOW': [4, 3, 4, 3, 3, 4], 'MID': [5, 4, 4, 4, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    2: {'LOW': [4, 2, 3, 2, 3, 3], 'MID': [4, 3, 3, 4, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    3: {'LOW': [5, 3, 4, 4, 3, 4], 'MID': [5, 4, 4, 4, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    4: {'LOW': [4, 3, 4, 3, 3, 4], 'MID': [5, 4, 4, 4, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    5: {'LOW': [4, 2, 4, 3, 3, 4], 'MID': [4, 3, 4, 4, 4, 4], 'HIGH': [5, 3, 5, 4, 4, 4]},
    6: {'LOW': [4, 3, 5, 3, 4, 4], 'MID': [5, 4, 5, 4, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    7: {'LOW': [5, 3, 3, 3, 3, 4], 'MID': [5, 4, 4, 4, 4, 4], 'HIGH': [4, 2, 3, 4, 3, 4]},
    8: {'LOW': [5, 3, 5, 3, 3, 4], 'MID': [5, 4, 5, 4, 4, 4], 'HIGH': [5, 3, 5, 4, 4, 4]},
    9: {'LOW': [3, 2, 3, 2, 3, 3], 'MID': [4, 3, 4, 3, 4, 4], 'HIGH': [5, 3, 4, 4, 4, 4]},
    10: {'LOW': [3, 2, 3, 2, 3, 3], 'MID': [4, 3, 4, 3, 4, 4], 'HIGH': [5, 4, 4, 4, 5, 4]},
}

# ---------------------------------------------------------------- PHASE 1: tier compliance (binary violation counts)
# items per lesson: wb_core (printed worksheet Q1..), qb_core, qb_think (bank 'stretch'), qb_chal ; V = violations ; flat = TH re-skins of Core
TIER = {
    1: dict(wb=(6, 1), qc=(6, 0), th=(8, 1), ch=(9, 0), flat=3, flat_printed=2, gf_V=0),
    2: dict(wb=(6, 1), qc=(6, 0), th=(9, 1), ch=(9, 0), flat=3, flat_printed=3, gf_V=0),
    3: dict(wb=(6, 1), qc=(6, 1), th=(9, 0), ch=(9, 0), flat=2, flat_printed=2, gf_V=0),
    4: dict(wb=(6, 0), qc=(6, 0), th=(9, 0), ch=(9, 1), flat=2, flat_printed=2, gf_V=0),
    5: dict(wb=(5, 0), qc=(6, 0), th=(9, 0), ch=(9, 0), flat=4, flat_printed=1, gf_V=0),
    6: dict(wb=(6, 0), qc=(6, 1), th=(9, 0), ch=(9, 0), flat=1, flat_printed=1, gf_V=0),
    7: dict(wb=(6, 0), qc=(6, 0), th=(8, 0), ch=(9, 3), flat=4, flat_printed=2, gf_V=2),
    8: dict(wb=(4, 0), qc=(6, 1), th=(8, 0), ch=(9, 2), flat=2, flat_printed=1, gf_V=1),
    9: dict(wb=(5, 2), qc=(6, 1), th=(10, 0), ch=(9, 0), flat=1, flat_printed=1, gf_V=0),
    10: dict(wb=(6, 0), qc=(6, 0), th=(8, 0), ch=(9, 1), flat=2, flat_printed=1, gf_V=0),
}
VIOL = {  # the actual violations, with reason (Phase 1)
    'L1 WB core Q1': 'b/c need regrouping 15 tens / 13 tens, taught at min 20-24; no concrete scaffold on the page',
    'L2 WB core Q5': 'magic triangle: trial space is large; the corner insight is only taught on slide p2l2-teachtri',
    'L3 WB core Q1': 'asks for 2 multiplication AND 2 division sentences: formal notation the lesson teaches',
    'L9 WB core Q3': 'six-step 3 l/5 l jug search; needs the state-table method',
    'L9 WB core Q5': 'reading clock hands + a.m./p.m. + elapsed time stacked in one item',
    'L3 bank core C5': 'same as WB Q1: x and / sentences',
    'L6 bank core C1': 'needs the $2.75 notation convention taught in this lesson',
    'L8 bank core C6': 'recall of the word cylinder, not reasoning',
    'L9 bank core C5': 'a.m./p.m. convention, unexplained',
    'L1 bank think S4': 'conjecture-and-counterexample about swapping digits: Challenge-level generalisation',
    'L2 bank think S8': 'magic square from 9 given numbers needs a new insight (total = sum / 3)',
    'L4 bank chal C1': 'lights every 3 s / 5 s = re-skin of Core Q6 (both say), no extension',
    'L7 bank chal C4': 'two fractions with denominator 6 making 1: three-line list, no extension',
    'L7 bank chal C8': 'fold a strip three times -> 8 parts: one-step doubling (also on printed Go further, No.6)',
    'L7 bank chal C9': 'half of a half: one step (also on printed Go further, No.7)',
    'L8 bank chal C5': 'cube steps 9+6+3: same as Think Harder S1, no extension',
    'L8 bank chal C9': 'opposite faces of a dice: one-step recall (also on printed Go further, No.7)',
    'L10 bank chal C6': '3/10 + 4/10 left, then x 5 cm: one step plus unit conversion',
}

def a_total(n): return sum(NOW_A[n])
def b_mean(n, p): return sum(NOW_B[n][p]) / 6
def tier_totals():
    t = {k: [0, 0] for k in ('wb', 'qc', 'th', 'ch')}
    for L in TIER.values():
        for k in t:
            t[k][0] += L[k][0]; t[k][1] += L[k][1]
    return t

# ---------------------------------------------------------------- PHASE 1: diagnostic simulation (assumed per-question success probabilities)
def dist(ps):
    d = [1.0]
    for p in ps:
        n = [0.0] * (len(d) + 1)
        for k, v in enumerate(d):
            n[k] += v * (1 - p); n[k + 1] += v * p
        d = n
    return d
band_cur = lambda m: 'join' if m >= 4 else ('chat' if m >= 2 else 'down')       # diag/build_diag.py as built
band_json = lambda m: 'join' if m >= 5 else ('support' if m >= 3 else 'down')    # p2.json "scoring" block (not rendered)
PROFILES = {
    'A strong-for-age (8y)': ([.97, .97, .97, .97], [.95, .9, .9, .85, .85, .95]),
    'B typical-for-age (8y)': ([.95, .9, .95, .9], [.85, .75, .7, .6, .65, .85]),
    'C weak-for-age (8y)': ([.8, .6, .7, .6], [.6, .3, .3, .2, .3, .5]),
    'D younger strong (6-7y)': ([.99, .97, .97, .95], [.85, .5, .6, .2, .3, .6]),
    'E older weak (9y)': ([.85, .7, .8, .7], [.7, .5, .55, .5, .55, .7]),
    'F rusher/guesser (8y)': ([.97, .95, .97, .95], [.7, .5, .4, .4, .5, .7]),
}
def diag_table():
    out = []
    for k, (w, m) in PROFILES.items():
        d = dist(m)
        cur = {'join': 0, 'chat': 0, 'down': 0}; js = {'join': 0, 'support': 0, 'down': 0}
        for s, pr in enumerate(d):
            cur[band_cur(s)] += pr; js[band_json(s)] += pr
        out.append((k, sum(w), sum(m), cur, js))
    return out

# ---------------------------------------------------------------- PHASE 2: BASELINES (typed in after Phase 1 was frozen)
BASE = {}   # filled in below by the lines added in Phase 2
BASE['A_before'] = {1: [2,1,1,1,1,1,2,0,0,0,1,2], 2: [1,1,1,2,1,1,2,0,1,0,1,2], 3: [2,1,1,1,1,1,2,1,0,0,1,1],
    4: [2,1,2,1,1,1,2,1,1,0,1,2], 5: [1,1,1,1,1,2,2,1,1,0,1,2], 6: [2,1,1,1,1,1,1,2,0,0,1,2],
    7: [2,1,1,2,1,2,2,1,0,0,1,1], 8: [2,1,1,1,1,1,1,1,0,0,1,1], 9: [2,1,1,1,1,2,2,1,1,0,1,2], 10: [1,1,1,1,2,1,2,1,1,0,1,2]}   # gifted_p2.md rubric tables
BASE['A_claimed_total'] = {1: 16, 2: 17, 3: 17, 4: 18, 5: 17, 6: 17, 7: 17, 8: 14, 9: 18, 10: 16}   # gifted_fixes_p2.md 'after' table (L10 lists 3 increments but states 16)
BASE['A_claimed_delta'] = {1: {3:1,6:1,9:1,10:1}, 2: {3:1,6:1,9:1,10:1}, 3: {3:1,6:1,9:2,10:1}, 4: {6:1,9:1,10:1}, 5: {3:1,9:1,10:1},
    6: {3:1,6:1,9:1,10:1}, 7: {3:1,9:1,10:1}, 8: {6:1,9:1,10:1}, 9: {3:1,9:1,10:1}, 10: {3:1,6:1,10:1}}
BASE['tier'] = dict(items=317, ok=272, pct=86, challenge_bad=28, th_core_level=8, wb_core_no_entry=8, claimed_after_pct=100)
# journey_p2.md six scores per persona (P,D,F,C,M,S); the baseline reviewer used LOW/MIDDLE/HIGH
BASE['B_means'] = {'LOW': [3.33,2.75,3.33,3.42,2.83,3.75,3.58,3.17,2.58,3.25], 'MID': [4.17,3.58,4.17,4.17,3.75,4.42,4.25,4.0,3.5,4.08],
    'HIGH': [3.0,4.17,3.83,3.83,4.17,4.0,3.58,4.08,4.08,4.17]}
BASE['B_dims'] = {'LOW': [3.65,2.45,3.75,3.10,3.05,3.20], 'MID': [4.60,3.40,4.30,3.70,4.05,4.00], 'HIGH': [4.90,3.15,4.20,3.85,3.95,3.30]}
BASE['B_persona'] = {'LOW': 3.20, 'MID': 4.01, 'HIGH': 3.89}

# Post-Phase-2 consistency note: the baseline counted 'the standard swap table again' as a wrong-tier Challenge item.
# Applying that same yardstick adds two more (L3 C7 trikes/cars 30 wheels - printed Go further No.5; L6 C8 5c/20c 8 things $1 - printed Go further No.6).
ADJ_EXTRA_CHAL_V = {3: 1, 6: 1}
# slide 'Think harder' items (3 per lesson, shown on the deck, NOT the same as the printed Think Harder page): 30 items, 1 Core-level (L2 item 3: 456 + 99 with the trick given)
SLIDE_TH = (30, 1)

if __name__ == '__main__':
    print('A totals now:', {n: a_total(n) for n in NOW_A}, 'mean', round(sum(map(a_total, NOW_A)) / 10, 2))
    for p in ('LOW', 'MID', 'HIGH'):
        print(p, {n: round(b_mean(n, p), 2) for n in NOW_B}, 'mean', round(sum(b_mean(n, p) for n in NOW_B) / 10, 2))
    t = tier_totals(); print('tier', t)
    for k, w, m, c, j in diag_table(): print(k, round(w, 1), round(m, 1), {a: f'{b:.0%}' for a, b in c.items()}, {a: f'{b:.0%}' for a, b in j.items()})

# ---------------------------------------------------------------- PHASE 2 (after Phase 1 was frozen): like-for-like diagnostic re-run
# Baseline profile rates copied from docs/audit/journey_p2.py (warm-up x4, main x6, stretch x2) so old and new rules can be compared on the SAME children.
BASE_PROF = {
    'strong-for-age (8y)': ([.98, .98, .97, .97], [.97, .9, .95, .9, .85, .95], [.6, .55]),
    'typical-for-age (8y)': ([.97, .95, .92, .92], [.92, .6, .85, .7, .6, .85], [.2, .15]),
    'weak-for-age (8y)': ([.85, .8, .55, .55], [.55, .15, .4, .2, .15, .45], [.02, .02]),
    'younger strong (6y9m)': ([.98, .98, .95, .95], [.9, .55, .5, .75, .3, .6], [.5, .4]),
    'older weak (9y)': ([.92, .9, .75, .75], [.75, .3, .65, .4, .35, .6], [.04, .04]),
    'guesser/rusher': ([.9, .5, .5, .85], [.6, .1, .4, .3, .2, .35], [.03, .03]),
}
def old_rule(w, t):   # baseline page rule on total of 8
    if t >= 6: return 'up' if (t == 8 and w == 4) else 'join'
    if t >= 4: return 'down' if w <= 2 else 'join+support'
    return 'down'
def new_rule(w, m, s):  # as built in diag/build_diag.py: main 6 only, 4-6 / 2-3 / 0-1 ; warm-up<=2 steers down inside the middle row; stretch>=1 prompts the level-up suggestion inside the join row
    if m >= 4: return 'join+tryUp' if s >= 1 else 'join'
    if m >= 2: return 'chat(warm<=2: L1)' if w <= 2 else 'chat'
    return 'down'
def rerun():
    rows = []
    for name, (w, m, s) in BASE_PROF.items():
        dw, dm, ds = dist(w), dist(m), dist(s)
        # baseline rule uses total of main+stretch
        dt = dist(m + s)
        old = {}
        for tw, pw in enumerate(dw):
            for tt, pt in enumerate(dt):
                k = old_rule(tw, tt); old[k] = old.get(k, 0) + pw * pt
        new = {}
        for tw, pw in enumerate(dw):
            for tm, pm in enumerate(dm):
                for ts, ps in enumerate(ds):
                    k = new_rule(tw, tm, ts); new[k] = new.get(k, 0) + pw * pm * ps
        rows.append((name, old, new))
    return rows
if __name__ == '__main__':
    print('\n== like-for-like re-run: baseline profile rates, old rule vs rule as built ==')
    for name, old, new in rerun():
        f = lambda d: ', '.join(f'{k} {v:.0%}' for k, v in sorted(d.items(), key=lambda x: -x[1]) if v >= .005)
        print(f'{name:24s} OLD: {f(old)}\n{"":24s} NEW: {f(new)}')


def tier_summary():
    t = tier_totals()
    n = sum(v[0] for v in t.values()) + SLIDE_TH[0]; v = sum(x[1] for x in t.values()) + SLIDE_TH[1]
    flat = sum(L['flat'] for L in TIER.values()); flatp = sum(L['flat_printed'] for L in TIER.values())
    adj = v + sum(ADJ_EXTRA_CHAL_V.values())
    return dict(items=n, viol=v, pct=100 * (n - v) / n, adj_viol=adj, adj_pct=100 * (n - adj) / n, flat=flat, flat_printed=flatp,
                strict_pct=100 * (n - adj - flat) / n, by_tier={k: (a, b, 100 * (a - b) / a) for k, (a, b) in t.items()})

if __name__ == '__main__':
    print('\n== tier summary =='); print(tier_summary())
    bt = BASE['A_before']; print('A before mean', sum(map(sum, bt.values())) / 10, ' claimed mean', sum(BASE['A_claimed_total'].values()) / 10, ' now mean', sum(map(a_total, NOW_A)) / 10)
