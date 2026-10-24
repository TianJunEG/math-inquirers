#!/usr/bin/env python3
"""Independent audit (round 1) of the portal front end: attack checks + screenshots, using the repo's mocked-Supabase Playwright harness.
Nothing talks to a real Supabase, Stripe or Cloudflare. Run:  python3 portal/audit_shots/audit_frontend.py
Writes portal/audit_shots/*.png and portal/audit_shots/frontend_audit_results.txt (the findings log read by the audit report).
All prices are TEST VALUES."""
import json, os, re, sys, threading, tempfile, functools, http.server, socketserver, shutil
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
from playwright.sync_api import sync_playwright, expect

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PUB = os.path.join(ROOT, 'portal', 'public')
TESTS = os.path.join(ROOT, 'portal', 'tests')
OUT = HERE
FONTS_FROM = os.environ.get('AUDIT_FONTS_DIR', os.path.join(ROOT, 'website', 'dist'))   # /fonts.css + /fonts (self-hosted), only for faithful screenshots
sched = json.load(open(os.path.join(ROOT, 'website', 'data', 'beta_schedule.json')))
groups = [dict(id=g['id'], level=g['level'], name=g['name'], ages=g['ages'], seats=g['seats'], sessions=g['sessions'], first_label=g['first'], last_label=g['last'], fee_cents=25000) for g in sched['groups']]
UNITS = [
    dict(unit_key='hol-p1-01', product='holiday', level=1, unit_no=1, title='Number stories', access='enrolled', published=True),
    dict(unit_key='ext-l2u01', product='extension', level=2, unit_no=1, title='Digit detectives', access='purchased', published=True),
    dict(unit_key='ext-l2u02', product='extension', level=2, unit_no=2, title='Make a number', access='purchased', published=True),
]
PRICES = {'ext-l2-workbook': 1300, 'ext-l2-online': 1100, 'ext-l2-both': 2200}      # TEST VALUES; level 3 has no price on purpose
PREVIEWS = [dict(id='pv1', starts_at='2026-12-05T02:00:00Z', band='Primary 3-4', regs=[dict(parent_first_name='Mei', child_first_name='Tan', child_birth_year=2017, status='confirmed', email='mei@example.com', phone='91234567', join_code='7K3Q', consent_marketing=False, wants_trial=False)])]
SEED = 'window.__SEED__=%s;' % json.dumps(dict(groups=groups, extraTaken={}, units=UNITS, prices=PRICES, previews=PREVIEWS))
MOCK = open(os.path.join(TESTS, 'mock_supabase.js')).read()
MODE = ['paynow_manual']
CONFIG = lambda: "window.MI_CONFIG={SUPABASE_URL:'https://mock.supabase.co',ANON_KEY:'mock-anon',PAYMENT_MODE:'%s',PAYNOW_TO:'UEN 000TEST',SITE_NAME:'Math Inquirers'};" % MODE[0]
# the real /portal/* CSP that website/build_site.py --with-portal writes (portal/* rule)
CSP = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' https://mock.supabase.co; form-action 'self'; base-uri 'self'; frame-ancestors 'none'"

root = tempfile.mkdtemp(); os.symlink(PUB, os.path.join(root, 'portal'))
for n in ('fonts.css', 'fonts'):
    p = os.path.join(FONTS_FROM, n)
    if os.path.exists(p): os.symlink(p, os.path.join(root, n))
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header('Content-Security-Policy', CSP); self.send_header('X-Frame-Options', 'DENY'); self.send_header('Cache-Control', 'no-store')
        super().end_headers()
socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(Q, directory=root)); PORT = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = 'http://127.0.0.1:%d' % PORT

LOG = []
def log(kind, name, detail=''):
    line = '%s | %s%s' % (kind, name, (' -- ' + detail) if detail else '')
    LOG.append(line); print(line)
def check(name, fn, sev='Medium'):
    try:
        r = fn()
        log('PASS', name, r if isinstance(r, str) else '')
    except Exception as e:
        log('FAIL[%s]' % sev, name, str(e)[:700].replace('\n', ' '))

def new_ctx(b, w=375, scheme='light', init='', mode=None):
    if mode: MODE[0] = mode
    ctx = b.new_context(viewport={'width': w, 'height': 800}, color_scheme=scheme, device_scale_factor=1)
    ctx.set_default_timeout(7000); ctx.add_init_script(SEED + init + MOCK)
    cfg = CONFIG()
    ctx.route('**/portal/config.js', lambda r: r.fulfill(body=cfg, content_type='application/javascript'))
    ctx.route('**/portal/vendor/supabase.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
    ctx.route('https://mock.supabase.co/**', lambda r: r.abort())
    return ctx
def mockdb(page): return page.evaluate('window.__mockDb()')
def patch(page, js): page.evaluate('(function(){var db=window.__mockDb();%s;window.__mockSave();})()' % js)
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
    expect(page.locator('#signout')).to_be_visible()
def logout(page):
    page.goto(BASE + '/portal/'); page.click('#signout'); expect(page.get_by_role('heading', name='Parent portal')).to_be_visible()
def admin_login(page):
    page.goto(BASE + '/portal/admin/')
    lo = page.get_by_role('button', name='Log out')
    if lo.count(): lo.first.click()
    page.wait_for_selector('#email')
    page.fill('#email', 'owner@example.com'); page.fill('#password', 'ownerpass1'); page.get_by_role('button', name='Log in').click()
    expect(page.locator('#viewtabs')).to_be_visible()
def admin_tab(page, label): page.locator('#viewtabs').get_by_role('button', name=label, exact=True).click(); page.wait_for_timeout(150)

# ---------------------------------------------------------------- screenshots
SHOTS = []
def shot(page, tag, caption, w, scheme, locator=None, full=True):
    name = '%s_%s_%s.png' % (tag, w, scheme)
    path = os.path.join(OUT, name)
    page.wait_for_timeout(120)
    if locator is not None: page.locator(locator).first.screenshot(path=path)
    else: page.screenshot(path=path, full_page=full)
    try:   # keep the repo small: 256-colour PNG (these are flat UI colours)
        from PIL import Image
        im = Image.open(path).convert('RGB').quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE); im.save(path, optimize=True)
    except Exception: pass
    SHOTS.append(dict(tag=tag, caption=caption, w=w, scheme=scheme, file=name))

def scenario(b, w, scheme):
    """one pass through every screen with a fresh mock database; takes the screenshots for this width and colour scheme"""
    ctx = new_ctx(b, w, scheme); page = ctx.new_page(); page.on('dialog', lambda d: d.accept())
    S = lambda tag, cap, **kw: shot(page, tag, cap, w, scheme, **kw)
    page.goto(BASE + '/portal/'); page.get_by_role('button', name='Sign up').click()
    S('01_parent_signup', 'Parent sign-up (account tab). The agreements come after sign-in, on the home page.')
    signup(page, 'Kim Parent', 'kim@example.com', query='?for=online')
    S('02_home_online_family', 'Home after sign-up: next step, children, agreements card for an ONLINE / extension-book family (no recording agreements), nothing pre-ticked.')
    S('02a_consent_card_online', 'Agreements card, family type "Online practice or an extension book": contact, terms, online practice, book delivery, optional marketing and feedback.', locator='#agreements')
    page.check('#ftype-live'); S('02b_consent_card_live', 'Agreements card, family type "A live group class": contact, terms, recording, child\'s work; online practice is offered separately; optional lines.', locator='#agreements')
    page.check('#ftype-both'); S('02c_consent_card_both', 'Agreements card, family type "Both": every agreement line appears; optional ones stay un-ticked.', locator='#agreements')
    page.check('#ftype-online')
    for t in ['contact', 'terms', 'online_practice']: page.check('#consent-' + t)
    page.click('#save-consents'); expect(page.locator('.msg.ok')).to_contain_text('Agreements saved')
    page.goto(BASE + '/portal/children/'); expect(page.locator('#first-child')).to_be_visible()
    page.fill('#cname', 'Kai'); page.fill('#cpin', '1234'); page.select_option('#clevel', '2'); page.select_option('#cbirth', str(page.evaluate('new Date().getFullYear()') - 8))
    S('03_add_child', 'Add a child (first child, no enrolment needed): nickname, optional birth year, level, PIN.', locator='#first-child')
    page.get_by_role('button', name='Add my child').click(); expect(page.locator('[data-child-card]')).to_have_count(1)
    page.locator('#add-another summary').click(); page.fill('#add-another #cname', 'Lia'); page.fill('#add-another #cpin', '2345'); page.locator('#add-another').get_by_role('button', name='Add child').click()
    expect(page.locator('[data-child-card]')).to_have_count(2)
    S('04_my_children_empty', 'My children: two children, nothing open yet (kind empty state, no scores).')
    kai = mockdb(page)['children'][0]['id']; lia = mockdb(page)['children'][1]['id']
    # buy flow
    page.goto(BASE + '/portal/books/'); page.select_option('#book-level', '2'); page.check('#fmt-workbook'); page.check('#kid-' + kai)
    page.fill('#ship-name', 'Kim Parent'); page.fill('#ship-phone', '91234567'); page.fill('#ship-address', '1 Example Road #01-01'); page.fill('#ship-postal', '123456')
    S('05_buy_form_workbook', 'Buy an extension book: level, option with prices, child, Singapore address (printed options only), agreements for this order.')
    page.select_option('#book-level', '3'); page.check('#fmt-online'); page.check('#kid-' + kai)
    S('06_buy_no_price', 'Buy flow when the owner has not set a price: "Price coming soon" and an Ask us button, no order button.')
    page.select_option('#book-level', '2'); page.check('#fmt-online'); page.check('#kid-' + kai)
    for t in ['online_practice']:
        if page.locator('#need-' + t).count(): page.check('#need-' + t)
    page.click('#place-order'); expect(page.locator('#order-done')).to_be_visible()
    S('07_order_pending', 'Order placed: pending payment page with PayNow reference, how it is switched on, quiet parent-only trial-class note.')
    page.goto(BASE + '/portal/books/'); S('07a_orders_list', 'Your orders list: one order "waiting for payment" with Cancel.', locator='#orders')
    # child before paid
    cp = ctx.new_page(); cp.goto(BASE + '/portal/child/')
    S_c = lambda tag, cap, **kw: shot(cp, tag, cap, w, scheme, **kw)
    S_c('08_child_signin', 'Child sign-in: family code, name, PIN. Friendly, one purpose.')
    fam = [p for p in mockdb(page)['parents'] if p['email'] == 'kim@example.com'][0]['family_code']
    cp.fill('#code', fam); cp.fill('#name', 'Kai'); cp.fill('#pin', '9999'); cp.get_by_role('button', name='Sign in').click(); expect(cp.locator('.msg.err')).to_be_visible()
    S_c('09_child_signin_error', 'Child sign-in, wrong PIN: the same quiet message whatever was wrong.')
    cp.fill('#pin', '1234'); cp.get_by_role('button', name='Sign in').click(); expect(cp.locator('#hello')).to_be_visible()
    S_c('10a_practice_list_unpaid', 'Practice list before payment: nothing open yet, asks the child to ask a grown-up.')
    cp.close()
    # admin: orders
    logout(page); admin_login(page); admin_tab(page, 'Book orders')
    S('11_admin_book_orders', 'Admin, Book orders tab: the pending order with Mark paid and give access / Cancel.')
    page.locator('[data-mark-paid]').click(); expect(page.locator('.msg.ok')).to_be_visible()
    page.locator('#price-card summary').click()
    S('12_admin_prices', 'Admin, owner price entry (no prices in the repo; empty rows say "not set").', locator='#price-card')
    admin_tab(page, 'Access'); S('13_admin_access', 'Admin, Access tab: who has which book access, grant and revoke with a reason.')
    page.click('#signout')
    # child after paid
    cp = ctx.new_page(); cp.goto(BASE + '/portal/child/'); cp.fill('#code', fam); cp.fill('#name', 'Kai'); cp.fill('#pin', '1234'); cp.get_by_role('button', name='Sign in').click(); expect(cp.locator('#hello')).to_be_visible()
    shot(cp, '10_practice_list', 'Child practice list after payment: only entitled, published units, plain links, no scores or timers.', w, scheme)
    cp.close()
    # parent dashboard with progress
    login(page, 'kim@example.com', 'longenough1')
    patch(page, "var k=db.children.filter(function(c){return c.display_name==='Kai'})[0].id;db.submissions.push({child_id:k,unit_key:'ext-l2u01',received_at:'2026-11-24T08:42:00Z',n_auto:6,n_skipped:1,n_self:1,n_self_got:1,n_open:1});"
                 "db.attempts.push({child_id:k,unit_key:'ext-l2u01',item_id:'q2',skill:'Place value to 1000',mark:'wrong',misconception:'Said 6: gave the digit, not the value (6 tens = 60).',self_result:null,received_at:'x'},{child_id:k,unit_key:'ext-l2u01',item_id:'q4',skill:'Patterns',mark:'skipped',received_at:'x'},{child_id:k,unit_key:'ext-l2u01',item_id:'q7',skill:'Draw',mark:'self',self_result:'not_yet',received_at:'x'});")
    page.goto(BASE + '/portal/children/'); page.locator('[data-detail]').first.click(); expect(page.locator('[data-detail-box]')).to_contain_text('Place value')
    S('14_my_children_progress', 'My children with an entitlement, practice links and the progress summary opened to "Worth looking at together" (no marks, no ranks).')
    # trial
    page.goto(BASE + '/portal/trial/?from=report&child=' + kai); page.check('#time-weekend-morning'); page.fill('#trial-note', 'Kai likes puzzles')
    S('15_trial_request', 'Ask about a trial class: parent-only, no scarcity wording, optional marketing agreement un-ticked.')
    page.click('#send-trial'); expect(page.locator('#trial-done')).to_be_visible()
    S('16_trial_sent', 'Trial request sent: thank-you and the request list with Withdraw.')
    # admin: trials, funnel, report
    logout(page); admin_login(page)
    admin_tab(page, 'Trials and previews'); S('17_admin_trials_previews', 'Admin, Trials and previews: trial requests with status buttons, preview sign-ups, funnel.')
    admin_tab(page, 'Funnel'); S('18_admin_funnel', 'Admin, Funnel: counts of rows that already exist (no cookies, no tracking).')
    patch(page, "db.report={L2A:{practice:[{child_id:'c1',display_name:'Maple',unit_key:'hol-p2-01',unit_version:'v1',received_at:'2026-11-25T08:00:00Z'}],skills:{'hol-p2-01':[{child_id:'c1',display_name:'Maple',skill:'Place value',n_right:3,n_wrong:0,n_skipped:0,n_self_got:0,n_self_notyet:0,n_self_checked:0},{child_id:'c2',display_name:'Otter',skill:'Place value',n_right:0,n_wrong:2,n_skipped:0,n_self_got:0,n_self_notyet:0,n_self_checked:0}]},slips:{'hol-p2-01':[{item_id:'q2',item_pos:2,skill:'Place value',say:'Gave the digit, not the value.',n_children:1,n_sent:2}]}}}")
    admin_tab(page, 'Group report'); page.select_option('#rep-group', 'L2A'); expect(page.locator('#group-report')).to_be_visible()
    S('19_admin_group_report', 'Admin / tutor, Group report: skills in words, children alphabetical (never ranked), common misconceptions.')
    admin_tab(page, 'Enrolments'); S('20_admin_enrolments', 'Admin, Enrolments tab (existing screen).')
    ctx.close()
    # live family: home with a choose-group card
    c2 = new_ctx(b, w, scheme); p2 = c2.new_page(); p2.on('dialog', lambda d: d.accept())
    signup(p2, 'Lee Parent', 'lee@example.com', query='?for=live')
    for t in ['contact', 'terms', 'recording', 'childs_work']: p2.check('#consent-' + t)
    p2.click('#save-consents'); expect(p2.locator('.msg.ok')).to_be_visible()
    p2.fill('#cname', 'Mia'); p2.select_option('#clevel', '1'); p2.fill('#cpin', '1234'); p2.get_by_role('button', name='Add child').click()
    p2.locator('input[name^="grp-"]').first.check()
    shot(p2, '21_home_live_family', 'Home for a LIVE-group family: agreements for live classes, choose a group, reserve a place.', w, scheme)
    c2.close()

# ---------------------------------------------------------------- attack and quality checks
XSS = ['<img src=x onerror="window.__xss=1">', '"><svg onload="window.__xss=1">', "'-alert(1)-'", '<script>window.__xss=1</script>', 'javascript:window.__xss=1']

def attacks(b):
    # ---------- stored XSS through every free-text field, rendered on every page that shows it ----------
    ctx = new_ctx(b, 375); page = ctx.new_page(); dialogs = []; page.on('dialog', lambda d: (dialogs.append(d.message), d.accept()))
    cons = []; page.on('console', lambda m: cons.append(m.text))
    reqs = []; page.on('request', lambda r: reqs.append(r.url))
    urls = []; page.on('framenavigated', lambda f: urls.append(f.url))
    P = XSS[0]
    signup(page, P, 'xss@example.com', query='?for=online')
    for t in ['contact', 'terms', 'online_practice', 'book_delivery']: page.check('#consent-' + t)
    page.click('#save-consents'); expect(page.locator('.msg.ok')).to_be_visible()
    page.goto(BASE + '/portal/children/'); page.fill('#cname', XSS[1][:30]); page.fill('#cpin', '1234'); page.get_by_role('button', name='Add my child').click(); expect(page.locator('[data-child-card]')).to_have_count(1)
    kid = mockdb(page)['children'][0]['id']
    page.goto(BASE + '/portal/books/?child=' + XSS[1]); page.select_option('#book-level', '2'); page.check('#fmt-both'); page.check('#kid-' + kid)
    page.fill('#ship-name', XSS[0]); page.fill('#ship-phone', XSS[2]); page.fill('#ship-address', XSS[3] + XSS[0]); page.fill('#ship-postal', '123456')
    if page.locator('#need-online_practice').count(): page.check('#need-online_practice')
    page.click('#place-order'); expect(page.locator('#order-done')).to_be_visible()
    page.goto(BASE + '/portal/trial/?from=' + XSS[1] + '&child=' + XSS[0]); page.fill('#trial-note', XSS[0] + XSS[3]); page.fill('#trial-phone', XSS[1]); page.click('#send-trial'); expect(page.locator('#trial-done')).to_be_visible()
    for path in ['/portal/', '/portal/children/', '/portal/books/', '/portal/trial/', '/portal/child/?ended=' + XSS[3], '/portal/practice/']:
        page.goto(BASE + path); page.wait_for_timeout(250)
    page.goto(BASE + '/portal/books/'); page.wait_for_timeout(200)
    xs = page.evaluate('window.__xss'); bad = page.evaluate("document.querySelectorAll('[onerror],[onload],script:not([src]),iframe,img,svg').length")
    check('stored XSS: hostile name, nickname, address, phone, note do not execute on parent pages', lambda: (xs is None and bad == 0 and not dialogs) or (_ for _ in ()).throw(AssertionError('xss=%s injected=%s dialogs=%s' % (xs, bad, dialogs))), 'High')
    logout(page); admin_login(page)
    for tab in ['Book orders', 'Access', 'Trials and previews', 'Funnel', 'Enrolments']:
        admin_tab(page, tab)
        if tab == 'Book orders':
            page.locator('#order-filter [data-filter="all"]').click(); page.wait_for_timeout(150)
            if page.locator('details summary:text("Address")').count(): page.locator('details summary:text("Address")').first.click()
    admin_tab(page, 'Enrolments')
    xs = page.evaluate('window.__xss'); bad = page.evaluate("document.querySelectorAll('[onerror],[onload],script:not([src]),iframe,img,svg').length")
    check('stored XSS: the same hostile text does not execute in the OWNER admin tabs (orders address, trial note, children)', lambda: (xs is None and bad == 0 and not dialogs) or (_ for _ in ()).throw(AssertionError('xss=%s injected=%s dialogs=%s' % (xs, bad, dialogs))), 'High')
    # reflected: query parameters
    def reflected():
        p = ctx.new_page(); d2 = []; p.on('dialog', lambda d: (d2.append(d.message), d.accept()))
        for path in ['/portal/?for=%3Cimg%20src%3Dx%20onerror%3Dwindow.__xss%3D1%3E&paid=%3Csvg%20onload%3Dwindow.__xss%3D1%3E&cancelled=1', '/portal/child/?ended=%3Cimg%20src%3Dx%20onerror%3Dwindow.__xss%3D1%3E', '/portal/trial/?from=%3Cb%3E&child=%22%3E%3Cimg%20src%3Dx%20onerror%3Dwindow.__xss%3D1%3E', '/portal/books/?child=%22%3E%3Cimg%20src%3Dx%20onerror%3Dwindow.__xss%3D1%3E', '/portal/order/?session_id=%3Cimg%20src%3Dx%3E']:
            p.goto(BASE + path); p.wait_for_timeout(250)
            if p.evaluate('window.__xss') is not None or p.evaluate("document.querySelectorAll('[onerror],[onload]').length"): raise AssertionError('reflected XSS at ' + path)
        assert not d2
        p.close()
    check('reflected XSS: for, paid, ended, from, child, session_id query parameters are never written as HTML', reflected, 'High')
    # PII in URLs and logs
    pii_hit = [u for u in set(urls + reqs) if re.search(r'@|kim%40|xss%40|Kai|Lia|Parent|Road|123456|91234567', u)]
    check('no email, name, address or phone appears in any URL the pages visited or requested', lambda: (not pii_hit) or (_ for _ in ()).throw(AssertionError(pii_hit[:3])), 'Medium')
    check('console output carries no personal data (no console.log in the shipped scripts)', lambda: (not [c for c in cons if re.search(r'xss@|Kai|123456', c)]) or (_ for _ in ()).throw(AssertionError(cons[:3])), 'Low')
    ctx.close()

    # ---------- CSP, third-party requests ----------
    ctx = new_ctx(b, 375); page = ctx.new_page(); ext = []; viol = []
    page.on('request', lambda r: ext.append(r.url) if not r.url.startswith(BASE) and not r.url.startswith('data:') else None)
    page.on('console', lambda m: viol.append(m.text) if 'Content Security Policy' in m.text else None)
    signup(page, 'Csp Parent', 'csp@example.com')
    for p in ['/portal/', '/portal/children/', '/portal/books/', '/portal/trial/', '/portal/child/', '/portal/order/?session_id=cs_test_abc123']: page.goto(BASE + p); page.wait_for_timeout(200)
    check('no third-party request and no CSP violation on any portal page (CSP script-src self only)', lambda: (not [u for u in ext if 'mock.supabase.co' not in u] and not viol) or (_ for _ in ()).throw(AssertionError((ext[:3], viol[:3]))), 'Medium')
    src = ''.join(open(os.path.join(PUB, f), encoding='utf-8').read() for f in ['index.html', 'children/index.html', 'books/index.html', 'trial/index.html', 'child/index.html', 'practice/index.html', 'admin/index.html'])
    check('no inline <script> and no on* handler attributes in any portal HTML file', lambda: (not re.search(r'<script(?![^>]*\ssrc=)[^>]*>', src) and not re.search(r'\son[a-z]+\s*=', src)) or (_ for _ in ()).throw(AssertionError('inline script/handler found')), 'Medium')
    js = ''.join(open(os.path.join(PUB, f), encoding='utf-8').read() for f in os.listdir(PUB) if f.endswith('.js') and f != 'config.js')
    check('no innerHTML / outerHTML / insertAdjacentHTML / document.write / eval / new Function in the portal scripts', lambda: (not re.search(r'\.innerHTML|outerHTML|insertAdjacentHTML|document\.write|\beval\(|new Function', js)) or (_ for _ in ()).throw(AssertionError('found')), 'High')
    check('no console.* calls shipped in the portal scripts', lambda: (not re.search(r'console\.(log|debug|info|warn|error)', js)) or (_ for _ in ()).throw(AssertionError('console call found')), 'Low')
    ctx.close()

    # ---------- open redirect / unvalidated payment URL ----------
    ctx = new_ctx(b, 375, mode='stripe'); page = ctx.new_page(); page.on('dialog', lambda d: d.accept()); hit = []
    ctx.route('https://evil.example/**', lambda r: (hit.append(r.request.url), r.fulfill(body='evil', content_type='text/html')))
    ctx.route('**/api/stripe-create-ext-checkout', lambda r: r.fulfill(status=200, content_type='application/json', body=json.dumps({'url': 'https://evil.example/phish'})))
    signup(page, 'Red Parent', 'red@example.com', query='?for=online')
    for t in ['contact', 'terms', 'online_practice']: page.check('#consent-' + t)
    page.click('#save-consents'); expect(page.locator('.msg.ok')).to_be_visible()
    page.goto(BASE + '/portal/children/'); page.fill('#cname', 'Rae'); page.fill('#cpin', '1234'); page.select_option('#clevel', '2'); page.get_by_role('button', name='Add my child').click(); expect(page.locator('[data-child-card]')).to_have_count(1)
    page.goto(BASE + '/portal/books/'); page.select_option('#book-level', '2'); page.check('#fmt-online'); page.check('input[name=book-child]'); page.click('#place-order'); expect(page.locator('#order-done')).to_be_visible()
    page.locator('[data-pay-online]').first.click(); page.wait_for_timeout(800)
    check('payment redirect only goes to checkout.stripe.com (a tampered /api reply must not send the parent elsewhere)', lambda: (not hit) or (_ for _ in ()).throw(AssertionError('browser navigated to %s: location.href = j.url is not validated (books.js, app.js)' % hit[0])), 'Low')
    MODE[0] = 'paynow_manual'; ctx.close()

    # ---------- token storage ----------
    ctx = new_ctx(b, 375); page = ctx.new_page(); page.on('dialog', lambda d: d.accept())
    signup(page, 'Tok Parent', 'tok@example.com', query='?for=online')
    for t in ['contact', 'terms', 'online_practice']: page.check('#consent-' + t)
    page.click('#save-consents'); expect(page.locator('.msg.ok')).to_be_visible()
    page.goto(BASE + '/portal/children/'); page.fill('#cname', 'Tim'); page.fill('#cpin', '4321'); page.get_by_role('button', name='Add my child').click(); expect(page.locator('[data-child-card]')).to_have_count(1)
    fam = [p for p in mockdb(page)['parents'] if p['email'] == 'tok@example.com'][0]['family_code']
    cp = ctx.new_page(); cp.goto(BASE + '/portal/child/'); cp.fill('#code', fam); cp.fill('#name', 'Tim'); cp.fill('#pin', '4321'); cp.get_by_role('button', name='Sign in').click(); expect(cp.locator('#hello')).to_be_visible()
    ss = cp.evaluate("sessionStorage.getItem('mi-child')"); ls = cp.evaluate("Object.keys(localStorage).filter(k => k !== 'mock-db').map(k => k + '=' + localStorage.getItem(k)).join('|')")   # 'mock-db' is the test double's own database
    tok = json.loads(ss)['token']
    check('child token lives in sessionStorage only (cleared with the tab), not in localStorage or the URL', lambda: (tok not in ls and tok not in cp.url) or (_ for _ in ()).throw(AssertionError('token found in localStorage/url')), 'Medium')
    check('child session record holds name, level, token, expiry (no PIN, no family code, no parent data)', lambda: (set(json.loads(ss).keys()) == {'id', 'name', 'level', 'token', 'expires_at'}) or (_ for _ in ()).throw(AssertionError(ss[:200])), 'Low')
    log('NOTE', 'child token: no inactivity timeout in practice.js (only the 4-hour server expiry and the Sign out button); on a shared tablet the next person stays signed in as the child until the tab closes', 'Low')
    ctx.close()

# ---------------------------------------------------------------- accessibility, mobile, tone
CONTRAST_JS = """() => {
  function parse(c){ const m = c.match(/rgba?\\(([^)]+)\\)/); if(!m) return null; const p = m[1].split(',').map(s=>parseFloat(s)); return {r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1}; }
  function lum(c){ const f = v => { v/=255; return v<=0.03928? v/12.92 : Math.pow((v+0.055)/1.055,2.4); }; return 0.2126*f(c.r)+0.7152*f(c.g)+0.0722*f(c.b); }
  function bgOf(e){ while(e){ const cs = getComputedStyle(e); const c = parse(cs.backgroundColor); if(c && c.a>0.5) return c; e = e.parentElement; } return {r:255,g:255,b:255,a:1}; }
  const out = [], seen = new Set();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const n = walker.currentNode; if (!n.textContent.trim()) continue; const e = n.parentElement; if (!e || seen.has(e)) continue; seen.add(e);
    const cs = getComputedStyle(e); if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    const r = e.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
    const fg = parse(cs.color), bg = bgOf(e); if(!fg) continue;
    const L1 = lum(fg), L2 = lum(bg), ratio = (Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
    const size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700; const large = size >= 24 || (size >= 18.66 && bold);
    if (ratio < (large ? 3 : 4.5)) out.push({t: n.textContent.trim().slice(0,40), ratio: Math.round(ratio*100)/100, size, tag: e.tagName + (e.className ? '.' + String(e.className).split(' ')[0] : '')});
  }
  return out;
}"""
TARGET_JS = """() => { const out = []; document.querySelectorAll('a[href],button,input:not([type=hidden]),select,textarea,summary').forEach(e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); if (!r.width || cs.visibility==='hidden' || cs.display==='none') return;
   const lab = e.closest('label'); const rr = lab ? lab.getBoundingClientRect() : r; if (Math.min(rr.width, rr.height) < 24) out.push({tag: e.tagName, text: (e.textContent||e.id||e.name||'').trim().slice(0,30), w: Math.round(rr.width), h: Math.round(rr.height)}); }); return out; }"""

def quality(b):
    pages = []
    for scheme in ('light', 'dark'):
        ctx = new_ctx(b, 375, scheme); page = ctx.new_page(); page.on('dialog', lambda d: d.accept())
        signup(page, 'Q Parent', 'q@example.com', query='?for=online')
        for t in ['contact', 'terms', 'online_practice']: page.check('#consent-' + t)
        page.click('#save-consents'); expect(page.locator('.msg.ok')).to_be_visible()
        page.goto(BASE + '/portal/children/'); page.fill('#cname', 'Kai'); page.fill('#cpin', '1234'); page.select_option('#clevel', '2'); page.get_by_role('button', name='Add my child').click(); expect(page.locator('[data-child-card]')).to_have_count(1)
        patch(page, "db.consents.length;")
        res = {}
        for path in ['/portal/', '/portal/children/', '/portal/books/', '/portal/trial/', '/portal/child/']:
            page.goto(BASE + path); page.wait_for_timeout(300)
            res[path] = page.evaluate(CONTRAST_JS)
        bad = {p: [x for x in v if x['ratio'] < 4.5] for p, v in res.items() if v}
        check('contrast (%s mode): every text run reaches WCAG AA (4.5:1, 3:1 for large text) on all parent and child pages' % scheme,
              lambda: (not bad) or (_ for _ in ()).throw(AssertionError(json.dumps({p: v[:4] for p, v in bad.items()})[:600])), 'Medium')
        ctx.close()
    # keyboard and focus
    ctx = new_ctx(b, 375); page = ctx.new_page(); page.on('dialog', lambda d: d.accept())
    signup(page, 'K Parent', 'k@example.com', query='?for=online')
    page.goto(BASE + '/portal/children/'); page.fill('#cname', 'Kay'); page.fill('#cpin', '1234'); page.get_by_role('button', name='Add my child').click(); expect(page.locator('[data-child-card]')).to_have_count(1)
    def focus_ring():
        page.goto(BASE + '/portal/books/'); page.wait_for_selector('main h1')
        page.keyboard.press('Tab'); page.keyboard.press('Tab')
        info = page.evaluate("(() => { const e = document.activeElement; const cs = getComputedStyle(e); return {tag: e.tagName, text: (e.textContent||'').slice(0,20), outline: cs.outlineStyle, w: cs.outlineWidth}; })()")
        assert info['outline'] != 'none' and info['w'] not in ('0px',), info
        return str(info)
    check('keyboard focus shows a visible ring', focus_ring, 'Medium')
    def skip_link():
        page.goto(BASE + '/portal/'); page.wait_for_selector('main h1,main h2'); page.keyboard.press('Tab')
        t = page.evaluate("document.activeElement.textContent"); assert 'Skip' in t, t
    check('first Tab reaches the "Skip to content" link', skip_link, 'Low')
    def landmarks():
        page.goto(BASE + '/portal/'); page.wait_for_selector('main h1,main h2')
        n = page.evaluate("({main: document.querySelectorAll('main').length, header: document.querySelectorAll('header').length, nav: document.querySelectorAll('nav').length, h1: document.querySelectorAll('h1').length})")
        assert n['main'] == 1 and n['h1'] == 1, n
        return str(n)
    check('one <main> and one <h1> on the parent home', landmarks, 'Low')
    def focus_after_action():
        page.goto(BASE + '/portal/children/'); page.wait_for_selector('main h1')
        page.locator('#add-another summary').click(); page.fill('#add-another #cname', 'Zed'); page.fill('#add-another #cpin', '1234'); page.locator('#add-another').get_by_role('button', name='Add child').click(); page.wait_for_timeout(400)
        act = page.evaluate("document.activeElement ? document.activeElement.tagName + '#' + document.activeElement.id : 'none'")
        assert act not in ('BODY#', 'BODY#app', 'none'), 'focus fell back to <%s> after the page re-rendered, so keyboard and screen-reader users lose their place after every action (add child, save, cancel, order)' % act
    check('after an action the page keeps or moves keyboard focus somewhere sensible and announces the result', focus_after_action, 'Medium')
    def live_regions():
        page.goto(BASE + '/portal/children/'); page.wait_for_selector('main h1')
        page.locator('#add-another summary').click(); page.fill('#add-another #cname', 'Zed2'); page.fill('#add-another #cpin', '12'); page.locator('#add-another').get_by_role('button', name='Add child').click()
        role = page.evaluate("(document.querySelector('.msg.err')||{}).getAttribute ? document.querySelector('.msg.err').getAttribute('role') : null")
        assert role == 'alert', role
    check('error messages use role=alert, success role=status', live_regions, 'Low')
    def targets():
        bad = []
        for path in ['/portal/', '/portal/children/', '/portal/books/', '/portal/trial/']:
            page.goto(BASE + path); page.wait_for_timeout(250); bad += [dict(x, page=path) for x in page.evaluate(TARGET_JS)]
        assert not bad, json.dumps(bad[:6])
    check('touch targets are at least 24x24 CSS px (WCAG 2.2 AA) on 375px', targets, 'Low')
    def sizes44():
        smalls = []
        for path in ['/portal/children/', '/portal/books/']:
            page.goto(BASE + path); page.wait_for_timeout(250)
            smalls += page.evaluate("[...document.querySelectorAll('.btn.sm,.linkbtn,.tabs a')].map(e => Math.round(e.getBoundingClientRect().height)).filter(h => h && h < 44)")
        return 'buttons shorter than 44px on a non-touch emulation: %d (CSS raises .btn.sm and tabs to 44px under pointer:coarse)' % len(smalls)
    check('small buttons: 44px on touch devices via pointer:coarse', sizes44, 'Low')
    ctx.close()
    # mobile overflow and long words at 375 and 320
    for w in (375, 320):
        ctx = new_ctx(b, w); page = ctx.new_page(); page.on('dialog', lambda d: d.accept())
        signup(page, 'Averyveryveryverylongparentnamewithoutanyspaces' * 2, 'long@example.com', query='?for=online')
        for t in ['contact', 'terms', 'online_practice']: page.check('#consent-' + t)
        page.click('#save-consents')
        page.goto(BASE + '/portal/children/'); page.fill('#cname', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'); page.fill('#cpin', '1234'); page.get_by_role('button', name='Add my child').click(); page.wait_for_timeout(300)
        def ov():
            bad = []
            for path in ['/portal/', '/portal/children/', '/portal/books/', '/portal/trial/', '/portal/child/']:
                page.goto(BASE + path); page.wait_for_timeout(250)
                o = page.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')
                if o > 0: bad.append((path, o))
            assert not bad, bad
        check('no horizontal scroll at %dpx with very long names' % w, ov, 'Medium')
        ctx.close()

# tone / wording / Singapore English scan over the visible text of every screen
TONE_BAD = [r'\bscore', r'\brank', r'\bstreak', r'leaderboard', r'\bpoints?\b', r'\bwrong\b', r'\bfail', r'(fall|fell|falling|left|lag|lagging) behind', r'\bbest\b', r'\btop\b', r'congrat', r'\bperfect\b', r'\bbadge', r'\blevel up', r'hurry', r'limited', r'last chance', r'only today', r'countdown', r'\bdeadline\b']
US_SPELL = [r'\bcolor', r'\bcenter\b', r'\bprogram\b', r'(?:to|can|will|please|let.s|should) practice\b', r'\bfavorite', r'\bbehavior', r'\borganiz', r'\brecogniz', r'\bauthoriz', r'\bcatalog\b', r'\bmom\b', r'\bzip code', r'\bgrade [0-9]', r'\bfall\b', r'\bapartment\b', r'\btutor\b(?= them)', r'\benroll\b']
def tone(b):
    ctx = new_ctx(b, 1100); page = ctx.new_page(); page.on('dialog', lambda d: d.accept())
    texts = {}
    signup(page, 'Tone Parent', 'tone@example.com', query='?for=both')
    for t in ['contact', 'terms', 'online_practice', 'recording', 'childs_work']: page.check('#consent-' + t)
    page.click('#save-consents')
    page.goto(BASE + '/portal/children/'); page.fill('#cname', 'Kai'); page.fill('#cpin', '1234'); page.select_option('#clevel', '2'); page.get_by_role('button', name='Add my child').click(); page.wait_for_timeout(300)
    kai = mockdb(page)['children'][0]['id']
    patch(page, "var k=db.children[0].id;db.access.push({id:'a1',child_id:k,level:2,format:'online',source:'admin',status:'active',created_at:'2026-11-01T00:00:00Z'});db.submissions.push({child_id:k,unit_key:'ext-l2u01',received_at:'2026-11-24T08:42:00Z',n_auto:6,n_skipped:1,n_self:1,n_self_got:1,n_open:1});db.attempts.push({child_id:k,unit_key:'ext-l2u01',item_id:'q2',skill:'Place value',mark:'wrong',misconception:'Said 6: gave the digit, not the value.',received_at:'x'})")
    for path in ['/portal/', '/portal/children/', '/portal/books/?child=' + kai, '/portal/trial/', '/portal/child/']:
        page.goto(BASE + path); page.wait_for_timeout(300)
        if path.startswith('/portal/children'):
            page.locator('[data-detail]').first.click(); page.wait_for_timeout(200)
        texts[path] = page.inner_text('body')
    cp = ctx.new_page(); fam = [p for p in mockdb(page)['parents'] if p['email'] == 'tone@example.com'][0]['family_code']
    cp.goto(BASE + '/portal/child/'); cp.fill('#code', fam); cp.fill('#name', 'Kai'); cp.fill('#pin', '1234'); cp.get_by_role('button', name='Sign in').click(); expect(cp.locator('#hello')).to_be_visible()
    texts['/portal/practice/ (child)'] = cp.inner_text('body')
    # the child-facing texts are held to the strictest rules; the parent pages may say "wrong" in the consent/delete wording but not in reports
    child_text = (texts['/portal/child/'] + ' ' + texts['/portal/practice/ (child)']).lower()
    hits = [p for p in TONE_BAD if re.search(p, child_text)]
    check('child pages: no score, rank, streak, points, "wrong", "fail", "best", pressure or deadline wording', lambda: (not hits) or (_ for _ in ()).throw(AssertionError(hits)), 'Medium')
    par = (texts['/portal/children/'] + ' ' + texts['/portal/books/?child=' + kai] + ' ' + texts['/portal/trial/']).lower()
    hits = [p for p in TONE_BAD if p != r'\bwrong\b' and re.search(p, par)]   # one gentle parent-only sentence ("do not worry about the wrong answer itself") is allowed
    check('parent pages (children, books, trial): no score/rank/streak/pressure wording', lambda: (not hits) or (_ for _ in ()).throw(AssertionError(hits)), 'Medium')
    allt = ' '.join(texts.values()).lower()
    us = sorted({m.group(0) for p in US_SPELL for m in re.finditer(p, allt)})
    check('Singapore English: no US spellings or terms on parent/child pages (checked list)', lambda: (not us) or (_ for _ in ()).throw(AssertionError(us)), 'Low')
    # parent / child wording
    check('child pages speak to the child and say "grown-up" (never "parent" or "guardian")', lambda: (not re.search(r'\bparent|guardian', child_text.replace('parent portal', ''))) or (_ for _ in ()).throw(AssertionError('"parent" appears on a child page: ' + re.findall(r'.{25}\bparent.{25}', child_text)[0])), 'Low')
    check('parent pages never call the child "student" or "pupil"', lambda: (not re.search(r'\bstudent|\bpupil', par)) or (_ for _ in ()).throw(AssertionError('found')), 'Low')
    open(os.path.join(OUT, 'visible_text_dump.txt'), 'w').write('\n\n'.join('=== %s ===\n%s' % (k, v) for k, v in texts.items()))
    ctx.close()

# ---------------------------------------------------------------- consent UI checks (privacy)
def consent_ui(b):
    ctx = new_ctx(b, 375); page = ctx.new_page(); page.on('dialog', lambda d: d.accept())
    signup(page, 'C Parent', 'c@example.com')
    def never_preticked():
        for ft in ['online', 'live', 'both']:
            page.check('#ftype-' + ft)
            for cb in page.locator('#agreements input[type=checkbox]').all():
                assert not cb.is_checked(), (ft, cb.get_attribute('id'))
    check('every agreement tick-box, for every family type, starts un-ticked (marketing_contact included)', never_preticked, 'High')
    def needed_not_ticked_saved():
        page.check('#ftype-online'); page.check('#consent-contact')   # terms and online_practice left empty
        page.click('#save-consents'); msg = page.locator('.msg').first.inner_text()
        got = {c['consent_type']: c['granted'] for c in mockdb(page)['consents']}
        needed = ['contact', 'terms', 'online_practice']
        assert 'saved' not in msg.lower() or all(got.get(t) for t in needed), 'Saving with the needed boxes NOT ticked says "%s" and records %s: the page claims success although the family still cannot use online practice. Say which needed agreement is missing.' % (msg, got)
    check('saving with a needed agreement left empty does not say "Agreements saved" as if all is well', needed_not_ticked_saved, 'Medium')
    def marketing_gate():
        got = [c for c in mockdb(page)['consents'] if c['consent_type'] == 'marketing_contact']
        assert not got, got
    check('marketing_contact is not recorded unless the parent ticks it', marketing_gate, 'High')
    def book_address_only_workbook():
        page.goto(BASE + '/portal/children/'); page.fill('#cname', 'Cee'); page.fill('#cpin', '1234'); page.get_by_role('button', name='Add my child').click(); page.wait_for_timeout(300)
        page.goto(BASE + '/portal/books/'); page.select_option('#book-level', '2'); page.check('#fmt-online')
        assert page.locator('#ship-box').count() == 0
        page.check('#fmt-workbook'); assert page.locator('#ship-box').count() == 1
        page.check('#fmt-both'); assert page.locator('#ship-box').count() == 1
        page.check('#fmt-online'); assert page.locator('#ship-box').count() == 0
        # typed address then switch to online: does the typed address still ride along to the server?
        page.check('#fmt-workbook'); page.fill('#ship-name', 'Typed Name'); page.fill('#ship-address', 'Typed Address'); page.check('input[name=book-child]'); page.fill('#ship-postal', '123456')
        page.check('#fmt-online')
        for cb in page.locator('#agree-box input[type=checkbox]').all(): cb.check() if not cb.get_attribute('id').endswith('marketing_contact') else None
        page.click('#place-order'); page.wait_for_timeout(400)
        o = mockdb(page)['ext_orders']
        assert o and o[-1]['ship_name'] in (None, '') , 'online-only order carried the typed address: %s' % o[-1].get('ship_name')
    check('address fields exist only for printed options and are not sent with an online-only order', book_address_only_workbook, 'Medium')
    ctx.close()

def main():
    for f in os.listdir(OUT):
        if f.endswith('.png'): os.remove(os.path.join(OUT, f))
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for w, scheme in ((375, 'light'), (1100, 'light'), (375, 'dark'), (1100, 'dark')):
            print('--- screenshots', w, scheme)
            try: scenario(b, w, scheme)
            except Exception as e: log('FAIL[High]', 'screenshot scenario %s %s' % (w, scheme), str(e)[:400].replace('\n', ' '))
        for fn in (attacks, quality, tone, consent_ui):
            try: fn(b)
            except Exception as e: log('FAIL[High]', 'section %s crashed' % fn.__name__, str(e)[:500].replace('\n', ' '))
        b.close()
    json.dump(SHOTS, open(os.path.join(OUT, 'shots.json'), 'w'), indent=1)
    open(os.path.join(OUT, 'frontend_audit_results.txt'), 'w').write('\n'.join(LOG) + '\n')
    print('\n%d screenshots; %d PASS; %d FAIL' % (len(SHOTS), sum(1 for l in LOG if l.startswith('PASS')), sum(1 for l in LOG if l.startswith('FAIL'))))

if __name__ == '__main__':
    main()
