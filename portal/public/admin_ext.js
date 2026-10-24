/* Owner admin: extra tabs for extension-book orders, access, trial/preview requests, funnel counts and the tutor group report.
   Loaded BEFORE admin.js, which calls each view's load(ctx). Authority is in the database: every admin_* function raises 'forbidden' unless
   auth.uid() is in public.admins (the group report also allows the group's tutor). This file only displays and calls those functions. */
(function () {
  var M = window.MI, h = M.h, sb = function () { return M.sb(); };
  var views = window.MI_ADMIN_VIEWS = window.MI_ADMIN_VIEWS || [];
  var LEVELS = [1, 2, 3, 4, 5, 6], FORMATS = ['workbook', 'online', 'both'];
  var STATUS = { pending_payment: 'waiting for payment', paid: 'paid', cancelled: 'cancelled', refunded: 'refunded' };
  var SHIP = { not_needed: '', to_ship: 'to post', shipped: 'posted', delivered: 'delivered' };
  var SOURCE = { stripe: 'Stripe', paynow_manual: 'PayNow (ticked by owner)', admin: 'free grant' };
  var TRIAL_SOURCE = { book: 'in the book', post_purchase: 'after buying', after_submit: 'after a unit', report: 'from a report', website: 'website', other: 'portal' };
  function head(ctx, title) {
    return h('div', { class: 'row' }, h('h1', { text: title }),
      h('button', { class: 'btn alt sm', type: 'button', id: 'signout', text: 'Log out', onclick: async function () { await sb().auth.signOut(); ctx.login(); } }));
  }
  function fail(ctx, err, what, file) {
    var t = String((err && (err.message || '')) || '') + String((err && err.code) || '');
    var forbidden = /forbidden|42501/.test(t), missing = /PGRST202|42883|does not exist|schema cache|Could not find the function/.test(t);
    return ctx.mount(ctx.app, ctx.viewTabs(), h('section', { class: 'card' }, h('h1', { text: forbidden ? 'Not an admin' : what + ' unavailable' }),
      h('p', { text: forbidden ? 'You are logged in, but this login is not set up as an owner. See portal/README.md.' : missing ? 'Run portal/supabase/' + file + ' in the Supabase SQL editor first (after reviewing it).' : M.errText(err) })));
  }
  function th(list) { return h('thead', null, h('tr', null, list.map(function (x) { return h('th', { text: x }); }))); }
  function act(ctx, fn, ok) { return async function () { var x = await fn(); ctx.reload(x && x.error ? { err: M.errText(x.error) } : ok); }; }
  function bookText(level, format) { return 'Level ' + level + ', ' + M.FORMAT_SHORT[format]; }

  /* ================= Book orders ================= */
  var ofilter = 'pending';
  views.push({ id: 'orders', label: 'Book orders', load: async function (ctx) {
    var res = await Promise.all([sb().rpc('admin_list_ext_orders'), sb().from('ext_orders').select('*'), sb().rpc('admin_list_ext_prices')]);
    var bad = res[0].error || res[1].error || res[2].error; if (bad) return fail(ctx, bad, 'Book orders', 'practice_submissions.sql and portal_ui.sql');
    var det = {}; (res[1].data || []).forEach(function (o) { det[o.id] = o; });
    var rows = (res[0].data || []).map(function (r) { var d = det[r.id] || {}; return Object.assign({}, d, r); });
    var prices = {}; (res[2].data || []).forEach(function (p) { prices[p.product_id] = p; });
    var tests = {
      pending: function (r) { return r.status === 'pending_payment'; },
      toship: function (r) { return r.status === 'paid' && r.ship_status === 'to_ship'; },
      shipped: function (r) { return r.ship_status === 'shipped'; },
      delivered: function (r) { return r.ship_status === 'delivered'; },
      refund: function (r) { return !!r.refund_due; },
      all: function () { return true; } };
    var labels = { pending: 'Awaiting payment', toship: 'To post', shipped: 'Posted', delivered: 'Delivered', refund: 'Refund due', all: 'All' };
    var nRefund = rows.filter(tests.refund).length;
    var shown = rows.filter(tests[ofilter]);
    var tabs = h('div', { class: 'tabs', id: 'order-filter' }, Object.keys(labels).map(function (f) {
      return h('button', { type: 'button', 'data-filter': f, 'aria-pressed': String(ofilter === f), text: labels[f] + ' (' + rows.filter(tests[f]).length + ')', onclick: function () { ofilter = f; ctx.reload(); } });
    }));
    function ship(r, st, ok) { return h('button', { class: 'btn sm', type: 'button', 'data-ship': st, text: st === 'shipped' ? 'Mark posted' : 'Mark delivered', onclick: act(ctx, function () { return sb().rpc('admin_set_ship_status', { p_order: r.id, p_status: st }); }, ok) }); }
    var table = !shown.length ? h('p', { class: 'empty muted', id: 'noOrders', text: 'Nothing to show here.' }) : h('div', { class: 'scroll' }, h('table', { id: 'orders' },
      th(['Reference', 'Parent', 'Child', 'Book', 'Amount', 'Status', 'Posting', ''] ),
      h('tbody', null, shown.map(function (r) {
        var addr = r.ship_name ? h('details', null, h('summary', { text: 'Address' }), h('div', { class: 'small', 'data-address': r.reference },
          r.ship_name, h('br'), r.ship_address, h('br'), 'Singapore ' + r.ship_postal, h('br'), r.ship_phone || '(no phone)')) : (r.format !== 'online' && r.status === 'paid' ? h('span', { class: 'small muted', text: 'address cleared' }) : null);
        return h('tr', { 'data-order': r.reference },
          h('td', { text: r.reference }), h('td', { class: 'small', text: r.parent_email }), h('td', { text: r.child_label || '(removed)' }), h('td', { text: bookText(r.level, r.format) }),
          h('td', { class: 'nw', text: M.money(r.amount_cents) }),
          h('td', null, h('span', { class: 'pill ' + r.status, text: STATUS[r.status] || r.status }),
            r.refund_due ? [' ', h('span', { class: 'pill refunded', 'data-refund-due': r.reference, text: 'refund due' }), h('div', { class: 'small', 'data-admin-note': r.reference, text: r.admin_note || '' })] : null),
          h('td', null, SHIP[r.ship_status] ? h('span', { class: 'pill', 'data-ship-status': r.ship_status, text: SHIP[r.ship_status] }) : null, addr),
          h('td', null,
            r.status === 'pending_payment' ? [h('button', { class: 'btn sm', type: 'button', 'data-mark-paid': r.reference, text: 'Mark paid and give access', onclick: async function () {
              if (!confirm('Mark ' + r.reference + ' (' + M.money(r.amount_cents) + ') as paid and switch on ' + bookText(r.level, r.format) + ' for ' + r.child_label + '? Check your bank first.')) return;
              var x = await sb().rpc('admin_mark_ext_order_paid', { p_order: r.id }); ctx.reload(x.error ? { err: M.errText(x.error) } : 'Marked ' + r.reference + ' paid.'); } }), ' ',
              h('button', { class: 'btn alt sm', type: 'button', 'data-cancel': r.reference, text: 'Cancel', onclick: function () {
                if (confirm('Cancel the unpaid order ' + r.reference + '? Its address is deleted.')) act(ctx, function () { return sb().rpc('admin_cancel_ext_order', { p_order: r.id }); }, 'Cancelled.')(); } })] : null,
            r.refund_due && r.status === 'cancelled' && r.paid_after_cancel_at && r.format === 'online' ? [h('button', { class: 'btn sm', type: 'button', 'data-reinstate': r.reference, text: 'Reinstate (switch the book on)', onclick: function () {
              if (confirm('The parent cancelled ' + r.reference + ' but then paid. Switch on ' + bookText(r.level, r.format) + ' for ' + (r.child_label || 'the child') + ' instead of refunding?')) act(ctx, function () { return sb().rpc('admin_reinstate_ext_order', { p_order: r.id }); }, 'Reinstated ' + r.reference + '.')(); } }), ' '] : null,
            r.refund_due ? [h('button', { class: 'btn alt sm', type: 'button', 'data-refund-done': r.reference, text: 'Refund done', onclick: function () {
              var note = prompt('Refund of ' + r.reference + ' done in Stripe or by PayNow. A short note (optional):', ''); if (note === null) return;
              act(ctx, function () { return sb().rpc('admin_resolve_ext_refund', { p_order: r.id, p_note: note }); }, 'Refund recorded for ' + r.reference + '.')(); } }), ' '] : null,
            r.status === 'paid' && r.ship_status === 'to_ship' ? ship(r, 'shipped', 'Marked posted.') : null,
            r.status === 'paid' && r.ship_status === 'shipped' ? ship(r, 'delivered', 'Marked delivered.') : null,
            r.status === 'paid' ? [' ', h('button', { class: 'btn alt sm', type: 'button', 'data-refund': r.reference, text: 'Refund and remove access', onclick: function () {
              if (confirm('Mark ' + r.reference + ' refunded and switch off online access? Do the actual refund in your bank or Stripe first.')) act(ctx, function () { return sb().rpc('admin_refund_ext_order', { p_order: r.id }); }, 'Refunded; access removed.')(); } })] : null));
      }))));
    var priceRows = LEVELS.reduce(function (acc, l) { return acc.concat(FORMATS.map(function (f) { return [l, f]; })); }, []).map(function (lf) {
      var id = 'ext-l' + lf[0] + '-' + lf[1], p = prices[id], inp = h('input', { type: 'text', inputmode: 'decimal', id: 'price-' + id, 'aria-label': 'Price in dollars for ' + id, value: p ? (p.amount_cents / 100).toFixed(2) : '' });
      return h('tr', { 'data-price': id }, h('td', { text: bookText(lf[0], lf[1]) }), h('td', { class: 'nw', text: p ? (M.money(p.amount_cents) + (p.active ? '' : ' (off)')) : 'not set' }), h('td', null, inp),
        h('td', null, h('button', { class: 'btn sm', type: 'button', 'data-save-price': id, text: 'Save', onclick: function () {
          var dollars = parseFloat(String(inp.value).replace(/[^0-9.]/g, '')), cents = Math.round(dollars * 100);
          if (!(cents > 0 && cents <= 1000000)) return ctx.reload({ err: 'Please type a price in dollars, like 24.90.' });
          act(ctx, function () { return sb().rpc('admin_set_ext_price', { p_product: id, p_cents: cents, p_active: true }); }, 'Price saved for ' + id + '.')(); } }),
          p && p.active ? [' ', h('button', { class: 'btn alt sm', type: 'button', 'data-off-price': id, text: 'Turn off', onclick: act(ctx, function () { return sb().rpc('admin_set_ext_price', { p_product: id, p_cents: p.amount_cents, p_active: false }); }, 'Price turned off; families see "price coming soon".') })] : null));
    });
    ctx.mount(ctx.app, ctx.viewTabs(), head(ctx, 'Extension book orders'), ctx.msgBox(ctx.msg),
      nRefund ? h('p', { class: 'msg warn', id: 'refund-banner', role: 'status', text: nRefund + ' order' + (nRefund === 1 ? ' needs' : 's need') + ' a refund decision (money was taken but the order is cancelled or the account was deleted). Open the "Refund due" tab.' }) : null,
      h('section', { class: 'card' }, h('h2', { text: shown.length + ' shown' }), tabs, table,
        h('p', { class: 'small muted', text: 'Mark paid only after the PayNow money has arrived. It switches on online access for the one child named on the order.' }),
        h('button', { class: 'btn alt sm', type: 'button', id: 'clear-addresses', text: 'Run the address clean-up now', onclick: async function () {
          if (!confirm('Delete the delivery name, address and phone of every order that is delivered or posted more than 30 days ago, cancelled, refunded, or paid but never posted for 90 days, and cancel orders unpaid for 14 days? (This also runs by itself if the daily schedule is set up: see portal/README.md.)')) return;
          var x = await sb().rpc('admin_clear_delivered_addresses'); ctx.reload(x.error ? { err: M.errText(x.error) } : 'Cleared ' + x.data + ' address(es).'); } })),
      h('details', { class: 'card', id: 'price-card' }, h('summary', { text: 'Prices (owner only)' }),
        h('p', { class: 'small muted', text: 'Nothing is filled in for you. A book with no price shows "price coming soon" and an "Ask us" button to families, and cannot be ordered.' }),
        h('div', { class: 'scroll' }, h('table', { id: 'prices' }, th(['Book', 'Now', 'Price (S$)', '']), h('tbody', null, priceRows)))));
    M.stack(ctx.app);
  } });

  /* ================= Access ================= */
  views.push({ id: 'access', label: 'Access', load: async function (ctx) {
    var res = await Promise.all([sb().rpc('admin_list_book_access'), sb().rpc('admin_list_children')]);
    var bad = res[0].error || res[1].error; if (bad) return fail(ctx, bad, 'Access', 'portal_ui.sql');
    var rows = res[0].data || [], kids = res[1].data || [];
    var child = h('select', { id: 'grant-child' }, [h('option', { value: '' }, 'Choose a child')].concat(kids.map(function (k) { return h('option', { value: k.child_id }, k.display_name + ' (Level ' + k.level + ') | ' + k.parent_email); })));
    var level = h('select', { id: 'grant-level' }, LEVELS.map(function (l) { return h('option', { value: l }, 'Level ' + l); }));
    var fmt = h('select', { id: 'grant-format' }, FORMATS.map(function (f) { return h('option', { value: f }, M.FORMAT_SHORT[f]); }));
    var gbox = h('div'), note = h('input', { type: 'text', id: 'grant-note', maxlength: 200, placeholder: 'Why (for example: replacement, gift, trial)' });
    var table = !rows.length ? h('p', { class: 'empty muted', id: 'noAccess', text: 'No access rows yet.' }) : h('div', { class: 'scroll' }, h('table', { id: 'access' },
      th(['Child', 'Parent', 'Book', 'How', 'Status', 'Since', '']),
      h('tbody', null, rows.map(function (r) {
        return h('tr', { 'data-access': r.access_id }, h('td', { text: r.child_name }), h('td', { class: 'small', text: r.parent_email }), h('td', { text: bookText(r.level, r.format) }),
          h('td', { text: (SOURCE[r.source] || r.source) + (r.source_note ? ': ' + r.source_note : '') }),
          h('td', null, h('span', { class: 'pill ' + (r.status === 'active' ? 'paid' : 'cancelled'), text: r.status })), h('td', { text: M.dayText(r.created_at) }),
          h('td', null, r.status === 'active' ? h('button', { class: 'btn alt sm', type: 'button', 'data-revoke': r.access_id, text: 'Revoke', onclick: function () {
            if (confirm('Switch off ' + bookText(r.level, r.format) + ' for ' + r.child_name + '? Their past answers stay until the retention rule removes them.')) act(ctx, function () { return sb().rpc('admin_revoke_book_access', { p_access: r.access_id }); }, 'Access revoked.')(); } }) : null));
      }))));
    ctx.mount(ctx.app, ctx.viewTabs(), head(ctx, 'Who can open which book'), ctx.msgBox(ctx.msg),
      h('section', { class: 'card' }, h('h2', { text: 'Give access (free)' }),
        h('p', { class: 'small muted', text: 'For a gift or a fix. For a paid order use Book orders, then "Mark paid and give access". One grant is for one child.' }),
        h('form', { novalidate: true, id: 'grant-form', onsubmit: async function (ev) {
          ev.preventDefault();
          if (!child.value) return M.notice(gbox, 'err', 'Please choose a child.');
          if (!note.value.trim()) return M.notice(gbox, 'err', 'Please give a short reason.');
          var x = await sb().rpc('admin_grant_book_access', { p_child: child.value, p_level: Number(level.value), p_format: fmt.value, p_note: note.value.trim() });
          ctx.reload(x.error ? { err: M.errText(x.error) } : 'Access given.'); } },
          h('div', { class: 'grid2' }, h('p', null, h('label', { for: 'grant-child', text: 'Child' }), child), h('p', null, h('label', { for: 'grant-level', text: 'Book level' }), level),
            h('p', null, h('label', { for: 'grant-format', text: 'What' }), fmt), h('p', null, h('label', { for: 'grant-note', text: 'Reason' }), note)),
          gbox, h('button', { class: 'btn', type: 'submit', text: 'Give access' }))),
      h('section', { class: 'card' }, h('h2', { text: rows.length + ' access rows' }), table));
    M.stack(ctx.app);
  } });

  /* ================= Trials and previews ================= */
  views.push({ id: 'trials', label: 'Trials and previews', load: async function (ctx) {
    var res = await Promise.all([sb().rpc('admin_list_trial_requests'), sb().rpc('preview_open_sessions'), sb().rpc('admin_preview_funnel')]);
    if (res[0].error) return fail(ctx, res[0].error, 'Trial requests', 'practice_submissions.sql');
    var rows = res[0].data || [], sessions = res[1].error ? null : (res[1].data || []), funnel = res[2].error ? null : (res[2].data || []);
    var sets = ['contacted', 'attended', 'enrolled', 'declined'];
    var table = !rows.length ? h('p', { class: 'empty muted', id: 'noTrials', text: 'No trial requests yet.' }) : h('div', { class: 'scroll' }, h('table', { id: 'trials' },
      th(['Received', 'Parent', 'Child', 'Level', 'Times', 'From', 'Note', 'Status', '']),
      h('tbody', null, rows.map(function (r) {
        return h('tr', { 'data-trial': r.id }, h('td', { text: M.dayText(r.created_at) }),
          h('td', null, r.parent_name || '', h('br'), h('span', { class: 'small muted', text: r.parent_email + (r.parent_phone ? ' ' + r.parent_phone : '') })),
          h('td', { text: r.child_label || '' }), h('td', { text: String(r.level) }), h('td', { class: 'small', text: (r.preferred || []).join(', ') }),
          h('td', { text: TRIAL_SOURCE[r.source] || r.source }), h('td', { class: 'small', text: r.note || '' }),
          h('td', null, h('span', { class: 'pill ' + r.status, 'data-trial-status': r.id, text: r.status })),
          h('td', null, sets.filter(function (s) { return s !== r.status && r.status !== 'withdrawn'; }).map(function (s) {
            return [h('button', { class: 'btn alt sm', type: 'button', 'data-set': s, text: 'Mark ' + s, onclick: act(ctx, function () { return sb().rpc('admin_set_trial_status', { p_id: r.id, p_status: s }); }, 'Marked ' + s + '.') }), ' ']; })));
      }))));
    var pv = [h('h2', { text: 'Preview class' })];
    if (sessions === null) pv.push(h('p', { class: 'muted', id: 'noPreview', text: 'Preview classes are not switched on (preview_class.sql has not been applied). That is fine for now.' }));
    else {
      pv.push(h('p', { class: 'small muted', text: 'Open sessions and their sign-ups. Contact details are shown to the owner only.' }));
      if (!sessions.length) pv.push(h('p', { class: 'muted', text: 'No open sessions.' }));
      sessions.forEach(function (s) {
        var box = h('div', { class: 'preview-list' });
        pv.push(h('div', { class: 'card', 'data-preview-session': s.id }, h('div', { class: 'row' }, h('strong', { text: M.fmtDate(s.starts_at) + ' | ' + s.band }), s.is_full ? h('span', { class: 'pill', text: 'full' }) : null,
          h('button', { class: 'btn alt sm', type: 'button', 'data-show-signups': s.id, text: 'Show sign-ups', onclick: async function () {
            var r = await sb().rpc('admin_preview_list', { p_session: s.id }); M.clear(box);
            if (r.error) return box.appendChild(h('p', { class: 'msg err', role: 'alert', text: M.errText(r.error) }));
            box.appendChild(!r.data.length ? h('p', { class: 'muted', text: 'No sign-ups yet.' }) : h('div', { class: 'scroll' }, h('table', null, th(['Parent', 'Child', 'Status', 'Contact', 'Wants trial']),
              h('tbody', null, r.data.map(function (x) { return h('tr', null, h('td', { text: x.parent_first_name }), h('td', { text: x.child_first_name + ' (' + x.child_birth_year + ')' }), h('td', { text: x.status }), h('td', { class: 'small', text: [x.email, x.phone].filter(Boolean).join(' ') }), h('td', { text: x.wants_trial ? 'yes' : '' })); })))));
            M.stack(box); } })), box));
      });
      if (funnel && funnel.length) pv.push(h('div', { class: 'scroll' }, h('table', { id: 'pfunnel' }, th(['Band', 'Held', 'Signed up', 'Attended', 'Asked for trial', 'Trial attended', 'Joined']),
        h('tbody', null, funnel.map(function (f) { return h('tr', null, [f.band, f.sessions_held, f.registered, f.attended, f.wants_trial, f.trial_attended, f.enrolled].map(function (v) { return h('td', { text: String(v) }); })); })))));
    }
    ctx.mount(ctx.app, ctx.viewTabs(), head(ctx, 'Trial class requests'), ctx.msgBox(ctx.msg),
      h('section', { class: 'card' }, h('h2', { text: rows.length + ' trial requests' }),
        h('p', { class: 'small muted', text: 'Parents only. Booking the actual slot is a WhatsApp or email follow-up by you. Requests are deleted after 12 months (default).' }), table),
      h('section', { class: 'card', id: 'preview-card' }, pv));
    M.stack(ctx.app);
  } });

  /* ================= Funnel ================= */
  views.push({ id: 'funnel', label: 'Funnel', load: async function (ctx) {
    var res = await Promise.all([sb().rpc('admin_funnel_counts'), sb().rpc('admin_practice_overview', { p_unit: null })]);
    if (res[0].error) return fail(ctx, res[0].error, 'Funnel', 'practice_submissions.sql');
    var f = res[0].data || {}, by = f.trial_by_source || {};
    var steps = [['Extension books paid', f.books_paid], ['Families who bought a book', f.families_bought], ['Children who started the online practice', f.children_started],
      ['Trial class requests', f.trial_requests], ['Trial class attended', f.trial_attended], ['Enrolled afterwards', f.enrolled]];
    var src = Object.keys(by).sort().map(function (k) { return (TRIAL_SOURCE[k] || k) + ' ' + by[k]; }).join(', ');
    var groupless = {}; (res[1].error ? [] : res[1].data || []).forEach(function (r) { if (!r.has_group) groupless[r.child_id + '|' + r.unit_key] = r; });
    var gl = Object.keys(groupless).map(function (k) { return groupless[k]; });
    ctx.mount(ctx.app, ctx.viewTabs(), head(ctx, 'Practice and trial class funnel'), ctx.msgBox(ctx.msg),
      h('section', { class: 'card' }, h('h2', { text: 'Counts' }), h('p', { class: 'small muted', text: 'Counts only, from rows that already exist. No cookies and no tracking of visitors.' }),
        h('table', { id: 'funnel' }, th(['Step', 'Count']), h('tbody', null, steps.map(function (s) { return h('tr', { 'data-step': s[0] }, h('td', { text: s[0] }), h('td', { text: String(s[1] == null ? 0 : s[1]) })); }))),
        src ? h('p', { class: 'small', id: 'trial-sources', text: 'Trial requests by where they came from: ' + src + '.' }) : null),
      h('section', { class: 'card' }, h('h2', { text: 'Children with no group (book families)' }),
        h('p', { class: 'small muted', text: 'You see these because there is no tutor group for them. A parent sees only their own child.' }),
        gl.length ? h('table', { id: 'groupless' }, th(['Child', 'Unit', 'Sent', 'Group']), h('tbody', null, gl.map(function (r) {
          return h('tr', null, h('td', { text: r.display_name }), h('td', { text: r.unit_key }), h('td', { text: M.dayText(r.received_at) }), h('td', { text: 'none' })); }))) : h('p', { class: 'muted', id: 'noGroupless', text: 'None yet.' })));
    M.stack(ctx.app);
  } });

  /* ================= Tutor group report ================= */
  var rep = { group: '', unit: '' };
  function reading(r) {
    var answered = (r.n_right || 0) + (r.n_wrong || 0);
    if (answered < 2) return ['·', 'not enough answers yet to say'];
    if (!r.n_wrong) return ['●', 'going well'];
    if (!r.n_right) return ['○', 'worth practising together'];
    return ['◐', 'some right, some to look at'];
  }
  views.push({ id: 'report', label: 'Group report', load: async function (ctx) {
    var gs = await sb().from('groups').select('id,name').order('id');
    if (gs.error) return fail(ctx, gs.error, 'Group report', 'schema.sql');
    var groups = gs.data || []; if (!rep.group && groups.length) rep.group = groups[0].id;
    var units = [], skillRows = [], slips = [], roster = [], err = null;
    if (rep.group) {
      var r1 = await sb().rpc('tutor_group_practice', { p_group: rep.group });
      if (r1.error) return fail(ctx, r1.error, 'Group report', 'practice_submissions.sql');
      var seen = {}; (r1.data || []).forEach(function (x) { if (!seen[x.unit_key]) { seen[x.unit_key] = 1; units.push(x.unit_key); } });
      if (units.indexOf(rep.unit) < 0) rep.unit = units[0] || '';
      var en = await sb().rpc('admin_list_enrolments');
      roster = (en.data || []).filter(function (e) { return e.group_id === rep.group && e.enrolment_status === 'confirmed' && e.child_name; }).map(function (e) { return e.child_name; });
      if (rep.unit) {
        var r2 = await Promise.all([sb().rpc('tutor_group_skill_report', { p_group: rep.group, p_unit: rep.unit }), sb().rpc('tutor_group_slips', { p_group: rep.group, p_unit: rep.unit })]);
        if (r2[0].error || r2[1].error) return fail(ctx, r2[0].error || r2[1].error, 'Group report', 'portal_ui.sql');
        skillRows = r2[0].data || []; slips = r2[1].data || [];
      }
    }
    var gsel = h('select', { id: 'rep-group', 'aria-label': 'Group', onchange: function (e) { rep.group = e.target.value; rep.unit = ''; ctx.reload(); } }, groups.map(function (g) { return h('option', { value: g.id, selected: g.id === rep.group }, g.name + ' (' + g.id + ')'); }));
    var usel = h('select', { id: 'rep-unit', 'aria-label': 'Unit', onchange: function (e) { rep.unit = e.target.value; ctx.reload(); } }, units.map(function (u) { return h('option', { value: u, selected: u === rep.unit }, u); }));
    var skills = []; skillRows.forEach(function (r) { if (r.skill && skills.indexOf(r.skill) < 0) skills.push(r.skill); }); skills.sort();
    var names = {}; roster.forEach(function (n) { names[n] = 1; }); skillRows.forEach(function (r) { names[r.display_name] = 1; });
    var sorted = Object.keys(names).sort(function (a, b) { return a.localeCompare(b); });   // alphabetical on purpose, never by result
    var sent = {}; skillRows.forEach(function (r) { sent[r.display_name] = 1; });
    var body = sorted.map(function (n) {
      var mine = skillRows.filter(function (r) { return r.display_name === n; });
      if (!sent[n]) return h('tr', { 'data-child': n }, h('td', { text: n }), h('td', { colspan: String(skills.length + 1), class: 'muted', text: 'has not sent answers yet' }));
      var cells = skills.map(function (s) { var r = mine.filter(function (x) { return x.skill === s; })[0]; var rd = r ? reading(r) : ['·', 'not enough answers yet to say']; return h('td', { 'data-skill': s, title: rd[1], text: rd[0] + ' ' + rd[1] }); });
      var paper = mine.filter(function (x) { return !x.skill; })[0];
      var ptxt = !paper ? '' : [paper.n_self_got ? 'got it' : '', paper.n_self_notyet ? 'not yet' : '', paper.n_self_checked ? 'checked' : ''].filter(Boolean).join(', ');
      return h('tr', { 'data-child': n }, [h('td', { text: n })].concat(cells, [h('td', { 'data-skill': 'paper', text: ptxt })]));
    });
    ctx.mount(ctx.app, ctx.viewTabs(), head(ctx, 'Tutor group report'), ctx.msgBox(ctx.msg),
      h('section', { class: 'card' }, h('div', { class: 'grid2' }, h('p', null, h('label', { for: 'rep-group', text: 'Group' }), gsel), h('p', null, h('label', { for: 'rep-unit', text: 'Unit' }), usel)),
        !units.length ? h('p', { class: 'muted empty', id: 'noReport', text: 'No answers have been sent for this group yet.' }) : [
          h('h2', { text: 'Group ' + rep.group + ': ' + rep.unit }),
          h('p', { class: 'small muted', text: sorted.filter(function (n) { return sent[n]; }).length + ' of ' + sorted.length + ' children have sent answers.' }),
          h('div', { class: 'scroll' }, h('table', { id: 'group-report', class: 'wide' }, th(['Child'].concat(skills, ['Checked on paper'])), h('tbody', null, body))),
          h('p', { class: 'small muted', text: '● going well · ◐ some right, some to look at · ○ worth practising together · · not enough answers to say (needs at least 2 auto-marked answers). Counts cover auto-marked questions only; checked-on-paper questions are shown separately.' }),
          h('h2', { text: 'For planning the next lesson: the most common misconceptions' }),
          slips.length ? h('div', { class: 'scroll' }, h('table', { id: 'slips' }, th(['Question', 'Skill', 'Likely misconception', 'Children']),
            h('tbody', null, slips.map(function (s) { return h('tr', null, h('td', { text: 'Question ' + s.item_pos }), h('td', { text: s.skill || '' }), h('td', { text: s.say }), h('td', { text: s.n_children + ' of ' + s.n_sent })); }))))
            : h('p', { class: 'muted', id: 'noSlips', text: 'No common misconceptions to show.' }),
          h('p', { class: 'small muted', text: 'Children are listed alphabetically on purpose. This page is for the tutor only. It is not shown to families and is not a league table.' })]));
    M.stack(ctx.app);
  } });
})();
