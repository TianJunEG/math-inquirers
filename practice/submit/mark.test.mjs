// node practice/submit/mark.test.mjs   (no dependencies)
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
const { mark } = createRequire(import.meta.url)('./mark.js');
let n = 0; const t = (name, rec, v, want, extra) => { const r = mark(rec, v); assert.equal(r.mark, want, name + ': got ' + JSON.stringify(r)); if (extra) assert.deepEqual({ ...r, mark: undefined }, { ...extra, mark: undefined }, name + ' detail'); n++; };
const num = { id: 'a', marking_mode: 'auto', type: 'number', key: 1000, slips: [{ a: [100], say: 'x' }] };
// whole number: wrong, right, forms, whitespace, skipped
t('right', num, '1000', 'right'); t('wrong', num, '999', 'wrong'); t('slip', num, '100', 'wrong', { slip: 0 });
t('thousands comma', num, '1,000', 'right'); t('spaces', num, '  1 000 ', 'right'); t('leading zero', num, '01000', 'right');
t('decimal in whole number item is wrong', num, '1000.0', 'wrong'); t('words are wrong', num, 'one thousand', 'wrong');
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
assert.throws(() => mark({ marking_mode: 'auto', type: 'bogus', key: 1 }, 'x')); n++;
console.log('mark.test.mjs: ' + n + ' checks passed');
