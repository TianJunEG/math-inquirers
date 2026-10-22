"""P1 close-the-gaps: adds the Warm-up check slide and the 'What was hard?' look-back slide to deck l<n>,
fixes the timings and text that mention them, and replaces unicode shape glyphs in slide text with drawn shapes.
Call apply(D, n) from gen_lK.py just before p1fix.finish().  Idempotent.
Data: hp/gaps.json (warm-up check questions and answers, open investigation, look-back options)."""
import os, re, json, glob
from slidekit import *
import p1fix

H = os.path.dirname(os.path.abspath(__file__))
GAPS = json.load(open(os.path.join(H, '..', 'hp', 'gaps.json')))
DOT = '<span style="display:inline-block;width:0.8em;height:0.8em;border-radius:50%;background:#1B2A49;vertical-align:-0.08em"></span>'
TRI = '<span style="display:inline-block;width:0;height:0;border-left:0.42em solid transparent;border-right:0.42em solid transparent;border-bottom:0.8em solid #1B2A49;vertical-align:-0.05em"></span>'
BOX = '<span style="display:inline-block;width:0.8em;height:0.8em;border:4px solid #1B2A49;border-radius:8px;background:#FFFFFF;vertical-align:-0.1em;margin-right:12px"></span>'
GLY = {'●': DOT, '▲': TRI}


def _w(D, sid, s):
    open(os.path.join(D, 'slides', sid + '.html'), 'w').write(s)


def dotrow(label, n, col):
    d = ''.join(f'<span style="display:inline-block;width:30px;height:30px;border-radius:50%;background:{col};margin-right:{14 if (i + 1) % 5 == 0 else 6}px"></span>' for i in range(n))
    return f'<div style="display:flex;align-items:center;gap:16px;font-size:30px;font-weight:800"><span style="width:130px">{E(label)}</span>{d}</div>'


def face(k):
    fill = {1: YEL, 2: '#BADCF5', 3: '#F5AA96'}[k]
    mouth = {1: '<path d="M22 46 Q36 62 50 46" fill="none" stroke="#1B2A49" stroke-width="5"/>', 2: '<line x1="24" y1="50" x2="48" y2="50" stroke="#1B2A49" stroke-width="5"/>', 3: '<path d="M22 56 Q36 40 50 56" fill="none" stroke="#1B2A49" stroke-width="5"/>'}[k]
    return (f'<svg aria-label="face" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" style="width:72px;height:72px"><circle cx="36" cy="36" r="32" fill="{fill}" stroke="#1B2A49" stroke-width="5"/>'
            f'<circle cx="25" cy="28" r="4" fill="#1B2A49"/><circle cx="47" cy="28" r="4" fill="#1B2A49"/>{mouth}</svg>')


def build(D, n):
    g = GAPS[str(n)]; p_ = 'l%d-' % n
    # ---- Sneak-peek puzzles (was "Warm-up check"): private, ungraded, ideas we have not learnt yet ----
    body = h2('Sneak-peek puzzles') + chip('Ideas we have not learnt yet. A guess is a great start. Your own paper: show only your tutor.', TEAL, CREAM, 28)
    tags = ['Anyone can try this one: use counters, draw or count', 'Now think about this one']
    for i, c in enumerate(g['check']):
        q = chip(tags[i], YEL if i == 0 else SKY, NAVY, 24) + p(f'<span style="color:{TEAL};font-weight:800">{i + 1}.</span>  {E(c["q"])}', 36, 600, raw=True)
        if n == 3 and i == 0:
            q += dotrow('Red', 7, '#C0392B') + dotrow('Blue', 5, '#2E6DA4') + dotrow('Green', 3, '#1E8449') + p('1 picture = 1 child', 28, 600, MUTED)
        ans = f'<div data-build-in="pop" style="width:470px;flex:none;background:{YEL};border-radius:20px;padding:18px 26px;display:flex;align-items:center"><p style="font-size:34px;font-weight:800;line-height:1.2">{E(c["short"])}</p></div>'
        body += f'<div style="display:flex;gap:24px;align-items:stretch"><div style="flex:1;background:{WHITE};border-radius:24px;padding:20px 34px;display:flex;flex-direction:column;gap:10px">{q}</div>{ans}</div>'
    notes = ('Minutes 7 to 10 (3 minutes). SAY: "These two are sneak-peek puzzles. They are ideas we have not learnt yet, so a guess is a great start, and I do not know is welcome. Nobody is marked." '
             'Question 1 is an access question: every child can try it with objects, a drawing or counting, so everyone starts with a win. Question 2 makes you think. '
             'Answers are not shown on boards in front of the group: face to face, each child holds their own paper low so only the tutor sees it; online, each child shows their own paper to the tutor on camera, or everyone holds paper to the camera at the same moment. There are no private chat messages. '
             'Never use boards held up in front of the group, and never read out or compare anyone\'s answer. Do not write scores down or announce them. '
             'Click to show each answer to the whole group only after everyone has had a try, and say "Lots of us had a different idea, and that is fine." '
             'Look for good ideas to praise in a later lesson; do not keep a list of who found question 2 easy. At minute 40 invite the WHOLE group (“When you have finished Start here, you can choose Think harder, Go further or the Investigation”), never one child by name. Everyone joins Explore and the Mini-lesson. Answers: ' + '  '.join(f'{i + 1}) {c["a"]}' for i, c in enumerate(g['check'])))
    _w(D, p_ + 'warmcheck', sec(p_ + 'warmcheck', '7–10 MIN', body, notes))
    # ---- Look-back (2 minutes, short and safe) ----
    def optrow(items):
        return ''.join(f'<span style="display:inline-flex;align-items:center;margin-right:34px;white-space:nowrap">{BOX}{E(x)}</span>' for x in items)
    rows = [('Something I did well', f'<span style="color:{MUTED}">write or draw one thing</span>'),
            ('The hardest part was ...', optrow(g['hard'] + ['something else'])),
            ('What helped me', optrow(['counters or objects', 'drawing it', 'trying again', 'I asked for help', 'I was not stuck'])),
            ('Next time I will try ...', optrow(['drawing it', 'using objects', 'checking my answer', 'asking a question'])),
            ('If you want', optrow(['I am still stuck (my tutor will come and help)', 'I would like to pass']))]
    body = h2('Look-back') + chip('Two minutes. There are no right answers. You can pass. Nobody reads it out.', TEAL, CREAM, 28)
    inner = ''.join(f'<div style="display:flex;gap:28px;align-items:center;padding:12px 0;{"border-top:2px solid #DCE4F0;" if k else ""}"><p style="width:430px;flex:none;font-size:34px;font-weight:800;color:{TEAL}">{E(a_)}</p><p style="font-size:28px;font-weight:600;line-height:1.5">{b_}</p></div>' for k, (a_, b_) in enumerate(rows))
    body += card(inner)
    notes = ('Minutes 88 to 90 (2 minutes, after the exit ticket). Children tick or write the Look-back box on the Choose and look-back page of their workbook. A pass is always allowed. '
             'It is never marked, never collected in front of the group and never read out; the tutor may look at it afterwards. If a child ticks "I am still stuck", check in during the open session next lesson (a quick visit to the shared breakout room or a hand signal, with a parent nearby; never a direct message). '
             'Do not ask children to share their boxes. Praise the strategy ("Drawing it got you unstuck"), not the speed. The "Next time I will try" row is optional and is never marked; at the start of the next lesson the tutor may say, to the whole group, "Today you could try drawing it, using objects or checking your answer" without naming anyone. Say: "Tick what was hard and what helped you. Write or draw one thing you did well. Then tick one thing you might try next time, if you like. You can pass."')
    _w(D, p_ + 'reflect', sec(p_ + 'reflect', '88–90 MIN', body, notes))


def cleanup(D):
    """Replace unicode shape glyphs in slide text with drawn shapes (CSS-drawn dot / triangle); report any left in SVG text."""
    for f in glob.glob(os.path.join(D, 'slides', '*.html')):
        s = open(f).read(); t = s
        # SVG cross marks (diag/explore.py): draw them
        t = re.sub(r'<text x="([\d.]+)" y="([\d.]+)" font-size="34" font-weight="700" fill="(#[0-9A-Fa-f]{6})"[^>]*>✕</text>',
                   lambda m: f'<line x1="{float(m.group(1)) - 9:.1f}" y1="{float(m.group(2)) - 28:.1f}" x2="{float(m.group(1)) + 9:.1f}" y2="{float(m.group(2)) - 8:.1f}" stroke="{m.group(3)}" stroke-width="5"/><line x1="{float(m.group(1)) - 9:.1f}" y1="{float(m.group(2)) - 8:.1f}" x2="{float(m.group(1)) + 9:.1f}" y2="{float(m.group(2)) - 28:.1f}" stroke="{m.group(3)}" stroke-width="5"/>', t)
        t = t.replace('Frog A: 4s (red ✕)', 'Frog A: 4s (red crosses)').replace('Frog B: 5s (blue ○)', 'Frog B: 5s (blue circles)')
        t = re.sub(r'>([^<>]*[\u25cf\u25b2][^<>]*)<', lambda m: '>' + m.group(1).replace('\u25cf', DOT).replace('\u25b2', TRI) + '<', t)
        if t != s: open(f, 'w').write(t)
        left = re.findall('[■-◿★☆]', t)
        if left: print('p1gaps: glyph left in', os.path.basename(f), set(left))


def apply(D, n):
    p_ = 'l%d-' % n
    build(D, n)
    dj = os.path.join(D, 'deck.json'); deck = json.load(open(dj)); o = deck['order']
    if p_ + 'warmcheck' not in o: o.insert(o.index(p_ + 'warm2') + 1, p_ + 'warmcheck')
    if p_ + 'reflect' not in o: o.insert(o.index(p_ + 'exit') + 1, p_ + 'reflect')
    json.dump(deck, open(dj, 'w'), indent=1, ensure_ascii=False)
    p1fix.relabel(D, p_ + 'warm2', '5–7 MIN'); p1fix.relabel(D, p_ + 'exit', '80–88 MIN')
    if 'If time is short, take questions 1 to 3' not in open(os.path.join(D, 'slides', p_ + 'warm2.html')).read():
        p1fix.patch(D, p_ + 'warm2', [('</aside>', ' If time is short, take questions 1 to 3 only: the 3-minute sneak-peek puzzles follow on the next slide.</aside>')], must=False)
    p1fix.patch(D, p_ + 'title', [('exit ticket 80 to 90.', 'exit ticket 80 to 88, then a two-minute look-back 88 to 90.'),
                                   ('warm-up 0 to 10,', 'warm-up 0 to 10 (game 0 to 5, quick questions 5 to 7, sneak-peek puzzles 7 to 10),')], must=False)
    if os.path.exists(os.path.join(D, 'slides', 'routine.html')): p1fix.patch(D, 'routine', [('<td>A quick game and quick questions</td>', '<td>A quick game, quick questions and 3 minutes of sneak-peek puzzles</td>'),
                                ('<td><b>Exit ticket</b></td><td>One question, then a stamp</td>', '<td><b>Exit ticket</b></td><td>One question, then a stamp, then a two-minute look-back (you can pass)</td>'),
                                ('Think Harder and Challenge are for early finishers or home.</td>', 'Think harder, Go further and the Investigation are in every workbook: choose them any time.</td>')], must=False)
    cleanup(D)
