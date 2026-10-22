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
        tot = {}; opt = 0; optmin = 0; ideas = {}
        for i, sid in enumerate(order):
            h = open(f'{R}/split/p4l{n}/project/slides/{sid}.html').read()
            t = clean(re.sub(r'<aside[\s\S]*?</aside>', '', h))
            m = re.search(r'(\d+)\s*[–-]\s*(\d+)\s*MIN(\s*•\s*OPTIONAL)?', t)
            if not m: continue
            d = int(m.group(2)) - int(m.group(1)); c = cat_of(sid, order, i)
            tot[c] = tot.get(c, 0) + d
            if m.group(3): opt += 1; optmin += d
            elif c in ('mini-lesson', 'teach before page 1', 'teach before page 2'): ideas[c] = ideas.get(c, 0) + 1
        out[n] = (tot, opt, optmin, ideas)
    return out

def time():
    T = time_table()
    cols = ['check', 'warm game', 'quick questions', 'explore', 'mini-lesson', 'key idea', 'brain break', 'teach before page 1', 'page 1 (pairs)', 'check page 1',
            'teach before page 2', 'page 2 (solo)', 'check page 2', 'talk time', 'exit ticket', 'reflection']
    print('L |', ' | '.join(cols), '| sum | optional slides / min')
    for n in range(1, 11):
        tot, opt, om, ideas = T[n]
        print(n, '|', ' | '.join(str(tot.get(c, 0)) for c in cols), '|', sum(tot.get(c, 0) for c in cols), '|', opt, '/', om)
    print('\nL | whole-group minutes on core-level content (quick Qs + mini-lesson + key + teach-before + both page checks + warm game) | page work minutes | non-optional teaching slides in mini-lesson / before page 1 / before page 2 | minutes per teach-before-page-2 idea')
    for n in range(1, 11):
        tot, opt, om, ideas = T[n]
        wg = sum(tot.get(c, 0) for c in ['warm game', 'quick questions', 'mini-lesson', 'key idea', 'teach before page 1', 'teach before page 2', 'check page 1', 'check page 2'])
        pw = tot.get('page 1 (pairs)', 0) + tot.get('page 2 (solo)', 0)
        k = ideas.get('teach before page 2', 0)
        print(n, '|', wg, '|', pw, '|', ideas.get('mini-lesson', 0), '/', ideas.get('teach before page 1', 0), '/', k, '|', round(tot.get('teach before page 2', 0) / k, 1) if k else '-')
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

# ================================================================ SCORES (Part 1)
# Criteria order: Participate, Difficulty fit, Fun/interest, Confidence, Motivation, Social/online.
# Difficulty fit uses 5 = just right (the brief's "3 = just right" would make the six-score mean meaningless); direction is in the note.
CRIT = ['Participate', 'Difficulty fit', 'Fun / interest', 'Confidence', 'Motivation', 'Social / online']
PERSONA = ['LOW', 'MIDDLE', 'HIGH']
LESSON_TITLE = {1: 'Factor Hunters', 2: 'Big Number Puzzles', 3: 'Operation Detectives', 4: 'Fraction Frontier', 5: 'Decimal Detectives',
                6: 'Angle Turns', 7: 'Area Architects II', 8: 'Symmetry and Nets', 9: 'Data Detectives', 10: 'Challenge Day'}
SCORES = {
1: {
 'LOW': [(3, "Check Q1 (lifts at every 3rd and 5th floor) can be started by listing; Q2 (Siti's '30, 60, 90') needs the factor/multiple split that is only taught at min 18-20"),
         (2, "TOO HARD: ws1 Q1 pairs of 48 (3 x 16, 4 x 12), ws2 Q5 table and Q6a four-clue riddle solo in 18 min; three new ideas in 5 min before page 2"),
         (3, "24-tile rectangles (explore) and the bus time line are concrete; Fizz-Buzz is fun until you slip"),
         (3, "'Not this one' is modelled (we1, we2) and Q1 gives '1 x 48' plus empty boxes, but the min-1 check is cold and Q6b asks for a written example"),
         (3, "Buses and bead packs give a purpose; progress is shown only by the end stamp"),
         (3, "Fizz-Buzz goes round the video tiles and 'a child who slips starts the next round' is public; page-1 partner may be sent to Think Harder at min 34")],
 'MIDDLE': [(4, "Both check items can be started; Q2 may get an answer with no reason"),
            (4, "Page 1 right; page 2 Q5/Q6 stretch but are reachable; reading is easy (329 words over two pages)"),
            (4, "Tiles, Fizz-Buzz, bus puzzle"),
            (4, "Worked examples, boxes on Q1 and the 'Stuck?' hint line carry them"),
            (3, "Nothing shows progress inside the lesson except the stamp"),
            (4, "Pair talk on explore and ws1, sentence starters at talk time")],
 'HIGH': [(5, "Both check items solved in seconds"),
          (3, "TOO EASY: quick questions, 12-min mini-lesson and ws1/ws2; Think Harder (Q1-3 same-type, Q4 and locker Q7 good) only starts at min 34"),
          (4, "Locker problem (Challenge Q7) and 'find ALL pairs of bus gaps' (Open) are the highlights; the warm games are trivial"),
          (4, "Early wins; risk is skipping the one-sentence reason and missing the fast track"),
          (4, "Open investigation gives a real goal (six gap pairs, systematic list)"),
          (3, "7 min of page checks and 5 min of teach-before-page-2 on pages they skipped; works alone from 34 to 80")]},
2: {
 'LOW': [(2, "Check Q1 ('which could be the real number: 7 499, 7 500, 8 499, 8 500') needs the halfway rule taught at min 18; Q2 asks why both answers are 50 000, so nothing to write at min 1"),
         (2, "TOO HARD: ws1 Q1 12-cell rounding table with 63 950, 9049, 80 503 traps; Q2 smallest/largest (62 500 / 63 499); ws2 Q4a riddle has four clues"),
         (3, "Place It Right (irreversible boxes) is a good game; the digit-card explore needs the 'no 0 card so start 49' insight"),
         (2, "Cold check, then page 1 opens on the carry trap ('Watch out for 9s'); Q2b hint 'Start at 5340 and check each one' is the one kind scaffold"),
         (3, "Stadium-size numbers and 'what can a rounded number hide' are a fair hook"),
         (3, "Digit cards 0-9 are not in the workbook cut-outs, so a child without them cannot join the explore; '60 045' on whiteboards is public")],
 'MIDDLE': [(4, "Check items doable by testing the four numbers"),
            (3, "Page 1 table plus ws2 Q4-Q6 in 18 min is dense; reading 242 words"),
            (4, "Place It Right, digit cards, stadium hook"),
            (3, "Trap items (63 950) catch most children once; 'Stuck?' number line helps"),
            (4, "Finding 'ALL' numbers that round to 50 000 has a clear aim"),
            (4, "Pair explore and compare-and-argue at talk time (Siti/Ravi)")],
 'HIGH': [(5, "Both check items quick, but the reason sentence must be written"),
          (3, "TOO EASY for core pages; we4 (two clues) shown at 25-27 is 'no longer on the worksheet'"),
          (4, "Place It Right and the five-digit riddles; Open investigation 'double rounding' (test 1 449 and 1 450) is excellent"),
          (4, "Quick wins; the double-rounding conjecture is a real discovery"),
          (4, "Challenge 'how many 5-digit numbers have digit sum 3' and palindrome puzzle give targets"),
          (3, "Listens to page checks on traps already avoided; solo 34-80")]},
3: {
 'LOW': [(3, "Check Q1 (one pair of brackets in 2 + 3 x 4 to make 20) is a try-it puzzle; Q2 (Ravi: 10 - 2 x 3 = 24) needs the order taught at min 18"),
         (1, "FAR TOO HARD: quick questions 4 800 / 6, 99 x 6, 45 x 20 on whiteboards; ws2 Q6 1 236 / 4 = 309; four methods in 5 min before page 2"),
         (2, "Target Numbers is a race ('first child to show a correct number sentence wins a point') that the slow child never wins; quick questions are 'boards up together'"),
         (2, "ws1 Q1a (36 + 14 x 5) is the very trap, Q1c (72 / 8 x 3) is the second; Q7 guess-and-check chains fail in public"),
         (3, "Number tricks that always end in 7 are a real hook if the child reaches Q5"),
         (2, "Speed race and boards-up under time pressure; ws2 has four multi-part items solo, with the tutor unable to see the page")],
 'MIDDLE': [(4, "Check items workable; Q2 maybe answered as 24"),
            (3, "Page 2 is four different tasks (machine, trick, bar model, chains) in 18 min"),
            (4, "Target Numbers, odd/even stand-crouch break, number trick"),
            (3, "Worked examples good; the trap (36 + 14 x 5) is hit once and corrected"),
            (4, "'Why does the trick always give 7?' is a good puzzle"),
            (3, "Race element helps some, discourages others")],
 'HIGH': [(5, "Both check items instant"),
          (3, "TOO EASY: core pages and the mental-maths questions; Think Harder (Challenge Q5 plus/minus puzzle, Q6 Mei's money) is right"),
          (5, "Target Numbers ('can you make 100?'), four 4s, make-any-target Open investigation are real puzzles"),
          (4, "Fast wins; rushing risk on left-to-right slips"),
          (4, "Open investigation 'make targets 1 to 12 from 2, 3, 4, 5' gives an aim"),
          (3, "Waits through ws1 check and the bar-model teach-before while on Think Harder")]},
4: {
 'LOW': [(3, "Warm 'more or less than a half?' thumbs are low-floor; check Q1 ('9/4 cups of flour') uses improper fractions that are only named at min 13-18"),
         (2, "TOO HARD: quick questions 2/3 = ?/12 and 3/4 + 1/8; ws2 Q4 five comparisons (4/9 vs 5/8) each needing 'how you know'; five ideas in the 5 min before page 2"),
         (4, "Pizza slices cut from paper circles are tactile and relatable; the fraction wall is in the cut-outs"),
         (3, "ws1 Q1 (count shaded fifths) is a sure win; Q4 asks for a written reason four times"),
         (3, "Pizza and sweet-jar contexts are purposeful; progress not visible"),
         (3, "Three paper circles must be pre-cut at home; a wrong 'bigger denominator' answer is aired in the talk-time Mei/Ravi claims")],
 'MIDDLE': [(4, "Thumbs and the pizza explore start everyone"),
            (3, "Four ideas in 12 min plus five in 5 min is heavy; Q4-Q6 solo in 18 min"),
            (4, "Pizza party, fraction wall"),
            (3, "Q1 bars and Q3 given bar model give early success; comparing is the hard part"),
            (4, "'Find ALL the twelfths' and 'is Mei right?' invite reasons"),
            (4, "Pairs on bars; thumbs warm-up is safe")],
 'HIGH': [(5, "Check items fast; the 3/8 vs 3/5 reason is one line"),
          (3, "TOO EASY: Q1-Q5 and the comparing tools; Challenge (half is 3 more than a third; Siti's book) fits"),
          (3, "Fractions of sets are routine; Challenge and 'fraction between 2/3 and 3/4' are the fun parts"),
          (4, "Quick wins"),
          (4, "Open investigation 'which fractions of 24 stickers are whole?' links back to Lesson 1 factors"),
          (3, "Page checks on pages skipped; work alone")]},
5: {
 'LOW': [(2, "Check Q1 is the classic 0.8 vs 0.75 and Q2 ('a decimal between 3.4 and 3.5, how do you know it fits?') wants place-value reasoning in 90 seconds"),
         (1, "FAR TOO HARD: thousandths, steps of 0.1/0.01/0.001, rounding to 1 dp and to whole numbers, rounding backwards, 12-number lists, 2.40 / 6; four ideas in 5 min before page 2"),
         (3, "Target 5 digit-box game and the 2.36 m ruler link are fun; then the abstract run starts at min 18"),
         (2, "Warm2 Q3 (0.8 vs 0.75) is deliberately left unsettled in public; Q3b/Q3c rounding detective; ends on the exit 'order 2.8, 2.08, 2.088'"),
         (3, "Prices and masses (cans, $9.40 bar model) give purpose"),
         (2, "Digit and decimal-point cards must be cut at home; 3 rounds of irreversible Target 5 in 2 min is rushed")],
 'MIDDLE': [(3, "Check Q2 open answer is fine; Q1 many say 0.75"),
            (3, "Dense: five teaching slides then page 2 Q4 lists 12 numbers and Q6 needs decimal division"),
            (4, "Target 5, zoom-in lines"),
            (3, "Misconception (more digits = bigger) is met and corrected; page 1 Q1 zoom lines are tricky"),
            (4, "Detective theme with 'check every clue'"),
            (3, "Pairs on page 1; solo page 2 is long")],
 'HIGH': [(5, "Both check items instant"),
          (3, "TOO EASY: ordering and rounding; Challenge (2.459 clue, apples and pear) and Open 'no decimal between 0.35 and 0.36?' are right"),
          (4, "Open investigation (is there a next decimal?) is the best idea in the lesson"),
          (4, "Quick wins on core"),
          (4, "Closest-to puzzles (Think Harder) and 'make your own' Challenge"),
          (3, "Waits through three slides on place-value chart and page checks")]},
6: {
 'LOW': [(4, "Robot turns and the paper clock are physical; check Q2 (90 - 35) is easy and Q1 can be done with fingers on a compass"),
         (3, "A LITTLE TOO HARD: protractor (inside/outside scale, c and d turned) is the gate; arithmetic is light; page 2 four tasks in 18 min"),
         (4, "Standing turns, compass dance, paper clock hands-on"),
         (3, "ws1 Q1 'My estimate' can never be wrong and answers within 2 degrees count; Q5 corner sums are quick"),
         (4, "Clocks and robots are everyday; stamp"),
         (3, "Protractor, ruler and paper clock must be at home (only right-angle testers are in the workbook); the tutor cannot see protractor placement; mirrored self-view reverses turns")],
 'MIDDLE': [(4, "Everyone can turn and answer"),
            (4, "Right pitch; page 1 measuring takes the time"),
            (4, "Standing and moving, clock puzzles"),
            (4, "Estimate-first routine protects against 140 vs 40"),
            (4, "Fan of angles 'find ALL' has an aim"),
            (4, "Whole-body activity on camera, pairs on fan")],
 'HIGH': [(5, "Check items instant"),
          (2, "TOO EASY: protractor, clock spaces, compass; 'What is the angle at 3:30?' (75) is the first real challenge"),
          (3, "Challenge Q1 (3:30) and the two-squares overlap are good; most of the lesson is procedural"),
          (4, "Early wins"),
          (3, "Open 'splitting a corner into three angles' (7 sets) has an aim but only for the fast track"),
          (3, "Stand-and-turn games are shared; waits through measuring checks")]},
7: {
 'LOW': [(3, "Check Q1/Q2 are spoken (6 m x 4 m room, 2 m x 1 m cut from a corner) with no picture; Q2 asks 'explain how you know' the perimeter is unchanged"),
         (2, "TOO HARD: 21 sub-items in 34 min (1.6 min each); missing lengths, area two ways, staircase, frame; 'layers' (Q4b) undefined"),
         (4, "12 tiles, A/P cards, 'six tiles' (Q3) and the body-shapes break are hands-on"),
         (3, "Q3 any six-tile shape works; Q2 table fills row by row; Q4a 'show Ravi' needs a written method"),
         (4, "Architects with fences and carpets is a good hook"),
         (3, "24 paper squares and scissors prepared at home; square-grid page is provided")],
 'MIDDLE': [(4, "Check Q1 workable from the words"),
            (3, "Dense page 2 (staircase, cut-and-rearrange, frame)"),
            (4, "Tiles and A/P cards"),
            (4, "Q3 and Q2 give wins; border Q6c is a good 'what did she forget'"),
            (4, "Same area, different perimeter is a real surprise"),
            (4, "Pair tile work")],
 'HIGH': [(5, "Check items instant"),
          (3, "TOO EASY on core; Challenge (two paths cross the garden; 9 by 4 cut into a square) is right"),
          (4, "Six-tile perimeters, Ravi's fence (extension), paths puzzle"),
          (4, "Early wins"),
          (4, "Open 'bigger area, bigger perimeter?' with all six 24 cm rectangles"),
          (3, "Work alone from 34; page checks on pages skipped")]},
8: {
 'LOW': [(4, "Check Q1 (straight row of 6 squares, can fold paper) and Q2 (H and A, fingers) need almost no reading"),
         (4, "A BIT HARD in places: fold-in-the-head (ws1 Q1 shapes B, D, F) and drawing mirror images (Q4) are spatial, not arithmetic; no calculations"),
         (5, "Paper cube, dice nets, mirror-partner break, letters with fingers"),
         (4, "Q3 dice nets use the known 7-sum; ws1 mostly ticks and numbers; cube net is in the workbook"),
         (4, "'I made a cube' is visible progress"),
         (3, "6 paper squares, tape and scissors must be ready; folding on camera is hard to check")],
 'MIDDLE': [(4, "Everyone can fold or finger-answer"),
            (4, "Good pitch; coordinate Q6 (A2, D3) is the stretch"),
            (5, "Nets, dice, mirrors"),
            (4, "Tick/draw rather than write; Q5 diagonal trap is taught first"),
            (4, "Eleven nets is a good 'find them all'"),
            (4, "Pair folding, mirror partner on camera")],
 'HIGH': [(5, "Check items instant"),
          (3, "TOO EASY on core; Think Harder (22-square cuboid net, two glued dice) fits"),
          (5, "Design your own dice, X and plus symmetry puzzle"),
          (4, "Quick wins"),
          (4, "Open 'row of four' (16 cases) is excellent"),
          (3, "Works alone; checks on skipped pages")]},
9: {
 'LOW': [(4, "Warm 'which graph tells the story' has no numbers; check Q1 (halfway between 100 and 150) is easy; Q2 asks for an abstract reason about scales"),
         (3, "A BIT HARD: scale reading is fine; 85 - 38 and 70 - 29 regrouping, same-jump table, and Q5 'two shops' scale argument are abstract"),
         (3, "Sugarcane juice and money boxes are fine; plotting 7 points with a ruler can drag"),
         (4, "Q1a (read Thursday = 75) is a sure first win; table totals can be checked two ways"),
         (3, "Some purpose in 'catch the misleading graph'"),
         (3, "Printed blank grid, ruler and two pencils must be ready (the workbook has no graph grid for Lesson 9); 'choose a scale' alone is exposing")],
 'MIDDLE': [(4, "Everyone can match graph to story"),
            (4, "Right pitch; Q5 is the stretch"),
            (3, "Graphs are only mildly exciting"),
            (4, "Reading and totals give early wins"),
            (3, "'Is the graph telling the truth?' is the one hook"),
            (4, "Pair plotting")],
 'HIGH': [(5, "Check items instant"),
          (2, "TOO EASY: reading values, listing changes, table totals; only Challenge (tanks cross at 4 h) and the scale argument stretch"),
          (3, "Mostly reading; the misleading-graph idea is nice"),
          (3, "Quick wins but little to be proud of"),
          (2, "Open 'three plants' is a calculation table; little curiosity"),
          (3, "Waits through slides on reading and totals")]},
10: {
 'LOW': [(3, "Check Q1 (ducks/rabbits, 8 animals, 22 legs) can be guessed or drawn; Q2 (add 7, double, get 30) can be undone; 'Who am I?' grid is easy"),
         (2, "TOO HARD: four puzzle cards in 5 min; ws1 Q1a (next-door numbers make 552 = 23 x 24), Q1b ($4 pens, $7 notebooks); ws2 Q6 'in 5 years' ages"),
         (3, "Logic and queue puzzles are fun; five puzzle types back to back are not"),
         (3, "The hook normalises 'you do not know how to start'; the logic grid (Q4) is a likely win; the group 'teach one puzzle' is exposing"),
         (4, "Certificate, last stamp and a specific thing each child did well"),
         (3, "Breakout pair per card then report back; talk-time 'teach it in two sentences'")],
 'MIDDLE': [(4, "Who am I and puzzle cards start everyone"),
            (3, "Hard but sequenced: four ways in are taught one at a time"),
            (4, "Puzzles are the fun part"),
            (4, "Strategy names ('suppose', 'work backwards') give hooks; certificate"),
            (5, "No new topic; certificate; 'tell a specific thing'"),
            (4, "Pairs and talk time")],
 'HIGH': [(5, "Cards and Who am I are instant"),
          (4, "Right: competition-style puzzles; the heads-and-legs suppose method and Challenge are new"),
          (5, "Four puzzle stations, logic grid, make-your-own heads-and-legs"),
          (5, "Real struggle on real puzzles with a method to try"),
          (5, "Open 'ring toss scores' (3 and 5 points) find ALL; certificate"),
          (4, "Breakout pairs, teach to the group")]},
}


def table_scores():
    rows = []
    for n in range(1, 11):
        r = [n, LESSON_TITLE[n]]
        for p in PERSONA:
            sc = [x[0] for x in SCORES[n][p]]
            r.append(round(sum(sc) / 6, 2))
        rows.append(r)
    return rows

def heatmap():
    print('| Lesson | LOW | MIDDLE | HIGH |')
    print('|---|---|---|---|')
    for n, t, a, b, c in table_scores():
        print(f'| {n} {t} | {a:.2f} | {b:.2f} | {c:.2f} |')
    for i, p in enumerate(PERSONA):
        print(p, 'mean of lesson means', round(sum(r[2 + i] for r in table_scores()) / 10, 2))
    print('criterion means (all lessons):')
    for k, c in enumerate(CRIT):
        print(' ', c, {p: round(sum(SCORES[n][p][k][0] for n in range(1, 11)) / 10, 2) for p in PERSONA})
    cells = sorted(((table_scores()[n - 1][2 + i], n, p) for n in range(1, 11) for i, p in enumerate(PERSONA)))
    print('weakest 8 cells:', cells[:8]); print('strongest 6 cells:', cells[-6:])

def lesson_md():
    out=[]
    for n in range(1,11):
        out.append(f"### Lesson {n}: {LESSON_TITLE[n]}\n")
        for pe in PERSONA:
            sc=SCORES[n][pe]; m=sum(x[0] for x in sc)/6
            out.append(f"**{pe}** (mean {m:.2f})\n")
            out.append("| Criterion | Score | Evidence |\n|---|---|---|")
            for c,(v,t) in zip(CRIT,sc): out.append(f"| {c} | {v} | {t} |")
            out.append("")
    return "\n".join(out)


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('load', 'all'): load()
    if what in ('time', 'all'): time()
    if what in ('diag', 'all'): diag()
    if what in ('heat', 'all'): heatmap()
    if what == 'lessons': print(lesson_md())


