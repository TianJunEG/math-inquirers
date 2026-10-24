/* Owner admin: list enrolments, tick off manual PayNow payments, see group fill. All authority is in the database:
   admin_* functions raise 'forbidden' unless auth.uid() is in public.admins. This page only displays. */
(function () {
  var M = window.MI, h = M.h, app = document.getElementById('app');
  document.getElementById('top').appendChild(M.header('Owner admin'));
  function mount() { M.mount.apply(M, arguments); M.stack(app); }
  function msgBox(m) { return m ? (typeof m === 'object' ? h('p', { class: 'msg err', role: 'alert', text: m.err }) : h('p', { class: 'msg ok', role: 'status', text: m })) : null; }
  var filter = 'pending', view = 'enrol', slotLabels = null, productNames = null;
  var EXT = window.MI_ADMIN_VIEWS || [];   // extra tabs (orders, access, trials, funnel, group report) registered by admin_ext.js, which loads first
  var WINDOWS = { 'wkday-am': 'Weekday mornings', 'wkday-pm': 'Weekday afternoons', 'wkday-eve': 'Weekday evenings', sat: 'Saturday', sun: 'Sunday' };
  var BANDS = { 'under-6': 'Under 6', '6-7': '6 to 7', '8-9': '8 to 9', '10-11': '10 to 11', '12-13': '12 to 13', '14-plus': '14 or older' };
  if (!M.configured()) { mount(app, h('section', { class: 'card' }, h('p', { text: 'Set SUPABASE_URL and ANON_KEY in portal/config.js first.' }))); return; }

  async function login() {
    var box = h('div'), em = h('input', { type: 'email', id: 'email' }), pw = h('input', { type: 'password', id: 'password' });
    mount(app, h('section', { class: 'card pop' }, h('h1', { text: 'Owner log in' }),
      h('form', { novalidate: true, onsubmit: async function (ev) { ev.preventDefault();
        var r = await M.sb().auth.signInWithPassword({ email: em.value.trim(), password: pw.value });
        if (r.error) return M.notice(box, 'err', M.errText(r.error)); load(); } },
        h('p', null, h('label', { for: 'email', text: 'Email' }), em), h('p', null, h('label', { for: 'password', text: 'Password' }), pw),
        h('button', { class: 'btn', type: 'submit', text: 'Log in' })), box));
  }

  async function load(msg) {
    var sb = M.sb(), s = await sb.auth.getSession();
    if (!s.data.session) return login();
    if (document.getElementById('viewtabs')) mount(app, viewTabs(), h('p', { class: 'muted', role: 'status', text: 'Loading...' }));
    var ev = EXT.filter(function (v) { return v.id === view; })[0];
    if (ev) return ev.load({ msg: msg, M: M, h: h, app: app, mount: mount, viewTabs: viewTabs, msgBox: msgBox, reload: load, login: login });
    if (view === 'interest') return loadInterest(msg);
    if (view === 'products') return loadProducts(msg);
    var res = await Promise.all([sb.rpc('admin_list_enrolments'), sb.rpc('group_fill'), sb.from('groups').select('id,name,seats').order('id')]);
    if (res[0].error) {
      var forbidden = /forbidden|42501/.test(res[0].error.message + (res[0].error.code || ''));
      return mount(app, h('section', { class: 'card' }, h('h1', { text: forbidden ? 'Not an admin' : 'Could not load enrolments' }),
        h('p', { text: forbidden ? 'You are logged in, but this login is not set up as an owner. See portal/README.md. You can log out and try another account.' : M.errText(res[0].error) }),
        h('button', { class: 'btn alt', type: 'button', text: 'Log out', onclick: async function () { await sb.auth.signOut(); login(); } })));
    }
    draw(res[0].data || [], res[1].data || [], res[2].data || [], msg);
  }

  function draw(rows, fill, groups, msg) {
    var fillBy = {}; fill.forEach(function (f) { fillBy[f.group_id] = f; });
    var fillCard = h('section', { class: 'card' }, h('h2', { text: 'Group fill' }), h('div', { class: 'scroll' }, h('table', { id: 'fill' },
      h('thead', null, h('tr', null, ['Group', 'Taken', 'Seats', 'Fill'].map(function (x) { return h('th', { text: x }); }))),
      h('tbody', null, groups.map(function (g) {
        var f = fillBy[g.id] || { taken: 0, seats: g.seats };
        return h('tr', { 'data-group': g.id }, h('td', { text: g.name }), h('td', { text: String(f.taken) }), h('td', { text: String(f.seats) }),
          h('td', null, h('div', { class: 'bar' }, h('i', { style: 'width:' + Math.round(100 * f.taken / f.seats) + '%' }))));
      })))));
    var shown = rows.filter(function (r) { return filter === 'all' || (filter === 'pending' ? r.payment_status === 'pending' && r.enrolment_status !== 'cancelled' : r.payment_status === filter); });
    var tabs = h('div', { class: 'tabs' }, ['pending', 'paid', 'all'].map(function (f) {
      return h('button', { type: 'button', 'aria-pressed': String(filter === f), text: f === 'pending' ? 'Awaiting payment' : f === 'paid' ? 'Paid' : 'All', onclick: function () { filter = f; draw(rows, fill, groups); } });
    }));
    var table = !shown.length ? h('p', { class: 'empty muted', id: 'noEnrolments', text: filter === 'pending' ? 'Nothing is waiting for payment.' : 'Nothing to show here yet.' }) : h('div', { class: 'scroll' }, h('table', { id: 'enrolments' },
      h('thead', null, h('tr', null, ['Reference', 'Child', 'Parent', 'Group', 'Method', 'Amount', 'Status', ''].map(function (x) { return h('th', { text: x }); }))),
      h('tbody', null, shown.map(function (r) {
        return h('tr', { 'data-enrolment': r.enrolment_id },
          h('td', { text: r.payment_reference }), h('td', { text: r.child_name || '(removed)' }),
          h('td', null, r.parent_name || '', h('br'), h('span', { class: 'small muted', text: (r.parent_email || '') + (r.parent_phone ? ' ' + r.parent_phone : '') })),
          h('td', { class: 'nw', text: r.group_id }), h('td', { text: r.payment_method === 'paynow_manual' ? 'PayNow' : r.payment_method }), h('td', { class: 'nw', text: M.money(r.amount_cents) }),
          h('td', null, h('span', { class: 'pill ' + r.payment_status, text: 'payment ' + r.payment_status }), ' ', h('span', { class: 'pill ' + r.enrolment_status, text: 'place ' + r.enrolment_status.replace('_', ' ') })),
          h('td', null, r.payment_status === 'pending' && r.enrolment_status !== 'cancelled' ? h('button', { class: 'btn sm', type: 'button', 'data-mark-paid': r.payment_reference, text: 'Mark paid', onclick: async function () {
            if (!confirm('Mark ' + r.payment_reference + ' (' + M.money(r.amount_cents) + ') as paid? Check your bank first.')) return;
            var x = await M.sb().rpc('admin_mark_paid', { p_payment: r.payment_id, p_note: 'PayNow ticked by owner' });
            load(x.error ? { err: M.errText(x.error) } : 'Marked ' + r.payment_reference + ' paid.'); } }) : null));
      }))));
    mount(app, viewTabs(), h('div', { class: 'row' }, h('h1', { text: 'Enrolments' }),
        h('button', { class: 'btn alt sm', type: 'button', id: 'signout', text: 'Log out', onclick: async function () { await M.sb().auth.signOut(); login(); } })),
      msgBox(msg), fillCard,
      h('section', { class: 'card' }, h('h2', { text: shown.length + ' shown' }), tabs, table));
  }
  function viewTabs() {
    return h('div', { class: 'tabs', id: 'viewtabs' }, [['enrol', 'Enrolments'], ['interest', 'Interest'], ['products', 'Shop interest']].concat(EXT.map(function (v) { return [v.id, v.label]; })).map(function (x) {
      return h('button', { type: 'button', 'data-view': x[0], 'aria-pressed': String(view === x[0]), text: x[1], onclick: function () { view = x[0]; load(); } });
    }));
  }

  /* ---- Interest tab: "Request another time" requests. Reads only through admin_* functions (is_admin() checked in the database). ---- */
  function slotName(id) { return (slotLabels && slotLabels[id]) ? slotLabels[id] + ' (' + id + ')' : id; }
  async function loadInterest(msg) {
    var sb = M.sb();
    if (slotLabels === null) {   // placeholder slot labels published by the site build (public data); fall back to ids if unavailable
      slotLabels = {};
      try { var r = await fetch('/interest-slots.json', { cache: 'no-store' }); if (r.ok) (await r.json()).slots.forEach(function (s) { slotLabels[s.id] = s.label; }); } catch (e) {}
    }
    var res = await Promise.all([sb.rpc('admin_interest_tally'), sb.rpc('admin_list_interest_requests')]);
    var bad = res[0].error || res[1].error;
    if (bad) {
      var forbidden = /forbidden|42501/.test(bad.message + (bad.code || ''));
      var missing = /admin_interest|PGRST202|42883|does not exist|schema cache/.test(bad.message + (bad.code || ''));
      return mount(app, viewTabs(), h('section', { class: 'card' }, h('h1', { text: forbidden ? 'Not an admin' : 'Interest requests unavailable' }),
        h('p', { text: forbidden ? 'You are logged in, but this login is not set up as an owner. See portal/README.md. You can log out and try another account.' : missing ? 'Run portal/supabase/interest_requests.sql in the Supabase SQL editor first.' : M.errText(bad) })));
    }
    drawInterest(res[0].data || [], res[1].data || [], msg);
  }
  function drawInterest(tally, rows, msg) {
    var sb = M.sb(), levels = {};
    tally.forEach(function (r) { (levels[r.level] = levels[r.level] || []).push(r); });
    var kindName = function (r) { return r.kind === 'slot' ? slotName(r.key) : r.kind === 'window' ? (WINDOWS[r.key] || r.key) : 'Free-text time given'; };
    var tallyRows = [];
    Object.keys(levels).sort().forEach(function (lv) {
      var items = levels[lv], total = items.filter(function (r) { return r.kind === 'total'; })[0];
      tallyRows.push(h('tr', { 'data-level': lv, class: 'tot' }, h('td', { text: 'Level ' + lv }), h('td', null, h('b', { text: 'All requests' })), h('td', { text: String(total ? total.n : 0) })));
      items.filter(function (r) { return r.kind !== 'total'; }).sort(function (a, b) { return Number(b.n) - Number(a.n); }).forEach(function (r) {
        tallyRows.push(h('tr', { 'data-level': lv, 'data-key': r.key }, h('td', { text: '' }), h('td', { text: kindName(r) }), h('td', { text: String(r.n) })));
      });
    });
    var tallyCard = h('section', { class: 'card' }, h('h2', { text: 'Tally by level and time' }),
      h('p', { class: 'small muted', text: 'Each request counts once under every time it ticked, so a level\'s rows can add up to more than its total.' }),
      tallyRows.length ? h('div', { class: 'scroll' }, h('table', { id: 'tally' }, h('thead', null, h('tr', null, ['Level', 'Time', 'Requests'].map(function (x) { return h('th', { text: x }); }))), h('tbody', null, tallyRows)))
                       : h('p', { id: 'noInterest', class: 'muted', text: 'No requests yet.' }));
    function times(r) { return (r.slots || []).map(slotName).concat((r.windows || []).map(function (w) { return WINDOWS[w] || w; })).concat(r.other_time ? ['Other: ' + r.other_time] : []).join('; '); }
    function act(fn, ok) { return async function () { var x = await fn(); loadInterest(x.error ? { err: M.errText(x.error) } : ok); }; }
    var list = h('div', { class: 'scroll' }, h('table', { id: 'requests' },
      h('thead', null, h('tr', null, ['Received', 'Level', 'Age', 'Times', 'Parent', 'Contact', 'Note', 'Status', ''].map(function (x) { return h('th', { text: x }); }))),
      h('tbody', null, rows.map(function (r) {
        return h('tr', { 'data-request': r.id },
          h('td', { text: new Date(r.created_at).toLocaleDateString('en-SG') }), h('td', { text: String(r.level) }), h('td', { text: BANDS[r.age_band] || r.age_band }),
          h('td', { text: times(r) }), h('td', { text: r.parent_first_name }),
          h('td', { text: [r.contact_whatsapp ? 'WhatsApp ' + r.contact_whatsapp : '', r.contact_email || ''].filter(Boolean).join(' / ') }),
          h('td', { text: r.note || '' }), h('td', null, h('span', { class: 'pill ' + r.status, text: r.status })),
          h('td', null,
            r.status !== 'contacted' ? h('button', { class: 'btn sm', type: 'button', 'data-set-status': 'contacted', text: 'Mark contacted', onclick: act(function () { return sb.rpc('admin_set_interest_status', { p_id: r.id, p_status: 'contacted' }); }, 'Marked contacted.') }) : null, ' ',
            h('button', { class: 'btn alt sm', type: 'button', 'data-delete': r.id, text: 'Delete', onclick: function () {
              if (!confirm('Delete this request for good? Do this when the parent asks, or once it is dealt with.')) return;
              act(function () { return sb.rpc('admin_delete_interest_request', { p_id: r.id }); }, 'Deleted.')(); } })));
      }))));
    mount(app, viewTabs(), h('div', { class: 'row' }, h('h1', { text: 'Interest in other times' }),
        h('button', { class: 'btn alt sm', type: 'button', id: 'signout', text: 'Log out', onclick: async function () { await sb.auth.signOut(); login(); } })),
      msgBox(msg), tallyCard,
      h('section', { class: 'card' }, h('h2', { text: rows.length + ' requests' }),
        h('p', { class: 'small muted', text: 'Placeholder times only: nothing here is a booking. Contact only about timing. Requests are deleted after 12 months (default).' }),
        h('button', { class: 'btn alt sm', type: 'button', id: 'purge', text: 'Delete expired requests', onclick: async function () {
          if (!confirm('Delete every request older than its retention date?')) return;
          var x = await sb.rpc('admin_purge_expired_interest_requests'); loadInterest(x.error ? { err: M.errText(x.error) } : 'Deleted ' + x.data + ' expired request(s).'); } }),
        rows.length ? list : h('p', { class: 'muted', text: 'No requests yet.' })));
  }

  /* ---- Shop interest tab: "Tell me when it's ready" requests from /shop/. Reads only through admin_* functions (is_admin() checked in the database). ---- */
  async function loadProducts(msg) {
    var sb = M.sb();
    if (productNames === null) {   // product names published by the site build (id -> name, no prices); fall back to ids if unavailable
      productNames = {};
      try { var r = await fetch('/shop-products.json', { cache: 'no-store' }); if (r.ok) productNames = await r.json(); } catch (e) {}
    }
    var res = await Promise.all([sb.rpc('admin_product_interest_tally'), sb.rpc('admin_list_product_interest')]);
    var bad = res[0].error || res[1].error;
    if (bad) {
      var forbidden = /forbidden|42501/.test(bad.message + (bad.code || ''));
      var missing = /admin_product_interest|PGRST202|42883|does not exist|schema cache/.test(bad.message + (bad.code || ''));
      return mount(app, viewTabs(), h('section', { class: 'card' }, h('h1', { text: forbidden ? 'Not an admin' : 'Shop interest unavailable' }),
        h('p', { text: forbidden ? 'You are logged in, but this login is not set up as an owner. See portal/README.md. You can log out and try another account.' : missing ? 'Run portal/supabase/product_interest.sql in the Supabase SQL editor first (after reviewing it).' : M.errText(bad) })));
    }
    drawProducts(res[0].data || [], res[1].data || [], msg);
  }
  function drawProducts(tally, rows, msg) {
    var sb = M.sb(), FMT = { soft: 'Soft copy', physical: 'Physical copy' };
    function pname(id) { return productNames && productNames[id] ? productNames[id] + ' (' + id + ')' : id; }
    function itemsText(items) { return (items || []).map(function (i) { return pname(i.product) + ', ' + (FMT[i.format] || i.format) + (i.format === 'physical' && i.qty > 1 ? ' x' + i.qty : ''); }).join('; '); }
    function act(fn, ok) { return async function () { var x = await fn(); loadProducts(x.error ? { err: M.errText(x.error) } : ok); }; }
    var total = tally.filter(function (r) { return r.product === '*'; })[0];
    var trs = tally.filter(function (r) { return r.product !== '*'; }).map(function (r) {
      return h('tr', { 'data-product': r.product, 'data-format': r.format }, h('td', { text: pname(r.product) }), h('td', { text: FMT[r.format] || r.format }), h('td', { text: String(r.requests) }), h('td', { text: String(r.copies) }));
    });
    var tallyCard = h('section', { class: 'card' }, h('h2', { text: 'Interest by product (' + (total ? total.requests : 0) + ' requests)' }),
      h('p', { class: 'small muted', text: 'Each request counts once under every product and copy type it asked for. Copies = physical quantities, soft copies count 1.' }),
      trs.length ? h('div', { class: 'scroll' }, h('table', { id: 'ptally' }, h('thead', null, h('tr', null, ['Product', 'Copy', 'Requests', 'Copies'].map(function (x) { return h('th', { text: x }); }))), h('tbody', null, trs)))
                 : h('p', { id: 'noProducts', class: 'muted', text: 'No requests yet.' }));
    var list = h('div', { class: 'scroll' }, h('table', { id: 'prequests' },
      h('thead', null, h('tr', null, ['Received', 'Items', 'Parent', 'Contact', 'Note', 'Status', ''].map(function (x) { return h('th', { text: x }); }))),
      h('tbody', null, rows.map(function (r) {
        return h('tr', { 'data-request': r.id },
          h('td', { text: new Date(r.created_at).toLocaleDateString('en-SG') }), h('td', { text: itemsText(r.items) }), h('td', { text: r.parent_first_name }),
          h('td', { text: [r.contact_whatsapp ? 'WhatsApp ' + r.contact_whatsapp : '', r.contact_email || ''].filter(Boolean).join(' / ') }),
          h('td', { text: r.note || '' }), h('td', null, h('span', { class: 'pill ' + r.status, text: r.status })),
          h('td', null,
            r.status !== 'notified' ? h('button', { class: 'btn sm', type: 'button', 'data-set-status': 'notified', text: 'Mark notified', onclick: act(function () { return sb.rpc('admin_set_product_interest_status', { p_id: r.id, p_status: 'notified' }); }, 'Marked notified.') }) : null, ' ',
            h('button', { class: 'btn alt sm', type: 'button', 'data-delete': r.id, text: 'Delete', onclick: function () {
              if (!confirm('Delete this request for good? Do this when the parent asks, or once they have been told the product is ready.')) return;
              act(function () { return sb.rpc('admin_delete_product_interest', { p_id: r.id }); }, 'Deleted.')(); } })));
      }))));
    mount(app, viewTabs(), h('div', { class: 'row' }, h('h1', { text: 'Shop interest' }),
        h('button', { class: 'btn alt sm', type: 'button', id: 'signout', text: 'Log out', onclick: async function () { await sb.auth.signOut(); login(); } })),
      msgBox(msg), tallyCard,
      h('section', { class: 'card' }, h('h2', { text: rows.length + ' requests' }),
        h('p', { class: 'small muted', text: 'Not orders: nothing is paid or reserved. Contact only to say a product is ready. Requests are deleted after 12 months (default).' }),
        h('button', { class: 'btn alt sm', type: 'button', id: 'ppurge', text: 'Delete expired requests', onclick: async function () {
          if (!confirm('Delete every request older than its retention date?')) return;
          var x = await sb.rpc('admin_purge_expired_product_interest'); loadProducts(x.error ? { err: M.errText(x.error) } : 'Deleted ' + x.data + ' expired request(s).'); } }),
        rows.length ? list : h('p', { class: 'muted', text: 'No requests yet.' })));
  }
  load();
})();
