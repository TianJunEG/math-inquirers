// node --test portal/tests/functions.test.mjs   (Node 20+). Stripe and Supabase are mocked by replacing globalThis.fetch.
// No network, no real keys: every secret below is a made-up test string.
import test from 'node:test';
import assert from 'node:assert/strict';
import { createHmac } from 'node:crypto';
import { onRequestPost as create } from '../functions/api/stripe-create-checkout.js';
import { onRequestPost as webhook } from '../functions/api/stripe-webhook.js';
import { verifyStripeSignature, stripeBody, timingSafeEqual } from '../functions/lib.js';

const ENV = { SUPABASE_URL: 'https://x.supabase.co', SUPABASE_ANON_KEY: 'anon', SUPABASE_SERVICE_ROLE_KEY: 'service', STRIPE_SECRET_KEY: 'sk_test_fake', STRIPE_WEBHOOK_SECRET: 'whsec_fake', SITE_URL: 'https://mathinquirers.example/' };
const E1 = '11111111-1111-4111-8111-111111111111', USER = '22222222-2222-4222-8222-222222222222', P1 = '33333333-3333-4333-8333-333333333333';
const realFetch = globalThis.fetch;
let calls, rpcReplies;
function mockFetch({ user = { id: USER }, stripe = { id: 'cs_test_9', url: 'https://checkout.stripe.com/c/pay/cs_test_9' }, stStatus = 200, rpcFail = false } = {}) {
  calls = [];
  globalThis.fetch = async (url, init = {}) => {
    url = String(url);
    const isForm = (init.headers || {})['Content-Type'] === 'application/x-www-form-urlencoded';
    const body = init.body ? (isForm ? Object.fromEntries(new URLSearchParams(init.body)) : JSON.parse(init.body)) : null;
    calls.push({ url, init, body });
    const ok = (o, s = 200) => new Response(JSON.stringify(o), { status: s });
    if (url.endsWith('/auth/v1/user')) return user ? ok(user) : ok({}, 401);
    if (url.includes('/rest/v1/rpc/')) { if (rpcFail) return ok({}, 500); return ok(rpcReplies[url.split('/rpc/')[1]] ?? null); }
    if (url === 'https://api.stripe.com/v1/checkout/sessions') return ok(stripe, stStatus);
    throw new Error('unexpected fetch ' + url);
  };
}
test.afterEach(() => { globalThis.fetch = realFetch; });
const req = (body, headers = {}) => new Request('https://s/api/x', { method: 'POST', headers: { 'Content-Type': 'application/json', ...headers }, body: typeof body === 'string' ? body : JSON.stringify(body) });
const row = { payment_id: P1, amount_cents: 25000, currency: 'SGD', group_fee_cents: 25000, group_name: 'Level 1 · Group A', reference: 'MI-ABC234', payment_status: 'pending', enrolment_status: 'pending_payment', parent_email: 'p@x.com', parent_name: 'P', attempt: 0 };
const AUTH = { Authorization: 'Bearer t' };

// ---------- signature verification ----------
const NOW = 1_800_000_000;
const sig = (raw, t = NOW, secret = ENV.STRIPE_WEBHOOK_SECRET) => `t=${t},v1=${createHmac('sha256', secret).update(`${t}.${raw}`).digest('hex')}`;

test('signature: valid, multiple v1 values, unknown schemes ignored', async () => {
  const raw = '{"a":1}';
  assert.deepEqual(await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, sig(raw), NOW), { ok: true });
  assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, sig(raw) + ',v1=' + '00'.repeat(32) + ',v0=abc', NOW)).ok, true);
  assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, `v1=${'00'.repeat(32)},` + sig(raw), NOW)).ok, true, 'any matching v1');
});
test('signature: wrong secret, tampered body, malformed or missing header', async () => {
  const raw = '{"a":1}';
  assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, sig(raw, NOW, 'whsec_other'), NOW)).reason, 'mismatch');
  assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw + ' ', sig(raw), NOW)).reason, 'mismatch');
  for (const h of ['', null, undefined, 'garbage', 't=abc,v1=00', `t=${NOW}`, `v1=${'00'.repeat(32)}`]) assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, h, NOW)).ok, false);
  assert.equal((await verifyStripeSignature('', raw, sig(raw), NOW)).ok, false, 'no secret configured');
});
test('signature: stale timestamp (replay of an old capture) and far-future timestamp are rejected; 5 minute edge is accepted', async () => {
  const raw = '{"a":1}';
  assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, sig(raw, NOW - 301), NOW)).reason, 'stale');
  assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, sig(raw, NOW + 301), NOW)).reason, 'stale');
  assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, sig(raw, NOW - 300), NOW)).ok, true);
  // a valid signature cannot be re-stamped with a fresh time
  const old = sig(raw, NOW - 1000); const restamped = old.replace(`t=${NOW - 1000}`, `t=${NOW}`);
  assert.equal((await verifyStripeSignature(ENV.STRIPE_WEBHOOK_SECRET, raw, restamped, NOW)).reason, 'mismatch');
});
test('helpers: timingSafeEqual and stripeBody bracket encoding', () => {
  assert.ok(timingSafeEqual('abc', 'abc')); assert.ok(!timingSafeEqual('abc', 'abd')); assert.ok(!timingSafeEqual('abc', 'abcd'));
  const b = new URLSearchParams(stripeBody({ a: ['x', 'y'], b: { c: 1, d: [{ e: 2 }] }, z: undefined }));
  assert.deepEqual(Object.fromEntries(b), { 'a[0]': 'x', 'a[1]': 'y', 'b[c]': '1', 'b[d][0][e]': '2' });
});

// ---------- create checkout ----------
test('create: refuses without env, token, valid user, or valid id', async () => {
  assert.equal((await create({ request: req({}), env: {} })).status, 500);
  mockFetch(); assert.equal((await create({ request: req({ enrolment_id: E1 }), env: ENV })).status, 401);
  mockFetch({ user: null }); assert.equal((await create({ request: req({ enrolment_id: E1 }, { Authorization: 'Bearer bad' }), env: ENV })).status, 401);
  mockFetch(); assert.equal((await create({ request: req({ enrolment_id: 'nope' }, AUTH), env: ENV })).status, 400);
  assert.equal((await create({ request: req('not json', AUTH), env: ENV })).status, 400);
});
test('create: someone else\'s or unknown enrolment -> 404; already paid -> 409; Stripe not called', async () => {
  rpcReplies = { service_begin_payment: [] }; mockFetch();
  assert.equal((await create({ request: req({ enrolment_id: E1 }, AUTH), env: ENV })).status, 404);
  rpcReplies = { service_begin_payment: [{ ...row, payment_status: 'paid' }] }; mockFetch();
  assert.equal((await create({ request: req({ enrolment_id: E1 }, AUTH), env: ENV })).status, 409);
  rpcReplies = { service_begin_payment: [{ ...row, currency: 'USD' }] }; mockFetch();
  assert.equal((await create({ request: req({ enrolment_id: E1 }, AUTH), env: ENV })).status, 409);
  assert.ok(!calls.some((c) => c.url.includes('stripe.com')));
});
test('create: success uses DB amount (ignores browser amount), SGD, card+paynow, client_reference_id, idempotency key, secret only in header', async () => {
  rpcReplies = { service_begin_payment: [row], service_attach_session: null }; mockFetch();
  const r = await create({ request: req({ enrolment_id: E1, amount: 1 }, AUTH), env: ENV });
  assert.equal(r.status, 200); assert.match((await r.json()).url, /^https:\/\/checkout\.stripe\.com\//);
  const st = calls.find((c) => c.url.includes('stripe.com'));
  assert.equal(st.init.headers.Authorization, 'Bearer sk_test_fake');
  assert.equal(st.init.headers['Idempotency-Key'], `mi-checkout-${P1}-0`);
  const b = st.body;
  assert.equal(b.mode, 'payment'); assert.equal(b['line_items[0][price_data][currency]'], 'sgd'); assert.equal(b['line_items[0][price_data][unit_amount]'], '25000');
  assert.equal(b['line_items[0][quantity]'], '1'); assert.equal(b['payment_method_types[0]'], 'paynow'); assert.equal(b['payment_method_types[1]'], 'card');
  assert.equal(b.client_reference_id, P1); assert.equal(b['metadata[enrolment_id]'], E1); assert.equal(b['metadata[payment_id]'], P1);
  assert.equal(b.success_url, `https://mathinquirers.example/portal/?paid=${E1}&session_id={CHECKOUT_SESSION_ID}`);
  assert.equal(b.cancel_url, `https://mathinquirers.example/portal/?cancelled=${E1}`);
  assert.ok(!JSON.stringify(calls.filter((c) => !c.url.includes('stripe.com'))).includes('sk_test_fake'), 'Stripe key never sent to Supabase');
  assert.deepEqual(calls.find((c) => c.url.endsWith('service_begin_payment')).body, { p_enrolment: E1, p_parent: USER });
  assert.deepEqual(calls.find((c) => c.url.endsWith('service_attach_session')).body, { p_payment: P1, p_session_id: 'cs_test_9' });
  // a retry after an expired session uses a new key
  rpcReplies = { service_begin_payment: [{ ...row, attempt: 2 }] }; mockFetch();
  await create({ request: req({ enrolment_id: E1 }, AUTH), env: ENV });
  assert.equal(calls.find((c) => c.url.includes('stripe.com')).init.headers['Idempotency-Key'], `mi-checkout-${P1}-2`);
});
test('create: Stripe failure -> 502 without leaking details; odd checkout url rejected', async () => {
  rpcReplies = { service_begin_payment: [row] }; mockFetch({ stStatus: 400 });
  const r = await create({ request: req({ enrolment_id: E1 }, AUTH), env: ENV });
  assert.equal(r.status, 502); assert.ok(!JSON.stringify(await r.json()).includes('sk_test'));
  mockFetch({ stripe: { id: 'cs_x', url: 'https://evil.example/pay' } });
  assert.equal((await create({ request: req({ enrolment_id: E1 }, AUTH), env: ENV })).status, 502);
});

// ---------- webhook ----------
const session = (o = {}) => ({ id: 'cs_test_9', object: 'checkout.session', mode: 'payment', payment_status: 'paid', amount_total: 25000, currency: 'sgd', client_reference_id: P1, payment_intent: 'pi_9', metadata: { payment_id: P1, enrolment_id: E1 }, ...o });
const evt = (type = 'checkout.session.completed', o = {}) => JSON.stringify({ id: 'evt_1', object: 'event', type, data: { object: session(o) } });
const hook = (raw, header) => new Request('https://s/api/stripe-webhook', { method: 'POST', headers: { 'Content-Type': 'application/json', ...(header ? { 'Stripe-Signature': header } : {}) }, body: raw });
const fresh = (raw) => sig(raw, Math.floor(Date.now() / 1000));
const rpcCalls = () => calls.filter((c) => c.url.includes('/rpc/'));

test('webhook: bad / missing / wrong-secret / stale signature -> 400 and no DB call', async () => {
  rpcReplies = { service_mark_paid: 'paid' }; mockFetch();
  const raw = evt();
  assert.equal((await webhook({ request: hook(raw, 't=1,v1=dead'), env: ENV })).status, 400);
  assert.equal((await webhook({ request: hook(raw, null), env: ENV })).status, 400);
  assert.equal((await webhook({ request: hook(raw, sig(raw, Math.floor(Date.now() / 1000), 'whsec_other')), env: ENV })).status, 400);
  assert.equal((await webhook({ request: hook(raw, sig(raw, Math.floor(Date.now() / 1000) - 3600)), env: ENV })).status, 400, 'replayed old capture');
  assert.equal((await webhook({ request: hook(raw + ' ', fresh(raw)), env: ENV })).status, 400, 'tampered body');
  assert.equal(calls.length, 0);
});
test('webhook: completed + paid marks paid with cents, currency, session and intent; service key used', async () => {
  rpcReplies = { service_mark_paid: 'paid' }; mockFetch();
  const raw = evt(); const r = await webhook({ request: hook(raw, fresh(raw)), env: ENV });
  assert.equal(r.status, 200); assert.equal((await r.json()).result, 'paid');
  assert.deepEqual(calls[0].body, { p_payment: P1, p_session_id: 'cs_test_9', p_payment_intent: 'pi_9', p_amount_cents: 25000, p_currency: 'sgd' });
  assert.equal(calls[0].init.headers.Authorization, 'Bearer service');
});
test('webhook: idempotent: same event delivered twice and async_payment_succeeded after completed are both 200', async () => {
  rpcReplies = { service_mark_paid: 'paid' }; mockFetch();
  const raw = evt(); assert.equal((await webhook({ request: hook(raw, fresh(raw)), env: ENV })).status, 200);
  rpcReplies = { service_mark_paid: 'already_paid' };
  const r = await webhook({ request: hook(raw, fresh(raw)), env: ENV });
  assert.equal(r.status, 200); assert.equal((await r.json()).result, 'already_paid');
  const raw2 = evt('checkout.session.async_payment_succeeded');
  assert.equal((await webhook({ request: hook(raw2, fresh(raw2)), env: ENV })).status, 200);
});
test('webhook: PayNow completed but unpaid waits; async_payment_succeeded then marks paid', async () => {
  rpcReplies = { service_mark_paid: 'paid' }; mockFetch();
  const raw = evt('checkout.session.completed', { payment_status: 'unpaid' });
  const r = await webhook({ request: hook(raw, fresh(raw)), env: ENV });
  assert.equal(r.status, 200); assert.equal((await r.json()).ignored, 'awaiting payment'); assert.equal(calls.length, 0);
  const raw2 = evt('checkout.session.async_payment_succeeded');
  assert.equal((await (await webhook({ request: hook(raw2, fresh(raw2)), env: ENV })).json()).result, 'paid');
  assert.equal(rpcCalls().length, 1);
});
test('webhook: expired and async_payment_failed reset the session, never mark paid', async () => {
  rpcReplies = { service_mark_session_failed: 'reset' }; mockFetch();
  for (const t of ['checkout.session.expired', 'checkout.session.async_payment_failed']) {
    const raw = evt(t, { payment_status: 'unpaid' }); const r = await webhook({ request: hook(raw, fresh(raw)), env: ENV });
    assert.equal(r.status, 200); assert.equal((await r.json()).result, 'reset');
  }
  assert.ok(rpcCalls().every((c) => c.url.endsWith('service_mark_session_failed')));
  assert.deepEqual(calls[0].body, { p_payment: P1, p_session_id: 'cs_test_9' });
});
test('webhook: other events, subscription mode, bad reference, bad amount are acknowledged but ignored', async () => {
  rpcReplies = { service_mark_paid: 'paid' }; mockFetch();
  const cases = [evt('charge.refunded'), evt('payment_intent.created'), evt('checkout.session.completed', { mode: 'subscription' }),
    evt('checkout.session.completed', { client_reference_id: 'nope', metadata: {} }), evt('checkout.session.completed', { amount_total: 0 }), evt('checkout.session.completed', { amount_total: 'abc' })];
  for (const raw of cases) { const r = await webhook({ request: hook(raw, fresh(raw)), env: ENV }); assert.equal(r.status, 200); assert.ok((await r.json()).ignored); }
  assert.equal(calls.length, 0);
});
test('webhook: amount or currency mismatch is passed to the DB, which rejects it; reported as needing attention, still 200', async () => {
  for (const [o, res] of [[{ amount_total: 100 }, 'amount_mismatch'], [{ currency: 'usd' }, 'currency_mismatch']]) {
    rpcReplies = { service_mark_paid: res }; mockFetch();
    const raw = evt('checkout.session.completed', o); const r = await webhook({ request: hook(raw, fresh(raw)), env: ENV });
    assert.equal(r.status, 200); assert.equal((await r.json()).result, res);
    assert.equal(calls[0].body.p_amount_cents, o.amount_total ?? 25000); assert.equal(calls[0].body.p_currency, o.currency ?? 'sgd');
  }
});
test('webhook: DB outage -> 502 so Stripe retries; missing env -> 500', async () => {
  mockFetch({ rpcFail: true }); const raw = evt();
  assert.equal((await webhook({ request: hook(raw, fresh(raw)), env: ENV })).status, 502);
  assert.equal((await webhook({ request: hook('{}', 'aa'), env: {} })).status, 500);
});

test('webhook: duplicate_payment, not_payable and late payments are answered 200 (no Stripe retry loop) and logged for the owner', async () => {
  const errs = []; const realErr = console.error; console.error = (...a) => errs.push(a.join(' '));
  try {
    for (const res of ['duplicate_payment', 'not_payable:refunded', 'paid_enrolment_cancelled']) {
      rpcReplies = { service_mark_paid: res }; mockFetch();
      const raw = evt(); const r = await webhook({ request: hook(raw, fresh(raw)), env: ENV });
      assert.equal(r.status, 200); assert.equal((await r.json()).result, res);
    }
  } finally { console.error = realErr; }
  assert.equal(errs.filter((e) => e.includes('NEEDS OWNER ATTENTION')).length, 3);
});
