/* Node unit tests for MiTeaser.check (the answer matcher): natural ways a child types an answer, and the wrong ones.
   python3 test_site.py runs this file first.  Usage: node website/teasers/test_check.js */
'use strict';
var fs = require('fs'), path = require('path');
var src = fs.readFileSync(path.join(__dirname, 'teasers.js'), 'utf8');
var g = { addEventListener: function () {} };
new Function('window', src)(g);
var C = g.MiTeaser.check;
var bad = [], n = 0;
function t(p, s, want) { n++; var r = C(p, s); if (r !== want) bad.push(JSON.stringify([p.a, s, r, want])); }
var N = function (a, extra) { return Object.assign({ a: String(a), t: 'n' }, extra || {}); };
/* number words */
t(N(19), 'nineteen', 'ok'); t(N(19), 'Nineteen.', 'ok'); t(N(19), 'It is nineteen', 'ok'); t(N(19), 'the answer is nineteen', 'ok');
t(N(19), 'eighteen', 'no'); t(N(19), 'ninety', 'no'); t(N(19), 'nineteenth', 'ok'); t(N(19), 'nine teen', 'no');
t(N(21), 'twenty-one', 'ok'); t(N(21), 'twenty one', 'ok'); t(N(21), 'twenty', 'no'); t(N(21), 'twenty-two', 'no'); t(N(21), 'twentyone', 'format');
t(N(105), 'one hundred and five', 'ok'); t(N(105), 'a hundred and five', 'ok'); t(N(105), 'one hundred five', 'ok'); t(N(105), 'one hundred and fifty', 'no');
t(N(3500000), 'three million five hundred thousand', 'ok'); t(N(3500000), 'three million', 'no');
t(N(2200), 'two thousand two hundred', 'ok'); t(N(2200), 'two thousand twenty', 'no');
t(N(0), 'zero', 'ok'); t(N(7), 'seven', 'ok'); t(N(7), 'seven cm', 'no'); t(N(7, { u: ['cm', 'centimetres'] }), 'seven cm', 'ok'); t(N(7, { u: ['cm'] }), 'seven m', 'no');
t(N(25), 'twenty-fifth', 'ok'); t(N(25), 'the twenty-fifth', 'ok'); t(N(25), 'twenty-sixth', 'no');
/* dates: "the 25th", "13 December", "December 13th" */
var D = N(13, { dt: 1, mo: ['december'] });
t(D, '13', 'ok'); t(D, '13th', 'ok'); t(D, 'the 13th', 'ok'); t(D, 'on the 13th', 'ok'); t(D, '13 December', 'ok'); t(D, '13th December', 'ok'); t(D, '13th of December', 'ok');
t(D, 'the 13th of December', 'ok'); t(D, 'December 13', 'ok'); t(D, 'Dec 13th', 'ok'); t(D, 'on 13 Dec', 'ok'); t(D, '13 december.', 'ok'); t(D, 'it is the 13th of December', 'ok');
t(D, '14 December', 'no'); t(D, '13 January', 'no'); t(D, 'January 13', 'no'); t(D, '31 December', 'no'); t(D, 'the 14th', 'no'); t(D, 'December', 'format'); t(D, 'the thirteenth', 'ok'); t(D, 'thirteen December', 'ok'); t(D, 'twelve December', 'no');
var W = N(25, { dt: 1 });                                       /* a date of an unnamed month */
t(W, 'the 25th', 'ok'); t(W, '25th', 'ok'); t(W, '25 December', 'ok'); t(W, 'the 25th of March', 'ok'); t(W, 'the 26th', 'no'); t(W, '24 December', 'no');
var X = N(25);                                                  /* not a date puzzle: a month word is not a number */
t(X, '25 December', 'no'); t(X, 'the 25th', 'ok'); t(X, 'on the 25th', 'ok');
/* fractions and mixed numbers in words and symbols */
var H = N('1/2', { e: 1 });
t(H, 'half', 'ok'); t(H, 'a half', 'ok'); t(H, 'one half', 'ok'); t(H, '½', 'ok'); t(H, '0.5', 'ok'); t(H, '2/4', 'simplify'); t(H, 'one third', 'no'); t(H, 'two quarters', 'simplify'); t(H, 'a quarter', 'no');
var Q = N('11/2', { e: 1 });
t(Q, '5 1/2', 'ok'); t(Q, '5½', 'ok'); t(Q, '5 ½', 'ok'); t(Q, 'five and a half', 'ok'); t(Q, '11/2', 'ok'); t(Q, '5.5', 'ok'); t(Q, 'five and a quarter', 'no'); t(Q, '5¼', 'no'); t(Q, 'six and a half', 'no');
var T = N('2/3', { e: 1 });
t(T, 'two thirds', 'ok'); t(T, '2/3', 'ok'); t(T, 'three thirds', 'no'); t(T, 'two fifths', 'no'); t(T, '4/6', 'simplify');
t(N('3/4', { e: 1 }), 'three quarters', 'ok'); t(N('3/4', { e: 1 }), '¾', 'ok'); t(N('3/4', { e: 1 }), 'three fourths', 'ok'); t(N('3/4', { e: 1 }), 'one quarter', 'no');
/* old behaviour must not change */
t(N(12, { u: ['cm'] }), '12 cm', 'ok'); t(N(12), '12.0', 'ok'); t(N(12), '', 'empty'); t(N(12), 'It is', 'format'); t(N(12), '12a', 'no'); t(N(12), 'twelve', 'ok'); t(N(12), 'twelfth', 'ok');
t(N(96, { u: ['%'] }), '0.96', 'ok'); t(N(96, { u: ['%'] }), 'ninety-six', 'ok'); t(N(96, { u: ['%', 'percent'] }), 'ninety six percent', 'ok');
t(N(90, { u: ['minutes', 'min'] }), '1 h 30 min', 'ok'); t(N(90, { u: ['minutes', 'min'] }), 'ninety minutes', 'ok');
/* text answers: a sentence round the name */
var S = { a: 'farid', t: 's', o: ['siti', 'ravi', 'hui min'] };
t(S, 'Farid', 'ok'); t(S, 'farid.', 'ok'); t(S, 'It is Farid', 'ok'); t(S, 'Farid plays cricket', 'ok'); t(S, 'I think Farid does', 'ok'); t(S, 'FARID PLAYS CRICKET.', 'ok');
t(S, 'Siti', 'no'); t(S, 'Siti plays cricket', 'no'); t(S, 'Farid or Siti', 'no'); t(S, 'not Farid', 'no'); t(S, 'Farid does not play cricket', 'no'); t(S, 'Ravi plays cricket and Farid plays tennis', 'no');
t(S, 'far', 'no'); t(S, 'farida', 'no'); t(S, 'Hui Min plays cricket', 'no');
var QC = { a: 'quarter circle', t: 's', x: ['quarter-circle'], o: ['half circle', 'circle', 'triangle'] };
t(QC, 'a quarter circle', 'ok'); t(QC, 'quarter-circle', 'ok'); t(QC, 'It is a quarter circle', 'ok'); t(QC, 'a circle', 'no'); t(QC, 'half circle', 'no'); t(QC, 'the shape is a quarter circle', 'ok'); t(QC, 'triangle', 'no');
var SU = { a: 'sunday', t: 's', o: ['monday', 'friday'] };
t(SU, 'Sunday', 'ok'); t(SU, 'on Sunday', 'ok'); t(SU, 'It is on Sunday', 'ok'); t(SU, 'monday', 'no'); t(SU, 'Sunday or Monday', 'no'); t(SU, 'sun', 'no');
/* lettered choices: (A) north (B) east (C) south (D) west */
var L = { a: 'south', t: 's', ch: ['north', 'east', 'south', 'west'], l: 1, o: ['north', 'east', 'west'] };
t(L, 'C', 'ok'); t(L, 'c', 'ok'); t(L, '(c)', 'ok'); t(L, 'c.', 'ok'); t(L, 'option C', 'ok'); t(L, 'south', 'ok'); t(L, 'South.', 'ok'); t(L, 'It is south', 'ok');
t(L, 'B', 'no'); t(L, 'D', 'no'); t(L, '(a)', 'no'); t(L, 'east', 'no'); t(L, 'e', 'no'); t(L, 'f', 'no');
var L2 = { a: 'south', t: 's', ch: ['north', 'east', 'south', 'west'], o: ['north', 'east', 'west'] };      /* options not lettered: a letter is not an answer */
t(L2, 'C', 'no'); t(L2, 'south', 'ok');
console.log(n + ' answer-matcher checks, ' + bad.length + ' failed');
bad.forEach(function (b) { console.log('  FAIL ' + b); });
process.exit(bad.length ? 1 : 0);
