"""Colour-by-code pages (P1-01, P1-12, P1-14): the pupil works out a small answer in every part of an outline picture,
finds the answer in the key and colours the part with their own crayon. Pictures, topic banks and the question layout come from
school/colour_by_code, copied unchanged from commit ebff080 into ../cbc_vendor so that later changes there cannot alter this pack. Printed black and white; the check is the tally of colours."""
import os, sys, html
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
CBC = os.path.normpath(os.path.join(HERE, "..", "cbc_vendor"))
if CBC not in sys.path: sys.path.append(CBC)          # appended: p1's own build/render/validate names win
import sheet as S                                      # noqa: E402  (colour_by_code/sheet.py)
import layout as L                                     # noqa: E402
from .common import Page

COLOURS = S.COLOURS

def region_checks(sh):
    """the page's own checks as a function of the answers (list of values in picture region order)"""
    pic, key = sh["pic"], sh["key"]
    ids = [r.id for r in pic.regions]
    truth = [sh["items"][i]["answer"] for i in ids]
    base = Counter(key.index(v) for v in truth)
    pairs = list(pic.mirror_pairs); groups = [g[0] for g in pic.groups]
    subs = [(s[2], s[3], s[4]) for s in sh["checks"] if s[0] == "subset"]
    pos = {i: k for k, i in enumerate(ids)}
    def chk(ans):
        if any(a not in key for a in ans): return False                 # no crayon colour for this answer: seen at once
        col = {i: key.index(ans[pos[i]]) for i in ids}
        if Counter(col.values()) != base: return False                   # tally
        if any(col[l] != col[r] for l, r in pairs): return False
        if any(len({col[i] for i in g}) != 1 for g in groups): return False
        if any(sum(col[i] == k for i in ids_) != c for ids_, k, c in subs): return False
        return True
    return ids, truth, chk

def thumb(sh):
    """small solved picture for the teacher key: one letter (Y R B G O) in every part"""
    from geom import path_d
    pic = sh["pic"]; parts = []
    for r in pic.regions:
        parts.append(f'<path d="{path_d(r.geom)}" fill="#fff" stroke="#000" stroke-width="1.1" fill-rule="evenodd"/>')
    for svgf, _ in pic.decor: parts.append(svgf)
    for r in pic.regions:
        p = r.geom.representative_point()
        parts.append(f'<text x="{p.x:.1f}" y="{p.y:.1f}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="700" font-size="11" fill="#000">{COLOURS[sh["idx"][r.id]][0].upper()}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-0.5 -0.5 181 201" style="width:42mm;height:auto">{"".join(parts)}</svg>'

def teacher_svg(sh):
    from geom import path_d
    pic, spec = sh["pic"], sh["spec"]; parts = []
    for r in pic.regions:
        parts.append(f'<path class="r" d="{path_d(r.geom)}"/>')
    for svgf, _ in pic.decor: parts.append(svgf)
    for r in pic.regions:
        it = sh["items"][r.id]; parts.append(f'<g>{L.render(it["tcontent"], it["tplace"])}</g>')
    return f'<svg class="pic" xmlns="http://www.w3.org/2000/svg" viewBox="-0.5 -0.5 181 201">{"".join(parts)}</svg>'

def cbc_page(no, spec, title, instr, strand, syll, topic_note, extra_note, school_free=True):
    sh = S.make_sheet(spec, "")
    pic, bank, tier = sh["pic"], sh["bank"], sh["tier"]
    parts = [f'<path class="r" d="{__import__("geom").path_d(r.geom)}"/>' for r in pic.regions]
    for svgf, _ in pic.decor: parts.append(svgf)
    for r in pic.regions:
        it = sh["items"][r.id]; parts.append(f'<g>{L.render(it["content"], it["place"])}</g>')
    svg = f'<svg class="pic" xmlns="http://www.w3.org/2000/svg" viewBox="-0.5 -0.5 181 201">{"".join(parts)}</svg>'
    keyrow = '<div class="cbckey">' + "".join(f'<div class="k"><b>{html.escape(tier.disp(v))}</b><i>{COLOURS[i]}</i></div>' for i, v in enumerate(sh["key"])) + "</div>"
    checks = [c[1].replace("These must be one colour each: ", "One colour each: ").replace("..", ".").replace("the top and bottom of the tree top", "both tree top parts") for c in sh["checks"]]
    ids, truth, chk = region_checks(sh)
    tally = sh["tally"]
    P = Page(no=no, title=title, tier=spec["tier"], topic=bank.topic_for(spec["tier"]), strand=strand, syll=syll,
             ptype="Colour by code (pupils colour with their own crayons)", mech="K1 colour key + K3 tally of colours (+ matching parts)",
             mech_plain="Colour key and tally: every answer must be on the key, and the number of parts of each colour must match the box",
             instr=instr, body=keyrow + svg, check=" ".join(checks), check_lines=checks, check_boxes=None,
             key=dict(answers="Colour key: " + ", ".join(f"{tier.disp(v)} = {COLOURS[i]}" for i, v in enumerate(sh["key"])),
                      check_result="Tally: " + ", ".join(f"{c} {n}" for c, n in tally.items()) + "." + "".join(" " + c for c in checks[1:])),
             note=topic_note + " " + extra_note, seed=spec["seed"], cbc=True, sheet_id=spec["id"])
    P["mini"] = f'<div>{thumb(sh)}</div>'
    P["teacher_svg"] = teacher_svg(sh)
    P["facts"] = " ".join(str(v) for v in tier.domain)
    # ---- verification (independent of the sheet builder where possible)
    wrong = [(r.id, it["q"].lines) for r in pic.regions for it in [sh["items"][r.id]] if [v for v in tier.domain if it["q"].holds(v)] != [it["answer"]]]
    P.v("V1 every question has exactly one answer in the bank's domain", not wrong, str(wrong[:2]))
    P.v("V1b every answer is one of the five key values", all(a in sh["key"] for a in truth))
    P.v("V1c all five colours used at least twice", min(tally.values()) >= 2, str(tally))
    P.v("V2 the right answers pass every check (tally, matching parts)", chk(list(truth)))
    P.v("V2b questions are not repeated", sh["dups"] == 0, sh["dups"])
    P.v("V7 regions 12 to 18, every label found a box", 12 <= len(pic.regions) <= 18, len(pic.regions))
    dom = list(tier.domain)
    tot = det = 0
    for i, t in enumerate(truth):
        for v in dom:
            if v == t: continue
            a = list(truth); a[i] = v; tot += 1; det += (not chk(a))
    P.v("V3 wrong answers rejected by the page's checks (>=95%)", det / tot >= .95, f"{det}/{tot}")
    P["cv"] = dict(rate=det / tot, single_total=tot, single_detected=det)
    P["model"] = dict(truth=truth, domains=[dom] * len(truth), check=chk, numeric=True)
    P["sheet"] = sh
    return P

def page01():
    return cbc_page(1, dict(id="CBC-11", picture="rocket", bank="place", tier=1, seed=201), "Colour the Rocket",
        ["Find the missing number in each part.", "Find it in the key.", "Colour the part with that colour."],
        "Number and Algebra - Whole Numbers", "1.1 to 1.3 (count a set, tens and ones)",
        "Every part asks a tens-and-ones question, such as how many ones in 25 or 50 + [ ] = 54. The answers are 1 to 5.",
        "Pupils colour the black-and-white outline with their own crayons. Check strip: count the parts of each colour; the two sides of the rocket match.")

def page12():
    return cbc_page(12, dict(id="CBC-10", picture="house", bank="shapes", tier=1, seed=114), "Colour the House",
        ["Count the corners in each part.", "Find the number in the key.", "Colour the part with that colour."],
        "Measurement and Geometry - Geometry", "Geometry 1.1 (identify, name, describe 2D shapes: triangle, square, rectangle, circle)",
        "Shapes are triangle, square, rectangle and circle only. A circle has no corners.",
        "Pupils colour the black-and-white outline with their own crayons. Check strip: count the parts of each colour; the windows and the roof sides match.")

def page14():
    return cbc_page(14, dict(id="CBC-05", picture="icecream", bank="count", tier=2, seed=105), "Colour the Ice Cream",
        ["Find the missing number in each pattern.", "Find it in the key.", "Colour the part with that colour."],
        "Number and Algebra - Whole Numbers", "1.6 (number patterns); counting in 2s, 5s and 10s leads to multiplication",
        "Patterns count in 2s, 5s or 10s, forwards or back, and the answers are 60 to 80.",
        "Pupils colour the black-and-white outline with their own crayons. Check strip: count the parts of each colour; the two sides match.")

PAGES = [page01, page12, page14]
