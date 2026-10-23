#!/usr/bin/env python3
"""Developer preview: python3 preview.py 1 2 3 [--dpi 80] [--bw] -> PNGs of the pupil pages (and verify lines) in the scratchpad."""
import sys, os, subprocess, argparse, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build, render
render.FONT = '/home/user/math-inquirers/fonts/node_modules/@fontsource'
from gen import outcomes
ap = argparse.ArgumentParser(); ap.add_argument("nos", nargs="*", type=int); ap.add_argument("--dpi", type=int, default=80); ap.add_argument("--bw", action="store_true")
ap.add_argument("--out", default="/tmp/claude-0/-home-user-math-inquirers/6d6b173e-8eda-5fdf-9c4d-af677bceddc6/scratchpad/prev"); ap.add_argument("--all", action="store_true")
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
pages = build.all_pages()
sel = [p for p in pages if (not a.nos or p["no"] in a.nos)]
for p in sel:
    bad = [(n, d) for n, o, d in p["verify"] if not o]
    print(f'P4-{p["no"]:02d} {p["title"]}: {len(p["verify"])} checks, {len(bad)} failed', bad[:3])
html = render.doc("".join(render.pupil_page(p, "") for p in sel), "preview")
hp = os.path.join(a.out, "prev.html"); open(hp, "w").write(html)
pdf = os.path.join(a.out, "prev.pdf"); build.to_pdf(hp, pdf)
for f in os.listdir(a.out):
    if f.startswith("pg-") : os.remove(os.path.join(a.out, f))
subprocess.run(["pdftoppm", "-r", str(a.dpi), "-png", pdf, os.path.join(a.out, "pg")], check=True)
if a.bw:
    subprocess.run(["pdftoppm", "-r", str(a.dpi), "-mono", "-png", pdf, os.path.join(a.out, "bw")], check=True)
print(sorted(f for f in os.listdir(a.out) if f.endswith(".png")))
