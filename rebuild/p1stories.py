"""P1 mathematician story break: adds slide l<n>-story ("Story break: <name>") after l<n>-break in deck l<n>.
Call apply(D, n) near the end of gen_lK.py (after p1round2.apply). Idempotent. Data: hp/stories_p1.json."""
import os, json
from slidekit import *

H = os.path.dirname(os.path.abspath(__file__))
ST = json.load(open(os.path.join(H, '..', 'hp', 'stories_p1.json')))


LEG = {8: 'The cats-and-animals picture is our own example, not from Euler\u2019s letters.',
       10: 'The taxi 1729 part is a story that Hardy told himself.'}


def build(n):
    s = ST[str(n)]; sid = 'l%d-story' % n
    facts = (p(f'<b>{E(s["name"])}</b>', 38, 800, NAVY, raw=True)
             + p(E(s['place']) + '  •  ' + E(s['years']), 32, 600, MUTED, raw=True))
    leg = ''
    if s['legend']:
        leg = p(E(LEG[n]), 28, 700, MUTED, raw=True)
    tryit = (chip('Try it (if you like)', YEL, NAVY, 26) + p(E(s['q']), 36, 600, NAVY, raw=True) + leg)
    left = (f'<div style="flex:1;background:{WHITE};border-radius:24px;padding:30px 40px;display:flex;flex-direction:column;gap:12px">'
            f'<p style="font-size:40px;font-weight:600;line-height:1.34">{E(s["story"])}</p></div>')
    right = (f'<div style="width:620px;flex:none;display:flex;flex-direction:column;gap:20px">'
             f'<div style="background:{SOFT};border-radius:24px;padding:22px 30px;display:flex;flex-direction:column;gap:6px">{facts}</div>'
             f'<div data-build-in="rise" style="background:{SKY};border-radius:24px;padding:22px 30px;display:flex;flex-direction:column;gap:12px">{tryit}</div></div>')
    body = (h2('Story break: ' + s['name'], 64)
            + chip('Optional  •  about 2 minutes  •  we can skip it', TEAL, CREAM, 26)
            + f'<div style="display:flex;gap:36px;align-items:flex-start">{left}{right}</div>')
    label = '37–39 MIN, optional'
    leg_note = (' Say it plainly: ' + LEG[n]) if s['legend'] else ''
    notes = ('Story break (optional, 2 minutes, inside the brain break; after the movement, before the worksheet). Read the story aloud slowly, or let a child read one sentence if they want to. '
             'Then, if time allows, click once to show the try-it question; it is only for fun, children may pass, and nobody is marked. '
             f'Link to the lesson: {s["link"]} '
             f'ANSWER to the try-it: {s["a"]}{leg_note} '
             'If the lesson is running late, SKIP this slide and go straight to the worksheet: nothing later depends on it. Keep it to 2 minutes so the break stays at 5 minutes.')
    return sec(sid, label, body, notes)


def apply(D, n):
    sid = 'l%d-story' % n
    open(os.path.join(D, 'slides', sid + '.html'), 'w').write(build(n))
    f = os.path.join(D, 'deck.json'); deck = json.load(open(f)); o = deck['order']
    if sid not in o:
        o.insert(o.index('l%d-break' % n) + 1, sid)
    json.dump(deck, open(f, 'w'), indent=1, ensure_ascii=False)
    bf = os.path.join(D, 'slides', 'l%d-break.html' % n); b = open(bf).read()
    if 'story break' not in b:   # one sentence on the brain-break slide notes
        b = b.replace('</aside>', ' After the movement, there is an optional 2-minute story break (next slide); skip it if you are short of time.</aside>', 1)
        open(bf, 'w').write(b)
