"""P1 gifted-style audit: rebuild the Stretch, Challenge and Challenge walk-through slides from hp/qbank.json.

Slide Stretch  = stretch[4:7]   (printed Think Harder T1-T4 = stretch[0:4])
Slide Challenge = challenge[-3:] (printed C1-C3; C3 is always the open / make-up-your-own prompt)
The old 'see it' picture slide (chdiag) drew the retired Challenge items, so it is dropped from the deck order (its file is kept so the older generator steps still run).
Call apply(D, n) from gen_lK.py just before p1fix.finish().  Idempotent.
"""
import os, json
from slidekit import *

H = os.path.dirname(os.path.abspath(__file__))
QB = json.load(open(os.path.join(H, '..', 'hp', 'qbank.json')))
OPT = 'Optional, if you finish early'

def _w(D, sid, s):
    open(os.path.join(D, 'slides', sid + '.html'), 'w').write(s)

def apply(D, n):
    q = QB[str(n)]; p_ = 'l%d-' % n
    st = q['stretch'][4:7]; ch = q['challenge'][-3:]
    assert len(st) == 3 and len(ch) == 3
    # Stretch
    body = h2('Think harder') + ''.join(card(p(f'<span style="color:#1F7A6F">{i+1}.</span>  {E(x["q"])}', 36, 600, raw=True)) for i, x in enumerate(st))
    notes = 'For any pair that chooses to try more (these are on the slide only; Think harder T1 to T4 are in the workbook). Answers: ' + '  '.join(f'{i+1}) {x["a"]}' for i, x in enumerate(st))
    _w(D, p_ + 'stretch', sec(p_ + 'stretch', OPT, body, notes))
    # Challenge (three items; the third is open)
    body = h2('Go further')
    for i, x in enumerate(ch):
        inner = p(f'<span style="color:#1F7A6F">{i+1}.</span>  {E(x["q"])}', 32, 600, raw=True)
        if i == 2: inner = chip('Make up your own', YEL, NAVY, 24) + inner
        body += card(inner)
    notes = ('For any pair that chooses Go further. Use it as a pair choice, or with volunteers in talk time (never call a child by name). Ask for the reason every time. '
             'Q3 is open: there is no single right answer, so ask children to check each other\'s work. Answers: ' + '  '.join(f'{i+1}) {x["a"]}' for i, x in enumerate(ch)))
    _w(D, p_ + 'challenge', sec(p_ + 'challenge', OPT, body, notes))
    # Walk-through: reveal the answers one at a time
    body = h2('Go further: talk it through', 60)
    prompts = ['What do we know? Can you draw it, or use counters?', 'Does anything stay the same? Does anything change?', 'Try it. Can your partner break your rule? Change one thing: what happens?']
    for i, x in enumerate(ch):
        a = x['a']
        inner = f'<p style="font-size:26px;font-weight:800;color:#1F7A6F">Q{i+1}{" (open)" if i == 2 else ""}: {E(prompts[i])}</p><p style="font-size:28px;font-weight:600;line-height:1.3">{E(a)}</p>'
        body += pin(128, 250 + i * 250, 1664, inner, 'rise', WHITE, 20, '18px 30px')
    notes = ('Use after pairs have tried. Reveal one answer at a time and ask a child to explain before you click. '
             'Many children stop at one answer: ask "Is there another way?" and "How do you know you found them all?" '
             'For Q3, ask two pairs to swap puzzles and solve each other\'s.')
    _w(D, p_ + 'chwalk', sec(p_ + 'chwalk', OPT, body, notes))
    # drop the retired picture slide
    dj = os.path.join(D, 'deck.json'); deck = json.load(open(dj))
    deck['order'] = [s for s in deck['order'] if s != p_ + 'chdiag']
    json.dump(deck, open(dj, 'w'), indent=1, ensure_ascii=False)
