// node practice/submit/handler.test.mjs : validation, re-marking (client claims ignored), idempotency, stale retry, privacy of free text.
import assert from 'node:assert/strict';
import { handle, validate, markAll, sha256Hex } from './handler.js';
import { memoryStore, KEYS } from './memory_store.mjs';
const TOKEN = 'T'.repeat(43), SID = '11111111-1111-4111-8111-111111111111';
const store = memoryStore({ tokenHash: await sha256Hex(TOKEN), consent: true });
const call = (body, o = {}) => handle(new Request('https://x.test/api/practice/submit', { method: o.method || 'POST', headers: { 'content-type': o.ct || 'application/json', authorization: o.auth ?? 'Bearer ' + TOKEN, ...(o.origin ? { origin: o.origin } : {}) }, ...(o.method === 'GET' ? {} : { body: o.raw ?? JSON.stringify(body) }) }), {}, store);
const base = { v: 1, unit: 'ext-l2u01', unit_version: 'v1', sid: SID, rev: 1, answers: {} };
let n = 0; const ok = (c, m) => { assert.ok(c, m); n++; };
// every client mark is ignored: sending client_marks claiming everything is right changes nothing
let r = await call({ ...base, answers: { q1: '7', q2: '1,000', q3: ['3', '9'], q4: '18, 12', q5: '>', q6: 'my text', q7: null }, self: { q8: 'got' }, client_marks: { q1: 'right', q2: 'right', q3: 'right' } });
let j = await r.json(); ok(r.status === 200 && j.ok, 'accepted');
const saved = store.data.get(SID);
const storedMarks = (e) => Object.fromEntries(e.rows.map((x) => [x.item_id, x.mark]));
assert.deepEqual(storedMarks(saved), { q1: 'wrong', q2: 'right', q3: 'wrong', q4: 'wrong', q5: 'right', q6: 'self', q7: 'skipped', q8: 'self', q9: 'skipped', q10: 'open' }); n++;
assert.deepEqual(saved.counts, { auto: 7, right: 2, wrong: 3, skipped: 2, self: 2, self_got: 1, open: 1 }); n++;
// R1-L4: the reply says only that it was stored; it carries no mark and no count, so resubmitting cannot be used to read the answer key
assert.deepEqual(Object.keys(j).sort(), ['duplicate', 'ok', 'rev', 'stale']); ok(!('marks' in j) && !('counts' in j) && !/right|wrong|skipped/.test(JSON.stringify(j)), 'reply holds no marks'); n++;
ok(saved.rows.find((x) => x.item_id === 'q1').slip_idx === 0, 'misconception slip matched on the server');
ok(saved.rows.find((x) => x.item_id === 'q3').partial_found === 1, 'one box of two right');
ok(saved.rows.find((x) => x.item_id === 'q4').partial_found === 2 && saved.rows.find((x) => x.item_id === 'q4').partial_of === 3, 'partial set');
ok(saved.rows.find((x) => x.item_id === 'q6').answer_text === null, 'free text of a self-checked item is not stored');
ok(saved.rows.find((x) => x.item_id === 'q10').answer_text === null, 'open item text not stored');
ok(saved.rows.find((x) => x.item_id === 'q8').self_result === 'got', 'self result kept');
// idempotent retry: same rev again -> duplicate, no second row
r = await call({ ...base, answers: { q1: '7' } }); j = await r.json(); ok(j.duplicate === true && store.data.size === 1, 'same rev is a duplicate (the first stays)');
assert.equal(saved.rev, 1); n++;
// later revision replaces; an older retry arriving late is ignored
r = await call({ ...base, rev: 3, answers: { q1: '9' } }); j = await r.json(); ok(j.rev === 3 && store.data.get(SID).rows.find((x) => x.item_id === 'q1').mark === 'right', 'rev 3 stored');
r = await call({ ...base, rev: 2, answers: { q1: '7' } }); j = await r.json(); ok(j.stale === true && store.data.get(SID).rev === 3, 'stale rev 2 ignored');
// rejected requests
const rej = async (body, o, status, word) => { const x = await call(body, o); const y = await x.json(); ok(x.status === status && y.error === word, `${word}: ${x.status} ${y.error}`); };
await rej(base, { auth: 'Bearer short' }, 401, 'session'); await rej(base, { auth: '' }, 401, 'session');
await rej(base, { method: 'GET' }, 405, 'method'); await rej(base, { ct: 'text/plain' }, 415, 'content_type');
await rej(base, { raw: '{bad' }, 400, 'json'); await rej(base, { origin: 'https://evil.test' }, 403, 'origin');
await rej({ ...base, answers: { zz: '1' } }, {}, 400, 'unknown_item'); await rej({ ...base, answers: { q1: 5 } }, {}, 400, 'answer_type');
await rej({ ...base, answers: { q1: 'x'.repeat(201) } }, {}, 400, 'too_long'); await rej({ ...base, rev: 0 }, {}, 400, 'rev');
await rej({ ...base, sid: 'nope' }, {}, 400, 'sid'); await rej({ ...base, extra: 1 }, {}, 400, 'unknown_field'); await rej({ ...base, unit: 'No Such!' }, {}, 400, 'unit');
await rej({ ...base, unit: 'ext-l9u99' }, {}, 404, 'unit'); await rej({ ...base, self: { q1: 'maybe' } }, {}, 400, 'self');
await rej({ ...base, answers: { ['i' + 'x'.repeat(41)]: '1' } }, {}, 400, 'item_id');
await rej({ ...base, answers: { q1: '1' }, pad: 'x'.repeat(70000) }, {}, 413, 'too_large');
// EXPLAIN-TO-TUTOR: the typed explanation of a self-check or open item is kept (trimmed, at most 500 characters), never for an auto-marked or paper-only item, never sent back
r = await call({ ...base, rev: 5, answers: { q1: '9', q6: '(written)', q10: '(written)' }, explain: { q6: '  Because 9 is one less than 10.  ', q10: 'x'.repeat(500), q1: 'sneaky', q8: 'a drawing note' } });
j = await r.json(); ok(r.status === 200 && j.ok, 'explain accepted');
const exrows = store.data.get(SID).rows, exrow = (id) => exrows.find((x) => x.item_id === id);
ok(exrow('q6').explain_text === 'Because 9 is one less than 10.', 'explanation trimmed and stored for a self-check item');
ok(exrow('q10').explain_text === 'x'.repeat(500), 'a 500 character explanation is kept whole for an open item');
ok(exrow('q1').explain_text === null && exrow('q8').explain_text === null && exrow('q2').explain_text === null, 'no explanation text for auto-marked, paper-only or absent items');
ok(exrow('q6').answer_text === null && exrow('q6').mark === 'self', 'the explanation is not an answer and never changes a mark');
ok(!JSON.stringify(j).includes('Because') && !('explain' in j) && !('marks' in j), 'the explanation is never in the reply');
ok(markAll(KEYS, {}, {}, { q6: '\u0000\u0007hi\u001f there' }).rows.find((x) => x.item_id === 'q6').explain_text === 'hi there', 'control characters removed');
ok(markAll(KEYS, {}, {}, { q6: '   ' }).rows.find((x) => x.item_id === 'q6').explain_text === null, 'blank explanation is null');
ok(validate({ ...base, explain: { q6: 'ok' } }) === null && validate({ ...base }) === null, 'validate: explain optional');
await rej({ ...base, rev: 6, explain: { q6: 'x'.repeat(501) } }, {}, 400, 'too_long'); await rej({ ...base, rev: 6, explain: { q6: 5 } }, {}, 400, 'explain');
await rej({ ...base, rev: 6, explain: ['a'] }, {}, 400, 'explain'); await rej({ ...base, rev: 6, explain: 'text' }, {}, 400, 'explain'); await rej({ ...base, rev: 6, explain: { 'bad id!': 'a' } }, {}, 400, 'explain');
await rej({ ...base, rev: 6, explain: { zz: 'a' } }, {}, 400, 'unknown_item');
await rej({ ...base, rev: 6, explain: Object.fromEntries(Array.from({ length: 61 }, (_, i) => ['e' + i, 'a'])) }, {}, 400, 'too_many');
assert.equal(store.data.get(SID).rev, 5); n++;   // none of the rejected ones was stored
// consent withdrawn / session expired in the store
store.consent = false; await rej({ ...base, sid: '22222222-2222-4222-8222-222222222222' }, {}, 403, 'consent'); store.consent = true;
store.rateLeft = 0; await rej({ ...base, sid: '33333333-3333-4333-8333-333333333333' }, {}, 429, 'rate'); store.rateLeft = 99;
assert.equal(store.data.size, 1); n++;   // nothing was stored by any rejected call
// a child never sends 'correct': the field is rejected outright
await rej({ ...base, correct: true }, {}, 400, 'unknown_field');
console.log('handler.test.mjs: ' + n + ' checks passed');
