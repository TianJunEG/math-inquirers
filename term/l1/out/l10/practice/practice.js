// Online practice runner. Static: the lesson file holds the questions, answers, hints, worked solutions and variants.
// Rules: no timers, no scores, no streaks, no leaderboard. Wrong answers get a hint, then a worked solution.
(function () {
  var q = new URLSearchParams(location.search), key = q.get('lesson') || 'p3l3';
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
  function calc(expr, env) {
    var s = expr; Object.keys(env).sort(function (a, b) { return b.length - a.length; }).forEach(function (k) { s = s.replace(new RegExp('\\b' + k + '\\b', 'g'), env[k]); });
    var m = /^\s*(\d+)\s*\/\/\s*(\d+)\s*$/.exec(s); if (m) return Math.floor(+m[1] / +m[2]);
    if (!/^[\d\s+\-*/%().]*$/.test(s)) throw new Error('bad expression');
    return Function('"use strict";return (' + s + ')')();
  }
  function fill(str, env) { return String(str).replace(/\{(\w+)\}/g, function (m, k) { return env[k] != null ? env[k] : m; }); }
  function variantOf(item, avoid) {
    var t = item.tpl, names = Object.keys(t.vars), env, tries = 0;
    do { env = {}; names.forEach(function (n) { var a = t.vars[n]; env[n] = a[Math.floor(Math.random() * a.length)]; }); tries++; } while (avoid && JSON.stringify(env) === avoid && tries < 12);
    var all = Object.assign({}, env); Object.keys(t.derive || {}).forEach(function (k) { all[k] = calc(t.derive[k], all); });
    all.ans = calc(t.answer, all);
    return { id: item.id, tier: item.tier, type: 'number', q: fill(t.q, all), answer: all.ans, hint: fill(t.hint, all), steps: t.steps.map(function (s) { return fill(s, all); }), slips: [], easier: item.easier, variantKey: JSON.stringify(env), isVariant: true, base: item };
  }

  // ---- reading an answer
  function nums(s) { return (String(s).replace(/,/g, ' ').match(/-?\d+(\.\d+)?/g) || []).map(Number); }
  function sameSet(a, b) { var x = a.slice().sort(function (p, r) { return p - r; }), y = b.slice().sort(function (p, r) { return p - r; }); return x.length === y.length && x.every(function (v, i) { return v === y[i]; }); }
  function readAnswer(item) {
    var f = document.querySelector('#ans input, #ans textarea');
    if (item.type === 'number') return nums(f.value)[0];
    if (item.type === 'set') return nums(f.value);
    if (item.type === 'multi') return Array.prototype.map.call(document.querySelectorAll('#ans input:checked'), function (c) { return +c.value; });
    if (item.type === 'choice') { var c = document.querySelector('#ans input:checked'); return c ? c.value : null; }
    return null;
  }
  function judge(item, a) {
    if (a == null || (Array.isArray(a) && !a.length && item.type === 'set') || (typeof a === 'number' && isNaN(a))) return { empty: true };
    if (item.type === 'number') return { ok: a === item.answer };
    if (item.type === 'choice') return { ok: a === item.answer };
    return { ok: sameSet(a, item.answer), part: a.some(function (v) { return item.answer.indexOf(v) > -1; }), extra: a.some(function (v) { return item.answer.indexOf(v) < 0; }), fewer: a.length < item.answer.length };
  }
  function slipFor(item, a) {
    var out = null;
    (item.slips || []).forEach(function (s) {
      var vals = s.a, hit = Array.isArray(a) ? (vals.length === a.length && vals.every(function (v) { return a.indexOf(v) > -1; })) : vals.indexOf(a) > -1;
      if (hit && !out) out = s.say;
    });
    return out;
  }
  function show(a) { return Array.isArray(a) ? a.join(', ') : String(a); }

  function items() { return L.items.filter(function (i) { return i.tier === tier; }); }
  function current() { var it = items()[idx]; return st[it.id] && st[it.id].variant ? st[it.id].variant : it; }
  function ensure(it) { st[it.id] = st[it.id] || { tries: 0 }; return st[it.id]; }

  function renderTiers() {
    var t = $('tiers'); t.textContent = '';
    ['core', 'stretch', 'challenge'].forEach(function (k) { t.appendChild(h('button', { type: 'button', text: TIER[k], 'aria-pressed': String(k === tier), on: { click: function () { tier = k; idx = 0; render(); } } })); });
    var d = $('dots'); d.textContent = '';
    items().forEach(function (it, i) { d.appendChild(h('button', { type: 'button', text: String(i + 1), class: saved[it.id] ? 'done' : '', 'aria-label': 'Question ' + (i + 1) + (saved[it.id] ? ', done' : ''), 'aria-current': String(i === idx), on: { click: function () { idx = i; render(); } } })); });
  }
  function control(item) {
    var box = h('div', { id: 'ans', class: 'row' });
    if (item.type === 'number') box.appendChild(h('input', { type: 'text', inputmode: 'decimal', autocomplete: 'off', 'aria-label': 'Your answer', id: 'ansf' }));
    if (item.type === 'set') { box.appendChild(h('input', { type: 'text', inputmode: 'numeric', autocomplete: 'off', 'aria-label': 'Your answers, separated by commas' })); }
    if (item.type === 'multi') item.options.forEach(function (o) { box.appendChild(h('label', { class: 'opt' }, [h('input', { type: 'checkbox', value: String(o) }), String(o)])); });
    if (item.type === 'choice') item.options.forEach(function (o) { box.appendChild(h('label', { class: 'opt' }, [h('input', { type: 'radio', name: 'c', value: o }), o])); });
    if (item.type === 'selfcheck') { box = h('div', { id: 'ans' }, [h('textarea', { 'aria-label': 'Your riddle', placeholder: 'Write your riddle here…' })]); }
    return box;
  }
  function stepsBlock(item, title) { return h('div', {}, [h('h2', { text: title || 'How it works' }), h('ol', {}, item.steps.map(function (s) { return h('li', { text: s }); }))]); }

  function render() {
    renderTiers();
    var base = items()[idx], item = current(), s = ensure(base), card = $('card'); card.textContent = '';
    card.appendChild(h('p', { class: 'q', text: item.q }));
    if (item.type === 'multi' || item.type === 'set') card.appendChild(h('p', { class: 'sub', style: 'margin:0 0 .5rem', text: item.type === 'multi' ? 'Tick every one that fits.' : 'Type every answer, with a comma between.' }));
    card.appendChild(control(item));
    var fb = h('div', { id: 'fb', 'aria-live': 'polite' });
    var row = h('div', { class: 'row', style: 'margin-top:1rem' });
    var done = s.state === 'ok' || s.state === 'shown';
    if (item.type === 'selfcheck') {
      row.appendChild(h('button', { type: 'button', class: 'act', text: 'Check my riddle', on: { click: function () { fb.textContent = ''; fb.appendChild(box('plain', stepsBlock(item, 'How to check it'))); saved[base.id] = 1; persist(); renderTiers(); extra(row, base, item, true); } } }));
    } else if (!done) {
      row.appendChild(h('button', { type: 'button', class: 'act', text: 'Check', on: { click: function () { check(base, item, s, fb, row); } } }));
      row.appendChild(h('button', { type: 'button', class: 'act quiet', text: 'Give me a hint', on: { click: function () { fb.textContent = ''; fb.appendChild(box('plain', h('p', { text: 'Hint: ' + item.hint }))); } } }));
    }
    card.appendChild(row); card.appendChild(fb);
    if (done) { fb.appendChild(box(s.state === 'ok' ? 'ok' : 'try', s.state === 'ok' ? [h('h2', { text: 'Yes, that is right.' }), stepsBlock(item)] : [h('h2', { text: 'Let us look at it together.' }), h('p', { text: 'The answer is ' + show(item.answer) + '.' }), stepsBlock(item, 'Here is how to get it')])); extra(row, base, item, false); }
    var inp = card.querySelector('input[type=text],textarea'); if (inp && !done) inp.addEventListener('keydown', function (e) { if (e.key === 'Enter' && inp.tagName === 'INPUT') check(base, item, s, fb, row); });
  }
  function box(cls, kids) { var d = h('div', { class: 'fb ' + cls }); [].concat(kids).forEach(function (k) { d.appendChild(k); }); return d; }

  function check(base, item, s, fb, row) {
    var a = readAnswer(item), j = judge(item, a); fb.textContent = '';
    if (j.empty) { fb.appendChild(box('plain', h('p', { text: 'Type or choose an answer first. It is fine to guess.' }))); return; }
    if (j.ok) { s.state = 'ok'; saved[base.id] = 1; persist(); render(); return; }
    s.tries++;
    if (s.tries === 1) {
      var slip = slipFor(item, a), msg = slip || (j.part && item.type !== 'number' ? (j.extra ? 'Some of these fit, but one does not. Check each one.' : 'Those fit. Are there more? Keep looking.') : 'Not quite yet. Have another go.');
      fb.appendChild(box('try', [h('h2', { text: 'Nearly. Try once more.' }), h('p', { text: msg }), h('p', { class: 'sub', style: 'margin:.4rem 0 0', text: 'Hint: ' + item.hint })]));
    } else { s.state = 'shown'; saved[base.id] = 1; persist(); render(); }
  }
  function extra(row, base, item, selfcheck) {
    var s = ensure(base);
    if (base.tpl) row.appendChild(h('button', { type: 'button', class: 'act', text: 'Try a similar one', on: { click: function () { st[base.id] = { tries: 0, variant: variantOf(base, s.variant && s.variant.variantKey) }; render(); } } }));
    if (item.easier && s.state === 'shown') row.appendChild(h('button', { type: 'button', class: 'act quiet', text: 'Try an easier one first', on: { click: function () { var e = L.items.filter(function (i) { return i.id === item.easier; })[0]; tier = e.tier; idx = items().indexOf(e); render(); } } }));
    row.appendChild(h('button', { type: 'button', class: 'act' + (base.tpl ? ' quiet' : ''), text: idx < items().length - 1 ? 'Next question' : 'Back to the first one', on: { click: function () { idx = (idx + 1) % items().length; render(); window.scrollTo(0, 0); } } }));
  }

  fetch('/data/' + key + '.json').then(function (r) { return r.json(); }).then(function (d) {
    L = d; document.title = 'Practice: ' + L.title + ' | Math Inquirers';
    $('title').textContent = L.title + ' practice'; $('sub').textContent = 'Level ' + L.level + ' · Lesson ' + L.lesson + ' · ' + L.topic;
    if (!TIER[tier]) tier = 'core'; render();
  });
})();
