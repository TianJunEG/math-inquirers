#!/usr/bin/env python3
"""Lesson 10 extras: the Term 1 end-of-term check outputs.

Reads the block `end_of_term_check` of term/l1/lessons/l10.json and writes, into term/l1/out/l10/:
  L10_Check_Student.pdf      the 4-page private check sheet for the child (print at 100%)
  L10_Check_Tutor_Key.pdf    procedure to give and return it privately, answer key and marking, record sheet, progress words, parent report line templates
  L10_Check_Parent_Note.pdf  one page for grown-ups (print, take, photo, return)
  html/check_*.html          the same pages as HTML

Run AFTER the normal build:   bash term/l1/build.sh 10 && python3 term/l1/assets/l10_extras.py
It does not change any shared tool. The shared builder does not know about the check, so it is built here (lesson-specific).
Real-PDF checks done here: page count (4, 2+, 1), page fill, and the printed lengths on the sheet (the 10 cm bar and the 9 cm line)
are measured on the rendered PDF at 254 dpi and must be within 0.6 mm.
"""
import glob, html, json, math, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.dirname(HERE)
TOOLS = os.path.join(L1, 'tools')
sys.path.insert(0, TOOLS)
from common import font_css, mi_uri, E, NAVY, TEAL, YEL  # noqa: E402
import b_print  # noqa: E402  (WB_CSS and EXTRA: the workbook style)
import svg  # noqa: E402

SOFT = '#FFF0C2'
SKY = '#DDEBF7'


def load():
    with open(os.path.join(L1, 'lessons', 'l10.json'), encoding='utf-8') as f:
        return json.load(f)


# ------------------------------------------------------------------ small pictures for the sheet

def minus(s):
    """Show a hyphen between spaces as a proper minus sign."""
    return s.replace(' - ', ' − ')


def numberline_svg(v):
    lo, hi, arrow, labels = v['lo'], v['hi'], v['arrow'], v['labels']
    x0, x1 = 40, 660
    x = lambda n: x0 + (n - lo) * (x1 - x0) / (hi - lo)
    base = 100
    p = [f'<line x1="{x0 - 14}" y1="{base}" x2="{x1 + 14}" y2="{base}" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>']
    for n in range(lo, hi + 1):
        major = n in labels
        p.append(f'<line x1="{x(n):.1f}" y1="{base - (16 if major else 10)}" x2="{x(n):.1f}" y2="{base + (16 if major else 10)}" stroke="{NAVY}" stroke-width="{3.5 if major else 2.5}" data-tick="{n}"/>')
        if major:
            p.append(f'<text x="{x(n):.1f}" y="{base + 48}" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial, sans-serif">{n}</text>')
    ax = x(arrow)
    p.append(f'<polygon points="{ax:.1f},{base - 20} {ax - 15:.1f},{base - 56} {ax + 15:.1f},{base - 56}" fill="{YEL}" stroke="{NAVY}" stroke-width="3" data-arrow="{arrow}" data-tip-x="{ax:.1f}"/>')
    p.append(f'<line x1="{ax:.1f}" y1="{base - 56}" x2="{ax:.1f}" y2="{base - 84}" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>')
    return f'<svg viewBox="0 0 700 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="number line from {lo} to {hi} with an arrow" style="width:100%;height:auto;display:block" data-lo="{lo}" data-hi="{hi}" data-x0="{x0}" data-x1="{x1}">{"".join(p)}</svg>'


def cards_svg(digits):
    p = []
    for i, dgt in enumerate(digits):
        x = 8 + i * 150
        p.append(f'<rect x="{x}" y="8" width="120" height="160" rx="16" fill="#fff" stroke="{NAVY}" stroke-width="4" data-card="{dgt}"/>')
        p.append(f'<text x="{x + 60}" y="118" font-size="104" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial, sans-serif">{dgt}</text>')
    w = 8 + len(digits) * 150
    return f'<svg viewBox="0 0 {w} 176" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="digit cards {" and ".join(map(str, digits))}" style="width:100%;height:auto;display:block">{"".join(p)}</svg>'


def line_mm_svg(mm):
    """A printed line exactly `mm` millimetres long (end ticks included), in real units so the PDF prints it true to size."""
    return (f'<svg width="{mm}mm" height="9mm" viewBox="0 0 {mm} 9" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="a line to measure" data-mm="{mm}" style="display:block">'
            f'<line x1="0.4" y1="4.5" x2="{mm - 0.4}" y2="4.5" stroke="{NAVY}" stroke-width="1.1"/>'
            f'<line x1="0.4" y1="1" x2="0.4" y2="8" stroke="{NAVY}" stroke-width="0.8"/><line x1="{mm - 0.4}" y1="1" x2="{mm - 0.4}" y2="8" stroke="{NAVY}" stroke-width="0.8"/></svg>')


def check_bar_svg(mm):
    return (f'<svg width="{mm}mm" height="7mm" viewBox="0 0 {mm} 7" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="print check bar" data-mm="{mm}" style="display:block">'
            f'<line x1="0.4" y1="3.5" x2="{mm - 0.4}" y2="3.5" stroke="#555" stroke-width="0.9"/>'
            f'<line x1="0.4" y1="0.8" x2="0.4" y2="6.2" stroke="#555" stroke-width="0.8"/><line x1="{mm - 0.4}" y1="0.8" x2="{mm - 0.4}" y2="6.2" stroke="#555" stroke-width="0.8"/></svg>')


def dotbox_svg():
    return (f'<svg viewBox="0 0 700 90" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="space to draw a line, with a dot at the start" style="width:100%;height:auto;display:block;margin:4px 0">'
            f'<rect x="3" y="3" width="694" height="84" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-dasharray="12 8"/>'
            f'<circle cx="46" cy="45" r="8" fill="{NAVY}" data-dot="1"/></svg>')


# ------------------------------------------------------------------ the student sheet

SHEET_CSS = """
.cbx{display:inline-block;width:38px;height:38px;border:2.5px solid #1B2A49;border-radius:9px;background:#fff;vertical-align:middle;margin:0 6px}
.wl2{display:inline-block;width:64%;border-bottom:2px dashed #1B2A49;height:24px;vertical-align:baseline}
.crl{background:#fff;border:2.5px solid #1F7A6F;border-radius:14px;padding:6px 16px 8px;margin:6px 0 4px;font-size:16.5px;position:relative}
.crl b.t{font-family:Fredoka;color:#1F7A6F;font-size:18px}
.crl ul{margin:2px 0 0 18px;padding:0}.crl li{margin:1px 0;font-weight:600}
.opt{border:3px dashed #1F7A6F;border-radius:16px;background:#E8F5F2;padding:10px 14px 12px;margin:30px 4px 10px;position:relative}
.opt .tagx{position:absolute;left:14px;top:-17px;background:#1F7A6F;color:#fff;border-radius:999px;padding:3px 16px;font-weight:700;font-size:16px}
.sub2{display:flex;gap:8px;padding-left:2px;align-items:flex-end;margin-top:12px}.sub2>span:last-child{flex:1}.sub2>span:last-child .wl2{width:78%}
.chk{page-break-inside:avoid}
.foot{font-size:12px;color:#3B4A6B;margin-top:6px}
.vis2{margin:8px 0 4px 6px}
.csheet .p4 .sub2{margin-top:26px}.csheet .p4 .wl2{height:34px}.csheet .p4 .al{height:30px}.csheet .qbox{margin:28px 4px 14px 4px!important;padding:24px 16px 12px!important}
"""


def blanks2(text):
    t = E(minus(text))
    t = t.replace('___', '<span class="al"></span>').replace('[box]', '<span class="cbx"></span>').replace('[wide]', '<span class="wl2"></span>')
    return t


def visual_html(q):
    v = q.get('visual')
    if not v:
        return ''
    t = v['type']
    if t == 'bundles':
        return f'<div class="vis2" style="width:330px">{svg.bundles(v["tens"], v["ones"])}</div>'
    if t == 'numberline':
        return f'<div class="vis2" style="width:600px">{numberline_svg(v)}</div>'
    if t == 'digitcards':
        return f'<div class="vis2" style="width:230px">{cards_svg(v["digits"])}</div>'
    if t == 'tenframes':
        return f'<div class="vis2" style="width:430px">{svg.ten_frame(v["a"], v["b"])}</div>'
    return ''


def qbox2(q, num, d, extra_after=None):
    parts = ''
    for p in q['parts']:
        pre = ''
        if q['id'] == 'C9' and p['l'] == 'b':
            pre = f'<div class="vis2" style="margin:12px 0 4px 34px">{line_mm_svg(d["end_of_term_check"]["line_mm"])}</div>'
        post = dotbox_svg() if (q['id'] == 'C9' and p['l'] == 'a') else ''
        lab = f'<span class="sl">{E(p["l"])}</span>' if p['l'] else ''
        parts += f'{pre}<div class="sub2">{lab}<span>{blanks2(p["text"])}</span></div>{post}'
    return f'<div class="qbox chk"><div class="q"><span class="qn">{num}</span><span class="qt">{E(minus(q["text"]))}</span></div>{visual_html(q)}{'<div class="draw"></div>' if q['id'] == 'C10' else ''}{parts}</div>'


def sheet_header(d, page, total):
    return (f'<div class="lh"><span class="lbadge">Term {d["term"]} • Check</span><span class="ltopic">End-of-term check • Start here level</span>'
            f'<span style="margin-left:auto;background:#FFC93C;color:#1B2A49;border-radius:999px;padding:4px 16px;font-weight:700;font-size:15px">Page {page} of {total}</span></div>')


def sheet_html(d):
    c = d['end_of_term_check']
    qs = {q['id']: q for q in c['questions']}
    total = c['sheet_pages']
    by_page = {}
    for q in c['questions']:
        by_page.setdefault(q['page'], []).append(q)
    mi = f'<img alt="Mi the dolphin" src="{mi_uri()}" style="width:22mm;height:auto;flex:none;margin:-4px 0 -6px 10px">'
    rules = '<div class="crl"><b class="t">Before you start</b><ul>' + ''.join(f'<li>{E(r)}</li>' for r in c['child_rules']) + '</ul></div>'
    pages = []
    num = 0
    for pg in range(1, total + 1):
        body = sheet_header(d, pg, total)
        if pg == 1:
            body += (f'<div style="position:relative"><img alt="Mi the dolphin" src="{mi_uri()}" style="position:absolute;right:4px;top:-6px;width:24mm;height:auto">'
                     f'<div class="ltitle">TERM 1 CHECK</div><div class="namer" style="width:74%"><b>Name</b><span></span><b>Date</b><span style="max-width:110px"></span></div></div>{rules}')
        else:
            body += '<div class="namer"><b>Name</b><span></span></div>'
        for q in by_page.get(pg, []):
            num += 1
            body += qbox2(q, num, d)
        if pg == total:
            o = c['optional']
            body += (f'<div class="opt"><span class="tagx">Think harder (optional)</span><div class="q" style="margin-top:6px"><span class="qt">{E(o["text"].replace("Think harder (optional). ", ""))}</span></div>'
                     + ''.join(f'<div class="sub2"><span>{blanks2(p["text"])}</span></div>' for p in o['parts'])
                     + '<div class="draw"></div><div class="foot">You may skip this one. It is not marked.</div></div>')
            body += '<div style="text-align:center;font-family:Fredoka;font-size:22px;color:#1F7A6F;margin:18px 0 4px">Well done for trying your best!</div>'
        if pg == total:
            body += (f'<div class="foot" style="margin-top:14px"><b>Print check (for the grown-up):</b> this bar must measure exactly 10 cm. If it does not, print again at 100% (actual size).</div>'
                     f'<div style="margin:6px 0 0 4px">{check_bar_svg(c["sheet_check_bar_mm"])}</div>')
        pages.append(f'<div class="page p{pg}">{body}</div>')
    css = f'{font_css()}{b_print.WB_CSS}{b_print.EXTRA}{SHEET_CSS}'
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Term 1 end-of-term check</title><style>{css}</style></head><body class="csheet">{"".join(pages)}</body></html>'


# ------------------------------------------------------------------ the tutor key

KEY_CSS = """
@page{size:A4;margin:14mm 13mm 16mm 13mm}
*{box-sizing:border-box}
body{margin:0;font-family:'Nunito Sans',Arial,sans-serif;color:#1B2A49;font-size:12.2px;line-height:1.4;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2,h3{font-family:'Fredoka',Arial,sans-serif;font-weight:600;margin:0}
h1{font-size:32px;line-height:1.05}
h2{font-size:19px;color:#1F7A6F;border-bottom:3px solid #FFC93C;padding-bottom:3px;margin:16px 0 7px;break-after:avoid}
h3{font-size:14.5px;margin:10px 0 3px;break-after:avoid}
.pb{break-before:page}
.cover{background:#1B2A49;color:#FFF9EC;border-radius:16px;padding:20px 24px;margin-bottom:10px;position:relative}
.cover .k{color:#FFC93C;font-weight:800;letter-spacing:.14em;font-size:11px}
.cover h1{color:#fff;font-size:36px;margin:4px 0}
.cover p{margin:3px 120px 3px 0;font-size:13px}
table{border-collapse:collapse;width:100%;margin:5px 0;font-size:11.2px}
th{background:#FFC93C;text-align:left;padding:3px 6px;border:1px solid #1B2A49}
td{padding:3px 6px;border:1px solid #C9D4EC;vertical-align:top}
tr{break-inside:avoid}
.box{border:2px solid #1B2A49;border-radius:9px;padding:6px 11px;margin:7px 0;background:#FFFDF5;break-inside:avoid}
.box.t{border-color:#1F7A6F;background:#E8F5F2}
.box.r{border-color:#D64545;background:#FDF0F0}
ol,ul{margin:3px 0 3px 18px;padding:0}li{margin:2px 0}
.small{font-size:10.8px;color:#3B4A6B}
.ans{font-weight:800;color:#1F7A6F}
.tick{display:inline-block;width:15px;height:15px;border:2px solid #1B2A49;border-radius:4px;background:#fff;vertical-align:-3px;margin:0 3px 0 8px}
.rec td{height:30px;text-align:center}
.wl{border-bottom:1.5px dotted #8A94AD;height:20px}
.note{border:2px dashed #1F7A6F;border-radius:10px;padding:8px 12px;margin:8px 0;background:#fff}
.k1{break-inside:avoid}
"""


def band_word(score, n, c):
    """Progress word from a strand score (points) and the number of questions counted."""
    if n == 0:
        return None
    f = score / n
    if f >= c['bands']['showing_min']:
        return 'showing'
    if f >= c['bands']['getting_min']:
        return 'getting'
    return 'beginning'


def key_html(d):
    c = d['end_of_term_check']
    W = c['words']
    qs = c['questions']
    H = []
    H.append(f'<div class="cover"><img alt="Mi the dolphin" src="{mi_uri()}" style="position:absolute;right:18px;top:12px;width:90px">'
             f'<div class="k">TUTOR KEY • LEVEL 1 • TERM 1 • END-OF-TERM CHECK</div><h1>{E(c["title"])}</h1>'
             f'<p>10 questions, one from each lesson of the term, all at Start here level, plus one optional Think harder item. About 30 minutes on private paper. '
             f'No ranking, no score shown to the group, progress words only. For the tutor: do not hand this key to families.</p></div>')
    H.append(f'<div class="box t"><b>Where it sits.</b> {E(c["where"])}. <span class="small">{E(c["plan_note"])}</span></div>')
    H.append('<h2>1. The ten questions at a glance</h2><table><tr><th>Q</th><th>Lesson</th><th>Strand (tutor label)</th><th>What it checks (Start here level)</th><th>Answer</th></tr>')
    smap = {s['id']: s for s in c['strands']}
    for q in qs:
        H.append(f'<tr><td><b>{q["id"][1:]}</b></td><td>L{q["lesson"]}</td><td>{E(smap[q["strand"]]["moe_label"])}</td><td>{E(q["skill"])}</td><td class="ans">{E(q["answer"])}</td></tr>')
    o = c['optional']
    H.append(f'<tr><td><b>Think harder</b></td><td>L{o["lesson"]}</td><td>{E(smap[o["strand"]]["moe_label"])}</td><td>{E(o["skill"])} (optional, never scored)</td><td class="ans">{E(o["answer"])}</td></tr></table>')
    H.append('<p class="small">The strand labels are for the tutor only and must not appear on any child or parent page. Each question is a fresh example of the Start here idea of its lesson (different numbers from the lesson pages), so a child who understood the lesson can answer it. '
             'Before first use, a tutor should read each question against what the lesson actually taught.</p>')
    H.append('<h2>2. Giving it: before and during</h2><ol>' + ''.join(f'<li>{E(x)}</li>' for x in c['give']) + '</ol>')
    H.append('<h2>3. Returning it privately: after the lesson</h2><ol>' + ''.join(f'<li>{E(x)}</li>' for x in c['after']) + '</ol>')
    H.append('<div class="box r"><b>Privacy checklist</b><ul>' + ''.join(f'<li>{E(x)}</li>' for x in c['privacy_checklist']) + '</ul></div>')
    H.append('<h3>Absent, late joiners, families who prefer not to, upset children</h3><ul>' + ''.join(f'<li>{E(x)}</li>' for x in c['late']) + '</ul>')
    H.append('<h2 class="pb">4. Answer key and marking</h2><p class="small">Mark each question R (right), P (partly right), N (not yet) or T (not taught: the child did not attend that lesson). '
             'Mark on the tutor record sheet only, never on the child\'s paper. A child may write steps in any clear layout. Do not mark neatness or spelling.</p>')
    for q in qs + [dict(o, id='Think harder')]:
        lab = q['id'] if q['id'] == 'Think harder' else 'Q' + q['id'][1:]
        parts = '; '.join(f'({p["l"]}) {minus(p["text"].replace("___", "__").replace("[box]", "[ ]").replace("[wide]", "...."))} = {p["ans"]}' if p['l'] else f'{minus(p["text"].replace("___", "__"))} = {p["ans"]}' for p in q['parts'])
        right = q.get('right', 'The answer is right.'); partly = q.get('partly', '-')
        H.append(f'<div class="box k1"><b>{lab}</b> (L{q["lesson"]}) {E(minus(q["text"]))}<div class="ans">Answer: {E(minus(q["answer"]))}</div><div class="small">{E(parts)}</div>'
                 f'<div class="small"><b>R:</b> {E(right)} <b>P:</b> {E(partly)}</div><div class="small"><b>Worked:</b> {E(minus(q["solution"]))}</div>'
                 f'<div class="small"><b>Watch for:</b> {E("; ".join(q["mistakes"]))}</div></div>')
    H.append('<div class="note"><b>Question 9, part (a):</b> in the photo the page is flat, so measure the drawn line against the 10 cm print-check bar on the same page (the drawn line should be 57% to 63% of the bar). '
             'If the photo is not clear enough to tell, ask the grown-up (not the child) for a clearer photo, or count the line as right if the child\'s answer to part (b) is right. Never ask a child to show the line to the camera.</div>')
    H.append('<h2 class="pb">5. Tutor record sheet (tutor only; one per child; delete after the note is sent)</h2>')
    H.append('<p>Child (first name only): <span style="display:inline-block;width:260px;border-bottom:1.5px dotted #8A94AD">&nbsp;</span> &nbsp; Date taken: <span style="display:inline-block;width:120px;border-bottom:1.5px dotted #8A94AD">&nbsp;</span></p>')
    H.append('<table class="rec"><tr>' + ''.join(f'<th>Q{q["id"][1:]}<br><span class="small">L{q["lesson"]}</span></th>' for q in qs) + '<th>Think<br>harder</th></tr><tr>' + '<td></td>' * 11 + '</tr></table>')
    H.append('<p class="small">Write R, P, N or T in each box. R = 1 point, P = 0.5, N = 0, T = left out. Then work out each strand score and choose a word from the table.</p>')
    H.append('<table><tr><th>Strand (parent name)</th><th>Questions</th><th>Points / counted</th><th>Word</th></tr>' + ''.join(
        f'<tr><td>{E(s["parent_name"])}</td><td>{", ".join("Q" + x[1:] for x in s["questions"])}</td><td>&nbsp;</td><td>' + ''.join(f'<span class="tick"></span>{E(W[k])} ' for k in ('showing', 'getting', 'beginning')) + '</td></tr>' for s in c['strands']) + '</table>')
    H.append('<h3>Progress words: how a score becomes a word</h3>')
    H.append(f'<p class="small">{E(c["bands"]["rule"])} The word depends only on the child\'s own answers, never on other children.</p>')
    H.append('<table><tr><th>Questions counted in the strand</th><th>' + E(W['showing']) + '</th><th>' + E(W['getting']) + '</th><th>' + E(W['beginning']) + '</th></tr>' + ''.join(
        f'<tr><td>{b["n"]}</td><td>{b["showing"]}</td><td>{b["getting"]}</td><td>{b["beginning"]}</td></tr>' for b in sorted(c['bands']['table'], key=lambda b: -b['n'])) + '</table>')
    H.append('<p class="small">If no question in a strand was taught to the child, write no line for that strand. Strand lines say what the child did and what helps next, never a grade. '
             'The optional Think harder question is never scored; add the optional line only if the child answered it correctly.</p>')
    H.append('<h2 class="pb">6. Parent report line templates (copy into the note to the parent contact)</h2>')
    rt = c['report_template']
    H.append(f'<div class="box t"><b>{E(rt["intro"])}</b><br>{E(rt["term_line"])}</div>')
    H.append('<table><tr><th>Area (parent wording)</th><th>' + E(W['showing']) + '</th><th>' + E(W['getting']) + '</th><th>' + E(W['beginning']) + '</th></tr>' + ''.join(
        f'<tr><td><b>{E(s["parent_name"])}</b><div class="small">Lessons {s["lessons"][0]}' + (f' to {s["lessons"][-1]}' if len(s["lessons"]) > 1 else '') + f'. We looked at {E(s["looked_at"])}.</div></td><td>{E(s["showing"])}</td><td>{E(s["getting"])}</td><td>{E(s["beginning"])}</td></tr>' for s in c['strands']) + '</table>')
    H.append(f'<div class="box"><b>Then add (from your own notes):</b><br>{E(rt["strength"])}<br>{E(rt["next_step"])}<br><i>{E(rt["optional"])}</i><br>{E(rt["closing"])}</div>')
    ex = rt['example_words']
    H.append('<h3>A filled example (fictional child, Mei)</h3><div class="note">' + f'<b>Term 1 progress note for Mei</b><br>{E(rt["term_line"])}<br>' + ''.join(
        f'<b>{E(s["parent_name"])}: {E(W[ex[s["id"]]])}.</b> {E(s[ex[s["id"]]].replace("[Name]", "Mei"))}<br>' for s in c['strands']) +
        'One thing Mei did well this term: she explained why 62 is bigger than 26 using bundles of ten.<br>One next step: act out two-step stories with counters at home.<br>' + E(rt['closing'].replace('[Name]', 'Mei')) + '</div>')
    H.append('<p class="small">Words to avoid in the note: score, mark, out of, rank, top, below average, behind, ahead of, pass, fail, predicted, ready for. No claim about exams, GEP or any contest. '
             'No mention of other children. The note goes to the parent contact only.</p>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Check key</title><style>{font_css()}{KEY_CSS}</style></head><body>{"".join(H)}</body></html>'


# ------------------------------------------------------------------ the grown-up note

NOTE_CSS = """
@page{size:A4;margin:12mm 15mm}
*{box-sizing:border-box}
body{margin:0;font-family:'Nunito Sans',Arial,sans-serif;color:#1B2A49;font-size:13px;line-height:1.38;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2{font-family:'Fredoka',Arial,sans-serif;font-weight:600;margin:0}
h1{font-size:27px;line-height:1.1}
h2{font-size:16px;color:#1F7A6F;margin:11px 0 3px;border-bottom:2px solid #FFC93C;padding-bottom:2px}
.hd{display:flex;align-items:center;gap:14px;border-bottom:3px solid #1B2A49;padding-bottom:8px;margin-bottom:8px}
.tp{color:#5B6785;font-size:11.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
ul{margin:3px 0 3px 18px;padding:0}li{margin:2px 0}
.panel{background:#F3F6FA;border-top:5px solid #1F7A6F;padding:9px 13px;margin:8px 0;break-inside:avoid}
.small{font-size:11px;color:#5B6785}
"""


def note_html(d):
    c = d['end_of_term_check']; n = c['parent_note']
    li = lambda xs: ''.join(f'<li>{E(x)}</li>' for x in xs)
    body = (f'<div class="hd"><img alt="Mi the dolphin" src="{mi_uri()}" style="width:20mm;height:auto"><div><div class="tp">Level 1 • Term 1 • For grown-ups</div><h1>{E(n["title"])}</h1></div></div>'
            f'<p style="margin:0 0 4px">{E(n["what"])}</p>'
            f'<h2>Before the lesson</h2><ul>{li(n["before"])}</ul>'
            f'<h2>During the check</h2><ul>{li(n["during"])}</ul>'
            f'<h2>After the lesson: sending the sheet privately</h2><ul>{li(n["after"])}</ul>'
            f'<div class="panel"><b>What you get back.</b> {E(n["back"])}</div>'
            f'<p>{E(n["make_up"])}</p>'
            f'<p class="small">Your child\'s paper, photos and note are treated as private: we never show them to other children or families, and we never compare children. Math Inquirers by Preciouslyours Pte Ltd.</p>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Grown-up note</title><style>{font_css()}{NOTE_CSS}</style></head><body>{body}</body></html>'


# ------------------------------------------------------------------ rendering and real-PDF checks

def render(pw, html_text, name, out_dir, pdf_name, footer, margin):
    hp = os.path.join(out_dir, 'html', name + '.html')
    os.makedirs(os.path.dirname(hp), exist_ok=True)
    open(hp, 'w', encoding='utf-8').write(html_text)
    pg = pw.new_page()
    pg.goto('file://' + hp, wait_until='networkidle')
    pg.wait_for_timeout(500)
    foot = (f'<div style="width:100%;font-size:9px;color:#5B6785;padding:0 12mm;display:flex;justify-content:space-between;font-family:Arial"><span>{footer}</span><span>Page <span class="pageNumber"></span></span></div>') if footer else '<div></div>'
    pg.pdf(path=os.path.join(out_dir, pdf_name), format='A4', print_background=True, prefer_css_page_size=False, display_header_footer=bool(footer),
           header_template='<div></div>', footer_template=foot, margin=margin)
    pg.close()
    return os.path.join(out_dir, pdf_name)


def longest_dark_run_mm(pdf, page, dpi=254, y_range=None):
    """Longest horizontal run of dark pixels (in mm) on a rendered page, optionally within rows y_range=(y0_mm, y1_mm)."""
    from PIL import Image
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', '-png', '-f', str(page), '-l', str(page), pdf, os.path.join(td, 'p')], check=True)
        f = sorted(glob.glob(os.path.join(td, 'p-*.png')))[0]
        im = Image.open(f).convert('L')
        w, h = im.size
        px = dpi / 25.4
        y0, y1 = (0, h) if not y_range else (int(y_range[0] * px), int(y_range[1] * px))
        data = im.load()
        best = []
        for y in range(y0, min(h, y1)):
            run = 0
            for x in range(w):
                if data[x, y] < 140:
                    run += 1
                else:
                    if run > 20:
                        best.append((run / px, y))
                    run = 0
            if run:
                best.append((run / px, y))
        return sorted(best, reverse=True)


def measure_sheet(pdf, c):
    """Measure the printed 10 cm bar (page 4) and the 9 cm line (page 3) on the rendered PDF. Returns (bar_mm, line_mm)."""
    bar_target, line_target = c['sheet_check_bar_mm'], c['line_mm']
    runs4 = longest_dark_run_mm(pdf, 4); runs3 = longest_dark_run_mm(pdf, 3)
    bar = min((r for r, _ in runs4 if abs(r - bar_target) < 3), key=lambda r: abs(r - bar_target), default=None)
    line = min((r for r, _ in runs3 if abs(r - line_target) < 3), key=lambda r: abs(r - line_target), default=None)
    return bar, line


def main():
    from playwright.sync_api import sync_playwright
    sys.path.insert(0, TOOLS)
    import pdfcheck
    d = load()
    c = d['end_of_term_check']
    od = os.path.join(L1, 'out', 'l10')
    os.makedirs(od, exist_ok=True)
    marg = {'top': '12mm', 'bottom': '14mm', 'left': '14mm', 'right': '14mm'}
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        sheet = render(b, sheet_html(d), 'check_student', od, 'L10_Check_Student.pdf', 'Math Inquirers Term 1 end-of-term check. Print at 100% (actual size).', {'top': '12mm', 'bottom': '15mm', 'left': '14mm', 'right': '14mm'})
        key = render(b, key_html(d), 'check_key', od, 'L10_Check_Tutor_Key.pdf', 'Math Inquirers Term 1 end-of-term check. Tutor key and private return plan. Tutor only.', {'top': '14mm', 'bottom': '16mm', 'left': '13mm', 'right': '13mm'})
        note = render(b, note_html(d), 'check_parent_note', od, 'L10_Check_Parent_Note.pdf', '', {'top': '12mm', 'bottom': '12mm', 'left': '15mm', 'right': '15mm'})
        b.close()
    ok = True
    n_sheet = pdfcheck.pdf_pages(sheet)
    fills = pdfcheck.pdf_fill(sheet, 12.0, 15.0)
    print('student sheet pages', n_sheet, 'fill', ', '.join(f'{f:.0%}' for f in fills))
    if n_sheet != c['sheet_pages']:
        print('FAIL student sheet has', n_sheet, 'pages, designed', c['sheet_pages']); ok = False
    for i, f in enumerate(fills, 1):
        if f < 0.80: print(f'WARN sheet page {i} only {f:.0%} full')
        if f > 1.0: print(f'WARN sheet page {i} over full')
    nk = pdfcheck.pdf_pages(key); nn = pdfcheck.pdf_pages(note)
    kfill = pdfcheck.pdf_fill(key, 14.0, 16.0)
    print('tutor key pages', nk, 'fill', ', '.join(f'{f:.0%}' for f in kfill), '| parent note pages', nn, 'fill', ', '.join(f'{f:.0%}' for f in pdfcheck.pdf_fill(note, 12.0, 12.0)))
    if nn != 1:
        print('FAIL parent note must be one page'); ok = False
    bar, line = measure_sheet(sheet, c)
    print('printed 10 cm bar measures', None if bar is None else f'{bar:.2f} mm', '| printed 9 cm line measures', None if line is None else f'{line:.2f} mm')
    for name, got, want in (('bar', bar, c['sheet_check_bar_mm']), ('line', line, c['line_mm'])):
        if got is None or abs(got - want) > 0.6:
            print(f'FAIL printed {name} is {got} mm, should be {want} mm'); ok = False
    print('built', od)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
