#!/usr/bin/env python3
"""Playwright test of the "Other times" placeholders and the "Request another time" form against website/dist.
    python3 website/tests/interest_test.py [--shots DIR]
Portal mode is simulated by injecting window.MI_CONFIG and mocking the Supabase REST call; no network is used."""
import json, os, sys, threading, functools, http.server, socketserver
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
from playwright.sync_api import sync_playwright, expect

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.abspath(os.path.join(HERE, '..', 'dist'))
SHOTS = sys.argv[sys.argv.index('--shots') + 1] if '--shots' in sys.argv else None
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(Q, directory=DIST)); BASE = 'http://127.0.0.1:%d' % srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
slots = json.load(open(os.path.join(HERE, '..', 'data', 'interest_slots.json')))['slots']
fails = []
def check(name, fn):
    try: fn(); print('ok  ', name)
    except Exception as e: fails.append(name); print('FAIL', name, '\n    ', str(e)[:500])

def fill_valid(p, **kw):
    p.select_option('#itLevel', kw.get('level', '2')); p.select_option('#itAge', '8-9')
    p.fill('#itName', 'Mei'); p.fill('#itWa', kw.get('wa', '9123 4567')); p.check('#itConsent')

with sync_playwright() as pw:
    b = pw.chromium.launch()
    def ctx(w=1280, portal=False):
        c = b.new_context(viewport={'width': w, 'height': 900})
        if portal: c.add_init_script("window.MI_CONFIG={SUPABASE_URL:'https://mock.supabase.co',ANON_KEY:'mock-anon-key'};")
        return c
    errors = []

    # ---- placeholders on the cards (every group card has an Other times area) ----
    c = ctx(); p = c.new_page(); p.on('pageerror', lambda e: errors.append(str(e))); p.goto(BASE + '/')
    def cards():
        expect(p.locator('#sess .session')).to_have_count(6)
        expect(p.locator('#sess .othertimes')).to_have_count(6)
        p.locator('#sess .session').nth(0).locator('.othertimes summary').click()
        l1 = p.locator('#sess .session').nth(0).locator('.othertimes li')
        want = [s for s in slots if 1 in s['levels']]
        expect(l1).to_have_count(len(want))
        expect(l1.first).to_contain_text('Not open yet')
        expect(p.locator('#sess .session').nth(0).locator('.othertimes')).to_contain_text('not open for enrolment')
    check('each level card lists placeholder slots labelled Not open yet', cards)
    def preselect():
        p.locator('#sess .session').nth(1).locator('.othertimes summary').click()
        p.locator('#sess .session').nth(1).locator('a[data-interest="R2"]').click()
        expect(p.locator('input[name=itslot][value=R2]')).to_be_checked()
        expect(p.locator('input[name=itslot][value=R1]')).not_to_be_checked()
        expect(p.locator('#itLevel')).to_have_value('2')
    check("I'm interested preselects slot and level", preselect)
    def deep_link():
        p2 = c.new_page(); p2.goto(BASE + '/?level=5&interest=R4B#request-time')
        expect(p2.locator('input[name=itslot][value=R4B]')).to_be_checked(); expect(p2.locator('#itLevel')).to_have_value('5'); p2.close()
    check('deep link from a level page preselects', deep_link)
    def level_page():
        p3 = c.new_page(); p3.goto(BASE + '/ages-8-10/'); p3.locator('.othertimes summary').click(); expect(p3.locator('.othertimes li').first).to_contain_text('Not open yet')
        href = p3.locator('.othertimes a[data-interest="R3"]').get_attribute('href'); assert href == '/?level=3&interest=R3#request-time', href; p3.close()
    check('level page shows placeholders linking to the form', level_page)


    # ---- reorganised slot picker ----
    def picker():
        q = c.new_page(); q.goto(BASE + '/?level=6#request-time')
        expect(q.locator('.sgroup h3')).to_have_text(['Holiday program (Nov to Dec 2026)', 'Term time (2027)'])
        expect(q.locator('.gnote:visible').first).to_have_text('Not open yet: tell us which you would join.')
        want = [s['id'] for s in slots if 6 in s['levels']]
        vis = q.locator('.slotchip:visible input').evaluate_all('e=>e.map(x=>x.value)'); assert sorted(vis) == sorted(want), vis
        assert 'not open yet' not in q.locator('#itSlots').inner_text().lower().replace('not open yet: tell us which you would join.', '')
        assert '2027 term time' not in q.locator('#itSlots').inner_text()
        expect(q.locator('#itCount')).to_have_text('0 times selected')
        q.locator('.slotchip:visible').first.click(); expect(q.locator('#itCount')).to_have_text('1 time selected')
        q.locator('#itLevel').select_option('1'); expect(q.locator('.slotchip:visible')).to_have_count(len([s for s in slots if 1 in s['levels'] or s['id'] == vis[0]]))
        q.click('#itAll'); expect(q.locator('.slotchip:visible')).to_have_count(len(slots)); q.click('#itAll')
        q.click('#itClear'); expect(q.locator('#itCount')).to_have_text('0 times selected')
        q.check('input[name=itwin][value=sat]'); expect(q.locator('#itCount')).to_have_text('1 time selected')
        hs = q.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth'); assert hs <= 0, hs
        for h in q.locator('.slotchip:visible').evaluate_all('e=>e.map(x=>x.getBoundingClientRect().height)'): assert h >= 44, h
        q.close()
    check('slots grouped, filtered by level, count/clear/show-all work', picker)
    def phone_fit():
        c3 = ctx(400); q = c3.new_page(); q.goto(BASE + '/?level=3#request-time')
        assert q.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth') <= 0
        c3.close()
    check('no horizontal scroll at 400px', phone_fit)

    # ---- validation ----
    def validation():
        p.goto(BASE + '/'); p.click('#itSubmit')
        for t in ["Choose your child's age range.", 'Tick at least one time', 'add your first name', 'Give a WhatsApp number or an email', 'Please tick the box']:
            expect(p.locator('#itForm')).to_contain_text(t)
        p.select_option('#itAge', '6-7'); p.check('input[name=itwin][value=sat]'); p.fill('#itName', 'Mei'); p.fill('#itEmail', 'nope'); p.check('#itConsent'); p.click('#itSubmit')
        expect(p.locator('#itForm')).to_contain_text('does not look right')
        p.fill('#itEmail', ''); p.fill('#itWa', '12'); p.click('#itSubmit'); expect(p.locator('#itForm')).to_contain_text('8 or more digits')
    check('validation messages (age, time, name, contact, email, phone, consent)', validation)

    # ---- WhatsApp fallback mode (no MI_CONFIG) ----
    def wa():
        p.goto(BASE + '/?level=2&interest=R1'); fill_valid(p); p.check('input[name=itwin][value=sat]'); p.fill('#itOther', 'Tue after 4pm'); p.fill('#itNote', 'Sibling too')
        p.click('#itSubmit')
        href = p.locator('#itWaLink').get_attribute('href'); assert href.startswith('https://wa.me/6598805962?text='), href
        from urllib.parse import unquote
        txt = unquote(href.split('text=')[1])
        for s in ['Level: Level 2 (ages 7-9)', "Child's age: 8 to 9", 'Holiday: Wed & Thu 9:00-10:30am', 'Saturday', 'Other: Tue after 4pm', 'Parent: Mei', 'WhatsApp 9123 4567', 'Note: Sibling too']:
            assert s in txt, (s, txt)
        assert 'child' not in txt.lower().replace("child's age", ''), txt     # no child name field anywhere
        expect(p.locator('#itPre')).to_contain_text('Hi! I')
        expect(p.locator('#itModeNote')).to_contain_text('+65 9880 5962')
    check('WhatsApp fallback builds a prefilled message to +65 9880 5962', wa)
    def rate_limit_client():
        p.reload(); fill_valid(p, wa='8111 2222'); p.check('input[name=itwin][value=sun]'); p.click('#itSubmit')
        expect(p.locator('#itMsg')).to_contain_text('wait a minute')
    check('client-side 1-minute throttle', rate_limit_client)
    def honeypot():
        c2 = ctx(); q = c2.new_page(); q.goto(BASE + '/'); fill_valid(q); q.check('input[name=itwin][value=sat]')
        q.evaluate("document.getElementById('itHp').value='http://spam'"); q.click('#itSubmit'); expect(q.locator('#itWaLink')).to_have_count(0); c2.close()
    check('honeypot filled => nothing happens', honeypot)
    c.close()

    # ---- portal mode (RPC mocked) ----
    c = ctx(portal=True); p = c.new_page(); calls = []
    def route(r):
        req = r.request
        if req.method == 'OPTIONS': return r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'})
        calls.append((req.url, req.headers, json.loads(req.post_data)))
        body = calls_response[0]
        r.fulfill(status=body[0], content_type='application/json', headers={'access-control-allow-origin': '*'}, body=json.dumps(body[1]))
    calls_response = [(200, {'ok': True, 'status': 'received'})]
    c.route('https://mock.supabase.co/**', route)
    p.goto(BASE + '/?level=3&interest=R3')
    def portal_ok():
        fill_valid(p, level='3'); p.check('input[name=itwin][value=wkday-eve]'); p.fill('#itOther', 'Mon 6pm'); p.click('#itSubmit')
        expect(p.locator('#itMsg')).to_contain_text('Thank you. We have your request'); assert len(calls) == 1
        url, hdr, body = calls[0]
        assert url == 'https://mock.supabase.co/rest/v1/rpc/submit_interest_request', url
        assert hdr['apikey'] == 'mock-anon-key' and hdr['authorization'] == 'Bearer mock-anon-key'
        assert body['p_level'] == 3 and body['p_age_band'] == '8-9' and body['p_slots'] == ['R3'] and body['p_windows'] == ['wkday-eve'] and body['p_other_time'] == 'Mon 6pm'
        assert body['p_first_name'] == 'Mei' and body['p_whatsapp'] == '91234567' and body['p_email'] is None and body['p_consent'] is True and body['p_consent_version']
        expect(p.locator('#itModeNote')).to_contain_text('stored securely')
    check('portal mode calls submit_interest_request with the anon key', portal_ok)
    def portal_dupe():
        p.evaluate("localStorage.clear()"); calls_response[0] = (200, {'ok': True, 'status': 'already_received'}); fill_valid(p); p.check('input[name=itwin][value=sat]'); p.click('#itSubmit')
        expect(p.locator('#itMsg')).to_contain_text('already have a request')
    check('portal duplicate-day response is shown kindly', portal_dupe)
    def portal_fail():
        p.evaluate("localStorage.clear()"); calls_response[0] = (500, {'message': 'boom'}); fill_valid(p); p.check('input[name=itwin][value=sat]'); p.click('#itSubmit')
        expect(p.locator('#itWaLink')).to_have_attribute('href', __import__('re').compile(r'^https://wa\.me/6598805962'))
        expect(p.locator('#itMsg')).to_contain_text('send it to us on WhatsApp instead')
    check('portal error falls back to WhatsApp', portal_fail)
    def portal_invalid():
        p.evaluate("localStorage.clear()"); calls_response[0] = (400, {'message': 'invalid_input'}); fill_valid(p); p.check('input[name=itwin][value=sat]'); p.click('#itSubmit')
        expect(p.locator('#itMsg')).to_contain_text('not accepted')
    check('portal invalid_input shows a message', portal_invalid)
    c.close()

    # ---- no-JS ----
    c = b.new_context(java_script_enabled=False, viewport={'width': 1280, 'height': 900}); q = c.new_page(); q.goto(BASE + '/ages-7-9/')
    check('no-JS level page still shows static placeholders', lambda: expect(q.locator('.othertimes li').first).to_contain_text('Not open yet'))
    q.goto(BASE + '/')
    check('no-JS home shows the noscript WhatsApp note', lambda: (_ for _ in ()).throw(AssertionError('missing')) if '+65 9880 5962' not in q.locator('#request-time').inner_text() else None)
    c.close()

    # ---- empty state: no slots for a level => generic text (render function) ----
    sys.path.insert(0, os.path.join(HERE, '..')); import interest_ui
    def empty():
        h = interest_ui.other_times_block(1, []); assert '<li>' not in h and 'Request another time' in h and 'None of the Level 1 times' in h
        f = interest_ui.form_section('1', '1'); assert 'id="itSlots"' in f and 'class="slotchip"' in f
    check('empty slot list renders a generic request link', empty)

    # ---- screenshots ----
    if SHOTS:
        os.makedirs(SHOTS, exist_ok=True)
        for w, name in ((1280, 'desktop'), (375, 'phone')):
            c = ctx(w); q = c.new_page(); q.goto(BASE + '/'); q.wait_for_selector('#sess .othertimes')
            q.locator('#classes').screenshot(path=os.path.join(SHOTS, name + '_cards.png'))
            q.goto(BASE + '/?level=2&interest=R2'); q.wait_for_timeout(300); q.locator('#request-time').screenshot(path=os.path.join(SHOTS, name + '_form.png'))
            q.click('#itSubmit'); q.locator('#request-time').screenshot(path=os.path.join(SHOTS, name + '_form_errors.png'))
            q.goto(BASE + '/ages-7-9/'); q.locator('#times').screenshot(path=os.path.join(SHOTS, name + '_levelpage.png'))
            hs = q.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth'); print(name, 'horizontal overflow px:', hs)
            c.close()
    b.close()
if errors: print('page errors:', errors); fails.append('page errors')
# the shop tests (cart, interest form, price rule) live in shop_test.py and run with this file
import subprocess
if subprocess.run([sys.executable, os.path.join(HERE, 'shop_test.py')] + (['--shots', os.path.join(SHOTS, 'shop')] if SHOTS else [])).returncode: fails.append('shop tests')
print('FAILED' if fails else 'ALL PASSED'); sys.exit(1 if fails else 0)
