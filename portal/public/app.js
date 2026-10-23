/* Parent portal: sign up / log in, children, agreements, group choice, payment status, delete my data. */
(function () {
  var M = window.MI, h = M.h, app = document.getElementById('app');
  document.getElementById('top').appendChild(M.header('Parent portal'));
  var S = { session: null, parent: null, children: [], groups: [], fill: {}, enrols: [], consents: {}, tab: 'login', flash: null };

  var CONSENT_TEXT = [ // wording copied from privacy.html "Wording used on the registration form"
    ['contact', true, 'I agree to Math Inquirers (Preciouslyours Pte Ltd) using my details to arrange the class and contact me about it.'],
    ['terms', true, 'I have read the terms and refund policy and agree to them.'],
    ['recording', true, 'I agree that live lessons are recorded as described in the privacy notice, and that recordings are shared only with the enrolled families of my child\'s group.'],
    ['childs_work', true, 'I agree that Math Inquirers keeps photos of my child\'s work, practice answers and short progress notes, as described in the privacy notice. I am the parent or legal guardian of the child.'],
    ['feedback_quotes', false, '(Optional) I agree that my feedback may be used, without my child\'s name, to improve and describe the program.']
  ];

  function render(nodes) { M.clear(app); [].concat(nodes).forEach(function (n) { if (n) app.appendChild(n); }); }
  function flash(kind, text) { S.flash = text ? { kind: kind, text: text } : null; }
  function flashBox() { var b = h('div'); if (S.flash) M.notice(b, S.flash.kind, S.flash.text); return b; }
  async function run(fn, okText) {
    S.flash = null;
    try { await fn(); if (okText) flash('ok', okText); } catch (e) { flash('err', M.errText(e)); }
    await refresh();
  }

  // ---------------- data ----------------
  async function refresh() {
    var sb = M.sb();
    var r = await sb.auth.getSession();
    S.session = r.data && r.data.session;
    if (!S.session) { S.parent = null; return draw(); }
    try {
      var res = await Promise.all([
        sb.from('parents').select('id,email,full_name,phone,family_code').single(),
        sb.from('children').select('id,display_name,level').order('created_at'),
        sb.from('groups').select('id,level,name,ages,seats,sessions,first_label,last_label,fee_cents').order('id'),
        sb.rpc('group_fill'), sb.rpc('my_enrolments'), sb.rpc('my_consents')]);
      res.forEach(function (x) { if (x.error) throw x.error; });
      S.parent = res[0].data; S.children = res[1].data || []; S.groups = res[2].data || [];
      S.fill = {}; (res[3].data || []).forEach(function (f) { S.fill[f.group_id] = f; });
      S.enrols = res[4].data || [];
      S.consents = {}; (res[5].data || []).forEach(function (c) { S.consents[c.consent_type] = c; });
    } catch (e) { flash('err', M.errText(e)); }
    draw();
  }

  // ---------------- signed out ----------------
  function drawAuth() {
    var box = h('div');
    var email = h('input', { type: 'email', id: 'email', autocomplete: 'email', required: true });
    var pw = h('input', { type: 'password', id: 'password', autocomplete: S.tab === 'signup' ? 'new-password' : 'current-password', minlength: 8 });
    var name = h('input', { type: 'text', id: 'fullname', autocomplete: 'name', maxlength: 100 });
    var form = h('form', { novalidate: true, onsubmit: async function (ev) {
      ev.preventDefault(); var sb = M.sb(); var em = email.value.trim();
      if (!em) return M.notice(box, 'err', 'Please enter your email.');
      try {
        if (S.tab === 'magic') {
          var r = await sb.auth.signInWithOtp({ email: em, options: { emailRedirectTo: location.origin + '/portal/' } });
          if (r.error) throw r.error; return M.notice(box, 'ok', 'Check your email for a log-in link.');
        }
        if (pw.value.length < 8) return M.notice(box, 'err', 'Password needs at least 8 characters.');
        if (S.tab === 'signup') {
          if (!name.value.trim()) return M.notice(box, 'err', 'Please enter your name.');
          var s = await sb.auth.signUp({ email: em, password: pw.value, options: { data: { full_name: name.value.trim() }, emailRedirectTo: location.origin + '/portal/' } });
          if (s.error) throw s.error;
          if (!s.data.session) return M.notice(box, 'ok', 'Almost there: check your email and click the link to confirm your address, then log in.');
        } else {
          var l = await sb.auth.signInWithPassword({ email: em, password: pw.value });
          if (l.error) throw l.error;
        }
        await refresh();
      } catch (e) { M.notice(box, 'err', M.errText(e)); }
    } },
      S.tab === 'signup' ? h('p', null, h('label', { for: 'fullname', text: 'Your name (parent or guardian)' }), name) : null,
      h('p', null, h('label', { for: 'email', text: 'Email' }), email),
      S.tab !== 'magic' ? h('p', null, h('label', { for: 'password', text: 'Password' }), pw, h('span', { class: 'small muted', text: S.tab === 'signup' ? 'At least 8 characters.' : 'Forgot it? Use the "Magic link" tab to get a log-in link by email.' })) : null,
      S.tab === 'magic' ? h('p', { class: 'small muted', text: 'We email you a link. Click it on this device to log in, with no password.' }) : null,
      h('p', null, h('button', { class: 'btn', type: 'submit', text: { login: 'Log in', signup: 'Create parent account', magic: 'Email me a link' }[S.tab] })));
    var tabs = h('div', { class: 'tabs', role: 'group', 'aria-label': 'Account' }, ['login', 'signup', 'magic'].map(function (t) {
      return h('button', { type: 'button', 'aria-pressed': String(S.tab === t), text: { login: 'Log in', signup: 'Sign up', magic: 'Magic link' }[t],
        onclick: function () { S.tab = t; draw(); } });
    }));
    render([flashBox(), h('section', { class: 'card pop' },
      h('h1', { text: 'Parent portal' }),
      h('p', { class: 'muted', text: 'Parents create the account and add their child. Your child gets a display name and a PIN, with no email of their own.' }),
      tabs, form, box)]);
  }

  // ---------------- signed in ----------------
  function section(title, intro, id) { return h('section', { class: 'card', id: id },  h('h2', { text: title }), intro ? h('p', { class: 'muted small', text: intro }) : null); }
  function levelOptions(sel) {
    var ages = {}; S.groups.forEach(function (g) { ages[g.level] = g.ages; });
    return [1, 2, 3, 4, 5, 6].map(function (n) {
      return h('option', { value: n, selected: String(sel) === String(n) }, 'Level ' + n + (ages[n] ? ' (ages ' + ages[n] + ')' : ''));
    });
  }
  function hasActiveEnrol(childId) { return S.enrols.some(function (e) { return e.child_id === childId && e.enrolment_status !== 'cancelled'; }); }
  function requiredOk() { return CONSENT_TEXT.every(function (c) { return !c[1] || (S.consents[c[0]] && S.consents[c[0]].granted); }); }

  function childrenCard() {
    var c = section('My children', 'Use a first name or nickname. We do not collect photos, school or NRIC.', 'my-children');
    if (!S.children.length) c.appendChild(h('p', { class: 'empty muted', text: 'No children added yet. Add one below to get started.' }));
    S.children.forEach(function (ch) {
      var row = h('div', { class: 'child', 'data-child': ch.id });
      var show = function () {
        M.clear(row);
        row.appendChild(h('div', null, h('strong', { text: ch.display_name }), ' ', h('span', { class: 'pill', text: 'Level ' + ch.level })));
        row.appendChild(h('div', { class: 'row' },
          h('button', { class: 'btn alt sm', type: 'button', text: 'Edit', onclick: edit }),
          h('button', { class: 'btn alt sm', type: 'button', text: 'Remove', onclick: function () {
            if (confirm('Remove ' + ch.display_name + ' and their PIN?')) run(function () { return rpc('delete_child', { p_child: ch.id }); }, 'Removed.'); } })));
      };
      var edit = function () {
        M.clear(row);
        var n = h('input', { type: 'text', value: ch.display_name, maxlength: 30, 'aria-label': 'Display name' });
        var l = h('select', { 'aria-label': 'Level' }, levelOptions(ch.level));
        var p = h('input', { type: 'password', inputmode: 'numeric', pattern: '[0-9]*', maxlength: 6, autocomplete: 'off', placeholder: 'New PIN (optional)', 'aria-label': 'New PIN' });
        row.appendChild(h('div', { class: 'grid2', style: 'width:100%' }, n, l, p));
        row.appendChild(h('div', { class: 'row' },
          h('button', { class: 'btn sm', type: 'button', text: 'Save', onclick: function () {
            run(function () { return rpc('update_child', { p_child: ch.id, p_name: n.value, p_level: Number(l.value), p_pin: p.value || null }); }, 'Saved.'); } }),
          h('button', { class: 'btn alt sm', type: 'button', text: 'Cancel', onclick: show })));
      };
      show(); c.appendChild(row);
    });
    var n = h('input', { type: 'text', id: 'cname', maxlength: 30, required: true, autocomplete: 'off' });
    var l = h('select', { id: 'clevel' }, levelOptions(1));
    var p = h('input', { type: 'password', id: 'cpin', inputmode: 'numeric', pattern: '[0-9]*', maxlength: 6, autocomplete: 'off', required: true });
    c.appendChild(h('form', { novalidate: true, onsubmit: function (ev) {
      ev.preventDefault();
      if (!n.value.trim()) return run(async function () { throw M.say('Please enter a display name.'); });
      if (!/^[0-9]{4,6}$/.test(p.value)) return run(async function () { throw M.say('The PIN must be 4 to 6 digits.'); });
      run(function () { return rpc('add_child', { p_name: n.value, p_level: Number(l.value), p_pin: p.value }); }, 'Child added. Their PIN is saved securely (we cannot show it again).');
    } }, h('h3', { text: 'Add a child' }),
      h('div', { class: 'grid2' },
        h('p', null, h('label', { for: 'cname', text: 'Display name' }), n),
        h('p', null, h('label', { for: 'clevel', text: 'Level' }), l),
        h('p', null, h('label', { for: 'cpin', text: 'PIN (4 to 6 digits)' }), p)),
      h('button', { class: 'btn', type: 'submit', text: 'Add child' })));
    return c;
  }
  async function rpc(name, args) { var r = await M.sb().rpc(name, args); if (r.error) throw r.error; return r.data; }

  function familyCard() {
    return h('section', { class: 'card' }, h('h2', { text: 'Child sign-in' }),
      h('p', { class: 'small muted', text: 'Your child signs in with this family code, their display name and their PIN.' }),
      h('p', null, h('span', { class: 'code', id: 'family-code', text: S.parent.family_code })),
      h('a', { class: 'btn alt sm', href: '/portal/child/', text: 'Open the child sign-in page' }));
  }

  function consentCard() {
    var boxes = {}; var done = requiredOk();
    var c = section('Agreements', 'Read the ' + '' + 'terms and the privacy and recording notice first. The first four are needed to join a live recorded group; the last is optional. You can change your mind at any time.', 'agreements');
    c.appendChild(h('p', { class: 'small' }, h('a', { href: '/terms/', target: '_blank', rel: 'noopener', text: 'Terms and refund policy' }), ' | ',
      h('a', { href: '/privacy/', target: '_blank', rel: 'noopener', text: 'Privacy and recording notice' })));
    CONSENT_TEXT.forEach(function (t) {
      var cur = S.consents[t[0]];
      var cb = h('input', { type: 'checkbox', id: 'consent-' + t[0], checked: !!(cur && cur.granted) }); boxes[t[0]] = cb;
      c.appendChild(h('label', { class: 'consent', for: 'consent-' + t[0] }, cb, h('span', null, (t[1] ? 'Needed: ' : '') + t[2])));
    });
    var last = S.consents.terms || S.consents.contact;
    if (last) c.appendChild(h('p', { class: 'small muted', text: 'Last saved ' + M.fmtDate(last.created_at) + ' (terms ' + last.terms_version + ', privacy ' + last.privacy_version + ').' }));
    c.appendChild(h('button', { class: 'btn', type: 'button', id: 'save-consents', text: done ? 'Update agreements' : 'Save agreements', onclick: function () {
      var items = {}; CONSENT_TEXT.forEach(function (t) {
        var prev = S.consents[t[0]]; var now = boxes[t[0]].checked;
        if (!prev ? (now || t[1]) : prev.granted !== now) items[t[0]] = now;   // record first answer for all needed ones, then only changes
      });
      if (!Object.keys(items).length) return run(async function () {}, 'Nothing changed.');
      run(function () { return rpc('record_consents', { p_items: items, p_terms: M.VERSIONS.terms, p_privacy: M.VERSIONS.privacy }); }, 'Agreements saved.');
    } }));
    return c;
  }

  function enrolCard() {
    var c = section('Choose a group', 'Beta: 5 weeks, 10 lessons of 90 minutes (Singapore time), groups of up to 8.', 'choose-group');
    if (!S.children.length) { c.appendChild(h('p', { text: 'Add a child above first.' })); return c; }
    var any = false;
    S.children.forEach(function (ch) {
      if (hasActiveEnrol(ch.id)) return; any = true;
      var chosen = null; var btn;
      var wrap = h('div', { class: 'card', 'data-enrol-for': ch.id }, h('h3', { text: ch.display_name + ' (Level ' + ch.level + ')' }));
      var gs = S.groups.filter(function (g) { return g.level === ch.level; });
      if (!gs.length) wrap.appendChild(h('p', { class: 'muted', text: 'No group is open for this level yet.' }));
      gs.forEach(function (g) {
        var f = S.fill[g.id] || { seats: g.seats, taken: 0 }; var left = f.seats - f.taken;
        var r = h('input', { type: 'radio', name: 'grp-' + ch.id, value: g.id, disabled: left <= 0, onchange: function () { chosen = g.id; btn.disabled = !requiredOk(); } });
        wrap.appendChild(h('label', { class: 'opt' + (left <= 0 ? ' full' : '') }, r, h('span', null,
          h('strong', { text: g.name + ' (ages ' + g.ages + ')' }), h('br'),
          M.sessionsText(g.sessions), ', first lesson ' + g.first_label + ', last ' + g.last_label, h('br'),
          h('span', { class: 'small muted', text: (left <= 0 ? 'Full' : left + ' of ' + f.seats + ' seats left') + ' | ' + M.money(g.fee_cents) + ' for all 10 lessons' }))));
      });
      btn = h('button', { class: 'btn', type: 'button', disabled: true, text: 'Reserve a place', onclick: function () {
        if (chosen) run(function () { return rpc('enrol_child', { p_child: ch.id, p_group: chosen }); }, 'Place reserved. Please pay to confirm it (see Payments below).'); } });
      wrap.appendChild(btn);
      if (!requiredOk()) wrap.appendChild(h('p', { class: 'small', text: 'Save the four needed agreements first.' }));
      c.appendChild(wrap);
    });
    if (!any) c.appendChild(h('p', { text: 'Every child already has a place or a reservation.' }));
    return c;
  }

  function paymentCard() {
    var c = section('Places and payments', null, 'payments');
    if (!S.enrols.length) { c.appendChild(h('p', { class: 'muted', text: 'Nothing reserved yet.' })); return c; }
    S.enrols.forEach(function (e) {
      var g = S.groups.filter(function (x) { return x.id === e.group_id; })[0];
      var d = h('div', { class: 'card', 'data-enrolment': e.enrolment_id },
        h('div', { class: 'row' }, h('strong', { text: e.child_name + ' | ' + (g ? g.name : e.group_id) }),
          h('span', { class: 'pill ' + e.enrolment_status, text: e.enrolment_status.replace('_', ' ') }),
          h('span', { class: 'pill ' + e.payment_status, 'data-pay-status': '1', text: 'payment ' + e.payment_status })),
        h('p', { text: 'Fee ' + M.money(e.amount_cents) + (e.paid_at ? ', paid ' + M.fmtDate(e.paid_at) : '') }));
      if (e.payment_status === 'pending') {
        if (M.CFG.PAYMENT_MODE === 'stripe') {
          d.appendChild(h('button', { class: 'btn', type: 'button', text: 'Pay ' + M.money(e.amount_cents) + ' online (card or PayNow)', 'data-pay-online': '1', onclick: function (ev) { payOnline(e.enrolment_id, d, ev.currentTarget); } }));
        } else {
          d.appendChild(h('div', { class: 'msg info' },
            h('div', null, 'Pay ' + M.money(e.amount_cents) + ' by PayNow to ' + M.CFG.PAYNOW_TO + '.'),
            h('div', null, 'Put this reference in the PayNow comment: ', h('span', { class: 'code', 'data-ref': '1', text: e.payment_reference })),
            h('div', { class: 'small', text: 'We tick it off by hand, usually within a day. This page will then show "paid" and your place becomes confirmed.' })));
        }
        if (e.enrolment_status === 'pending_payment') d.appendChild(h('button', { class: 'btn alt sm', type: 'button', text: 'Cancel this reservation', onclick: function () {
          if (confirm('Cancel this reservation and release the seat?')) run(function () { return rpc('cancel_my_enrolment', { p_enrolment: e.enrolment_id }); }, 'Reservation cancelled.'); } }));
      } else if (e.payment_status === 'paid') {
        d.appendChild(h('p', { class: 'small muted', text: 'Reference ' + e.payment_reference + '. To cancel or ask for a refund, message us (see the terms).' }));
      }
      c.appendChild(d);
    });
    return c;
  }
  async function payOnline(enrolmentId, box, btn) {
    if (btn) { btn.disabled = true; btn.textContent = 'Opening secure payment page...'; }
    try {
      var tok = S.session.access_token;
      var r = await fetch('/api/stripe-create-checkout', { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + tok }, body: JSON.stringify({ enrolment_id: enrolmentId }) });
      var j = await r.json().catch(function () { return {}; });
      if (!r.ok || !j.url) throw M.say('Could not start the payment. Nothing was charged. Please try again.');
      location.href = j.url;   // top-level redirect to Stripe Checkout; card details never touch our pages
    } catch (e) { if (btn) { btn.disabled = false; btn.textContent = 'Try again'; } M.notice(box.appendChild(h('div')), 'err', M.errText(e)); }
  }

  function accountCard() {
    var c = section('Your details and data', null, 'details');
    var nm = h('input', { type: 'text', id: 'pname', value: S.parent.full_name || '', maxlength: 100 });
    var ph = h('input', { type: 'tel', id: 'pphone', value: S.parent.phone || '', maxlength: 30, autocomplete: 'tel' });
    c.appendChild(h('form', { novalidate: true, onsubmit: function (ev) { ev.preventDefault();
      run(async function () { var r = await M.sb().from('parents').update({ full_name: nm.value.trim() || null, phone: ph.value.trim() || null }).eq('id', S.parent.id); if (r.error) throw r.error; }, 'Details saved.'); } },
      h('div', { class: 'grid2' }, h('p', null, h('label', { for: 'pname', text: 'Name' }), nm), h('p', null, h('label', { for: 'pphone', text: 'Phone (optional)' }), ph)),
      h('p', { class: 'small muted', text: 'Signed in as ' + S.parent.email }), h('button', { class: 'btn alt', type: 'submit', text: 'Save details' })));
    var d = h('details', null, h('summary', { text: 'Delete my data' }),
      h('p', { class: 'small', text: 'This removes your children, their PINs and practice data, strips your name, email and phone, cancels open places and deletes your login. Payment and agreement records are kept without your details for the period in the privacy notice. If you have paid, we will refund as the terms say.' }));
    var t = h('input', { type: 'text', id: 'del-confirm', placeholder: 'Type DELETE', autocomplete: 'off', 'aria-label': 'Type DELETE to confirm' });
    d.appendChild(t);
    d.appendChild(h('p', null, h('button', { class: 'btn danger', type: 'button', id: 'del-btn', text: 'Delete everything', onclick: async function () {
      if (t.value.trim() !== 'DELETE') return run(async function () { throw M.say('Type DELETE in the box to confirm.'); });
      try { await rpc('delete_my_data', {}); await M.sb().auth.signOut(); flash('ok', 'Your data has been deleted.'); } catch (e) { flash('err', M.errText(e)); }
      await refresh();
    } })));
    c.appendChild(d);
    return c;
  }

  function nextStep() {
    var live = S.enrols.filter(function (e) { return e.enrolment_status !== 'cancelled'; });
    var pend = live.filter(function (e) { return e.payment_status === 'pending'; });
    var t, href;
    if (pend.length) { t = 'Next step: pay for the reserved place to confirm it.'; href = '#payments'; }
    else if (!S.children.length) { t = 'Next step: add your child.'; href = '#my-children'; }
    else if (!requiredOk()) { t = 'Next step: save the four needed agreements.'; href = '#agreements'; }
    else if (S.children.some(function (c) { return !hasActiveEnrol(c.id); })) { t = 'Next step: choose a group and reserve a place.'; href = '#choose-group'; }
    else { t = 'You are all set for now.'; }
    return h('p', { class: 'msg info next', id: 'next-step' }, t, href ? ' ' : null, href ? h('a', { href: href, text: 'Go there' }) : null);
  }
  function draw() {
    if (!M.configured()) return render(h('section', { class: 'card pop' }, h('h1', { text: 'Portal not set up yet' }), h('p', { text: 'The owner still needs to put the Supabase URL and anon key in portal/config.js (see portal/README.md).' })));
    if (S.session && !S.parent) return render([flashBox(), h('section', { class: 'card pop' }, h('h1', { text: 'We could not load your account' }),
      h('p', { text: 'This is usually a weak connection. Your details are safe. Try again, or log out and log back in.' }),
      h('div', { class: 'row' }, h('button', { class: 'btn', type: 'button', id: 'retry', text: 'Try again', onclick: function () { flash(null); refresh(); } }),
        h('button', { class: 'btn alt', type: 'button', id: 'signout', text: 'Log out', onclick: async function () { await M.sb().auth.signOut(); flash(null); await refresh(); } })))]);
    if (!S.session) return drawAuth();
    var q = new URLSearchParams(location.search);
    var back = q.get('paid') ? h('div', { class: 'msg info', 'data-return': 'paid', text: 'Thanks. We confirm your place when Stripe tells us the payment has gone through. For a card this takes a few seconds; PayNow can take a little longer. Refresh this page in a minute if it still says pending.' })
      : q.get('cancelled') ? h('div', { class: 'msg info', 'data-return': 'cancelled', text: 'Payment cancelled, nothing was charged. Your place is still held while payment is pending; use the Pay button below to try again.' }) : null;
    render([flashBox(), back, nextStep(),
      h('div', { class: 'row' }, h('h1', { text: 'Hello' + (S.parent.full_name ? ', ' + S.parent.full_name : '') }),
        h('button', { class: 'btn alt sm', type: 'button', id: 'signout', text: 'Log out', onclick: async function () { await M.sb().auth.signOut(); flash(null); await refresh(); } })),
      paymentCard(), childrenCard(), consentCard(), enrolCard(), familyCard(), accountCard()]);
  }

  if (!M.configured()) return draw();
  M.sb().auth.onAuthStateChange(function (ev) { if (ev === 'SIGNED_IN' || ev === 'SIGNED_OUT') refresh(); });
  refresh();
})();
