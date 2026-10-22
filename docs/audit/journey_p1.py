"""Helper for docs/audit/journey_p1.md. Read-only analysis of P1 content.
Run: python3 -I docs/audit/journey_p1.py   (from repo root)
Prints: reading load per lesson (core page, Think Harder/Challenge, open investigation, look-back),
workbook word counts, and the diagnostic simulation / cut-score maths."""
import re, html, json, itertools, math, random
R = '/home/claude/math-inquirers'
raw = open(f'{R}/hp/workbook_body.html').read()
txt = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', raw)))

def syl(w):
    w = w.lower(); w = re.sub(r'[^a-z]', '', w)
    if not w: return 0
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1: n -= 1
    return max(n, 1)

def stats(s):
    s2 = re.sub(r'_+', ' ', s)
    words = [w for w in re.findall(r"[A-Za-z’']+", s2)]
    sents = max(1, len(re.findall(r'[.?!]', s2)))
    syls = sum(syl(w) for w in words)
    fk = 0.39 * len(words) / sents + 11.8 * syls / max(1, len(words)) - 15.59 if words else 0
    longw = [w for w in words if syl(w) >= 3]
    return len(words), sents, round(fk, 1), len(longw)

# Reading load from SOURCE strings: core page text from hp/workbook.js (per LESSON section), T/C from qbank, investigation from gaps.json
src = open(f'{R}/hp/workbook.js').read()
QB = json.load(open(f'{R}/hp/qbank.json')); GP = json.load(open(f'{R}/hp/gaps.json'))
sec = {}
for n in range(1, 11):
    a = src.index(f'/* ---------- LESSON {n} ')
    b = src.index(f'/* ---------- LESSON {n+1} ') if n < 10 else src.index('/* ---------- APPENDIX')
    seg = src[a:b]
    # drop the extra(n-1) call line and code; keep prose string literals with >=3 words
    lits = re.findall(r"'((?:[^'\\]|\\.)*)'", seg)
    lits = [l for l in lits if len(re.findall(r'[A-Za-z]{2,}', l)) >= 3 and not l.endswith('.png') and 'require' not in l and 'D9D9D9' not in l]
    sec[n] = ' '.join(lits)
print('n | CORE page: words, sentences, FK grade, words>=3 syllables | T1-T4+C1-C3 words/FK | investigation words/FK | longest single core item (words)')
for n in range(1, 11):
    core = sec[n]
    tc = ' '.join(x['q'] for x in QB[str(n)]['stretch'][:4]) + ' ' + ' '.join(x['q'] for x in QB[str(n)]['challenge'][-3:])
    iv = GP[str(n)]['invest']['q']
    items = [l for l in re.findall(r"'((?:[^'\\]|\\.)*)'", src[src.index(f'/* ---------- LESSON {n} '):]) ][:0]
    longest = max((len(re.findall(r"[A-Za-z’']+", l)) for l in re.findall(r"'((?:[^'\\]|\\.)*)'", src[src.index(f'/* ---------- LESSON {n} '):(src.index(f'/* ---------- LESSON {n+1} ') if n < 10 else src.index('/* ---------- APPENDIX'))])), default=0)
    print(n, stats(core), stats(tc)[::2], stats(iv)[::2], longest)
# look-back box
lb = 'What was hard? A one-minute look-back. There are no right answers. Tick or write. The hardest part was ... I got unstuck by ... counters or objects drawing it asking someone trying again Next time I will try ... It felt: easy OK hard'
print('look-back box', stats(lb))

# =====================  PART 2: diagnostic simulation  =====================
# Per-question P(correct) are MY ASSUMPTIONS (no real child data exist). Order: W1..W4, M1..M6, S1, S2
def pb(ps):
    d = [1.0]
    for p in ps:
        n = [0.0] * (len(d) + 1)
        for i, v in enumerate(d):
            n[i] += v * (1 - p); n[i + 1] += v * p
        d = n
    return d
PROF = {
 'Strong-for-age (age 7, P1, top 15%)':        [.99,.99,.99,.99, .95,.97,.90,.80,.90,.90, .50,.35],
 'Typical-for-age (age 7, P1, meets school)':  [.98,.97,.95,.95, .85,.85,.65,.50,.60,.70, .12,.06],
 'Weak-for-age (age 7, P1, struggling)':       [.90,.80,.75,.80, .45,.50,.15,.10,.20,.40, .02,.01],
 'Younger and strong (age 6, K2/P1 start)':    [.99,.98,.98,.98, .90,.90,.35,.55,.65,.80, .20,.08],
 'Older and weak (age 8, P2/P3, shaky number sense)': [.98,.97,.95,.97, .70,.70,.50,.35,.45,.55, .06,.03],
 'Guesser / rusher (age 7, typical ability)':  [.85,.85,.80,.90, .65,.65,.40,.25,.30,.50, .05,.03],
}
def cur_rule(w, sc):          # rule as printed on the parent page
    if sc >= 6: return 'JOIN (try P2 check)' if (sc == 8 and w == 4) else 'JOIN'
    if sc >= 4: return 'JOIN + support; taster/chat first (warm-up<=2)' if w <= 2 else 'JOIN + support'
    return 'taster + tutor chat first'
def dist_outcomes(ps, rule=cur_rule):
    dw, dm, ds = pb(ps[:4]), pb(ps[4:10]), pb(ps[10:])
    out = {}; tot = [0.0] * 9
    for w, pw in enumerate(dw):
        for m, pm in enumerate(dm):
            for s, pS in enumerate(ds):
                p = pw * pm * pS; tot[m + s] += p
                k = rule(w, m + s); out[k] = out.get(k, 0) + p
    return out, tot, (sum(i*v for i,v in enumerate(dw)), sum(i*v for i,v in enumerate(dm)), sum(i*v for i,v in enumerate(ds)))
print('\n=== PART 2: placement outcomes under the CURRENT rule ===')
for name, ps in PROF.items():
    o, tot, e = dist_outcomes(ps)
    print(name, 'E[warm,main,stretch]=%.2f/%.2f/%.2f' % e)
    for k, v in sorted(o.items(), key=lambda x: -x[1]): print('   %-52s %.0f%%' % (k, 100 * v))
    print('   score/8 distribution:', [round(100 * x) for x in tot])
# Alternative rule: judge on the 6 main questions; stretch is a bonus only
def alt_rule(w, sc, m=None): pass
def dist_outcomes_alt(ps):
    dw, dm, ds = pb(ps[:4]), pb(ps[4:10]), pb(ps[10:])
    out = {}
    for w, pw in enumerate(dw):
        for m, pm in enumerate(dm):
            for s, pS in enumerate(ds):
                p = pw * pm * pS
                if m >= 4: k = 'JOIN' + (' (try P2 check)' if (m >= 5 and s >= 1 and w >= 3) else '')
                elif m >= 2: k = 'JOIN + support' if w >= 3 else 'taster + chat first'
                else: k = 'taster + tutor chat first'
                out[k] = out.get(k, 0) + p
    return out
print('\n=== ALTERNATIVE: main>=4 join; main 2-3 support; main<=1 taster; stretch only unlocks the P2 check (main>=5, stretch>=1, warm-up>=3) ===')
for name, ps in PROF.items():
    o = dist_outcomes_alt(ps)
    print(name); [print('   %-30s %.0f%%' % (k, 100 * v)) for k, v in sorted(o.items(), key=lambda x: -x[1])]
# Luck: fixed true accuracy p on the 8 scored items (stretch inflated to p as an upper bound), and p on main only
print('\n=== Luck table: child answers each of the 6 main questions right with probability p (stretch ~0) ===')
for p in (.9, .8, .7, .6, .5, .4, .3):
    d = pb([p] * 6)
    print('p=%.1f E[main]=%.1f  P(6)=%.0f%%  P(>=4)=%.0f%%  P(<=3)=%.0f%%  P(<=1)=%.0f%%' % (p, 6*p, 100*d[6], 100*sum(d[4:]), 100*sum(d[:4]), 100*sum(d[:2])))
print('Same with all 8 items equally hard (p on every item, binomial 8):')
for p in (.9, .8, .7, .6, .5, .4):
    d = pb([p] * 8)
    print('p=%.1f P(>=6)=%.0f%% P(4-5)=%.0f%% P(<=3)=%.0f%%' % (p, 100*sum(d[6:]), 100*(d[4]+d[5]), 100*sum(d[:4])))
# pure guessing: chance of a lucky numeric guess
print('\nPure guess P(correct): M6 (3 names) ~1/3; numeric items ~1/10 to 1/20; P(>=4 of 6 mains by blind guess) ~ %.4f' % sum(pb([1/3, .1, .1, .1, .1, .1])[4:]))
# reading load of the diagnostic questions
d = json.load(open(f'{R}/diag/content/p1.json'))
print('\nDiagnostic reading load (words, FK grade):')
for sec in ('foundation', 'core', 'stretch'):
    for i, it in enumerate(d[sec], 1):
        w, s, fk, lw = stats(it['q']); print(' ', sec[:4], i, w, fk, it['q'][:60])

# arithmetic checks used in the report
print('\n=== Arithmetic checks ===')
print('S2 unique:', [(a, 5 - a) for a in range(6) if 10*a + 5*(5-a) == 40], ' S1 unique:', [(x, 10 - x) for x in range(11) if abs(x-(10-x)) == 4 and x < 10 - x])
print('L6 ways to make 20 with 20/10/5:', sum(1 for a in range(2) for b in range(3) for c in range(5) if 20*a+10*b+5*c == 20),
      '| 30:', sum(1 for a in range(2) for b in range(4) for c in range(7) if 20*a+10*b+5*c == 30),
      '| 25:', sum(1 for a in range(2) for b in range(3) for c in range(6) if 20*a+10*b+5*c == 25))
print('L7 squares in 3x3:', sum((3-k+1)**2 for k in range(1, 4)), '| 4x2:', sum((4-k+1)*(2-k+1) for k in range(1, 3)), '| 4x3:', sum((4-k+1)*(3-k+1) for k in range(1, 4)))
print('L8 orders of 3:', len(list(itertools.permutations('AMB'))), '| with Ali not first:', sum(1 for p in itertools.permutations('AMB') if p[0] != 'A'))
print('L2 pairs of 10 (ordered, both parity same):', all((a % 2) == ((10-a) % 2) for a in range(11)), '| of 20:', all((a % 2) == ((20-a) % 2) for a in range(21)))
print('L2 magic triangle side totals possible with 1..6:', sorted({a+b+c for a,b,c in itertools.permutations(range(1,7),3)} & {9,10,11,12,13}))
tri = []
for c in itertools.permutations(range(1, 7), 6):
    A, B, C, ab, bc, ca = c
    if A+ab+B == B+bc+C == C+ca+A: tri.append(A+ab+B)
print('  totals that really work:', sorted(set(tri)))
print('L1 common numbers of 4s and 5s up to 20/50:', [n for n in range(1, 51) if n % 4 == 0 and n % 5 == 0])
print('L5 queue: 3rd from both ends =', 3+3-1, '| 8th from both =', 8+8-1, '| snail 3up/1down on 9cm wall: day', next(d for d in range(1, 20) if 3*d - (d-1) >= 9))
print('L9 ruler 3->9 =', 9-3, '| L10 pattern 5,8,..10th =', 5+3*9, '| 4,9,..7th =', 4+5*6)

# Simple alternative R3: total of 8: 5-8 join (8 with warm-up 4 and >=1 stretch...), 3-4 join+support, 0-2 taster/chat
def r3(w, sc):
    if sc >= 5: return 'JOIN'
    if sc >= 3: return 'JOIN + support' if w >= 3 else 'taster + chat first'
    return 'taster + chat first'
print('\n=== R3: total>=5 join; 3-4 support (taster if warm-up<=2); 0-2 taster ===')
for name, ps in PROF.items():
    o, tot, e = dist_outcomes(ps, r3)
    print(name, {k: round(100 * v) for k, v in sorted(o.items(), key=lambda x: -x[1]) if v > .005})
print('\nSensitivity: typical child with higher accuracy (mains .85 average) under the CURRENT rule')
hi = [.99,.98,.97,.97, .92,.92,.80,.70,.80,.85, .20,.10]
o, tot, e = dist_outcomes(hi); print({k: round(100 * v) for k, v in sorted(o.items(), key=lambda x: -x[1]) if v > .005}, [round(100*x) for x in tot])

# =====================  PART 1: scores (my judgement; evidence is in journey_p1.md)  =====================
# order: Participate, Difficulty fit (3 = just right), Fun, Confidence, Motivation, Social/online
S = {
 1: {'LOW': (4,2,3,2,3,3), 'MID': (5,3,4,3,4,4), 'HIGH': (5,2,4,3,3,3)},
 2: {'LOW': (4,2,3,3,3,3), 'MID': (5,3,4,3,3,4), 'HIGH': (5,2,3,4,3,3)},
 3: {'LOW': (5,3,5,4,4,4), 'MID': (5,4,5,4,4,4), 'HIGH': (5,2,4,4,3,4)},
 4: {'LOW': (5,3,4,3,3,3), 'MID': (5,4,4,4,4,4), 'HIGH': (5,2,3,3,3,3)},
 5: {'LOW': (4,2,3,2,3,3), 'MID': (5,3,4,3,4,4), 'HIGH': (5,3,4,4,4,3)},
 6: {'LOW': (3,1,2,1,2,2), 'MID': (4,2,3,2,3,3), 'HIGH': (5,3,5,4,4,4)},
 7: {'LOW': (4,3,4,3,3,3), 'MID': (5,3,5,4,4,4), 'HIGH': (5,3,5,4,4,3)},
 8: {'LOW': (3,2,3,2,3,3), 'MID': (4,3,4,3,4,4), 'HIGH': (5,3,5,4,4,4)},
 9: {'LOW': (4,2,4,3,3,3), 'MID': (5,3,4,3,4,4), 'HIGH': (5,3,4,4,4,3)},
 10:{'LOW': (3,2,3,3,4,2), 'MID': (4,3,4,4,4,3), 'HIGH': (5,3,5,4,5,4)},
}
print('\n=== HEATMAP (mean of six scores) ===')
print('L   LOW   MID   HIGH')
cells = []
for n in range(1, 11):
    m = {k: sum(v) / 6 for k, v in S[n].items()}
    print('%-3d %.2f  %.2f  %.2f' % (n, m['LOW'], m['MID'], m['HIGH']))
    cells += [(m[k], n, k) for k in m]
for k in ('LOW', 'MID', 'HIGH'):
    print(k, 'level mean %.2f' % (sum(sum(S[n][k]) / 6 for n in S) / 10),
          '| by dimension P,D,F,C,M,S:', [round(sum(S[n][k][i] for n in S) / 10, 1) for i in range(6)])
cells.sort()
print('5 weakest:', [(round(a, 2), n, k) for a, n, k in cells[:7]])
print('3 strongest:', [(round(a, 2), n, k) for a, n, k in cells[-6:]])
ft = 'Fast track. Got both warm-up check questions right and can say why? Ask your tutor. You may go straight to the Think Harder and Challenge pages and the Open investigation while the group works on this page. Come back to the group for talk time.'
print('Fast-track box words:', len(ft.split()))
