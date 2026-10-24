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
  function str(s) { return String(s == null ? '' : s); }
  // ---- same rules as sheet.js
  function toNum(s) { s = str(s).replace(/\s/g, '').replace(/(\d),(?=\d{3}(\D|$))/g, '$1'); return /^-?\d+$/.test(s) ? +s : null; }
  function nums(s) { s = str(s).replace(/(\d),(?=\d{3}(\D|$))/g, '$1'); if (/[,;]/.test(s)) return s.split(/[,;]/).reduce(function (acc, tok) { tok = tok.trim(); if (/^\d{1,3}(\s\d{3})+$/.test(tok)) tok = tok.replace(/\s/g, ''); return acc.concat(tok.match(/-?\d+/g) || []); }, []).map(Number); return (s.match(/-?\d+/g) || []).map(Number); }
  function sameSet(a, b) { var x = a.slice().sort(function (p, r) { return p - r; }), y = b.slice().sort(function (p, r) { return p - r; }); return x.length === y.length && x.every(function (v, i) { return v === y[i]; }); }
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
  function normText(s) { return str(s).normalize('NFKC').toLowerCase().replace(/[.!]+$/, '').replace(/[\s\-]+/g, ' ').trim(); }
  function squash(s) { return normText(s).replace(/ /g, ''); }

  function matchSlip(rec, v) { // which listed wrong answer (if any) the child gave: its index, so a report can say why
    var slips = rec.slips || [], got, i;
    for (i = 0; i < slips.length; i++) {
      var a = slips[i].a;
      if (rec.type === 'fields' ? (Array.isArray(v) && a.length === v.length && a.every(function (x, k) { return toNum(v[k]) === x; })) :
          rec.type === 'set' ? (got = nums(v), rec.ordered ? (got.length === a.length && got.every(function (x, k) { return x === a[k]; })) : sameSet(got, a)) :
          rec.type === 'choice' ? str(v) === str(a[0]) : toNum(v) === a[0]) return i;
    }
    return undefined;
  }

  function mark(rec, v) {
    if (rec.marking_mode === 'none' || rec.type === 'open') return { mark: 'open' };
    if (rec.marking_mode === 'self' || rec.type === 'selfcheck') return { mark: 'self' };
    if (!answered(rec.type, v)) return { mark: 'skipped' };
    var ok, detail, key = rec.key, r;
    switch (rec.type) {
      case 'number': ok = toNum(v) === key; break;
      case 'choice': ok = str(v) === str(key); break;
      case 'fields': {
        var arr = Array.isArray(v) ? v : [], boxes = key.map(function (k, i) { return toNum(arr[i]) === k; });
        ok = boxes.every(Boolean) && arr.length === key.length; detail = { boxes: boxes }; break; }
      case 'set': {
        var a = nums(v);
        ok = rec.ordered ? (a.length === key.length && a.every(function (x, i) { return x === key[i]; })) : sameSet(a, key);
        detail = { found: rec.ordered ? a.filter(function (x, i) { return x === key[i]; }).length : common(a, key), of: key.length, given: a.length }; break; }
      case 'fraction': {
        var f = parseFraction(v), k = parseFraction(key);
        if (!f || !k) ok = false;
        else if (!fracEqual(f, k)) ok = false;
        else if (!rec.equivalent && !lowest(f)) { ok = false; detail = { reason: 'not_simplest' }; }
        else ok = true;
        break; }
      case 'decimal': { var d = parseDecimal(v), kd = parseDecimal(key); ok = !!(d && kd && decEqual(d, kd)); break; }
      case 'text': { var keys = Array.isArray(key) ? key : [key]; ok = keys.some(function (x) { return normText(x) === normText(v) || squash(x) === squash(v); }); break; }
      default: throw new Error('unknown item type ' + rec.type);
    }
    r = { mark: ok ? 'right' : 'wrong' };
    if (detail) r.detail = detail;
    if (!ok) { var sl = matchSlip(rec, v); if (sl !== undefined) r.slip = sl; }
    return r;
  }
  return { mark: mark, toNum: toNum, nums: nums, sameSet: sameSet, answered: answered };
});
