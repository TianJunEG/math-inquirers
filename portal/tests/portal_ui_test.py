#!/usr/bin/env python3
"""Playwright test of the portal SCREENS (consent card per family type, add child, My children, extension book purchase, child sign-in and practice list,
trial class request, admin tabs) against tests/mock_supabase.js. Nothing talks to a real Supabase, Stripe or Cloudflare.
    python3 portal/tests/portal_ui_test.py
The mock re-implements the behaviour of the SQL functions; the SQL itself is tested against real Postgres by portal/supabase/test/run_sql_test.sh.
All prices below are TEST VALUES, not real prices."""
import json, os, re, sys, threading, tempfile, functools, http.server, socketserver
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
from playwright.sync_api import sync_playwright, expect

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, '..', 'public')
sched = json.load(open(os.path.join(HERE, '..', '..', 'website', 'data', 'beta_schedule.json')))
groups = [dict(id=g['id'], level=g['level'], name=g['name'], ages=g['ages'], seats=g['seats'], sessions=g['sessions'], first_label=g['first'], last_label=g['last'], fee_cents=25000) for g in sched['groups']]
UNITS = [
    dict(unit_key='hol-p1-01', product='holiday', level=1, unit_no=1, title='Number stories', access='enrolled', published=True),
    dict(unit_key='hol-p1-02', product='holiday', level=1, unit_no=2, title='Not released yet', access='enrolled', published=False),
    dict(unit_key='ext-l2u01', product='extension', level=2, unit_no=1, title='Digit detectives', access='purchased', published=True),
    dict(unit_key='ext-l2u02', product='extension', level=2, unit_no=2, title='Make a number', access='purchased', published=True),
    dict(unit_key='ext-l3u01', product='extension', level=3, unit_no=1, title='Level three unit', access='purchased', published=True),
]
PRICES = {'ext-l2-workbook': 1300, 'ext-l2-online': 1100, 'ext-l2-both': 2200}      # TEST VALUES; level 3 has no price on purpose
PREVIEWS = [dict(id='pv1', starts_at='2026-12-05T02:00:00Z', band='Primary 3-4', regs=[dict(parent_first_name='Mei', child_first_name='Tan', child_birth_year=2017, status='confirmed', email='mei@example.com', phone='91234567', wants_trial=True)])]
SEED = 'window.__SEED__=%s;' % json.dumps(dict(groups=groups, extraTaken={}, units=UNITS, prices=PRICES, previews=PREVIEWS))
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
    except Exception as e: fails.append(name); print('FAIL', name, '\n    ', str(e)[:600])

def new_ctx(b, w=375, init=''):
    ctx = b.new_context(viewport={'width': w, 'height': 800})
    ctx.set_default_timeout(6000); ctx.add_init_script(SEED + init + MOCK)
    ctx.route('**/portal/config.js', lambda r: r.fulfill(body=CONFIG(), content_type='application/javascript'))
    ctx.route('**/portal/vendor/supabase.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
    ctx.route('https://mock.supabase.co/**', lambda r: r.abort())
    return ctx

def mockdb(page): return page.evaluate('window.__mockDb()')
def patch(page, js):
    """change the mock database from a test (what the Worker / the owner's SQL would do), then reload so the page sees it"""
    page.evaluate('(function(){var db=window.__mockDb();%s;window.__mockSave();})()' % js)

def login(page, email, pw):
    page.goto(BASE + '/portal/')
    if page.locator('#signout').count():
        page.click('#signout'); expect(page.get_by_role('heading', name='Parent portal')).to_be_visible()
    page.fill('#email', email); page.fill('#password', pw); page.get_by_role('button', name='Log in', exact=True).last.click()
    expect(page.locator('#signout')).to_be_visible()
def signup(page, name, email, pw='longenough1', query=''):
    page.goto(BASE + '/portal/' + query)
    page.get_by_role('button', name='Sign up').click()
    page.fill('#fullname', name); page.fill('#email', email); page.fill('#password', pw)
    page.get_by_role('button', name='Create parent account').click()
    expect(page.get_by_role('heading', name='Hello, ' + name)).to_be_visible()
def logout(page):
    page.goto(BASE + '/portal/')
    page.click('#signout'); expect(page.get_by_role('heading', name='Parent portal')).to_be_visible()
def admin_login(page):
    page.goto(BASE + '/portal/admin/')
    lo = page.get_by_role('button', name='Log out')
    if lo.count(): lo.first.click()
    page.wait_for_selector('#email')
    page.fill('#email', 'owner@example.com'); page.fill('#password', 'ownerpass1'); page.get_by_role('button', name='Log in').click()
    expect(page.locator('#viewtabs')).to_be_visible()
def admin_tab(page, label):
    page.locator('#viewtabs').get_by_role('button', name=label, exact=True).click()

with sync_playwright() as pw:
    b = pw.chromium.launch()
    ctx = new_ctx(b); page = ctx.new_page()
    errors = []; external = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' and 'Failed to load resource' not in m.text else None)
    page.on('request', lambda r: external.append(r.url) if not r.url.startswith(BASE) and not r.url.startswith('data:') and not r.url.startswith('https://checkout.stripe.com/') else None)
    page.on('dialog', lambda d: d.accept())
    def overflow(): return page.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')

    # ============ (1) sign-up and the agreements card, per family type ============
    check('sign up (online family link) lands on the portal home', lambda: signup(page, 'Kim Parent', 'kim@example.com', query='?for=online'))
    def card_online():
        expect(page.locator('#ftype-online')).to_be_checked()
        for t in ['contact', 'terms', 'online_practice', 'book_delivery', 'marketing_contact', 'feedback_quotes']: expect(page.locator('#consent-' + t)).to_be_visible()
        for t in ['recording', 'childs_work']: expect(page.locator('#consent-' + t)).to_have_count(0)
        for t in ['contact', 'terms', 'online_practice', 'book_delivery', 'marketing_contact', 'feedback_quotes']: assert not page.locator('#consent-' + t).is_checked(), t + ' must not be pre-ticked'
        assert 'recorded' not in page.locator('#agreements').inner_text().lower().split('only for live')[0]
    check('online family: no recording or childs_work agreement is asked, nothing pre-ticked', card_online)
    def card_types():
        page.check('#ftype-live')
        for t in ['contact', 'terms', 'recording', 'childs_work', 'online_practice', 'marketing_contact']: expect(page.locator('#consent-' + t)).to_be_visible()
        expect(page.locator('#consent-book_delivery')).to_have_count(0)
        page.check('#ftype-both')
        for t in ['contact', 'terms', 'recording', 'childs_work', 'online_practice', 'book_delivery', 'marketing_contact', 'feedback_quotes']: expect(page.locator('#consent-' + t)).to_be_visible()
        page.check('#ftype-online'); expect(page.locator('#consent-recording')).to_have_count(0)
    check('live and both family types show the live-group agreements', card_types)
    def save_online():
        for t in ['contact', 'terms', 'online_practice']: page.check('#consent-' + t)
        page.click('#save-consents'); expect(page.locator('.msg.ok')).to_contain_text('Agreements saved')
        got = {c['consent_type']: c['granted'] for c in mockdb(page)['consents']}
        assert got == {'contact': True, 'terms': True, 'online_practice': True}, got
    check('saving for an online family records only contact, terms, online_practice', save_online)
    def versions():
        assert all(c['terms_version'].startswith('terms-') for c in mockdb(page)['consents'])
        expect(page.locator('#agreements')).to_contain_text('Math Inquirers (Preciouslyours Pte Ltd) receives my child')
    check('consents carry versions; online_practice wording is the drafted line', versions)
    def live_blocked():
        # no live consents yet and the family has no enrolment: reserving a place explains what is missing, with a link
        page.check('#ftype-live'); page.goto(BASE + '/portal/?for=live')
        expect(page.locator('#ftype-live')).to_be_checked()
    check('?for=live presets the live block', live_blocked)

    # ============ (2) add child profile (no enrolment), on the dashboard ============
    page.goto(BASE + '/portal/children/')
    def first_child_form():
        expect(page.locator('#first-child')).to_be_visible(); expect(page.locator('#first-child')).to_contain_text('do not need to join a class')
        page.fill('#cname', 'Kai'); page.fill('#cpin', '12'); page.get_by_role('button', name='Add my child').click()
        expect(page.locator('.msg.err')).to_contain_text('4 to 6 digits')
        page.fill('#cpin', '7391'); page.select_option('#clevel', '2')
        y = page.evaluate('new Date().getFullYear()'); page.select_option('#cbirth', str(y - 8))
        page.get_by_role('button', name='Add my child').click()
        expect(page.locator('[data-child-card]')).to_have_count(1); expect(page.locator('[data-child-card]')).to_contain_text('Kai')
        c = mockdb(page)['children'][0]; assert c['birth_year'] == y - 8 and c['level'] == 2, c
        assert not mockdb(page)['enrolments'], 'no enrolment needed'
    check('add a child with birth year, level and PIN, with no enrolment', first_child_form)
    def second_child():
        page.locator('#add-another summary').click(); page.fill('#add-another #cname', 'Lia'); page.fill('#add-another #cpin', '7142'); page.locator('#add-another').get_by_role('button', name='Add child').click()
        expect(page.locator('[data-child-card]')).to_have_count(2)
        assert mockdb(page)['children'][1].get('birth_year') is None, 'birth year is optional'
    check('add a sibling without a birth year', second_child)
    def name_text():
        page.locator('#add-another summary').click(); page.fill('#add-another #cname', '<b onmouseover=1>x</b>'); page.fill('#add-another #cpin', '5016'); page.locator('#add-another').get_by_role('button', name='Add child').click()
        expect(page.locator('[data-child-card]')).to_have_count(3)
        assert page.locator('[data-child-card] b').count() == 0
        page.evaluate("window.__mockDb().children.pop();window.__mockSave()")
        page.goto(BASE + '/portal/children/')
    check('a child name is shown as text, never as HTML', name_text)

    # ============ (3) My children dashboard: nothing entitled yet ============
    def dash_empty():
        card = page.locator('[data-child-card]').first
        expect(card.locator('[data-nothing-open]')).to_be_visible(); expect(card).to_contain_text('Nothing is open yet')
        assert page.locator('[data-unit]').count() == 0, 'no unit links without an entitlement'
        expect(card.locator('[data-no-progress]')).to_contain_text('No answers have been sent yet')
        assert overflow() <= 0, 'overflow %s' % overflow()
    check('dashboard: no entitlement shows no practice link and a kind empty state', dash_empty)

    # ============ (6) buy an extension book ============
    page.goto(BASE + '/portal/books/')
    def prices_shown():
        page.select_option('#book-level', '2')
        expect(page.locator('[data-price-for="ext-l2-online"]')).to_have_text('S$11.00')
        expect(page.locator('[data-price-for="ext-l2-both"]')).to_have_text('S$22.00')
        expect(page.locator('[data-price-for="ext-l2-workbook"]')).to_have_text('S$13.00')
    check('prices come from the price list', prices_shown)
    def coming_soon():
        page.select_option('#book-level', '3'); page.check('#fmt-online'); page.check('#kid-' + mockdb(page)['children'][0]['id'])
        expect(page.locator('[data-price-for="ext-l3-online"]')).to_have_text('Price coming soon')
        expect(page.locator('#order-summary')).not_to_contain_text('S$')
        assert page.locator('#place-order').count() == 0, 'no order button without a price'
        href = page.locator('#ask-us').get_attribute('href'); assert href.startswith('https://wa.me/') and 'Level%203' in href, href
        assert not [r for r in mockdb(page)['ext_orders']]
    check('no price set: "price coming soon" and an Ask us button, no order', coming_soon)
    def no_ship_for_online():
        page.select_option('#book-level', '2'); page.check('#fmt-online')
        assert page.locator('#ship-box').count() == 0; assert page.locator('#need-book_delivery').count() == 0
        for t in ['contact', 'terms', 'online_practice']: assert page.locator('#need-' + t).count() == 0, 'already agreed: not asked again'
        page.check('#fmt-workbook'); expect(page.locator('#ship-box')).to_be_visible(); expect(page.locator('#ship-box')).to_contain_text('Singapore addresses only')
        expect(page.locator('#need-book_delivery')).to_be_visible(); assert page.locator('#need-online_practice').count() == 0
        page.check('#fmt-both'); expect(page.locator('#ship-box')).to_be_visible()
    check('shipping address and delivery agreement only for printed options', no_ship_for_online)
    def singapore_only():
        page.check('#fmt-workbook'); page.check('#kid-' + mockdb(page)['children'][0]['id'])
        page.fill('#ship-name', 'Kim Parent'); page.fill('#ship-address', '1 Test Road'); page.fill('#ship-postal', '12345'); page.check('#need-book_delivery')
        page.click('#place-order'); expect(page.locator('.msg.err')).to_contain_text('6 digits')
        page.fill('#ship-postal', '12345a'); page.click('#place-order'); expect(page.locator('.msg.err')).to_contain_text('6 digits')
        assert not mockdb(page)['ext_orders']
    check('postal code must be a 6-digit Singapore code', singapore_only)
    def agreement_needed():
        page.fill('#ship-postal', '123456'); page.uncheck('#need-book_delivery')
        page.click('#place-order'); expect(page.locator('.msg.err')).to_contain_text('Needed')
        assert not mockdb(page)['ext_orders']
    check('a needed agreement must be ticked before ordering', agreement_needed)
    kai = mockdb(page)['children'][0]['id']; lia = mockdb(page)['children'][1]['id']
    def order_online():
        page.check('#fmt-online'); page.click('#place-order')
        expect(page.locator('#order-done')).to_be_visible()
        expect(page.locator('#order-done [data-ref]')).to_have_text(re.compile(r'^MI-[A-Z2-9]{6}$'))
        expect(page.locator('#order-done')).to_contain_text('S$11.00'); expect(page.locator('#order-done')).to_contain_text('UEN 000TEST')
        o = mockdb(page)['ext_orders']; assert len(o) == 1 and o[0]['status'] == 'pending_payment' and o[0]['format'] == 'online' and o[0]['child_id'] == kai and o[0]['amount_cents'] == 1100, o
        assert o[0]['ship_name'] is None and o[0]['ship_status'] == 'not_needed'
        assert mockdb(page)['access'] == [], 'paying has not happened: no access'
        assert page.locator('[data-pay-online]').count() == 0, 'card button hidden unless PAYMENT_MODE is stripe'
        got = {c['consent_type'] for c in mockdb(page)['consents']}; assert 'recording' not in got and 'childs_work' not in got, got
    check('online-only order for Kai: pending, MI- reference, PayNow text, no card button, no access yet', order_online)
    def trial_cta():
        expect(page.locator('#order-done details summary')).to_have_text('For grown-ups: while you wait')
        href = page.locator('#order-done a[href*="/portal/trial/"]').get_attribute('href'); assert 'from=post_purchase' in href, href
        t = page.locator('#order-done').inner_text().lower()
        for bad in ['hurry', 'limited', 'countdown', 'last chance', 'only today', 'seats left']: assert bad not in t, bad
    check('post-purchase trial class link is a quiet parent-only note', trial_cta)
    def order_listed_and_dup():
        page.goto(BASE + '/portal/books/')
        expect(page.locator('[data-order]')).to_have_count(1); expect(page.locator('[data-order-status]')).to_have_text('waiting for payment')
        page.select_option('#book-level', '2'); page.check('#fmt-online'); page.check('#kid-' + kai); page.click('#place-order')
        expect(page.locator('.msg.err')).to_contain_text('unpaid order'); assert len(mockdb(page)['ext_orders']) == 1
    check('orders list shows the pending order; a duplicate is refused kindly', order_listed_and_dup)
    def cancel_and_reorder():
        page.locator('[data-cancel-order]').click(); expect(page.locator('.msg.ok')).to_contain_text('Order cancelled')
        assert mockdb(page)['ext_orders'][0]['status'] == 'cancelled'
        page.select_option('#book-level', '2'); page.check('#fmt-online'); page.check('#kid-' + kai); page.click('#place-order'); expect(page.locator('#order-done')).to_be_visible()
        assert len(mockdb(page)['ext_orders']) == 2
    check('parent can cancel an unpaid order and order again', cancel_and_reorder)
    def stripe_button():
        MODE[0] = 'stripe'
        seen = []
        def fake(r): seen.append(r.request.post_data_json); r.fulfill(status=200, content_type='application/json', body=json.dumps({'url': 'https://checkout.stripe.com/c/pay/cs_test_fake2'}))
        page.route('**/api/stripe-create-ext-checkout', fake)
        page.route('https://checkout.stripe.com/**', lambda r: r.fulfill(status=200, content_type='text/html', body='<p>stripe stand-in</p>'))
        page.goto(BASE + '/portal/books/'); expect(page.locator('[data-pay-online]')).to_have_count(1)
        page.locator('[data-pay-online]').click(); page.wait_for_url('https://checkout.stripe.com/**'); assert len(seen) == 1 and 'order_id' in seen[0], seen
        page.goto(BASE + '/portal/books/')   # back from the Stripe stand-in
        MODE[0] = 'paynow_manual'
    check('Stripe button appears only when PAYMENT_MODE is stripe', stripe_button)

    # ============ (7) admin marks paid and gives access; before that, the child can not open anything ============
    def child_before_paid():
        cp = ctx.new_page(); cp.goto(BASE + '/portal/child/')
        fam = [p for p in mockdb(page)['parents'] if p['email'] == 'kim@example.com'][0]['family_code']
        cp.fill('#code', fam); cp.fill('#name', 'Kai'); cp.fill('#pin', '7391'); cp.get_by_role('button', name='Sign in').click()
        expect(cp.locator('#hello')).to_have_text('Hello, Kai!')
        expect(cp.locator('#nothing-open')).to_be_visible(); assert cp.locator('[data-unit]').count() == 0, 'unpaid order opens nothing'
        cp.close()
    check('before payment the child can sign in but sees no unit', child_before_paid)
    logout(page)
    admin_login(page)
    def admin_orders():
        admin_tab(page, 'Book orders')
        expect(page.locator('[data-order]')).to_have_count(1)
        row = page.locator('[data-order]'); expect(row).to_contain_text('kim@example.com'); expect(row).to_contain_text('Kai'); expect(row).to_contain_text('Level 2, online only'); expect(row).to_contain_text('S$11.00')
        row.locator('[data-mark-paid]').click()
        expect(page.locator('.msg.ok')).to_contain_text('paid'); expect(page.locator('#noOrders')).to_be_visible()
        a = mockdb(page)['access']; assert len(a) == 1 and a[0]['child_id'] == kai and a[0]['level'] == 2 and a[0]['format'] == 'online' and a[0]['source'] == 'paynow_manual' and a[0]['status'] == 'active', a
        assert len(a) == 1 and not [x for x in a if x['child_id'] == lia], 'the sibling gets nothing'
    check('admin: Book orders -> mark paid and give access creates access for that child only', admin_orders)
    def admin_orders_filters():
        page.locator('#order-filter [data-filter="all"]').click(); expect(page.locator('[data-order]')).to_have_count(2)
        expect(page.locator('[data-order] .pill.paid')).to_have_count(1); expect(page.locator('[data-order] .pill.cancelled')).to_have_count(1)
    check('admin: order filters', admin_orders_filters)
    def prices_admin():
        page.locator('#price-card summary').click()
        expect(page.locator('[data-price="ext-l3-online"]')).to_contain_text('not set')
        page.fill('#price-ext-l3-online', 'abc'); page.locator('[data-save-price="ext-l3-online"]').click(); expect(page.locator('.msg.err')).to_contain_text('price in dollars')
        page.locator('#price-card summary').click(); page.fill('#price-ext-l3-online', '9.50'); page.locator('[data-save-price="ext-l3-online"]').click()
        expect(page.locator('.msg.ok')).to_contain_text('Price saved'); assert mockdb(page)['prices']['ext-l3-online'] == 950
        page.locator('#price-card summary').click(); page.locator('[data-off-price="ext-l3-online"]').click()
        assert 'ext-l3-online' not in mockdb(page)['prices']
    check('admin: owner sets and turns off a price; nothing is pre-filled', prices_admin)

    # ============ (4)(5) child sign-in and practice list ============
    fam = [p for p in mockdb(page)['parents'] if p['email'] == 'kim@example.com'][0]['family_code']
    cpage = ctx.new_page(); cpage.on('dialog', lambda d: d.accept())
    cpage.goto(BASE + '/portal/child/')
    def child_wrong():
        cpage.fill('#code', fam); cpage.fill('#name', 'Kai'); cpage.fill('#pin', '1873'); cpage.get_by_role('button', name='Sign in').click()
        expect(cpage.locator('.msg.err')).to_contain_text('did not work'); assert cpage.evaluate("sessionStorage.getItem('mi-child')") is None
    check('child sign-in: wrong PIN gives the same quiet message and no session', child_wrong)
    def child_ok():
        cpage.fill('#code', fam.lower()); cpage.fill('#name', ' kai '); cpage.fill('#pin', '7391'); cpage.get_by_role('button', name='Sign in').click()
        expect(cpage.locator('#hello')).to_have_text('Hello, Kai!'); assert cpage.url.endswith('/portal/practice/')
        tok = json.loads(cpage.evaluate("sessionStorage.getItem('mi-child')")); assert len(tok['token']) >= 32 and tok['id'] == kai
    check('child sign-in with family code, name and PIN opens the practice list', child_ok)
    def child_units():
        links = cpage.locator('[data-unit]'); expect(links).to_have_count(2)
        hrefs = sorted(links.evaluate_all('els => els.map(e => e.getAttribute("href"))')); assert hrefs == ['/practice/ext/l2u01/', '/practice/ext/l2u02/'], hrefs
        expect(cpage.locator('[data-group="extension"]')).to_contain_text('Digit detectives')
        assert cpage.locator('[data-group="holiday"]').count() == 0 and cpage.locator('[data-unit="ext-l3u01"]').count() == 0
        assert '%' not in cpage.inner_text('main') and 'score' not in cpage.inner_text('main').lower()
        assert cpage.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth') <= 0
    check('practice list shows only the purchased level, as links, with no score words', child_units)
    def child_bye():
        cpage.click('#bye'); expect(cpage.locator('#ended-note')).to_contain_text('signed out')
        assert cpage.evaluate("sessionStorage.getItem('mi-child')") is None
        assert [s for s in mockdb(cpage)['child_sessions'] if s['revoked']], 'session revoked on the server side'
        cpage.goto(BASE + '/portal/practice/'); cpage.wait_for_url('**/portal/child/')
    check('child sign-out revokes the session; the practice page then sends them to sign in', child_bye)
    def sibling():
        cpage.goto(BASE + '/portal/child/'); cpage.fill('#code', fam); cpage.fill('#name', 'Lia'); cpage.fill('#pin', '7142'); cpage.get_by_role('button', name='Sign in').click()
        expect(cpage.locator('#hello')).to_have_text('Hello, Lia!'); expect(cpage.locator('#nothing-open')).to_be_visible()
        assert cpage.locator('[data-unit]').count() == 0, 'the sibling got no access from the purchase'
        cpage.click('#bye')
    check('a sibling signs in but gets no unit (one purchase = one child)', sibling)
    def expired():
        cpage.goto(BASE + '/portal/child/'); cpage.fill('#code', fam); cpage.fill('#name', 'Kai'); cpage.fill('#pin', '7391'); cpage.get_by_role('button', name='Sign in').click()
        expect(cpage.locator('#hello')).to_be_visible()
        patch(cpage, "db.child_sessions.forEach(function(s){s.expires_at='2020-01-01T00:00:00Z'})")
        cpage.goto(BASE + '/portal/practice/'); cpage.wait_for_url('**/portal/child/?ended=expired'); expect(cpage.locator('#ended-note')).to_contain_text('sign in again')
    check('an ended session sends the child back to sign in with a kind note', expired)
    def no_consent_no_session():
        patch(cpage, "db.consents.push({parent_id:db.parents.filter(function(p){return p.email==='kim@example.com'})[0].id,consent_type:'online_practice',granted:false,terms_version:'t',privacy_version:'p',created_at:new Date().toISOString()})")
        cpage.goto(BASE + '/portal/child/'); cpage.fill('#code', fam); cpage.fill('#name', 'Kai'); cpage.fill('#pin', '7391'); cpage.get_by_role('button', name='Sign in').click()
        expect(cpage.locator('.msg.err')).to_contain_text('did not work')
        patch(cpage, "db.consents.pop()")
    check('withdrawing the online practice agreement stops child sessions', no_consent_no_session)

    # ============ parent view after payment: dashboard, links, progress ============
    login(page, 'kim@example.com', 'longenough1')
    page.goto(BASE + '/portal/children/')
    def dash_entitled():
        kc = page.locator('[data-child-card="%s"]' % kai); lc = page.locator('[data-child-card="%s"]' % lia)
        expect(kc.locator('[data-access="book-2-online"]')).to_have_text('Extension Workbook, Level 2: online practice.')
        hrefs = sorted(kc.locator('[data-unit]').evaluate_all('els => els.map(e => e.getAttribute("href"))')); assert hrefs == ['/practice/ext/l2u01/', '/practice/ext/l2u02/'], hrefs
        expect(lc.locator('[data-nothing-open]')).to_be_visible(); assert lc.locator('[data-unit]').count() == 0
        expect(kc.get_by_role('link', name='Open the child sign-in page')).to_have_attribute('href', '/portal/child/')
    check('dashboard: Kai sees the book and its unit links, Lia sees nothing open', dash_entitled)
    def books_blocks_dup():
        page.goto(BASE + '/portal/books/'); page.select_option('#book-level', '2'); page.check('#fmt-online')
        expect(page.locator('#kid-' + kai)).to_be_disabled(); expect(page.locator('#kid-' + lia)).to_be_enabled()
        expect(page.locator('[data-online-on]')).to_have_count(1)
    check('books: Kai can not buy online Level 2 twice; Lia can (her own purchase)', books_blocks_dup)
    def progress():
        patch(page, "var k=db.children.filter(function(c){return c.display_name==='Kai'})[0].id;db.submissions.push({child_id:k,unit_key:'ext-l2u01',received_at:'2026-11-24T08:42:00Z',n_auto:6,n_skipped:1,n_self:1,n_self_got:1,n_open:1});"
              "db.attempts.push({child_id:k,unit_key:'ext-l2u01',item_id:'q2',skill:'Place value to 1000',mark:'wrong',misconception:'Said 6: gave the digit, not the value (6 tens = 60).',self_result:null,received_at:'x'},{child_id:k,unit_key:'ext-l2u01',item_id:'q8',skill:'Patterns',mark:'skipped',misconception:null,self_result:null},{child_id:k,unit_key:'ext-l2u01',item_id:'q11',skill:'Draw it',mark:'self',misconception:null,self_result:'not_yet'})")
        page.goto(BASE + '/portal/children/')
        row = page.locator('[data-unit-progress="ext-l2u01"]'); expect(row).to_contain_text('answered 5 of 6 questions'); expect(row).to_contain_text('1 left for later'); expect(row).to_contain_text('done on paper')
        txt = page.locator('main').inner_text().lower()
        for bad in ['score', 'rank', 'streak', 'percent', '%', 'leaderboard', 'behind', 'best']: assert bad not in txt, bad
        row.locator('[data-detail]').click()
        box = page.locator('[data-detail-box]'); expect(box).to_contain_text('Place value to 1000'); expect(box).to_contain_text('gave the digit, not the value'); expect(box).to_contain_text('left for later'); expect(box).to_contain_text('not yet')
        expect(box).not_to_contain_text('Patterns')
        assert page.locator('[data-no-progress]').count() == 1, 'Lia still has nothing sent'
    check('progress summary: counts of what was done, kind wording, no score/rank/streak; details list what to look at together', progress)
    def parent_trial_cta():
        expect(page.locator('[data-child-card="%s"] details.nextstep summary' % kai)).to_have_text('For grown-ups: a possible next step')
        assert page.locator('[data-child-card="%s"] details.nextstep' % lia).count() == 0, 'no nudge for a child with no answers'
    check('trial class note is parent-only and only after answers exist', parent_trial_cta)
    def delete_practice():
        page.locator('[data-delete-practice="%s"]' % kai).click(); expect(page.locator('.msg.ok')).to_contain_text('deleted')
        assert mockdb(page)['submissions'] == []; expect(page.locator('[data-no-progress]')).to_have_count(2)
    check('parent can delete a child\'s practice answers', delete_practice)

    # ============ (8) trial class request, for a family that is not enrolled ============
    def trial_form():
        page.goto(BASE + '/portal/trial/?from=report&child=' + kai)
        expect(page.locator('#trial-child')).to_have_value(kai); expect(page.locator('#trial-level')).to_have_value('2')
        assert page.locator('#need-contact').count() == 0 and page.locator('#need-terms').count() == 0, 'already agreed'
        expect(page.locator('#need-marketing_contact')).to_be_visible(); assert not page.locator('#need-marketing_contact').is_checked(), 'never pre-ticked'
        text = page.locator('main').inner_text().lower()
        for bad in ['free', 'hurry', 'limited', 'seats left', 'last chance', 'countdown']: assert bad not in text, bad
        page.check('#time-weekend-morning'); page.fill('#trial-note', 'Kai likes puzzles'); page.fill('#trial-phone', '91234567')
        page.click('#send-trial'); expect(page.locator('#trial-done')).to_be_visible()
        t = mockdb(page)['trials']; assert len(t) == 1 and t[0]['source'] == 'report' and t[0]['child_id'] == kai and t[0]['level'] == 2 and t[0]['preferred'] == ['weekend-morning'] and t[0]['status'] == 'new', t
        assert not [c for c in mockdb(page)['consents'] if c['consent_type'] == 'marketing_contact'], 'marketing agreement not recorded when left unticked'
        assert [p for p in mockdb(page)['parents'] if p['email'] == 'kim@example.com'][0]['phone'] == '91234567'
        expect(page.locator('[data-trial]')).to_have_count(1)
    check('trial request from a non-enrolled family: source, child, level, times; marketing agreement stays unrecorded', trial_form)
    def trial_withdraw():
        page.locator('[data-withdraw]').click(); expect(page.locator('.msg.ok')).to_contain_text('withdrawn'); assert mockdb(page)['trials'][0]['status'] == 'withdrawn'
        page.goto(BASE + '/portal/trial/'); page.check('#time-weekday-evening'); page.check('#need-marketing_contact'); page.click('#send-trial'); expect(page.locator('#trial-done')).to_be_visible()
        assert mockdb(page)['trials'][1]['source'] == 'other'
        assert [c for c in mockdb(page)['consents'] if c['consent_type'] == 'marketing_contact' and c['granted']], 'optional agreement recorded when ticked'
    check('a trial request can be withdrawn; the optional marketing agreement is recorded only when ticked', trial_withdraw)

    # ============ admin tabs: access, trials/previews, funnel, group report ============
    logout(page); admin_login(page)
    def admin_access():
        admin_tab(page, 'Access')
        expect(page.locator('[data-access]')).to_have_count(1); expect(page.locator('#access')).to_contain_text('Kai'); expect(page.locator('#access')).to_contain_text('PayNow (ticked by owner)')
        page.select_option('#grant-child', lia); page.select_option('#grant-level', '2'); page.select_option('#grant-format', 'online')
        page.click('#grant-form button[type=submit]'); expect(page.locator('#grant-form .msg.err')).to_contain_text('reason')
        page.fill('#grant-note', 'gift test'); page.click('#grant-form button[type=submit]'); expect(page.locator('.msg.ok')).to_contain_text('Access given')
        expect(page.locator('[data-access]')).to_have_count(2); assert [a for a in mockdb(page)['access'] if a['child_id'] == lia and a['source'] == 'admin']
        page.locator('tr', has_text='gift test').locator('[data-revoke]').click(); expect(page.locator('.msg.ok')).to_contain_text('revoked')
        assert [a for a in mockdb(page)['access'] if a['child_id'] == lia][0]['status'] == 'revoked'
        assert [a for a in mockdb(page)['access'] if a['child_id'] == kai][0]['status'] == 'active', 'revoking one child leaves the other'
    check('admin: grant and revoke access for a named child', admin_access)
    def admin_trials():
        admin_tab(page, 'Trials and previews')
        expect(page.locator('#trials [data-trial]')).to_have_count(2); expect(page.locator('#trials')).to_contain_text('from a report'); expect(page.locator('#trials')).to_contain_text('91234567')
        first = page.locator('#trials [data-trial]').nth(1)
        first.locator('[data-set="contacted"]').click(); expect(page.locator('.msg.ok')).to_contain_text('contacted')
        assert any(t['status'] == 'contacted' for t in mockdb(page)['trials'])
        page.locator('[data-show-signups="pv1"]').click(); expect(page.locator('.preview-list')).to_contain_text('mei@example.com')
        expect(page.locator('#pfunnel')).to_contain_text('Primary 3-4')
    check('admin: trial requests list with status buttons, preview sign-ups and funnel', admin_trials)
    def admin_funnel():
        admin_tab(page, 'Funnel')
        expect(page.locator('[data-step="Extension books paid"] td').nth(1)).to_have_text('1'); expect(page.locator('[data-step="Trial class requests"] td').nth(1)).to_have_text('1')
        expect(page.locator('#trial-sources')).to_contain_text('portal 1')
        txt = page.locator('main').inner_text().lower(); assert 'cookie' in txt and 'tracking' in txt
    check('admin: funnel counts (rows that already exist, no tracking)', admin_funnel)
    def admin_report():
        patch(page, "db.report={L2A:{practice:[{child_id:'c1',display_name:'Maple',unit_key:'hol-p2-01',unit_version:'v1',received_at:'2026-11-25T08:00:00Z'}],"
              "skills:{'hol-p2-01':[{child_id:'c1',display_name:'Maple',skill:'Place value',n_right:3,n_wrong:0,n_skipped:0,n_self_got:0,n_self_notyet:0,n_self_checked:0},"
              "{child_id:'c1',display_name:'Maple',skill:'Comparing',n_right:1,n_wrong:2,n_skipped:0,n_self_got:0,n_self_notyet:0,n_self_checked:0},"
              "{child_id:'c1',display_name:'Maple',skill:null,n_right:0,n_wrong:0,n_skipped:0,n_self_got:1,n_self_notyet:0,n_self_checked:0},"
              "{child_id:'c2',display_name:'Otter',skill:'Place value',n_right:0,n_wrong:2,n_skipped:0,n_self_got:0,n_self_notyet:0,n_self_checked:0},"
              "{child_id:'c2',display_name:'Otter',skill:'Comparing',n_right:1,n_wrong:0,n_skipped:0,n_self_got:0,n_self_notyet:0,n_self_checked:0}]},"
              "slips:{'hol-p2-01':[{item_id:'q2',item_pos:2,skill:'Place value',say:'Gave the digit, not the value.',n_children:1,n_sent:2}]}}}")
        admin_tab(page, 'Group report')
        page.select_option('#rep-group', 'L2A')
        expect(page.locator('#group-report')).to_be_visible()
        names = page.locator('#group-report tbody tr').evaluate_all('els => els.map(e => e.getAttribute("data-child"))'); assert names == sorted(names), 'alphabetical, never by result: %s' % names
        expect(page.locator('tr[data-child="Maple"] [data-skill="Place value"]')).to_contain_text('going well')
        expect(page.locator('tr[data-child="Otter"] [data-skill="Place value"]')).to_contain_text('worth practising together')
        expect(page.locator('tr[data-child="Maple"] [data-skill="Comparing"]')).to_contain_text('some right, some to look at')
        expect(page.locator('tr[data-child="Otter"] [data-skill="Comparing"]')).to_contain_text('not enough answers yet')
        expect(page.locator('tr[data-child="Maple"] [data-skill="paper"]')).to_have_text('got it')
        expect(page.locator('#slips')).to_contain_text('Gave the digit, not the value.'); expect(page.locator('#slips')).to_contain_text('1 of 2')
        assert 'league table' in page.locator('main').inner_text()
    check('admin: tutor group report (readings in words, alphabetical, misconceptions, paper column)', admin_report)
    def forbidden_for_parent():
        logout(page); login(page, 'kim@example.com', 'longenough1')
        page.goto(BASE + '/portal/admin/'); expect(page.get_by_role('heading', name='Not an admin')).to_be_visible()
        page.click('text=Log out')
    check('a parent opening the admin page sees Not an admin', forbidden_for_parent)

    # ============ enrolled family: holiday unit shown only if entitled and released ============
    def enrolled_family():
        c2 = new_ctx(b); p2 = c2.new_page(); p2.on('dialog', lambda d: d.accept())
        signup(p2, 'Enrolled Parent', 'enr@example.com')
        for t in ['contact', 'terms', 'recording', 'childs_work']: p2.check('#consent-' + t)
        p2.check('#consent-online_practice'); p2.click('#save-consents'); expect(p2.locator('.msg.ok')).to_contain_text('Agreements saved')
        p2.fill('#cname', 'Mia'); p2.select_option('#clevel', '1'); p2.fill('#cpin', '7391'); p2.get_by_role('button', name='Add child').click()
        p2.locator('input[name^="grp-"]').first.check(); p2.get_by_role('button', name='Reserve a place').first.click()
        expect(p2.locator('[data-enrolment]')).to_have_count(1)
        # reserved but unpaid: nothing opens
        p2.goto(BASE + '/portal/children/'); expect(p2.locator('[data-nothing-open]')).to_be_visible()
        fam2 = [p for p in mockdb(p2)['parents'] if p['email'] == 'enr@example.com'][0]['family_code']
        admin_login(p2); p2.goto(BASE + '/portal/admin/'); p2.get_by_role('button', name='Mark paid').click(); expect(p2.locator('.msg.ok')).to_contain_text('paid')
        p2.click('#signout')
        login(p2, 'enr@example.com', 'longenough1'); p2.goto(BASE + '/portal/children/')
        expect(p2.locator('[data-access="enrolled-1"]')).to_contain_text('Holiday and term practice for Level 1')
        hrefs = p2.locator('[data-unit]').evaluate_all('els => els.map(e => e.getAttribute("href"))'); assert hrefs == ['/practice/holiday/p1/01/'], hrefs
        cp2 = c2.new_page(); cp2.goto(BASE + '/portal/child/'); cp2.fill('#code', fam2); cp2.fill('#name', 'Mia'); cp2.fill('#pin', '7391'); cp2.get_by_role('button', name='Sign in').click()
        expect(cp2.locator('[data-group="holiday"]')).to_contain_text('Number stories'); assert cp2.locator('[data-unit="hol-p1-02"]').count() == 0, 'unreleased unit hidden'
        assert cp2.locator('[data-group="extension"]').count() == 0, 'an enrolment does not unlock extension books'
        c2.close()
    check('enrolled family: confirmed place opens released holiday units only; unpaid opens nothing', enrolled_family)

    # ============ a parent without any entitlement ============
    def no_entitlement():
        c3 = new_ctx(b); p3 = c3.new_page()
        signup(p3, 'Plain Parent', 'plain@example.com', query='?for=online')
        for t in ['contact', 'terms', 'online_practice']: p3.check('#consent-' + t)
        p3.click('#save-consents'); expect(p3.locator('.msg.ok')).to_contain_text('Agreements saved')
        p3.fill('#cname', 'Zed'); p3.fill('#cpin', '8403'); p3.get_by_role('button', name='Add child').click()
        fam3 = [p for p in mockdb(p3)['parents'] if p['email'] == 'plain@example.com'][0]['family_code']
        p3.goto(BASE + '/portal/children/'); expect(p3.locator('[data-nothing-open]')).to_be_visible(); assert p3.locator('[data-unit]').count() == 0
        cp3 = c3.new_page(); cp3.goto(BASE + '/portal/child/'); cp3.fill('#code', fam3); cp3.fill('#name', 'Zed'); cp3.fill('#pin', '8403'); cp3.get_by_role('button', name='Sign in').click()
        expect(cp3.locator('#nothing-open')).to_be_visible(); assert cp3.locator('[data-unit]').count() == 0
        c3.close()
    check('a parent with no entitlement sees no unit, for the parent or the child', no_entitlement)
    def signed_out_pages():
        c4 = new_ctx(b); p4 = c4.new_page()
        for path in ['/portal/children/', '/portal/books/', '/portal/trial/']:
            p4.goto(BASE + path); expect(p4.locator('#signed-out')).to_be_visible(); expect(p4.locator('#to-login')).to_have_attribute('href', '/portal/')
        p4.goto(BASE + '/portal/practice/'); p4.wait_for_url('**/portal/child/')
        c4.close()
    check('signed-out visitors are asked to log in (no data shown)', signed_out_pages)
    def missing_sql():
        c5 = new_ctx(b, init='window.__NO_UI_SQL__=true;'); p5 = c5.new_page()
        signup(p5, 'Early Parent', 'early@example.com')
        for path in ['/portal/children/', '/portal/books/']:
            p5.goto(BASE + path); expect(p5.get_by_text('not switched on yet')).to_be_visible()
        p5.goto(BASE + '/portal/'); expect(p5.get_by_role('heading', name='Hello, Early Parent')).to_be_visible()
        c5.close()
    check('if portal_ui.sql is not applied the new pages say so kindly and the home page still works', missing_sql)

    # ============ round-1 audit fixes (docs/audit_final/portal_ui_fixes_round1.md) ============
    def r1_agreements_warn():
        c7 = new_ctx(b); p7 = c7.new_page(); p7.on('dialog', lambda d: d.accept())
        signup(p7, 'Warn Parent', 'warn@example.com', query='?for=online')
        p7.check('#consent-contact'); p7.click('#save-consents')
        msg = p7.locator('.msg.warn'); expect(msg).to_contain_text('still not ticked'); expect(msg).to_contain_text('terms and refund policy'); expect(msg).to_contain_text('online practice')
        assert 'Agreements saved' not in p7.locator('main').inner_text(), 'must not claim success'
        assert p7.evaluate('document.activeElement.classList.contains("msg")'), 'keyboard focus moves to the message'
        p7.check('#consent-terms'); p7.check('#consent-online_practice'); p7.click('#save-consents'); expect(p7.locator('.msg.ok')).to_contain_text('Agreements saved')
        assert p7.evaluate('document.activeElement.classList.contains("msg")')
        c7.close()
    check('R1-M8/M9: saving with needed agreements left empty says which ones, not "saved"; focus moves to the message', r1_agreements_warn)

    def r1_focus_and_pin():
        c8 = new_ctx(b); p8 = c8.new_page(); p8.on('dialog', lambda d: d.accept())
        signup(p8, 'Focus Parent', 'focus@example.com', query='?for=online')
        for t in ['contact', 'terms', 'online_practice']: p8.check('#consent-' + t)
        p8.click('#save-consents'); p8.fill('#cname', 'Fay'); p8.fill('#cpin', '1234'); p8.get_by_role('button', name='Add child').click()
        expect(p8.locator('#add-child-form .msg.err')).to_contain_text('too easy'); assert p8.locator('[data-child]').count() == 0, 'a weak PIN is not sent'
        assert p8.input_value('#cname') == 'Fay', 'what was typed is kept'
        p8.fill('#cpin', '2016'); p8.get_by_role('button', name='Add child').click(); expect(p8.locator('#add-child-form .msg.err')).to_contain_text('too easy')
        p8.fill('#cpin', '7391'); p8.get_by_role('button', name='Add child').click()
        expect(p8.locator('.msg.ok')).to_contain_text('Child added'); assert p8.evaluate('document.activeElement.classList.contains("msg")'), 'focus moves to the result after adding a child'
        # Edit -> a weak new PIN is refused by the database rule too, and the page says so
        p8.locator('[data-child] button', has_text='Edit').click(); p8.fill('input[aria-label="New PIN"]', '0000'); p8.get_by_role('button', name='Save', exact=True).click()
        expect(p8.locator('.msg.err')).to_contain_text('too easy')
        p8.locator('[data-child] button', has_text='Edit').click(); p8.fill('input[aria-label="New PIN"]', '4829'); p8.get_by_role('button', name='Save', exact=True).click(); expect(p8.locator('.msg.ok')).to_contain_text('Saved')
        c8.close()
    check('R1-M7/M9: weak PINs are explained before sending and refused on Edit; focus moves to the result', r1_focus_and_pin)

    def r1_lockout_alert():
        c9 = new_ctx(b); p9 = c9.new_page(); p9.on('dialog', lambda d: d.accept())
        signup(p9, 'Lock Parent', 'lock@example.com', query='?for=online')
        for t in ['contact', 'terms', 'online_practice']: p9.check('#consent-' + t)
        p9.click('#save-consents'); p9.fill('#cname', 'Lou'); p9.fill('#cpin', '7391'); p9.get_by_role('button', name='Add child').click(); expect(p9.locator('[data-child]')).to_have_count(1)
        fam = [p for p in mockdb(p9)['parents'] if p['email'] == 'lock@example.com'][0]['family_code']
        cp = c9.new_page(); cp.goto(BASE + '/portal/child/')
        for i in range(5):
            cp.fill('#code', fam); cp.fill('#name', 'Lou'); cp.fill('#pin', '8%d29' % i); cp.get_by_role('button', name='Sign in').click(); expect(cp.locator('#pin')).to_have_value('')
        cp.fill('#code', fam); cp.fill('#name', 'Lou'); cp.fill('#pin', '7391'); cp.get_by_role('button', name='Sign in').click()
        expect(cp.locator('.msg.err')).to_be_visible(); assert 'practice' not in cp.url, 'a locked child cannot sign in even with the right PIN'
        p9.goto(BASE + '/portal/'); expect(p9.locator('#pin-alerts')).to_contain_text('Lou was locked out'); expect(p9.locator('#pin-alerts')).to_contain_text('choose a new PIN')
        p9.goto(BASE + '/portal/children/'); expect(p9.locator('#pin-alerts')).to_be_visible()
        p9.click('#dismiss-alerts'); expect(p9.locator('#pin-alerts')).to_have_count(0)
        c9.close()
    check('R1-M7: five wrong PINs lock the child (even the right PIN is refused) and the parent sees an alert on the dashboard until dismissed', r1_lockout_alert)

    def r1_remove_with_access():
        c10 = new_ctx(b); p10 = c10.new_page(); p10.on('dialog', lambda d: d.accept())
        signup(p10, 'Two Parent', 'two@example.com', query='?for=online')
        for t in ['contact', 'terms', 'online_practice']: p10.check('#consent-' + t)
        p10.click('#save-consents')
        for nm, pn in (('Ann', '7391'), ('Bo', '6204')):
            p10.fill('#cname', nm); p10.fill('#cpin', pn); p10.get_by_role('button', name='Add child').click(); expect(p10.locator('[data-child]', has_text=nm)).to_be_visible()
        patch(p10, "var a=db.children.filter(function(c){return c.display_name==='Ann'})[0];db.access.push({id:'ax',child_id:a.id,level:2,format:'online',source:'admin',status:'active',created_at:'2026-11-01T00:00:00Z'})")
        p10.reload(); row = p10.locator('[data-child]', has_text='Ann'); row.get_by_role('button', name='Remove').click()
        expect(p10.locator('.msg.err')).to_contain_text('online access'); expect(p10.locator('.ask')).to_contain_text('would end it')
        assert len(mockdb(p10)['children']) == 2, 'nothing was removed'
        expect(p10.locator('[data-giveup]')).to_be_disabled(); p10.check('#giveup-' + mockdb(p10)['children'][0]['id'])
        p10.locator('[data-move]').click(); expect(p10.locator('.msg.ok')).to_contain_text('Access moved')
        db = mockdb(p10); assert [c['display_name'] for c in db['children'] if c['display_name'] in ('Ann', 'Bo')] == ['Bo'] and db['access'][0]['child_id'] == [c['id'] for c in db['children'] if c['display_name'] == 'Bo'][0]
        # Bo now holds the access: removing Bo asks again; give it up explicitly
        p10.locator('[data-child]', has_text='Bo').get_by_role('button', name='Remove').click(); expect(p10.locator('.ask')).to_be_visible()
        p10.check('#giveup-' + [c['id'] for c in mockdb(p10)['children'] if c['display_name'] == 'Bo'][0]); p10.locator('[data-giveup]').click(); expect(p10.locator('.msg.ok')).to_contain_text('access ended')
        assert [c['display_name'] for c in mockdb(p10)['children'] if c['display_name'] in ('Ann', 'Bo')] == []
        c10.close()
    check('R1-M5: removing a child who holds online access asks what to do (move it to a sibling, or give it up with an explicit tick)', r1_remove_with_access)

    def r1_stripe_tamper():
        MODE[0] = 'stripe'
        c11 = new_ctx(b); p11 = c11.new_page(); p11.on('dialog', lambda d: d.accept())
        signup(p11, 'Pay Parent', 'pay@example.com', query='?for=live')
        for t in ['contact', 'terms', 'recording', 'childs_work']: p11.check('#consent-' + t)
        p11.click('#save-consents'); p11.fill('#cname', 'Pip'); p11.fill('#cpin', '7391'); p11.get_by_role('button', name='Add child').click()
        p11.locator('input[name^="grp-"]').first.check(); p11.get_by_role('button', name='Reserve a place').first.click(); expect(p11.locator('[data-enrolment]')).to_have_count(1)
        for evil in ('https://evil.example/phish', 'http://checkout.stripe.com/x', 'https://checkout.stripe.com.evil.example/x', 'https://user:pw@checkout.stripe.com/x', 'javascript:alert(1)'):
            def tampered(evil):
                return lambda r: r.fulfill(status=200, content_type='application/json', body=json.dumps({'url': evil}))
            p11.route('**/api/stripe-create-checkout', tampered(evil))
            p11.locator('[data-pay-online]').click(); expect(p11.locator('.msg.err')).to_contain_text('Could not start the payment')
            assert p11.url.startswith(BASE), evil + ' -> ' + p11.url
            p11.unroute('**/api/stripe-create-checkout')
        MODE[0] = 'paynow_manual'; c11.close()
    check('R1-L1: a tampered payment URL (other host, http, lookalike host, userinfo, javascript:) is never followed', r1_stripe_tamper)

    def r1_long_name_and_idle():
        c12 = new_ctx(b); p12 = c12.new_page(); p12.on('dialog', lambda d: d.accept())
        signup(p12, 'Long' * 12, 'longname@example.com', query='?for=online')
        for t in ['contact', 'terms', 'online_practice']: p12.check('#consent-' + t)
        p12.click('#save-consents'); p12.goto(BASE + '/portal/children/'); p12.fill('#cname', 'W' * 30); p12.fill('#cpin', '7391'); p12.get_by_role('button', name='Add my child').click(); expect(p12.locator('[data-child-card]')).to_have_count(1)
        for path in ['/portal/', '/portal/children/', '/portal/books/', '/portal/trial/']:
            p12.goto(BASE + path); p12.wait_for_selector('main h1'); assert p12.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth') <= 0, path + ' scrolls sideways with a 30-letter nickname'
        fam = [p for p in mockdb(p12)['parents'] if p['email'] == 'longname@example.com'][0]['family_code']
        cp = c12.new_page(); cp.goto(BASE + '/portal/child/'); cp.fill('#code', fam); cp.fill('#name', 'W' * 30); cp.fill('#pin', '7391'); cp.get_by_role('button', name='Sign in').click()
        expect(cp.locator('#bye')).to_be_visible(); assert cp.locator('#bye').bounding_box()['y'] < 300, 'Sign out is at the top of the list'
        assert cp.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth') <= 0
        cp.evaluate("sessionStorage.setItem('mi-child-seen', String(Date.now() - 31 * 60 * 1000))"); cp.reload(); cp.wait_for_url('**/portal/child/**')
        assert 'ended=idle' in cp.url and cp.evaluate("sessionStorage.getItem('mi-child')") is None; expect(cp.locator('#ended-note')).to_contain_text('away for a while')
        assert [x for x in mockdb(cp)['child_sessions']][0]['revoked'], 'the idle sign-out revokes the token in the database'
        c12.close()
    check('R1-M12/L6: a 30-letter nickname does not scroll the pages sideways; Sign out is at the top; 31 minutes idle signs the child out', r1_long_name_and_idle)

    def r1_trial_phone():
        c13 = new_ctx(b); p13 = c13.new_page(); p13.on('dialog', lambda d: d.accept())
        signup(p13, 'Phone Parent', 'phone@example.com', query='?for=online')
        patch(p13, "db.parents.filter(function(p){return p.email==='phone@example.com'})[0].phone='81112222'")
        p13.goto(BASE + '/portal/trial/'); p13.wait_for_selector('#trial-phone')
        p13.check('#need-contact'); p13.check('#need-terms'); p13.fill('#trial-phone', '93334444'); p13.get_by_role('button', name='Send my request').click()
        expect(p13.locator('.msg.ok, #trial-done')).to_be_visible()
        db = mockdb(p13); assert [p for p in db['parents'] if p['email'] == 'phone@example.com'][0]['phone'] == '81112222', 'the account phone is not overwritten silently'
        assert 'phone for this request: 93334444' in db['trials'][-1]['note'], db['trials'][-1]['note']
        c13.close()
    check('R1-L9: a different phone typed on the trial form does not overwrite the account phone (goes into the request note unless ticked)', r1_trial_phone)

    def r1_paynow_placeholder():
        c15 = b.new_context(viewport={'width': 375, 'height': 800}); c15.set_default_timeout(6000); c15.add_init_script(SEED + MOCK)
        c15.route('**/portal/config.js', lambda r: r.fulfill(body="window.MI_CONFIG={SUPABASE_URL:'https://mock.supabase.co',ANON_KEY:'mock-anon',PAYMENT_MODE:'paynow_manual',PAYNOW_TO:'PayNow number or UEN (to confirm)',SITE_NAME:'Math Inquirers'};", content_type='application/javascript'))
        c15.route('**/portal/vendor/supabase.js', lambda r: r.fulfill(body='', content_type='application/javascript')); c15.route('https://mock.supabase.co/**', lambda r: r.abort())
        p15 = c15.new_page(); p15.on('dialog', lambda d: d.accept())
        signup(p15, 'Pn Parent', 'pn@example.com', query='?for=live')
        for t in ['contact', 'terms', 'recording', 'childs_work']: p15.check('#consent-' + t)
        p15.click('#save-consents'); p15.fill('#cname', 'Pat'); p15.fill('#cpin', '7391'); p15.get_by_role('button', name='Add child').click()
        p15.locator('input[name^="grp-"]').first.check(); p15.get_by_role('button', name='Reserve a place').first.click(); expect(p15.locator('[data-enrolment]')).to_have_count(1)
        line = p15.locator('[data-paynow-line]').first.inner_text(); assert 'to confirm' not in line and 'WhatsApp' in line, line
        c15.close()
    check('R1-L10: with PORTAL_PAYNOW_TO unset the page does not show the "(to confirm)" placeholder as a PayNow target', r1_paynow_placeholder)

    def r1_admin_refund_due():
        c14 = new_ctx(b); p14 = c14.new_page(); p14.on('dialog', lambda d: d.accept()); p14.on('dialog', lambda d: None)
        signup(p14, 'Late Parent', 'late@example.com', query='?for=online')
        for t in ['contact', 'terms', 'online_practice']: p14.check('#consent-' + t)
        p14.click('#save-consents'); p14.fill('#cname', 'Lee'); p14.fill('#cpin', '7391'); p14.get_by_role('button', name='Add child').click(); expect(p14.locator('[data-child]')).to_have_count(1)
        patch(p14, "var c=db.children.filter(function(x){return x.display_name==='Lee'})[0],u=db.users.filter(function(x){return x.email==='late@example.com'})[0];db.ext_orders.push({id:'ol',reference:'MI-LATE01',parent_id:u.id,child_id:c.id,child_label:'Lee',level:2,format:'online',product_id:'ext-l2-online',amount_cents:1100,currency:'SGD',method:'stripe',status:'cancelled',paid_at:null,ship_status:'not_needed',ship_name:null,ship_address:null,ship_postal:null,ship_phone:null,created_at:'2026-11-01T00:00:00Z',refund_due:true,paid_after_cancel_at:'2026-11-01T01:00:00Z',admin_note:'Stripe payment received after the order was cancelled: refund it, or reinstate it if online-only'})")
        admin_login(p14); admin_tab(p14, 'Book orders')
        expect(p14.locator('#refund-banner')).to_contain_text('1 order needs a refund decision')
        p14.locator('#order-filter [data-filter="refund"]').click()
        row = p14.locator('[data-order="MI-LATE01"]'); expect(row).to_contain_text('refund due'); expect(row.locator('[data-admin-note]')).to_contain_text('after the order was cancelled')
        row.locator('[data-reinstate]').click(); expect(p14.locator('.msg.ok')).to_contain_text('Reinstated')
        db = mockdb(p14); assert db['ext_orders'][0]['status'] == 'paid' and not db['ext_orders'][0]['refund_due'] and db['access'][0]['child_id'] == db['ext_orders'][0]['child_id']
        c14.close()
    check('R1-M3: admin sees money received on a cancelled order flagged "refund due" and can reinstate an online order', r1_admin_refund_due)

    # ============ layout, theme, accessibility, CSP ============
    def pages_layout():
        login(page, 'kim@example.com', 'longenough1')
        for path in ['/portal/', '/portal/children/', '/portal/books/', '/portal/trial/', '/portal/child/']:
            page.goto(BASE + path); page.wait_for_selector('main h1, main h2'); assert overflow() <= 0, '%s overflows by %s' % (path, overflow())
        admin_login(page)
        for tab in ['Book orders', 'Access', 'Trials and previews', 'Funnel', 'Group report']:
            admin_tab(page, tab); page.wait_for_timeout(100); assert overflow() <= 0, '%s overflows by %s' % (tab, overflow())
    check('no horizontal scroll at 375px on every new page and admin tab', pages_layout)
    def a11y():
        for path in ['/portal/books/', '/portal/trial/', '/portal/children/', '/portal/child/']:
            login(page, 'kim@example.com', 'longenough1') if path != '/portal/child/' else None
            page.goto(BASE + path); page.wait_for_selector('main h1')
            bad = page.evaluate("""() => [...document.querySelectorAll('input:not([type=hidden]),select,textarea')].filter(e => {
                if (e.getAttribute('aria-label')) return false; if (e.id && document.querySelector('label[for="' + e.id + '"]')) return false; if (e.closest('label')) return false; return true; }).map(e => e.outerHTML.slice(0, 80))""")
            assert not bad, path + ' unlabelled: %s' % bad
            assert page.locator('h1').count() == 1, path + ' needs exactly one h1'
            assert page.evaluate("document.documentElement.lang") == 'en'
    check('every field has a label; one h1 per page; lang set', a11y)
    def dark_desktop():
        c6 = b.new_context(viewport={'width': 1100, 'height': 800}, color_scheme='dark'); c6.add_init_script(SEED + MOCK)
        c6.route('**/portal/config.js', lambda r: r.fulfill(body=CONFIG(), content_type='application/javascript')); c6.route('**/portal/vendor/supabase.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
        p6 = c6.new_page(); p6.goto(BASE + '/portal/books/'); expect(p6.locator('#signed-out')).to_be_visible()
        bg = p6.evaluate('getComputedStyle(document.body).backgroundColor'); assert bg == 'rgb(15, 22, 38)', bg
        c6.close()
    check('dark mode renders on the new pages', dark_desktop)
    check('no JS errors', lambda: (not errors) or (_ for _ in ()).throw(AssertionError(errors[:3])))
    check('no requests outside the page origin (no CDN, no third party, no real Supabase)', lambda: (not external) or (_ for _ in ()).throw(AssertionError(external[:3])))
    b.close()

if fails: print('\nFAILED:', fails); sys.exit(1)
print('\nALL PORTAL UI TESTS PASSED')
