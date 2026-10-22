"""Math Inquirers P2 re-budget (docs/audit/timing_p2.md section 6/7): every lesson fits 90 minutes when run live online.

ONE source of truth for the minutes:   PARTS  (part budgets, sum 90)   and   SLIDES  (slide pills).
  python3 rebuild/p2budget.py            writes p2/budget.json (read by p2/guide.js for the seg() times and by the tutor console)
  p2gaps.add(S, K) calls apply(S, K)     rewrites every slide pill and every leading 'Minutes a to b' in the speaker notes
The generators' own literals ('8-14 MIN', 'Minutes 8 to 14.') are the OLD clock times: they are overwritten here, so edit minutes in THIS file only.
Slide timing: SLIDES[K][short id] = (start, end) or OPT (optional, if you finish early: no clock time, not in the tutor timer).
"""
import json, os, re

OPT = 'OPT'
OPT_PILL = 'Optional, if you finish early'

def fmt(x):
    return ('%g' % x)

# ---- part budgets (title, minutes) in lesson order; start/end are computed. Each list sums to 90. ----
def _std(mini=12.0, brk=3.0, p1=14.0, pre=None, c1=2.5, teach=4.5, p2=11.5, c2=2.5, flex=3.0, close=('Closing and stamps', 1.5), pre_title=None):
    parts = [('Opening', 1.5), ('Sneak-peek puzzles', 4.5), ('Warm-up', 4.5), ('Explore', 13.0), ('Mini-lesson', mini), ('Brain break', brk)]
    if pre: parts.append((pre_title or 'Worksheet teach slide', pre))
    parts += [('Worksheet page 1 (pairs)', p1), ('Check together, page 1', c1), ('Short teaching', teach), ('Worksheet page 2 (alone)', p2),
              ('Check together, page 2', c2), ('Flex (spare time)', flex), ('Talk time', 5.0), ('Exit ticket', 5.0), ('Looking back', 2.0), close]
    return parts

PLAN = {
    1: _std(),
    2: _std(),
    3: _std(),
    4: _std(teach=2.5, flex=5.0),
    5: _std(pre=2.5, p1=11.5),
    6: _std(pre=2.5, p1=11.5),
    7: _std(),
    8: _std(),
    9: _std(mini=10.5, flex=4.5),
    10: _std(mini=10.0, pre=2.5, p1=12.0, teach=3.5, flex=4.0, close=('Certificates and closing', 3.0)),
}

def parts(K):
    out = []; t = 0.0
    for title, m in PLAN[K]:
        out.append({'title': title, 'start': round(t, 2), 'end': round(t + m, 2)}); t += m
    assert abs(t - 90) < 1e-9, (K, t)
    return out

# ---- slide pills: SLIDES[K] = {short id: (start, end) | OPT}.  Filled below, lesson by lesson. ----
SLIDES = {}
OPTIONAL_COMMON = ['stretch', 'challenge', 'chdiag', 'chwalk']

def _tl(K, **kw):
    """Standard slide windows. Returns dict; kw overrides/extends."""
    p = {x['title']: (x['start'], x['end']) for x in parts(K)}
    return p

def budget_json():
    out = {'lessons': {}}
    for K in range(1, 11):
        sl = SLIDES.get(K, {})
        out['lessons'][str(K)] = {'parts': parts(K), 'optional_slides': [f'p2l{K}-{k}' for k, v in sl.items() if v == OPT]}
    return out

# ---------------------------------------------------------------------------------------------------------------
PILL = re.compile(r'(<p style="position:absolute;right:128px;top:64px;[^>]*>)([^<]*)(</p>)')
OLDMIN = re.compile(r'>(\d+(?:\.\d+)?[–-]\d+(?:\.\d+)?) MIN<')
NOTE = re.compile(r'(<aside>)(Minutes? \d+(?:\.\d+)? to \d+(?:\.\d+)?)(?=[ .(])')

def label(se):
    return f'{fmt(se[0])}–{fmt(se[1])} MIN'

def apply(S, K):
    """Set the pill and the leading 'Minutes a to b' of each slide in S (dict id -> html). Slides without an entry keep their text (title, break pills are matched too)."""
    P = f'p2l{K}-'; tab = SLIDES[K]
    missing = [i for i in S if i[len(P):] not in tab and i[len(P):] != 'title']
    assert not missing, ('slides without a time in p2budget.SLIDES[%d]' % K, missing)
    for i in list(S):
        short = i[len(P):]
        if short == 'title': continue
        se = tab[short]; h = S[i]
        if se == OPT:
            h, n = PILL.subn(lambda m: m.group(1) + OPT_PILL + m.group(3), h, count=1)
            if not n: raise SystemExit('no pill in ' + i)
            h = NOTE.sub(lambda m: m.group(1) + 'Optional, if you finish early (no clock time)', h, count=1)
            if '<aside>Optional, if you finish early' not in h:
                h = h.replace('<aside>', '<aside>Optional, if you finish early (no clock time). ', 1)
        else:
            lab = label(se)
            if PILL.search(h): h = PILL.sub(lambda m: m.group(1) + lab + m.group(3), h, count=1)
            elif OLDMIN.search(h): h = OLDMIN.sub('>' + lab + '<', h, count=1)
            else: raise SystemExit('no pill in ' + i)
            txt = f'Minutes {fmt(se[0])} to {fmt(se[1])}'
            if NOTE.search(h): h = NOTE.sub(lambda m: m.group(1) + txt, h, count=1)
            else: h = h.replace('<aside>', f'<aside>{txt}. ', 1)
        S[i] = h
    return S

def plan_sentence(K):
    """The 'Time plan' of the title-slide notes."""
    ps = parts(K); a = lambda x: f"{x['title'].lower().replace(' (pairs)', '').replace(' (alone)', '')} {fmt(x['start'])} to {fmt(x['end'])}"
    return 'Time plan: ' + ', '.join(a(x) for x in ps) + '. The Think harder and Go further slides are optional, if you finish early (no clock time).'
