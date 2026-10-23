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


def row(d):
    """The lesson's `spine` object ({main, also, role, reason[, lean_now]}) or None."""
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
            'also': [tool(a) for a in s.get('also', [])], 'reason': s.get('reason', ''), 'role': s.get('role', ''),
            'lean': [tool(a) for a in s.get('lean_now', [])]}


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
        cells = ''.join(f'<span style="display:inline-flex;align-items:center;gap:0.6mm">{icon(t["id"], 7)}{_tick(3.2)}</span>' for t in TOOLS)
        return (f'<div class="spchip" data-spine="chip" style="{BOX}margin:1.5mm 0 0;padding:1mm 2mm 1.2mm;display:flex;flex-direction:column;gap:0.8mm">'
                f'<span style="font-size:9pt;font-weight:800;letter-spacing:.05em">{LABELS["tool_of_day"]}: {LABELS["choose_one"]}. Tick the one you chose.</span>'
                f'<span style="display:flex;justify-content:space-between">{cells}</span></div>')
    t = x['tool']
    also = ('<span style="font-size:9pt"><b>' + LABELS['also'].strip() + '</b> ' + ', '.join(E(a['name']) for a in x['also']) + '</span>') if x['also'] else ''
    used = f'<span style="display:inline-flex;align-items:center;gap:1mm;font-size:9pt;font-weight:700;white-space:nowrap">{_tick(3.6)}{LABELS["used"]}</span>'
    if compact:
        return (f'<div class="spchip" data-spine="chip" style="{BOX}margin:1.5mm 0 0;padding:0.6mm 2mm;display:flex;align-items:center;gap:2mm">'
                f'<span style="font-size:9pt;font-weight:800;letter-spacing:.05em;white-space:nowrap">{LABELS["tool_of_day"]}</span>{icon(t["id"], 7)}'
                f'<span style="font-family:Fredoka,Arial,sans-serif;font-size:12pt;font-weight:700;white-space:nowrap">{E(t["name"])}</span>{used}'
                f'<span style="margin-left:auto">{also}</span></div>')
    return (f'<div class="spchip" data-spine="chip" style="{BOX}margin:1.5mm 0 0;padding:1mm 2.5mm;display:flex;gap:2.5mm;align-items:center">{icon(t["id"], 11)}'
            f'<div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between;align-items:center;gap:2mm"><span style="font-size:9pt;font-weight:800;letter-spacing:.06em">{LABELS["tool_of_day"]}</span>{used}</div>'
            f'<div style="font-family:Fredoka,Arial,sans-serif;font-size:13pt;font-weight:700;line-height:1.15">{E(t["name"])}</div>'
            f'<div style="font-size:9pt;line-height:1.2">{E(x["def"])}{(" &nbsp; " + also) if also else ""}</div></div></div>')


def wb_lookback(d):
    """The common look-back box (replaces the old 'Something I did well / hardest / helped / next time' box). Same prompts in every lesson."""
    if not row(d):
        return ''
    dot = f'<span style="flex:1;border-bottom:0.4mm dotted {INK};height:5.5mm;min-width:18mm"></span>'
    yn = ''.join(f'<span style="display:inline-flex;align-items:center;gap:1mm;white-space:nowrap">{_tick(4)}<b style="font-size:10pt">{w}</b></span>' for w in ('yes', 'not yet'))
    def r(n, q, right):
        return (f'<div class="r" style="display:flex;align-items:center;gap:3mm;margin-top:1.5mm"><span style="flex:none;width:6mm;height:6mm;border:0.5mm solid {INK};border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:800;font-size:10pt">{n}</span>'
                f'<span style="flex:1;font-size:11pt;font-weight:700;line-height:1.15">{E(q)}</span><span style="display:flex;align-items:center;gap:3mm;flex:none;{"width:70mm" if n == 3 else ""}">{right}</span></div>')
    a3 = f'<span style="font-size:9pt;white-space:nowrap">{E(LB["answer3"][BAND])}:</span>{dot}'
    tools = ''.join(f'<span style="display:inline-flex;align-items:center;gap:0.8mm">{icon(t["id"], 7)}{_tick(3.6)}</span>' for t in TOOLS)
    return (f'<div class="lbk sp" data-spine="lookback" style="border:0.5mm solid {INK};border-radius:2mm;background:#fff;color:{INK};font-family:\'Nunito Sans\',Arial,sans-serif;padding:2mm 4mm 2.2mm;margin-top:4mm;break-inside:avoid">'
            f'<div style="display:flex;align-items:baseline;gap:3mm"><span style="font-family:Fredoka,Arial,sans-serif;font-weight:700;font-size:15pt">Look back</span><span style="font-size:9pt">{E(LB["intro"])}</span></div>'
            f'{r(1, PROMPTS[0], yn)}{r(2, PROMPTS[1], yn)}{r(3, PROMPTS[2], a3)}'
            f'<div style="display:flex;align-items:center;justify-content:space-between;gap:2mm;margin-top:2mm;border-top:0.4mm solid {INK};padding-top:1.5mm"><span style="font-size:9pt;font-weight:800;white-space:nowrap">{E(LB["footer_tools"])}:</span>{tools}</div>'
            f'<div style="display:flex;gap:6mm;margin-top:1.2mm;font-size:9pt"><span style="display:inline-flex;align-items:center;gap:1.2mm">{_tick(3.6)}{E(STUCK)}</span><span style="display:inline-flex;align-items:center;gap:1.2mm">{_tick(3.6)}{E(LB["pass"])}</span></div></div>')


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
        lean = ('; the content for now leans on ' + ' and '.join(t['name'] for t in x['lean'])) if x['lean'] else ''
        body = (f'<b>Choose one.</b> No single tool of the day: the child picks and ticks the tool they used{E(lean)}. {E(x["reason"])}')
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


def lookback_lines():
    """Plain text for the look-back script lines and slide note (used by tools/apply_spine_term.py)."""
    T = _TERM
    return T['look_back']['say'], T['look_back']['do']


# ------------------------------------------------------------------ deck (b_deck.py)

def deck_chip(d, size=44):
    """'TODAY'S TOOL' chip for the title slide (dark background): cream stroke icon and the tool name."""
    x = info(d)
    if not x:
        return ''
    if x['choose']:
        ics = ''.join(icon(t['id'], 64, CREAM, 'px') for t in TOOLS)
        return (f'<div data-spine="chip" style="align-self:flex-start;background:#26385F;border-radius:24px;padding:18px 34px;display:flex;align-items:center;gap:26px">'
                f'<p style="font-size:26px;font-weight:700;letter-spacing:3px;color:#FFC93C">TODAY\'S TOOL</p><p style="font-size:{size}px;font-weight:700">You choose</p><div style="display:flex;gap:14px">{ics}</div></div>')
    ic = icon(x['tool']['id'], 84, CREAM, 'px')
    return (f'<div data-spine="chip" style="align-self:flex-start;background:#26385F;border-radius:24px;padding:18px 34px;display:flex;align-items:center;gap:26px">'
            f'{ic}<div><p style="font-size:26px;font-weight:700;letter-spacing:3px;color:#FFC93C">TODAY\'S TOOL</p><p style="font-size:{size}px;font-weight:700">{E(x["name"])}</p></div></div>')


def deck_lookback(d, NAVY, TEAL, MUTED, CARD, chip):
    """Look-back slide body (replaces b_deck.lookback): three prompts, 'Tool I used' row, stuck and pass. `chip` is b_deck.chip."""
    if not row(d):
        return None
    box = lambda: f'<span style="display:inline-block;width:0.8em;height:0.8em;border:3px solid {NAVY};border-radius:8px;background:#fff;margin-right:12px;vertical-align:-0.05em"></span>'
    rows = ''
    for k, q in enumerate(PROMPTS, 1):
        ans = (f'<span style="white-space:nowrap">{box()}yes &nbsp; {box()}not yet</span>' if k < 3 else f'<span style="color:{MUTED}">{E(LB["answer3"][BAND])}</span>')
        rows += (f'<div style="display:flex;gap:28px;align-items:center;padding:12px 0;{"border-top:2px solid #DCE4F0;" if k > 1 else ""}"><span style="flex:none;width:64px;height:64px;border-radius:50%;border:3px solid {NAVY};display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:800">{k}</span>'
                 f'<p style="flex:1;font-size:46px;font-weight:700;line-height:1.2">{E(q)}</p><p style="font-size:32px;font-weight:600">{ans}</p></div>')
    ics = ''.join(f'<span style="display:inline-flex;align-items:center;gap:8px">{icon(t["id"], 62, NAVY, "px")}{box()}</span>' for t in TOOLS)
    foot = (f'<div style="display:flex;align-items:center;gap:22px;border-top:2px solid #DCE4F0;padding-top:14px"><p style="font-size:30px;font-weight:800;color:{TEAL};flex:none">{E(LB["footer_tools"])}</p><div style="display:flex;gap:18px;flex-wrap:wrap">{ics}</div></div>'
            f'<p style="font-size:28px;font-weight:600">{box()}{E(STUCK)} &nbsp;&nbsp; {box()}{E(LB["pass"])}</p>')
    return chip('Three minutes. ' + LB['intro'], 30) + f'<div style="{CARD}padding:18px 40px;display:flex;flex-direction:column;gap:6px;max-width:1500px">{rows}{foot}</div>'
