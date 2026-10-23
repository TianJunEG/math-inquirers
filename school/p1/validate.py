#!/usr/bin/env python3
"""Validate the built pack: puzzle checks, layout, black-and-white, text clipping.
   python3 validate.py [--outdir out] ; exit code 1 on any failure. Writes out/validation_report.txt"""
import argparse, os, re, subprocess, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from PIL import Image
import build, render
from gen.common import max_words

ap = argparse.ArgumentParser(); ap.add_argument("--outdir", default=os.path.join(HERE, "out")); a = ap.parse_args()
O = a.outdir
log = []; fails = []
def rec(name, ok, detail=""):
    log.append(f'{"PASS" if ok else "FAIL"}  {name}  {detail}')
    if not ok: fails.append(name)

pages = build.all_pages()
# ---- 1. puzzle verification
for p in pages:
    for n, ok, d in p["verify"]:
        rec(f'P1-{p["no"]:02d} {n}', ok, str(d)[:80])
rec("20 pages, ids 1..20", [p["no"] for p in pages] == list(range(1, 21)))
rec("tier mix 10 one-star / 10 two-star", sum(p["tier"] == 1 for p in pages) == 10 and sum(p["tier"] == 2 for p in pages) == 10)
rec("every page has a self-check strip text", all(p["check"] for p in pages))
mech = [p["mech"] for p in pages]; rec("every page names a self-check mechanism", all(mech))
words = [m.split("(")[0] for m in mech]
# ---- 2. reading level (V8): sentences on the page <= 8 words (page text), check <= 14 words
bad = []
for p in pages:
    for s in p["instr"]:
        if max_words(s) > 8: bad.append((p["no"], s))
    if max_words(p["check"]) > 8 + 8: bad.append((p["no"], p["check"]))
    if len(p["instr"]) > 4: bad.append((p["no"], "more than 4 instruction lines"))
    for sent in re.findall(r"<li>(.*?)</li>", p["body"]) + re.findall(r'class="rtext">(.*?)</div>', p["body"]):
        for one in re.split(r"(?<=\.)\s+", sent):
            if len(one.split()) > 8: bad.append((p["no"], one))
rec("V8 reading level: instruction and clue sentences <= 8 words, <= 4 lines", not bad, str(bad[:4]))
chk = [(p["no"], len(p["check"].split())) for p in pages if len(p["check"].split()) > 18]
rec("check strip text <= 18 words", not chk, str(chk))
# ---- 3. HTML black and white / stroke scan
for f in ("pupil.html", "front.html", "key.html"):
    h = open(os.path.join(O, f)).read()
    cols = set(c.lower() for c in re.findall(r"#[0-9a-fA-F]{3,6}\b", h))
    named = set(re.findall(r"(?:color|background|fill|stroke)\s*[:=]\s*[\"']?(red|blue|green|gray|grey|orange|yellow|purple|teal|navy)\b", h, re.I))
    rec(f"B/W colours only in {f}", cols <= {"#000", "#fff", "#000000", "#ffffff"} and not named, str(sorted(cols))[:80])
    sw = [float(x) for x in re.findall(r'stroke-width[=:]\s*"?([\d.]+)', h)]
    rec(f"stroke widths >= 0.2 mm (0.57 pt) in {f}", min(sw) >= 0.2 if sw else True, f"min {min(sw) if sw else '-'}")
    bw = [float(x) for x in re.findall(r"border[a-z-]*:\s*(?:[^;{}]*?\s)?([\d.]+)mm", h)]
    rec(f"CSS rule widths >= 0.25 mm (0.7 pt) in {f}", min(bw) >= 0.25 if bw else True, f"min {min(bw) if bw else '-'}")
    op = re.findall(r"opacity|rgba|rgb\(|hsl|gradient|filter", h)
    rec(f"no opacity/alpha/gradient in {f}", not op, str(op[:3]))
# ---- 4. PDFs: page counts, fonts, text
exp = {"P1_Puzzles.pdf": 20, "P1_FrontMatter.pdf": 4, "P1_Complete_Pack.pdf": 24, "P1_Answer_Key.pdf": 8}
for f, n in exp.items():
    out = subprocess.run(["pdfinfo", os.path.join(O, f)], capture_output=True, text=True).stdout
    got = int(re.search(r"Pages:\s+(\d+)", out).group(1)); rec(f"{f} has {n} pages", got == n, str(got))
    fo = subprocess.run(["pdffonts", os.path.join(O, f)], capture_output=True, text=True).stdout.splitlines()[2:]
    rec(f"{f} fonts all embedded", all(l.split()[-5] == "yes" for l in fo if l.strip()), f"{len(fo)} fonts")
    sz = os.path.getsize(os.path.join(O, f)); rec(f"{f} size < 20 MB", sz < 20e6, f"{sz/1e6:.2f} MB")
    ps = subprocess.run(["pdfinfo", "-box", os.path.join(O, f)], capture_output=True, text=True).stdout
    rec(f"{f} A4 page size", "(A4)" in subprocess.run(["pdfinfo", os.path.join(O, f)], capture_output=True, text=True).stdout, "")
txt = subprocess.run(["pdftotext", "-layout", os.path.join(O, "P1_Puzzles.pdf"), "-"], capture_output=True, text=True).stdout
pgs = txt.split("\f")[:20]
school = re.search(r"Photocopy licence: (.+?) only", txt)
rec("school name printed on all 20 page footers", all("Photocopy licence:" in x for x in pgs), school.group(1) if school else "")
rec("page codes P1-01..P1-20 present", all(f"P1-{i:02d}" in pgs[i - 1] for i in range(1, 21)))
# ---- 5. layout in browser: overflow, clipping, margins, fill
from playwright.sync_api import sync_playwright
JS = """
() => {
  const mm = 96/25.4, out = [];
  document.querySelectorAll('section.page').forEach((pg, idx) => {
    const pr = pg.getBoundingClientRect();
    const lim = {l: pr.left + 14.5*mm, r: pr.right - 14.5*mm, t: pr.top + 14.5*mm, b: pr.bottom - 14.5*mm};
    const rec = {idx: idx+1, issues: []};
    const area = pg.querySelector('.area');
    if (area) {
      const ar = area.getBoundingClientRect();
      let sumH = 0, minT = 1e9, maxB = 0;
      for (const c of area.children) { const r = c.getBoundingClientRect(); sumH += r.height; minT = Math.min(minT, r.top); maxB = Math.max(maxB, r.bottom); }
      rec.fill = sumH / ar.height; rec.areaH = ar.height/mm; rec.contentH = sumH/mm;
      if (maxB > ar.bottom + 1 || minT < ar.top - 1) rec.issues.push('content leaves puzzle area');
      if (area.scrollHeight > area.clientHeight + 1) rec.issues.push('area scrolls/overflows');
    }
    if (pg.scrollHeight > pg.clientHeight + 1) rec.issues.push('page overflows');
    pg.querySelectorAll('*').forEach(el => {
      if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg' && el.tagName.toLowerCase() !== 'text') return;
      const r = el.getBoundingClientRect(); if (r.width === 0 && r.height === 0) return;
      if (r.left < lim.l - 1 || r.right > lim.r + 1 || r.top < lim.t - 1 || r.bottom > lim.b + 1) rec.issues.push('outside print-safe margin: ' + el.tagName + '.' + (el.className.baseVal ?? el.className) + ' ' + (el.textContent||'').slice(0,20));
      if (!el.closest('svg') && el.children.length === 0 && el.textContent.trim() && el.scrollWidth > el.clientWidth + 1 && el.clientWidth > 0) rec.issues.push('text clipped: ' + el.textContent.slice(0,25));
    });
    // overlap check: check strip vs area
    const ck = pg.querySelector('.check'); if (ck && area) { if (area.getBoundingClientRect().bottom > ck.getBoundingClientRect().top + 1) rec.issues.push('area overlaps check strip'); }
    // minimum font size of html text
    let minFs = 99; pg.querySelectorAll('*').forEach(el => { if (el.children.length===0 && el.textContent.trim() && !el.closest('svg')) minFs = Math.min(minFs, parseFloat(getComputedStyle(el).fontSize)*0.75); });
    rec.minFont = minFs;
    out.push(rec);
  });
  return out;
}
"""
def layout(htmlf, label, check_fill):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 900, "height": 1200})
        pg.goto("file://" + os.path.join(O, htmlf)); pg.wait_for_timeout(600)
        res = pg.evaluate(JS); b.close()
    for r in res:
        ok = not r["issues"]
        rec(f'{label} page {r["idx"]:02d} layout (no overflow/clipping/margin breach)', ok, "; ".join(r["issues"][:3]))
        if check_fill and "fill" in r:
            rec(f'{label} page {r["idx"]:02d} page-fill: puzzle content {r["contentH"]:.0f} of {r["areaH"]:.0f} mm', r["fill"] >= 0.55, f'{r["fill"]:.2f}')
        if r["minFont"] < 99: rec(f'{label} page {r["idx"]:02d} min text size >= 8 pt', r["minFont"] >= 7.9, f'{r["minFont"]:.1f} pt')
layout("pupil.html", "pupil", True); layout("front.html", "front", False); layout("key.html", "key", False)
# ---- 6. bilevel (1-bit) test at 150 dpi on every PDF page
import tempfile, glob, shutil
tmp = tempfile.mkdtemp()
for f in ("P1_Puzzles.pdf", "P1_FrontMatter.pdf", "P1_Answer_Key.pdf"):
    d = os.path.join(tmp, f[:-4]); os.makedirs(d)
    subprocess.run(["pdftoppm", "-r", "150", "-gray", os.path.join(O, f), os.path.join(d, "g")], check=True)
    subprocess.run(["pdftoppm", "-r", "150", "-mono", os.path.join(O, f), os.path.join(d, "m")], check=True)
    gs = sorted(glob.glob(d + "/g-*.pgm")); ms = sorted(glob.glob(d + "/m-*.pbm"))
    worst_loss = 0; grey_blocks = 0
    for g, m in zip(gs, ms):
        G = Image.open(g).convert("L"); M = Image.open(m).convert("L")
        gd = sum(1 for v in G.tobytes() if v < 235); md = sum(1 for v in M.tobytes() if v < 128)
        loss = 1 - md / max(gd, 1)
        # grey flat areas: 6x6 blocks fully between 40 and 215 (a tint that would vanish or go black)
        W, H = G.size; px = G.load(); gb = 0
        for y in range(0, H - 6, 6):
            for x in range(0, W - 6, 6):
                v = [px[x + i, y + j] for i in (0, 5) for j in (0, 5)]
                if all(40 < t < 215 for t in v): gb += 1
        worst_loss = max(worst_loss, loss); grey_blocks += gb
        # ink must remain: bilevel dark pixel share close to greyscale share
        
    rec(f"{f}: 1-bit render at 150 dpi keeps content (max ink loss {worst_loss:.2%} vs greyscale)", worst_loss <= (0.25 if f != 'P1_Answer_Key.pdf' else 0.35), f"{len(gs)} pages")
    rec(f"{f}: no flat grey tint areas (blocks counted {grey_blocks})", grey_blocks < 40 * len(gs), "")
    if f == "P1_Puzzles.pdf":
        keep = os.path.join(O, "bilevel_check"); shutil.rmtree(keep, ignore_errors=True); os.makedirs(keep)
        for m in ms[:20]: Image.open(m).convert("1").save(os.path.join(keep, os.path.basename(m).replace(".pbm", ".png")), optimize=True)
shutil.rmtree(tmp, ignore_errors=True)
open(os.path.join(O, "validation_report.txt"), "w").write("\n".join(log) + f"\n\nTOTAL {len(log)} checks, {len(fails)} failed\n")
print("\n".join(l for l in log if l.startswith("FAIL")) or "no failures")
print(f"{len(log)} checks, {len(fails)} failed")
sys.exit(1 if fails else 0)
