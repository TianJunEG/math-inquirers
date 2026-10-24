#!/usr/bin/env python3
"""Browser test of the OPTIONAL send-to-tutor flag in practice/ext/public/sheet.js, against the LOCAL STUB endpoint (nothing leaves this machine).

    python3 practice/ext/build_ext.py 2 1 && python3 practice/submit/make_keys.py 2 1 && python3 practice/submit/test_submit.py

1. flag OFF (the pilot as it is): a whole session makes no request except loading the page's own files;
   flag set but no child session token: still none;
2. flag ON: a child answers (right, wrong, skipped, equivalent formats, sets in another order), submits; the browser's marks equal the server's re-marking;
   the request carries answers only (no mark, no 'correct'); the server never sees free text of the self-check item;
3. a lost response (stored, then 503): the retry with the same revision is a duplicate, one submission only;
4. offline at submit, tab closed, page opened later: the answers are sent then;
5. self-check ticks are recorded as self-marked, not as right.
"""
import json, os, re, subprocess, sys, time, urllib.request
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_keys                                       # noqa: E402
from playwright.sync_api import sync_playwright        # noqa: E402

DIST = os.path.join(os.path.dirname(HERE), 'ext', 'dist', 'l2u01')
key, ver, data, keys, _ = make_keys.build(2, 1)
kf = os.path.join(HERE, 'out'); os.makedirs(kf, exist_ok=True); kf = os.path.join(kf, 'ext-l2u01.keys.json')
json.dump(dict(unit='ext-l2u01', version=ver, keys=keys), open(kf, 'w'))
items = data['items']
fails = []
def fail(m): fails.append(m); print('FAIL', m)
def ok(c, m):
    if not c: fail(m)

proc = subprocess.Popen(['node', os.path.join(HERE, 'stub_server.mjs'), DIST, kf], stdout=subprocess.PIPE, text=True)
info = json.loads(proc.stdout.readline()); BASE = f'http://127.0.0.1:{info["port"]}'; TOKEN = info['token']
def state(): return json.load(urllib.request.urlopen(BASE + '/__state'))
def arm(mode, n): urllib.request.urlopen(urllib.request.Request(BASE + '/__arm', data=json.dumps({'mode': mode, 'n': n}).encode(), method='POST'))
def submits(): return [r for r in state()['requests'] if 'body' in r]

def fill(page, it, plan):
    """plan: right | wrong | skip | format (right answer typed in other formats)"""
    t = it['type']
    if plan == 'skip' or t == 'selfcheck':
        if t == 'selfcheck' and plan != 'skip': page.locator('#ans textarea').fill('my private thoughts 12345')
        return
    if t == 'fields':
        a = [f['answer'] for f in it['fields']]
        if plan == 'wrong': a = [x + 1 for x in a]
        boxes = page.locator('#ans input[data-f]')
        for i, x in enumerate(a):
            txt = f'{x:,}' if plan == 'format' and x >= 1000 else (f'  {x} ' if plan == 'format' else str(x))
            boxes.nth(i).fill(txt)
    elif t == 'set':
        a = list(it['answer'])
        if plan == 'wrong': a = a[:-1] + [a[-1] + 1]
        if plan == 'format' and not it['ordered']: a = list(reversed(a))
        page.locator('#ans input[type=text]').fill(', '.join(map(str, a)))
    elif t == 'choice':
        pick = it['answer'] if plan != 'wrong' else [o for o in it['options'] if o != it['answer']][0]
        page.locator('#ans label.opt', has_text=re.compile('^' + re.escape(pick) + '$')).click()

def goto(page, i): page.locator(f'#nav button[data-i="{i}"]').click()
INIT_ON = "window.MI_SUBMIT = {endpoint: '/api/practice/submit'}; try{sessionStorage.setItem('mi-child', JSON.stringify({name:'Mia',level:2,token:'%s'}));}catch(e){}" % TOKEN
INIT_NOTOKEN = "window.MI_SUBMIT = {endpoint: '/api/practice/submit'};"

with sync_playwright() as pw:
    br = pw.chromium.launch()
    def session(init=None):
        c = br.new_context(viewport={'width': 800, 'height': 900})
        if init: c.add_init_script(init)
        p = c.new_page(); errs = []
        p.on('pageerror', lambda e: errs.append(str(e)))
        p.goto(BASE + '/index.html'); p.wait_for_selector('#card .q'); return c, p, errs
    def run_child(p, plans):
        for i, it in enumerate(items):
            goto(p, i); fill(p, it, plans(i, it))
        p.locator('#submit').click()
        if p.locator('#yes').count(): p.locator('#yes').click()
        p.wait_for_selector('#summary')

    # ---- 1. flag off, and flag on without a token: no request at all
    for init, label in ((None, 'flag off'), (INIT_NOTOKEN, 'flag set, no token')):
        c, p, errs = session(init)
        run_child(p, lambda i, it: 'right')
        ok(not submits(), f'{label}: a submit request was made')
        ok(p.locator('#syncnote').count() == 0, f'{label}: the page mentions sending to the tutor')
        ok(not errs, f'{label}: page errors {errs}')
        ok(not [r for r in state()['requests'] if r.get('static') and not re.search(r'(index\.html|sheet\.js|\.json|\.css|\.woff2?|fonts|^/$)', r['static'])], f'{label}: unexpected file requested')
        c.close()
    print('1. flag off / no token: no submit request')

    # ---- 2. flag on: mixed child
    plans = lambda i, it: ['right', 'wrong', 'skip', 'format'][i % 4]
    c, p, errs = session(INIT_ON)
    ok(p.locator('#syncnote').count() == 1 and 'sent to your tutor' in p.locator('#syncnote').inner_text(), 'no plain notice before submit')
    run_child(p, plans)
    p.wait_for_function("document.querySelector('#syncnote') && /Sent to your tutor/.test(document.querySelector('#syncnote').textContent)", timeout=8000)
    sub = submits(); ok(len(sub) == 1, f'expected 1 submit, got {len(sub)}')
    body = json.loads(sub[0]['body'])
    ok(set(body) <= {'v', 'unit', 'unit_version', 'sid', 'rev', 'answers', 'self'}, f'unexpected fields sent: {set(body)}')
    ok('mark' not in sub[0]['body'].lower() and 'correct' not in sub[0]['body'].lower(), 'a mark or correct flag was sent')
    ok(body['unit_version'] == ver, f'unit version {body["unit_version"]} != {ver}')
    ok('my private thoughts' not in sub[0]['body'], 'free text of a self-check item was sent')
    stored = list(state()['stored'].values()); ok(len(stored) == 1, 'one stored submission')
    srv_marks = {r['item_id']: r['mark'] for r in stored[0]['rows']}
    cmap = {'right': 'right', 'wrong': 'wrong', 'blank': 'skipped', 'self': 'self'}
    bad = 0
    for i, it in enumerate(items):
        cc = p.locator(f'#nav button[data-i="{i}"]').get_attribute('class').split()[-1]
        want = cmap[cc]; got = srv_marks[it['id']]
        if got == 'open' and want == 'self': continue
        if want != got: bad += 1; fail(f'{it["id"]} ({it["type"]}, plan {plans(i, it)}): browser says {want}, server says {got}')
    kinds = {}
    for i, it in enumerate(items): kinds[plans(i, it)] = kinds.get(plans(i, it), 0) + 1
    print(f'2. {len(items)} items, plans {kinds}: browser and server marks agree on {len(items) - bad}; server counts {stored[0]["counts"]}')
    ok(any(v == 'right' for v in srv_marks.values()) and any(v == 'wrong' for v in srv_marks.values()) and any(v == 'skipped' for v in srv_marks.values()), 'test did not cover right, wrong and skipped')
    ok(not errs, f'page errors {errs}')

    # ---- 5. self tick (the open item is the only selfcheck in this unit)
    si = [i for i, it in enumerate(items) if it['type'] == 'selfcheck'][0]
    goto(p, si); p.locator('button', has_text='I got it').click()
    p.wait_for_function("document.querySelector('#syncnote') && /Sent/.test(document.querySelector('#syncnote').textContent)", timeout=8000)
    time.sleep(3.2)
    st = state(); ok(len(submits()) == 2, f'self tick should send once more, got {len(submits())}')
    ok(list(st['stored'].values())[0]['rev'] == 2, 'rev 2 stored after the tick')
    print('5. self tick sent as revision 2')
    c.close()

    # ---- 3. lost response -> retry -> duplicate
    n0 = len(state()['stored'])
    arm('store503', 1)
    c, p, errs = session(INIT_ON)
    run_child(p, lambda i, it: 'right')
    p.wait_for_function("document.querySelector('#syncnote') && /Sent to your tutor/.test(document.querySelector('#syncnote').textContent)", timeout=15000)
    st = state(); ok(len(st['stored']) == n0 + 1, 'retry created a second submission'); ok(st['duplicates'] == 1, f'expected 1 duplicate, got {st["duplicates"]}')
    print('3. response lost, retry accepted as a duplicate: one stored submission')
    c.close()

    # ---- 4. offline at submit, tab closed, opened later
    n0 = len(state()['stored'])
    c, p, errs = session(INIT_ON)
    c.set_offline(True)
    run_child(p, lambda i, it: 'right')
    time.sleep(0.5)
    ok('saved on this device' in p.locator('#syncnote').inner_text(), 'no kind offline message: ' + p.locator('#syncnote').inner_text())
    ok(len(state()['stored']) == n0, 'something was stored while offline')
    p.close()
    c.set_offline(False)
    p2 = c.new_page(); p2.goto(BASE + '/index.html'); p2.wait_for_selector('#card .q')
    p2.wait_for_function("document.querySelector('#syncnote') && /Sent to your tutor/.test(document.querySelector('#syncnote').textContent)", timeout=8000)
    ok(len(state()['stored']) == n0 + 1, 'the reopened page did not send the saved submission')
    ok(p2.locator('#summary').count() == 1, 'submitted state was not restored')
    print('4. offline submit, tab closed, reopened: sent once')
    c.close(); br.close()

proc.terminate()
print('FAILED' if fails else 'test_submit.py: all checks passed', len(fails) or '')
sys.exit(1 if fails else 0)
