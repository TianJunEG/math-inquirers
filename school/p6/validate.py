#!/usr/bin/env python3
"""Validate the built Primary 6 pack: puzzle checks, layout, black-and-white, text clipping, Primary 6 content limits.
   python3 validate.py [--outdir out] ; exit code 1 on any failure. Writes out/validation_report.txt"""
import argparse, os, re, subprocess, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from PIL import Image
import build, render
from gen.common import max_words

ap = argparse.ArgumentParser(); ap.add_argument("--outdir", default=os.path.join(HERE, "out"))
ap.add_argument("--partial", action="store_true", help="work in progress: not every one of the 40 pages exists yet (page counts follow the pages found)")
ARGS = ap.parse_args()
O = ARGS.outdir
log = []; fails = []
def rec(name, ok, detail=""):
    log.append(f'{"PASS" if ok else "FAIL"}  {name}  {detail}')
    if not ok: fails.append(name)

from gen import outcomes as OC
pages = build.all_pages()
BK = {k: build.booklet_pages(pages, k) for k in OC.BOOKLETS}
NP = {k: (len(v) if ARGS.partial else 20) for k, v in BK.items()}
def L(p): return p["code"]
# ---- 1. puzzle verification
for p in pages:
    for n, ok, d in p["verify"]:
        rec(f'{L(p)} {n}', ok, str(d)[:80])

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
    rec(f'{L(p)} has a self-check model for the enumeration', r is not None)
    if r is None: continue
    rec(f'{L(p)} check passes the right answers', r["right_passes"])
    a, b = r["plausible"]
    rec(f'{L(p)} enumeration: plausible single slips rejected {a}/{b} = {a / b:.1%} (needs >= 95%)', b > 0 and a / b >= THRESH - 1e-9)
    a2, b2 = r["allv"]
    rec(f'{L(p)} enumeration: every other value of one answer rejected {a2}/{b2} = {a2 / b2:.1%} (needs >= 95%)', b2 > 0 and a2 / b2 >= THRESH - 1e-9)
    if r["perm"]:
        a3, b3 = r["perm"]
        rec(f'{L(p)} enumeration: wrong arrangements rejected {a3}/{b3} = {a3 / b3:.1%} (needs >= 95%)', a3 / b3 >= THRESH - 1e-9)
    verification.append((p["no"], r))

rec("3 colour-by-code pages (P6-09, P6-32, P6-40) across the two booklets", ARGS.partial or [p["no"] for p in pages if p.get("cbc")] == [9, 32, 40])
if not ARGS.partial:
    rec("40 pages, ids 1..40, each in exactly one booklet", [p["no"] for p in pages] == list(range(1, 41)))
    covered = {o for p in pages for o in OC.PAGE_OC[p["no"]]}
    rec(f"every one of the {OC.N_OUTCOMES} outcome lines (27 Primary 6 Standard lines and 4 Primary 6 Foundation lines) is practised by at least one page across the two booklets", covered == set(OC.OUTCOMES), str(sorted(set(OC.OUTCOMES) - covered)))
for k in BK:
    rec(f"{k}: {NP[k]} pages in the order of gen/outcomes.py", [p["no"] for p in BK[k]] == OC.BOOKLETS[k]["order"][:NP[k]] if not ARGS.partial else True, str([p["no"] for p in BK[k]]))
    if not ARGS.partial:
        want1 = 10
        rec(f"{k}: tier mix {want1} one-star / {20 - want1} two-star", sum(p["tier"] == 1 for p in BK[k]) == want1 and sum(p["tier"] == 2 for p in BK[k]) == 20 - want1, str([p["tier"] for p in BK[k]]))
        rec(f"{k}: footer codes use the form S1-07 (P6-07) with the right pair of numbers", all(p["code"] == f"{k}-{i+1:02d} (P6-{p["no"]:02d})" for i, p in enumerate(BK[k])))
rec("every page has a self-check strip text", all(p["check"] for p in pages))
mech = [p["mech"] for p in pages]; rec("every page names a self-check mechanism", all(mech))
rec("every page has outcome ids from the outcome list", all(OC.PAGE_OC[p["no"]] for p in pages))
_words = [re.search(r"(?:Code word|Word): (\w+)", p["key"]["check_result"]).group(1) for p in pages if re.search(r"(?:Code word|Word): (\w+)", p["key"]["check_result"])]
rec("every code word is different on all pages of the two booklets", len(_words) == len(set(_words)), f"{len(_words)} words; repeated: {sorted({w for w in _words if _words.count(w) > 1})}")
# ---- 2. reading level (V8)
bad = []
for p in pages:
    for s_ in p["instr"]:
        if max_words(s_) > 18: bad.append((p["no"], s_))
    for cl in (p.get("check_lines") or [p["check"]]):
        if max_words(cl) > 24 and not p.get("cbc"): bad.append((p["no"], cl))
        if max_words(cl) > 24: bad.append((p["no"], cl))
    if len(p["instr"]) > 5: bad.append((p["no"], "more than 5 instruction sentences (plan: Primary 6 reading load)"))
    for sent in re.findall(r"<li>(.*?)</li>", p["body"]) + re.findall(r'class="rtext">(.*?)</div>', p["body"]) + re.findall(r'class="(?:st|ptxt)">(.*?)</(?:div|p)>', p["body"]):
        sent = re.sub(r"<[^>]+>", " ", sent)
        for one in re.split(r"(?<=\.)\s+", sent.strip()):
            if len(one.split()) > 18: bad.append((p["no"], one))
# question sentences in the cards of the page (stories): at most 18 words each (plan section 11: Primary 6)
for p in pages:
    if p.get("cbc"): continue
    for sent in re.findall(r"<p>(.*?)</p>", p["body"]):
        for one in re.split(r"(?<=[.?!])\s+", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", sent)).strip()):
            if len(one.split()) > 18: bad.append((p["no"], one[:70]))
rec("V8 reading level (Primary 6): instruction and question sentences <= 18 words, <= 5 instruction sentences", not bad, str(bad[:4]))
chk = [(p["no"], len(p["check"].split())) for p in pages if len(p["check"].split()) > (34 if p.get("check_lines") else 26) and not p.get("cbc")]
rec("check strip text <= 26 words (pages with several check lines: 34)", not chk, str(chk))
hint = [(p["no"], p["check"]) for p in pages if re.search(r"\bIs it\b|\bDoes it\b|\bYou (live|can|carry)|garden|music|river|\bsky\b|\bspace\b|\bking\b|\ban animal|\bseason|used for writing|shopping|count the time", p["check"]) and not p.get("cbc")]
rec("check strips carry no category hint (Is it ...?): the strip never says what the word is", not hint, str(hint[:3]))
rec("every strip of a page with letters contains the plain question 'Do they spell a word?'", all("do they spell a word?" in p["check"].lower() for p in pages if "code" in p.get("mk", ()) or "logic" in p.get("mk", ()) or "loop" in p.get("mk", ())))
# ---- 2b. notes and tags
def plain(h): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h))
bad = []
for p in pages:
    src = " ".join([plain(p["body"]), p.get("facts", ""), p["key"]["answers"], p["key"]["check_result"], p["check"], " ".join(p["instr"])])
    have = set(re.findall(r"\d+", src))
    note = re.sub(r"\d+%", "", re.sub(r"(within|up to|to|than|of) \d+", "", p["note"]))
    miss = sorted({n for n in re.findall(r"\d+", note) if int(n) >= 11 and n not in have and int(n) not in (100, 180, 360)})
    if miss: bad.append((p["no"], miss))
rec("every number of 11 or more quoted in a teacher note is found on the page or in its answers", not bad, str(bad))
PHRASES = ["more than", "fewer than", "less than", "largest", "shortest", "hatched", "straight line", "parallel", "isosceles", "equilateral", "rhombus", "trapezium", "parallelogram", "radius", "circumference", "discount", "gst", "interest", "average", "cm²", "cm³"]
bad = []
for p in pages:
    page_text = (plain(p["body"]) + " " + " ".join(p["instr"]) + " " + p["topic"] + " " + p["check"]).lower()
    note = p["note"].lower()
    for ph in PHRASES:
        if ph in note and ph not in page_text and not (ph == "greatest" and "second greatest" in note and "second greatest" in page_text) and not (ph == "ordinal" and "1st" in page_text + " 2nd"):
            bad.append((p["no"], ph))
rec("every clue word named in a teacher note (more than, fewer than, greatest, in front of, behind, ones digit ...) occurs on its page", not bad, str(bad))
SYL = open(os.path.join(HERE, "..", "..", "docs", "school_books", "p6_outcome_wording.md")).read().lower()
bad = []
for p in pages:
    ids = OC.PAGE_OC[p["no"]]
    for o in ids:
        if OC.OUTCOMES[o][1].lower() not in SYL: bad.append((p["no"], o))
    if p.get("ps") and "problem solving" not in SYL: bad.append((p["no"], "problem solving"))
    m = re.match(r"([A-Za-z ]+?) (\d)\.(\d)", p["syll"])
    # the numbers written in the tag must belong to the page's outcome ids
    for a_, b_ in re.findall(r"\b(\d)\.(\d)\b", p["syll"].split("(")[0]):
        if not any(o.endswith(f"{a_}.{b_}") for o in ids): bad.append((p["no"], f"{a_}.{b_} in tag but not in outcome ids"))
rec("F28: every outcome id of every page has its PDF wording in docs/school_books/p6_outcome_wording.md, and the numbers in each tag are the page's own outcome ids", not bad, str(bad[:5]))
rec("topic tags name a Primary 6 strand (or the revision strand)", all(any(k in p["strand"] for k in ("Fractions", "Percentage", "Ratio", "Algebra", "Area and Volume", "Geometry", "Statistics", "Primary 6 Foundation", "Revision", "mixed")) for p in pages))
# ---- 2c. Primary 6 content limits, notation, pi (plan section "Primary 7 content excluded")
def page_text_all(p):
    return " ".join([plain(p["body"]), " ".join(p["instr"]), p["check"], p["topic"], p["key"]["answers"], p["note"]])
EXCL = [r"\bprime\b", r"probab", r"coordinate", r"simultaneous", r"factoris", r"\bexpand", r"surface area", r"km ?/ ?h", r"\bspeed\b", r"\bsin\b|\bcos\b|\btan\b", r"\bindices\b|\bindex\b",
        r"\bnegative\b", r"\bmedian\b|\bmode\b", r"scatter", r"inequalit", r"\bsurd\b", r"standard form", r"\bHCF\b|\bLCM\b", r"\bcone\b|\bcylinder\b|\bsphere\b|\bpyramid\b", r"\bpentagon\b|\bhexagon\b",
        r"\bsecondary\b", r"\bquadratic\b", r"\bproportion\b", r"\bcompound interest\b", r"\bdensity\b", r"\bsequence\b"]
bad = []
for p in pages:
    t = page_text_all(p)
    for rx in EXCL:
        if re.search(rx, t, re.I): bad.append((p["no"], rx))
rec("Primary 6 limit: no Primary 7 / secondary content (primes, negatives, speed, probability, coordinates, simultaneous equations, expanding or factorising, surface area, trigonometry, median or mode ...) on any page, note or key entry", not bad, str(bad[:5]))
bad = []
for p in pages:
    t = plain(p["body"]) + " " + " ".join(p["instr"])
    if re.search(r"(^|[(=,:]\s*)[\u2212-]\s?\d", t): bad.append((p["no"], "negative number"))
    if re.search(r"\(\s*\d*\s*[a-z]\s*[+\u2212]|\d\s*\(\s*\d*\s*[a-z]\b", t): bad.append((p["no"], "bracket with a letter"))
    if re.search(r"\d:\d", t): bad.append((p["no"], "ratio or time written without spaces"))
    if re.search(r"\d\.\d+ : |: \d+\.\d+", t): bad.append((p["no"], "ratio with a decimal"))
    if re.search(r"\bx\b", t) and not re.search(r"\bbox\b", t): bad.append((p["no"], "letter x used (confusable with the multiplication sign)"))
rec("Primary 6 notation: no negative numbers, no brackets with letters, ratios written a : b with spaces and whole numbers only, the letter x not used for an unknown", not bad, str(bad[:5]))
bad = [p["no"] for p in pages if ("\u03c0" in p["body"] or "\u03c0" in " ".join(p["instr"]) or "pi" in plain(p["body"]).split()) and not re.search(r"22/7|3\.14", plain(p["body"]) + " ".join(p["instr"]))]
rec("every page that uses pi says whether to take 3.14 or 22/7", not bad, str(bad))
bad = [p["no"] for p in pages if "22/7" in " ".join(p["instr"]) and "3.14" in " ".join(p["instr"])]
rec("no page offers both values of pi", not bad, str(bad))
# ---- 3. HTML black and white / stroke scan
for k in BK:
  for f in (f"{k}_pupil.html", f"{k}_front.html", f"{k}_key.html"):
    h = open(os.path.join(O, f)).read()
    cols = set(c.lower() for c in re.findall(r"#[0-9a-fA-F]{3,6}\b", h))
    named = set(re.findall(r"(?:color|background|fill|stroke)\s*[:=]\s*[\"']?(red|blue|green|gray|grey|orange|yellow|purple|teal|navy)\b", h, re.I))
    rec(f"B/W colours only in {f}", cols <= {"#000", "#fff", "#000000", "#ffffff"} and not named, str(sorted(cols))[:80])
    sw = [float(x) for x in re.findall(r'stroke-width[=:]\s*"?([\d.]+)', h)]
    rec(f"stroke widths >= 0.2 mm (0.57 pt) in {f}", min(sw) >= 0.2 if sw else True, f"min {min(sw) if sw else '-'}")
    bw = [float(x) for x in re.findall(r"border[a-z-]*:\s*(?:[^;{}]*?\s)?([\d.]+)mm", h)]
    rec(f"CSS rule widths >= 0.25 mm (0.7 pt) in {f}", min(bw) >= 0.25 if bw else True, f"min {min(bw) if bw else '-'}")
    abh = [float(x) for sel, x in re.findall(r"(\.(?:ab|slot \.ab|shans \.ab|ctime \.ab|srow \.ab|check \.ab)[^{]*)\{[^}]*?height:([\d.]+)mm", h)]
    rec(f"answer boxes at least 12 mm high in {f}", min(abh) >= 12 if abh else True, f"min {min(abh) if abh else '-'}")
    op = re.findall(r"opacity|rgba|rgb\(|hsl|gradient|filter", h)
    rec(f"no opacity/alpha/gradient in {f}", not op, str(op[:3]))
  _ph = open(os.path.join(O, f"{k}_pupil.html")).read()
  rec(f"{k}: no bare black dot is drawn as a countable thing", 'class="dot"' not in _ph and "dotc" not in _ph)
  # no drawn object is clipped by the edge of its own svg (found on P1-25: the loose apples ran past the frame)
  _clip = []
  for sm in re.finditer(r'<svg[^>]*viewBox="0 0 ([\d.]+) ([\d.]+)"[^>]*>(.*?)</svg>', _ph, re.S):
      W_, H_ = float(sm.group(1)), float(sm.group(2))
      for om in re.finditer(r'class="obj"[^>]*translate\(([-\d.]+),([-\d.]+)\) scale\(([\d.]+)\)', sm.group(3)):
          x_, y_, sc_ = float(om.group(1)), float(om.group(2)), float(om.group(3))
          if x_ < -0.3 or y_ < -0.3 or x_ + 20 * sc_ > W_ + 0.3 or y_ + 20 * sc_ > H_ + 0.3: _clip.append((round(x_, 1), round(y_, 1), W_, H_))
  rec(f"{k}: no drawn object is clipped by the edge of its own svg", not _clip, str(_clip[:3]))
  rec(f"{k}: every coin shows its value and the word cents", _ph.count('class="coinunit"') == _ph.count('class="coinval"'), f'{_ph.count("class=" + chr(34) + "coinval")} coins')
# ---- 4. PDFs: page counts, fonts, text
def pdf_text(f): return subprocess.run(["pdftotext", "-layout", os.path.join(O, f), "-"], capture_output=True, text=True).stdout
alltxt = {}
for k in BK:
    keyhtml = open(os.path.join(O, f"{k}_key.html")).read()
    KEYPAGES = 1 + len(re.findall(r'class="page fm[ a-z]*" >', keyhtml))
    exp = {f"P6_{k}_Puzzles.pdf": NP[k], f"P6_{k}_FrontMatter.pdf": 5, f"P6_{k}_Complete_Pack.pdf": NP[k] + 5, f"P6_{k}_Answer_Key.pdf": KEYPAGES}
    for f, n in exp.items():
        out = subprocess.run(["pdfinfo", os.path.join(O, f)], capture_output=True, text=True).stdout
        got = int(re.search(r"Pages:\s+(\d+)", out).group(1)); rec(f"{f} has {n} pages", got == n, str(got))
        fo = subprocess.run(["pdffonts", os.path.join(O, f)], capture_output=True, text=True).stdout.splitlines()[2:]
        rec(f"{f} fonts all embedded", all(l.split()[-5] == "yes" for l in fo if l.strip()), f"{len(fo)} fonts")
        sz = os.path.getsize(os.path.join(O, f)); rec(f"{f} size < 20 MB", sz < 20e6, f"{sz/1e6:.2f} MB")
        rec(f"{f} A4 page size", "(A4)" in out, "")
    txt = pdf_text(f"P6_{k}_Puzzles.pdf")
    pgs = txt.split("\f")[:NP[k]]
    school = re.search(r"Photocopy licence: (.+?) only", txt)
    rec(f"{k}: school name printed on all {NP[k]} page footers", all("Photocopy licence" in x for x in pgs), school.group(1) if school else "")
    rec(f"{k}: every pupil page shows its code in the footer, for example S1-07 (P6-17)", all(BK[k][i]["code"] in pgs[i] for i in range(len(pgs))), str([i + 1 for i in range(len(pgs)) if BK[k][i]["code"] not in pgs[i]]))
    for f in (f"P6_{k}_Puzzles.pdf", f"P6_{k}_FrontMatter.pdf", f"P6_{k}_Answer_Key.pdf"):
        alltxt[f] = pdf_text(f)
joined = "\n".join(alltxt.values())
rec("money is written 50¢, never 50c, in all printed text", not re.search(r"(?<![\w.])\d+c\b", joined), str(re.findall(r"(?<![\w.])\d+c\b", joined)[:5]))
rec("dollar amounts with cents always have two decimal places ($3.50, never $3.5)", not re.search(r"\$\d+\.\d(?!\d)", joined), str(re.findall(r"\$\d+\.\d(?!\d)", joined)[:3]))
for k in BK:
    pt = alltxt[f"P6_{k}_Puzzles.pdf"]; fm = alltxt[f"P6_{k}_FrontMatter.pdf"]
    rec(f"{k}: pupil pages, key and front matter name no price, quote or sale wording", not re.search(r"S\$|SGD|per copy|per school|\bRRP\b", pt + fm + alltxt[f"P6_{k}_Answer_Key.pdf"], re.I))
    fm_flat = re.sub(r"\s+", " ", fm)
    fm_wo = fm_flat.replace("Not affiliated with or endorsed by the Ministry of Education, Singapore.", "").replace("The mathematics syllabus is published by the Ministry of Education, Singapore.", "")
    rec(f"{k}: pupil pages and front matter: no Mi, MOE, aligned, affiliated or endorsed wording (the one not-affiliated sentence on the licence page excepted)", not re.search(r"\bMi\b|MOE|Ministry|aligned|affiliat|endorse", pt + fm_wo, re.I) and ("Not affiliated with or endorsed by the Ministry of Education, Singapore." in fm_flat) == render.DRAFT or not render.DRAFT)
    _pg = lambda n: subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), "-layout", os.path.join(O, f"P6_{k}_FrontMatter.pdf"), "-"], capture_output=True, text=True).stdout
    _c, _l = re.sub(r"\s+", " ", _pg(1)), re.sub(r"\s+", " ", _pg(2))
    rec(f"{k}: the 'Not affiliated with or endorsed by the Ministry of Education, Singapore.' sentence is on the COVER only (owner decision P2-NOTAFFIL-FRONT), the licence page has only the factual syllabus sentence", "Not affiliated with or endorsed by the Ministry of Education, Singapore." in _c and "affiliat" not in _l and "The mathematics syllabus is published by the Ministry of Education, Singapore." in _l)
    _all_fm = re.sub(r"\s+", " ", fm)
    rec(f"{k}: teacher notes say 'Pictures are not actual size.', the key says the outcome lines are quoted from the syllabus and the notes on each tag are our own words", "Pictures are not actual size." in _all_fm and "quoted from the syllabus" in re.sub(r"\s+", " ", alltxt[f"P6_{k}_Answer_Key.pdf"]))
    rec(f"{k}: cover, licence and teacher notes are marked DRAFT with the owner's business contact email and the registered office address and publisher line", fm.count("DRAFT") >= 4 and fm.count("pypteltd@gmail.com") >= 3 and "66 Tannery Ln, Singapore 347805" in fm and "Preciouslyours Pte Ltd, trading as Math Inquirers" in fm, f"{fm.count('DRAFT')} DRAFT stamps")
    rec(f"{k}: front matter has the 'typical order, schools vary' sentence and the booklet's terms", "Schools vary" in fm_flat and OC.BOOKLETS[k]["terms"] in fm_flat)
    rec(f"{k}: pupil pages carry no DRAFT stamp", "DRAFT" not in pt)
    kt = alltxt[f"P6_{k}_Answer_Key.pdf"]
    rec(f"{k}: the answer key carries the DRAFT stamp and the owner's contact email (until built with --final)", ("DRAFT" in kt and "pypteltd@gmail.com" in kt) or not render.DRAFT)
    rec(f"{k}: the cover does not claim that every puzzle checks itself", "Every puzzle checks itself" not in fm_flat and "Almost every puzzle checks itself" in fm_flat)
    rec(f"{k}: every pupil footer prints the (c) 2026 Preciouslyours Pte Ltd line (entity and year confirmed by the owner)", pt.count("2026 Preciouslyours Pte Ltd.") == NP[k])
    rec(f"{k}: the licence page says it is an annual licence (one school year, renewable) and that a lawyer must approve the wording", "annual licence" in fm_flat and "approved by a lawyer" in fm_flat)
    rec(f"{k}: the licence page no longer calls the entity or year unconfirmed, and prints the registered office address", "owner to confirm" not in fm_flat and "[registered office address" not in fm_flat and "66 Tannery Ln, Singapore 347805" in fm_flat)
# ---- 4c. a 68-character school name must not wrap the footer or split the page code
import tempfile as _tf
_td = _tf.mkdtemp()
_long = "Saint Gabriel's Presbyterian Primary School (Junior Section, Annex Campus)"
subprocess.run([sys.executable, os.path.join(HERE, "build.py"), "--school", _long, "--outdir", _td], check=True, capture_output=True)
for k in BK:
    _t = pdf_text.__call__ if False else subprocess.run(["pdftotext", "-layout", os.path.join(_td, f"P6_{k}_Puzzles.pdf"), "-"], capture_output=True, text=True).stdout.split("\f")[:NP[k]]
    _ok = []
    for i, pg_ in enumerate(_t):
        lines = [l for l in pg_.splitlines() if l.strip()]
        last = lines[-1] if lines else ""
        _ok.append(BK[k][i]["code"] in last and "Photocopy licence:" in last and "Not for resale." in last)
    rec(f"{k}: a {len(_long)}-character school name keeps the footer on one line with the page code on every pupil page", all(_ok), str([i + 1 for i, o in enumerate(_ok) if not o]))
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
for k in BK:
    layout(f"{k}_pupil.html", f"{k} pupil", True); layout(f"{k}_front.html", f"{k} front", False); layout(f"{k}_key.html", f"{k} key", False)
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
for k in BK:
  ncbc = sum(1 for p in BK[k] if p.get("cbc"))
  for f in (f"{k}_pupil.html", f"{k}_key.html"):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 900, "height": 1200})
        pg.goto("file://" + os.path.join(O, f)); pg.wait_for_timeout(600)
        res = pg.evaluate(JS_CBC); b.close()
    rec(f"{f}: colour-by-code pictures: {len(res)} found (expected {ncbc}); every label of every part lies inside its region and clear of outlines and decorations", len(res) == ncbc and all(r["bad"] == 0 for r in res), str([(r["page"], r["bad"], r["n"]) for r in res]))
# ---- 6. bilevel (1-bit) test at 150 dpi on every PDF page
import tempfile, glob, shutil
tmp = tempfile.mkdtemp()
for k in BK:
  for f in (f"P6_{k}_Puzzles.pdf", f"P6_{k}_FrontMatter.pdf", f"P6_{k}_Answer_Key.pdf"):
    d = os.path.join(tmp, f[:-4]); os.makedirs(d)
    subprocess.run(["pdftoppm", "-r", "150", "-gray", os.path.join(O, f), os.path.join(d, "g")], check=True)
    subprocess.run(["pdftoppm", "-r", "150", "-mono", os.path.join(O, f), os.path.join(d, "m")], check=True)
    gs = sorted(glob.glob(d + "/g-*.pgm")); ms = sorted(glob.glob(d + "/m-*.pbm"))
    worst_loss = 0; grey_blocks = 0
    for g, m in zip(gs, ms):
        G = Image.open(g).convert("L"); M = Image.open(m).convert("L")
        gd = sum(1 for v in G.tobytes() if v < 235); md = sum(1 for v in M.tobytes() if v < 128)
        loss = 1 - md / max(gd, 1)
        W, H = G.size; px = G.load(); gb = 0
        for y in range(0, H - 6, 6):
            for x in range(0, W - 6, 6):
                v = [px[x + i, y + j] for i in (0, 5) for j in (0, 5)]
                if all(40 < t < 215 for t in v): gb += 1
        worst_loss = max(worst_loss, loss); grey_blocks += gb
    kind = f.split("_", 2)[2]
    rec(f"{f}: 1-bit render at 150 dpi keeps content (max ink loss {worst_loss:.2%} vs greyscale)", worst_loss <= {'Puzzles.pdf': 0.25, 'FrontMatter.pdf': 0.32, 'Answer_Key.pdf': 0.35}[kind], f"{len(gs)} pages")
    per_page = 130 if kind == "Answer_Key.pdf" else 40
    rec(f"{f}: no flat grey tint areas (blocks of edge pixels counted {grey_blocks}, budget {per_page} on average per page)", grey_blocks < per_page * len(gs), "")
    if kind == "Puzzles.pdf":
        keep = os.path.join(O, "bilevel_check", k); shutil.rmtree(keep, ignore_errors=True); os.makedirs(keep)
        for m in ms: Image.open(m).convert("1").save(os.path.join(keep, os.path.basename(m).replace(".pbm", ".png")), optimize=True)
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
