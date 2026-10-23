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
CONSENT_VERSION = 'privacy-2026-10-draft'   # same version string as portal/public/common.js VERSIONS.privacy; bump with privacy.html


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
.chips label{display:inline-flex;gap:8px;align-items:center;border:2px solid var(--line);border-radius:999px;padding:6px 12px;background:var(--bg);font-weight:600;font-size:15px;cursor:pointer}
.chips label:has(input:checked){background:var(--mint);border-color:var(--ink)}
.chips input{width:auto;accent-color:var(--teal)}
.chips.slotchips label{border-radius:14px;border-style:dashed;align-items:flex-start}
.chips.slotchips label:has(input:checked){border-style:solid}
.chips.slotchips input{margin-top:4px}
.fine2{font-size:13px;color:var(--muted)}
.field .err{color:var(--red);font-weight:700;font-size:14px}
'''


def form_section(wa_num, wa_show):
    """The 'Request another time' section for the home page. Slot checkboxes come from the JSON; JS adds behaviour, the markup is complete without it."""
    slots = load_slots()
    lv = ''.join('<option value="%d">Level %d (ages %s)</option>' % (n, n, a) for n, a in LEVEL_AGES.items())
    ab = '<option value="">Choose…</option>' + ''.join('<option value="%s">%s</option>' % (c, l) for c, l in AGE_BANDS)
    sl = ''.join(
        '<label><input type="checkbox" name="itslot" value="%s" data-label="%s"><span><b>%s</b><br><span class="small muted">%s · not open yet</span></span></label>'
        % (esc(s['id']), esc(s['label'] + ', ' + slot_when(s)), esc(s['label']), esc(slot_when(s))) for s in slots)
    wn = ''.join('<label><input type="checkbox" name="itwin" value="%s" data-label="%s"><span>%s</span></label>' % (c, l, l) for c, l in WINDOWS)
    wa_lbl = ''
    return '''<section class="band peach" id="request-time" style="display:block"><div class="sec"><span class="eyebrow">Other times</span><h2>Request another time</h2>
<p class="muted">The groups above are the ones open now. If none of them fit, tell us the times that would suit your family. We use the replies to decide which new groups to open. <b>This is not a booking</b>: nothing is reserved and nothing is charged. If we open a group that matches, we message you first.</p></div>
<noscript><div class="msg info">This form needs JavaScript. Without it, message us on WhatsApp at <a href="https://wa.me/%(wa_num)s">%(wa_show)s</a> with your child's level and age range and the days and times that would suit you.</div></noscript>
<form class="card" id="itForm" novalidate autocomplete="off">
<div class="grid2"><div class="field"><label for="itLevel">Level</label><select id="itLevel" name="level">%(lv)s</select></div>
<div class="field"><label for="itAge">Child's age range</label><select id="itAge" name="age" required>%(ab)s</select><span class="fine2">An age range only. Please do not give your child's name.</span></div></div>
<fieldset class="field" style="border:0;padding:0;margin:0 0 12px"><legend class="flabel">Times you are interested in <span class="muted" style="font-weight:600">(tick any)</span></legend>
%(slhead)s<div class="chips slotchips" id="itSlots">%(sl)s</div>
<div class="small muted" style="margin:10px 0 6px">Or a general window</div><div class="chips" id="itWins">%(wn)s</div></fieldset>
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
        wa_num=wa_num, wa_show=esc(wa_show), lv=lv, ab=ab, sl=sl, wn=wn, wa_lbl=wa_lbl,
        slhead=('<div class="small muted" style="margin-bottom:6px">Placeholder groups we are considering (not open yet)</div>' if slots else ''))
