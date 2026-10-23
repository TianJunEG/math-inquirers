#!/usr/bin/env python3
"""Verify every colour-by-code worksheet. Exit code 1 on any failure. Writes out/verification.json, out/verification.txt and out/inventory.md.
   python3 verify.py [--level 2] [--out out]      (without --level: every level in turn; level N reads and writes out/pN/)
Checks (per worksheet unless noted):
  banks (every bank, both tiers): each question has exactly one answer in the bank's domain and it is the intended one; printed equations are re-evaluated from their text
  pictures: 12 to 18 regions, regions do not overlap, mirror pairs are exact mirror images, a label box at least 28 mm wide fits every region
  unique answers, answers all in the key, all five colours used, tally printed on the page equals the tally of the answers
  mirror pairs / groups / counted subset (e.g. exactly N red scales) hold and are printed correctly
  single-slip detection: every single wrong answer of every region is tried; the share caught by the page's checks must be >= 95 %
  text fit: conservative font metrics (build time) and a real browser measurement of every label against its region
  1-bit 150 dpi legibility, no grey tints, regions stay separate in the 1-bit render; page layout, fonts, wording rules, black and white only"""
import argparse, glob, html, json, os, re, subprocess, sys, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from PIL import Image
from shapely.geometry import box as sbox
import zlib
import sheet as S, build as B, layout as L
import textcheck as TC
from banks import banks, gallery, levels, rules, BOX
from pictures import PICTURES

ap = argparse.ArgumentParser(); ap.add_argument("--level", type=int); ap.add_argument("--out", default=os.path.join(HERE, "out")); a = ap.parse_args()
if a.level is None:                       # every level in turn, one process each
    rc = 0
    for n in levels(): rc |= subprocess.call([sys.executable, os.path.abspath(__file__), "--level", str(n), "--out", a.out])
    sys.exit(1 if rc else 0)
LEVEL = a.level; BANKS = banks(LEVEL); GALLERY = gallery(LEVEL); RULES = rules(LEVEL)
OUT = os.path.join(a.out, f"p{LEVEL}")
log, fails, report = [], [], {}
def rec(name, ok, detail=""):
    log.append(f'{"PASS" if ok else "FAIL"}  {name}  {detail}')
    if not ok: fails.append(name)
THRESH = 0.95

# ---------------------------------------------------------------------------------------------- 1. banks
def _amount(tok):
    """a printed amount in a choose-one-of-three line: 245, $2.45 or 35¢ -> the value as the key stores it (cents for money)"""
    m = re.fullmatch(r"\$(\d+)\.(\d\d)", tok)
    if m: return int(m[1]) * 100 + int(m[2])
    return int(tok.rstrip("\u00a2"))
def design_rules(q, tier, bank):
    """rules from the third audit that every question of every bank must keep (checked on the printed text and the art)"""
    out = []; text = " ".join(q.lines)
    head = q.lines[0] if q.lines else ""
    if len(q.lines) == 2 and (head in ("Greatest:", "Smallest:", "Middle number:") or re.fullmatch(r"Which is (odd|even)\?", head)):
        offered = [_amount(t) for t in q.lines[1].split()]
        if len(offered) != 3 or any(v not in tier.key for v in offered): out.append(("choose-one-of-three has a number that is not on the key (the key alone would answer it)", q.lines))
    if q.art is not None and q.art.meta.get("kind") == "clock":
        import art as A
        h_, m_ = A.decode_clock(q.art.meta)
        if A.hand_gap(h_, m_) < 40.0 - 1e-6: out.append(("clock hands less than 40 degrees apart", (h_, m_)))
    if q.art is not None and q.art.meta.get("kind") == "ruler" and q.art.meta["start"] != 0: out.append(("ruler strip does not start at 0", q.art.meta))
    if LEVEL == 2:
        if re.search(r"\$\d+\.\d\d\s*[+\u2212-]|[+\u2212-]\s*\$\d+\.\d\d", text) or re.search(r"Change|Paid", text): out.append(("add or subtract with decimal money (Primary 3)", q.lines))
        if re.search(r"\b1 (kg|m) \u2212", text) or re.search(r"\d+ kg [+\u2212] \d+ g|\d+ g [+\u2212] \d+ kg", text): out.append(("kg to g or m to cm conversion (Primary 3)", q.lines))
    return out

for bid, bank in BANKS.items():
    for t, tier in bank.tiers.items():
        tag = f"bank {bid} tier {t}"
        rec(f"{tag}: key has five distinct values inside the domain", len(set(tier.key)) == 5 and all(k in tier.domain for k in tier.key))
        bad, made, forms, nonum = [], 0, set(), 0
        rule_bad = []
        for ai, ans in enumerate(tier.key):
            for f in tier.forms:
                for k in range(25):
                    rng = random.Random(zlib.crc32(f"{bid}|{t}|{ai}|{f.__name__}|{k}".encode()))
                    q = f(ans, rng)
                    if q is None: continue
                    made += 1; forms.add(f.__name__)
                    rule_bad += design_rules(q, tier, bank)
                    sol = [v for v in tier.domain if q.holds(v)]
                    if sol != [ans]: bad.append((f.__name__, q.lines, sol))
                    solved = " ".join(q.sol)
                    if q.a_text is not None and BOX in " ".join(q.lines):
                        want = __import__("qcore").AFRAC(*q.a_text.split("/")) if ("\u27e8" in solved and "/" in q.a_text) else L.ANS_L + q.a_text + L.ANS_R
                        if want not in solved: bad.append((f.__name__, "answer not in teacher lines", q.sol))
                    try:                  # independent evaluator: solve the PRINTED text (and the decoded picture) without the bank's own holds() or answer
                        v_, rule_ = TC.solve(q.lines, q.art.meta if q.art is not None else None, tier.instr or bank.instr, tier.kind)
                        if not TC.matches(v_, ans): bad.append((f.__name__, "independent evaluator disagrees", q.lines, v_, ans, rule_))
                    except TC.Unparsed: bad.append((f.__name__, "independent evaluator cannot parse", q.lines))
                    for e in q.eq:        # re-evaluate the printed equation with the intended answer substituted
                        if not __import__("qcore").eq_eval(e, ans, q.eq_money): bad.append((f.__name__, "equation", e))
                    if q.extra is not None and not q.extra(ans): bad.append((f.__name__, "bank-specific picture or text check", q.lines))
                    if q.extra is None and q.art is not None and q.art.meta.get("kind") == "clock":
                        import art as A
                        if A.decode_clock(q.art.meta) != ans: bad.append((f.__name__, "clock hands", q.art.meta))
                    if q.extra is None and q.art is not None and q.art.meta.get("kind") == "ruler":
                        m = q.art.meta
                        if m["end"] - m["start"] != ans: bad.append((f.__name__, "ruler", m))
                    if q.extra is None and q.art is not None and q.art.meta.get("kind") in ("coins", "notes"):
                        if sum(q.art.meta["values"]) != ans: bad.append((f.__name__, "coins", q.art.meta))
                    if q.extra is None and q.art is not None and q.art.meta.get("kind") == "shapes":
                        import art as A
                        if sum(A.SHAPES[k_] for k_ in q.art.meta["kinds"]) * (1 if t == 1 else 2) != ans: bad.append((f.__name__, "shapes", q.art.meta))
                    if hasattr(q, "seq"):
                        terms, blank = q.seq
                        if terms[blank] != ans: bad.append((f.__name__, "sequence", q.seq))
        rec(f"{tag}: {made} sample questions each have exactly one answer in the domain, equal to the intended one ({len(forms)} forms)", not bad and made > 200, str(bad[:2])[:150])
        rec(f"{tag}: {len(rule_bad)} design-rule breaches in the sample questions (choose-one-of-three numbers all on the key, clocks with hands >= 40 degrees apart, rulers from 0, no decimal-money sums or kg/g conversions at Primary 2)", not rule_bad, str(rule_bad[:2])[:200])
        report[tag] = dict(questions=made, forms=sorted(forms), bad=len(bad))

# the evaluator must be able to fail: a wrong answer, and a wrong question text, must both be rejected
_v, _ = TC.solve(["10 less than 71,", f"then 1 more: {BOX}"]); rec("evaluator self-test: '10 less than 71, then 1 more' is 62, not 60", _v == 62 and not TC.matches(_v, 60))
_v, _ = TC.solve(["10 more than 54,", f"then 1 more: {BOX}"]); rec("evaluator self-test: '10 more than 54, then 1 more' is 65", _v == 65)
_v, _ = TC.solve(["35\u00a2 + $1.20 = " + BOX + "\u00a2"]); rec("evaluator self-test: money equation", _v == 155)
try: TC.solve(["Colour the owl's left wing: " + BOX]); rec("evaluator self-test: an unknown question is refused", False)
except TC.Unparsed: rec("evaluator self-test: an unknown question is refused", True)

# ---------------------------------------------------------------------------------------------- 2. pictures
for pid, fn in PICTURES.items():
    pic = fn(); n = len(pic.regions); tag = f"picture {pid}"
    rec(f"{tag}: 12 to 18 regions", 12 <= n <= 18, str(n))
    rec(f"{tag}: every region is one valid polygon, area >= 250 mm2, inside the canvas", all(r.geom.is_valid and r.geom.geom_type == "Polygon" and r.geom.area >= 250 and r.geom.bounds[0] >= -0.01 and r.geom.bounds[2] <= 180.01 and r.geom.bounds[1] >= -0.01 and r.geom.bounds[3] <= 200.01 for r in pic.regions))
    ov = [(a_.id, b_.id, round(a_.geom.intersection(b_.geom).area, 2)) for i, a_ in enumerate(pic.regions) for b_ in pic.regions[i + 1:] if a_.geom.intersection(b_.geom).area > 1.0]
    rec(f"{tag}: regions do not overlap", not ov, str(ov[:3]))
    ids = [r.id for r in pic.regions]; rec(f"{tag}: region ids are unique", len(set(ids)) == n)
    by = pic.by_id()
    from geom import mir
    bad = [(l, r) for l, r in pic.mirror_pairs if by[l].geom.symmetric_difference(mir(by[r].geom)).area > 0.5]
    rec(f"{tag}: mirror pairs are exact mirror images ({len(pic.mirror_pairs)} pairs)", not bad, str(bad))
    narrow = []
    for r in pic.regions:
        w12 = max([b[2] for b in pic.boxes(r.id) if b[3] <= 12.0] or [0])
        if w12 < 28.0: narrow.append((r.id, w12))
    rec(f"{tag}: a label box at least 28 mm wide and 12 mm high fits every region", not narrow, str(narrow))
    report[tag] = dict(regions=n, pairs=len(pic.mirror_pairs), twins=len(pic.twins))

# ---------------------------------------------------------------------------------------------- 3. worksheets
def pdftext(path): return subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True).stdout

def slip_stats(sh):
    """try every single wrong answer in every region; count how many the page's checks reject"""
    pic, tier, key, idx = sh["pic"], sh["tier"], sh["key"], sh["idx"]
    truth = {r.id: key.index(sh["items"][r.id]["answer"]) for r in pic.regions}
    assert truth == idx
    base = {k: sum(1 for v in truth.values() if v == k) for k in range(5)}
    def failed_checks(col): return S.flags(sh, col)
    assert not failed_checks(dict(truth)), "right answers must pass every check"
    tot = in_key = det_all = det_key = det_structure = 0
    for r in pic.regions:
        for w in tier.domain:
            if w == sh["items"][r.id]["answer"]: continue
            tot += 1
            if w not in key: det_all += 1; continue            # no crayon colour exists for this answer: the pupil sees it at once
            in_key += 1
            col = dict(truth); col[r.id] = key.index(w)
            f = failed_checks(col)
            if f: det_all += 1; det_key += 1
            if any(x != "tally" for x in f): det_structure += 1
    # double slips by full enumeration: every pair of regions, each coloured with any wrong colour (4 x 4 cases per pair); a swap is the case
    # where the two regions exchange their colours (the tally does not change), which only the mirror or twin-mark checks can catch
    ids = [r.id for r in pic.regions]; d_tot = d_det = sw_tot = sw_det = 0; d_tally_only = 0
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a_, b_ = ids[i], ids[j]
            for ca in range(5):
                if ca == truth[a_]: continue
                for cb in range(5):
                    if cb == truth[b_]: continue
                    col = dict(truth); col[a_] = ca; col[b_] = cb
                    f = failed_checks(col); d_tot += 1
                    if f: d_det += 1
                    if f == ["tally"]: d_tally_only += 1
                    if ca == truth[b_] and cb == truth[a_]:
                        sw_tot += 1
                        if f: sw_det += 1
    return dict(double_cases=d_tot, double_detected=d_det, double_rate=round(d_det / d_tot, 4), swap_cases=sw_tot, swap_detected=sw_det,
                swap_rate=round(sw_det / max(sw_tot, 1), 4)) | dict(wrong_values=tot, in_key=in_key, detected_all=det_all, rate_all=round(det_all / tot, 4), detected_in_key=det_key,
                rate_in_key=round(det_key / max(in_key, 1), 4), caught_by_structure_checks=round(det_structure / max(in_key, 1), 4))

def tally_from_pdf(txt):
    m = re.search(r"You should have:\s*yellow (\d+), red (\d+), blue (\d+), green (\d+), orange (\d+)", re.sub(r"\s+", " ", txt))
    return [int(x) for x in m.groups()] if m else None

sheets = [S.make_sheet(sp, "") for sp in GALLERY]
ws_report = {}
for sh in sheets:
    sp = sh["spec"]; wid = sp["id"]; pic, bank, tier = sh["pic"], sh["bank"], sh["tier"]
    R = {}; ws_report[wid] = R
    slug = B.slug(sp)
    pdf_p, pdf_t = os.path.join(OUT, slug + "_pupil.pdf"), os.path.join(OUT, slug + "_teacher.pdf")
    rec(f"{wid}: pupil and teacher PDFs exist", os.path.exists(pdf_p) and os.path.exists(pdf_t))
    if not (os.path.exists(pdf_p) and os.path.exists(pdf_t)): continue
    items = sh["items"]
    # unique answer per question, in the key
    probs = []
    for rid, it in items.items():
        sol = [v for v in tier.domain if it["q"].holds(v)]
        if sol != [it["answer"]]: probs.append((rid, it["q"].lines, sol))
        if it["answer"] not in sh["key"]: probs.append((rid, "answer not in key"))
    rec(f"{wid}: every question has exactly one answer and it is one of the five key values", not probs, str(probs[:2]))
    # independent evaluator on every printed question of this worksheet (the page as printed, not the bank's answers)
    ev_bad = []; ev_rules = set()
    for rid, it in items.items():
        q = it["q"]
        try:
            v_, rule_ = TC.solve(q.lines, q.art.meta if q.art is not None else None, tier.instr or bank.instr, tier.kind); ev_rules.add(rule_)
            if not TC.matches(v_, it["answer"]) or it["answer"] not in sh["key"]: ev_bad.append((rid, q.lines, v_, it["answer"]))
        except TC.Unparsed: ev_bad.append((rid, q.lines, "unparsed"))
    rec(f"{wid}: independent evaluator re-solves all {len(items)} printed questions from their text and picture; each equals the answer coloured and that answer is a key value", not ev_bad, str(ev_bad[:2]))
    rb = [x for it in items.values() for x in design_rules(it["q"], tier, bank)]
    rec(f"{wid}: design rules hold on every printed question (choose-one-of-three numbers all on the key, clocks >= 40 degrees, rulers from 0, no Primary 3 money or mass items)", not rb, str(rb[:2])[:200])
    # dedupe by what a question IS (sorted numbers, wording without line breaks, decoded picture), not by its text
    sigs = [S.canon(it["q"]) for it in items.values()]
    rec(f"{wid}: no two regions have the same question (compared by evaluated content: operands in any order, same clock, same coins, same picture)", len(set(sigs)) == len(sigs), f"{len(sigs) - len(set(sigs))} repeated")
    texts = [" ".join(it["q"].lines).replace("\u27e6", "").replace("\u27e7", "") for it in items.values()]
    faces = [S.canon(it["q"])[2] for it in items.values() if it["q"].art is not None and it["q"].art.meta.get("kind") == "clock"]
    digital = [" ".join(it["q"].lines) for it in items.values() if re.fullmatch(r"(?:[A-Za-z ]+: )?\d{1,2}:\d\d(?:[^\d].*)?", " ".join(it["q"].lines)) and it["q"].art is None]
    rec(f"{wid}: no clock face is drawn twice and no digital time is printed twice", len(set(faces)) == len(faces) and len(set(digital)) == len(digital))
    # key coverage and tally
    colours_used = [sh["key"].index(it["answer"]) for it in items.values()]
    cnt = [colours_used.count(k) for k in range(5)]
    rec(f"{wid}: all five key values and colours are used (counts {cnt}, each at least 2)", min(cnt) >= 2)
    tp = tally_from_pdf(pdftext(pdf_p)); tt = tally_from_pdf(pdftext(pdf_t))
    rec(f"{wid}: tally printed on the pupil page equals the tally of the answers", tp == cnt, f"printed {tp}")
    rec(f"{wid}: tally printed on the teacher page equals the tally of the answers", tt == cnt, f"printed {tt}")
    ans = {r.id: items[r.id]["answer"] for r in pic.regions}
    rec(f"{wid}: mirror pairs share one colour ({len(pic.mirror_pairs)} pairs)", all(ans[l] == ans[r] for l, r in pic.mirror_pairs))
    rec(f"{wid}: twin-mark sets share one colour ({len(pic.twins)} sets)", all(len({ans[i] for i in ids_}) == 1 for ids_, _ in pic.twins))
    for s in [c for c in sh["checks"] if c[0] == "subset"]:
        ids, k, c = s[2], s[3], s[4]
        real = sum(1 for i in ids if ans[i] == sh["key"][k])
        printed = re.search(r"Exactly (\d+)", re.sub(r"\s+", " ", pdftext(pdf_p)))
        rec(f"{wid}: counted-subset check '{s[1]}' is true of the answers and printed correctly", real == c and printed and int(printed.group(1)) == c, f"real {real}")
    # single slips
    st = slip_stats(sh); R["single_slip"] = st
    rec(f"{wid}: single-slip detection {st['detected_all']}/{st['wrong_values']} = {st['rate_all']:.1%} (every wrong value of every region; needs >= 95%)", st["rate_all"] >= THRESH)
    rec(f"{wid}: single-slip detection for wrong values that do have a crayon colour {st['detected_in_key']}/{st['in_key']} = {st['rate_in_key']:.1%} (needs >= 95%)", st["rate_in_key"] >= THRESH)
    rec(f"{wid}: double-slip detection by enumeration {st['double_detected']}/{st['double_cases']} = {st['double_rate']:.1%} (every pair of regions, every pair of wrong colours; needs >= 95%)", st["double_rate"] >= THRESH)
    rec(f"{wid}: swap detection {st['swap_detected']}/{st['swap_cases']} = {st['swap_rate']:.1%} (two regions exchange their colours, tally unchanged; needs >= 95%)", st["swap_rate"] >= THRESH)
    # geometric fit of every label (conservative metrics) with margin to the outline
    prob = []
    minf = 99; tmin = 99; short = 0
    for r in pic.regions:
        it = items[r.id]
        for lab, pl in (("pupil", it["place"]), ("teacher", it["tplace"])):
            cx, cy = pl["box"][0], pl["box"][1]
            rect = sbox(cx - pl["w"] / 2, cy - pl["h"] / 2, cx + pl["w"] / 2, cy + pl["h"] / 2)
            if not r.geom.buffer(-0.6).contains(rect): prob.append((r.id, lab))
            if lab == "pupil": minf = min(minf, pl["f"]); R.setdefault("label_widths", []).append(round(pl["box"][2], 1))
            else: tmin = min(tmin, pl["f"])
        short += it["teacher_short"]
    rec(f"{wid}: every label lies inside its region with at least 0.6 mm clear of the outline (conservative metrics)", not prob, str(prob[:3]))
    rec(f"{wid}: smallest pupil text {minf} mm (>= 4.2 mm, about 12 pt)", minf >= 4.2)
    R["min_pupil_font_mm"] = minf; R["min_teacher_font_mm"] = tmin; R["teacher_short_labels"] = short
    del R["label_widths"]
    from shapely.geometry import LineString
    chords = []
    for r in pic.regions:
        cx, cy = items[r.id]["place"]["box"][0], items[r.id]["place"]["box"][1]
        seg = r.geom.intersection(LineString([(-5, cy), (185, cy)]))
        parts = [seg] if seg.geom_type == "LineString" else list(seg.geoms)
        parts = [s_ for s_ in parts if s_.geom_type == "LineString"]
        w = max((s_.length for s_ in parts if s_.distance(__import__("shapely.geometry", fromlist=["Point"]).Point(cx, cy)) < 0.01), default=0)
        chords.append((round(w, 1), r.id))
    R["narrowest_region_width_at_label_mm"] = min(chords)[0]
    rec(f"{wid}: every region is at least 28 mm wide where its label sits (narrowest {min(chords)})", min(chords)[0] >= 28.0)

# ---------------------------------------------------------------------------------------------- 4. browser: real text against real regions
from playwright.sync_api import sync_playwright
JS = """
() => {
  const svg = document.querySelector('svg.pic'); const out = {labels: [], decor: 0, issues: []};
  const regions = {}; svg.querySelectorAll('path.r').forEach(p => regions[p.dataset.r] = p);
  const decor = [...svg.children].filter(e => !e.classList.contains('r') && !e.classList.contains('lab'));
  svg.querySelectorAll('g.lab').forEach(g => {
    const id = g.dataset.r; const p = regions[id]; const bb = g.getBBox();
    const pts = []; const nx = 9, ny = 5;
    for (let i = 0; i <= nx; i++) for (let j = 0; j <= ny; j++) pts.push([bb.x - 0.45 + (bb.width + 0.9) * i / nx, bb.y - 0.45 + (bb.height + 0.9) * j / ny]);
    let outside = 0, hit = 0;
    for (const [x, y] of pts) {
      const dp = new DOMPoint(x, y);
      if (!p.isPointInFill(dp) || p.isPointInStroke(dp)) outside++;
      for (const d of decor) if (d.isPointInFill && (d.isPointInFill(dp) || d.isPointInStroke(dp))) hit++;
    }
    // text actually measured: widest text run
    let tw = 0; g.querySelectorAll('text').forEach(t => tw = Math.max(tw, t.getBBox().width));
    out.labels.push({id, x: bb.x, y: bb.y, w: bb.width, h: bb.height, outside, hit, fs: Math.min(...[...g.querySelectorAll('text')].map(t => parseFloat(t.style.fontSize || 99)))});
  });
  const page = document.querySelector('.page'); const r = svg.getBoundingClientRect(); const mm = 25.4 / 96;
  out.svg = {left: r.left * mm, top: r.top * mm, width: r.width * mm, height: r.height * mm};
  const chk = document.querySelector('.chk').getBoundingClientRect(), ft = document.querySelector('footer').getBoundingClientRect(), hd = document.querySelector('header').getBoundingClientRect();
  out.layout = {pageOverflow: page.scrollHeight > page.clientHeight + 1, svgBottom: r.bottom * mm, chkTop: chk.top * mm, chkBottom: chk.bottom * mm, footerTop: ft.top * mm, footerBottom: ft.bottom * mm, headerTop: hd.top * mm,
    minLeft: Math.min(...[...page.querySelectorAll('*')].map(e => e.getBoundingClientRect()).filter(b => b.width > 0).map(b => b.left)) * mm,
    maxRight: Math.max(...[...page.querySelectorAll('*')].map(e => e.getBoundingClientRect()).filter(b => b.width > 0).map(b => b.right)) * mm};
  return out;
}
"""
browser_res = {}
with sync_playwright() as pw:
    br = pw.chromium.launch()
    for sh in sheets:
        sp = sh["spec"]; wid = sp["id"]; slug = B.slug(sp)
        for kind in ("pupil", "teacher"):
            hp = os.path.join(OUT, "html", f"{slug}_{kind}.html")
            if not os.path.exists(hp): rec(f"{wid} {kind}: html exists", False); continue
            pg = br.new_page(viewport={"width": 794, "height": 1123}); pg.goto("file://" + hp); pg.wait_for_timeout(600)
            res = pg.evaluate(JS); pg.close(); browser_res[(wid, kind)] = res
            bad = [l for l in res["labels"] if l["outside"] or l["hit"]]
            rec(f"{wid} {kind}: real browser text of all {len(res['labels'])} labels lies inside its region, clear of outlines and decorations", not bad, str([(b['id'], b['outside'], b['hit']) for b in bad][:4]))
            lay = res["layout"]
            rec(f"{wid} {kind}: layout: no page overflow, picture above the check box, check box above the footer, 14.4 to 195.6 mm sides",
                not lay["pageOverflow"] and lay["svgBottom"] <= lay["chkTop"] + 0.1 and lay["chkBottom"] <= lay["footerTop"] + 0.1 and lay["minLeft"] >= 14.0 and lay["maxRight"] <= 196.0 and lay["footerBottom"] <= 297 - 6, str({k: round(v, 1) if isinstance(v, float) else v for k, v in lay.items()}))
    br.close()

# ---------------------------------------------------------------------------------------------- 5. PDFs: wording, fonts, size, 1-bit legibility
import tempfile
tmp = tempfile.mkdtemp()
FORBIDDEN = re.compile(r"S\$|SGD|per copy|per school|\bRRP\b|discount|\bMi\b|MOE|Ministry|aligned|alignment|affiliat|endorse" + ("" if RULES.get("allow_division_sign") else "|÷"), re.I)
total_bytes = 0
for sh in sheets:
    sp = sh["spec"]; wid = sp["id"]; slug = B.slug(sp)
    for kind in ("pupil", "teacher"):
        path = os.path.join(OUT, f"{slug}_{kind}.pdf")
        if not os.path.exists(path): continue
        total_bytes += os.path.getsize(path)
        info = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
        rec(f"{wid} {kind}: one A4 page", re.search(r"Pages:\s+1\b", info) is not None and "(A4)" in info)
        fo = subprocess.run(["pdffonts", path], capture_output=True, text=True).stdout.splitlines()[2:]
        rec(f"{wid} {kind}: fonts embedded", all(l.split()[-5] == "yes" for l in fo if l.strip()), f"{len(fo)} fonts")
        txt = pdftext(path)
        rec(f"{wid} {kind}: wording rules (no price, Mi, alignment claim, division sign; cents written 50¢ not 50c)", not FORBIDDEN.search(txt) and not re.search(r"(?<![\w.])\d+c\b", txt), str(FORBIDDEN.findall(txt)[:3]))
        rec(f"{wid} {kind}: footer has a school-name field and the worksheet code", "School name:" in txt and wid in txt)
        if sp["bank"] == "time" and RULES.get("time_words_only"): rec(f"{wid} {kind}: time uses only o'clock and half past", not re.search(r"quarter|\bten past|twenty|\bto \d", txt, re.I))
        h = open(os.path.join(OUT, "html", f"{slug}_{kind}.html")).read()
        body = h[h.index("<body>"):]
        cols = set(c.lower() for c in re.findall(r"#[0-9a-fA-F]{3,6}\b", h))
        rec(f"{wid} {kind}: html uses only black and white (#000, #fff)", cols <= {"#000", "#fff", "#000000", "#ffffff"} and not re.search(r"(?:fill|stroke|color|background)\s*[:=]\s*[\"']?(red|blue|green|gray|grey|orange|yellow)", h, re.I), str(sorted(cols))[:60])
        bxw = [float(x) for x in re.findall(r'<rect class="bx" data-l="\d+" data-t="\u25a1"[^>]*? width="([\d.]+)"', h)]
        if kind == "pupil": rec(f"{wid} pupil: every blank box a pupil writes in is at least 5 mm wide ({len(bxw)} boxes, smallest {min(bxw) if bxw else '-'} mm)", all(w >= 5.0 for w in bxw))
        sw = [float(x) for x in re.findall(r'stroke-width[=:]\s*"?([\d.]+)', h)]
        rec(f"{wid} {kind}: outline width 0.9 mm and no line thinner than 0.3 mm", "stroke-width:0.9" in h and min(sw) >= 0.3, f"min {min(sw)}")
        # 1-bit legibility at 150 dpi
        d = os.path.join(tmp, f"{wid}{kind}"); os.makedirs(d)
        subprocess.run(["pdftoppm", "-r", "150", "-gray", path, os.path.join(d, "g")], check=True)
        subprocess.run(["pdftoppm", "-r", "150", "-mono", path, os.path.join(d, "m")], check=True)
        G = np.array(Image.open(glob.glob(d + "/g-*.pgm")[0]).convert("L")); M = np.array(Image.open(glob.glob(d + "/m-*.pbm")[0]).convert("L"))
        loss = 1 - (M < 128).sum() / max((G < 235).sum(), 1)
        rec(f"{wid} {kind}: 1-bit render at 150 dpi keeps the ink (loss {loss:.1%}, needs <= 25%)", loss <= 0.25)
        # grey flat tints
        blocks = G[:G.shape[0] // 6 * 6, :G.shape[1] // 6 * 6].reshape(G.shape[0] // 6, 6, G.shape[1] // 6, 6)
        mn, mx = blocks.min(axis=(1, 3)), blocks.max(axis=(1, 3))
        grey = int(((mn > 40) & (mx < 215)).sum())
        rec(f"{wid} {kind}: no flat grey tint areas in the greyscale render ({grey} blocks, limit 60)", grey < 60)
        # regions stay separate: connected white areas in the 1-bit image
        from scipy import ndimage
        white = M > 128
        lab, n = ndimage.label(white)
        sizes = np.bincount(lab.ravel())[1:]
        big = int((sizes >= 600).sum())      # background (1) + each region; glyph holes are far smaller
        npics = len(sh["pic"].regions)
        rec(f"{wid} {kind}: all {npics} regions stay separate white areas in the 1-bit render ({big} large white areas incl. background and boxes)", big >= npics + 1, "")
        # per label ink retention in the 1-bit render
        res = browser_res.get((wid, kind))
        if res:
            ox, oy = res["svg"]["left"], res["svg"]["top"]; worst = 0; worst_id = ""
            for lb in res["labels"]:
                x0 = int((ox + lb["x"] + 0.5) / 25.4 * 150) - 2; x1 = int((ox + lb["x"] + lb["w"] + 0.5) / 25.4 * 150) + 2
                y0 = int((oy + lb["y"] + 0.5) / 25.4 * 150) - 2; y1 = int((oy + lb["y"] + lb["h"] + 0.5) / 25.4 * 150) + 2
                g = (G[y0:y1, x0:x1] < 235).sum(); m = (M[y0:y1, x0:x1] < 128).sum()
                ls = 1 - m / max(g, 1)
                if ls > worst: worst, worst_id = ls, lb["id"]
            rec(f"{wid} {kind}: every label keeps its ink in the 1-bit render (worst {worst:.0%} lost, {worst_id}; needs <= 40%)", worst <= 0.40)
    # gallery files
rec("all PDFs together are under 20 MB", total_bytes < 20e6, f"{total_bytes / 1e6:.2f} MB")
cs = os.path.join(OUT, "contact_sheet.pdf")
rec("contact sheet PDF exists with 2 pages", os.path.exists(cs) and re.search(r"Pages:\s+2\b", subprocess.run(["pdfinfo", cs], capture_output=True, text=True).stdout) is not None)
LO_HI = {1: (12, 14), 2: (14, 16)}.get(LEVEL, (10, 16))
rec(f"Primary {LEVEL} gallery has {LO_HI[0]} to {LO_HI[1]} worksheets, at least 5 pictures, at least 6 topics, mixed stars, unique ids",
    LO_HI[0] <= len(GALLERY) <= LO_HI[1] and len({g["picture"] for g in GALLERY}) >= 5 and len({g["bank"] for g in GALLERY}) >= 6 and {g["tier"] for g in GALLERY} == {1, 2} and len({g["id"] for g in GALLERY}) == len(GALLERY),
    f"{len(GALLERY)} worksheets, {len({g['picture'] for g in GALLERY})} pictures, {len({g['bank'] for g in GALLERY})} topics")
rec("library has at least 5 pictures and 6 topic banks", len(PICTURES) >= 5 and len(BANKS) >= 6, f"{len(PICTURES)} pictures, {len(BANKS)} banks")

# ---------------------------------------------------------------------------------------------- report
open(os.path.join(OUT, "verification.txt"), "w").write("\n".join(log) + f"\n\n{len(log) - len(fails)} passed, {len(fails)} failed\n")
inv = ["| id | picture | topic | stars | key (answers, in colour order yellow, red, blue, green, orange) | regions | checks printed on the page | single-slip detection | double-slip / swap detection | min text | verification |", "|---|---|---|---|---|---|---|---|---|---|---|"]
for sh in sheets:
    sp = sh["spec"]; R = ws_report.get(sp["id"], {}); st = R.get("single_slip", {})
    chk = ["tally"] + (["mirror pairs"] if sh["pic"].mirror_pairs else []) + (["small marks (parts with the same mark share a colour)"] if sh["pic"].twins else []) + [s[1].split(":")[0].split(".")[0].replace("The ", "").lower() + " count" for s in sh["checks"] if s[0] == "subset"]
    mine = [l for l in log if l.startswith("FAIL") and sp["id"] in l]
    inv.append(f"| {sp['id']} | {sh['pic'].title} | {sh['bank'].topic_for(sp['tier'])} | {sp['tier']} | {', '.join(sh['tier'].disp(k) for k in sh['key'])} | {len(sh['pic'].regions)} | {', '.join(chk)} | {st.get('detected_all', 0)}/{st.get('wrong_values', 0)} = {st.get('rate_all', 0):.1%} | {st.get('double_rate', 0):.1%} / {st.get('swap_rate', 0):.1%} | {R.get('min_pupil_font_mm', 0)} mm | {'PASS' if not mine else 'FAIL'} |")
open(os.path.join(OUT, "inventory.md"), "w").write("\n".join(inv) + "\n")
json.dump(dict(passed=len(log) - len(fails), failed=len(fails), failures=fails, worksheets=ws_report, banks_and_pictures=report), open(os.path.join(OUT, "verification.json"), "w"), indent=1)
print("\n".join(l for l in log if l.startswith("FAIL")) or "no failures")
print(f"{len(log) - len(fails)} passed, {len(fails)} failed")
sys.exit(1 if fails else 0)
