"""Strategy chip ("tool of the day"), tool row and COMMON LOOK-BACK for the Term-time Level 1 builders (term/l1).

Design: term/l1/SPINE_TERM_DESIGN.md.  Wording (tool names, definitions, look-back prompts) comes ONLY from levels/spine.json (band A, ages 6-8);
the choice of tool for each lesson comes from term/l1/spine_term.json and is copied into each lesson file as the `spine` object by tools/apply_spine_term.py.

Every function returns '' (or None) for a lesson that has no `spine` object, so a lesson file without it builds exactly as before.
No colour is used except ink on white (black-and-white print safe); icons are the stroke-only holiday icons (levels/spine_icons/*.svg).
"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(L1))
E = html.escape
INK = '#1B2A49'
CREAM = '#FFF9EC'
BAND = 'A'
STUCK = 'I am still stuck (my grown-up will photograph this page for my tutor)'   # same words as common.STUCK_TEXT (the WhatsApp route stays)

_SP = json.load(open(os.path.join(ROOT, 'levels', 'spine.json'), encoding='utf-8'))
_TERM = json.load(open(os.path.join(L1, 'spine_term.json'), encoding='utf-8'))
TOOLS = _SP['tools']
LB = _SP['lookback']
LABELS = _SP['card_labels']
PROMPTS = LB['prompts'][BAND]
_svg = {}


def tool(i):
    return next(t for t in TOOLS if t['id'] == i)


def icon(i, size, color=INK, unit='mm'):
    if i not in _svg:
        _svg[i] = re.sub(r'\s*\n\s*', ' ', open(os.path.join(ROOT, 'levels', 'spine_icons', i + '.svg'), encoding='utf-8').read().strip())
    s = _svg[i].replace('width="64" height="64"', f'width="{size}{unit}" height="{size}{unit}"', 1)
    return s.replace('<svg ', f'<svg style="color:{color};flex:none;display:block" ', 1)


def met(d):
    """The tools met so far in the lesson's term (consolidation plan: Term 1 four tools, Term 2 six, Term 3 seven, Term 4 eight), in levels/spine.json order."""
    ids = _TERM['tools_met'][str(d.get('term', 1))]
    return [t for t in TOOLS if t['id'] in ids]


def row(d):
    """The lesson's `spine` object ({main, also, role, reason[, chip]}) or None."""
    s = d.get('spine')
    if not s:
        return None
    return s


def info(d):
    s = row(d)
    if not s:
        return None
    ch = s['main'] == 'choose'
    t = None if ch else tool(s['main'])
    return {'row': s, 'choose': ch, 'tool': t, 'name': 'Choose one' if ch else t['name'], 'def': '' if ch else t['def'][BAND],
            'also': [tool(a) for a in s.get('also', [])], 'reason': s.get('reason', ''), 'role': s.get('role', '')}


def _tick(mm):
    return f'<span style="display:inline-block;width:{mm}mm;height:{mm}mm;border:0.5mm solid {INK};border-radius:0.6mm;background:#fff;flex:none"></span>'


BOX = f"border:0.5mm solid {INK};border-radius:1.5mm;background:#fff;color:{INK};font-family:'Nunito Sans',Arial,sans-serif;break-inside:avoid;"


# ------------------------------------------------------------------ workbook (b_print.py)

def wb_chip(d, compact=False):
    """Strategy chip under the name line on the Start-here page (inside the left column, beside Mi). `compact` = one row, no definition."""
    x = info(d)
    if not x:
        return ''
    if x['choose']:
        cells = ''.join(f'<span style="display:inline-flex;flex-direction:column;align-items:center;gap:0.3mm;flex:1 1 0;min-width:0"><span style="display:inline-flex;align-items:center;gap:0.6mm">{icon(t["id"], 7)}{_tick(3.2)}</span>'
                        f'<span style="font-size:{"13.4" if len(met(d)) <= 6 else "10.2"}pt;font-weight:700;line-height:1.05;text-align:center;overflow-wrap:normal">{E(t["name"])}</span></span>' for t in met(d))
        return (f'<div class="spchip" data-spine="chip" style="{BOX}margin:1.5mm 0 0;padding:1mm 2mm 1.2mm;display:flex;flex-direction:column;gap:0.8mm">'
                f'<span style="font-size:9pt;font-weight:800;letter-spacing:.05em">{LABELS["tool_of_day"]}: {LABELS["choose_one"]}. Tick the one you chose.</span>'
                f'<span style="display:flex;justify-content:space-between;gap:1mm">{cells}</span></div>')
    t = x['tool']
    also = ('<span style="font-size:10.5pt"><b>' + LABELS['also'].strip() + '</b> ' + ', '.join(E(a['name']) for a in x['also']) + '</span>') if x['also'] else ''
    used = f'<span style="display:inline-flex;align-items:center;gap:1mm;font-size:10.5pt;font-weight:700;white-space:nowrap">{_tick(3.6)}{LABELS["used"]}</span>'
    if compact:
        return (f'<div class="spchip" data-spine="chip" style="{BOX}margin:1.5mm 0 0;padding:0.6mm 2mm;display:flex;align-items:center;gap:2mm">'
                f'<span style="font-size:10.5pt;font-weight:800;letter-spacing:.05em;white-space:nowrap">{LABELS["tool_of_day"]}</span>{icon(t["id"], 7)}'
                f'<span style="font-family:Fredoka,Arial,sans-serif;font-size:12pt;font-weight:700;white-space:nowrap">{E(t["name"])}</span>{used}'
                f'<span style="margin-left:auto">{also}</span></div>')
    # two rows: label + name + tick, then the definition and the 'also' tools (about 11 mm high: it fits beside Mi, so the page grows by about nothing)
    return (f'<div class="spchip" data-spine="chip" style="{BOX}margin:1.5mm 0 0;padding:0.7mm 2.5mm;display:flex;gap:2.5mm;align-items:center">{icon(t["id"], 10)}'
            f'<div style="flex:1;min-width:0"><div style="display:flex;align-items:center;gap:2.5mm"><span style="font-size:10pt;font-weight:800;letter-spacing:.05em;white-space:nowrap">{LABELS["tool_of_day"]}</span>'
            f'<span style="font-family:Fredoka,Arial,sans-serif;font-size:13pt;font-weight:700;line-height:1.15;white-space:nowrap">{E(t["name"])}</span><span style="margin-left:auto">{used}</span></div>'
            f'<div style="font-size:10.5pt;line-height:1.2">{E(x["def"])}{(" &nbsp; " + also) if also else ""}</div></div></div>')


# Look-back box styles that follow the builder's tightening classes (tight, tight2, tight3 on the page): the box gets shorter exactly where the old one did.
CSS = """
.spl{border:0.5mm solid #1B2A49;border-radius:2mm;background:#fff;color:#1B2A49;font-family:'Nunito Sans',Arial,sans-serif;padding:2mm 4mm 2.2mm;margin-top:4mm;break-inside:avoid}
.spl .sph{display:flex;align-items:baseline;gap:3mm}.spl .sph b{font-family:Fredoka,Arial,sans-serif;font-weight:700;font-size:15pt}.spl .sph span{font-size:9pt}
.spl .spr{display:flex;align-items:center;gap:3mm;margin-top:1.5mm}.spl .spn{flex:none;width:6mm;height:6mm;border:0.5mm solid #1B2A49;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:800;font-size:10pt}
.spl .spq{flex:1;font-size:11pt;font-weight:700;line-height:1.15}.spl .spa{display:flex;align-items:center;gap:3mm;flex:none}.spl .spa3{width:70mm}
.spl .spt{display:flex;align-items:center;justify-content:space-between;gap:2mm;margin-top:2mm;border-top:0.4mm solid #1B2A49;padding-top:1.5mm}
.spl .sps{display:flex;gap:6mm;margin-top:1.2mm;font-size:9pt}
.tight .spl{margin-top:2.5mm;padding:1.4mm 3.5mm 1.5mm}.tight .spl .spr{margin-top:1mm}.tight .spl .spn{width:5.4mm;height:5.4mm}.tight .spl .spt{margin-top:1.4mm;padding-top:1mm}.tight .spl .spt svg{width:6.2mm;height:6.2mm}.tight .spl .sps{margin-top:0.8mm}
.tight2 .spl{margin-top:1.5mm;padding:1mm 3mm 1.1mm}.tight2 .spl .sph b{font-size:12.5pt}.tight2 .spl .spr{margin-top:0.5mm}.tight2 .spl .spq{font-size:10pt}.tight2 .spl .spn{width:5mm;height:5mm;font-size:9pt}.tight2 .spl .spt{margin-top:0.8mm;padding-top:0.6mm}.tight2 .spl .spt svg{width:5.4mm;height:5.4mm}.tight2 .spl .sps{margin-top:0.5mm;font-size:8.5pt}
.tight3 .spl{margin-top:1mm;padding:0.8mm 3mm 0.8mm}.tight3 .spl .sph b{font-size:11.5pt}.tight3 .spl .spr{margin-top:0.2mm}.tight3 .spl .spq{font-size:9.5pt}.tight3 .spl .spn{width:4.6mm;height:4.6mm}.tight3 .spl .spt{margin-top:0.5mm;padding-top:0.4mm}.tight3 .spl .spt svg{width:4.8mm;height:4.8mm}.tight3 .spl .sps{margin-top:0.3mm;font-size:8.5pt}
"""


def wb_lookback(d):
    """The common look-back box (replaces the old 'Something I did well / hardest / helped / next time' box). Same prompts in every lesson."""
    if not row(d):
        return ''
    dot = f'<span style="flex:1;border-bottom:0.4mm dotted {INK};height:5mm;min-width:18mm"></span>'
    yn = ''.join(f'<span style="display:inline-flex;align-items:center;gap:1mm;white-space:nowrap">{_tick(4)}<b style="font-size:10pt">{w}</b></span>' for w in ('yes', 'not yet'))
    def r(n, q, right):
        return f'<div class="spr"><span class="spn">{n}</span><span class="spq">{E(q)}</span><span class="spa{" spa3" if n == 3 else ""}">{right}</span></div>'
    a3 = f'<span style="font-size:9pt;white-space:nowrap">{E(LB["answer3"][BAND])}:</span>{dot}'
    mm = 7 if len(met(d)) > 6 else 8
    tools = ''.join(f'<span style="display:inline-flex;align-items:center;gap:1.2mm">{icon(t["id"], mm)}{_tick(3.6)}</span>' for t in met(d))
    return (f'<div class="spl" data-spine="lookback"><div class="sph"><b>Look back</b><span>{E(LB["intro"])}</span></div>'
            f'{r(1, PROMPTS[0], yn)}{r(2, PROMPTS[1], yn)}{r(3, PROMPTS[2], a3)}'
            f'<div class="spt"><b style="font-size:9pt;white-space:nowrap">{E(LB["footer_tools"])}:</b>{tools}</div>'
            f'<div class="sps"><span style="display:inline-flex;align-items:center;gap:1.2mm">{_tick(3.6)}{E(STUCK)}</span><span style="display:inline-flex;align-items:center;gap:1.2mm">{_tick(3.6)}{E(LB["pass"])}</span></div></div>')


def home_line(d):
    """One sentence for the home sheet's intro paragraph."""
    x = info(d)
    if not x:
        return ''
    if x['choose']:
        return 'In the lesson you chose your own tool. Which tool will you use today?'
    return f'The tool of the day was {x["name"]}. {x["def"]}'


# ------------------------------------------------------------------ tutor guide (b_guide.py)

def guide_row(d):
    """(label, html) for the 'At a glance' table, or None."""
    x = info(d)
    if not x:
        return None
    if x['choose']:
        body = (f'<b>Choose one.</b> No single tool of the day: the child picks from the {len(met(d))} tools met so far ({E(", ".join(t["name"] for t in met(d)))}) and ticks the one they used. {E(x["reason"])}')
    else:
        also = ('<br>Also useful: ' + ', '.join(E(a['name']) for a in x['also'])) if x['also'] else ''
        body = f'<b>{E(x["name"])}</b> <span class="small">({"introduced" if x["role"] == "I" else ("practised" if x["role"] == "P" else "applied")} in this lesson)</span>: {E(x["def"])}{also}<div class="small">{E(x["reason"])}</div>'
    return 'Tool of the day', body


def guide_lookback(d):
    """HTML for the guide's Look-back paragraph."""
    ps = '; '.join(f'<i>{E(p)}</i>' for p in PROMPTS)
    return (f'Children pick one problem from today and answer three questions: {ps}. They tick yes or not yet for questions 1 and 2, and write one word or draw for question 3. '
            f'Below that is the <i>{E(LB["footer_tools"])}</i> row (eight icons with tick boxes), then <i>{E(STUCK)}</i> and <i>{E(LB["pass"])}</i>. '
            'Never collected or read out in front of the group. A child who ticks still stuck gets a check-in in the open session next lesson.')


def guide_toolbox(d):
    """A compact box for the front matter: the eight tools in band A words (today's marked) and the three look-back questions. Same in every lesson."""
    x = info(d)
    if not x:
        return ''
    li = ''.join(f'<li><b>{E(t["name"])}</b>{" (today)" if (not x["choose"] and t["id"] == x["tool"]["id"]) else ""}: {E(t["def"][BAND])}</li>' for t in met(d))
    later = [t["name"] for t in TOOLS if t not in met(d)]
    qs = ''.join(f'<li>{E(q)}</li>' for q in PROMPTS)
    return (f'<div class="box t"><b>Toolbox so far this term and look-back (the same wording in every lesson)</b><div style="column-count:2;column-gap:18px;font-size:11.5px"><ul style="margin:3px 0 3px 16px">{li}</ul></div>'
            f'<div class="small"><b>Look-back, about 2 minutes, one problem from today:</b></div><ol style="margin:2px 0 2px 18px;font-size:11.5px">{qs}</ol>'
            f'<div class="small">The child ticks the tool used. Name the tool, not the answer, when you praise. {E(LB["intro"])}' + (f' Later terms add: {E(", ".join(later))}.' if later else '') + '</div></div>')


def lookback_lines():
    """Plain text for the look-back script lines and slide note (used by tools/apply_spine_term.py)."""
    T = _TERM
    return T['look_back']['say'], T['look_back']['do']


# ------------------------------------------------------------------ deck (b_deck.py)

def deck_chip(d):
    """'TODAY'S TOOL' pill at the bottom left of the title slide (dark background): cream stroke icon and the tool name. Absolutely placed (y 946-1016 px), below the card
    (the lowest content measured on the 40 title slides ends at y 910) and above the footer line, so the title block does not move."""
    x = info(d)
    if not x:
        return ''
    pill = 'data-spine="chip" style="position:absolute;left:128px;bottom:62px;background:#26385F;border-radius:999px;padding:8px 30px 8px 18px;display:flex;align-items:center;gap:18px;color:#FFF9EC"'
    if x['choose']:
        ics = ''.join(icon(t['id'], 40, CREAM, 'px') for t in met(d))
        return f'<div {pill}><p style="font-size:26px;font-weight:800;letter-spacing:3px;color:#FFC93C">TODAY\'S TOOL</p><p style="font-size:34px;font-weight:700">You choose</p><div style="display:flex;gap:8px">{ics}</div></div>'
    return f'<div {pill}>{icon(x["tool"]["id"], 52, CREAM, "px")}<p style="font-size:26px;font-weight:800;letter-spacing:3px;color:#FFC93C">TODAY\'S TOOL</p><p style="font-size:38px;font-weight:700">{E(x["name"])}</p></div>'


def deck_lookback(d, NAVY, TEAL, MUTED, CARD, chip):
    """Look-back slide body (replaces b_deck.lookback): three prompts, 'Tool I used' row, stuck and pass. `chip` is b_deck.chip."""
    if not row(d):
        return None
    box = lambda: f'<span style="display:inline-block;width:0.8em;height:0.8em;border:3px solid {NAVY};border-radius:8px;background:#fff;margin-right:12px;vertical-align:-0.05em"></span>'
    rows = ''
    for k, q in enumerate(PROMPTS, 1):
        ans = (f'<span style="white-space:nowrap">{box()}yes &nbsp; {box()}not yet</span>' if k < 3 else f'<span style="color:{MUTED}">{E(LB["answer3"][BAND])}</span>')
        rows += (f'<div style="display:flex;gap:28px;align-items:center;padding:16px 0;{"border-top:2px solid #DCE4F0;" if k > 1 else ""}"><span style="flex:none;width:70px;height:70px;border-radius:50%;border:3px solid {NAVY};display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:800">{k}</span>'
                 f'<p style="flex:1;font-size:50px;font-weight:700;line-height:1.2">{E(q)}</p><p style="font-size:34px;font-weight:600">{ans}</p></div>')
    ics = ''.join(f'<span style="display:inline-flex;align-items:center;gap:8px">{icon(t["id"], 78, NAVY, "px")}{box()}</span>' for t in met(d))
    foot = (f'<div style="display:flex;align-items:center;gap:22px;border-top:2px solid #DCE4F0;padding-top:14px"><p style="font-size:34px;font-weight:800;color:{TEAL};flex:none">{E(LB["footer_tools"])}</p><div style="display:flex;gap:18px;flex-wrap:wrap">{ics}</div></div>'
            f'<p style="font-size:32px;font-weight:600">{box()}{E(STUCK)} &nbsp;&nbsp; {box()}{E(LB["pass"])}</p>')
    return chip('Three minutes. ' + LB['intro'], 30) + f'<div style="{CARD}padding:20px 44px;display:flex;flex-direction:column;gap:10px;max-width:1560px">{rows}{foot}</div>'
