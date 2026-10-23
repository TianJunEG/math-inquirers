"""Printed pieces: student workbook (+ separate answer key), home practice sheet, one-page parent summary. Student style = hp/wb_style.css (A + D)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *  # noqa
E = Ef      # family-facing pages: one lesson numbering scheme
import svg

WB_CSS = open(os.path.join(ROOT, 'hp', 'wb_style.css'), encoding='utf-8').read()
PARENT_CSS = open(os.path.join(ROOT, 'hp', 'parent_style.css'), encoding='utf-8').read()
EXTRA = """
body{font-size:18.5px!important}.qbox{padding:26px 16px 12px!important;margin:26px 4px 18px 4px!important}.ln{height:31px!important;margin-top:2px!important}.sub{margin-top:7px;font-size:19px}.sl{font-size:18px!important}.al{height:22px!important}.pv td{height:36px!important;font-size:22px!important}.qbox .qn{font-size:18px!important}

.pv{border-collapse:collapse;font-family:Fredoka;margin:4px 0}.pv th{background:#FFC93C;border:2px solid #1B2A49;padding:1px 16px;font-size:13px}.pv td{border:2px solid #1B2A49;padding:2px 16px;min-width:60px;height:26px;background:#fff;font-size:18px;text-align:center}
.draw{border:2.5px dashed #1B2A49;border-radius:10px;height:105px;background:#fff;margin:6px 0 6px 4px}
.vis{width:310px;margin:6px 0 6px 4px}
.al{display:inline-block;min-width:17mm;border-bottom:2px dashed #1B2A49;height:18px;vertical-align:baseline}
.choice{border:2px dashed #1F7A6F;border-radius:12px;background:#E8F5F2;padding:5px 12px;font-size:15px;margin:2px 0 8px}
.p1 .draw{height:84px!important}.p1 .qbox{margin:22px 4px 8px 4px!important;padding:22px 16px 8px!important}.p1 .vis{width:270px!important}.hm{padding-left:3mm}.hm .qbox{margin:20px 4px 8px 4px!important;padding:20px 14px 6px!important}.hm .boxb{width:26px;height:26px;margin:0 3px}.hm .ln{height:29px!important}.p5 .qbox{margin:20px 4px 8px 4px!important;padding:22px 16px 6px!important}.p5 .ln{height:26px!important}.p5 .vis{width:230px!important;margin:2px 0 0 4px!important}.p5 .lbk{margin-top:4px;padding:4px 10px 5px}.p5 .lbk .r{margin-top:3px!important;font-size:15.5px!important}.p5 .qbox .qt{font-size:17px}.p5 .banner{margin:4px 0!important}.p5 p{margin:2px 0!important}.page{break-after:page}.page:last-child{break-after:auto}
.lbk{border:2px solid #1B2A49;border-radius:14px;background:#FFFDF5;padding:5px 12px 6px;margin-top:6px}.lbk .r{margin-top:3px!important;font-size:13.5px!important}
.lbk .r{display:flex;flex-wrap:wrap;gap:3px 9px;margin-top:6px;font-size:16.5px;align-items:center}.lbk .r b{flex:none;width:165px}
.bx{display:inline-block;width:15px;height:15px;border:2px solid #1B2A49;border-radius:4px;background:#fff;vertical-align:-2px;margin:0 3px 0 6px}
.wl{border-bottom:2px dotted #8A94AD;height:24px}
.boxb{display:inline-block;width:36px;height:36px;border:2.5px solid #1B2A49;border-radius:9px;background:#fff;vertical-align:middle;margin:0 5px}
.qbox:has(svg.h100){display:grid;grid-template-columns:1fr 310px;column-gap:8px;align-items:start}
.qbox:has(svg.h100)>.q{grid-column:1 / span 2}
.qbox:has(svg.h100)>.vis{grid-column:2;grid-row:2 / span 8;width:310px!important;margin:0!important}
.qbox:has(svg.h100)>.sub,.qbox:has(svg.h100)>.ln,.qbox:has(svg.h100)>.draw{grid-column:1}
.qbox:has(svg.h100.wide){display:block}
.qbox:has(svg.h100.wide)>.vis{width:100%!important;margin:4px 0!important}
.p1 .qbox:has(svg.h100)>.vis{width:296px!important}
.tight .qbox{margin:14px 4px 5px 4px!important;padding:18px 14px 4px!important}.tight .ln{height:25px!important}.tight .draw{height:78px!important}.tight .vis{width:240px!important}.tight .sub{margin-top:4px}
.tight2 .qbox{margin:10px 4px 3px 4px!important;padding:16px 12px 2px!important}.tight2 .ln{height:22px!important}.tight2 .draw{height:64px!important}.tight2 .vis{width:200px!important}.tight2 .lbk .r{font-size:12px!important}.tight2.p5 .qt{font-size:15.5px}
.tight3 .qbox{margin:8px 4px 2px 4px!important;padding:14px 10px 2px!important}.tight3 .ln{height:19px!important}.tight3 .qt,.tight3 .sub{font-size:15px!important}.tight3 .lbk .r{font-size:13px!important}.tight3 .banner{font-size:15px!important}
.hm.t1 .qbox{margin:14px 4px 5px 4px!important;padding:16px 12px 4px!important}.hm.t1 .ln{height:24px!important}.hm.t2 .qbox{margin:10px 4px 3px 4px!important;padding:14px 12px 2px!important}.hm.t2 .ln{height:20px!important}.hm.t2 .q{font-size:17px}
.yn{display:inline-flex;gap:30px;margin-left:12px;font-family:Fredoka;font-weight:600;font-size:20px}.yn span{padding:1px 14px}
.banner{break-after:avoid;display:block;width:fit-content}
.vis.wide{width:100%!important;max-width:520px}.vis.wide.bm{max-width:430px}.vis.sm{width:175px!important}.visrow .vis.sm{width:175px!important;max-width:175px}.visrow .vis.md{width:235px!important;max-width:235px}.vis.md{width:250px!important}.vis.nar{width:150px!important}.vis.nar.rt{width:235px!important}.vis.arr{width:250px!important}.vis.xw{width:100%!important;max-width:540px}.p1 .vis.xw{max-width:400px}.tight .vis.xw{max-width:420px}.tight2 .vis.xw{max-width:340px}
.visrow{display:flex;gap:10px;align-items:flex-end;margin:4px 0}.visrow .vis{width:calc(100%/var(--n) - 10px)!important;max-width:330px;margin:2px 0!important}
.tf{border-collapse:collapse;margin:6px 4px;font-size:16px}.tf th{background:#FFC93C;border:2px solid #1B2A49;padding:3px 12px}.tf td{border:2px solid #1B2A49;padding:6px 10px;background:#fff}.tf td.tk{text-align:center;width:70px}.tf .bx{width:22px;height:22px}
.mcq{display:flex;align-items:flex-start;justify-content:space-between;margin:4px 6px}.mo{display:flex;gap:8px;margin:5px 0}.mn{font-weight:800;color:#1F7A6F}.mbr{border:2px solid #1B2A49;border-radius:6px;padding:4px 18px;background:#fff;font-size:20px;align-self:center}
.stp{display:flex;align-items:flex-end;gap:10px;margin:6px 4px 0 6px;font-size:16px}.stp b{color:#1F7A6F;width:60px}.pins2{font-size:14px;color:#3B4A6B;margin:0 6px 4px}
.keybox{border:2px solid #1B2A49;border-radius:6px;padding:6px 10px;margin:6px 0;background:#fff;break-inside:avoid;font-size:14px}
.keybox .a{font-weight:800;color:#1F7A6F}
"""


def hdr(d, tag, title=None, mi=False):
    head = (f'<div class="lh"><span class="lbadge">Term {d["term"]} • Lesson {d["lesson_in_term"]}</span><span class="ltopic">{E(header_topic(d))}</span>'
            f'<span style="margin-left:auto;background:#FFC93C;color:#1B2A49;border-radius:999px;padding:4px 16px;font-weight:700;font-size:15px">{tag}</span></div>'
            + (f'<div class="ltitle" style="font-size:{38 if len(title) <= 24 else (30 if len(title) <= 36 else (25 if len(title) <= 48 else 21))}px;line-height:1.1">{E(title)}</div>' if title else '')
            + '<div class="namer"><b>Name</b><span></span><b>Date</b><span style="max-width:120px"></span></div>')
    if not mi:
        return head
    i = head.index('<div class="ltitle">') if '<div class="ltitle">' in head else head.index('<div class="namer">')
    img = f'<img alt="Mi the dolphin" src="{mi_uri()}" style="width:22mm;height:auto;flex:none;margin:-2px 0 -8px 8px">'
    return head[:i] + f'<div style="display:flex;align-items:flex-start"><div style="flex:1;min-width:0">' + head[i:] + f'</div>{img}</div>'


CHOICE_PATTERNS = [(r'circle (yes or no|yes/no)', ('Yes', 'No')), (r'circle (right or wrong|right/wrong)', ('Right', 'Wrong')),
                   (r'(circle) (true or false|true/false)', ('True', 'False'))]


def choice_words(text, explicit=None):
    """Words to print for the child to circle: explicit `choices`, else detected from the instruction ('Circle Yes or No.')."""
    if explicit: return list(explicit)
    for pat, words in CHOICE_PATTERNS:
        if re.search(pat, text, re.I): return list(words)
    return None


def choice_html(words):
    return '<span class="yn">' + ''.join(f'<span>{E(w)}</span>' for w in words) + '</span>'


def _vis_html(v):
    if v.get('type') == 'ruler':   # true 1:1 scale on paper
        return f'<div class="vis" style="width:auto!important;margin:6px 0 6px 4px">{svg.ruler(v.get("start", 0), v.get("end", 15), v.get("objects"), v.get("mark"), true_scale=True)}</div>'
    wide = v.get('type') in ('table', 'bar_model', 'line_up', 'picture_graph', 'money')
    xw = v.get('type') in ('number_line', 'seq')
    arr = v.get('type') == 'array'
    nar = v.get('type') in ('round_table', 'domino')
    sm = v.get('type') in ('clock', 'price_tag', 'fold_punch', 'network', 'shapes2d')
    md = v.get('type') in ('cube_stack', 'grid', 'calendar')
    return f'<div class="vis{" wide" if wide else ""}{" xw" if xw else ""}{" sm" if sm else ""}{" md" if md else ""}{" arr" if arr else ""}{" nar" if nar else ""}{" bm" if v.get("type") == "bar_model" else ""}{" rt" if v.get("type") == "round_table" else ""}">{svg.render_visual(v)}</div>'


def inv_draw(inv):
    """A drawing box on the Investigation page whenever the task asks the child to draw (inv.draw: true, or a number of boxes; or the words draw/sketch in the task)."""
    dr = inv.get('draw')
    if dr is None: dr = bool(re.search(r'\b(draw|sketch)\b', inv.get('first', '') + ' ' + inv.get('text', ''), re.I))
    n = 1 if dr is True else int(dr or 0)
    return ''.join('<div class="draw" style="height:%dpx"></div>' % (96 if n == 1 else 66) for _ in range(n))


def inv_vis(inv):
    vs = ([inv['visual']] if inv.get('visual') else []) + list(inv.get('visuals') or [])
    if not vs: return ''
    if len(vs) == 1: return _vis_html(vs[0])
    return f'<div class="visrow" style="--n:{len(vs)}">' + ''.join(_vis_html(v) for v in vs) + '</div>'


def qbox(q, label=None, draw=False):
    lab = label or q['id']
    vis = _vis_html(q['visual']) if q.get('visual') else ''
    if q.get('visuals'):      # two or more pictures in one question, side by side
        k = len(q['visuals'])
        vis += f'<div class="visrow" style="--n:{k}">' + ''.join(_vis_html(v) for v in q['visuals']) + '</div>'
    parts = ''
    if q.get('parts'):
        for p in q['parts']:
            cw = choice_words(p['text'], p.get('choices'))
            parts += f'<div class="sub"><span class="sl">{E("(" + p["l"] + ")") if p["l"] else ""}</span><span>{blanks(p["text"])}</span>{choice_html(cw) if cw else ""}</div>'
    if q.get('draw'):
        nd = q['draw'] if isinstance(q['draw'], int) and not isinstance(q['draw'], bool) else 1
        vis += ''.join('<div class="draw" style="height:%dpx"></div>' % (105 if nd == 1 else 70) for _ in range(nd))
    if q.get('tf'):           # statement / True / False with tick boxes
        rows = ''.join(f'<tr><td>{blanks(r["s"])}</td><td class="tk"><i class="bx"></i></td><td class="tk"><i class="bx"></i></td></tr>' for r in q['tf'])
        parts += f'<table class="tf"><tr><th>Statement</th><th>True</th><th>False</th></tr>{rows}</table><div class="pins2">Put a tick (\u2713) in the correct box.</div>'
    if q.get('mcq'):          # options (1) to (4) with a bracket at the right margin
        opts = ''.join(f'<div class="mo"><span class="mn">({i})</span><span>{blanks(str(o))}</span></div>' for i, o in enumerate(q['mcq']['options'], 1))
        parts += f'<div class="mcq"><div>{opts}</div>' + ('<span class="mbr">(&nbsp;&nbsp;&nbsp;&nbsp;)</span>' if q['mcq'].get('bracket', True) else '') + '</div>'
    ln = ''.join('<div class="ln"></div>' for _ in range(q.get('lines', 0)))
    if q.get('steps'):        # labelled step lines
        ln += ''.join(f'<div class="stp"><b>{E(s)}</b><span class="ln" style="flex:1"></span></div>' for s in q['steps'])
    cq = choice_words(q['text'], q.get('choices'))
    if cq and not any(choice_words(p['text'], p.get('choices')) for p in q.get('parts', [])): parts += f'<div class="sub">{choice_html(cq)}</div>'
    return f'<div class="qbox"><div class="q"><span class="qn">{lab}</span><span class="qt">{blanks(q["text"])}</span></div>{vis}{parts}{ln}</div>'


NONCUT_KITS = {'hundred', 'hundred_square', 'groups_mat', 'array_mat', 'number_line', 'plates', 'grid_mat', 'graph_mat'}


def kit_note(k, d=None):
    """The same practical advice on every kit page: one side only, who cuts, where the pieces live. "We use them again" only when a later lesson does."""
    if k.get('type') in NONCUT_KITS:
        return 'No cutting needed: keep this page flat to use in the lesson. Print it on its own sheet, or on one side only.'
    import figs3
    reuse = figs3.kit_reused(k) if (k.get('type') in figs3.KITS3 or (d or {}).get('term', 1) >= 3) else True        # Term 1 and 2 kits keep the old sentence
    return ('Print this page on its own sheet, or on one side only, so cutting never spoils another page. A grown-up cuts; children do not use scissors. '
            'Keep the pieces in an envelope with your name.' + (' We use them again.' if reuse else ''))


def kit_pages(d):
    """One printed page for each page of a kit (a kit such as the fold shapes can need more than one)."""
    import figs3
    out = []
    for k in kits(d):
        figs = svg.kit_figure(k).split(figs3.KIT_SEP)
        style = figs3.kit_style(k) if k.get('type') in figs3.KITS3 else f'width:{k.get("width", 84)}%'
        for i, fg in enumerate(figs):
            title = k.get('title', 'Kit page') + (f' (page {i + 1} of {len(figs)})' if len(figs) > 1 else '')
            intro = f'<p style="font-size:13.5px;margin:2px 0 3px">{E(k.get("intro", "A grown-up cuts these out before the lesson."))}</p><p style="font-size:12px;margin:0 0 6px;color:#3B4A6B"><b>{E(kit_note(k, d))}</b></p>' if i == 0 else \
                '<p style="font-size:12px;margin:2px 0 6px;color:#3B4A6B"><b>More pieces: the same kit, cut out the same way.</b></p>'
            out.append(f'<div class="page kit">{hdr(d, "Kit")}<div class="ltitle" style="font-size:24px">{E(title)}</div>{intro}<div style="{style}">{fg}</div></div>')
    return out


def workbook_html(d, key=False):
    t = d['tiers']; inv = t['investigation']
    P = []
    P.append(f'<div class="page p1">{hdr(d, "Start here", d["title"].upper() + "!", mi=True)}<div class="choice">After question {wb(d, "choice_after", 3)} you may choose: carry on, or try <b>Think harder</b>.</div><p style="font-style:italic;margin:2px 0 6px">{E(wb(d, "hint_p1", "Use objects, your kit or a drawing. Say your answer out loud, then write it."))}</p>' + ''.join(qbox(q) for q in t['start'] if q['page'] == 1) + '</div>')
    P.append(f'<div class="page">{hdr(d, "Start here")}' + (f'<p style="font-style:italic;margin:2px 0 6px">{E(wb(d, "hint_p2"))}</p>' if wb(d, 'hint_p2') else '') + ''.join(qbox(q) for q in t['start'] if q['page'] == 2) + '</div>')
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
            '<div class="r"><b></b><span><i class="bx"></i>I am still stuck (my grown-up will photograph this page for my tutor)</span><span><i class="bx"></i>I would like to pass</span></div></div>')
    P.append(f'<div class="page p5">{hdr(d, "Choose, then look back")}<div class="banner">Investigation: {E(inv["title"])}</div><p style="font-style:italic;margin:2px 0">{E(wb(d, "inv_intro", "Try this any time. You do not have to finish."))}</p>'
             f'<p style="margin:3px 0"><b>{E(wb(d, "inv_first_label", "First, try this."))}</b> {E(inv["first"])}</p>{inv_vis(inv)}<p style="margin:3px 0"><b>{E(wb(d, "inv_then_label", "Next, try this."))}</b> {E(inv["text"])}</p>' + inv_draw(inv) + '<div class="ln"></div>' * d.get('_inv_lines', 4) +
             f'<div class="banner" style="margin-top:6px">Exit ticket</div><p style="font-style:italic;margin:2px 0">On your own, at the end of the lesson. No looking back.</p>{ex}{look}</div>')
    P += kit_pages(d)
    body = ''.join(P)
    for i in sorted(set(d.get('_tight', ())) | set(d.get('_tight2', ())) | set(d.get('_tight3', ())), reverse=True):    # pages measured over full get tighter spacing
        parts = body.split('<div class="page')
        if i + 1 < len(parts): parts[i + 1] = (' tight tight2 tight3' if i in d.get('_tight3', ()) else (' tight tight2' if i in d.get('_tight2', ()) else ' tight')) + parts[i + 1]
        body = '<div class="page'.join(parts)
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{font_css()}{WB_CSS}{EXTRA}</style></head><body>{body}</body></html>'


def key_html(d):
    t = d['tiers']; inv = t['investigation']
    P = [f'<h1 style="font-family:Fredoka;margin:0;color:#1B2A49">Answer key: Lesson {d["lesson_in_term"]}, {E(d["title"])}</h1><p style="font-size:13px;margin:2px 0 8px"><b>For the tutor and grown-ups.</b> Keep this page away from the child until they have finished and checked their own work. Ask <i>how do you know?</i> before saying right or wrong.</p>']
    def block(q):
        return (f'<div class="keybox"><b>{q["id"]}.</b> {blanks(q["text"])}<div class="a">Answer: {E(q["answer"])}</div><div style="font-size:12.5px">{E(q["solution"])}</div>'
                f'<div style="font-size:12px;color:#3B4A6B"><b>Watch for:</b> {"; ".join(E(m) for m in q["mistakes"])}</div></div>')
    P.append('<div class="banner">Start here (pages 1 and 2)</div>' + ''.join(block(q) for q in t['start']))
    P.append('<div class="banner">Think harder (page 3)</div>' + ''.join(block(q) for q in t['think']))
    P.append('<div class="banner">Go further (page 4)</div>' + ''.join(block(q) for q in t['go']))
    P.append(f'<div class="banner">Investigation (page 5): {E(inv["title"])}</div><div class="keybox"><div class="a">{E(inv["answer"])}</div><div style="font-size:12px"><b>Look for:</b> {E(inv["look_for"])}</div></div>')
    P.append('<div class="banner">Exit ticket (page 5)</div>' + ''.join(block(q) for q in d['exit']))
    P.append(f'<div class="banner">Sneak-peek puzzles (not in the workbook)</div><div class="keybox">1. {E(d["sneak_peek"]["a1"])}<br>2. {E(d["sneak_peek"]["a2"])}</div>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{font_css()}{WB_CSS}{EXTRA}body{{background-image:none}}</style></head><body>{"".join(P)}</body></html>'


def part_breaks(h):
    """Each part (b), (c), ... of a home question starts on its own line."""
    return re.sub(r'\s+\(([b-f])\)\s', r'<br>(\1) ', h)


def home_html(d, answers=False):
    """answers=False: the question sheet (one page). answers=True: the grown-up answers (one page), a separate PDF so a double-sided print never puts answers on the back of the questions."""
    H = d['home_practice']
    qs = ''
    for h in H:
        tag = {'start': 'Start here', 'think': 'Think harder', 'go': 'Go further'}[h['tier']]
        qs += f'<div class="qbox"><div class="q"><span class="qn">{h["id"][1:]}</span><span class="qt"><span style="font-size:12px;color:#1F7A6F;font-weight:800">{tag}{(" \u2022 Practice from earlier: " + E(h["rewind_of"])) if h.get("rewind_of") else ""}</span><br>{part_breaks(blanks(h["text"]))}</span></div>' + (f'<div class="sub">{choice_html(choice_words(h["text"], h.get("choices")))}</div>' if choice_words(h["text"], h.get("choices")) else '') + '<div class="ln"></div>' * (2 if h['id'] == 'H5' else 1) + '</div>'
    ans = ''.join(f'<div class="keybox"><b>{h["id"][1:]}.</b> <span class="a">{E(h["answer"])}</span><div style="font-size:12.5px">{E(h["solution"])}</div></div>' for h in H)
    if answers:
        page = (f'<div class="page">{hdr(d, "Answers", d["title"] + ": home practice answers")}<p style="font-size:13px">For grown-ups. Please let your child try first, then check together. Ask <i>how do you know?</i> If your child is stuck, wait 10 seconds, then suggest drawing it.</p>{ans}'
                f'<p style="font-size:12.5px;margin-top:10px">More practice online (no timers, no scores): ask your tutor for the practice link.</p></div>')
    else:
        page = f'<div class="page hm {("t" + str(d.get("_home_tight"))) if d.get("_home_tight") else ""}">{hdr(d, "Home practice", d["title"] + ": practice at home")}<p style="margin:2px 0 6px;font-size:14.5px">About 15 minutes, a few days after the lesson. {E(wb(d, "home_hint", "Use real things or draw it."))} A grown-up may read the questions aloud. Wrong answers are fine: they show what to try next. The answers are on a separate sheet, so they never print on the back of this one.</p>{qs}</div>'
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{font_css()}{WB_CSS}{EXTRA}</style></head><body>{page}</body></html>'


def parent_html(d):
    p = d['parent']
    li = lambda xs, cls='': ''.join(f'<li>{E(x)}</li>' for x in xs)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{font_css()}{PARENT_CSS}'
            '@page{size:A4;margin:12mm 15mm}body{font-size:%spx;line-height:%s}' % (('13.2', '1.38'), ('12.6', '1.3'), ('12', '1.25'))[min(d.get('_parent_tight', 0), 2)] + '.side h3{font-size:15px}.panel{padding:10px 14px;margin-bottom:10px}.panel h3{font-size:16px}.tips li{margin-bottom:6px}.hd{margin:0 0 10px}.big{font-size:60px}'
            f'</style></head><body><div class="hd"><img alt="Mi the dolphin" src="{mi_uri()}" style="width:22mm;height:auto"><div class="big">{d["lesson_in_term"]}</div><div><div class="tp">Level {d["level"]} • Term {d["term"]} • Lesson {d["lesson_in_term"]} • For parents</div><h1>{E(d["title"])}</h1></div></div>'
            f'<div class="cols"><div><div class="kick">What we did</div><p style="margin:3px 0 8px">{E(p["summary"] + ((" " + d["beyond"]["parent"]) if d.get("beyond", {}).get("parent") else ""))}</p>'
            f'<div class="quote">{E(p.get("quote") or d["big_idea"] + ".")}</div>'
            f'<div class="kick">Try at home (5 minutes)</div><ol class="tips">{li(p["try_home"])}</ol>'
            f'<div class="panel"><h3>When your child is stuck</h3><p style="margin:0">{E(p["when_stuck"])}</p></div></div>'
            f'<div><div class="side"><h3>Words we used</h3><ul style="margin:0;padding-left:16px">{li(p["words"])}</ul></div>'
            f'<div class="side" style="margin-top:12px"><h3>Good questions</h3><ul style="margin:0;padding-left:16px">{li(p["ask"])}</ul></div>'
            f'<div class="side" style="margin-top:12px"><h3>{"Have ready for next lesson" if p.get("next_materials") else "Things to have ready"}</h3><ul style="margin:0;padding-left:16px">{li(p["next_materials"] if isinstance(p.get("next_materials"), list) else ([p["next_materials"]] if p.get("next_materials") else d["materials"]["child"][:3]))}</ul></div></div></div>'
            f'<div class="panel"><h3>Next lesson</h3><p style="margin:0">{E(p["next"])} Missed a lesson? Every lesson is recorded; your tutor will share a private link with enrolled families.</p></div>'
            f'<p style="font-size:11.5px;color:#5B6785;margin:8px 0 0">{E(p["term_line"])} We share what we see in your child’s thinking, never a rank or a mark compared with other children. Math Inquirers by Preciouslyours Pte Ltd.</p></body></html>')


def build_print(d, pw):
    import pdfcheck
    page_fill(pw, d)
    od = outdir(d)
    n = d['_num']
    def render(name, html, footer, pdfname, fmt='A4'):
        hp = os.path.join(outdir(d, 'html'), name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg = pw.new_page(); pg.goto('file://' + hp, wait_until='networkidle'); pg.wait_for_timeout(500)
        foot = f'<div style="width:100%;font-size:9px;color:#5B6785;padding:0 14mm 3mm;display:flex;justify-content:space-between;font-family:Arial"><span>{footer}</span><span>Page <span class="pageNumber"></span></span></div>' if footer else '<div></div>'
        pg.pdf(path=os.path.join(od, pdfname), format=fmt, print_background=True, display_header_footer=bool(footer), header_template='<div></div>', footer_template=foot,
               margin={'top': '14mm', 'bottom': '16mm', 'left': '14mm', 'right': '14mm'} if footer else {'top': '12mm', 'bottom': '12mm', 'left': '15mm', 'right': '15mm'})
        pg.close()
        return os.path.join(od, pdfname)
    f = f'Math Inquirers Term {d["term"]} \u2022 Notice it. Test it. Explain why.'
    # workbook: re-render with tighter spacing on the overflowing page until the real PDF has exactly the designed pages
    want = workbook_html(d).count('<div class="page')
    d.setdefault('_tight', set()); d.setdefault('_tight2', set()); d.setdefault('_tight3', set())
    for attempt in range(8):
        path = render('workbook', workbook_html(d), f + f' \u2022 Lesson {d["lesson_in_term"]}', f'L{n}_Workbook.pdf')
        got = pdfcheck.pdf_pages(path)
        if got == want: break
        fills = pdfcheck.pdf_fill(path)
        bads = []; hi = -1                       # map PDF pages to designed pages: an orphan page belongs to the designed page before it
        for i, x in enumerate(fills):
            if x < 0.40 and i > 0 and fills[i - 1] >= 0.88: bads.append(hi)
            else: hi += 1
        bads = bads or [max(range(len(fills)), key=lambda i: fills[i])]
        for bad in bads:
            if bad in d['_tight2']: d['_tight3'].add(bad)
            if bad in d['_tight']: d['_tight2'].add(bad)
            d['_tight'].add(bad)
    if kits(d):          # a one-sided kit-only PDF, so the kit page is never the back of the exit-ticket page
        kp = workbook_html(d)
        head = kp[:kp.index('<body>') + 6]
        render('kit', head + ''.join(kit_pages(d)) + '</body></html>', f + f' \u2022 Lesson {d["lesson_in_term"]} \u2022 Kit (print one side only)', f'L{n}_Kit_Pages.pdf')
    render('workbook_key', key_html(d), f + ' \u2022 Answer key (tutor and grown-ups)', f'L{n}_Workbook_Answer_Key.pdf')
    for lvl in (0, 1, 2):
        d['_home_tight'] = lvl
        path = render('home', home_html(d), f + ' \u2022 Home practice', f'L{n}_Home_Practice.pdf')
        if pdfcheck.pdf_pages(path) == 1: break
    render('home_answers', home_html(d, True), f + ' \u2022 Home practice answers (grown-ups)', f'L{n}_Home_Answers.pdf')
    for lvl in (0, 1, 2):          # the one-page parent summary: shrink the type a little until it is one page
        d['_parent_tight'] = lvl
        path = render('parent', parent_html(d), '', f'L{n}_Parent_Summary.pdf')
        if pdfcheck.pdf_pages(path) == 1: break


def _measure(pw, d):
    hp = os.path.join(outdir(d, 'html'), 'workbook_fill.html')
    open(hp, 'w', encoding='utf-8').write(workbook_html(d))
    pg = pw.new_page(viewport={'width': 688, 'height': 1123})
    pg.goto('file://' + hp, wait_until='networkidle'); pg.wait_for_timeout(300)
    res = pg.evaluate("""() => Array.from(document.querySelectorAll('.page:not(.kit)')).map(p => {
        const top = p.getBoundingClientRect().top; let m = 0;
        Array.from(p.children).forEach(c => { m = Math.max(m, c.getBoundingClientRect().bottom - top); });
        return m / (267 / 25.4 * 96); })""")
    pg.close()
    return res


def page_fill(pw, d):
    """Fraction of the printable A4 height (267 mm) used by each workbook page except the kit page.
    Also chooses (1) how many writing lines the Investigation gets on page 5 (the most that still fit): d['_inv_lines'],
    (2) which pages are too full and get tighter spacing: d['_tight']."""
    d['_tight'] = set(); d['_inv_lines'] = 4
    for k in (6, 5, 4):
        d['_inv_lines'] = k
        fills = _measure(pw, d)
        if len(fills) < 5 or fills[4] <= 0.95:
            break
    fills = _measure(pw, d)
    over = {i for i, f in enumerate(fills) if f > 0.975}
    if over:
        d['_tight'] = over
        fills = _measure(pw, d)
    return fills
