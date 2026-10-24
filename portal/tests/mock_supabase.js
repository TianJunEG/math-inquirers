/* In-memory stand-in for supabase-js + the SQL functions, for Playwright tests ONLY (never shipped: it lives in tests/).
   State persists in localStorage so it survives page navigations. It re-implements the *behaviour* the SQL functions have
   (checked separately against real Postgres by supabase/test/run_sql_test.sh); it cannot prove the SQL is right. */
(function () {
  var KEY = 'mock-db';
  var seed = window.__SEED__ || { groups: [] };
  function load() { try { var s = localStorage.getItem(KEY); if (s) return JSON.parse(s); } catch (e) {} return { users: [], parents: [], children: [], enrolments: [], payments: [], consents: [], groups: seed.groups, extraTaken: seed.extraTaken || {}, session: null, n: 0 }; }
  var db = load(); function save() { localStorage.setItem(KEY, JSON.stringify(db)); }
  // portal screens (ext orders, access, trial requests, child sessions, submissions) and the seeded units/prices; created on first use
  ['ext_orders', 'access', 'trials', 'child_sessions', 'submissions', 'attempts'].forEach(function (k) { if (!db[k]) db[k] = []; });
  if (!db.units) db.units = seed.units || [];
  if (!db.prices) db.prices = seed.prices || {};
  if (!db.report) db.report = {};
  if (!db.previews) db.previews = seed.previews || [];
  window.__mockSave = save;
  function id(p) { db.n++; return p + '-' + db.n; }
  function code(n) { var a = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789', s = ''; for (var i = 0; i < n; i++) s += a[Math.floor(Math.random() * a.length)]; return s; }
  function err(m) { return { message: m }; }
  function me() { return db.session && db.users.filter(function (u) { return u.id === db.session.user.id; })[0]; }
  function isAdmin() { var u = me(); return u && u.email === 'owner@example.com'; }
  function taken(gid) { return (db.extraTaken[gid] || 0) + db.enrolments.filter(function (e) { return e.group_id === gid && e.status !== 'cancelled'; }).length; }
  var REQ = ['contact', 'terms', 'recording', 'childs_work'];
  function latest(pid) { var m = {}; db.consents.filter(function (c) { return c.parent_id === pid; }).forEach(function (c) { m[c.consent_type] = c; }); return m; }
  function interest() { if (!db.interest) db.interest = [
    { id: 'i1', created_at: '2026-10-20T01:00:00Z', expires_at: '2027-10-20T01:00:00Z', level: 2, age_band: '8-9', slots: ['R1', 'MON-PM'], windows: ['sat'], other_time: null, parent_first_name: 'Mei', contact_whatsapp: '91234567', contact_email: null, note: null, status: 'new' },
    { id: 'i2', created_at: '2026-10-21T01:00:00Z', expires_at: '2027-10-21T01:00:00Z', level: 2, age_band: '6-7', slots: ['R1'], windows: [], other_time: 'Tue 4pm', parent_first_name: 'Sam', contact_whatsapp: null, contact_email: 'sam@example.com', note: 'sibling', status: 'new' }]; return db.interest; }
  window.__mockDb = function () { return db; };

  var rpcs = {
    add_child: function (a) { var u = me(); if (!/^[0-9]{4,6}$/.test(a.p_pin)) throw err('pin_format');
      if (db.children.some(function (c) { return c.parent_id === u.id && c.display_name.toLowerCase() === a.p_name.trim().toLowerCase(); })) throw err('duplicate key children_parent_name_uq');
      db.children.push({ id: id('c'), parent_id: u.id, display_name: a.p_name.trim(), level: a.p_level, pin: 'hash:' + a.p_pin, created_at: new Date().toISOString(), failed: 0 }); return null; },
    update_child: function (a) { var c = db.children.filter(function (x) { return x.id === a.p_child; })[0]; if (!c) throw err('not_found');
      if (a.p_level !== c.level && db.enrolments.some(function (e) { return e.child_id === c.id && e.status !== 'cancelled'; })) throw err('level_locked_by_enrolment');
      c.display_name = a.p_name; c.level = a.p_level; if (a.p_pin) c.pin = 'hash:' + a.p_pin; return null; },
    delete_child: function (a) { if (db.enrolments.some(function (e) { return e.child_id === a.p_child && e.status !== 'cancelled'; })) throw err('cancel_enrolment_first');
      db.children = db.children.filter(function (c) { return c.id !== a.p_child; }); return null; },
    group_fill: function () { return db.groups.map(function (g) { return { group_id: g.id, seats: g.seats, taken: taken(g.id) }; }); },
    my_consents: function () { var m = latest(me().id); return Object.keys(m).map(function (k) { return m[k]; }); },
    record_consents: function (a) { Object.keys(a.p_items).forEach(function (k) { db.consents.push({ parent_id: me().id, consent_type: k, granted: a.p_items[k], terms_version: a.p_terms, privacy_version: a.p_privacy, created_at: new Date().toISOString() }); }); return null; },
    enrol_child: function (a) { var u = me(), c = db.children.filter(function (x) { return x.id === a.p_child && x.parent_id === u.id; })[0], g = db.groups.filter(function (x) { return x.id === a.p_group; })[0];
      if (!c || !g) throw err('not_found'); if (g.level !== c.level) throw err('level_mismatch');
      if (db.enrolments.some(function (e) { return e.child_id === c.id && e.status !== 'cancelled'; })) throw err('already_enrolled');
      var l = latest(u.id); if (REQ.some(function (k) { return !(l[k] && l[k].granted); })) throw err('consents_missing:x');
      if (taken(g.id) >= g.seats) throw err('group_full');
      var e = { id: id('e'), parent_id: u.id, child_id: c.id, child_label: c.display_name, group_id: g.id, status: 'pending_payment', created_at: new Date().toISOString() };
      db.enrolments.push(e); db.payments.push({ id: id('p'), enrolment_id: e.id, method: 'paynow_manual', status: 'pending', reference: 'MI-' + code(6), amount_cents: g.fee_cents, paid_at: null }); return e.id; },
    cancel_my_enrolment: function (a) { var e = db.enrolments.filter(function (x) { return x.id === a.p_enrolment; })[0]; var p = db.payments.filter(function (x) { return x.enrolment_id === a.p_enrolment; })[0];
      if (!e || p.status !== 'pending') throw err('cannot_cancel_contact_us'); e.status = 'cancelled'; p.status = 'cancelled'; return null; },
    my_enrolments: function () { var u = me(); return db.enrolments.filter(function (e) { return e.parent_id === u.id; }).map(function (e) { var p = db.payments.filter(function (x) { return x.enrolment_id === e.id; })[0];
      return { enrolment_id: e.id, child_id: e.child_id, child_name: e.child_label, group_id: e.group_id, enrolment_status: e.status, payment_id: p.id, payment_method: p.method, payment_status: p.status, payment_reference: p.reference, amount_cents: p.amount_cents, paid_at: p.paid_at, created_at: e.created_at }; }); },
    child_sign_in: function (a) { var par = db.parents.filter(function (p) { return p.family_code === String(a.p_family_code).trim().toUpperCase(); })[0]; if (!par) return [];
      var c = db.children.filter(function (x) { return x.parent_id === par.id && x.display_name.toLowerCase() === a.p_name.trim().toLowerCase(); })[0]; if (!c) return [];
      if (c.locked) return []; if (c.pin === 'hash:' + a.p_pin) { c.failed = 0; return [{ child_id: c.id, display_name: c.display_name, level: c.level }]; }
      c.failed++; if (c.failed >= 5) c.locked = true; return []; },
    admin_interest_tally: function () { if (!isAdmin()) throw err('forbidden'); var rows = interest(), out = [], m = {};
      rows.forEach(function (r) { var k = [r.level, 'total', '*'].join('|'); m[k] = (m[k] || 0) + 1; r.slots.forEach(function (s) { k = [r.level, 'slot', s].join('|'); m[k] = (m[k] || 0) + 1; }); });
      Object.keys(m).forEach(function (k) { var p = k.split('|'); out.push({ level: +p[0], kind: p[1], key: p[2], n: m[k] }); }); return out; },
    admin_list_interest_requests: function () { if (!isAdmin()) throw err('forbidden'); return interest(); },
    admin_set_interest_status: function (a) { if (!isAdmin()) throw err('forbidden'); interest().forEach(function (r) { if (r.id === a.p_id) r.status = a.p_status; }); return null; },
    admin_delete_interest_request: function (a) { if (!isAdmin()) throw err('forbidden'); db.interest = interest().filter(function (r) { return r.id !== a.p_id; }); return null; },
    admin_purge_expired_interest_requests: function () { if (!isAdmin()) throw err('forbidden'); return 0; },
    admin_list_enrolments: function () { if (!isAdmin()) throw err('forbidden'); return db.enrolments.map(function (e) { var p = db.payments.filter(function (x) { return x.enrolment_id === e.id; })[0], pa = db.parents.filter(function (x) { return x.id === e.parent_id; })[0];
      return { enrolment_id: e.id, created_at: e.created_at, parent_email: pa.email, parent_name: pa.full_name, parent_phone: pa.phone, child_name: e.child_label, level: 1, group_id: e.group_id, enrolment_status: e.status, payment_id: p.id, payment_method: p.method, payment_status: p.status, payment_reference: p.reference, amount_cents: p.amount_cents, paid_at: p.paid_at }; }); },
    admin_mark_paid: function (a) { if (!isAdmin()) throw err('forbidden'); var p = db.payments.filter(function (x) { return x.id === a.p_payment; })[0]; p.status = 'paid'; p.paid_at = new Date().toISOString();
      db.enrolments.forEach(function (e) { if (e.id === p.enrolment_id && e.status === 'pending_payment') e.status = 'confirmed'; }); return null; },
    delete_my_data: function () { var u = me(); db.children = db.children.filter(function (c) { return c.parent_id !== u.id; }); db.enrolments.forEach(function (e) { if (e.parent_id === u.id) e.status = 'cancelled'; });
      db.parents = db.parents.filter(function (p) { return p.id !== u.id; }); db.users = db.users.filter(function (x) { return x.id !== u.id; }); return null; }
  };

  /* ---- portal screens: behaviour of portal_ui.sql and practice_submissions.sql functions (checked against real Postgres by the SQL tests) ---- */
  function nowIso() { return new Date().toISOString(); }
  function adm() { if (!isAdmin()) throw err('forbidden'); }
  function ownChild(id) { var u = me(); return db.children.filter(function (c) { return c.id === id && c.parent_id === u.id; })[0]; }
  function consentOk(pid) { var l = latest(pid); return ['contact', 'terms', 'online_practice'].every(function (k) { return l[k] && l[k].granted; }); }
  function hasC(pid, k) { var l = latest(pid); return !!(l[k] && l[k].granted); }
  function levelOf(gid) { return db.groups.filter(function (g) { return g.id === gid; })[0].level; }
  function ents(childId) {
    var c = db.children.filter(function (x) { return x.id === childId; })[0], out = [], seen = {};
    db.enrolments.forEach(function (e) {
      var ch = db.children.filter(function (x) { return x.id === e.child_id; })[0];
      if (e.status === 'confirmed' && ch && ch.parent_id === c.parent_id) { var L = levelOf(e.group_id); if (!seen[L]) { seen[L] = 1; out.push({ kind: 'enrolled', level: L, format: null, source: 'enrolment', access_id: null, since: e.created_at }); } }
    });
    db.access.forEach(function (a) { if (a.child_id === childId && a.status === 'active') out.push({ kind: 'book', level: a.level, format: a.format, source: a.source, access_id: a.id, since: a.created_at }); });
    return out;
  }
  function unitsFor(childId) {
    var e = ents(childId);
    return db.units.filter(function (u) {
      if (!u.published || u.access === 'open') return false;
      if (u.access === 'enrolled') return e.some(function (x) { return x.kind === 'enrolled' && x.level === u.level; });
      return e.some(function (x) { return x.kind === 'book' && x.level === u.level && (x.format === 'online' || x.format === 'both'); });
    });
  }
  function childForToken(tok) {
    var s = db.child_sessions.filter(function (x) { return x.token === tok && !x.revoked && new Date(x.expires_at) > new Date(); })[0];
    return s ? { s: s, c: db.children.filter(function (x) { return x.id === s.child_id; })[0] } : null;
  }
  function validYear(y) { var n = new Date().getFullYear(); return y == null || (y >= n - 18 && y <= n - 3); }
  function tokenStr() { var a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-', s = ''; for (var i = 0; i < 43; i++) s += a[Math.floor(Math.random() * a.length)]; return s; }
  function adminOrder(o) { var p = db.parents.filter(function (x) { return x.id === o.parent_id; })[0]; return { id: o.id, reference: o.reference, parent_email: p && p.email, child_label: o.child_label, product_id: o.product_id, status: o.status, ship_status: o.ship_status, paid_at: o.paid_at, created_at: o.created_at }; }
  Object.assign(rpcs, {
    add_child_profile: function (a) { if (!validYear(a.p_birth_year)) throw err('bad_birth_year'); rpcs.add_child(a); var u = me(); db.children.filter(function (c) { return c.parent_id === u.id && c.display_name.toLowerCase() === a.p_name.trim().toLowerCase(); })[0].birth_year = a.p_birth_year || null; return null; },
    update_child_birth_year: function (a) { if (!validYear(a.p_year)) throw err('bad_birth_year'); var c = ownChild(a.p_child); if (!c) throw err('not_found'); c.birth_year = a.p_year; return null; },
    list_ext_prices: function () { return Object.keys(db.prices).map(function (k) { return { product_id: k, amount_cents: db.prices[k] }; }); },
    create_ext_order: function (a) {
      var u = me(), c = ownChild(a.p_child); if (!c) throw err('not_found');
      if (['workbook', 'online', 'both'].indexOf(a.p_format) < 0 || a.p_level < 1 || a.p_level > 6) throw err('bad_product');
      var key = 'ext-l' + a.p_level + '-' + a.p_format, price = db.prices[key]; if (price == null) throw err('price_not_set');
      if (!hasC(u.id, 'terms') || !hasC(u.id, 'contact')) throw err('consents_missing:contact,terms');
      if (a.p_format !== 'workbook' && !hasC(u.id, 'online_practice')) throw err('consents_missing:online_practice');
      if (a.p_format !== 'online') {
        if (!hasC(u.id, 'book_delivery')) throw err('consents_missing:book_delivery');
        if (!(a.p_ship_name || '').trim() || !(a.p_ship_address || '').trim() || !/^[0-9]{6}$/.test(a.p_ship_postal || '')) throw err('bad_address');
      }
      if (a.p_format !== 'workbook' && db.access.some(function (x) { return x.child_id === c.id && x.level === a.p_level && x.status === 'active' && x.format !== 'workbook'; })) throw err('already_has_online');
      if (db.ext_orders.some(function (o) { return o.child_id === c.id && o.level === a.p_level && o.status === 'pending_payment' && (o.format === a.p_format || (o.format !== 'workbook' && a.p_format !== 'workbook')); })) throw err('already_pending');
      var o = { id: id('o'), reference: 'MI-' + code(6), parent_id: u.id, child_id: c.id, child_label: c.display_name, level: a.p_level, format: a.p_format, product_id: key, amount_cents: price, currency: 'SGD', method: 'paynow_manual',
        status: 'pending_payment', paid_at: null, ship_status: a.p_format === 'online' ? 'not_needed' : 'to_ship', ship_name: a.p_format === 'online' ? null : a.p_ship_name, ship_address: a.p_format === 'online' ? null : a.p_ship_address,
        ship_postal: a.p_format === 'online' ? null : a.p_ship_postal, ship_phone: a.p_ship_phone || null, shipped_at: null, delivered_at: null, created_at: nowIso() };
      db.ext_orders.push(o); return o.id; },
    cancel_my_ext_order: function (a) { var u = me(), o = db.ext_orders.filter(function (x) { return x.id === a.p_order && x.parent_id === u.id && x.status === 'pending_payment'; })[0]; if (!o) throw err('cannot_cancel_order');
      o.status = 'cancelled'; o.ship_status = 'not_needed'; o.ship_name = o.ship_address = o.ship_postal = o.ship_phone = null; return null; },
    my_children_access: function () { var u = me(), out = []; db.children.filter(function (c) { return c.parent_id === u.id; }).forEach(function (c) { ents(c.id).forEach(function (e) { out.push(Object.assign({ child_id: c.id }, e)); }); }); return out; },
    my_children_units: function () { var u = me(), out = []; db.children.filter(function (c) { return c.parent_id === u.id; }).forEach(function (c) { unitsFor(c.id).forEach(function (x) { out.push(Object.assign({ child_id: c.id }, x)); }); }); return out; },
    my_children_progress: function () { var u = me(), kids = db.children.filter(function (c) { return c.parent_id === u.id; }).map(function (c) { return c.id; }), by = {};
      db.submissions.filter(function (s) { return kids.indexOf(s.child_id) >= 0; }).forEach(function (s) { var k = s.child_id + '|' + s.unit_key; (by[k] = by[k] || []).push(s); });
      return Object.keys(by).map(function (k) { var l = by[k].slice().sort(function (a, b) { return a.received_at < b.received_at ? 1 : -1; }), s = l[0], un = db.units.filter(function (x) { return x.unit_key === s.unit_key; })[0] || {};
        return { child_id: s.child_id, unit_key: s.unit_key, title: un.title, product: un.product, level: un.level, unit_no: un.unit_no, tries: l.length, last_received_at: s.received_at, n_auto: s.n_auto, n_skipped: s.n_skipped, n_self: s.n_self, n_self_got: s.n_self_got, n_open: s.n_open }; }); },
    practice_child_detail: function (a) { if (!ownChild(a.p_child)) throw err('forbidden'); return db.attempts.filter(function (x) { return x.child_id === a.p_child && x.unit_key === a.p_unit; }); },
    delete_child_practice: function (a) { if (!ownChild(a.p_child)) throw err('not_found'); var n = db.submissions.filter(function (s) { return s.child_id === a.p_child; }).length;
      db.submissions = db.submissions.filter(function (s) { return s.child_id !== a.p_child; }); db.attempts = db.attempts.filter(function (s) { return s.child_id !== a.p_child; }); db.child_sessions = db.child_sessions.filter(function (s) { return s.child_id !== a.p_child; }); return n; },
    request_trial: function (a) { var u = me(); if (a.p_child && !ownChild(a.p_child)) throw err('not_found');
      if (!hasC(u.id, 'contact') || !hasC(u.id, 'terms')) throw err('consents_missing:contact,terms');
      if (db.trials.filter(function (t) { return t.parent_id === u.id; }).length >= 3) throw err('too_many');
      var t = { id: id('t'), parent_id: u.id, child_id: a.p_child || null, level: a.p_level, preferred: a.p_preferred || [], note: a.p_note, source: a.p_source, status: 'new', created_at: nowIso() }; db.trials.push(t); return t.id; },
    withdraw_trial_request: function (a) { var u = me(); db.trials.forEach(function (t) { if (t.id === a.p_id && t.parent_id === u.id && t.status === 'new') t.status = 'withdrawn'; }); return null; },
    child_start_session: function (a) {
      var par = db.parents.filter(function (p) { return p.family_code === String(a.p_family_code).trim().toUpperCase(); })[0]; if (!par) return [];
      var r = rpcs.child_sign_in(a); if (!r.length) return []; if (!consentOk(par.id)) return [];
      var tok = tokenStr(), exp = new Date(Date.now() + 4 * 3600 * 1000).toISOString();
      db.child_sessions.push({ token: tok, child_id: r[0].child_id, expires_at: exp, revoked: false });
      return [{ token: tok, child_id: r[0].child_id, display_name: r[0].display_name, level: r[0].level, expires_at: exp }]; },
    child_end_session: function (a) { db.child_sessions.forEach(function (s) { if (s.token === a.p_token) s.revoked = true; }); return null; },
    child_session_overview: function (a) { var x = childForToken(a.p_token); if (!x) return null;
      return { child_id: x.c.id, name: x.c.display_name, level: x.c.level, expires_at: x.s.expires_at, can_submit: consentOk(x.c.parent_id),
        access: ents(x.c.id).filter(function (e) { return e.kind === 'enrolled' || e.format === 'online' || e.format === 'both'; }).map(function (e) { return { kind: e.kind, level: e.level, format: e.format }; }),
        units: unitsFor(x.c.id).map(function (u) { return { unit_key: u.unit_key, product: u.product, level: u.level, unit_no: u.unit_no, title: u.title }; }) }; },
    // owner
    admin_list_ext_orders: function () { adm(); return db.ext_orders.map(adminOrder); },
    admin_mark_ext_order_paid: function (a) { adm(); var o = db.ext_orders.filter(function (x) { return x.id === a.p_order; })[0]; if (!o) throw err('not_found'); if (o.status === 'paid') return null; if (o.status !== 'pending_payment') throw err('bad_status');
      o.status = 'paid'; o.paid_at = nowIso(); db.access.push({ id: id('a'), child_id: o.child_id, level: o.level, format: o.format, source: 'paynow_manual', order_id: o.id, source_note: null, status: 'active', created_at: nowIso(), ended_at: null }); return null; },
    admin_cancel_ext_order: function (a) { adm(); var o = db.ext_orders.filter(function (x) { return x.id === a.p_order && x.status === 'pending_payment'; })[0]; if (!o) throw err('cannot_cancel_order'); o.status = 'cancelled'; o.ship_status = 'not_needed'; o.ship_name = o.ship_address = o.ship_postal = o.ship_phone = null; return null; },
    admin_refund_ext_order: function (a) { adm(); db.ext_orders.forEach(function (o) { if (o.id === a.p_order && o.status === 'paid') o.status = 'refunded'; }); db.access.forEach(function (x) { if (x.order_id === a.p_order && x.status === 'active') x.status = 'refunded'; }); return null; },
    admin_set_ship_status: function (a) { adm(); db.ext_orders.forEach(function (o) { if (o.id === a.p_order && o.format !== 'online') { o.ship_status = a.p_status; if (a.p_status === 'shipped') o.shipped_at = nowIso(); if (a.p_status === 'delivered') o.delivered_at = nowIso(); } }); return null; },
    admin_clear_delivered_addresses: function () { adm(); return 0; },
    admin_list_children: function () { adm(); return db.children.map(function (c) { var p = db.parents.filter(function (x) { return x.id === c.parent_id; })[0]; return { child_id: c.id, display_name: c.display_name, level: c.level, birth_year: c.birth_year || null, parent_email: p.email, parent_name: p.full_name }; }); },
    admin_list_book_access: function () { adm(); return db.access.map(function (a) { var c = db.children.filter(function (x) { return x.id === a.child_id; })[0], p = db.parents.filter(function (x) { return x.id === c.parent_id; })[0];
      return { access_id: a.id, child_id: a.child_id, child_name: c.display_name, parent_email: p.email, level: a.level, format: a.format, source: a.source, source_note: a.source_note, status: a.status, created_at: a.created_at, ended_at: a.ended_at }; }); },
    admin_grant_book_access: function (a) { adm(); var x = { id: id('a'), child_id: a.p_child, level: a.p_level, format: a.p_format, source: 'admin', source_note: a.p_note, status: 'active', created_at: nowIso(), ended_at: null }; db.access.push(x); return x.id; },
    admin_revoke_book_access: function (a) { adm(); db.access.forEach(function (x) { if (x.id === a.p_access && x.status === 'active') { x.status = 'revoked'; x.ended_at = nowIso(); } }); return null; },
    admin_list_ext_prices: function () { adm(); return Object.keys(db.prices).map(function (k) { return { product_id: k, amount_cents: db.prices[k], active: !(db.priceOff || {})[k] }; }); },
    admin_set_ext_price: function (a) { adm(); db.prices[a.p_product] = a.p_cents; db.priceOff = db.priceOff || {}; db.priceOff[a.p_product] = !a.p_active; if (!a.p_active) delete db.prices[a.p_product]; return null; },
    admin_list_trial_requests: function () { adm(); return db.trials.map(function (t) { var p = db.parents.filter(function (x) { return x.id === t.parent_id; })[0], c = db.children.filter(function (x) { return x.id === t.child_id; })[0];
      return { id: t.id, parent_email: p.email, parent_name: p.full_name, parent_phone: p.phone, child_label: c && c.display_name, level: t.level, preferred: t.preferred, note: t.note, source: t.source, status: t.status, created_at: t.created_at }; }); },
    admin_set_trial_status: function (a) { adm(); db.trials.forEach(function (t) { if (t.id === a.p_id) t.status = a.p_status; }); return null; },
    admin_funnel_counts: function () { adm(); var paid = db.ext_orders.filter(function (o) { return o.status === 'paid'; }), by = {};
      db.trials.filter(function (t) { return t.status !== 'withdrawn'; }).forEach(function (t) { by[t.source] = (by[t.source] || 0) + 1; });
      var started = {}; db.submissions.forEach(function (s) { var u = db.units.filter(function (x) { return x.unit_key === s.unit_key; })[0]; if (u && u.access === 'purchased') started[s.child_id] = 1; });
      return { books_paid: paid.length, families_bought: Object.keys(paid.reduce(function (m, o) { m[o.parent_id] = 1; return m; }, {})).length, children_started: Object.keys(started).length,
        trial_requests: db.trials.filter(function (t) { return t.status !== 'withdrawn'; }).length, trial_by_source: by, trial_attended: db.trials.filter(function (t) { return t.status === 'attended' || t.status === 'enrolled'; }).length,
        enrolled: db.trials.filter(function (t) { return t.status === 'enrolled'; }).length }; },
    admin_practice_overview: function () { adm(); return db.submissions.map(function (s) { var c = db.children.filter(function (x) { return x.id === s.child_id; })[0], p = db.parents.filter(function (x) { return x.id === c.parent_id; })[0];
      return { child_id: c.id, display_name: c.display_name, parent_email: p.email, has_group: db.enrolments.some(function (e) { return e.child_id === c.id && e.status === 'confirmed'; }), unit_key: s.unit_key, received_at: s.received_at, n_auto: s.n_auto }; }); },
    tutor_group_practice: function (a) { adm(); return (db.report[a.p_group] || { practice: [] }).practice; },
    tutor_group_skill_report: function (a) { adm(); return ((db.report[a.p_group] || {}).skills || {})[a.p_unit] || []; },
    tutor_group_slips: function (a) { adm(); return ((db.report[a.p_group] || {}).slips || {})[a.p_unit] || []; },
    preview_open_sessions: function () { return db.previews.map(function (p) { return { id: p.id, starts_at: p.starts_at, band: p.band, is_full: false }; }); },
    admin_preview_list: function (a) { adm(); return (db.previews.filter(function (p) { return p.id === a.p_session; })[0] || { regs: [] }).regs; },
    admin_preview_funnel: function () { adm(); return [{ band: 'Primary 3-4', sessions_held: 1, registered: 4, attended: 3, wants_trial: 1, trial_attended: 0, enrolled: 0 }]; }
  });

  function table(name) {
    var u = me(), q = { op: 'select', upd: null, cond: [], ord: null };
    var src = { parents: db.parents, children: db.children, groups: db.groups, ext_orders: db.ext_orders, child_book_access: db.access, trial_requests: db.trials }[name] || [];
    function visible() {
      if (name === 'groups') return db.groups;
      if (!u) return [];
      var rows = src.filter(function (r) {
        if (name === 'parents') return r.id === u.id;
        if (name === 'child_book_access') { var c = db.children.filter(function (x) { return x.id === r.child_id; })[0]; return isAdmin() || (c && c.parent_id === u.id); }
        if (name === 'ext_orders' || name === 'trial_requests') return isAdmin() || r.parent_id === u.id;
        return r.parent_id === u.id;
      });
      return rows.map(function (r) { var c = Object.assign({}, r); delete c.pin; delete c.failed; delete c.locked; return c; });
    }
    var b = {
      select: function () { return b; }, single: function () { q.single = true; return b; },
      order: function (col, o) { q.ord = [col, o && o.ascending === false ? -1 : 1]; return b; },
      update: function (v) { q.op = 'update'; q.upd = v; return b; },
      eq: function (k, v) { q.cond.push(['eq', k, v]); return b; }, neq: function (k, v) { q.cond.push(['neq', k, v]); return b; },
      then: function (res, rej) {
        var out;
        function ok(r) { return q.cond.every(function (c) { return c[0] === 'eq' ? r[c[1]] === c[2] : r[c[1]] !== c[2]; }); }
        if (q.op === 'update') { src.forEach(function (r) { if (ok(r) && r.id === u.id) Object.assign(r, q.upd); }); save(); out = { data: null, error: null }; }
        else {
          var v = visible().filter(ok);
          if (q.ord) v.sort(function (x, y) { return (x[q.ord[0]] > y[q.ord[0]] ? 1 : x[q.ord[0]] < y[q.ord[0]] ? -1 : 0) * q.ord[1]; });
          out = q.single ? { data: v[0] || null, error: v[0] ? null : err('no rows') } : { data: v, error: null };
        }
        return Promise.resolve(out).then(res, rej);
      }
    };
    return b;
  }
  var listeners = [];
  function fire(ev) { listeners.forEach(function (l) { l(ev, db.session); }); }
  function mk(u) { return { access_token: 'tok-' + u.id, user: { id: u.id, email: u.email } }; }
  var auth = {
    getSession: function () { return Promise.resolve({ data: { session: db.session }, error: null }); },
    signUp: function (a) { if (db.users.some(function (u) { return u.email === a.email; })) return Promise.resolve({ data: {}, error: err('User already registered') });
      var u = { id: id('u'), email: a.email, password: a.password }; db.users.push(u);
      db.parents.push({ id: u.id, email: a.email, full_name: a.options && a.options.data.full_name, phone: null, family_code: code(6) });
      if (window.__CONFIRM_EMAIL__) { save(); return Promise.resolve({ data: { session: null, user: {} }, error: null }); }
      db.session = mk(u); save(); return Promise.resolve({ data: { session: db.session }, error: null }); },
    signInWithPassword: function (a) { var u = db.users.filter(function (x) { return x.email === a.email && x.password === a.password; })[0];
      if (!u) return Promise.resolve({ data: {}, error: err('Invalid login credentials') }); db.session = mk(u); save(); setTimeout(function () { fire('SIGNED_IN'); }, 0); return Promise.resolve({ data: { session: db.session }, error: null }); },
    resetPasswordForEmail: function (email, o) { window.__resets = (window.__resets || []).concat([{ email: email, redirectTo: o && o.redirectTo }]); return Promise.resolve({ data: {}, error: null }); },
    updateUser: function (a) { var u = me(); if (!u) return Promise.resolve({ data: {}, error: err('Auth session missing') }); if (window.__UPDATE_FAIL__) return Promise.resolve({ data: {}, error: err('weird internal db error xyz') }); u.password = a.password; save(); return Promise.resolve({ data: { user: { id: u.id } }, error: null }); },
    __recover: function (email) { var u = db.users.filter(function (x) { return x.email === email; })[0]; db.session = mk(u); save(); fire('PASSWORD_RECOVERY'); setTimeout(function () { fire('SIGNED_IN'); }, 0); },
    signInWithOtp: function () { return Promise.resolve({ data: {}, error: null }); },
    signOut: function () { db.session = null; save(); setTimeout(function () { fire('SIGNED_OUT'); }, 0); return Promise.resolve({ error: null }); },
    onAuthStateChange: function (cb) { listeners.push(cb); return { data: { subscription: { unsubscribe: function () {} } } }; }
  };
  window.__recover = auth.__recover;
  window.supabase = { createClient: function () { return {
    auth: auth, from: table,
    rpc: function (name, args) { try { var r = rpcs[name](args || {}); save(); return Promise.resolve({ data: r, error: null }); } catch (e) { return Promise.resolve({ data: null, error: e.message ? e : err(String(e)) }); } }
  }; } };
  db.users.push; // admin account for tests
  if (!db.users.some(function (u) { return u.email === 'owner@example.com'; })) { var o = { id: 'u-owner', email: 'owner@example.com', password: 'ownerpass1' }; db.users.push(o); db.parents.push({ id: o.id, email: o.email, full_name: 'Owner', family_code: 'OWNER1' }); save(); }
})();
