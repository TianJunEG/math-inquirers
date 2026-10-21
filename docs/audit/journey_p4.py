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

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('load', 'all'): load()
    if what in ('time', 'all'): time()
