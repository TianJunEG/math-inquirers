// Online practice runner. Static: the lesson file holds the questions, answers, hints, worked solutions and variants.
// Rules: no timers, no scores, no streaks, no leaderboard. Wrong answers get a hint, then a worked solution.
(function () {
  var q = new URLSearchParams(location.search), key = q.get('lesson') || window.MI_LESSON || 'p3l3';
  var $ = function (id) { return document.getElementById(id); };
  var TIER = { core: 'Start here', stretch: 'Think harder', challenge: 'Go further' };
  var L, tier = q.get('set') || 'core', idx = 0, st = {}, saved = {};
  try { saved = JSON.parse(localStorage.getItem('mi-practice-' + key) || '{}'); } catch (e) { saved = {}; }
  function persist() { try { localStorage.setItem('mi-practice-' + key, JSON.stringify(saved)); } catch (e) {} }

  function h(tag, attrs, kids) {
    var e = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) { if (k === 'text') e.textContent = attrs[k]; else if (k === 'on') Object.keys(attrs.on).forEach(function (n) { e.addEventListener(n, attrs.on[n]); }); else e.setAttribute(k, attrs[k]); });
    (kids || []).forEach(function (c) { if (c) e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return e;
  }
  // ---- templates: numbers are substituted, the answer is computed, so a variant cannot be wrong
  var HELP = {
    multiples: function (k, lim) { var o = []; for (var i = k; i <= lim; i += k) o.push(i); return o; },
    common: function (a, b, lim) { var o = []; for (var n = 1; n <= lim; n++) if (n % a === 0 && n % b === 0) o.push(n); return o; },
    divisors: function (n) { var o = []; for (var i = 1; i <= n; i++) if (n % i === 0) o.push(i); return o; }
  };
  function calc(expr, env) {
    var hm = /^\s*(multiples|common|divisors)\(([^)]*)\)\s*$/.exec(expr);
    if (hm) return HELP[hm[1]].apply(null, hm[2].split(',').map(function (x) { return calc(x, env); }));
    var s = expr; Object.keys(env).sort(function (a, b) { return b.length - a.length; }).forEach(function (k) { s = s.replace(new RegExp('\\b' + k + '\\b', 'g'), env[k]); });
    return arith(s);
  }
  // small evaluator: + - * / // % and brackets, with // as whole-number division (so "(a+b)//2 + 1" works anywhere in an expression)
  function arith(s) {
    if (!/^[\d\s+\-*/%().]*$/.test(s)) throw new Error('bad expression');
    var toks = s.match(/\/\/|[\d.]+|[-+*/%()]/g) || [], p = 0;
    function peek() { return toks[p]; }
    function prim() { var t = toks[p++]; if (t === '(') { var v = sum(); p++; return v; } if (t === '-') return -prim(); if (t === '+') return prim(); return parseFloat(t); }
    function prod() { var v = prim(); while (/^(\*|\/|\/\/|%)$/.test(peek() || '')) { var o = toks[p++], r = prim(); v = o === '*' ? v * r : o === '/' ? v / r : o === '%' ? v % r : Math.floor(v / r); } return v; }
    function sum() { var v = prod(); while (peek() === '+' || peek() === '-') { var o = toks[p++], r = prod(); v = o === '+' ? v + r : v - r; } return v; }
    var out = sum(); if (p < toks.length) throw new Error('bad expression'); return out;
  }
  var WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'], TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
  function numWord(n) { n = +n; if (n < 20) return WORDS[n]; if (n < 100) return TENS[Math.floor(n / 10)] + (n % 10 ? '-' + WORDS[n % 10] : ''); return String(n); }
  function ordinal(n) { n = +n; var r = n % 100, s = (r >= 11 && r <= 13) ? 'th' : ({ 1: 'st', 2: 'nd', 3: 'rd' }[n % 10] || 'th'); return n + s; }
  function fill(str, env, keep) { return String(str).replace(/\{(\w+)(?:\|(\w+))?\}/g, function (m, k, f) { if (env[k] == null || (keep && keep.indexOf(k) > -1)) return m; var v = env[k]; if (Array.isArray(v)) v = v.join(', '); return f === 'ord' ? ordinal(v) : f === 'word' ? numWord(v) : f === 'usd' ? '$' + v : f === 'c' ? v + '\u00a2' : f === 'cents' ? v + (+v === 1 ? ' cent' : ' cents') : f === 'dollars' ? v + (+v === 1 ? ' dollar' : ' dollars') : f === 'hour' ? v + (+v === 1 ? ' hour' : ' hours') : f === 'min' ? v + (+v === 1 ? ' minute' : ' minutes') : f === 'mm' ? (+v < 10 ? '0' + (+v) : String(v)) : v; }); }
  function variantOf(item, avoid) {
    var t = item.tpl, names = Object.keys(t.vars), env, tries = 0;
    do { env = {}; names.forEach(function (n) { var a = t.vars[n]; env[n] = a[Math.floor(Math.random() * a.length)]; }); tries++; } while (avoid && JSON.stringify(env) === avoid && tries < 12);
    var all = Object.assign({}, env); Object.keys(t.derive || {}).forEach(function (k) { all[k] = calc(t.derive[k], all); });
    var v = { id: item.id, tier: item.tier, q: fill(t.q, all), hint: fill(t.hint, all), slips: [], easier: item.easier, variantKey: JSON.stringify(env), isVariant: true, base: item };
    if (t.answers) {                                    // several ordered boxes
      v.type = 'fields'; v.frame = fill(t.frame, all, Object.keys(t.answers));     // box names stay as boxes even when a number has the same name
      v.fields = Object.keys(t.answers).map(function (k) { return { id: k, answer: calc(t.answers[k], all), pad: t.pad && t.pad[k] ? t.pad[k] : 0 }; });
      all.ans = v.fields.map(function (f) { return f.answer; }).join(', ');
    } else if (t.options) {                             // templated choice
      v.type = 'choice'; v.options = t.options.map(function (o) { return fill(o, all); }); v.answer = v.options[calc(t.answer_index, all)]; all.ans = v.answer;
    } else {
      all.ans = calc(t.answer, all);
      if (Array.isArray(all.ans)) { v.type = 'set'; v.answer = all.ans; v.ordered = !!t.ordered; } else { v.type = 'number'; v.answer = all.ans; }
    }
    v.steps = t.steps.map(function (s) { return fill(s, all); });
    if (item.svg) v.svg = (t.svgs && t.svgs[JSON.stringify(env)]) || null;       // a picture only if one was drawn for these numbers
    return v;
  }

  // ---- reading an answer
  function nums(s) { return (String(s).replace(/,/g, ' ').match(/-?\d+(\.\d+)?/g) || []).map(Number); }
  function sameSet(a, b) { var x = a.slice().sort(function (p, r) { return p - r; }), y = b.slice().sort(function (p, r) { return p - r; }); return x.length === y.length && x.every(function (v, i) { return v === y[i]; }); }
  function readAnswer(item) {
    var f = document.querySelector('#ans input, #ans textarea');
    if (item.type === 'fields') { var o = {}; Array.prototype.forEach.call(document.querySelectorAll('#ans input'), function (i) { o[i.getAttribute('data-f')] = nums(i.value)[0]; }); return o; }
    if (item.type === 'number') return nums(f.value)[0];
    if (item.type === 'set') return nums(f.value);
    if (item.type === 'multi') return Array.prototype.map.call(document.querySelectorAll('#ans input:checked'), function (c) { return +c.value; });
    if (item.type === 'choice') { var c = document.querySelector('#ans input:checked'); return c ? c.value : null; }
    return null;
  }
  function judge(item, a) {
    if (item.type === 'fields') { var bad = item.fields.filter(function (f) { return a[f.id] == null || isNaN(a[f.id]); }); if (bad.length) return { empty: true }; var wrong = item.fields.filter(function (f) { return a[f.id] !== f.answer; }).map(function (f) { return f.id; }); return { ok: !wrong.length, wrong: wrong }; }
    if (a == null || (Array.isArray(a) && !a.length && item.type === 'set') || (typeof a === 'number' && isNaN(a))) return { empty: true };
    if (item.type === 'number') return { ok: a === item.answer };
    if (item.type === 'choice') return { ok: a === item.answer };
    if (item.ordered) return { ok: a.length === item.answer.length && a.every(function (v, i) { return v === item.answer[i]; }), part: a.some(function (v) { return item.answer.indexOf(v) > -1; }), extra: a.some(function (v) { return item.answer.indexOf(v) < 0; }), fewer: a.length < item.answer.length, order: a.length === item.answer.length && sameSet(a, item.answer) };
    return { ok: sameSet(a, item.answer), part: a.some(function (v) { return item.answer.indexOf(v) > -1; }), extra: a.some(function (v) { return item.answer.indexOf(v) < 0; }), fewer: a.length < item.answer.length };
  }
  function slipFor(item, a) {
    var out = null;
    (item.slips || []).forEach(function (s) {
      var vals = s.a, hit = Array.isArray(a) ? (vals.length === a.length && (item.ordered ? vals.every(function (v, i) { return a[i] === v; }) : vals.every(function (v) { return a.indexOf(v) > -1; }))) : vals.indexOf(a) > -1;
      if (hit && !out) out = s.say;
    });
    return out;
  }
  function show(a, item) { if (item && item.type === 'fields') return item.frame.replace(/\{(\w+)\}/g, function (m, k) { var f = item.fields.filter(function (f) { return f.id === k; })[0]; return f ? (f.pad && String(f.answer).length < f.pad ? ('0000'.slice(0, f.pad - String(f.answer).length) + f.answer) : f.answer) : m; }); return Array.isArray(a) ? a.join(', ') : String(a); }

  function items() { return L.items.filter(function (i) { return i.tier === tier; }); }
  function current() { var it = items()[idx]; return st[it.id] && st[it.id].variant ? st[it.id].variant : it; }
  function ensure(it) { st[it.id] = st[it.id] || { tries: 0 }; return st[it.id]; }

  function renderTiers() {
    var t = $('tiers'); t.textContent = '';
    ['core', 'stretch', 'challenge'].forEach(function (k) { t.appendChild(h('button', { type: 'button', text: TIER[k], 'aria-pressed': String(k === tier), on: { click: function () { tier = k; idx = 0; render(); } } })); });
    var d = $('dots'); d.textContent = '';
    items().forEach(function (it, i) { d.appendChild(h('button', { type: 'button', text: String(i + 1), class: saved[it.id] ? 'done' : '', 'aria-label': 'Question ' + (i + 1) + (saved[it.id] ? ', done' : ''), 'aria-current': String(i === idx), on: { click: function () { idx = i; render(); } } })); });
  }
  function shuffled(item) {
    if (!item._order) { var a = item.options.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } item._order = a; }
    return item._order;
  }
  function control(item) {
    var box = h('div', { id: 'ans', class: 'row' });
    if (item.type === 'fields') {
      box = h('div', { id: 'ans', class: 'row' });
      item.frame.split(/(\{\w+\})/).forEach(function (part) { var m = /^\{(\w+)\}$/.exec(part); if (m && !item.fields.some(function (f) { return f.id === m[1]; })) m = null; if (m) box.appendChild(h('input', { type: 'text', inputmode: 'numeric', autocomplete: 'off', size: '3', style: 'width:4.2rem;text-align:center', 'data-f': m[1], 'aria-label': 'Box ' + m[1] })); else if (part) box.appendChild(h('span', { text: part, style: 'font-size:1.15em;font-weight:700' })); });
    }
    if (item.type === 'number') box.appendChild(h('input', { type: 'text', inputmode: 'decimal', autocomplete: 'off', 'aria-label': 'Your answer', id: 'ansf' }));
    if (item.type === 'set') { box.appendChild(h('input', { type: 'text', inputmode: 'numeric', autocomplete: 'off', 'aria-label': 'Your answers, separated by commas' })); }
    if (item.type === 'multi') item.options.forEach(function (o) { box.appendChild(h('label', { class: 'opt' }, [h('input', { type: 'checkbox', value: String(o) }), String(o)])); });
    if (item.type === 'choice') shuffled(item).forEach(function (o) { box.appendChild(h('label', { class: 'opt' }, [h('input', { type: 'radio', name: 'c', value: o }), o])); });
    if (item.type === 'selfcheck') { box = h('div', { id: 'ans' }, [h('textarea', { 'aria-label': 'Your answer', placeholder: 'Write here…' })]); }
    return box;
  }
  function stepsBlock(item, title) { return h('div', {}, [h('h2', { text: title || 'How it works' }), h('ol', {}, item.steps.map(function (s) { return h('li', { text: s }); }))]); }

  function render() {
    renderTiers();
    var base = items()[idx], item = current(), s = ensure(base), card = $('card'); card.textContent = '';
    card.appendChild(h('p', { class: 'q', text: item.q }));
    if (item.svg) { var fig = h('div', { class: 'fig', style: 'max-width:30rem;margin:0 0 1rem' }); var doc = new DOMParser().parseFromString(item.svg, 'image/svg+xml').documentElement; if (doc && doc.nodeName === 'svg') { Array.prototype.forEach.call(doc.querySelectorAll('script,foreignObject'), function (x) { x.remove(); }); fig.appendChild(document.importNode(doc, true)); card.appendChild(fig); } }
    if (item.type === 'multi' || item.type === 'set') card.appendChild(h('p', { class: 'sub', style: 'margin:0 0 .5rem', text: item.type === 'multi' ? 'Tick every one that fits.' : 'Type every answer, with a comma between.' }));
    card.appendChild(control(item));
    var fb = h('div', { id: 'fb', 'aria-live': 'polite' });
    var row = h('div', { class: 'row', style: 'margin-top:1rem' });
    var done = s.state === 'ok' || s.state === 'shown';
    if (item.type === 'selfcheck') {
      row.appendChild(h('button', { type: 'button', class: 'act', text: item.button || 'Show me how to check', on: { click: function () { var ta = card.querySelector('textarea'); fb.textContent = ''; fb.appendChild(box('plain', stepsBlock(item, 'How to check it'))); if (ta && ta.value.trim()) { saved[base.id] = 1; persist(); renderTiers(); } extra(row, base, item, true); } } }));
    } else if (!done) {
      row.appendChild(h('button', { type: 'button', class: 'act', text: 'Check', on: { click: function () { check(base, item, s, fb, row); } } }));
      row.appendChild(h('button', { type: 'button', class: 'act quiet', text: 'Give me a hint', on: { click: function () { fb.textContent = ''; fb.appendChild(box('plain', h('p', { text: 'Hint: ' + item.hint }))); } } }));
    }
    card.appendChild(row); card.appendChild(fb);
    if (done) { fb.appendChild(box(s.state === 'ok' ? 'ok' : 'try', s.state === 'ok' ? [h('h2', { text: 'Yes, that is right.' }), stepsBlock(item)] : [h('h2', { text: 'Let us look at it together.' }), h('p', { text: 'The answer is ' + show(item.answer, item) + '.' }), stepsBlock(item, 'Here is how to get it')])); extra(row, base, item, false); }
    var inp = card.querySelector('input[type=text],textarea'); if (inp && !done) { try { inp.focus({ preventScroll: true }); } catch (e) {} }
    if (inp && !done) inp.addEventListener('keydown', function (e) { if (e.key === 'Enter' && inp.tagName === 'INPUT') check(base, item, s, fb, row); });
  }
  function box(cls, kids) { var d = h('div', { class: 'fb ' + cls }); [].concat(kids).forEach(function (k) { d.appendChild(k); }); return d; }

  function check(base, item, s, fb, row) {
    var a = readAnswer(item), j = judge(item, a); fb.textContent = '';
    var raw = (document.querySelector('#ans input[type=text]') || {}).value;
    if (item.type === 'number' && raw && raw.trim()) {
      if (!/\d/.test(raw)) { fb.appendChild(box('plain', h('p', { text: 'Please type the answer with number digits, like 54.' }))); return; }
      if (nums(raw).length > 1) { fb.appendChild(box('plain', h('p', { text: 'Please type just the answer number.' }))); return; }
    }
    if (j.empty && item.type === 'fields') { fb.appendChild(box('plain', h('p', { text: 'Type a number in every box. It is fine to guess.' }))); return; }
    if (j.empty) { fb.appendChild(box('plain', h('p', { text: 'Type or choose an answer first. It is fine to guess.' }))); return; }
    if (j.ok) { s.state = 'ok'; saved[base.id] = 1; persist(); render(); return; }
    var sig = JSON.stringify(a); if (s.tries === 1 && s.last === sig) { fb.appendChild(box('plain', h('p', { text: 'That is the same answer as before. Read the hint and try a different one.' }))); return; }
    s.last = sig; s.tries++;
    if (s.tries === 1) {
      var slip = slipFor(item, a), msg = slip || (j.order ? 'Those are the right numbers, but not in the right order. Check the order.' : j.part && item.type !== 'number' ? (j.extra ? 'Some of these fit, but one does not. Check each one.' : 'Those fit. Are there more? Keep looking.') : 'Not quite yet. Have another go.');
      if (j.wrong) { Array.prototype.forEach.call(document.querySelectorAll('#ans input'), function (i) { if (j.wrong.indexOf(i.getAttribute('data-f')) > -1) i.style.borderColor = '#B5481F'; }); msg = 'Look again at the boxes with a red edge.'; }
      fb.appendChild(box('try', [h('h2', { text: 'Not yet. Try once more.' }), h('p', { text: msg }), h('p', { class: 'sub', style: 'margin:.4rem 0 0', text: 'Hint: ' + item.hint })]));
    } else { s.state = 'shown'; saved[base.id] = 1; persist(); render(); }
  }
  function extra(row, base, item, selfcheck) {
    var s = ensure(base);
    if (base.tpl) row.appendChild(h('button', { type: 'button', class: 'act', text: 'Try a similar one', on: { click: function () { st[base.id] = { tries: 0, variant: variantOf(base, s.variant && s.variant.variantKey) }; render(); } } }));
    if (item.easier && s.state === 'shown') row.appendChild(h('button', { type: 'button', class: 'act quiet', text: 'Try an easier one first', on: { click: function () { var e = L.items.filter(function (i) { return i.id === item.easier; })[0]; tier = e.tier; idx = items().indexOf(e); render(); } } }));
    row.appendChild(h('button', { type: 'button', class: 'act' + (base.tpl ? ' quiet' : ''), text: idx < items().length - 1 ? 'Next question' : 'Back to the first one', on: { click: function () { idx = (idx + 1) % items().length; render(); window.scrollTo(0, 0); } } }));
  }

  fetch('data/' + key + '.json').then(function (r) { if (!r.ok) throw new Error('missing'); return r.json(); }).then(function (d) {
    L = d; document.title = 'Practice: ' + L.title + ' | Math Inquirers';
    $('title').textContent = L.title + ' practice'; $('sub').textContent = 'Level ' + L.level + ' · Lesson ' + L.lesson + ' · ' + L.topic;
    if (!TIER[tier]) tier = 'core'; render();
  }).catch(function () {
    $('title').textContent = 'Practice'; $('card').textContent = 'This practice link is not complete. Please ask your tutor for the right link.';
  });
})();
