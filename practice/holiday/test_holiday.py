#!/usr/bin/env python3
"""Browser test of a built holiday practice lesson (Playwright/Chromium) and screenshots.  Shared by every level.

    python3 practice/holiday/build_holiday.py p1 1 && python3 practice/holiday/test_holiday.py p1 1

1. re-reads the BUILT data file and recomputes every answer with the lesson's independent checkers again (the output file is checked, not the build);
2. opens the questions in REVERSE order in a real browser, types the correct answer into each (several accepted wordings for text answers), submits (with the
   'no answer' confirm only if a marked question is blank), and expects every auto-marked question right, every self-check shown as 'check yourself', and a worked
   solution for every question (and the correct-drawing figure for paper-only items);
3. a second child answers wrongly, skips some, reloads (answers survive), submits: wrong / no answer markers, solutions for skipped questions; solutions are
   hidden before submit and again after 'Change my answers'; wrong text wordings are marked wrong;
4. every variant family: forces each combination of the variables, checks the question shown equals the template and the ORACLE's answer is accepted;
   Shared-matcher fixes (week 2 audit) are covered here too: unit and notation forms, equal fractions (equiv_frac), algebra rules as polynomials (poly), number words only when
   declared, short distinct question buttons, label+box groups that never split at 390 and 360 px, solution figures at least 11 px and not clipped at 360 px, the typed explanation
   in the submission payload (trimmed, at most 500 characters) when sending is on, and the tutor-report marking_mode of every self-check item.
5. screenshots at 390 px and 900 px, light and dark, into practice/holiday/<key>/<NN>/proof/; checks there is no horizontal scroll, that every figure
   text is at least 11 px on screen at 390 px, and that no figure text is clipped.
"""
import functools, http.server, itertools, json, os, re, sys, threading
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_holiday as H                      # noqa: E402
B = H.B
from playwright.sync_api import sync_playwright   # noqa: E402

key = sys.argv[1] if len(sys.argv) > 1 else 'p1'
n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
lk = f'{key}l{n:02d}'
BASE = os.path.join(HERE, key, f'{n:02d}')
DIST = os.path.join(BASE, 'dist')
PROOF = os.path.join(BASE, 'proof'); os.makedirs(PROOF, exist_ok=True)
data = json.load(open(os.path.join(DIST, 'data', lk + '.json'), encoding='utf-8'))
items = data['items']
lesson = H.load_lesson(key, n)
src = {s['id']: s for s in lesson.ITEMS}
fails = []


def fail(msg):
    fails.append(msg); print('FAIL', msg)


# ---- 1. the built data against fresh independent checks
nchk = 0
for it in items:
    s = src[it['id']]
    chk = s.get('check')
    if chk is None:
        if not (s['type'] == 'selfcheck' and s.get('open')):
            fail(f'{it["id"]}: no checker')
        continue
    got = chk(); nchk += 1
    t = it['type']
    if t == 'fields':
        ok = [int(x) for x in got] == [f['answer'] for f in it['fields']]
    elif t == 'number':
        ok = int(got) == it['answer']
    elif t == 'choice':
        ok = got == it['answer']
    elif t == 'set':
        ok = (list(map(int, got)) == it['answer']) if it['ordered'] else sorted(map(int, got)) == sorted(it['answer'])
    elif t == 'text':
        ok = (tuple(got) == tuple(s['rule']) and it['answer'] == H.hlib.rule_accepts(*got)) if s.get('rule') else str(got).strip().lower() in [str(x).strip().lower() for x in it['answer']]
    else:
        ok = s.get('facts') is None or got == s['facts']
    if not ok:
        fail(f'{it["id"]}: built data differs from the independent check {got}')
print(f'1. {len(items)} built items; {nchk} re-checked against the independent checkers')

# ---- 1b. the build-time twins in hlib (poly_parse, frac_list_ok) agree with the shared matcher in practice/submit/mark.js on a battery of strings
import subprocess
_RULES = [('4n+12', ['(n+3)\u00d74', '4n+12', '4(n+3)', '4*(n+3)', '4x(n+3)', '(n+3)4', '12+4n', '(8n+24)\u00f72', '4n+16\u22124', '(n+3)\u00d74 = 4n+12', 'OUT = 4(n+3)', 'out=4n+12', '4n+12=OUT', '4n+12.', '  4 n + 12 ', '2(2n+6)',
                      '4n-12', 'n+3\u00d74', '(n+3)+4', '4n+3', '4(n+4)', '(n+3)\u00d75', '3n+12', '7n', '4n', '12', 'n+3 = 4n+12', '4n+12=', 'OUT', '4n+12 n', '4n 12', '4n\u00b2+12', 'fourn+12', '4n+12/0', '(4n+12', 'n^9', '(n+1)'*12]),
           ('n+3', ['(2n+6)\u00f72', '(2n+6)/2', '2n+6\u00f72', 'n+6', '3+n', 'n+3', '(n+3)']), ('0.5n', ['n/2', 'n\u00f72', '0.5n', '.5n', '-0.5n', '2n/4', 'n/3']), ('n^2+2n+1', ['(n+1)\u00b2', '(n+1)^2', 'n\u00d7n+2n+1', 'n\u00b2+1', 'n^2+2n+1', '(n+1)(n+1)'])]
_FRACS = [('7/12, 2/3, 5/6', ['7/12, 8/12, 10/12', '7/12 8/12 10/12', '14/24,2/3,5/6', '8/12, 7/12, 10/12', '7/12, 8/12', '7/12, 8/12, 10/12, 1', '7/0, 8/12, 10/12', '0.5, 2/3, 5/6', '7/12, 2/3, 5/6.']),
          ('1/4 < 1/2 < 3/4', ['2/8 < 4/8 < 6/8', '2/8 > 4/8 > 6/8', '2/8, 4/8, 6/8']), ('1 1/2', ['3/2', '6/4', '11/2', '1 1/2', '1 2/4'])]
_cases = [dict(rec=dict(marking_mode='auto', type='text', key=[k], poly='n'), v=v, py=H.hlib.poly_ok([k], v, 'n')) for k, vs in _RULES for v in vs]
_cases += [dict(rec=dict(marking_mode='auto', type='text', key=[k], equiv_frac=True), v=v, py=H.hlib.frac_list_ok([k], v)) for k, vs in _FRACS for v in vs]
_js = "const M=require(process.argv[1]);const c=JSON.parse(require('fs').readFileSync(0,'utf8'));console.log(JSON.stringify(c.map(x=>M.mark(x.rec,x.v).mark==='right')))"
_out = json.loads(subprocess.run(['node', '-e', _js, os.path.join(H.ROOT, 'practice', 'submit', 'mark.js')], input=json.dumps(_cases), capture_output=True, text=True, check=True).stdout)
for _c, _o in zip(_cases, _out):
    # mark.js also accepts the printed forms exactly; the python twin only the polynomial / fraction reading, so compare only where the python one says no and the string is not the key itself
    if _c['py'] != _o and not (not _c['py'] and _o and _c['v'].strip() in _c['rec']['key']): fail(f'hlib and mark.js disagree on {_c["rec"].get("poly") and "rule" or "fractions"} {_c["rec"]["key"]} typed {_c["v"]!r}: python {_c["py"]}, mark.js {_o}')
print(f'1b. hlib (build time) and mark.js (browser and server) agree on {len(_cases)} typed rules and fraction lists')


class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Q, directory=DIST))
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{srv.server_address[1]}/index.html'

WRONG_TEXT = {'add': 'take away 7', 'take away': 'add 7'}


def enter(page, it, wrong=False, alt=0):
    t = it['type']
    if t == 'fields':
        a = [f['answer'] for f in it['fields']]
        if wrong: a = [x + 1 for x in a]
        boxes = page.locator('#ans input[data-f]')
        assert boxes.count() == len(a), (it['id'], boxes.count(), len(a))
        for i, x in enumerate(a): boxes.nth(i).fill(str(x))
    elif t == 'set':
        a = list(it['answer'])
        if wrong: a = a[:-1] + [a[-1] + 1]
        page.locator('#ans input[type=text]').fill(', '.join(map(str, a)))
    elif t == 'number':
        page.locator('#ans input[type=text]').fill(str(it['answer'] + (1 if wrong else 0)))
    elif t == 'choice':
        pick = it['answer'] if not wrong else [o for o in it['options'] if o != it['answer']][0]
        page.locator('#ans label.opt', has_text=re.compile('^' + re.escape(pick) + '$')).click()
    elif t == 'text':
        s = src[it['id']]
        txt = (WRONG_TEXT[s['rule'][0]] if s.get('rule') else 'zzz not it') if wrong else it['answer'][alt % len(it['answer'])]
        page.locator('#ans input[type=text]').fill(txt)
    elif t == 'selfcheck':
        if page.locator('#ans textarea').count():
            page.locator('#ans textarea').fill('my own words')


def goto(page, i):
    page.locator(f'#nav button[data-i="{i}"]').click()


def idx_of(item_id):
    return [k for k, x in enumerate(items) if x['id'] == item_id][0]


def fresh(br, w=800, h=900, dark=False):
    c = br.new_context(viewport={'width': w, 'height': h}, color_scheme='dark' if dark else 'light')
    p = c.new_page(); p.goto(URL); p.wait_for_selector('#card .q')
    return c, p


def figure_text_check(page, w, mn=11, sel='#card svg text'):
    """Every figure text on screen at least mn px, and none outside its svg."""
    return page.evaluate("""([MIN, SEL]) => {
      const bad = [];
      document.querySelectorAll(SEL).forEach(t => {
        const svg = t.ownerSVGElement, ctm = t.getScreenCTM(); if (!ctm) return;
        const fs = parseFloat(getComputedStyle(t).fontSize) * ctm.a;
        const r = t.getBoundingClientRect(), s = svg.getBoundingClientRect();
        if (fs < MIN) bad.push('small ' + t.textContent + ' ' + fs.toFixed(1));
        if (r.left < s.left - 1 || r.right > s.right + 1 || r.top < s.top - 1 || r.bottom > s.bottom + 1) bad.push('clipped ' + t.textContent);
      });
      return bad;
    }""", [mn, sel])


with sync_playwright() as pw:
    br = pw.chromium.launch()
    errors = []
    N = len(items)
    cls = lambda p, i: p.locator(f'#nav button[data-i="{i}"]').get_attribute('class').split()[-1]
    nself = sum(1 for it in items if it['type'] == 'selfcheck')
    npaper = sum(1 for it in items if it.get('paper'))

    # ---- 2: a child who answers everything, in reverse order
    ctx, page = fresh(br)
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    page.reload(); page.wait_for_selector('#card .q')
    for i in reversed(range(N)):
        goto(page, i)
        if page.locator('#card .q').inner_text() != items[i]['q']: fail(f'{items[i]["id"]}: shown question differs from data')
        if page.locator('#sol').count(): fail(f'{items[i]["id"]}: solution visible before submit')
        if items[i].get('paper'):
            if 'Do this on paper, then check your drawing against the answer shown on screen' not in page.locator('#paper').inner_text(): fail(f'{items[i]["id"]}: no paper note')
            if page.locator('#ans textarea').count(): fail(f'{items[i]["id"]}: paper-only item has a text box')
        enter(page, items[i], alt=i)
    page.locator('#submit').click()
    # self-check and paper-only items are never 'unanswered': a child who has answered every marked question is not asked 'Submit anyway?'
    if page.locator('#yes').count() or page.locator('#askbox').count(): fail('"Submit anyway?" shown although every marked question has an answer')
    if page.evaluate("document.activeElement && document.activeElement.id") != 'summary': fail('focus not on the summary after Submit')
    summ = page.locator('#summary').inner_text()
    if f'{N - nself} of {N - nself} marked questions are right' not in summ: fail('summary: ' + summ)
    for i, it in enumerate(items):
        goto(page, i)
        c = cls(page, i)
        if c != ('self' if it['type'] == 'selfcheck' else 'right'): fail(f'{it["id"]}: marker {c}')
        if not page.locator('#sol li').count(): fail(f'{it["id"]}: no worked steps after submit')
        if it.get('sol_svg') and not page.locator('#solfig svg').count(): fail(f'{it["id"]}: no figure of the correct drawing')
        if it.get('paper') and not it.get('sol_svg'): fail(f'{it["id"]}: paper item without a solution figure')
        sol = page.locator('#sol').inner_text()
        if it['type'] in ('fields',) and not all(str(f['answer']) in sol for f in it['fields']): fail(f'{it["id"]}: answer not in solution')
    print(f'2. {N} questions opened in reverse order, all answered, submitted: {N - nself} marked right, {nself} to check yourself ({npaper} paper-only with a figure of the correct drawing), {N} worked solutions shown')
    page.locator('#again').click()
    if page.locator('#sol').count(): fail('solution still visible after "Change my answers"')
    ctx.close()

    # ---- 2b: the same answers typed the way children type them: no spaces after commas, a final full stop, .0, a unit word, a statement with its result
    ctx, page = fresh(br)
    for i, it in enumerate(items):
        t = it['type']
        goto(page, i)
        if t == 'set':
            big = any(abs(x) >= 10000 for x in it['answer'])
            page.locator('#ans input[type=text]').fill(','.join(map(str, it['answer'])) if not big else ', '.join(map(str, it['answer'])))
        elif t == 'number':
            page.locator('#ans input[type=text]').fill(f"{it['answer']}.0")
        elif t == 'fields':
            for k, f in enumerate(it['fields']): page.locator('#ans input[data-f]').nth(k).fill(f"{f.get('pre', '')}{f['answer']}" if k % 2 == 0 else f"{f['answer']}.")
        else:
            enter(page, it, alt=i)
    page.locator('#submit').click()
    if page.locator('#yes').count(): page.locator('#yes').click()
    summ = page.locator('#summary').inner_text()
    if f'{N - nself} of {N - nself} marked questions are right' not in summ: fail('2b (comma without space, 20.0, 6:20, 29.): ' + summ)
    ctx.close()
    print('2b. lists typed with commas and no spaces, whole numbers typed as 20.0 or 29., and clock boxes typed as 6:20 are all marked right')

    # ---- 2c: reading aids: focus, labels, input modes, helper line, footer, noindex, placeholder contrast
    ctx, page = fresh(br)
    act = lambda: page.evaluate("(document.activeElement.className||'') + '|' + (document.activeElement.id||'')")
    page.locator('#nav button[data-i="1"]').click()
    if 'q|' not in act(): fail('focus not on the question after choosing a question: ' + act())
    page.get_by_role('button', name='Skip to next').click()
    if 'q|' not in act(): fail('focus not on the question after Skip: ' + act())
    page.get_by_role('button', name='Give me a hint').click()
    if not act().endswith('|hintbox'): fail('focus not on the hint after Give me a hint: ' + act())
    page.get_by_role('button', name='Hide the hint').click()
    if not act().endswith('|hintbtn'): fail('focus lost after hiding the hint: ' + act())
    if page.locator('a.skip').count() != 1: fail('no skip link')
    page.reload(); page.wait_for_selector('#card .q'); page.keyboard.press('Tab')
    if page.evaluate("document.activeElement.className") != 'skip': fail('the skip link is not the first Tab stop')
    page.keyboard.press('Enter')
    if 'q|' not in act(): fail('the skip link does not move focus to the question')
    labs = []
    for i, it in enumerate(items):
        goto(page, i)
        no = it.get('no')
        lab = page.locator(f'#nav button[data-i="{i}"] b').inner_text()
        labs.append(lab)
        aria = page.locator(f'#nav button[data-i="{i}"]').get_attribute('aria-label')
        if not lab or len(lab) > 14: fail(f'{it["id"]}: nav label {lab!r} is empty or long')
        if lab in ('Investigation', 'Think', 'Go', 'Think harder', 'Go further', 'Start', 'Extra'): fail(f'{it["id"]}: nav label {lab!r} is only a group word (printed {no!r})')
        mm = re.match(r'(\d+\([a-z]\)|[A-Z]\d+)', no or '')
        if mm and mm.group(1) not in lab and not it.get('label'): fail(f'{it["id"]}: nav label {lab!r} lost the printed number {mm.group(1)!r} of {no!r}')
        if re.match(r'Investigation\b', no or '') and not lab.startswith('Inv'): fail(f'{it["id"]}: investigation label {lab!r}')
        if no and no not in aria: fail(f'{it["id"]}: accessible name {aria!r} lacks the full label {no!r}')
        if it['type'] in ('set', 'number', 'fields'):
            mode = page.locator('#ans input').first.get_attribute('inputmode')
            neg = any((x if isinstance(x, int) else 0) < 0 for x in ([f['answer'] for f in it['fields']] if it['type'] == 'fields' else (it['answer'] if it['type'] == 'set' else [it['answer']])))
            if (it['type'] == 'set' or neg) and mode != 'text': fail(f'{it["id"]}: list/negative item has inputmode {mode} (iPhone number pad has no comma or minus)')
            if not (it['type'] == 'set' or neg) and mode != 'numeric': fail(f'{it["id"]}: inputmode {mode}')
            if it['type'] == 'set' and 'Use commas between numbers' not in page.locator('#card').inner_text(): fail(f'{it["id"]}: no "Use commas between numbers" helper')
            for inp in page.locator('#ans input').all():
                if no and no.split(' ')[0] not in (inp.get_attribute('aria-label') or ''): fail(f'{it["id"]}: input label {inp.get_attribute("aria-label")!r} lacks the question number'); break
        if it['type'] == 'choice':
            if page.locator('#ans').evaluate("e => e.tagName") != 'FIELDSET' or not page.locator('#ans legend').inner_text().strip(): fail(f'{it["id"]}: radio group has no fieldset/legend')
    dup = sorted({l for l in labs if labs.count(l) > 1})
    if dup: fail(f'nav labels shared by two questions (the runner must add a/b): {dup}')
    foot = page.locator('.foot').inner_text()
    if 'nothing is sent anywhere' in foot or 'Your answers stay on this device' not in foot: fail('footer wording (sending off): ' + foot)
    if page.locator('meta[name=robots][content*=noindex]').count() != 1: fail('no noindex meta')
    ctx.close()
    for dark in (False, True):
        ctx, page = fresh(br, 390, 900, dark)
        ti = [k for k, x in enumerate(items) if x['type'] == 'selfcheck' and not x.get('paper')]
        if ti:
            goto(page, ti[0])
            cr = page.evaluate(r"""() => { const t = document.querySelector('#ans textarea'), cs = getComputedStyle(t, '::placeholder');
              const p = s => (s.match(/[\d.]+/g) || []).slice(0, 3).map(Number), lum = c => { const [r, g, b] = c.map(v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * r + .7152 * g + .0722 * b; };
              let bg = null, e = t; while (e && !bg) { const c = getComputedStyle(e).backgroundColor; if (c && !/rgba\(.*, 0\)|transparent/.test(c)) bg = c; e = e.parentElement; }
              const a = lum(p(cs.color)), b = lum(p(bg || 'rgb(255,255,255)')); return (Math.max(a, b) + .05) / (Math.min(a, b) + .05); }""")
            if cr < 4.5: fail(f'placeholder contrast {cr:.2f} (dark={dark}) is below 4.5')
        ctx.close()
    # sending switched on (token present): the footer says so and the 'I checked / I got it / not yet' ticks are visible after submit
    ctx = br.new_context(viewport={'width': 800, 'height': 900})
    page = ctx.new_page()
    posted = []
    def _send(r):
        posted.append(json.loads(r.request.post_data or '{}'))
        r.fulfill(status=200, content_type='application/json', body='{"ok":true,"marks":{}}')
    page.route('**/hol-send/**', _send)
    page.add_init_script("window.MI_SUBMIT={endpoint:'http://127.0.0.1:9/hol-send/x',token:'t'.repeat(40),unit:'hol-test',version:'v1'}")
    page.goto(URL); page.wait_for_selector('#card .q')
    typed_ids = [x['id'] for x in items if x['type'] == 'selfcheck' and not x.get('paper')]
    if typed_ids:       # the typed explanation goes in the payload (trimmed, at most 500 characters); 'answers' still says only '(written)'
        goto(page, idx_of(typed_ids[0])); page.locator('#ans textarea').fill('   ' + 'Because it is so. ' * 40 + '   ')
        if len(typed_ids) > 1: goto(page, idx_of(typed_ids[1])); page.locator('#ans textarea').fill('short note')
    foot = page.locator('.foot').inner_text()
    if 'are sent to your tutor so they can help you' not in foot or 'explanation boxes' not in foot or 'nothing is sent' in foot: fail('footer wording (sending on): ' + foot)
    si = [k for k, x in enumerate(items) if x['type'] == 'selfcheck']
    page.locator('#submit').click()
    if page.locator('#yes').count(): page.locator('#yes').click()
    page.wait_for_timeout(600)
    if not posted: fail('sending on: nothing was posted')
    elif typed_ids:
        pl = posted[-1]; ex = pl.get('explain') or {}
        if set(ex) != set(typed_ids[:2]): fail(f'explain keys {sorted(ex)} != typed {typed_ids[:2]}')
        t0 = ex.get(typed_ids[0], '')
        if not (0 < len(t0) <= 500) or t0 != t0.strip() or not t0.startswith('Because it is so.'): fail(f'explanation not trimmed and capped at 500: {len(t0)} {t0[:30]!r}')
        if len(typed_ids) > 1 and ex.get(typed_ids[1]) != 'short note': fail('short explanation not sent as typed')
        if pl['answers'][typed_ids[0]] != '(written)': fail('answers[...] must stay "(written)"')
        if any(k in pl for k in ('correct', 'marks', 'client_marks')): fail('payload carries a mark')
        if set(pl) - {'v', 'unit', 'unit_version', 'sid', 'rev', 'answers', 'self', 'explain'}: fail('unexpected payload fields ' + str(set(pl)))
        if page.locator('#card').inner_text().count('Because it is so') > 0 and not page.locator('#ans textarea').count(): pass
    if si:
        goto(page, si[0])
        for lbl in ('I checked it', 'I got it', 'Not yet'):
            if not page.get_by_role('button', name=lbl).count(): fail(f'sending on: no "{lbl}" tick')
    ctx.close()
    print('2c. focus moves to the question / hint / confirm / summary; skip link; question numbers on the buttons; fieldset legends; input modes; helper line; footer for both modes; noindex; placeholder contrast')

    # ---- 3: wrong answers, skips, reload
    ctx, page = fresh(br)
    skip = {3, 10, 20} if N > 21 else {1}
    for i in range(N):
        if i in skip: continue
        goto(page, i); enter(page, items[i], wrong=True)
    page.reload(); page.wait_for_selector('#card .q')
    page.locator('#submit').click()
    nblank = sum(1 for i, it in enumerate(items) if i in skip and it['type'] != 'selfcheck')
    if nblank:
        if page.evaluate("document.activeElement && document.activeElement.id") != 'askbox': fail('focus not on the Submit anyway? prompt')
        if not re.search(rf'\b{nblank} questions? (has|have) no answer', page.locator('#askbox').inner_text()): fail(f'confirm does not count exactly the {nblank} unanswered marked questions: ' + page.locator('#askbox').inner_text())
        page.locator('#keep').click()
        if page.evaluate("document.activeElement && document.activeElement.id") != 'submit' or page.locator('#summary').count(): fail('Keep working: focus not back on Submit, or it submitted')
        page.locator('#submit').click(); page.locator('#yes').click()
    elif page.locator('#askbox').count():
        fail('Submit anyway? shown although only self-check items are unanswered')
    for i, it in enumerate(items):
        c = cls(page, i)
        want = 'blank' if (i in skip and it['type'] != 'selfcheck') else ('self' if it['type'] == 'selfcheck' else ('blank' if i in skip else 'wrong'))
        if c != want: fail(f'{it["id"]}: marker {c}, expected {want}')
    for i in skip:
        if items[i]['type'] != 'selfcheck':
            goto(page, i)
            if 'skipped' not in page.locator('#sol').inner_text() or not page.locator('#sol li').count(): fail('skipped question has no solution')
    page.reload(); page.wait_for_selector('#summary')
    print(f'3. wrong answers (including wrong rule wordings) marked wrong, skipped questions marked "no answer" with solutions, answers and submitted state survive a reload')
    ctx.close()

    # ---- 4: variants through the page
    nvar = 0
    ctx, page = fresh(br)
    page.evaluate("window.__q=[];window.__orig=Math.random;Math.random=function(){return window.__q.length?window.__q.shift():0.5}")
    vitems = [(i, it) for i, it in enumerate(items) if 'tpl' in it]
    for i, it in vitems:
        goto(page, i); enter(page, it)
    page.locator('#submit').click()
    if page.locator('#yes').count(): page.locator('#yes').click()
    for i, it in vitems:
        tp = it['tpl']; names = list(tp['vars'])
        combos = list(itertools.product(*[tp['vars'][k] for k in names]))
        if len(combos) > 200:
            step = len(combos) / 150.0
            combos = [combos[int(k * step)] for k in range(150)] + [combos[0], combos[-1]]
        v = lesson.VARIANTS[it['id']]
        goto(page, i)
        for combo in combos:
            env = dict(zip(names, combo))
            fr = [(tp['vars'][nm].index(env[nm]) + 0.5) / len(tp['vars'][nm]) for nm in names]
            page.evaluate('q => { window.__q = q.slice(); }', fr)
            page.get_by_role('button', name=re.compile('similar one')).click()
            full = dict(env)
            for kk, e in tp.get('derive', {}).items(): full[kk] = B.ev(e, full)
            want_q = re.sub(r'\{(\w+)\}', lambda m: str(full[m.group(1)]) if m.group(1) in full else m.group(0), tp['q'])
            shown = page.locator('#simq .q').inner_text()
            if shown != want_q: fail(f'{it["id"]} {env}: shown "{shown}" != "{want_q}"')
            if 'frame' in tp:
                fr_txt = re.sub(r'\{(\w+)\}', lambda m: str(full[m.group(1)]) if m.group(1) in full else '', tp['frame'])
                row = page.locator('#simq .row').first.inner_text().replace('\n', '')
                if re.sub(r'\s+', '', row) != re.sub(r'\s+', '', fr_txt): fail(f'{it["id"]} {env}: frame "{row}" != "{fr_txt}"')
            ans = v['oracle'](env)
            if isinstance(ans, dict):
                boxes = page.locator('#simq input[data-sf]')
                for k, nm in enumerate(tp['answers']): boxes.nth(k).fill(str(ans[nm]))
            else:
                page.locator('#simq input[data-sf]').fill(str(int(ans)))
            if nvar % 25 == 0:      # a wrong first try shows the hint but not the answer; a second wrong try shows the answer
                for tryno in (1, 2):
                    if isinstance(ans, dict):
                        for k, nm in enumerate(tp['answers']): page.locator('#simq input[data-sf]').nth(k).fill('-77')
                    else:
                        page.locator('#simq input[data-sf]').fill('-77')
                    page.locator('#simq').get_by_role('button', name='Check').click()
                    txt = page.locator('#simfb').inner_text()
                    if tryno == 1 and ('The answer is' in txt or 'Hint:' not in txt): fail(f'{it["id"]}: first wrong try must show the hint only: {txt!r}')
                    if tryno == 2 and 'The answer is' not in txt: fail(f'{it["id"]}: second wrong try must show the answer')
                if isinstance(ans, dict):
                    for k, nm in enumerate(tp['answers']): page.locator('#simq input[data-sf]').nth(k).fill(str(ans[nm]))
                else:
                    page.locator('#simq input[data-sf]').fill(str(int(ans)))
            page.locator('#simq').get_by_role('button', name='Check').click()
            if 'Yes, that is right' not in page.locator('#simfb').inner_text(): fail(f'{it["id"]} {env}: oracle answer {ans} not accepted')
            nvar += 1
    print(f'4. {nvar} variants driven through the page: the question shown equals the template and the oracle answer is accepted')
    ctx.close()

    # ---- 5: layout checks and screenshots
    ctx, page = fresh(br, 390, 900)
    nsm = 0
    for i, it in enumerate(items):
        goto(page, i)
        if page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'): fail(f'{it["id"]}: horizontal scroll at 390 px')
        for b in figure_text_check(page, 390): fail(f'{it["id"]}: figure text {b} at 390 px'); nsm += 1
    ctx.close()
    ctx, page = fresh(br, 360, 900)
    for i, it in enumerate(items):
        goto(page, i)
        if page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'): fail(f'{it["id"]}: horizontal scroll at 360 px')
        for b in figure_text_check(page, 360, 11.5): fail(f'{it["id"]}: figure text {b} at 360 px (minimum 11.5 px)')
    ctx.close()
    # a label and its box never split at phone width: every box sits in one non-breaking group with the words just before it, and the label's last line is on the box's line
    GROUPS = """() => [...document.querySelectorAll('#ans .fg')].map(g => {
        const inp = g.querySelector('input'), lab = g.querySelector('.fl'), ib = inp.getBoundingClientRect(), card = document.querySelector('#card').getBoundingClientRect();
        const lb = lab ? lab.getBoundingClientRect() : null, gb = g.getBoundingClientRect();
        return { label: lab ? lab.textContent : '', ok_line: !lb || (ib.top + ib.height / 2 >= lb.top - 1 && ib.top + ib.height / 2 <= lb.bottom + 1), inside: gb.left >= card.left - 1 && gb.right <= card.right + 1, nowrap: getComputedStyle(g).flexWrap === 'nowrap' && ['flex', 'inline-flex'].includes(getComputedStyle(g).display) };
      }); """
    for w in (390, 360):
        ctx, page = fresh(br, w, 900)
        ng = 0
        for i, it in enumerate(items):
            if it['type'] != 'fields': continue
            goto(page, i)
            for g in page.evaluate(GROUPS):
                ng += 1
                if not g['ok_line']: fail(f'{it["id"]}: label {g["label"]!r} is not on the same line as its box at {w} px')
                if not g['inside']: fail(f'{it["id"]}: label group {g["label"]!r} leaves the card at {w} px')
                if not g['nowrap']: fail(f'{it["id"]}: box group is not a non-breaking flex group')
            want = {('p5', 4, '4b'): ['EBF', 'FCD'], ('p5', 4, '3a'): ['Height of triangle ABC', 'Area of ABC'], ('p5', 4, '3b'): ['Height of triangle ACD', 'Area of ACD'], ('p6', 4, '1c'): ['OUT =', 'IN for OUT 48'], ('p6', 4, 'C3'): ['IN 20 gives OUT', 'OUT 99 comes from IN']}.get((key, n, it['id']))
            if want:
                labs_ = [g['label'].replace('\xa0', ' ') for g in page.evaluate(GROUPS)]
                for wtxt in want:
                    if not any(wtxt in l for l in labs_): fail(f'{it["id"]}: no group labelled {wtxt!r} at {w} px (labels {labs_})')
        ctx.close()
    # solution figures (shown after Submit, inside the answer box): text at least 11 px at 360 px and 390 px, and not cut off by the figure's edge
    nsol = 0
    for w in (360, 390):
        ctx, page = fresh(br, w, 900)
        page.locator('#submit').click()
        if page.locator('#yes').count(): page.locator('#yes').click()
        for i, it in enumerate(items):
            if not it.get('sol_svg'): continue
            goto(page, i); nsol += 1
            if page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'): fail(f'{it["id"]}: horizontal scroll with the solution figure at {w} px')
            for b in figure_text_check(page, w, 11, '#solfig svg text'): fail(f'{it["id"]}: solution figure text {b} at {w} px')
            if page.evaluate("[...document.querySelectorAll('#solfig svg')].some(s => getComputedStyle(s).overflow !== 'visible')"): fail(f'{it["id"]}: solution svg clips its overflow')
        ctx.close()
    print(f'5b. {nsol} solution figures at 360 and 390 px: text at least 11 px and inside the figure, no horizontal scroll')
    print(f'5c. {ng} label+box groups at 390 and 360 px: each in one nowrap flex group, label on the box line, inside the card')
    print(f'5. all {N} questions fit at 390 and 360 px with no horizontal scroll; figure text is at least 11 px (11.5 px at 360 px) and inside its figure')

    def shot(name, w, h, dark=False, steps=None, full=False):
        c, p = fresh(br, w, h, dark)
        if steps: steps(p)
        if p.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'): fail(f'{name}: horizontal scroll')
        p.wait_for_timeout(150); p.screenshot(path=os.path.join(PROOF, name), full_page=full); c.close()

    def idx(i):
        return [k for k, x in enumerate(items) if x['id'] == i][0]

    def answer_some(p, upto=None, wrong_at=()):
        for i, it in enumerate(items[:upto]):
            if it['type'] != 'selfcheck':
                goto(p, i); enter(p, it, wrong=(i in wrong_at))

    def submitted(p):
        answer_some(p, None, wrong_at=(2, 7)); p.locator('#submit').click()
        if p.locator('#yes').count(): p.locator('#yes').click()

    figs = [x['id'] for x in items if x.get('svg')]
    paper_ids = [x['id'] for x in items if x.get('paper')]
    text_ids = [x['id'] for x in items if x['type'] == 'text']
    fid = figs[0] if figs else items[0]['id']
    pid = paper_ids[0] if paper_ids else fid
    tid = text_ids[0] if text_ids else fid
    vid = vitems[0][1]['id'] if vitems else fid
    shot('01_top_phone_light.png', 390, 1000, steps=lambda p: (answer_some(p, 6), goto(p, idx(tid))))
    shot('02_figure_question_phone_dark.png', 390, 1000, dark=True, steps=lambda p: goto(p, idx(pid)), full=True)
    shot('03_question_desktop_light.png', 900, 1100, steps=lambda p: (answer_some(p, 8), goto(p, idx(fid)), p.get_by_role('button', name='Give me a hint').click()))
    shot('04_confirm_submit_desktop_dark.png', 900, 1100, dark=True, steps=lambda p: (answer_some(p, 20), p.locator('#submit').click()), full=True)
    shot('05_paper_solution_phone_light.png', 390, 1000, steps=lambda p: (submitted(p), goto(p, idx(pid))), full=True)
    shot('06_paper_solution_desktop_dark.png', 900, 1200, dark=True, steps=lambda p: (submitted(p), goto(p, idx(pid))), full=True)
    shot('07_marked_wrong_phone_dark.png', 390, 1000, dark=True, steps=lambda p: (submitted(p), goto(p, 2)), full=True)
    shot('08_similar_desktop_light.png', 900, 1100, steps=lambda p: (submitted(p), goto(p, idx(vid)), p.get_by_role('button', name='Try a similar one').click()), full=True)
    for name, ix in (('09_lastfig_phone_light.png', figs[-1] if figs else fid),):
        shot(name, 390, 1000, steps=lambda p, ix=ix: goto(p, idx(ix)), full=True)
    if errors: fail('browser errors: ' + '; '.join(sorted(set(errors))[:5]))
    br.close()

# ---- 6. server-side marking: the keys made by practice/submit/make_keys.py, marked by the shared practice/submit/mark.js, agree with the page
import subprocess
sys.path.insert(0, os.path.join(H.ROOT, 'practice', 'submit'))
import make_keys                                   # noqa: E402
_k, _ver, _d, keys, _tags = make_keys.build(0, n, key)
nmodes = {}
for it, kr in zip(items, keys):      # the report mode is the item's own marking_mode: self = compare with a model answer / paper drawing, none = truly open
    if it['type'] != 'selfcheck':
        for fl in ('words', 'poly', 'equiv_frac', 'unit'):
            if it.get(fl) != kr.get(fl): fail(f'{it["id"]}: flag {fl} is {it.get(fl)!r} in the data but {kr.get(fl)!r} in the key')
        continue
    want = ('none', 'open') if it['marking_mode'] == 'none' and not it.get('paper') else ('self', 'selfcheck')
    if (kr['marking_mode'], kr['type']) != want: fail(f'{it["id"]}: self-check with marking_mode {it["marking_mode"]} exported as {kr["marking_mode"]}/{kr["type"]}')
    if it.get('paper') and kr['marking_mode'] != 'self': fail(f'{it["id"]}: paper-only item exported as {kr["marking_mode"]}')
    if re.search(r'\b(explain|why|how do you know)\b', (it['no'] + ' ' + it['q'][:60]).lower()) and kr['marking_mode'] != 'self' and not src[it['id']].get('marking_mode'):
        fail(f'{it["id"]}: an Explain item with no marking_mode of its own is exported as {kr["marking_mode"]}')
    nmodes[kr['marking_mode']] = nmodes.get(kr['marking_mode'], 0) + 1
cases = []
for it, kr in zip(items, keys):
    if kr['marking_mode'] != 'auto':
        cases.append(dict(rec=kr, v=None, want='self' if kr['marking_mode'] == 'self' else 'open')); continue
    t = it['type']
    right = [str(f['answer']) for f in it['fields']] if t == 'fields' else (', '.join(map(str, it['answer'])) if t == 'set' else (it['answer'][0] if t == 'text' else str(it['answer'])))
    wrong = [str(f['answer'] + 1) for f in it['fields']] if t == 'fields' else (str(it['answer'][0] + 100) if t == 'set' else ('zzz' if t == 'text' else ('No' if it['answer'] == 'Yes' else 'Yes') if t == 'choice' else str(it['answer'] + 1)))
    if t == 'choice':
        wrong = [o for o in it['options'] if o != it['answer']][0]
    cases.append(dict(rec=kr, v=right, want='right')); cases.append(dict(rec=kr, v=wrong, want='wrong')); cases.append(dict(rec=kr, v='', want='skipped'))
    if t == 'text' and it.get('poly'):      # the same rule written in other ways is right; changed rules are wrong
        a0 = it['answer'][0].replace('OUT = ', '').replace('out=', '')
        for v in (f'({a0})*1', f'0+{a0}', f'{a0}+0', f'OUT = {a0}', f'{a0} = {a0}'): cases.append(dict(rec=kr, v=v, want='right'))
        for v in (f'{a0}+1', f'{a0}-1', f'2*({a0})', f'({a0})+n'): cases.append(dict(rec=kr, v=v, want='wrong'))
    if t == 'text' and it.get('equiv_frac'):
        tk, rest = H.hlib.frac_tokens(it['answer'][0])
        if not rest and len(tk) > 1:
            cases.append(dict(rec=kr, v=', '.join(f'{2 * a}/{2 * b}' for a, b in tk), want='right')); cases.append(dict(rec=kr, v=', '.join(f'{a}/{b}' for a, b in reversed(tk)), want='wrong'))
            cases.append(dict(rec=kr, v=', '.join(f'{a + 1}/{b}' for a, b in tk), want='wrong'))
    if t in ('number', 'fields') and not it.get('unit') is False:      # unit and bracket forms of a whole number answer
        vals = [f['answer'] for f in it['fields']] if t == 'fields' else [it['answer']]
        if t == 'number': cases.append(dict(rec=kr, v=f'{vals[0]} cm2', want='right')); cases.append(dict(rec=kr, v=f'({vals[0]})', want='right')); cases.append(dict(rec=kr, v=f'{vals[0]}°C', want='right'))
    if t in ('number', 'fields'):       # number words never count unless the item declares words
        w1 = [f['answer'] for f in it['fields']] if t == 'fields' else [it['answer']]
        if all(0 <= x <= 9 for x in w1) and not it.get('words'):
            W = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            cases.append(dict(rec=kr, v=[W[x] for x in w1] if t == 'fields' else W[w1[0]], want='wrong'))
js = "const M=require(process.argv[1]);const c=JSON.parse(require('fs').readFileSync(0,'utf8'));console.log(JSON.stringify(c.map(x=>M.mark(x.rec,x.v).mark)))"
out = json.loads(subprocess.run(['node', '-e', js, os.path.join(H.ROOT, 'practice', 'submit', 'mark.js')], input=json.dumps(cases), capture_output=True, text=True, check=True).stdout)
bad = [(c['rec']['id'], c['want'], o) for c, o in zip(cases, out) if c['want'] != o]
if bad: fail(f'server marking differs: {bad[:5]}')
print(f'6. self-check items exported as {nmodes}; {len(keys)} server keys made; mark.js marks {len(cases)} right / wrong / blank / self answers as expected')

print('RESULT:', 'OK' if not fails else f'{len(fails)} FAILURES')
sys.exit(1 if fails else 0)
