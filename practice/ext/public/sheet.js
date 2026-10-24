// Worksheet-style online practice (extension units, and reusable for term and holiday data in the same item format).
// The child can open any question in any order, skip, change answers, then submit. Marking and full worked solutions appear only after
// submitting. By default everything stays on this device (localStorage, guarded): no account, nothing is sent anywhere. No timer, score, streak or ranking.
// OPTIONAL SEND TO TUTOR (feature flag, OFF): only if the page sets window.MI_SUBMIT = {endpoint: '...'} AND a child session token exists
// (MI_SUBMIT.token, or sessionStorage 'mi-child'.token from the portal child sign-in) does Submit also POST the answers (never a mark) to the endpoint.
// The server marks again from its own key. Without the flag, or without a token, this file makes no network request except loading its own data file.
// See docs/online_submission_design.md.
(function () {
  var key = window.MI_LESSON, $ = function (id) { return document.getElementById(id); };
  var TIERS = [['core', 'Start here'], ['invest', 'Investigation'], ['stretch', 'Think harder'], ['challenge', 'Go further'], ['check', 'Check yourself']];
  var L, cur = 0, S = { a: {}, sub: false, sid: '', rev: 0, sent: 0, self: {} }, ask = false, sim = {};
  var EXPLAIN_MAX = 500;   // characters of a typed explanation that may be sent to the tutor (the server enforces the same cap)
  var CFG = (typeof window.MI_SUBMIT === 'object' && window.MI_SUBMIT) || null, SY = { msg: '', busy: false, tries: 0, timer: 0, selfTimer: 0 }, VER = '';
  function load() { try { var o = JSON.parse(localStorage.getItem('mi-sheet-' + key) || '{}'); if (o && o.a) S = { a: o.a, sub: !!o.sub, sid: String(o.sid || ''), rev: o.rev | 0, sent: o.sent | 0, self: o.self || {} }; } catch (e) {} }
  function save() { try { localStorage.setItem('mi-sheet-' + key, JSON.stringify(S)); } catch (e) {} }
  function h(tag, at, kids) {
    var e = document.createElement(tag);
    Object.keys(at || {}).forEach(function (k) { if (k === 'text') e.textContent = at[k]; else if (k === 'on') Object.keys(at.on).forEach(function (n) { e.addEventListener(n, at.on[n]); }); else e.setAttribute(k, at[k]); });
    (kids || []).forEach(function (c) { if (c) e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return e;
  }
  // ---- small shared styles (skip link, hidden labels, focus ring on the question, placeholder contrast); uses the page's own colour variables
  (function () {
    var st = document.createElement('style');
    st.textContent = '.sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}' +
      '.skip{position:absolute;left:8px;top:-4rem;z-index:5;background:var(--ink);color:var(--card,#fff);padding:.7rem 1rem;border-radius:10px;font-weight:800;text-decoration:none}.skip:focus{top:8px;outline:3px solid var(--focus)}' +
      '.q:focus,#summary:focus,#askbox:focus,#hintbox:focus{outline:3px solid var(--focus);outline-offset:4px;border-radius:6px}' +
      'fieldset.row{border:0;padding:0;margin:0;min-width:0}textarea::placeholder,input::placeholder{color:var(--mut);opacity:1}.nb{padding:0 .45rem}.nb b{white-space:nowrap}' +
      '.helper{margin:0 0 .5rem;font-weight:700}' +
      '.fg{display:inline-flex;flex-wrap:nowrap;align-items:center;gap:.25rem;max-width:100%;vertical-align:middle}.fg .fl{flex:0 1 auto;min-width:2.5rem}.fg .ft,.fg input{flex:0 0 auto}.fg .ft{white-space:nowrap}' +
      '.card svg,.fb svg{overflow:visible}';
    document.head.appendChild(st);
  })();
  // ---- reading and judging
  // BEGIN SHARED (this block is identical in practice/ext/public/sheet.js and practice/submit/mark.js; mark.test.mjs checks it)
  // Reading numbers. A single number: a thousands separator (comma or one space) is allowed only in valid groups (1,000 / 12 500), a leading $ or a unicode minus
  // is ignored/normalised, a final full stop or .0 ('29.', '20.0') is ignored, and a unit word after the number ('301 sticks', '20 min') is ignored unless the item says unit:false.
  // opt.pre = text printed just before the box ('6:' for a box in '6:{f1}'), which the child may repeat ('6:20').
  function str(s) { return String(s == null ? '' : s); }
  function minus(s) { return str(s).replace(/[−–—‐‑]/g, '-'); }
  // Number words ('five', 'twenty-five', 'one hundred and five', 'minus five') are read ONLY when the item declares words:true (no default).
  var NW = { zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, ten: 10, eleven: 11, twelve: 12, thirteen: 13, fourteen: 14, fifteen: 15, sixteen: 16, seventeen: 17, eighteen: 18, nineteen: 19, twenty: 20, thirty: 30, forty: 40, fifty: 50, sixty: 60, seventy: 70, eighty: 80, ninety: 90 };
  function wordsToNum(s) {
    var t = str(s).normalize('NFKC').toLowerCase().replace(/[-,]/g, ' ').replace(/\band\b/g, ' ').replace(/\s+/g, ' ').trim().replace(/[.!]+$/, ''), neg = false, ws, i, w, chunk = 0, cur = 0, total = 0, hund = false, seen = false;
    if (/^(minus|negative) /.test(t)) { neg = true; t = t.replace(/^\S+ /, ''); }
    if (!t) return null;
    ws = t.split(' ');
    for (i = 0; i < ws.length; i++) {
      w = ws[i];
      if (NW[w] !== undefined) {
        if (NW[w] >= 20) { if (chunk) return null; chunk = NW[w]; }
        else if (NW[w] > 0 || ws.length === 1) { if (chunk && !(chunk >= 20 && chunk % 10 === 0 && NW[w] < 10)) return null; chunk += NW[w]; }
        else return null;
        seen = true;
      } else if (w === 'hundred') { if (hund || chunk < 1 || chunk > 9) return null; cur = chunk * 100; chunk = 0; hund = true; }
      else if (w === 'thousand') { if (cur + chunk < 1 || total) return null; total = (cur + chunk) * 1000; cur = 0; chunk = 0; hund = false; }
      else return null;
    }
    if (!seen && !total && !cur) return null;
    var v = total + cur + chunk; return neg ? -v : v;
  }
  // Units after the number: a word ('301 sticks', '20 minutes', 'sq cm'), a word with an attached power ('84 cm2', '84cm^2', '84 cm²'), a rate ('km/h') or a degree sign ('-25 °C', '11°C', '44°').
  // A single pair of brackets round the whole answer is ignored ('(-25)'). Two numbers ('4 or 5', '1 2') are never a unit.
  var UW = '[a-z][a-z.]*(?:\\^?[23]|\\s?[²³])?', UNITRE = new RegExp('^(-?\\d[\\d, ]*?(?:\\.0+)?)\\s*(?:[°º]\\s*[a-z]?|' + UW + '(?:\\s+' + UW + ')*(?:\\/[a-z]+)?)$', 'i');
  function toNum(s, opt) {
    s = minus(s).trim();
    var pb = /^\(\s*([^()]*?)\s*\)\s*(.*)$/.exec(s); if (pb) s = pb[2] ? pb[1] + ' ' + pb[2] : pb[1];   // '(-25)' and '(-25) °C'
    if (opt && opt.words) { var wn = wordsToNum(s); if (wn !== null) return wn; }
    s = s.replace(/^\$\s*/, '');
    if (opt && opt.pre && s.indexOf(opt.pre) === 0) s = s.slice(opt.pre.length).trim();
    s = s.replace(/\.0*$/, '');
    if (!opt || opt.unit !== false) { var u = UNITRE.exec(s); if (u) s = u[1].trim().replace(/\.0+$/, ''); }
    if (/^-?\d{1,3}(?:[, ]\d{3})+$/.test(s)) s = s.replace(/[, ]/g, '');
    return /^-?\d+$/.test(s) ? +s : null;
  }
  // Reading a typed list. Rule: a comma or space is a thousands separator ONLY when the item is 'grouped' (its answers are 5-digit or longer numbers, or the item
  // says grouped:true) AND the run is a leading group of 1-3 digits followed only by groups of exactly 3 digits joined by a comma or ONE space ('12,500', '12 500').
  // Everything else separates numbers ('250,450', '250, 450', '250 450', '18; 12'). For a grouped item both readings are offered, and the answer is right if either matches.
  function listOf(s) { return (s.match(/-?\d+/g) || []).map(Number); }
  function numsAll(s, grouped) {
    s = minus(s);
    var a = listOf(s);
    if (!grouped) return [a];
    var m = listOf(s.replace(/(^|\D)(\d{1,3}(?:[, ]\d{3})+)(?!\d)/g, function (_, p, g) { return p + g.replace(/[, ]/g, ''); }));
    return a.length === m.length && a.every(function (v, i) { return v === m[i]; }) ? [a] : [a, m];
  }
  function nums(s, grouped) { return numsAll(s, grouped)[0]; }
  function isGrouped(flag, key) { return flag != null ? !!flag : (Array.isArray(key) ? key : [key]).some(function (k) { return typeof k === 'number' && Math.abs(k) >= 10000; }); }
  function sameSet(a, b) { var x = a.slice().sort(function (p, r) { return p - r; }), y = b.slice().sort(function (p, r) { return p - r; }); return x.length === y.length && x.every(function (v, i) { return v === y[i]; }); }
  function setMatch(v, key, ordered, grouped) { // -> {ok, a: the reading that matched (or the first reading)}
    var ps = numsAll(v, isGrouped(grouped, key)), best = ps[0], ok = false;
    ps.forEach(function (a) { var o = ordered ? (a.length === key.length && a.every(function (x, i) { return x === key[i]; })) : sameSet(a, key); if (o && !ok) { ok = true; best = a; } });
    return { ok: ok, a: best };
  }
  // Reading words and expressions: only case, spacing, x * times, unicode minus and a final full stop are normalised. A minus sign is never dropped and the space in a
  // mixed number ('5 1/2') is kept, so '-1/2' is not '1/2', '(6+4)x5-2' is not '(6+4)x52' and '1 1/2' is not '11/2'. A hyphen between two letters is a space ('north-west').
  function normText(s) {
    return minus(str(s).normalize('NFKC')).toLowerCase().replace(/[×*·⋅]/g, 'x').replace(/÷/g, '/').replace(/\s+/g, ' ').trim().replace(/[.!]+$/, '').trim()
      .replace(/([a-z])-(?=[a-z])/g, '$1 ');
  }
  function squash(s) { return normText(s).replace(/(\d) (?=\d)/g, '$1\u0001').replace(/ /g, '').replace(/\u0001/g, ' '); }
  function evalExpr(s) { // digits, + - x / ( ) only; null if it is not such an expression
    s = normText(s).replace(/x/g, '*').replace(/\s/g, '');
    if (!/^[\d+\-*\/().]+$/.test(s)) return null;
    var t = s.match(/[\d.]+|[-+*\/()]/g) || [], p = 0, bad = false;
    function prim() { var x = t[p++]; if (x === '(') { var v = sum(); if (t[p++] !== ')') bad = true; return v; } if (x === '-') return -prim(); if (x == null || !/^[\d.]+$/.test(x)) { bad = true; return 0; } return parseFloat(x); }
    function prod() { var v = prim(); while (t[p] === '*' || t[p] === '/') { var o = t[p++], r = prim(); v = o === '*' ? v * r : v / r; } return v; }
    function sum() { var v = prod(); while (t[p] === '+' || t[p] === '-') { var o = t[p++], r = prod(); v = o === '+' ? v + r : v - r; } return v; }
    var out = sum(); return bad || p < t.length || !isFinite(out) ? null : out;
  }
  function textOK(keys, v) {
    var cands = [v], m = /^(.*[\d)])\s*=\s*(-?[\d.\/ ]*\d)\s*[.!]?$/.exec(minus(str(v)).trim()); // a statement with its result: '(6+4)x5-2=48'
    if (m) { var l = evalExpr(m[1]), r = evalExpr(m[2].replace(/(\d) (\d+\/\d)/, '($1+$2)').replace(/ /g, '')); if (l != null && r != null && Math.abs(l - r) < 1e-9) cands.push(m[1]); }
    var m2 = /^(-?[\d.\/ ]*\d)\s*=\s*(.*[\d)])\s*[.!]?$/.exec(minus(str(v)).trim()); // the result first: '5/12=1/3+1/12'
    if (m2) { var r2 = evalExpr(m2[1].replace(/(\d) (\d+\/\d)/, '($1+$2)').replace(/ /g, '')), l2 = evalExpr(m2[2]); if (l2 != null && r2 != null && Math.abs(l2 - r2) < 1e-9) cands.push(m2[2]); }
    return keys.some(function (x) { return cands.some(function (c) { return normText(x) === normText(c) || squash(x) === squash(c); }); });
  }
  // Equal fractions in a typed list (item flag equiv_frac): '7/12, 8/12, 10/12' is right for the key '7/12, 2/3, 5/6'. Same order, same number of fractions, each equal in value
  // (cross-multiplied); any other symbol (such as < or >) must match the key. Without the flag only the printed forms are accepted.
  function fracTok(s) {
    var t = [], rest = minus(str(s).normalize('NFKC')).replace(/\s*\/\s*/g, '/').replace(/(-?)(\d+)\s+(\d+)\/(\d+)|(-?\d+)\/(\d+)|-?\d+/g, function (m, sg, w, a, b, n2, d2) {
      var f = w !== undefined ? { n: (+w * +b + +a) * (sg ? -1 : 1), d: +b } : n2 !== undefined ? { n: +n2, d: +d2 } : { n: +m, d: 1 };
      t.push(f); return ' ';
    });
    return { t: t, rest: rest.replace(/[\s,;]+/g, '').replace(/[.!]+$/, '') };
  }
  function fracListOK(keys, v) {
    var V = fracTok(v);
    return V.t.length > 0 && V.t.every(function (f) { return f.d > 0; }) && keys.some(function (k) {
      var K = fracTok(k);
      return K.t.length === V.t.length && K.rest === V.rest && K.t.every(function (f, i) { return f.d > 0 && f.n * V.t[i].d === V.t[i].n * f.d; });
    });
  }
  // Algebra rules (item flag poly:'n'): the typed rule is compared with the key as a POLYNOMIAL in n. A tiny recursive-descent parser (digits, the letter, + - x * / ( ) ^ and writing side by side
  // such as 4n or 4(n+3)); division only by a number. Nothing is ever evaluated as code. '(n+3)x4 = 4n+12' and 'OUT = 4(n+3)' are chains of '=': every side that is not the word OUT must equal the key.
  function polyParse(s, vr) {
    s = minus(str(s).replace(/²/g, '^2').replace(/³/g, '^3').normalize('NFKC')).toLowerCase().replace(/[×·⋅*]/g, '*').replace(/÷/g, '/');   // the powers first: NFKC would turn ² into a plain 2
    if (vr !== 'x') s = s.replace(/x/g, '*');
    if (/\d\s+\d/.test(s)) return null;
    var t = s.replace(/\s+/g, '').match(/\d+\.?\d*|\.\d+|[-+*\/()^]|./g) || [], p = 0, bad = false;
    function num(x) { return x != null && /^(\d+\.?\d*|\.\d+)$/.test(x); }
    function mul(a, b) { var r = [], i, j; if (a.length + b.length > 10) { bad = true; return [0]; } for (i = 0; i < a.length; i++) for (j = 0; j < b.length; j++) r[i + j] = (r[i + j] || 0) + a[i] * b[j]; return r; }
    function atom() { var x = t[p++]; if (x === '(') { var v = sum(); if (t[p++] !== ')') bad = true; return v; } if (x === vr) return [0, 1]; if (num(x)) return [parseFloat(x)]; bad = true; return [0]; }
    function pw() { var b = atom(), e, r, i; if (t[p] === '^') { p++; e = t[p++]; if (!/^[0-4]$/.test(e || '')) { bad = true; return b; } r = [1]; for (i = 0; i < +e; i++) r = mul(r, b); return r; } return b; }
    function un() { if (t[p] === '-') { p++; return mul([-1], un()); } if (t[p] === '+') { p++; return un(); } return pw(); }
    function prod() {
      var v = un(), o, d;
      for (;;) {
        o = t[p];
        if (o === '*') { p++; v = mul(v, un()); }
        else if (o === '/') { p++; d = un(); if (d.length !== 1 || d[0] === 0) { bad = true; return v; } v = v.map(function (c) { return c / d[0]; }); }
        else if (o === '(' || o === vr || (num(o) && !num(t[p - 1]))) v = mul(v, pw());
        else return v;
      }
    }
    function sum() { var v = prod(), o, r, i, n; while (t[p] === '+' || t[p] === '-') { o = t[p++]; r = prod(); n = Math.max(v.length, r.length); for (i = 0; i < n; i++) v[i] = (v[i] || 0) + (o === '+' ? 1 : -1) * (r[i] || 0); } return v; }
    var out = sum();
    if (bad || p < t.length) return null;
    while (out.length > 1 && Math.abs(out[out.length - 1]) < 1e-12) out.pop();
    return out.every(isFinite) ? out : null;
  }
  function polyEq(a, b) { return a.length === b.length && a.every(function (c, i) { return Math.abs(c - b[i]) < 1e-9 * (1 + Math.abs(c)); }); }
  function ruleSides(s) { return minus(str(s)).trim().replace(/[.!]+$/, '').split('=').map(function (x) { return x.trim(); }).filter(function (x) { return !/^out$/i.test(x); }); }
  function polyOK(keys, v, vr) {
    vr = typeof vr === 'string' && vr.length === 1 && vr !== 'x' ? vr.toLowerCase() : 'n';
    var kp = [], sides = ruleSides(v);
    keys.forEach(function (k) { ruleSides(k).forEach(function (sd) { var q = polyParse(sd, vr); if (q) kp.push(q); }); });
    return sides.length > 0 && kp.length > 0 && sides.every(function (sd) { var q = polyParse(sd, vr); return !!q && kp.some(function (k) { return polyEq(q, k); }); });
  }
  // One text answer: the printed forms (textOK), plus, only when the item says so, equal fractions (equiv_frac) or an equal polynomial (poly).
  function textMatch(o, keys, v) { return textOK(keys, v) || !!(o && o.equiv_frac && fracListOK(keys, v)) || !!(o && o.poly && polyOK(keys, v, o.poly)); }
  // END SHARED
  function answered(it, v) {
    if (v == null) return false;
    if (it.type === 'fields') return v.some(function (x) { return String(x).trim() !== ''; });
    return String(v).trim() !== '';
  }
  function judge(it, v) {
    if (it.type === 'selfcheck') return 'self';
    if (!answered(it, v)) return 'blank';
    if (it.type === 'choice') return v === it.answer ? 'right' : 'wrong';
    if (it.type === 'text') return textMatch(it, it.answer, v) ? 'right' : 'wrong';
    if (it.type === 'number') return toNum(v, { unit: it.unit, words: it.words }) === it.answer ? 'right' : 'wrong';
    if (it.type === 'fields') return it.fields.every(function (f, i) { return toNum(v[i], { unit: it.unit, words: it.words, pre: f.pre }) === f.answer; }) ? 'right' : 'wrong';
    return setMatch(v, it.answer, it.ordered, it.grouped).ok ? 'right' : 'wrong';
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
  // Short, distinct labels for the question buttons, derived from the printed number (it.no); a lesson may set item.label to override. 'Investigation 2' -> 'Inv 2',
  // 'Think harder 3 (why)' -> 'T3', 'Go further 6' -> 'G6', '1(c) explain' -> '1(c)'. Two questions with the same label get a suffix: '3(d)-a', '3(d)-b'.
  var PREF = [[/^(?:investigation|inv)\b\.?\s*/i, 'Inv', ' '], [/^think harder\b\s*/i, 'T', ''], [/^go further\b\s*/i, 'G', ''], [/^exit slip\b\s*/i, 'Exit', ' '], [/^take-home\b\s*/i, 'Home', ' '], [/^make up your own\b\s*/i, 'Make', ' '], [/^extra\b\s*/i, 'Extra', ' ']];
  var CORE = /^((?:[A-Za-z]?\d+|[A-Z](?![A-Za-z]))\s?(?:\([a-z]\d?\)|\(\d{1,3}\))?|\([a-z]\d?\))/, LBL = { lab: [], dup: [] };
  function shortLabel(it, i) {
    if (it.label) return String(it.label);
    var no = String(it.no == null || String(it.no).trim() === '' ? i + 1 : it.no).trim(), pre = '', sep = '', rest = no, m, k, core = '';
    for (k = 0; k < PREF.length; k++) { m = PREF[k][0].exec(no); if (m) { pre = PREF[k][1]; sep = PREF[k][2]; rest = no.slice(m[0].length); break; } }
    m = CORE.exec(rest); if (m) core = m[1].replace(/\s+/g, ' ').trim();
    if (!pre && it.tier === 'invest' && /^\d/.test(core)) { pre = 'Inv'; sep = ' '; }
    if (pre) return pre + (core ? sep + core : '');
    return core || no.split(/\s+/)[0].slice(0, 8);
  }
  function labelsAll() {
    var base = L.items.map(shortLabel), cnt = {}, seen = {};
    base.forEach(function (b) { cnt[b] = (cnt[b] || 0) + 1; });
    return { lab: base.map(function (b) { if (cnt[b] < 2) return b; seen[b] = (seen[b] || 0) + 1; return b + '-' + (seen[b] <= 26 ? String.fromCharCode(96 + seen[b]) : seen[b]); }), dup: base.map(function (b) { return cnt[b] > 1; }) };
  }
  function say(t) { var a = $('announce'); if (a) a.textContent = t; }
  function focusTo(sel) { var e = sel && document.querySelector(sel); if (e) { try { e.focus(); } catch (x) {} } }
  function nav() {
    var n = $('nav'); n.textContent = ''; var i0 = 0;
    TIERS.forEach(function (t) {
      var its = L.items.map(function (it, i) { return [it, i]; }).filter(function (p) { return p[0].tier === t[0]; });
      if (!its.length) return;
      var g = h('div', { class: 'ng', role: 'group', 'aria-label': t[1] }, [h('span', { class: 'nt', text: t[1] })]);
      its.forEach(function (p) {
        var st = status(p[0], p[1]);
        g.appendChild(h('button', { type: 'button', class: 'nb ' + st, 'data-i': String(p[1]), 'aria-current': String(p[1] === cur), 'aria-label': 'Question ' + (p[0].no || (p[1] + 1)) + (LBL.dup[p[1]] ? ' (button ' + LBL.lab[p[1]] + ')' : '') + ', ' + MARK[st], title: MARK[st], on: { click: function () { cur = p[1]; ask = false; render('.q'); say('Question ' + (p[0].no || (p[1] + 1)) + ' of ' + L.items.length); } } }, [h('b', { text: LBL.lab[p[1]] }), h('i', { text: SYM[st], 'aria-hidden': 'true' })]));
      });
      n.appendChild(g);
    });
    var typed = L.items.filter(function (it) { return it.type !== 'selfcheck'; }), na = typed.filter(function (it) { return answered(it, S.a[it.id]); }).length;
    $('count').textContent = S.sub ? 'Submitted. You can look at every question and its solution.' : na + ' of ' + typed.length + ' marked questions have an answer. You can open any question, in any order.';
  }
  function fig(it) { if (!it.svg) return null; var d = new DOMParser().parseFromString(it.svg, 'image/svg+xml').documentElement; if (!d || d.nodeName !== 'svg') return null; Array.prototype.forEach.call(d.querySelectorAll('script,foreignObject'), function (x) { x.remove(); }); var w = h('div', { class: 'fig' }); w.appendChild(document.importNode(d, true)); return w; }
  function negAns(it) { var a = it.type === 'fields' ? it.fields.map(function (f) { return f.answer; }) : [].concat(it.answer); return a.some(function (x) { return typeof x === 'number' && x < 0; }); }
  function imode(it) { return it.type === 'set' || negAns(it) ? 'text' : 'numeric'; }   // the iPhone number pad has no comma, space or minus
  function labelTail(s) { // [text before the label, the label] for the words just before a box
    var core = s.replace(/\s+$/, ''), re = /\n|\s{2,}|;/g, start = 0, mm, words, lab = [], len = 0, j;
    while ((mm = re.exec(core))) start = mm.index + mm[0].length;
    words = core.slice(start).split(' ').filter(function (w) { return w !== ''; });
    for (j = words.length - 1; j >= 0; j--) {
      if (lab.length && (len + words[j].length + 1 > 34 || /[,.!?]$/.test(words[j]))) break;
      lab.unshift(words[j]); len += words[j].length + 1;
    }
    if (!lab.length) return [s, ''];
    var txt = lab.join(' '), at = core.lastIndexOf(txt);
    return [core.slice(0, at) + ' ', txt];
  }
  function qn(it) { return it.no ? 'question ' + it.no : 'question ' + (cur + 1); }
  function control(it, locked) {
    var v = S.a[it.id], box = h('div', { id: 'ans', class: 'row' });
    function set(val) { S.a[it.id] = val; save(); nav(); bar(); }
    if (it.type === 'fields') {
      var cur_ = Array.isArray(v) ? v : it.fields.map(function () { return ''; });
      // A box keeps its label in ONE non-breaking group (flex, no wrap): the label is the words just before the box, back to a clause break (a semicolon, two or more spaces, a new line, or a word ending in a comma or full stop),
      // at most 34 characters; the first word or unit after the box (and punctuation such as '.') stays with it. So 'FCD (cm²):' can never be left at the end of the line beside another question's box.
      var fparts = it.frame.split(/(\{\w+\})/), prevG = null, pend = '', ids = it.fields.map(function (f) { return f.id; });
      fparts.forEach(function (part, pi) {
        var m = /^\{(\w+)\}$/.exec(part), idx = m ? ids.indexOf(m[1]) : -1;
        if (idx > -1) {
          var inp = h('input', { type: 'text', inputmode: imode(it), autocomplete: 'off', 'data-f': m[1], 'aria-label': 'Box ' + (idx + 1) + ' of ' + qn(it), style: 'width:5rem;text-align:center' }); inp.value = cur_[idx] || ''; if (locked) inp.disabled = true; inp.addEventListener('input', function () { var a = it.fields.map(function (f, i) { return i === idx ? inp.value : (cur_[i] || ''); }); cur_ = a; set(a); });
          prevG = h('span', { class: 'fg' }, [pend ? h('span', { class: 'fr fl', text: pend }) : null, inp]); pend = ''; box.appendChild(prevG);
        } else if (part) {
          if (prevG) { var lead = /^[^ \n\t]+/.exec(part); if (lead) { prevG.appendChild(h('span', { class: 'fr ft', text: lead[0] })); part = part.slice(lead[0].length); } }
          if (pi + 1 < fparts.length && /^\{\w+\}$/.test(fparts[pi + 1])) { var lt = labelTail(part); pend = lt[1]; part = lt[0]; }
          prevG = null;
          if (part.trim()) box.appendChild(h('span', { class: 'fr', text: part }));
        }
      });
    } else if (it.type === 'text') {
      var inp4 = h('input', { type: 'text', autocomplete: 'off', autocapitalize: 'none', spellcheck: 'false', 'aria-label': 'Your answer for ' + qn(it) }); inp4.value = v || ''; if (locked) inp4.disabled = true; inp4.addEventListener('input', function () { set(inp4.value); }); box.appendChild(inp4);
    } else if (it.type === 'set' || it.type === 'number') {
      var inp2 = h('input', { type: 'text', inputmode: imode(it), autocomplete: 'off', 'aria-label': (it.type === 'set' ? 'Your answers for ' + qn(it) + ', separated by commas' : 'Your answer for ' + qn(it)) }); inp2.value = v || ''; if (locked) inp2.disabled = true; inp2.addEventListener('input', function () { set(inp2.value); }); box.appendChild(inp2);
    } else if (it.type === 'choice') {
      box = h('fieldset', { id: 'ans', class: 'row' }, [h('legend', { class: 'sr', text: it.q })]);
      it.options.forEach(function (o) { var r = h('input', { type: 'radio', name: 'c', value: o }); if (v === o) r.checked = true; if (locked) r.disabled = true; r.addEventListener('change', function () { set(o); }); box.appendChild(h('label', { class: 'opt' }, [r, o])); });
    } else if (it.type === 'selfcheck') {
      if (it.paper) box = h('div', { id: 'ans' });
      else { var ta = h('textarea', { 'aria-label': 'Your answer for ' + qn(it), placeholder: 'Write here...' }); ta.value = v || ''; if (locked) ta.disabled = true; ta.addEventListener('input', function () { set(ta.value); }); box = h('div', { id: 'ans' }, [ta]); }
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
      if (v.type === 'fields') v.frame.split(/(\{\w+\})/).forEach(function (part) { var m = /^\{(\w+)\}$/.exec(part); if (m && v.fields.some(function (f) { return f.id === m[1]; })) { var i2 = h('input', { type: 'text', inputmode: negAns(v) ? 'text' : 'numeric', autocomplete: 'off', 'data-sf': m[1], 'aria-label': 'Box in the similar question', style: 'width:5rem;text-align:center' }); inputs.push(i2); row.appendChild(i2); } else if (part) row.appendChild(h('span', { class: 'fr', text: part })); });
      else { var i3 = h('input', { type: 'text', inputmode: negAns(v) ? 'text' : 'numeric', autocomplete: 'off', 'data-sf': 'n', 'aria-label': 'Your answer to the similar question' }); inputs.push(i3); row.appendChild(i3); }
      p.appendChild(row);
      var out = h('div', { id: 'simfb', 'aria-live': 'polite' });
      p.appendChild(h('div', { class: 'row' }, [h('button', { type: 'button', class: 'act', text: 'Check', on: { click: function () {
        var ok = v.type === 'fields' ? v.fields.every(function (f, i) { return toNum(inputs[i].value) === f.answer; }) : toNum(inputs[0].value) === v.answer;
        st.tries = (st.tries | 0) + 1;
        out.textContent = ''; var ans = 'The answer is ' + (v.type === 'fields' ? v.fields.map(function (f) { return f.answer; }).join(', ') : v.answer) + '.', steps = h('ol', {}, v.steps.map(function (x) { return h('li', { text: x }); }));
        // first wrong try: the hint only, so the child can try again; the answer and steps appear from the second wrong try
        out.appendChild(h('div', { class: 'fb ' + (ok ? 'ok' : 'try'), tabindex: '-1', id: 'simres' }, ok ? [h('h2', { text: 'Yes, that is right.' }), steps] : st.tries < 2 ? [h('h2', { text: 'Not yet.' }), h('p', { text: 'Hint: ' + v.hint }), h('p', { text: 'Try once more.' })] : [h('h2', { text: 'Not yet.' }), h('p', { text: 'Hint: ' + v.hint }), h('p', { text: ans }), steps]));
        focusTo('#simres');
      } } })]));
      p.appendChild(out); w.appendChild(p);
    }
    return w;
  }
  // A figure whose content reaches past its viewBox (text made larger for phones, a long caption, a bead at the edge) gets a wider viewBox, so nothing is cut off.
  function fitFigs() {
    function fit() {
      Array.prototype.forEach.call(document.querySelectorAll('#card .fig svg, #card .fb svg'), function (sv) {
        try {
          var vb = (sv.getAttribute('viewBox') || '').split(/[\s,]+/).map(Number); if (vb.length !== 4 || vb.some(isNaN)) return;
          var bb = sv.getBBox(), pd = 4, x0 = Math.min(vb[0], bb.x - pd), y0 = Math.min(vb[1], bb.y - pd), x1 = Math.max(vb[0] + vb[2], bb.x + bb.width + pd), y1 = Math.max(vb[1] + vb[3], bb.y + bb.height + pd);
          if (x0 < vb[0] - 0.5 || y0 < vb[1] - 0.5 || x1 > vb[0] + vb[2] + 0.5 || y1 > vb[1] + vb[3] + 0.5) sv.setAttribute('viewBox', [x0, y0, x1 - x0, y1 - y0].map(function (v) { return Math.round(v * 10) / 10; }).join(' '));
        } catch (e) {}
      });
    }
    fit(); try { if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit); } catch (e) {}
  }
  var hintOpen = {};
  function render(foc) {
    nav();
    var it = L.items[cur], card = $('card'); card.textContent = '';
    var locked = S.sub;
    card.appendChild(h('p', { class: 'q', tabindex: '-1', text: it.q }));
    var f = fig(it); if (f) card.appendChild(f);
    if (it.type === 'selfcheck' && it.paper) card.appendChild(h('p', { class: 'fb plain', id: 'paper', text: 'Do this on paper, then check your drawing against the answer shown on screen.' }));
    if (it.type === 'set') card.appendChild(h('p', { class: 'sub', style: 'margin:0 0 .5rem', text: 'Type every answer, with a comma between. Use commas between numbers.' }));
    card.appendChild(control(it, locked));
    if (!S.sub) {
      var hb = h('div', { class: 'row', style: 'margin-top:.8rem' }, [h('button', { type: 'button', id: 'hintbtn', class: 'act quiet', text: hintOpen[it.id] ? 'Hide the hint' : 'Give me a hint', 'aria-expanded': String(!!hintOpen[it.id]), on: { click: function () { hintOpen[it.id] = !hintOpen[it.id]; render(hintOpen[it.id] ? '#hintbox' : '#hintbtn'); say(hintOpen[it.id] ? 'Hint shown' : 'Hint hidden'); } } })]);
      card.appendChild(hb);
      if (hintOpen[it.id]) card.appendChild(h('div', { class: 'fb plain', id: 'hintbox', tabindex: '-1', role: 'note' }, [h('p', { text: 'Hint: ' + it.hint })]));
      if (it.type === 'selfcheck' && !it.paper) card.appendChild(h('p', { class: 'sub', text: 'You can write an answer here, or just do it on paper. The example comes with the solutions after you submit.' }));
    } else {
      card.appendChild(solution(it));
    }
    var pn = h('div', { class: 'row', style: 'margin-top:1rem' }, [
      h('button', { type: 'button', class: 'act quiet', text: 'Previous', on: { click: function () { cur = (cur + L.items.length - 1) % L.items.length; render('.q'); window.scrollTo(0, 0); say('Question ' + (L.items[cur].no || (cur + 1)) + ' of ' + L.items.length); } } }),
      h('button', { type: 'button', class: 'act quiet', text: S.sub ? 'Next' : 'Skip to next', on: { click: function () { cur = (cur + 1) % L.items.length; render('.q'); window.scrollTo(0, 0); say('Question ' + (L.items[cur].no || (cur + 1)) + ' of ' + L.items.length); } } })]);
    card.appendChild(pn);
    bar(); fitFigs();
    if (foc) focusTo(foc === '.q' ? '#card .q' : foc);
  }
  function bar() {
    var b = $('bar'); b.textContent = '';
    var un = L.items.filter(function (it) { return it.type !== 'selfcheck' && !answered(it, S.a[it.id]); }).length;   // a self-check or paper task is never 'unanswered'
    var sl = syncLine(); if (sl) b.appendChild(sl);
    if (S.sub) { b.appendChild(summary()); b.appendChild(h('div', { class: 'row' }, [h('button', { type: 'button', id: 'again', class: 'act', text: 'Change my answers and submit again', on: { click: function () { S.sub = false; save(); render('.q'); say('You can change your answers now.'); } } }), h('button', { type: 'button', class: 'act quiet', text: 'Start again with empty answers', on: { click: function () { S = { a: {}, sub: false, sid: '', rev: 0, sent: 0, self: {} }; sim = {}; hintOpen = {}; save(); cur = 0; render('.q'); } } })])); return; }
    if (ask) {
      b.appendChild(h('div', { class: 'fb try', role: 'alertdialog', 'aria-label': 'Submit anyway?', id: 'askbox', tabindex: '-1' }, [h('p', { text: un + (un === 1 ? ' question has' : ' questions have') + ' no answer yet. Submit anyway? You will see the solutions for every question.' }), h('div', { class: 'row' }, [h('button', { type: 'button', id: 'yes', class: 'act', text: 'Yes, submit', on: { click: function () { submit(); } } }), h('button', { type: 'button', id: 'keep', class: 'act quiet', text: 'Keep working', on: { click: function () { ask = false; bar(); focusTo('#submit'); } } })])]));
      return;
    }
    b.appendChild(h('button', { type: 'button', id: 'submit', class: 'act', text: 'Submit my answers', on: { click: function () { if (un) { ask = true; bar(); focusTo('#askbox'); } else submit(); } } }));
  }
  function submit() { S.sub = true; ask = false; if (syncOn()) { if (!S.sid) S.sid = newId(); S.rev = (S.rev | 0) + 1; SY.tries = 0; SY.msg = ''; } save(); hintOpen = {}; render(); var s = $('bar'); if (s && s.scrollIntoView) s.scrollIntoView({ block: 'nearest' }); focusTo('#summary'); send(); }
  function summary() {
    var c = { right: 0, wrong: 0, blank: 0, self: 0 }; L.items.forEach(function (it) { c[judge(it, S.a[it.id])]++; });
    var marked = L.items.length - c.self;
    return h('div', { class: 'fb plain', id: 'summary', tabindex: '-1' }, [h('h2', { text: 'Your answers are marked' }), h('p', { text: c.right + ' of ' + marked + ' marked questions are right. ' + c.wrong + ' to look at again, ' + c.blank + ' with no answer' + (c.self ? ', and ' + c.self + ' to check yourself.' : '.') + ' Open any question to see its worked solution.' }), h('p', { class: 'sub', text: '✓ right   ✗ look again   – no answer   ✎ check yourself' })]);
  }
  // ---- optional send to tutor (flag OFF by default)
  function tok() { try { if (CFG && CFG.token) return CFG.token; var c = JSON.parse(sessionStorage.getItem('mi-child') || 'null'); return (c && c.token) || null; } catch (e) { return null; } }
  function syncOn() { return !!(CFG && CFG.endpoint && tok()); }
  function newId() {
    try { if (window.crypto && crypto.randomUUID) return crypto.randomUUID(); var b = crypto.getRandomValues(new Uint8Array(16)); b[6] = b[6] & 15 | 64; b[8] = b[8] & 63 | 128;
      var x = Array.prototype.map.call(b, function (v) { return ('0' + v.toString(16)).slice(-2); }).join(''); return x.slice(0, 8) + '-' + x.slice(8, 12) + '-' + x.slice(12, 16) + '-' + x.slice(16, 20) + '-' + x.slice(20); } catch (e) { return ''; }
  }
  function payload() {
    var ans = {}, ex = {}, nex = 0;
    L.items.forEach(function (it) {
      var v = S.a[it.id];
      // a self-check answer is never marked: answers[id] only says that something was written. EXPLAIN-TO-TUTOR: the typed explanation itself (trimmed, at most EXPLAIN_MAX characters) goes in the separate
      // 'explain' map, only while sending is switched on (this function runs only then), so the tutor can read it. The server never returns it and the page never shows it as a mark.
      if (it.type === 'selfcheck') {
        ans[it.id] = answered(it, v) ? '(written)' : null;
        if (!it.paper && answered(it, v)) { var tx = String(v).replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, '').trim().slice(0, EXPLAIN_MAX).trim(); if (tx && nex < 400) { ex[it.id] = tx; nex++; } }
      }
      else ans[it.id] = answered(it, v) ? (Array.isArray(v) ? v.map(String) : String(v)) : null;
    });
    var self = {}; Object.keys(S.self || {}).forEach(function (k) { self[k] = S.self[k]; });
    var out = { v: 1, unit: CFG.unit || ('ext-' + key), unit_version: CFG.version || VER, sid: S.sid, rev: S.rev, answers: ans, self: self };
    if (nex) out.explain = ex;
    return out;
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
  function chrome() {
    if (!$('announce')) document.body.appendChild(h('div', { id: 'announce', class: 'sr', role: 'status', 'aria-live': 'polite' }));
    if (!document.querySelector('.skip')) document.body.insertBefore(h('a', { class: 'skip', href: '#card', text: 'Skip to the question', on: { click: function (e) { e.preventDefault(); focusTo('#card .q'); } } }), document.body.firstChild);
  }
  // the privacy line in the page footer must be true for the mode the page is in: sending off = on this device only; sending on = sent to the tutor
  function footer() {
    var f = document.querySelector('.foot'), t = syncOn() ? 'Your answers, and what you write in the explanation boxes, are sent to your tutor so they can help you.' : 'Your answers stay on this device.';
    if (!f) return;
    var sp = $('footpriv');
    if (sp) sp.textContent = t;
    else f.textContent = f.textContent.replace(/Your answers stay in this browser only: nothing is sent anywhere\./, t);
  }
  chrome();
  load();
  fetch('data/' + key + '.json').then(function (r) { if (!r.ok) throw new Error('missing'); return r.text(); }).then(function (txt) {
    var d = JSON.parse(txt), vp = Promise.resolve('');
    // the unit version = first 8 hex of the SHA-256 of this exact data file, so a server key can never be used for a changed question
    if (syncOn() && !CFG.version && window.crypto && crypto.subtle) vp = crypto.subtle.digest('SHA-256', new TextEncoder().encode(txt)).then(function (b) { return Array.prototype.map.call(new Uint8Array(b), function (v) { return ('0' + v.toString(16)).slice(-2); }).join('').slice(0, 8); }, function () { return ''; });
    return vp.then(function (v) { VER = v; return d; });
  }).then(function (d) {
    L = d; LBL = labelsAll(); document.title = 'Practice: ' + L.title + ' | Math Inquirers';
    $('title').textContent = L.title + ' practice'; $('sub').textContent = 'Level ' + L.level + ' · ' + (L.unit_label || 'Lesson ' + L.lesson) + ' · ' + L.topic;
    footer(); render();
    if (S.sub && S.sent < S.rev) send();   // a tab closed before the send finished: try again when the page is opened again
  }).catch(function () { $('title').textContent = 'Practice'; $('card').textContent = 'This practice link is not complete. Please ask your tutor for the right link.'; });
})();
