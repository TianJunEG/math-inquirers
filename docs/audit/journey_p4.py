"""Helper for docs/audit/journey_p4.md. READ-ONLY analysis of the P4 content (no content file is edited).
Run from anywhere:  python3 -I docs/audit/journey_p4.py [load|time|diag|all]
  load : reading and writing load per lesson (core worksheet pages, Think Harder pages, warm-up check items)
  time : minute accounting per lesson from the slide time labels (doing / listening / waiting) and optional slides
  diag : arithmetic check of the P4 placement diagnostic, cut-score maths and the six-profile simulation
The per-lesson 1-5 scores are held in the table SCORES at the bottom (so the heatmap in the report is computed, not typed).
"""
import re, html, json, math, random, glob, os, sys, itertools
R = '/home/claude/math-inquirers'

# ---------------------------------------------------------------- helpers
def syl(w):
    w = re.sub(r'[^a-z]', '', w.lower())
    if not w: return 0
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1: n -= 1
    return max(n, 1)

def stats(s):
    s2 = re.sub(r'_+', ' ', s)
    words = re.findall(r"[A-Za-z']+", s2)
    sents = max(1, len(re.findall(r'[.?!]', s2)))
    syls = sum(syl(w) for w in words)
    fk = 0.39 * len(words) / sents + 11.8 * syls / max(1, len(words)) - 15.59 if words else 0
    return len(words), sents, round(fk, 1)

def clean(h):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<svg[\s\S]*?</svg>', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg[\s\S]*?</svg>', ' ', h))))).strip()

CHECKQ = {}
def _checkq():
    import subprocess
    js = "const L=require('/home/claude/math-inquirers/p4/data.js');const o={};L.content.forEach((c,i)=>o[i+1]=c.gaps.check.map(x=>x.q));console.log(JSON.stringify(o))"
    r = subprocess.run(['node', '-e', js], capture_output=True, text=True, cwd=f'{R}/p4')
    for k, v in json.loads(r.stdout).items(): CHECKQ[int(k)] = v
_checkq()
# ---------------------------------------------------------------- LOAD
def load():
    raw = open(f'{R}/p4/workbook_body.html').read()
    badges = [(m.start(), int(m.group(1))) for m in re.finditer(r'<span class="lbadge">Lesson (\d+)</span>', raw)]
    first, second = {}, {}
    for pos, n in badges:
        (second if n in first else first)[n] = pos
    end_all = raw.index('Cut-outs')
    rows = []
    print('L | CORE pages (2): words / FK grade / main Qs / sub-items / "explain/why" prompts / longest item words | THINK HARDER+open: words / FK | check Q1+Q2 words | writing-prompt share')
    gaps = {}
    for n in range(1, 11):
        a, b = first[n], second[n]
        c = second[n + 1] if False else (first[n + 1] if n < 10 else end_all)
        core = raw[a:b]; th = raw[b:c]
        main_q = len(re.findall(r'class="p q', core)); subs = len(re.findall(r'class="p sub', core))
        items = re.findall(r'<div class="p (?:q|sub)[^>]*>(.*?)</div>', core, flags=re.S)
        longest = max((stats(clean(i))[0] for i in items), default=0)
        txt = clean(core)
        why = len(re.findall(r'explain|how do you know|how did you know|why|what do you notice|write how|what did she forget|show ravi', txt, flags=re.I))
        w, s, fk = stats(txt)
        tw, ts, tfk = stats(clean(th))
        dj = json.load(open(f'{R}/split/p4l{n}/project/deck.json'))
        cw = [stats(q)[0] for q in CHECKQ[n]]
        rows.append((n, w, fk, main_q, subs, why, longest, tw, tfk, cw))
        print(n, '|', w, '/', fk, '/', main_q, '/', subs, '/', why, '/', longest, '|', tw, '/', tfk, '|', cw)
    return rows

# ---------------------------------------------------------------- TIME
CAT = [('check', 'check'), ('warm1', 'warm game'), ('warm2', 'quick questions'), ('explore', 'explore'), ('key', 'key idea'),
       ('break', 'brain break'), ('ws1ans', 'check page 1'), ('ws2ans', 'check page 2'), ('ws1', 'page 1 (pairs)'), ('ws2', 'page 2 (solo)'),
       ('talk', 'talk time'), ('exit', 'exit ticket'), ('reflect', 'reflection')]
def cat_of(sid, order, i):
    s = sid.split('-', 1)[1]
    for k, v in CAT:
        if s.startswith(k): return v
    if s in ('title', 'end'): return 'title'
    if s in ('stretch', 'challenge', 'chdiag', 'chwalk'): return 'think harder (no slot)'
    # teach / we / try: before the break = mini-lesson, between ws1ans and ws2 = teach before page 2, between break and ws1 = teach before page 1
    pos_break = next(j for j, x in enumerate(order) if x.split('-', 1)[1] == 'break')
    pos_ws1 = next(j for j, x in enumerate(order) if x.split('-', 1)[1] == 'ws1')
    pos_ws2 = next(j for j, x in enumerate(order) if x.split('-', 1)[1] == 'ws2')
    if i < pos_break: return 'mini-lesson'
    if i < pos_ws1: return 'teach before page 1'
    if i < pos_ws2: return 'teach before page 2'
    return 'other'

def time_table():
    out = {}
    for n in range(1, 11):
        dj = json.load(open(f'{R}/split/p4l{n}/project/deck.json')); order = dj['order']
        tot = {}; opt = 0; optmin = 0
        for i, sid in enumerate(order):
            h = open(f'{R}/split/p4l{n}/project/slides/{sid}.html').read()
            t = clean(re.sub(r'<aside[\s\S]*?</aside>', '', h))
            m = re.search(r'(\d+)\s*[–-]\s*(\d+)\s*MIN(\s*•\s*OPTIONAL)?', t)
            if not m: continue
            d = int(m.group(2)) - int(m.group(1)); c = cat_of(sid, order, i)
            tot[c] = tot.get(c, 0) + d
            if m.group(3): opt += 1; optmin += d
        out[n] = (tot, opt, optmin)
    return out

def time():
    T = time_table()
    cols = ['check', 'warm game', 'quick questions', 'explore', 'mini-lesson', 'key idea', 'brain break', 'teach before page 1', 'page 1 (pairs)', 'check page 1',
            'teach before page 2', 'page 2 (solo)', 'check page 2', 'talk time', 'exit ticket', 'reflection']
    print('L |', ' | '.join(cols), '| sum | optional slides / min')
    for n in range(1, 11):
        tot, opt, om = T[n]
        print(n, '|', ' | '.join(str(tot.get(c, 0)) for c in cols), '|', sum(tot.get(c, 0) for c in cols), '|', opt, '/', om)
    # listening/waiting for a fast-tracked HIGH child: mini-lesson + teach-before + both page checks + key idea
    print('\nL | minutes tutor-led whole-group teaching or answer-checking (mini-lesson + key + teach-before pages + page checks) | solo/pair working minutes (page1+page2) | minutes of page work per worksheet sub-item')
    return T


# ---------------------------------------------------------------- DIAG
from fractions import Fraction
from math import comb
DJ = json.load(open(f'{R}/diag/content/p4.json'))

def poisson_binomial(ps):
    dist = [1.0]
    for p in ps:
        new = [0.0] * (len(dist) + 1)
        for k, q in enumerate(dist):
            new[k] += q * (1 - p); new[k + 1] += q * p
        dist = new
    return dist

def verify_diag():
    print('--- arithmetic and uniqueness checks of the 12 diagnostic questions')
    chk = []
    chk.append(('W1 5000-1346', 5000 - 1346, 3654))
    chk.append(('W2 9x7', 9 * 7, 63))
    chk.append(('W3 2/3=?/12', Fraction(2, 3) * 12, 8))
    chk.append(('W4 7x6', 7 * 6, 42))
    chk.append(('Q5 factors of 18', [d for d in range(1, 19) if 18 % d == 0], [1, 2, 3, 6, 9, 18]))
    chk.append(('Q6 round 48572 to 1000', int(round(48572 / 1000 + 1e-9)) * 1000, 49000))
    chk.append(('Q7 12+6x3-4', 12 + 6 * 3 - 4, 26))
    chk.append(('Q8 2 3/5 + 1 4/5', Fraction(13, 5) + Fraction(9, 5), Fraction(22, 5)))
    chk.append(('Q9 3.7+2.85', round(3.7 + 2.85, 2), 6.55))
    chk.append(('Q10 width', 36 // 2 - 11, 7))
    s1 = [n for n in range(31, 50) if n % 4 == 0 and n % 6 == 0 and sum(map(int, str(n))) == 9]
    chk.append(('S1 puzzle (unique?)', s1, [36]))
    s2 = [(c, 3 * c) for c in range(1, 200) if 3 * c - 12 == c + 12]
    chk.append(('S2 transfer (unique?)', s2, [(12, 36)]))
    for name, got, want in chk: print(f'  {name}: {got}  expected {want}  {"OK" if got == want else "MISMATCH"}')
    print('  common-error claims in the tutor key:')
    print('   Q1 4346 (subtract smaller digit from larger in each column):', int(''.join(str(abs(int(a) - int(b))) for a, b in zip('5000', '1346'))))
    print('   Q7 left to right:', (12 + 6) * 3 - 4, '(key says 50)')
    print('   Q10 36-11 =', 36 - 11, ' 36-11-11 =', 36 - 11 - 11, '(key says 25 or 14)')
    print('   Q9 key says common error 6.12 or 5.82. Real misalignments give: digits added as whole numbers 37+285 =', 37 + 285, '-> 3.22; 3.07+2.85 =', round(3.07 + 2.85, 2), '; neither is 6.12 or 5.82')

def cut_tables():
    print('--- 8 questions, cut scores 6-8 / 4-5 / 0-3, children with the SAME chance p on every item (independent model)')
    print('p    mean  P(6-8)  P(4-5)  P(0-3)')
    for p in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]:
        d = poisson_binomial([p] * 8)
        print(f'{p:.2f} {8*p:4.1f}  {sum(d[6:]):.3f}   {sum(d[4:6]):.3f}   {sum(d[:4]):.3f}')
    print('standard deviation of an 8-item score at p=.5: %.2f marks; at p=.75: %.2f marks' % (math.sqrt(8 * .25), math.sqrt(8 * .75 * .25)))
    print('--- warm-up (4 items): P(warm-up <=2) and P(4/4)')
    for p in [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]:
        d = poisson_binomial([p] * 4)
        print(f'p={p:.2f}  P(<=2)={sum(d[:3]):.3f}  P(4/4)={d[4]:.3f}  P(12/12 all)={p**12:.3f}  P(8/8 and 4/4)=P(12/12)')

PROFILES = {  # per-item chances (my estimates, NOT measured; order = 4 warm-up, 6 main, 2 stretch)
 'A strong-for-age (10, finishing P4)':  ([.98, .99, .97, .95], [.97, .93, .95, .88, .93, .92], [.85, .55]),
 'B typical-for-age (10, finishing P4)': ([.88, .95, .88, .85], [.85, .75, .78, .62, .75, .72], [.40, .10]),
 'C weak-for-age (10, finishing P4)':    ([.55, .80, .45, .60], [.40, .35, .25, .12, .45, .20], [.08, .01]),
 'D younger and strong (9, finishing P3)': ([.95, .98, .90, .92], [.55, .65, .35, .25, .55, .80], [.50, .25]),
 'E older and weak (11, finishing P5)':  ([.75, .90, .60, .80], [.50, .50, .40, .25, .50, .40], [.10, .02]),
 'F rusher / guesser (10, capable)':     ([.80, .95, .70, .55], [.60, .55, .50, .25, .45, .45], [.25, .05]),
}

def place(warm, ms):
    if ms >= 6: return 'P4 (try P5 check)' if (ms == 8 and warm == 4) else 'P4'
    if ms >= 4: return 'P4 + support, P3 suggested' if warm <= 2 else 'P4 + support'
    return 'P3 (one level down)'

def sim(n=200000, day_sd=0.0, seed=1):
    rnd = random.Random(seed)
    res = {}
    for name, (w, m, s) in PROFILES.items():
        cnt = {}; tot = 0.0; wt = 0.0
        for _ in range(n):
            shift = rnd.gauss(0, day_sd) if day_sd else 0.0
            def hit(p):
                if shift:
                    lo = math.log(p / (1 - p)) + shift; p = 1 / (1 + math.exp(-lo))
                return rnd.random() < p
            ww = sum(hit(p) for p in w); ms = sum(hit(p) for p in m + s)
            k = place(ww, ms); cnt[k] = cnt.get(k, 0) + 1; tot += ms; wt += ww
        res[name] = (wt / n, tot / n, {k: v / n for k, v in cnt.items()})
    return res

def profiles():
    for sd, label in [(0.0, 'independent items'), (0.6, 'with a child-level day effect (logit SD 0.6, so slips and good days are correlated)')]:
        print(f'--- six profiles, {label}')
        R_ = sim(60000, sd)
        for name, (wm, mm, d) in R_.items():
            print(f'{name}: mean warm-up {wm:.2f}/4, mean main+stretch {mm:.2f}/8')
            for k, v in sorted(d.items(), key=lambda x: -x[1]): print(f'     {v*100:5.1f}%  {k}')
    # exact distribution of main+stretch score for B (independent)
    for name in PROFILES:
        w, m, s = PROFILES[name]; d = poisson_binomial(m + s)
        print(name.split(' ')[0], 'exact score distribution 0..8:', [round(x, 3) for x in d], ' P(6-8)=%.2f P(4-5)=%.2f P(0-3)=%.2f' % (sum(d[6:]), sum(d[4:6]), sum(d[:4])))
    # pure guesser: open numeric answers, 2-way traps count as coin flips
    g = [.01, .01, .05, .01, .02, .45, .30, .03, .08, .30, .02, .01]
    d = poisson_binomial(g[4:])
    print('blind guesser (rounding up/down, order of operations, 7 vs 25 are coin-flips; the rest nearly 0): mean main+stretch %.2f, P(>=4)=%.3f, P(>=6)=%.4f' % (sum(g[4:]), sum(d[4:]), sum(d[6:])))
    d2 = poisson_binomial(g[:4]); print('   warm-up for the same guesser: mean %.2f' % sum(g[:4]))

def diag():
    verify_diag(); cut_tables(); profiles()

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('load', 'all'): load()
    if what in ('time', 'all'): time()
    if what in ('diag', 'all'): diag()
