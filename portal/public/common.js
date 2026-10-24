/* Shared helpers for the portal pages. No innerHTML anywhere: all text goes through textContent. */
(function () {
  var CFG = window.MI_CONFIG || {};
  // Bump these whenever the text of terms.html / privacy.html changes: they are stored with every consent record.
  // 10d: adds the draft wording for online_practice, book_delivery and marketing_contact (docs/legal/online_submission_consent_draft.md). Still DRAFT: owner and lawyer to approve.
  var VERSIONS = { terms: 'terms-2026-10d-draft', privacy: 'privacy-2026-10d-draft' };

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
    pin_weak: 'That PIN is too easy to guess (for example 1234, 0000, the same digit repeated, or a year). Please choose another 4 to 6 digits.',
    has_online_access: 'This child has online access that was paid for. Removing the child would end it. You can move the access to a brother or sister, or confirm that you want to give it up.',
    target_has_access: 'That brother or sister already has online access to the same book level, so it cannot be moved there.',
    confirmation_needed: 'Please confirm first.',
    too_many_orders: 'You have made quite a few orders in the last hour. Please wait a little while, then try again.',
    too_many_children: 'You can add up to 6 children.',
    level_locked_by_enrolment: 'The level cannot change while the child has a place in a group. Cancel the place first.',
    cancel_enrolment_first: 'Cancel this child\'s place first.',
    cannot_cancel_contact_us: 'This place is already paid, so please message us to cancel.',
    forbidden: 'This page is for the owner only.',
    not_signed_in: 'Please log in again.',
    price_not_set: 'The price for this book is not set yet, so it cannot be ordered online. Please use the "Ask us" button and we will reply.',
    already_has_online: 'This child already has online access to that book level.',
    already_pending: 'There is already an unpaid order for this child and book. Please pay it or cancel it first (see "Your orders").',
    bad_address: 'Please check the delivery details. We post to Singapore addresses only, and the postal code has 6 digits.',
    bad_birth_year: 'Please choose a birth year from the list, or leave it blank.',
    cannot_cancel_order: 'That order cannot be cancelled here. If it is already paid, please message us.',
    bad_input: 'Something in that form was not accepted. Please reload the page and try again.',
    too_many: 'You have sent a few requests today already. We will reply soon, so please wait a day before sending another.',
    not_found: 'We could not find that. Please reload the page and try again.'
  };
  var GENERIC = 'Something went wrong on our side. Please try again in a moment. If it keeps happening, message us on WhatsApp.';
  // Only text we wrote ourselves (say()) or that maps to a known code is shown. Anything else (database, network or
  // library messages) becomes the generic line so internals never reach the screen.
  function say(text) { var e = new Error(text); e.friendly = true; return e; }
  function errText(err) {
    if (err && err.friendly) return err.message;
    var m = String((err && (err.message || err.error_description)) || '');
    if (/consents_missing/.test(m)) return 'Please tick and save the agreements this needs first (see Agreements).';
    if (/duplicate key|children_parent_name_uq/.test(m)) return 'You already have a child with that name. Use a different display name.';
    for (var k in MESSAGES) if (m.indexOf(k) !== -1) return MESSAGES[k];
    if (/Invalid login/i.test(m)) return 'Email or password is not right. Check them and try again, or use "Magic link" to get a log-in link by email.';
    if (/already registered|already been registered/i.test(m)) return 'There is already an account with that email. Try the Log in tab.';
    if (/not confirmed/i.test(m)) return 'Please click the link in the confirmation email first, then log in.';
    if (/rate limit|too many/i.test(m)) return 'Too many tries just now. Please wait a few minutes and try again.';
    if (/password/i.test(m) && /(at least|weak|short)/i.test(m)) return 'Please choose a longer password (at least 8 characters).';
    if (/failed to fetch|network|load failed/i.test(m)) return 'We could not reach the server. Check your internet connection and try again.';
    if (/jwt|expired|not authenticated/i.test(m)) return 'Please log in again.';
    return GENERIC;
  }
  // R1-L10: if the owner has not set PORTAL_PAYNOW_TO at build time the config still says "(to confirm)"; do not show that to a parent as if it were a PayNow number.
  function paynowLine(cents) {
    var to = String(CFG.PAYNOW_TO || ''), real = to && !/to confirm|PAYNOW_TO/i.test(to);
    return real ? 'Pay ' + money(cents) + ' by PayNow to ' + to + '.' : 'Pay ' + money(cents) + ' by PayNow. Message us on WhatsApp for the PayNow details and quote the reference below.';
  }
  function money(cents) { return 'S$' + (cents / 100).toFixed(2); }
  function sessionsText(sessions) {
    return (sessions || []).map(function (s) { return s.day + ' ' + s.start + '-' + s.end; }).join(' and ');
  }
  function fmtDate(iso) {
    try { return new Date(iso).toLocaleString('en-SG', { timeZone: 'Asia/Singapore', dateStyle: 'medium', timeStyle: 'short' }); } catch (e) { return iso; }
  }
  // A result message. tabindex -1 lets it take keyboard focus (focusResult below); role=alert for errors, status for the rest, so it is announced.
  function notice(box, kind, text) {
    clear(box); if (text) box.appendChild(h('p', { class: 'msg ' + kind, role: kind === 'err' ? 'alert' : 'status', tabindex: -1, text: text }));
  }
  /* ---------- keyboard focus after an action (the pages redraw by clearing the container, which drops focus to <body>) ---------- */
  // focusKey() remembers WHICH control had focus (id, a data-* attribute, or tag + visible text); focusRestore() puts focus back on its twin after the redraw.
  function focusKey(root) {
    var a = document.activeElement; if (!a || a === document.body || (root && !root.contains(a))) return null;
    var k = { tag: a.tagName, id: a.id || '', text: (a.textContent || '').trim().slice(0, 60), name: a.getAttribute('name') || '', value: a.getAttribute('value') || '' };
    [].some.call(a.attributes, function (at) { if (/^data-/.test(at.name)) { k.data = [at.name, at.value]; return true; } });
    return k;
  }
  function focusRestore(root, k) {
    if (!k || !root) return;
    var n = null;
    if (k.id) n = document.getElementById(k.id);
    if (!n && k.data) n = root.querySelector('[' + k.data[0] + '="' + String(k.data[1]).replace(/"/g, '') + '"]');
    if (!n) n = [].filter.call(root.querySelectorAll(k.tag.toLowerCase()), function (e) { return (e.textContent || '').trim().slice(0, 60) === k.text && (e.getAttribute('name') || '') === k.name && (e.getAttribute('value') || '') === k.value; })[0];
    if (n) try { n.focus(); } catch (e) {}
  }
  // After an action: move focus to the result message (it is announced and the person lands where the news is); with no message, to the page heading.
  function focusResult(root) {
    root = root || document;
    var m = root.querySelector('.msg.err[role], .msg.warn[role], .msg.ok[role]');
    var t = m || root.querySelector('h1');
    if (!t) return;
    if (!t.hasAttribute('tabindex')) t.setAttribute('tabindex', '-1');
    try { t.focus(); if (m && t.scrollIntoView) t.scrollIntoView({ block: 'nearest' }); } catch (e) {}
  }
  // A polite live region that is never redrawn, for news that is not a message (e.g. "signed out because you were away").
  function announce(text) {
    var r = document.getElementById('mi-live');
    if (!r) { r = h('div', { id: 'mi-live', class: 'sr', 'aria-live': 'polite', role: 'status' }); document.body.appendChild(r); }
    r.textContent = ''; setTimeout(function () { r.textContent = text; }, 30);
  }
  // The payment page address must be Stripe's own: a tampered /api reply must not be able to send the parent anywhere else.
  function stripeUrl(u) {
    try { var x = new URL(String(u)); return x.protocol === 'https:' && x.hostname === 'checkout.stripe.com' && !x.username && !x.password && (!x.port || x.port === '443') ? x.href : null; } catch (e) { return null; }
  }
  function goToStripe(u) {
    var ok = stripeUrl(u);
    if (!ok) throw say('Could not start the payment. Nothing was charged. Please try again.');
    location.href = ok;   // top-level redirect to Stripe Checkout; card details never touch our pages
  }
  function themeInit() {
    try { var t = localStorage.getItem('mi-theme'); if (t) document.documentElement.setAttribute('data-theme', t); } catch (e) {}
  }
  themeInit();
  function header(subtitle) {
    return h('header', { class: 'top' },
      h('a', { class: 'skip', href: '#app', text: 'Skip to content' }),
      h('a', { class: 'brand', href: '/' }, h('i', { text: '?' }), h('span', { text: CFG.SITE_NAME || 'Math Inquirers' })),
      h('span', { class: 'sub', text: subtitle || '' }));
  }
  // Mobile: tables become one card per row. Copies each header label onto its cells (the CSS shows them).
  function stack(root) {
    [].forEach.call((root || document).querySelectorAll('table'), function (t) {
      var heads = [].map.call(t.querySelectorAll('thead th'), function (th) { return th.textContent; });
      t.classList.add('stack');
      [].forEach.call(t.querySelectorAll('tbody tr'), function (tr) { [].forEach.call(tr.children, function (td, i) { td.setAttribute('data-label', heads[i] || ''); }); });
    });
  }
  /* ---------- agreements (consent types). Wording: docs/legal/online_submission_consent_draft.md (DRAFT) and privacy.html "Wording used on the registration form" ---------- */
  var CONSENTS = {
    contact: 'I agree to Math Inquirers (Preciouslyours Pte Ltd) using my details to arrange the class or order and contact me about it.',
    terms: 'I have read the terms and refund policy and agree to them.',
    online_practice: 'I am the parent or legal guardian of this child. I agree that when my child presses "Submit" on an online practice page, Math Inquirers (Preciouslyours Pte Ltd) receives my child\'s answers, marks them again on our server, and keeps them with my child\'s profile (first name or nickname and level) to make practice reports for me and, if my child is in one of our groups, for my child\'s tutor. We do not use my child\'s answers for advertising. We keep them for 12 months after the last submission, or until 90 days after my child\'s online access ends, whichever is sooner, and then delete them. I can ask to see, correct or delete them, or withdraw this agreement, at any time.',
    recording: 'I agree that live lessons are recorded as described in the privacy notice, and that recordings are shared only with the enrolled families of my child\'s group.',
    childs_work: 'I agree that Math Inquirers keeps photos of my child\'s work, practice answers and short progress notes, as described in the privacy notice. I am the parent or legal guardian of the child.',
    book_delivery: 'I agree that Math Inquirers (Preciouslyours Pte Ltd) may give my delivery name, Singapore address, postal code and phone number to its printer and courier, only to print and deliver the book I ordered, and will delete them 30 days after the parcel is confirmed delivered.',
    marketing_contact: '(Optional) I agree that Math Inquirers may contact me by email or WhatsApp to suggest a trial class or a next book, including a suggestion based on how my child did in the online practice. I can say stop at any time and we will stop. I do not have to agree to use the online practice or to ask for a trial class.',
    feedback_quotes: '(Optional) I agree that my feedback may be used, without my child\'s name, to improve and describe the program.'
  };
  var FORMATS = { workbook: 'Workbook only (printed, posted to you)', online: 'Online only (practice pages for one child)', both: 'Workbook and online' };
  var FORMAT_SHORT = { workbook: 'printed workbook', online: 'online only', both: 'workbook and online' };
  var WA = 'https://wa.me/6598805962';
  function waLink(text) { return WA + (text ? '?text=' + encodeURIComponent(text) : ''); }
  function two(n) { return (n < 10 ? '0' : '') + n; }
  // Practice page address for a unit row {product, level, unit_no}. Patterns: docs/online_versions_plan.md section 6.
  function unitUrl(u) {
    var n = two(Number(u.unit_no || 0));
    if (u.product === 'holiday') return '/practice/holiday/p' + u.level + '/' + n + '/';
    if (u.product === 'term') return '/practice/term/l' + u.level + '/' + n + '/';
    return '/practice/ext/l' + u.level + 'u' + n + '/';
  }
  function unitLabel(u) {
    var n = Number(u.unit_no || 0);
    var base = u.product === 'holiday' ? 'Holiday, Level ' + u.level + ', lesson ' + n : u.product === 'term' ? 'Term, Level ' + u.level + ', lesson ' + n : 'Extension book, Level ' + u.level + ', unit ' + n;
    return base + (u.title ? ': ' + u.title : '');
  }
  async function rpc(name, args) { var r = await sb().rpc(name, args || {}); if (r.error) throw r.error; return r.data; }
  function dayText(iso) { try { return new Date(iso).toLocaleDateString('en-SG', { timeZone: 'Asia/Singapore', day: 'numeric', month: 'short', year: 'numeric' }); } catch (e) { return iso; } }
  window.MI = { rpc: rpc, CONSENTS: CONSENTS, FORMATS: FORMATS, FORMAT_SHORT: FORMAT_SHORT, waLink: waLink, unitUrl: unitUrl, unitLabel: unitLabel, dayText: dayText, stack: stack, say: say, h: h, mount: mount, clear: clear, configured: configured, sb: sb, errText: errText, money: money, sessionsText: sessionsText,
                fmtDate: fmtDate, paynowLine: paynowLine, notice: notice, header: header, CFG: CFG, VERSIONS: VERSIONS,
                focusKey: focusKey, focusRestore: focusRestore, focusResult: focusResult, announce: announce, stripeUrl: stripeUrl, goToStripe: goToStripe };
})();
