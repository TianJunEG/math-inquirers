#!/usr/bin/env python3
"""Re-audit of Math Inquirers Level 3 (P3): data and arithmetic helper.

PHASE 1 (blind) block: scores written BEFORE any earlier audit file
(gifted_p3.md, journey_p3.md, fixpass/close_gaps/fixes logs) was opened.
PHASE 2 block (BASE_*): baseline numbers copied from the earlier audits afterwards.
Run:  python3 docs/audit/reaudit_p3.py   (prints all tables used in reaudit_p3.md)
"""
from statistics import mean

# ---------------------------------------------------------------- PHASE 1: instrument A
CRIT = ["1 LFHC", "2 Depth", "3 Generalise", "4 Justify", "5 Multi-path", "6 Ladder",
        "7 Student-led", "8 Complexity", "9 Posing", "10 Metacog", "11 Pacing", "12 Extension"]
#            1  2  3  4  5  6  7  8  9 10 11 12
NOW_A = {
    1: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
    2: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
    3: [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2],
    4: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1],
    5: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
    6: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
    7: [2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],   # blind value; criterion 5 corrected to 2 after compare, see POST_COMPARE_FIX
    8: [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
    9: [2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2],
    10: [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2],
}

# Post-compare correction (disclosed, not blind): while checking the baseline's L7 c5 = 2 I re-read slide p3l7-teach3
# ("Find the area of this L-shape in two ways ... Two ways agree, so we can trust our answer") plus teach2 (push out) vs
# Q4 hint (cut into two rectangles). My blind 1 had missed it. Corrected to 2. Every other criterion-5 '1' was re-checked
# by grepping all 10 decks for 'two ways / another way / Way 1': no further change.
POST_COMPARE_FIX = {(7, 5): (1, 2)}   # (lesson, criterion) -> (blind, corrected)
for (_l, _c), (_b, _n) in POST_COMPARE_FIX.items():
    NOW_A[_l][_c - 1] = _n

# tier verdicts. Strict rule: B (borderline) counts as a violation; lenient: B counts as compliant.
# Question bank items: core 6/lesson, think-harder (stretch) 8-9, challenge 8-9.
QB_N = {"core": 60, "stretch": 84, "challenge": 90}
QB_B = {  # item -> reason
    "L2 stretch s5": "smallest/greatest 4-digit number with digit sum 30 is an L1 place-value idea, not the L2 taught idea",
    "L3 challenge c6": "40-60 sweets shared by 6 and 9: list-and-test, one step of the taught method (Think-harder level)",
    "L5 challenge c2": "30-50 chocolates shared by 2,3,4,6: same list-and-test as the Think-harder riddle s7",
    "L7 challenge c4": "square perimeter 20 -> side 5 -> big square 10 -> 40: three routine steps, no extension",
}
# printed workbook 'Start here' pages: 6 numbered questions per lesson = 60 items
SH_N = 60
SH_B = {
    "L1 Q6": "(if time) count 4-digit numbers with digit sum 3 by listing = Think-harder demand on a core page",
    "L2 Q6": "(if time) AB+AB+AB=CAB letter puzzle = Think-harder demand",
    "L3 Q4": "(if time) 3x3 multiplication grid from two clue facts = Think-harder demand",
    "L3 Q6": "(if time) numbers divisible by 6 and 8 with a digit-sum clue = Think-harder demand",
    "L5 Q6": "(if time) party-table two-condition problem = Think-harder demand",
    "L6 Q4": "adding/subtracting unlike fractions (1/4+3/8, 1/3+5/12) needs the taught equal-parts method; only the wall helps",
    "L10 Q6": "(if time) odd 3-digit, digit sum 6, find ALL = Think-harder demand",
}
PRINT_TH_GF_N = 70   # 4 Think harder + 3 Go further per lesson (all drawn from the bank, no B)
INV_N = 10           # investigation pages, each with an 'Easy first step'

# ---------------------------------------------------------------- PHASE 1: instrument B
DIM = ["Participate", "Fit", "Fun", "Confidence", "Motivation", "Social/online"]
#          P  D  F  C  M  S
NOW_B = {
    "LOW": {1: [4, 3, 4, 3, 3, 3], 2: [3, 2, 3, 2, 3, 3], 3: [4, 3, 4, 3, 3, 3], 4: [4, 3, 4, 3, 3, 3], 5: [4, 3, 4, 3, 3, 3],
            6: [3, 2, 3, 2, 3, 3], 7: [4, 3, 4, 3, 3, 4], 8: [4, 3, 4, 3, 3, 3], 9: [3, 2, 4, 2, 3, 3], 10: [4, 2, 4, 3, 3, 3]},
    "MIDDLE": {1: [4, 4, 4, 4, 4, 4], 2: [4, 3, 4, 3, 4, 4], 3: [4, 4, 5, 4, 4, 4], 4: [4, 4, 4, 4, 4, 4], 5: [4, 4, 4, 4, 4, 4],
               6: [4, 3, 4, 3, 4, 4], 7: [4, 4, 4, 4, 4, 4], 8: [4, 4, 4, 4, 4, 4], 9: [4, 3, 5, 3, 4, 4], 10: [4, 3, 4, 4, 4, 4]},
    "HIGH": {1: [5, 3, 4, 5, 4, 4], 2: [5, 4, 5, 5, 4, 4], 3: [5, 3, 4, 5, 5, 4], 4: [5, 3, 4, 5, 4, 4], 5: [5, 3, 5, 5, 5, 4],
             6: [5, 3, 4, 5, 4, 4], 7: [5, 3, 4, 5, 5, 4], 8: [5, 3, 5, 5, 5, 4], 9: [5, 3, 5, 5, 5, 4], 10: [5, 4, 5, 5, 4, 4]},
}

# ---------------------------------------------------------------- PHASE 1: diagnostic simulation
def dist(ps):
    d = {0: 1.0}
    for p in ps:
        nd = {}
        for k, v in d.items():
            nd[k] = nd.get(k, 0) + v * (1 - p)
            nd[k + 1] = nd.get(k + 1, 0) + v * p
        d = nd
    return d

def rule(main, warm, stretch):
    """Placement rule exactly as in diag/build_diag.py (result page, page 3)."""
    if main >= 4:
        return "Join L3" + (" (+ try L4 check)" if stretch >= 1 else "")
    if main >= 2:
        return "Chat + taster; L3 with support" + ("; L2 may be more comfortable" if warm <= 2 else "")
    return "Suggest L2"

PROFILES = {  # per-item success probabilities: warm-up (4), main (6), stretch (2); judgement, not data
    "A strong-for-age (9, P3)": ([.98, .95, .98, .98], [.9, .85, .85, .85, .95, .8], [.6, .6]),
    "B typical-for-age (9)": ([.95, .85, .9, .95], [.7, .6, .7, .6, .75, .55], [.2, .25]),
    "C weak-for-age (9)": ([.8, .45, .7, .8], [.3, .15, .3, .15, .3, .2], [.03, .05]),
    "D younger strong (7, end P2)": ([.95, .8, .9, .95], [.75, .5, .4, .3, .1, .5], [.6, .5]),
    "E older weak (10, P4)": ([.85, .6, .8, .9], [.45, .3, .45, .3, .5, .3], [.05, .1]),
    "F rushes/guesses (9)": ([.8, .7, .85, .9], [.6, .5, .55, .45, .65, .4], [.15, .15]),
}

def diag_report():
    out = []
    for n, (w, m, s) in PROFILES.items():
        dm = dist(m)
        band = {"0-1": sum(v for k, v in dm.items() if k <= 1), "2-3": sum(v for k, v in dm.items() if 2 <= k <= 3),
                "4-6": sum(v for k, v in dm.items() if k >= 4)}
        exp = sum(k * v for k, v in dm.items())
        out.append((n, round(sum(w)), round(exp), round(sum(s)), rule(round(exp), round(sum(w)), round(sum(s))),
                    {k: round(v, 2) for k, v in band.items()}))
    return out

# ---------------------------------------------------------------- PHASE 2: baselines (copied AFTER the blind scoring above)
# Source: docs/audit/gifted_p3.md (rubric, 'before' = original audit; 'claimed' = the 'after rework' column of that file)
BASE_A_BEFORE = {
    1: [2, 1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 2], 2: [2, 1, 2, 2, 1, 1, 1, 1, 0, 1, 1, 2], 3: [2, 1, 2, 2, 2, 1, 2, 1, 0, 1, 1, 2],
    4: [2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2], 5: [2, 1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 2], 6: [2, 1, 2, 2, 1, 1, 1, 1, 0, 1, 1, 2],
    7: [2, 1, 2, 2, 2, 1, 2, 1, 0, 1, 1, 2], 8: [2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 2], 9: [2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1],
    10: [2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2]}
BASE_A_CLAIMED_TOTAL = {1: 18, 2: 17, 3: 19, 4: 18, 5: 18, 6: 17, 7: 19, 8: 16, 9: 17, 10: 18}
# tier compliance: items audited, violations (original); claimed after rework = 100%
BASE_TIER = {1: (29, 5), 2: (29, 5), 3: (29, 5), 4: (30, 8), 5: (32, 5), 6: (33, 9), 7: (32, 10), 8: (32, 12), 9: (30, 5), 10: (29, 5)}
# Source: docs/audit/journey_p3.md section 1.1 per-lesson tables (original review)
BASE_B_BEFORE = {
    "LOW": {1: [4, 3, 4, 3, 3, 3], 2: [3, 2, 3, 2, 3, 3], 3: [2, 2, 3, 2, 3, 2], 4: [4, 3, 4, 3, 3, 3], 5: [3, 2, 3, 2, 3, 3],
            6: [4, 3, 3, 3, 3, 3], 7: [3, 3, 4, 3, 3, 3], 8: [3, 2, 3, 3, 3, 3], 9: [2, 1, 3, 2, 3, 2], 10: [4, 3, 4, 4, 4, 3]},
    "MIDDLE": {1: [5, 4, 4, 4, 4, 4], 2: [4, 3, 4, 3, 4, 4], 3: [4, 3, 4, 4, 4, 3], 4: [5, 4, 4, 4, 4, 4], 5: [4, 3, 4, 4, 4, 4],
               6: [5, 4, 4, 4, 4, 4], 7: [4, 4, 4, 4, 4, 4], 8: [4, 3, 4, 4, 4, 4], 9: [3, 3, 4, 3, 4, 3], 10: [5, 4, 5, 4, 5, 4]},
    "HIGH": {1: [5, 3, 4, 4, 4, 4], 2: [5, 4, 5, 4, 5, 4], 3: [5, 4, 5, 5, 5, 4], 4: [5, 3, 4, 4, 4, 4], 5: [5, 4, 4, 4, 5, 4],
             6: [5, 3, 4, 4, 4, 4], 7: [5, 3, 5, 4, 5, 4], 8: [5, 4, 5, 4, 5, 4], 9: [5, 4, 5, 4, 5, 4], 10: [5, 3, 4, 4, 4, 4]}}
# tier violations by lesson now (strict: borderline counts as violation; like-for-like: 'if time' stars counted with their question)
NOW_TIER_ITEMS = {1: 29, 2: 30, 3: 29, 4: 30, 5: 32, 6: 33, 7: 32, 8: 32, 9: 30, 10: 29}   # QB + 6 Start-here + slide-only Think-harder (L5-L8: 3 each)
NOW_TIER_VIOL = {1: 1, 2: 2, 3: 3, 4: 0, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0, 10: 1}
NOW_TIER_VIOL_LFL = {1: 0, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 1, 8: 0, 9: 0, 10: 0}

def compare():
    L = range(1, 11)
    print("| L | before | claimed | now | d vs before | d vs claimed |"); 
    for l in L:
        b = sum(BASE_A_BEFORE[l]); c = BASE_A_CLAIMED_TOTAL[l]; n = sum(NOW_A[l])
        print(f"| {l} | {b} | {c} | {n} | {n-b:+d} | {n-c:+d} |")
    mb = mean(sum(BASE_A_BEFORE[l]) for l in L); mc = mean(BASE_A_CLAIMED_TOTAL.values()); mn = mean(sum(NOW_A[l]) for l in L)
    print(f"| mean | {mb:.1f} | {mc:.1f} | {mn:.1f} | {mn-mb:+.1f} | {mn-mc:+.1f} |")
    print()
    print("criterion | before mean | now mean | delta | lessons up | lessons down")
    for c in range(12):
        bm = mean(BASE_A_BEFORE[l][c] for l in L); nm = mean(NOW_A[l][c] for l in L)
        up = [l for l in L if NOW_A[l][c] > BASE_A_BEFORE[l][c]]; dn = [l for l in L if NOW_A[l][c] < BASE_A_BEFORE[l][c]]
        print(f"{CRIT[c]} | {bm:.1f} | {nm:.1f} | {nm-bm:+.1f} | {up} | {dn}")
    print()
    print("heatmap lesson: LOW before/now, MIDDLE, HIGH, lesson mean")
    for l in L:
        row = []
        for p in ("LOW", "MIDDLE", "HIGH"):
            b = mean(BASE_B_BEFORE[p][l]); n = mean(NOW_B[p][l]); row.append((b, n))
        print(l, " | ".join(f"{b:.2f} -> {n:.2f} ({n-b:+.2f})" for b, n in row),
              f"| mean {mean(r[0] for r in row):.2f} -> {mean(r[1] for r in row):.2f}")
    for p in ("LOW", "MIDDLE", "HIGH"):
        print(p, "level mean", round(mean(mean(v) for v in BASE_B_BEFORE[p].values()), 2), "->", round(mean(mean(v) for v in NOW_B[p].values()), 2))
        print("   dims before", [round(mean(BASE_B_BEFORE[p][l][i] for l in L), 1) for i in range(6)],
              "now", [round(mean(NOW_B[p][l][i] for l in L), 1) for i in range(6)])
    print()
    tb = sum(v[0] for v in BASE_TIER.values()); vb = sum(v[1] for v in BASE_TIER.values())
    tn = sum(NOW_TIER_ITEMS.values()); vn = sum(NOW_TIER_VIOL.values()); vl = sum(NOW_TIER_VIOL_LFL.values())
    print(f"tier before {tb-vb}/{tb} = {100*(tb-vb)/tb:.1f}% ; now strict {tn-vn}/{tn} = {100*(tn-vn)/tn:.1f}% ; now like-for-like {tn-vl}/{tn} = {100*(tn-vl)/tn:.1f}%")
    for l in L:
        i, v = BASE_TIER[l]; ni, nv, nl = NOW_TIER_ITEMS[l], NOW_TIER_VIOL[l], NOW_TIER_VIOL_LFL[l]
        print(f"L{l}: before {i-v}/{i} {100*(i-v)/i:.0f}% | now strict {ni-nv}/{ni} {100*(ni-nv)/ni:.0f}% | lfl {ni-nl}/{ni} {100*(ni-nl)/ni:.0f}%")

if __name__ == "__main__":
    print("A totals now:", {k: sum(v) for k, v in NOW_A.items()}, "mean", round(mean(sum(v) for v in NOW_A.values()), 2))
    for c in range(12):
        print(CRIT[c], round(mean(v[c] for v in NOW_A.values()), 2))
    for p, d in NOW_B.items():
        print(p, {k: round(mean(v), 2) for k, v in d.items()}, "level mean", round(mean(mean(v) for v in d.values()), 2))
        print("  dims", {DIM[i]: round(mean(v[i] for v in d.values()), 2) for i in range(6)})
    tot_qb = sum(QB_N.values()); b_qb = len(QB_B)
    print("QB strict", tot_qb - b_qb, "/", tot_qb, round(100 * (tot_qb - b_qb) / tot_qb, 1))
    print("SH strict", SH_N - len(SH_B), "/", SH_N, round(100 * (SH_N - len(SH_B)) / SH_N, 1))
    allN = tot_qb + SH_N; allB = b_qb + len(SH_B)
    print("distinct items strict", allN - allB, "/", allN, round(100 * (allN - allB) / allN, 1))
    for r in diag_report():
        print(r)
    print()
    compare()
