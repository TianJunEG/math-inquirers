"""Data -> HTML for the extension workbooks (page bodies only; build.py wraps them in pages, numbers them and makes the PDFs)."""
import html, json, os, re, base64
import figs

HERE = os.path.dirname(os.path.abspath(__file__))
EXT = os.path.dirname(HERE)
ROOT = os.path.dirname(EXT)

TIER = {'start': ('Start here', 'S'), 'think': ('Think harder', 'T'), 'go': ('Go further', 'G'), 'quiz': ('Check yourself', 'C')}

ICON = {   # 24x24 icons: circle, diamond, star, tick
    'start': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" stroke-width="1"/></svg>',
    'think': '<svg viewBox="0 0 24 24"><path d="M12 1.5 22.5 12 12 22.5 1.5 12Z" stroke-width="1"/></svg>',
    'go': '<svg viewBox="0 0 24 24"><path d="M12 1.5l3.1 6.9 7.4.8-5.5 5 1.6 7.4L12 17.8 5.4 21.6 7 14.2 1.5 9.2l7.4-.8z" stroke-width="1"/></svg>',
    'quiz': '<svg viewBox="0 0 24 24"><path d="M3 13l6 6L21 5" fill="none" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}


def esc(s):
    return html.escape(str(s), quote=False)


def mk(text):
    """Inline markup: {b} answer box, {l} answer line, {circ:a|b|c} choices to circle, newline = line break."""
    t = esc(text)
    t = re.sub(r'\{circ:([^}]*)\}', lambda m: '<span class="circ">' + ''.join(f'<i>{o}</i>' for o in m.group(1).split('|')) + '</span>', t)
    t = t.replace('{b}', '<span class="abox"></span>').replace('{ll}', '<span class="aline long"></span>').replace('{l}', '<span class="aline"></span>')
    return t.replace('\n', '<br>')


def plain(text):
    """Text without markup, for lint / checks / answers."""
    t = re.sub(r'\{circ:([^}]*)\}', lambda m: ' / '.join(m.group(1).split('|')), text)
    return t.replace('{b}', '___').replace('{ll}', '___').replace('{l}', '___').replace('\n', ' ')


def data_uri(path):
    return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()


def badge(tier, n, theme):
    shape = {
        'start': '<circle cx="12" cy="12" r="11" />',
        'think': '<path d="M12 .8 23.2 12 12 23.2.8 12Z"/>',
        'go': '<path d="M12 .8l3.4 7.4 8 .9-6 5.4 1.7 8L12 18.5 4.9 22.5l1.7-8-6-5.4 8-.9z"/><circle cx="12" cy="13" r="6.2" fill="#fff" stroke="none"/>',
        'quiz': '<rect x="1.5" y="1.5" width="21" height="21" rx="4"/>',
    }[tier]
    fill = '#FFC93C' if theme == 'colour' else '#fff'
    return (f'<div class="badge"><svg viewBox="0 0 24 24"><g fill="{fill}" stroke="#{"1B2A49" if theme == "colour" else "000"}" stroke-width="1.5" stroke-linejoin="round">{shape}</g></svg>'
            f'<span style="{"font-size:10pt" if str(n) == "Try" else ""}">{n}</span></div>')


def fig_html(spec, theme):
    return f'<div class="fig">{figs.render(spec, theme)}</div>'


def space_html(sp):
    if not sp:
        return ''
    if 'table' in sp:
        t = sp['table']
        head = ''.join(f'<th>{esc(c)}</th>' for c in t['cols'])
        body = ''.join('<tr>' + '<td></td>' * len(t['cols']) + '</tr>' for _ in range(t['rows']))
        return f'<table class="wt"><tr>{head}</tr>{body}</table>'
    rows = []
    for r in sp['rows']:
        if '{' in r:
            rows.append(f'<div class="rw free">{mk(r)}</div>')
        elif r.startswith('Draw'):   # a drawing needs a blank strip, not one rule (audit 2, L5)
            rows.append(f'<div class="rw draw"><span class="rl">{esc(r)}</span><span class="rln"></span></div>')
        else:
            rows.append(f'<div class="rw"><span class="rl">{esc(r)}</span><span class="rln"></span></div>')
    return '<div class="rows">' + ''.join(rows) + '</div>'


def item_html(it, n, theme, hint=True, extra_cls=''):
    tier = it['tier']
    out = [f'<div class="item {extra_cls}" id="{it["id"]}">', badge(tier, n, theme)]
    if it.get('beyond'):
        out.append(f'<div class="beyond">&#9733; Beyond Level 1: {esc(it["beyond"])}</div>')
    out.append(f'<div class="stem">{mk(it["text"])}</div>')
    parts_html = ''
    if it.get('parts'):
        parts_html = '<div class="parts' + (' prow' if it.get('partsrow') else '') + '">' + ''.join(
            f'<div class="part"><span class="plab">{("(" + p["label"] + ")") if p["label"] else ""}</span><span>{mk(p["text"])}</span></div>' for p in it['parts']) + '</div>'
    if it.get('figure') and it.get('figside'):      # figure to the right of the answer parts (saves height)
        out.append(f'<div class="figside">{parts_html}{fig_html(it["figure"], theme)}</div>')
    else:
        if it.get('figure'):
            out.append(fig_html(it['figure'], theme))
        out.append(parts_html)
    out.append(space_html(it.get('space')))
    if hint and it.get('hint'):
        out.append(f'<div class="hint"><b>Hint.</b> {esc(it["hint"])}</div>')
    out.append('</div>')
    return ''.join(out)


def tier_banner(tier, sub=''):
    name = TIER[tier][0]
    return f'<div class="tier t-{tier}">{ICON[tier]}<span>{name}</span><small>{esc(sub)}</small></div>'


def head(unit, cfg):
    return (f'<div class="ph"><span class="lv">Level {unit["level"]}</span><span class="un">Unit {unit["unit"]} &middot; {esc(unit["title"])}</span>'
            f'<span class="nm">Name<i></i></span></div>')


def items_of(unit, tier, page=None):
    return [it for it in unit['items'] if it['tier'] == tier and (page is None or it['page'] == page)]


def worked_html(ex, theme, label):
    """A worked example box. Optional: figure, side (figure to the left of the steps), figure sizes come from the spec."""
    steps = ''.join(f'<li><span>{mk(s)}</span></li>' for s in ex['steps'])
    fig = fig_html(ex['figure'], theme) if ex.get('figure') else ''
    if ex.get('side') and fig:
        mid = f'<div class="exside"><div class="exfig">{fig}</div><ol class="steps">{steps}</ol></div>'
    else:
        mid = fig + f'<ol class="steps">{steps}</ol>'
    return (f'<div class="wex"><span class="tab">{label}</span><div class="stem">{mk(ex["problem"])}</div>{mid}'
            f'<div class="ansbar">Answer: {esc(ex["answer"])}</div></div>')


def facts_html(F, theme):
    body = ''
    if F.get('figure'):
        body += fig_html(F['figure'], theme)
    if F.get('lines'):
        body += '<ul>' + ''.join(f'<li>{mk(x)}</li>' for x in F['lines']) + '</ul>'
    return f'<div class="howto facts"><span class="tab">{esc(F["title"])}</span>{body}</div>'


def snug(unit, key):
    """Optional tighter spacing for one practice page (unit JSON: "snug": ["think", "start2", ...])."""
    return ' snug' if key in unit.get('snug', []) else ''


def unit_pages(unit, theme, cfg):
    """The seven pages of a unit as dicts {kind, label, body}."""
    L = unit['learn']; ex = L['example']
    pages = []
    # 1 learn it
    howto = ('<div class="howto"><span class="tab">' + esc(L["howto"]["title"]) + '</span><ol>'
             + ''.join(f'<li>{mk(s)}</li>' for s in L['howto']['steps']) + '</ol></div>')
    if L.get('facts'):
        cols = ' style="grid-template-columns:minmax(0,1fr) auto"' if L['facts'].get('figure') else ''   # a figure in the box sets its width
        row = f'<div class="two hf"{cols}>{howto}{facts_html(L["facts"], theme)}</div>'
    else:
        row = howto
    learn = [head(unit, cfg), '<div class="pbody learn' + (' tight' if L.get('tight') else '') + '">',
             f'<div class="h1">Learn it: {esc(unit["topic"])}</div>',
             f'<div class="goal"><b>My goal.</b> {esc(unit["goal"])}</div>',
             (f'<div class="lead">{mk(L["intro"])}</div>' if L.get('intro') else '')]
    w1 = worked_html(ex, theme, 'Worked example 1' if L.get('example2') else 'Worked example')
    if L.get('example2') and L.get('pair'):
        learn.append(f'<div class="two wexpair">{w1}{worked_html(L["example2"], theme, "Worked example 2")}</div>')
    else:
        learn.append(w1)
        if L.get('example2'):
            learn.append(worked_html(L['example2'], theme, 'Worked example 2'))
    learn.append(row)
    tr = L['try']
    learn.append('<div class="tryit"><div class="tier t-start" style="margin-bottom:2mm;font-size:14pt">' + ICON['start'] + '<span>Your turn</span><small>Answer at the back of the book.</small></div>'
                 + item_html(dict(tr, tier='start'), 'Try', theme, hint=False, extra_cls='trysz') + '</div>')
    learn.append('</div>')
    pages.append({'kind': 'learn', 'label': 'Learn it', 'body': ''.join(learn)})
    # 2-4 start here
    subs = {1: 'Do these first. Take your time.', 2: 'Keep going. Check your work.', 3: 'Nearly there. You can do it.'}
    cnt = 0
    for pn in (1, 2, 3):
        its = items_of(unit, 'start', pn)
        body = [head(unit, cfg), '<div class="pbody practice' + snug(unit, f'start{pn}') + '">', tier_banner('start', subs[pn])]
        for it in its:
            cnt += 1
            body.append(item_html(it, cnt, theme))
        body.append('</div>')
        pages.append({'kind': 'practice', 'label': f'Start here {pn}', 'body': ''.join(body)})
    # 5 think harder
    body = [head(unit, cfg), '<div class="pbody practice' + snug(unit, 'think') + '">', tier_banner('think', 'Hints are upside down. Try first!')]
    for i, it in enumerate(items_of(unit, 'think'), 1):
        body.append(item_html(it, i, theme))
    body.append('</div>')
    pages.append({'kind': 'practice', 'label': 'Think harder', 'body': ''.join(body)})
    # 6 go further
    body = [head(unit, cfg), '<div class="pbody practice' + snug(unit, 'go') + '">', tier_banner('go', 'A weekend page. Big challenges. Hints are upside down.')]
    for i, it in enumerate(items_of(unit, 'go'), 1):
        body.append(item_html(it, i, theme))
    body.append('</div>')
    pages.append({'kind': 'practice', 'label': 'Go further', 'body': ''.join(body)})
    # 7 check yourself
    qs = items_of(unit, 'quiz')
    body = [head(unit, cfg), '<div class="pbody practice' + snug(unit, 'quiz') + '">', tier_banner('quiz', 'No hints. Try each one on your own.')]
    for i, it in enumerate(qs, 1):
        it2 = it if it.get('figure') else dict(it, space={'rows': ['Working:']})   # a graph or picture item is answered in the box: no working line
        body.append(item_html(it2, i, theme, hint=False))
    body.append('<div class="score"><span>My score:</span><span class="abox"></span><span>out of 4. Check the answers at the back.</span></div>')
    body.append('<div class="box"><h3>What next?</h3><ul class="adv"><li><b>4 or 3:</b> well done! Go on to the next unit.</li>'
                '<li><b>2:</b> read Learn it again. Then try a Start here page once more.</li>'
                '<li><b>1 or 0:</b> do Learn it and Start here again with a helper. Then try Check yourself again.</li></ul></div>')
    body.append('<div class="box grow"><h3>Look back</h3><div class="rows"><div class="rw free">This unit was &nbsp;<span class="tickl"><span class="tick"></span> easy</span><span class="tickl"><span class="tick"></span> just right</span><span class="tickl"><span class="tick"></span> hard</span></div>'
                '<div class="rw"><span class="rl">The idea I want to remember:</span><span class="rln"></span></div>'
                '<div class="rw"><span class="rl">Something I want to ask or try:</span><span class="rln"></span></div></div></div>')
    body.append('</div>')
    pages.append({'kind': 'practice', 'label': 'Check yourself', 'body': ''.join(body)})
    return pages


def ans_text(it):
    if it.get('parts'):
        return ' '.join(f'<b>({p["label"]})</b> {esc(p["answer"]["text"])}' if p['label'] else esc(p['answer']['text']) for p in it['parts'])
    return esc(it['answer']['text'])


def answer_blocks(unit, start_pg=None):
    """Answer entries for the back of the book: list of html blocks (the unit heading is merged into the first entry)."""
    blocks = []
    head_html = f'<div class="ans-unit"><span>Unit {unit["unit"]} &middot; {esc(unit["title"])}</span></div>'
    L = unit['learn']['try']
    entries = [('Your turn', ans_text(L), L['explanation'], 'learn', 0, 0)]
    for tier in ('start', 'think', 'go', 'quiz'):
        for i, it in enumerate(items_of(unit, tier), 1):
            off = {'start': it.get('page', 1), 'think': 4, 'go': 5, 'quiz': 6}[tier]    # page of the item in the unit: Learn it is page 0
            entries.append((f'{TIER[tier][0]} {i}', ans_text(it), it['explanation'], tier, i, off))
    first = True
    prev_tier = None
    for e in entries:
        tier = e[3] if len(e) > 3 else 'learn'
        grp = ''
        if tier != prev_tier and tier != 'learn':
            grp = f'<div class="ans-grp">{TIER[tier][0]}</div>'
        prev_tier = tier
        label = e[0] if tier == 'learn' else f'{e[4]}'
        pg = f'<small>page {start_pg + e[5]}</small>' if start_pg else ''
        body = (f'<div class="ae"><div class="k">{label}{pg}</div><div class="a"><span class="ans"><b>Answer:</b> {e[1]}</span>'
                f'<span class="why">{esc(e[2])}</span></div></div>')
        blocks.append((head_html if first else '') + grp + body)
        first = False
    return blocks
