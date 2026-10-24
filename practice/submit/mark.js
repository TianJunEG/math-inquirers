// Shared auto-marking for the online workbooks. Pure functions, no DOM, no network.
// Used (1) by the Cloudflare Worker at submission to RE-MARK every answer from the stored answer key (a 'correct' flag sent by a browser is never read),
// and (2) by tests that compare it with the pilot runner (practice/ext/public/sheet.js) in a real browser.
// For the pilot item types (number, fields, set, choice) the rules are the same as sheet.js on purpose: same input, same mark.
// New types (fraction, decimal, text) are used by Phase 2 and are not in the pilot data yet.
//
// A KEY record:  { id, marking_mode: 'auto'|'self'|'none', type, key, ordered?, equivalent?, slips? }
//   number    key: 12              (a unit after the number is ignored: '84 cm2', '84cm^2', '84 cm²', '-25 °C', '11°C'; one pair of brackets round it: '(-25)'; unit:false refuses units;
//                                    words:true also accepts number words: 'five', 'twenty-five', 'minus five'; no default)
//   fields    key: [3, 4]               (several boxes; all must be right; time: [true,false] flags an hours box followed by a minutes box: '5:25' in the first box with the second empty is 5 and 25)
//   set       key: [85, 508], ordered: true|false
//   choice    key: '<'                  (exact option text)
//   fraction  key: '3/8', equivalent: false (default: must be in lowest terms) | true (any equal fraction is right)
//   decimal   key: '0.5'                (0.50 and .5 are the same number)
//   text      key: ['NW', 'north west'] (case, spacing, hyphen and a final full stop do not matter)
//             equiv_frac:true  every fraction of a typed list may be written in any equal form, same order ('7/12, 8/12, 10/12' for '7/12, 2/3, 5/6')
//             poly:'n'         an algebra rule is compared as a polynomial in n; '=' chains allowed ('(n+3)x4 = 4n+12', 'OUT = 4(n+3)'); (2n+6)/2 equals n+3; keys list the accepted writings
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
  // Units after the number: a word ('301 sticks', '20 minutes', 'sq cm'), a word with an attached power ('84 cm2', '84cm^2', '84 cm²'), a rate ('km/h') a degree sign ('-25 °C', '11°C', '44°') or a cent sign / cent word ('35¢', '35 cents') or a litre sign ('27 ℓ', '27 l', '27 litres'), then at most two more plain words in all (a unit and a short tail: '27 ℓ of water', '27 liters of water', '35 cents change', '35 cents left'; longer tails are refused; for cents a bare lowercase 'c' is refused as ambiguous; '$0.35' is never turned into cents).
  // A single pair of brackets round the whole answer is ignored ('(-25)'). Two numbers ('4 or 5', '1 2') are never a unit.
  var UW = '[a-z][a-z.]*(?:\\^?[23]|\\s?[²³])?', UNITRE = new RegExp('^(-?\\d[\\d, ]*?(?:\\.0+)?)\\s*(?:[°º]\\s*[a-z]?|%|[¢ℓ](?:\\s+[a-z]+){0,2}|' + UW + '(?:\\s+' + UW + '){0,2}(?:\\/[a-z]+)?)$', 'i');
  // A clock hour (item flag clock:true, set by the builder when the stem or frame says o'clock and the answer is a bare hour): '3', '3 o'clock', '3:00', '03:00', '3.00', '3 pm' / '3 am' are all the hour 3;
  // the minutes must be 00, so '3:30' is never 3. Without the flag only the plain number forms are read.
  function clockHour(s) {
    var m = /^(\d{1,2})\s*(?:o['\u2019\u2018`]?\s*clock|[:.]\s*00)(?:\s*(?:[ap]\.?m\.?))?\s*\.?$/i.exec(s) || /^(\d{1,2})\s*[ap]\.?m\.?\s*\.?$/i.exec(s);
    return m ? m[1].replace(/^0+(?=\d)/, '') : null;
  }
  function toNum(s, opt) {
    s = minus(s).trim().replace(/^\+\s*(?=\d)/, '');   // a leading plus sign ('+1', '+ 1') is not a unit and is always accepted; '+-1' and '1+' are not numbers
    var pb = /^\(\s*([^()]*?)\s*\)\s*(.*)$/.exec(s); if (pb) s = (pb[2] ? pb[1] + ' ' + pb[2] : pb[1]).replace(/^\+\s*(?=\d)/, '');   // '(-25)' and '(-25) °C'
    if (opt && opt.clock) { var ck = clockHour(s); if (ck !== null) s = ck; }
    if (opt && opt.dollars_ok) { var dm = /^\$\s*0?\.(\d\d)\s*\.?$/.exec(s); if (dm) return +dm[1]; }   // '$0.48' for 48 cents, only when the item says dollars_ok
    if (opt && opt.words) { var wn = wordsToNum(s); if (wn !== null) return wn; }
    if (!opt || opt.unit !== false) s = s.replace(/^(?:∠|angle\s+)\s*[a-z]{1,3}\s*(?:=|is)\s*/i, '');   // '∠AOC = 90°', 'angle AOC is 90' (an angle name before the number; never for unit:false)
    s = s.replace(/^\$\s*/, '');
    if (opt && opt.pre && s.indexOf(opt.pre) === 0) s = s.slice(opt.pre.length).trim();
    s = s.replace(/\.0*$/, '');
    if (!opt || opt.unit !== false) { var u = UNITRE.exec(s); if (u && !/\d\s*c(?![a-z])/.test(s)) s = u[1].trim().replace(/\.0+$/, ''); }
    if (/^-?\d{1,3}(?:[, ]\d{3})+$/.test(s)) s = s.replace(/[, ]/g, '');
    return /^-?\d+$/.test(s) ? +s : null;
  }
  // Time of day in two boxes (hours, minutes; the builder flags the hours box, item flag time:true): a whole time typed in the FIRST box with the second left empty ('5:25', '5.25', '5 25')
  // is read as hours 5, minutes 25. Minutes need two digits. A time typed in both boxes is read as typed. flags = list with true at the hours box.
  function timeFix(arr, flags) {
    if (!Array.isArray(arr) || !Array.isArray(flags)) return arr;
    var out = arr.slice(), i, m;
    for (i = 0; i + 1 < out.length; i++) {
      if (flags[i] && str(out[i]).trim() !== '' && str(out[i + 1]).trim() === '') {
        m = /^(\d{1,2})\s*(?:[:.]|\s)\s*(\d{2})$/.exec(minus(str(out[i])).trim());
        if (m) { out[i] = m[1]; out[i + 1] = m[2]; }
      }
    }
    return out;
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
  // A short lead-in before a text answer ('It is Wednesday', 'It will be Wednesday.', 'The answer is 12'): ignored for text items unless the item says accept_prefix:false;
  // accept_prefix may also be a list of extra lead-ins. It is removed only from what the child typed, never from the key, and 'It is not Wednesday' stays wrong.
  var LEAD = ['it is', 'it will be', 'it\'s', 'the answer is', 'my answer is', 'answer is', 'answer:'];
  function lead(v, o) {
    if (o && o.accept_prefix === false) return str(v);
    var t = minus(str(v).normalize('NFKC')).trim(), ls = LEAD.concat(o && Array.isArray(o.accept_prefix) ? o.accept_prefix.map(function (x) { return str(x).toLowerCase(); }) : []), low = t.toLowerCase(), i;
    for (i = 0; i < ls.length; i++) if (low.indexOf(ls[i]) === 0 && /^(?::\s*|\s+)\S/.test(t.slice(ls[i].length))) return t.slice(ls[i].length).replace(/^[\s:]+/, '');
    return t;
  }
  // Same meaning, other words: 'a is equal to b' / 'a equals b' = 'a = b'; a short list of single letters, numbers or fractions may be joined by commas, 'and' or '&' ('A and B and D', 'A, B and D').
  function canon(s) {
    var n = normText(s).replace(/\s+(?:is equal to|equals)\s+/g, ' = ').replace(/^(?:the\s+)?shapes?\s+(?=[a-z](?![a-z]))/, '').replace(/[,;\s]+$/, ''), parts = n.split(/\s*,\s*and\s+|\s*[,;&]\s*|\s+and\s+/);
    if (parts.length > 1 && parts.every(function (x) { return /^(?:[a-z]|-?\d+(?:\/\d+)?)$/.test(x); })) n = parts.join(',');
    return n;
  }
  // "CAT" or 'CAT' or curly quotes round the whole answer (a final full stop outside them is fine); null if the answer is not wrapped in one matching pair.
  var QP = { '"': '"', '\u201c': '\u201d', '\u2018': '\u2019', "'": "'", '\u201e': '\u201c', '\u00ab': '\u00bb' };
  function unquote(v) {
    var t = str(v).normalize('NFKC').trim().replace(/[.!]+$/, '').trim(), q = QP[t.charAt(0)], inner;
    if (!q || t.length < 3 || t.charAt(t.length - 1) !== q) return null;
    inner = t.slice(1, -1);
    return inner.indexOf(q) > -1 || inner.indexOf(t.charAt(0)) > -1 ? null : inner.trim();
  }
  // Item flag accept_by: a pair of sides may be written 'a by b', 'a x b', 'a × b' with an optional 'a' / 'the' in front and 'square' / 'rectangle' / 'cm' after;
  // a single-number key (a square's side) stands for 'n by n'. Either order of a pair is read the same. Without the flag only the printed forms are accepted.
  function sidesPair(s) {
    var t = normText(s).replace(/^(?:an?|the)\s+/, '').replace(/\s*cm\b/g, '').replace(/(?:\s+(?:square|rectangle|sides?|units?))+$/, '').trim(), m = /^(\d+)\s*(?:x|by)\s*(\d+)$/.exec(t), n = /^(\d+)$/.exec(t);
    return m ? [+m[1], +m[2]].sort() : n ? [+n[1], +n[1]] : null;
  }
  function byOK(keys, v) {
    var p = sidesPair(v), t = normText(v);
    return !!p && !/^\d+$/.test(t) && keys.some(function (k) { var q = sidesPair(k); return !!q && q[0] === p[0] && q[1] === p[1]; });
  }
  function textOK(keys, v, o) {
    var cands = [v], m = /^(.*[\d)])\s*=\s*(-?[\d.\/ ]*\d)\s*[.!]?$/.exec(minus(str(v)).trim()); // a statement with its result: '(6+4)x5-2=48'
    if (m) { var l = evalExpr(m[1]), r = evalExpr(m[2].replace(/(\d) (\d+\/\d)/, '($1+$2)').replace(/ /g, '')); if (l != null && r != null && Math.abs(l - r) < 1e-9) cands.push(m[1]); }
    var m2 = /^(-?[\d.\/ ]*\d)\s*=\s*(.*[\d)])\s*[.!]?$/.exec(minus(str(v)).trim()); // the result first: '5/12=1/3+1/12'
    if (m2) { var r2 = evalExpr(m2[1].replace(/(\d) (\d+\/\d)/, '($1+$2)').replace(/ /g, '')), l2 = evalExpr(m2[2]); if (l2 != null && r2 != null && Math.abs(l2 - r2) < 1e-9) cands.push(m2[2]); }
    var ld = lead(v, o); if (ld !== str(v).trim()) cands.push(ld);
    // natural writings of a word or a single letter: "CAT" in quotes (a word key), 'the letter E' / 'letter E' (a one-letter key)
    var wordKey = keys.some(function (k) { return /^[a-z][a-z' -]*$/i.test(str(k).trim()); }), letKey = keys.some(function (k) { return /^[a-z]$/i.test(str(k).trim()); }), uq, lm;
    if (wordKey) { uq = unquote(v); if (uq !== null) cands.push(uq); }
    if (letKey) { lm = /^(?:the\s+)?letter\s+(.+)$/i.exec(minus(str(v).normalize('NFKC')).trim()); if (lm) { cands.push(lm[1]); uq = unquote(lm[1]); if (uq !== null) cands.push(uq); } }
    return keys.some(function (x) { return cands.some(function (c) { return normText(x) === normText(c) || squash(x) === squash(c) || squash(canon(x)) === squash(canon(c)); }); });
  }
  // Equal fractions in a typed list (item flag equiv_frac): '7/12, 8/12, 10/12' is right for the key '7/12, 2/3, 5/6'. Same order, same number of fractions, each equal in value
  // (cross-multiplied); any other symbol (such as < or >) must match the key. Without the flag only the printed forms are accepted.
  function fracTok(s) {
    var t = [], rest = minus(str(s).normalize('NFKC')).replace(/(\d+)\s+out\s+of\s+(\d+)/gi, '$1/$2').replace(/\s*\/\s*/g, '/').replace(/(-?)(\d+)\s+(\d+)\/(\d+)|(-?\d+)\/(\d+)|-?\d+/g, function (m, sg, w, a, b, n2, d2) {
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
  // A leading label ('total =', 'S =', 'rule:', 'Total angle =', 'Sum of angles =') is ignored only when it is 1 to 3 plain words (letters only, no digits) that are not the variable,
  // do not use the variable letter as a word, and none of which appears in the rest of the rule.
  function ruleSides(s, vr) {
    var a = minus(str(s)).trim().replace(/[.!]+$/, '').replace(/^rule\s*:\s*/i, '').split('=').map(function (x) { return x.trim(); }), lab = (a[0] || '').replace(/\s+/g, ' ').toLowerCase(), body;
    if (a.length > 1 && /^[a-z]+(?: [a-z]+){0,2}$/.test(lab) && lab !== 'out' && lab !== vr) {
      body = a.slice(1).join('=').toLowerCase();
      if (lab.split(' ').every(function (w) { return w !== vr && !new RegExp('(^|[^a-z])' + w + '($|[^a-z])').test(body); })) a.shift();
    }
    return a.filter(function (x) { return !/^out$/i.test(x); });
  }
  function polyOK(keys, v, vr) {
    vr = typeof vr === 'string' && vr.length === 1 && vr !== 'x' ? vr.toLowerCase() : 'n';
    var kp = [], sides = ruleSides(v, vr);
    keys.forEach(function (k) { ruleSides(k, vr).forEach(function (sd) { var q = polyParse(sd, vr); if (q) kp.push(q); }); });
    return sides.length > 0 && kp.length > 0 && sides.every(function (sd) { var q = polyParse(sd, vr); return !!q && kp.some(function (k) { return polyEq(q, k); }); });
  }
  // One text answer: the printed forms (textOK), plus, only when the item says so, equal fractions (equiv_frac) or an equal polynomial (poly).
  function textMatch(o, keys, v) { return textOK(keys, v, o) || !!(o && o.equiv_frac && (fracListOK(keys, v) || fracListOK(keys, lead(v, o)))) || !!(o && o.poly && polyOK(keys, v, o.poly)) || !!(o && o.accept_by && byOK(keys, v)); }
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
    s = str(s).normalize('NFKC').replace(/−/g, '-').trim().replace(/(\d+)\s+out\s+of\s+(\d+)/i, '$1/$2').replace(/\s*\/\s*/g, '/');   // '1 out of 4' is 1/4
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

  function nopt(rec) { return { unit: rec.unit, words: rec.words, clock: rec.clock === true, dollars_ok: rec.dollars_ok }; }
  function fopt(rec, i) { return { unit: rec.unit, words: rec.words, pre: rec.pre && rec.pre[i] || '', clock: rec.clock === true || (Array.isArray(rec.clock) && !!rec.clock[i]), dollars_ok: rec.dollars_ok }; }
  function matchSlip(rec, v) { // which listed wrong answer (if any) the child gave: its index, so a report can say why
    var slips = rec.slips || [], got, i;
    if (rec.type === 'fields') v = timeFix(v, rec.time);
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
        var arr = Array.isArray(v) ? timeFix(v, rec.time) : [], boxes = key.map(function (k, i) { return toNum(arr[i], fopt(rec, i)) === k; });
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
      case 'text': { var keys = Array.isArray(key) ? key : [key]; ok = textMatch(rec, keys, v); break; }
      default: throw new Error('unknown item type ' + rec.type);
    }
    r = { mark: ok ? 'right' : 'wrong' };
    if (detail) r.detail = detail;
    if (!ok) { var sl = matchSlip(rec, v); if (sl !== undefined) r.slip = sl; }
    return r;
  }
  return { mark: mark, toNum: toNum, nums: nums, sameSet: sameSet, answered: answered };
});
