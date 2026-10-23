/* In-memory stand-in for supabase-js + the SQL functions, for Playwright tests ONLY (never shipped: it lives in tests/).
   State persists in localStorage so it survives page navigations. It re-implements the *behaviour* the SQL functions have
   (checked separately against real Postgres by supabase/test/run_sql_test.sh); it cannot prove the SQL is right. */
(function () {
  var KEY = 'mock-db';
  var seed = window.__SEED__ || { groups: [] };
  function load() { try { var s = localStorage.getItem(KEY); if (s) return JSON.parse(s); } catch (e) {} return { users: [], parents: [], children: [], enrolments: [], payments: [], consents: [], groups: seed.groups, extraTaken: seed.extraTaken || {}, session: null, n: 0 }; }
  var db = load(); function save() { localStorage.setItem(KEY, JSON.stringify(db)); }
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

  function table(name) {
    var rows = { parents: db.parents, children: db.children, groups: db.groups }[name] || [];
    var u = me(), q = { op: 'select', rows: null, upd: null, cond: [] };
    function visible() {
      if (name === 'groups') return db.groups;
      if (!u) return [];
      return rows.filter(function (r) { return (name === 'parents' ? r.id : r.parent_id) === u.id; }).map(function (r) { var c = Object.assign({}, r); delete c.pin; delete c.failed; delete c.locked; return c; });
    }
    var b = {
      select: function () { return b; }, order: function () { return b; }, single: function () { q.single = true; return b; },
      update: function (v) { q.op = 'update'; q.upd = v; return b; }, eq: function (k, v) { q.cond.push([k, v]); return b; },
      then: function (res, rej) {
        var out;
        if (q.op === 'update') { rows.forEach(function (r) { if (q.cond.every(function (c) { return r[c[0]] === c[1]; }) && r.id === u.id) Object.assign(r, q.upd); }); save(); out = { data: null, error: null }; }
        else { var v = visible(); out = q.single ? { data: v[0] || null, error: v[0] ? null : err('no rows') } : { data: v, error: null }; }
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
    signInWithOtp: function () { return Promise.resolve({ data: {}, error: null }); },
    signOut: function () { db.session = null; save(); setTimeout(function () { fire('SIGNED_OUT'); }, 0); return Promise.resolve({ error: null }); },
    onAuthStateChange: function (cb) { listeners.push(cb); return { data: { subscription: { unsubscribe: function () {} } } }; }
  };
  window.supabase = { createClient: function () { return {
    auth: auth, from: table,
    rpc: function (name, args) { try { var r = rpcs[name](args || {}); save(); return Promise.resolve({ data: r, error: null }); } catch (e) { return Promise.resolve({ data: null, error: e.message ? e : err(String(e)) }); } }
  }; } };
  db.users.push; // admin account for tests
  if (!db.users.some(function (u) { return u.email === 'owner@example.com'; })) { var o = { id: 'u-owner', email: 'owner@example.com', password: 'ownerpass1' }; db.users.push(o); db.parents.push({ id: o.id, email: o.email, full_name: 'Owner', family_code: 'OWNER1' }); save(); }
})();
