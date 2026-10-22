"""Tutor guide chapter builder: JSON -> HTML + PDF (A4). Timings, time-stamped script, recording cues, answers, slide list."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *  # noqa
import svg

CSS = """
@page{size:A4;margin:15mm 14mm 17mm 14mm}
*{box-sizing:border-box}
body{margin:0;font-family:'Nunito Sans',Arial,sans-serif;color:#1B2A49;font-size:12.5px;line-height:1.42;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2,h3{font-family:'Fredoka',Arial,sans-serif;font-weight:600;margin:0}
h1{font-size:34px;line-height:1.05}
h2{font-size:21px;color:#1F7A6F;border-bottom:3px solid #FFC93C;padding-bottom:3px;margin:20px 0 8px;break-after:avoid}
h3{font-size:15px;margin:12px 0 4px;break-after:avoid}
.pb{break-before:page}
.cover{background:#1B2A49;color:#FFF9EC;border-radius:18px;padding:26px 28px;margin-bottom:14px}
.cover .k{color:#FFC93C;font-weight:800;letter-spacing:.14em;font-size:11px}
.cover h1{color:#fff;font-size:44px;margin:6px 0}
.cover p{margin:4px 130px 4px 0;font-size:14px}
table{border-collapse:collapse;width:100%;margin:6px 0;font-size:11.8px}
th{background:#FFC93C;text-align:left;padding:4px 7px;border:1px solid #1B2A49}
td{padding:4px 7px;border:1px solid #C9D4EC;vertical-align:top}
tr{break-inside:avoid}
.box{border:2px solid #1B2A49;border-radius:10px;padding:8px 12px;margin:8px 0;background:#FFFDF5;break-inside:avoid}
.box.t{border-color:#1F7A6F;background:#E8F5F2}
.box.r{border-color:#D64545;background:#FDF0F0}
.seg{margin:14px 0 4px;display:flex;gap:10px;align-items:center;break-after:avoid}
.seg .tm{background:#1F7A6F;color:#fff;border-radius:999px;padding:3px 12px;font-weight:800;font-size:12px;white-space:nowrap}
.seg .nm{font-family:'Fredoka';font-size:17px;font-weight:600}
.seg .fit{margin-left:auto;font-size:11px;color:#3B4A6B}
.ln{display:grid;grid-template-columns:44px 52px 1fr;gap:6px;padding:3px 0;border-bottom:1px dotted #C9D4EC;break-inside:avoid}
.ln .ts{font-variant-numeric:tabular-nums;color:#5B6785;font-size:11px}
.ln .kd{font-weight:800;font-size:10.5px;letter-spacing:.04em;color:#1F7A6F}
.ln.REC{background:#FFF4D1}.ln.REC .kd{color:#9A6B00}.ln.REC .tx{font-style:italic}
.ln.STUCK{background:#FDF0F0}.ln.STUCK .kd{color:#D64545}
.ln.NOTE{background:#F3F6FA}.ln.NOTE .kd{color:#3B4A6B}
.ln.opt{opacity:.8}
.q{border:1.5px solid #1B2A49;border-radius:8px;padding:6px 10px;margin:6px 0;break-inside:avoid}
.q .h{display:flex;gap:8px;align-items:baseline}.q .id{background:#FFC93C;border:1.5px solid #1B2A49;border-radius:3px;padding:0 8px;font-weight:800;font-family:Fredoka}
.q .a{background:#E8F5F2;border-left:4px solid #1F7A6F;padding:2px 8px;margin:4px 0;font-weight:700}
.q .m{font-size:11.5px;color:#3B4A6B}
.vis{width:150px;float:right;margin-left:10px}
.small{font-size:11px;color:#3B4A6B}
ul{margin:3px 0 3px 16px;padding:0}li{margin:1px 0}
.ok{color:#1F7A6F;font-weight:800}.bad{color:#D64545;font-weight:800}
"""


def flat(blocks):
    out = []
    for b in blocks:
        t = b['t']
        if t in ('chip', 'p', 'say', 'answer'): out.append(b['text'])
        elif t == 'list': out += b['items']
        elif t == 'card': out += ([b['head'] + ':'] if b.get('head') else []) + b['items']
        elif t == 'numrow': out.append(' '.join(str(i) for i in b['items']))
        elif t == 'table': out += [' | '.join(r) for r in b['rows']]
        elif t == 'visual': out.append('[picture: ' + b['type'] + (f" {b.get('tens', '')} tens {b.get('ones', '')} ones" if b['type'] == 'bundles' else '') + ']')
        elif t in ('qs', 'answers'): out.append(('questions ' if t == 'qs' else 'answers ') + ', '.join(b['ids']))
        elif t == 'cols':
            for c in b['cols']: out += flat(c)
        elif t == 'lookback': out.append('[look-back box]')
    return out


def line_html(d, part, t0, sec, ln, sm):
    k = ln['k']
    txt = resolve_text(d, part, ln)
    if k == 'SLIDE':
        s = sm[ln['slide']]
        txt = f'Show slide <b>{E(s["title"])}</b> <span class="small">({E(ln["slide"])})</span>' + (' <i>(optional)</i>' if ln.get('optional') else '')
    else:
        txt = E(txt)
    kd = {'SAY': 'SAY', 'READ': 'READ', 'ASK': 'ASK', 'DO': 'DO', 'WORK': 'CHILDREN', 'HOLD': 'HOLD UP', 'MOVE': 'MOVE', 'REC': 'REC', 'STUCK': 'IF STUCK', 'NOTE': 'NOTE', 'SLIDE': 'SLIDE'}[k]
    extra = ''
    if k == 'ASK': extra = f' <span class="small">[wait about {ln.get("resp", ASK_RESP_S)} s for answers]</span>'
    if k in ('WORK', 'DO'): extra = f' <span class="small">[{mmss(ln["s"])}]</span>'
    ts = mmss(t0) if k not in ('STUCK', 'NOTE') and not ln.get('optional') else ''
    return f'<div class="ln {k}{" opt" if ln.get("optional") else ""}"><span class="ts">{ts}</span><span class="kd">{kd}</span><span class="tx">{txt}{extra}</span></div>'


def q_html(q, tier_label=None):
    vis = f'<div class="vis">{svg.render_visual(q["visual"])}</div>' if q.get('visual') else ''
    parts = ''.join(f'<div class="small">{E(p["l"] + ")  " if p["l"] else "")}{E(p["text"])}</div>' for p in q.get('parts', []))
    h = f'<div class="h"><span class="id">{q["id"]}</span><b>{E(q["text"])}</b></div>'
    inner = f'{vis}{h}{parts}<div class="a">Answer: {E(q["answer"])}</div>'
    if q.get('hint'): inner += f'<div class="m"><b>Hint (say this first):</b> {E(q["hint"])}</div>'
    inner += f'<div class="m"><b>Worked solution:</b> {E(q["solution"])}</div>'
    inner += '<div class="m"><b>Common mistakes:</b> ' + '; '.join(E(m) for m in q['mistakes']) + '</div>'
    if q.get('mins'): inner += f'<div class="small">Time for a middle child: about {q["mins"]} min.</div>'
    return f'<div class="q">{inner}</div>'


def build_html(d):
    sm = slide_map(d); pm = part_map(d); segs = segment_timeline(d)
    used = sum(s['used'] for s in segs); slow = sum(slow_used(s) for s in segs)
    H = []
    H.append(f'<div class="cover" style="position:relative"><img alt="Mi the dolphin" src="{mi_uri()}" style="position:absolute;right:22px;top:14px;width:110px"><div class="k">TUTOR GUIDE • LEVEL {d["level"]} • TERM {d["term"]} • LESSON {d["lesson_in_term"]} OF 10</div><h1>{E(d["title"])}</h1><p><b>Big idea:</b> {E(d["big_idea"])}. {E(d["child_idea"])}</p><p>90 minutes • live online or face to face • up to 8 children • ages {d["ages"]} • Notice it. Test it. Explain why.</p></div>')
    H.append('<h2>1. At a glance</h2><table>')
    rows = [('Strand', E(d['moe']['strand']) + ' (' + '; '.join(E(x) for x in d['moe']['topics']) + ')<div class="small">' + E(d['moe']['note']) + '</div>'),
            ('Objectives', '<ul>' + ''.join(f'<li>{E(o)}</li>' for o in d['objectives']) + '</ul>'),
            ('Joining cold', '<b>Remember warm-up covers:</b> ' + '; '.join(E(x) for x in d['joining_cold']['remember']) + '.<br>' + E(d['joining_cold']['assumes']) + '<br><span class="small">' + E(d['joining_cold']['note']) + '</span>'),
            ('Child materials', '<ul>' + ''.join(f'<li>{E(x)}</li>' for x in d['materials']['child']) + '</ul>'),
            ('Tutor materials', '<ul>' + ''.join(f'<li>{E(x)}</li>' for x in d['materials']['tutor']) + '</ul><div class="small">' + E(d['materials']['notes']) + '</div>'),
            ('Tiers', 'Start here (' + str(len(d['tiers']['start'])) + ' questions, pages 1 and 2), Think harder (' + str(len(d['tiers']['think'])) + ', page 3), Go further (' + str(len(d['tiers']['go'])) + ', page 4), Investigation and look-back (page 5), kit page (page 6). Labels are neutral; nobody is told which page they are on.'),
            ('Contest-style move', 'Used at Think harder only: ' + '; '.join(E(x) for x in d['contest_moves']) + '. Never advertised to children or parents.')]
    for a, b in rows: H.append(f'<tr><th style="width:110px">{a}</th><td>{b}</td></tr>')
    H.append('</table>')
    H.append('<div class="box t"><b>Before the lesson</b><ul>' + ''.join(f'<li>{E(x)}</li>' for x in d['tutor_prep']) + '</ul></div>')
    H.append('<div class="box r"><b>Safeguarding and recording (this lesson)</b><ul>' + ''.join(f'<li>{E(x)}</li>' for x in d['safeguarding']) + '</ul></div>')
    # timing table
    H.append('<h2>2. Timing plan (90 minutes exactly)</h2><table><tr><th>Minutes</th><th>Part</th><th>Min</th><th>Slides</th><th>Script fills</th></tr>')
    seg_by = {s['part']: s for s in segs}
    for p in d['timing']['parts']:
        sl = [s['title'] for s in d['slides'] if s['part'] == p['id'] and not s.get('optional')]
        H.append(f'<tr><td>{p["start"]}–{p["end"]}</td><td><b>{E(p["title"])}</b></td><td>{p["end"] - p["start"]}</td><td class="small">{len(sl)}: {E(", ".join(sl))}</td><td>{mmss(seg_by[p["id"]]["used"])}</td></tr>')
    H.append(f'<tr><td></td><td><b>Total</b></td><td><b>{sum(p["end"] - p["start"] for p in d["timing"]["parts"])}</b></td><td></td><td><b>{mmss(used)}</b></td></tr></table>')
    H.append(f'<p class="small">The script needs {mmss(used)} of the 90:00 when children are quick. A slow class (speech 10% slower, children and slide changes 20% slower) needs {mmss(slow)}. The last 5 minutes are a standing buffer: if you are behind, use them; do not start anything new. Clock checks: minute 14 (end of sneak-peek), minute 42 (start of workbook), minute 70 (talk time). If more than 2 minutes behind at minute 42, skip in this order: quick questions in Remember, the last explore number, the quick-fire in the mini-lesson, the optional slide. Never skip the look-back or the camera and privacy moments.</p>')
    # scripts
    H.append('<h2 class="pb">3. Lesson script</h2><p class="small">Times show when each line should start, counted from the start of the lesson, if you keep to the script. SAY lines are spoken in your own words. REC lines are the short recording-voice cues for children who watch later. Children answer aloud, with fingers or hands; no private chat; no boards held up in front of the group.</p>')
    for s in segs:
        p = pm[s['part']]
        H.append(f'<div class="seg"><span class="tm">{p["start"]}:00 – {p["end"]}:00</span><span class="nm">{E(p["title"])}</span><span class="fit">script {mmss(s["used"])} of {mmss(s["alloc"])}</span></div>')
        for (t0, sec, ln) in s['lines']:
            H.append(line_html(d, s['part'], t0, sec, ln, sm))
    sp = d['spare_time']
    H.append('<h2>3b. Spare-time menu: if the class is ahead</h2><div class="box t"><ul>' + ''.join(f'<li>{E(r)}</li>' for r in sp['rules']) + f'</ul><div class="small">{E(sp["note"])}</div></div><table><tr><th>Activity</th><th>Minutes</th><th>You say</th><th>Recording cue</th><th>Answer</th></tr>')
    for m in sp['menu']:
        H.append(f'<tr><td><b>{E(m["title"])}</b></td><td>{m["minutes"]} (optional)</td><td>{E(m["tutor"])}</td><td><i>{E(m["rec"])}</i></td><td>{E(m["answer"])}</td></tr>')
    H.append('</table>')
    # questions
    H.append('<h2 class="pb">4. Questions, answers, hints and common mistakes</h2>')
    sp = d['sneak_peek']
    H.append(f'<h3>Sneak-peek puzzles (minutes 10 to 14)</h3><div class="q"><b>Puzzle 1 (access):</b> {E(sp["q1"])}<div class="a">Answer: {E(sp["a1"])}</div><b>Puzzle 2 (think):</b> {E(sp["q2"])}<div class="a">Answer: {E(sp["a2"])}</div><div class="m">Unmarked. Papers are shown to the camera once, together. Reveal puzzle 2 in Talk time.</div></div>')
    H.append('<h3>Start here (workbook pages 1 and 2)</h3>')
    for q in d['tiers']['start']: H.append(q_html(q))
    H.append('<h3>Think harder (page 3): the taught idea in a new setting</h3>')
    for q in d['tiers']['think']: H.append(q_html(q))
    H.append('<h3>Go further (page 4): mastery and extension</h3>')
    for q in d['tiers']['go']: H.append(q_html(q))
    inv = d['tiers']['investigation']
    H.append(f'<h3>Investigation (page 5): {E(inv["title"])}</h3><div class="q"><b>Easy first step:</b> {E(inv["first"])}<br><b>Then:</b> {E(inv["text"])}<div class="a">Model answer: {E(inv["answer"])}</div><div class="m"><b>Look for:</b> {E(inv["look_for"])}</div><div class="m"><b>Common mistakes:</b> {"; ".join(E(m) for m in inv["mistakes"])}</div></div>')
    tk = d['talk']
    H.append(f'<h3>Talk and explain (minutes 70 to 76)</h3><div class="q"><b>{E(tk["question"])}</b> <span class="small">Sentence starter: {E(tk["starter"])}</span><div class="a">Model answer: {E(tk["answer"])}</div><div class="m"><b>Look for:</b> {E(tk["look_for"])} Volunteers first, a pass is always fine, never call a child by name to answer, no tallies.</div></div>')
    H.append('<h3>Exit ticket (minutes 76 to 82): 3 questions</h3>')
    for q in d['exit']: H.append(q_html(dict(q, hint='', mins=None)))
    lb = d['look_back']
    H.append('<h3>Look-back (minutes 82 to 85)</h3><div class="q">Children tick or write: <i>Something I did well</i>; <i>The hardest part was</i> (' + '; '.join(E(x) for x in lb['hardest']) + '); <i>What helped me</i> (' + '; '.join(E(x) for x in lb['helped']) + '); <i>Next time I will try</i> (' + '; '.join(E(x) for x in lb['next']) + '); <i>I am still stuck (my tutor will come and help)</i> and <i>I would like to pass</i>. Never collected or read out in front of the group. A child who ticks still stuck gets a check-in in the open session next lesson.</div>')
    H.append('<h2>5. Home practice and online practice</h2><table><tr><th>#</th><th>Tier</th><th>Question</th><th>Answer</th></tr>')
    for h in d['home_practice']: H.append(f'<tr><td>{h["id"]}</td><td>{TIER_NAME[h["tier"]]}</td><td>{E(h["text"])}</td><td>{E(h["answer"])}</td></tr>')
    H.append('</table>')
    op = d['online_practice']
    H.append(f'<p class="small">Online practice (<code>out/l{d["_num"]}/practice</code>, key <code>{op["key"]}</code>): {len(op["items"])} items; {sum(1 for i in op["items"] if "tpl" in i)} have a template that makes unlimited similar questions with a computed answer. Every template variant is checked by the validator against a brute-force oracle and the runner’s own JavaScript. No timers, no scores, no streaks.</p>')
    H.append('<h2>6. Parent line for the term report</h2><div class="box">' + E(d['parent']['report_line']) + '<div class="small">Term line (plan, section 5): ' + E(d['parent']['term_line']) + ' Add one named strength and one next step from your own observation. No marks, no ranking, no claim of exam results.</div></div>')
    # slides
    H.append('<h2 class="pb">7. Slide list</h2><table><tr><th>#</th><th>Time</th><th>Slide</th><th>On screen</th><th>Speaker note</th></tr>')
    for i, s in enumerate(d['slides'], 1):
        tm = 'optional' if s.get('optional') else f'{pm[s["part"]]["start"]}–{pm[s["part"]]["end"]}'
        H.append(f'<tr><td>{i}</td><td>{tm}</td><td><b>{E(s["title"])}</b><div class="small">{E(s["id"])}</div></td><td class="small">{E(" / ".join(flat(s["blocks"])))}</td><td class="small">{E(s["note"])}</td></tr>')
    H.append('</table>')
    # recording chapters
    H.append('<h2>8. Recording cues and chapter markers</h2><p class="small">Say each cue once, to the camera, at the start of the part. Add a chapter marker at each time. A child watching alone cannot ask you a question, so say the page and question number aloud, read each question and each answer aloud, and repeat a child’s answer in your own words.</p><table><tr><th>Chapter</th><th>Part</th><th>You say (recording voice)</th><th>A child watching later</th></tr>')
    for p in d['timing']['parts']:
        r = d['rec'][p['id']]
        H.append(f'<tr><td>{p["start"]}:00</td><td>{E(p["title"])}</td><td><i>{E(r["say"])}</i></td><td>{E(r["action"])}</td></tr>')
    H.append('</table>')
    # timing appendix
    H.append('<h2>9. Timing check (model, not a stopwatch)</h2><table><tr><th>Part</th><th>Allocated</th><th>Script</th><th>Slow class</th><th>Flag</th></tr>')
    for (p, a, u, sl, fl) in d['_timing_rows']:
        H.append(f'<tr><td>{p}</td><td>{mmss(a)}</td><td>{mmss(u)}</td><td>{mmss(sl)}</td><td>{fl}</td></tr>')
    H.append(f'<tr><td><b>Total</b></td><td>90:00</td><td>{mmss(used)}</td><td>{mmss(slow)}</td><td></td></tr></table>')
    ci = child_item_table(d)
    H.append(f'<p class="small">Assumptions as docs/audit/timing_p1.md: speech 120 words a minute, read-aloud 110, slide change 25 s, a group question 10 s thinking plus 20 s answers, papers to the camera 30 s. Workbook: Start here has {ci["n"]} questions; a middle child needs about {ci["p1"]:.1f} min for page 1 and {ci["p2"]:.1f} min for page 2 (a slower child about 1.7 times as long, so may finish page 1 and part of page 2; that is fine, the check-together slides cover every answer). The lesson has no breakout rooms, so no breakout time is counted.</p>')
    body = ''.join(H)
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Tutor guide: Lesson {d["lesson_in_term"]} {E(d["title"])}</title><style>{font_css()}{CSS}</style></head><body>{body}</body></html>'


def build_guide(d, pw=None):
    od = outdir(d)
    html = build_html(d)
    hp = os.path.join(od, f'L{d["_num"]}_Tutor_Guide.html')
    open(hp, 'w', encoding='utf-8').write(html)
    if pw:
        pg = pw.new_page(); pg.goto('file://' + hp, wait_until='networkidle'); pg.wait_for_timeout(500)
        foot = f'<div style="width:100%;font-size:8.5px;color:#5B6785;padding:0 14mm;display:flex;justify-content:space-between;font-family:Arial"><span>Math Inquirers Term 1 • Level 1 • Lesson {d["lesson_in_term"]}: {d["title"]} • Tutor guide</span><span>Page <span class="pageNumber"></span></span></div>'
        pg.pdf(path=os.path.join(od, f'L{d["_num"]}_Tutor_Guide.pdf'), format='A4', print_background=True, display_header_footer=True, header_template='<div></div>', footer_template=foot, margin={'top': '15mm', 'bottom': '17mm', 'left': '14mm', 'right': '14mm'})
        pg.close()
