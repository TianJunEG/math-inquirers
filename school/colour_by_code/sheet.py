"""Make one worksheet: assign an answer to each region (keeping the picture's matching rules), make a question for every
region that fits its label box, and write the pupil and teacher pages as HTML."""
import html, math, os, random
from collections import Counter
import layout as L
from banks import get_bank, BOX
from pictures import PICTURES

COLOURS = ["yellow", "red", "blue", "green", "orange"]
HERE = os.path.dirname(os.path.abspath(__file__))

class BuildError(Exception): pass

def components(pic):
    parent = {r.id: r.id for r in pic.regions}
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for ids in [list(p) for p in pic.mirror_pairs] + [g[0] for g in pic.groups]:
        for i in ids[1:]: parent[find(i)] = find(ids[0])
    comp = {}
    for r in pic.regions: comp.setdefault(find(r.id), []).append(r.id)
    return list(comp.values())

def assign(pic, rng):
    """answer index 0..4 for every region: matching sets share one; every colour used 2 to 4 times; each counted subset
    has at least one and not all of some colour"""
    comps = components(pic); n = len(pic.regions)
    for _ in range(20000):
        idx = {}
        for c in comps:
            k = rng.randrange(5)
            for rid in c: idx[rid] = k
        cnt = Counter(idx.values())
        if len(cnt) < 5 or min(cnt.values()) < 2 or max(cnt.values()) > max(4, math.ceil(n / 5) + 1): continue
        if all(any(0 < sum(idx[i] == k for i in ids) < len(ids) for k in range(5)) for ids, _ in pic.subsets):
            return idx
    raise BuildError("no assignment")

def make_sheet(spec, school=""):
    pic = PICTURES[spec["picture"]]()
    level = spec.get("level", 1)
    bank = get_bank(level, spec["bank"]); tier = bank.tiers[spec["tier"]]
    rng = random.Random(spec["seed"])
    idx = assign(pic, rng)
    key = tier.key
    order = list(pic.regions); rng.shuffle(order)
    use = Counter(); seen = set(); items = {}; dups = 0
    for reg in order:
        a = key[idx[reg.id]]
        boxes = pic.boxes(reg.id)
        cen = reg.geom.centroid
        ref = (cen.x, cen.y) if reg.geom.contains(cen) else (lambda p: (p.x, p.y))(reg.geom.representative_point())
        cands = []
        for allow_dup in (False, True):
            forms = sorted(tier.forms, key=lambda f: (use[f.__name__], rng.random()))
            for form in forms:
                for attempt in range(6):
                    q = form(a, rng)
                    if q is None: break
                    sig = " / ".join(q.lines) + str(getattr(q.art, "meta", ""))
                    if sig in seen and not allow_dup: continue
                    content = L.Content(q.lines, q.art, q.layout)
                    p = L.fit(content, boxes, ref=ref)
                    if p is None: break
                    col = f"({COLOURS[idx[reg.id]]})"
                    ta = L.Content(q.sol + [col], q.art, q.layout)
                    tb = L.Content(q.sol[:-1] + [q.sol[-1] + " " + col], q.art, q.layout)
                    tc_ = L.Content([L.ANS_L + str(tier.disp(a)) + L.ANS_R + " " + col], q.art, "stack" if q.layout == "stack" else "row")
                    fa, fb = L.fit(ta, boxes, fmax=p["f"], fmin=L.F_MIN_TEACHER, ref=ref), L.fit(tb, boxes, fmax=p["f"], fmin=L.F_MIN_TEACHER, ref=ref)
                    opts = [(x["f"], k, x, c, False) for k, (x, c) in enumerate([(fa, ta), (fb, tb)]) if x]
                    if not opts:
                        fc = L.fit(tc_, boxes, fmax=p["f"], fmin=L.F_MIN_TEACHER, ref=ref)
                        if fc: opts = [(fc["f"], 2, fc, tc_, True)]
                    if not opts: break
                    _, _, tp, tc, short = max(opts, key=lambda o: (o[0], -o[1]))
                    cands.append((p["f"], -use[form.__name__], form, q, content, p, tc, tp, sig, short, sig in seen))
                    break
                if len(cands) >= 8 or (cands and max(c[0] for c in cands) >= 4.8 and len(cands) >= 3): break
            if cands: break
        if not cands: raise BuildError(f"{spec['id']}: no question fits region {reg.id} (boxes {boxes})")
        best = max(cands, key=lambda c: (c[0], c[1]))
        _, _, form, q, content, p, tc, tp, sig, short, dup = best
        use[form.__name__] += 1; seen.add(sig)
        items[reg.id] = dict(id=reg.id, answer=a, colour=COLOURS[idx[reg.id]], q=q, form=form.__name__, content=content, place=p, tcontent=tc, tplace=tp, teacher_short=short, dup=dup)
    tally = {COLOURS[k]: sum(1 for r in pic.regions if idx[r.id] == k) for k in range(5)}
    return dict(spec=spec, level=level, pic=pic, bank=bank, tier=tier, key=key, idx=idx, items=items, tally=tally, dups=sum(1 for i in items.values() if i['dup']), school=school, checks=check_sentences(pic, idx, tally))

def check_sentences(pic, idx, tally):
    out = [("tally", "Count the parts of each colour. You should have: " + ", ".join(f"{c} {n}" for c, n in tally.items()) + ".")]
    if pic.mirror_pairs: out.append(("mirror", f"The two sides of the {pic.title.lower()} match: parts that mirror each other have the same colour."))
    if pic.groups: out.append(("group", "These must be one colour each: " + "; ".join(g[1] for g in pic.groups) + "."))
    for ids, template in pic.subsets:
        best = None
        for k in range(5):
            c = sum(idx[i] == k for i in ids)
            if 0 < c < len(ids) and (best is None or abs(c - len(ids) / 3) < abs(best[1] - len(ids) / 3)): best = (k, c)
        k, c = best
        out.append(("subset", template.format(n=len(ids), c=c, colour=COLOURS[k], are="is" if c == 1 else "are"), ids, k, c))
    return out

# ----------------------------------------------------------------- html
def star_svg(n):
    pts = " ".join(f"{(10 if i % 2 == 0 else 4.2) * math.cos(-math.pi / 2 + i * math.pi / 5):.2f},{(10 if i % 2 == 0 else 4.2) * math.sin(-math.pi / 2 + i * math.pi / 5):.2f}" for i in range(10))
    one = f'<svg xmlns="http://www.w3.org/2000/svg" width="8mm" height="8mm" viewBox="-10 -10 20 20"><polygon fill="#000" stroke="#000" stroke-width="0.6" points="{pts}"/></svg>'
    return f'<span class="stars" title="{n} star">{one * n}</span>'

def css(font_rel):
    return f"""
@font-face{{font-family:'Fredoka';font-weight:600;src:url('{font_rel}/fredoka/files/fredoka-latin-600-normal.woff2') format('woff2')}}
@font-face{{font-family:'Fredoka';font-weight:700;src:url('{font_rel}/fredoka/files/fredoka-latin-700-normal.woff2') format('woff2')}}
@font-face{{font-family:'Nunito Sans';font-weight:400;src:url('{font_rel}/nunito-sans/files/nunito-sans-latin-400-normal.woff2') format('woff2')}}
@font-face{{font-family:'Nunito Sans';font-weight:800;src:url('{font_rel}/nunito-sans/files/nunito-sans-latin-800-normal.woff2') format('woff2')}}
@page{{size:A4;margin:0}}*{{box-sizing:border-box}}
html,body{{margin:0;background:#fff;color:#000;font-family:'Nunito Sans',Arial,sans-serif}}
.page{{width:210mm;height:297mm;padding:9mm 14.5mm 8mm;display:flex;flex-direction:column;overflow:hidden;page-break-after:always}}
header{{display:flex;align-items:center;gap:4mm;border-bottom:0.8mm solid #000;padding-bottom:1.5mm}}
h1{{font-family:'Fredoka';font-weight:600;font-size:23pt;margin:0;flex:1;line-height:1.05}}
.stars{{display:inline-flex;gap:1mm}}
.nm{{font-size:10.5pt;line-height:1.7;text-align:right;white-space:nowrap}}.nm span{{display:inline-block;border-bottom:0.4mm solid #000;width:38mm}}
.instr{{font-size:12pt;line-height:1.2;margin:2mm 0 1.6mm}}
.key{{display:flex;gap:2mm;justify-content:space-between;margin:0 0 1mm}}
.k{{flex:1;border:0.6mm solid #000;border-radius:2mm;padding:0.6mm 1.5mm;text-align:center;line-height:1.15}}
.k b{{display:block;font-family:'Fredoka';font-weight:700;font-size:13.5pt}}.k i{{display:block;font-style:normal;font-size:11pt;border-top:0.3mm solid #000;margin-top:0.4mm;padding-top:0.3mm}}
svg.pic{{display:block;margin:0 auto;width:181mm;height:auto}}
svg.pic .r{{fill:#fff;stroke:#000;stroke-width:0.9;stroke-linejoin:round;fill-rule:evenodd}}
svg.pic text{{font-family:'Fredoka';font-weight:600;dominant-baseline:central;fill:#000;text-anchor:start}}
svg.pic text.a{{font-weight:700}}
svg.pic .bx{{fill:#fff;stroke:#000;stroke-width:0.45}}
svg.pic .ul{{stroke:#000;stroke-width:0.4}}
.chk{{border:0.8mm solid #000;border-radius:3mm;padding:1.6mm 4mm;margin-top:1mm;font-size:10.5pt;line-height:1.28}}
.chk b{{font-family:'Fredoka';font-weight:600}}.chk div{{margin-top:0.2mm}}
footer{{margin-top:auto;display:flex;justify-content:space-between;font-size:8pt;padding-top:1mm;gap:6mm}}
"""

def page_html(sh, teacher=False):
    pic, bank, spec = sh["pic"], sh["bank"], sh["spec"]
    parts = []
    for r in pic.regions:
        parts.append(f'<path class="r" id="{spec["id"]}-{r.id}" data-r="{r.id}" d="{__import__("geom").path_d(r.geom)}"/>')
    for svgf, _ in pic.decor: parts.append(svgf)
    for r in pic.regions:
        it = sh["items"][r.id]
        if teacher: parts.append(f'<g class="lab" data-r="{r.id}">{L.render(it["tcontent"], it["tplace"])}</g>')
        else: parts.append(f'<g class="lab" data-r="{r.id}">{L.render(it["content"], it["place"])}</g>')
    svg = f'<svg class="pic" xmlns="http://www.w3.org/2000/svg" viewBox="-0.5 -0.5 181 201">{"".join(parts)}</svg>'
    keyhtml = "".join(f'<div class="k"><b>{html.escape(sh["tier"].disp(v))}</b><i>{COLOURS[i]}</i></div>' for i, v in enumerate(sh["key"]))
    chk = "".join(f"<div>{html.escape(c[1])}</div>" for c in sh["checks"])
    title = f'{pic.title} {bank.title}' + (" &ndash; Teacher Answers" if teacher else "")
    tsize = 23 if len(title) <= 22 else (19.5 if len(title) <= 30 else 17)
    instr = (sh["tier"].instr or bank.instr) if not teacher else "Teacher answers: each answer is filled in and the colour is shown in brackets. Pupils colour their own copy."
    school = html.escape(sh["school"]) if sh["school"] else "School name: ______________________________"
    stars = "1 star" if spec["tier"] == 1 else "2 stars"
    head_r = star_svg(spec["tier"]) + ('<div class="nm">Name <span></span><br>Class <span></span></div>' if not teacher else "")
    return (f'<div class="page" data-ws="{spec["id"]}"><header><h1 style="font-size:{tsize}pt">{title}</h1>{head_r}</header><p class="instr">{html.escape(instr)}</p>'
            f'<div class="key">{keyhtml}</div>{svg}<div class="chk"><b>Check your work.</b>{chk}</div>'
            f'<footer><span>{school}</span><span>{spec["id"]} &middot; Primary {sh["level"]} &middot; {html.escape(bank.topic_for(spec["tier"]))} &middot; {stars}</span></footer></div>')
