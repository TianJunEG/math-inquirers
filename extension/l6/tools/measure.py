#!/usr/bin/env python3
"""Measure the natural height (mm) of every item of a Level 6 unit as the real page lays it out, and suggest which Start here page each item goes on.
    python3 extension/l6/tools/measure.py 1 [--apply]      (--apply writes the suggested page numbers into extension/data/l6_u01.json)
Capacity and spacing come from the real stylesheet (tools/ext.css) at the print and soft content width (172 mm)."""
import argparse, itertools, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'extension', 'tools'))
import build   # noqa: E402  (must come first: figs.py puts term/l1/tools, which has its own build.py, on the path)
import render   # noqa: E402
from playwright.sync_api import sync_playwright   # noqa: E402

PX = 3.7795


def measure(unit, theme='colour'):
    lv = build.CFG['levels'][str(unit['level'])]
    cfg_vars = f"--fs:{lv['font_px']}px;--line:{lv['line_mm']}mm;--boxw:{lv['box_mm'][0]}mm;--boxh:{lv['box_mm'][1]}mm"
    css = build.font_css() + open(os.path.join(ROOT, 'extension', 'tools', 'ext.css'), encoding='utf-8').read()
    items = unit['items']
    parts = []
    cnt = {}
    for it in items:
        cnt[it['tier']] = cnt.get(it['tier'], 0) + 1
        parts.append(f'<div class="meas" data-id="{it["id"]}">' + render.item_html(it, cnt[it['tier']], theme, hint=it['tier'] != 'quiz') + '</div>')
    banners = ''.join(f'<div class="bn" data-t="{t}">{render.tier_banner(t, "Hints are upside down. Try first!")}</div>' for t in ('start', 'think', 'go', 'quiz'))
    html = (f'<html><head><meta charset="utf-8"><style>{css}</style></head><body class="{theme} print" style="{cfg_vars}">'
            f'<section class="page recto"><div class="pg"><div class="ph"><span class="lv">x</span></div><div class="pbody practice" id="pb"></div></div></section>'
            f'<div style="position:absolute;left:25mm;top:310mm;width:172mm"><div class="pbody practice" style="display:block">{banners}{"".join(parts)}</div></div></body></html>')
    p = os.path.join(os.environ.get('TMPDIR', '/tmp'), f'_meas_l6_{os.getpid()}.html')
    open(p, 'w', encoding='utf-8').write(html)
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page()
        pg.goto('file://' + p); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        cap = pg.evaluate('document.getElementById("pb").clientHeight') / PX
        hs = pg.evaluate('Object.fromEntries(Array.from(document.querySelectorAll(".meas")).map(e=>[e.dataset.id, e.firstElementChild.getBoundingClientRect().height]))')
        bn = pg.evaluate('Object.fromEntries(Array.from(document.querySelectorAll(".bn")).map(e=>[e.dataset.t, e.firstElementChild.getBoundingClientRect().height]))')
        br.close()
    os.unlink(p)
    return cap, {k: v / PX for k, v in hs.items()}, {k: v / PX for k, v in bn.items()}


GAP = 3.0   # .pbody gap, mm


def page_fill(ids, hs, bn_h, cap, extra=0.0):
    return (bn_h + sum(GAP + hs[i] for i in ids) + extra) / cap


def suggest(items, hs, bn_h, cap, lo=0.87, hi=0.985, pages=3):
    ids = [i['id'] for i in items]
    n = len(ids)
    best = None
    # order-preserving cut points first
    for cuts in itertools.combinations(range(1, n), pages - 1):
        segs = [ids[a:b] for a, b in zip((0,) + cuts, cuts + (n,))]
        fills = [page_fill(s, hs, bn_h, cap) for s in segs]
        if all(lo <= f <= hi for f in fills):
            score = max(fills) - min(fills)
            if best is None or score < best[0]:
                best = (score, segs, fills)
    if best:
        return best[1], best[2], 'contiguous'
    # any assignment (items keep their order inside a page)
    for assign in itertools.product(range(pages), repeat=n):
        segs = [[ids[k] for k in range(n) if assign[k] == p] for p in range(pages)]
        if any(not s for s in segs):
            continue
        fills = [page_fill(s, hs, bn_h, cap) for s in segs]
        if all(lo <= f <= hi for f in fills):
            inv = sum(1 for a in range(n) for b in range(a + 1, n) if assign[a] > assign[b])
            score = inv * 10 + (max(fills) - min(fills))
            if best is None or score < best[0]:
                best = (score, segs, fills)
    if best:
        return best[1], best[2], 'reordered'
    return None, None, 'none'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('unit', type=int); ap.add_argument('--apply', action='store_true'); ap.add_argument('--lo', type=float, default=0.87)
    ap.add_argument('--hi', type=float, default=0.985)
    a = ap.parse_args()
    f = os.path.join(ROOT, 'extension', 'data', f'l6_u{a.unit:02d}.json')
    unit = json.load(open(f, encoding='utf-8'))
    cap, hs, bn = measure(unit)
    print(f'page body capacity {cap:.1f} mm; banners ' + ', '.join(f'{k} {v:.1f}' for k, v in bn.items()))
    for it in unit['items']:
        print(f'  {it["id"]:<12s} {hs[it["id"]]:6.1f} mm')
    start = [i for i in unit['items'] if i['tier'] == 'start']
    segs, fills, how = suggest(start, hs, bn['start'], cap, a.lo, a.hi)
    print('Start here suggestion:', how)
    if segs:
        for k, (s, fl) in enumerate(zip(segs, fills), 1):
            print(f'  page {k}: fill {fl:.3f}  ' + ' '.join(i[-3:] for i in s))
    else:
        tot = sum(hs[i['id']] + GAP for i in start) + 3 * bn['start']
        print(f'  no assignment fits; total start height {tot:.0f} mm for 3 pages of {cap:.0f} mm (need {0.87 * 3 * cap:.0f}..{0.985 * 3 * cap:.0f})')
    for tier, label in (('think', 'Think harder'), ('go', 'Go further')):
        its = [i['id'] for i in unit['items'] if i['tier'] == tier]
        print(f'{label}: fill {page_fill(its, hs, bn[tier], cap):.3f}')
    q = [i['id'] for i in unit['items'] if i['tier'] == 'quiz']
    print(f'Check yourself items: {sum(hs[i] + GAP for i in q):.0f} mm (page body {cap:.0f} mm; score box, advice and look-back need about 95 mm)')
    if a.apply and segs:
        for k, s in enumerate(segs, 1):
            for it in unit['items']:
                if it['id'] in s:
                    it['page'] = k
        json.dump(unit, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('pages written')


if __name__ == '__main__':
    main()
