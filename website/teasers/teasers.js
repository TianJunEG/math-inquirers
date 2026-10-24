/* Math Inquirers daily teaser: static, no cookies, no tracking, no timers, no scores.
   The puzzle for a day is chosen from the Singapore calendar date (UTC+8, no daylight saving),
   so every visitor sees the same puzzle that day and it changes at midnight Singapore time.
   MiTeaser.init({box, level, ages, pool, base, now}) replaces the fixed fallback puzzle in `box`. */
(function (g) {
  'use strict';
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
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
    s = s.replace(/−|–|—/g, '-').replace(/\s+/g, ' ').trim();
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
    return String(s).toLowerCase().replace(/[’‘]/g, "'").replace(/ /g, ' ').replace(/\s+/g, ' ').trim()
      .replace(/^=\s*/, '').replace(/[.!]+$/, '').trim();
  }
  function byLen(a, b) { return b.length - a.length; }
  /* result: 'ok' | 'simplify' | 'no' | 'empty' | 'format' */
  function check(p, input) {
    var s = norm(input || '');
    if (!s) return 'empty';
    if (p.t === 's') {
      var t = s.replace(/[^a-z0-9' ]/g, ' ').replace(/\s+/g, ' ').trim().replace(/^(the|a|an|it was|it is) /, '').trim();
      var ok = [p.a].concat(p.x || []);
      for (var i = 0; i < ok.length; i++) {
        if (t === ok[i].toLowerCase().replace(/[^a-z0-9' ]/g, ' ').replace(/\s+/g, ' ').trim()) return 'ok';
      }
      return 'no';
    }
    var want = parseNum(p.a);
    var pre = (p.p || []).slice().sort(byLen), uni = (p.u || []).map(function (x) { return x.toLowerCase(); }).sort(byLen);
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
    if (got.n * want.d !== want.n * got.d) return 'no';
    if (p.e && !got.red) return 'simplify';
    return 'ok';
  }

  /* ---------- picking ---------- */
  function pickFromPool(pool, day) { return pool[((day % pool.length) + pool.length) % pool.length]; }

  /* ---------- rendering ---------- */
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function render(box, opts, p, when, source) {
    box.innerHTML = '';
    box.setAttribute('data-teaser', p.i);
    box.setAttribute('data-teaser-date', when.key);
    box.setAttribute('data-teaser-source', source);
    var tag = el('span', 'tag', 'Ages ' + opts.ages + ' · Puzzle for ' + when.label);
    box.appendChild(tag);
    if (p.b) box.appendChild(el('div', 'big', p.b));
    var q = el('p', 'pzq', p.q);
    q.style.fontSize = '18px';
    box.appendChild(q);
    if (p.c) {
      var pre = el('pre', 'pzcode', p.c);
      pre.setAttribute('aria-label', 'Puzzle diagram or program');
      box.appendChild(pre);
    }
    var row = el('div', 'row');
    var inp = document.createElement('input');
    inp.id = 'pzA';
    inp.setAttribute('aria-label', 'Your answer');
    inp.setAttribute('placeholder', 'Your answer');
    inp.setAttribute('autocomplete', 'off');
    inp.setAttribute('autocapitalize', 'off');
    inp.setAttribute('spellcheck', 'false');
    inp.setAttribute('inputmode', /^\d+$/.test(p.a) ? 'numeric' : 'text');
    inp.style.maxWidth = '200px';
    var btn = el('button', 'btn yel', 'Check');
    btn.id = 'pzCheck';
    btn.type = 'button';
    row.appendChild(inp);
    row.appendChild(btn);
    box.appendChild(row);
    var msg = el('div');
    msg.id = 'pzMsg';
    msg.setAttribute('role', 'status');
    msg.setAttribute('aria-live', 'polite');
    box.appendChild(msg);
    box.appendChild(el('p', 'small muted pzmeta', 'A new puzzle every day at midnight, Singapore time. Nothing is saved or counted.'));

    function show(cls, text, hint) {
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
    }
    var tries = 0;
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
      tries++;
      if (r === 'simplify') { show('info', 'That is the right amount. Can you write it in its simplest form?'); return; }
      if (r === 'format') { show('info', 'Try writing your answer with digits, like 12' + (p.t === 's' ? ' or a word' : '') + '.'); return; }
      var d2 = show('no', 'Not yet. Hint: ' + p.h);
      var more = el('button', 'btn sm alt', 'Show me how');
      more.type = 'button';
      more.style.marginTop = '8px';
      more.addEventListener('click', reveal);
      msg.appendChild(more);
    }
    btn.addEventListener('click', go);
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go(); } });
  }

  function init(opts) {
    var box = opts.box;
    if (!box) return;
    var now = opts.now || function () { return Date.now(); };
    var rendered = null;
    function run() {
      var when = sgt(now());
      if (rendered === when.key) return;
      rendered = when.key;
      var usePool = function () { render(box, opts, pickFromPool(opts.pool, when.day), when, 'pool'); };
      if (opts.data) {   /* previews: month data supplied in the page instead of fetched */
        var local = opts.data(opts.level, when.mm);
        if (local && local[when.key]) render(box, opts, local[when.key], when, 'month'); else usePool();
        return;
      }
      if (!opts.base || typeof fetch !== 'function') { usePool(); return; }
      var done = false;
      var timer = setTimeout(function () { if (!done) { done = true; usePool(); } }, 2500);
      fetch(opts.base + 'L' + opts.level + '-' + when.mm + '.json').then(function (r) {
        if (!r.ok) throw new Error('no batch');
        return r.json();
      }).then(function (j) {
        if (done) return;
        done = true; clearTimeout(timer);
        if (j && j[when.key]) render(box, opts, j[when.key], when, 'month'); else usePool();
      }).catch(function () { if (!done) { done = true; clearTimeout(timer); usePool(); } });
    }
    run();
    /* if the page stays open past midnight Singapore time, pick up the new day when the visitor comes back to it */
    if (opts.listen !== false) {
      document.addEventListener('visibilitychange', function () { if (!document.hidden) run(); });
      g.addEventListener('focus', run);
    }
    return { refresh: run };
  }

  g.MiTeaser = { sgt: sgt, check: check, init: init, pick: pickFromPool, parseNum: parseNum };
})(window);
