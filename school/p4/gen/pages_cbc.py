"""Colour-by-code pages (P4-05, P4-11, P4-40): the pupil works out a small answer in every part of an outline picture,
finds the answer in the key and colours the part with their own crayon. Pictures, topic banks and the question layout come from
school/colour_by_code, copied from commit ebff080 into ../cbc_vendor so that later changes there cannot alter this pack; the Primary 4 banks (banks_p4.py) and rules (textcheck.py) were added in the copy. Printed black and white; the check is the tally of colours."""
import os, sys, html
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
CBC = os.path.normpath(os.path.join(HERE, "..", "cbc_vendor"))
if CBC not in sys.path: sys.path.append(CBC)          # appended: p1's own build/render/validate names win
import sheet as S                                      # noqa: E402  (colour_by_code/sheet.py)
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
    L.BOX_SIDE = 9.0                       # larger answer boxes (audit M4 and round 2: three-digit answers)
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
    P.v("V1a the independent evaluator (textcheck) re-solves all %d printed questions from their text and picture and gets the coloured answer" % len(sh["items"]), not ev_bad, str(ev_bad[:2]))
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

def page05():
    return cbc_page(5, dict(id="CBC-P4-01", picture="elephant", bank="numbers4", tier=2, seed=401, level=4), "Colour the Elephant",
        ["Work out the answer in each part.", "Find it in the key.", "Colour the part. No crayon? Write Y, R, B, G or O."],
        "Number and Algebra - Whole Numbers", "1.1, 1.2, 1.3, 1.4, 1.5 (place value, numbers in words, comparing, patterns and rounding; numbers up to 100 000)",
        "Every part asks a question about numbers up to 100 000: the value of a digit, a number in words, 10, 100, 1000 or 10 000 more or less, the greatest or smallest of three close numbers, a number pattern or rounding to the nearest 10, 100 or 1000.",
        oc=["NU1.1", "NU1.2", "NU1.3", "NU1.4", "NU1.5"])

def page11():
    return cbc_page(11, dict(id="CBC-P4-02", picture="castle", bank="mult4", tier=2, seed=402, level=4), "Colour the Castle",
        ["Work out the answer in each part.", "Find it in the key.", "Colour the part. No crayon? Write Y, R, B, G or O."],
        "Number and Algebra - Whole Numbers", "3.1, 3.2 (multiplication algorithm up to 4 digits by 1 digit and 3 digits by 2 digits; division algorithm up to 4 digits by 1 digit)",
        "Every part asks a multiplication or division with larger numbers: 4 digits by 1 digit, 3 digits by 2 digits, a missing factor, a division of a 4-digit number by a 1-digit number, a short story or a multiplication followed by a subtraction.",
        oc=["FO3.1", "FO3.2"])

def page40():
    return cbc_page(40, dict(id="CBC-P4-03", picture="sailboat", bank="dec4", tier=2, seed=403, level=4), "Colour the Sailboat",
        ["Work out the answer in each part.", "Find it in the key.", "Colour the part. No crayon? Write Y, R, B, G or O."],
        "Number and Algebra - Decimals", "1.2, 1.4, 1.5, 2.1, 3.1, 3.2 (comparing decimals, fractions as decimals, rounding, adding and subtracting, multiplying and dividing decimals)",
        "Every part works with decimals up to 2 decimal places: adding or subtracting, multiplying or dividing by a 1-digit number, a whole number divided by a whole number, rounding to a whole number, 1 or 2 decimal places, a fraction written as a decimal, the greatest of three decimals or 0.1 or 0.01 more or less.",
        oc=["DP1.2", "DP1.4", "DP1.5", "DA2.1", "DM3.1", "DM3.2"])

PAGES = [page05, page11, page40]
