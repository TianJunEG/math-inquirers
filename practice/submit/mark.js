// Shared auto-marking for the online workbooks. Pure functions, no DOM, no network.
// Used (1) by the Cloudflare Worker at submission to RE-MARK every answer from the stored answer key (a 'correct' flag sent by a browser is never read),
// and (2) by tests that compare it with the pilot runner (practice/ext/public/sheet.js) in a real browser.
// For the pilot item types (number, fields, set, choice) the rules are the same as sheet.js on purpose: same input, same mark.
// New types (fraction, decimal, text) are used by Phase 2 and are not in the pilot data yet.
//
// A KEY record:  { id, marking_mode: 'auto'|'self'|'none', type, key, ordered?, equivalent?, slips? }
//   number    key: 12
//   fields    key: [3, 4]               (several boxes; all must be right)
//   set       key: [85, 508], ordered: true|false
//   choice    key: '<'                  (exact option text)
//   fraction  key: '3/8', equivalent: false (default: must be in lowest terms) | true (any equal fraction is right)
//   decimal   key: '0.5'                (0.50 and .5 are the same number)
//   text      key: ['NW', 'north west'] (case, spacing, hyphen and a final full stop do not matter)
//   selfcheck marking_mode 'self'  (child compares with the shown solution; never auto-marked; paper-only items are this)
//   open      marking_mode 'none'  (many answers are right; never marked)
// Result: { mark: 'right'|'wrong'|'skipped'|'self'|'open', detail?: {...}, slip?: index }
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(); else root.MIMark = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  // BEGIN SHARED (this block is identical in practice/ext/public/sheet.js and practice/submit/mark.js; mark.test.mjs checks it)
  // Reading numbers. A single number: a thousands separator (comma or one space) is allowed only in valid groups (1,000 / 12 500), a leading $ or a unicode minus
  // is ignored/normalised, a final full stop or .0 ('29.', '20.0') is ignored, and a unit word after the number ('301 sticks', '20 min') is ignored unless the item says unit:false.
  // opt.pre = text printed just before the box ('6:' for a box in '6:{f1}'), which the child may repeat ('6:20').
  function str(s) { return String(s == null ? '' : s); }
  function minus(s) { return str(s).replace(/[−–—‐‑]/g, '-'); }
  function toNum(s, opt) {
    s = minus(s).trim().replace(/^\$\s*/, '');
    if (opt && opt.pre && s.indexOf(opt.pre) === 0) s = s.slice(opt.pre.length).trim();
    s = s.replace(/\.0*$/, '');
    if (!opt || opt.unit !== false) { var u = /^(-?\d[\d, ]*?)\s*[a-z][a-z .²³]*$/i.exec(s); if (u) s = u[1].trim(); }
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
  // END SHARED
  function answered(type, v) {
    if (v == null) return false;
    if (Array.isArray(v)) return v.some(function (x) { return str(x).trim() !== ''; });
    return str(v).trim() !== '';
  }
  function common(a, b) { // size of the multiset intersection of two number lists
    var rest = b.slice(), n = 0;
    a.forEach(function (x) { var i = rest.indexOf(x); if (i > -1) { rest.splice(i, 1); n++; } });
    return n;
  }
  // ---- new types
  function gcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { var t = a % b; a = b; b = t; } return a; }
  function parseFraction(s) { // '3/8', '1 1/2', '2' -> {n, d} as BigInt, or null
    s = str(s).normalize('NFKC').replace(/−/g, '-').trim().replace(/\s*\/\s*/g, '/');
    var m = /^(-?)(?:(\d+)\s+)?(\d+)\/(\d+)$/.exec(s), w, n, d, neg;
    if (m) { neg = m[1] === '-'; w = BigInt(m[2] || 0); n = BigInt(m[3]); d = BigInt(m[4]); if (d === 0n) return null; n = w * d + n; if (neg) n = -n; return { n: n, d: d }; }
    m = /^-?\d+$/.exec(s); if (m) return { n: BigInt(s), d: 1n };
    return null;
  }
  function fracEqual(a, b) { return a.n * b.d === b.n * a.d; }
  function lowest(f) { return gcd(f.n, f.d) === 1n; }
  function parseDecimal(s) { // -> {sign, int, frac} with no spurious zeros, or null
    s = str(s).normalize('NFKC').replace(/−/g, '-').replace(/\s/g, '').replace(/(\d),(?=\d{3}(\D|$))/g, '$1');
    var m = /^([+-]?)(\d*)(?:\.(\d*))?$/.exec(s);
    if (!m || (m[2] === '' && (m[3] === undefined || m[3] === ''))) return null;
    var i = m[2].replace(/^0+(?=\d)/, '') || '0', f = (m[3] || '').replace(/0+$/, '');
    var neg = m[1] === '-' && (i !== '0' || f !== '');
    return { neg: neg, i: i, f: f };
  }
  function decEqual(a, b) { return a.neg === b.neg && a.i === b.i && a.f === b.f; }

  function nopt(rec) { return { unit: rec.unit }; }
  function fopt(rec, i) { return { unit: rec.unit, pre: rec.pre && rec.pre[i] || '' }; }
  function matchSlip(rec, v) { // which listed wrong answer (if any) the child gave: its index, so a report can say why
    var slips = rec.slips || [], got, i;
    for (i = 0; i < slips.length; i++) {
      var a = slips[i].a;
      if (rec.type === 'fields' ? (Array.isArray(v) && a.length === v.length && a.every(function (x, k) { return toNum(v[k], fopt(rec, k)) === x; })) :
          rec.type === 'set' ? setMatch(v, a, rec.ordered, rec.grouped).ok :
          rec.type === 'choice' ? str(v) === str(a[0]) : toNum(v, nopt(rec)) === a[0]) return i;
    }
    return undefined;
  }

  function mark(rec, v) {
    if (rec.marking_mode === 'none' || rec.type === 'open') return { mark: 'open' };
    if (rec.marking_mode === 'self' || rec.type === 'selfcheck') return { mark: 'self' };
    if (!answered(rec.type, v)) return { mark: 'skipped' };
    var ok, detail, key = rec.key, r;
    switch (rec.type) {
      case 'number': ok = toNum(v, nopt(rec)) === key; break;
      case 'choice': ok = str(v) === str(key); break;
      case 'fields': {
        var arr = Array.isArray(v) ? v : [], boxes = key.map(function (k, i) { return toNum(arr[i], fopt(rec, i)) === k; });
        ok = boxes.every(Boolean) && arr.length === key.length; detail = { boxes: boxes }; break; }
      case 'set': {
        var sm = setMatch(v, key, rec.ordered, rec.grouped), a = sm.a; ok = sm.ok;
        detail = { found: rec.ordered ? a.filter(function (x, i) { return x === key[i]; }).length : common(a, key), of: key.length, given: a.length }; break; }
      case 'fraction': {
        var f = parseFraction(v), k = parseFraction(key);
        if (!f || !k) ok = false;
        else if (!fracEqual(f, k)) ok = false;
        else if (!rec.equivalent && !lowest(f)) { ok = false; detail = { reason: 'not_simplest' }; }
        else ok = true;
        break; }
      case 'decimal': { var d = parseDecimal(v), kd = parseDecimal(key); ok = !!(d && kd && decEqual(d, kd)); break; }
      case 'text': { var keys = Array.isArray(key) ? key : [key]; ok = textOK(keys, v); break; }
      default: throw new Error('unknown item type ' + rec.type);
    }
    r = { mark: ok ? 'right' : 'wrong' };
    if (detail) r.detail = detail;
    if (!ok) { var sl = matchSlip(rec, v); if (sl !== undefined) r.slip = sl; }
    return r;
  }
  return { mark: mark, toNum: toNum, nums: nums, sameSet: sameSet, answered: answered };
});
