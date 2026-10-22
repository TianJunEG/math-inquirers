// node --test portal/tests/functions.test.mjs   (Node 20+). HitPay and Supabase are mocked by replacing globalThis.fetch.
import test from 'node:test';
import assert from 'node:assert/strict';
import { createHmac } from 'node:crypto';
import { onRequestPost as create } from '../functions/api/hitpay-create.js';
import { onRequestPost as webhook } from '../functions/api/hitpay-webhook.js';
import { legacyPayload } from '../functions/lib.js';

const ENV = { SUPABASE_URL: 'https://x.supabase.co', SUPABASE_ANON_KEY: 'anon', SUPABASE_SERVICE_ROLE_KEY: 'service', HITPAY_API_KEY: 'hp-key', HITPAY_SALT: 'salty', SITE_URL: 'https://mathinquirers.example/' };
const E1 = '11111111-1111-4111-8111-111111111111', USER = '22222222-2222-4222-8222-222222222222';
const realFetch = globalThis.fetch;
let calls, rpcReplies;
function mockFetch({ user = { id: USER }, hitpay = { id: 'REQ9', url: 'https://securecheckout.sandbox.hit-pay.com/pay/REQ9' }, hpStatus = 200, rpcFail = false } = {}) {
  calls = [];
  globalThis.fetch = async (url, init = {}) => {
    const body = init.body ? JSON.parse(init.body) : null;
    calls.push({ url: String(url), init, body });
    url = String(url);
    const ok = (o, s = 200) => new Response(JSON.stringify(o), { status: s });
    if (url.endsWith('/auth/v1/user')) return user ? ok(user) : ok({}, 401);
    if (url.includes('/rest/v1/rpc/')) {
      if (rpcFail) return ok({}, 500);
      const fn = url.split('/rpc/')[1];
      return ok(rpcReplies[fn] ?? null);
    }
    if (url.includes('/v1/payment-requests')) return ok(hitpay, hpStatus);
    throw new Error('unexpected fetch ' + url);
  };
}
test.afterEach(() => { globalThis.fetch = realFetch; });
const req = (body, headers = {}) => new Request('https://s/api/x', { method: 'POST', headers: { 'Content-Type': 'application/json', ...headers }, body: typeof body === 'string' ? body : JSON.stringify(body) });
const pendingRow = { amount_cents: 25000, reference: 'MI-ABC234', payment_status: 'pending', enrolment_status: 'pending_payment', parent_email: 'p@x.com', parent_name: 'P' };

test('create: refuses without env, token, valid user, or valid id', async () => {
  assert.equal((await create({ request: req({}), env: {} })).status, 500);
  mockFetch(); assert.equal((await create({ request: req({ enrolment_id: E1 }), env: ENV })).status, 401);
  mockFetch({ user: null }); assert.equal((await create({ request: req({ enrolment_id: E1 }, { Authorization: 'Bearer bad' }), env: ENV })).status, 401);
  mockFetch(); assert.equal((await create({ request: req({ enrolment_id: 'nope' }, { Authorization: 'Bearer t' }), env: ENV })).status, 400);
  assert.equal((await create({ request: req('not json', { Authorization: 'Bearer t' }), env: ENV })).status, 400);
});
test('create: someone else\'s or unknown enrolment -> 404; already paid -> 409', async () => {
  rpcReplies = { service_begin_hitpay: [] }; mockFetch();
  assert.equal((await create({ request: req({ enrolment_id: E1 }, { Authorization: 'Bearer t' }), env: ENV })).status, 404);
  rpcReplies = { service_begin_hitpay: [{ ...pendingRow, payment_status: 'paid' }] }; mockFetch();
  assert.equal((await create({ request: req({ enrolment_id: E1 }, { Authorization: 'Bearer t' }), env: ENV })).status, 409);
  assert.ok(!calls.some((c) => c.url.includes('payment-requests')), 'HitPay not called');
});
test('create: success uses DB amount, enrolment id as reference, sandbox host, service key only for rpc', async () => {
  rpcReplies = { service_begin_hitpay: [pendingRow], service_attach_hitpay: null }; mockFetch();
  const r = await create({ request: req({ enrolment_id: E1, amount: 1 }, { Authorization: 'Bearer t' }), env: ENV });
  assert.equal(r.status, 200); assert.match((await r.json()).url, /hit-pay\.com/);
  const hp = calls.find((c) => c.url.includes('payment-requests'));
  assert.equal(hp.url, 'https://api.sandbox.hit-pay.com/v1/payment-requests');
  assert.equal(hp.init.headers['X-BUSINESS-API-KEY'], 'hp-key');
  assert.equal(hp.body.amount, '250.00'); assert.equal(hp.body.currency, 'SGD'); assert.equal(hp.body.reference_number, E1);
  assert.equal(hp.body.redirect_url, `https://mathinquirers.example/portal/?paid=${E1}`);
  assert.equal(hp.body.webhook, 'https://mathinquirers.example/api/hitpay-webhook');
  const begin = calls.find((c) => c.url.endsWith('service_begin_hitpay'));
  assert.deepEqual(begin.body, { p_enrolment: E1, p_parent: USER });
  assert.equal(calls.find((c) => c.url.endsWith('service_attach_hitpay')).body.p_request_id, 'REQ9');
  // live only when asked
  mockFetch(); await create({ request: req({ enrolment_id: E1 }, { Authorization: 'Bearer t' }), env: { ...ENV, HITPAY_ENV: 'live' } });
  assert.ok(calls.find((c) => c.url.includes('payment-requests')).url.startsWith('https://api.hit-pay.com/'));
});
test('create: HitPay failure -> 502 without leaking details', async () => {
  rpcReplies = { service_begin_hitpay: [pendingRow] }; mockFetch({ hpStatus: 422 });
  const r = await create({ request: req({ enrolment_id: E1 }, { Authorization: 'Bearer t' }), env: ENV });
  assert.equal(r.status, 502); assert.ok(!JSON.stringify(await r.json()).includes('hp-key'));
});

const payload = (o = {}) => JSON.stringify({ id: 'REQ9', status: 'completed', amount: '250.00', currency: 'SGD', reference_number: E1, payments: [{ id: 'PAY1', status: 'succeeded', payment_type: 'paynow_online' }], ...o });
const sign = (raw, salt = ENV.HITPAY_SALT) => createHmac('sha256', salt).update(raw).digest('hex');
const hook = (raw, sig, extra = {}) => new Request('https://s/api/hitpay-webhook', { method: 'POST', headers: { 'Content-Type': 'application/json', ...(sig ? { 'Hitpay-Signature': sig } : {}), ...extra }, body: raw });

test('webhook: bad / missing / wrong-salt signature -> 401 and no DB call', async () => {
  rpcReplies = { service_mark_hitpay_paid: 'paid' }; mockFetch();
  const raw = payload();
  assert.equal((await webhook({ request: hook(raw, 'deadbeef'), env: ENV })).status, 401);
  assert.equal((await webhook({ request: hook(raw, null), env: ENV })).status, 401);
  assert.equal((await webhook({ request: hook(raw, sign(raw, 'other-salt')), env: ENV })).status, 401);
  assert.equal((await webhook({ request: hook(raw, 'zz'), env: ENV })).status, 401);
  assert.equal((await webhook({ request: hook(raw + ' ', sign(raw)), env: ENV })).status, 401, 'tampered body');
  assert.equal(calls.length, 0);
});
test('webhook: valid completed payment marks paid with cents; replay is harmless', async () => {
  rpcReplies = { service_mark_hitpay_paid: 'paid' }; mockFetch();
  const raw = payload();
  const r = await webhook({ request: hook(raw, sign(raw)), env: ENV });
  assert.equal(r.status, 200); assert.equal((await r.json()).result, 'paid');
  assert.deepEqual(calls[0].body, { p_enrolment: E1, p_request_id: 'REQ9', p_payment_id: 'PAY1', p_amount_cents: 25000 });
  assert.equal(calls[0].init.headers.Authorization, 'Bearer service');
  rpcReplies = { service_mark_hitpay_paid: 'already_paid' };
  assert.equal((await webhook({ request: hook(raw, sign(raw)), env: ENV })).status, 200);
});
test('webhook: non-completed, bad reference, wrong currency are acknowledged but ignored', async () => {
  rpcReplies = { service_mark_hitpay_paid: 'paid' }; mockFetch();
  for (const o of [{ status: 'pending' }, { reference_number: 'not-a-uuid' }, { currency: 'USD' }, { amount: 'abc' }]) {
    const raw = payload(o); const r = await webhook({ request: hook(raw, sign(raw)), env: ENV });
    assert.equal(r.status, 200); assert.ok((await r.json()).ignored);
  }
  assert.equal(calls.length, 0);
});
test('webhook: amount mismatch is reported, not marked; DB outage -> 502 so HitPay retries', async () => {
  rpcReplies = { service_mark_hitpay_paid: 'amount_mismatch' }; mockFetch();
  const raw = payload({ amount: '1.00' });
  const r = await webhook({ request: hook(raw, sign(raw)), env: ENV });
  assert.equal(calls[0].body.p_amount_cents, 100); assert.equal((await r.json()).result, 'amount_mismatch');
  mockFetch({ rpcFail: true });
  assert.equal((await webhook({ request: hook(payload(), sign(payload())), env: ENV })).status, 502);
});
test('webhook: legacy form-encoded scheme with hmac field', async () => {
  rpcReplies = { service_mark_hitpay_paid: 'paid' }; mockFetch();
  const p = { payment_id: 'PAY2', payment_request_id: 'REQ9', phone: '', amount: '250.00', currency: 'SGD', status: 'completed', reference_number: E1 };
  const hmac = sign(legacyPayload(p));
  const mk = (h) => new Request('https://s/w', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ ...p, hmac: h }).toString() });
  assert.equal((await webhook({ request: mk(hmac), env: ENV })).status, 200);
  assert.equal(calls[0].body.p_payment_id, 'PAY2');
  assert.equal((await webhook({ request: mk('00'.repeat(32)), env: ENV })).status, 401);
});
test('webhook: missing env -> 500', async () => {
  assert.equal((await webhook({ request: hook('{}', 'aa'), env: {} })).status, 500);
});
