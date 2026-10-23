#!/usr/bin/env python3
"""Generate the shop page source (website/shop/shop.html) from data/products.json. build_site.py then wraps it as /shop/ and copies
shop/cart.js, shop/shop.js, shop/checkout.js and shop/mi.png next to it.

    python3 shop_build.py [--products path/to/products.json] [--out path/to/shop.html]

PRICE RULE (owner, 23 Oct 2026: prices are on hold, nothing may show a price): a price is shown ONLY when a product has status 'available'
AND price_cents is set. Everything else renders as 'Coming soon' with no price. The builder warns about every price_cents it finds.
The browser never decides this: only products that pass the rule carry prices in the data embedded in the page.
"""
import html
import json
import os
import re
import sys

import interest_ui
from level_pages import LEVELS

HERE = os.path.dirname(os.path.abspath(__file__))
PRODUCTS = os.path.join(HERE, 'data', 'products.json')
OUT = os.path.join(HERE, 'shop', 'shop.html')
FORMATS = ('soft', 'physical')
FORMAT_LABEL = {'soft': 'Soft copy', 'physical': 'Physical copy'}
FORMAT_NOTE = {'soft': 'PDF download, sent by email', 'physical': 'Printed and posted to a Singapore address'}
STATUSES = ('coming-soon', 'available')
COVER_BG = ['#FFF0C4', '#D6E9FB', '#D3F1E4', '#FFE2D6', '#E6DFFB', '#FFC93C']
WA_NUM, WA_SHOW = '6598805962', '+65 9880 5962'   # same business WhatsApp as lp_build.py


def esc(s):
    return html.escape(str(s), quote=True)


def money(cents):
    return 'S$%d' % (cents // 100) if cents % 100 == 0 else 'S$%d.%02d' % (cents // 100, cents % 100)


def load(path=PRODUCTS):
    """Validated products with an effective status and the prices that may be shown. Returns (products, warnings)."""
    d = json.load(open(path, encoding='utf-8'))
    out, warns, seen = [], [], set()
    for p in d['products']:
        pid = p['id']
        assert re.fullmatch(r'[a-z0-9-]{1,24}', pid), 'product id %r' % pid
        assert pid not in seen, 'duplicate product id ' + pid
        seen.add(pid)
        assert p['level'] in range(1, 7), 'level of ' + pid
        fm = list(p.get('formats') or [])
        assert fm and all(f in FORMATS for f in fm), 'formats of ' + pid
        assert p.get('status', 'coming-soon') in STATUSES, 'status of ' + pid
        raw = p.get('price_cents')
        prices = {}
        if raw is not None:
            if isinstance(raw, dict):
                prices = {f: int(raw[f]) for f in fm if f in raw}
            else:
                prices = {f: int(raw) for f in fm}
            assert all(v > 0 for v in prices.values()), 'price of %s must be a positive number of cents' % pid
        status = p.get('status', 'coming-soon')
        shown = {}
        if status == 'available':
            if all(f in prices for f in fm):
                shown = prices
            else:
                warns.append('%s is status "available" but has no price for every format: shown as coming soon until price_cents is set' % pid)
                status = 'coming-soon'
        elif prices:
            pass
        if raw is not None:
            warns.append('%s has price_cents set (%s): %s' % (pid, json.dumps(raw), 'PRICE WILL BE SHOWN on /shop/' if shown else 'hidden, status is %s' % p.get('status', 'coming-soon')))
        q = dict(p); q['status'] = status; q['shown_prices'] = shown
        out.append(q)
    return out, warns


def cover(p):
    n = p['level']
    return ('<div class="cover" style="background:%s" aria-hidden="true"><span class="cl">Level</span><span class="cn">%d</span><span class="cx">Extension</span></div>'
            % (COVER_BG[(n - 1) % len(COVER_BG)], n))


def card(p):
    n = p['level']
    avail = p['status'] == 'available'
    rows = ''
    for f in p['formats']:
        pr = p['shown_prices'].get(f)
        rows += ('<div class="fmt" data-format="%s"><div class="ft"><b>%s</b><span class="small muted">%s</span></div>%s'
                 '<button type="button" class="btn sm alt addbtn" data-add="%s" data-format="%s" aria-pressed="false" hidden>%s</button></div>'
                 % (f, FORMAT_LABEL[f], FORMAT_NOTE[f], ('<span class="fprice">%s</span>' % money(pr)) if pr else '',
                    esc(p['id']), f, 'Add to cart' if avail else 'Add to your list'))
    return ('<article class="pcard2" id="level-%d" data-product="%s" data-status="%s">%s<div class="pbody">'
            '<div class="row" style="gap:8px"><span class="pill %s">%s</span><span class="small muted">Ages %s</span></div>'
            '<h3>%s</h3><p class="small">%s</p><div class="fmts">%s</div></div></article>'
            % (n, esc(p['id']), p['status'], cover(p), 'p-ok' if avail else 'p-wait', 'Available' if avail else 'Coming soon',
               esc(p.get('ages') or interest_ui.LEVEL_AGES[n]), esc(p['name']), esc(p['description']), rows))


CSS = '''
[hidden]{display:none!important}
.shophero{grid-template-columns:1.3fr 1fr}
.miwrap{justify-self:center;display:grid;justify-items:center;gap:6px;background:#D6E9FB;border:2.5px solid #1B2A49;border-radius:26px;padding:14px 20px 8px;box-shadow:5px 5px 0 #1B2A49;color:#1B2A49;max-width:220px}
.miwrap img{display:block;height:150px;width:auto}
.miwrap span{font:600 17px var(--head)}
.shoplay{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:26px;align-items:start}
.pgrid{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.pcard2{display:grid;grid-template-columns:84px minmax(0,1fr);gap:14px;align-content:start;background:var(--card);border:2.5px solid var(--ink);border-radius:22px;padding:16px;box-shadow:5px 5px 0 var(--ink);scroll-margin-top:16px}
.pcard2:target{outline:3px solid var(--coral);outline-offset:3px}
.pbody{display:grid;gap:8px;align-content:start;min-width:0}
.pbody h3{font-size:21px}
.cover{width:84px;height:112px;border:2.5px solid #1B2A49;border-left-width:9px;border-radius:6px 12px 12px 6px;box-shadow:3px 3px 0 #1B2A49;color:#1B2A49;display:grid;align-content:center;justify-items:center;text-align:center;gap:0;font-family:var(--head)}
.cover .cl{font-size:12px;text-transform:uppercase;letter-spacing:.08em;font-weight:600}
.cover .cn{font-size:40px;line-height:1;font-weight:600}
.cover .cx{font-size:11px;font-weight:600;margin-top:6px;border-top:2px solid #1B2A49;padding-top:3px}
.fmts{display:grid;gap:8px;margin-top:2px}
.fmt{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 10px;align-items:center;border:2px dashed var(--line);border-radius:14px;padding:8px 10px;background:var(--bg)}
.fmt .ft{display:grid;gap:0;min-width:0}
.fmt .fprice{font:600 18px var(--head);grid-column:1/-1}
.fmt .addbtn{grid-column:1/-1;justify-self:start;min-height:44px}
.addbtn[aria-pressed="true"]{background:var(--mint);color:var(--fg)}
.listbox{position:sticky;top:14px;display:grid;gap:12px;background:var(--card);border:2.5px solid var(--ink);border-radius:22px;padding:18px;box-shadow:6px 6px 0 var(--ink)}
.listbox h2{font-size:26px}
.listbox ul{list-style:none;padding:0;margin:0;display:grid;gap:8px}
.listbox h3{font-size:16px}
.lline{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:6px 10px;align-items:center;border:2px solid var(--line);border-radius:14px;padding:8px 10px;background:var(--bg)}
.lline .lname{min-width:0}
.lline .lact{display:flex;gap:8px;align-items:center;grid-column:1/-1;flex-wrap:wrap}
.qty{display:inline-flex;align-items:center;gap:2px;border:2px solid var(--ink);border-radius:12px;background:var(--card)}
.qty button{font:800 18px var(--body);width:44px;height:44px;border:0;background:none;color:var(--fg);cursor:pointer;border-radius:10px}
.qty button:disabled{opacity:.35;cursor:not-allowed}
.qty output{min-width:28px;text-align:center;font-weight:800}
.linkbtn2{font:700 14px var(--body);color:var(--teal);background:none;border:0;padding:0 6px;min-height:44px;cursor:pointer;text-decoration:underline}
.listbox .btn{min-height:44px;text-align:center}
.listbox .total{display:flex;justify-content:space-between;font-weight:800;border-top:1.5px solid var(--line);padding-top:8px}
.listbar{position:fixed;left:0;right:0;bottom:0;z-index:5;display:none;justify-content:center;padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));background:var(--card);border-top:2.5px solid var(--ink)}
.listbar a{text-decoration:none}
#notify[hidden]{display:none}
#notify .items{display:grid;gap:8px;margin-bottom:12px}
#notify .items label{display:flex;gap:10px;align-items:center;min-height:44px;border:2px solid var(--line);border-radius:12px;padding:6px 12px;background:var(--bg);font-weight:700;cursor:pointer}
#notify .items label:has(input:checked){background:var(--mint);border-color:var(--ink)}
#notify .items input{width:20px;height:20px;flex:none;margin:0;accent-color:var(--teal)}
#notify.band{grid-template-columns:1fr}
.waout{display:grid;gap:10px}
.waout pre{white-space:pre-wrap;background:var(--bg);border:2px dashed var(--line);border-radius:12px;padding:12px;font:14px/1.5 var(--body);margin:0}
@media (max-width:980px){.shoplay{grid-template-columns:1fr}.listbox{position:static}.shophero{grid-template-columns:1fr}}
@media (max-width:700px){.pgrid{grid-template-columns:1fr}.listbar.on{display:flex}main{padding-bottom:84px}}
@media (max-width:420px){.pcard2{grid-template-columns:64px minmax(0,1fr);padding:14px}.cover{width:64px;height:88px}.cover .cn{font-size:30px}.cover .cx{font-size:9px}.grid2{grid-template-columns:1fr}.miwrap img{height:110px}}
'''

NAV = ('<a class="tab" href="/#program" style="text-decoration:none">Program</a><a class="tab" href="/#classes" style="text-decoration:none">Classes</a>'
       '<a class="tab" href="/#levels" style="text-decoration:none">Levels</a><a class="tab" href="/#price" style="text-decoration:none">Price</a>'
       '<a class="tab" href="/#faq" style="text-decoration:none">FAQ</a>'
       '<a class="tab" href="/shop/" style="text-decoration:none" aria-current="true" data-shoplink>Shop<span class="cartn" data-cartn hidden></span></a>'
       '<a class="btn yel sm" href="/#register" style="margin-left:6px;padding:8px 16px">Register</a>')

CONSENT = ('I agree that Math Inquirers (Preciouslyours Pte Ltd) may keep my first name, my contact details and the items I choose, '
           '<b>only to tell me when those products are ready</b>. We keep this for <b>12 months</b> and then delete it. '
           'No marketing beyond that product notice. You can ask us to delete it sooner. See the <a href="/privacy/" target="_blank">privacy notice</a>.')


def render(products, warns=()):
    p_json = []
    for p in products:
        e = {'id': p['id'], 'level': p['level'], 'name': p['name'], 'ages': p.get('ages') or interest_ui.LEVEL_AGES[p['level']],
             'formats': p['formats'], 'status': p['status']}
        if p['shown_prices']:
            e['prices'] = p['shown_prices']   # ONLY present when status is available and a price is set
        p_json.append(e)
    shop = {'products': p_json, 'wa': WA_NUM, 'waShow': WA_SHOW, 'consent': interest_ui.CONSENT_VERSION, 'checkoutEnabled': False}
    cards = ''.join(card(p) for p in products)
    desc = 'Extension workbooks for Math Inquirers Levels 1 to 6, coming soon in soft copy and printed copy. Add what you want to your list and we will tell you when it is ready.'
    return '''<title>Shop: extension workbooks coming soon | Math Inquirers</title>
<meta name="description" content="%(desc)s">
<style>%(css)s</style>
<div class="wrap">
<header class="bar"><a class="brand" href="/" style="text-decoration:none"><i>?</i><span>Math Inquirers</span></a><nav class="nav" aria-label="Site">%(nav)s</nav></header>
<main id="top">
<p class="crumbs"><a href="/">Home</a> · Shop</p>
<section class="hero shophero"><div class="sec"><span class="eyebrow">Shop · Coming soon</span><h1>Extension <mark>workbooks</mark></h1><p class="slogan">Notice it. Test it. Explain why.</p>
<p class="lead">Extra-challenge puzzles with full answers, one workbook for each level, to try at home at your own pace.</p>
<div class="row" style="margin-top:6px"><a class="btn yel" href="#products">See the workbooks</a></div></div>
<div class="miwrap"><img src="/shop/mi.png" width="126" height="150" alt="Mi the dolphin waving hello"><span>Not ready yet!</span></div></section>

<div class="shoplay" id="products">
<section class="sec" aria-labelledby="ph"><div class="shead"><span class="eyebrow">Coming soon</span><h2 id="ph">One workbook for each level</h2>
<p class="muted">Each workbook has worked examples at the start, puzzles in the same style as the holiday program for its level, and full answers with short explanations. Choose a <b>soft copy</b> (a PDF sent to your email) or a <b>physical copy</b> (printed and posted to a Singapore address). They are <b>not on sale yet</b>: add the ones you want to your list and we will tell you when they are ready. Nothing is reserved or charged.</p></div>
<div class="pgrid">%(cards)s</div></section>

<aside class="listbox" id="yourlist" aria-labelledby="lh" aria-live="polite"><h2 id="lh">Your list</h2>
<noscript><div class="msg info">The list needs JavaScript. Without it, message us on WhatsApp at <a href="https://wa.me/%(wa)s">%(waShow)s</a> and tell us which workbook and which copy you would like.</div></noscript>
<div id="listBody"><p class="muted small" id="listEmpty">Nothing on your list yet. Tap <b>Add to your list</b> on a workbook.</p></div>
<div class="row" style="flex-direction:column;align-items:stretch;gap:8px">
<button type="button" class="btn yel" id="notifyBtn" hidden>Tell me when it's ready</button>
<button type="button" class="btn" id="checkoutBtn" hidden disabled>Checkout</button></div>
<div id="listMsg"></div>
<p class="small muted" id="listNote">Your list is kept in this browser only, so it is still here when you come back or visit other pages.</p></aside>
</div>

<section class="band peach" id="notify" hidden><div class="sec"><span class="eyebrow">Tell me when it's ready</span><h2>We will message you</h2>
<p class="muted">Tell us where to reach you. We message you <b>once</b>, when the workbooks on your list are ready. <b>This is not an order</b>: nothing is reserved and nothing is charged.</p></div>
<form class="card" id="nfForm" novalidate autocomplete="off">
<fieldset class="field" style="border:0;padding:0;margin:0 0 12px"><legend class="flabel">Tell me when these are ready <span class="muted" style="font-weight:600">(untick any you do not want)</span></legend><div class="items" id="nfItems"></div></fieldset>
<div class="grid2"><div class="field"><label for="nfName">Your first name</label><input id="nfName" name="name" maxlength="40" autocomplete="given-name" required></div>
<div class="field"><label for="nfNote">Anything else? <span class="muted" style="font-weight:600">(optional)</span></label><input id="nfNote" name="note" maxlength="400"></div></div>
<div class="grid2"><div class="field"><label for="nfWa">WhatsApp number</label><input id="nfWa" name="wa" type="tel" inputmode="tel" autocomplete="tel" placeholder="9123 4567"></div>
<div class="field"><label for="nfEmail">or email</label><input id="nfEmail" name="email" type="email" autocomplete="email" maxlength="120"></div></div>
<p class="fine2" style="margin:-4px 0 12px">Give at least one, so we can reach you. Please do not give your child's name.</p>
<div class="hp" aria-hidden="true"><label>Leave this empty<input id="nfHp" name="company_website" tabindex="-1" autocomplete="off"></label></div>
<label class="check" for="nfConsent"><input type="checkbox" id="nfConsent" name="consent"><span>%(consent)s</span></label>
<div id="nfMsg" aria-live="polite"></div>
<button class="btn" type="submit" id="nfSubmit">Tell me when it's ready</button>
<p class="fine2" style="margin-top:10px" id="nfModeNote"></p></form></section>
</main>
<div class="listbar" id="listBar"><a class="btn yel" href="#yourlist">Your list <span class="cartn" id="listBarN"></span></a></div>
<footer><div><b>Math Inquirers</b><p style="margin-top:6px">An independent maths enrichment program by Preciouslyours Pte Ltd, Singapore. Not affiliated with MOE or the Gifted Education Programme. We do not identify or test for giftedness and we do not promise exam or competition results.</p></div><div><b>Contact</b><p style="margin-top:6px">WhatsApp: %(waShow)s<br><a href="/">Back to the home page</a></p></div><div><b>Your details</b><p style="margin-top:6px">We use your details only to tell you when a product is ready, in line with the PDPA. <a href="/terms/">Terms</a> · <a href="/privacy/">Privacy</a></p></div></footer>
</div>
<!--PORTAL_CONFIG-->
<script>window.MI_SHOP=%(shop)s;</script>
<script src="/shop/cart.js" defer></script>
<script src="/shop/checkout.js" defer></script>
<script src="/shop/shop.js" defer></script>
''' % dict(desc=esc(desc), css=open(os.path.join(HERE, 'lp_parts.txt'), encoding='utf-8').read() + _level_css() + interest_ui.CSS + CSS, nav=NAV,
           cards=cards, wa=WA_NUM, waShow=esc(WA_SHOW), consent=CONSENT, shop=json.dumps(shop).replace('</', '<\\/'))


def _level_css():
    from level_pages import LEVEL_CSS, PAGE_CSS
    return LEVEL_CSS + PAGE_CSS


def main():
    path = sys.argv[sys.argv.index('--products') + 1] if '--products' in sys.argv else PRODUCTS
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else OUT
    products, warns = load(path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(render(products, warns))
    print('wrote', out, '(%d products)' % len(products))
    for w in warns:
        print('WARNING (shop price):', w)
    return warns


if __name__ == '__main__':
    main()
