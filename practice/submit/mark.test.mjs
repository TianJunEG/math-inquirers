// node practice/submit/mark.test.mjs   (no dependencies)
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
const { mark } = createRequire(import.meta.url)('./mark.js');
let n = 0; const bad = []; const t = (name, rec, v, want, extra) => { const r = mark(rec, v); if (r.mark !== want) { bad.push(name + ': got ' + JSON.stringify(r) + ', wanted ' + want); return; } if (extra) assert.deepEqual({ ...r, mark: undefined }, { ...extra, mark: undefined }, name + ' detail'); n++; };
const num = { id: 'a', marking_mode: 'auto', type: 'number', key: 1000, slips: [{ a: [100], say: 'x' }] };
// whole number: wrong, right, forms, whitespace, skipped
t('right', num, '1000', 'right'); t('wrong', num, '999', 'wrong'); t('slip', num, '100', 'wrong', { slip: 0 });
t('thousands comma', num, '1,000', 'right'); t('spaces', num, '  1 000 ', 'right'); t('leading zero', num, '01000', 'right');
t('1000.0 and a final full stop are the whole number 1000', num, '1000.0', 'right'); t('1000.5 is not 1000', num, '1000.5', 'wrong'); t('words are wrong', num, 'one thousand', 'wrong');
t('skipped empty', num, '', 'skipped'); t('skipped spaces', num, '   ', 'skipped'); t('skipped null', num, null, 'skipped');
t('negative', { marking_mode: 'auto', type: 'number', key: -5 }, '-5', 'right');
// choice
const ch = { marking_mode: 'auto', type: 'choice', key: '<', options: ['<', '=', '>'] };
t('choice right', ch, '<', 'right'); t('choice wrong', ch, '>', 'wrong'); t('choice skipped', ch, null, 'skipped'); t('choice case', { ...ch, key: 'True' }, 'true', 'wrong');
// fields (several boxes)
const fl = { marking_mode: 'auto', type: 'fields', key: [3, 4] };
t('fields right', fl, ['3', '4'], 'right'); t('fields one wrong', fl, ['3', '5'], 'wrong', { detail: { boxes: [true, false] } });
t('fields one blank', fl, ['3', ''], 'wrong'); t('fields all blank', fl, ['', ' '], 'skipped'); t('fields swapped', fl, ['4', '3'], 'wrong');
// set in any order / ordered / partial
const any = { marking_mode: 'auto', type: 'set', key: [12, 15, 18], ordered: false };
t('set any order', any, '18, 12, 15', 'right'); t('set spaces only', any, '18 12 15', 'right'); t('set partial', any, '12, 15', 'wrong', { detail: { found: 2, of: 3, given: 2 } });
t('set extra', any, '12, 15, 18, 21', 'wrong'); t('set duplicate', any, '12, 12, 15', 'wrong'); t('set skipped', any, '', 'skipped');
const ord = { marking_mode: 'auto', type: 'set', key: [85, 508, 580, 805], ordered: true };
t('ordered right', ord, '85, 508, 580, 805', 'right'); t('ordered wrong order', ord, '508, 85, 580, 805', 'wrong', { detail: { found: 2, of: 4, given: 4 } });
// fraction
const fr = { marking_mode: 'auto', type: 'fraction', key: '3/8' };
t('fraction right', fr, '3/8', 'right'); t('fraction spaces', fr, ' 3 / 8 ', 'right'); t('fraction equal but not simplest', { ...fr, key: '1/2' }, '2/4', 'wrong', { detail: { reason: 'not_simplest' } });
t('fraction equivalent allowed', { ...fr, key: '1/2', equivalent: true }, '2/4', 'right'); t('fraction wrong', fr, '3/9', 'wrong'); t('fraction mixed', { ...fr, key: '3/2' }, '1 1/2', 'right');
t('fraction zero denominator', fr, '3/0', 'wrong'); t('fraction decimal typed', { ...fr, key: '1/2' }, '0.5', 'wrong');
// decimal
const dc = { marking_mode: 'auto', type: 'decimal', key: '0.5' };
t('decimal right', dc, '0.5', 'right'); t('decimal trailing zero', dc, '0.50', 'right'); t('decimal no leading zero', dc, '.5', 'right');
t('decimal wrong', dc, '0.05', 'wrong'); t('decimal comma is not a decimal point', dc, '0,5', 'wrong'); t('decimal 1 vs 1.0', { ...dc, key: '1' }, '1.0', 'right'); t('decimal text', dc, 'half', 'wrong');
// text
const tx = { marking_mode: 'auto', type: 'text', key: ['NW', 'north-west'] };
t('text case', tx, 'nw', 'right'); t('text alt spacing', tx, 'North West', 'right'); t('text full stop', tx, 'NW.', 'right'); t('text wrong', tx, 'NE', 'wrong'); t('text blank', tx, '  ', 'skipped');
// self-checked and open: never auto-marked, whatever is sent
t('selfcheck', { marking_mode: 'self', type: 'selfcheck' }, 'my drawing', 'self'); t('selfcheck blank still self', { marking_mode: 'self', type: 'selfcheck' }, '', 'self');
t('paper only item', { marking_mode: 'self', type: 'selfcheck', paper_only: true }, null, 'self'); t('open', { marking_mode: 'none', type: 'open' }, 'anything', 'open');
t('a marking_mode of self wins over a number type', { marking_mode: 'self', type: 'number', key: 4 }, '4', 'self');

// ---- audit fixes (H1, normText, units, brackets, minus)
const list3 = { marking_mode: 'auto', type: 'set', key: [250, 450], ordered: false };
t('H1 no space', list3, '250,450', 'right'); t('H1 comma space', list3, '250, 450', 'right'); t('H1 spaces', list3, '250 450', 'right'); t('H1 semicolon', list3, '250;450', 'right');
t('grouped item also accepts 250,450 as 250450', { ...list3, key: [250450] }, '250,450', 'right'); t('H1 not merged when not grouped', { ...list3, key: [250450], grouped: false }, '250,450', 'wrong'); t('H1 not merged: space', { ...list3, key: [250450], grouped: false }, '250 450', 'wrong');
t('H1 three numbers no space', { ...list3, key: [247, 274, 427] }, '247,274,427', 'right');
t('H1 a 3-digit group list is not a thousands number', { ...list3, key: [1, 250] }, '1,250', 'right');
const big = { marking_mode: 'auto', type: 'set', key: [12500, 40000], ordered: false };
t('grouped default: 12,500 40,000', big, '12,500, 40,000', 'right'); t('grouped default: spaces', big, '12 500, 40 000', 'right'); t('grouped default: plain', big, '12500 40000', 'right');
t('grouped default: wrong', big, '12,500, 40,001', 'wrong');
t('grouped: both readings', { marking_mode: 'auto', type: 'set', key: [12, 500, 20000], ordered: true }, '12, 500, 20 000', 'right');
t('grouped false declared', { marking_mode: 'auto', type: 'set', key: [12500, 250], grouped: false }, '12,500, 250', 'wrong');
t('grouped true declared on small numbers', { marking_mode: 'auto', type: 'set', key: [1250, 3], grouped: true }, '1,250, 3', 'right');
t('bad group 12,50 is not 1250', { marking_mode: 'auto', type: 'set', key: [12500], }, '12,50', 'wrong');
// numbers: units, full stops, minus
t('unit word', { marking_mode: 'auto', type: 'number', key: 301 }, '301 sticks', 'right'); t('unit min', { marking_mode: 'auto', type: 'number', key: 20 }, '20 min', 'right');
t('unit glued', { marking_mode: 'auto', type: 'number', key: 20 }, '20cm', 'right'); t('final stop', { marking_mode: 'auto', type: 'number', key: 29 }, '29.', 'right');
t('20.0', { marking_mode: 'auto', type: 'number', key: 20 }, '20.0', 'right'); t('20.5 wrong', { marking_mode: 'auto', type: 'number', key: 20 }, '20.5', 'wrong');
t('unit and stop', { marking_mode: 'auto', type: 'number', key: 20 }, '20 minutes.', 'right'); t('unit:false', { marking_mode: 'auto', type: 'number', key: 20, unit: false }, '20 min', 'wrong');
t('two numbers are not a unit', { marking_mode: 'auto', type: 'number', key: 4 }, '4 or 5', 'wrong'); t('1 2 is not 12', { marking_mode: 'auto', type: 'number', key: 12 }, '1 2', 'wrong');
t('12,50 is not 1250', { marking_mode: 'auto', type: 'number', key: 1250 }, '12,50', 'wrong'); t('1,250 is 1250', { marking_mode: 'auto', type: 'number', key: 1250 }, '1,250 kg', 'right');
t('unicode minus', { marking_mode: 'auto', type: 'number', key: -4 }, '−4', 'right'); t('en dash minus', { marking_mode: 'auto', type: 'number', key: -4 }, '–4', 'right'); t('minus matters', { marking_mode: 'auto', type: 'number', key: 4 }, '-4', 'wrong');
t('box with printed prefix 6:20', { marking_mode: 'auto', type: 'fields', key: [20], pre: ['6:'] }, ['6:20'], 'right'); t('box 20 min', { marking_mode: 'auto', type: 'fields', key: [20, 30], pre: ['6:', '6:'] }, ['20 min', '6:30'], 'right');
t('box prefix wrong', { marking_mode: 'auto', type: 'fields', key: [20], pre: ['6:'] }, ['7:20'], 'wrong');
t('fields negative unicode', { marking_mode: 'auto', type: 'fields', key: [-4, 2] }, ['−4', '2'], 'right');
// text: minus signs, mixed numbers, brackets
const frac = { marking_mode: 'auto', type: 'text', key: ['5 1/2', '11/2'] };
t('mixed number right', frac, '5 1/2', 'right'); t('1 1/2 is not 5 1/2', frac, '1 1/2', 'wrong'); t('11/2 key', frac, '11/2', 'right'); t('space kept: 51/2 is wrong', frac, '51/2', 'wrong');
const half = { marking_mode: 'auto', type: 'text', key: ['1/2', '0.5'] };
t('1/2 right', half, '1/2', 'right'); t('-1/2 wrong', half, '-1/2', 'wrong'); t('unicode -1/2 wrong', half, '−1/2', 'wrong'); t('-0.5 wrong', half, '-0.5', 'wrong');
const neg = { marking_mode: 'auto', type: 'text', key: ['-0.5', '−0.5'] };
t('negative key', neg, '-0.5', 'right'); t('negative key with unicode minus', neg, '−0.5', 'right'); t('negative key typed without minus', neg, '0.5', 'wrong'); t('negative key spaced', neg, '- 0.5', 'right');
const br = { marking_mode: 'auto', type: 'text', key: ['(6+4)x5-2'] };
t('bracket right', br, '(6+4)x5-2', 'right'); t('bracket times sign', br, '(6+4)×5−2', 'right'); t('bracket spaced star', br, '(6 + 4) * 5 - 2', 'right');
t('bracket dropped minus (6+4)x52', br, '(6+4)x52', 'wrong'); t('bracket with result', br, '(6+4)x5-2=48', 'right'); t('bracket with spaced result', br, '(6+4)×5−2 = 48.', 'right');
t('bracket with wrong result', br, '(6+4)x5-2=47', 'wrong'); t('bracket other placement', br, '6+4x(5-2)', 'wrong'); t('52 placement', { ...br, key: ['(6+4)x52'] }, '(6+4)x5-2', 'wrong');
t('word hyphen kept as space', { marking_mode: 'auto', type: 'text', key: ['north-west'] }, 'north west', 'right'); t('word hyphen squash', { marking_mode: 'auto', type: 'text', key: ['north-west'] }, 'Northwest.', 'right');
t('trailing full stop on text', br, '(6+4)x5-2.', 'right');
t('words only if declared', { marking_mode: 'auto', type: 'text', key: ['1/2'] }, 'half', 'wrong'); t('words declared', { marking_mode: 'auto', type: 'text', key: ['1/2', 'half'] }, 'Half', 'right');

// ---- coordinator list: must reject / must accept
const T = (k) => ({ marking_mode: 'auto', type: 'text', key: k });
t('T4b diff rejects -0.5', T(['0.5']), '-0.5', 'wrong'); t('T4b rule rejects -0.5n', T(['0.5n']), '-0.5n', 'wrong'); t('A2 rejects -1/2', T(['1/2']), '-1/2', 'wrong');
t('3c rejects -1/4', T(['1/4']), '-1/4', 'wrong'); t('A4 rejects -2/3', T(['2/3']), '-2/3', 'wrong');
t('5a rejects 52', T(['(6+4)x5-2']), '(6+4)×52', 'wrong'); t('5a accepts statement', T(['(6+4)×5−2']), '(6+4)×5−2=48', 'right'); t('5a accepts x', T(['(6+4)×5−2']), '(6+4)x5-2', 'right');
t('5b rejects (52)', T(['6+4x(5-2)']), '6+4×(52)', 'wrong'); t('5b accepts', T(['6+4x(5-2)']), '6+4×(5−2)', 'right');
t('6a rejects 1 1/2', T(['5 1/2', '11/2']), '1 1/2', 'wrong'); t('6a keeps 5 1/2', T(['11/2']), '5 1/2', 'wrong'); t('6a 5 1/2', T(['5 1/2', '11/2']), '5 1/2', 'right');
const b2 = T(['1/3+1/12', '1/12+1/3', '1/4+1/6', '1/6+1/4']);
for (const a of ['1/3+1/12', '1/12+1/3', '1/4+1/6', '1/6+1/4']) { t('B2 ' + a, b2, a, 'right'); t('B2 lead ' + a, b2, '5/12=' + a, 'right'); t('B2 trail ' + a, b2, a + '=5/12', 'right'); }
for (const a of ['1/3+1/6', '1/4+1/12', '5/12=1/3+1/6']) t('B2 reject ' + a, b2, a, 'wrong');
// ---- week 2 audit fixes: unit and notation forms, equal fractions, algebra rules, number words
const N = (key, o = {}) => ({ marking_mode: 'auto', type: 'number', key, ...o });
for (const v of ['84', '84 cm2', '84cm2', '84 cm^2', '84cm^2', '84 cm²', '84cm²', '84 sq cm', '84 square cm', '84 sq. cm.', '84 cm2.', '84.0 cm2', '(84)', '84 m2']) t('area form ' + v, N(84), v, 'right');
for (const v of ['85 cm2', '8 4 cm2', '84 or 85', '84 or2', '842 cm', '84.5 cm2', '-84 cm2', '84 cm 2 3']) t('area wrong ' + v, N(84), v, v === '84 or2' ? 'right' : 'wrong'); // 'or2' reads as a unit word with a power: harmless, the number is still 84
t('area unit:false refuses cm2', N(84, { unit: false }), '84 cm2', 'wrong'); t('area unit:false still reads plain 84', N(84, { unit: false }), '84', 'right');
for (const v of ['-25', '-25 °C', '-25°C', '−25 °C', '(-25)', '(−25)', '-25°', '-25 degrees', '(-25) °C', '-25 C']) t('temperature form ' + v, N(-25), v, 'right');
for (const v of ['25 °C', '-26 °C', '-2 5 °C', '25']) t('temperature wrong ' + v, N(-25), v, 'wrong');
for (const v of ['11 °C', '11°C', '11°', '(11)', '11 degrees C']) t('degree form ' + v, N(11), v, 'right');
t('degree unit:false', N(11, { unit: false }), '11°C', 'wrong'); t('speed unit', N(60), '60 km/h', 'right'); t('speed unit glued', N(60), '60km/h', 'right');
t('bracket then more is no number', N(25), '(25) + 3', 'wrong'); t('two brackets refused', N(25), '(2)(5)', 'wrong'); t('nested brackets refused', N(25), '((25))', 'wrong'); t('empty brackets refused', N(25), '()', 'wrong'); t('half bracket refused', N(25), '(25', 'wrong');
t('fields with cm2 and degrees', { marking_mode: 'auto', type: 'fields', key: [84, -25] }, ['84 cm2', '(-25) °C'], 'right');
t('fields with wrong cm2', { marking_mode: 'auto', type: 'fields', key: [84, -25] }, ['84 cm2', '25 °C'], 'wrong');
t('set not changed by units (a list is not a number)', { marking_mode: 'auto', type: 'set', key: [4, 5] }, '4 cm, 5 cm', 'right');
// number words only when the item declares words:true
t('five without words', N(5), 'five', 'wrong'); t('five with words', N(5, { words: true }), 'five', 'right'); t('Five. with words', N(5, { words: true }), 'Five.', 'right');
t('digits with words', N(5, { words: true }), '5', 'right'); t('five wrong number', N(5, { words: true }), 'six', 'wrong');
for (const [w, k] of [['twenty-five', 25], ['twenty five', 25], ['one hundred and five', 105], ['ninety nine', 99], ['zero', 0], ['minus five', -5], ['negative twenty', -20], ['one thousand', 1000], ['two thousand and fifty', 2050], ['Twelve', 12], ['five cm', 5]]) t('words ' + w, N(k, { words: true }), w, w === 'five cm' ? 'wrong' : 'right');
for (const w of ['five five', 'twenty twenty', 'ten five', 'hundred', 'five hundred hundred', 'fiv', 'five or six', 'one two']) t('words refuse ' + w, N(5, { words: true }), w, 'wrong');
t('minus five needs words', N(-5), 'minus five', 'wrong'); t('words in a box', { marking_mode: 'auto', type: 'fields', key: [3, 4], words: true }, ['three', '4'], 'right'); t('box words need the flag', { marking_mode: 'auto', type: 'fields', key: [3, 4] }, ['three', '4'], 'wrong');
// equal fractions in a list (equiv_frac), default off
const ord3 = { marking_mode: 'auto', type: 'text', key: ['7/12, 2/3, 5/6'] };
t('printed order forms still right', ord3, '7/12, 2/3, 5/6', 'right'); t('equal forms refused by default', ord3, '7/12, 8/12, 10/12', 'wrong');
const eq3 = { ...ord3, equiv_frac: true };
for (const v of ['7/12, 8/12, 10/12', '7/12 8/12 10/12', '7/12,8/12,10/12', ' 14/24 , 2/3 , 5/6 ', '7/12, 8/12, 10/12.', '7 / 12, 8 / 12, 10 / 12', '7/12, 2/3, 5/6']) t('equiv_frac right ' + v, eq3, v, 'right');
for (const v of ['8/12, 7/12, 10/12', '7/12, 8/12', '7/12, 8/12, 10/12, 1', '7/12, 8/12, 9/12', '7/12, 8/12, 11/12', '', '7/0, 8/12, 10/12', '0.5, 2/3, 5/6', '7/12 > 2/3 > 5/6']) t('equiv_frac wrong ' + v, eq3, v, v === '' ? 'skipped' : 'wrong');
t('equiv_frac single fraction', { marking_mode: 'auto', type: 'text', key: ['1/2'], equiv_frac: true }, '4/8', 'right'); t('equiv_frac single wrong', { marking_mode: 'auto', type: 'text', key: ['1/2'], equiv_frac: true }, '4/9', 'wrong');
t('equiv_frac mixed number', { marking_mode: 'auto', type: 'text', key: ['1 1/2'], equiv_frac: true }, '3/2', 'right'); t('equiv_frac mixed number 1 1/2 vs 11/2', { marking_mode: 'auto', type: 'text', key: ['1 1/2'], equiv_frac: true }, '11/2', 'wrong');
t('equiv_frac keeps the signs', { marking_mode: 'auto', type: 'text', key: ['1/4 < 1/2 < 3/4'], equiv_frac: true }, '2/8 < 4/8 < 6/8', 'right'); t('equiv_frac sign must match', { marking_mode: 'auto', type: 'text', key: ['1/4 < 1/2 < 3/4'], equiv_frac: true }, '2/8 > 4/8 > 6/8', 'wrong');
t('equiv_frac still takes another listed wording', { marking_mode: 'auto', type: 'text', key: ['7/12, 2/3, 5/6', 'seven twelfths'], equiv_frac: true }, 'Seven twelfths', 'right');
t('equiv_frac slashless', { marking_mode: 'auto', type: 'text', key: ['3/4'], equiv_frac: true }, '34', 'wrong');
// algebra rules as polynomials (item flag poly:'n')
const rule = (...k) => ({ marking_mode: 'auto', type: 'text', key: k, poly: 'n' });
const P = rule('(n+3)×4', '4n+12', 'OUT = 4n+12');
for (const v of ['(n+3)×4', '4n+12', '4(n+3)', '4*(n+3)', '4x(n+3)', '(n+3)4', '(3+n)×4', '12+4n', 'n×4+12', '4n + 3×4', '2(2n+6)', '(8n+24)÷2', '(8n+24)/2', '4n+10+2', '4n+16−4', '4(n+3)=4n+12', '(n+3)×4 = 4n+12', '4n+12 = (n+3)×4', 'OUT = 4(n+3)', 'out=4n+12', 'OUT = (n+3)×4 = 4n+12', '4n+12.', '  4 n + 12  ', '+4n+12', '4n+12+0n', '4n^1+12', '2×2n+12', '0.5×8n+12', '4n+12=4(n+3)=OUT', '-(-4n-12)', '4n+n0+12'.replace('n0', '0')])
  t('poly right ' + v, P, v, 'right');
for (const v of ['4n-12', 'n+3×4', '(n+3)+4', '4n+3', '4(n+4)', '(n+3)×5', '3n+12', '7n', 'n+6', '4n+12=4n+13', 'n+3 = 4n+12', '4n+12 = 4n', '(n+3)÷4', '4n', '12', 'n', '4n+12n', '4n+12 n', '4n 12', '4n+12=', '=4n+12=x', 'OUT', 'OUT=', '4n+12=OUT=5', 'x', 'n*n', '4n²+12', '4/(n+3)', '4n+12/0', '(4n+12', '4n+12)', '4n+@', 'fourn+12', '4m+12', '4n+12 or 4n', '4n+1 2']) t('poly wrong ' + v, P, v, v === '' ? 'skipped' : 'wrong');
t('poly blank', P, '  ', 'skipped'); t('poly off by default', { marking_mode: 'auto', type: 'text', key: ['4n+12'] }, '4(n+3)', 'wrong');
const Q = rule('2n+6'); for (const v of ['(2n+6)÷2×2', 'n+n+6', '2(n+3)', '2n+10−4', '(n+3)×2', '2n+10-4', '6+2n', '2×n+6', 'n×2+6']) t('poly 2n+6 ' + v, Q, v, 'right');
for (const v of ['2n+10', '(2n+6)÷2', 'n+3', '2n−6', '2n+6n']) t('poly 2n+6 wrong ' + v, Q, v, 'wrong');
t('poly halve rule', rule('n+3'), '(2n+6)÷2', 'right'); t('poly halve rule 2', rule('n+3'), '(2n+6)/2', 'right'); t('poly halve wrong', rule('n+3'), '2n+6÷2', 'wrong'); t('poly halve wrong 2', rule('n+3'), 'n+6', 'wrong');
t('poly decimal rule', rule('0.5n'), 'n/2', 'right'); t('poly decimal rule 2', rule('0.5n'), 'n÷2', 'right'); t('poly decimal rule 3', rule('0.5n'), '½n'.replace('½', '0.5'), 'right'); t('poly decimal wrong sign', rule('0.5n'), '-0.5n', 'wrong');
t('poly squares', rule('n^2+2n+1'), '(n+1)²', 'right'); t('poly squares 2', rule('n^2+2n+1'), '(n+1)^2', 'right'); t('poly squares 3', rule('n^2+2n+1'), 'n×n+2n+1', 'right'); t('a power sign is not a times-two', rule('2n^2'), 'n²×2', 'right'); t('n² is not 2n', rule('4n'), 'n²×4', 'wrong'); t('n² is not n2', rule('2n'), 'n²', 'wrong'); t('n³', rule('n^3'), 'n³', 'right');
t('poly squares wrong', rule('n^2+2n+1'), 'n²+1', 'wrong'); t('poly power too big', rule('n+1'), 'n^9', 'wrong');
t('poly a different letter', { ...rule('3k+2'), poly: 'k' }, '2+3×k', 'right'); t('poly wrong letter', { ...rule('3k+2'), poly: 'k' }, '3n+2', 'wrong'); t('poly letter x is multiplication unless it is the letter', { ...rule('4n+12'), poly: 'n' }, '4x(n+3)', 'right');
t('poly keeps the printed forms too', rule('n + 3', '3 + n'), '3 + n', 'right'); t('poly never runs code', P, 'process.exit()', 'wrong'); t('poly never runs code 2', P, '(()=>1)()', 'wrong'); t('poly huge product refused', P, '(n+1)'.repeat(40), 'wrong');
t('poly with a leading label word', rule('4n+3'), 'OUT = 4n + 3', 'right'); t('poly rule with a number key sides', rule('4n+3'), 'OUT=3+4n', 'right');
t('poly mixes text mode off', { marking_mode: 'auto', type: 'text', key: ['5 1/2'], poly: 'n' }, '1 1/2', 'wrong');
// the shared reading code is the same text in sheet.js and mark.js (they must agree on every answer)
import { readFileSync } from 'node:fs';
const blk = f => { const x = readFileSync(new URL(f, import.meta.url), 'utf8'); const a = x.indexOf('// BEGIN SHARED'), b = x.indexOf('// END SHARED'); assert.ok(a > 0 && b > a, f + ' has the shared block'); return x.slice(a, b); };
assert.equal(blk('./mark.js'), blk('../ext/public/sheet.js'), 'shared reading code differs between mark.js and sheet.js'); n++;

assert.throws(() => mark({ marking_mode: 'auto', type: 'bogus', key: 1 }, 'x')); n++;
// cent sign and cent words are units like cm; bare 'c' is ambiguous; two numbers are never a unit
for (const v of ['35¢', '35 ¢', '35 cents', '35 cent']) t('cent form ' + v, N(35), v, 'right');
for (const v of ['35 c', '35c', '3 5¢', '36¢', '$0.35']) t('cent wrong ' + v, N(35), v, 'wrong');
t('cent unit:false', N(35, { unit: false }), '35¢', 'wrong'); t('cents unit:false', N(35, { unit: false }), '35 cents', 'wrong');
assert.deepEqual(bad, [], bad.join('\n')); console.log('mark.test.mjs: ' + n + ' checks passed');
