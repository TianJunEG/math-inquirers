/* Trial class request for a parent, with or without an enrolment. Creates a trial_requests row through request_trial() (needs only the "contact"
   and "terms" agreements; the optional marketing agreement is separate and never pre-ticked). Booking the slot itself is a follow-up by the owner.
   Parents only: a child never sees this page. No countdowns, no scarcity wording. */
(function () {
  var M = window.MI, h = M.h, P = M.P, app = document.getElementById('app'), S = P.state;
  document.getElementById('top').appendChild(M.header('Trial class'));
  var q = new URLSearchParams(location.search);
  var SOURCES = ['book', 'post_purchase', 'after_submit', 'report', 'website', 'other'];
  var source = SOURCES.indexOf(q.get('from')) >= 0 ? q.get('from') : 'other';
  var TIMES = [['weekday-afternoon', 'Weekday afternoons'], ['weekday-evening', 'Weekday evenings'], ['weekend-morning', 'Weekend mornings'], ['weekend-afternoon', 'Weekend afternoons']];
  var F = { child: q.get('child') || '', level: 0, times: {}, note: '', phone: '', savePhone: false, ticks: {} }, D = { reqs: [], missing: false, done: false }, flashMsg = null, ready = false;
  var STATUS = { new: 'received', contacted: 'we have been in touch', attended: 'attended', enrolled: 'joined a class', declined: 'not going ahead', withdrawn: 'withdrawn' };
  function flash(kind, text) { flashMsg = text ? { kind: kind, text: text } : null; }
  // keep keyboard focus on the same control across a redraw (clearing the container would drop it to <body>)
  function draw(nodes) { var k = M.focusKey(app); M.clear(app); [].concat(nodes).forEach(function (n) { if (n) app.appendChild(n); }); M.focusRestore(app, k); }
  // after every action the result message (or the page heading) takes keyboard focus and is announced
  async function run(fn, ok) { flash(null); try { await fn(); if (ok) flash('ok', ok); } catch (e) { flash('err', M.errText(e)); } await refresh(); M.focusResult(app); }
  function childById(id) { return S.children.filter(function (c) { return c.id === id; })[0]; }

  async function refresh() {
    try {
      await P.load();
      if (S.session) {
        var r = await M.sb().from('trial_requests').select('*').order('created_at', { ascending: false });
        if (r.error) { if (P.isMissingSql(r.error)) D.missing = true; else throw r.error; } else { D.missing = false; D.reqs = r.data || []; }
        if (!childById(F.child)) F.child = '';
        if (!F.level) F.level = (childById(F.child) || S.children[0] || { level: 1 }).level;
        if (!F.phone && S.parent && S.parent.phone) F.phone = S.parent.phone;
      }
    } catch (e) { flash('err', M.errText(e)); }
    ready = true; paint();
  }

  async function submit(ev) {
    ev.preventDefault();
    var got = lines.collect();
    if (!got.ok) return run(async function () { throw M.say(got.problem); });
    var prefs = TIMES.filter(function (t) { return F.times[t[0]]; }).map(function (t) { return t[0]; });
    flash(null);
    try {
      await P.saveConsents(got.items);
      // The account phone is changed only when there is none yet, or the parent ticked the box. Otherwise a different number typed here goes into this request's note only.
      var typed = F.phone.trim(), note = F.note.trim();
      if (typed !== (S.parent.phone || '')) {
        if (!S.parent.phone || F.savePhone) {
          var u = await M.sb().from('parents').update({ phone: typed || null }).eq('id', S.parent.id); if (u.error) throw u.error;
        } else if (typed) note = (note ? note + ' | ' : '') + 'phone for this request: ' + typed;
      }
      await M.rpc('request_trial', { p_child: F.child || null, p_level: F.level, p_preferred: prefs, p_note: note.slice(0, 300) || null, p_source: source });
      D.done = true; F.note = ''; F.times = {};
    } catch (e) { flash('err', M.errText(e)); }
    await refresh();
    M.focusResult(app);
  }

  var lines = null;
  function requestForm() {
    lines = P.consentLines(['contact', 'terms'], ['marketing_contact'], F.ticks);
    var kids = S.children.length ? h('p', null, h('label', { for: 'trial-child', text: 'Which child is it for? (optional)' }),
      h('select', { id: 'trial-child', onchange: function (e) { F.child = e.target.value; var c = childById(F.child); if (c) F.level = c.level; paint(); } },
        [h('option', { value: '', selected: !F.child }, 'Not sure yet')].concat(S.children.map(function (c) { return h('option', { value: c.id, selected: F.child === c.id }, c.display_name + ' (Level ' + c.level + ')'); })))) : null;
    return h('form', { novalidate: true, id: 'trial-form', onsubmit: submit },
      kids,
      h('p', null, h('label', { for: 'trial-level', text: 'Which level would you like to try?' }),
        h('select', { id: 'trial-level', onchange: function (e) { F.level = Number(e.target.value); } }, P.levelOptions(F.level))),
      h('fieldset', null, h('legend', { text: 'Times that could suit you (tick any)' }),
        TIMES.map(function (t) {
          return h('label', { class: 'consent', for: 'time-' + t[0] }, h('input', { type: 'checkbox', id: 'time-' + t[0], checked: !!F.times[t[0]], onchange: function (e) { F.times[t[0]] = e.target.checked; } }), h('span', { text: t[1] }));
        }), h('p', { class: 'small muted', text: 'These are only wishes. We will talk to you about real times.' })),
      h('p', null, h('label', { for: 'trial-phone', text: 'Phone or WhatsApp (optional)' }), h('input', { type: 'tel', id: 'trial-phone', maxlength: 30, autocomplete: 'tel', value: F.phone, oninput: function (e) { F.phone = e.target.value; } }),
        h('span', { class: 'small muted', text: 'We will reply to ' + S.parent.email + ' unless you add a number.' }),
        S.parent.phone ? h('span', { class: 'consent', style: 'margin-top:8px' }, h('input', { type: 'checkbox', id: 'trial-savephone', checked: F.savePhone, onchange: function (e) { F.savePhone = e.target.checked; } }),
          h('label', { for: 'trial-savephone', class: 'inline', text: 'If I typed a different number, also change the phone saved on my account' })) : null),
      h('p', null, h('label', { for: 'trial-note', text: 'Anything you would like us to know? (optional, up to 300 characters)' }),
        h('textarea', { id: 'trial-note', maxlength: 300, rows: 3, oninput: function (e) { F.note = e.target.value; } }, F.note)),
      lines.missing.length || ['marketing_contact'].some(function (t) { return !P.granted(t); }) ? h('fieldset', { id: 'agree-box' }, h('legend', { text: 'Agreements' }), P.legalLinks(), lines.node,
        h('p', { class: 'small muted', text: 'Only the first two are needed to ask for a trial class. The optional one lets us message you first with a suggestion later; leave it empty if you prefer.' })) : null,
      h('p', null, h('button', { class: 'btn', type: 'submit', id: 'send-trial', text: 'Send my request' }),
        h('span', { class: 'small muted', text: ' No payment, no obligation. You can withdraw the request below at any time.' })));
  }

  function reqCard(r) {
    var c = childById(r.child_id);
    return h('div', { class: 'card', 'data-trial': r.id },
      h('div', { class: 'row' }, h('strong', { text: 'Level ' + r.level + (c ? ' for ' + c.display_name : '') }), h('span', { class: 'pill ' + r.status, 'data-trial-status': r.id, text: STATUS[r.status] || r.status })),
      h('p', { class: 'small muted', text: 'Sent ' + M.dayText(r.created_at) + (r.preferred && r.preferred.length ? ' | times: ' + r.preferred.join(', ') : '') }),
      r.status === 'new' ? h('button', { class: 'btn alt sm', type: 'button', 'data-withdraw': r.id, text: 'Withdraw this request', onclick: function () {
        run(function () { return M.rpc('withdraw_trial_request', { p_id: r.id }); }, 'Request withdrawn.'); } }) : null);
  }

  function paint() {
    if (!M.configured()) return draw(P.notReady());
    var fb = h('div'); if (flashMsg) M.notice(fb, flashMsg.kind, flashMsg.text);
    if (!ready) return draw(h('p', { class: 'muted', text: 'Loading...' }));
    if (!S.session) return draw([fb, P.signedOut('Log in or create a parent account to ask about a trial class. You do not need to be enrolled.')]);
    if (!S.parent) return draw([fb, h('section', { class: 'card' }, h('p', { text: 'We could not load your account. Please reload the page.' }))]);
    if (D.missing) return draw([P.nav('trial'), P.missingSql()]);
    var out = [fb, h('div', { class: 'row' }, h('h1', { text: 'Ask about a trial class' }), P.signOutButton(function () { flash(null); refresh(); })), P.nav('trial')];
    if (D.done) {
      D.done = false;
      out.push(h('section', { class: 'card pop', id: 'trial-done' }, h('h2', { text: 'Thank you, we have your request' }),
        h('p', { text: 'We will get in touch by email (or the number you gave) to talk about times and what a trial looks like. There is nothing to pay now.' })));
    }
    out.push(h('section', { class: 'card' }, h('h2', { text: 'A trial class' }),
      h('p', { class: 'muted', text: 'For parents. Tell us the level and some times that could suit you, and we will be in touch to talk it through. It is fine to ask even if your child has only used a workbook, and you do not need an enrolment.' }),
      requestForm()));
    out.push(h('section', { class: 'card', id: 'trial-list' }, h('h2', { text: 'Your requests' }),
      D.reqs.length ? D.reqs.map(reqCard) : h('p', { class: 'muted empty', 'data-no-trials': '1', text: 'No requests yet.' })));
    draw(out);
  }

  if (!M.configured()) return paint();
  M.sb().auth.onAuthStateChange(function (ev) { if (ev === 'SIGNED_OUT') refresh(); });
  refresh();
})();
