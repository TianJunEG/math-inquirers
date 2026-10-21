"""Math Inquirers P6, Lesson 8: Secret Codes. Writes split/p6l8/project (deck.json + slides/*.html).
Text that the tutor guide also reads (today, warm-up, explore, key idea, talk, exit, question bank) comes from p6/content/l8.js.
Code strips and clocks are computed (letter number + shift, mod 26), so every picture is exact."""
import json, os, sys, math, re, subprocess, datetime
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import slidekit
from slidekit import *
slidekit.FOOT = 'Math Inquirers P6  •  Notice it. Test it. Explain why.'
ROOT = os.path.join(H, '..')
D = os.path.join(ROOT, 'split', 'p6l8', 'project'); os.makedirs(os.path.join(D, 'slides'), exist_ok=True)
C = json.loads(subprocess.check_output(['node', '-e', "const c=require(process.argv[1]);console.log(JSON.stringify({lesson:c.lesson,script:c.script,deck:c.deck,qbank:c.qbank}))", os.path.join(ROOT, 'p6', 'content', 'l8.js')]))
L, SC, DK, QB = C['lesson'], C['script'], C['deck'], C['qbank']
S = {}
def put(i, h): S[i] = h
RED = '#D64545'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ---------- SVG helpers ----------
def SV(w, h, body, label, extra=''): return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;{extra}">{body}</svg>'
def T(x, y, s, size=32, fill=NAVY, weight=700, anchor='middle'): return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Fredoka, Arial">{E(str(s))}</text>'

# code blocks: our own simple coloured shapes. prog items: (kind, text) or (kind, text, [children]); {..} = white slot
BC = {'event': (YEL, NAVY), 'ctrl': (WHITE, NAVY), 'motion': (SKY, NAVY), 'pen': (TEAL, WHITE), 'var': (RED, WHITE), 'looks': (YEL, NAVY)}
def cwid(s, fs): return sum(fs * (0.36 if c in "iltfjr .,:()'|" else 0.78 if (c.isupper() or c in 'mw%×') else 0.62) for c in s)
def segs(t): return [(x[1:-1], True) if x.startswith('{') else (x.strip(), False) for x in re.split(r'(\{[^}]*\})', t) if x.strip()]
def blocks(prog, fs=28, h=52):
    pad, arm, gap, sp = 14, 28, 9, 12
    def lw(t): return sum(cwid(g, fs) + (2 * sp if sl else 0) + gap for g, sl in segs(t)) - gap + 2 * pad
    def txt(x, y, t, fg):
        s = ''; cx = x + pad; ty = y + h / 2 + fs * 0.36
        for g, sl in segs(t):
            w = cwid(g, fs)
            if sl:
                s += f'<rect x="{cx:.1f}" y="{y+7}" width="{w+2*sp:.1f}" height="{h-14}" rx="{(h-14)/2}" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>'
                s += f'<text x="{cx+sp+w/2:.1f}" y="{ty:.1f}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Arial">{E(g)}</text>'; cx += w + 2 * sp + gap
            else:
                s += f'<text x="{cx:.1f}" y="{ty:.1f}" font-size="{fs}" font-weight="700" fill="{fg}" font-family="Arial">{E(g)}</text>'; cx += w + gap
        return s
    mx = [0]
    def draw(items, x, y):
        s = ''
        for it in items:
            kind, t = it[0], it[1]; bg, fg = BC[kind]
            if len(it) > 2:
                w = max(lw(t), 180); inner, y2 = draw(it[2], x + arm, y + h + 3)
                yb = max(y2, y + h + 24); wb = max(w * 0.45, 120)
                s += f'<path d="M{x} {y} H{x+w:.1f} V{y+h} H{x+arm} V{yb} H{x+wb:.1f} V{yb+22} H{x} Z" fill="{bg}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>' + txt(x, y, t, fg) + inner
                mx[0] = max(mx[0], x + w); y = yb + 25
            else:
                w = lw(t)
                s += f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="{22 if kind=="event" else 10}" fill="{bg}" stroke="{NAVY}" stroke-width="3"/>' + txt(x, y, t, fg)
                mx[0] = max(mx[0], x + w); y += h + 3
        return s, y
    body, y = draw(prog, 3, 3)
    return body, math.ceil(mx[0] + 6), math.ceil(y + 3)
def blocks_svg(prog, label, fs=28, h=52):
    b, w, hh = blocks(prog, fs, h); return SV(w, hh, b, label)

def ostep(left, top, n, text, ov=None, ovw=0, ovh=0, dx=0, dy=0, tw=1000, size=34, build='fade'):
    """One click = overlay marks (same left/top as the base picture) + the step text box beside it."""
    lab = f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    box = f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;flex:none"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{E(text)}</p></div>'
    if ov is None: return pin(left + dx, top, tw, box, build)
    o = f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov}</div>'
    return pin(left, top, dx + tw, f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>', build)
def soft(left, top, width, text, size=34, build='fade'): return pin(left, top, width - 56, p(text, size, 700), build, SOFT, 20, '18px 28px')
def stitle(t, size=34): return p(t, size, 600, MUTED)
def num(a, b): return f'<span style="color:{TEAL}">{E(a)}</span>  {E(b)}'
def check2(sid, time, title, rows, notes, lw=230, size=34, gap=24, top=250):
    """check-together slide: label + answer box (click), heights from the number of lines"""
    body = h2(title); y = top
    for a, b, nl in rows:
        hgt = int(nl * size * 1.25 + 36)
        body += pin(128, y, lw - 20, f'<p style="font-size:34px;font-weight:800;color:{TEAL}">{E(a)}</p>', None, WHITE, 20, '18px 24px')
        body += pin(128 + lw, y, 1664 - lw - 52, f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>', 'pop', YEL, 20, '18px 26px')
        y += hgt + gap
    assert y <= 940, (sid, y)
    return sec(sid, time, body, notes)
def qa_slide(sid, time, title, sub, rows, notes, size=36, step=150, top=330, qw=1250):
    body = h2(title) + (stitle(sub) if sub else '')
    for i, (a, b, c) in enumerate(rows):
        body += qrow(128, top + i * step, qw, a, b, size) + answer(128 + qw + 42, top + i * step, 1664 - qw - 42, c)
    return sec(sid, time, body, notes)
def dark(sid, bg, inner, notes, foot='#B7C3DD'):
    return (f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'{inner}\n<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:{foot}">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')

