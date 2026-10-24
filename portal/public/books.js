/* Extension books: choose a level, how you want it (workbook only / online only / workbook + online), which child it is for, and (for a printed
   copy) a Singapore delivery address. Creates an order in "pending payment" with a PayNow reference (MI-XXXXXX), the same manual way as the
   enrolment payments. The price always comes from the database (ext_prices, set by the owner); this page never invents one. If a price is not
   set it says "price coming soon" and offers an "Ask us" button. One purchase is for ONE child. The card button stays hidden until
   PAYMENT_MODE is 'stripe'. Nothing here marks an order paid: only the owner can (admin page). */
(function () {
  var M = window.MI, h = M.h, P = M.P, app = document.getElementById('app'), S = P.state;
  document.getElementById('top').appendChild(M.header('Extension books'));
  var q = new URLSearchParams(location.search);
  var F = { level: 0, format: '', child: q.get('child') || '', name: '', address: '', postal: '', phone: '' };
  var D = { prices: {}, orders: [], access: [], missing: false, last: null, ticks: {} }, flashMsg = null, ready = false;
  function flash(kind, text) { flashMsg = text ? { kind: kind, text: text } : null; }
  // keep keyboard focus on the same control across a redraw (clearing the container would drop it to <body>)
  function draw(nodes) { var k = M.focusKey(app); M.clear(app); [].concat(nodes).forEach(function (n) { if (n) app.appendChild(n); }); M.focusRestore(app, k); }
  // after every action the result message (or the page heading) takes keyboard focus and is announced
  async function run(fn, ok) { flash(null); try { await fn(); if (ok) flash('ok', ok); } catch (e) { flash('err', M.errText(e)); } await refresh(); M.focusResult(app); }
  var FORMATS = ['workbook', 'online', 'both'];
  function sku() { return F.level && F.format ? 'ext-l' + F.level + '-' + F.format : ''; }
  function price() { var c = D.prices[sku()]; return c == null ? null : c; }
  function childById(id) { return S.children.filter(function (c) { return c.id === id; })[0]; }
  function hasOnline(childId, level) {
    return D.access.some(function (a) { return a.child_id === childId && a.kind === 'book' && a.level === level && (a.format === 'online' || a.format === 'both'); });
  }

  async function refresh() {
    try {
      await P.load();
      if (S.session) {
        var sb = M.sb(), res = await Promise.all([sb.rpc('list_ext_prices'), sb.from('ext_orders').select('*').order('created_at', { ascending: false }), sb.rpc('my_children_access')]);
        var bad = res.filter(function (x) { return x.error; })[0];
        if (bad) { if (P.isMissingSql(bad.error)) D.missing = true; else throw bad.error; }
        else {
          D.missing = false; D.prices = {}; (res[0].data || []).forEach(function (r) { D.prices[r.product_id] = r.amount_cents; });
          D.orders = res[1].data || []; D.access = res[2].data || [];
        }
        if (S.children.length === 1 && !childById(F.child)) F.child = S.children[0].id;
        if (!F.level && S.children.length) F.level = (childById(F.child) || S.children[0]).level;
      }
    } catch (e) { flash('err', M.errText(e)); }
    ready = true; paint();
  }

  function needTypes() {
    var t = ['contact', 'terms'];
    if (F.format && F.format !== 'workbook') t.push('online_practice');
    if (F.format && F.format !== 'online') t.push('book_delivery');
    return t;
  }

  function orderForm() {
    var form = h('form', { novalidate: true, id: 'order-form', onsubmit: submit });
    var asks = h('p', { class: 'small muted', text: 'Not sure about the price or which one to pick? Ask us and we will reply.' });
    // 1. level
    var lv = h('select', { id: 'book-level', onchange: function (e) { F.level = Number(e.target.value); paint(); } }, [1, 2, 3, 4, 5, 6].map(function (n) { return h('option', { value: n, selected: F.level === n }, 'Level ' + n); }));
    form.appendChild(h('fieldset', null, h('legend', { text: '1. Which level?' }), h('p', null, h('label', { for: 'book-level', text: 'Extension Workbook level' }), lv),
      h('p', { class: 'small muted', text: 'Ten units of extra problems for the level. The level of the book does not have to match your child\'s level.' })));
    // 2. option
    var opts = FORMATS.map(function (f) {
      var key = 'ext-l' + F.level + '-' + f, c = D.prices[key];
      return h('label', { class: 'opt' + (F.format === f ? ' on' : '') },
        h('input', { type: 'radio', name: 'book-format', value: f, id: 'fmt-' + f, checked: F.format === f, onchange: function () { F.format = f; paint(); var e = document.getElementById('fmt-' + f); if (e) e.focus(); } }),
        h('span', null, h('strong', { text: M.FORMATS[f] }), h('br'),
          c == null ? h('span', { class: 'small muted price', 'data-price-for': key, text: 'Price coming soon' }) : h('span', { class: 'price', 'data-price-for': key, text: M.money(c) })));
    });
    form.appendChild(h('fieldset', null, h('legend', { text: '2. How would you like it?' }), opts));
    // 3. child
    var kids = S.children.length ? S.children.map(function (c) {
      var blocked = F.format && F.format !== 'workbook' && hasOnline(c.id, F.level);
      return h('label', { class: 'opt' + (blocked ? ' full' : '') },
        h('input', { type: 'radio', name: 'book-child', value: c.id, id: 'kid-' + c.id, disabled: blocked, checked: F.child === c.id, onchange: function () { F.child = c.id; paint(); var e = document.getElementById('kid-' + c.id); if (e) e.focus(); } }),
        h('span', null, h('strong', { text: c.display_name }), ' ', h('span', { class: 'small muted', text: 'Level ' + c.level }), blocked ? h('span', { class: 'small', text: ' already has online access to this level' }) : null));
    }) : [h('p', { class: 'muted', text: 'Add your child first (below), then come back to choose.' })];
    form.appendChild(h('fieldset', null, h('legend', { text: '3. Which child is it for?' }), kids,
      h('p', { class: 'small muted', text: 'One purchase is for one child. Online access is set up for this child only; a brother or sister needs their own.' })));
    // 4. delivery
    if (F.format && F.format !== 'online') {
      form.appendChild(h('fieldset', { id: 'ship-box' }, h('legend', { text: '4. Where should we post it?' }),
        h('p', { class: 'small muted', text: 'Singapore addresses only. We use these details only to print and post your book, and delete them 30 days after it is delivered.' }),
        h('div', { class: 'grid2' },
          field('ship-name', 'Name for the parcel', 'name', { maxlength: 100, autocomplete: 'name' }),
          field('ship-phone', 'Phone (for the courier)', 'phone', { maxlength: 30, type: 'tel', autocomplete: 'tel' }),
          field('ship-address', 'Address (block, street, unit)', 'address', { maxlength: 200, autocomplete: 'street-address' }),
          field('ship-postal', 'Postal code (6 digits)', 'postal', { maxlength: 6, inputmode: 'numeric', autocomplete: 'postal-code' }))));
    }
    // 5. agreements
    var lines = P.consentLines(needTypes(), ['marketing_contact'], D.ticks);
    D.lines = lines;
    if (lines.missing.length) {
      form.appendChild(h('fieldset', { id: 'agree-box' }, h('legend', { text: (F.format && F.format !== 'online' ? '5' : '4') + '. Agreements for this order' }), P.legalLinks(), lines.node,
        h('p', { class: 'small muted', text: 'Only what this order needs is asked. You do not need to agree to live-lesson recording to buy a book.' })));
    }
    // summary + submit
    var c = price(), childSel = childById(F.child);
    var summary = F.format ? ('Level ' + F.level + ', ' + M.FORMAT_SHORT[F.format] + (childSel ? ', for ' + childSel.display_name : '') + (c != null ? ': ' + M.money(c) : '')) : 'Choose an option to see the price.';
    form.appendChild(h('p', { class: 'msg info', id: 'order-summary', role: 'status', text: summary }));
    if (F.format && c == null) {
      form.appendChild(h('p', null, h('strong', { text: 'The price for this book is not set yet.' }), ' You can ask us and we will tell you when it is ready.'));
      form.appendChild(h('p', null, h('a', { class: 'btn', id: 'ask-us', href: M.waLink('Hi, I would like to know the price of Extension Workbook Level ' + F.level + ' (' + M.FORMAT_SHORT[F.format] + ').'), rel: 'noopener', text: 'Ask us' })));
    } else {
      form.appendChild(h('p', null, h('button', { class: 'btn', type: 'submit', id: 'place-order', disabled: !F.format || c == null, text: 'Place order' }),
        h('span', { class: 'small muted', text: ' This does not charge you. You pay afterwards by PayNow' + (M.CFG.PAYMENT_MODE === 'stripe' ? ' or by card' : '') + ' with your reference.' })));
    }
    form.appendChild(asks);
    return form;
  }
  function field(id, label, key, o) {
    var inp = h('input', { type: o.type || 'text', id: id, value: F[key], maxlength: o.maxlength, inputmode: o.inputmode, autocomplete: o.autocomplete,
      oninput: function (e) { F[key] = e.target.value; } });
    return h('p', null, h('label', { for: id, text: label }), inp);
  }

  async function submit(ev) {
    ev.preventDefault();
    var c = childById(F.child);
    if (!F.level || !F.format) return run(async function () { throw M.say('Please choose a level and an option.'); });
    if (!c) return run(async function () { throw M.say('Please choose which child the book is for.'); });
    if (price() == null) return run(async function () { throw new Error('price_not_set'); });
    if (F.format !== 'workbook' && hasOnline(c.id, F.level)) return run(async function () { throw M.say('This child already has online access to that level.'); });
    var ship = F.format !== 'online';
    if (ship) {
      if (!F.name.trim() || !F.address.trim()) return run(async function () { throw M.say('Please fill in the name and address for the parcel.'); });
      if (!/^[0-9]{6}$/.test(F.postal.trim())) return run(async function () { throw new Error('bad_address'); });
    }
    var got = D.lines.collect();
    if (!got.ok) return run(async function () { throw M.say(got.problem); });
    var btn = document.getElementById('place-order'); if (btn) btn.disabled = true;
    flash(null);
    try {
      await P.saveConsents(got.items);
      var id = await M.rpc('create_ext_order', { p_child: c.id, p_level: F.level, p_format: F.format,
        p_ship_name: ship ? F.name.trim() : null, p_ship_address: ship ? F.address.trim() : null, p_ship_postal: ship ? F.postal.trim() : null, p_ship_phone: ship ? (F.phone.trim() || null) : null });
      D.last = id; flash('ok', 'Order placed. Please pay with the reference below so we can switch it on. An order that is not paid within 14 days is cancelled automatically.');
      F.format = ''; F.name = F.address = F.postal = F.phone = '';
    } catch (e) { flash('err', M.errText(e)); }
    await refresh();
    M.focusResult(app);
  }

  function payBlock(o) {
    var box = h('div', { class: 'msg info pay', 'data-pay-for': o.reference });
    box.appendChild(h('div', { 'data-paynow-line': '1', text: M.paynowLine(o.amount_cents) }));
    box.appendChild(h('div', null, 'Put this reference in the PayNow comment: ', h('span', { class: 'code', 'data-ref': '1', text: o.reference })));
    box.appendChild(h('div', { class: 'small', text: 'We tick it off by hand, usually within a day. This page will then show "paid" and ' + (o.format === 'workbook' ? 'we will post your book.' : 'online access is switched on for ' + (o.child_label || 'your child') + '.') }));
    if (M.CFG.PAYMENT_MODE === 'stripe') {
      box.appendChild(h('button', { class: 'btn sm', type: 'button', 'data-pay-online': o.id, text: 'Pay ' + M.money(o.amount_cents) + ' online (card or PayNow)', onclick: function (e) { payOnline(o, box, e.currentTarget); } }));
    }
    return box;
  }
  async function payOnline(o, box, btn) {
    btn.disabled = true; btn.textContent = 'Opening secure payment page...';
    try {
      var r = await fetch('/api/stripe-create-ext-checkout', { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + S.session.access_token }, body: JSON.stringify({ order_id: o.id }) });
      var j = await r.json().catch(function () { return {}; });
      if (!r.ok || !j.url) throw M.say('Could not start the payment. Nothing was charged. Please try again.');
      M.goToStripe(j.url);   // only https://checkout.stripe.com/... is followed
    } catch (e) { btn.disabled = false; btn.textContent = 'Try again'; var eb = box.querySelector('[data-pay-error]') || box.appendChild(h('div', { 'data-pay-error': '1' })); M.notice(eb, 'err', M.errText(e)); M.focusResult(eb); }
  }
  var STATUS = { pending_payment: 'waiting for payment', paid: 'paid', cancelled: 'cancelled', refunded: 'refunded' };
  var SHIP = { to_ship: 'We are getting your book ready to post', shipped: 'Posted', delivered: 'Delivered' };
  function orderCard(o) {
    var kid = o.child_label || 'your child';
    var c = h('div', { class: 'card order', 'data-order': o.reference },
      h('div', { class: 'row' }, h('strong', { text: 'Level ' + o.level + ', ' + M.FORMAT_SHORT[o.format] + ' for ' + kid }),
        h('span', { class: 'pill ' + o.status, 'data-order-status': o.reference, text: STATUS[o.status] || o.status })),
      h('p', { class: 'small muted', text: 'Reference ' + o.reference + ' | ' + M.money(o.amount_cents) + ' | ordered ' + M.dayText(o.created_at) }));
    if (o.status === 'pending_payment') {
      c.appendChild(payBlock(o));
      c.appendChild(h('button', { class: 'btn alt sm', type: 'button', 'data-cancel-order': o.reference, text: 'Cancel this order', onclick: function () {
        if (confirm('Cancel this unpaid order? Any delivery address is deleted.')) run(function () { return M.rpc('cancel_my_ext_order', { p_order: o.id }); }, 'Order cancelled.'); } }));
    } else if (o.status === 'paid') {
      if (o.format !== 'workbook') c.appendChild(h('p', { 'data-online-on': o.reference }, 'Online access is on for ' + kid + '. ', h('a', { href: '/portal/children/', text: 'See the practice pages' })));
      if (o.format !== 'online') c.appendChild(h('p', { 'data-ship-status': o.reference, text: (SHIP[o.ship_status] || '') + (o.ship_status === 'shipped' && o.shipped_at ? ' on ' + M.dayText(o.shipped_at) : '') + (o.ship_status === 'delivered' && o.delivered_at ? ' on ' + M.dayText(o.delivered_at) : '') + '.' }));
    } else if (o.status === 'refunded') {
      c.appendChild(h('p', { class: 'small', text: 'Refunded. Online access for this order has been switched off.' }));
    }
    return c;
  }

  function paint() {
    if (!M.configured()) return draw(P.notReady());
    var fb = h('div'); if (flashMsg) M.notice(fb, flashMsg.kind, flashMsg.text);
    if (!ready) return draw(h('p', { class: 'muted', text: 'Loading...' }));
    if (!S.session) return draw([fb, P.signedOut('Log in or create a parent account to order a book. You do not need to join a class.')]);
    if (!S.parent) return draw([fb, h('section', { class: 'card' }, h('p', { text: 'We could not load your account. Please reload the page.' }))]);
    if (D.missing) return draw([P.nav('books'), P.missingSql()]);
    var out = [fb, h('div', { class: 'row' }, h('h1', { text: 'Extension books' }), P.signOutButton(function () { flash(null); refresh(); })), P.nav('books')];
    var last = D.last && D.orders.filter(function (o) { return o.id === D.last; })[0];
    if (last) {
      out.push(h('section', { class: 'card pop', id: 'order-done' }, h('h2', { text: 'Thank you, your order is in' }), payBlock(last),
        h('details', { class: 'nextstep' }, h('summary', { text: 'For grown-ups: while you wait' }),
          h('p', { class: 'small', text: 'If you would like to talk about a small group class, you can ask for a trial class whenever you like. There is no deadline and no obligation, and nothing changes for your child.' }),
          h('a', { class: 'btn alt sm', href: '/portal/trial/?from=post_purchase&child=' + last.child_id, text: 'Ask about a trial class' }))));
    }
    out.push(h('section', { class: 'card' }, h('h2', { text: 'Order an extension book' }),
      h('p', { class: 'muted', text: 'Extra problems to stretch your child. Choose a printed workbook, online practice, or both. You do not need to be in any class.' }),
      S.children.length ? orderForm() : null));
    if (!S.children.length) {
      out.push(h('section', { class: 'card pop', id: 'first-child' }, h('h2', { text: 'First, add your child' }),
        h('p', { class: 'muted', text: 'The book is set up for one child. Add them here, then choose the book.' }),
        P.childForm({ run: run, title: 'Your child', submitText: 'Add my child' })));
    }
    var open = D.orders.filter(function (o) { return o.id !== D.last; });
    out.push(h('section', { class: 'card', id: 'orders' }, h('h2', { text: 'Your orders' }),
      open.length ? open.map(orderCard) : h('p', { class: 'muted empty', 'data-no-orders': '1', text: last ? 'Your new order is shown above. Earlier orders will be listed here.' : 'No orders yet.' })));
    draw(out);
  }

  if (!M.configured()) return paint();
  M.sb().auth.onAuthStateChange(function (ev) { if (ev === 'SIGNED_OUT') refresh(); });
  refresh();
})();
