// node practice/submit/mark.test.mjs   (no dependencies)
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
const { mark } = createRequire(import.meta.url)('./mark.js');
let n = 0; const t = (name, rec, v, want, extra) => { const r = mark(rec, v); assert.equal(r.mark, want, name + ': got ' + JSON.stringify(r)); if (extra) assert.deepEqual({ ...r, mark: undefined }, { ...extra, mark: undefined }, name + ' detail'); n++; };
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
// the shared reading code is the same text in sheet.js and mark.js (they must agree on every answer)
import { readFileSync } from 'node:fs';
const blk = f => { const x = readFileSync(new URL(f, import.meta.url), 'utf8'); const a = x.indexOf('// BEGIN SHARED'), b = x.indexOf('// END SHARED'); assert.ok(a > 0 && b > a, f + ' has the shared block'); return x.slice(a, b); };
assert.equal(blk('./mark.js'), blk('../ext/public/sheet.js'), 'shared reading code differs between mark.js and sheet.js'); n++;

assert.throws(() => mark({ marking_mode: 'auto', type: 'bogus', key: 1 }, 'x')); n++;
console.log('mark.test.mjs: ' + n + ' checks passed');
