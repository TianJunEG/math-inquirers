"""Shared pieces of the 'Other times' placeholders and the 'Request another time' form.

Used by lp_build.py (home page: form + level cards) and level_pages.py (placeholders on each level page, linking to the home form).
Data comes from data/interest_slots.json (owner edits that file; ids are stored with each request).
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LEVEL_AGES = {1: '6-8', 2: '7-9', 3: '8-10', 4: '9-11', 5: '10-12', 6: '11-13'}
AGE_BANDS = [('under-6', 'Under 6'), ('6-7', '6 to 7'), ('8-9', '8 to 9'), ('10-11', '10 to 11'), ('12-13', '12 to 13'), ('14-plus', '14 or older')]
WINDOWS = [('wkday-am', 'Weekday mornings'), ('wkday-pm', 'Weekday afternoons'), ('wkday-eve', 'Weekday evenings'), ('sat', 'Saturday'), ('sun', 'Sunday')]
CONSENT_VERSION = 'privacy-2026-10b-draft'   # same version string as portal/public/common.js VERSIONS.privacy; bump with privacy.html


def esc(s):
    return html.escape(str(s), quote=True)


def t12(t):
    h, m = map(int, t.split(':'))
    return '%d:%02d%s' % ((h % 12) or 12, m, 'pm' if h >= 12 else 'am')


def load_slots():
    d = json.load(open(os.path.join(HERE, 'data', 'interest_slots.json'), encoding='utf-8'))
    out = []
    for s in d['slots']:
        if s.get('show', True) is False:
            continue
        assert all(c.isalnum() or c == '-' for c in s['id']) and len(s['id']) <= 16, 'slot id %r' % s['id']
        out.append(s)
    assert len({s['id'] for s in out}) == len(out), 'duplicate slot id'
    return out


DAY_ORDER = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
GROUPS = [('hol', 'Holiday program (Nov to Dec 2026)'), ('term', 'Term time (2027)')]
GROUP_NOTE = 'Not open yet: tell us which you would join.'


def slot_group(s):
    return s.get('group') or ('term' if s['id'].startswith('T27-') else 'hol')


def t_short(t):
    h, m = map(int, t.split(':'))
    return '%d:%02d' % ((h % 12) or 12, m), ('pm' if h >= 12 else 'am')


def span(x):
    """'9:00-10:30am' (the suffix is repeated only when am/pm differ)."""
    a, ap = t_short(x['start']); b, bp = t_short(x['end'])
    return '%s-%s%s' % (a, b, bp) if ap == bp else '%s%s-%s%s' % (a, ap, b, bp)


def slot_row(s):
    """Row heading in the grid: 'Wed & Thu'."""
    days = []
    for x in s['sessions']:
        if x['day'] not in days:
            days.append(x['day'])
    return ' & '.join(days)


def slot_chip_text(s):
    """Short time text for the chip: '9:00-10:30am', 'Between 1:15-5:00pm', or per-day text when the times differ."""
    ss = s['sessions']
    if s.get('window'):
        return 'Between ' + span(ss[0])
    if len({span(x) for x in ss}) == 1:
        return span(ss[0])
    return ', '.join('%s %s' % (x['day'], span(x)) for x in ss)


def slot_readable(s):
    """Label used in the WhatsApp message: 'Holiday: Wed & Thu 9:00-10:30am' / 'Term 2027: Thu 5:45-7:15pm'."""
    pre = 'Term 2027: ' if slot_group(s) == 'term' else 'Holiday: '
    t = slot_chip_text(s)
    return pre + (t if t[:3] in DAY_ORDER else slot_row(s) + ' ' + t)


def slot_when(s):
    """'Wed 9:00am–10:30am & Thu 9:00am–10:30am' (a window slot reads 'Mon between 1:15pm and 5:00pm')."""
    if s.get('window'):
        return ' & '.join('%s between %s and %s' % (x['day'], t12(x['start']), t12(x['end'])) for x in s['sessions'])
    return ' & '.join('%s %s–%s' % (x['day'], t12(x['start']), t12(x['end'])) for x in s['sessions'])


def link(level, slot_id=None):
    q = 'level=%d' % level
    if slot_id:
        q += '&amp;interest=%s' % esc(slot_id)
    return '/?%s#request-time' % q


def other_times_block(level, slots):
    """The 'Other times' area for one level card. Static HTML (works without JS): each button is a link to the home page form."""
    mine = [s for s in slots if level in s.get('levels', [])]
    rows = ''.join(
        '<li><div><b>%s</b><br><span class="small muted">%s</span></div><span class="pill p-wait">Not open yet</span>'
        '<a class="btn sm alt" href="%s" data-interest="%s" data-level="%d" aria-label="I\'m interested in %s">I\'m interested</a></li>'
        % (esc(s['label']), esc(slot_when(s)), link(level, s['id']), esc(s['id']), level, esc(s['label'] + ', ' + slot_when(s)))
        for s in mine)
    head = '<p class="small muted">%s</p>' % (
        'These times are <b>not open for enrolment</b>. Tell us if one suits you and we may open it when enough families are interested.' if mine
        else 'None of the Level %d times above suit? Tell us what does and we may open another group when enough families are interested.' % level)
    return ('<details class="othertimes" data-level="%d"><summary>Other times <span class="pill p-wait">Not open yet</span></summary>%s%s<a class="small" href="%s" data-interest="" data-level="%d"><b>Request another time</b></a></details>'
            % (level, head, ('<ul>%s</ul>' % rows) if rows else '', link(level), level))


CSS = '''
.othertimes{border-top:2px dashed var(--line);margin-top:6px;padding-top:10px;display:grid;gap:8px}
.othertimes summary{font:600 17px var(--head);cursor:pointer}
.othertimes[open] summary{margin-bottom:8px}
.othertimes ul{list-style:none;padding:0;margin:0;display:grid;gap:8px}
.othertimes li{display:grid;grid-template-columns:1fr auto;gap:4px 10px;align-items:center;background:var(--bg);border:2px dashed var(--line);border-radius:14px;padding:8px 10px}
.othertimes li .btn{grid-column:1/-1;justify-self:start}
.othertimes a.small{justify-self:start}
.hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label,.slotchip{display:inline-flex;gap:8px;align-items:center;min-height:44px;box-sizing:border-box;border:2px solid var(--line);border-radius:12px;padding:6px 12px;background:var(--bg);font-weight:600;font-size:15px;line-height:1.25;cursor:pointer}
.chips label:has(input:checked){background:var(--mint);border-color:var(--ink);font-weight:700}
.chips label:has(input:focus-visible){outline:3px solid var(--teal);outline-offset:2px}
.chips input{width:20px;height:20px;flex:none;margin:0;accent-color:var(--teal)}
.chips label[hidden]{display:none}
#itWins label{border-radius:999px}
.slotbar{display:flex;flex-wrap:wrap;align-items:center;gap:6px 16px;margin:2px 0 12px}
.slotbar[hidden],.slotbar [hidden],.sgroup[hidden],#itNone[hidden],.srow[hidden]{display:none}
.slotbar .count{font-weight:700;font-size:15px;margin-right:auto}
.linkbtn{font:600 15px var(--body,inherit);color:var(--teal);background:none;border:0;padding:0 4px;min-height:44px;cursor:pointer;text-decoration:underline}
.sgroup{margin:0 0 16px}
.gh,.gh2{font:700 16px var(--head);margin:0 0 2px}
.gnote{font-size:14px;color:var(--muted);margin:0 0 8px}
.srow{display:grid;grid-template-columns:84px 1fr;gap:6px 10px;align-items:start;padding:8px 0;border-top:1px solid var(--line)}
.rday{font-weight:700;font-size:15px;padding-top:10px}
.winwrap{margin-top:6px;border-top:2px solid var(--line);padding-top:12px}
.winwrap .gh2{margin-bottom:8px}
@media(max-width:420px){.srow{grid-template-columns:70px 1fr;gap:6px}.chips label,.slotchip{padding:6px 10px}}
.fine2{font-size:13px;color:var(--muted)}
.field .err{color:var(--red);font-weight:700;font-size:14px}
'''


def slot_groups_html(slots):
    """Slots grouped by program, then rows by day(s), each slot a short time chip (data-levels drives the level filter in interest.js)."""
    out = []
    for gid, gname in GROUPS:
        mine = [s for s in slots if slot_group(s) == gid]
        if not mine:
            continue
        rows = {}
        for s in mine:
            rows.setdefault(slot_row(s), []).append(s)
        def key(item):
            d = item[1][0]['sessions'][0]['day']
            return (DAY_ORDER.index(d) if d in DAY_ORDER else 9, item[0])
        body = ''
        for n, (rname, rs) in enumerate(sorted(rows.items(), key=key)):
            rs.sort(key=lambda s: s['sessions'][0]['start'])
            chips = ''.join(
                '<label class="slotchip" data-levels="%s"><input type="checkbox" name="itslot" value="%s" data-label="%s"><span>%s</span></label>'
                % (' '.join(str(l) for l in s.get('levels', [])), esc(s['id']), esc(slot_readable(s)), esc(slot_chip_text(s))) for s in rs)
            rid = 'itRow-%s-%d' % (gid, n)
            body += '<div class="srow" role="group" aria-labelledby="%s"><span class="rday" id="%s">%s</span><div class="chips">%s</div></div>' % (rid, rid, esc(rname), chips)
        out.append('<div class="sgroup" data-group="%s"><h3 class="gh" id="itG-%s">%s</h3><p class="gnote">%s</p>%s</div>' % (gid, gid, esc(gname), GROUP_NOTE, body))
    return '<div id="itSlots">%s<p class="gnote" id="itNone" hidden>No suggested times for this level yet. Choose \'Show all times\', a general window below, or write your own.</p></div>' % ''.join(out)


def form_section(wa_num, wa_show):
    """The 'Request another time' section for the home page. Slot checkboxes come from the JSON; JS adds behaviour, the markup is complete without it."""
    slots = load_slots()
    lv = ''.join('<option value="%d">Level %d (ages %s)</option>' % (n, n, a) for n, a in LEVEL_AGES.items())
    ab = '<option value="">Choose…</option>' + ''.join('<option value="%s">%s</option>' % (c, l) for c, l in AGE_BANDS)
    sl = slot_groups_html(slots)
    wn = ''.join('<label><input type="checkbox" name="itwin" value="%s" data-label="%s"><span>%s</span></label>' % (c, l, l) for c, l in WINDOWS)
    wa_lbl = ''
    return '''<section class="band peach" id="request-time" style="display:block"><div class="sec"><span class="eyebrow">Other times</span><h2>Request another time</h2>
<p class="muted">The groups above are the ones open now. If none of them fit, tell us the times that would suit your family. We use the replies to decide which new groups to open. <b>This is not a booking</b>: nothing is reserved and nothing is charged. If we open a group that matches, we message you first.</p></div>
<noscript><div class="msg info">This form needs JavaScript. Without it, message us on WhatsApp at <a href="https://wa.me/%(wa_num)s">%(wa_show)s</a> with your child's level and age range and the days and times that would suit you.</div></noscript>
<form class="card" id="itForm" novalidate autocomplete="off">
<div class="grid2"><div class="field"><label for="itLevel">Level</label><select id="itLevel" name="level">%(lv)s</select></div>
<div class="field"><label for="itAge">Child's age range</label><select id="itAge" name="age" required>%(ab)s</select><span class="fine2">An age range only. Please do not give your child's name.</span></div></div>
<fieldset class="field" style="border:0;padding:0;margin:0 0 12px"><legend class="flabel">Times you are interested in <span class="muted" style="font-weight:600">(tick any)</span></legend>
<div class="slotbar" id="itBar" hidden><span class="count" id="itCount" aria-live="polite">0 times selected</span><button type="button" class="linkbtn" id="itClear" hidden>Clear selection</button><button type="button" class="linkbtn" id="itAll" aria-pressed="false">Show all times</button></div>
%(sl)s
<div class="winwrap"><div class="gh2" id="itWinH">Or a general window</div><div class="chips" id="itWins" role="group" aria-labelledby="itWinH">%(wn)s</div></div></fieldset>
<div class="field"><label for="itOther">Another day or time <span class="muted" style="font-weight:600">(optional)</span></label><input id="itOther" name="other" maxlength="200" placeholder="For example: Tuesday after 4pm"></div>
<div class="grid2"><div class="field"><label for="itName">Your first name</label><input id="itName" name="name" maxlength="40" autocomplete="given-name" required></div>
<div class="field"><label for="itNote">Anything else? <span class="muted" style="font-weight:600">(optional)</span></label><input id="itNote" name="note" maxlength="400"></div></div>
<div class="grid2"><div class="field"><label for="itWa">WhatsApp number</label><input id="itWa" name="wa" type="tel" inputmode="tel" autocomplete="tel" placeholder="9123 4567"></div>
<div class="field"><label for="itEmail">or email</label><input id="itEmail" name="email" type="email" autocomplete="email" maxlength="120"></div></div>
<p class="fine2" style="margin:-4px 0 12px">Give at least one, so we can reach you.</p>
<div class="hp" aria-hidden="true"><label>Leave this empty<input id="itHp" name="company_website" tabindex="-1" autocomplete="off"></label></div>
<label class="check" for="itConsent"><input type="checkbox" id="itConsent" name="consent"><span>I agree that Math Inquirers (Preciouslyours Pte Ltd) may keep my first name, my contact details, my child's age range and the times I choose, <b>only to plan new class times</b> and to contact me <b>about those times</b>. We keep this for <b>12 months</b> and then delete it. No marketing. You can ask us to delete it sooner. See the <a href="/privacy/" target="_blank">privacy notice</a>.</span></label>
<div id="itMsg" aria-live="polite"></div>
<button class="btn" type="submit" id="itSubmit">Send my request</button>
<p class="fine2" style="margin-top:10px" id="itModeNote"></p></form></section>''' % dict(
        wa_num=wa_num, wa_show=esc(wa_show), lv=lv, ab=ab, sl=sl, wn=wn, wa_lbl=wa_lbl)
