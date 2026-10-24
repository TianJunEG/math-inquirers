/* Shared pieces of the parent pages (children dashboard, extension books, trial class request, and the add-child form on the home page).
   Loaded after common.js. No innerHTML anywhere: all text goes through textContent. */
(function () {
  var M = window.MI, h = M.h;
  var P = M.P = { state: { session: null, parent: null, children: [], consents: {} } };

  // Session, parent, children (with the optional birth year) and the latest answer for each agreement.
  P.load = async function () {
    var S = P.state, sb = M.sb(), r = await sb.auth.getSession();
    S.session = r.data && r.data.session;
    if (!S.session) { S.parent = null; S.children = []; S.consents = {}; return S; }
    var res = await Promise.all([
      sb.from('parents').select('id,email,full_name,phone,family_code').single(),
      sb.from('children').select('id,display_name,level,birth_year').order('created_at'),
      sb.rpc('my_consents')]);
    res.forEach(function (x) { if (x.error) throw x.error; });
    S.parent = res[0].data; S.children = res[1].data || [];
    S.consents = {}; (res[2].data || []).forEach(function (c) { S.consents[c.consent_type] = c; });
    await P.loadAlerts();
    return S;
  };
  // PIN lock alerts for the dashboard (my_pin_alerts). If the SQL is not applied yet, or anything fails, there simply are no alerts.
  P.loadAlerts = async function () {
    try { var r = await M.sb().rpc('my_pin_alerts'); P.state.alerts = r.error ? [] : (r.data || []); } catch (e) { P.state.alerts = []; }
    return P.state.alerts;
  };
  // "Anna was locked out of sign-in ..." shown to the parent until they press "Got it" (or set a new PIN). run(fn, okText) is the page's action runner.
  P.alertsCard = function (run) {
    var a = P.state.alerts || [];
    if (!a.length) return null;
    var names = {}; a.forEach(function (x) { names[x.child_name] = true; });
    var latest = a[0], who = Object.keys(names).join(', ');
    return h('section', { class: 'card', id: 'pin-alerts', role: 'region', 'aria-label': 'Sign-in lock alerts' },
      h('h2', { text: 'Someone typed a wrong PIN several times' }),
      h('p', { class: 'msg warn', text: who + (Object.keys(names).length > 1 ? ' were' : ' was') + ' locked out of child sign-in after several wrong PINs (' + a.length + (a.length === 1 ? ' time' : ' times') + ', most recently ' + M.fmtDate(latest.locked_at) + (latest.still_locked ? '; locked until ' + M.fmtDate(latest.locked_until) : '') + '). If it was your child, they can try again when the lock ends. If it was not, please choose a new PIN: press Edit under My children and type a new one.' }),
      h('button', { class: 'btn alt sm', type: 'button', id: 'dismiss-alerts', text: 'Got it', onclick: function () { run(function () { return M.rpc('dismiss_pin_alerts', {}); }, 'Okay, hidden.'); } }));
  };
  // Mirrors the database rule (_pin_check in schema.sql) so the family sees the reason before anything is sent: the same digit repeated, a run up or down,
  // a repeated pair or triple, a few very common PINs, and birth-year patterns. The database enforces it again.
  P.weakPin = function (p) {
    return /^(.)\1+$/.test(p) || '01234567890'.indexOf(p) >= 0 || '09876543210'.indexOf(p) >= 0 || /^(..)\1+$/.test(p) || /^(...)\1$/.test(p)
      || ['2580', '0852', '1004', '1010', '1122', '1313', '2000', '2001', '6969', '7410', '8520', '1230', '3210', '123321', '112233', '121314', '654321'].indexOf(p) >= 0
      || /^(19[4-9][0-9]|20[0-3][0-9])$/.test(p) || /^(19[4-9][0-9]|20[0-3][0-9])(0[1-9]|1[0-2])$/.test(p) || /^(0[1-9]|1[0-2])(19[4-9][0-9]|20[0-3][0-9])$/.test(p);
  };
  P.granted = function (type) { var c = P.state.consents[type]; return !!(c && c.granted); };

  P.nav = function (active) {
    return h('nav', { class: 'tabs', 'aria-label': 'Portal pages' }, [
      ['home', '/portal/', 'Home'], ['children', '/portal/children/', 'My children'], ['books', '/portal/books/', 'Extension books'], ['trial', '/portal/trial/', 'Trial class']
    ].map(function (x) { return h('a', { href: x[1], 'aria-current': active === x[0] ? 'page' : null, text: x[2] }); }));
  };

  P.signedOut = function (why) {
    return h('section', { class: 'card pop', id: 'signed-out' }, h('h1', { text: 'Please log in first' }),
      h('p', { class: 'muted', text: why || 'This page is for parents. Log in, or create a parent account (it takes a minute and you do not need to join a class).' }),
      h('a', { class: 'btn', id: 'to-login', href: '/portal/', text: 'Log in or sign up' }));
  };

  P.notReady = function () {
    return h('section', { class: 'card pop' }, h('h1', { text: 'Portal not set up yet' }),
      h('p', { text: 'The owner still needs to put the Supabase URL and anon key in portal/config.js (see portal/README.md).' }));
  };

  // When the screens' SQL (portal/supabase/portal_ui.sql) has not been applied, say so kindly instead of showing an error code.
  P.isMissingSql = function (e) { return /PGRST202|42883|does not exist|schema cache|Could not find the function/i.test(String((e && (e.message || e.code)) || '') + String((e && e.code) || '')); };
  P.missingSql = function () {
    return h('section', { class: 'card' }, h('h2', { text: 'This page is not switched on yet' }),
      h('p', { text: 'The owner still needs to add the database pieces for this page (portal/supabase/portal_ui.sql). Nothing is wrong with your account.' }));
  };

  P.yearOptions = function (sel) {
    var y = new Date().getFullYear(), out = [h('option', { value: '', selected: !sel }, 'Prefer not to say')];
    for (var i = 3; i <= 18; i++) out.push(h('option', { value: y - i, selected: String(sel) === String(y - i) }, String(y - i)));
    return out;
  };
  P.levelOptions = function (sel, ages) {
    return [1, 2, 3, 4, 5, 6].map(function (n) {
      return h('option', { value: n, selected: String(sel) === String(n) }, 'Level ' + n + (ages && ages[n] ? ' (ages ' + ages[n] + ')' : ''));
    });
  };

  /* Add-a-child form. opts: { run(fn, okText), ages, onFlash, defaultLevel, submitText }.
     Works for families with NO enrolment. Display name = first name or nickname; the birth year is optional. */
  P.childForm = function (opts) {
    opts = opts || {};
    var n = h('input', { type: 'text', id: 'cname', maxlength: 30, required: true, autocomplete: 'off' });
    var by = h('select', { id: 'cbirth' }, P.yearOptions(''));
    var l = h('select', { id: 'clevel' }, P.levelOptions(opts.defaultLevel || 1, opts.ages));
    var p = h('input', { type: 'password', id: 'cpin', inputmode: 'numeric', pattern: '[0-9]*', maxlength: 6, autocomplete: 'off', required: true });
    var note = h('div');
    return h('form', { novalidate: true, id: 'add-child-form', onsubmit: function (ev) {
      ev.preventDefault();
      if (!n.value.trim()) { M.notice(note, 'err', 'Please enter a first name or nickname.'); return n.focus(); }
      if (!/^[0-9]{4,6}$/.test(p.value)) { M.notice(note, 'err', 'The PIN must be 4 to 6 digits.'); return p.focus(); }   // checked here so what was typed is not lost
      if (P.weakPin(p.value)) { M.notice(note, 'err', M.errText(new Error('pin_weak'))); return p.focus(); }
      var year = by.value ? Number(by.value) : null;
      opts.run(function () {
        return year ? M.rpc('add_child_profile', { p_name: n.value, p_level: Number(l.value), p_pin: p.value, p_birth_year: year })
                    : M.rpc('add_child', { p_name: n.value, p_level: Number(l.value), p_pin: p.value });
      }, 'Child added. Their PIN is saved securely (we cannot show it again).');
    } },
      h('h3', { text: opts.title || 'Add a child' }),
      h('p', { class: 'small muted', text: 'Use a first name or a nickname. We do not ask for photos, school or NRIC. The PIN is what your child types to sign in; we store it scrambled and cannot show it again.' }),
      h('div', { class: 'grid2' },
        h('p', null, h('label', { for: 'cname', text: 'First name or nickname' }), n),
        h('p', null, h('label', { for: 'cbirth', text: 'Birth year (optional)' }), by),
        h('p', null, h('label', { for: 'clevel', text: 'Level' }), l),
        h('p', null, h('label', { for: 'cpin', text: 'PIN (4 to 6 digits)' }), p)),
      note, h('button', { class: 'btn', type: 'submit', text: opts.submitText || 'Add child' }));
  };

  /* Agreement tick-boxes for the types not yet granted. Returns { node, missing, collect() }.
     collect() returns { ok, items, problem }: ok is false when a needed one is not ticked; items is ready for record_consents. */
  P.consentLines = function (types, optional, state) {
    optional = optional || []; state = state || {};
    var boxes = {}, missing = types.filter(function (t) { return !P.granted(t); }), opt = optional.filter(function (t) { return !P.granted(t); });
    var node = h('div', { class: 'consents' });
    missing.concat(opt).forEach(function (t) {
      var cb = h('input', { type: 'checkbox', id: 'need-' + t, checked: !!state[t], onchange: function (e) { state[t] = e.target.checked; } }); boxes[t] = cb;
      node.appendChild(h('label', { class: 'consent', for: 'need-' + t }, cb, h('span', null, (missing.indexOf(t) >= 0 ? 'Needed: ' : '') + M.CONSENTS[t])));
    });
    return { node: node, missing: missing, collect: function () {
      var items = {}, bad = null;
      missing.forEach(function (t) { if (boxes[t].checked) items[t] = true; else if (!bad) bad = t; });
      opt.forEach(function (t) { if (boxes[t].checked) items[t] = true; });
      return { ok: !bad, items: items, problem: bad ? 'Please tick the agreements marked "Needed" to go on. You can read the terms and privacy notice first.' : null };
    } };
  };
  P.saveConsents = function (items) {
    if (!Object.keys(items).length) return Promise.resolve();
    return M.rpc('record_consents', { p_items: items, p_terms: M.VERSIONS.terms, p_privacy: M.VERSIONS.privacy });
  };
  P.legalLinks = function () {
    return h('p', { class: 'small legal' }, h('a', { href: '/terms/', target: '_blank', rel: 'noopener', text: 'Terms and refund policy' }),
      h('a', { href: '/privacy/', target: '_blank', rel: 'noopener', text: 'Privacy and recording notice' }));
  };

  P.signOutButton = function (after) {
    return h('button', { class: 'btn alt sm', type: 'button', id: 'signout', text: 'Log out', onclick: async function () { await M.sb().auth.signOut(); if (after) after(); } });
  };
})();
