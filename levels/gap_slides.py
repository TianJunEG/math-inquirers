"""Slide-only skill additions for the HOLIDAY decks at Levels 4-6 (owner decision GAPS-SLIDES-NOW, docs/sasmo/holiday_slide_additions_L4_6.md).
Adds OPTIONAL slides ('Optional, if you finish early': no clock time, no minutes) to split/p4lN, p5lN, p6lN from levels/gap_items.py.
IDEMPOTENT post-pass, called from levels/restyle.py after mi_deco, or run directly (second run changes 0 files):
    python3 levels/gap_slides.py split/p4l3 [...]
Per item: one slide file split/<deck>/project/slides/<deck>-gap-<id>.html (written in the restyled form, tagged data-gap=<hash>;
rewritten only when the item text or this renderer changes), and its id in deck.json order, placed just before the talk/showcase/exit slide.
Nothing here touches workbooks, print files or p4/p5/p6 content/*.js: items live only in levels/gap_items.py.
Stale '-gap-' slides that are no longer in the items are removed. Mi is never placed on these slides (mi_deco only targets title, break, last)."""
import sys, os, re, json, glob, hashlib, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, 'rebuild'))
import slidekit
from slidekit import NAVY, CREAM, TEAL, YEL, WHITE, MUTED, SOFT, SKY, GREY, HF, BF, E, sec, h2, p, card, pin
RENDER_VERSION = 'r7'
PILL = 'Optional, if you finish early'
RED = '#D64545'
BEFORE = ('talk', 'showcase', 'exit', 'reflect', 'end')

# ---------------------------------------------------------------- figures (inline SVG, drawn shapes only)
def _svg(label, w, h, inner):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{inner}</svg>'
def _t(x, y, s, size=30, fill=NAVY, anchor='middle', weight=700):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Nunito Sans, Arial">{E(str(s))}</text>'

def fig_sum(a, b, r, op='+'):
    """vertical letter or digit sum, right-aligned, monospaced"""
    def row(s, pre=''):
        return f'<p style="font-family:\'Courier New\', monospace;font-size:70px;font-weight:700;letter-spacing:14px;text-align:right;line-height:1.15;white-space:pre">{E(pre)}{E(s)}</p>'
    ln = f'<div style="border-top:6px solid {NAVY};width:100%"></div>'
    return (f'<div aria-label="Sum: {E(a)} {op} {E(b)} = {E(r)}" style="display:flex;flex-direction:column;align-items:flex-end;padding:6px 18px">'
            + row(a, '  ') + row(b, op + ' ') + ln + row(r, '  ') + '</div>')

def fig_pie(parts, label):
    import math
    cx, cy, R = 200, 200, 180; ang = -90.0; s = ''
    for frac, col in parts:
        a0 = math.radians(ang); a1 = math.radians(ang + 360 * frac)
        x0, y0, x1, y1 = cx + R * math.cos(a0), cy + R * math.sin(a0), cx + R * math.cos(a1), cy + R * math.sin(a1)
        big = 1 if frac > 0.5 else 0
        s += f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{R} {R} 0 {big} 1 {x1:.1f} {y1:.1f} Z" fill="{col}" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>'
        ang += 360 * frac
    s += f'<circle cx="{cx}" cy="{cy}" r="10" fill="{NAVY}"/>'
    return _svg(label, 400, 400, s).replace('width:400px;height:400px', 'width:330px;height:330px')

def fig_fan(npts):
    """apex above a base with npts marked points (a fan of lines)"""
    W, H = 560, 330; ax, ay = 280, 30; y = 290; xs = [60 + i * (440 / (npts - 1)) for i in range(npts)]
    s = f'<line x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
    for x in xs: s += f'<line x1="{ax}" y1="{ay}" x2="{x:.1f}" y2="{y}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/><circle cx="{x:.1f}" cy="{y}" r="9" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'
    s += f'<circle cx="{ax}" cy="{ay}" r="9" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'
    return _svg(f'A point at the top joined to {npts} points along a base line', W, H, s)

def fig_tri12():
    """triangle with two lines from the apex to the base and one line across (parallel to the base)"""
    W, H = 560, 380; A = (280, 30); B = (40, 340); C = (520, 340)
    def on(P, Q, t): return (P[0] + (Q[0] - P[0]) * t, P[1] + (Q[1] - P[1]) * t)
    D = on(B, C, 1 / 3); Ee = on(B, C, 2 / 3); Fp = on(A, B, 0.55); Gp = on(A, C, 0.55)
    s = f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/>'
    for P in (D, Ee): s += f'<line x1="{A[0]}" y1="{A[1]}" x2="{P[0]:.1f}" y2="{P[1]:.1f}" stroke="{NAVY}" stroke-width="6"/>'
    s += f'<line x1="{Fp[0]:.1f}" y1="{Fp[1]:.1f}" x2="{Gp[0]:.1f}" y2="{Gp[1]:.1f}" stroke="{NAVY}" stroke-width="6"/>'
    return _svg('A big triangle with two lines from the top corner to the base and one line across, parallel to the base', W, H, s)

def fig_grid(cols, rows, label):
    cs = 92; W, H = cols * cs + 12, rows * cs + 12
    s = f'<rect x="6" y="6" width="{cols*cs}" height="{rows*cs}" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/>'
    for c in range(1, cols): s += f'<line x1="{6+c*cs}" y1="6" x2="{6+c*cs}" y2="{6+rows*cs}" stroke="{NAVY}" stroke-width="4"/>'
    for r in range(1, rows): s += f'<line x1="6" y1="{6+r*cs}" x2="{6+cols*cs}" y2="{6+r*cs}" stroke="{NAVY}" stroke-width="4"/>'
    return _svg(label, W, H, s)

def fig_stairs(steps, label):
    st = 70; W, H = steps * st + 70, steps * st + 70; x0, y0 = 30, 30
    pts = [(x0, y0 + steps * st)]
    for i in range(steps):
        pts.append((x0 + i * st, y0 + (steps - i - 1) * st)); pts.append((x0 + (i + 1) * st, y0 + (steps - i - 1) * st))
    pts.append((x0 + steps * st, y0 + steps * st))
    s = f'<polygon points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="{SKY}" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/>'
    return _svg(label, W + 20, H, s)

def fig_quarter(label):
    s = f'<rect x="50" y="20" width="340" height="340" fill="{SKY}" stroke="{NAVY}" stroke-width="6"/>'
    s += f'<path d="M50 360 L50 20 A340 340 0 0 1 390 360 Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/>'
    s += _t(220, 400, '10 cm', 28)
    return _svg(label, 420, 420, s)

def fig_dice(label):
    def die(x, y, show):
        r = f'<rect x="{x}" y="{y}" width="130" height="130" rx="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/>'
        if show: r += ''.join(f'<circle cx="{x+a}" cy="{y+b}" r="10" fill="{NAVY}"/>' for a, b in [(35, 35), (95, 35), (35, 95), (95, 95)])
        else: r += _t(x + 65, y + 82, '?', 60, MUTED)
        return r
    s = die(40, 270, False) + die(40, 140, False) + die(40, 10, True)
    s += f'<rect x="10" y="404" width="190" height="10" fill="{NAVY}"/>' + _t(200, 90, 'top die: 4 on top', 28, TEAL, 'start') + _t(220, 440, 'table', 28, TEAL, 'start')
    return _svg(label, 440, 450, s)

def fig_bars(rows, label, unit=70):
    """rows: [(name, [(units, fill, text)])]"""
    H = 24 + len(rows) * 84; W = 40 + max(sum(u for u, _, _ in r[1]) for r in rows) * unit + 190
    s = ''
    for i, (nm, segs) in enumerate(rows):
        y = 14 + i * 84; x = 170
        s += _t(150, y + 46, nm, 30, NAVY, 'end')
        for u, fillc, tx in segs:
            for k in range(u): s += f'<rect x="{x+k*unit}" y="{y}" width="{unit}" height="64" fill="{fillc}" stroke="{NAVY}" stroke-width="4"/>'
            if tx: s += _t(x + u * unit / 2, y + 43, tx, 28)
            x += u * unit
    return _svg(label, W, H, s)

def fig_table(head, rows, label, colw=None):
    colw = colw or [190] * len(head)
    def row(cells, bg, wt):
        return '<div style="display:flex;background:%s;border:3px solid %s;border-radius:10px;margin-top:6px">%s</div>' % (bg, NAVY, ''.join(f'<div style="width:{w}px;padding:5px 6px;font-size:28px;font-weight:{wt};text-align:center">{E(str(c))}</div>' for c, w in zip(cells, colw)))
    return f'<div aria-label="{E(label)}">' + row(head, YEL, 800) + ''.join(row(r, WHITE, 600) for r in rows) + '</div>'

FIGS = {'sum': fig_sum, 'pie': fig_pie, 'fan': fig_fan, 'tri12': fig_tri12, 'grid': fig_grid, 'stairs': fig_stairs, 'quarter': fig_quarter,
        'dice': fig_dice, 'bars': fig_bars, 'table': fig_table}

# ---------------------------------------------------------------- slide
def M(t):
    """typographic signs for display: digit x digit -> times, digit - digit -> minus, digit / digit with spaces -> divide"""
    t = re.sub(r'(?<=[\d)]) x (?=[\d(])', ' \u00d7 ', t)
    t = re.sub(r'(?<=[\d)]) - (?=[\d(])', ' \u2212 ', t)
    return re.sub(r'(?<=[\d)]) / (?=[\d(])', ' \u00f7 ', t)
def render(it, deckkey, lv):
    it = dict(it); it['q'] = [M(x) for x in it['q']]; it['ans'] = [M(x) for x in it['ans']]
    for k in ('say', 'ask', 'listen', 'why'): it[k] = M(it[k])
    if it.get('var'): it['var'] = (M(it['var'][0]), M(it['var'][1]))
    slidekit.FOOT = f'Math Inquirers P{lv} Holiday Program  •  Notice it. Test it. Explain why.'
    ql = sum(len(x) for x in it['q'])
    size = 34 if ql < 330 else 31 if ql < 460 else 28
    qs = ''
    for line in it['q']:
        m = re.match(r'^(\([a-z]\)|[0-9]\.)\s+(.*)$', line, re.S)
        if m: qs += p(f'<span style="color:{TEAL};font-weight:800">{E(m.group(1))}</span>  {E(m.group(2))}', size, 600, raw=True)
        else: qs += p(line, size, 600)
    fig = ''
    if it.get('fig'):
        f = it['fig']; fn = FIGS[f[0]]; html_fig = fn(*f[1:])
        fig = f'<div style="flex:none;background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;align-items:center;justify-content:center">{html_fig}</div>'
    qcard = f'<div style="flex:1;min-width:0;background:{WHITE};border-radius:24px;padding:24px 40px;display:flex;flex-direction:column;gap:10px">{qs}</div>'
    row = f'<div style="display:flex;gap:28px;align-items:stretch">{qcard}{fig}</div>'
    tool = f'<p style="align-self:flex-start;background:{SOFT};border:3px solid {YEL};border-radius:30px;padding:6px 22px;font-size:26px;font-weight:800;color:{NAVY}">Tool: {E(it["tool"])}</p>'
    pre = ''
    if it.get('preview'):
        pre = f'<p style="align-self:flex-start;background:{NAVY};color:{CREAM};border-radius:30px;padding:6px 22px;font-size:26px;font-weight:800">PREVIEW: a Primary 6 topic, beyond Level 5. A taste, not a test.</p>'
    ans = '<div data-build-in="pop" style="background:%s;border-radius:20px;padding:16px 28px;display:flex;flex-direction:column;gap:6px">%s</div>' % (YEL, ''.join(f'<p style="font-size:{30 if size>=31 else 28}px;font-weight:800;line-height:1.25">{E(a)}</p>' for a in it['ans']))
    title = f"{it['kind']}: {it['skill']}"
    body = h2(title, 60) + f'<div style="display:flex;gap:16px;flex-wrap:wrap">{tool}{pre}</div>' + row + ans
    var = it.get('var')
    notes = (f'{PILL} (no clock time): show it while some pairs are working or have finished, or use it live as an extra warm-up or tutor-bank question; never at a fixed minute, and it never takes time from the plan. '
             f'ADDED ITEM {it["id"]} (a slide-only addition for the skill gap "{it["skill"]}"; it is not in the printed workbook). TOOL: {it["tool"]}. '
             + ('PREVIEW LABEL: say "This is a first taste of a topic from a later level. We are not testing it; we are noticing how it works." ' if it.get('preview') else '')
             + f'SAY: {it["say"]} ASK: {it["ask"]} LISTEN FOR: {it["listen"]} '
             f'Everyone writes the answer on their own paper, then say the answer together on three, then click the answer box. Nobody holds anything up, nobody is marked, and passing is always fine. '
             f'ANSWER: {" ".join(it["ans"])} WHY: {it["why"]} '
             + (f'SAME SKILL, NEW NUMBERS (tutor bank, say it aloud or write it on the board): {var[0]} Answer: {var[1]} ' if var else ''))
    s = sec(f'{deckkey}-gap-{it["id"]}', PILL, body, notes)
    return s.replace('data-transition="fade"', 'data-transition="fade" data-gap="@HASH@"', 1)

def item_hash(it):
    return hashlib.sha1((RENDER_VERSION + json.dumps(it, sort_keys=True, ensure_ascii=False)).encode()).hexdigest()[:10]

def _load_fix():
    m = sys.modules.get('__main__')
    if m is not None and hasattr(m, 'fix') and hasattr(m, 'level_of'): return m.fix
    src = open(os.path.join(HERE, 'restyle.py'), encoding='utf-8').read()
    src = src.split('for d in sys.argv[1:]:')[0]
    ns = {'__name__': 'restyle_fix'}; exec(compile(src, 'restyle_prefix', 'exec'), ns)
    return ns['fix']

def key_level(d):
    k = os.path.basename(d.rstrip('/')); m = re.match(r'p(\d)l(\d+)$', k)
    return (k, int(m.group(1)), int(m.group(2))) if m else (k, None, 0)

def apply(d, fix=None):
    import gap_items
    k, lv, ln = key_level(d)
    if lv not in (4, 5, 6): return 0
    fix = fix or _load_fix()
    items = [it for it in gap_items.ITEMS if it['lv'] == lv and it['ln'] == ln]
    base = os.path.join(d, 'project'); sl = os.path.join(base, 'slides'); dj = os.path.join(base, 'deck.json')
    n = 0; ids = []
    for it in items:
        sid = f'{k}-gap-{it["id"]}'; ids.append(sid); path = os.path.join(sl, sid + '.html'); h = item_hash(it)
        cur = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        if f'data-gap="{h}"' in cur: continue
        raw = render(it, k, lv).replace('@HASH@', h)
        open(path, 'w', encoding='utf-8').write(fix(raw, str(lv))); n += 1
    for f in glob.glob(os.path.join(sl, f'{k}-gap-*.html')):
        sid = os.path.basename(f)[:-5]
        if sid not in ids: os.remove(f); n += 1
    deck = json.load(open(dj, encoding='utf-8')); order = [x for x in deck['order'] if '-gap-' not in x]
    if ids:
        pos = next((i for i, x in enumerate(order) if x.split('-')[-1] in BEFORE), len(order))
        order = order[:pos] + ids + order[pos:]
    if order != deck['order']:
        deck['order'] = order; json.dump(deck, open(dj, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); n += 1
    return n

if __name__ == '__main__':
    for d in sys.argv[1:]: print(d, apply(d))
