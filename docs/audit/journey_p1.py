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
