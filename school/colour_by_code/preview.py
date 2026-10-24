"""Debug view of a picture: region ids, the 12 mm-high label box. python3 preview.py rocket [out.html]"""
import sys, os, html
from pictures import PICTURES
from geom import *
def svg(pic):
    s = []
    for r in pic.regions:
        s.append(f'<path d="{path_d(r.geom)}" fill="#fff" stroke="#000" stroke-width="0.9" stroke-linejoin="round" fill-rule="evenodd"/>')
    for svgf, _ in pic.decor: s.append(svgf)
    for r in pic.regions:
        bx = pic.boxes(r.id)
        for (cx, cy, w, h) in bx:
            if h == 12: s.append(f'<rect x="{cx-w/2:.2f}" y="{cy-h/2:.2f}" width="{w:.2f}" height="{h}" fill="none" stroke="#c00" stroke-width="0.3"/><text x="{cx:.1f}" y="{cy:.1f}" font-size="3.5" text-anchor="middle" fill="#c00">{r.id} {w:.0f}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {W+2} {H+2}" width="720" style="border:1px solid #ccc">{"".join(s)}</svg>'
if __name__ == "__main__":
    names = sys.argv[1:] or list(PICTURES)
    out = os.path.join(os.environ.get("PREV", "/tmp"), "prev.html")
    body = "".join(f"<div style='display:inline-block'><h4>{n}</h4>{svg(PICTURES[n]())}</div>" for n in names)
    open(out, "w").write(f"<html><body>{body}</body></html>")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 760 * min(len(names), 2), "height": 860}); pg.goto("file://" + out)
        pg.screenshot(path=out.replace(".html", ".png"), full_page=True); b.close()
    for n in names:
        pic = PICTURES[n](); print(n, len(pic.regions), [ (r.id, next((b[2] for b in pic.boxes(r.id) if b[3]==12), None)) for r in pic.regions])
