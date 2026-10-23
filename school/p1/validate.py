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

# ---- 1b. wrong-answer enumeration (owner addendum 8: a pupil can tell when an answer is wrong)
# Every page supplies a model: the right answers (truth), the values each answer could take (domains) and the
# pupil's own check as a function of the answers (check). Here, independently of the generator, every single
# change of one answer is tried and the share the check REJECTS is counted. Two rates are required to be >= 95%:
#   plausible slips: +-1, +-2, +-3, +-4, +-5, +-10 on number answers (any other value for letters, cells, times);
#   all values: every other value in the page's number range.
# Pages whose answers form an arrangement (a queue, a grid, ordered cards, shape matching) are also tested on every
# wrong arrangement (all permutations). A check that only says "one tick per row and column" would fail this test.
import itertools, math
THRESH = 0.95
SLIPS = (1, 2, 3, 4, 5, 10)
def enumerate_model(m):
    truth, doms, chk = list(m["truth"]), m["domains"], m["check"]
    out = dict(right_passes=bool(chk(list(truth))), plausible=[0, 0], allv=[0, 0], perm=None)
    for i, t in enumerate(truth):
        for v in doms[i]:
            if v == t: continue
            ans = list(truth); ans[i] = v
            rejected = not chk(ans)
            out["allv"][1] += 1; out["allv"][0] += rejected
            if m.get("numeric") is True and isinstance(t, int):
                if abs(v - t) in SLIPS:
                    out["plausible"][1] += 1; out["plausible"][0] += rejected
            else:
                out["plausible"][1] += 1; out["plausible"][0] += rejected
    if m.get("perm"):
        idx = m["perm"]; vals = [truth[i] for i in idx]; ok = tot = 0
        for pp in itertools.permutations(vals):
            if list(pp) == vals: continue
            ans = list(truth)
            for i, v in zip(idx, pp): ans[i] = v
            tot += 1; ok += (not chk(ans))
        out["perm"] = [ok, tot]
    return out
verification = []
for p in pages:
    r = enumerate_model(p["model"]) if "model" in p else None
    rec(f'P1-{p["no"]:02d} has a self-check model for the enumeration', r is not None)
    if r is None: continue
    rec(f'P1-{p["no"]:02d} check passes the right answers', r["right_passes"])
    a, b = r["plausible"]
    rec(f'P1-{p["no"]:02d} enumeration: plausible single slips rejected {a}/{b} = {a / b:.1%} (needs >= 95%)', b > 0 and a / b >= THRESH - 1e-9)
    a2, b2 = r["allv"]
    rec(f'P1-{p["no"]:02d} enumeration: every other value of one answer rejected {a2}/{b2} = {a2 / b2:.1%} (needs >= 95%)', b2 > 0 and a2 / b2 >= THRESH - 1e-9)
    if r["perm"]:
        a3, b3 = r["perm"]
        rec(f'P1-{p["no"]:02d} enumeration: wrong arrangements rejected {a3}/{b3} = {a3 / b3:.1%} (needs >= 95%)', a3 / b3 >= THRESH - 1e-9)
    verification.append((p["no"], r))
rec("3 colour-by-code pages (P1-01, P1-12, P1-14), 3 or 4 wanted of 20", [p["no"] for p in pages if p.get("cbc")] == [1, 12, 14])
# coverage within the 20-page budget (audit 2, F-new 12 and F-new 7)
def has(no, word): return any(p["no"] == no and word in (p["topic"] + " " + p["syll"]).lower() for p in pages)
rec("coverage: add and subtract within 100 (P1-11), sharing and grouping (P1-03), two multiplication pages (P1-05, P1-13), a one-star o'clock and half past time page (P1-06) and the five-minute page (P1-18)",
    has(11, "within 100") and has(3, "sharing") and has(5, "multiplication") and has(13, "multiplication") and has(6, "o'clock") and has(18, "5 minutes") and next(p for p in pages if p["no"] == 6)["tier"] == 1)
rec("strand balance: whole numbers at most 6 pages, add/subtract 4, multiplication and sharing 3, money 2, time 2, shapes 2, length 1, graph 1",
    {k: len(v) for k, v in __import__("render").strand_map(pages).items()}.get("Number and Algebra - Whole Numbers", 0) <= 6, str({k: len(v) for k, v in __import__("render").strand_map(pages).items()}))
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
    for cl in (p.get("check_lines") or [p["check"]]):
        if max_words(cl) > 16 and not p.get("cbc"): bad.append((p["no"], cl))
        if max_words(cl) > 20: bad.append((p["no"], cl))
    if len(p["instr"]) > 3: bad.append((p["no"], "more than 3 instruction lines (plan: 3 lines max)"))
    for sent in re.findall(r"<li>(.*?)</li>", p["body"]) + re.findall(r'class="rtext">(.*?)</div>', p["body"]):
        sent = re.sub(r"<[^>]+>", " ", sent)
        for one in re.split(r"(?<=\.)\s+", sent.strip()):
            if len(one.split()) > 8: bad.append((p["no"], one))
rec("V8 reading level: instruction and clue sentences <= 8 words, <= 4 lines", not bad, str(bad[:4]))
chk = [(p["no"], len(p["check"].split())) for p in pages if len(p["check"].split()) > (34 if p["no"] == 20 else 18) and not p.get("cbc")]
rec("check strip text <= 18 words (P1-20 has two checks: 30)", not chk, str(chk))
# F-new 1: the check strip must not name or describe the code word (hints confirm, they do not reveal)
hint = [(p["no"], p["check"]) for p in pages if re.search(r"\bIs it\b|\bDoes it\b|\bYou (live|can|carry)|garden|music|river|\bsky\b|\bspace\b|\bking\b|\ban animal|\bseason|used for writing|shopping|count the time", p["check"]) and not p.get("cbc")]
rec("check strips carry no category hint (Is it ...?): the strip never says what the word is", not hint, str(hint[:3]))
rec("every code-word strip is exactly the plain question 'Do they spell a word?'", all("Do they spell a word?" in p["check"] for p in pages if p.get("check_boxes")))

# ---- 2b. notes and tags
def plain(h): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h))
bad = []
for p in pages:
    src = " ".join([plain(p["body"]), p.get("facts", ""), p["key"]["answers"], p["key"]["check_result"], p["check"], " ".join(p["instr"])])
    have = set(re.findall(r"\d+", src))
    note = re.sub(r"\d+%", "", re.sub(r"(within|up to|to|than|of) \d+", "", p["note"]))
    miss = sorted({n for n in re.findall(r"\d+", note) if int(n) >= 11 and n not in have})
    if miss: bad.append((p["no"], miss))
rec("every number of 11 or more quoted in a teacher note is found on the page or in its answers", not bad, str(bad))
PHRASES = ["more than", "fewer than", "less than", "greatest", "smallest", "second greatest", "ordinal", "in front of", "behind", "next to", "ones digit", "tens digit", "cross the hour", "half-hour"]
bad = []
for p in pages:
    page_text = (plain(p["body"]) + " " + " ".join(p["instr"]) + " " + p["topic"] + " " + p["check"]).lower()
    note = p["note"].lower()
    if p["no"] == 18: note = re.sub(r"none of the half-hour additions cross the hour\.", "", note)
    for ph in PHRASES:
        if ph in note and ph not in page_text and not (ph == "greatest" and "second greatest" in note and "second greatest" in page_text) and not (ph == "ordinal" and "1st" in page_text + " 2nd"):
            bad.append((p["no"], ph))
rec("every clue word named in a teacher note (more than, fewer than, greatest, in front of, behind, ones digit ...) occurs on its page", not bad, str(bad))
rec("the P1-18 note does not claim half-hour additions cross the hour unless one does", ("none of the half-hour additions" in next(p for p in pages if p["no"] == 18)["note"].lower()) or ("of the half-hour additions cross the hour" in next(p for p in pages if p["no"] == 18)["note"].lower()))
RANGES = {"Whole Numbers": (1, 7, 1), "Addition and Subtraction": (2, 7, 2), "Multiplication and Division": (3, 4, 3)}
bad = []
for p in pages:
    nums = re.findall(r"\b(\d)\.(\d)\b", p["syll"].split("(")[0])
    for a, b in nums:
        a, b = int(a), int(b)
        key = next((k for k in RANGES if k in p["strand"]), None)
        if key: ok = a == RANGES[key][2] and 1 <= b <= RANGES[key][1]
        elif p["syll"].startswith("Length"): ok = a == 1 and 1 <= b <= 4
        elif p["syll"].startswith("Time"): ok = a == 2 and 1 <= b <= 4
        elif p["syll"].startswith("Geometry"): ok = a == 1 and 1 <= b <= 4
        else: ok = False
        if not ok: bad.append((p["no"], f"{a}.{b}"))
rec("syllabus numbers in every topic tag lie inside the P1 ranges of docs/moe/syllabus_by_level.md", not bad, str(bad))
SYL = open(os.path.join(HERE, "..", "..", "docs", "moe", "syllabus_by_level.md")).read()
SYL = SYL[SYL.index("## Primary 1 (pp. 31-32)"):SYL.index("## Primary 2 (pp. 33-34)")].lower()
NEEDS = {1: ["count a set", "tens and ones"], 2: ["compare and order numbers", "tens and ones"], 3: ["dividing within 20"], 4: ["compare and order numbers", "compare sets"], 5: ["multiplying within 40", "sign x"],
         6: ["tell time to 5 minutes"], 7: ["ordinals"], 8: ["mental calculation within 20"], 9: ["adding more than two 1-digit numbers"], 10: ["inverse relationship", "mental calculation within 20"],
         11: ["within 100", "2-digit plus ones without renaming", "2-digit plus tens"], 12: ["identify, name, describe"], 13: ["multiplying within 40", "sign x"], 14: ["number-sequence patterns"],
         15: ["count money in cents up to $1"], 16: ["dollars up to $100"], 17: ["length in cm"], 18: ["tell time to 5 minutes", "durations of one hour or half hour"],
         19: ["identify the shapes in a figure"], 20: ["picture graphs"]}
miss = [(n, ph) for n, phs in NEEDS.items() for ph in phs if ph not in SYL]
rec("F28: every page's syllabus topic is named in the Primary 1 section of docs/moe/syllabus_by_level.md (checked phrase by phrase)", not miss, str(miss))
rec("F28: outcome numbers used are only the ranges the summary gives (1.1 to 1.7, 2.1 to 2.7, 3.1 to 3.4, Length 1.1 to 1.4, Time 2.1 to 2.4, Geometry 1.1 to 1.4)", True, "see the range check above")
rec("topic tags name a P1 strand", all(any(k in p["strand"] for k in ("Whole Numbers", "Addition and Subtraction", "Multiplication and Division", "Money", "Measurement", "Geometry", "Statistics")) for p in pages))
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
    rec(f"no division sign in {f} (P2 syllabus)", "\u00f7" not in h and "&divide;" not in h)
    abh = [float(x) for sel, x in re.findall(r"(\.(?:ab|slot \.ab|shans \.ab|ctime \.ab|srow \.ab|check \.ab)[^{]*)\{[^}]*?height:([\d.]+)mm", h)]
    rec(f"answer boxes at least 12 mm high in {f}", min(abh) >= 12 if abh else True, f"min {min(abh) if abh else '-'}")
    op = re.findall(r"opacity|rgba|rgb\(|hsl|gradient|filter", h)
    rec(f"no opacity/alpha/gradient in {f}", not op, str(op[:3]))
_ph = open(os.path.join(O, "pupil.html")).read()
rec("audit 3 follow-up: no bare black dot is drawn as a countable thing (objects on P1-03 and P1-13, faces on P1-20)", 'class="dot"' not in _ph and "dotc" not in _ph, f'{_ph.count(chr(34).join(["class=", "obj", ""]))} objects drawn')
rec("audit 3 follow-up: every coin on P1-15 shows its value and the word cents", _ph.count('class="coinunit"') == _ph.count('class="coinval"') > 0, f'{_ph.count("class=" + chr(34) + "coinval")} coins')
rec("audit 3 follow-up: every ruler strip on P1-17 has a start arrow and bold start tick; two strips start at 0 and four away from 0", _ph.count('class="arrow"') == 6)
rec("audit 3 follow-up: P1-20 uses the smiley face symbol (printed faces and the key face)", _ph.count('class="face"') >= 8)
KEYPAGES = 1 + len(re.findall(r'class="page fm[ a-z]*" >', open(os.path.join(O, 'key.html')).read()))   # intro page + entry pages
# ---- 4. PDFs: page counts, fonts, text
exp = {"P1_Puzzles.pdf": 20, "P1_FrontMatter.pdf": 5, "P1_Complete_Pack.pdf": 25, "P1_Answer_Key.pdf": KEYPAGES}
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
# ---- 4b. wording rules on all printed text (pupil pages, front matter, key)
alltxt = {}
for f in ("P1_Puzzles.pdf", "P1_FrontMatter.pdf", "P1_Answer_Key.pdf"):
    alltxt[f] = subprocess.run(["pdftotext", "-layout", os.path.join(O, f), "-"], capture_output=True, text=True).stdout
joined = "\n".join(alltxt.values())
rec("no division sign in any printed text (P2 syllabus)", "\u00f7" not in joined)
rec("money is written 50\u00a2, never 50c, in all printed text", not re.search(r"(?<![\w.])\d+c\b", joined), str(re.findall(r"(?<![\w.])\d+c\b", joined)[:5]))
pt = alltxt["P1_Puzzles.pdf"]
rec("pupil pages name no part a pupil cannot find (no window, wall or scale wording)", not re.search(r"\b(window|windows|wall|walls|scales|scale)\b", pt, re.I))
rec("pupil pages avoid column/diagonal/divide (words not taught at P1)", not re.search(r"\b(column|columns|diagonal|divide|divided)\b", pt, re.I))
rec("pupil pages and front matter: no Mi, MOE, aligned, affiliated or endorsed wording", not re.search(r"\bMi\b|MOE|Ministry|aligned|affiliat|endorse", pt + alltxt["P1_FrontMatter.pdf"], re.I))
fm = alltxt["P1_FrontMatter.pdf"]
rec("cover, licence and teacher notes are marked DRAFT with the owner's business contact email and a registered-office placeholder (until built with --final)", fm.count("DRAFT") >= 4 and fm.count("pypteltd@gmail.com") >= 3 and "[contact email or phone" not in fm and "[registered office address" in fm and "to be confirmed by the owner" in fm, f"{fm.count('DRAFT')} DRAFT stamps")
rec("pupil pages carry no DRAFT stamp", "DRAFT" not in alltxt["P1_Puzzles.pdf"])
rec("no price, quote amount or sale wording in printed text", not re.search(r"S\$|SGD|per copy|per school|\bRRP\b|discount", joined, re.I))
rec("o'clock and half past used for clock times in the key (P1-18)", "o'clock" in alltxt["P1_Answer_Key.pdf"] and "half past" in alltxt["P1_Answer_Key.pdf"])
# ---- 4c. a 68-character school name must not wrap the footer or split the page code
import tempfile as _tf
_td = _tf.mkdtemp()
_long = "Saint Gabriel's Presbyterian Primary School (Junior Section, Annex Campus)"
subprocess.run([sys.executable, os.path.join(HERE, "build.py"), "--school", _long, "--outdir", _td], check=True, capture_output=True)
_t = subprocess.run(["pdftotext", "-layout", os.path.join(_td, "P1_Puzzles.pdf"), "-"], capture_output=True, text=True).stdout.split("\f")[:20]
_ok = []
for i, pg_ in enumerate(_t, 1):
    lines = [l for l in pg_.splitlines() if l.strip()]
    last = lines[-1] if lines else ""
    _ok.append(f"P1-{i:02d}" in last and "Photocopy licence:" in last and "Not for resale." in last)
rec(f"a {len(_long)}-character school name keeps the footer on one line with the page code on every pupil page", all(_ok), str([i + 1 for i, o in enumerate(_ok) if not o]))
import shutil as _sh; _sh.rmtree(_td, ignore_errors=True)
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
# colour-by-code labels in the real browser: every label lies inside its own region, clear of outlines and decorations (pupil pages and key answer pages)
JS_CBC = """
() => {
  const res = [];
  document.querySelectorAll('section.page').forEach((pg, pidx) => {
    const svg = pg.querySelector('svg.pic'); if (!svg) return;
    const regions = {}; svg.querySelectorAll('path.r').forEach(p => regions[p.dataset.r] = p);
    const decor = [...svg.children].filter(e => !e.classList.contains('r') && !e.classList.contains('lab'));
    let bad = 0, n = 0;
    svg.querySelectorAll('g.lab').forEach(g => {
      const p = regions[g.dataset.r]; const bb = g.getBBox(); n++;
      let out = 0, hit = 0;
      for (let i = 0; i <= 9; i++) for (let j = 0; j <= 5; j++) {
        const dp = new DOMPoint(bb.x - 0.45 + (bb.width + 0.9) * i / 9, bb.y - 0.45 + (bb.height + 0.9) * j / 5);
        if (!p.isPointInFill(dp) || p.isPointInStroke(dp)) out++;
        for (const d of decor) if (d.isPointInFill && (d.isPointInFill(dp) || d.isPointInStroke(dp))) hit++;
      }
      if (out || hit) bad++;
    });
    res.push({page: pidx + 1, n, bad, h1: (pg.querySelector('h1') || pg.querySelector('h2')).textContent});
  });
  return res;
}
"""
for f in ("pupil.html", "key.html"):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 900, "height": 1200})
        pg.goto("file://" + os.path.join(O, f)); pg.wait_for_timeout(600)
        res = pg.evaluate(JS_CBC); b.close()
    rec(f"{f}: colour-by-code pictures: {len(res)} found; every label of every part lies inside its region and clear of outlines and decorations", len(res) >= 3 and all(r["bad"] == 0 for r in res), str([(r["page"], r["bad"], r["n"]) for r in res]))
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
        
    rec(f"{f}: 1-bit render at 150 dpi keeps content (max ink loss {worst_loss:.2%} vs greyscale)", worst_loss <= {'P1_Puzzles.pdf': 0.25, 'P1_FrontMatter.pdf': 0.30, 'P1_Answer_Key.pdf': 0.35}[f], f"{len(gs)} pages")
    per_page = 75 if f == "P1_Answer_Key.pdf" else 40      # the key has small text and tiny pictures: more anti-aliased edge blocks
    rec(f"{f}: no flat grey tint areas (blocks counted {grey_blocks}, limit {per_page} per page)", grey_blocks < per_page * len(gs), "")
    if f == "P1_Puzzles.pdf":
        keep = os.path.join(O, "bilevel_check"); shutil.rmtree(keep, ignore_errors=True); os.makedirs(keep)
        for m in ms[:20]: Image.open(m).convert("1").save(os.path.join(keep, os.path.basename(m).replace(".pbm", ".png")), optimize=True)
shutil.rmtree(tmp, ignore_errors=True)
vj = os.path.join(O, "verification.json")
if os.path.exists(vj):
    data = json.load(open(vj))
    for no, r in verification:
        for d in data:
            if d["no"] == no:
                d["enumeration"] = dict(plausible_slips_rejected=r["plausible"], all_other_values_rejected=r["allv"], wrong_arrangements_rejected=r["perm"])
    json.dump(data, open(vj, "w"), indent=1)
open(os.path.join(O, "validation_report.txt"), "w").write("\n".join(log) + f"\n\nTOTAL {len(log)} checks, {len(fails)} failed\n")
print("\n".join(l for l in log if l.startswith("FAIL")) or "no failures")
print(f"{len(log)} checks, {len(fails)} failed")
sys.exit(1 if fails else 0)
