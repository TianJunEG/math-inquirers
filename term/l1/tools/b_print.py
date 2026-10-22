"""Printed pieces: student workbook (+ separate answer key), home practice sheet, one-page parent summary. Student style = hp/wb_style.css (A + D)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *  # noqa
import svg

WB_CSS = open(os.path.join(ROOT, 'hp', 'wb_style.css'), encoding='utf-8').read()
PARENT_CSS = open(os.path.join(ROOT, 'hp', 'parent_style.css'), encoding='utf-8').read()
EXTRA = """
body{font-size:18.5px!important}.qbox{padding:26px 16px 12px!important;margin:26px 4px 18px 4px!important}.ln{height:31px!important;margin-top:2px!important}.sub{margin-top:7px;font-size:19px}.sl{font-size:18px!important}.al{min-width:70px!important;height:22px!important}.pv td{height:36px!important;font-size:22px!important}.qbox .qn{font-size:18px!important}

.pv{border-collapse:collapse;font-family:Fredoka;margin:4px 0}.pv th{background:#FFC93C;border:2px solid #1B2A49;padding:1px 16px;font-size:13px}.pv td{border:2px solid #1B2A49;padding:2px 16px;min-width:60px;height:26px;background:#fff;font-size:18px;text-align:center}
.draw{border:2.5px dashed #1B2A49;border-radius:10px;height:105px;background:#fff;margin:6px 0 6px 4px}
.vis{width:310px;margin:6px 0 6px 4px}
.al{display:inline-block;min-width:54px;border-bottom:2px dashed #1B2A49;height:18px;vertical-align:baseline}
.choice{border:2px dashed #1F7A6F;border-radius:12px;background:#E8F5F2;padding:5px 12px;font-size:15px;margin:2px 0 8px}
.p1 .draw{height:84px!important}.p1 .qbox{margin:22px 4px 8px 4px!important;padding:22px 16px 8px!important}.p1 .vis{width:270px!important}.hm .qbox{margin:20px 4px 8px 4px!important;padding:20px 14px 6px!important}.hm .ln{height:29px!important}.p5 .qbox{margin:20px 4px 8px 4px!important;padding:22px 16px 6px!important}.p5 .ln{height:26px!important}.p5 .vis{width:230px!important;margin:2px 0 0 4px!important}.p5 .lbk{margin-top:4px}.p5 .banner{margin:4px 0!important}.p5 p{margin:2px 0!important}.page{break-after:page}.page:last-child{break-after:auto}
.lbk{border:2px solid #1B2A49;border-radius:14px;background:#FFFDF5;padding:5px 12px 6px;margin-top:6px}.lbk .r{margin-top:3px!important;font-size:13.5px!important}
.lbk .r{display:flex;flex-wrap:wrap;gap:2px 8px;margin-top:5px;font-size:14.5px;align-items:center}.lbk .r b{flex:none;width:165px}
.bx{display:inline-block;width:15px;height:15px;border:2px solid #1B2A49;border-radius:4px;background:#fff;vertical-align:-2px;margin:0 3px 0 6px}
.wl{border-bottom:2px dotted #8A94AD;height:24px}
.boxb{display:inline-block;width:36px;height:36px;border:2.5px solid #1B2A49;border-radius:9px;background:#fff;vertical-align:middle;margin:0 5px}
.keybox{border:2px solid #1B2A49;border-radius:6px;padding:6px 10px;margin:6px 0;background:#fff;break-inside:avoid;font-size:14px}
.keybox .a{font-weight:800;color:#1F7A6F}
"""


def hdr(d, tag, title=None, mi=False):
    head = (f'<div class="lh"><span class="lbadge">Term {d["term"]} • Lesson {d["lesson_in_term"]}</span><span class="ltopic">{E(header_topic(d))}</span>'
            f'<span style="margin-left:auto;background:#FFC93C;color:#1B2A49;border-radius:999px;padding:4px 16px;font-weight:700;font-size:15px">{tag}</span></div>'
            + (f'<div class="ltitle">{E(title)}</div>' if title else '')
            + '<div class="namer"><b>Name</b><span></span><b>Date</b><span style="max-width:120px"></span></div>')
    if not mi:
        return head
    i = head.index('<div class="ltitle">') if '<div class="ltitle">' in head else head.index('<div class="namer">')
    img = f'<img alt="Mi the dolphin" src="{mi_uri()}" style="width:22mm;height:auto;flex:none;margin:-2px 0 -8px 8px">'
    return head[:i] + f'<div style="display:flex;align-items:flex-start"><div style="flex:1;min-width:0">' + head[i:] + f'</div>{img}</div>'


def qbox(q, label=None, draw=False):
    lab = label or q['id']
    vis = f'<div class="vis">{svg.render_visual(q["visual"])}</div>' if q.get('visual') else ''
    parts = ''
    if q.get('parts'):
        for p in q['parts']:
            parts += f'<div class="sub"><span class="sl">{E(p["l"])}</span><span>{blanks(p["text"])}</span></div>'
    if q.get('draw'): vis += '<div class="draw"></div>'
    ln = ''.join('<div class="ln"></div>' for _ in range(q.get('lines', 0)))
    return f'<div class="qbox"><div class="q"><span class="qn">{lab}</span><span class="qt">{E(q["text"])}</span></div>{vis}{parts}{ln}</div>'


def kit_pages(d):
    out = []
    for k in kits(d):
        out.append(f'<div class="page kit">{hdr(d, "Kit")}<div class="ltitle" style="font-size:24px">{E(k.get("title", "Kit page"))}</div><p style="font-size:13.5px;margin:2px 0 6px">{E(k.get("intro", "A grown-up cuts these out before the lesson."))}</p><div style="width:{k.get("width", 84)}%">{svg.kit_figure(k)}</div></div>')
    return out


def workbook_html(d, key=False):
    t = d['tiers']; inv = t['investigation']
    P = []
    P.append(f'<div class="page p1">{hdr(d, "Start here", d["title"].upper() + "!", mi=True)}<div class="choice">After question 3 you may choose: carry on, or try <b>Think harder</b>.</div><p style="font-style:italic;margin:2px 0 6px">{E(wb(d, "hint_p1", "Use objects, your kit or a drawing. Say your answer out loud, then write it."))}</p>' + ''.join(qbox(q) for q in t['start'] if q['page'] == 1) + '</div>')
    P.append(f'<div class="page">{hdr(d, "Start here")}' + ''.join(qbox(q) for q in t['start'] if q['page'] == 2) + '</div>')
    P.append(f'<div class="page">{hdr(d, "Think harder")}<p style="font-style:italic;margin:2px 0 6px">{E(wb(d, "hint_p3", "Use objects, draw a picture or make a table. Then write how you know. Choose any question, in any order."))}</p>' + ''.join(qbox(q) for q in t['think']) + '</div>')
    P.append(f'<div class="page">{hdr(d, "Go further")}<p style="font-style:italic;margin:2px 0 6px">{E(wb(d, "hint_p4", "Choose any question. You do not have to finish them all."))}</p>' + ''.join(qbox(q) for q in t['go']) + '</div>')
    ex = ''.join(qbox(q, 'E' + q['id'][1:] if False else q['id']) for q in d['exit'])
    lb = d['look_back']
    bx = lambda items: ''.join(f'<span><i class="bx"></i>{E(x)}</span>' for x in items)
    look = ('<div class="lbk"><div style="font-weight:700;color:#1F7A6F;font-size:18px">Look-back <span style="font-weight:400;font-size:12.5px;color:#3B4A6B">There are no right answers. You can pass. Nobody reads it out.</span></div>'
            '<div class="r"><b>Something I did well:</b><span class="wl" style="flex:1;min-width:120px"></span></div>'
            f'<div class="r"><b>The hardest part was ...</b>{bx(lb["hardest"])}</div>'
            f'<div class="r"><b>What helped me:</b>{bx(lb["helped"])}</div>'
            f'<div class="r"><b>Next time I will try:</b>{bx(lb["next"])}</div>'
            '<div class="r"><b></b><span><i class="bx"></i>I am still stuck (my tutor will come and help)</span><span><i class="bx"></i>I would like to pass</span></div></div>')
    P.append(f'<div class="page p5">{hdr(d, "Choose, then look back")}<div class="banner">Investigation: {E(inv["title"])}</div><p style="font-style:italic;margin:2px 0">Choose this any time you like. You do not have to finish it.</p>'
             f'<p style="margin:3px 0"><b>Easy first step:</b> {E(inv["first"])}</p><p style="margin:3px 0"><b>Then:</b> {E(inv["text"])}</p>' + '<div class="ln"></div>' * 1 +
             f'<div class="banner" style="margin-top:6px">Exit ticket</div><p style="font-style:italic;margin:2px 0">On your own, at the end of the lesson. No looking back.</p>{ex}{look}</div>')
    P += kit_pages(d)
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{font_css()}{WB_CSS}{EXTRA}</style></head><body>{"".join(P)}</body></html>'


def key_html(d):
    t = d['tiers']; inv = t['investigation']
    P = [f'<h1 style="font-family:Fredoka;margin:0;color:#1B2A49">Answer key: Lesson {d["lesson_in_term"]}, {E(d["title"])}</h1><p style="font-size:13px;margin:2px 0 8px"><b>For the tutor and grown-ups.</b> Keep this page away from the child until they have finished and checked their own work. Ask <i>how do you know?</i> before saying right or wrong.</p>']
    def block(q):
        return (f'<div class="keybox"><b>{q["id"]}.</b> {E(q["text"])}<div class="a">Answer: {E(q["answer"])}</div><div style="font-size:12.5px">{E(q["solution"])}</div>'
                f'<div style="font-size:12px;color:#3B4A6B"><b>Watch for:</b> {"; ".join(E(m) for m in q["mistakes"])}</div></div>')
    P.append('<div class="banner">Start here (pages 1 and 2)</div>' + ''.join(block(q) for q in t['start']))
    P.append('<div class="banner">Think harder (page 3)</div>' + ''.join(block(q) for q in t['think']))
    P.append('<div class="banner">Go further (page 4)</div>' + ''.join(block(q) for q in t['go']))
    P.append(f'<div class="banner">Investigation (page 5): {E(inv["title"])}</div><div class="keybox"><div class="a">{E(inv["answer"])}</div><div style="font-size:12px"><b>Look for:</b> {E(inv["look_for"])}</div></div>')
    P.append('<div class="banner">Exit ticket (page 5)</div>' + ''.join(block(q) for q in d['exit']))
    P.append(f'<div class="banner">Sneak-peek puzzles (not in the workbook)</div><div class="keybox">1. {E(d["sneak_peek"]["a1"])} stars.<br>2. {E(d["sneak_peek"]["a2"])}</div>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{font_css()}{WB_CSS}{EXTRA}body{{background-image:none}}</style></head><body>{"".join(P)}</body></html>'


def home_html(d):
    H = d['home_practice']
    qs = ''
    for h in H:
        tag = {'start': 'Start here', 'think': 'Think harder', 'go': 'Go further'}[h['tier']]
        qs += f'<div class="qbox"><div class="q"><span class="qn">{h["id"][1:]}</span><span class="qt"><span style="font-size:12px;color:#1F7A6F;font-weight:800">{tag}</span><br>{E(h["text"])}</span></div>' + '<div class="ln"></div>' * (2 if h['id'] == 'H5' else 1) + '</div>'
    ans = ''.join(f'<div class="keybox"><b>{h["id"][1:]}.</b> <span class="a">{E(h["answer"])}</span><div style="font-size:12.5px">{E(h["solution"])}</div></div>' for h in H)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{font_css()}{WB_CSS}{EXTRA}</style></head><body>'
            f'<div class="page hm">{hdr(d, "Home practice", d["title"] + ": practice at home")}<p style="margin:2px 0 6px;font-size:14.5px">About 15 minutes, a few days after the lesson. Use real things or draw bundles. A grown-up may read the questions aloud. Wrong answers are fine: they show what to try next.</p>{qs}</div>'
            f'<div class="page"><div class="ltitle">Answers for grown-ups</div><p style="font-size:13px">Please let your child try first, then check together. Ask <i>how do you know?</i> If your child is stuck, wait 10 seconds, then suggest drawing the bundles.</p>{ans}'
            f'<p style="font-size:12.5px;margin-top:10px">More practice online (no timers, no scores): ask your tutor for the practice link, key <b>{d["online_practice"]["key"]}</b>.</p></div></body></html>')


def parent_html(d):
    p = d['parent']
    li = lambda xs, cls='': ''.join(f'<li>{E(x)}</li>' for x in xs)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{font_css()}{PARENT_CSS}'
            '@page{size:A4;margin:12mm 15mm}body{font-size:13.2px;line-height:1.38}.side h3{font-size:15px}.panel{padding:10px 14px;margin-bottom:10px}.panel h3{font-size:16px}.tips li{margin-bottom:6px}.hd{margin:0 0 10px}.big{font-size:60px}'
            f'</style></head><body><div class="hd"><img alt="Mi the dolphin" src="{mi_uri()}" style="width:22mm;height:auto"><div class="big">{d["lesson_in_term"]}</div><div><div class="tp">Level {d["level"]} • Term {d["term"]} • Lesson {d["lesson_in_term"]} • For parents</div><h1>{E(d["title"])}</h1></div></div>'
            f'<div class="cols"><div><div class="kick">What we did</div><p style="margin:3px 0 8px">{E(p["summary"])}</p>'
            f'<div class="quote">{E(p.get("quote") or d["big_idea"] + ".")}</div>'
            f'<div class="kick">Try at home (5 minutes)</div><ol class="tips">{li(p["try_home"])}</ol>'
            f'<div class="panel"><h3>When your child is stuck</h3><p style="margin:0">{E(p["when_stuck"])}</p></div></div>'
            f'<div><div class="side"><h3>Words we used</h3><ul style="margin:0;padding-left:16px">{li(p["words"])}</ul></div>'
            f'<div class="side" style="margin-top:12px"><h3>Good questions</h3><ul style="margin:0;padding-left:16px">{li(p["ask"])}</ul></div>'
            f'<div class="side" style="margin-top:12px"><h3>Things to have ready</h3><ul style="margin:0;padding-left:16px">{li(d["materials"]["child"][:3])}</ul></div></div></div>'
            f'<div class="panel"><h3>Next lesson</h3><p style="margin:0">{E(p["next"])} Missed a lesson? Every lesson is recorded; your tutor will share a private link with enrolled families.</p></div>'
            f'<p style="font-size:11.5px;color:#5B6785;margin:8px 0 0">{E(p["term_line"])} We share what we see in your child’s thinking, never a rank or a mark compared with other children. Math Inquirers by Preciouslyours Pte Ltd.</p></body></html>')


def build_print(d, pw):
    od = outdir(d)
    n = d['_num']
    def render(name, html, footer, pdfname, fmt='A4'):
        hp = os.path.join(outdir(d, 'html'), name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg = pw.new_page(); pg.goto('file://' + hp, wait_until='networkidle'); pg.wait_for_timeout(500)
        foot = f'<div style="width:100%;font-size:9px;color:#5B6785;padding:0 14mm;display:flex;justify-content:space-between;font-family:Arial"><span>{footer}</span><span>Page <span class="pageNumber"></span></span></div>' if footer else '<div></div>'
        pg.pdf(path=os.path.join(od, pdfname), format=fmt, print_background=True, display_header_footer=bool(footer), header_template='<div></div>', footer_template=foot,
               margin={'top': '14mm', 'bottom': '16mm', 'left': '14mm', 'right': '14mm'} if footer else {'top': '12mm', 'bottom': '12mm', 'left': '15mm', 'right': '15mm'})
        pg.close()
    f = 'Math Inquirers Term 1 • Notice it. Test it. Explain why.'
    render('workbook', workbook_html(d), f + f' • Lesson {d["lesson_in_term"]}', f'L{n}_Workbook.pdf')
    render('workbook_key', key_html(d), f + ' • Answer key (tutor and grown-ups)', f'L{n}_Workbook_Answer_Key.pdf')
    render('home', home_html(d), f + ' • Home practice', f'L{n}_Home_Practice.pdf')
    render('parent', parent_html(d), '', f'L{n}_Parent_Summary.pdf')


def page_fill(pw, d):
    """Fraction of the printable A4 height (267 mm) used by each workbook page except the kit page."""
    hp = os.path.join(outdir(d, 'html'), 'workbook_fill.html')
    open(hp, 'w', encoding='utf-8').write(workbook_html(d))
    pg = pw.new_page(viewport={'width': 794, 'height': 1123})
    pg.goto('file://' + hp, wait_until='networkidle'); pg.wait_for_timeout(300)
    res = pg.evaluate("""() => Array.from(document.querySelectorAll('.page:not(.kit)')).map(p => {
        const top = p.getBoundingClientRect().top; let m = 0;
        Array.from(p.children).forEach(c => { m = Math.max(m, c.getBoundingClientRect().bottom - top); });
        return m / (267 / 25.4 * 96); })""")
    pg.close()
    return res
