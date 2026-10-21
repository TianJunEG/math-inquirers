"""Helper for docs/audit/journey_p6.md.  Run: python3 docs/audit/journey_p6.py
Part 1: heatmap means from the score table below.
Part 2: verifies the 12 diagnostic answers and computes placement probabilities for the 6 profiles.
Read-only: touches no content file."""
import itertools, json, math, os, random
from fractions import Fraction

# ---------------------------------------------------------------- PART 1
# scores: [Participate, Difficulty fit, Fun, Confidence, Motivation, Social/online]  (5 = best; D is 5 = just right)
S = {
 1: {'LOW': [3,2,3,3,3,2], 'MID': [4,4,4,3,4,3], 'HIGH': [5,3,4,4,4,3]},
 2: {'LOW': [3,2,3,2,3,2], 'MID': [4,3,4,3,4,3], 'HIGH': [5,3,4,4,4,4]},
 3: {'LOW': [4,3,4,3,3,3], 'MID': [5,4,4,4,4,4], 'HIGH': [5,3,4,4,4,3]},
 4: {'LOW': [3,2,3,2,3,2], 'MID': [4,3,4,3,4,4], 'HIGH': [5,3,4,4,4,4]},
 5: {'LOW': [3,2,4,3,3,3], 'MID': [4,3,5,4,4,4], 'HIGH': [5,3,5,4,4,4]},
 6: {'LOW': [4,2,4,2,3,3], 'MID': [5,4,5,4,4,4], 'HIGH': [5,3,5,4,5,4]},
 7: {'LOW': [2,1,3,2,3,2], 'MID': [3,3,4,3,4,4], 'HIGH': [4,4,5,4,5,4]},
 8: {'LOW': [4,2,4,2,3,3], 'MID': [4,3,5,4,5,4], 'HIGH': [5,4,5,4,5,4]},
 9: {'LOW': [4,4,3,3,3,3], 'MID': [5,4,4,4,4,4], 'HIGH': [5,2,3,4,3,3]},
 10:{'LOW': [3,2,3,2,3,1], 'MID': [4,3,4,3,4,3], 'HIGH': [5,3,5,4,5,3]},
}
cells = []
print('HEATMAP (mean of six scores)')
print('L   LOW   MID  HIGH   lesson mean')
for n in range(1, 11):
    m = {p: sum(v) / 6 for p, v in S[n].items()}
    cells += [(m[p], n, p) for p in m]
    print(f'{n:<3} {m["LOW"]:.2f}  {m["MID"]:.2f}  {m["HIGH"]:.2f}   {sum(m.values())/3:.2f}')
for p in ('LOW', 'MID', 'HIGH'):
    print(p, 'level mean %.2f' % (sum(sum(S[n][p]) / 6 for n in S) / 10))
dims = ['Participate', 'DifficultyFit', 'Fun', 'Confidence', 'Motivation', 'Social']
for p in ('LOW', 'MID', 'HIGH'):
    print(p, {d: round(sum(S[n][p][i] for n in S) / 10, 2) for i, d in enumerate(dims)})
cells.sort()
print('weakest 6:', [(round(c[0], 2), c[1], c[2]) for c in cells[:6]])
print('strongest 4:', [(round(c[0], 2), c[1], c[2]) for c in cells[-4:]])

# ---------------------------------------------------------------- PART 2
print('\nVERIFY DIAGNOSTIC ANSWERS')
assert Fraction(5, 2) - Fraction(3, 4) == Fraction(7, 4); print('W1 7/4 ok')
assert 60 * 0.75 == 45; print('W2 45 ok')
assert 180 - 52 - 63 == 65; print('W3 65 ok')
assert 135 / 1.5 == 90 and abs(135 / 1.30 - 103.8) < 0.1; print('W4 90 ok; trap 135/1.30 = %.1f' % (135 / 1.30))
assert (31 - 5) / 2 == 13 and 31 / 2 == 15.5; print('C1 13 ok (halve-first trap gives 10.5 after -5: %.1f)' % (31 / 2 - 5))
pr = [n for n in range(30, 51) if n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))]
print('C2 primes 30-50:', pr, len(pr)); assert len(pr) == 5
assert -4 + 9 - 12 == -7; print('C3 -7 ok')
assert Fraction(7, 12) == Fraction(4 + 3, 12) and Fraction(5, 12) != Fraction(7, 12); print('C4 7/12 ok')
assert 5 * 12 - (8 + 10 + 15 + 11) == 16; print('C5 16 ok; mean of the four =', (8 + 10 + 15 + 11) / 4)
h = (10 + 17) % 12 or 12
print('C6 hour =', h, '(27 on a plain count; 5 = 17 mod 12)'); assert h == 3
dirs = ['N', 'E', 'S', 'W']; assert dirs[(0 + 6) % 4] == 'S'; print('S1 South ok')
ev = [a * 100 + b * 10 + c for a, b, c in itertools.permutations([1, 2, 3, 4], 3) if c % 2 == 0]
print('S2 even 3-digit numbers:', sorted(ev), len(ev)); assert len(ev) == 12
print('S2 trap: all 3-digit numbers =', len(list(itertools.permutations([1, 2, 3, 4], 3))))

# per-question success probabilities (my estimates; see md for reasoning).  order: W1..W4, C1..C6, S1, S2
Q = ['W1', 'W2', 'W3', 'W4', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'S1', 'S2']
PROF = {
 'strong-for-age (12, post-PSLE, AL1-2)':      [.97, .97, .98, .92, .95, .75, .85, .65, .92, .85, .88, .65],
 'typical-for-age (12, post-PSLE, AL3-5)':      [.85, .85, .93, .65, .70, .40, .55, .30, .65, .50, .55, .20],
 'weak-for-age (12, post-PSLE, AL6-8)':         [.35, .40, .60, .15, .30, .15, .25, .10, .20, .20, .25, .05],
 'younger strong (11, P5, not yet PSLE)':       [.85, .75, .90, .35, .85, .55, .60, .45, .70, .80, .80, .60],
 'older weak (13, Sec 1, weak)':                [.50, .50, .75, .30, .35, .50, .50, .15, .35, .30, .35, .10],
 'rusher (capable, careless, falls for traps)': [.85, .70, .90, .55, .50, .40, .45, .30, .40, .35, .50, .30],
 'pure guesser (random answers)':               [.02, .05, .05, .02, .03, .10, .05, .05, .03, .08, .25, .03],
}

def dist(ps):
    d = [1.0]
    for p in ps:
        nd = [0.0] * (len(d) + 1)
        for k, v in enumerate(d):
            nd[k] += v * (1 - p); nd[k + 1] += v * p
        d = nd
    return d

def band(m):
    return 'join' if m >= 6 else ('support' if m >= 4 else 'down')

print('\nPLACEMENT PROBABILITIES (current rule), independent-question model')
print('%-46s %5s %5s | %6s %6s %6s | P(w<=2) | P(join&w<=2)* | P(8/8 & 4/4)' % ('profile', 'E[w]', 'E[m]', 'join', 'supp', 'down'))
RES = {}
for name, ps in PROF.items():
    w, m = dist(ps[:4]), dist(ps[4:])
    ew = sum(k * v for k, v in enumerate(w)); em = sum(k * v for k, v in enumerate(m))
    pj = sum(m[6:]); psup = sum(m[4:6]); pd = sum(m[:4])
    pw2 = sum(w[:3])
    # "support" band with warm-up <= 2 -> suggestion to consider P5
    psup_p5 = psup * pw2
    top = m[8] * w[4]
    RES[name] = (ew, em, pj, psup, pd, pw2, psup_p5, top)
    print('%-46s %5.2f %5.2f | %6.3f %6.3f %6.3f | %6.3f | %6.3f | %6.4f' % (name, ew, em, pj, psup, pd, pw2, psup_p5, top))
    print('     P(P5 suggested) = P(down) + P(support & warm<=2) = %.3f' % (pd + psup_p5))

print('\nIDENTICAL-QUESTION MODEL: probability of each band for a child with true per-question success p (8 scored questions)')
print('  p    P(6-8)  P(4-5)  P(0-3)')
for p in [.3, .4, .5, .55, .6, .65, .7, .75, .8, .85, .9, .95]:
    m = dist([p] * 8)
    print('%5.2f  %6.3f  %6.3f  %6.3f' % (p, sum(m[6:]), sum(m[4:6]), sum(m[:4])))
print('  exactly 8/8 at p=.9: %.3f ; p=.95: %.3f ; p=.8: %.3f' % (.9 ** 8, .95 ** 8, .8 ** 8))

# near-miss sensitivity: a child whose "true" level is the join threshold (p ~ .72 -> E=5.8)
for p in (.70, .72, .75):
    m = dist([p] * 8); print('  p=%.2f  E=%.2f  P(>=6)=%.3f  P(<=5)=%.3f  P(<=3)=%.3f' % (p, 8 * p, sum(m[6:]), sum(m[:6]), sum(m[:4])))

# Guessing: how many questions can be guessed? S1 has 4 sensible answers; C6 12; others open numbers.
g = PROF['pure guesser (random answers)']
print('\nGuesser: P(S1 right by luck) = 0.25; chance of >=4 of 8 by guessing = %.5f ; >=6 = %.2e' % (sum(dist(g[4:])[4:]), sum(dist(g[4:])[6:])))
# Blank-and-skip is allowed ("Try your best, or skip it"), so a refuser scores 0 -> "down".

# Monte-Carlo with shared ability (correlated questions), to show the independence model understates mis-placement
random.seed(6)
def mc(ps, sd=0.12, n=40000):
    out = {'join': 0, 'support': 0, 'down': 0}
    for _ in range(n):
        shift = random.gauss(0, sd)   # day-to-day / child-level shared noise on the logit scale ~ +/-12 points
        sc = 0
        for p in ps[4:]:
            q = min(.99, max(.01, p + shift * (1 - abs(2 * p - 1) * .0)))
            sc += random.random() < q
        out[band(sc)] += 1
    return {k: round(v / n, 3) for k, v in out.items()}
print('\nWith shared day-to-day noise (sd 0.12 on every question):')
for name in ['strong-for-age (12, post-PSLE, AL1-2)', 'typical-for-age (12, post-PSLE, AL3-5)', 'younger strong (11, P5, not yet PSLE)']:
    print('  %-46s %s' % (name, mc(PROF[name])))

# Proposed rule (see md): warm-up decides readiness, main+stretch decides only the *support note*
def proposed(w, m):
    if w >= 3:
        return 'join P6' + (' (tutor note: new topics, first-week catch-up)' if m <= 3 else '')
    if w == 2:
        return 'join P6 with support, or tutor chat'
    return 'tutor chat + free taster; offer P5 only if age <= 12'
print('\nPROPOSED RULE, outcome probabilities')
for name, ps in PROF.items():
    w, m = dist(ps[:4]), dist(ps[4:])
    pj = sum(w[3:]); ps_ = w[2]; pt = sum(w[:2])
    print('  %-46s join %.3f | join-with-support/chat %.3f | taster/chat %.3f' % (name, pj, ps_, pt))
