"""Colour-by-code pages (P6-09, P6-32, P6-40): the pupil works out a small answer in every part of an outline picture, finds the answer in the key and colours the
part with their own crayon. Pictures, the question layout and the checks come from school/colour_by_code, copied unchanged from commit ebff080 into ../cbc_vendor
(the Primary 6 topic banks banks_p6.py and the Primary 6 rules in textcheck.py were added to the COPY only: the shared library is not changed).
Printed black and white; the check is the tally of colours."""
import os, sys, html
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
CBC = os.path.normpath(os.path.join(HERE, "..", "cbc_vendor"))
if CBC not in sys.path: sys.path.append(CBC)          # appended: this pack's own names win
import sheet as S                                      # noqa: E402  (cbc_vendor/sheet.py)
import textcheck as TC                                 # noqa: E402  (the library's independent evaluator)
import layout as L                                     # noqa: E402
from .common import Page

COLOURS = S.COLOURS

def region_checks(sh):
    """the page's own checks as a function of the answers (list of values in picture region order): the library's `flags`
    (tally, matching left-right parts, matching small marks); an answer that is not in the key has no crayon colour and is seen at once"""
    pic, key = sh["pic"], sh["key"]
    ids = [r.id for r in pic.regions]
    truth = [sh["items"][i]["answer"] for i in ids]
    def chk(ans):
        if any(a not in key for a in ans): return False
        return not S.flags(sh, {i: key.index(a) for i, a in zip(ids, ans)})
    return ids, truth, chk

def slip_enumeration(sh, ids, truth, chk):
    """single slips (every wrong value in every region), double slips (every pair of regions, every pair of wrong colours) and swaps
    (two regions exchange colours): counts of cases and of cases the page's checks reject"""
    key, dom = sh["key"], list(sh["tier"].domain)
    single = [0, 0]
    for i, t in enumerate(truth):
        for v in dom:
            if v == t: continue
            a = list(truth); a[i] = v; single[1] += 1; single[0] += (not chk(a))
    double = [0, 0]; swap = [0, 0]
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            for vi in key:
                if vi == truth[i]: continue
                for vj in key:
                    if vj == truth[j]: continue
                    a = list(truth); a[i] = vi; a[j] = vj
                    r = not chk(a); double[1] += 1; double[0] += r
                    if vi == truth[j] and vj == truth[i]: swap[1] += 1; swap[0] += r
    return single, double, swap

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
        parts.append(f'<path class="r" data-r="{r.id}" d="{path_d(r.geom)}"/>')
    for svgf, _ in pic.decor: parts.append(svgf)
    for r in pic.regions:
        it = sh["items"][r.id]; parts.append(f'<g class="lab" data-r="{r.id}">{L.render(it["tcontent"], it["tplace"])}</g>')
    return f'<svg class="pic" xmlns="http://www.w3.org/2000/svg" viewBox="-0.5 -0.5 181 201">{"".join(parts)}</svg>'

def mirror_truth(pic):
    """parts that sit in mirror-image places but are NOT a declared mirror pair (the printed 'left and right' rule would be false for them)"""
    from shapely import affinity
    regs = {r.id: r for r in pic.regions}; pairs = {frozenset(p) for p in pic.mirror_pairs}; bad = []
    ids = [r.id for r in pic.regions]
    for i, ai in enumerate(ids):
        m = affinity.scale(regs[ai].geom, xfact=-1, yfact=1, origin=(90, 0))
        for bj in ids[i + 1:]:
            inter = m.intersection(regs[bj].geom).area
            if inter > 0.9 * min(m.area, regs[bj].geom.area) and frozenset((ai, bj)) not in pairs: bad.append((ai, bj))
    return bad

def cbc_page(no, spec, title, instr, strand, syll, topic_note, oc=()):
    old = L.BOX_SIDE
    L.BOX_SIDE = 10.0                       # larger answer boxes (audit M4 and round 2: three-digit answers)
    try: return _cbc_page(no, spec, title, instr, strand, syll, topic_note, oc)
    finally: L.BOX_SIDE = old

def _cbc_page(no, spec, title, instr, strand, syll, topic_note, oc=()):
    sh = S.make_sheet(spec, "")
    pic, bank, tier = sh["pic"], sh["bank"], sh["tier"]
    parts = [f'<path class="r" data-r="{r.id}" d="{__import__("geom").path_d(r.geom)}"/>' for r in pic.regions]
    for svgf, _ in pic.decor: parts.append(svgf)
    for r in pic.regions:
        it = sh["items"][r.id]; parts.append(f'<g class="lab" data-r="{r.id}">{L.render(it["content"], it["place"])}</g>')
    svg = f'<svg class="pic" xmlns="http://www.w3.org/2000/svg" viewBox="-0.5 -0.5 181 201">{"".join(parts)}</svg>'
    keyrow = '<div class="cbckey">' + "".join(f'<div class="k"><b>{S.key_html(tier.disp(v))}</b><i>{COLOURS[i]}</i></div>' for i, v in enumerate(sh["key"])) + "</div>"
    checks = [c[1] for c in sh["checks"]]
    check_html = [S.check_html(c) for c in sh["checks"]]
    kinds = [c[0] for c in sh["checks"]]
    ids, truth, chk = region_checks(sh)
    tally = sh["tally"]
    match_note = ("the parts in the same place on the left and on the right match" if "mirror" in kinds else "") + (" and " if "mirror" in kinds and "twin" in kinds else "") + ("parts with the same small mark match" if "twin" in kinds else "")
    P = Page(no=no, title=title, tier=spec["tier"], topic=bank.topic_for(spec["tier"]), strand=strand, syll=syll,
             ptype="Colour by code (pupils colour with their own crayons)", mech="K1 colour key + K3 tally of colours (+ matching parts)",
             mech_plain="Colour key and tally: every answer must be on the key, the number of parts of each colour must match the box, and " + match_note,
             instr=instr, body=keyrow + svg, check=" ".join(checks), check_lines=checks, check_html_lines=check_html, check_boxes=None,
             key=dict(answers="Colour key: " + ", ".join(f"{tier.disp(v)} = {COLOURS[i]}" for i, v in enumerate(sh["key"])),
                      check_result="Tally: " + ", ".join(f"{c} {n}" for c, n in tally.items()) + "; " + match_note + "."),
             note=topic_note + " Pupils colour the black-and-white outline with their own crayons (or, for a pencil-only copy, write Y, R, B, G or O in each part: the tally and the matching parts can be checked the same way). Check strip: count the parts of each colour (the tally is printed); " + match_note + ".",
             seed=spec["seed"], cbc=True, sheet_id=spec["id"], oc=list(oc), mk=("cbc",))
    P["mini"] = f'<div>{thumb(sh)}</div>'
    P["teacher_svg"] = teacher_svg(sh)
    P["facts"] = " ".join(str(v) for v in tier.domain)
    # ---- verification (independent of the sheet builder where possible)
    wrong = [(r.id, it["q"].lines) for r in pic.regions for it in [sh["items"][r.id]] if [v for v in tier.domain if it["q"].holds(v)] != [it["answer"]]]
    P.v("V1 every question has exactly one answer in the bank's domain", not wrong, str(wrong[:2]))
    ev_bad = []
    for rid, it in sh["items"].items():
        q = it["q"]
        try:
            v_, rule_ = TC.solve(q.lines, q.art.meta if q.art is not None else None, tier.instr or bank.instr, tier.kind)
            if not TC.matches(v_, it["answer"]): ev_bad.append((rid, q.lines, v_, it["answer"]))
        except TC.Unparsed: ev_bad.append((rid, q.lines, "unparsed"))
    P.v("V1a the independent evaluator (textcheck) re-solves all %d printed questions from their text and gets the coloured answer" % len(sh["items"]), not ev_bad, str(ev_bad[:2]))
    P.v("V1b every answer is one of the five key values", all(a in sh["key"] for a in truth))
    P.v("V1c all five colours used at least twice", min(tally.values()) >= 2, str(tally))
    P.v("V2 the right answers pass every check (tally, matching parts)", chk(list(truth)))
    P.v("V2b questions are not repeated", sh["dups"] == 0, sh["dups"])
    P.v("V7 regions 12 to 18, every label found a box", 12 <= len(pic.regions) <= 18, len(pic.regions))
    P.v("V2c the printed left-right rule is true: no two parts sit in mirror-image places without being a declared pair", not mirror_truth(pic) if "mirror" in kinds else True, mirror_truth(pic))
    single, double, swap = slip_enumeration(sh, ids, truth, chk)
    P.v("V3 single wrong answers rejected by the page's checks (>=95%)", single[0] / single[1] >= .95, f"{single[0]}/{single[1]}")
    P.v("V3b double slips (every pair of regions, every pair of wrong colours) rejected (>=95%)", double[0] / double[1] >= .95, f"{double[0]}/{double[1]}")
    P.v("V3c swaps of two parts' colours rejected (>=95%)", swap[0] / swap[1] >= .95, f"{swap[0]}/{swap[1]}")
    P["cv"] = dict(rate=single[0] / single[1], single_total=single[1], single_detected=single[0], double=double, swap=swap)
    P["model"] = dict(truth=truth, domains=[list(tier.domain)] * len(truth), check=chk, numeric=True)
    P["sheet"] = sh
    return P

CINSTR = ["Work out the answer in each part.", "Find it in the key.", "Colour the part. No crayon? Write Y, R, B, G or O."]

def page09():
    return cbc_page(9, dict(id="CBC-P6-01", picture="car", bank="ratio", tier=2, seed=1, level=6), "Colour the Car", CINSTR,
        "Number and Algebra - Ratio and Percentage", "Ratio 1.2, 1.3, 1.6 and Percentage 1.1, 1.2 (equivalent ratios, sharing in a ratio, the missing term, finding the whole, percentage change)",
        "Every part asks a ratio or percentage question with a whole-number answer: a missing term in equal ratios, a share of a quantity shared in a ratio, a percentage of a number, the whole when a percentage of it is given, or the number before a percentage increase.",
        oc=["RA1.2", "RA1.3", "RA1.6", "PC1.1", "PC1.2"])

def page32():
    return cbc_page(32, dict(id="CBC-P6-02", picture="butterfly", bank="volavg", tier=2, seed=1, level=6), "Colour the Butterfly", CINSTR,
        "Measurement and Geometry - Area and Volume; Statistics", "Volume 2.1, 2.2, 2.3 and Statistics (volume of a cuboid or cube, the missing height or edge, average, total and number)",
        "Every part asks about the volume of a cuboid or cube (the volume from the edges, the height from the volume and the base area, a cube's edge or volume) or about an average (from a list, from a total, or the total from an average). Volumes are in cm³.",
        oc=["VO2.1", "VO2.2", "VO2.3", "ST1.1", "ST1.2"])

def page40():
    return cbc_page(40, dict(id="CBC-P6-03", picture="elephant", bank="mixed", tier=2, seed=4, level=6), "Colour the Elephant", CINSTR,
        "Number and Algebra - mixed Primary 6", "Mixed: percentage of a number (Primary 6 Foundation Percentage 1.3), Fractions 1.2, Algebra 1.4 and 1.5, Ratio 1.3, Statistics 1.1",
        "Every part asks a mixed Primary 6 question with a whole-number answer: a percentage of a number, a whole number divided by a fraction, the value of an expression with a letter, an equation with a letter, a share in a ratio, or an average.",
        oc=["PF.PC", "FR1.2", "AL1.4", "AL1.5", "RA1.3", "ST1.1"])

PAGES = [page09, page32, page40]
