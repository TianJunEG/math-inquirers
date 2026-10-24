// Worksheet-style online practice (extension units, and reusable for term and holiday data in the same item format).
// The child can open any question in any order, skip, change answers, then submit. Marking and full worked solutions appear only after
// submitting. By default everything stays in this browser (localStorage, guarded): no account, nothing is sent anywhere. No timer, score, streak or ranking.
// OPTIONAL SEND TO TUTOR (feature flag, OFF): only if the page sets window.MI_SUBMIT = {endpoint: '...'} AND a child session token exists
// (MI_SUBMIT.token, or sessionStorage 'mi-child'.token from the portal child sign-in) does Submit also POST the answers (never a mark) to the endpoint.
// The server marks again from its own key. Without the flag, or without a token, this file makes no network request except loading its own data file.
// See docs/online_submission_design.md.
(function () {
  var key = window.MI_LESSON, $ = function (id) { return document.getElementById(id); };
  var TIERS = [['core', 'Start here'], ['invest', 'Investigation'], ['stretch', 'Think harder'], ['challenge', 'Go further'], ['check', 'Check yourself']];
  var L, cur = 0, S = { a: {}, sub: false, sid: '', rev: 0, sent: 0, self: {} }, ask = false, sim = {};
  var CFG = (typeof window.MI_SUBMIT === 'object' && window.MI_SUBMIT) || null, SY = { msg: '', busy: false, tries: 0, timer: 0, selfTimer: 0 }, VER = '';
  function load() { try { var o = JSON.parse(localStorage.getItem('mi-sheet-' + key) || '{}'); if (o && o.a) S = { a: o.a, sub: !!o.sub, sid: String(o.sid || ''), rev: o.rev | 0, sent: o.sent | 0, self: o.self || {} }; } catch (e) {} }
  function save() { try { localStorage.setItem('mi-sheet-' + key, JSON.stringify(S)); } catch (e) {} }
  function h(tag, at, kids) {
    var e = document.createElement(tag);
    Object.keys(at || {}).forEach(function (k) { if (k === 'text') e.textContent = at[k]; else if (k === 'on') Object.keys(at.on).forEach(function (n) { e.addEventListener(n, at.on[n]); }); else e.setAttribute(k, at[k]); });
    (kids || []).forEach(function (c) { if (c) e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return e;
  }
  // ---- reading and judging
  function toNum(s) { s = String(s == null ? '' : s).replace(/\s/g, '').replace(/^\$/, '').replace(/(\d),(?=\d{3}(\D|$))/g, '$1'); return /^-?\d+$/.test(s) ? +s : null; }
  function nums(s) { s = String(s || '').replace(/(\d),(?=\d{3}(\D|$))/g, '$1'); if (/[,;]/.test(s)) return s.split(/[,;]/).reduce(function (acc, tok) { tok = tok.trim(); if (/^\d{1,3}(\s\d{3})+$/.test(tok)) tok = tok.replace(/\s/g, ''); return acc.concat(tok.match(/-?\d+/g) || []); }, []).map(Number); return (s.match(/-?\d+/g) || []).map(Number); }
  function sameSet(a, b) { var x = a.slice().sort(function (p, r) { return p - r; }), y = b.slice().sort(function (p, r) { return p - r; }); return x.length === y.length && x.every(function (v, i) { return v === y[i]; }); }
  // text answers: same rule as practice/submit/mark.js (case, spacing, hyphens and a final full stop do not matter)
  function normText(s) { return String(s == null ? '' : s).normalize('NFKC').toLowerCase().replace(/[.!]+$/, '').replace(/[\s\-]+/g, ' ').trim(); }
  function squash(s) { return normText(s).replace(/ /g, ''); }
  function answered(it, v) {
    if (v == null) return false;
    if (it.type === 'fields') return v.some(function (x) { return String(x).trim() !== ''; });
    return String(v).trim() !== '';
  }
  function judge(it, v) {
    if (it.type === 'selfcheck') return 'self';
    if (!answered(it, v)) return 'blank';
    if (it.type === 'choice') return v === it.answer ? 'right' : 'wrong';
    if (it.type === 'text') return it.answer.some(function (x) { return normText(x) === normText(v) || squash(x) === squash(v); }) ? 'right' : 'wrong';
    if (it.type === 'number') return toNum(v) === it.answer ? 'right' : 'wrong';
    if (it.type === 'fields') return it.fields.every(function (f, i) { return toNum(v[i]) === f.answer; }) ? 'right' : 'wrong';
    var a = nums(v), ok = it.ordered ? (a.length === it.answer.length && a.every(function (x, i) { return x === it.answer[i]; })) : sameSet(a, it.answer);
    return ok ? 'right' : 'wrong';
  }
  function show(it) {
    if (it.shown) return it.shown;
    if (it.type === 'fields') return it.fields.map(function (f) { return f.answer; }).join(', ');
    return Array.isArray(it.answer) ? it.answer.join(', ') : String(it.answer);
  }
  // ---- templates (same expression language as the runner; answers are computed, so a variant cannot be wrong)
  function arith(s) {
    if (!/^[\d\s+\-*/%().]*$/.test(s)) throw new Error('bad expression');
    var t = s.match(/\/\/|[\d.]+|[-+*/%()]/g) || [], p = 0;
    function peek() { return t[p]; }
    function prim() { var x = t[p++]; if (x === '(') { var v = sum(); p++; return v; } if (x === '-') return -prim(); return parseFloat(x); }
    function prod() { var v = prim(); while (/^(\*|\/|\/\/|%)$/.test(peek() || '')) { var o = t[p++], r = prim(); v = o === '*' ? v * r : o === '/' ? v / r : o === '%' ? v % r : Math.floor(v / r); } return v; }
    function sum() { var v = prod(); while (peek() === '+' || peek() === '-') { var o = t[p++], r = prod(); v = o === '+' ? v + r : v - r; } return v; }
    var out = sum(); if (p < t.length) throw new Error('bad expression'); return out;
  }
  function calc(expr, env) { var s = expr; Object.keys(env).sort(function (a, b) { return b.length - a.length; }).forEach(function (k) { s = s.replace(new RegExp('\\b' + k + '\\b', 'g'), env[k]); }); return arith(s); }
  function fill(str, env, keep) { return String(str).replace(/\{(\w+)\}/g, function (m, k) { return env[k] == null || (keep && keep.indexOf(k) > -1) ? m : env[k]; }); }
  function variantOf(it) {
    var t = it.tpl, env = {}, all;
    Object.keys(t.vars).forEach(function (n) { var a = t.vars[n]; env[n] = a[Math.floor(Math.random() * a.length)]; });
    all = Object.assign({}, env); Object.keys(t.derive || {}).forEach(function (k) { all[k] = calc(t.derive[k], all); });
    var v = { q: fill(t.q, all), hint: fill(t.hint, all) };
    if (t.answers) { v.type = 'fields'; v.frame = fill(t.frame, all, Object.keys(t.answers)); v.fields = Object.keys(t.answers).map(function (k) { return { id: k, answer: calc(t.answers[k], all) }; }); all.ans = v.fields.map(function (f) { return f.answer; }).join(', '); }
    else { v.type = 'number'; v.answer = calc(t.answer, all); all.ans = v.answer; }
    v.steps = t.steps.map(function (s) { return fill(s, all); });
    return v;
  }
  // ---- pieces of the page
  function status(it, i) { var j = judge(it, S.a[it.id]); if (S.sub) return j === 'right' ? 'right' : j === 'wrong' ? 'wrong' : j === 'self' ? 'self' : 'blank'; return answered(it, S.a[it.id]) ? 'done' : 'open'; }
  var MARK = { done: 'answered', open: 'not answered yet', right: 'right', wrong: 'to look at again', blank: 'no answer', self: 'self-check' };
  var SYM = { done: '●', open: '○', right: '✓', wrong: '✗', blank: '–', self: '✎' };
  function nav() {
    var n = $('nav'); n.textContent = ''; var i0 = 0;
    TIERS.forEach(function (t) {
      var its = L.items.map(function (it, i) { return [it, i]; }).filter(function (p) { return p[0].tier === t[0]; });
      if (!its.length) return;
      var g = h('div', { class: 'ng', role: 'group', 'aria-label': t[1] }, [h('span', { class: 'nt', text: t[1] })]);
      its.forEach(function (p) {
        var st = status(p[0], p[1]);
        g.appendChild(h('button', { type: 'button', class: 'nb ' + st, 'data-i': String(p[1]), 'aria-current': String(p[1] === cur), 'aria-label': 'Question ' + (p[1] + 1) + ', ' + MARK[st], title: MARK[st], on: { click: function () { cur = p[1]; ask = false; render(); } } }, [h('b', { text: String(p[1] + 1) }), h('i', { text: SYM[st], 'aria-hidden': 'true' })]));
      });
      n.appendChild(g);
    });
    var na = L.items.filter(function (it) { return answered(it, S.a[it.id]); }).length;
    $('count').textContent = S.sub ? 'Submitted. You can look at every question and its solution.' : na + ' of ' + L.items.length + ' questions have an answer. You can open any question, in any order.';
  }
  function fig(it) { if (!it.svg) return null; var d = new DOMParser().parseFromString(it.svg, 'image/svg+xml').documentElement; if (!d || d.nodeName !== 'svg') return null; Array.prototype.forEach.call(d.querySelectorAll('script,foreignObject'), function (x) { x.remove(); }); var w = h('div', { class: 'fig' }); w.appendChild(document.importNode(d, true)); return w; }
  function control(it, locked) {
    var v = S.a[it.id], box = h('div', { id: 'ans', class: 'row' });
    function set(val) { S.a[it.id] = val; save(); nav(); bar(); }
    if (it.type === 'fields') {
      var cur_ = Array.isArray(v) ? v : it.fields.map(function () { return ''; });
      // the word just before a box (and the punctuation just after it) stays with the box, so '1/' and its box never split over two lines
      var fparts = it.frame.split(/(\{\w+\})/), prevG = null, tail = '';
      fparts.forEach(function (part, pi) {
        var m = /^\{(\w+)\}$/.exec(part), idx = m ? it.fields.map(function (f) { return f.id; }).indexOf(m[1]) : -1;
        if (idx > -1) {
          var inp = h('input', { type: 'text', inputmode: 'numeric', autocomplete: 'off', 'data-f': m[1], 'aria-label': 'Box ' + (idx + 1), style: 'width:5rem;text-align:center' }); inp.value = cur_[idx] || ''; if (locked) inp.disabled = true; inp.addEventListener('input', function () { var a = it.fields.map(function (f, i) { return i === idx ? inp.value : (cur_[i] || ''); }); cur_ = a; set(a); });
          prevG = h('span', { class: 'fg', style: 'display:inline-flex;align-items:center;gap:.25rem;white-space:nowrap' }, [tail ? h('span', { class: 'fr', text: tail }) : null, inp]); tail = ''; box.appendChild(prevG);
        } else if (part) {
          if (prevG) { var lead = /^[^ \n\t]+/.exec(part); if (lead) { prevG.appendChild(h('span', { class: 'fr', text: lead[0] })); part = part.slice(lead[0].length); } }
          var nextIsBox = pi + 1 < fparts.length && /^\{\w+\}$/.test(fparts[pi + 1]);
          if (nextIsBox) { var tl = /[^ \n\t]+(?=[ \n\t]*$)/.exec(part); if (tl) { tail = tl[0]; part = part.slice(0, tl.index); } }
          prevG = null;
          if (part.trim()) box.appendChild(h('span', { class: 'fr', text: part }));
        }
      });
    } else if (it.type === 'text') {
      var inp4 = h('input', { type: 'text', autocomplete: 'off', autocapitalize: 'none', spellcheck: 'false', 'aria-label': 'Your answer' }); inp4.value = v || ''; if (locked) inp4.disabled = true; inp4.addEventListener('input', function () { set(inp4.value); }); box.appendChild(inp4);
    } else if (it.type === 'set' || it.type === 'number') {
      var inp2 = h('input', { type: 'text', inputmode: 'numeric', autocomplete: 'off', 'aria-label': it.type === 'set' ? 'Your answers, separated by commas' : 'Your answer' }); inp2.value = v || ''; if (locked) inp2.disabled = true; inp2.addEventListener('input', function () { set(inp2.value); }); box.appendChild(inp2);
    } else if (it.type === 'choice') {
      it.options.forEach(function (o) { var r = h('input', { type: 'radio', name: 'c', value: o }); if (v === o) r.checked = true; if (locked) r.disabled = true; r.addEventListener('change', function () { set(o); }); box.appendChild(h('label', { class: 'opt' }, [r, o])); });
    } else if (it.type === 'selfcheck') {
      if (it.paper) box = h('div', { id: 'ans' });
      else { var ta = h('textarea', { 'aria-label': 'Your answer', placeholder: 'Write here...' }); ta.value = v || ''; if (locked) ta.disabled = true; ta.addEventListener('input', function () { set(ta.value); }); box = h('div', { id: 'ans' }, [ta]); }
    }
    return box;
  }
  function solution(it) {
    var j = judge(it, S.a[it.id]), cls = j === 'right' ? 'ok' : j === 'self' ? 'plain' : 'try';
    var head = j === 'right' ? 'Right.' : j === 'wrong' ? 'Look at this one again.' : j === 'blank' ? 'You skipped this one.' : 'Compare your answer with this.';
    var d = h('div', { class: 'fb ' + cls, id: 'sol' }, [h('h2', { text: head })]);
    if (it.type !== 'selfcheck') d.appendChild(h('p', { text: 'The answer is ' + show(it) + '.' }));
    var tk = selfTick(it); if (tk) d.appendChild(tk);
    if (it.sol_svg) { var sf = fig({ svg: it.sol_svg }); if (sf) { sf.id = 'solfig'; d.appendChild(sf); } }
    d.appendChild(h('h2', { text: 'Solution' })); d.appendChild(h('ol', {}, it.steps.map(function (s) { return h('li', { text: s }); })));
    if (it.tpl) d.appendChild(similar(it));
    return d;
  }
  function similar(it) {
    var w = h('div', { class: 'sim' }), st = sim[it.id];
    w.appendChild(h('button', { type: 'button', class: 'act quiet', text: st ? 'Try another similar one' : 'Try a similar one', on: { click: function () { sim[it.id] = { v: variantOf(it), done: false }; render(); document.getElementById('simq') && document.getElementById('simq').scrollIntoView({ block: 'nearest' }); } } }));
    if (st) {
      var v = st.v, p = h('div', { class: 'simbox', id: 'simq' }, [h('p', { class: 'q', text: v.q })]), row = h('div', { class: 'row' }), inputs = [];
      if (v.type === 'fields') v.frame.split(/(\{\w+\})/).forEach(function (part) { var m = /^\{(\w+)\}$/.exec(part); if (m && v.fields.some(function (f) { return f.id === m[1]; })) { var i2 = h('input', { type: 'text', inputmode: 'numeric', autocomplete: 'off', 'data-sf': m[1], 'aria-label': 'Box', style: 'width:5rem;text-align:center' }); inputs.push(i2); row.appendChild(i2); } else if (part) row.appendChild(h('span', { class: 'fr', text: part })); });
      else { var i3 = h('input', { type: 'text', inputmode: 'numeric', autocomplete: 'off', 'data-sf': 'n', 'aria-label': 'Your answer' }); inputs.push(i3); row.appendChild(i3); }
      p.appendChild(row);
      var out = h('div', { id: 'simfb', 'aria-live': 'polite' });
      p.appendChild(h('div', { class: 'row' }, [h('button', { type: 'button', class: 'act', text: 'Check', on: { click: function () {
        var ok = v.type === 'fields' ? v.fields.every(function (f, i) { return toNum(inputs[i].value) === f.answer; }) : toNum(inputs[0].value) === v.answer;
        out.textContent = ''; out.appendChild(h('div', { class: 'fb ' + (ok ? 'ok' : 'try') }, ok ? [h('h2', { text: 'Yes, that is right.' }), h('ol', {}, v.steps.map(function (s) { return h('li', { text: s }); }))] : [h('h2', { text: 'Not yet.' }), h('p', { text: 'Hint: ' + v.hint }), h('p', { text: 'The answer is ' + (v.type === 'fields' ? v.fields.map(function (f) { return f.answer; }).join(', ') : v.answer) + '.' }), h('ol', {}, v.steps.map(function (s) { return h('li', { text: s }); }))]));
      } } })]));
      p.appendChild(out); w.appendChild(p);
    }
    return w;
  }
  var hintOpen = {};
  function render() {
    nav();
    var it = L.items[cur], card = $('card'); card.textContent = '';
    var locked = S.sub;
    card.appendChild(h('p', { class: 'q', text: it.q }));
    var f = fig(it); if (f) card.appendChild(f);
    if (it.type === 'selfcheck' && it.paper) card.appendChild(h('p', { class: 'fb plain', id: 'paper', text: 'Do this on paper, then check your drawing against the answer shown on screen.' }));
    if (it.type === 'set') card.appendChild(h('p', { class: 'sub', style: 'margin:0 0 .5rem', text: 'Type every answer, with a comma between.' }));
    card.appendChild(control(it, locked));
    if (!S.sub) {
      var hb = h('div', { class: 'row', style: 'margin-top:.8rem' }, [h('button', { type: 'button', class: 'act quiet', text: hintOpen[it.id] ? 'Hide the hint' : 'Give me a hint', 'aria-expanded': String(!!hintOpen[it.id]), on: { click: function () { hintOpen[it.id] = !hintOpen[it.id]; render(); } } })]);
      card.appendChild(hb);
      if (hintOpen[it.id]) card.appendChild(h('div', { class: 'fb plain' }, [h('p', { text: 'Hint: ' + it.hint })]));
      if (it.type === 'selfcheck' && !it.paper) card.appendChild(h('p', { class: 'sub', text: 'You can write an answer here, or just do it on paper. The example comes with the solutions after you submit.' }));
    } else {
      card.appendChild(solution(it));
    }
    var pn = h('div', { class: 'row', style: 'margin-top:1rem' }, [
      h('button', { type: 'button', class: 'act quiet', text: 'Previous', on: { click: function () { cur = (cur + L.items.length - 1) % L.items.length; render(); window.scrollTo(0, 0); } } }),
      h('button', { type: 'button', class: 'act quiet', text: S.sub ? 'Next' : 'Skip to next', on: { click: function () { cur = (cur + 1) % L.items.length; render(); window.scrollTo(0, 0); } } })]);
    card.appendChild(pn);
    bar();
  }
  function bar() {
    var b = $('bar'); b.textContent = '';
    var un = L.items.filter(function (it) { return !answered(it, S.a[it.id]); }).length;
    var sl = syncLine(); if (sl) b.appendChild(sl);
    if (S.sub) { b.appendChild(summary()); b.appendChild(h('div', { class: 'row' }, [h('button', { type: 'button', id: 'again', class: 'act', text: 'Change my answers and submit again', on: { click: function () { S.sub = false; save(); render(); } } }), h('button', { type: 'button', class: 'act quiet', text: 'Start again with empty answers', on: { click: function () { S = { a: {}, sub: false, sid: '', rev: 0, sent: 0, self: {} }; sim = {}; hintOpen = {}; save(); cur = 0; render(); } } })])); return; }
    if (ask) {
      b.appendChild(h('div', { class: 'fb try', role: 'alertdialog', 'aria-label': 'Submit anyway?' }, [h('p', { text: un + (un === 1 ? ' question has' : ' questions have') + ' no answer. Submit anyway? You will see the solutions for every question.' }), h('div', { class: 'row' }, [h('button', { type: 'button', id: 'yes', class: 'act', text: 'Yes, submit', on: { click: function () { submit(); } } }), h('button', { type: 'button', id: 'keep', class: 'act quiet', text: 'Keep working', on: { click: function () { ask = false; bar(); } } })])]));
      return;
    }
    b.appendChild(h('button', { type: 'button', id: 'submit', class: 'act', text: 'Submit my answers', on: { click: function () { if (un) { ask = true; bar(); } else submit(); } } }));
  }
  function submit() { S.sub = true; ask = false; if (syncOn()) { if (!S.sid) S.sid = newId(); S.rev = (S.rev | 0) + 1; SY.tries = 0; SY.msg = ''; } save(); hintOpen = {}; render(); var s = $('bar'); if (s && s.scrollIntoView) s.scrollIntoView({ block: 'nearest' }); send(); }
  function summary() {
    var c = { right: 0, wrong: 0, blank: 0, self: 0 }; L.items.forEach(function (it) { c[judge(it, S.a[it.id])]++; });
    var marked = L.items.length - c.self;
    return h('div', { class: 'fb plain', id: 'summary' }, [h('h2', { text: 'Your answers are marked' }), h('p', { text: c.right + ' of ' + marked + ' marked questions are right. ' + c.wrong + ' to look at again, ' + c.blank + ' with no answer' + (c.self ? ', and ' + c.self + ' to check yourself.' : '.') + ' Open any question to see its worked solution.' }), h('p', { class: 'sub', text: '✓ right   ✗ look again   – no answer   ✎ check yourself' })]);
  }
  // ---- optional send to tutor (flag OFF by default)
  function tok() { try { if (CFG && CFG.token) return CFG.token; var c = JSON.parse(sessionStorage.getItem('mi-child') || 'null'); return (c && c.token) || null; } catch (e) { return null; } }
  function syncOn() { return !!(CFG && CFG.endpoint && tok()); }
  function newId() {
    try { if (window.crypto && crypto.randomUUID) return crypto.randomUUID(); var b = crypto.getRandomValues(new Uint8Array(16)); b[6] = b[6] & 15 | 64; b[8] = b[8] & 63 | 128;
      var x = Array.prototype.map.call(b, function (v) { return ('0' + v.toString(16)).slice(-2); }).join(''); return x.slice(0, 8) + '-' + x.slice(8, 12) + '-' + x.slice(12, 16) + '-' + x.slice(16, 20) + '-' + x.slice(20); } catch (e) { return ''; }
  }
  function payload() {
    var ans = {};
    L.items.forEach(function (it) {
      var v = S.a[it.id];
      // free text of a self-check item is never sent: only that something was written
      if (it.type === 'selfcheck') ans[it.id] = answered(it, v) ? '(written)' : null;
      else ans[it.id] = answered(it, v) ? (Array.isArray(v) ? v.map(String) : String(v)) : null;
    });
    var self = {}; Object.keys(S.self || {}).forEach(function (k) { self[k] = S.self[k]; });
    return { v: 1, unit: CFG.unit || ('ext-' + key), unit_version: CFG.version || VER, sid: S.sid, rev: S.rev, answers: ans, self: self };
  }
  function note(t) { SY.msg = t; var n = $('syncnote'); if (n) n.textContent = t; }
  function retry() {
    SY.busy = false; if (SY.tries >= 3) { note('We could not send your answers yet. They are safe on this device, and we will try again when you are back online.'); return; }
    note('Your answers are saved on this device. Sending to your tutor again soon.'); clearTimeout(SY.timer); SY.timer = setTimeout(send, [5000, 30000, 120000][SY.tries++]);
  }
  function send() {
    if (!syncOn() || !S.sub || SY.busy || !S.sid || S.sent >= S.rev || !VER && !CFG.version) return;
    SY.busy = true; var rev = S.rev, body;
    try { body = JSON.stringify(payload()); } catch (e) { SY.busy = false; return; }
    fetch(CFG.endpoint, { method: 'POST', credentials: 'omit', headers: { 'content-type': 'application/json', authorization: 'Bearer ' + tok() }, body: body })
      .then(function (r) { return r.json().then(function (j) { return { st: r.status, j: j }; }, function () { return { st: r.status, j: {} }; }); })
      .then(function (x) {
        SY.busy = false;
        if (x.st === 200 && x.j && x.j.ok) { S.sent = Math.max(S.sent, rev); save(); SY.tries = 0; note('Sent to your tutor.'); if (S.rev > rev) send(); }
        else if (x.st === 401) note('Please sign in again to send your answers to your tutor. They are saved on this device.');
        else if (x.st === 403 || x.st === 404) note('Your answers are saved here, but this page cannot send them to your tutor. Please ask a grown-up to check the sign-in and permissions.');
        else if (x.st === 429 || x.st >= 500) retry();
        else note('Your answers are saved here, but we could not send them. Please tell your tutor.');
      }, retry);
  }
  window.addEventListener('online', function () { SY.tries = 0; send(); });
  document.addEventListener('visibilitychange', function () { if (!document.hidden && S.sub && S.sent < S.rev) { SY.tries = 0; send(); } });
  function syncLine() { return syncOn() ? h('p', { class: 'sub', id: 'syncnote', role: 'status', 'aria-live': 'polite', text: SY.msg || (S.sub ? '' : 'When you press Submit, your answers are also sent to your tutor.') }) : null; }
  function pickSelf(it, val) {
    S.self = S.self || {}; S.self[it.id] = val; S.rev = (S.rev | 0) + 1; save(); render();
    clearTimeout(SY.selfTimer); SY.selfTimer = setTimeout(send, 2500);   // one send after the last tick, not one per tick
  }
  function selfTick(it) {
    if (!syncOn() || it.type !== 'selfcheck') return null;
    var cur_ = (S.self || {})[it.id], opts = [['checked', 'I checked it'], ['got', 'I got it'], ['not_yet', 'Not yet']];
    return h('div', { class: 'row', role: 'group', 'aria-label': 'How did you do? You can skip this.' }, [h('span', { class: 'sub', text: 'Optional: how did it go?' })].concat(opts.map(function (o) {
      return h('button', { type: 'button', class: 'act quiet', 'aria-pressed': String(cur_ === o[0]), text: (cur_ === o[0] ? '✓ ' : '') + o[1], on: { click: function () { pickSelf(it, o[0]); } } });
    })));
  }
  load();
  fetch('data/' + key + '.json').then(function (r) { if (!r.ok) throw new Error('missing'); return r.text(); }).then(function (txt) {
    var d = JSON.parse(txt), vp = Promise.resolve('');
    // the unit version = first 8 hex of the SHA-256 of this exact data file, so a server key can never be used for a changed question
    if (syncOn() && !CFG.version && window.crypto && crypto.subtle) vp = crypto.subtle.digest('SHA-256', new TextEncoder().encode(txt)).then(function (b) { return Array.prototype.map.call(new Uint8Array(b), function (v) { return ('0' + v.toString(16)).slice(-2); }).join('').slice(0, 8); }, function () { return ''; });
    return vp.then(function (v) { VER = v; return d; });
  }).then(function (d) {
    L = d; document.title = 'Practice: ' + L.title + ' | Math Inquirers';
    $('title').textContent = L.title + ' practice'; $('sub').textContent = 'Level ' + L.level + ' · ' + (L.unit_label || 'Lesson ' + L.lesson) + ' · ' + L.topic;
    render();
    if (S.sub && S.sent < S.rev) send();   // a tab closed before the send finished: try again when the page is opened again
  }).catch(function () { $('title').textContent = 'Practice'; $('card').textContent = 'This practice link is not complete. Please ask your tutor for the right link.'; });
})();
