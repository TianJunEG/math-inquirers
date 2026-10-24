#!/usr/bin/env python3
"""Developer check: python3 devcheck.py 1 2 3  -> builds those pupil pages and reports layout issues (overflow, clipping, margins, fill) and failed puzzle checks."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build, render
render.FONT = "/home/user/math-inquirers/fonts/node_modules/@fontsource"
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
nos = [int(a) for a in sys.argv[1:] if a.isdigit()]
pages = [p for p in build.all_pages() if not nos or p["no"] in nos]
for p in pages:
    bad = [(n, d) for n, o, d in p["verify"] if not o]
    if bad: print("CHECK FAIL", p["no"], bad[:3])
tmp = "/tmp/claude-0/-home-user-math-inquirers/6d6b173e-8eda-5fdf-9c4d-af677bceddc6/scratchpad/p6prev/dev.html"
os.makedirs(os.path.dirname(tmp), exist_ok=True)
open(tmp, "w").write(render.doc("".join(render.pupil_page(p, "") for p in pages), "dev"))
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 900, "height": 1200}); pg.goto("file://" + tmp); pg.wait_for_timeout(500)
    res = pg.evaluate(JS); b.close()
for p, r in zip(pages, res):
    print(p["no"], p["title"], "fill %.2f" % r.get("fill", 0), "area %.0f content %.0f mm" % (r.get("areaH", 0), r.get("contentH", 0)), "minFont %.1f" % r["minFont"], r["issues"][:3])
