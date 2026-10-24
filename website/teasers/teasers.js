/* Math Inquirers daily teaser: static, no cookies, no tracking, no timers for the puzzle, no scores.
   The puzzle for a day is chosen from the Singapore calendar date (UTC+8, no daylight saving),
   so every visitor sees the same puzzle that day and it changes at midnight Singapore time.

   MiTeaser.init({box, level, ages, released, inline, base, now}):
     box       the element that holds the page's fixed puzzle (kept in the page; it is the fallback)
     released  months (MM) that have a released batch
     inline    {MM: {MM-DD: puzzle}} batches built into the page (the latest released months)
     base      folder to fetch other released months from
   If the date has a puzzle (inline, or fetched in time), it is shown and labelled with its date.
   If not (month not released, fetch failed or slow), the page's own fixed puzzle stays exactly as it is:
   it is never labelled with a date. A slow reply is accepted when it arrives, unless the visitor has
   already started on the fixed puzzle. */
(function (g) {
  'use strict';
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var WAIT_MS = 8000;
  function pad(n) { return (n < 10 ? '0' : '') + n; }

  /* Singapore date from a UTC millisecond timestamp. SGT is a fixed UTC+8, so the browser's own
     time zone never matters. */
  function sgt(ms) {
    var shifted = ms + 8 * 3600000;
    var d = new Date(shifted);
    return {
      mm: pad(d.getUTCMonth() + 1), dd: pad(d.getUTCDate()), year: d.getUTCFullYear(),
      day: Math.floor(shifted / 86400000), dow: d.getUTCDay(), month: d.getUTCMonth(),
      key: pad(d.getUTCMonth() + 1) + '-' + pad(d.getUTCDate()),
      label: DAYS[d.getUTCDay()] + ' ' + d.getUTCDate() + ' ' + MONTHS[d.getUTCMonth()]
    };
  }

  /* ---------- answer checking ---------- */
  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = a % b; a = b; b = t; } return a; }
  function cleanNum(s) {
    s = s.replace(/−|–|—/g, '-').replace(/[⁄∕]/g, '/').replace(/\s+/g, ' ').trim();
    if (/^\+\d/.test(s)) s = s.slice(1);
    if (/^-?\d{1,3}(,\d{3})+(\.\d+)?$/.test(s)) s = s.replace(/,/g, '');
    else if (/^-?\d{1,3}( \d{3})+(\.\d+)?$/.test(s)) s = s.replace(/ /g, '');
    return s;
  }
  /* returns {n, d, red} (value n/d, red = fraction written in lowest terms) or null */
  function parseNum(s) {
    s = cleanNum(s);
    var m;
    if ((m = /^(-?)(\d+)$/.exec(s))) return { n: (m[1] ? -1 : 1) * parseInt(m[2], 10), d: 1, red: true };
    if ((m = /^(-?)(\d*)\.(\d+)$/.exec(s))) {
      var den = Math.pow(10, m[3].length);
      return { n: (m[1] ? -1 : 1) * (parseInt(m[2] || '0', 10) * den + parseInt(m[3], 10)), d: den, red: true };
    }
    if ((m = /^(-?)(\d+) ?\/ ?(\d+)$/.exec(s))) {
      var dd = parseInt(m[3], 10);
      if (!dd) return null;
      var nn = parseInt(m[2], 10);
      return { n: (m[1] ? -1 : 1) * nn, d: dd, red: gcd(nn, dd) === 1 };
    }
    if ((m = /^(\d+) (\d+) ?\/ ?(\d+)$/.exec(s))) {
      var d3 = parseInt(m[3], 10), n3 = parseInt(m[2], 10);
      if (!d3) return null;
      return { n: parseInt(m[1], 10) * d3 + n3, d: d3, red: gcd(n3, d3) === 1 };
    }
    return null;
  }
  function norm(s) {
    return String(s).toLowerCase().replace(/[’‘]/g, "'").replace(/ /g, ' ').replace(/\s+/g, ' ').trim()
      .replace(/^=\s*/, '').replace(/[.!]+$/, '').trim();
  }
  function byLen(a, b) { return b.length - a.length; }
  function squash(t) { return t.replace(/[^a-z0-9' ]/g, ' ').replace(/\s+/g, ' ').trim(); }
  /* result: 'ok' | 'simplify' | 'no' | 'empty' | 'format' */
  function check(p, input) {
    var s = norm(input || '');
    if (!s) return 'empty';
    if (p.t === 's') {
      var t = squash(s).replace(/^((it is|it was|it's|on|in|the|a|an) )+/, '').trim();
      var ok = [p.a].concat(p.x || []);
      for (var i = 0; i < ok.length; i++) {
        var want = squash(ok[i].toLowerCase());
        if (t === want || t.replace(/ /g, '') === want.replace(/ /g, '')) return 'ok';
      }
      return 'no';
    }
    var wantN = parseNum(p.a);
    var pre = (p.p || []).slice().sort(byLen), uni = (p.u || []).map(function (x) { return x.toLowerCase(); }).sort(byLen);
    var asMinutes = uni.indexOf('minutes') >= 0 || uni.indexOf('min') >= 0;
    var asPercent = uni.indexOf('%') >= 0;
    var m;
    /* ordinal suffix: 21st, 2nd, 5 th */
    if ((m = /^(\d+) ?(st|nd|rd|th)$/.exec(s))) s = m[1];
    /* 1 h 30 min for a minutes answer */
    if (asMinutes && (m = /^(\d+) ?(h|hr|hrs|hour|hours) ?(\d+) ?(m|min|mins|minute|minutes)?$/.exec(s))) {
      s = String(parseInt(m[1], 10) * 60 + parseInt(m[3], 10));
    }
    var cands = [s], i2, j;
    for (i2 = 0; i2 < pre.length; i2++) {
      if (s.indexOf(pre[i2]) === 0) cands.push(s.slice(pre[i2].length).trim());
    }
    var more = [];
    for (i2 = 0; i2 < cands.length; i2++) {
      for (j = 0; j < uni.length; j++) {
        var c = cands[i2];
        if (c.length > uni[j].length && c.slice(-uni[j].length) === uni[j]) more.push(c.slice(0, -uni[j].length).trim());
      }
    }
    cands = cands.concat(more);
    var got = null;
    for (i2 = 0; i2 < cands.length && !got; i2++) got = parseNum(cands[i2]);
    if (!got) return /\d/.test(s) ? 'no' : 'format';
    if (got.n * wantN.d === wantN.n * got.d) {
      if (p.e && !got.red) return 'simplify';
      return 'ok';
    }
    /* a percentage written as a decimal: 0.96 for 96% */
    if (asPercent && s.indexOf('.') >= 0 && got.n * 100 * wantN.d === wantN.n * got.d) return 'ok';
    return 'no';
  }

  /* ---------- rendering ---------- */
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function build(opts, p, when, source) {
    var wrap = el('div', 'pzdaily');
    wrap.setAttribute('data-pzdaily', '1');
    wrap.appendChild(el('span', 'tag', 'Ages ' + opts.ages + ' · Puzzle for ' + when.label));
    if (p.b) wrap.appendChild(el('div', 'big', p.b));
    var q = el('p', 'pzq', p.q);
    q.style.fontSize = '18px';
    wrap.appendChild(q);
    if (p.c) {
      var pre = el('pre', 'pzcode', p.c);
      pre.setAttribute('role', 'group');
      pre.setAttribute('aria-label', 'Puzzle diagram or program');
      wrap.appendChild(pre);
    }
    var lab = el('label', 'pzlab', 'Your answer');
    lab.setAttribute('for', 'pzdA');
    wrap.appendChild(lab);
    var row = el('div', 'row');
    var inp = document.createElement('input');
    inp.id = 'pzdA';
    inp.setAttribute('placeholder', 'Type it here');
    inp.setAttribute('autocomplete', 'off');
    inp.setAttribute('autocapitalize', 'off');
    inp.setAttribute('spellcheck', 'false');
    inp.setAttribute('inputmode', /^\d+$/.test(p.a) ? 'numeric' : 'text');
    inp.style.maxWidth = '200px';
    var btn = el('button', 'btn yel', 'Check');
    btn.id = 'pzdCheck';
    btn.type = 'button';
    row.appendChild(inp);
    row.appendChild(btn);
    wrap.appendChild(row);
    var msg = el('div');
    msg.id = 'pzdMsg';
    msg.setAttribute('role', 'status');
    msg.setAttribute('aria-live', 'polite');
    msg.setAttribute('tabindex', '-1');
    wrap.appendChild(msg);
    wrap.appendChild(el('p', 'small muted pzmeta', 'A new puzzle every day at midnight, Singapore time. Nothing is saved or counted.'));

    function show(cls, text) {
      msg.innerHTML = '';
      var d = el('div', 'msg ' + cls);
      d.appendChild(document.createTextNode(text));
      msg.appendChild(d);
      return d;
    }
    function reveal() {
      msg.innerHTML = '';
      var d = el('div', 'msg info');
      d.appendChild(el('b', null, 'The answer is ' + p.s + '.'));
      d.appendChild(document.createElement('br'));
      d.appendChild(document.createTextNode(p.w));
      msg.appendChild(d);
      msg.focus();   /* the button that was pressed is gone: move focus to the explanation so keyboard and screen-reader users stay in place */
    }
    function go() {
      var r = check(p, inp.value);
      if (r === 'empty') { show('info', 'Type your answer first, then press Check.'); return; }
      if (r === 'ok') {
        msg.innerHTML = '';
        var d = el('div', 'msg ok');
        d.appendChild(el('b', null, 'Correct! '));
        d.appendChild(document.createTextNode(p.w));
        d.appendChild(document.createElement('br'));
        d.appendChild(document.createTextNode('Now ask: how do you know?'));
        msg.appendChild(d);
        return;
      }
      if (r === 'simplify') { show('info', 'That is the right amount. Can you write it in its simplest form?'); return; }
      if (r === 'format') { show('info', 'Try writing your answer with digits, like 12' + (p.t === 's' ? ' or a word' : '') + '.'); return; }
      show('no', 'Not yet. Hint: ' + p.h);
      var more = el('button', 'btn sm alt', 'Show me how');
      more.type = 'button';
      more.style.marginTop = '8px';
      more.addEventListener('click', reveal);
      msg.appendChild(more);
    }
    btn.addEventListener('click', go);
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go(); } });
    return wrap;
  }

  function init(opts) {
    var box = opts.box;
    if (!box) return;
    var now = opts.now || function () { return Date.now(); };
    var fixedNodes = Array.prototype.slice.call(box.childNodes);
    var daily = null, handled = null, token = 0;
    box.setAttribute('data-teaser-source', 'fixed');

    function fixedTouched() {
      for (var i = 0; i < fixedNodes.length; i++) {
        var n = fixedNodes[i];
        if (n.nodeType !== 1) continue;
        var inner = n.querySelectorAll ? n.querySelectorAll('input') : [];
        var all = (n.tagName === 'INPUT' ? [n] : []).concat(Array.prototype.slice.call(inner));
        for (var k = 0; k < all.length; k++) if (all[k].value) return true;
        var d2 = (n.tagName === 'DETAILS' ? [n] : []).concat(Array.prototype.slice.call(n.querySelectorAll ? n.querySelectorAll('details') : []));
        for (k = 0; k < d2.length; k++) if (d2[k].open) return true;
        var m2 = n.id === 'pzMsg' ? n : (n.querySelector ? n.querySelector('#pzMsg') : null);
        if (m2 && m2.childNodes.length) return true;
      }
      return false;
    }
    function setFixed(hidden) {
      for (var i = 0; i < fixedNodes.length; i++) if (fixedNodes[i].nodeType === 1) fixedNodes[i].hidden = hidden;
    }
    function showFixed() {
      if (daily && daily.parentNode) daily.parentNode.removeChild(daily);
      daily = null;
      setFixed(false);
      box.setAttribute('data-teaser-source', 'fixed');
      box.removeAttribute('data-teaser');
      box.removeAttribute('data-teaser-date');
      box.setAttribute('data-teaser-state', 'done');
    }
    function showDaily(p, when, source) {
      if (daily && daily.parentNode) daily.parentNode.removeChild(daily);
      daily = build(opts, p, when, source);
      setFixed(true);
      box.appendChild(daily);
      box.setAttribute('data-teaser', p.i);
      box.setAttribute('data-teaser-date', when.key);
      box.setAttribute('data-teaser-source', source);
      box.setAttribute('data-teaser-state', 'done');
    }
    function released(mm) { return !opts.released || opts.released.indexOf(mm) >= 0; }

    function run() {
      var when = sgt(now());
      if (handled === when.key) return;
      handled = when.key;
      var my = ++token;
      box.setAttribute('data-teaser-state', 'loading');
      var month = null;
      if (opts.data) month = opts.data(opts.level, when.mm);                 /* previews: month data supplied in the page */
      else if (opts.inline && opts.inline[when.mm]) month = opts.inline[when.mm];
      if (month) {
        if (month[when.key]) showDaily(month[when.key], when, 'month'); else showFixed();
        return;
      }
      if (opts.data || !released(when.mm) || !opts.base || typeof fetch !== 'function') { showFixed(); return; }
      /* a released month that is not built into the page: fetch it, keep the fixed puzzle meanwhile */
      showFixed();
      box.setAttribute('data-teaser-state', 'loading');
      var timer = setTimeout(function () { if (my === token) box.setAttribute('data-teaser-state', 'done'); }, WAIT_MS);
      fetch(opts.base + 'L' + opts.level + '-' + when.mm + '.json').then(function (r) {
        if (!r.ok) throw new Error('no batch');
        return r.json();
      }).then(function (j) {
        clearTimeout(timer);
        if (my !== token) return;
        if (j && j[when.key] && !fixedTouched()) showDaily(j[when.key], when, 'month');
        else box.setAttribute('data-teaser-state', 'done');
      }).catch(function () { clearTimeout(timer); if (my === token) box.setAttribute('data-teaser-state', 'done'); });
    }
    run();
    /* if the page stays open past midnight Singapore time, pick up the new day when the visitor comes back to it */
    if (opts.listen !== false) {
      document.addEventListener('visibilitychange', function () { if (!document.hidden) run(); });
      g.addEventListener('focus', run);
    }
    return { refresh: run };
  }

  g.MiTeaser = { sgt: sgt, check: check, init: init, parseNum: parseNum };
})(window);
