/* Shared helpers for the portal pages. No innerHTML anywhere: all text goes through textContent. */
(function () {
  var CFG = window.MI_CONFIG || {};
  // Bump these whenever the text of terms.html / privacy.html changes: they are stored with every consent record.
  var VERSIONS = { terms: 'terms-2026-10b-draft', privacy: 'privacy-2026-10b-draft' };

  function h(tag, attrs) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      var v = attrs[k];
      if (v == null || v === false) return;
      if (k === 'class') e.className = v;
      else if (k.slice(0, 2) === 'on') e.addEventListener(k.slice(2), v);
      else if (k === 'text') e.textContent = v;
      else e.setAttribute(k, v === true ? '' : v);
    });
    for (var i = 2; i < arguments.length; i++) add(e, arguments[i]);
    return e;
  }
  function add(e, c) {
    if (c == null || c === false) return;
    if (Array.isArray(c)) c.forEach(function (x) { add(e, x); });
    else e.appendChild(typeof c === 'object' ? c : document.createTextNode(String(c)));
  }
  function mount(e) { clear(e); for (var i = 1; i < arguments.length; i++) add(e, arguments[i]); return e; }
  function clear(e) { while (e.firstChild) e.removeChild(e.firstChild); return e; }

  function configured() {
    return CFG.SUPABASE_URL && CFG.ANON_KEY && CFG.SUPABASE_URL !== 'SUPABASE_URL' && CFG.ANON_KEY !== 'ANON_KEY';
  }
  var client = null;
  function sb() {
    if (!client) client = window.supabase.createClient(CFG.SUPABASE_URL, CFG.ANON_KEY, { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true } });
    return client;
  }
  var MESSAGES = {
    group_full: 'Sorry, that group is full.',
    level_mismatch: 'That group is for a different level.',
    already_enrolled: 'This child already has a place.',
    pin_format: 'The PIN must be 4 to 6 digits.',
    too_many_children: 'You can add up to 6 children.',
    level_locked_by_enrolment: 'The level cannot change while the child has a place in a group. Cancel the place first.',
    cancel_enrolment_first: 'Cancel this child\'s place first.',
    cannot_cancel_contact_us: 'This place is already paid, so please message us to cancel.',
    forbidden: 'This page is for the owner only.',
    not_signed_in: 'Please log in again.'
  };
  function errText(err) {
    var m = (err && (err.message || err.error_description)) || String(err || 'Something went wrong');
    if (/consents_missing/.test(m)) return 'Please tick and save the four needed agreements first.';
    if (/duplicate key|children_parent_name_uq/.test(m)) return 'You already have a child with that name. Use a different display name.';
    for (var k in MESSAGES) if (m.indexOf(k) !== -1) return MESSAGES[k];
    if (/Invalid login/i.test(m)) return 'Email or password is not right.';
    return m.length > 160 ? 'Something went wrong. Please try again.' : m;
  }
  function money(cents) { return 'S$' + (cents / 100).toFixed(2); }
  function sessionsText(sessions) {
    return (sessions || []).map(function (s) { return s.day + ' ' + s.start + '-' + s.end; }).join(' and ');
  }
  function fmtDate(iso) {
    try { return new Date(iso).toLocaleString('en-SG', { timeZone: 'Asia/Singapore', dateStyle: 'medium', timeStyle: 'short' }); } catch (e) { return iso; }
  }
  function notice(box, kind, text) {
    clear(box); if (text) box.appendChild(h('p', { class: 'msg ' + kind, role: kind === 'err' ? 'alert' : 'status', text: text }));
  }
  function themeInit() {
    try { var t = localStorage.getItem('mi-theme'); if (t) document.documentElement.setAttribute('data-theme', t); } catch (e) {}
  }
  themeInit();
  function header(subtitle) {
    return h('header', { class: 'top' },
      h('a', { class: 'brand', href: '/' }, h('i', { text: '?' }), h('span', { text: CFG.SITE_NAME || 'Math Inquirers' })),
      h('span', { class: 'sub', text: subtitle || '' }));
  }
  window.MI = { h: h, mount: mount, clear: clear, configured: configured, sb: sb, errText: errText, money: money, sessionsText: sessionsText,
                fmtDate: fmtDate, notice: notice, header: header, CFG: CFG, VERSIONS: VERSIONS };
})();
