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
    # ---- Warm-up check ----
    body = h2('Warm-up check') + chip('Whiteboards: answer and say how you know', TEAL, CREAM, 28)
    for i, c in enumerate(g['check']):
        q = p(f'<span style="color:{TEAL};font-weight:800">{i + 1}.</span>  {E(c["q"])}', 36, 600, raw=True)
        if n == 3 and i == 0:
            q += dotrow('Red', 7, '#C0392B') + dotrow('Blue', 5, '#2E6DA4') + dotrow('Green', 3, '#1E8449') + p('1 picture = 1 child', 28, 600, MUTED)
        ans = f'<div data-build-in="pop" style="width:470px;flex:none;background:{YEL};border-radius:20px;padding:18px 26px;display:flex;align-items:center"><p style="font-size:34px;font-weight:800;line-height:1.2">{E(c["short"])}</p></div>'
        body += f'<div style="display:flex;gap:24px;align-items:stretch"><div style="flex:1;background:{WHITE};border-radius:24px;padding:24px 34px;display:flex;flex-direction:column;gap:10px">{q}</div>{ans}</div>'
    notes = ('Minutes 7 to 10 (3 minutes). Two questions on the key idea in a new setting. Children write their answer and how they know on a whiteboard and show it on a count of three; click to show each answer. '
             'Ask one or two children "How do you know?". Quietly note who got both right and gave a reason: those children may start the worksheet on the Think Harder page (then Challenge and the Open investigation) while the group works on the core page. '
             'Tell them privately at minute 40; do not announce names or scores. Everyone still joins Explore and the Mini-lesson. Answers: ' + '  '.join(f'{i + 1}) {c["a"]}' for i, c in enumerate(g['check'])))
    _w(D, p_ + 'warmcheck', sec(p_ + 'warmcheck', '7–10 MIN', body, notes))
    # ---- Look-back ----
    def optrow(items):
        return ''.join(f'<span style="display:inline-flex;align-items:center;margin-right:34px;white-space:nowrap">{BOX}{E(x)}</span>' for x in items)
    rows = [('The hardest part was ...', optrow(g['hard'] + ['something else'])),
            ('I got unstuck by ...', optrow(['counters or objects', 'drawing it', 'asking someone', 'trying again'])),
            ('Next time I will try ...', f'<span style="display:inline-flex;align-items:center;gap:14px">write or draw one thing &nbsp;&nbsp; It felt: {face(1)} easy {face(2)} OK {face(3)} hard</span>')]
    body = h2('What was hard?') + chip('Look back: 1 minute. There are no right answers.', TEAL, CREAM, 28)
    for a, b in rows:
        body += card(f'<p style="font-size:38px;font-weight:800;color:{TEAL}">{E(a)}</p><p style="font-size:32px;font-weight:600;line-height:1.5">{b}</p>')
    notes = ('Minutes 88 to 90 (1 minute, after the exit ticket). Children tick or write the "What was hard?" box in their workbook. Ask one or two children to share one line; never mark or grade it. '
             'Praise the strategy ("Drawing it got you unstuck"), not the speed. Say: "Tick what was hard, tick what helped you get unstuck, and write one thing you will try next time."')
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
        p1fix.patch(D, p_ + 'warm2', [('</aside>', ' If time is short, take questions 1 to 3 only: the 3-minute Warm-up check follows on the next slide.</aside>')], must=False)
    p1fix.patch(D, p_ + 'title', [('exit ticket 80 to 90.', 'exit ticket 80 to 88, then a one-minute look-back (What was hard?) 88 to 90.'),
                                   ('warm-up 0 to 10,', 'warm-up 0 to 10 (minutes 7 to 10 are the Warm-up check, which decides who starts the worksheet on the Think Harder page),')], must=False)
    if os.path.exists(os.path.join(D, 'slides', 'routine.html')): p1fix.patch(D, 'routine', [('<td>A quick game and quick questions</td>', '<td>A quick game, quick questions and a 3-minute Warm-up check</td>'),
                                ('<td><b>Exit ticket</b></td><td>One question, then a stamp</td>', '<td><b>Exit ticket</b></td><td>One question, then a stamp, then a one-minute look-back: what was hard?</td>'),
                                ('Think Harder and Challenge are for early finishers or home.</td>', 'Think Harder, Challenge and the Open investigation are for early finishers, home, or children on the fast track.</td>')], must=False)
    cleanup(D)
