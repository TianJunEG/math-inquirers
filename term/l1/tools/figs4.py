"""Diagram upgrade figures (Diagram fixes batch, 23 Oct 2026): picture-symbol icons batch 3, balance, clock_row, measure strip helpers,
combos, bead strings, labelled panels. Nothing here replaces figs2 / figs3 / svg.py: those call into this module for the new names.

Conventions as figs2/figs3: an inline <svg> that scales to its container, flat palette, navy outline, nothing depends on colour alone
(shapes and patterns differ), no bare dots as picture symbols.
"""
import math

import figs2
from figs2 import NAVY, TEAL, YEL, SKY, SOFT, RED, MINT, FONT, SW, _o, _svg, _esc, token_svg, icon, SKIN

GREEN = '#3DBE7A'; BLUE = '#3B6FC9'; ORANGE = '#F28C38'; PINK = '#FF8FB1'; BROWN = '#6B4226'; GREYF = '#C9D2E3'; PURPLE = '#7B4FB5'


# ------------------------------------------------------------------ icons batch 3 (64 x 64 box)

def icon_body(n):
    o = _o
    if n == 'cat':
        return (f'<polygon points="12,26 14,4 28,16" {o(ORANGE)}/><polygon points="52,26 50,4 36,16" {o(ORANGE)}/>'
                f'<ellipse cx="32" cy="36" rx="23" ry="20" {o(ORANGE)}/><circle cx="24" cy="32" r="3.2" fill="{NAVY}"/><circle cx="40" cy="32" r="3.2" fill="{NAVY}"/>'
                f'<polygon points="29,39 35,39 32,43" fill="{NAVY}"/><path d="M32 43 Q27 48 23 45 M32 43 Q37 48 41 45" fill="none" stroke="{NAVY}" stroke-width="2.2" stroke-linecap="round"/>'
                f'<path d="M4 38 L18 40 M4 46 L18 44 M60 38 L46 40 M60 46 L46 44" fill="none" stroke="{NAVY}" stroke-width="2" stroke-linecap="round"/>')
    if n == 'pear':
        return (f'<path d="M32 10 C42 10 42 24 46 32 C54 42 50 58 32 58 C14 58 10 42 18 32 C22 24 22 10 32 10 Z" {o("#B5D86A")}/>'
                f'<path d="M32 10 C32 6 34 3 38 2" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/><path d="M22 44 C22 50 26 53 30 53" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
    if n == 'plum':
        return (f'<circle cx="32" cy="36" r="23" {o("#8E4FB8")}/><path d="M32 14 C28 24 28 44 32 58" fill="none" stroke="{NAVY}" stroke-width="2"/>'
                f'<path d="M32 14 C32 9 34 6 38 4" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/><path d="M36 10 C42 3 52 5 54 8 C50 15 41 15 36 10 Z" {o(GREEN)}/>'
                f'<path d="M18 30 C19 25 23 22 27 22" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>')
    if n == 'fig':
        return (f'<path d="M32 10 C38 10 40 16 42 24 C52 34 52 56 32 58 C12 56 12 34 22 24 C24 16 26 10 32 10 Z" {o("#9C6BB5")}/>'
                f'<path d="M32 12 V58 M24 28 C22 40 24 50 28 56 M40 28 C42 40 40 50 36 56" fill="none" stroke="{NAVY}" stroke-width="1.8" opacity=".55"/><rect x="29" y="4" width="6" height="8" rx="2" {o(GREEN)}/>')
    if n == 'orange':
        return (f'<circle cx="32" cy="34" r="24" {o("#F7A12E")}/><circle cx="32" cy="12" r="2.6" fill="{NAVY}"/><path d="M34 11 C40 4 50 6 52 9 C48 15 40 15 34 11 Z" {o(GREEN)}/>'
                f'<path d="M16 28 C17 23 21 20 25 20" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>'
                + ''.join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="{NAVY}" opacity=".5"/>' for x, y in ((24, 36), (38, 30), (42, 44), (28, 48), (34, 40))))
    if n == 'pawn':       # chess piece
        return (f'<circle cx="32" cy="16" r="11" {o("#fff")}/><path d="M24 26 H40 L44 46 H20 Z" {o("#fff")}/><rect x="14" y="46" width="36" height="8" rx="3" {o(NAVY)}/>'
                f'<line x1="22" y1="26" x2="42" y2="26" stroke="{NAVY}" stroke-width="3"/>')
    if n == 'die':        # ludo die
        pips = ((20, 20), (44, 20), (32, 32), (20, 44), (44, 44))
        return f'<rect x="6" y="6" width="52" height="52" rx="9" {o("#fff")}/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{RED}"/>' for x, y in pips)
    if n == 'card':       # playing card
        return (f'<rect x="12" y="4" width="40" height="56" rx="6" {o("#fff")}/><text x="20" y="24" font-size="16" font-weight="800" fill="{RED}" font-family="{FONT}">A</text>'
                f'<path d="M32 50 C20 42 22 32 28 34 C30 35 32 37 32 38 C32 37 34 35 36 34 C42 32 44 42 32 50 Z" fill="{RED}" stroke="{NAVY}" stroke-width="1.6"/>')
    if n == 'hat':
        return (f'<ellipse cx="32" cy="46" rx="29" ry="9" {o("#3B6FC9")}/><path d="M14 44 C14 14 50 14 50 44 Z" {o("#3B6FC9")}/><rect x="14" y="36" width="36" height="7" {o(YEL)}/>')
    if n == 'stone':
        return (f'<path d="M8 46 C6 32 16 18 30 16 C44 14 58 24 56 40 C56 50 46 54 32 54 C20 54 10 52 8 46 Z" {o("#B8BFCC")}/>'
                f'<path d="M20 30 C24 26 30 25 34 26" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/><circle cx="42" cy="42" r="1.8" fill="{NAVY}" opacity=".5"/><circle cx="26" cy="44" r="1.8" fill="{NAVY}" opacity=".5"/>')
    if n == 'feather':
        return (f'<path d="M12 56 C8 30 26 8 56 6 C54 34 38 52 12 56 Z" {o("#7FC4E8")}/><path d="M10 58 C22 44 34 30 52 10" fill="none" stroke="{NAVY}" stroke-width="2.6" stroke-linecap="round"/>'
                f'<path d="M24 40 L16 36 M32 32 L22 26 M40 24 L32 16 M30 40 L38 44 M38 32 L46 36" fill="none" stroke="{NAVY}" stroke-width="1.8" stroke-linecap="round"/>')
    if n == 'mint':
        return (f'<circle cx="32" cy="32" r="25" {o("#fff")}/>' + ''.join(f'<path d="M32 32 L{32 + 24 * math.cos(math.radians(a)):.1f} {32 + 24 * math.sin(math.radians(a)):.1f} A24 24 0 0 1 {32 + 24 * math.cos(math.radians(a + 30)):.1f} {32 + 24 * math.sin(math.radians(a + 30)):.1f} Z" fill="{RED}"/>' for a in range(0, 360, 60))
                + f'<circle cx="32" cy="32" r="25" fill="none" stroke="{NAVY}" stroke-width="{SW}"/>')
    if n == 'toffee':
        return (f'<polygon points="2,16 18,32 2,48" {o("#C98B3C")}/><polygon points="62,16 46,32 62,48" {o("#C98B3C")}/><rect x="14" y="18" width="36" height="28" rx="6" {o("#E3B15A")}/>'
                f'<path d="M20 26 H44 M20 32 H44 M20 38 H44" stroke="#fff" stroke-width="2" opacity=".8"/>')
    if n == 'gum':        # gumball
        return (f'<circle cx="32" cy="30" r="22" {o("#7ED6C0")}/><path d="M18 24 C20 18 25 14 30 14" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
                f'<rect x="22" y="52" width="20" height="8" rx="3" {o(NAVY)}/>')
    if n == 'rose':
        return (f'<line x1="32" y1="38" x2="32" y2="62" stroke="#2F9E5B" stroke-width="4"/><path d="M32 52 C40 50 46 54 48 58 C40 60 34 58 32 52 Z" {o(GREEN)}/>'
                f'<circle cx="32" cy="24" r="20" {o("#E0455F")}/><path d="M32 24 m-4 0 a4 4 0 1 1 8 0 a8 8 0 1 1 -16 0 a12 12 0 1 1 24 0" fill="none" stroke="{NAVY}" stroke-width="2.4" stroke-linecap="round"/>')
    if n == 'daisy':
        pet = ''.join(f'<ellipse cx="32" cy="12" rx="5.5" ry="11" transform="rotate({a} 32 26)" {o("#fff")}/>' for a in range(0, 360, 40))
        return f'<line x1="32" y1="38" x2="32" y2="62" stroke="#2F9E5B" stroke-width="4"/>{pet}<circle cx="32" cy="26" r="8" {o(YEL)}/>'
    if n == 'tulip':
        return (f'<line x1="32" y1="36" x2="32" y2="62" stroke="#2F9E5B" stroke-width="4"/><path d="M26 54 C18 50 14 42 16 36 C22 40 26 46 28 54 Z" {o(GREEN)}/>'
                f'<path d="M14 10 L22 20 L32 6 L42 20 L50 10 C54 30 46 40 32 40 C18 40 10 30 14 10 Z" {o("#F2A93B")}/>')
    if n == 'bowl':
        return (f'<path d="M4 28 H60 C60 46 48 56 32 56 C16 56 4 46 4 28 Z" {o("#fff")}/><path d="M12 36 H52" stroke="{TEAL}" stroke-width="4"/><ellipse cx="32" cy="28" rx="28" ry="5" {o("#EAF6FB")}/>')
    if n == 'stamp':
        holes = ''.join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff" stroke="{NAVY}" stroke-width="1.4"/>' for x, y in [(8 + 8 * k, 4) for k in range(7)] + [(8 + 8 * k, 60) for k in range(7)] + [(4, 8 + 8 * k) for k in range(7)] + [(60, 8 + 8 * k) for k in range(7)])
        return f'<rect x="4" y="4" width="56" height="56" {o("#FBE9B7")}/>' + holes + f'<rect x="13" y="13" width="38" height="38" {o("#fff")}/><polygon points="32,18 36,28 46,28 38,35 41,45 32,39 23,45 26,35 18,28 28,28" {o(RED)}/>'
    if n == 'duck':
        return (f'<ellipse cx="28" cy="42" rx="24" ry="16" {o(YEL)}/><circle cx="42" cy="22" r="13" {o(YEL)}/><polygon points="52,22 63,26 52,30" {o(ORANGE)}/><circle cx="44" cy="19" r="2.6" fill="{NAVY}"/>'
                f'<path d="M12 42 C18 34 30 34 34 44 C26 48 16 48 12 42 Z" fill="#F2B500" stroke="{NAVY}" stroke-width="2"/>')
    if n == 'goose':
        return (f'<ellipse cx="28" cy="46" rx="24" ry="14" {o("#fff")}/><path d="M42 40 C50 34 40 22 42 14" fill="none" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/><path d="M42 40 C50 34 40 22 42 14" fill="none" stroke="#fff" stroke-width="9.6" stroke-linecap="round"/>'
                f'<circle cx="42" cy="12" r="8" {o("#fff")}/><polygon points="49,10 60,13 49,16" {o(ORANGE)}/><circle cx="43" cy="10" r="2.2" fill="{NAVY}"/>')
    if n == 'hen':
        return (f'<ellipse cx="28" cy="40" rx="23" ry="18" {o("#C98B5A")}/><circle cx="44" cy="20" r="11" {o("#C98B5A")}/><path d="M38 10 L40 4 L44 9 L47 3 L50 10 Z" {o(RED)}/>'
                f'<polygon points="53,20 62,23 53,26" {o(YEL)}/><circle cx="46" cy="18" r="2.4" fill="{NAVY}"/><path d="M12 38 C20 30 32 32 34 42 C26 48 16 46 12 38 Z" fill="#A66B3C" stroke="{NAVY}" stroke-width="2"/><path d="M4 30 L12 38 L4 46" fill="{RED}" stroke="{NAVY}" stroke-width="2" opacity="0"/>')
    if n == 'kite':
        return (f'<polygon points="32,2 54,26 32,50 10,26" {o("#E4572E")}/><path d="M32 2 V50 M10 26 H54" stroke="{NAVY}" stroke-width="2"/><path d="M32 50 C26 54 38 58 30 62" fill="none" stroke="{NAVY}" stroke-width="2.4"/>')
    if n == 'dog':
        return (f'<path d="M10 14 C2 16 2 36 12 38 Z" {o("#8A5A2B")}/><path d="M54 14 C62 16 62 36 52 38 Z" {o("#8A5A2B")}/><ellipse cx="32" cy="34" rx="21" ry="22" {o("#D9A15F")}/>'
                f'<ellipse cx="32" cy="44" rx="11" ry="9" {o("#F3DDB4")}/><ellipse cx="32" cy="40" rx="4.6" ry="3.4" fill="{NAVY}"/><circle cx="23" cy="28" r="3" fill="{NAVY}"/><circle cx="41" cy="28" r="3" fill="{NAVY}"/>'
                f'<path d="M32 43 V48 M26 49 Q32 54 38 49" fill="none" stroke="{NAVY}" stroke-width="2.2" stroke-linecap="round"/>')
    if n == 'kite_blue':
        return (f'<polygon points="32,2 54,26 32,50 10,26" {o("#4D8FE0")}/><path d="M32 2 V50 M10 26 H54" stroke="#fff" stroke-width="2.4"/><circle cx="32" cy="26" r="4" fill="#fff" stroke="{NAVY}" stroke-width="1.6"/><path d="M32 50 C26 54 38 58 30 62" fill="none" stroke="{NAVY}" stroke-width="2.4"/>')
    if n == 'book_sc':
        return (f'<rect x="8" y="6" width="48" height="52" rx="4" {o("#7B4FB5")}/><rect x="14" y="10" width="38" height="44" rx="3" {o("#fff")}/>'
                f'<path d="M28 18 H36 M30 18 V28 L22 42 C20 46 22 48 26 48 H38 C42 48 44 46 42 42 L34 28 V18" fill="#BFE3DC" stroke="{NAVY}" stroke-width="2.2" stroke-linejoin="round"/>')
    if n == 'egg':
        return f'<path d="M32 4 C46 4 54 28 54 38 C54 50 44 60 32 60 C20 60 10 50 10 38 C10 28 18 4 32 4 Z" {o("#FFF6E0")}/><path d="M20 30 C21 24 24 18 28 15" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>'
    if n.startswith('fish_'):
        col, pat = {'fish_red': (RED, 'stripe'), 'fish_blue': ('#4D8FE0', 'spot'), 'fish_gold': ('#F2B500', 'plain')}[n]
        deco = ''
        if pat == 'stripe': deco = f'<path d="M22 18 V46 M30 17 V47 M38 20 V44" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>'
        if pat == 'spot': deco = ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff"/>' for x, y in ((24, 36), (32, 26), (36, 38), (28, 44)))
        return f'<polygon points="46,32 62,18 62,46" {o(col)}/><ellipse cx="28" cy="32" rx="24" ry="16" {o(col)}/>{deco}<circle cx="15" cy="28" r="3.2" fill="{NAVY}"/>'
    if n.startswith('book_'):
        cover = {'book_m': BLUE, 'book_s': '#2F9E5B', 'book_a': ORANGE}[n]
        mark = {'book_m': f'<path d="M32 18 V34 M24 26 H40" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/><path d="M24 42 H40" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>',
                'book_s': f'<path d="M32 38 C20 30 22 20 28 22 C30 23 32 25 32 26 C32 25 34 23 36 22 C42 20 44 30 32 38 Z" fill="{RED}" stroke="{NAVY}" stroke-width="1.6"/>',
                'book_a': f'<circle cx="26" cy="26" r="5" fill="{RED}"/><circle cx="38" cy="26" r="5" fill="{BLUE}"/><circle cx="32" cy="38" r="5" fill="{YEL}"/>'}[n]
        return f'<rect x="8" y="6" width="48" height="52" rx="4" {o(cover)}/><rect x="14" y="10" width="38" height="44" rx="3" {o("#fff")}/>' + mark
    if n == 'crab':
        legs = ''.join(f'<line x1="{x}" y1="40" x2="{x + s * 8}" y2="54" stroke="{NAVY}" stroke-width="2.6" stroke-linecap="round"/>' for x in (22, 28, 36, 42) for s in ((-1 if x < 32 else 1),))
        return (legs + f'<ellipse cx="32" cy="38" rx="20" ry="13" {o("#E4572E")}/><path d="M14 34 C4 30 4 14 14 16 C18 20 16 26 18 30 Z" {o("#E4572E")}/><path d="M50 34 C60 30 60 14 50 16 C46 20 48 26 46 30 Z" {o("#E4572E")}/>'
                f'<circle cx="26" cy="30" r="3" fill="#fff" stroke="{NAVY}" stroke-width="1.6"/><circle cx="38" cy="30" r="3" fill="#fff" stroke="{NAVY}" stroke-width="1.6"/>')
    if n == 'snail':
        return (f'<path d="M4 50 C4 46 10 44 56 44 C60 44 60 50 56 52 L8 52 C5 52 4 51 4 50 Z" {o("#F1D9AE")}/><circle cx="34" cy="30" r="15" {o("#C98B5A")}/><path d="M34 30 m-4 0 a4 4 0 1 1 8 0 a8 8 0 1 1 -16 0" fill="none" stroke="{NAVY}" stroke-width="2.2"/>'
                f'<path d="M54 44 V30 M60 44 V32" stroke="{NAVY}" stroke-width="2.6" stroke-linecap="round"/><circle cx="54" cy="29" r="2.4" fill="{NAVY}"/><circle cx="60" cy="31" r="2.4" fill="{NAVY}"/>')
    if n == 'crayon':
        return (f'<g transform="rotate(-45 32 32)"><rect x="8" y="25" width="38" height="14" {o("#E4572E")}/><polygon points="46,25 58,32 46,39" {o("#E4572E")}/><rect x="14" y="25" width="6" height="14" fill="#fff" opacity=".7"/><rect x="26" y="25" width="6" height="14" fill="#fff" opacity=".7"/></g>')
    if n == 'shirt':
        return f'<path d="M20 8 L4 20 L12 32 L18 28 V56 H46 V28 L52 32 L60 20 L44 8 C40 14 24 14 20 8 Z" {o("#3B6FC9")}/>'
    if n == 'shorts':
        return f'<path d="M10 12 H54 L58 54 H36 L32 34 L28 54 H6 Z" {o("#F28C38")}/><line x1="10" y1="20" x2="54" y2="20" stroke="{NAVY}" stroke-width="2.4"/>'
    if n == 'seat':
        return f'<rect x="14" y="6" width="36" height="30" rx="6" {o("#3B6FC9")}/><rect x="8" y="32" width="48" height="14" rx="5" {o("#5C8DDB")}/><line x1="16" y1="46" x2="16" y2="58" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/><line x1="48" y1="46" x2="48" y2="58" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>'
    if n == 'pocket':
        return f'<path d="M8 10 H56 V40 C56 52 44 58 32 58 C20 58 8 52 8 40 Z" {o("#5C8DDB")}/><path d="M8 18 H56" stroke="{NAVY}" stroke-width="2.4" stroke-dasharray="5 3"/>'
    if n == 'page':
        return f'<path d="M12 4 H42 L54 16 V60 H12 Z" {o("#fff")}/><path d="M42 4 V16 H54" fill="none" stroke="{NAVY}" stroke-width="2.4"/><path d="M20 28 H46 M20 38 H46 M20 48 H38" stroke="{NAVY}" stroke-width="2.4"/>'
    raise ValueError('unknown icon ' + n)


ICONS4 = ['dog', 'kite_blue', 'book_sc', 'cat', 'pear', 'plum', 'fig', 'orange', 'pawn', 'die', 'card', 'hat', 'stone', 'feather', 'mint', 'toffee', 'gum', 'rose', 'daisy', 'tulip', 'bowl', 'stamp', 'duck', 'goose', 'hen',
          'kite', 'egg', 'fish_red', 'fish_blue', 'fish_gold', 'book_m', 'book_s', 'book_a', 'crab', 'snail', 'crayon', 'shirt', 'shorts', 'seat', 'pocket', 'page']


# ------------------------------------------------------------------ jump lines (number line rows with points, empty arc room, route arcs)

def jump_lines(start=0, end=100, step=1, label_every=10, rows=None, room=True, width=1000, label_w=0):
    """One or more number-line rows that share a scale. Each row = {'label': 'Frog A', 'points': [12, {'v': 46, 'box': True}], 'jumps': [[12, 42, '3 tens']], 'hide': []}.
    A point is a yellow tile under the line joined to its tick by a short stem ({'box': True} draws an empty box to fill instead of the number).
    jumps are curved arrows above the line (the label sits on top of the arc). room=True leaves clear space above the line so a child can draw
    her own jumps. Ticks every `step`, a number under every `label_every`; a label that would touch a point tile is left out."""
    rows = rows or [{}]
    if any(r.get('label') for r in rows): label_w = max(label_w, 130)
    pad = 40 + label_w
    x = lambda v: pad + (v - start) / (end - start) * (width - pad - 40)
    n_rows = len(rows)
    P = []
    y = 0
    for ri, row in enumerate(rows):
        jumps = row.get('jumps') or []
        top = 120 if (jumps or room) else 40
        base = y + top
        pts = [({'v': q} if not isinstance(q, dict) else q) for q in row.get('points', [])]
        P.append(f'<line x1="{pad - 14}" y1="{base}" x2="{width - 26}" y2="{base}" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>')
        if row.get('label'):
            P.append(f'<text x="8" y="{base + 12}" font-size="36" font-weight="800" fill="{NAVY}" font-family="{FONT}">{_esc(row["label"])}</text>')
        hide = set(row.get('hide', []))
        v = start
        while v <= end:
            major = (v - start) % label_every == 0
            P.append(f'<line x1="{x(v):.1f}" y1="{base - (18 if major else 9)}" x2="{x(v):.1f}" y2="{base + (18 if major else 9)}" stroke="{NAVY}" stroke-width="{4 if major else 2.2}"/>')
            if major and v not in hide:
                hw = 10 * len(str(v)) + 10
                clash = any(abs(x(v) - x(p['v'])) < hw / 2 + 6 for p in pts)
                if not clash:
                    P.append(f'<text x="{x(v):.1f}" y="{base + 56}" font-size="36" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{v}</text>')
            v += step
        for p in pts:
            xv = x(p['v'])
            P.append(f'<line x1="{xv:.1f}" y1="{base}" x2="{xv:.1f}" y2="{base + 72}" stroke="{NAVY}" stroke-width="3.6"/>')
            P.append(f'<circle cx="{xv:.1f}" cy="{base}" r="9" fill="{RED}" stroke="{NAVY}" stroke-width="2.6"/>')
            if p.get('box'):
                P.append(f'<rect x="{xv - 30:.1f}" y="{base + 72}" width="60" height="56" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3.6"/>')
            else:
                P.append(f'<rect x="{xv - 33:.1f}" y="{base + 72}" width="66" height="56" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="3.2"/>'
                         f'<text x="{xv:.1f}" y="{base + 112}" font-size="38" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{p.get("text", p["v"])}</text>')
        for (a, b, lab) in jumps:
            xa, xb = x(a), x(b); mid = (xa + xb) / 2; hg = min(70, 22 + abs(xb - xa) * 0.25)
            P.append(f'<path d="M{xa:.1f} {base - 16} Q{mid:.1f} {base - 16 - 2 * hg:.1f} {xb:.1f} {base - 40}" fill="none" stroke="{TEAL}" stroke-width="5" stroke-linecap="round"/>')
            P.append(f'<polygon points="{xb:.1f},{base - 14} {xb - 13:.1f},{base - 40} {xb + 13:.1f},{base - 40}" fill="{TEAL}"/>')
            P.append(f'<text x="{mid:.1f}" y="{base - 16 - hg - 12:.1f}" font-size="32" font-weight="800" text-anchor="middle" fill="{TEAL}" stroke="#fff" stroke-width="6" paint-order="stroke" font-family="{FONT}">{_esc(lab)}</text>')
        y = base + (150 if pts else 80)
    return (f'<svg viewBox="0 0 {width} {y}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="number line from {start} to {end}" style="width:100%;height:auto;display:block">{"".join(P)}</svg>')


# ------------------------------------------------------------------ balance

def _bal_items(items, isz):
    """Measure the pieces on one pan: returns (list of (kind, spec, w, h), total width). A piece: {'icon':'button','n':6}, {'text':'5'}, {'blank':True} or a plain number/str."""
    out = []
    for it in items:
        if not isinstance(it, dict): it = {'text': str(it)}
        if it.get('icon'):
            n = it.get('n', 1); cols = it.get('cols') or min(n, 3 if n > 4 else n); rows = -(-n // cols)
            out.append(('icons', it, cols * (isz + 4), rows * (isz + 4)))
        elif it.get('blank'):
            out.append(('blank', it, it.get('w', 150), 90))
        else:
            out.append(('text', it, 78 if len(str(it['text'])) <= 2 else 28 * len(str(it['text'])) + 24, 64))
    return out


def balance(left=None, right=None, tilt='level', width=1000, icon_size=44):
    """A pan balance. left / right = lists of pieces on each pan: {'icon': 'button', 'n': 6} a group of pictures, {'text': '5'} a number tile ('?' is a plain tile),
    {'blank': True} a dashed empty place for the child to draw in. tilt: 'level', 'left' (left pan lower = heavier) or 'right'."""
    cx = width / 2; L = 290
    ang = {'level': 0, 'left': 7, 'right': -7}[tilt]
    ey_off = L * math.sin(math.radians(ang)); ex_off = L * math.cos(math.radians(ang))
    by = 120                                     # beam pivot y
    P = []
    P.append(f'<polygon points="{cx - 70},{by + 250} {cx + 70},{by + 250} {cx},{by + 14}" {_o("#C9D2E3")}/>')
    P.append(f'<line x1="{cx - ex_off:.1f}" y1="{by + ey_off:.1f}" x2="{cx + ex_off:.1f}" y2="{by - ey_off:.1f}" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/>')
    P.append(f'<circle cx="{cx}" cy="{by}" r="16" {_o(YEL)}/>')
    isz = icon_size
    for side, items in ((-1, left or []), (1, right or [])):
        ex = cx + side * ex_off; ey = by + side * (-1) * (-ey_off) if False else (by + ey_off if side < 0 else by - ey_off)
        py = ey + 190                            # pan rim y
        pw = 300
        P.append(f'<path d="M{ex:.1f} {ey:.1f} L{ex - pw / 2:.1f} {py:.1f} M{ex:.1f} {ey:.1f} L{ex + pw / 2:.1f} {py:.1f}" stroke="{NAVY}" stroke-width="3.4" fill="none"/>')
        P.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="8" {_o(YEL)}/>')
        pcs = _bal_items(items, isz)
        plus_after = {id(a[1]): (a[0] == 'text' and b[0] == 'text') for a, b in zip(pcs, pcs[1:])}
        gap = 34
        tw = sum(w for _, _, w, _ in pcs) + gap * max(0, len(pcs) - 1)
        sc = min(1.0, (pw - 30) / tw) if tw else 1.0
        x = ex - tw * sc / 2
        for kind, it, w, h in pcs:
            wc = w * sc; hc = h * sc
            y1 = py - 6 - hc
            if kind == 'icons':
                n = it.get('n', 1); cols = it.get('cols') or min(n, 3 if n > 4 else n)
                for k in range(n):
                    r_, c_ = divmod(k, cols)
                    P.append(icon(it['icon'], x + (c_ + .5) * (isz + 4) * sc, y1 + (r_ + .5) * (isz + 4) * sc, isz * sc))
            elif kind == 'blank':
                P.append(f'<rect x="{x:.1f}" y="{y1:.1f}" width="{wc:.1f}" height="{hc:.1f}" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-dasharray="9 7"/>')
            else:
                t = str(it['text'])
                if t == '?':
                    P.append(f'<rect x="{x:.1f}" y="{y1:.1f}" width="{wc:.1f}" height="{hc:.1f}" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/><text x="{x + wc / 2:.1f}" y="{y1 + hc * 0.72:.1f}" font-size="{44 * sc:.0f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">?</text>')
                else:
                    P.append(f'<rect x="{x:.1f}" y="{y1:.1f}" width="{wc:.1f}" height="{hc:.1f}" rx="12" {_o(YEL)}/><text x="{x + wc / 2:.1f}" y="{y1 + hc * 0.7:.1f}" font-size="{(40 if len(t) <= 2 else 28) * sc:.0f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(t)}</text>')
            x += wc + gap * sc
            if kind == 'text' and plus_after.get(id(it)):
                P.append(f'<text x="{x - gap * sc / 2:.1f}" y="{y1 + hc * 0.68:.1f}" font-size="{40 * sc:.0f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">+</text>')
        P.append(f'<path d="M{ex - pw / 2 - 8:.1f} {py:.1f} H{ex + pw / 2 + 8:.1f} C{ex + pw / 2:.1f} {py + 40:.1f} {ex - pw / 2:.1f} {py + 40:.1f} {ex - pw / 2 - 8:.1f} {py:.1f} Z" {_o("#fff")}/>')
    H = by + 250 + 30
    P.insert(0, f'<rect x="{cx - 110}" y="{by + 246}" width="220" height="16" rx="6" {_o("#C9D2E3")}/>')
    y0 = int(by - abs(ey_off) - 30)               # crop the empty space above the beam
    return f'<svg viewBox="0 {y0} {width} {H + 20 - y0}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="pan balance" style="width:100%;height:auto;display:block">{"".join(P)}</svg>'


def shelf(items=None, title=None, size=64, per_row=6):
    """A shelf: pictures standing on a board, with a name above ('Shelf 1'). items=[{'icon':'cookie','n':3}, ...] in order from the left."""
    flat = []
    for it in items or []: flat += [it['icon']] * it.get('n', 1)
    cols = per_row; rows = -(-len(flat) // cols)
    W = cols * (size + 8) + 40; top = 50 if title else 8
    P = []
    if title: P.append(f'<text x="14" y="38" font-size="36" font-weight="800" fill="{TEAL}" font-family="{FONT}">{_esc(title)}</text>')
    for r in range(rows):
        yb = top + (r + 1) * (size + 12)
        for k, ic in enumerate(flat[r * cols:(r + 1) * cols]):
            P.append(icon(ic, 20 + k * (size + 8) + size / 2 + 4, yb - size / 2, size))
        P.append(f'<rect x="6" y="{yb}" width="{W - 12}" height="14" rx="4" {_o("#C98B5A")}/>')
    return _svg(W, top + rows * (size + 12) + 18, ''.join(P), title or 'shelf')


def combos(tops=4, bottoms=2, top_icon='shirt', bottom_icon='shorts', size=58):
    """Tops and bottoms in one row ('4 tops' with '2 shorts'), so a child can pair every top with every pair of shorts."""
    P = []; x = 10; cy = size / 2 + 8
    for k in range(tops):
        P.append(icon(top_icon, x + size / 2, cy, size)); x += size + 6
    x += 14
    P.append(f'<text x="{x + 20}" y="{cy + 14}" font-size="40" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">+</text>'); x += 54
    for k in range(bottoms):
        P.append(icon(bottom_icon, x + size / 2, cy, size)); x += size + 6
    return _svg(x + 10, size + 16, ''.join(P), f'{tops} tops and {bottoms} pairs of shorts')


def render(v):
    """Dispatch for the new figure types; None if v['type'] is not one of them (called first from figs2.render)."""
    t = v['type']
    if t == 'jump_lines':
        return jump_lines(v.get('start', 0), v.get('end', 100), v.get('step', 1), v.get('label_every', 10), v.get('rows'), v.get('room', True))
    if t == 'combos':
        return combos(v.get('tops', 4), v.get('bottoms', 2), v.get('top_icon', 'shirt'), v.get('bottom_icon', 'shorts'))
    if t == 'shelf':
        return shelf(v.get('items'), v.get('title'), v.get('size', 64), v.get('per_row', 6))
    if t == 'balance':
        return balance(v.get('left'), v.get('right'), v.get('tilt', 'level'))
    return None
