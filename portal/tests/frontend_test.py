#!/usr/bin/env python3
"""Playwright (1.56.0, chromium from PLAYWRIGHT_BROWSERS_PATH) test of the portal front end against tests/mock_supabase.js.
    python3 portal/tests/frontend_test.py"""
import json, os, sys, threading, tempfile, functools, http.server, socketserver
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
from playwright.sync_api import sync_playwright, expect

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, '..', 'public')
sched = json.load(open(os.path.join(HERE, '..', '..', 'website', 'data', 'beta_schedule.json')))
groups = [dict(id=g['id'], level=g['level'], name=g['name'], ages=g['ages'], seats=g['seats'], sessions=g['sessions'], first_label=g['first'], last_label=g['last'], fee_cents=25000) for g in sched['groups']]
SEED = 'window.__SEED__=%s;' % json.dumps(dict(groups=groups, extraTaken={'L2A': 8, 'L3A': 7}))
MOCK = open(os.path.join(HERE, 'mock_supabase.js')).read()
MODE = ['paynow_manual']
CONFIG = lambda: "window.MI_CONFIG={SUPABASE_URL:'https://mock.supabase.co',ANON_KEY:'mock-anon',PAYMENT_MODE:'%s',PAYNOW_TO:'UEN 000TEST',SITE_NAME:'Math Inquirers'};" % MODE[0]

root = tempfile.mkdtemp(); os.symlink(os.path.abspath(PUB), os.path.join(root, 'portal'))
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' https://mock.supabase.co; base-uri 'self'")
        super().end_headers()
socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(Q, directory=root)); PORT = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = 'http://127.0.0.1:%d' % PORT

fails = []
def check(name, fn):
    try: fn(); print('ok  ', name)
    except Exception as e: fails.append(name); print('FAIL', name, '\n    ', str(e)[:400])

def new_ctx(b, w=375):
    ctx = b.new_context(viewport={'width': w, 'height': 800})
    ctx.add_init_script(SEED + MOCK)
    ctx.route('**/portal/config.js', lambda r: r.fulfill(body=CONFIG(), content_type='application/javascript'))
    ctx.route('**/portal/vendor/supabase.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
    ctx.route('https://mock.supabase.co/**', lambda r: r.abort())
    return ctx

with sync_playwright() as pw:
    b = pw.chromium.launch()
    ctx = new_ctx(b); page = ctx.new_page()
    errors = []; external = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' and 'Failed to load resource' not in m.text else None)
    page.on('request', lambda r: external.append(r.url) if not r.url.startswith(BASE) and not r.url.startswith('data:') and not r.url.startswith('https://checkout.stripe.com/') else None)
    def overflow(): return page.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')

    # --- signed-out ---
    page.goto(BASE + '/portal/')
    check('login form shown, no horizontal scroll at 375px', lambda: (expect(page.get_by_role('heading', name='Parent portal')).to_be_visible(), overflow() <= 0 or (_ for _ in ()).throw(AssertionError('overflow %s' % overflow()))))
    def bad_login():
        page.fill('#email', 'nobody@example.com'); page.fill('#password', 'wrongwrong'); page.get_by_role('button', name='Log in', exact=True).last.click()
        expect(page.locator('.msg.err')).to_contain_text('not right')
    check('wrong password shows friendly error', bad_login)
    def signup():
        page.get_by_role('button', name='Sign up').click()
        page.fill('#fullname', 'Test Parent'); page.fill('#email', 'parent@example.com'); page.fill('#password', 'longenough1')
        page.get_by_role('button', name='Create parent account').click()
        expect(page.get_by_role('heading', name='Hello, Test Parent')).to_be_visible()
    check('sign up creates account and lands in portal', signup)

    # --- children ---
    def add_child_bad_pin():
        page.fill('#cname', 'Mia'); page.fill('#cpin', '12'); page.get_by_role('button', name='Add child').click()
        expect(page.locator('.msg.err')).to_contain_text('4 to 6 digits')
    check('PIN must be 4-6 digits', add_child_bad_pin)
    def add_child():
        page.fill('#cname', 'Mia'); page.select_option('#clevel', '1'); page.fill('#cpin', '7391'); page.get_by_role('button', name='Add child').click()
        expect(page.locator('[data-child]')).to_have_count(1); expect(page.locator('[data-child]')).to_contain_text('Mia')
    check('add child', add_child)
    def dup():
        page.fill('#cname', 'mia'); page.fill('#cpin', '9152'); page.get_by_role('button', name='Add child').click()
        expect(page.locator('.msg.err')).to_contain_text('already have a child')
    check('duplicate name rejected', dup)
    def xss():
        page.fill('#cname', '<img src=x onerror=window.__x=1>'); page.select_option('#clevel', '2'); page.fill('#cpin', '3584'); page.get_by_role('button', name='Add child').click()
        expect(page.locator('[data-child]')).to_have_count(2)
        assert page.evaluate('window.__x') is None and page.locator('[data-child] img').count() == 0
    check('child name is rendered as text (no HTML injection)', xss)
    def edit_child():
        page.locator('[data-child]').nth(1).get_by_role('button', name='Edit').click()
        page.locator('[data-child]').nth(1).get_by_label('Display name').fill('Ben'); page.locator('[data-child]').nth(1).get_by_label('Level').select_option('3')
        page.locator('[data-child]').nth(1).get_by_role('button', name='Save').click()
        expect(page.locator('[data-child]').nth(1)).to_contain_text('Level 3')
    check('edit child name + level', edit_child)

    # --- consents + enrol ---
    def enrol_blocked():
        expect(page.locator('[data-enrol-for]').first.get_by_text('Joining a live group needs four agreements', exact=False)).to_be_visible()
        page.locator('input[name^="grp-"]').first.check()
        expect(page.get_by_role('button', name='Reserve a place').first).to_be_disabled()
    check('cannot reserve before consents', enrol_blocked)
    def consents():
        for t in ['contact', 'terms', 'recording', 'childs_work']: page.check('#consent-' + t)
        page.click('#save-consents'); expect(page.locator('.msg.ok')).to_contain_text('Agreements saved')
        db = page.evaluate('window.__mockDb().consents'); assert len(db) == 4 and all(c['terms_version'].startswith('terms-') and c['granted'] for c in db), db
        assert page.evaluate("document.querySelector('#consent-feedback_quotes').checked") is False
    check('record the four needed consents with versions', consents)
    def reserve():
        page.locator('[data-enrol-for]').first.locator('input[name^="grp-"]').first.check()
        page.get_by_role('button', name='Reserve a place').first.click()
        expect(page.locator('[data-enrolment]')).to_have_count(1)
        expect(page.locator('[data-ref]')).to_have_text(__import__('re').compile(r'^MI-[A-Z2-9]{6}$'))
        expect(page.locator('[data-pay-status]')).to_contain_text('pending'); expect(page.locator('[data-enrolment]')).to_contain_text('S$250.00')
        expect(page.locator('[data-enrolment]')).to_contain_text('UEN 000TEST')
    check('reserve L1A: pending payment with PayNow reference shown', reserve)
    def stripe_mode():
        MODE[0] = 'stripe'
        seen = []
        def fake(r):
            seen.append(r.request.post_data_json); r.fulfill(status=200, content_type='application/json', body=json.dumps({'url': 'https://checkout.stripe.com/c/pay/cs_test_fake1'}))
        page.route('**/api/stripe-create-checkout', fake)
        page.route('https://checkout.stripe.com/**', lambda r: r.fulfill(status=200, content_type='text/html', body='<p>stripe stand-in</p>'))   # only Stripe's own host may be navigated to
        page.goto(BASE + '/portal/?cancelled=x')
        expect(page.locator('[data-return="cancelled"]')).to_contain_text('nothing was charged')
        expect(page.locator('[data-ref]')).to_have_count(0)            # no manual PayNow reference in stripe mode
        page.locator('[data-pay-online]').click()
        page.wait_for_url('https://checkout.stripe.com/**'); assert len(seen) == 1 and 'enrolment_id' in seen[0], seen
        page.goto(BASE + '/portal/?paid=x&session_id=cs_test')
        expect(page.locator('[data-return="paid"]')).to_contain_text('Stripe')
        MODE[0] = 'paynow_manual'; page.unroute('**/api/stripe-create-checkout'); page.goto(BASE + '/portal/')
        expect(page.locator('[data-ref]')).to_have_count(1)            # manual PayNow stays the default
    check('stripe mode: Pay button calls our function and redirects; return pages; manual mode intact', stripe_mode)
    def fullgrp():
        # child 'Ben' is level 3: L3A has 7 extra taken -> 1 left; the xss-named child moved to level 3 already. Level 2 group is full (8 extra)
        txt = page.locator('[data-enrol-for]').first.inner_text(); assert 'seats left' in txt, txt
    check('seat count shown', fullgrp)
    def level_lock():
        page.locator('[data-child]').first.get_by_role('button', name='Edit').click()
        page.locator('[data-child]').first.get_by_label('Level').select_option('2'); page.locator('[data-child]').first.get_by_role('button', name='Save').click()
        expect(page.locator('.msg.err')).to_contain_text('level cannot change')
    check('level locked while enrolled', level_lock)
    def overflow_ok(): assert overflow() <= 0, overflow()
    check('no horizontal overflow when signed in (375px)', overflow_ok)

    # --- child sign-in stub ---
    fam = page.inner_text('#family-code')
    cp = ctx.new_page(); cp.goto(BASE + '/portal/child/')
    def child_wrong():
        cp.fill('#code', fam); cp.fill('#name', 'Mia'); cp.fill('#pin', '0000'); cp.get_by_role('button', name='Sign in').click()
        expect(cp.locator('.msg.err')).to_contain_text('did not work')
    check('child wrong PIN gives generic error', child_wrong)
    def child_needs_online_consent():
        # a live-group family that has not ticked the online practice agreement: sign-in is refused quietly (child_start_session needs it)
        cp.fill('#code', fam); cp.fill('#name', 'Mia'); cp.fill('#pin', '7391'); cp.get_by_role('button', name='Sign in').click()
        expect(cp.locator('.msg.err')).to_contain_text('did not work'); assert cp.url.endswith('/portal/child/')
        page.check('#consent-online_practice'); page.click('#save-consents'); expect(page.locator('.msg.ok')).to_contain_text('Agreements saved')
    check('child sign-in needs the online practice agreement', child_needs_online_consent)
    def child_ok():
        cp.goto(BASE + '/portal/child/')   # a fresh page reads the saved agreements (the mock keeps one copy of the data per page load)
        cp.fill('#code', fam.lower()); cp.fill('#name', ' mia '); cp.fill('#pin', '7391'); cp.get_by_role('button', name='Sign in').click()
        expect(cp.locator('#hello')).to_have_text('Hello, Mia!'); assert cp.url.endswith('/portal/practice/')
        expect(cp.locator('#nothing-open')).to_be_visible()      # a live-group child with no published unit yet: nothing to open, no links
    check('child name+PIN leads to the practice list', child_ok)
    def child_out():
        cp.click('#bye'); expect(cp.get_by_role('heading', name='Hi! Sign in to practise')).to_be_visible()
        cp.goto(BASE + '/portal/practice/'); cp.wait_for_url('**/portal/child/')
    check('practice page redirects when not signed in', child_out)

    # --- admin ---
    page.click('#signout'); expect(page.get_by_role('heading', name='Parent portal')).to_be_visible()
    ap = ctx.new_page(); ap.goto(BASE + '/portal/admin/')
    def admin_forbidden():
        # a parent (non-admin) logging in to /admin gets 'Not an admin'
        ap.fill('#email', 'parent@example.com'); ap.fill('#password', 'longenough1'); ap.get_by_role('button', name='Log in').click()
        expect(ap.get_by_role('heading', name='Not an admin')).to_be_visible(); ap.get_by_role('button', name='Log out').click()
    check('non-admin sees Not an admin', admin_forbidden)
    def admin_flow():
        ap.fill('#email', 'owner@example.com'); ap.fill('#password', 'ownerpass1'); ap.get_by_role('button', name='Log in').click()
        expect(ap.locator('#enrolments tbody tr')).to_have_count(1)
        expect(ap.locator('#fill tr[data-group="L1A"]')).to_contain_text('1')
        ap.once('dialog', lambda d: d.accept()); ap.locator('[data-mark-paid]').click()
        expect(ap.locator('.msg.ok')).to_contain_text('paid')
        ap.get_by_role('button', name='Paid', exact=True).click(); expect(ap.locator('#enrolments tbody tr')).to_have_count(1)
        expect(ap.locator('#enrolments tbody tr')).to_contain_text('paid')
    check('admin lists enrolments, marks paid, sees group fill', admin_flow)
    def admin_interest():
        ap.route('**/interest-slots.json', lambda r: r.fulfill(body=json.dumps({'slots': [{'id': 'R1', 'label': 'Wed & Thu mornings'}]}), content_type='application/json'))
        ap.locator('[data-view=interest]').click()
        expect(ap.get_by_role('heading', name='Interest in other times')).to_be_visible()
        expect(ap.locator('#tally tr[data-level="2"].tot')).to_contain_text('2')
        expect(ap.locator('#tally tr[data-key="R1"]')).to_contain_text('Wed & Thu mornings (R1)')
        expect(ap.locator('#tally tr[data-key="R1"]')).to_contain_text('2')
        expect(ap.locator('#requests tbody tr')).to_have_count(2)
        expect(ap.locator('#requests')).to_contain_text('sam@example.com')
        ap.locator('[data-request=i1] [data-set-status]').click(); expect(ap.locator('[data-request=i1] .pill')).to_have_text('contacted')
        ap.once('dialog', lambda d: d.accept()); ap.locator('[data-delete=i2]').click(); expect(ap.locator('#requests tbody tr')).to_have_count(1)
    check('admin Interest tab: tally, list, mark contacted, delete', admin_interest)
    ap.click('#signout')
    def parent_sees_paid():
        page.reload(); page.fill('#email', 'parent@example.com'); page.fill('#password', 'longenough1'); page.get_by_role('button', name='Log in', exact=True).last.click()
        expect(page.locator('[data-pay-status]')).to_contain_text('paid'); expect(page.locator('[data-enrolment]')).to_contain_text('confirmed')
    check('parent sees paid + confirmed', parent_sees_paid)
    def cant_cancel_paid():
        assert page.get_by_role('button', name='Cancel this reservation').count() == 0
    check('no self-cancel button once paid', cant_cancel_paid)

    # --- delete my data ---
    def delete_data():
        page.locator('summary', has_text='Delete my data').click()
        page.once('dialog', lambda d: d.accept())
        page.fill('#del-confirm', 'nope'); page.click('#del-btn'); expect(page.locator('.msg.err')).to_contain_text('Type DELETE')
        page.locator('summary', has_text='Delete my data').click(); page.fill('#del-confirm', 'DELETE'); page.click('#del-btn')
        expect(page.get_by_role('heading', name='Parent portal')).to_be_visible()
        db = page.evaluate('window.__mockDb()'); assert not any(u['email'] == 'parent@example.com' for u in db['users']) and not db['children']
    check('delete my data removes login and children', delete_data)

    # --- full group (separate family) + magic link + confirm-email signup ---
    def full_group():
        p2 = ctx.new_page(); p2.goto(BASE + '/portal/')
        p2.get_by_role('button', name='Sign up').click(); p2.fill('#fullname', 'Fam Two'); p2.fill('#email', 'two@example.com'); p2.fill('#password', 'longenough2'); p2.get_by_role('button', name='Create parent account').click()
        p2.fill('#cname', 'Zoe'); p2.select_option('#clevel', '2'); p2.fill('#cpin', '1873'); p2.get_by_role('button', name='Add child').click()
        opt = p2.locator('[data-enrol-for] label.opt'); expect(opt.first).to_contain_text('Full'); expect(opt.first.locator('input')).to_be_disabled()
    check('full group cannot be chosen', full_group)
    def magic():
        p3 = new_ctx(b).new_page(); p3.goto(BASE + '/portal/'); p3.get_by_role('button', name='Magic link').click(); p3.fill('#email', 'x@example.com'); p3.get_by_role('button', name='Email me a link').click()
        expect(p3.locator('.msg.ok')).to_contain_text('Check your email')
    check('magic link request', magic)

    def forgot():
        p4 = new_ctx(b).new_page(); p4.goto(BASE + '/portal/')
        p4.locator('#forgot-link').click(); expect(p4.get_by_role('heading', name='Parent portal')).to_be_visible()
        assert p4.evaluate('document.activeElement.id') == 'email'
        assert p4.locator('#password').count() == 0 and p4.locator('#forgot-link').count() == 0
        p4.get_by_role('button', name='Email me a reset link').click(); expect(p4.locator('.msg.err')).to_contain_text('enter your email')
        for em in ['two@example.com', 'nobody-at-all@example.com']:       # existing and unknown email: identical message
            p4.fill('#email', em); p4.get_by_role('button', name='Email me a reset link').click()
            expect(p4.locator('.msg.ok')).to_have_text('If that email has an account, a reset link is on its way. Check your inbox (and spam), then click the link on this device.')
        r = p4.evaluate('window.__resets'); assert [x['email'] for x in r] == ['two@example.com', 'nobody-at-all@example.com'] and r[0]['redirectTo'] == BASE + '/portal/', r
        p4.get_by_role('button', name='Back to log in').click(); expect(p4.locator('#password')).to_be_visible()
    check('forgot password: request, neutral message for any email, redirectTo is the portal', forgot)
    def recovery():
        p5 = ctx.new_page(); p5.goto(BASE + '/portal/')
        p5.evaluate("window.__recover('two@example.com')")
        expect(p5.get_by_role('heading', name='Choose a new password')).to_be_focused()
        p5.get_by_role('button', name='Save new password').click(); expect(p5.locator('.msg.err')).to_contain_text('at least 8'); assert p5.evaluate('document.activeElement.id') == 'newpw'
        p5.fill('#newpw', 'short'); p5.fill('#newpw2', 'short'); p5.get_by_role('button', name='Save new password').click(); expect(p5.locator('.msg.err')).to_contain_text('at least 8')
        p5.fill('#newpw', 'brandnewpass1'); p5.fill('#newpw2', 'brandnewpass2'); p5.get_by_role('button', name='Save new password').click()
        expect(p5.locator('.msg.err')).to_contain_text('not the same'); assert p5.evaluate('document.activeElement.id') == 'newpw2'
        assert p5.evaluate("document.querySelector('#newpw').type") == 'password'; p5.check('#showpw'); assert p5.evaluate("document.querySelector('#newpw').type + document.querySelector('#newpw2').type") == 'texttext'
        assert p5.locator('#newpw').bounding_box()['height'] >= 40 and p5.locator('button[type=submit]').bounding_box()['height'] >= 44
        p5.evaluate('window.__UPDATE_FAIL__=true'); p5.fill('#newpw2', 'brandnewpass1'); p5.get_by_role('button', name='Save new password').click()
        expect(p5.locator('.msg.err')).to_contain_text('Something went wrong'); assert 'xyz' not in p5.locator('.msg.err').inner_text()
        p5.evaluate('window.__UPDATE_FAIL__=false'); p5.get_by_role('button', name='Save new password').click()
        expect(p5.get_by_role('heading', name='Hello, Fam Two')).to_be_visible(); expect(p5.locator('.msg.ok')).to_contain_text('password is changed')
        assert [u['password'] for u in p5.evaluate('window.__mockDb().users') if u['email'] == 'two@example.com'] == ['brandnewpass1']
    check('recovery screen: validation, show/hide, safe error, success signs in', recovery)
    def recovery_stays():
        p6 = ctx.new_page(); p6.goto(BASE + '/portal/'); p6.evaluate("window.__recover('two@example.com')")
        p6.wait_for_timeout(300); expect(p6.get_by_role('heading', name='Choose a new password')).to_be_visible()   # later SIGNED_IN must not skip the screen
    check('recovery screen is not replaced by the later SIGNED_IN event', recovery_stays)

    check('no JS errors', lambda: (not errors) or (_ for _ in ()).throw(AssertionError(errors)))
    check('no requests outside the page origin (CSP-friendly, no CDN)', lambda: (not external) or (_ for _ in ()).throw(AssertionError(external)))
    # desktop layout and dark mode
    ctx2 = new_ctx(b, 1100); ctx2.emulate_media = None
    d = ctx2.new_page(); d.emulate_media(color_scheme='dark'); d.goto(BASE + '/portal/')
    check('desktop + dark mode render', lambda: expect(d.get_by_role('heading', name='Parent portal')).to_be_visible())
    d.screenshot(path=os.path.join(tempfile.gettempdir(), 'portal_dark.png'))
    # unconfigured
    c3 = b.new_context(); c3.route('**/portal/config.js', lambda r: r.fulfill(body="window.MI_CONFIG={SUPABASE_URL:'SUPABASE_URL',ANON_KEY:'ANON_KEY'};", content_type='application/javascript'))
    c3.route('**/portal/vendor/supabase.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
    u = c3.new_page(); u.goto(BASE + '/portal/')
    check('placeholder config shows "not set up" message', lambda: expect(u.get_by_role('heading', name='Portal not set up yet')).to_be_visible())
    b.close()
srv.shutdown()
print('\nFAILED: %s' % fails if fails else '\nALL FRONT-END TESTS PASSED'); sys.exit(1 if fails else 0)
