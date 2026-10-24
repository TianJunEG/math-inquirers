#!/usr/bin/env python3
"""Build the A5 Inquirer Kit strategy toolbox card (double-sided) from levels/spine.json.

    python3 print/make_toolbox_card.py            # all bands, both variants -> outputs/kit/
    python3 print/make_toolbox_card.py --band B   # one band only

Output per band (A = ages 6-8, B = ages 8-10, C = ages 10-13), 2 pages each (page 1 front, page 2 back):
  outputs/kit/Math_Inquirers_Toolbox_Card_<band>_<ages>_PRINT_BW.pdf   1-bit 600 dpi, pure black on white (printer file)
  outputs/kit/Math_Inquirers_Toolbox_Card_<band>_<ages>_SCREEN_colour.pdf  colour vector soft copy

A5 portrait 148 x 210 mm, no bleed, no crop marks. Double-sided: print flipped on the LONG edge (back is the same
way up as the front). Text and icons come only from levels/spine.json and levels/spine_icons/*.svg, so wording
cannot drift from the decks, workbooks and guides. No Mi on the card. Re-running overwrites the same files.
Needs: playwright (chromium), PyMuPDF (fitz), Pillow.
"""
import os, sys, io, html, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'levels'))
import spine_icons as si

OUT = os.path.join(ROOT, 'outputs', 'kit')
AGES = {'A': ('6-8', 'Levels 1 and 2'), 'B': ('8-10', 'Levels 3 and 4'), 'C': ('10-13', 'Levels 5 and 6')}
E = html.escape

CSS = """
@page { size: 148mm 210mm; margin: 0 }
* { box-sizing: border-box; margin: 0; padding: 0 }
:root { --ink:#1B2A49; --paper:#fff; --tint:#FFF3CF; --accent:#FFC93C; }
body.bw { --ink:#000; --tint:#fff; --accent:#fff; }
html, body { background: var(--paper); color: var(--ink); font-family: 'Liberation Sans', Arial, Helvetica, sans-serif; }
.page { width:148mm; height:210mm; padding:9mm 10mm 8mm; page-break-after:always; position:relative; overflow:hidden; display:flex; flex-direction:column; }
.page:last-child { page-break-after:auto }
.top { display:flex; align-items:center; justify-content:space-between; border:0.6mm solid var(--ink); border-radius:3mm; background:var(--accent); padding:2.2mm 4mm; }
.top h1 { font-size:21pt; line-height:1.05; font-weight:800 }
.top .sub { font-size:10.5pt; margin-top:0.8mm }
.age { text-align:center; border:0.6mm solid var(--ink); border-radius:2.5mm; background:var(--paper); padding:1mm 3mm; }
.age b { display:block; font-size:19pt; line-height:1.05 }
.age span { font-size:10.5pt; font-weight:700 }
.rows { flex:1; display:flex; flex-direction:column; justify-content:space-between; margin-top:3mm }
.row { display:flex; align-items:center; gap:3.5mm; border-bottom:0.3mm solid var(--ink); padding:0 0 1.2mm; flex:1; }
.row:last-child { border-bottom:none }
.ic { width:15mm; height:15mm; flex:none; display:flex; align-items:center; justify-content:center; border:0.5mm solid var(--ink); border-radius:50%; background:var(--tint); }
.ic svg { width:11.5mm; height:11.5mm }
.tx { flex:1 }
.nmr { display:flex; align-items:center; justify-content:space-between; gap:2mm }
.nm { font-size:14pt; font-weight:800; line-height:1.1 }
.nm i { font-style:normal; display:inline-block; width:5.6mm; height:5.6mm; line-height:4.8mm; text-align:center; border:0.4mm solid var(--ink); border-radius:50%; font-size:10.5pt; margin-right:1.8mm; vertical-align:1px }
.t1 { flex:none; font-size:10.5pt; font-weight:800; border:0.5mm solid var(--ink); border-radius:2mm; padding:0.2mm 2mm; background:var(--accent); line-height:1.2 }
.df { font-size:12pt; line-height:1.17; margin-top:0.6mm }
.foot { font-size:10.5pt; text-align:center; margin-top:1.6mm; }
/* back */
.intro { font-size:12pt; margin-top:3mm; line-height:1.22 }
.qs { margin-top:3mm; display:flex; flex-direction:column; gap:2.6mm }
.q { display:flex; gap:3mm; align-items:flex-start }
.q .n { flex:none; width:8mm; height:8mm; border-radius:50%; border:0.5mm solid var(--ink); background:var(--accent); font-weight:800; font-size:13pt; text-align:center; line-height:7mm }
.q .t { font-size:QPTpt; font-weight:800; line-height:1.17; padding-top:0.6mm }
.draw { margin-top:2.6mm; border:0.5mm solid var(--ink); border-radius:3mm; height:DRAWHmm; position:relative; }
.draw span { position:absolute; left:4mm; top:1.8mm; font-size:10.5pt }
.stuck { border:0.6mm solid var(--ink); border-radius:3mm; background:var(--tint); padding:2.6mm 4mm 3mm; margin-top:3.6mm }
.stuck .lab { font-size:14pt; font-weight:800 }
.steps { display:flex; flex-direction:column; gap:2.2mm; margin-top:2.4mm }
.step { display:flex; align-items:center; gap:3mm; font-size:14pt; font-weight:800 }
.step i { font-style:normal; flex:none; width:3.2mm; height:3.2mm; border-radius:50%; background:var(--ink) }
.spacer { flex:1 }
.pub { font-size:9pt; text-align:center; margin-top:2mm }
"""

PUBLISHER = 'Math Inquirers. © 2026 Preciouslyours Pte Ltd.'   # matches the school booklets' front-matter wording
STUCK_STEPS = ['Wait.', 'Try a tool.', 'Try a smaller case.', 'Ask.']   # exact words of term/l1 lessons 20 and 30
# The four tools taught in Term 1 (Level 1 term, lesson 10 "Our four tools"); marked on band A only.
TERM1 = {'draw', 'actout', 'pattern', 'list'}


def front(band, bw):
    ages, lv = AGES[band]

    def row(t):
        tag = '<span class="t1">Term 1</span>' if band == 'A' and t['id'] in TERM1 else ''
        return (f'<div class="row"><div class="ic">{si.icon(t["id"], "currentColor", 64)}</div>'
                f'<div class="tx"><div class="nmr"><div class="nm"><i>{t["n"]}</i>{E(t["name"])}</div>{tag}</div>'
                f'<div class="df">{E(t["def"][band])}</div></div></div>')
    rows = ''.join(row(t) for t in si.SPINE['tools'])
    return (f'<section class="page"><div class="top"><div><h1>Toolbox Card</h1><div class="sub">Eight tools for starting a problem</div></div>'
            f'<div class="age"><span>AGES</span><b>{ages}</b></div></div>'
            f'<div class="rows">{rows}</div>'
            f'<div class="foot">Math Inquirers | Inquirer Kit</div></section>')


def back(band, bw):
    lb = si.SPINE['lookback']
    p = lb['prompts'][band]
    a3 = lb['answer3'][band]
    qhtml = ''.join(f'<div class="q"><div class="n">{n}</div><div class="t">{E(p[n-1])}</div></div>' for n in (1, 2, 3))
    cap = {'A': 'Draw or write one word.'}.get(band, 'I checked by ...')
    ages = AGES[band][0]
    steps = ''.join(f'<div class="step"><i></i>{E(w)}</div>' for i, w in enumerate(STUCK_STEPS, 1))
    return (f'<section class="page"><div class="top"><div><h1>Look back</h1><div class="sub">Toolbox Card</div></div>'
            f'<div class="age"><span>AGES</span><b>{ages}</b></div></div>'
            f'<div class="intro">{E(lb["intro"])}</div><div class="qs">{qhtml}</div>'
            f'<div class="draw"><span>{E(cap if band != "A" else cap.capitalize())} Use a pencil.</span></div>'
            f'<div class="stuck"><div class="lab">When I am stuck</div><div class="steps">{steps}</div></div>'
            f'<div class="spacer"></div><div class="pub">{E(PUBLISHER)}</div></section>')


def page_html(band, bw):
    qpt = {'A': 13, 'B': 12.5, 'C': 12}[band]
    drawh = {'A': 48, 'B': 40, 'C': 34}[band]
    css = CSS.replace("QPT", str(qpt)).replace("DRAWH", str(drawh))
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>Toolbox Card {band}</title><style>{css}</style></head>'
            f'<body class="{"bw" if bw else "col"}">{front(band, bw)}{back(band, bw)}</body></html>')


def render(pw, html_text, path):
    b = pw.chromium.launch()
    pg = b.new_page()
    pg.set_content(html_text)
    pg.pdf(path=path, width='148mm', height='210mm', print_background=True, prefer_css_page_size=True)
    b.close()


def to_1bit(src_pdf, dst_pdf, dpi=600, title='Toolbox Card'):
    import fitz
    from PIL import Image
    doc = fitz.open(src_pdf)
    imgs = []
    for pg in doc:
        pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), colorspace=fitz.csGRAY, alpha=False)
        im = Image.frombytes('L', (pm.width, pm.height), pm.samples)
        imgs.append(im.point(lambda v: 0 if v < 140 else 255).convert('1'))
    imgs[0].save(dst_pdf, 'PDF', resolution=dpi, save_all=True, append_images=imgs[1:], title=title, author='Math Inquirers')
    doc.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--band', choices=list(AGES))
    ap.add_argument('--tmp', default=os.path.join(ROOT, 'outputs', 'kit', '.tmp'))
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(a.tmp, exist_ok=True)
    with sync_playwright() as pw:
        for band in ([a.band] if a.band else list(AGES)):
            stem = f'Math_Inquirers_Toolbox_Card_{band}_{AGES[band][0]}'
            render(pw, page_html(band, False), os.path.join(OUT, stem + '_SCREEN_colour.pdf'))
            tmp = os.path.join(a.tmp, stem + '_vec.pdf')
            render(pw, page_html(band, True), tmp)
            to_1bit(tmp, os.path.join(OUT, stem + '_PRINT_BW.pdf'), title=f'Toolbox Card {band} (ages {AGES[band][0]}) print')
            os.remove(tmp)
            print('built', stem)
    try:
        os.rmdir(a.tmp)
    except OSError:
        pass


if __name__ == '__main__':
    main()
