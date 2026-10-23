#!/usr/bin/env python3
"""Playwright test of the shop (/shop/): product cards, the 'Your list' cart, the 'Tell me when it's ready' form, the price rule and the checkout stub.
    python3 website/tests/shop_test.py [--shots DIR]        (interest_test.py runs this file too)
Needs a built site (python3 website/build_site.py). Portal mode is simulated by injecting window.MI_CONFIG and mocking the Supabase REST call;
no network is used. The price rule is tested against a temporary products file built with shop_build + build_site.wrap."""
import json, os, re, shutil, sys, tempfile, threading, functools, http.server, socketserver
from urllib.parse import unquote
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
from playwright.sync_api import sync_playwright, expect

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.abspath(os.path.join(HERE, '..'))
DIST = os.path.join(WEB, 'dist')
SHOTS = sys.argv[sys.argv.index('--shots') + 1] if '--shots' in sys.argv else None
sys.path.insert(0, WEB)
import shop_build, build_site


class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
socketserver.TCPServer.allow_reuse_address = True
def serve(directory):
    srv = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(Q, directory=directory))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, 'http://127.0.0.1:%d' % srv.server_address[1]
srv, BASE = serve(DIST)

# ---- a second site, built from a temporary products file, to test the price rule ----
TMP = tempfile.mkdtemp(prefix='shoptest-')
prods = json.load(open(os.path.join(WEB, 'data', 'products.json'), encoding='utf-8'))
for p in prods['products']:
    if p['id'] == 'ext-l1': p.update(status='available', price_cents={'soft': 800, 'physical': 1550})
    if p['id'] == 'ext-l2': p.update(price_cents=1000)                          # price set but coming-soon: must stay hidden
    if p['id'] == 'ext-l3': p.update(status='available')                        # available without a price: treated as coming soon
pf = os.path.join(TMP, 'products.json'); json.dump(prods, open(pf, 'w'))
products, warns = shop_build.load(pf)
frag = os.path.join(TMP, 'shop.html'); open(frag, 'w', encoding='utf-8').write(shop_build.render(products, warns))
os.makedirs(os.path.join(TMP, 'site', 'shop'))
open(os.path.join(TMP, 'site', 'shop', 'index.html'), 'w', encoding='utf-8').write(build_site.wrap(frag, 'Shop', 'x', 'shop/index.html'))
for f in ('cart.js', 'shop.js', 'checkout.js', 'mi.png'): shutil.copy(os.path.join(WEB, 'shop', f), os.path.join(TMP, 'site', 'shop', f))
srv2, BASE2 = serve(os.path.join(TMP, 'site'))

fails, errors = [], []
def check(name, fn):
    try: fn(); print('ok  ', name)
    except Exception as e: fails.append(name); print('FAIL', name, '\n    ', str(e)[:600])

def fill_valid(p, **kw):
    p.fill('#nfName', kw.get('name', 'Mei')); p.fill('#nfWa', kw.get('wa', '9123 4567')); p.check('#nfConsent')

def add(p, pid, fmt): p.locator('.addbtn[data-add="%s"][data-format="%s"]' % (pid, fmt)).click()
def cart(p): return p.evaluate("JSON.parse(localStorage.getItem('mi_cart_v1')||'{\"items\":[]}').items")

with sync_playwright() as pw:
    b = pw.chromium.launch()
    def ctx(w=1280, portal=False, scheme='light', base=None):
        c = b.new_context(viewport={'width': w, 'height': 900}, color_scheme=scheme); c.set_default_timeout(8000)
        if portal: c.add_init_script("window.MI_CONFIG={SUPABASE_URL:'https://mock.supabase.co',ANON_KEY:'mock-anon-key'};")
        return c
    def page(c):
        p = c.new_page(); p.on('pageerror', lambda e: errors.append(str(e))); return p

    # ---- no prices while everything is coming soon ----
    c = ctx(); p = page(c); p.goto(BASE + '/shop/')
    def no_price():
        expect(p.locator('.pcard2')).to_have_count(6)
        expect(p.locator('.pcard2 .pill')).to_have_text(['Coming soon'] * 6)
        body = p.inner_text('body'); assert 'S$' not in body and '$' not in body, 'a price is visible'
        html_src = p.content()
        assert re.search(r'S\$\s*\d', html_src) is None, 'price text in the source'
        assert '"prices"' not in html_src and 'price_cents' not in html_src, 'price data embedded'
        assert 'noindex' in html_src, 'private preview robots meta missing'
    check('shop page: 6 coming-soon cards, no price anywhere', no_price)
    def checkout_hidden():
        expect(p.locator('#checkoutBtn')).to_be_hidden(); assert p.locator('#checkoutBtn').is_disabled()
        expect(p.locator('#notifyBtn')).to_be_hidden()
        expect(p.locator('#listBody')).to_contain_text('Nothing on your list yet')
    check('checkout button hidden/disabled and notify hidden with an empty list', checkout_hidden)
    def labels():
        expect(p.locator('.addbtn').first).to_have_text('Add to your list'); expect(p.locator('#lh')).to_have_text('Your list')
        assert p.locator('.addbtn').count() == 12, p.locator('.addbtn').count()
    check("cards say 'Add to your list'; panel is 'Your list'", labels)

    # ---- cart: add, remove, quantity, persist, badge across the site ----
    def add_remove():
        add(p, 'ext-l1', 'soft'); add(p, 'ext-l3', 'physical')
        expect(p.locator('#soonList .lline')).to_have_count(2)
        assert cart(p) == [{'p': 'ext-l1', 'f': 'soft', 'q': 1}, {'p': 'ext-l3', 'f': 'physical', 'q': 1}], cart(p)
        expect(p.locator('.addbtn[data-add="ext-l1"][data-format="soft"]')).to_have_attribute('aria-pressed', 'true')
        expect(p.locator('.addbtn[data-add="ext-l1"][data-format="soft"]')).to_contain_text('On your list')
        expect(p.locator('.addbtn[data-add="ext-l1"][data-format="physical"]')).to_have_attribute('aria-pressed', 'false')
        expect(p.locator('#notifyBtn')).to_be_visible(); expect(p.locator('#checkoutBtn')).to_be_hidden()
        expect(p.locator('nav [data-cartn]')).to_have_text('2')
        p.locator('.addbtn[data-add="ext-l1"][data-format="soft"]').click()          # toggles off
        assert [x['p'] + x['f'] for x in cart(p)] == ['ext-l3physical']
        add(p, 'ext-l1', 'physical')                                                  # same product, other format = its own line
        assert len(cart(p)) == 2
        p.locator('[data-line="ext-l1|physical"] [data-remove]').click()
        assert len(cart(p)) == 1
    check('add / remove per product and format (toggle on the card, Remove in the list)', add_remove)
    def qty():
        line = p.locator('[data-line="ext-l3|physical"]')
        expect(line.locator('output')).to_have_text('1'); assert line.locator('[data-qty="-1"]').is_disabled()
        line.locator('[data-qty="1"]').click(); line.locator('[data-qty="1"]').click(); expect(line.locator('output')).to_have_text('3')
        assert cart(p)[0]['q'] == 3; expect(p.locator('nav [data-cartn]')).to_have_text('3')
        line.locator('[data-qty="-1"]').click(); expect(line.locator('output')).to_have_text('2')
        for _ in range(12): line.locator('[data-qty="1"]').click() if not line.locator('[data-qty="1"]').is_disabled() else None
        expect(line.locator('output')).to_have_text('10')
        add(p, 'ext-l2', 'soft'); expect(p.locator('[data-line="ext-l2|soft"] output')).to_have_count(0)    # soft copies have no quantity
        p.locator('[data-line="ext-l2|soft"] [data-remove]').click()
        for _ in range(9): line.locator('[data-qty="-1"]').click()
        expect(line.locator('output')).to_have_text('1')
    check('physical copies have a quantity (1 to 10); soft copies do not', qty)
    def persist():
        p.reload(); expect(p.locator('#soonList .lline')).to_have_count(1)
        expect(p.locator('.addbtn[data-add="ext-l3"][data-format="physical"]')).to_have_attribute('aria-pressed', 'true')
        p.goto(BASE + '/'); expect(p.locator('header [data-cartn]')).to_have_text('1')
        p.goto(BASE + '/ages-8-10/'); expect(p.locator('header [data-cartn]')).to_have_text('1')
        assert p.locator('header a[data-shoplink]').get_attribute('href') == '/shop/'
        p.goto(BASE + '/shop/')
    check('the list is remembered across reloads and shown in the nav on other pages', persist)
    def bad_storage():
        c2 = ctx(); q = page(c2)
        q.add_init_script("localStorage.setItem('mi_cart_v1','{not json')"); q.goto(BASE + '/shop/')
        expect(q.locator('#listBody')).to_contain_text('Nothing on your list yet'); add(q, 'ext-l4', 'soft'); expect(q.locator('#soonList .lline')).to_have_count(1)
        q.add_init_script("localStorage.setItem('mi_cart_v1', JSON.stringify({v:1,items:[{p:'ext-l9',f:'soft',q:1},{p:'x',f:'bogus',q:1},{p:'ext-l2',f:'physical',q:99}]}))")
        q.reload(); expect(q.locator('#soonList .lline')).to_have_count(1); expect(q.locator('[data-line="ext-l2|physical"] output')).to_have_text('10')   # unknown product / format dropped, qty clamped to 10
        c2.close()
        c3 = ctx(); r = page(c3)   # storage that throws on every use: page still works for this visit
        r.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('blocked')}})"); r.goto(BASE + '/shop/')
        add(r, 'ext-l5', 'soft'); expect(r.locator('#soonList .lline')).to_have_count(1); c3.close()
    check('corrupt or blocked localStorage does not break the page', bad_storage)
    def anchors():
        q = page(c); q.goto(BASE + '/shop/#level-4'); expect(q.locator('#level-4')).to_be_visible(); assert q.evaluate("document.querySelector('#level-4').getBoundingClientRect().top") < 400; q.close()
        for n, slug in ((1, 'ages-6-8'), (6, 'ages-11-13')):
            q = page(c); q.goto(BASE + '/%s/' % slug)
            t = q.locator('#extension'); expect(t).to_contain_text('Extension workbooks coming soon'); assert t.locator('a').get_attribute('href') == '/shop/#level-%d' % n; q.close()
        q = page(c); q.goto(BASE + '/'); expect(q.locator('header a[data-shoplink]')).to_be_visible(); expect(q.locator('footer a[href="/shop/"]')).to_have_count(1); q.close()
    check('#level-N anchors, level-page teasers and home nav/footer links', anchors)

    # ---- form validation ----
    def validation():
        p.click('#notifyBtn'); expect(p.locator('#notify')).to_be_visible(); p.click('#nfSubmit')
        for t in ['add your first name', 'Give a WhatsApp number or an email', 'Please tick the box']:
            expect(p.locator('#nfForm')).to_contain_text(t)
        p.locator('input[name=nfitem]').evaluate_all('e=>e.forEach(x=>x.checked=false)'); p.click('#nfSubmit'); expect(p.locator('#nfForm')).to_contain_text('Tick at least one workbook')
        p.locator('input[name=nfitem]').evaluate_all('e=>e.forEach(x=>x.checked=true)'); p.fill('#nfName', 'Mei'); p.fill('#nfEmail', 'nope'); p.check('#nfConsent'); p.click('#nfSubmit')
        expect(p.locator('#nfForm')).to_contain_text('does not look right')
        p.fill('#nfEmail', ''); p.fill('#nfWa', '12'); p.click('#nfSubmit'); expect(p.locator('#nfForm')).to_contain_text('8 or more digits')
        assert p.locator('#nfWaLink').count() == 0, 'nothing may be sent while invalid'
        expect(p.locator('#nfForm')).to_contain_text('only to tell me when those products are ready'); expect(p.locator('#nfForm')).to_contain_text('12 months')
    check('validation: items, name, contact, email, phone, consent; PDPA wording on the form', validation)

    # ---- WhatsApp fallback ----
    def wa():
        p.goto(BASE + '/shop/'); add(p, 'ext-l1', 'soft'); add(p, 'ext-l3', 'physical'); p.locator('[data-line="ext-l3|physical"] [data-qty="1"]').click()
        p.click('#notifyBtn'); expect(p.locator('#nfModeNote')).to_contain_text('+65 9880 5962')
        fill_valid(p); p.fill('#nfNote', 'For my son'); p.click('#nfSubmit')
        href = p.locator('#nfWaLink').get_attribute('href'); assert href.startswith('https://wa.me/6598805962?text='), href
        txt = unquote(href.split('text=')[1])
        for s in ['Please tell me when these Math Inquirers products are ready', '- Extension Workbook, Level 1 (ages 6-8): soft copy', '- Extension Workbook, Level 3 (ages 8-10): physical copy x2',
                  'Parent: Mei', 'Contact: WhatsApp 9123 4567', 'Note: For my son', 'not an order']:
            assert s in txt, (s, txt)
        assert 'S$' not in txt and '$' not in txt
        expect(p.locator('#nfPre')).to_contain_text('Hi! Please tell me')
        assert len(cart(p)) == 2, 'list kept until the message is actually sent'
    check('WhatsApp fallback: prefilled message to +65 9880 5962 lists the items readably', wa)
    def throttle():
        p.reload(); p.click('#notifyBtn'); fill_valid(p, wa='8111 2222'); p.click('#nfSubmit'); expect(p.locator('#nfMsg')).to_contain_text('wait a minute')
    check('client-side 1-minute throttle', throttle)
    def honeypot():
        c2 = ctx(); q = page(c2); q.goto(BASE + '/shop/'); add(q, 'ext-l1', 'soft'); q.click('#notifyBtn'); fill_valid(q)
        q.evaluate("document.getElementById('nfHp').value='http://spam'"); q.click('#nfSubmit'); expect(q.locator('#nfWaLink')).to_have_count(0); c2.close()
    check('honeypot filled => nothing happens', honeypot)
    def phone_fit():
        for w in (400, 360):
            c3 = ctx(w); q = page(c3); q.goto(BASE + '/shop/'); add(q, 'ext-l1', 'soft'); add(q, 'ext-l2', 'physical'); q.click('#notifyBtn')
            assert q.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth') <= 0, w
            for h_ in q.locator('.addbtn:visible, #nfSubmit, .qty button:visible, [data-remove]:visible').evaluate_all('e=>e.map(x=>x.getBoundingClientRect().height)'): assert h_ >= 40, (w, h_)
            c3.close()
    check('no horizontal scroll at 400 and 360 px; tap targets >= 40px', phone_fit)
    c.close()

    # ---- portal mode (RPC mocked) ----
    c = ctx(portal=True); p = page(c); calls = []
    def route(r):
        req = r.request
        if req.method == 'OPTIONS': return r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'})
        calls.append((req.url, req.headers, json.loads(req.post_data)))
        body = resp[0]; r.fulfill(status=body[0], content_type='application/json', headers={'access-control-allow-origin': '*'}, body=json.dumps(body[1]))
    resp = [(200, {'ok': True, 'status': 'received'})]
    c.route('https://mock.supabase.co/**', route)
    p.goto(BASE + '/shop/')
    def setup():
        p.evaluate("localStorage.clear()"); p.reload(); add(p, 'ext-l2', 'soft'); add(p, 'ext-l5', 'physical'); p.locator('[data-line="ext-l5|physical"] [data-qty="1"]').click()
        p.click('#notifyBtn'); fill_valid(p, wa='+65 9123 4567')
    def portal_ok():
        setup(); p.click('#nfSubmit')
        expect(p.locator('#nfMsg')).to_contain_text('Thank you. We have your request'); assert len(calls) == 1
        url, hdr, body = calls[0]
        assert url == 'https://mock.supabase.co/rest/v1/rpc/submit_product_interest', url
        assert hdr['apikey'] == 'mock-anon-key' and hdr['authorization'] == 'Bearer mock-anon-key'
        assert body['p_items'] == [{'product': 'ext-l2', 'format': 'soft', 'qty': 1}, {'product': 'ext-l5', 'format': 'physical', 'qty': 2}], body['p_items']
        assert body['p_first_name'] == 'Mei' and body['p_whatsapp'] == '91234567' and body['p_email'] is None and body['p_consent'] is True and body['p_consent_version'] and body['p_hp'] is None
        assert set(body) == {'p_first_name', 'p_whatsapp', 'p_email', 'p_items', 'p_note', 'p_consent', 'p_consent_version', 'p_hp'}, set(body)
        assert 'price' not in json.dumps(body)
        expect(p.locator('#nfModeNote')).to_contain_text('stored securely')
        assert cart(p) == [], 'sent items leave the list'
    check('portal mode calls submit_product_interest with the anon key and {product,format,qty} items', portal_ok)
    def portal_dupe():
        p.evaluate("localStorage.clear()"); resp[0] = (200, {'ok': True, 'status': 'already_received'}); p.reload(); setup(); p.click('#nfSubmit')
        expect(p.locator('#nfMsg')).to_contain_text('already have a request')
    check('portal duplicate-day response is shown kindly', portal_dupe)
    def portal_fail():
        p.evaluate("localStorage.clear()"); resp[0] = (500, {'message': 'boom'}); p.reload(); setup(); p.click('#nfSubmit')
        expect(p.locator('#nfWaLink')).to_have_attribute('href', re.compile(r'^https://wa\.me/6598805962')); expect(p.locator('#nfMsg')).to_contain_text('send it to us on WhatsApp instead')
    check('portal error falls back to WhatsApp', portal_fail)
    def portal_invalid():
        p.evaluate("localStorage.clear()"); resp[0] = (400, {'message': 'invalid_input'}); p.reload(); setup(); p.click('#nfSubmit')
        expect(p.locator('#nfMsg')).to_contain_text('not accepted')
    check('portal invalid_input shows a message', portal_invalid)
    c.close()

    # ---- price rule against a temporary products file ----
    c = ctx(); p = page(c); p.goto(BASE2 + '/shop/')
    def price_rule():
        assert any('ext-l2' in w and 'hidden' in w for w in warns) and any('ext-l1' in w and 'PRICE WILL BE SHOWN' in w for w in warns), warns
        assert any('ext-l3' in w and 'no price' in w for w in warns), warns
        c1 = p.locator('#level-1'); expect(c1).to_contain_text('Available'); expect(c1.locator('.fmt[data-format=soft] .fprice')).to_have_text('S$8')
        expect(c1.locator('.fmt[data-format=physical] .fprice')).to_have_text('S$15.50'); expect(c1.locator('.addbtn').first).to_have_text('Add to cart')
        for n in (2, 3, 4, 5, 6):
            t = p.locator('#level-%d' % n); expect(t).to_contain_text('Coming soon'); assert 'S$' not in t.inner_text(), (n, t.inner_text())
        src = p.content(); assert '1000' not in src and 'price_cents' not in src, 'hidden price leaked into the page'
    check('price shown only when status is available AND a price is set (temp products file)', price_rule)
    def ready_cart():
        add(p, 'ext-l1', 'soft'); add(p, 'ext-l1', 'physical'); add(p, 'ext-l2', 'soft')
        p.locator('[data-line="ext-l1|physical"] [data-qty="1"]').click()
        expect(p.locator('#readyList .lline')).to_have_count(2); expect(p.locator('#soonList .lline')).to_have_count(1)
        expect(p.locator('#listTotal')).to_have_text('S$39'); expect(p.locator('[data-line="ext-l1|physical"]')).to_contain_text('S$31')       # 2 x 15.50
        expect(p.locator('#checkoutBtn')).to_be_visible(); assert p.locator('#checkoutBtn').is_disabled(), 'stays disabled until the Stripe function is wired'
        expect(p.locator('#notifyBtn')).to_be_visible()
    check('available items go in "Ready to order" with a total; coming-soon items stay on the notify list; checkout visible but disabled', ready_cart)
    def stub():
        r = p.evaluate("MiCheckout.start({items:[{product:'ext-l1',format:'soft',qty:1}]}).then(()=>'resolved',e=>e.error)"); assert r == 'not_enabled', r
        v = p.evaluate("MiCheckout.validate({items:[{product:'ext-l1',format:'soft',qty:1},{product:'ext-l1',format:'physical',qty:1}],contact:{email:'x'},shipping:{line1:'1 Road',postal_code:'12'}})")
        assert sorted(x['field'] for x in v) == ['email', 'ship_name', 'ship_postal'], v
        ok = p.evaluate("MiCheckout.validate({items:[{product:'ext-l1',format:'physical',qty:1}],contact:{},shipping:{name:'Mei',line1:'1 Road #01-01',postal_code:'123 456'}})"); assert ok == [], ok
        assert p.evaluate("MiCheckout.ENDPOINT") == '/api/shop/checkout'
    check('checkout stub: not_enabled, Singapore address + email rules documented in validate()', stub)
    c.close()

    # ---- no-JS ----
    c = b.new_context(java_script_enabled=False, viewport={'width': 1280, 'height': 900}); q = c.new_page(); q.goto(BASE + '/shop/')
    check('no-JS: cards still show, add buttons stay hidden, WhatsApp note shown', lambda: (expect(q.locator('.pcard2')).to_have_count(6), expect(q.locator('.addbtn:visible')).to_have_count(0), expect(q.locator('#yourlist')).to_contain_text('+65 9880 5962')))
    c.close()

    # ---- screenshots ----
    if SHOTS:
        os.makedirs(SHOTS, exist_ok=True)
        for scheme in ('light', 'dark'):
            for w in (1280, 400):
                c = ctx(w, scheme=scheme); q = page(c); q.goto(BASE + '/shop/'); q.wait_for_timeout(300)
                tag = '%s_%d' % (scheme, w)
                q.screenshot(path=os.path.join(SHOTS, 'shop_%s_page.png' % tag), full_page=True)
                add(q, 'ext-l1', 'soft'); add(q, 'ext-l3', 'physical'); q.locator('[data-line="ext-l3|physical"] [data-qty="1"]').click(); add(q, 'ext-l6', 'soft'); q.wait_for_timeout(200)
                q.locator('#yourlist').screenshot(path=os.path.join(SHOTS, 'shop_%s_cart.png' % tag))
                q.click('#notifyBtn'); q.wait_for_timeout(600); q.click('#nfSubmit'); q.wait_for_timeout(200)
                q.locator('#notify').screenshot(path=os.path.join(SHOTS, 'shop_%s_form_errors.png' % tag))
                fill_valid(q); q.fill('#nfEmail', 'mei@example.com'); q.click('#nfSubmit'); q.wait_for_timeout(300)
                q.locator('#notify').screenshot(path=os.path.join(SHOTS, 'shop_%s_form_whatsapp.png' % tag))
                q.goto(BASE + '/ages-8-10/'); q.locator('#extension').scroll_into_view_if_needed()
                q.locator('#extension').screenshot(path=os.path.join(SHOTS, 'shop_%s_levelpage_teaser.png' % tag))
                print(tag, 'horizontal overflow px:', q.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth'))
                c.close()
    b.close()
shutil.rmtree(TMP, ignore_errors=True)
if errors: print('page errors:', errors); fails.append('page errors')
print('SHOP FAILED' if fails else 'SHOP ALL PASSED'); sys.exit(1 if fails else 0)
