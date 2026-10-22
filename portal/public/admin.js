/* Owner admin: list enrolments, tick off manual PayNow payments, see group fill. All authority is in the database:
   admin_* functions raise 'forbidden' unless auth.uid() is in public.admins. This page only displays. */
(function () {
  var M = window.MI, h = M.h, app = document.getElementById('app');
  document.getElementById('top').appendChild(M.header('Owner admin'));
  var filter = 'pending';
  if (!M.configured()) { M.mount(app, h('section', { class: 'card' }, h('p', { text: 'Set SUPABASE_URL and ANON_KEY in portal/config.js first.' }))); return; }

  async function login() {
    var box = h('div'), em = h('input', { type: 'email', id: 'email' }), pw = h('input', { type: 'password', id: 'password' });
    M.mount(app, h('section', { class: 'card pop' }, h('h1', { text: 'Owner log in' }),
      h('form', { novalidate: true, onsubmit: async function (ev) { ev.preventDefault();
        var r = await M.sb().auth.signInWithPassword({ email: em.value.trim(), password: pw.value });
        if (r.error) return M.notice(box, 'err', M.errText(r.error)); load(); } },
        h('p', null, h('label', { for: 'email', text: 'Email' }), em), h('p', null, h('label', { for: 'password', text: 'Password' }), pw),
        h('button', { class: 'btn', type: 'submit', text: 'Log in' })), box));
  }

  async function load(msg) {
    var sb = M.sb(), s = await sb.auth.getSession();
    if (!s.data.session) return login();
    var res = await Promise.all([sb.rpc('admin_list_enrolments'), sb.rpc('group_fill'), sb.from('groups').select('id,name,seats').order('id')]);
    if (res[0].error) {
      var forbidden = /forbidden|42501/.test(res[0].error.message + (res[0].error.code || ''));
      return M.mount(app, h('section', { class: 'card' }, h('h1', { text: forbidden ? 'Not an admin' : 'Error' }),
        h('p', { text: forbidden ? 'This login is not in the admins table. See portal/README.md.' : M.errText(res[0].error) }),
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
    var table = h('div', { class: 'scroll' }, h('table', { id: 'enrolments' },
      h('thead', null, h('tr', null, ['Reference', 'Child', 'Parent', 'Group', 'Method', 'Amount', 'Status', ''].map(function (x) { return h('th', { text: x }); }))),
      h('tbody', null, shown.map(function (r) {
        return h('tr', { 'data-enrolment': r.enrolment_id },
          h('td', { text: r.payment_reference }), h('td', { text: r.child_name || '(removed)' }),
          h('td', null, r.parent_name || '', h('br'), h('span', { class: 'small muted', text: (r.parent_email || '') + (r.parent_phone ? ' ' + r.parent_phone : '') })),
          h('td', { text: r.group_id }), h('td', { text: r.payment_method }), h('td', { text: M.money(r.amount_cents) }),
          h('td', null, h('span', { class: 'pill ' + r.payment_status, text: r.payment_status }), ' ', h('span', { class: 'pill ' + r.enrolment_status, text: r.enrolment_status.replace('_', ' ') })),
          h('td', null, r.payment_status === 'pending' && r.enrolment_status !== 'cancelled' ? h('button', { class: 'btn sm', type: 'button', 'data-mark-paid': r.payment_reference, text: 'Mark paid', onclick: async function () {
            if (!confirm('Mark ' + r.payment_reference + ' (' + M.money(r.amount_cents) + ') as paid? Check your bank first.')) return;
            var x = await M.sb().rpc('admin_mark_paid', { p_payment: r.payment_id, p_note: 'PayNow ticked by owner' });
            load(x.error ? M.errText(x.error) : 'Marked ' + r.payment_reference + ' paid.'); } }) : null));
      }))));
    M.mount(app, h('div', { class: 'row' }, h('h1', { text: 'Enrolments' }),
        h('button', { class: 'btn alt sm', type: 'button', id: 'signout', text: 'Log out', onclick: async function () { await M.sb().auth.signOut(); login(); } })),
      msg ? h('p', { class: 'msg info', text: msg }) : null, fillCard,
      h('section', { class: 'card' }, h('h2', { text: shown.length + ' shown' }), tabs, table));
  }
  load();
})();
